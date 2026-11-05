# PRESTIGE — Prestige Estates Projects Ltd.
*MIDCAP_100 · Realty · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -4.3%**, **12 months -9.0%** (rank 185 / 188 of 200 for 3m / 12m); beta 1.56
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +23.6%): 3 months 36%, 12 months 30%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -15.6% … P90 -6.4%; plausible 12m relative-return range incl. stock-specific noise: -44.5% … +10.7%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves -3.9 pp (model impact -7.7% beta-adjusted vs realised market-adjusted move +12.6%); forward event exposure -10.6% (3m -5.5%; half assumed priced); company-specific events +2.7%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| India CPI inflation (`F_CPI_IN`) | +1 pp | -8.05 | +0.00 | -4.98 | -2.51 | -0.57 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -5.02 | -4.00 | -0.78 | -0.21 | -0.03 | — |
| Residential real-estate sales (`F_HOUSING_DEMAND`) | +10% sales volume | +4.77 | +5.00 | +0.00 | -0.17 | -0.06 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -4.37 | +0.00 | -1.77 | -1.52 | -1.09 | -1.1% |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -4.09 | +0.00 | +0.00 | -2.74 | -1.34 | — |
| India real GDP growth (`F_GDP_IN`) | +1 pp | -3.27 | +0.00 | -0.81 | -1.66 | -0.80 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +3.27 | +3.00 | +0.04 | +0.10 | +0.12 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -2.63 | +0.00 | -0.11 | -0.85 | -1.67 | — |
| Affordable-housing / home-loan support (`P_HOUSING_POLICY`) | +1 = stronger support | +2.26 | +1.50 | +0.80 | +0.00 | -0.04 | — |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +2.20 | +0.00 | +0.46 | +1.33 | +0.41 | — |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -2.18 | +0.00 | -1.16 | -0.72 | -0.29 | +3.5% |
| Brent crude oil price (`F_BRENT`) | +10% Brent | -2.16 | +0.00 | -0.36 | -1.18 | -0.62 | +0.0% |
| Capital-gains / securities tax burden (`P_CAPITAL_GAINS_TAX`) | +1 = higher | -1.90 | -1.20 | -0.65 | -0.01 | -0.03 | — |
| US equity market (`F_US_EQUITIES`) | +5% S&P 500 | +1.69 | +0.00 | +0.96 | +0.57 | +0.16 | +1.2% |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -12.0% | -12.0% | +0.0 | -1.9 | -6.5 | -3.6 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -9.2% | -9.2% | +0.0 | -5.7 | -2.9 | -0.6 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -7.3% | -7.3% | -6.6 | -0.1 | -0.3 | -0.4 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -5.3% | -5.3% | -4.5 | -0.7 | +0.1 | -0.1 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +8.3% | +4.1% | +7.5 | +0.1 | +0.3 | +0.4 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.36 | -8.5% | -3.0% | +0.0 | -2.4 | -3.9 | -2.1 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -2.9% | -2.9% | -0.4 | -1.9 | -0.7 | +0.0 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.28 | -10.3% | -2.9% | +0.0 | -8.1 | -1.4 | -0.8 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.58 | +4.7% | +2.7% | +0.0 | +1.2 | +2.2 | +1.2 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -2.5% | -2.5% | -1.8 | -0.8 | +0.0 | +0.1 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -2.5% | -2.5% | -0.2 | -1.4 | -0.7 | -0.2 |
| Risk: USD/INR >98 and/or reserves < US$650bn (disorderly rupee, emergency RBI response) (`EV_RUPEE_BREAK_98_RESERVE_STRESS`) | risk_scenario | 0.22 | -11.2% | -2.5% | -9.5 | -1.8 | +0.1 | -0.0 |

