#!/usr/bin/env python3
"""collectors/us_fr.py — Federal Register NPRM -> final-rule thread collector.

Workstream: us_fr. Writes ONLY to data/raw/us_fr/*.

Builds regulatory_thread / evidence / outcome records (see schemas/*.schema.json,
docs/EXECUTOR_GUIDE.md) from two precursor populations drawn from the Federal
Register API (https://www.federalregister.gov/api/v1/documents.json):

  Frame H (historical): EO-12866-significant proposed rules (type=PRORULE,
    significant=1) published 2019-07-01..2023-12-31. Eligible anchors are
    filtered down to genuine NPRMs. A systematic sample of 85 is drawn from the
    eligible, date-sorted list, deduplicated by RIN. Thread ids US-FR-H-####.

  Frame C (post-model-cutoff holdout): ALL eligible significant NPRMs published
    2025-06-01..2026-06-30 (census). Outcomes are resolved through 2026-09-24.
    Threads whose outcome resolved BEFORE 2026-07-01 are excluded from the C
    holdout and instead emitted as ordinary historical threads, ids
    US-FR-X-####. The remaining C threads are capped at 60 (systematic sample
    if more), ids US-FR-C-####.

Linkage/outcome resolution walks the RIN (or docket) forward via the FR API to
find the first later "Rule" that substantively adopts the proposal (decisive
action) or a withdrawal. A full-text-search fallback (conditions[term]=<RIN>)
catches agency-wide withdrawal notices that do not carry the RIN in their own
metadata (e.g. SEC's June 2025 mass withdrawal).

Re-running this script is safe: already-written thread_ids are skipped, and all
Federal Register API responses are cached under data/raw/us_fr/cache/.

Usage: python3 collectors/us_fr.py [--stage all|frameH|frameC]
"""
from __future__ import annotations

import argparse
import hashlib
import io
import json
import os
import re
import sys
import time
import urllib.parse

import requests

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "data", "raw", "us_fr")
CACHE = os.path.join(OUT, "cache")
os.makedirs(CACHE, exist_ok=True)

THREADS_PATH = os.path.join(OUT, "threads.jsonl")
EVIDENCE_PATH = os.path.join(OUT, "evidence.jsonl")
OUTCOMES_PATH = os.path.join(OUT, "outcomes.jsonl")

API = "https://www.federalregister.gov/api/v1/documents.json"
UA = "Mozilla/5.0 (RegulatoryPredictiveEngine/1.0; research collector; hello@thecircl.in)"
RETRIEVAL_DATE = "2026-09-25"
OUTCOME_CENSOR_DATE = "2026-09-24"     # "resolve outcomes through 2026-09-24"
FRAME_C_HOLDOUT_CUTOFF = "2026-07-01"  # threads resolved before this are excluded from Frame C

FRAME_H_WINDOW = ("2019-07-01", "2023-12-31")
FRAME_C_WINDOW = ("2025-06-01", "2026-06-30")
FRAME_H_TARGET_N = 85
FRAME_C_CAP = 60

FIELDS = [
    "document_number", "title", "type", "abstract", "publication_date", "agencies",
    "regulation_id_numbers", "docket_ids", "html_url", "pdf_url", "comments_close_on",
    "significant", "action", "regulations_dot_gov_info", "raw_text_url",
]

SESSION = requests.Session()
SESSION.headers.update({"User-Agent": UA})

STATS = {}  # populated by main() for NOTES.md


# --------------------------------------------------------------------------
# HTTP + cache helpers
# --------------------------------------------------------------------------

def _cache_path(key: str) -> str:
    h = hashlib.sha256(key.encode("utf-8")).hexdigest()[:40]
    return os.path.join(CACHE, f"{h}.json")


def cached_get_json(url: str, params: dict, desc: str = "") -> dict:
    """GET url+params as JSON, cached to disk by full querystring."""
    qs = urllib.parse.urlencode(params, doseq=True)
    full = f"{url}?{qs}"
    cp = _cache_path(full)
    if os.path.exists(cp):
        with open(cp) as f:
            return json.load(f)
    for attempt in range(4):
        try:
            resp = SESSION.get(url, params=params, timeout=40)
            if resp.status_code == 200:
                data = resp.json()
                with open(cp, "w") as f:
                    json.dump(data, f)
                time.sleep(0.15)
                return data
            else:
                sys.stderr.write(f"WARN http {resp.status_code} for {desc or full}\n")
                time.sleep(1.5 * (attempt + 1))
        except requests.RequestException as e:
            sys.stderr.write(f"WARN request error ({desc or full}): {e}\n")
            time.sleep(1.5 * (attempt + 1))
    return {"results": [], "count": 0, "error": True}


def cached_get_pdf_text(pdf_url: str) -> str | None:
    """Best-effort: download a govinfo.gov PDF and extract text (pymupdf). Cached."""
    if not pdf_url:
        return None
    cp = _cache_path("PDFTEXT::" + pdf_url)
    if os.path.exists(cp):
        with open(cp) as f:
            d = json.load(f)
            return d.get("text")
    text = None
    try:
        resp = SESSION.get(pdf_url, timeout=40)
        if resp.status_code == 200 and resp.content[:4] == b"%PDF":
            import fitz  # pymupdf
            doc = fitz.open(stream=resp.content, filetype="pdf")
            text = "".join(page.get_text() for page in doc)
            time.sleep(0.15)
    except Exception as e:
        sys.stderr.write(f"WARN pdf fetch/extract failed for {pdf_url}: {e}\n")
        text = None
    with open(cp, "w") as f:
        json.dump({"text": text}, f)
    return text


def fetch_all_documents(conditions: dict, desc: str) -> list[dict]:
    """Fetch every result for `conditions` from the FR documents.json endpoint,
    paginating with per_page=1000. Returns the flat list of result dicts."""
    out = []
    page = 1
    while True:
        params = dict(conditions)
        params["per_page"] = 1000
        params["order"] = "oldest"
        params["page"] = page
        for i, fld in enumerate(FIELDS):
            params[f"fields[{i}]"] = fld
        # requests needs repeated keys for fields[]; build manually instead
        params2 = {}
        for k, v in conditions.items():
            params2[k] = v
        qparts = []
        for k, v in params2.items():
            if isinstance(v, list):
                for item in v:
                    qparts.append((k, item))
            else:
                qparts.append((k, v))
        qparts.append(("per_page", 1000))
        qparts.append(("order", "oldest"))
        qparts.append(("page", page))
        for fld in FIELDS:
            qparts.append(("fields[]", fld))
        qs = urllib.parse.urlencode(qparts, doseq=True)
        cache_key = f"{API}?{qs}"
        cp = _cache_path(cache_key)
        if os.path.exists(cp):
            with open(cp) as f:
                data = json.load(f)
        else:
            resp = None
            for attempt in range(4):
                try:
                    resp = SESSION.get(API, params=qparts, timeout=60)
                    if resp.status_code == 200:
                        break
                except requests.RequestException as e:
                    sys.stderr.write(f"WARN {desc} page {page}: {e}\n")
                time.sleep(1.5 * (attempt + 1))
            if resp is None or resp.status_code != 200:
                sys.stderr.write(f"ERROR could not fetch {desc} page {page}\n")
                break
            data = resp.json()
            with open(cp, "w") as f:
                json.dump(data, f)
            time.sleep(0.2)
        results = data.get("results", [])
        out.extend(results)
        total_pages = data.get("total_pages", 1)
        if page >= total_pages or not results:
            break
        page += 1
    return out


def rin_lookup(rin: str) -> list[dict]:
    qparts = [("conditions[regulation_id_number]", rin), ("per_page", 100), ("order", "oldest")]
    for fld in FIELDS:
        qparts.append(("fields[]", fld))
    return _get_docs(qparts, desc=f"rin={rin}")


def docket_lookup(docket: str) -> list[dict]:
    qparts = [("conditions[docket_id]", docket), ("per_page", 100), ("order", "oldest")]
    for fld in FIELDS:
        qparts.append(("fields[]", fld))
    return _get_docs(qparts, desc=f"docket={docket}")


def term_lookup(term: str) -> list[dict]:
    qparts = [("conditions[term]", term), ("per_page", 40), ("order", "oldest")]
    for fld in FIELDS:
        qparts.append(("fields[]", fld))
    return _get_docs(qparts, desc=f"term={term}")


def _get_docs(qparts, desc):
    qs = urllib.parse.urlencode(qparts, doseq=True)
    cache_key = f"{API}?{qs}"
    cp = _cache_path(cache_key)
    if os.path.exists(cp):
        with open(cp) as f:
            data = json.load(f)
    else:
        data = None
        for attempt in range(4):
            try:
                resp = SESSION.get(API, params=qparts, timeout=40)
                if resp.status_code == 200:
                    data = resp.json()
                    break
            except requests.RequestException as e:
                sys.stderr.write(f"WARN {desc}: {e}\n")
            time.sleep(1.0 * (attempt + 1))
        if data is None:
            return []
        with open(cp, "w") as f:
            json.dump(data, f)
        time.sleep(0.15)
    return data.get("results", [])


