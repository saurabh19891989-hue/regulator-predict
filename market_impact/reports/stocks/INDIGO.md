# INDIGO — InterGlobe Aviation Ltd.
*NIFTY_50 · Services · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -0.1%**, **12 months -0.2%** (rank 111 / 113 of 200 for 3m / 12m); beta 1.26
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +25.4%): 3 months 50%, 12 months 50%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -8.7% … P90 +6.5%; plausible 12m relative-return range incl. stock-specific noise: -25.2% … +40.2%
- Decomposition (12m): 0.5 × forward event exposure -0.5% (3m -0.6%; half assumed priced) + 0.5 × company-specific catalysts +1.1%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply -4.2% (beta-adjusted) vs a realised market-adjusted move of +16.0% — gap -20.2 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Air/hotel/tourism demand (`F_TRAVEL_DEMAND`) | +10% | +9.00 | +9.00 | +0.00 | +0.00 | +0.00 | — |
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +6.37 | +3.50 | +2.88 | +0.03 | -0.04 | — |
| Airfare caps / government fare intervention (`NEW_AIRFARE_REGULATION`) | +1 = binding fare caps in stress periods | -6.00 | -6.00 | +0.00 | +0.00 | +0.00 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -5.79 | -2.50 | -2.38 | -0.51 | -0.41 | — |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +3.30 | +0.00 | +2.06 | +1.11 | +0.13 | — |
| Brent crude oil price (`F_BRENT`) | +10% Brent | -3.17 | -2.50 | -0.24 | -0.27 | -0.16 | +0.0% |
| Domestic airline industry capacity additions by competitors (`NEW_DOMESTIC_AIRLINE_CAPACITY`) | +1 = +5% industry capacity | -3.00 | -3.00 | +0.00 | +0.00 | +0.00 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -2.90 | -2.00 | -0.46 | -0.24 | -0.20 | -1.1% |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +2.79 | +2.50 | +0.24 | +0.01 | +0.04 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -2.14 | +0.00 | -1.78 | -0.46 | +0.10 | — |
| Consumer premiumisation (`T_PREMIUMISATION`) | +1 | +1.94 | +0.00 | +1.72 | +0.22 | +0.00 | — |
| OPEC+ crude supply decisions (`NEW_OPEC_PLUS_SUPPLY`) | +1 mb/d OPEC+ production (quota/actual) | +1.92 | +0.00 | +1.60 | +0.14 | +0.18 | — |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -1.74 | +0.00 | -1.17 | -0.54 | -0.02 | +3.5% |
| Russia-Ukraine war / Western sanctions intensity on Russia (`NEW_RUSSIA_UKRAINE_WAR`) | +1 = escalation (new sanctions round, strikes on energy/port infrastructure); -1 = ceasefire/sanctions relief | -1.68 | +0.00 | -1.58 | -0.10 | -0.00 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -6.1% | -6.1% | -5.5 | -0.5 | -0.0 | -0.1 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.55 | +8.3% | +4.6% | +6.3 | +1.3 | +0.6 | +0.2 |
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -3.9% | -3.9% | -3.0 | -0.5 | -0.2 | -0.1 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +7.1% | +3.5% | +6.2 | +0.7 | +0.0 | +0.1 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.25 | -12.9% | -3.2% | -8.5 | -2.8 | -1.2 | -0.4 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -2.5% | -2.5% | +0.0 | -2.0 | -0.5 | +0.1 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -2.2% | -2.2% | -2.1 | +0.0 | -0.0 | -0.0 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -1.7% | -1.7% | -0.8 | -0.9 | -0.1 | +0.1 |
| Risk: USD/INR >98 and/or reserves < US$650bn (disorderly rupee, emergency RBI response) (`EV_RUPEE_BREAK_98_RESERVE_STRESS`) | risk_scenario | 0.18 | -9.4% | -1.7% | -8.7 | -0.1 | -0.4 | -0.2 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -1.7% | -1.7% | -1.2 | -0.1 | -0.2 | -0.1 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -1.7% | -1.7% | -0.6 | -0.9 | -0.2 | -0.0 |
| US midterms (3 Nov 2026): Democrats win House and Senate (`EV_US_MIDTERMS_DEM_SWEEP`) | occurred | 1.00 | +1.6% | +1.6% | +1.4 | +0.2 | +0.0 | +0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → INDIGO | +6.25% | +3.12% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → INDIGO | +3.25% | +1.79% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ C_MIDEAST_CONFLICT → INDIGO | +2.50% | +1.38% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → INDIGO | -5.50% | -1.38% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ C_MIDEAST_CONFLICT → INDIGO | -3.00% | -0.75% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → INDIGO | -3.75% | -0.67% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → INDIGO | -2.40% | -0.60% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_FPI_FLOWS → INDIGO | -2.40% | -0.60% |
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → INDIGO | -1.20% | -0.60% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → INDIGO | -2.33% | -0.58% |
| 1 | EV_HORMUZ_FULL_CLOSURE ⇒ F_BRENT → INDIGO | -11.25% | -0.56% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_USDINR → INDIGO | -2.60% | -0.47% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_GDP → F_BRENT → INDIGO | +1.80% | +0.45% |
| 1 | EV_CPI_BREACH_6PCT ⇒ F_GSEC_10Y_IN → INDIGO | -0.75% | -0.45% |
| 1 | EV_BUDGET_FY28_LTCG_RELIEF ⇒ F_FPI_FLOWS → INDIGO | +1.25% | +0.44% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_FPI_FLOWS → INDIGO | -1.60 | events | -4.00% |
| 1 | C_MIDEAST_CONFLICT → INDIGO | +1.00 | events | -2.50% |
| 1 | F_GSEC_10Y_IN → INDIGO | +1.55 | director_override | -2.33% |
| 1 | F_US_10Y → INDIGO | +1.68 | observed | -1.17% |
| 1 | F_REPO_IN → INDIGO | +1.00 | events | -0.80% |
| 1 | F_USDINR → INDIGO | -0.37 | observed | +0.74% |
| 1 | F_URBAN_DEMAND → INDIGO | +0.20 | events | +0.70% |
| 2 | F_URBAN_DEMAND → F_TRAVEL_DEMAND → INDIGO | +0.20 | events | +0.58% |
| 1 | F_REFINING_MARGIN → INDIGO | +0.60 | events | -0.54% |
| 2 | C_MIDEAST_CONFLICT → F_TRAVEL_DEMAND → INDIGO | +1.00 | events | -0.54% |
| 1 | P_FUEL_TAX_IN → INDIGO | -0.50 | events | +0.40% |
| 1 | F_BRENT → INDIGO | +0.00 | observed | -0.00% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-11-16 | Supreme Court deadline on airfare regulation matter (Sunday Guardian headline 2026-10-16); possible clarity on rules | regulatory | 0.70 | -0.5% | -0.35% |
| 2026-12 | Peak winter/wedding-season fares; Q3 FY27 capacity and PRASK (>25% PRASK growth guided for FY27) | guidance | 0.80 | +1.5% | +1.20% |
| 2027-01 | Q3 FY27 results (seasonally strong; Q3 FY26 net profit Rs549 cr) | results | 0.95 | +1.0% | +0.95% |
| 2027-01 | 2027 fare-intervention provisions start; first use of powers in extraordinary situations | regulatory | 0.15 | -5.0% | -0.75% |

