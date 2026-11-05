# AUROPHARMA — Aurobindo Pharma Ltd.
*MIDCAP_100 · Healthcare · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -2.0%**, **12 months -4.4%** (rank 156 / 162 of 200 for 3m / 12m); beta 0.82
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +21.6%): 3 months 43%, 12 months 60%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -4.9% … P90 -0.3%; plausible 12m relative-return range incl. stock-specific noise: -14.9% … +17.2%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves -3.3 pp (model impact -6.6% beta-adjusted vs realised market-adjusted move +18.6%); forward event exposure +1.8% (3m +1.1%; half assumed priced); company-specific events -1.8%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| US generic drug price erosion (higher = worse) (`F_US_GENERIC_PRICING`) | +5 pp erosion | -5.00 | -5.00 | +0.00 | +0.00 | +0.00 | — |
| USFDA inspection/enforcement intensity (`P_USFDA_ENFORCEMENT`) | +1 = stricter | -3.00 | -4.00 | +1.00 | +0.00 | +0.00 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | +2.56 | +3.20 | -0.34 | -0.18 | -0.11 | -1.1% |
| China+1 manufacturing relocation to India (`T_CHINA_PLUS_ONE`) | +1 | +2.41 | +2.50 | -0.13 | +0.02 | +0.01 | — |
| US tariffs on pharmaceuticals (`P_US_PHARMA_TARIFF`) | +10 pp on Indian pharma exports | -2.40 | -3.00 | +0.60 | +0.00 | +0.00 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +1.78 | +2.00 | -0.25 | +0.00 | +0.02 | — |
| US–China trade decoupling (`C_US_CHINA_DECOUPLING`) | +1 = more decoupling | +1.61 | +0.00 | +1.42 | +0.24 | -0.05 | — |
| Chemical feedstock (benzene, propylene, etc.) (`F_CHEM_FEEDSTOCK`) | +10% feedstock | -1.60 | -1.60 | +0.00 | +0.00 | +0.00 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -1.25 | +0.00 | -0.48 | -0.47 | -0.30 | — |
| India 10-year G-sec yield (`F_GSEC_10Y_IN`) | +25 bp yield | -1.21 | -1.20 | +0.00 | +0.00 | -0.01 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -1.04 | +0.00 | +0.01 | -1.01 | -0.04 | — |
| Europe growth (`F_EU_GDP`) | +1 pp | +1.01 | +1.00 | +0.00 | +0.01 | -0.01 | — |
| GLP-1 / obesity drug adoption (`T_GLP1`) | +1 | +1.00 | +1.00 | +0.00 | +0.00 | +0.00 | — |
| China growth / stimulus (`F_CHINA_GDP`) | +1 pp | -0.89 | +0.00 | -0.78 | -0.10 | -0.01 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -3.9% | -3.9% | -4.4 | +0.5 | +0.0 | -0.1 |
| USFDA warning letters: Alembic, Aurobindo-Eugia, Dabur (Jul-Aug 2026) (`EV_USFDA_WARNING_WAVE_26`) | occurred | 1.00 | -3.0% | -3.0% | -4.0 | +1.0 | +0.0 | +0.0 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +4.3% | +2.1% | +5.0 | -0.8 | -0.0 | +0.1 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -1.7% | -1.7% | -1.7 | +0.0 | +0.0 | -0.0 |
| US imposes tariffs on generic drugs (200% threat) or removes India's speciality exemption (`EV_PHARMA_GENERICS_TARIFF`) | risk_scenario | 0.12 | -14.0% | -1.7% | -14.0 | +0.0 | +0.0 | +0.0 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -1.2% | -1.2% | +0.0 | +0.0 | -1.2 | -0.1 |
| China+1 momentum: Apple/Foxconn/Tata iPhone 18 Pro export ramp, India ~50% of US smartphone imports, PLI round 4 (textiles) and component schemes (`EV_CHINA_PLUS_ONE_ELECTRONICS`) | anticipated | 0.80 | +1.5% | +1.2% | +1.5 | -0.1 | +0.0 | +0.0 |
| Rupee at 95-96/USD and heavy RBI FX defence; reserves fall ~US$55bn from peak (`EV_RUPEE_DEFENCE_RESERVES_26`) | occurred | 1.00 | -1.1% | -1.1% | -1.2 | +0.1 | +0.0 | +0.0 |
| US midterms (3 Nov 2026): Democrats win House and Senate (`EV_US_MIDTERMS_DEM_SWEEP`) | occurred | 1.00 | +0.9% | +0.9% | +1.0 | -0.0 | -0.0 | +0.0 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -0.8% | -0.8% | -0.7 | -0.1 | -0.0 | -0.0 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -0.7% | -0.7% | +0.0 | -0.7 | -0.0 | -0.1 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -0.7% | -0.7% | +0.0 | -0.9 | +0.2 | -0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → AUROPHARMA | +5.00% | +2.50% |
| 1 | EV_CHINA_PLUS_ONE_ELECTRONICS ⇒ T_CHINA_PLUS_ONE → AUROPHARMA | +1.50% | +1.20% |
| 1 | EV_PHARMA_GENERICS_TARIFF ⇒ P_US_PHARMA_TARIFF → AUROPHARMA | -9.00% | -1.08% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_USDINR → AUROPHARMA | +4.16% | +0.75% |
| 1 | EV_PHARMA_GENERICS_TARIFF ⇒ F_US_GENERIC_PRICING → AUROPHARMA | -5.00% | -0.60% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → AUROPHARMA | -3.00% | -0.54% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → AUROPHARMA | -1.92% | -0.48% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_FPI_FLOWS → AUROPHARMA | -1.92% | -0.48% |
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → AUROPHARMA | -0.96% | -0.48% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → AUROPHARMA | -1.87% | -0.47% |
| 1 | EV_INDIA_US_INTERIM_DEAL_SIGNED ⇒ T_CHINA_PLUS_ONE → AUROPHARMA | +0.75% | +0.41% |
| 2 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → F_CHEM_FEEDSTOCK → AUROPHARMA | +0.71% | +0.39% |
| 2 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → F_USDINR → AUROPHARMA | -0.74% | -0.37% |
| 2 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → F_USDINR → AUROPHARMA | -0.66% | -0.36% |
| 1 | EV_CPI_BREACH_6PCT ⇒ F_GSEC_10Y_IN → AUROPHARMA | -0.60% | -0.36% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | P_USFDA_ENFORCEMENT → AUROPHARMA | +1.00 | events | -4.00% |
| 1 | F_FPI_FLOWS → AUROPHARMA | -1.60 | events | -3.20% |
| 1 | F_GSEC_10Y_IN → AUROPHARMA | +1.55 | director_override | -1.86% |
| 1 | F_USDINR → AUROPHARMA | -0.37 | observed | -1.18% |
| 2 | P_USFDA_ENFORCEMENT → F_US_GENERIC_PRICING → AUROPHARMA | +1.00 | events | +1.00% |
| 1 | P_US_PHARMA_TARIFF → AUROPHARMA | +0.20 | events | -0.60% |
| 2 | P_US_TARIFF_INDIA → T_CHINA_PLUS_ONE → AUROPHARMA | -0.60 | events | +0.36% |
| 1 | F_REPO_IN → AUROPHARMA | +1.00 | events | -0.30% |
| 2 | P_FDI_RULES → T_CHINA_PLUS_ONE → AUROPHARMA | +0.50 | events | +0.25% |
| 1 | F_EU_GDP → AUROPHARMA | +0.22 | events | +0.22% |
| 2 | P_ANTI_DUMPING_IN → F_CHEM_FEEDSTOCK → AUROPHARMA | +0.40 | events | -0.13% |
| 2 | P_US_PHARMA_TARIFF → F_US_GENERIC_PRICING → AUROPHARMA | +0.20 | events | +0.12% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-11-20 | Interim dividend Rs 7/share paid (by Nov 20) | corporate_action | 0.99 | +0.2% | +0.25% |
| 2027-02 | Q3 FY27 results: US pricing, launches, margin sustainability | results | 0.95 | +0.0% | +0.00% |
| 2027-03 | USFDA inspection outcomes across Eugia/other units | regulatory | 0.12 | -8.0% | -0.96% |
| 2027-06 | Section 232 tariff scope extended to generics | regulatory | 0.08 | -14.0% | -1.12% |

