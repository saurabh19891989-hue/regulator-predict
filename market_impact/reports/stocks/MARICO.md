# MARICO — Marico Ltd.
*MIDCAP_100 · Fast Moving Consumer Goods · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -0.3%**, **12 months -0.2%** (rank 108 / 108 of 200 for 3m / 12m); beta 0.72
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +16.0%): 3 months 49%, 12 months 50%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -1.9% … P90 +1.3%; plausible 12m relative-return range incl. stock-specific noise: -18.0% … +17.6%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves -0.1 pp (model impact -0.1% beta-adjusted vs realised market-adjusted move +6.9%); forward event exposure +1.7% (3m +0.6%; half assumed priced); company-specific events +0.5%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Copra / coconut oil price (`NEW_COPRA_COCONUT_OIL`) | +15% copra price | -3.80 | -3.80 | +0.00 | +0.00 | +0.00 | — |
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | +1.80 | +2.00 | +0.00 | -0.16 | -0.04 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -1.49 | +0.00 | -1.49 | +0.01 | -0.01 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -1.28 | -1.20 | -0.06 | -0.01 | +0.00 | — |
| Palm / edible oil price (`F_EDIBLE_OIL`) | +10% edible oils | -1.19 | -1.10 | +0.00 | -0.01 | -0.08 | +1.9% |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -1.18 | +0.00 | -0.48 | -0.19 | -0.51 | — |
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +1.10 | +1.20 | +0.00 | -0.10 | +0.00 | — |
| Consumer premiumisation (`T_PREMIUMISATION`) | +1 | +1.04 | +1.00 | +0.05 | +0.00 | -0.01 | — |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -0.95 | +0.00 | -0.16 | -0.82 | +0.03 | — |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +0.93 | +0.00 | +0.66 | +0.39 | -0.11 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +0.81 | +0.80 | -0.04 | +0.02 | +0.03 | — |
| Packaging cost (paper, plastics) (`F_PACKAGING`) | +10% packaging cost | -0.80 | -0.80 | +0.00 | +0.00 | +0.00 | — |
| Russia-Ukraine war / Western sanctions intensity on Russia (`NEW_RUSSIA_UKRAINE_WAR`) | +1 = escalation (new sanctions round, strikes on energy/port infrastructure); -1 = ceasefire/sanctions relief | -0.77 | +0.00 | -0.51 | -0.08 | -0.18 | — |
| Monsoon rainfall vs normal (`F_MONSOON`) | +10% above long-period average | +0.73 | +0.00 | +0.45 | -0.04 | +0.31 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -3.6% | -3.6% | -2.0 | -0.3 | -1.1 | -0.2 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -1.9% | -1.9% | +0.0 | -1.9 | +0.0 | +0.0 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -1.8% | -1.8% | -1.8 | +0.1 | -0.0 | -0.1 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -1.3% | -1.3% | -1.2 | -0.1 | -0.0 | -0.0 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +2.0% | +1.0% | +2.0 | -0.1 | +0.0 | +0.1 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -0.9% | -0.9% | +0.0 | -0.6 | +0.0 | -0.4 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.36 | -2.2% | -0.8% | -1.0 | -0.4 | -0.7 | -0.1 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.58 | +1.3% | +0.7% | +0.6 | +0.2 | +0.4 | +0.1 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.28 | -1.9% | -0.5% | +0.0 | -1.8 | +0.0 | -0.1 |
| Rural demand indicators mixed: tractor volumes dip in Oct, 2W festive sales firm, rural CPI above urban, rural jobs scheme person-days down (`EV_RURAL_DEMAND_SOFT26`) | occurred | 1.00 | -0.5% | -0.5% | -0.6 | +0.0 | +0.0 | +0.0 |
| RBI MPC Dec 2026 (~4 Dec): hikes repo another 25 bp to 5.75% (`EV_RBI_DEC26_HIKE25`) | scheduled | 0.40 | -1.3% | -0.5% | -1.2 | -0.1 | -0.0 | -0.0 |
| US waives Russia-oil secondary sanctions/100% tariff threat on buyers incl. India (17 Oct) (`EV_RUSSIA_WAIVER_OCT17`) | occurred | 1.00 | +0.5% | +0.5% | +0.0 | +0.2 | +0.0 | +0.2 |

