"""In-sample check: does the graph's attribution of June–November driver moves explain realised stock moves?

Run after mi.graph: python3 -m market_impact.mi.insample
For every driver with a recent state (observed market series, occurred-event estimate, or reviewed override) the
graph's company response is computed with the same clamping as the engine. The cross-section of implied impacts
(beta-adjusted) is correlated with realised beta-adjusted moves since RECENT_START.
Output: results/insample_check.csv (+ results/dashboard/insample_check.csv), printed summary.
"""
import os
from collections import defaultdict

import numpy as np
import pandas as pd

from . import graph as G

DECISION_TIME = [  # measured 2026-11-05 before the stock reviews; it motivated dropping the recent component
    {"check": "All drivers (decision-time run, before reviews)", "correlation": -0.335, "spearman": -0.342, "stocks": 198,
     "group": "history", "note": "the result that removed the 'unpriced recent impact' from the headline"},
]


def main():
    nodes, edges, events, profiles, _ = G.assemble()
    net = G.Network(nodes, edges)
    occurred = [e for e in events if e.get("status") == "occurred"]
    state, src = G.recent_state(nodes, occurred)
    clamped = frozenset(src)
    contrib = defaultdict(lambda: defaultdict(float))
    for n, m in state.items():
        if abs(m) < 1e-9 or n not in nodes:
            continue
        tot, _, _ = net.unit_response(n, clamped=clamped - {n})
        for c, v in tot.items():
            contrib[n][c] += m * v
    comps = net.companies
    real, beta = G.realised_moves(comps)
    df = pd.DataFrame({n: pd.Series(d) for n, d in contrib.items()}).reindex(comps).fillna(0.0)
    df["beta"] = pd.Series(beta)
    df["real"] = pd.Series(real)
    df["industry"] = pd.Series({c: nodes[c].get("nse_industry") for c in comps})
    df = df.dropna(subset=["real"])
    drivers = [n for n in contrib if n in df.columns]

    def adj(cols):
        x = df[cols].sum(axis=1) if cols else pd.Series(0.0, index=df.index)
        return x - df.beta * x.mean()

    rows = []
    groups = {"All drivers (final run)": drivers,
              "Market-observed drivers only": [n for n in drivers if src.get(n) == "observed"],
              "Event-estimated drivers only": [n for n in drivers if src.get(n) == "events"],
              "Reviewed overrides only": [n for n in drivers if src.get(n) == "director_override"]}
    for name, cols in groups.items():
        x = adj(cols)
        rows.append({"check": name, "correlation": round(float(x.corr(df.real)), 3),
                     "spearman": round(float(x.corr(df.real, method="spearman")), 3), "stocks": int(len(df)),
                     "group": "final", "note": f"{len(cols)} drivers"})
    x = adj(drivers)
    w = pd.DataFrame({"x": x, "y": df.real, "ind": df.industry})
    w[["x", "y"]] = w.groupby("ind")[["x", "y"]].transform(lambda s: s - s.mean())
    rows.append({"check": "All drivers, within industries", "correlation": round(float(w.x.corr(w.y)), 3),
                 "spearman": round(float(w.x.corr(w.y, method="spearman")), 3), "stocks": int(len(df)), "group": "final",
                 "note": "industry averages removed from both sides"})
    # per-driver diagnostics: which observed drivers carry signal
    per = []
    for n in drivers:
        xs = df[n] - df.beta * df[n].mean()
        if xs.abs().sum() < 5:
            continue
        per.append({"driver": n, "source": src.get(n), "state_ssu": round(state[n], 2), "footprint": round(float(xs.abs().sum()), 1),
                    "correlation": round(float(xs.corr(df.real)), 3)})
    pd.DataFrame(per).sort_values("footprint", ascending=False).to_csv(G.R("results", "insample_by_driver.csv"), index=False)
    out = pd.DataFrame(DECISION_TIME + rows)
    out.to_csv(G.R("results", "insample_check.csv"), index=False)
    os.makedirs(G.R("results", "dashboard"), exist_ok=True)
    out[["check", "correlation", "spearman", "stocks", "note"]].to_csv(G.R("results", "dashboard", "insample_check.csv"), index=False)
    print(out.to_string(index=False))


if __name__ == "__main__":
    main()
