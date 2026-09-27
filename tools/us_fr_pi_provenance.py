"""Collect Federal Register public-inspection dates and write auditable patches.

Run from the repository root: python tools/us_fr_pi_provenance.py
This reads the preserved US-FR executor rows; it does not edit them or rebuild data.
The PI date is an observed public-availability bound, not proof that the agency
did not release the document earlier. See the accompanying scope report.
"""

from __future__ import annotations

import concurrent.futures
import datetime as dt
import hashlib
import json
import re
import sys
import time
import urllib.error
import urllib.request
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw" / "us_fr"
AUDITS = ROOT / "data" / "audits"
PROVENANCE = AUDITS / "us_fr_pi_provenance_2026-09-27.jsonl"
PATCHES = AUDITS / "patches" / "us_fr_public_availability_2026-09-27.jsonl"
SCOPE = AUDITS / "us_fr_date_scope_2026-09-27.jsonl"
DOCNUM = re.compile(r"/documents/\d{4}/\d{2}/\d{2}/(\d{4}-\d{4,5})(?:/|$)")
CENSOR_DATE = "2026-09-24"

# Dated official EPA notices, checked separately from Federal Register PI.
# These affect only the two specified evidence rows, not all EPA rows.
EARLIER_AGENCY = {
    "US-FR-H-0002-E01": (
        "2019-06-25",
        "https://www.epa.gov/newsreleases/reducing-regulatory-burdens-epas-proposal-levels-playing-field-sources-reduce",
        "EPA's dated press release publicly announced this proposal on 2019-06-25.",
    ),
    "US-FR-C-0018-E01": (
        "2025-11-17",
        "https://www.epa.gov/newsreleases/epa-army-corps-unveil-clear-durable-wotus-proposal",
        "EPA's dated release publicly announced the proposed rule on 2025-11-17; its WOTUS page links proposal material.",
    ),
    "US-FR-C-0018-E02": (
        "2026-09-04",
        "https://www.epa.gov/newsreleases/epa-and-army-seek-additional-input-proposed-waters-us-definition-while-advancing",
        "EPA's dated release announced the supplemental proposal on 2026-09-04; EPA's WOTUS page links the prepublication proposal.",
    ),
}
EARLIER_OUTCOME = {
    "US-FR-H-0002": (
        "2020-10-01",
        "https://www.epa.gov/newsreleases/epa-encourages-innovation-levels-playing-field-sources-are-reducing-hazardous-air",
        "EPA's dated press release publicly announced finalization of this rule on 2020-10-01.",
    ),
}


