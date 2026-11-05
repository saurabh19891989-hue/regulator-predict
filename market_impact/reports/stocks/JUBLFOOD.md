# JUBLFOOD — Jubilant Foodworks Ltd.
*MIDCAP_100 · Consumer Services · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -0.3%**, **12 months -0.7%** (rank 145 / 151 of 200 for 3m / 12m); beta 0.98
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +25.7%): 3 months 49%, 12 months 47%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -2.8% … P90 +0.9%; plausible 12m relative-return range incl. stock-specific noise: -34.6% … +32.4%
- Decomposition (12m): 0.5 × forward event exposure -1.4% (3m -0.7%; half assumed priced; market-priced macro drift removed) + 0.5 × company-specific catalysts +0.2%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply -0.8% (beta-adjusted) vs a realised market-adjusted move of +2.2% — gap -3.0 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## Where the expected return comes from
Market-priced macro drivers (rates, FX, commodities, indices, volatility, flows, growth, inflation) are taken as priced, so what is left is policy, regulatory, sector, theme, geopolitical and company-specific exposure — where 2nd–4th-order effects are most likely to be missed. Percentage points of the expected relative return.
| source | 12m: 1st order | 12m: 2nd–4th order | 12m total | 3m total |
|---|---|---|---|---|
| Policy | +0.00 | -0.03 | -0.03 | -0.04 |
| Regulatory | +0.00 | -0.01 | -0.01 | -0.00 |
| Sector | -0.12 | -0.03 | -0.15 | -0.06 |
| Theme | +0.09 | -0.03 | +0.06 | +0.01 |
| Geopolitics | +0.00 | -0.03 | -0.03 | -0.02 |
| Company catalysts | +0.12 | +0.00 | +0.12 | +0.12 |
| Market-priced macro | +0.00 | +0.00 | +0.00 | -0.00 |
| Beta adjustment | — | — | -0.56 | -0.25 |
| Universe centring | — | — | -0.15 | -0.10 |
| **Expected relative return** | | | **-0.74** | **-0.34** |

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +3.88 | +4.00 | +0.00 | -0.08 | -0.04 | — |
| Quick-commerce disruption of retail/FMCG distribution (`T_QUICK_COMMERCE`) | +1 | -3.00 | -3.00 | +0.00 | +0.00 | +0.00 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -2.05 | +0.00 | -2.04 | +0.03 | -0.04 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -2.00 | -1.80 | -0.15 | -0.04 | -0.01 | — |
| Milk / dairy input cost (`F_DAIRY`) | +8% milk procurement price | -1.66 | -1.40 | -0.10 | +0.00 | -0.16 | — |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +1.58 | +0.00 | +1.12 | +0.53 | -0.07 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +1.57 | +1.50 | +0.02 | +0.02 | +0.02 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -1.25 | +0.00 | -0.60 | -0.30 | -0.35 | — |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -1.13 | -0.60 | +0.00 | -0.56 | +0.03 | — |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -0.89 | +0.00 | -0.58 | -0.28 | -0.02 | +3.5% |
| Brent crude oil price (`F_BRENT`) | +10% Brent | -0.86 | -0.50 | -0.11 | -0.21 | -0.04 | +0.0% |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -0.76 | -0.20 | -0.38 | -0.21 | +0.03 | -1.1% |
| Russia-Ukraine war / Western sanctions intensity on Russia (`NEW_RUSSIA_UKRAINE_WAR`) | +1 = escalation (new sanctions round, strikes on energy/port infrastructure); -1 = ceasefire/sanctions relief | -0.74 | +0.00 | -0.58 | -0.13 | -0.03 | — |
| Wheat price (`F_WHEAT`) | +10% wheat | -0.73 | -0.60 | -0.05 | +0.00 | -0.08 | -1.3% |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -3.4% | -3.4% | -3.3 | -0.0 | -0.1 | -0.1 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -3.0% | -3.0% | -0.7 | -2.3 | +0.0 | -0.0 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -2.0% | -2.0% | -1.8 | -0.2 | -0.1 | -0.0 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +3.9% | +2.0% | +3.8 | +0.1 | +0.1 | +0.1 |
| RBI MPC Dec 2026 (~4 Dec): hikes repo another 25 bp to 5.75% (`EV_RBI_DEC26_HIKE25`) | scheduled | 0.42 | -2.0% | -0.8% | -1.8 | -0.2 | -0.1 | -0.0 |
| Risk: USD/INR >98 and/or reserves < US$650bn (disorderly rupee, emergency RBI response) (`EV_RUPEE_BREAK_98_RESERVE_STRESS`) | risk_scenario | 0.18 | -4.7% | -0.8% | -4.3 | -0.2 | -0.3 | +0.0 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.55 | +1.5% | +0.8% | +0.7 | +0.4 | +0.4 | +0.1 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -0.8% | -0.8% | +0.0 | -0.6 | +0.1 | -0.3 |
| US midterms (3 Nov 2026): Democrats win House and Senate (`EV_US_MIDTERMS_DEM_SWEEP`) | occurred | 1.00 | +0.8% | +0.8% | +0.8 | +0.0 | +0.0 | +0.0 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.25 | -2.8% | -0.7% | +0.0 | -2.9 | +0.0 | +0.0 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.25 | -2.8% | -0.7% | -1.1 | -0.8 | -0.7 | -0.2 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -0.7% | -0.7% | +0.0 | -0.6 | -0.1 | +0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → JUBLFOOD | +3.75% | +1.88% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → JUBLFOOD | -1.80% | -0.76% |
| 1 | EV_RBI_FEB27_HIKE25 ⇒ F_REPO_IN → JUBLFOOD | -1.80% | -0.49% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → JUBLFOOD | -2.25% | -0.40% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → JUBLFOOD | -1.44% | -0.36% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_FPI_FLOWS → JUBLFOOD | -1.44% | -0.36% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → JUBLFOOD | +0.65% | +0.36% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → JUBLFOOD | -1.40% | -0.35% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_REPO_IN → JUBLFOOD | -1.80% | -0.32% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → JUBLFOOD | -1.10% | -0.28% |
| 1 | EV_BUDGET_FY28_LTCG_RELIEF ⇒ F_FPI_FLOWS → JUBLFOOD | +0.75% | +0.26% |
| 1 | EV_Q2_FY27_GDP_STRONG ⇒ F_FPI_FLOWS → JUBLFOOD | +0.30% | +0.24% |
| 1 | EV_LABOUR_CODES_RULES ⇒ F_WAGES_IN → JUBLFOOD | -0.30% | -0.24% |
| 1 | EV_INDIA_STAGFLATION_SCARE ⇒ F_REPO_IN → JUBLFOOD | -1.80% | -0.22% |
| 2 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → JUBLFOOD | -1.40% | -0.21% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_FPI_FLOWS → JUBLFOOD | -1.60 | events | -2.40% |
| 1 | F_REPO_IN → JUBLFOOD | +1.00 | events | -1.80% |
| 1 | F_FOOD_INFLATION_IN → JUBLFOOD | +2.00 | events | -1.20% |
| 1 | F_URBAN_DEMAND → JUBLFOOD | +0.20 | events | +0.80% |
| 2 | F_MONSOON → F_DAIRY → JUBLFOOD | -1.56 | events | -0.35% |
| 1 | F_WHEAT → JUBLFOOD | -0.13 | observed | +0.08% |
| 1 | F_USDINR → JUBLFOOD | -0.37 | observed | +0.07% |
| 1 | F_BRENT → JUBLFOOD | +0.00 | observed | -0.00% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-11-10 | Q2 FY27 results (Sep quarter not yet in pack; board date estimated, model knowledge) | results | 0.90 | +0.0% | +0.00% |
| 2026-12 | Store additions guidance towards ~3,800-4,000 stores and Popeyes expansion | capex | 0.50 | +0.5% | +0.25% |
| 2027-01-08 | Q3 FY27 business update | guidance | 0.80 | +0.0% | +0.00% |

