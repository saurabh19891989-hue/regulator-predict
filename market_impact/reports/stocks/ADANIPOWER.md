# ADANIPOWER — Adani Power Ltd.
*NIFTY_NEXT_50 · Power · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +0.9%**, **12 months +1.4%** (rank 24 / 37 of 200 for 3m / 12m); beta 1.00
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +30.3%): 3 months 52%, 12 months 52%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -3.1% … P90 +5.7%; plausible 12m relative-return range incl. stock-specific noise: -37.5% … +39.9%
- Decomposition (12m): 0.5 × forward event exposure +1.3% (3m +1.4%; half assumed priced; market-priced macro drift removed) + 0.5 × company-specific catalysts +2.0%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply +2.0% (beta-adjusted) vs a realised market-adjusted move of -16.6% — gap +18.5 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Indian electricity demand (`F_POWER_DEMAND_IN`) | +3 pp demand growth | +2.50 | +1.60 | +0.82 | +0.08 | +0.00 | — |
| Indian power exchange (IEX) prices (`F_POWER_PRICE_IN`) | +15% average spot power price | +2.30 | +2.30 | +0.00 | +0.00 | +0.00 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +1.99 | +1.80 | +0.13 | +0.03 | +0.04 | — |
| India 10-year G-sec yield (`F_GSEC_10Y_IN`) | +25 bp yield | -1.92 | -1.80 | -0.12 | +0.00 | +0.00 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -1.79 | +0.00 | -1.24 | -0.48 | -0.07 | — |
| Indian data-centre build-out (`T_DATA_CENTRES_IN`) | +1 | +1.65 | +1.50 | +0.06 | +0.06 | +0.02 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -1.60 | -1.20 | -0.40 | +0.01 | -0.01 | — |
| Power market / DISCOM reform (`P_POWER_REFORM`) | +1 = reform progress | +1.54 | +2.00 | -0.46 | +0.00 | +0.00 | — |
| Monsoon rainfall vs normal (`F_MONSOON`) | +10% above long-period average | -1.53 | -0.50 | -0.80 | -0.37 | +0.15 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -1.39 | -0.60 | -0.38 | -0.21 | -0.20 | -1.1% |
| Indian corporate credit spreads (`F_CREDIT_SPREADS_IN`) | +50 bp spreads | -1.21 | -1.20 | +0.00 | +0.00 | -0.01 | — |
| ENSO state (El Nino strength) (`NEW_EL_NINO`) | +1 = El Nino year (ONI >= +1.0 sustained); -1 = La Nina | +1.16 | +0.00 | +0.50 | +0.48 | +0.18 | — |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -1.16 | +0.00 | -0.74 | -0.37 | -0.04 | +3.5% |
| Renewable / transmission policy support (`P_RENEWABLE_SUPPORT`) | +1 = stronger support | -0.98 | -0.80 | -0.09 | -0.09 | +0.00 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Indian spot power: IEX prices hit Rs20/unit ceiling (19 Sep), Q2 prices up ~46% y/y; El Nino lifts demand (`EV_POWER_SPOT_SPIKE`) | occurred | 1.00 | +8.3% | +8.3% | +8.5 | -0.2 | +0.0 | +0.0 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -4.4% | -4.4% | -4.0 | -0.3 | -0.1 | -0.1 |
| Summer 2027 peak-demand shortfall / IEX at cap under super El Nino (`EV_SUMMER27_POWER_SHORTFALL`) | anticipated | 0.40 | +9.2% | +3.7% | +9.6 | -0.2 | -0.0 | -0.1 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -2.9% | -2.9% | -2.9 | +0.0 | +0.0 | -0.0 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +5.0% | +2.5% | +4.5 | +0.3 | +0.1 | +0.1 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -2.1% | -2.1% | +0.0 | -1.4 | -0.6 | -0.1 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -2.0% | -2.0% | -2.0 | +0.0 | +0.0 | -0.0 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | +1.4% | +1.4% | +1.0 | +0.6 | -0.0 | -0.1 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.25 | -5.2% | -1.3% | +0.0 | -4.7 | -0.6 | +0.0 |
| Risk: USD/INR >98 and/or reserves < US$650bn (disorderly rupee, emergency RBI response) (`EV_RUPEE_BREAK_98_RESERVE_STRESS`) | risk_scenario | 0.18 | -6.9% | -1.2% | -6.5 | -0.5 | +0.0 | +0.0 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -1.2% | -1.2% | +0.0 | -1.0 | -0.2 | +0.0 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -1.1% | -1.1% | +0.0 | -1.2 | -0.1 | +0.1 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_SUMMER27_POWER_SHORTFALL ⇒ F_POWER_PRICE_IN → ADANIPOWER | +6.90% | +2.76% |
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → ADANIPOWER | +4.50% | +2.25% |
| 1 | EV_SUMMER27_POWER_SHORTFALL ⇒ F_POWER_DEMAND_IN → ADANIPOWER | +2.40% | +0.96% |
| 1 | EV_POWER_DISTRIB_REFORM ⇒ P_POWER_REFORM → ADANIPOWER | +2.00% | +0.90% |
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → ADANIPOWER | -1.44% | -0.72% |
| 1 | EV_NUCLEAR_SHANTI_RULES_FINAL ⇒ P_POWER_REFORM → ADANIPOWER | +1.00% | +0.60% |
| 1 | EV_COAL_IMPORT_BLEND_REVIVED ⇒ F_POWER_PRICE_IN → ADANIPOWER | +1.15% | +0.57% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → ADANIPOWER | -1.20% | -0.50% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → ADANIPOWER | -2.70% | -0.49% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → ADANIPOWER | -1.73% | -0.43% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_FPI_FLOWS → ADANIPOWER | -1.73% | -0.43% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → ADANIPOWER | -1.68% | -0.42% |
| 3 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_POWER_DEMAND_IN → F_POWER_PRICE_IN → ADANIPOWER | -0.53% | -0.36% |
| 1 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → ADANIPOWER | -0.50% | -0.34% |
| 1 | EV_FERT_SUBSIDY_TOPUP_WINTER ⇒ F_GSEC_10Y_IN → ADANIPOWER | -0.36% | -0.32% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_POWER_PRICE_IN → ADANIPOWER | +1.90 | director_override | +4.37% |
| 1 | F_FPI_FLOWS → ADANIPOWER | -1.60 | events | -2.88% |
| 1 | F_GSEC_10Y_IN → ADANIPOWER | +1.55 | director_override | -2.79% |
| 1 | F_POWER_DEMAND_IN → ADANIPOWER | +1.20 | events | +1.92% |
| 1 | F_COAL_INDIA → ADANIPOWER | +1.50 | events | -1.50% |
| 1 | F_REPO_IN → ADANIPOWER | +1.00 | events | -1.20% |
| 1 | F_MONSOON → ADANIPOWER | -1.56 | events | +0.78% |
| 1 | F_CREDIT_SPREADS_IN → ADANIPOWER | +0.50 | events | -0.60% |
| 1 | C_MIDEAST_CONFLICT → ADANIPOWER | +1.00 | events | +0.50% |
| 1 | P_RENEWABLE_SUPPORT → ADANIPOWER | +0.60 | director_override | -0.48% |
| 1 | F_COAL_INTL → ADANIPOWER | +0.70 | director_override | -0.35% |
| 1 | F_USDINR → ADANIPOWER | -0.37 | observed | +0.22% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-11 | Korba Phase-II first 660 MW unit commercial operation (grid-synchronised; 'expected shortly'); second unit Q4 FY27 | capex | 0.80 | +1.1% | +0.92% |
| 2026-12 | BHEL orders formalised and further long-term PPAs signed (62% of 24 GW tied); at least one new >1 GW PPA/LoA | other | 0.60 | +1.5% | +0.90% |
| 2027-01 | Q3 FY27 results (Q2 declared 23 Oct; estimate late Jan 2027); imported-coal cost lag (Gujarat indexation) hits Q3 | results | 0.97 | -1.0% | -0.97% |
| 2027-03 | NCLT/CoC approval for GVK Energy (330 MW Alaknanda hydro) resolution plan and other CIRP acquisitions (3 GW inorganic in pipeline) | corporate_action | 0.60 | +0.9% | +0.54% |
| 2027-03 | Government extends Section 11 / imported-coal blending directions or new capacity addition target beyond 97 GW | regulatory | 0.50 | +0.8% | +0.38% |
| 2027-03 | Renewed adverse US legal-regulatory action on Adani Group | litigation | 0.05 | -12.0% | -0.60% |
| 2027-04 | Mahan Phase-II 1,600 MW COD (targeted early FY28) | capex | 0.35 | +1.5% | +0.52% |

