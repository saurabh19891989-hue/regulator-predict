# APOLLOHOSP — Apollo Hospitals Enterprise Ltd.
*NIFTY_50 · Healthcare · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -1.8%**, **12 months -4.0%** (rank 150 / 151 of 200 for 3m / 12m); beta 0.87
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +19.5%): 3 months 43%, 12 months 38%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -10.7% … P90 +1.2%; plausible 12m relative-return range incl. stock-specific noise: -34.3% … +22.8%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves -1.0 pp (model impact -2.9% beta-adjusted vs realised market-adjusted move -0.9%); forward event exposure -3.7% (3m -1.7%; half assumed priced); company-specific events -0.0%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +3.18 | +3.00 | +0.13 | -0.02 | +0.07 | — |
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +2.81 | +2.50 | +0.40 | +0.00 | -0.10 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -2.68 | +0.00 | -0.47 | -1.21 | -1.00 | — |
| Insurance regulation tightening (IRDAI) (`P_IRDAI_REG`) | +1 = tightening | -2.50 | -2.50 | +0.00 | +0.00 | +0.00 | — |
| Consumer premiumisation (`T_PREMIUMISATION`) | +1 | +2.13 | +2.00 | +0.10 | +0.03 | -0.00 | — |
| US equity market (`F_US_EQUITIES`) | +5% S&P 500 | +2.07 | +0.00 | +1.34 | +0.63 | +0.09 | +1.2% |
| India 10-year G-sec yield (`F_GSEC_10Y_IN`) | +25 bp yield | -2.05 | -2.00 | +0.00 | -0.04 | -0.02 | — |
| US dollar index (`F_DXY`) | +3% DXY | -1.88 | +0.00 | -1.44 | -0.29 | -0.15 | +2.2% |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -1.78 | -0.80 | -0.59 | -0.34 | -0.05 | +3.5% |
| Brent crude oil price (`F_BRENT`) | +10% Brent | -1.76 | +0.00 | -0.77 | -0.59 | -0.41 | +0.0% |
| India real GDP growth (`F_GDP_IN`) | +1 pp | +1.76 | +2.00 | +0.01 | -0.12 | -0.13 | — |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +1.69 | +0.00 | +0.56 | +0.85 | +0.28 | — |
| US average effective tariff rate (all partners) (`NEW_US_TARIFF_GLOBAL`) | +5 pp effective tariff rate | -1.62 | +0.00 | -0.32 | -0.89 | -0.41 | — |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -1.62 | +0.00 | +0.29 | -1.25 | -0.67 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -10.5% | -10.5% | +0.0 | -4.5 | -3.4 | -2.5 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -7.3% | -7.3% | -6.9 | -0.3 | +0.0 | -0.2 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +8.3% | +4.1% | +7.8 | +0.3 | -0.0 | +0.2 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -3.1% | -3.1% | +0.0 | -3.0 | -0.1 | +0.0 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -2.9% | -2.9% | -2.8 | +0.0 | -0.1 | -0.0 |
| Gold and silver slump from January 2026 peaks (silver -53%, gold -24%) (`EV_PRECIOUS_METALS_CRASH_2026`) | occurred | 1.00 | -2.7% | -2.7% | +0.0 | -2.7 | +0.0 | +0.0 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.28 | -9.0% | -2.5% | -3.2 | -5.2 | -0.8 | +0.2 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.36 | -6.8% | -2.4% | -1.3 | -2.4 | -1.9 | -1.3 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.58 | +3.9% | +2.3% | +0.4 | +1.7 | +1.0 | +0.8 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -2.2% | -2.2% | +0.0 | -1.5 | -0.4 | -0.2 |
| Disorderly yen carry-trade unwind (Aug-2024-style) after BoJ/MoF action (`EV_YEN_CARRY_UNWIND_RISK`) | risk_scenario | 0.18 | -10.9% | -2.0% | -4.0 | -6.5 | -0.4 | +0.1 |
| Risk: USD/INR >98 and/or reserves < US$650bn (disorderly rupee, emergency RBI response) (`EV_RUPEE_BREAK_98_RESERVE_STRESS`) | risk_scenario | 0.22 | -8.0% | -1.8% | -7.8 | +0.1 | -0.3 | -0.0 |

