# SUPREMEIND — Supreme Industries Ltd.
*MIDCAP_100 · Capital Goods · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -0.3%**, **12 months +0.0%** (rank 139 / 96 of 200 for 3m / 12m); beta 0.88
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +23.4%): 3 months 49%, 12 months 51%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -1.9% … P90 +2.9%; plausible 12m relative-return range incl. stock-specific noise: -29.0% … +31.3%
- Decomposition (12m): 0.5 × forward event exposure -0.0% (3m -0.2%; half assumed priced; market-priced macro drift removed) + 0.5 × company-specific catalysts +0.4%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply -2.0% (beta-adjusted) vs a realised market-adjusted move of -9.8% — gap +7.8 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## Where the expected return comes from
Market-priced macro drivers (rates, FX, commodities, indices, volatility, flows, growth, inflation) are taken as priced, so what is left is policy, regulatory, sector, theme, geopolitical and company-specific exposure — where 2nd–4th-order effects are most likely to be missed. Percentage points of the expected relative return.
| source | 12m: 1st order | 12m: 2nd–4th order | 12m total | 3m total |
|---|---|---|---|---|
| Policy | -0.33 | -0.03 | -0.36 | -0.25 |
| Sector | +0.60 | +0.15 | +0.75 | +0.30 |
| Theme | +0.00 | +0.01 | +0.01 | +0.00 |
| Geopolitics | +0.09 | +0.01 | +0.10 | +0.08 |
| Company catalysts | +0.20 | +0.00 | +0.20 | -0.06 |
| Market-priced macro | -0.00 | -0.00 | -0.00 | +0.00 |
| Beta adjustment | — | — | -0.51 | -0.23 |
| Universe centring | — | — | -0.15 | -0.10 |
| **Expected relative return** | | | **+0.04** | **-0.26** |

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | +2.07 | +2.00 | +0.00 | +0.08 | -0.01 | — |
| Indian anti-dumping duties (chemicals, solar, others) (`P_ANTI_DUMPING_IN`) | +1 = new broad duties | -2.01 | -2.00 | +0.00 | -0.01 | +0.00 | — |
| Residential real-estate sales (`F_HOUSING_DEMAND`) | +10% sales volume | +2.00 | +2.00 | +0.00 | -0.02 | +0.02 | — |
| Monsoon rainfall vs normal (`F_MONSOON`) | +10% above long-period average | +1.61 | +1.20 | +0.23 | +0.08 | +0.10 | — |
| Central + state government capex (`F_GOVT_CAPEX`) | +10% capex growth | +1.56 | +1.50 | +0.00 | +0.04 | +0.02 | — |
| Petrochemical / polymer spreads (`F_PETROCHEM_SPREADS`) | +10% polymer-naphtha spreads | -1.50 | -1.50 | +0.00 | +0.00 | +0.00 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -1.34 | -1.50 | +0.18 | -0.08 | +0.06 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -1.03 | -0.80 | -0.18 | -0.03 | -0.02 | — |
| ENSO state (El Nino strength) (`NEW_EL_NINO`) | +1 = El Nino year (ONI >= +1.0 sustained); -1 = La Nina | -0.73 | +0.00 | -0.58 | -0.10 | -0.05 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -0.72 | -0.60 | -0.06 | -0.06 | +0.00 | -1.1% |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -0.65 | +0.00 | -0.58 | -0.03 | -0.03 | — |
| Affordable-housing / home-loan support (`P_HOUSING_POLICY`) | +1 = stronger support | +0.64 | +0.00 | +0.64 | +0.00 | +0.00 | — |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +0.60 | +0.00 | +0.48 | +0.08 | +0.04 | — |
| General-government fiscal slippage / extra borrowing vs budget (Centre + states) (`NEW_FISCAL_SLIPPAGE_IN`) | +0.5 pp of GDP deficit above budget (~Rs2 lakh cr) | -0.57 | +0.00 | -0.48 | -0.07 | -0.01 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -2.0% | -2.0% | -1.5 | -0.3 | -0.1 | -0.1 |
| India Q1 FY27 GDP grows 7.8% (31 Aug 2026), beating ~7.3% consensus (`EV_GDP_Q1FY27_7_8`) | occurred | 1.00 | +1.7% | +1.7% | +1.5 | +0.1 | +0.1 | -0.0 |
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -1.5% | -1.5% | -1.5 | +0.0 | -0.0 | -0.0 |
| IMD April 2027 long-range forecast says normal or above-normal monsoon (>=96% LPA) (`EV_MONSOON27_FIRST_FORECAST_NORMAL`) | scheduled | 0.68 | +1.6% | +1.1% | +1.2 | +0.3 | +0.1 | +0.0 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -1.1% | -1.1% | -0.8 | -0.2 | +0.0 | -0.0 |
| Finance ministry notifies anti-dumping duties on a meaningful batch of Chinese chemicals/APIs/others (`EV_INDIA_ADD_DUTIES_NOTIFIED_H1_2027`) | anticipated | 0.70 | -1.4% | -1.0% | -1.4 | +0.0 | -0.0 | +0.0 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -0.9% | -0.9% | +0.0 | -0.8 | -0.0 | -0.1 |
| DGTR opens wave of anti-dumping probes on Chinese chemicals, APIs and steel (`EV_INDIA_ANTIDUMPING_WAVE_SEP_OCT26`) | occurred | 1.00 | -0.8% | -0.8% | -0.8 | +0.0 | -0.0 | +0.0 |
| North-east monsoon 2026 normal or above-normal (relief for southern reservoirs) (`EV_NEMONSOON26_NORMAL_UP`) | anticipated | 0.85 | +0.9% | +0.7% | +0.6 | +0.1 | +0.1 | +0.0 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.55 | +1.2% | +0.7% | +1.1 | +0.1 | -0.0 | +0.1 |
| Rural demand indicators mixed: tractor volumes dip in Oct, 2W festive sales firm, rural CPI above urban, rural jobs scheme person-days down (`EV_RURAL_DEMAND_SOFT26`) | occurred | 1.00 | -0.6% | -0.6% | -0.6 | +0.0 | -0.0 | +0.0 |
| IMD April 2027 forecast says below-normal monsoon (<96% LPA) - second weak year risk (`EV_MONSOON27_DEFICIT_FORECAST`) | risk_scenario | 0.32 | -1.8% | -0.6% | -1.2 | -0.3 | -0.2 | -0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_INDIA_ADD_DUTIES_NOTIFIED_H1_2027 ⇒ P_ANTI_DUMPING_IN → SUPREMEIND | -1.40% | -0.98% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ C_MIDEAST_CONFLICT → SUPREMEIND | +1.50% | +0.83% |
| 1 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → SUPREMEIND | +1.20% | +0.82% |
| 1 | EV_NEMONSOON26_NORMAL_UP ⇒ F_MONSOON → SUPREMEIND | +0.60% | +0.51% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ C_MIDEAST_CONFLICT → SUPREMEIND | -1.80% | -0.45% |
| 1 | EV_BUDGET27_AGRI_RURAL ⇒ F_RURAL_DEMAND → SUPREMEIND | +0.60% | +0.42% |
| 1 | EV_MONSOON27_DEFICIT_FORECAST ⇒ F_MONSOON → SUPREMEIND | -1.20% | -0.38% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → SUPREMEIND | -0.80% | -0.34% |
| 1 | EV_RURAL_RELIEF_PACKAGE ⇒ F_RURAL_DEMAND → SUPREMEIND | +0.60% | +0.33% |
| 1 | EV_STATE_POLLS_FEB_MAR27 ⇒ F_RURAL_DEMAND → SUPREMEIND | +0.40% | +0.27% |
| 1 | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → SUPREMEIND | +0.30% | +0.27% |
| 1 | EV_WHEAT27_CROP_BELOW ⇒ F_RURAL_DEMAND → SUPREMEIND | -0.40% | -0.26% |
| 1 | EV_SUMMER27_POWER_SHORTFALL ⇒ F_MONSOON → SUPREMEIND | -0.60% | -0.24% |
| 1 | EV_RBI_FEB27_HIKE25 ⇒ F_REPO_IN → SUPREMEIND | -0.80% | -0.22% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → SUPREMEIND | -0.39% | -0.21% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_MONSOON → SUPREMEIND | -1.56 | events | -1.87% |
| 1 | C_MIDEAST_CONFLICT → SUPREMEIND | +1.00 | events | -1.50% |
| 1 | F_REPO_IN → SUPREMEIND | +1.00 | events | -0.80% |
| 1 | P_ANTI_DUMPING_IN → SUPREMEIND | +0.40 | events | -0.80% |
| 1 | F_RURAL_DEMAND → SUPREMEIND | -0.25 | events | -0.50% |
| 1 | F_GOVT_CAPEX → SUPREMEIND | +0.20 | director_override | +0.30% |
| 2 | F_GSEC_10Y_IN → F_HOUSING_DEMAND → SUPREMEIND | +1.55 | director_override | -0.25% |
| 2 | F_GDP_IN → F_HOUSING_DEMAND → SUPREMEIND | +0.50 | events | +0.24% |
| 1 | F_USDINR → SUPREMEIND | -0.37 | observed | +0.22% |
| 2 | F_REPO_IN → F_HOUSING_DEMAND → SUPREMEIND | +1.00 | events | -0.21% |
| 2 | F_CHINA_GDP → F_PETROCHEM_SPREADS → SUPREMEIND | +0.30 | events | -0.18% |
| 2 | F_STEEL_INDIA → F_HOUSING_DEMAND → SUPREMEIND | +1.35 | events | -0.11% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-12 | PVC price movement (management says near peak, may rise slightly) | other | 0.50 | -0.2% | -0.12% |
| 2027-01 | Q3 FY27 results (Dec quarter) | results | 0.95 | +0.0% | +0.00% |
| 2028-03 | New plant commissioning (Jammu, Patna, Erode, Pondicherry, JNPT) - first fully operational by Mar 2028 | capex | 0.30 | +1.8% | +0.53% |

