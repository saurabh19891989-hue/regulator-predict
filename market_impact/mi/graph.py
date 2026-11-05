"""Exposure Propagation Network: assemble, validate, propagate (1st–4th order), score, rank.

Run: python3 -m market_impact.mi.graph [--draws 400]
Inputs: graph/nodes_seed.json, graph/backbone_*.json, graph/node_aliases.json (optional), events/*.json,
        companies/*.json, results/empirical_sensitivities.csv, data/prices/close.csv
Outputs (results/): nodes_all.csv, edges_all.csv, edge_flags.csv, sensitivity_matrix.csv, sensitivity_by_order.csv,
        event_impacts.csv, company_paths.jsonl, driver_rank_by_company.csv, rankings.csv, assembly_report.json
"""
import argparse
import glob
import json
import math
import os
from collections import defaultdict

import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
R = lambda *p: os.path.join(HERE, *p)
DAMP = {1: 1.0, 2: 0.8, 3: 0.6, 4: 0.45}       # per-order uncertainty damping (PLAN.md)
MAX_DEPTH = 4
MIN_CONTRIB = 0.005                            # prune paths contributing < 0.005 % equity value per unit shock
CONF_W = {"high": 1.0, "medium": 0.6, "low": 0.3}
DRIVER = {"FACTOR", "POLICY", "COUNTRY", "THEME", "NEW"}
PRICED_SHARE_FWD = 0.5        # share of forward event expectations assumed already in prices
RECENT_CONVERGENCE = {"3m": 0.3, "12m": 0.5}   # share of the still-unpriced impact of occurred events expected to be priced
RESIDUAL_CAP = 10.0           # cap on |residual contribution| (% points)
IVOL_CAP = 60.0               # cap on 12m idiosyncratic vol used for noise (corporate-action price breaks inflate it)
# Unpriced part of an occurred-event impact: same sign as the model impact and never larger than it. A stock that moved
# further than the events explain is treated as having idiosyncratic news, not as a mean-reversion candidate.
RECENT_START = "2026-06-01"
OVERLAP_DAMP = 0.5            # indirect paths from X to c get half credit when c already has a direct edge from X
import re as _re
MARKET_WIDE = _re.compile(r"union budget|budget fy|\bmpc\b|rbi (policy|rate|monetary)|repo rate|gst council|state election|"
                          r"general election|fomc|fed (rate|meeting)|opec|monsoon", _re.I)


def load_json(p):
    try:
        return json.load(open(p))
    except Exception:
        return None


