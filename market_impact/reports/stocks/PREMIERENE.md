# PREMIERENE — Premier Energies Ltd.
*MIDCAP_100 · Capital Goods · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +0.9%**, **12 months +0.8%** (rank 16 / 47 of 200 for 3m / 12m); beta 1.26
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +34.2%): 3 months 52%, 12 months 51%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -2.4% … P90 +5.1%; plausible 12m relative-return range incl. stock-specific noise: -46.8% … +42.5%
- Decomposition (12m): 0.5 × forward event exposure +1.1% (3m +0.2%; half assumed priced; market-priced macro drift removed) + 0.5 × company-specific catalysts +0.8%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply +14.5% (beta-adjusted) vs a realised market-adjusted move of -22.7% — gap +37.2 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## Where the expected return comes from
Market-priced macro drivers (rates, FX, commodities, indices, volatility, flows, growth, inflation) are taken as priced, so what is left is policy, regulatory, sector, theme, geopolitical and company-specific exposure — where 2nd–4th-order effects are most likely to be missed. Percentage points of the expected relative return.
| source | 12m: 1st order | 12m: 2nd–4th order | 12m total | 3m total |
|---|---|---|---|---|
| Policy | +1.00 | +0.02 | +1.02 | +0.31 |
| Sector | +0.00 | -0.15 | -0.15 | -0.06 |
| Theme | +0.36 | +0.01 | +0.37 | +0.19 |
| Geopolitics | +0.00 | +0.01 | +0.01 | -0.02 |
| Company catalysts | +0.39 | +0.00 | +0.39 | +0.90 |
| Market-priced macro | +0.00 | -0.00 | -0.00 | -0.00 |
| Beta adjustment | — | — | -0.72 | -0.33 |
| Universe centring | — | — | -0.15 | -0.10 |
| **Expected relative return** | | | **+0.77** | **+0.89** |

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Renewable / transmission policy support (`P_RENEWABLE_SUPPORT`) | +1 = stronger support | +6.94 | +6.00 | +1.04 | -0.10 | +0.00 | — |
| Indian solar module / cell realisations (`NEW_SOLAR_CELL_MODULE_PRICE`) | +10% Indian module/cell realisations | +4.00 | +4.00 | +0.00 | +0.00 | +0.00 | — |
| Energy transition investment (`T_ENERGY_TRANSITION`) | +1 | +3.78 | +4.00 | -0.21 | +0.00 | -0.01 | — |
| Indian anti-dumping duties (chemicals, solar, others) (`P_ANTI_DUMPING_IN`) | +1 = new broad duties | +3.00 | +3.00 | +0.00 | +0.00 | +0.00 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -1.45 | -1.50 | +0.04 | +0.01 | +0.00 | — |
| Silver price (`F_SILVER`) | +12% silver | -1.40 | -1.40 | +0.00 | +0.00 | +0.00 | -30.0% |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -1.22 | -1.00 | -0.12 | -0.09 | -0.01 | -1.1% |
| Gold price (`F_GOLD`) | +8% gold (USD) | -1.16 | +0.00 | -1.12 | -0.04 | +0.00 | -8.4% |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -1.04 | +0.00 | -1.06 | -0.00 | +0.02 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -0.98 | +0.00 | -0.12 | -0.60 | -0.25 | — |
| China chemical/API dumping intensity (`F_CHINA_CHEM_EXPORTS`) | +15% export volumes / price cuts | +0.96 | +0.00 | +0.96 | +0.00 | +0.00 | — |
| EV incentives / mandates (`P_EV_POLICY`) | +1 = stronger EV push | +0.91 | +0.00 | +0.96 | -0.05 | +0.00 | — |
| China growth / stimulus (`F_CHINA_GDP`) | +1 pp | -0.65 | +0.00 | -0.19 | -0.37 | -0.09 | — |
| US–China trade decoupling (`C_US_CHINA_DECOUPLING`) | +1 = more decoupling | +0.61 | +0.00 | +0.00 | +0.39 | +0.22 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Cabinet approves Rs14,500 cr VGF for ~92 GWh grid-scale storage (4 Nov) (`EV_BESS_VGF_NOV26`) | occurred | 1.00 | +7.9% | +7.9% | +8.0 | -0.1 | +0.0 | -0.0 |
| Gold and silver slump from January 2026 peaks (silver -53%, gold -24%) (`EV_PRECIOUS_METALS_CRASH_2026`) | occurred | 1.00 | +3.5% | +3.5% | +3.5 | +0.0 | +0.0 | +0.0 |
| ALMM List-II (domestic cells) in force; approved cell capacity 37.8 GW (12th revision, 9 Oct); solar project costs seen +20% (`EV_SOLAR_ALMM2_CELL_MANDATE`) | occurred | 1.00 | +3.5% | +3.5% | +3.0 | +0.5 | -0.1 | +0.0 |
| Finance ministry notifies anti-dumping duties on a meaningful batch of Chinese chemicals/APIs/others (`EV_INDIA_ADD_DUTIES_NOTIFIED_H1_2027`) | anticipated | 0.70 | +2.1% | +1.5% | +2.1 | +0.0 | +0.0 | +0.0 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -1.5% | -1.5% | -1.5 | +0.0 | +0.0 | +0.0 |
| DGTR opens wave of anti-dumping probes on Chinese chemicals, APIs and steel (`EV_INDIA_ANTIDUMPING_WAVE_SEP_OCT26`) | occurred | 1.00 | +1.2% | +1.2% | +1.2 | +0.0 | +0.0 | +0.0 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -1.2% | -1.2% | +0.0 | -1.2 | -0.0 | +0.0 |
| Aluminium -20% since June; copper off record; Nifty Metal -7% in October (`EV_BASE_METALS_ALUMINIUM_SLIDE`) | occurred | 1.00 | +1.0% | +1.0% | +1.0 | +0.0 | +0.0 | +0.0 |
| Gold/silver rebound as Fed hike fears fade or Iran war ends (`EV_PRECIOUS_METALS_REBOUND_H1_2027`) | anticipated | 0.45 | -2.1% | -1.0% | -2.1 | +0.0 | -0.0 | +0.0 |
| Gold falls to ~$3,500 / silver to ~$40 on Fed hike(s) and strong dollar (`EV_PRECIOUS_METALS_FURTHER_SLIDE`) | risk_scenario | 0.30 | +2.9% | +0.9% | +2.8 | +0.0 | +0.1 | +0.0 |
| CAFE-III fuel-efficiency norms notified (30 Sep 2026); no small-car carve-out; 3x credit for BEVs (`EV_CAFE3_NOTIFIED`) | occurred | 1.00 | +0.7% | +0.7% | +0.0 | +0.8 | -0.0 | +0.0 |
| Final SHANTI Act rules / first private-sector nuclear licence process (`EV_NUCLEAR_SHANTI_RULES_FINAL`) | anticipated | 0.60 | +1.1% | +0.7% | +1.2 | -0.1 | +0.0 | -0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_INDIA_ADD_DUTIES_NOTIFIED_H1_2027 ⇒ P_ANTI_DUMPING_IN → PREMIERENE | +2.10% | +1.47% |
| 1 | EV_PRECIOUS_METALS_REBOUND_H1_2027 ⇒ F_SILVER → PREMIERENE | -2.10% | -0.94% |
| 1 | EV_PRECIOUS_METALS_FURTHER_SLIDE ⇒ F_SILVER → PREMIERENE | +2.80% | +0.84% |
| 1 | EV_NUCLEAR_SHANTI_RULES_FINAL ⇒ T_ENERGY_TRANSITION → PREMIERENE | +1.20% | +0.72% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → PREMIERENE | -1.50% | -0.63% |
| 1 | EV_GST_RATE_CHANGE_APR27 ⇒ P_RENEWABLE_SUPPORT → PREMIERENE | +1.80% | +0.54% |
| 1 | EV_RBI_FEB27_HIKE25 ⇒ F_REPO_IN → PREMIERENE | -1.50% | -0.41% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_REPO_IN → PREMIERENE | -1.50% | -0.27% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_USDINR → PREMIERENE | -1.30% | -0.23% |
| 2 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → F_USDINR → PREMIERENE | +0.46% | +0.23% |
| 3 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ C_MIDEAST_CONFLICT → F_GOLD → F_SILVER → PREMIERENE | +0.34% | +0.18% |
| 1 | EV_INDIA_STAGFLATION_SCARE ⇒ F_REPO_IN → PREMIERENE | -1.50% | -0.18% |
| 1 | EV_RBI_APR27_CUT25 ⇒ F_REPO_IN → PREMIERENE | +1.50% | +0.15% |
| 2 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → F_USDINR → PREMIERENE | +0.27% | +0.15% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_FED_FUNDS → F_REPO_IN → PREMIERENE | +0.54% | +0.14% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | P_RENEWABLE_SUPPORT → PREMIERENE | +0.60 | director_override | +3.60% |
| 1 | F_SILVER → PREMIERENE | -2.50 | observed | +3.49% |
| 1 | F_REPO_IN → PREMIERENE | +1.00 | events | -1.50% |
| 1 | P_ANTI_DUMPING_IN → PREMIERENE | +0.40 | events | +1.20% |
| 1 | T_ENERGY_TRANSITION → PREMIERENE | +0.30 | director_override | +1.20% |
| 1 | F_ALUMINIUM → PREMIERENE | -1.96 | observed | +0.98% |
| 1 | F_USDINR → PREMIERENE | -0.37 | observed | +0.37% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-12 | 7 GW TOPCon cell plant commercial production start (company: 'shortly') | capex | 0.80 | +2.2% | +1.80% |
| 2027-01 | Q3 FY27 results | results | 0.95 | +0.0% | +0.00% |
| 2027-03 | Further cell/module price compression as Indian cell capacity scales (JM: 60-70 GW) | other | 0.40 | -7.0% | -2.80% |
| 2027-07 | First phase 6 GWh BESS commissioning | capex | 0.50 | +1.8% | +0.88% |
| 2027-12 | Ingot-wafer 10 GW phase 1 commissioning (target Dec 2027) | capex | 0.30 | +3.0% | +0.90% |

