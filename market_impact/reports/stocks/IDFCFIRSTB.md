# IDFCFIRSTB — IDFC First Bank Ltd.
*MIDCAP_100 · Financial Services · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +0.6%**, **12 months +0.9%** (rank 30 / 35 of 200 for 3m / 12m); beta 1.09
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +21.1%): 3 months 52%, 12 months 51%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -7.1% … P90 +8.9%; plausible 12m relative-return range incl. stock-specific noise: -26.7% … +28.2%
- Decomposition (12m): 0.5 × forward event exposure +1.7% (3m +1.5%; half assumed priced; market-priced macro drift removed) + 0.5 × company-specific catalysts +0.5%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply -5.3% (beta-adjusted) vs a realised market-adjusted move of +2.7% — gap -8.0 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## Where the expected return comes from
Market-priced macro drivers (rates, FX, commodities, indices, volatility, flows, growth, inflation) are taken as priced, so what is left is policy, regulatory, sector, theme, geopolitical and company-specific exposure — where 2nd–4th-order effects are most likely to be missed. Percentage points of the expected relative return.
| source | 12m: 1st order | 12m: 2nd–4th order | 12m total | 3m total |
|---|---|---|---|---|
| Policy | +0.00 | +0.35 | +0.35 | -0.04 |
| Regulatory | -0.43 | -0.06 | -0.49 | -0.06 |
| Sector | -1.11 | +2.61 | +1.50 | +1.09 |
| Theme | +0.00 | +0.18 | +0.18 | +0.11 |
| Geopolitics | +0.00 | -0.09 | -0.09 | -0.08 |
| Company catalysts | +0.25 | +0.00 | +0.25 | +0.00 |
| Market-priced macro | +0.00 | +0.00 | +0.00 | -0.00 |
| Beta adjustment | — | — | -0.63 | -0.28 |
| Universe centring | — | — | -0.15 | -0.10 |
| **Expected relative return** | | | **+0.93** | **+0.65** |

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Credit cost / NPA cycle (higher = worse) (`F_ASSET_QUALITY_IN`) | +50 bp credit cost | -14.04 | -14.00 | +0.00 | -0.03 | -0.00 | — |
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | +7.07 | +0.00 | +5.28 | +2.18 | -0.38 | — |
| Unsecured retail & microfinance stress (higher = worse) (`F_UNSECURED_STRESS`) | +1 pp delinquencies | -6.60 | -5.00 | -1.32 | -0.16 | -0.12 | — |
| India real GDP growth (`F_GDP_IN`) | +1 pp | +6.00 | +3.50 | +3.31 | -0.62 | -0.20 | — |
| Monsoon rainfall vs normal (`F_MONSOON`) | +10% above long-period average | +4.84 | +0.00 | +1.73 | +2.15 | +0.96 | — |
| RBI prudential tightening (risk weights, LCR, provisioning) (`P_RBI_PRUDENTIAL`) | +1 = tightening step | -4.37 | -2.50 | -2.51 | +0.52 | +0.11 | — |
| Private corporate capex (`F_PRIVATE_CAPEX`) | +10% capex growth | +3.97 | +0.00 | +2.64 | +1.82 | -0.49 | — |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -3.96 | -3.00 | -0.59 | -0.31 | -0.07 | +3.5% |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +3.18 | +3.00 | +0.11 | -0.02 | +0.09 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -3.14 | +0.00 | -0.96 | -1.17 | -1.01 | — |
| Indian wage / employee-cost inflation (`F_WAGES_IN`) | +2 pp | +3.01 | +0.00 | +0.80 | +1.49 | +0.72 | — |
| Central + state government capex (`F_GOVT_CAPEX`) | +10% capex growth | +2.84 | +0.00 | +1.26 | +1.51 | +0.06 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -2.68 | +0.00 | -2.12 | -0.89 | +0.32 | — |
| US average effective tariff rate (all partners) (`NEW_US_TARIFF_GLOBAL`) | +5 pp effective tariff rate | -2.60 | +0.00 | -1.20 | -1.05 | -0.35 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -7.0% | -7.0% | -6.6 | -0.2 | +0.0 | -0.2 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -6.1% | -6.1% | +0.0 | -2.2 | -2.7 | -1.2 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +9.2% | +4.6% | +8.7 | +0.3 | -0.1 | +0.2 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -3.7% | -3.7% | +0.0 | -2.4 | -1.5 | +0.2 |
| IMD April 2027 long-range forecast says normal or above-normal monsoon (>=96% LPA) (`EV_MONSOON27_FIRST_FORECAST_NORMAL`) | scheduled | 0.68 | +4.7% | +3.2% | +0.0 | +1.7 | +2.5 | +0.5 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -3.1% | -3.1% | -2.7 | -0.2 | -0.1 | -0.0 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.25 | -12.2% | -3.1% | -7.5 | -4.4 | -0.5 | +0.1 |
| India Q1 FY27 GDP grows 7.8% (31 Aug 2026), beating ~7.3% consensus (`EV_GDP_Q1FY27_7_8`) | occurred | 1.00 | +3.0% | +3.0% | +1.8 | +1.7 | -0.2 | -0.1 |
| RBI expected-credit-loss (ECL) provisioning goes live as scheduled (FY28 start) (`EV_ECL_ROLLOUT_APR27`) | scheduled | 0.90 | -3.0% | -2.7% | -3.2 | +0.2 | +0.0 | -0.0 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -2.4% | -2.4% | -1.4 | -0.8 | +0.1 | -0.2 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.55 | +4.0% | +2.2% | +1.2 | +1.4 | +1.1 | +0.3 |
| North-east monsoon 2026 normal or above-normal (relief for southern reservoirs) (`EV_NEMONSOON26_NORMAL_UP`) | anticipated | 0.85 | +2.5% | +2.2% | +0.0 | +0.9 | +1.4 | +0.3 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → IDFCFIRSTB | +7.50% | +3.75% |
| 1 | EV_ECL_ROLLOUT_APR27 ⇒ F_ASSET_QUALITY_IN → IDFCFIRSTB | -2.10% | -1.89% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → IDFCFIRSTB | -7.50% | -1.88% |
| 1 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → IDFCFIRSTB | -7.50% | -1.12% |
| 1 | EV_BANKING_LIQUIDITY_DEFICIT_MAR27 ⇒ F_LIQUIDITY_IN → IDFCFIRSTB | -1.80% | -1.08% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → IDFCFIRSTB | -4.50% | -0.81% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_RISK_SENTIMENT → IDFCFIRSTB | -3.00% | -0.75% |
| 1 | EV_NVDA_NOV17_BEAT ⇒ F_RISK_SENTIMENT → IDFCFIRSTB | +1.20% | +0.74% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → IDFCFIRSTB | -2.88% | -0.72% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_FPI_FLOWS → IDFCFIRSTB | -2.88% | -0.72% |
| 1 | EV_ECL_ROLLOUT_APR27 ⇒ P_RBI_PRUDENTIAL → IDFCFIRSTB | -0.75% | -0.68% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_RISK_SENTIMENT → IDFCFIRSTB | +1.20% | +0.66% |
| 2 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_GDP_IN → IDFCFIRSTB | +0.93% | +0.63% |
| 1 | EV_INDIA_STAGFLATION_SCARE ⇒ F_GDP_IN → IDFCFIRSTB | -5.25% | -0.63% |
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → IDFCFIRSTB | -1.20% | -0.60% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_FPI_FLOWS → IDFCFIRSTB | -1.60 | events | -4.80% |
| 1 | F_GSEC_10Y_IN → IDFCFIRSTB | +1.55 | director_override | -2.33% |
| 1 | F_GDP_IN → IDFCFIRSTB | +0.50 | events | +1.75% |
| 2 | F_MONSOON → F_UNSECURED_STRESS → IDFCFIRSTB | -1.56 | events | -1.25% |
| 2 | F_GDP_IN → F_ASSET_QUALITY_IN → IDFCFIRSTB | +0.50 | events | +1.12% |
| 1 | F_LIQUIDITY_IN → IDFCFIRSTB | -0.90 | events | -1.08% |
| 1 | F_REPO_IN → IDFCFIRSTB | +1.00 | events | -1.00% |
| 2 | F_CPI_IN → F_UNSECURED_STRESS → IDFCFIRSTB | +1.15 | events | -0.69% |
| 2 | F_RURAL_DEMAND → F_ASSET_QUALITY_IN → IDFCFIRSTB | -0.25 | events | -0.56% |
| 2 | F_REPO_IN → F_ASSET_QUALITY_IN → IDFCFIRSTB | +1.00 | events | -0.56% |
| 1 | T_FORMALISATION → IDFCFIRSTB | +0.30 | events | +0.45% |
| 1 | F_RISK_SENTIMENT → IDFCFIRSTB | +0.11 | observed | -0.34% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2027-01-24 | Q3 FY27 results (estimated from Q2 on 2026-10-24); watch credit cost, NIM, opex | results | 0.95 | +0.0% | +0.00% |
| 2027-03 | FY27 year-end: management target of sustained ~1% RoA path / credit-cost normalisation | guidance | 0.50 | +1.0% | +0.50% |

