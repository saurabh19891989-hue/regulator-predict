# LENSKART — Lenskart Solutions Ltd.
*MIDCAP_100 · Consumer Services · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -2.9%**, **12 months -4.3%** (rank 193 / 191 of 200 for 3m / 12m); beta 0.84
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +34.6%): 3 months 43%, 12 months 42%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -10.6% … P90 +1.0%; plausible 12m relative-return range incl. stock-specific noise: -58.8% … +45.3%
- Decomposition (12m): 0.5 × forward event exposure -7.1% (3m -4.2%; half assumed priced) + 0.5 × company-specific catalysts -0.6%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply -3.0% (beta-adjusted) vs a realised market-adjusted move of +35.8% — gap -38.8 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +4.73 | +5.00 | +0.00 | -0.22 | -0.05 | — |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -3.94 | -3.00 | -0.58 | -0.32 | -0.05 | +3.5% |
| Consumer premiumisation (`T_PREMIUMISATION`) | +1 | +3.18 | +3.00 | +0.20 | +0.00 | -0.02 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +3.11 | +3.00 | +0.03 | +0.03 | +0.05 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -2.75 | -2.50 | -0.19 | -0.04 | -0.02 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -2.65 | +0.00 | -2.62 | +0.01 | -0.04 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -2.59 | +0.00 | -0.96 | -1.03 | -0.60 | — |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +2.42 | +1.50 | +0.70 | +0.34 | -0.12 | — |
| US average effective tariff rate (all partners) (`NEW_US_TARIFF_GLOBAL`) | +5 pp effective tariff rate | -2.16 | +0.00 | -1.20 | -0.84 | -0.12 | — |
| USD/JPY exchange rate (`NEW_USDJPY`) | +3% USD/JPY (yen weaker) | +2.12 | +0.00 | +1.92 | +0.09 | +0.11 | — |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -1.39 | +0.00 | +0.00 | -1.44 | +0.05 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -1.26 | -0.30 | -0.68 | -0.30 | +0.02 | -1.1% |
| Brent crude oil price (`F_BRENT`) | +10% Brent | -1.20 | +0.00 | -0.76 | -0.41 | -0.03 | +0.0% |
| India real GDP growth (`F_GDP_IN`) | +1 pp | -1.13 | +0.00 | -1.16 | +0.06 | -0.03 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -6.8% | -6.8% | -6.6 | -0.1 | -0.1 | -0.1 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +9.0% | +4.5% | +8.7 | +0.1 | +0.1 | +0.1 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -3.0% | -3.0% | +0.0 | -3.0 | +0.0 | +0.0 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.25 | -11.7% | -2.9% | -7.5 | -4.3 | -0.1 | +0.2 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -2.8% | -2.8% | -2.5 | -0.2 | -0.1 | -0.0 |
| Disorderly yen carry-trade unwind (Aug-2024-style) after BoJ/MoF action (`EV_YEN_CARRY_UNWIND_RISK`) | risk_scenario | 0.15 | -12.5% | -1.9% | -7.5 | -5.0 | +0.1 | -0.1 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.55 | +3.2% | +1.7% | +1.2 | +1.2 | +0.7 | +0.1 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.25 | -6.6% | -1.7% | -3.0 | -2.3 | -1.2 | -0.2 |
| AI/tech selloff and capex-forecast pause (Oct 2026) (`EV_AI_SELLOFF_OCT26`) | occurred | 1.00 | -1.6% | -1.6% | -1.0 | -0.5 | -0.0 | +0.0 |
| US midterms (3 Nov 2026): Democrats win House and Senate (`EV_US_MIDTERMS_DEM_SWEEP`) | occurred | 1.00 | +1.5% | +1.5% | +1.5 | +0.0 | -0.1 | +0.0 |
| Risk: USD/INR >98 and/or reserves < US$650bn (disorderly rupee, emergency RBI response) (`EV_RUPEE_BREAK_98_RESERVE_STRESS`) | risk_scenario | 0.18 | -7.9% | -1.4% | -7.4 | -0.2 | -0.3 | +0.0 |
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -1.3% | -1.3% | +0.0 | -1.0 | -0.2 | -0.1 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → LENSKART | +7.50% | +3.75% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → LENSKART | -7.50% | -1.88% |
| 1 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → LENSKART | -7.50% | -1.12% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → LENSKART | -2.50% | -1.05% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → LENSKART | -4.50% | -0.81% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_RISK_SENTIMENT → LENSKART | -3.00% | -0.75% |
| 1 | EV_NVDA_NOV17_BEAT ⇒ F_RISK_SENTIMENT → LENSKART | +1.20% | +0.74% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → LENSKART | -2.88% | -0.72% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_FPI_FLOWS → LENSKART | -2.88% | -0.72% |
| 1 | EV_RBI_FEB27_HIKE25 ⇒ F_REPO_IN → LENSKART | -2.50% | -0.68% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_RISK_SENTIMENT → LENSKART | +1.20% | +0.66% |
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_RISK_SENTIMENT → LENSKART | +1.20% | +0.60% |
| 1 | EV_CPI_BREACH_6PCT ⇒ F_REPO_IN → LENSKART | -1.00% | -0.60% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_GDP → F_RISK_SENTIMENT → LENSKART | -2.16% | -0.54% |
| 1 | EV_BUDGET_FY28_LTCG_RELIEF ⇒ F_FPI_FLOWS → LENSKART | +1.50% | +0.52% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_FPI_FLOWS → LENSKART | -1.60 | events | -4.80% |
| 1 | F_REPO_IN → LENSKART | +1.00 | events | -2.50% |
| 1 | F_URBAN_DEMAND → LENSKART | +0.20 | events | +1.00% |
| 1 | F_RISK_SENTIMENT → LENSKART | +0.11 | observed | -0.34% |
| 1 | F_USDINR → LENSKART | -0.37 | observed | +0.11% |
| 2 | P_ANTI_DUMPING_IN → F_CHEM_FEEDSTOCK → LENSKART | +0.40 | events | -0.04% |
| 2 | F_BRENT → F_CHEM_FEEDSTOCK → LENSKART | +0.00 | observed | -0.00% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-11-10 | Anniversary of IPO listing (10 Nov 2025): lock-in expiries of promoter/pre-IPO holders possible; block-deal supply risk (verify RHP) | corporate_action | 0.50 | -3.0% | -1.50% |
| 2027-02-05 | Q3 FY27 results (festive/winter quarter) | results | 0.85 | +0.5% | +0.42% |
| 2027-03 | Store roll-out update toward 10,000 stores (Investing.com Q2 slides) | capex | 0.50 | +1.0% | +0.50% |

