# HINDPETRO — Hindustan Petroleum Corporation Ltd.
*MIDCAP_100 · Oil Gas & Consumable Fuels · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +5.4%**, **12 months +13.4%** (rank 10 / 2 of 200 for 3m / 12m); beta 1.46
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +23.1%): 3 months 68%, 12 months 70%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 +4.4% … P90 +25.0%; plausible 12m relative-return range incl. stock-specific noise: -25.1% … +53.1%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +1.8 pp (model impact +3.7% beta-adjusted vs realised market-adjusted move -8.5%); forward event exposure +23.4% (3m +10.8%; half assumed priced); company-specific events +2.1%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| OMC petrol+diesel marketing margin (`NEW_OMC_MARKETING_MARGIN`) | +Rs1/litre average marketing margin (vs normal ~Rs3-4/l) | +12.00 | +12.00 | +0.00 | -0.00 | -0.00 | — |
| Refining margins (GRM / cracks) (`F_REFINING_MARGIN`) | +$2/bbl gross refining margin | +4.98 | +5.00 | -0.02 | +0.00 | +0.00 | +15.4% |
| Government compensation to OMCs for fuel/LPG under-recoveries (`NEW_OMC_COMPENSATION`) | +1 = Rs25,000 cr compensation to oil marketing companies | +4.50 | +4.50 | +0.00 | +0.00 | +0.00 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -4.32 | -4.50 | -0.11 | +0.45 | -0.16 | — |
| Russia (oil discounts, defence, sanctions) (`C_RUSSIA`) | +1 = closer trade access / larger discounts | +3.25 | +1.50 | +1.92 | -0.20 | +0.02 | — |
| Brent crude oil price (`F_BRENT`) | +10% Brent | -2.98 | -3.00 | +0.13 | -0.10 | -0.01 | +0.0% |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -2.32 | -2.20 | -0.01 | -0.10 | -0.01 | -1.1% |
| OPEC+ crude supply decisions (`NEW_OPEC_PLUS_SUPPLY`) | +1 mb/d OPEC+ production (quota/actual) | +1.91 | +0.00 | +1.92 | -0.16 | +0.15 | — |
| Red Sea / Suez shipping disruption (`C_RED_SEA`) | +1 = disruption | +1.59 | +0.00 | +1.60 | -0.01 | +0.00 | — |
| Windfall / export taxes on commodities (`P_WINDFALL_EXPORT_TAX`) | +1 = imposition | -1.57 | -0.40 | -1.20 | +0.00 | +0.03 | — |
| Fuel excise / retail price policy (+ = higher taxes/regulated squeeze) (`P_FUEL_TAX_IN`) | +1 = Rs 2/litre excise rise | -1.52 | -1.50 | +0.00 | -0.03 | +0.01 | — |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -1.34 | +0.00 | -0.10 | -1.34 | +0.09 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -1.23 | +0.00 | -1.36 | +0.13 | +0.00 | — |
| China growth / stimulus (`F_CHINA_GDP`) | +1 pp | -1.10 | +0.00 | -1.08 | +0.04 | -0.06 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Retail petrol/diesel price freeze with crude >$100 squeezes OMC marketing margins; Q2 FY27 results split refiners (`EV_OMC_FUEL_FREEZE_LOSSES`) | occurred | 1.00 | -36.0% | -36.0% | -36.0 | +0.0 | +0.0 | +0.0 |
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -15.9% | -15.9% | -14.1 | -1.1 | -0.6 | -0.1 |
| Government allows OMCs a retail petrol/diesel price hike (Rs3-5/l) (`EV_INDIA_RETAIL_FUEL_HIKE`) | anticipated | 0.45 | +29.7% | +13.4% | +30.0 | -0.4 | +0.1 | -0.0 |
| Domestic LPG under-recoveries >Rs59,000 cr (to July); government compensation boosts IOC Q2 (`EV_LPG_UNDERRECOVERY`) | occurred | 1.00 | -12.0% | -12.0% | -12.0 | +0.0 | +0.0 | +0.0 |
| Cabinet approves further LPG under-recovery compensation to OMCs (`EV_LPG_COMPENSATION_CABINET`) | anticipated | 0.60 | +12.0% | +7.2% | +12.0 | +0.0 | -0.0 | -0.0 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.36 | -11.2% | -4.0% | -13.4 | +2.5 | -0.1 | -0.1 |
| US waives Russia-oil secondary sanctions/100% tariff threat on buyers incl. India (17 Oct) (`EV_RUSSIA_WAIVER_OCT17`) | occurred | 1.00 | +3.7% | +3.7% | +1.5 | +2.1 | -0.0 | +0.1 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.58 | +5.9% | +3.4% | +5.0 | +0.6 | +0.2 | +0.1 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -2.1% | -2.1% | +0.0 | -1.7 | -0.5 | +0.0 |
| Hormuz effectively closed for >2 weeks (Brent > $150) (`EV_HORMUZ_FULL_CLOSURE`) | risk_scenario | 0.06 | -26.3% | -1.6% | -30.8 | +5.1 | -0.3 | -0.3 |
| India cuts Russian crude below ~1 mb/d as part of US trade deal (`EV_RUSSIAN_CRUDE_CUT_TRADE_DEAL`) | anticipated | 0.30 | -4.7% | -1.4% | -4.0 | -0.7 | +0.0 | -0.0 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -1.1% | -1.1% | +0.0 | -1.0 | -0.0 | -0.1 |

