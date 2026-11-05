# WAAREEENER — Waaree Energies Ltd.
*MIDCAP_100 · Capital Goods · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -0.1%**, **12 months +0.7%** (rank 110 / 84 of 200 for 3m / 12m); beta 1.36
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +34.3%): 3 months 50%, 12 months 62%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -3.4% … P90 +5.0%; plausible 12m relative-return range incl. stock-specific noise: -23.0% … +48.1%
- Decomposition (12m): 0.5 × forward event exposure +2.9% (3m +1.1%; half assumed priced) + 0.5 × company-specific catalysts -0.7%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply +17.4% (beta-adjusted) vs a realised market-adjusted move of -27.7% — gap +45.1 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Renewable / transmission policy support (`P_RENEWABLE_SUPPORT`) | +1 = stronger support | +6.70 | +6.00 | +0.78 | -0.08 | +0.00 | — |
| Indian solar module / cell realisations (`NEW_SOLAR_CELL_MODULE_PRICE`) | +10% Indian module/cell realisations | +5.00 | +5.00 | +0.00 | +0.00 | +0.00 | — |
| Energy transition investment (`T_ENERGY_TRANSITION`) | +1 | +2.82 | +3.00 | -0.17 | +0.00 | -0.02 | — |
| US tariffs on Indian goods (`P_US_TARIFF_INDIA`) | +10 pp average tariff | -2.12 | -2.00 | -0.09 | -0.02 | -0.01 | — |
| Indian electricity demand (`F_POWER_DEMAND_IN`) | +3 pp demand growth | +2.00 | +2.00 | +0.00 | +0.00 | +0.00 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -1.52 | -1.30 | -0.12 | -0.10 | -0.01 | -1.1% |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -1.46 | -1.50 | +0.05 | +0.01 | -0.02 | — |
| Russia (oil discounts, defence, sanctions) (`C_RUSSIA`) | +1 = closer trade access / larger discounts | -1.28 | +0.00 | -1.28 | -0.01 | +0.01 | — |
| Monsoon rainfall vs normal (`F_MONSOON`) | +10% above long-period average | -1.10 | +0.00 | -1.15 | -0.12 | +0.16 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -1.10 | +0.00 | -1.12 | +0.01 | +0.02 | — |
| USD/CNY (`F_USDCNY`) | +3% USD/CNY (yuan weaker) | -1.04 | -1.00 | -0.06 | +0.03 | -0.01 | -1.4% |
| US average effective tariff rate (all partners) (`NEW_US_TARIFF_GLOBAL`) | +5 pp effective tariff rate | -1.03 | +0.00 | -0.80 | -0.24 | +0.02 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -1.02 | +0.00 | -0.22 | -0.54 | -0.26 | — |
| Indian anti-dumping duties (chemicals, solar, others) (`P_ANTI_DUMPING_IN`) | +1 = new broad duties | +1.00 | +1.00 | +0.00 | +0.00 | +0.00 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Cabinet approves Rs14,500 cr VGF for ~92 GWh grid-scale storage (4 Nov) (`EV_BESS_VGF_NOV26`) | occurred | 1.00 | +7.4% | +7.4% | +7.5 | -0.1 | +0.0 | -0.0 |
| ALMM List-II (domestic cells) in force; approved cell capacity 37.8 GW (12th revision, 9 Oct); solar project costs seen +20% (`EV_SOLAR_ALMM2_CELL_MANDATE`) | occurred | 1.00 | +3.3% | +3.3% | +3.0 | +0.4 | -0.0 | +0.0 |
| Gold and silver slump from January 2026 peaks (silver -53%, gold -24%) (`EV_PRECIOUS_METALS_CRASH_2026`) | occurred | 1.00 | +2.0% | +2.0% | +2.0 | +0.0 | +0.0 | +0.0 |
| Indian spot power: IEX prices hit Rs20/unit ceiling (19 Sep), Q2 prices up ~46% y/y; El Nino lifts demand (`EV_POWER_SPOT_SPIKE`) | occurred | 1.00 | +2.0% | +2.0% | +2.0 | +0.0 | +0.0 | +0.0 |
| Aluminium -20% since June; copper off record; Nifty Metal -7% in October (`EV_BASE_METALS_ALUMINIUM_SLIDE`) | occurred | 1.00 | +1.8% | +1.8% | +1.8 | +0.0 | +0.0 | +0.0 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -1.5% | -1.5% | -1.5 | +0.1 | +0.0 | -0.0 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -1.2% | -1.2% | +0.0 | -1.3 | +0.0 | +0.1 |
| Summer 2027 peak-demand shortfall / IEX at cap under super El Nino (`EV_SUMMER27_POWER_SHORTFALL`) | anticipated | 0.40 | +3.1% | +1.2% | +3.0 | +0.0 | +0.1 | -0.1 |
| US waives Russia-oil secondary sanctions/100% tariff threat on buyers incl. India (17 Oct) (`EV_RUSSIA_WAIVER_OCT17`) | occurred | 1.00 | +1.1% | +1.1% | +1.0 | +0.0 | +0.1 | +0.0 |
| Waiver lapses and US imposes secondary tariff (up to 100%) or sanctions on Indian refiners buying Russian oil (`EV_RUSSIA_TARIFF_ENFORCED`) | risk_scenario | 0.15 | -5.7% | -0.8% | -5.0 | -0.4 | -0.2 | -0.0 |
| IMD April 2027 long-range forecast says normal or above-normal monsoon (>=96% LPA) (`EV_MONSOON27_FIRST_FORECAST_NORMAL`) | scheduled | 0.68 | -1.2% | -0.8% | +0.0 | -1.1 | +0.0 | -0.1 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.55 | +1.1% | +0.6% | +0.0 | +0.6 | +0.5 | +0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_SUMMER27_POWER_SHORTFALL ⇒ F_POWER_DEMAND_IN → WAAREEENER | +3.00% | +1.20% |
| 2 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → F_POWER_DEMAND_IN → WAAREEENER | -1.15% | -0.78% |
| 1 | EV_RUSSIA_TARIFF_ENFORCED ⇒ P_US_TARIFF_INDIA → WAAREEENER | -5.00% | -0.75% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → WAAREEENER | -1.50% | -0.63% |
| 1 | EV_INDIA_US_INTERIM_DEAL_SIGNED ⇒ P_US_TARIFF_INDIA → WAAREEENER | +1.00% | +0.55% |
| 1 | EV_PRECIOUS_METALS_REBOUND_H1_2027 ⇒ F_SILVER → WAAREEENER | -1.20% | -0.54% |
| 1 | EV_INDIA_US_TALKS_COLLAPSE ⇒ P_US_TARIFF_INDIA → WAAREEENER | -3.00% | -0.54% |
| 1 | EV_NUCLEAR_SHANTI_RULES_FINAL ⇒ T_ENERGY_TRANSITION → WAAREEENER | +0.90% | +0.54% |
| 1 | EV_GST_RATE_CHANGE_APR27 ⇒ P_RENEWABLE_SUPPORT → WAAREEENER | +1.80% | +0.54% |
| 1 | EV_INDIA_ADD_DUTIES_NOTIFIED_H1_2027 ⇒ P_ANTI_DUMPING_IN → WAAREEENER | +0.70% | +0.49% |
| 2 | EV_NEMONSOON26_NORMAL_UP ⇒ F_MONSOON → F_POWER_DEMAND_IN → WAAREEENER | -0.57% | -0.49% |
| 1 | EV_PRECIOUS_METALS_FURTHER_SLIDE ⇒ F_SILVER → WAAREEENER | +1.60% | +0.48% |
| 1 | EV_RBI_FEB27_HIKE25 ⇒ F_REPO_IN → WAAREEENER | -1.50% | -0.41% |
| 2 | EV_RUSSIAN_CRUDE_CUT_TRADE_DEAL ⇒ C_RUSSIA → P_US_TARIFF_INDIA → WAAREEENER | +1.28% | +0.38% |
| 2 | EV_MONSOON27_DEFICIT_FORECAST ⇒ F_MONSOON → F_POWER_DEMAND_IN → WAAREEENER | +1.15% | +0.37% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | P_RENEWABLE_SUPPORT → WAAREEENER | +0.60 | director_override | +3.60% |
| 1 | F_POWER_DEMAND_IN → WAAREEENER | +1.20 | events | +2.40% |
| 1 | F_SILVER → WAAREEENER | -2.50 | observed | +2.00% |
| 1 | F_ALUMINIUM → WAAREEENER | -1.96 | observed | +1.77% |
| 1 | F_REPO_IN → WAAREEENER | +1.00 | events | -1.50% |
| 1 | P_US_TARIFF_INDIA → WAAREEENER | -0.60 | events | +1.20% |
| 1 | T_ENERGY_TRANSITION → WAAREEENER | +0.30 | director_override | +0.90% |
| 1 | F_USDINR → WAAREEENER | -0.37 | observed | +0.48% |
| 1 | F_USDCNY → WAAREEENER | -0.47 | observed | +0.47% |
| 1 | P_ANTI_DUMPING_IN → WAAREEENER | +0.40 | events | +0.40% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-11 | US ITC / Commerce follow-through on AD/CVD orders on Indian cells | regulatory | 0.60 | -1.5% | -0.90% |
| 2026-12-04 | Section 232 minimum import prices and 15% duty on polysilicon derivatives take effect (US) | regulatory | 0.85 | +0.0% | +0.00% |
| 2027-01 | Q3 FY27 results (Dec quarter); test of FY27 EBITDA guidance Rs 7,000-7,700 cr | results | 0.95 | +0.0% | +0.00% |
| 2027-02 | Reversal or confirmation of cancelled ~3 GW US export orders | other | 0.40 | +0.5% | +0.20% |
| 2027-03 | Completion of Waaree Green Data Centers integration / first data-centre capex disclosure | corporate_action | 0.40 | +0.0% | +0.00% |

