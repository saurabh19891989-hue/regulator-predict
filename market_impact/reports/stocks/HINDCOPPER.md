# HINDCOPPER — Hindustan Copper Ltd.
*MIDCAP_100 · Metals & Mining · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +1.6%**, **12 months +1.4%** (rank 16 / 44 of 200 for 3m / 12m); beta 1.40
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +48.4%): 3 months 53%, 12 months 60%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -1.8% … P90 +6.1%; plausible 12m relative-return range incl. stock-specific noise: -46.0% … +62.6%
- Decomposition (12m): 0.5 × forward event exposure +8.2% (3m +4.3%; half assumed priced) + 0.5 × company-specific catalysts -4.4%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply +2.5% (beta-adjusted) vs a realised market-adjusted move of -27.0% — gap +29.5 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Copper price (`F_COPPER`) | +10% copper | +6.00 | +6.00 | +0.00 | +0.00 | +0.00 | -2.4% |
| Mining royalty / mineral tax burden (`P_MINING_ROYALTY`) | +1 = higher | -3.00 | -3.00 | +0.00 | +0.00 | +0.00 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | +2.80 | +3.00 | -0.17 | -0.03 | +0.00 | -1.1% |
| China growth / stimulus (`F_CHINA_GDP`) | +1 pp | +2.72 | +1.00 | +1.60 | +0.10 | +0.01 | — |
| Energy transition investment (`T_ENERGY_TRANSITION`) | +1 | +2.72 | +2.00 | +0.72 | +0.00 | -0.00 | — |
| Renewable / transmission policy support (`P_RENEWABLE_SUPPORT`) | +1 = stronger support | +1.39 | +0.00 | +1.04 | +0.35 | +0.00 | — |
| US dollar index (`F_DXY`) | +3% DXY | -1.30 | +0.00 | -1.42 | +0.11 | +0.01 | +2.2% |
| US–China trade decoupling (`C_US_CHINA_DECOUPLING`) | +1 = more decoupling | -0.80 | +0.00 | -0.32 | -0.46 | -0.03 | — |
| EV incentives / mandates (`P_EV_POLICY`) | +1 = stronger EV push | +0.64 | +0.00 | +0.48 | +0.16 | +0.00 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -0.64 | -0.50 | -0.12 | -0.02 | +0.00 | — |
| Foreign portfolio flows into Indian government/corporate bonds (FAR, index-linked) (`NEW_FPI_DEBT_FLOWS`) | +US$5 bn net debt inflow per quarter | -0.57 | +0.00 | -0.60 | +0.03 | +0.00 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +0.53 | +0.80 | -0.28 | +0.01 | +0.00 | — |
| US 10-year Treasury yield (`F_US_10Y`) | +25 bp yield | -0.39 | +0.00 | -0.16 | -0.18 | -0.05 | +9.4% |
| US tariffs on Indian goods (`P_US_TARIFF_INDIA`) | +10 pp average tariff | +0.37 | +0.00 | +0.28 | +0.09 | +0.01 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Aluminium -20% since June; copper off record; Nifty Metal -7% in October (`EV_BASE_METALS_ALUMINIUM_SLIDE`) | occurred | 1.00 | -1.4% | -1.4% | -1.4 | +0.0 | +0.0 | +0.0 |
| Cabinet approves Rs14,500 cr VGF for ~92 GWh grid-scale storage (4 Nov) (`EV_BESS_VGF_NOV26`) | occurred | 1.00 | +1.4% | +1.4% | +1.0 | +0.4 | +0.0 | -0.0 |
| China Central Economic Work Conference / NPC (Dec 2026-Mar 2027): larger-than-expected fiscal or property stimulus (`EV_CHINA_CEWC_STIMULUS_DEC26`) | anticipated | 0.45 | +2.8% | +1.3% | +2.8 | -0.1 | +0.0 | +0.0 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -1.2% | -1.2% | -1.8 | +0.6 | -0.0 | +0.0 |
| Rupee at 95-96/USD and heavy RBI FX defence; reserves fall ~US$55bn from peak (`EV_RUPEE_DEFENCE_RESERVES_26`) | occurred | 1.00 | -1.0% | -1.0% | -1.1 | +0.1 | +0.0 | +0.0 |
| China Dec CEWC / Mar 2027 NPC delivers large fiscal stimulus and consumption push (`EV_CHINA_NPC_MAR27_BIG_STIMULUS`) | anticipated | 0.35 | +2.7% | +0.9% | +1.0 | +1.5 | +0.1 | +0.0 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -0.7% | -0.7% | +0.0 | -0.8 | +0.1 | -0.0 |
| China Q3 GDP +4.5% (beat); property 'mini-stimulus' of late September; PMI 49.3; LPR unchanged (`EV_CHINA_Q3_GDP_AND_MINI_STIMULUS`) | occurred | 1.00 | +0.7% | +0.7% | +0.3 | +0.4 | +0.0 | +0.0 |
| ALMM List-II (domestic cells) in force; approved cell capacity 37.8 GW (12th revision, 9 Oct); solar project costs seen +20% (`EV_SOLAR_ALMM2_CELL_MANDATE`) | occurred | 1.00 | +0.7% | +0.7% | +0.0 | +0.5 | +0.2 | +0.0 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -0.6% | -0.6% | -0.5 | -0.1 | -0.0 | -0.0 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +1.2% | +0.6% | +2.0 | -0.8 | +0.1 | +0.0 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -0.5% | -0.5% | +0.0 | -0.7 | +0.1 | -0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_CHINA_CEWC_STIMULUS_DEC26 ⇒ F_COPPER → HINDCOPPER | +2.40% | +1.08% |
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → HINDCOPPER | +2.00% | +1.00% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_USDINR → HINDCOPPER | +3.90% | +0.70% |
| 2 | EV_CHINA_NPC_MAR27_BIG_STIMULUS ⇒ F_CHINA_GDP → F_COPPER → HINDCOPPER | +1.76% | +0.62% |
| 2 | EV_FED_DEC26_HIKE25 ⇒ F_DXY → F_COPPER → HINDCOPPER | -0.50% | -0.36% |
| 1 | EV_NUCLEAR_SHANTI_RULES_FINAL ⇒ T_ENERGY_TRANSITION → HINDCOPPER | +0.60% | +0.36% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → HINDCOPPER | +0.65% | +0.36% |
| 1 | EV_CHINA_NPC_MAR27_BIG_STIMULUS ⇒ F_CHINA_GDP → HINDCOPPER | +1.00% | +0.35% |
| 2 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → F_USDINR → HINDCOPPER | -0.69% | -0.35% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → HINDCOPPER | -1.10% | -0.28% |
| 2 | EV_FED_H1_2027_FURTHER_HIKES ⇒ F_DXY → F_COPPER → HINDCOPPER | -0.67% | -0.27% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → F_USDINR → HINDCOPPER | +0.90% | +0.22% |
| 2 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → F_USDINR → HINDCOPPER | -0.40% | -0.22% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → HINDCOPPER | -1.20% | -0.22% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → HINDCOPPER | -0.50% | -0.21% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_COPPER → HINDCOPPER | -0.24 | observed | -1.42% |
| 1 | F_FPI_FLOWS → HINDCOPPER | -1.60 | events | -1.28% |
| 1 | F_USDINR → HINDCOPPER | -0.37 | observed | -1.11% |
| 1 | T_ENERGY_TRANSITION → HINDCOPPER | +0.30 | director_override | +0.60% |
| 1 | F_REPO_IN → HINDCOPPER | +1.00 | events | -0.50% |
| 1 | F_CHINA_GDP → HINDCOPPER | +0.30 | events | +0.30% |
| 1 | F_BRENT → HINDCOPPER | +0.00 | observed | -0.00% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-11 | Q2 FY27 results (Q1 was ~2026-08-10; date not confirmed) | results | 0.95 | +0.0% | +0.00% |
| 2027-01 | Arbitration award case: commercial court conditionally stayed the 50% deposit requirement (2026-09-22); further ruling pending | litigation | 0.30 | -2.0% | -0.60% |
| 2027-03 | QIP of up to ~9.69 crore shares / Rs500 cr NCD executed | corporate_action | 0.60 | -5.0% | -3.00% |
| 2027-06 | Further government stake sale | corporate_action | 0.15 | -5.5% | -0.82% |

