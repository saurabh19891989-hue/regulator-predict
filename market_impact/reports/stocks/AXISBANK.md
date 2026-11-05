# AXISBANK — Axis Bank Ltd.
*NIFTY_50 · Financial Services · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -3.6%**, **12 months -7.6%** (rank 178 / 183 of 200 for 3m / 12m); beta 1.15
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +19.7%): 3 months 36%, 12 months 38%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -17.4% … P90 +1.3%; plausible 12m relative-return range incl. stock-specific noise: -39.2% … +16.4%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves -1.6 pp (model impact -8.6% beta-adjusted vs realised market-adjusted move -5.4%); forward event exposure -8.0% (3m -3.7%; half assumed priced); company-specific events -1.5%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Credit cost / NPA cycle (higher = worse) (`F_ASSET_QUALITY_IN`) | +50 bp credit cost | -8.55 | -8.50 | +0.00 | -0.04 | -0.01 | — |
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | +5.14 | +0.00 | +3.28 | +2.78 | -0.92 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -4.93 | +0.00 | -2.03 | -2.83 | -0.07 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -4.61 | -3.00 | -0.24 | -0.63 | -0.73 | — |
| RBI prudential tightening (risk weights, LCR, provisioning) (`P_RBI_PRUDENTIAL`) | +1 = tightening step | -4.19 | -2.50 | -1.95 | +0.18 | +0.07 | — |
| Monsoon rainfall vs normal (`F_MONSOON`) | +10% above long-period average | +3.82 | +0.00 | +0.99 | +2.02 | +0.81 | — |
| India real GDP growth (`F_GDP_IN`) | +1 pp | +3.61 | +2.50 | +2.10 | -0.75 | -0.24 | — |
| Private corporate capex (`F_PRIVATE_CAPEX`) | +10% capex growth | +3.35 | +0.00 | +2.08 | +2.37 | -1.10 | — |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -3.13 | +0.00 | +0.00 | -1.37 | -1.77 | — |
| Unsecured retail & microfinance stress (higher = worse) (`F_UNSECURED_STRESS`) | +1 pp delinquencies | -3.12 | -2.00 | -0.92 | -0.12 | -0.08 | — |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +2.79 | +0.00 | +0.00 | +1.22 | +1.57 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +2.73 | +2.50 | +0.15 | -0.01 | +0.08 | — |
| Central + state government capex (`F_GOVT_CAPEX`) | +10% capex growth | +2.48 | +0.00 | +0.90 | +1.73 | -0.15 | — |
| Brent crude oil price (`F_BRENT`) | +10% Brent | -2.42 | +0.00 | -0.85 | -1.03 | -0.54 | +0.0% |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -17.3% | -17.3% | -4.5 | -4.6 | -5.3 | -2.9 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -6.6% | -6.6% | -6.1 | -0.4 | +0.0 | -0.2 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -6.2% | -6.2% | +0.0 | -2.3 | -3.5 | -0.3 |
| RBI expected-credit-loss (ECL) provisioning goes live as scheduled (FY28 start) (`EV_ECL_ROLLOUT_APR27`) | scheduled | 0.62 | -8.0% | -4.9% | -8.2 | +0.3 | +0.0 | -0.0 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -4.8% | -4.8% | +0.0 | -1.2 | -2.5 | -1.0 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.58 | +7.9% | +4.6% | +3.8 | +1.5 | +1.7 | +0.9 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.36 | -12.7% | -4.5% | -5.4 | -2.7 | -2.9 | -1.6 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +7.5% | +3.7% | +6.8 | +0.4 | -0.0 | +0.2 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -3.4% | -3.4% | -2.8 | -0.3 | -0.2 | -0.1 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.28 | -11.3% | -3.2% | -6.0 | -4.5 | -0.9 | +0.0 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -2.9% | -2.9% | +0.0 | -2.7 | -0.1 | -0.1 |
| IMD April 2027 long-range forecast says normal or above-normal monsoon (>=96% LPA) (`EV_MONSOON27_FIRST_FORECAST_NORMAL`) | scheduled | 0.68 | +3.9% | +2.6% | +0.0 | +1.0 | +2.3 | +0.6 |

