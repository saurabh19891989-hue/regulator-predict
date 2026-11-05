# HYUNDAI — Hyundai Motor India Ltd.
*NIFTY_NEXT_50 · Automobile and Auto Components · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -2.6%**, **12 months -4.5%** (rank 165 / 157 of 200 for 3m / 12m); beta 1.07
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +20.4%): 3 months 40%, 12 months 45%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -10.0% … P90 -1.2%; plausible 12m relative-return range incl. stock-specific noise: -19.5% … +23.3%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves -2.7 pp (model impact -5.4% beta-adjusted vs realised market-adjusted move +7.9%); forward event exposure -2.9% (3m -2.0%; half assumed priced); company-specific events +1.5%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +9.96 | +5.00 | +3.69 | +0.93 | +0.34 | — |
| Indian vehicle demand (`F_AUTO_DEMAND_IN`) | +10% volumes | +9.00 | +9.00 | +0.00 | +0.00 | +0.00 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -4.03 | +0.00 | -1.45 | -2.79 | +0.21 | — |
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +3.81 | +0.00 | +4.32 | -0.08 | -0.43 | — |
| Critical-mineral supply tightness (China export controls on rare earths, magnets, graphite, Ga/Ge) (`NEW_RARE_EARTH_SUPPLY`) | +1 = new/tighter export-control round | -3.48 | +0.00 | -3.48 | +0.00 | +0.00 | — |
| Intensity of new-model competition in India passenger vehicles (`NEW_PV_SUV_COMPETITION`) | +1 = major new-model wave by rivals (about -1pp share for incumbent) | -3.00 | -3.00 | +0.00 | +0.00 | +0.00 | — |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -2.55 | +0.00 | +0.00 | -1.02 | -1.52 | — |
| Chip/electronics component supply tightness (higher = tighter) (`F_SEMICONDUCTOR_SUPPLY`) | +1 = tightening | -2.50 | -2.50 | +0.00 | +0.00 | +0.00 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -2.38 | -1.20 | -0.66 | -0.13 | -0.39 | — |
| Consumer premiumisation (`T_PREMIUMISATION`) | +1 | +2.16 | +2.00 | +0.00 | +0.16 | -0.00 | — |
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | +2.13 | +0.00 | +2.95 | -0.13 | -0.69 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -2.04 | -1.00 | -0.87 | -0.11 | -0.06 | — |
| China growth / stimulus (`F_CHINA_GDP`) | +1 pp | -2.02 | +0.00 | -0.99 | -0.64 | -0.39 | — |
| US–China trade decoupling (`C_US_CHINA_DECOUPLING`) | +1 = more decoupling | -1.96 | +0.00 | -0.80 | -1.32 | +0.16 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -10.0% | -10.0% | -6.8 | -0.3 | -1.4 | -1.5 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -4.9% | -4.9% | +0.0 | -1.7 | -3.4 | +0.3 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -3.7% | -3.7% | -3.3 | -0.1 | -0.1 | -0.2 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.36 | -6.8% | -2.4% | -3.9 | -0.8 | -1.1 | -1.0 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.58 | +4.2% | +2.4% | +2.7 | +0.4 | +0.6 | +0.5 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -2.2% | -2.2% | -1.4 | -0.6 | -0.1 | -0.1 |
| Global and Indian steel prices at multi-year highs (global HRC +60% y/y) (`EV_STEEL_RALLY_2026`) | occurred | 1.00 | -2.2% | -2.2% | -2.1 | +0.0 | -0.0 | -0.0 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -2.1% | -2.1% | -2.1 | +0.0 | +0.0 | -0.0 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +4.2% | +2.1% | +3.8 | +0.1 | +0.1 | +0.2 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -1.7% | -1.7% | +0.0 | -1.5 | -0.1 | -0.1 |
| Gold and silver slump from January 2026 peaks (silver -53%, gold -24%) (`EV_PRECIOUS_METALS_CRASH_2026`) | occurred | 1.00 | -1.3% | -1.3% | +0.0 | -1.3 | +0.0 | +0.0 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -1.3% | -1.3% | +0.0 | -0.9 | -0.3 | -0.2 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → HYUNDAI | +3.75% | +1.88% |
| 2 | EV_RARE_EARTH_CONTROLS_REIMPOSED ⇒ NEW_RARE_EARTH_SUPPLY → F_AUTO_DEMAND_IN → HYUNDAI | -4.32% | -1.08% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → HYUNDAI | -2.50% | -0.89% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → HYUNDAI | +1.50% | +0.87% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ C_MIDEAST_CONFLICT → HYUNDAI | +1.20% | +0.70% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → HYUNDAI | -2.24% | -0.63% |
| 2 | EV_BUDGET27_AGRI_RURAL ⇒ F_RURAL_DEMAND → F_AUTO_DEMAND_IN → HYUNDAI | +0.89% | +0.62% |
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → HYUNDAI | -1.20% | -0.60% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ C_MIDEAST_CONFLICT → HYUNDAI | -1.44% | -0.51% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_AI_CAPEX → F_SEMICONDUCTOR_SUPPLY → HYUNDAI | +1.80% | +0.50% |
| 2 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → HYUNDAI | -2.80% | -0.50% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → HYUNDAI | -2.25% | -0.49% |
| 2 | EV_RURAL_RELIEF_PACKAGE ⇒ F_RURAL_DEMAND → F_AUTO_DEMAND_IN → HYUNDAI | +0.89% | +0.49% |
| 1 | EV_CPI_BREACH_6PCT ⇒ F_GSEC_10Y_IN → HYUNDAI | -0.75% | -0.45% |
| 3 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_RURAL_DEMAND → F_AUTO_DEMAND_IN → HYUNDAI | +0.63% | +0.43% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_GSEC_10Y_IN → HYUNDAI | +1.70 | events | -2.55% |
| 1 | F_STEEL_INDIA → HYUNDAI | +1.65 | events | -2.47% |
| 1 | F_FPI_FLOWS → HYUNDAI | -1.60 | events | -2.40% |
| 1 | C_MIDEAST_CONFLICT → HYUNDAI | +1.50 | events | -1.80% |
| 1 | F_REPO_IN → HYUNDAI | +1.00 | events | -1.00% |
| 1 | F_ALUMINIUM → HYUNDAI | -1.96 | observed | +0.98% |
| 1 | F_AUTO_DEMAND_IN → HYUNDAI | -0.10 | events | -0.90% |
| 2 | F_AI_CAPEX → F_SEMICONDUCTOR_SUPPLY → HYUNDAI | -0.30 | events | +0.18% |
| 1 | F_USDINR → HYUNDAI | -0.37 | observed | -0.11% |
| 2 | C_US_CHINA_DECOUPLING → F_SEMICONDUCTOR_SUPPLY → HYUNDAI | -0.10 | events | +0.08% |
| 1 | F_COPPER → HYUNDAI | -0.24 | observed | +0.07% |
| 3 | C_US_CHINA_DECOUPLING → NEW_RARE_EARTH_SUPPLY → F_SEMICONDUCTOR_SUPPLY → HYUNDAI | -0.10 | events | +0.03% |

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