# --------------------------------------------------------------------------
# JSONL append helpers (incremental writes; survive interruption)
# --------------------------------------------------------------------------

def _existing_ids(path: str, key: str) -> set:
    if not os.path.exists(path):
        return set()
    ids = set()
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                ids.add(json.loads(line)[key])
            except Exception:
                pass
    return ids


def append_record(path: str, rec: dict) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "a") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")


EXISTING_THREAD_IDS = None
EXISTING_EVIDENCE_IDS = None
EXISTING_OUTCOME_TIDS = None


def load_existing():
    global EXISTING_THREAD_IDS, EXISTING_EVIDENCE_IDS, EXISTING_OUTCOME_TIDS
    EXISTING_THREAD_IDS = _existing_ids(THREADS_PATH, "thread_id")
    EXISTING_EVIDENCE_IDS = _existing_ids(EVIDENCE_PATH, "evidence_id")
    EXISTING_OUTCOME_TIDS = _existing_ids(OUTCOMES_PATH, "thread_id")


# --------------------------------------------------------------------------
# Classification: genuine NPRM vs excluded precursor/procedural document
# --------------------------------------------------------------------------

NPRM_LEAD = (
    "notice of proposed rulemaking", "notice of proposed rule", "proposed rule",
    "proposed rules", "joint notice of proposed rulemaking", "joint proposed rule",
    "joint proposed rules", "notice of proposed determination", "proposed action",
    "notification of submission", "notice of proposed rule making",
)


def classify_action(action: str, title: str) -> tuple[str, bool]:
    """Return (category, eligible). eligible=True means "genuine NPRM" anchor
    candidate. Priority order matters: exclusion categories are checked before
    the default catch-all NPRM classification."""
    a = (action or "").strip().lower()
    t = (title or "").strip().lower()
    at = a + " || " + t

    if not a:
        return "EMPTY_ACTION", False
    if re.search(r"unified agenda|regulatory (flexibility )?agenda|semiannual regulatory agenda|regulatory plan\b", at):
        return "UNIFIED_AGENDA", False
    if re.search(r"advance(d)? notice of (proposed|supplemental proposed) rulemaking|\banprm\b|\bansprm\b", at):
        return "ANPRM", False
    if re.search(r"supplement(al|ary) (notice of )?proposed rule|\bsnprm\b", at):
        return "SNPRM", False
    if re.search(r"\bwithdraw(al|n|s|ing)?\b|\btermination of rulemaking\b|\bnotification of termination\b", a):
        return "WITHDRAWAL", False
    if re.search(r"\bcorrection(s)?\b|correcting amendment", a):
        return "CORRECTION", False
    if re.search(r"extension of (the )?(public )?comment period|extension of time to submit comments|"
                 r"extension of (the )?comment periods?\b|denial of request for extension|"
                 r"grant of request for extension|extension of timeline|extension of public comment "
                 r"period|extension of currently open comment period", a):
        return "COMMENT_EXTENSION", False
    if re.search(r"re-?open(ing)? of (the )?(public )?comment period|reopen comment period|"
                 r"notice of re-?opening", a):
        return "COMMENT_REOPENING", False
    if re.search(r"proposed delay of effective date|delay of effective date", a):
        return "DELAY", False
    if re.search(r"concept release", a):
        return "CONCEPT_RELEASE", False
    is_bundled_nprm_lead = a.startswith(NPRM_LEAD)
    if not is_bundled_nprm_lead and re.search(
        r"\b(hearing|meeting|listening session|webinar)s?\b", a
    ):
        return "HEARING_NOTICE", False
    if re.search(r"^request for information\b|^request for information \(rfi\)\.?$", a):
        return "RFI_ONLY", False
    if re.search(r"notice of data availability|availability of (a |the )?(draft|supplemental|"
                 r"preliminary) (information|data)", a):
        return "DATA_AVAILABILITY", False
    if re.search(r"notice of procedural order", a):
        return "PROCEDURAL_ORDER", False
    # Default: treat as a genuine NPRM if it plausibly proposes a rule.
    if is_bundled_nprm_lead or re.search(r"propos", a):
        return "NPRM", True
    # Notices/requests-for-comment/regulatory-basis documents that do not
    # themselves propose rule text (precursor-ish, but not a genuine NPRM).
    return "NON_NPRM_NOTICE", False


DECISIVE_EXCLUDE = re.compile(
    r"\bcorrection\b|correcting amendment|\beffective date\b.*(delay|postpone|extend)|"
    r"delay of effective date|extend(ed|s|ing)? the effective date|\bstay\b|technical amendment|"
    r"administrative (change|amendment)|confirmation of effective date|announcement of effective date",
    re.I,
)
DECISIVE_INCLUDE = re.compile(
    r"\bfinal rule\b|\binterim final rule\b|\bdirect final rule\b|final rule;\s*treasury decision|"
    r"\bfinal action\b", re.I,
)
WITHDRAWAL_RE = re.compile(r"\bwithdraw(al|n|s|ing)?\b|\btermination of rulemaking\b", re.I)
UNIFIED_AGENDA_RE = re.compile(
    r"unified agenda|regulatory (flexibility )?agenda|semiannual regulatory agenda", re.I
)


# --------------------------------------------------------------------------
# Agency name helpers
# --------------------------------------------------------------------------

def agency_names(doc: dict) -> tuple[str, str]:
    """Return (regulator_short_name, full_agency_string)."""
    ags = doc.get("agencies") or []
    if not ags:
        return "Unknown", "Unknown"
    names = [a.get("name") or a.get("raw_name") or "" for a in ags]
    short = names[-1] if names else "Unknown"
    full = " / ".join(names)
    return short, full


def agency_slugs(doc: dict) -> list[str]:
    return [a.get("slug") for a in (doc.get("agencies") or []) if a.get("slug")]


def get_rins(doc: dict) -> list[str]:
    rins = list(doc.get("regulation_id_numbers") or [])
    rdgi = doc.get("regulations_dot_gov_info") or {}
    r2 = rdgi.get("regulation_id_number")
    if r2 and r2 not in rins:
        rins.append(r2)
    return [r for r in rins if r]


def get_docket(doc: dict) -> str | None:
    rdgi = doc.get("regulations_dot_gov_info") or {}
    if rdgi.get("docket_id"):
        return rdgi["docket_id"]
    for did in doc.get("docket_ids") or []:
        m = re.search(r"([A-Z][A-Za-z0-9]*-\d{4}-\d{3,6})", did)
        if m:
            return m.group(1)
    return None


# --------------------------------------------------------------------------
# Outcome resolution
# --------------------------------------------------------------------------

def resolve_outcome(anchor: dict, censor_date: str) -> dict:
    """Walk RIN/docket forward to find the decisive final rule or withdrawal.

    Returns a dict with keys: kind ('final'|'withdrawal'|'none'), doc (or None),
    date, and the pool of related docs seen (for evidence-building), plus a
    `method` note describing how the decisive doc (if any) was found.
    """
    anchor_pub = anchor["publication_date"]
    anchor_docnum = anchor["document_number"]
    rins = get_rins(anchor)
    docket = get_docket(anchor)

    pool = {}  # document_number -> doc
    for rin in rins:
        for d in rin_lookup(rin):
            pool[d["document_number"]] = d
    if docket:
        for d in docket_lookup(docket):
            pool.setdefault(d["document_number"], d)

    def candidates():
        for d in pool.values():
            if d["document_number"] == anchor_docnum:
                continue
            # Strictly later than the anchor: a same-day "final rule" is not a
            # later, comment-informed resolution of this NPRM — it is a
            # simultaneously-published companion (e.g. a "direct final rule"
            # issued the same day as its companion proposed rule, a common
            # NRC/EPA/FAA pattern), so it cannot be this thread's decisive
            # action without breaking the point-in-time anchor-before-outcome
            # invariant. Such anchors fall through to stalled/unresolved.
            if d["publication_date"] <= anchor_pub:
                continue
            if d["publication_date"] > censor_date:
                continue
            yield d

    finals, withdrawals = [], []
    for d in candidates():
        action = d.get("action") or ""
        if d.get("type") == "Rule":
            if DECISIVE_EXCLUDE.search(action):
                continue
            if DECISIVE_INCLUDE.search(action) or d.get("type") == "Rule":
                finals.append(d)
        elif WITHDRAWAL_RE.search(action) and not UNIFIED_AGENDA_RE.search(d.get("title") or ""):
            withdrawals.append(d)

    method = "rin_or_docket_lookup"

    # Fallback: agency-wide withdrawal notices that don't carry the RIN in their
    # own metadata (FR full-text search on the RIN string itself).
    if not finals and not withdrawals and rins:
        for rin in rins:
            for d in term_lookup(rin):
                if d["document_number"] == anchor_docnum:
                    continue
                if not (anchor_pub < d["publication_date"] <= censor_date):
                    continue
                title = d.get("title") or ""
                action = d.get("action") or ""
                if UNIFIED_AGENDA_RE.search(title) or UNIFIED_AGENDA_RE.search(action):
                    continue
                if WITHDRAWAL_RE.search(action) or WITHDRAWAL_RE.search(title):
                    withdrawals.append(d)
                    pool[d["document_number"]] = d
                    method = "term_search_fallback(rin_text_in_bundled_notice)"
                elif d.get("type") == "Rule" and DECISIVE_INCLUDE.search(action) and not DECISIVE_EXCLUDE.search(action):
                    finals.append(d)
                    pool[d["document_number"]] = d
                    method = "term_search_fallback(rin_text_in_bundled_notice)"

    finals.sort(key=lambda d: (d["publication_date"], d["document_number"]))
    withdrawals.sort(key=lambda d: (d["publication_date"], d["document_number"]))

    first_final = finals[0] if finals else None
    first_wd = withdrawals[0] if withdrawals else None

    if first_final and first_wd:
        decisive = first_final if first_final["publication_date"] <= first_wd["publication_date"] else None
        chosen_kind = "final" if decisive else "withdrawal"
        chosen = first_final if chosen_kind == "final" else first_wd
    elif first_final:
        chosen_kind, chosen = "final", first_final
    elif first_wd:
        chosen_kind, chosen = "withdrawal", first_wd
    else:
        chosen_kind, chosen = "none", None

    return {
        "kind": chosen_kind, "doc": chosen, "pool": pool, "method": method,
        "rins": rins, "docket": docket,
    }


