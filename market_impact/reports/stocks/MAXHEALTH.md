# MAXHEALTH — Max Healthcare Institute Ltd.
*NIFTY_50 · Healthcare · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -1.5%**, **12 months -1.8%** (rank 142 / 128 of 200 for 3m / 12m); beta 1.11
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +25.6%): 3 months 45%, 12 months 45%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -5.3% … P90 +2.4%; plausible 12m relative-return range incl. stock-specific noise: -45.0% … +14.6%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +0.0 pp (model impact -3.2% beta-adjusted vs realised market-adjusted move -6.2%); forward event exposure -0.3% (3m +0.3%; half assumed priced); company-specific events -1.0%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| India NPPA/NLEM drug price control and trade-margin regulation (`NEW_NPPA_DRUG_PRICE_CONTROL`) | +1 = one tightening step (NLEM expansion or trade-margin cap) | -6.00 | -6.00 | +0.00 | +0.00 | +0.00 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +3.47 | +3.50 | -0.09 | +0.01 | +0.05 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -3.26 | +0.00 | -2.78 | -0.40 | -0.08 | — |
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +2.30 | +2.20 | +0.32 | -0.13 | -0.09 | — |
| US dollar index (`F_DXY`) | +3% DXY | -2.29 | -1.50 | -0.65 | -0.09 | -0.05 | +2.2% |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -2.25 | -2.00 | -0.13 | -0.08 | -0.04 | — |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -2.02 | +0.00 | -1.31 | -0.64 | -0.07 | +3.5% |
| Consumer premiumisation (`T_PREMIUMISATION`) | +1 | +1.90 | +1.80 | +0.09 | +0.02 | -0.01 | — |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -1.79 | +0.00 | +0.00 | -1.61 | -0.19 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -1.76 | +0.00 | +0.00 | -0.73 | -1.03 | — |
| US equity market (`F_US_EQUITIES`) | +5% S&P 500 | +1.73 | +0.00 | +1.12 | +0.54 | +0.06 | +1.2% |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +1.63 | +0.00 | +0.62 | +1.07 | -0.06 | — |
| US 10-year Treasury yield (`F_US_10Y`) | +25 bp yield | -1.21 | +0.00 | -0.99 | -0.19 | -0.03 | +9.4% |
| Capital-gains / securities tax burden (`P_CAPITAL_GAINS_TAX`) | +1 = higher | -1.21 | +0.00 | -1.26 | +0.06 | -0.01 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -7.7% | -7.7% | -7.7 | +0.2 | -0.0 | -0.1 |
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -6.8% | -6.8% | +0.0 | -1.5 | -4.1 | -1.2 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +8.7% | +4.4% | +8.8 | -0.2 | +0.0 | +0.2 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -3.8% | -3.8% | +0.0 | -3.2 | -0.5 | -0.1 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -2.6% | -2.6% | -1.1 | -1.7 | +0.1 | +0.1 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.28 | -9.2% | -2.6% | +0.0 | -8.6 | -0.6 | -0.1 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -2.3% | -2.3% | -2.0 | -0.1 | -0.1 | -0.0 |
| Gold and silver slump from January 2026 peaks (silver -53%, gold -24%) (`EV_PRECIOUS_METALS_CRASH_2026`) | occurred | 1.00 | -2.3% | -2.3% | -1.0 | -1.5 | +0.3 | -0.0 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -2.0% | -2.0% | -0.6 | -1.1 | -0.2 | -0.1 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.36 | -5.4% | -1.9% | +0.0 | -2.3 | -2.5 | -0.6 |
| Disorderly yen carry-trade unwind (Aug-2024-style) after BoJ/MoF action (`EV_YEN_CARRY_UNWIND_RISK`) | risk_scenario | 0.18 | -10.5% | -1.9% | +0.0 | -10.0 | -0.1 | -0.4 |
| US midterms (3 Nov 2026): Democrats win House and Senate (`EV_US_MIDTERMS_DEM_SWEEP`) | occurred | 1.00 | +1.8% | +1.8% | +1.8 | +0.0 | -0.0 | +0.0 |

