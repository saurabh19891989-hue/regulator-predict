# CGPOWER — CG Power and Industrial Solutions Ltd.
*NIFTY_NEXT_50 · Capital Goods · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +0.6%**, **12 months +1.2%** (rank 39 / 40 of 200 for 3m / 12m); beta 1.07
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +28.4%): 3 months 52%, 12 months 52%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -1.4% … P90 +4.5%; plausible 12m relative-return range incl. stock-specific noise: -34.1% … +39.3%
- Decomposition (12m): 0.5 × forward event exposure +2.6% (3m +1.0%; half assumed priced; market-priced macro drift removed) + 0.5 × company-specific catalysts +0.4%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply +7.9% (beta-adjusted) vs a realised market-adjusted move of -14.8% — gap +22.7 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Grid & electrification capex (`T_GRID_ELECTRIFICATION`) | +1 | +5.00 | +5.00 | +0.00 | +0.00 | +0.00 | — |
| Central + state government capex (`F_GOVT_CAPEX`) | +10% capex growth | +3.84 | +3.50 | +0.28 | +0.06 | +0.00 | — |
| Private corporate capex (`F_PRIVATE_CAPEX`) | +10% capex growth | +3.54 | +3.50 | +0.00 | -0.10 | +0.14 | — |
| Indian data-centre build-out (`T_DATA_CENTRES_IN`) | +1 | +2.54 | +2.00 | +0.50 | +0.04 | -0.01 | — |
| Renewable / transmission policy support (`P_RENEWABLE_SUPPORT`) | +1 = stronger support | +2.35 | +1.00 | +0.80 | +0.55 | +0.00 | — |
| Energy transition investment (`T_ENERGY_TRANSITION`) | +1 | +2.24 | +0.00 | +2.25 | +0.00 | -0.01 | — |
| Global AI / data-centre capex (`F_AI_CAPEX`) | +10% growth | +2.07 | +1.50 | +0.38 | +0.17 | +0.02 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -1.45 | -1.30 | -0.10 | -0.02 | -0.03 | — |
| Production-linked incentive schemes (`P_PLI`) | +1 = expansion/disbursement | +1.37 | +1.20 | +0.14 | +0.04 | -0.01 | — |
| General-government fiscal slippage / extra borrowing vs budget (Centre + states) (`NEW_FISCAL_SLIPPAGE_IN`) | +0.5 pp of GDP deficit above budget (~Rs2 lakh cr) | -1.26 | +0.00 | -1.12 | -0.09 | -0.05 | — |
| Indian electricity demand (`F_POWER_DEMAND_IN`) | +3 pp demand growth | +1.20 | +0.00 | +1.20 | +0.00 | +0.00 | — |
| Power market / DISCOM reform (`P_POWER_REFORM`) | +1 = reform progress | +1.20 | +0.00 | +1.20 | +0.00 | +0.00 | — |
| US equity market (`F_US_EQUITIES`) | +5% S&P 500 | +1.01 | +1.00 | +0.00 | +0.01 | +0.01 | +1.2% |
| USD/CNY (`F_USDCNY`) | +3% USD/CNY (yuan weaker) | -0.99 | -1.00 | -0.01 | +0.03 | -0.01 | -1.4% |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| India Q1 FY27 GDP grows 7.8% (31 Aug 2026), beating ~7.3% consensus (`EV_GDP_Q1FY27_7_8`) | occurred | 1.00 | +4.0% | +4.0% | +3.5 | +0.5 | +0.1 | -0.0 |
| Cabinet approves Rs14,500 cr VGF for ~92 GWh grid-scale storage (4 Nov) (`EV_BESS_VGF_NOV26`) | occurred | 1.00 | +2.9% | +2.9% | +1.0 | +1.9 | +0.0 | -0.0 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.25 | -8.9% | -2.2% | -7.5 | -0.8 | -0.5 | -0.1 |
| Global and Indian steel prices at multi-year highs (global HRC +60% y/y) (`EV_STEEL_RALLY_2026`) | occurred | 1.00 | -1.9% | -1.9% | -1.9 | +0.0 | -0.0 | +0.0 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -1.5% | -1.5% | -1.3 | -0.2 | +0.0 | -0.0 |
| Indian spot power: IEX prices hit Rs20/unit ceiling (19 Sep), Q2 prices up ~46% y/y; El Nino lifts demand (`EV_POWER_SPOT_SPIKE`) | occurred | 1.00 | +1.2% | +1.2% | +0.0 | +1.2 | +0.0 | +0.0 |
| ALMM List-II (domestic cells) in force; approved cell capacity 37.8 GW (12th revision, 9 Oct); solar project costs seen +20% (`EV_SOLAR_ALMM2_CELL_MANDATE`) | occurred | 1.00 | +1.2% | +1.2% | +0.5 | +0.4 | +0.3 | +0.0 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -1.1% | -1.1% | +0.0 | -0.9 | -0.1 | -0.1 |
| AI/tech selloff and capex-forecast pause (Oct 2026) (`EV_AI_SELLOFF_OCT26`) | occurred | 1.00 | -1.0% | -1.0% | -0.8 | -0.1 | -0.1 | -0.0 |
| Union Budget 2027-28 capex/railway allocation (infra, railways, defence) (`EV_BUDGET27_CAPEX_RAILWAY`) | scheduled | 0.90 | +0.9% | +0.8% | +0.8 | +0.1 | +0.0 | +0.0 |
| US Q3 data: GDP 3.4%, CPI 3.7%, September payrolls only +29k (`EV_US_Q3_DATA_MIXED`) | occurred | 1.00 | +0.8% | +0.8% | +0.0 | +0.7 | +0.1 | +0.0 |
| Final SHANTI Act rules / first private-sector nuclear licence process (`EV_NUCLEAR_SHANTI_RULES_FINAL`) | anticipated | 0.60 | +1.3% | +0.8% | +0.0 | +1.3 | +0.0 | -0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_AI_CAPEX → CGPOWER | -4.50% | -1.12% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → CGPOWER | -3.00% | -0.75% |
| 1 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → CGPOWER | -3.00% | -0.75% |
| 2 | EV_SUMMER27_POWER_SHORTFALL ⇒ F_POWER_DEMAND_IN → T_GRID_ELECTRIFICATION → CGPOWER | +1.80% | +0.72% |
| 1 | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → CGPOWER | +0.70% | +0.63% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → CGPOWER | -1.30% | -0.55% |
| 2 | EV_POWER_DISTRIB_REFORM ⇒ P_POWER_REFORM → T_GRID_ELECTRIFICATION → CGPOWER | +1.20% | +0.54% |
| 3 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_POWER_DEMAND_IN → T_GRID_ELECTRIFICATION → CGPOWER | -0.64% | -0.44% |
| 2 | EV_NUCLEAR_SHANTI_RULES_FINAL ⇒ P_POWER_REFORM → T_GRID_ELECTRIFICATION → CGPOWER | +0.60% | +0.36% |
| 2 | EV_NUCLEAR_SHANTI_RULES_FINAL ⇒ T_ENERGY_TRANSITION → T_GRID_ELECTRIFICATION → CGPOWER | +0.60% | +0.36% |
| 1 | EV_RBI_FEB27_HIKE25 ⇒ F_REPO_IN → CGPOWER | -1.30% | -0.35% |
| 1 | EV_CHINA_PLUS_ONE_ELECTRONICS ⇒ P_PLI → CGPOWER | +0.36% | +0.29% |
| 1 | EV_NVDA_NOV17_BEAT ⇒ F_AI_CAPEX → CGPOWER | +0.45% | +0.28% |
| 3 | EV_NEMONSOON26_NORMAL_UP ⇒ F_MONSOON → F_POWER_DEMAND_IN → T_GRID_ELECTRIFICATION → CGPOWER | -0.32% | -0.27% |
| 1 | EV_ANTHROPIC_IPO_LISTING ⇒ F_AI_CAPEX → CGPOWER | +0.30% | +0.26% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 2 | F_POWER_DEMAND_IN → T_GRID_ELECTRIFICATION → CGPOWER | +1.20 | events | +1.44% |
| 1 | F_REPO_IN → CGPOWER | +1.00 | events | -1.30% |
| 1 | F_GOVT_CAPEX → CGPOWER | +0.20 | director_override | +0.70% |
| 1 | P_RENEWABLE_SUPPORT → CGPOWER | +0.60 | director_override | +0.60% |
| 2 | T_ENERGY_TRANSITION → T_GRID_ELECTRIFICATION → CGPOWER | +0.30 | director_override | +0.60% |
| 1 | F_ALUMINIUM → CGPOWER | -1.96 | observed | +0.59% |
| 2 | P_RENEWABLE_SUPPORT → T_GRID_ELECTRIFICATION → CGPOWER | +0.60 | director_override | +0.48% |
| 1 | F_USDCNY → CGPOWER | -0.47 | observed | +0.47% |
| 1 | F_STEEL_GLOBAL → CGPOWER | +0.50 | director_override | -0.45% |
| 1 | F_AI_CAPEX → CGPOWER | -0.30 | events | -0.45% |
| 2 | F_GDP_IN → F_PRIVATE_CAPEX → CGPOWER | +0.50 | events | +0.35% |
| 1 | F_US_EQUITIES → CGPOWER | +0.23 | observed | +0.23% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-11 | TII Q2 results show CG consolidation (minorities, EV/semiconductor drag at parent) | other | 0.90 | +0.0% | +0.00% |
| 2026-12 | Hyperscaler capex updates / AI-bubble narrative shifts | other | 0.60 | -1.0% | -0.60% |
| 2027 | Semiconductor OSAT: transition from pilot line to commercial volumes (Sanand) | capex | 0.50 | +2.0% | +1.00% |
| 2027-01 | Q3 FY27 results: test of margin sustainability above 16% and order intake after Rs 8,485 cr in Q2 | results | 0.97 | +0.0% | +0.00% |