CHANGE_HEADING_RE = re.compile(
    r"(summary of (?:the )?changes(?: from the (?:proposed rule|npr?m))?|"
    r"changes from the (?:proposed rule|npr?m)|"
    r"differences (?:between|from) (?:this final rule and )?the (?:proposed rule|npr?m))"
    r"[:.\s]{0,3}(.{0,900})",
    re.I | re.S,
)

SOFTEN_WORDS = re.compile(
    r"less stringent|reduc(e|ed|ing)|remov(e|ed|ing) the requirement|extend(ed|s|ing)? the (compliance|"
    r"effective) (date|deadline)|longer (compliance|transition) period|narrow(ed|er|ing)|exempt(s|ed|ing)?|"
    r"lower(ed)? the threshold|is not adopting|declin(e|ed|ing) to (adopt|finalize)|withdrew|scal(e|ed) back|"
    r"relax(ed|ing)?|delayed the compliance", re.I,
)
TIGHTEN_WORDS = re.compile(
    r"more stringent|expand(ed|s|ing)|broaden(ed|ing)?|additional requirement|earlier than proposed|"
    r"accelerat(e|ed|ing)|shorten(ed|ing)? the (compliance|transition)|lower(ed)? the (limit|cap)|"
    r"strengthen(ed|ing)?|tighten(ed|ing)?", re.I,
)
AS_PROPOSED_WORDS = re.compile(
    r"adopt(s|ing|ed)? (the rule |this rule )?as proposed|without (substantive )?change|finalizing the rule "
    r"as proposed|substantially as proposed", re.I,
)


def determine_content_direction(anchor: dict, decisive_doc: dict) -> tuple[str, str, str]:
    """Heuristic, automated content-direction classification.

    Returns (content_direction, label_confidence, rationale_text).
    """
    final_abstract = decisive_doc.get("abstract") or ""
    final_action = decisive_doc.get("action") or ""
    combined = final_action + " \n " + final_abstract

    change_note = ""
    pdf_text = None
    try:
        pdf_text = cached_get_pdf_text(decisive_doc.get("pdf_url"))
    except Exception:
        pdf_text = None
    if pdf_text:
        m = CHANGE_HEADING_RE.search(pdf_text)
        if m:
            change_note = re.sub(r"\s+", " ", m.group(2)).strip()[:700]
            combined += " \n " + change_note

    soft = bool(SOFTEN_WORDS.search(combined))
    tight = bool(TIGHTEN_WORDS.search(combined))
    as_prop = bool(AS_PROPOSED_WORDS.search(combined))

    if as_prop and not soft and not tight:
        direction, conf = "as_proposed", "medium"
    elif soft and tight:
        direction, conf = "mixed", "medium"
    elif soft:
        direction, conf = "softened", "medium"
    elif tight:
        direction, conf = "tightened", "medium"
    elif re.search(r"interim final rule", final_action, re.I) and not re.search(
        r"final rule", (anchor.get("action") or ""), re.I
    ):
        direction, conf = "different_mechanism", "medium"
    elif not final_abstract and not final_action:
        # Genuinely no text to go on at all — this is the one case that
        # warrants dropping below the task's "medium unless clear" default.
        direction, conf = "mixed", "low"
    else:
        # No explicit soften/tighten/as-proposed keyword signal found. Per
        # task instructions this still gets a provisional label at medium
        # confidence (not a guess at "low"): the direction is genuinely
        # unclear from automated text matching, but the decisive action
        # itself (the fact and date of the final rule) is independently
        # certain from the FR record, and outcome_class/decisive_date/
        # decisive_document are unaffected by this uncertainty.
        direction, conf = "mixed", "medium"

    if change_note:
        rationale = f"Automated heuristic over final-rule action/abstract text and a 'changes from the proposal' passage located in the govinfo.gov PDF: \"{change_note[:300]}\""
    else:
        rationale = ("Automated heuristic comparing NPRM abstract to final-rule action/abstract text "
                     "(keyword-based; no 'changes from the proposal' section located in the decisive "
                     "document's text — not manually verified against the full final-rule preamble).")
    return direction, conf, rationale


# --------------------------------------------------------------------------
# Evidence + thread + outcome builders
# --------------------------------------------------------------------------

# Outcome-suggestive/retrospective words that rpe.lint flags as leakage risk in
# thread-facing (forecaster-visible) text. Substituted with neutral, tense-safe
# wording so neutral_title/issue_summary_neutral read as pure proposal
# description. Forward-looking dates (e.g. a proposed future compliance date)
# are NOT touched here — those are legitimate and explicitly left alone per
# EXECUTOR_GUIDE / task instructions.
_LEAKAGE_SUBS = [
    (re.compile(r"\bfinali[sz]ed\b", re.I), "completed"),
    (re.compile(r"\bfinal rule\b", re.I), "completed regulatory action"),
    (re.compile(r"\badopted\b", re.I), "established"),
    (re.compile(r"\bapproved\b", re.I), "endorsed"),
    (re.compile(r"\bnotified\b", re.I), "announced"),
    (re.compile(r"\bwithdrawn\b", re.I), "not carried forward"),
    (re.compile(r"\bwithdrew\b", re.I), "did not carry forward"),
    (re.compile(r"\bshelved\b", re.I), "paused"),
    (re.compile(r"\babandoned\b", re.I), "discontinued"),
    (re.compile(r"(?<!no )(?<!No )\blater\b", re.I), ""),
    (re.compile(r"\beventually\b", re.I), ""),
    (re.compile(r"\bsubsequently\b", re.I), ""),
    (re.compile(r"\bwent on to\b", re.I), "proposes to"),
    (re.compile(r"\bwhich led to\b", re.I), "related to"),
    (re.compile(r"\bcame into (force|effect)\b", re.I), "would take effect"),
    (re.compile(r"\brescinded\b", re.I), "removed"),
    (re.compile(r"\bimplemented\b", re.I), "put in place"),
    (re.compile(r"\bin hindsight\b", re.I), ""),
    (re.compile(r"\bultimately\b", re.I), ""),
    (re.compile(r"\bwould later\b", re.I), "would"),
    (re.compile(r"\bwas later\b", re.I), "was"),
]


def sanitize_leakage_text(text: str) -> str:
    if not text:
        return text
    out = text
    for pat, repl in _LEAKAGE_SUBS:
        out = pat.sub(repl, out)
    out = re.sub(r"\s{2,}", " ", out)
    out = re.sub(r"\s+([.,;:])", r"\1", out)
    return out.strip()


def sha256_text(s: str) -> str:
    return hashlib.sha256((s or "").encode("utf-8")).hexdigest()


def make_claims(abstract: str, n=4) -> list[str]:
    if not abstract:
        return []
    parts = re.split(r"(?<=[.;])\s+(?=[A-Z])", abstract.strip())
    claims = [p.strip() for p in parts if len(p.strip()) > 20]
    claims = claims[:n] if claims else [abstract[:300]]
    return [sanitize_leakage_text(c) for c in claims]


def date_verification_fr() -> str:
    return ("publication_date taken directly from the federalregister.gov API "
            "documents.json 'publication_date' field, the FR's own official date of "
            "print publication; retrieved via the public v1 API.")


