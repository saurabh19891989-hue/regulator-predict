# JUBLFOOD — Jubilant Foodworks Ltd.
*MIDCAP_100 · Consumer Services · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -1.2%**, **12 months -2.4%** (rank 136 / 133 of 200 for 3m / 12m); beta 0.98
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +25.7%): 3 months 46%, 12 months 48%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -5.3% … P90 -0.6%; plausible 12m relative-return range incl. stock-specific noise: -33.1% … +30.9%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves -0.4 pp (model impact -0.7% beta-adjusted vs realised market-adjusted move +2.2%); forward event exposure -2.0% (3m -0.8%; half assumed priced); company-specific events +0.2%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +3.72 | +4.00 | +0.00 | -0.21 | -0.07 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -3.27 | +0.00 | -3.07 | -0.09 | -0.11 | — |
| Quick-commerce disruption of retail/FMCG distribution (`T_QUICK_COMMERCE`) | +1 | -3.00 | -3.00 | +0.00 | +0.00 | +0.00 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -2.00 | -1.80 | -0.15 | -0.04 | -0.01 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -1.87 | +0.00 | -0.60 | -0.45 | -0.82 | — |
| Milk / dairy input cost (`F_DAIRY`) | +8% milk procurement price | -1.75 | -1.40 | -0.10 | +0.00 | -0.25 | — |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +1.73 | +0.00 | +1.12 | +0.81 | -0.19 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +1.59 | +1.50 | +0.02 | +0.02 | +0.05 | — |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -1.45 | -0.60 | +0.00 | -0.85 | -0.00 | — |
| India real GDP growth (`F_GDP_IN`) | +1 pp | -1.24 | +0.00 | -1.13 | +0.05 | -0.16 | — |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -1.04 | +0.00 | -0.58 | -0.35 | -0.11 | +3.5% |
| Russia-Ukraine war / Western sanctions intensity on Russia (`NEW_RUSSIA_UKRAINE_WAR`) | +1 = escalation (new sanctions round, strikes on energy/port infrastructure); -1 = ceasefire/sanctions relief | -1.01 | +0.00 | -0.58 | -0.24 | -0.19 | — |
| US dollar index (`F_DXY`) | +3% DXY | -1.01 | +0.00 | -0.71 | -0.18 | -0.12 | +2.2% |
| Brent crude oil price (`F_BRENT`) | +10% Brent | -1.01 | -0.50 | -0.12 | -0.29 | -0.09 | +0.0% |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -5.5% | -5.5% | -2.5 | -0.6 | -1.7 | -0.7 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -4.4% | -4.4% | -0.7 | -3.5 | -0.1 | -0.1 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -3.6% | -3.6% | -3.3 | -0.1 | -0.1 | -0.1 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -2.0% | -2.0% | -1.8 | -0.2 | -0.1 | -0.0 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +4.0% | +2.0% | +3.8 | +0.1 | +0.1 | +0.2 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.36 | -3.8% | -1.4% | -1.2 | -1.0 | -1.1 | -0.4 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.28 | -4.4% | -1.2% | +0.0 | -3.8 | -0.4 | -0.3 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.58 | +2.1% | +1.2% | +0.8 | +0.5 | +0.6 | +0.2 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -1.1% | -1.1% | +0.0 | -1.0 | -0.1 | -0.0 |
| Risk: USD/INR >98 and/or reserves < US$650bn (disorderly rupee, emergency RBI response) (`EV_RUPEE_BREAK_98_RESERVE_STRESS`) | risk_scenario | 0.22 | -4.7% | -1.0% | -4.3 | -0.2 | -0.3 | +0.0 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -1.0% | -1.0% | +0.0 | -0.6 | +0.3 | -0.7 |
| Disorderly yen carry-trade unwind (Aug-2024-style) after BoJ/MoF action (`EV_YEN_CARRY_UNWIND_RISK`) | risk_scenario | 0.18 | -5.7% | -1.0% | +0.0 | -4.7 | -0.5 | -0.5 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → JUBLFOOD | +3.75% | +1.88% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → JUBLFOOD | -1.80% | -0.72% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → JUBLFOOD | -2.24% | -0.63% |
| 2 | EV_PULSES_VEG_SPIKE_WINTER ⇒ F_CPI_IN → F_REPO_IN → JUBLFOOD | -2.07% | -0.52% |
| 2 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → JUBLFOOD | -2.80% | -0.50% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → JUBLFOOD | -2.25% | -0.49% |
| 1 | EV_RBI_FEB27_HIKE25 ⇒ F_REPO_IN → JUBLFOOD | -1.80% | -0.49% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → JUBLFOOD | -1.25% | -0.45% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → JUBLFOOD | +0.75% | +0.44% |
| 1 | EV_CPI_BREACH_6PCT ⇒ F_REPO_IN → JUBLFOOD | -0.72% | -0.43% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → JUBLFOOD | -1.44% | -0.40% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_REPO_IN → JUBLFOOD | -1.80% | -0.40% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_FPI_FLOWS → JUBLFOOD | -1.44% | -0.36% |
| 3 | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → F_GDP_IN → F_REPO_IN → JUBLFOOD | -0.31% | -0.28% |
| 2 | EV_INDIA_RETAIL_FUEL_HIKE ⇒ F_CPI_IN → F_REPO_IN → JUBLFOOD | -0.62% | -0.28% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_FPI_FLOWS → JUBLFOOD | -1.60 | events | -2.40% |
| 1 | F_REPO_IN → JUBLFOOD | +1.00 | events | -1.80% |
| 1 | F_FOOD_INFLATION_IN → JUBLFOOD | +2.00 | events | -1.20% |
| 1 | F_URBAN_DEMAND → JUBLFOOD | +0.20 | events | +0.80% |
| 2 | F_MONSOON → F_DAIRY → JUBLFOOD | -1.56 | events | -0.35% |
| 1 | F_WHEAT → JUBLFOOD | -0.13 | observed | +0.08% |
| 1 | F_USDINR → JUBLFOOD | -0.37 | observed | +0.07% |
| 1 | F_BRENT → JUBLFOOD | +0.00 | observed | -0.00% |

