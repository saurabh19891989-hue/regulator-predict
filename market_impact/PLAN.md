# Market Impact Graph — Nifty 200 multi-order exposure programme

**Authorised by the user on 2026-11-05** as a programme separate from the Regulatory Predictive Precursor Engine (which
closed with a formal NO-GO on 2026-10-05). The root `CLAUDE.md` out-of-scope rule governs the regulatory programme;
this directory has its own rules in `market_impact/CLAUDE.md`.

## Goal
Build a large, explicit network of how events, commodities, macro factors, policies, geographies, industries and
companies affect each other; use it in two directions:
1. **Event → companies:** start from a recent or upcoming event and trace its 1st, 2nd, 3rd and 4th-order effects onto
   every Nifty 200 company.
2. **Company → drivers:** start from a company and list everything that moves it, ranked by sensitivity × current or
   expected shock, with the causal path for each.
Then produce per-company analyses, event analyses, rankings and scenario-implied expected relative returns
(3-month and 12-month, versus the Nifty 200), each with the effects responsible.

## Universe
Nifty 200 as published by NSE Indices on 2026-11-05 (`data/raw/nifty200.csv`, 200 stocks). Nifty Next 50 members are
the first and deepest tier; Nifty 50 and the 100 midcaps follow.

## Model: Exposure Propagation Network (EPN)
**Nodes** (shared vocabulary in `graph/nodes_seed.json`, extendable):
`COMPANY` (200) · `INDUSTRY` (~45 fine-grained) · `FACTOR` (commodities, FX, rates, macro aggregates — each with a
defined *standard shock*) · `POLICY` (repo rate, duties, GST, PLI, regulation) · `COUNTRY` (trade/geopolitical exposure)
· `THEME` (AI capex, China+1, energy transition…) · `EVENT` (dated, with probabilities).

**Unit convention (everything chains dimensionlessly):** every non-company node has a *standard shock unit* (SSU),
e.g. Brent +10%, USD/INR +3% (rupee weaker), repo rate +25 bp, coal +15%, HRC steel +10%. An edge weight `w` is the
change in the target, in target SSU, per +1 SSU of the source. For a company target the unit is **% change in equity
value**. Each edge carries sign, central weight, low/high range, lag (0–3 m, 3–12 m, >12 m), mechanism text,
confidence and evidence.

**Layering rule (prevents double counting):** events attach to factor/policy/industry/country nodes, not directly to
companies, unless the effect is company-specific. Companies attach to the most proximate driver (e.g. HRC price, not
"China dumping"). The assembler flags parallel paths of different length between the same pair for review.

**Propagation:** for a shock vector on entry nodes, enumerate simple paths of length 1–4 to every company; path
contribution = product of edge weights × per-order uncertainty damping (1.0, 0.8, 0.6, 0.45). Impact is reported by
order (1st/2nd/3rd/4th) and by path, so "which effect affects which company" is always traceable.

**Empirical grounding (no LLM):** 3 years of weekly market-adjusted stock returns regressed on ~30 factor series
(steel, coal, iron ore, Brent, gas, copper, aluminium, gold, silver, USD/INR, CNY, DXY, US 10y, grains, cotton, sugar,
VIX, S&P 500…). Each company←factor edge is compared with its empirical sensitivity: sign conflicts are flagged and
weights are shrunk toward the data where the estimate is significant.

## Expected returns (scenario-implied, relative to Nifty 200)
- Upcoming events: Σ probability × propagated impact within the horizon, with timing weights.
- Recent events (Jun–Nov 2026): model impact compared with the realised market-adjusted move since the event; only
  the unrealised residual counts, at an assumed 50% convergence over 3 months.
- Cross-sectionally demeaned (market-wide effects removed), reported with scenario dispersion and confidence.
- **These are exposure-driven estimates, not validated forecasts.** The previous programme found that LLM forecasts
  did not beat strong baselines out of sample. Every ranking is therefore frozen in a timestamped prospective ledger
  with a momentum and sector-neutral baseline, to be scored at 1, 3 and 12 months.

## Phases
| phase | work | who |
|---|---|---|
| 0 | Plan, schemas, seed node vocabulary; prices, empirical sensitivities, screener.in dossiers, news headlines | Director + code (no LLM) |
| 1a | Backbone graph: factor→factor, factor→industry, industry→industry supply-chain edges | Opus agents |
| 1b | Event catalogue: recent + upcoming, probabilities, entry shocks, 1st–4th order chains (6 themes) | Sonnet agents |
| 1c | Company profiles: 200 companies, ~8 per agent, grouped by industry; Next 50 deepest | Sonnet swarm (~25 agents) |
| 2 | Assemble, validate against empirical betas, propagate, attribute, score, rank | code |
| 3 | Red-team top/bottom 20 and long chains for double counting, stale facts, sign errors | Opus agents |
| 4 | Per-stock and per-event reports, ranking table, dashboard, prospective ledger | Director + code |

## Outputs
`graph/` nodes and edges · `events/catalogue.json` · `companies/<TICKER>.json|md` · `results/` impacts, attributions,
rankings · `reports/` · `ledger/` frozen predictions.