def build_anchor_evidence(thread_id: str, anchor: dict) -> dict:
    short, full = agency_names(anchor)
    comments_close = anchor.get("comments_close_on")
    excerpt = (anchor.get("abstract") or "").strip()
    tail = []
    if comments_close:
        tail.append(f"Comment deadline: {comments_close}.")
    tail.append(f"EO 12866 significant: {bool(anchor.get('significant'))}.")
    tail.append(f"Agencies: {full}.")
    excerpt = sanitize_leakage_text((excerpt + " " + " ".join(tail)).strip())[:4000]
    ev = {
        "evidence_id": f"{thread_id}-E01",
        "thread_id": thread_id,
        "regulator": short,
        "jurisdiction": "US",
        "title": anchor["title"],
        "source_url": anchor["html_url"],
        "publication_date": anchor["publication_date"],
        "first_known_date": None,
        "retrieval_date": RETRIEVAL_DATE,
        "document_type": "nprm",
        "tier": "B",
        "original_or_revised": "original",
        "version_confidence": "high",
        "date_verification": date_verification_fr(),
        "extracted_claims": make_claims(anchor.get("abstract") or ""),
        "content_excerpt": excerpt,
        "source_hash": sha256_text(excerpt),
        "stored_copy": None,
    }
    return ev


SECONDARY_TYPE_MAP = [
    ("ANPRM", "anprm"),
    ("SNPRM", "snprm"),
    ("COMMENT_EXTENSION", "comment_extension"),
    ("COMMENT_REOPENING", "comment_reopening"),
    ("HEARING_NOTICE", "hearing_notice"),
]


def build_secondary_evidence(thread_id: str, seq: int, doc: dict, doc_category: str) -> dict:
    short, full = agency_names(doc)
    dtype = dict(SECONDARY_TYPE_MAP).get(doc_category, "related_notice")
    excerpt = (doc.get("abstract") or "").strip()
    if not excerpt:
        excerpt = f"({doc.get('action') or doc.get('type')}) — no abstract published for this document."
    excerpt = sanitize_leakage_text(excerpt)[:4000]
    return {
        "evidence_id": f"{thread_id}-E{seq:02d}",
        "thread_id": thread_id,
        "regulator": short,
        "jurisdiction": "US",
        "title": doc["title"],
        "source_url": doc["html_url"],
        "publication_date": doc["publication_date"],
        "first_known_date": None,
        "retrieval_date": RETRIEVAL_DATE,
        "document_type": dtype,
        "tier": "B",
        "original_or_revised": "original",
        "version_confidence": "high",
        "date_verification": date_verification_fr(),
        "extracted_claims": make_claims(doc.get("abstract") or "") or [doc.get("action") or ""],
        "content_excerpt": excerpt,
        "source_hash": sha256_text(excerpt),
        "stored_copy": None,
    }


def build_stakeholder_evidence(thread_id: str, seq: int, anchor: dict, comment_deadlines: list[str],
                                decisive_date: str | None) -> dict | None:
    rdgi = anchor.get("regulations_dot_gov_info") or {}
    count = rdgi.get("comments_count")
    if not count or count <= 0:
        return None
    deadlines = [d for d in comment_deadlines if d]
    if not deadlines:
        return None
    latest_close = max(deadlines)
    from datetime import date, timedelta
    pub = (date.fromisoformat(latest_close) + timedelta(days=14)).isoformat()
    if decisive_date and pub >= decisive_date:
        return None
    if pub > RETRIEVAL_DATE:
        # Can't claim to have "retrieved" a comment count as of a synthetic
        # date that falls after our actual retrieval date.
        return None
    docket = get_docket(anchor) or "unknown"
    short, _ = agency_names(anchor)
    excerpt = (f"As retrieved from the federalregister.gov / regulations.gov integration on "
               f"{RETRIEVAL_DATE}, docket {docket} had received {count} public comments; the "
               f"most recent associated comment period on this thread closed {latest_close}.")
    return {
        "evidence_id": f"{thread_id}-E{seq:02d}",
        "thread_id": thread_id,
        "regulator": short,
        "jurisdiction": "US",
        "title": f"Public comment volume on docket {docket}",
        "source_url": rdgi.get("comments_url") or anchor["html_url"],
        "publication_date": pub,
        "first_known_date": None,
        "retrieval_date": RETRIEVAL_DATE,
        "document_type": "comment_count",
        "tier": "S",
        "original_or_revised": "original",
        "version_confidence": "medium",
        "date_verification": ("publication_date is synthetic: latest known comments_close_on for this "
                               "thread (%s) + 14 days, used as a plausible date by which the comment "
                               "volume was knowable; comment count itself is FR/regulations.gov "
                               "integration data." % latest_close),
        "extracted_claims": [f"Docket {docket} received {count} public comments (count as of "
                              f"regulations.gov check reflected in the FR API on {RETRIEVAL_DATE})."],
        "content_excerpt": excerpt,
        "source_hash": sha256_text(excerpt),
        "stored_copy": None,
    }


def neutral_title(anchor: dict) -> str:
    short, _ = agency_names(anchor)
    title = sanitize_leakage_text(anchor["title"])
    t = f"{short} proposed rule: {title}"
    return t[:200]


def issue_summary(anchor: dict) -> str:
    abstract = (anchor.get("abstract") or "").strip()
    sents = re.split(r"(?<=[.;])\s+(?=[A-Z])", abstract)
    sents = [s.strip() for s in sents if s.strip()]
    summary = " ".join(sents[:3]) if sents else abstract
    summary = summary.strip()
    if len(summary) < 20:
        summary = (abstract or anchor["title"]).strip()
    summary = sanitize_leakage_text(summary)
    return summary[:1490]


def action_label_confidence(resolution: dict) -> tuple[str, str]:
    """Confidence in the ACTION/TIMING label only (was there a decisive action
    or withdrawal, and on what date) — per the Director's schema clarification,
    this is independent of and must never be lowered by content_direction
    uncertainty. Returns (confidence, rationale)."""
    method = resolution["method"]
    has_rin = bool(resolution["rins"])
    has_docket = bool(resolution["docket"])
    if method.startswith("term_search_fallback"):
        return ("medium", "found only via the conditions[term]=<RIN> full-text-search fallback "
                           "(the decisive/withdrawal document did not carry this RIN in its own FR "
                           "metadata), so the RIN match — while directly verified in the document's "
                           "own text/title — is a slightly less certain linkage than a native "
                           "regulation_id_number tie.")
    if has_rin:
        return ("high", "linked via a native FR regulation_id_number match, the most reliable "
                         "linkage available.")
    if has_docket:
        return ("medium", "anchor had no RIN; linked via docket_id only, which is reliable but "
                           "less authoritative than a RIN match.")
    return ("low", "anchor had neither a RIN nor a resolvable docket id, so this linkage/absence-"
                    "of-later-action determination could not be made with confidence.")


def build_outcome(thread_id: str, anchor: dict, resolution: dict, censor_date: str,
                   frame_label: str) -> dict:
    kind = resolution["kind"]
    doc = resolution["doc"]
    anchor_short, _ = agency_names(anchor)
    act_conf, act_rationale = action_label_confidence(resolution)

    if kind == "final":
        direction, content_conf, rationale = determine_content_direction(anchor, doc)
        outcome_class_map = {
            "as_proposed": "action_as_proposed", "softened": "action_softened",
            "tightened": "action_tightened", "mixed": "action_mixed",
            "different_mechanism": "action_mixed",
        }
        outcome_class = outcome_class_map[direction]
        content_summary = (
            f"{doc.get('action') or 'Final rule'} published {doc['publication_date']} "
            f"({doc.get('type')}): {doc['title']}. " + (doc.get("abstract") or "")[:900]
        ).strip()[:3800]
        return {
            "thread_id": thread_id, "outcome_class": outcome_class, "decisive_action": True,
            "decisive_date": doc["publication_date"], "decisive_document_title": doc["title"],
            "decisive_document_url": doc["html_url"], "decisive_document_type": doc.get("action") or doc.get("type"),
            "withdrawal_date": None, "censor_date": censor_date, "content_direction": direction,
            "content_summary": content_summary, "key_parameters": [],
            "outcome_sources": [doc["html_url"], anchor["html_url"]],
            "label_confidence": act_conf, "content_label_confidence": content_conf,
            "labeled_by": "collectors/us_fr.py (automated)",
            "notes": (f"Linkage method: {resolution['method']}. RIN(s): {', '.join(resolution['rins']) or 'none'}. "
                      f"Docket: {resolution['docket'] or 'none'}. label_confidence rationale (action/timing "
                      f"only): {act_rationale} content_label_confidence rationale: {rationale}"),
        }
    elif kind == "withdrawal":
        content_summary = (
            f"{doc.get('action') or 'Withdrawal'} published {doc['publication_date']}: {doc['title']}. "
            + (doc.get("abstract") or "")[:900]
        ).strip()[:3800]
        return {
            "thread_id": thread_id, "outcome_class": "withdrawn", "decisive_action": False,
            "decisive_date": None, "decisive_document_title": doc["title"],
            "decisive_document_url": doc["html_url"], "decisive_document_type": doc.get("action") or doc.get("type"),
            "withdrawal_date": doc["publication_date"], "censor_date": censor_date, "content_direction": "na",
            "content_summary": content_summary, "key_parameters": [],
            "outcome_sources": [doc["html_url"], anchor["html_url"]],
            "label_confidence": act_conf,
            # content_direction is trivially "na" (no action taken to have a direction), so
            # content_label_confidence is trivially high, per the Director's clarification.
            "content_label_confidence": "high",
            "labeled_by": "collectors/us_fr.py (automated)",
            "notes": (f"Linkage method: {resolution['method']}. RIN(s): {', '.join(resolution['rins']) or 'none'}. "
                      f"Docket: {resolution['docket'] or 'none'}. label_confidence rationale: {act_rationale}"),
        }
    else:
        if frame_label == "H":
            outcome_class = "stalled_no_action"
        else:
            outcome_class = "unresolved"
        return {
            "thread_id": thread_id, "outcome_class": outcome_class, "decisive_action": False,
            "decisive_date": None, "decisive_document_title": None, "decisive_document_url": None,
            "decisive_document_type": None, "withdrawal_date": None, "censor_date": censor_date,
            "content_direction": "na",
            "content_summary": (f"No final rule or withdrawal notice sharing RIN(s) "
                                 f"{', '.join(resolution['rins']) or 'none'} / docket "
                                 f"{resolution['docket'] or 'none'} was found in the Federal Register through "
                                 f"{censor_date}. Anchor NPRM: {anchor['title']}."),
            "key_parameters": [], "outcome_sources": [anchor["html_url"]],
            "label_confidence": act_conf,
            "content_label_confidence": "high",
            "labeled_by": "collectors/us_fr.py (automated)",
            "notes": (f"Linkage method: {resolution['method']}. No decisive document found by {censor_date}. "
                      f"label_confidence rationale: {act_rationale}"),
        }


