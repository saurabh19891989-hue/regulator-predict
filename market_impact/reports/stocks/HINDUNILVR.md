# HINDUNILVR — Hindustan Unilever Ltd.
*NIFTY_50 · Fast Moving Consumer Goods · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -0.0%**, **12 months +0.4%** (rank 105 / 90 of 200 for 3m / 12m); beta 0.76
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +15.7%): 3 months 50%, 12 months 52%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -1.2% … P90 +1.8%; plausible 12m relative-return range incl. stock-specific noise: -17.8% … +19.1%
- Decomposition (12m): 0.5 × forward event exposure +1.2% (3m +0.3%; half assumed priced) + 0.5 × company-specific catalysts +0.6%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply +0.6% (beta-adjusted) vs a realised market-adjusted move of -8.4% — gap +9.1 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +1.95 | +2.00 | +0.00 | -0.07 | +0.01 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -1.51 | +0.00 | -0.96 | -0.31 | -0.24 | — |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +1.48 | +1.00 | +0.40 | +0.13 | -0.05 | — |
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | +1.44 | +1.50 | +0.00 | -0.11 | +0.05 | — |
| Brent crude oil price (`F_BRENT`) | +10% Brent | -1.13 | -0.80 | -0.16 | -0.15 | -0.02 | +0.0% |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -1.09 | -1.00 | -0.06 | -0.02 | -0.01 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +1.07 | +1.00 | +0.05 | +0.01 | +0.01 | — |
| Consumer premiumisation (`T_PREMIUMISATION`) | +1 | +1.07 | +1.00 | +0.08 | +0.00 | -0.01 | — |
| Palm / edible oil price (`F_EDIBLE_OIL`) | +10% edible oils | -0.86 | -0.80 | +0.00 | -0.01 | -0.04 | +1.9% |
| Indian wage / employee-cost inflation (`F_WAGES_IN`) | +2 pp | +0.83 | +0.00 | +1.00 | -0.12 | -0.04 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -0.81 | +0.00 | -1.00 | +0.20 | -0.01 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -0.81 | -0.50 | -0.24 | -0.10 | +0.04 | -1.1% |
| Russia-Ukraine war / Western sanctions intensity on Russia (`NEW_RUSSIA_UKRAINE_WAR`) | +1 = escalation (new sanctions round, strikes on energy/port infrastructure); -1 = ceasefire/sanctions relief | -0.70 | +0.00 | -0.58 | -0.09 | -0.03 | — |
| OPEC+ crude supply decisions (`NEW_OPEC_PLUS_SUPPLY`) | +1 mb/d OPEC+ production (quota/actual) | +0.69 | +0.00 | +0.51 | +0.10 | +0.09 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -2.4% | -2.4% | -2.2 | -0.1 | -0.0 | -0.0 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +2.7% | +1.4% | +2.5 | +0.1 | +0.0 | +0.0 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -1.1% | -1.1% | -1.0 | -0.1 | -0.0 | -0.0 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -1.1% | -1.1% | +0.0 | -1.3 | +0.2 | -0.0 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.55 | +1.7% | +1.0% | +1.0 | +0.4 | +0.3 | +0.1 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.25 | -3.2% | -0.8% | -1.8 | -0.8 | -0.5 | -0.1 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -0.8% | -0.8% | +0.0 | -0.4 | +0.0 | -0.4 |
| Risk: USD/INR >98 and/or reserves < US$650bn (disorderly rupee, emergency RBI response) (`EV_RUPEE_BREAK_98_RESERVE_STRESS`) | risk_scenario | 0.18 | -3.3% | -0.6% | -3.1 | -0.1 | -0.1 | +0.0 |
| US midterms (3 Nov 2026): Democrats win House and Senate (`EV_US_MIDTERMS_DEM_SWEEP`) | occurred | 1.00 | +0.5% | +0.5% | +0.5 | +0.0 | +0.0 | +0.0 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.25 | -2.0% | -0.5% | +0.0 | -2.0 | +0.0 | +0.0 |
| RBI MPC Dec 2026 (~4 Dec): hikes repo another 25 bp to 5.75% (`EV_RBI_DEC26_HIKE25`) | scheduled | 0.42 | -1.1% | -0.5% | -1.0 | -0.1 | -0.0 | -0.0 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -0.5% | -0.5% | +0.0 | -0.4 | -0.1 | +0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → HINDUNILVR | +2.50% | +1.25% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → HINDUNILVR | +1.04% | +0.57% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → HINDUNILVR | -1.76% | -0.44% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → HINDUNILVR | -1.00% | -0.42% |
| 1 | EV_BUDGET27_AGRI_RURAL ⇒ F_RURAL_DEMAND → HINDUNILVR | +0.45% | +0.31% |
| 1 | EV_RBI_FEB27_HIKE25 ⇒ F_REPO_IN → HINDUNILVR | -1.00% | -0.27% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → HINDUNILVR | -1.50% | -0.27% |
| 1 | EV_RURAL_RELIEF_PACKAGE ⇒ F_RURAL_DEMAND → HINDUNILVR | +0.45% | +0.25% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → HINDUNILVR | -0.96% | -0.24% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_FPI_FLOWS → HINDUNILVR | -0.96% | -0.24% |
| 1 | EV_CPI_BREACH_6PCT ⇒ F_REPO_IN → HINDUNILVR | -0.40% | -0.24% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → HINDUNILVR | -0.93% | -0.23% |
| 2 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_RURAL_DEMAND → HINDUNILVR | +0.34% | +0.23% |
| 1 | EV_STATE_POLLS_FEB_MAR27 ⇒ F_RURAL_DEMAND → HINDUNILVR | +0.30% | +0.20% |
| 1 | EV_WHEAT27_CROP_BELOW ⇒ F_RURAL_DEMAND → HINDUNILVR | -0.30% | -0.20% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_FPI_FLOWS → HINDUNILVR | -1.60 | events | -1.60% |
| 1 | F_REPO_IN → HINDUNILVR | +1.00 | events | -1.00% |
| 1 | F_URBAN_DEMAND → HINDUNILVR | +0.20 | events | +0.40% |
| 1 | F_RURAL_DEMAND → HINDUNILVR | -0.25 | events | -0.38% |
| 1 | F_USDINR → HINDUNILVR | -0.37 | observed | +0.18% |
| 1 | F_EDIBLE_OIL → HINDUNILVR | +0.19 | observed | -0.15% |
| 3 | P_ANTI_DUMPING_IN → F_CHEM_FEEDSTOCK → F_PACKAGING → HINDUNILVR | +0.40 | events | -0.01% |
| 3 | F_CHINA_GDP → F_PETROCHEM_SPREADS → F_PACKAGING → HINDUNILVR | +0.30 | events | -0.01% |
| 4 | F_CHINA_GDP → F_CHINA_CHEM_EXPORTS → F_PETROCHEM_SPREADS → F_PACKAGING → HINDUNILVR | +0.30 | events | -0.00% |
| 1 | F_BRENT → HINDUNILVR | +0.00 | observed | -0.00% |
| 4 | C_US_CHINA_DECOUPLING → F_CHINA_CHEM_EXPORTS → F_PETROCHEM_SPREADS → F_PACKAGING → HINDUNILVR | -0.10 | events | -0.00% |
| 3 | F_BRENT → F_CHEM_FEEDSTOCK → F_PACKAGING → HINDUNILVR | +0.00 | observed | -0.00% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-11 | Interim dividend Rs 19/share payment (declared with Q2 results) | corporate_action | 0.95 | -0.5% | -0.47% |
| 2026-12 | Post-Diwali price increases across FMCG to recover input cost | other | 0.60 | +1.2% | +0.75% |
| 2027-01 | Q3 FY27 results; price hikes post Diwali visible in volume/margin | results | 0.90 | +0.0% | +0.00% |
| 2027-03 | Share buyback announcement (management asked about it on 28 Oct 2026; none announced) | corporate_action | 0.10 | +3.5% | +0.35% |

