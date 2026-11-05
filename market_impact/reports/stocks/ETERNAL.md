# ETERNAL — Eternal Ltd.
*NIFTY_50 · Consumer Services · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -5.2%**, **12 months -10.9%** (rank 194 / 196 of 200 for 3m / 12m); beta 1.05
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +26.8%): 3 months 35%, 12 months 42%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -20.0% … P90 -5.4%; plausible 12m relative-return range incl. stock-specific noise: -36.8% … +33.1%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves -2.6 pp (model impact -5.1% beta-adjusted vs realised market-adjusted move +39.0%); forward event exposure -14.3% (3m -6.6%; half assumed priced); company-specific events -0.0%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Quick-commerce disruption of retail/FMCG distribution (`T_QUICK_COMMERCE`) | +1 | +8.00 | +8.00 | +0.00 | +0.00 | +0.00 | — |
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +5.80 | +6.00 | +0.00 | -0.12 | -0.09 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -4.29 | +0.00 | -3.94 | -0.18 | -0.16 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -4.27 | +0.00 | -1.76 | -1.06 | -1.45 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +3.66 | +3.50 | +0.05 | +0.03 | +0.08 | — |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -3.65 | -2.50 | -0.68 | -0.39 | -0.07 | +3.5% |
| US equity market (`F_US_EQUITIES`) | +5% S&P 500 | +3.13 | +0.00 | +2.32 | +0.67 | +0.14 | +1.2% |
| FDI liberalisation (`P_FDI_RULES`) | +1 = liberalisation | -2.89 | -3.00 | +0.02 | +0.06 | +0.03 | — |
| Labour code implementation cost (`P_LABOUR_CODES`) | +1 = implementation | -2.85 | -3.00 | +0.00 | +0.20 | -0.05 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -2.81 | -2.50 | -0.22 | -0.05 | -0.04 | — |
| US average effective tariff rate (all partners) (`NEW_US_TARIFF_GLOBAL`) | +5 pp effective tariff rate | -2.66 | +0.00 | -1.00 | -1.08 | -0.59 | — |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +2.65 | +0.00 | +1.68 | +1.03 | -0.07 | — |
| USD/JPY exchange rate (`NEW_USDJPY`) | +3% USD/JPY (yen weaker) | +2.38 | +0.00 | +1.84 | +0.28 | +0.25 | — |
| US dollar index (`F_DXY`) | +3% DXY | -2.19 | +0.00 | -1.66 | -0.38 | -0.15 | +2.2% |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -10.7% | -10.7% | -4.0 | -2.6 | -3.1 | -1.0 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -9.1% | -9.1% | -8.7 | -0.1 | -0.1 | -0.2 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -5.5% | -5.5% | -0.6 | -4.5 | -0.2 | -0.2 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +10.2% | +5.1% | +9.8 | +0.1 | +0.1 | +0.2 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.28 | -16.3% | -4.6% | -10.0 | -6.1 | -0.3 | +0.1 |
| Disorderly yen carry-trade unwind (Aug-2024-style) after BoJ/MoF action (`EV_YEN_CARRY_UNWIND_RISK`) | risk_scenario | 0.18 | -20.4% | -3.7% | -12.5 | -7.6 | -0.1 | -0.2 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.36 | -8.7% | -3.1% | -5.0 | -1.5 | -1.7 | -0.5 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -2.9% | -2.9% | -2.5 | -0.2 | -0.1 | -0.1 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.58 | +4.5% | +2.6% | +2.5 | +0.8 | +1.0 | +0.3 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -2.3% | -2.3% | +0.0 | -2.4 | +0.0 | +0.1 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -2.2% | -2.2% | +0.0 | -1.5 | -0.5 | -0.2 |
| Labour codes: states finalise rules (deadline 31 Oct 2026), wider operational rollout (`EV_LABOUR_CODES_RULES`) | anticipated | 0.80 | -2.7% | -2.1% | -3.0 | +0.6 | -0.2 | -0.1 |

