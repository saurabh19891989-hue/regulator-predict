# RADICO — Radico Khaitan Ltd
*MIDCAP_100 · Fast Moving Consumer Goods · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -0.5%**, **12 months -1.3%** (rank 122 / 122 of 200 for 3m / 12m); beta 0.90
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +27.5%): 3 months 48%, 12 months 52%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -3.4% … P90 +2.3%; plausible 12m relative-return range incl. stock-specific noise: -28.1% … +38.5%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +0.0 pp (model impact +0.3% beta-adjusted vs realised market-adjusted move +24.7%); forward event exposure +0.0% (3m +0.1%; half assumed priced); company-specific events -0.2%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Consumer premiumisation (`T_PREMIUMISATION`) | +1 | +3.11 | +3.00 | +0.12 | +0.00 | -0.01 | — |
| Rice price (`F_RICE`) | +10% rice | -3.10 | -3.00 | +0.00 | +0.01 | -0.11 | — |
| State excise / liquor pricing policy (key states) (`NEW_STATE_LIQUOR_POLICY`) | +1 = adverse change in excise duty or pricing in UP, Rajasthan, Karnataka, Maharashtra | -3.00 | -3.00 | +0.00 | +0.00 | +0.00 | — |
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +2.84 | +3.00 | +0.00 | -0.11 | -0.05 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -2.35 | +0.00 | -2.15 | -0.12 | -0.09 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -2.15 | +0.00 | -0.89 | -0.35 | -0.91 | — |
| Packaging cost (paper, plastics) (`F_PACKAGING`) | +10% packaging cost | -1.80 | -1.80 | +0.00 | +0.00 | +0.00 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -1.68 | -1.50 | -0.13 | -0.03 | -0.02 | — |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -1.45 | +0.00 | +0.13 | -1.54 | -0.04 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +1.33 | +1.30 | -0.03 | +0.02 | +0.04 | — |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +1.31 | +0.00 | +0.84 | +0.56 | -0.09 | — |
| Brent crude oil price (`F_BRENT`) | +10% Brent | -1.00 | -0.50 | -0.09 | -0.36 | -0.05 | +0.0% |
| ENSO state (El Nino strength) (`NEW_EL_NINO`) | +1 = El Nino year (ONI >= +1.0 sustained); -1 = La Nina | -0.93 | +0.00 | -0.72 | -0.30 | +0.08 | — |
| Monsoon rainfall vs normal (`F_MONSOON`) | +10% above long-period average | +0.92 | +0.00 | +0.53 | -0.16 | +0.56 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -5.8% | -5.8% | -2.5 | -0.9 | -2.0 | -0.4 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -3.0% | -3.0% | -2.9 | +0.1 | -0.1 | -0.1 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -2.9% | -2.9% | +0.0 | -2.3 | -0.5 | -0.1 |
| Kharif 2026 output hit: paddy area down, foodgrain target cut, rice output seen sharpest fall in ~2 decades (`EV_KHARIF26_OUTPUT_HIT`) | occurred | 1.00 | -2.3% | -2.3% | -1.8 | +0.1 | -0.6 | -0.0 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -1.7% | -1.7% | -1.5 | -0.1 | -0.0 | -0.0 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +3.4% | +1.7% | +3.2 | -0.1 | +0.1 | +0.1 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.36 | -3.7% | -1.3% | -1.6 | -0.6 | -1.2 | -0.3 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.58 | +2.2% | +1.3% | +0.8 | +0.7 | +0.7 | +0.1 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -1.2% | -1.2% | +0.0 | -0.7 | +0.2 | -0.7 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.28 | -3.4% | -0.9% | +0.0 | -3.0 | -0.1 | -0.2 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -0.8% | -0.8% | +0.0 | -0.8 | -0.0 | +0.0 |
| OMC ethanol tender ESY 2026-27: no cane juice/syrup/B-heavy ethanol; maize price incentive cut; grain-based ethanol takes over (`EV_ETHANOL_ESY27_TENDER`) | occurred | 1.00 | +0.8% | +0.8% | +0.8 | +0.0 | +0.0 | +0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → RADICO | +3.25% | +1.62% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → RADICO | -1.50% | -0.60% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → RADICO | -1.94% | -0.54% |
| 2 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_RICE → RADICO | +0.72% | +0.49% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → RADICO | -1.25% | -0.45% |
| 2 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → RADICO | -2.43% | -0.44% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → RADICO | +0.75% | +0.44% |
| 2 | EV_PULSES_VEG_SPIKE_WINTER ⇒ F_CPI_IN → F_REPO_IN → RADICO | -1.73% | -0.43% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → RADICO | -1.95% | -0.43% |
| 1 | EV_RBI_FEB27_HIKE25 ⇒ F_REPO_IN → RADICO | -1.50% | -0.41% |
| 1 | EV_RICE_BROKEN_EXPORT_CURB ⇒ F_RICE → RADICO | +0.90% | +0.40% |
| 1 | EV_CPI_BREACH_6PCT ⇒ F_REPO_IN → RADICO | -0.60% | -0.36% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → RADICO | -1.25% | -0.35% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_REPO_IN → RADICO | -1.50% | -0.33% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_FPI_FLOWS → RADICO | -1.25% | -0.31% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_FPI_FLOWS → RADICO | -1.60 | events | -2.08% |
| 1 | F_RICE → RADICO | +0.60 | events | -1.80% |
| 1 | F_REPO_IN → RADICO | +1.00 | events | -1.50% |
| 1 | P_SUGAR_ETHANOL → RADICO | -1.50 | events | +1.20% |
| 1 | F_URBAN_DEMAND → RADICO | +0.20 | events | +0.60% |
| 1 | F_GAS_GLOBAL → RADICO | -0.47 | observed | +0.19% |
| 1 | F_USDINR → RADICO | -0.37 | observed | -0.11% |
| 1 | F_EU_GDP → RADICO | +0.22 | events | +0.09% |
| 3 | P_ANTI_DUMPING_IN → F_CHEM_FEEDSTOCK → F_PACKAGING → RADICO | +0.40 | events | -0.03% |
| 3 | F_CHINA_GDP → F_PETROCHEM_SPREADS → F_PACKAGING → RADICO | +0.30 | events | -0.02% |
| 4 | F_USDCNY → F_CHINA_CHEM_EXPORTS → F_PETROCHEM_SPREADS → F_PACKAGING → RADICO | -0.47 | observed | -0.01% |
| 4 | P_ANTI_DUMPING_IN → F_CHINA_CHEM_EXPORTS → F_PETROCHEM_SPREADS → F_PACKAGING → RADICO | +0.40 | events | -0.01% |

