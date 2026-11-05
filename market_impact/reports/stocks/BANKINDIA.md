# BANKINDIA — Bank of India
*MIDCAP_100 · Financial Services · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -0.0%**, **12 months -3.0%** (rank 99 / 142 of 200 for 3m / 12m); beta 1.14
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +20.7%): 3 months 50%, 12 months 48%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -12.7% … P90 +4.9%; plausible 12m relative-return range incl. stock-specific noise: -30.8% … +30.1%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +0.0 pp (model impact -0.3% beta-adjusted vs realised market-adjusted move -4.5%); forward event exposure -0.7% (3m +0.5%; half assumed priced); company-specific events -3.0%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Credit cost / NPA cycle (higher = worse) (`F_ASSET_QUALITY_IN`) | +50 bp credit cost | -10.06 | -10.00 | +0.00 | -0.04 | -0.02 | — |
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | +7.10 | +0.00 | +3.76 | +4.13 | -0.79 | — |
| RBI prudential tightening (risk weights, LCR, provisioning) (`P_RBI_PRUDENTIAL`) | +1 = tightening step | -5.98 | -4.00 | -2.24 | +0.18 | +0.08 | — |
| India real GDP growth (`F_GDP_IN`) | +1 pp | +5.32 | +3.00 | +3.17 | -0.65 | -0.20 | — |
| Private corporate capex (`F_PRIVATE_CAPEX`) | +10% capex growth | +5.01 | +0.00 | +2.40 | +3.62 | -1.01 | — |
| Monsoon rainfall vs normal (`F_MONSOON`) | +10% above long-period average | +3.96 | +0.00 | +1.04 | +2.70 | +0.22 | — |
| Central + state government capex (`F_GOVT_CAPEX`) | +10% capex growth | +3.32 | +1.50 | +0.54 | +1.25 | +0.03 | — |
| India 10-year G-sec yield (`F_GSEC_10Y_IN`) | +25 bp yield | -3.23 | -3.00 | +0.00 | -0.13 | -0.11 | — |
| Indian wage / employee-cost inflation (`F_WAGES_IN`) | +2 pp | +3.21 | +0.00 | +0.24 | +1.84 | +1.13 | — |
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +3.09 | +0.00 | +1.20 | +2.39 | -0.50 | — |
| General-government fiscal slippage / extra borrowing vs budget (Centre + states) (`NEW_FISCAL_SLIPPAGE_IN`) | +0.5 pp of GDP deficit above budget (~Rs2 lakh cr) | -2.91 | +0.00 | -1.68 | -0.40 | -0.83 | — |
| Unsecured retail & microfinance stress (higher = worse) (`F_UNSECURED_STRESS`) | +1 pp delinquencies | -2.81 | -1.50 | -1.04 | -0.13 | -0.15 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -2.64 | +0.00 | -1.44 | -0.59 | -0.61 | — |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +2.30 | +0.00 | +0.00 | +0.13 | +2.17 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -8.5% | -8.5% | -4.0 | -1.6 | -1.2 | -1.8 |
| RBI expected-credit-loss (ECL) provisioning goes live as scheduled (FY28 start) (`EV_ECL_ROLLOUT_APR27`) | scheduled | 0.62 | -10.3% | -6.4% | -10.5 | +0.2 | +0.0 | -0.0 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -5.0% | -5.0% | -5.0 | -0.1 | +0.2 | -0.1 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -5.0% | -5.0% | +0.0 | -1.3 | -3.4 | -0.3 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -4.9% | -4.9% | -4.2 | -0.3 | -0.2 | -0.2 |
| India Q1 FY27 GDP grows 7.8% (31 Aug 2026), beating ~7.3% consensus (`EV_GDP_Q1FY27_7_8`) | occurred | 1.00 | +4.2% | +4.2% | +3.0 | +1.6 | -0.3 | -0.1 |
| Retail petrol/diesel price freeze with crude >$100 squeezes OMC marketing margins; Q2 FY27 results split refiners (`EV_OMC_FUEL_FREEZE_LOSSES`) | occurred | 1.00 | -3.2% | -3.2% | +0.0 | -1.1 | -1.1 | -1.0 |
| IMD April 2027 long-range forecast says normal or above-normal monsoon (>=96% LPA) (`EV_MONSOON27_FIRST_FORECAST_NORMAL`) | scheduled | 0.68 | +4.6% | +3.1% | +0.0 | +1.0 | +2.5 | +1.0 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +5.6% | +2.8% | +5.6 | +0.1 | -0.2 | +0.1 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.28 | -9.4% | -2.6% | -6.0 | -3.2 | -0.3 | +0.1 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -2.5% | -2.5% | +0.0 | -2.5 | +0.2 | -0.1 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -2.4% | -2.4% | +0.0 | +2.5 | -4.4 | -0.5 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_ECL_ROLLOUT_APR27 ⇒ F_ASSET_QUALITY_IN → BANKINDIA | -5.00% | -3.10% |
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → BANKINDIA | +5.00% | +2.50% |
| 1 | EV_ECL_ROLLOUT_APR27 ⇒ P_RBI_PRUDENTIAL → BANKINDIA | -4.00% | -2.48% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → BANKINDIA | -6.00% | -1.68% |
| 1 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → BANKINDIA | -7.50% | -1.35% |
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → BANKINDIA | -2.40% | -1.20% |
| 1 | EV_RBI_GOLD_LOAN_TIGHTEN ⇒ P_RBI_PRUDENTIAL → BANKINDIA | -4.00% | -1.20% |
| 1 | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → BANKINDIA | +1.20% | +1.08% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → BANKINDIA | +2.50% | +1.00% |
| 1 | EV_ECL_ROLLOUT_APR27 ⇒ F_CREDIT_GROWTH_IN → BANKINDIA | -1.50% | -0.93% |
| 1 | EV_ECL_DEFERRED ⇒ P_RBI_PRUDENTIAL → BANKINDIA | +2.40% | +0.91% |
| 1 | EV_CPI_BREACH_6PCT ⇒ F_GSEC_10Y_IN → BANKINDIA | -1.50% | -0.90% |
| 2 | EV_PULSES_VEG_SPIKE_WINTER ⇒ F_CPI_IN → F_REPO_IN → BANKINDIA | +2.88% | +0.72% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → BANKINDIA | -2.00% | -0.71% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → BANKINDIA | +1.20% | +0.70% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_GSEC_10Y_IN → BANKINDIA | +1.70 | events | -5.10% |
| 1 | F_FPI_FLOWS → BANKINDIA | -1.60 | events | -3.20% |
| 1 | F_REPO_IN → BANKINDIA | +1.00 | events | +2.50% |
| 1 | F_GDP_IN → BANKINDIA | +0.50 | events | +1.50% |
| 1 | F_GOVT_CAPEX → BANKINDIA | +1.00 | events | +1.50% |
| 2 | F_GDP_IN → F_ASSET_QUALITY_IN → BANKINDIA | +0.50 | events | +0.80% |
| 2 | F_RURAL_DEMAND → F_ASSET_QUALITY_IN → BANKINDIA | -0.25 | events | -0.40% |
| 2 | F_REPO_IN → F_ASSET_QUALITY_IN → BANKINDIA | +1.00 | events | -0.40% |
| 2 | F_MONSOON → F_UNSECURED_STRESS → BANKINDIA | -1.56 | events | -0.37% |
| 3 | F_MONSOON → F_UNSECURED_STRESS → F_ASSET_QUALITY_IN → BANKINDIA | -1.56 | events | -0.37% |
| 2 | F_REPO_IN → F_CREDIT_GROWTH_IN → BANKINDIA | +1.00 | events | -0.35% |
| 1 | F_USDINR → BANKINDIA | -0.37 | observed | -0.30% |

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