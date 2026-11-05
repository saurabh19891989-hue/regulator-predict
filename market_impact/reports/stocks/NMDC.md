# NMDC — NMDC Ltd.
*MIDCAP_100 · Metals & Mining · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +1.5%**, **12 months +2.8%** (rank 5 / 7 of 200 for 3m / 12m); beta 1.16
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +23.0%): 3 months 55%, 12 months 57%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -2.4% … P90 +10.6%; plausible 12m relative-return range incl. stock-specific noise: -25.8% … +34.5%
- Decomposition (12m): 0.5 × forward event exposure +3.9% (3m +1.8%; half assumed priced; market-priced macro drift removed) + 0.5 × company-specific catalysts +2.2%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply -1.5% (beta-adjusted) vs a realised market-adjusted move of -29.2% — gap +27.7 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Iron ore price (`F_IRON_ORE`) | +15% iron ore | +9.09 | +9.00 | +0.00 | +0.10 | -0.01 | -12.5% |
| China growth / stimulus (`F_CHINA_GDP`) | +1 pp | +4.83 | +0.00 | +4.04 | +0.49 | +0.30 | — |
| Mining royalty / mineral tax burden (`P_MINING_ROYALTY`) | +1 = higher | -3.00 | -3.00 | +0.00 | +0.00 | +0.00 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | +2.13 | +2.00 | +0.19 | -0.06 | +0.00 | -1.1% |
| Indian domestic steel price (`F_STEEL_INDIA`) | +7% domestic HRC/rebar price | +1.88 | +2.00 | -0.12 | +0.00 | +0.00 | — |
| Indian safeguard/anti-dumping duty on steel imports (`P_STEEL_DUTY_IN`) | +10 pp effective duty | +1.40 | +1.00 | +0.40 | +0.00 | +0.00 | — |
| US–China trade decoupling (`C_US_CHINA_DECOUPLING`) | +1 = more decoupling | -1.38 | +0.00 | +0.00 | -1.21 | -0.18 | — |
| Central + state government capex (`F_GOVT_CAPEX`) | +10% capex growth | +1.07 | +1.00 | +0.14 | -0.04 | -0.03 | — |
| Global HRC steel price (`F_STEEL_GLOBAL`) | +10% global HRC | +0.93 | +0.00 | +0.99 | -0.06 | +0.00 | +20.6% |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -0.72 | -0.60 | -0.08 | -0.04 | +0.00 | — |
| Coking coal price (`F_COKING_COAL`) | +15% coking coal | +0.62 | +0.00 | +0.40 | +0.24 | -0.01 | — |
| US dollar index (`F_DXY`) | +3% DXY | +0.50 | +0.00 | +0.32 | +0.17 | +0.01 | +2.2% |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | +0.48 | +0.00 | +0.24 | +0.17 | +0.07 | +3.5% |
| China steel exports (`F_CHINA_STEEL_EXPORTS`) | +15% y/y | -0.45 | +0.00 | -0.24 | -0.23 | +0.02 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Iron ore at two-year low; NMDC price cuts then partial hike (`EV_IRON_ORE_TWO_YEAR_LOW`) | occurred | 1.00 | -7.5% | -7.5% | -7.5 | +0.0 | -0.1 | +0.0 |
| China Central Economic Work Conference / NPC (Dec 2026-Mar 2027): larger-than-expected fiscal or property stimulus (`EV_CHINA_CEWC_STIMULUS_DEC26`) | anticipated | 0.45 | +5.7% | +2.6% | +5.4 | -0.1 | +0.3 | +0.1 |
| Global and Indian steel prices at multi-year highs (global HRC +60% y/y) (`EV_STEEL_RALLY_2026`) | occurred | 1.00 | +2.1% | +2.1% | +2.2 | -0.1 | +0.0 | +0.0 |
| China Dec CEWC / Mar 2027 NPC delivers large fiscal stimulus and consumption push (`EV_CHINA_NPC_MAR27_BIG_STIMULUS`) | anticipated | 0.35 | +4.8% | +1.7% | +0.0 | +4.0 | +0.5 | +0.3 |
| China Q3 GDP +4.5% (beat); property 'mini-stimulus' of late September; PMI 49.3; LPR unchanged (`EV_CHINA_Q3_GDP_AND_MINI_STIMULUS`) | occurred | 1.00 | +1.4% | +1.4% | +0.0 | +1.1 | +0.2 | +0.1 |
| China property-sector credit event / sharp relapse (large developer or LGFV default) (`EV_CHINA_PROPERTY_RELAPSE`) | risk_scenario | 0.10 | -11.7% | -1.2% | -11.7 | +0.4 | -0.3 | -0.1 |
| China enforces steel output cuts / export licensing discipline ('anti-involution') (`EV_CHINA_STEEL_OUTPUT_CURB_2027`) | anticipated | 0.50 | -2.3% | -1.2% | -2.7 | +0.4 | -0.1 | +0.0 |
| India Q1 FY27 GDP grows 7.8% (31 Aug 2026), beating ~7.3% consensus (`EV_GDP_Q1FY27_7_8`) | occurred | 1.00 | +1.0% | +1.0% | +1.0 | +0.1 | -0.1 | -0.0 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | +0.9% | +0.9% | +0.0 | +0.8 | +0.1 | +0.0 |
| DGTR recommends/imposes anti-dumping duty on hot-rolled flat steel from China, Japan, Russia (`EV_INDIA_HR_STEEL_AD_PROVISIONAL`) | anticipated | 0.55 | +1.6% | +0.9% | +1.6 | +0.0 | +0.0 | +0.0 |
| Rupee at 95-96/USD and heavy RBI FX defence; reserves fall ~US$55bn from peak (`EV_RUPEE_DEFENCE_RESERVES_26`) | occurred | 1.00 | -0.8% | -0.8% | -0.7 | -0.1 | +0.0 | +0.0 |
| Coking coal price spike squeezes Indian steel margins (`EV_COKING_COAL_SURGE_AUG26`) | occurred | 1.00 | +0.8% | +0.8% | +0.8 | -0.0 | +0.0 | +0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_CHINA_CEWC_STIMULUS_DEC26 ⇒ F_IRON_ORE → NMDC | +5.40% | +2.43% |
| 2 | EV_CHINA_NPC_MAR27_BIG_STIMULUS ⇒ F_CHINA_GDP → F_IRON_ORE → NMDC | +4.20% | +1.47% |
| 1 | EV_CHINA_STEEL_OUTPUT_CURB_2027 ⇒ F_IRON_ORE → NMDC | -2.70% | -1.35% |
| 1 | EV_CHINA_PROPERTY_RELAPSE ⇒ F_IRON_ORE → NMDC | -11.70% | -1.17% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_USDINR → NMDC | +2.60% | +0.47% |
| 2 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → F_USDINR → NMDC | -0.92% | -0.46% |
| 1 | EV_INDIA_HR_STEEL_AD_PROVISIONAL ⇒ P_STEEL_DUTY_IN → NMDC | +0.80% | +0.44% |
| 1 | EV_INDIA_HR_STEEL_AD_PROVISIONAL ⇒ F_STEEL_INDIA → NMDC | +0.80% | +0.44% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → NMDC | +0.65% | +0.36% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → NMDC | -1.10% | -0.28% |
| 3 | EV_US_CHINA_TRUCE_EXTENDED ⇒ C_US_CHINA_DECOUPLING → F_CHINA_GDP → F_IRON_ORE → NMDC | +0.38% | +0.27% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → NMDC | -0.60% | -0.25% |
| 3 | EV_RARE_EARTH_CONTROLS_REIMPOSED ⇒ C_US_CHINA_DECOUPLING → F_CHINA_GDP → F_IRON_ORE → NMDC | -1.01% | -0.25% |
| 2 | EV_CHINA_STEEL_EXPORT_FLOOD ⇒ F_STEEL_GLOBAL → F_STEEL_INDIA → NMDC | -0.99% | -0.25% |
| 1 | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → NMDC | +0.20% | +0.18% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_IRON_ORE → NMDC | -0.83 | observed | -7.47% |
| 1 | F_STEEL_INDIA → NMDC | +1.35 | events | +2.70% |
| 1 | F_USDINR → NMDC | -0.37 | observed | -0.74% |
| 1 | F_REPO_IN → NMDC | +1.00 | events | -0.60% |
| 1 | F_GOVT_CAPEX → NMDC | +0.20 | director_override | +0.20% |
| 2 | F_STEEL_INDIA → P_STEEL_DUTY_IN → NMDC | +1.35 | events | -0.16% |
| 3 | F_CHINA_GDP → F_CHINA_STEEL_EXPORTS → P_STEEL_DUTY_IN → NMDC | +0.30 | events | -0.03% |
| 3 | F_USDCNY → F_CHINA_STEEL_EXPORTS → P_STEEL_DUTY_IN → NMDC | -0.47 | observed | -0.02% |
| 3 | C_US_CHINA_DECOUPLING → F_CHINA_STEEL_EXPORTS → P_STEEL_DUTY_IN → NMDC | -0.10 | events | -0.00% |
| 1 | F_BRENT → NMDC | +0.00 | observed | -0.00% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-09-27 | Rs5,427 cr slurry pipeline/processing/pellet plant commissioned (occurred) | capex | 1.00 | +1.5% | +1.50% |
| 2026-11 | Q2 FY27 results (Q1 was 2026-08-14; date unconfirmed) | results | 0.95 | +0.0% | +0.00% |
| 2026-12 | Monthly iron ore price reset(s); September-October YTD production +22.8% to 27.27 Mt | other | 0.80 | +0.0% | +0.00% |
| 2027-03 | Interim dividend declaration (dividend yield 5%) | corporate_action | 0.70 | +1.0% | +0.70% |

