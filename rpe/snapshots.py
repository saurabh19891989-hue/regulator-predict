"""Point-in-time snapshot construction (Design T and Design K) and ablation arms.

A snapshot = (thread, cutoff date, arm) → the exact list of evidence items a blind forecaster may see.
Outcome-derived fields (T, pseudo-anchor, positive/negative, offsets) live ONLY in the snapshot index,
never in rendered packets.

Usage: python3 -m rpe.snapshots   → writes data/snapshots/index.jsonl
"""
import json
import os
import random
from collections import Counter, defaultdict

from .common import CENSOR_DATE, DATA, add_days, d, days_between, read_jsonl, sha256_text, write_jsonl

T_OFFSETS = [365, 270, 180, 120, 90, 60, 30, 14, 7]
K_CUTOFFS = ["2026-06-26", "2026-07-26", "2026-08-25"]   # Design K (CLEAN, prospective)
CENSOR_LAST = "2026-09-24"                               # last fully observed day
ARMS = {
    "ALL": {"B", "C", "S", "D"},
    "B_ONLY": {"B"},
    "C_ONLY": {"C"},
    "B_PLUS_C": {"B", "C"},                 # == FULL_TRAJECTORY (all official items)
    "B_C_STAKEHOLDERS": {"B", "C", "S"},
    "B_C_STAKEHOLDERS_PLUS_NEWS": {"B", "C", "S", "D"},
    "LATEST_DOCUMENT_ONLY": {"B", "C"},     # restricted to the single most recent official item
    "TITLE_ONLY": set(),
}
OFFICIAL = {"B", "C"}


def seeded_rng(*parts):
    return random.Random(int(sha256_text("|".join(map(str, parts)))[:12], 16))


def available_date(ev):
    fk = ev.get("first_known_date")
    pub = ev["publication_date"]
    return max(pub, fk) if fk else pub


def pseudo_anchors(threads, outcomes):
    """T for positives; seeded matched pseudo-anchor T* for no-action threads."""
    omap = {o["thread_id"]: o for o in outcomes}
    gaps = defaultdict(list)
    for t in threads:
        o = omap[t["thread_id"]]
        if o["decisive_action"]:
            gaps[t["family"]].append(days_between(t["anchor_date"], o["decisive_date"]))
    pooled = sorted(g for v in gaps.values() for g in v)
    res = {}
    for t in threads:
        o = omap[t["thread_id"]]
        if o["decisive_action"]:
            res[t["thread_id"]] = {"anchor_T": o["decisive_date"], "pseudo": False}
            continue
        pool = sorted(gaps[t["family"]]) if len(gaps[t["family"]]) >= 5 else pooled
        if not pool:
            pool = [180]
        g = seeded_rng("pseudo", t["thread_id"]).choice(pool)
        T = add_days(t["anchor_date"], g)
        cap = CENSOR_LAST
        if o.get("withdrawal_date"):
            cap = min(cap, add_days(o["withdrawal_date"], -1))
        T = min(T, cap)
        res[t["thread_id"]] = {"anchor_T": T, "pseudo": True, "gap_days": g}
    return res


def label(outcome, cutoff, h):
    """1 / 0 / None(censored) for 'decisive action within (cutoff, cutoff+h]'."""
    dd = outcome.get("decisive_date")
    end = add_days(cutoff, h)
    if dd and d(cutoff) < d(dd) <= d(end):
        return 1
    if dd and d(dd) <= d(cutoff):
        return None  # already resolved (should not happen for valid snapshots)
    if d(end) <= d(CENSOR_LAST):
        return 0
    return None


