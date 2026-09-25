"""Merge validated workstreams into the canonical stores.

  data/threads/threads.jsonl     thread records + stratum/quality/family (no outcome fields)
  data/evidence/evidence.jsonl   Tier B/C/S/D evidence (incl. merged US reginfo agenda/OIRA items)
  data/outcomes/outcomes.jsonl   SEALED outcome labels — never rendered into packets

Usage: python3 -m rpe.build
"""
import importlib.util
import json
import re
import os
import sys
from collections import Counter, defaultdict

from .common import CENSOR_DATE, DATA, ROOT, MODEL_KNOWLEDGE_CUTOFF, add_days, d, read_jsonl, write_jsonl
from .validate import validate_dir

LATE_BOUNDARY = add_days(MODEL_KNOWLEDGE_CUTOFF, 1)  # post-published-cutoff outcome; never described as guaranteed clean
SKIP_DIRS = {"us_reginfo"}


LATE_ANCHOR_MIN = "2025-06-01"  # unresolved threads count as LATE only if initiated recently


def stratum_of(t, o):
    """LATE = resolution on/after the stated model cutoff, or a RECENT proposal still unresolved.
    Old unresolved proposals are HIST: their non-action up to mid-2026 is knowable from training data."""
    rd = resolution_date(o)
    if rd:
        return "LATE" if d(rd) >= d(LATE_BOUNDARY) else "HIST"
    return "LATE" if d(t["anchor_date"]) >= d(LATE_ANCHOR_MIN) else "HIST"


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


COMPLETED_RE = re.compile(r"\s*Review completed (\d{4}-\d{2}-\d{2}), decision: ([^.]*)\.?")


def split_oira(items):
    """An OIRA 'received' item must not carry its completion (a later event). Split into two dated items."""
    out = []
    for it in items:
        if it.get("document_type") != "oira_review_received":
            out.append(it)
            continue
        txt = it.get("content_excerpt", "")
        m = COMPLETED_RE.search(txt)
        rec = dict(it)
        rec["content_excerpt"] = COMPLETED_RE.sub("", txt).strip()
        rec["extracted_claims"] = [c for c in it.get("extracted_claims", []) if "completed" not in c.lower()]
        out.append(rec)
        if m:
            comp = dict(it)
            comp["document_type"] = "oira_review_concluded"
            comp["publication_date"] = m.group(1)
            comp["title"] = it["title"].replace("review received", "review concluded")
            comp["content_excerpt"] = rec["content_excerpt"].replace("review received", "review concluded on " + m.group(1) + " (received") + f"). Decision: {m.group(2)}."
            comp["extracted_claims"] = [f"OIRA concluded EO 12866 review on {m.group(1)}; decision: {m.group(2)}."]
            out.append(comp)
    return out


def merge_reginfo(threads, outcomes, evidence, reginfo):
    """Attach Unified Agenda + OIRA precursor items to US-FR threads, strictly before resolution."""
    added = 0
    omap = {o["thread_id"]: o for o in outcomes}
    rdir = os.path.join(DATA, "raw", "us_reginfo")
    full = os.path.join(rdir, "agenda_entries.jsonl")
    sub = os.path.join(rdir, "agenda_entries_sampled.jsonl")
    want = set()
    for t in threads:
        if t["thread_id"].startswith("US-FR") and t.get("rin"):
            want |= {r.strip() for r in str(t["rin"]).replace(";", ",").split(",") if r.strip()}
    src = full if os.path.exists(full) else sub
    ag_by = defaultdict(list)
    for e in read_jsonl(src):
        if e.get("rin") in want:
            ag_by[e["rin"]].append(e)
    if src == full:  # refresh the committed subset (full bulk file is gitignored)
        write_jsonl(sub, [e for r in sorted(ag_by) for e in ag_by[r]])
    editions = json.load(open(os.path.join(rdir, "agenda_editions.json")))
    oi_by = defaultdict(list)
    for r in read_jsonl(os.path.join(rdir, "oira_reviews.jsonl")):
        oi_by[r.get("rin")].append(r)
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
                items += list(reginfo.agenda_evidence_for_rin(rin, before, ag_by.get(rin, []), editions) or [])
                items += list(reginfo.oira_evidence_for_rin(rin, before, oi_by.get(rin, [])) or [])
            except Exception as e:
                print(f"reginfo merge failed for {rin}: {e}", file=sys.stderr)
                continue
            items = split_oira(items)
            for i, it in enumerate(items):
                key = (it.get("document_type"), it.get("publication_date"), it.get("title"))
                if key in seen:
                    continue
                seen.add(key)
                it = dict(it)
                tag = {"regulatory_agenda_entry": "AG", "oira_review_received": "OR", "oira_review_concluded": "OC"}.get(it.get("document_type"), "RG")
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
        t["stratum"] = stratum_of(t, om[t["thread_id"]])
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
            t["stratum"] = stratum_of(t, o)
            t["quality"] = "RAPID"          # promoted to GOLD only by audit (rpe.audit)
            so = t.get("sampling_origin")
            if so not in ("precursor_population", "outcome_backfill", "purposive"):
                so = "precursor_population" if t.get("sampling_method") in ("census", "systematic", "random") else "purposive"
            t["sampling_origin"] = so
            threads.append(t)
            outcomes.append(o)
        keep = {t["thread_id"] for t in threads}
        evidence += [e for e in ev if e["thread_id"] in keep]
        per_ws[ws] = {"threads_in": len(th), "kept": sum(1 for t in th if t["thread_id"] in keep), "errors": len(errs)}

    reginfo = load_reginfo()
    has_ri = os.path.exists(os.path.join(DATA, "raw", "us_reginfo", "agenda_editions.json"))
    added = merge_reginfo(threads, outcomes, evidence, reginfo) if (reginfo and has_ri) else 0

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
        if a and a["verdict"] in ("clean", "minor_issue_fixed") and a.get("gold_eligible"):
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
        "by_sampling_origin": dict(Counter(t["sampling_origin"] for t in threads)),
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
