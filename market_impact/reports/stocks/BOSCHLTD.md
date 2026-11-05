# BOSCHLTD — Bosch Ltd.
*NIFTY_NEXT_50 · Automobile and Auto Components · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -1.6%**, **12 months -2.7%** (rank 144 / 143 of 200 for 3m / 12m); beta 1.10
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +25.9%): 3 months 45%, 12 months 50%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -6.5% … P90 -0.7%; plausible 12m relative-return range incl. stock-specific noise: -17.1% … +36.6%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves -1.3 pp (model impact -2.7% beta-adjusted vs realised market-adjusted move +35.7%); forward event exposure -2.0% (3m -1.0%; half assumed priced); company-specific events +1.5%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Indian vehicle demand (`F_AUTO_DEMAND_IN`) | +10% volumes | +6.00 | +6.00 | +0.00 | +0.00 | +0.00 | — |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +5.35 | +2.00 | +2.46 | +0.63 | +0.26 | — |
| Chip/electronics component supply tightness (higher = tighter) (`F_SEMICONDUCTOR_SUPPLY`) | +1 = tightening | -4.00 | -4.00 | +0.00 | +0.00 | +0.00 | — |
| Critical-mineral supply tightness (China export controls on rare earths, magnets, graphite, Ga/Ge) (`NEW_RARE_EARTH_SUPPLY`) | +1 = new/tighter export-control round | -3.36 | +0.00 | -3.36 | +0.00 | +0.00 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -3.34 | +0.00 | -1.26 | -2.19 | +0.11 | — |
| EV incentives / mandates (`P_EV_POLICY`) | +1 = stronger EV push | -3.02 | -3.00 | +0.00 | -0.02 | -0.01 | — |
| Auto safety and emission norm tightening (ADAS/airbags, CAFE-III, BS-VII) (`NEW_AUTO_SAFETY_EMISSION_NORMS`) | +1 = a material tightening step | +2.50 | +2.50 | +0.00 | +0.00 | +0.00 | — |
| US–China trade decoupling (`C_US_CHINA_DECOUPLING`) | +1 = more decoupling | -2.46 | +0.00 | -1.28 | -1.34 | +0.17 | — |
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +2.44 | +0.00 | +2.88 | -0.13 | -0.31 | — |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -2.03 | +0.00 | +0.00 | -0.84 | -1.19 | — |
| India 10-year G-sec yield (`F_GSEC_10Y_IN`) | +25 bp yield | -1.99 | -2.00 | +0.00 | +0.00 | +0.01 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -1.89 | -1.00 | -0.15 | -0.41 | -0.34 | -1.1% |
| Consumer premiumisation (`T_PREMIUMISATION`) | +1 | +1.61 | +1.50 | +0.00 | +0.11 | +0.00 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -1.60 | +0.00 | -0.72 | -0.39 | -0.49 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -4.0% | -4.0% | +0.0 | -1.4 | -2.7 | +0.1 |
| CAFE-III fuel-efficiency norms notified (30 Sep 2026); no small-car carve-out; 3x credit for BEVs (`EV_CAFE3_NOTIFIED`) | occurred | 1.00 | -3.0% | -3.0% | -3.0 | +0.0 | -0.0 | -0.0 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -2.8% | -2.8% | -2.8 | +0.0 | +0.0 | -0.0 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -1.6% | -1.6% | -1.1 | -0.3 | -0.1 | -0.1 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -1.2% | -1.2% | +0.0 | -0.8 | -0.1 | -0.3 |
| China re-imposes/hardens rare-earth and critical-mineral export controls hitting India's autos and electronics (`EV_RARE_EARTH_CONTROLS_REIMPOSED`) | risk_scenario | 0.25 | -4.5% | -1.1% | -1.2 | -3.6 | +0.1 | +0.1 |
| Aluminium -20% since June; copper off record; Nifty Metal -7% in October (`EV_BASE_METALS_ALUMINIUM_SLIDE`) | occurred | 1.00 | +1.1% | +1.1% | +1.1 | +0.0 | +0.0 | +0.0 |
| Global and Indian steel prices at multi-year highs (global HRC +60% y/y) (`EV_STEEL_RALLY_2026`) | occurred | 1.00 | -1.0% | -1.0% | -1.0 | +0.0 | -0.0 | -0.0 |
| Kharif 2026 output hit: paddy area down, foodgrain target cut, rice output seen sharpest fall in ~2 decades (`EV_KHARIF26_OUTPUT_HIT`) | occurred | 1.00 | -1.0% | -1.0% | +0.0 | +0.0 | -0.4 | -0.6 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.55 | +1.8% | +1.0% | +0.7 | +0.4 | +0.3 | +0.5 |
| CPI prints >=6.0% (RBI upper tolerance) in Oct-Jan data (releases 12 Nov - 12 Feb) (`EV_CPI_BREACH_6PCT`) | anticipated | 0.60 | -1.5% | -0.9% | -1.2 | -0.2 | -0.3 | +0.2 |
| PM E-DRIVE extended to March 2028; e2W incentive cut to Rs 5,000 (`EV_PM_EDRIVE_EXT`) | occurred | 1.00 | -0.9% | -0.9% | -0.9 | +0.0 | -0.0 | -0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → BOSCHLTD | -1.60% | -0.80% |
| 2 | EV_RARE_EARTH_CONTROLS_REIMPOSED ⇒ NEW_RARE_EARTH_SUPPLY → F_AUTO_DEMAND_IN → BOSCHLTD | -2.88% | -0.72% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_AI_CAPEX → F_SEMICONDUCTOR_SUPPLY → BOSCHLTD | +2.88% | +0.72% |
| 1 | EV_CPI_BREACH_6PCT ⇒ F_GSEC_10Y_IN → BOSCHLTD | -1.00% | -0.60% |
| 2 | EV_NBS_RABI_HIKE ⇒ P_FERT_SUBSIDY → F_GSEC_10Y_IN → BOSCHLTD | -0.48% | -0.46% |
| 2 | EV_BUDGET27_AGRI_RURAL ⇒ F_RURAL_DEMAND → F_AUTO_DEMAND_IN → BOSCHLTD | +0.59% | +0.41% |
| 1 | EV_FERT_SUBSIDY_TOPUP_WINTER ⇒ F_GSEC_10Y_IN → BOSCHLTD | -0.40% | -0.36% |
| 1 | EV_BANKING_LIQUIDITY_DEFICIT_MAR27 ⇒ F_GSEC_10Y_IN → BOSCHLTD | -0.60% | -0.36% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_GSEC_10Y_IN → BOSCHLTD | -2.00% | -0.36% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → BOSCHLTD | +0.65% | +0.36% |
| 2 | EV_RURAL_RELIEF_PACKAGE ⇒ F_RURAL_DEMAND → F_AUTO_DEMAND_IN → BOSCHLTD | +0.59% | +0.32% |
| 1 | EV_RBI_DEC26_HOLD ⇒ F_GSEC_10Y_IN → BOSCHLTD | +0.60% | +0.31% |
| 1 | EV_RARE_EARTH_CONTROLS_REIMPOSED ⇒ F_SEMICONDUCTOR_SUPPLY → BOSCHLTD | -1.20% | -0.30% |
| 3 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_RURAL_DEMAND → F_AUTO_DEMAND_IN → BOSCHLTD | +0.42% | +0.28% |
| 1 | EV_BUDGET27_AGRI_RURAL ⇒ F_GSEC_10Y_IN → BOSCHLTD | -0.40% | -0.28% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | P_EV_POLICY → BOSCHLTD | +1.10 | events | -3.30% |
| 1 | F_GSEC_10Y_IN → BOSCHLTD | +1.55 | director_override | -3.10% |
| 1 | F_STEEL_INDIA → BOSCHLTD | +1.35 | events | -1.22% |
| 1 | F_ALUMINIUM → BOSCHLTD | -1.96 | observed | +0.98% |
| 1 | F_AUTO_DEMAND_IN → BOSCHLTD | -0.10 | events | -0.60% |
| 1 | F_REPO_IN → BOSCHLTD | +1.00 | events | -0.50% |
| 1 | F_USDINR → BOSCHLTD | -0.37 | observed | +0.37% |
| 2 | F_AI_CAPEX → F_SEMICONDUCTOR_SUPPLY → BOSCHLTD | -0.30 | events | +0.29% |
| 2 | C_US_CHINA_DECOUPLING → F_SEMICONDUCTOR_SUPPLY → BOSCHLTD | -0.10 | events | +0.13% |
| 1 | F_COPPER → BOSCHLTD | -0.24 | observed | +0.07% |
| 3 | C_US_CHINA_DECOUPLING → NEW_RARE_EARTH_SUPPLY → F_SEMICONDUCTOR_SUPPLY → BOSCHLTD | -0.10 | events | +0.04% |
| 1 | F_BRENT → BOSCHLTD | +0.00 | observed | -0.00% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-11 | Q2 FY27 results (date not confirmed; may coincide with Nov 6 board meeting) | results | 0.95 | +0.0% | +0.00% |
| 2026-11-06 | Board meeting to consider first-ever bonus issue and share sub-division (and likely Q2 FY27 results, unverified) | corporate_action | 0.90 | +1.0% | +0.90% |
| 2027-02 | Q3 FY27 results and demand read-through for festive quarter | results | 0.95 | +0.0% | +0.00% |
| 2027-04 | Bonus/split effective and possible index/ETF flow effects | corporate_action | 0.60 | +1.0% | +0.60% |

