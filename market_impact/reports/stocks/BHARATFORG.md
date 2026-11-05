# BHARATFORG — Bharat Forge Ltd.
*MIDCAP_100 · Automobile and Auto Components · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +0.3%**, **12 months +0.5%** (rank 66 / 61 of 200 for 3m / 12m); beta 1.23
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +24.9%): 3 months 51%, 12 months 50%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -3.5% … P90 +5.0%; plausible 12m relative-return range incl. stock-specific noise: -31.4% … +32.1%
- Decomposition (12m): 0.5 × forward event exposure -0.3% (3m -1.0%; half assumed priced; market-priced macro drift removed) + 0.5 × company-specific catalysts +1.6%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply +4.7% (beta-adjusted) vs a realised market-adjusted move of -11.3% — gap +16.0 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## Where the expected return comes from
Market-priced macro drivers (rates, FX, commodities, indices, volatility, flows, growth, inflation) are taken as priced, so what is left is policy, regulatory, sector, theme, geopolitical and company-specific exposure — where 2nd–4th-order effects are most likely to be missed. Percentage points of the expected relative return.
| source | 12m: 1st order | 12m: 2nd–4th order | 12m total | 3m total |
|---|---|---|---|---|
| Policy | +0.00 | +0.08 | +0.08 | -0.34 |
| Sector | -0.05 | +0.11 | +0.06 | +0.04 |
| Theme | +0.21 | -0.07 | +0.14 | +0.05 |
| Geopolitics | +0.00 | +0.29 | +0.29 | +0.06 |
| Company catalysts | +0.82 | +0.00 | +0.82 | +0.90 |
| Market-priced macro | +0.00 | +0.00 | +0.00 | +0.00 |
| Beta adjustment | — | — | -0.70 | -0.32 |
| Universe centring | — | — | -0.15 | -0.10 |
| **Expected relative return** | | | **+0.54** | **+0.29** |

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| India–Pakistan tension (`C_INDIA_PAKISTAN`) | +1 = escalation | +3.74 | +0.00 | +3.54 | +0.21 | -0.01 | — |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +3.25 | +0.00 | +2.46 | +0.40 | +0.39 | — |
| Indian defence procurement & indigenisation (`P_DEFENCE_PROCUREMENT`) | +10% domestic orders | +3.25 | +3.00 | +0.24 | +0.00 | +0.01 | — |
| Indian vehicle demand (`F_AUTO_DEMAND_IN`) | +10% volumes | +3.00 | +3.00 | +0.00 | +0.00 | +0.00 | — |
| US tariffs on Indian goods (`P_US_TARIFF_INDIA`) | +10 pp average tariff | -2.99 | -3.00 | +0.04 | -0.02 | -0.02 | — |
| Russia (oil discounts, defence, sanctions) (`C_RUSSIA`) | +1 = closer trade access / larger discounts | -2.02 | +0.00 | -2.02 | -0.01 | -0.00 | — |
| India 10-year G-sec yield (`F_GSEC_10Y_IN`) | +25 bp yield | -2.00 | -2.00 | +0.00 | +0.00 | +0.00 | — |
| Indian defence exports (`T_DEFENCE_EXPORTS`) | +1 | +2.00 | +2.00 | +0.00 | +0.00 | +0.00 | — |
| US growth (`F_US_GDP`) | +1 pp | +1.95 | +1.80 | +0.16 | +0.15 | -0.16 | — |
| US average effective tariff rate (all partners) (`NEW_US_TARIFF_GLOBAL`) | +5 pp effective tariff rate | -1.94 | +0.00 | -1.56 | -0.11 | -0.27 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | +1.79 | +2.50 | -0.32 | -0.20 | -0.19 | -1.1% |
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +1.54 | +0.00 | +1.44 | +0.18 | -0.08 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -1.53 | +0.00 | -1.40 | -0.08 | -0.05 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +1.39 | +1.50 | -0.15 | +0.01 | +0.03 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| DAC clears Rs 1.10 lakh crore (7 Sep) and further proposals (Rs 2.12 lakh crore reported 26 Oct) (`EV_DAC_APPROVALS_H2_26`) | occurred | 1.00 | +3.2% | +3.2% | +3.0 | +0.2 | +0.0 | +0.0 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -3.1% | -3.1% | -3.3 | +0.3 | -0.0 | -0.1 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -2.8% | -2.8% | -2.8 | +0.0 | +0.0 | -0.0 |
| US Q3 data: GDP 3.4%, CPI 3.7%, September payrolls only +29k (`EV_US_Q3_DATA_MIXED`) | occurred | 1.00 | +2.3% | +2.3% | +2.2 | +0.2 | -0.1 | -0.0 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +3.4% | +1.7% | +3.8 | -0.5 | +0.1 | +0.1 |
| US recession (two negative quarters or NBER-style) beginning by mid-2027 (`EV_US_RECESSION_RISK_2027`) | risk_scenario | 0.25 | -6.0% | -1.5% | -5.4 | -1.9 | +1.4 | -0.1 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -1.4% | -1.4% | -0.6 | -0.6 | -0.1 | -0.1 |
| US waives Russia-oil secondary sanctions/100% tariff threat on buyers incl. India (17 Oct) (`EV_RUSSIA_WAIVER_OCT17`) | occurred | 1.00 | +1.4% | +1.4% | +1.5 | -0.1 | -0.0 | +0.0 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -1.3% | -1.3% | +0.0 | +0.0 | -1.4 | +0.1 |
| US midterms (3 Nov 2026): Democrats win House and Senate (`EV_US_MIDTERMS_DEM_SWEEP`) | occurred | 1.00 | +1.1% | +1.1% | +1.1 | +0.0 | -0.0 | +0.0 |
| Waiver lapses and US imposes secondary tariff (up to 100%) or sanctions on Indian refiners buying Russian oil (`EV_RUSSIA_TARIFF_ENFORCED`) | risk_scenario | 0.15 | -7.1% | -1.1% | -7.1 | +0.2 | -0.1 | -0.2 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -1.0% | -1.0% | +0.0 | -0.8 | -0.2 | +0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → BHARATFORG | +3.75% | +1.88% |
| 1 | EV_US_RECESSION_RISK_2027 ⇒ F_US_GDP → BHARATFORG | -5.40% | -1.35% |
| 1 | EV_RUSSIA_TARIFF_ENFORCED ⇒ P_US_TARIFF_INDIA → BHARATFORG | -7.50% | -1.12% |
| 1 | EV_INDIA_US_INTERIM_DEAL_SIGNED ⇒ P_US_TARIFF_INDIA → BHARATFORG | +1.50% | +0.83% |
| 1 | EV_INDIA_US_TALKS_COLLAPSE ⇒ P_US_TARIFF_INDIA → BHARATFORG | -4.50% | -0.81% |
| 1 | EV_BUDGET27_CAPEX_RAILWAY ⇒ P_DEFENCE_PROCUREMENT → BHARATFORG | +0.90% | +0.81% |
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → BHARATFORG | -1.60% | -0.80% |
| 1 | EV_DEFENCE_EXPORT_ORDERS ⇒ T_DEFENCE_EXPORTS → BHARATFORG | +1.20% | +0.60% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_USDINR → BHARATFORG | +3.25% | +0.58% |
| 2 | EV_RUSSIAN_CRUDE_CUT_TRADE_DEAL ⇒ C_RUSSIA → P_US_TARIFF_INDIA → BHARATFORG | +1.92% | +0.58% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → BHARATFORG | -2.25% | -0.40% |
| 2 | EV_RUSSIA_WAIVER_EXTENDED ⇒ C_RUSSIA → P_US_TARIFF_INDIA → BHARATFORG | -0.58% | -0.40% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → BHARATFORG | -1.44% | -0.36% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_FPI_FLOWS → BHARATFORG | -1.44% | -0.36% |
| 2 | EV_RARE_EARTH_CONTROLS_REIMPOSED ⇒ NEW_RARE_EARTH_SUPPLY → F_AUTO_DEMAND_IN → BHARATFORG | -1.44% | -0.36% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_GSEC_10Y_IN → BHARATFORG | +1.55 | director_override | -3.10% |
| 1 | F_FPI_FLOWS → BHARATFORG | -1.60 | events | -2.40% |
| 1 | F_US_GDP → BHARATFORG | +1.20 | events | +2.16% |
| 1 | P_US_TARIFF_INDIA → BHARATFORG | -0.60 | events | +1.80% |
| 1 | F_AUTO_DEMAND_IN → BHARATFORG | +0.50 | director_override | +1.50% |
| 1 | P_DEFENCE_PROCUREMENT → BHARATFORG | +0.50 | director_override | +1.50% |
| 1 | F_STEEL_INDIA → BHARATFORG | +1.35 | events | -0.94% |
| 1 | F_USDINR → BHARATFORG | -0.37 | observed | -0.92% |
| 1 | T_ENERGY_TRANSITION → BHARATFORG | +0.30 | director_override | -0.30% |
| 1 | F_EU_GDP → BHARATFORG | +0.22 | events | +0.22% |
| 2 | P_DEFENCE_PROCUREMENT → T_DEFENCE_EXPORTS → BHARATFORG | +0.50 | director_override | +0.12% |
| 1 | F_BRENT → BHARATFORG | +0.00 | observed | +0.00% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-11-05 | Q2 FY27 results (post-loss quarter; watch OPM recovery and exceptional items) | results | 1.00 | +0.0% | +0.00% |
| 2026-12 | Defence orders (artillery, ammunition) and KSSL ramp | other | 0.60 | +3.0% | +1.80% |
| 2027-02 | Q3 FY27 results | results | 0.95 | +0.0% | +0.00% |
| 2027-03 | India-US trade deal or additional US tariff on Indian goods | regulatory | 0.30 | -0.5% | -0.15% |

