# TATACAP — Tata Capital Ltd.
*NIFTY_NEXT_50 · Financial Services · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -9.1%**, **12 months -17.0%** (rank 199 / 199 of 200 for 3m / 12m); beta 1.10
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +20.7%): 3 months 19%, 12 months 28%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -32.7% … P90 -11.5%; plausible 12m relative-return range incl. stock-specific noise: -41.1% … +6.8%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves -5.2 pp (model impact -10.5% beta-adjusted vs realised market-adjusted move +9.7%); forward event exposure -20.0% (3m -10.4%; half assumed priced); company-specific events -1.2%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| India CPI inflation (`F_CPI_IN`) | +1 pp | -9.27 | +0.00 | -4.68 | -4.39 | -0.21 | — |
| Credit cost / NPA cycle (higher = worse) (`F_ASSET_QUALITY_IN`) | +50 bp credit cost | -7.48 | -7.00 | -0.48 | -0.03 | +0.02 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -6.54 | +0.00 | -1.76 | -2.77 | -2.01 | -1.1% |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -5.25 | +0.00 | +0.00 | -2.74 | -2.51 | — |
| RBI prudential tightening (risk weights, LCR, provisioning) (`P_RBI_PRUDENTIAL`) | +1 = tightening step | -5.02 | -3.50 | -1.91 | +0.24 | +0.14 | — |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +4.86 | +0.00 | +1.76 | +1.67 | +1.43 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -4.45 | -3.00 | -1.48 | +0.03 | -0.00 | — |
| Indian corporate credit spreads (`F_CREDIT_SPREADS_IN`) | +50 bp spreads | -4.05 | -4.00 | -0.12 | +0.08 | -0.01 | — |
| Unsecured retail & microfinance stress (higher = worse) (`F_UNSECURED_STRESS`) | +1 pp delinquencies | -3.22 | -2.50 | -0.72 | -0.04 | +0.04 | — |
| India 10-year G-sec yield (`F_GSEC_10Y_IN`) | +25 bp yield | -3.11 | -2.50 | -0.58 | -0.05 | +0.02 | — |
| Brent crude oil price (`F_BRENT`) | +10% Brent | -2.90 | +0.00 | -0.24 | -1.45 | -1.22 | +0.0% |
| India FX reserves (RBI intervention) (`NEW_FX_RESERVES_IN`) | +US$25bn reserves (RBI buys / net inflows) | +2.68 | +0.00 | +0.93 | +1.39 | +0.36 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -2.51 | +0.00 | +0.00 | -0.49 | -2.01 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +2.46 | +2.00 | +0.10 | +0.14 | +0.22 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -15.3% | -15.3% | +0.0 | -1.2 | -7.5 | -6.6 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -10.9% | -10.9% | +0.0 | -5.4 | -5.2 | -0.3 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -5.6% | -5.6% | -4.4 | -0.2 | -0.4 | -0.6 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -5.4% | -5.4% | -5.1 | -0.3 | -0.0 | +0.0 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -5.3% | -5.3% | -4.5 | -0.9 | +0.2 | -0.1 |
| RBI expected-credit-loss (ECL) provisioning goes live as scheduled (FY28 start) (`EV_ECL_ROLLOUT_APR27`) | scheduled | 0.62 | -8.0% | -5.0% | -8.0 | -0.2 | +0.1 | +0.0 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -3.7% | -3.7% | +0.0 | -2.4 | -0.8 | -0.5 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.36 | -9.8% | -3.5% | +0.0 | -1.5 | -4.3 | -4.0 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.58 | +5.5% | +3.2% | +0.0 | +0.7 | +2.5 | +2.3 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +6.3% | +3.2% | +5.0 | +0.2 | +0.4 | +0.7 |
| Gold and silver slump from January 2026 peaks (silver -53%, gold -24%) (`EV_PRECIOUS_METALS_CRASH_2026`) | occurred | 1.00 | -3.0% | -3.0% | +0.0 | -2.2 | -0.5 | -0.4 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -2.8% | -2.8% | +0.0 | -0.5 | -1.3 | -0.9 |

## Strongest causal chains (1st–4th order)
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_RECORD_OUTFLOW_26 ⇒ F_FPI_FLOWS → TATACAP | -4.40% | -4.40% |
| 2 | EV_CPI_REACCEL_SEP26 ⇒ F_CPI_IN → F_REPO_IN → TATACAP | -3.97% | -3.97% |
| 1 | EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26 ⇒ F_GSEC_10Y_IN → TATACAP | -3.50% | -3.50% |
| 1 | EV_RBI_OCT26_HIKE25 ⇒ F_REPO_IN → TATACAP | -3.00% | -3.00% |
| 3 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_CPI_IN → F_REPO_IN → TATACAP | -2.66% | -2.66% |
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → TATACAP | +5.00% | +2.50% |
| 1 | EV_ECL_ROLLOUT_APR27 ⇒ P_RBI_PRUDENTIAL → TATACAP | -3.50% | -2.17% |
| 1 | EV_ECL_ROLLOUT_APR27 ⇒ F_ASSET_QUALITY_IN → TATACAP | -3.50% | -2.17% |
| 3 | EV_CPI_REACCEL_SEP26 ⇒ F_CPI_IN → F_REPO_IN → F_GSEC_10Y_IN → TATACAP | -1.31% | -1.31% |
| 3 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_GDP_IN → F_ASSET_QUALITY_IN → TATACAP | -1.25% | -1.25% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → TATACAP | -3.00% | -1.20% |
| 1 | EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26 ⇒ F_CREDIT_SPREADS_IN → TATACAP | -1.20% | -1.20% |
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_FPI_FLOWS → TATACAP | -1.19% | -1.19% |
| 2 | EV_GDP_Q1FY27_7_8 ⇒ F_GDP_IN → F_ASSET_QUALITY_IN → TATACAP | +1.12% | +1.12% |
| 2 | EV_UST_SELLOFF_SEP26 ⇒ F_US_10Y → F_GSEC_10Y_IN → TATACAP | -1.10% | -1.10% |

