# BHARTIARTL — Bharti Airtel Ltd.
*NIFTY_50 · Telecommunication · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +0.7%**, **12 months +1.4%** (rank 74 / 64 of 200 for 3m / 12m); beta 0.88
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +16.8%): 3 months 53%, 12 months 30%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -1.3% … P90 +4.8%; plausible 12m relative-return range incl. stock-specific noise: -15.4% … +19.8%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves -0.3 pp (model impact -0.6% beta-adjusted vs realised market-adjusted move +9.6%); forward event exposure +2.5% (3m -0.1%; half assumed priced); company-specific events +3.1%

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
| Broad mobile tariff hike by Jio/Airtel (12-15%) (`EV_TELECOM_TARIFF_HIKE_2027`) | anticipated | 0.75 | +6.5% | +4.9% | +6.6 | +0.0 | -0.1 | -0.0 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -4.8% | -4.8% | -4.4 | -0.2 | -0.0 | -0.1 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -3.2% | -3.2% | +0.0 | -2.1 | -1.1 | -0.0 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +5.5% | +2.8% | +5.0 | +0.3 | +0.0 | +0.2 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -2.1% | -2.1% | -2.1 | +0.0 | -0.0 | +0.0 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -1.7% | -1.7% | -1.6 | +0.0 | -0.0 | -0.0 |
| Bharti Airtel raises postpaid plans by Rs 50 (3-11%) (`EV_AIRTEL_POSTPAID_HIKE`) | occurred | 1.00 | +1.6% | +1.6% | +1.6 | +0.0 | -0.0 | -0.0 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.25 | -5.1% | -1.3% | +0.0 | -4.2 | -0.9 | -0.0 |
| Risk: USD/INR >98 and/or reserves < US$650bn (disorderly rupee, emergency RBI response) (`EV_RUPEE_BREAK_98_RESERVE_STRESS`) | risk_scenario | 0.18 | -6.4% | -1.1% | -6.3 | +0.1 | -0.1 | -0.0 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.55 | +2.1% | +1.1% | +0.5 | +0.7 | +0.5 | +0.4 |
| US midterms (3 Nov 2026): Democrats win House and Senate (`EV_US_MIDTERMS_DEM_SWEEP`) | occurred | 1.00 | +1.1% | +1.1% | +0.9 | +0.1 | +0.0 | +0.0 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -1.1% | -1.1% | +0.2 | -0.9 | -0.3 | -0.1 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_TELECOM_TARIFF_HIKE_2027 ⇒ P_TELECOM_TARIFFS → BHARTIARTL | +6.60% | +4.95% |
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → BHARTIARTL | +5.00% | +2.50% |
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → BHARTIARTL | -1.20% | -0.60% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → BHARTIARTL | -3.00% | -0.54% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → BHARTIARTL | -1.20% | -0.50% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → BHARTIARTL | -1.92% | -0.48% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_FPI_FLOWS → BHARTIARTL | -1.92% | -0.48% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → BHARTIARTL | -1.87% | -0.47% |
| 1 | EV_CPI_BREACH_6PCT ⇒ F_GSEC_10Y_IN → BHARTIARTL | -0.75% | -0.45% |
| 1 | EV_BUDGET_FY28_LTCG_RELIEF ⇒ F_FPI_FLOWS → BHARTIARTL | +1.00% | +0.35% |
| 2 | EV_PULSES_VEG_SPIKE_WINTER ⇒ F_CPI_IN → F_REPO_IN → BHARTIARTL | -1.38% | -0.35% |
| 2 | EV_NBS_RABI_HIKE ⇒ P_FERT_SUBSIDY → F_GSEC_10Y_IN → BHARTIARTL | -0.36% | -0.34% |
| 1 | EV_SATCOM_LAUNCH ⇒ P_TELECOM_TARIFFS → BHARTIARTL | -0.55% | -0.33% |
| 1 | EV_RBI_FEB27_HIKE25 ⇒ F_REPO_IN → BHARTIARTL | -1.20% | -0.32% |
| 1 | EV_Q2_FY27_GDP_STRONG ⇒ F_FPI_FLOWS → BHARTIARTL | +0.40% | +0.32% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_FPI_FLOWS → BHARTIARTL | -1.60 | events | -3.20% |
| 1 | F_GSEC_10Y_IN → BHARTIARTL | +1.55 | director_override | -2.33% |
| 1 | P_TELECOM_TARIFFS → BHARTIARTL | +0.30 | events | +1.65% |
| 1 | F_REPO_IN → BHARTIARTL | +1.00 | events | -1.20% |
| 1 | F_US_10Y → BHARTIARTL | +1.68 | observed | +0.50% |
| 1 | F_GDP_IN → BHARTIARTL | +0.50 | events | +0.50% |
| 1 | F_USDINR → BHARTIARTL | -0.37 | observed | +0.18% |
| 2 | F_DXY → C_AFRICA_LATAM → BHARTIARTL | +0.74 | observed | -0.09% |
| 2 | T_GENAI_SERVICES → T_DATA_CENTRES_IN → BHARTIARTL | +1.00 | events | +0.06% |
| 2 | F_AI_CAPEX → T_DATA_CENTRES_IN → BHARTIARTL | -0.30 | events | -0.03% |
| 1 | F_BRENT → BHARTIARTL | +0.00 | observed | -0.00% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-11-05 | Q2 FY27 results (today): ARPU, India margin, Africa, capex | results | 1.00 | +0.5% | +0.50% |
| 2026-12 | Next industry tariff hike (prepaid) after Airtel postpaid +Rs50; Nomura base case Dec quarter | other | 0.40 | +5.5% | +2.20% |
| 2027-01 | Q3 FY27 results | results | 0.95 | +0.5% | +0.47% |
| 2027-03 | Spectrum auction / backhaul spectrum fee decision (TRAI proposal; telcos urged Centre to accept, 2026-10-29) | regulatory | 0.30 | -0.5% | -0.15% |

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