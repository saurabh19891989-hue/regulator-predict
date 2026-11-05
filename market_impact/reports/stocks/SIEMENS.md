# SIEMENS — Siemens Ltd.
*NIFTY_NEXT_50 · Capital Goods · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +1.9%**, **12 months +4.3%** (rank 40 / 34 of 200 for 3m / 12m); beta 1.24
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +25.0%): 3 months 56%, 12 months 80%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 +0.4% … P90 +5.2%; plausible 12m relative-return range incl. stock-specific noise: -4.0% … +35.8%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +3.9 pp (model impact +7.8% beta-adjusted vs realised market-adjusted move -13.1%); forward event exposure +2.5% (3m +1.0%; half assumed priced); company-specific events +0.5%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Private corporate capex (`F_PRIVATE_CAPEX`) | +10% capex growth | +4.11 | +4.50 | +0.00 | -0.38 | -0.01 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -2.91 | +0.00 | -2.60 | -0.24 | -0.07 | — |
| China+1 manufacturing relocation to India (`T_CHINA_PLUS_ONE`) | +1 | +2.74 | +2.50 | +0.24 | +0.01 | -0.01 | — |
| Central + state government capex (`F_GOVT_CAPEX`) | +10% capex growth | +2.67 | +2.50 | +0.36 | -0.06 | -0.13 | — |
| Indian data-centre build-out (`T_DATA_CENTRES_IN`) | +1 | +2.61 | +2.50 | +0.13 | +0.00 | -0.02 | — |
| Railway capex (`P_RAILWAY_CAPEX`) | +10% | +2.15 | +2.00 | +0.12 | +0.03 | -0.01 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -2.13 | -2.00 | -0.08 | -0.01 | -0.04 | — |
| Power/T&D equipment capacity additions vs demand (pricing pressure) (`NEW_POWER_EQUIP_CAPACITY`) | +1 = peer capacity additions outpace demand enough to cut order pricing/margins ~100 bp | -2.00 | -2.00 | +0.00 | +0.00 | +0.00 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -1.97 | -1.50 | -0.16 | -0.23 | -0.08 | -1.1% |
| US equity market (`F_US_EQUITIES`) | +5% S&P 500 | +1.82 | +1.50 | +0.19 | +0.09 | +0.04 | +1.2% |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -1.69 | +0.00 | -0.26 | -0.79 | -0.65 | — |
| Production-linked incentive schemes (`P_PLI`) | +1 = expansion/disbursement | +1.62 | +1.00 | +0.58 | +0.07 | -0.03 | — |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -1.55 | +0.00 | +0.00 | -1.43 | -0.12 | — |
| Global AI / data-centre capex (`F_AI_CAPEX`) | +10% growth | +1.38 | +0.00 | +1.02 | +0.32 | +0.04 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Union Budget 2027-28 capex/railway allocation (infra, railways, defence) (`EV_BUDGET27_CAPEX_RAILWAY`) | scheduled | 0.90 | +3.7% | +3.4% | +3.6 | +0.3 | -0.1 | -0.1 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -3.3% | -3.3% | +0.0 | -3.0 | -0.3 | -0.1 |
| India Q1 FY27 GDP grows 7.8% (31 Aug 2026), beating ~7.3% consensus (`EV_GDP_Q1FY27_7_8`) | occurred | 1.00 | +2.4% | +2.4% | +2.5 | +0.2 | -0.2 | -0.1 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.25 | -9.2% | -2.3% | -6.5 | -2.0 | -0.6 | -0.0 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -2.2% | -2.2% | -2.0 | -0.2 | +0.0 | -0.0 |
| China+1 momentum: Apple/Foxconn/Tata iPhone 18 Pro export ramp, India ~50% of US smartphone imports, PLI round 4 (textiles) and component schemes (`EV_CHINA_PLUS_ONE_ELECTRONICS`) | anticipated | 0.80 | +2.0% | +1.6% | +1.8 | +0.2 | +0.0 | -0.0 |
| US Q3 data: GDP 3.4%, CPI 3.7%, September payrolls only +29k (`EV_US_Q3_DATA_MIXED`) | occurred | 1.00 | +1.6% | +1.6% | +0.0 | +1.4 | +0.2 | -0.0 |
| US recession (two negative quarters or NBER-style) beginning by mid-2027 (`EV_US_RECESSION_RISK_2027`) | risk_scenario | 0.25 | -5.0% | -1.3% | -4.5 | -0.7 | +0.1 | +0.1 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.55 | +2.0% | +1.1% | +0.3 | +0.8 | +0.7 | +0.3 |
| AI/tech selloff and capex-forecast pause (Oct 2026) (`EV_AI_SELLOFF_OCT26`) | occurred | 1.00 | -1.1% | -1.1% | -0.8 | -0.2 | -0.1 | -0.0 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -1.1% | -1.1% | +0.0 | -0.8 | -0.3 | -0.0 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.25 | -3.9% | -1.0% | -0.8 | -1.5 | -1.2 | -0.5 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → SIEMENS | +2.00% | +1.80% |
| 1 | EV_BUDGET27_CAPEX_RAILWAY ⇒ P_RAILWAY_CAPEX → SIEMENS | +1.60% | +1.44% |
| 1 | EV_CHINA_PLUS_ONE_ELECTRONICS ⇒ T_CHINA_PLUS_ONE → SIEMENS | +1.50% | +1.20% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → SIEMENS | -4.50% | -1.12% |
| 1 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → SIEMENS | -4.50% | -1.12% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → SIEMENS | -2.00% | -0.84% |
| 2 | EV_PULSES_VEG_SPIKE_WINTER ⇒ F_CPI_IN → F_REPO_IN → SIEMENS | -2.30% | -0.58% |
| 1 | EV_RBI_FEB27_HIKE25 ⇒ F_REPO_IN → SIEMENS | -2.00% | -0.54% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → SIEMENS | -2.00% | -0.50% |
| 1 | EV_CPI_BREACH_6PCT ⇒ F_REPO_IN → SIEMENS | -0.80% | -0.48% |
| 2 | EV_INDIA_RETAIL_FUEL_HIKE ⇒ NEW_OMC_MARKETING_MARGIN → F_GOVT_CAPEX → SIEMENS | +1.50% | +0.45% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_AI_CAPEX → T_DATA_CENTRES_IN → SIEMENS | -1.80% | -0.45% |
| 1 | EV_INDIA_US_INTERIM_DEAL_SIGNED ⇒ T_CHINA_PLUS_ONE → SIEMENS | +0.75% | +0.41% |
| 1 | EV_NVDA_NOV17_BEAT ⇒ F_US_EQUITIES → SIEMENS | +0.60% | +0.37% |
| 2 | EV_LPG_COMPENSATION_CABINET ⇒ NEW_OMC_MARKETING_MARGIN → F_GOVT_CAPEX → SIEMENS | +0.60% | +0.36% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_GOVT_CAPEX → SIEMENS | +1.00 | events | +2.50% |
| 1 | F_REPO_IN → SIEMENS | +1.00 | events | -2.00% |
| 1 | F_USDINR → SIEMENS | -0.37 | observed | +0.55% |
| 2 | F_GDP_IN → F_PRIVATE_CAPEX → SIEMENS | +0.50 | events | +0.45% |
| 2 | T_GENAI_SERVICES → T_DATA_CENTRES_IN → SIEMENS | +1.00 | events | +0.40% |
| 2 | P_US_TARIFF_INDIA → T_CHINA_PLUS_ONE → SIEMENS | -0.60 | events | +0.36% |
| 2 | F_GOVT_CAPEX → F_PRIVATE_CAPEX → SIEMENS | +1.00 | events | +0.36% |
| 1 | F_US_EQUITIES → SIEMENS | +0.23 | observed | +0.35% |
| 2 | T_ENERGY_TRANSITION → F_PRIVATE_CAPEX → SIEMENS | +0.50 | events | +0.27% |
| 2 | F_CREDIT_SPREADS_IN → F_PRIVATE_CAPEX → SIEMENS | +0.50 | events | -0.27% |
| 2 | P_FDI_RULES → T_CHINA_PLUS_ONE → SIEMENS | +0.50 | events | +0.25% |
| 2 | F_AI_CAPEX → T_DATA_CENTRES_IN → SIEMENS | -0.30 | events | -0.18% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-11 | Q2 FY27 results (Jul-Sep 2026): OPM trajectory (Q1 9%) and treatment of LVM proceeds | results | 0.90 | -0.5% | -0.45% |
| 2026-12 | Further analyst downgrades/upgrades after Jefferies downgrade on demand risks (2026-10-16) | guidance | 0.50 | -1.0% | -0.50% |
| 2027-01 | Possible special dividend / capital return from LVM sale proceeds | corporate_action | 0.25 | +2.5% | +0.62% |
| 2027-02 | Q3 FY27 results | results | 0.90 | +0.0% | +0.00% |
| 2027-03 | Large metro / locomotive / signalling order awards in India | other | 0.40 | +2.0% | +0.80% |
| 2027-05 | Annual (March FY) results and dividend | results | 0.90 | +0.0% | +0.00% |

