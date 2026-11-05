# ADANIENSOL — Adani Energy Solutions Ltd.
*NIFTY_NEXT_50 · Power · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +1.3%**, **12 months +0.8%** (rank 9 / 53 of 200 for 3m / 12m); beta 1.43
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +39.7%): 3 months 53%, 12 months 50%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -3.4% … P90 +4.4%; plausible 12m relative-return range incl. stock-specific noise: -50.4% … +46.5%
- Decomposition (12m): 0.5 × forward event exposure +0.7% (3m +0.8%; half assumed priced; market-priced macro drift removed) + 0.5 × company-specific catalysts +1.5%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply +1.7% (beta-adjusted) vs a realised market-adjusted move of -9.5% — gap +11.2 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Renewable / transmission policy support (`P_RENEWABLE_SUPPORT`) | +1 = stronger support | +5.26 | +4.00 | +0.78 | +0.47 | +0.00 | — |
| Grid & electrification capex (`T_GRID_ELECTRIFICATION`) | +1 | +5.00 | +5.00 | +0.00 | +0.00 | +0.00 | — |
| Power market / DISCOM reform (`P_POWER_REFORM`) | +1 = reform progress | +3.52 | +3.00 | +0.52 | +0.00 | +0.00 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +3.06 | +2.80 | +0.17 | +0.05 | +0.04 | — |
| Indian data-centre build-out (`T_DATA_CENTRES_IN`) | +1 | +2.34 | +1.80 | +0.46 | +0.06 | +0.02 | — |
| Indian electricity demand (`F_POWER_DEMAND_IN`) | +3 pp demand growth | +2.28 | +1.50 | +0.77 | +0.01 | +0.00 | — |
| Indian corporate credit spreads (`F_CREDIT_SPREADS_IN`) | +50 bp spreads | -2.22 | -2.20 | +0.00 | +0.00 | -0.02 | — |
| India 10-year G-sec yield (`F_GSEC_10Y_IN`) | +25 bp yield | -2.22 | -2.00 | -0.22 | +0.00 | +0.00 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -2.17 | -1.00 | -0.64 | -0.22 | -0.31 | -1.1% |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -2.12 | +0.00 | -1.37 | -0.66 | -0.09 | — |
| Energy transition investment (`T_ENERGY_TRANSITION`) | +1 | +1.99 | +0.00 | +1.94 | +0.00 | +0.06 | — |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -1.80 | +0.00 | -1.17 | -0.57 | -0.06 | +3.5% |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -1.66 | -1.20 | -0.47 | +0.01 | +0.00 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -1.44 | -0.60 | +0.00 | -0.43 | -0.41 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -6.7% | -6.7% | -6.2 | -0.4 | -0.1 | -0.1 |
| Cabinet approves Rs14,500 cr VGF for ~92 GWh grid-scale storage (4 Nov) (`EV_BESS_VGF_NOV26`) | occurred | 1.00 | +5.8% | +5.8% | +4.0 | +1.8 | +0.0 | +0.0 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +7.7% | +3.9% | +7.0 | +0.5 | +0.1 | +0.1 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -3.5% | -3.5% | -3.5 | +0.0 | +0.0 | -0.0 |
| Indian spot power: IEX prices hit Rs20/unit ceiling (19 Sep), Q2 prices up ~46% y/y; El Nino lifts demand (`EV_POWER_SPOT_SPIKE`) | occurred | 1.00 | +3.3% | +3.3% | +2.7 | +0.6 | +0.0 | +0.0 |
| ALMM List-II (domestic cells) in force; approved cell capacity 37.8 GW (12th revision, 9 Oct); solar project costs seen +20% (`EV_SOLAR_ALMM2_CELL_MANDATE`) | occurred | 1.00 | +2.6% | +2.6% | +2.0 | +0.4 | +0.2 | +0.0 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -2.5% | -2.5% | +0.0 | -1.6 | -0.8 | -0.2 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -2.2% | -2.2% | -2.2 | +0.0 | +0.0 | -0.1 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.25 | -7.9% | -2.0% | +0.0 | -6.9 | -1.1 | +0.0 |
| Risk: USD/INR >98 and/or reserves < US$650bn (disorderly rupee, emergency RBI response) (`EV_RUPEE_BREAK_98_RESERVE_STRESS`) | risk_scenario | 0.18 | -9.6% | -1.7% | -8.7 | -1.0 | +0.0 | +0.1 |
| US midterms (3 Nov 2026): Democrats win House and Senate (`EV_US_MIDTERMS_DEM_SWEEP`) | occurred | 1.00 | +1.7% | +1.7% | +1.4 | +0.2 | +0.0 | +0.0 |
| Summer 2027 peak-demand shortfall / IEX at cap under super El Nino (`EV_SUMMER27_POWER_SHORTFALL`) | anticipated | 0.40 | +4.1% | +1.6% | +3.5 | +0.9 | -0.1 | -0.2 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → ADANIENSOL | +7.00% | +3.50% |
| 1 | EV_POWER_DISTRIB_REFORM ⇒ P_POWER_REFORM → ADANIENSOL | +3.00% | +1.35% |
| 1 | EV_SUMMER27_POWER_SHORTFALL ⇒ F_POWER_DEMAND_IN → ADANIENSOL | +2.25% | +0.90% |
| 1 | EV_NUCLEAR_SHANTI_RULES_FINAL ⇒ P_POWER_REFORM → ADANIENSOL | +1.50% | +0.90% |
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → ADANIENSOL | -1.60% | -0.80% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → ADANIENSOL | -4.20% | -0.76% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → ADANIENSOL | -2.69% | -0.67% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_FPI_FLOWS → ADANIENSOL | -2.69% | -0.67% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → ADANIENSOL | -2.61% | -0.65% |
| 2 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_POWER_DEMAND_IN → ADANIENSOL | -0.86% | -0.58% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → ADANIENSOL | -1.20% | -0.50% |
| 1 | EV_BUDGET_FY28_LTCG_RELIEF ⇒ F_FPI_FLOWS → ADANIENSOL | +1.40% | +0.49% |
| 1 | EV_SUMMER27_POWER_SHORTFALL ⇒ F_POWER_PRICE_IN → ADANIENSOL | +1.20% | +0.48% |
| 1 | EV_Q2_FY27_GDP_STRONG ⇒ F_FPI_FLOWS → ADANIENSOL | +0.56% | +0.45% |
| 1 | EV_BANKING_LIQUIDITY_DEFICIT_MAR27 ⇒ F_CREDIT_SPREADS_IN → ADANIENSOL | -0.66% | -0.40% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_FPI_FLOWS → ADANIENSOL | -1.60 | events | -4.48% |
| 1 | F_GSEC_10Y_IN → ADANIENSOL | +1.55 | director_override | -3.10% |
| 1 | P_RENEWABLE_SUPPORT → ADANIENSOL | +0.60 | director_override | +2.40% |
| 1 | F_POWER_DEMAND_IN → ADANIENSOL | +1.20 | events | +1.80% |
| 1 | F_REPO_IN → ADANIENSOL | +1.00 | events | -1.20% |
| 1 | F_CREDIT_SPREADS_IN → ADANIENSOL | +0.50 | events | -1.10% |
| 1 | F_STEEL_INDIA → ADANIENSOL | +1.35 | events | -1.08% |
| 1 | F_POWER_PRICE_IN → ADANIENSOL | +1.90 | director_override | +0.76% |
| 2 | F_POWER_DEMAND_IN → T_GRID_ELECTRIFICATION → ADANIENSOL | +1.20 | events | +0.72% |
| 1 | C_MIDEAST_CONFLICT → ADANIENSOL | +1.00 | events | -0.60% |
| 2 | T_ENERGY_TRANSITION → T_GRID_ELECTRIFICATION → ADANIENSOL | +0.30 | director_override | +0.60% |
| 2 | P_RENEWABLE_SUPPORT → T_GRID_ELECTRIFICATION → ADANIENSOL | +0.60 | director_override | +0.48% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-11 | Closing of IntelliSmart acquisition (Rs 3,050 cr) after CCI approval on 31 Oct 2026 | corporate_action | 0.85 | +1.0% | +0.85% |
| 2026-12 | Commissioning of Khavda Phase-4 remaining elements / Halvad (ROW-dependent), WRSR, Navinal per mgmt; slippage would trim the Rs 15,000 cr FY27 capitalisation guide | capex | 0.50 | +3.0% | +1.50% |
| 2027-01 | Q3 FY27 results (date not announced; Q2 was 22 Oct, so estimate late Jan 2027); H2 capex ramp Rs 8-9k cr to be evidenced | results | 0.97 | +0.0% | +0.00% |
| 2027-03 | FY27 transmission capitalisation guidance (~Rs 15,000 cr) revised down because of Gujarat ROW delays | guidance | 0.35 | -5.2% | -1.84% |
| 2027-03 | Renewed US regulatory/legal action against Adani Group (criminal case dismissed 10 Aug 2026; status of any SEC civil matter not verified by this profile) | litigation | 0.06 | -14.0% | -0.84% |
| 2027-06 | New transmission awards from Rs 1.4 lakh cr near-term pipeline incl. PM-DHARA corridors (at least one >Rs 3,000 cr win) | other | 0.60 | +2.5% | +1.50% |