def rows(path: Path) -> list[dict]:
    with path.open(encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def write_jsonl(path: Path, items: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as f:
        for item in items:
            f.write(json.dumps(item, ensure_ascii=False, sort_keys=True) + "\n")


def docnum(url: str | None) -> str | None:
    m = DOCNUM.search(url or "")
    return m.group(1) if m else None


def fetch(number: str) -> dict:
    url = f"https://www.federalregister.gov/api/v1/public-inspection-documents/{number}.json"
    last_error = None
    for attempt in range(3):
        try:
            request = urllib.request.Request(url, headers={"User-Agent": "regulator-predict-date-audit/1.0", "Accept": "application/json"})
            with urllib.request.urlopen(request, timeout=35) as response:
                raw = response.read()
                obj = json.loads(raw)
            if obj.get("document_number") != number:
                raise ValueError(f"unexpected document_number {obj.get('document_number')!r}")
            return {
                "source_kind": "federal_register_public_inspection_api",
                "document_number": number,
                "api_url": url,
                "http_status": 200,
                "response_sha256": hashlib.sha256(raw).hexdigest(),
                "filed_at": obj.get("filed_at"),
                "filing_type": obj.get("filing_type"),
                "last_public_inspection_issue": obj.get("last_public_inspection_issue"),
                "publication_date": obj.get("publication_date"),
                "html_url": obj.get("html_url"),
                "pdf_url": obj.get("pdf_url"),
                "title": obj.get("title"),
                "type": obj.get("type"),
            }
        except urllib.error.HTTPError as exc:
            last_error = str(exc)
            if exc.code == 404:
                break
            if exc.code == 429:
                retry_after = exc.headers.get("Retry-After")
                time.sleep(min(float(retry_after), 30) if retry_after and retry_after.isdigit() else 2 * (attempt + 1))
            else:
                time.sleep(0.5 * (attempt + 1))
        except (urllib.error.URLError, TimeoutError, ValueError, json.JSONDecodeError) as exc:
            last_error = str(exc)
            time.sleep(0.5 * (attempt + 1))
    return {"source_kind": "federal_register_public_inspection_api", "document_number": number,
            "api_url": url, "error": last_error}


def patch(op: str, ident_key: str, ident: str, field: str, value: str, reason: str) -> dict:
    return {"op": op, ident_key: ident, "field": field, "value": value, "reason": reason}


def main() -> None:
    evidence = rows(RAW / "evidence.jsonl")
    outcomes = rows(RAW / "outcomes.jsonl")
    references = defaultdict(lambda: {"evidence_ids": [], "outcome_thread_ids": []})
    for e in evidence:
        number = docnum(e.get("source_url"))
        if number:
            references[number]["evidence_ids"].append(e["evidence_id"])
    for o in outcomes:
        number = docnum(o.get("decisive_document_url"))
        if number:
            references[number]["outcome_thread_ids"].append(o["thread_id"])

    if "--reuse" in sys.argv or "--resume" in sys.argv:
        records = [r for r in rows(PROVENANCE) if r["source_kind"] == "federal_register_public_inspection_api"]
        assert {r["document_number"] for r in records} == set(references), "cached document set differs"
        if "--resume" in sys.argv:
            for index, rec in enumerate(records):
                if rec.get("error") and "429" in rec["error"]:
                    time.sleep(0.5)
                    records[index] = fetch(rec["document_number"])
    else:
        with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
            records = list(pool.map(fetch, sorted(references)))
    fetched_at = dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")
    for rec in records:
        rec.setdefault("fetched_at_utc", fetched_at)
        rec["evidence_ids"] = sorted(references[rec["document_number"]]["evidence_ids"])
        rec["outcome_thread_ids"] = sorted(references[rec["document_number"]]["outcome_thread_ids"])
    for evidence_id, (date, url, note) in EARLIER_AGENCY.items():
        records.append({"source_kind": "dated_agency_release", "evidence_ids": [evidence_id],
                        "public_date": date, "source_url": url, "finding": note,
                        "fetched_at_utc": fetched_at})
    for thread_id, (date, url, note) in EARLIER_OUTCOME.items():
        records.append({"source_kind": "dated_agency_release", "outcome_thread_ids": [thread_id],
                        "public_date": date, "source_url": url, "finding": note,
                        "fetched_at_utc": fetched_at})
    write_jsonl(PROVENANCE, records)
    by_number = {r["document_number"]: r for r in records if r["source_kind"] == "federal_register_public_inspection_api"}

    changes = []
    counters = defaultdict(int)
    for e in evidence:
        number = docnum(e.get("source_url"))
        if not number:
            counters["non_fr_evidence"] += 1
            continue
        rec = by_number[number]
        if not rec.get("filed_at"):
            counters["missing_pi_evidence"] += 1
            continue
        pi_date = rec["filed_at"][:10]  # ISO timestamp includes Eastern offset.
        if rec["publication_date"] != e["publication_date"]:
            counters["print_date_disagreement_evidence"] += 1
        agency = EARLIER_AGENCY.get(e["evidence_id"])
        date = agency[0] if agency and agency[0] < pi_date else pi_date
        source = agency[1] if agency and agency[0] < pi_date else rec["api_url"]
        reason = (f"First documented public availability {date}; FR {number} PI filed_at={rec['filed_at']} "
                  f"and print publication_date={rec['publication_date']}. Source: {source}. "
                  "Earlier agency availability outside the sampled review remains unchecked unless a dated agency source is cited here.")
        for field in ("publication_date", "first_known_date"):
            if e.get(field) != date:
                changes.append(patch("set_evidence", "evidence_id", e["evidence_id"], field, date, reason))
                counters[f"{field}_patches"] += 1
        counters["pi_evidence"] += 1

    for o in outcomes:
        number = docnum(o.get("decisive_document_url"))
        if not number:
            continue
        rec = by_number[number]
        if not rec.get("filed_at"):
            counters["missing_pi_outcome"] += 1
            continue
        pi_date = rec["filed_at"][:10]
        agency = EARLIER_OUTCOME.get(o["thread_id"])
        date = agency[0] if agency and agency[0] < pi_date else pi_date
        if o["decisive_action"] and o.get("decisive_date") != date:
            reason = (f"FR {number} PI filed_at={rec['filed_at']} before print publication_date={rec['publication_date']}; "
                      f"{rec['api_url']}. " +
                      (f"Earlier dated agency adoption release: {agency[1]}." if agency and agency[0] < pi_date else
                       "PI is the latest documented first-public-adoption date here; an earlier agency adoption release has not been ruled out."))
            changes.append(patch("set_outcome", "thread_id", o["thread_id"], "decisive_date", date, reason))
            counters["decisive_date_patches"] += 1
        elif o.get("withdrawal_date") and o["withdrawal_date"] != date:
            reason = (f"FR {number} withdrawal PI filed_at={rec['filed_at']} before print publication_date={rec['publication_date']}; "
                      f"{rec['api_url']}. Earlier agency withdrawal release has not been ruled out.")
            changes.append(patch("set_outcome", "thread_id", o["thread_id"], "withdrawal_date", date, reason))
            counters["withdrawal_date_patches"] += 1
        counters["pi_outcome"] += 1

    write_jsonl(PATCHES, changes)
    scope = []
    for o in outcomes:
        thread_id = o["thread_id"]
        thread_evidence = [e for e in evidence if e["thread_id"] == thread_id]
        fr_numbers = sorted({n for e in thread_evidence if (n := docnum(e.get("source_url")))})
        outcome_number = docnum(o.get("decisive_document_url"))
        if outcome_number:
            fr_numbers = sorted(set(fr_numbers) | {outcome_number})
        missing = [n for n in fr_numbers if not by_number[n].get("filed_at")]
        scope.append({
            "thread_id": thread_id,
            "pi_coverage_complete": not missing,
            "missing_pi_document_numbers": missing,
            "documented_earlier_agency_evidence_ids": sorted(e["evidence_id"] for e in thread_evidence if e["evidence_id"] in EARLIER_AGENCY),
            "documented_earlier_agency_outcome": thread_id in EARLIER_OUTCOME,
            "date_sensitivity_scope": "pi_bound_after_versioned_rebuild" if not missing else "mixed_pi_print_bound_after_versioned_rebuild",
            "needs_full_earliest_agency_date_audit": True,
            "censor_date": CENSOR_DATE,
        })
    write_jsonl(SCOPE, scope)
    print(json.dumps({"provenance": str(PROVENANCE.relative_to(ROOT)), "patches": str(PATCHES.relative_to(ROOT)),
                      "scope": str(SCOPE.relative_to(ROOT)),
                      "unique_fr_documents": len(references), "api_success": sum(bool(x.get("filed_at")) for x in records),
                      "api_failed": [x["document_number"] for x in records if x.get("source_kind") == "federal_register_public_inspection_api" and not x.get("filed_at")],
                      "patch_count": len(changes), **counters}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
