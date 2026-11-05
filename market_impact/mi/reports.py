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
    rpaths = {}
    if os.path.exists(R("results", "recent_state_paths.jsonl")):
        for line in open(R("results", "recent_state_paths.jsonl")):
            o = json.loads(line)
            rpaths[o["company"]] = o["top"]
    events = {}
    eff = R("results", "events_effective.json")      # catalogue after dedup drops and Director/red-team overrides
    if os.path.exists(eff):
        for e in json.load(open(eff))["events"]:
            events[e["event_id"]] = e
    else:
        for p in glob.glob(R("events", "*.json")):
            for e in json.load(open(p)).get("events", []):
                events[e["event_id"]] = e
    return rk, ev, so, nodes, fs, paths, events, rpaths


def stock_report(r, ev, so, nodes, fs, paths, events, rpaths=None):
    t = r.company
    L = [f"# {t} — {r['name']}", f"*{r.tier} · {r.nse_industry} · analysis date 2026-11-05 · model run from the Market Impact Graph*", ""]
    pb = lambda x: "—" if x is None or pd.isna(x) else f"{100 * x:.0f}%"
    L += ["## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)",
          f"- Expected relative return: **3 months {f1(r.exp_rel_return_3m)}%**, **12 months {f1(r.exp_rel_return_12m)}%** "
          f"(rank {int(r.rank_3m)} / {int(r.rank_12m)} of 200 for 3m / 12m); beta {r.get('beta', float('nan')):.2f}",
          f"- Probability of beating the universe (incl. idiosyncratic noise, 12m vol {f1(r.get('idio_vol_12m'))}%): "
          f"3 months {pb(r.get('prob_outperform_3m'))}, 12 months {pb(r.get('mc_prob_outperform'))}",
          f"- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 {f1(r.get('mc_p10_12m'))}% … "
          f"P90 {f1(r.get('mc_p90_12m'))}%; plausible 12m relative-return range incl. stock-specific noise: "
          f"{f1(r.get('ret_p10_12m'))}% … {f1(r.get('ret_p90_12m'))}%",
          f"- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves {f1(r.residual_contribution)} pp "
          f"(model impact {f1(r.recent_events_model_impact)}% beta-adjusted vs realised market-adjusted move "
          f"{f1(r.realised_mkt_adj_since_jun)}%); forward event exposure {f1(r.forward_exposure_12m)}% (3m {f1(r.forward_exposure_3m)}%; "
          f"half assumed priced); company-specific events {f1(r.company_events_12m)}%", ""]
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
    fw = [p for p in paths.get(t, []) if p.get("status") != "occurred"]
    if fw:
        L += ["## Strongest forward causal chains (upcoming/risk events, 1st–4th order)",
              "Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).",
              "| order | chain | impact if event | expected 12m |", "|---|---|---|---|"]
        for p in fw[:15]:
            L.append(f"| {p['order']} | {p['path']} | {f2(p['impact_if_event'])}% | {f2(p['expected_12m'])}% |")
        L.append("")
    rp = (rpaths or {}).get(t, [])
    if rp:
        L += ["## What has already moved since 1 June 2026 (driver change × path)",
              "Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, "
              "before beta adjustment and before comparing with the realised share-price move.",
              "| order | chain | driver change (SSU) | source | impact |", "|---|---|---|---|---|"]
        for p in rp[:12]:
            L.append(f"| {p['order']} | {p['path']} | {p['state_ssu']:+.2f} | {p['source']} | {f2(p['impact'])}% |")
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
    if e.get("director_override"):
        L += ["**Review override applied:** " + str(e["director_override"]), ""]
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


