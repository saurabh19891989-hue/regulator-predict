# BANKINDIA — Bank of India
*MIDCAP_100 · Financial Services · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +0.8%**, **12 months +0.1%** (rank 22 / 86 of 200 for 3m / 12m); beta 1.14
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +20.7%): 3 months 53%, 12 months 49%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -4.3% … P90 +4.7%; plausible 12m relative-return range incl. stock-specific noise: -26.7% … +26.4%
- Decomposition (12m): 0.5 × forward event exposure +0.2% (3m +0.8%; half assumed priced; market-priced macro drift removed) + 0.5 × company-specific catalysts +0.4%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply -0.8% (beta-adjusted) vs a realised market-adjusted move of -4.5% — gap +3.7 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## Where the expected return comes from
Market-priced macro drivers (rates, FX, commodities, indices, volatility, flows, growth, inflation) are taken as priced, so what is left is policy, regulatory, sector, theme, geopolitical and company-specific exposure — where 2nd–4th-order effects are most likely to be missed. Percentage points of the expected relative return.
| source | 12m: 1st order | 12m: 2nd–4th order | 12m total | 3m total |
|---|---|---|---|---|
| Policy | +0.16 | +0.09 | +0.24 | -0.12 |
| Regulatory | -0.68 | -0.07 | -0.76 | -0.07 |
| Sector | -0.81 | +2.02 | +1.21 | +0.87 |
| Theme | +0.00 | +0.10 | +0.10 | +0.06 |
| Geopolitics | +0.00 | -0.04 | -0.04 | -0.04 |
| Company catalysts | +0.19 | +0.00 | +0.19 | +0.45 |
| Market-priced macro | +0.00 | -0.00 | -0.00 | +0.00 |
| Beta adjustment | — | — | -0.65 | -0.29 |
| Universe centring | — | — | -0.15 | -0.10 |
| **Expected relative return** | | | **+0.15** | **+0.76** |

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Credit cost / NPA cycle (higher = worse) (`F_ASSET_QUALITY_IN`) | +50 bp credit cost | -10.06 | -10.00 | +0.00 | -0.04 | -0.02 | — |
| RBI prudential tightening (risk weights, LCR, provisioning) (`P_RBI_PRUDENTIAL`) | +1 = tightening step | -5.98 | -4.00 | -2.24 | +0.18 | +0.08 | — |
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | +5.38 | +0.00 | +3.76 | +1.79 | -0.17 | — |
| India real GDP growth (`F_GDP_IN`) | +1 pp | +5.23 | +3.00 | +2.69 | -0.27 | -0.19 | — |
| Private corporate capex (`F_PRIVATE_CAPEX`) | +10% capex growth | +3.64 | +0.00 | +2.40 | +1.52 | -0.27 | — |
| Central + state government capex (`F_GOVT_CAPEX`) | +10% capex growth | +3.24 | +1.50 | +0.54 | +1.09 | +0.12 | — |
| India 10-year G-sec yield (`F_GSEC_10Y_IN`) | +25 bp yield | -3.10 | -3.00 | +0.00 | -0.06 | -0.04 | — |
| Monsoon rainfall vs normal (`F_MONSOON`) | +10% above long-period average | +2.95 | +0.00 | +1.04 | +1.63 | +0.28 | — |
| Unsecured retail & microfinance stress (higher = worse) (`F_UNSECURED_STRESS`) | +1 pp delinquencies | -2.78 | -1.50 | -1.04 | -0.13 | -0.11 | — |
| General-government fiscal slippage / extra borrowing vs budget (Centre + states) (`NEW_FISCAL_SLIPPAGE_IN`) | +0.5 pp of GDP deficit above budget (~Rs2 lakh cr) | -2.27 | +0.00 | -1.68 | -0.24 | -0.35 | — |
| Indian wage / employee-cost inflation (`F_WAGES_IN`) | +2 pp | +2.22 | +0.00 | +0.24 | +1.47 | +0.52 | — |
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +2.11 | +0.00 | +1.20 | +1.02 | -0.10 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -2.08 | +0.00 | -1.44 | -0.34 | -0.30 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +1.99 | +2.00 | +0.05 | -0.06 | +0.00 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -4.7% | -4.7% | -4.2 | -0.3 | -0.1 | -0.0 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -4.4% | -4.4% | -4.4 | -0.1 | +0.1 | -0.0 |
| India Q1 FY27 GDP grows 7.8% (31 Aug 2026), beating ~7.3% consensus (`EV_GDP_Q1FY27_7_8`) | occurred | 1.00 | +4.1% | +4.1% | +3.0 | +1.3 | -0.1 | -0.1 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -3.7% | -3.7% | +0.0 | -1.3 | -2.1 | -0.4 |
| RBI expected-credit-loss (ECL) provisioning goes live as scheduled (FY28 start) (`EV_ECL_ROLLOUT_APR27`) | scheduled | 0.90 | -3.1% | -2.8% | -3.1 | +0.1 | +0.0 | -0.0 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +5.5% | +2.8% | +5.6 | +0.1 | -0.2 | +0.0 |
| IMD April 2027 long-range forecast says normal or above-normal monsoon (>=96% LPA) (`EV_MONSOON27_FIRST_FORECAST_NORMAL`) | scheduled | 0.68 | +3.1% | +2.1% | +0.0 | +1.0 | +1.6 | +0.5 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.25 | -6.6% | -1.6% | -3.8 | -2.7 | -0.2 | +0.1 |
| Rural demand indicators mixed: tractor volumes dip in Oct, 2W festive sales firm, rural CPI above urban, rural jobs scheme person-days down (`EV_RURAL_DEMAND_SOFT26`) | occurred | 1.00 | -1.6% | -1.6% | +0.0 | -1.1 | -0.5 | +0.1 |
| Budget FY2027-28: FY27 deficit overshoot confirmed and consolidation path slowed (`EV_BUDGET_FY28_FISCAL_SLIPPAGE`) | scheduled | 0.50 | -3.0% | -1.5% | -2.7 | -0.2 | -0.1 | -0.0 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.55 | +2.6% | +1.5% | +1.6 | +0.4 | +0.4 | +0.2 |
| North-east monsoon 2026 normal or above-normal (relief for southern reservoirs) (`EV_NEMONSOON26_NORMAL_UP`) | anticipated | 0.85 | +1.6% | +1.4% | +0.0 | +0.5 | +0.8 | +0.3 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → BANKINDIA | +5.00% | +2.50% |
| 1 | EV_ECL_ROLLOUT_APR27 ⇒ F_ASSET_QUALITY_IN → BANKINDIA | -1.50% | -1.35% |
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → BANKINDIA | -2.40% | -1.20% |
| 1 | EV_ECL_ROLLOUT_APR27 ⇒ P_RBI_PRUDENTIAL → BANKINDIA | -1.20% | -1.08% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → BANKINDIA | +2.50% | +1.05% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → BANKINDIA | -3.75% | -0.94% |
| 1 | EV_RBI_FEB27_HIKE25 ⇒ F_REPO_IN → BANKINDIA | +2.50% | +0.68% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → BANKINDIA | +1.04% | +0.57% |
| 1 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → BANKINDIA | -3.75% | -0.56% |
| 2 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_GDP_IN → BANKINDIA | +0.80% | +0.54% |
| 1 | EV_FERT_SUBSIDY_TOPUP_WINTER ⇒ F_GSEC_10Y_IN → BANKINDIA | -0.60% | -0.54% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → BANKINDIA | -3.00% | -0.54% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_GSEC_10Y_IN → BANKINDIA | -3.00% | -0.54% |
| 1 | EV_INDIA_STAGFLATION_SCARE ⇒ F_GDP_IN → BANKINDIA | -4.50% | -0.54% |
| 1 | EV_CPI_BREACH_6PCT ⇒ F_GSEC_10Y_IN → BANKINDIA | -0.90% | -0.54% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_GSEC_10Y_IN → BANKINDIA | +1.55 | director_override | -4.65% |
| 1 | F_FPI_FLOWS → BANKINDIA | -1.60 | events | -3.20% |
| 1 | F_REPO_IN → BANKINDIA | +1.00 | events | +2.50% |
| 1 | F_GDP_IN → BANKINDIA | +0.50 | events | +1.50% |
| 2 | F_GDP_IN → F_ASSET_QUALITY_IN → BANKINDIA | +0.50 | events | +0.80% |
| 2 | F_RURAL_DEMAND → F_ASSET_QUALITY_IN → BANKINDIA | -0.25 | events | -0.40% |
| 2 | F_REPO_IN → F_ASSET_QUALITY_IN → BANKINDIA | +1.00 | events | -0.40% |
| 2 | F_MONSOON → F_UNSECURED_STRESS → BANKINDIA | -1.56 | events | -0.37% |
| 2 | F_REPO_IN → F_CREDIT_GROWTH_IN → BANKINDIA | +1.00 | events | -0.35% |
| 1 | F_GOVT_CAPEX → BANKINDIA | +0.20 | director_override | +0.30% |
| 1 | F_USDINR → BANKINDIA | -0.37 | observed | -0.30% |
| 2 | F_GDP_IN → F_CREDIT_GROWTH_IN → BANKINDIA | +0.50 | events | +0.26% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2027-01-22 | Q3 FY27 results (inferred; Q2 reported 2026-10-23) | results | 0.90 | +1.0% | +0.90% |
| 2027-03 | Possible government OFS/QIP for capital or liquidity (model knowledge: government holding 73.4%, MPS-compliant) | corporate_action | 0.15 | -3.5% | -0.53% |

