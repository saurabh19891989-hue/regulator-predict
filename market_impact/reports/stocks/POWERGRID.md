# POWERGRID — Power Grid Corporation of India Ltd.
*NIFTY_50 · Power · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -0.4%**, **12 months +0.3%** (rank 127 / 95 of 200 for 3m / 12m); beta 0.92
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +20.8%): 3 months 48%, 12 months 52%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -2.0% … P90 +2.8%; plausible 12m relative-return range incl. stock-specific noise: -26.6% … +22.2%
- Decomposition (12m): 0.5 × forward event exposure +0.7% (3m -0.5%; half assumed priced) + 0.5 × company-specific catalysts +0.9%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply +1.0% (beta-adjusted) vs a realised market-adjusted move of -13.1% — gap +14.1 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Grid & electrification capex (`T_GRID_ELECTRIFICATION`) | +1 | +3.50 | +3.50 | +0.00 | +0.00 | +0.00 | — |
| India 10-year G-sec yield (`F_GSEC_10Y_IN`) | +25 bp yield | -3.00 | -3.00 | +0.00 | +0.00 | +0.00 | — |
| CERC allowed regulated ROE for transmission (`NEW_CERC_ROE`) | +50 bp allowed ROE | +3.00 | +3.00 | +0.00 | +0.00 | +0.00 | — |
| Renewable / transmission policy support (`P_RENEWABLE_SUPPORT`) | +1 = stronger support | +2.64 | +1.50 | +0.82 | +0.32 | +0.00 | — |
| Indian electricity demand (`F_POWER_DEMAND_IN`) | +3 pp demand growth | +1.92 | +1.50 | +0.42 | +0.00 | +0.00 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -1.80 | +0.00 | -1.22 | -0.55 | -0.03 | — |
| General-government fiscal slippage / extra borrowing vs budget (Centre + states) (`NEW_FISCAL_SLIPPAGE_IN`) | +0.5 pp of GDP deficit above budget (~Rs2 lakh cr) | -1.68 | +0.00 | -1.58 | -0.09 | -0.01 | — |
| Energy transition investment (`T_ENERGY_TRANSITION`) | +1 | +1.66 | +1.00 | +0.65 | +0.00 | +0.01 | — |
| Winning-bid discount intensity in transmission TBCB auctions (`NEW_TBCB_BID_DISCOUNTS`) | +1 = 10% lower winning equity IRR vs base | -1.50 | -1.50 | +0.00 | +0.00 | +0.00 | — |
| Power market / DISCOM reform (`P_POWER_REFORM`) | +1 = reform progress | +1.42 | +1.00 | +0.42 | +0.00 | +0.00 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +1.41 | +1.20 | +0.14 | +0.02 | +0.05 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -1.36 | -0.80 | -0.62 | +0.06 | +0.01 | — |
| Indian data-centre build-out (`T_DATA_CENTRES_IN`) | +1 | +1.17 | +0.80 | +0.34 | +0.03 | +0.00 | — |
| US 10-year Treasury yield (`F_US_10Y`) | +25 bp yield | -1.14 | +0.00 | -1.02 | -0.14 | +0.02 | +9.4% |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -4.2% | -4.2% | -4.2 | +0.0 | +0.0 | -0.0 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -3.1% | -3.1% | -2.6 | -0.3 | -0.0 | -0.1 |
| Cabinet approves Rs14,500 cr VGF for ~92 GWh grid-scale storage (4 Nov) (`EV_BESS_VGF_NOV26`) | occurred | 1.00 | +2.9% | +2.9% | +2.0 | +0.9 | +0.0 | +0.0 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -2.1% | -2.1% | +0.0 | -1.4 | -0.6 | -0.0 |
| Indian spot power: IEX prices hit Rs20/unit ceiling (19 Sep), Q2 prices up ~46% y/y; El Nino lifts demand (`EV_POWER_SPOT_SPIKE`) | occurred | 1.00 | +1.9% | +1.9% | +1.5 | +0.4 | +0.0 | +0.0 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -1.7% | -1.7% | -1.7 | +0.0 | +0.0 | -0.0 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +3.2% | +1.6% | +2.7 | +0.4 | +0.1 | +0.1 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -1.4% | -1.4% | +0.0 | -1.3 | -0.1 | +0.0 |
| ALMM List-II (domestic cells) in force; approved cell capacity 37.8 GW (12th revision, 9 Oct); solar project costs seen +20% (`EV_SOLAR_ALMM2_CELL_MANDATE`) | occurred | 1.00 | +1.3% | +1.3% | +0.8 | +0.4 | +0.2 | +0.0 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -1.2% | -1.2% | +0.0 | -1.0 | -0.2 | +0.0 |
| Budget FY2027-28: FY27 deficit overshoot confirmed and consolidation path slowed (`EV_BUDGET_FY28_FISCAL_SLIPPAGE`) | scheduled | 0.50 | -2.3% | -1.2% | -2.2 | -0.0 | -0.0 | -0.0 |
| CPI prints >=6.0% (RBI upper tolerance) in Oct-Jan data (releases 12 Nov - 12 Feb) (`EV_CPI_BREACH_6PCT`) | anticipated | 0.60 | -1.9% | -1.1% | -1.8 | -0.0 | -0.0 | -0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → POWERGRID | +3.00% | +1.50% |
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → POWERGRID | -2.40% | -1.20% |
| 1 | EV_SUMMER27_POWER_SHORTFALL ⇒ F_POWER_DEMAND_IN → POWERGRID | +2.25% | +0.90% |
| 1 | EV_CPI_BREACH_6PCT ⇒ F_GSEC_10Y_IN → POWERGRID | -1.50% | -0.90% |
| 2 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_POWER_DEMAND_IN → POWERGRID | -0.86% | -0.58% |
| 1 | EV_FERT_SUBSIDY_TOPUP_WINTER ⇒ F_GSEC_10Y_IN → POWERGRID | -0.60% | -0.54% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_GSEC_10Y_IN → POWERGRID | -3.00% | -0.54% |
| 1 | EV_BANKING_LIQUIDITY_DEFICIT_MAR27 ⇒ F_GSEC_10Y_IN → POWERGRID | -0.90% | -0.54% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → POWERGRID | +2.00% | +0.50% |
| 1 | EV_RBI_DEC26_HOLD ⇒ F_GSEC_10Y_IN → POWERGRID | +0.90% | +0.47% |
| 1 | EV_POWER_DISTRIB_REFORM ⇒ P_POWER_REFORM → POWERGRID | +1.00% | +0.45% |
| 1 | EV_BUDGET27_AGRI_RURAL ⇒ F_GSEC_10Y_IN → POWERGRID | -0.60% | -0.42% |
| 1 | EV_RBI_FEB27_HOLD ⇒ F_GSEC_10Y_IN → POWERGRID | +0.60% | +0.40% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_GSEC_10Y_IN → POWERGRID | -0.90% | -0.38% |
| 2 | EV_NEMONSOON26_NORMAL_UP ⇒ F_MONSOON → F_POWER_DEMAND_IN → POWERGRID | -0.43% | -0.37% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_GSEC_10Y_IN → POWERGRID | +1.55 | director_override | -4.65% |
| 1 | F_FPI_FLOWS → POWERGRID | -1.60 | events | -1.92% |
| 1 | F_POWER_DEMAND_IN → POWERGRID | +1.20 | events | +1.80% |
| 1 | P_RENEWABLE_SUPPORT → POWERGRID | +0.60 | director_override | +0.90% |
| 1 | F_REPO_IN → POWERGRID | +1.00 | events | -0.80% |
| 1 | F_ALUMINIUM → POWERGRID | -1.96 | observed | +0.59% |
| 1 | F_STEEL_INDIA → POWERGRID | +1.35 | events | -0.54% |
| 2 | F_POWER_DEMAND_IN → T_GRID_ELECTRIFICATION → POWERGRID | +1.20 | events | +0.50% |
| 2 | P_RENEWABLE_SUPPORT → T_GRID_ELECTRIFICATION → POWERGRID | +0.60 | director_override | +0.34% |
| 1 | T_ENERGY_TRANSITION → POWERGRID | +0.30 | director_override | +0.30% |
| 1 | F_GOVT_CAPEX → POWERGRID | +0.20 | director_override | +0.24% |
| 2 | T_ENERGY_TRANSITION → T_GRID_ELECTRIFICATION → POWERGRID | +0.30 | director_override | +0.21% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-11 | Interim dividend Rs 3/share ex-date (mechanical price adjustment ~1.1% of Rs 261) | corporate_action | 0.90 | -1.1% | -0.99% |
| 2026-11/2027-03 | New TBCB/RTM project awards and ISTS bids (wins add to Rs 2.2 lakh cr order book) | capex | 0.80 | +1.0% | +0.80% |
| 2027-02 | Q3 FY27 results: capitalisation pace vs guided Rs 37,000-40,000 cr capex | results | 0.95 | +0.5% | +0.47% |
| 2027-05 | Q4/FY27 results and FY28 capex/capitalisation guidance; final dividend | guidance | 0.90 | +1.0% | +0.90% |
| 2027-2029 | CERC tariff period 2029-34 consultation (ROE and norms) - long-dated regulatory risk | regulatory | 0.10 | -3.0% | -0.30% |

