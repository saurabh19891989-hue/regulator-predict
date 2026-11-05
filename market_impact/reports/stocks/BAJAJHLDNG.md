# BAJAJHLDNG — Bajaj Holdings & Investment Ltd.
*NIFTY_NEXT_50 · Financial Services · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -0.1%**, **12 months -0.6%** (rank 123 / 141 of 200 for 3m / 12m); beta 1.04
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +20.9%): 3 months 50%, 12 months 51%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -2.8% … P90 +0.8%; plausible 12m relative-return range incl. stock-specific noise: -26.8% … +26.1%
- Decomposition (12m): 0.5 × forward event exposure -1.6% (3m -0.5%; half assumed priced; market-priced macro drift removed) + 0.5 × company-specific catalysts +0.6%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply -0.1% (beta-adjusted) vs a realised market-adjusted move of +0.5% — gap -0.5 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## Where the expected return comes from
Market-priced macro drivers (rates, FX, commodities, indices, volatility, flows, growth, inflation) are taken as priced, so what is left is policy, regulatory, sector, theme, geopolitical and company-specific exposure — where 2nd–4th-order effects are most likely to be missed. Percentage points of the expected relative return.
| source | 12m: 1st order | 12m: 2nd–4th order | 12m total | 3m total |
|---|---|---|---|---|
| Policy | +0.05 | -0.02 | +0.03 | -0.00 |
| Regulatory | +0.00 | -0.35 | -0.35 | -0.08 |
| Sector | +0.00 | +0.09 | +0.09 | +0.09 |
| Theme | +0.00 | +0.02 | +0.02 | +0.02 |
| Geopolitics | +0.00 | -0.01 | -0.01 | -0.00 |
| Company catalysts | +0.31 | -0.00 | +0.31 | +0.24 |
| Market-priced macro | +0.00 | +0.00 | +0.00 | +0.00 |
| Beta adjustment | — | — | -0.60 | -0.27 |
| Universe centring | — | — | -0.15 | -0.10 |
| **Expected relative return** | | | **-0.64** | **-0.09** |

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| India CPI inflation (`F_CPI_IN`) | +1 pp | -1.45 | +0.00 | -0.74 | -0.46 | -0.25 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -1.36 | -1.00 | -0.04 | -0.18 | -0.14 | -1.1% |
| Household savings shift to financial assets (`T_FINANCIALISATION`) | +1 | +1.36 | +1.00 | +0.40 | -0.01 | -0.03 | — |
| Credit cost / NPA cycle (higher = worse) (`F_ASSET_QUALITY_IN`) | +50 bp credit cost | -1.34 | +0.00 | -1.22 | -0.11 | -0.01 | — |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -1.34 | -0.60 | -0.51 | -0.19 | -0.04 | +3.5% |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +1.31 | +1.00 | +0.31 | -0.00 | +0.00 | — |
| RBI prudential tightening (risk weights, LCR, provisioning) (`P_RBI_PRUDENTIAL`) | +1 = tightening step | -1.29 | +0.00 | -0.76 | -0.60 | +0.07 | — |
| India 10-year G-sec yield (`F_GSEC_10Y_IN`) | +25 bp yield | -1.26 | -0.80 | -0.40 | -0.05 | -0.01 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -1.20 | +0.00 | -0.36 | -0.59 | -0.25 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -1.17 | -0.60 | -0.25 | -0.33 | +0.01 | — |
| Unsecured retail & microfinance stress (higher = worse) (`F_UNSECURED_STRESS`) | +1 pp delinquencies | -1.16 | +0.00 | -0.85 | -0.26 | -0.04 | — |
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +1.14 | +0.00 | +0.61 | +0.34 | +0.19 | — |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +1.10 | +0.00 | +0.00 | +0.82 | +0.28 | — |
| Insurance regulation tightening (IRDAI) (`P_IRDAI_REG`) | +1 = tightening | -1.08 | +0.00 | -1.03 | -0.04 | +0.00 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -2.9% | -2.9% | -2.2 | -0.7 | +0.0 | +0.0 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -1.9% | -1.9% | -1.1 | -0.7 | -0.0 | +0.0 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +3.6% | +1.8% | +2.7 | +0.9 | -0.0 | +0.0 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -1.7% | -1.7% | +0.0 | -0.8 | -0.5 | -0.3 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.25 | -5.7% | -1.4% | -3.9 | -1.3 | -0.5 | +0.0 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -1.3% | -1.3% | -0.8 | -0.3 | -0.2 | +0.0 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -1.1% | -1.1% | +0.0 | -0.8 | -0.3 | +0.0 |
| Risk: USD/INR >98 and/or reserves < US$650bn (disorderly rupee, emergency RBI response) (`EV_RUPEE_BREAK_98_RESERVE_STRESS`) | risk_scenario | 0.18 | -5.2% | -0.9% | -4.2 | -0.6 | -0.4 | +0.0 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -0.9% | -0.9% | +0.0 | -0.8 | -0.2 | +0.1 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.55 | +1.7% | +0.9% | +0.2 | +0.9 | +0.2 | +0.2 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.25 | -3.2% | -0.8% | -0.6 | -1.7 | -0.5 | -0.4 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -0.8% | -0.8% | +0.0 | +0.0 | -0.2 | -0.6 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → BAJAJHLDNG | +2.50% | +1.25% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → BAJAJHLDNG | -2.40% | -0.60% |
| 1 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → BAJAJHLDNG | -2.40% | -0.60% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → BAJAJHLDNG | -1.50% | -0.38% |
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → BAJAJHLDNG | -0.64% | -0.32% |
| 2 | EV_IRDAI_COMMISSION_RESET ⇒ P_IRDAI_REG → BAJAJFINSV → BAJAJHLDNG | -0.64% | -0.32% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → BAJAJHLDNG | -1.50% | -0.27% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → BAJAJHLDNG | -0.60% | -0.25% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_USDINR → BAJAJHLDNG | -1.30% | -0.23% |
| 2 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → BAJAJFINSV → BAJAJHLDNG | +0.46% | +0.23% |
| 1 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → BAJAJHLDNG | -1.50% | -0.22% |
| 2 | EV_ECL_ROLLOUT_APR27 ⇒ P_RBI_PRUDENTIAL → BAJAJFINSV → BAJAJHLDNG | -0.23% | -0.21% |
| 1 | EV_NVDA_NOV17_BEAT ⇒ F_US_EQUITIES → BAJAJHLDNG | +0.32% | +0.20% |
| 1 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_US_EQUITIES → BAJAJHLDNG | -1.20% | -0.18% |
| 1 | EV_BUDGET_FY28_LTCG_RELIEF ⇒ F_FPI_FLOWS → BAJAJHLDNG | +0.50% | +0.17% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_FPI_FLOWS → BAJAJHLDNG | -1.60 | events | -1.60% |
| 1 | F_GSEC_10Y_IN → BAJAJHLDNG | +1.55 | director_override | -1.24% |
| 1 | F_REPO_IN → BAJAJHLDNG | +1.00 | events | -0.60% |
| 2 | F_GSEC_10Y_IN → BAJAJFINSV → BAJAJHLDNG | +1.55 | director_override | -0.47% |
| 1 | F_USDINR → BAJAJHLDNG | -0.37 | observed | +0.37% |
| 2 | F_AUTO_DEMAND_IN → BAJAJ-AUTO → BAJAJHLDNG | +0.50 | director_override | +0.34% |
| 2 | F_FPI_FLOWS → BAJAJFINSV → BAJAJHLDNG | -1.60 | events | -0.29% |
| 2 | F_GOLD → BAJAJFINSV → BAJAJHLDNG | -1.05 | observed | -0.26% |
| 2 | F_CREDIT_SPREADS_IN → BAJAJFINSV → BAJAJHLDNG | +0.50 | events | -0.24% |
| 3 | F_MONSOON → F_UNSECURED_STRESS → BAJAJFINSV → BAJAJHLDNG | -1.56 | events | -0.20% |
| 1 | F_US_EQUITIES → BAJAJHLDNG | +0.23 | observed | +0.19% |
| 2 | P_EV_POLICY → BAJAJ-AUTO → BAJAJHLDNG | +1.10 | events | +0.18% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-12 | Further block purchases of Bajaj Finserv shares via subsidiary/intra-group (April 2026 precedent raised stake to 38.41%) | corporate_action | 0.25 | +0.5% | +0.12% |
| 2027 | Corporate restructuring / holdco simplification that narrows the ~49% NAV discount (speculative; none announced) *(review: [RT_N50_B] RT_N50_B: The profile itself calls it 'speculative; none announced'. At p 0.05 x +25 mid it was the largest company-event item (+1.25).)* | corporate_action | 0.02 | +25.0% | +0.50% |
| 2027-01/02 | Q3 FY27 results (Q2 declared 2026-11-03) | results | 0.95 | +0.0% | +0.00% |

