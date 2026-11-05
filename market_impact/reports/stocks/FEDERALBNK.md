# FEDERALBNK — Federal Bank Ltd.
*MIDCAP_100 · Financial Services · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +0.4%**, **12 months -0.3%** (rank 61 / 115 of 200 for 3m / 12m); beta 0.98
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +19.9%): 3 months 52%, 12 months 52%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -5.4% … P90 +4.6%; plausible 12m relative-return range incl. stock-specific noise: -25.2% … +28.3%
- Decomposition (12m): 0.5 × forward event exposure -0.3% (3m +0.8%; half assumed priced; market-priced macro drift removed) + 0.5 × company-specific catalysts +0.2%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply -4.1% (beta-adjusted) vs a realised market-adjusted move of +12.6% — gap -16.6 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Credit cost / NPA cycle (higher = worse) (`F_ASSET_QUALITY_IN`) | +50 bp credit cost | -9.04 | -9.00 | +0.00 | -0.04 | +0.00 | — |
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | +4.74 | +0.00 | +1.68 | +3.18 | -0.12 | — |
| India real GDP growth (`F_GDP_IN`) | +1 pp | +4.72 | +0.00 | +5.03 | -0.20 | -0.11 | — |
| RBI prudential tightening (risk weights, LCR, provisioning) (`P_RBI_PRUDENTIAL`) | +1 = tightening step | -4.29 | -2.50 | -2.07 | +0.17 | +0.11 | — |
| Private corporate capex (`F_PRIVATE_CAPEX`) | +10% capex growth | +3.17 | +0.00 | +0.48 | +2.95 | -0.26 | — |
| Gulf economy / remittances (`F_GULF_REMITTANCES`) | +10% | +2.99 | +3.00 | -0.02 | +0.02 | -0.01 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -2.80 | -1.75 | -0.54 | -0.23 | -0.28 | — |
| Bank deposit growth / funding ease (`F_DEPOSIT_GROWTH_IN`) | +3 pp | +2.71 | +2.50 | +0.48 | -0.11 | -0.15 | — |
| Monsoon rainfall vs normal (`F_MONSOON`) | +10% above long-period average | +2.71 | +0.00 | +0.24 | +1.76 | +0.71 | — |
| Unsecured retail & microfinance stress (higher = worse) (`F_UNSECURED_STRESS`) | +1 pp delinquencies | -2.59 | -1.50 | -0.96 | -0.04 | -0.09 | — |
| Central + state government capex (`F_GOVT_CAPEX`) | +10% capex growth | +2.15 | +0.00 | +0.00 | +1.77 | +0.38 | — |
| Bank credit growth (`F_CREDIT_GROWTH_IN`) | +3 pp | +2.08 | +3.00 | -0.45 | -0.59 | +0.12 | — |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -2.02 | -1.50 | -0.33 | -0.19 | -0.00 | +3.5% |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +2.00 | +2.00 | -0.00 | -0.01 | +0.00 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -4.4% | -4.4% | -4.4 | +0.0 | +0.0 | -0.0 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -3.4% | -3.4% | +0.0 | -0.3 | -2.2 | -0.9 |
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -3.1% | -3.1% | -1.8 | -0.8 | -0.5 | -0.1 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -3.0% | -3.0% | -2.5 | -0.4 | -0.0 | -0.1 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +5.6% | +2.8% | +5.6 | -0.0 | -0.0 | +0.0 |
| India Q1 FY27 GDP grows 7.8% (31 Aug 2026), beating ~7.3% consensus (`EV_GDP_Q1FY27_7_8`) | occurred | 1.00 | +2.4% | +2.4% | +0.0 | +2.5 | -0.0 | -0.1 |
| RBI expected-credit-loss (ECL) provisioning goes live as scheduled (FY28 start) (`EV_ECL_ROLLOUT_APR27`) | scheduled | 0.90 | -2.5% | -2.2% | -2.5 | +0.1 | +0.0 | -0.0 |
| IMD April 2027 long-range forecast says normal or above-normal monsoon (>=96% LPA) (`EV_MONSOON27_FIRST_FORECAST_NORMAL`) | scheduled | 0.68 | +2.8% | +1.9% | +0.0 | +0.2 | +1.8 | +0.8 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -1.8% | -1.8% | +0.0 | -0.2 | -1.2 | -0.4 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.25 | -6.8% | -1.7% | -3.8 | -2.7 | -0.2 | -0.1 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.55 | +3.0% | +1.6% | +1.7 | +0.5 | +0.7 | +0.1 |
| Rural demand indicators mixed: tractor volumes dip in Oct, 2W festive sales firm, rural CPI above urban, rural jobs scheme person-days down (`EV_RURAL_DEMAND_SOFT26`) | occurred | 1.00 | -1.4% | -1.4% | +0.0 | -0.5 | -1.0 | +0.1 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → FEDERALBNK | +5.00% | +2.50% |
| 1 | EV_ECL_ROLLOUT_APR27 ⇒ F_ASSET_QUALITY_IN → FEDERALBNK | -1.35% | -1.21% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ C_MIDEAST_CONFLICT → FEDERALBNK | +1.75% | +0.96% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → FEDERALBNK | -3.75% | -0.94% |
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → FEDERALBNK | -1.44% | -0.72% |
| 1 | EV_ECL_ROLLOUT_APR27 ⇒ P_RBI_PRUDENTIAL → FEDERALBNK | -0.75% | -0.68% |
| 1 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → FEDERALBNK | -3.75% | -0.56% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → FEDERALBNK | -3.00% | -0.54% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ C_MIDEAST_CONFLICT → FEDERALBNK | -2.10% | -0.53% |
| 2 | EV_INDIA_STAGFLATION_SCARE ⇒ F_GDP_IN → F_ASSET_QUALITY_IN → FEDERALBNK | -4.32% | -0.52% |
| 3 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_GDP_IN → F_ASSET_QUALITY_IN → FEDERALBNK | +0.72% | +0.49% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → FEDERALBNK | -1.92% | -0.48% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_FPI_FLOWS → FEDERALBNK | -1.92% | -0.48% |
| 2 | EV_Q2_FY27_GDP_STRONG ⇒ F_GDP_IN → F_ASSET_QUALITY_IN → FEDERALBNK | +0.58% | +0.46% |
| 1 | EV_BANKING_LIQUIDITY_DEFICIT_MAR27 ⇒ F_DEPOSIT_GROWTH_IN → FEDERALBNK | +0.75% | +0.45% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_FPI_FLOWS → FEDERALBNK | -1.60 | events | -3.20% |
| 1 | F_GSEC_10Y_IN → FEDERALBNK | +1.55 | director_override | -2.79% |
| 1 | C_MIDEAST_CONFLICT → FEDERALBNK | +1.00 | events | -1.75% |
| 2 | F_GDP_IN → F_ASSET_QUALITY_IN → FEDERALBNK | +0.50 | events | +1.44% |
| 2 | F_GDP_IN → F_CREDIT_GROWTH_IN → FEDERALBNK | +0.50 | events | +0.51% |
| 1 | F_REPO_IN → FEDERALBNK | +1.00 | events | +0.50% |
| 2 | F_MONSOON → F_UNSECURED_STRESS → FEDERALBNK | -1.56 | events | -0.37% |
| 2 | F_RURAL_DEMAND → F_ASSET_QUALITY_IN → FEDERALBNK | -0.25 | events | -0.36% |
| 2 | F_REPO_IN → F_ASSET_QUALITY_IN → FEDERALBNK | +1.00 | events | -0.36% |
| 2 | F_REPO_IN → F_CREDIT_GROWTH_IN → FEDERALBNK | +1.00 | events | -0.35% |
| 2 | F_GDP_IN → F_DEPOSIT_GROWTH_IN → FEDERALBNK | +0.50 | events | +0.30% |
| 1 | F_USDINR → FEDERALBNK | -0.37 | observed | -0.30% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-12 | Renewed Jana SFB acquisition announcement or definitive withdrawal | corporate_action | 0.10 | -2.0% | -0.20% |
| 2027-01-16 | Q3 FY27 results (inferred; Q2 reported 2026-10-16) | results | 0.90 | +0.5% | +0.45% |

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