"""Download 5y daily closes (Yahoo chart API) for the universe + factor series; compute empirical sensitivities.

Run: python3 -m market_impact.mi.prices
Outputs: data/prices/close.csv, results/empirical_sensitivities.csv (per company × factor, SSU-scaled, market-adjusted)
"""
import json
import math
import os
import time
import urllib.parse
import urllib.request

import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/130.0 Safari/537.36"}
# SSU size in the series' natural move: ("pct", x) = x% price move; ("bp", x) = x basis points; ("pts", x) = x points
SSU_SCALE = {"F_BRENT": ("pct", 10), "F_GAS_GLOBAL": ("pct", 15), "F_COAL_INTL": ("pct", 15), "F_REFINING_MARGIN": ("pct", 10),
             "F_STEEL_GLOBAL": ("pct", 10), "F_IRON_ORE": ("pct", 15), "F_COPPER": ("pct", 10), "F_ALUMINIUM": ("pct", 10),
             "F_GOLD": ("pct", 8), "F_SILVER": ("pct", 12), "F_WHEAT": ("pct", 10), "F_SUGAR": ("pct", 10), "F_COTTON": ("pct", 10),
             "F_EDIBLE_OIL": ("pct", 10), "F_USDINR": ("pct", 3), "F_DXY": ("pct", 3), "F_USDCNY": ("pct", 3),
             "F_US_10Y": ("bp", 25), "F_FED_FUNDS": ("bp", 25), "F_RISK_SENTIMENT": ("pts", 5), "F_US_EQUITIES": ("pct", 5)}


def fetch(sym, rng="5y"):
    u = f"https://query1.finance.yahoo.com/v8/finance/chart/{urllib.parse.quote(sym)}?range={rng}&interval=1d"
    for attempt in range(3):
        try:
            d = json.load(urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=30))
            r = d["chart"]["result"][0]
            idx = pd.to_datetime(r["timestamp"], unit="s").normalize()
            s = pd.Series(r["indicators"]["quote"][0]["close"], index=idx, dtype="float64")
            return s[~s.index.duplicated(keep="last")].dropna()
        except Exception:
            time.sleep(2 * (attempt + 1))
    return None


def main():
    nodes = json.load(open(os.path.join(HERE, "graph", "nodes_seed.json")))
    want = {n["id"]: n["series"] for n in nodes if n.get("series")}
    want["MKT_NIFTY50"] = "^NSEI"
    want["MKT_NIFTY100"] = "^CNX100"
    want["MKT_INDIAVIX"] = "^INDIAVIX"
    closes, missing = {}, []
    for i, (nid, sym) in enumerate(sorted(want.items())):
        s = fetch(sym)
        if s is None or len(s) < 50:
            missing.append(nid)
        else:
            closes[nid] = s
        time.sleep(0.3)
    df = pd.DataFrame(closes).sort_index()
    df.to_csv(os.path.join(HERE, "data", "prices", "close.csv"))
    json.dump({"missing": missing, "n_series": len(closes), "last_date": str(df.index.max().date())},
              open(os.path.join(HERE, "data", "prices", "meta.json"), "w"), indent=1)
    sensitivities(df)
    print(json.dumps({"series": len(closes), "missing": missing, "last": str(df.index.max().date())}))


def sensitivities(df):
    """Weekly, last 3y: r_stock = a + b_m*r_mkt + b_f*x_f (one factor at a time). SSU-scaled elasticity = b_f * SSU."""
    w = df.resample("W-FRI").last()
    w = w[w.index >= w.index.max() - pd.Timedelta(days=3 * 365)]
    nodes = {n["id"]: n for n in json.load(open(os.path.join(HERE, "graph", "nodes_seed.json")))}
    comps = [c for c in w.columns if nodes.get(c, {}).get("type") == "COMPANY"]
    mkt = np.log(w["MKT_NIFTY50"]).diff()
    rows = []
    for f, (kind, size) in SSU_SCALE.items():
        if f not in w.columns:
            continue
        if kind == "pct":
            x = np.log(w[f]).diff() * 100            # % move
        elif kind == "bp":
            x = w[f].diff() * 100                    # yield in % → bp
        else:
            x = w[f].diff()                          # points
        for c in comps:
            y = np.log(w[c]).diff() * 100
            d = pd.concat([y, mkt * 100, x], axis=1).dropna()
            if len(d) < 60:
                continue
            X = np.column_stack([np.ones(len(d)), d.iloc[:, 1], d.iloc[:, 2]])
            beta, *_ = np.linalg.lstsq(X, d.iloc[:, 0].values, rcond=None)
            resid = d.iloc[:, 0].values - X @ beta
            s2 = resid @ resid / (len(d) - 3)
            cov = s2 * np.linalg.inv(X.T @ X)
            t = beta[2] / math.sqrt(cov[2, 2]) if cov[2, 2] > 0 else 0.0
            rows.append({"company": c, "factor": f, "beta_per_unit": beta[2], "elasticity_per_ssu": beta[2] * size,
                         "t_stat": t, "beta_mkt": beta[1], "n_weeks": len(d)})
    out = pd.DataFrame(rows)
    out.to_csv(os.path.join(HERE, "results", "empirical_sensitivities.csv"), index=False)
    # market beta + recent performance per company
    perf = []
    last = df.index.max()
    for c in comps:
        s = df[c].dropna()
        def ret(days):
            past = s[s.index <= last - pd.Timedelta(days=days)]
            return float(s.iloc[-1] / past.iloc[-1] - 1) * 100 if len(past) else None
        perf.append({"company": c, "last_close": float(s.iloc[-1]), "ret_1m": ret(30), "ret_3m": ret(91),
                     "ret_6m": ret(182), "ret_12m": ret(365), "vol_1y_ann": float(np.log(s).diff().tail(250).std() * math.sqrt(250) * 100)})
    pd.DataFrame(perf).to_csv(os.path.join(HERE, "results", "price_performance.csv"), index=False)


if __name__ == "__main__":
    main()
