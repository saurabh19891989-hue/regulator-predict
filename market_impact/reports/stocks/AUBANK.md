# AUBANK — AU Small Finance Bank Ltd.
*MIDCAP_100 · Financial Services · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -4.8%**, **12 months -9.5%** (rank 191 / 189 of 200 for 3m / 12m); beta 0.95
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +22.5%): 3 months 33%, 12 months 38%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -24.8% … P90 -2.5%; plausible 12m relative-return range incl. stock-specific noise: -27.9% … +24.2%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves -0.6 pp (model impact -8.3% beta-adjusted vs realised market-adjusted move -7.1%); forward event exposure -13.2% (3m -6.1%; half assumed priced); company-specific events -2.3%

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
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -14.7% | -14.7% | +0.0 | -1.8 | -8.2 | -4.8 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -8.0% | -8.0% | +0.0 | -4.7 | -3.6 | +0.3 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -7.5% | -7.5% | -6.6 | -0.1 | -0.3 | -0.5 |
| RBI expected-credit-loss (ECL) provisioning goes live as scheduled (FY28 start) (`EV_ECL_ROLLOUT_APR27`) | scheduled | 0.62 | -7.2% | -4.5% | -7.8 | +0.5 | +0.0 | +0.0 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +8.5% | +4.3% | +7.5 | +0.2 | +0.3 | +0.6 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -4.0% | -4.0% | +0.0 | -1.1 | -1.9 | -1.1 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -3.6% | -3.6% | -3.0 | -0.7 | +0.2 | -0.1 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.36 | -9.9% | -3.5% | +0.0 | -2.2 | -4.8 | -2.8 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -3.3% | -3.3% | +0.0 | -2.6 | -0.3 | -0.3 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.58 | +5.4% | +3.1% | +0.0 | +1.1 | +2.7 | +1.6 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -2.9% | -2.9% | -2.6 | -0.2 | -0.0 | -0.1 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.28 | -10.2% | -2.9% | +0.0 | -7.4 | -1.6 | -1.2 |

## Strongest causal chains (1st–4th order)
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_RECORD_OUTFLOW_26 ⇒ F_FPI_FLOWS → AUBANK | -6.60% | -6.60% |
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → AUBANK | +7.50% | +3.75% |
| 2 | EV_CPI_REACCEL_SEP26 ⇒ F_CPI_IN → F_REPO_IN → AUBANK | -3.31% | -3.31% |
| 1 | EV_RBI_OCT26_HIKE25 ⇒ F_REPO_IN → AUBANK | -2.50% | -2.50% |
| 3 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_CPI_IN → F_REPO_IN → AUBANK | -2.21% | -2.21% |
| 1 | EV_ECL_ROLLOUT_APR27 ⇒ F_ASSET_QUALITY_IN → AUBANK | -3.50% | -2.17% |
| 1 | EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26 ⇒ F_GSEC_10Y_IN → AUBANK | -2.10% | -2.10% |
| 1 | EV_ECL_ROLLOUT_APR27 ⇒ P_RBI_PRUDENTIAL → AUBANK | -3.00% | -1.86% |
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_FPI_FLOWS → AUBANK | -1.78% | -1.78% |
| 1 | EV_US_MIDTERMS_DEM_SWEEP ⇒ F_FPI_FLOWS → AUBANK | +1.50% | +1.50% |
| 3 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_USDINR → F_FPI_FLOWS → AUBANK | -1.41% | -1.41% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → AUBANK | -4.48% | -1.25% |
| 3 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_GDP_IN → F_ASSET_QUALITY_IN → AUBANK | -1.25% | -1.25% |
| 3 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_USDINR → F_LIQUIDITY_IN → AUBANK | -1.17% | -1.17% |
| 4 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_USDINR → NEW_FX_RESERVES_IN → F_LIQUIDITY_IN → AUBANK | -1.15% | -1.15% |

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