"""Validate a workstream directory (schemas + referential integrity + leakage lint).

Usage: python3 -m rpe.validate data/raw/<workstream> [--quiet]
Exit code 1 if any error.
"""
import json
import os
import sys
from collections import Counter

import jsonschema

from .common import load_schema, read_jsonl
from .lint import lint_evidence, lint_outcome, lint_thread_text


def validate_dir(path, quiet=False):
    threads = read_jsonl(os.path.join(path, "threads.jsonl"))
    evidence = read_jsonl(os.path.join(path, "evidence.jsonl"))
    outcomes = read_jsonl(os.path.join(path, "outcomes.jsonl"))
    sch = {k: load_schema(k) for k in ("thread", "evidence", "outcome")}
    errors, warnings = [], []

    def chk(kind, rec, key):
        for e in jsonschema.Draft202012Validator(sch[kind]).iter_errors(rec):
            errors.append(f"{kind} {rec.get(key)}: schema: {e.message[:200]} at {list(e.path)}")

    for t in threads:
        chk("thread", t, "thread_id")
    for e in evidence:
        chk("evidence", e, "evidence_id")
    for o in outcomes:
        chk("outcome", o, "thread_id")

    tids = Counter(t["thread_id"] for t in threads)
    for k, n in tids.items():
        if n > 1:
            errors.append(f"duplicate thread_id {k}")
    eids = Counter(e["evidence_id"] for e in evidence)
    for k, n in eids.items():
        if n > 1:
            errors.append(f"duplicate evidence_id {k}")
    tmap = {t["thread_id"]: t for t in threads}
    omap = {o["thread_id"]: o for o in outcomes}
    emap = {e["evidence_id"]: e for e in evidence}
    for e in evidence:
        if e["thread_id"] not in tmap:
            errors.append(f"evidence {e['evidence_id']} references unknown thread {e['thread_id']}")
    for t in threads:
        tid = t["thread_id"]
        if tid not in omap:
            errors.append(f"thread {tid} has no outcome record")
        a = emap.get(t["anchor_evidence_id"])
        if not a:
            errors.append(f"thread {tid}: anchor evidence {t['anchor_evidence_id']} missing")
        else:
            if a["publication_date"] != t["anchor_date"]:
                errors.append(f"thread {tid}: anchor_date != anchor evidence publication_date")
            if a["tier"] != "B":
                warnings.append(f"thread {tid}: anchor evidence is tier {a['tier']} (expected B)")
        for lvl, msg in lint_thread_text(t):
            (errors if lvl == "error" else warnings).append(f"thread {tid}: {msg}")
        if tid in omap:
            for lvl, msg in lint_outcome(omap[tid], t):
                (errors if lvl == "error" else warnings).append(f"outcome {tid}: {msg}")
    for e in evidence:
        for lvl, msg in lint_evidence(e, omap.get(e["thread_id"])):
            (errors if lvl == "error" else warnings).append(f"evidence {e['evidence_id']}: {msg}")
    for o in outcomes:
        if o["thread_id"] not in tmap:
            errors.append(f"outcome for unknown thread {o['thread_id']}")

    stats = {
        "threads": len(threads), "evidence": len(evidence), "outcomes": len(outcomes),
        "tiers": dict(Counter(e["tier"] for e in evidence)),
        "outcome_classes": dict(Counter(o["outcome_class"] for o in outcomes)),
        "positives": sum(1 for o in outcomes if o["decisive_action"]),
        "negatives": sum(1 for o in outcomes if not o["decisive_action"]),
        "gold_candidates": sum(1 for t in threads if t.get("quality_tier_proposed") == "GOLD_CANDIDATE"),
        "errors": len(errors), "warnings": len(warnings),
    }
    if not quiet:
        for m in errors:
            print("ERROR  ", m)
        for m in warnings:
            print("WARN   ", m)
    print(json.dumps(stats, indent=1))
    return errors, warnings, stats


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    errs, _, _ = validate_dir(args[0], quiet="--quiet" in sys.argv)
    sys.exit(1 if errs else 0)
