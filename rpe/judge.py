"""Blinded content judge: scenario mechanism accuracy + parameter-range coverage (positives only).

For each selected (positive thread, forecast) the judge sees ONLY: the matter title, the forecaster's scenarios, and
the actual outcome summary/parameters. It never sees model, arm, cutoff or stratum. A naive baseline item
("adopted exactly as proposed", proposed parameter values as point predictions) is mixed in blind for every thread.

Usage:
  python3 -m rpe.judge make <run> --forecast-runs R1 --offsets T-90,T-30 --size 30
  python3 -m rpe.judge score <run>   → data/audits/content_judgements.jsonl
"""
import argparse
import json
import os
import random

from .common import DATA, append_jsonl, now_iso, read_jsonl, sha256_text
from .packets import FC_ROOT, STUB

HEADER = """# BLIND CONTENT-MATCH JUDGING (research evaluation task)
Each item shows a regulatory matter, a set of PREDICTED policy scenarios (with probabilities, mechanisms and
predicted parameter ranges), and what the regulator ACTUALLY adopted. Judge strictly and consistently.
For each item output:
- "top1": does the highest-probability predicted scenario match the ACTUAL adopted mechanism in substance?
  "match" | "partial" (right direction/main mechanism but a material element wrong or missing) | "no_match"
- "any": best judgement over ALL predicted scenarios (match | partial | no_match)
- "params": for each predicted parameter that can be compared with an actual adopted value:
  {{"name": "...", "covered": true|false}} (true iff the actual value lies within the predicted range/point).
  Omit parameters that cannot be compared.
Replace the ENTIRE content of the output file named in your instructions with:
{{"judgements": [{{"id": "<item id>", "top1": "...", "any": "...", "params": [], "note": "<=20 words"}}]}}
"""


def make(run, forecast_runs, offsets, size=30, designs=("T", "K"), seed=7):
    idx = {r["snapshot_id"]: r for r in read_jsonl(os.path.join(DATA, "snapshots", "index.jsonl"))}
    om = {o["thread_id"]: o for o in read_jsonl(os.path.join(DATA, "outcomes", "outcomes.jsonl"))}
    th = {t["thread_id"]: t for t in read_jsonl(os.path.join(DATA, "threads", "threads.jsonl"))}
    led = [r for r in read_jsonl(os.path.join(DATA, "forecasts", "ledger.jsonl")) if r["run"] in forecast_runs and r["alias_of"] is None]
    items, naive_done = [], set()
    for r in led:
        s = idx.get(r["snapshot_id"])
        if not s or s["design"] not in designs or (offsets and s["offset"] not in offsets):
            continue
        o = om[s["thread_id"]]
        if not o["decisive_action"] or not r["forecast"]["policy_scenarios"]:
            continue
        actual = {"summary": o.get("content_summary", ""), "parameters": o.get("key_parameters", [])}
        items.append({"kind": "forecast", "snapshot_id": s["snapshot_id"], "run": r["run"], "thread_id": s["thread_id"],
                      "scenarios": r["forecast"]["policy_scenarios"], "actual": actual})
        if s["thread_id"] not in naive_done:
            naive_done.add(s["thread_id"])
            props = {p.get("name", "param"): p.get("proposed") for p in (o.get("key_parameters") or []) if p.get("proposed")}
            items.append({"kind": "naive_as_proposed", "snapshot_id": None, "run": "NAIVE", "thread_id": s["thread_id"],
                          "scenarios": [{"scenario": "Adopted exactly as proposed", "probability": 1.0,
                                         "mechanism": "The proposal as published is adopted without material change",
                                         "parameter_ranges": props}], "actual": actual})
    random.Random(seed).shuffle(items)
    inbox, outbox = os.path.join(FC_ROOT, run, "inbox"), os.path.join(FC_ROOT, run, "outbox")
    os.makedirs(inbox, exist_ok=True)
    os.makedirs(outbox, exist_ok=True)
    man = {"run": run, "batches": []}
    for i in range(0, len(items), size):
        chunk = items[i:i + size]
        bid = f"{run}_b{i // size + 1:03d}"
        lines = [HEADER]
        keymap = {}
        for j, it in enumerate(chunk):
            iid = "J" + sha256_text(f"{run}|{bid}|{j}")[:8]
            keymap[iid] = {k: it[k] for k in ("kind", "snapshot_id", "run", "thread_id")}
            sc = "\n".join(f"   - p={x['probability']:.2f} | {x['scenario']} | mechanism: {x['mechanism']} | params: {json.dumps(x.get('parameter_ranges') or {})}"
                           for x in it["scenarios"])
            lines.append(f"\n## ITEM {iid}\nMatter: {th[it['thread_id']]['neutral_title']}\nPREDICTED scenarios:\n{sc}\n"
                         f"ACTUAL adopted: {it['actual']['summary'][:1500]}\nACTUAL parameters: {json.dumps(it['actual']['parameters'])[:1200]}")
        body = "\n".join(lines)
        pin, pout = os.path.join(inbox, bid + ".md"), os.path.join(outbox, bid + ".json")
        open(pin, "w").write(body)
        if not os.path.exists(pout):
            open(pout, "w").write(STUB)
        man["batches"].append({"batch_id": bid, "packet": pin, "output": pout, "items": keymap})
    json.dump(man, open(os.path.join(DATA, "forecasts", "runs", f"{run}.json"), "w"), indent=1)
    return man


def score(run):
    man = json.load(open(os.path.join(DATA, "forecasts", "runs", f"{run}.json")))
    out, pending = [], []
    for b in man["batches"]:
        txt = open(b["output"]).read()
        if "PENDING_FORECAST" in txt:
            pending.append(b["batch_id"])
            continue
        js = {x["id"]: x for x in json.loads(txt).get("judgements", [])}
        for iid, meta in b["items"].items():
            j = js.get(iid)
            if not j:
                continue
            ps = j.get("params") or []
            out.append({**meta, "judge_run": run, "top1": j.get("top1"), "any": j.get("any"),
                        "params_compared": len(ps), "params_covered": sum(1 for p in ps if p.get("covered")),
                        "note": j.get("note", ""), "scored_at": now_iso()})
    path = os.path.join(DATA, "audits", "content_judgements.jsonl")
    append_jsonl(path, out)
    return {"scored": len(out), "pending": pending}


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd")
    ap.add_argument("run")
    ap.add_argument("--forecast-runs", default="")
    ap.add_argument("--offsets", default="")
    ap.add_argument("--size", type=int, default=30)
    a = ap.parse_args()
    if a.cmd == "make":
        m = make(a.run, a.forecast_runs.split(","), [x for x in a.offsets.split(",") if x], a.size)
        print(json.dumps({"batches": len(m["batches"]), "items": sum(len(b["items"]) for b in m["batches"])}))
    else:
        print(json.dumps(score(a.run), indent=1))
