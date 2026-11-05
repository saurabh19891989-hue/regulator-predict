# COLPAL — Colgate Palmolive (India) Ltd.
*MIDCAP_100 · Fast Moving Consumer Goods · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +0.7%**, **12 months +1.4%** (rank 81 / 79 of 200 for 3m / 12m); beta 0.91
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +23.5%): 3 months 52%, 12 months 55%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -0.8% … P90 +4.0%; plausible 12m relative-return range incl. stock-specific noise: -17.0% … +28.9%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +0.6 pp (model impact +1.3% beta-adjusted vs realised market-adjusted move -19.3%); forward event exposure +2.9% (3m +1.4%; half assumed priced); company-specific events +0.9%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Oral-care competition intensity (HUL, Dabur, Patanjali, Himalaya) (`NEW_ORAL_CARE_COMPETITION`) | +1 = materially sharper discounting/advertising by rivals in toothpaste | -3.00 | -3.00 | +0.00 | +0.00 | +0.00 | — |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +2.51 | +2.00 | +0.37 | +0.19 | -0.05 | — |
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | +1.87 | +2.00 | +0.00 | -0.12 | -0.01 | — |
| Consumer premiumisation (`T_PREMIUMISATION`) | +1 | +1.55 | +1.50 | +0.06 | +0.00 | -0.01 | — |
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +1.43 | +1.50 | +0.00 | -0.08 | +0.01 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -1.39 | +0.00 | -0.48 | -0.38 | -0.53 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -1.39 | +0.00 | -1.44 | +0.08 | -0.02 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -1.07 | -1.00 | -0.05 | -0.02 | +0.00 | — |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -0.89 | +0.00 | -0.16 | -0.79 | +0.06 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +0.86 | +0.80 | +0.02 | +0.01 | +0.02 | — |
| Packaging cost (paper, plastics) (`F_PACKAGING`) | +10% packaging cost | -0.80 | -0.80 | +0.00 | +0.00 | +0.00 | — |
| Monsoon rainfall vs normal (`F_MONSOON`) | +10% above long-period average | +0.78 | +0.00 | +0.45 | -0.00 | +0.33 | — |
| Brent crude oil price (`F_BRENT`) | +10% Brent | -0.75 | -0.40 | -0.12 | -0.20 | -0.03 | +0.0% |
| Palm / edible oil price (`F_EDIBLE_OIL`) | +10% edible oils | -0.68 | -0.60 | +0.00 | -0.01 | -0.07 | +1.9% |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -4.0% | -4.0% | -2.0 | -0.6 | -1.1 | -0.2 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -1.9% | -1.9% | -1.8 | -0.1 | -0.0 | -0.1 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -1.8% | -1.8% | +0.0 | -1.8 | +0.1 | -0.0 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +2.2% | +1.1% | +2.0 | +0.1 | +0.0 | +0.1 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -1.1% | -1.1% | -1.0 | -0.1 | -0.0 | -0.0 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -1.0% | -1.0% | +0.0 | -0.6 | +0.0 | -0.4 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.36 | -2.6% | -0.9% | -1.0 | -0.7 | -0.7 | -0.1 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.58 | +1.4% | +0.8% | +0.6 | +0.3 | +0.4 | +0.1 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.28 | -2.5% | -0.7% | +0.0 | -2.1 | -0.3 | -0.1 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -0.6% | -0.6% | +0.0 | -0.6 | -0.1 | +0.0 |
| US waives Russia-oil secondary sanctions/100% tariff threat on buyers incl. India (17 Oct) (`EV_RUSSIA_WAIVER_OCT17`) | occurred | 1.00 | +0.6% | +0.6% | +0.0 | +0.3 | +0.1 | +0.2 |
| Risk: USD/INR >98 and/or reserves < US$650bn (disorderly rupee, emergency RBI response) (`EV_RUPEE_BREAK_98_RESERVE_STRESS`) | risk_scenario | 0.22 | -2.6% | -0.6% | -2.5 | -0.1 | -0.1 | +0.0 |