def assemble():
    nodes = {n["id"]: dict(n) for n in json.load(open(R("graph", "nodes_seed.json")))}
    aliases = load_json(R("graph", "node_aliases.json")) or {}
    A = lambda x: aliases.get(x, x)
    raw_edges, events, new_nodes, profiles = [], [], {}, {}

    def add_new(lst, who):
        for n in lst or []:
            i = A(n.get("id"))
            if i and i not in nodes and i not in new_nodes:
                new_nodes[i] = {"id": i, "type": "NEW", "name": n.get("name", i), "ssu": n.get("ssu", ""),
                                "proposed_type": n.get("type"), "proposed_by": who}

    for p in sorted(glob.glob(R("graph", "backbone_*.json"))):
        o = load_json(p) or {}
        add_new(o.get("new_nodes_proposed"), os.path.basename(p))
        for e in o.get("edges", []):
            raw_edges.append({**e, "src": A(e["src"]), "dst": A(e["dst"]), "origin": os.path.basename(p), "layer": "backbone"})
    de = load_json(R("graph", "director_edges.json")) or {}
    add_new(de.get("new_nodes_proposed"), "director")
    for e in de.get("edges", []):
        raw_edges.append({**e, "src": A(e["src"]), "dst": A(e["dst"]), "origin": "director", "layer": "director"})
    dedup = load_json(R("events", "dedup.json")) or {}
    drop_ev = set(dedup.get("drop", []))
    ev_over = (load_json(R("graph", "event_overrides.json")) or {}).get("events", {})
    drop_ev |= {k for k, v in ev_over.items() if v.get("drop")}
    for p in sorted(glob.glob(R("events", "*.json"))):
        if os.path.basename(p) == "dedup.json":
            continue
        o = load_json(p) or {}
        add_new(o.get("new_nodes_proposed"), os.path.basename(p))
        for e in o.get("edges", []) or []:
            raw_edges.append({**e, "src": A(e["src"]), "dst": A(e["dst"]), "origin": os.path.basename(p), "layer": "event_edges"})
        for ev in o.get("events", []):
            if ev.get("event_id") in drop_ev:
                continue
            ev = dict(ev)
            ov = ev_over.get(ev["event_id"], {})
            for k in ("prob_by_3m", "prob_by_12m", "status", "date"):
                if k in ov:
                    ev[k] = ov[k]
            if "entry_shocks" in ov:
                ev["entry_shocks"] = ov["entry_shocks"]
            if ov:
                ev["director_override"] = ov.get("reason", "")
            ev["theme_file"] = os.path.basename(p)
            ev["entry_shocks"] = [{**s, "node": A(s["node"])} for s in ev.get("entry_shocks", [])]
            events.append(ev)
    for p in sorted(glob.glob(R("companies", "*.json"))):
        o = load_json(p)
        if not o or "ticker" not in o:
            continue
        profiles[o["ticker"]] = o
        add_new(o.get("new_nodes_proposed"), o["ticker"])
        for e in o.get("exposures", []):
            raw_edges.append({**e, "src": A(e["src"]), "dst": o["ticker"], "origin": o["ticker"], "layer": "company"})
        for e in o.get("company_links", []) or []:
            raw_edges.append({**e, "src": A(e["src"]), "dst": A(e["dst"]), "origin": o["ticker"], "layer": "company_link"})
    nodes.update(new_nodes)
    for ov in (load_json(R("graph", "edge_overrides.json")) or {}).get("scale", []):
        for e in raw_edges:
            if e["src"] == A(ov["src"]) and e["dst"] == A(ov["dst"]) and (ov.get("origin") in (None, e["origin"])):
                for k in ("w", "w_low", "w_high"):
                    e[k] = float(e[k]) * float(ov["factor"])
                e["mechanism"] = f"[Director override ×{ov['factor']}: {ov['reason']}] " + str(e.get("mechanism", ""))
    # dedupe (src,dst): confidence-weighted mean, union range, provenance
    groups = defaultdict(list)
    for e in raw_edges:
        if e["src"] not in nodes or e["dst"] not in nodes or e["src"] == e["dst"]:
            continue
        if nodes[e["src"]]["type"] == "INDUSTRY" or nodes[e["dst"]]["type"] == "INDUSTRY":
            continue
        groups[(e["src"], e["dst"])].append(e)
    edges = []
    for (s, d), lst in groups.items():
        ws = np.array([CONF_W.get(e.get("confidence"), 0.3) for e in lst])
        w = float(np.dot(ws, [float(e["w"]) for e in lst]) / ws.sum())
        lo = min(float(min(e["w_low"], e["w_high"])) for e in lst)
        hi = max(float(max(e["w_low"], e["w_high"])) for e in lst)
        best = max(lst, key=lambda e: CONF_W.get(e.get("confidence"), 0.3))
        edges.append({"src": s, "dst": d, "w": w, "w_low": min(lo, w), "w_high": max(hi, w), "relation": best.get("relation"),
                      "lag": best.get("lag"), "confidence": best.get("confidence"), "mechanism": best.get("mechanism", "")[:400],
                      "layer": best["layer"], "n_sources": len(lst), "origins": ";".join(sorted({e["origin"] for e in lst}))})
    dropped = len(raw_edges) - sum(len(v) for v in groups.values())
    return nodes, edges, events, profiles, dropped


def empirical_flags(edges):
    p = R("results", "empirical_sensitivities.csv")
    if not os.path.exists(p):
        return []
    emp = pd.read_csv(p).set_index(["company", "factor"])
    flags = []
    for e in edges:
        k = (e["dst"], e["src"])
        if e["layer"] != "company" or k not in emp.index:
            continue
        r = emp.loc[k]
        el, t = float(r["elasticity_per_ssu"]), float(r["t_stat"])
        e["emp_elasticity"], e["emp_t"] = el, t
        if abs(t) >= 2.5 and np.sign(el) != np.sign(e["w"]) and abs(e["w"]) > 0.5:
            e["flag"] = "sign_conflict_with_empirical"
            flags.append({**{k2: e[k2] for k2 in ("src", "dst", "w", "relation")}, "emp_elasticity": el, "emp_t": t})
    return flags


