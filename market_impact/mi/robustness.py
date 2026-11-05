"""Robustness of the rankings to the model's arbitrary choices.

Run after mi.graph: python3 -m market_impact.mi.robustness
Each variant re-runs the engine (no Monte Carlo) with one assumption changed and compares its 12m and 3m rankings with
the baseline: Spearman rank correlation, overlap of the top-20 and bottom-20 sets, and each stock's rank range.
results/ is backed up and restored, so the baseline outputs are untouched.
Outputs: results/robustness.csv, results/robustness_ranks.csv, reports/ROBUSTNESS.md (+ dashboard copies).
"""
import copy
import os
import shutil
import tempfile

import numpy as np
import pandas as pd

from . import graph as G

R = G.R


def _run(label, patch=None, unpatch=None):
    try:
        if patch:
            patch()
        G.run(0)
        rk = pd.read_csv(R("results", "rankings.csv")).set_index("company")
        return rk[["exp_rel_return_3m", "exp_rel_return_12m"]].rename(columns=lambda c: f"{label}|{c}")
    finally:
        if unpatch:
            unpatch()


def _setter(name, value):
    old = copy.deepcopy(getattr(G, name))
    return (lambda: setattr(G, name, value)), (lambda: setattr(G, name, old))


def _damp(scale):
    old = dict(G.DAMP)
    new = {k: (v if k == 1 else min(1.0, v * scale)) for k, v in old.items()}
    return (lambda: G.DAMP.update(new)), (lambda: G.DAMP.update(old))


def _edge_noise(seed, sd=0.3):
    orig = G.assemble

    def noisy():
        nodes, edges, events, profiles, dropped = orig()
        rng = np.random.default_rng(seed)
        for e in edges:
            f = float(np.exp(rng.normal(0.0, sd)))
            for k in ("w", "w_low", "w_high"):
                e[k] = float(e[k]) * f
        return nodes, edges, events, profiles, dropped
    return (lambda: setattr(G, "assemble", noisy)), (lambda: setattr(G, "assemble", orig))


def _prob_noise(seed, lo=0.7, hi=1.3):
    orig = G.assemble

    def noisy():
        nodes, edges, events, profiles, dropped = orig()
        rng = np.random.default_rng(seed)
        for ev in events:
            if ev.get("status") == "occurred":
                continue
            f = float(rng.uniform(lo, hi))
            p3 = min(1.0, float(ev.get("prob_by_3m", 0) or 0) * f)
            p12 = min(1.0, float(ev.get("prob_by_12m", 0) or 0) * f)
            ev["prob_by_3m"], ev["prob_by_12m"] = min(p3, p12), p12
        return nodes, edges, events, profiles, dropped
    return (lambda: setattr(G, "assemble", noisy)), (lambda: setattr(G, "assemble", orig))


def _no_beta():
    orig = G.realised_moves

    def flat(comps):
        moves, betas = orig(comps)
        return moves, {c: 1.0 for c in betas}
    return (lambda: setattr(G, "realised_moves", flat)), (lambda: setattr(G, "realised_moves", orig))


VARIANTS = [
    ("Company catalysts weighted 0.25 (vs 0.5)", "PRICED_SHARE_COMPANY", 0.75),
    ("Company catalysts weighted 0.75 (vs 0.5)", "PRICED_SHARE_COMPANY", 0.25),
    ("No company catalysts", "PRICED_SHARE_COMPANY", 1.0),
    ("Higher-order damping ×0.8", "damp", 0.8),
    ("Higher-order damping ×1.2", "damp", 1.2),
    ("Overlap damping 0.25 (vs 0.5)", "OVERLAP_DAMP", 0.25),
    ("Overlap damping 0.75 (vs 0.5)", "OVERLAP_DAMP", 0.75),
    ("1st order only (depth 1)", "MAX_DEPTH", 1),
    ("Up to 2nd order (depth 2)", "MAX_DEPTH", 2),
    ("Up to 3rd order (depth 3)", "MAX_DEPTH", 3),
    ("No market-priced neutralisation", "MARKET_PRICED", set()),
    ("No beta adjustment", "nobeta", None),
    ("Edge weights ×lognormal(0.3), seed 1", "edge", 1),
    ("Edge weights ×lognormal(0.3), seed 2", "edge", 2),
    ("Edge weights ×lognormal(0.3), seed 3", "edge", 3),
    ("Event probabilities ×U(0.7,1.3), seed 1", "prob", 1),
    ("Event probabilities ×U(0.7,1.3), seed 2", "prob", 2),
    ("Event probabilities ×U(0.7,1.3), seed 3", "prob", 3),
]


def _compare(base, var, name, h):
    b, v = base[f"base|exp_rel_return_{h}"], var
    k = 20
    top_b, top_v = set(b.nlargest(k).index), set(v.nlargest(k).index)
    bot_b, bot_v = set(b.nsmallest(k).index), set(v.nsmallest(k).index)
    return {"variant": name, "horizon": h, "spearman": round(float(b.corr(v, method="spearman")), 3),
            "top20_overlap": len(top_b & top_v), "bottom20_overlap": len(bot_b & bot_v),
            "top10_still_top20": len(set(b.nlargest(10).index) & top_v), "dispersion_sd": round(float(v.std()), 2)}


