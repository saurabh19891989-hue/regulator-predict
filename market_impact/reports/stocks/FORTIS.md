# FORTIS — Fortis Healthcare Ltd.
*MIDCAP_100 · Healthcare · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -3.0%**, **12 months -3.1%** (rank 171 / 143 of 200 for 3m / 12m); beta 0.99
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +23.3%): 3 months 40%, 12 months 42%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -5.5% … P90 -0.1%; plausible 12m relative-return range incl. stock-specific noise: -22.8% … +19.0%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +0.0 pp (model impact -1.8% beta-adjusted vs realised market-adjusted move -17.2%); forward event exposure +0.1% (3m +0.3%; half assumed priced); company-specific events -4.0%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| India NPPA/NLEM drug price control and trade-margin regulation (`NEW_NPPA_DRUG_PRICE_CONTROL`) | +1 = one tightening step (NLEM expansion or trade-margin cap) | -5.00 | -5.00 | +0.00 | +0.00 | +0.00 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +2.41 | +2.50 | -0.17 | +0.02 | +0.05 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -2.13 | -0.60 | -1.29 | -0.20 | -0.04 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -2.05 | -1.80 | -0.14 | -0.10 | -0.02 | — |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -2.01 | +0.00 | -0.35 | -1.49 | -0.17 | — |
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +1.98 | +2.00 | +0.30 | -0.22 | -0.10 | — |
| Consumer premiumisation (`T_PREMIUMISATION`) | +1 | +1.59 | +1.50 | +0.08 | +0.02 | -0.02 | — |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +1.57 | +0.00 | +0.73 | +1.00 | -0.15 | — |
| Indian wage / employee-cost inflation (`F_WAGES_IN`) | +2 pp | -1.48 | -1.70 | +0.27 | +0.05 | -0.10 | — |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -1.15 | +0.00 | -0.72 | -0.38 | -0.05 | +3.5% |
| US equity market (`F_US_EQUITIES`) | +5% S&P 500 | +1.06 | +0.00 | +0.80 | +0.23 | +0.02 | +1.2% |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -0.97 | +0.00 | +0.00 | -0.24 | -0.73 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | +0.95 | +1.80 | -0.52 | -0.31 | -0.02 | -1.1% |
| Monsoon rainfall vs normal (`F_MONSOON`) | +10% above long-period average | +0.86 | +0.00 | +0.40 | +0.04 | +0.42 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -5.2% | -5.2% | -5.5 | +0.5 | -0.0 | -0.2 |
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -4.2% | -4.2% | +0.0 | -0.1 | -2.9 | -1.2 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +6.0% | +3.0% | +6.2 | -0.5 | +0.0 | +0.2 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -2.5% | -2.5% | -0.7 | -1.5 | -0.3 | +0.0 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -2.1% | -2.1% | -1.8 | -0.1 | -0.1 | -0.0 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.28 | -5.4% | -1.5% | +0.0 | -5.3 | +0.0 | -0.2 |
| Disorderly yen carry-trade unwind (Aug-2024-style) after BoJ/MoF action (`EV_YEN_CARRY_UNWIND_RISK`) | risk_scenario | 0.18 | -6.6% | -1.2% | +0.0 | -6.6 | +0.4 | -0.4 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.36 | -3.3% | -1.2% | +0.0 | -0.9 | -1.8 | -0.6 |
| US midterms (3 Nov 2026): Democrats win House and Senate (`EV_US_MIDTERMS_DEM_SWEEP`) | occurred | 1.00 | +1.2% | +1.2% | +1.2 | -0.1 | -0.0 | +0.0 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -1.2% | -1.2% | +0.0 | -1.3 | +0.2 | +0.0 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -1.1% | -1.1% | +0.0 | -0.5 | -0.0 | -0.5 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -1.1% | -1.1% | +0.0 | -0.9 | -0.1 | -0.1 |

## Strongest causal chains (1st–4th order)
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_RECORD_OUTFLOW_26 ⇒ F_FPI_FLOWS → FORTIS | -5.50% | -5.50% |
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → FORTIS | +6.25% | +3.12% |
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_USDINR → FORTIS | +2.82% | +2.82% |
| 1 | EV_RBI_OCT26_HIKE25 ⇒ F_REPO_IN → FORTIS | -1.80% | -1.80% |
| 3 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_CPI_IN → F_REPO_IN → FORTIS | -1.59% | -1.59% |
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_FPI_FLOWS → FORTIS | -1.49% | -1.49% |
| 1 | EV_US_MIDTERMS_DEM_SWEEP ⇒ F_FPI_FLOWS → FORTIS | +1.25% | +1.25% |
| 2 | EV_CPI_REACCEL_SEP26 ⇒ F_CPI_IN → F_REPO_IN → FORTIS | -1.19% | -1.19% |
| 3 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_USDINR → F_FPI_FLOWS → FORTIS | -1.17% | -1.17% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → FORTIS | -3.73% | -1.05% |
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_GDP_IN → FORTIS | -0.89% | -0.89% |
| 2 | EV_UST_SELLOFF_SEP26 ⇒ F_US_10Y → F_FPI_FLOWS → FORTIS | -0.85% | -0.85% |
| 2 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → FORTIS | -4.67% | -0.84% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → FORTIS | -3.75% | -0.82% |
| 2 | EV_UST_SELLOFF_SEP26 ⇒ F_DXY → F_FPI_FLOWS → FORTIS | -0.80% | -0.80% |

