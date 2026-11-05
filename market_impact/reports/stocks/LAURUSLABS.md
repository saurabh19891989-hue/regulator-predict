# LAURUSLABS — Laurus Labs Ltd.
*MIDCAP_100 · Healthcare · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +0.1%**, **12 months +0.8%** (rank 96 / 85 of 200 for 3m / 12m); beta 0.96
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +34.0%): 3 months 50%, 12 months 32%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -5.4% … P90 +7.3%; plausible 12m relative-return range incl. stock-specific noise: -39.5% … +31.7%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves -3.4 pp (model impact -6.7% beta-adjusted vs realised market-adjusted move +62.5%); forward event exposure +7.1% (3m +5.1%; half assumed priced); company-specific events +3.6%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| China+1 manufacturing relocation to India (`T_CHINA_PLUS_ONE`) | +1 | +5.89 | +6.00 | -0.16 | +0.05 | +0.01 | — |
| USFDA inspection/enforcement intensity (`P_USFDA_ENFORCEMENT`) | +1 = stricter | -3.80 | -4.00 | +0.20 | +0.00 | +0.00 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | +3.17 | +4.00 | -0.62 | -0.19 | -0.02 | -1.1% |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +2.70 | +3.00 | -0.37 | +0.02 | +0.04 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -2.00 | -1.80 | -0.16 | -0.01 | -0.03 | — |
| Production-linked incentive schemes (`P_PLI`) | +1 = expansion/disbursement | +1.84 | +0.00 | +1.92 | -0.10 | +0.01 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -1.83 | +0.00 | -1.27 | -0.58 | +0.02 | — |
| China chemical/API dumping intensity (`F_CHINA_CHEM_EXPORTS`) | +15% export volumes / price cuts | -1.50 | -1.50 | +0.00 | +0.00 | +0.00 | — |
| GLP-1 / obesity drug adoption (`T_GLP1`) | +1 | +1.50 | +1.50 | +0.00 | +0.00 | +0.00 | — |
| US tariffs on pharmaceuticals (`P_US_PHARMA_TARIFF`) | +10 pp on Indian pharma exports | -1.38 | -1.50 | +0.12 | +0.00 | +0.00 | — |
| US tariffs on Indian goods (`P_US_TARIFF_INDIA`) | +10 pp average tariff | -1.37 | +0.00 | -1.42 | +0.06 | -0.02 | — |
| India real GDP growth (`F_GDP_IN`) | +1 pp | -1.06 | +0.00 | -0.31 | -0.58 | -0.18 | — |
| Russia (oil discounts, defence, sanctions) (`C_RUSSIA`) | +1 = closer trade access / larger discounts | -1.02 | +0.00 | +0.00 | -1.26 | +0.24 | — |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -1.01 | +0.00 | +0.00 | -0.70 | -0.31 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -5.8% | -5.8% | -6.6 | +1.0 | -0.0 | -0.1 |
| USFDA warning letters: Alembic, Aurobindo-Eugia, Dabur (Jul-Aug 2026) (`EV_USFDA_WARNING_WAVE_26`) | occurred | 1.00 | -3.8% | -3.8% | -4.0 | +0.2 | +0.0 | +0.0 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +6.6% | +3.3% | +7.5 | -1.1 | +0.0 | +0.1 |
| China+1 momentum: Apple/Foxconn/Tata iPhone 18 Pro export ramp, India ~50% of US smartphone imports, PLI round 4 (textiles) and component schemes (`EV_CHINA_PLUS_ONE_ELECTRONICS`) | anticipated | 0.80 | +3.5% | +2.8% | +3.6 | -0.1 | +0.0 | -0.0 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -2.1% | -2.1% | +0.0 | -1.5 | -0.7 | +0.0 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -2.0% | -2.0% | -1.8 | -0.2 | -0.0 | -0.1 |
| US midterms (3 Nov 2026): Democrats win House and Senate (`EV_US_MIDTERMS_DEM_SWEEP`) | occurred | 1.00 | +1.4% | +1.4% | +1.5 | -0.1 | -0.0 | +0.0 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.28 | -4.7% | -1.3% | +0.0 | -5.4 | +0.9 | -0.2 |
| Rupee at 95-96/USD and heavy RBI FX defence; reserves fall ~US$55bn from peak (`EV_RUPEE_DEFENCE_RESERVES_26`) | occurred | 1.00 | -1.2% | -1.2% | -1.5 | +0.2 | +0.1 | +0.0 |
| India-US interim trade agreement formally signed/announced (`EV_INDIA_US_INTERIM_DEAL_SIGNED`) | anticipated | 0.65 | +1.8% | +1.1% | +1.8 | -0.1 | +0.0 | +0.0 |
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | +1.1% | +1.1% | +0.0 | +4.5 | -2.5 | -0.8 |
| Disorderly yen carry-trade unwind (Aug-2024-style) after BoJ/MoF action (`EV_YEN_CARRY_UNWIND_RISK`) | risk_scenario | 0.18 | -5.7% | -1.0% | +0.0 | -6.8 | +1.4 | -0.4 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → LAURUSLABS | +7.50% | +3.75% |
| 1 | EV_CHINA_PLUS_ONE_ELECTRONICS ⇒ T_CHINA_PLUS_ONE → LAURUSLABS | +3.60% | +2.88% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → LAURUSLABS | -4.48% | -1.25% |
| 1 | EV_INDIA_US_INTERIM_DEAL_SIGNED ⇒ T_CHINA_PLUS_ONE → LAURUSLABS | +1.80% | +1.17% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_USDINR → LAURUSLABS | +5.20% | +1.14% |
| 2 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → F_USDINR → LAURUSLABS | +3.16% | +1.13% |
| 2 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → F_USDINR → LAURUSLABS | -1.90% | -1.10% |
| 2 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → LAURUSLABS | -5.60% | -1.01% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → LAURUSLABS | -4.50% | -0.99% |
| 1 | EV_CHINA_FDI_EASING_PN3 ⇒ T_CHINA_PLUS_ONE → LAURUSLABS | +1.20% | +0.84% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → LAURUSLABS | -2.88% | -0.81% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_FPI_FLOWS → LAURUSLABS | -2.88% | -0.72% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → LAURUSLABS | -1.80% | -0.72% |
| 1 | EV_INDIA_EU_FTA_SIGNED ⇒ T_CHINA_PLUS_ONE → LAURUSLABS | +0.60% | +0.55% |
| 1 | EV_PHARMA_GENERICS_TARIFF ⇒ P_US_PHARMA_TARIFF → LAURUSLABS | -4.50% | -0.54% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_FPI_FLOWS → LAURUSLABS | -1.60 | events | -4.80% |
| 1 | P_USFDA_ENFORCEMENT → LAURUSLABS | +1.00 | events | -4.00% |
| 1 | F_REPO_IN → LAURUSLABS | +1.00 | events | -1.80% |
| 1 | F_USDINR → LAURUSLABS | -0.37 | observed | -1.48% |
| 2 | P_US_TARIFF_INDIA → T_CHINA_PLUS_ONE → LAURUSLABS | -0.60 | events | +0.86% |
| 1 | P_US_PHARMA_TARIFF → LAURUSLABS | +0.50 | events | -0.75% |
| 2 | P_FDI_RULES → T_CHINA_PLUS_ONE → LAURUSLABS | +0.50 | events | +0.60% |
| 2 | P_USFDA_ENFORCEMENT → F_US_GENERIC_PRICING → LAURUSLABS | +1.00 | events | +0.20% |
| 2 | F_USDCNY → F_CHINA_CHEM_EXPORTS → LAURUSLABS | -0.47 | observed | +0.17% |
| 2 | F_CHINA_GDP → F_CHINA_CHEM_EXPORTS → LAURUSLABS | +0.30 | events | +0.14% |
| 2 | P_ANTI_DUMPING_IN → F_CHINA_CHEM_EXPORTS → LAURUSLABS | +0.40 | events | +0.14% |
| 2 | C_US_CHINA_DECOUPLING → T_CHINA_PLUS_ONE → LAURUSLABS | -0.10 | events | -0.13% |

