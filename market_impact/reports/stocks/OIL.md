# OIL — Oil India Ltd.
*MIDCAP_100 · Oil Gas & Consumable Fuels · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +5.3%**, **12 months +8.3%** (rank 11 / 20 of 200 for 3m / 12m); beta 0.81
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +34.4%): 3 months 62%, 12 months 65%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -3.7% … P90 +28.2%; plausible 12m relative-return range incl. stock-specific noise: -24.3% … +75.9%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +5.4 pp (model impact +10.8% beta-adjusted vs realised market-adjusted move -15.0%); forward event exposure +7.9% (3m +4.8%; half assumed priced); company-specific events +0.2%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | +8.80 | +4.50 | +3.44 | +0.77 | +0.09 | — |
| Brent crude oil price (`F_BRENT`) | +10% Brent | +5.58 | +5.00 | +0.58 | +0.04 | -0.03 | +0.0% |
| OPEC+ crude supply decisions (`NEW_OPEC_PLUS_SUPPLY`) | +1 mb/d OPEC+ production (quota/actual) | -3.97 | +0.00 | -3.20 | -0.69 | -0.08 | — |
| Russia-Ukraine war / Western sanctions intensity on Russia (`NEW_RUSSIA_UKRAINE_WAR`) | +1 = escalation (new sanctions round, strikes on energy/port infrastructure); -1 = ceasefire/sanctions relief | +3.40 | +0.00 | +2.43 | +0.87 | +0.09 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | +2.90 | +3.00 | -0.04 | -0.06 | +0.00 | -1.1% |
| China growth / stimulus (`F_CHINA_GDP`) | +1 pp | +2.09 | +0.00 | +1.67 | +0.40 | +0.02 | — |
| Windfall (SAED) tax on domestic crude (`NEW_CRUDE_WINDFALL_TAX_IN`) | +1 = SAED reimposed at ~Rs10,000/tonne | -1.80 | -1.80 | +0.00 | +0.00 | +0.00 | — |
| US growth (`F_US_GDP`) | +1 pp | +1.12 | +0.00 | +1.20 | +0.12 | -0.20 | — |
| US dollar index (`F_DXY`) | +3% DXY | +0.97 | +0.00 | +0.70 | +0.27 | -0.01 | +2.2% |
| Refining margins (GRM / cracks) (`F_REFINING_MARGIN`) | +$2/bbl gross refining margin | +0.90 | +0.90 | +0.00 | +0.00 | +0.00 | +15.4% |
| India real GDP growth (`F_GDP_IN`) | +1 pp | -0.70 | +0.00 | -0.32 | -0.29 | -0.09 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -0.65 | -0.50 | -0.12 | -0.03 | +0.00 | — |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | +0.63 | +0.00 | +0.36 | +0.24 | +0.04 | +3.5% |
| US tariffs on Indian goods (`P_US_TARIFF_INDIA`) | +10 pp average tariff | +0.61 | +0.00 | +0.42 | +0.17 | +0.02 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | +35.8% | +35.8% | +32.9 | +2.7 | +0.3 | -0.1 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.58 | -14.0% | -8.1% | -12.7 | -1.1 | -0.2 | -0.0 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.36 | +20.8% | +7.4% | +18.2 | +2.2 | +0.5 | +0.0 |
| Hormuz effectively closed for >2 weeks (Brent > $150) (`EV_HORMUZ_FULL_CLOSURE`) | risk_scenario | 0.06 | +48.4% | +3.0% | +42.1 | +5.1 | +1.1 | +0.1 |
| US Q3 data: GDP 3.4%, CPI 3.7%, September payrolls only +29k (`EV_US_Q3_DATA_MIXED`) | occurred | 1.00 | +1.4% | +1.4% | +0.0 | +1.4 | +0.2 | -0.2 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | +1.3% | +1.3% | +0.0 | +1.4 | -0.0 | -0.1 |
| Rupee at 95-96/USD and heavy RBI FX defence; reserves fall ~US$55bn from peak (`EV_RUPEE_DEFENCE_RESERVES_26`) | occurred | 1.00 | -1.1% | -1.1% | -1.1 | +0.0 | +0.0 | +0.0 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | +0.8% | +0.8% | +0.0 | +0.5 | +0.4 | -0.1 |
| Gold and silver slump from January 2026 peaks (silver -53%, gold -24%) (`EV_PRECIOUS_METALS_CRASH_2026`) | occurred | 1.00 | +0.8% | +0.8% | +0.0 | +0.5 | +0.4 | -0.1 |
| Risk: USD/INR >98 and/or reserves < US$650bn (disorderly rupee, emergency RBI response) (`EV_RUPEE_BREAK_98_RESERVE_STRESS`) | risk_scenario | 0.22 | +3.4% | +0.7% | +3.4 | +0.0 | +0.0 | +0.0 |
| China Dec CEWC / Mar 2027 NPC delivers large fiscal stimulus and consumption push (`EV_CHINA_NPC_MAR27_BIG_STIMULUS`) | anticipated | 0.35 | +2.1% | +0.7% | +0.0 | +1.6 | +0.5 | +0.0 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | -1.4% | -0.7% | +0.0 | -1.5 | +0.0 | +0.1 |

