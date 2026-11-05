# PHOENIXLTD — Phoenix Mills Ltd.
*MIDCAP_100 · Realty · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -4.0%**, **12 months -6.8%** (rank 182 / 178 of 200 for 3m / 12m); beta 1.29
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +22.8%): 3 months 36%, 12 months 30%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -14.2% … P90 -3.4%; plausible 12m relative-return range incl. stock-specific noise: -41.7% … +18.6%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves -3.1 pp (model impact -6.2% beta-adjusted vs realised market-adjusted move +14.8%); forward event exposure -6.8% (3m -3.9%; half assumed priced); company-specific events +1.8%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -3.73 | -3.00 | -0.65 | -0.07 | -0.01 | — |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -3.71 | +0.00 | -0.29 | -2.52 | -0.89 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -3.66 | -0.50 | -2.24 | -0.86 | -0.06 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -3.47 | +0.00 | -1.29 | -1.54 | -0.65 | -1.1% |
| Consumer premiumisation (`T_PREMIUMISATION`) | +1 | +3.13 | +3.00 | +0.12 | +0.03 | -0.02 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +2.75 | +2.50 | +0.10 | +0.03 | +0.12 | — |
| India 10-year G-sec yield (`F_GSEC_10Y_IN`) | +25 bp yield | -2.57 | -2.50 | -0.06 | -0.02 | +0.01 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -2.39 | +0.00 | -0.06 | -0.88 | -1.45 | — |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +2.17 | +1.00 | +0.40 | +0.68 | +0.08 | — |
| Brent crude oil price (`F_BRENT`) | +10% Brent | -2.09 | +0.00 | -0.53 | -0.94 | -0.62 | +0.0% |
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +1.95 | +2.00 | +0.40 | -0.24 | -0.21 | — |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -1.81 | +0.00 | -0.93 | -0.63 | -0.25 | +3.5% |
| US dollar index (`F_DXY`) | +3% DXY | -1.74 | +0.00 | -1.10 | -0.35 | -0.29 | +2.2% |
| US 10-year Treasury yield (`F_US_10Y`) | +25 bp yield | -1.39 | +0.00 | -1.15 | -0.20 | -0.04 | +9.4% |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -11.4% | -11.4% | +0.0 | -2.7 | -5.1 | -3.6 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -6.2% | -6.2% | -5.5 | -0.2 | -0.1 | -0.3 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -4.2% | -4.2% | -0.6 | -2.6 | -1.1 | -0.0 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -4.1% | -4.1% | -3.8 | -0.1 | -0.1 | -0.1 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -3.6% | -3.6% | -3.5 | -0.1 | -0.1 | +0.0 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +7.0% | +3.5% | +6.2 | +0.2 | +0.1 | +0.4 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -3.1% | -3.1% | +0.0 | -2.8 | -0.3 | -0.1 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.36 | -7.8% | -2.8% | +0.0 | -2.5 | -3.1 | -2.2 |
| Gold and silver slump from January 2026 peaks (silver -53%, gold -24%) (`EV_PRECIOUS_METALS_CRASH_2026`) | occurred | 1.00 | -2.6% | -2.6% | +0.0 | -2.5 | +0.0 | -0.2 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.58 | +4.3% | +2.5% | +0.0 | +1.3 | +1.7 | +1.3 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -2.3% | -2.3% | +0.0 | -1.7 | -0.4 | -0.2 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.28 | -8.2% | -2.3% | +0.0 | -6.4 | -1.4 | -0.4 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → PHOENIXLTD | +6.25% | +3.12% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → PHOENIXLTD | -3.00% | -1.20% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → PHOENIXLTD | -3.73% | -1.05% |
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → PHOENIXLTD | -2.00% | -1.00% |
| 2 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → PHOENIXLTD | -4.67% | -0.84% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → PHOENIXLTD | -3.75% | -0.82% |
| 1 | EV_RBI_FEB27_HIKE25 ⇒ F_REPO_IN → PHOENIXLTD | -3.00% | -0.81% |
| 1 | EV_CPI_BREACH_6PCT ⇒ F_GSEC_10Y_IN → PHOENIXLTD | -1.25% | -0.75% |
| 1 | EV_CPI_BREACH_6PCT ⇒ F_REPO_IN → PHOENIXLTD | -1.20% | -0.72% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → PHOENIXLTD | -2.40% | -0.67% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_REPO_IN → PHOENIXLTD | -3.00% | -0.66% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_FPI_FLOWS → PHOENIXLTD | -2.40% | -0.60% |
| 2 | EV_NBS_RABI_HIKE ⇒ P_FERT_SUBSIDY → F_GSEC_10Y_IN → PHOENIXLTD | -0.60% | -0.57% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_GSEC_10Y_IN → PHOENIXLTD | -2.50% | -0.55% |
| 3 | EV_WHEAT27_CROP_BELOW ⇒ F_FOOD_INFLATION_IN → F_CPI_IN → F_REPO_IN → PHOENIXLTD | -0.76% | -0.49% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_GSEC_10Y_IN → PHOENIXLTD | +1.70 | events | -4.25% |
| 1 | F_FPI_FLOWS → PHOENIXLTD | -1.60 | events | -4.00% |
| 1 | F_REPO_IN → PHOENIXLTD | +1.00 | events | -3.00% |
| 1 | F_GDP_IN → PHOENIXLTD | +0.50 | events | +0.60% |
| 1 | F_CPI_IN → PHOENIXLTD | +1.15 | events | -0.57% |
| 1 | F_URBAN_DEMAND → PHOENIXLTD | +0.20 | events | +0.40% |
| 1 | F_STEEL_INDIA → PHOENIXLTD | +1.65 | events | -0.33% |
| 1 | F_US_TECH_SPEND → PHOENIXLTD | -0.60 | events | -0.24% |
| 2 | F_GSEC_10Y_IN → F_HOUSING_DEMAND → PHOENIXLTD | +1.70 | events | -0.10% |
| 2 | C_MIDEAST_CONFLICT → F_TRAVEL_DEMAND → PHOENIXLTD | +1.50 | events | -0.09% |
| 2 | F_REPO_IN → F_HOUSING_DEMAND → PHOENIXLTD | +1.00 | events | -0.05% |
| 2 | T_GENAI_SERVICES → F_HOUSING_DEMAND → PHOENIXLTD | +1.00 | events | -0.04% |

