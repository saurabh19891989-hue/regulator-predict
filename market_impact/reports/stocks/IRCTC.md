# IRCTC — Indian Railway Catering And Tourism Corporation Ltd.
*MIDCAP_100 · Consumer Services · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +0.1%**, **12 months -0.6%** (rank 85 / 138 of 200 for 3m / 12m); beta 1.20
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +19.8%): 3 months 51%, 12 months 49%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -2.0% … P90 +1.5%; plausible 12m relative-return range incl. stock-specific noise: -26.0% … +24.9%
- Decomposition (12m): 0.5 × forward event exposure +0.3% (3m -0.1%; half assumed priced; market-priced macro drift removed) + 0.5 × company-specific catalysts -1.2%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply +2.0% (beta-adjusted) vs a realised market-adjusted move of -15.8% — gap +17.8 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## Where the expected return comes from
Market-priced macro drivers (rates, FX, commodities, indices, volatility, flows, growth, inflation) are taken as priced, so what is left is policy, regulatory, sector, theme, geopolitical and company-specific exposure — where 2nd–4th-order effects are most likely to be missed. Percentage points of the expected relative return.
| source | 12m: 1st order | 12m: 2nd–4th order | 12m total | 3m total |
|---|---|---|---|---|
| Policy | +0.11 | +0.12 | +0.23 | -0.04 |
| Regulatory | +0.00 | -0.01 | -0.01 | -0.00 |
| Sector | +0.00 | +0.66 | +0.66 | +0.29 |
| Theme | +0.00 | +0.03 | +0.03 | +0.02 |
| Geopolitics | -0.09 | +0.02 | -0.07 | -0.02 |
| Company catalysts | -0.60 | +0.00 | -0.60 | +0.30 |
| Market-priced macro | +0.00 | +0.00 | +0.00 | -0.00 |
| Beta adjustment | — | — | -0.69 | -0.31 |
| Universe centring | — | — | -0.15 | -0.10 |
| **Expected relative return** | | | **-0.58** | **+0.14** |

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Railway convenience-fee / ticketing / catering policy (`NEW_RAIL_TICKET_FEE_POLICY`) | +1 = tightening (cuts convenience fees, opens ticketing to agents, or changes catering contracts) | -6.00 | -6.00 | +0.00 | +0.00 | +0.00 | — |
| Air/hotel/tourism demand (`F_TRAVEL_DEMAND`) | +10% | +4.00 | +4.00 | +0.00 | +0.00 | +0.00 | — |
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +3.55 | +0.00 | +3.56 | +0.00 | -0.02 | — |
| India real GDP growth (`F_GDP_IN`) | +1 pp | +2.61 | +2.50 | +0.01 | -0.04 | +0.14 | — |
| India–Pakistan tension (`C_INDIA_PAKISTAN`) | +1 = escalation | -2.07 | -2.00 | -0.08 | -0.01 | +0.03 | — |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +1.95 | +0.00 | +0.48 | +1.36 | +0.11 | — |
| Private corporate capex (`F_PRIVATE_CAPEX`) | +10% capex growth | +1.66 | +0.00 | +1.60 | +0.01 | +0.05 | — |
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | +1.58 | +0.00 | +1.60 | +0.01 | -0.03 | — |
| Monsoon rainfall vs normal (`F_MONSOON`) | +10% above long-period average | +1.53 | +0.00 | +1.01 | +0.42 | +0.11 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -1.34 | +0.00 | -0.48 | -0.58 | -0.27 | — |
| Indian wage / employee-cost inflation (`F_WAGES_IN`) | +2 pp | +1.29 | +0.00 | +0.00 | +1.34 | -0.05 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -1.29 | -1.00 | +0.00 | -0.22 | -0.07 | — |
| Railway capex (`P_RAILWAY_CAPEX`) | +10% | +1.25 | +1.20 | +0.00 | +0.04 | +0.01 | — |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -1.18 | -0.80 | +0.00 | -0.22 | -0.16 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -2.2% | -2.2% | -2.2 | +0.0 | +0.0 | -0.0 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -1.9% | -1.9% | -0.9 | -0.7 | -0.7 | +0.3 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -1.9% | -1.9% | +0.0 | -1.3 | -0.5 | -0.1 |
| India Q1 FY27 GDP grows 7.8% (31 Aug 2026), beating ~7.3% consensus (`EV_GDP_Q1FY27_7_8`) | occurred | 1.00 | +1.7% | +1.7% | +1.2 | +0.5 | -0.0 | -0.0 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -1.3% | -1.3% | -1.0 | +0.0 | -0.3 | -0.1 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +2.5% | +1.2% | +2.5 | +0.0 | -0.0 | +0.0 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.55 | +1.6% | +0.9% | +0.0 | +1.2 | +0.3 | +0.1 |
| IMD April 2027 long-range forecast says normal or above-normal monsoon (>=96% LPA) (`EV_MONSOON27_FIRST_FORECAST_NORMAL`) | scheduled | 0.68 | +1.3% | +0.9% | +0.2 | +0.7 | +0.4 | +0.0 |
| Risk: stagflation scare - CPI >=6.5% while GDP growth slips below ~6% (Q3 FY27 data, late Feb 2027) (`EV_INDIA_STAGFLATION_SCARE`) | risk_scenario | 0.12 | -5.6% | -0.7% | -4.8 | -0.2 | -0.5 | -0.1 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.25 | -2.7% | -0.7% | +0.0 | -1.9 | -0.6 | -0.2 |
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -0.7% | -0.7% | +0.0 | -0.5 | -0.1 | -0.1 |
| North-east monsoon 2026 normal or above-normal (relief for southern reservoirs) (`EV_NEMONSOON26_NORMAL_UP`) | anticipated | 0.85 | +0.7% | +0.6% | +0.2 | +0.3 | +0.2 | +0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → IRCTC | +2.50% | +1.25% |
| 2 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_GDP_IN → IRCTC | +0.67% | +0.45% |
| 1 | EV_INDIA_STAGFLATION_SCARE ⇒ F_GDP_IN → IRCTC | -3.75% | -0.45% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → IRCTC | -1.00% | -0.42% |
| 1 | EV_Q2_FY27_GDP_STRONG ⇒ F_GDP_IN → IRCTC | +0.50% | +0.40% |
| 2 | EV_BUDGET27_AGRI_RURAL ⇒ F_RURAL_DEMAND → F_GDP_IN → IRCTC | +0.48% | +0.34% |
| 2 | EV_NEMONSOON26_NORMAL_UP ⇒ F_MONSOON → F_GDP_IN → IRCTC | +0.33% | +0.28% |
| 1 | EV_RBI_FEB27_HIKE25 ⇒ F_REPO_IN → IRCTC | -1.00% | -0.27% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → IRCTC | -1.50% | -0.27% |
| 2 | EV_RURAL_RELIEF_PACKAGE ⇒ F_RURAL_DEMAND → F_GDP_IN → IRCTC | +0.48% | +0.26% |
| 2 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ C_MIDEAST_CONFLICT → F_TRAVEL_DEMAND → IRCTC | +0.48% | +0.26% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → IRCTC | -0.96% | -0.24% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_FPI_FLOWS → IRCTC | -0.96% | -0.24% |
| 1 | EV_PULSES_VEG_SPIKE_WINTER ⇒ F_FOOD_INFLATION_IN → IRCTC | -0.96% | -0.24% |
| 1 | EV_Q2_FY27_GDP_SOFT ⇒ F_GDP_IN → IRCTC | -2.00% | -0.24% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_FOOD_INFLATION_IN → IRCTC | +2.00 | events | -1.60% |
| 1 | F_FPI_FLOWS → IRCTC | -1.60 | events | -1.60% |
| 1 | F_GDP_IN → IRCTC | +0.50 | events | +1.25% |
| 1 | F_REPO_IN → IRCTC | +1.00 | events | -1.00% |
| 2 | F_URBAN_DEMAND → F_TRAVEL_DEMAND → IRCTC | +0.20 | events | +0.51% |
| 2 | C_MIDEAST_CONFLICT → F_TRAVEL_DEMAND → IRCTC | +1.00 | events | -0.48% |
| 3 | P_ANTI_DUMPING_IN → F_CHEM_FEEDSTOCK → F_PACKAGING → IRCTC | +0.40 | events | -0.00% |
| 3 | F_CHINA_GDP → F_PETROCHEM_SPREADS → F_PACKAGING → IRCTC | +0.30 | events | -0.00% |
| 3 | F_BRENT → F_CHEM_FEEDSTOCK → F_PACKAGING → IRCTC | +0.00 | observed | -0.00% |
| 4 | F_BRENT → F_CHEM_FEEDSTOCK → F_PETROCHEM_SPREADS → F_PACKAGING → IRCTC | +0.00 | observed | +0.00% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-11 | Interim dividend announcement alongside H1 results (history, model knowledge) | corporate_action | 0.60 | +1.0% | +0.60% |
| 2026-11-12 | Q2 FY27 results (Sep quarter not yet reported in pack; date estimated from prior-year pattern, model knowledge) | results | 0.90 | +0.0% | +0.00% |
| 2027-03 | Government OFS in IRCTC planned in FY27 (floor typically at ~8-10% discount) | corporate_action | 0.40 | -4.5% | -1.80% |

