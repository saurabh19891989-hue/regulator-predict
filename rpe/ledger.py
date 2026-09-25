"""Append-only, hash-chained forecast ledger.

Ingests forecaster outbox files for a run, validates + coherence-checks each forecast, and appends immutable
records to data/forecasts/ledger.jsonl. A (run, snapshot_id) pair can be ingested once; nothing is ever rewritten.
Raw outbox files are copied verbatim to data/forecasts/raw/<run>/ for audit.

Usage:
  python3 -m rpe.ledger ingest <run> --model opus-5.5
  python3 -m rpe.ledger verify
  python3 -m rpe.ledger status <run>
"""
import argparse
import json
import os
import shutil

import jsonschema

from .common import DATA, append_jsonl, load_schema, now_iso, read_jsonl, stable_hash

LEDGER = os.path.join(DATA, "forecasts", "ledger.jsonl")
H = ["7d", "30d", "60d", "90d", "180d"]
CONTENT = ["as_proposed", "softened", "tightened", "mixed", "different_mechanism"]
NEXT = ["final_action", "revised_or_further_consultation", "formal_withdrawal", "no_further_official_step"]


def _clip(x):
    try:
        x = float(x)
    except (TypeError, ValueError):
        return None
    return min(1.0, max(0.0, x))


def _norm(dct, keys, repairs, name):
    vals = {k: _clip(dct.get(k, 0.0)) or 0.0 for k in keys}
    s = sum(vals.values())
    if s <= 0:
        repairs.append(f"{name}: all zero → uniform")
        return {k: 1.0 / len(keys) for k in keys}
    if abs(s - 1) > 0.02:
        repairs.append(f"{name}: sum {s:.3f} normalised")
    return {k: v / s for k, v in vals.items()}


def canonicalise(raw):
    """Map compact forecaster output → canonical forecast schema, recording every repair."""
    rep = []
    p = raw.get("p") or {}
    t, prev = {}, 0.0
    for h in H:
        v = _clip(p.get(h))
        if v is None:
            raise ValueError(f"missing/invalid p.{h}")
        if v < prev - 1e-9:
            rep.append(f"timing non-monotone at {h}: {v:.3f} < {prev:.3f} → raised")
            v = prev
        t[h] = v
        prev = v
    scen = []
    for s in (raw.get("scenarios") or [])[:4]:
        scen.append({"scenario": str(s.get("s", ""))[:200], "probability": _clip(s.get("p")) or 0.0,
                     "mechanism": str(s.get("mech", ""))[:400], "parameter_ranges": s.get("params") or {},
                     "supporting_evidence_ids": s.get("ev") or [], "contrary_evidence_ids": s.get("contra") or []})
    tot = sum(s["probability"] for s in scen)
    if tot > 1.0001:
        rep.append(f"scenario probs sum {tot:.3f} → scaled")
        for s in scen:
            s["probability"] /= tot
    f = {
        "snapshot_id": raw["id"],
        "action_probability_180d": t["180d"],
        "timing": t,
        "next_step_probabilities": _norm(raw.get("next") or {}, NEXT, rep, "next"),
        "delay_or_no_action_probability": 1.0 - t["180d"],
        "content_direction_probs": _norm(raw.get("content") or {}, CONTENT, rep, "content"),
        "policy_scenarios": scen,
        "confidence_notes": str(raw.get("notes", ""))[:600],
        "missing_information": list(raw.get("missing") or [])[:5],
        "recognised_outcome": bool(raw.get("recognised_outcome", False)),
        "insufficient_evidence": bool(raw.get("insufficient_evidence", False)),
    }
    jsonschema.validate(f, load_schema("forecast"))
    return f, rep


def _last_hash():
    rows = read_jsonl(LEDGER)
    return rows[-1]["record_hash"] if rows else "GENESIS"