## Strongest causal chains (1st–4th order)
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_RECORD_OUTFLOW_26 ⇒ F_FPI_FLOWS → MAXHEALTH | -7.70% | -7.70% |
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → MAXHEALTH | +8.75% | +4.38% |
| 2 | EV_CPI_REACCEL_SEP26 ⇒ F_CPI_IN → F_REPO_IN → MAXHEALTH | -2.65% | -2.65% |
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_FPI_FLOWS → MAXHEALTH | -2.08% | -2.08% |
| 1 | EV_RBI_OCT26_HIKE25 ⇒ F_REPO_IN → MAXHEALTH | -2.00% | -2.00% |
| 3 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_CPI_IN → F_REPO_IN → MAXHEALTH | -1.77% | -1.77% |
| 1 | EV_US_MIDTERMS_DEM_SWEEP ⇒ F_FPI_FLOWS → MAXHEALTH | +1.75% | +1.75% |
| 3 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_USDINR → F_FPI_FLOWS → MAXHEALTH | -1.64% | -1.64% |
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_USDINR → MAXHEALTH | +1.56% | +1.56% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → MAXHEALTH | -5.23% | -1.46% |
| 2 | EV_UST_SELLOFF_SEP26 ⇒ F_US_10Y → F_FPI_FLOWS → MAXHEALTH | -1.19% | -1.19% |
| 2 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → MAXHEALTH | -6.53% | -1.18% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → MAXHEALTH | -5.25% | -1.16% |
| 1 | EV_UST_SELLOFF_SEP26 ⇒ F_DXY → MAXHEALTH | -1.09% | -1.09% |
| 2 | EV_PRECIOUS_METALS_CRASH_2026 ⇒ F_US_10Y → F_FPI_FLOWS → MAXHEALTH | -1.05% | -1.05% |

## Analyst profile (agent research, sourced)
# MAXHEALTH (Max Healthcare Institute) — Nifty 50, as of 2026-11-05

## Business
Max Healthcare is the premium North-Indian multi-speciality hospital operator (Delhi NCR, Mohali, Dehradun, Lucknow, Mumbai, Nagpur and expanding). It has among the highest ARPOB and an EBITDA margin around 27%. Q2 FY27 (2026-10-30): consolidated revenue +20% YoY, consolidated PAT Rs 414 cr (-15%), network PAT Rs 448 cr (+10%). The screener pack shows narrower sales (Rs 2,569 cr, EBITDA Rs 711 cr, 28%) than the company's network figures (Q1 network sales Rs 2,982 cr), so growth rates are more reliable than absolute levels.

## What moves the stock (ranked)
1. **Drug price/MRP regulation** (-6.0 per tightening step): the stock slid ~20% in three weeks to a 2-year low after the Supreme Court (2026-09-30) questioned steep cancer-drug markups and floated a 16% MRP cap; the Centre cut cancer-drug prices ~30% in October. Oncology is a core Max speciality.
2. **FPI flows and sentiment** (+3.5): 40.5% FII holding and beta ~1.25; FIIs have trimmed from 45.4%.
3. **Discount rate** (-2.0 per +25bp): 64x P/E.
4. **Urban demand/GDP** (+2.2, +1.6) and **premiumisation** (+1.8).
5. **Wages** (-1.0).
6. **DXY/USD-INR**: empirical DXY +3.26 (t=2.5) contradicts the prior; flagged and shrunk.

## Transmission examples
- **SC order on MRP caps -> pharmacy/oncology margin cut -> EBITDA -7% -> P/E derating at 64x** (1st to 3rd order), partly offset by procedure re-pricing.
- **Fed hawkish -> DXY and US yields up -> FPI outflow -> FIIs trim a 40%-FII-owned stock -> liquidity-driven selloff -> cost of equity up for expansion** (3rd order).
- **Wage inflation (labour codes, doctor retention) -> costs up -> tariff hikes needed -> insurers resist -> occupancy mix shifts** (3rd order).
- **Monsoon/rural income strong -> urban/semi-urban affluence -> elective surgeries and health insurance take-up up -> occupancy up** (3rd order).

## Current situation
Post-slump recovery: +2.9% 1m, -13% 3m, -18% 12m. Brokers: ICICI Securities Buy Rs 1,300; PL Buy Rs 1,080; CLSA positive (2026-11-04). Competitors (Rainbow, Artemis, Yatharth) report 12-14% ARPOB growth with capacity adds.

## Upcoming events
SC/NPPA follow-ups (Dec), Q3 results (Feb 2027), new bed commissioning.

## Bull and bear
Bull: regulatory clarity and capacity ramp support 20% earnings CAGR, price Rs 1,200+. Bear: MRP caps extended to consumables, FII selling, wage squeeze; derates to 45x. Confidence medium; call details only via headlines.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.