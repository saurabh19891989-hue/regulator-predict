# TATACAP — Tata Capital Ltd.
*NIFTY_NEXT_50 · Financial Services · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -3.7%**, **12 months -6.7%** (rank 197 / 199 of 200 for 3m / 12m); beta 1.10
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +20.7%): 3 months 36%, 12 months 28%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -13.9% … P90 -3.3%; plausible 12m relative-return range incl. stock-specific noise: -38.1% … +18.8%
- Decomposition (12m): 0.5 × forward event exposure -11.2% (3m -6.8%; half assumed priced) + 0.5 × company-specific catalysts -1.2%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply -8.0% (beta-adjusted) vs a realised market-adjusted move of +9.7% — gap -17.8 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Credit cost / NPA cycle (higher = worse) (`F_ASSET_QUALITY_IN`) | +50 bp credit cost | -7.48 | -7.00 | -0.48 | -0.03 | +0.02 | — |
| RBI prudential tightening (risk weights, LCR, provisioning) (`P_RBI_PRUDENTIAL`) | +1 = tightening step | -5.02 | -3.50 | -1.91 | +0.24 | +0.14 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -4.44 | -3.00 | -1.48 | +0.05 | -0.02 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -4.35 | +0.00 | -2.95 | -1.43 | +0.02 | — |
| Indian corporate credit spreads (`F_CREDIT_SPREADS_IN`) | +50 bp spreads | -4.05 | -4.00 | -0.12 | +0.08 | -0.01 | — |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +3.62 | +0.00 | +1.76 | +1.21 | +0.65 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -3.25 | +0.00 | -1.12 | -1.38 | -0.75 | -1.1% |
| Unsecured retail & microfinance stress (higher = worse) (`F_UNSECURED_STRESS`) | +1 pp delinquencies | -3.22 | -2.50 | -0.72 | -0.04 | +0.04 | — |
| India 10-year G-sec yield (`F_GSEC_10Y_IN`) | +25 bp yield | -2.98 | -2.50 | -0.46 | -0.03 | +0.01 | — |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -2.66 | +0.00 | +0.00 | -1.79 | -0.87 | — |
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | +2.62 | +0.00 | +2.18 | +1.12 | -0.67 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +2.29 | +2.00 | +0.10 | +0.07 | +0.12 | — |
| Monsoon rainfall vs normal (`F_MONSOON`) | +10% above long-period average | +2.06 | +0.00 | +0.40 | +0.96 | +0.70 | — |
| Indian vehicle demand (`F_AUTO_DEMAND_IN`) | +10% volumes | +2.00 | +2.00 | +0.00 | +0.00 | +0.00 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -5.3% | -5.3% | -4.5 | -0.8 | +0.2 | -0.1 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -5.3% | -5.3% | +0.0 | -3.4 | -1.8 | -0.1 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -5.2% | -5.2% | -5.1 | -0.2 | +0.0 | +0.0 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -5.0% | -5.0% | -4.4 | -0.2 | -0.2 | -0.3 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +5.8% | +2.9% | +5.0 | +0.2 | +0.2 | +0.4 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -2.6% | -2.6% | +0.0 | -0.5 | -1.2 | -0.9 |
| RBI MPC Dec 2026 (~4 Dec): hikes repo another 25 bp to 5.75% (`EV_RBI_DEC26_HIKE25`) | scheduled | 0.42 | -5.3% | -2.2% | -4.5 | -0.8 | +0.2 | -0.1 |
| RBI expected-credit-loss (ECL) provisioning goes live as scheduled (FY28 start) (`EV_ECL_ROLLOUT_APR27`) | scheduled | 0.90 | -2.4% | -2.2% | -2.4 | -0.0 | +0.0 | +0.0 |
| CPI prints >=6.0% (RBI upper tolerance) in Oct-Jan data (releases 12 Nov - 12 Feb) (`EV_CPI_BREACH_6PCT`) | anticipated | 0.60 | -3.5% | -2.1% | -2.5 | -0.9 | -0.1 | -0.0 |
| Risk: USD/INR >98 and/or reserves < US$650bn (disorderly rupee, emergency RBI response) (`EV_RUPEE_BREAK_98_RESERVE_STRESS`) | risk_scenario | 0.18 | -11.3% | -2.0% | -9.7 | -2.0 | +0.4 | +0.0 |
| Banking system liquidity turns to sustained deficit by end-March 2027 (`EV_BANKING_LIQUIDITY_DEFICIT_MAR27`) | anticipated | 0.60 | -3.1% | -1.9% | -3.2 | +0.0 | +0.0 | +0.0 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -1.9% | -1.9% | +0.0 | -1.4 | -0.4 | -0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → TATACAP | +5.00% | +2.50% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → TATACAP | -3.00% | -1.26% |
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → TATACAP | -2.00% | -1.00% |
| 1 | EV_ECL_ROLLOUT_APR27 ⇒ P_RBI_PRUDENTIAL → TATACAP | -1.05% | -0.95% |
| 1 | EV_ECL_ROLLOUT_APR27 ⇒ F_ASSET_QUALITY_IN → TATACAP | -1.05% | -0.95% |
| 1 | EV_RBI_FEB27_HIKE25 ⇒ F_REPO_IN → TATACAP | -3.00% | -0.81% |
| 1 | EV_CPI_BREACH_6PCT ⇒ F_GSEC_10Y_IN → TATACAP | -1.25% | -0.75% |
| 1 | EV_CPI_BREACH_6PCT ⇒ F_REPO_IN → TATACAP | -1.20% | -0.72% |
| 1 | EV_BANKING_LIQUIDITY_DEFICIT_MAR27 ⇒ F_LIQUIDITY_IN → TATACAP | -1.20% | -0.72% |
| 1 | EV_BANKING_LIQUIDITY_DEFICIT_MAR27 ⇒ F_CREDIT_SPREADS_IN → TATACAP | -1.20% | -0.72% |
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_CREDIT_SPREADS_IN → TATACAP | -1.20% | -0.60% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_REPO_IN → TATACAP | -3.00% | -0.54% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → TATACAP | -3.00% | -0.54% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → TATACAP | -1.92% | -0.48% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_FPI_FLOWS → TATACAP | -1.92% | -0.48% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_GSEC_10Y_IN → TATACAP | +1.55 | director_override | -3.88% |
| 1 | F_FPI_FLOWS → TATACAP | -1.60 | events | -3.20% |
| 1 | F_REPO_IN → TATACAP | +1.00 | events | -3.00% |
| 1 | F_CREDIT_SPREADS_IN → TATACAP | +0.50 | events | -2.00% |
| 2 | F_GDP_IN → F_ASSET_QUALITY_IN → TATACAP | +0.50 | events | +1.12% |
| 1 | F_AUTO_DEMAND_IN → TATACAP | +0.50 | director_override | +1.00% |
| 1 | F_LIQUIDITY_IN → TATACAP | -0.90 | events | -0.72% |
| 2 | F_MONSOON → F_UNSECURED_STRESS → TATACAP | -1.56 | events | -0.62% |
| 2 | F_CPI_IN → F_UNSECURED_STRESS → TATACAP | +1.15 | events | -0.35% |
| 2 | F_GDP_IN → F_CREDIT_GROWTH_IN → TATACAP | +0.50 | events | +0.34% |
| 2 | F_RURAL_DEMAND → F_ASSET_QUALITY_IN → TATACAP | -0.25 | events | -0.28% |
| 2 | F_REPO_IN → F_ASSET_QUALITY_IN → TATACAP | +1.00 | events | -0.28% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-10-12 | One-year IPO anniversary: lock-in/anchor expiries passed; stock flat versus IPO | other | 1.00 | +0.0% | +0.00% |
| 2027-01 | Q3 FY27 results (inferred; Q2 on 2026-10-27): margin recovery test (management targets Q4) | results | 0.92 | +0.0% | +0.00% |
| 2027-03 | RBI final revolving-credit norms (draft Aug 2026; NBFCs seeking review) | regulatory | 0.55 | -1.5% | -0.83% |
| 2027-06 | Tata Sons listing/OFS decision: RBI rejected licence surrender 2026-09-12; sell-down in Tata Capital to meet public-shareholding norms possible (scenario) | corporate_action | 0.30 | -1.5% | -0.45% |

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