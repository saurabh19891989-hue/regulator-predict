# RELIANCE — Reliance Industries Ltd.
*NIFTY_50 · Oil Gas & Consumable Fuels · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +0.1%**, **12 months +1.9%** (rank 84 / 14 of 200 for 3m / 12m); beta 1.10
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +17.8%): 3 months 51%, 12 months 56%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -1.0% … P90 +5.5%; plausible 12m relative-return range incl. stock-specific noise: -21.8% … +24.8%
- Decomposition (12m): 0.5 × forward event exposure +2.1% (3m +0.4%; half assumed priced; market-priced macro drift removed) + 0.5 × company-specific catalysts +2.1%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply -0.1% (beta-adjusted) vs a realised market-adjusted move of -5.7% — gap +5.6 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## Where the expected return comes from
Market-priced macro drivers (rates, FX, commodities, indices, volatility, flows, growth, inflation) are taken as priced, so what is left is policy, regulatory, sector, theme, geopolitical and company-specific exposure — where 2nd–4th-order effects are most likely to be missed. Percentage points of the expected relative return.
| source | 12m: 1st order | 12m: 2nd–4th order | 12m total | 3m total |
|---|---|---|---|---|
| Policy | -0.09 | -0.00 | -0.09 | -0.09 |
| Sector | +1.68 | +0.10 | +1.78 | +0.51 |
| Theme | +0.00 | +0.04 | +0.04 | +0.03 |
| Geopolitics | -0.13 | +0.11 | -0.02 | +0.04 |
| Company catalysts | +1.03 | +0.00 | +1.03 | +0.04 |
| Market-priced macro | +0.00 | +0.00 | +0.00 | +0.00 |
| Beta adjustment | — | — | -0.63 | -0.28 |
| Universe centring | — | — | -0.15 | -0.10 |
| **Expected relative return** | | | **+1.95** | **+0.14** |

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Mobile tariff hikes (`P_TELECOM_TARIFFS`) | +10% ARPU via tariff hike | +3.98 | +4.00 | +0.00 | -0.02 | +0.00 | — |
| Windfall / export taxes on commodities (`P_WINDFALL_EXPORT_TAX`) | +1 = imposition | -3.43 | -3.00 | -0.43 | +0.00 | +0.00 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +2.57 | +2.50 | +0.05 | +0.01 | +0.01 | — |
| Refining margins (GRM / cracks) (`F_REFINING_MARGIN`) | +$2/bbl gross refining margin | +1.62 | +1.80 | -0.18 | +0.00 | +0.00 | +15.4% |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -1.46 | +0.00 | -0.99 | -0.46 | -0.01 | +3.5% |
| US average effective tariff rate (all partners) (`NEW_US_TARIFF_GLOBAL`) | +5 pp effective tariff rate | -1.11 | +0.00 | -0.20 | -0.48 | -0.43 | — |
| USD/JPY exchange rate (`NEW_USDJPY`) | +3% USD/JPY (yen weaker) | +1.02 | +0.00 | +0.60 | +0.27 | +0.16 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -1.02 | -1.00 | -0.01 | +0.02 | -0.03 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -1.01 | -0.50 | -0.48 | -0.04 | +0.01 | -1.1% |
| Petrochemical / polymer spreads (`F_PETROCHEM_SPREADS`) | +10% polymer-naphtha spreads | +1.00 | +1.00 | +0.00 | +0.00 | +0.00 | — |
| Capital-gains / securities tax burden (`P_CAPITAL_GAINS_TAX`) | +1 = higher | -0.92 | +0.00 | -0.90 | -0.02 | +0.00 | — |
| US dollar index (`F_DXY`) | +3% DXY | -0.89 | +0.00 | -0.78 | -0.09 | -0.01 | +2.2% |
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +0.87 | +0.80 | +0.00 | +0.08 | -0.02 | — |
| US tariffs on Indian goods (`P_US_TARIFF_INDIA`) | +10 pp average tariff | -0.87 | -0.50 | -0.26 | -0.09 | -0.01 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -5.6% | -5.6% | -5.5 | -0.1 | -0.0 | -0.0 |
| Broad mobile tariff hike by Jio/Airtel (12-15%) (`EV_TELECOM_TARIFF_HIKE_2027`) | anticipated | 0.75 | +4.8% | +3.6% | +4.8 | +0.0 | -0.0 | +0.0 |
| Windfall/export levy re-set: petrol nil, diesel Rs11.5/l, ATF ~Rs11/l (31 Oct); excise reportedly cut (3 Nov, unverified) (`EV_EXPORT_LEVY_REVISIONS`) | occurred | 1.00 | -3.4% | -3.4% | -3.0 | -0.4 | +0.0 | +0.0 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +6.5% | +3.2% | +6.2 | +0.1 | +0.0 | +0.0 |
| US waives Russia-oil secondary sanctions/100% tariff threat on buyers incl. India (17 Oct) (`EV_RUSSIA_WAIVER_OCT17`) | occurred | 1.00 | +1.6% | +1.6% | +1.1 | +0.5 | -0.0 | +0.1 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.25 | -5.8% | -1.4% | +0.0 | -5.5 | -0.4 | +0.1 |
| US midterms (3 Nov 2026): Democrats win House and Senate (`EV_US_MIDTERMS_DEM_SWEEP`) | occurred | 1.00 | +1.3% | +1.3% | +1.3 | +0.0 | +0.0 | +0.0 |
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | +1.2% | +1.2% | +1.6 | -0.1 | -0.1 | -0.1 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -1.0% | -1.0% | -1.0 | -0.0 | +0.0 | -0.0 |
| Risk: USD/INR >98 and/or reserves < US$650bn (disorderly rupee, emergency RBI response) (`EV_RUPEE_BREAK_98_RESERVE_STRESS`) | risk_scenario | 0.18 | -5.5% | -1.0% | -5.4 | -0.0 | -0.0 | +0.0 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -1.0% | -1.0% | +0.0 | -0.9 | -0.0 | -0.0 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -0.9% | -0.9% | +0.0 | -0.8 | -0.1 | +0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_TELECOM_TARIFF_HIKE_2027 ⇒ P_TELECOM_TARIFFS → RELIANCE | +4.80% | +3.60% |
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → RELIANCE | +6.25% | +3.12% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → RELIANCE | -3.75% | -0.67% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → RELIANCE | -2.40% | -0.60% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_FPI_FLOWS → RELIANCE | -2.40% | -0.60% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_REFINING_MARGIN → RELIANCE | -1.08% | -0.59% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → RELIANCE | -2.33% | -0.58% |
| 1 | EV_BUDGET_FY28_LTCG_RELIEF ⇒ F_FPI_FLOWS → RELIANCE | +1.25% | +0.44% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → RELIANCE | -1.00% | -0.42% |
| 1 | EV_Q2_FY27_GDP_STRONG ⇒ F_FPI_FLOWS → RELIANCE | +0.50% | +0.40% |
| 2 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → RELIANCE | -2.33% | -0.35% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ C_MIDEAST_CONFLICT → RELIANCE | -0.50% | -0.28% |
| 1 | EV_RUSSIAN_CRUDE_CUT_TRADE_DEAL ⇒ F_REFINING_MARGIN → RELIANCE | -0.90% | -0.27% |
| 2 | EV_YEN_CARRY_UNWIND_RISK ⇒ NEW_USDJPY → F_FPI_FLOWS → RELIANCE | -1.80% | -0.27% |
| 1 | EV_RBI_FEB27_HIKE25 ⇒ F_REPO_IN → RELIANCE | -1.00% | -0.27% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_FPI_FLOWS → RELIANCE | -1.60 | events | -4.00% |
| 1 | P_WINDFALL_EXPORT_TAX → RELIANCE | +1.00 | events | -3.00% |
| 1 | F_REFINING_MARGIN → RELIANCE | +0.60 | events | +1.08% |
| 1 | F_REPO_IN → RELIANCE | +1.00 | events | -1.00% |
| 1 | C_RUSSIA → RELIANCE | +1.00 | events | +0.80% |
| 1 | C_MIDEAST_CONFLICT → RELIANCE | +1.00 | events | +0.50% |
| 1 | P_US_TARIFF_INDIA → RELIANCE | -0.60 | events | +0.30% |
| 1 | P_TELECOM_TARIFFS → RELIANCE | +0.05 | events | +0.20% |
| 1 | F_USDINR → RELIANCE | -0.37 | observed | +0.18% |
| 1 | F_URBAN_DEMAND → RELIANCE | +0.20 | events | +0.16% |
| 2 | F_CHINA_GDP → F_PETROCHEM_SPREADS → RELIANCE | +0.30 | events | +0.12% |
| 2 | T_GENAI_SERVICES → T_DATA_CENTRES_IN → RELIANCE | +0.50 | director_override | +0.06% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-12 | Index inclusion/flows for newly listed Jio Platforms (fast entry into Nifty/Sensex/MSCI) with possible RIL weight changes | corporate_action | 0.50 | +0.0% | +0.00% |
| 2026-12 | Windfall export-levy reviews on diesel/petrol/ATF (fortnightly) | regulatory | 0.80 | -0.5% | -0.40% |
| 2027-01 | Q3 FY27 results (RIL reports in the third week of January) | results | 0.95 | +0.5% | +0.47% |
| 2027-03 | US sanctions / 100% secondary-tariff outcome for Russian-oil buyers | regulatory | 0.25 | -2.5% | -0.62% |
| 2027-06 | Jio tariff hike round post-listing (model expectation; not announced) | guidance | 0.50 | +4.0% | +2.00% |
| 2027-06 | Reliance Retail listing/DRHP plans (management had guided to a listing; no filing retrieved) | corporate_action | 0.20 | +3.0% | +0.60% |

