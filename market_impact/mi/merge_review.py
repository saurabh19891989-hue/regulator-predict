"""Merge red-team review files (review/<ID>.json) into the Director override files.

Run: python3 -m market_impact.mi.merge_review
- edge_scale       → graph/edge_overrides.json ("scale", tagged by=<ID>)
- event_overrides  → graph/event_overrides.json ("events")
- event_drop       → graph/event_overrides.json (drop=true)
- recent_state_overrides → graph/recent_state_overrides.json ("overrides")
Idempotent: entries previously merged from a reviewer are replaced on re-run. Director-authored entries (no "by")
are kept and win over reviewer entries on the same key. review/rejected.json ({"<ID>": ["<key>", ...]}) lists items
the Director rejected; keys are "edge:src>dst@origin", "event:EV_X", "drop:EV_X", "state:NODE".
Conflicts (two reviewers on the same key) keep the first reviewer in PRIORITY order and are written to
review/merge_log.json.
"""
import ast
import glob
import json
import os
import re

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
R = lambda *p: os.path.join(HERE, *p)
PRIORITY = ["DIRECTOR_CE", "RT_BACKBONE", "RT_EVENTS", "RT_TOP_A", "RT_TOP_B", "RT_BOT_A", "RT_BOT_B", "RT_N50_A", "RT_N50_B"]


def load(p, default):
    return json.load(open(p)) if os.path.exists(p) else default


def norm_origin(o):
    if not o or o in ("null", "None"):
        return None
    o = os.path.basename(str(o))
    if not o.endswith(".json"):
        for d in ("events", "graph"):
            if os.path.exists(R(d, o + ".json")):
                return o + ".json"
    return o