## Analyst profile (agent research, sourced)
# ADANIENSOL — Adani Energy Solutions Ltd. (as of 2026-11-05)

*Scenario/exposure analysis only. All effects are relative to the Nifty 200 and are not validated forecasts. Facts are sourced in `ADANIENSOL.json` (company Q2 FY27 press release and call transcript of 22-23 Oct 2026, screener.in, Google-News headline searches); items marked "model knowledge" are from training memory.*

## Business
AESL is India's largest private transmission company (29,802 ckm, 1.43 lakh MVA across 16 states; 92% EBITDA margin in the segment) and has diversified into four other engines. Mumbai distribution (AEML, plus MPSEZ Utility in Mundra) is a regulated-asset-base business (RAB Rs 10,456 cr, +11% YoY) that generates the largest share of revenue but a modest share of profit. Smart metering (14.8 mn installed, 24.6 mn under implementation, Rs 29,519 cr revenue potential) is an annuity-like build-own-operate model. The newest and fastest-growing unit is the Energy Solutions platform: it buys renewable/thermal supply and sells round-the-clock and C&I power (12.2 bn units in Q2; operating EBITDA Rs 803 cr, about 26% of the quarter). Q2 FY27 total income was Rs 10,239 cr (+51%), EBITDA Rs 3,548 cr (+67%), PAT Rs 1,364 cr (+145%). Promoters hold 73.4%; FIIs have fallen from 17.6% to 9.6% in 18 months while DIIs rose to 13.6%.

