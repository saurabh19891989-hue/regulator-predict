# LTF — L&T Finance Ltd.
*MIDCAP_100 · Financial Services · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -0.1%**, **12 months -0.6%** (rank 124 / 133 of 200 for 3m / 12m); beta 1.55
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +26.6%): 3 months 50%, 12 months 47%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -3.5% … P90 +2.8%; plausible 12m relative-return range incl. stock-specific noise: -34.2% … +34.4%
- Decomposition (12m): 0.5 × forward event exposure -1.1% (3m -0.1%; half assumed priced; market-priced macro drift removed) + 0.5 × company-specific catalysts +0.3%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply -3.7% (beta-adjusted) vs a realised market-adjusted move of -4.3% — gap +0.6 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## Where the expected return comes from
Market-priced macro drivers (rates, FX, commodities, indices, volatility, flows, growth, inflation) are taken as priced, so what is left is policy, regulatory, sector, theme, geopolitical and company-specific exposure — where 2nd–4th-order effects are most likely to be missed. Percentage points of the expected relative return.
| source | 12m: 1st order | 12m: 2nd–4th order | 12m total | 3m total |
|---|---|---|---|---|
| Policy | +0.00 | +0.06 | +0.06 | -0.08 |
| Regulatory | -0.43 | -0.09 | -0.52 | -0.05 |
| Sector | +0.18 | +0.57 | +0.76 | +0.43 |
| Theme | +0.00 | +0.04 | +0.04 | +0.03 |
| Geopolitics | +0.00 | -0.01 | -0.01 | +0.01 |
| Company catalysts | +0.15 | -0.00 | +0.15 | +0.06 |
| Market-priced macro | +0.00 | -0.00 | -0.00 | -0.00 |
| Beta adjustment | — | — | -0.89 | -0.40 |
| Universe centring | — | — | -0.15 | -0.10 |
| **Expected relative return** | | | **-0.55** | **-0.10** |

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Credit cost / NPA cycle (higher = worse) (`F_ASSET_QUALITY_IN`) | +50 bp credit cost | -5.96 | -5.50 | -0.48 | +0.00 | +0.02 | — |
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | +4.38 | +3.00 | +0.98 | +0.65 | -0.25 | — |
| Indian corporate credit spreads (`F_CREDIT_SPREADS_IN`) | +50 bp spreads | -3.96 | -4.00 | +0.00 | +0.07 | -0.02 | — |
| Unsecured retail & microfinance stress (higher = worse) (`F_UNSECURED_STRESS`) | +1 pp delinquencies | -3.67 | -3.00 | -0.62 | -0.07 | +0.02 | — |
| RBI prudential tightening (risk weights, LCR, provisioning) (`P_RBI_PRUDENTIAL`) | +1 = tightening step | -3.34 | -2.50 | -1.16 | +0.18 | +0.14 | — |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +3.22 | +0.00 | +1.96 | +0.82 | +0.45 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -2.74 | -2.00 | -0.77 | +0.03 | +0.01 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -2.70 | +0.00 | -2.03 | -0.74 | +0.07 | — |
| Monsoon rainfall vs normal (`F_MONSOON`) | +10% above long-period average | +2.49 | +1.00 | +0.58 | +0.57 | +0.34 | — |
| Bank credit growth (`F_CREDIT_GROWTH_IN`) | +3 pp | -2.37 | +0.00 | -1.68 | -0.69 | +0.00 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -2.00 | +0.00 | -1.08 | -0.39 | -0.53 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -1.92 | -0.80 | -0.40 | -0.25 | -0.46 | -1.1% |
| India 10-year G-sec yield (`F_GSEC_10Y_IN`) | +25 bp yield | -1.90 | -1.50 | -0.40 | +0.00 | +0.00 | — |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -1.88 | +0.00 | -0.24 | -1.19 | -0.45 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -3.8% | -3.8% | -3.3 | -0.3 | -0.1 | -0.1 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -3.5% | -3.5% | +0.0 | -2.6 | -0.9 | +0.0 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -3.5% | -3.5% | -3.2 | -0.3 | +0.1 | -0.1 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -3.2% | -3.2% | -3.3 | +0.0 | +0.1 | +0.0 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -3.1% | -3.1% | -1.3 | -0.7 | -0.7 | -0.4 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +4.4% | +2.2% | +3.8 | +0.4 | +0.2 | +0.1 |
| IMD April 2027 long-range forecast says normal or above-normal monsoon (>=96% LPA) (`EV_MONSOON27_FIRST_FORECAST_NORMAL`) | scheduled | 0.68 | +2.6% | +1.7% | +1.0 | +0.6 | +0.8 | +0.2 |
| Risk: USD/INR >98 and/or reserves < US$650bn (disorderly rupee, emergency RBI response) (`EV_RUPEE_BREAK_98_RESERVE_STRESS`) | risk_scenario | 0.18 | -8.2% | -1.5% | -6.8 | -1.8 | +0.3 | +0.1 |
| RBI MPC Dec 2026 (~4 Dec): hikes repo another 25 bp to 5.75% (`EV_RBI_DEC26_HIKE25`) | scheduled | 0.42 | -3.5% | -1.5% | -3.2 | -0.3 | +0.1 | -0.1 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.55 | +2.5% | +1.4% | +1.2 | +0.5 | +0.6 | +0.2 |
| RBI expected-credit-loss (ECL) provisioning goes live as scheduled (FY28 start) (`EV_ECL_ROLLOUT_APR27`) | scheduled | 0.90 | -1.5% | -1.3% | -1.6 | +0.0 | +0.1 | +0.0 |
| Rural demand indicators mixed: tractor volumes dip in Oct, 2W festive sales firm, rural CPI above urban, rural jobs scheme person-days down (`EV_RURAL_DEMAND_SOFT26`) | occurred | 1.00 | -1.3% | -1.3% | -0.9 | -0.3 | -0.2 | +0.1 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → LTF | +3.75% | +1.88% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → LTF | -2.00% | -0.84% |
| 1 | EV_ECL_ROLLOUT_APR27 ⇒ F_ASSET_QUALITY_IN → LTF | -0.82% | -0.74% |
| 1 | EV_BANKING_LIQUIDITY_DEFICIT_MAR27 ⇒ F_CREDIT_SPREADS_IN → LTF | -1.20% | -0.72% |
| 1 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → LTF | +1.00% | +0.68% |
| 1 | EV_ECL_ROLLOUT_APR27 ⇒ P_RBI_PRUDENTIAL → LTF | -0.75% | -0.68% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → LTF | +1.17% | +0.64% |
| 1 | EV_BUDGET27_AGRI_RURAL ⇒ F_RURAL_DEMAND → LTF | +0.90% | +0.63% |
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → LTF | -1.20% | -0.60% |
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_CREDIT_SPREADS_IN → LTF | -1.20% | -0.60% |
| 1 | EV_RBI_FEB27_HIKE25 ⇒ F_REPO_IN → LTF | -2.00% | -0.54% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → LTF | -1.98% | -0.50% |
| 1 | EV_RURAL_RELIEF_PACKAGE ⇒ F_RURAL_DEMAND → LTF | +0.90% | +0.49% |
| 1 | EV_NEMONSOON26_NORMAL_UP ⇒ F_MONSOON → LTF | +0.50% | +0.42% |
| 1 | EV_STATE_POLLS_FEB_MAR27 ⇒ F_RURAL_DEMAND → LTF | +0.60% | +0.41% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_FPI_FLOWS → LTF | -1.60 | events | -2.40% |
| 1 | F_GSEC_10Y_IN → LTF | +1.55 | director_override | -2.33% |
| 1 | F_REPO_IN → LTF | +1.00 | events | -2.00% |
| 1 | F_CREDIT_SPREADS_IN → LTF | +0.50 | events | -2.00% |
| 1 | F_MONSOON → LTF | -1.56 | events | -1.56% |
| 1 | F_AUTO_DEMAND_IN → LTF | +0.50 | director_override | +0.90% |
| 2 | F_GDP_IN → F_ASSET_QUALITY_IN → LTF | +0.50 | events | +0.88% |
| 1 | F_RURAL_DEMAND → LTF | -0.25 | events | -0.75% |
| 2 | F_CPI_IN → F_UNSECURED_STRESS → LTF | +1.15 | events | -0.41% |
| 2 | F_MONSOON → F_UNSECURED_STRESS → LTF | -1.56 | events | -0.37% |
| 1 | F_USDINR → LTF | -0.37 | observed | +0.30% |
| 1 | F_STEEL_GLOBAL → LTF | +0.50 | director_override | +0.25% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-11 | Further NCD/sub-debt raising (Rs 1,000 cr NCDs allotted 4 Nov; sub-bond bids 9 Oct) to fund 25%+ book growth | other | 0.90 | +0.0% | +0.00% |
| 2027-01 | Q3 FY27 results (Q2 was 15 Oct 2026) | results | 0.95 | +0.0% | +0.00% |
| 2027-03 | FY27 close: Lakshya 2026 targets (RoA >2.8%, RoE >16%) delivery check | guidance | 0.60 | +0.5% | +0.30% |

