# ASIANPAINT — Asian Paints Ltd.
*NIFTY_50 · Consumer Durables · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -0.4%**, **12 months -0.5%** (rank 117 / 114 of 200 for 3m / 12m); beta 0.93
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +22.0%): 3 months 48%, 12 months 52%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -3.2% … P90 +1.1%; plausible 12m relative-return range incl. stock-specific noise: -19.0% … +22.9%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +0.0 pp (model impact -0.1% beta-adjusted vs realised market-adjusted move -8.3%); forward event exposure +0.6% (3m -0.1%; half assumed priced); company-specific events +0.8%

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
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -8.5% | -8.5% | -3.0 | -3.7 | -1.0 | -0.8 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -2.6% | -2.6% | -2.2 | -0.3 | -0.0 | -0.1 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -2.4% | -2.4% | +0.0 | -0.9 | -1.1 | -0.4 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.36 | -5.2% | -1.9% | -1.5 | -2.4 | -0.7 | -0.5 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -1.8% | -1.8% | -1.4 | -0.3 | -0.0 | -0.0 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.58 | +2.9% | +1.7% | +0.9 | +1.4 | +0.4 | +0.3 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -1.7% | -1.7% | +0.0 | -1.3 | -0.4 | -0.0 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +3.0% | +1.5% | +2.5 | +0.4 | +0.1 | +0.1 |
| Gold and silver slump from January 2026 peaks (silver -53%, gold -24%) (`EV_PRECIOUS_METALS_CRASH_2026`) | occurred | 1.00 | -1.4% | -1.4% | +0.0 | -1.1 | -0.3 | +0.0 |
| US waives Russia-oil secondary sanctions/100% tariff threat on buyers incl. India (17 Oct) (`EV_RUSSIA_WAIVER_OCT17`) | occurred | 1.00 | +1.4% | +1.4% | +0.0 | +0.4 | +0.8 | +0.2 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -1.0% | -1.0% | +0.0 | -0.6 | -0.3 | -0.1 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -1.0% | -1.0% | +0.0 | -0.4 | -0.3 | -0.3 |

## Strongest causal chains (1st–4th order)
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → ASIANPAINT | -2.97% | -2.97% |
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_CHEM_FEEDSTOCK → ASIANPAINT | -2.69% | -2.69% |
| 1 | EV_FPI_RECORD_OUTFLOW_26 ⇒ F_FPI_FLOWS → ASIANPAINT | -2.20% | -2.20% |
| 1 | EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26 ⇒ F_GSEC_10Y_IN → ASIANPAINT | -1.40% | -1.40% |
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → ASIANPAINT | +2.50% | +1.25% |
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_USDINR → ASIANPAINT | -0.70% | -0.70% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → ASIANPAINT | -1.50% | -0.54% |
| 3 | EV_CPI_REACCEL_SEP26 ⇒ F_CPI_IN → F_REPO_IN → F_GSEC_10Y_IN → ASIANPAINT | -0.52% | -0.52% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → ASIANPAINT | +0.90% | +0.52% |
| 3 | EV_CPI_REACCEL_SEP26 ⇒ F_CPI_IN → F_REPO_IN → F_HOUSING_DEMAND → ASIANPAINT | -0.52% | -0.52% |
| 1 | EV_US_MIDTERMS_DEM_SWEEP ⇒ F_FPI_FLOWS → ASIANPAINT | +0.50% | +0.50% |
| 3 | EV_RUSSIA_WAIVER_OCT17 ⇒ C_RUSSIA → F_BRENT → F_CHEM_FEEDSTOCK → ASIANPAINT | +0.49% | +0.49% |
| 2 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → F_CHEM_FEEDSTOCK → ASIANPAINT | -1.36% | -0.49% |
| 2 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → F_CHEM_FEEDSTOCK → ASIANPAINT | +0.82% | +0.47% |
| 2 | EV_UST_SELLOFF_SEP26 ⇒ F_US_10Y → F_GSEC_10Y_IN → ASIANPAINT | -0.44% | -0.44% |

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