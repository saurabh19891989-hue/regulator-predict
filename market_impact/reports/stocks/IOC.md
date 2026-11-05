# IOC — Indian Oil Corporation Ltd.
*NIFTY_NEXT_50 · Oil Gas & Consumable Fuels · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +3.4%**, **12 months +7.0%** (rank 3 / 2 of 200 for 3m / 12m); beta 1.27
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +20.5%): 3 months 63%, 12 months 72%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 +2.1% … P90 +14.0%; plausible 12m relative-return range incl. stock-specific noise: -13.7% … +42.3%
- Decomposition (12m): 0.5 × forward event exposure +10.7% (3m +5.1%; half assumed priced) + 0.5 × company-specific catalysts +4.2%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply +3.4% (beta-adjusted) vs a realised market-adjusted move of -1.2% — gap +4.6 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| OMC petrol+diesel marketing margin (`NEW_OMC_MARKETING_MARGIN`) | +Rs1/litre average marketing margin (vs normal ~Rs3-4/l) | +6.49 | +6.50 | +0.00 | -0.01 | +0.00 | — |
| Refining margins (GRM / cracks) (`F_REFINING_MARGIN`) | +$2/bbl gross refining margin | +3.95 | +4.00 | -0.05 | +0.00 | +0.00 | +15.4% |
| Russia (oil discounts, defence, sanctions) (`C_RUSSIA`) | +1 = closer trade access / larger discounts | +3.54 | +2.50 | +1.17 | -0.15 | +0.02 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -3.50 | -3.50 | -0.08 | +0.32 | -0.24 | — |
| Government compensation to OMCs for fuel/LPG under-recoveries (`NEW_OMC_COMPENSATION`) | +1 = Rs25,000 cr compensation to oil marketing companies | +3.20 | +3.20 | +0.00 | +0.00 | +0.00 | — |
| Brent crude oil price (`F_BRENT`) | +10% Brent | -2.31 | -2.20 | +0.08 | -0.19 | -0.01 | +0.0% |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -1.84 | -1.80 | +0.02 | -0.05 | -0.01 | -1.1% |
| Windfall / export taxes on commodities (`P_WINDFALL_EXPORT_TAX`) | +1 = imposition | -1.76 | -0.80 | -0.96 | +0.00 | +0.00 | — |
| Petrochemical / polymer spreads (`F_PETROCHEM_SPREADS`) | +10% polymer-naphtha spreads | +1.50 | +1.50 | +0.00 | +0.00 | +0.00 | — |
| OPEC+ crude supply decisions (`NEW_OPEC_PLUS_SUPPLY`) | +1 mb/d OPEC+ production (quota/actual) | +1.49 | +0.00 | +1.41 | -0.05 | +0.13 | — |
| Red Sea / Suez shipping disruption (`C_RED_SEA`) | +1 = disruption | +1.27 | +0.00 | +1.28 | -0.01 | +0.00 | — |
| India real GDP growth (`F_GDP_IN`) | +1 pp | +1.06 | +1.20 | -0.19 | +0.05 | -0.00 | — |
| Fuel excise / retail price policy (+ = higher taxes/regulated squeeze) (`P_FUEL_TAX_IN`) | +1 = Rs 2/litre excise rise | -1.01 | -1.00 | +0.00 | -0.01 | +0.01 | — |
| Global natural gas / LNG price (`F_GAS_GLOBAL`) | +15% gas/LNG price | -0.70 | -0.70 | +0.00 | +0.00 | +0.00 | -7.0% |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Domestic LPG under-recoveries >Rs59,000 cr (to July); government compensation boosts IOC Q2 (`EV_LPG_UNDERRECOVERY`) | occurred | 1.00 | -6.5% | -6.5% | -6.5 | +0.0 | +0.0 | +0.0 |
| Retail petrol/diesel price freeze with crude >$100 squeezes OMC marketing margins; Q2 FY27 results split refiners (`EV_OMC_FUEL_FREEZE_LOSSES`) | occurred | 1.00 | -6.5% | -6.5% | -6.5 | +0.0 | +0.0 | +0.0 |
| Government allows OMCs a retail petrol/diesel price hike (Rs3-5/l) (`EV_INDIA_RETAIL_FUEL_HIKE`) | anticipated | 0.30 | +16.1% | +4.8% | +16.2 | -0.2 | +0.0 | +0.0 |
| US waives Russia-oil secondary sanctions/100% tariff threat on buyers incl. India (17 Oct) (`EV_RUSSIA_WAIVER_OCT17`) | occurred | 1.00 | +3.9% | +3.9% | +2.5 | +1.4 | -0.0 | +0.0 |
| Cabinet approves further LPG under-recovery compensation to OMCs (`EV_LPG_COMPENSATION_CABINET`) | anticipated | 0.60 | +6.5% | +3.9% | +6.5 | +0.0 | -0.0 | +0.0 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.55 | +4.9% | +2.7% | +4.0 | +0.6 | +0.3 | +0.0 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.25 | -8.1% | -2.0% | -9.7 | +2.0 | -0.2 | -0.1 |
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -1.4% | -1.4% | -1.1 | -0.3 | -0.0 | -0.0 |
| India cuts Russian crude below ~1 mb/d as part of US trade deal (`EV_RUSSIAN_CRUDE_CUT_TRADE_DEAL`) | anticipated | 0.30 | -4.6% | -1.4% | -4.5 | -0.2 | +0.1 | -0.0 |
| Windfall/export levy re-set: petrol nil, diesel Rs11.5/l, ATF ~Rs11/l (31 Oct); excise reportedly cut (3 Nov, unverified) (`EV_EXPORT_LEVY_REVISIONS`) | occurred | 1.00 | -1.3% | -1.3% | -0.3 | -1.0 | +0.0 | -0.0 |
| Waiver lapses and US imposes secondary tariff (up to 100%) or sanctions on Indian refiners buying Russian oil (`EV_RUSSIA_TARIFF_ENFORCED`) | risk_scenario | 0.15 | -6.4% | -1.0% | -4.3 | -1.8 | -0.3 | -0.0 |
| Hormuz effectively closed for >2 weeks (Brent > $150) (`EV_HORMUZ_FULL_CLOSURE`) | risk_scenario | 0.05 | -17.6% | -0.9% | -20.8 | +4.0 | -0.6 | -0.2 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_INDIA_RETAIL_FUEL_HIKE ⇒ NEW_OMC_MARKETING_MARGIN → IOC | +16.25% | +4.88% |
| 1 | EV_LPG_COMPENSATION_CABINET ⇒ NEW_OMC_MARKETING_MARGIN → IOC | +6.50% | +3.90% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ C_MIDEAST_CONFLICT → IOC | +3.50% | +1.93% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → IOC | +2.86% | +1.57% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_REFINING_MARGIN → IOC | -2.40% | -1.32% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → IOC | -4.84% | -1.21% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ C_MIDEAST_CONFLICT → IOC | -4.20% | -1.05% |
| 1 | EV_RUSSIAN_CRUDE_CUT_TRADE_DEAL ⇒ C_RUSSIA → IOC | -2.50% | -0.75% |
| 1 | EV_RUSSIAN_CRUDE_CUT_TRADE_DEAL ⇒ F_REFINING_MARGIN → IOC | -2.00% | -0.60% |
| 1 | EV_RUSSIA_WAIVER_EXTENDED ⇒ C_RUSSIA → IOC | +0.75% | +0.52% |
| 1 | EV_HORMUZ_FULL_CLOSURE ⇒ F_BRENT → IOC | -9.90% | -0.50% |
| 2 | EV_RED_SEA_CLOSURE ⇒ C_RED_SEA → F_REFINING_MARGIN → IOC | +1.92% | +0.48% |
| 2 | EV_RED_SEA_SUEZ_NORMALISATION ⇒ C_RED_SEA → F_REFINING_MARGIN → IOC | -1.02% | -0.46% |
| 2 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ C_MIDEAST_CONFLICT → F_REFINING_MARGIN → IOC | +1.79% | +0.45% |
| 1 | EV_HORMUZ_FULL_CLOSURE ⇒ C_MIDEAST_CONFLICT → IOC | -8.75% | -0.44% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | C_MIDEAST_CONFLICT → IOC | +1.00 | events | -3.50% |
| 1 | NEW_OMC_MARKETING_MARGIN → IOC | -0.50 | director_override | -3.25% |
| 1 | C_RUSSIA → IOC | +1.00 | events | +2.50% |
| 1 | F_REFINING_MARGIN → IOC | +0.60 | events | +2.40% |
| 1 | P_WINDFALL_EXPORT_TAX → IOC | +1.00 | events | -0.80% |
| 1 | F_GAS_GLOBAL → IOC | +1.00 | director_override | -0.70% |
| 1 | F_USDINR → IOC | -0.37 | observed | +0.66% |
| 1 | F_REPO_IN → IOC | +1.00 | events | -0.60% |
| 1 | F_GDP_IN → IOC | +0.50 | events | +0.60% |
| 1 | P_FUEL_TAX_IN → IOC | -0.50 | events | +0.50% |
| 2 | F_CHINA_GDP → F_PETROCHEM_SPREADS → IOC | +0.30 | events | +0.18% |
| 3 | F_USDCNY → F_CHINA_CHEM_EXPORTS → F_PETROCHEM_SPREADS → IOC | -0.47 | observed | +0.04% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-12 | Retail petrol/diesel price hike or excise cut/hike if Brent re-crosses $100 (OMCs said they can absorb $85-90, hikes likely above $100) | regulatory | 0.12 | +3.8% | +0.45% |
| 2026-12 | Interim dividend / record date announcements (Maharatna PSU, yield 5.7%; 12% interim record date reported 24 Oct 2026 - company not verified) | corporate_action | 0.50 | +0.8% | +0.38% |
| 2027-01 | Q3 FY27 results (IOC reports late Jan / early Feb; date not yet announced) - inventory loss reversal risk if crude keeps falling | results | 0.95 | -0.5% | -0.47% |
| 2027-02 | US-Iran de-escalation after Democratic midterm win: Brent below $90 restores marketing margins | other | 0.40 | +5.0% | +2.00% |
| 2027-03 | Centre decision on OMC compensation (Rs 75,000 cr ask across OMCs; LPG under-recovery) | regulatory | 0.45 | +3.5% | +1.57% |
| 2027-12 | Panipat expansion (25->33 MMTPA) / Paradip-Gujarat petchem milestones (model knowledge) | capex | 0.20 | +1.5% | +0.30% |

