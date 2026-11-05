# INDHOTEL — Indian Hotels Co. Ltd.
*MIDCAP_100 · Consumer Services · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -0.6%**, **12 months -0.6%** (rank 124 / 116 of 200 for 3m / 12m); beta 1.17
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +17.2%): 3 months 47%, 12 months 50%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -8.4% … P90 +3.7%; plausible 12m relative-return range incl. stock-specific noise: -21.3% … +29.8%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves -1.3 pp (model impact -2.5% beta-adjusted vs realised market-adjusted move +28.8%); forward event exposure +2.4% (3m +0.6%; half assumed priced); company-specific events +1.2%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Air/hotel/tourism demand (`F_TRAVEL_DEMAND`) | +10% | +5.00 | +5.00 | +0.00 | +0.00 | +0.00 | — |
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +4.64 | +2.50 | +2.30 | -0.09 | -0.07 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -4.00 | -2.50 | -0.78 | -0.39 | -0.33 | — |
| Consumer premiumisation (`T_PREMIUMISATION`) | +1 | +3.67 | +3.00 | +0.50 | +0.17 | -0.00 | — |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +3.52 | +0.00 | +1.30 | +2.15 | +0.07 | — |
| India real GDP growth (`F_GDP_IN`) | +1 pp | +3.29 | +3.50 | -0.25 | -0.05 | +0.08 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -3.22 | +0.00 | -2.16 | -0.86 | -0.20 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +2.45 | +2.50 | -0.07 | -0.01 | +0.04 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -2.08 | -1.50 | -0.13 | -0.32 | -0.13 | — |
| Private corporate capex (`F_PRIVATE_CAPEX`) | +10% capex growth | +2.05 | +0.00 | +2.24 | -0.24 | +0.05 | — |
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | +1.90 | +0.00 | +2.24 | -0.28 | -0.05 | — |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -1.81 | +0.00 | +0.00 | -1.36 | -0.45 | — |
| Monsoon rainfall vs normal (`F_MONSOON`) | +10% above long-period average | +1.79 | +0.00 | +0.93 | +0.35 | +0.51 | — |
| Brent crude oil price (`F_BRENT`) | +10% Brent | -1.37 | -0.80 | -0.23 | -0.23 | -0.11 | +0.0% |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -11.3% | -11.3% | -7.7 | -1.6 | -1.3 | -0.6 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -5.4% | -5.4% | -5.5 | +0.2 | +0.0 | -0.1 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -3.9% | -3.9% | +0.0 | -2.5 | -1.2 | -0.2 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.58 | +5.5% | +3.2% | +3.7 | +1.1 | +0.6 | +0.2 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +6.1% | +3.1% | +6.2 | -0.2 | -0.0 | +0.1 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.36 | -8.4% | -3.0% | -5.0 | -1.9 | -1.1 | -0.3 |
| India Q1 FY27 GDP grows 7.8% (31 Aug 2026), beating ~7.3% consensus (`EV_GDP_Q1FY27_7_8`) | occurred | 1.00 | +2.3% | +2.3% | +2.2 | +0.2 | -0.1 | -0.0 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -2.3% | -2.3% | +0.0 | -1.2 | -0.4 | -0.6 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -2.2% | -2.2% | -1.5 | -0.1 | -0.4 | -0.1 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.28 | -5.6% | -1.6% | +0.0 | -5.7 | -0.2 | +0.3 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -1.4% | -1.4% | +0.0 | -1.5 | +0.1 | +0.0 |
| Disorderly yen carry-trade unwind (Aug-2024-style) after BoJ/MoF action (`EV_YEN_CARRY_UNWIND_RISK`) | risk_scenario | 0.18 | -7.2% | -1.3% | +0.0 | -7.2 | +0.1 | -0.1 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → INDHOTEL | +6.25% | +3.12% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ C_MIDEAST_CONFLICT → INDHOTEL | +2.50% | +1.45% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ C_MIDEAST_CONFLICT → INDHOTEL | -3.00% | -1.07% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → INDHOTEL | -3.73% | -1.05% |
| 2 | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → F_GDP_IN → INDHOTEL | +1.01% | +0.91% |
| 2 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → INDHOTEL | -4.67% | -0.84% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → INDHOTEL | -3.75% | -0.82% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → INDHOTEL | -2.00% | -0.71% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → INDHOTEL | +1.20% | +0.70% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → INDHOTEL | -2.40% | -0.67% |
| 2 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_GDP_IN → INDHOTEL | +0.93% | +0.63% |
| 1 | EV_INDIA_STAGFLATION_SCARE ⇒ F_GDP_IN → INDHOTEL | -5.25% | -0.63% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_FPI_FLOWS → INDHOTEL | -2.40% | -0.60% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → INDHOTEL | -1.50% | -0.60% |
| 1 | EV_Q2_FY27_GDP_STRONG ⇒ F_GDP_IN → INDHOTEL | +0.70% | +0.56% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_FPI_FLOWS → INDHOTEL | -1.60 | events | -4.00% |
| 1 | C_MIDEAST_CONFLICT → INDHOTEL | +1.50 | events | -3.75% |
| 1 | F_GDP_IN → INDHOTEL | +0.50 | events | +1.75% |
| 1 | F_REPO_IN → INDHOTEL | +1.00 | events | -1.50% |
| 1 | F_URBAN_DEMAND → INDHOTEL | +0.20 | events | +0.50% |
| 2 | C_MIDEAST_CONFLICT → F_TRAVEL_DEMAND → INDHOTEL | +1.50 | events | -0.45% |
| 2 | F_URBAN_DEMAND → F_TRAVEL_DEMAND → INDHOTEL | +0.20 | events | +0.32% |
| 1 | F_USDINR → INDHOTEL | -0.37 | observed | -0.30% |
| 1 | F_BRENT → INDHOTEL | +0.00 | observed | -0.00% |

