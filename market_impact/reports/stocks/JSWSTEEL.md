# JSWSTEEL — JSW Steel Ltd.
*NIFTY_50 · Metals & Mining · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +0.4%**, **12 months +2.3%** (rank 62 / 13 of 200 for 3m / 12m); beta 1.04
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +17.0%): 3 months 52%, 12 months 57%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -2.7% … P90 +8.4%; plausible 12m relative-return range incl. stock-specific noise: -20.8% … +24.3%
- Decomposition (12m): 0.5 × forward event exposure +3.7% (3m +1.0%; half assumed priced; market-priced macro drift removed) + 0.5 × company-specific catalysts +1.4%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply +8.5% (beta-adjusted) vs a realised market-adjusted move of -0.4% — gap +8.8 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Indian domestic steel price (`F_STEEL_INDIA`) | +7% domestic HRC/rebar price | +8.82 | +9.00 | -0.18 | -0.00 | +0.00 | — |
| Global HRC steel price (`F_STEEL_GLOBAL`) | +10% global HRC | +4.36 | +0.00 | +4.44 | -0.08 | +0.00 | +20.6% |
| Coking coal price (`F_COKING_COAL`) | +15% coking coal | -4.07 | -5.50 | +0.90 | +0.55 | -0.02 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | +3.41 | +2.50 | +1.03 | -0.12 | +0.00 | -1.1% |
| Indian safeguard/anti-dumping duty on steel imports (`P_STEEL_DUTY_IN`) | +10 pp effective duty | +3.30 | +1.50 | +1.80 | +0.00 | +0.00 | — |
| Central + state government capex (`F_GOVT_CAPEX`) | +10% capex growth | +2.69 | +2.00 | +0.77 | -0.04 | -0.05 | — |
| China steel exports (`F_CHINA_STEEL_EXPORTS`) | +15% y/y | -2.64 | +0.00 | -1.56 | -1.11 | +0.03 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -1.54 | -1.20 | -0.15 | -0.16 | -0.03 | — |
| EU steel safeguard / CBAM burden on imports (`NEW_EU_STEEL_ACCESS`) | +1 = tightening step (quota cut / higher out-of-quota tariff / CBAM cost) | -1.32 | -0.80 | -0.54 | +0.02 | +0.00 | — |
| Iron ore price (`F_IRON_ORE`) | +15% iron ore | -1.06 | -1.50 | +0.00 | +0.46 | -0.02 | -12.5% |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | +0.94 | +0.00 | +0.00 | +0.56 | +0.37 | — |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +0.87 | +0.00 | +0.66 | +0.26 | -0.05 | — |
| Indian vehicle demand (`F_AUTO_DEMAND_IN`) | +10% volumes | +0.80 | +0.80 | +0.00 | +0.00 | +0.00 | — |
| General-government fiscal slippage / extra borrowing vs budget (Centre + states) (`NEW_FISCAL_SLIPPAGE_IN`) | +0.5 pp of GDP deficit above budget (~Rs2 lakh cr) | -0.78 | +0.00 | -0.64 | -0.18 | +0.03 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Global and Indian steel prices at multi-year highs (global HRC +60% y/y) (`EV_STEEL_RALLY_2026`) | occurred | 1.00 | +9.7% | +9.7% | +9.9 | -0.2 | -0.0 | +0.0 |
| Coking coal price spike squeezes Indian steel margins (`EV_COKING_COAL_SURGE_AUG26`) | occurred | 1.00 | -3.6% | -3.6% | -3.6 | -0.1 | -0.0 | +0.0 |
| India Q1 FY27 GDP grows 7.8% (31 Aug 2026), beating ~7.3% consensus (`EV_GDP_Q1FY27_7_8`) | occurred | 1.00 | +2.9% | +2.9% | +2.4 | +0.6 | -0.1 | -0.0 |
| DGTR recommends/imposes anti-dumping duty on hot-rolled flat steel from China, Japan, Russia (`EV_INDIA_HR_STEEL_AD_PROVISIONAL`) | anticipated | 0.55 | +4.8% | +2.6% | +4.8 | +0.0 | -0.0 | +0.0 |
| EU quota-halving steel regime and CBAM cut Indian steel exports to EU (`EV_EU_STEEL_REGIME_CBAM_HITS_INDIA`) | occurred | 1.00 | -2.1% | -2.1% | -2.1 | +0.0 | +0.0 | +0.0 |
| Chinese steel/aluminium export surge floods Asia as China demand stays weak (`EV_CHINA_STEEL_EXPORT_FLOOD`) | risk_scenario | 0.25 | -6.2% | -1.6% | +0.0 | -6.8 | +0.5 | +0.0 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -1.6% | -1.6% | -1.2 | -0.1 | -0.2 | -0.0 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | +1.4% | +1.4% | +0.0 | +1.0 | +0.4 | -0.0 |
| Rupee at 95-96/USD and heavy RBI FX defence; reserves fall ~US$55bn from peak (`EV_RUPEE_DEFENCE_RESERVES_26`) | occurred | 1.00 | -1.3% | -1.3% | -0.9 | -0.4 | +0.0 | -0.0 |
| China enforces steel output cuts / export licensing discipline ('anti-involution') (`EV_CHINA_STEEL_OUTPUT_CURB_2027`) | anticipated | 0.50 | +2.5% | +1.3% | +0.4 | +2.3 | -0.2 | +0.0 |
| Iron ore at two-year low; NMDC price cuts then partial hike (`EV_IRON_ORE_TWO_YEAR_LOW`) | occurred | 1.00 | +0.9% | +0.9% | +1.2 | +0.0 | -0.4 | +0.0 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | -1.7% | -0.9% | +0.0 | -1.3 | -0.5 | +0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_INDIA_HR_STEEL_AD_PROVISIONAL ⇒ F_STEEL_INDIA → JSWSTEEL | +3.60% | +1.98% |
| 2 | EV_CHINA_STEEL_EXPORT_FLOOD ⇒ F_STEEL_GLOBAL → F_STEEL_INDIA → JSWSTEEL | -4.44% | -1.11% |
| 2 | EV_CHINA_NPC_MAR27_BIG_STIMULUS ⇒ F_CHINA_GDP → F_COKING_COAL → JSWSTEEL | -2.20% | -0.77% |
| 2 | EV_CHINA_STEEL_EXPORT_FLOOD ⇒ F_CHINA_STEEL_EXPORTS → F_STEEL_INDIA → JSWSTEEL | -2.70% | -0.68% |
| 1 | EV_STEEL_SAFEGUARD_EARLY_RELAXATION ⇒ F_STEEL_INDIA → JSWSTEEL | -4.50% | -0.67% |
| 2 | EV_CHINA_STEEL_OUTPUT_CURB_2027 ⇒ F_STEEL_GLOBAL → F_STEEL_INDIA → JSWSTEEL | +1.33% | +0.67% |
| 1 | EV_INDIA_HR_STEEL_AD_PROVISIONAL ⇒ P_STEEL_DUTY_IN → JSWSTEEL | +1.20% | +0.66% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_USDINR → JSWSTEEL | +3.25% | +0.58% |
| 2 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → F_USDINR → JSWSTEEL | -1.15% | -0.58% |
| 2 | EV_CHINA_STEEL_OUTPUT_CURB_2027 ⇒ F_CHINA_STEEL_EXPORTS → F_STEEL_INDIA → JSWSTEEL | +1.08% | +0.54% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → JSWSTEEL | -1.20% | -0.50% |
| 1 | EV_CHINA_CEWC_STIMULUS_DEC26 ⇒ F_IRON_ORE → JSWSTEEL | -0.90% | -0.40% |
| 2 | EV_CHINA_CEWC_STIMULUS_DEC26 ⇒ F_CHINA_GDP → F_COKING_COAL → JSWSTEEL | -0.88% | -0.40% |
| 2 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → F_USDINR → JSWSTEEL | -0.67% | -0.37% |
| 1 | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → JSWSTEEL | +0.40% | +0.36% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_STEEL_INDIA → JSWSTEEL | +1.35 | events | +12.15% |
| 1 | F_COKING_COAL → JSWSTEEL | +1.30 | events | -7.15% |
| 1 | F_IRON_ORE → JSWSTEEL | -0.83 | observed | +1.25% |
| 1 | F_REPO_IN → JSWSTEEL | +1.00 | events | -1.20% |
| 1 | F_USDINR → JSWSTEEL | -0.37 | observed | -0.92% |
| 1 | NEW_EU_STEEL_ACCESS → JSWSTEEL | +1.00 | events | -0.80% |
| 1 | F_GDP_IN → JSWSTEEL | +0.50 | events | +0.40% |
| 1 | F_GOVT_CAPEX → JSWSTEEL | +0.20 | director_override | +0.40% |
| 1 | F_AUTO_DEMAND_IN → JSWSTEEL | +0.50 | director_override | +0.40% |
| 2 | F_STEEL_INDIA → P_STEEL_DUTY_IN → JSWSTEEL | +1.35 | events | -0.24% |
| 1 | F_EU_GDP → JSWSTEEL | +0.22 | events | +0.09% |
| 3 | F_CHINA_GDP → F_CHINA_STEEL_EXPORTS → P_STEEL_DUTY_IN → JSWSTEEL | +0.30 | events | -0.04% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-10-22 | Board approves Rs7,500 cr Sambalpur expansion (occurred; stock -3.1% that day) | capex | 1.00 | +0.0% | +0.00% |
| 2027-01 | Q3 FY27 results (late Jan); monthly production updates in first week of each month | results | 0.95 | +0.0% | +0.00% |
| 2027-03 | Draft National Steel Policy 2047 finalised (604 Mt capacity target, consultation open) | regulatory | 0.40 | +1.0% | +0.40% |
| 2027-03 | Safeguard/anti-dumping duty review or tightening on flat steel imports | regulatory | 0.25 | +4.0% | +1.00% |

