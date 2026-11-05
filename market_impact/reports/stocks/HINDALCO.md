# HINDALCO — Hindalco Industries Ltd.
*NIFTY_50 · Metals & Mining · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +0.4%**, **12 months +0.1%** (rank 55 / 98 of 200 for 3m / 12m); beta 0.97
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +22.5%): 3 months 52%, 12 months 52%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -3.8% … P90 +5.7%; plausible 12m relative-return range incl. stock-specific noise: -28.5% … +30.9%
- Decomposition (12m): 0.5 × forward event exposure +2.8% (3m +1.2%; half assumed priced; market-priced macro drift removed) + 0.5 × company-specific catalysts -2.1%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply -8.5% (beta-adjusted) vs a realised market-adjusted move of -22.1% — gap +13.6 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Aluminium price (`F_ALUMINIUM`) | +10% aluminium | +6.00 | +6.00 | +0.00 | +0.00 | +0.00 | -19.6% |
| China growth / stimulus (`F_CHINA_GDP`) | +1 pp | +2.72 | +0.00 | +2.75 | -0.02 | -0.01 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | +1.77 | +1.80 | +0.02 | -0.04 | -0.01 | -1.1% |
| US growth (`F_US_GDP`) | +1 pp | +1.49 | +1.50 | +0.05 | -0.02 | -0.04 | — |
| Energy transition investment (`T_ENERGY_TRANSITION`) | +1 | +1.23 | +0.00 | +1.15 | +0.09 | -0.01 | — |
| India real GDP growth (`F_GDP_IN`) | +1 pp | +1.02 | +1.20 | -0.08 | -0.10 | -0.01 | — |
| Indian domestic coal price & availability cost (`F_COAL_INDIA`) | +10% domestic coal cost (notified/e-auction) | -1.00 | -1.00 | +0.00 | +0.00 | +0.00 | — |
| Copper price (`F_COPPER`) | +10% copper | +0.80 | +0.80 | +0.00 | +0.00 | +0.00 | -2.4% |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -0.76 | -0.60 | -0.07 | -0.08 | -0.01 | — |
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | +0.70 | +0.00 | +0.77 | -0.01 | -0.06 | — |
| Private corporate capex (`F_PRIVATE_CAPEX`) | +10% capex growth | +0.68 | +0.00 | +0.77 | -0.05 | -0.05 | — |
| US–China trade decoupling (`C_US_CHINA_DECOUPLING`) | +1 = more decoupling | -0.66 | +0.00 | +0.00 | -0.71 | +0.05 | — |
| Monsoon rainfall vs normal (`F_MONSOON`) | +10% above long-period average | +0.65 | +0.00 | +0.32 | +0.32 | +0.01 | — |
| US average effective tariff rate (all partners) (`NEW_US_TARIFF_GLOBAL`) | +5 pp effective tariff rate | -0.62 | +0.00 | -0.46 | +0.09 | -0.25 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Aluminium -20% since June; copper off record; Nifty Metal -7% in October (`EV_BASE_METALS_ALUMINIUM_SLIDE`) | occurred | 1.00 | -12.0% | -12.0% | -12.0 | +0.0 | +0.0 | +0.0 |
| US Q3 data: GDP 3.4%, CPI 3.7%, September payrolls only +29k (`EV_US_Q3_DATA_MIXED`) | occurred | 1.00 | +1.8% | +1.8% | +1.8 | +0.0 | -0.0 | -0.1 |
| India coal crunch: critical plant stocks, e-auction premiums ~94%, captive plants ordered to maximise output; CIL October output +19% (`EV_INDIA_COAL_CRUNCH`) | occurred | 1.00 | -1.5% | -1.5% | -1.5 | +0.0 | +0.0 | +0.0 |
| US recession (two negative quarters or NBER-style) beginning by mid-2027 (`EV_US_RECESSION_RISK_2027`) | risk_scenario | 0.25 | -4.0% | -1.0% | -4.5 | +0.1 | +0.3 | +0.1 |
| China Dec CEWC / Mar 2027 NPC delivers large fiscal stimulus and consumption push (`EV_CHINA_NPC_MAR27_BIG_STIMULUS`) | anticipated | 0.35 | +2.7% | +0.9% | +0.0 | +2.7 | -0.0 | +0.0 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -0.8% | -0.8% | -0.6 | -0.1 | -0.1 | -0.0 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | +0.7% | +0.7% | +0.0 | +0.7 | +0.0 | +0.0 |
| China Q3 GDP +4.5% (beat); property 'mini-stimulus' of late September; PMI 49.3; LPR unchanged (`EV_CHINA_Q3_GDP_AND_MINI_STIMULUS`) | occurred | 1.00 | +0.7% | +0.7% | +0.0 | +0.7 | -0.0 | +0.0 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -0.7% | -0.7% | +0.0 | -0.5 | -0.2 | -0.0 |
| Rupee at 95-96/USD and heavy RBI FX defence; reserves fall ~US$55bn from peak (`EV_RUPEE_DEFENCE_RESERVES_26`) | occurred | 1.00 | -0.7% | -0.7% | -0.7 | -0.0 | +0.0 | -0.0 |
| Cabinet approves Rs14,500 cr VGF for ~92 GWh grid-scale storage (4 Nov) (`EV_BESS_VGF_NOV26`) | occurred | 1.00 | +0.6% | +0.6% | +0.0 | +0.6 | +0.0 | -0.0 |
| China Central Economic Work Conference / NPC (Dec 2026-Mar 2027): larger-than-expected fiscal or property stimulus (`EV_CHINA_CEWC_STIMULUS_DEC26`) | anticipated | 0.45 | +1.2% | +0.5% | +0.3 | +0.9 | -0.0 | -0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_US_RECESSION_RISK_2027 ⇒ F_US_GDP → HINDALCO | -4.50% | -1.12% |
| 2 | EV_CHINA_NPC_MAR27_BIG_STIMULUS ⇒ F_CHINA_GDP → F_ALUMINIUM → HINDALCO | +2.28% | +0.80% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_USDINR → HINDALCO | +2.34% | +0.42% |
| 2 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → F_USDINR → HINDALCO | -0.83% | -0.41% |
| 2 | EV_CHINA_CEWC_STIMULUS_DEC26 ⇒ F_CHINA_GDP → F_ALUMINIUM → HINDALCO | +0.91% | +0.41% |
| 2 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ C_MIDEAST_CONFLICT → F_ALUMINIUM → HINDALCO | -0.72% | -0.40% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ C_MIDEAST_CONFLICT → HINDALCO | +0.50% | +0.28% |
| 2 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → F_USDINR → HINDALCO | -0.48% | -0.27% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → HINDALCO | -0.60% | -0.25% |
| 1 | EV_INDIA_ADD_DUTIES_NOTIFIED_H1_2027 ⇒ P_ANTI_DUMPING_IN → HINDALCO | +0.35% | +0.24% |
| 2 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_GDP_IN → HINDALCO | +0.32% | +0.22% |
| 2 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ C_MIDEAST_CONFLICT → F_ALUMINIUM → HINDALCO | +0.86% | +0.22% |
| 1 | EV_INDIA_STAGFLATION_SCARE ⇒ F_GDP_IN → HINDALCO | -1.80% | -0.22% |
| 2 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → F_USDINR → HINDALCO | +0.82% | +0.20% |
| 2 | EV_SUMMER27_POWER_SHORTFALL ⇒ F_POWER_DEMAND_IN → F_COAL_INDIA → HINDALCO | -0.48% | -0.19% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_ALUMINIUM → HINDALCO | -1.96 | observed | -11.77% |
| 1 | F_US_GDP → HINDALCO | +1.20 | events | +1.80% |
| 1 | F_COAL_INDIA → HINDALCO | +1.50 | events | -1.50% |
| 1 | F_USDINR → HINDALCO | -0.37 | observed | -0.66% |
| 1 | F_REPO_IN → HINDALCO | +1.00 | events | -0.60% |
| 1 | F_GDP_IN → HINDALCO | +0.50 | events | +0.60% |
| 1 | C_MIDEAST_CONFLICT → HINDALCO | +1.00 | events | -0.50% |
| 1 | P_US_TARIFF_INDIA → HINDALCO | -0.60 | events | +0.24% |
| 1 | P_ANTI_DUMPING_IN → HINDALCO | +0.40 | events | +0.20% |
| 1 | F_COPPER → HINDALCO | -0.24 | observed | -0.19% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-11-06 | Q2 FY27 results (record Q1 PAT Rs7,013 cr is the bar; LME aluminium eased vs Q1) | results | 0.97 | +0.0% | +0.00% |
| 2027-02 | Q3 FY27 results and Novelis net-debt reduction milestones | results | 0.90 | +0.0% | +0.00% |
| 2027-03 | EGA Al Taweelah smelter at full output (target Q1 2027) pressures LME aluminium | other | 0.70 | -3.0% | -2.10% |