## Analyst profile (agent research, sourced)
# Phoenix Mills (PHOENIXLTD) - profile as of 2026-11-05

## Business
Phoenix Mills is the premium-mall specialist of the Indian listed market: Phoenix Marketcity (Mumbai, Pune, Bengaluru, Chennai), Palladium, Mall of Asia (Bengaluru), plus offices, hotels and a small residential arm. The annuity model yields a 60% operating margin and, unlike the developers, revenue is recurring (rent plus turnover rent). Management guided 14-15% rental growth through FY28 (scanx, 2026-11-04) and H1 FY27 retail consumption was +28%, led by the new Mall of Asia (Multibagg AI, 2026-10-31). Q2 owner profit grew 7%. At a P/E of 57 and P/B 8.3 the stock is priced as a quality compounder (BofA, 2026-09-17) and rose 12% in the last month.

## What moves the stock
1. **Premiumisation (+3.0)** and **urban consumption (+2.0 per +5pp)**: tenant sales feed turnover rent.
2. **Yields and rates**: G-sec 10y -2.5 per +25 bp (cap-rate/long-duration effect) and repo -3.0; the RBI hiked to 5.50% on 2026-10-07 and G-sec/US yields are elevated (US 10Y 4.89%).
3. FPI/DII flows (+2.5/+1.0), GDP (+1.2), GST cuts (+1.0), travel (+0.5), substitution by quick commerce (-0.4), CPI (-0.5), office tenants (US tech +0.4).
The pack's top empirical sensitivities (sugar +1.43, gas -0.77) are below |t|=2 and unrelated to the business, so they are ignored.

## Transmission examples
- **Rates (4 orders)**: oil at $95 -> CPI up -> RBI hikes again -> 10y G-sec up -> required mall/office yields widen -> asset values fall and a 57x multiple compresses, while interest cost on mall capex rises.
- **Consumption (3 orders)**: GST cut or income-tax relief -> tenant sales growth -> turnover rent above minimum guarantee -> rental growth above 14-15% guidance.
- **Wealth (3 orders)**: equity rally -> luxury spending -> Palladium sales -> luxury brands expand space -> higher renewal spreads.
- **Channel shift (3 orders)**: quick-commerce growth -> low-ticket mall footfall slips -> anchor and F&B tenant sales weaken -> turnover rent growth slows.

## Current situation
Consumption and rental guidance are strong; the share is near its high, so valuation, not fundamentals, is the main risk. Final dividend Rs 2.50 recommended; BofA Property Week on 2026-11-06.

## Upcoming
Dividend payment, festive-season consumption data, Q3 results (~February 2027), December MPC.

## Bull / Bear
Bull: sustained 14-15% rental growth plus Mall of Asia ramp. Bear: yields rise further and the 57x multiple compresses. Confidence medium; segment shares and debt are model estimates.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.