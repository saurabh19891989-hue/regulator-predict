# ATGL — Adani Total Gas Ltd.
*MIDCAP_100 · Oil Gas & Consumable Fuels · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -0.3%**, **12 months -0.9%** (rank 110 / 119 of 200 for 3m / 12m); beta 1.19
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +36.5%): 3 months 49%, 12 months 57%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -4.5% … P90 +2.8%; plausible 12m relative-return range incl. stock-specific noise: -32.0% … +43.9%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +0.0 pp (model impact -0.8% beta-adjusted vs realised market-adjusted move -26.0%); forward event exposure +0.7% (3m +0.0%; half assumed priced); company-specific events -0.1%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| CGD APM gas allocation (`NEW_CGD_APM_ALLOCATION`) | +1 = 10pp cut in APM gas allocation to CNG/PNG(D) | -5.00 | -5.00 | +0.00 | +0.00 | +0.00 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -3.57 | -1.50 | -1.06 | -0.70 | -0.32 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -2.19 | +0.00 | -1.89 | -0.35 | +0.05 | — |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +1.87 | +0.00 | +0.98 | +0.92 | -0.04 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -1.63 | -1.50 | -0.04 | -0.05 | -0.04 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +1.62 | +1.50 | +0.07 | +0.01 | +0.03 | — |
| Global natural gas / LNG price (`F_GAS_GLOBAL`) | +15% gas/LNG price | -1.60 | -1.60 | +0.00 | +0.00 | +0.00 | -7.0% |
| Brent crude oil price (`F_BRENT`) | +10% Brent | -1.59 | -0.80 | -0.53 | -0.22 | -0.04 | +0.0% |
| Russia-Ukraine war / Western sanctions intensity on Russia (`NEW_RUSSIA_UKRAINE_WAR`) | +1 = escalation (new sanctions round, strikes on energy/port infrastructure); -1 = ceasefire/sanctions relief | -1.52 | +0.00 | -0.83 | -0.49 | -0.20 | — |
| OPEC+ crude supply decisions (`NEW_OPEC_PLUS_SUPPLY`) | +1 mb/d OPEC+ production (quota/actual) | +1.42 | +0.00 | +0.51 | +0.64 | +0.27 | — |
| China growth / stimulus (`F_CHINA_GDP`) | +1 pp | -1.40 | +0.00 | -0.94 | -0.33 | -0.12 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -1.32 | -0.80 | -0.31 | -0.18 | -0.03 | -1.1% |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -1.28 | +0.00 | +0.00 | -1.12 | -0.17 | — |
| Indian vehicle demand (`F_AUTO_DEMAND_IN`) | +10% volumes | +1.20 | +1.20 | +0.00 | +0.00 | +0.00 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -11.2% | -11.2% | -6.2 | -3.5 | -1.2 | -0.3 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -3.6% | -3.6% | -3.3 | -0.2 | -0.0 | -0.1 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.58 | +5.0% | +2.9% | +2.7 | +1.7 | +0.5 | +0.1 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.36 | -8.1% | -2.9% | -5.4 | -1.5 | -1.0 | -0.2 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -2.6% | -2.6% | +0.0 | -2.2 | -0.5 | +0.1 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +4.1% | +2.1% | +3.8 | +0.2 | +0.0 | +0.1 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -1.7% | -1.7% | -1.5 | -0.0 | -0.1 | -0.0 |
| LNG supply disruption: ~90 delayed Qatar cargoes to Petronet; India re-sources to US/UAE; Henry Hub proxy only +12% in 3m (`EV_LNG_HORMUZ_DISRUPTION`) | occurred | 1.00 | -1.6% | -1.6% | -1.6 | +0.0 | +0.0 | +0.0 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.28 | -4.9% | -1.4% | +0.0 | -4.1 | -0.8 | -0.0 |
| US waives Russia-oil secondary sanctions/100% tariff threat on buyers incl. India (17 Oct) (`EV_RUSSIA_WAIVER_OCT17`) | occurred | 1.00 | +1.4% | +1.4% | +0.0 | +0.6 | +0.5 | +0.2 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -1.3% | -1.3% | +0.0 | -1.1 | -0.1 | +0.0 |
| Hormuz effectively closed for >2 weeks (Brent > $150) (`EV_HORMUZ_FULL_CLOSURE`) | risk_scenario | 0.06 | -20.0% | -1.2% | -13.4 | -3.6 | -2.4 | -0.6 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → ATGL | +3.75% | +1.88% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ C_MIDEAST_CONFLICT → ATGL | +1.50% | +0.87% |
| 1 | EV_EU_WINTER_GAS_SPIKE ⇒ F_GAS_GLOBAL → ATGL | -4.00% | -0.80% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → ATGL | -2.00% | -0.71% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → ATGL | +1.20% | +0.70% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ C_MIDEAST_CONFLICT → ATGL | -1.80% | -0.64% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → ATGL | -2.24% | -0.63% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → ATGL | -1.50% | -0.60% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_GAS_GLOBAL → ATGL | -1.60% | -0.57% |
| 2 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → ATGL | -2.80% | -0.50% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → ATGL | -2.25% | -0.49% |
| 2 | EV_PULSES_VEG_SPIKE_WINTER ⇒ F_CPI_IN → F_REPO_IN → ATGL | -1.73% | -0.43% |
| 1 | EV_RBI_FEB27_HIKE25 ⇒ F_REPO_IN → ATGL | -1.50% | -0.41% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → ATGL | -1.44% | -0.40% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_FPI_FLOWS → ATGL | -1.44% | -0.36% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_FPI_FLOWS → ATGL | -1.60 | events | -2.40% |
| 1 | C_MIDEAST_CONFLICT → ATGL | +1.50 | events | -2.25% |
| 1 | F_REPO_IN → ATGL | +1.00 | events | -1.50% |
| 1 | P_EV_POLICY → ATGL | +1.10 | events | -1.10% |
| 1 | F_GAS_GLOBAL → ATGL | -0.47 | observed | +0.75% |
| 1 | F_GDP_IN → ATGL | +0.50 | events | +0.50% |
| 1 | F_USDINR → ATGL | -0.37 | observed | +0.30% |
| 1 | F_AUTO_DEMAND_IN → ATGL | -0.10 | events | -0.12% |
| 1 | F_BRENT → ATGL | +0.00 | observed | -0.00% |

