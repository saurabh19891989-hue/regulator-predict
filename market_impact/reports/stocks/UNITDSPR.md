# UNITDSPR — United Spirits Ltd.
*MIDCAP_100 · Fast Moving Consumer Goods · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -1.1%**, **12 months -1.0%** (rank 133 / 121 of 200 for 3m / 12m); beta 0.86
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +22.1%): 3 months 46%, 12 months 55%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -3.5% … P90 +2.6%; plausible 12m relative-return range incl. stock-specific noise: -25.3% … +26.1%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves -0.1 pp (model impact -0.3% beta-adjusted vs realised market-adjusted move +8.4%); forward event exposure +1.5% (3m +0.4%; half assumed priced); company-specific events -0.9%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Consumer premiumisation (`T_PREMIUMISATION`) | +1 | +2.08 | +2.00 | +0.08 | +0.00 | +0.00 | — |
| State excise / pricing policy for alcohol (`NEW_STATE_EXCISE_ALCOHOL`) | +1 = adverse change of Maharashtra/Karnataka scale (Popular NSV about -20%) | -2.00 | -2.00 | +0.00 | +0.00 | +0.00 | — |
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +1.95 | +2.00 | +0.00 | +0.00 | -0.05 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -1.80 | +0.00 | -0.96 | -0.49 | -0.35 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -1.43 | +0.00 | -0.71 | -0.60 | -0.11 | — |
| India 10-year G-sec yield (`F_GSEC_10Y_IN`) | +25 bp yield | -1.30 | -1.30 | +0.00 | +0.00 | +0.00 | — |
| Sugar price (`F_SUGAR`) | +10% sugar | -1.30 | -1.20 | -0.10 | +0.00 | +0.00 | +27.8% |
| Brent crude oil price (`F_BRENT`) | +10% Brent | -0.94 | -0.50 | -0.21 | -0.11 | -0.12 | +0.0% |
| Sugar export / ethanol blending policy (`P_SUGAR_ETHANOL`) | +1 = more favourable to millers | -0.93 | -0.80 | -0.13 | +0.00 | +0.00 | — |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +0.82 | +0.00 | +0.56 | +0.11 | +0.15 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -0.75 | -0.40 | +0.00 | -0.23 | -0.12 | -1.1% |
| Russia-Ukraine war / Western sanctions intensity on Russia (`NEW_RUSSIA_UKRAINE_WAR`) | +1 = escalation (new sanctions round, strikes on energy/port infrastructure); -1 = ceasefire/sanctions relief | -0.71 | +0.00 | -0.36 | -0.21 | -0.14 | — |
| OPEC+ crude supply decisions (`NEW_OPEC_PLUS_SUPPLY`) | +1 mb/d OPEC+ production (quota/actual) | +0.70 | +0.00 | +0.32 | +0.25 | +0.13 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -0.66 | +0.00 | -0.68 | -0.02 | +0.03 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -5.4% | -5.4% | -2.5 | -1.6 | -0.6 | -0.7 |
| Sugar supply shock: 2025-26 output cut to ~306 lakh t, retail sugar at record, first duty-free raw sugar imports in a decade (`EV_SUGAR_SHORTFALL26`) | occurred | 1.00 | -3.0% | -3.0% | -3.0 | +0.0 | +0.0 | +0.0 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -1.8% | -1.8% | -1.8 | +0.0 | -0.0 | -0.0 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -1.5% | -1.5% | +0.0 | -0.7 | -0.7 | -0.1 |
| OMC ethanol tender ESY 2026-27: no cane juice/syrup/B-heavy ethanol; maize price incentive cut; grain-based ethanol takes over (`EV_ETHANOL_ESY27_TENDER`) | occurred | 1.00 | +1.4% | +1.4% | +1.4 | +0.0 | +0.0 | +0.0 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.58 | +1.9% | +1.1% | +0.8 | +0.7 | +0.2 | +0.3 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.36 | -3.0% | -1.1% | -1.8 | -0.4 | -0.4 | -0.5 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -0.8% | -0.8% | +0.0 | -0.6 | -0.1 | -0.0 |
| Gold and silver slump from January 2026 peaks (silver -53%, gold -24%) (`EV_PRECIOUS_METALS_CRASH_2026`) | occurred | 1.00 | -0.7% | -0.7% | +0.0 | -0.6 | -0.1 | -0.0 |
| US waives Russia-oil secondary sanctions/100% tariff threat on buyers incl. India (17 Oct) (`EV_RUSSIA_WAIVER_OCT17`) | occurred | 1.00 | +0.6% | +0.6% | +0.0 | +0.3 | +0.2 | +0.1 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -0.6% | -0.6% | -0.4 | -0.1 | -0.1 | -0.0 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -0.6% | -0.6% | +0.0 | -0.4 | -0.0 | -0.2 |

