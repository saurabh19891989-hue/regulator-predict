# MOTHERSON — Samvardhana Motherson International Ltd.
*NIFTY_NEXT_50 · Automobile and Auto Components · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +0.3%**, **12 months +0.3%** (rank 69 / 79 of 200 for 3m / 12m); beta 1.36
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +25.6%): 3 months 51%, 12 months 48%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -3.4% … P90 +5.7%; plausible 12m relative-return range incl. stock-specific noise: -32.1% … +33.9%
- Decomposition (12m): 0.5 × forward event exposure +1.6% (3m +0.6%; half assumed priced; market-priced macro drift removed) + 0.5 × company-specific catalysts -0.4%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply +6.0% (beta-adjusted) vs a realised market-adjusted move of +11.5% — gap -5.5 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +3.19 | +0.00 | +2.46 | +0.47 | +0.26 | — |
| Indian vehicle demand (`F_AUTO_DEMAND_IN`) | +10% volumes | +3.00 | +3.00 | +0.00 | +0.00 | +0.00 | — |
| Chip/electronics component supply tightness (higher = tighter) (`F_SEMICONDUCTOR_SUPPLY`) | +1 = tightening | -3.00 | -3.00 | +0.00 | +0.00 | +0.00 | — |
| US–China trade decoupling (`C_US_CHINA_DECOUPLING`) | +1 = more decoupling | -2.23 | +0.00 | -1.56 | -0.67 | -0.00 | — |
| India 10-year G-sec yield (`F_GSEC_10Y_IN`) | +25 bp yield | -2.00 | -2.00 | +0.00 | +0.00 | +0.00 | — |
| US tariffs on imported autos and auto parts (incl. Mexico/USMCA) (`NEW_US_AUTO_PARTS_TARIFFS`) | +10pp average tariff | -2.00 | -2.00 | +0.00 | +0.00 | +0.00 | — |
| Critical-mineral supply tightness (China export controls on rare earths, magnets, graphite, Ga/Ge) (`NEW_RARE_EARTH_SUPPLY`) | +1 = new/tighter export-control round | -1.64 | +0.00 | -1.68 | +0.04 | +0.00 | — |
| Europe growth (`F_EU_GDP`) | +1 pp | +1.50 | +1.50 | +0.00 | +0.00 | +0.00 | — |
| USD/CNY (`F_USDCNY`) | +3% USD/CNY (yuan weaker) | -1.45 | -1.50 | +0.06 | +0.00 | -0.01 | -1.4% |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -1.39 | +0.00 | -1.30 | -0.08 | -0.01 | — |
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +1.37 | +0.00 | +1.44 | +0.01 | -0.08 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -1.15 | +0.00 | -0.24 | -1.02 | +0.11 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -1.09 | +0.00 | -1.15 | +0.09 | -0.03 | — |
| US growth (`F_US_GDP`) | +1 pp | +0.97 | +1.20 | -0.05 | -0.07 | -0.11 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -2.8% | -2.8% | -2.8 | +0.0 | +0.0 | -0.0 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -1.4% | -1.4% | +0.0 | -0.3 | -1.3 | +0.1 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -1.2% | -1.2% | -0.6 | -0.5 | -0.1 | -0.0 |
| US Q3 data: GDP 3.4%, CPI 3.7%, September payrolls only +29k (`EV_US_Q3_DATA_MIXED`) | occurred | 1.00 | +1.1% | +1.1% | +1.2 | +0.1 | -0.2 | -0.0 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -1.0% | -1.0% | -0.4 | -0.5 | -0.1 | -0.0 |
| Budget FY2027-28: FY27 deficit overshoot confirmed and consolidation path slowed (`EV_BUDGET_FY28_FISCAL_SLIPPAGE`) | scheduled | 0.50 | -1.6% | -0.8% | -1.6 | +0.0 | +0.0 | -0.0 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.55 | +1.3% | +0.7% | +0.8 | +0.3 | +0.0 | +0.2 |
| China re-imposes/hardens rare-earth and critical-mineral export controls hitting India's autos and electronics (`EV_RARE_EARTH_CONTROLS_REIMPOSED`) | risk_scenario | 0.25 | -2.7% | -0.7% | -0.9 | -1.9 | +0.1 | -0.0 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -0.7% | -0.7% | +0.0 | -0.6 | +0.0 | -0.0 |
| Aluminium -20% since June; copper off record; Nifty Metal -7% in October (`EV_BASE_METALS_ALUMINIUM_SLIDE`) | occurred | 1.00 | +0.6% | +0.6% | +0.6 | +0.0 | +0.0 | +0.0 |
| RBI MPC Dec 2026 (~4 Dec): hikes repo another 25 bp to 5.75% (`EV_RBI_DEC26_HIKE25`) | scheduled | 0.42 | -1.2% | -0.5% | -0.6 | -0.5 | -0.1 | -0.0 |
| FOMC 8-9 Dec 2026: 25 bp hike to 4.00-4.25% (`EV_FED_DEC26_HIKE25`) | scheduled | 0.72 | -0.7% | -0.5% | -0.4 | -0.2 | -0.1 | -0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_US_RECESSION_RISK_2027 ⇒ F_US_GDP → MOTHERSON | -3.60% | -0.90% |
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → MOTHERSON | -1.60% | -0.80% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_AI_CAPEX → F_SEMICONDUCTOR_SUPPLY → MOTHERSON | +2.16% | +0.54% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → MOTHERSON | +0.78% | +0.43% |
| 1 | EV_INDIA_EU_FTA_SIGNED ⇒ F_EU_GDP → MOTHERSON | +0.45% | +0.41% |
| 2 | EV_RARE_EARTH_CONTROLS_REIMPOSED ⇒ NEW_RARE_EARTH_SUPPLY → F_AUTO_DEMAND_IN → MOTHERSON | -1.44% | -0.36% |
| 1 | EV_FERT_SUBSIDY_TOPUP_WINTER ⇒ F_GSEC_10Y_IN → MOTHERSON | -0.40% | -0.36% |
| 1 | EV_CPI_BREACH_6PCT ⇒ F_GSEC_10Y_IN → MOTHERSON | -0.60% | -0.36% |
| 1 | EV_BANKING_LIQUIDITY_DEFICIT_MAR27 ⇒ F_GSEC_10Y_IN → MOTHERSON | -0.60% | -0.36% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_GSEC_10Y_IN → MOTHERSON | -2.00% | -0.36% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → MOTHERSON | -1.32% | -0.33% |
| 1 | EV_RBI_DEC26_HOLD ⇒ F_GSEC_10Y_IN → MOTHERSON | +0.60% | +0.31% |
| 1 | EV_US_RECESSION_RISK_2027 ⇒ F_FED_FUNDS → MOTHERSON | +1.20% | +0.30% |
| 1 | EV_FED_DEC26_HIKE25 ⇒ F_FED_FUNDS → MOTHERSON | -0.40% | -0.29% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_USDINR → MOTHERSON | +1.56% | +0.28% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_GSEC_10Y_IN → MOTHERSON | +1.55 | director_override | -3.10% |
| 1 | F_AUTO_DEMAND_IN → MOTHERSON | +0.50 | director_override | +1.50% |
| 1 | F_US_GDP → MOTHERSON | +1.20 | events | +1.44% |
| 1 | F_USDCNY → MOTHERSON | -0.47 | observed | +0.70% |
| 1 | F_FED_FUNDS → MOTHERSON | +1.62 | observed | -0.65% |
| 1 | F_ALUMINIUM → MOTHERSON | -1.96 | observed | +0.59% |
| 1 | F_GAS_GLOBAL → MOTHERSON | +1.00 | director_override | -0.50% |
| 1 | F_USDINR → MOTHERSON | -0.37 | observed | -0.44% |
| 1 | F_EU_GDP → MOTHERSON | +0.22 | events | +0.33% |
| 1 | T_ENERGY_TRANSITION → MOTHERSON | +0.30 | director_override | +0.30% |
| 2 | F_AI_CAPEX → F_SEMICONDUCTOR_SUPPLY → MOTHERSON | -0.30 | events | +0.22% |
| 2 | C_US_CHINA_DECOUPLING → F_SEMICONDUCTOR_SUPPLY → MOTHERSON | -0.10 | events | +0.10% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-11 | Q2 FY27 consolidated results (trading window closed from late Sep; date not retrieved) | results | 0.95 | +0.0% | +0.00% |
| 2026-12 | Completion of Rotary Connectors 50.1% acquisition (approvals pending) | corporate_action | 0.70 | +0.5% | +0.35% |
| 2027-02 | Q3 FY27 results and European production read-through | results | 0.95 | +0.0% | +0.00% |
| 2027-03 | US-Mexico/USMCA auto tariff outcome and EU-US trade terms | regulatory | 0.50 | -1.5% | -0.75% |

