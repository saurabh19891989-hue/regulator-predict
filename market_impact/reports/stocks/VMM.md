# VMM — Vishal Mega Mart Ltd.
*MIDCAP_100 · Consumer Services · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +0.7%**, **12 months +2.5%** (rank 74 / 60 of 200 for 3m / 12m); beta 1.11
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +21.9%): 3 months 53%, 12 months 48%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -2.5% … P90 +8.2%; plausible 12m relative-return range incl. stock-specific noise: -43.0% … +21.4%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +0.0 pp (model impact -0.3% beta-adjusted vs realised market-adjusted move -25.6%); forward event exposure +5.4% (3m +2.0%; half assumed priced); company-specific events +1.9%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +3.58 | +3.50 | +0.00 | +0.03 | +0.05 | — |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +3.36 | +2.50 | +0.73 | +0.15 | -0.01 | — |
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | +3.14 | +3.00 | +0.00 | +0.05 | +0.09 | — |
| Indian wage / employee-cost inflation (`F_WAGES_IN`) | +2 pp | +2.72 | +2.00 | +0.92 | -0.10 | -0.10 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -2.21 | +0.00 | -1.65 | -0.25 | -0.32 | — |
| Monsoon rainfall vs normal (`F_MONSOON`) | +10% above long-period average | +2.17 | +0.00 | +1.42 | +0.33 | +0.42 | — |
| Value-fashion and mass-retail competition intensity (`NEW_VALUE_FASHION_COMPETITION`) | +1 = materially sharper expansion/discounting by Reliance Trends/Yousta, Max, Style Union, Myntra, V-Mart | -2.00 | -2.00 | +0.00 | +0.00 | +0.00 | — |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -1.85 | -1.50 | -0.12 | -0.27 | +0.05 | — |
| Brent crude oil price (`F_BRENT`) | +10% Brent | -1.24 | -1.00 | -0.07 | -0.13 | -0.04 | +0.0% |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -1.23 | -1.00 | -0.13 | -0.06 | -0.03 | — |
| Russia-Ukraine war / Western sanctions intensity on Russia (`NEW_RUSSIA_UKRAINE_WAR`) | +1 = escalation (new sanctions round, strikes on energy/port infrastructure); -1 = ceasefire/sanctions relief | -1.22 | +0.00 | -0.78 | -0.32 | -0.11 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -1.07 | +0.00 | -1.11 | +0.20 | -0.16 | — |
| Quick-commerce disruption of retail/FMCG distribution (`T_QUICK_COMMERCE`) | +1 | -1.00 | -1.00 | +0.00 | +0.00 | +0.00 | — |
| ENSO state (El Nino strength) (`NEW_EL_NINO`) | +1 = El Nino year (ONI >= +1.0 sustained); -1 = La Nina | -0.92 | +0.00 | +0.00 | -0.77 | -0.15 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -6.9% | -6.9% | -5.8 | -0.2 | -0.7 | -0.2 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -3.0% | -3.0% | -1.7 | -1.4 | +0.3 | -0.2 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -2.7% | -2.7% | +0.0 | -1.8 | -0.4 | -0.5 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.36 | -3.9% | -1.4% | -2.5 | -0.7 | -0.5 | -0.1 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.58 | +2.3% | +1.4% | +2.0 | +0.1 | +0.2 | +0.1 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -1.3% | -1.3% | -1.0 | -0.1 | -0.1 | -0.1 |
| IMD April 2027 long-range forecast says normal or above-normal monsoon (>=96% LPA) (`EV_MONSOON27_FIRST_FORECAST_NORMAL`) | scheduled | 0.68 | +1.4% | +1.0% | +0.3 | +0.8 | +0.1 | +0.2 |
| Kharif 2026 output hit: paddy area down, foodgrain target cut, rice output seen sharpest fall in ~2 decades (`EV_KHARIF26_OUTPUT_HIT`) | occurred | 1.00 | -0.9% | -0.9% | -0.8 | -0.1 | -0.1 | +0.0 |
| India Q1 FY27 GDP grows 7.8% (31 Aug 2026), beating ~7.3% consensus (`EV_GDP_Q1FY27_7_8`) | occurred | 1.00 | +0.9% | +0.9% | +0.7 | +0.1 | +0.1 | -0.0 |
| India 2027 wheat crop (harvest Mar-Apr 2027) below 2026's record ~120 MT (`EV_WHEAT27_CROP_BELOW`) | anticipated | 0.65 | -1.3% | -0.9% | -1.2 | +0.0 | -0.1 | -0.0 |
| Rural demand indicators mixed: tractor volumes dip in Oct, 2W festive sales firm, rural CPI above urban, rural jobs scheme person-days down (`EV_RURAL_DEMAND_SOFT26`) | occurred | 1.00 | -0.8% | -0.8% | -0.9 | +0.0 | +0.1 | +0.0 |
| Food inflation overshoot: Dec-Feb CPI food >9% y/y on pulses, vegetables, edible oils, milk (`EV_PULSES_VEG_SPIKE_WINTER`) | risk_scenario | 0.25 | -3.0% | -0.7% | -1.8 | -1.3 | +0.2 | -0.2 |

