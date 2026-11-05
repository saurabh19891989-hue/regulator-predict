# SWIGGY — Swiggy Ltd.
*MIDCAP_100 · Consumer Services · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -2.7%**, **12 months -3.0%** (rank 172 / 147 of 200 for 3m / 12m); beta 1.17
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +38.6%): 3 months 44%, 12 months 80%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -4.8% … P90 +1.1%; plausible 12m relative-return range incl. stock-specific noise: -8.4% … +44.4%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +0.0 pp (model impact -7.1% beta-adjusted vs realised market-adjusted move -30.0%); forward event exposure -3.1% (3m -3.0%; half assumed priced); company-specific events -0.8%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Quick-commerce competitive intensity (Blinkit, Zepto, Flipkart Minutes, Amazon) (`NEW_QCOMMERCE_COMPETITION`) | +1 = materially faster dark-store expansion/discounting by rivals | -8.00 | -8.00 | +0.00 | +0.00 | +0.00 | — |
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +3.93 | +4.00 | +0.00 | -0.02 | -0.05 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +3.06 | +3.00 | +0.00 | +0.02 | +0.04 | — |
| Quick-commerce disruption of retail/FMCG distribution (`T_QUICK_COMMERCE`) | +1 | +3.00 | +3.00 | +0.00 | +0.00 | +0.00 | — |
| Labour code implementation cost (`P_LABOUR_CODES`) | +1 = implementation | -2.90 | -3.00 | +0.00 | +0.13 | -0.03 | — |
| US Fed funds rate (`F_FED_FUNDS`) | +25 bp | -2.87 | -2.50 | -0.09 | -0.18 | -0.10 | +11.2% |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -2.66 | +0.00 | -2.37 | -0.19 | -0.11 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -2.63 | +0.00 | -0.84 | -0.74 | -1.05 | — |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -1.78 | +0.00 | -1.12 | -0.63 | -0.03 | +3.5% |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +1.77 | +0.00 | +1.12 | +0.62 | +0.03 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -1.72 | -1.50 | -0.16 | -0.02 | -0.04 | — |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -1.70 | -1.00 | +0.00 | -0.65 | -0.05 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -1.70 | +0.00 | -1.20 | -0.45 | -0.05 | -1.1% |
| US dollar index (`F_DXY`) | +3% DXY | -1.67 | +0.00 | -1.32 | -0.26 | -0.09 | +2.2% |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -6.7% | -6.7% | -6.6 | +0.0 | -0.0 | -0.1 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -4.2% | -4.2% | -1.1 | -2.7 | -0.2 | -0.1 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +7.7% | +3.8% | +7.5 | +0.0 | +0.1 | +0.1 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -3.8% | -3.8% | -2.5 | -1.1 | -0.1 | -0.1 |
| FOMC 8-9 Dec 2026: 25 bp hike to 4.00-4.25% (`EV_FED_DEC26_HIKE25`) | scheduled | 0.72 | -3.4% | -2.4% | -2.5 | -0.7 | -0.1 | -0.1 |
| Labour codes: states finalise rules (deadline 31 Oct 2026), wider operational rollout (`EV_LABOUR_CODES_RULES`) | anticipated | 0.80 | -2.7% | -2.2% | -3.0 | +0.4 | -0.1 | -0.0 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -1.8% | -1.8% | -1.5 | -0.2 | -0.0 | -0.1 |
| US midterms (3 Nov 2026): Democrats win House and Senate (`EV_US_MIDTERMS_DEM_SWEEP`) | occurred | 1.00 | +1.5% | +1.5% | +1.5 | +0.0 | +0.0 | +0.0 |
| Fed hikes >=50 bp cumulative beyond Oct level by Apr 2027 (`EV_FED_H1_2027_FURTHER_HIKES`) | anticipated | 0.40 | -3.7% | -1.5% | -2.5 | -0.9 | -0.2 | -0.1 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.55 | +2.5% | +1.4% | +0.9 | +0.7 | +0.7 | +0.2 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -1.3% | -1.3% | +0.0 | -0.5 | -0.1 | -0.7 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.25 | -5.1% | -1.3% | +0.0 | -5.7 | +0.5 | +0.1 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → SWIGGY | +7.50% | +3.75% |
| 1 | EV_LABOUR_CODES_RULES ⇒ P_LABOUR_CODES → SWIGGY | -3.00% | -2.40% |
| 1 | EV_US_RECESSION_RISK_2027 ⇒ F_FED_FUNDS → SWIGGY | +7.50% | +1.88% |
| 1 | EV_FED_DEC26_HIKE25 ⇒ F_FED_FUNDS → SWIGGY | -2.50% | -1.80% |
| 1 | EV_FED_H1_2027_FURTHER_HIKES ⇒ F_FED_FUNDS → SWIGGY | -2.50% | -1.00% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → SWIGGY | -4.50% | -0.81% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → SWIGGY | -2.88% | -0.72% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_FPI_FLOWS → SWIGGY | -2.88% | -0.72% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → SWIGGY | -2.80% | -0.70% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → SWIGGY | -1.50% | -0.63% |
| 1 | EV_BUDGET_FY28_LTCG_RELIEF ⇒ F_FPI_FLOWS → SWIGGY | +1.50% | +0.52% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → SWIGGY | +0.91% | +0.50% |
| 1 | EV_Q2_FY27_GDP_STRONG ⇒ F_FPI_FLOWS → SWIGGY | +0.60% | +0.48% |
| 1 | EV_FED_H1_2027_CUTS ⇒ F_FED_FUNDS → SWIGGY | +3.75% | +0.45% |
| 2 | EV_PULSES_VEG_SPIKE_WINTER ⇒ F_CPI_IN → F_REPO_IN → SWIGGY | -1.73% | -0.43% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_FPI_FLOWS → SWIGGY | -1.60 | events | -4.80% |
| 1 | F_FED_FUNDS → SWIGGY | +1.62 | observed | -4.05% |
| 1 | F_FOOD_INFLATION_IN → SWIGGY | +2.00 | events | -2.00% |
| 1 | F_REPO_IN → SWIGGY | +1.00 | events | -1.50% |
| 1 | F_URBAN_DEMAND → SWIGGY | +0.20 | events | +0.80% |
| 1 | F_BRENT → SWIGGY | +0.00 | observed | -0.00% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-12 | More block deals / large holder exits after Tencent (Rs 982 cr, 2026-10-30) | corporate_action | 0.40 | -3.0% | -1.20% |
| 2026-12 | Regulatory action on quick commerce (CCI / FSSAI / dark-store rules) | regulatory | 0.25 | +0.5% | +0.12% |
| 2027-01 | Q3 FY27 results: Instamart contribution margin and loss trajectory (festive quarter) | results | 0.95 | +0.0% | +0.00% |
| 2027-03 | Instamart break-even / contribution-positive target commentary and fundraising need | guidance | 0.30 | +1.0% | +0.30% |

