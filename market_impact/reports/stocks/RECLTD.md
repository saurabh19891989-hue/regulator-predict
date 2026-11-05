# RECLTD — REC Ltd.
*MIDCAP_100 · Financial Services · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +0.5%**, **12 months +1.2%** (rank 45 / 26 of 200 for 3m / 12m); beta 1.35
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +21.0%): 3 months 52%, 12 months 53%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -3.1% … P90 +5.1%; plausible 12m relative-return range incl. stock-specific noise: -25.5% … +29.1%
- Decomposition (12m): 0.5 × forward event exposure +1.7% (3m +1.4%; half assumed priced; market-priced macro drift removed) + 0.5 × company-specific catalysts +1.1%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply -0.4% (beta-adjusted) vs a realised market-adjusted move of -16.7% — gap +16.3 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## Where the expected return comes from
Market-priced macro drivers (rates, FX, commodities, indices, volatility, flows, growth, inflation) are taken as priced, so what is left is policy, regulatory, sector, theme, geopolitical and company-specific exposure — where 2nd–4th-order effects are most likely to be missed. Percentage points of the expected relative return.
| source | 12m: 1st order | 12m: 2nd–4th order | 12m total | 3m total |
|---|---|---|---|---|
| Policy | +1.87 | -0.17 | +1.71 | +0.65 |
| Regulatory | -0.51 | -0.08 | -0.59 | -0.05 |
| Sector | +0.26 | +0.22 | +0.48 | +0.41 |
| Theme | +0.00 | +0.06 | +0.06 | +0.04 |
| Geopolitics | +0.00 | -0.03 | -0.03 | -0.03 |
| Company catalysts | +0.35 | +0.18 | +0.54 | -0.08 |
| Market-priced macro | +0.00 | +0.00 | +0.00 | -0.00 |
| Beta adjustment | — | — | -0.77 | -0.35 |
| Universe centring | — | — | -0.15 | -0.10 |
| **Expected relative return** | | | **+1.25** | **+0.50** |

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Credit cost / NPA cycle (higher = worse) (`F_ASSET_QUALITY_IN`) | +50 bp credit cost | -5.29 | -5.00 | -0.30 | +0.00 | +0.01 | — |
| Power market / DISCOM reform (`P_POWER_REFORM`) | +1 = reform progress | +4.00 | +4.00 | +0.00 | +0.00 | +0.00 | — |
| RBI prudential tightening (risk weights, LCR, provisioning) (`P_RBI_PRUDENTIAL`) | +1 = tightening step | -3.99 | -3.00 | -1.13 | +0.03 | +0.11 | — |
| Central + state government capex (`F_GOVT_CAPEX`) | +10% capex growth | +2.79 | +2.50 | +0.00 | +0.33 | -0.04 | — |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -2.75 | -2.00 | -0.47 | -0.27 | -0.02 | +3.5% |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +2.62 | +2.50 | +0.06 | +0.04 | +0.02 | — |
| Renewable / transmission policy support (`P_RENEWABLE_SUPPORT`) | +1 = stronger support | +2.50 | +2.50 | +0.00 | +0.00 | +0.00 | — |
| Indian corporate credit spreads (`F_CREDIT_SPREADS_IN`) | +50 bp spreads | -2.49 | -2.50 | +0.00 | +0.04 | -0.03 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -2.11 | +0.00 | -0.64 | -0.78 | -0.69 | — |
| Indian electricity demand (`F_POWER_DEMAND_IN`) | +3 pp demand growth | +2.00 | +2.00 | +0.00 | +0.00 | +0.00 | — |
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | +1.98 | +0.00 | +0.80 | +1.35 | -0.17 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -1.85 | -0.80 | -0.41 | -0.63 | -0.00 | — |
| India 10-year G-sec yield (`F_GSEC_10Y_IN`) | +25 bp yield | -1.75 | -1.50 | -0.25 | +0.00 | -0.00 | — |
| Bank credit growth (`F_CREDIT_GROWTH_IN`) | +3 pp | -1.70 | +0.00 | -1.02 | -0.72 | +0.04 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -5.8% | -5.8% | -5.5 | -0.1 | -0.1 | -0.0 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +7.4% | +3.7% | +7.0 | +0.2 | +0.1 | +0.0 |
| India Q1 FY27 GDP grows 7.8% (31 Aug 2026), beating ~7.3% consensus (`EV_GDP_Q1FY27_7_8`) | occurred | 1.00 | +3.1% | +3.1% | +2.5 | +1.0 | -0.2 | -0.2 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -2.8% | -2.8% | -2.8 | +0.0 | +0.0 | +0.0 |
| Cabinet approves Rs14,500 cr VGF for ~92 GWh grid-scale storage (4 Nov) (`EV_BESS_VGF_NOV26`) | occurred | 1.00 | +2.6% | +2.6% | +2.5 | +0.0 | +0.0 | +0.1 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -2.3% | -2.3% | -0.9 | -0.5 | -0.8 | -0.1 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.25 | -8.9% | -2.2% | -5.0 | -3.6 | -0.4 | +0.1 |
| Indian spot power: IEX prices hit Rs20/unit ceiling (19 Sep), Q2 prices up ~46% y/y; El Nino lifts demand (`EV_POWER_SPOT_SPIKE`) | occurred | 1.00 | +2.0% | +2.0% | +2.0 | +0.0 | +0.0 | +0.0 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -1.9% | -1.9% | -1.8 | -0.2 | +0.1 | -0.1 |
| Electricity (Amendment) Bill / distribution parallel licensing and DISCOM privatisation steps (`EV_POWER_DISTRIB_REFORM`) | anticipated | 0.45 | +4.0% | +1.8% | +4.0 | +0.0 | +0.0 | +0.0 |
| RBI expected-credit-loss (ECL) provisioning goes live as scheduled (FY28 start) (`EV_ECL_ROLLOUT_APR27`) | scheduled | 0.90 | -1.7% | -1.5% | -1.6 | -0.1 | +0.0 | -0.0 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.55 | +2.7% | +1.5% | +0.8 | +0.7 | +1.0 | +0.2 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → RECLTD | +6.25% | +3.12% |
| 1 | EV_POWER_DISTRIB_REFORM ⇒ P_POWER_REFORM → RECLTD | +4.00% | +1.80% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → RECLTD | -5.00% | -1.25% |
| 1 | EV_SUMMER27_POWER_SHORTFALL ⇒ F_POWER_DEMAND_IN → RECLTD | +3.00% | +1.20% |
| 1 | EV_NUCLEAR_SHANTI_RULES_FINAL ⇒ P_POWER_REFORM → RECLTD | +2.00% | +1.20% |
| 1 | EV_ECL_ROLLOUT_APR27 ⇒ P_RBI_PRUDENTIAL → RECLTD | -0.90% | -0.81% |
| 2 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_POWER_DEMAND_IN → RECLTD | -1.15% | -0.78% |
| 1 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → RECLTD | -5.00% | -0.75% |
| 1 | EV_ECL_ROLLOUT_APR27 ⇒ F_ASSET_QUALITY_IN → RECLTD | -0.75% | -0.68% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → RECLTD | -3.75% | -0.67% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → RECLTD | -2.40% | -0.60% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_FPI_FLOWS → RECLTD | -2.40% | -0.60% |
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → RECLTD | -1.20% | -0.60% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_RISK_SENTIMENT → RECLTD | -2.00% | -0.50% |
| 1 | EV_NVDA_NOV17_BEAT ⇒ F_RISK_SENTIMENT → RECLTD | +0.80% | +0.50% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_FPI_FLOWS → RECLTD | -1.60 | events | -4.00% |
| 1 | F_POWER_DEMAND_IN → RECLTD | +1.20 | events | +2.40% |
| 1 | F_GSEC_10Y_IN → RECLTD | +1.55 | director_override | -2.33% |
| 1 | P_RENEWABLE_SUPPORT → RECLTD | +0.60 | director_override | +1.50% |
| 1 | F_CREDIT_SPREADS_IN → RECLTD | +0.50 | events | -1.25% |
| 1 | F_CPI_IN → RECLTD | +1.15 | events | -0.92% |
| 1 | F_REPO_IN → RECLTD | +1.00 | events | -0.80% |
| 2 | F_GDP_IN → F_ASSET_QUALITY_IN → RECLTD | +0.50 | events | +0.80% |
| 1 | F_COAL_INTL → RECLTD | +0.70 | director_override | -0.70% |
| 1 | F_GOVT_CAPEX → RECLTD | +0.20 | director_override | +0.50% |
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