## Analyst profile (agent research, sourced)
# Samvardhana Motherson International (MOTHERSON) — Market Impact profile, 2026-11-05

## Business
SAMIL is the flagship of the Motherson Group and a global tier-1 supplier. Its core is wiring harnesses, rear-view mirrors and vision systems, and plastic modules (bumpers, cockpits) through Peguform and SMRC, supplemented by new businesses in aerospace, medical, electronics and logistics. Around 80% of revenue is earned outside India (model knowledge): Europe 40-45%, Americas ~20%, Asia the rest. Customers are mostly German and US OEMs, with Indian OEMs a growing minority. Net debt is substantial (~1.3x EBITDA, estimate), giving equity holders a leveraged claim on a ~10.5% EBITDA margin. The stock has strong momentum (+28% in six months, +59.7% in twelve) and trades with a market beta of ~1.5. No screener dossier was available, so the consolidated Q2 FY27 numbers were not retrieved; the profile relies on pack sensitivities, news and model knowledge.

## What moves the stock (ranked)
1. **European auto production (C_EU_UK +1.5 per +1pp) and US production (+1.2).** Highly operating-levered; German OEM weakness is the largest swing.
2. **Global risk appetite and China read-through.** Empirical USD/CNY (-5.4, t=-2.7) is the only strongly significant FX series; it is a risk-sentiment proxy.
3. **Tariff / trade policy (US auto parts -2.0).** Mexico and US plants sit inside USMCA supply chains; talks stalled in October.
4. **Semiconductor and rare-earth supply (-3.0).** OEM stoppages hit schedule volumes immediately.
5. **USD/INR (+1.2 per +3%)**: the translation effect is positive for a company earning abroad.
6. **India auto volumes (+3.0 per +10%).** Motherson Sumi Wiring India revenue grew 47% in Q2.
7. **Commodities (copper, resins, aluminium)**: small thanks to pass-through, but timing lags cause quarterly noise. The empirical copper and aluminium betas are positive (aluminium t=2.9), reflecting the cycle, not costs.
8. **Rates (G-sec -2.0; Fed -0.4)** via valuation and floating debt.

