# BAJFINANCE — Bajaj Finance Ltd.
*NIFTY_50 · Financial Services · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -4.6%**, **12 months -7.6%** (rank 200 / 200 of 200 for 3m / 12m); beta 1.17
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +19.4%): 3 months 32%, 12 months 28%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -14.5% … P90 -4.7%; plausible 12m relative-return range incl. stock-specific noise: -43.1% … +17.7%
- Decomposition (12m): 0.5 × forward event exposure -13.5% (3m -7.9%; half assumed priced) + 0.5 × company-specific catalysts -0.7%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply -8.9% (beta-adjusted) vs a realised market-adjusted move of +14.3% — gap -23.3 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Credit cost / NPA cycle (higher = worse) (`F_ASSET_QUALITY_IN`) | +50 bp credit cost | -5.61 | -5.00 | -0.60 | -0.03 | +0.02 | — |
| Indian corporate credit spreads (`F_CREDIT_SPREADS_IN`) | +50 bp spreads | -5.05 | -5.00 | -0.12 | +0.06 | +0.01 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -4.49 | +0.00 | -3.57 | -0.92 | -0.00 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -4.37 | -3.00 | -1.40 | +0.03 | +0.01 | — |
| RBI prudential tightening (risk weights, LCR, provisioning) (`P_RBI_PRUDENTIAL`) | +1 = tightening step | -4.30 | -3.00 | -1.61 | +0.16 | +0.15 | — |
| Unsecured retail & microfinance stress (higher = worse) (`F_UNSECURED_STRESS`) | +1 pp delinquencies | -4.05 | -3.50 | -0.56 | -0.05 | +0.06 | — |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +3.08 | +0.00 | +1.60 | +1.11 | +0.36 | — |
| India 10-year G-sec yield (`F_GSEC_10Y_IN`) | +25 bp yield | -3.05 | -2.50 | -0.54 | -0.03 | +0.02 | — |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -2.78 | -2.00 | -0.39 | -0.27 | -0.12 | +3.5% |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -2.70 | -0.50 | -0.56 | -0.87 | -0.77 | -1.1% |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -2.65 | +0.00 | +0.00 | -2.09 | -0.55 | — |
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +2.53 | +2.50 | +0.24 | +0.20 | -0.41 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +2.36 | +2.00 | +0.15 | +0.08 | +0.14 | — |
| Monsoon rainfall vs normal (`F_MONSOON`) | +10% above long-period average | +2.12 | +0.00 | +0.56 | +0.70 | +0.85 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -5.5% | -5.5% | -5.4 | -0.1 | +0.0 | +0.0 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -5.4% | -5.4% | -4.8 | -0.7 | +0.2 | -0.1 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -5.4% | -5.4% | +0.0 | -4.1 | -1.2 | -0.1 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -5.2% | -5.2% | -4.4 | -0.3 | -0.2 | -0.3 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +6.8% | +3.4% | +5.8 | +0.4 | +0.2 | +0.4 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -2.7% | -2.7% | +0.0 | -0.7 | -0.9 | -1.1 |
| RBI MPC Dec 2026 (~4 Dec): hikes repo another 25 bp to 5.75% (`EV_RBI_DEC26_HIKE25`) | scheduled | 0.42 | -5.4% | -2.3% | -4.8 | -0.7 | +0.2 | -0.1 |
| Risk: USD/INR >98 and/or reserves < US$650bn (disorderly rupee, emergency RBI response) (`EV_RUPEE_BREAK_98_RESERVE_STRESS`) | risk_scenario | 0.18 | -12.3% | -2.2% | -10.3 | -2.2 | +0.1 | +0.1 |
| CPI prints >=6.0% (RBI upper tolerance) in Oct-Jan data (releases 12 Nov - 12 Feb) (`EV_CPI_BREACH_6PCT`) | anticipated | 0.60 | -3.6% | -2.1% | -2.5 | -1.2 | +0.1 | +0.0 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.25 | -8.2% | -2.1% | -5.0 | -2.9 | -0.3 | -0.0 |
| Budget FY2027-28: FY27 deficit overshoot confirmed and consolidation path slowed (`EV_BUDGET_FY28_FISCAL_SLIPPAGE`) | scheduled | 0.50 | -4.1% | -2.0% | -3.9 | -0.1 | -0.0 | -0.0 |
| Banking system liquidity turns to sustained deficit by end-March 2027 (`EV_BANKING_LIQUIDITY_DEFICIT_MAR27`) | anticipated | 0.60 | -3.4% | -2.0% | -3.5 | +0.0 | +0.0 | +0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → BAJFINANCE | +5.00% | +2.50% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → BAJFINANCE | -3.00% | -1.26% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → BAJFINANCE | -5.00% | -1.25% |
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → BAJFINANCE | -2.00% | -1.00% |
| 1 | EV_BANKING_LIQUIDITY_DEFICIT_MAR27 ⇒ F_CREDIT_SPREADS_IN → BAJFINANCE | -1.50% | -0.90% |
| 1 | EV_RBI_FEB27_HIKE25 ⇒ F_REPO_IN → BAJFINANCE | -3.00% | -0.81% |
| 1 | EV_ECL_ROLLOUT_APR27 ⇒ P_RBI_PRUDENTIAL → BAJFINANCE | -0.90% | -0.81% |
| 1 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → BAJFINANCE | -5.00% | -0.75% |
| 1 | EV_CPI_BREACH_6PCT ⇒ F_GSEC_10Y_IN → BAJFINANCE | -1.25% | -0.75% |
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_CREDIT_SPREADS_IN → BAJFINANCE | -1.50% | -0.75% |
| 1 | EV_CPI_BREACH_6PCT ⇒ F_REPO_IN → BAJFINANCE | -1.20% | -0.72% |
| 1 | EV_BANKING_LIQUIDITY_DEFICIT_MAR27 ⇒ F_LIQUIDITY_IN → BAJFINANCE | -1.20% | -0.72% |
| 1 | EV_ECL_ROLLOUT_APR27 ⇒ F_ASSET_QUALITY_IN → BAJFINANCE | -0.75% | -0.68% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_REPO_IN → BAJFINANCE | -3.00% | -0.54% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → BAJFINANCE | -3.00% | -0.54% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_GSEC_10Y_IN → BAJFINANCE | +1.55 | director_override | -3.88% |
| 1 | F_FPI_FLOWS → BAJFINANCE | -1.60 | events | -3.20% |
| 1 | F_REPO_IN → BAJFINANCE | +1.00 | events | -3.00% |
| 1 | F_CREDIT_SPREADS_IN → BAJFINANCE | +0.50 | events | -2.50% |
| 2 | F_MONSOON → F_UNSECURED_STRESS → BAJFINANCE | -1.56 | events | -0.87% |
| 2 | F_GDP_IN → F_ASSET_QUALITY_IN → BAJFINANCE | +0.50 | events | +0.80% |
| 1 | F_LIQUIDITY_IN → BAJFINANCE | -0.90 | events | -0.72% |
| 1 | F_URBAN_DEMAND → BAJFINANCE | +0.20 | events | +0.50% |
| 1 | F_AUTO_DEMAND_IN → BAJFINANCE | +0.50 | director_override | +0.50% |
| 2 | F_CPI_IN → F_UNSECURED_STRESS → BAJFINANCE | +1.15 | events | -0.48% |
| 2 | F_GDP_IN → F_CREDIT_GROWTH_IN → BAJFINANCE | +0.50 | events | +0.34% |
| 1 | F_GOLD → BAJFINANCE | -1.05 | observed | -0.31% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-11 | QIP launch/closing for Rs11,700cr (approvals pending: shareholder postal ballot/ SEBI QIP floor price) | corporate_action | 0.70 | -1.5% | -1.05% |
| 2027-01 | Quarterly business update (Q3 FY27 AUM, deposits) around 2027-01-03/04 | guidance | 0.90 | +0.5% | +0.45% |
| 2027-01-26 | Q3 FY27 results (date inferred from cadence: Q2 on 2026-10-19) | results | 0.90 | +0.0% | +0.00% |

