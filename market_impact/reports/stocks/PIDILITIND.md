# PIDILITIND — Pidilite Industries Ltd.
*NIFTY_NEXT_50 · Chemicals · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -1.4%**, **12 months -1.8%** (rank 140 / 128 of 200 for 3m / 12m); beta 0.89
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +13.2%): 3 months 42%, 12 months 38%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -6.8% … P90 +0.8%; plausible 12m relative-return range incl. stock-specific noise: -28.7% … +19.6%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves -0.3 pp (model impact -0.6% beta-adjusted vs realised market-adjusted move +2.7%); forward event exposure -0.7% (3m -1.1%; half assumed priced); company-specific events +0.1%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -3.04 | -1.50 | -0.60 | -0.65 | -0.28 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -2.86 | +0.00 | -2.33 | -0.28 | -0.25 | — |
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +2.34 | +2.50 | +0.00 | -0.11 | -0.05 | — |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +2.27 | +1.50 | +0.51 | +0.31 | -0.04 | — |
| Consumer premiumisation (`T_PREMIUMISATION`) | +1 | +2.09 | +2.00 | +0.10 | +0.00 | -0.01 | — |
| Brent crude oil price (`F_BRENT`) | +10% Brent | -1.86 | -1.00 | -0.57 | -0.22 | -0.07 | +0.0% |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -1.83 | -1.50 | -0.22 | -0.10 | -0.01 | — |
| OPEC+ crude supply decisions (`NEW_OPEC_PLUS_SUPPLY`) | +1 mb/d OPEC+ production (quota/actual) | +1.60 | +0.00 | +0.64 | +0.68 | +0.28 | — |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -1.51 | +0.00 | -0.10 | -1.28 | -0.13 | — |
| Residential real-estate sales (`F_HOUSING_DEMAND`) | +10% sales volume | +1.46 | +1.50 | +0.00 | -0.05 | +0.01 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -1.46 | -1.00 | -0.12 | -0.25 | -0.08 | -1.1% |
| Chemical feedstock (benzene, propylene, etc.) (`F_CHEM_FEEDSTOCK`) | +10% feedstock | -1.24 | -1.20 | -0.05 | +0.01 | +0.00 | — |
| Russia-Ukraine war / Western sanctions intensity on Russia (`NEW_RUSSIA_UKRAINE_WAR`) | +1 = escalation (new sanctions round, strikes on energy/port infrastructure); -1 = ceasefire/sanctions relief | -1.21 | +0.00 | -0.40 | -0.53 | -0.28 | — |
| Russia (oil discounts, defence, sanctions) (`C_RUSSIA`) | +1 = closer trade access / larger discounts | +1.10 | +0.00 | +0.48 | +0.43 | +0.19 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -11.5% | -11.5% | -7.2 | -2.8 | -1.1 | -0.4 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -3.4% | -3.4% | +0.0 | -2.8 | -0.3 | -0.3 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.58 | +4.5% | +2.6% | +3.0 | +0.9 | +0.4 | +0.2 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.36 | -6.9% | -2.5% | -4.3 | -1.6 | -0.7 | -0.3 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -1.9% | -1.9% | -1.5 | -0.3 | -0.0 | -0.0 |
| US waives Russia-oil secondary sanctions/100% tariff threat on buyers incl. India (17 Oct) (`EV_RUSSIA_WAIVER_OCT17`) | occurred | 1.00 | +1.3% | +1.3% | +0.0 | +0.5 | +0.5 | +0.2 |
| Hormuz effectively closed for >2 weeks (Brent > $150) (`EV_HORMUZ_FULL_CLOSURE`) | risk_scenario | 0.06 | -16.0% | -1.0% | -9.8 | -3.8 | -1.7 | -0.8 |
| US Q3 data: GDP 3.4%, CPI 3.7%, September payrolls only +29k (`EV_US_Q3_DATA_MIXED`) | occurred | 1.00 | -0.9% | -0.9% | +0.0 | -0.4 | -0.4 | -0.1 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -0.8% | -0.8% | +0.0 | -0.5 | -0.2 | -0.2 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -0.8% | -0.8% | +0.0 | -0.3 | +0.1 | -0.6 |
| Risk: USD/INR >98 and/or reserves < US$650bn (disorderly rupee, emergency RBI response) (`EV_RUPEE_BREAK_98_RESERVE_STRESS`) | risk_scenario | 0.22 | -3.5% | -0.8% | -2.8 | -0.6 | -0.1 | +0.0 |
| RBI MPC Dec 2026 (~4 Dec): hikes repo another 25 bp to 5.75% (`EV_RBI_DEC26_HIKE25`) | scheduled | 0.40 | -1.9% | -0.8% | -1.5 | -0.3 | -0.0 | -0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → PIDILITIND | -2.50% | -0.89% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ C_MIDEAST_CONFLICT → PIDILITIND | +1.50% | +0.87% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → PIDILITIND | +1.50% | +0.87% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ C_MIDEAST_CONFLICT → PIDILITIND | -1.80% | -0.64% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → PIDILITIND | -1.50% | -0.60% |
| 2 | EV_PULSES_VEG_SPIKE_WINTER ⇒ F_CPI_IN → F_REPO_IN → PIDILITIND | -1.73% | -0.43% |
| 1 | EV_RBI_FEB27_HIKE25 ⇒ F_REPO_IN → PIDILITIND | -1.50% | -0.41% |
| 1 | EV_HORMUZ_FULL_CLOSURE ⇒ F_BRENT → PIDILITIND | -6.00% | -0.38% |
| 2 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → F_CHEM_FEEDSTOCK → PIDILITIND | -1.02% | -0.36% |
| 1 | EV_CPI_BREACH_6PCT ⇒ F_REPO_IN → PIDILITIND | -0.60% | -0.36% |
| 2 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → F_CHEM_FEEDSTOCK → PIDILITIND | +0.61% | +0.36% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_REPO_IN → PIDILITIND | -1.50% | -0.33% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_USDINR → PIDILITIND | -1.30% | -0.29% |
| 1 | EV_BUDGET27_AGRI_RURAL ⇒ F_RURAL_DEMAND → PIDILITIND | +0.36% | +0.25% |
| 3 | EV_WHEAT27_CROP_BELOW ⇒ F_FOOD_INFLATION_IN → F_CPI_IN → F_REPO_IN → PIDILITIND | -0.38% | -0.25% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | C_MIDEAST_CONFLICT → PIDILITIND | +1.50 | events | -2.25% |
| 1 | F_REPO_IN → PIDILITIND | +1.00 | events | -1.50% |
| 2 | F_GSEC_10Y_IN → F_HOUSING_DEMAND → PIDILITIND | +1.70 | events | -0.61% |
| 1 | F_URBAN_DEMAND → PIDILITIND | +0.20 | events | +0.50% |
| 1 | F_USDINR → PIDILITIND | -0.37 | observed | +0.37% |
| 1 | F_RURAL_DEMAND → PIDILITIND | -0.25 | events | -0.30% |
| 2 | F_GDP_IN → F_HOUSING_DEMAND → PIDILITIND | +0.50 | events | +0.18% |
| 2 | F_REPO_IN → F_HOUSING_DEMAND → PIDILITIND | +1.00 | events | -0.16% |
| 2 | T_GENAI_SERVICES → F_HOUSING_DEMAND → PIDILITIND | +1.00 | events | -0.12% |
| 2 | F_STEEL_INDIA → F_HOUSING_DEMAND → PIDILITIND | +1.65 | events | -0.10% |
| 2 | P_ANTI_DUMPING_IN → F_CHEM_FEEDSTOCK → PIDILITIND | +0.40 | events | -0.10% |
| 2 | F_USDCNY → F_CHINA_CHEM_EXPORTS → PIDILITIND | -0.47 | observed | -0.07% |