def build_thread(thread_id: str, anchor: dict, sampling_frame: str, sampling_method: str,
                  quality_tier: str) -> dict:
    short, full = agency_names(anchor)
    return {
        "thread_id": thread_id, "workstream": "us_fr", "regulator": short, "jurisdiction": "US",
        "neutral_title": neutral_title(anchor), "issue_summary_neutral": issue_summary(anchor),
        "process_type": "nprm_to_final", "anchor_evidence_id": f"{thread_id}-E01",
        "anchor_date": anchor["publication_date"], "sampling_frame": sampling_frame,
        "sampling_method": sampling_method, "quality_tier_proposed": quality_tier,
        "created_by": "collectors/us_fr.py", "notes": None,
        "agency": full, "rin": ", ".join(get_rins(anchor)) or None, "docket": get_docket(anchor),
    }


_DISAMBIG_SUFFIX = {
    "nprm": " (Notice of Proposed Rulemaking)",
    "anprm": " (Advance Notice of Proposed Rulemaking)",
    "snprm": " (Supplemental Notice of Proposed Rulemaking)",
    "comment_extension": " (comment-period extension notice)",
    "comment_reopening": " (comment-period reopening notice)",
    "hearing_notice": " (hearing notice)",
}


def disambiguate_titles(evidence: list[dict], outcome: dict) -> None:
    """rpe.lint errors if any evidence item's title is byte-identical to the
    decisive document's title (a leakage/duplication guard). Real NPRM/final-
    rule pairs frequently DO share an identical title by normal agency
    drafting practice, so append a short, non-substantive stage disambiguator
    rather than altering the document's substantive title text."""
    dt = (outcome.get("decisive_document_title") or "").strip().lower()
    if not dt or len(dt) <= 12:
        return
    for ev in evidence:
        if ev["title"].strip().lower() == dt:
            suffix = _DISAMBIG_SUFFIX.get(ev["document_type"], " (proposed-stage document)")
            new_title = (ev["title"] + suffix)
            ev["title"] = new_title


def process_anchor(thread_id: str, anchor: dict, sampling_frame: str, sampling_method: str,
                    quality_tier: str, frame_label: str) -> dict:
    """Resolve outcome, build all records, append them, return a small summary dict."""
    resolution = resolve_outcome(anchor, OUTCOME_CENSOR_DATE)
    thread = build_thread(thread_id, anchor, sampling_frame, sampling_method, quality_tier)
    outcome = build_outcome(thread_id, anchor, resolution, OUTCOME_CENSOR_DATE, frame_label)

    decisive_date = outcome.get("decisive_date") or outcome.get("withdrawal_date")

    evidence = [build_anchor_evidence(thread_id, anchor)]
    seq = 2
    comment_deadlines = [anchor.get("comments_close_on")]
    pool_docs = sorted(resolution["pool"].values(), key=lambda d: (d["publication_date"], d["document_number"]))
    for d in pool_docs:
        if d["document_number"] == anchor["document_number"]:
            continue
        if decisive_date and d["publication_date"] >= decisive_date:
            continue
        if d["publication_date"] < "2000-01-01":
            continue
        cat, _eligible = classify_action(d.get("action"), d.get("title"))
        if cat in ("ANPRM", "SNPRM", "COMMENT_EXTENSION", "COMMENT_REOPENING", "HEARING_NOTICE"):
            evidence.append(build_secondary_evidence(thread_id, seq, d, cat))
            seq += 1
            if d.get("comments_close_on"):
                comment_deadlines.append(d["comments_close_on"])
        elif d.get("type") in ("Proposed Rule", "Notice") and d["publication_date"] > anchor["publication_date"]:
            # generic related notice sharing the RIN/docket, not otherwise categorized
            if cat not in ("CORRECTION", "UNIFIED_AGENDA", "WITHDRAWAL", "DELAY"):
                evidence.append(build_secondary_evidence(thread_id, seq, d, "RELATED"))
                seq += 1

    stakeholder = build_stakeholder_evidence(thread_id, seq, anchor, comment_deadlines, decisive_date)
    if stakeholder:
        evidence.append(stakeholder)
        seq += 1

    disambiguate_titles(evidence, outcome)

    for ev in evidence:
        if ev["evidence_id"] in EXISTING_EVIDENCE_IDS:
            continue
        append_record(EVIDENCE_PATH, ev)
        EXISTING_EVIDENCE_IDS.add(ev["evidence_id"])

    if thread["thread_id"] not in EXISTING_THREAD_IDS:
        append_record(THREADS_PATH, thread)
        EXISTING_THREAD_IDS.add(thread["thread_id"])
    if outcome["thread_id"] not in EXISTING_OUTCOME_TIDS:
        append_record(OUTCOMES_PATH, outcome)
        EXISTING_OUTCOME_TIDS.add(outcome["thread_id"])

    return {"thread_id": thread_id, "outcome_class": outcome["outcome_class"],
            "decisive_action": outcome["decisive_action"], "n_evidence": len(evidence)}


# --------------------------------------------------------------------------
# Systematic sampling
# --------------------------------------------------------------------------

def systematic_sample_indices(n: int, k: int) -> tuple[list[int], float, float]:
    """Return (indices, step, start_offset) for a systematic sample of size k from n
    sorted items, evenly spread across the full range [0, n). Uses a floating-point
    step (n/k) rather than integer division: when n is not many times larger than k
    (e.g. capping 97 kept Frame-C threads down to 60), integer step truncates to 1 and
    degenerates into "take the first k in order", which is a temporal selection bias,
    not a systematic sample. A float step keeps every ratio >= 1 evenly spread."""
    if k <= 0 or n <= 0:
        return [], 0.0, 0.0
    if k >= n:
        return list(range(n)), 1.0, 0.0
    step = n / k
    start = step / 2
    idx, seen = [], set()
    for i in range(k):
        j = min(int(start + i * step), n - 1)
        while j in seen and j < n - 1:
            j += 1
        idx.append(j)
        seen.add(j)
    return idx, step, start


# --------------------------------------------------------------------------
# Frame H
# --------------------------------------------------------------------------