## Analyst profile (agent research, sourced)
# Bharat Forge Ltd. (BHARATFORG) — Market Impact profile, 2026-11-05

## Business
Bharat Forge makes forged and machined components: crankshafts, axle beams and chassis parts for commercial vehicles and passenger cars, plus industrial forgings (oil & gas, rail, power), aerospace parts, and defence products through Kalyani Strategic Systems (artillery, ammunition, armoured vehicles). Exports are about 45% of revenue, led by the US and Europe. Q1 FY27 sales were Rs 4,640 cr (+19% y/y) at an OPM of 15%, but a Rs 358 cr exceptional item (not characterised in the sources retrieved) produced a net loss of Rs 90 cr. The company raised Rs 2,000 cr in a QIP at Rs 1,890 (23 Sep 2026), then invested Rs 2,400 cr in KSSL (16 Oct) and signed a long-term Pratt & Whitney Canada engine-part deal (5 Oct). Q2 FY27 results are due 5 November 2026.

## What moves the stock (ranked)
1. **Q2/Q3 earnings quality**: margin recovery from 15% and absence of further exceptional items; P/E of 89 on trailing earnings.
2. **US trade policy and truck cycle**: tariffs (-3.0 per +10pp) and US growth (+1.8).
3. **Defence (P_DEFENCE_PROCUREMENT +3.0, T_DEFENCE_EXPORTS +2.0)**: the growth narrative.
4. **USD/INR (+2.5 per +3%)** and **discount rate (G-sec -2.0).**
5. **Steel (-0.7)**, with pass-through formulas, and **India auto volumes (+3.0).**
6. **Structural EV drag (-1.0)** offset by aerospace, rail and defence.

