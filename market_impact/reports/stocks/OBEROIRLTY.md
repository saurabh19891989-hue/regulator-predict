# OBEROIRLTY — Oberoi Realty Ltd.
*MIDCAP_100 · Realty · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +0.1%**, **12 months +0.1%** (rank 92 / 91 of 200 for 3m / 12m); beta 1.22
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +23.7%): 3 months 50%, 12 months 49%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -3.0% … P90 +1.8%; plausible 12m relative-return range incl. stock-specific noise: -29.2% … +31.1%
- Decomposition (12m): 0.5 × forward event exposure -1.4% (3m -0.6%; half assumed priced; market-priced macro drift removed) + 0.5 × company-specific catalysts +1.9%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply -3.6% (beta-adjusted) vs a realised market-adjusted move of +0.2% — gap -3.8 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## Where the expected return comes from
Market-priced macro drivers (rates, FX, commodities, indices, volatility, flows, growth, inflation) are taken as priced, so what is left is policy, regulatory, sector, theme, geopolitical and company-specific exposure — where 2nd–4th-order effects are most likely to be missed. Percentage points of the expected relative return.
| source | 12m: 1st order | 12m: 2nd–4th order | 12m total | 3m total |
|---|---|---|---|---|
| Policy | +0.09 | -0.02 | +0.07 | +0.03 |
| Regulatory | +0.00 | -0.02 | -0.02 | -0.00 |
| Sector | -0.07 | +0.06 | -0.01 | +0.01 |
| Theme | +0.00 | -0.01 | -0.01 | -0.01 |
| Geopolitics | +0.00 | -0.02 | -0.02 | -0.02 |
| Company catalysts | +0.95 | +0.00 | +0.95 | +0.50 |
| Market-priced macro | +0.00 | -0.00 | -0.00 | -0.00 |
| Beta adjustment | — | — | -0.70 | -0.32 |
| Universe centring | — | — | -0.15 | -0.10 |
| **Expected relative return** | | | **+0.12** | **+0.09** |

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Residential real-estate sales (`F_HOUSING_DEMAND`) | +10% sales volume | +3.50 | +3.50 | +0.00 | -0.00 | +0.00 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -3.29 | -2.50 | -0.69 | -0.06 | -0.05 | — |
| Consumer premiumisation (`T_PREMIUMISATION`) | +1 | +2.62 | +2.50 | +0.10 | +0.01 | +0.01 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -2.59 | +0.00 | -2.00 | -0.52 | -0.07 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +2.10 | +2.00 | +0.02 | +0.04 | +0.04 | — |
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +1.69 | +1.50 | +0.16 | +0.12 | -0.09 | — |
| Affordable-housing / home-loan support (`P_HOUSING_POLICY`) | +1 = stronger support | +1.56 | +1.00 | +0.56 | +0.00 | -0.00 | — |
| Capital-gains / securities tax burden (`P_CAPITAL_GAINS_TAX`) | +1 = higher | -1.47 | -1.00 | -0.45 | -0.01 | -0.01 | — |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +1.46 | +0.00 | +0.76 | +0.50 | +0.21 | — |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -1.41 | +0.00 | +0.00 | -1.10 | -0.31 | — |
| India 10-year G-sec yield (`F_GSEC_10Y_IN`) | +25 bp yield | -1.34 | -1.20 | -0.14 | +0.00 | +0.00 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -1.23 | +0.00 | -0.06 | -0.51 | -0.66 | — |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -1.13 | +0.00 | -0.71 | -0.38 | -0.04 | +3.5% |
| USD/JPY exchange rate (`NEW_USDJPY`) | +3% USD/JPY (yen weaker) | +0.82 | +0.00 | +0.48 | +0.19 | +0.14 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -4.6% | -4.6% | -4.4 | -0.0 | -0.1 | -0.1 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -3.4% | -3.4% | -2.9 | -0.5 | -0.0 | -0.1 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -3.0% | -3.0% | +0.0 | -2.3 | -0.6 | -0.1 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +5.2% | +2.6% | +5.0 | +0.0 | +0.1 | +0.1 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -1.9% | -1.9% | -1.7 | -0.2 | -0.0 | -0.0 |
| RBI MPC Dec 2026 (~4 Dec): hikes repo another 25 bp to 5.75% (`EV_RBI_DEC26_HIKE25`) | scheduled | 0.42 | -3.4% | -1.4% | -2.9 | -0.5 | -0.0 | -0.1 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -1.3% | -1.3% | +0.0 | -1.1 | -0.2 | +0.0 |
| Risk: USD/INR >98 and/or reserves < US$650bn (disorderly rupee, emergency RBI response) (`EV_RUPEE_BREAK_98_RESERVE_STRESS`) | risk_scenario | 0.18 | -7.0% | -1.3% | -6.3 | -0.6 | -0.0 | -0.0 |
| US midterms (3 Nov 2026): Democrats win House and Senate (`EV_US_MIDTERMS_DEM_SWEEP`) | occurred | 1.00 | +1.1% | +1.1% | +1.0 | +0.1 | +0.0 | +0.0 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.25 | -4.1% | -1.0% | +0.0 | -4.0 | -0.2 | +0.1 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -0.9% | -0.9% | +0.0 | -1.0 | -0.0 | +0.1 |
| RBI MPC Feb 2027 (~5 Feb, just after Budget): hikes 25 bp (`EV_RBI_FEB27_HIKE25`) | scheduled | 0.27 | -3.4% | -0.9% | -2.9 | -0.5 | -0.0 | -0.1 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → OBEROIRLTY | +5.00% | +2.50% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → OBEROIRLTY | -2.50% | -1.05% |
| 1 | EV_RBI_FEB27_HIKE25 ⇒ F_REPO_IN → OBEROIRLTY | -2.50% | -0.68% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → OBEROIRLTY | -3.00% | -0.54% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → OBEROIRLTY | -1.92% | -0.48% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_FPI_FLOWS → OBEROIRLTY | -1.92% | -0.48% |
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → OBEROIRLTY | -0.96% | -0.48% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → OBEROIRLTY | -1.87% | -0.47% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_REPO_IN → OBEROIRLTY | -2.50% | -0.45% |
| 1 | EV_BUDGET_FY28_LTCG_RELIEF ⇒ F_FPI_FLOWS → OBEROIRLTY | +1.00% | +0.35% |
| 1 | EV_Q2_FY27_GDP_STRONG ⇒ F_FPI_FLOWS → OBEROIRLTY | +0.40% | +0.32% |
| 1 | EV_INDIA_STAGFLATION_SCARE ⇒ F_REPO_IN → OBEROIRLTY | -2.50% | -0.30% |
| 2 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → OBEROIRLTY | -1.87% | -0.28% |
| 1 | EV_RBI_APR27_CUT25 ⇒ F_REPO_IN → OBEROIRLTY | +2.50% | +0.25% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_FED_FUNDS → F_REPO_IN → OBEROIRLTY | +0.90% | +0.23% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_FPI_FLOWS → OBEROIRLTY | -1.60 | events | -3.20% |
| 1 | F_REPO_IN → OBEROIRLTY | +1.00 | events | -2.50% |
| 1 | F_GSEC_10Y_IN → OBEROIRLTY | +1.55 | director_override | -1.86% |
| 1 | F_STEEL_INDIA → OBEROIRLTY | +1.35 | events | -0.54% |
| 2 | F_GDP_IN → F_HOUSING_DEMAND → OBEROIRLTY | +0.50 | events | +0.42% |
| 2 | F_REPO_IN → F_HOUSING_DEMAND → OBEROIRLTY | +1.00 | events | -0.36% |
| 1 | F_URBAN_DEMAND → OBEROIRLTY | +0.20 | events | +0.30% |
| 1 | F_US_TECH_SPEND → OBEROIRLTY | -0.60 | events | -0.24% |
| 2 | F_GSEC_10Y_IN → F_HOUSING_DEMAND → OBEROIRLTY | +1.55 | director_override | -0.21% |
| 2 | T_GENAI_SERVICES → F_HOUSING_DEMAND → OBEROIRLTY | +0.50 | director_override | -0.14% |
| 1 | F_USDINR → OBEROIRLTY | -0.37 | observed | -0.11% |
| 2 | F_STEEL_INDIA → F_HOUSING_DEMAND → OBEROIRLTY | +1.35 | events | -0.09% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-11 | Second interim dividend Rs 2/share record/payment (declared 2026-10-16); mechanical price adjustment ~0.1% | corporate_action | 0.95 | +0.0% | +0.00% |
| 2026-12/2027-06 | First Delhi-NCR land/JD deal announcement | capex | 0.35 | +1.5% | +0.52% |
| 2027-01 | Q3 FY27 results (model-estimated from Q2 on 2026-10-16) | results | 0.95 | +0.5% | +0.47% |
| 2027-05 | FY27 results and new-launch pipeline (Thane/Worli/Borivali phases) | guidance | 0.90 | +1.0% | +0.90% |

