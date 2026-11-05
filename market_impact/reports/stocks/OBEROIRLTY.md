# OBEROIRLTY — Oberoi Realty Ltd.
*MIDCAP_100 · Realty · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -3.2%**, **12 months -5.2%** (rank 176 / 166 of 200 for 3m / 12m); beta 1.22
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +23.7%): 3 months 39%, 12 months 40%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -10.0% … P90 -2.5%; plausible 12m relative-return range incl. stock-specific noise: -42.4% … +24.6%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves -2.2 pp (model impact -4.4% beta-adjusted vs realised market-adjusted move +0.2%); forward event exposure -5.6% (3m -3.2%; half assumed priced); company-specific events +1.9%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| India CPI inflation (`F_CPI_IN`) | +1 pp | -5.74 | +0.00 | -3.44 | -1.85 | -0.44 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -3.40 | -2.50 | -0.69 | -0.17 | -0.04 | — |
| Residential real-estate sales (`F_HOUSING_DEMAND`) | +10% sales volume | +3.39 | +3.50 | +0.00 | -0.07 | -0.03 | — |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -2.90 | +0.00 | +0.00 | -1.90 | -1.01 | — |
| Consumer premiumisation (`T_PREMIUMISATION`) | +1 | +2.61 | +2.50 | +0.10 | +0.01 | -0.00 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +2.16 | +2.00 | +0.02 | +0.06 | +0.08 | — |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +2.03 | +0.00 | +0.76 | +0.92 | +0.36 | — |
| India real GDP growth (`F_GDP_IN`) | +1 pp | -1.83 | +0.00 | -0.32 | -0.99 | -0.52 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -1.69 | +0.00 | -0.06 | -0.47 | -1.16 | — |
| India 10-year G-sec yield (`F_GSEC_10Y_IN`) | +25 bp yield | -1.60 | -1.20 | -0.42 | +0.00 | +0.02 | — |
| Affordable-housing / home-loan support (`P_HOUSING_POLICY`) | +1 = stronger support | +1.54 | +1.00 | +0.56 | +0.00 | -0.02 | — |
| Capital-gains / securities tax burden (`P_CAPITAL_GAINS_TAX`) | +1 = higher | -1.48 | -1.00 | -0.45 | -0.01 | -0.02 | — |
| Brent crude oil price (`F_BRENT`) | +10% Brent | -1.44 | +0.00 | -0.15 | -0.80 | -0.49 | +0.0% |
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +1.39 | +1.50 | +0.16 | -0.06 | -0.21 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -8.0% | -8.0% | +0.0 | -0.8 | -4.4 | -2.8 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -6.6% | -6.6% | +0.0 | -4.0 | -2.1 | -0.5 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -4.8% | -4.8% | -4.4 | -0.0 | -0.1 | -0.2 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -3.5% | -3.5% | -2.9 | -0.6 | -0.0 | -0.1 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +5.5% | +2.7% | +5.0 | +0.0 | +0.2 | +0.3 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -2.3% | -2.3% | +0.0 | -1.8 | -0.5 | -0.1 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -2.3% | -2.3% | -1.7 | -0.6 | -0.0 | +0.0 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.36 | -5.6% | -2.0% | +0.0 | -1.3 | -2.7 | -1.6 |
| Gold and silver slump from January 2026 peaks (silver -53%, gold -24%) (`EV_PRECIOUS_METALS_CRASH_2026`) | occurred | 1.00 | -1.9% | -1.9% | +0.0 | -1.6 | -0.2 | -0.1 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -1.9% | -1.9% | +0.0 | -1.2 | -0.5 | -0.2 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.58 | +3.1% | +1.8% | +0.0 | +0.6 | +1.5 | +0.9 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.28 | -6.2% | -1.7% | +0.0 | -5.1 | -0.7 | -0.5 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → OBEROIRLTY | +5.00% | +2.50% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → OBEROIRLTY | -2.50% | -1.00% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → OBEROIRLTY | -2.99% | -0.84% |
| 2 | EV_PULSES_VEG_SPIKE_WINTER ⇒ F_CPI_IN → F_REPO_IN → OBEROIRLTY | -2.88% | -0.72% |
| 1 | EV_RBI_FEB27_HIKE25 ⇒ F_REPO_IN → OBEROIRLTY | -2.50% | -0.68% |
| 2 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → OBEROIRLTY | -3.73% | -0.67% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → OBEROIRLTY | -3.00% | -0.66% |
| 1 | EV_CPI_BREACH_6PCT ⇒ F_REPO_IN → OBEROIRLTY | -1.00% | -0.60% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_REPO_IN → OBEROIRLTY | -2.50% | -0.55% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → OBEROIRLTY | -1.92% | -0.54% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_FPI_FLOWS → OBEROIRLTY | -1.92% | -0.48% |
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → OBEROIRLTY | -0.96% | -0.48% |
| 3 | EV_WHEAT27_CROP_BELOW ⇒ F_FOOD_INFLATION_IN → F_CPI_IN → F_REPO_IN → OBEROIRLTY | -0.63% | -0.41% |
| 3 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → F_CPI_IN → F_REPO_IN → OBEROIRLTY | -1.12% | -0.40% |
| 3 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → F_CPI_IN → F_REPO_IN → OBEROIRLTY | +0.67% | +0.39% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_FPI_FLOWS → OBEROIRLTY | -1.60 | events | -3.20% |
| 1 | F_REPO_IN → OBEROIRLTY | +1.00 | events | -2.50% |
| 1 | F_GSEC_10Y_IN → OBEROIRLTY | +1.70 | events | -2.04% |
| 2 | F_GSEC_10Y_IN → F_HOUSING_DEMAND → OBEROIRLTY | +1.70 | events | -0.71% |
| 1 | F_STEEL_INDIA → OBEROIRLTY | +1.65 | events | -0.66% |
| 2 | F_GDP_IN → F_HOUSING_DEMAND → OBEROIRLTY | +0.50 | events | +0.42% |
| 2 | F_REPO_IN → F_HOUSING_DEMAND → OBEROIRLTY | +1.00 | events | -0.36% |
| 1 | F_URBAN_DEMAND → OBEROIRLTY | +0.20 | events | +0.30% |
| 2 | T_GENAI_SERVICES → F_HOUSING_DEMAND → OBEROIRLTY | +1.00 | events | -0.28% |
| 1 | F_US_TECH_SPEND → OBEROIRLTY | -0.60 | events | -0.24% |
| 2 | F_STEEL_INDIA → F_HOUSING_DEMAND → OBEROIRLTY | +1.65 | events | -0.12% |
| 1 | F_USDINR → OBEROIRLTY | -0.37 | observed | -0.11% |

