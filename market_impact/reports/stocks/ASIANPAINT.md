# ASIANPAINT — Asian Paints Ltd.
*NIFTY_50 · Consumer Durables · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -0.3%**, **12 months -0.5%** (rank 114 / 110 of 200 for 3m / 12m); beta 0.93
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +22.0%): 3 months 49%, 12 months 60%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -1.3% … P90 +0.7%; plausible 12m relative-return range incl. stock-specific noise: -18.8% … +15.4%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +0.0 pp (model impact -0.2% beta-adjusted vs realised market-adjusted move -8.3%); forward event exposure +0.3% (3m +0.1%; half assumed priced); company-specific events +0.8%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -3.05 | +0.00 | -0.72 | -1.82 | -0.50 | — |
| Consumer durables category promotional / discount intensity (`NEW_CONSUMER_DURABLES_PRICE_WAR`) | +1 pp of industry-wide margin given up (discounts, channel incentives, ad spend) in room AC and appliances | -2.50 | -2.50 | +0.00 | +0.00 | +0.00 | — |
| Residential real-estate sales (`F_HOUSING_DEMAND`) | +10% sales volume | +2.05 | +2.00 | +0.00 | +0.04 | +0.01 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -1.97 | +0.00 | -0.71 | -0.95 | -0.32 | — |
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +1.89 | +1.80 | +0.00 | +0.14 | -0.05 | — |
| Brent crude oil price (`F_BRENT`) | +10% Brent | -1.62 | -0.60 | -0.75 | -0.15 | -0.12 | +0.0% |
| Chemical feedstock (benzene, propylene, etc.) (`F_CHEM_FEEDSTOCK`) | +10% feedstock | -1.60 | -1.60 | +0.00 | +0.00 | +0.00 | — |
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | +1.56 | +1.40 | +0.00 | +0.22 | -0.06 | — |
| OPEC+ crude supply decisions (`NEW_OPEC_PLUS_SUPPLY`) | +1 mb/d OPEC+ production (quota/actual) | +1.48 | +0.00 | +0.38 | +0.90 | +0.20 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -1.43 | -0.90 | -0.16 | -0.18 | -0.19 | -1.1% |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +1.37 | +0.00 | +0.89 | +0.13 | +0.36 | — |
| India 10-year G-sec yield (`F_GSEC_10Y_IN`) | +25 bp yield | -1.24 | -1.00 | -0.24 | +0.00 | +0.00 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +1.17 | +1.00 | +0.12 | +0.02 | +0.02 | — |
| Russia-Ukraine war / Western sanctions intensity on Russia (`NEW_RUSSIA_UKRAINE_WAR`) | +1 = escalation (new sanctions round, strikes on energy/port infrastructure); -1 = ceasefire/sanctions relief | -1.15 | +0.00 | -0.24 | -0.62 | -0.28 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -2.6% | -2.6% | -2.2 | -0.3 | -0.0 | -0.1 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -2.4% | -2.4% | +0.0 | -0.9 | -1.1 | -0.4 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -1.8% | -1.8% | -1.4 | -0.3 | -0.0 | -0.0 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +3.0% | +1.5% | +2.5 | +0.4 | +0.1 | +0.1 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.55 | +2.5% | +1.4% | +0.8 | +1.2 | +0.3 | +0.3 |
| US waives Russia-oil secondary sanctions/100% tariff threat on buyers incl. India (17 Oct) (`EV_RUSSIA_WAIVER_OCT17`) | occurred | 1.00 | +1.4% | +1.4% | +0.0 | +0.4 | +0.8 | +0.2 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.25 | -4.6% | -1.1% | -1.3 | -2.1 | -0.6 | -0.5 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -1.0% | -1.0% | +0.0 | -0.6 | -0.3 | -0.1 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -1.0% | -1.0% | +0.0 | -0.4 | -0.3 | -0.3 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -1.0% | -1.0% | +0.0 | -0.8 | -0.2 | -0.0 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -0.9% | -0.9% | -0.3 | -0.6 | -0.0 | -0.1 |
| Risk: USD/INR >98 and/or reserves < US$650bn (disorderly rupee, emergency RBI response) (`EV_RUPEE_BREAK_98_RESERVE_STRESS`) | risk_scenario | 0.18 | -4.6% | -0.8% | -3.7 | -0.8 | -0.1 | +0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → ASIANPAINT | +2.50% | +1.25% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → ASIANPAINT | +0.78% | +0.43% |
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → ASIANPAINT | -0.80% | -0.40% |
| 2 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → F_CHEM_FEEDSTOCK → ASIANPAINT | +0.71% | +0.39% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → ASIANPAINT | -1.32% | -0.33% |
| 1 | EV_CPI_BREACH_6PCT ⇒ F_GSEC_10Y_IN → ASIANPAINT | -0.50% | -0.30% |
| 2 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → F_CHEM_FEEDSTOCK → ASIANPAINT | -1.20% | -0.30% |
| 1 | EV_BUDGET27_AGRI_RURAL ⇒ F_RURAL_DEMAND → ASIANPAINT | +0.42% | +0.29% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → ASIANPAINT | -1.50% | -0.27% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → ASIANPAINT | -0.96% | -0.24% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_FPI_FLOWS → ASIANPAINT | -0.96% | -0.24% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → ASIANPAINT | -0.93% | -0.23% |
| 1 | EV_RURAL_RELIEF_PACKAGE ⇒ F_RURAL_DEMAND → ASIANPAINT | +0.42% | +0.23% |
| 2 | EV_NBS_RABI_HIKE ⇒ P_FERT_SUBSIDY → F_GSEC_10Y_IN → ASIANPAINT | -0.24% | -0.23% |
| 2 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_RURAL_DEMAND → ASIANPAINT | +0.32% | +0.22% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_FPI_FLOWS → ASIANPAINT | -1.60 | events | -1.60% |
| 1 | F_GSEC_10Y_IN → ASIANPAINT | +1.55 | director_override | -1.55% |
| 2 | F_REPO_IN → F_HOUSING_DEMAND → ASIANPAINT | +1.00 | events | -0.42% |
| 2 | F_GSEC_10Y_IN → F_HOUSING_DEMAND → ASIANPAINT | +1.55 | director_override | -0.37% |
| 1 | F_URBAN_DEMAND → ASIANPAINT | +0.20 | events | +0.36% |
| 1 | F_RURAL_DEMAND → ASIANPAINT | -0.25 | events | -0.35% |
| 1 | F_USDINR → ASIANPAINT | -0.37 | observed | +0.33% |
| 2 | F_GDP_IN → F_HOUSING_DEMAND → ASIANPAINT | +0.50 | events | +0.24% |
| 2 | T_GENAI_SERVICES → F_HOUSING_DEMAND → ASIANPAINT | +1.00 | events | -0.16% |
| 2 | P_ANTI_DUMPING_IN → F_CHEM_FEEDSTOCK → ASIANPAINT | +0.40 | events | -0.13% |
| 2 | F_STEEL_INDIA → F_HOUSING_DEMAND → ASIANPAINT | +1.35 | events | -0.11% |
| 1 | F_BRENT → ASIANPAINT | +0.00 | observed | -0.00% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-11 | Interim dividend Rs5.75/share: ex-date/record date reached in early Nov (stock rose 2.7% on 3 Nov ahead of ex-date); exact dates not verified | corporate_action | 0.95 | -0.2% | -0.24% |
| 2026-12 | Further list-price increase / festive promotions: raw-material inflation passthrough decision; Birla Opus reaction | guidance | 0.40 | +2.5% | +1.00% |
| 2026-12 | Leo Puri (ex-JPMorgan) named next chairman (announced 2026-09-08); effective date not verified | corporate_action | 0.60 | +0.0% | +0.00% |
| 2027-01 | Q3 FY27 results (date not announced; historically mid/late Jan). Watch gross margin recovery after price increases and decorative volume vs 8-10% guidance | results | 0.95 | +0.0% | +0.00% |

