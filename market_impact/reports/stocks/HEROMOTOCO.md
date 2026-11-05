# HEROMOTOCO — Hero MotoCorp Ltd.
*MIDCAP_100 · Automobile and Auto Components · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +1.3%**, **12 months +2.0%** (rank 31 / 31 of 200 for 3m / 12m); beta 1.15
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +21.3%): 3 months 55%, 12 months 50%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -0.6% … P90 +5.7%; plausible 12m relative-return range incl. stock-specific noise: -22.6% … +32.4%
- Decomposition (12m): 0.5 × forward event exposure +2.7% (3m +1.4%; half assumed priced) + 0.5 × company-specific catalysts +2.2%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply +7.8% (beta-adjusted) vs a realised market-adjusted move of +8.9% — gap -1.1 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +4.81 | +0.00 | +3.93 | +0.84 | +0.04 | — |
| Indian vehicle demand (`F_AUTO_DEMAND_IN`) | +10% volumes | +4.50 | +4.50 | +0.00 | +0.00 | +0.00 | — |
| USD/CNY (`F_USDCNY`) | +3% USD/CNY (yuan weaker) | -2.03 | -2.00 | -0.05 | +0.01 | +0.01 | -1.4% |
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | +2.00 | +1.50 | +0.74 | -0.14 | -0.10 | — |
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +1.98 | +0.00 | +2.16 | -0.18 | -0.01 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -1.54 | -0.80 | -0.48 | -0.13 | -0.13 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -1.36 | -1.00 | -0.20 | -0.10 | -0.06 | -1.1% |
| Critical-mineral supply tightness (China export controls on rare earths, magnets, graphite, Ga/Ge) (`NEW_RARE_EARTH_SUPPLY`) | +1 = new/tighter export-control round | -1.31 | +0.00 | -1.31 | +0.00 | +0.00 | — |
| Indian domestic steel price (`F_STEEL_INDIA`) | +7% domestic HRC/rebar price | -1.20 | -1.20 | +0.00 | +0.00 | +0.00 | — |
| US–China trade decoupling (`C_US_CHINA_DECOUPLING`) | +1 = more decoupling | -1.10 | +0.00 | -0.80 | -0.42 | +0.12 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -1.03 | -0.70 | -0.23 | -0.06 | -0.04 | — |
| Aluminium price (`F_ALUMINIUM`) | +10% aluminium | -1.00 | -1.00 | +0.00 | +0.00 | +0.00 | -19.6% |
| Indian wage / employee-cost inflation (`F_WAGES_IN`) | +2 pp | +0.97 | +0.00 | +0.36 | +0.75 | -0.14 | — |
| China growth / stimulus (`F_CHINA_GDP`) | +1 pp | -0.97 | +0.00 | -0.42 | -0.35 | -0.20 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Aluminium -20% since June; copper off record; Nifty Metal -7% in October (`EV_BASE_METALS_ALUMINIUM_SLIDE`) | occurred | 1.00 | +2.0% | +2.0% | +2.0 | +0.0 | +0.0 | +0.0 |
| Global and Indian steel prices at multi-year highs (global HRC +60% y/y) (`EV_STEEL_RALLY_2026`) | occurred | 1.00 | -1.3% | -1.3% | -1.3 | +0.0 | +0.0 | +0.0 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.55 | +2.1% | +1.2% | +1.6 | +0.3 | +0.2 | +0.1 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -1.1% | -1.1% | +0.0 | -0.8 | -0.5 | +0.3 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -1.0% | -1.0% | -0.7 | -0.2 | -0.1 | -0.0 |
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -1.0% | -1.0% | -0.8 | -0.1 | -0.0 | -0.0 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.25 | -3.2% | -0.8% | -2.3 | -0.5 | -0.3 | -0.1 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -0.8% | -0.8% | +0.0 | -0.4 | -0.2 | -0.2 |
| Rural demand indicators mixed: tractor volumes dip in Oct, 2W festive sales firm, rural CPI above urban, rural jobs scheme person-days down (`EV_RURAL_DEMAND_SOFT26`) | occurred | 1.00 | -0.6% | -0.6% | -0.4 | -0.2 | +0.0 | +0.0 |
| China re-imposes/hardens rare-earth and critical-mineral export controls hitting India's autos and electronics (`EV_RARE_EARTH_CONTROLS_REIMPOSED`) | risk_scenario | 0.25 | -2.4% | -0.6% | +0.0 | -2.6 | +0.1 | +0.1 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -0.5% | -0.5% | +0.0 | -0.4 | -0.1 | -0.0 |
| China Q3 GDP +4.5% (beat); property 'mini-stimulus' of late September; PMI 49.3; LPR unchanged (`EV_CHINA_Q3_GDP_AND_MINI_STIMULUS`) | occurred | 1.00 | +0.5% | +0.5% | +0.9 | -0.2 | -0.1 | -0.1 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 2 | EV_RARE_EARTH_CONTROLS_REIMPOSED ⇒ NEW_RARE_EARTH_SUPPLY → F_AUTO_DEMAND_IN → HEROMOTOCO | -2.16% | -0.54% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ C_MIDEAST_CONFLICT → HEROMOTOCO | +0.80% | +0.44% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → HEROMOTOCO | +0.78% | +0.43% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → HEROMOTOCO | -1.32% | -0.33% |
| 1 | EV_BUDGET27_AGRI_RURAL ⇒ F_RURAL_DEMAND → HEROMOTOCO | +0.45% | +0.31% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → HEROMOTOCO | -0.70% | -0.29% |
| 1 | EV_INDIA_HR_STEEL_AD_PROVISIONAL ⇒ F_STEEL_INDIA → HEROMOTOCO | -0.48% | -0.26% |
| 1 | EV_RURAL_RELIEF_PACKAGE ⇒ F_RURAL_DEMAND → HEROMOTOCO | +0.45% | +0.25% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ C_MIDEAST_CONFLICT → HEROMOTOCO | -0.96% | -0.24% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_USDINR → HEROMOTOCO | -1.30% | -0.23% |
| 2 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_RURAL_DEMAND → HEROMOTOCO | +0.34% | +0.23% |
| 2 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → F_USDINR → HEROMOTOCO | +0.46% | +0.23% |
| 2 | EV_GST_RATE_CHANGE_APR27 ⇒ P_GST_CONSUMPTION → F_AUTO_DEMAND_IN → HEROMOTOCO | +0.74% | +0.22% |
| 1 | EV_CHINA_NPC_MAR27_BIG_STIMULUS ⇒ F_USDCNY → HEROMOTOCO | +0.60% | +0.21% |
| 1 | EV_STATE_POLLS_FEB_MAR27 ⇒ F_RURAL_DEMAND → HEROMOTOCO | +0.30% | +0.20% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_AUTO_DEMAND_IN → HEROMOTOCO | +0.50 | director_override | +2.25% |
| 1 | F_ALUMINIUM → HEROMOTOCO | -1.96 | observed | +1.96% |
| 1 | F_STEEL_INDIA → HEROMOTOCO | +1.35 | events | -1.62% |
| 1 | F_USDCNY → HEROMOTOCO | -0.47 | observed | +0.93% |
| 1 | P_EV_POLICY → HEROMOTOCO | +1.10 | events | +0.88% |
| 1 | C_MIDEAST_CONFLICT → HEROMOTOCO | +1.00 | events | -0.80% |
| 1 | F_REPO_IN → HEROMOTOCO | +1.00 | events | -0.70% |
| 1 | F_RURAL_DEMAND → HEROMOTOCO | -0.25 | events | -0.38% |
| 1 | F_USDINR → HEROMOTOCO | -0.37 | observed | +0.37% |
| 1 | F_COPPER → HEROMOTOCO | -0.24 | observed | +0.07% |
| 2 | F_CHINA_GDP → F_RUBBER → HEROMOTOCO | +0.30 | events | -0.02% |
| 3 | P_ANTI_DUMPING_IN → F_CHEM_FEEDSTOCK → F_RUBBER → HEROMOTOCO | +0.40 | events | -0.01% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-11-08 | Diwali festive retail peak (festive dispatch strength drives Q3) | other | 0.95 | +1.2% | +1.19% |
| 2026-12-01 | November dispatch figures | guidance | 0.99 | +0.5% | +0.49% |
| 2027-01 | Q3 FY27 results; management guides stable margin in Q3 | results | 0.97 | +0.0% | +0.00% |
| 2027-03 | VIDA capacity ramp toward 80,000 units/month target (ET Auto headline 2026-10) | capex | 0.50 | +1.0% | +0.50% |

