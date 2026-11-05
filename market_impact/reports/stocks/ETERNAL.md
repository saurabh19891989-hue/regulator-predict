# ETERNAL — Eternal Ltd.
*NIFTY_50 · Consumer Services · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -1.2%**, **12 months -2.5%** (rank 190 / 195 of 200 for 3m / 12m); beta 1.05
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +26.8%): 3 months 46%, 12 months 45%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -5.7% … P90 -0.5%; plausible 12m relative-return range incl. stock-specific noise: -36.2% … +30.2%
- Decomposition (12m): 0.5 × forward event exposure -4.7% (3m -3.0%; half assumed priced; market-priced macro drift removed) + 0.5 × company-specific catalysts -0.0%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply -0.7% (beta-adjusted) vs a realised market-adjusted move of +39.0% — gap -39.7 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## Where the expected return comes from
Market-priced macro drivers (rates, FX, commodities, indices, volatility, flows, growth, inflation) are taken as priced, so what is left is policy, regulatory, sector, theme, geopolitical and company-specific exposure — where 2nd–4th-order effects are most likely to be missed. Percentage points of the expected relative return.
| source | 12m: 1st order | 12m: 2nd–4th order | 12m total | 3m total |
|---|---|---|---|---|
| Policy | -1.76 | +0.06 | -1.69 | -1.24 |
| Regulatory | +0.00 | -0.02 | -0.02 | -0.01 |
| Sector | +0.00 | +0.27 | +0.27 | +0.16 |
| Theme | -0.24 | -0.04 | -0.28 | -0.11 |
| Geopolitics | +0.00 | -0.05 | -0.05 | -0.03 |
| Company catalysts | -0.00 | +0.00 | -0.00 | +0.38 |
| Market-priced macro | +0.00 | -0.00 | +0.00 | -0.00 |
| Beta adjustment | — | — | -0.60 | -0.27 |
| Universe centring | — | — | -0.15 | -0.10 |
| **Expected relative return** | | | **-2.51** | **-1.22** |

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Quick-commerce disruption of retail/FMCG distribution (`T_QUICK_COMMERCE`) | +1 | +8.00 | +8.00 | +0.00 | +0.00 | +0.00 | — |
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +5.98 | +6.00 | +0.00 | +0.00 | -0.02 | — |
| FDI liberalisation (`P_FDI_RULES`) | +1 = liberalisation | -2.94 | -3.00 | +0.02 | +0.03 | +0.01 | — |
| Labour code implementation cost (`P_LABOUR_CODES`) | +1 = implementation | -2.82 | -3.00 | +0.00 | +0.20 | -0.02 | — |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +2.09 | +0.00 | +1.68 | +0.51 | -0.09 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -1.85 | +0.00 | -1.28 | -0.24 | -0.33 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -1.81 | -1.50 | -0.22 | -0.07 | -0.02 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -1.63 | +0.00 | -1.92 | +0.39 | -0.10 | — |
| Indian wage / employee-cost inflation (`F_WAGES_IN`) | +2 pp | +1.63 | +0.00 | +1.92 | -0.29 | -0.00 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +1.50 | +1.40 | +0.05 | +0.02 | +0.03 | — |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -1.48 | -1.00 | -0.29 | -0.16 | -0.03 | +3.5% |
| Brent crude oil price (`F_BRENT`) | +10% Brent | -1.20 | -0.80 | -0.14 | -0.23 | -0.04 | +0.0% |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -0.99 | -0.50 | -0.34 | -0.19 | +0.04 | -1.1% |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -0.97 | -0.50 | +0.00 | -0.53 | +0.06 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -3.3% | -3.3% | -3.1 | -0.1 | -0.0 | -0.1 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -2.4% | -2.4% | -0.6 | -2.2 | +0.5 | -0.1 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +4.2% | +2.1% | +3.9 | +0.1 | +0.1 | +0.1 |
| Labour codes: states finalise rules (deadline 31 Oct 2026), wider operational rollout (`EV_LABOUR_CODES_RULES`) | anticipated | 0.80 | -2.5% | -2.0% | -3.0 | +0.6 | -0.1 | +0.0 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -1.8% | -1.8% | -1.5 | -0.2 | -0.1 | -0.0 |
| India further eases Press Note 3 rules for China/border-country FDI (approval timelines, minority stakes) (`EV_CHINA_FDI_EASING_PN3`) | anticipated | 0.70 | -2.0% | -1.4% | -2.1 | +0.0 | +0.0 | +0.0 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.55 | +2.2% | +1.2% | +1.4 | +0.3 | +0.4 | +0.1 |
| India Q1 FY27 GDP grows 7.8% (31 Aug 2026), beating ~7.3% consensus (`EV_GDP_Q1FY27_7_8`) | occurred | 1.00 | +1.1% | +1.1% | +1.2 | +0.0 | -0.1 | -0.0 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.25 | -4.3% | -1.1% | -2.5 | -2.1 | +0.2 | +0.1 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.25 | -4.2% | -1.0% | -2.8 | -0.6 | -0.7 | -0.2 |
| IT services: muted Q2 FY27 growth, AI deflation and deal-conversion concerns (`EV_IT_AI_DEFLATION_Q2FY27`) | occurred | 1.00 | -0.9% | -0.9% | +0.0 | -0.8 | -0.2 | +0.0 |
| India-China thaw: Xi visit around BRICS summit in India (mid-Sep 2026), flights resume, Chinese-investment curbs eased (`EV_INDIA_CHINA_THAW_SEP26`) | occurred | 1.00 | -0.9% | -0.9% | -0.9 | +0.0 | -0.0 | +0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_LABOUR_CODES_RULES ⇒ P_LABOUR_CODES → ETERNAL | -3.00% | -2.40% |
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → ETERNAL | +3.50% | +1.75% |
| 1 | EV_CHINA_FDI_EASING_PN3 ⇒ P_FDI_RULES → ETERNAL | -2.10% | -1.47% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → ETERNAL | -1.50% | -0.63% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → ETERNAL | -2.50% | -0.62% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → ETERNAL | +1.04% | +0.57% |
| 1 | EV_QCOMM_FDI_CRACKDOWN ⇒ T_QUICK_COMMERCE → ETERNAL | -4.00% | -0.48% |
| 2 | EV_LABOUR_CODES_RULES ⇒ F_WAGES_IN → F_URBAN_DEMAND → ETERNAL | +0.58% | +0.46% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → ETERNAL | -1.76% | -0.44% |
| 1 | EV_RBI_FEB27_HIKE25 ⇒ F_REPO_IN → ETERNAL | -1.50% | -0.41% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → ETERNAL | -2.10% | -0.38% |
| 1 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → ETERNAL | -2.50% | -0.38% |
| 1 | EV_QCOMM_FDI_CRACKDOWN ⇒ P_FDI_RULES → ETERNAL | +3.00% | +0.36% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → ETERNAL | -1.34% | -0.34% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_FPI_FLOWS → ETERNAL | -1.34% | -0.34% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_FPI_FLOWS → ETERNAL | -1.60 | events | -2.24% |
| 1 | P_FDI_RULES → ETERNAL | +0.50 | events | -1.50% |
| 1 | F_REPO_IN → ETERNAL | +1.00 | events | -1.50% |
| 1 | F_URBAN_DEMAND → ETERNAL | +0.20 | events | +1.20% |
| 1 | F_FOOD_INFLATION_IN → ETERNAL | +2.00 | events | -1.00% |
| 1 | F_USDINR → ETERNAL | -0.37 | observed | +0.18% |
| 1 | F_RISK_SENTIMENT → ETERNAL | +0.11 | observed | -0.11% |
| 1 | F_BRENT → ETERNAL | +0.00 | observed | -0.00% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-11 | Block deals/stake sales by large holders (Goldman block 16 Oct was Rs169 cr; small) | corporate_action | 0.40 | -0.8% | -0.30% |
| 2026-12 | Blinkit store count milestones towards 3,500 (and 5,000 by FY28 per CIOL) | capex | 0.60 | +1.0% | +0.60% |
| 2027-01-21 | Q3 FY27 results (model knowledge: Q3 FY26 results were around 21 Jan) | results | 0.90 | +0.5% | +0.45% |
| 2027-03 | Gig-worker social-security contribution rules operationalised under labour codes | regulatory | 0.30 | -2.5% | -0.75% |

