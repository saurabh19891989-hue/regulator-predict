# LT — Larsen & Toubro Ltd.
*NIFTY_50 · Construction · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +2.3%**, **12 months +4.8%** (rank 34 / 31 of 200 for 3m / 12m); beta 1.15
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +18.9%): 3 months 60%, 12 months 50%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 +1.9% … P90 +6.7%; plausible 12m relative-return range incl. stock-specific noise: -24.1% … +16.0%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +3.0 pp (model impact +6.0% beta-adjusted vs realised market-adjusted move -4.4%); forward event exposure +5.8% (3m +1.5%; half assumed priced); company-specific events -0.1%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Gulf Cooperation Council economies (`C_GCC`) | +1 pp growth | +3.49 | +3.50 | +0.00 | -0.01 | +0.00 | — |
| Central + state government capex (`F_GOVT_CAPEX`) | +10% capex growth | +3.43 | +3.50 | +0.20 | -0.11 | -0.15 | — |
| Private corporate capex (`F_PRIVATE_CAPEX`) | +10% capex growth | +2.58 | +3.00 | +0.00 | -0.38 | -0.03 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -2.55 | +0.00 | -2.14 | -0.36 | -0.05 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -2.17 | -2.00 | -0.13 | -0.01 | -0.03 | — |
| India–Pakistan tension (`C_INDIA_PAKISTAN`) | +1 = escalation | +1.50 | +0.00 | +1.30 | +0.23 | -0.03 | — |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -1.35 | +0.00 | +0.00 | -1.18 | -0.17 | — |
| Indian defence procurement & indigenisation (`P_DEFENCE_PROCUREMENT`) | +10% domestic orders | +1.35 | +1.20 | +0.14 | +0.02 | -0.01 | — |
| Brent crude oil price (`F_BRENT`) | +10% Brent | +1.21 | +0.80 | +0.69 | -0.19 | -0.09 | +0.0% |
| General-government fiscal slippage / extra borrowing vs budget (Centre + states) (`NEW_FISCAL_SLIPPAGE_IN`) | +0.5 pp of GDP deficit above budget (~Rs2 lakh cr) | -1.20 | +0.00 | -1.12 | -0.10 | +0.02 | — |
| OPEC+ crude supply decisions (`NEW_OPEC_PLUS_SUPPLY`) | +1 mb/d OPEC+ production (quota/actual) | +1.12 | +0.00 | +1.73 | -0.82 | +0.22 | — |
| Indian data-centre build-out (`T_DATA_CENTRES_IN`) | +1 | +1.06 | +1.00 | +0.08 | +0.00 | -0.02 | — |
| India real GDP growth (`F_GDP_IN`) | +1 pp | -1.04 | +0.00 | -0.68 | -0.22 | -0.14 | — |
| US/EU enterprise IT services spend (`F_US_TECH_SPEND`) | +5% growth | +1.00 | +1.00 | +0.00 | +0.00 | +0.00 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Union Budget 2027-28 capex/railway allocation (infra, railways, defence) (`EV_BUDGET27_CAPEX_RAILWAY`) | scheduled | 0.90 | +3.9% | +3.6% | +4.0 | +0.2 | -0.1 | -0.1 |
| India Q1 FY27 GDP grows 7.8% (31 Aug 2026), beating ~7.3% consensus (`EV_GDP_Q1FY27_7_8`) | occurred | 1.00 | +3.0% | +3.0% | +3.5 | -0.1 | -0.3 | -0.1 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -2.9% | -2.9% | +0.0 | -2.5 | -0.4 | -0.0 |
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -2.8% | -2.8% | +0.0 | -2.8 | +0.0 | -0.0 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -2.2% | -2.2% | -2.0 | -0.2 | -0.0 | -0.0 |
| DAC clears Rs 1.10 lakh crore (7 Sep) and further proposals (Rs 2.12 lakh crore reported 26 Oct) (`EV_DAC_APPROVALS_H2_26`) | occurred | 1.00 | +1.3% | +1.3% | +1.2 | +0.1 | +0.0 | -0.0 |
| RBI MPC Dec 2026 (~4 Dec): hikes repo another 25 bp to 5.75% (`EV_RBI_DEC26_HIKE25`) | scheduled | 0.42 | -2.2% | -0.9% | -2.0 | -0.2 | -0.0 | -0.0 |
| US waives Russia-oil secondary sanctions/100% tariff threat on buyers incl. India (17 Oct) (`EV_RUSSIA_WAIVER_OCT17`) | occurred | 1.00 | -0.9% | -0.9% | +0.0 | -0.4 | -0.6 | +0.2 |
| Domestic LPG under-recoveries >Rs59,000 cr (to July); government compensation boosts IOC Q2 (`EV_LPG_UNDERRECOVERY`) | occurred | 1.00 | -0.7% | -0.7% | +0.0 | -0.8 | +0.0 | +0.1 |
| Retail petrol/diesel price freeze with crude >$100 squeezes OMC marketing margins; Q2 FY27 results split refiners (`EV_OMC_FUEL_FREEZE_LOSSES`) | occurred | 1.00 | -0.7% | -0.7% | +0.0 | -0.8 | +0.0 | +0.1 |
| US Q3 data: GDP 3.4%, CPI 3.7%, September payrolls only +29k (`EV_US_Q3_DATA_MIXED`) | occurred | 1.00 | +0.7% | +0.7% | +0.0 | +0.6 | +0.3 | -0.2 |
| Global and Indian steel prices at multi-year highs (global HRC +60% y/y) (`EV_STEEL_RALLY_2026`) | occurred | 1.00 | -0.7% | -0.7% | -0.7 | +0.0 | -0.0 | +0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_BUDGET27_CAPEX_RAILWAY ⇒ F_GOVT_CAPEX → LT | +2.80% | +2.52% |
| 2 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ C_MIDEAST_CONFLICT → C_GCC → LT | +2.80% | +1.54% |
| 1 | EV_BUDGET27_CAPEX_RAILWAY ⇒ P_DEFENCE_PROCUREMENT → LT | +1.20% | +1.08% |
| 2 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ C_MIDEAST_CONFLICT → C_GCC → LT | -3.36% | -0.84% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → LT | -2.00% | -0.84% |
| 2 | EV_INDIA_RETAIL_FUEL_HIKE ⇒ NEW_OMC_MARKETING_MARGIN → F_GOVT_CAPEX → LT | +2.10% | +0.63% |
| 2 | EV_PULSES_VEG_SPIKE_WINTER ⇒ F_CPI_IN → F_REPO_IN → LT | -2.30% | -0.58% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → LT | -1.04% | -0.57% |
| 1 | EV_RBI_FEB27_HIKE25 ⇒ F_REPO_IN → LT | -2.00% | -0.54% |
| 2 | EV_LPG_COMPENSATION_CABINET ⇒ NEW_OMC_MARKETING_MARGIN → F_GOVT_CAPEX → LT | +0.84% | +0.50% |
| 1 | EV_CPI_BREACH_6PCT ⇒ F_REPO_IN → LT | -0.80% | -0.48% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → LT | +1.76% | +0.44% |
| 2 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → C_GCC → LT | -0.73% | -0.40% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_REPO_IN → LT | -2.00% | -0.36% |
| 2 | EV_HORMUZ_FULL_CLOSURE ⇒ C_MIDEAST_CONFLICT → C_GCC → LT | -7.00% | -0.35% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_GOVT_CAPEX → LT | +1.00 | events | +3.50% |
| 1 | F_REPO_IN → LT | +1.00 | events | -2.00% |
| 1 | P_DEFENCE_PROCUREMENT → LT | +1.00 | events | +1.20% |
| 1 | F_STEEL_INDIA → LT | +1.35 | events | -0.81% |
| 1 | F_US_TECH_SPEND → LT | -0.60 | events | -0.60% |
| 2 | F_GDP_IN → F_PRIVATE_CAPEX → LT | +0.50 | events | +0.30% |
| 1 | F_USDINR → LT | -0.37 | observed | -0.30% |
| 2 | F_GOVT_CAPEX → F_PRIVATE_CAPEX → LT | +1.00 | events | +0.24% |
| 2 | T_ENERGY_TRANSITION → F_PRIVATE_CAPEX → LT | +0.50 | events | +0.18% |
| 2 | F_CREDIT_SPREADS_IN → F_PRIVATE_CAPEX → LT | +0.50 | events | -0.18% |
| 2 | T_GENAI_SERVICES → T_DATA_CENTRES_IN → LT | +1.00 | events | +0.16% |
| 2 | F_REPO_IN → F_PRIVATE_CAPEX → LT | +1.00 | events | -0.10% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-12 | Large (>Rs10,000 cr) order announcements, Middle East/hydrocarbon/green hydrogen | other | 0.60 | +1.8% | +1.05% |
| 2027-01 | Q3 FY27 results (L&T typically reports ~20-25 Jan; estimate) | results | 0.97 | +0.0% | +0.00% |
| 2027-06 | Middle East escalation disrupting project sites or payments | other | 0.15 | -7.5% | -1.12% |