## Analyst profile (agent research, sourced)
# HEROMOTOCO - Hero MotoCorp Ltd. (as of 2026-11-05)

## Business
Hero MotoCorp is India's largest two-wheeler maker (Oct 2026 dispatches 7.34 lakh units, +16% y/y; Sept 7.66 lakh, +12%). The mix is entry-level commuter motorcycles with a premium and scooter push and an EV brand, VIDA, which retailed 66,000 units in Q2 FY27 (+74%) and turned gross-margin positive. It is debt-free, pays out ~71% of profit and yields ~3.4%. Roughly 6% of sales are exports (Latin America, Bangladesh, Africa). It holds an associate stake in Ather Energy, whose fundraising produced a Rs 397 cr one-time gain in Q2.

## What moves the stock (ranked)
1. **Industry volumes and festive demand** (F_AUTO_DEMAND_IN +4.5 per +10%; rural +1.5): ~1.7x operating gearing. Diwali falls on ~8 November, so Q3 benefits from festive retail.
2. **Metals** (steel -1.2 per +7%, aluminium -1.0 per +10%, copper -0.3) and rubber (-0.3): management says input inflation persists in Q3 but expects a stable margin via cost cuts, VIDA economics and selective price rises.
3. **Credit cost** (F_REPO_IN -0.7 per +25bp): the October hike to 5.50% and a 'calibrated tightening' stance hit the most rate-sensitive vehicle buyer.
4. **EV transition** (P_EV_POLICY +0.8, P_PLI +0.8): VIDA is a net positive today (EBITDA drag narrowed to Rs 168 cr, PLI accrual Rs 63 cr) but low-speed EVs threaten the entry segment.
5. **Brent and USD/INR** (-0.6, -1.0): small direct effects. The pack's only significant empirical factor, USD/CNY (-6.27 per +3%, t -3.5), is kept at a shrunk -2.0 because the link is probably a proxy.

