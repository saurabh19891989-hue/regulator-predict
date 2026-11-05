# GLENMARK — Glenmark Pharmaceuticals Ltd.
*MIDCAP_100 · Healthcare · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +0.3%**, **12 months +1.0%** (rank 87 / 66 of 200 for 3m / 12m); beta 0.79
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +20.8%): 3 months 51%, 12 months 45%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -2.8% … P90 +3.4%; plausible 12m relative-return range incl. stock-specific noise: -32.4% … +28.0%
- Decomposition (12m): 0.5 × forward event exposure +1.2% (3m +0.2%; half assumed priced) + 0.5 × company-specific catalysts +1.6%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply -1.6% (beta-adjusted) vs a realised market-adjusted move of +10.3% — gap -11.9 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| US generic drug price erosion (higher = worse) (`F_US_GENERIC_PRICING`) | +5 pp erosion | -3.00 | -3.00 | +0.00 | +0.00 | +0.00 | — |
| USFDA inspection/enforcement intensity (`P_USFDA_ENFORCEMENT`) | +1 = stricter | -2.90 | -3.50 | +0.60 | +0.00 | +0.00 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | +2.65 | +3.00 | -0.26 | -0.11 | +0.01 | -1.1% |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -1.42 | -1.20 | -0.17 | -0.04 | -0.01 | — |
| Africa & Latin America demand (`C_AFRICA_LATAM`) | +1 pp growth | +1.20 | +1.20 | +0.00 | +0.00 | +0.00 | — |
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +1.17 | +1.30 | +0.00 | -0.08 | -0.06 | — |
| Europe growth (`F_EU_GDP`) | +1 pp | +0.79 | +0.80 | +0.00 | -0.01 | +0.00 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +0.76 | +1.00 | -0.28 | +0.02 | +0.02 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | +0.55 | +0.00 | +0.00 | +0.56 | -0.01 | — |
| Foreign portfolio flows into Indian government/corporate bonds (FAR, index-linked) (`NEW_FPI_DEBT_FLOWS`) | +US$5 bn net debt inflow per quarter | -0.53 | +0.00 | -0.60 | +0.05 | +0.02 | — |
| India real GDP growth (`F_GDP_IN`) | +1 pp | -0.53 | +0.00 | -0.49 | +0.00 | -0.04 | — |
| Brent crude oil price (`F_BRENT`) | +10% Brent | +0.46 | +0.00 | +0.50 | -0.01 | -0.03 | +0.0% |
| US tariffs on pharmaceuticals (`P_US_PHARMA_TARIFF`) | +10 pp on Indian pharma exports | -0.44 | -0.80 | +0.36 | +0.00 | +0.00 | — |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +0.38 | +0.00 | +0.36 | +0.08 | -0.06 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| USFDA warning letters: Alembic, Aurobindo-Eugia, Dabur (Jul-Aug 2026) (`EV_USFDA_WARNING_WAVE_26`) | occurred | 1.00 | -2.9% | -2.9% | -3.5 | +0.6 | +0.0 | +0.0 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -1.7% | -1.7% | -2.2 | +0.6 | -0.0 | -0.0 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -1.4% | -1.4% | -1.2 | -0.2 | -0.0 | -0.0 |
| Rupee at 95-96/USD and heavy RBI FX defence; reserves fall ~US$55bn from peak (`EV_RUPEE_DEFENCE_RESERVES_26`) | occurred | 1.00 | -1.0% | -1.0% | -1.1 | +0.1 | +0.0 | -0.0 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +1.8% | +0.9% | +2.5 | -0.8 | +0.0 | +0.0 |
| US imposes tariffs on generic drugs (200% threat) or removes India's speciality exemption (`EV_PHARMA_GENERICS_TARIFF`) | risk_scenario | 0.12 | -5.4% | -0.6% | -5.4 | +0.0 | +0.0 | +0.0 |
| RBI MPC Dec 2026 (~4 Dec): hikes repo another 25 bp to 5.75% (`EV_RBI_DEC26_HIKE25`) | scheduled | 0.42 | -1.4% | -0.6% | -1.2 | -0.2 | -0.0 | -0.0 |
| RBI MPC Feb 2027 (~5 Feb, just after Budget): hikes 25 bp (`EV_RBI_FEB27_HIKE25`) | scheduled | 0.27 | -1.4% | -0.4% | -1.2 | -0.2 | -0.0 | -0.0 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -0.4% | -0.4% | +0.0 | -0.3 | -0.0 | +0.0 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.55 | -0.6% | -0.3% | +0.0 | -0.6 | +0.0 | +0.0 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -0.3% | -0.3% | +0.0 | -0.3 | +0.0 | -0.0 |
| US midterms (3 Nov 2026): Democrats win House and Senate (`EV_US_MIDTERMS_DEM_SWEEP`) | occurred | 1.00 | +0.3% | +0.3% | +0.5 | -0.2 | -0.0 | +0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → GLENMARK | +2.50% | +1.25% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_USDINR → GLENMARK | +3.90% | +0.70% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → GLENMARK | -1.20% | -0.50% |
| 2 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → F_USDINR → GLENMARK | -0.80% | -0.44% |
| 1 | EV_PHARMA_GENERICS_TARIFF ⇒ F_US_GENERIC_PRICING → GLENMARK | -3.00% | -0.36% |
| 2 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → F_USDINR → GLENMARK | -0.69% | -0.35% |
| 2 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → F_USDINR → GLENMARK | +1.36% | +0.34% |
| 1 | EV_RBI_FEB27_HIKE25 ⇒ F_REPO_IN → GLENMARK | -1.20% | -0.32% |
| 1 | EV_PHARMA_GENERICS_TARIFF ⇒ P_US_PHARMA_TARIFF → GLENMARK | -2.40% | -0.29% |
| 1 | EV_CPI_BREACH_6PCT ⇒ F_REPO_IN → GLENMARK | -0.48% | -0.29% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → GLENMARK | -1.50% | -0.27% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → GLENMARK | -0.96% | -0.24% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_FPI_FLOWS → GLENMARK | -0.96% | -0.24% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → GLENMARK | -0.93% | -0.23% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → F_USDINR → GLENMARK | +0.90% | +0.22% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_FPI_FLOWS → GLENMARK | -1.60 | events | -1.60% |
| 1 | P_USFDA_ENFORCEMENT → GLENMARK | +0.40 | director_override | -1.40% |
| 1 | F_REPO_IN → GLENMARK | +1.00 | events | -1.20% |
| 1 | F_USDINR → GLENMARK | -0.37 | observed | -1.11% |
| 1 | F_URBAN_DEMAND → GLENMARK | +0.20 | events | +0.26% |
| 2 | P_USFDA_ENFORCEMENT → F_US_GENERIC_PRICING → GLENMARK | +0.40 | director_override | +0.24% |
| 2 | F_DXY → C_AFRICA_LATAM → GLENMARK | +0.74 | observed | -0.21% |
| 1 | F_EU_GDP → GLENMARK | +0.22 | events | +0.18% |
| 1 | P_US_PHARMA_TARIFF → GLENMARK | +0.20 | events | -0.16% |
| 2 | P_US_PHARMA_TARIFF → F_US_GENERIC_PRICING → GLENMARK | +0.20 | events | +0.07% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-11-12 | Q2 FY27 results (date unverified; trading window closed 2026-09-28) | results | 0.95 | +0.0% | +0.00% |
| 2026-12-06 | IGI/partner presents updated ISB 2001 data at ASH meeting | other | 0.90 | +1.0% | +0.90% |
| 2027-02 | Q3 FY27 results | results | 0.95 | +0.0% | +0.00% |
| 2027-03 | USFDA inspections of Monroe/Baddi/Indore sites | regulatory | 0.30 | -3.5% | -1.05% |
| 2027-06 | Next ISB 2001 milestone payments / trial progress from AbbVie (timing not disclosed) | other | 0.30 | +6.0% | +1.80% |

