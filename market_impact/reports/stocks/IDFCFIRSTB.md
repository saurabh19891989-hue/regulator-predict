# IDFCFIRSTB — IDFC First Bank Ltd.
*MIDCAP_100 · Financial Services · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -5.5%**, **12 months -10.6%** (rank 196 / 194 of 200 for 3m / 12m); beta 1.09
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +21.1%): 3 months 30%, 12 months 35%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -28.5% … P90 +3.5%; plausible 12m relative-return range incl. stock-specific noise: -34.7% … +15.8%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves -2.9 pp (model impact -5.8% beta-adjusted vs realised market-adjusted move +2.7%); forward event exposure -13.5% (3m -6.0%; half assumed priced); company-specific events +0.5%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Credit cost / NPA cycle (higher = worse) (`F_ASSET_QUALITY_IN`) | +50 bp credit cost | -14.04 | -14.00 | +0.00 | -0.03 | -0.00 | — |
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | +8.13 | +0.00 | +5.28 | +4.13 | -1.28 | — |
| Unsecured retail & microfinance stress (higher = worse) (`F_UNSECURED_STRESS`) | +1 pp delinquencies | -6.58 | -5.00 | -1.32 | -0.16 | -0.11 | — |
| Monsoon rainfall vs normal (`F_MONSOON`) | +10% above long-period average | +5.98 | +0.00 | +1.73 | +3.08 | +1.17 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -5.61 | +0.00 | -2.69 | -3.11 | +0.19 | — |
| India real GDP growth (`F_GDP_IN`) | +1 pp | +5.42 | +3.50 | +3.12 | -1.03 | -0.17 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -4.58 | +0.00 | -0.96 | -1.41 | -2.21 | — |
| Private corporate capex (`F_PRIVATE_CAPEX`) | +10% capex growth | +4.56 | +0.00 | +2.64 | +3.40 | -1.48 | — |
| RBI prudential tightening (risk weights, LCR, provisioning) (`P_RBI_PRUDENTIAL`) | +1 = tightening step | -4.37 | -2.50 | -2.51 | +0.52 | +0.11 | — |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -4.11 | -3.00 | -0.59 | -0.38 | -0.14 | +3.5% |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -3.90 | +0.00 | +0.00 | -1.88 | -2.02 | — |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +3.89 | +0.00 | +0.00 | +1.84 | +2.05 | — |
| Indian wage / employee-cost inflation (`F_WAGES_IN`) | +2 pp | +3.58 | +0.00 | +0.80 | +1.60 | +1.18 | — |
| Central + state government capex (`F_GOVT_CAPEX`) | +10% capex growth | +3.58 | +0.00 | +1.26 | +2.50 | -0.19 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -19.0% | -19.0% | +0.0 | -6.1 | -8.7 | -4.2 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -8.6% | -8.6% | -7.8 | -0.2 | -0.2 | -0.4 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -7.5% | -7.5% | +0.0 | -2.2 | -3.9 | -1.5 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -7.2% | -7.2% | +0.0 | -3.1 | -4.0 | -0.1 |
| RBI expected-credit-loss (ECL) provisioning goes live as scheduled (FY28 start) (`EV_ECL_ROLLOUT_APR27`) | scheduled | 0.62 | -9.9% | -6.2% | -10.8 | +0.8 | +0.0 | -0.0 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.28 | -18.7% | -5.2% | -12.0 | -5.2 | -1.0 | -0.4 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.36 | -13.5% | -4.8% | -3.6 | -3.1 | -4.6 | -2.3 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +9.6% | +4.8% | +8.7 | +0.3 | +0.2 | +0.4 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.58 | +7.2% | +4.2% | +1.5 | +1.7 | +2.7 | +1.3 |
| IMD April 2027 long-range forecast says normal or above-normal monsoon (>=96% LPA) (`EV_MONSOON27_FIRST_FORECAST_NORMAL`) | scheduled | 0.68 | +6.0% | +4.1% | +0.0 | +1.7 | +3.5 | +0.8 |
| Disorderly yen carry-trade unwind (Aug-2024-style) after BoJ/MoF action (`EV_YEN_CARRY_UNWIND_RISK`) | risk_scenario | 0.18 | -22.6% | -4.1% | -15.0 | -6.5 | -0.5 | -0.5 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -3.3% | -3.3% | -2.7 | -0.2 | -0.2 | -0.2 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_ECL_ROLLOUT_APR27 ⇒ F_ASSET_QUALITY_IN → IDFCFIRSTB | -7.00% | -4.34% |
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → IDFCFIRSTB | +7.50% | +3.75% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → IDFCFIRSTB | -12.00% | -3.36% |
| 1 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → IDFCFIRSTB | -15.00% | -2.70% |
| 1 | EV_ECL_ROLLOUT_APR27 ⇒ P_RBI_PRUDENTIAL → IDFCFIRSTB | -2.50% | -1.55% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_RISK_SENTIMENT → IDFCFIRSTB | -3.60% | -1.29% |
| 3 | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → F_GDP_IN → F_ASSET_QUALITY_IN → IDFCFIRSTB | +1.21% | +1.09% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_RISK_SENTIMENT → IDFCFIRSTB | -4.32% | -1.08% |
| 1 | EV_BANKING_LIQUIDITY_DEFICIT_MAR27 ⇒ F_LIQUIDITY_IN → IDFCFIRSTB | -1.80% | -1.08% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → IDFCFIRSTB | -4.50% | -0.99% |
| 2 | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → F_GDP_IN → IDFCFIRSTB | +1.01% | +0.91% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_RISK_SENTIMENT → IDFCFIRSTB | +1.50% | +0.87% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → IDFCFIRSTB | -2.88% | -0.81% |
| 1 | EV_ECL_ROLLOUT_APR27 ⇒ F_CREDIT_GROWTH_IN → IDFCFIRSTB | -1.25% | -0.78% |
| 3 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_GDP_IN → F_ASSET_QUALITY_IN → IDFCFIRSTB | +1.12% | +0.76% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_FPI_FLOWS → IDFCFIRSTB | -1.60 | events | -4.80% |
| 1 | F_GSEC_10Y_IN → IDFCFIRSTB | +1.70 | events | -2.55% |
| 1 | F_GDP_IN → IDFCFIRSTB | +0.50 | events | +1.75% |
| 2 | F_MONSOON → F_UNSECURED_STRESS → IDFCFIRSTB | -1.56 | events | -1.25% |
| 2 | F_GDP_IN → F_ASSET_QUALITY_IN → IDFCFIRSTB | +0.50 | events | +1.12% |
| 1 | F_LIQUIDITY_IN → IDFCFIRSTB | -0.90 | events | -1.08% |
| 1 | F_REPO_IN → IDFCFIRSTB | +1.00 | events | -1.00% |
| 2 | F_CPI_IN → F_UNSECURED_STRESS → IDFCFIRSTB | +1.15 | events | -0.69% |
| 2 | F_RURAL_DEMAND → F_ASSET_QUALITY_IN → IDFCFIRSTB | -0.25 | events | -0.56% |
| 2 | F_REPO_IN → F_ASSET_QUALITY_IN → IDFCFIRSTB | +1.00 | events | -0.56% |
| 3 | F_MONSOON → F_UNSECURED_STRESS → F_ASSET_QUALITY_IN → IDFCFIRSTB | -1.56 | events | -0.52% |
| 1 | T_FORMALISATION → IDFCFIRSTB | +0.30 | events | +0.45% |

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