## Worked chains
- **Middle East escalation -> Brent up (1st) -> petrol price pump and commuter running costs up (2nd) -> rural entry-level buyers delay purchases or move to low-speed EVs (3rd) -> Hero volume -2-3% and operating deleverage of 1.7x (4th).**
- **Brent up -> INR weaker (2nd) -> imported electronics/EV parts dearer and aluminium/copper in INR higher (3rd) -> margin -30-60bp unless priced (4th).**
- **Brent up -> CPI up (2nd) -> RBI tightens (3rd) -> NBFC two-wheeler loan rates up and credit tightening in unsecured/subprime (4th) -> financed-volume decline.**
- **Aluminium down 20% since June (supply) -> lower casting cost (2nd) -> margin tailwind in H2 FY27 (3rd) -> room to hold prices and absorb steel/rubber (4th).**

## Current situation
Q2 FY27: revenue Rs 14,970 cr (+23%), EBITDA Rs 1,997 cr (13.3%), reported PAT Rs 1,861 cr (+41%) but ~Rs 1,456 cr (+5%) excluding the one-time gain, which missed estimates; shares fell ~4% on 2026-10-29. Management expects Q3 margin stable and export growth back in double digits after logistics disruption to Colombia and Bangladesh. The stock trades at ~18x earnings, below the auto sector average, and is +8% in a month.

## Upcoming
November dispatches (1 Dec), a possible further RBI step in December, Q3 results (~late Jan 2027), VIDA capacity ramp.

## Bull and bear
Bull: festive share gains toward 14%, VIDA turning EBITDA-positive, aluminium relief, rural recovery and a defensive 3.4% yield. Bear: commodity pass-through lags, rate hikes and entry-level substitution by low-speed EVs cut volumes, and VIDA/Ather accounting adds noise.

Confidence: medium; cost shares and pass-through ratios are model estimates flagged in each edge.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.