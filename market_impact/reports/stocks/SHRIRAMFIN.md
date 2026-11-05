# SHRIRAMFIN — Shriram Finance Ltd.
*NIFTY_50 · Financial Services · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -5.1%**, **12 months -7.3%** (rank 193 / 181 of 200 for 3m / 12m); beta 1.42
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +27.0%): 3 months 35%, 12 months 32%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -16.5% … P90 -2.6%; plausible 12m relative-return range incl. stock-specific noise: -38.7% … +22.3%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves -3.5 pp (model impact -8.9% beta-adjusted vs realised market-adjusted move -1.8%); forward event exposure -6.6% (3m -4.4%; half assumed priced); company-specific events +1.4%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| India CPI inflation (`F_CPI_IN`) | +1 pp | -7.10 | +0.00 | -3.30 | -3.48 | -0.32 | — |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +6.11 | +0.00 | +2.87 | +2.16 | +1.09 | — |
| Credit cost / NPA cycle (higher = worse) (`F_ASSET_QUALITY_IN`) | +50 bp credit cost | -4.86 | -4.50 | -0.30 | -0.03 | -0.02 | — |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -4.08 | +0.00 | +0.00 | -2.10 | -1.98 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -3.92 | -2.50 | -1.09 | -0.22 | -0.11 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -3.67 | +0.00 | -1.20 | -1.14 | -1.33 | — |
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | +3.61 | +0.00 | +3.79 | +0.89 | -1.07 | — |
| RBI prudential tightening (risk weights, LCR, provisioning) (`P_RBI_PRUDENTIAL`) | +1 = tightening step | -3.60 | -2.00 | -1.63 | +0.02 | +0.00 | — |
| Indian vehicle demand (`F_AUTO_DEMAND_IN`) | +10% volumes | +3.50 | +3.50 | +0.00 | +0.00 | +0.00 | — |
| Monsoon rainfall vs normal (`F_MONSOON`) | +10% above long-period average | +3.34 | +2.00 | +0.40 | +0.62 | +0.32 | — |
| Indian corporate credit spreads (`F_CREDIT_SPREADS_IN`) | +50 bp spreads | -2.78 | -2.50 | -0.15 | -0.10 | -0.03 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +2.73 | +2.50 | +0.09 | +0.03 | +0.12 | — |
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +2.61 | +0.00 | +2.88 | +0.40 | -0.67 | — |
| India real GDP growth (`F_GDP_IN`) | +1 pp | +2.38 | +3.00 | +0.53 | -0.88 | -0.28 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -11.7% | -11.7% | -5.0 | -1.9 | -2.7 | -2.3 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -8.6% | -8.6% | +0.0 | -3.8 | -4.3 | -0.4 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -6.1% | -6.1% | -5.5 | -0.2 | -0.1 | -0.3 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -4.5% | -4.5% | -3.5 | -0.7 | -0.2 | -0.2 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -4.2% | -4.2% | -2.5 | -0.5 | -0.8 | -0.4 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -4.1% | -4.1% | -2.0 | -1.6 | -0.3 | -0.2 |
| RBI expected-credit-loss (ECL) provisioning goes live as scheduled (FY28 start) (`EV_ECL_ROLLOUT_APR27`) | scheduled | 0.62 | -5.9% | -3.6% | -5.5 | -0.4 | -0.0 | +0.0 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +6.9% | +3.5% | +6.2 | +0.2 | +0.1 | +0.4 |
| Gold and silver slump from January 2026 peaks (silver -53%, gold -24%) (`EV_PRECIOUS_METALS_CRASH_2026`) | occurred | 1.00 | -3.4% | -3.4% | -1.8 | -1.5 | -0.1 | -0.1 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -3.2% | -3.2% | -2.8 | -0.1 | -0.2 | -0.0 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -2.9% | -2.9% | -1.0 | -1.1 | -0.5 | -0.3 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.36 | -7.8% | -2.8% | -2.5 | -2.1 | -1.8 | -1.4 |

## Strongest causal chains (1st–4th order)
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_RECORD_OUTFLOW_26 ⇒ F_FPI_FLOWS → SHRIRAMFIN | -5.50% | -5.50% |
| 1 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → SHRIRAMFIN | -4.95% | -4.95% |
| 2 | EV_CPI_REACCEL_SEP26 ⇒ F_CPI_IN → F_REPO_IN → SHRIRAMFIN | -3.31% | -3.31% |
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → SHRIRAMFIN | +6.25% | +3.12% |
| 1 | EV_SWMONSOON26_DEFICIT ⇒ F_MONSOON → SHRIRAMFIN | -2.52% | -2.52% |
| 1 | EV_RBI_OCT26_HIKE25 ⇒ F_REPO_IN → SHRIRAMFIN | -2.50% | -2.50% |
| 1 | EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26 ⇒ F_GSEC_10Y_IN → SHRIRAMFIN | -2.10% | -2.10% |
| 1 | EV_UST_SELLOFF_SEP26 ⇒ F_US_10Y → SHRIRAMFIN | -2.04% | -2.04% |
| 1 | EV_PRECIOUS_METALS_CRASH_2026 ⇒ F_US_10Y → SHRIRAMFIN | -1.80% | -1.80% |
| 1 | EV_GDP_Q1FY27_7_8 ⇒ F_GDP_IN → SHRIRAMFIN | +1.50% | +1.50% |
| 1 | EV_ECL_ROLLOUT_APR27 ⇒ F_ASSET_QUALITY_IN → SHRIRAMFIN | -2.25% | -1.40% |
| 1 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → SHRIRAMFIN | +2.00% | +1.36% |
| 1 | EV_US_MIDTERMS_DEM_SWEEP ⇒ F_FPI_FLOWS → SHRIRAMFIN | +1.25% | +1.25% |
| 1 | EV_ECL_ROLLOUT_APR27 ⇒ P_RBI_PRUDENTIAL → SHRIRAMFIN | -2.00% | -1.24% |
| 3 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_CPI_IN → F_REPO_IN → SHRIRAMFIN | -1.11% | -1.11% |

