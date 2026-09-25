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


ALLOWED = {
    "set_evidence": {"publication_date", "first_known_date", "extracted_claims", "content_excerpt", "tier", "title",
                     "original_or_revised", "version_confidence"},
    "set_outcome": {"decisive_date", "decisive_action", "outcome_class", "withdrawal_date", "content_direction",
                    "content_label_confidence", "label_confidence"},
    "set_thread": {"neutral_title", "issue_summary_neutral"},
}


def apply_patches(threads, evidence, outcomes, excluded):
    """Apply auditor patches (data/audits/patches/*.jsonl) on top of executor data. Returns patched lists + log."""
    pdir = os.path.join(DATA, "audits", "patches")
    log = []
    if not os.path.isdir(pdir):
        return threads, evidence, outcomes, log
    tm = {t["thread_id"]: t for t in threads}
    om = {o["thread_id"]: o for o in outcomes}
    em = {e["evidence_id"]: e for e in evidence}
    dropped, excl = set(), set()
    for fn in sorted(os.listdir(pdir)):
        for p in read_jsonl(os.path.join(pdir, fn)):
            op = p.get("op")
            ok = False
            if op == "set_evidence" and p.get("evidence_id") in em and p.get("field") in ALLOWED[op]:
                em[p["evidence_id"]][p["field"]] = p["value"]; ok = True
            elif op == "set_outcome" and p.get("thread_id") in om and p.get("field") in ALLOWED[op]:
                om[p["thread_id"]][p["field"]] = p["value"]; ok = True
            elif op == "set_thread" and p.get("thread_id") in tm and p.get("field") in ALLOWED[op]:
                tm[p["thread_id"]][p["field"]] = p["value"]; ok = True
            elif op == "drop_evidence" and p.get("evidence_id") in em:
                dropped.add(p["evidence_id"]); ok = True
            elif op == "exclude_thread" and p.get("thread_id") in tm:
                excl.add(p["thread_id"]); ok = True
            log.append({**p, "applied": ok, "file": fn})
    for tid in excl:
        excluded.append({"thread_id": tid, "reason": "audit_exclude_patch"})
    threads = [t for t in threads if t["thread_id"] not in excl]
    outcomes = [o for o in outcomes if o["thread_id"] not in excl]
    anchors = {t["anchor_evidence_id"] for t in threads}
    evidence = [e for e in evidence if e["thread_id"] not in excl and (e["evidence_id"] not in dropped or e["evidence_id"] in anchors)]
    for t in threads:  # keep anchor_date consistent with a patched anchor item; recompute stratum
        a = em.get(t["anchor_evidence_id"])
        if a:
            t["anchor_date"] = a["publication_date"]
        o = om[t["thread_id"]]
        rd = resolution_date(o)
        t["stratum"] = "CLEAN" if (rd is None or d(rd) >= d(CLEAN_BOUNDARY)) else "HIST"
    return threads, evidence, outcomes, log


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

    threads, evidence, outcomes, patch_log = apply_patches(threads, evidence, outcomes, excluded)
    # re-lint after patches: invalid outcomes exclude the thread; post-outcome evidence is dropped (logged)
    from .lint import lint_evidence, lint_outcome
    omap = {o["thread_id"]: o for o in outcomes}
    bad = {t["thread_id"] for t in threads if any(l == "error" for l, _ in lint_outcome(omap[t["thread_id"]], t))}
    for tid in bad:
        excluded.append({"thread_id": tid, "reason": "outcome_invalid_after_patch"})
    threads = [t for t in threads if t["thread_id"] not in bad]
    outcomes = [o for o in outcomes if o["thread_id"] not in bad]
    evidence = [e for e in evidence if e["thread_id"] not in bad]
    kept_ev = []
    for e in evidence:
        errs = [m for lvl, m in lint_evidence(e, omap.get(e["thread_id"])) if lvl == "error"]
        if errs:
            patch_log.append({"op": "auto_drop_evidence", "evidence_id": e["evidence_id"], "reason": errs[0]})
        else:
            kept_ev.append(e)
    evidence = kept_ev
    # GOLD = audited clean/minor-fixed + gold_eligible; audit exclusions honoured
    audits = []
    adir = os.path.join(DATA, "audits")
    for fn in sorted(os.listdir(adir)) if os.path.isdir(adir) else []:
        if fn.startswith("audit_") and fn.endswith(".jsonl"):
            audits += read_jsonl(os.path.join(adir, fn))
    latest = {}
    for a in audits:
        latest[a["thread_id"]] = a
    drop = {tid for tid, a in latest.items() if a["verdict"] == "contaminated_exclude"}
    for t in threads:
        a = latest.get(t["thread_id"])
        t["audited"] = a is not None
        t["audit_verdict"] = a["verdict"] if a else None
        if a and a["verdict"] in ("clean", "minor_issue_fixed", "contaminated_rebuild") and a.get("gold_eligible"):
            t["quality"] = "GOLD"
    for tid in drop:
        excluded.append({"thread_id": tid, "reason": "audit_contaminated_exclude"})
    threads = [t for t in threads if t["thread_id"] not in drop]
    outcomes = [o for o in outcomes if o["thread_id"] not in drop]
    evidence = [e for e in evidence if e["thread_id"] not in drop]
    write_jsonl(os.path.join(DATA, "derived", "patch_log.jsonl"), patch_log)

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
        "by_quality": dict(Counter(t["quality"] for t in threads)),
        "audited": sum(1 for t in threads if t.get("audited")),
        "patches_applied": sum(1 for x in patch_log if x.get("applied")),
        "auto_dropped_evidence": sum(1 for x in patch_log if x.get("op") == "auto_drop_evidence"),
    }
    json.dump(summary, open(os.path.join(DATA, "derived", "build_summary.json"), "w"), indent=1)
    if verbose:
        print(json.dumps(summary, indent=1))
    return summary


if __name__ == "__main__":
    build()