## Analyst profile (agent research, sourced)
# Power Grid Corporation (POWERGRID) - profile as of 2026-11-05

## Business
Power Grid is India's central transmission utility, owning the bulk of the inter-state grid under CERC-regulated tariffs that pay an allowed ROE of about 15.5% on regulated equity (model knowledge; verify against the 2024-29 regulations). Revenue depends on line availability, not on power volumes or prices, so earnings are bond-like: Q2 FY27 PAT was Rs 3,866 crore (+8.4%), a Rs 3 interim dividend was declared, the order book stands near Rs 2.2 lakh crore and FY27 capex guidance was raised to Rs 37,000-40,000 crore, with H1 capitalisation more than doubling to Rs 9,300 crore (Saur Energy / Multibagg AI, 2026-11-04). The government owns 51.34%. The stock trades at P/E 15, yield 3.4% and has fallen 17% in six months.

## What moves the stock
1. **G-sec yields (-3.0 per +25 bp)**: the dominant driver; it is valued as a regulated bond proxy. With the RBI's hike to 5.50% on 2026-10-07 and a US 10Y at 4.89%, the multiple has compressed.
2. **Grid build-out (+3.5)**: renewables, data centres and demand growth push transmission capex; Power Grid has asked cable and wire makers to scale up (ET 2026-10-28).
3. **Regulation (CERC ROE +3.0 per +50 bp)** and **TBCB competition (-1.5)**.
4. Policy (renewable support +1.5, power reform +1.0), defensive profile (VIX +0.8, agrees with the pack, t=2.2), flows (+1.2), small input costs (steel -0.4, aluminium -0.3, copper -0.2), repo/funding (-0.8).
The pack's USD/INR sensitivity (+1.18, t=1.0) is not significant and has the opposite sign to my prior; weight kept small.

