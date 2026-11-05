# ABCAPITAL — Aditya Birla Capital Ltd.
*MIDCAP_100 · Financial Services · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -0.2%**, **12 months -1.4%** (rank 129 / 173 of 200 for 3m / 12m); beta 1.31
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +19.6%): 3 months 49%, 12 months 45%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -5.1% … P90 +1.2%; plausible 12m relative-return range incl. stock-specific noise: -26.0% … +22.2%
- Decomposition (12m): 0.5 × forward event exposure -2.3% (3m -0.2%; half assumed priced; market-priced macro drift removed) + 0.5 × company-specific catalysts -0.1%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply -2.5% (beta-adjusted) vs a realised market-adjusted move of +7.7% — gap -10.2 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## Where the expected return comes from
Market-priced macro drivers (rates, FX, commodities, indices, volatility, flows, growth, inflation) are taken as priced, so what is left is policy, regulatory, sector, theme, geopolitical and company-specific exposure — where 2nd–4th-order effects are most likely to be missed. Percentage points of the expected relative return.
| source | 12m: 1st order | 12m: 2nd–4th order | 12m total | 3m total |
|---|---|---|---|---|
| Policy | +0.00 | +0.18 | +0.18 | +0.01 |
| Regulatory | -1.04 | -0.11 | -1.15 | -0.22 |
| Sector | -0.66 | +1.16 | +0.49 | +0.44 |
| Theme | +0.00 | +0.09 | +0.09 | +0.06 |
| Geopolitics | +0.00 | -0.03 | -0.03 | -0.03 |
| Company catalysts | -0.07 | +0.01 | -0.06 | +0.01 |
| Market-priced macro | +0.00 | +0.00 | +0.00 | +0.00 |
| Beta adjustment | — | — | -0.75 | -0.34 |
| Universe centring | — | — | -0.15 | -0.10 |
| **Expected relative return** | | | **-1.38** | **-0.17** |

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Credit cost / NPA cycle (higher = worse) (`F_ASSET_QUALITY_IN`) | +50 bp credit cost | -6.31 | -6.00 | -0.29 | -0.03 | +0.01 | — |
| RBI prudential tightening (risk weights, LCR, provisioning) (`P_RBI_PRUDENTIAL`) | +1 = tightening step | -4.48 | -3.00 | -1.70 | +0.13 | +0.10 | — |
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | +3.12 | +0.00 | +1.28 | +2.03 | -0.19 | — |
| Insurance regulation tightening (IRDAI) (`P_IRDAI_REG`) | +1 = tightening | -3.10 | -3.00 | +0.00 | -0.11 | +0.01 | — |
| Unsecured retail & microfinance stress (higher = worse) (`F_UNSECURED_STRESS`) | +1 pp delinquencies | -2.74 | -2.00 | -0.68 | -0.02 | -0.04 | — |
| India real GDP growth (`F_GDP_IN`) | +1 pp | +2.59 | +0.00 | +3.15 | -0.30 | -0.25 | — |
| Indian corporate credit spreads (`F_CREDIT_SPREADS_IN`) | +50 bp spreads | -2.57 | -2.40 | -0.15 | +0.04 | -0.06 | — |
| Domestic SIP / DII flows (`F_DOMESTIC_FLOWS`) | +10% monthly SIP + DII inflow | +2.49 | +2.50 | +0.00 | +0.00 | -0.01 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -2.48 | -1.50 | -0.95 | +0.03 | -0.07 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -2.35 | +0.00 | -1.30 | -0.99 | -0.07 | — |
| Monsoon rainfall vs normal (`F_MONSOON`) | +10% above long-period average | +2.17 | +0.00 | +0.32 | +1.16 | +0.69 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +2.06 | +2.00 | +0.03 | +0.04 | -0.01 | — |
| Private corporate capex (`F_PRIVATE_CAPEX`) | +10% capex growth | +1.89 | +0.00 | +0.40 | +1.78 | -0.29 | — |
| Household savings shift to financial assets (`T_FINANCIALISATION`) | +1 | +1.77 | +0.00 | +2.00 | -0.24 | +0.02 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -4.5% | -4.5% | -4.4 | -0.1 | -0.1 | +0.0 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -3.0% | -3.0% | +0.0 | -1.5 | -1.2 | -0.2 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -2.9% | -2.9% | -2.2 | -0.7 | +0.1 | -0.1 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -2.7% | -2.7% | +0.0 | -0.4 | -1.5 | -0.9 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +5.2% | +2.6% | +5.0 | +0.1 | +0.1 | -0.0 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -2.1% | -2.1% | -1.8 | -0.2 | -0.0 | -0.0 |
| RBI expected-credit-loss (ECL) provisioning goes live as scheduled (FY28 start) (`EV_ECL_ROLLOUT_APR27`) | scheduled | 0.90 | -2.2% | -2.0% | -2.2 | -0.0 | +0.0 | +0.0 |
| IMD April 2027 long-range forecast says normal or above-normal monsoon (>=96% LPA) (`EV_MONSOON27_FIRST_FORECAST_NORMAL`) | scheduled | 0.68 | +2.1% | +1.5% | +0.0 | +0.3 | +1.3 | +0.5 |
| India Q1 FY27 GDP grows 7.8% (31 Aug 2026), beating ~7.3% consensus (`EV_GDP_Q1FY27_7_8`) | occurred | 1.00 | +1.3% | +1.3% | +0.0 | +1.6 | -0.1 | -0.1 |
| Risk: USD/INR >98 and/or reserves < US$650bn (disorderly rupee, emergency RBI response) (`EV_RUPEE_BREAK_98_RESERVE_STRESS`) | risk_scenario | 0.18 | -6.9% | -1.2% | -5.3 | -2.0 | +0.3 | +0.1 |
| RBI MPC Dec 2026 (~4 Dec): hikes repo another 25 bp to 5.75% (`EV_RBI_DEC26_HIKE25`) | scheduled | 0.42 | -2.9% | -1.2% | -2.2 | -0.7 | +0.1 | -0.1 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -1.2% | -1.2% | +0.0 | -0.9 | -0.3 | +0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → ABCAPITAL | +5.00% | +2.50% |
| 1 | EV_IRDAI_COMMISSION_RESET ⇒ P_IRDAI_REG → ABCAPITAL | -2.10% | -1.05% |
| 1 | EV_ECL_ROLLOUT_APR27 ⇒ P_RBI_PRUDENTIAL → ABCAPITAL | -0.90% | -0.81% |
| 1 | EV_ECL_ROLLOUT_APR27 ⇒ F_ASSET_QUALITY_IN → ABCAPITAL | -0.90% | -0.81% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → ABCAPITAL | -1.50% | -0.63% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → ABCAPITAL | -3.00% | -0.54% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → ABCAPITAL | -1.92% | -0.48% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_FPI_FLOWS → ABCAPITAL | -1.92% | -0.48% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → ABCAPITAL | -1.87% | -0.47% |
| 1 | EV_BANKING_LIQUIDITY_DEFICIT_MAR27 ⇒ F_CREDIT_SPREADS_IN → ABCAPITAL | -0.72% | -0.43% |
| 1 | EV_RBI_FEB27_HIKE25 ⇒ F_REPO_IN → ABCAPITAL | -1.50% | -0.41% |
| 1 | EV_RBI_GOLD_LOAN_TIGHTEN ⇒ P_RBI_PRUDENTIAL → ABCAPITAL | -1.20% | -0.36% |
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_CREDIT_SPREADS_IN → ABCAPITAL | -0.72% | -0.36% |
| 1 | EV_BUDGET_FY28_LTCG_RELIEF ⇒ F_FPI_FLOWS → ABCAPITAL | +1.00% | +0.35% |
| 2 | EV_INDIA_STAGFLATION_SCARE ⇒ F_GDP_IN → F_ASSET_QUALITY_IN → ABCAPITAL | -2.88% | -0.35% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_FPI_FLOWS → ABCAPITAL | -1.60 | events | -3.20% |
| 1 | F_REPO_IN → ABCAPITAL | +1.00 | events | -1.50% |
| 1 | F_GSEC_10Y_IN → ABCAPITAL | +1.55 | director_override | -1.24% |
| 1 | F_CREDIT_SPREADS_IN → ABCAPITAL | +0.50 | events | -1.20% |
| 2 | F_GDP_IN → F_ASSET_QUALITY_IN → ABCAPITAL | +0.50 | events | +0.96% |
| 2 | F_MONSOON → F_UNSECURED_STRESS → ABCAPITAL | -1.56 | events | -0.50% |
| 2 | F_GDP_IN → F_CREDIT_GROWTH_IN → ABCAPITAL | +0.50 | events | +0.43% |
| 2 | F_REPO_IN → F_CREDIT_GROWTH_IN → ABCAPITAL | +1.00 | events | -0.29% |
| 2 | F_CPI_IN → F_UNSECURED_STRESS → ABCAPITAL | +1.15 | events | -0.28% |
| 2 | F_RURAL_DEMAND → F_ASSET_QUALITY_IN → ABCAPITAL | -0.25 | events | -0.24% |
| 2 | F_REPO_IN → F_ASSET_QUALITY_IN → ABCAPITAL | +1.00 | events | -0.24% |
| 2 | F_GDP_IN → P_RBI_PRUDENTIAL → ABCAPITAL | +0.50 | events | -0.24% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2027-01 | Q3 FY27 results (inferred; Q2 on 2026-10-30): lending margin, credit cost and insurance new-business margin | results | 0.92 | +0.0% | +0.00% |
| 2027-03 | Gold-loan business ramp-up and any RBI gold-loan rule changes | regulatory | 0.30 | -0.5% | -0.15% |

