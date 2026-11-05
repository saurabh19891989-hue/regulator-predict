# M&M — Mahindra & Mahindra Ltd.
*NIFTY_50 · Automobile and Auto Components · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +3.6%**, **12 months +5.1%** (rank 23 / 29 of 200 for 3m / 12m); beta 1.45
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +16.9%): 3 months 66%, 12 months 60%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 +3.3% … P90 +9.7%; plausible 12m relative-return range incl. stock-specific noise: -13.5% … +26.2%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +2.9 pp (model impact +5.8% beta-adjusted vs realised market-adjusted move -2.7%); forward event exposure +4.3% (3m +3.0%; half assumed priced); company-specific events +2.1%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +3.43 | +2.00 | +1.09 | +0.33 | +0.01 | — |
| Indian vehicle demand (`F_AUTO_DEMAND_IN`) | +10% volumes | +2.50 | +2.50 | +0.00 | +0.00 | +0.00 | — |
| Chip/electronics component supply tightness (higher = tighter) (`F_SEMICONDUCTOR_SUPPLY`) | +1 = tightening | -2.00 | -2.00 | +0.00 | +0.00 | +0.00 | — |
| Consumer premiumisation (`T_PREMIUMISATION`) | +1 | +1.54 | +1.50 | +0.00 | +0.04 | -0.01 | — |
| EV incentives / mandates (`P_EV_POLICY`) | +1 = stronger EV push | +1.47 | +1.50 | -0.02 | -0.01 | +0.00 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -1.33 | +0.00 | -0.88 | -0.53 | +0.08 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -1.16 | +0.00 | -1.02 | +0.08 | -0.22 | — |
| Critical-mineral supply tightness (China export controls on rare earths, magnets, graphite, Ga/Ge) (`NEW_RARE_EARTH_SUPPLY`) | +1 = new/tighter export-control round | -1.12 | +0.00 | -1.11 | -0.01 | +0.00 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -1.02 | -0.80 | -0.16 | -0.04 | -0.02 | — |
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | +0.96 | +0.80 | +0.41 | -0.15 | -0.10 | — |
| China growth / stimulus (`F_CHINA_GDP`) | +1 pp | -0.94 | +0.00 | -0.47 | -0.29 | -0.19 | — |
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +0.92 | +0.00 | +1.20 | -0.19 | -0.09 | — |
| Brent crude oil price (`F_BRENT`) | +10% Brent | -0.91 | -0.80 | +0.03 | -0.09 | -0.05 | +0.0% |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -0.88 | +0.00 | -0.06 | -0.55 | -0.27 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -1.6% | -1.6% | +0.0 | -1.1 | -0.7 | +0.1 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -1.0% | -1.0% | -0.8 | -0.2 | -0.0 | -0.0 |
| CAFE-III fuel-efficiency norms notified (30 Sep 2026); no small-car carve-out; 3x credit for BEVs (`EV_CAFE3_NOTIFIED`) | occurred | 1.00 | +0.9% | +0.9% | +1.0 | -0.0 | -0.0 | +0.0 |
| Global and Indian steel prices at multi-year highs (global HRC +60% y/y) (`EV_STEEL_RALLY_2026`) | occurred | 1.00 | -0.9% | -0.9% | -0.9 | +0.0 | -0.0 | +0.0 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.55 | +1.3% | +0.7% | +1.0 | +0.0 | +0.1 | +0.1 |
| US waives Russia-oil secondary sanctions/100% tariff threat on buyers incl. India (17 Oct) (`EV_RUSSIA_WAIVER_OCT17`) | occurred | 1.00 | +0.6% | +0.6% | +0.2 | +0.4 | -0.0 | +0.1 |
| Aluminium -20% since June; copper off record; Nifty Metal -7% in October (`EV_BASE_METALS_ALUMINIUM_SLIDE`) | occurred | 1.00 | +0.5% | +0.5% | +0.5 | +0.0 | +0.0 | +0.0 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.25 | -2.1% | -0.5% | -1.8 | +0.0 | -0.2 | -0.2 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -0.5% | -0.5% | +0.0 | -0.2 | -0.1 | -0.1 |
| Kharif 2026 output hit: paddy area down, foodgrain target cut, rice output seen sharpest fall in ~2 decades (`EV_KHARIF26_OUTPUT_HIT`) | occurred | 1.00 | -0.4% | -0.4% | +0.0 | -0.0 | -0.3 | -0.1 |
| PM E-DRIVE extended to March 2028; e2W incentive cut to Rs 5,000 (`EV_PM_EDRIVE_EXT`) | occurred | 1.00 | +0.4% | +0.4% | +0.4 | -0.0 | -0.0 | +0.0 |
| RBI MPC Dec 2026 (~4 Dec): hikes repo another 25 bp to 5.75% (`EV_RBI_DEC26_HIKE25`) | scheduled | 0.42 | -1.0% | -0.4% | -0.8 | -0.2 | -0.0 | -0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → M&M | +1.04% | +0.57% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → M&M | -1.76% | -0.44% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_AI_CAPEX → F_SEMICONDUCTOR_SUPPLY → M&M | +1.44% | +0.36% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → M&M | -0.80% | -0.34% |
| 2 | EV_RARE_EARTH_CONTROLS_REIMPOSED ⇒ NEW_RARE_EARTH_SUPPLY → F_AUTO_DEMAND_IN → M&M | -1.20% | -0.30% |
| 2 | EV_PULSES_VEG_SPIKE_WINTER ⇒ F_CPI_IN → F_REPO_IN → M&M | -0.92% | -0.23% |
| 1 | EV_RBI_FEB27_HIKE25 ⇒ F_REPO_IN → M&M | -0.80% | -0.22% |
| 1 | EV_CPI_BREACH_6PCT ⇒ F_REPO_IN → M&M | -0.32% | -0.19% |
| 1 | EV_HORMUZ_FULL_CLOSURE ⇒ F_BRENT → M&M | -3.60% | -0.18% |
| 1 | EV_INDIA_HR_STEEL_AD_PROVISIONAL ⇒ F_STEEL_INDIA → M&M | -0.32% | -0.18% |
| 1 | EV_BUDGET27_AGRI_RURAL ⇒ F_RURAL_DEMAND → M&M | +0.24% | +0.17% |
| 1 | EV_RUSSIA_TARIFF_ENFORCED ⇒ P_US_TARIFF_INDIA → M&M | -1.00% | -0.15% |
| 1 | EV_RARE_EARTH_CONTROLS_REIMPOSED ⇒ F_SEMICONDUCTOR_SUPPLY → M&M | -0.60% | -0.15% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_GDP → F_BRENT → M&M | +0.58% | +0.14% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_REPO_IN → M&M | -0.80% | -0.14% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | P_EV_POLICY → M&M | +1.10 | events | +1.65% |
| 1 | F_STEEL_INDIA → M&M | +1.35 | events | -1.08% |
| 1 | F_REPO_IN → M&M | +1.00 | events | -0.80% |
| 1 | F_ALUMINIUM → M&M | -1.96 | observed | +0.49% |
| 1 | F_AUTO_DEMAND_IN → M&M | -0.10 | events | -0.25% |
| 1 | P_US_TARIFF_INDIA → M&M | -0.60 | events | +0.24% |
| 1 | F_RURAL_DEMAND → M&M | -0.25 | events | -0.20% |
| 2 | F_AI_CAPEX → F_SEMICONDUCTOR_SUPPLY → M&M | -0.30 | events | +0.14% |
| 1 | F_USDINR → M&M | -0.37 | observed | -0.07% |
| 2 | C_US_CHINA_DECOUPLING → F_SEMICONDUCTOR_SUPPLY → M&M | -0.10 | events | +0.06% |
| 1 | F_COPPER → M&M | -0.24 | observed | +0.05% |
| 3 | C_US_CHINA_DECOUPLING → NEW_RARE_EARTH_SUPPLY → F_SEMICONDUCTOR_SUPPLY → M&M | -0.10 | events | +0.02% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-11-08 | Diwali: delayed tractor retail and SUV festive deliveries (Oct tractor sales -12% on calendar shift) | other | 0.95 | +1.2% | +1.19% |
| 2026-12 | US-India trade agreement or tariff change | regulatory | 0.30 | +1.0% | +0.30% |
| 2026-12-01 | November sales: tractor rebound test and SUV order book | guidance | 0.99 | +0.5% | +0.49% |
| 2027-01 | SML Mahindra truck and bus division acquisition (Rs 525 cr) completion | corporate_action | 0.70 | +0.1% | +0.07% |
| 2027-02 | Q3 FY27 results (auto margin recovery vs commodity; farm margin) | results | 0.97 | +0.0% | +0.00% |

