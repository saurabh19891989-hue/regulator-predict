# EXIDEIND — Exide Industries Ltd.
*MIDCAP_100 · Automobile and Auto Components · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +0.7%**, **12 months +2.0%** (rank 77 / 69 of 200 for 3m / 12m); beta 1.14
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +27.6%): 3 months 52%, 12 months 55%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -1.8% … P90 +6.7%; plausible 12m relative-return range incl. stock-specific noise: -18.7% … +43.0%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +1.5 pp (model impact +3.0% beta-adjusted vs realised market-adjusted move -11.1%); forward event exposure +2.4% (3m +0.8%; half assumed priced); company-specific events +1.0%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +4.52 | +0.00 | +3.28 | +0.93 | +0.31 | — |
| Production-linked incentive schemes (`P_PLI`) | +1 = expansion/disbursement | +4.00 | +4.00 | +0.00 | +0.01 | -0.01 | — |
| Indian vehicle demand (`F_AUTO_DEMAND_IN`) | +10% volumes | +4.00 | +4.00 | +0.00 | +0.00 | +0.00 | — |
| Energy transition investment (`T_ENERGY_TRANSITION`) | +1 | +2.99 | +3.00 | +0.00 | +0.00 | -0.01 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -2.66 | +0.00 | -1.21 | -1.51 | +0.07 | — |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -1.58 | +0.00 | +0.00 | -0.77 | -0.82 | — |
| Renewable / transmission policy support (`P_RENEWABLE_SUPPORT`) | +1 = stronger support | +1.56 | +0.00 | +1.56 | +0.00 | +0.00 | — |
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +1.53 | +0.00 | +1.92 | -0.15 | -0.24 | — |
| Zinc / lead price (`F_ZINC_LEAD`) | +10% zinc | -1.50 | -1.50 | +0.00 | +0.00 | +0.00 | — |
| India 10-year G-sec yield (`F_GSEC_10Y_IN`) | +25 bp yield | -1.49 | -1.50 | +0.00 | +0.00 | +0.01 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -1.42 | -0.80 | -0.05 | -0.33 | -0.25 | -1.1% |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -1.39 | +0.00 | -0.72 | -0.31 | -0.35 | — |
| Critical-mineral supply tightness (China export controls on rare earths, magnets, graphite, Ga/Ge) (`NEW_RARE_EARTH_SUPPLY`) | +1 = new/tighter export-control round | -1.30 | +0.00 | -1.40 | +0.10 | +0.00 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -1.18 | -0.60 | -0.52 | -0.04 | -0.01 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -5.3% | -5.3% | -3.0 | -0.6 | -0.5 | -1.1 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -3.1% | -3.1% | +0.0 | -1.4 | -1.8 | +0.1 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -2.1% | -2.1% | -2.1 | +0.0 | +0.0 | -0.0 |
| Cabinet approves Rs14,500 cr VGF for ~92 GWh grid-scale storage (4 Nov) (`EV_BESS_VGF_NOV26`) | occurred | 1.00 | +1.5% | +1.5% | +1.5 | +0.0 | +0.0 | -0.0 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -1.4% | -1.4% | -1.0 | -0.2 | -0.1 | -0.0 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.36 | -3.1% | -1.1% | -1.5 | -0.4 | -0.4 | -0.8 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.58 | +1.8% | +1.0% | +0.9 | +0.2 | +0.2 | +0.4 |
| China+1 momentum: Apple/Foxconn/Tata iPhone 18 Pro export ramp, India ~50% of US smartphone imports, PLI round 4 (textiles) and component schemes (`EV_CHINA_PLUS_ONE_ELECTRONICS`) | anticipated | 0.80 | +1.3% | +1.0% | +1.2 | +0.0 | +0.0 | +0.0 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -0.9% | -0.9% | +0.0 | -0.6 | -0.0 | -0.3 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -0.9% | -0.9% | +0.0 | -0.6 | -0.2 | -0.1 |
| Kharif 2026 output hit: paddy area down, foodgrain target cut, rice output seen sharpest fall in ~2 decades (`EV_KHARIF26_OUTPUT_HIT`) | occurred | 1.00 | -0.8% | -0.8% | +0.0 | +0.0 | -0.4 | -0.4 |
| Risk: USD/INR >98 and/or reserves < US$650bn (disorderly rupee, emergency RBI response) (`EV_RUPEE_BREAK_98_RESERVE_STRESS`) | risk_scenario | 0.22 | -3.5% | -0.8% | -3.1 | -0.2 | -0.1 | -0.1 |