class Network:
    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = edges
        self.out = defaultdict(list)
        for i, e in enumerate(edges):
            src_t = nodes[e["src"]]["type"]
            # company → company edges carry only idiosyncratic (company-specific) shocks; see paths_from
            if src_t == "COMPANY" and e["layer"] != "company_link":
                continue
            self.out[e["src"]].append(i)
        self.companies = [n for n, v in nodes.items() if v["type"] == "COMPANY"]
        self.direct_src = defaultdict(set)
        for e in edges:
            if e["layer"] in ("company", "director") and nodes[e["dst"]]["type"] == "COMPANY":
                self.direct_src[e["dst"]].add(e["src"])

    def paths_from(self, start, w_vec=None, clamped=frozenset()):
        """Enumerate simple paths from `start` (unit +1 shock). Yields (edge_idx_tuple, contribution, end_node).
        `clamped` drivers are observed: their actual move is already in the state vector, so paths never enter them."""
        W = w_vec if w_vec is not None else np.array([e["w"] for e in self.edges])
        stack = [(start, (), 1.0, frozenset([start]))]
        while stack:
            node, path, prod, seen = stack.pop()
            for ei in self.out.get(node, ()):
                d = self.edges[ei]["dst"]
                if d in seen or d in clamped:
                    continue
                k = len(path) + 1
                p2 = prod * W[ei]
                contrib = p2 * DAMP[k]
                if k >= 2 and start in self.direct_src.get(d, ()):
                    contrib *= OVERLAP_DAMP
                if self.nodes[d]["type"] == "COMPANY":
                    if abs(contrib) >= MIN_CONTRIB:
                        yield path + (ei,), contrib, d
                    # factor/driver-origin shocks stop at companies: consolidated profiles already embed subsidiary
                    # economics, so passing driver shocks through holding links would double count.
                    if self.nodes[start]["type"] != "COMPANY":
                        continue
                if k < MAX_DEPTH and abs(p2) * DAMP.get(k + 1, 0) >= MIN_CONTRIB * 0.1:
                    stack.append((d, path + (ei,), p2, seen | {d}))

    def unit_response(self, start, clamped=frozenset()):
        """Company response to +1 SSU at start: totals and by order, plus path list."""
        tot = defaultdict(float)
        by_order = defaultdict(lambda: defaultdict(float))
        paths = []
        for path, c, d in self.paths_from(start, clamped=clamped):
            tot[d] += c
            by_order[d][len(path)] += c
            paths.append((path, c, d))
        return tot, by_order, paths


def path_str(net, start, path):
    s = [start] + [net.edges[i]["dst"] for i in path]
    return " → ".join(s)


