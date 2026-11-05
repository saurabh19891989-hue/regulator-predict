"""Generate per-stock, per-event and summary reports from graph results.

Run after mi.graph: python3 -m market_impact.mi.reports
Outputs: reports/stocks/<T>.md, reports/events/<EV>.md, reports/RANKINGS.md, reports/EVENTS.md
"""
import glob
import json
import os
from collections import defaultdict

import pandas as pd

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
R = lambda *p: os.path.join(HERE, *p)
f1 = lambda x: "—" if x is None or pd.isna(x) else f"{x:+.1f}"
f2 = lambda x: "—" if x is None or pd.isna(x) else f"{x:+.2f}"


def load():
    rk = pd.read_csv(R("results", "rankings.csv"))
    ev = pd.read_csv(R("results", "event_impacts.csv")) if os.path.exists(R("results", "event_impacts.csv")) else pd.DataFrame()
    so = pd.read_csv(R("results", "sensitivity_by_order.csv")) if os.path.exists(R("results", "sensitivity_by_order.csv")) else pd.DataFrame()
    nodes = pd.read_csv(R("results", "nodes_all.csv")).set_index("id")
    fs = pd.read_csv(R("results", "factor_state.csv")).set_index("node") if os.path.exists(R("results", "factor_state.csv")) else pd.DataFrame()
    paths = {}
    if os.path.exists(R("results", "company_paths.jsonl")):
        for line in open(R("results", "company_paths.jsonl")):
            o = json.loads(line)
            paths[o["company"]] = o["top_paths"]
    events = {}
    for p in glob.glob(R("events", "*.json")):
        for e in json.load(open(p)).get("events", []):
            events[e["event_id"]] = e
    return rk, ev, so, nodes, fs, paths, events


def stock_report(r, ev, so, nodes, fs, paths, events):
    t = r.company
    L = [f"# {t} — {r['name']}", f"*{r.tier} · {r.nse_industry} · analysis date 2026-11-05 · model run from the Market Impact Graph*", ""]
    L += ["## Scenario-implied verdict (relative to the Nifty 200 average; not a validated forecast)",
          f"- Expected relative return: **3 months {f1(r.exp_rel_return_3m)}%**, **12 months {f1(r.exp_rel_return_12m)}%** "
          f"(rank {int(r.rank_3m)} / {int(r.rank_12m)} of 200 for 3m / 12m)",
          f"- 12-month Monte Carlo range (event occurrence × edge-weight uncertainty): P10 {f1(r.get('mc_p10_12m'))}%, "
          f"P50 {f1(r.get('mc_p50_12m'))}%, P90 {f1(r.get('mc_p90_12m'))}%; probability of beating the universe "
          f"{'—' if pd.isna(r.get('mc_prob_outperform')) else f'{100 * r.mc_prob_outperform:.0f}%'}",
          f"- Decomposition: unrealised residual of Jun–Nov 2026 events {f1(r.residual_contribution)} pp "
          f"(model impact {f1(r.recent_events_model_impact)}% vs realised market-adjusted move {f1(r.realised_mkt_adj_since_jun)}%); "
          f"forward event exposure 3m {f1(r.forward_exposure_3m)}% / 12m {f1(r.forward_exposure_12m)}% (half assumed priced); "
          f"company-specific events 12m {f1(r.company_events_12m)}%", ""]
    g = so[so.company == t].copy() if len(so) else pd.DataFrame()
    if len(g):
        g["total"] = g[["order1", "order2", "order3", "order4"]].sum(axis=1)
        g = g.reindex(g.total.abs().sort_values(ascending=False).index).head(14)
        L += ["## What moves this stock (company → drivers)",
              "% change in equity value for a +1 standard shock of each driver, split by causal order.",
              "| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |", "|---|---|---|---|---|---|---|---|"]
        for _, x in g.iterrows():
            nm = nodes.loc[x.driver, "name"] if x.driver in nodes.index else x.driver
            ssu = nodes.loc[x.driver, "ssu"] if x.driver in nodes.index else ""
            mv = fs.loc[x.driver, "chg_since_2026_06_01_pct"] if len(fs) and x.driver in fs.index else None
            L.append(f"| {nm} (`{x.driver}`) | {ssu} | {f2(x.total)} | {f2(x.order1)} | {f2(x.order2)} | {f2(x.order3)} | {f2(x.order4)} | {f1(mv) + '%' if mv is not None else '—'} |")
        L.append("")
    e = ev[ev.company == t].copy() if len(ev) else pd.DataFrame()
    if len(e):
        e["exp12"] = e.impact_if_event * e.prob_12m.astype(float)
        e = e.reindex(e.exp12.abs().sort_values(ascending=False).index).head(12)
        L += ["## Events affecting this stock (event → company)",
              "| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |", "|---|---|---|---|---|---|---|---|---|"]
        for _, x in e.iterrows():
            title = events.get(x.event, {}).get("title", x.event)
            L.append(f"| {title} (`{x.event}`) | {x.status} | {float(x.prob_12m):.2f} | {f1(x.impact_if_event)}% | {f1(x.exp12)}% | "
                     f"{f1(x.order1)} | {f1(x.order2)} | {f1(x.order3)} | {f1(x.order4)} |")
        L.append("")
    if paths.get(t):
        L += ["## Strongest causal chains (1st–4th order)", "| order | chain | impact if event | expected 12m |", "|---|---|---|---|"]
        for p in paths[t][:15]:
            L.append(f"| {p['order']} | {p['path']} | {f2(p['impact_if_event'])}% | {f2(p['expected_12m'])}% |")
        L.append("")
    md = R("companies", f"{t}.md")
    L += ["## Analyst profile (agent research, sourced)", open(md).read() if os.path.exists(md) else "_Profile not yet available._", ""]
    L += ["## Caveats", "Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price "
          "co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record."]
    return "\n".join(L)


