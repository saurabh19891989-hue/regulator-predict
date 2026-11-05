# VOLTAS — Voltas Ltd.
*MIDCAP_100 · Consumer Durables · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +0.9%**, **12 months +1.3%** (rank 69 / 67 of 200 for 3m / 12m); beta 1.11
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +27.5%): 3 months 53%, 12 months 40%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -0.5% … P90 +3.5%; plausible 12m relative-return range incl. stock-specific noise: -11.8% … +23.8%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +2.4 pp (model impact +4.8% beta-adjusted vs realised market-adjusted move -16.1%); forward event exposure -0.4% (3m -0.2%; half assumed priced); company-specific events +0.5%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Consumer durables category promotional / discount intensity (`NEW_CONSUMER_DURABLES_PRICE_WAR`) | +1 pp of industry-wide margin given up (discounts, channel incentives, ad spend) in room AC and appliances | -6.00 | -6.00 | +0.00 | +0.00 | +0.00 | — |
| USD/CNY (`F_USDCNY`) | +3% USD/CNY (yuan weaker) | +3.36 | +3.50 | -0.14 | +0.00 | +0.00 | -1.4% |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -3.35 | -3.00 | +0.00 | -0.21 | -0.14 | -1.1% |
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +3.01 | +3.00 | +0.00 | +0.03 | -0.02 | — |
| China growth / stimulus (`F_CHINA_GDP`) | +1 pp | -2.74 | +0.00 | -2.14 | -0.50 | -0.09 | — |
| Copper price (`F_COPPER`) | +10% copper | -2.14 | -2.00 | -0.14 | +0.00 | +0.00 | -2.4% |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -2.06 | +0.00 | -1.32 | -0.50 | -0.25 | — |
| US–China trade decoupling (`C_US_CHINA_DECOUPLING`) | +1 = more decoupling | +2.06 | +0.00 | +1.40 | +0.55 | +0.11 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -1.82 | +0.00 | -0.17 | -1.17 | -0.48 | — |
| Brent crude oil price (`F_BRENT`) | +10% Brent | -1.48 | +0.00 | -0.95 | -0.30 | -0.23 | +0.0% |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +1.31 | +0.00 | +0.92 | +0.26 | +0.14 | — |
| India 10-year G-sec yield (`F_GSEC_10Y_IN`) | +25 bp yield | -1.13 | -1.00 | -0.12 | +0.00 | -0.01 | — |
| Consumer premiumisation (`T_PREMIUMISATION`) | +1 | +1.12 | +1.00 | +0.12 | +0.00 | +0.00 | — |
| Residential real-estate sales (`F_HOUSING_DEMAND`) | +10% sales volume | +1.05 | +1.00 | +0.00 | +0.03 | +0.03 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -2.4% | -2.4% | +0.0 | -1.5 | -0.6 | -0.3 |
| China Q3 GDP +4.5% (beat); property 'mini-stimulus' of late September; PMI 49.3; LPR unchanged (`EV_CHINA_Q3_GDP_AND_MINI_STIMULUS`) | occurred | 1.00 | -2.1% | -2.1% | -1.6 | -0.4 | -0.2 | -0.0 |
| Aluminium -20% since June; copper off record; Nifty Metal -7% in October (`EV_BASE_METALS_ALUMINIUM_SLIDE`) | occurred | 1.00 | +1.9% | +1.9% | +1.9 | +0.0 | +0.0 | +0.0 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -1.6% | -1.6% | -1.4 | -0.2 | -0.0 | -0.0 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -1.6% | -1.6% | +0.0 | -1.4 | -0.0 | -0.2 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.55 | +2.4% | +1.3% | +0.0 | +1.5 | +0.5 | +0.4 |
| India Q1 FY27 GDP grows 7.8% (31 Aug 2026), beating ~7.3% consensus (`EV_GDP_Q1FY27_7_8`) | occurred | 1.00 | +1.2% | +1.2% | +1.2 | +0.1 | -0.1 | -0.1 |
| Rupee at 95-96/USD and heavy RBI FX defence; reserves fall ~US$55bn from peak (`EV_RUPEE_DEFENCE_RESERVES_26`) | occurred | 1.00 | +1.1% | +1.1% | +1.1 | -0.1 | +0.0 | +0.0 |
| China Dec CEWC / Mar 2027 NPC delivers large fiscal stimulus and consumption push (`EV_CHINA_NPC_MAR27_BIG_STIMULUS`) | anticipated | 0.35 | -3.1% | -1.1% | -1.1 | -1.4 | -0.6 | -0.1 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.25 | -4.3% | -1.1% | +0.0 | -2.6 | -0.8 | -0.8 |
| Risk: USD/INR >98 and/or reserves < US$650bn (disorderly rupee, emergency RBI response) (`EV_RUPEE_BREAK_98_RESERVE_STRESS`) | risk_scenario | 0.18 | -5.7% | -1.0% | -4.9 | -0.6 | -0.2 | -0.0 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +1.9% | +1.0% | +0.0 | +1.7 | +0.0 | +0.2 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_USDINR → VOLTAS | -3.90% | -0.70% |
| 2 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → F_USDINR → VOLTAS | +1.38% | +0.69% |
| 2 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → F_USDINR → VOLTAS | +1.23% | +0.68% |
| 2 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → F_USDINR → VOLTAS | -2.09% | -0.52% |
| 1 | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → VOLTAS | +0.48% | +0.43% |
| 2 | EV_CHINA_NPC_MAR27_BIG_STIMULUS ⇒ F_CHINA_GDP → F_COPPER → VOLTAS | -1.17% | -0.41% |
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → VOLTAS | -0.80% | -0.40% |
| 1 | EV_CHINA_NPC_MAR27_BIG_STIMULUS ⇒ F_USDCNY → VOLTAS | -1.05% | -0.37% |
| 1 | EV_CHINA_CEWC_STIMULUS_DEC26 ⇒ F_COPPER → VOLTAS | -0.80% | -0.36% |
| 2 | EV_US_CHINA_TRUCE_EXTENDED ⇒ C_US_CHINA_DECOUPLING → F_USDCNY → VOLTAS | -0.42% | -0.30% |
| 1 | EV_CPI_BREACH_6PCT ⇒ F_GSEC_10Y_IN → VOLTAS | -0.50% | -0.30% |
| 2 | EV_RARE_EARTH_CONTROLS_REIMPOSED ⇒ C_US_CHINA_DECOUPLING → F_USDCNY → VOLTAS | +1.12% | +0.28% |
| 2 | EV_LABOUR_CODES_RULES ⇒ F_WAGES_IN → F_URBAN_DEMAND → VOLTAS | +0.29% | +0.23% |
| 2 | EV_NBS_RABI_HIKE ⇒ P_FERT_SUBSIDY → F_GSEC_10Y_IN → VOLTAS | -0.24% | -0.23% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → F_USDINR → VOLTAS | -0.90% | -0.22% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_USDCNY → VOLTAS | -0.47 | observed | -1.63% |
| 1 | F_GSEC_10Y_IN → VOLTAS | +1.55 | director_override | -1.55% |
| 1 | F_ALUMINIUM → VOLTAS | -1.96 | observed | +1.37% |
| 1 | F_USDINR → VOLTAS | -0.37 | observed | +1.11% |
| 1 | F_URBAN_DEMAND → VOLTAS | +0.20 | events | +0.60% |
| 1 | F_GOVT_CAPEX → VOLTAS | +1.00 | events | +0.60% |
| 1 | F_COPPER → VOLTAS | -0.24 | observed | +0.47% |
| 2 | F_REPO_IN → F_HOUSING_DEMAND → VOLTAS | +1.00 | events | -0.21% |
| 2 | F_GSEC_10Y_IN → F_HOUSING_DEMAND → VOLTAS | +1.55 | director_override | -0.19% |
| 2 | F_GDP_IN → F_HOUSING_DEMAND → VOLTAS | +0.50 | events | +0.12% |
| 2 | T_GENAI_SERVICES → F_HOUSING_DEMAND → VOLTAS | +1.00 | events | -0.08% |
| 2 | F_STEEL_INDIA → F_HOUSING_DEMAND → VOLTAS | +1.35 | events | -0.05% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-11 | Q2 FY27 results (date not verified; SEBI deadline 14 Nov). Off-season quarter; watch UCP margin after 1 Oct price hike and share trends | results | 0.95 | +0.0% | +0.00% |
| 2026-11-04 | Qatar court dismissed OHL appeal in pending Voltas litigation (outcome relative to Voltas not read in full; direction likely favourable) | litigation | 1.00 | +0.5% | +0.50% |
| 2027-01 | Q3 FY27 results | results | 0.95 | +0.0% | +0.00% |
| 2027-03 | Peak summer season sell-in; share defence vs Daikin/LG/Blue Star at 17.3% share | other | 0.90 | +0.0% | +0.00% |