## Analyst profile (agent research, sourced)
# JUBLFOOD — Jubilant FoodWorks Ltd., as of 2026-11-05

*Sources: screener.in pack (through Jun-26), Q2 FY27 business update headlines (7-8 Oct 2026; bodies not retrieved).*

## Business
Master franchisee of Domino's (India, Sri Lanka, Bangladesh, Turkey), Popeyes and Hong's Kitchen. TTM sales Rs 9,838 cr, EBITDA margin ~20%, PAT Rs 450 cr, P/E 78. Q2 FY27 revenue +11.9% to Rs 2,608.7 cr, Domino's India LFL +4%, 3,820 stores (Reuters/CNBC TV18, 7-8 Oct). Stock -24% in 12m, Rs 452.

## What moves the stock (ranked)
1. Domino's India LFL and urban demand (F_URBAN_DEMAND +4).
2. Input costs: cheese/dairy (F_DAIRY -1.4), wheat (-0.6), wages (-1.0), fuel (-0.5).
3. Aggregator and quick-commerce competition (-3).
4. Rates and FPI flows (-1.8, +1.5).
5. Turkey/FX and royalty (small).

## Transmission examples
- **Brent up** -> fuel for delivery and LPG ovens -> costs +0.1% of revenue -> margin dips; CPI rises -> RBI on hold -> consumer wallets squeezed -> LFL drops (3rd-4th).
- **Dairy price spike (+8%)** -> cheese cost -> gross margin -60 bp unless prices raised -> price hikes reduce order volume -> LFL softens (2nd-3rd).
- **Rural/urban stimulus or GST cut** -> discretionary eating out -> LFL +2pp -> operating leverage lifts EBITDA ~5%.
- **Aggregator push into own brands** -> order share loss, higher commissions.

## Current situation
Q1 FY27: PAT Rs 100 cr (+6%), Popeyes LFL 40%+ (Business Standard, 14 Aug). Q2 update on 7 Oct: shares fell 4-6% as LFL disappointed. Motilal Oswal Buy, TP Rs 625 (14 Oct). Promoter 40.3%, DIIs 40%, FIIs 13.3%. Q2 results due ~mid-Nov.

## Bull / bear
Bull: LFL recovery above 6%, Popeyes scaling. Bear: LFL stuck, dairy inflation, price war, 78x P/E de-rates.

## Uncertainties
Cost shares and Turkey exposure are model estimates; Q2 profit not yet reported.

## Additional notes
Store growth (3,820 stores) outpaces LFL, so returns on new stores matter; Popeyes is small but growing fast and diversifies away from pizza. Turkey (roughly 5% of revenue, model knowledge) adds lira-inflation risk not captured by USD/INR. Upcoming: Q2 FY27 results (~10 Nov), Q3 update (~8 Jan 2027).


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.