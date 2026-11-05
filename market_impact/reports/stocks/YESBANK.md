# YESBANK — Yes Bank Ltd.
*MIDCAP_100 · Financial Services · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -4.2%**, **12 months -6.0%** (rank 199 / 197 of 200 for 3m / 12m); beta 1.04
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +32.3%): 3 months 40%, 12 months 45%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -14.3% … P90 +0.6%; plausible 12m relative-return range incl. stock-specific noise: -39.8% … +26.5%
- Decomposition (12m): 0.5 × forward event exposure -10.3% (3m -5.9%; half assumed priced) + 0.5 × company-specific catalysts -0.8%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply -9.8% (beta-adjusted) vs a realised market-adjusted move of -35.3% — gap +25.5 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Credit cost / NPA cycle (higher = worse) (`F_ASSET_QUALITY_IN`) | +50 bp credit cost | -10.25 | -10.00 | -0.18 | -0.05 | -0.02 | — |
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | +5.06 | +0.00 | +4.48 | +1.34 | -0.76 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -4.86 | +0.00 | -3.59 | -1.41 | +0.14 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -4.49 | -3.00 | -1.40 | +0.01 | -0.10 | — |
| India real GDP growth (`F_GDP_IN`) | +1 pp | +4.38 | +4.00 | +1.92 | -1.24 | -0.30 | — |
| RBI prudential tightening (risk weights, LCR, provisioning) (`P_RBI_PRUDENTIAL`) | +1 = tightening step | -4.07 | -2.00 | -2.61 | +0.42 | +0.12 | — |
| Monsoon rainfall vs normal (`F_MONSOON`) | +10% above long-period average | +3.91 | +0.00 | +1.39 | +1.60 | +0.93 | — |
| Bank deposit growth / funding ease (`F_DEPOSIT_GROWTH_IN`) | +3 pp | +3.77 | +3.50 | +0.73 | -0.30 | -0.16 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +3.39 | +3.00 | +0.17 | +0.02 | +0.21 | — |
| India FX reserves (RBI intervention) (`NEW_FX_RESERVES_IN`) | +US$25bn reserves (RBI buys / net inflows) | +3.31 | +0.00 | +2.37 | +0.80 | +0.15 | — |
| Private corporate capex (`F_PRIVATE_CAPEX`) | +10% capex growth | +3.31 | +0.00 | +3.20 | +0.99 | -0.88 | — |
| Unsecured retail & microfinance stress (higher = worse) (`F_UNSECURED_STRESS`) | +1 pp delinquencies | -3.29 | -2.00 | -1.12 | -0.13 | -0.04 | — |
| India 10-year G-sec yield (`F_GSEC_10Y_IN`) | +25 bp yield | -3.27 | -3.00 | -0.15 | -0.09 | -0.03 | — |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -3.19 | +0.00 | +0.00 | -2.31 | -0.87 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -7.5% | -7.5% | -6.6 | -0.4 | -0.0 | -0.5 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -6.1% | -6.1% | +0.0 | -4.1 | -2.0 | +0.1 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -6.1% | -6.1% | -5.6 | -0.3 | -0.1 | -0.0 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -5.1% | -5.1% | -4.2 | -0.8 | +0.0 | -0.1 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -4.9% | -4.9% | +0.0 | -1.7 | -2.0 | -1.2 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +8.6% | +4.3% | +7.5 | +0.4 | +0.0 | +0.6 |
| Risk: USD/INR >98 and/or reserves < US$650bn (disorderly rupee, emergency RBI response) (`EV_RUPEE_BREAK_98_RESERVE_STRESS`) | risk_scenario | 0.18 | -15.8% | -2.8% | -14.2 | -1.4 | -0.0 | -0.2 |
| IMD April 2027 long-range forecast says normal or above-normal monsoon (>=96% LPA) (`EV_MONSOON27_FIRST_FORECAST_NORMAL`) | scheduled | 0.68 | +3.6% | +2.5% | +0.0 | +1.4 | +2.1 | +0.2 |
| CPI prints >=6.0% (RBI upper tolerance) in Oct-Jan data (releases 12 Nov - 12 Feb) (`EV_CPI_BREACH_6PCT`) | anticipated | 0.60 | -3.9% | -2.3% | -2.7 | -1.0 | -0.3 | +0.0 |
| RBI expected-credit-loss (ECL) provisioning goes live as scheduled (FY28 start) (`EV_ECL_ROLLOUT_APR27`) | scheduled | 0.90 | -2.6% | -2.3% | -2.7 | +0.1 | +0.0 | +0.0 |
| India Q1 FY27 GDP grows 7.8% (31 Aug 2026), beating ~7.3% consensus (`EV_GDP_Q1FY27_7_8`) | occurred | 1.00 | +2.3% | +2.3% | +2.0 | +1.0 | -0.5 | -0.2 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -2.2% | -2.2% | +0.0 | -1.8 | -0.4 | +0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → YESBANK | +7.50% | +3.75% |
| 1 | EV_BANKING_LIQUIDITY_DEFICIT_MAR27 ⇒ F_LIQUIDITY_IN → YESBANK | -3.00% | -1.80% |
| 1 | EV_ECL_ROLLOUT_APR27 ⇒ F_ASSET_QUALITY_IN → YESBANK | -1.50% | -1.35% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → YESBANK | -3.00% | -1.26% |
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → YESBANK | -2.40% | -1.20% |
| 1 | EV_CPI_BREACH_6PCT ⇒ F_GSEC_10Y_IN → YESBANK | -1.50% | -0.90% |
| 1 | EV_RBI_FEB27_HIKE25 ⇒ F_REPO_IN → YESBANK | -3.00% | -0.81% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → YESBANK | -4.50% | -0.81% |
| 2 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_GDP_IN → YESBANK | +1.07% | +0.73% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → YESBANK | -2.88% | -0.72% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_FPI_FLOWS → YESBANK | -2.88% | -0.72% |
| 1 | EV_CPI_BREACH_6PCT ⇒ F_REPO_IN → YESBANK | -1.20% | -0.72% |
| 1 | EV_INDIA_STAGFLATION_SCARE ⇒ F_GDP_IN → YESBANK | -6.00% | -0.72% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → YESBANK | -2.80% | -0.70% |
| 1 | EV_Q2_FY27_GDP_STRONG ⇒ F_GDP_IN → YESBANK | +0.80% | +0.64% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_FPI_FLOWS → YESBANK | -1.60 | events | -4.80% |
| 1 | F_GSEC_10Y_IN → YESBANK | +1.55 | director_override | -4.65% |
| 1 | F_REPO_IN → YESBANK | +1.00 | events | -3.00% |
| 1 | F_GDP_IN → YESBANK | +0.50 | events | +2.00% |
| 1 | F_LIQUIDITY_IN → YESBANK | -0.90 | events | -1.80% |
| 2 | F_GDP_IN → F_ASSET_QUALITY_IN → YESBANK | +0.50 | events | +0.80% |
| 1 | F_CREDIT_SPREADS_IN → YESBANK | +0.50 | events | -0.75% |
| 2 | F_MONSOON → F_UNSECURED_STRESS → YESBANK | -1.56 | events | -0.50% |
| 2 | F_REPO_IN → F_CREDIT_GROWTH_IN → YESBANK | +1.00 | events | -0.47% |
| 2 | F_RURAL_DEMAND → F_ASSET_QUALITY_IN → YESBANK | -0.25 | events | -0.40% |
| 2 | F_REPO_IN → F_ASSET_QUALITY_IN → YESBANK | +1.00 | events | -0.40% |
| 2 | F_GDP_IN → F_CREDIT_GROWTH_IN → YESBANK | +0.50 | events | +0.34% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-12 | Yes Bank decision on further legal remedy (review/curative petition) on AT1 ruling; provisioning decision for Rs 8.4k cr write-off reversal | litigation | 0.50 | +0.0% | +0.00% |
| 2027-01 | Q3 FY27 results: first booking (or not) of AT1 liability, NIM post-hike | results | 0.95 | -2.0% | -1.90% |
| 2027-06 | SMBC raises stake / capital infusion (Reuters 2026-10-14 lists large cross-border financial deals; SMBC reportedly priced in adverse AT1 verdict, Moneycontrol 2026-10-22) | corporate_action | 0.15 | +7.5% | +1.12% |

