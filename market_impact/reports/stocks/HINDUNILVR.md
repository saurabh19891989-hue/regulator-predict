# HINDUNILVR — Hindustan Unilever Ltd.
*NIFTY_50 · Fast Moving Consumer Goods · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -0.2%**, **12 months -0.1%** (rank 106 / 106 of 200 for 3m / 12m); beta 0.76
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +15.7%): 3 months 49%, 12 months 45%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -2.0% … P90 +1.5%; plausible 12m relative-return range incl. stock-specific noise: -18.1% … +18.9%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +0.3 pp (model impact +0.6% beta-adjusted vs realised market-adjusted move -8.4%); forward event exposure +0.9% (3m +0.4%; half assumed priced); company-specific events +0.6%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -2.11 | +0.00 | -0.96 | -0.55 | -0.60 | — |
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +1.93 | +2.00 | +0.00 | -0.07 | -0.00 | — |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +1.56 | +1.00 | +0.40 | +0.21 | -0.05 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -1.55 | +0.00 | -1.57 | +0.06 | -0.03 | — |
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | +1.41 | +1.50 | +0.00 | -0.11 | +0.02 | — |
| Brent crude oil price (`F_BRENT`) | +10% Brent | -1.24 | -0.80 | -0.19 | -0.22 | -0.03 | +0.0% |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -1.09 | -1.00 | -0.06 | -0.02 | -0.01 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +1.08 | +1.00 | +0.05 | +0.01 | +0.02 | — |
| Consumer premiumisation (`T_PREMIUMISATION`) | +1 | +1.07 | +1.00 | +0.08 | +0.00 | -0.01 | — |
| OPEC+ crude supply decisions (`NEW_OPEC_PLUS_SUPPLY`) | +1 mb/d OPEC+ production (quota/actual) | +1.00 | +0.00 | +0.51 | +0.22 | +0.26 | — |
| Russia-Ukraine war / Western sanctions intensity on Russia (`NEW_RUSSIA_UKRAINE_WAR`) | +1 = escalation (new sanctions round, strikes on energy/port infrastructure); -1 = ceasefire/sanctions relief | -0.98 | +0.00 | -0.58 | -0.23 | -0.18 | — |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -0.94 | +0.00 | -0.12 | -0.87 | +0.05 | — |
| Palm / edible oil price (`F_EDIBLE_OIL`) | +10% edible oils | -0.88 | -0.80 | +0.00 | -0.01 | -0.07 | +1.9% |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -0.88 | -0.50 | -0.24 | -0.15 | +0.01 | -1.1% |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -6.5% | -6.5% | -4.0 | -0.9 | -1.3 | -0.3 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -2.4% | -2.4% | -2.2 | -0.1 | -0.0 | -0.1 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -1.9% | -1.9% | +0.0 | -1.9 | +0.1 | -0.0 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.36 | -4.0% | -1.4% | -2.0 | -1.0 | -0.9 | -0.2 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +2.8% | +1.4% | +2.5 | +0.1 | +0.0 | +0.1 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.58 | +2.3% | +1.3% | +1.2 | +0.5 | +0.5 | +0.1 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -1.1% | -1.1% | -1.0 | -0.1 | -0.0 | -0.0 |
| US waives Russia-oil secondary sanctions/100% tariff threat on buyers incl. India (17 Oct) (`EV_RUSSIA_WAIVER_OCT17`) | occurred | 1.00 | +0.9% | +0.9% | +0.0 | +0.5 | +0.2 | +0.2 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.28 | -3.2% | -0.9% | +0.0 | -2.7 | -0.4 | -0.1 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -0.9% | -0.9% | +0.0 | -0.4 | +0.0 | -0.5 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -0.8% | -0.8% | +0.0 | -0.7 | -0.1 | +0.0 |
| Gold and silver slump from January 2026 peaks (silver -53%, gold -24%) (`EV_PRECIOUS_METALS_CRASH_2026`) | occurred | 1.00 | -0.7% | -0.7% | +0.0 | -0.7 | -0.0 | -0.0 |

## Strongest causal chains (1st–4th order)
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → HINDUNILVR | -3.96% | -3.96% |
| 1 | EV_FPI_RECORD_OUTFLOW_26 ⇒ F_FPI_FLOWS → HINDUNILVR | -2.20% | -2.20% |
| 2 | EV_CPI_REACCEL_SEP26 ⇒ F_CPI_IN → F_REPO_IN → HINDUNILVR | -1.32% | -1.32% |
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → HINDUNILVR | +2.50% | +1.25% |
| 1 | EV_RBI_OCT26_HIKE25 ⇒ F_REPO_IN → HINDUNILVR | -1.00% | -1.00% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → HINDUNILVR | -2.00% | -0.71% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → HINDUNILVR | +1.20% | +0.70% |
| 1 | EV_US_MIDTERMS_DEM_SWEEP ⇒ F_FPI_FLOWS → HINDUNILVR | +0.50% | +0.50% |
| 1 | EV_RURAL_DEMAND_SOFT26 ⇒ F_RURAL_DEMAND → HINDUNILVR | -0.45% | -0.45% |
| 3 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_CPI_IN → F_REPO_IN → HINDUNILVR | -0.44% | -0.44% |
| 2 | EV_SWMONSOON26_DEFICIT ⇒ F_MONSOON → F_RURAL_DEMAND → HINDUNILVR | -0.43% | -0.43% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → HINDUNILVR | -1.49% | -0.42% |
| 1 | EV_GDP_Q1FY27_7_8 ⇒ F_URBAN_DEMAND → HINDUNILVR | +0.40% | +0.40% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → HINDUNILVR | -1.00% | -0.40% |
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_USDINR → HINDUNILVR | -0.39% | -0.39% |

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