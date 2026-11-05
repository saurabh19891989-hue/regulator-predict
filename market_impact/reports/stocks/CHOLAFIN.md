# CHOLAFIN — Cholamandalam Investment and Finance Company Ltd.
*NIFTY_NEXT_50 · Financial Services · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -1.3%**, **12 months -2.0%** (rank 181 / 162 of 200 for 3m / 12m); beta 1.37
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +22.3%): 3 months 45%, 12 months 32%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -4.9% … P90 +0.3%; plausible 12m relative-return range incl. stock-specific noise: -27.5% … +25.2%
- Decomposition (12m): 0.5 × forward event exposure -2.0% (3m -1.1%; half assumed priced) + 0.5 × company-specific catalysts -1.0%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply -1.1% (beta-adjusted) vs a realised market-adjusted move of +12.3% — gap -13.3 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Credit cost / NPA cycle (higher = worse) (`F_ASSET_QUALITY_IN`) | +50 bp credit cost | -8.23 | -8.00 | -0.24 | +0.00 | +0.01 | — |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +3.56 | +1.00 | +1.58 | +0.53 | +0.45 | — |
| Indian vehicle demand (`F_AUTO_DEMAND_IN`) | +10% volumes | +3.50 | +3.50 | +0.00 | +0.00 | +0.00 | — |
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | +3.12 | +1.50 | +1.27 | +0.80 | -0.45 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -2.37 | +0.00 | -1.39 | -0.97 | -0.01 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -2.24 | -1.30 | -0.89 | -0.01 | -0.03 | — |
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +2.24 | +0.00 | +1.68 | +0.83 | -0.27 | — |
| RBI prudential tightening (risk weights, LCR, provisioning) (`P_RBI_PRUDENTIAL`) | +1 = tightening step | -2.22 | -1.00 | -1.52 | +0.21 | +0.08 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +2.15 | +2.00 | +0.04 | +0.03 | +0.07 | — |
| Monsoon rainfall vs normal (`F_MONSOON`) | +10% above long-period average | +2.12 | +1.00 | +0.23 | +0.68 | +0.22 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -2.06 | +0.00 | -0.85 | -0.85 | -0.37 | -1.1% |
| Indian corporate credit spreads (`F_CREDIT_SPREADS_IN`) | +50 bp spreads | -1.99 | -2.00 | +0.00 | +0.05 | -0.04 | — |
| Central + state government capex (`F_GOVT_CAPEX`) | +10% capex growth | +1.71 | +1.50 | +0.00 | +0.37 | -0.16 | — |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -1.57 | +0.00 | -0.12 | -0.86 | -0.59 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -4.7% | -4.7% | -4.4 | -0.1 | -0.1 | -0.2 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -3.0% | -3.0% | +0.0 | -1.7 | -1.2 | -0.1 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +5.4% | +2.7% | +5.0 | +0.1 | +0.1 | +0.2 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -2.7% | -2.7% | -1.3 | -0.3 | -0.9 | -0.3 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -2.6% | -2.6% | -2.0 | -0.6 | +0.1 | -0.1 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -2.4% | -2.4% | -2.4 | -0.0 | +0.0 | -0.0 |
| India Q1 FY27 GDP grows 7.8% (31 Aug 2026), beating ~7.3% consensus (`EV_GDP_Q1FY27_7_8`) | occurred | 1.00 | +2.4% | +2.4% | +1.5 | +1.4 | -0.4 | -0.1 |
| IMD April 2027 long-range forecast says normal or above-normal monsoon (>=96% LPA) (`EV_MONSOON27_FIRST_FORECAST_NORMAL`) | scheduled | 0.68 | +2.2% | +1.5% | +1.0 | +0.2 | +0.8 | +0.1 |
| Risk: USD/INR >98 and/or reserves < US$650bn (disorderly rupee, emergency RBI response) (`EV_RUPEE_BREAK_98_RESERVE_STRESS`) | risk_scenario | 0.18 | -7.4% | -1.3% | -6.5 | -1.2 | +0.3 | -0.0 |
| RBI expected-credit-loss (ECL) provisioning goes live as scheduled (FY28 start) (`EV_ECL_ROLLOUT_APR27`) | scheduled | 0.90 | -1.5% | -1.3% | -1.5 | +0.0 | -0.0 | +0.0 |
| Banking system liquidity turns to sustained deficit by end-March 2027 (`EV_BANKING_LIQUIDITY_DEFICIT_MAR27`) | anticipated | 0.60 | -2.1% | -1.3% | -2.1 | -0.0 | -0.0 | -0.0 |
| Risk: stagflation scare - CPI >=6.5% while GDP growth slips below ~6% (Q3 FY27 data, late Feb 2027) (`EV_INDIA_STAGFLATION_SCARE`) | risk_scenario | 0.12 | -10.0% | -1.2% | -2.5 | -7.1 | -0.5 | +0.1 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → CHOLAFIN | +5.00% | +2.50% |
| 1 | EV_ECL_ROLLOUT_APR27 ⇒ F_ASSET_QUALITY_IN → CHOLAFIN | -1.20% | -1.08% |
| 1 | EV_BANKING_LIQUIDITY_DEFICIT_MAR27 ⇒ F_LIQUIDITY_IN → CHOLAFIN | -1.20% | -0.72% |
| 1 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → CHOLAFIN | +1.00% | +0.68% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → CHOLAFIN | -1.30% | -0.55% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → CHOLAFIN | -3.00% | -0.54% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → CHOLAFIN | -1.92% | -0.48% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_FPI_FLOWS → CHOLAFIN | -1.92% | -0.48% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → CHOLAFIN | -1.87% | -0.47% |
| 2 | EV_INDIA_STAGFLATION_SCARE ⇒ F_GDP_IN → F_ASSET_QUALITY_IN → CHOLAFIN | -3.84% | -0.46% |
| 1 | EV_NEMONSOON26_NORMAL_UP ⇒ F_MONSOON → CHOLAFIN | +0.50% | +0.42% |
| 2 | EV_RARE_EARTH_CONTROLS_REIMPOSED ⇒ NEW_RARE_EARTH_SUPPLY → F_AUTO_DEMAND_IN → CHOLAFIN | -1.68% | -0.42% |
| 2 | EV_Q2_FY27_GDP_STRONG ⇒ F_GDP_IN → F_ASSET_QUALITY_IN → CHOLAFIN | +0.51% | +0.41% |
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → CHOLAFIN | -0.80% | -0.40% |
| 1 | EV_BANKING_LIQUIDITY_DEFICIT_MAR27 ⇒ F_CREDIT_SPREADS_IN → CHOLAFIN | -0.60% | -0.36% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_FPI_FLOWS → CHOLAFIN | -1.60 | events | -3.20% |
| 1 | F_AUTO_DEMAND_IN → CHOLAFIN | +0.50 | director_override | +1.75% |
| 1 | F_MONSOON → CHOLAFIN | -1.56 | events | -1.56% |
| 1 | F_GSEC_10Y_IN → CHOLAFIN | +1.55 | director_override | -1.55% |
| 1 | F_REPO_IN → CHOLAFIN | +1.00 | events | -1.30% |
| 2 | F_GDP_IN → F_ASSET_QUALITY_IN → CHOLAFIN | +0.50 | events | +1.28% |
| 1 | F_CREDIT_SPREADS_IN → CHOLAFIN | +0.50 | events | -1.00% |
| 1 | F_LIQUIDITY_IN → CHOLAFIN | -0.90 | events | -0.72% |
| 1 | F_STEEL_GLOBAL → CHOLAFIN | +2.06 | observed | +0.62% |
| 1 | F_RURAL_DEMAND → CHOLAFIN | -0.25 | events | -0.38% |
| 2 | F_REPO_IN → F_ASSET_QUALITY_IN → CHOLAFIN | +1.00 | events | -0.32% |
| 1 | F_GOVT_CAPEX → CHOLAFIN | +0.20 | director_override | +0.30% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-12 | Rs5,000cr QIP launch/pricing (board approved 2026-10-28; shareholder approval route and timing unverified); ~3.3% of market cap | corporate_action | 0.70 | -1.5% | -1.05% |
| 2027-01 | Q3 FY27 results (Q2 declared 2026-10-28) | results | 0.95 | +0.0% | +0.00% |

