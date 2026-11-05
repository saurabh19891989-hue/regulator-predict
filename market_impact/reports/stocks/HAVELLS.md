# HAVELLS — Havells India Ltd.
*MIDCAP_100 · Consumer Durables · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +0.3%**, **12 months +0.8%** (rank 71 / 56 of 200 for 3m / 12m); beta 1.15
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +18.3%): 3 months 51%, 12 months 52%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -1.7% … P90 +3.9%; plausible 12m relative-return range incl. stock-specific noise: -22.8% … +25.0%
- Decomposition (12m): 0.5 × forward event exposure +1.8% (3m +0.7%; half assumed priced; market-priced macro drift removed) + 0.5 × company-specific catalysts +0.2%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply +2.7% (beta-adjusted) vs a realised market-adjusted move of -11.7% — gap +14.4 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Residential real-estate sales (`F_HOUSING_DEMAND`) | +10% sales volume | +2.57 | +2.50 | +0.00 | +0.04 | +0.03 | — |
| Private corporate capex (`F_PRIVATE_CAPEX`) | +10% capex growth | +2.24 | +2.00 | +0.00 | +0.20 | +0.04 | — |
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +1.68 | +1.50 | +0.00 | +0.19 | -0.01 | — |
| Central + state government capex (`F_GOVT_CAPEX`) | +10% capex growth | +1.57 | +1.20 | +0.16 | +0.16 | +0.04 | — |
| Indian data-centre build-out (`T_DATA_CENTRES_IN`) | +1 | +1.57 | +1.50 | +0.06 | +0.00 | +0.01 | — |
| Formalisation of the economy (`T_FORMALISATION`) | +1 | +1.54 | +1.50 | +0.00 | +0.04 | +0.00 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -1.17 | +0.00 | -0.59 | -0.48 | -0.10 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -1.13 | +0.00 | -1.04 | -0.07 | -0.02 | — |
| Consumer durables category promotional / discount intensity (`NEW_CONSUMER_DURABLES_PRICE_WAR`) | +1 pp of industry-wide margin given up (discounts, channel incentives, ad spend) in room AC and appliances | -1.10 | -1.10 | +0.00 | +0.00 | +0.00 | — |
| India real GDP growth (`F_GDP_IN`) | +1 pp | +1.02 | +0.00 | +1.00 | +0.13 | -0.11 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -0.99 | -0.80 | +0.00 | -0.11 | -0.08 | -1.1% |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +0.92 | +0.00 | +0.62 | +0.05 | +0.25 | — |
| India 10-year G-sec yield (`F_GSEC_10Y_IN`) | +25 bp yield | -0.92 | -0.80 | -0.10 | -0.02 | +0.00 | — |
| General-government fiscal slippage / extra borrowing vs budget (Centre + states) (`NEW_FISCAL_SLIPPAGE_IN`) | +0.5 pp of GDP deficit above budget (~Rs2 lakh cr) | -0.89 | +0.00 | -0.70 | -0.13 | -0.06 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| India Q1 FY27 GDP grows 7.8% (31 Aug 2026), beating ~7.3% consensus (`EV_GDP_Q1FY27_7_8`) | occurred | 1.00 | +2.0% | +2.0% | +1.5 | +0.7 | -0.1 | -0.1 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -1.4% | -1.4% | +0.0 | -0.7 | -0.6 | -0.2 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -1.4% | -1.4% | -1.1 | -0.2 | -0.0 | -0.0 |
| Aluminium -20% since June; copper off record; Nifty Metal -7% in October (`EV_BASE_METALS_ALUMINIUM_SLIDE`) | occurred | 1.00 | -1.2% | -1.2% | -1.2 | +0.0 | +0.0 | +0.0 |
| Global and Indian steel prices at multi-year highs (global HRC +60% y/y) (`EV_STEEL_RALLY_2026`) | occurred | 1.00 | -1.2% | -1.2% | -1.0 | -0.1 | -0.0 | -0.0 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -1.1% | -1.1% | -0.2 | -0.8 | -0.0 | -0.0 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -0.7% | -0.7% | +0.0 | +0.0 | -0.3 | -0.4 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -0.5% | -0.5% | +0.0 | -0.3 | -0.2 | -0.0 |
| Risk: USD/INR >98 and/or reserves < US$650bn (disorderly rupee, emergency RBI response) (`EV_RUPEE_BREAK_98_RESERVE_STRESS`) | risk_scenario | 0.18 | -2.8% | -0.5% | -1.8 | -0.9 | -0.1 | +0.0 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -0.5% | -0.5% | +0.0 | -0.5 | -0.0 | -0.0 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -0.5% | -0.5% | +0.0 | -0.4 | -0.1 | +0.0 |
| Risk: stagflation scare - CPI >=6.5% while GDP growth slips below ~6% (Q3 FY27 data, late Feb 2027) (`EV_INDIA_STAGFLATION_SCARE`) | risk_scenario | 0.12 | -3.9% | -0.5% | +0.0 | -3.1 | -0.7 | -0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → HAVELLS | -0.64% | -0.32% |
| 2 | EV_LABOUR_CODES_RULES ⇒ P_LABOUR_CODES → T_FORMALISATION → HAVELLS | +0.36% | +0.29% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_AI_CAPEX → T_DATA_CENTRES_IN → HAVELLS | -1.08% | -0.27% |
| 2 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → F_HOUSING_DEMAND → HAVELLS | -0.52% | -0.22% |
| 1 | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → HAVELLS | +0.24% | +0.22% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_USDINR → HAVELLS | -1.04% | -0.19% |
| 2 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → F_USDINR → HAVELLS | +0.37% | +0.18% |
| 2 | EV_CHINA_NPC_MAR27_BIG_STIMULUS ⇒ F_CHINA_GDP → F_COPPER → HAVELLS | +0.47% | +0.16% |
| 1 | EV_FERT_SUBSIDY_TOPUP_WINTER ⇒ F_GSEC_10Y_IN → HAVELLS | -0.16% | -0.14% |
| 1 | EV_CHINA_CEWC_STIMULUS_DEC26 ⇒ F_COPPER → HAVELLS | +0.32% | +0.14% |
| 1 | EV_CPI_BREACH_6PCT ⇒ F_GSEC_10Y_IN → HAVELLS | -0.24% | -0.14% |
| 1 | EV_BANKING_LIQUIDITY_DEFICIT_MAR27 ⇒ F_GSEC_10Y_IN → HAVELLS | -0.24% | -0.14% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_GSEC_10Y_IN → HAVELLS | -0.80% | -0.14% |
| 2 | EV_RBI_FEB27_HIKE25 ⇒ F_REPO_IN → F_HOUSING_DEMAND → HAVELLS | -0.52% | -0.14% |
| 1 | EV_CHINA_STEEL_EXPORT_FLOOD ⇒ F_STEEL_GLOBAL → HAVELLS | +0.50% | +0.12% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_GSEC_10Y_IN → HAVELLS | +1.55 | director_override | -1.24% |
| 1 | F_ALUMINIUM → HAVELLS | -1.96 | observed | -0.98% |
| 2 | F_REPO_IN → F_HOUSING_DEMAND → HAVELLS | +1.00 | events | -0.52% |
| 1 | T_FORMALISATION → HAVELLS | +0.30 | events | +0.45% |
| 2 | F_GDP_IN → F_HOUSING_DEMAND → HAVELLS | +0.50 | events | +0.30% |
| 1 | F_URBAN_DEMAND → HAVELLS | +0.20 | events | +0.30% |
| 1 | F_USDINR → HAVELLS | -0.37 | observed | +0.30% |
| 1 | F_STEEL_GLOBAL → HAVELLS | +0.50 | director_override | -0.25% |
| 1 | F_GOVT_CAPEX → HAVELLS | +0.20 | director_override | +0.24% |
| 2 | F_GDP_IN → F_PRIVATE_CAPEX → HAVELLS | +0.50 | events | +0.20% |
| 1 | F_COPPER → HAVELLS | -0.24 | observed | -0.19% |
| 2 | F_GSEC_10Y_IN → F_HOUSING_DEMAND → HAVELLS | +1.55 | director_override | -0.15% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-12 | Cable list-price / metal-pass-through repricing following aluminium decline; margin recovery or competitive price cuts | guidance | 0.50 | +0.5% | +0.25% |
| 2027-01 | Q3 FY27 results (date not announced; Q2 was 2026-10-22). Watch cable contribution margin and Lloyd profitability | results | 0.95 | +0.0% | +0.00% |
| 2027-03 | Summer 2027 fan/Lloyd AC demand and price increases (industry hikes up to 8%) | other | 0.80 | +0.0% | +0.00% |