def main():
    backup = tempfile.mkdtemp(prefix="mi_results_")
    shutil.copytree(R("results"), os.path.join(backup, "results"))
    try:
        base = _run("base")
        cols = [base]
        for name, kind, val in VARIANTS:
            if kind == "damp":
                p, u = _damp(val)
            elif kind == "edge":
                p, u = _edge_noise(val)
            elif kind == "prob":
                p, u = _prob_noise(val)
            elif kind == "nobeta":
                p, u = _no_beta()
            else:
                p, u = _setter(kind, val)
            cols.append(_run(name, p, u))
            print("done:", name)
        allr = pd.concat(cols, axis=1)
    finally:
        shutil.rmtree(R("results"))
        shutil.copytree(os.path.join(backup, "results"), R("results"))
        shutil.rmtree(backup, ignore_errors=True)
    # leave-one-source-out from the exact attribution (no re-run needed)
    att = pd.read_csv(R("results", "attribution.csv"))
    loo = {}
    for cat in ["Policy", "Regulatory", "Sector", "Theme", "Geopolitics", "Company catalysts"]:
        for h in ("3m", "12m"):
            a = att[att.horizon == h]
            tot = a.groupby("company").value.sum()
            minus = tot - a[a.category == cat].groupby("company").value.sum().reindex(tot.index).fillna(0.0)
            loo[(f"Without {cat.lower()}", h)] = minus - minus.mean()
    rows = []
    for name, _, _ in VARIANTS:
        for h in ("3m", "12m"):
            rows.append(_compare(allr, allr[f"{name}|exp_rel_return_{h}"], name, h))
    for (name, h), v in loo.items():
        rows.append(_compare(allr, v.reindex(allr.index), name, h))
    res = pd.DataFrame(rows)
    res.to_csv(R("results", "robustness.csv"), index=False)
    # per-stock rank stability (12m) across all re-run variants
    ranks = pd.DataFrame({c.split("|")[0]: allr[c].rank(ascending=False) for c in allr.columns if c.endswith("12m")})
    rr = pd.DataFrame({"ticker": ranks.index, "base_rank": ranks["base"].astype(int).values,
                       "best_rank": ranks.min(axis=1).astype(int).values, "worst_rank": ranks.max(axis=1).astype(int).values,
                       "median_rank": ranks.median(axis=1).round(0).astype(int).values,
                       "share_in_top20": (ranks <= 20).mean(axis=1).round(2).values,
                       "share_in_bottom20": (ranks > len(ranks) - 20).mean(axis=1).round(2).values}).sort_values("base_rank")
    rr.to_csv(R("results", "robustness_ranks.csv"), index=False)
    os.makedirs(R("results", "dashboard"), exist_ok=True)
    res[res.horizon == "12m"].drop(columns="horizon").to_csv(R("results", "dashboard", "robustness.csv"), index=False)
    rr.to_csv(R("results", "dashboard", "robustness_ranks.csv"), index=False)
    _report(res, rr)
    print(res[res.horizon == "12m"].to_string(index=False))


def _report(res, rr):
    r12 = res[res.horizon == "12m"]
    L = ["# Robustness of the rankings (analysis date 2026-11-05)", "",
         "Each row changes one arbitrary modelling choice and compares the resulting ranking with the baseline. "
         "Spearman = rank correlation of expected relative returns across 200 stocks; overlaps count shared names in the "
         "top or bottom 20. 'Without …' rows remove one source of expected return using the exact attribution.", "",
         "Note: the forward-event 'priced share' multiplies every forward exposure equally, so it changes the size of the "
         "expected returns but not the ranking; it is therefore not listed. Company catalysts are varied separately.", "",
         "| variant | 12m Spearman | 3m Spearman | top-20 overlap (12m) | bottom-20 overlap (12m) | base top-10 still top-20 | spread (sd, 12m) |",
         "|---|---|---|---|---|---|---|"]
    for _, x in r12.iterrows():
        s3 = res[(res.horizon == "3m") & (res.variant == x.variant)].spearman.iloc[0]
        L.append(f"| {x.variant} | {x.spearman:.2f} | {s3:.2f} | {x.top20_overlap}/20 | {x.bottom20_overlap}/20 | "
                 f"{x.top10_still_top20}/10 | {x.dispersion_sd:.2f} |")
    stable_top = rr[(rr.base_rank <= 20) & (rr.share_in_top20 >= 0.8)].ticker.tolist()
    stable_bot = rr[(rr.base_rank > len(rr) - 20) & (rr.share_in_bottom20 >= 0.8)].ticker.tolist()
    L += ["", "## Most stable names (in the top or bottom 20 in at least 80% of re-run variants)",
          f"- Top: {', '.join(stable_top) or '—'}", f"- Bottom: {', '.join(stable_bot) or '—'}", "",
          "## Reading", "- Edge-weight and probability noise test whether the ranking depends on precise numbers the agents "
          "could not know; depth variants show how much the 2nd–4th-order links change the answer; 'without …' rows show "
          "which source of expected return drives the ranking.",
          "- Per-stock best, worst and median rank across variants: `results/robustness_ranks.csv`."]
    open(R("reports", "ROBUSTNESS.md"), "w").write("\n".join(L) + "\n")


if __name__ == "__main__":
    main()