## Analyst profile (agent research, sourced)
# LENSKART — Lenskart Solutions Ltd., as of 2026-11-05

*Sources: screener.in pack and Google News headlines (Sep-Nov 2026); bodies not retrieved.*

## Business
Vertically integrated eyewear: design, manufacturing (India), retail stores, online, plus Owndays and other international formats. TTM sales Rs 10,383 cr (+41%); Q2 FY27 sales Rs 2,845 cr (+36%), OP Rs 622 cr (22%), PAT Rs 232 cr (2.3x), international margin 10.6% on 29.5% growth (Entrackr, Multibagg AI, 4-5 Nov). Management cites a path to 10,000 stores and a long-term 25% margin. Market cap Rs 1.26 lakh cr (P/E 161), IPO Nov 2025.

## What moves the stock (ranked)
1. Execution: SSSG, margin expansion and store roll-out.
2. Discount rate and flows (F_REPO_IN -2.5, F_FPI_FLOWS +3, F_RISK_SENTIMENT -3).
3. Urban demand and premiumisation (+5, +3).
4. Pre-IPO selling supply (block deals Sep 21 and Oct 12).
5. Costs and FX: frames/lenses imports and resins, wages (small).

## Transmission examples
- **Brent up** -> polymer lens/frame resin costs -> COGS +0.2% -> margin -20 bp; also CPI -> RBI hold -> urban discretionary demand slows.
- **Rupee weakens** -> imported frames/lenses cost more (-) but international revenue translates higher (+); FPI selling hurts the 18% FII-held stock.
- **GST/consumption stimulus** -> price reductions -> volume up -> operating leverage on fixed store costs.
- **Block deal / lock-in expiry** -> supply -> price falls 3-5% in days (Sep 21: -3%, Oct 12: -5%).

## Current situation
Shares +11% on 5 Nov to an all-time high (Business Standard), five brokerages bullish. Promoters hold 17.5%; FIIs rose from 4% to 18% in two quarters.

## Bull / bear
Bull: SSSG above 15%, margin to 25%, international scale. Bear: 161x P/E with ROE 6%, rate shock, competition, sell-downs by early investors.

## Uncertainties
Mix and import share are estimates; no empirical sensitivities available (short price history).


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.