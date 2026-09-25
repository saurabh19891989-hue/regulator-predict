"""Merge validated workstreams into the canonical stores.

  data/threads/threads.jsonl     thread records + stratum/quality/family (no outcome fields)
  data/evidence/evidence.jsonl   Tier B/C/S/D evidence (incl. merged US reginfo agenda/OIRA items)
  data/outcomes/outcomes.jsonl   SEALED outcome labels — never rendered into packets

Usage: python3 -m rpe.build
"""
import importlib.util
import json
import os
import sys
from collections import Counter

from .common import CENSOR_DATE, DATA, ROOT, add_days, d, read_jsonl, write_jsonl
from .validate import validate_dir

CLEAN_BOUNDARY = "2026-07-01"   # outcome resolved on/after this date → cannot be in forecaster training data
SKIP_DIRS = {"us_reginfo"}


def family_of(thread_id):
    p = thread_id.split("-")
    return f"{p[0]}-{p[1]}"


def resolution_date(o):
    return o.get("decisive_date") or o.get("withdrawal_date")


def load_reginfo():
    path = os.path.join(ROOT, "collectors", "reginfo.py")
    if not os.path.exists(path):
        return None
    spec = importlib.util.spec_from_file_location("reginfo", path)
    mod = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(mod)
    except Exception as e:  # collector still under construction
        print("reginfo import failed:", e, file=sys.stderr)
        return None
    return mod


def merge_reginfo(threads, outcomes, evidence, reginfo):
    """Attach Unified Agenda + OIRA precursor items to US-FR threads, strictly before resolution."""
    added = 0
    omap = {o["thread_id"]: o for o in outcomes}
    for t in threads:
        if not t["thread_id"].startswith("US-FR") or not t.get("rin"):
            continue
        o = omap[t["thread_id"]]
        before = resolution_date(o) or add_days(CENSOR_DATE, 1)
        rins = [r.strip() for r in str(t["rin"]).replace(";", ",").split(",") if r.strip()]
        seen = set()
        for rin in rins:
            items = []
            try:
                items += list(reginfo.agenda_evidence_for_rin(rin, before) or [])
                items += list(reginfo.oira_evidence_for_rin(rin, before) or [])
            except Exception as e:
                print(f"reginfo merge failed for {rin}: {e}", file=sys.stderr)
                continue
            for i, it in enumerate(items):
                key = (it.get("document_type"), it.get("publication_date"), it.get("title"))
                if key in seen:
                    continue
                seen.add(key)
                it = dict(it)
                tag = "AG" if it.get("document_type") == "regulatory_agenda_entry" else "OI"
                it["evidence_id"] = f"{t['thread_id']}-{tag}{len(seen):02d}"
                it["thread_id"] = t["thread_id"]
                it.setdefault("regulator", t["regulator"])
                it.setdefault("jurisdiction", t["jurisdiction"])
                it.setdefault("tier", "B")
                it.setdefault("retrieval_date", CENSOR_DATE)
                it.setdefault("original_or_revised", "original")
                it.setdefault("version_confidence", "high")
                it.setdefault("extracted_claims", [])
                it.setdefault("first_known_date", None)
                if d(it["publication_date"]) >= d(before):
                    continue
                evidence.append(it)
                added += 1
    return added


def build(verbose=True):
    raw = os.path.join(DATA, "raw")
    threads, evidence, outcomes, excluded = [], [], [], []
    per_ws = {}
    for ws in sorted(os.listdir(raw)):
        p = os.path.join(raw, ws)
        if ws in SKIP_DIRS or not os.path.isdir(p) or not os.path.exists(os.path.join(p, "threads.jsonl")):
            continue
        errs, _, stats = validate_dir(p, quiet=True)
        th = read_jsonl(os.path.join(p, "threads.jsonl"))
        ev = read_jsonl(os.path.join(p, "evidence.jsonl"))
        oc = read_jsonl(os.path.join(p, "outcomes.jsonl"))
        bad = set()
        for m in errs:  # exclude only the threads an error refers to
            for t in th:
                if t["thread_id"] in m:
                    bad.add(t["thread_id"])
            for e in ev:
                if e["evidence_id"] in m:
                    bad.add(e["thread_id"])
        omap = {o["thread_id"]: o for o in oc}
        for t in th:
            tid = t["thread_id"]
            o = omap.get(tid)
            if tid in bad or o is None:
                excluded.append({"thread_id": tid, "reason": "validation_error" if tid in bad else "no_outcome"})
                continue
            if o.get("label_confidence") == "low":
                excluded.append({"thread_id": tid, "reason": "low_label_confidence"})
                continue
            t = dict(t)
            t["family"] = family_of(tid)
            rd = resolution_date(o)
            t["stratum"] = "CLEAN" if (rd is None or d(rd) >= d(CLEAN_BOUNDARY)) else "HIST"
            t["quality"] = "RAPID"          # promoted to GOLD only by audit (rpe.audit)
            threads.append(t)
            outcomes.append(o)
        keep = {t["thread_id"] for t in threads}
        evidence += [e for e in ev if e["thread_id"] in keep]
        per_ws[ws] = {"threads_in": len(th), "kept": sum(1 for t in th if t["thread_id"] in keep), "errors": len(errs)}

    reginfo = load_reginfo()
    added = merge_reginfo(threads, outcomes, evidence, reginfo) if reginfo else 0

    # apply GOLD promotions from audits, if any
    gold_path = os.path.join(DATA, "audits", "gold_promotions.json")
    if os.path.exists(gold_path):
        gold = set(json.load(open(gold_path)))
        for t in threads:
            if t["thread_id"] in gold:
                t["quality"] = "GOLD"

    write_jsonl(os.path.join(DATA, "threads", "threads.jsonl"), threads)
    write_jsonl(os.path.join(DATA, "evidence", "evidence.jsonl"), evidence)
    write_jsonl(os.path.join(DATA, "outcomes", "outcomes.jsonl"), outcomes)
    write_jsonl(os.path.join(DATA, "threads", "excluded.jsonl"), excluded)
    summary = {
        "workstreams": per_ws, "threads": len(threads), "evidence": len(evidence), "reginfo_items_added": added,
        "excluded": dict(Counter(x["reason"] for x in excluded)),
        "by_family": dict(Counter(t["family"] for t in threads)),
        "by_stratum": dict(Counter(t["stratum"] for t in threads)),
        "positives": sum(1 for o in outcomes if o["decisive_action"]),
        "negatives": sum(1 for o in outcomes if not o["decisive_action"]),
        "outcome_classes": dict(Counter(o["outcome_class"] for o in outcomes)),
        "tiers": dict(Counter(e["tier"] for e in evidence)),
    }
    json.dump(summary, open(os.path.join(DATA, "derived", "build_summary.json"), "w"), indent=1)
    if verbose:
        print(json.dumps(summary, indent=1))
    return summary


if __name__ == "__main__":
    build()