## Analyst profile (agent research, sourced)
# AUROPHARMA - Aurobindo Pharma Ltd. (Midcap 100, US generics)

## Business
Aurobindo is a vertically integrated generics maker (oral solids, injectables through Eugia, antiretrovirals, APIs, penicillin chain, emerging biosimilars and CRDMO). The US is about 47% of sales and Europe about 28% (model estimates; not primary-source verified). Q2 FY27 sales were a record Rs 10,263 cr, operating profit Rs 2,153 cr (21%) and PAT Rs 1,124 cr (+32.5%). Fixed assets have expanded to Rs 21.4k cr, and ROE is only 10%.

## What moves the stock, ranked
1. **US generic pricing and launches (-5.0 per +5pp erosion).** Adquey ointment (US launch 2026-10-01, Nuvama sees US$300m peak) and perampanel tablets offset base erosion.
2. **USD/INR (+3.2 per +3%).**
3. **USFDA/regulatory and tariffs (-4.0, -3.0).** The Sep 29 US pharma tariff exempts Indian specialty drugs; generics are outside it (model knowledge).
4. **China dependence and China+1 (+0.8 / +2.5).**
5. **Input costs (-1.6, -0.4) and rates (-1.2, -0.3).**
6. **FPI flows (+2.0).**

## Transmission examples
- **Weak rupee (INR 94.5) -> export earnings up -> EBITDA +8% per 3% -> margin cushion offsets US price erosion.** If the Middle East escalation lifts Brent, INR weakens further (2nd), US-priced revenue becomes more valuable in INR (3rd), but Brent also raises solvent cost (4th); net positive.
- **US chain consolidation -> price erosion up -> Aurobindo US margin down -> capex discipline questioned.**
- **Section 232 extended to generics (low probability) -> US retailers seek price-sharing -> Aurobindo (47% US) is among the most exposed Indian generics names.**
- **China export controls or dumping -> KSM price swings -> Aurobindo input costs.** Dumping lowers costs, restrictions raise them; PLI Penicillin-G dampens it.

## Current situation
Strong Q2, new highs, FII stake up from 15.2% to 17.4% in two quarters. Pack: 12m +52.7%, 6m +18.7%. Management completed A1 Biochem acquisition to build a CRDMO platform.

## Upcoming events
Dividend payout by 2026-11-20; Q3 results Feb 2027; USFDA inspection cycle; tariff developments.

## Bull and bear
**Bull:** growth, launches, weak rupee, rising FII interest, biosimilar optionality. **Bear:** US price erosion, tariff tail, 52-week-high valuation versus low ROE. Confidence medium: no call transcript was read.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.