# DIVISLAB — Divi's Laboratories Ltd.
*NIFTY_NEXT_50 · Healthcare · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +0.4%**, **12 months +0.9%** (rank 51 / 34 of 200 for 3m / 12m); beta 0.88
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +20.3%): 3 months 52%, 12 months 51%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -5.0% … P90 +4.8%; plausible 12m relative-return range incl. stock-specific noise: -26.1% … +28.2%
- Decomposition (12m): 0.5 × forward event exposure +1.2% (3m +1.1%; half assumed priced; market-priced macro drift removed) + 0.5 × company-specific catalysts +1.0%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply -0.9% (beta-adjusted) vs a realised market-adjusted move of +49.8% — gap -50.6 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## Where the expected return comes from
Market-priced macro drivers (rates, FX, commodities, indices, volatility, flows, growth, inflation) are taken as priced, so what is left is policy, regulatory, sector, theme, geopolitical and company-specific exposure — where 2nd–4th-order effects are most likely to be missed. Percentage points of the expected relative return.
| source | 12m: 1st order | 12m: 2nd–4th order | 12m total | 3m total |
|---|---|---|---|---|
| Policy | -0.42 | -0.07 | -0.49 | -0.30 |
| Sector | -0.13 | +0.20 | +0.07 | +0.02 |
| Theme | +1.53 | +0.00 | +1.54 | +1.08 |
| Geopolitics | +0.00 | -0.03 | -0.03 | -0.04 |
| Company catalysts | +0.51 | +0.00 | +0.51 | +0.00 |
| Market-priced macro | +0.00 | -0.00 | -0.00 | +0.00 |
| Beta adjustment | — | — | -0.50 | -0.23 |
| Universe centring | — | — | -0.15 | -0.10 |
| **Expected relative return** | | | **+0.94** | **+0.45** |

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| GLP-1 / obesity drug adoption (`T_GLP1`) | +1 | +8.00 | +8.00 | +0.00 | +0.00 | +0.00 | — |
| China+1 manufacturing relocation to India (`T_CHINA_PLUS_ONE`) | +1 | +3.47 | +3.50 | -0.09 | +0.04 | +0.02 | — |
| China chemical/API dumping intensity (`F_CHINA_CHEM_EXPORTS`) | +15% export volumes / price cuts | -3.02 | -3.00 | +0.00 | -0.02 | +0.00 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +2.86 | +3.00 | -0.15 | +0.00 | +0.01 | — |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -2.14 | -1.50 | -0.43 | -0.22 | +0.01 | +3.5% |
| USFDA inspection/enforcement intensity (`P_USFDA_ENFORCEMENT`) | +1 = stricter | -2.10 | -2.40 | +0.30 | +0.00 | +0.00 | — |
| US average effective tariff rate (all partners) (`NEW_US_TARIFF_GLOBAL`) | +5 pp effective tariff rate | -1.69 | +0.00 | -0.92 | -0.41 | -0.35 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -1.64 | +0.00 | -1.08 | -0.38 | -0.18 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | +1.55 | +2.20 | -0.48 | -0.09 | -0.08 | -1.1% |
| US generic drug price erosion (higher = worse) (`F_US_GENERIC_PRICING`) | +5 pp erosion | -1.50 | -1.50 | +0.00 | +0.00 | +0.00 | — |
| USD/JPY exchange rate (`NEW_USDJPY`) | +3% USD/JPY (yen weaker) | +1.44 | +0.00 | +1.32 | +0.05 | +0.07 | — |
| US tariffs on Indian goods (`P_US_TARIFF_INDIA`) | +10 pp average tariff | -1.39 | -0.80 | -0.54 | -0.05 | +0.00 | — |
| US tariffs on pharmaceuticals (`P_US_PHARMA_TARIFF`) | +10 pp on Indian pharma exports | -1.32 | -1.50 | +0.18 | +0.00 | +0.00 | — |
| India 10-year G-sec yield (`F_GSEC_10Y_IN`) | +25 bp yield | -1.20 | -1.20 | +0.00 | +0.00 | +0.00 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -6.3% | -6.3% | -6.6 | +0.3 | +0.0 | -0.0 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +7.7% | +3.8% | +8.1 | -0.4 | -0.0 | +0.0 |
| USFDA warning letters: Alembic, Aurobindo-Eugia, Dabur (Jul-Aug 2026) (`EV_USFDA_WARNING_WAVE_26`) | occurred | 1.00 | -2.1% | -2.1% | -2.4 | +0.3 | +0.0 | +0.0 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.25 | -7.5% | -1.9% | -3.8 | -4.0 | +0.1 | +0.1 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -1.7% | -1.7% | -1.7 | +0.0 | +0.0 | -0.0 |
| China+1 momentum: Apple/Foxconn/Tata iPhone 18 Pro export ramp, India ~50% of US smartphone imports, PLI round 4 (textiles) and component schemes (`EV_CHINA_PLUS_ONE_ELECTRONICS`) | anticipated | 0.80 | +2.1% | +1.7% | +2.1 | -0.1 | +0.0 | +0.0 |
| US midterms (3 Nov 2026): Democrats win House and Senate (`EV_US_MIDTERMS_DEM_SWEEP`) | occurred | 1.00 | +1.6% | +1.6% | +1.6 | +0.0 | -0.1 | +0.0 |
| Disorderly yen carry-trade unwind (Aug-2024-style) after BoJ/MoF action (`EV_YEN_CARRY_UNWIND_RISK`) | risk_scenario | 0.15 | -8.0% | -1.2% | -3.8 | -4.7 | +0.4 | +0.1 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.55 | +2.0% | +1.1% | +1.2 | +0.5 | +0.2 | +0.1 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.25 | -4.1% | -1.0% | -2.6 | -0.9 | -0.5 | -0.1 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -1.0% | -1.0% | +0.0 | -0.9 | -0.1 | -0.0 |
| AI/tech selloff and capex-forecast pause (Oct 2026) (`EV_AI_SELLOFF_OCT26`) | occurred | 1.00 | -1.0% | -1.0% | -0.5 | -0.5 | +0.0 | +0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → DIVISLAB | +7.50% | +3.75% |
| 1 | EV_CHINA_PLUS_ONE_ELECTRONICS ⇒ T_CHINA_PLUS_ONE → DIVISLAB | +2.10% | +1.68% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → DIVISLAB | -3.75% | -0.94% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → DIVISLAB | -4.50% | -0.81% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → DIVISLAB | -2.88% | -0.72% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_FPI_FLOWS → DIVISLAB | -2.88% | -0.72% |
| 1 | EV_INDIA_US_INTERIM_DEAL_SIGNED ⇒ T_CHINA_PLUS_ONE → DIVISLAB | +1.05% | +0.58% |
| 1 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → DIVISLAB | -3.75% | -0.56% |
| 1 | EV_PHARMA_GENERICS_TARIFF ⇒ P_US_PHARMA_TARIFF → DIVISLAB | -4.50% | -0.54% |
| 1 | EV_BUDGET_FY28_LTCG_RELIEF ⇒ F_FPI_FLOWS → DIVISLAB | +1.50% | +0.52% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_USDINR → DIVISLAB | +2.86% | +0.51% |
| 1 | EV_CHINA_FDI_EASING_PN3 ⇒ T_CHINA_PLUS_ONE → DIVISLAB | +0.70% | +0.49% |
| 1 | EV_Q2_FY27_GDP_STRONG ⇒ F_FPI_FLOWS → DIVISLAB | +0.60% | +0.48% |
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → DIVISLAB | -0.96% | -0.48% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_RISK_SENTIMENT → DIVISLAB | -1.50% | -0.38% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_FPI_FLOWS → DIVISLAB | -1.60 | events | -4.80% |
| 1 | T_GLP1 → DIVISLAB | +0.30 | director_override | +2.40% |
| 1 | F_GSEC_10Y_IN → DIVISLAB | +1.55 | director_override | -1.86% |
| 1 | P_USFDA_ENFORCEMENT → DIVISLAB | +0.40 | director_override | -0.96% |
| 1 | F_USDINR → DIVISLAB | -0.37 | observed | -0.81% |
| 1 | P_US_TARIFF_INDIA → DIVISLAB | -0.60 | events | +0.48% |
| 2 | P_FDI_RULES → T_CHINA_PLUS_ONE → DIVISLAB | +0.50 | events | +0.35% |
| 2 | F_USDCNY → F_CHINA_CHEM_EXPORTS → DIVISLAB | -0.47 | observed | +0.34% |
| 1 | P_US_PHARMA_TARIFF → DIVISLAB | +0.20 | events | -0.30% |
| 2 | F_CHINA_GDP → F_CHINA_CHEM_EXPORTS → DIVISLAB | +0.30 | events | +0.29% |
| 2 | P_ANTI_DUMPING_IN → F_CHINA_CHEM_EXPORTS → DIVISLAB | +0.40 | events | +0.29% |
| 2 | P_US_TARIFF_INDIA → T_CHINA_PLUS_ONE → DIVISLAB | -0.60 | events | +0.25% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-11 | Q2 FY27 results (screener shows Jun-26 as latest; Sep-26 quarter pending) | results | 0.95 | +0.0% | +0.00% |
| 2027-03 | NSE March 2027 index review - Divi's possible Nifty 50 inclusion (ET 2026-10-06; Sahi: ~US$824m inflows) | corporate_action | 0.45 | +3.0% | +1.35% |
| 2027-06 | New Kakinada/Visakhapatnam capex commissioning (CWIP Rs 2,113 cr at Mar-26) | capex | 0.50 | +1.0% | +0.50% |
| 2027-06 | USFDA inspection of a major unit leading to OAI/warning | regulatory | 0.07 | -12.0% | -0.84% |