## Analyst profile (agent research, sourced)
# BAJFINANCE - Bajaj Finance Ltd. (Nifty 50, consumer NBFC) - as of 2026-11-05

## Business
The largest diversified NBFC: AUM Rs5.85 lakh cr (+26.5% y/y), consumer durable and digital EMI finance, personal and business loans, SME, mortgages via Bajaj Housing Finance (AUM Rs1.5 lakh cr), vehicles, gold and deposits. Funded ~74% by borrowings (banks, NCD/CP, deposits). Promoters 54.7% (Bajaj Finserv ~51%), FIIs 19.8%, DIIs 17%.

## What moves the stock, ranked
1. **Funding cost, spreads and rate path** - RBI hiked to 5.50% on 2026-10-07 and moved to 'calibrated tightening'. Most assets are fixed-rate so NIM compresses before repricing. Repo +25bp ~ -3 (arithmetic: ~Rs376cr annual cost on floating funding = -1.4% PBT, plus rollover repricing and multiple), credit spreads +50bp ~ -5.
2. **Credit cost / asset quality** - +50bp credit cost = -5 (Rs2,750cr on ~10% of PBT, persistence 0.5). Unsecured stress +1pp = -3.5.
3. **Valuation/discount rate and FPI flows** - 34x P/E, 5.6x P/B; G-sec 10y +25bp ~ -2.5.
4. **Capital raise and dilution** - Rs11,700cr QIP (1.8% of mcap) plus Rs5,800cr warrants (0.9%): short-term supply overhang, long-term capital for ~25% growth.
5. **Regulation (RBI prudential)** - precedent of RBI action on BFL products.
6. **Demand** - urban demand, housing, autos.

Empirical pack: steel +1.74 (t 2.6) is significant but unrelated to the business, so weight 0; gold +1.16 (t 1.7) shrunk to +0.3; INR, Brent insignificant.

## Transmission examples
- **Middle East escalation -> Brent +10% -> India CPI +0.3pp, INR weaker -> RBI hikes again -> BFL funding cost up on floating bank lines (~35% of borrowings) within the quarter while fixed-rate loans reprice only on new disbursals -> NIM -10 to -15bp -> EPS -2 to -3% -> P/E de-rates at 34x -> equity -4 to -5%; second-order: consumer demand softens (urban demand down) and delinquencies rise at the bottom of the unsecured book.**
- **Gold price falls -> gold-loan LTV breaches (Reuters 2026-10-21 reported early stress) -> auctions -> NBFC sector credit-spread widening -> BFL bond issuance +20-30bp -> margin pressure.**
- **Bank liquidity tightens after the hike -> banks reprice term loans and CP -> BFL's CP/NCD rollover costs rise.**

## Current situation
Q2 PAT Rs6,266cr (+29%), AUM +26.5%. Share price Rs1,065 (-7% 3m but +10.5% 1m). Capital raise of Rs17,500cr approved on 2026-10-01; the stock fell 5-6% on the announcement in late September, rebounded 4-5% on Q2 business update, fell 3% after the Q2 call on margin commentary.

## Upcoming
QIP execution (Nov 2026), early-January Q3 business update, Q3 results late January 2027, December MPC.

## Bull / bear
Bull: strong AUM growth, credit-cost tailwind, raise completes cleanly, rates peak. Bear: margin compression persists, unsecured stress rises, dilution weighs, regulation, de-rating.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.