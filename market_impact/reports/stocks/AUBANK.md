# AUBANK — AU Small Finance Bank Ltd.
*MIDCAP_100 · Financial Services · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -4.1%**, **12 months -7.5%** (rank 188 / 189 of 200 for 3m / 12m); beta 0.95
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +22.5%): 3 months 36%, 12 months 60%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -13.5% … P90 -1.0%; plausible 12m relative-return range incl. stock-specific noise: -14.5% … +21.0%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves -0.7 pp (model impact -8.5% beta-adjusted vs realised market-adjusted move -7.1%); forward event exposure -9.1% (3m -4.5%; half assumed priced); company-specific events -2.3%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Credit cost / NPA cycle (higher = worse) (`F_ASSET_QUALITY_IN`) | +50 bp credit cost | -7.02 | -7.00 | +0.00 | -0.03 | +0.02 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -6.52 | +0.00 | -3.94 | -2.93 | +0.35 | — |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +5.79 | +0.00 | +2.78 | +1.72 | +1.29 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -5.32 | +0.00 | -2.16 | -2.09 | -1.07 | -1.1% |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -4.26 | +0.00 | -0.16 | -2.36 | -1.74 | — |
| RBI prudential tightening (risk weights, LCR, provisioning) (`P_RBI_PRUDENTIAL`) | +1 = tightening step | -4.15 | -3.00 | -1.54 | +0.33 | +0.07 | — |
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | +3.47 | +2.00 | +1.25 | +0.86 | -0.64 | — |
| Unsecured retail & microfinance stress (higher = worse) (`F_UNSECURED_STRESS`) | +1 pp delinquencies | -3.44 | -2.50 | -0.88 | -0.02 | -0.04 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -3.38 | -2.50 | -0.99 | +0.21 | -0.10 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +3.34 | +3.00 | +0.06 | +0.10 | +0.18 | — |
| Monsoon rainfall vs normal (`F_MONSOON`) | +10% above long-period average | +3.21 | +0.00 | +0.85 | +1.48 | +0.88 | — |
| Indian vehicle demand (`F_AUTO_DEMAND_IN`) | +10% volumes | +3.00 | +3.00 | +0.00 | +0.00 | +0.00 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -2.86 | +0.00 | +0.00 | -0.74 | -2.12 | — |
| Brent crude oil price (`F_BRENT`) | +10% Brent | -2.76 | +0.00 | -0.36 | -1.55 | -0.85 | +0.0% |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -8.0% | -8.0% | +0.0 | -4.7 | -3.6 | +0.3 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -7.4% | -7.4% | -6.6 | -0.1 | -0.2 | -0.4 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +8.5% | +4.3% | +7.5 | +0.2 | +0.3 | +0.6 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -4.0% | -4.0% | +0.0 | -1.1 | -1.9 | -1.1 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -3.6% | -3.6% | -3.0 | -0.7 | +0.2 | -0.1 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -2.9% | -2.9% | -2.6 | -0.2 | -0.0 | -0.1 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.55 | +4.6% | +2.6% | +0.0 | +0.9 | +2.3 | +1.4 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -2.4% | -2.4% | +0.0 | -1.6 | -0.5 | -0.3 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.25 | -8.6% | -2.1% | +0.0 | -1.9 | -4.2 | -2.5 |
| Kharif 2026 output hit: paddy area down, foodgrain target cut, rice output seen sharpest fall in ~2 decades (`EV_KHARIF26_OUTPUT_HIT`) | occurred | 1.00 | -2.1% | -2.1% | +0.0 | -0.1 | -1.2 | -0.9 |
| IMD April 2027 long-range forecast says normal or above-normal monsoon (>=96% LPA) (`EV_MONSOON27_FIRST_FORECAST_NORMAL`) | scheduled | 0.68 | +3.0% | +2.1% | +0.0 | +0.9 | +1.9 | +0.3 |
| RBI expected-credit-loss (ECL) provisioning goes live as scheduled (FY28 start) (`EV_ECL_ROLLOUT_APR27`) | scheduled | 0.90 | -2.2% | -2.0% | -2.3 | +0.1 | +0.0 | +0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → AUBANK | +7.50% | +3.75% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → AUBANK | -2.50% | -1.05% |
| 1 | EV_ECL_ROLLOUT_APR27 ⇒ F_ASSET_QUALITY_IN → AUBANK | -1.05% | -0.95% |
| 1 | EV_BANKING_LIQUIDITY_DEFICIT_MAR27 ⇒ F_LIQUIDITY_IN → AUBANK | -1.50% | -0.90% |
| 1 | EV_RBI_GOLD_LOAN_TIGHTEN ⇒ P_RBI_PRUDENTIAL → AUBANK | -3.00% | -0.90% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → AUBANK | -4.50% | -0.81% |
| 1 | EV_ECL_ROLLOUT_APR27 ⇒ P_RBI_PRUDENTIAL → AUBANK | -0.90% | -0.81% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → AUBANK | -2.88% | -0.72% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_FPI_FLOWS → AUBANK | -2.88% | -0.72% |
| 2 | EV_PULSES_VEG_SPIKE_WINTER ⇒ F_CPI_IN → F_REPO_IN → AUBANK | -2.88% | -0.72% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → AUBANK | -2.80% | -0.70% |
| 1 | EV_RBI_FEB27_HIKE25 ⇒ F_REPO_IN → AUBANK | -2.50% | -0.68% |
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → AUBANK | -1.20% | -0.60% |
| 1 | EV_CPI_BREACH_6PCT ⇒ F_REPO_IN → AUBANK | -1.00% | -0.60% |
| 3 | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → F_GDP_IN → F_ASSET_QUALITY_IN → AUBANK | +0.60% | +0.54% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_FPI_FLOWS → AUBANK | -1.60 | events | -4.80% |
| 1 | F_REPO_IN → AUBANK | +1.00 | events | -2.50% |
| 1 | F_GSEC_10Y_IN → AUBANK | +1.55 | director_override | -2.33% |
| 2 | F_GDP_IN → F_ASSET_QUALITY_IN → AUBANK | +0.50 | events | +1.12% |
| 1 | F_LIQUIDITY_IN → AUBANK | -0.90 | events | -0.90% |
| 2 | F_MONSOON → F_UNSECURED_STRESS → AUBANK | -1.56 | events | -0.62% |
| 1 | F_RURAL_DEMAND → AUBANK | -0.25 | events | -0.50% |
| 2 | F_GDP_IN → F_CREDIT_GROWTH_IN → AUBANK | +0.50 | events | +0.43% |
| 2 | F_CPI_IN → F_UNSECURED_STRESS → AUBANK | +1.15 | events | -0.35% |
| 1 | F_AUTO_DEMAND_IN → AUBANK | -0.10 | events | -0.30% |
| 2 | F_REPO_IN → F_CREDIT_GROWTH_IN → AUBANK | +1.00 | events | -0.29% |
| 2 | F_REPO_IN → F_ASSET_QUALITY_IN → AUBANK | +1.00 | events | -0.28% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-12 | Data-leak investigation outcome and possible RBI/regulatory action | regulatory | 0.40 | -2.2% | -0.90% |
| 2027-01 | Q3 FY27 results (inferred; Q2 call 2026-10-24): NIM trend and credit cost | results | 0.92 | -0.5% | -0.46% |
| 2027-03 | Universal bank transition milestones (licence terms, branch/CASA targets); stage not independently verified | regulatory | 0.50 | +1.5% | +0.75% |
| 2027-04 | ECL framework effective; AU's transition hit unquantified | regulatory | 0.85 | -2.0% | -1.70% |

