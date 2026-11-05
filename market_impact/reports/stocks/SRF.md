# SRF — SRF Ltd.
*MIDCAP_100 · Chemicals · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +1.9%**, **12 months +4.0%** (rank 48 / 43 of 200 for 3m / 12m); beta 0.84
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +21.7%): 3 months 57%, 12 months 65%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 +0.1% … P90 +8.4%; plausible 12m relative-return range incl. stock-specific noise: -14.2% … +25.0%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +1.8 pp (model impact +3.6% beta-adjusted vs realised market-adjusted move -11.8%); forward event exposure +6.2% (3m +3.1%; half assumed priced); company-specific events +0.5%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Global refrigerant gas prices (`NEW_REFRIGERANT_PRICES`) | +10% HFC/HFO refrigerant prices | +3.00 | +3.00 | +0.00 | +0.00 | +0.00 | — |
| China chemical/API dumping intensity (`F_CHINA_CHEM_EXPORTS`) | +15% export volumes / price cuts | -2.73 | -2.50 | -0.16 | -0.05 | -0.02 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -2.59 | +0.00 | -1.44 | -0.59 | -0.56 | — |
| Petrochemical / polymer spreads (`F_PETROCHEM_SPREADS`) | +10% polymer-naphtha spreads | +2.50 | +2.50 | +0.00 | +0.00 | +0.00 | — |
| China+1 manufacturing relocation to India (`T_CHINA_PLUS_ONE`) | +1 | +2.42 | +2.50 | -0.08 | +0.01 | -0.01 | — |
| Chemical feedstock (benzene, propylene, etc.) (`F_CHEM_FEEDSTOCK`) | +10% feedstock | -2.15 | -1.80 | -0.35 | +0.00 | +0.00 | — |
| Brent crude oil price (`F_BRENT`) | +10% Brent | -1.81 | -1.20 | -0.30 | -0.26 | -0.05 | +0.0% |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | +1.71 | +2.00 | -0.10 | -0.16 | -0.03 | -1.1% |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +1.43 | +0.00 | +0.98 | +0.47 | -0.02 | — |
| OPEC+ crude supply decisions (`NEW_OPEC_PLUS_SUPPLY`) | +1 mb/d OPEC+ production (quota/actual) | +1.42 | +0.00 | +0.77 | +0.36 | +0.30 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -1.41 | +0.00 | -0.98 | -0.45 | +0.03 | — |
| RBI repo rate (`F_REPO_IN`) | +25 bp repo | -1.40 | -1.20 | -0.15 | -0.04 | -0.01 | — |
| China growth / stimulus (`F_CHINA_GDP`) | +1 pp | +1.36 | +0.00 | +1.42 | +0.06 | -0.12 | — |
| Indian anti-dumping duties (chemicals, solar, others) (`P_ANTI_DUMPING_IN`) | +1 = new broad duties | +1.33 | +1.20 | +0.12 | +0.01 | +0.00 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -8.8% | -8.8% | -5.9 | -1.5 | -1.2 | -0.2 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -1.6% | -1.6% | +0.0 | -1.1 | -0.6 | +0.1 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.58 | +2.5% | +1.5% | +1.8 | +0.3 | +0.3 | +0.1 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.36 | -4.1% | -1.5% | -3.0 | -0.5 | -0.5 | -0.1 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -1.4% | -1.4% | -1.2 | -0.2 | -0.0 | -0.0 |
| US waives Russia-oil secondary sanctions/100% tariff threat on buyers incl. India (17 Oct) (`EV_RUSSIA_WAIVER_OCT17`) | occurred | 1.00 | +1.2% | +1.2% | +0.0 | +0.7 | +0.2 | +0.2 |
| China+1 momentum: Apple/Foxconn/Tata iPhone 18 Pro export ramp, India ~50% of US smartphone imports, PLI round 4 (textiles) and component schemes (`EV_CHINA_PLUS_ONE_ELECTRONICS`) | anticipated | 0.80 | +1.4% | +1.2% | +1.5 | -0.0 | +0.0 | -0.0 |
| US Q3 data: GDP 3.4%, CPI 3.7%, September payrolls only +29k (`EV_US_Q3_DATA_MIXED`) | occurred | 1.00 | -1.0% | -1.0% | +0.0 | -0.4 | -0.3 | -0.3 |
| US recession (two negative quarters or NBER-style) beginning by mid-2027 (`EV_US_RECESSION_RISK_2027`) | risk_scenario | 0.25 | +3.2% | +0.8% | +0.0 | +1.3 | +1.5 | +0.4 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | +0.7% | +0.7% | +0.0 | +0.9 | -0.1 | -0.1 |
| Finance ministry notifies anti-dumping duties on a meaningful batch of Chinese chemicals/APIs/others (`EV_INDIA_ADD_DUTIES_NOTIFIED_H1_2027`) | anticipated | 0.70 | +0.9% | +0.7% | +0.8 | +0.1 | +0.0 | +0.0 |
| Rupee at 95-96/USD and heavy RBI FX defence; reserves fall ~US$55bn from peak (`EV_RUPEE_DEFENCE_RESERVES_26`) | occurred | 1.00 | -0.6% | -0.6% | -0.7 | +0.0 | +0.1 | +0.0 |