def select_items(items, arm, cutoff):
    vis = [e for e in items if d(available_date(e)) <= d(cutoff)]
    classes = ARMS[arm]
    sel = [e for e in vis if e["tier"] in classes]
    if arm == "LATEST_DOCUMENT_ONLY":
        off = sorted([e for e in vis if e["tier"] in OFFICIAL], key=lambda e: (available_date(e), e["evidence_id"]))
        sel = off[-1:] if off else []
    present = Counter(e["tier"] for e in vis)
    n_official = present["B"] + present["C"]
    avail, why = True, ""
    if arm == "C_ONLY" and present["C"] == 0:
        avail, why = False, "no tier C by cutoff"
    elif arm == "B_ONLY" and present["B"] == 0:
        avail, why = False, "no tier B by cutoff"
    elif arm == "B_C_STAKEHOLDERS" and present["S"] == 0:
        avail, why = False, "no stakeholder items by cutoff"
    elif arm == "B_C_STAKEHOLDERS_PLUS_NEWS" and present["D"] == 0:
        avail, why = False, "no news by cutoff"
    elif arm == "LATEST_DOCUMENT_ONLY" and n_official < 2:
        avail, why = False, "fewer than 2 official items (identical to B_PLUS_C)"
    elif arm not in ("TITLE_ONLY",) and not sel:
        avail, why = False, "no items in arm classes"
    sel = sorted(sel, key=lambda e: (available_date(e), e["evidence_id"]))
    return sel, avail, why, dict(present)


def build_index(arms=None):
    arms = arms or list(ARMS)
    threads = read_jsonl(os.path.join(DATA, "threads", "threads.jsonl"))
    outcomes = read_jsonl(os.path.join(DATA, "outcomes", "outcomes.jsonl"))
    evidence = read_jsonl(os.path.join(DATA, "evidence", "evidence.jsonl"))
    omap = {o["thread_id"]: o for o in outcomes}
    ev_by = defaultdict(list)
    for e in evidence:
        ev_by[e["thread_id"]].append(e)
    anchors = pseudo_anchors(threads, outcomes)
    rows = []

    def add(t, cutoff, design, offset):
        o = omap[t["thread_id"]]
        rd = o.get("decisive_date") or o.get("withdrawal_date")
        if d(cutoff) < d(t["anchor_date"]):
            return
        if rd and d(cutoff) >= d(rd):
            return
        for arm in arms:
            sel, avail, why, present = select_items(ev_by[t["thread_id"]], arm, cutoff)
            key = f"{t['thread_id']}|{cutoff}|{arm}|{design}"
            sid = "S" + sha256_text("snap|" + key)[:10]
            rows.append({
                "snapshot_id": sid, "thread_id": t["thread_id"], "family": t["family"],
                "stratum": t["stratum"], "quality": t["quality"], "design": design, "offset": offset,
                "cutoff_date": cutoff, "arm": arm, "available": avail, "unavailable_reason": why,
                "evidence_ids": [e["evidence_id"] for e in sel], "classes_present": present,
                "clean_snapshot": d(cutoff) >= d(K_CUTOFFS[0]),
                "is_pseudo_anchor": anchors[t["thread_id"]]["pseudo"],
                "anchor_T": anchors[t["thread_id"]]["anchor_T"],
                "labels": {str(h): label(o, cutoff, h) for h in (7, 30, 60, 90, 180)},
            })

    for t in threads:
        T = anchors[t["thread_id"]]["anchor_T"]
        for k in T_OFFSETS:
            add(t, add_days(T, -k), "T", f"T-{k}")
        if t["stratum"] == "CLEAN":
            for c in K_CUTOFFS:
                add(t, c, "K", f"K@{c}")
    # dedupe identical design-T / design-K snapshots of the same thread/cutoff/arm (keep T)
    seen, out = set(), []
    for r in rows:
        k = (r["thread_id"], r["cutoff_date"], r["arm"])
        if k in seen:
            continue
        seen.add(k)
        out.append(r)
    write_jsonl(os.path.join(DATA, "snapshots", "index.jsonl"), out)
    summ = {
        "snapshots": len(out),
        "available_by_arm": dict(Counter(r["arm"] for r in out if r["available"])),
        "threads_with_valid_T_snapshot": len({r["thread_id"] for r in out if r["design"] == "T" and r["arm"] == "ALL" and r["available"]}),
        "design_K_ALL": sum(1 for r in out if r["design"] == "K" and r["arm"] == "ALL" and r["available"]),
    }
    json.dump(summ, open(os.path.join(DATA, "derived", "snapshot_summary.json"), "w"), indent=1)
    return out, summ


if __name__ == "__main__":
    _, s = build_index()
    print(json.dumps(s, indent=1))
