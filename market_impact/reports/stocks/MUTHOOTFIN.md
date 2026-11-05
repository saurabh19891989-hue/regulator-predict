# MUTHOOTFIN — Muthoot Finance Ltd.
*NIFTY_NEXT_50 · Financial Services · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -2.2%**, **12 months -5.0%** (rank 157 / 162 of 200 for 3m / 12m); beta 1.04
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +28.6%): 3 months 44%, 12 months 32%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -10.4% … P90 +2.8%; plausible 12m relative-return range incl. stock-specific noise: -40.8% … +41.7%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +0.0 pp (model impact -6.6% beta-adjusted vs realised market-adjusted move -17.2%); forward event exposure -5.8% (3m -2.1%; half assumed priced); company-specific events -1.9%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Gold-loan competitive intensity (bank/NBFC entry, yield compression) (`NEW_GOLD_LOAN_COMPETITION`) | +1 = ~100bp industry gold-loan yield compression or ~3pp share shift to banks/new entrants | -7.00 | -7.00 | +0.00 | +0.00 | +0.00 | — |
| RBI prudential tightening (risk weights, LCR, provisioning) (`P_RBI_PRUDENTIAL`) | +1 = tightening step | -4.78 | -4.00 | -0.88 | +0.01 | +0.09 | — |
| Credit cost / NPA cycle (higher = worse) (`F_ASSET_QUALITY_IN`) | +50 bp credit cost | -3.79 | -3.50 | -0.30 | +0.00 | +0.01 | — |
| Gold price (`F_GOLD`) | +8% gold (USD) | +3.42 | +3.50 | +0.00 | -0.06 | -0.02 | -8.4% |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -3.40 | +0.00 | -2.03 | -1.43 | +0.06 | — |
| US dollar index (`F_DXY`) | +3% DXY | -2.65 | +0.00 | -2.28 | -0.19 | -0.18 | +2.2% |
| Indian corporate credit spreads (`F_CREDIT_SPREADS_IN`) | +50 bp spreads | -2.42 | -2.50 | +0.00 | +0.05 | +0.03 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +2.16 | +2.00 | +0.07 | +0.01 | +0.07 | — |
| Bank credit growth (`F_CREDIT_GROWTH_IN`) | +3 pp | -2.14 | +0.00 | -1.26 | -0.78 | -0.10 | — |
| US 10-year Treasury yield (`F_US_10Y`) | +25 bp yield | -2.10 | +0.00 | -1.50 | -0.51 | -0.09 | +9.4% |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -1.96 | +0.00 | +0.00 | -1.16 | -0.81 | — |
| Formalisation of the economy (`T_FORMALISATION`) | +1 | +1.91 | +2.00 | +0.00 | -0.06 | -0.04 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -1.84 | -1.50 | -0.44 | +0.05 | +0.05 | — |
| India real GDP growth (`F_GDP_IN`) | +1 pp | -1.59 | +0.00 | +0.08 | -1.15 | -0.53 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Gold and silver slump from January 2026 peaks (silver -53%, gold -24%) (`EV_PRECIOUS_METALS_CRASH_2026`) | occurred | 1.00 | -5.6% | -5.6% | -3.7 | -1.7 | -0.2 | -0.1 |
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -4.9% | -4.9% | +0.0 | +0.0 | -2.8 | -2.2 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -4.7% | -4.7% | -4.4 | -0.1 | -0.1 | -0.2 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -4.6% | -4.6% | +0.0 | -4.2 | -0.3 | -0.1 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -4.0% | -4.0% | +0.0 | -2.3 | -1.7 | +0.1 |
| RBI expected-credit-loss (ECL) provisioning goes live as scheduled (FY28 start) (`EV_ECL_ROLLOUT_APR27`) | scheduled | 0.62 | -5.9% | -3.6% | -5.8 | -0.3 | +0.1 | +0.0 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -2.8% | -2.8% | +0.0 | -2.3 | -0.4 | -0.1 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +5.4% | +2.7% | +5.0 | +0.1 | +0.1 | +0.2 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -2.3% | -2.3% | -2.3 | -0.1 | +0.1 | -0.0 |
| Gold falls to ~$3,500 / silver to ~$40 on Fed hike(s) and strong dollar (`EV_PRECIOUS_METALS_FURTHER_SLIDE`) | risk_scenario | 0.30 | -7.2% | -2.2% | -6.7 | -0.2 | -0.3 | -0.1 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -2.0% | -2.0% | -2.1 | +0.0 | +0.1 | +0.1 |
| Gold/silver rebound as Fed hike fears fade or Iran war ends (`EV_PRECIOUS_METALS_REBOUND_H1_2027`) | anticipated | 0.45 | +4.4% | +2.0% | +3.5 | +0.7 | +0.2 | +0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → MUTHOOTFIN | +5.00% | +2.50% |
| 1 | EV_ECL_ROLLOUT_APR27 ⇒ P_RBI_PRUDENTIAL → MUTHOOTFIN | -4.00% | -2.48% |
| 1 | EV_PRECIOUS_METALS_FURTHER_SLIDE ⇒ F_GOLD → MUTHOOTFIN | -6.65% | -2.00% |
| 1 | EV_PRECIOUS_METALS_REBOUND_H1_2027 ⇒ F_GOLD → MUTHOOTFIN | +3.50% | +1.58% |
| 1 | EV_RBI_GOLD_LOAN_TIGHTEN ⇒ P_RBI_PRUDENTIAL → MUTHOOTFIN | -4.00% | -1.20% |
| 1 | EV_ECL_ROLLOUT_APR27 ⇒ F_ASSET_QUALITY_IN → MUTHOOTFIN | -1.75% | -1.09% |
| 1 | EV_ECL_DEFERRED ⇒ P_RBI_PRUDENTIAL → MUTHOOTFIN | +2.40% | +0.91% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → MUTHOOTFIN | -2.99% | -0.84% |
| 2 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → MUTHOOTFIN | -3.73% | -0.67% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → MUTHOOTFIN | -3.00% | -0.66% |
| 2 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ C_MIDEAST_CONFLICT → F_GOLD → MUTHOOTFIN | -1.12% | -0.65% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → MUTHOOTFIN | -1.50% | -0.60% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → MUTHOOTFIN | -1.92% | -0.54% |
| 2 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ C_MIDEAST_CONFLICT → F_GOLD → MUTHOOTFIN | +1.34% | +0.48% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_FPI_FLOWS → MUTHOOTFIN | -1.92% | -0.48% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_GOLD → MUTHOOTFIN | -1.05 | observed | -3.67% |
| 1 | F_FPI_FLOWS → MUTHOOTFIN | -1.60 | events | -3.20% |
| 1 | F_GSEC_10Y_IN → MUTHOOTFIN | +1.70 | events | -1.70% |
| 1 | F_REPO_IN → MUTHOOTFIN | +1.00 | events | -1.50% |
| 1 | F_CREDIT_SPREADS_IN → MUTHOOTFIN | +0.50 | events | -1.25% |
| 1 | T_FORMALISATION → MUTHOOTFIN | +0.30 | events | +0.60% |
| 2 | F_GDP_IN → F_ASSET_QUALITY_IN → MUTHOOTFIN | +0.50 | events | +0.56% |
| 2 | F_GDP_IN → P_RBI_PRUDENTIAL → MUTHOOTFIN | +0.50 | events | -0.32% |
| 3 | F_GDP_IN → F_CREDIT_GROWTH_IN → P_RBI_PRUDENTIAL → MUTHOOTFIN | +0.50 | events | -0.15% |
| 2 | F_RURAL_DEMAND → F_ASSET_QUALITY_IN → MUTHOOTFIN | -0.25 | events | -0.14% |
| 2 | F_REPO_IN → F_ASSET_QUALITY_IN → MUTHOOTFIN | +1.00 | events | -0.14% |
| 3 | F_MONSOON → F_UNSECURED_STRESS → F_ASSET_QUALITY_IN → MUTHOOTFIN | -1.56 | events | -0.13% |

