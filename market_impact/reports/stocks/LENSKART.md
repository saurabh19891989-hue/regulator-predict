# LENSKART — Lenskart Solutions Ltd.
*MIDCAP_100 · Consumer Services · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -5.0%**, **12 months -9.9%** (rank 192 / 192 of 200 for 3m / 12m); beta 0.84
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +34.6%): 3 months 39%, 12 months 35%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -21.5% … P90 -1.8%; plausible 12m relative-return range incl. stock-specific noise: -53.2% … +22.1%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves -1.5 pp (model impact -3.1% beta-adjusted vs realised market-adjusted move +35.8%); forward event exposure -13.8% (3m -5.6%; half assumed priced); company-specific events -0.6%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +4.69 | +5.00 | +0.00 | -0.22 | -0.09 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -4.36 | +0.00 | -4.06 | -0.18 | -0.12 | — |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -3.98 | -3.00 | -0.58 | -0.33 | -0.07 | +3.5% |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -3.50 | +0.00 | -0.96 | -1.24 | -1.30 | — |
| Consumer premiumisation (`T_PREMIUMISATION`) | +1 | +3.18 | +3.00 | +0.20 | +0.00 | -0.02 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +3.13 | +3.00 | +0.03 | +0.03 | +0.07 | — |
| US equity market (`F_US_EQUITIES`) | +5% S&P 500 | +3.10 | +0.00 | +2.40 | +0.59 | +0.11 | +1.2% |
| US average effective tariff rate (all partners) (`NEW_US_TARIFF_GLOBAL`) | +5 pp effective tariff rate | -2.78 | +0.00 | -1.20 | -1.06 | -0.53 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -2.75 | -2.50 | -0.19 | -0.04 | -0.02 | — |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +2.64 | +1.50 | +0.70 | +0.53 | -0.09 | — |
| USD/JPY exchange rate (`NEW_USDJPY`) | +3% USD/JPY (yen weaker) | +2.38 | +0.00 | +1.92 | +0.24 | +0.22 | — |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -2.28 | +0.00 | +0.00 | -2.24 | -0.05 | — |
| Brent crude oil price (`F_BRENT`) | +10% Brent | -1.94 | +0.00 | -0.79 | -0.91 | -0.24 | +0.0% |
| US dollar index (`F_DXY`) | +3% DXY | -1.88 | +0.00 | -1.39 | -0.33 | -0.16 | +2.2% |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -12.0% | -12.0% | +0.0 | -5.4 | -5.0 | -1.6 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -8.1% | -8.1% | -7.8 | -0.1 | -0.1 | -0.2 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -5.0% | -5.0% | +0.0 | -4.7 | -0.2 | -0.1 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.28 | -17.5% | -4.9% | -12.0 | -5.2 | -0.4 | +0.1 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +9.1% | +4.5% | +8.7 | +0.1 | +0.1 | +0.2 |
| Disorderly yen carry-trade unwind (Aug-2024-style) after BoJ/MoF action (`EV_YEN_CARRY_UNWIND_RISK`) | risk_scenario | 0.18 | -21.8% | -3.9% | -15.0 | -6.5 | -0.1 | -0.2 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.36 | -9.7% | -3.5% | -3.6 | -2.7 | -2.7 | -0.8 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.58 | +5.0% | +2.9% | +1.5 | +1.5 | +1.5 | +0.5 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -2.8% | -2.8% | -2.5 | -0.2 | -0.1 | -0.0 |
| US Q3 data: GDP 3.4%, CPI 3.7%, September payrolls only +29k (`EV_US_Q3_DATA_MIXED`) | occurred | 1.00 | +2.3% | +2.3% | +0.0 | +0.7 | +1.3 | +0.3 |
| US recession (two negative quarters or NBER-style) beginning by mid-2027 (`EV_US_RECESSION_RISK_2027`) | risk_scenario | 0.25 | -9.3% | -2.3% | +0.0 | -8.5 | -0.1 | -0.7 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -2.0% | -2.0% | +0.0 | -1.3 | -0.4 | -0.2 |

## Strongest causal chains (1st–4th order)
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_RECORD_OUTFLOW_26 ⇒ F_FPI_FLOWS → LENSKART | -6.60% | -6.60% |
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → LENSKART | +7.50% | +3.75% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → LENSKART | -12.00% | -3.36% |
| 2 | EV_CPI_REACCEL_SEP26 ⇒ F_CPI_IN → F_REPO_IN → LENSKART | -3.31% | -3.31% |
| 1 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → LENSKART | -15.00% | -2.70% |
| 1 | EV_RBI_OCT26_HIKE25 ⇒ F_REPO_IN → LENSKART | -2.50% | -2.50% |
| 3 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_CPI_IN → F_REPO_IN → LENSKART | -2.21% | -2.21% |
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_FPI_FLOWS → LENSKART | -1.78% | -1.78% |
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_CHEM_FEEDSTOCK → LENSKART | -1.68% | -1.68% |
| 1 | EV_US_MIDTERMS_DEM_SWEEP ⇒ F_FPI_FLOWS → LENSKART | +1.50% | +1.50% |
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ C_MIDEAST_CONFLICT → F_RISK_SENTIMENT → LENSKART | -1.44% | -1.44% |
| 3 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_USDINR → F_FPI_FLOWS → LENSKART | -1.41% | -1.41% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_RISK_SENTIMENT → LENSKART | -3.60% | -1.29% |
| 1 | EV_FPI_RECORD_OUTFLOW_26 ⇒ F_RISK_SENTIMENT → LENSKART | -1.20% | -1.20% |
| 3 | EV_US_Q3_DATA_MIXED ⇒ F_US_GDP → F_US_EQUITIES → F_RISK_SENTIMENT → LENSKART | +1.17% | +1.17% |

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