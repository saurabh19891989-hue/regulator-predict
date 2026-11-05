# BPCL — Bharat Petroleum Corporation Ltd.
*NIFTY_NEXT_50 · Oil Gas & Consumable Fuels · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +4.5%**, **12 months +10.4%** (rank 16 / 13 of 200 for 3m / 12m); beta 1.24
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +19.7%): 3 months 68%, 12 months 65%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 +3.0% … P90 +18.6%; plausible 12m relative-return range incl. stock-specific noise: -9.5% … +40.3%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +4.7 pp (model impact +10.6% beta-adjusted vs realised market-adjusted move +1.3%); forward event exposure +11.0% (3m +4.9%; half assumed priced); company-specific events +2.8%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| OMC petrol+diesel marketing margin (`NEW_OMC_MARKETING_MARGIN`) | +Rs1/litre average marketing margin (vs normal ~Rs3-4/l) | +5.97 | +6.00 | +0.00 | -0.01 | -0.01 | — |
| Russia (oil discounts, defence, sanctions) (`C_RUSSIA`) | +1 = closer trade access / larger discounts | +5.03 | +3.00 | +2.52 | -0.52 | +0.03 | — |
| Refining margins (GRM / cracks) (`F_REFINING_MARGIN`) | +$2/bbl gross refining margin | +4.91 | +5.00 | -0.09 | +0.00 | +0.00 | +15.4% |
| Brent crude oil price (`F_BRENT`) | +10% Brent | -4.74 | -5.50 | +0.88 | -0.10 | -0.02 | +0.0% |
| Fuel excise / retail price policy (+ = higher taxes/regulated squeeze) (`P_FUEL_TAX_IN`) | +1 = Rs 2/litre excise rise | -4.02 | -4.00 | +0.00 | -0.02 | +0.00 | — |
| Windfall / export taxes on commodities (`P_WINDFALL_EXPORT_TAX`) | +1 = imposition | -2.67 | -1.50 | -1.20 | +0.00 | +0.03 | — |
| OPEC+ crude supply decisions (`NEW_OPEC_PLUS_SUPPLY`) | +1 mb/d OPEC+ production (quota/actual) | +2.60 | +0.00 | +3.52 | -1.06 | +0.14 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -2.07 | -1.50 | -1.50 | +1.09 | -0.16 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -1.63 | -1.50 | -0.03 | -0.10 | +0.00 | -1.1% |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -1.53 | +0.00 | -0.36 | -1.24 | +0.07 | — |
| China growth / stimulus (`F_CHINA_GDP`) | +1 pp | -1.32 | +0.00 | -1.76 | +0.50 | -0.06 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -1.12 | +0.00 | -1.22 | +0.08 | +0.02 | — |
| US growth (`F_US_GDP`) | +1 pp | -0.86 | +0.00 | -1.27 | +0.35 | +0.07 | — |
| Red Sea / Suez shipping disruption (`C_RED_SEA`) | +1 = disruption | +0.77 | +0.00 | +0.82 | -0.05 | +0.00 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -20.7% | -20.7% | -22.0 | +1.9 | -0.5 | -0.1 |
| Retail petrol/diesel price freeze with crude >$100 squeezes OMC marketing margins; Q2 FY27 results split refiners (`EV_OMC_FUEL_FREEZE_LOSSES`) | occurred | 1.00 | -17.9% | -17.9% | -18.0 | +0.0 | +0.0 | +0.0 |
| Government allows OMCs a retail petrol/diesel price hike (Rs3-5/l) (`EV_INDIA_RETAIL_FUEL_HIKE`) | anticipated | 0.45 | +14.7% | +6.6% | +15.0 | -0.4 | +0.1 | -0.0 |
| Domestic LPG under-recoveries >Rs59,000 cr (to July); government compensation boosts IOC Q2 (`EV_LPG_UNDERRECOVERY`) | occurred | 1.00 | -6.0% | -6.0% | -6.0 | +0.0 | +0.0 | +0.0 |
| US waives Russia-oil secondary sanctions/100% tariff threat on buyers incl. India (17 Oct) (`EV_RUSSIA_WAIVER_OCT17`) | occurred | 1.00 | +5.3% | +5.3% | +3.0 | +2.7 | -0.4 | +0.1 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.36 | -11.8% | -4.2% | -15.6 | +4.1 | -0.3 | -0.2 |
| Cabinet approves further LPG under-recovery compensation to OMCs (`EV_LPG_COMPENSATION_CABINET`) | anticipated | 0.60 | +6.0% | +3.6% | +6.0 | +0.0 | -0.0 | -0.0 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.58 | +5.6% | +3.2% | +5.8 | -0.6 | +0.4 | +0.1 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -2.3% | -2.3% | +0.0 | -1.8 | -0.5 | +0.0 |
| India cuts Russian crude below ~1 mb/d as part of US trade deal (`EV_RUSSIAN_CRUDE_CUT_TRADE_DEAL`) | anticipated | 0.30 | -6.5% | -1.9% | -5.5 | -1.3 | +0.3 | -0.0 |
| Hormuz effectively closed for >2 weeks (Brent > $150) (`EV_HORMUZ_FULL_CLOSURE`) | risk_scenario | 0.06 | -28.6% | -1.8% | -36.8 | +9.2 | -0.7 | -0.4 |
| Waiver lapses and US imposes secondary tariff (up to 100%) or sanctions on Indian refiners buying Russian oil (`EV_RUSSIA_TARIFF_ENFORCED`) | risk_scenario | 0.15 | -8.8% | -1.3% | -7.4 | -1.2 | -0.1 | -0.1 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_INDIA_RETAIL_FUEL_HIKE ⇒ NEW_OMC_MARKETING_MARGIN → BPCL | +15.00% | +6.75% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → BPCL | -13.75% | -4.91% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → BPCL | +8.25% | +4.79% |
| 1 | EV_LPG_COMPENSATION_CABINET ⇒ NEW_OMC_MARKETING_MARGIN → BPCL | +6.00% | +3.60% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_REFINING_MARGIN → BPCL | -4.00% | -2.32% |
| 1 | EV_HORMUZ_FULL_CLOSURE ⇒ F_BRENT → BPCL | -33.00% | -2.06% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_GDP → F_BRENT → BPCL | +3.96% | +0.99% |
| 1 | EV_RUSSIAN_CRUDE_CUT_TRADE_DEAL ⇒ C_RUSSIA → BPCL | -3.00% | -0.90% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ C_MIDEAST_CONFLICT → BPCL | +1.50% | +0.87% |
| 2 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ C_MIDEAST_CONFLICT → F_REFINING_MARGIN → BPCL | +2.24% | +0.80% |
| 2 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → P_FUEL_TAX_IN → BPCL | +2.13% | +0.76% |
| 1 | EV_RUSSIAN_CRUDE_CUT_TRADE_DEAL ⇒ F_REFINING_MARGIN → BPCL | -2.50% | -0.75% |
| 2 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → P_FUEL_TAX_IN → BPCL | -1.28% | -0.74% |
| 1 | EV_RUSSIA_TARIFF_ENFORCED ⇒ F_BRENT → BPCL | -4.40% | -0.66% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ C_MIDEAST_CONFLICT → BPCL | -1.80% | -0.64% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_REFINING_MARGIN → BPCL | +1.54 | observed | +7.71% |
| 1 | C_RUSSIA → BPCL | +1.00 | events | +3.00% |
| 1 | NEW_OMC_MARKETING_MARGIN → BPCL | -0.50 | director_override | -3.00% |
| 1 | C_MIDEAST_CONFLICT → BPCL | +1.50 | events | -2.25% |
| 1 | P_FUEL_TAX_IN → BPCL | -0.50 | events | +2.00% |
| 1 | P_WINDFALL_EXPORT_TAX → BPCL | +1.00 | events | -1.50% |
| 1 | F_REPO_IN → BPCL | +1.00 | events | -0.80% |
| 1 | F_USDINR → BPCL | -0.37 | observed | +0.55% |
| 1 | P_EV_POLICY → BPCL | +1.10 | events | -0.44% |
| 1 | F_GDP_IN → BPCL | +0.50 | events | +0.30% |
| 1 | F_SHIPPING_RATES → BPCL | +0.30 | events | -0.12% |
| 1 | F_BRENT → BPCL | +0.00 | observed | -0.01% |