## Analyst profile (agent research, sourced)
# HINDCOPPER — Hindustan Copper Ltd. (Midcap 100, I_NONFERROUS) — as of 2026-11-05

## Business
India's only vertically integrated copper-ore miner (Khetri, Malanjkhand, Indian Copper Complex, Rakha), 60.1% government-owned after the August 2026 offer for sale. Revenue is concentrate and cathode priced off LME copper in rupees, against a largely fixed mining cost base, which gives very high operating leverage: TTM sales Rs3,498 cr, EBITDA Rs1,758 cr (50% margin versus 28% in FY22). Q1 FY27: sales Rs936 cr, EBITDA Rs508 cr, PAT Rs352 cr. Market cap Rs41,485 cr at 34x earnings.

## What moves the stock
1. **LME copper** (w +6 per +10%): +10% is roughly +20% EBITDA at constant cost; pack empirical +4.16 (t=+3.5). Copper is near a record above $14,000/t but the pack shows a 4.7% fall in three months.
2. **USD/INR** (+3 per +3%): INR realisation, INR costs.
3. **Theme: energy transition / grid / data-centre copper** (+2): scarcity rerating that spot copper does not capture.
4. **Policy and ownership:** mining royalty risk (-3), government stake sales and QIP dilution (events), FPI flows (+0.8).
5. Small: diesel/power cost (-0.5), China growth (+1), rates (-0.5).

## Transmission examples
- **Copper path:** US-China tension eases -> China GDP outlook up -> copper demand up -> LME +8% -> HCL EBITDA +16% -> equity about +5 to +8%; third order: higher profits support the Rs7,000 cr expansion and reduce QIP size, and a stronger rupee would claw back some of the gain.
- **Dollar path:** US 10-year yield up -> DXY up -> copper down (empirical DXY -3.84, t=-2.3) -> HCL revenue down; offset only if INR weakens along with the DXY, which raises rupee realisation.
- **Fiscal path:** Government needs disinvestment proceeds -> further OFS in HCL (Aug OFS raised ~Rs3,000 cr, shares -7.5% on the day) -> overhang and free-float increase; fourth order: higher float and FII share may lift index weight and passive demand later.
- **Oil path:** Brent up -> diesel/explosive costs up -> cost +0.6% -> EBITDA -1% (small).

## Current situation
Dividend of Rs1.86 and QIP of ~9.69 crore shares plus Rs500 cr NCD approved at AGM (2026-09-24). Rs7,000 cr capex over 5-6 years (2026-09-22). A commercial court granted a conditional stay on an arbitration award requiring a 50% deposit (2026-09-22). Stock -21% over three months after the OFS and the copper pullback.

## Upcoming events
Q2 FY27 results mid-November (not confirmed), QIP launch (prob 0.6 by Mar 2027, -2 to -8%), arbitration developments, possible further government sale.

## Bull and bear
Bull: copper stays above $14,000, ore output ramps, critical-mineral scarcity multiple. Bear: copper mean-reverts, dilution via QIP, expansions slip, valuation (34x, P/B 12x) already rich. Confidence medium; cost split is a model estimate, since the pack does not give it.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.