## Analyst profile (agent research, sourced)
# NMDC — NMDC Ltd. (Midcap 100, I_MINING) — as of 2026-11-05

## Business
India's largest iron-ore miner (Bailadila in Chhattisgarh, Donimalai and Kumaraswamy in Karnataka), 60.8% government-owned, about 45 Mt/yr output, selling lump and fines to steel mills. Net-cash balance sheet and a 5% dividend yield. Q1 FY27: sales Rs6,795 cr, EBITDA Rs2,468 cr (36%), PAT Rs1,976 cr, flat YoY on weak offtake and lower prices. TTM sales Rs32,127 cr, EBITDA Rs9,249 cr (29%); market cap Rs61,850 cr. Prices were cut on 2026-08-08 (lump Rs5,250/t, fines Rs4,500/t). YTD production is +22.8% (27.27 Mt, 2026-10-01).

## What moves the stock
1. **Iron ore price** (+9 per +15%): ~95% of revenue is ore; costs are largely fixed; the pack's empirical +6.23 (t=+3.8) is the strongest statistic. 2. **USD/INR** (+2.0). 3. **Domestic steel price** (+2.0, demand/pricing ceiling). 4. **Royalty/levies** (-3.0). 5. Government capex (+1.0), steel-duty policy (+1.0), repo (-0.6), Brent/diesel (-0.5).