## Analyst profile (agent research, sourced)
# LAURUSLABS (Laurus Labs) — Midcap, as of 2026-11-05

## Business
Laurus Labs makes APIs, finished-dose generics (notably ARV drugs for donor-funded tenders), and a fast-growing contract development and manufacturing (CDMO) business, Laurus Synthesis, plus Laurus Bio. Exports are the large majority of revenue. Q2 FY27 (reported 2026-10-29): sales Rs 2,206 cr (+33% YoY), EBITDA Rs 750 cr (34%), net profit Rs 436 cr (+126%), the sixth straight quarter of margin expansion (24% in Jun-25). Management guides to 30%+ EBITDA margin with ~Rs 3,000 cr capex (Trade Brains). It also bought 60% of Canada's Galenvs Sciences and SI&C Resins (about Rs 64 cr) and invested Rs 107.8 cr in KRKA Pharma. Segment shares are model knowledge.

## What moves the stock (ranked)
1. **China+1 / CDMO outsourcing** (T_CHINA_PLUS_ONE +6.0 per unit): the principal narrative; Nuvama sees 24% upside on the CDMO shift. A related decoupling node (C_US_CHINA_DECOUPLING +3.0) overlaps and should not be added in full.
2. **USD/INR** (+4.0 per +3%): ~85% USD/EUR revenue; the pack's +2.46 (t=1.3) is lower.
3. **USFDA enforcement on a concentrated site base** (-4.0).
4. **FPI flows** (+3.0): FII holding rose from 25.8% to 30.8% in two quarters; momentum stock (+92% in 6m).
5. **Rates/discount rate** (-1.8) at 93x P/E, **Chinese API dumping** (-1.5), **tariffs** (-1.5), **generic pricing** (-1.0).

## Transmission examples
- **US biosecurity legislation restricts Chinese CDMOs -> innovator companies move late-stage and commercial supply to India -> Laurus Synthesis order book grows -> capex fills -> margin expands** (1st to 3rd order).
- **Brent/oil shock -> INR weaker -> Laurus USD revenue translates higher, but solvents and power costs rise ~0.5% -> net EBITDA up on currency** (2nd order).
- **Fed hawkish -> US yields up -> FPI outflow from richly valued midcaps -> Laurus (FII 31%) falls -> equity cost for capex rises** (3rd order).
- **Donor funding cuts (PEPFAR/Global Fund) -> ARV tender volumes fall -> Generics revenue -15% -> offsets CDMO growth -> mix shift to CDMO accelerates** (3rd order).

## Current situation
Stock +136% in 12m and +92% in 6m, hitting a 52-week high of Rs 2,442 after Q2. Net profit tripled from FY25. The balance of risk is valuation rather than operations.

## Upcoming events
Q3 FY27 (late Jan 2027), acquisition completions (Galenvs, SI&C), capex commissioning, US policy on Chinese CDMOs.

## Bull and bear
Bull: multi-year CDMO contracts, 34% margins, EPS Rs 40+ by FY28 supports Rs 3,000. Bear: one lost contract or FDA OAI breaks the narrative; at 93x P/E, a 30% de-rating is plausible. Confidence medium: strong reported numbers but narrative and segment shares rely on headlines and model knowledge.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.