## Analyst profile (agent research, sourced)
# SHRIRAMFIN - Shriram Finance Ltd. (Nifty 50, NBFC vehicle/consumer)

## Business
Shriram Finance is India's dominant lender against used commercial vehicles, serving small truck operators, plus new CVs, passenger vehicles, tractors, MSME loans, gold loans and personal loans. AUM crossed Rs 3.3 lakh crore in Q2 FY27 (Investing.com slides headline, 2026-10-23); borrowings are Rs 2.36 lakh crore (screener, Sep 2026) funded by bank term loans, NCDs, public deposits and ECBs. Financing margin has expanded to 37% (Sep-26 quarter) as funding cost fell during the 2025-26 easing cycle. MUFG Bank holds ~20% after a large preferential issue (equity plus reserves rose from Rs 65.5k cr to Rs 111k cr), which also supports capital adequacy and a cheaper funding franchise.

## What moves the stock, ranked
1. **Asset quality / credit cost (F_ASSET_QUALITY_IN, weight -4.5 per +50bp).** Q2 FY27 Stage 3 rose and management flagged higher near-term credit costs; the stock fell ~10% in two days to an 11-month low (Business Standard, 2026-10-26). A further 50bp of credit cost on a Rs 3.3 lakh cr book is Rs 1,650 cr, about 8% of annual PBT.
2. **Rates and funding (repo -2.5, G-sec -1.5, credit spreads -2.5).** RBI hiked repo to 5.50% on 2026-10-07 and shifted to "calibrated tightening". Shriram's assets are mostly fixed-rate, liabilities partly floating, so margins compress with a 2-4 quarter lag.
3. **Rural demand and the monsoon (+2.0 per +10% rainfall).** Management cut growth guidance on El Nino risk to rural repayment capacity.
4. **Vehicle and freight cycle (F_AUTO_DEMAND_IN +3.5, F_GDP_IN +3.0).**
5. **Diesel price (F_BRENT -1.0)** - empirically significant (t=-2.0) and mechanistically sound.
6. **FPI flows and global rates (F_FPI_FLOWS +2.5, F_US_10Y -1.2).**
7. **Event/ownership optionality:** MUFG control reports (2026-10-13) lifted the stock 6-7% before a company denial.

## Transmission examples
- **Middle East escalation -> Brent up -> diesel up -> trucker margin squeeze -> delinquencies.** 1st: Brent +10%; 2nd: diesel +6% raises operating cost ~3-4% of truck revenue; 3rd: freight rates lag, operators' EMI cover falls, stage-2 rises in Shriram's used-CV book; 4th: credit cost +15-25bp, EPS -3-4%, relative stock -1 to -2%. Also Brent up -> INR down -> RBI stays hawkish -> funding cost up (second route).
- **El Nino weak monsoon -> rural income down -> food inflation up -> RBI delays easing/hikes -> NBFC funding up.** Combines F_MONSOON (+) with F_FOOD_INFLATION_IN and F_REPO_IN: stock hit via both collections and margin.
- **US midterm / risk-on -> FPI inflows -> NBFC multiple re-rating:** US growth/yield move -> F_FPI_FLOWS -> large-cap financial valuations; stock rose 5.8% on 2026-11-05.
- **Bank deposit competition:** system deposit growth weak -> banks bid for CP/NCD money -> NCD spread up -> Shriram funding cost up.

## Current situation
Q2 FY27 PAT Rs 3,684 cr (+59% YoY; ET quotes Rs 3,677 cr) on financing profit Rs 5,103 cr. Interest expense fell to Rs 4,965 cr from Rs 5,525 cr a year ago. Offsetting this, gross/net Stage 3 rose and FY27 growth guidance was trimmed; Jefferies and Citi cut targets. At P/E 17.9 and a reported ~68% discount to Bajaj Finance (Financial Express 2026-11-01) the stock prices in some of this. The pack's 12m return is +20.9% but 3m is -15.6%.

## Upcoming events
Q3 FY27 results (Jan 2027), RBI MPC in early December (25% chance of another hike by my estimate), possible MUFG control step (15% in 12m), rural stress data through the winter.

## Bull and bear
**Bull:** MUFG control/capital, structurally lower funding cost, new-vehicle financing diversification, sub-18x P/E with ROE 16%. **Bear:** El Nino-driven stress in a book that is borrower-concentrated in small truckers, higher funding cost with fixed-rate assets, the guidance cut signalling slower growth, and NBFC regulatory tightening. Medium overall confidence: asset-quality detail comes from headlines, not primary filings (not retrievable in this run).


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.