## Analyst profile (agent research, sourced)
# MUTHOOTFIN - Muthoot Finance Ltd. (Nifty Next 50, I_GOLD_LOANS) - as of 2026-11-05

## Business
Muthoot Finance is India's largest gold-loan non-bank lender. Short-tenure loans (typically 3-12 months, increasingly with monthly interest/EMI structures) are made against pledged jewellery at a regulated loan-to-value ratio, funded by bank term loans, NCDs, CP and some foreign-currency debt. About 88% of income is the standalone gold-loan franchise, concentrated in southern India; the rest is Belstar microfinance, Muthoot Homefin, vehicle/personal loans and a Sri Lankan subsidiary. Promoters hold 73.35%; FIIs have cut from 12.3% to 9.7% since March 2026 while DIIs rose to 12.5%. At Rs2,845 (P/E 10.2, P/B 2.6) the stock is 31% below its Rs4,150 high and 6m -21%, i.e. the market already prices a gold-cycle and asset-quality de-rating.

## What moves the stock, ranked
1. **Gold price (F_GOLD, w +3.5 per +8%).** A higher price raises the loan per gram and AUM; the pack's empirical elasticity (+2.87, t=+3.3) is the only statistically strong channel and agrees with the fundamental estimate. Gold is 22-26% below its January peak but rebounded in August; AUM growth of ~42% y/y was powered by price as much as tonnage.
2. **Asset quality (w -3.5 per +50bp credit cost).** Stage III is 3.87% and management (FE, 2026-11-01) blames short-tenure and monthly-EMI loans. Reuters (2026-10-21) reports peers see early stress. Gold loans are over-collateralised, so loss severity is low, but sentiment and auction delays matter.
3. **Competition (NEW_GOLD_LOAN_COMPETITION, w -7 per 100bp yield compression).** Banks, L&T Finance, ABCAPITAL (entered 2026-08-19) and fintech entrants pursue the same customer; this is the largest negative if it materialises.
4. **RBI prudential rules (w -4).** Gold Loan Directions (2025) already set LTV and auction norms; a tightening of tenor/EMI structures is the main regulatory risk.
5. **Funding cost: repo, G-sec, spreads (w -1.5, -1.0, -2.5).** Repo went to 5.50% on 2026-10-07 with more hikes flagged in the minutes; 10y G-sec is 7.19%. Short-tenure assets reprice quickly, so the net NIM hit is small relative to growth NBFCs such as BAJFINANCE.
6. **Flows and sentiment (FPI +2), policy duty (+1.5), formalisation (+2).**

