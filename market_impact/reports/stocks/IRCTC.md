# IRCTC — Indian Railway Catering And Tourism Corporation Ltd.
*MIDCAP_100 · Consumer Services · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +1.1%**, **12 months +1.9%** (rank 61 / 70 of 200 for 3m / 12m); beta 1.20
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +19.8%): 3 months 54%, 12 months 60%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -0.6% … P90 +5.6%; plausible 12m relative-return range incl. stock-specific noise: -20.1% … +22.5%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +0.9 pp (model impact +1.8% beta-adjusted vs realised market-adjusted move -15.8%); forward event exposure +5.5% (3m +2.0%; half assumed priced); company-specific events -1.2%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Railway convenience-fee / ticketing / catering policy (`NEW_RAIL_TICKET_FEE_POLICY`) | +1 = tightening (cuts convenience fees, opens ticketing to agents, or changes catering contracts) | -6.00 | -6.00 | +0.00 | +0.00 | +0.00 | — |
| Air/hotel/tourism demand (`F_TRAVEL_DEMAND`) | +10% | +4.00 | +4.00 | +0.00 | +0.00 | +0.00 | — |
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +3.36 | +0.00 | +3.56 | -0.14 | -0.06 | — |
| India real GDP growth (`F_GDP_IN`) | +1 pp | +2.33 | +2.50 | -0.18 | -0.09 | +0.09 | — |
| India–Pakistan tension (`C_INDIA_PAKISTAN`) | +1 = escalation | -2.07 | -2.00 | -0.08 | -0.01 | +0.02 | — |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +2.02 | +0.00 | +0.48 | +1.51 | +0.03 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -1.80 | +0.00 | -1.15 | -0.57 | -0.07 | — |
| Monsoon rainfall vs normal (`F_MONSOON`) | +10% above long-period average | +1.58 | +0.00 | +1.01 | +0.32 | +0.24 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -1.43 | +0.00 | -0.48 | -0.58 | -0.36 | — |
| Private corporate capex (`F_PRIVATE_CAPEX`) | +10% capex growth | +1.36 | +0.00 | +1.60 | -0.22 | -0.02 | — |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -1.33 | -0.80 | +0.00 | -0.38 | -0.15 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -1.30 | -1.00 | +0.00 | -0.22 | -0.08 | — |
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | +1.27 | +0.00 | +1.60 | -0.22 | -0.11 | — |
| Railway capex (`P_RAILWAY_CAPEX`) | +10% | +1.24 | +1.20 | +0.00 | +0.04 | +0.00 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -4.9% | -4.9% | +0.0 | -2.8 | -1.4 | -0.6 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -3.0% | -3.0% | -0.9 | -1.3 | -0.7 | -0.1 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -2.2% | -2.2% | -2.2 | +0.0 | +0.0 | -0.1 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -2.0% | -2.0% | +0.0 | -1.3 | -0.4 | -0.3 |
| India Q1 FY27 GDP grows 7.8% (31 Aug 2026), beating ~7.3% consensus (`EV_GDP_Q1FY27_7_8`) | occurred | 1.00 | +1.6% | +1.6% | +1.2 | +0.4 | -0.0 | -0.0 |
| Union Budget 2027-28 capex/railway allocation (infra, railways, defence) (`EV_BUDGET27_CAPEX_RAILWAY`) | scheduled | 0.90 | +1.7% | +1.5% | +1.0 | +0.7 | +0.1 | -0.1 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -1.4% | -1.4% | -1.0 | +0.0 | -0.3 | -0.1 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +2.5% | +1.3% | +2.5 | +0.0 | -0.0 | +0.1 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.36 | -3.3% | -1.2% | +0.0 | -2.1 | -0.9 | -0.3 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.58 | +2.0% | +1.1% | +0.0 | +1.3 | +0.5 | +0.2 |
| IMD April 2027 long-range forecast says normal or above-normal monsoon (>=96% LPA) (`EV_MONSOON27_FIRST_FORECAST_NORMAL`) | scheduled | 0.68 | +1.1% | +0.8% | +0.2 | +0.7 | +0.3 | -0.0 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.28 | -2.7% | -0.7% | +0.0 | -2.5 | -0.3 | +0.1 |

## Strongest causal chains (1st–4th order)
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_RECORD_OUTFLOW_26 ⇒ F_FPI_FLOWS → IRCTC | -2.20% | -2.20% |
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_GDP_IN → IRCTC | -1.49% | -1.49% |
| 2 | EV_CPI_REACCEL_SEP26 ⇒ F_CPI_IN → F_REPO_IN → IRCTC | -1.32% | -1.32% |
| 1 | EV_GDP_Q1FY27_7_8 ⇒ F_GDP_IN → IRCTC | +1.25% | +1.25% |
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → IRCTC | +2.50% | +1.25% |
| 1 | EV_RBI_OCT26_HIKE25 ⇒ F_REPO_IN → IRCTC | -1.00% | -1.00% |
| 3 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_CPI_IN → F_REPO_IN → IRCTC | -0.89% | -0.89% |
| 1 | EV_CPI_REACCEL_SEP26 ⇒ F_FOOD_INFLATION_IN → IRCTC | -0.88% | -0.88% |
| 1 | EV_BUDGET27_CAPEX_RAILWAY ⇒ P_RAILWAY_CAPEX → IRCTC | +0.96% | +0.86% |
| 2 | EV_SWMONSOON26_DEFICIT ⇒ F_MONSOON → F_GDP_IN → IRCTC | -0.84% | -0.84% |
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ C_MIDEAST_CONFLICT → F_TRAVEL_DEMAND → IRCTC | -0.72% | -0.72% |
| 2 | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → F_GDP_IN → IRCTC | +0.72% | +0.65% |
| 3 | EV_OMC_FUEL_FREEZE_LOSSES ⇒ NEW_OMC_MARKETING_MARGIN → F_GOVT_CAPEX → F_GDP_IN → IRCTC | -0.61% | -0.61% |
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_FPI_FLOWS → IRCTC | -0.59% | -0.59% |
| 2 | EV_GDP_Q1FY27_7_8 ⇒ F_URBAN_DEMAND → F_TRAVEL_DEMAND → IRCTC | +0.51% | +0.51% |

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