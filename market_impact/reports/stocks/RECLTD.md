# RECLTD — REC Ltd.
*MIDCAP_100 · Financial Services · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +0.1%**, **12 months +0.7%** (rank 95 / 83 of 200 for 3m / 12m); beta 1.35
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +21.0%): 3 months 50%, 12 months 30%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -7.0% … P90 +5.4%; plausible 12m relative-return range incl. stock-specific noise: -21.7% … +22.9%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +1.7 pp (model impact +3.4% beta-adjusted vs realised market-adjusted move -16.7%); forward event exposure -0.9% (3m -0.2%; half assumed priced); company-specific events +1.1%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Credit cost / NPA cycle (higher = worse) (`F_ASSET_QUALITY_IN`) | +50 bp credit cost | -5.29 | -5.00 | -0.30 | +0.00 | +0.01 | — |
| Power market / DISCOM reform (`P_POWER_REFORM`) | +1 = reform progress | +4.00 | +4.00 | +0.00 | +0.00 | +0.00 | — |
| RBI prudential tightening (risk weights, LCR, provisioning) (`P_RBI_PRUDENTIAL`) | +1 = tightening step | -3.99 | -3.00 | -1.13 | +0.03 | +0.11 | — |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -2.81 | -2.00 | -0.47 | -0.29 | -0.06 | +3.5% |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -2.77 | +0.00 | -1.07 | -0.81 | -0.89 | -1.1% |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -2.68 | +0.00 | -0.64 | -0.92 | -1.12 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +2.67 | +2.50 | +0.06 | +0.04 | +0.06 | — |
| Central + state government capex (`F_GOVT_CAPEX`) | +10% capex growth | +2.64 | +2.50 | +0.00 | +0.28 | -0.14 | — |
| Renewable / transmission policy support (`P_RENEWABLE_SUPPORT`) | +1 = stronger support | +2.50 | +2.50 | +0.00 | +0.00 | +0.00 | — |
| Indian corporate credit spreads (`F_CREDIT_SPREADS_IN`) | +50 bp spreads | -2.48 | -2.50 | +0.00 | +0.04 | -0.02 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -2.42 | -0.80 | -0.64 | -0.97 | -0.01 | — |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -2.39 | +0.00 | -0.47 | -0.77 | -1.16 | — |
| US equity market (`F_US_EQUITIES`) | +5% S&P 500 | +2.38 | +0.00 | +1.76 | +0.49 | +0.13 | +1.2% |
| US average effective tariff rate (all partners) (`NEW_US_TARIFF_GLOBAL`) | +5 pp effective tariff rate | -2.11 | +0.00 | -0.80 | -0.79 | -0.52 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -5.9% | -5.9% | -5.5 | -0.1 | -0.1 | -0.1 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +7.5% | +3.7% | +7.0 | +0.2 | +0.1 | +0.2 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -3.0% | -3.0% | -0.9 | -0.7 | -1.2 | -0.1 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -2.8% | -2.8% | -2.8 | +0.0 | +0.0 | -0.0 |
| Cabinet approves Rs14,500 cr VGF for ~92 GWh grid-scale storage (4 Nov) (`EV_BESS_VGF_NOV26`) | occurred | 1.00 | +2.5% | +2.5% | +2.5 | +0.0 | +0.0 | +0.0 |
| India Q1 FY27 GDP grows 7.8% (31 Aug 2026), beating ~7.3% consensus (`EV_GDP_Q1FY27_7_8`) | occurred | 1.00 | +2.5% | +2.5% | +2.5 | +0.8 | -0.6 | -0.3 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.25 | -9.1% | -2.3% | -5.0 | -3.6 | -0.5 | +0.0 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -2.0% | -2.0% | +0.0 | -1.2 | -0.5 | -0.2 |
| Indian spot power: IEX prices hit Rs20/unit ceiling (19 Sep), Q2 prices up ~46% y/y; El Nino lifts demand (`EV_POWER_SPOT_SPIKE`) | occurred | 1.00 | +2.0% | +2.0% | +2.0 | +0.0 | +0.0 | +0.0 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.55 | +3.5% | +1.9% | +0.8 | +0.7 | +1.3 | +0.7 |
| Union Budget 2027-28 capex/railway allocation (infra, railways, defence) (`EV_BUDGET27_CAPEX_RAILWAY`) | scheduled | 0.90 | +2.1% | +1.9% | +2.0 | +0.0 | +0.2 | -0.1 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -1.9% | -1.9% | -1.8 | -0.2 | +0.1 | -0.1 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → RECLTD | +6.25% | +3.12% |
| 1 | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → RECLTD | +2.00% | +1.80% |
| 1 | EV_POWER_DISTRIB_REFORM ⇒ P_POWER_REFORM → RECLTD | +4.00% | +1.80% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → RECLTD | -5.00% | -1.25% |
| 1 | EV_SUMMER27_POWER_SHORTFALL ⇒ F_POWER_DEMAND_IN → RECLTD | +3.00% | +1.20% |
| 1 | EV_NUCLEAR_SHANTI_RULES_FINAL ⇒ P_POWER_REFORM → RECLTD | +2.00% | +1.20% |
| 1 | EV_RBI_GOLD_LOAN_TIGHTEN ⇒ P_RBI_PRUDENTIAL → RECLTD | -3.00% | -0.90% |
| 1 | EV_ECL_ROLLOUT_APR27 ⇒ P_RBI_PRUDENTIAL → RECLTD | -0.90% | -0.81% |
| 2 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_POWER_DEMAND_IN → RECLTD | -1.15% | -0.78% |
| 1 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → RECLTD | -5.00% | -0.75% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_RISK_SENTIMENT → RECLTD | -2.88% | -0.72% |
| 1 | EV_ECL_ROLLOUT_APR27 ⇒ F_ASSET_QUALITY_IN → RECLTD | -0.75% | -0.68% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → RECLTD | -3.75% | -0.67% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → RECLTD | -2.40% | -0.60% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_FPI_FLOWS → RECLTD | -2.40% | -0.60% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_FPI_FLOWS → RECLTD | -1.60 | events | -4.00% |
| 1 | P_RENEWABLE_SUPPORT → RECLTD | +1.50 | events | +3.75% |
| 1 | F_GOVT_CAPEX → RECLTD | +1.00 | events | +2.50% |
| 1 | F_POWER_DEMAND_IN → RECLTD | +1.20 | events | +2.40% |
| 1 | F_GSEC_10Y_IN → RECLTD | +1.55 | director_override | -2.33% |
| 1 | F_CREDIT_SPREADS_IN → RECLTD | +0.50 | events | -1.25% |
| 1 | F_CPI_IN → RECLTD | +1.15 | events | -0.92% |
| 1 | F_REPO_IN → RECLTD | +1.00 | events | -0.80% |
| 2 | F_GDP_IN → F_ASSET_QUALITY_IN → RECLTD | +0.50 | events | +0.80% |
| 1 | F_COAL_INTL → RECLTD | +0.70 | director_override | -0.70% |
| 2 | F_GDP_IN → P_RBI_PRUDENTIAL → RECLTD | +0.50 | events | -0.24% |
| 1 | F_RISK_SENTIMENT → RECLTD | +0.11 | observed | -0.22% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-11 | Record date/payment of second interim dividend Rs3.50 (declared 2026-10-26) | corporate_action | 0.95 | -0.6% | -0.57% |
| 2026-12 | Shareholder/creditor meetings and filings for PFC-REC merger scheme | corporate_action | 0.60 | +1.0% | +0.60% |
| 2027-01-30 | Q3 FY27 results (date approximate; Q2 on 2026-10-26) | results | 0.90 | +0.0% | +0.00% |
| 2027-04 | NCLT sanction / completion of PFC-REC merger (reported target April 2027) | corporate_action | 0.45 | +1.5% | +0.68% |