## Transmission examples
- **Rates (4 orders)**: oil at $95 -> CPI and rupee weakness -> RBI hikes again -> 10y G-sec +25 bp -> utility earnings yields re-rate -> POWERGRID value -3% despite unchanged cash flows; reversal when yields fall.
- **Demand growth (4 orders)**: heatwave or industrial demand beats (+3pp) -> peak load rises -> CEA/CTUIL plan new ISTS evacuation lines -> bids awarded -> RAB growth -> higher PAT in 2-3 years.
- **Data centres (4 orders)**: AI-linked data-centre build-out in Mumbai/Chennai -> new load pockets -> 400/765 kV substations needed -> orders to Power Grid and equipment suppliers (Hitachi Energy India, GE Vernova T&D, CG Power) -> capex pipeline up.
- **Steel/aluminium (3 orders)**: tower steel and conductor costs up -> TBCB bidders face margin compression, private rivals bid less aggressively -> Power Grid wins better-priced awards (a small positive offset to its own cost increase).

## Current situation
Operating momentum is positive (capex raised, capitalisation doubled), but results were mixed on revenue; dividend yield support is meaningful. The market is pricing rates, not delivery.

## Upcoming
Dividend ex-date, TBCB awards, Q3 results (~February 2027), RBI/yield path, long-dated CERC period 2029-34.

## Bull / Bear
Bull: yields fall, capitalisation converts the Rs 2.2 lakh crore order book, defensive rotation. Bear: yields keep rising, private competition erodes IRRs, regulatory ROE cut after 2029. Confidence medium; debt, FX debt share and ROE base are model estimates.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.