## Strongest causal chains (1st–4th order)
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → MARICO | -1.98% | -1.98% |
| 1 | EV_FPI_RECORD_OUTFLOW_26 ⇒ F_FPI_FLOWS → MARICO | -1.76% | -1.76% |
| 2 | EV_CPI_REACCEL_SEP26 ⇒ F_CPI_IN → F_REPO_IN → MARICO | -1.59% | -1.59% |
| 1 | EV_RBI_OCT26_HIKE25 ⇒ F_REPO_IN → MARICO | -1.20% | -1.20% |
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → MARICO | +2.00% | +1.00% |
| 1 | EV_RURAL_DEMAND_SOFT26 ⇒ F_RURAL_DEMAND → MARICO | -0.60% | -0.60% |
| 2 | EV_SWMONSOON26_DEFICIT ⇒ F_MONSOON → F_RURAL_DEMAND → MARICO | -0.57% | -0.57% |
| 3 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_CPI_IN → F_REPO_IN → MARICO | -0.53% | -0.53% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → MARICO | -1.20% | -0.48% |
| 1 | EV_BUDGET27_AGRI_RURAL ⇒ F_RURAL_DEMAND → MARICO | +0.60% | +0.42% |
| 1 | EV_US_MIDTERMS_DEM_SWEEP ⇒ F_FPI_FLOWS → MARICO | +0.40% | +0.40% |
| 4 | EV_SWMONSOON26_DEFICIT ⇒ F_MONSOON → F_FOOD_INFLATION_IN → F_CPI_IN → F_REPO_IN → MARICO | -0.39% | -0.39% |
| 2 | EV_GDP_Q1FY27_7_8 ⇒ F_GDP_IN → F_REPO_IN → MARICO | -0.38% | -0.38% |
| 3 | EV_KHARIF26_OUTPUT_HIT ⇒ F_FOOD_INFLATION_IN → F_CPI_IN → F_REPO_IN → MARICO | -0.38% | -0.38% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → MARICO | -1.00% | -0.36% |

## Analyst profile (agent research, sourced)
# Marico — what moves the stock

**Business.** Marico sells Parachute coconut oil (~60% of the branded market), Saffola edible oils/foods, value-added hair oils and digital-first brands, with about a quarter of sales abroad. Copra (dried coconut) is the biggest cost line at roughly 28% of costs (approximate, model knowledge), so profit swings with copra before pricing catches up. Q2 FY27 (Sep 2026): sales Rs 2,722 cr (+12%), operating margin 18% (13% in the March quarter), Parachute volume growth a 22-quarter high, FY27 guidance raised (screener.in; Zee Business, Economic Times, 2 to 3 Nov 2026).

## Ranked drivers
1. **Copra/coconut oil prices.** About -3.8% equity value per +15% copra. Copra is down ~35% from peak, the reason margins are rebuilding.
2. **Rural demand.** Rural volume rebound lifted Q2; a weak monsoon is the key risk.
3. **Vegetable oil and crude-linked inputs.** Saffola's oils and paraffin/packaging carry cost risk.
4. **Valuation and rates.** The stock is near its 52-week high at ~60x earnings.
5. **International currencies and demand.**

## Worked transmission chains
- **Copra falls -> Marico cuts Parachute price/ raises packs -> volumes rebound against regional brands -> operating leverage lifts margin -> guidance upgrade (3rd order).** This is the exact sequence of Q2.
- **Middle East escalation -> Brent up -> HDPE and paraffin costs up -> hair-oil gross margin down; Brent up -> INR weaker -> RBI holds -> multiples stay compressed (4th order).**
- **Weak monsoon -> coconut-belt rainfall and rural incomes -> copra supply tightens or demand weakens -> Parachute price/volume trade-off swings.**
- **Edible-oil import duty cut (24 Sep) -> Saffola oils cheaper -> Saffola margin recovers within a quarter.**

## Current situation
Management raised FY27 growth and EBITDA-margin guidance (Economic Times 2026-11-04; exact figures not retrieved). Livemint (2026-11-03) asks whether gains persist beyond the copra windfall. The Plix buyout adds digital-first exposure. A discrepancy exists between screener net profit (Rs 683 cr incl. other income Rs 330 cr) and press-reported PAT (Rs 550 cr).

## Upcoming
Q3 business update (early Jan 2027), copra price path, Plix integration.

## Bull / bear
**Bull:** copra stays low, rural rebound, foods and digital scale. **Bear:** copra reflation, valuation de-rating, weak monsoon. Cost shares are approximate.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.