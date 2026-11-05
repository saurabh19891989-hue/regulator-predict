# TVSMOTOR — TVS Motor Company Ltd.
*NIFTY_NEXT_50 · Automobile and Auto Components · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +0.3%**, **12 months +1.5%** (rank 82 / 42 of 200 for 3m / 12m); beta 1.44
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +22.0%): 3 months 51%, 12 months 40%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -0.8% … P90 +4.6%; plausible 12m relative-return range incl. stock-specific noise: -27.6% … +16.1%
- Decomposition (12m): 0.5 × forward event exposure +3.0% (3m +0.8%; half assumed priced) + 0.5 × company-specific catalysts +0.9%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply +6.7% (beta-adjusted) vs a realised market-adjusted move of +27.0% — gap -20.4 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +7.29 | +0.00 | +5.74 | +1.30 | +0.25 | — |
| Indian vehicle demand (`F_AUTO_DEMAND_IN`) | +10% volumes | +7.00 | +7.00 | +0.00 | +0.00 | +0.00 | — |
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +3.26 | +0.00 | +3.36 | +0.04 | -0.14 | — |
| EV incentives / mandates (`P_EV_POLICY`) | +1 = stronger EV push | +2.96 | +3.00 | +0.00 | -0.04 | +0.00 | — |
| Critical-mineral supply tightness (China export controls on rare earths, magnets, graphite, Ga/Ge) (`NEW_RARE_EARTH_SUPPLY`) | +1 = new/tighter export-control round | -2.88 | -2.00 | -0.88 | +0.00 | +0.00 | — |
| Consumer premiumisation (`T_PREMIUMISATION`) | +1 | +2.63 | +2.50 | +0.00 | +0.13 | +0.00 | — |
| Competitive intensity in Indian two-wheelers/EV two-wheelers (`NEW_2W_COMPETITIVE_INTENSITY`) | +1 = price/share war episode | -2.50 | -2.50 | +0.00 | +0.00 | +0.00 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +2.43 | +2.50 | -0.14 | +0.04 | +0.02 | — |
| China growth / stimulus (`F_CHINA_GDP`) | +1 pp | -2.14 | +0.00 | -1.58 | -0.32 | -0.25 | — |
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | +2.13 | +0.00 | +2.30 | +0.06 | -0.23 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -1.76 | +0.00 | -1.25 | -0.22 | -0.29 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -1.65 | -1.00 | -0.48 | -0.10 | -0.07 | — |
| Indian wage / employee-cost inflation (`F_WAGES_IN`) | +2 pp | +1.42 | +0.00 | +0.00 | +1.48 | -0.06 | — |
| Indian domestic steel price (`F_STEEL_INDIA`) | +7% domestic HRC/rebar price | -1.32 | -1.30 | +0.00 | -0.01 | -0.01 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -5.3% | -5.3% | -5.5 | +0.3 | -0.1 | -0.1 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +6.0% | +3.0% | +6.2 | -0.4 | +0.1 | +0.1 |
| Aluminium -20% since June; copper off record; Nifty Metal -7% in October (`EV_BASE_METALS_ALUMINIUM_SLIDE`) | occurred | 1.00 | +2.5% | +2.5% | +2.5 | +0.0 | +0.0 | +0.0 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -1.7% | -1.7% | -1.0 | -0.5 | -0.1 | -0.1 |
| CAFE-III fuel-efficiency norms notified (30 Sep 2026); no small-car carve-out; 3x credit for BEVs (`EV_CAFE3_NOTIFIED`) | occurred | 1.00 | +1.7% | +1.7% | +1.7 | +0.0 | -0.0 | +0.0 |
| Global and Indian steel prices at multi-year highs (global HRC +60% y/y) (`EV_STEEL_RALLY_2026`) | occurred | 1.00 | -1.4% | -1.4% | -1.4 | +0.0 | -0.0 | -0.0 |
| US midterms (3 Nov 2026): Democrats win House and Senate (`EV_US_MIDTERMS_DEM_SWEEP`) | occurred | 1.00 | +1.3% | +1.3% | +1.4 | -0.1 | +0.0 | +0.0 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -1.2% | -1.2% | -0.6 | -0.5 | -0.1 | -0.0 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -1.2% | -1.2% | -0.9 | -0.4 | +0.1 | +0.0 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.55 | +2.1% | +1.1% | +1.0 | +0.6 | +0.4 | +0.1 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -1.1% | -1.1% | +0.0 | -0.3 | -1.2 | +0.4 |
| China re-imposes/hardens rare-earth and critical-mineral export controls hitting India's autos and electronics (`EV_RARE_EARTH_CONTROLS_REIMPOSED`) | risk_scenario | 0.25 | -4.0% | -1.0% | -3.0 | -1.3 | +0.3 | +0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → TVSMOTOR | +6.25% | +3.12% |
| 1 | EV_RARE_EARTH_CONTROLS_REIMPOSED ⇒ NEW_RARE_EARTH_SUPPLY → TVSMOTOR | -3.00% | -0.75% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → TVSMOTOR | -3.75% | -0.67% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → TVSMOTOR | -2.40% | -0.60% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_FPI_FLOWS → TVSMOTOR | -2.40% | -0.60% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → TVSMOTOR | -2.33% | -0.58% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → TVSMOTOR | +1.04% | +0.57% |
| 2 | EV_BUDGET27_AGRI_RURAL ⇒ F_RURAL_DEMAND → F_AUTO_DEMAND_IN → TVSMOTOR | +0.69% | +0.48% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → TVSMOTOR | -1.76% | -0.44% |
| 1 | EV_BUDGET_FY28_LTCG_RELIEF ⇒ F_FPI_FLOWS → TVSMOTOR | +1.25% | +0.44% |
| 2 | EV_RARE_EARTH_CONTROLS_REIMPOSED ⇒ NEW_RARE_EARTH_SUPPLY → F_AUTO_DEMAND_IN → TVSMOTOR | -1.68% | -0.42% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → TVSMOTOR | -1.00% | -0.42% |
| 1 | EV_Q2_FY27_GDP_STRONG ⇒ F_FPI_FLOWS → TVSMOTOR | +0.50% | +0.40% |
| 2 | EV_RURAL_RELIEF_PACKAGE ⇒ F_RURAL_DEMAND → F_AUTO_DEMAND_IN → TVSMOTOR | +0.69% | +0.38% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_USDINR → TVSMOTOR | +1.95% | +0.35% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_FPI_FLOWS → TVSMOTOR | -1.60 | events | -4.00% |
| 1 | F_AUTO_DEMAND_IN → TVSMOTOR | +0.50 | director_override | +3.50% |
| 1 | P_EV_POLICY → TVSMOTOR | +1.10 | events | +3.30% |
| 1 | F_ALUMINIUM → TVSMOTOR | -1.96 | observed | +2.35% |
| 1 | F_STEEL_INDIA → TVSMOTOR | +1.35 | events | -1.76% |
| 1 | F_US_10Y → TVSMOTOR | +1.68 | observed | -1.26% |
| 1 | F_REPO_IN → TVSMOTOR | +1.00 | events | -1.00% |
| 1 | F_USDINR → TVSMOTOR | -0.37 | observed | -0.55% |
| 2 | F_DXY → C_AFRICA_LATAM → TVSMOTOR | +0.74 | observed | -0.18% |
| 1 | F_COPPER → TVSMOTOR | -0.24 | observed | +0.12% |
| 2 | C_US_CHINA_DECOUPLING → NEW_RARE_EARTH_SUPPLY → TVSMOTOR | -0.10 | events | +0.10% |
| 2 | F_CHINA_GDP → F_RUBBER → TVSMOTOR | +0.30 | events | -0.02% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-12 | Srinivasan family dispute: court or settlement developments | litigation | 0.40 | -1.0% | -0.40% |
| 2026-12 | EV capacity ramp toward 80,000 units/month | capex | 0.80 | +1.0% | +0.80% |
| 2026-12-01 | November sales print | other | 1.00 | +0.0% | +0.00% |
| 2027-01 | Q3 FY27 results | results | 0.95 | +0.0% | +0.00% |
| 2027-07 | Consumer-finance demerger (board approved 2026-10-28; NCLT and shareholder approvals pending, 8-10 months) | corporate_action | 0.35 | +1.5% | +0.52% |