## Transmission examples
- **China path:** China stimulus or property relief -> seaborne ore up -> NMDC raises list prices after a lag (65% pass-through) -> margin up 3-4 points -> equity +8 to +10; the reverse caused the August cut.
- **Steel path:** Domestic steel prices rise (post-Diwali) -> mills' margins widen -> NMDC can raise lump/fines prices and sees higher offtake -> EBITDA up; third order: large producers' captive-mine growth caps the upside; fourth: royalty/auction regime changes in Odisha shift market share.
- **Policy path:** Draft National Steel Policy 2047 (604 Mt capacity) -> long-run ore demand growth -> supports the Rs5,427 cr slurry/pellet capex valuation; Mining royalty hikes would cut margin directly.
- **Dollar path:** USD/INR up -> import-parity ore price up in INR -> revenue +1.5% per +3% -> EBITDA +5%.

## Current situation
Muted Q1 followed by price cut, production boom and a Rs5,427 cr project commissioning on 2026-09-27 (including a 2 MTPA pellet plant). Stock -18% over 3m, near its 52-week low (Rs65). Nuvama turned bullish (2026-08-17); Citi cut target on costs.

## Upcoming events
Q2 results mid-Nov (date unconfirmed); monthly price resets; interim dividend.

## Bull and bear
Bull: ore prices at a trough, volumes up, dividend. Bear: low offtake, further price cuts, royalty hikes. Confidence medium.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.