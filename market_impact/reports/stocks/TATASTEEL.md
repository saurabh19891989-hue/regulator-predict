# TATASTEEL — Tata Steel Ltd.
*NIFTY_50 · Metals & Mining · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +6.7%**, **12 months +12.4%** (rank 6 / 4 of 200 for 3m / 12m); beta 1.17
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +20.4%): 3 months 75%, 12 months 80%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 +10.3% … P90 +19.2%; plausible 12m relative-return range incl. stock-specific noise: -9.1% … +51.3%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +8.1 pp (model impact +16.3% beta-adjusted vs realised market-adjusted move -19.3%); forward event exposure +9.6% (3m +5.2%; half assumed priced); company-specific events +1.1%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Indian domestic steel price (`F_STEEL_INDIA`) | +7% domestic HRC/rebar price | +7.99 | +8.00 | +0.00 | -0.01 | +0.00 | — |
| China growth / stimulus (`F_CHINA_GDP`) | +1 pp | +4.54 | +0.00 | -0.41 | +3.50 | +1.45 | — |
| Global HRC steel price (`F_STEEL_GLOBAL`) | +10% global HRC | +3.97 | +2.00 | +1.97 | +0.00 | -0.01 | +20.6% |
| Indian safeguard/anti-dumping duty on steel imports (`P_STEEL_DUTY_IN`) | +10 pp effective duty | +3.19 | +0.00 | +3.20 | +0.00 | -0.01 | — |
| China steel exports (`F_CHINA_STEEL_EXPORTS`) | +15% y/y | -3.06 | +0.00 | -2.28 | -0.78 | +0.00 | — |
| US–China trade decoupling (`C_US_CHINA_DECOUPLING`) | +1 = more decoupling | -2.84 | +0.00 | -1.00 | -0.49 | -1.35 | — |
| USD/CNY (`F_USDCNY`) | +3% USD/CNY (yuan weaker) | -2.70 | -2.50 | +0.07 | -0.18 | -0.10 | -1.4% |
| Coking coal price (`F_COKING_COAL`) | +15% coking coal | -2.40 | -4.00 | +1.08 | +0.52 | +0.00 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | +2.22 | +1.50 | +0.88 | -0.14 | -0.02 | -1.1% |
| Central + state government capex (`F_GOVT_CAPEX`) | +10% capex growth | +1.87 | +1.50 | +0.56 | -0.11 | -0.09 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -1.25 | -1.00 | -0.12 | -0.10 | -0.03 | — |
| Europe growth (`F_EU_GDP`) | +1 pp | +1.19 | +1.20 | +0.00 | -0.01 | +0.00 | — |
| Iron ore price (`F_IRON_ORE`) | +15% iron ore | +1.13 | +0.50 | +0.22 | +0.41 | +0.00 | -12.5% |
| Indian vehicle demand (`F_AUTO_DEMAND_IN`) | +10% volumes | +1.00 | +1.00 | +0.00 | +0.00 | +0.00 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Global and Indian steel prices at multi-year highs (global HRC +60% y/y) (`EV_STEEL_RALLY_2026`) | occurred | 1.00 | +12.9% | +12.9% | +12.9 | +0.0 | -0.0 | +0.0 |
| China Q3 GDP +4.5% (beat); property 'mini-stimulus' of late September; PMI 49.3; LPR unchanged (`EV_CHINA_Q3_GDP_AND_MINI_STIMULUS`) | occurred | 1.00 | +2.4% | +2.4% | +1.1 | -0.3 | +1.1 | +0.5 |
| DGTR recommends/imposes anti-dumping duty on hot-rolled flat steel from China, Japan, Russia (`EV_INDIA_HR_STEEL_AD_PROVISIONAL`) | anticipated | 0.55 | +3.2% | +1.8% | +3.2 | +0.0 | -0.0 | +0.0 |
| China Dec CEWC / Mar 2027 NPC delivers large fiscal stimulus and consumption push (`EV_CHINA_NPC_MAR27_BIG_STIMULUS`) | anticipated | 0.35 | +4.8% | +1.7% | +0.8 | -0.9 | +3.6 | +1.4 |
| Coking coal price spike squeezes Indian steel margins (`EV_COKING_COAL_SURGE_AUG26`) | occurred | 1.00 | -1.6% | -1.6% | -2.0 | +0.4 | -0.0 | +0.0 |
| India Q1 FY27 GDP grows 7.8% (31 Aug 2026), beating ~7.3% consensus (`EV_GDP_Q1FY27_7_8`) | occurred | 1.00 | +1.6% | +1.6% | +1.5 | +0.3 | -0.2 | -0.1 |
| Chinese steel/aluminium export surge floods Asia as China demand stays weak (`EV_CHINA_STEEL_EXPORT_FLOOD`) | risk_scenario | 0.25 | -5.6% | -1.4% | -2.0 | -4.4 | +0.7 | +0.0 |
| Union Budget 2027-28 capex/railway allocation (infra, railways, defence) (`EV_BUDGET27_CAPEX_RAILWAY`) | scheduled | 0.90 | +1.5% | +1.3% | +1.2 | +0.4 | -0.1 | -0.1 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -1.2% | -1.2% | -1.0 | -0.1 | -0.1 | -0.0 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | +1.2% | +1.2% | +0.0 | +0.6 | +0.7 | -0.1 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -1.1% | -1.1% | +0.0 | -1.0 | -0.0 | -0.1 |
| China Central Economic Work Conference / NPC (Dec 2026-Mar 2027): larger-than-expected fiscal or property stimulus (`EV_CHINA_CEWC_STIMULUS_DEC26`) | anticipated | 0.45 | +2.2% | +1.0% | +0.3 | -0.1 | +1.6 | +0.4 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_INDIA_HR_STEEL_AD_PROVISIONAL ⇒ F_STEEL_INDIA → TATASTEEL | +3.20% | +1.76% |
| 1 | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → TATASTEEL | +1.20% | +1.08% |
| 1 | EV_UNION_BUDGET_FEB27_METALS ⇒ F_COKING_COAL → TATASTEEL | +1.20% | +1.08% |
| 2 | EV_CHINA_STEEL_EXPORT_FLOOD ⇒ F_CHINA_STEEL_EXPORTS → F_STEEL_INDIA → TATASTEEL | -2.40% | -0.60% |
| 1 | EV_STEEL_SAFEGUARD_EARLY_RELAXATION ⇒ F_STEEL_INDIA → TATASTEEL | -4.00% | -0.60% |
| 2 | EV_CHINA_NPC_MAR27_BIG_STIMULUS ⇒ F_CHINA_GDP → F_COKING_COAL → TATASTEEL | -1.60% | -0.56% |
| 1 | EV_CHINA_STEEL_EXPORT_FLOOD ⇒ F_STEEL_GLOBAL → TATASTEEL | -2.00% | -0.50% |
| 2 | EV_CHINA_STEEL_EXPORT_FLOOD ⇒ F_STEEL_GLOBAL → F_STEEL_INDIA → TATASTEEL | -1.97% | -0.49% |
| 2 | EV_CHINA_STEEL_OUTPUT_CURB_2027 ⇒ F_CHINA_STEEL_EXPORTS → F_STEEL_INDIA → TATASTEEL | +0.96% | +0.48% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → TATASTEEL | -1.00% | -0.42% |
| 3 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → F_USDINR → F_STEEL_INDIA → TATASTEEL | -0.83% | -0.41% |
| 3 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → F_USDINR → F_STEEL_INDIA → TATASTEEL | -0.74% | -0.41% |
| 2 | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → F_STEEL_INDIA → TATASTEEL | +0.45% | +0.40% |
| 3 | EV_CHINA_NPC_MAR27_BIG_STIMULUS ⇒ F_CHINA_GDP → F_STEEL_GLOBAL → F_STEEL_INDIA → TATASTEEL | +1.11% | +0.39% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_USDINR → TATASTEEL | +1.95% | +0.35% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_STEEL_INDIA → TATASTEEL | +1.35 | events | +10.80% |
| 1 | F_COKING_COAL → TATASTEEL | +1.30 | events | -5.20% |
| 1 | F_STEEL_GLOBAL → TATASTEEL | +2.06 | observed | +4.11% |
| 1 | F_GOVT_CAPEX → TATASTEEL | +1.00 | events | +1.50% |
| 1 | F_USDCNY → TATASTEEL | -0.47 | observed | +1.17% |
| 1 | F_REPO_IN → TATASTEEL | +1.00 | events | -1.00% |
| 1 | NEW_EU_STEEL_ACCESS → TATASTEEL | +1.00 | events | +1.00% |
| 1 | F_USDINR → TATASTEEL | -0.37 | observed | -0.55% |
| 1 | F_IRON_ORE → TATASTEEL | -0.83 | observed | -0.42% |
| 1 | F_GAS_GLOBAL → TATASTEEL | -0.47 | observed | +0.28% |
| 1 | F_EU_GDP → TATASTEEL | +0.22 | events | +0.26% |
| 1 | F_AUTO_DEMAND_IN → TATASTEEL | -0.10 | events | -0.10% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-11 | Q2 FY27 results (date not confirmed; analysts expected EBITDA to decline QoQ per Livemint 2026-10-18) | results | 0.95 | +0.0% | +0.00% |
| 2027-02 | Q3 FY27 results | results | 0.95 | +0.0% | +0.00% |
| 2027-03 | Dutch government joint letter of intent deadline (extended five months to March 2027): binding support for IJmuiden decarbonisation | regulatory | 0.55 | +0.5% | +0.28% |
| 2027-03 | Safeguard duty tightening on Indian flat imports | regulatory | 0.25 | +3.5% | +0.88% |

