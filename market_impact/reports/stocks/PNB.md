# PNB — Punjab National Bank
*NIFTY_NEXT_50 · Financial Services · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +1.4%**, **12 months +1.3%** (rank 20 / 48 of 200 for 3m / 12m); beta 1.22
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +23.0%): 3 months 55%, 12 months 55%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -2.8% … P90 +3.7%; plausible 12m relative-return range incl. stock-specific noise: -29.5% … +33.9%
- Decomposition (12m): 0.5 × forward event exposure +1.8% (3m +2.4%; half assumed priced) + 0.5 × company-specific catalysts +1.8%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply +1.2% (beta-adjusted) vs a realised market-adjusted move of +15.5% — gap -14.4 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Credit cost / NPA cycle (higher = worse) (`F_ASSET_QUALITY_IN`) | +50 bp credit cost | -6.05 | -6.00 | +0.00 | -0.03 | -0.01 | — |
| India real GDP growth (`F_GDP_IN`) | +1 pp | +4.35 | +3.00 | +1.95 | -0.50 | -0.10 | — |
| RBI prudential tightening (risk weights, LCR, provisioning) (`P_RBI_PRUDENTIAL`) | +1 = tightening step | -4.28 | -3.00 | -1.51 | +0.20 | +0.03 | — |
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | +3.96 | +0.00 | +3.01 | +1.26 | -0.31 | — |
| Central + state government capex (`F_GOVT_CAPEX`) | +10% capex growth | +3.33 | +2.00 | +0.54 | +0.83 | -0.04 | — |
| Private corporate capex (`F_PRIVATE_CAPEX`) | +10% capex growth | +3.03 | +0.00 | +2.32 | +1.07 | -0.37 | — |
| Monsoon rainfall vs normal (`F_MONSOON`) | +10% above long-period average | +2.46 | +0.00 | +0.93 | +1.23 | +0.30 | — |
| Bank deposit growth / funding ease (`F_DEPOSIT_GROWTH_IN`) | +3 pp | +2.15 | +2.00 | +0.40 | -0.18 | -0.07 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +2.12 | +2.00 | +0.11 | -0.04 | +0.05 | — |
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +1.74 | +0.00 | +1.20 | +0.73 | -0.20 | — |
| General-government fiscal slippage / extra borrowing vs budget (Centre + states) (`NEW_FISCAL_SLIPPAGE_IN`) | +0.5 pp of GDP deficit above budget (~Rs2 lakh cr) | -1.73 | +0.00 | -1.24 | -0.22 | -0.27 | — |
| Unsecured retail & microfinance stress (higher = worse) (`F_UNSECURED_STRESS`) | +1 pp delinquencies | -1.65 | -0.80 | -0.68 | -0.07 | -0.09 | — |
| Indian wage / employee-cost inflation (`F_WAGES_IN`) | +2 pp | +1.61 | +0.00 | +0.13 | +1.09 | +0.39 | — |
| India 10-year G-sec yield (`F_GSEC_10Y_IN`) | +25 bp yield | -1.58 | -1.50 | +0.00 | -0.06 | -0.02 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -4.7% | -4.7% | -4.4 | -0.2 | +0.1 | -0.1 |
| India Q1 FY27 GDP grows 7.8% (31 Aug 2026), beating ~7.3% consensus (`EV_GDP_Q1FY27_7_8`) | occurred | 1.00 | +4.1% | +4.1% | +3.5 | +1.0 | -0.3 | -0.1 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -3.1% | -3.1% | +0.0 | -1.2 | -1.5 | -0.4 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -2.8% | -2.8% | -2.5 | -0.2 | -0.1 | -0.0 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +5.3% | +2.7% | +5.0 | +0.3 | -0.1 | +0.1 |
| RBI expected-credit-loss (ECL) provisioning goes live as scheduled (FY28 start) (`EV_ECL_ROLLOUT_APR27`) | scheduled | 0.90 | -2.1% | -1.9% | -2.2 | +0.1 | +0.0 | -0.0 |
| IMD April 2027 long-range forecast says normal or above-normal monsoon (>=96% LPA) (`EV_MONSOON27_FIRST_FORECAST_NORMAL`) | scheduled | 0.68 | +2.5% | +1.7% | +0.0 | +0.9 | +1.3 | +0.2 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -1.4% | -1.4% | +0.0 | -0.3 | -1.1 | +0.1 |
| US midterms (3 Nov 2026): Democrats win House and Senate (`EV_US_MIDTERMS_DEM_SWEEP`) | occurred | 1.00 | +1.2% | +1.2% | +1.0 | +0.2 | -0.0 | +0.0 |
| Rural demand indicators mixed: tractor volumes dip in Oct, 2W festive sales firm, rural CPI above urban, rural jobs scheme person-days down (`EV_RURAL_DEMAND_SOFT26`) | occurred | 1.00 | -1.2% | -1.2% | +0.0 | -0.9 | -0.4 | +0.1 |
| North-east monsoon 2026 normal or above-normal (relief for southern reservoirs) (`EV_NEMONSOON26_NORMAL_UP`) | anticipated | 0.85 | +1.3% | +1.1% | +0.0 | +0.5 | +0.7 | +0.2 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.55 | +2.0% | +1.1% | +0.0 | +1.2 | +0.5 | +0.3 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → PNB | +5.00% | +2.50% |
| 1 | EV_ECL_ROLLOUT_APR27 ⇒ P_RBI_PRUDENTIAL → PNB | -0.90% | -0.81% |
| 1 | EV_ECL_ROLLOUT_APR27 ⇒ F_ASSET_QUALITY_IN → PNB | -0.90% | -0.81% |
| 1 | EV_BANKING_LIQUIDITY_DEFICIT_MAR27 ⇒ F_LIQUIDITY_IN → PNB | -1.20% | -0.72% |
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → PNB | -1.20% | -0.60% |
| 2 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_GDP_IN → PNB | +0.80% | +0.54% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → PNB | -3.00% | -0.54% |
| 1 | EV_INDIA_STAGFLATION_SCARE ⇒ F_GDP_IN → PNB | -4.50% | -0.54% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → PNB | -1.92% | -0.48% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_FPI_FLOWS → PNB | -1.92% | -0.48% |
| 1 | EV_Q2_FY27_GDP_STRONG ⇒ F_GDP_IN → PNB | +0.60% | +0.48% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → PNB | -1.87% | -0.47% |
| 1 | EV_CPI_BREACH_6PCT ⇒ F_GSEC_10Y_IN → PNB | -0.75% | -0.45% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → PNB | +1.00% | +0.42% |
| 2 | EV_BUDGET27_AGRI_RURAL ⇒ F_RURAL_DEMAND → F_GDP_IN → PNB | +0.58% | +0.40% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_FPI_FLOWS → PNB | -1.60 | events | -3.20% |
| 1 | F_GSEC_10Y_IN → PNB | +1.55 | director_override | -2.33% |
| 1 | F_GDP_IN → PNB | +0.50 | events | +1.50% |
| 1 | F_REPO_IN → PNB | +1.00 | events | +1.00% |
| 1 | F_LIQUIDITY_IN → PNB | -0.90 | events | -0.72% |
| 2 | F_GDP_IN → F_ASSET_QUALITY_IN → PNB | +0.50 | events | +0.48% |
| 1 | F_GOVT_CAPEX → PNB | +0.20 | director_override | +0.40% |
| 2 | F_REPO_IN → F_CREDIT_GROWTH_IN → PNB | +1.00 | events | -0.29% |
| 2 | F_RURAL_DEMAND → F_ASSET_QUALITY_IN → PNB | -0.25 | events | -0.24% |
| 2 | F_REPO_IN → F_ASSET_QUALITY_IN → PNB | +1.00 | events | -0.24% |
| 2 | F_GDP_IN → F_CREDIT_GROWTH_IN → PNB | +0.50 | events | +0.21% |
| 2 | F_MONSOON → F_UNSECURED_STRESS → PNB | -1.56 | events | -0.20% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-12 | Government PSU-bank consolidation/stake-sale announcements (reports 2026-10-23; PNB not named for stake cut) | corporate_action | 0.30 | +2.0% | +0.60% |
| 2027-01 | Q3 FY27 results (inferred; Q2 on 2026-10-16): proof of 7-9bp NIM expansion | results | 0.92 | +0.5% | +0.46% |
| 2027-02 | Debut dollar bond (offshore) if hedging costs allow | capex | 0.40 | +0.0% | +0.00% |
| 2027-03 | Cabinet raises FDI cap in PSU banks from 20% to 49% (draft cabinet note with RBI backing; reports 21 Oct 2026) *(review: [DIRECTOR_CE] RT_N50_A: replaces conflated P_FDI_RULES edge)* | regulatory | 0.50 | +1.5% | +0.75% |

