# INDUSINDBK — IndusInd Bank Ltd.
*MIDCAP_100 · Financial Services · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -4.2%**, **12 months -8.0%** (rank 184 / 187 of 200 for 3m / 12m); beta 1.23
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +19.7%): 3 months 34%, 12 months 45%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -23.8% … P90 +6.7%; plausible 12m relative-return range incl. stock-specific noise: -33.9% … +23.2%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves -1.6 pp (model impact -7.7% beta-adjusted vs realised market-adjusted move -4.5%); forward event exposure -9.4% (3m -3.9%; half assumed priced); company-specific events -1.1%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Credit cost / NPA cycle (higher = worse) (`F_ASSET_QUALITY_IN`) | +50 bp credit cost | -16.04 | -16.00 | +0.00 | -0.03 | -0.01 | — |
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | +10.08 | +0.00 | +6.08 | +5.11 | -1.11 | — |
| Unsecured retail & microfinance stress (higher = worse) (`F_UNSECURED_STRESS`) | +1 pp delinquencies | -7.81 | -6.00 | -1.44 | -0.23 | -0.14 | — |
| Monsoon rainfall vs normal (`F_MONSOON`) | +10% above long-period average | +6.91 | +0.00 | +2.03 | +3.68 | +1.21 | — |
| India real GDP growth (`F_GDP_IN`) | +1 pp | +6.85 | +4.00 | +3.90 | -0.90 | -0.15 | — |
| Private corporate capex (`F_PRIVATE_CAPEX`) | +10% capex growth | +5.93 | +0.00 | +2.88 | +4.40 | -1.35 | — |
| RBI prudential tightening (risk weights, LCR, provisioning) (`P_RBI_PRUDENTIAL`) | +1 = tightening step | -5.07 | -3.00 | -2.65 | +0.45 | +0.13 | — |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -4.68 | -3.50 | -0.75 | -0.41 | -0.01 | +3.5% |
| Indian wage / employee-cost inflation (`F_WAGES_IN`) | +2 pp | +4.62 | +0.00 | +0.96 | +2.06 | +1.60 | — |
| Central + state government capex (`F_GOVT_CAPEX`) | +10% capex growth | +4.55 | +0.00 | +1.44 | +3.07 | +0.04 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -4.54 | +0.00 | -0.99 | -1.64 | -1.91 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -4.29 | +0.00 | -1.49 | -3.02 | +0.21 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +4.09 | +4.00 | +0.09 | -0.04 | +0.04 | — |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +4.03 | +0.00 | +0.00 | +1.70 | +2.33 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -16.7% | -16.7% | +0.0 | -6.7 | -7.6 | -2.4 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -10.4% | -10.4% | -10.2 | -0.2 | +0.1 | -0.1 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -8.7% | -8.7% | +0.0 | -2.6 | -4.6 | -1.5 |
| RBI expected-credit-loss (ECL) provisioning goes live as scheduled (FY28 start) (`EV_ECL_ROLLOUT_APR27`) | scheduled | 0.62 | -11.3% | -7.0% | -12.0 | +0.8 | +0.0 | -0.0 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.28 | -21.3% | -6.0% | -14.0 | -6.8 | -0.7 | +0.3 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -5.9% | -5.9% | +0.0 | -1.7 | -4.0 | -0.2 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +11.6% | +5.8% | +11.4 | +0.2 | -0.1 | +0.1 |
| IMD April 2027 long-range forecast says normal or above-normal monsoon (>=96% LPA) (`EV_MONSOON27_FIRST_FORECAST_NORMAL`) | scheduled | 0.68 | +7.1% | +4.8% | +0.0 | +2.0 | +3.9 | +1.1 |
| Disorderly yen carry-trade unwind (Aug-2024-style) after BoJ/MoF action (`EV_YEN_CARRY_UNWIND_RISK`) | risk_scenario | 0.18 | -25.9% | -4.7% | -17.5 | -8.5 | -0.1 | +0.2 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.36 | -12.7% | -4.5% | -4.2 | -3.4 | -4.0 | -1.2 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -3.9% | -3.9% | -1.4 | -2.5 | -0.0 | -0.0 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.58 | +6.6% | +3.8% | +1.8 | +1.8 | +2.3 | +0.7 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → INDUSINDBK | +10.00% | +5.00% |
| 1 | EV_ECL_ROLLOUT_APR27 ⇒ F_ASSET_QUALITY_IN → INDUSINDBK | -8.00% | -4.96% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → INDUSINDBK | -14.00% | -3.92% |
| 1 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → INDUSINDBK | -17.50% | -3.15% |
| 1 | EV_ECL_ROLLOUT_APR27 ⇒ P_RBI_PRUDENTIAL → INDUSINDBK | -3.00% | -1.86% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_RISK_SENTIMENT → INDUSINDBK | -4.20% | -1.50% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → INDUSINDBK | -6.00% | -1.32% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_RISK_SENTIMENT → INDUSINDBK | -5.04% | -1.26% |
| 3 | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → F_GDP_IN → F_ASSET_QUALITY_IN → INDUSINDBK | +1.38% | +1.24% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → INDUSINDBK | -3.84% | -1.08% |
| 2 | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → F_GDP_IN → INDUSINDBK | +1.15% | +1.04% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_RISK_SENTIMENT → INDUSINDBK | +1.75% | +1.02% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_FPI_FLOWS → INDUSINDBK | -3.84% | -0.96% |
| 1 | EV_RBI_GOLD_LOAN_TIGHTEN ⇒ P_RBI_PRUDENTIAL → INDUSINDBK | -3.00% | -0.90% |
| 3 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_GDP_IN → F_ASSET_QUALITY_IN → INDUSINDBK | +1.28% | +0.87% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_FPI_FLOWS → INDUSINDBK | -1.60 | events | -6.40% |
| 1 | F_GSEC_10Y_IN → INDUSINDBK | +1.70 | events | -2.55% |
| 1 | F_GDP_IN → INDUSINDBK | +0.50 | events | +2.00% |
| 2 | F_MONSOON → F_UNSECURED_STRESS → INDUSINDBK | -1.56 | events | -1.50% |
| 1 | F_US_10Y → INDUSINDBK | +1.68 | observed | -1.34% |
| 2 | F_GDP_IN → F_ASSET_QUALITY_IN → INDUSINDBK | +0.50 | events | +1.28% |
| 2 | F_CPI_IN → F_UNSECURED_STRESS → INDUSINDBK | +1.15 | events | -0.83% |
| 2 | F_RURAL_DEMAND → F_ASSET_QUALITY_IN → INDUSINDBK | -0.25 | events | -0.64% |
| 2 | F_REPO_IN → F_ASSET_QUALITY_IN → INDUSINDBK | +1.00 | events | -0.64% |
| 3 | F_MONSOON → F_UNSECURED_STRESS → F_ASSET_QUALITY_IN → INDUSINDBK | -1.56 | events | -0.60% |
| 1 | F_GOLD → INDUSINDBK | -1.05 | observed | -0.42% |
| 1 | F_RISK_SENTIMENT → INDUSINDBK | +0.11 | observed | -0.39% |

