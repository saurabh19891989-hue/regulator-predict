# DLF — DLF Ltd.
*NIFTY_NEXT_50 · Realty · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -0.3%**, **12 months -0.8%** (rank 139 / 145 of 200 for 3m / 12m); beta 1.53
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +20.6%): 3 months 49%, 12 months 48%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -3.5% … P90 +0.9%; plausible 12m relative-return range incl. stock-specific noise: -29.1% … +27.0%
- Decomposition (12m): 0.5 × forward event exposure -2.1% (3m -0.9%; half assumed priced; market-priced macro drift removed) + 0.5 × company-specific catalysts +1.0%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply -3.2% (beta-adjusted) vs a realised market-adjusted move of +20.9% — gap -24.1 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Residential real-estate sales (`F_HOUSING_DEMAND`) | +10% sales volume | +3.61 | +3.50 | +0.10 | +0.01 | +0.00 | — |
| Consumer premiumisation (`T_PREMIUMISATION`) | +1 | +3.09 | +3.00 | +0.06 | +0.02 | +0.01 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -2.90 | -2.00 | -0.77 | -0.08 | -0.05 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +2.59 | +2.50 | +0.04 | +0.02 | +0.04 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -2.47 | +0.00 | -1.81 | -0.59 | -0.06 | — |
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +1.81 | +1.50 | +0.24 | +0.16 | -0.08 | — |
| Affordable-housing / home-loan support (`P_HOUSING_POLICY`) | +1 = stronger support | +1.79 | +1.20 | +0.56 | +0.03 | +0.00 | — |
| India 10-year G-sec yield (`F_GSEC_10Y_IN`) | +25 bp yield | -1.75 | -1.60 | -0.14 | -0.01 | -0.01 | — |
| Capital-gains / securities tax burden (`P_CAPITAL_GAINS_TAX`) | +1 = higher | -1.58 | -1.00 | -0.56 | -0.01 | -0.01 | — |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +1.47 | +0.00 | +0.70 | +0.57 | +0.21 | — |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -1.41 | +0.00 | -0.90 | -0.46 | -0.05 | +3.5% |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -1.40 | +0.00 | +0.00 | -1.06 | -0.34 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -1.37 | +0.00 | +0.00 | -0.70 | -0.67 | — |
| India real GDP growth (`F_GDP_IN`) | +1 pp | +1.37 | +1.20 | +0.42 | -0.14 | -0.12 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -5.7% | -5.7% | -5.5 | -0.1 | -0.0 | -0.1 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +6.5% | +3.2% | +6.2 | +0.1 | +0.0 | +0.1 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -3.1% | -3.1% | -2.5 | -0.5 | -0.1 | -0.1 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -2.9% | -2.9% | +0.0 | -2.1 | -0.7 | -0.1 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -2.5% | -2.5% | -2.2 | -0.2 | -0.0 | -0.0 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -1.5% | -1.5% | +0.0 | -1.2 | -0.3 | +0.0 |
| US midterms (3 Nov 2026): Democrats win House and Senate (`EV_US_MIDTERMS_DEM_SWEEP`) | occurred | 1.00 | +1.4% | +1.4% | +1.2 | +0.1 | +0.0 | +0.0 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.25 | -5.5% | -1.4% | +0.0 | -5.2 | -0.4 | +0.1 |
| Risk: USD/INR >98 and/or reserves < US$650bn (disorderly rupee, emergency RBI response) (`EV_RUPEE_BREAK_98_RESERVE_STRESS`) | risk_scenario | 0.18 | -7.6% | -1.4% | -7.0 | -0.5 | -0.1 | -0.1 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -1.3% | -1.3% | +0.0 | -0.4 | -0.3 | -0.6 |
| RBI MPC Dec 2026 (~4 Dec): hikes repo another 25 bp to 5.75% (`EV_RBI_DEC26_HIKE25`) | scheduled | 0.42 | -3.1% | -1.3% | -2.5 | -0.5 | -0.1 | -0.1 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -1.2% | -1.2% | +0.0 | -1.3 | -0.0 | +0.1 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → DLF | +6.25% | +3.12% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → DLF | -2.00% | -0.84% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → DLF | -3.75% | -0.67% |
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → DLF | -1.28% | -0.64% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → DLF | -2.40% | -0.60% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_FPI_FLOWS → DLF | -2.40% | -0.60% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → DLF | -2.33% | -0.58% |
| 1 | EV_RBI_FEB27_HIKE25 ⇒ F_REPO_IN → DLF | -2.00% | -0.54% |
| 1 | EV_BUDGET_FY28_LTCG_RELIEF ⇒ F_FPI_FLOWS → DLF | +1.25% | +0.44% |
| 1 | EV_Q2_FY27_GDP_STRONG ⇒ F_FPI_FLOWS → DLF | +0.50% | +0.40% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_REPO_IN → DLF | -2.00% | -0.36% |
| 2 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → DLF | -2.33% | -0.35% |
| 1 | EV_FERT_SUBSIDY_TOPUP_WINTER ⇒ F_GSEC_10Y_IN → DLF | -0.32% | -0.29% |
| 1 | EV_CPI_BREACH_6PCT ⇒ F_GSEC_10Y_IN → DLF | -0.48% | -0.29% |
| 1 | EV_BANKING_LIQUIDITY_DEFICIT_MAR27 ⇒ F_GSEC_10Y_IN → DLF | -0.48% | -0.29% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_FPI_FLOWS → DLF | -1.60 | events | -4.00% |
| 1 | F_GSEC_10Y_IN → DLF | +1.55 | director_override | -2.48% |
| 1 | F_REPO_IN → DLF | +1.00 | events | -2.00% |
| 1 | F_GDP_IN → DLF | +0.50 | events | +0.60% |
| 1 | F_STEEL_INDIA → DLF | +1.35 | events | -0.54% |
| 1 | F_US_TECH_SPEND → DLF | -0.60 | events | -0.48% |
| 2 | F_REPO_IN → F_HOUSING_DEMAND → DLF | +1.00 | events | -0.36% |
| 1 | F_URBAN_DEMAND → DLF | +0.20 | events | +0.30% |
| 2 | F_GSEC_10Y_IN → F_HOUSING_DEMAND → DLF | +1.55 | director_override | -0.21% |
| 2 | F_GDP_IN → F_HOUSING_DEMAND → DLF | +0.50 | events | +0.21% |
| 2 | T_GENAI_SERVICES → F_HOUSING_DEMAND → DLF | +0.50 | director_override | -0.14% |
| 1 | F_USDINR → DLF | -0.37 | observed | -0.11% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-12/2027-03 | Launch of luxury projects from Rs 58,000 cr pipeline (Gurugram/Goa/Mumbai); sell-through speed is the key datapoint *(review: [RT_N50_B] RT_N50_B: The Rs58,000 cr pipeline was announced on 2026-10-19 and is in consensus. Only the sell-through surprise is unpriced, so the impact is symmetric.)* | capex | 0.75 | +0.0% | +0.00% |
| 2026-12/2027-06 | Further DCCDL/GIC stake or monetisation, or office/retail asset acquisitions, using surplus cash | corporate_action | 0.20 | +0.5% | +0.10% |
| 2027-01 | Q3 FY27 results (date model-estimated from Q2 on 2026-10-16): bookings run-rate vs Rs 3,800 cr in Q2, margin recovery | results | 0.95 | +0.5% | +0.47% |
| 2027-03 | NSE semi-annual index review (effective March): DLF possible Nifty 50 candidate on market cap; weakly sourced model judgement | corporate_action | 0.10 | +4.0% | +0.40% |
| 2027-05 | Q4/FY27 results and FY28 guidance: management says revenue growth resumes in FY28 as Rs 75,000 cr projects near completion *(review: [RT_N50_B] RT_N50_B: The results/guidance range had a positive skew (-5..+8) with no evidence of a beat. Q2 sales were -23% y/y and operating margin 1.8%.)* | guidance | 0.90 | +0.0% | +0.00% |