## Strongest causal chains (1st–4th order)
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → SRF | -5.94% | -5.94% |
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_CHEM_FEEDSTOCK → SRF | -3.03% | -3.03% |
| 2 | EV_CPI_REACCEL_SEP26 ⇒ F_CPI_IN → F_REPO_IN → SRF | -1.59% | -1.59% |
| 2 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_USDINR → SRF | +1.56% | +1.56% |
| 1 | EV_CHINA_PLUS_ONE_ELECTRONICS ⇒ T_CHINA_PLUS_ONE → SRF | +1.50% | +1.20% |
| 1 | EV_RBI_OCT26_HIKE25 ⇒ F_REPO_IN → SRF | -1.20% | -1.20% |
| 3 | EV_IRAN_WAR_HORMUZ_OIL ⇒ F_BRENT → F_CHEM_FEEDSTOCK → F_PETROCHEM_SPREADS → SRF | -1.10% | -1.10% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → SRF | -3.00% | -1.07% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → SRF | +1.80% | +1.04% |
| 2 | EV_FPI_RECORD_OUTFLOW_26 ⇒ F_FPI_FLOWS → F_USDINR → SRF | +0.81% | +0.81% |
| 1 | EV_RUPEE_DEFENCE_RESERVES_26 ⇒ F_USDINR → SRF | -0.74% | -0.74% |
| 1 | EV_INDIA_ADD_DUTIES_NOTIFIED_H1_2027 ⇒ P_ANTI_DUMPING_IN → SRF | +0.84% | +0.59% |
| 2 | EV_RUSSIA_WAIVER_OCT17 ⇒ C_RUSSIA → F_BRENT → SRF | +0.58% | +0.58% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_USDINR → SRF | +2.60% | +0.57% |
| 3 | EV_RUSSIA_WAIVER_OCT17 ⇒ C_RUSSIA → F_BRENT → F_CHEM_FEEDSTOCK → SRF | +0.55% | +0.55% |

## Analyst profile (agent research, sourced)
# SRF — SRF Ltd. (as of 2026-11-05)

*Facts from screener.in (pack, through Sep 2026) and Google News headlines; article bodies not retrieved. Segment shares and cost shares are model estimates. No expected-return number.*

## Business
SRF makes fluorospecialty chemicals, refrigerant gases and agchem/pharma intermediates (Chemicals), BOPET/BOPP packaging films, nylon tyre cord and technical textiles, plus laminates and a new aluminium foil unit. Q2 FY27 sales were Rs 4,904 cr (+35% y/y), EBITDA Rs 946 cr (19.3%), PAT Rs 509 cr (+31%). The market cap is Rs 73,570 cr at P/E 31 and 4.8x book.

## What moves the stock (ranked)
1. **Feedstock cost with partial pass-through (F_CHEM_FEEDSTOCK -1.8, F_BRENT -1.2).**
2. **USD/INR (+2.0 per +3%)** for export mix.
3. **Chinese pricing (-2.5)** vs **China+1 awards (+2.5).**
4. **Refrigerant prices (+3.0) and film spreads (+2.5).**
5. **Rates (-1.2 per 25bp),** auto demand (+1.2), anti-dumping (+1.2).

## Transmission examples
- **Middle East escalation -> Brent -> PTA/MEG and nylon chips -> film and tyre-cord cost -> margins.** C_MIDEAST_CONFLICT -> Brent +10% (1st) -> polyester/nylon feed +5% (2nd) -> films/technical textiles cost +1.1% of sales; 60% passed after 1-2 quarters (3rd) -> segment EBIT dips and the stock re-rates lower (4th).
- **China oversupply in films/refrigerants -> price cuts -> SRF margin -> capex returns.** F_CHINA_CHEM_EXPORTS +15% -> film and refrigerant prices fall -> chemicals EBITDA -6% -> ROCE below the 14.6% base -> multiple de-rates.
- **Weaker rupee -> exports.** USD/INR +3% -> export revenue +1.3% -> net +0.66% of sales -> EBITDA +3.4% (50% hedged), but FPI outflows may offset the multiple.
- **RBI hike (7 Oct) -> auto and capex.** Slower auto volumes -> tyre cord; higher debt cost on capex.

## Current situation
Q2 (21 Oct): PAT +31% but margin at an eight-quarter low; the miss was in chemicals and non-fluoro businesses (NDTV Profit). Shares hit a 52-week low on 22 Oct (5th day of decline); Jefferies, Morgan Stanley and UBS stay cautious while HSBC (17 Sep) saw 33% upside. SRF plans a Rs 600 cr aluminium foil plant in MP.

## Upcoming
Q3 FY27 results (~Jan 2027); capex milestones; refrigerant pricing.

## Bull case
Chemicals mix recovers, foil and fluorospecialty add growth, rupee tailwind.

## Bear case
Chemicals margins stay compressed, Chinese pricing hits films and refrigerants, capex returns disappoint at 31x earnings.

## Uncertainties
Segment-level numbers and net debt not retrieved; conflicting broker views.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.