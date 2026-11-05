# HDFCBANK — HDFC Bank Ltd.
*NIFTY_50 · Financial Services · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -2.7%**, **12 months -4.9%** (rank 169 / 160 of 200 for 3m / 12m); beta 1.00
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +14.0%): 3 months 35%, 12 months 48%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -12.6% … P90 +2.6%; plausible 12m relative-return range incl. stock-specific noise: -25.5% … +15.9%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves -2.9 pp (model impact -9.0% beta-adjusted vs realised market-adjusted move -3.2%); forward event exposure -0.5% (3m -0.6%; half assumed priced); company-specific events -1.1%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Credit cost / NPA cycle (higher = worse) (`F_ASSET_QUALITY_IN`) | +50 bp credit cost | -6.05 | -6.00 | +0.00 | -0.03 | -0.02 | — |
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | +4.81 | +0.00 | +2.80 | +2.72 | -0.70 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -4.14 | -2.50 | -0.36 | -0.58 | -0.70 | — |
| India real GDP growth (`F_GDP_IN`) | +1 pp | +3.82 | +2.50 | +2.10 | -0.57 | -0.20 | — |
| Bank deposit growth / funding ease (`F_DEPOSIT_GROWTH_IN`) | +3 pp | +3.73 | +3.50 | +0.40 | -0.10 | -0.07 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -3.72 | +0.00 | -1.19 | -2.39 | -0.14 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +3.63 | +3.50 | +0.07 | -0.02 | +0.07 | — |
| Private corporate capex (`F_PRIVATE_CAPEX`) | +10% capex growth | +3.55 | +0.00 | +2.00 | +2.40 | -0.84 | — |
| Monsoon rainfall vs normal (`F_MONSOON`) | +10% above long-period average | +3.43 | +0.00 | +0.91 | +1.85 | +0.67 | — |
| RBI prudential tightening (risk weights, LCR, provisioning) (`P_RBI_PRUDENTIAL`) | +1 = tightening step | -3.26 | -2.00 | -1.46 | +0.13 | +0.07 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -2.91 | +0.00 | -0.93 | -0.81 | -1.18 | -1.1% |
| Central + state government capex (`F_GOVT_CAPEX`) | +10% capex growth | +2.59 | +0.00 | +0.90 | +1.71 | -0.02 | — |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +2.39 | +0.00 | +0.00 | +0.94 | +1.45 | — |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -2.38 | +0.00 | +0.00 | -0.86 | -1.52 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -12.6% | -12.6% | -6.7 | -1.8 | -2.6 | -1.5 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -8.0% | -8.0% | -7.7 | -0.1 | +0.0 | -0.2 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -4.7% | -4.7% | +0.0 | -1.4 | -3.0 | -0.4 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +9.0% | +4.5% | +8.8 | +0.1 | -0.0 | +0.2 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -4.3% | -4.3% | +0.0 | -1.1 | -2.3 | -0.8 |
| RBI expected-credit-loss (ECL) provisioning goes live as scheduled (FY28 start) (`EV_ECL_ROLLOUT_APR27`) | scheduled | 0.62 | -6.0% | -3.7% | -6.2 | +0.2 | +0.0 | -0.0 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.58 | +6.1% | +3.5% | +3.4 | +1.1 | +1.1 | +0.5 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.36 | -9.8% | -3.5% | -4.5 | -2.3 | -2.1 | -0.9 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -3.2% | -3.2% | +0.0 | -3.0 | -0.1 | -0.1 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -3.2% | -3.2% | -2.5 | -0.4 | -0.2 | -0.1 |
| Gold and silver slump from January 2026 peaks (silver -53%, gold -24%) (`EV_PRECIOUS_METALS_CRASH_2026`) | occurred | 1.00 | -2.8% | -2.8% | +0.0 | -2.8 | -0.0 | +0.0 |
| IMD April 2027 long-range forecast says normal or above-normal monsoon (>=96% LPA) (`EV_MONSOON27_FIRST_FORECAST_NORMAL`) | scheduled | 0.68 | +3.6% | +2.4% | +0.0 | +0.9 | +2.0 | +0.6 |