## Analyst profile (agent research, sourced)
# LTF - L&T Finance (midcap, retail NBFC)

## Business
L&T Finance is an L&T Group retail lender (L&T holds ~65.9%) that has repositioned from infrastructure to retail under 'Lakshya 2026'. The book is about Rs 1.35 lakh cr (+29% y/y at Q2 FY27) spanning rural business finance (two-wheelers, farm equipment, microfinance), personal and consumer loans, home loans and LAP, and SME. Revenue Rs 20.0k cr TTM; PAT Rs 3.4k cr TTM, Q2 FY27 PAT ~Rs 973 cr (+33%). Funding mix: bank loans, NCDs, sub-debt and CP, with modest deposit base (model knowledge).

## What moves the stock (ranked)
1. **Credit spreads and cost of funds** - interest expense is 37% of revenue; ET BFSI warned on 3 Oct that EPS cuts could reach 12% across NBFCs. The 7 Oct repo hike to 5.50% and wider NCD spreads extend the squeeze.
2. **Asset quality in rural/unsecured** - a +50bp credit cost shock is about -5.5% equity; MFI/personal loans are the amplifiers.
3. **Rural demand/monsoon/auto volumes** - drive disbursements and collections.
4. **Regulatory risk** - RBI action on unsecured/MFI and risk weights.
5. **Flows** - beta 1.8-2.0; FIIs 7.4%, DIIs 15.8%.

