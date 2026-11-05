"""Prospective ledger: freeze today's rankings (with a no-model momentum baseline) and score them later.

Freeze: python3 -m market_impact.mi.ledger freeze      → ledger/predictions_<YYYYMMDD>.csv (+ .sha256)
Score:  python3 -m market_impact.mi.ledger score <file> → realised relative returns, rank IC vs momentum baseline
Frozen files are never edited; scoring writes a separate file.
"""
import hashlib
import json
import os
import subprocess
import sys
from datetime import datetime, timezone

import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
R = lambda *p: os.path.join(HERE, *p)


def momentum_baseline():
    df = pd.read_csv(R("data", "prices", "close.csv"), index_col=0, parse_dates=True)
    last = df.index.max()
    out = {}
    for c in df.columns:
        if c.startswith(("F_", "MKT_")):
            continue
        s = df[c].dropna()
        a = s[s.index <= last - pd.Timedelta(days=365)]
        b = s[s.index <= last - pd.Timedelta(days=30)]
        if len(a) and len(b):
            out[c] = float(b.iloc[-1] / a.iloc[-1] - 1)        # 12-1 month momentum
    m = pd.Series(out)
    return ((m - m.mean()) / m.std()).rename("baseline_momentum_z")


def freeze():
    rk = pd.read_csv(R("results", "rankings.csv"))
    px = pd.read_csv(R("data", "prices", "close.csv"), index_col=0, parse_dates=True)
    now = datetime.now(timezone.utc).replace(microsecond=0)
    try:
        commit = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=HERE).decode().strip()
    except Exception:
        commit = "unknown"
    rk = rk.merge(momentum_baseline().reset_index().rename(columns={"index": "company"}), on="company", how="left")
    rk["entry_date"] = str(px.index.max().date())
    rk["entry_close"] = rk.company.map(lambda c: float(px[c].dropna().iloc[-1]) if c in px else np.nan)
    rk["frozen_at_utc"] = now.isoformat()
    rk["code_commit_at_freeze"] = commit
    keep = ["frozen_at_utc", "code_commit_at_freeze", "entry_date", "company", "name", "tier", "nse_industry", "entry_close",
            "rank_3m", "rank_12m", "exp_rel_return_3m", "exp_rel_return_12m", "mc_p10_12m", "mc_p50_12m", "mc_p90_12m",
            "mc_prob_outperform", "profile_confidence", "baseline_momentum_z"]
    rk = rk[[c for c in keep if c in rk.columns]]
    os.makedirs(R("ledger"), exist_ok=True)
    path = R("ledger", f"predictions_{now.strftime('%Y%m%d')}.csv")
    if os.path.exists(path):
        sys.exit(f"refusing to overwrite frozen ledger {path}")
    rk.to_csv(path, index=False)
    h = hashlib.sha256(open(path, "rb").read()).hexdigest()
    open(path + ".sha256", "w").write(h + "\n")
    print(json.dumps({"frozen": path, "rows": len(rk), "sha256": h}))


def score(path, horizon_days=None):
    f = pd.read_csv(path)
    h = hashlib.sha256(open(path, "rb").read()).hexdigest()
    exp = open(path + ".sha256").read().strip() if os.path.exists(path + ".sha256") else None
    px = pd.read_csv(R("data", "prices", "close.csv"), index_col=0, parse_dates=True)
    entry = pd.Timestamp(f.entry_date.iloc[0])
    end = px.index.max() if horizon_days is None else entry + pd.Timedelta(days=horizon_days)
    real = {}
    for c, e in zip(f.company, f.entry_close):
        if c in px:
            s = px[c].dropna()
            s = s[s.index <= end]
            if len(s):
                real[c] = float(s.iloc[-1] / e - 1) * 100
    f["realised_ret"] = f.company.map(real)
    f["realised_rel"] = f.realised_ret - f.realised_ret.mean()
    ok = f.dropna(subset=["realised_rel"])
    ic = lambda col: float(ok[col].rank().corr(ok.realised_rel.rank()))
    res = {"file": path, "hash_ok": exp == h, "entry": str(entry.date()), "scored_to": str(end.date()), "n": len(ok),
           "rank_ic_model_12m_signal": ic("exp_rel_return_12m"), "rank_ic_model_3m_signal": ic("exp_rel_return_3m"),
           "rank_ic_momentum_baseline": ic("baseline_momentum_z"),
           "top_decile_minus_bottom_model": float(ok.nlargest(20, "exp_rel_return_3m").realised_rel.mean() - ok.nsmallest(20, "exp_rel_return_3m").realised_rel.mean())}
    out = path.replace(".csv", f"_score_{end.strftime('%Y%m%d')}.json")
    json.dump(res, open(out, "w"), indent=1)
    print(json.dumps(res, indent=1))


if __name__ == "__main__":
    if sys.argv[1] == "freeze":
        freeze()
    else:
        score(sys.argv[2], int(sys.argv[3]) if len(sys.argv) > 3 else None)
