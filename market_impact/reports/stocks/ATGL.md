# ATGL — Adani Total Gas Ltd.
*MIDCAP_100 · Oil Gas & Consumable Fuels · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +0.3%**, **12 months -0.4%** (rank 70 / 127 of 200 for 3m / 12m); beta 1.19
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +36.5%): 3 months 51%, 12 months 49%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -4.0% … P90 +2.8%; plausible 12m relative-return range incl. stock-specific noise: -46.4% … +42.1%
- Decomposition (12m): 0.5 × forward event exposure -0.3% (3m -0.1%; half assumed priced; market-priced macro drift removed) + 0.5 × company-specific catalysts -0.1%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply -7.6% (beta-adjusted) vs a realised market-adjusted move of -26.0% — gap +18.4 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## Where the expected return comes from
Market-priced macro drivers (rates, FX, commodities, indices, volatility, flows, growth, inflation) are taken as priced, so what is left is policy, regulatory, sector, theme, geopolitical and company-specific exposure — where 2nd–4th-order effects are most likely to be missed. Percentage points of the expected relative return.
| source | 12m: 1st order | 12m: 2nd–4th order | 12m total | 3m total |
|---|---|---|---|---|
| Policy | +0.00 | +0.02 | +0.02 | -0.05 |
| Sector | +0.00 | +0.22 | +0.22 | +0.08 |
| Theme | +0.00 | +0.05 | +0.05 | +0.03 |
| Geopolitics | +0.09 | +0.15 | +0.24 | +0.19 |
| Company catalysts | -0.17 | +0.11 | -0.06 | +0.42 |
| Market-priced macro | +0.00 | +0.00 | +0.00 | -0.00 |
| Beta adjustment | — | — | -0.68 | -0.31 |
| Universe centring | — | — | -0.15 | -0.10 |
| **Expected relative return** | | | **-0.36** | **+0.26** |

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| CGD APM gas allocation (`NEW_CGD_APM_ALLOCATION`) | +1 = 10pp cut in APM gas allocation to CNG/PNG(D) | -5.00 | -5.00 | +0.00 | +0.00 | +0.00 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -3.43 | -1.50 | -1.06 | -0.65 | -0.23 | — |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +1.73 | +0.00 | +0.98 | +0.69 | +0.05 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -1.62 | -1.50 | -0.04 | -0.05 | -0.04 | — |
| Global natural gas / LNG price (`F_GAS_GLOBAL`) | +15% gas/LNG price | -1.60 | -1.60 | +0.00 | +0.00 | +0.00 | -7.0% |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +1.60 | +1.50 | +0.07 | +0.01 | +0.01 | — |
| Brent crude oil price (`F_BRENT`) | +10% Brent | -1.46 | -0.80 | -0.49 | -0.15 | -0.02 | +0.0% |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -1.21 | -0.80 | -0.31 | -0.08 | -0.02 | -1.1% |
| Indian vehicle demand (`F_AUTO_DEMAND_IN`) | +10% volumes | +1.20 | +1.20 | +0.00 | +0.00 | +0.00 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -1.13 | +0.00 | -1.02 | -0.23 | +0.12 | — |
| China growth / stimulus (`F_CHINA_GDP`) | +1 pp | -1.13 | +0.00 | -0.94 | -0.15 | -0.04 | — |
| Russia-Ukraine war / Western sanctions intensity on Russia (`NEW_RUSSIA_UKRAINE_WAR`) | +1 = escalation (new sanctions round, strikes on energy/port infrastructure); -1 = ceasefire/sanctions relief | -1.05 | +0.00 | -0.83 | -0.22 | +0.00 | — |
| EV incentives / mandates (`P_EV_POLICY`) | +1 = stronger EV push | -0.99 | -1.00 | +0.00 | +0.00 | +0.01 | — |
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | +0.98 | +0.00 | +1.03 | -0.00 | -0.04 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -3.5% | -3.5% | -3.3 | -0.2 | -0.0 | -0.0 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.55 | +4.4% | +2.4% | +2.5 | +1.5 | +0.3 | +0.0 |
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -2.2% | -2.2% | -1.5 | -0.6 | -0.1 | -0.1 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +4.0% | +2.0% | +3.8 | +0.2 | +0.0 | +0.0 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.25 | -7.0% | -1.8% | -5.2 | -1.2 | -0.6 | -0.1 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -1.6% | -1.6% | -1.5 | -0.0 | -0.1 | -0.0 |
| LNG supply disruption: ~90 delayed Qatar cargoes to Petronet; India re-sources to US/UAE; Henry Hub proxy only +12% in 3m (`EV_LNG_HORMUZ_DISRUPTION`) | occurred | 1.00 | -1.6% | -1.6% | -1.6 | +0.0 | +0.0 | +0.0 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -1.4% | -1.4% | +0.0 | -1.2 | -0.3 | +0.1 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -0.9% | -0.9% | +0.0 | -0.3 | -0.3 | -0.3 |
| CAFE-III fuel-efficiency norms notified (30 Sep 2026); no small-car carve-out; 3x credit for BEVs (`EV_CAFE3_NOTIFIED`) | occurred | 1.00 | -0.9% | -0.9% | -0.9 | +0.0 | +0.0 | +0.0 |
| Risk: USD/INR >98 and/or reserves < US$650bn (disorderly rupee, emergency RBI response) (`EV_RUPEE_BREAK_98_RESERVE_STRESS`) | risk_scenario | 0.18 | -4.9% | -0.9% | -4.8 | -0.0 | -0.1 | -0.1 |
| Hormuz effectively closed for >2 weeks (Brent > $150) (`EV_HORMUZ_FULL_CLOSURE`) | risk_scenario | 0.05 | -16.9% | -0.8% | -12.2 | -3.0 | -1.6 | -0.2 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → ATGL | +3.75% | +1.88% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ C_MIDEAST_CONFLICT → ATGL | +1.50% | +0.83% |
| 1 | EV_EU_WINTER_GAS_SPIKE ⇒ F_GAS_GLOBAL → ATGL | -4.00% | -0.80% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → ATGL | -1.50% | -0.63% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → ATGL | +1.04% | +0.57% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ C_MIDEAST_CONFLICT → ATGL | -1.80% | -0.45% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → ATGL | -1.76% | -0.44% |
| 1 | EV_RBI_FEB27_HIKE25 ⇒ F_REPO_IN → ATGL | -1.50% | -0.41% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → ATGL | -2.25% | -0.40% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_GAS_GLOBAL → ATGL | -1.60% | -0.40% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → ATGL | -1.44% | -0.36% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_FPI_FLOWS → ATGL | -1.44% | -0.36% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → ATGL | -1.40% | -0.35% |
| 2 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ C_MIDEAST_CONFLICT → F_GAS_GLOBAL → ATGL | +0.58% | +0.32% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_REPO_IN → ATGL | -1.50% | -0.27% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_GAS_GLOBAL → ATGL | +4.61 | observed | -7.38% |
| 1 | F_FPI_FLOWS → ATGL | -1.60 | events | -2.40% |
| 1 | C_MIDEAST_CONFLICT → ATGL | +1.00 | events | -1.50% |
| 1 | F_REPO_IN → ATGL | +1.00 | events | -1.50% |
| 1 | P_EV_POLICY → ATGL | +1.10 | events | -1.10% |
| 1 | F_AUTO_DEMAND_IN → ATGL | +0.50 | director_override | +0.60% |
| 1 | F_GDP_IN → ATGL | +0.50 | events | +0.50% |
| 1 | F_USDINR → ATGL | -0.37 | observed | +0.30% |
| 1 | F_BRENT → ATGL | +0.00 | observed | -0.00% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-12 | Further CNG/PNG price revision as gas costs rise (a 'calibrated' hike was done 23 Oct) | guidance | 0.45 | +2.2% | +1.01% |
| 2027-01 | Q3 FY27 results (Adani Total Gas usually reports in the second half of the month after quarter-end; date not announced) | results | 0.95 | +0.0% | +0.00% |
| 2027-03 | APM allocation / pricing change to CGD (quarterly allocation cycle) or government PNG scheme (Aug 2026 'Govt scheme boosts PNG networks') | regulatory | 0.35 | -2.0% | -0.70% |
| 2027-06 | Adani-group legal/regulatory headline risk (US enforcement matters; status after mid-2026 not verified) | litigation | 0.10 | -6.5% | -0.65% |

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