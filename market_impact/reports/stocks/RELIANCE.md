# RELIANCE — Reliance Industries Ltd.
*NIFTY_50 · Oil Gas & Consumable Fuels · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +1.5%**, **12 months +3.6%** (rank 53 / 47 of 200 for 3m / 12m); beta 1.10
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +17.8%): 3 months 57%, 12 months 68%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 +0.5% … P90 +9.2%; plausible 12m relative-return range incl. stock-specific noise: -12.1% … +26.9%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +1.5 pp (model impact +3.0% beta-adjusted vs realised market-adjusted move -5.7%); forward event exposure +4.4% (3m +2.6%; half assumed priced); company-specific events +2.1%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Mobile tariff hikes (`P_TELECOM_TARIFFS`) | +10% ARPU via tariff hike | +3.97 | +4.00 | +0.00 | -0.03 | +0.00 | — |
| Windfall / export taxes on commodities (`P_WINDFALL_EXPORT_TAX`) | +1 = imposition | -3.41 | -3.00 | -0.43 | +0.00 | +0.02 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +2.58 | +2.50 | +0.05 | +0.01 | +0.02 | — |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -1.75 | +0.00 | -0.72 | -0.95 | -0.07 | — |
| Refining margins (GRM / cracks) (`F_REFINING_MARGIN`) | +$2/bbl gross refining margin | +1.62 | +1.80 | -0.18 | +0.00 | +0.00 | +15.4% |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -1.62 | +0.00 | -0.99 | -0.56 | -0.06 | +3.5% |
| US dollar index (`F_DXY`) | +3% DXY | -1.54 | +0.00 | -1.22 | -0.26 | -0.06 | +2.2% |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -1.47 | +0.00 | -1.38 | -0.13 | +0.04 | — |
| US equity market (`F_US_EQUITIES`) | +5% S&P 500 | +1.38 | +0.00 | +0.80 | +0.48 | +0.10 | +1.2% |
| US average effective tariff rate (all partners) (`NEW_US_TARIFF_GLOBAL`) | +5 pp effective tariff rate | -1.25 | +0.00 | -0.20 | -0.58 | -0.47 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -1.09 | -0.50 | -0.48 | -0.10 | -0.01 | -1.1% |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -1.02 | -1.00 | -0.01 | +0.02 | -0.03 | — |
| Petrochemical / polymer spreads (`F_PETROCHEM_SPREADS`) | +10% polymer-naphtha spreads | +1.00 | +1.00 | +0.00 | +0.00 | +0.00 | — |
| USD/JPY exchange rate (`NEW_USDJPY`) | +3% USD/JPY (yen weaker) | +0.99 | +0.00 | +0.60 | +0.21 | +0.18 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -5.7% | -5.7% | -5.5 | -0.1 | -0.0 | -0.1 |
| Broad mobile tariff hike by Jio/Airtel (12-15%) (`EV_TELECOM_TARIFF_HIKE_2027`) | anticipated | 0.75 | +4.8% | +3.6% | +4.8 | +0.0 | -0.0 | +0.0 |
| Windfall/export levy re-set: petrol nil, diesel Rs11.5/l, ATF ~Rs11/l (31 Oct); excise reportedly cut (3 Nov, unverified) (`EV_EXPORT_LEVY_REVISIONS`) | occurred | 1.00 | -3.4% | -3.4% | -3.0 | -0.4 | +0.0 | +0.0 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +6.5% | +3.3% | +6.2 | +0.1 | +0.0 | +0.1 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -2.7% | -2.7% | +0.0 | -2.4 | -0.4 | +0.0 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.28 | -8.0% | -2.2% | +0.0 | -6.9 | -1.0 | -0.0 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -1.8% | -1.8% | +0.0 | -1.7 | -0.1 | +0.1 |
| US waives Russia-oil secondary sanctions/100% tariff threat on buyers incl. India (17 Oct) (`EV_RUSSIA_WAIVER_OCT17`) | occurred | 1.00 | +1.7% | +1.7% | +1.1 | +0.5 | +0.0 | +0.2 |
| Gold and silver slump from January 2026 peaks (silver -53%, gold -24%) (`EV_PRECIOUS_METALS_CRASH_2026`) | occurred | 1.00 | -1.6% | -1.6% | +0.0 | -1.6 | -0.1 | +0.0 |
| Disorderly yen carry-trade unwind (Aug-2024-style) after BoJ/MoF action (`EV_YEN_CARRY_UNWIND_RISK`) | risk_scenario | 0.18 | -8.8% | -1.6% | +0.0 | -8.0 | -0.7 | -0.1 |
| US midterms (3 Nov 2026): Democrats win House and Senate (`EV_US_MIDTERMS_DEM_SWEEP`) | occurred | 1.00 | +1.3% | +1.3% | +1.3 | +0.0 | +0.0 | +0.0 |
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | +1.3% | +1.3% | +4.9 | -1.4 | -1.9 | -0.3 |

## Strongest causal chains (1st–4th order)
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_RECORD_OUTFLOW_26 ⇒ F_FPI_FLOWS → RELIANCE | -5.50% | -5.50% |
| 1 | EV_TELECOM_TARIFF_HIKE_2027 ⇒ P_TELECOM_TARIFFS → RELIANCE | +4.80% | +3.60% |
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → RELIANCE | +6.25% | +3.12% |
| 1 | EV_EXPORT_LEVY_REVISIONS ⇒ P_WINDFALL_EXPORT_TAX → RELIANCE | -3.00% | -3.00% |
| 1 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_REFINING_MARGIN → RELIANCE | +2.70% | +2.70% |
| 1 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → RELIANCE | +1.49% | +1.49% |
| 2 | EV_CPI_REACCEL_SEP26 ⇒ F_CPI_IN → F_REPO_IN → RELIANCE | -1.32% | -1.32% |
| 1 | EV_US_MIDTERMS_DEM_SWEEP ⇒ F_FPI_FLOWS → RELIANCE | +1.25% | +1.25% |
| 1 | EV_AIRTEL_POSTPAID_HIKE ⇒ P_TELECOM_TARIFFS → RELIANCE | +1.20% | +1.20% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → RELIANCE | -3.73% | -1.05% |
| 1 | EV_RBI_OCT26_HIKE25 ⇒ F_REPO_IN → RELIANCE | -1.00% | -1.00% |
| 2 | EV_UST_SELLOFF_SEP26 ⇒ F_US_10Y → F_FPI_FLOWS → RELIANCE | -0.85% | -0.85% |
| 2 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → RELIANCE | -4.67% | -0.84% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_REFINING_MARGIN → RELIANCE | -1.44% | -0.84% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → RELIANCE | -3.75% | -0.82% |

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