## Analyst profile (agent research, sourced)
# ETERNAL — Eternal Ltd. (Zomato, Blinkit, Hyperpure, District), as of 2026-11-05

*Sources: screener.in pack and Google News headlines (Oct 2026); bodies not retrieved. Model knowledge is labelled.*

## Business
Eternal runs Zomato food delivery and dining, Blinkit quick commerce (now inventory-led, which inflated reported revenue to Rs 24,138 cr in Q2 FY27, +78% y/y), Hyperpure and District. Operating profit was Rs 752 cr (3.1% of revenue) and PAT Rs 125 cr (+92%), a miss vs estimates (Moneycontrol, 21 Oct). Market cap Rs 3.44 lakh cr, P/E ~700, FIIs 33%.

## What moves the stock (ranked)
1. Blinkit/quick-commerce growth and store roll-out (T_QUICK_COMMERCE, +8 per unit); management targets 3,500 stores near term and 5,000 by FY28 (CIOL, 22 Oct).
2. Urban demand (F_URBAN_DEMAND +6 per +5pp).
3. Discount rate and risk appetite (F_REPO_IN -2.5, F_RISK_SENTIMENT -2.5) because earnings are tiny relative to price.
4. FPI flows (+3.5).
5. Labour codes (gig-worker contributions, -3) and FDI/competition rules (-3).
6. Fuel for riders (-0.8).

## Transmission examples
- **Brent up** -> petrol cost for ~half the riders -> payouts rise, partly passed to customers -> delivery fee/AOV rise -> food-delivery frequency softens (2nd) -> adjusted EBITDA margin dips 20-40 bp (3rd) -> equity -0.8 per +10%.
- **Middle East escalation** -> Brent and risk-off VIX up -> FPIs sell India growth names -> 33% FII-held Eternal falls with beta >1 (2nd) -> funding for rivals (Swiggy, Zepto) tightens, which may relieve Eternal's competitive pressure (3rd/4th), a partial offset.
- **RBI holds rates after INR depreciation** -> real yields up -> long-duration discount rate up -> multiple compresses.
- **Swiggy retrenchment** (Swiggy -17% on Instamart losses, 23 Oct) -> less subsidy competition -> Blinkit share gains -> unit economics improve (positive, company-specific).

## Current situation
Q2 results on 21 Oct: stock fell 3.5% then recovered next day with brokerages bullish despite EBITDA miss. Goldman sold Rs 169 cr in a block (16 Oct) but also expects ~16% upside (29 Sep). Stock sits at its 52-week high (Rs 357), +38.6% in 6 months.

## Upcoming
Q3 FY27 results (~21 Jan 2027), gig-worker rule implementation (~Mar 2027, 30%), store milestones.

## Bull / bear
Bull: Blinkit adjusted margins reach target, Swiggy's pullback consolidates share, FPI inflows continue. Bear: price war from Zepto/Amazon/Flipkart, labour-code costs, rates up, multiple compression from 700x P/E.

## Uncertainties
Revenue mix is approximate, the Blinkit profit metric is headline-quoted, and empirical links (edible oil -4.4, t -2.9) have no clear mechanism.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.