# GMRAIRPORT — GMR Airports Ltd.
*MIDCAP_100 · Services · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -3.4%**, **12 months -6.3%** (rank 180 / 179 of 200 for 3m / 12m); beta 1.34
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +20.7%): 3 months 37%, 12 months 60%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -13.4% … P90 -1.6%; plausible 12m relative-return range incl. stock-specific noise: -39.7% … +15.4%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves -1.4 pp (model impact -6.5% beta-adjusted vs realised market-adjusted move -3.7%); forward event exposure -10.4% (3m -6.4%; half assumed priced); company-specific events +2.7%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Air/hotel/tourism demand (`F_TRAVEL_DEMAND`) | +10% | +9.00 | +9.00 | +0.00 | +0.00 | +0.00 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -8.13 | +0.00 | -4.70 | -2.96 | -0.48 | — |
| Airport tariff regulation outcomes (AERA) (`NEW_AIRPORT_TARIFF_REGULATION`) | +1 = control-period order raising aero yield ~10% | +6.00 | +6.00 | +0.00 | +0.00 | +0.00 | — |
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +5.31 | +2.50 | +3.28 | -0.26 | -0.21 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -5.30 | -2.50 | -1.49 | -0.62 | -0.70 | — |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +5.24 | +0.00 | +1.78 | +3.02 | +0.44 | — |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -4.26 | +0.00 | +0.00 | -2.68 | -1.58 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -4.15 | -3.00 | -0.72 | -0.40 | -0.03 | — |
| Indian corporate credit spreads (`F_CREDIT_SPREADS_IN`) | +50 bp spreads | -3.59 | -3.50 | +0.00 | -0.09 | +0.00 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -3.41 | -1.20 | -0.45 | -1.00 | -0.76 | -1.1% |
| India 10-year G-sec yield (`F_GSEC_10Y_IN`) | +25 bp yield | -2.88 | -2.50 | -0.35 | -0.04 | +0.01 | — |
| Brent crude oil price (`F_BRENT`) | +10% Brent | -2.85 | -1.50 | -0.43 | -0.45 | -0.47 | +0.0% |
| New NCR airport competing with Delhi (`NEW_NCR_AIRPORT_COMPETITION`) | +1 = 5% of Delhi passengers diverted | -2.50 | -2.50 | +0.00 | +0.00 | +0.00 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +2.42 | +2.00 | +0.21 | +0.05 | +0.17 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -9.4% | -9.4% | +0.0 | -5.4 | -3.5 | -0.5 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -5.3% | -5.3% | -4.4 | -0.5 | -0.1 | -0.4 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -5.0% | -5.0% | -4.5 | -0.1 | -0.4 | -0.1 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -4.7% | -4.7% | -4.5 | +0.0 | -0.1 | -0.0 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.55 | +7.6% | +4.2% | +4.5 | +1.5 | +0.8 | +0.9 |
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -3.4% | -3.4% | -2.5 | -0.6 | -0.1 | -0.2 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +6.2% | +3.1% | +5.0 | +0.6 | +0.1 | +0.5 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.25 | -12.1% | -3.0% | -6.3 | -2.5 | -1.6 | -1.6 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -2.5% | -2.5% | +0.0 | -1.6 | -0.6 | -0.3 |
| Risk: USD/INR >98 and/or reserves < US$650bn (disorderly rupee, emergency RBI response) (`EV_RUPEE_BREAK_98_RESERVE_STRESS`) | risk_scenario | 0.18 | -12.1% | -2.2% | -10.1 | -1.3 | -0.5 | -0.3 |
| Kharif 2026 output hit: paddy area down, foodgrain target cut, rice output seen sharpest fall in ~2 decades (`EV_KHARIF26_OUTPUT_HIT`) | occurred | 1.00 | -2.1% | -2.1% | +0.0 | +0.0 | -1.3 | -0.8 |
| RBI MPC Dec 2026 (~4 Dec): hikes repo another 25 bp to 5.75% (`EV_RBI_DEC26_HIKE25`) | scheduled | 0.42 | -5.0% | -2.1% | -4.5 | -0.1 | -0.4 | -0.1 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → GMRAIRPORT | +5.00% | +2.50% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ C_MIDEAST_CONFLICT → GMRAIRPORT | +2.50% | +1.38% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → GMRAIRPORT | -3.00% | -1.26% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → GMRAIRPORT | +1.95% | +1.07% |
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → GMRAIRPORT | -2.00% | -1.00% |
| 2 | EV_PULSES_VEG_SPIKE_WINTER ⇒ F_CPI_IN → F_REPO_IN → GMRAIRPORT | -3.46% | -0.86% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → GMRAIRPORT | -3.30% | -0.83% |
| 1 | EV_RBI_FEB27_HIKE25 ⇒ F_REPO_IN → GMRAIRPORT | -3.00% | -0.81% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ C_MIDEAST_CONFLICT → GMRAIRPORT | -3.00% | -0.75% |
| 1 | EV_CPI_BREACH_6PCT ⇒ F_GSEC_10Y_IN → GMRAIRPORT | -1.25% | -0.75% |
| 1 | EV_CPI_BREACH_6PCT ⇒ F_REPO_IN → GMRAIRPORT | -1.20% | -0.72% |
| 1 | EV_BANKING_LIQUIDITY_DEFICIT_MAR27 ⇒ F_CREDIT_SPREADS_IN → GMRAIRPORT | -1.05% | -0.63% |
| 2 | EV_NBS_RABI_HIKE ⇒ P_FERT_SUBSIDY → F_GSEC_10Y_IN → GMRAIRPORT | -0.60% | -0.57% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_REPO_IN → GMRAIRPORT | -3.00% | -0.54% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → GMRAIRPORT | -3.00% | -0.54% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_GSEC_10Y_IN → GMRAIRPORT | +1.55 | director_override | -3.88% |
| 1 | F_FPI_FLOWS → GMRAIRPORT | -1.60 | events | -3.20% |
| 1 | F_REPO_IN → GMRAIRPORT | +1.00 | events | -3.00% |
| 1 | C_MIDEAST_CONFLICT → GMRAIRPORT | +1.00 | events | -2.50% |
| 1 | F_CREDIT_SPREADS_IN → GMRAIRPORT | +0.50 | events | -1.75% |
| 1 | F_GDP_IN → GMRAIRPORT | +0.50 | events | +1.00% |
| 1 | F_ALUMINIUM → GMRAIRPORT | -1.96 | observed | +0.78% |
| 2 | F_URBAN_DEMAND → F_TRAVEL_DEMAND → GMRAIRPORT | +0.20 | events | +0.58% |
| 2 | C_MIDEAST_CONFLICT → F_TRAVEL_DEMAND → GMRAIRPORT | +1.00 | events | -0.54% |
| 1 | F_URBAN_DEMAND → GMRAIRPORT | +0.20 | events | +0.50% |
| 1 | F_USDINR → GMRAIRPORT | -0.37 | observed | +0.44% |
| 1 | F_BRENT → GMRAIRPORT | +0.00 | observed | -0.00% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-12 | Delhi Cargo Terminal 1 concession start (award letter 2026-11-04) and Delhi F&B licence (Rs109 cr fee in FY28) | capex | 0.80 | +1.0% | +0.80% |
| 2026-12 | Bhogapuram (Vizag) airport commercial operations ramp (opening advanced to Q2 FY27 per Multibagg; status unverified) | capex | 0.50 | +1.5% | +0.75% |
| 2027-01 | Q3 FY27 results; H2 traffic recovery thesis tested | results | 0.95 | +1.0% | +0.95% |
| 2027-03 | AERA tariff determination / true-up decisions for Delhi/Hyderabad | regulatory | 0.25 | +1.5% | +0.38% |
| 2027-03 | Promoter/ FPI block trades (e.g. GQG sold Rs818 cr block 2026-10-09) | corporate_action | 0.40 | -0.5% | -0.20% |