## Strongest causal chains (1st–4th order)
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_RECORD_OUTFLOW_26 ⇒ F_FPI_FLOWS → AXISBANK | -5.50% | -5.50% |
| 1 | EV_IRAN_WAR_HORMUZ_OIL ⇒ C_MIDEAST_CONFLICT → AXISBANK | -4.50% | -4.50% |
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → AXISBANK | +6.25% | +3.12% |
| 1 | EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26 ⇒ F_GSEC_10Y_IN → AXISBANK | -2.80% | -2.80% |
| 1 | EV_ECL_ROLLOUT_APR27 ⇒ F_ASSET_QUALITY_IN → AXISBANK | -4.25% | -2.63% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ C_MIDEAST_CONFLICT → AXISBANK | +3.00% | +1.74% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → AXISBANK | -6.00% | -1.68% |
| 1 | EV_ECL_ROLLOUT_APR27 ⇒ P_RBI_PRUDENTIAL → AXISBANK | -2.50% | -1.55% |
| 3 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_GDP_IN → F_ASSET_QUALITY_IN → AXISBANK | -1.51% | -1.51% |
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_FPI_FLOWS → AXISBANK | -1.49% | -1.49% |
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_GDP_IN → AXISBANK | -1.49% | -1.49% |
| 1 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → AXISBANK | -7.50% | -1.35% |
| 2 | EV_CPI_REACCEL_SEP26 ⇒ F_CPI_IN → F_REPO_IN → AXISBANK | -1.32% | -1.32% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ C_MIDEAST_CONFLICT → AXISBANK | -3.60% | -1.29% |
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_USDINR → AXISBANK | -1.25% | -1.25% |

## Analyst profile (agent research, sourced)
# AXISBANK - Axis Bank Ltd. (Nifty 50, private bank) - as of 2026-11-05

## Business
Third-largest private bank by network: retail (cards, personal and mortgage loans, Citi's former consumer book), SME and corporate lending, treasury, with subsidiaries in AMC, broking and capital markets. Gross advances Rs13.8 lakh cr (+23% y/y at 30 Sep 2026), deposits +21%. Promoters own 7.86%, so the stock trades on flows: FIIs 38.05% (42.04% in March), DIIs 44.5%.

## What moves the stock, ranked
1. **Funding cost and NIM (repo, deposit growth/mix, FCNR(B))** - NII +12% y/y trailed advances +23%; the October-19 sell-off (-4 to -5%) was about margin and fees, not asset quality.
2. **FPI flows / risk sentiment** - a 4pp FII share loss in six months; market beta ~1.25.
3. **Credit cost (asset quality, unsecured stress)** - +50bp credit cost is about -8.5% on equity value (Rs6,900cr pre-tax vs Rs30,000cr PAT, persistence 0.5).
4. **Credit growth/GDP** - +3pp credit growth ~ +3.
5. **Rates as discount rate** - repo hiked to 5.50% on 2026-10-07 ('calibrated tightening'); 10y yield +25bp ~ -2.
6. **Regulation (RBI prudential, ECL from April 2027)**.
7. **Geopolitics (Middle East, Brent)** - transmission to RBI path and FPI risk appetite.

Empirical pack: no macro factor is significant (|t| < 1.5; cotton -1.02, steel +0.74 are noise); the market-beta of ~1.25 dominates, so the model leans on fundamentals-based weights, flagged low confidence for rates.

## Transmission examples
- **Middle East escalation -> Brent +10% (already +49.5% in 12m) -> INR weaker and CPI +0.3pp -> RBI stays hawkish/hikes again -> Axis loan yields reprice up in weeks while term deposits reprice over 6-12 months -> NIM up 5-10bp (positive) -> but 10y G-sec +25bp cuts the AFS book and the P/E -> net slightly negative; and weaker corporate/SME cash flow 4th-order lifts slippages in 2027.**
- **US yields / DXY up -> FPI outflow from India financials -> Axis (38% FII) falls 2-3% beyond beta -> cost of raising AT1/Tier-2 rises.**
- **Gold-loan and unsecured stress (Reuters 2026-10-21) -> NBFC borrowers' stress -> bank exposure to NBFCs (Axis wholesale book) and cards -> credit cost +10-20bp -> -2 to -4%.**

## Current situation
Q2 FY27 standalone PAT Rs7,003cr (+38%); consolidated PAT per screener Rs7,666cr, flat q/q. Provisions fell, asset quality improved, but fee income and expenses missed. Stock Rs1,275 (P/E 13.2x, P/B ~1.7x).

## Upcoming
Q3 results mid-Jan 2027 (inferred), December MPC, RBI ECL framework April 2027, deposit-repricing and FCNR(B) cycle.

## Bull / bear
Bull: lagging deposit repricing after the hike lifts margin; credit cost drifts lower; cost ratio normalises; FPIs return to quality private banks. Bear: NIM keeps falling, unsecured stress rises, FII share keeps leaking, higher yields de-rate banks.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.