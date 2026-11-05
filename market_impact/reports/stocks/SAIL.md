# SAIL — Steel Authority of India Ltd.
*MIDCAP_100 · Metals & Mining · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +5.5%**, **12 months +11.7%** (rank 9 / 5 of 200 for 3m / 12m); beta 1.29
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +30.7%): 3 months 64%, 12 months 68%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 +2.8% … P90 +25.0%; plausible 12m relative-return range incl. stock-specific noise: -24.9% … +50.7%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +3.8 pp (model impact +7.6% beta-adjusted vs realised market-adjusted move -23.2%); forward event exposure +19.0% (3m +7.9%; half assumed priced); company-specific events -0.8%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Indian domestic steel price (`F_STEEL_INDIA`) | +7% domestic HRC/rebar price | +14.74 | +15.00 | -0.24 | -0.02 | +0.00 | — |
| Global HRC steel price (`F_STEEL_GLOBAL`) | +10% global HRC | +7.16 | +0.00 | +7.40 | -0.22 | -0.01 | +20.6% |
| Coking coal price (`F_COKING_COAL`) | +15% coking coal | -5.60 | -8.00 | +1.50 | +0.93 | -0.03 | — |
| Indian safeguard/anti-dumping duty on steel imports (`P_STEEL_DUTY_IN`) | +10 pp effective duty | +4.99 | +2.00 | +3.00 | +0.00 | -0.01 | — |
| China growth / stimulus (`F_CHINA_GDP`) | +1 pp | +4.35 | +0.00 | -2.97 | +4.80 | +2.52 | — |
| China steel exports (`F_CHINA_STEEL_EXPORTS`) | +15% y/y | -3.97 | +0.00 | -2.68 | -1.37 | +0.08 | — |
| Central + state government capex (`F_GOVT_CAPEX`) | +10% capex growth | +3.49 | +2.50 | +1.19 | -0.12 | -0.08 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | +2.54 | +1.00 | +1.75 | -0.21 | +0.00 | -1.1% |
| EU steel safeguard / CBAM burden on imports (`NEW_EU_STEEL_ACCESS`) | +1 = tightening step (quota cut / higher out-of-quota tariff / CBAM cost) | -1.75 | +0.00 | -1.80 | +0.05 | +0.00 | — |
| US–China trade decoupling (`C_US_CHINA_DECOUPLING`) | +1 = more decoupling | -1.52 | +0.00 | +0.00 | +0.32 | -1.84 | — |
| Mining royalty / mineral tax burden (`P_MINING_ROYALTY`) | +1 = higher | -1.50 | -1.50 | +0.00 | +0.00 | +0.00 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | +1.48 | +0.00 | +0.00 | +0.28 | +1.20 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -1.47 | -1.20 | -0.04 | -0.18 | -0.05 | — |
| Railway capex (`P_RAILWAY_CAPEX`) | +10% | +1.42 | +1.20 | +0.12 | +0.11 | -0.01 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Global and Indian steel prices at multi-year highs (global HRC +60% y/y) (`EV_STEEL_RALLY_2026`) | occurred | 1.00 | +11.0% | +11.0% | +11.4 | -0.3 | -0.0 | +0.0 |
| Coking coal price spike squeezes Indian steel margins (`EV_COKING_COAL_SURGE_AUG26`) | occurred | 1.00 | -7.5% | -7.5% | -7.4 | -0.1 | -0.0 | +0.0 |
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | +6.1% | +6.1% | +0.0 | +1.1 | +4.8 | +0.2 |
| DGTR recommends/imposes anti-dumping duty on hot-rolled flat steel from China, Japan, Russia (`EV_INDIA_HR_STEEL_AD_PROVISIONAL`) | anticipated | 0.55 | +7.6% | +4.2% | +7.6 | +0.0 | -0.0 | +0.0 |
| India Q1 FY27 GDP grows 7.8% (31 Aug 2026), beating ~7.3% consensus (`EV_GDP_Q1FY27_7_8`) | occurred | 1.00 | +3.6% | +3.6% | +2.9 | +0.9 | -0.1 | -0.1 |
| Union Budget 2027-28 capex/railway allocation (infra, railways, defence) (`EV_BUDGET27_CAPEX_RAILWAY`) | scheduled | 0.90 | +3.8% | +3.4% | +3.0 | +1.0 | -0.1 | -0.1 |
| Retail petrol/diesel price freeze with crude >$100 squeezes OMC marketing margins; Q2 FY27 results split refiners (`EV_OMC_FUEL_FREEZE_LOSSES`) | occurred | 1.00 | -3.1% | -3.1% | +0.0 | -1.8 | -1.4 | +0.1 |
| Chinese steel/aluminium export surge floods Asia as China demand stays weak (`EV_CHINA_STEEL_EXPORT_FLOOD`) | risk_scenario | 0.25 | -9.7% | -2.4% | +0.0 | -11.4 | +1.7 | +0.0 |
| EU quota-halving steel regime and CBAM cut Indian steel exports to EU (`EV_EU_STEEL_REGIME_CBAM_HITS_INDIA`) | occurred | 1.00 | -2.2% | -2.2% | -2.2 | +0.0 | +0.0 | +0.0 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | +1.8% | +1.8% | +0.0 | +0.5 | +1.5 | -0.2 |
| China Dec CEWC / Mar 2027 NPC delivers large fiscal stimulus and consumption push (`EV_CHINA_NPC_MAR27_BIG_STIMULUS`) | anticipated | 0.35 | +4.5% | +1.6% | +0.0 | -3.0 | +4.9 | +2.6 |
| China Q3 GDP +4.5% (beat); property 'mini-stimulus' of late September; PMI 49.3; LPR unchanged (`EV_CHINA_Q3_GDP_AND_MINI_STIMULUS`) | occurred | 1.00 | +1.5% | +1.5% | +0.0 | -0.9 | +1.6 | +0.9 |