## Analyst profile (agent research, sourced)
# FORTIS (Fortis Healthcare) — Midcap, as of 2026-11-05

## Business
Fortis runs about 36 healthcare facilities with roughly 4,000 operational beds (screener.in), mainly in NCR, Mumbai, Bengaluru and Punjab, plus SRL, a 57%-owned diagnostics chain with 415 labs. Hospitals are about three quarters of revenue. IHH Healthcare of Malaysia holds ~31%. Q1 FY27 (Jun 2026): sales Rs 2,545 cr (+17.5% YoY), EBITDA Rs 537 cr (21%), PAT Rs 273 cr; management targets a 25% EBITDA margin by FY28 and approved Rs 252 cr capex. Q2 FY27 is due shortly and is not in the pack, so the latest quarter used here is Q1.

## What moves the stock (ranked)
1. **Drug-price and trade-margin regulation** (-5.0 per tightening step). On 2026-09-29/30 the Supreme Court questioned cancer-drug markups and asked why MRP should not be capped at 16% above cost; hospital stocks lost about US$2.6 bn (ThePrint). The Centre then cut cancer-drug prices ~30% and NPPA tightened compliance. This is a new proposed node (NEW_P_DRUG_PRICE_CONTROL).
2. **Governance/litigation overhang** (event-specific, 18% downside tail). The Delhi HC ordered a six-month forensic audit of Fortis, IHH and RHT transactions on 2026-08-31 in the Daiichi-Singh brothers case; the Supreme Court declined to stop it on 2026-09-25. Fortis says it will be cleared of links to the Singh brothers. A Delhi HC order making listed firms answerable for promoters' personal debt (Livemint 2026-09-23) widens the risk framing.
3. **FPI flows** (+2.5 per US$5 bn): FIIs fell from 26.0% to 23.2% in two quarters.
4. **Wage and doctor costs** (-1.7 per +2pp) and **urban demand** (+2.0).
5. **Rates** (-1.8 per +25bp): 57x P/E growth stock, modest net debt (interest Rs 320 cr a year).
6. **USD/INR**: empirical +2.98 (t=2.0) but fundamentally weak, so shrunk to +1.8.

## Transmission examples
- **SC remark on markups -> policy proposal of MRP cap -> hospital pharmacy and oncology margin compresses -> EBITDA -7% -> multiple compresses (57x)** (1st to 3rd order). Hospitals could recoup via procedure pricing, limiting the hit.
- **Higher CPI -> RBI holds repo -> bond yields up -> discount rate on long-duration healthcare growth stocks up -> Fortis P/E derates** (3rd order); concurrently hiring costs rise (wage inflation).
- **FPI outflow (US rates up, strong USD) -> FIIs sell Fortis (23% holding) -> valuation drop -> cost of equity for expansion up** (3rd order).
- **Daiichi-Singh audit finds diverted funds -> IHH/Fortis claims reopened -> contingent liability (Rs ~5,200 cr cited by Law.asia) -> governance discount -> insurers/doctor relationships unaffected but index funds underweight** (4th order).

## Current situation
Stock -20% over 12m and -12% over 3m, 6% above its 705 low after a bounce in October. Brokers: Nomura Neutral (TP Rs 1,030), PL Capital Buy, Jefferies bullish on six healthcare stocks (2026-10-02). Q2 FY27 results pending.

## Upcoming events
Q2 results (mid-November, unverified), audit hearings (to ~Feb 2027), Supreme Court/NPPA drug-margin follow-ups, bed-addition commissioning.

## Bull and bear
Bull: regulatory clarity, 25% margin path, clean audit; EBITDA Rs 2,900 cr by FY28 supports Rs 1,000+. Bear: MRP caps spread to consumables, adverse audit, wage squeeze; margin stuck at 21%, derating to 40x. Confidence low: Q2 numbers and call content not available, ARPOB/occupancy not fetched, mix figures model knowledge.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.