## Analyst profile (agent research, sourced)
# RECLTD - REC Ltd (as of 2026-11-05)

## Business
REC is a Maharatna government NBFC financing the power chain (generation, transmission, distribution) and, increasingly, renewables and other infrastructure. The loan book is Rs6.17 lakh cr (+Rs26,537cr in Q2), funded by AAA bonds. Q2 FY27 PAT fell 21% to Rs3,478cr as expenses rose to Rs1,090cr (from Rs476cr) (CNBC TV18, Upstox, 2026-10-26). The stock trades at P/E 5.2, P/B 0.82, dividend yield 6.2%. PFC holds a controlling stake (~52.6%, model) and the boards agreed to merge REC into PFC.

## What moves the stock (ranked)
1. **Merger terms (PFC link +0.7 per +1% PFC move)** - 88 PFC shares per 100 REC; RBI conditional NoC 2026-10-15; NCLT and shareholder approvals pending, reported target April 2027.
2. **Asset quality (-5.0 per +50bp)** and **funding spreads (-2.5 per +50bp)**, G-sec (-1.5), repo (-0.8).
3. **Power-sector policy:** reform (+4.0), demand (+2.0), government capex (+2.5), renewables support (+2.5).
4. **Regulation (-3.0):** NBFC scale-based rules and merger scrutiny.
5. **Flows/risk:** FPI (+2.5), VIX (-2.0), coal (-1.0).
Pack: Fed funds +3.71 (t 2.0) has no mechanism; ignored. Coal -3.61 (t -1.9) shrunk to -1.0.

## Transmission examples
- **Thermal coal price up -> generation costs and discom working capital stressed -> discoms delay repayments (stage-2/3 risk) -> REC provisions up (Q2 expenses already Rs1,090cr) -> PAT down -> dividend capacity down; 4th order: government equity support/recapitalisation questions.**
- **Repo hike (2026-10-07) -> AAA yields +10bp -> REC bond refinancing costs up (20-25% of Rs5.2 lakh cr per year) -> NIM -3bp -> PAT -3%; plus lower infra loan demand.**
- **Merger approvals -> REC converts to PFC at 0.88x -> REC price tracks PFC (link 0.7) -> arbitrage narrows -> a potential re-rating from P/B 0.82 to PFC's multiple; delays leave a discount.**
- **Middle East escalation -> Brent up -> USD/INR weaker -> FPI outflow from PSU financials (beta 1.5) -> multiple down even though NII is rupee-based.**

## Current situation
52-week low on 2026-09-29, bounce after the RBI NoC (2026-10-15/17). Interim dividend Rs3.50 declared 2026-10-26. New transmission SPVs (Bikaner, Mirzapur) incorporated 2026-10-06.

## Upcoming events
Merger steps (Dec 2026 to Apr 2027), Q3 results (~2027-01-30), RBI MPC (2026-12-04).

## Bull and bear
**Bull:** cheap on earnings and book, high dividend, merger narrative, power capex.
**Bear:** dilution/terms, profit decline, discom credit risk, funding costs.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.