## Analyst profile (agent research, sourced)
# PNB - Punjab National Bank (Nifty Next 50, I_PSU_BANKS) - as of 2026-11-05

## Business
PNB is a government-owned (70.08%) bank with roughly Rs11-12 lakh cr of advances and Rs16-17 lakh cr of deposits (model estimates; reported Q2 NII is Rs11,601cr). About half the loan book is linked to the repo rate (EBLR), the rest to MCLR or fixed rates, so PNB is asset-sensitive: policy hikes lift yields faster than deposit costs. Retail, agriculture and MSME account for the majority of credit, with a large corporate book that has largely finished its post-2018 clean-up. The stock trades at 0.95x book and 6.9x earnings and rallied 12% in a month on a strong Q2.

## What moves the stock, ranked
1. **Credit cost / asset quality (w -6 per +50bp).** Provisions drove the earnings recovery (financing profit Rs3,834cr vs Rs2,242cr a year earlier); a cycle turn would reverse it. Slippages were up quarter on quarter even as GNPA improved.
2. **Repo and NIM (w +1.0).** The 2026-10-07 hike (to 5.50%) is a net positive: PNB guides NIM +7-9bp in Q3. The sign could flip if hikes slow credit growth or raise deposit costs faster.
3. **ECL and prudential rules (w -3.0).** RBI's expected-credit-loss framework starts April 2027. SBI estimates Rs19,500cr post-tax, Union Bank Rs5,500cr; PNB's figure is not yet found. PSU banks are expected to face more pressure.
4. **G-sec yields (w -1.5).** AFS MTM and cost of equity; 10y is 7.19%, down from 7.48%.
5. **Growth: credit, deposits, GDP, capex (+2.5, +2.0, +3.0, +2.0).** Deposit mobilisation is the constraint; Q2 business updates showed it clearly.
6. **Policy and flows (FDI/consolidation +3, FPI +2, liquidity +0.8).**