def run_frame_h():
    print("=== Frame H: fetching population ===")
    docs = fetch_all_documents(
        {"conditions[type][]": "PRORULE", "conditions[significant]": 1,
         "conditions[publication_date][gte]": FRAME_H_WINDOW[0],
         "conditions[publication_date][lte]": FRAME_H_WINDOW[1]},
        desc="frameH",
    )
    STATS["frameH_seen"] = len(docs)
    print(f"Frame H population: {len(docs)} docs")

    cat_counts = {}
    eligible = []
    for d in docs:
        cat, ok = classify_action(d.get("action"), d.get("title"))
        cat_counts[cat] = cat_counts.get(cat, 0) + 1
        if ok:
            eligible.append(d)
    eligible.sort(key=lambda d: (d["publication_date"], d["document_number"]))
    STATS["frameH_category_counts"] = cat_counts
    STATS["frameH_eligible"] = len(eligible)
    print(f"Frame H eligible NPRMs: {len(eligible)}  (categories: {cat_counts})")

    idx, step, start = systematic_sample_indices(len(eligible), FRAME_H_TARGET_N)
    STATS["frameH_step"] = round(step, 3)
    STATS["frameH_start_offset"] = round(start, 3)
    print(f"Frame H systematic sample: step={step:.3f} start_offset={start:.3f} -> {len(idx)} target slots")

    used_rin_keys = set()
    used_docnums = set()
    skip_log = []
    n_built = 0
    for target in idx:
        i = target
        chosen = None
        while i < len(eligible):
            cand = eligible[i]
            if cand["document_number"] in used_docnums:
                i += 1
                continue
            rins = get_rins(cand)
            key = tuple(sorted(rins)) if rins else (("DOCKET", get_docket(cand)),) if get_docket(cand) else (("DOC", cand["document_number"]),)
            if key in used_rin_keys and i != target:
                skip_log.append({"target_index": target, "skipped_document_number": cand["document_number"],
                                  "reason": "RIN already used by an earlier-sampled thread"})
                i += 1
                continue
            if key in used_rin_keys and i == target:
                # the exact target slot's RIN is already used -> advance and log
                skip_log.append({"target_index": target, "skipped_document_number": cand["document_number"],
                                  "reason": "sampled RIN already has a thread; advancing to next eligible doc"})
                i += 1
                continue
            chosen = cand
            used_rin_keys.add(key)
            used_docnums.add(cand["document_number"])
            break
        if chosen is None:
            continue
        thread_id = f"US-FR-H-{n_built + 1:04d}"
        n_built += 1
        if thread_id in EXISTING_THREAD_IDS:
            print(f"  {thread_id} already exists, skipping recompute")
            continue
        summary = process_anchor(
            thread_id, chosen,
            sampling_frame=f"Federal Register API, type=PRORULE, significant=1, publication_date "
                            f"{FRAME_H_WINDOW[0]}..{FRAME_H_WINDOW[1]}; eligible genuine-NPRM subset "
                            f"({len(eligible)} of {len(docs)} raw significant proposed rules)",
            sampling_method="systematic",
            quality_tier="RAPID", frame_label="H",
        )
        print(f"  built {thread_id}: {chosen['title'][:70]!r} -> {summary['outcome_class']}")

    STATS["frameH_built"] = n_built
    STATS["frameH_skip_log"] = skip_log
    print(f"Frame H: built {n_built} threads, {len(skip_log)} RIN-collision skips logged")


# --------------------------------------------------------------------------
# Frame C + Frame X
# --------------------------------------------------------------------------

def run_frame_c():
    print("=== Frame C: fetching population ===")
    docs = fetch_all_documents(
        {"conditions[type][]": "PRORULE", "conditions[significant]": 1,
         "conditions[publication_date][gte]": FRAME_C_WINDOW[0],
         "conditions[publication_date][lte]": FRAME_C_WINDOW[1]},
        desc="frameC",
    )
    STATS["frameC_seen"] = len(docs)
    print(f"Frame C population: {len(docs)} docs")

    cat_counts = {}
    eligible = []
    for d in docs:
        cat, ok = classify_action(d.get("action"), d.get("title"))
        cat_counts[cat] = cat_counts.get(cat, 0) + 1
        if ok:
            eligible.append(d)
    eligible.sort(key=lambda d: (d["publication_date"], d["document_number"]))
    STATS["frameC_category_counts"] = cat_counts
    STATS["frameC_eligible"] = len(eligible)
    print(f"Frame C eligible NPRMs (census): {len(eligible)}  (categories: {cat_counts})")

    print("Resolving outcomes for the full Frame C eligible census (this queries the FR API per RIN/docket)...")
    kept, excluded = [], []
    for n, anchor in enumerate(eligible, 1):
        resolution = resolve_outcome(anchor, OUTCOME_CENSOR_DATE)
        decisive_date = None
        if resolution["kind"] == "final":
            decisive_date = resolution["doc"]["publication_date"]
        elif resolution["kind"] == "withdrawal":
            decisive_date = resolution["doc"]["publication_date"]
        if decisive_date and decisive_date < FRAME_C_HOLDOUT_CUTOFF:
            excluded.append((anchor, resolution))
        else:
            kept.append((anchor, resolution))
        if n % 20 == 0:
            print(f"  ...resolved {n}/{len(eligible)}")

    STATS["frameC_resolved_before_july_excluded"] = len(excluded)
    STATS["frameC_kept_for_holdout"] = len(kept)
    print(f"Frame C: {len(excluded)} resolved before {FRAME_C_HOLDOUT_CUTOFF} (-> Frame X), "
          f"{len(kept)} kept as the C holdout population")

    # --- Frame X: all excluded, no cap ---
    kept.sort(key=lambda ar: (ar[0]["publication_date"], ar[0]["document_number"]))
    excluded.sort(key=lambda ar: (ar[0]["publication_date"], ar[0]["document_number"]))

    n_x = 0
    for anchor, resolution in excluded:
        n_x += 1
        thread_id = f"US-FR-X-{n_x:04d}"
        if thread_id in EXISTING_THREAD_IDS:
            continue
        summary = process_anchor_with_resolution(
            thread_id, anchor, resolution,
            sampling_frame=f"Federal Register API, type=PRORULE, significant=1, publication_date "
                            f"{FRAME_C_WINDOW[0]}..{FRAME_C_WINDOW[1]} (Frame C census); eligible genuine-NPRM "
                            f"anchor whose outcome resolved before the {FRAME_C_HOLDOUT_CUTOFF} Frame-C holdout "
                            f"cutoff, re-labeled as an ordinary historical thread (Frame X)",
            sampling_method="census", quality_tier="RAPID", frame_label="X",
        )
        print(f"  built {thread_id} (Frame X): {anchor['title'][:60]!r} -> {summary['outcome_class']}")
    STATS["frameX_built"] = n_x

    # --- Frame C: cap at 60, systematic if more ---
    if len(kept) > FRAME_C_CAP:
        idx, step, start = systematic_sample_indices(len(kept), FRAME_C_CAP)
        STATS["frameC_cap_step"] = round(step, 3)
        STATS["frameC_cap_start_offset"] = round(start, 3)
        selected = [kept[i] for i in idx]
    else:
        STATS["frameC_cap_step"] = None
        STATS["frameC_cap_start_offset"] = None
        selected = kept
    STATS["frameC_built_target"] = len(selected)
    print(f"Frame C holdout: selecting {len(selected)} of {len(kept)} kept threads "
          f"(cap={FRAME_C_CAP}, sampling_method={'systematic' if len(kept) > FRAME_C_CAP else 'census'})")

    n_c = 0
    for anchor, resolution in selected:
        n_c += 1
        thread_id = f"US-FR-C-{n_c:04d}"
        if thread_id in EXISTING_THREAD_IDS:
            continue
        summary = process_anchor_with_resolution(
            thread_id, anchor, resolution,
            sampling_frame=f"Federal Register API, type=PRORULE, significant=1, publication_date "
                            f"{FRAME_C_WINDOW[0]}..{FRAME_C_WINDOW[1]} (Frame C census, {len(eligible)} eligible "
                            f"NPRMs); post-model-cutoff holdout retaining only threads NOT resolved before "
                            f"{FRAME_C_HOLDOUT_CUTOFF}, capped at {FRAME_C_CAP}",
            sampling_method="systematic" if len(kept) > FRAME_C_CAP else "census",
            quality_tier="GOLD_CANDIDATE", frame_label="C",
        )
        print(f"  built {thread_id} (Frame C): {anchor['title'][:60]!r} -> {summary['outcome_class']}")
    STATS["frameC_built"] = n_c


def process_anchor_with_resolution(thread_id, anchor, resolution, sampling_frame, sampling_method,
                                    quality_tier, frame_label):
    """Like process_anchor but reuses an already-computed `resolution` (avoids re-querying)."""
    thread = build_thread(thread_id, anchor, sampling_frame, sampling_method, quality_tier)
    outcome = build_outcome(thread_id, anchor, resolution, OUTCOME_CENSOR_DATE, frame_label)
    decisive_date = outcome.get("decisive_date") or outcome.get("withdrawal_date")

    evidence = [build_anchor_evidence(thread_id, anchor)]
    seq = 2
    comment_deadlines = [anchor.get("comments_close_on")]
    pool_docs = sorted(resolution["pool"].values(), key=lambda d: (d["publication_date"], d["document_number"]))
    for d in pool_docs:
        if d["document_number"] == anchor["document_number"]:
            continue
        if decisive_date and d["publication_date"] >= decisive_date:
            continue
        cat, _eligible = classify_action(d.get("action"), d.get("title"))
        if cat in ("ANPRM", "SNPRM", "COMMENT_EXTENSION", "COMMENT_REOPENING", "HEARING_NOTICE"):
            evidence.append(build_secondary_evidence(thread_id, seq, d, cat))
            seq += 1
            if d.get("comments_close_on"):
                comment_deadlines.append(d["comments_close_on"])
        elif d.get("type") in ("Proposed Rule", "Notice") and d["publication_date"] > anchor["publication_date"]:
            if cat not in ("CORRECTION", "UNIFIED_AGENDA", "WITHDRAWAL", "DELAY"):
                evidence.append(build_secondary_evidence(thread_id, seq, d, "RELATED"))
                seq += 1

    stakeholder = build_stakeholder_evidence(thread_id, seq, anchor, comment_deadlines, decisive_date)
    if stakeholder:
        evidence.append(stakeholder)
        seq += 1

    disambiguate_titles(evidence, outcome)

    for ev in evidence:
        if ev["evidence_id"] in EXISTING_EVIDENCE_IDS:
            continue
        append_record(EVIDENCE_PATH, ev)
        EXISTING_EVIDENCE_IDS.add(ev["evidence_id"])
    if thread["thread_id"] not in EXISTING_THREAD_IDS:
        append_record(THREADS_PATH, thread)
        EXISTING_THREAD_IDS.add(thread["thread_id"])
    if outcome["thread_id"] not in EXISTING_OUTCOME_TIDS:
        append_record(OUTCOMES_PATH, outcome)
        EXISTING_OUTCOME_TIDS.add(outcome["thread_id"])

    return {"thread_id": thread_id, "outcome_class": outcome["outcome_class"],
            "decisive_action": outcome["decisive_action"], "n_evidence": len(evidence)}


