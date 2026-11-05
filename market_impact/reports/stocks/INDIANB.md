# INDIANB — Indian Bank
*MIDCAP_100 · Financial Services · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -0.8%**, **12 months -2.4%** (rank 129 / 140 of 200 for 3m / 12m); beta 1.17
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +26.2%): 3 months 48%, 12 months 40%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -6.8% … P90 +2.0%; plausible 12m relative-return range incl. stock-specific noise: -50.1% … +16.1%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +0.0 pp (model impact +0.6% beta-adjusted vs realised market-adjusted move +4.7%); forward event exposure -3.3% (3m -0.8%; half assumed priced); company-specific events +0.7%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Credit cost / NPA cycle (higher = worse) (`F_ASSET_QUALITY_IN`) | +50 bp credit cost | -8.05 | -8.00 | +0.00 | -0.03 | -0.02 | — |
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | +5.25 | +0.00 | +3.36 | +2.59 | -0.70 | — |
| India real GDP growth (`F_GDP_IN`) | +1 pp | +4.27 | +3.00 | +1.97 | -0.56 | -0.14 | — |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -3.65 | -3.00 | -0.33 | -0.23 | -0.10 | +3.5% |
| Private corporate capex (`F_PRIVATE_CAPEX`) | +10% capex growth | +3.61 | +0.00 | +2.24 | +2.21 | -0.84 | — |
| Monsoon rainfall vs normal (`F_MONSOON`) | +10% above long-period average | +3.46 | +0.00 | +0.96 | +1.94 | +0.56 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -3.30 | +0.00 | -0.69 | -2.49 | -0.12 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -3.19 | +0.00 | -0.96 | -1.09 | -1.14 | — |
| RBI prudential tightening (risk weights, LCR, provisioning) (`P_RBI_PRUDENTIAL`) | +1 = tightening step | -2.93 | -1.50 | -1.71 | +0.23 | +0.06 | — |
| Central + state government capex (`F_GOVT_CAPEX`) | +10% capex growth | +2.84 | +1.50 | +0.54 | +0.83 | -0.04 | — |
| US average effective tariff rate (all partners) (`NEW_US_TARIFF_GLOBAL`) | +5 pp effective tariff rate | -2.80 | +0.00 | -1.20 | -0.96 | -0.64 | — |
| US equity market (`F_US_EQUITIES`) | +5% S&P 500 | +2.50 | +0.00 | +1.92 | +0.45 | +0.13 | +1.2% |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +2.29 | +0.00 | +0.00 | +0.87 | +1.41 | — |
| Brent crude oil price (`F_BRENT`) | +10% Brent | -2.27 | +0.00 | -0.79 | -0.80 | -0.67 | +0.0% |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -4.4% | -4.4% | +0.0 | -1.2 | -2.4 | -0.7 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -4.3% | -4.3% | +0.0 | -0.8 | -3.1 | -0.4 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -3.9% | -3.9% | -3.3 | -0.3 | -0.1 | -0.2 |
| India Q1 FY27 GDP grows 7.8% (31 Aug 2026), beating ~7.3% consensus (`EV_GDP_Q1FY27_7_8`) | occurred | 1.00 | +3.6% | +3.6% | +3.0 | +1.0 | -0.3 | -0.1 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -3.4% | -3.4% | -2.9 | -0.2 | -0.2 | -0.1 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +5.7% | +2.8% | +5.0 | +0.4 | +0.1 | +0.3 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.25 | -10.5% | -2.6% | -7.5 | -2.3 | -0.7 | -0.1 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.55 | +4.5% | +2.5% | +1.2 | +1.2 | +1.1 | +1.0 |
| IMD April 2027 long-range forecast says normal or above-normal monsoon (>=96% LPA) (`EV_MONSOON27_FIRST_FORECAST_NORMAL`) | scheduled | 0.68 | +3.6% | +2.5% | +0.0 | +1.0 | +2.1 | +0.6 |
| US Q3 data: GDP 3.4%, CPI 3.7%, September payrolls only +29k (`EV_US_Q3_DATA_MIXED`) | occurred | 1.00 | +2.4% | +2.4% | +0.0 | +1.2 | +1.2 | +0.1 |
| US recession (two negative quarters or NBER-style) beginning by mid-2027 (`EV_US_RECESSION_RISK_2027`) | risk_scenario | 0.25 | -8.9% | -2.2% | +0.0 | -8.7 | +0.2 | -0.4 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.25 | -8.9% | -2.2% | -3.0 | -2.1 | -2.0 | -1.8 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → INDIANB | -7.50% | -1.88% |
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → INDIANB | +3.75% | +1.88% |
| 1 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → INDIANB | -7.50% | -1.12% |
| 1 | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → INDIANB | +1.20% | +1.08% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_RISK_SENTIMENT → INDIANB | -4.32% | -1.08% |
| 1 | EV_ECL_ROLLOUT_APR27 ⇒ F_ASSET_QUALITY_IN → INDIANB | -1.20% | -1.08% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_RISK_SENTIMENT → INDIANB | -3.00% | -0.75% |
| 1 | EV_NVDA_NOV17_BEAT ⇒ F_RISK_SENTIMENT → INDIANB | +1.20% | +0.74% |
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → INDIANB | -1.44% | -0.72% |
| 1 | EV_BANKING_LIQUIDITY_DEFICIT_MAR27 ⇒ F_LIQUIDITY_IN → INDIANB | -1.20% | -0.72% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_RISK_SENTIMENT → INDIANB | +1.20% | +0.66% |
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_RISK_SENTIMENT → INDIANB | +1.20% | +0.60% |
| 2 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_GDP_IN → INDIANB | +0.80% | +0.54% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_GDP → F_RISK_SENTIMENT → INDIANB | -2.16% | -0.54% |
| 1 | EV_CPI_BREACH_6PCT ⇒ F_GSEC_10Y_IN → INDIANB | -0.90% | -0.54% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_GSEC_10Y_IN → INDIANB | +1.55 | director_override | -2.79% |
| 1 | F_FPI_FLOWS → INDIANB | -1.60 | events | -2.40% |
| 1 | F_GDP_IN → INDIANB | +0.50 | events | +1.50% |
| 1 | F_GOVT_CAPEX → INDIANB | +1.00 | events | +1.50% |
| 1 | F_LIQUIDITY_IN → INDIANB | -0.90 | events | -0.72% |
| 2 | F_GDP_IN → F_ASSET_QUALITY_IN → INDIANB | +0.50 | events | +0.64% |
| 1 | F_RISK_SENTIMENT → INDIANB | +0.11 | observed | -0.34% |
| 2 | F_RURAL_DEMAND → F_ASSET_QUALITY_IN → INDIANB | -0.25 | events | -0.32% |
| 2 | F_REPO_IN → F_ASSET_QUALITY_IN → INDIANB | +1.00 | events | -0.32% |
| 1 | F_REPO_IN → INDIANB | +1.00 | events | +0.30% |
| 3 | F_MONSOON → F_UNSECURED_STRESS → F_ASSET_QUALITY_IN → INDIANB | -1.56 | events | -0.30% |
| 1 | F_USDINR → INDIANB | -0.37 | observed | +0.30% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-12 | Interim dividend / further monetisation of NSE stake and NSE IPO progress (one-off gains) | corporate_action | 0.30 | +1.8% | +0.53% |
| 2027 | Formal PSU bank consolidation announcement involving Indian Bank (EAC-PM paper, rumours 2026-09; PIB fact-check on 'merger of 9 PSU banks') | corporate_action | 0.07 | +2.0% | +0.14% |
| 2027-01-15 | Q3 FY27 results (estimated from Q2 on 2026-10-15); NII, margin and one-off gains watched | results | 0.95 | +0.0% | +0.00% |