## Analyst profile (agent research, sourced)
# ABCAPITAL - Aditya Birla Capital Ltd. (Nifty 200, I_NBFC_VEHICLE_CONSUMER) - as of 2026-11-05

## Business
Aditya Birla Capital is the financial-services holding company of the Aditya Birla Group (promoters 68.8%). Lending through an NBFC and a housing-finance company is the largest business (about 58% of group value, model estimate); the rest is a life-insurance joint venture with Sun Life, asset management (ABSLAMC), health insurance and wealth/broking. Q2 FY27 consolidated profit rose 38% to Rs1,288cr as lending grew and costs were controlled. On 2026-08-19 it entered gold loans. At Rs399 it trades at 29.8x earnings and 3.1x book with ROE of 11.6%, which prices in continued strong growth.

## What moves the stock, ranked
1. **Credit cost (F_ASSET_QUALITY_IN -6.0) and unsecured stress (-2.0).** The lending book of ~Rs1.65 lakh cr (model estimate) is the main earnings engine and carries consumer and small-business credit risk.
2. **Funding cost: spreads (-4.0), repo (-1.5), G-sec (-0.8, mixed).** Borrowings ~Rs1.3 lakh cr; the 2026-10-07 hike and wider AAA spreads compress margins before assets reprice. Rising G-sec yields help the life insurer slightly.
3. **Regulation: RBI prudential (-3.0) and IRDAI (-3.0).** Revolving-credit curbs and gold-loan norms affect lending; surrender/commission rules affect insurance.
4. **Growth drivers: credit growth (+2.5), domestic financial flows (+2.5), housing (+1.5).**
5. **Flows (+2.0)** and a weak **Grasim group link (+0.05)**.

