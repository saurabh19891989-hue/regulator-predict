# OIL — Oil India Ltd.
*MIDCAP_100 · Oil Gas & Consumable Fuels · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +3.1%**, **12 months +4.7%** (rank 25 / 32 of 200 for 3m / 12m); beta 0.81
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +34.4%): 3 months 57%, 12 months 40%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -5.6% … P90 +16.5%; plausible 12m relative-return range incl. stock-specific noise: -58.5% … +65.0%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +4.1 pp (model impact +8.2% beta-adjusted vs realised market-adjusted move -15.0%); forward event exposure +3.2% (3m +2.0%; half assumed priced); company-specific events +0.2%

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
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.55 | -12.6% | -6.9% | -11.5 | -0.9 | -0.1 | -0.0 |
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | +5.2% | +5.2% | +5.0 | +0.1 | +0.1 | +0.0 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.25 | +19.0% | +4.8% | +16.7 | +1.9 | +0.4 | +0.0 |
| Hormuz effectively closed for >2 weeks (Brent > $150) (`EV_HORMUZ_FULL_CLOSURE`) | risk_scenario | 0.05 | +40.1% | +2.0% | +34.6 | +4.3 | +1.0 | +0.1 |
| US Q3 data: GDP 3.4%, CPI 3.7%, September payrolls only +29k (`EV_US_Q3_DATA_MIXED`) | occurred | 1.00 | +1.4% | +1.4% | +0.0 | +1.4 | +0.2 | -0.2 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | +1.1% | +1.1% | +0.0 | +1.2 | -0.0 | -0.0 |
| Rupee at 95-96/USD and heavy RBI FX defence; reserves fall ~US$55bn from peak (`EV_RUPEE_DEFENCE_RESERVES_26`) | occurred | 1.00 | -1.1% | -1.1% | -1.1 | +0.0 | +0.0 | +0.0 |
| OPEC+ 29 Nov meeting: 2027 quotas raised (market-share / post-war normalisation) (`EV_OPEC_NOV29_RAISE`) | scheduled | 0.20 | -3.9% | -0.8% | -3.5 | -0.4 | -0.0 | +0.0 |
| China Dec CEWC / Mar 2027 NPC delivers large fiscal stimulus and consumption push (`EV_CHINA_NPC_MAR27_BIG_STIMULUS`) | anticipated | 0.35 | +2.1% | +0.7% | +0.0 | +1.6 | +0.5 | +0.0 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | -1.4% | -0.7% | +0.0 | -1.5 | +0.0 | +0.1 |
| Waiver lapses and US imposes secondary tariff (up to 100%) or sanctions on Indian refiners buying Russian oil (`EV_RUSSIA_TARIFF_ENFORCED`) | risk_scenario | 0.15 | +4.8% | +0.7% | +3.0 | +1.3 | +0.5 | +0.0 |
| US recession (two negative quarters or NBER-style) beginning by mid-2027 (`EV_US_RECESSION_RISK_2027`) | risk_scenario | 0.25 | -2.8% | -0.7% | +0.0 | -3.5 | +0.6 | +0.1 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → OIL | -6.50% | -3.58% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → OIL | +11.00% | +2.75% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ C_MIDEAST_CONFLICT → OIL | -4.50% | -2.48% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ C_MIDEAST_CONFLICT → OIL | +5.40% | +1.35% |
| 1 | EV_HORMUZ_FULL_CLOSURE ⇒ F_BRENT → OIL | +22.50% | +1.12% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_GDP → F_BRENT → OIL | -3.60% | -0.90% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_USDINR → OIL | +3.90% | +0.70% |
| 1 | EV_OPEC_NOV29_RAISE ⇒ F_BRENT → OIL | -3.50% | -0.70% |
| 2 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → F_USDINR → OIL | -1.38% | -0.69% |
| 1 | EV_RUSSIA_TARIFF_ENFORCED ⇒ F_BRENT → OIL | +4.00% | +0.60% |
| 1 | EV_HORMUZ_FULL_CLOSURE ⇒ C_MIDEAST_CONFLICT → OIL | +11.25% | +0.56% |
| 2 | EV_CHINA_NPC_MAR27_BIG_STIMULUS ⇒ F_CHINA_GDP → F_BRENT → OIL | +1.60% | +0.56% |
| 2 | EV_RUSSIAN_CRUDE_CUT_TRADE_DEAL ⇒ C_RUSSIA → F_BRENT → OIL | +1.20% | +0.36% |
| 2 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → F_USDINR → OIL | -0.62% | -0.34% |
| 1 | EV_RUSSIAN_CRUDE_CUT_TRADE_DEAL ⇒ C_RUSSIA → OIL | -1.00% | -0.30% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | C_MIDEAST_CONFLICT → OIL | +1.00 | events | +4.50% |
| 1 | F_REFINING_MARGIN → OIL | +1.54 | observed | +1.39% |
| 1 | F_USDINR → OIL | -0.37 | observed | -1.11% |
| 1 | C_RUSSIA → OIL | +1.00 | events | +1.00% |
| 1 | F_REPO_IN → OIL | +1.00 | events | -0.50% |
| 1 | F_GAS_GLOBAL → OIL | -0.47 | observed | -0.14% |
| 1 | F_BRENT → OIL | +0.00 | observed | +0.01% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-11 | Q2 FY27 results/ dividend (screener shows Sep-26 quarter OP Rs 5,793 cr, OPM 46%; PAT not retrieved, ~Rs 4k cr derived from PBT) | results | 1.00 | +0.0% | +0.00% |
| 2026-12 | Exploration updates (KG basin gas discovery 22 Oct 2026) and production target of 1 Mt per quarter | capex | 0.50 | +1.5% | +0.75% |
| 2027-02 | Q3 FY27 results | results | 0.95 | +0.0% | +0.00% |
| 2027-03 | Crude windfall levy reimposition / subsidy-sharing decision as part of OMC compensation | regulatory | 0.15 | -4.0% | -0.60% |

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