## Analyst profile (agent research, sourced)
# YESBANK - Yes Bank Ltd. (Midcap 100, private banks)

## Business
Yes Bank is a mid-sized private bank rebuilt since the March 2020 reconstruction, now anchored by SMBC. Sep-2026 balance sheet: deposits Rs 3.54 lakh crore, borrowings Rs 78,410 cr, investments Rs 99,968 cr, net worth about Rs 53,400 cr. Funding cost is high (interest expense is 67% of Q2 revenue), so the bank's economics depend on deposit mix, repo-linked loan repricing and credit costs. TTM net profit is Rs 4,195 cr, ROE only 7%, and the stock trades at 0.94x book.

## What moves the stock, ranked
1. **AT1 litigation outcome (company-specific).** The Supreme Court on 2026-10-15 set aside the 2020 write-off of Rs 8,415 cr AT1 bonds; the stock fell 17% in two days. Estimates of the earnings hit are Rs 5,217-5,400 cr (ET, CNBC TV18 headlines), unbooked pending a further appeal (Reuters 2026-10-17). That is about 10% of net worth and of market cap.
2. **Asset quality / credit cost (-10 per +50bp).** Low provisions are what lifts profits today; a small reversal of that tailwind has outsized effect on a Rs 4.2k cr profit base.
3. **Funding cost and NIM (repo -3.0, deposit growth +3.5, liquidity +2.0).**
4. **Treasury MTM and discount rate (G-sec -3.0).**
5. **Growth and macro (credit growth +4, GDP +4).**
6. **Foreign flows (+3.0)** with FIIs at 47.8%.

