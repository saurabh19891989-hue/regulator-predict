# TMCV — Tata Motors Ltd.
*NIFTY_NEXT_50 · Capital Goods · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +1.3%**, **12 months +2.5%** (rank 30 / 20 of 200 for 3m / 12m); beta 1.53
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +27.8%): 3 months 54%, 12 months 40%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -0.2% … P90 +7.0%; plausible 12m relative-return range incl. stock-specific noise: -37.2% … +27.4%
- Decomposition (12m): 0.5 × forward event exposure +4.4% (3m +2.2%; half assumed priced) + 0.5 × company-specific catalysts +1.4%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply +8.7% (beta-adjusted) vs a realised market-adjusted move of +8.8% — gap -0.1 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +8.01 | +0.00 | +5.74 | +2.10 | +0.18 | — |
| Indian vehicle demand (`F_AUTO_DEMAND_IN`) | +10% volumes | +7.00 | +7.00 | +0.00 | +0.00 | +0.00 | — |
| Market-share pressure in Indian medium and heavy CVs (`NEW_INDIA_CV_SHARE_PRESSURE`) | +1 = 2 pp market share loss to competitors | -5.00 | -5.00 | +0.00 | +0.00 | +0.00 | — |
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +4.78 | +0.00 | +4.96 | -0.13 | -0.06 | — |
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | +4.57 | +0.00 | +4.86 | -0.20 | -0.09 | — |
| Central + state government capex (`F_GOVT_CAPEX`) | +10% capex growth | +4.51 | +4.00 | +0.57 | +0.08 | -0.14 | — |
| India real GDP growth (`F_GDP_IN`) | +1 pp | +3.73 | +4.00 | -0.34 | -0.16 | +0.23 | — |
| Road/highway awarding (`P_INFRA_SPENDING_ROADS`) | +10% | +2.75 | +2.50 | +0.19 | +0.05 | +0.00 | — |
| Private corporate capex (`F_PRIVATE_CAPEX`) | +10% capex growth | +2.38 | +0.00 | +2.56 | -0.20 | +0.02 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -2.34 | -1.50 | -0.43 | -0.31 | -0.10 | — |
| Monsoon rainfall vs normal (`F_MONSOON`) | +10% above long-period average | +2.34 | +0.00 | +1.07 | +0.95 | +0.33 | — |
| Indian wage / employee-cost inflation (`F_WAGES_IN`) | +2 pp | +2.31 | +0.00 | +0.00 | +2.46 | -0.15 | — |
| Indian domestic steel price (`F_STEEL_INDIA`) | +7% domestic HRC/rebar price | -2.23 | -2.20 | +0.00 | -0.02 | -0.01 | — |
| Critical-mineral supply tightness (China export controls on rare earths, magnets, graphite, Ga/Ge) (`NEW_RARE_EARTH_SUPPLY`) | +1 = new/tighter export-control round | -2.08 | +0.00 | -2.08 | +0.00 | +0.00 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| India Q1 FY27 GDP grows 7.8% (31 Aug 2026), beating ~7.3% consensus (`EV_GDP_Q1FY27_7_8`) | occurred | 1.00 | +6.2% | +6.2% | +6.0 | +0.3 | -0.2 | +0.0 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -2.9% | -2.9% | +0.0 | -1.3 | -1.2 | -0.4 |
| Global and Indian steel prices at multi-year highs (global HRC +60% y/y) (`EV_STEEL_RALLY_2026`) | occurred | 1.00 | -2.5% | -2.5% | -2.4 | +0.0 | -0.0 | -0.0 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -2.4% | -2.4% | -1.5 | -0.4 | -0.4 | -0.1 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -2.3% | -2.3% | -2.2 | +0.1 | -0.1 | -0.1 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -1.9% | -1.9% | +0.0 | -0.9 | -1.6 | +0.6 |
| IMD April 2027 long-range forecast says normal or above-normal monsoon (>=96% LPA) (`EV_MONSOON27_FIRST_FORECAST_NORMAL`) | scheduled | 0.68 | +2.3% | +1.6% | +0.0 | +1.1 | +1.1 | +0.1 |
| Rural demand indicators mixed: tractor volumes dip in Oct, 2W festive sales firm, rural CPI above urban, rural jobs scheme person-days down (`EV_RURAL_DEMAND_SOFT26`) | occurred | 1.00 | -1.4% | -1.4% | +0.0 | -1.5 | +0.1 | +0.0 |
| Risk: stagflation scare - CPI >=6.5% while GDP growth slips below ~6% (Q3 FY27 data, late Feb 2027) (`EV_INDIA_STAGFLATION_SCARE`) | risk_scenario | 0.12 | -11.0% | -1.3% | -7.5 | -2.4 | -0.9 | -0.2 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +2.6% | +1.3% | +2.5 | -0.1 | +0.1 | +0.1 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.55 | +2.3% | +1.3% | +1.3 | +0.6 | +0.2 | +0.2 |
| North-east monsoon 2026 normal or above-normal (relief for southern reservoirs) (`EV_NEMONSOON26_NORMAL_UP`) | anticipated | 0.85 | +1.3% | +1.1% | +0.0 | +0.5 | +0.6 | +0.1 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → TMCV | +2.50% | +1.25% |
| 2 | EV_RARE_EARTH_CONTROLS_REIMPOSED ⇒ NEW_RARE_EARTH_SUPPLY → F_AUTO_DEMAND_IN → TMCV | -3.36% | -0.84% |
| 2 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_GDP_IN → TMCV | +1.07% | +0.73% |
| 1 | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → TMCV | +0.80% | +0.72% |
| 1 | EV_INDIA_STAGFLATION_SCARE ⇒ F_GDP_IN → TMCV | -6.00% | -0.72% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → TMCV | +1.30% | +0.72% |
| 1 | EV_Q2_FY27_GDP_STRONG ⇒ F_GDP_IN → TMCV | +0.80% | +0.64% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → TMCV | -1.50% | -0.63% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → TMCV | -2.20% | -0.55% |
| 2 | EV_BUDGET27_AGRI_RURAL ⇒ F_RURAL_DEMAND → F_GDP_IN → TMCV | +0.77% | +0.54% |
| 1 | EV_INDIA_HR_STEEL_AD_PROVISIONAL ⇒ F_STEEL_INDIA → TMCV | -0.88% | -0.48% |
| 2 | EV_BUDGET27_AGRI_RURAL ⇒ F_RURAL_DEMAND → F_AUTO_DEMAND_IN → TMCV | +0.69% | +0.48% |
| 2 | EV_NEMONSOON26_NORMAL_UP ⇒ F_MONSOON → F_GDP_IN → TMCV | +0.53% | +0.45% |
| 2 | EV_RURAL_RELIEF_PACKAGE ⇒ F_RURAL_DEMAND → F_GDP_IN → TMCV | +0.77% | +0.42% |
| 1 | EV_INDIA_EU_FTA_SIGNED ⇒ F_EU_GDP → TMCV | +0.45% | +0.41% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_AUTO_DEMAND_IN → TMCV | +0.50 | director_override | +3.50% |
| 1 | F_STEEL_INDIA → TMCV | +1.35 | events | -2.97% |
| 1 | F_GDP_IN → TMCV | +0.50 | events | +2.00% |
| 1 | F_FPI_FLOWS → TMCV | -1.60 | events | -1.60% |
| 1 | F_REPO_IN → TMCV | +1.00 | events | -1.50% |
| 1 | P_EV_POLICY → TMCV | +1.10 | events | +1.10% |
| 1 | F_GOVT_CAPEX → TMCV | +0.20 | director_override | +0.80% |
| 1 | F_ALUMINIUM → TMCV | -1.96 | observed | +0.78% |
| 1 | F_EU_GDP → TMCV | +0.22 | events | +0.33% |
| 1 | F_USDINR → TMCV | -0.37 | observed | -0.11% |
| 2 | F_CHINA_GDP → F_RUBBER → TMCV | +0.30 | events | -0.02% |
| 3 | P_ANTI_DUMPING_IN → F_CHEM_FEEDSTOCK → F_RUBBER → TMCV | +0.40 | events | -0.01% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-11 | Iveco tender offer reopening period (2-6 Nov) and settlement; final acceptance level and regulatory clearances | corporate_action | 0.90 | +0.5% | +0.45% |
| 2026-12-01 | Monthly CV sales (November) release | other | 0.98 | +0.0% | +0.00% |
| 2027-02 | Q3 FY27 results (Dec quarter) | results | 0.95 | +0.5% | +0.47% |
| 2027-03 | Iveco integration plan / squeeze-out and financing details; leverage rises | corporate_action | 0.60 | +0.0% | +0.00% |
| 2027-05 | Q4 FY27 results and FY28 outlook | results | 0.95 | +0.5% | +0.47% |