## Analyst profile (agent research, sourced)
# LT — Larsen & Toubro Ltd. (as of 2026-11-05)

*Facts from screener.in (pack through Sep 2026) and Google News headlines; bodies not retrieved. Order-book geography/segment shares and stake percentages are model knowledge/estimates. No expected-return number.*

## Business
L&T is India's largest engineering and construction group. Projects and Manufacturing (infrastructure, hydrocarbon, power, process, defence) is about 80% of revenue and about 40% of its order book is international, mainly the Middle East (model knowledge). It also owns about 69% of LTM and 66% of L&T Finance. Q2 FY27: revenue Rs 78,750 cr (+16%), attributable PAT Rs 5,202 cr (+33%, ET), order inflows +28% (Upstox).

## What moves the stock (ranked)
1. **Government and private capex (F_GOVT_CAPEX +3.5, F_PRIVATE_CAPEX +3.0 per +10%).**
2. **GCC growth and oil-funded capex (C_GCC +3.5; F_BRENT +0.8).**
3. **Rates and the multiple (F_REPO_IN -2.0 per 25bp).**
4. **Commodity inflation (steel -0.6 per +7%)** with most cost covered by price-variation clauses.
5. **Subsidiaries (LTM 0.12, LTF 0.08)** and secular themes (defence +1.2, data centres +1.0).