## Analyst profile (agent research, sourced)
# SIEMENS — Siemens Ltd. (profile as of 2026-11-05)

Sources: pack `market_impact/data/packs/SIEMENS.md`; web-search summaries of the Q1 FY27 release (investywise, niftytrader, Upstox, Sahi); Investing.com and Equitymaster headlines for the Jefferies downgrade and price moves (headlines only). Segment shares and cost shares are model estimates. Several Siemens AG / Siemens Healthineers / Siemens Mobility Europe headlines in the pack are about foreign group companies and are not SIEMENS Ltd evidence. No expected-return number is given.

## Business
Siemens Ltd (75% Siemens AG) sells electrification and automation in India: Smart Infrastructure (switchgear, low and medium voltage products, building technology), Digital Industries (factory automation, drives, software) and Mobility (locomotives, metro, rail signalling). The Energy business was demerged into Siemens Energy India in 2025, and the Low Voltage Motors unit was sold, producing a Rs 2,099 cr gain in the June 2026 quarter. The financial year now ends in March. Core economics: sales Rs 18,062 cr TTM, OPM around 9-11%, large treasury with net cash and other income ~Rs 2,177 cr. P/E of 81 is inflated by the one-off gain on a margin-depressed base.

## What moves the stock (ranked)
1. **Private capex (+4.5 per +10% growth)** and China+1 manufacturing relocation (+2.5): Digital Industries and Smart Infrastructure follow factory and infrastructure investment.
2. **Margin recovery or further compression:** OPM was 9% in the June 2026 quarter against 13% a year earlier; ex-gain profit fell ~19% (Rs 343 cr). Jefferies downgraded the stock on demand risks on 2026-10-16 and the shares fell 5% on 2026-10-21. Competition (-2 per unit) and imported content (USD/INR -1.5) are the likely culprits, but management commentary was not retrieved.
3. **Government capex (+2.5)** and **railway capex (+2.0):** metro, rail electrification, signalling and locomotive programmes. Backlog is Rs 46,670 cr (+9.6% YoY).
4. **Data centres (+2.5):** power distribution and building management for hyperscale campuses.
5. **Valuation channels:** repo +25 bp ≈ -2 (long duration), US equities +1.5 (empirical t=+2.4), VIX -0.8.
6. **Costs:** copper -0.4 (pack's +1.65 is a cyclical correlation, flagged), steel minor.

## Transmission examples
- **Global trade/US tariffs (4th order):** higher US tariffs on Indian goods -> Indian exporters' margins fall -> their capex plans (autos, machinery) are deferred -> Digital Industries automation orders slow -> Siemens Ltd's order growth falls below 10% -> operating leverage on a 9% margin hurts earnings sharply. Jefferies' demand-risk call fits this chain.
- **Weak rupee (2nd/3rd order):** USD/INR at 94.5 (+6.5% y/y) -> imported products and software from the group cost more -> list-price increases lag -> margin compresses further -> earnings estimates cut -> de-rating from an elevated multiple.
- **Rail and metro capex (3rd order):** higher railway capex -> signalling and locomotive orders -> Mobility revenue up with high backlog visibility; but Indian locomotive tenders are competitive and local-content rules raise cost -> margin dilution.
- **Rates/risk-off (3rd order):** US 10y at ~4.9% -> FPIs trim (FII 6.8% flat) -> high-multiple capital goods de-rate -> equity falls even if orders grow. Reverse: rate relief re-rates it quickly.

## Current situation
Stock Rs 3,437, -10.8% in a month, -13% in 3 months, within a Rs 2,826-4,149 range. The June 2026 quarter: sales Rs 4,714 cr (+14.8%), reported PAT Rs 2,143 cr (five-fold, one-off), ex-gain about Rs 343 cr (-19%). Backlog Rs 46,670 cr (+9.6%). Jefferies downgrade (2026-10-16); weak capital goods sentiment (BSE capital goods -4% on 2026-10-23). Cash from the LVM sale raises the chance of a capital return but nothing was announced in retrieved sources.

## Upcoming events
Q2 FY27 results (November 2026), possible special dividend, Q3 results (Feb 2027), annual results (May 2027), large rail/metro order awards.

## Bull case
Margins recover to 12-13%, order inflow accelerates with private capex and data centres, LVM proceeds are returned, and the company re-rates on cleaner earnings.

## Bear case
Demand slows (Jefferies), margins stay at 9-10%, the FX hit grows, and a P/E on core earnings of ~100x compresses to 60x; an additional drag if Siemens AG reorganises and further assets are sold.

## Uncertainties
Segment mix, order inflow, reason for margin decline and the Jefferies rationale are not verified. Confidence: low.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.