## Analyst profile (agent research, sourced)
# JUBLFOOD — Jubilant FoodWorks Ltd., as of 2026-11-05

*Sources: screener.in pack (through Jun-26), Q2 FY27 business update headlines (7-8 Oct 2026; bodies not retrieved).*

## Business
Master franchisee of Domino's (India, Sri Lanka, Bangladesh, Turkey), Popeyes and Hong's Kitchen. TTM sales Rs 9,838 cr, EBITDA margin ~20%, PAT Rs 450 cr, P/E 78. Q2 FY27 revenue +11.9% to Rs 2,608.7 cr, Domino's India LFL +4%, 3,820 stores (Reuters/CNBC TV18, 7-8 Oct). Stock -24% in 12m, Rs 452.

## What moves the stock (ranked)
1. Domino's India LFL and urban demand (F_URBAN_DEMAND +4).
2. Input costs: cheese/dairy (F_DAIRY -1.4), wheat (-0.6), wages (-1.0), fuel (-0.5).
3. Aggregator and quick-commerce competition (-3).
4. Rates and FPI flows (-1.8, +1.5).
5. Turkey/FX and royalty (small).

## Transmission examples
- **Brent up** -> fuel for delivery and LPG ovens -> costs +0.1% of revenue -> margin dips; CPI rises -> RBI on hold -> consumer wallets squeezed -> LFL drops (3rd-4th).
- **Dairy price spike (+8%)** -> cheese cost -> gross margin -60 bp unless prices raised -> price hikes reduce order volume -> LFL softens (2nd-3rd).
- **Rural/urban stimulus or GST cut** -> discretionary eating out -> LFL +2pp -> operating leverage lifts EBITDA ~5%.
- **Aggregator push into own brands** -> order share loss, higher commissions.

## Current situation
Q1 FY27: PAT Rs 100 cr (+6%), Popeyes LFL 40%+ (Business Standard, 14 Aug). Q2 update on 7 Oct: shares fell 4-6% as LFL disappointed. Motilal Oswal Buy, TP Rs 625 (14 Oct). Promoter 40.3%, DIIs 40%, FIIs 13.3%. Q2 results due ~mid-Nov.

## Bull / bear
Bull: LFL recovery above 6%, Popeyes scaling. Bear: LFL stuck, dairy inflation, price war, 78x P/E de-rates.

## Uncertainties
Cost shares and Turkey exposure are model estimates; Q2 profit not yet reported.

## Additional notes
Store growth (3,820 stores) outpaces LFL, so returns on new stores matter; Popeyes is small but growing fast and diversifies away from pizza. Turkey (roughly 5% of revenue, model knowledge) adds lira-inflation risk not captured by USD/INR. Upcoming: Q2 FY27 results (~10 Nov), Q3 update (~8 Jan 2027).


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.