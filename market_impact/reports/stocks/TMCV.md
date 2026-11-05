# TMCV — Tata Motors Ltd.
*NIFTY_NEXT_50 · Capital Goods · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +0.7%**, **12 months +3.9%** (rank 76 / 44 of 200 for 3m / 12m); beta 1.53
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +27.8%): 3 months 52%, 12 months 60%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 +0.0% … P90 +11.9%; plausible 12m relative-return range incl. stock-specific noise: -17.0% … +47.5%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +0.0 pp (model impact +7.0% beta-adjusted vs realised market-adjusted move +8.8%); forward event exposure +8.8% (3m +2.0%; half assumed priced); company-specific events +1.4%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +8.35 | +0.00 | +5.74 | +2.32 | +0.28 | — |
| Indian vehicle demand (`F_AUTO_DEMAND_IN`) | +10% volumes | +7.00 | +7.00 | +0.00 | +0.00 | +0.00 | — |
| Market-share pressure in Indian medium and heavy CVs (`NEW_INDIA_CV_SHARE_PRESSURE`) | +1 = 2 pp market share loss to competitors | -5.00 | -5.00 | +0.00 | +0.00 | +0.00 | — |
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +4.53 | +0.00 | +4.96 | -0.26 | -0.17 | — |
| Central + state government capex (`F_GOVT_CAPEX`) | +10% capex growth | +4.48 | +4.00 | +0.57 | +0.08 | -0.16 | — |
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | +4.18 | +0.00 | +4.86 | -0.40 | -0.28 | — |
| India real GDP growth (`F_GDP_IN`) | +1 pp | +3.60 | +4.00 | -0.34 | -0.23 | +0.17 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -3.45 | +0.00 | -1.67 | -1.80 | +0.01 | — |
| Road/highway awarding (`P_INFRA_SPENDING_ROADS`) | +10% | +2.75 | +2.50 | +0.19 | +0.05 | +0.00 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -2.53 | +0.00 | -1.30 | -0.67 | -0.57 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -2.36 | -1.50 | -0.43 | -0.31 | -0.12 | — |
| Monsoon rainfall vs normal (`F_MONSOON`) | +10% above long-period average | +2.33 | +0.00 | +1.07 | +0.86 | +0.41 | — |
| Indian domestic steel price (`F_STEEL_INDIA`) | +7% domestic HRC/rebar price | -2.25 | -2.20 | +0.00 | -0.03 | -0.02 | — |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -2.24 | +0.00 | +0.00 | -1.28 | -0.96 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -8.7% | -8.7% | -5.0 | -1.4 | -1.2 | -1.2 |
| India Q1 FY27 GDP grows 7.8% (31 Aug 2026), beating ~7.3% consensus (`EV_GDP_Q1FY27_7_8`) | occurred | 1.00 | +6.2% | +6.2% | +6.0 | +0.3 | -0.2 | +0.0 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -4.3% | -4.3% | +0.0 | -1.9 | -2.5 | +0.0 |
| Union Budget 2027-28 capex/railway allocation (infra, railways, defence) (`EV_BUDGET27_CAPEX_RAILWAY`) | scheduled | 0.90 | +3.6% | +3.2% | +3.2 | +0.5 | +0.1 | -0.1 |
| Global and Indian steel prices at multi-year highs (global HRC +60% y/y) (`EV_STEEL_RALLY_2026`) | occurred | 1.00 | -3.1% | -3.1% | -3.1 | +0.0 | -0.0 | -0.0 |
| Retail petrol/diesel price freeze with crude >$100 squeezes OMC marketing margins; Q2 FY27 results split refiners (`EV_OMC_FUEL_FREEZE_LOSSES`) | occurred | 1.00 | -3.1% | -3.1% | +0.0 | -2.9 | -0.5 | +0.2 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -2.9% | -2.9% | +0.0 | -1.3 | -1.1 | -0.5 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -2.4% | -2.4% | -1.5 | -0.4 | -0.4 | -0.1 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -2.3% | -2.3% | -2.2 | +0.1 | -0.1 | -0.1 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.36 | -5.1% | -1.8% | -2.5 | -1.2 | -0.8 | -0.7 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.58 | +3.0% | +1.7% | +1.5 | +0.6 | +0.4 | +0.4 |
| IMD April 2027 long-range forecast says normal or above-normal monsoon (>=96% LPA) (`EV_MONSOON27_FIRST_FORECAST_NORMAL`) | scheduled | 0.68 | +2.3% | +1.5% | +0.0 | +1.1 | +1.1 | +0.1 |

## Strongest causal chains (1st–4th order)
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → TMCV | -4.95% | -4.95% |
| 1 | EV_GDP_Q1FY27_7_8 ⇒ F_GOVT_CAPEX → TMCV | +4.00% | +4.00% |
| 1 | EV_STEEL_RALLY_2026 ⇒ F_STEEL_INDIA → TMCV | -3.08% | -3.08% |
| 1 | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → TMCV | +3.20% | +2.88% |
| 2 | EV_OMC_FUEL_FREEZE_LOSSES ⇒ NEW_OMC_MARKETING_MARGIN → F_GOVT_CAPEX → TMCV | -2.88% | -2.88% |
| 1 | EV_FPI_RECORD_OUTFLOW_26 ⇒ F_FPI_FLOWS → TMCV | -2.20% | -2.20% |
| 1 | EV_GDP_Q1FY27_7_8 ⇒ F_GDP_IN → TMCV | +2.00% | +2.00% |
| 2 | EV_CPI_REACCEL_SEP26 ⇒ F_CPI_IN → F_REPO_IN → TMCV | -1.99% | -1.99% |
| 1 | EV_RBI_OCT26_HIKE25 ⇒ F_REPO_IN → TMCV | -1.50% | -1.50% |
| 2 | EV_SWMONSOON26_DEFICIT ⇒ F_MONSOON → F_GDP_IN → TMCV | -1.34% | -1.34% |
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → TMCV | +2.50% | +1.25% |
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_GDP_IN → TMCV | -1.19% | -1.19% |
| 2 | EV_INDIA_RETAIL_FUEL_HIKE ⇒ NEW_OMC_MARKETING_MARGIN → F_GOVT_CAPEX → TMCV | +2.40% | +1.08% |
| 3 | EV_CPI_REACCEL_SEP26 ⇒ F_CPI_IN → F_REPO_IN → F_AUTO_DEMAND_IN → TMCV | -1.04% | -1.04% |
| 3 | EV_OMC_FUEL_FREEZE_LOSSES ⇒ NEW_OMC_MARKETING_MARGIN → F_GOVT_CAPEX → F_GDP_IN → TMCV | -0.97% | -0.97% |

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