## Analyst profile (agent research, sourced)
# Cholamandalam Investment and Finance (CHOLAFIN) - Market Impact profile, as of 2026-11-05

## Business
Chola is the flagship NBFC of the Murugappa group and India's largest vehicle financier by profit. Roughly two-thirds of AUM is vehicle finance (commercial and passenger vehicles, tractors, used vehicles, two-wheelers), about a quarter is home loans and loan against property, and the balance is SME and consumer credit (segment shares are model estimates; the pack gives only totals). Q2 FY27: revenue Rs9,271cr, interest cost Rs4,334cr, PAT Rs1,630cr (+41% y/y); AUM roughly Rs2.68 lakh cr (+25% per one source; another says +33% - treat as uncertain). Management retained its 20-23% AUM growth outlook and the board approved a Rs5,000cr QIP on 28 Oct. Q1 FY27 Stage 3 was 3.29% (net 1.81%) with a credit-cost guide of about 1.3-1.6%. The stock trades at 24x earnings and 4.1x book with a 19.4% ROE and a very high market beta of 1.5.

## What moves the stock, ranked
1. **Asset quality (-8.0 per +50bp credit cost)**: 50bp on Rs2.68 lakh cr is ~16% of earnings.
2. **Vehicle demand (+3.5 per +10% volumes)**: the engine of disbursements and AUM.
3. **Credit spreads (-2.0 per +50bp)** and **repo (-1.3 per +25bp)**: a fixed-rate asset book funded 55% floating; hikes squeeze NIM before repricing catches up.
4. **FPI flows (+2.0)**, **govt capex (+1.5)**, **rural demand (+1.5)**, **steel / infra proxy (+1.0)**.
5. Smaller: G-sec yield (-1.0), P_RBI_PRUDENTIAL (-1.0), monsoon (+1.0), GST (+1.0), housing (+0.7), unsecured (-0.7), Brent (-0.5).
Empirical check: global HRC steel is the one significant co-movement (+2.18, t +2.8; copper +1.27 t 1.9). The causal story (steel -> construction/mining activity -> CV demand/utilisation -> collections) is plausible but overlaps with the capex and auto-demand edges, so we carry +1.0, and flag it for de-duplication. Other factors have |t|<2.