## Strongest causal chains (1st–4th order)
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → VMM | -4.95% | -4.95% |
| 1 | EV_CPI_REACCEL_SEP26 ⇒ F_FOOD_INFLATION_IN → VMM | -1.65% | -1.65% |
| 2 | EV_CPI_REACCEL_SEP26 ⇒ F_CPI_IN → F_REPO_IN → VMM | -1.32% | -1.32% |
| 1 | EV_RBI_OCT26_HIKE25 ⇒ F_REPO_IN → VMM | -1.00% | -1.00% |
| 1 | EV_RURAL_DEMAND_SOFT26 ⇒ F_RURAL_DEMAND → VMM | -0.90% | -0.90% |
| 1 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_REFINING_MARGIN → VMM | -0.90% | -0.90% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → VMM | -2.50% | -0.89% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → VMM | +1.50% | +0.87% |
| 2 | EV_SWMONSOON26_DEFICIT ⇒ F_MONSOON → F_RURAL_DEMAND → VMM | -0.86% | -0.86% |
| 2 | EV_SWMONSOON26_DEFICIT ⇒ F_MONSOON → F_FOOD_INFLATION_IN → VMM | -0.81% | -0.81% |
| 1 | EV_KHARIF26_OUTPUT_HIT ⇒ F_FOOD_INFLATION_IN → VMM | -0.75% | -0.75% |
| 2 | EV_CPI_REACCEL_SEP26 ⇒ F_CPI_IN → F_WAGES_IN → VMM | +0.74% | +0.74% |
| 1 | EV_GDP_Q1FY27_7_8 ⇒ F_URBAN_DEMAND → VMM | +0.70% | +0.70% |
| 2 | EV_CPI_REACCEL_SEP26 ⇒ F_CPI_IN → F_URBAN_DEMAND → VMM | -0.64% | -0.64% |
| 1 | EV_BUDGET27_AGRI_RURAL ⇒ F_RURAL_DEMAND → VMM | +0.90% | +0.63% |

## Analyst profile (agent research, sourced)
# VMM (Vishal Mega Mart Ltd.) - company profile as of 2026-11-05

## Business
Vishal Mega Mart is a value-retail chain of about 844 stores selling apparel, general merchandise and FMCG, mostly to middle- and lower-income households in tier-2/3 cities. TTM sales are Rs 13,910 cr (+18%) with EBITDA of Rs 1,987 cr (14.3%) and profit Rs 897 cr. The September 2026 quarter showed sales of Rs 3,399 cr (+14%), an operating margin of 12% (13% a year ago) and profit of Rs 158 cr (+4%), below estimates; management attributed the weakness to a festive shift into the December quarter. The stock is Rs 94, -34% in 12 months, at a 52-week low (screener.in pack, 2026-11-05).

## What moves the stock (ranked)
1. **Same-store sales growth and the festive calendar.** The Q2 miss is partly timing; Q3 (Oct-Dec) should recover.
2. **Mass-market consumer income and inflation.** Brent has a significant empirical beta of -1.47 (t=-2.8), consistent with fuel/LPG budgets of its customers and logistics costs.
3. **Competition from Trent's Zudio, DMart, Reliance and online value fashion.**
4. **Overhang.** Promoters (PE-backed) and FIIs are sellers; DIIs hold 36.5%.
5. **Rates and valuation.** 49x P/E.

## Transmission examples
- **Middle East escalation -> Brent up -> petrol/LPG/transport costs -> low-income household budgets squeezed -> VMM discretionary basket weakens.** Order 2: CPI up; order 3: RBI holds; order 4: SSSG down. Brent has risen 15% in three months and 50% in twelve.
- **Brent up -> logistics and plastics cost up -> gross margin down** (about -1% of EBITDA per 10%).
- **Good monsoon -> rural income -> tier-3 footfalls -> apparel and home volumes.**
- **GST cut -> lower shelf price -> volume uplift** for apparel and FMCG.
- **Zudio expansion -> competition for same households -> VMM discounting.**

## Current situation
Q2 below estimates; brokerages stayed positive but cut targets (Business Today, Livemint 2026-10-22). The festive shift is expected to reverse in Q3.

## Upcoming events
Q3 FY27 (January 2027), possible promoter block sale, store additions.

## Bull case
Festive recovery, SSSG back to 8-10%, margin to 14.5%; stock rerates to 60x on 25% EPS growth.

## Bear case
SSSG weak, competitors intensify, further selling: 30x multiple, -30%.

## Uncertainties
Revenue mix, store geography and ownership details are model estimates; filings not fetched; headline text only.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.