## Transmission examples
- **Middle East escalation -> Brent at ~$95 (+49.5% 12m) -> diesel and CNG cost for 3W/CV/farm users -> rural cash flow squeeze -> MFI and 2W delinquencies up -> LTF credit cost rises -> margin and growth cut; simultaneous 2nd-order: INR weaker -> CPI up -> RBI hike (done 7 Oct) -> bank-loan funding costs reset up; 3rd-order: NBFC spreads widen -> NCD issuance gets pricier.**
- **Weak monsoon -> food inflation -> rural income down -> tractor and 2W demand falls -> LTF disbursements and collections weaken; RBI then can't cut because of food CPI -> funding cost stays high (4th order).**
- **US 10y 4.89% -> FPI outflow -> high-beta NBFC underperforms -> equity-raising ability dims.**

## Current situation
Record Q2 profit, retail book +29% and AI-linked cost efficiency, but the stock fell up to 6% on results and -11.9% over three months as margin/funding concerns dominated. Analysts remain constructive (Motilal Oswal target Rs 330; UBS/Nomura positive earlier). It raised Rs 1,000 cr NCDs on 4 Nov and subordinated bonds on 9 Oct.

## Upcoming
Q3 FY27 mid-January 2027; RBI MPC in December; monitoring of funding spreads.

## Bull / bear
Bull: RoA reaches 2.8%+, cost efficiencies hold, credit cost normal, re-rate toward 3x book. Bear: funding squeeze, rural stress, regulation, and multiple compression from 2.4x book.

Uncertainty: asset-mix shares and borrowing mix are model knowledge; the empirical steel (+2.0, t 2.3) and USD/INR (+3.5, t 2.3) sensitivities were judged coincidental and shrunk.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.