## Analyst profile (agent research, sourced)
# HINDALCO — Hindalco Industries Ltd. (Nifty 50, I_NONFERROUS) — as of 2026-11-05

## Business
Aditya Birla Group's metals flagship with two engines. (1) India: integrated aluminium (captive bauxite and coal, Utkal and Aditya alumina refineries, smelters, rolled/foil/extrusion downstream) plus a copper smelter. (2) Novelis, the largest aluminium flat-rolled and can-sheet producer, roughly 55% of group sales (model knowledge). Q1 FY27 (Jun 2026): sales Rs84,825 cr, EBITDA Rs13,932 cr (16% OPM), record PAT Rs7,013 cr; India upstream alone was ~Rs7,400 cr of EBITDA (AL Circle, 2026-08-10). TTM EBITDA Rs40,903 cr; market cap Rs2.11 lakh cr. Q2 FY27 results fall on 2026-11-06.

## What moves the stock (ranked by modelled weight)
1. **LME aluminium** (w +6 per +10%): about 10% of EBITDA per 10% price move; the pack's empirical +5.45 (t=+7.3) agrees. Aluminium has slid from ~$3,400 to ~$3,050-3,200 on Gulf supply returning.
2. **USD/INR** (+1.8 per +3% weaker rupee): USD-linked aluminium revenue against INR costs, plus Novelis translation.
3. **US demand via Novelis** (+1.5 per +1pp growth): cans, autos, specialty sheet.
4. **India GDP / downstream demand** (+1.2), **Indian coal cost** (-1.0, partly hedged by captive blocks), **copper** (+0.8 as a basket proxy), **repo/discount rate** (-0.6), **Gulf conflict** (-0.5 net of the price channel).

