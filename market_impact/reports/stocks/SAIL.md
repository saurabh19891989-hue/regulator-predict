# SAIL — Steel Authority of India Ltd.
*MIDCAP_100 · Metals & Mining · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +0.7%**, **12 months +1.6%** (rank 31 / 30 of 200 for 3m / 12m); beta 1.29
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +30.7%): 3 months 52%, 12 months 51%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -4.9% … P90 +9.7%; plausible 12m relative-return range incl. stock-specific noise: -39.5% … +40.5%
- Decomposition (12m): 0.5 × forward event exposure +5.4% (3m +1.7%; half assumed priced; market-priced macro drift removed) + 0.5 × company-specific catalysts -1.8%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply +13.5% (beta-adjusted) vs a realised market-adjusted move of -23.2% — gap +36.7 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Indian domestic steel price (`F_STEEL_INDIA`) | +7% domestic HRC/rebar price | +14.75 | +15.00 | -0.24 | -0.01 | +0.00 | — |
| Global HRC steel price (`F_STEEL_GLOBAL`) | +10% global HRC | +7.29 | +0.00 | +7.40 | -0.11 | +0.00 | +20.6% |
| Coking coal price (`F_COKING_COAL`) | +15% coking coal | -5.60 | -8.00 | +1.50 | +0.93 | -0.03 | — |
| Indian safeguard/anti-dumping duty on steel imports (`P_STEEL_DUTY_IN`) | +10 pp effective duty | +5.00 | +2.00 | +3.00 | +0.00 | +0.00 | — |
| China steel exports (`F_CHINA_STEEL_EXPORTS`) | +15% y/y | -4.51 | +0.00 | -2.68 | -1.86 | +0.04 | — |
| Central + state government capex (`F_GOVT_CAPEX`) | +10% capex growth | +3.61 | +2.50 | +1.19 | -0.04 | -0.03 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | +2.63 | +1.00 | +1.75 | -0.13 | +0.01 | -1.1% |
| China growth / stimulus (`F_CHINA_GDP`) | +1 pp | +1.93 | +0.00 | -2.97 | +2.95 | +1.95 | — |
| EU steel safeguard / CBAM burden on imports (`NEW_EU_STEEL_ACCESS`) | +1 = tightening step (quota cut / higher out-of-quota tariff / CBAM cost) | -1.77 | +0.00 | -1.80 | +0.03 | +0.00 | — |
| Mining royalty / mineral tax burden (`P_MINING_ROYALTY`) | +1 = higher | -1.50 | -1.50 | +0.00 | +0.00 | +0.00 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -1.46 | -1.20 | -0.04 | -0.18 | -0.04 | — |
| Railway capex (`P_RAILWAY_CAPEX`) | +10% | +1.43 | +1.20 | +0.12 | +0.11 | +0.00 | — |
| Iron ore price (`F_IRON_ORE`) | +15% iron ore | +1.24 | +0.50 | +0.00 | +0.76 | -0.02 | -12.5% |
| US–China trade decoupling (`C_US_CHINA_DECOUPLING`) | +1 = more decoupling | -1.13 | +0.00 | +0.00 | +0.32 | -1.45 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Global and Indian steel prices at multi-year highs (global HRC +60% y/y) (`EV_STEEL_RALLY_2026`) | occurred | 1.00 | +16.2% | +16.2% | +16.5 | -0.3 | -0.0 | +0.0 |
| Coking coal price spike squeezes Indian steel margins (`EV_COKING_COAL_SURGE_AUG26`) | occurred | 1.00 | -4.5% | -4.5% | -4.4 | -0.1 | -0.0 | +0.0 |
| DGTR recommends/imposes anti-dumping duty on hot-rolled flat steel from China, Japan, Russia (`EV_INDIA_HR_STEEL_AD_PROVISIONAL`) | anticipated | 0.55 | +7.6% | +4.2% | +7.6 | +0.0 | -0.0 | +0.0 |
| India Q1 FY27 GDP grows 7.8% (31 Aug 2026), beating ~7.3% consensus (`EV_GDP_Q1FY27_7_8`) | occurred | 1.00 | +3.8% | +3.8% | +2.9 | +1.0 | -0.1 | -0.0 |
| Chinese steel/aluminium export surge floods Asia as China demand stays weak (`EV_CHINA_STEEL_EXPORT_FLOOD`) | risk_scenario | 0.25 | -10.6% | -2.6% | +0.0 | -11.4 | +0.9 | +0.0 |
| EU quota-halving steel regime and CBAM cut Indian steel exports to EU (`EV_EU_STEEL_REGIME_CBAM_HITS_INDIA`) | occurred | 1.00 | -2.2% | -2.2% | -2.2 | +0.0 | +0.0 | +0.0 |
| China enforces steel output cuts / export licensing discipline ('anti-involution') (`EV_CHINA_STEEL_OUTPUT_CURB_2027`) | anticipated | 0.50 | +3.3% | +1.7% | -0.1 | +3.8 | -0.3 | +0.0 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -1.5% | -1.5% | -1.2 | -0.0 | -0.2 | -0.0 |
| India relaxes steel import curbs early (safeguard cut/exemptions) after inflation or FTA pressure (`EV_STEEL_SAFEGUARD_EARLY_RELAXATION`) | risk_scenario | 0.15 | -9.1% | -1.4% | -9.1 | +0.0 | +0.0 | +0.0 |
| Iron ore at two-year low; NMDC price cuts then partial hike (`EV_IRON_ORE_TWO_YEAR_LOW`) | occurred | 1.00 | -1.0% | -1.0% | -0.4 | +0.0 | -0.6 | +0.0 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | +1.0% | +1.0% | +0.0 | +0.4 | +0.7 | -0.0 |
| Rupee at 95-96/USD and heavy RBI FX defence; reserves fall ~US$55bn from peak (`EV_RUPEE_DEFENCE_RESERVES_26`) | occurred | 1.00 | -1.0% | -1.0% | -0.4 | -0.6 | +0.0 | -0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_INDIA_HR_STEEL_AD_PROVISIONAL ⇒ F_STEEL_INDIA → SAIL | +6.00% | +3.30% |
| 2 | EV_CHINA_STEEL_EXPORT_FLOOD ⇒ F_STEEL_GLOBAL → F_STEEL_INDIA → SAIL | -7.40% | -1.85% |
| 1 | EV_STEEL_SAFEGUARD_EARLY_RELAXATION ⇒ F_STEEL_INDIA → SAIL | -7.50% | -1.12% |
| 2 | EV_CHINA_STEEL_EXPORT_FLOOD ⇒ F_CHINA_STEEL_EXPORTS → F_STEEL_INDIA → SAIL | -4.50% | -1.12% |
| 2 | EV_CHINA_NPC_MAR27_BIG_STIMULUS ⇒ F_CHINA_GDP → F_COKING_COAL → SAIL | -3.20% | -1.12% |
| 2 | EV_CHINA_STEEL_OUTPUT_CURB_2027 ⇒ F_STEEL_GLOBAL → F_STEEL_INDIA → SAIL | +2.22% | +1.11% |
| 2 | EV_CHINA_STEEL_OUTPUT_CURB_2027 ⇒ F_CHINA_STEEL_EXPORTS → F_STEEL_INDIA → SAIL | +1.80% | +0.90% |
| 1 | EV_INDIA_HR_STEEL_AD_PROVISIONAL ⇒ P_STEEL_DUTY_IN → SAIL | +1.60% | +0.88% |
| 3 | EV_CHINA_NPC_MAR27_BIG_STIMULUS ⇒ F_CHINA_GDP → F_CHINA_STEEL_EXPORTS → F_STEEL_INDIA → SAIL | +1.69% | +0.59% |
| 2 | EV_CHINA_CEWC_STIMULUS_DEC26 ⇒ F_CHINA_GDP → F_COKING_COAL → SAIL | -1.28% | -0.58% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → SAIL | -1.20% | -0.50% |
| 1 | EV_UNION_BUDGET_FEB27_METALS ⇒ F_COKING_COAL → SAIL | +1.36% | +0.48% |
| 4 | EV_CHINA_NPC_MAR27_BIG_STIMULUS ⇒ F_CHINA_GDP → F_CHINA_STEEL_EXPORTS → F_STEEL_GLOBAL → F_STEEL_INDIA → SAIL | +1.33% | +0.46% |
| 1 | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → SAIL | +0.50% | +0.45% |
| 2 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_USDINR → F_STEEL_INDIA → SAIL | +2.34% | +0.42% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_STEEL_INDIA → SAIL | +1.35 | events | +20.25% |
| 1 | F_COKING_COAL → SAIL | +1.30 | events | -10.40% |
| 1 | F_REPO_IN → SAIL | +1.00 | events | -1.20% |
| 1 | F_GOVT_CAPEX → SAIL | +0.20 | director_override | +0.50% |
| 1 | F_IRON_ORE → SAIL | -0.83 | observed | -0.42% |
| 1 | F_GDP_IN → SAIL | +0.50 | events | +0.40% |
| 1 | F_USDINR → SAIL | -0.37 | observed | -0.37% |
| 2 | F_STEEL_INDIA → P_STEEL_DUTY_IN → SAIL | +1.35 | events | -0.32% |
| 3 | F_CHINA_GDP → F_CHINA_STEEL_EXPORTS → P_STEEL_DUTY_IN → SAIL | +0.30 | events | -0.05% |
| 3 | F_USDCNY → F_CHINA_STEEL_EXPORTS → P_STEEL_DUTY_IN → SAIL | -0.47 | observed | -0.03% |
| 3 | C_US_CHINA_DECOUPLING → F_CHINA_STEEL_EXPORTS → P_STEEL_DUTY_IN → SAIL | -0.10 | events | -0.01% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2027-02 | Q3 FY27 results (Q2 on 2026-10-27) | results | 0.95 | +0.0% | +0.00% |
| 2027-03 | Wage-agreement renewal for executives/workers due around end of the current cycle (model knowledge, unverified) | other | 0.40 | -3.5% | -1.40% |
| 2027-06 | Government stake sale (OFS) in SAIL | corporate_action | 0.07 | -5.5% | -0.39% |

