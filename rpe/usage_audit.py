"""Model-routing and spend audit from Claude Code transcripts (reads only model/usage metadata, never content).

Usage: python3 -m rpe.usage_audit  → prints table, writes data/derived/usage_audit.json
"""
import glob
import json
import os
from collections import Counter, defaultdict

PROJ = "/root/.claude/projects/-home-user-regulator-predict"
SESSION = "91e5b9f5-d683-5b72-a27c-87c3694866b1"
# USD per million tokens: input, output, cache read, cache write 5m, cache write 1h (list prices, claude-api skill 2026-06-24)
PRICE = {
    "claude-opus-5-5": (4.0, 20.0, 0.20, 5.0, 8.0),
    "claude-sonnet-5": (2.0, 10.0, 0.20, 2.5, 4.0),
    "claude-haiku-4-5": (1.0, 5.0, 0.10, 1.25, 2.0),
    "claude-fable-5-1": (10.0, 50.0, 0.25, 12.5, 20.0),
}
LABELS = {
    "a81466956d26a1bee": "isolation test (statusline-setup)", "aecfbb2638bc4f8cb": "executor us_fr",
    "aa30d335f9dafbe48": "executor us_reginfo", "a981b9e972df21229": "executor us_fda",
    "a45538d150ee4e5ea": "executor in_sebi_h", "abb27a8e1301fc4d0": "executor in_sebi_r",
    "a7dff2243867b2c72": "executor in_rbi", "a1c56e86be0401d5b": "executor in_irdai",
    "af45f231e75e57880": "executor in_trai", "a1b5332e0a174c297": "executor in_dgtr",
    "a11a70786e89a2e4d": "executor us_baserates", "afb186100ee9f0096": "forecaster SMOKE1_b001",
    "adf8a56925ee92911": "forecaster SMOKE1_b002", "a5501cd2bd7dae687": "forecaster SMOKE1_b003",
    "ae6163d8fc8d6791f": "forecaster SMOKE1_b004",
}
INTENDED = {"executor": "claude-sonnet-5", "forecaster": "claude-opus-5-5", "isolation": "claude-haiku-4-5",
            "director": "claude-opus-5-5"}


def price_key(model):
    for k in PRICE:
        if model and model.startswith(k):
            return k
    return None


def aggregate(path):
    per_req = {}
    efforts = Counter()
    with open(path) as f:
        for line in f:
            try:
                o = json.loads(line)
            except json.JSONDecodeError:
                continue
            if o.get("type") != "assistant":
                continue
            m = o.get("message") or {}
            u = m.get("usage") or {}
            rid = o.get("requestId") or m.get("id")
            if o.get("effort"):
                efforts[str(o.get("effort"))] += 1
            prev = per_req.get(rid)
            if prev is None or (u.get("output_tokens") or 0) >= (prev[1].get("output_tokens") or 0):
                per_req[rid] = (m.get("model"), u)
    tot = defaultdict(lambda: Counter())
    for model, u in per_req.values():
        c = tot[model]
        c["requests"] += 1
        c["input"] += u.get("input_tokens") or 0
        c["output"] += u.get("output_tokens") or 0
        c["cache_read"] += u.get("cache_read_input_tokens") or 0
        cc = u.get("cache_creation") or {}
        w5, w1 = cc.get("ephemeral_5m_input_tokens"), cc.get("ephemeral_1h_input_tokens")
        if w5 is None and w1 is None:
            w5 = u.get("cache_creation_input_tokens") or 0
        c["cache_write_5m"] += w5 or 0
        c["cache_write_1h"] += w1 or 0
    out = {}
    for model, c in tot.items():
        pk = price_key(model)
        cost = None
        if pk:
            pi, po, pr, p5, p1 = PRICE[pk]
            cost = (c["input"] * pi + c["output"] * po + c["cache_read"] * pr + c["cache_write_5m"] * p5 + c["cache_write_1h"] * p1) / 1e6
        out[model] = {**c, "usd": round(cost, 4) if cost is not None else None}
    return out, dict(efforts)


def main():
    rows = []
    sub = sorted(glob.glob(os.path.join(PROJ, SESSION, "subagents", "agent-*.jsonl")))
    for p in sub:
        aid = os.path.basename(p)[len("agent-"):-len(".jsonl")]
        agg, eff = aggregate(p)
        rows.append({"agent": aid, "task": LABELS.get(aid, "?"), "models": agg, "effort": eff})
    main_path = os.path.join(PROJ, SESSION + ".jsonl")
    if os.path.exists(main_path):
        agg, eff = aggregate(main_path)
        rows.append({"agent": "main", "task": "director (this session)", "models": agg, "effort": eff})
    by_model = defaultdict(lambda: Counter())
    total = 0.0
    for r in rows:
        for m, c in r["models"].items():
            for k in ("requests", "input", "output", "cache_read", "cache_write_5m", "cache_write_1h"):
                by_model[m][k] += c[k]
            by_model[m]["usd"] += c["usd"] or 0
            total += c["usd"] or 0
        role = r["task"].split()[0]
        exp = INTENDED.get(role)
        r["intended_model"] = exp
        r["routing_ok"] = (set(r["models"]) == {exp}) if exp else None
    res = {"rows": rows, "by_model": {m: dict(c) for m, c in by_model.items()}, "total_usd_list_price": round(total, 2)}
    json.dump(res, open("/home/user/regulator-predict/data/derived/usage_audit.json", "w"), indent=1)
    print(f"{'task':38s} {'model(s) actually used':28s} {'intended':18s} ok  req   input  cacheW   cacheR     out     USD  effort")
    for r in rows:
        for m, c in r["models"].items():
            print(f"{r['task'][:38]:38s} {str(m)[:28]:28s} {str(r['intended_model'])[:18]:18s} {'Y' if r['routing_ok'] else 'N'} {c['requests']:4d} {c['input']:7d} {c['cache_write_5m']+c['cache_write_1h']:7d} {c['cache_read']:8d} {c['output']:7d} {c['usd'] or 0:7.2f}  {r['effort']}")
    print("\nBY MODEL:")
    for m, c in res["by_model"].items():
        print(f"  {m:24s} requests={c['requests']:5d} input={c['input']:8d} cache_write={c['cache_write_5m']+c['cache_write_1h']:9d} cache_read={c['cache_read']:10d} output={c['output']:8d} USD={c['usd']:.2f}")
    print(f"\nTOTAL (list price, all transcripts in this session): ${res['total_usd_list_price']}")


if __name__ == "__main__":
    main()