## Strongest causal chains (1st–4th order)
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → OIL | +24.75% | +24.75% |
| 1 | EV_IRAN_WAR_HORMUZ_OIL ⇒ C_MIDEAST_CONFLICT → OIL | +6.75% | +6.75% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → OIL | +12.50% | +4.46% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → OIL | -7.50% | -4.35% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ C_MIDEAST_CONFLICT → OIL | -4.50% | -2.61% |
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_USDINR → OIL | +2.35% | +2.35% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ C_MIDEAST_CONFLICT → OIL | +5.40% | +1.93% |
| 1 | EV_HORMUZ_FULL_CLOSURE ⇒ F_BRENT → OIL | +30.00% | +1.88% |
| 2 | EV_US_Q3_DATA_MIXED ⇒ F_US_GDP → F_BRENT → OIL | +1.44% | +1.44% |
| 1 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_REFINING_MARGIN → OIL | +1.35% | +1.35% |
| 2 | EV_FPI_RECORD_OUTFLOW_26 ⇒ F_FPI_FLOWS → F_USDINR → OIL | +1.21% | +1.21% |
| 2 | EV_RUSSIA_WAIVER_OCT17 ⇒ C_RUSSIA → F_BRENT → OIL | -1.20% | -1.20% |
| 1 | EV_RUPEE_DEFENCE_RESERVES_26 ⇒ F_USDINR → OIL | -1.11% | -1.11% |
| 1 | EV_RUSSIA_WAIVER_OCT17 ⇒ C_RUSSIA → OIL | +1.00% | +1.00% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_GDP → F_BRENT → OIL | -3.60% | -0.90% |

## Analyst profile (agent research, sourced)
# Oil India (OIL) — market impact profile (as of 2026-11-05)

## Business
Oil India produces crude and gas in Assam and Rajasthan, transports Assam crude by pipeline and owns 69.6% of Numaligarh Refinery. Domestic crude is sold at Brent-linked prices (no subsidy-sharing today), so upstream revenue moves nearly one-for-one with Brent in rupee terms; royalties absorb ~20%.

## What moves the stock (ranked)
1. **Brent (+5.0 per +10%)** — pack t-stat +5.7, the strongest factor.
2. **USD/INR (+3.0 per +3%)** — realisations in INR.
3. **Windfall tax / subsidy-sharing risk (NEW_CRUDE_WINDFALL_TAX_IN -1.8)**.
4. **Mid-East conflict (+4.5)** as a Brent proxy; **Russia assets (+1.0)**.
5. **NRL refining margins (+0.9)**.

## Worked transmission examples
- Hormuz escalation -> Brent +12% (order 1) -> OIL's crude realisation up, quarterly EBITDA +Rs 0.5k cr (order 2) -> government weighs windfall levy or subsidy sharing as OMCs' losses mount (order 3) -> stock gives back some gains; a retail price hike also becomes more likely, normalising OMC margins and reducing pressure for upstream burden-sharing (order 4).
- Brent -9% (4-5 Nov) -> realisation falls -> OIL -4.3% over the month; Q3 FY27 realisation lower than Q2.
- USD/INR up with Brent -> double lift to INR realisation; however if INR strengthens on de-escalation, the stock loses on both.
- Output growth: drilling programme and +11% crude output add volume upside independent of price.

## Current situation
Q1 FY27 was a record (standalone PAT Rs 2,870 cr; consolidated Rs 4,027 cr). The Sep-26 quarter shows OPM 46% with operating profit Rs 5,793 cr, PBT Rs 5,322 cr. The stock is -4.3% in a month as Brent fell, trades at 8.3x earnings and 1.2x book, with a 2.6% yield.

## Upcoming events
Q2 results/dividend, Q3 results (Feb 2027), KG discovery appraisal, any windfall-tax signal.

## Bull / bear
Bull: Brent sticks above $90, output growth, NRL expansion. Bear: Brent falls under $80 after the war settles, windfall tax or sharing, project delays.

*Weights are exposure estimates, not return forecasts. Net profit for the latest quarter was not retrieved and should be refreshed.*


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.