## Analyst profile (agent research, sourced)
# Hindustan Unilever — what moves the stock

**Business.** The largest Indian FMCG company, with Home Care, Beauty & Personal Care and Foods & Refreshment. It is debt-free, pays out ~92% of earnings, and trades at 41.6x earnings after a 19% drop in twelve months (screener.in, 2026-11-05). Q2 FY27: sales Rs 18,226 cr (+14.5%), operating margin 22% (24% a year earlier), PAT Rs 2,796 cr (+4%).

## Ranked drivers
1. **Urban and rural volume growth.** The Q2 print showed volume-led growth at a 14-quarter high; the key risk is the below-normal 2026 monsoon.
2. **Input costs: crude-linked chemicals and plastics, palm oil, tea.** The margin fell two points year on year as Brent rose (+15% in three months).
3. **Discount rate.** At 41.6x earnings, a 25bp repo move is worth about -1% of equity value.
4. **Strategy execution.** A 22-24% EBITDA-margin ambition and capex at ~3% of turnover (Capital Markets Day Sept 2026).
5. **FPI flows.** FII holding is down from 10.1% to 9.3% in two quarters.

## Worked transmission chains
- **Middle East escalation -> Brent up -> LAB/surfactant and polymer prices up -> detergent and packaging costs up -> gross margin down -> HUL must take price hikes -> rural volume elasticity bites (4th order).**
- **Brent up -> INR weaker (94.49) -> RBI cannot cut -> yields stay high -> a 41x multiple de-rates even if earnings hold.**
- **Weak monsoon -> rural incomes lower -> detergent/soap trade-down to local brands -> HUL rural volume growth slows -> operating deleverage.** The 2026 below-normal rainfall is already a headline risk (Moneycontrol 2026-10-05).
- **India cuts edible-oil import duty (24 Sep 2026) -> palm derivatives cheaper -> soap margin relief in 1-2 quarters; partially offsets the crude effect.**

## Current situation
Management's Q2 messaging stressed volume growth and reinvestment; brokers (Jefferies, Nomura) trimmed targets yet saw ~29% upside (ET 2026-10-29). Post-Diwali price rises are expected across FMCG (The Core 2026-11-03).

## Upcoming
Q3 FY27 results (about January 2027), dividend payment, possible buyback chatter, further price actions.

## Bull / bear
**Bull:** volume recovery, valuation near multi-year lows, margin relief from the oil duty cut. **Bear:** input inflation, weak rural demand, strategy-related margin dilution, FPI outflows. Cost-share estimates are model-knowledge approximations.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.