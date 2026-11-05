# BDL — Bharat Dynamics Ltd.
*MIDCAP_100 · Capital Goods · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +4.6%**, **12 months +12.7%** (rank 15 / 3 of 200 for 3m / 12m); beta 1.40
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +40.7%): 3 months 59%, 12 months 55%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 +9.4% … P90 +25.8%; plausible 12m relative-return range incl. stock-specific noise: -33.3% … +80.2%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +5.5 pp (model impact +11.0% beta-adjusted vs realised market-adjusted move -17.5%); forward event exposure +12.9% (3m +4.0%; half assumed priced); company-specific events +4.0%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| India–Pakistan tension (`C_INDIA_PAKISTAN`) | +1 = escalation | +6.18 | +3.00 | +2.81 | +0.38 | -0.01 | — |
| Indian defence procurement & indigenisation (`P_DEFENCE_PROCUREMENT`) | +10% domestic orders | +5.42 | +5.00 | +0.42 | +0.00 | +0.00 | — |
| Indian defence exports (`T_DEFENCE_EXPORTS`) | +1 | +3.00 | +3.00 | +0.00 | +0.00 | +0.00 | — |
| Central + state government capex (`F_GOVT_CAPEX`) | +10% capex growth | +1.41 | +1.50 | +0.00 | -0.06 | -0.02 | — |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -1.10 | -1.00 | -0.05 | -0.04 | -0.02 | +3.5% |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -0.92 | -0.80 | -0.05 | -0.08 | +0.00 | -1.1% |
| US average effective tariff rate (all partners) (`NEW_US_TARIFF_GLOBAL`) | +5 pp effective tariff rate | -0.78 | +0.00 | -0.40 | -0.27 | -0.10 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -0.77 | +0.00 | -0.85 | +0.05 | +0.03 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -0.75 | +0.00 | -0.25 | -0.31 | -0.19 | — |
| Russia (oil discounts, defence, sanctions) (`C_RUSSIA`) | +1 = closer trade access / larger discounts | -0.75 | -0.80 | +0.00 | +0.02 | +0.03 | — |
| US equity market (`F_US_EQUITIES`) | +5% S&P 500 | +0.61 | +0.00 | +0.48 | +0.11 | +0.03 | +1.2% |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -0.56 | -0.60 | +0.03 | +0.01 | +0.00 | — |
| US–China trade decoupling (`C_US_CHINA_DECOUPLING`) | +1 = more decoupling | -0.51 | +0.00 | -0.40 | -0.11 | -0.00 | — |
| Chip/electronics component supply tightness (higher = tighter) (`F_SEMICONDUCTOR_SUPPLY`) | +1 = tightening | -0.50 | -0.50 | +0.00 | +0.00 | +0.00 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Union Budget 2027-28 capex/railway allocation (infra, railways, defence) (`EV_BUDGET27_CAPEX_RAILWAY`) | scheduled | 0.90 | +6.5% | +5.8% | +6.2 | +0.4 | -0.1 | -0.0 |
| DAC clears Rs 1.10 lakh crore (7 Sep) and further proposals (Rs 2.12 lakh crore reported 26 Oct) (`EV_DAC_APPROVALS_H2_26`) | occurred | 1.00 | +5.4% | +5.4% | +5.0 | +0.4 | +0.0 | +0.0 |
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -2.6% | -2.6% | +0.0 | -1.6 | -0.7 | -0.3 |
| New BrahMos/defence export contracts (Philippines follow-on, Indonesia, Vietnam or others) announced (`EV_DEFENCE_EXPORT_ORDERS`) | anticipated | 0.50 | +2.8% | +1.4% | +2.8 | +0.0 | +0.0 | +0.0 |
| India Q1 FY27 GDP grows 7.8% (31 Aug 2026), beating ~7.3% consensus (`EV_GDP_Q1FY27_7_8`) | occurred | 1.00 | +1.3% | +1.3% | +1.5 | -0.2 | -0.0 | -0.0 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.28 | -4.1% | -1.1% | -4.0 | +0.2 | -0.3 | -0.0 |
| Disorderly yen carry-trade unwind (Aug-2024-style) after BoJ/MoF action (`EV_YEN_CARRY_UNWIND_RISK`) | risk_scenario | 0.18 | -5.5% | -1.0% | -5.0 | -0.2 | -0.3 | -0.0 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -0.9% | -0.9% | +0.0 | -1.0 | +0.1 | +0.1 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -0.8% | -0.8% | -0.4 | -0.3 | -0.0 | -0.1 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.36 | -2.4% | -0.8% | -1.2 | -0.6 | -0.4 | -0.2 |
| Retail petrol/diesel price freeze with crude >$100 squeezes OMC marketing margins; Q2 FY27 results split refiners (`EV_OMC_FUEL_FREEZE_LOSSES`) | occurred | 1.00 | -0.8% | -0.8% | +0.0 | -1.1 | +0.2 | +0.1 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.58 | +1.2% | +0.7% | +0.5 | +0.3 | +0.2 | +0.1 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_BUDGET27_CAPEX_RAILWAY ⇒ P_DEFENCE_PROCUREMENT → BDL | +5.00% | +4.50% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → BDL | -4.00% | -1.12% |
| 1 | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → BDL | +1.20% | +1.08% |
| 1 | EV_DEFENCE_EXPORT_ORDERS ⇒ T_DEFENCE_EXPORTS → BDL | +1.80% | +0.90% |
| 1 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → BDL | -5.00% | -0.90% |
| 1 | EV_DEFENCE_EXPORT_ORDERS ⇒ P_DEFENCE_PROCUREMENT → BDL | +1.00% | +0.50% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_RISK_SENTIMENT → BDL | -1.20% | -0.43% |
| 2 | EV_INDIA_RETAIL_FUEL_HIKE ⇒ NEW_OMC_MARKETING_MARGIN → F_GOVT_CAPEX → BDL | +0.90% | +0.40% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_RISK_SENTIMENT → BDL | -1.44% | -0.36% |
| 2 | EV_BUDGET27_CAPEX_RAILWAY ⇒ P_DEFENCE_PROCUREMENT → T_DEFENCE_EXPORTS → BDL | +0.36% | +0.32% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_RISK_SENTIMENT → BDL | +0.50% | +0.29% |
| 1 | EV_INDIA_PAK_CRISIS ⇒ C_INDIA_PAKISTAN → BDL | +3.00% | +0.27% |
| 1 | EV_NVDA_NOV17_BEAT ⇒ F_RISK_SENTIMENT → BDL | +0.40% | +0.25% |
| 1 | EV_RUSSIAN_CRUDE_CUT_TRADE_DEAL ⇒ C_RUSSIA → BDL | +0.80% | +0.24% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → BDL | -0.60% | -0.24% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | P_DEFENCE_PROCUREMENT → BDL | +1.00 | events | +5.00% |
| 1 | F_GOVT_CAPEX → BDL | +1.00 | events | +1.50% |
| 1 | C_RUSSIA → BDL | +1.00 | events | -0.80% |
| 1 | F_REPO_IN → BDL | +1.00 | events | -0.60% |
| 1 | F_ALUMINIUM → BDL | -1.96 | observed | -0.59% |
| 2 | P_DEFENCE_PROCUREMENT → T_DEFENCE_EXPORTS → BDL | +1.00 | events | +0.36% |
| 1 | F_USDINR → BDL | -0.37 | observed | +0.30% |
| 1 | F_RISK_SENTIMENT → BDL | +0.11 | observed | -0.11% |
| 2 | F_AI_CAPEX → F_SEMICONDUCTOR_SUPPLY → BDL | -0.30 | events | +0.04% |
| 2 | C_US_CHINA_DECOUPLING → F_SEMICONDUCTOR_SUPPLY → BDL | -0.10 | events | +0.02% |
| 3 | C_US_CHINA_DECOUPLING → NEW_RARE_EARTH_SUPPLY → F_SEMICONDUCTOR_SUPPLY → BDL | -0.10 | events | +0.01% |