## Analyst profile (agent research, sourced)
# CGPOWER - CG Power and Industrial Solutions Ltd. (as of 2026-11-05)

## Business
CG Power is the Murugappa-group electrical-equipment company in which Tube Investments of India is the majority holder (promoter group 56.34%). Power Systems (power and distribution transformers, switchgear; 47% of Q2 FY27 sales) is the profit engine: sales Rs 1,769 cr (+41%), EBITDA margin 25.9%. Industrial Systems (LT and HT motors, drives, fans, railway products; ~53% of sales) grew 25%; CG holds roughly 38-39% of the LT-motor and 19-20% of the HT-motor market. A semiconductor OSAT venture is the long-dated option. Consolidated Q2: revenue Rs 3,802 cr (+30%), EBITDA Rs 621 cr (16.3%), PAT Rs 409 cr (+44%), order intake Rs 8,485 cr (+78%) and backlog Rs 23,646 cr (+58%), about 1.7x trailing revenue. It is debt-free but working-capital days rose from 31 to 70.

## What moves the stock (ranked, % equity value per standard shock)
1. **Grid electrification** (T_GRID_ELECTRIFICATION +5.0): transmission build-out with analyst-cited visibility to FY36; Power Systems order intake rose 137% in Q2.
2. **Government capex** (F_GOVT_CAPEX +3.5 per +10%) and **private capex** (F_PRIVATE_CAPEX +3.5): utilities, railways, metros on one side; factories on the other.
3. **Data centres and AI** (T_DATA_CENTRES_IN +2.0, F_AI_CAPEX +1.5, F_US_EQUITIES +1.0): the Rs 900 cr US hyperscale transformer order is the proof point; the empirical +2.10 per +5% S&P (t 2.2) shows how much the stock trades as an AI-risk-appetite name. SBI Securities flags AI-capex slowdown as a near-term sentiment risk.
4. **Discount rate** (F_REPO_IN -1.3): at 91x earnings, the RBI's October hike and 'no cuts' stance matter.
5. **Input costs** (steel/CRGO -0.9, copper -0.5, aluminium -0.3): partly hedged; Q2 margin still expanded.
6. **Option value** (P_PLI +1.2 for semiconductors, railways +0.6, renewables +1.0).