## Analyst profile (agent research, sourced)
# JSWSTEEL — JSW Steel Ltd. (Nifty 50, I_STEEL) — as of 2026-11-05

## Business
India's second-largest steelmaker (JSW Group): integrated flat and long steel at Vijayanagar, Dolvi, Salem and Bhushan Power & Steel, with captive iron-ore mines in Karnataka and Odisha and growing coated/special-steel capacity. About 87% of sales are domestic. Q2 FY27 (Sep 2026): sales Rs54,486 cr, EBITDA Rs10,120 cr (19% margin), consolidated PAT Rs5,359 cr (about three-fold YoY; other outlets quote Rs5,279 cr), record volumes, falling interest cost (Rs1,602 cr vs Rs2,413 cr a year earlier). TTM EBITDA Rs34,248 cr; market cap Rs3.32 lakh cr. Board approved Rs7,500 cr Sambalpur expansion on 2026-10-22.

## What moves the stock
1. **Domestic steel price** (+9 per +7%): the spread over imported coking coal is the earnings engine; central weight lower than the mechanical +13.5 because price and coking-coal cost rise together.
2. **Coking coal** (-5.5 per +15%): about a quarter of costs, mostly imported; Reuters (2026-08-19) flagged the squeeze.
3. **Government capex** (+2) and **USD/INR** (+2.5, low confidence), **safeguard policy** (+1.5), **repo/discount rate** (-1.2), **iron ore** (-1.5 cost-side; pack shows +2.3 because ore and steel prices co-move), auto demand (+0.8).