## Transmission examples
- **Mideast escalation (4 orders).** Hormuz risk -> Brent $95-100 -> polymer resin and European energy up -> SMRC cost lags pass-through by a quarter -> margin dips ~20-30bp; in parallel, Brent up -> inflation and weaker euro-area consumer -> European car registrations soften -> Peguform/SMP volumes fall -> operating leverage cuts EBIT by 2-3x the revenue move.
- **Tariff chain (3-4 orders).** US-Mexico talks collapse -> tariffs on Mexican-assembled vehicles/parts -> US OEMs shift or cut production -> Motherson's Mexican wiring and module plants lose schedules -> price renegotiation with OEMs lags -> EBIT hit.
- **Rate-differential chain (3 orders).** US 10-year at 4.89% and a stronger dollar -> EM/FPI outflows -> high-beta Indian large caps sell off -> MOTHERSON falls more than Nifty despite an INR-translation tailwind.
- **Copper chain (2 orders).** Copper up -> wiring harness cost up -> pass-through with 1-3 month lag -> short-term working-capital drag -> reversal when index resets.
- **Energy transition (3 orders).** EV adoption -> more wiring/high-voltage content per vehicle and thermal/vision modules -> revenue per vehicle up -> offset by EV volume uncertainty in Europe.

## Current situation
Q1 FY27 results pushed the stock to a record in August. Since then: the Rotary Connectors acquisition (50.1%, EV Rs 500 cr, 2026-09-21) adds a defence-connector leg; a US indirect subsidiary was incorporated (2026-09-23); MSWIL reported revenue +47% and PAT +35% (Q2 FY27), though margins declined. SAMIL's own Q2 FY27 results are pending (trading window closed from late September). The October 7 RBI hike and September auto-sales dip hit sentiment briefly, but the stock still gained 4.3% in the last month.

## Upcoming events
Q2 FY27 results (November), Rotary Connectors closing, Q3 results (February 2027), US/Mexico tariff outcomes, Union Budget (1 Feb 2027).

## Bull case
European volumes stabilise, new businesses scale towards 45% of revenue, deleveraging continues, and INR weakness inflates reported profit.

## Bear case
OEM restructuring in Germany, US tariffs, or a chip shock cuts volumes; high leverage and 1.5 beta magnify any FPI outflow; after a 60% run, valuation leaves little room. Limits: no fundamentals retrieved; cost and geography splits are estimates; the Q2 FY27 date is unconfirmed.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.