## Analyst profile (agent research, sourced)
# SUPREMEIND — Supreme Industries (as of 2026-11-05)

## Business
India's largest plastics converter: piping systems (PVC/CPVC/HDPE for plumbing, agriculture, infrastructure; about 70% of volume), packaging and cross-laminated films, industrial moulded parts, consumer products and composite LPG cylinders. Q2 FY27 (reported 26 Oct 2026): revenue Rs 3,361 cr (+40%), operating margin 12.8%, PAT Rs 262 cr (+59%). Piping volumes rose 24% in Q2 and 23% in October after a 13.5% fall in Q1 triggered by an "unprecedented" April cut in PVC prices (distributors destocked). Industry PVC volume fell about 10% in H1 while Supreme gained share. Guidance was cut: piping volume +13% (from 15-17%), total volume +10% (from 12%), FY27 revenue Rs 13,500-14,000 cr, operating margin 14-14.5%, capex about Rs 1,000 cr, six new plants by March 2029. The company is debt free; the stock (Rs 3,320, P/E 37) fell about 4% on the print and is -15% over 12 months.

## What moves the stock, ranked
1. **Polymer prices and their direction** (-1.5 per +10% polymer spreads). Rising PVC gives inventory gains and restocking; falling PVC causes destocking (the Q1 pattern). Resin is about 70% of costs; selling prices follow with a 10-15 day lag.
2. **West Asia supply of PE/PP** (-1.5 per escalation). The Chairman said polyethylene prices rose with crude and disrupted Middle East supply, and packaging could not pass this on.
3. **Housing, rural and monsoon demand** (+2.0, +2.0, +1.2).
4. **Government capex / Jal Jeevan Mission** (+1.5). Nal Se Jal is "significantly lower than budgeted" as states do not match central funds.
5. **Trade policy** (anti-dumping on PVC resin -2.0, low confidence), **USD/INR** (-0.6) and **repo** (-0.8).

