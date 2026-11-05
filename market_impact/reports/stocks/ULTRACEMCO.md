# ULTRACEMCO — UltraTech Cement Ltd.
*NIFTY_50 · Construction Materials · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +1.2%**, **12 months +3.5%** (rank 59 / 46 of 200 for 3m / 12m); beta 1.18
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +16.4%): 3 months 56%, 12 months 55%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 +0.9% … P90 +9.1%; plausible 12m relative-return range incl. stock-specific noise: -16.6% … +31.7%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +0.9 pp (model impact +5.4% beta-adjusted vs realised market-adjusted move +3.6%); forward event exposure +5.1% (3m +1.0%; half assumed priced); company-specific events +2.4%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Indian cement trade price (realisation) (`NEW_CEMENT_PRICE_IN`) | +Rs10/bag (~+2.5%) | +6.00 | +6.00 | +0.00 | +0.00 | +0.00 | — |
| Central + state government capex (`F_GOVT_CAPEX`) | +10% capex growth | +2.83 | +2.80 | +0.10 | +0.02 | -0.09 | — |
| Residential real-estate sales (`F_HOUSING_DEMAND`) | +10% sales volume | +2.27 | +2.30 | +0.00 | -0.03 | +0.00 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -2.26 | +0.00 | -1.23 | -0.72 | -0.30 | — |
| Affordable-housing / home-loan support (`P_HOUSING_POLICY`) | +1 = stronger support | +2.16 | +1.80 | +0.37 | +0.00 | -0.01 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -1.80 | +0.00 | -0.96 | -0.39 | -0.45 | — |
| International thermal coal price (`F_COAL_INTL`) | +15% seaborne thermal coal | -1.70 | -1.70 | +0.00 | +0.00 | +0.00 | +0.0% |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -1.39 | -1.00 | -0.26 | -0.11 | -0.02 | — |
| General-government fiscal slippage / extra borrowing vs budget (Centre + states) (`NEW_FISCAL_SLIPPAGE_IN`) | +0.5 pp of GDP deficit above budget (~Rs2 lakh cr) | -1.22 | +0.00 | -0.90 | -0.27 | -0.05 | — |
| Brent crude oil price (`F_BRENT`) | +10% Brent | -1.14 | -0.80 | -0.06 | -0.18 | -0.10 | +0.0% |
| Private corporate capex (`F_PRIVATE_CAPEX`) | +10% capex growth | +1.12 | +1.20 | +0.00 | -0.03 | -0.06 | — |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -1.08 | +0.00 | +0.00 | -0.68 | -0.40 | — |
| China growth / stimulus (`F_CHINA_GDP`) | +1 pp | -1.07 | +0.00 | -0.80 | -0.12 | -0.14 | — |
| OPEC+ crude supply decisions (`NEW_OPEC_PLUS_SUPPLY`) | +1 mb/d OPEC+ production (quota/actual) | +0.80 | +0.00 | +0.51 | +0.08 | +0.21 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -6.1% | -6.1% | -4.0 | -0.3 | -1.3 | -0.5 |
| India Q1 FY27 GDP grows 7.8% (31 Aug 2026), beating ~7.3% consensus (`EV_GDP_Q1FY27_7_8`) | occurred | 1.00 | +2.6% | +2.6% | +2.8 | +0.2 | -0.2 | -0.1 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -2.6% | -2.6% | +0.0 | -1.4 | -0.8 | -0.4 |
| Union Budget 2027-28 capex/railway allocation (infra, railways, defence) (`EV_BUDGET27_CAPEX_RAILWAY`) | scheduled | 0.90 | +2.3% | +2.0% | +2.2 | +0.1 | +0.0 | -0.1 |
| Retail petrol/diesel price freeze with crude >$100 squeezes OMC marketing margins; Q2 FY27 results split refiners (`EV_OMC_FUEL_FREEZE_LOSSES`) | occurred | 1.00 | -1.9% | -1.9% | +0.0 | -2.0 | +0.1 | +0.1 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -1.5% | -1.5% | -1.0 | -0.5 | +0.0 | -0.0 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.58 | +2.0% | +1.2% | +1.2 | +0.1 | +0.5 | +0.2 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.36 | -3.3% | -1.2% | -2.0 | -0.6 | -0.4 | -0.4 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -0.8% | -0.8% | +0.0 | -0.8 | +0.0 | +0.0 |
| US waives Russia-oil secondary sanctions/100% tariff threat on buyers incl. India (17 Oct) (`EV_RUSSIA_WAIVER_OCT17`) | occurred | 1.00 | +0.7% | +0.7% | +0.0 | +0.4 | +0.1 | +0.2 |
| Domestic LPG under-recoveries >Rs59,000 cr (to July); government compensation boosts IOC Q2 (`EV_LPG_UNDERRECOVERY`) | occurred | 1.00 | -0.6% | -0.6% | +0.0 | -0.7 | +0.0 | +0.0 |
| RBI MPC Dec 2026 (~4 Dec): hikes repo another 25 bp to 5.75% (`EV_RBI_DEC26_HIKE25`) | scheduled | 0.40 | -1.5% | -0.6% | -1.0 | -0.5 | +0.0 | -0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → ULTRACEMCO | +2.24% | +2.02% |
| 2 | EV_INDIA_RETAIL_FUEL_HIKE ⇒ NEW_OMC_MARKETING_MARGIN → F_GOVT_CAPEX → ULTRACEMCO | +1.68% | +0.76% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → ULTRACEMCO | -2.00% | -0.71% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → ULTRACEMCO | +1.20% | +0.70% |
| 1 | EV_COAL_IMPORT_BLEND_REVIVED ⇒ F_COAL_INTL → ULTRACEMCO | -0.85% | -0.43% |
| 2 | EV_LPG_COMPENSATION_CABINET ⇒ NEW_OMC_MARKETING_MARGIN → F_GOVT_CAPEX → ULTRACEMCO | +0.67% | +0.40% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → ULTRACEMCO | -1.00% | -0.40% |
| 1 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → ULTRACEMCO | -0.50% | -0.34% |
| 1 | EV_HORMUZ_FULL_CLOSURE ⇒ F_BRENT → ULTRACEMCO | -4.80% | -0.30% |
| 2 | EV_PULSES_VEG_SPIKE_WINTER ⇒ F_CPI_IN → F_REPO_IN → ULTRACEMCO | -1.15% | -0.29% |
| 1 | EV_RBI_FEB27_HIKE25 ⇒ F_REPO_IN → ULTRACEMCO | -1.00% | -0.27% |
| 1 | EV_CPI_BREACH_6PCT ⇒ F_REPO_IN → ULTRACEMCO | -0.40% | -0.24% |
| 2 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → F_HOUSING_DEMAND → ULTRACEMCO | -0.44% | -0.22% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_REPO_IN → ULTRACEMCO | -1.00% | -0.22% |
| 2 | EV_CHINA_NPC_MAR27_BIG_STIMULUS ⇒ F_CHINA_GDP → F_COAL_INTL → ULTRACEMCO | -0.54% | -0.19% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_GOVT_CAPEX → ULTRACEMCO | +1.00 | events | +2.80% |
| 1 | F_COAL_INTL → ULTRACEMCO | +0.70 | director_override | -1.19% |
| 1 | F_REPO_IN → ULTRACEMCO | +1.00 | events | -1.00% |
| 2 | F_GSEC_10Y_IN → F_HOUSING_DEMAND → ULTRACEMCO | +1.70 | events | -0.94% |
| 1 | F_MONSOON → ULTRACEMCO | -1.56 | events | +0.78% |
| 2 | F_GDP_IN → F_HOUSING_DEMAND → ULTRACEMCO | +0.50 | events | +0.28% |
| 2 | F_REPO_IN → F_HOUSING_DEMAND → ULTRACEMCO | +1.00 | events | -0.24% |
| 2 | T_GENAI_SERVICES → F_HOUSING_DEMAND → ULTRACEMCO | +1.00 | events | -0.18% |
| 2 | F_STEEL_INDIA → F_HOUSING_DEMAND → ULTRACEMCO | +1.65 | events | -0.15% |
| 1 | F_USDINR → ULTRACEMCO | -0.37 | observed | +0.15% |
| 2 | F_GDP_IN → F_PRIVATE_CAPEX → ULTRACEMCO | +0.50 | events | +0.12% |
| 2 | F_GOVT_CAPEX → F_PRIVATE_CAPEX → ULTRACEMCO | +1.00 | events | +0.10% |

