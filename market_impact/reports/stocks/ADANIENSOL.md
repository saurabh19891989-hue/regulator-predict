# ADANIENSOL — Adani Energy Solutions Ltd.
*NIFTY_NEXT_50 · Power · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +2.9%**, **12 months +3.1%** (rank 33 / 54 of 200 for 3m / 12m); beta 1.43
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +39.7%): 3 months 56%, 12 months 50%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -2.4% … P90 +8.9%; plausible 12m relative-return range incl. stock-specific noise: -46.3% … +56.9%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +3.1 pp (model impact +6.1% beta-adjusted vs realised market-adjusted move -9.5%); forward event exposure +0.9% (3m +1.5%; half assumed priced); company-specific events +1.5%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Renewable / transmission policy support (`P_RENEWABLE_SUPPORT`) | +1 = stronger support | +5.26 | +4.00 | +0.78 | +0.47 | +0.00 | — |
| Grid & electrification capex (`T_GRID_ELECTRIFICATION`) | +1 | +5.00 | +5.00 | +0.00 | +0.00 | +0.00 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -3.84 | +0.00 | -2.06 | -1.59 | -0.19 | — |
| Power market / DISCOM reform (`P_POWER_REFORM`) | +1 = reform progress | +3.52 | +3.00 | +0.52 | +0.00 | +0.00 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +3.12 | +2.80 | +0.17 | +0.05 | +0.10 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -2.58 | -1.00 | -0.64 | -0.53 | -0.41 | -1.1% |
| Indian data-centre build-out (`T_DATA_CENTRES_IN`) | +1 | +2.32 | +1.80 | +0.46 | +0.06 | +0.01 | — |
| Indian electricity demand (`F_POWER_DEMAND_IN`) | +3 pp demand growth | +2.30 | +1.50 | +0.77 | +0.03 | +0.00 | — |
| India 10-year G-sec yield (`F_GSEC_10Y_IN`) | +25 bp yield | -2.23 | -2.00 | -0.22 | +0.00 | -0.01 | — |
| Indian corporate credit spreads (`F_CREDIT_SPREADS_IN`) | +50 bp spreads | -2.20 | -2.20 | +0.00 | +0.00 | -0.00 | — |
| US dollar index (`F_DXY`) | +3% DXY | -2.16 | +0.00 | -1.47 | -0.45 | -0.25 | +2.2% |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -2.13 | +0.00 | -1.17 | -0.74 | -0.22 | +3.5% |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -2.03 | +0.00 | +0.00 | -1.14 | -0.90 | — |
| Energy transition investment (`T_ENERGY_TRANSITION`) | +1 | +1.96 | +0.00 | +1.94 | +0.00 | +0.03 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -10.8% | -10.8% | -0.9 | -3.2 | -3.8 | -2.8 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -7.0% | -7.0% | -6.2 | -0.4 | -0.1 | -0.3 |
| Cabinet approves Rs14,500 cr VGF for ~92 GWh grid-scale storage (4 Nov) (`EV_BESS_VGF_NOV26`) | occurred | 1.00 | +5.8% | +5.8% | +4.0 | +1.8 | +0.0 | +0.0 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -4.4% | -4.4% | +0.0 | -2.4 | -1.8 | -0.2 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +7.9% | +4.0% | +7.0 | +0.5 | +0.1 | +0.3 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -3.5% | -3.5% | +0.0 | -2.9 | -0.5 | -0.1 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -3.5% | -3.5% | -3.5 | +0.0 | +0.0 | -0.0 |
| Indian spot power: IEX prices hit Rs20/unit ceiling (19 Sep), Q2 prices up ~46% y/y; El Nino lifts demand (`EV_POWER_SPOT_SPIKE`) | occurred | 1.00 | +3.3% | +3.3% | +2.7 | +0.6 | +0.0 | +0.0 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.28 | -11.8% | -3.3% | +0.0 | -8.6 | -2.5 | -0.6 |
| Gold and silver slump from January 2026 peaks (silver -53%, gold -24%) (`EV_PRECIOUS_METALS_CRASH_2026`) | occurred | 1.00 | -3.1% | -3.1% | +0.0 | -2.6 | -0.4 | -0.1 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.36 | -8.2% | -2.9% | -0.7 | -2.9 | -2.8 | -1.8 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.58 | +4.5% | +2.6% | +0.6 | +1.6 | +1.4 | +1.0 |

## Strongest causal chains (1st–4th order)
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_RECORD_OUTFLOW_26 ⇒ F_FPI_FLOWS → ADANIENSOL | -6.16% | -6.16% |
| 1 | EV_BESS_VGF_NOV26 ⇒ P_RENEWABLE_SUPPORT → ADANIENSOL | +4.00% | +4.00% |
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → ADANIENSOL | +7.00% | +3.50% |
| 1 | EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26 ⇒ F_GSEC_10Y_IN → ADANIENSOL | -2.80% | -2.80% |
| 1 | EV_SOLAR_ALMM2_CELL_MANDATE ⇒ P_RENEWABLE_SUPPORT → ADANIENSOL | +2.00% | +2.00% |
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_FPI_FLOWS → ADANIENSOL | -1.66% | -1.66% |
| 2 | EV_CPI_REACCEL_SEP26 ⇒ F_CPI_IN → F_REPO_IN → ADANIENSOL | -1.59% | -1.59% |
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_USDINR → ADANIENSOL | -1.56% | -1.56% |
| 1 | EV_POWER_SPOT_SPIKE ⇒ F_POWER_DEMAND_IN → ADANIENSOL | +1.50% | +1.50% |
| 1 | EV_US_MIDTERMS_DEM_SWEEP ⇒ F_FPI_FLOWS → ADANIENSOL | +1.40% | +1.40% |
| 1 | EV_POWER_DISTRIB_REFORM ⇒ P_POWER_REFORM → ADANIENSOL | +3.00% | +1.35% |
| 3 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_USDINR → F_FPI_FLOWS → ADANIENSOL | -1.31% | -1.31% |
| 1 | EV_POWER_SPOT_SPIKE ⇒ F_POWER_PRICE_IN → ADANIENSOL | +1.20% | +1.20% |
| 1 | EV_RBI_OCT26_HIKE25 ⇒ F_REPO_IN → ADANIENSOL | -1.20% | -1.20% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → ADANIENSOL | -4.18% | -1.17% |

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