def summary(rk, ev, so, nodes, paths, events, rpaths=None):
    """reports/SUMMARY.md — the one-page answer: rankings, Next 50, sectors, events, drivers, multi-order chains."""
    pb = lambda x: "—" if x is None or pd.isna(x) else f"{100 * x:.0f}%"
    asm = json.load(open(R("results", "assembly_report.json")))
    L = ["# Market Impact Graph — Nifty 200 second-to-fourth-order effects (analysis date 2026-11-05)", "",
         "**What this is.** A causal exposure network: events → macro/commodity/policy/geopolitical drivers → companies, "
         f"with {asm['edges']} weighted edges among {asm['nodes']} nodes ({asm['profiles']} company profiles, "
         f"{asm['events']} events of which {asm['occurred_events']} already occurred since June 2026). Effects propagate up to "
         "four hops, damped by order, with double-count controls (clamping, overlap damping, link semantics).", "",
         "**How to read the numbers.** Expected returns are *scenario-implied*, beta-adjusted and relative to the Nifty 200 "
         "average. They combine the still-unpriced part of June–November driver moves with probability-weighted forward events "
         "(half assumed priced) and company-specific catalysts. They are not validated forecasts; the rankings are frozen in "
         "`ledger/` and will be scored against realised returns and a momentum baseline.", ""]
    cols = "| # | ticker | name | industry | exp 3m | exp 12m | P(beat 12m) | strongest positive chain | strongest negative chain |"
    top = defaultdict(lambda: ("—", "—"))
    for c, lst in paths.items():
        pos = [p for p in lst if p["expected_12m"] > 0 and p.get("status") != "occurred"]
        neg = [p for p in lst if p["expected_12m"] < 0 and p.get("status") != "occurred"]
        top[c] = (pos[0]["path"] if pos else "—", neg[0]["path"] if neg else "—")
    def table(df, title):
        out = [f"## {title}", cols, "|---|---|---|---|---|---|---|---|---|"]
        for _, r in df.iterrows():
            p, n = top[r.company]
            out.append(f"| {int(r.rank_12m)} | [{r.company}](stocks/{r.company}.md) | {r['name']} | {r.nse_industry} | {f1(r.exp_rel_return_3m)} | "
                       f"{f1(r.exp_rel_return_12m)} | {pb(r.mc_prob_outperform)} | {p} | {n} |")
        return out + [""]
    srt = rk.sort_values("rank_12m")
    L += table(srt.head(20), "Top 20 (12-month, beta-adjusted, relative)")
    L += table(srt.tail(20).iloc[::-1], "Bottom 20")
    L += table(srt[srt.tier == "NIFTY_NEXT_50"], "Nifty Next 50 — all 50 ranked")
    sec = rk.groupby("nse_industry").agg(n=("company", "size"), exp3=("exp_rel_return_3m", "mean"), exp12=("exp_rel_return_12m", "mean"),
                                          best=("exp_rel_return_12m", lambda x: rk.loc[x.idxmax(), "company"]),
                                          worst=("exp_rel_return_12m", lambda x: rk.loc[x.idxmin(), "company"])).sort_values("exp12", ascending=False)
    L += ["## Sector view (average of member stocks)", "| industry | stocks | exp 3m | exp 12m | best | worst |", "|---|---|---|---|---|---|"]
    L += [f"| {i} | {int(x.n)} | {f1(x.exp3)} | {f1(x.exp12)} | {x.best} | {x.worst} |" for i, x in sec.iterrows()] + [""]
    if len(ev):
        e = ev[ev.status != "occurred"].copy()
        e["exp12"] = e.impact_if_event * e.prob_12m.astype(float)
        g = e.groupby("event").agg(mass=("impact_if_event", lambda x: x.abs().sum()), p12=("prob_12m", "first")).sort_values("mass", ascending=False).head(15)
        L += ["## Upcoming and risk events that matter most (impact if the event happens, % equity, raw)",
              "| event | status | P(12m) | biggest winners | biggest losers |", "|---|---|---|---|---|"]
        for eid, x in g.iterrows():
            ge = e[e.event == eid]
            w = ", ".join(f"{a.company} {f1(a.impact_if_event)}" for _, a in ge.nlargest(5, "impact_if_event").iterrows() if a.impact_if_event > 0)
            l = ", ".join(f"{a.company} {f1(a.impact_if_event)}" for _, a in ge.nsmallest(5, "impact_if_event").iterrows() if a.impact_if_event < 0)
            L.append(f"| [{events.get(eid, {}).get('title', eid)}](events/{eid}.md) | {events.get(eid, {}).get('status')} | {float(x.p12):.2f} | {w or '—'} | {l or '—'} |")
        L.append("")
        o = ev[ev.status == "occurred"].copy()
        g = o.groupby("event").impact_if_event.apply(lambda x: x.abs().sum()).sort_values(ascending=False).head(10)
        L += ["## Events since June 2026 with the widest footprint (model impact, % equity, raw)", "| event | winners | losers |", "|---|---|---|"]
        for eid in g.index:
            ge = o[o.event == eid]
            w = ", ".join(f"{a.company} {f1(a.impact_if_event)}" for _, a in ge.nlargest(4, "impact_if_event").iterrows() if a.impact_if_event > 0)
            l = ", ".join(f"{a.company} {f1(a.impact_if_event)}" for _, a in ge.nsmallest(4, "impact_if_event").iterrows() if a.impact_if_event < 0)
            L.append(f"| [{events.get(eid, {}).get('title', eid)}](events/{eid}.md) | {w or '—'} | {l or '—'} |")
        L.append("")
    if len(so):
        so2 = so.copy()
        so2["total"] = so2[["order1", "order2", "order3", "order4"]].sum(axis=1)
        so2["ind"] = so2[["order2", "order3", "order4"]].sum(axis=1)
        d = so2.groupby("driver").agg(reach=("total", lambda x: int((x.abs() >= 0.5).sum())), mass=("total", lambda x: x.abs().sum()),
                                       ind=("ind", lambda x: x.abs().sum())).sort_values("mass", ascending=False).head(20)
        L += ["## Drivers with the widest reach (see DRIVERS.md for the company lists)",
              "| driver | standard shock | companies moved ≥0.5% | share via 2nd–4th order |", "|---|---|---|---|"]
        L += [f"| {nodes.loc[i, 'name'] if i in nodes.index else i} (`{i}`) | {nodes.loc[i, 'ssu'] if i in nodes.index else ''} | {x.reach} | "
              f"{100 * x.ind / max(x.mass, 1e-9):.0f}% |" for i, x in d.iterrows()] + [""]
    chains = [(c, p) for c, lst in paths.items() for p in lst if p["order"] >= 3 and p.get("status") != "occurred"]
    chains.sort(key=lambda cp: -abs(cp[1]["expected_12m"]))
    L += ["## Strongest 3rd- and 4th-order chains from upcoming/risk events (expected 12m = probability × impact)",
          "| company | order | chain | impact if event | expected 12m |", "|---|---|---|---|---|"]
    L += [f"| {c} | {p['order']} | {p['path']} | {f2(p['impact_if_event'])}% | {f2(p['expected_12m'])}% |" for c, p in chains[:25]] + [""]
    rc = [(c, p) for c, lst in (rpaths or {}).items() for p in lst if p["order"] >= 2]
    rc.sort(key=lambda cp: -abs(cp[1]["impact"]))
    L += ["## Strongest 2nd–4th-order chains from what already moved since 1 June 2026 (raw model impact)",
          "| company | order | chain | driver change (SSU) | source | impact |", "|---|---|---|---|---|---|"]
    L += [f"| {c} | {p['order']} | {p['path']} | {p['state_ssu']:+.2f} | {p['source']} | {f2(p['impact'])}% |" for c, p in rc[:25]] + [""]
    L += ["## Files", "- `RANKINGS.md` — all 200 stocks; `stocks/<TICKER>.md` — per-stock deep dive (drivers by order, events, chains, "
          "analyst profile); `events/<EVENT>.md` — per-event winners/losers by order; `EVENTS.md`; `DRIVERS.md`.",
          "- Data: `results/rankings.csv`, `results/sensitivity_by_order.csv`, `results/event_impacts.csv`, `results/edges_all.csv`.",
          "- Method: `PLAN.md`, `docs/AGENT_SPEC.md`; review trail: `review/`, `graph/*overrides*.json`."]
    open(R("reports", "SUMMARY.md"), "w").write("\n".join(L) + "\n")


