# NATIONALUM — National Aluminium Co. Ltd.
*MIDCAP_100 · Metals & Mining · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +1.6%**, **12 months +1.7%** (rank 45 / 61 of 200 for 3m / 12m); beta 1.13
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +37.6%): 3 months 53%, 12 months 30%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -1.9% … P90 +10.1%; plausible 12m relative-return range incl. stock-specific noise: -38.7% … +13.9%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +0.0 pp (model impact -10.5% beta-adjusted vs realised market-adjusted move -29.5%); forward event exposure +7.4% (3m +4.6%; half assumed priced); company-specific events -1.8%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Aluminium price (`F_ALUMINIUM`) | +10% aluminium | +6.50 | +6.50 | +0.00 | +0.00 | +0.00 | -19.6% |
| China growth / stimulus (`F_CHINA_GDP`) | +1 pp | +4.06 | +0.00 | +2.31 | +1.73 | +0.02 | — |
| Mining royalty / mineral tax burden (`P_MINING_ROYALTY`) | +1 = higher | -3.00 | -3.00 | +0.00 | +0.00 | +0.00 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | +2.90 | +3.00 | -0.04 | -0.06 | +0.00 | -1.1% |
| Copper price (`F_COPPER`) | +10% copper | +2.60 | +0.00 | +2.60 | +0.00 | +0.00 | -2.4% |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | +2.32 | +0.00 | +0.96 | +1.20 | +0.16 | — |
| Alumina price (FOB Australia) (`NEW_ALUMINA_PRICE`) | +15% alumina | +2.00 | +2.00 | +0.00 | +0.00 | +0.00 | — |
| Energy transition investment (`T_ENERGY_TRANSITION`) | +1 | +1.78 | +1.00 | +0.50 | +0.29 | -0.01 | — |
| Renewable / transmission policy support (`P_RENEWABLE_SUPPORT`) | +1 = stronger support | +1.26 | +0.00 | +0.50 | +0.48 | +0.29 | — |
| US–China trade decoupling (`C_US_CHINA_DECOUPLING`) | +1 = more decoupling | -1.06 | +0.00 | +0.00 | -0.60 | -0.46 | — |
| Indian domestic coal price & availability cost (`F_COAL_INDIA`) | +10% domestic coal cost (notified/e-auction) | -0.94 | -1.00 | +0.06 | +0.00 | +0.00 | — |
| India real GDP growth (`F_GDP_IN`) | +1 pp | -0.70 | +0.00 | -0.32 | -0.30 | -0.08 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -0.65 | -0.50 | -0.12 | -0.03 | +0.00 | — |
| US tariffs on Indian goods (`P_US_TARIFF_INDIA`) | +10 pp average tariff | +0.61 | +0.00 | +0.42 | +0.17 | +0.02 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Aluminium -20% since June; copper off record; Nifty Metal -7% in October (`EV_BASE_METALS_ALUMINIUM_SLIDE`) | occurred | 1.00 | -12.7% | -12.7% | -12.7 | +0.0 | +0.0 | +0.0 |
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | +1.8% | +1.8% | +0.0 | +1.6 | +0.1 | +0.1 |
| China Dec CEWC / Mar 2027 NPC delivers large fiscal stimulus and consumption push (`EV_CHINA_NPC_MAR27_BIG_STIMULUS`) | anticipated | 0.35 | +4.0% | +1.4% | +0.0 | +2.2 | +1.8 | +0.0 |
| India coal crunch: critical plant stocks, e-auction premiums ~94%, captive plants ordered to maximise output; CIL October output +19% (`EV_INDIA_COAL_CRUNCH`) | occurred | 1.00 | -1.2% | -1.2% | -1.2 | +0.0 | +0.0 | +0.0 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | +1.1% | +1.1% | +0.0 | +1.2 | -0.0 | -0.0 |
| China Q3 GDP +4.5% (beat); property 'mini-stimulus' of late September; PMI 49.3; LPR unchanged (`EV_CHINA_Q3_GDP_AND_MINI_STIMULUS`) | occurred | 1.00 | +1.1% | +1.1% | +0.0 | +0.6 | +0.5 | +0.0 |
| Rupee at 95-96/USD and heavy RBI FX defence; reserves fall ~US$55bn from peak (`EV_RUPEE_DEFENCE_RESERVES_26`) | occurred | 1.00 | -1.1% | -1.1% | -1.1 | +0.0 | +0.0 | +0.0 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.55 | -1.8% | -1.0% | +0.7 | -2.3 | -0.2 | +0.0 |
| China Central Economic Work Conference / NPC (Dec 2026-Mar 2027): larger-than-expected fiscal or property stimulus (`EV_CHINA_CEWC_STIMULUS_DEC26`) | anticipated | 0.45 | +2.1% | +0.9% | +0.0 | +2.0 | +0.1 | +0.0 |
| Cabinet approves Rs14,500 cr VGF for ~92 GWh grid-scale storage (4 Nov) (`EV_BESS_VGF_NOV26`) | occurred | 1.00 | +0.9% | +0.9% | +0.5 | +0.2 | +0.1 | -0.0 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | -1.4% | -0.7% | +0.0 | -1.5 | +0.0 | +0.1 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -0.7% | -0.7% | -0.5 | -0.1 | -0.0 | +0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 2 | EV_CHINA_NPC_MAR27_BIG_STIMULUS ⇒ F_CHINA_GDP → F_ALUMINIUM → NATIONALUM | +2.47% | +0.86% |
| 2 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ C_MIDEAST_CONFLICT → F_ALUMINIUM → NATIONALUM | -1.56% | -0.86% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_USDINR → NATIONALUM | +3.90% | +0.70% |
| 2 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → F_USDINR → NATIONALUM | -1.38% | -0.69% |
| 3 | EV_CHINA_NPC_MAR27_BIG_STIMULUS ⇒ F_CHINA_GDP → F_COPPER → F_ALUMINIUM → NATIONALUM | +1.43% | +0.50% |
| 2 | EV_CHINA_CEWC_STIMULUS_DEC26 ⇒ F_COPPER → F_ALUMINIUM → NATIONALUM | +1.04% | +0.47% |
| 2 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ C_MIDEAST_CONFLICT → F_ALUMINIUM → NATIONALUM | +1.87% | +0.47% |
| 2 | EV_CHINA_CEWC_STIMULUS_DEC26 ⇒ F_CHINA_GDP → F_ALUMINIUM → NATIONALUM | +0.99% | +0.44% |
| 1 | EV_SUMMER27_POWER_SHORTFALL ⇒ F_POWER_PRICE_IN → NATIONALUM | +0.90% | +0.36% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → NATIONALUM | +0.65% | +0.36% |
| 2 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → F_USDINR → NATIONALUM | -0.62% | -0.34% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → NATIONALUM | -1.10% | -0.28% |
| 2 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → F_USDINR → NATIONALUM | +1.04% | +0.26% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → F_USDINR → NATIONALUM | +0.90% | +0.22% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → NATIONALUM | -0.50% | -0.21% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_ALUMINIUM → NATIONALUM | -1.96 | observed | -12.75% |
| 1 | F_COAL_INDIA → NATIONALUM | +1.50 | events | -1.50% |
| 1 | F_USDINR → NATIONALUM | -0.37 | observed | -1.11% |
| 1 | F_POWER_PRICE_IN → NATIONALUM | +1.90 | director_override | +0.57% |
| 1 | T_ENERGY_TRANSITION → NATIONALUM | +0.50 | events | +0.50% |
| 1 | F_REPO_IN → NATIONALUM | +1.00 | events | -0.50% |
| 1 | F_BRENT → NATIONALUM | +0.00 | observed | -0.00% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-11-03 | Q2 FY27 results (occurred): PAT +28%, interim dividend Rs4.50 | results | 1.00 | +0.0% | +0.00% |
| 2027-02 | Q3 FY27 results | results | 0.95 | +0.0% | +0.00% |
| 2027-03 | Refinery expansion start-up and Anugul smelter expansion approvals progress | capex | 0.60 | +1.0% | +0.60% |
| 2027-03 | Full restart of EGA Al Taweelah (Q1 2027) pressures LME | other | 0.70 | -3.5% | -2.45% |

