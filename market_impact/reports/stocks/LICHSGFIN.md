# LICHSGFIN — LIC Housing Finance Ltd.
*MIDCAP_100 · Financial Services · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +0.2%**, **12 months +0.3%** (rank 93 / 81 of 200 for 3m / 12m); beta 1.22
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +24.1%): 3 months 51%, 12 months 50%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -3.3% … P90 +3.2%; plausible 12m relative-return range incl. stock-specific noise: -32.2% … +30.7%
- Decomposition (12m): 0.5 × forward event exposure +0.3% (3m +0.6%; half assumed priced; market-priced macro drift removed) + 0.5 × company-specific catalysts +0.9%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply +3.8% (beta-adjusted) vs a realised market-adjusted move of -7.1% — gap +10.9 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Credit cost / NPA cycle (higher = worse) (`F_ASSET_QUALITY_IN`) | +50 bp credit cost | -7.37 | -7.00 | -0.36 | -0.02 | +0.01 | — |
| India real GDP growth (`F_GDP_IN`) | +1 pp | +3.94 | +0.00 | +4.08 | -0.02 | -0.12 | — |
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | +3.82 | +0.00 | +1.12 | +2.70 | -0.01 | — |
| RBI prudential tightening (risk weights, LCR, provisioning) (`P_RBI_PRUDENTIAL`) | +1 = tightening step | -3.68 | -2.00 | -1.87 | +0.05 | +0.14 | — |
| Indian corporate credit spreads (`F_CREDIT_SPREADS_IN`) | +50 bp spreads | -3.16 | -3.00 | -0.09 | +0.01 | -0.09 | — |
| Affordable-housing / home-loan support (`P_HOUSING_POLICY`) | +1 = stronger support | +2.91 | +2.50 | +0.32 | +0.03 | +0.06 | — |
| Private corporate capex (`F_PRIVATE_CAPEX`) | +10% capex growth | +2.49 | +0.00 | +0.24 | +2.38 | -0.13 | — |
| Residential real-estate sales (`F_HOUSING_DEMAND`) | +10% sales volume | +2.22 | +2.00 | +0.09 | +0.22 | -0.09 | — |
| India 10-year G-sec yield (`F_GSEC_10Y_IN`) | +25 bp yield | -1.91 | -1.50 | -0.38 | -0.02 | -0.01 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | +1.85 | +3.00 | -1.08 | -0.05 | -0.02 | — |
| Monsoon rainfall vs normal (`F_MONSOON`) | +10% above long-period average | +1.78 | +0.00 | +0.00 | +1.46 | +0.32 | — |
| Central + state government capex (`F_GOVT_CAPEX`) | +10% capex growth | +1.77 | +0.00 | +0.00 | +1.40 | +0.36 | — |
| Unsecured retail & microfinance stress (higher = worse) (`F_UNSECURED_STRESS`) | +1 pp delinquencies | -1.68 | +0.00 | -1.36 | -0.12 | -0.20 | — |
| Indian wage / employee-cost inflation (`F_WAGES_IN`) | +2 pp | +1.59 | +0.00 | +0.00 | +0.66 | +0.93 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -3.3% | -3.3% | -3.0 | -0.2 | -0.0 | -0.0 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -2.3% | -2.3% | -2.2 | -0.1 | +0.0 | +0.0 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -2.2% | -2.2% | +0.0 | +0.0 | -1.8 | -0.4 |
| India Q1 FY27 GDP grows 7.8% (31 Aug 2026), beating ~7.3% consensus (`EV_GDP_Q1FY27_7_8`) | occurred | 1.00 | +2.0% | +2.0% | +0.0 | +2.0 | +0.0 | -0.1 |
| RBI expected-credit-loss (ECL) provisioning goes live as scheduled (FY28 start) (`EV_ECL_ROLLOUT_APR27`) | scheduled | 0.90 | -2.0% | -1.8% | -1.9 | -0.1 | +0.0 | -0.0 |
| IMD April 2027 long-range forecast says normal or above-normal monsoon (>=96% LPA) (`EV_MONSOON27_FIRST_FORECAST_NORMAL`) | scheduled | 0.68 | +2.1% | +1.4% | +0.0 | +0.0 | +1.3 | +0.8 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +2.5% | +1.3% | +2.5 | +0.2 | -0.1 | -0.1 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | +1.2% | +1.2% | +1.9 | -0.7 | +0.1 | -0.1 |
| Budget FY2027-28: FY27 deficit overshoot confirmed and consolidation path slowed (`EV_BUDGET_FY28_FISCAL_SLIPPAGE`) | scheduled | 0.50 | -2.3% | -1.2% | -2.1 | -0.2 | -0.0 | -0.0 |
| Rural demand indicators mixed: tractor volumes dip in Oct, 2W festive sales firm, rural CPI above urban, rural jobs scheme person-days down (`EV_RURAL_DEMAND_SOFT26`) | occurred | 1.00 | -1.1% | -1.1% | +0.0 | -0.3 | -0.8 | +0.0 |
| US recession (two negative quarters or NBER-style) beginning by mid-2027 (`EV_US_RECESSION_RISK_2027`) | risk_scenario | 0.25 | -4.4% | -1.1% | -3.0 | -1.5 | -0.1 | +0.2 |
| US Q3 data: GDP 3.4%, CPI 3.7%, September payrolls only +29k (`EV_US_Q3_DATA_MIXED`) | occurred | 1.00 | +1.0% | +1.0% | +0.5 | +0.1 | +0.4 | -0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → LICHSGFIN | +3.00% | +1.26% |
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → LICHSGFIN | +2.50% | +1.25% |
| 1 | EV_ECL_ROLLOUT_APR27 ⇒ F_ASSET_QUALITY_IN → LICHSGFIN | -1.05% | -0.95% |
| 1 | EV_RBI_FEB27_HIKE25 ⇒ F_REPO_IN → LICHSGFIN | +3.00% | +0.81% |
| 1 | EV_US_RECESSION_RISK_2027 ⇒ F_FED_FUNDS → LICHSGFIN | -3.00% | -0.75% |
| 1 | EV_FED_DEC26_HIKE25 ⇒ F_FED_FUNDS → LICHSGFIN | +1.00% | +0.72% |
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → LICHSGFIN | -1.20% | -0.60% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_REPO_IN → LICHSGFIN | +3.00% | +0.54% |
| 1 | EV_ECL_ROLLOUT_APR27 ⇒ P_RBI_PRUDENTIAL → LICHSGFIN | -0.60% | -0.54% |
| 1 | EV_BANKING_LIQUIDITY_DEFICIT_MAR27 ⇒ F_CREDIT_SPREADS_IN → LICHSGFIN | -0.90% | -0.54% |
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_CREDIT_SPREADS_IN → LICHSGFIN | -0.90% | -0.45% |
| 2 | EV_INDIA_STAGFLATION_SCARE ⇒ F_GDP_IN → F_ASSET_QUALITY_IN → LICHSGFIN | -3.36% | -0.40% |
| 1 | EV_FED_H1_2027_FURTHER_HIKES ⇒ F_FED_FUNDS → LICHSGFIN | +1.00% | +0.40% |
| 3 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_GDP_IN → F_ASSET_QUALITY_IN → LICHSGFIN | +0.56% | +0.38% |
| 1 | EV_INDIA_STAGFLATION_SCARE ⇒ F_REPO_IN → LICHSGFIN | +3.00% | +0.36% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_REPO_IN → LICHSGFIN | +1.00 | events | +3.00% |
| 1 | F_GSEC_10Y_IN → LICHSGFIN | +1.55 | director_override | -2.33% |
| 1 | F_FED_FUNDS → LICHSGFIN | +1.62 | observed | +1.62% |
| 1 | F_FPI_FLOWS → LICHSGFIN | -1.60 | events | -1.60% |
| 1 | F_CREDIT_SPREADS_IN → LICHSGFIN | +0.50 | events | -1.50% |
| 2 | F_GDP_IN → F_ASSET_QUALITY_IN → LICHSGFIN | +0.50 | events | +1.12% |
| 2 | F_RURAL_DEMAND → F_ASSET_QUALITY_IN → LICHSGFIN | -0.25 | events | -0.28% |
| 2 | F_REPO_IN → F_ASSET_QUALITY_IN → LICHSGFIN | +1.00 | events | -0.28% |
| 3 | F_MONSOON → F_UNSECURED_STRESS → F_ASSET_QUALITY_IN → LICHSGFIN | -1.56 | events | -0.26% |
| 2 | F_GDP_IN → F_CREDIT_GROWTH_IN → LICHSGFIN | +0.50 | events | +0.26% |
| 2 | F_GDP_IN → F_HOUSING_DEMAND → LICHSGFIN | +0.50 | events | +0.24% |
| 2 | F_REPO_IN → F_HOUSING_DEMAND → LICHSGFIN | +1.00 | events | -0.21% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2027-01 | Q3 FY27 results (Q2 was 30 Oct 2026; Q3 likely late Jan/early Feb) | results | 0.95 | +0.0% | +0.00% |
| 2027-03 | Resolution of Essel/Subhash Chandra-guarantee exposures (full repayment offers noted 8 Oct) | litigation | 0.50 | +1.8% | +0.88% |

