# BOSCHLTD — Bosch Ltd.
*NIFTY_NEXT_50 · Automobile and Auto Components · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -1.7%**, **12 months -2.3%** (rank 145 / 131 of 200 for 3m / 12m); beta 1.10
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +25.9%): 3 months 45%, 12 months 32%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -6.9% … P90 +3.0%; plausible 12m relative-return range incl. stock-specific noise: -41.7% … +18.4%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves -1.4 pp (model impact -2.8% beta-adjusted vs realised market-adjusted move +35.7%); forward event exposure -1.0% (3m -1.1%; half assumed priced); company-specific events +1.5%

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
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -5.7% | -5.7% | -2.5 | -1.0 | -0.8 | -1.5 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -4.0% | -4.0% | +0.0 | -1.4 | -2.7 | +0.1 |
| CAFE-III fuel-efficiency norms notified (30 Sep 2026); no small-car carve-out; 3x credit for BEVs (`EV_CAFE3_NOTIFIED`) | occurred | 1.00 | -3.0% | -3.0% | -3.0 | +0.0 | -0.0 | -0.0 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -2.8% | -2.8% | -2.8 | +0.0 | +0.0 | -0.0 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -1.6% | -1.6% | -1.1 | -0.3 | -0.1 | -0.1 |
| Global and Indian steel prices at multi-year highs (global HRC +60% y/y) (`EV_STEEL_RALLY_2026`) | occurred | 1.00 | -1.3% | -1.3% | -1.3 | +0.0 | -0.0 | -0.0 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -1.3% | -1.3% | +0.0 | -1.0 | -0.2 | -0.1 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.36 | -3.6% | -1.3% | -1.2 | -0.7 | -0.6 | -1.1 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -1.3% | -1.3% | +0.0 | -0.8 | -0.1 | -0.3 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.58 | +2.1% | +1.2% | +0.8 | +0.4 | +0.3 | +0.6 |
| China re-imposes/hardens rare-earth and critical-mineral export controls hitting India's autos and electronics (`EV_RARE_EARTH_CONTROLS_REIMPOSED`) | risk_scenario | 0.25 | -4.5% | -1.1% | -1.2 | -3.6 | +0.1 | +0.1 |
| Aluminium -20% since June; copper off record; Nifty Metal -7% in October (`EV_BASE_METALS_ALUMINIUM_SLIDE`) | occurred | 1.00 | +1.1% | +1.1% | +1.1 | +0.0 | +0.0 | +0.0 |

## Strongest causal chains (1st–4th order)
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26 ⇒ F_GSEC_10Y_IN → BOSCHLTD | -2.80% | -2.80% |
| 1 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → BOSCHLTD | -2.48% | -2.48% |
| 1 | EV_CAFE3_NOTIFIED ⇒ P_EV_POLICY → BOSCHLTD | -2.40% | -2.40% |
| 1 | EV_STEEL_RALLY_2026 ⇒ F_STEEL_INDIA → BOSCHLTD | -1.26% | -1.26% |
| 3 | EV_CPI_REACCEL_SEP26 ⇒ F_CPI_IN → F_REPO_IN → F_GSEC_10Y_IN → BOSCHLTD | -1.05% | -1.05% |
| 1 | EV_BASE_METALS_ALUMINIUM_SLIDE ⇒ F_ALUMINIUM → BOSCHLTD | +0.98% | +0.98% |
| 1 | EV_PM_EDRIVE_EXT ⇒ P_EV_POLICY → BOSCHLTD | -0.90% | -0.90% |
| 3 | EV_CPI_REACCEL_SEP26 ⇒ F_CPI_IN → F_REPO_IN → F_AUTO_DEMAND_IN → BOSCHLTD | -0.89% | -0.89% |
| 2 | EV_UST_SELLOFF_SEP26 ⇒ F_US_10Y → F_GSEC_10Y_IN → BOSCHLTD | -0.88% | -0.88% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_AI_CAPEX → F_SEMICONDUCTOR_SUPPLY → BOSCHLTD | +2.88% | +0.81% |
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → BOSCHLTD | -1.60% | -0.80% |
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_USDINR → BOSCHLTD | -0.78% | -0.78% |
| 2 | EV_PRECIOUS_METALS_CRASH_2026 ⇒ F_US_10Y → F_GSEC_10Y_IN → BOSCHLTD | -0.78% | -0.78% |
| 2 | EV_RARE_EARTH_CONTROLS_REIMPOSED ⇒ NEW_RARE_EARTH_SUPPLY → F_AUTO_DEMAND_IN → BOSCHLTD | -2.88% | -0.72% |
| 2 | EV_CPI_REACCEL_SEP26 ⇒ F_CPI_IN → F_REPO_IN → BOSCHLTD | -0.66% | -0.66% |

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