## Analyst profile (agent research, sourced)
# Bosch Ltd. (BOSCHLTD) — Market Impact profile, 2026-11-05

## Business
Bosch Ltd. is the listed Indian arm of Robert Bosch GmbH (70.5% promoter holding). About 85% of revenue is mobility (model knowledge): diesel and gasoline fuel-injection and powertrain systems, braking and driver-assistance electronics, two-wheeler and power-sports systems, and a large aftermarket. The rest is power tools, building technology and energy products. The balance sheet is net cash, so earnings carry sizeable treasury income, and trailing operating margin is ~13-14%. Q1 FY27 (June 2026) sales were Rs 5,842 cr (+22% y/y) with mobility +25.7% and OPM 14%; net profit of Rs 706 cr fell 37% only because the prior-year quarter had a one-off gain. The stock is at record highs (+76% since April, per Business Standard 2026-11-03) at 64x earnings and ~10x book, with a first-ever bonus and split on the agenda of the 2026-11-06 board meeting.

## What moves the stock (ranked)
1. **Auto/CV/tractor volumes (F_AUTO_DEMAND_IN, +6 per +10%)** — the dominant fundamental. Operating leverage is high because the incremental margin (~25%) is almost double the average.
2. **Valuation / discount rate (F_GSEC_10Y_IN, -2 per +25bp)** — a 64x multiple is the most rate-sensitive in the batch. The 7 Oct 2026 RBI hike to 5.50% and 4.89% US 10-year yields work against it.
3. **Electronics / semiconductor supply (-4 per unit of tightening)** — low probability, high impact.
4. **EV transition (P_EV_POLICY, -3)** — structural drag on diesel injection, partly offset by safety and emission content.
5. **Metals (steel -0.9, aluminium -0.5, copper -0.3 per standard shock)** — modest, because most contracts have pass-through. Global HRC is +20.6% since June, aluminium -19.6%.
6. **USD/INR (-1.0 per +3%)** — Bosch is a net importer.
7. **Positive structural themes**: tighter safety/emission norms (+2.5), premiumisation (+1.5), GST relief (+2).