## Analyst profile (agent research, sourced)
# PIDILITIND — Pidilite Industries (Nifty Next 50, as of 2026-11-05)

## Business
Pidilite makes Fevicol, Fevikwik, M-Seal, Dr. Fixit, Araldite, Roff and Fevicryl. Consumer & Bazaar (C&B) is about 80% of sales and Business-to-Business (industrial adhesives, resins, pigments) about 21%. International subsidiaries are roughly 14% of revenue. The franchise rests on mass distribution through hardware and carpentry channels, dominant brands and premiumisation. Q2 FY27 (reported 28 Oct 2026) delivered revenue of Rs 4,298 cr (+20.9%) on underlying volume growth of 11.1% (C&B) and 9.2% (B2B), but gross margin fell about 640 bp to 48.6% and EBITDA margin to 20.4% (24% a year ago). PAT was Rs 626 cr (+7.2%). Management guides EBITDA margin to a 20-24% corridor, expects H2 at the higher end, and took price increases of 12-15% in Q1 and 3-5% in October (Yahoo/GuruFocus call summary, CNBC TV18). The company is almost debt free and trades at about 59x trailing earnings.

## What moves the stock, ranked
1. **Petrochemical raw materials (Brent, VAM, epoxy, solvents).** About 44% of sales is petrochemical-linked input. The stock's empirical Brent elasticity is -0.96 per +10% (t -3.1) and the refining-margin elasticity -0.71 (t -2.5), both significant, and they match the fundamental estimate of about -1.0 in the graph. VAM swung from near US$2,000/t to about US$1,000/t in 2026 on West Asia supply, which is why Q2 gross margin cratered while Q1 (low-cost inventory) looked strong.
2. **Valuation and the discount rate.** At 59x earnings, a 25 bp repo move is worth about -1.5% and any margin miss is punished (-3% on the Q2 print).
3. **USD/INR and foreign flows.** Empirical USD/INR -2.32 (t -2.7) and DXY -1.65 (t -2.9). Fundamentally imports are only about 15% of sales, so I attribute roughly half of the empirical number to foreign-flow behaviour in premium-multiple stocks and shrink to -1.0.
4. **Housing, urban and rural demand** (+1.5, +2.5, +1.2 respectively per standard shock), plus premiumisation (+2).
5. **West Asia directly.** MENA subsidiary weakness (working-capital constraints) and weak exports to West Asia, apart from the crude effect (-1.5).