## Analyst profile (agent research, sourced)
# SAIL — Steel Authority of India Ltd. (Midcap 100, I_STEEL) — as of 2026-11-05

## Business
Government-owned (65%) integrated steel producer with plants at Bhilai, Durgapur, Rourkela, Bokaro and Burnpur, about 20 Mtpa crude capacity going to 35 Mtpa. Strong public-sector franchise: rails, structurals, plates, defence and special steels. Captive iron ore and limestone, but about 70% of coking coal is imported (model knowledge). Q2 FY27: sales Rs31,998 cr, EBITDA Rs4,216 cr (13%), PAT Rs1,750 cr (about four-fold YoY). TTM sales Rs116,428 cr, EBITDA Rs15,072 cr; market cap Rs69,599 cr. FY27 capex raised to Rs15,000 cr; Rs50,000 cr internal funding expected (2026-10-31).

## What moves the stock
1. **Indian steel price** (+15 per +7%): highest operating leverage in the group; margin 13% on a heavy fixed-cost base.
2. **Coking coal** (-8 per +15%) with ~70% import dependence.
3. **Government/railway capex** (+2.5, +1.2), **import-duty policy** (+2), **repo/discount rate** (-1.2), **USD/INR** (+1.0), royalty (-1.5), iron ore (+0.5), GDP (+0.8).