## Strongest causal chains (1st–4th order)
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_RECORD_OUTFLOW_26 ⇒ F_FPI_FLOWS → PRESTIGE | -6.60% | -6.60% |
| 2 | EV_CPI_REACCEL_SEP26 ⇒ F_CPI_IN → F_REPO_IN → PRESTIGE | -5.30% | -5.30% |
| 1 | EV_RBI_OCT26_HIKE25 ⇒ F_REPO_IN → PRESTIGE | -4.00% | -4.00% |
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → PRESTIGE | +7.50% | +3.75% |
| 3 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_CPI_IN → F_REPO_IN → PRESTIGE | -3.54% | -3.54% |
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_FPI_FLOWS → PRESTIGE | -1.78% | -1.78% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → PRESTIGE | -4.00% | -1.60% |
| 1 | EV_US_MIDTERMS_DEM_SWEEP ⇒ F_FPI_FLOWS → PRESTIGE | +1.50% | +1.50% |
| 3 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_GDP_IN → F_REPO_IN → PRESTIGE | +1.43% | +1.43% |
| 3 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_USDINR → F_FPI_FLOWS → PRESTIGE | -1.41% | -1.41% |
| 1 | EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26 ⇒ F_GSEC_10Y_IN → PRESTIGE | -1.40% | -1.40% |
| 3 | EV_CPI_REACCEL_SEP26 ⇒ F_CPI_IN → F_REPO_IN → F_HOUSING_DEMAND → PRESTIGE | -1.29% | -1.29% |
| 4 | EV_SWMONSOON26_DEFICIT ⇒ F_MONSOON → F_FOOD_INFLATION_IN → F_CPI_IN → F_REPO_IN → PRESTIGE | -1.29% | -1.29% |
| 2 | EV_GDP_Q1FY27_7_8 ⇒ F_GDP_IN → F_REPO_IN → PRESTIGE | -1.28% | -1.28% |
| 3 | EV_KHARIF26_OUTPUT_HIT ⇒ F_FOOD_INFLATION_IN → F_CPI_IN → F_REPO_IN → PRESTIGE | -1.27% | -1.27% |

## Analyst profile (agent research, sourced)
# Prestige Estates Projects (PRESTIGE) - profile as of 2026-11-05

## Business
Prestige is a Bengaluru-rooted, diversified developer with large residential pipelines (Bengaluru, Mumbai, NCR, Hyderabad, Chennai, Kochi) and an annuity/hospitality portfolio. It is the most leveraged name in this batch: TTM interest is Rs 1,617 crore against operating profit of Rs 3,630 crore. Q2 FY27 bookings rose 20% to Rs 7,225 crore (Business Standard, 2026-10-13) and management plans Rs 40,000 crore of launches in H2 (2026-10-20). On 2026-09-30 CPP Investments agreed to buy 27% of the hospitality arm for Rs 3,000 crore, a deleveraging step that followed the cancellation of hospitality IPO plans (2026-09-28). On 2026-11-04 Prestige acquired Gloind Vintage Infra at Rs 519 crore EV, and on 2026-10-01 the Bombay High Court set aside a MahaREAT order in the Mahalaxmi project case.

## What moves the stock
1. **Housing volumes (+5.0)** and **repo (-4.0 per +25 bp)**: higher leverage plus beta ~2 makes this the most rate-sensitive realty stock; the RBI hiked to 5.50% on 2026-10-07.
2. **FPI flows (+3.0)**, credit spreads (-1.2), G-sec (-1.0), RBI prudential norms (-0.8).
3. Bengaluru tech employment (US tech spend +0.8), premium mix (+1.5), policy (housing +1.5, capital gains -1.2), travel (+0.5), NRI (+0.4), costs (steel -0.7, cement -0.4, wages -0.4, aluminium -0.2).
Data check: DXY (+3.48 per +3%, t=2.7) and aluminium (-2.48 per +10%, t=-2.2) are significant in the pack but not mechanism-consistent in size; shrunk and flagged low.

## Transmission examples
- **Rates (4 orders)**: Middle East flare-up -> Brent up -> CPI and rupee pressure -> RBI hikes again in December -> Prestige's floating-rate debt cost rises and Bengaluru mortgage EMI up -> bookings slow while interest expense bites -> earnings and multiple (P/E 62) compress.
- **Tech cycle (4 orders)**: US tech/AI spending slows -> Bengaluru IT/GCC hiring slows -> housing demand in Whitefield/North Bengaluru softens and office leasing weakens -> pre-sales growth fades.
- **Deleveraging (3 orders)**: CPPIB closes Rs 3,000 crore hospitality deal -> net debt falls -> interest burden eases -> lower rate sensitivity.
- **Costs (3 orders)**: steel/cement up -> unsold inventory cost up -> margin cut on new launches.

## Current situation
Bookings strong, earnings volatile, debt high. The stock rose 11% in a month and trades at P/E 62; Motilal (TP Rs 1,830) sees 29% upside, but that is a sell-side view.

## Upcoming
H2 launches, CPPIB closing, Q3 results (~February 2027), Mahalaxmi litigation, December MPC.

## Bull / Bear
Bull: launches sell, hospitality proceeds cut debt, RBI pauses. Bear: more tightening hits the most levered stock; launches under-absorb; legal setbacks. Confidence medium; debt split and geographic mix are model estimates.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.