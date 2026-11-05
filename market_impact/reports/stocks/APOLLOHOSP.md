# APOLLOHOSP — Apollo Hospitals Enterprise Ltd.
*NIFTY_50 · Healthcare · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -0.4%**, **12 months -1.7%** (rank 149 / 177 of 200 for 3m / 12m); beta 0.87
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +19.5%): 3 months 48%, 12 months 46%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -7.2% … P90 +2.0%; plausible 12m relative-return range incl. stock-specific noise: -27.0% … +22.9%
- Decomposition (12m): 0.5 × forward event exposure -2.9% (3m -1.4%; half assumed priced; market-priced macro drift removed) + 0.5 × company-specific catalysts -0.0%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply -3.2% (beta-adjusted) vs a realised market-adjusted move of -0.9% — gap -2.2 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +3.15 | +3.00 | +0.13 | -0.02 | +0.04 | — |
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +2.91 | +2.50 | +0.40 | +0.05 | -0.03 | — |
| Insurance regulation tightening (IRDAI) (`P_IRDAI_REG`) | +1 = tightening | -2.50 | -2.50 | +0.00 | +0.00 | +0.00 | — |
| Consumer premiumisation (`T_PREMIUMISATION`) | +1 | +2.13 | +2.00 | +0.10 | +0.03 | +0.00 | — |
| India real GDP growth (`F_GDP_IN`) | +1 pp | +2.12 | +2.00 | +0.12 | +0.08 | -0.08 | — |
| India 10-year G-sec yield (`F_GSEC_10Y_IN`) | +25 bp yield | -2.03 | -2.00 | +0.00 | -0.01 | -0.01 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -1.82 | +0.00 | -0.47 | -0.97 | -0.37 | — |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -1.74 | -0.80 | -0.59 | -0.32 | -0.03 | +3.5% |
| Private corporate capex (`F_PRIVATE_CAPEX`) | +10% capex growth | +1.46 | +0.00 | +1.28 | +0.13 | +0.04 | — |
| Rural consumption growth (`F_RURAL_DEMAND`) | +5 pp | +1.40 | +0.00 | +1.28 | +0.06 | +0.05 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -1.30 | -0.50 | -0.38 | -0.29 | -0.13 | -1.1% |
| USD/JPY exchange rate (`NEW_USDJPY`) | +3% USD/JPY (yen weaker) | +1.26 | +0.00 | +1.04 | +0.11 | +0.11 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -1.20 | -0.60 | -0.51 | -0.07 | -0.01 | — |
| US average effective tariff rate (all partners) (`NEW_US_TARIFF_GLOBAL`) | +5 pp effective tariff rate | -1.18 | +0.00 | -0.32 | -0.67 | -0.19 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -6.9% | -6.9% | -6.6 | -0.3 | +0.0 | -0.1 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +8.2% | +4.1% | +7.8 | +0.3 | -0.0 | +0.1 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -2.9% | -2.9% | -2.8 | +0.0 | -0.1 | -0.0 |
| US midterms (3 Nov 2026): Democrats win House and Senate (`EV_US_MIDTERMS_DEM_SWEEP`) | occurred | 1.00 | +1.7% | +1.7% | +1.5 | +0.2 | -0.0 | +0.0 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.25 | -6.6% | -1.7% | -2.0 | -4.4 | -0.4 | +0.1 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -1.5% | -1.5% | +0.0 | -1.3 | -0.2 | -0.0 |
| India Q1 FY27 GDP grows 7.8% (31 Aug 2026), beating ~7.3% consensus (`EV_GDP_Q1FY27_7_8`) | occurred | 1.00 | +1.5% | +1.5% | +1.5 | +0.1 | -0.0 | -0.0 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -1.5% | -1.5% | -1.2 | -0.1 | -0.1 | -0.0 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -1.5% | -1.5% | +0.0 | -1.6 | +0.1 | +0.1 |
| Risk: USD/INR >98 and/or reserves < US$650bn (disorderly rupee, emergency RBI response) (`EV_RUPEE_BREAK_98_RESERVE_STRESS`) | risk_scenario | 0.18 | -8.0% | -1.4% | -7.8 | +0.1 | -0.3 | -0.0 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.55 | +2.4% | +1.3% | +0.3 | +1.4 | +0.4 | +0.2 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -1.2% | -1.2% | +0.0 | -0.7 | -0.2 | -0.3 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → APOLLOHOSP | +7.50% | +3.75% |
| 1 | EV_IRDAI_COMMISSION_RESET ⇒ P_IRDAI_REG → APOLLOHOSP | -1.75% | -0.88% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → APOLLOHOSP | -4.50% | -0.81% |
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → APOLLOHOSP | -1.60% | -0.80% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → APOLLOHOSP | -2.88% | -0.72% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_FPI_FLOWS → APOLLOHOSP | -2.88% | -0.72% |
| 1 | EV_BUDGET_FY28_LTCG_RELIEF ⇒ F_FPI_FLOWS → APOLLOHOSP | +1.50% | +0.52% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → APOLLOHOSP | -2.00% | -0.50% |
| 1 | EV_Q2_FY27_GDP_STRONG ⇒ F_FPI_FLOWS → APOLLOHOSP | +0.60% | +0.48% |
| 2 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_GDP_IN → APOLLOHOSP | +0.53% | +0.36% |
| 1 | EV_FERT_SUBSIDY_TOPUP_WINTER ⇒ F_GSEC_10Y_IN → APOLLOHOSP | -0.40% | -0.36% |
| 1 | EV_CPI_BREACH_6PCT ⇒ F_GSEC_10Y_IN → APOLLOHOSP | -0.60% | -0.36% |
| 1 | EV_BANKING_LIQUIDITY_DEFICIT_MAR27 ⇒ F_GSEC_10Y_IN → APOLLOHOSP | -0.60% | -0.36% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_GSEC_10Y_IN → APOLLOHOSP | -2.00% | -0.36% |
| 1 | EV_INDIA_STAGFLATION_SCARE ⇒ F_GDP_IN → APOLLOHOSP | -3.00% | -0.36% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_FPI_FLOWS → APOLLOHOSP | -1.60 | events | -4.80% |
| 1 | F_GSEC_10Y_IN → APOLLOHOSP | +1.55 | director_override | -3.10% |
| 1 | F_GDP_IN → APOLLOHOSP | +0.50 | events | +1.00% |
| 1 | F_REPO_IN → APOLLOHOSP | +1.00 | events | -0.60% |
| 1 | F_CPI_IN → APOLLOHOSP | +1.15 | events | +0.57% |
| 1 | F_URBAN_DEMAND → APOLLOHOSP | +0.20 | events | +0.50% |
| 1 | F_GAS_GLOBAL → APOLLOHOSP | +1.00 | director_override | -0.30% |
| 1 | F_USDINR → APOLLOHOSP | -0.37 | observed | +0.18% |
| 1 | F_RISK_SENTIMENT → APOLLOHOSP | +0.11 | observed | -0.09% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-12 | Composite scheme of arrangement among four group entities: NCLT order received 2026-11-04 (creditor nod 2026-10-30); effective date/filings | corporate_action | 0.85 | +1.0% | +0.85% |
| 2027-02 | Q3 FY27 results: occupancy, ARPOB, pharmacy margin, expansion cost drag | results | 0.95 | +0.0% | +0.00% |
| 2027-03 | IRDAI / insurer cashless tariff negotiations or hospital-insurer dispute | regulatory | 0.30 | -3.0% | -0.90% |
| 2027-06 | New hospital/bed commissioning and expansion cost absorption (Reuters: expansion costs cloud results) | capex | 0.70 | +0.0% | +0.00% |

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