## Transmission examples
- **4th order (energy shock):** Middle East escalation (1st: Brent up) -> VAM, acrylic, solvent and freight costs rise (2nd) -> Pidilite takes price increases but can only recover about 70% in 1-2 quarters, and absorbing the rest takes gross margin from about 55% toward 48% (3rd) -> EBITDA margin drops to the bottom of the 20-24% corridor and the 59x multiple compresses (4th). This is exactly what happened in Q2 FY27.
- **Macro chain:** Brent up -> INR weaker (oil importer) -> RBI holds or hikes -> housing finance costlier -> new-home and renovation volumes slow -> Fevicol/Dr. Fixit volumes decelerate from 11% UVG. This second path hits volumes six to nine months later.
- **Easing chain:** Brent down -> VAM down -> Pidilite passes rebates to trade selectively (as management said in July) rather than cutting list prices -> gross margin rebuilds faster than revenue growth falls, which is the Q3-Q4 upside setup.
- **China chain:** Chinese chemical exports surge -> epoxy/acrylic input prices fall (positive) but cheaper imported adhesives appear in the bazaar (negative, small).

## Current situation
Q2 missed on EBITDA (Rs 877 cr vs poll Rs 942 cr) and margin (20.4% vs 22.2%) but beat on revenue. CNBC reports advertising spend of Rs 141 cr and calls it a 12.6% decline, yet quotes Rs 123 cr for the year-ago quarter, so the direction is unclear; any cut would flatter margin. Management said "steady margins in H1" and confidence in H2 momentum; broker Prabhudas Lilladher is Accumulate at Rs 1,600. The CFO transition (Amit Agarwal named CFO-designate, 9 Oct) is a minor governance event. The pack's price (Rs 1,556) conflicts with the CNBC article's "closed at Rs 1,392" statement; I used the pack's Yahoo close and flag the discrepancy as unresolved.

## Upcoming events
Q3 FY27 results in late Jan-Feb 2027 are the key test (probability 0.95, impact roughly -6% to +7%). Selective price cuts if input costs keep easing; the MD's sustained-$100-crude tail risk (prob ~0.15, -2% to -8%).

## Bull case
VAM and crude normalise, price increases stick, gross margin returns toward 52-55% while UVG stays in double digits; EBITDA margin of 23-24% in H2 and FY28 growth of 15-18% justify a premium multiple.

## Bear case
Crude holds above $95-100, MENA stays weak, volumes slow with housing, and margin stays at 20% so that the 59x multiple derates toward 45-50x. Uncertainty: the cost-structure shares are my estimates anchored on reported COGS; I did not find a disclosed raw-material basket.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.