## Analyst profile (agent research, sourced)
# Oberoi Realty (OBEROIRLTY) - profile as of 2026-11-05

## Business
Oberoi Realty is the most conservatively financed developer in the Nifty 200 realty group. It builds ultra-luxury and premium housing in Mumbai (Worli, Goregaon, Borivali, Thane, Mulund), owns annuity assets (Commerz offices, Oberoi Mall, Oberoi Garden City) and hotels. Interest cost is only Rs 205 crore TTM versus operating profit of Rs 3,560 crore (about 57% margin), so rate-driven financing risk is small; rate risk is demand and valuation, not interest cost. Q2 FY27 PAT was about Rs 762 crore (flat) on revenue down 6%, while pre-sales beat Nomura's estimates (Moneycontrol, 2026-10-19). The company declared a Rs 2 second interim dividend (2026-10-16) and said it is open to land buys and joint development across Delhi-NCR (Business Standard, 2026-10-19).

## What moves the stock
1. **Mumbai housing volumes (+3.5 per +10%)**; luxury demand is wealth-driven, so less rate-elastic than mid-segment names.
2. **Repo (-2.5 per +25 bp)** after the RBI's hike to 5.50% on 2026-10-07; beta is only about 1.3, the lowest in the group.
3. **Premiumisation (+2.5)** and **G-sec yields (-1.2)** via cap rates on the annuity book.
4. FPI/DII flows (+2.0, +0.8), urban demand (+1.5), travel/hotels (+0.5), NRI remittances (+0.4), US tech spend (+0.4), policy (housing +1.0, capital gains -1.0), costs (steel -0.4, cement -0.3, wages -0.3).
The pack shows wheat (+1.8, t=2.1) and edible oil (+2.45, t=1.9) co-movement; no mechanism links them, so they are ignored as spurious.