## Analyst profile (agent research, sourced)
# LICHSGFIN - LIC Housing Finance (midcap housing finance)

## Business
LIC Housing Finance is the second-largest private-sector-style HFC by book in India (portfolio roughly Rs 3 lakh cr), majority promoted by LIC (45.24%). It lends mainly to salaried individuals for home purchase and construction (97% retail in H1 FY27), plus LAP and developer/project finance (a legacy stress area). Funding is dominated by NCDs and bank loans (model knowledge), with NHB refinance and deposits. TTM revenue Rs 28.6k cr, net profit Rs 5.9k cr; Q2 FY27 net profit about Rs 1,507 cr (+11%).

## What moves the stock (ranked)
1. **Policy rate / spread dynamics** - the stock is a rate-cycle name. With floating assets repricing before liabilities, Morgan Stanley estimated a 7.2% PBT boost from the 7 Oct hike to 5.50%. Offsetting: deposit/NCD repricing, competition from banks at 7.1-7.35% and slower demand.
2. **Credit spreads / funding cost** - 85% of borrowing is market-linked; each +50bp spread costs about 3% of equity value after pass-through.
3. **Asset quality** - Stage 3 fell to 2.05% with Rs 553 cr recoveries in Q2, but provisioning coverage dropped; legacy exposures (Subhash Chandra-guarantee loans, where four firms offered full repayment on 8 Oct) are binary catalysts.
4. **Housing demand and policy** - disbursements +11%, management targets 14-15%.
5. **Parent/flows** - LIC owns 45%; FIIs trimmed from 21.5% to 18.9%.