def run(draws=400):
    nodes, edges, events, profiles, dropped = assemble()
    groups = (load_json(R("events", "dedup.json")) or {}).get("exclusive_groups", [])
    for g in groups:
        for key in ("prob_by_3m", "prob_by_12m"):
            tot_p = sum(float(e.get(key, 0)) for e in events if e["event_id"] in g)
            if tot_p > 1:
                for e in events:
                    if e["event_id"] in g:
                        e[key] = float(e.get(key, 0)) / tot_p
    flags = empirical_flags(edges)
    net = Network(nodes, edges)
    drivers = [n for n, v in nodes.items() if v["type"] in DRIVER]
    # 1) driver → company sensitivity matrix (company → drivers view)
    sens_rows, order_rows = [], []
    unit_cache = {}
    for d in drivers:
        tot, by_order, paths = net.unit_response(d)
        unit_cache[d] = (tot, by_order, paths)
        for c, v in tot.items():
            sens_rows.append({"driver": d, "company": c, "per_ssu": v})
            o = by_order[c]
            order_rows.append({"driver": d, "company": c, **{f"order{k}": o.get(k, 0.0) for k in range(1, 5)}})
    pd.DataFrame(sens_rows).to_csv(R("results", "sensitivity_matrix.csv"), index=False)
    pd.DataFrame(order_rows).to_csv(R("results", "sensitivity_by_order.csv"), index=False)

    # 2) event impacts (conditional on event). Within an event, every node it explicitly shocks is clamped:
    #    the agent's shock on a consequence node (e.g. Brent) already includes the cause's effect (e.g. conflict).
    W_central = np.array([e["w"] for e in edges])
    ev_rows, comp_paths = [], defaultdict(list)
    ev_imp, ev_mc = {}, {}
    resp_cache = {}
    for ev in events:
        imp = defaultdict(float)
        imp_o = defaultdict(lambda: defaultdict(float))
        mc_rows = []
        entry = frozenset(sh["node"] for sh in ev.get("entry_shocks", []) if sh["node"] in nodes and nodes[sh["node"]]["type"] != "COMPANY")
        for sh in ev.get("entry_shocks", []):
            n, m = sh["node"], float(sh.get("ssu", 0))
            if n not in nodes:
                continue
            if nodes[n]["type"] == "COMPANY":           # company-specific event: entry is % equity value directly
                imp[n] += m
                imp_o[n][1] += m
                mc_rows.append(((), 1.0, m, n))
                for path, cval, c in net.paths_from(n):   # idiosyncratic spillover via holding/group/customer links
                    imp[c] += m * cval
                    imp_o[c][len(path) + 1] += m * cval
                    pw = float(np.prod(W_central[list(path)]))
                    mc_rows.append((path, cval / pw if pw else 0.0, m, c))
                continue
            key = (n, entry - {n})
            if key not in resp_cache:
                resp_cache[key] = net.unit_response(n, clamped=entry - {n})
            tot, by_order, paths = resp_cache[key]
            for c, v in tot.items():
                imp[c] += m * v
                for k, vv in by_order[c].items():
                    imp_o[c][k] += m * vv
            for path, cval, c in paths:
                pw = float(np.prod(W_central[list(path)]))
                mc_rows.append((path, cval / pw if pw else 0.0, m, c))
                comp_paths[c].append({"event": ev["event_id"], "path": ev["event_id"] + " ⇒ " + path_str(net, n, path),
                                      "order": len(path), "impact_if_event": m * cval,
                                      "expected_3m": m * cval * float(ev.get("prob_by_3m", 0)),
                                      "expected_12m": m * cval * float(ev.get("prob_by_12m", 0))})
        ev_imp[ev["event_id"]] = imp
        ev_mc[ev["event_id"]] = mc_rows
        for c, v in imp.items():
            ev_rows.append({"event": ev["event_id"], "status": ev.get("status"), "prob_3m": ev.get("prob_by_3m"),
                            "prob_12m": ev.get("prob_by_12m"), "company": c, "impact_if_event": v,
                            **{f"order{k}": imp_o[c].get(k, 0.0) for k in range(1, 5)}})
    evdf = pd.DataFrame(ev_rows)
    evdf.to_csv(R("results", "event_impacts.csv"), index=False)
    with open(R("results", "company_paths.jsonl"), "w") as f:
        for c, lst in comp_paths.items():
            lst = sorted(lst, key=lambda x: -abs(x["expected_12m"]))[:40]
            f.write(json.dumps({"company": c, "top_paths": lst}, ensure_ascii=False) + "\n")

    # 3) company-specific events from profiles (conditional impact midpoint × prob)
    cs = defaultdict(lambda: [0.0, 0.0])
    for t, o in profiles.items():
        for ce in o.get("company_events", []) or []:
            if MARKET_WIDE.search(str(ce.get("event", ""))):   # covered by the event catalogue → avoid double count
                continue
            try:
                mid = (float(ce.get("impact_pct_low", 0)) + float(ce.get("impact_pct_high", 0))) / 2
                p = float(ce.get("prob", 0))
            except (TypeError, ValueError):
                continue
            cs[t][1] += p * mid
            cs[t][0] += p * mid if str(ce.get("date", ""))[:7] <= "2027-02" else 0.0

    link_out = defaultdict(list)
    for e in edges:
        if e["layer"] == "company_link":
            link_out[e["src"]].append((e["dst"], e["w"]))
    for t in list(cs):
        for d2, w in link_out.get(t, []):
            cs[d2][0] += w * cs[t][0] * DAMP[2]
            cs[d2][1] += w * cs[t][1] * DAMP[2]

    # 4) expected relative returns
    comps = net.companies
    occurred = [e for e in events if e.get("status") == "occurred"]
    forward = [e for e in events if e.get("status") != "occurred"]
    realised, beta = realised_moves(comps)
    res = []
    state, state_src = recent_state(nodes, occurred)
    clamped = frozenset(state_src)     # every node with a specified recent change is clamped against the others
    rec_imp = defaultdict(float)
    rec_paths = defaultdict(list)
    for n, m in state.items():
        if abs(m) < 1e-9 or n not in nodes:
            continue
        tot, _, paths = net.unit_response(n, clamped=clamped - {n})
        for c, v in tot.items():
            rec_imp[c] += m * v
        for path, cval, c in paths:
            rec_paths[c].append({"driver": n, "state_ssu": m, "source": state_src[n], "path": path_str(net, n, path),
                                 "order": len(path), "impact": m * cval})
    with open(R("results", "recent_state_paths.jsonl"), "w") as f:
        for c, lst in rec_paths.items():
            f.write(json.dumps({"company": c, "top": sorted(lst, key=lambda x: -abs(x["impact"]))[:25]}) + "\n")
    pd.DataFrame([{"driver": n, "state_ssu": m, "source": state_src[n]} for n, m in state.items()]).to_csv(
        R("results", "recent_state_vector.csv"), index=False)
    # Beta adjustment: realised moves are market-adjusted with each stock's beta, so model impacts are made comparable
    # by removing beta x (universe-average impact). Rankings therefore measure exposure beyond what beta implies.
    f3_raw = {c: sum(float(e.get("prob_by_3m", 0)) * ev_imp[e["event_id"]].get(c, 0.0) for e in forward) for c in comps}
    f12_raw = {c: sum(float(e.get("prob_by_12m", 0)) * ev_imp[e["event_id"]].get(c, 0.0) for e in forward) for c in comps}
    m_rec, m3, m12 = (float(np.mean([d.get(c, 0.0) for c in comps])) for d in (rec_imp, f3_raw, f12_raw))
    for c in comps:
        b = beta.get(c, 1.0)
        rec_raw = rec_imp.get(c, 0.0)
        rec = rec_raw - b * m_rec
        f3, f12 = f3_raw[c] - b * m3, f12_raw[c] - b * m12
        rz = realised.get(c)
        resid = float(np.clip(rec - rz, min(0.0, rec), max(0.0, rec))) if rz is not None else 0.0
        rc3 = float(np.clip(RECENT_CONVERGENCE["3m"] * resid, -RESIDUAL_CAP, RESIDUAL_CAP))
        rc12 = float(np.clip(RECENT_CONVERGENCE["12m"] * resid, -RESIDUAL_CAP, RESIDUAL_CAP))
        res.append({"company": c, "beta": b, "recent_events_model_impact_raw": rec_raw, "forward_exposure_12m_raw": f12_raw[c],
                    "recent_events_model_impact": rec, "realised_mkt_adj_since_jun": rz,
                    "unpriced_recent_impact": resid, "residual_contribution_3m": rc3, "residual_contribution": rc12,
                    "forward_exposure_3m": f3, "forward_exposure_12m": f12,
                    "company_events_3m": cs[c][0], "company_events_12m": cs[c][1],
                    "raw_er_3m": rc3 + (1 - PRICED_SHARE_FWD) * (f3 + cs[c][0]),
                    "raw_er_12m": rc12 + (1 - PRICED_SHARE_FWD) * (f12 + cs[c][1])})
    rk = pd.DataFrame(res)
    for h in ("3m", "12m"):
        rk[f"exp_rel_return_{h}"] = rk[f"raw_er_{h}"] - rk[f"raw_er_{h}"].mean()   # relative to universe average
    # 5) Monte Carlo over edge-weight uncertainty and event occurrence → P10/P90 of 12m relative return
    base12 = dict(zip(rk.company, rk.residual_contribution + (1 - PRICED_SHARE_FWD) * rk.company_events_12m))
    ivol = idio_vol(net.companies)
    rk = rk.merge(monte_carlo(net, events, ev_mc, base12, draws, ivol, beta), on="company", how="left")
    rk["idio_vol_12m"] = rk.company.map(ivol)
    from scipy.stats import norm as _norm
    rk["prob_outperform_3m"] = [float(_norm.cdf(e / (v / 2))) if v and v == v else np.nan
                                for e, v in zip(rk.exp_rel_return_3m, rk.idio_vol_12m)]
    meta = {n: nodes[n] for n in comps}
    rk["name"] = rk.company.map(lambda c: meta[c]["name"])
    rk["tier"] = rk.company.map(lambda c: meta[c].get("tier"))
    rk["nse_industry"] = rk.company.map(lambda c: meta[c].get("nse_industry"))
    rk["profiled"] = rk.company.isin(profiles)
    rk["n_exposures"] = rk.company.map(lambda c: len(profiles.get(c, {}).get("exposures", [])))
    rk["profile_confidence"] = rk.company.map(lambda c: profiles.get(c, {}).get("confidence_overall"))
    rk = rk.sort_values("exp_rel_return_12m", ascending=False)
    rk["rank_12m"] = range(1, len(rk) + 1)
    rk["rank_3m"] = rk.exp_rel_return_3m.rank(ascending=False, method="first").astype(int)
    rk.to_csv(R("results", "rankings.csv"), index=False)

    # 6) top drivers per company (sensitivity × current/expected driver move)
    driver_rows = []
    smat = pd.DataFrame(sens_rows)
    for c, g in smat.groupby("company"):
        g = g.reindex(g.per_ssu.abs().sort_values(ascending=False).index).head(15)
        for _, r in g.iterrows():
            driver_rows.append({"company": c, "driver": r.driver, "driver_name": nodes[r.driver]["name"],
                                "pct_equity_per_ssu": r.per_ssu, "ssu": nodes[r.driver].get("ssu")})
    pd.DataFrame(driver_rows).to_csv(R("results", "driver_rank_by_company.csv"), index=False)

    pd.DataFrame([{k: v for k, v in n.items() if k in ("id", "type", "name", "ssu", "series", "tier", "nse_industry", "proposed_by", "proposed_type")}
                  for n in nodes.values()]).to_csv(R("results", "nodes_all.csv"), index=False)
    pd.DataFrame(edges).to_csv(R("results", "edges_all.csv"), index=False)
    pd.DataFrame(flags).to_csv(R("results", "edge_flags.csv"), index=False)
    rep = {"nodes": len(nodes), "new_nodes": sum(1 for n in nodes.values() if n["type"] == "NEW"),
           "edges": len(edges), "edges_by_layer": pd.Series([e["layer"] for e in edges]).value_counts().to_dict() if edges else {},
           "edges_dropped_unknown_or_industry": dropped, "events": len(events), "occurred_events": len(occurred),
           "profiles": len(profiles), "empirical_sign_conflicts": len(flags),
           "assumptions": {"damping": DAMP, "priced_share_forward": PRICED_SHARE_FWD,
                           "recent_convergence": RECENT_CONVERGENCE, "residual_cap": RESIDUAL_CAP, "max_depth": MAX_DEPTH,
                           "overlap_damp": OVERLAP_DAMP}}
    # overlap diagnostic: company has direct edges from A and B while a driver edge A→B exists (possible double count)
    direct = defaultdict(dict)
    for e in edges:
        if e["layer"] in ("company", "director") and nodes[e["dst"]]["type"] == "COMPANY":
            direct[e["dst"]][e["src"]] = e["w"]
    drv_edges = {(e["src"], e["dst"]): e["w"] for e in edges if e["layer"] in ("backbone", "event_edges") and abs(e["w"]) >= 0.3}
    ov_rows = []
    for c, srcs in direct.items():
        for a_ in srcs:
            for b_ in srcs:
                if a_ != b_ and (a_, b_) in drv_edges:
                    ov_rows.append({"company": c, "A": a_, "B": b_, "w_A_to_B": drv_edges[(a_, b_)], "w_A_direct": srcs[a_],
                                    "w_B_direct": srcs[b_], "indirect_via_B": drv_edges[(a_, b_)] * srcs[b_] * DAMP[2]})
    pd.DataFrame(ov_rows).to_csv(R("results", "overlap_flags.csv"), index=False)
    reach = {eid: sum(abs(v) for v in imp.values()) for eid, imp in ev_imp.items()}
    rep["overlap_flags"] = len(ov_rows)
    rep["events_zero_reach"] = sorted(e for e, v in reach.items() if v < 1e-6)
    targeted = {s["node"] for ev in events for s in ev.get("entry_shocks", [])}
    rep["dead_end_drivers"] = sorted(n for n in targeted if n in nodes and nodes[n]["type"] != "COMPANY" and not net.out.get(n))
    rep["recent_state_drivers"] = {"observed": int(sum(1 for v in state_src.values() if v == "observed")),
                                   "from_events": int(sum(1 for v in state_src.values() if v == "events"))}
    json.dump(rep, open(R("results", "assembly_report.json"), "w"), indent=1)
    return rep