## Analyst profile (agent research, sourced)
# PREMIERENE — Premier Energies (as of 2026-11-05)

## Business
Premier Energies is India's largest solar-cell manufacturer (10.6 GW cells, 11.1 GW modules, effective utilisation 99% and 92%), also making transformers and EPC, and building a 7 GW TOPCon cell plant (commissioning shortly), 10 GW ingot-wafer (December 2027 / December 2028), 6 GWh BESS (July 2027) and aluminium frames (September 2027). Q2 FY27 (reported 4 Nov 2026): consolidated revenue about Rs 2,632-2,656 cr (+38-43%), operating EBITDA about Rs 736-760 cr (28% vs 30.5%), PAT Rs 462 cr (+31%, -2% q/q), order book 10.7 GW / Rs 16,600 cr (99% domestic), net debt Rs 1,911 cr, D/E 0.72, first dividend Rs 0.50. The pack's Screener table is a non-consolidated extract (sales Rs 253 cr in Q2) and was disregarded; the screener P/E of 307 is likewise unusable. On H1 FY27 annualised PAT the stock trades at about 21x (derived).

## What moves the stock, ranked
1. **Policy: ALMM List-II (cells), duties, subsidies** (+6 per standard policy shock). ALMM-II took effect in June 2026 and made domestic cells the bottleneck; Wood Mackenzie sees utility-scale system prices up about 20% by Q4 2026.
2. **Module/cell realisations** (+4 per +10%). Premier is cell-integrated, so price rises drop through at a higher rate than for module-only makers. JM estimates industry cell capacity could reach 60-70 GW, a big overhang by 2027-28.
3. **Energy transition demand** (+4), **repo and funding** (-1.5), **silver** (-1.4), **USD/INR** (-1.0), **aluminium** (-0.5).
4. **US trade** (-0.3): final US AD/CVD of 123% + 126% on Indian solar and Section 232 minimum import prices from 4 Dec affect Indian exporters, but Premier's exports are 1% of the order book.