## Analyst profile (agent research, sourced)
# HAVELLS - Havells India Ltd. (midcap, electricals and consumer durables)

## Business
Debt-free electrical-products group: cables & wires 47% of Q2 FY27 revenue (Rs2,999cr, +47.9%), plus switchgear, lighting, electrical consumer durables (fans, heaters, appliances) and the Lloyd brand. TTM revenue ~Rs25,188cr, EBITDA ~9.1%. Cable prices float with copper and aluminium, so margins swing with metal-price direction rather than level.

## What moves the stock (ranked)
1. **Copper and aluminium (+0.8 / +0.5 per +10%)**: counter-intuitive sign (rising metals give inventory gains; falling metals compress contribution margin). Q2 cable contribution margin fell to 13.9% from 17.7% on the aluminium fall (-19.6% since June).
2. **Housing and construction (+2.5), private capex (+2.0), government capex (+1.2), data centres (+1.5).**
3. **Urban demand (+1.5)** for fans/appliances/Lloyd; **price war (-1.1)** in Lloyd categories.
4. FX (-0.8), steel (-0.5), formalisation (+1.5), G-sec yield (-0.8).

## Transmission examples
- **China demand shock -> copper and aluminium fall (1st) -> Havells cable price cuts and inventory losses (2nd) -> cable contribution margin down 300-400bp (3rd) -> consensus EBITDA cuts and de-rating (4th).**
- **AI/grid capex boom -> power-cable and switchgear demand up -> copper up -> short-term inventory gain, but copper-intensive Lloyd/fans cost up -> net slightly positive.**
- **Brent up -> INR weaker -> RBI on hold -> housing demand softer -> wires, lighting and fans installed less -> Havells ECD and wire volumes down.**
- **Government power-T&D spend rises -> PSU orders to cable makers incl. Polycab/KEI -> pricing competition at the large-order end intensifies, hitting contribution margin.**

## Current situation
Q2 FY27 beat estimates (revenue +34.6%, EBITDA +30.5%) but margin 8.98% vs 9.27% and cable contribution margin fell; the stock still made a new 52-week low on 2026-10-23. UBS downgraded (2026-10-09); Citi Buy; Nomura Neutral. Price Rs1,073, -28% in 12m. Pack empirical gold/silver betas (t=2.5/2.0) are spurious and ignored; copper (+0.96, t=1.8) agrees.

## Upcoming
Q3 FY27 results (~late Jan 2027); cable repricing; summer 2027 season.

## Bull / bear
Bull: metal stabilises, cables margin recovers, data-centre/capex tailwinds, market share gains; valuation reset to 39x. Bear: cables competitive intensity, aluminium/copper volatility, Lloyd drag and growth rotation.

Uncertainties: segment split beyond cables is approximate; metal-share-of-cost estimates; inventory-day assumption (30 days) not disclosed.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.