## Analyst profile (agent research, sourced)
# ADANIPOWER — Adani Power Ltd. (as of 2026-11-05)

*Scenario/exposure analysis relative to the Nifty 200; not a validated forecast. Primary source is the Adani Power Q2 FY27 analyst-call transcript (26 Oct 2026, filed on BSE 30 Oct) plus screener.in and headline searches; the company IR site was not reachable (HTTP 403) so the press release and slides were not read. "Model knowledge" marks facts from training memory.*

## Business
Adani Power is India's largest private thermal generator, with roughly 18 GW operating and a 24 GW pipeline under construction or awarded, of which 62% already has long-term PPAs. Management targets about 45 GW by 2032 (42 GW organic plus about 3 GW of insolvency-court acquisitions). Most output is sold under long- and medium-term PPAs (23.4 of 26.4 bn units in Q2) with state discoms and Bangladesh (Godda); roughly 11-13% is merchant/short-term. Fuel is predominantly domestic linkage coal, with imported coal at Mundra-type plants. Q2 FY27 continuing revenue was Rs 17,014 cr (+29.8%) and continuing EBITDA Rs 6,321 cr (+18.5%), while reported PAT of Rs 7,019 cr (+142%) was inflated by Rs 2,422 cr of one-time prior-period revenue (Gujarat PPA energy-charge revisions). Net debt is Rs 45,846 cr, rated AA+ after an upgrade by CARE and India Ratings. Promoters hold 74.96%.