## Transmission examples
- **Policy chain:** Government keeps ALMM-II and adds ALMM for wafers -> domestic cell scarcity -> cell and module prices stay high -> Premier's integrated margin holds ~28% -> cash flow funds ingot-wafer capex -> rerating on integration.
- **Oversupply chain:** US closes to Indian solar (AD/CVD + 232) -> Waaree, Vikram and others redirect capacity to India -> domestic module prices fall -> utilisation and margins at module makers slip (Premier less so thanks to cell scarcity) -> cell price war when 60-70 GW arrives.
- **Commodity chain:** Silver price falls (-30% since June) -> TOPCon cell cost down -> margin tailwind; if silver re-spikes with a risk-off geopolitical shock, cost +, margin -1 to -2 pp.
- **Macro chain:** Brent up -> INR weaker -> imported wafers, glass, EVA and USD machinery dearer; RBI delays easing -> developers' financing costlier -> tendering slows -> order intake stalls.

## Current situation and upcoming events
Stock about Rs 874-904 (Yahoo vs CNBC close; unresolved), 3m -16%. Promoter holding fell to 58.5% in June 2026 (placement/stake sale; details not retrieved), DIIs up to 18.9%. Events: 7 GW plant start (Dec 2026, prob 0.8), Q3 results (Jan 2027), BESS (Jul 2027, prob 0.5), and an industry price compression event (prob 0.4).

## Bull and bear
Bull: 7 GW TOPCon at 25.8% efficiency, BESS and wafer integration protect 28% margins and the Rs 16,600 cr order book converts. Bear: cell oversupply, margin slide continues (30.5% -> 28%), cash conversion stays weak (CFO/PAT 0.72) while capex rises. Uncertainty: cost shares are estimates; current Indian duty status not verified.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.