## Transmission examples
- **Gold up, 1st to 4th order:** US midterm outcome and a softer dollar lift gold (1st) -> collateral value per gram rises (2nd) -> Muthoot lends more per customer, AUM growth accelerates and LTV cushions widen (3rd) -> the stock re-rates and auction losses fall (4th); competition then responds by cutting yields, capping the gain.
- **Oil/geopolitics route:** Middle East escalation -> Brent up (95 now; 107 in late Sept) -> India CPI and RBI hike expectations up -> G-sec yields up (7.48% peak) -> funding spreads for NBFCs widen -> Muthoot's NCD cost rises and equity discount rate rises, while the same risk-off bids gold (partial hedge).
- **Gold down:** gold -10% -> loans written at peak LTV breach 75% -> auctions and fresh margin calls rise -> Stage III climbs from 3.87% -> credit cost and sentiment worsen; the rural/southern borrower base cuts new pledges -> AUM growth slows.
- **Policy route:** RBI sees EMI-structured gold loans fuelling NPAs -> tenor/valuation rules tightened -> growth slows for all gold lenders, but Muthoot (scale, compliance) loses less than smaller NBFCs, a relative positive.

## Current situation
Q2 FY27: standalone PAT Rs2,977cr (+27%), consolidated Rs3,278cr (+36%), NII +34%, AUM +42% (FE). Cost lines are rising: interest Rs3,365cr and opex Rs1,459cr in the quarter. Stage III 3.87%. The stock rebounded ~9% from its 52-week low after results. A new MD took charge from September, and the Muthoot Money merger has completed.

## Upcoming
Q3 results ~Feb 2027; December MPC; gold price path; RBI tone on gold-loan structures; possible regulatory consultation.

## Bull and bear
Bull: gold stabilises, Stage III peaks, yields hold, P/E 10x re-rates. Bear: gold falls another 10%+, NPAs accelerate, banks/new entrants force yield cuts, RBI tightens. Net: gold is the dominant lever; the model's confidence is medium because AUM growth composition (price versus volume) and the NPA trajectory are only visible through headlines and the pack.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.