## Analyst profile (agent research, sourced)
# Reliance Industries (RELIANCE) — market impact profile (as of 2026-11-05)

## Business
Reliance is a three-engine conglomerate: O2C (Jamnagar refining and petchem, export-oriented and therefore outside India's regulated-price regime), Jio (telecom and digital, now separately listed), and Retail. Each reacts to different factors, so the stock behaves as a sum-of-the-parts. In Q2 FY27 O2C produced a windfall from wide fuel cracks while Jio listed and retail was soft.

## What moves the stock (ranked)
1. **Refining margins / cracks (F_REFINING_MARGIN +1.8)** and **export-levy policy (P_WINDFALL_EXPORT_TAX -3.0)** — the O2C swing factors.
2. **Telecom tariffs (P_TELECOM_TARIFFS +4.0)** — Jio value.
3. **Flows and rates (F_FPI_FLOWS +2.5, F_REPO_IN -1.0)** — index heavyweight.
4. **Petchem spreads (+1.0), Russia/US tariffs (C_RUSSIA +0.8, P_US_TARIFF_INDIA -0.5), retail demand (+0.8).**

## Worked transmission examples
- Hormuz escalation -> Brent and diesel cracks up (order 1) -> RIL exports at global cracks, domestic OMCs face frozen prices (order 2: RIL earns a relative windfall) -> government raises export levies (order 3: lowers the windfall, a policy edge) -> RIL's net gain is lower than the cracks imply (order 4: Q2 result vs levies). Meanwhile OMCs lose, so RIL outperforms them in the cross-section.
- Rupee weaker -> RIL's USD revenues rise but foreign investors reduce exposure (FIIs 18.7% -> 16.7%) -> index outflow pressure on the heavyweight.
- Jio tariff hike -> ARPU +10% -> group EBITDA +5.6% -> because Jio is now listed, the market re-rates the stake directly (Jio value discovery lifted RIL 12%); a failed hike or competitor price war (Bharti) would reverse it.
- US Russia-oil secondary tariffs -> RIL must source costlier crude -> narrower GRM and higher risk premium; spills over to Indian exporters.

## Current situation
Q2 FY27: operating profit Rs 56.6k cr (+19% q/q), profit ~+41% y/y (Reuters), O2C EBITDA +68%, retail weak. Stock +12% on 2 Nov, +7.7% over a month, but -11% over 12 months at 21.6x earnings. Goldman Sachs sees 58% upside; Moneycontrol ~33%.

## Upcoming events
Q3 results (Jan 2027), index inclusion for Jio Platforms, tariff hikes, windfall levy reviews, Russia sanctions.

## Bull / bear
Bull: cracks stay wide, Jio tariffs rise, Retail IPO, New Energy delivers. Bear: cracks normalise as the war ends, export levies rise, Russian-oil sanctions, retail slowdown, leverage rising.

*Weights are exposure estimates, not return forecasts. Jio Platforms' share of RIL post-IPO was not verified.*


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.