## Analyst profile (agent research, sourced)
# IRCTC — Indian Railway Catering and Tourism Corp., as of 2026-11-05

*Sources: screener.in pack (through Jun-26), Google News headlines Aug-Oct 2026 (bodies not retrieved).*

## Business
IRCTC holds the monopoly on railway e-ticketing (convenience fees), catering, Rail Neer and runs tourism. TTM sales Rs 5,425 cr, OPM 31% (down from 47% in FY22), PAT Rs 1,393 cr, almost no debt, yield 2.0%, P/E 26.6. Government holds 62.4%. Q1 FY27 sales Rs 1,370 cr (+18%) but PAT Rs 330 cr flat; catering +34% (Upstox, 12 Aug).

## What moves the stock (ranked)
1. Government/Railway Board policy: convenience fee, catering and ticketing rules (new node proposed, -6 per tightening step), and the planned FY27 OFS (Moneycontrol 12 Aug; ~-4 to -8% on the event).
2. Passenger and tourism volume (F_TRAVEL_DEMAND +4, F_GDP_IN +2.5).
3. Mix and margin: catering cost inflation (F_FOOD_INFLATION_IN -0.8, F_PACKAGING -0.3).
4. Railway-PSU sentiment (P_RAILWAY_CAPEX +1.2; group down ~40% in a year, Livemint 17 Oct).
5. Rates (-1.0) and geopolitics (C_INDIA_PAKISTAN -2.0).

## Transmission examples
- **Food inflation up** -> catering input cost rises, tariff fixed by Railways -> segment margin slips (Q1 OPM 28% vs 34%) -> EBITDA flat despite +18% revenue -> de-rating (P/E from ~40x to 26x).
- **India-Pakistan escalation** -> train cancellations and tourism cuts in northern circuits -> volumes dip -> PSU risk-off and FPI exit (3.5% stake) -> price falls.
- **Railway capex up** -> more trains/capacity -> passenger growth +0.5% (weak) -> but sentiment lifts the basket (+14% day on 30 Sep, Zee Business).
- **Government OFS** -> supply of ~5-10% equity at a ~8-10% discount -> temporary price drop, free float rises, index weight up.

## Current situation
Stock Rs 460, -36% in 12m and near its 2020 level (NDTV Profit, 14 Oct); 52-week low Rs 435. Q2 FY27 results (Sep quarter) not yet in the pack, expected ~mid-Nov with possible interim dividend.

## Bull / bear
Bull: fee revision, strong festive travel, dividend yield support. Bear: OFS overhang, further margin dilution, policy caps.

## Uncertainties
Revenue mix and segment margins are model estimates; Q2 not yet released; fed funds link (+2.75, t 2.1) deemed non-causal.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.