## Analyst profile (agent research, sourced)
# IDFCFIRSTB - IDFC FIRST Bank Ltd. (as of 2026-11-05)

## Business
IDFC FIRST Bank is a mid-sized, widely held private bank with a retail-heavy loan book (vehicle and consumer finance, credit cards, MSME, micro-loans, home loans) and a smaller wholesale book inherited from IDFC Bank. It has no promoter: FIIs hold 36.7%, DIIs 25.4%, the government 7.8% and the public ~30% (Sep 2026). Loan assets grew ~30% in Q2 FY27. Net profit was Rs1,045cr in Q2 (Rs352cr a year earlier) after a thin FY26 (Rs1,636cr, Mar-2026 qtr only Rs319cr), so ROE is only ~4% on screener's numbers.

## What moves the stock (ranked)
1. **Credit cost / asset quality (-14 per +50bp)**: operating profit is thin versus a fast-growing book, so every 10bp of credit cost is ~7% of PAT. This is by far the largest sensitivity in the batch.
2. **Unsecured and MFI stress (-5 per +1pp delinquencies)**: cards, personal, consumer and micro-loans are over a quarter of loans.
3. **GDP / credit growth (+3.5 / +2.5)** and **deposits/funding (+2.5)**: growth with operating leverage and cheaper CASA drives the RoE path.
4. **FPI flows and risk-off (+3.0 / -3.0)**: a high-beta (1.17) FII-owned stock.
5. **Rates**: the hike (repo 5.50%) helps asset yield but borrowers and deposit costs offset; net -1.0 (low confidence). G-sec -1.5 via discount rate.
6. **Prudential regulation (-2.5)**.

