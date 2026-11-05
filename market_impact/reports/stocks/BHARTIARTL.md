# BHARTIARTL — Bharti Airtel Ltd.
*NIFTY_50 · Telecommunication · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +0.7%**, **12 months +1.2%** (rank 79 / 80 of 200 for 3m / 12m); beta 0.88
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +16.8%): 3 months 53%, 12 months 50%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -3.4% … P90 +4.3%; plausible 12m relative-return range incl. stock-specific noise: -23.6% … +20.5%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves -0.2 pp (model impact -0.5% beta-adjusted vs realised market-adjusted move +9.6%); forward event exposure +2.1% (3m -0.0%; half assumed priced); company-specific events +3.1%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Mobile tariff hikes (`P_TELECOM_TARIFFS`) | +10% ARPU via tariff hike | +5.44 | +5.50 | +0.00 | -0.05 | -0.02 | — |
| Jio/Airtel price and share competition vs Vi (`NEW_TELECOM_SHARE_COMPETITION`) | +1 = intensification costing the incumbent ~1pp revenue share / 3% ARPU | -5.00 | -5.00 | +0.00 | +0.00 | +0.00 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -2.78 | +0.00 | -1.84 | -0.91 | -0.02 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +2.17 | +2.00 | +0.11 | +0.01 | +0.06 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -2.13 | +0.00 | -0.48 | -0.82 | -0.82 | — |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -1.56 | +0.00 | +0.00 | -1.06 | -0.49 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -1.52 | -1.20 | -0.30 | -0.00 | -0.02 | — |
| India 10-year G-sec yield (`F_GSEC_10Y_IN`) | +25 bp yield | -1.52 | -1.50 | +0.00 | -0.02 | -0.00 | — |
| US dollar index (`F_DXY`) | +3% DXY | -1.51 | +0.00 | -1.12 | -0.26 | -0.13 | +2.2% |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -1.43 | +0.00 | -0.81 | -0.50 | -0.12 | +3.5% |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -1.36 | -0.50 | -0.36 | -0.34 | -0.16 | -1.1% |
| US equity market (`F_US_EQUITIES`) | +5% S&P 500 | +1.16 | +0.00 | +0.64 | +0.44 | +0.09 | +1.2% |
| Brent crude oil price (`F_BRENT`) | +10% Brent | -1.06 | -0.40 | -0.26 | -0.25 | -0.15 | +0.0% |
| OPEC+ crude supply decisions (`NEW_OPEC_PLUS_SUPPLY`) | +1 mb/d OPEC+ production (quota/actual) | +0.87 | +0.00 | +0.26 | +0.31 | +0.31 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -6.0% | -6.0% | -2.0 | -1.3 | -1.6 | -1.1 |
| Broad mobile tariff hike by Jio/Airtel (12-15%) (`EV_TELECOM_TARIFF_HIKE_2027`) | anticipated | 0.75 | +6.5% | +4.9% | +6.6 | +0.0 | -0.1 | -0.0 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -4.9% | -4.9% | -4.4 | -0.3 | -0.0 | -0.2 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -3.2% | -3.2% | +0.0 | -2.1 | -1.1 | -0.0 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +5.5% | +2.8% | +5.0 | +0.3 | +0.0 | +0.2 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -2.1% | -2.1% | -2.1 | +0.0 | -0.0 | +0.0 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.28 | -6.8% | -1.9% | +0.0 | -5.4 | -1.2 | -0.2 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -1.7% | -1.7% | -1.6 | +0.0 | -0.0 | -0.0 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.36 | -4.6% | -1.6% | -1.0 | -1.6 | -1.2 | -0.7 |
| Bharti Airtel raises postpaid plans by Rs 50 (3-11%) (`EV_AIRTEL_POSTPAID_HIKE`) | occurred | 1.00 | +1.6% | +1.6% | +1.6 | +0.0 | -0.0 | -0.0 |
| Risk: USD/INR >98 and/or reserves < US$650bn (disorderly rupee, emergency RBI response) (`EV_RUPEE_BREAK_98_RESERVE_STRESS`) | risk_scenario | 0.22 | -6.4% | -1.4% | -6.3 | +0.1 | -0.1 | -0.0 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.58 | +2.4% | +1.4% | +0.6 | +0.8 | +0.6 | +0.4 |