## Analyst profile (agent research, sourced)
# Bajaj Holdings & Investment (BAJAJHLDNG) - Market Impact profile, as of 2026-11-05

## Business
Bajaj Holdings is the listed investment vehicle of the Bajaj group (promoters 51.46%). It owns large stakes in Bajaj Finserv (about 38-39%, raised via an April 2026 block deal to 38.41%), Bajaj Auto and Maharashtra Scooters, plus a smaller portfolio. At 30 June 2026 its investments were worth Rs2.34 lakh cr, or Rs21,062 per share (Sahi, 15 Sep), versus a share price of Rs10,811: a discount to NAV of roughly 49%. Operating revenue (Rs924cr TTM) is only dividends and interest; reported consolidated profit (TTM ~Rs9,440cr, Q2 FY27 owner profit Rs1,993cr, +28% y/y) is mostly equity-accounted share of investee profits and is not what the market capitalises. The stock pays a modest dividend (Rs65 interim declared in September) and trades at 12.9x earnings and 1.6x book. Screener also notes a low effective tax rate and ROE of ~12%.

## What moves the stock, ranked
A holding company has almost no direct commodity exposure, so we used company links for the look-through and a handful of market/discount drivers.
1. **Bajaj Finserv (0.38 per +1% in BFS)** - the single biggest NAV driver. BFS (BAJAJFINSV) carries Bajaj Finance (rates, credit costs, RBI prudential rules) and insurance (IRDAI), so all NBFC/insurance shocks transmit here.
2. **Bajaj Auto (0.30 per +1%)** - two-wheeler/three-wheeler demand, KTM exposure, exports, commodity costs and EV policy; modelled in the BAJAJ-AUTO profile.
3. **Discount drivers**: G-sec yield (-0.8 per +25bp), domestic flows (+1.0), FPI (+1.0), VIX (-0.6), capital-gains tax (-0.6), repo (-0.6).
4. **Proxy edges** with caution: USD/INR (-1.0) and US equities (+0.8), shrunk from the pack's -2.51 and +1.61 estimates because they proxy FPI risk-on/off already counted.
Empirical check: global HRC steel (-1.87, t -2.3) and US equities (+1.61, t +2.1) are the only |t|>=2 coefficients. Steel has no plausible causal link to a financial holdco (Bajaj Auto's steel input cost is at best a small effect already in its own profile), so it is treated as spurious and omitted.

## Transmission examples
- **Middle East escalation -> Brent up -> CPI up -> RBI hikes (repo 5.50% now) -> Bajaj Finance funding cost up and loan growth slows -> BFS profit expectations fall -> BFS share price falls -> BHIL NAV down 0.38 for each 1% -> the holdco discount also widens on risk-off.**
- **Brent up -> INR weaker -> FPI outflows from financials -> BFS and BHIL de-rate together** (the pack's -2.5 USD/INR sensitivity is consistent).
- **Good monsoon -> rural demand -> two-wheeler sales up -> Bajaj Auto earnings up -> NAV up** (+0.30 per 1%), plus rural NBFC credit quality better.
- **RBI prudential tightening on NBFCs -> Bajaj Finance growth caps (as in 2023) -> BFS down -> BHIL down; the discount may widen as governance premium narrows.**
- **Budget 2027 raises capital-gains tax -> holdco monetisation value and flows fall -> discount widens.**

## Current situation
BHIL reported Q2 on 3 Nov: owner profit Rs1,993cr (+28%). Stock is -5.1% over 3 months and -10.6% over 12 months; MarketsMojo downgraded to Sell on 4 Nov (low-quality signal). The investee Bajaj Finserv's large dividend announcement in September (Business Today headline) supports holdco cash flows.

## Upcoming
Q3 results (late Jan/Feb 2027), Union Budget, investee results, potential intra-group share purchases (0.25) and a speculative restructuring (0.05).

## Bull and bear
**Bull:** deep NAV discount (~49%), quality investees, growing look-through earnings, possible discount narrowing. **Bear:** the discount is structural, concentration in two holdings, NBFC regulatory risk, and a rising-rate cycle.

## Sizing notes and caveats
Link weights: if Bajaj Finserv and Bajaj Auto are each roughly a third of the Rs2.34 lakh cr portfolio (Trendlyne/Roic weights, not verified here), a 1% move in either changes NAV by ~0.33%, and the holdco price follows NAV with a stable discount, giving 0.30-0.38 after rounding for the stake in BFS. The Director should avoid adding BHIL's own exposures to rates or consumer demand on top of these links: BAJAJFINSV and BAJAJ-AUTO already carry them, and the remaining direct edges here are only discount and sentiment effects. Stake percentages differ across sources (BFS 38.4-41.6%; Bajaj Auto 33-36% in sources that appear to be portfolio weights, not ownership), so the link weights are deliberately given wide ranges and the confidence is low.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.