## Analyst profile (agent research, sourced)
# Adani Total Gas (ATGL) — market impact profile (as of 2026-11-05)

## Business
ATGL distributes natural gas as CNG (about 55% of volume, model knowledge), industrial/commercial PNG and domestic PNG in dozens of licence areas. Its unit margin per standard cubic metre is the spread between a blended gas cost and a retail tariff set by the company (CNG/industrial) or lagged formulas. The blend runs from administered APM gas (cheap, priority-allocated to CNG and domestic PNG) to HPHT, New Regulatory Gas and spot LNG, so each government APM cut or LNG spike compresses margin until tariffs are raised.

## What moves the stock (ranked)
1. **Allocation of cheap gas (NEW_CGD_APM_ALLOCATION, weight -5.0 per 10pp cut).**
2. **LNG / spot gas price (F_GAS_GLOBAL, C_MIDEAST_CONFLICT).**
3. **Discount rate (F_REPO_IN)** — at 100x earnings the multiple, not near-term earnings, dominates.
4. **Volume drivers (F_AUTO_DEMAND_IN, F_GDP_IN)**, offset by EV substitution (P_EV_POLICY).
5. **Brent** — conflicting channels (CNG competitiveness vs oil-linked gas cost).
6. **Group contagion (ADANIENT).**

## Worked transmission examples
- Hormuz escalation -> Qatari LNG disrupted -> Asian spot LNG up (order 1) -> ATGL's marginal gas cost rises and the government keeps APM share flat or lower for CGD (order 2) -> EBITDA margin falls from 17% towards 14% until CNG is repriced; the market sees CNG pricing power limited by the petrol price gap (order 3) -> CNG vehicle conversion slows, the stock de-rates from a growth multiple (order 4).
- Brent up -> diesel and petrol prices (subject to OMC under-recoveries) -> CNG savings improve -> volumes up, but if the government holds pump prices, the advantage barely widens, so the benefit is muted; at the same time, higher inflation delays RBI easing (repo steady), hurting a long-duration stock.
- USD/INR up -> LNG import costs up -> cost pass-through lag (1-2 quarters) -> temporary margin trough.

## Current situation
Q2 FY27 net profit Rs 173 cr (+6% y/y), volume +12%, OPM 17% (vs 20% a year ago), as higher gas costs and a smaller APM allocation weighed. A calibrated CNG price hike was announced on 23 Oct. The share is -11.6% over three months and trades near 100x trailing earnings. Promoters hold 74.8%; FIIs 12.8%.

## Upcoming events
Q3 FY27 results; further CNG price moves; APM allocation reviews; Adani-group legal headlines.

## Bull / bear
Bull: LNG normalises after de-escalation, CNG hikes stick, volumes compound at 12%+, multiple holds. Bear: another APM cut plus spot LNG spike compresses EBITDA, and a 100x P/E leaves no cushion; Adani-group legal shock.

*Weights are exposure estimates, not return forecasts; Adani contagion edge units are % of ATGL per % of ADANIENT.*


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.