def main():
    rk, ev, so, nodes, fs, paths, events, rpaths = load()
    os.makedirs(R("reports", "stocks"), exist_ok=True)
    os.makedirs(R("reports", "events"), exist_ok=True)
    for f in glob.glob(R("reports", "events", "*.md")):      # regenerate: dropped events must not linger
        os.remove(f)
    for _, r in rk.iterrows():
        open(R("reports", "stocks", f"{r.company}.md"), "w").write(stock_report(r, ev, so, nodes, fs, paths, events, rpaths))
    for eid, e in events.items():
        open(R("reports", "events", f"{eid}.md"), "w").write(event_report(eid, e, ev, nodes))
    # rankings table with top +/- drivers per company (from event paths)
    top = defaultdict(lambda: ("—", "—"))
    for c, lst in paths.items():
        pos = [p for p in lst if p["expected_12m"] > 0 and p.get("status") != "occurred"]
        neg = [p for p in lst if p["expected_12m"] < 0 and p.get("status") != "occurred"]
        top[c] = (pos[0]["path"] if pos else "—", neg[0]["path"] if neg else "—")
    L = ["# Nifty 200 — scenario-implied ranking (relative to the universe average), 2026-11-05", "",
         "Expected relative returns are exposure-driven estimates from the Market Impact Graph, not validated forecasts.", "",
         "Beta-adjusted: each stock's impacts are net of beta × the universe-average impact. P(beat 12m) includes "
         "idiosyncratic noise. Model band = P10…P90 of the 12m expectation over event and edge-weight draws.", "",
         "| rank 12m | ticker | name | tier | industry | exp 3m % | exp 12m % | model band 12m | P(beat 3m) | P(beat 12m) | strongest positive chain | strongest negative chain |",
         "|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for _, r in rk.sort_values("rank_12m").iterrows():
        p, n = top[r.company]
        L.append(f"| {int(r.rank_12m)} | {r.company} | {r['name']} | {r.tier} | {r.nse_industry} | {f1(r.exp_rel_return_3m)} | "
                 f"{f1(r.exp_rel_return_12m)} | {f1(r.get('mc_p10_12m'))}…{f1(r.get('mc_p90_12m'))} | "
                 f"{'—' if pd.isna(r.get('prob_outperform_3m')) else f'{100 * r.prob_outperform_3m:.0f}%'} | "
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
    # driver → companies map (what effect hits which company), with the driver's recent and expected move
    D = ["# Drivers — which companies each effect moves", "",
         "% change in equity value per +1 standard shock (SSU) of the driver, all orders (1st–4th), raw (not beta-adjusted). "
         "Recent state = the driver's change since 1 Jun 2026 in SSU (observed market series, occurred events or Director "
         "override).", ""]
    rs = pd.read_csv(R("results", "recent_state_vector.csv")).set_index("driver") if os.path.exists(R("results", "recent_state_vector.csv")) else pd.DataFrame()
    if len(so):
        so2 = so.copy()
        so2["total"] = so2[["order1", "order2", "order3", "order4"]].sum(axis=1)
        so2["indirect"] = so2[["order2", "order3", "order4"]].sum(axis=1)
        reach = so2[so2.total.abs() >= 0.5].groupby("driver").agg(n=("company", "size"), mass=("total", lambda x: x.abs().sum()))
        for d in reach.sort_values("mass", ascending=False).index[:80]:
            g = so2[so2.driver == d]
            nm = nodes.loc[d, "name"] if d in nodes.index else d
            ssu = nodes.loc[d, "ssu"] if d in nodes.index else ""
            st = f"{rs.loc[d, 'state_ssu']:+.2f} SSU ({rs.loc[d, 'source']})" if len(rs) and d in rs.index else "—"
            win = ", ".join(f"{x.company} {x.total:+.1f}" for _, x in g.nlargest(8, "total").iterrows() if x.total > 0)
            los = ", ".join(f"{x.company} {x.total:+.1f}" for _, x in g.nsmallest(8, "total").iterrows() if x.total < 0)
            ind = 100 * g.indirect.abs().sum() / max(g.total.abs().sum(), 1e-9)
            D += [f"## {nm} (`{d}`) — SSU {ssu}", f"- Companies with |effect| ≥ 0.5%: {int(reach.loc[d, 'n'])}; share via 2nd–4th order: {ind:.0f}%; "
                  f"recent state: {st}", f"- Gains: {win or '—'}", f"- Losses: {los or '—'}", ""]
    open(R("reports", "DRIVERS.md"), "w").write("\n".join(D) + "\n")
    summary(rk, ev, so, nodes, paths, events, rpaths)
    print({"stocks": len(rk), "events": len(events)})


if __name__ == "__main__":
    main()