## What moves the stock (ranked by modelled sensitivity x current shock)
1. **Rates and credit spreads (G-sec, repo, spreads).** A P/E-48 compounder with Rs 52k cr of borrowings. RBI hiked the repo by 25bp to 5.50% on 7 Oct 2026 and said cuts are off the table, and US 10y is 4.89% (+9% since June). The model puts -2.0% on +25bp G-sec yield (discount rate), -1.2% for repo (funding) and -2.2% for +50bp in credit spreads. Management says most debt is fixed or hedged, so the P&L effect is small; the valuation effect dominates.
2. **Policy support for grid build-out (P_RENEWABLE_SUPPORT +4, T_GRID_ELECTRIFICATION +5).** The Rs 1.86 lakh cr PM-DHARA green-energy-corridor scheme (approved 30 Sep 2026) and the Rs 1.4 lakh cr near-term tender pipeline determine order-book growth. The stock rose 5.5% on 1 Oct.
3. **Execution of transmission commissioning.** The company-specific driver: H1 commissioning was negligible because of right-of-way problems in Gujarat (Halvad, Khavda), yet management has not cut the ~Rs 15,000 cr FY27 capitalisation guide. This appears in `company_events` rather than as a driver edge.
4. **Group and governance overhang.** The US criminal case against Gautam Adani was dismissed on 10 Aug 2026; `company_links` carries a 0.35 group-contagion edge from Adani Enterprises.
5. **Energy Solutions margins (F_POWER_DEMAND_IN, F_POWER_PRICE_IN).** Mixed sign: rising demand lifts volumes; rising spot prices help legacy merchant volume but hurt while new RTC contracts are priced fixed.
6. **Flows and risk appetite (F_FPI_FLOWS +2.8).** High-beta stock with a thin foreign holder base.