## Analyst profile (agent research, sourced)
# BANKINDIA - Bank of India (midcap, PSU bank) - as of 2026-11-05

## Business
A Government-owned (73.38%) bank with domestic retail/MSME/agri/corporate lending and an international book. Market cap Rs62,599cr at P/E 5x and P/B 0.66x, with ROE 12.4% and a 3.4% dividend yield. Q2 FY27 PAT Rs3,202cr (+25%).

## What moves the stock, ranked
1. **Rates / NIM** - RBI hiked repo to 5.50% on 2026-10-07; PSU banks raised repo-linked lending rates by 25bp on 2026-10-09. Management guides NIM to 2.55% in H2 FY27. +10bp NIM on ~Rs10 lakh cr earning assets = Rs1,000cr pre-tax = ~6% of PAT; persistence 0.25 gives +1.5; with P/B re-rating potential w = +2.5 per +25bp repo. The gain is transient if deposit rates reprice.
2. **Credit cost / asset quality** - +50bp credit cost is ~-10% (Rs3,500cr pre-tax on Rs12,517cr TTM PAT, persistence 0.5). Low current GNPA means the shock is a stress scenario.
3. **G-sec yields (treasury MTM and discount rate)** - 10y +25bp ~ -3.
4. **ECL transition and RBI prudential rules** - Canara's Rs15,000cr warning (2026-10-15) shows day-1 hits; -4 per prudential step, wide range.
5. **Growth: GDP, credit and government capex** - PSU banks are the most cyclical lenders.
6. **Flows, sentiment, FX** - small FII float (7.6%); domestic-flow driven.