## Strongest causal chains (1st–4th order)
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_SUGAR_SHORTFALL26 ⇒ F_SUGAR → UNITDSPR | -3.36% | -3.36% |
| 1 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → UNITDSPR | -2.48% | -2.48% |
| 1 | EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26 ⇒ F_GSEC_10Y_IN → UNITDSPR | -1.82% | -1.82% |
| 1 | EV_ETHANOL_ESY27_TENDER ⇒ P_SUGAR_ETHANOL → UNITDSPR | +0.80% | +0.80% |
| 3 | EV_CPI_REACCEL_SEP26 ⇒ F_CPI_IN → F_REPO_IN → F_GSEC_10Y_IN → UNITDSPR | -0.68% | -0.68% |
| 1 | EV_ETHANOL_ESY27_TENDER ⇒ F_SUGAR → UNITDSPR | +0.60% | +0.60% |
| 2 | EV_UST_SELLOFF_SEP26 ⇒ F_US_10Y → F_GSEC_10Y_IN → UNITDSPR | -0.57% | -0.57% |
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ C_MIDEAST_CONFLICT → F_GAS_GLOBAL → UNITDSPR | -0.54% | -0.54% |
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → UNITDSPR | -1.04% | -0.52% |
| 2 | EV_PRECIOUS_METALS_CRASH_2026 ⇒ F_US_10Y → F_GSEC_10Y_IN → UNITDSPR | -0.51% | -0.51% |
| 1 | EV_LNG_HORMUZ_DISRUPTION ⇒ F_GAS_GLOBAL → UNITDSPR | -0.50% | -0.50% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → UNITDSPR | -1.25% | -0.45% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → UNITDSPR | +0.75% | +0.44% |
| 1 | EV_SUGAR_SHORTFALL26 ⇒ P_SUGAR_ETHANOL → UNITDSPR | +0.40% | +0.40% |
| 1 | EV_GDP_Q1FY27_7_8 ⇒ F_URBAN_DEMAND → UNITDSPR | +0.40% | +0.40% |

## Analyst profile (agent research, sourced)
# United Spirits (UNITDSPR) - Market Impact profile, as of 2026-11-05

## Business
United Spirits, the Indian arm of Diageo (56.68%), sells whisky, vodka, rum and gin through state-regulated channels. Prestige & Above (P&A) brands such as Johnnie Walker, Black Dog, Signature and Royal Challenge are about 83% of net sales value (model estimate); Popular brands (McDowell's No.1 etc.) are the remainder. In Q2 FY27 NSV rose 2.8% to Rs3,258cr, with P&A +6.3% and Popular -22.7% as policy changes in Maharashtra and Karnataka bit. Gross margin expanded 88bp to 48.0%, but a 57% jump in advertising spend cut EBITDA 4.3% to Rs643cr (margin 19.7%) and PAT fell 2.1% to Rs462cr. TTM sales are Rs12,717cr at a ~18% operating margin; ROCE 26%; the company is almost debt-free. Stock P/E is 56 and 11.3x book.

## What moves the stock, ranked
1. **State excise policy (-2.0 per Maharashtra-sized shock)** - the dominant idiosyncratic risk; it shaped Q2.
2. **Premiumisation (+2.0)** and **urban demand (+2.0)**: P&A growth is the valuation driver.
3. **Sugar / molasses -> ENA cost (-1.2 per +10%)**, ethanol policy (-0.8), rice (-0.5).
4. **G-sec yield (-1.3)** for a 56x multiple; glass energy (gas -0.5), packaging (-0.6), Brent (-0.5), USD/INR (-0.4).
Empirical check: gas shows +0.90 (t +2.6), opposite to the cost logic; we assume that is risk-on beta and keep a fundamental -0.5 at low confidence. USD/INR +2.22 (t 1.8) likewise conflicts with import-cost logic.

## Transmission examples
- **Middle East escalation -> Brent up -> glass energy, freight and PET up -> cost of goods up; the company already reported the West Asia crisis as a gross-margin offset in Q2.** Second order: gas and LNG up -> glass bottle cost up. Third: Brent up -> CPI up -> RBI hikes -> G-sec up -> a 56x stock de-rates.
- **Sugar up (+28% since June) -> molasses up -> ENA (alcohol) up -> COGS up; ethanol blending policy competes for molasses/grain -> ENA tighter -> price hikes limited by state MRP approvals -> gross margin pressure.**
- **State government changes excise slab or MRP regime -> Popular volumes fall -> mix improves but absolute profit falls -> policy risk spreads to other states.**
- **Urban consumption slows -> P&A growth below double digits -> operating leverage lost -> multiple compresses.**

## Current situation
Q2 on 28 Oct: gross margin beat lifted the stock 4%; Nomura (TP Rs1,700) and Jefferies (up to +27%) are positive. A DRI (customs) search was disclosed on 17 Oct with no financial impact reported; a senior financial controller resigned on 28 Sep. The stock is -8% over 3 months.

## Upcoming
Q3 festive results (Jan/Feb 2027), DRI outcome (0.3), state excise changes (0.5).

## Bull and bear
**Bull:** gross margin gains, premium mix, low debt, strong cash. **Bear:** 56x P/E, state policy, input cost inflation, high advertising.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.