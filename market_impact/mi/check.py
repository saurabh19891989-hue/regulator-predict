"""Validate agent output files against docs/AGENT_SPEC.md.

Usage: python3 -m market_impact.mi.check <file> [<file> ...]
Handles companies/<T>.json, events/<THEME>.json, graph/backbone_<part>.json. Exit 1 on any error.
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NODES = {n["id"]: n for n in json.load(open(os.path.join(HERE, "graph", "nodes_seed.json")))}
DRIVER_TYPES = {"FACTOR", "POLICY", "COUNTRY", "THEME"}
RELATIONS = {"input_cost", "output_price", "demand_driver", "competition", "funding_cost", "discount_rate",
             "fx_translation", "policy_effect", "macro_transmission", "geopolitical_exposure", "regulatory_risk",
             "holding_stake", "group_contagion", "dominant_customer", "substitution"}
COMPANY_LINK_REL = {"holding_stake", "group_contagion", "dominant_customer"}
LAGS = {"0-3m", "3-12m", ">12m"}
CONF = {"high", "medium", "low"}
DATE = re.compile(r"^\d{4}-\d{2}(-\d{2})?$")


def kind(nid, new_ids):
    if nid in NODES:
        return NODES[nid]["type"]
    if nid in new_ids or str(nid).startswith("NEW_"):
        return "NEW"
    if str(nid).startswith("EV_"):
        return "EVENT"
    return None


def check_edge(e, errs, where, new_ids):
    for k in ("src", "dst", "relation", "w", "w_low", "w_high", "lag", "mechanism", "confidence"):
        if k not in e:
            errs.append(f"{where}: edge missing {k}")
            return
    if e["relation"] not in RELATIONS:
        errs.append(f"{where}: bad relation {e['relation']}")
    if e["lag"] not in LAGS:
        errs.append(f"{where}: bad lag {e['lag']}")
    if e["confidence"] not in CONF:
        errs.append(f"{where}: bad confidence {e['confidence']}")
    try:
        w, lo, hi = float(e["w"]), float(e["w_low"]), float(e["w_high"])
        if not (min(lo, hi) - 1e-9 <= w <= max(lo, hi) + 1e-9):
            errs.append(f"{where}: w {w} outside [{lo},{hi}]")
        if abs(w) > 80:
            errs.append(f"{where}: |w| {w} implausibly large (>80% equity value or >80 SSU)")
    except (TypeError, ValueError):
        errs.append(f"{where}: non-numeric weight")
    for side in ("src", "dst"):
        k = kind(e[side], new_ids)
        if k is None:
            errs.append(f"{where}: unknown node {e[side]} (use vocabulary ids, a ticker, or propose NEW_*)")
        elif k == "INDUSTRY":
            errs.append(f"{where}: INDUSTRY node {e[side]} cannot be an edge endpoint")


def new_ids_of(obj):
    out = set()
    for n in obj.get("new_nodes_proposed", []) or []:
        if not str(n.get("id", "")).startswith("NEW_"):
            pass
        out.add(n.get("id"))
    return out


def check_company(obj, errs):
    t = obj.get("ticker")
    if t not in NODES or NODES[t]["type"] != "COMPANY":
        errs.append(f"unknown ticker {t}")
        return
    for k in ("name", "industry", "business_summary", "exposures", "supply_chain", "company_events", "current_state",
              "key_risks", "upside_triggers", "confidence_overall", "sources"):
        if k not in obj:
            errs.append(f"{t}: missing {k}")
    if obj.get("industry") not in NODES or NODES.get(obj.get("industry"), {}).get("type") != "INDUSTRY":
        errs.append(f"{t}: industry must be an INDUSTRY node id")
    nid = new_ids_of(obj)
    ex = obj.get("exposures", [])
    need = 8 if NODES[t].get("tier") == "NIFTY_NEXT_50" else 6
    if len(ex) < need:
        errs.append(f"{t}: only {len(ex)} exposures (need >= {need})")
    for i, e in enumerate(ex):
        check_edge(e, errs, f"{t} exposures[{i}]", nid)
        if e.get("dst") != t:
            errs.append(f"{t} exposures[{i}]: dst must be {t}")
        if kind(e.get("src"), nid) not in DRIVER_TYPES | {"NEW"}:
            errs.append(f"{t} exposures[{i}]: src {e.get('src')} must be a driver node (FACTOR/POLICY/COUNTRY/THEME/NEW_)")
    for i, e in enumerate(obj.get("company_links", []) or []):
        check_edge(e, errs, f"{t} company_links[{i}]", nid)
        if e.get("relation") not in COMPANY_LINK_REL:
            errs.append(f"{t} company_links[{i}]: relation must be one of {sorted(COMPANY_LINK_REL)}")
        if NODES.get(e.get("src"), {}).get("type") != "COMPANY" or NODES.get(e.get("dst"), {}).get("type") != "COMPANY":
            errs.append(f"{t} company_links[{i}]: both ends must be universe tickers")
    for i, ev in enumerate(obj.get("company_events", [])):
        if not (0 <= float(ev.get("prob", -1)) <= 1):
            errs.append(f"{t} company_events[{i}]: prob outside [0,1]")
    if not obj.get("sources"):
        errs.append(f"{t}: no sources")


def check_events(obj, errs):
    nid = new_ids_of(obj)
    ids = set()
    for i, ev in enumerate(obj.get("events", [])):
        w = f"events[{i}] {ev.get('event_id')}"
        for k in ("event_id", "title", "category", "status", "date", "prob_by_3m", "prob_by_12m", "description",
                  "entry_shocks", "chains", "sources", "confidence"):
            if k not in ev:
                errs.append(f"{w}: missing {k}")
        if not str(ev.get("event_id", "")).startswith("EV_"):
            errs.append(f"{w}: event_id must start with EV_")
        if ev.get("event_id") in ids:
            errs.append(f"{w}: duplicate id")
        ids.add(ev.get("event_id"))
        if ev.get("status") not in {"occurred", "scheduled", "anticipated", "risk_scenario"}:
            errs.append(f"{w}: bad status")
        p3, p12 = float(ev.get("prob_by_3m", -1)), float(ev.get("prob_by_12m", -1))
        if not (0 <= p3 <= p12 + 1e-9 <= 1 + 1e-9):
            errs.append(f"{w}: need 0 <= prob_by_3m <= prob_by_12m <= 1")
        if ev.get("status") == "occurred" and p3 < 0.999:
            errs.append(f"{w}: occurred events must have prob 1")
        if not DATE.match(str(ev.get("date", ""))):
            errs.append(f"{w}: bad date")
        if not ev.get("entry_shocks"):
            errs.append(f"{w}: no entry_shocks")
        for s in ev.get("entry_shocks", []):
            k = kind(s.get("node"), nid)
            if k not in DRIVER_TYPES | {"NEW", "COMPANY"}:
                errs.append(f"{w}: entry node {s.get('node')} must be a driver (or a company for company-specific events)")
            try:
                float(s["ssu"])
            except (KeyError, TypeError, ValueError):
                errs.append(f"{w}: entry shock needs numeric ssu")
        if not ev.get("sources"):
            errs.append(f"{w}: no sources")
    for i, e in enumerate(obj.get("edges", []) or []):
        check_edge(e, errs, f"edges[{i}]", nid)
        for side in ("src", "dst"):
            if kind(e.get(side), nid) not in DRIVER_TYPES | {"NEW"}:
                errs.append(f"edges[{i}]: {side} {e.get(side)} must be a driver node")


def check_backbone(obj, errs):
    nid = new_ids_of(obj)
    seen = set()
    for i, e in enumerate(obj.get("edges", [])):
        check_edge(e, errs, f"edges[{i}]", nid)
        for side in ("src", "dst"):
            if kind(e.get(side), nid) not in DRIVER_TYPES | {"NEW"}:
                errs.append(f"edges[{i}]: {side} {e.get(side)} must be a driver node")
        k = (e.get("src"), e.get("dst"))
        if k in seen:
            errs.append(f"edges[{i}]: duplicate {k}")
        seen.add(k)
        if e.get("src") == e.get("dst"):
            errs.append(f"edges[{i}]: self-loop")


def main(paths):
    bad = 0
    for p in paths:
        errs = []
        try:
            obj = json.load(open(p))
        except Exception as e:
            print(f"FAIL {p}: invalid JSON: {e}")
            bad += 1
            continue
        if "/companies/" in p or "ticker" in obj:
            check_company(obj, errs)
        elif "/events/" in p or "events" in obj:
            check_events(obj, errs)
        else:
            check_backbone(obj, errs)
        for m in errs[:60]:
            print("ERROR", p, "|", m)
        print(("OK  " if not errs else "FAIL") + f" {p} ({len(errs)} errors)")
        bad += bool(errs)
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main(sys.argv[1:])
