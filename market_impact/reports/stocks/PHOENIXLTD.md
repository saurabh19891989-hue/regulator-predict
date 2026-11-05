# PHOENIXLTD — Phoenix Mills Ltd.
*MIDCAP_100 · Realty · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -0.6%**, **12 months -0.9%** (rank 164 / 148 of 200 for 3m / 12m); beta 1.29
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +22.8%): 3 months 48%, 12 months 49%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -3.6% … P90 +1.0%; plausible 12m relative-return range incl. stock-specific noise: -29.5% … +27.1%
- Decomposition (12m): 0.5 × forward event exposure -1.9% (3m -0.9%; half assumed priced; market-priced macro drift removed) + 0.5 × company-specific catalysts +0.6%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply -3.9% (beta-adjusted) vs a realised market-adjusted move of +14.8% — gap -18.8 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Consumer premiumisation (`T_PREMIUMISATION`) | +1 | +3.16 | +3.00 | +0.12 | +0.03 | +0.01 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +2.65 | +2.50 | +0.10 | +0.00 | +0.04 | — |
| India 10-year G-sec yield (`F_GSEC_10Y_IN`) | +25 bp yield | -2.54 | -2.50 | -0.02 | -0.01 | -0.01 | — |
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +2.43 | +2.00 | +0.40 | +0.07 | -0.04 | — |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +1.85 | +1.00 | +0.40 | +0.30 | +0.15 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -1.76 | -0.50 | -0.79 | -0.46 | -0.01 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -1.71 | -0.99 | -0.65 | -0.05 | -0.02 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -1.65 | +0.00 | -0.97 | -0.40 | -0.29 | -1.1% |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -1.52 | +0.00 | -0.93 | -0.53 | -0.06 | +3.5% |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -1.49 | +0.00 | -0.06 | -0.88 | -0.54 | — |
| India real GDP growth (`F_GDP_IN`) | +1 pp | +1.30 | +1.20 | +0.18 | -0.00 | -0.08 | — |
| General-government fiscal slippage / extra borrowing vs budget (Centre + states) (`NEW_FISCAL_SLIPPAGE_IN`) | +0.5 pp of GDP deficit above budget (~Rs2 lakh cr) | -1.28 | +0.00 | -1.00 | -0.21 | -0.07 | — |
| US 10-year Treasury yield (`F_US_10Y`) | +25 bp yield | -1.17 | +0.00 | -1.15 | -0.08 | +0.06 | +9.4% |
| Capital-gains / securities tax burden (`P_CAPITAL_GAINS_TAX`) | +1 = higher | -1.09 | -0.50 | -0.56 | -0.03 | +0.00 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -5.8% | -5.8% | -5.5 | -0.2 | -0.0 | -0.1 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -3.6% | -3.6% | -3.5 | -0.0 | -0.1 | -0.0 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +6.6% | +3.3% | +6.2 | +0.2 | +0.0 | +0.1 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -2.1% | -2.1% | -0.6 | -0.9 | -0.6 | -0.0 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -2.0% | -2.0% | -1.7 | -0.1 | -0.1 | -0.0 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -1.5% | -1.5% | +0.0 | -1.3 | -0.2 | +0.0 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -1.5% | -1.5% | +0.0 | -1.6 | -0.0 | +0.1 |
| US midterms (3 Nov 2026): Democrats win House and Senate (`EV_US_MIDTERMS_DEM_SWEEP`) | occurred | 1.00 | +1.5% | +1.5% | +1.2 | +0.2 | +0.0 | +0.0 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.25 | -5.5% | -1.4% | +0.0 | -5.0 | -0.6 | +0.1 |
| Risk: USD/INR >98 and/or reserves < US$650bn (disorderly rupee, emergency RBI response) (`EV_RUPEE_BREAK_98_RESERVE_STRESS`) | risk_scenario | 0.18 | -7.6% | -1.4% | -7.2 | -0.2 | -0.2 | -0.0 |
| Budget FY2027-28: FY27 deficit overshoot confirmed and consolidation path slowed (`EV_BUDGET_FY28_FISCAL_SLIPPAGE`) | scheduled | 0.50 | -2.4% | -1.2% | -2.0 | -0.2 | -0.1 | -0.0 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -1.2% | -1.2% | +0.0 | -0.4 | -0.4 | -0.4 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → PHOENIXLTD | +6.25% | +3.12% |
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → PHOENIXLTD | -2.00% | -1.00% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → PHOENIXLTD | -3.75% | -0.67% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → PHOENIXLTD | -2.40% | -0.60% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_FPI_FLOWS → PHOENIXLTD | -2.40% | -0.60% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → PHOENIXLTD | -2.33% | -0.58% |
| 1 | EV_FERT_SUBSIDY_TOPUP_WINTER ⇒ F_GSEC_10Y_IN → PHOENIXLTD | -0.50% | -0.45% |
| 1 | EV_CPI_BREACH_6PCT ⇒ F_GSEC_10Y_IN → PHOENIXLTD | -0.75% | -0.45% |
| 1 | EV_BANKING_LIQUIDITY_DEFICIT_MAR27 ⇒ F_GSEC_10Y_IN → PHOENIXLTD | -0.75% | -0.45% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_GSEC_10Y_IN → PHOENIXLTD | -2.50% | -0.45% |
| 1 | EV_BUDGET_FY28_LTCG_RELIEF ⇒ F_FPI_FLOWS → PHOENIXLTD | +1.25% | +0.44% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → PHOENIXLTD | -0.99% | -0.42% |
| 1 | EV_Q2_FY27_GDP_STRONG ⇒ F_FPI_FLOWS → PHOENIXLTD | +0.50% | +0.40% |
| 1 | EV_RBI_DEC26_HOLD ⇒ F_GSEC_10Y_IN → PHOENIXLTD | +0.75% | +0.39% |
| 2 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → PHOENIXLTD | -2.33% | -0.35% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_FPI_FLOWS → PHOENIXLTD | -1.60 | events | -4.00% |
| 1 | F_GSEC_10Y_IN → PHOENIXLTD | +1.55 | director_override | -3.88% |
| 1 | F_REPO_IN → PHOENIXLTD | +1.00 | events | -0.99% |
| 1 | F_GDP_IN → PHOENIXLTD | +0.50 | events | +0.60% |
| 1 | F_CPI_IN → PHOENIXLTD | +1.15 | events | -0.57% |
| 1 | F_URBAN_DEMAND → PHOENIXLTD | +0.20 | events | +0.40% |
| 1 | F_STEEL_INDIA → PHOENIXLTD | +1.35 | events | -0.27% |
| 1 | F_US_TECH_SPEND → PHOENIXLTD | -0.60 | events | -0.24% |
| 2 | C_MIDEAST_CONFLICT → F_TRAVEL_DEMAND → PHOENIXLTD | +1.00 | events | -0.06% |
| 2 | F_REPO_IN → F_HOUSING_DEMAND → PHOENIXLTD | +1.00 | events | -0.05% |
| 3 | T_FORMALISATION → T_FINANCIALISATION → F_DOMESTIC_FLOWS → PHOENIXLTD | +0.30 | events | +0.04% |
| 2 | F_URBAN_DEMAND → F_TRAVEL_DEMAND → PHOENIXLTD | +0.20 | events | +0.03% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-11/2026-12 | Final dividend Rs 2.50/share for FY26 recommended (scanx 2026-11-01): record/payment date; mechanical price adjustment ~0.1% | corporate_action | 0.90 | +0.0% | +0.00% |
| 2026-12/2027-03 | Festive/Diwali and holiday consumption datapoints; mall consumption growth vs +28% H1 *(review: [RT_BOT_B] )* | other | 0.90 | +0.0% | +0.00% |
| 2027-02 | Q3 FY27 results (date model-estimated; Q2 reported ~2026-10-30) *(review: [RT_BOT_B] )* | results | 0.95 | +0.0% | +0.00% |
| 2027-06 | New mall openings/Phase expansions (Mall of Asia stabilisation, Bangalore) and ISMDPL consolidation effects | capex | 0.60 | +1.0% | +0.60% |