## Analyst profile (agent research, sourced)
# ASIANPAINT - Asian Paints Ltd. (Nifty 50, paints / home decor)

## Business
India's largest decorative paint company, ~85% decorative India (urban ~60%, repaint ~70% of demand), ~9% international, small industrial and home-decor arms (mix approximate, model knowledge). Raw materials are ~60% of sales: TiO2, monomers, resins, solvents, additives, packaging. The company is net cash, P/E ~49, ROCE ~26%.

## What moves the stock (ranked, scenario weights per standard shock in % equity value)
1. **Competition / promotional intensity (NEW_CONSUMER_DURABLES_PRICE_WAR, -2.5 per +1pp):** Grasim's Birla Opus and others are buying share with dealer incentives. Q2 FY27 PBDIT margin fell 202bp to 15.6%.
2. **Chemical / petrochemical feedstock (-1.6 per +10%):** Q2 gross margin fell 349bp to 39.6% on raw-material inflation; price/mix of ~8% only partly offset it.
3. **Housing and repaint demand (+2.0 housing, +1.8 urban, +1.4 rural):** decorative volume grew 6.4% in Q2, below the 8-10% FY27 range cited by one aggregator.
4. **Discount rate (-1.0 per +25bp G-sec):** long-duration stock.
5. **USD/INR (-0.9 per +3%) and Brent direct (-0.6 per +10%).**
6. FII flows (+1.0), international (+0.3).