## Analyst profile (agent research, sourced)
# INDIANB - Indian Bank (as of 2026-11-05)

## Business
Indian Bank is a mid-sized public sector bank (government 73.84%) with a strong south-India retail, agri and MSME franchise, a large government-securities book and a corporate loan portfolio. Q2 FY27 profit was Rs3,462cr (+15%) on NII +18% (screener shows Rs3,541cr for the quarter), but a Rs1,388cr gain from the sale of NSE shares was disclosed on 2026-10-16 (ET; whether it sits wholly in Q2 is unverified), so core earnings growth is lower than the headline. Valuation is modest: P/E 9.1, P/B 1.38 with ROE 15.4% and a 2.1% dividend yield.

## What moves the stock (ranked)
1. **Credit cost (-8 per +50bp)**: the largest cyclical risk, though PSU provisioning cover is high and recoveries strong.
2. **GDP/credit growth and capex (+3.0, +2.0, +1.5)**: a state-owned lender to infra and government-linked borrowers.
3. **Risk sentiment and flows (-3.0, +1.5)**: PSU banks are high-beta (1.2).
4. **Bond yields (-1.8)**: the large G-sec book makes MTM a real sensitivity.
5. **Repo (+0.3) and deposits (+1.5)**: the October hike should help NIM before deposits reprice, unlike for private banks.
6. **Prudential regulation (-1.5)** and **unsecured stress (-1.0)** (low exposure).

## Transmission examples
- **Middle East escalation -> Brent ~$105 -> INR ~97 -> CPI +0.4pp -> RBI hikes**: 2nd order: G-sec 10Y +30bp -> Indian Bank MTM on AFS book (-1.0 to -1.8). 3rd: EBLR loans reprice up quickly; NIM +5bp for two quarters (+1). 4th: borrowers in MSME/retail face stress after 2-3 quarters, credit cost +10bp (-2); government capex held up (positive, +0.5). Net around -1 to -2.
- **Government capex surge -> infra borrowers -> corporate credit demand**: +10% capex -> infra/PSU lending demand +1pp -> NII +1% -> +1.5.
- **PSU consolidation policy**: EAC-PM paper and unconfirmed merger reports -> sector volatility; direction depends on whether Indian Bank is acquirer or target (+/-). Low probability (7%).
- **NSE IPO/stake monetisation** -> one-off gains -> higher book value and dividends, a non-recurring boost.

## Current situation
Stock +9.7% in a month, near its Rs1,001 52-week high (low Rs764). Opex jumped 24% YoY in Q2, financing profit fell to Rs661cr (screener's definition), so the headline profit is driven by other income including the NSE gain. FIIs rose to 6.9%. PSU peers: SBI posted record Rs21,121cr Q1 FY27 profit.

## Upcoming
Q3 FY27 results mid-January 2027 (estimated); RBI MPC December; PSU consolidation talk; dividend and capital plan.

## Bull case
Hike drives NIM +10bp, loan growth 12-14%, credit cost stays <0.5%, more NSE gains; re-rating to 1.6x book (+15-20%).
## Bear case
Bond yields rise further, deposit competition squeezes NIM, one-offs fade and credit cost rises; PSU de-rating (-15%).


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.