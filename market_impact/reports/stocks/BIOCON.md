# BIOCON — Biocon Ltd.
*MIDCAP_100 · Healthcare · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -1.2%**, **12 months -2.4%** (rank 171 / 172 of 200 for 3m / 12m); beta 1.01
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +24.3%): 3 months 46%, 12 months 50%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -10.0% … P90 +1.1%; plausible 12m relative-return range incl. stock-specific noise: -36.7% … +33.3%
- Decomposition (12m): 0.5 × forward event exposure -2.3% (3m -2.3%; half assumed priced) + 0.5 × company-specific catalysts -1.7%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply -4.6% (beta-adjusted) vs a realised market-adjusted move of -19.6% — gap +15.0 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | +4.27 | +5.00 | -0.36 | -0.24 | -0.13 | -1.1% |
| USFDA inspection/enforcement intensity (`P_USFDA_ENFORCEMENT`) | +1 = stricter | -3.50 | -4.00 | +0.50 | +0.00 | +0.00 | — |
| GLP-1 / obesity drug adoption (`T_GLP1`) | +1 | +3.00 | +3.00 | +0.00 | +0.00 | +0.00 | — |
| US tariffs on pharmaceuticals (`P_US_PHARMA_TARIFF`) | +10 pp on Indian pharma exports | -2.70 | -3.00 | +0.30 | +0.00 | +0.00 | — |
| US generic drug price erosion (higher = worse) (`F_US_GENERIC_PRICING`) | +5 pp erosion | -2.50 | -2.50 | +0.00 | +0.00 | +0.00 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -2.04 | -1.50 | -0.52 | -0.01 | -0.01 | — |
| India 10-year G-sec yield (`F_GSEC_10Y_IN`) | +25 bp yield | -1.49 | -1.50 | +0.00 | +0.00 | +0.01 | — |
| US Fed funds rate (`F_FED_FUNDS`) | +25 bp | -1.31 | -1.00 | -0.15 | -0.22 | +0.05 | +11.2% |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +1.16 | +1.50 | -0.40 | +0.02 | +0.04 | — |
| US growth (`F_US_GDP`) | +1 pp | +1.07 | +1.50 | -0.24 | +0.02 | -0.21 | — |
| India real GDP growth (`F_GDP_IN`) | +1 pp | -1.00 | +0.00 | -0.54 | -0.34 | -0.13 | — |
| Chemical feedstock (benzene, propylene, etc.) (`F_CHEM_FEEDSTOCK`) | +10% feedstock | -1.00 | -1.00 | +0.00 | +0.00 | +0.00 | — |
| Europe growth (`F_EU_GDP`) | +1 pp | +0.77 | +0.80 | +0.00 | -0.01 | -0.02 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -0.65 | +0.00 | -0.22 | -0.42 | -0.01 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| USFDA warning letters: Alembic, Aurobindo-Eugia, Dabur (Jul-Aug 2026) (`EV_USFDA_WARNING_WAVE_26`) | occurred | 1.00 | -3.5% | -3.5% | -4.0 | +0.5 | +0.0 | +0.0 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -2.6% | -2.6% | -3.3 | +0.9 | -0.0 | -0.1 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -2.2% | -2.2% | -1.9 | -0.2 | -0.0 | -0.0 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -2.1% | -2.1% | -2.1 | +0.0 | +0.0 | +0.0 |
| Rupee at 95-96/USD and heavy RBI FX defence; reserves fall ~US$55bn from peak (`EV_RUPEE_DEFENCE_RESERVES_26`) | occurred | 1.00 | -1.7% | -1.7% | -1.9 | +0.1 | +0.1 | +0.0 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -1.5% | -1.5% | -1.0 | -0.5 | +0.0 | +0.0 |
| US imposes tariffs on generic drugs (200% threat) or removes India's speciality exemption (`EV_PHARMA_GENERICS_TARIFF`) | risk_scenario | 0.12 | -11.5% | -1.4% | -11.5 | +0.0 | +0.0 | +0.0 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +2.7% | +1.3% | +3.8 | -1.2 | +0.1 | +0.1 |
| US Q3 data: GDP 3.4%, CPI 3.7%, September payrolls only +29k (`EV_US_Q3_DATA_MIXED`) | occurred | 1.00 | +1.3% | +1.3% | +1.3 | +0.1 | -0.0 | -0.1 |
| RBI MPC Dec 2026 (~4 Dec): hikes repo another 25 bp to 5.75% (`EV_RBI_DEC26_HIKE25`) | scheduled | 0.42 | -2.2% | -0.9% | -1.9 | -0.2 | -0.0 | -0.0 |
| FOMC 8-9 Dec 2026: 25 bp hike to 4.00-4.25% (`EV_FED_DEC26_HIKE25`) | scheduled | 0.72 | -1.3% | -0.9% | -1.0 | -0.2 | -0.0 | +0.0 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -0.7% | -0.7% | +0.0 | -0.3 | -0.5 | +0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → BIOCON | +3.75% | +1.88% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_USDINR → BIOCON | +6.50% | +1.17% |
| 1 | EV_US_RECESSION_RISK_2027 ⇒ F_US_GDP → BIOCON | -4.50% | -1.12% |
| 1 | EV_PHARMA_GENERICS_TARIFF ⇒ P_US_PHARMA_TARIFF → BIOCON | -9.00% | -1.08% |
| 1 | EV_US_RECESSION_RISK_2027 ⇒ F_FED_FUNDS → BIOCON | +3.00% | +0.75% |
| 2 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → F_USDINR → BIOCON | -1.34% | -0.74% |
| 1 | EV_FED_DEC26_HIKE25 ⇒ F_FED_FUNDS → BIOCON | -1.00% | -0.72% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → BIOCON | -1.50% | -0.63% |
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → BIOCON | -1.20% | -0.60% |
| 2 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → F_USDINR → BIOCON | -1.15% | -0.58% |
| 2 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → F_USDINR → BIOCON | +2.27% | +0.57% |
| 2 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → F_CHEM_FEEDSTOCK → BIOCON | +0.88% | +0.49% |
| 1 | EV_CPI_BREACH_6PCT ⇒ F_GSEC_10Y_IN → BIOCON | -0.75% | -0.45% |
| 1 | EV_RBI_FEB27_HIKE25 ⇒ F_REPO_IN → BIOCON | -1.50% | -0.41% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → BIOCON | -2.25% | -0.40% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_FPI_FLOWS → BIOCON | -1.60 | events | -2.40% |
| 1 | F_GSEC_10Y_IN → BIOCON | +1.55 | director_override | -2.33% |
| 1 | F_USDINR → BIOCON | -0.37 | observed | -1.85% |
| 1 | F_US_GDP → BIOCON | +1.20 | events | +1.80% |
| 1 | F_FED_FUNDS → BIOCON | +1.62 | observed | -1.62% |
| 1 | P_USFDA_ENFORCEMENT → BIOCON | +0.40 | director_override | -1.60% |
| 1 | F_REPO_IN → BIOCON | +1.00 | events | -1.50% |
| 1 | T_GLP1 → BIOCON | +0.30 | director_override | +0.90% |
| 1 | P_US_PHARMA_TARIFF → BIOCON | +0.20 | events | -0.60% |
| 2 | P_USFDA_ENFORCEMENT → F_US_GENERIC_PRICING → BIOCON | +0.40 | director_override | +0.20% |
| 1 | F_EU_GDP → BIOCON | +0.22 | events | +0.18% |
| 2 | P_ANTI_DUMPING_IN → F_CHEM_FEEDSTOCK → BIOCON | +0.40 | events | -0.08% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-12 | EU marketing authorisation for pertuzumab biosimilar; launches (Pebrilzo dates in US after Genentech settlement) | regulatory | 0.60 | +1.5% | +0.90% |
| 2026-12 | Further block deals/stake sales by financial holders (Active Pine sold ~1% on 2026-09-09) | corporate_action | 0.40 | -1.0% | -0.40% |
| 2027-02 | Q3 FY27 results: H2-weighted biosimilar shipments, margin recovery from 19-20% | results | 0.95 | +0.0% | +0.00% |
| 2027-03 | USFDA inspection outcome at biologics/generics sites | regulatory | 0.10 | -9.0% | -0.90% |
| 2027-06 | Section 232 clarification on biosimilars/generics | regulatory | 0.10 | -13.0% | -1.30% |