## Analyst profile (agent research, sourced)
# DLF Ltd. (DLF) - Nifty Next 50 profile, as of 2026-11-05

## Business
DLF is India's largest listed developer (market cap about Rs 1.83 lakh crore, promoter family 74.08%). It earns in two ways. Residential development, concentrated in Gurugram/NCR luxury and super-luxury with additions in Goa, Mumbai and Chandigarh, drives bookings and, with a lag, revenue; rental income via DLF Cyber City Developers (DCCDL, with GIC as co-owner) plus malls and hospitality provides annuity cash flow. The screener consolidated interest line is only Rs 93 crore TTM and the company is essentially debt-free, so DLF behaves like a net-cash, long-duration, high-multiple real-estate stock (P/E 40, P/B 4.0). Reported sales are lumpy: Q2 FY27 revenue was Rs 1,261 crore (-23% y/y) with operating profit of just Rs 23 crore, yet PAT was Rs 1,301 crore, supported by JV share, other income (Rs 2,069 crore in FY26) and a Rs 738 crore non-cash gain (Moneycontrol, 2026-10-19). Bookings, not reported revenue, are the real signal: Rs 3,800 crore in Q2, a sold-out Rs 1,985 crore Gurugram senior-living tower, and a Rs 58,000 crore launch plan (Business Standard, 2026-10-19). Management says revenue growth resumes in FY28 as Rs 75,000 crore of projects near completion and sees Rs 42,460 crore surplus cash potential from launched projects (Q2 call, 2026-10-17).