## Strongest causal chains (1st–4th order)
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_RECORD_OUTFLOW_26 ⇒ F_FPI_FLOWS → APOLLOHOSP | -6.60% | -6.60% |
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → APOLLOHOSP | +7.50% | +3.75% |
| 1 | EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26 ⇒ F_GSEC_10Y_IN → APOLLOHOSP | -2.80% | -2.80% |
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_FPI_FLOWS → APOLLOHOSP | -1.78% | -1.78% |
| 1 | EV_US_MIDTERMS_DEM_SWEEP ⇒ F_FPI_FLOWS → APOLLOHOSP | +1.50% | +1.50% |
| 3 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_USDINR → F_FPI_FLOWS → APOLLOHOSP | -1.41% | -1.41% |
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_GDP_IN → APOLLOHOSP | -1.19% | -1.19% |
| 2 | EV_UST_SELLOFF_SEP26 ⇒ F_US_10Y → F_FPI_FLOWS → APOLLOHOSP | -1.02% | -1.02% |
| 1 | EV_GDP_Q1FY27_7_8 ⇒ F_GDP_IN → APOLLOHOSP | +1.00% | +1.00% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → APOLLOHOSP | -4.50% | -0.99% |
| 2 | EV_UST_SELLOFF_SEP26 ⇒ F_DXY → F_FPI_FLOWS → APOLLOHOSP | -0.96% | -0.96% |
| 2 | EV_PRECIOUS_METALS_CRASH_2026 ⇒ F_DXY → F_FPI_FLOWS → APOLLOHOSP | -0.92% | -0.92% |
| 2 | EV_PRECIOUS_METALS_CRASH_2026 ⇒ F_US_10Y → F_FPI_FLOWS → APOLLOHOSP | -0.90% | -0.90% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → APOLLOHOSP | -3.20% | -0.90% |
| 2 | EV_UST_SELLOFF_SEP26 ⇒ F_US_10Y → F_GSEC_10Y_IN → APOLLOHOSP | -0.88% | -0.88% |

## Analyst profile (agent research, sourced)
# APOLLOHOSP - Apollo Hospitals Enterprise Ltd. (Nifty 50, hospitals)

## Business
Apollo Hospitals runs India's largest private hospital network and, through Apollo HealthCo, a large pharmacy distribution/retail and digital (24/7) business, plus diagnostics and primary-care clinics. Hospitals are roughly half of revenue and the large majority of EBITDA (segment splits are model estimates; a primary segment disclosure was not retrieved). TTM revenue is Rs 27,630 cr with a 15% EBITDA margin and Rs 2,338 cr PAT. Q2 FY27: revenue Rs 7,615 cr (+23%), operating profit Rs 1,191 cr, PAT Rs 660 cr.

## What moves the stock, ranked
1. **Valuation/discount rate and flows (P/E 53; G-sec -2.0, FPI +3.0).** FIIs hold 43% and added in Sep 2026. A growth stock with P/B 11 trades on the cost of equity more than quarterly noise.
2. **Hospital volumes and mix (urban demand +2.5, GDP +2.0, premiumisation +2.0).**
3. **Costs: doctor/employee wages (-1.3) and expansion pre-operative costs.** Reuters (2026-11-05) ties the share fall to expansion costs.
4. **Payer and regulatory risk (IRDAI -2.5, drug price control -1.0).**
5. **Corporate restructuring:** NCLT order (2026-11-04) on a composite scheme with four entities; creditors approved on 2026-10-30. Impact depends on structure (details not retrieved).
6. **Rates (repo -0.6) and FX (-0.5).**

## Transmission examples
- **Oil/Middle East shock -> inflation up -> RBI hikes (repo 5.50% on 2026-10-07) -> bond yields up -> discount rate on 50x multiple.** Brent +10% (1st) -> CPI +0.3pp (2nd) -> more RBI tightening, G-sec +25bp (3rd) -> Apollo -2% on rates alone (4th), while the CPI also lets hospital tariffs rise 4-6%.
- **Insurer-hospital cashless dispute -> IRDAI/insurer pressure on package rates -> hospital ARPOB growth falls 1-2pp -> EBITDA -5-9% -> read-across to Max/Fortis, as on 2026-09-30 when hospital stocks fell up to 7%.**
- **Wage inflation (doctor and nurse shortages) -> employee cost +2pp -> margin -40bp -> partially offset via tariff.**
- **Higher FPI inflows after the US midterm result -> large-cap healthcare re-rating:** F_US_EQUITIES up -> F_FPI_FLOWS -> Apollo +3%.
- **Weak rupee -> imported implants and equipment costlier, but international patient revenue (GCC, Africa) rises in INR; net slightly negative.**

## Current situation
Strong results (revenue +23%, PAT +34%) but margins stalled near 16% because new beds are in ramp-up. Stock Rs 8,356, 12m +7%, 3m -6.9%, 1m +5.6%. Promoter 28.0%.

## Upcoming events
Q3 FY27 results (Feb 2027), implementation of the NCLT-approved scheme (est. by early 2027), bed additions, insurer tariff negotiations.

## Bull and bear
**Bull:** consistent 15-20% growth, margin upside as new capacity matures, restructuring unlocks value, strong FII demand. **Bear:** 53x earnings, expansion costs, regulatory tariff caps, pharmacy dilution, rate hikes. Confidence medium: exposures are mechanistic with limited company-disclosed numbers.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.