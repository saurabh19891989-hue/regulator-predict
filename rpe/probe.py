"""Memorisation recall probe (negative control for training-data leakage).

Asks the forecaster model, with NO evidence, whether it remembers what happened to each matter after the anchor
date. Threads it recalls correctly are flagged; primary results are re-estimated excluding them.

Usage:
  python3 -m rpe.probe make <run> --size 40
  python3 -m rpe.probe score <run>      → data/audits/memorisation_probe.jsonl
"""
import argparse
import json
import os

from .common import DATA, append_jsonl, d, days_between, now_iso, read_jsonl, sha256_text
from .packets import FC_ROOT, STUB

HEADER = """# RECALL QUESTIONNAIRE (research on model memory — not a forecasting task)
Below are {n} regulatory matters, each identified by regulator, a short title and the date the matter was
initiated. For each, report ONLY what you remember from your training data about what happened AFTERWARDS.
Do not reason about what was likely; if you do not specifically remember, say recall = "none".

Replace the ENTIRE content of the output file named in your instructions with one JSON object:
{{"answers": [{{"id": "<matter id>", "recall": "none|vague|specific",
  "believed_outcome": "adopted|not_adopted|withdrawn|unknown",
  "believed_date": "YYYY-MM or null (month the decisive adoption/withdrawal happened)",
  "confidence": 0.0, "what_you_remember": "<=25 words"}}]}}
"""


def make(run, size=40):
    threads = read_jsonl(os.path.join(DATA, "threads", "threads.jsonl"))
    inbox, outbox = os.path.join(FC_ROOT, run, "inbox"), os.path.join(FC_ROOT, run, "outbox")
    os.makedirs(inbox, exist_ok=True)
    os.makedirs(outbox, exist_ok=True)
    man = {"run": run, "batches": []}
    for i in range(0, len(threads), size):
        chunk = threads[i:i + size]
        bid = f"{run}_b{i // size + 1:03d}"
        ids = {t["thread_id"]: "M" + sha256_text("probe|" + t["thread_id"])[:8] for t in chunk}
        body = HEADER.format(n=len(chunk)) + "\n".join(
            f"- id {ids[t['thread_id']]} | {t['regulator']} ({t['jurisdiction']}) | initiated {t['anchor_date']} | {t['neutral_title']}"
            for t in chunk)
        for t in chunk:
            assert t["thread_id"] not in body
        pin, pout = os.path.join(inbox, bid + ".md"), os.path.join(outbox, bid + ".json")
        open(pin, "w").write(body)
        if not os.path.exists(pout):
            open(pout, "w").write(STUB)
        man["batches"].append({"batch_id": bid, "packet": pin, "output": pout, "ids": ids})
    os.makedirs(os.path.join(DATA, "forecasts", "runs"), exist_ok=True)
    json.dump(man, open(os.path.join(DATA, "forecasts", "runs", f"{run}.json"), "w"), indent=1)
    return man


def score(run):
    man = json.load(open(os.path.join(DATA, "forecasts", "runs", f"{run}.json")))
    om = {o["thread_id"]: o for o in read_jsonl(os.path.join(DATA, "outcomes", "outcomes.jsonl"))}
    out, pending = [], []
    for b in man["batches"]:
        txt = open(b["output"]).read()
        if "PENDING_FORECAST" in txt:
            pending.append(b["batch_id"])
            continue
        ans = {a["id"]: a for a in json.loads(txt).get("answers", [])}
        os.makedirs(os.path.join(DATA, "forecasts", "raw", run), exist_ok=True)
        open(os.path.join(DATA, "forecasts", "raw", run, b["batch_id"] + ".json"), "w").write(txt)
        for tid, mid in b["ids"].items():
            a = ans.get(mid, {})
            o = om.get(tid)
            if not o:
                continue
            act = o["decisive_action"]
            bel = a.get("believed_outcome", "unknown")
            outcome_ok = (bel == "adopted" and act) or (bel in ("not_adopted", "withdrawn") and not act)
            date_ok = None
            if act and a.get("believed_date") and len(str(a["believed_date"])) >= 7:
                try:
                    date_ok = abs(days_between(a["believed_date"][:7] + "-15", o["decisive_date"])) <= 92
                except Exception:
                    date_ok = False
            rec = a.get("recall", "none")
            conf = float(a.get("confidence", 0) or 0)
            out.append({"run": run, "thread_id": tid, "recall": rec, "believed_outcome": bel,
                        "believed_date": a.get("believed_date"), "confidence": conf,
                        "outcome_matches": bool(outcome_ok), "date_within_3m": date_ok,
                        "recalled_correctly": bool(rec in ("vague", "specific") and outcome_ok and conf >= 0.6),
                        "scored_at": now_iso()})
    path = os.path.join(DATA, "audits", "memorisation_probe.jsonl")
    done = {(r["run"], r["thread_id"]) for r in read_jsonl(path)}
    append_jsonl(path, [r for r in out if (r["run"], r["thread_id"]) not in done])
    return {"scored": len(out), "pending": pending,
            "recalled_correctly": sum(r["recalled_correctly"] for r in out),
            "claimed_recall": sum(r["recall"] != "none" for r in out)}


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd")
    ap.add_argument("run")
    ap.add_argument("--size", type=int, default=40)
    a = ap.parse_args()
    if a.cmd == "make":
        m = make(a.run, a.size)
        print(json.dumps({"batches": len(m["batches"])}))
    else:
        print(json.dumps(score(a.run), indent=1))