## What moves the stock (ranked, by model weight and confidence)
1. **Luxury premiumisation (w +3.0)**: DLF's edge is that the buyer is wealth-driven, not EMI-driven. Sell-outs and price realisations matter more than market-wide volumes.
2. **Housing-market volume (w +3.5 per +10%)**: but Anarock shows only +3% y/y for Jul-Sep 2026 across seven cities, so the cycle is flat, not accelerating.
3. **FPI flows (w +2.5)**: beta 1.7-1.9; FII holding slid 13.5% -> 11.4% over two quarters while DIIs rose 6.9% -> 9.1%.
4. **RBI repo (w -2.0 per +25 bp)** and **G-sec yields (w -1.6)**: the RBI hiked to 5.50% on 2026-10-07 and signalled no cuts; analysts quoted by India Today/The Hindu see up to 50 bp more by December. The stock nonetheless rose 11% in the following month, so the sentiment hit is not yet visible; this is the main asymmetry.
5. Macro growth/urban wealth (GDP +1.2, urban demand +1.5), US tech spend/GCC leasing (+0.8), policy (housing +1.2, capital gains -1.0), and minor input-cost items (steel -0.4, cement -0.3, wages -0.3).

The empirical pack shows no statistically significant commodity or FX sensitivity (largest |t| 1.5, silver), so factor weights rely on mechanism, not data; confidence is medium at best.

## Worked transmission examples
- **Rate path (4 orders)**: Middle East escalation -> Brent +10% (already ~$95, +15% in 3 months) -> India CPI up and rupee weaker (USD/INR 94.5) -> RBI delivers another hike in December -> mortgage rates +25 bp and G-sec yields up -> luxury-housing sentiment and cap rates on Cyber City offices worsen -> DLF multiple derates by roughly 3-4% (repo -2.0 plus G-sec -1.6 per 25 bp each), partly offset because DLF is net cash and earns more on treasury balances.
- **Wealth effect (3 orders)**: equity-market rally / FPI inflow -> HNI and promoter wealth up -> super-luxury demand in Gurugram -> faster sell-through of the Rs 58,000 crore pipeline -> bookings beat and surplus cash released earlier.
- **Office channel (4 orders)**: US tech/AI capex slows -> GCC and IT hiring in Gurugram slows -> Cyber City leasing and renewals soften (though 96% leased limits the near-term hit) -> DCCDL rent growth fades -> DLF's annuity value and dividend capacity weaken.
- **Construction cost (3 orders)**: China steel exports surge or domestic HRC cools -> lower steel -> small cost relief on unsold inventory; negligible for DLF because of fixed-price contracts.

## Current situation
Q2 FY27 headline: PAT +11% but revenue -23% and operating margin 1.8%; analysts (Jefferies, CLSA, Motilal TP Rs 780) focus on launches and surplus cash. The stock is near its 52-week high (Rs 774) after +11% in a month. TTM PAT Rs 4,567 crore versus operating profit Rs 974 crore shows how much of earnings is non-operating.

## Upcoming
Launches from the Rs 58,000 crore pipeline through FY27; Q3 results (about January 2027, model-estimated); RBI's December MPC; March 2027 index review; FY28 revenue-recovery guidance.

## Bull case
Pipeline sells out quickly, surplus cash is returned or redeployed accretively, rent growth continues, FPI flows return, and the RBI pauses: stock compounds toward the broker bull cases (41% upside quoted by Jefferies/CLSA, a sell-side view, not our forecast).

## Bear case
More tightening and higher yields compress a P/E-40 multiple, FIIs keep selling, luxury demand stalls after launches, and the market refocuses on weak operating profit and non-cash earnings quality.

Confidence: medium. Segment NAV weights, NRI share, and DCCDL ownership are model estimates and are not verified from filings in this pass.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.