## Analyst profile (agent research, sourced)
# BPCL — Bharat Petroleum Corporation Ltd. (Nifty Next 50, I_REFINING_OMC) — as of 2026-11-05

## Business
Government-owned (53%) oil refiner and marketer. Refining capacity is ~38-40 Mtpa at Mumbai, Kochi and Bina (with a petrochemical expansion at Bina); marketing covers roughly a quarter of India's petrol, diesel and LPG through ~23,000 outlets, plus lubricants, aviation fuel and city-gas stakes. Retail pump prices are effectively administered, so the earnings sign on crude is negative in the short run, unlike a merchant refiner. TTM sales are Rs538,088 cr but EBITDA only Rs26,238 cr (4.9%); FY26 EBITDA was Rs41,202 cr. Market cap is Rs1.38 lakh cr; P/E 9.8; dividend yield 5.6%.

The war-driven crude spike produced a Q1 FY27 loss (EBITDA Rs-4,055 cr, PAT Rs-1,873 cr); Q2 recovered to EBITDA Rs8,973 cr and PAT Rs4,863 cr (-21.5% YoY) on strong refining and still-weak marketing margins.

## What moves the stock (ranked)
1. **Brent** (w -5.5 per +10%): the main swing. ICRA said OMCs lost Rs530 cr a day (2026-09-23). Empirical -2.16 (t=-4.4) over three years understates the sensitivity in a frozen-price regime; the weight is a compromise.
2. **Refining margin** (+5 per +$2): about 290 mn bbl throughput; +$2 = ~Rs5,500 cr. The pack shows -1.61 (t=-3.4), but the proxy is a heating-oil future that moves with diesel spikes, so the sign conflict is flagged rather than adopted.
3. **Fuel tax and compensation policy** (-4, wide range): excise changes absorbed by OMCs, the Rs75,000 cr compensation request (Centre to decide in 2027).
4. **Russia access** (+3): discounted crude, now threatened by the US sanctions law; BPCL expects lower Russian purchases in November.
5. **USD/INR** (-1.5), **Gulf conflict** (-1.5 beyond Brent), **repo** (-0.8), freight (-0.4), GDP (+0.6), EV policy (-0.4), windfall levy (-1.5).