## Transmission examples
- **Tariff chain (4 orders).** India-US trade talks stall (Reuters 6 Oct) -> additional duty on India-origin forgings -> US Class 8 and industrial customers absorb part but reshuffle suppliers -> Bharat Forge's US volumes and prices fall -> utilisation at Pune/Baramati forging lines declines -> operating leverage amplifies the EBITDA hit.
- **Oil chain (3 orders).** Brent $95-100 -> US shale and oil & gas capex improves -> industrial forging orders (oil & gas) rise -> positive for Bharat Forge exports; at the same time India's diesel prices hurt Indian trucking -> domestic CV orders slow.
- **Steel chain (3 orders).** Global HRC +20.6% -> special-steel bar price up -> pass-through formulas recover most with a quarter's lag -> working-capital strain and a transient 30-60bp margin dip.
- **Defence chain (4 orders).** Geopolitical tensions (Iran, Russia-NATO) -> Western demand for artillery and ammunition -> export orders for KSSL -> utilisation of defence lines, higher margin mix -> re-rating.
- **Rates/flows chain (3 orders).** US 10-year 4.89% -> FPI outflows -> high-multiple midcaps derate -> equity raised in QIP at Rs 1,890 is under water, weighing sentiment.

## Current situation
The stock trades at Rs 1,815 (3-month -17.9%) below the QIP price. Promoter holding fell 0.95 point to 43.12% in Sep 2026. Domestic institutions hold 33%. The Q1 loss, the QIP and the KSSL investment mean Q2 numbers carry heavy weight. Q2 results are due today, so the figures were not available at analysis time.

## Upcoming events
Q2 FY27 results (today), Q3 (Feb), tariff decisions, defence orders, Budget (1 Feb 2027).

## Bull case
A clean quarter with 17%+ OPM, defence/aerospace momentum, and US tariff relief re-rate the stock toward the Rs 2,295 high.

## Bear case
Another exceptional item or margin miss, US tariffs, weaker CV cycle, and a derating of an 89x P/E. Limits: the exceptional item's nature and the Q2 result were not retrieved; mix and cost shares are estimates.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.