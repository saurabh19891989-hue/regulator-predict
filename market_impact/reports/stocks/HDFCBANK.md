# HDFCBANK — HDFC Bank Ltd.
*NIFTY_50 · Financial Services · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +0.5%**, **12 months +0.5%** (rank 47 / 66 of 200 for 3m / 12m); beta 1.00
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +14.0%): 3 months 53%, 12 months 50%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -5.4% … P90 +5.6%; plausible 12m relative-return range incl. stock-specific noise: -20.3% … +19.3%
- Decomposition (12m): 0.5 × forward event exposure +1.1% (3m +1.0%; half assumed priced; market-priced macro drift removed) + 0.5 × company-specific catalysts +0.2%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply -7.4% (beta-adjusted) vs a realised market-adjusted move of -3.2% — gap -4.2 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## Where the expected return comes from
Market-priced macro drivers (rates, FX, commodities, indices, volatility, flows, growth, inflation) are taken as priced, so what is left is policy, regulatory, sector, theme, geopolitical and company-specific exposure — where 2nd–4th-order effects are most likely to be missed. Percentage points of the expected relative return.
| source | 12m: 1st order | 12m: 2nd–4th order | 12m total | 3m total |
|---|---|---|---|---|
| Policy | +0.00 | +0.08 | +0.08 | -0.13 |
| Regulatory | -0.34 | -0.03 | -0.37 | -0.04 |
| Sector | -0.33 | +1.51 | +1.18 | +0.74 |
| Theme | +0.00 | +0.14 | +0.14 | +0.09 |
| Geopolitics | +0.16 | -0.04 | +0.12 | +0.08 |
| Company catalysts | +0.10 | -0.01 | +0.09 | +0.09 |
| Market-priced macro | +0.00 | +0.00 | +0.00 | +0.00 |
| Beta adjustment | — | — | -0.57 | -0.26 |
| Universe centring | — | — | -0.15 | -0.10 |
| **Expected relative return** | | | **+0.52** | **+0.48** |

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Credit cost / NPA cycle (higher = worse) (`F_ASSET_QUALITY_IN`) | +50 bp credit cost | -6.05 | -6.00 | +0.00 | -0.03 | -0.02 | — |
| India real GDP growth (`F_GDP_IN`) | +1 pp | +4.24 | +2.50 | +2.19 | -0.27 | -0.18 | — |
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | +4.03 | +0.00 | +2.80 | +1.42 | -0.18 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -4.01 | -2.50 | -0.36 | -0.58 | -0.57 | — |
| Bank deposit growth / funding ease (`F_DEPOSIT_GROWTH_IN`) | +3 pp | +3.73 | +3.50 | +0.40 | -0.10 | -0.07 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +3.56 | +3.50 | +0.07 | -0.02 | +0.01 | — |
| RBI prudential tightening (risk weights, LCR, provisioning) (`P_RBI_PRUDENTIAL`) | +1 = tightening step | -3.26 | -2.00 | -1.46 | +0.13 | +0.07 | — |
| Private corporate capex (`F_PRIVATE_CAPEX`) | +10% capex growth | +3.01 | +0.00 | +2.00 | +1.26 | -0.25 | — |
| Monsoon rainfall vs normal (`F_MONSOON`) | +10% above long-period average | +2.68 | +0.00 | +0.91 | +1.24 | +0.53 | — |
| Unsecured retail & microfinance stress (higher = worse) (`F_UNSECURED_STRESS`) | +1 pp delinquencies | -2.39 | -1.50 | -0.68 | -0.11 | -0.10 | — |
| Central + state government capex (`F_GOVT_CAPEX`) | +10% capex growth | +2.04 | +0.00 | +0.90 | +1.04 | +0.11 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -1.92 | +0.00 | -0.93 | -0.18 | -0.81 | -1.1% |
| India 10-year G-sec yield (`F_GSEC_10Y_IN`) | +25 bp yield | -1.88 | -1.80 | +0.00 | -0.05 | -0.03 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -1.84 | +0.00 | -0.90 | -1.07 | +0.12 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -7.8% | -7.8% | -7.7 | -0.2 | +0.0 | -0.0 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +8.9% | +4.4% | +8.8 | +0.1 | -0.0 | +0.0 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -3.4% | -3.4% | +0.0 | -1.1 | -1.6 | -0.7 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -3.1% | -3.1% | -2.5 | -0.4 | -0.1 | -0.0 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.55 | +5.1% | +2.8% | +3.3 | +0.9 | +0.7 | +0.1 |
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -2.8% | -2.8% | -2.5 | +0.0 | -0.2 | -0.1 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -2.5% | -2.5% | +0.0 | -1.0 | -1.5 | +0.0 |
| India Q1 FY27 GDP grows 7.8% (31 Aug 2026), beating ~7.3% consensus (`EV_GDP_Q1FY27_7_8`) | occurred | 1.00 | +2.2% | +2.2% | +1.2 | +1.1 | -0.1 | -0.1 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.25 | -7.9% | -2.0% | -4.3 | -2.0 | -1.3 | -0.3 |
| US midterms (3 Nov 2026): Democrats win House and Senate (`EV_US_MIDTERMS_DEM_SWEEP`) | occurred | 1.00 | +1.9% | +1.9% | +1.8 | +0.1 | +0.0 | +0.0 |
| IMD April 2027 long-range forecast says normal or above-normal monsoon (>=96% LPA) (`EV_MONSOON27_FIRST_FORECAST_NORMAL`) | scheduled | 0.68 | +2.7% | +1.8% | +0.0 | +0.9 | +1.4 | +0.4 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -1.7% | -1.7% | -1.0 | -0.5 | -0.1 | -0.2 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → HDFCBANK | +8.75% | +4.38% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ C_MIDEAST_CONFLICT → HDFCBANK | +2.50% | +1.38% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → HDFCBANK | -5.25% | -0.95% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → HDFCBANK | -3.27% | -0.82% |
| 1 | EV_ECL_ROLLOUT_APR27 ⇒ F_ASSET_QUALITY_IN → HDFCBANK | -0.90% | -0.81% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ C_MIDEAST_CONFLICT → HDFCBANK | -3.00% | -0.75% |
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → HDFCBANK | -1.44% | -0.72% |
| 1 | EV_BANKING_LIQUIDITY_DEFICIT_MAR27 ⇒ F_DEPOSIT_GROWTH_IN → HDFCBANK | +1.05% | +0.63% |
| 1 | EV_BUDGET_FY28_LTCG_RELIEF ⇒ F_FPI_FLOWS → HDFCBANK | +1.75% | +0.61% |
| 1 | EV_Q2_FY27_GDP_STRONG ⇒ F_FPI_FLOWS → HDFCBANK | +0.70% | +0.56% |
| 1 | EV_ECL_ROLLOUT_APR27 ⇒ P_RBI_PRUDENTIAL → HDFCBANK | -0.60% | -0.54% |
| 2 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → HDFCBANK | -3.27% | -0.49% |
| 2 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_GDP_IN → HDFCBANK | +0.67% | +0.45% |
| 1 | EV_INDIA_STAGFLATION_SCARE ⇒ F_GDP_IN → HDFCBANK | -3.75% | -0.45% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → HDFCBANK | +0.78% | +0.43% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_FPI_FLOWS → HDFCBANK | -1.60 | events | -5.60% |
| 1 | F_GSEC_10Y_IN → HDFCBANK | +1.55 | director_override | -2.79% |
| 1 | C_MIDEAST_CONFLICT → HDFCBANK | +1.00 | events | -2.50% |
| 1 | F_GDP_IN → HDFCBANK | +0.50 | events | +1.25% |
| 1 | F_REPO_IN → HDFCBANK | +1.00 | events | -0.50% |
| 2 | F_GDP_IN → F_ASSET_QUALITY_IN → HDFCBANK | +0.50 | events | +0.48% |
| 2 | F_LIQUIDITY_IN → F_DEPOSIT_GROWTH_IN → HDFCBANK | -0.90 | events | -0.38% |
| 2 | F_MONSOON → F_UNSECURED_STRESS → HDFCBANK | -1.56 | events | -0.37% |
| 2 | F_REPO_IN → F_CREDIT_GROWTH_IN → HDFCBANK | +1.00 | events | -0.29% |
| 2 | F_RURAL_DEMAND → F_ASSET_QUALITY_IN → HDFCBANK | -0.25 | events | -0.24% |
| 2 | F_REPO_IN → F_ASSET_QUALITY_IN → HDFCBANK | +1.00 | events | -0.24% |
| 2 | F_GDP_IN → F_CREDIT_GROWTH_IN → HDFCBANK | +0.50 | events | +0.21% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-12 | Further senior-management departures or appointments (BusinessLine 2026-11-02: another senior executive departs) | other | 0.50 | -0.5% | -0.25% |
| 2027-01-17 | Q3 FY27 results - first full quarter under CEO Bagchi (date inferred; Q2 on 2026-10-17) | results | 0.90 | +0.5% | +0.45% |

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