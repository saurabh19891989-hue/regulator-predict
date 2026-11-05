"""Build per-company evidence packs, factor-state table and agent batches (no LLM).

Run after prices/dossiers/news: python3 -m market_impact.mi.packs
Outputs: data/packs/<T>.md, results/factor_state.md, results/factor_state.csv, results/batches.json
"""
import csv
import json
import os

import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def factor_state():
    df = pd.read_csv(os.path.join(HERE, "data", "prices", "close.csv"), index_col=0, parse_dates=True)
    nodes = {n["id"]: n for n in json.load(open(os.path.join(HERE, "graph", "nodes_seed.json")))}
    last = df.index.max()
    rows = []
    for c in df.columns:
        if nodes.get(c, {}).get("type") == "COMPANY":
            continue
        s = df[c].dropna()
        if s.empty:
            continue

        def chg(days):
            past = s[s.index <= last - pd.Timedelta(days=days)]
            if past.empty:
                return None
            return float(s.iloc[-1] / past.iloc[-1] - 1) * 100
        rows.append({"node": c, "name": nodes.get(c, {}).get("name", c), "series": nodes.get(c, {}).get("series", ""),
                     "last": round(float(s.iloc[-1]), 4), "last_date": str(s.index[-1].date()),
                     "chg_1m_pct": chg(30), "chg_3m_pct": chg(91), "chg_6m_pct": chg(182), "chg_12m_pct": chg(365),
                     "chg_since_2026_06_01_pct": float(s.iloc[-1] / s[s.index <= "2026-06-01"].iloc[-1] - 1) * 100 if (s.index <= "2026-06-01").any() else None})
    fs = pd.DataFrame(rows)
    fs.to_csv(os.path.join(HERE, "results", "factor_state.csv"), index=False)
    md = ["# Factor state as of " + str(last.date()) + " (Yahoo Finance closes; % changes)", "",
          "| node | name | last | 1m | 3m | 6m | 12m | since 2026-06-01 |", "|---|---|---|---|---|---|---|---|"]
    f = lambda x: "" if x is None or (isinstance(x, float) and np.isnan(x)) else f"{x:+.1f}"
    for r in rows:
        md.append(f"| {r['node']}{' (STALE: last ' + r['last_date'] + ')' if r['last_date'] < str((last - pd.Timedelta(days=14)).date()) else ''} | {r['name']} | {r['last']} | {f(r['chg_1m_pct'])} | {f(r['chg_3m_pct'])} | {f(r['chg_6m_pct'])} | {f(r['chg_12m_pct'])} | {f(r['chg_since_2026_06_01_pct'])} |")
    md.append("\nNote: yields (US 10Y, ^IRX) and VIX changes are % changes of the level, not bp/points.")
    open(os.path.join(HERE, "results", "factor_state.md"), "w").write("\n".join(md) + "\n")


def packs():
    nodes = {n["id"]: n for n in json.load(open(os.path.join(HERE, "graph", "nodes_seed.json")))}
    sens = pd.read_csv(os.path.join(HERE, "results", "empirical_sensitivities.csv"))
    perf = pd.read_csv(os.path.join(HERE, "results", "price_performance.csv")).set_index("company")
    os.makedirs(os.path.join(HERE, "data", "packs"), exist_ok=True)
    for t, n in nodes.items():
        if n["type"] != "COMPANY":
            continue
        out = [f"# Evidence pack — {t} ({n['name']})", f"Tier: {n['tier']} · NSE industry: {n['nse_industry']} · as of 2026-11-05", ""]
        dp = os.path.join(HERE, "data", "dossiers", f"{t}.md")
        out += ["## Fundamentals (screener.in)", open(dp).read() if os.path.exists(dp) else "(dossier unavailable — fetch https://www.screener.in/company/" + t + "/consolidated/ yourself)", ""]
        if t in perf.index:
            p = perf.loc[t]
            out += ["## Price performance (%, Yahoo closes)",
                    f"last close {p['last_close']:.2f}; 1m {p['ret_1m']:+.1f}; 3m {p['ret_3m']:+.1f}; 6m {p['ret_6m']:+.1f}; 12m {p['ret_12m']:+.1f}; 1y vol {p['vol_1y_ann']:.0f}% ann.", ""]
        s = sens[sens.company == t].copy()
        if len(s):
            s["abs_t"] = s.t_stat.abs()
            s = s.sort_values("abs_t", ascending=False).head(12)
            out += ["## Empirical market-adjusted sensitivities (weekly, 3y; % stock move per +1 SSU of the factor, controlling for Nifty 50)",
                    "| factor | elasticity per SSU | t-stat | market beta |", "|---|---|---|---|"]
            for _, r in s.iterrows():
                out.append(f"| {r.factor} | {r.elasticity_per_ssu:+.2f} | {r.t_stat:+.1f} | {r.beta_mkt:.2f} |")
            out += ["(|t| ≥ 2 is a statistically meaningful co-movement; this is price co-movement, not proof of a fundamental link.)", ""]
        npth = os.path.join(HERE, "data", "news", f"{t}.json")
        if os.path.exists(npth):
            items = json.load(open(npth)).get("items", [])[:18]
            out += ["## Recent headlines (Google News, last 60 days; verify before relying)"] + \
                   [f"- {i['date']} | {i['title']} | {i['source']}" for i in items] + [""]
        open(os.path.join(HERE, "data", "packs", f"{t}.md"), "w").write("\n".join(out))


def batches(size=8):
    nodes = json.load(open(os.path.join(HERE, "graph", "nodes_seed.json")))
    comps = [n for n in nodes if n["type"] == "COMPANY"]
    comps.sort(key=lambda n: (n["nse_industry"], 0 if n["tier"] == "NIFTY_NEXT_50" else 1, n["id"]))
    out = [comps[i:i + size] for i in range(0, len(comps), size)]
    b = [{"batch": f"B{i + 1:02d}", "tickers": [c["id"] for c in grp], "industries": sorted({c["nse_industry"] for c in grp}),
          "next50": sum(c["tier"] == "NIFTY_NEXT_50" for c in grp)} for i, grp in enumerate(out)]
    json.dump(b, open(os.path.join(HERE, "results", "batches.json"), "w"), indent=1)
    return b


if __name__ == "__main__":
    factor_state()
    packs()
    b = batches()
    print(len(b), "batches;", sum(len(x["tickers"]) for x in b), "companies")
