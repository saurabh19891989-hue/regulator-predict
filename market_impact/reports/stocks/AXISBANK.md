# AXISBANK — Axis Bank Ltd.
*NIFTY_50 · Financial Services · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +0.4%**, **12 months -0.0%** (rank 60 / 104 of 200 for 3m / 12m); beta 1.15
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +19.7%): 3 months 52%, 12 months 52%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -6.3% … P90 +6.1%; plausible 12m relative-return range incl. stock-specific noise: -24.1% … +26.4%
- Decomposition (12m): 0.5 × forward event exposure +0.4% (3m +0.9%; half assumed priced; market-priced macro drift removed) + 0.5 × company-specific catalysts -0.2%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply -6.6% (beta-adjusted) vs a realised market-adjusted move of -5.4% — gap -1.2 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## Where the expected return comes from
Market-priced macro drivers (rates, FX, commodities, indices, volatility, flows, growth, inflation) are taken as priced, so what is left is policy, regulatory, sector, theme, geopolitical and company-specific exposure — where 2nd–4th-order effects are most likely to be missed. Percentage points of the expected relative return.
| source | 12m: 1st order | 12m: 2nd–4th order | 12m total | 3m total |
|---|---|---|---|---|
| Policy | +0.00 | +0.13 | +0.13 | -0.11 |
| Regulatory | -0.43 | -0.06 | -0.48 | -0.05 |
| Sector | -0.69 | +1.65 | +0.96 | +0.73 |
| Theme | +0.00 | +0.14 | +0.14 | +0.09 |
| Geopolitics | +0.19 | -0.05 | +0.13 | +0.11 |
| Company catalysts | -0.12 | +0.00 | -0.12 | +0.00 |
| Market-priced macro | +0.00 | -0.00 | -0.00 | -0.00 |
| Beta adjustment | — | — | -0.66 | -0.30 |
| Universe centring | — | — | -0.15 | -0.10 |
| **Expected relative return** | | | **-0.05** | **+0.37** |

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Credit cost / NPA cycle (higher = worse) (`F_ASSET_QUALITY_IN`) | +50 bp credit cost | -8.55 | -8.50 | +0.00 | -0.04 | -0.01 | — |
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | +4.56 | +0.00 | +3.28 | +1.50 | -0.22 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -4.43 | -3.00 | -0.24 | -0.58 | -0.61 | — |
| India real GDP growth (`F_GDP_IN`) | +1 pp | +4.26 | +2.50 | +2.29 | -0.35 | -0.19 | — |
| RBI prudential tightening (risk weights, LCR, provisioning) (`P_RBI_PRUDENTIAL`) | +1 = tightening step | -4.19 | -2.50 | -1.95 | +0.18 | +0.07 | — |
| Unsecured retail & microfinance stress (higher = worse) (`F_UNSECURED_STRESS`) | +1 pp delinquencies | -3.13 | -2.00 | -0.92 | -0.12 | -0.09 | — |
| Private corporate capex (`F_PRIVATE_CAPEX`) | +10% capex growth | +3.07 | +0.00 | +2.08 | +1.30 | -0.31 | — |
| Monsoon rainfall vs normal (`F_MONSOON`) | +10% above long-period average | +3.07 | +0.00 | +0.99 | +1.41 | +0.67 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +2.67 | +2.50 | +0.15 | -0.01 | +0.02 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -2.32 | +0.00 | -1.46 | -1.04 | +0.17 | — |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -2.32 | -1.50 | -0.51 | -0.28 | -0.02 | +3.5% |
| Bank deposit growth / funding ease (`F_DEPOSIT_GROWTH_IN`) | +3 pp | +2.24 | +2.00 | +0.48 | -0.13 | -0.11 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -2.14 | -1.00 | -1.00 | +0.01 | -0.15 | — |
| Bank credit growth (`F_CREDIT_GROWTH_IN`) | +3 pp | +2.11 | +3.00 | -0.50 | -0.47 | +0.08 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -5.9% | -5.9% | -5.5 | -0.3 | +0.0 | -0.0 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -3.9% | -3.9% | +0.0 | -1.2 | -1.8 | -0.8 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +7.3% | +3.6% | +6.8 | +0.4 | -0.0 | +0.1 |
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -3.5% | -3.5% | -3.0 | -0.2 | -0.2 | -0.1 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -3.3% | -3.3% | -2.8 | -0.3 | -0.1 | -0.0 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.55 | +5.9% | +3.2% | +3.6 | +1.2 | +0.9 | +0.2 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -3.1% | -3.1% | +0.0 | -1.7 | -1.5 | +0.1 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -2.5% | -2.5% | -1.6 | -0.6 | -0.0 | -0.2 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.25 | -9.2% | -2.3% | -5.1 | -2.2 | -1.5 | -0.4 |
| India Q1 FY27 GDP grows 7.8% (31 Aug 2026), beating ~7.3% consensus (`EV_GDP_Q1FY27_7_8`) | occurred | 1.00 | +2.2% | +2.2% | +1.2 | +1.1 | -0.1 | -0.1 |
| RBI expected-credit-loss (ECL) provisioning goes live as scheduled (FY28 start) (`EV_ECL_ROLLOUT_APR27`) | scheduled | 0.90 | -2.4% | -2.2% | -2.5 | +0.1 | +0.0 | -0.0 |
| IMD April 2027 long-range forecast says normal or above-normal monsoon (>=96% LPA) (`EV_MONSOON27_FIRST_FORECAST_NORMAL`) | scheduled | 0.68 | +3.0% | +2.0% | +0.0 | +1.0 | +1.6 | +0.4 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → AXISBANK | +6.25% | +3.12% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ C_MIDEAST_CONFLICT → AXISBANK | +3.00% | +1.65% |
| 1 | EV_ECL_ROLLOUT_APR27 ⇒ F_ASSET_QUALITY_IN → AXISBANK | -1.27% | -1.15% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → AXISBANK | -3.75% | -0.94% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ C_MIDEAST_CONFLICT → AXISBANK | -3.60% | -0.90% |
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → AXISBANK | -1.60% | -0.80% |
| 1 | EV_ECL_ROLLOUT_APR27 ⇒ P_RBI_PRUDENTIAL → AXISBANK | -0.75% | -0.68% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → AXISBANK | -3.75% | -0.67% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → AXISBANK | -2.40% | -0.60% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_FPI_FLOWS → AXISBANK | -2.40% | -0.60% |
| 1 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → AXISBANK | -3.75% | -0.56% |
| 2 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_GDP_IN → AXISBANK | +0.67% | +0.45% |
| 1 | EV_INDIA_STAGFLATION_SCARE ⇒ F_GDP_IN → AXISBANK | -3.75% | -0.45% |
| 1 | EV_BUDGET_FY28_LTCG_RELIEF ⇒ F_FPI_FLOWS → AXISBANK | +1.25% | +0.44% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → AXISBANK | -1.00% | -0.42% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_FPI_FLOWS → AXISBANK | -1.60 | events | -4.00% |
| 1 | F_GSEC_10Y_IN → AXISBANK | +1.55 | director_override | -3.10% |
| 1 | C_MIDEAST_CONFLICT → AXISBANK | +1.00 | events | -3.00% |
| 1 | F_GDP_IN → AXISBANK | +0.50 | events | +1.25% |
| 1 | F_REPO_IN → AXISBANK | +1.00 | events | -1.00% |
| 2 | F_GDP_IN → F_ASSET_QUALITY_IN → AXISBANK | +0.50 | events | +0.68% |
| 2 | F_MONSOON → F_UNSECURED_STRESS → AXISBANK | -1.56 | events | -0.50% |
| 2 | F_REPO_IN → F_CREDIT_GROWTH_IN → AXISBANK | +1.00 | events | -0.35% |
| 2 | F_RURAL_DEMAND → F_ASSET_QUALITY_IN → AXISBANK | -0.25 | events | -0.34% |
| 2 | F_REPO_IN → F_ASSET_QUALITY_IN → AXISBANK | +1.00 | events | -0.34% |
| 1 | F_USDINR → AXISBANK | -0.37 | observed | +0.30% |
| 2 | F_CPI_IN → F_UNSECURED_STRESS → AXISBANK | +1.15 | events | -0.28% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2027-01-16 | Q3 FY27 results (date inferred from prior-year cadence; Q2 reported 2026-10-17) | results | 0.90 | +0.0% | +0.00% |
| 2027-03 | Quarter-end FCNR(B) swap-window maturities and deposit-repricing cycle (NIM sensitivity) | other | 0.50 | -0.5% | -0.25% |

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