## Strongest causal chains (1st–4th order)
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_RECORD_OUTFLOW_26 ⇒ F_FPI_FLOWS → ETERNAL | -7.70% | -7.70% |
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → ETERNAL | +8.75% | +4.38% |
| 1 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → ETERNAL | -3.96% | -3.96% |
| 2 | EV_CPI_REACCEL_SEP26 ⇒ F_CPI_IN → F_REPO_IN → ETERNAL | -3.31% | -3.31% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → ETERNAL | -10.00% | -2.80% |
| 1 | EV_RBI_OCT26_HIKE25 ⇒ F_REPO_IN → ETERNAL | -2.50% | -2.50% |
| 1 | EV_LABOUR_CODES_RULES ⇒ P_LABOUR_CODES → ETERNAL | -3.00% | -2.40% |
| 1 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → ETERNAL | -12.50% | -2.25% |
| 1 | EV_US_MIDTERMS_DEM_SWEEP ⇒ F_FPI_FLOWS → ETERNAL | +1.75% | +1.75% |
| 1 | EV_CHINA_FDI_EASING_PN3 ⇒ P_FDI_RULES → ETERNAL | -2.10% | -1.47% |
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ C_MIDEAST_CONFLICT → F_RISK_SENTIMENT → ETERNAL | -1.20% | -1.20% |
| 1 | EV_GDP_Q1FY27_7_8 ⇒ F_URBAN_DEMAND → ETERNAL | +1.20% | +1.20% |
| 2 | EV_UST_SELLOFF_SEP26 ⇒ F_US_10Y → F_FPI_FLOWS → ETERNAL | -1.19% | -1.19% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → ETERNAL | -5.25% | -1.16% |
| 2 | EV_UST_SELLOFF_SEP26 ⇒ F_DXY → F_FPI_FLOWS → ETERNAL | -1.12% | -1.12% |

## Analyst profile (agent research, sourced)
# ETERNAL — Eternal Ltd. (Zomato, Blinkit, Hyperpure, District), as of 2026-11-05

*Sources: screener.in pack and Google News headlines (Oct 2026); bodies not retrieved. Model knowledge is labelled.*

## Business
Eternal runs Zomato food delivery and dining, Blinkit quick commerce (now inventory-led, which inflated reported revenue to Rs 24,138 cr in Q2 FY27, +78% y/y), Hyperpure and District. Operating profit was Rs 752 cr (3.1% of revenue) and PAT Rs 125 cr (+92%), a miss vs estimates (Moneycontrol, 21 Oct). Market cap Rs 3.44 lakh cr, P/E ~700, FIIs 33%.

## What moves the stock (ranked)
1. Blinkit/quick-commerce growth and store roll-out (T_QUICK_COMMERCE, +8 per unit); management targets 3,500 stores near term and 5,000 by FY28 (CIOL, 22 Oct).
2. Urban demand (F_URBAN_DEMAND +6 per +5pp).
3. Discount rate and risk appetite (F_REPO_IN -2.5, F_RISK_SENTIMENT -2.5) because earnings are tiny relative to price.
4. FPI flows (+3.5).
5. Labour codes (gig-worker contributions, -3) and FDI/competition rules (-3).
6. Fuel for riders (-0.8).

## Transmission examples
- **Brent up** -> petrol cost for ~half the riders -> payouts rise, partly passed to customers -> delivery fee/AOV rise -> food-delivery frequency softens (2nd) -> adjusted EBITDA margin dips 20-40 bp (3rd) -> equity -0.8 per +10%.
- **Middle East escalation** -> Brent and risk-off VIX up -> FPIs sell India growth names -> 33% FII-held Eternal falls with beta >1 (2nd) -> funding for rivals (Swiggy, Zepto) tightens, which may relieve Eternal's competitive pressure (3rd/4th), a partial offset.
- **RBI holds rates after INR depreciation** -> real yields up -> long-duration discount rate up -> multiple compresses.
- **Swiggy retrenchment** (Swiggy -17% on Instamart losses, 23 Oct) -> less subsidy competition -> Blinkit share gains -> unit economics improve (positive, company-specific).

## Current situation
Q2 results on 21 Oct: stock fell 3.5% then recovered next day with brokerages bullish despite EBITDA miss. Goldman sold Rs 169 cr in a block (16 Oct) but also expects ~16% upside (29 Sep). Stock sits at its 52-week high (Rs 357), +38.6% in 6 months.

## Upcoming
Q3 FY27 results (~21 Jan 2027), gig-worker rule implementation (~Mar 2027, 30%), store milestones.

## Bull / bear
Bull: Blinkit adjusted margins reach target, Swiggy's pullback consolidates share, FPI inflows continue. Bear: price war from Zepto/Amazon/Flipkart, labour-code costs, rates up, multiple compression from 700x P/E.

## Uncertainties
Revenue mix is approximate, the Blinkit profit metric is headline-quoted, and empirical links (edible oil -4.4, t -2.9) have no clear mechanism.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.