## Analyst profile (agent research, sourced)
# WAAREEENER — Waaree Energies (as of 2026-11-05)

## Business
Waaree is India's largest solar-module maker by capacity (12 GW+ in India per Screener, plus 3.2 GW in Texas after two new 800 MW lines started in November 2026) and is diversifying into cells, inverters (1.1 GW line live 30 Sep 2026), BESS, T&D EPC, specialty gases and data centres (it bought Waaree Green Data Centers in October). Q2 FY27 (reported 27 Oct 2026): revenue Rs 7,518 cr (+24%, -5% q/q), EBITDA Rs 1,335 cr (17.8% vs 23.2%), PAT Rs 753 cr (-14%; attributable Rs 719 cr). Segment mix: retail 46% (up from 28.9% in Q1), utilities 23%, overseas 18.5%, EPC/O&M/T&D 12.6%. Kotak noted weakness in non-DCR demand, a 4% q/q fall in the order book and about 3 GW of cancelled US export orders amid Section 232 uncertainty. FY27 EBITDA guidance of Rs 7,000-7,700 cr was reiterated; H1 EBITDA was about Rs 2,775 cr, so H2 must jump. The stock hit a 52-week low of Rs 2,162 on 28 Oct and is 35% below the April high; brokers: 12 Buy, 4 Hold, 2 Sell (Bloomberg, via IndiaIPO).