## Transmission examples
- **Middle East escalation -> Brent up -> naphtha/propylene/benzene up (2nd) -> monomer, solvent and resin prices up (3rd) -> Asian Paints gross margin down 100-150bp with a 1-2 quarter lag until list prices rise (4th).** Then the price hike dampens volumes in a 6.4%-volume market, and competitors with deeper pockets (Birla Opus) may not follow, which stretches the margin dip.
- **Brent up -> INR weaker (India imports ~85% of crude) -> imported TiO2 and additives dearer and RBI holds rates -> housing finance costlier -> new-construction and repaint demand softer (3rd) -> decorative volumes lower (4th).**
- **China chemical exports up (price cuts) -> TiO2 and resin prices down -> margin tailwind in 2-3 quarters; offset if the cheaper input also funds competitor discounting.**
- **Strong FPI inflows -> large-cap quality premium rebuilt (stock held 13.8% FII, rising) -> re-rating independent of fundamentals.**

## Current situation
Q2 FY27 (reported 2026-10-29): sales Rs9,954cr (+16.9%), volume +6.8%, PAT ~Rs1,068cr (+7.5%), interim dividend Rs5.75. Brokerages trimmed targets (Rs2,808-2,925) and see FY27 margin pressure. Price Rs2,525 (3m -8.3%, 12m +1.6%). The pack's empirical betas (DXY -2.29, t=-3.1; Brent -0.94, t=-2.3) agree in sign with the model; the silver/gold positive betas (t~2-2.7) have no fundamental link and are ignored.

## Upcoming
Q3 FY27 results ~Jan 2027; possible further price hikes; chairman transition (Leo Puri named Sep 2026, effective date unverified); dividend ex-date passed/passing in early Nov.

## Bull case
Feedstock eases (Brent -5.6% 1m), Birla Opus rationalises, festive volumes beat; gross margin recovers toward 42%+; de-rated multiple expands.

## Bear case
Crude/TiO2 rebound plus rupee at 94.5 and a prolonged discounting war leave PBDIT margin in the mid-teens, volume stays at ~6%, and the 49x multiple compresses.

Uncertainties: segment mix and rural/urban splits are approximate model knowledge; earnings-call commentary not verified from a transcript.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.