## Strongest causal chains (1st–4th order)
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_TELECOM_TARIFF_HIKE_2027 ⇒ P_TELECOM_TARIFFS → BHARTIARTL | +6.60% | +4.95% |
| 1 | EV_FPI_RECORD_OUTFLOW_26 ⇒ F_FPI_FLOWS → BHARTIARTL | -4.40% | -4.40% |
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → BHARTIARTL | +5.00% | +2.50% |
| 1 | EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26 ⇒ F_GSEC_10Y_IN → BHARTIARTL | -2.10% | -2.10% |
| 1 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → BHARTIARTL | -1.98% | -1.98% |
| 1 | EV_AIRTEL_POSTPAID_HIKE ⇒ P_TELECOM_TARIFFS → BHARTIARTL | +1.65% | +1.65% |
| 2 | EV_CPI_REACCEL_SEP26 ⇒ F_CPI_IN → F_REPO_IN → BHARTIARTL | -1.59% | -1.59% |
| 1 | EV_RBI_OCT26_HIKE25 ⇒ F_REPO_IN → BHARTIARTL | -1.20% | -1.20% |
| 1 | EV_US_MIDTERMS_DEM_SWEEP ⇒ F_FPI_FLOWS → BHARTIARTL | +1.00% | +1.00% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → BHARTIARTL | -2.99% | -0.84% |
| 3 | EV_CPI_REACCEL_SEP26 ⇒ F_CPI_IN → F_REPO_IN → F_GSEC_10Y_IN → BHARTIARTL | -0.79% | -0.79% |
| 2 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → BHARTIARTL | -3.73% | -0.67% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → BHARTIARTL | -3.00% | -0.66% |
| 2 | EV_UST_SELLOFF_SEP26 ⇒ F_DXY → F_FPI_FLOWS → BHARTIARTL | -0.64% | -0.64% |
| 2 | EV_PRECIOUS_METALS_CRASH_2026 ⇒ F_DXY → F_FPI_FLOWS → BHARTIARTL | -0.62% | -0.62% |

## Analyst profile (agent research, sourced)
# BHARTIARTL — Bharti Airtel Ltd. (Nifty 50) — profile as of 2026-11-05

## Business
India's premium-ARPU mobile leader by quality (Rs264 ARPU in Q1 FY27; 681m customers in 15 countries; 30m postpaid), plus Airtel Africa (~19% of revenue), home broadband/DTH, Airtel Business and Nxtra data centres, and a ~50% stake in Indus Towers (model knowledge). Q1 FY27: revenue Rs58,539 cr (+18.4%), EBITDA Rs33,599 cr (57.4%), India EBITDA margin 60.1%, India capex Rs9,698 cr (TelecomTalk, Aug 2026). Q2 FY27 results are being announced today, 2026-11-05.

## What moves the stock (ranked)
1. **Tariffs (+5.5 per +10% ARPU).** ~100% drop-through on Rs1.2 lakh cr of India mobile revenue; the Oct-2026 postpaid +Rs50 hike is partly priced, a prepaid hike (Nomura base case: Dec quarter) is the next catalyst.
2. **Competitive intensity (-5).** Jio's IPO (Rs30,213 cr, ~90% to debt reduction) could either free capital for aggression or support tariff discipline.
3. **Discount-rate and funding (-1.5 per +25bp 10y, -1.2 per +25bp repo)** — a 41x P/E stock with ~Rs2 lakh cr net debt incl. leases (estimate).
4. **FPI flows (+2.0)** — FIIs cut from 27.8% to 25.4% in two quarters.
5. **Africa and FX (+0.5 / -0.5)** — USD-linked Africa revenue vs USD debt/capex.

## Transmission examples
- Middle East escalation -> Brent up -> INR weaker -> Airtel capex and USD lease/debt cost up, but Africa revenue in INR terms up (net near zero) -> RBI stays on hold -> urban demand softer -> postpaid adds slow.
- Tariff hike -> Airtel ARPU up -> FCF up -> deleveraging -> lower interest -> higher EPS; same hike -> Vi ARPU up -> tenant risk down -> Indus Towers (Airtel owns ~50%) benefits -> Airtel's holding value rises (company link 0.039).
- Jio IPO proceeds repay debt -> Jio balance sheet stronger -> less pressure to chase subscribers -> tariff discipline (positive Airtel) OR Jio uses strength for 5G bundles (negative).
- Gold/silver/risk-off -> FPI outflows -> Airtel de-rates as a large cap in FII hands (25% FII holding) even though fundamentals are defensive.

## Current situation
Q1 FY27: ARPU +5.6% y/y; India mobile revenue +9.2%; record postpaid adds. Stock +13.7% in the month to Rs2,058 (Business Today, Oct 2026 headlines) on the postpaid hike and Jio IPO read-across; Q2 preview (Business Standard, 2026-11-04) expects double-digit revenue growth. Pack shows -2.6% 12-month return, so the recent rally is a recovery.

## Upcoming events
Q2 FY27 results (2026-11-05); prepaid tariff hike (prob ~0.4 by Dec); Q3 results (Jan 2027); backhaul spectrum fee decision.

## Bull and bear
Bull: prepaid hike, ARPU Rs300 path, Africa margin gains, Kotak's 24% upside (EBITDA CAGR 14%). Bear: tariff pause, Jio share push, 41x P/E derates, Africa devaluation.

## Gaps
Q2 numbers not yet available; net debt and Africa mix are estimates from model knowledge and should be verified.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.