def ingest(run, model, agent_type="statusline-setup[Read,Edit] (isolated)"):
    man = json.load(open(os.path.join(DATA, "forecasts", "runs", f"{run}.json")))
    if man.get("invalidated"):
        raise ValueError(f"run {run} was invalidated: {man.get('invalid_reason', 'no reason recorded')}")
    done = {(r["run"], r["snapshot_id"]) for r in read_jsonl(LEDGER)}
    prev = _last_hash()
    new, problems, pending = [], [], []
    rawdir = os.path.join(DATA, "forecasts", "raw", run)
    os.makedirs(rawdir, exist_ok=True)
    for b in man["batches"]:
        if not os.path.exists(b["output"]):
            pending.append(b["batch_id"])
            continue
        txt = open(b["output"]).read().strip()
        if "PENDING_FORECAST" in txt:
            pending.append(b["batch_id"])
            continue
        try:
            obj = json.loads(txt)
        except json.JSONDecodeError as e:
            problems.append(f"{b['batch_id']}: bad JSON ({e})")
            continue
        shutil.copyfile(b["output"], os.path.join(rawdir, b["batch_id"] + ".json"))
        got = {}
        for raw in obj.get("forecasts", []):
            got[raw.get("id")] = raw
        for sid in b["snapshot_ids"]:
            if (run, sid) in done:
                continue
            raw = got.get(sid)
            if raw is None:
                problems.append(f"{b['batch_id']}: missing forecast for {sid}")
                continue
            try:
                f, rep = canonicalise(raw)
            except Exception as e:
                problems.append(f"{b['batch_id']}: {sid} invalid ({e})")
                continue
            rec = {"run": run, "batch_id": b["batch_id"], "model": model, "agent_type": agent_type,
                   "snapshot_id": sid, "alias_of": None, "packet_sha256": b["packet_sha256"],
                   "ingested_at": now_iso(), "forecast": f, "coherence_repairs": rep, "prev_hash": prev}
            rec["record_hash"] = stable_hash(rec)
            prev = rec["record_hash"]
            new.append(rec)
            done.add((run, sid))
            for alias, target in man.get("aliases", {}).items():
                if target == sid and (run, alias) not in done:
                    a = dict(rec, snapshot_id=alias, alias_of=sid, prev_hash=prev)
                    a.pop("record_hash")
                    a["forecast"] = dict(f, snapshot_id=alias)
                    a["record_hash"] = stable_hash(a)
                    prev = a["record_hash"]
                    new.append(a)
                    done.add((run, alias))
        extra = set(got) - set(b["snapshot_ids"])
        if extra:
            problems.append(f"{b['batch_id']}: unexpected ids {sorted(extra)[:5]}")
    append_jsonl(LEDGER, new)
    return {"run": run, "ingested": len(new), "pending_batches": pending, "problems": problems}


def verify():
    prev = "GENESIS"
    rows = read_jsonl(LEDGER)
    for i, r in enumerate(rows):
        h = r["record_hash"]
        body = dict(r)
        body.pop("record_hash")
        if body["prev_hash"] != prev or stable_hash(body) != h:
            return {"ok": False, "broken_at": i, "records": len(rows)}
        prev = h
    return {"ok": True, "records": len(rows)}


def status(run):
    man = json.load(open(os.path.join(DATA, "forecasts", "runs", f"{run}.json")))
    done = {r["snapshot_id"] for r in read_jsonl(LEDGER) if r["run"] == run}
    out = []
    for b in man["batches"]:
        n = sum(1 for s in b["snapshot_ids"] if s in done)
        out.append((b["batch_id"], n, len(b["snapshot_ids"])))
    return out


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd")
    ap.add_argument("run", nargs="?")
    ap.add_argument("--model", default="unknown")
    a = ap.parse_args()
    if a.cmd == "ingest":
        print(json.dumps(ingest(a.run, a.model), indent=1))
    elif a.cmd == "verify":
        print(json.dumps(verify()))
    elif a.cmd == "status":
        for row in status(a.run):
            print(*row)