## Analyst profile (agent research, sourced)
# Phoenix Mills (PHOENIXLTD) - profile as of 2026-11-05

## Business
Phoenix Mills is the premium-mall specialist of the Indian listed market: Phoenix Marketcity (Mumbai, Pune, Bengaluru, Chennai), Palladium, Mall of Asia (Bengaluru), plus offices, hotels and a small residential arm. The annuity model yields a 60% operating margin and, unlike the developers, revenue is recurring (rent plus turnover rent). Management guided 14-15% rental growth through FY28 (scanx, 2026-11-04) and H1 FY27 retail consumption was +28%, led by the new Mall of Asia (Multibagg AI, 2026-10-31). Q2 owner profit grew 7%. At a P/E of 57 and P/B 8.3 the stock is priced as a quality compounder (BofA, 2026-09-17) and rose 12% in the last month.

## What moves the stock
1. **Premiumisation (+3.0)** and **urban consumption (+2.0 per +5pp)**: tenant sales feed turnover rent.
2. **Yields and rates**: G-sec 10y -2.5 per +25 bp (cap-rate/long-duration effect) and repo -3.0; the RBI hiked to 5.50% on 2026-10-07 and G-sec/US yields are elevated (US 10Y 4.89%).
3. FPI/DII flows (+2.5/+1.0), GDP (+1.2), GST cuts (+1.0), travel (+0.5), substitution by quick commerce (-0.4), CPI (-0.5), office tenants (US tech +0.4).
The pack's top empirical sensitivities (sugar +1.43, gas -0.77) are below |t|=2 and unrelated to the business, so they are ignored.

## Transmission examples
- **Rates (4 orders)**: oil at $95 -> CPI up -> RBI hikes again -> 10y G-sec up -> required mall/office yields widen -> asset values fall and a 57x multiple compresses, while interest cost on mall capex rises.
- **Consumption (3 orders)**: GST cut or income-tax relief -> tenant sales growth -> turnover rent above minimum guarantee -> rental growth above 14-15% guidance.
- **Wealth (3 orders)**: equity rally -> luxury spending -> Palladium sales -> luxury brands expand space -> higher renewal spreads.
- **Channel shift (3 orders)**: quick-commerce growth -> low-ticket mall footfall slips -> anchor and F&B tenant sales weaken -> turnover rent growth slows.

## Current situation
Consumption and rental guidance are strong; the share is near its high, so valuation, not fundamentals, is the main risk. Final dividend Rs 2.50 recommended; BofA Property Week on 2026-11-06.

## Upcoming
Dividend payment, festive-season consumption data, Q3 results (~February 2027), December MPC.

## Bull / Bear
Bull: sustained 14-15% rental growth plus Mall of Asia ramp. Bear: yields rise further and the 57x multiple compresses. Confidence medium; segment shares and debt are model estimates.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.