## Analyst profile (agent research, sourced)
# AUBANK - AU Small Finance Bank Ltd. (Nifty 200, I_PRIVATE_BANKS) - as of 2026-11-05

## Business
AU Small Finance Bank is a Rajasthan-origin lender that has become one of India's largest small finance banks and is transitioning to universal-bank status. Vehicle finance (Wheels AUM above Rs50,000cr) is the largest segment, followed by SME, commercial and mortgage loans, with microfinance (ex-Fincare, 1,000+ branches), cards and personal loans. Funding is deposit-heavy, mostly retail term deposits. Foreign investors own about 36%, domestic institutions 33%, promoters 22.7%. The stock trades at 22.4x earnings and 3.3x book but is down 13% in three months after management flagged margin pressure on 2026-10-26.

## What moves the stock, ranked
1. **Credit cost (F_ASSET_QUALITY_IN -7.0) and unsecured/MFI stress (-2.5).** Vehicle, SME and MFI books are cyclical.
2. **Margin: repo (-2.5), deposits (+2.0), liquidity (+1.0), G-sec (-1.5).** The October hike raises deposit costs against largely fixed-rate assets; management said so on the Q2 call.
3. **Growth drivers: auto demand (+3.0), credit growth (+2.5), rural demand (+2.0).**
4. **Regulation and operations (P_RBI_PRUDENTIAL -3.0).** Universal-bank transition conditions, ECL from April 2027 and the data-leak probe (2026-10-30).
5. **Flows (+3.0).** High FII ownership makes the stock sensitive to foreign flows.

## Transmission examples
- **Oil -> rates -> margin:** Brent at 95 -> CPI up -> RBI hikes -> term deposit rates rise within quarters while vehicle loans are mostly fixed-rate -> NIM falls (the exact warning on 2026-10-26) -> EPS growth slows -> multiple falls.
- **Rural/auto chain:** good monsoon and festival demand -> vehicle and tractor sales up -> Wheels disbursement up -> AUM growth stays at 20%+ -> operating leverage; weak rural incomes raise MFI and vehicle delinquency.
- **Regulatory chain:** data leak -> RBI scrutiny of cyber-security and customer data -> possible restrictions or penalties -> brand and deposit-gathering hit during the universal-bank transition.
- **Ownership chain:** ICICI Pru AMC buying up to 9.95% (RBI approved) -> institutional demand supports the price; FII selling after the margin warning does the opposite.

## Current situation and bull/bear
Q2 PAT Rs858cr (+53%) but market punished margin guidance. Brokerages (Jefferies, Motilal) see up to 37% upside. Bull: margins stabilise as deposits reprice, universal-bank licence lifts CASA, auto cycle strong. Bear: deposit costs keep rising with more RBI hikes, credit cost normalises, data-leak action. Confidence is low because balance-sheet splits and the exact licence status are model estimates or unverified.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.