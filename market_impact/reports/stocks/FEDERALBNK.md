# FEDERALBNK — Federal Bank Ltd.
*MIDCAP_100 · Financial Services · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -3.4%**, **12 months -7.1%** (rank 179 / 186 of 200 for 3m / 12m); beta 0.98
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +19.9%): 3 months 37%, 12 months 10%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -14.7% … P90 -2.7%; plausible 12m relative-return range incl. stock-specific noise: -45.7% … -3.7%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves -4.9 pp (model impact -9.7% beta-adjusted vs realised market-adjusted move +12.6%); forward event exposure -1.2% (3m +0.2%; half assumed priced); company-specific events -1.0%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Credit cost / NPA cycle (higher = worse) (`F_ASSET_QUALITY_IN`) | +50 bp credit cost | -9.04 | -9.00 | +0.00 | -0.04 | +0.00 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -5.01 | -3.50 | -0.54 | -0.43 | -0.55 | — |
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | +4.62 | +0.00 | +1.68 | +3.77 | -0.83 | — |
| RBI prudential tightening (risk weights, LCR, provisioning) (`P_RBI_PRUDENTIAL`) | +1 = tightening step | -4.29 | -2.50 | -2.07 | +0.17 | +0.11 | — |
| India real GDP growth (`F_GDP_IN`) | +1 pp | +4.04 | +0.00 | +5.78 | -1.34 | -0.40 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +4.04 | +4.00 | -0.00 | -0.01 | +0.05 | — |
| Gulf economy / remittances (`F_GULF_REMITTANCES`) | +10% | +3.01 | +3.00 | -0.02 | +0.03 | -0.00 | — |
| Monsoon rainfall vs normal (`F_MONSOON`) | +10% above long-period average | +2.83 | +0.00 | +0.24 | +2.09 | +0.50 | — |
| US equity market (`F_US_EQUITIES`) | +5% S&P 500 | +2.80 | +0.00 | +2.00 | +0.66 | +0.13 | +1.2% |
| Private corporate capex (`F_PRIVATE_CAPEX`) | +10% capex growth | +2.78 | +0.00 | +0.48 | +3.33 | -1.03 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -2.75 | +0.00 | +0.12 | -2.87 | -0.01 | — |
| Bank deposit growth / funding ease (`F_DEPOSIT_GROWTH_IN`) | +3 pp | +2.71 | +2.50 | +0.48 | -0.11 | -0.15 | — |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -2.63 | -1.50 | -0.70 | -0.39 | -0.03 | +3.5% |
| Unsecured retail & microfinance stress (higher = worse) (`F_UNSECURED_STRESS`) | +1 pp delinquencies | -2.62 | -1.50 | -0.96 | -0.04 | -0.12 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -8.9% | -8.9% | -8.8 | +0.0 | +0.0 | -0.1 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +10.7% | +5.3% | +10.6 | -0.0 | -0.0 | +0.1 |
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -5.1% | -5.1% | -3.5 | -0.8 | -0.6 | -0.2 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -3.6% | -3.6% | +0.0 | +0.1 | -3.4 | -0.3 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -3.6% | -3.6% | +0.0 | -0.3 | -2.6 | -0.6 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -3.1% | -3.1% | -2.5 | -0.4 | -0.1 | -0.2 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.55 | +5.5% | +3.0% | +3.5 | +0.7 | +1.0 | +0.4 |
| US Q3 data: GDP 3.4%, CPI 3.7%, September payrolls only +29k (`EV_US_Q3_DATA_MIXED`) | occurred | 1.00 | +2.5% | +2.5% | +0.0 | +0.6 | +1.5 | +0.4 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.25 | -9.8% | -2.4% | -3.8 | -5.6 | -0.4 | -0.0 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -2.4% | -2.4% | +0.0 | -1.6 | -0.5 | -0.2 |
| RBI expected-credit-loss (ECL) provisioning goes live as scheduled (FY28 start) (`EV_ECL_ROLLOUT_APR27`) | scheduled | 0.90 | -2.5% | -2.2% | -2.5 | +0.1 | +0.0 | -0.0 |
| US recession (two negative quarters or NBER-style) beginning by mid-2027 (`EV_US_RECESSION_RISK_2027`) | risk_scenario | 0.25 | -8.9% | -2.2% | +0.0 | -7.6 | -0.8 | -0.5 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → FEDERALBNK | +10.00% | +5.00% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ C_MIDEAST_CONFLICT → FEDERALBNK | +3.50% | +1.93% |
| 1 | EV_ECL_ROLLOUT_APR27 ⇒ F_ASSET_QUALITY_IN → FEDERALBNK | -1.35% | -1.21% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → FEDERALBNK | -6.00% | -1.08% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ C_MIDEAST_CONFLICT → FEDERALBNK | -4.20% | -1.05% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → FEDERALBNK | -3.84% | -0.96% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_FPI_FLOWS → FEDERALBNK | -3.84% | -0.96% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → FEDERALBNK | -3.75% | -0.94% |
| 1 | EV_RBI_GOLD_LOAN_TIGHTEN ⇒ P_RBI_PRUDENTIAL → FEDERALBNK | -2.50% | -0.75% |
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → FEDERALBNK | -1.44% | -0.72% |
| 1 | EV_BUDGET_FY28_LTCG_RELIEF ⇒ F_FPI_FLOWS → FEDERALBNK | +2.00% | +0.70% |
| 3 | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → F_GDP_IN → F_ASSET_QUALITY_IN → FEDERALBNK | +0.78% | +0.70% |
| 1 | EV_ECL_ROLLOUT_APR27 ⇒ P_RBI_PRUDENTIAL → FEDERALBNK | -0.75% | -0.68% |
| 1 | EV_Q2_FY27_GDP_STRONG ⇒ F_FPI_FLOWS → FEDERALBNK | +0.80% | +0.64% |
| 1 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → FEDERALBNK | -3.75% | -0.56% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_FPI_FLOWS → FEDERALBNK | -1.60 | events | -6.40% |
| 1 | C_MIDEAST_CONFLICT → FEDERALBNK | +1.00 | events | -3.50% |
| 1 | F_GSEC_10Y_IN → FEDERALBNK | +1.55 | director_override | -2.79% |
| 2 | F_GDP_IN → F_ASSET_QUALITY_IN → FEDERALBNK | +0.50 | events | +1.44% |
| 2 | F_GDP_IN → F_CREDIT_GROWTH_IN → FEDERALBNK | +0.50 | events | +0.51% |
| 1 | F_REPO_IN → FEDERALBNK | +1.00 | events | +0.50% |
| 2 | F_MONSOON → F_UNSECURED_STRESS → FEDERALBNK | -1.56 | events | -0.37% |
| 2 | F_RURAL_DEMAND → F_ASSET_QUALITY_IN → FEDERALBNK | -0.25 | events | -0.36% |
| 2 | F_REPO_IN → F_ASSET_QUALITY_IN → FEDERALBNK | +1.00 | events | -0.36% |
| 2 | F_REPO_IN → F_CREDIT_GROWTH_IN → FEDERALBNK | +1.00 | events | -0.35% |
| 3 | F_MONSOON → F_UNSECURED_STRESS → F_ASSET_QUALITY_IN → FEDERALBNK | -1.56 | events | -0.34% |
| 2 | F_GDP_IN → F_DEPOSIT_GROWTH_IN → FEDERALBNK | +0.50 | events | +0.30% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-12 | Renewed Jana SFB acquisition announcement or definitive withdrawal | corporate_action | 0.10 | -2.0% | -0.20% |
| 2027-01-16 | Q3 FY27 results (inferred; Q2 reported 2026-10-16) | results | 0.90 | +0.5% | +0.45% |
| 2027-04-01 | RBI ECL framework effective (model knowledge) | regulatory | 0.85 | -1.5% | -1.27% |

