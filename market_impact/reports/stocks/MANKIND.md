# MANKIND — Mankind Pharma Ltd.
*MIDCAP_100 · Healthcare · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -1.6%**, **12 months -1.8%** (rank 143 / 126 of 200 for 3m / 12m); beta 0.65
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +26.0%): 3 months 45%, 12 months 50%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -4.9% … P90 +0.3%; plausible 12m relative-return range incl. stock-specific noise: -27.8% … +26.9%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +0.0 pp (model impact +1.7% beta-adjusted vs realised market-adjusted move +4.9%); forward event exposure -0.7% (3m -0.9%; half assumed priced); company-specific events -0.5%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| India NPPA/NLEM drug price control and trade-margin regulation (`NEW_NPPA_DRUG_PRICE_CONTROL`) | +1 = one tightening step (NLEM expansion or trade-margin cap) | -3.00 | -3.00 | +0.00 | +0.00 | +0.00 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -2.61 | +0.00 | -2.27 | -0.20 | -0.13 | — |
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +2.08 | +2.00 | +0.32 | -0.17 | -0.07 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -2.04 | -1.80 | -0.10 | -0.11 | -0.02 | — |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -1.40 | +0.00 | +0.00 | -1.33 | -0.07 | — |
| Consumer premiumisation (`T_PREMIUMISATION`) | +1 | +1.39 | +1.30 | +0.08 | +0.02 | -0.02 | — |
| US dollar index (`F_DXY`) | +3% DXY | +1.34 | +1.50 | -0.11 | -0.01 | -0.04 | +2.2% |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +1.34 | +0.00 | +0.56 | +0.94 | -0.16 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -1.22 | +0.00 | +0.00 | -0.75 | -0.47 | — |
| Brent crude oil price (`F_BRENT`) | +10% Brent | -1.13 | +0.00 | -0.64 | -0.35 | -0.15 | +0.0% |
| India real GDP growth (`F_GDP_IN`) | +1 pp | +0.99 | +1.60 | -0.46 | -0.08 | -0.07 | — |
| Monsoon rainfall vs normal (`F_MONSOON`) | +10% above long-period average | +0.81 | +0.00 | +0.43 | -0.01 | +0.40 | — |
| Chemical feedstock (benzene, propylene, etc.) (`F_CHEM_FEEDSTOCK`) | +10% feedstock | -0.80 | -0.80 | +0.00 | +0.00 | +0.00 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +0.79 | +0.80 | -0.06 | +0.01 | +0.04 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -5.8% | -5.8% | +0.0 | -3.2 | -1.8 | -0.8 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -3.0% | -3.0% | +0.0 | -2.6 | -0.3 | -0.1 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -2.1% | -2.1% | -1.8 | -0.1 | -0.2 | -0.0 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -1.7% | -1.7% | -1.8 | +0.2 | -0.0 | -0.1 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.36 | -3.2% | -1.2% | +0.0 | -1.7 | -1.0 | -0.5 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.58 | +1.9% | +1.1% | +0.0 | +1.0 | +0.6 | +0.3 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -1.0% | -1.0% | +0.0 | -0.5 | +0.0 | -0.5 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +1.9% | +1.0% | +2.0 | -0.2 | +0.0 | +0.1 |
| Gold and silver slump from January 2026 peaks (silver -53%, gold -24%) (`EV_PRECIOUS_METALS_CRASH_2026`) | occurred | 1.00 | +0.9% | +0.9% | +1.0 | -0.3 | +0.2 | -0.1 |
| India Q1 FY27 GDP grows 7.8% (31 Aug 2026), beating ~7.3% consensus (`EV_GDP_Q1FY27_7_8`) | occurred | 1.00 | +0.9% | +0.9% | +1.2 | -0.2 | -0.1 | -0.0 |
| RBI MPC Dec 2026 (~4 Dec): hikes repo another 25 bp to 5.75% (`EV_RBI_DEC26_HIKE25`) | scheduled | 0.40 | -2.1% | -0.8% | -1.8 | -0.1 | -0.2 | -0.0 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | +0.8% | +0.8% | +1.1 | -0.3 | +0.1 | +0.0 |