## Transmission examples
- **Oil -> rates -> NBFC margin:** Brent at 95 (107 in late Sept) -> CPI up -> RBI hikes again -> bank lending rates and AAA spreads up -> ABCAPITAL's floating liabilities reprice faster than fixed-rate retail assets -> lending NIM compresses -> group EPS growth slows and the 29.8x multiple de-rates.
- **Equity-market chain:** risk-off, VIX up -> SIP flows slow and equity markets fall -> AMC AUM and ULIP premiums fall -> fee income drops -> insurance and AMC contribution weakens (about 30% of value).
- **Regulatory chain:** RBI restricts revolving/unsecured credit -> lending growth slows in consumer segments -> operating leverage fades; but new gold-loan business may offset if gold prices recover.
- **Insurance chain:** IRDAI tightens surrender/commission norms -> distribution incentives change -> new-business margins fall -> value of in-force book re-rated lower.

## Current situation and bull/bear
Q2 profit +38%; stock up 20% in 12 months; Jefferies bullish. Bull: lending growth with improving credit cost, insurance margin gains, cost programmes. Bear: rate-driven margin squeeze, credit-cost normalisation, regulatory tightening, high multiple. Confidence is low: the segment weights and funding split are model estimates and should be refreshed from the Q2 investor presentation.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.