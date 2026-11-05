# TATACONSUM — Tata Consumer Products Ltd.
*NIFTY_50 · Fast Moving Consumer Goods · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +0.2%**, **12 months +0.2%** (rank 74 / 80 of 200 for 3m / 12m); beta 0.87
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +15.9%): 3 months 51%, 12 months 54%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -2.3% … P90 +4.0%; plausible 12m relative-return range incl. stock-specific noise: -19.6% … +19.4%
- Decomposition (12m): 0.5 × forward event exposure -0.1% (3m -0.2%; half assumed priced; market-priced macro drift removed) + 0.5 × company-specific catalysts +0.8%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply +0.7% (beta-adjusted) vs a realised market-adjusted move of -9.7% — gap +10.4 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## Where the expected return comes from
Market-priced macro drivers (rates, FX, commodities, indices, volatility, flows, growth, inflation) are taken as priced, so what is left is policy, regulatory, sector, theme, geopolitical and company-specific exposure — where 2nd–4th-order effects are most likely to be missed. Percentage points of the expected relative return.
| source | 12m: 1st order | 12m: 2nd–4th order | 12m total | 3m total |
|---|---|---|---|---|
| Policy | +0.03 | +0.01 | +0.04 | -0.02 |
| Sector | +0.24 | +0.21 | +0.46 | +0.18 |
| Theme | -0.02 | -0.02 | -0.04 | -0.02 |
| Geopolitics | +0.00 | +0.01 | +0.01 | +0.01 |
| Company catalysts | +0.39 | +0.00 | +0.39 | +0.39 |
| Market-priced macro | +0.00 | +0.00 | +0.00 | -0.00 |
| Beta adjustment | — | — | -0.50 | -0.22 |
| Universe centring | — | — | -0.15 | -0.10 |
| **Expected relative return** | | | **+0.21** | **+0.21** |

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Cocoa, coffee, tea prices (`F_COCOA_COFFEE_TEA`) | +15% beverage commodities | -3.30 | -3.30 | +0.00 | +0.00 | +0.00 | — |
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +2.32 | +2.30 | +0.00 | +0.00 | +0.02 | — |
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | +1.78 | +1.70 | +0.00 | +0.00 | +0.08 | — |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +1.53 | +1.00 | +0.46 | +0.06 | +0.00 | — |
| ENSO state (El Nino strength) (`NEW_EL_NINO`) | +1 = El Nino year (ONI >= +1.0 sustained); -1 = La Nina | -1.24 | +0.00 | -0.79 | -0.40 | -0.05 | — |
| Consumer premiumisation (`T_PREMIUMISATION`) | +1 | +1.09 | +1.00 | +0.09 | +0.00 | +0.00 | — |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -1.07 | -0.80 | -0.07 | -0.19 | -0.01 | — |
| Monsoon rainfall vs normal (`F_MONSOON`) | +10% above long-period average | +1.06 | +0.00 | +0.73 | +0.13 | +0.20 | — |
| Indian wage / employee-cost inflation (`F_WAGES_IN`) | +2 pp | +1.02 | +0.00 | +1.14 | -0.08 | -0.05 | — |
| India 10-year G-sec yield (`F_GSEC_10Y_IN`) | +25 bp yield | -1.00 | -1.00 | +0.00 | +0.00 | +0.00 | — |
| Packaging cost (paper, plastics) (`F_PACKAGING`) | +10% packaging cost | -0.80 | -0.80 | +0.00 | +0.00 | +0.00 | — |
| Quick-commerce disruption of retail/FMCG distribution (`T_QUICK_COMMERCE`) | +1 | +0.80 | +0.80 | +0.00 | +0.00 | +0.00 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -0.79 | +0.00 | -0.71 | -0.04 | -0.05 | — |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | +0.73 | +0.80 | -0.03 | -0.03 | -0.01 | +3.5% |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -1.9% | -1.9% | -0.9 | -0.9 | -0.0 | -0.1 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -1.4% | -1.4% | -1.4 | +0.0 | -0.0 | -0.0 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -1.3% | -1.3% | +0.0 | -0.9 | -0.2 | -0.3 |
| Kharif 2026 output hit: paddy area down, foodgrain target cut, rice output seen sharpest fall in ~2 decades (`EV_KHARIF26_OUTPUT_HIT`) | occurred | 1.00 | -0.5% | -0.5% | -0.4 | -0.0 | -0.1 | -0.0 |
| India Q1 FY27 GDP grows 7.8% (31 Aug 2026), beating ~7.3% consensus (`EV_GDP_Q1FY27_7_8`) | occurred | 1.00 | +0.5% | +0.5% | +0.5 | +0.0 | +0.1 | -0.0 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -0.5% | -0.5% | -0.3 | -0.1 | -0.1 | +0.0 |
| IMD April 2027 long-range forecast says normal or above-normal monsoon (>=96% LPA) (`EV_MONSOON27_FIRST_FORECAST_NORMAL`) | scheduled | 0.68 | +0.8% | +0.5% | +0.2 | +0.4 | +0.1 | +0.1 |
| Rural demand indicators mixed: tractor volumes dip in Oct, 2W festive sales firm, rural CPI above urban, rural jobs scheme person-days down (`EV_RURAL_DEMAND_SOFT26`) | occurred | 1.00 | -0.5% | -0.5% | -0.5 | +0.0 | +0.0 | -0.0 |
| US Q3 data: GDP 3.4%, CPI 3.7%, September payrolls only +29k (`EV_US_Q3_DATA_MIXED`) | occurred | 1.00 | -0.5% | -0.5% | +0.0 | -0.4 | -0.2 | +0.0 |
| India 2027 wheat crop (harvest Mar-Apr 2027) below 2026's record ~120 MT (`EV_WHEAT27_CROP_BELOW`) | anticipated | 0.65 | -0.8% | -0.5% | -0.7 | +0.0 | -0.1 | -0.0 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -0.5% | -0.5% | +0.0 | -0.3 | -0.2 | +0.0 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.25 | +1.9% | +0.5% | +2.0 | -0.1 | -0.0 | +0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → TATACONSUM | +2.00% | +0.50% |
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → TATACONSUM | -0.80% | -0.40% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → TATACONSUM | +0.65% | +0.36% |
| 1 | EV_BUDGET27_AGRI_RURAL ⇒ F_RURAL_DEMAND → TATACONSUM | +0.51% | +0.36% |
| 1 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → TATACONSUM | +2.00% | +0.30% |
| 1 | EV_RURAL_RELIEF_PACKAGE ⇒ F_RURAL_DEMAND → TATACONSUM | +0.51% | +0.28% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → TATACONSUM | -1.10% | -0.28% |
| 2 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_RURAL_DEMAND → TATACONSUM | +0.39% | +0.26% |
| 1 | EV_PULSES_VEG_SPIKE_WINTER ⇒ F_FOOD_INFLATION_IN → TATACONSUM | -0.96% | -0.24% |
| 1 | EV_STATE_POLLS_FEB_MAR27 ⇒ F_RURAL_DEMAND → TATACONSUM | +0.34% | +0.23% |
| 1 | EV_WHEAT27_CROP_BELOW ⇒ F_RURAL_DEMAND → TATACONSUM | -0.34% | -0.22% |
| 1 | EV_WHEAT27_CROP_BELOW ⇒ F_FOOD_INFLATION_IN → TATACONSUM | -0.32% | -0.21% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_RISK_SENTIMENT → TATACONSUM | +0.80% | +0.20% |
| 1 | EV_NVDA_NOV17_BEAT ⇒ F_RISK_SENTIMENT → TATACONSUM | -0.32% | -0.20% |
| 1 | EV_FERT_SUBSIDY_TOPUP_WINTER ⇒ F_GSEC_10Y_IN → TATACONSUM | -0.20% | -0.18% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_FOOD_INFLATION_IN → TATACONSUM | +2.00 | events | -1.60% |
| 1 | F_GSEC_10Y_IN → TATACONSUM | +1.55 | director_override | -1.55% |
| 1 | F_URBAN_DEMAND → TATACONSUM | +0.20 | events | +0.46% |
| 1 | F_RURAL_DEMAND → TATACONSUM | -0.25 | events | -0.43% |
| 1 | F_USDINR → TATACONSUM | -0.37 | observed | +0.18% |
| 1 | F_RISK_SENTIMENT → TATACONSUM | +0.11 | observed | +0.09% |
| 3 | P_ANTI_DUMPING_IN → F_CHEM_FEEDSTOCK → F_PACKAGING → TATACONSUM | +0.40 | events | -0.01% |
| 3 | F_CHINA_GDP → F_PETROCHEM_SPREADS → F_PACKAGING → TATACONSUM | +0.30 | events | -0.01% |
| 4 | F_USDCNY → F_CHINA_CHEM_EXPORTS → F_PETROCHEM_SPREADS → F_PACKAGING → TATACONSUM | -0.47 | observed | -0.00% |
| 4 | P_ANTI_DUMPING_IN → F_CHINA_CHEM_EXPORTS → F_PETROCHEM_SPREADS → F_PACKAGING → TATACONSUM | +0.40 | events | -0.00% |
| 4 | F_CHINA_GDP → F_CHINA_CHEM_EXPORTS → F_PETROCHEM_SPREADS → F_PACKAGING → TATACONSUM | +0.30 | events | -0.00% |
| 4 | C_US_CHINA_DECOUPLING → F_CHINA_CHEM_EXPORTS → F_PETROCHEM_SPREADS → F_PACKAGING → TATACONSUM | -0.10 | events | -0.00% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-11/12 | Additional price increases / tea cost trajectory (Q2 call: price hikes support H2) | guidance | 0.60 | +0.5% | +0.30% |
| 2027-01 | Q3 FY27 results (Q2 on 2026-10-26) | results | 0.95 | +0.5% | +0.47% |
| 2027-05 | Q4 FY27 results and FY28 outlook | results | 0.95 | +0.0% | +0.00% |

