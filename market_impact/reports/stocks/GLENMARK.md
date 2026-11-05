# GLENMARK — Glenmark Pharmaceuticals Ltd.
*MIDCAP_100 · Healthcare · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -0.6%**, **12 months -0.6%** (rank 122 / 117 of 200 for 3m / 12m); beta 0.79
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +20.8%): 3 months 48%, 12 months 50%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -5.7% … P90 +4.6%; plausible 12m relative-return range incl. stock-specific noise: -30.7% … +32.4%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves -1.8 pp (model impact -3.5% beta-adjusted vs realised market-adjusted move +10.3%); forward event exposure +2.9% (3m +1.5%; half assumed priced); company-specific events +1.6%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| US generic drug price erosion (higher = worse) (`F_US_GENERIC_PRICING`) | +5 pp erosion | -3.00 | -3.00 | +0.00 | +0.00 | +0.00 | — |
| USFDA inspection/enforcement intensity (`P_USFDA_ENFORCEMENT`) | +1 = stricter | -2.90 | -3.50 | +0.60 | +0.00 | +0.00 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | +2.57 | +3.00 | -0.26 | -0.16 | -0.01 | -1.1% |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -1.42 | -1.20 | -0.17 | -0.04 | -0.01 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -1.39 | +0.00 | -0.99 | -0.34 | -0.06 | — |
| Africa & Latin America demand (`C_AFRICA_LATAM`) | +1 pp growth | +1.20 | +1.20 | +0.00 | +0.00 | +0.00 | — |
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +1.15 | +1.30 | +0.00 | -0.08 | -0.08 | — |
| India real GDP growth (`F_GDP_IN`) | +1 pp | -0.92 | +0.00 | -0.49 | -0.28 | -0.16 | — |
| Europe growth (`F_EU_GDP`) | +1 pp | +0.79 | +0.80 | +0.00 | -0.01 | +0.00 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +0.77 | +1.00 | -0.28 | +0.02 | +0.03 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | +0.72 | +0.00 | +0.00 | +0.93 | -0.21 | — |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -0.71 | +0.00 | +0.00 | -0.55 | -0.17 | — |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +0.64 | +0.00 | +0.36 | +0.26 | +0.02 | — |
| Brent crude oil price (`F_BRENT`) | +10% Brent | +0.52 | +0.00 | +0.83 | -0.19 | -0.12 | +0.0% |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| USFDA warning letters: Alembic, Aurobindo-Eugia, Dabur (Jul-Aug 2026) (`EV_USFDA_WARNING_WAVE_26`) | occurred | 1.00 | -2.9% | -2.9% | -3.5 | +0.6 | +0.0 | +0.0 |
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | +2.6% | +2.6% | +0.0 | +4.1 | -0.9 | -0.6 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -1.6% | -1.6% | +0.0 | -1.1 | -0.4 | -0.0 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -1.6% | -1.6% | -2.2 | +0.8 | -0.0 | -0.1 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -1.4% | -1.4% | -1.2 | -0.2 | -0.0 | -0.0 |
| Rupee at 95-96/USD and heavy RBI FX defence; reserves fall ~US$55bn from peak (`EV_RUPEE_DEFENCE_RESERVES_26`) | occurred | 1.00 | -1.0% | -1.0% | -1.1 | +0.1 | +0.1 | -0.0 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +1.8% | +0.9% | +2.5 | -0.8 | +0.0 | +0.1 |
| US imposes tariffs on generic drugs (200% threat) or removes India's speciality exemption (`EV_PHARMA_GENERICS_TARIFF`) | risk_scenario | 0.12 | -5.4% | -0.6% | -5.4 | +0.0 | +0.0 | +0.0 |
| RBI MPC Dec 2026 (~4 Dec): hikes repo another 25 bp to 5.75% (`EV_RBI_DEC26_HIKE25`) | scheduled | 0.40 | -1.4% | -0.6% | -1.2 | -0.2 | -0.0 | -0.0 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.36 | +1.3% | +0.5% | +0.0 | +2.1 | -0.5 | -0.3 |
| US waives Russia-oil secondary sanctions/100% tariff threat on buyers incl. India (17 Oct) (`EV_RUSSIA_WAIVER_OCT17`) | occurred | 1.00 | -0.5% | -0.5% | +0.0 | -0.1 | -0.4 | +0.1 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.58 | -0.8% | -0.5% | +0.0 | -1.2 | +0.3 | +0.2 |

## Strongest causal chains (1st–4th order)
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_USDINR → GLENMARK | +4.69% | +4.69% |
| 1 | EV_USFDA_WARNING_WAVE_26 ⇒ P_USFDA_ENFORCEMENT → GLENMARK | -3.50% | -3.50% |
| 1 | EV_FPI_RECORD_OUTFLOW_26 ⇒ F_FPI_FLOWS → GLENMARK | -2.20% | -2.20% |
| 2 | EV_CPI_REACCEL_SEP26 ⇒ F_CPI_IN → F_REPO_IN → GLENMARK | -1.59% | -1.59% |
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → GLENMARK | +2.50% | +1.25% |
| 1 | EV_RBI_OCT26_HIKE25 ⇒ F_REPO_IN → GLENMARK | -1.20% | -1.20% |
| 1 | EV_RUPEE_DEFENCE_RESERVES_26 ⇒ F_USDINR → GLENMARK | -1.11% | -1.11% |
| 3 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_CPI_IN → F_REPO_IN → GLENMARK | -1.06% | -1.06% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_USDINR → GLENMARK | +3.90% | +0.86% |
| 2 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → F_USDINR → GLENMARK | +2.37% | +0.85% |
| 2 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → F_USDINR → GLENMARK | -1.42% | -0.83% |
| 2 | EV_CPI_REACCEL_SEP26 ⇒ F_CPI_IN → F_USDINR → GLENMARK | +0.69% | +0.69% |
| 2 | EV_FPI_RECORD_OUTFLOW_26 ⇒ F_FPI_FLOWS → F_USDINR → GLENMARK | +0.61% | +0.61% |
| 2 | EV_USFDA_WARNING_WAVE_26 ⇒ P_USFDA_ENFORCEMENT → F_US_GENERIC_PRICING → GLENMARK | +0.60% | +0.60% |
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_FPI_FLOWS → GLENMARK | -0.59% | -0.59% |

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