## Analyst profile (agent research, sourced)
# ULTRACEMCO — UltraTech Cement Ltd. (as of 2026-11-05)

*Facts are from screener.in (evidence pack) and Google News headlines (Sep-Nov 2026); publisher bodies returned 403, so headline-only numbers are flagged. "Model knowledge" items are from memory. No expected-return number is given.*

## Business
UltraTech is India's largest cement maker, a majority-owned (about 56%, model knowledge) Aditya Birla Group subsidiary of Grasim, with grey and white cement, ready-mix and overseas plants. Q2 FY27 sales were Rs 23,295 cr (+19% y/y), EBITDA Rs 3,719 cr (OPM 16%), PAT Rs 1,501 cr (+21%). TTM sales Rs 95,572 cr and EBITDA Rs 18,244 cr. The stock (Rs 12,243, P/E 40.6) is the premium-quality name, up 13.9% in a month.

## What moves the stock (ranked)
1. **Cement price (NEW_CEMENT_PRICE_IN, +6.0 per Rs 10/bag):** about 16% EBITDA per Rs 10/bag. Nomura (12 Oct) calls Rs 12-15/bag hikes necessary just to offset fuel, and names UltraTech top pick.
2. **Government and infrastructure capex (+2.8 per +10%):** the highest infra/institutional exposure among peers.
3. **Housing demand (+2.3 per +10%)** and **housing policy (+1.8)**.
4. **Kiln fuel (F_COAL_INTL -1.7 per +15%):** lower than Ambuja because of high waste-heat and green-power share.
5. **Rates and valuation (F_REPO_IN -1.0 per 25 bp):** at 40x earnings the multiple is the exposure; RBI hiked on 7 Oct.
6. **Brent/freight (-0.8 per +10%),** FX (-0.4 per +3%), monsoon, royalty.