## Analyst profile (agent research, sourced)
# TMCV — Tata Motors Ltd., commercial vehicles (profile as of 2026-11-05)

Sources: pack `market_impact/data/packs/TMCV.md` (no empirical sensitivity table: new listing); web-search summaries of Autocar Pro, The Week, HDFC Sky, ticker.finology.in, Upstox. Segment and cost shares are model estimates; the Iveco status after 2026-10-27 was not confirmed from a primary source. No expected-return number is given.

## Business
After the demerger, TMCV is India's biggest commercial vehicle company: medium and heavy trucks (M&HCV), intermediate and small CVs, pickups, vans, buses and e-buses, with spares and services. Passenger vehicles sit in the separate listed Tata Motors Passenger Vehicles (TMPV). Q2 FY27 volumes were 135,114 (+42.7%), domestic 113,982 (+30.9%), international 21,132. Revenue was about Rs 25,300 cr (+36%), profit Rs 1,254 cr, and the interest bill has fallen to about Rs 100 cr per quarter. The strategic overlay is the tender offer for Iveco Group (Italy) at EUR 14.40 per share, which would roughly double the scale and add a European platform.

## What moves the stock (ranked)
1. **Indian CV cycle (+7 per +10% industry volumes):** industry volumes are +24% in H1 FY27 (Autocar Pro) on infrastructure, mining and replacement demand; GDP (+4 per pp) and government capex (+4) feed it. Operating leverage is high, so volume surprises dominate.
2. **Iveco transaction:** completion adds leverage, EUR exposure and European cycle risk (+1.5 per pp EU GDP) in exchange for scale and platform synergies. The stock rose 4% on 2026-10-27 as acceptances crossed the threshold; Nomura cut its target to Rs 511 on 2026-10-26 (still +29%). Net effect on equity value is uncertain (-4% to +5% on completion).
3. **Input costs:** steel (-2.2 per +7% HRC; global HRC +20.6% since June), aluminium (-0.4), rubber (-0.3); pass-through is by price hikes (done 2026-09-17) with a one to two quarter lag.
4. **Financing and fuel:** repo +25 bp ≈ -1.5 (CV loan EMIs), Brent +10% ≈ -1.0 (diesel cost for fleet owners).
5. **Competition (-5 per 2 pp share loss):** Ashok Leyland, VECV, Mahindra.
6. **Flows (+1)** and EV policy (+1).