## Worked transmission examples
- **Middle East escalation -> Brent/LNG up (1st) -> Indian inflation expectations up and RBI "calibrated tightening" (2nd) -> G-sec 10y and corporate spreads widen (3rd) -> discount rate on long-duration annuity compounders rises and refinancing of the Rs 87,000 cr construction programme gets pricier (4th) -> AESL de-rates even though its tariffs are fixed.** Offsetting channel: the same conflict strengthens the energy-security case for domestic grid capex.
- **Weak monsoon (-13% in Q2) -> record peak demand of 270 GW and power-demand growth of 11% (1st) -> spot power prices and coal-stock stress (2nd) -> states and discoms sign more RTC/firm supply, which AESL's Energy Solutions platform supplies (MSEDCL 2,500 MW, 25 years) (3rd) -> higher Energy Solutions EBITDA but also timing-mismatch margin risk when spot is above the contracted price (4th).**
- **PM-DHARA approved -> more ISTS corridors tendered (1st) -> AESL's bid-win pipeline grows (2nd) -> order book rises above Rs 87,000 cr and requires more capital (3rd) -> equity raise or promoter infusion (e.g. the Rs 3,500 cr QIP) dilutes per-share value but improves the growth runway (4th).**
- **Steel/aluminium inflation -> tower and conductor cost up on fixed TBCB tariffs (1st) -> project IRR on new awards falls (2nd) -> bidding becomes more conservative and AESL loses share to Power Grid (3rd).** Note that the pack's empirical steel beta is positive; the model rejects it as a market co-movement.

## Current situation
Q2 FY27 headline growth is strong but core transmission EBITDA grew only 15% YoY (Rs 1,394 cr) and distribution is growing 3% in revenue. Management reiterated transmission capex of about Rs 14,000 cr (Rs 8-9k cr in H2) and said three projects (WRSR, Khavda Ph-4 and Halvad) should commission this fiscal year. Smart-meter installation was only 1.3 mn in Q2 against a 10 mn full-year goal. The stock was down 6% after the call and is 19% below its 52-week high.

## Upcoming events
IntelliSmart acquisition closing (CCI approved 31 Oct; closing expected within about a month), Halvad ROW resolution and line commissioning, Q3 FY27 results (late Jan 2027, estimated), new TBCB awards, and a tail risk of renewed US legal action (probability low). Probabilities and impact ranges are in `company_events`.

## Bull and bear
**Bull:** commissioning catches up in H2 (EBITDA conversion of Rs 87k cr pipeline), Energy Solutions continues to scale, rating upgrades follow dismissal of the US case, PM-DHARA lifts the tender pipeline. **Bear:** ROW delays slip into FY28, spreads widen as the RBI tightens, Energy Solutions margins compress, smart-meter volume disappoints, and the stock's 48x P/E leaves little room for error.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.