## Analyst profile (agent research, sourced)
# Radico Khaitan — what moves the stock

**Business.** Radico makes mass whisky and brandy (8PM, Old Admiral) and a fast-growing premium range (Magic Moments vodka, Morpheus, Rampur single malt, Jaisalmer gin). Sep-2026 quarter: sales Rs 1,745 cr (+17%), operating margin 20% (16% a year earlier), PAT Rs 232 cr (+66%) (screener.in, 2026-11-05). The stock is +41% over twelve months at 75x earnings, so expectations are high.

## Ranked drivers
1. **Premiumisation and urban demand.** P&A volume guidance for FY27 was lifted to 30%; every extra point of mix lifts margins.
2. **State excise and pricing policy.** Duty cuts in Karnataka more than doubled premium volumes (Multibagg, 2026-11-04); the opposite move in a large state would hurt.
3. **Grain (ENA) and glass costs.** About half of costs; state price control limits pass-through.
4. **Valuation and flows.** A 75x multiple makes the stock sensitive to rates and FPI flow.
5. **Exports and UK access.**

## Worked transmission chains
- **Middle East escalation -> Brent up -> energy for glass furnaces and freight up -> bottle prices up -> COGS up -> margin down (3rd order); Brent up -> INR weaker -> RBI holds -> a 75x multiple de-rates (4th order).**
- **Government raises ethanol blending -> diverts rice and maize -> grain prices up -> ENA costs up -> Radico must pay more for spirit; partial hedge from own distilleries.**
- **Karnataka cuts excise -> premium prices fall -> premium volumes double -> mix improves -> margin up; other states copy -> structural tailwind (4th order).**
- **Weak monsoon -> lower grain supply -> grain price spike -> input costs up, while rural regular-spirit demand weakens and consumers trade down.**

## Current situation
Management said vodka share of India's IMFL market reached 6.3% and sustained a ~20% EBITDA margin (scanx 2026-11-03). Regular volumes are losing ground to premium (ET 2026-10-27). The mid-Q2 empirical link to global gas (+1.04, t=+2.5) is unexplained and is not used causally.

## Upcoming
Q3 FY27 results (about Jan 2027), state excise resets (Mar 2027), guidance updates.

## Bull / bear
**Bull:** premium mix, margin at 20%+, duty cuts spreading. **Bear:** excise hikes, grain/glass inflation, a 75x multiple. Segment mix is approximate.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.