## Analyst profile (agent research, sourced)
# TATASTEEL — Tata Steel Ltd. (Nifty 50, I_STEEL) — as of 2026-11-05

## Business
India's largest steel group: Tata Steel India (Jamshedpur, Kalinganagar, Angul/Neelachal, NINL) with captive iron ore and about 45% captive coking coal, plus Tata Steel Netherlands, Tata Steel UK (Port Talbot moving to electric-arc steelmaking) and South-East Asian assets. Q1 FY27: sales Rs60,794 cr, EBITDA Rs9,264 cr (15%), PAT Rs2,385 cr. TTM EBITDA Rs36,189 cr. Net debt is around Rs80k cr (model estimate), so EV is ~1.4x market cap (Rs2.26 lakh cr). Q2 India crude steel output rose 10% YoY to 6.21 Mt.

## What moves the stock
1. **Indian steel price** (+8 per +7%), 2. **coking coal** (-4 per +15%, cushioned by captive coal), 3. **China/yuan** (-2.5; empirical -4.77, t=-2.9, shrunk to avoid double counting with price edges), 4. **global/European HRC** (+2), 5. **EU growth and decarbonisation policy** (+1.2), 6. **USD/INR, rates, government capex, auto demand** (+1.5, -1.0, +1.5, +1.0).

