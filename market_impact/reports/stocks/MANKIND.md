# MANKIND — Mankind Pharma Ltd.
*MIDCAP_100 · Healthcare · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -0.6%**, **12 months -0.5%** (rank 162 / 127 of 200 for 3m / 12m); beta 0.65
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +26.0%): 3 months 48%, 12 months 49%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -2.3% … P90 +0.9%; plausible 12m relative-return range incl. stock-specific noise: -35.8% … +30.3%
- Decomposition (12m): 0.5 × forward event exposure -0.0% (3m -0.1%; half assumed priced; market-priced macro drift removed) + 0.5 × company-specific catalysts -0.5%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply +1.5% (beta-adjusted) vs a realised market-adjusted move of +4.9% — gap -3.4 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| India NPPA/NLEM drug price control and trade-margin regulation (`NEW_NPPA_DRUG_PRICE_CONTROL`) | +1 = one tightening step (NLEM expansion or trade-margin cap) | -3.00 | -3.00 | +0.00 | +0.00 | +0.00 | — |
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +2.24 | +2.00 | +0.32 | -0.04 | -0.03 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -2.03 | -1.80 | -0.10 | -0.11 | -0.01 | — |
| India real GDP growth (`F_GDP_IN`) | +1 pp | +1.49 | +1.60 | -0.12 | +0.04 | -0.03 | — |
| US dollar index (`F_DXY`) | +3% DXY | +1.42 | +1.50 | -0.06 | -0.01 | -0.01 | +2.2% |
| Consumer premiumisation (`T_PREMIUMISATION`) | +1 | +1.40 | +1.30 | +0.08 | +0.02 | -0.01 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -1.16 | +0.00 | -1.24 | +0.05 | +0.02 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -1.11 | +0.00 | +0.00 | -0.83 | -0.28 | — |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +1.08 | +0.00 | +0.56 | +0.58 | -0.06 | — |
| Private corporate capex (`F_PRIVATE_CAPEX`) | +10% capex growth | +1.03 | +0.00 | +1.02 | -0.02 | +0.03 | — |
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | +1.00 | +0.00 | +1.02 | -0.06 | +0.03 | — |
| Monsoon rainfall vs normal (`F_MONSOON`) | +10% above long-period average | +0.95 | +0.00 | +0.43 | +0.19 | +0.33 | — |
| Brent crude oil price (`F_BRENT`) | +10% Brent | -0.92 | +0.00 | -0.71 | -0.21 | -0.00 | +0.0% |
| Chemical feedstock (benzene, propylene, etc.) (`F_CHEM_FEEDSTOCK`) | +10% feedstock | -0.80 | -0.80 | +0.00 | +0.00 | +0.00 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -2.1% | -2.1% | -1.8 | -0.1 | -0.1 | -0.0 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -1.7% | -1.7% | -1.8 | +0.1 | -0.0 | -0.0 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -1.4% | -1.4% | +0.0 | -1.4 | -0.0 | +0.0 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -1.2% | -1.2% | +0.0 | -0.5 | -0.2 | -0.4 |
| India Q1 FY27 GDP grows 7.8% (31 Aug 2026), beating ~7.3% consensus (`EV_GDP_Q1FY27_7_8`) | occurred | 1.00 | +1.1% | +1.1% | +1.2 | -0.1 | -0.0 | -0.0 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +1.9% | +0.9% | +2.0 | -0.2 | +0.0 | +0.0 |
| RBI MPC Dec 2026 (~4 Dec): hikes repo another 25 bp to 5.75% (`EV_RBI_DEC26_HIKE25`) | scheduled | 0.42 | -2.1% | -0.9% | -1.8 | -0.1 | -0.1 | -0.0 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.55 | +1.3% | +0.7% | +0.0 | +1.0 | +0.3 | +0.0 |
| Risk: stagflation scare - CPI >=6.5% while GDP growth slips below ~6% (Q3 FY27 data, late Feb 2027) (`EV_INDIA_STAGFLATION_SCARE`) | risk_scenario | 0.12 | -4.8% | -0.6% | -4.2 | -0.5 | -0.1 | -0.0 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.25 | -2.3% | -0.6% | +0.0 | -1.7 | -0.6 | -0.0 |
| RBI MPC Feb 2027 (~5 Feb, just after Budget): hikes 25 bp (`EV_RBI_FEB27_HIKE25`) | scheduled | 0.27 | -2.0% | -0.6% | -1.8 | -0.1 | -0.1 | -0.0 |
| IMD April 2027 long-range forecast says normal or above-normal monsoon (>=96% LPA) (`EV_MONSOON27_FIRST_FORECAST_NORMAL`) | scheduled | 0.68 | +0.8% | +0.5% | +0.0 | +0.4 | +0.3 | +0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → MANKIND | +2.00% | +1.00% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → MANKIND | -1.80% | -0.76% |
| 1 | EV_RBI_FEB27_HIKE25 ⇒ F_REPO_IN → MANKIND | -1.80% | -0.49% |
| 2 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → F_CHEM_FEEDSTOCK → MANKIND | +0.71% | +0.39% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_REPO_IN → MANKIND | -1.80% | -0.32% |
| 1 | EV_FED_DEC26_HIKE25 ⇒ F_DXY → MANKIND | +0.45% | +0.32% |
| 2 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → F_CHEM_FEEDSTOCK → MANKIND | -1.20% | -0.30% |
| 2 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_GDP_IN → MANKIND | +0.43% | +0.29% |
| 1 | EV_INDIA_STAGFLATION_SCARE ⇒ F_GDP_IN → MANKIND | -2.40% | -0.29% |
| 1 | EV_Q2_FY27_GDP_STRONG ⇒ F_GDP_IN → MANKIND | +0.32% | +0.26% |
| 1 | EV_FED_H1_2027_FURTHER_HIKES ⇒ F_DXY → MANKIND | +0.60% | +0.24% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → MANKIND | -1.20% | -0.22% |
| 1 | EV_INDIA_STAGFLATION_SCARE ⇒ F_REPO_IN → MANKIND | -1.80% | -0.22% |
| 2 | EV_BUDGET27_AGRI_RURAL ⇒ F_RURAL_DEMAND → F_GDP_IN → MANKIND | +0.31% | +0.22% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → MANKIND | -0.77% | -0.19% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_REPO_IN → MANKIND | +1.00 | events | -1.80% |
| 1 | F_FPI_FLOWS → MANKIND | -1.60 | events | -1.28% |
| 1 | F_DXY → MANKIND | +0.74 | observed | +1.11% |
| 1 | F_GDP_IN → MANKIND | +0.50 | events | +0.80% |
| 1 | F_URBAN_DEMAND → MANKIND | +0.20 | events | +0.40% |
| 1 | F_USDINR → MANKIND | -0.37 | observed | -0.22% |
| 2 | P_ANTI_DUMPING_IN → F_CHEM_FEEDSTOCK → MANKIND | +0.40 | events | -0.06% |
| 2 | F_BRENT → F_CHEM_FEEDSTOCK → MANKIND | +0.00 | observed | -0.00% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-12 | Supreme Court-mandated expert panel on pharma marketing practices (setup/terms) | regulatory | 0.60 | -2.0% | -1.20% |
| 2027-01 | Q3 FY27 results: IPM growth, BSV integration, margin vs 30% | results | 0.95 | +0.5% | +0.47% |
| 2027-03 | Completion of ACTx 70% acquisition (EUR 48m, Rs 511 cr) | corporate_action | 0.80 | +0.0% | +0.00% |
| 2027-04 | Annual NLEM / NPPA price revision (WPI-linked) | regulatory | 0.90 | +0.2% | +0.23% |

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