## Analyst profile (agent research, sourced)
# DIVISLAB - Divi's Laboratories Ltd. (Nifty Next 50, CDMO/API)

## Business
Divi's Laboratories manufactures generic active pharmaceutical ingredients, custom-synthesis (CS) intermediates and APIs for global innovator companies, and carotenoid-based nutraceutical ingredients. It is the largest listed Indian CRDMO-type player by market cap (Rs 2.68 lakh crore) and nearly debt free (borrowings Rs 7 cr, Mar-26). Roughly 85-90% of revenue is exported and CS contributes the larger share (model knowledge; a primary segment split could not be retrieved in this run). TTM sales are Rs 11,230 cr with a 35% EBITDA margin; Q1 FY27 margin spiked to 41% on better mix and volumes. Capex is ongoing (CWIP Rs 2,113 cr at Mar-26 against fixed assets of Rs 6,528 cr).

## What moves the stock, ranked
1. **Oral GLP-1 / large-molecule-adjacent CS pipeline (T_GLP1, +8 per unit).** The 2026 re-rating is driven by the market linking Divi's to obesity-drug intermediates: Citi's Rs 11,700 target rests on "oral Wegovy upside" (NDTV Profit, 2026-09-23) and the stock rose on the EU panel nod for Lilly's pill (CNBC TV18, 2026-10-19). Treat the customer link as unconfirmed market narrative. This is the single biggest source of upside and of de-rating risk.
2. **Multiple risk (FPI flows +3.0, risk sentiment -1.5, G-sec -1.2).** At P/E 90, small moves in discount rate or sentiment dominate. An RBI hike on 2026-10-07 and US 10y at 4.9% are headwinds; the post-midterm risk-on is a tailwind.
3. **USD/INR (+2.2 per +3%).** Rupee at 94.5, near record weakness, supports reported margin; effect is partial given hedging.
4. **Chinese competition and China+1 (-3.0 / +3.5).** Generic API pricing vs CS order flow shifting out of China.
5. **US trade and regulatory (tariff -1.5, USFDA -6.0 conditional tail).**
6. **Input costs (feedstock -0.8, Brent -0.5, wages -0.3).**
7. **Index event:** potential Nifty 50 inclusion (March 2027 review) - est. 45% probability, +1 to +5%.

