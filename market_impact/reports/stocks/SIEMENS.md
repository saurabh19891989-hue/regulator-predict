# SIEMENS — Siemens Ltd.
*NIFTY_NEXT_50 · Capital Goods · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +2.0%**, **12 months +4.8%** (rank 43 / 36 of 200 for 3m / 12m); beta 1.24
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +25.0%): 3 months 56%, 12 months 68%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 +2.4% … P90 +9.7%; plausible 12m relative-return range incl. stock-specific noise: -13.4% … +39.7%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +4.1 pp (model impact +8.3% beta-adjusted vs realised market-adjusted move -13.1%); forward event exposure +3.1% (3m +0.8%; half assumed priced); company-specific events +0.5%

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
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -6.4% | -6.4% | +0.0 | -2.7 | -2.8 | -0.9 |
| Union Budget 2027-28 capex/railway allocation (infra, railways, defence) (`EV_BUDGET27_CAPEX_RAILWAY`) | scheduled | 0.90 | +3.7% | +3.4% | +3.6 | +0.3 | -0.1 | -0.1 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -3.3% | -3.3% | +0.0 | -3.0 | -0.3 | -0.1 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.28 | -10.7% | -3.0% | -7.7 | -2.2 | -0.8 | -0.1 |
| India Q1 FY27 GDP grows 7.8% (31 Aug 2026), beating ~7.3% consensus (`EV_GDP_Q1FY27_7_8`) | occurred | 1.00 | +2.4% | +2.4% | +2.5 | +0.2 | -0.2 | -0.1 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -2.2% | -2.2% | -2.0 | -0.2 | +0.0 | -0.0 |
| Retail petrol/diesel price freeze with crude >$100 squeezes OMC marketing margins; Q2 FY27 results split refiners (`EV_OMC_FUEL_FREEZE_LOSSES`) | occurred | 1.00 | -1.7% | -1.7% | +0.0 | -1.8 | -0.0 | +0.1 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.36 | -4.5% | -1.6% | -1.0 | -1.7 | -1.3 | -0.5 |
| China+1 momentum: Apple/Foxconn/Tata iPhone 18 Pro export ramp, India ~50% of US smartphone imports, PLI round 4 (textiles) and component schemes (`EV_CHINA_PLUS_ONE_ELECTRONICS`) | anticipated | 0.80 | +2.0% | +1.6% | +1.8 | +0.2 | +0.0 | -0.0 |
| US Q3 data: GDP 3.4%, CPI 3.7%, September payrolls only +29k (`EV_US_Q3_DATA_MIXED`) | occurred | 1.00 | +1.6% | +1.6% | +0.0 | +1.4 | +0.2 | -0.0 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -1.4% | -1.4% | -0.3 | -0.8 | -0.1 | -0.2 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.58 | +2.4% | +1.4% | +0.4 | +0.9 | +0.8 | +0.3 |

## Strongest causal chains (1st–4th order)
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 2 | EV_CPI_REACCEL_SEP26 ⇒ F_CPI_IN → F_REPO_IN → SIEMENS | -2.65% | -2.65% |
| 1 | EV_GDP_Q1FY27_7_8 ⇒ F_GOVT_CAPEX → SIEMENS | +2.50% | +2.50% |
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_USDINR → SIEMENS | -2.35% | -2.35% |
| 1 | EV_RBI_OCT26_HIKE25 ⇒ F_REPO_IN → SIEMENS | -2.00% | -2.00% |
| 2 | EV_OMC_FUEL_FREEZE_LOSSES ⇒ NEW_OMC_MARKETING_MARGIN → F_GOVT_CAPEX → SIEMENS | -1.80% | -1.80% |
| 1 | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → SIEMENS | +2.00% | +1.80% |
| 3 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_CPI_IN → F_REPO_IN → SIEMENS | -1.77% | -1.77% |
| 1 | EV_BUDGET27_CAPEX_RAILWAY ⇒ P_RAILWAY_CAPEX → SIEMENS | +1.60% | +1.44% |
| 2 | EV_US_Q3_DATA_MIXED ⇒ F_US_GDP → F_US_EQUITIES → SIEMENS | +1.30% | +1.30% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → SIEMENS | -4.50% | -1.26% |
| 1 | EV_CHINA_PLUS_ONE_ELECTRONICS ⇒ T_CHINA_PLUS_ONE → SIEMENS | +1.50% | +1.20% |
| 1 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → SIEMENS | -4.50% | -1.12% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → SIEMENS | -3.20% | -0.90% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → SIEMENS | -2.00% | -0.80% |
| 1 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → SIEMENS | -4.00% | -0.72% |

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