## Analyst profile (agent research, sourced)
# M&M - Mahindra & Mahindra Ltd. (as of 2026-11-05)

## Business
M&M is India's largest tractor maker and a top-three SUV maker. Standalone Q2 FY27 revenue was Rs 44,282 cr (+26%); the auto segment sold ~3.31 lakh vehicles (UV 1.83 lakh, record SUV month of 73,338 in October) and the farm segment 1.16 lakh tractors (-6%). It also owns about 52% of Mahindra Finance and about 26% of Tech Mahindra (stakes from model knowledge, to verify), which are a significant part of its market value. Promoter holding is just 18.4%; FIIs have trimmed from 36.2% to 33.3% while DIIs rose to 34.2% over two quarters.

## What moves the stock (ranked, % equity value per standard shock)
1. **SUV/auto volumes and share** (F_AUTO_DEMAND_IN +2.5 per +10%; T_PREMIUMISATION +1.5): product cycle is strong but Tata overtook Mahindra in H1 FY27 PV share.
2. **Metals and battery costs** (steel -0.8 per +7%, aluminium -0.25, copper -0.2, cells -0.3): standalone EBITDA grew only 4% on 26% revenue growth, margin 15.2% vs 18.4%; aluminium -20% since June is a relief.
3. **Rates** (F_REPO_IN -0.8 per +25bp): hits SUV and tractor finance and the Mahindra Finance subsidiary; RBI hiked to 5.50% on 2026-10-07.
4. **Rural/farm** (F_RURAL_DEMAND +0.8): domestic tractors +2% over Apr-Oct, Oct -13% from a Diwali calendar shift (Diwali falls ~8 Nov).
5. **Subsidiary values** (TECHM link 0.08, M&MFIN link 0.04): Tech Mahindra moves and Mahindra Finance credit news transmit at roughly 8% and 4% of their percentage moves.
6. **Policy** (P_EV_POLICY +1.5, P_GST_CONSUMPTION +2.0, P_US_TARIFF_INDIA -0.4).