The pack's strongest empirical statistics are aluminium +2.84 (t 2.6), US equities +2.10 (t 2.2) and USD/CNY -4.42 (t -1.8). The positive aluminium/copper readings reflect cyclical co-movement with the electrification theme, not a cost benefit, so the cost edges are kept small and negative with ranges crossing zero.

## Worked transmission chains
- **AI-capex scepticism (1st) -> S&P 500 and US power-equipment names fall (2nd) -> CG de-rates on lower hyperscaler demand and sentiment (3rd) -> TII (CG's parent) falls by about half of CG's move because of the holding link (4th).**
- **Middle East escalation -> Brent up (1st) -> India CPI up (2nd) -> RBI hikes (3rd, repo already 5.50%) -> discount rate on a 91x P/E stock rises and utilities' financing costs rise (4th) -> -1.3% per 25bp.**
- **Brent up -> INR weaker (2nd) -> imported CRGO and components costlier (3rd) -> Power Systems margin from 25.9% toward 24-25% unless price-variation clauses bite (4th), offset partly by export order values rising in INR.**
- **Government raises transmission capex (Budget 1 Feb 2027) -> PGCIL/state tenders (2nd) -> transformer, switchgear, motor orders (3rd) -> backlog rises and execution timelines lengthen, working capital rises (4th).**
- **Copper up (global electrification demand) -> winding-wire cost up (2nd) -> price-variation clauses recover most (3rd) -> competitors with fixed-price backlogs squeezed, CG gains share (4th).**

## Current situation
Q2 FY27 results on 2026-10-23 were strong, but the stock slipped on the day and then rose 2.5% on 26 October as Nomura, UBS and Citi kept Buy ratings (Kotak Sell, Jefferies Hold). It is up 29% in 2026 but 17% below its July high and fell 11.6% in the last month with a 15 September sell-off (Brent ~$107, global yields up) and the 20-21 October AI-worry move in ABB. On 2026-11-05 it moved back above its 200-day average.

## Upcoming
Q3 FY27 results (late Jan 2027), Union Budget (1 Feb 2027), RBI December MPC, semiconductor commissioning milestones, hyperscaler capex updates.

## Bull case
Orders keep outrunning revenue, Power Systems margin holds above 25%, exports and data-centre wins add a second leg, and semiconductor option value is recognised: analysts' targets of Rs 925-1,100 imply 15-37% upside.

## Bear case
A de-rating from 91x on higher rates or an AI-capex pause, copper/CRGO inflation squeezing fixed-price backlog, competition from Hitachi Energy, Siemens Energy and GE Vernova T&D, execution slippage and rising working capital.

Confidence: medium on drivers, low on magnitudes (cost shares and segment margins are model estimates).


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.