## Analyst profile (agent research, sourced)
# Indian Oil Corporation (IOC) — market impact profile (as of 2026-11-05)

## Business
IOC runs ~80 MMTPA of refining capacity, roughly half of India's fuel marketing, a national pipeline network, LPG, petrochemicals and gas ventures. It earns a refining margin (global, moves with crude and cracks), a marketing margin (regulated in practice: retail petrol, diesel and LPG prices are changed rarely, so the margin is the difference between a sticky pump price and a moving crude/product cost), a pipeline tariff and a smaller petchem spread. This makes IOC structurally ambivalent about crude: high crude is good for GRM and inventory, bad for marketing; the net depends on whether pump prices move and whether the government compensates. Shares: promoters 51.5%, other government 19.6%, FII 8.6%, DII 9.9%.

## What moves the stock (ranked)
1. **Brent and frozen pump prices (F_BRENT, C_MIDEAST_CONFLICT)** — the dominant driver; empirical elasticity -1.80 per +10% Brent (t -3.7) and mid-east escalation -3.5.
2. **Refining margin (F_REFINING_MARGIN)** — +4.0 per +$2/bbl; Q2 FY27 shows GRM and inventory gains can swing quarterly PAT by Rs 20k+ cr.
3. **Policy: compensation, excise and windfall levies (NEW_OMC_COMPENSATION, P_FUEL_TAX_IN, P_WINDFALL_EXPORT_TAX)** — compensation of Rs 25k cr is worth ~+3% of market cap; a Rs 2/L excise absorption ~-1%.
4. **Russian discount and sanctions (C_RUSSIA)**.
5. **USD/INR, rates, GDP, petchem, gas** — second-tier.