Pack empirical betas include strong wheat (+3.4) and edible-oil (+3.6) co-movements: these are rural-demand/commodity-sentiment proxies, not causal.

## Transmission examples
- **Coal path:** China supply shock -> coking coal +15% -> SAIL cost +4.2% before price hikes -> EBITDA -28% unpriced; 40% pass-through -> -17%; equity -8; third order: weaker profit slows self-funded 35 Mtpa expansion; fourth: government may need to fund or delay.
- **Fiscal path:** Government capex up (rails, bridges) -> rail and structural orders up -> utilisation up -> SAIL operating leverage; the Budget and railway capex announcements are the transmission.
- **Policy path:** Import curbs tightened -> HRC import parity rises -> domestic price +4-6% -> SAIL EBITDA +25-30%; SMM (2026-10-07) reports the ministry unlikely to tighten.
- **Disinvestment path:** Fiscal pressure -> OFS in PSU metals (as with Hindustan Copper in August) -> supply overhang -> SAIL -5%.

## Current situation
Strong profit recovery; stock reacted -4% on the Q2 print (Investing.com 2026-10-28) despite profit +315%. In F&O ban (2026-11-03). Target raised to Rs188 on 2026-11-04 (TradingView).

## Upcoming events
Q3 results Feb 2027; wage-agreement renewal (model knowledge, unverified); safeguard duty decision; possible OFS (low probability).

## Bull and bear
Bull: price hikes stick, expansion on time, leverage falls. Bear: coal squeeze, import surge, capex overruns, government stake sale. Confidence medium; net debt and import share are model estimates.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.