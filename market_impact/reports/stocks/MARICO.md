# MARICO — Marico Ltd.
*MIDCAP_100 · Fast Moving Consumer Goods · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +0.1%**, **12 months +0.1%** (rank 91 / 90 of 200 for 3m / 12m); beta 0.72
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +16.0%): 3 months 50%, 12 months 51%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -1.0% … P90 +1.4%; plausible 12m relative-return range incl. stock-specific noise: -20.5% … +19.7%
- Decomposition (12m): 0.5 × forward event exposure +0.1% (3m -0.1%; half assumed priced; market-priced macro drift removed) + 0.5 × company-specific catalysts +0.5%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply -0.2% (beta-adjusted) vs a realised market-adjusted move of +6.9% — gap -7.1 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## Where the expected return comes from
Market-priced macro drivers (rates, FX, commodities, indices, volatility, flows, growth, inflation) are taken as priced, so what is left is policy, regulatory, sector, theme, geopolitical and company-specific exposure — where 2nd–4th-order effects are most likely to be missed. Percentage points of the expected relative return.
| source | 12m: 1st order | 12m: 2nd–4th order | 12m total | 3m total |
|---|---|---|---|---|
| Policy | +0.00 | +0.01 | +0.01 | -0.01 |
| Sector | +0.29 | +0.19 | +0.48 | +0.19 |
| Theme | +0.00 | -0.02 | -0.02 | -0.02 |
| Geopolitics | +0.00 | -0.01 | -0.01 | -0.01 |
| Company catalysts | +0.23 | +0.00 | +0.23 | +0.23 |
| Market-priced macro | +0.00 | +0.00 | +0.00 | +0.00 |
| Beta adjustment | — | — | -0.41 | -0.19 |
| Universe centring | — | — | -0.15 | -0.10 |
| **Expected relative return** | | | **+0.12** | **+0.09** |

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Copra / coconut oil price (`NEW_COPRA_COCONUT_OIL`) | +15% copra price | -3.80 | -3.80 | +0.00 | +0.00 | +0.00 | — |
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | +1.98 | +2.00 | +0.00 | -0.02 | +0.01 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -1.28 | -1.20 | -0.06 | -0.01 | +0.00 | — |
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +1.21 | +1.20 | +0.00 | -0.02 | +0.02 | — |
| Palm / edible oil price (`F_EDIBLE_OIL`) | +10% edible oils | -1.16 | -1.10 | +0.00 | -0.01 | -0.04 | +1.9% |
| Consumer premiumisation (`T_PREMIUMISATION`) | +1 | +1.05 | +1.00 | +0.05 | +0.00 | +0.00 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -0.85 | +0.00 | -0.48 | -0.16 | -0.22 | — |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +0.81 | +0.00 | +0.66 | +0.21 | -0.06 | — |
| Packaging cost (paper, plastics) (`F_PACKAGING`) | +10% packaging cost | -0.80 | -0.80 | +0.00 | +0.00 | +0.00 | — |
| Monsoon rainfall vs normal (`F_MONSOON`) | +10% above long-period average | +0.79 | +0.00 | +0.45 | +0.08 | +0.26 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +0.79 | +0.80 | -0.04 | +0.02 | +0.01 | — |
| Indian wage / employee-cost inflation (`F_WAGES_IN`) | +2 pp | +0.77 | +0.00 | +0.86 | -0.08 | -0.01 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -0.65 | +0.00 | -0.80 | +0.16 | +0.00 | — |
| Brent crude oil price (`F_BRENT`) | +10% Brent | -0.61 | -0.40 | -0.07 | -0.15 | +0.01 | +0.0% |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -1.7% | -1.7% | -1.8 | +0.1 | -0.0 | -0.0 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -1.3% | -1.3% | -1.2 | -0.1 | -0.0 | -0.0 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -1.0% | -1.0% | +0.0 | -0.6 | -0.1 | -0.3 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +2.0% | +1.0% | +2.0 | -0.1 | +0.0 | +0.0 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -0.9% | -0.9% | +0.0 | -1.1 | +0.2 | +0.0 |
| Rural demand indicators mixed: tractor volumes dip in Oct, 2W festive sales firm, rural CPI above urban, rural jobs scheme person-days down (`EV_RURAL_DEMAND_SOFT26`) | occurred | 1.00 | -0.6% | -0.6% | -0.6 | +0.0 | +0.0 | +0.0 |
| RBI MPC Dec 2026 (~4 Dec): hikes repo another 25 bp to 5.75% (`EV_RBI_DEC26_HIKE25`) | scheduled | 0.42 | -1.3% | -0.5% | -1.2 | -0.1 | -0.0 | -0.0 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.55 | +1.0% | +0.5% | +0.5 | +0.2 | +0.3 | -0.0 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.25 | -1.8% | -0.4% | -0.9 | -0.4 | -0.5 | +0.0 |
| IMD April 2027 long-range forecast says normal or above-normal monsoon (>=96% LPA) (`EV_MONSOON27_FIRST_FORECAST_NORMAL`) | scheduled | 0.68 | +0.6% | +0.4% | +0.0 | +0.5 | +0.1 | +0.0 |
| Risk: stagflation scare - CPI >=6.5% while GDP growth slips below ~6% (Q3 FY27 data, late Feb 2027) (`EV_INDIA_STAGFLATION_SCARE`) | risk_scenario | 0.12 | -3.5% | -0.4% | -2.8 | -0.5 | -0.2 | -0.0 |
| Union Budget FY28 (1 Feb 2027) raises agri/rural spending and fertiliser subsidy; PM-Kisan/rural jobs top-up (`EV_BUDGET27_AGRI_RURAL`) | scheduled | 0.70 | +0.6% | +0.4% | +0.6 | +0.0 | -0.0 | +0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → MARICO | +2.00% | +1.00% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → MARICO | -1.20% | -0.50% |
| 1 | EV_BUDGET27_AGRI_RURAL ⇒ F_RURAL_DEMAND → MARICO | +0.60% | +0.42% |
| 1 | EV_RURAL_RELIEF_PACKAGE ⇒ F_RURAL_DEMAND → MARICO | +0.60% | +0.33% |
| 1 | EV_RBI_FEB27_HIKE25 ⇒ F_REPO_IN → MARICO | -1.20% | -0.32% |
| 2 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_RURAL_DEMAND → MARICO | +0.45% | +0.31% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → MARICO | +0.52% | +0.29% |
| 1 | EV_STATE_POLLS_FEB_MAR27 ⇒ F_RURAL_DEMAND → MARICO | +0.40% | +0.27% |
| 1 | EV_WHEAT27_CROP_BELOW ⇒ F_RURAL_DEMAND → MARICO | -0.40% | -0.26% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → MARICO | -0.88% | -0.22% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → MARICO | -1.20% | -0.22% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_REPO_IN → MARICO | -1.20% | -0.22% |
| 2 | EV_NEMONSOON26_NORMAL_UP ⇒ F_MONSOON → F_RURAL_DEMAND → MARICO | +0.23% | +0.19% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → MARICO | -0.77% | -0.19% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_FPI_FLOWS → MARICO | -0.77% | -0.19% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_FPI_FLOWS → MARICO | -1.60 | events | -1.28% |
| 1 | F_REPO_IN → MARICO | +1.00 | events | -1.20% |
| 1 | F_RURAL_DEMAND → MARICO | -0.25 | events | -0.50% |
| 1 | F_URBAN_DEMAND → MARICO | +0.20 | events | +0.24% |
| 1 | F_EDIBLE_OIL → MARICO | +0.19 | observed | -0.21% |
| 1 | F_USDINR → MARICO | -0.37 | observed | -0.15% |
| 3 | P_ANTI_DUMPING_IN → F_CHEM_FEEDSTOCK → F_PACKAGING → MARICO | +0.40 | events | -0.01% |
| 3 | F_CHINA_GDP → F_PETROCHEM_SPREADS → F_PACKAGING → MARICO | +0.30 | events | -0.01% |
| 4 | F_USDCNY → F_CHINA_CHEM_EXPORTS → F_PETROCHEM_SPREADS → F_PACKAGING → MARICO | -0.47 | observed | -0.00% |
| 4 | P_ANTI_DUMPING_IN → F_CHINA_CHEM_EXPORTS → F_PETROCHEM_SPREADS → F_PACKAGING → MARICO | +0.40 | events | -0.00% |
| 4 | F_CHINA_GDP → F_CHINA_CHEM_EXPORTS → F_PETROCHEM_SPREADS → F_PACKAGING → MARICO | +0.30 | events | -0.00% |
| 4 | C_US_CHINA_DECOUPLING → F_CHINA_CHEM_EXPORTS → F_PETROCHEM_SPREADS → F_PACKAGING → MARICO | -0.10 | events | -0.00% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-11 | Plix acquisition completion/integration | corporate_action | 0.70 | +0.0% | +0.00% |
| 2026-12 | Parachute price cuts or pack changes as copra falls | other | 0.50 | +0.0% | +0.00% |
| 2027-01 | Q3 FY27 business update and results (about Jan-Feb 2027) | results | 0.90 | +0.5% | +0.45% |

