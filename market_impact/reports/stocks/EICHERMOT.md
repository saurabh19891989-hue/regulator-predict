# EICHERMOT — Eicher Motors Ltd.
*NIFTY_50 · Automobile and Auto Components · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -0.4%**, **12 months -0.5%** (rank 116 / 116 of 200 for 3m / 12m); beta 1.11
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +21.6%): 3 months 48%, 12 months 42%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -4.1% … P90 +1.7%; plausible 12m relative-return range incl. stock-specific noise: -26.6% … +29.1%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves -0.5 pp (model impact -1.1% beta-adjusted vs realised market-adjusted move +2.9%); forward event exposure +1.7% (3m +0.7%; half assumed priced); company-specific events +0.6%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +6.52 | +4.00 | +1.84 | +0.46 | +0.22 | — |
| Indian vehicle demand (`F_AUTO_DEMAND_IN`) | +10% volumes | +4.50 | +4.50 | +0.00 | +0.00 | +0.00 | — |
| Competitive intensity in Indian two-wheelers/EV two-wheelers (`NEW_2W_COMPETITIVE_INTENSITY`) | +1 = price/share war episode | -2.50 | -2.50 | +0.00 | +0.00 | +0.00 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -2.36 | +0.00 | -0.87 | -1.61 | +0.12 | — |
| Consumer premiumisation (`T_PREMIUMISATION`) | +1 | +2.08 | +2.00 | +0.00 | +0.08 | +0.00 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +2.07 | +2.00 | +0.01 | +0.02 | +0.04 | — |
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +2.00 | +0.00 | +2.16 | +0.07 | -0.22 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -1.60 | +0.00 | -0.55 | -0.38 | -0.67 | — |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -1.48 | +0.00 | +0.00 | -0.59 | -0.89 | — |
| Critical-mineral supply tightness (China export controls on rare earths, magnets, graphite, Ga/Ge) (`NEW_RARE_EARTH_SUPPLY`) | +1 = new/tighter export-control round | -1.44 | +0.00 | -1.44 | +0.00 | +0.00 | — |
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | +1.23 | +0.00 | +1.48 | +0.11 | -0.36 | — |
| China growth / stimulus (`F_CHINA_GDP`) | +1 pp | -1.22 | +0.00 | -0.64 | -0.35 | -0.23 | — |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -1.22 | +0.00 | -0.71 | -0.44 | -0.07 | +3.5% |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -1.19 | -0.60 | -0.49 | -0.04 | -0.05 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -4.9% | -4.9% | -2.0 | -0.5 | -1.4 | -1.1 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -4.6% | -4.6% | -4.4 | -0.0 | -0.1 | -0.1 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -2.8% | -2.8% | +0.0 | -1.0 | -2.0 | +0.1 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +5.2% | +2.6% | +5.0 | +0.0 | +0.1 | +0.1 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -1.8% | -1.8% | +0.0 | -1.7 | -0.1 | -0.0 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.28 | -5.5% | -1.5% | +0.0 | -4.8 | -0.7 | -0.0 |
| Gold and silver slump from January 2026 peaks (silver -53%, gold -24%) (`EV_PRECIOUS_METALS_CRASH_2026`) | occurred | 1.00 | -1.5% | -1.5% | +0.0 | -1.5 | +0.0 | +0.0 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -1.4% | -1.4% | -1.4 | +0.0 | +0.0 | -0.0 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.36 | -3.8% | -1.4% | -1.0 | -1.1 | -1.1 | -0.6 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -1.3% | -1.3% | -0.9 | -0.3 | -0.1 | -0.1 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -1.3% | -1.3% | +0.0 | -0.9 | -0.2 | -0.1 |
| Disorderly yen carry-trade unwind (Aug-2024-style) after BoJ/MoF action (`EV_YEN_CARRY_UNWIND_RISK`) | risk_scenario | 0.18 | -6.7% | -1.2% | +0.0 | -6.0 | -0.5 | -0.3 |