## Strongest causal chains (1st–4th order)
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_RECORD_OUTFLOW_26 ⇒ F_FPI_FLOWS → HDFCBANK | -7.70% | -7.70% |
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → HDFCBANK | +8.75% | +4.38% |
| 1 | EV_IRAN_WAR_HORMUZ_OIL ⇒ C_MIDEAST_CONFLICT → HDFCBANK | -3.75% | -3.75% |
| 1 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → HDFCBANK | -2.97% | -2.97% |
| 1 | EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26 ⇒ F_GSEC_10Y_IN → HDFCBANK | -2.52% | -2.52% |
| 1 | EV_ECL_ROLLOUT_APR27 ⇒ F_ASSET_QUALITY_IN → HDFCBANK | -3.00% | -1.86% |
| 1 | EV_US_MIDTERMS_DEM_SWEEP ⇒ F_FPI_FLOWS → HDFCBANK | +1.75% | +1.75% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → HDFCBANK | -5.23% | -1.46% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ C_MIDEAST_CONFLICT → HDFCBANK | +2.50% | +1.45% |
| 1 | EV_GDP_Q1FY27_7_8 ⇒ F_GDP_IN → HDFCBANK | +1.25% | +1.25% |
| 1 | EV_ECL_ROLLOUT_APR27 ⇒ P_RBI_PRUDENTIAL → HDFCBANK | -2.00% | -1.24% |
| 2 | EV_UST_SELLOFF_SEP26 ⇒ F_US_10Y → F_FPI_FLOWS → HDFCBANK | -1.19% | -1.19% |
| 2 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → HDFCBANK | -6.53% | -1.18% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → HDFCBANK | -5.25% | -1.16% |
| 2 | EV_UST_SELLOFF_SEP26 ⇒ F_DXY → F_FPI_FLOWS → HDFCBANK | -1.12% | -1.12% |

## Analyst profile (agent research, sourced)
# HDFCBANK - HDFC Bank Ltd. (Nifty 50, private bank) - as of 2026-11-05

## Business
India's largest private bank after the 2023 merger with HDFC Ltd: Rs27 lakh cr-scale loan book (retail, mortgage, wholesale), deposits +18.8% y/y in Q2 FY27 with CASA lagging time deposits. Owns stakes in HDFC Life, HDFC AMC and HDB Financial. FIIs 39.4% (44.05% in March), DIIs 43.4%.

## What moves the stock, ranked
1. **Management/execution risk** - Anup Bagchi appointed MD & CEO on 2026-10-01; shares fell 2.3% on the pick, another executive departed on 2026-11-02. Company-specific, not a driver node; it is the main source of stock-specific variance.
2. **FPI flows** - FII holding down 4.7pp in six months; +3.5% per US$5bn quarterly net inflow.
3. **Deposit growth / CD ratio / NIM** - the structural merger-digestion story; +3pp deposit growth ~ +3.5.
4. **Treasury and yields** - Q2 profit growth (4.7%) was cut by a Rs1,610cr treasury loss; 10y +25bp ~ -1.8.
5. **Repo and discount rate** - RBI hiked to 5.50% on 2026-10-07; floating-rate book reprices first, net effect ambiguous (-0.5).
6. **Credit cost** - +50bp credit cost = -6% (Rs13,500cr pre-tax on Rs83,685cr TTM PAT, persistence 0.5).
7. **Regulation, geopolitics**.

Empirical pack: cotton -1.29 (t -2.4), coal +2.09 (t 2.3) and US equities -0.91 (t -2.0) are statistically notable but lack fundamental paths for a bank; set near zero. Brent -0.56 (t -1.7) agrees in sign with our -0.6.

## Transmission examples
- **Middle East escalation -> Brent up -> INR weaker (USD/INR already 94.5, +6.5% 12m) -> inflation up -> RBI hikes again -> HDFC floating loans reprice immediately, deposits with a 6-12 month lag -> NIM +5-10bp near term -> but 10y G-sec up cuts AFS book (Rs750cr per 25bp) and P/E -> net ~flat to negative; 4th order: higher borrowing costs for mortgage customers slow housing credit and real-estate demand.**
- **FPI reallocation away from India financials (US 10y 4.89%, +17.7% 12m) -> HDFC Bank, with the largest foreign float, falls more than index -> funding cost of FCNR/AT1 rises.**
- **Leadership shock -> analyst downgrades -> passive and active FII selling -> weak stock -> employee-retention costs rise.**

## Current situation
Q2 profit Rs19,510cr (+4.7%) broadly in line, margin stabilised, deposits +19%. Stock Rs753 (P/E 14.6x), near 52-week low then rebounded ~6% in a month.

## Upcoming
Q3 results mid-Jan 2027 (inferred), December MPC, executive appointments, ECL regime from April 2027.

## Bull / bear
Bull: new CEO resets, deposits rebuild, CD ratio normalises, rates help NIM, FPIs return. Bear: further executive exits, NIM down, slow loan growth, structural share loss to ICICI/Axis, higher yields.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.