## Transmission examples
- **Oil shock -> inflation -> RBI hikes more:** Brent +10% (1st) -> CPI +0.3pp (2nd) -> RBI second hike after 2026-10-07 (3rd) -> repo-linked assets reprice before deposits, NIM -6bp, bond MTM loss on AFS (4th) -> EPS -4%, valuation -3%.
- **Unsecured stress at fintech/NBFC peers -> RBI prudential tightening -> risk-weights up -> CET1 down at a bank already absorbing an AT1 charge.**
- **SMBC channel:** Japanese bank balance-sheet and yen funding costs -> SMBC appetite for further capital in India -> Yes Bank capital cushion. Positive if SMBC adds equity (Reuters lists large cross-border financial deals in 2026).
- **FPI flows:** US midterm result (2026-11-04/05) -> risk-on -> FPI inflows -> high-beta, high-FII bank outperforms; but the foreign limit caps buying.

## Current situation
Q2 FY27: net profit Rs 1,084 cr (+63-65% YoY), NII +23%, asset quality stable, but AT1 charge excluded. Nomura cut its target to Rs 18; ten brokers had Sell/Underperform calls on 2026-10-21. Stock Rs 16, 52-week range 15.1-25.8. DIIs and FIIs increased holdings in Sep 2026; public fell to 29.1%.

## Upcoming events
Decision on further legal remedies and provisioning (Dec 2026-Jan 2027), Q3 results (Jan 2027), RBI MPC (Dec), possible SMBC stake raise.

## Bull and bear
**Bull:** the market already prices the full AT1 charge (~10% of cap) and the stock is at 0.94x book with improving core earnings; review petition or negotiated settlement is a call option; SMBC support. **Bear:** the full charge cuts CET1 and capital-raising options, ROE stays single-digit, repo hikes pressure NIM, and the AT1 episode keeps tier-1 market access shut. Confidence medium: figures come from headlines and screener; no primary filing or earnings-call text was retrievable.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.