## Transmission examples
- **Middle East escalation -> Brent up -> petcoke and diesel up -> cement cost up -> margins down.** C_MIDEAST_CONFLICT -> Brent +10% (1st) -> diesel and freight +0.5% of costs, petcoke landed cost up (2nd) -> cost per tonne +Rs 120-200 (3rd) -> industry attempts Rs 10-15/bag hikes; UltraTech, with scale and WHRS, keeps spread better than weaker peers (4th, relative positive).
- **Brent up -> INR weaker -> RBI tight -> housing weaker -> volumes lower.** At USD/INR 94.5 and Brent $95, RBI hiked to 5.50% and says no cuts near-term, so home-loan rates stay higher and housing demand (65% of cement) slows; volume growth falls from the +19% Q2 pace.
- **Infra capex -> clinker demand -> operating leverage.** Union Budget (1 Feb 2027) raising road/rail capex +10% -> +1.7% volume -> +5.8% EBITDA -> +2.8% equity.
- **Peer capacity wave -> competition.** Ambuja's 30 MTPA (2 Nov) and others lift supply; if demand lags, regional price cuts erode the very price term (NEW_CEMENT_PRICE_IN) that is UltraTech's largest driver.

## Current situation
Q2 FY27 (19 Oct): profit +21% on volume and efficiency; shares dipped 5% from the day's high, then rose 3% on 21 Oct as brokerages (Jefferies, Citi) split. Q2 EBITDA fell 29% q/q seasonally (monsoon) and OPM was 16% vs 20% in Q1. Stated ambition: 240 MT capacity and Rs 1,400 EBITDA/t (Sahi headline; timeline not verified). Nuvama is neutral on costs, JK Cement its top pick; InCred sees recovery.

## Upcoming
Price-hike realisation (Nov-Dec); Q3 FY27 results (mid/late Jan 2027, estimate); Union Budget 1 Feb 2027; RBI December policy; capacity commissioning.

## Bull case
Hikes hold, fuel eases, demand revives post-monsoon and with festive/GST tailwinds, EBITDA/t moves to Rs 1,300+, multiple holds near 18x EV/EBITDA.

## Bear case
Fuel costs stay high, rate hike slows housing, competitor capacity forces price cuts, and the 40x P/E de-rates toward 30x.

## Uncertainties
Cost shares are model estimates; EBITDA/t, debt and India Cements stake not verified; Q2 PAT differs slightly across headlines (Rs 1,494 vs 1,501 cr).


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.