## Analyst profile (agent research, sourced)
# Tata Consumer Products (TATACONSUM) - Market Impact profile, as of 2026-11-05

## Business
Tata Consumer is a food-and-beverage group built around tea (Tata Tea, Tetley), coffee, salt (Tata Salt), the Sampann range of pulses and spices, ready-to-drink drinks, and the acquired Capital Foods and Organic India brands, with an international tea/coffee business and a 50:50 Starbucks JV in India (portfolio from model knowledge; segment shares are approximate). In Q2 FY27 revenue rose 14% to Rs5,661cr and EBITDA 18% to Rs794cr (margin 14.0%, +40bp); PAT was about Rs470cr (+16%). India tea/coffee revenue was Rs1,244cr (-1%) on flat volumes; "growth businesses" grew 40%, with Sampann +57% and RTD +47%. Screener shows a P/E of 62, P/B of 4.8 and a low ROE of 7.4%, so the stock is priced for sustained mid-teens growth and margin recovery.

## What moves the stock, ranked
1. **Tea/coffee/cocoa cost (-3.3 per +15%)** - the key margin lever and the reason price hikes matter.
2. **Urban demand (+2.3)** and **rural demand (+1.7)**: premium growth businesses are urban, core tea/salt are rural.
3. **G-sec yield (-1.0)** (valuation duration), **premiumisation (+1.0)**, **GST cuts (+1.0)**, **VIX (+0.8, defensive)**, **packaging (-0.8)**, **food inflation (-0.8)**, **quick commerce (+0.8)**, **FX (-0.5)**, **Brent (-0.5)**.
Empirical check: the only |t|>=2 coefficient is F_RISK_SENTIMENT (+0.88, t +2.8) - consistent with FMCG's defensive character, so it is retained. Copper, US equities and metals coefficients are insignificant and lack a causal link.