## Analyst profile (agent research, sourced)
# SWIGGY (Swiggy Ltd.) - company profile as of 2026-11-05

## Business
Swiggy runs food delivery, the Instamart quick-commerce network, out-of-home dining and supply-chain services. Consolidated sales in the September 2026 quarter were Rs 7,571 cr (+36% y/y) with an operating loss of Rs 772 cr and a net loss of Rs 922 cr; TTM sales are Rs 26,914 cr and the TTM operating loss is Rs 2,904 cr (screener.in, retrieved 2026-11-05). Reuters and The Tech Portal reported Instamart losses widening to Rs 895 cr. The shares closed at Rs 188-189 (market cap Rs 52,156 cr), -54% over twelve months, after falling 15-17% to a record low on 2026-10-23. Tencent sold out through a Rs 982 cr block on 2026-10-30, FIIs fell from 14.6% to 8.9% in two quarters, and DIIs rose to 34.5%.

## What moves the stock (ranked)
1. **Quick-commerce competition and cash burn.** Blinkit (Eternal) targets 3,500 dark stores by March 2027 and Flipkart Minutes overtook Instamart in dark-store count in August. A step-up in rival intensity is the dominant risk: central -8 equity points per +1 unit.
2. **Funding and ownership overhang.** Cash from operations was -Rs 2,898 cr in FY26, financed by Rs 9,397 cr of financing inflows. Large-holder exits (Tencent) and FII selling pressure the stock.
3. **Urban discretionary demand.** Order growth and AOV respond to urban wage and employment trends.
4. **Discount rates.** Loss-making growth equity; Fed funds and repo matter.
5. **Regulation and labour.** FSSAI oversight of online food, CCI scrutiny of discounting, gig-worker social-security contributions.

## Transmission examples
- **Middle East escalation -> Brent up -> petrol/diesel up -> delivery partner payouts up -> contribution margin down.** Order 2: rider fuel costs rise; order 3: Swiggy raises incentives or fees; order 4: order frequency falls among price-sensitive users. Impact is small relative to competition.
- **Brent up -> US 10Y and risk-off up -> FPI outflow -> already thin FII register falls further -> stock gaps.**
- **Rival raises capital (Zepto/Flipkart) -> dark-store expansion -> Instamart discounting -> Swiggy burn and funding need rise -> equity dilution risk.** This is the main fourth-order path.
- **Regulator curbs deep discounting (CCI/dark-store rules) -> burn reduces for all players -> Swiggy upside.** The sign of regulation is ambiguous; FSSAI licensing costs are negative.
- **Food inflation -> restaurant menu inflation -> fewer delivery orders.**

## Current situation
Q2 revenue growth of 36% was healthy, but losses widened sequentially and analysts cut targets (Moneycontrol, Business Standard, CNBC TV18, 2026-10-23). Anand Rathi had upgraded to Buy on 2026-10-19. Shares +5% on 2026-11-05 (screener).

## Upcoming events
Q3 FY27 results (January 2027), possible further holder exits, regulatory decisions on quick commerce, Instamart break-even commentary.

## Bull case
Rivals' discipline plus regulatory limits on discounting allow Instamart to reach contribution break-even in 2-3 quarters while food delivery profits rise; with DIIs at 34.5%, the shares re-rate 40-60% from a depressed base.

## Bear case
A deeper price war requires another capital raise; the stock falls 30%+.

## Uncertainties
Segment shares and cost split are model estimates, cash balance after the FY26 raise not verified, labour-code timing unverified. Confidence overall low.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.