## Analyst profile (agent research, sourced)
# NATIONALUM — National Aluminium Company Ltd. (Midcap 100, I_NONFERROUS) — as of 2026-11-05

## Business
Government-owned (51.3%) bauxite-alumina-aluminium producer in Odisha: 2.1 Mtpa alumina refinery (expansion nearing start-up), 0.46 Mtpa smelter and 1,200 MW captive power; roughly half of alumina is exported. Q2 FY27: net sales Rs5,380 cr (+26%), PAT Rs1,835 cr (+28%), best-ever H1 PAT Rs3,837 cr, interim dividend Rs4.50. TTM sales Rs20,466 cr, EBITDA Rs9,641 cr (47%); market cap Rs60,444 cr; net cash. Rs30,000 cr expansion plan includes a smelter at Anugul.

## What moves the stock
1. **LME aluminium** (+6.5 per +10%): pack empirical +7.08 (t=+5.8) agrees. 2. **USD/INR** (+3.0). 3. **Alumina price** (+2.0; proposed node). 4. **Indian coal cost** (-1.0, with Utkal-D captive target of 4.8 MT). 5. Royalty (-3.0), Brent (-0.5), energy-transition theme (+1.0), repo (-0.5).

## Transmission examples
- **Gulf path:** Peace deal -> Hormuz risk down -> EGA's Al Taweelah smelter back to full output by Q1 2027 (50% done 2026-10-21) -> LME aluminium toward $2,800 (Axis Capital) -> NALCO smelter revenue -12% -> EBITDA -16% -> equity -8; third order: Gulf alumina buyers get more local supply, weakening NALCO alumina export demand.
- **Cost path:** Brent up -> CP coke and pitch up -> smelter cost up; at the same time INR depreciation lifts USD-linked revenue, a partial offset.
- **Policy path:** Mining royalty or Odisha levy hike -> bauxite cost up -> margin down 2-3%.
- **China path:** China capacity cap holds -> global deficit -> aluminium firm -> NALCO profits.

## Current situation
Record H1 but cost pressure and a 16.4% fall in alumina exports in Q2; LME has fallen to ~$3,050-3,200 (low since February on 2026-10-12). Prabhudas Lilladher target Rs385 (2026-11-04).

## Upcoming events
Q3 results Feb 2027; refinery expansion start-up; EGA restart; smelter approvals.

## Bull and bear
Bull: LME holds above $3,300, refinery ramps, low-cost integration. Bear: oversupply (Discovery Alert, 2026-10-26), alumina weakness, capex execution. Confidence medium.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.