## Strongest causal chains (1st–4th order)
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_OMC_FUEL_FREEZE_LOSSES ⇒ NEW_OMC_MARKETING_MARGIN → HINDPETRO | -36.00% | -36.00% |
| 1 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → HINDPETRO | -14.85% | -14.85% |
| 1 | EV_INDIA_RETAIL_FUEL_HIKE ⇒ NEW_OMC_MARKETING_MARGIN → HINDPETRO | +30.00% | +13.50% |
| 1 | EV_LPG_UNDERRECOVERY ⇒ NEW_OMC_MARKETING_MARGIN → HINDPETRO | -12.00% | -12.00% |
| 1 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_REFINING_MARGIN → HINDPETRO | +7.50% | +7.50% |
| 1 | EV_LPG_COMPENSATION_CABINET ⇒ NEW_OMC_MARKETING_MARGIN → HINDPETRO | +12.00% | +7.20% |
| 1 | EV_IRAN_WAR_HORMUZ_OIL ⇒ C_MIDEAST_CONFLICT → HINDPETRO | -6.75% | -6.75% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → HINDPETRO | -7.50% | -2.68% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ C_MIDEAST_CONFLICT → HINDPETRO | +4.50% | +2.61% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → HINDPETRO | +4.50% | +2.61% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_REFINING_MARGIN → HINDPETRO | -4.00% | -2.32% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ C_MIDEAST_CONFLICT → HINDPETRO | -5.40% | -1.93% |
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_USDINR → HINDPETRO | -1.72% | -1.72% |
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → P_FUEL_TAX_IN → HINDPETRO | +1.58% | +1.58% |
| 1 | EV_RUSSIA_WAIVER_OCT17 ⇒ C_RUSSIA → HINDPETRO | +1.50% | +1.50% |

## Analyst profile (agent research, sourced)
# Hindustan Petroleum (HINDPETRO) — market impact profile (as of 2026-11-05)

## Business
HPCL earns most of its profit in marketing (petrol, diesel, LPG, lubes) where margins are squeezed when crude rises faster than regulated pump prices, and in refining (Mumbai, Visakh, a stake in Bathinda's HMEL and the new Barmer refinery). Because marketing sales are twice refining throughput, HPCL is the most crude-sensitive of the three big OMCs. ONGC owns 54.9%.

## What moves the stock (ranked)
1. **Brent with frozen pump prices (F_BRENT -3.0, C_MIDEAST_CONFLICT -4.5)** — empirical t-stat -4.6. Q1 FY27 operating profit of -Rs 16.1k cr shows the scale.
2. **Refining margins (F_REFINING_MARGIN +5.0).**
3. **Compensation, excise and levies (NEW_OMC_COMPENSATION +4.5, P_FUEL_TAX_IN, P_WINDFALL_EXPORT_TAX).**
4. **Rupee and rates (F_USDINR, F_REPO_IN).**
5. **Operating events** — Visakh refinery fire and HRRL commissioning.

## Worked transmission examples
- Iran-war escalation -> Brent +12% -> pump prices frozen -> HPCL's under-recovery on ~45bn litres of petrol/diesel plus LPG -> quarterly operating loss -> debt rises, interest cover falls (already low) -> government's choice between retail hike (CPI up, RBI easing delayed) or compensation (fiscal slippage, higher G-sec yields) -> ONGC, as 54.9% owner, loses upstream gain on HPCL's consolidated loss (company link via ONGC).
- Crude down 9% (4-5 Nov) -> under-recovery narrows within days -> inventory losses on stocks held -> Q3 FY27 reported profit could still be hit by inventory loss even as underlying margin recovers.
- Visakh outage -> HPCL buys products from others (cost) and loses GRM on ~15 MMTPA -> secondary effect on regional diesel supply and competitors' margins.
- USD/INR up on Brent -> additional import cost on frozen retail -> more under-recovery -> larger compensation ask.

## Current situation
Q2 FY27 consolidated net profit Rs 3.6k cr (Q1: -Rs 12.3k cr). Shares are +8.8% over a month but -21% over a year; yield 6.35%. The 2 Nov fire at Visakh refinery (no casualties) hit sentiment only briefly (+4% on 3 Nov). Nomura is Neutral (TP Rs 380); Prabhudas Lilladher holds with TP Rs 342.

## Upcoming events
Visakh restart, Q3 results (Feb), compensation decision (2027), HRRL start, excise/pump-price moves.

## Bull / bear
Bull: Brent <$85, compensation, GRM >$8, HRRL on time. Bear: Brent re-spikes, Vizag long outage, leveraged balance sheet, no compensation.

*Weights are exposure estimates, not return forecasts.*


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.