## Strongest causal chains (1st–4th order)
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → EXIDEIND | -2.97% | -2.97% |
| 1 | EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26 ⇒ F_GSEC_10Y_IN → EXIDEIND | -2.10% | -2.10% |
| 1 | EV_BESS_VGF_NOV26 ⇒ T_ENERGY_TRANSITION → EXIDEIND | +1.50% | +1.50% |
| 1 | EV_CHINA_PLUS_ONE_ELECTRONICS ⇒ P_PLI → EXIDEIND | +1.20% | +0.96% |
| 2 | EV_CPI_REACCEL_SEP26 ⇒ F_CPI_IN → F_REPO_IN → EXIDEIND | -0.79% | -0.79% |
| 3 | EV_CPI_REACCEL_SEP26 ⇒ F_CPI_IN → F_REPO_IN → F_GSEC_10Y_IN → EXIDEIND | -0.79% | -0.79% |
| 2 | EV_SOLAR_ALMM2_CELL_MANDATE ⇒ P_RENEWABLE_SUPPORT → T_ENERGY_TRANSITION → EXIDEIND | +0.78% | +0.78% |
| 2 | EV_UST_SELLOFF_SEP26 ⇒ F_US_10Y → F_GSEC_10Y_IN → EXIDEIND | -0.66% | -0.66% |
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_USDINR → EXIDEIND | -0.63% | -0.63% |
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → EXIDEIND | -1.20% | -0.60% |
| 1 | EV_RBI_OCT26_HIKE25 ⇒ F_REPO_IN → EXIDEIND | -0.60% | -0.60% |
| 3 | EV_CPI_REACCEL_SEP26 ⇒ F_CPI_IN → F_REPO_IN → F_AUTO_DEMAND_IN → EXIDEIND | -0.60% | -0.60% |
| 2 | EV_PRECIOUS_METALS_CRASH_2026 ⇒ F_US_10Y → F_GSEC_10Y_IN → EXIDEIND | -0.58% | -0.58% |
| 2 | EV_CAFE3_NOTIFIED ⇒ P_EV_POLICY → T_ENERGY_TRANSITION → EXIDEIND | +0.58% | +0.58% |
| 1 | EV_NUCLEAR_SHANTI_RULES_FINAL ⇒ T_ENERGY_TRANSITION → EXIDEIND | +0.90% | +0.54% |

## Analyst profile (agent research, sourced)
# Exide Industries Ltd. (EXIDEIND) — Market Impact profile, 2026-11-05

## Business
Exide is India's largest lead-acid battery maker. Automotive batteries (OEM and replacement) are ~70% of revenue; industrial batteries (telecom, UPS, solar, railways, submarines) ~28%; Exide Energy Solutions, its lithium-ion cell venture, is pre-scale (Phase-I of a 6 GWh plant commissioned 23 Sep 2026). The company is near debt-free, trades at P/E 23 and ROE of only 7.5%. In the September 2026 quarter sales were Rs 5,026 cr (+20% y/y), operating margin 12% and profit Rs 386 cr (+75%); the stock jumped 7% on 4 November after falling 22% over three months.

## What moves the stock (ranked)
1. **Lead price (F_ZINC_LEAD -1.5 per +10%)**: lead is roughly 38-43% of cost; margin swings with the timing of price pass-through.
2. **Auto demand (+4.0 per +10%)**: OEM volumes immediately, replacement with lag.
3. **Li-ion/energy-storage optionality (T_ENERGY_TRANSITION +3.0, P_PLI +4.0)**: the valuation debate (Equitymaster compares Exide and HBL Power for BESS).
4. **Discount rate / funding (G-sec -1.5, repo -0.6).**
5. **Oil derivatives and FX (Brent -0.6, USD/INR -0.8).**
6. **Battery materials (net -0.5, ambiguous).**

## Transmission examples
- **Lead chain (3 orders).** China smelter curbs or a mine outage -> LME lead +10% -> Exide's raw material costs rise 2.7% of revenue -> OEM contracts reprice after 1-3 months but replacement MRPs take quarters -> temporary margin dip of 70bp -> reversal once price hikes land.
- **Oil/rate chain (4 orders).** Hormuz escalation -> Brent $95-100 -> polypropylene and freight up (cost) and CPI up -> RBI hikes (7 Oct) and signals no cuts -> vehicle loans dearer -> OEM volumes and replacement purchases slow -> battery volumes lag.
- **Policy chain (3 orders).** PM-DHARA/PLI tailwinds (stock +10% on 30 Sep) -> investor confidence in Exide Energy -> ability to raise funding at low cost for cell ramp -> lower valuation discount but higher capex risk if customers lag.
- **Materials substitution (4 orders).** Lithium and cell prices fall -> Li-ion cheaper for 2W/UPS -> lead-acid replacement slows (negative for legacy) but Exide's own cell margin improves -> net depends on Exide's cell share.
- **Rupee chain (2 orders).** INR weaker -> USD-linked lead and equipment costs up -> price pass-through lag -> margin dip; empirical data show the opposite sign (not significant).

## Current situation
Q2 FY27 marks a margin recovery from 9% to 12%, FII holding rising to 13.2%, and promoters unchanged at 46%. The stock was -8.9% over the month before the results and rallied after them. September brought the Li-ion plant commissioning, a Rs 100 cr infusion and an ExCom battery pact.

## Upcoming events
Q3 results (Feb); Li-ion ramp-up; Budget (1 Feb 2027); PLI developments.

## Bull case
Lead stays stable, OPM holds 12%+, Li-ion shows customer wins and PLI income, and the market re-rates Exide as an energy-storage platform.

## Bear case
Lead spikes, Li-ion losses balloon, demand slows after rate hikes, and the market de-rates a 7.5% ROE business. Limits: lead cost share, segment mix and PLI amounts are estimates; PM-DHARA details are unverified.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.