## Strongest causal chains (1st–4th order)
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_STEEL_RALLY_2026 ⇒ F_STEEL_INDIA → SAIL | +21.00% | +21.00% |
| 1 | EV_COKING_COAL_SURGE_AUG26 ⇒ F_COKING_COAL → SAIL | -13.36% | -13.36% |
| 1 | EV_STEEL_RALLY_2026 ⇒ F_COKING_COAL → SAIL | -9.60% | -9.60% |
| 1 | EV_COKING_COAL_SURGE_AUG26 ⇒ F_STEEL_INDIA → SAIL | +6.00% | +6.00% |
| 3 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_USDINR → F_STEEL_INDIA → SAIL | +5.28% | +5.28% |
| 1 | EV_INDIA_HR_STEEL_AD_PROVISIONAL ⇒ F_STEEL_INDIA → SAIL | +6.00% | +3.30% |
| 1 | EV_GDP_Q1FY27_7_8 ⇒ F_GOVT_CAPEX → SAIL | +2.50% | +2.50% |
| 1 | EV_EU_STEEL_REGIME_CBAM_HITS_INDIA ⇒ F_STEEL_INDIA → SAIL | -2.25% | -2.25% |
| 1 | EV_UNION_BUDGET_FEB27_METALS ⇒ F_COKING_COAL → SAIL | +2.40% | +2.16% |
| 2 | EV_CHINA_STEEL_EXPORT_FLOOD ⇒ F_STEEL_GLOBAL → F_STEEL_INDIA → SAIL | -7.40% | -1.85% |
| 2 | EV_OMC_FUEL_FREEZE_LOSSES ⇒ NEW_OMC_MARKETING_MARGIN → F_GOVT_CAPEX → SAIL | -1.80% | -1.80% |
| 1 | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → SAIL | +2.00% | +1.80% |
| 2 | EV_CPI_REACCEL_SEP26 ⇒ F_CPI_IN → F_REPO_IN → SAIL | -1.59% | -1.59% |
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_USDINR → SAIL | +1.56% | +1.56% |
| 3 | EV_OMC_FUEL_FREEZE_LOSSES ⇒ NEW_OMC_MARKETING_MARGIN → F_GOVT_CAPEX → F_STEEL_INDIA → SAIL | -1.42% | -1.42% |

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