## Analyst profile (agent research, sourced)
# FEDERALBNK - Federal Bank Ltd. (midcap, private bank) - as of 2026-11-05

## Business
Kerala-headquartered private bank with a differentiated NRI and remittance franchise, strong gold-loan, MSME, agri and retail books. Market cap Rs83,353cr; Q2 FY27 standalone PAT Rs1,386cr (record, +45% y/y), NII +26%, NPAs at a decadal low. FIIs 28.5%, DIIs 49.3%.

## What moves the stock, ranked
1. **Asset quality** - +50bp credit cost is ~-9 (Rs975cr post-tax on Rs5,388cr TTM PAT, persistence 0.5); currently benign, so the stock prices continued improvement.
2. **FPI flows** - FII share rising 26% -> 28.5%; +4 per US$5bn/qtr.
3. **NRI/Gulf channel** - Gulf remittances +10% ~ +3; Middle East conflict escalation ~ -3.5 (Kerala is the most Gulf-exposed state). Empirical Brent +0.69 and USDINR +1.68 (t 1.4-1.5) are in the same oil-rich-Gulf/remittance direction.
4. **Credit and deposit growth** - +3pp each ~ +3 and +2.5.
5. **Rates** - repo hike benefits floating loans (+0.5) while 10y G-sec +25bp ~ -1.8 via AFS and P/E.
6. **M&A (Jana SFB)** - reported share-swap deal ~Rs6,500cr; market punished Federal on the news (-3/-4%) and rewarded the denial (+4-5%): acquisition is perceived negative.
7. **Regulation**.

## Transmission examples
- **Middle East escalation -> Gulf employment/remittances fall and oil rises -> NRI deposit inflows slow -> CASA ratio falls, NIM -2bp -> and Kerala consumption slows -> gold-loan collateral value and MSME stress -> credit cost +10bp -> EPS -4% -> -5% price (4th order via Kerala state economy).**
- **Repo +25bp -> loans reprice immediately, deposits slowly -> NIM +3-5bp -> PAT +3.5% -> stock +1% after P/E offset.**
- **Gold price falls -> LTV pressure on gold loans (Reuters flags early stress) -> margin calls/auctions -> credit cost up in the gold book.**

## Current situation
Record Q2; shares Rs337 near upper range after +42% in 12 months, -4.6% in 3 months. Jana SFB deal reports created volatility.

## Upcoming
Q3 results mid-January, December MPC, possible Jana-related news, ECL in April 2027.

## Bull / bear
Bull: NIM expansion, benign credit cost, NRI franchise, FPI inflows. Bear: Gulf shock, credit normalisation, expensive after +42%, acquisition surprise.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.