## Analyst profile (agent research, sourced)
# BDL - Bharat Dynamics Ltd. (Defence PSU, missiles)

## Business
Bharat Dynamics makes guided missiles and underwater weapons, principally for the Indian MoD, under DRDO designs (Akash, Astra) and foreign licences (Invar). The business is long-cycle: order book Rs26,176 cr is roughly nine times TTM sales, but delivery milestones are lumpy (FY26 sales -19%, Q1 FY27 +131%). Treasury income (Rs440 cr TTM) exceeds operating profit (Rs352 cr), so reported PAT and P/E (75x) are distorted. The stock fell 27% in 12 months to a 52-week low on 2026-10-28.

## What moves the stock, ranked
1. **Defence procurement flow** (P_DEFENCE_PROCUREMENT +5.0 per +10% orders): DAC approvals (Rs2.12 lakh cr on 2026-10-26/27) and actual order placement.
2. **Execution cadence**: quarterly revenue and margin surprises (results 2026-11-12).
3. **Geopolitical escalation** (India-Pakistan +3.0) and export wins (+3.0).
4. **Market risk appetite and rates** (high beta 1.6-1.7; repo 5.50% after the 2026-10-07 hike affects both treasury income and the multiple).
5. **Supply chain**: Russian licence content, imported electronics, rupee.

## Transmission examples
- **India-Pakistan border escalation -> emergency procurement and replenishment of missile stocks -> accelerated Akash/Astra/Invar orders -> BDL revenue visibility up** (2nd-3rd order); simultaneously it lifts Brent slightly and FPI outflows (4th order) which hit the stock's beta.
- **Higher repo -> bank deposit rates up -> BDL treasury yield up (+) but 75x P/E discounted at a higher rate (-)**; the net is negative in the model.
- **Russia sanctions/payment issues -> Invar kits delayed -> milestone billing slips -> quarterly revenue misses** (3rd order).
- **Semiconductor tightening -> seeker electronics delayed -> deliveries slip to next quarter.**

## Current situation
Orders: Rs811 cr anti-airfield weapons (2026-09-23), Rs1,307 cr Navy order (2026-10-15). Brokers see Akash and Astra ramp-ups driving growth (2026-10-08). Despite the 2026-10-27 DAC news the stock remained near lows, signalling market doubt about conversion. Promoters 74.93%, FIIs 1.8%.

## Upcoming
Q2 FY27 results on 2026-11-12 (screener); possible big missile orders from DAC-cleared proposals; Q3 results Feb 2027.

## Bull and bear
Bull: order book visibility, converting Akash-NG/Astra into higher deliveries, margin recovery from 15% toward 20-25%. Bear: execution slippage, single customer, treasury income masking low operating margin, valuation.

Uncertainties: import content, deposit size, DAC allocation to BDL are assumptions or unverified.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.