## What moves the stock, ranked
1. **US trade barriers** (-2.0 per +10 pp). Final AD 123.04% and CVD 126.09% on Indian cells/modules (11 Sep 2026) and Section 232 minimum import prices ($0.22/W cells, $0.38/W modules, +15% polysilicon-derivative duty) effective 4 Dec 2026. Direct damage to exports is mostly realised; the Texas capacity (3.2 GW) is the hedge.
2. **Indian policy** (+6): ALMM-II, DCR and PM Surya Ghar (retail 46%).
3. **Module/cell realisations** (+5 per +10%) in a market where cell capacity may reach 60-70 GW.
4. **Imported-input costs and FX** (USD/INR -1.3, aluminium -0.9, silver -0.8, USD/CNY -1.0).
5. **Funding costs** (-1.5) as diversification (BESS, data centres, US plants) lifts capex and interest (Rs 105 cr in Q2 vs Rs 43 cr a year earlier).
6. **Energy-transition diversification** (+3) and power demand (+2).

## Transmission examples
- **Trade chain:** US imposes AD/CVD and Section 232 MIPs -> Indian exports to the US collapse and orders cancel (3 GW) -> inventory and capacity diverted to India -> domestic non-DCR module prices fall -> margin compresses to 17.8% -> guidance of Rs 7,000-7,700 cr at risk -> brokers cut targets (observed in Oct 2026).
- **Onshoring upside chain:** Section 232 gives preference to US producers that onshore -> Waaree's Texas output (3.2 GW) sells at US prices much higher than import-parity -> margin on overseas revenue rises -> offsets Indian price pressure (uncertain; depends on US cell supply).
- **Commodity-FX chain:** Middle East escalation -> Brent up, INR weaker, freight up -> imported cell, glass and silver dearer in INR -> gross margin (26%) falls while developers resist price increases.
- **Rate chain:** RBI holds -> developers' project IRR lower -> utility tenders slow -> utilities share (23%) falls and working capital rises.

## Current situation and upcoming events
Section 232 effective date 4 Dec 2026 (prob 0.85, impact -4% to +4%); Q3 results (Jan 2027); further US AD/CVD process steps (Nov 2026); status of cancelled US orders (Feb 2027). Share count and the exact cell capacity were not verified.

## Bull and bear
Bull: Texas onshoring benefits, strong retail pull and cell ramp restore 20%+ margins, so FY27 guidance is met and the stock rerates from 18x. Bear: US exports remain closed, domestic oversupply deepens, guidance is cut and the data-centre/BESS diversification dilutes returns. Uncertainty: order-book numbers conflict across sources (JM quotes Rs 5,920 cr after cancellations), PAT quoted at Rs 719 cr vs Rs 753 cr by definition.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.