## Strongest causal chains (1st–4th order)
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_RECORD_OUTFLOW_26 ⇒ F_FPI_FLOWS → EICHERMOT | -4.40% | -4.40% |
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → EICHERMOT | +5.00% | +2.50% |
| 1 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → EICHERMOT | -1.98% | -1.98% |
| 1 | EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26 ⇒ F_GSEC_10Y_IN → EICHERMOT | -1.40% | -1.40% |
| 1 | EV_US_MIDTERMS_DEM_SWEEP ⇒ F_FPI_FLOWS → EICHERMOT | +1.00% | +1.00% |
| 1 | EV_STEEL_RALLY_2026 ⇒ F_STEEL_INDIA → EICHERMOT | -0.98% | -0.98% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → EICHERMOT | -2.99% | -0.84% |
| 1 | EV_GDP_Q1FY27_7_8 ⇒ F_GOVT_CAPEX → EICHERMOT | +0.80% | +0.80% |
| 2 | EV_CPI_REACCEL_SEP26 ⇒ F_CPI_IN → F_REPO_IN → EICHERMOT | -0.79% | -0.79% |
| 2 | EV_UST_SELLOFF_SEP26 ⇒ F_US_10Y → F_FPI_FLOWS → EICHERMOT | -0.68% | -0.68% |
| 2 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → EICHERMOT | -3.73% | -0.67% |
| 3 | EV_CPI_REACCEL_SEP26 ⇒ F_CPI_IN → F_REPO_IN → F_AUTO_DEMAND_IN → EICHERMOT | -0.67% | -0.67% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → EICHERMOT | -3.00% | -0.66% |
| 2 | EV_UST_SELLOFF_SEP26 ⇒ F_DXY → F_FPI_FLOWS → EICHERMOT | -0.64% | -0.64% |
| 2 | EV_PRECIOUS_METALS_CRASH_2026 ⇒ F_DXY → F_FPI_FLOWS → EICHERMOT | -0.62% | -0.62% |

## Analyst profile (agent research, sourced)
# Eicher Motors Ltd. (EICHERMOT) — Market Impact profile, 2026-11-05

## Business
Eicher owns Royal Enfield (RE), the global leader in 250-750cc motorcycles, and 50% of VECV, its heavy-vehicle joint venture with Volvo. RE earns an operating margin of 24-25% with almost no debt, and treasury income of Rs 2,260 cr lifts profit above operations. Exports are about 12-14% of RE volumes (UK, Europe, LatAm, ASEAN, Nepal, Bangladesh). Q1 FY27 sales were Rs 6,632 cr (+31% y/y) with PAT Rs 1,463 cr. September RE sales were 133,958 (+8%) and October motorcycles +7%, while VECV sales jumped 35% in October.

## What moves the stock (ranked)
1. **Domestic mid-premium demand (+4.5 per +10% industry volumes)** and RE's own launches/pricing.
2. **Discount rate / flows**: P/E 36; FIIs hold 24% (G-sec -1.0; F_FPI_FLOWS +2.0).
3. **GST policy (+4.0 per further cut)**: the 350cc threshold under GST 2.0 is crucial; reclassification is both an upside and a risk.
4. **Cost inputs**: steel (-0.7), aluminium (-0.3), where pass-through is partial.
5. **Competition (-2.5)** from Bajaj-Triumph, Honda, Hero-Harley and TVS.
6. **VECV cycle (+0.8)** via government capex and freight.
7. **Rates (-0.6), FX (+0.3), Brent (-0.4).**

## Transmission examples
- **Rate chain (3 orders).** Inflation from Brent $95+ -> RBI hikes to 5.50% (7 Oct) -> RE buyers' EMIs rise (60-65% financed) -> ticket sizes and discretionary buying slow -> RE volumes lag; but treasury income rises on higher yields, cushioning EPS.
- **Steel chain (3 orders).** China steel exports / global HRC +20.6% -> domestic steel +4-5% -> RE frame and tank cost up -> EBITDA margin -50bp -> price rise of 1-2% in January -> volumes mildly elastic.
- **GST chain (3 orders).** Government revisits the 40% rate on >350cc -> RE's 650 range falls into 18% -> on-road price -10% on 650s -> mix shifts up; ASP and margin improve.
- **Mideast chain (4 orders).** Hormuz escalation -> Brent >$100 -> INR weaker (94.5) -> exports in INR gain slightly, but petrol prices and CPI rise -> rate cuts delayed -> urban discretionary slows.
- **VECV chain (3 orders).** Govt capex up -> trucking demand -> CV orders -> VECV profit share up (~9% of PAT).

## Current situation
RE grows steadily. Q2 FY27 results were scheduled for 28 October; their numbers were not captured, so Q1 is the latest hard data. After a ~9% drop on 1 October (September sales), the stock recovered +8.8% in a month. Brokerages (Nuvama, Elara) list it among top auto picks. FIIs trimmed from 26.8% to 24.0% across six months.

## Upcoming events
Monthly sales (Dec 1), Q3 results (early Feb), Flying Flea European roll-out, Budget (1 Feb 2027).

## Bull case
Volume growth of 10%+, ASP growth, margin >25%, VECV up-cycle and export expansion with India's UK/EU trade deals.

## Bear case
Rate/cost headwinds, GST reversal, mid-premium competition and a valuation de-rating if growth slows. Limits: Q2 numbers not captured; cost shares and VECV profit share are estimates.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.