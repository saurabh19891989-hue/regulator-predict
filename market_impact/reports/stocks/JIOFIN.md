# JIOFIN — Jio Financial Services Ltd.
*NIFTY_50 · Financial Services · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -0.4%**, **12 months +0.1%** (rank 151 / 87 of 200 for 3m / 12m); beta 1.35
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +16.6%): 3 months 48%, 12 months 50%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -4.6% … P90 +3.2%; plausible 12m relative-return range incl. stock-specific noise: -21.9% … +22.4%
- Decomposition (12m): 0.5 × forward event exposure -2.6% (3m -0.7%; half assumed priced; market-priced macro drift removed) + 0.5 × company-specific catalysts +3.1%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply -6.3% (beta-adjusted) vs a realised market-adjusted move of -8.4% — gap +2.1 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## Where the expected return comes from
Market-priced macro drivers (rates, FX, commodities, indices, volatility, flows, growth, inflation) are taken as priced, so what is left is policy, regulatory, sector, theme, geopolitical and company-specific exposure — where 2nd–4th-order effects are most likely to be missed. Percentage points of the expected relative return.
| source | 12m: 1st order | 12m: 2nd–4th order | 12m total | 3m total |
|---|---|---|---|---|
| Policy | +0.00 | +0.01 | +0.01 | -0.05 |
| Regulatory | -0.43 | -0.12 | -0.55 | -0.07 |
| Sector | -0.33 | +0.34 | +0.01 | +0.13 |
| Theme | +0.00 | +0.07 | +0.07 | +0.05 |
| Geopolitics | +0.00 | -0.06 | -0.06 | -0.04 |
| Company catalysts | +1.44 | +0.13 | +1.57 | +0.00 |
| Market-priced macro | +0.00 | -0.00 | -0.00 | +0.00 |
| Beta adjustment | — | — | -0.77 | -0.35 |
| Universe centring | — | — | -0.15 | -0.10 |
| **Expected relative return** | | | **+0.14** | **-0.43** |

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Household savings shift to financial assets (`T_FINANCIALISATION`) | +1 | +3.57 | +2.50 | +1.02 | +0.03 | +0.02 | — |
| India 10-year G-sec yield (`F_GSEC_10Y_IN`) | +25 bp yield | -3.33 | -3.00 | -0.30 | -0.04 | +0.01 | — |
| Indian corporate credit spreads (`F_CREDIT_SPREADS_IN`) | +50 bp spreads | -3.16 | -3.00 | -0.15 | +0.02 | -0.02 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -3.08 | +0.00 | -1.70 | -1.21 | -0.17 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +3.00 | +2.50 | +0.41 | +0.04 | +0.05 | — |
| RBI prudential tightening (risk weights, LCR, provisioning) (`P_RBI_PRUDENTIAL`) | +1 = tightening step | -2.76 | -2.00 | -0.85 | +0.00 | +0.09 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -2.66 | +0.00 | -1.04 | -0.65 | -0.97 | -1.1% |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -2.50 | -1.50 | -1.04 | +0.03 | +0.02 | — |
| Domestic SIP / DII flows (`F_DOMESTIC_FLOWS`) | +10% monthly SIP + DII inflow | +2.20 | +2.00 | +0.22 | +0.00 | -0.01 | — |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -1.98 | -1.00 | -0.47 | -0.39 | -0.12 | +3.5% |
| Capital-gains / securities tax burden (`P_CAPITAL_GAINS_TAX`) | +1 = higher | -1.91 | +0.00 | -1.72 | -0.18 | -0.01 | — |
| Indian equity market volumes & retail activity (`F_EQUITY_ACTIVITY_IN`) | +20% traded value / demat additions | +1.72 | +1.80 | +0.00 | -0.08 | +0.00 | — |
| Digital payments / UPI disruption of incumbents (`T_DIGITAL_PAYMENTS`) | +1 | +1.67 | +1.20 | +0.20 | +0.23 | +0.04 | — |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -1.67 | +0.00 | +0.00 | -0.95 | -0.72 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -6.6% | -6.6% | -5.5 | -0.9 | -0.1 | -0.1 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -5.3% | -5.3% | -5.1 | -0.1 | -0.0 | -0.0 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +7.9% | +4.0% | +6.7 | +1.0 | +0.1 | +0.1 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -3.6% | -3.6% | +0.0 | -2.0 | -1.4 | -0.2 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -3.3% | -3.3% | -3.0 | -0.3 | +0.1 | -0.1 |
| Risk: USD/INR >98 and/or reserves < US$650bn (disorderly rupee, emergency RBI response) (`EV_RUPEE_BREAK_98_RESERVE_STRESS`) | risk_scenario | 0.18 | -10.4% | -1.9% | -8.2 | -2.2 | -0.1 | +0.1 |
| Budget FY2027-28: FY27 deficit overshoot confirmed and consolidation path slowed (`EV_BUDGET_FY28_FISCAL_SLIPPAGE`) | scheduled | 0.50 | -3.7% | -1.9% | -3.5 | -0.1 | -0.1 | -0.0 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -1.9% | -1.9% | +0.0 | -1.5 | -0.3 | -0.0 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -1.8% | -1.8% | +0.0 | -1.8 | -0.1 | +0.1 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.25 | -7.0% | -1.7% | -2.5 | -3.6 | -0.9 | +0.0 |
| US midterms (3 Nov 2026): Democrats win House and Senate (`EV_US_MIDTERMS_DEM_SWEEP`) | occurred | 1.00 | +1.7% | +1.7% | +1.2 | +0.4 | +0.0 | +0.0 |
| RBI MPC Dec 2026 (~4 Dec): hikes repo another 25 bp to 5.75% (`EV_RBI_DEC26_HIKE25`) | scheduled | 0.42 | -3.3% | -1.4% | -3.0 | -0.3 | +0.1 | -0.1 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → JIOFIN | +6.25% | +3.12% |
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → JIOFIN | -2.40% | -1.20% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → JIOFIN | -3.75% | -0.67% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → JIOFIN | -1.50% | -0.63% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → JIOFIN | -2.50% | -0.62% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → JIOFIN | -2.40% | -0.60% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_FPI_FLOWS → JIOFIN | -2.40% | -0.60% |
| 1 | EV_FERT_SUBSIDY_TOPUP_WINTER ⇒ F_GSEC_10Y_IN → JIOFIN | -0.60% | -0.54% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_GSEC_10Y_IN → JIOFIN | -3.00% | -0.54% |
| 1 | EV_ECL_ROLLOUT_APR27 ⇒ P_RBI_PRUDENTIAL → JIOFIN | -0.60% | -0.54% |
| 1 | EV_CPI_BREACH_6PCT ⇒ F_GSEC_10Y_IN → JIOFIN | -0.90% | -0.54% |
| 1 | EV_BANKING_LIQUIDITY_DEFICIT_MAR27 ⇒ F_GSEC_10Y_IN → JIOFIN | -0.90% | -0.54% |
| 1 | EV_BANKING_LIQUIDITY_DEFICIT_MAR27 ⇒ F_CREDIT_SPREADS_IN → JIOFIN | -0.90% | -0.54% |
| 1 | EV_RBI_DEC26_HOLD ⇒ F_GSEC_10Y_IN → JIOFIN | +0.90% | +0.47% |
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_CREDIT_SPREADS_IN → JIOFIN | -0.90% | -0.45% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_GSEC_10Y_IN → JIOFIN | +1.55 | director_override | -4.65% |
| 1 | F_FPI_FLOWS → JIOFIN | -1.60 | events | -4.00% |
| 1 | F_REPO_IN → JIOFIN | +1.00 | events | -1.50% |
| 1 | F_CREDIT_SPREADS_IN → JIOFIN | +0.50 | events | -1.50% |
| 2 | F_GDP_IN → F_CREDIT_GROWTH_IN → JIOFIN | +0.50 | events | +0.43% |
| 1 | F_EQUITY_ACTIVITY_IN → JIOFIN | +0.20 | events | +0.36% |
| 2 | F_REPO_IN → F_CREDIT_GROWTH_IN → JIOFIN | +1.00 | events | -0.29% |
| 2 | F_MONSOON → F_UNSECURED_STRESS → JIOFIN | -1.56 | events | -0.25% |
| 2 | F_LIQUIDITY_IN → F_CREDIT_GROWTH_IN → JIOFIN | -0.90 | events | -0.18% |
| 2 | F_GDP_IN → P_RBI_PRUDENTIAL → JIOFIN | +0.50 | events | -0.16% |
| 2 | F_CPI_IN → F_UNSECURED_STRESS → JIOFIN | +1.15 | events | -0.14% |
| 2 | T_FORMALISATION → T_FINANCIALISATION → JIOFIN | +0.30 | events | +0.12% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2027-01 | Q3 FY27 results (mid-Jan 2027 est.; Q2 was 15 Oct 2026) | results | 0.95 | +0.0% | +0.00% |
| 2027-03 | Closing of BofA investment into Jio Credit after regulatory approvals | corporate_action | 0.55 | +2.2% | +1.24% |
| 2027-03 | Launch of stock broking with BlackRock and Allianz insurance venture | other | 0.45 | +1.5% | +0.68% |
| 2027-04 | Offset to catalogue event EV_ECL_ROLLOUT_APR27 (bank provisioning-norm transition from Apr 2027): NBFCs are outside its scope (Ind AS 109 impairment since FY2018); cancels the generic-node impact *(review: [RT_BOT_A] EV_ECL_ROLLOUT_APR27 reaches this NBFC through generic nodes (P_RBI_PRUDENTIAL/F_ASSET_QUALITY_IN/F_CREDIT_GROWTH_IN). The impacts at the 08:44 run, conditional at p 0.9, are BAJFINANCE -1.98, TATACAP -2.41, JIOFIN -1.08 and BAJAJFINSV -1.67; the BAJAJFINSV offset is net of the BAJFINANCE offset passed through the 0.75 x 0.8 link. Offset ranges are ±20%. Wording avoids the MARKET_WIDE regex on purpose. A bank-only node is the cleaner fix and would remove the need for these offsets.)* | regulatory | 0.90 | +1.1% | +0.97% |

