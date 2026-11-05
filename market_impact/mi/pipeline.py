"""One-command refresh and scoring for the Market Impact Graph.

Refresh everything (no LLM calls):
    python3 -m market_impact.mi.pipeline refresh [--prices] [--draws 1000] [--robustness] [--freeze LABEL "NOTE"]
  1 prices (optional, network)  → data/prices/close.csv, results/empirical_sensitivities.csv
  2 factor state                → results/factor_state.md|csv
  3 merge review overrides      → graph/*overrides*.json (from review/*.json)
  4 graph engine                → results/* (rankings, attribution, event impacts, chains …)
  5 in-sample check             → results/insample_check.csv
  6 reports                     → reports/*.md, reports/stocks/*, reports/events/*
  7 dashboard datasets          → results/dashboard/*.csv
  8 robustness (optional)       → results/robustness*.csv, reports/ROBUSTNESS.md
  9 tests                       → market_impact/tests
 10 freeze (optional)           → ledger/predictions_<date>[_LABEL].csv (+ sha256); never overwrites

Score every frozen ledger file at a horizon (refreshes prices first unless --no-prices):
    python3 -m market_impact.mi.pipeline score --days 91 [--no-prices]
  → ledger/<file>_score_<date>.json for each file, and reports/LEDGER_SCORES.md

Updating the content (events, new facts) is done with override files (graph/event_overrides.json,
graph/company_event_overrides.json, graph/edge_overrides.json, graph/recent_state_overrides.json) or review/*.json,
never by editing agent files; then run `refresh` and freeze a new dated ledger.
"""
import argparse
import glob
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
R = lambda *p: os.path.join(HERE, *p)


def step(name, fn):
    print(f"== {name}", flush=True)
    fn()


def refresh(a):
    from . import dashboard_data, graph, insample, merge_review, packs, prices, reports
    if a.prices:
        step("prices", prices.main)
    step("factor state", packs.factor_state)
    step("merge review overrides", merge_review.main)
    step("graph engine", lambda: print(json.dumps({k: v for k, v in graph.run(a.draws).items()
                                                   if k in ("nodes", "edges", "events", "profiles", "attribution_max_abs_error_pp")})))
    step("in-sample check", insample.main)
    step("reports", reports.main)
    step("dashboard datasets", dashboard_data.main)
    if a.robustness:
        from . import robustness
        step("robustness", robustness.main)
    step("tests", lambda: subprocess.run([sys.executable, "-m", "pytest", "-q", os.path.join(HERE, "tests")], check=True))
    if a.freeze:
        from . import ledger
        step("freeze", lambda: ledger.freeze(a.freeze[0] if a.freeze[0] != "-" else None, a.freeze[1] if len(a.freeze) > 1 else None))


def score(a):
    from . import ledger, prices
    if not a.no_prices:
        step("prices", prices.main)
    rows = []
    for p in sorted(glob.glob(R("ledger", "predictions_*.csv"))):
        if "_score_" in p:
            continue
        print("== score", os.path.basename(p))
        ledger.score(p, a.days)
        outs = sorted(glob.glob(p.replace(".csv", "_score_*.json")))
        if outs:
            rows.append((os.path.basename(p), json.load(open(outs[-1]))))
    L = ["# Ledger scores", "", "Rank IC = Spearman correlation between the frozen expected relative return and the realised "
         "beta-adjusted relative return over the horizon. Baseline = 12-1 month momentum frozen at the same time.", "",
         "| ledger file | entry | scored to | n | hash ok | IC 12m signal | IC 3m signal | IC momentum | top-20 minus bottom-20 (pp) | hit rate P(beat) |",
         "|---|---|---|---|---|---|---|---|---|---|"]
    f = lambda x: "—" if x is None else f"{x:+.3f}"
    for name, s in rows:
        L.append(f"| {name} | {s.get('entry')} | {s.get('scored_to')} | {s.get('n')} | {s.get('hash_ok')} | "
                 f"{f(s.get('rank_ic_model_12m_signal'))} | {f(s.get('rank_ic_model_3m_signal'))} | {f(s.get('rank_ic_momentum_baseline'))} | "
                 f"{f(s.get('top_decile_minus_bottom_model'))} | {f(s.get('hit_rate_prob_outperform_12m'))} |")
    open(R("reports", "LEDGER_SCORES.md"), "w").write("\n".join(L) + "\n")
    print("\n".join(L))


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("refresh")
    r.add_argument("--prices", action="store_true", help="re-download prices (network)")
    r.add_argument("--draws", type=int, default=1000)
    r.add_argument("--robustness", action="store_true")
    r.add_argument("--freeze", nargs="+", metavar=("LABEL", "NOTE"), help="freeze a ledger file; LABEL '-' for none")
    s = sub.add_parser("score")
    s.add_argument("--days", type=int, required=True)
    s.add_argument("--no-prices", action="store_true")
    a = ap.parse_args()
    refresh(a) if a.cmd == "refresh" else score(a)


if __name__ == "__main__":
    main()