def event_report(eid, e, ev, nodes):
    g = ev[ev.event == eid].copy()
    L = [f"# {e.get('title', eid)} (`{eid}`)", f"*{e.get('category')} · status {e.get('status')} · date {e.get('date')} · "
         f"P(3m) {e.get('prob_by_3m')} · P(12m) {e.get('prob_by_12m')} · confidence {e.get('confidence')}*", "",
         e.get("description", ""), ""]
    if e.get("what_already_moved"):
        L += ["**Already moved:** " + str(e["what_already_moved"]), ""]
    L += ["## Entry shocks (conditional on the event)"] + [
        f"- `{s['node']}` {nodes.loc[s['node'], 'name'] if s['node'] in nodes.index else ''}: {s.get('ssu')} SSU "
        f"(range {s.get('low')}…{s.get('high')}) {s.get('note', '')}" for s in e.get("entry_shocks", [])] + [""]
    if e.get("chains"):
        L += ["## Causal chains (agent)"] + [f"- order {c.get('order')}: {' → '.join(c.get('path', []))} — {c.get('explanation', '')}" for c in e["chains"]] + [""]
    if len(g):
        for title, part in (("Most positively affected", g.nlargest(15, "impact_if_event")), ("Most negatively affected", g.nsmallest(15, "impact_if_event"))):
            L += [f"## {title} (impact if the event happens, % equity value)", "| company | total | 1st | 2nd | 3rd | 4th |", "|---|---|---|---|---|---|"]
            for _, x in part.iterrows():
                L.append(f"| {x.company} | {f1(x.impact_if_event)} | {f1(x.order1)} | {f1(x.order2)} | {f1(x.order3)} | {f1(x.order4)} |")
            L.append("")
        tot = g[["order1", "order2", "order3", "order4"]].abs().sum()
        L += ["Share of absolute impact by order: " + ", ".join(f"{k[-1]}: {100 * v / max(tot.sum(), 1e-9):.0f}%" for k, v in tot.items()), ""]
    L += ["## Sources"] + [f"- {s.get('date', '')} {s.get('title', '')} {s.get('url', '')}" for s in e.get("sources", [])]
    return "\n".join(L)


def main():
    rk, ev, so, nodes, fs, paths, events = load()
    os.makedirs(R("reports", "stocks"), exist_ok=True)
    os.makedirs(R("reports", "events"), exist_ok=True)
    for _, r in rk.iterrows():
        open(R("reports", "stocks", f"{r.company}.md"), "w").write(stock_report(r, ev, so, nodes, fs, paths, events))
    for eid, e in events.items():
        open(R("reports", "events", f"{eid}.md"), "w").write(event_report(eid, e, ev, nodes))
    # rankings table with top +/- drivers per company (from event paths)
    top = defaultdict(lambda: ("—", "—"))
    for c, lst in paths.items():
        pos = [p for p in lst if p["expected_12m"] > 0]
        neg = [p for p in lst if p["expected_12m"] < 0]
        top[c] = (pos[0]["path"] if pos else "—", neg[0]["path"] if neg else "—")
    L = ["# Nifty 200 — scenario-implied ranking (relative to the universe average), 2026-11-05", "",
         "Expected relative returns are exposure-driven estimates from the Market Impact Graph, not validated forecasts.", "",
         "| rank 12m | ticker | name | tier | industry | exp 3m % | exp 12m % | P10–P90 12m | P(beat) | strongest positive chain | strongest negative chain |",
         "|---|---|---|---|---|---|---|---|---|---|---|"]
    for _, r in rk.sort_values("rank_12m").iterrows():
        p, n = top[r.company]
        L.append(f"| {int(r.rank_12m)} | {r.company} | {r['name']} | {r.tier} | {r.nse_industry} | {f1(r.exp_rel_return_3m)} | "
                 f"{f1(r.exp_rel_return_12m)} | {f1(r.get('mc_p10_12m'))}…{f1(r.get('mc_p90_12m'))} | "
                 f"{'—' if pd.isna(r.get('mc_prob_outperform')) else f'{100 * r.mc_prob_outperform:.0f}%'} | {p} | {n} |")
    open(R("reports", "RANKINGS.md"), "w").write("\n".join(L) + "\n")
    E = ["# Event catalogue — impact summary", "", "| event | category | status | date | P(3m) | P(12m) | biggest winners (if event) | biggest losers (if event) |",
         "|---|---|---|---|---|---|---|---|"]
    for eid, e in sorted(events.items(), key=lambda kv: (kv[1].get("status") != "occurred", str(kv[1].get("date")))):
        g = ev[ev.event == eid] if len(ev) else pd.DataFrame()
        win = ", ".join(f"{x.company} {f1(x.impact_if_event)}" for _, x in g.nlargest(4, "impact_if_event").iterrows()) if len(g) else "—"
        los = ", ".join(f"{x.company} {f1(x.impact_if_event)}" for _, x in g.nsmallest(4, "impact_if_event").iterrows()) if len(g) else "—"
        E.append(f"| [{e.get('title', eid)}](events/{eid}.md) | {e.get('category')} | {e.get('status')} | {e.get('date')} | {e.get('prob_by_3m')} | {e.get('prob_by_12m')} | {win} | {los} |")
    open(R("reports", "EVENTS.md"), "w").write("\n".join(E) + "\n")
    print({"stocks": len(rk), "events": len(events)})


if __name__ == "__main__":
    main()
