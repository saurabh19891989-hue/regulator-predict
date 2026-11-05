"""Compact datasets for the dashboard (results/dashboard/*.csv), built from the graph outputs.

Run after mi.graph and mi.reports: python3 -m market_impact.mi.dashboard_data
"""
import json
import os
from collections import defaultdict

import pandas as pd

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
R = lambda *p: os.path.join(HERE, *p)
OUT = R("results", "dashboard")


def main():
    os.makedirs(OUT, exist_ok=True)
    rk = pd.read_csv(R("results", "rankings.csv"))
    nodes = pd.read_csv(R("results", "nodes_all.csv")).set_index("id")
    paths = {}
    for line in open(R("results", "company_paths.jsonl")):
        o = json.loads(line)
        paths[o["company"]] = [p for p in o["top_paths"] if p.get("status") != "occurred"]
    top = defaultdict(lambda: ("", ""))
    for c, lst in paths.items():
        pos = [p for p in lst if p["expected_12m"] > 0]
        neg = [p for p in lst if p["expected_12m"] < 0]
        top[c] = (pos[0]["path"] if pos else "", neg[0]["path"] if neg else "")
    r = pd.DataFrame({
        "rank_12m": rk.rank_12m, "rank_3m": rk.rank_3m, "ticker": rk.company, "name": rk["name"],
        "tier": rk.tier.str.replace("NIFTY_NEXT_50", "Next 50").str.replace("NIFTY_50", "Nifty 50").str.replace("MIDCAP_100", "Midcap"),
        "industry": rk.nse_industry, "exp_3m": rk.exp_rel_return_3m.round(2), "exp_12m": rk.exp_rel_return_12m.round(2),
        "p_beat_3m": rk.prob_outperform_3m.round(3), "p_beat_12m": rk.mc_prob_outperform.round(3),
        "band_p10": rk.mc_p10_12m.round(2), "band_p90": rk.mc_p90_12m.round(2),
        "forward_events": (0.5 * rk.forward_exposure_12m).round(2),
        "company_events": (0.5 * rk.company_events_12m).round(2), "beta": rk.beta.round(2),
        "realised_since_jun": rk.realised_mkt_adj_since_jun.round(1), "graph_gap_since_jun": rk.graph_vs_market_gap.round(1),
        "upside_scenario_chain": rk.company.map(lambda c: top[c][0]), "downside_scenario_chain": rk.company.map(lambda c: top[c][1]),
        "confidence": rk.profile_confidence})
    r.sort_values("rank_12m").to_csv(os.path.join(OUT, "rankings.csv"), index=False)

    sec = rk.groupby("nse_industry").agg(stocks=("company", "size"), exp_3m=("exp_rel_return_3m", "mean"),
                                          exp_12m=("exp_rel_return_12m", "mean")).round(2).reset_index()
    best = rk.loc[rk.groupby("nse_industry").exp_rel_return_12m.idxmax(), ["nse_industry", "company"]].rename(columns={"company": "best"})
    worst = rk.loc[rk.groupby("nse_industry").exp_rel_return_12m.idxmin(), ["nse_industry", "company"]].rename(columns={"company": "worst"})
    sec = sec.merge(best, on="nse_industry").merge(worst, on="nse_industry").rename(columns={"nse_industry": "industry"})
    sec.sort_values("exp_12m", ascending=False).to_csv(os.path.join(OUT, "sectors.csv"), index=False)

    ev = pd.read_csv(R("results", "event_impacts.csv"))
    evs = {e["event_id"]: e for e in json.load(open(R("results", "events_effective.json")))["events"]}
    rows = []
    for eid, g in ev.groupby("event"):
        e = evs.get(eid, {})
        o = g[["order1", "order2", "order3", "order4"]].abs().sum()
        tot = max(o.sum(), 1e-9)
        rows.append({"event_id": eid, "title": e.get("title", eid), "category": e.get("category"), "status": e.get("status"),
                     "date": e.get("date"), "p_3m": e.get("prob_by_3m"), "p_12m": e.get("prob_by_12m"),
                     "footprint": round(float(g.impact_if_event.abs().sum()), 1),
                     "companies_moved": int((g.impact_if_event.abs() >= 1).sum()),
                     "share_1st": round(o.order1 / tot, 3), "share_2nd": round(o.order2 / tot, 3),
                     "share_3rd": round(o.order3 / tot, 3), "share_4th": round(o.order4 / tot, 3),
                     "winners": ", ".join(f"{x.company} {x.impact_if_event:+.1f}" for _, x in g.nlargest(4, "impact_if_event").iterrows() if x.impact_if_event > 0.05),
                     "losers": ", ".join(f"{x.company} {x.impact_if_event:+.1f}" for _, x in g.nsmallest(4, "impact_if_event").iterrows() if x.impact_if_event < -0.05)})
    pd.DataFrame(rows).sort_values("footprint", ascending=False).to_csv(os.path.join(OUT, "events.csv"), index=False)

    so = pd.read_csv(R("results", "sensitivity_by_order.csv"))
    so["total"] = so[["order1", "order2", "order3", "order4"]].sum(axis=1)
    rs = pd.read_csv(R("results", "recent_state_vector.csv")).set_index("driver")
    rows = []
    for d, g in so.groupby("driver"):
        mass = g.total.abs().sum()
        if mass < 1:
            continue
        o = g[["order1", "order2", "order3", "order4"]].abs().sum()
        rows.append({"driver": d, "name": nodes.loc[d, "name"] if d in nodes.index else d,
                     "standard_shock": nodes.loc[d, "ssu"] if d in nodes.index else "",
                     "since_june_ssu": round(float(rs.loc[d, "state_ssu"]), 2) if d in rs.index else None,
                     "since_june_source": rs.loc[d, "source"] if d in rs.index else "",
                     "companies_moved": int((g.total.abs() >= 0.5).sum()), "footprint": round(float(mass), 1),
                     "indirect_share": round(float((o.order2 + o.order3 + o.order4) / max(o.sum(), 1e-9)), 3),
                     "gains": ", ".join(f"{x.company} {x.total:+.1f}" for _, x in g.nlargest(5, "total").iterrows() if x.total > 0.05),
                     "losses": ", ".join(f"{x.company} {x.total:+.1f}" for _, x in g.nsmallest(5, "total").iterrows() if x.total < -0.05)})
    pd.DataFrame(rows).sort_values("footprint", ascending=False).to_csv(os.path.join(OUT, "drivers.csv"), index=False)

    ch = [{"ticker": c, "order": p["order"], "chain": p["path"], "impact_if_event": round(p["impact_if_event"], 2),
           "expected_12m": round(p["expected_12m"], 2)} for c, lst in paths.items() for p in lst if p["order"] >= 2]
    pd.DataFrame(ch).sort_values("expected_12m", key=lambda s: -s.abs()).head(300).to_csv(os.path.join(OUT, "chains.csv"), index=False)

    o = so[["order1", "order2", "order3", "order4"]].abs().sum()
    pd.DataFrame({"order": ["1st", "2nd", "3rd", "4th"], "share": (o / o.sum()).round(4).values}).to_csv(os.path.join(OUT, "order_shares.csv"), index=False)
    asm = json.load(open(R("results", "assembly_report.json")))
    pd.DataFrame([{"nodes": asm["nodes"], "edges": asm["edges"], "events": asm["events"], "occurred_events": asm["occurred_events"],
                   "profiles": asm["profiles"], "analysis_date": "2026-11-05"}]).to_csv(os.path.join(OUT, "model_size.csv"), index=False)
    print(sorted(os.listdir(OUT)))


if __name__ == "__main__":
    main()
