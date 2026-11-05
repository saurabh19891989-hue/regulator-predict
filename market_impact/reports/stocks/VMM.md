# VMM — Vishal Mega Mart Ltd.
*MIDCAP_100 · Consumer Services · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +0.7%**, **12 months +2.2%** (rank 27 / 14 of 200 for 3m / 12m); beta 1.11
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +21.9%): 3 months 53%, 12 months 57%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -0.4% … P90 +6.2%; plausible 12m relative-return range incl. stock-specific noise: -26.2% … +32.1%
- Decomposition (12m): 0.5 × forward event exposure +3.0% (3m +0.8%; half assumed priced; market-priced macro drift removed) + 0.5 × company-specific catalysts +1.9%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply +0.0% (beta-adjusted) vs a realised market-adjusted move of -25.6% — gap +25.6 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +3.66 | +3.50 | +0.00 | +0.10 | +0.06 | — |
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | +3.31 | +3.00 | +0.00 | +0.16 | +0.14 | — |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +3.30 | +2.50 | +0.73 | +0.07 | +0.00 | — |
| Indian wage / employee-cost inflation (`F_WAGES_IN`) | +2 pp | +2.83 | +2.00 | +0.92 | -0.06 | -0.04 | — |
| Monsoon rainfall vs normal (`F_MONSOON`) | +10% above long-period average | +2.03 | +0.00 | +1.42 | +0.38 | +0.23 | — |
| Value-fashion and mass-retail competition intensity (`NEW_VALUE_FASHION_COMPETITION`) | +1 = materially sharper expansion/discounting by Reliance Trends/Yousta, Max, Style Union, Myntra, V-Mart | -2.00 | -2.00 | +0.00 | +0.00 | +0.00 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -1.93 | +0.00 | -1.65 | -0.16 | -0.12 | — |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -1.69 | -1.50 | -0.12 | -0.15 | +0.08 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -1.23 | -1.00 | -0.13 | -0.06 | -0.03 | — |
| Brent crude oil price (`F_BRENT`) | +10% Brent | -1.18 | -1.00 | -0.06 | -0.10 | -0.02 | +0.0% |
| Russia-Ukraine war / Western sanctions intensity on Russia (`NEW_RUSSIA_UKRAINE_WAR`) | +1 = escalation (new sanctions round, strikes on energy/port infrastructure); -1 = ceasefire/sanctions relief | -1.04 | +0.00 | -0.78 | -0.23 | -0.03 | — |
| India real GDP growth (`F_GDP_IN`) | +1 pp | +1.03 | +0.00 | +0.54 | +0.47 | +0.01 | — |
| Quick-commerce disruption of retail/FMCG distribution (`T_QUICK_COMMERCE`) | +1 | -1.00 | -1.00 | +0.00 | +0.00 | +0.00 | — |
| ENSO state (El Nino strength) (`NEW_EL_NINO`) | +1 = El Nino year (ONI >= +1.0 sustained); -1 = La Nina | -0.93 | +0.00 | +0.00 | -0.77 | -0.16 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -2.6% | -2.6% | +0.0 | -1.8 | -0.5 | -0.3 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -2.3% | -2.3% | -1.7 | -0.7 | +0.2 | -0.1 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -1.3% | -1.3% | -1.0 | -0.1 | -0.1 | -0.0 |
| India Q1 FY27 GDP grows 7.8% (31 Aug 2026), beating ~7.3% consensus (`EV_GDP_Q1FY27_7_8`) | occurred | 1.00 | +1.1% | +1.1% | +0.7 | +0.3 | +0.1 | -0.0 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.55 | +1.9% | +1.0% | +1.7 | +0.0 | +0.1 | +0.0 |
| IMD April 2027 long-range forecast says normal or above-normal monsoon (>=96% LPA) (`EV_MONSOON27_FIRST_FORECAST_NORMAL`) | scheduled | 0.68 | +1.5% | +1.0% | +0.3 | +0.8 | +0.2 | +0.1 |
| Rural demand indicators mixed: tractor volumes dip in Oct, 2W festive sales firm, rural CPI above urban, rural jobs scheme person-days down (`EV_RURAL_DEMAND_SOFT26`) | occurred | 1.00 | -0.9% | -0.9% | -0.9 | +0.0 | +0.0 | +0.0 |
| India 2027 wheat crop (harvest Mar-Apr 2027) below 2026's record ~120 MT (`EV_WHEAT27_CROP_BELOW`) | anticipated | 0.65 | -1.3% | -0.8% | -1.2 | +0.0 | -0.1 | -0.0 |
| Kharif 2026 output hit: paddy area down, foodgrain target cut, rice output seen sharpest fall in ~2 decades (`EV_KHARIF26_OUTPUT_HIT`) | occurred | 1.00 | -0.8% | -0.8% | -0.8 | -0.1 | -0.1 | +0.0 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.25 | -3.3% | -0.8% | -2.2 | -0.7 | -0.3 | -0.1 |
| North-east monsoon 2026 normal or above-normal (relief for southern reservoirs) (`EV_NEMONSOON26_NORMAL_UP`) | anticipated | 0.85 | +0.9% | +0.8% | +0.3 | +0.4 | +0.1 | +0.1 |
| Union Budget FY28 (1 Feb 2027) raises agri/rural spending and fertiliser subsidy; PM-Kisan/rural jobs top-up (`EV_BUDGET27_AGRI_RURAL`) | scheduled | 0.70 | +1.0% | +0.7% | +0.9 | +0.0 | +0.0 | +0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → VMM | +1.30% | +0.72% |
| 1 | EV_BUDGET27_AGRI_RURAL ⇒ F_RURAL_DEMAND → VMM | +0.90% | +0.63% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → VMM | -2.20% | -0.55% |
| 1 | EV_RURAL_RELIEF_PACKAGE ⇒ F_RURAL_DEMAND → VMM | +0.90% | +0.49% |
| 1 | EV_LABOUR_CODES_RULES ⇒ F_WAGES_IN → VMM | +0.60% | +0.48% |
| 2 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_RURAL_DEMAND → VMM | +0.68% | +0.46% |
| 1 | EV_PULSES_VEG_SPIKE_WINTER ⇒ F_FOOD_INFLATION_IN → VMM | -1.80% | -0.45% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → VMM | -1.00% | -0.42% |
| 1 | EV_STATE_POLLS_FEB_MAR27 ⇒ F_RURAL_DEMAND → VMM | +0.60% | +0.41% |
| 1 | EV_WHEAT27_CROP_BELOW ⇒ F_FOOD_INFLATION_IN → VMM | -0.60% | -0.39% |
| 1 | EV_WHEAT27_CROP_BELOW ⇒ F_RURAL_DEMAND → VMM | -0.60% | -0.39% |
| 2 | EV_NEMONSOON26_NORMAL_UP ⇒ F_MONSOON → F_RURAL_DEMAND → VMM | +0.34% | +0.29% |
| 1 | EV_INDIA_STAGFLATION_SCARE ⇒ F_RURAL_DEMAND → VMM | -2.40% | -0.29% |
| 1 | EV_RBI_FEB27_HIKE25 ⇒ F_REPO_IN → VMM | -1.00% | -0.27% |
| 1 | EV_NEMONSOON26_NORMAL_UP ⇒ F_FOOD_INFLATION_IN → VMM | +0.30% | +0.26% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_FOOD_INFLATION_IN → VMM | +2.00 | events | -3.00% |
| 1 | F_REPO_IN → VMM | +1.00 | events | -1.00% |
| 1 | F_RURAL_DEMAND → VMM | -0.25 | events | -0.75% |
| 1 | F_URBAN_DEMAND → VMM | +0.20 | events | +0.70% |
| 1 | F_REFINING_MARGIN → VMM | +0.60 | events | -0.36% |
| 1 | F_COTTON → VMM | +0.19 | observed | -0.08% |
| 1 | F_USDINR → VMM | -0.37 | observed | +0.07% |
| 1 | F_BRENT → VMM | +0.00 | observed | -0.00% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-12 | Promoter/PE block sale or share overhang (promoters 40.12% -> 40.02%, FIIs selling) | corporate_action | 0.30 | -3.0% | -0.90% |
| 2027-01 | Q3 FY27 results: festive shift reverses (Diwali 2026-11-08, model knowledge) so SSSG and margin should rebound | results | 0.95 | +2.0% | +1.90% |
| 2027-03 | Store additions toward FY27 target (currently ~844 stores) | capex | 0.90 | +1.0% | +0.90% |

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