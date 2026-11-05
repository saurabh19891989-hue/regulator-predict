# ETERNAL — Eternal Ltd.
*NIFTY_50 · Consumer Services · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -2.7%**, **12 months -4.8%** (rank 191 / 194 of 200 for 3m / 12m); beta 1.05
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +26.8%): 3 months 42%, 12 months 48%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -10.8% … P90 -0.8%; plausible 12m relative-return range incl. stock-specific noise: -37.8% … +22.9%
- Decomposition (12m): 0.5 × forward event exposure -8.7% (3m -5.7%; half assumed priced) + 0.5 × company-specific catalysts -0.0%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply -5.1% (beta-adjusted) vs a realised market-adjusted move of +39.0% — gap -44.1 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Quick-commerce disruption of retail/FMCG distribution (`T_QUICK_COMMERCE`) | +1 | +8.00 | +8.00 | +0.00 | +0.00 | +0.00 | — |
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +5.84 | +6.00 | +0.00 | -0.12 | -0.05 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +3.64 | +3.50 | +0.05 | +0.03 | +0.05 | — |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -3.60 | -2.50 | -0.68 | -0.37 | -0.05 | +3.5% |
| FDI liberalisation (`P_FDI_RULES`) | +1 = liberalisation | -2.90 | -3.00 | +0.02 | +0.06 | +0.02 | — |
| Labour code implementation cost (`P_LABOUR_CODES`) | +1 = implementation | -2.83 | -3.00 | +0.00 | +0.20 | -0.02 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -2.81 | -2.50 | -0.22 | -0.05 | -0.04 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -2.77 | +0.00 | -1.76 | -0.50 | -0.51 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -2.26 | +0.00 | -2.50 | +0.31 | -0.07 | — |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +2.17 | +0.00 | +1.68 | +0.66 | -0.16 | — |
| USD/JPY exchange rate (`NEW_USDJPY`) | +3% USD/JPY (yen weaker) | +2.08 | +0.00 | +1.84 | +0.11 | +0.13 | — |
| US average effective tariff rate (all partners) (`NEW_US_TARIFF_GLOBAL`) | +5 pp effective tariff rate | -2.01 | +0.00 | -1.00 | -0.82 | -0.19 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -1.50 | -0.50 | -0.76 | -0.27 | +0.03 | -1.1% |
| Brent crude oil price (`F_BRENT`) | +10% Brent | -1.43 | -0.80 | -0.26 | -0.32 | -0.05 | +0.0% |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -8.0% | -8.0% | -7.7 | -0.1 | -0.1 | -0.1 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +10.1% | +5.1% | +9.8 | +0.1 | +0.1 | +0.1 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -3.1% | -3.1% | -0.6 | -2.9 | +0.4 | -0.1 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -2.9% | -2.9% | -2.5 | -0.2 | -0.1 | -0.1 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.25 | -11.1% | -2.8% | -6.2 | -5.1 | +0.0 | +0.1 |
| Labour codes: states finalise rules (deadline 31 Oct 2026), wider operational rollout (`EV_LABOUR_CODES_RULES`) | anticipated | 0.80 | -2.6% | -2.1% | -3.0 | +0.6 | -0.1 | -0.0 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.55 | +3.4% | +1.8% | +2.0 | +0.6 | +0.6 | +0.1 |
| Disorderly yen carry-trade unwind (Aug-2024-style) after BoJ/MoF action (`EV_YEN_CARRY_UNWIND_RISK`) | risk_scenario | 0.15 | -12.1% | -1.8% | -6.2 | -5.9 | +0.1 | -0.1 |
| US midterms (3 Nov 2026): Democrats win House and Senate (`EV_US_MIDTERMS_DEM_SWEEP`) | occurred | 1.00 | +1.8% | +1.8% | +1.8 | +0.0 | -0.1 | +0.0 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.25 | -6.8% | -1.7% | -4.3 | -1.3 | -1.1 | -0.2 |
| Risk: USD/INR >98 and/or reserves < US$650bn (disorderly rupee, emergency RBI response) (`EV_RUPEE_BREAK_98_RESERVE_STRESS`) | risk_scenario | 0.18 | -8.9% | -1.6% | -8.4 | -0.2 | -0.3 | +0.0 |
| AI/tech selloff and capex-forecast pause (Oct 2026) (`EV_AI_SELLOFF_OCT26`) | occurred | 1.00 | -1.5% | -1.5% | -0.9 | -0.6 | -0.0 | +0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → ETERNAL | +8.75% | +4.38% |
| 1 | EV_LABOUR_CODES_RULES ⇒ P_LABOUR_CODES → ETERNAL | -3.00% | -2.40% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → ETERNAL | -6.25% | -1.56% |
| 1 | EV_CHINA_FDI_EASING_PN3 ⇒ P_FDI_RULES → ETERNAL | -2.10% | -1.47% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → ETERNAL | -2.50% | -1.05% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → ETERNAL | -5.25% | -0.95% |
| 1 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → ETERNAL | -6.25% | -0.94% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → ETERNAL | -3.36% | -0.84% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_FPI_FLOWS → ETERNAL | -3.36% | -0.84% |
| 1 | EV_RBI_FEB27_HIKE25 ⇒ F_REPO_IN → ETERNAL | -2.50% | -0.68% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_RISK_SENTIMENT → ETERNAL | -2.50% | -0.62% |
| 1 | EV_NVDA_NOV17_BEAT ⇒ F_RISK_SENTIMENT → ETERNAL | +1.00% | +0.62% |
| 1 | EV_BUDGET_FY28_LTCG_RELIEF ⇒ F_FPI_FLOWS → ETERNAL | +1.75% | +0.61% |
| 1 | EV_CPI_BREACH_6PCT ⇒ F_REPO_IN → ETERNAL | -1.00% | -0.60% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → ETERNAL | +1.04% | +0.57% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_FPI_FLOWS → ETERNAL | -1.60 | events | -5.60% |
| 1 | F_REPO_IN → ETERNAL | +1.00 | events | -2.50% |
| 1 | P_FDI_RULES → ETERNAL | +0.50 | events | -1.50% |
| 1 | F_URBAN_DEMAND → ETERNAL | +0.20 | events | +1.20% |
| 1 | F_FOOD_INFLATION_IN → ETERNAL | +2.00 | events | -1.00% |
| 1 | F_RISK_SENTIMENT → ETERNAL | +0.11 | observed | -0.28% |
| 1 | F_USDINR → ETERNAL | -0.37 | observed | +0.18% |
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