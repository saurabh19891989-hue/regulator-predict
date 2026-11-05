# JSWSTEEL — JSW Steel Ltd.
*NIFTY_50 · Metals & Mining · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +3.3%**, **12 months +8.5%** (rank 27 / 19 of 200 for 3m / 12m); beta 1.04
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +17.0%): 3 months 65%, 12 months 70%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 +0.1% … P90 +21.4%; plausible 12m relative-return range incl. stock-specific noise: -16.2% … +34.6%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +2.3 pp (model impact +4.6% beta-adjusted vs realised market-adjusted move -0.4%); forward event exposure +13.4% (3m +5.4%; half assumed priced); company-specific events +1.4%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Indian domestic steel price (`F_STEEL_INDIA`) | +7% domestic HRC/rebar price | +8.81 | +9.00 | -0.18 | -0.01 | +0.00 | — |
| Global HRC steel price (`F_STEEL_GLOBAL`) | +10% global HRC | +4.26 | +0.00 | +4.44 | -0.17 | -0.01 | +20.6% |
| Coking coal price (`F_COKING_COAL`) | +15% coking coal | -4.07 | -5.50 | +0.90 | +0.55 | -0.02 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | +3.32 | +2.50 | +1.03 | -0.20 | -0.01 | -1.1% |
| Indian safeguard/anti-dumping duty on steel imports (`P_STEEL_DUTY_IN`) | +10 pp effective duty | +3.29 | +1.50 | +1.80 | +0.00 | -0.01 | — |
| Central + state government capex (`F_GOVT_CAPEX`) | +10% capex growth | +2.55 | +2.00 | +0.77 | -0.11 | -0.11 | — |
| China steel exports (`F_CHINA_STEEL_EXPORTS`) | +15% y/y | -2.31 | +0.00 | -1.56 | -0.81 | +0.06 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | +1.69 | +0.00 | +0.00 | +0.87 | +0.82 | — |
| China growth / stimulus (`F_CHINA_GDP`) | +1 pp | +1.65 | +0.00 | -2.90 | +3.05 | +1.50 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -1.55 | -1.20 | -0.15 | -0.16 | -0.04 | — |
| US dollar index (`F_DXY`) | +3% DXY | +1.35 | +0.00 | +0.59 | +0.70 | +0.06 | +2.2% |
| Brent crude oil price (`F_BRENT`) | +10% Brent | +1.22 | +0.00 | +0.69 | +0.61 | -0.08 | +0.0% |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -1.15 | +0.00 | -0.88 | -0.04 | -0.22 | — |
| Iron ore price (`F_IRON_ORE`) | +15% iron ore | -1.06 | -1.50 | +0.00 | +0.46 | -0.02 | -12.5% |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | +6.4% | +6.4% | +0.0 | +3.4 | +3.2 | -0.2 |
| Global and Indian steel prices at multi-year highs (global HRC +60% y/y) (`EV_STEEL_RALLY_2026`) | occurred | 1.00 | +5.7% | +5.7% | +6.0 | -0.3 | -0.0 | +0.0 |
| Coking coal price spike squeezes Indian steel margins (`EV_COKING_COAL_SURGE_AUG26`) | occurred | 1.00 | -5.7% | -5.7% | -5.6 | -0.1 | -0.0 | +0.0 |
| India Q1 FY27 GDP grows 7.8% (31 Aug 2026), beating ~7.3% consensus (`EV_GDP_Q1FY27_7_8`) | occurred | 1.00 | +2.7% | +2.7% | +2.4 | +0.5 | -0.1 | -0.1 |
| DGTR recommends/imposes anti-dumping duty on hot-rolled flat steel from China, Japan, Russia (`EV_INDIA_HR_STEEL_AD_PROVISIONAL`) | anticipated | 0.55 | +4.8% | +2.6% | +4.8 | +0.0 | -0.0 | +0.0 |
| Retail petrol/diesel price freeze with crude >$100 squeezes OMC marketing margins; Q2 FY27 results split refiners (`EV_OMC_FUEL_FREEZE_LOSSES`) | occurred | 1.00 | -2.2% | -2.2% | +0.0 | -1.4 | -0.9 | +0.1 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | +1.9% | +1.9% | +0.0 | +1.1 | +0.9 | -0.2 |
| Union Budget 2027-28 capex/railway allocation (infra, railways, defence) (`EV_BUDGET27_CAPEX_RAILWAY`) | scheduled | 0.90 | +2.0% | +1.8% | +1.6 | +0.6 | -0.1 | -0.1 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -1.6% | -1.6% | -1.2 | -0.1 | -0.2 | -0.0 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.36 | +4.2% | +1.5% | +0.0 | +2.1 | +2.0 | +0.0 |
| Chinese steel/aluminium export surge floods Asia as China demand stays weak (`EV_CHINA_STEEL_EXPORT_FLOOD`) | risk_scenario | 0.25 | -5.7% | -1.4% | +0.0 | -6.8 | +1.1 | +0.0 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -1.3% | -1.3% | +0.0 | -1.0 | -0.1 | -0.2 |

## Strongest causal chains (1st–4th order)
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_STEEL_RALLY_2026 ⇒ F_STEEL_INDIA → JSWSTEEL | +12.60% | +12.60% |
| 1 | EV_COKING_COAL_SURGE_AUG26 ⇒ F_COKING_COAL → JSWSTEEL | -9.18% | -9.18% |
| 1 | EV_STEEL_RALLY_2026 ⇒ F_COKING_COAL → JSWSTEEL | -6.60% | -6.60% |
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_USDINR → JSWSTEEL | +3.91% | +3.91% |
| 1 | EV_COKING_COAL_SURGE_AUG26 ⇒ F_STEEL_INDIA → JSWSTEEL | +3.60% | +3.60% |
| 3 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_USDINR → F_STEEL_INDIA → JSWSTEEL | +3.17% | +3.17% |
| 1 | EV_GDP_Q1FY27_7_8 ⇒ F_GOVT_CAPEX → JSWSTEEL | +2.00% | +2.00% |
| 1 | EV_INDIA_HR_STEEL_AD_PROVISIONAL ⇒ F_STEEL_INDIA → JSWSTEEL | +3.60% | +1.98% |
| 2 | EV_CPI_REACCEL_SEP26 ⇒ F_CPI_IN → F_REPO_IN → JSWSTEEL | -1.59% | -1.59% |
| 1 | EV_UNION_BUDGET_FEB27_METALS ⇒ F_COKING_COAL → JSWSTEEL | +1.65% | +1.48% |
| 1 | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → JSWSTEEL | +1.60% | +1.44% |
| 2 | EV_OMC_FUEL_FREEZE_LOSSES ⇒ NEW_OMC_MARKETING_MARGIN → F_GOVT_CAPEX → JSWSTEEL | -1.44% | -1.44% |
| 1 | EV_EU_STEEL_REGIME_CBAM_HITS_INDIA ⇒ F_STEEL_INDIA → JSWSTEEL | -1.35% | -1.35% |
| 1 | EV_IRON_ORE_TWO_YEAR_LOW ⇒ F_IRON_ORE → JSWSTEEL | +1.24% | +1.24% |
| 1 | EV_RBI_OCT26_HIKE25 ⇒ F_REPO_IN → JSWSTEEL | -1.20% | -1.20% |

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