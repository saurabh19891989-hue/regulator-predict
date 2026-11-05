# BAJFINANCE — Bajaj Finance Ltd.
*NIFTY_50 · Financial Services · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -10.4%**, **12 months -18.8%** (rank 200 / 200 of 200 for 3m / 12m); beta 1.17
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +19.4%): 3 months 14%, 12 months 15%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -32.9% … P90 -11.2%; plausible 12m relative-return range incl. stock-specific noise: -61.6% … +3.3%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves -5.3 pp (model impact -10.6% beta-adjusted vs realised market-adjusted move +14.3%); forward event exposure -24.0% (3m -12.2%; half assumed priced); company-specific events -0.7%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| India CPI inflation (`F_CPI_IN`) | +1 pp | -9.57 | +0.00 | -5.30 | -3.92 | -0.36 | — |
| Credit cost / NPA cycle (higher = worse) (`F_ASSET_QUALITY_IN`) | +50 bp credit cost | -5.61 | -5.00 | -0.60 | -0.03 | +0.02 | — |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -5.27 | +0.00 | +0.00 | -3.04 | -2.23 | — |
| Indian corporate credit spreads (`F_CREDIT_SPREADS_IN`) | +50 bp spreads | -5.05 | -5.00 | -0.12 | +0.06 | +0.01 | — |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +4.43 | +0.00 | +1.60 | +1.64 | +1.19 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -4.35 | -3.00 | -1.40 | +0.02 | +0.03 | — |
| RBI prudential tightening (risk weights, LCR, provisioning) (`P_RBI_PRUDENTIAL`) | +1 = tightening step | -4.30 | -3.00 | -1.61 | +0.16 | +0.15 | — |
| Unsecured retail & microfinance stress (higher = worse) (`F_UNSECURED_STRESS`) | +1 pp delinquencies | -4.05 | -3.50 | -0.56 | -0.05 | +0.06 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -3.89 | -0.50 | -0.88 | -1.50 | -1.01 | -1.1% |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -3.32 | +0.00 | -0.54 | -0.68 | -2.09 | — |
| Brent crude oil price (`F_BRENT`) | +10% Brent | -3.15 | +0.00 | -0.40 | -1.49 | -1.26 | +0.0% |
| India 10-year G-sec yield (`F_GSEC_10Y_IN`) | +25 bp yield | -3.15 | -2.50 | -0.62 | -0.05 | +0.02 | — |
| India FX reserves (RBI intervention) (`NEW_FX_RESERVES_IN`) | +US$25bn reserves (RBI buys / net inflows) | +2.97 | +0.00 | +0.98 | +1.56 | +0.42 | — |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -2.94 | -2.00 | -0.39 | -0.32 | -0.23 | +3.5% |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -17.4% | -17.4% | +0.0 | -2.8 | -7.8 | -6.9 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -11.2% | -11.2% | +0.0 | -6.1 | -4.6 | -0.5 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -6.5% | -6.5% | -5.2 | -0.3 | -0.3 | -0.6 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -5.7% | -5.7% | -5.4 | -0.2 | -0.0 | +0.0 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -5.4% | -5.4% | -4.8 | -0.7 | +0.2 | -0.1 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.36 | -11.7% | -4.2% | -2.4 | -1.3 | -4.1 | -3.8 |
| RBI expected-credit-loss (ECL) provisioning goes live as scheduled (FY28 start) (`EV_ECL_ROLLOUT_APR27`) | scheduled | 0.62 | -6.6% | -4.1% | -6.5 | -0.3 | +0.1 | +0.0 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -3.9% | -3.9% | +0.0 | -2.7 | -0.8 | -0.4 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.58 | +6.3% | +3.7% | +1.0 | +0.7 | +2.4 | +2.2 |
| Gold and silver slump from January 2026 peaks (silver -53%, gold -24%) (`EV_PRECIOUS_METALS_CRASH_2026`) | occurred | 1.00 | -3.7% | -3.7% | -0.3 | -2.3 | -0.5 | -0.5 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.28 | -12.9% | -3.6% | -8.0 | -3.5 | -0.8 | -0.6 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +7.2% | +3.6% | +5.8 | +0.4 | +0.4 | +0.7 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → BAJFINANCE | +5.00% | +2.50% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → BAJFINANCE | -8.00% | -2.24% |
| 1 | EV_ECL_ROLLOUT_APR27 ⇒ P_RBI_PRUDENTIAL → BAJFINANCE | -3.00% | -1.86% |
| 1 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → BAJFINANCE | -10.00% | -1.80% |
| 1 | EV_ECL_ROLLOUT_APR27 ⇒ F_ASSET_QUALITY_IN → BAJFINANCE | -2.50% | -1.55% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → BAJFINANCE | -3.00% | -1.20% |
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → BAJFINANCE | -2.00% | -1.00% |
| 1 | EV_BANKING_LIQUIDITY_DEFICIT_MAR27 ⇒ F_CREDIT_SPREADS_IN → BAJFINANCE | -1.50% | -0.90% |
| 1 | EV_RBI_GOLD_LOAN_TIGHTEN ⇒ P_RBI_PRUDENTIAL → BAJFINANCE | -3.00% | -0.90% |
| 2 | EV_PULSES_VEG_SPIKE_WINTER ⇒ F_CPI_IN → F_REPO_IN → BAJFINANCE | -3.46% | -0.86% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_RISK_SENTIMENT → BAJFINANCE | -2.40% | -0.86% |
| 1 | EV_RBI_FEB27_HIKE25 ⇒ F_REPO_IN → BAJFINANCE | -3.00% | -0.81% |
| 1 | EV_CPI_BREACH_6PCT ⇒ F_GSEC_10Y_IN → BAJFINANCE | -1.25% | -0.75% |
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_CREDIT_SPREADS_IN → BAJFINANCE | -1.50% | -0.75% |
| 1 | EV_CPI_BREACH_6PCT ⇒ F_REPO_IN → BAJFINANCE | -1.20% | -0.72% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_GSEC_10Y_IN → BAJFINANCE | +1.70 | events | -4.25% |
| 1 | F_FPI_FLOWS → BAJFINANCE | -1.60 | events | -3.20% |
| 1 | F_REPO_IN → BAJFINANCE | +1.00 | events | -3.00% |
| 1 | F_CREDIT_SPREADS_IN → BAJFINANCE | +0.50 | events | -2.50% |
| 2 | F_MONSOON → F_UNSECURED_STRESS → BAJFINANCE | -1.56 | events | -0.87% |
| 2 | F_GDP_IN → F_ASSET_QUALITY_IN → BAJFINANCE | +0.50 | events | +0.80% |
| 1 | F_LIQUIDITY_IN → BAJFINANCE | -0.90 | events | -0.72% |
| 1 | F_URBAN_DEMAND → BAJFINANCE | +0.20 | events | +0.50% |
| 2 | F_CPI_IN → F_UNSECURED_STRESS → BAJFINANCE | +1.15 | events | -0.48% |
| 2 | F_GDP_IN → F_CREDIT_GROWTH_IN → BAJFINANCE | +0.50 | events | +0.34% |
| 1 | F_GOLD → BAJFINANCE | -1.05 | observed | -0.31% |
| 2 | F_GDP_IN → F_UNSECURED_STRESS → BAJFINANCE | +0.50 | events | +0.28% |

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