## What moves the stock
1. **Spot power prices (F_POWER_PRICE_IN +2.3).** Merchant tariffs rose 33% YoY and coal stocks at plants are at multi-year lows (96 plants critical in October, 6-7 days of stock against a 19-20 day norm per JSW's call). The merchant slice is shrinking as capacity is tied into medium-term PPAs, which cuts upside and downside.
2. **Demand and weather (F_POWER_DEMAND_IN +1.6, F_MONSOON -2.0).** Q2 demand grew 11.5% to 502 BU with a 13% monsoon deficit and a 15% fall in hydro; thermal supplied 73% of the incremental generation and Adani's PLF jumped to 70.1% from 62.8%. A normal monsoon reverses part of that.
3. **Fuel-cost pass-through (F_COAL_INTL -0.5, F_COAL_INDIA -1.0).** Imported coal landed cost is up about 50% YoY; fuel cost was 60% of continuing revenue. Gujarat PPAs are indexed with a lag of more than six months (Q3 impact), Bangladesh is passed through at once. Domestic coal prices are unchanged, but coal quality costs rose.
4. **Pipeline execution and PPA wins.** Korba-II unit 1 sync'd, Mahan-II early FY28, BHEL orders for four 2x800 MW units (4 Nov), Bhutan 770 MW JV, Alaknanda hydro via GVK.
5. **Rates, spreads and G-sec (-1.8, -1.2, -1.2)**, lower than renewable peers because net debt is only 1.8x EBITDA and capex is funded by accruals.
6. **Group sentiment and flows** (0.30 from Adani Enterprises; FPI +1.8).
Pack empirical sensitivities are weak (steel +1.95 t 1.7, coal +3.60 t 1.6); none is significant, so the weights rest on fundamentals.

## Worked transmission examples
- **Middle East escalation -> LNG supply shock and higher Brent (1st) -> Asian utilities switch to coal, seaborne coal rises (2nd) -> Adani's imported-coal fuel cost jumps; Bangladesh tariff adjusts immediately but Gujarat PPAs lag six months (3rd) -> unrecovered cost compresses margin for one to two quarters while merchant prices rise; if rupee also weakens (Brent -> INR 94.5 -> more), import cost rises further (4th).**
- **Weak monsoon -> hydro output down and cooling demand up (1st) -> thermal PLF rises, spot prices high, coal stocks critical (2nd) -> government directs imported-coal blending / captive output and raises the case for >100 GW new thermal (3rd) -> more long-term PPA tenders from states (Maharashtra 1,600 MW RTC at Raipur-III) and higher valuation for the 24 GW pipeline (4th).**
- **RBI hike on 7 Oct 2026 -> repo 5.50% and "calibrated tightening" (1st) -> MCLR and bond yields rise (2nd) -> financing cost for the Rs 1.5 lakh cr pipeline increases, PPA bids must be priced higher (3rd) -> some state tenders go to competitors with cheaper capital (NTPC, JSW) (4th).** The effect on Adani Power is smaller than on renewables because of low leverage.
- **BHEL order win -> BHEL's order book improves (1st) -> Adani's capex is locked at known prices (2nd) -> lower cost overrun risk but higher execution/timeline dependence on BHEL (3rd).** BHEL is a universe ticker; the two-way link is covered by the BHEL profile.

## Current situation
H1 FY27 continuing revenue was Rs 35,464 cr and continuing EBITDA Rs 13,304 cr (+20%); debt rose to Rs 61,860 cr from Rs 53,556 cr. Management says tariffs will have to rise to some extent because of fuel and that Q3 margins will show the Gujarat indexation lag. Stock Rs 204.5, +29% in 12 months but -11% over 6 months; Elara sees 16% upside.

## Upcoming events
Korba-II unit 1 COD, Mahan-II COD (early FY28), new PPAs for the 38% untied pipeline, GVK/Alaknanda approvals, Q3 results (late Jan 2027, estimated), and government decisions on blending or Section 11 directions. Probabilities are in `company_events`.

## Bull and bear
**Bull:** sustained double-digit demand growth and tight supply keep PLF and merchant prices high, the 24 GW pipeline commissions on time with fully tied PPAs, and governance headwinds recede. **Bear:** a normal monsoon and slower demand, imported-coal cost lag, discom payment delays or tariff re-openings, project delays and a return of group legal risk.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.