## Analyst profile (agent research, sourced)
# VOLTAS - Voltas Ltd. (midcap, room ACs and projects)

## Business
India's #1 room-AC brand: unitary cooling products are ~80% of Q1 FY27 revenue, projects ~15%, engineered products/Voltas Beko the rest. EBITDA margin ~4% TTM (UCP EBIT 5.3% in Q1 FY27), so every 1pp of discounting or 1% of unhedged cost moves EBITDA 20%+. Secondary market share 17.3% (FY27 to June), lead ~4pp over the nearest rival; management says it prioritises share over margin.

## What moves the stock (ranked)
1. **Category price war (-6.0 per +1pp)** - the largest weight in the book.
2. **USD/INR (-3.0 per +3%)** and **USD/CNY (+3.5 per +3% yuan weakness)** - pack shows USD/CNY +7.29 (t=3.1), the strongest empirical link.
3. **Copper (-2.0 per +10%)** and aluminium (-0.7).
4. **Urban demand and summer (+3.0 per +5pp)**: operating leverage.
5. G-sec yield (-1.0), premiumisation (+1.0), housing (+1.0), government capex (+0.6).

## Transmission examples
- **Middle East escalation -> Brent up -> freight and polymer/foam costs up (2nd) and INR weaker (2nd) -> compressor and coil costs up (3rd) -> RAC list prices raised 5-8% from 1 Oct (4th) -> demand elasticity and rival discounting decide whether the hike sticks.**
- **Copper rally (+28% in 12m) driven by AI/grid demand -> AC BOM up -> industry hikes -> Daikin +8-10% (from 16 Sep), Blue Star +8%, LG +5-7% -> Voltas follows; margin only recovers if the competitors hold price.**
- **China stimulus -> CNY firm -> Chinese compressor/component prices up -> Voltas input costs up (opposite of the CNY-weakness gain).**
- **Brent up -> INR down -> RBI holds -> housing loans dearer -> first-time AC buyers delay -> UCP volumes and mix weaker (4th order).**

## Current situation
Q1 FY27 PAT +51% to Rs213cr on UCP revenue +32% and 1 million RACs in 81 days; Goldman nevertheless cut its target to Rs1,075 (Sell) on revenue miss and margin headwinds. Price Rs1,095 (-19.6% 12m, 3m -14.2%) at 77x trailing earnings. On 2026-11-04 the Qatar court dismissed OHL's appeal in the pending litigation. Q2 FY27 results are due by 14 Nov (date not verified).

## Upcoming
Q2 results (Nov), possible additional AC price hike, Q3 results (Jan), summer 2027 season, Beko/Atomberg JV ramp.

## Bull / bear
Bull: metals and rupee ease, hot summer, share lead converts to 7-8% UCP margin. Bear: copper/INR up with discounting, margin stuck at 4-5%, JV losses and tail legal costs.

Uncertainties: Q2 FY27 not yet in data; USD/INR vs USD/CNY empirical signs partially conflict; litigation outcome direction not verified.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.