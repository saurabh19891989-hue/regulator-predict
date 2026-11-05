# MUTHOOTFIN — Muthoot Finance Ltd.
*NIFTY_NEXT_50 · Financial Services · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -0.5%**, **12 months -2.3%** (rank 156 / 193 of 200 for 3m / 12m); beta 1.04
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +28.6%): 3 months 49%, 12 months 47%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -7.8% … P90 +1.9%; plausible 12m relative-return range incl. stock-specific noise: -36.0% … +31.2%
- Decomposition (12m): 0.5 × forward event exposure -2.8% (3m -0.6%; half assumed priced; market-priced macro drift removed) + 0.5 × company-specific catalysts -1.6%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply -6.5% (beta-adjusted) vs a realised market-adjusted move of -17.2% — gap +10.7 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## Where the expected return comes from
Market-priced macro drivers (rates, FX, commodities, indices, volatility, flows, growth, inflation) are taken as priced, so what is left is policy, regulatory, sector, theme, geopolitical and company-specific exposure — where 2nd–4th-order effects are most likely to be missed. Percentage points of the expected relative return.
| source | 12m: 1st order | 12m: 2nd–4th order | 12m total | 3m total |
|---|---|---|---|---|
| Policy | +0.00 | +0.12 | +0.12 | +0.05 |
| Regulatory | -0.68 | -0.07 | -0.76 | -0.05 |
| Sector | -0.24 | +0.14 | -0.10 | +0.04 |
| Theme | +0.00 | +0.02 | +0.02 | +0.02 |
| Geopolitics | +0.00 | -0.10 | -0.10 | -0.09 |
| Company catalysts | -0.78 | +0.00 | -0.78 | -0.11 |
| Market-priced macro | +0.00 | +0.00 | +0.00 | -0.00 |
| Beta adjustment | — | — | -0.60 | -0.27 |
| Universe centring | — | — | -0.15 | -0.10 |
| **Expected relative return** | | | **-2.34** | **-0.51** |

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Gold-loan competitive intensity (bank/NBFC entry, yield compression) (`NEW_GOLD_LOAN_COMPETITION`) | +1 = ~100bp industry gold-loan yield compression or ~3pp share shift to banks/new entrants | -7.00 | -7.00 | +0.00 | +0.00 | +0.00 | — |
| RBI prudential tightening (risk weights, LCR, provisioning) (`P_RBI_PRUDENTIAL`) | +1 = tightening step | -4.78 | -4.00 | -0.88 | +0.01 | +0.09 | — |
| Credit cost / NPA cycle (higher = worse) (`F_ASSET_QUALITY_IN`) | +50 bp credit cost | -3.79 | -3.50 | -0.30 | +0.00 | +0.01 | — |
| Gold price (`F_GOLD`) | +8% gold (USD) | +3.47 | +3.50 | +0.00 | -0.03 | -0.00 | -8.4% |
| Indian corporate credit spreads (`F_CREDIT_SPREADS_IN`) | +50 bp spreads | -2.44 | -2.50 | +0.00 | +0.05 | +0.01 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +2.10 | +2.00 | +0.07 | +0.01 | +0.02 | — |
| US dollar index (`F_DXY`) | +3% DXY | -2.00 | +0.00 | -1.94 | -0.07 | +0.00 | +2.2% |
| US 10-year Treasury yield (`F_US_10Y`) | +25 bp yield | -1.91 | +0.00 | -1.50 | -0.38 | -0.04 | +9.4% |
| Formalisation of the economy (`T_FORMALISATION`) | +1 | +1.91 | +2.00 | +0.00 | -0.06 | -0.04 | — |
| Bank credit growth (`F_CREDIT_GROWTH_IN`) | +3 pp | -1.87 | +0.00 | -1.26 | -0.58 | -0.03 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -1.85 | -1.50 | -0.44 | +0.05 | +0.04 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -1.70 | +0.00 | -1.16 | -0.61 | +0.07 | — |
| Gold import duty (`P_GOLD_IMPORT_DUTY`) | +5 pp | +1.51 | +1.50 | +0.00 | +0.00 | +0.01 | — |
| India 10-year G-sec yield (`F_GSEC_10Y_IN`) | +25 bp yield | -1.25 | -1.00 | -0.25 | +0.00 | +0.00 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -4.6% | -4.6% | -4.4 | -0.1 | -0.0 | -0.0 |
| Gold and silver slump from January 2026 peaks (silver -53%, gold -24%) (`EV_PRECIOUS_METALS_CRASH_2026`) | occurred | 1.00 | -3.6% | -3.6% | -3.7 | +0.0 | +0.0 | +0.0 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +5.2% | +2.6% | +5.0 | +0.1 | +0.1 | +0.0 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -2.4% | -2.4% | +0.0 | -2.4 | -0.1 | +0.1 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -2.4% | -2.4% | +0.0 | -2.2 | -0.2 | -0.0 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -2.3% | -2.3% | -2.3 | -0.1 | +0.1 | -0.0 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -2.1% | -2.1% | -2.1 | +0.0 | +0.1 | +0.0 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -2.0% | -2.0% | +0.0 | -1.3 | -0.7 | +0.0 |
| Gold falls to ~$3,500 / silver to ~$40 on Fed hike(s) and strong dollar (`EV_PRECIOUS_METALS_FURTHER_SLIDE`) | risk_scenario | 0.30 | -6.6% | -2.0% | -6.7 | +0.0 | +0.1 | +0.0 |
| RBI expected-credit-loss (ECL) provisioning goes live as scheduled (FY28 start) (`EV_ECL_ROLLOUT_APR27`) | scheduled | 0.90 | -1.8% | -1.6% | -1.7 | -0.1 | +0.0 | +0.0 |
| Gold/silver rebound as Fed hike fears fade or Iran war ends (`EV_PRECIOUS_METALS_REBOUND_H1_2027`) | anticipated | 0.45 | +3.5% | +1.6% | +3.5 | +0.0 | -0.0 | -0.0 |
| US midterms (3 Nov 2026): Democrats win House and Senate (`EV_US_MIDTERMS_DEM_SWEEP`) | occurred | 1.00 | +1.3% | +1.3% | +1.0 | +0.3 | +0.1 | +0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → MUTHOOTFIN | +5.00% | +2.50% |
| 1 | EV_PRECIOUS_METALS_FURTHER_SLIDE ⇒ F_GOLD → MUTHOOTFIN | -6.65% | -2.00% |
| 1 | EV_PRECIOUS_METALS_REBOUND_H1_2027 ⇒ F_GOLD → MUTHOOTFIN | +3.50% | +1.58% |
| 1 | EV_ECL_ROLLOUT_APR27 ⇒ P_RBI_PRUDENTIAL → MUTHOOTFIN | -1.20% | -1.08% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → MUTHOOTFIN | -1.50% | -0.63% |
| 2 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ C_MIDEAST_CONFLICT → F_GOLD → MUTHOOTFIN | -1.12% | -0.62% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → MUTHOOTFIN | -3.00% | -0.54% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → MUTHOOTFIN | -1.92% | -0.48% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_FPI_FLOWS → MUTHOOTFIN | -1.92% | -0.48% |
| 1 | EV_RBI_GOLD_LOAN_TIGHTEN ⇒ P_RBI_PRUDENTIAL → MUTHOOTFIN | -1.60% | -0.48% |
| 1 | EV_ECL_ROLLOUT_APR27 ⇒ F_ASSET_QUALITY_IN → MUTHOOTFIN | -0.53% | -0.47% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → MUTHOOTFIN | -1.87% | -0.47% |
| 1 | EV_BANKING_LIQUIDITY_DEFICIT_MAR27 ⇒ F_CREDIT_SPREADS_IN → MUTHOOTFIN | -0.75% | -0.45% |
| 1 | EV_RBI_FEB27_HIKE25 ⇒ F_REPO_IN → MUTHOOTFIN | -1.50% | -0.41% |
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → MUTHOOTFIN | -0.80% | -0.40% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_GOLD → MUTHOOTFIN | -1.05 | observed | -3.67% |
| 1 | F_FPI_FLOWS → MUTHOOTFIN | -1.60 | events | -3.20% |
| 1 | F_GSEC_10Y_IN → MUTHOOTFIN | +1.55 | director_override | -1.55% |
| 1 | F_REPO_IN → MUTHOOTFIN | +1.00 | events | -1.50% |
| 1 | F_CREDIT_SPREADS_IN → MUTHOOTFIN | +0.50 | events | -1.25% |
| 1 | T_FORMALISATION → MUTHOOTFIN | +0.30 | events | +0.60% |
| 2 | F_GDP_IN → F_ASSET_QUALITY_IN → MUTHOOTFIN | +0.50 | events | +0.56% |
| 2 | F_GDP_IN → P_RBI_PRUDENTIAL → MUTHOOTFIN | +0.50 | events | -0.32% |
| 3 | F_GDP_IN → F_CREDIT_GROWTH_IN → P_RBI_PRUDENTIAL → MUTHOOTFIN | +0.50 | events | -0.15% |
| 2 | F_RURAL_DEMAND → F_ASSET_QUALITY_IN → MUTHOOTFIN | -0.25 | events | -0.14% |
| 2 | F_REPO_IN → F_ASSET_QUALITY_IN → MUTHOOTFIN | +1.00 | events | -0.14% |
| 3 | F_MONSOON → F_UNSECURED_STRESS → F_ASSET_QUALITY_IN → MUTHOOTFIN | -1.56 | events | -0.13% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-11 | Management transition: Alexander George as MD (appointed 2026-09-02) settles in; any strategy reset on growth vs asset quality | corporate_action | 0.50 | +0.5% | +0.25% |
| 2027-02 | Q3 FY27 results (date inferred from Q2 on 2026-10-31); key read: Stage III trend, NIM, AUM growth vs +42% | results | 0.92 | -0.5% | -0.46% |
| 2027-03 | RBI or industry action on gold-loan tenor/EMI structure and valuation practices following rising NPAs (scenario, no announced proposal found) *(review: [RT_N50_B] RT_N50_B: Keep as the gold-lender-specific part of EV_RBI_GOLD_LOAN_TIGHTEN (generic P_RBI_PRUDENTIAL shock cut to 0.4 in event_overrides). Probability aligned with the event (0.3).)* | regulatory | 0.30 | -4.5% | -1.35% |

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