## Transmission examples
- **Middle East escalation -> Brent up -> freight, fuel, polymer packaging up -> input cost up -> EBITDA margin down; and Brent up -> INR weaker -> imported coffee/cocoa dearer while UK/US earnings translate higher (net small).**
- **Brent up -> CPI up (Sep CPI 5.54%, food 7.74%) -> RBI keeps hiking (repo 5.50%) -> G-sec yield up -> a 62x P/E stock de-rates; and household squeeze trims urban premium demand.**
- **Poor tea-crop (weather) in Assam/Kenya -> auction prices up -> Tata Consumer takes price hikes -> volumes soften -> margin recovery delayed -> estimates cut.**
- **Good monsoon -> rural incomes up -> salt, tea and staples volumes up -> operating leverage -> margin up.**
- **GST cut on packaged foods -> shelf price down -> volumes up in Sampann and snacks.**

## Current situation
After Q2 the stock jumped 6-7%, then drifted; +10.4% over a month but -8.6% over 12m. Motilal Oswal (Buy, TP Rs1,230) and Citi/Morgan Stanley were constructive. The debate is whether price hikes can offset higher tea and salt costs while core India beverage volumes stay flat.

## Upcoming
Q3 results (late Jan 2027), further price actions, tea/coffee cost trends, RBI December MPC.

## Bull and bear
**Bull:** growth businesses +40%, margin recovery, defensive earnings. **Bear:** 62x P/E, weak core tea volumes, cost inflation, low ROE.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.