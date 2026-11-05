# LENSKART — Lenskart Solutions Ltd.
*MIDCAP_100 · Consumer Services · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -0.3%**, **12 months -0.5%** (rank 140 / 131 of 200 for 3m / 12m); beta 0.84
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +34.6%): 3 months 49%, 12 months 49%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -3.1% … P90 +1.2%; plausible 12m relative-return range incl. stock-specific noise: -46.5% … +41.9%
- Decomposition (12m): 0.5 × forward event exposure -1.5% (3m -0.8%; half assumed priced; market-priced macro drift removed) + 0.5 × company-specific catalysts +0.9%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply +0.9% (beta-adjusted) vs a realised market-adjusted move of +35.8% — gap -34.9 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## Where the expected return comes from
Market-priced macro drivers (rates, FX, commodities, indices, volatility, flows, growth, inflation) are taken as priced, so what is left is policy, regulatory, sector, theme, geopolitical and company-specific exposure — where 2nd–4th-order effects are most likely to be missed. Percentage points of the expected relative return.
| source | 12m: 1st order | 12m: 2nd–4th order | 12m total | 3m total |
|---|---|---|---|---|
| Policy | +0.05 | -0.06 | -0.01 | -0.04 |
| Regulatory | +0.00 | -0.01 | -0.01 | -0.00 |
| Sector | -0.12 | -0.05 | -0.17 | -0.06 |
| Theme | +0.00 | -0.04 | -0.04 | -0.03 |
| Geopolitics | +0.00 | -0.05 | -0.05 | -0.03 |
| Company catalysts | +0.46 | +0.00 | +0.46 | +0.21 |
| Market-priced macro | +0.00 | +0.00 | +0.00 | +0.00 |
| Beta adjustment | — | — | -0.48 | -0.22 |
| Universe centring | — | — | -0.15 | -0.10 |
| **Expected relative return** | | | **-0.45** | **-0.27** |

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +4.88 | +5.00 | +0.00 | -0.08 | -0.03 | — |
| Consumer premiumisation (`T_PREMIUMISATION`) | +1 | +3.19 | +3.00 | +0.20 | +0.00 | -0.01 | — |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +2.41 | +1.50 | +0.70 | +0.27 | -0.06 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -2.03 | +0.00 | -2.04 | +0.08 | -0.07 | — |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -1.90 | -1.50 | -0.24 | -0.14 | -0.02 | +3.5% |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -1.74 | -1.50 | -0.19 | -0.06 | +0.01 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -1.60 | +0.00 | -0.48 | -0.69 | -0.43 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +1.28 | +1.20 | +0.03 | +0.02 | +0.03 | — |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -1.07 | +0.00 | +0.00 | -1.13 | +0.06 | — |
| US average effective tariff rate (all partners) (`NEW_US_TARIFF_GLOBAL`) | +5 pp effective tariff rate | -1.02 | +0.00 | -0.60 | -0.39 | -0.03 | — |
| USD/JPY exchange rate (`NEW_USDJPY`) | +3% USD/JPY (yen weaker) | +0.97 | +0.00 | +0.89 | +0.04 | +0.04 | — |
| Brent crude oil price (`F_BRENT`) | +10% Brent | -0.89 | +0.00 | -0.55 | -0.33 | -0.02 | +0.0% |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -0.79 | -0.30 | -0.31 | -0.22 | +0.04 | -1.1% |
| Bank credit growth (`F_CREDIT_GROWTH_IN`) | +3 pp | +0.79 | +0.00 | +0.80 | +0.00 | -0.01 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -2.8% | -2.8% | -2.6 | -0.1 | -0.0 | -0.1 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -2.3% | -2.3% | +0.0 | -2.4 | +0.1 | -0.1 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +3.8% | +1.9% | +3.6 | +0.1 | +0.1 | +0.1 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -1.8% | -1.8% | -1.5 | -0.2 | -0.1 | +0.0 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.25 | -5.4% | -1.3% | -3.8 | -1.8 | +0.1 | +0.1 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.55 | +2.0% | +1.1% | +0.6 | +0.8 | +0.5 | +0.1 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.25 | -3.9% | -1.0% | -1.5 | -1.4 | -0.9 | -0.1 |
| Disorderly yen carry-trade unwind (Aug-2024-style) after BoJ/MoF action (`EV_YEN_CARRY_UNWIND_RISK`) | risk_scenario | 0.15 | -5.8% | -0.9% | -3.8 | -2.0 | -0.0 | -0.0 |
| Risk: USD/INR >98 and/or reserves < US$650bn (disorderly rupee, emergency RBI response) (`EV_RUPEE_BREAK_98_RESERVE_STRESS`) | risk_scenario | 0.18 | -4.2% | -0.8% | -3.7 | -0.2 | -0.3 | +0.0 |
| RBI MPC Dec 2026 (~4 Dec): hikes repo another 25 bp to 5.75% (`EV_RBI_DEC26_HIKE25`) | scheduled | 0.42 | -1.8% | -0.7% | -1.5 | -0.2 | -0.1 | +0.0 |
| AI/tech selloff and capex-forecast pause (Oct 2026) (`EV_AI_SELLOFF_OCT26`) | occurred | 1.00 | -0.7% | -0.7% | -0.5 | -0.2 | +0.0 | +0.0 |
| India Q1 FY27 GDP grows 7.8% (31 Aug 2026), beating ~7.3% consensus (`EV_GDP_Q1FY27_7_8`) | occurred | 1.00 | +0.7% | +0.7% | +1.0 | -0.2 | -0.1 | -0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → LENSKART | +3.00% | +1.50% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → LENSKART | -3.75% | -0.94% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → LENSKART | -1.50% | -0.63% |
| 1 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → LENSKART | -3.75% | -0.56% |
| 1 | EV_RBI_FEB27_HIKE25 ⇒ F_REPO_IN → LENSKART | -1.50% | -0.41% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_RISK_SENTIMENT → LENSKART | -1.50% | -0.38% |
| 1 | EV_NVDA_NOV17_BEAT ⇒ F_RISK_SENTIMENT → LENSKART | +0.60% | +0.37% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_RISK_SENTIMENT → LENSKART | +0.60% | +0.33% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → LENSKART | -1.80% | -0.32% |
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_RISK_SENTIMENT → LENSKART | +0.60% | +0.30% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → LENSKART | -1.15% | -0.29% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_FPI_FLOWS → LENSKART | -1.15% | -0.29% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_GDP → F_RISK_SENTIMENT → LENSKART | -1.08% | -0.27% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_REPO_IN → LENSKART | -1.50% | -0.27% |
| 2 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → F_CHEM_FEEDSTOCK → LENSKART | +0.44% | +0.24% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_FPI_FLOWS → LENSKART | -1.60 | events | -1.92% |
| 1 | F_REPO_IN → LENSKART | +1.00 | events | -1.50% |
| 1 | F_URBAN_DEMAND → LENSKART | +0.20 | events | +1.00% |
| 1 | F_RISK_SENTIMENT → LENSKART | +0.11 | observed | -0.17% |
| 1 | F_USDINR → LENSKART | -0.37 | observed | +0.11% |
| 2 | P_ANTI_DUMPING_IN → F_CHEM_FEEDSTOCK → LENSKART | +0.40 | events | -0.04% |
| 2 | F_BRENT → F_CHEM_FEEDSTOCK → LENSKART | +0.00 | observed | -0.00% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
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