def recent_state(nodes, occurred):
    """Driver state change since RECENT_START in SSU. Observable drivers: measured from prices; others: sum of
    deduplicated occurred-event shocks (agent estimates), clipped to ±3 SSU."""
    from .prices import SSU_SCALE
    df = pd.read_csv(R("data", "prices", "close.csv"), index_col=0, parse_dates=True)
    base = df[df.index <= RECENT_START].index.max()
    state, src = {}, {}
    stale = set()
    for f, (kind, size) in SSU_SCALE.items():
        if f not in df.columns:
            continue
        s = df[f].dropna()
        if len(s) < 30 or s.tail(30).nunique() <= 1:      # stale series (e.g. coal) → not observable
            stale.add(f)
            continue
        b, l = s[s.index <= base].iloc[-1], s.iloc[-1]
        if kind == "pct":
            v = (l / b - 1) * 100 / size
        elif kind == "bp":
            v = (l - b) * 100 / size
        else:
            v = (l - b) / size
        state[f], src[f] = float(v), "observed"
    agg = defaultdict(float)
    for ev in occurred:
        for sh in ev.get("entry_shocks", []):
            n = sh["node"]
            if n in src or n not in nodes or nodes[n]["type"] == "COMPANY":
                continue
            agg[n] += float(sh.get("ssu", 0))
    for n, v in agg.items():
        state[n], src[n] = float(np.clip(v, -3, 3)), "events"
    for ov in (load_json(R("graph", "recent_state_overrides.json")) or {}).get("overrides", []):
        state[ov["node"]], src[ov["node"]] = float(ov["state_ssu"]), "director_override"
    return state, src