## Analyst profile (agent research, sourced)
# Oberoi Realty (OBEROIRLTY) - profile as of 2026-11-05

## Business
Oberoi Realty is the most conservatively financed developer in the Nifty 200 realty group. It builds ultra-luxury and premium housing in Mumbai (Worli, Goregaon, Borivali, Thane, Mulund), owns annuity assets (Commerz offices, Oberoi Mall, Oberoi Garden City) and hotels. Interest cost is only Rs 205 crore TTM versus operating profit of Rs 3,560 crore (about 57% margin), so rate-driven financing risk is small; rate risk is demand and valuation, not interest cost. Q2 FY27 PAT was about Rs 762 crore (flat) on revenue down 6%, while pre-sales beat Nomura's estimates (Moneycontrol, 2026-10-19). The company declared a Rs 2 second interim dividend (2026-10-16) and said it is open to land buys and joint development across Delhi-NCR (Business Standard, 2026-10-19).

## What moves the stock
1. **Mumbai housing volumes (+3.5 per +10%)**; luxury demand is wealth-driven, so less rate-elastic than mid-segment names.
2. **Repo (-2.5 per +25 bp)** after the RBI's hike to 5.50% on 2026-10-07; beta is only about 1.3, the lowest in the group.
3. **Premiumisation (+2.5)** and **G-sec yields (-1.2)** via cap rates on the annuity book.
4. FPI/DII flows (+2.0, +0.8), urban demand (+1.5), travel/hotels (+0.5), NRI remittances (+0.4), US tech spend (+0.4), policy (housing +1.0, capital gains -1.0), costs (steel -0.4, cement -0.3, wages -0.3).
The pack shows wheat (+1.8, t=2.1) and edible oil (+2.45, t=1.9) co-movement; no mechanism links them, so they are ignored as spurious.

## Transmission examples
- **Rates (4 orders)**: oil at $95 -> CPI up and rupee weak -> RBI hikes again -> G-sec 10y rises -> cap rates on Commerz/Oberoi Mall widen and luxury buyers' mortgages cost more -> NAV -2 to -4% and pre-sales slow modestly.
- **Equity wealth (3 orders)**: strong Nifty and FPI inflows -> HNI wealth up -> Worli/Sky City sales -> pre-sales beat (as in Q2) -> operating leverage at 57% margins.
- **Tech/office (4 orders)**: US tech slowdown -> Mumbai BFSI/IT hiring weaker -> Commerz leasing -> lower rental growth.
- **Costs (3 orders)**: steel/cement up -> construction cost +0.3% of revenue; minor given high margins.

## Current situation
Earnings flat, valuation lowest of the realty peers (P/E 24), strong balance sheet, six sell-side Buy calls with TPs near Rs 2,100. The stock is range-bound (12m -2%, 1m -0.4%) while peers rallied after the hike.

## Upcoming
Q3 FY27 (about January 2027), December MPC, first NCR deal (prob ~0.35 within the horizon), new phase launches.

## Bull / Bear
Bull: pre-sales beats convert to revenue, NCR deal adds growth, capital return. Bear: Mumbai luxury sales falter under higher rates; revenue remains lumpy. Confidence medium; segment NAV weights are model estimates.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.