## Transmission examples
- **Middle East escalation -> Brent up -> CPI up -> RBI hawkish (hiked 7 Oct) -> HFC asset yields reset up (PLR) quickly -> NIM temporarily up (+); but 3rd-order: higher EMIs -> housing demand softens -> disbursement growth slows -> 4th-order: LIC HFL's loan book growth < 8%, offsetting NIM gains.**
- **US 10y 4.89% -> FPI selling of Indian financials (FII share falling) -> LICHSGFIN (beta 1.4) underperforms -> NCD yields rise via G-sec -> funding cost up for fixed-term borrowings reset in 12-18m.**
- **Weak real-estate cycle -> developer stress -> LRD/project loan NPAs -> higher provisions; improvement in the Essel exposure resolution gives upside.**

## Current situation
Valuation is deeply discounted (P/B 0.65x, P/E 4.9x), reflecting low growth (portfolio CAGR below 8% over 5 years) and market-share loss to banks and Bajaj Housing/HDFC. Q2 was mixed: profit up 11%, but spreads narrowed in H1 and coverage fell (Multibagg AI). Brokerages are Hold (target Rs 520 vs 530 spot).

## Upcoming
Q3 FY27 late January/February 2027; RBI MPC December; guarantee loan resolution; LIC parent news.

## Bull / bear
Bull: hike-driven NIM expansion, disbursement 14-15% growth, NPA recoveries, re-rating toward 1x book. Bear: spread compression, demand slowdown, legacy defaults, refinancing at wider spreads.

Note: BusinessLine's headline reports Q2 PAT as Rs 150.7 cr; screener shows Rs 1,507 cr, which fits the quarterly trend, so the headline is treated as a unit typo.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.