## Analyst profile (agent research, sourced)
# TVS Motor Company Ltd. (TVSMOTOR) — Market Impact profile, 2026-11-05

## Business
TVS Motor is India's third-largest two-wheeler maker and a major three-wheeler and electric two-wheeler player (iQube, Orbiter), with Norton Motorcycles and Swiss E-Mobility Group overseas. Motorcycles and scooters are about 72% of revenue, EVs ~8%, three-wheelers ~7%; exports are about 28% of volumes (Africa, Latin America, ASEAN, South Asia). Its consumer-finance arm, TVS Credit, is about 8% of consolidated revenue and is being demerged. Q2 FY27 (Sep 2026) was a record: revenue Rs 17,103 cr, EBITDA +47% y/y, profit +46-52% and record market share. The market capitalisation is around Rs 2.1 lakh cr (estimate), with the stock +28.7% in 12 months.

## What moves the stock (ranked)
1. **Domestic two-wheeler demand (F_AUTO_DEMAND_IN +7 per +10% volumes).** October 2W sales +22% to 5.15 lakh units; festival demand, rural income and GST-2.0 pricing are the drivers.
2. **US yields and flows (F_US_10Y -1.5, t=-3.1; F_FPI_FLOWS +2.5).** The stock's beta is ~1.5 and its empirical rate/dollar sensitivity is the most statistically significant in this batch.
3. **Metals (aluminium -1.2, steel -1.3, copper -0.5).** Aluminium (t=-2.0) is a real cost, but aluminium is -19.6% since June, which supports Q3 margins; steel is +20.6%.
4. **Margin-structure items**: premiumisation (+2.5), EV scale (+3.0), competition (-2.5).
5. **Rates (repo -1.0)** through retail finance affordability.
6. **FX (USD/INR +1.5 per +3%)** from the ~28% export share.
7. **Idiosyncratic events**: finance demerger (8-10 months) and promoter family dispute.