## Transmission examples
- **Middle East escalation -> Brent up -> CPI up -> RBI hikes again -> bank MCLR/T-bill benchmarks up -> Chola's floating borrowings reprice in 1-3 months while 80% of its vehicle loans are fixed -> NIM compresses until new loans are priced higher.** Fourth order: tighter spreads -> lower disbursement growth in price-sensitive segments.
- **Brent up -> diesel and freight cost up -> truck-operator margins squeezed -> CV loan delinquencies rise -> Stage 3 up -> credit cost up** (damped because retail diesel is administered).
- **Brent up -> INR weaker -> FPI outflow -> NBFC multiples compress** (FII 24.9% of the cap table).
- **Good monsoon -> tractor and rural LCV sales up -> collections better -> credit cost down -> ROA up -> multiple supported** (a positive 3rd-order chain).
- **GST cut on vehicles -> vehicle sales up -> disbursements up -> AUM growth** (+1.0 per unit).

## Current situation
Stock Rs1,770 (+9.9% over one month; -8.7% over three months) after Q2. UBS/Jefferies/JM list Chola among top NBFC picks. The Rs5,000cr QIP, if executed, adds ~3.3% to share count; discount pricing is the near-term overhang. NIM moderated in Q2 on lower gains (PL), and AUM-growth data from different sources conflict.

## Upcoming
Q3 results (late Jan 2027), QIP execution (probability 0.7 by Mar 2027), RBI December MPC, Union Budget (Feb 2027), vehicle-sales data monthly, possible RBI prudential changes.

## Bull and bear
**Bull:** 25% AUM growth, ROE ~19%, credit cost easing, vehicle cycle supported by GST cut and festive demand, strong liability franchise. **Bear:** rate hikes squeeze spreads, 4.1x book leaves no cushion, Stage 3 at 3.3%, QIP dilution and a vehicle-demand slowdown.

## Data caveats
Screener.in numbers (revenue Rs9,271cr, PAT Rs1,630cr, book value Rs403) are consistent with press coverage, but the AUM and disbursement growth figures come from secondary sources that disagree (25% versus 33% AUM growth; a Quartr summary also showed a different PAT). We therefore keep the AUM-driven edges at medium or low confidence and recommend the Director verify the investor presentation before the numbers feed a ranking. The Murugappa group link to Tube Investments (TIINDIA) is from model knowledge and carries a deliberately tiny weight.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.