## Transmission examples
- **Middle East escalation (C_MIDEAST_CONFLICT) -> Brent up -> GCC fiscal receipts up -> more capex awards, but site risk.** Brent +10% (1st) -> Saudi/UAE/Qatar budgets rise (2nd) -> hydrocarbon and infrastructure awards to L&T up (3rd) -> order book and revenue +; against that, project delays and insurance cost (4th). Net sign positive for orders, negative for execution tail risk. Reuters (27 Oct) said the Q2 beat eased Middle East concerns.
- **Brent up -> INR down -> RBI tight -> private capex slows.** USD/INR 94.5 and a 5.50% repo (7 Oct hike) lift hurdle rates for private projects (3rd), lowering domestic process-industry orders (4th) while L&T's international USD revenue provides some hedge.
- **Budget capex step-up -> roads/rail/metro awards -> L&T order inflow -> revenue 12 months later.**
- **Steel price up -> contract costs** (price-variation protects 70%) -> small margin dip.
- **US tech spend down -> LTM revenue -> look-through value.**

## Current situation
Q2 (27 Oct): beat; PAT +33% (ET) and revenue +16%, shares +6% (Upstox) after losing 5% in the quarter despite a Rs 1.48 lakh cr inflow (23 Sep). Motilal Oswal sees 19% upside; JPMorgan has the highest target. It won a Rs 10-15k cr contract in October and more than Rs 15,000 cr in the Middle East in August.

## Upcoming
Q3 FY27 (~late Jan 2027); Union Budget 1 Feb 2027; large order announcements; RBI December policy.

## Bull case
Order inflows keep >20% growth, margins hold above 11%, Budget raises capex, GCC awards continue.

## Bear case
Middle East disruption, high rates delay private capex, working capital strain.

## Uncertainties
Order-book composition and margins not verified from filings; PAT definitions differ across publishers.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.