## Analyst profile (agent research, sourced)
# JIOFIN - Jio Financial Services (Nifty 50, NBFC holding / fintech build-out)

## Business
JIOFIN is a young financial-services platform spun out of Reliance in 2023. Subsidiaries: Jio Credit/Jio Finance (home, LAP, securities-backed, digital loans; AUM above Rs 30,000 cr in Q1 FY27), JioBlackRock Asset Management (50:50, regular plans launched 17 Aug 2026), Jio Payments Solutions and a 50% payments bank, Jio Insurance Broking, an Allianz insurance venture and a coming BlackRock broking business. In August 2026 Bank of America agreed to take up to 49.9% of Jio Credit for Rs 18,268 cr. Promoters hold 50.99% (after 25 crore share allotment on 30 Oct 2026).

## What moves the stock (ranked)
1. **Risk sentiment and flows** - beta about 1.5 to Nifty 50, FIIs 10% (down from 11.3%), plus mechanical DII/index flows. VIX +5 points is worth roughly -5%.
2. **Discount rate / yields** - TTM ROE 1.2% against P/E 92 means value sits in the future; the Oct-2026 hike and 4.89% US 10y raise the discount rate on terminal value (-3% per +25bp 10y).
3. **Funding cost** - wholesale-funded; interest expense jumped from Rs 136 cr (Sep-25) to Rs 578 cr (Sep-26). Spread widening of 50bp is about 3.5% of annualised operating profit.
4. **Execution and deal news** - BofA deal closing, broking/insurance launches, AUM milestones.
5. **Group/Reliance sentiment** - Jio Platforms IPO (launched 22 Oct 2026) can drain or lift flows; JIOFIN fell 1% on 28 Oct.