## Strongest causal chains (1st–4th order)
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_CHEM_FEEDSTOCK → MANKIND | -2.69% | -2.69% |
| 2 | EV_CPI_REACCEL_SEP26 ⇒ F_CPI_IN → F_REPO_IN → MANKIND | -2.38% | -2.38% |
| 1 | EV_RBI_OCT26_HIKE25 ⇒ F_REPO_IN → MANKIND | -1.80% | -1.80% |
| 1 | EV_FPI_RECORD_OUTFLOW_26 ⇒ F_FPI_FLOWS → MANKIND | -1.76% | -1.76% |
| 3 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_CPI_IN → F_REPO_IN → MANKIND | -1.59% | -1.59% |
| 1 | EV_UST_SELLOFF_SEP26 ⇒ F_DXY → MANKIND | +1.09% | +1.09% |
| 1 | EV_PRECIOUS_METALS_CRASH_2026 ⇒ F_DXY → MANKIND | +1.05% | +1.05% |
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → MANKIND | +2.00% | +1.00% |
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_GDP_IN → MANKIND | -0.95% | -0.95% |
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_USDINR → MANKIND | +0.94% | +0.94% |
| 1 | EV_GDP_Q1FY27_7_8 ⇒ F_GDP_IN → MANKIND | +0.80% | +0.80% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → MANKIND | -1.80% | -0.72% |
| 3 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_GDP_IN → F_REPO_IN → MANKIND | +0.64% | +0.64% |
| 1 | EV_FED_SEP26_HIKE ⇒ F_DXY → MANKIND | +0.60% | +0.60% |
| 4 | EV_SWMONSOON26_DEFICIT ⇒ F_MONSOON → F_FOOD_INFLATION_IN → F_CPI_IN → F_REPO_IN → MANKIND | -0.58% | -0.58% |

## Analyst profile (agent research, sourced)
# MANKIND (Mankind Pharma) — Midcap, as of 2026-11-05

## Business
Mankind is an India-focused pharma company with ~15.2% prescription share, a ~15,000-strong field force, chronic and acute portfolios, consumer healthcare brands (Manforce, Prega News and others) and, since 2024, Bharat Serums & Vaccines (BSV) in women's health and critical care. Exports are small (about 50 US launches). Promoters own 72.6%. Q2 FY27 (2026-10-26): revenue +17% to ~Rs 3,145 cr, EBITDA margin ~30% (+300bp YoY), net profit ~Rs 711-716 cr (+37-39%, press; the pack's Rs 582 cr differs and is probably before an exceptional or other-income line). On 2026-10-15 it agreed to buy 70% of Belgian CAR-T company ACTx for EUR 48m.

## What moves the stock (ranked)
1. **Pharma marketing and pricing regulation** (-3.0 per step; new node NEW_P_PHARMA_MARKETING_PRICE_REG): the Supreme Court on 2026-10-08 told the Centre to form an expert panel on unethical marketing and freebies, and it is pressing for MRP/trade-margin caps; Mankind fell up to 3%.
2. **Urban demand and GDP** (+2.0, +1.6): consumer health and acute therapies are discretionary-sensitive.
3. **Rates/discount rate** (-1.8) on a 43x P/E.
4. **Raw-material inflation** (-0.8), **FPI flows** (+0.8), **USD/INR** (+0.6).
5. Pack signals: DXY +1.80 (t=1.7) and edible oil -1.83 (t=-1.5) are weak and likely rotation effects; the edible-oil link has no cost-basis here.

## Transmission examples
- **SC panel on marketing -> UCPMP becomes binding -> Mankind cuts doctor engagement spending/ reps productivity falls -> IPM share gains slow -> revenue growth 17% -> 13%** (1st to 3rd order).
- **Petrochemical feedstock up (Brent up) -> excipients, solvents, packaging up -> RM costs +2% -> NLEM price pass-through only annual -> margin -100bp** (2nd order); simultaneously Brent up -> INR weaker -> RM imports dearer (3rd order).
- **Fed/Indian yields up -> BSV debt cost and multiple pressure -> 43x P/E derates** (2nd to 3rd order).
- **Strong monsoon -> rural incomes -> acute/seasonal and OTC volumes up -> chronic diagnosis rate up** (3rd order).

## Current situation
Stock +8% on 2026-10-27 after an earnings beat; brokers split (Kotak Buy TP Rs 3,000, Jefferies Buy, others flag valuation). Interest costs fell from Rs 149 cr to Rs 88 cr a quarter. Valuation is the main debate.

## Upcoming events
SC-mandated panel (Dec), Q3 results (Jan 2027), ACTx closing, NPPA annual price revision (April).

## Bull and bear
Bull: 15%+ IPM-beating growth, 32% margin, deleveraging; EPS Rs 70 by FY28 supports Rs 3,000. Bear: marketing code binds, trade-margin caps, BSV disappointment, 43x multiple compresses to 30x. Confidence medium; PAT basis mismatch flagged.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.