## Transmission examples
- **Gulf peace -> cheaper energy -> steel:** Iran talks ease Hormuz risk -> Brent falls -> freight and power costs fall (1st order, small) -> INR firms -> imported coking coal cheaper in rupees but import-parity HRC also falls (2nd) -> price-cost spread roughly stable; fourth order: lower inflation lets RBI hold or cut, helping housing and capex demand for long products.
- **China path:** Yuan weakens or China exports rise -> import-parity HRC down in India -> domestic prices fall (the Sep 2026 'import parity' ceiling, NDTV Profit) -> JSW EBITDA/t compresses -> equity down; the Indian response (safeguard tightening) is a policy option with probability ~0.25.
- **Coal path:** China supply shock (Argus) -> coking coal up -> cost up before price hikes -> margin squeeze for a quarter, then partial pass-through; JSW has less captive coal than Tata Steel, so the hit is bigger.
- **Demand path:** Government capex up -> infrastructure steel demand up -> utilisation and prices firmer -> operating leverage on large fixed cost.

## Current situation
Record quarter, but the stock fell about 3% on the day on the Sambalpur capex and then rose 6% on 2026-10-26 as brokers saw up to 39% upside. Net debt is falling. The stock is -13.7% over 3m. Draft National Steel Policy 2047 (2026-10-11) sets 604 Mt capacity and triples coking-coal demand, a mild cost-risk signal for import-reliant mills.

## Upcoming events
Q3 results in late Jan 2027; monthly production updates; Steel Policy finalisation (prob 0.4 by Mar 2027); possible safeguard tightening (0.25).

## Bull and bear
Bull: price hikes stick, coal stabilises, deleveraging continues. Bear: Chinese export wave, coking-coal rally, capex-led leverage, CBAM. Confidence medium; cost shares are model estimates because the pack lacks a cost breakdown.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.