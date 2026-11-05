# HYUNDAI — Hyundai Motor India Ltd.
*NIFTY_NEXT_50 · Automobile and Auto Components · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +0.3%**, **12 months +0.4%** (rank 65 / 71 of 200 for 3m / 12m); beta 1.07
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +20.4%): 3 months 51%, 12 months 52%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -3.8% … P90 +3.7%; plausible 12m relative-return range incl. stock-specific noise: -28.1% … +26.1%
- Decomposition (12m): 0.5 × forward event exposure -0.0% (3m -0.2%; half assumed priced; market-priced macro drift removed) + 0.5 × company-specific catalysts +1.0%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply +1.2% (beta-adjusted) vs a realised market-adjusted move of +7.9% — gap -6.7 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## Where the expected return comes from
Market-priced macro drivers (rates, FX, commodities, indices, volatility, flows, growth, inflation) are taken as priced, so what is left is policy, regulatory, sector, theme, geopolitical and company-specific exposure — where 2nd–4th-order effects are most likely to be missed. Percentage points of the expected relative return.
| source | 12m: 1st order | 12m: 2nd–4th order | 12m total | 3m total |
|---|---|---|---|---|
| Policy | +0.15 | +0.10 | +0.25 | -0.04 |
| Sector | -0.20 | +0.33 | +0.12 | -0.02 |
| Theme | +0.00 | -0.06 | -0.06 | -0.04 |
| Geopolitics | +0.08 | +0.20 | +0.28 | +0.27 |
| Company catalysts | +0.52 | +0.00 | +0.52 | +0.52 |
| Market-priced macro | +0.00 | +0.00 | +0.00 | +0.00 |
| Beta adjustment | — | — | -0.62 | -0.28 |
| Universe centring | — | — | -0.15 | -0.10 |
| **Expected relative return** | | | **+0.36** | **+0.31** |

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +9.80 | +5.00 | +3.69 | +0.86 | +0.25 | — |
| Indian vehicle demand (`F_AUTO_DEMAND_IN`) | +10% volumes | +9.00 | +9.00 | +0.00 | +0.00 | +0.00 | — |
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +4.30 | +0.00 | +4.32 | +0.06 | -0.08 | — |
| Critical-mineral supply tightness (China export controls on rare earths, magnets, graphite, Ga/Ge) (`NEW_RARE_EARTH_SUPPLY`) | +1 = new/tighter export-control round | -3.48 | +0.00 | -3.48 | +0.00 | +0.00 | — |
| Intensity of new-model competition in India passenger vehicles (`NEW_PV_SUV_COMPETITION`) | +1 = major new-model wave by rivals (about -1pp share for incumbent) | -3.00 | -3.00 | +0.00 | +0.00 | +0.00 | — |
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | +2.93 | +0.00 | +2.95 | +0.10 | -0.13 | — |
| Chip/electronics component supply tightness (higher = tighter) (`F_SEMICONDUCTOR_SUPPLY`) | +1 = tightening | -2.50 | -2.50 | +0.00 | +0.00 | +0.00 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -2.26 | -1.20 | -0.66 | -0.15 | -0.26 | — |
| Consumer premiumisation (`T_PREMIUMISATION`) | +1 | +2.17 | +2.00 | +0.00 | +0.16 | +0.01 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -2.05 | -1.00 | -0.87 | -0.11 | -0.07 | — |
| US–China trade decoupling (`C_US_CHINA_DECOUPLING`) | +1 = more decoupling | -2.00 | +0.00 | -0.80 | -1.32 | +0.12 | — |
| Indian wage / employee-cost inflation (`F_WAGES_IN`) | +2 pp | +1.73 | +0.00 | +0.00 | +1.83 | -0.10 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -1.72 | +0.00 | -0.88 | -1.29 | +0.45 | — |
| China growth / stimulus (`F_CHINA_GDP`) | +1 pp | -1.67 | +0.00 | -0.99 | -0.39 | -0.29 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -3.6% | -3.6% | -3.3 | -0.1 | -0.1 | -0.1 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -2.2% | -2.2% | -1.4 | -0.6 | -0.1 | -0.1 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -2.2% | -2.2% | +0.0 | -1.0 | -1.7 | +0.5 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -2.1% | -2.1% | -2.1 | +0.0 | +0.0 | -0.0 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +4.1% | +2.0% | +3.8 | +0.1 | +0.1 | +0.1 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.55 | +3.5% | +1.9% | +2.5 | +0.3 | +0.4 | +0.3 |
| Global and Indian steel prices at multi-year highs (global HRC +60% y/y) (`EV_STEEL_RALLY_2026`) | occurred | 1.00 | -1.7% | -1.7% | -1.7 | +0.0 | -0.0 | -0.0 |
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -1.4% | -1.4% | -1.2 | -0.1 | -0.1 | -0.1 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.25 | -5.5% | -1.4% | -3.6 | -0.7 | -0.7 | -0.5 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -1.2% | -1.2% | +0.0 | +0.0 | -0.8 | -0.4 |
| China re-imposes/hardens rare-earth and critical-mineral export controls hitting India's autos and electronics (`EV_RARE_EARTH_CONTROLS_REIMPOSED`) | risk_scenario | 0.25 | -4.8% | -1.2% | -0.8 | -4.3 | +0.2 | +0.1 |
| Aluminium -20% since June; copper off record; Nifty Metal -7% in October (`EV_BASE_METALS_ALUMINIUM_SLIDE`) | occurred | 1.00 | +1.1% | +1.1% | +1.1 | +0.0 | +0.0 | +0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → HYUNDAI | +3.75% | +1.88% |
| 2 | EV_RARE_EARTH_CONTROLS_REIMPOSED ⇒ NEW_RARE_EARTH_SUPPLY → F_AUTO_DEMAND_IN → HYUNDAI | -4.32% | -1.08% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → HYUNDAI | +1.30% | +0.72% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ C_MIDEAST_CONFLICT → HYUNDAI | +1.20% | +0.66% |
| 2 | EV_BUDGET27_AGRI_RURAL ⇒ F_RURAL_DEMAND → F_AUTO_DEMAND_IN → HYUNDAI | +0.89% | +0.62% |
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → HYUNDAI | -1.20% | -0.60% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → HYUNDAI | -2.20% | -0.55% |
| 2 | EV_RURAL_RELIEF_PACKAGE ⇒ F_RURAL_DEMAND → F_AUTO_DEMAND_IN → HYUNDAI | +0.89% | +0.49% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_AI_CAPEX → F_SEMICONDUCTOR_SUPPLY → HYUNDAI | +1.80% | +0.45% |
| 3 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_RURAL_DEMAND → F_AUTO_DEMAND_IN → HYUNDAI | +0.63% | +0.43% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → HYUNDAI | -1.00% | -0.42% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → HYUNDAI | -2.25% | -0.40% |
| 2 | EV_STATE_POLLS_FEB_MAR27 ⇒ F_RURAL_DEMAND → F_AUTO_DEMAND_IN → HYUNDAI | +0.59% | +0.40% |
| 2 | EV_WHEAT27_CROP_BELOW ⇒ F_RURAL_DEMAND → F_AUTO_DEMAND_IN → HYUNDAI | -0.59% | -0.38% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → HYUNDAI | -1.44% | -0.36% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_AUTO_DEMAND_IN → HYUNDAI | +0.50 | director_override | +4.50% |
| 1 | F_FPI_FLOWS → HYUNDAI | -1.60 | events | -2.40% |
| 1 | F_GSEC_10Y_IN → HYUNDAI | +1.55 | director_override | -2.33% |
| 1 | F_STEEL_INDIA → HYUNDAI | +1.35 | events | -2.03% |
| 1 | C_MIDEAST_CONFLICT → HYUNDAI | +1.00 | events | -1.20% |
| 1 | F_REPO_IN → HYUNDAI | +1.00 | events | -1.00% |
| 1 | F_ALUMINIUM → HYUNDAI | -1.96 | observed | +0.98% |
| 2 | F_AI_CAPEX → F_SEMICONDUCTOR_SUPPLY → HYUNDAI | -0.30 | events | +0.18% |
| 1 | F_USDINR → HYUNDAI | -0.37 | observed | -0.11% |
| 2 | C_US_CHINA_DECOUPLING → F_SEMICONDUCTOR_SUPPLY → HYUNDAI | -0.10 | events | +0.08% |
| 1 | F_COPPER → HYUNDAI | -0.24 | observed | +0.07% |
| 3 | C_US_CHINA_DECOUPLING → NEW_RARE_EARTH_SUPPLY → F_SEMICONDUCTOR_SUPPLY → HYUNDAI | -0.10 | events | +0.03% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-12 | New model launches (Bayon / new Venue cycle) driving volumes | other | 0.70 | +1.5% | +1.05% |
| 2027-01 | Q3 FY27 results (margin recovery test; CLSA expects recovery) | results | 0.95 | +0.0% | +0.00% |
| 2027-03 | Talegaon Phase-1 ramp-up: start-up costs and depreciation vs volume gains | capex | 0.80 | +0.0% | +0.00% |