def idio_vol(comps):
    """12-month idiosyncratic (market-beta-adjusted) volatility in % from the last 52 weekly returns."""
    df = pd.read_csv(R("data", "prices", "close.csv"), index_col=0, parse_dates=True)
    lr = np.log(df.resample("W-FRI").last()).diff()
    out = {}
    for c in comps:
        if c not in lr.columns:
            continue
        x = lr[[c, "MKT_NIFTY50"]].dropna().tail(52)
        if len(x) < 26:
            continue
        b = np.cov(x[c], x["MKT_NIFTY50"])[0, 1] / np.var(x["MKT_NIFTY50"])
        out[c] = float((x[c] - b * x["MKT_NIFTY50"]).std() * np.sqrt(52) * 100)
    return out


def realised_moves(comps):
    """Market-adjusted move since RECENT_START, using a Blume-shrunk 3-year weekly beta vs the Nifty 50.
    Returns (moves %, betas)."""
    p = R("data", "prices", "close.csv")
    df = pd.read_csv(p, index_col=0, parse_dates=True)
    m = df["MKT_NIFTY50"]
    w = df.resample("W-FRI").last()
    lr = np.log(w).diff()
    out, betas = {}, {}
    base = df[df.index <= RECENT_START].index.max()
    for c in comps:
        if c not in df.columns:
            continue
        x = lr[[c, "MKT_NIFTY50"]].dropna().tail(156)
        raw = np.cov(x[c], x["MKT_NIFTY50"])[0, 1] / np.var(x["MKT_NIFTY50"]) if len(x) > 30 else 1.0
        betas[c] = float(np.clip(0.67 * raw + 0.33, 0.3, 2.0))
        if base not in df.index or pd.isna(df.loc[base, c]):
            continue
        rc = df[c].dropna().iloc[-1] / df.loc[base, c] - 1
        rm = m.dropna().iloc[-1] / m.loc[base] - 1
        out[c] = float((rc - betas[c] * rm) * 100)
    return out, betas