## Transmission examples
- **Oil-rates-demand chain (4 orders).** Mideast escalation -> Brent $95-100 and INR weaker (94.5) -> inflation up and the RBI raises repo to 5.50% (7 Oct) with no cuts in sight -> 2W loan EMIs and fuel costs rise for the entry-level rider -> entry commuter volumes soften while premium holds -> TVS's premium-heavy mix holds up better than Hero's.
- **Aluminium chain (3 orders).** China aluminium output curbs -> LME aluminium up -> engine and wheel casting costs up -> TVS margin falls ~35bp if unrecovered -> price hike in Jan -> volumes elastic only at the entry level. (Currently reverse: aluminium -19.6% helps.)
- **Rare earth chain (4 orders).** China limits magnet exports -> motor suppliers cut allocations -> iQube/Orbiter output constrained (capacity crunch flagged in Aug) -> EV sales lost to Ather/Ola/Bajaj -> operating leverage and PLI incentives lost.
- **FX chain (3 orders).** USD/INR rises -> export realisations in INR up -> but Nigeria/Egypt currency weakness reduces African import demand -> net positive but volatile.
- **Dollar chain (3 orders).** Fed on hold with 4.89% 10-year -> DXY +2% since June -> FPI outflows from Indian consumer discretionary -> TVS (beta 1.5, FIIs hold) derates beyond fundamentals.

## Current situation
Q2 FY27: record revenue and EBITDA +47%, with brokerages raising targets (Motilal Oswal estimates +11%, CLSA and Nomura up to 15% upside; Citi Sell). Management said EV capacity will rise to 80,000 units/month and the consumer-finance business will be demerged in 8-10 months. October sales: 2W +22%, total +29%. A promoter family dispute (Goodreturns 2026-10-27) adds governance headline risk. Note that reported profit figures differ (Rs 1,219 cr vs Rs 1,377 cr) between outlets, likely due to perimeter (standalone/ consolidated).

## Upcoming events
Monthly sales (Dec 1); Q3 results (January); demerger approvals; EV capacity ramp; Budget 1 Feb 2027; family dispute developments.

## Bull case
Share gains persist, EBITDA margins reach 14%, the EV business turns profitable, and the demerger crystallises value for TVS Credit.

## Bear case
Commodity and rate headwinds compress margins, festive pre-buying fades, rare-earth or competitor pressure hits EVs, and promoter-family litigation distracts. Limits: no fundamentals page was retrieved, valuation multiples are missing, and cost splits are estimates.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.