## Transmission examples
- **Oral GLP-1 approval -> Lilly/Novo scale-up -> intermediate/KSM demand -> Divi's CS volumes -> EBITDA.** 1st: EC approval after EU panel nod; 2nd: global GLP-1 pill supply chain builds inventory; 3rd: Indian CRDMO orders (Divi's, Laurus) rise; 4th: Divi's capex and margin guidance rise, valuations re-rate. Reverse: trial or safety setback or price-war in GLP-1 -> orders cut -> 15-25% de-rating.
- **Middle East escalation -> Brent up -> INR down -> Divi's exports worth more rupees (+) but solvent and freight costs (-) and risk-off FPI selling in high-P/E names (-).** Net approximately zero to slightly negative because FPI flow and multiple compression dominate.
- **US tariff headline on Indian pharma -> API customers' pricing talks -> CS contracts re-priced -> margin -150-250bp; plus China+1 customers still need non-China suppliers (partial offset).**
- **China stimulus -> Chinese API output cheaper -> Indian generic API price pressure -> Divi's generic segment margins -> small effect because CS is cost-plus.**

## Current situation
Q1 FY27: sales Rs 3,080 cr (+28% YoY), EBITDA Rs 1,255 cr, PAT Rs 902 cr, EPS Rs 33.98. The Sep-26 quarter results are due in November (date not yet in the sources fetched). Promoter 51.87%; FIIs 20.4%. Stock Rs 10,082 (12m +48%, 52-week high Rs 10,153). Citi Buy; Jefferies positive on CRDMO.

## Upcoming events
Q2 FY27 results (Nov 2026); EC decision on Lilly's oral GLP-1 (Dec 2026); March 2027 NSE index review; Q3 results (Feb 2027).

## Bull and bear
**Bull:** GLP-1 supply contracts, 40%+ margins sustained by CS mix, nearly zero leverage, INR tailwind, Nifty 50 inclusion flows. **Bear:** at 90x earnings and 16x book, any CS order delay, tariff headline or USFDA action can cause 10-20% drawdowns; customer concentration is opaque; the margin spike may include one-offs. Confidence medium: financials from screener, narrative items from headlines only (primary conference-call text unavailable here).


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.