## Transmission examples
- **Middle East escalation -> Brent ~$105 -> INR ~97 -> CPI up -> RBI hikes again**: consumer budgets tighten (fuel, food) -> 2nd order: vehicle-loan and micro-loan delinquencies rise 0.5-1pp within 2-3 quarters (-3 to -5) -> 3rd order: provisions eat the thin RoE; FIIs cut high-beta financials (-2) -> 4th order: management must raise deposit rates to hold growth, NIM compresses further.
- **RBI easing prudential norms or lower deposit rates -> deposit-cost relief** -> CoF -10bp -> NIM +6bp -> PAT +8% (positive, +2 to +3).
- **Good monsoon -> rural income -> vehicle/MFI collections** -> lower rural credit cost -> credit-cost -10bp = +7% PAT.
- **UPI/GST formalisation -> better credit data -> lower acquisition cost** for MSME and consumer segments.

## Current situation
Q2 FY27 profit Rs1,045cr (+196% YoY; down ~3% QoQ from Q1's record Rs1,075cr per Moneycontrol/ET 2026-10-24). Stock is -10% in 3 months and flagged oversold on 2026-10-26 even as it is +9% in 6 months; a 30% rally into early October preceded this. NII and loan growth are strong; the debate is whether credit cost has genuinely turned.

## Upcoming
Q3 FY27 results ~late Jan 2027 (estimated); RBI MPC December; potential capital raise; deposit-cost trend; microfinance collections.

## Bull case
Credit cost normalises, opex ratio falls with scale, deposit cost advantage returns - RoA climbs toward 1.2% and the stock re-rates to ~2x P/B (+40%).
## Bear case
Unsecured/MFI stress returns with higher rates and an INR/oil shock; RoE stays <5%; equity raise at a discount. Downside -25% or more given thin earnings.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.