## Transmission examples
- **Middle East escalation -> Brent up (94.99, +49.5% 12m) -> India inflation and INR pressure -> RBI hawkish (hiked to 5.50% on 7 Oct) -> G-sec and AAA spreads up -> JIOFIN wholesale funding cost up -> NIM and growth slower -> multiple compresses on a P/E-92 stock.**
- **US 10y up -> FPI outflow -> Nifty down -> JIOFIN (beta 1.5, FII 10%) drops more than market -> DII index funds buy, partly cushioning (4th-order: lower retail wealth effect reduces MF/broking flows for JioBlackRock).**
- **Jio Platforms listing -> Reliance group re-rating -> group_contagion lifts JIOFIN sentiment; but absorption of Rs ~36k cr (US$3.8bn) of retail/institutional demand may crowd out other group names for weeks.**
- **Unsecured stress in India (MFI/PL) -> NBFC spread widening -> investor haircut to all new lenders -> BofA deal valuation questioned.**

## Current situation
Q2 FY27 PAT Rs 340 cr (-51% y/y) because last year's quarter held a gain and costs scaled; but NII +165% and income more than doubled. MOFSL cut FY27 estimates yet kept target Rs 300. Stock -12.6% over 3m, -23.9% over 12m, 1m +5.5%.

## Upcoming
Jio Platforms listing, Q3 results mid-Jan 2027, BofA closing, broking and insurance launches.

## Bull / bear
Bull: AUM compounds 50%+, BofA validates valuation, ecosystem cross-sell, ROE climbs towards 10% by FY29. Bear: valuation (P/E 92) has no earnings support, funding costs rise, credit quality unseasoned, group IPO diverts flows.

Uncertainty: lending-mix and funding-mix shares are model-knowledge approximations; weights are low-confidence and the empirical USDCNY +4.3 (t=2.2) sensitivity was judged spurious and not modelled.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.