def monte_carlo(net, events, ev_mc, base12, draws, ivol=None, beta=None):
    """Forward events only: sample occurrence (12m, exclusive groups respected) and edge weights (Beta(2,2) in
    [low, high]); add the deterministic base (unrealised residual + company events); demean per draw.
    mc_p*: uncertainty of the model's expectation. ret_p* and mc_prob_outperform additionally add idiosyncratic
    noise (trailing 52-week market-adjusted volatility), i.e. the spread of plausible 12-month relative returns."""
    if draws <= 0 or not events:
        return pd.DataFrame({"company": net.companies})
    rng = np.random.default_rng(20261105)
    E = net.edges
    lo = np.array([e["w_low"] for e in E]); hi = np.array([e["w_high"] for e in E])
    comps = net.companies
    cidx = {c: i for i, c in enumerate(comps)}
    base = np.array([base12.get(c, 0.0) for c in comps])
    ev_paths = []
    for ev in events:
        if ev.get("status") == "occurred":
            continue
        rows = [r for r in ev_mc.get(ev["event_id"], []) if r[3] in cidx]
        if rows:
            L = len(E)
            P = np.full((len(rows), MAX_DEPTH), L, dtype=np.int64)
            for i, (pth, _, _, _) in enumerate(rows):
                P[i, :len(pth)] = pth
            ev_paths.append((ev, P, np.array([r[1] for r in rows]), np.array([r[2] for r in rows]), np.array([cidx[r[3]] for r in rows])))
    groups = (load_json(R("events", "dedup.json")) or {}).get("exclusive_groups", [])
    gid = {e: gi for gi, g in enumerate(groups) for e in g}
    p12 = {ev["event_id"]: float(ev.get("prob_by_12m", 0)) for ev in events}
    out = np.zeros((draws, len(comps)))
    outn = np.zeros((draws, len(comps)))
    iv = np.array([(ivol or {}).get(c, np.nan) for c in comps])
    iv = np.where(np.isnan(iv), np.nanmedian(iv) if np.isfinite(iv).any() else 30.0, iv)
    iv = np.minimum(iv, IVOL_CAP)
    bv = np.array([(beta or {}).get(c, 1.0) for c in comps])
    for k in range(draws):
        Wd = np.append(lo + (hi - lo) * rng.beta(2, 2, size=len(E)), 1.0)
        chosen = {}
        for gi, g in enumerate(groups):            # at most one outcome per exclusive group
            ps = np.array([p12.get(e, 0.0) for e in g])
            if ps.sum() > 1:
                ps = ps / ps.sum()
            u, acc = rng.random(), 0.0
            chosen[gi] = None
            for e, pe in zip(g, ps):
                acc += pe
                if u < acc:
                    chosen[gi] = e
                    break
        tot = np.zeros(len(comps))
        for ev, P, dmp, mult, ci in ev_paths:
            eid = ev["event_id"]
            if eid in gid:
                if chosen.get(gid[eid]) != eid:
                    continue
            elif rng.random() > p12[eid]:
                continue
            vals = Wd[P].prod(axis=1) * dmp * mult * (1 - PRICED_SHARE_FWD)
            np.add.at(tot, ci, vals)
        tot = tot - bv * tot.mean() + base
        out[k] = tot - tot.mean()
        tn = tot + rng.normal(0.0, iv)
        outn[k] = tn - tn.mean()
    return pd.DataFrame({"company": comps, "mc_p10_12m": np.percentile(out, 10, axis=0),
                         "mc_p50_12m": np.percentile(out, 50, axis=0), "mc_p90_12m": np.percentile(out, 90, axis=0),
                         "ret_p10_12m": np.percentile(outn, 10, axis=0), "ret_p90_12m": np.percentile(outn, 90, axis=0),
                         "mc_prob_outperform": (outn > 0).mean(axis=0)})


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--draws", type=int, default=400)
    a = ap.parse_args()
    print(json.dumps(run(a.draws), indent=1))
