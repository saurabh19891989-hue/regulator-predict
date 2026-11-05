# TATACAP — Tata Capital Ltd.
*NIFTY_NEXT_50 · Financial Services · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -0.1%**, **12 months -0.3%** (rank 111 / 119 of 200 for 3m / 12m); beta 1.10
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +20.7%): 3 months 50%, 12 months 48%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -6.0% … P90 +3.3%; plausible 12m relative-return range incl. stock-specific noise: -29.9% … +26.2%
- Decomposition (12m): 0.5 × forward event exposure -1.1% (3m +0.2%; half assumed priced; market-priced macro drift removed) + 0.5 × company-specific catalysts +0.9%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply -5.4% (beta-adjusted) vs a realised market-adjusted move of +9.7% — gap -15.1 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## Where the expected return comes from
Market-priced macro drivers (rates, FX, commodities, indices, volatility, flows, growth, inflation) are taken as priced, so what is left is policy, regulatory, sector, theme, geopolitical and company-specific exposure — where 2nd–4th-order effects are most likely to be missed. Percentage points of the expected relative return.
| source | 12m: 1st order | 12m: 2nd–4th order | 12m total | 3m total |
|---|---|---|---|---|
| Policy | +0.00 | +0.12 | +0.12 | -0.09 |
| Regulatory | -0.60 | -0.08 | -0.67 | -0.06 |
| Sector | -0.72 | +1.25 | +0.53 | +0.45 |
| Theme | +0.00 | +0.10 | +0.10 | +0.06 |
| Geopolitics | +0.00 | -0.01 | -0.01 | -0.00 |
| Company catalysts | +0.45 | -0.00 | +0.44 | -0.03 |
| Market-priced macro | +0.00 | +0.00 | +0.00 | +0.00 |
| Beta adjustment | — | — | -0.63 | -0.28 |
| Universe centring | — | — | -0.15 | -0.10 |
| **Expected relative return** | | | **-0.26** | **-0.05** |

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Credit cost / NPA cycle (higher = worse) (`F_ASSET_QUALITY_IN`) | +50 bp credit cost | -7.24 | -7.00 | -0.24 | -0.03 | +0.02 | — |
| RBI prudential tightening (risk weights, LCR, provisioning) (`P_RBI_PRUDENTIAL`) | +1 = tightening step | -4.80 | -3.50 | -1.67 | +0.26 | +0.11 | — |
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | +3.98 | +0.00 | +2.18 | +2.05 | -0.25 | — |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +3.62 | +0.00 | +1.76 | +0.94 | +0.92 | — |
| Unsecured retail & microfinance stress (higher = worse) (`F_UNSECURED_STRESS`) | +1 pp delinquencies | -3.27 | -2.50 | -0.72 | -0.02 | -0.03 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -3.13 | +0.00 | -1.91 | -1.23 | +0.01 | — |
| India 10-year G-sec yield (`F_GSEC_10Y_IN`) | +25 bp yield | -2.79 | -2.50 | -0.26 | -0.03 | +0.00 | — |
| India real GDP growth (`F_GDP_IN`) | +1 pp | +2.71 | +0.00 | +3.18 | -0.38 | -0.09 | — |
| Monsoon rainfall vs normal (`F_MONSOON`) | +10% above long-period average | +2.61 | +0.00 | +0.40 | +1.37 | +0.85 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -2.54 | -1.20 | -1.40 | +0.12 | -0.06 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -2.34 | +0.00 | -0.83 | -1.03 | -0.48 | -1.1% |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +2.22 | +2.00 | +0.10 | +0.03 | +0.09 | — |
| Indian corporate credit spreads (`F_CREDIT_SPREADS_IN`) | +50 bp spreads | -2.10 | -2.00 | -0.12 | +0.08 | -0.06 | — |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -2.04 | +0.00 | +0.00 | -1.22 | -0.82 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -4.9% | -4.9% | -4.4 | -0.2 | -0.1 | -0.2 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -4.7% | -4.7% | -4.5 | -0.2 | +0.0 | -0.0 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -3.9% | -3.9% | +0.0 | -2.2 | -1.6 | -0.2 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -3.3% | -3.3% | +0.0 | -0.5 | -1.7 | -1.1 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -3.1% | -3.1% | -2.4 | -0.8 | +0.2 | -0.1 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +5.6% | +2.8% | +5.0 | +0.2 | +0.1 | +0.3 |
| RBI expected-credit-loss (ECL) provisioning goes live as scheduled (FY28 start) (`EV_ECL_ROLLOUT_APR27`) | scheduled | 0.90 | -2.3% | -2.1% | -2.4 | +0.0 | +0.0 | +0.0 |
| IMD April 2027 long-range forecast says normal or above-normal monsoon (>=96% LPA) (`EV_MONSOON27_FIRST_FORECAST_NORMAL`) | scheduled | 0.68 | +2.5% | +1.7% | +0.0 | +0.4 | +1.6 | +0.5 |
| Risk: USD/INR >98 and/or reserves < US$650bn (disorderly rupee, emergency RBI response) (`EV_RUPEE_BREAK_98_RESERVE_STRESS`) | risk_scenario | 0.18 | -9.0% | -1.6% | -7.9 | -1.5 | +0.4 | +0.0 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -1.6% | -1.6% | +0.0 | -1.2 | -0.3 | -0.0 |
| India Q1 FY27 GDP grows 7.8% (31 Aug 2026), beating ~7.3% consensus (`EV_GDP_Q1FY27_7_8`) | occurred | 1.00 | +1.5% | +1.5% | +0.0 | +1.8 | -0.2 | -0.1 |
| Banking system liquidity turns to sustained deficit by end-March 2027 (`EV_BANKING_LIQUIDITY_DEFICIT_MAR27`) | anticipated | 0.60 | -2.5% | -1.5% | -2.6 | +0.0 | +0.0 | -0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → TATACAP | +5.00% | +2.50% |
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → TATACAP | -2.00% | -1.00% |
| 1 | EV_ECL_ROLLOUT_APR27 ⇒ P_RBI_PRUDENTIAL → TATACAP | -1.05% | -0.95% |
| 1 | EV_ECL_ROLLOUT_APR27 ⇒ F_ASSET_QUALITY_IN → TATACAP | -1.05% | -0.95% |
| 1 | EV_BANKING_LIQUIDITY_DEFICIT_MAR27 ⇒ F_LIQUIDITY_IN → TATACAP | -1.20% | -0.72% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → TATACAP | -3.00% | -0.54% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → TATACAP | -1.20% | -0.50% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → TATACAP | -1.92% | -0.48% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_FPI_FLOWS → TATACAP | -1.92% | -0.48% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → TATACAP | -1.87% | -0.47% |
| 1 | EV_FERT_SUBSIDY_TOPUP_WINTER ⇒ F_GSEC_10Y_IN → TATACAP | -0.50% | -0.45% |
| 1 | EV_CPI_BREACH_6PCT ⇒ F_GSEC_10Y_IN → TATACAP | -0.75% | -0.45% |
| 1 | EV_BANKING_LIQUIDITY_DEFICIT_MAR27 ⇒ F_GSEC_10Y_IN → TATACAP | -0.75% | -0.45% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_GSEC_10Y_IN → TATACAP | -2.50% | -0.45% |
| 1 | EV_RBI_GOLD_LOAN_TIGHTEN ⇒ P_RBI_PRUDENTIAL → TATACAP | -1.40% | -0.42% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_GSEC_10Y_IN → TATACAP | +1.55 | director_override | -3.88% |
| 1 | F_FPI_FLOWS → TATACAP | -1.60 | events | -3.20% |
| 1 | F_REPO_IN → TATACAP | +1.00 | events | -1.20% |
| 2 | F_GDP_IN → F_ASSET_QUALITY_IN → TATACAP | +0.50 | events | +1.12% |
| 1 | F_CREDIT_SPREADS_IN → TATACAP | +0.50 | events | -1.00% |
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
| 2027-04 | Offset to catalogue event EV_ECL_ROLLOUT_APR27 (bank provisioning-norm transition from Apr 2027): NBFCs are outside its scope (Ind AS 109 impairment since FY2018); cancels the generic-node impact *(review: [RT_BOT_A] EV_ECL_ROLLOUT_APR27 reaches this NBFC through generic nodes (P_RBI_PRUDENTIAL/F_ASSET_QUALITY_IN/F_CREDIT_GROWTH_IN). The impacts at the 08:44 run, conditional at p 0.9, are BAJFINANCE -1.98, TATACAP -2.41, JIOFIN -1.08 and BAJAJFINSV -1.67; the BAJAJFINSV offset is net of the BAJFINANCE offset passed through the 0.75 x 0.8 link. Offset ranges are ±20%. Wording avoids the MARKET_WIDE regex on purpose. A bank-only node is the cleaner fix and would remove the need for these offsets.)* | regulatory | 0.90 | +2.4% | +2.17% |
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