Empirical pack: gas -1.02 (t -2.1) is the only |t|>=2 and has no plausible bank channel; US10Y -1.23 (t -1.7) and Brent -0.65 agree in sign with our macro-yield channel.

## Transmission examples
- **Middle East escalation -> Brent +10% -> CPI +0.3pp -> RBI hikes again -> BoI loans reprice within weeks (EBLR) -> NIM +5bp -> but 10y yield up Rs625cr AFS loss per 25bp -> net positive on income, negative on capital; 4th-order: slower exporters/MSME borrowers raise slippages in 2027.**
- **USD/INR up -> overseas income translation up (BoI has a global book) but FPI selling -> mixed.**
- **ECL rule effective April 2027 -> Canara-style provisioning shock -> investors cut P/B on PSU banks -> BoI falls with the sector although fundamentals are stable -> capital raising via OFS risk.**

## Current situation
PAT growth strong from low base; shares Rs138 (+4.3% 1m). Governance link: government shareholding; SBI data breach headline (2026-11-04) affects sector sentiment.

## Upcoming
December MPC, Q3 results (Jan 2027), ECL regime (April 2027).

## Bull / bear
Bull: NIM expansion, PAT upgrades, P/B 0.66 re-rates. Bear: deposit repricing erases NIM gain, credit cycle turns, ECL hit, OFS.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.