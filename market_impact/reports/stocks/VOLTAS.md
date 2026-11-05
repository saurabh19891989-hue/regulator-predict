# VOLTAS — Voltas Ltd.
*MIDCAP_100 · Consumer Durables · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +0.8%**, **12 months +1.8%** (rank 72 / 72 of 200 for 3m / 12m); beta 1.11
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +27.5%): 3 months 52%, 12 months 60%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -1.6% … P90 +5.3%; plausible 12m relative-return range incl. stock-specific noise: -30.0% … +30.6%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +2.5 pp (model impact +5.0% beta-adjusted vs realised market-adjusted move -16.1%); forward event exposure +0.3% (3m -0.4%; half assumed priced); company-specific events +0.5%

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
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -7.9% | -7.9% | +0.0 | -4.9 | -1.7 | -1.3 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -2.4% | -2.4% | +0.0 | -1.5 | -0.6 | -0.3 |
| China Q3 GDP +4.5% (beat); property 'mini-stimulus' of late September; PMI 49.3; LPR unchanged (`EV_CHINA_Q3_GDP_AND_MINI_STIMULUS`) | occurred | 1.00 | -2.1% | -2.1% | -1.6 | -0.4 | -0.2 | -0.0 |
| Aluminium -20% since June; copper off record; Nifty Metal -7% in October (`EV_BASE_METALS_ALUMINIUM_SLIDE`) | occurred | 1.00 | +1.9% | +1.9% | +1.9 | +0.0 | +0.0 | +0.0 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.36 | -4.8% | -1.7% | +0.0 | -3.0 | -1.0 | -0.9 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -1.7% | -1.7% | +0.0 | -1.5 | -0.0 | -0.2 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -1.6% | -1.6% | -1.4 | -0.2 | -0.0 | -0.0 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.58 | +2.8% | +1.6% | +0.0 | +1.8 | +0.5 | +0.5 |
| Risk: USD/INR >98 and/or reserves < US$650bn (disorderly rupee, emergency RBI response) (`EV_RUPEE_BREAK_98_RESERVE_STRESS`) | risk_scenario | 0.22 | -5.7% | -1.2% | -4.9 | -0.6 | -0.2 | -0.0 |
| India Q1 FY27 GDP grows 7.8% (31 Aug 2026), beating ~7.3% consensus (`EV_GDP_Q1FY27_7_8`) | occurred | 1.00 | +1.2% | +1.2% | +1.2 | +0.1 | -0.1 | -0.1 |
| Rupee at 95-96/USD and heavy RBI FX defence; reserves fall ~US$55bn from peak (`EV_RUPEE_DEFENCE_RESERVES_26`) | occurred | 1.00 | +1.1% | +1.1% | +1.1 | -0.1 | +0.0 | +0.0 |
| China Dec CEWC / Mar 2027 NPC delivers large fiscal stimulus and consumption push (`EV_CHINA_NPC_MAR27_BIG_STIMULUS`) | anticipated | 0.35 | -3.1% | -1.1% | -1.1 | -1.4 | -0.6 | -0.1 |

## Strongest causal chains (1st–4th order)
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_USDINR → VOLTAS | -4.69% | -4.69% |
| 1 | EV_CHINA_Q3_GDP_AND_MINI_STIMULUS ⇒ F_USDCNY → VOLTAS | -1.58% | -1.58% |
| 1 | EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26 ⇒ F_GSEC_10Y_IN → VOLTAS | -1.40% | -1.40% |
| 1 | EV_BASE_METALS_ALUMINIUM_SLIDE ⇒ F_ALUMINIUM → VOLTAS | +1.37% | +1.37% |
| 2 | EV_FPI_RECORD_OUTFLOW_26 ⇒ F_FPI_FLOWS → F_USDINR → VOLTAS | -1.21% | -1.21% |
| 1 | EV_RUPEE_DEFENCE_RESERVES_26 ⇒ F_USDINR → VOLTAS | +1.11% | +1.11% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_USDINR → VOLTAS | -3.90% | -0.86% |
| 2 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → F_USDINR → VOLTAS | -2.37% | -0.85% |
| 2 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → F_USDINR → VOLTAS | +1.42% | +0.83% |
| 2 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → F_USDINR → VOLTAS | +1.38% | +0.69% |
| 2 | EV_CPI_REACCEL_SEP26 ⇒ F_CPI_IN → F_USDINR → VOLTAS | -0.69% | -0.69% |
| 2 | EV_UST_SELLOFF_SEP26 ⇒ F_DXY → F_USDCNY → VOLTAS | +0.61% | +0.61% |
| 1 | EV_GDP_Q1FY27_7_8 ⇒ F_URBAN_DEMAND → VOLTAS | +0.60% | +0.60% |
| 1 | EV_GDP_Q1FY27_7_8 ⇒ F_GOVT_CAPEX → VOLTAS | +0.60% | +0.60% |
| 2 | EV_PRECIOUS_METALS_CRASH_2026 ⇒ F_DXY → F_USDCNY → VOLTAS | +0.59% | +0.59% |

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