## Analyst profile (agent research, sourced)
# INDIGO — InterGlobe Aviation Ltd. (Nifty 50) — profile as of 2026-11-05

## Business
India's largest airline: low-cost, single-type fleet (262 aircraft at last screener count), ~65% domestic share in September 2026 (Sahi, 2026-10-06), growing international network. Heavily lease-financed, so a large share of costs is USD-linked. FY26 net loss Rs2,394 cr; Q1 FY27 loss Rs238 cr; Q2 FY27 (Sep quarter, seasonally weak) loss Rs1,879 cr on revenue Rs23,364 cr (+26% y/y) as fuel and a weaker rupee outran fares (Free Press Journal summary of the company release).

## What moves the stock (ranked)
1. **Crude/ATF (-2.5 per +10% Brent; empirical -1.79, t -3.8).** Fuel ~38% of costs; fare pass-through of 80-90% (Nomura) comes with a lag. Brent is $95 on the factor file (+49.5% 12m, -5.6% 1m) and crude fell ~7.6% on 2026-11-03, which drove a 3-day, ~14% rally.
2. **Rupee (-2.0 per +3% USD/INR).** USD leases, maintenance and fuel; MTM on lease liabilities hits reported profit.
3. **Travel demand/operating leverage (+9 per +10% demand).** Supply is constrained (capacity roughly flat in Q2, single-digit FY27), so demand upside drops through at ~90%.
4. **Airfare regulation (-6 central, two-sided).** New rules notified 2026-11-02 let the government intervene in fares in extraordinary situations from 2027.
5. **Competitive capacity (-3), Middle East airspace (-2.5), rates (-1.5/-0.8).**

## Transmission examples
- Middle East escalation -> Brent up (1st: IndiGo -2.5 per +10%) -> ATF up with a 1-2 quarter pass-through lag -> airfares up -> demand elasticity trims pax growth (2nd) -> INR weaker as oil import bill rises (3rd: another -2.0) -> RBI holds, urban demand softens (4th). Plus airspace reroutes add direct cost.
- Brent falls $10 -> ATF down ~8% -> margins expand as fares stay sticky (PRASK >25% growth guided) -> Q3/Q4 EBITDA surprise -> deleveraging of lease burden; stock rallies as on 2026-11-03/05.
- Airfare rules -> government may cap fares in peak/crisis -> pass-through of fuel spikes limited -> fuel beta rises (the two shocks compound).
- Engine groundings -> capacity cap -> higher industry yields but wet-lease costs rise; competitor Air India group gains if it adds capacity.
- GMR Airports: IndiGo is its largest airline customer; IndiGo capacity cuts or weak profits reduce passenger traffic at Delhi/Hyderabad (company link recorded on GMRAIRPORT).

## Current situation
Pack: price Rs5,426, +20.4% 6m, -3.7% 12m, 35% vol. Promoters 41.57% (down 21.7pp over 3 years), DIIs 33.3%. Analysts divided on recovery timeline (BusinessLine, 2026-10-30), Nomura sees Rs6,000. Q3 is seasonally strongest; Q3 FY26 net profit was Rs549 cr.

## Upcoming events
SC airfare matter (Nov 16 deadline per Sunday Guardian headline); peak-season Q3 results (Jan 2027); first uses of 2027 fare-intervention powers (low probability).

## Bull and bear
Bull: Brent < $85, INR stable, PRASK +25%, mild airfare rules, mid-teens growth resumes from FY28. Bear: crude re-spike with cap-limited pass-through, price war from competitors, engine groundings, INR slide.

## Gaps
Net debt/cash, exact fuel share and hedging not obtained from primary filings; CASK figures in secondary sources looked inconsistent and were not used.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.