## Analyst profile (agent research, sourced)
# Hyundai Motor India Ltd. (HYUNDAI) — Market Impact profile, 2026-11-05

## Business
Hyundai Motor India (HMIL) is India's second-largest car maker, 82.5% owned by Hyundai Motor Company and listed in October 2024. It sells mainly SUVs (Creta, Venue, Alcazar, Exter) plus the Grand i10, Aura, i20 and Verna, and is rolling out EV and hybrid variants. Roughly 78% of revenue is domestic and 20% exports to the Middle East, Africa, Latin America and South Asia (4 million cumulative exports, V3Cars 2026-10-16). It is debt-free, earns ROE ~30%, and pays a royalty to the parent of about 3.5% of sales (model knowledge). On 2026-10-14 it inaugurated its Talegaon (Pune) plant under a Rs 11,000 cr plan to 2030, which adds ~3.2 lakh units of capacity and takes the total toward 11.4 lakh.

## What moves the stock (ranked)
1. **Domestic PV demand (F_AUTO_DEMAND_IN, +9 per +10% volumes).** Operating leverage is high; the margin has fallen to ~10% so incremental volume is worth more.
2. **Margin versus input costs.** Steel (-1.5 per +7%), aluminium, copper, platinum-group metals. Global HRC is +20.6% since June, aluminium -19.6%, so the cost mix is turning mildly favourable for aluminium and adverse for steel.
3. **Competition / market share (-3).** The Q2 call and brokerage notes hinge on whether new models stop the share slide.
4. **Policy: GST (+5 per further cut), rates (repo -1.0), discount rate (G-sec -1.5).** The Sept-2025 GST 2.0 cut boosted compact-car demand; the 7 Oct 2026 RBI hike to 5.50% is the new headwind.
5. **Supply shocks (semiconductors, rare earths: -2.5)** and **Mideast/Hormuz risk (-1.2).**
6. **Flows (F_FPI_FLOWS +1.5).** FIIs cut from 5.4% to 3.2% in two quarters.

