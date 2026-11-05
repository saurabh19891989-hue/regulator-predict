"""Find likely duplicate events across theme files (to be resolved in events/dedup.json by the Director).

Run: python3 -m market_impact.mi.event_dups
"""
import glob
import json
import os
import re
from datetime import date

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STOP = {"the", "of", "and", "in", "on", "to", "a", "for", "by", "with", "india", "indian", "us", "2026", "2027", "ev"}


def toks(s):
    return {w for w in re.findall(r"[a-z0-9]+", s.lower()) if w not in STOP and len(w) > 2}


def d(s):
    s = str(s)
    try:
        return date.fromisoformat(s[:10]) if len(s) >= 10 else date.fromisoformat(s[:7] + "-15")
    except ValueError:
        return None


def main():
    evs = []
    for p in sorted(glob.glob(os.path.join(HERE, "events", "*.json"))):
        if p.endswith("dedup.json"):
            continue
        for e in json.load(open(p)).get("events", []):
            evs.append((os.path.basename(p), e))
    out = []
    for i in range(len(evs)):
        for j in range(i + 1, len(evs)):
            (fa, a), (fb, b) = evs[i], evs[j]
            na = {s["node"] for s in a.get("entry_shocks", [])}
            nb = {s["node"] for s in b.get("entry_shocks", [])}
            jac = len(na & nb) / max(1, len(na | nb))
            tt = len(toks(a["event_id"] + " " + a.get("title", "")) & toks(b["event_id"] + " " + b.get("title", "")))
            da, db = d(a.get("date")), d(b.get("date"))
            close = da and db and abs((da - db).days) <= 75
            same_kind = (a.get("status") == "occurred") == (b.get("status") == "occurred")
            score = jac + 0.15 * tt + (0.3 if close else 0)
            if same_kind and score >= 0.8 and (jac >= 0.34 or tt >= 2):
                out.append((round(score, 2), fa, a["event_id"], a.get("status"), a.get("date"), fb, b["event_id"], b.get("status"), b.get("date")))
    for r in sorted(out, reverse=True):
        print(*r, sep=" | ")
    print(len(out), "candidate pairs among", len(evs), "events")


if __name__ == "__main__":
    main()