## Analyst profile (agent research, sourced)
# BIOCON - Biocon Ltd. (Midcap 100, biosimilars)

## Business
Biocon is India's leading biosimilar company. After consolidation of Biocon Biologics the group has biosimilars (insulins, oncology antibodies, immunology, a growing pertuzumab programme), generics/APIs and the Syngene research-services stake. Revenue is Rs 17.4k cr TTM, EBITDA Rs 3.5k cr (20% margin) but PAT just Rs 340 cr because interest is Rs 895 cr and depreciation heavy (fixed assets Rs 39.7k cr). Borrowings are Rs 15.7k cr. Shareholding: promoters 44.7%, FIIs 8.6%, DIIs 29.2%.

## What moves the stock, ranked
1. **USD/INR (+5.0 per +3%).** The strongest empirical sensitivity in the batch (+6.12, t=3.4). Mechanism: ~70% foreign revenue; EBITDA +8% per 3% INR depreciation; thin PAT amplifies the equity effect.
2. **Biosimilar launches, pricing and shipments (US generic pricing -2.5, US demand +1.5, GLP-1 +3.0).** Q2 profit -51% on shipment timing; management flags a stronger H2.
3. **Leverage and rates (repo -1.5, Fed funds -1.0, G-sec -1.5).** Interest absorbs 90% of EBITDA less depreciation.
4. **Regulatory/trade (tariff -3.0, USFDA -4.0).** Biosimilar treatment under Section 232 is uncertain.
5. **Ownership flows:** block sales by Active Pine and DII absorption (DII +5.9pp).
6. **Input costs (-1.0).**

## Transmission examples
- **Fed/USD strength -> USD/INR up -> Biocon's USD revenues rise in rupees (+) but USD debt translation loss (-) -> net positive; 4th order: higher US rates (+25bp) lift SOFR-linked debt costs.**
- **Oil shock -> inflation -> RBI tightening -> floating rupee debt cost up -> low-ICR earnings squeeze -> equity -1.5% per 25bp.**
- **Pertuzumab settlement -> US launch -> competitive pricing vs Genentech/others -> Biocon share gains but price erosion 20-30%.**
- **US tariff on 'branded' drugs -> biosimilar status clarified -> if included, US ~30% of sales renegotiated.**

## Current situation
Weak Q2 (net profit Rs 41 cr), stock near yearly low (Univest 2026-10-21; 3m -17%). Equity shows flows from public to DIIs (block deal 2026-09-09). Overall confidence low because fundamentals are thin and several facts come from headlines only.

## Upcoming events
Q3 results (Feb 2027), pertuzumab EU/US launches, USFDA cycles, tariff clarifications.

## Bull and bear
**Bull:** H2 shipments, weaker rupee, new launches, deleveraging, GLP-1 generics. **Bear:** thin PAT, high debt, price erosion, tariff or FDA hit.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.