## Worked transmission examples
- **War -> crude -> OMC margin (4 orders).** Hormuz escalation (order 0) lifts Brent 10-15% (order 1) -> pump prices unchanged so petrol/diesel/LPG under-recover (Rs 530 cr/day industry-wide at ~$105, ICRA) (order 2: IOC EBITDA falls, as seen in Q1 FY27's operating profit of Rs 4.1k cr) -> OMC borrowings and working-capital needs rise, credit spreads widen for PSU issuers and the government considers either a retail hike or compensation (order 3) -> a retail hike lifts CPI (+0.3-0.4pp per Rs 3/L, rough estimate) so RBI delays easing, which hurts rate-sensitive sectors but lifts IOC's relative earnings once pass-through occurs (order 4).
- **Crude -> rupee -> import bill.** Brent up -> USD/INR up (crude is ~25% of India's import bill) -> IOC's rupee crude cost rises further, and USD debt marks lower -> additional EBITDA pressure beyond the dollar price effect -> government faces fiscal slippage from excise concessions.
- **Falling crude (current regime).** US midterm result -> war de-escalation hopes -> Brent below $95 -> marketing margin recovers within weeks while inventory gains reverse -> Q3 FY27 profit lower than Q2 but with a better underlying marketing contribution -> market rewards the lower volatility (OMCs +up to 7% on 5 Nov).
- **Russian-oil channel.** Wider Urals discounts -> lower crude cost for IOC -> higher GRM in INR -> yet US secondary tariffs (100% threat on Russian-oil buyers, Sep 2026) would raise trade-policy risk for Indian exporters (RELIANCE, textiles) rather than IOC directly.

## Current situation
Q2 FY27 record: standalone PAT Rs 21,630 cr, consolidated Rs 22,503 cr, driven by refining margins and inventory gains; earlier Q1 FY27 delivered a Rs 1,141 cr loss. OPM 13% vs 7% a year ago. Shares +10% in a month but -14% over 12 months at 4.3x trailing earnings and 0.89x book; Nomura target implies ~42% upside. Management warned LPG losses persist; analysts (NDTV Profit) expect H2 pain as inventory gains reverse. IOC is trimming West Asian term crude under annual deals (BS, 21 Oct). OMCs have asked for Rs 75,000 cr compensation with a decision in 2027.

## Upcoming events
Q3 FY27 results (late Jan/Feb 2027), possible pump-price or excise change, compensation decision, interim dividend, Panipat/petchem milestones, Iran war diplomacy.

## Bull case
Brent drifts to $80-90, GRM stays >$8-10/bbl (Singapore cracks wide because of diesel shortages), government compensates LPG losses, dividend yield of 6% supports a re-rating from 0.9x to 1.2x book.

## Bear case
Brent re-spikes above $105 with no pump price change, Q2 inventory gains reverse, windfall levies tighten, LPG loses Rs 25k+ cr a year, and the market treats Q2 as peak earnings.

*Weights are exposure estimates with ranges, not return forecasts.*


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.