Note the pack also shows strong co-movement with US equities (+3.2, t=+4.5) and VIX (-1.3, t=-3.1): the stock carries a high-beta cyclical component beyond any single commodity.

## Transmission examples
- **Gulf conflict de-escalation (aluminium path):** Iran talks progress -> Hormuz risk falls -> EGA's Al Taweelah smelter restart proceeds (50% done 2026-10-21, full by Q1 2027) -> Gulf supply returns -> LME aluminium -10% (Axis sees $2,800 in CY27) -> Hindalco India EBITDA -10% -> equity about -6%; third order: lower energy prices also cut caustic and CP-coke costs, a partial offset (+0.5).
- **Energy channel:** Brent up -> petroleum coke, caustic and freight costs up -> smelter cash cost up; fourth order: INR weakens on the oil bill -> USD revenue worth more in rupees, helping India EBITDA while Novelis's USD debt costs more to service in rupee terms.
- **Rates/US demand:** US 10-year yield up -> US auto and housing demand softer -> Novelis auto-sheet volumes down -> group EBITDA/t lower; also higher yield lifts discount rate on Novelis's leveraged balance sheet.
- **China:** China stimulus -> China GDP up -> aluminium and copper bid -> LME up -> India upstream margin up; reverse if China exports surplus semis.

## Current situation
Record Q1; Novelis net debt expected to fall and EBITDA/tonne to improve (Sahi/scanx, 2026-08). AluChem acquisition terminated on 2026-10-02. First coil at the Alabama greenfield on 2026-10-07. Stock down 8.5% in three months with technical "death cross" noted (Business Standard, 2026-10-27); Motilal Oswal and CLSA remain positive.

## Upcoming events
Q2 FY27 results 2026-11-06 (prob 0.97, +/-6%); Al Taweelah full restart by Q1 2027; Q3 results in Feb 2027.

## Bull and bear
Bull: aluminium holds above $3,300, Novelis deleverages, EBITDA doubling plan credible. Bear: LME to $2,800, Novelis execution misses, energy/caustic inflation, US tariff changes. Confidence medium; Novelis share of EBITDA and net debt figures are model knowledge and not verified against filings.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.