## Transmission examples
- **Rates (4 orders)**: oil at $95 -> CPI up and rupee weak -> RBI hikes again -> G-sec 10y rises -> cap rates on Commerz/Oberoi Mall widen and luxury buyers' mortgages cost more -> NAV -2 to -4% and pre-sales slow modestly.
- **Equity wealth (3 orders)**: strong Nifty and FPI inflows -> HNI wealth up -> Worli/Sky City sales -> pre-sales beat (as in Q2) -> operating leverage at 57% margins.
- **Tech/office (4 orders)**: US tech slowdown -> Mumbai BFSI/IT hiring weaker -> Commerz leasing -> lower rental growth.
- **Costs (3 orders)**: steel/cement up -> construction cost +0.3% of revenue; minor given high margins.

## Current situation
Earnings flat, valuation lowest of the realty peers (P/E 24), strong balance sheet, six sell-side Buy calls with TPs near Rs 2,100. The stock is range-bound (12m -2%, 1m -0.4%) while peers rallied after the hike.

## Upcoming
Q3 FY27 (about January 2027), December MPC, first NCR deal (prob ~0.35 within the horizon), new phase launches.

## Bull / Bear
Bull: pre-sales beats convert to revenue, NCR deal adds growth, capital return. Bear: Mumbai luxury sales falter under higher rates; revenue remains lumpy. Confidence medium; segment NAV weights are model estimates.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.