## Transmission examples
- **Mideast escalation (4 orders).** Iran/Hormuz escalation (C_MIDEAST_CONFLICT) -> Brent above $100 (it already touched that on 8 Oct) -> India's fuel and freight costs rise and INR weakens (USD/INR 94.5) -> RBI, already in "calibrated tightening", cannot cut -> vehicle-loan rates stay high -> CV/tractor/2W volumes soften -> Bosch mobility volumes and operating leverage reverse. Net effect on Bosch is negative but small per step (Brent -0.5; rates -0.5; discount rate -2).
- **Rate-hike discount channel (3 orders).** Higher US 10-year (4.89%, +9.4% since June) -> FPI outflows from Indian large caps -> richest multiples compress first -> Bosch (64x) de-rates more than the market even if fundamentals are unchanged.
- **Semiconductor / China channel (3 orders).** US-China decoupling or an Nexperia-type dispute -> chip and rare-earth shortage at OEMs -> OEM production stoppages -> Bosch supply volumes and expedite costs hit, while its own electronics imports price higher.
- **Metals channel (2 orders).** Global HRC +20.6% -> domestic steel up (F_STEEL_INDIA) -> forgings/housings cost up -> pass-through lag of 1-2 quarters squeezes margin -> but the effect is small vs. volume.
- **Policy upside (3 orders).** Mandatory ADAS/airbags -> content per vehicle up -> Bosch electronics/sensor revenue rises -> margin mix improves.

## Current situation
- Q1 FY27: revenue beat (Investing.com, Aug 11), margins 14%. Q2 FY27 results are due (date not confirmed; may coincide with the Nov 6 board meeting).
- India autos had a record August, then a weak September (Bajaj Auto domestic -12%) followed by strong October prints (cars crossed 5 lakh units). The RBI hike on 7 Oct (first in ~4 years) hit auto stocks.
- Bosch GmbH kept its group outlook despite lower auto output and EV drain (Automotive News, 2026-09-23).
- Promoter holding unchanged at 70.54%; FIIs 7.2%, DIIs 15.2% (Sep 2026).

## Upcoming events
Nov 6 board (bonus, split, possibly Q2); Q3 FY27 results ~Feb 2027; Union Budget 1 Feb 2027; monthly auto sales (1st of each month); RBI MPC (Dec/Feb).

## Bull case
Mobility growth of 20%+ persists through the festive season, margins reach 15%, bonus/split broadens retail ownership, and safety-norm content gains let the premium multiple hold. Net cash and a 49% dividend payout limit downside.

## Bear case
Volumes normalise after the GST-led surge, the high base weighs from Q3, ICE-related profit pools shrink faster than expected, and at 64x a small miss triggers a 10-15% de-rating. Evidence limits: cost shares and the royalty rate are estimates (model knowledge); Q2 results were not retrieved.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.