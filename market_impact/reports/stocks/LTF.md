# LTF — L&T Finance Ltd.
*MIDCAP_100 · Financial Services · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -2.3%**, **12 months -3.8%** (rank 159 / 147 of 200 for 3m / 12m); beta 1.55
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +26.6%): 3 months 43%, 12 months 38%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -7.7% … P90 +0.3%; plausible 12m relative-return range incl. stock-specific noise: -26.4% … +24.7%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +0.0 pp (model impact -4.1% beta-adjusted vs realised market-adjusted move -4.3%); forward event exposure -5.6% (3m -3.1%; half assumed priced); company-specific events +0.3%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Credit cost / NPA cycle (higher = worse) (`F_ASSET_QUALITY_IN`) | +50 bp credit cost | -5.96 | -5.50 | -0.48 | +0.00 | +0.02 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -5.36 | +0.00 | -3.18 | -2.22 | +0.05 | — |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +3.98 | +0.00 | +1.96 | +1.27 | +0.76 | — |
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | +3.94 | +3.00 | +0.98 | +0.42 | -0.46 | — |
| Indian corporate credit spreads (`F_CREDIT_SPREADS_IN`) | +50 bp spreads | -3.93 | -4.00 | +0.00 | +0.07 | +0.00 | — |
| Unsecured retail & microfinance stress (higher = worse) (`F_UNSECURED_STRESS`) | +1 pp delinquencies | -3.65 | -3.00 | -0.62 | -0.07 | +0.05 | — |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -3.43 | +0.00 | -0.24 | -1.90 | -1.29 | — |
| RBI prudential tightening (risk weights, LCR, provisioning) (`P_RBI_PRUDENTIAL`) | +1 = tightening step | -3.34 | -2.50 | -1.16 | +0.18 | +0.14 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -3.01 | +0.00 | -1.08 | -0.68 | -1.25 | — |
| Bank credit growth (`F_CREDIT_GROWTH_IN`) | +3 pp | -2.85 | +0.00 | -1.68 | -1.06 | -0.11 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -2.71 | -2.00 | -0.77 | +0.03 | +0.04 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -2.50 | -0.80 | -0.40 | -0.70 | -0.60 | -1.1% |
| Monsoon rainfall vs normal (`F_MONSOON`) | +10% above long-period average | +2.38 | +1.00 | +0.58 | +0.47 | +0.33 | — |
| India 10-year G-sec yield (`F_GSEC_10Y_IN`) | +25 bp yield | -1.88 | -1.50 | -0.40 | +0.00 | +0.02 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -9.8% | -9.8% | -4.5 | -1.1 | -2.5 | -1.9 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -6.7% | -6.7% | +0.0 | -3.9 | -2.7 | -0.0 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -4.1% | -4.1% | -3.3 | -0.3 | -0.1 | -0.3 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -3.5% | -3.5% | -3.2 | -0.3 | +0.1 | -0.1 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -3.2% | -3.2% | -3.3 | +0.0 | +0.1 | +0.0 |
| RBI expected-credit-loss (ECL) provisioning goes live as scheduled (FY28 start) (`EV_ECL_ROLLOUT_APR27`) | scheduled | 0.62 | -4.9% | -3.0% | -5.2 | +0.1 | +0.2 | +0.1 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -3.0% | -3.0% | -1.3 | -0.7 | -0.6 | -0.4 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -2.5% | -2.5% | +0.0 | -1.8 | -0.6 | -0.2 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +4.6% | +2.3% | +3.8 | +0.4 | +0.2 | +0.4 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.36 | -6.5% | -2.3% | -2.3 | -1.3 | -1.6 | -1.3 |
| Gold and silver slump from January 2026 peaks (silver -53%, gold -24%) (`EV_PRECIOUS_METALS_CRASH_2026`) | occurred | 1.00 | -2.1% | -2.1% | +0.0 | -1.6 | -0.3 | -0.1 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.58 | +3.6% | +2.1% | +1.4 | +0.7 | +0.9 | +0.7 |

## Strongest causal chains (1st–4th order)
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → LTF | -4.46% | -4.46% |
| 1 | EV_FPI_RECORD_OUTFLOW_26 ⇒ F_FPI_FLOWS → LTF | -3.30% | -3.30% |
| 2 | EV_CPI_REACCEL_SEP26 ⇒ F_CPI_IN → F_REPO_IN → LTF | -2.65% | -2.65% |
| 1 | EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26 ⇒ F_GSEC_10Y_IN → LTF | -2.10% | -2.10% |
| 1 | EV_RBI_OCT26_HIKE25 ⇒ F_REPO_IN → LTF | -2.00% | -2.00% |
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → LTF | +3.75% | +1.88% |
| 1 | EV_ECL_ROLLOUT_APR27 ⇒ F_ASSET_QUALITY_IN → LTF | -2.75% | -1.71% |
| 1 | EV_ECL_ROLLOUT_APR27 ⇒ P_RBI_PRUDENTIAL → LTF | -2.50% | -1.55% |
| 1 | EV_SWMONSOON26_DEFICIT ⇒ F_MONSOON → LTF | -1.26% | -1.26% |
| 1 | EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26 ⇒ F_CREDIT_SPREADS_IN → LTF | -1.20% | -1.20% |
| 1 | EV_STEEL_RALLY_2026 ⇒ F_STEEL_GLOBAL → LTF | +1.03% | +1.03% |
| 1 | EV_RURAL_DEMAND_SOFT26 ⇒ F_RURAL_DEMAND → LTF | -0.90% | -0.90% |
| 3 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_CPI_IN → F_REPO_IN → LTF | -0.89% | -0.89% |
| 2 | EV_GDP_Q1FY27_7_8 ⇒ F_GDP_IN → F_ASSET_QUALITY_IN → LTF | +0.88% | +0.88% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → LTF | -2.25% | -0.80% |

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