## Worked chains
- **US-Israeli war on Iran escalates -> Brent up (1st) -> diesel and CNG cost up, rural freight and farm input costs rise (2nd) -> tractor buying delayed and rural sentiment weaker (3rd) -> farm EBITDA down and Mahindra Finance collections on tractor loans slow (4th).**
- **Brent up -> INR weaker (2nd) -> imported electronics/EV cells costlier (3rd) -> BEV margins squeezed vs PLI offset (4th); simultaneously Tech Mahindra benefits from weaker INR, cushioning the stake value.**
- **Brent up -> CPI up (2nd) -> RBI hikes again (3rd) -> higher vehicle loan rates (4th) -> SUV volumes -0.4% per 25bp, Mahindra Finance NIM compresses unless repriced.**
- **US tariff easing after midterms -> risk-on, FPI inflow (2nd) -> FII reaccumulation in an under-owned heavyweight (3rd) -> multiple expansion (4th).**

## Current situation
Q2 FY27 (2026-11-05): standalone profit Rs 5,102 cr (+13%) beat estimates but margin contracted; the stock gained ~4.8% to ~Rs 3,104 yet is -17.6% YTD. The consolidated profit figure in press (Rs 4,588 cr) looks inconsistent with Q1 and should be reconciled. Mahindra Finance's Q2 PAT of Rs 882 cr (+55%) did not stop a 10% fall in that stock on 22 October, which also affects the stake value. SML Mahindra (Rs 525 cr truck/bus unit purchase) should complete by January 2027.

## Upcoming
November sales (1 Dec), RBI December MPC, Q3 results (~Feb 2027), US-India trade developments.

## Bull and bear
Bull: strong SUV and EV pipeline with PLI, tractor rebound after Diwali, lower aluminium and crude, FII return, sum-of-parts upside. Bear: share loss to Tata/Maruti, rate hikes, weak rural, margin squeeze and subsidiary volatility.

Confidence: medium (low on stake percentages and the consolidated Q2 figure).


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.