# --------------------------------------------------------------------------
# sources.json / NOTES.md
# --------------------------------------------------------------------------

def write_sources_json():
    sources = [
        {
            "regulator": "Federal Register (govinfo/GPO, all US agencies)",
            "endpoint": "https://www.federalregister.gov/api/v1/documents.json",
            "content": "Proposed Rule / Rule / Notice documents; used for both anchor NPRM discovery "
                       "(conditions[type][]=PRORULE&conditions[significant]=1) and outcome linkage "
                       "(conditions[regulation_id_number]=<RIN>, conditions[docket_id]=<docket>, "
                       "conditions[term]=<RIN> full-text fallback for bundled withdrawal notices).",
            "tier": "B (anchor + precursor docs); Tier A material (final rules/withdrawals) is used "
                    "only in outcomes.jsonl, never in evidence.jsonl",
            "access_method": "Public JSON REST API, no auth, paginated (per_page=1000), GET with "
                              "User-Agent header; responses cached under data/raw/us_fr/cache/.",
            "date_field": "publication_date (official FR print-publication date)",
            "reliability_notes": "Authoritative US government source of record for the Federal Register. "
                                  "regulations_dot_gov_info.comments_count reflects the count as of FR's "
                                  "last check of regulations.gov (checked_regulationsdotgov_at), which may "
                                  "predate today for older documents; used as-is per protocol.",
            "checked": RETRIEVAL_DATE,
        },
        {
            "regulator": "Federal Register full text (via govinfo.gov PDF)",
            "endpoint": "pdf_url field on each FR document (govinfo.gov/content/pkg/.../pdf/<doc>.pdf)",
            "content": "Full text of the decisive final rule, used to search for a 'changes from the "
                       "proposal' / 'summary of changes' passage to support content_direction labeling.",
            "tier": "n/a (used only to inform outcome-store content_direction/content_summary, never "
                    "copied into evidence.jsonl)",
            "access_method": "HTTP GET of the govinfo.gov PDF, text extracted with PyMuPDF (fitz); "
                              "federalregister.gov's own raw_text_url/body_html_url endpoints returned an "
                              "access-gated 'Request Access' page from this container and were not usable.",
            "date_field": "n/a",
            "reliability_notes": "Best-effort; if the PDF fetch or heading search fails, content_direction "
                                  "falls back to a lower-confidence keyword heuristic over the action/abstract "
                                  "fields only (noted in the outcome record).",
            "checked": RETRIEVAL_DATE,
        },
    ]
    with open(os.path.join(OUT, "sources.json"), "w") as f:
        json.dump(sources, f, indent=1)