## Transmission examples
- **Europe path:** Middle East de-escalation -> gas price down -> European energy cost down (1st) -> IJmuiden and Port Talbot margins up (2nd) -> UK/Netherlands losses narrow, reducing the cash call from India (3rd) -> consolidated net debt/EBITDA falls and valuation multiple improves (4th).
- **China path:** US-China decoupling pushes Chinese steel to Asia -> India import parity falls -> HRC down -> India EBITDA down; Tata's coking-coal captive share cushions the cost side, so the spread loss is smaller than at SAIL.
- **Policy path:** Dutch joint letter of intent extended to March 2027 (25 Sep 2026): a signed subsidy deal removes decarbonisation funding risk; failure risks closure/impairment costs. CBAM and the EU quota (2.8 Mt window for India) shape European third-country competition.
- **Rates path:** Higher US/India yields -> discount rate on a levered cyclical up -> equity multiple compresses.

## Current situation
Stock near its 52-week low region (+5% on 2026-11-02, the largest one-day gain in 14 months), -16.5% over 6m. Livemint (2026-10-18) expected Q2 EBITDA to decline QoQ. Tata Steel bought 394 crore shares of T Steel Holdings for Rs3,260 cr (2026-09-29). Draft Steel Policy 2047 drew focus on 2026-10-16.

## Upcoming events
Q2 results in November (date unconfirmed); Dutch LoI deadline March 2027; Q3 results Feb 2027.

## Bull and bear
Bull: Indian prices firm, Europe turns, Dutch deal signed. Bear: Europe losses persist, coking coal squeezes, China exports. Confidence medium; segment shares and net debt are model estimates and should be verified against the Q2 filing.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.