## Transmission examples
- **Iran talks succeed:** Brent falls (Brent -8% on 2026-11-02 on peace hopes) -> under-recoveries on LPG, diesel and petrol shrink (1st) -> OMC marketing margin recovers while retail prices stay unchanged (2nd) -> BPCL quarterly EBITDA moves back toward the Rs10-11k cr run-rate (3rd) -> higher cash flow supports the 5.6% dividend and Andhra refinery funding (4th). Also, a lower oil bill strengthens the rupee, trimming import cost further, and eases CPI so RBI may hold rates, supporting fuel demand growth.
- **Escalation / Hormuz attack:** tanker attacks (Reuters, 2026-09-10) -> Brent above $100 -> BPCL's Gulf-sourced crude (55% secured for October) must be replaced by costlier WTI or Russian cargoes (1st-2nd) -> freight and insurance rise -> GRM may rise too, but frozen retail prices let marketing losses dominate (3rd) -> government pressure for compensation and a stake sale to fund subsidies (4th).
- **Russia sanctions:** US law and tariff threat (waived 2026-10-27) -> Russian purchases fall -> BPCL buys at a smaller discount -> ~$3/bbl x 25% of 290 mn bbl = ~Rs2,000 cr EBITDA lost, partly offset by lower war-risk premia.
- **Rates path:** Higher RBI repo -> working capital interest up (small) -> discount rate on a bond-proxy PSU up -> multiple compression.

## Current situation
Stock Rs318, up 5.7% in a month but -14.8% over twelve months. Analysts raised targets (Rs305-347) after Q2. LPG loss per cylinder eased from Rs507 to Rs290 but November brings a 'twist' (ET NOW, 2026-10-26). The Andhra Pradesh Ramayapatnam refinery-petchem complex (Rs1.45 lakh cr) has an environmental clearance recommendation (2026-10-04) and a subsidiary is to be set up (2026-10-23). Brent figure caution: factor_state shows 94.99 (front-month Yahoo close), while headlines quote $100-110 on 2-4 Nov; the weight is built on the factor_state level and the discrepancy is unresolved.

## Upcoming events
Q3 FY27 results late Jan 2027; compensation decision (prob 0.45 by Mar 2027, +4 to +12%); Russian sanctions outcome (0.4, -5 to +2%); November LPG price action.

## Bull and bear
Bull: peace deal, compensation, strong GRM. Bear: Brent rebound with frozen prices, no compensation, large capex under government direction. Confidence medium; cost splits and volumes are model estimates not filed in the pack.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.