## Analyst profile (agent research, sourced)
# INDHOTEL — Indian Hotels Co. Ltd. (Taj), as of 2026-11-05

*Screener was blocked, so fundamentals are headline-based (Google News, Oct 2026) plus labelled model knowledge.*

## Business
IHCL is India's largest hospitality company: Taj, SeleQtions, Vivanta, Ginger and Gateway, increasingly asset-light via management contracts, targeting a ~700-hotel portfolio by FY27 (Business Standard, 22 Oct). Q2 FY27 revenue was Rs 2,566 cr (+21%); FY27 revenue growth guidance was raised by 300 bp to 15-17% (ET HospitalityWorld, Hotelier India). The stock hit a 52-week high around Rs 868 (+29.7% in 6m, +17.9% in 1m).

## What moves the stock (ranked)
1. Travel and corporate/leisure demand (F_TRAVEL_DEMAND +5 per +10%; F_GDP_IN +3.5 per pp).
2. Luxury/premiumisation and wedding spend (T_PREMIUMISATION +3).
3. Urban demand (+2.5).
4. Geopolitics: Mideast conflict (-2.5) and India-Pakistan tension (travel disruption).
5. FPI flows (+2.5) and rates (-1.5).
6. Costs: wages (-0.6), fuel (-0.8). FX is a mild positive (+0.8) as foreign-guest revenue rises with a weaker rupee.

## Transmission examples
- **Mideast escalation** -> Gulf airspace/hub disruption and Brent up -> airfares rise, inbound/outbound travel falls (1st-2nd) -> RevPAR growth slows in luxury and Gulf-linked markets, power costs rise (3rd) -> guidance trimmed and FPIs cut high-beta consumer names (4th).
- **Strong GDP and festive season** -> corporate travel, MICE and weddings -> ARR up in capacity-constrained cities -> operating leverage (65% flow-through) -> estimate upgrades (as in Oct) -> FPI buying.
- **Weaker INR** -> foreign tourists find India cheaper -> USD-priced rooms yield more rupees; overseas hotel profits translate higher; but imports (equipment, F&B) rise slightly.
- **Rate cuts** -> real estate and hotel developers' capex cheaper, discount rate down -> multiple expands; new supply risk grows later (>12m).

## Current situation
Peers confirm strength: SAMHI occupancy 78.6% and RevPAR +14.3% (4 Nov); Motilal Oswal sees up to 34% upside across hotel stocks (2 Oct). PL Capital included IHCL in its Diwali picks (31 Oct). MarketsMOJO rates it Hold (momentum high, valuation stretched).

## Upcoming
Q3 FY27 results (~early Feb 2027), Budget (1 Feb), new signings.

## Bull / bear
Bull: guidance raised again, ARR growth above 10%, signings pace. Bear: rally 18% in a month leaves little margin of safety; geopolitical shock; supply additions in 2027-28.

## Uncertainties
No fundamentals or EV/EBITDA retrieved; mix and cost shares are model estimates; all weights low confidence.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.