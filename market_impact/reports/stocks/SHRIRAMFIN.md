# SHRIRAMFIN — Shriram Finance Ltd.
*NIFTY_50 · Financial Services · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -4.6%**, **12 months -6.4%** (rank 194 / 180 of 200 for 3m / 12m); beta 1.42
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +27.0%): 3 months 37%, 12 months 70%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -6.5% … P90 -4.0%; plausible 12m relative-return range incl. stock-specific noise: -20.0% … +62.8%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves -3.7 pp (model impact -9.2% beta-adjusted vs realised market-adjusted move -1.8%); forward event exposure -4.6% (3m -3.2%; half assumed priced); company-specific events +1.4%

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
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -8.6% | -8.6% | +0.0 | -3.8 | -4.3 | -0.4 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -6.0% | -6.0% | -5.5 | -0.2 | -0.1 | -0.3 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -4.5% | -4.5% | -3.5 | -0.7 | -0.2 | -0.2 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -4.2% | -4.2% | -2.5 | -0.5 | -0.8 | -0.4 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +6.9% | +3.5% | +6.2 | +0.2 | +0.1 | +0.4 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -3.2% | -3.2% | -2.8 | -0.1 | -0.2 | -0.0 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -2.9% | -2.9% | -1.0 | -1.1 | -0.5 | -0.3 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -2.6% | -2.6% | -1.4 | -0.9 | -0.2 | -0.1 |
| IMD April 2027 long-range forecast says normal or above-normal monsoon (>=96% LPA) (`EV_MONSOON27_FIRST_FORECAST_NORMAL`) | scheduled | 0.68 | +3.7% | +2.5% | +2.0 | +0.4 | +1.0 | +0.3 |
| Kharif 2026 output hit: paddy area down, foodgrain target cut, rice output seen sharpest fall in ~2 decades (`EV_KHARIF26_OUTPUT_HIT`) | occurred | 1.00 | -2.0% | -2.0% | +0.0 | +0.0 | -1.1 | -1.0 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.55 | +3.7% | +2.0% | +1.3 | +0.9 | +0.8 | +0.7 |
| North-east monsoon 2026 normal or above-normal (relief for southern reservoirs) (`EV_NEMONSOON26_NORMAL_UP`) | anticipated | 0.85 | +2.3% | +1.9% | +1.0 | +0.2 | +0.7 | +0.3 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → SHRIRAMFIN | +6.25% | +3.12% |
| 1 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → SHRIRAMFIN | +2.00% | +1.36% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → SHRIRAMFIN | -2.50% | -1.05% |
| 1 | EV_NEMONSOON26_NORMAL_UP ⇒ F_MONSOON → SHRIRAMFIN | +1.00% | +0.85% |
| 2 | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → F_GDP_IN → SHRIRAMFIN | +0.86% | +0.78% |
| 2 | EV_PULSES_VEG_SPIKE_WINTER ⇒ F_CPI_IN → F_REPO_IN → SHRIRAMFIN | -2.88% | -0.72% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → SHRIRAMFIN | +1.30% | +0.72% |
| 1 | EV_RBI_FEB27_HIKE25 ⇒ F_REPO_IN → SHRIRAMFIN | -2.50% | -0.68% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → SHRIRAMFIN | -3.75% | -0.67% |
| 1 | EV_MONSOON27_DEFICIT_FORECAST ⇒ F_MONSOON → SHRIRAMFIN | -2.00% | -0.64% |
| 1 | EV_ECL_ROLLOUT_APR27 ⇒ F_ASSET_QUALITY_IN → SHRIRAMFIN | -0.67% | -0.61% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → SHRIRAMFIN | -2.40% | -0.60% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_FPI_FLOWS → SHRIRAMFIN | -2.40% | -0.60% |
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → SHRIRAMFIN | -1.20% | -0.60% |
| 1 | EV_CPI_BREACH_6PCT ⇒ F_REPO_IN → SHRIRAMFIN | -1.00% | -0.60% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_FPI_FLOWS → SHRIRAMFIN | -1.60 | events | -4.00% |
| 1 | F_MONSOON → SHRIRAMFIN | -1.56 | events | -3.12% |
| 1 | F_REPO_IN → SHRIRAMFIN | +1.00 | events | -2.50% |
| 1 | F_GSEC_10Y_IN → SHRIRAMFIN | +1.55 | director_override | -2.33% |
| 1 | F_US_10Y → SHRIRAMFIN | +1.68 | observed | -2.01% |
| 1 | F_GDP_IN → SHRIRAMFIN | +0.50 | events | +1.50% |
| 1 | F_CREDIT_SPREADS_IN → SHRIRAMFIN | +0.50 | events | -1.25% |
| 2 | F_GDP_IN → F_ASSET_QUALITY_IN → SHRIRAMFIN | +0.50 | events | +0.36% |
| 1 | F_AUTO_DEMAND_IN → SHRIRAMFIN | -0.10 | events | -0.35% |
| 2 | F_REPO_IN → F_CREDIT_GROWTH_IN → SHRIRAMFIN | +1.00 | events | -0.29% |
| 2 | F_GDP_IN → F_CREDIT_GROWTH_IN → SHRIRAMFIN | +0.50 | events | +0.21% |
| 2 | F_RURAL_DEMAND → F_ASSET_QUALITY_IN → SHRIRAMFIN | -0.25 | events | -0.18% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2027-01 | Q3 FY27 results (AUM growth vs cut guidance, Stage 3 trend) | results | 0.95 | +0.0% | +0.00% |
| 2027-03 | MUFG announces step toward majority control / open offer (Bloomberg 2026-10-13 report; company denied 2026-10-14) | corporate_action | 0.15 | +9.5% | +1.43% |

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