## Analyst profile (agent research, sourced)
# Marico — what moves the stock

**Business.** Marico sells Parachute coconut oil (~60% of the branded market), Saffola edible oils/foods, value-added hair oils and digital-first brands, with about a quarter of sales abroad. Copra (dried coconut) is the biggest cost line at roughly 28% of costs (approximate, model knowledge), so profit swings with copra before pricing catches up. Q2 FY27 (Sep 2026): sales Rs 2,722 cr (+12%), operating margin 18% (13% in the March quarter), Parachute volume growth a 22-quarter high, FY27 guidance raised (screener.in; Zee Business, Economic Times, 2 to 3 Nov 2026).

## Ranked drivers
1. **Copra/coconut oil prices.** About -3.8% equity value per +15% copra. Copra is down ~35% from peak, the reason margins are rebuilding.
2. **Rural demand.** Rural volume rebound lifted Q2; a weak monsoon is the key risk.
3. **Vegetable oil and crude-linked inputs.** Saffola's oils and paraffin/packaging carry cost risk.
4. **Valuation and rates.** The stock is near its 52-week high at ~60x earnings.
5. **International currencies and demand.**

## Worked transmission chains
- **Copra falls -> Marico cuts Parachute price/ raises packs -> volumes rebound against regional brands -> operating leverage lifts margin -> guidance upgrade (3rd order).** This is the exact sequence of Q2.
- **Middle East escalation -> Brent up -> HDPE and paraffin costs up -> hair-oil gross margin down; Brent up -> INR weaker -> RBI holds -> multiples stay compressed (4th order).**
- **Weak monsoon -> coconut-belt rainfall and rural incomes -> copra supply tightens or demand weakens -> Parachute price/volume trade-off swings.**
- **Edible-oil import duty cut (24 Sep) -> Saffola oils cheaper -> Saffola margin recovers within a quarter.**

## Current situation
Management raised FY27 growth and EBITDA-margin guidance (Economic Times 2026-11-04; exact figures not retrieved). Livemint (2026-11-03) asks whether gains persist beyond the copra windfall. The Plix buyout adds digital-first exposure. A discrepancy exists between screener net profit (Rs 683 cr incl. other income Rs 330 cr) and press-reported PAT (Rs 550 cr).

## Upcoming
Q3 business update (early Jan 2027), copra price path, Plix integration.

## Bull / bear
**Bull:** copra stays low, rural rebound, foods and digital scale. **Bear:** copra reflation, valuation de-rating, weak monsoon. Cost shares are approximate.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.