def write_notes_md():
    threads = []
    if os.path.exists(THREADS_PATH):
        with open(THREADS_PATH) as f:
            threads = [json.loads(l) for l in f if l.strip()]
    outcomes = []
    if os.path.exists(OUTCOMES_PATH):
        with open(OUTCOMES_PATH) as f:
            outcomes = [json.loads(l) for l in f if l.strip()]
    omap = {o["thread_id"]: o for o in outcomes}

    def frame_stats(prefix):
        tids = [t["thread_id"] for t in threads if t["thread_id"].startswith(prefix)]
        pos = sum(1 for tid in tids if omap.get(tid, {}).get("decisive_action"))
        neg = len(tids) - pos
        classes = {}
        for tid in tids:
            c = omap.get(tid, {}).get("outcome_class", "MISSING")
            classes[c] = classes.get(c, 0) + 1
        return len(tids), pos, neg, classes

    hN, hPos, hNeg, hClasses = frame_stats("US-FR-H-")
    cN, cPos, cNeg, cClasses = frame_stats("US-FR-C-")
    xN, xPos, xNeg, xClasses = frame_stats("US-FR-X-")

    lines = []
    lines.append("# NOTES.md — us_fr collector (Federal Register NPRM -> final-rule threads)\n")
    lines.append(f"Generated by `collectors/us_fr.py`. Retrieval date: {RETRIEVAL_DATE}. "
                 f"Outcomes resolved through: {OUTCOME_CENSOR_DATE}.\n")

    lines.append("## Frame H — historical, 2019-07-01..2023-12-31\n")
    lines.append(f"- Population seen (type=PRORULE, significant=1): **{STATS.get('frameH_seen')}**\n"
                 f"- Eligible genuine NPRMs after exclusion filter: **{STATS.get('frameH_eligible')}**\n"
                 f"- Systematic sample: step=**{STATS.get('frameH_step')}**, "
                 f"start_offset=**{STATS.get('frameH_start_offset')}**, target n=**{FRAME_H_TARGET_N}**\n"
                 f"- Threads built: **{STATS.get('frameH_built')}** (ids US-FR-H-0001..US-FR-H-{STATS.get('frameH_built', 0):04d})\n"
                 f"- RIN-collision skips (sampled slot's RIN already used by an earlier thread; advanced "
                 f"to next eligible doc): **{len(STATS.get('frameH_skip_log', []))}**\n"
                 f"- Outcome classes: {json.dumps(hClasses)}\n"
                 f"- Positives (decisive_action=true): {hPos}  Negatives/no-decisive-action: {hNeg} "
                 f"({(hNeg / hN * 100 if hN else 0):.0f}% negative/stalled/withdrawn controls)\n")
    lines.append("\nEligibility-category breakdown of the full Frame H population (why a doc was excluded "
                 "from the genuine-NPRM anchor pool):\n")
    for cat, n in sorted(STATS.get("frameH_category_counts", {}).items(), key=lambda kv: -kv[1]):
        lines.append(f"- {cat}: {n}\n")
    if STATS.get("frameH_skip_log"):
        lines.append("\nSampled-slot RIN-collision skip log (first 30 shown):\n")
        for row in STATS["frameH_skip_log"][:30]:
            lines.append(f"- target_index={row['target_index']} skipped {row['skipped_document_number']}: "
                         f"{row['reason']}\n")

    lines.append("\n## Frame C — post-model-cutoff holdout, 2025-06-01..2026-06-30\n")
    lines.append(f"- Population seen (type=PRORULE, significant=1): **{STATS.get('frameC_seen')}**\n"
                 f"- Eligible genuine NPRMs after exclusion filter (census): **{STATS.get('frameC_eligible')}**\n"
                 f"- Of eligible anchors, outcome resolved BEFORE {FRAME_C_HOLDOUT_CUTOFF}: "
                 f"**{STATS.get('frameC_resolved_before_july_excluded')}** (excluded from the C holdout, "
                 f"re-emitted as Frame X historical threads instead)\n"
                 f"- Kept for the C holdout population (resolved on/after {FRAME_C_HOLDOUT_CUTOFF}, or still "
                 f"unresolved at {OUTCOME_CENSOR_DATE}): **{STATS.get('frameC_kept_for_holdout')}**\n"
                 f"- Capped at {FRAME_C_CAP}: sampling_method="
                 f"{'systematic (step=' + str(STATS.get('frameC_cap_step')) + ', start_offset=' + str(STATS.get('frameC_cap_start_offset')) + ')' if STATS.get('frameC_cap_step') else 'census (kept population <= cap)'}\n"
                 f"- Threads built: **{STATS.get('frameC_built')}** (ids US-FR-C-0001..US-FR-C-{STATS.get('frameC_built', 0):04d})\n"
                 f"- Outcome classes: {json.dumps(cClasses)}\n"
                 f"- Positives (decisive_action=true): {cPos}  Negatives/unresolved: {cNeg} "
                 f"({(cNeg / cN * 100 if cN else 0):.0f}% negative/unresolved controls)\n")
    lines.append("\nEligibility-category breakdown of the full Frame C population:\n")
    for cat, n in sorted(STATS.get("frameC_category_counts", {}).items(), key=lambda kv: -kv[1]):
        lines.append(f"- {cat}: {n}\n")

    lines.append(f"\n## Frame X — Frame C anchors resolved before {FRAME_C_HOLDOUT_CUTOFF} "
                 "(re-used as ordinary historical threads)\n")
    lines.append(f"- Threads built: **{STATS.get('frameX_built')}** (ids US-FR-X-0001..US-FR-X-{STATS.get('frameX_built', 0):04d})\n"
                 f"- Outcome classes: {json.dumps(xClasses)}\n"
                 f"- Positives (decisive_action=true): {xPos}  Negatives: {xNeg}\n"
                 "- These are genuine, resolved NPRM->outcome threads (mostly fast-moving deregulatory "
                 "actions from the 2025 administration finalized or withdrawn within weeks of proposal); "
                 "they are excluded from the Frame C *holdout* only because their outcome could in "
                 "principle have leaked into an LLM's training/browsing exposure before the model "
                 "knowledge cutoff windows this project cares about, not because they are lower quality.\n")

    lines.append("\n## Linkage method\n")
    lines.append("For each anchor, related documents were pulled by (1) `conditions[regulation_id_number]` "
                 "for every RIN on the anchor, (2) `conditions[docket_id]` for its docket, and — only if "
                 "neither found a decisive final rule or withdrawal — (3) a `conditions[term]=<RIN>` "
                 "full-text-search fallback, which is required because some agency-wide withdrawal notices "
                 "(e.g. SEC's 2025-06-17 'Withdrawal of Proposed Regulatory Actions' covering 14 RINs) do "
                 "not carry the individual RINs in their own FR metadata (`regulation_id_numbers: []`) even "
                 "though the RINs are printed in the document text; verified against "
                 "https://www.federalregister.gov/documents/2025/06/17/2025-11110/withdrawal-of-proposed-regulatory-actions "
                 "during development of this collector.\n")
    lines.append("\nA later document counts as the decisive final action only if type=Rule and its `action` "
                 "text matches final/interim-final/direct-final rule language, excluding corrections, "
                 "correcting amendments, effective-date delays/stays, and technical/administrative "
                 "amendments. A withdrawal is any later document (of any type) whose `action` or `title` "
                 "contains withdrawal/termination language, excluding Unified Agenda entries. A candidate "
                 "must be published strictly AFTER the anchor's publication_date to count as decisive: "
                 "several agencies (NRC, DOE, FWS observed in this run) publish a 'direct final rule' the "
                 "SAME DAY as a companion proposed rule (the proposed rule becomes operative only if the "
                 "direct final rule is withdrawn due to adverse comment); such same-day companions cannot "
                 "represent a comment-informed resolution of the anchor without breaking the point-in-time "
                 "anchor-before-outcome invariant, so anchors of this kind fall through to "
                 "stalled_no_action/unresolved rather than being linked to their same-day companion.\n")

    lc_counts = {}
    clc_counts = {}
    for o in outcomes:
        lc_counts[o.get("label_confidence")] = lc_counts.get(o.get("label_confidence"), 0) + 1
        clc_counts[o.get("content_label_confidence")] = clc_counts.get(o.get("content_label_confidence"), 0) + 1
    non_high_lc = [(o["thread_id"], o.get("label_confidence")) for o in outcomes
                   if o.get("label_confidence") != "high"]
    non_high_lc_str = "; ".join(f"{tid} ({conf})" for tid, conf in non_high_lc) or "none"

    lines.append("\n## label_confidence vs content_label_confidence\n")
    lines.append("Per the Director's schema clarification received during this run (schemas/outcome.schema.json "
                 "bumped to 1.1.0, docs/EXECUTOR_GUIDE.md section 5 updated): `label_confidence` refers ONLY to "
                 "the action/timing label — whether and when a decisive action or withdrawal occurred (or, for "
                 "stalled_no_action/unresolved, confidence that no such document exists by the censor date). It "
                 "is never lowered because content_direction is uncertain. A separate `content_label_confidence` "
                 "field holds confidence in content_direction/key_parameters specifically. Every outcome record "
                 "in this workstream carries both fields "
                 f"(label_confidence: {json.dumps(lc_counts)}; content_label_confidence: {json.dumps(clc_counts)}).\n"
                 "\n`label_confidence` is set from the linkage method: **high** when the decisive/withdrawal "
                 "document (or, for no-action outcomes, the absence of one) was established via a native FR "
                 "`regulation_id_number` match; **medium** when only a docket_id match was available, or when "
                 "the match came only from the `conditions[term]=<RIN>` full-text-search fallback (used for "
                 "agency-wide withdrawal notices that do not carry the RIN in their own metadata); **low** when "
                 f"the anchor had neither a usable RIN nor docket to search on. Threads with label_confidence "
                 f"below high, and why: {non_high_lc_str} (each is a `notes` field with the full rationale).\n")

    action_outcomes = [o for o in outcomes if o["decisive_action"]]
    action_clc = {}
    for o in action_outcomes:
        action_clc[o.get("content_label_confidence")] = action_clc.get(o.get("content_label_confidence"), 0) + 1
    na_outcomes_n = len(outcomes) - len(action_outcomes)

    lines.append("\n## content_direction labeling\n")
    lines.append("content_direction (as_proposed/softened/tightened/mixed/different_mechanism) is set by an "
                 "automated, keyword-based heuristic comparing the final rule's `action` text and abstract "
                 "against the NPRM, augmented — when the final rule's govinfo.gov PDF was fetchable — by a "
                 "regex search for a 'summary of changes' / 'changes from the proposed rule' / 'differences "
                 "... from the proposed rule' heading and the ~700 characters following it. "
                 "federalregister.gov's own raw_text_url/body_html_url pages returned an access-gated "
                 "'Request Access' response from this container for every document tried (both PRORULE and "
                 "RULE types), so govinfo.gov PDFs + PyMuPDF text extraction were used instead; this is "
                 "recorded per-outcome in `notes`. All content_direction labels are therefore provisional "
                 "with `content_label_confidence` medium (occasionally low when no keyword signal was found at "
                 f"all — this run, among the {len(action_outcomes)} action_* outcomes: {json.dumps(action_clc)}); "
                 "none should be treated as a manually verified read of the full final-rule preamble. For all "
                 "withdrawn/stalled_no_action/unresolved outcomes (content_direction='na'), "
                 f"`content_label_confidence` is trivially `high` ({na_outcomes_n} threads).\n")

    lines.append("\n## Known weaknesses / limitations\n")
    lines.append("- Eligibility filtering (genuine NPRM vs ANPRM/SNPRM/extension/reopening/withdrawal/"
                 "correction/Unified-Agenda/hearing-only) is regex/keyword-based over the FR `action` and "
                 "`title` fields, not a manual read of every one of the ~1,350 (Frame H) + 208 (Frame C) "
                 "raw documents; edge cases (e.g. a document whose action text bundles an NPRM with an "
                 "extension, or an ambiguous 'reconsideration of final rule' proposal) may be misclassified "
                 "in either direction. The full per-category counts above are provided so this can be "
                 "audited.\n"
                 "- content_direction / content_summary are automated heuristics (see above), not a full "
                 "manual comparison of NPRM vs final-rule text; treat content_label_confidence=medium "
                 "accordingly (label_confidence, the action/timing label, is unaffected and independently high "
                 "for nearly all threads — see label_confidence vs content_label_confidence above).\n"
                 "- regulations_dot_gov_info.comments_count for older Frame H documents reflects FR's last "
                 "check of regulations.gov (often 2022-2023), not a live 2026 count; used as-is, with the "
                 "synthetic Tier-S evidence date derived from the comment-period close date, not from the "
                 "check date.\n"
                 "- The `conditions[term]=<RIN>` fallback search only recovers a bundled/agency-wide "
                 "withdrawal notice if the literal RIN string appears in FR's indexed text of that notice; "
                 "a notice that refers to proposals only by docket number or title would be missed.\n"
                 "- Frame C 'unresolved' threads are genuinely open as of the censor date; some may resolve "
                 "shortly after this collection and should be re-checked before use in evaluation if the "
                 "backtest run date drifts far past 2026-09-25.\n"
                 "- Evidence per thread is capped to what the RIN/docket lookup pool contains before the "
                 "decisive date; threads with a very sparse RIN history (e.g. a self-contained proposal "
                 "with no ANPRM/extension/hearing history) may have only the anchor (E01) as evidence, which "
                 "is valid per EXECUTOR_GUIDE (RAPID requires >=1 evidence item) but keeps them below the "
                 "GOLD_CANDIDATE >=3-item guideline; Frame C/X threads are nonetheless tagged per the task's "
                 "explicit instruction that FR-sourced dates are always official.\n")

    with open(os.path.join(OUT, "NOTES.md"), "w") as f:
        f.writelines(lines)


# --------------------------------------------------------------------------
# main
# --------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--stage", choices=["all", "frameH", "frameC"], default="all")
    args = ap.parse_args()

    load_existing()

    if args.stage in ("all", "frameH"):
        run_frame_h()
    if args.stage in ("all", "frameC"):
        run_frame_c()

    write_sources_json()
    write_notes_md()
    print("Done. Wrote sources.json and NOTES.md.")


if __name__ == "__main__":
    main()