## Transmission examples
- **Middle East escalation (4th order):** escalation -> Brent up (Brent is +15% over 3 months) -> diesel prices rise (2nd) -> fleet operators' margins squeeze and freight rates lag (3rd) -> truck purchases deferred and financier credit tightens (4th) -> TMCV domestic volumes soften. Parallel path: Brent up -> INR weaker -> RBI holds -> CV loan costs stay high -> demand dampened. A ceasefire reverses this; one undated report links a Tata Motors spike to an Iran ceasefire, and Brent is -5.6% in one month, which is consistent with the sharp rally on 2026-11-05 but not verified.
- **Infrastructure push (3rd order):** Union Budget lifts road/rail outlay -> more tipper and HCV demand -> TMCV volumes and utilisation up -> operating leverage lifts OPM from 10% to 12% -> earnings upgrades.
- **Steel up (3rd order):** China cuts steel exports -> Indian HRC up 7% -> body/chassis cost +1.4% -> OPM falls ~1.4 pp before price hikes -> TMCV hikes prices (done) -> volumes pull forward before hike then dip.
- **Europe (4th order):** after closing, EU growth slows -> Iveco volumes fall -> consolidated EBITDA drops with a leveraged balance sheet -> TMCV share price falls even if India is strong.

## Current situation
Stock Rs 434 (market cap Rs 1.6 lakh cr), -5.7% in three months, flat in a month, 52-week range Rs 306-509. P/E 22. Revenue and volumes are strong but OPM slipped ~90 bp YoY. On 2026-11-05 Tata Motors and Ashok Leyland rose up to 12% in a Nifty Auto surge (ET, Moneycontrol); the reasons given were not retrieved. FII holding 19.0%, DII 18.6% rising. Promoters 42.5%.

## Upcoming events
Iveco offer settlement and regulatory clearances (Nov 2026 - Q1 2027), monthly sales on the 1st, Q3 FY27 results (Feb 2027), Budget (Feb 2027), Q4 results (May 2027).

## Bull case
CV upcycle continues for 4-6 more quarters, Iveco closes with credible synergy and deleveraging, OPM reaches 12-13%, and the stock re-rates toward analyst targets of Rs 500+.

## Bear case
Cyclical peak: industry growth falls to single digits, steel and diesel squeeze fleet owners, Iveco proves dilutive with higher leverage, and the P/E compresses from 22x to 15x.

## Uncertainties
Basis of Q2 revenue and margin differs across sources; Iveco final acceptance and funding not verified; no sensitivity table. Confidence: low.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.