## Analyst profile (agent research, sourced)
# TATACAP - Tata Capital Ltd. (Nifty Next 50, I_NBFC_VEHICLE_CONSUMER) - as of 2026-11-05

## Business
Tata Capital is the financial-services arm of Tata Sons, which owns 85.41%. It listed in October 2025 at Rs326 and has since traded flat. With a loan book above Rs3 trillion it lends across consumer (personal loans, two-wheelers, cars, credit lines), commercial vehicles and equipment, housing and loan-against-property, SME and corporate, and has a wealth and distribution business. Borrowings of about Rs2.4 lakh cr (model estimate from Q2 interest of Rs4,680cr) are funded by banks, NCDs and CP. The Q2 FY27 result was strong on growth (AUM +26%, profit +51% according to Business Standard) but margin is under pressure from funding costs until the Q4 recovery that management guides.

## What moves the stock, ranked
1. **Credit cost (w -7 per +50bp) and unsecured stress (w -2.5).** The book is diversified and mostly secured, but unsecured lines are the growth engine. Asset quality "held" in Q2.
2. **Funding costs: repo (-3.0), spreads (-4.0), G-sec (-2.5).** The 2026-10-07 hike to 5.50% and wider NBFC spreads hit margin before assets reprice; Mint (2026-09-22) already asked whether Tata Capital can protect margins. Management expects margin recovery from Q4.
3. **Regulation (P_RBI_PRUDENTIAL -3.5).** RBI's revolving-credit curbs (draft August 2026) affect 3-4% of AUM; alternate products are being tested. The group also faces the RBI order for Tata Sons to list (2026-09-12).
4. **Demand: credit growth +2.0, autos +2.0, housing +1.5.** Auto demand matters through commercial and passenger vehicle finance.
5. **Group and flows: TCS group_contagion +0.1, FPI +2.0.** Tata Sons' governance and listing questions have swung Tata stocks by up to 20% (2026-09-15).

## Transmission examples
- **Rates -> margin -> multiple:** Brent at 95 keeps CPI high -> RBI signals further hikes -> bank lending rates and AAA NBFC spreads rise -> Tata Capital's floating-rate borrowings reprice within one quarter while retail assets reprice slowly -> NIM compresses (as Q2 showed) -> EPS growth and the 24.5x multiple fall; if oil eases (it fell after US midterms) yields compress and the Q4 recovery arrives early.
- **Auto cycle:** GST and festive demand lift vehicle sales -> more CV and car disbursements -> AUM growth stays above 25% -> operating leverage; weak monsoon or fuel prices reverse it.
- **Regulatory chain:** RBI sees revolving credit as a risk -> credit-line products restricted -> 3-4% of AUM migrates to term loans -> yield and fee income slip -> sentiment hit on all consumer NBFCs, including BAJFINANCE.
- **Group chain:** Tata Sons listing/OFS plan -> expectations of supply of Tata Capital shares (promoter 85% must fall toward 75%) -> overhang on the stock; conversely a listing of Tata Sons could crystallise group value.

## Current situation
Q2 profit +51% with AUM +26%; shares +5% on results; Citi has a Buy with a Rs450 target. FIIs hold 5.1%. A discrepancy exists between screener (Rs1,832cr net profit) and press (Rs1,660cr), which is probably a definition difference and is unresolved.

## Upcoming
Q3 results (Jan 2027), final revolving-credit norms, December MPC, Tata Sons listing/OFS developments, margin recovery in Q4.

## Bull and bear
Bull: margins recover as guided, growth stays above 25%, credit cost stays low, overhang from Tata Sons clears. Bear: further rate hikes and spreads delay recovery, RBI tightens unsecured lending, a promoter OFS adds supply. Confidence medium; margin and book-composition numbers are model estimates.

## Notes on evidence quality
The Q2 growth rates, the 3-4% revolving-credit impact, the RBI order on Tata Sons, the Citi initiation and the margin-recovery guidance come from dated news headlines (URLs in the JSON). The segment mix, floating share of borrowings and unsecured share are model estimates. The pack has no empirical sensitivity table for TATACAP because the listing is under a year old, so none of the weights is checked against price data; confidence is therefore medium at best and several edges are labelled low.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.