## Strongest causal chains (1st–4th order)
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → COLPAL | -1.98% | -1.98% |
| 1 | EV_FPI_RECORD_OUTFLOW_26 ⇒ F_FPI_FLOWS → COLPAL | -1.76% | -1.76% |
| 2 | EV_CPI_REACCEL_SEP26 ⇒ F_CPI_IN → F_REPO_IN → COLPAL | -1.32% | -1.32% |
| 1 | EV_RBI_OCT26_HIKE25 ⇒ F_REPO_IN → COLPAL | -1.00% | -1.00% |
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → COLPAL | +2.00% | +1.00% |
| 1 | EV_RURAL_DEMAND_SOFT26 ⇒ F_RURAL_DEMAND → COLPAL | -0.60% | -0.60% |
| 2 | EV_SWMONSOON26_DEFICIT ⇒ F_MONSOON → F_RURAL_DEMAND → COLPAL | -0.57% | -0.57% |
| 3 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_CPI_IN → F_REPO_IN → COLPAL | -0.44% | -0.44% |
| 1 | EV_BUDGET27_AGRI_RURAL ⇒ F_RURAL_DEMAND → COLPAL | +0.60% | +0.42% |
| 1 | EV_US_MIDTERMS_DEM_SWEEP ⇒ F_FPI_FLOWS → COLPAL | +0.40% | +0.40% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → COLPAL | -1.00% | -0.40% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → COLPAL | -1.00% | -0.36% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → COLPAL | +0.60% | +0.35% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → COLPAL | -1.19% | -0.33% |
| 1 | EV_RURAL_RELIEF_PACKAGE ⇒ F_RURAL_DEMAND → COLPAL | +0.60% | +0.33% |

## Analyst profile (agent research, sourced)
# COLPAL (Colgate-Palmolive (India) Ltd.) - company profile as of 2026-11-05

## Business
Colgate-Palmolive India is the leading toothpaste and toothbrush company. It is debt-free with ROCE of 108% and distributes more than 100% of earnings. TTM sales are Rs 6,391 cr (+9%) with EBITDA Rs 1,908 cr (30%). The Sep-26 quarter delivered sales of Rs 1,706 cr (+12%), operating margin of 28% (31% a year earlier) and PAT of Rs 342 cr (+4%), a narrow miss; advertising was stepped up. The stock is Rs 1,688, -23% in 12 months, near its 52-week low of Rs 1,564 (screener.in pack, 2026-11-05). The US parent holds 51%.

## What moves the stock (ranked)
1. **Category volume growth and share versus HUL, Dabur and Patanjali.** Advertising spend rose, taking 3 points off the margin; competition is the largest swing factor.
2. **Rural and urban demand.** Rural is ~40% of sales.
3. **Input costs.** Palm-derived surfactants, packaging and plastics together ~24% of costs.
4. **GST and policy.** The stock rose ~7% on 2026-10-09 after the GST Council meeting, though the Council made no broad rate cuts; the specific trigger was not verified.
5. **Valuation and rates.** A 33x P/E with 2.9% yield makes it a bond proxy.

## Transmission examples
- **Middle East escalation -> Brent up -> polymer packaging and freight up -> gross margin down; also palm oil up -> surfactant and glycerin cost up.** Brent +10% costs ~1.6% of EBITDA; with packaging and palm it can reach 4-5%. Management then raises A&P efficiency or price; volumes soften in rural towns.
- **Brent up -> USD/INR up -> imported intermediates, toothbrushes and royalty cost up** (small, -0.25).
- **Good monsoon -> rural income -> toothpaste penetration and premium trade-up** (+2).
- **Rival launches (HUL, Patanjali) -> Colgate raises A&P -> margin down** (competition).
- **US parent portfolio action -> India sale or restructuring** (low probability tail).

## Current situation
Q2 miss and the A&P step-up triggered the 52-week low on 2026-10-22. Interim dividend Rs 24. FIIs 13.7%, DIIs 15.5%, public 19.8%.

## Upcoming events
Q3 FY27 results (January 2027), dividend record date.

## Bull case
Volume growth recovers to 6-8% with margin back to 31%; yield support and defensive demand.

## Bear case
Share losses continue, A&P stays elevated, margin 26-27% and de-rating to 28x: -15%.

## Uncertainties
Cost shares, revenue mix and rural share are model estimates; filings were not fetched.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.