## Analyst profile (agent research, sourced)
# GMRAIRPORT — GMR Airports Ltd. (Midcap 100) — profile as of 2026-11-05

## Business
Private airport developer-operator: Delhi (DIAL) and Hyderabad (GHIAL) are the profit engines, with Goa (Mopa), Bhogapuram/Visakhapatnam, Crete (Greece), Cebu and cargo, hospitality and land development. TTM revenue Rs16.0k cr (+29%), EBITDA Rs6.1k cr (38%), interest Rs3.8k cr, PAT Rs788 cr. Q2 FY27: PAT Rs65 cr (+86% y/y) on revenue ~Rs4.1k cr (+12%), EBITDA flat q/q (screener.in pack). H1 FY27 passengers hit a record 58.2m but growth was flat Apr-Sep, with +0.9% in September (Sahi, Oct 2026).

## What moves the stock (ranked)
1. **Air-travel demand (+9 per +10%).** Operating leverage on a Rs6.1k cr EBITDA base; non-aero is ~40% of revenue.
2. **Rates and credit spreads (-3.0 repo, -2.5 G-sec, -3.5 spreads).** Debt ~Rs45k cr (estimate); Q2 interest Rs993 cr vs EBITDA Rs1,480 cr; P/E 178.
3. **Airport tariff regulation (+6 central, unknown timing).** AERA control-period outcomes for Delhi and Hyderabad.
4. **Fuel/airline health (Brent -1.5; IndiGo link 0.05).** Airlines pass fuel to fares, trimming pax.
5. **Competition and geopolitics (-2.5 each):** Noida airport vs Delhi; Middle East disruptions to Gulf routes.

## Transmission examples
- Middle East escalation -> Brent up -> ATF up (1st) -> IndiGo/Air India raise fares, cut capacity (2nd) -> GMR pax growth flat, non-aero spends fall (3rd) -> EBITDA/PAT squeezed against fixed interest (4th). Simultaneously Gulf route cancellations hit international pax at Delhi.
- Crude falls ~7% (as on 2026-11-03) -> airlines recover (IndiGo +6-7%) -> more capacity in peak season -> H2 traffic recovery promised by management -> GMR shares rise.
- RBI holds / G-sec yield up -> floating debt cost up and discount rate up -> equity de-rates (beta 1.5) -> leveraged infra names fall more than market.
- USD/INR up -> USD bond servicing cost up (partly tariff pass-through) -> small net negative; weaker INR also lifts airline costs, which feed back to traffic.

## Current situation and upcoming
Stock ~Rs99 (52w Rs84-116), +6.8% in 1m, -6.7% in 3m. Block deal of Rs818 cr on 2026-10-09 (GQG selling) shows FPI churn; FIIs 22.95%. Delhi Cargo Terminal 1 award letter (2026-11-04); Delhi F&B licence Rs109 cr FY28 fee. Emkay Buy, target Rs120 (2026-10-30). Upcoming: Q3 FY27 (Jan 2027), AERA decisions, Bhogapuram ramp.

## Bull and bear
Bull: H2 recovery, non-aero monetisation, cargo/real estate, deleveraging and rating upgrades. Bear: flat traffic persists, airline stress, adverse AERA order, interest burden, Noida diversion.

## Gaps
Debt split, DIAL/GHIAL contribution and AERA calendar are estimates (model knowledge); GMR-specific AERA and NCR competition news were not found in the sources reviewed.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.