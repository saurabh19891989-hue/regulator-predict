# TATACONSUM — Tata Consumer Products Ltd.
*NIFTY_50 · Fast Moving Consumer Goods · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +0.8%**, **12 months +2.2%** (rank 73 / 66 of 200 for 3m / 12m); beta 0.87
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +15.9%): 3 months 54%, 12 months 42%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -2.1% … P90 +7.8%; plausible 12m relative-return range incl. stock-specific noise: -15.4% … +22.3%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +0.3 pp (model impact +0.6% beta-adjusted vs realised market-adjusted move -9.7%); forward event exposure +5.3% (3m +2.0%; half assumed priced); company-specific events +0.8%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Cocoa, coffee, tea prices (`F_COCOA_COFFEE_TEA`) | +15% beverage commodities | -3.30 | -3.30 | +0.00 | +0.00 | +0.00 | — |
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +2.29 | +2.30 | +0.00 | +0.00 | -0.01 | — |
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | +1.72 | +1.70 | +0.00 | +0.00 | +0.02 | — |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +1.56 | +1.00 | +0.46 | +0.06 | +0.04 | — |
| ENSO state (El Nino strength) (`NEW_EL_NINO`) | +1 = El Nino year (ONI >= +1.0 sustained); -1 = La Nina | -1.26 | +0.00 | -0.79 | -0.40 | -0.07 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -1.16 | +0.00 | -0.71 | -0.34 | -0.11 | — |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -1.16 | -0.80 | -0.07 | -0.19 | -0.09 | — |
| Monsoon rainfall vs normal (`F_MONSOON`) | +10% above long-period average | +1.13 | +0.00 | +0.73 | +0.16 | +0.24 | — |
| Consumer premiumisation (`T_PREMIUMISATION`) | +1 | +1.09 | +1.00 | +0.09 | +0.00 | +0.00 | — |
| India 10-year G-sec yield (`F_GSEC_10Y_IN`) | +25 bp yield | -1.00 | -1.00 | +0.00 | +0.00 | +0.00 | — |
| Indian wage / employee-cost inflation (`F_WAGES_IN`) | +2 pp | +0.98 | +0.00 | +1.14 | -0.08 | -0.09 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -0.89 | +0.00 | -0.34 | -0.20 | -0.35 | — |
| Packaging cost (paper, plastics) (`F_PACKAGING`) | +10% packaging cost | -0.80 | -0.80 | +0.00 | +0.00 | +0.00 | — |
| Quick-commerce disruption of retail/FMCG distribution (`T_QUICK_COMMERCE`) | +1 | +0.80 | +0.80 | +0.00 | +0.00 | +0.00 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -3.7% | -3.7% | -2.5 | -0.0 | -0.6 | -0.6 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -2.3% | -2.3% | -0.9 | -0.9 | -0.4 | -0.1 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -1.4% | -1.4% | -1.4 | +0.0 | -0.0 | -0.0 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -1.4% | -1.4% | +0.0 | -0.9 | -0.2 | -0.3 |
| US Q3 data: GDP 3.4%, CPI 3.7%, September payrolls only +29k (`EV_US_Q3_DATA_MIXED`) | occurred | 1.00 | -0.9% | -0.9% | +0.0 | -0.4 | -0.5 | -0.0 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.28 | +3.1% | +0.9% | +3.2 | -0.1 | -0.1 | +0.1 |
| US recession (two negative quarters or NBER-style) beginning by mid-2027 (`EV_US_RECESSION_RISK_2027`) | risk_scenario | 0.25 | +3.0% | +0.7% | +0.0 | +2.1 | +0.6 | +0.3 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -0.7% | -0.7% | +0.0 | -0.5 | -0.2 | -0.0 |
| Disorderly yen carry-trade unwind (Aug-2024-style) after BoJ/MoF action (`EV_YEN_CARRY_UNWIND_RISK`) | risk_scenario | 0.18 | +3.6% | +0.6% | +4.0 | -0.1 | -0.3 | +0.0 |
| Gold and silver slump from January 2026 peaks (silver -53%, gold -24%) (`EV_PRECIOUS_METALS_CRASH_2026`) | occurred | 1.00 | -0.6% | -0.6% | +0.0 | -0.5 | -0.1 | -0.0 |
| Kharif 2026 output hit: paddy area down, foodgrain target cut, rice output seen sharpest fall in ~2 decades (`EV_KHARIF26_OUTPUT_HIT`) | occurred | 1.00 | -0.6% | -0.6% | -0.4 | -0.0 | -0.1 | -0.0 |
| Food inflation overshoot: Dec-Feb CPI food >9% y/y on pulses, vegetables, edible oils, milk (`EV_PULSES_VEG_SPIKE_WINTER`) | risk_scenario | 0.25 | -2.2% | -0.6% | -1.0 | -0.8 | -0.3 | -0.1 |

## Strongest causal chains (1st–4th order)
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → TATACONSUM | -2.48% | -2.48% |
| 1 | EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26 ⇒ F_GSEC_10Y_IN → TATACONSUM | -1.40% | -1.40% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → TATACONSUM | +3.20% | +0.90% |
| 1 | EV_CPI_REACCEL_SEP26 ⇒ F_FOOD_INFLATION_IN → TATACONSUM | -0.88% | -0.88% |
| 1 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → TATACONSUM | +4.00% | +0.72% |
| 3 | EV_CPI_REACCEL_SEP26 ⇒ F_CPI_IN → F_REPO_IN → F_GSEC_10Y_IN → TATACONSUM | -0.52% | -0.52% |
| 1 | EV_RURAL_DEMAND_SOFT26 ⇒ F_RURAL_DEMAND → TATACONSUM | -0.51% | -0.51% |
| 2 | EV_SWMONSOON26_DEFICIT ⇒ F_MONSOON → F_RURAL_DEMAND → TATACONSUM | -0.49% | -0.49% |
| 1 | EV_GDP_Q1FY27_7_8 ⇒ F_URBAN_DEMAND → TATACONSUM | +0.46% | +0.46% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → TATACONSUM | -1.25% | -0.45% |
| 2 | EV_UST_SELLOFF_SEP26 ⇒ F_US_10Y → F_GSEC_10Y_IN → TATACONSUM | -0.44% | -0.44% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → TATACONSUM | +0.75% | +0.44% |
| 2 | EV_SWMONSOON26_DEFICIT ⇒ F_MONSOON → F_FOOD_INFLATION_IN → TATACONSUM | -0.43% | -0.43% |
| 2 | EV_CPI_REACCEL_SEP26 ⇒ F_CPI_IN → F_URBAN_DEMAND → TATACONSUM | -0.42% | -0.42% |
| 1 | EV_KHARIF26_OUTPUT_HIT ⇒ F_FOOD_INFLATION_IN → TATACONSUM | -0.40% | -0.40% |

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