## Transmission examples
- **Energy chain:** Middle East escalation -> Brent up and Gulf polymer exports disrupted -> PE/PP prices jump -> packaging and consumer segments absorb the rise (as in Q2) -> consolidated margin below the 14-14.5% guidance; at the same time piping inventories gain from rising PVC -> partially offsetting.
- **Destocking chain:** PVC prices fall sharply (as in April) -> dealers defer purchases -> piping volumes fall (Q1 -13.5%) -> operating leverage turns negative -> margin miss -> stock de-rates; recovery arrives when prices stabilise (Q2 +24%).
- **Fiscal chain:** Brent up -> fuel subsidies and inflation up -> states squeeze capex and delay JJM co-funding -> Nal Se Jal pipe orders slip -> infrastructure piping volumes lag the agri and housing segments.
- **Macro chain:** INR weaker -> imported PVC dearer -> prices raised -> short-run inventory gain but demand elasticity at the retail end.

## Current situation and upcoming events
Both Q1 and Q2 margins missed estimates; employee costs +25% y/y. Management says no further guidance cut is expected and first 25 days of October were +23% volume. Events: Q3 results (Jan 2027), Union Budget (1 Feb 2027), PVC price direction (Dec 2026), plant commissioning (2028).

## Bull and bear
Bull: stable PVC, restocking and housing/agri strength deliver 13% piping growth, value-added products (+38% to Rs 1,476 cr) lift margin to 14.5%. Bear: crude-led polymer spikes squeeze packaging/consumer, PVC falls again to destock channels, JJM stays weak and the P/E compresses toward 30x. Uncertainty: cost-share and segment-mix numbers are approximate (not company-disclosed in the sources read); current anti-dumping status on PVC unverified.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.