## Transmission examples
- **Oil -> NIM -> equity:** Middle East escalation -> Brent up (95 now) -> CPI up -> RBI hikes again (minutes flag more) -> EBLR loans reprice within a month, deposits lag -> NIM rises 7-9bp -> EPS up; but 10y yields rise -> AFS losses -> net effect roughly +1 on equity, with credit-growth risk if crude persists.
- **Liquidity -> competition:** RBI drains surplus (CRR maintenance at 99%) -> deposit competition intensifies -> PSU banks raise term-deposit rates -> NIM gain from the hike is partly given back -> credit growth slows -> loan targets missed.
- **Fiscal chain:** government capex up -> PSU borrowers and EPC contractors repay and borrow -> credit growth and asset quality improve -> credit cost falls; conversely a fiscal squeeze pushes G-sec yields up, hurting the treasury book.
- **ECL chain:** ECL rule (April 2027) -> large one-time provisions for PSU banks -> capital pressure -> dividend/capital-raise concerns -> government capital or stake sale talk -> multiple pressure on PSU peers; the 2026-10-23 stake-cut reports show the direction (PNB not named).

## Current situation
Q2 FY27 PAT Rs5,532cr (+13%), NII +11%, NIM above guidance, profit target Rs6,000cr per quarter. PNB raised lending rates after the hike. A debut dollar bond (planned early 2027) is deferred industry-wide due to hedging costs. The government is pursuing privatisation/consolidation (IDBI to Fairfax approved 2026-10-14; four other PSU banks to cut stakes to 75%; PNB not among them).

## Upcoming
Q3 results (Jan 2027), December MPC, ECL effective April 2027, consolidation announcements, any dollar bond.

## Bull and bear
Bull: NIM expansion, credit cost stays low, sector re-rating from consolidation. Bear: slippages climb, ECL hit is larger than expected, deposit competition erodes NIM, yields spike. Confidence medium; ECL figure and the loan-book split are not disclosed in the sources reviewed.

## Notes on evidence quality
Reported figures (PAT Rs5,532cr, NII Rs11,601cr, NIM guidance of 7-9bp, lending-rate hikes, dollar bond deferral, RBI penalty) are from dated news headlines whose URLs are in the JSON. Balance-sheet scale, the EBLR share of loans, the size of the AFS book and the deposit repricing lag are model estimates and should be replaced with investor-presentation numbers. The pack's empirical sensitivities are all statistically weak for PNB (largest |t| is 2.9 for global gas, with no plausible mechanism), so they were not used to shrink any weight.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.