## Analyst profile (agent research, sourced)
# INDUSINDBK - IndusInd Bank Ltd. (as of 2026-11-05)

## Business
IndusInd Bank is a mid-sized private bank historically strong in vehicle finance, microfinance and forex/trade, with a sizeable corporate book. After the FY25 derivative-accounting problem and credit-cost spike (model knowledge), it has been rebuilding profit: Q2 FY27 net profit was Rs1,242cr per screener (Rs1,176cr as reported by Moneycontrol - consolidated vs standalone likely), against a Rs437cr loss a year earlier. TTM earnings are only Rs3,001cr, so the Rs71k cr market cap (about 1.05x book) is priced on recovery, not current ROE of 1.4%. Promoters hold just 15.82%; institutions own ~72%.

## What moves the stock (ranked)
1. **Credit cost (-16 per +50bp)** and **unsecured/MFI stress (-6 per +1pp)**: thin earnings make every provisioning basis point count for 2-3% of profit.
2. **Macro growth and risk (GDP +4.0; VIX -3.5; FPI flows +4.0)**: a beta-1.3 stock owned by FIIs and DIIs.
3. **Funding and NIM (deposit growth +2.5; repo -0.3)**: FCNR(B) deposits cost 7-8bp of NIM in Q2; management expects recovery in H2 as asset yields reprice.
4. **Regulatory/legal (-3.0 prudential; litigation tail)**.
5. **Rates/valuation (G-sec -1.5; US10Y -0.8)** and **INR (-0.3, ambiguous)**.

## Transmission examples
- **Middle East escalation -> Brent ~$105 -> INR ~97 and CPI up -> RBI hikes again**: 2nd order: commercial-vehicle and two-wheeler borrowers face higher fuel costs and EMIs; MFI borrowers see food inflation. 3rd: delinquencies +0.5-1pp over 2-3 quarters (-3 to -6). 4th: with a 1.05x P/B and little capital buffer, the market cuts the recovery narrative (-2 to -3 more) and FIIs reduce exposure (-2).
- **Rate hike -> EBLR loans reprice -> NIM recovers faster than deposits**: +25bp -> +4bp NIM (+1 to PAT) but RBI's tightening slows vehicle demand (-0.5); net near zero.
- **Gold price shock**: gold loans (new focus) are collateralised; a 10% gold fall reduces collateral cushion but not margin; small effect. **Gold up** also raises ticket size.
- **Good monsoon -> rural income -> MFI collections up** -> credit cost -5bp -> +3.5% PAT.

## Current situation
Stock -10% in 3 months, ~flat month on month; Reuters (2026-10-23): margin hit from foreign deposits to ease in Q3. Jefferies cut its target after Q2 despite the profit swing. Management is cautious on microfinance and is pivoting to gold loans and higher-yielding assets. FII ownership rose to 30.5% (Sep 2026) from 28.6%.

## Upcoming
Q3 results ~late January 2027 (estimated): NIM recovery proof point; RBI MPC December; any resolution of FY25 accounting inquiries; promoter/ownership events.

## Bull case
Credit cost normalises, NIM rebounds 20-30bp, ROE rises toward 8-10%, stock re-rates from 1.05x to 1.4x book (+30%).
## Bear case
Microfinance/vehicle stress returns with higher rates and fuel costs, regulatory/litigation tail, NIM stuck: -25% or worse.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.