def main():
    nodes = {n["id"] for n in json.load(open(R("graph", "nodes_seed.json")))}
    if os.path.exists(R("results", "nodes_all.csv")):
        import pandas as pd
        nodes |= set(pd.read_csv(R("results", "nodes_all.csv")).id)
    rejected = load(R("review", "rejected.json"), {})
    files = sorted(glob.glob(R("review", "*.json")), key=lambda p: (
        PRIORITY.index(os.path.basename(p)[:-5]) if os.path.basename(p)[:-5] in PRIORITY else 99, p))
    files = [p for p in files if os.path.basename(p) not in ("rejected.json", "merge_log.json")]
    ceo = load(R("graph", "company_event_overrides.json"), {"overrides": [], "add": []})
    ceo["overrides"] = [x for x in ceo.get("overrides", []) if not x.get("by")]
    ceo["add"] = [x for x in ceo.get("add", []) if not x.get("by")]
    seen_ce = {(x["ticker"], x["match"].lower()) for x in ceo["overrides"]}

    eo = load(R("graph", "edge_overrides.json"), {"scale": []})
    eo["scale"] = [x for x in eo["scale"] if not x.get("by")]
    director_keys = {(x["src"], x["dst"], norm_origin(x.get("origin"))) for x in eo["scale"]}
    ev = load(R("graph", "event_overrides.json"), {"events": {}})
    ev["events"] = {k: v for k, v in ev["events"].items() if not v.get("by")}
    rs = load(R("graph", "recent_state_overrides.json"), {"overrides": []})
    rs["overrides"] = [x for x in rs["overrides"] if not x.get("by")]
    log = {"applied": [], "conflicts": [], "rejected": [], "invalid": []}
    seen_edge, seen_ev, seen_state = {}, {}, {x["node"]: "director" for x in rs["overrides"]}

    for p in files:
        rid = os.path.basename(p)[:-5]
        try:
            o = json.load(open(p))
        except json.JSONDecodeError as e:
            log["invalid"].append(f"{rid}: {e}")
            continue
        rej = set(rejected.get(rid, []))
        for x in o.get("edge_scale", []) or []:
            k = (x["src"], x["dst"], norm_origin(x.get("origin")))
            key = f"edge:{k[0]}>{k[1]}@{k[2]}"
            if key in rej:
                log["rejected"].append(f"{rid} {key}")
                continue
            if k in director_keys or k in seen_edge:
                log["conflicts"].append(f"{key}: {rid} factor {x.get('factor')} vs {seen_edge.get(k, 'director')}")
                continue
            seen_edge[k] = f"{rid} factor {x.get('factor')}"
            eo["scale"].append({"src": k[0], "dst": k[1], "origin": k[2], "factor": float(x["factor"]),
                                "reason": f"[{rid}] {x.get('reason', '')}", "by": rid})
            log["applied"].append(f"{rid} {key} ×{x['factor']}")
        for eid, ov in (o.get("event_overrides") or {}).items():
            key = f"event:{eid}"
            if key in rej:
                log["rejected"].append(f"{rid} {key}")
                continue
            if eid in ev["events"] and ev["events"][eid].get("by") != rid:
                log["conflicts"].append(f"{key}: {rid} vs {ev['events'][eid].get('by', 'director')}")
                continue
            ov = {k: v for k, v in ov.items() if k in ("prob_by_3m", "prob_by_12m", "status", "date", "entry_shocks", "reason")}
            if "entry_shocks" in ov:
                bad = [s.get("node") for s in ov["entry_shocks"] if s.get("node") not in nodes]
                if bad:
                    log["invalid"].append(f"{rid} {key}: unknown nodes {bad}")
                    ov.pop("entry_shocks")
            p3, p12 = ov.get("prob_by_3m"), ov.get("prob_by_12m")
            if p3 is not None and p12 is not None and float(p3) > float(p12):
                ov["prob_by_12m"] = p3
            ev["events"][eid] = {**ov, "by": rid}
            log["applied"].append(f"{rid} {key}")
        # company-event fixes: a "company_event_overrides" block, or exact JSON objects embedded in findings text
        ce_block = o.get("company_event_overrides") or {}
        ce_list = list(ce_block.get("overrides", [])) if isinstance(ce_block, dict) else []
        for f in o.get("findings", []) or []:
            blob = " ".join(str(v) for v in f.values())
            for m in re.finditer(r"""\{[^{}]*['"]ticker['"]\s*:\s*['"][^'"]+['"][^{}]*['"]match['"][^{}]*\}""", blob):
                try:
                    ce_list.append(json.loads(m.group(0)))
                except json.JSONDecodeError:
                    try:
                        ce_list.append(ast.literal_eval(m.group(0)))     # findings holding dicts stringify with ' quotes
                    except (ValueError, SyntaxError):
                        log["invalid"].append(f"{rid}: unparsable company-event fix {m.group(0)[:80]}")
        for x in ce_list:
            k = (x.get("ticker"), str(x.get("match", "")).lower())
            key = f"ce:{k[0]}:{k[1]}"
            if key in rej:
                log["rejected"].append(f"{rid} {key}")
                continue
            if k in seen_ce:
                log["conflicts"].append(f"{key}: {rid}")
                continue
            seen_ce.add(k)
            ceo["overrides"].append({**x, "reason": f"[{rid}] {x.get('reason', '')}", "by": rid})
            log["applied"].append(f"{rid} {key}")
        for x in (ce_block.get("add", []) if isinstance(ce_block, dict) else []):
            ceo["add"].append({**x, "reason": f"[{rid}] {x.get('reason', '')}", "by": rid})
            log["applied"].append(f"{rid} ce-add:{x.get('ticker')}")
        for eid, reason in (o.get("event_drop") or {}).items():
            key = f"drop:{eid}"
            if key in rej:
                log["rejected"].append(f"{rid} {key}")
                continue
            ev["events"][eid] = {"drop": True, "reason": f"[{rid}] {reason}", "by": rid}
            log["applied"].append(f"{rid} {key}")
        for x in o.get("recent_state_overrides", []) or []:
            key = f"state:{x['node']}"
            if key in rej:
                log["rejected"].append(f"{rid} {key}")
                continue
            if x["node"] in seen_state:
                log["conflicts"].append(f"{key}: {rid} vs {seen_state[x['node']]}")
                continue
            seen_state[x["node"]] = rid
            rs["overrides"].append({"node": x["node"], "state_ssu": float(x["state_ssu"]), "reason": f"[{rid}] {x.get('reason', '')}", "by": rid})
            log["applied"].append(f"{rid} {key}")

    json.dump(eo, open(R("graph", "edge_overrides.json"), "w"), indent=1)
    json.dump(ev, open(R("graph", "event_overrides.json"), "w"), indent=1)
    json.dump(rs, open(R("graph", "recent_state_overrides.json"), "w"), indent=1)
    json.dump(ceo, open(R("graph", "company_event_overrides.json"), "w"), indent=1)
    json.dump(log, open(R("review", "merge_log.json"), "w"), indent=1)
    print({k: len(v) for k, v in log.items()})


if __name__ == "__main__":
    main()
