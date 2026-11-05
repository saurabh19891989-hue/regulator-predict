# POWERGRID — Power Grid Corporation of India Ltd.
*NIFTY_50 · Power · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +0.7%**, **12 months +2.6%** (rank 75 / 58 of 200 for 3m / 12m); beta 0.92
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +20.8%): 3 months 53%, 12 months 52%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -1.2% … P90 +7.9%; plausible 12m relative-return range incl. stock-specific noise: -17.4% … +24.3%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +1.8 pp (model impact +3.7% beta-adjusted vs realised market-adjusted move -13.1%); forward event exposure +3.0% (3m +0.5%; half assumed priced); company-specific events +0.9%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Grid & electrification capex (`T_GRID_ELECTRIFICATION`) | +1 | +3.50 | +3.50 | +0.00 | +0.00 | +0.00 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -3.34 | +0.00 | -1.68 | -1.61 | -0.04 | — |
| India 10-year G-sec yield (`F_GSEC_10Y_IN`) | +25 bp yield | -3.00 | -3.00 | +0.00 | +0.00 | -0.00 | — |
| CERC allowed regulated ROE for transmission (`NEW_CERC_ROE`) | +50 bp allowed ROE | +3.00 | +3.00 | +0.00 | +0.00 | +0.00 | — |
| Renewable / transmission policy support (`P_RENEWABLE_SUPPORT`) | +1 = stronger support | +2.63 | +1.50 | +0.82 | +0.32 | -0.01 | — |
| Indian electricity demand (`F_POWER_DEMAND_IN`) | +3 pp demand growth | +1.92 | +1.50 | +0.42 | +0.00 | +0.00 | — |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -1.82 | +0.00 | +0.00 | -0.93 | -0.90 | — |
| General-government fiscal slippage / extra borrowing vs budget (Centre + states) (`NEW_FISCAL_SLIPPAGE_IN`) | +0.5 pp of GDP deficit above budget (~Rs2 lakh cr) | -1.69 | +0.00 | -1.58 | -0.08 | -0.03 | — |
| Energy transition investment (`T_ENERGY_TRANSITION`) | +1 | +1.64 | +1.00 | +0.65 | -0.01 | +0.01 | — |
| Winning-bid discount intensity in transmission TBCB auctions (`NEW_TBCB_BID_DISCOUNTS`) | +1 = 10% lower winning equity IRR vs base | -1.50 | -1.50 | +0.00 | +0.00 | +0.00 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +1.44 | +1.20 | +0.14 | +0.02 | +0.08 | — |
| Power market / DISCOM reform (`P_POWER_REFORM`) | +1 = reform progress | +1.42 | +1.00 | +0.42 | +0.00 | +0.00 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -1.35 | -0.80 | -0.62 | +0.06 | +0.02 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -1.30 | -0.20 | -0.30 | -0.50 | -0.29 | -1.1% |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -6.5% | -6.5% | +0.0 | -0.7 | -2.6 | -3.1 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -4.2% | -4.2% | -4.2 | +0.0 | +0.0 | -0.0 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -3.8% | -3.8% | +0.0 | -1.9 | -1.9 | -0.1 |
| Cabinet approves Rs14,500 cr VGF for ~92 GWh grid-scale storage (4 Nov) (`EV_BESS_VGF_NOV26`) | occurred | 1.00 | +2.9% | +2.9% | +2.0 | +0.9 | -0.0 | +0.0 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -2.9% | -2.9% | -2.3 | -0.3 | -0.0 | -0.2 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -2.4% | -2.4% | +0.0 | -2.1 | -0.3 | -0.1 |
| Gold and silver slump from January 2026 peaks (silver -53%, gold -24%) (`EV_PRECIOUS_METALS_CRASH_2026`) | occurred | 1.00 | -2.1% | -2.1% | +0.0 | -1.9 | -0.1 | -0.0 |
| Indian spot power: IEX prices hit Rs20/unit ceiling (19 Sep), Q2 prices up ~46% y/y; El Nino lifts demand (`EV_POWER_SPOT_SPIKE`) | occurred | 1.00 | +1.9% | +1.9% | +1.5 | +0.4 | +0.0 | +0.0 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -1.7% | -1.7% | -1.7 | +0.0 | +0.0 | -0.0 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +3.3% | +1.7% | +2.7 | +0.4 | +0.1 | +0.2 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -1.5% | -1.5% | +0.0 | -1.1 | -0.3 | -0.1 |
| ALMM List-II (domestic cells) in force; approved cell capacity 37.8 GW (12th revision, 9 Oct); solar project costs seen +20% (`EV_SOLAR_ALMM2_CELL_MANDATE`) | occurred | 1.00 | +1.3% | +1.3% | +0.8 | +0.4 | +0.2 | -0.0 |

## Strongest causal chains (1st–4th order)
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26 ⇒ F_GSEC_10Y_IN → POWERGRID | -4.20% | -4.20% |
| 1 | EV_FPI_RECORD_OUTFLOW_26 ⇒ F_FPI_FLOWS → POWERGRID | -2.64% | -2.64% |
| 3 | EV_CPI_REACCEL_SEP26 ⇒ F_CPI_IN → F_REPO_IN → F_GSEC_10Y_IN → POWERGRID | -1.57% | -1.57% |
| 1 | EV_POWER_SPOT_SPIKE ⇒ F_POWER_DEMAND_IN → POWERGRID | +1.50% | +1.50% |
| 1 | EV_BESS_VGF_NOV26 ⇒ P_RENEWABLE_SUPPORT → POWERGRID | +1.50% | +1.50% |
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → POWERGRID | +3.00% | +1.50% |
| 2 | EV_UST_SELLOFF_SEP26 ⇒ F_US_10Y → F_GSEC_10Y_IN → POWERGRID | -1.33% | -1.33% |
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → POWERGRID | -2.40% | -1.20% |
| 1 | EV_GDP_Q1FY27_7_8 ⇒ F_GOVT_CAPEX → POWERGRID | +1.20% | +1.20% |
| 2 | EV_PRECIOUS_METALS_CRASH_2026 ⇒ F_US_10Y → F_GSEC_10Y_IN → POWERGRID | -1.17% | -1.17% |
| 2 | EV_CPI_REACCEL_SEP26 ⇒ F_CPI_IN → F_REPO_IN → POWERGRID | -1.06% | -1.06% |
| 4 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_CPI_IN → F_REPO_IN → F_GSEC_10Y_IN → POWERGRID | -1.05% | -1.05% |
| 1 | EV_SUMMER27_POWER_SHORTFALL ⇒ F_POWER_DEMAND_IN → POWERGRID | +2.25% | +0.90% |
| 1 | EV_RBI_OCT26_HIKE25 ⇒ F_GSEC_10Y_IN → POWERGRID | -0.90% | -0.90% |
| 1 | EV_CPI_BREACH_6PCT ⇒ F_GSEC_10Y_IN → POWERGRID | -1.50% | -0.90% |

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