# TVSMOTOR — TVS Motor Company Ltd.
*NIFTY_NEXT_50 · Automobile and Auto Components · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +0.6%**, **12 months +1.5%** (rank 83 / 78 of 200 for 3m / 12m); beta 1.44
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +22.0%): 3 months 52%, 12 months 35%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -2.9% … P90 +6.7%; plausible 12m relative-return range incl. stock-specific noise: -32.1% … +18.9%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +0.0 pp (model impact +0.8% beta-adjusted vs realised market-adjusted move +27.0%); forward event exposure +4.4% (3m +2.3%; half assumed priced); company-specific events +0.9%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +7.68 | +0.00 | +5.74 | +1.45 | +0.49 | — |
| Indian vehicle demand (`F_AUTO_DEMAND_IN`) | +10% volumes | +7.00 | +7.00 | +0.00 | +0.00 | +0.00 | — |
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +3.10 | +0.00 | +3.36 | +0.04 | -0.30 | — |
| EV incentives / mandates (`P_EV_POLICY`) | +1 = stronger EV push | +2.95 | +3.00 | +0.00 | -0.04 | -0.01 | — |
| Critical-mineral supply tightness (China export controls on rare earths, magnets, graphite, Ga/Ge) (`NEW_RARE_EARTH_SUPPLY`) | +1 = new/tighter export-control round | -2.88 | -2.00 | -0.88 | +0.00 | +0.00 | — |
| Consumer premiumisation (`T_PREMIUMISATION`) | +1 | +2.63 | +2.50 | +0.00 | +0.13 | +0.00 | — |
| China growth / stimulus (`F_CHINA_GDP`) | +1 pp | -2.55 | +0.00 | -1.58 | -0.61 | -0.36 | — |
| Competitive intensity in Indian two-wheelers/EV two-wheelers (`NEW_2W_COMPETITIVE_INTENSITY`) | +1 = price/share war episode | -2.50 | -2.50 | +0.00 | +0.00 | +0.00 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +2.44 | +2.50 | -0.14 | +0.04 | +0.03 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -2.44 | +0.00 | -0.85 | -1.78 | +0.20 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -2.02 | +0.00 | -1.25 | -0.03 | -0.74 | — |
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | +1.88 | +0.00 | +2.30 | +0.06 | -0.49 | — |
| US 10-year Treasury yield (`F_US_10Y`) | +25 bp yield | -1.77 | -1.50 | -0.25 | -0.01 | -0.01 | +9.4% |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -1.65 | -1.00 | -0.48 | -0.10 | -0.07 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -6.5% | -6.5% | -4.0 | -0.0 | -1.7 | -0.9 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -5.3% | -5.3% | -5.5 | +0.4 | -0.1 | -0.1 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -3.4% | -3.4% | -2.5 | -0.9 | +0.1 | -0.0 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +6.0% | +3.0% | +6.2 | -0.4 | +0.1 | +0.1 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -3.0% | -3.0% | +0.0 | -1.0 | -2.2 | +0.2 |
| Gold and silver slump from January 2026 peaks (silver -53%, gold -24%) (`EV_PRECIOUS_METALS_CRASH_2026`) | occurred | 1.00 | -2.9% | -2.9% | -2.2 | -0.9 | +0.2 | +0.0 |
| Aluminium -20% since June; copper off record; Nifty Metal -7% in October (`EV_BASE_METALS_ALUMINIUM_SLIDE`) | occurred | 1.00 | +2.5% | +2.5% | +2.5 | +0.0 | +0.0 | +0.0 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -2.1% | -2.1% | -1.2 | -0.6 | -0.2 | -0.1 |
| Global and Indian steel prices at multi-year highs (global HRC +60% y/y) (`EV_STEEL_RALLY_2026`) | occurred | 1.00 | -1.9% | -1.9% | -1.8 | +0.0 | -0.0 | -0.0 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -1.7% | -1.7% | -1.0 | -0.5 | -0.1 | -0.1 |
| CAFE-III fuel-efficiency norms notified (30 Sep 2026); no small-car carve-out; 3x credit for BEVs (`EV_CAFE3_NOTIFIED`) | occurred | 1.00 | +1.7% | +1.7% | +1.7 | +0.0 | -0.0 | -0.0 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.36 | -4.6% | -1.6% | -2.0 | -1.0 | -1.2 | -0.4 |

## Strongest causal chains (1st–4th order)
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_RECORD_OUTFLOW_26 ⇒ F_FPI_FLOWS → TVSMOTOR | -5.50% | -5.50% |
| 1 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → TVSMOTOR | -3.96% | -3.96% |
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → TVSMOTOR | +6.25% | +3.12% |
| 1 | EV_UST_SELLOFF_SEP26 ⇒ F_US_10Y → TVSMOTOR | -2.55% | -2.55% |
| 1 | EV_CAFE3_NOTIFIED ⇒ P_EV_POLICY → TVSMOTOR | +2.40% | +2.40% |
| 1 | EV_BASE_METALS_ALUMINIUM_SLIDE ⇒ F_ALUMINIUM → TVSMOTOR | +2.35% | +2.35% |
| 1 | EV_PRECIOUS_METALS_CRASH_2026 ⇒ F_US_10Y → TVSMOTOR | -2.25% | -2.25% |
| 1 | EV_STEEL_RALLY_2026 ⇒ F_STEEL_INDIA → TVSMOTOR | -1.82% | -1.82% |
| 2 | EV_CPI_REACCEL_SEP26 ⇒ F_CPI_IN → F_REPO_IN → TVSMOTOR | -1.32% | -1.32% |
| 1 | EV_US_MIDTERMS_DEM_SWEEP ⇒ F_FPI_FLOWS → TVSMOTOR | +1.25% | +1.25% |
| 1 | EV_FED_SEP26_HIKE ⇒ F_US_10Y → TVSMOTOR | -1.20% | -1.20% |
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_USDINR → TVSMOTOR | +1.17% | +1.17% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → TVSMOTOR | -3.73% | -1.05% |
| 3 | EV_CPI_REACCEL_SEP26 ⇒ F_CPI_IN → F_REPO_IN → F_AUTO_DEMAND_IN → TVSMOTOR | -1.04% | -1.04% |
| 1 | EV_RBI_OCT26_HIKE25 ⇒ F_REPO_IN → TVSMOTOR | -1.00% | -1.00% |

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