## Analyst profile (agent research, sourced)
# GLENMARK (Glenmark Pharmaceuticals) — Midcap, as of 2026-11-05

## Business
Glenmark sells generics, branded products and OTC in about 80 countries: India roughly 42%, North America 25%, Europe 13% and the rest of the world 20% (model-knowledge shares). Its equity story increasingly rests on Ichnos Glenmark Innovation (IGI), whose trispecific antibody ISB 2001 was licensed to AbbVie in 2025 (terms from model knowledge). Reported quarterly profit is therefore lumpy: Sep-25 PAT -Rs 739 cr, Dec-25 +Rs 282 cr, Mar-26 -Rs 74 cr, Jun-26 +Rs 736 cr. TTM sales are Rs 8,480 cr (-9%) with an 11% margin, and the stock trades at 48x TTM EPS and 2.9x book after +36% in a year. Q2 FY27 results are pending (trading window closed 2026-09-28) and are not in the pack.

## What moves the stock (ranked)
1. **Innovation/licensing news** (event-specific rather than macro): IGI's partner presents updated ISB 2001 data at ASH (announced 2026-11-04) and AbbVie milestones can swing value by 5-10% of market cap each; there is no driver node, so this sits in company_events.
2. **USD/INR** (+3.0 per +3%): the pack's only |t|>2 factor (+3.87, t=2.4); model gives a slightly lower +3.0.
3. **USFDA enforcement** (-3.5): Goa received VAI on 2026-09-23.
4. **US generic pricing** (-3.0) and **tariff risk** (-0.8).
5. **EM and Europe demand** (+1.2, +0.8), **India urban demand** (+1.3), **rates** (-1.2), **FPI flows** (+1.0).

## Transmission examples
- **Fed hawkish -> USD stronger -> INR weaker -> Glenmark USD/EUR-linked earnings and licensing receipts translate higher -> EBITDA up** (2nd order); also Brent up -> INR weaker, so Brent shocks help via currency while raising freight.
- **ISB 2001 data positive at ASH -> AbbVie triggers milestone -> Glenmark receives cash and reduces net debt -> ROE rises from 4% and the P/B 2.9x premium is justified** (1st to 3rd order).
- **USFDA OAI at Baddi/Indore -> US filings delayed -> US sales -5% -> margin compresses -> 48x P/E collapses** (2nd to 3rd order).
- **Strong Latin American demand/ Brazil Ryaltris launch -> EM sales +20% -> margin accretion -> global OTC mix improves** (3rd order).

## Current situation
Stock +8.5% in 1m, +36% in 12m. Catalysts since August: fluticasone nasal spray approval (2026-08-20), Brazil Ryaltris launch (2026-09-11), Goa VAI (2026-09-23), US adapalene launch (2026-10-06) and IGI ASH data (2026-11-04). The big unknown is the Q2 print and how licensing income is booked.

## Upcoming events
Q2 FY27 results (mid-Nov, unverified), ASH presentation (December), Q3 results (Feb 2027), AbbVie milestone news.

## Bull and bear
Bull: ISB 2001 de-risks, EM launches scale, EBITDA margin 22-25% on Rs 9,500 cr sales = EPS Rs 45+, making 48x TTM look 25x forward. Bear: weak Q2 core earnings, adverse ISB 2001 trial data, USFDA action; stock trades back to book value x 2 (Rs 1,800). Confidence low: segment shares, deal terms from model knowledge, and Q2 not available.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.