## Transmission examples
- **Oil-shock chain (4 orders).** Iran tanker attacks / Hormuz risk -> Brent above $100 (8 Oct) -> petrol/diesel and CNG prices and inflation expectations up, INR weaker (94.5) -> RBI delivers a 25bp hike (7 Oct) and signals no cuts -> car loans dearer (~80% of cars are financed) and used-car/first-time buyers delay -> Hyundai's entry-SUV volumes soften while discounts rise -> margin falls further below 10%.
- **Steel / margin chain (3 orders).** China steel export policy and a strong global HRC (+20.6%) -> Indian steel prices up -> body-in-white cost up 4-5% of materials -> without price increases (competition limits pass-through) EBITDA margin loses 40-70bp.
- **Share chain (3 orders).** Competitors launch new compact SUVs -> Hyundai discounts to defend volumes -> margin down -> brokerages (Jefferies) cut estimates -> stock derates relative to M&M/Tata.
- **Policy chain (3 orders).** GST rationalisation -> lower on-road prices for small cars -> entry-segment recovery where Hyundai's Grand i10/Exter/Venue play -> operating leverage on higher volumes.
- **Korea link.** Parent capex ($15.5bn plan through 2032) and Won/USD move component and royalty costs; the headline plan is a positive signal for localisation and exports.

## Current situation
Q2 FY27 (Sep 2026): record sales of Rs 20,696 cr but EBITDA margin ~10% and net profit Rs 1,196 cr (-24% y/y) as expenses outpaced revenue (Moneycontrol 2026-10-28). Shares still rose 5-6% on the view that margins trough: CLSA expects recovery, Nomura points to the new model cycle (Bayon), Morgan Stanley is bullish, Jefferies warns about share loss. September was the highest-ever monthly sales; October was strong again. 12-month price -11%, 3-month -4%, 1-month +6.8%.

## Upcoming events
Monthly sales on the 1st; Q3 FY27 results ~January 2027; Pune ramp-up; Union Budget 1 Feb 2027; any further GST/EV policy.

## Bull case
New launches stabilise share at 13%+, margins recover to 12-13% as depreciation spreads over higher volumes and aluminium eases, exports from Pune grow, and the GST-led small-car recovery continues.

## Bear case
Share erosion forces discounting; steel and PGM costs stay high; the rate hike slows retail; the Pune plant's depreciation outruns volume; FIIs keep selling a stock with a lock-in-driven shareholder base. Limits: cost shares, export mix and royalty rate are model estimates; Jefferies' detailed caution was only seen as a headline.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.