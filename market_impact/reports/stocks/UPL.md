# UPL — UPL Ltd.
*MIDCAP_100 · Chemicals · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +0.3%**, **12 months +1.7%** (rank 76 / 26 of 200 for 3m / 12m); beta 1.05
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +25.4%): 3 months 51%, 12 months 53%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -1.6% … P90 +7.4%; plausible 12m relative-return range incl. stock-specific noise: -29.5% … +35.9%
- Decomposition (12m): 0.5 × forward event exposure +1.9% (3m +0.8%; half assumed priced; market-priced macro drift removed) + 0.5 × company-specific catalysts +2.0%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply +2.1% (beta-adjusted) vs a realised market-adjusted move of -23.4% — gap +25.6 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Global agrochemical prices and channel destocking (`NEW_AGROCHEM_PRICES_GLOBAL`) | +10% global agchem active prices / volumes | +8.00 | +8.00 | +0.00 | +0.00 | +0.00 | — |
| China chemical/API dumping intensity (`F_CHINA_CHEM_EXPORTS`) | +15% export volumes / price cuts | -3.04 | -3.00 | +0.00 | -0.04 | +0.00 | — |
| US–China trade decoupling (`C_US_CHINA_DECOUPLING`) | +1 = more decoupling | -1.74 | +0.00 | -1.20 | -0.53 | -0.01 | — |
| Palm / edible oil price (`F_EDIBLE_OIL`) | +10% edible oils | +1.51 | +1.50 | +0.00 | +0.00 | +0.01 | +1.9% |
| Africa & Latin America demand (`C_AFRICA_LATAM`) | +1 pp growth | +1.50 | +1.50 | +0.00 | +0.00 | +0.00 | — |
| Chemical feedstock (benzene, propylene, etc.) (`F_CHEM_FEEDSTOCK`) | +10% feedstock | -1.20 | -1.20 | +0.00 | +0.00 | +0.00 | — |
| China growth / stimulus (`F_CHINA_GDP`) | +1 pp | +1.01 | +0.00 | +0.96 | +0.02 | +0.03 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | +1.00 | +1.00 | +0.00 | +0.00 | +0.00 | -1.1% |
| US Fed funds rate (`F_FED_FUNDS`) | +25 bp | -1.00 | -1.00 | +0.00 | +0.00 | +0.00 | +11.2% |
| US growth (`F_US_GDP`) | +1 pp | -0.80 | +0.00 | -0.64 | -0.12 | -0.04 | — |
| Monsoon rainfall vs normal (`F_MONSOON`) | +10% above long-period average | +0.77 | +0.80 | +0.00 | +0.00 | -0.03 | — |
| USD/CNY (`F_USDCNY`) | +3% USD/CNY (yuan weaker) | -0.63 | +0.00 | -0.62 | +0.00 | -0.01 | -1.4% |
| US average effective tariff rate (all partners) (`NEW_US_TARIFF_GLOBAL`) | +5 pp effective tariff rate | -0.57 | +0.00 | -0.16 | -0.26 | -0.15 | — |
| Indian anti-dumping duties (chemicals, solar, others) (`P_ANTI_DUMPING_IN`) | +1 = new broad duties | +0.48 | +0.00 | +0.48 | +0.00 | +0.00 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -1.1% | -1.1% | -1.0 | -0.1 | -0.0 | -0.0 |
| 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`) | occurred | 1.00 | -1.0% | -1.0% | -1.0 | +0.0 | +0.0 | +0.0 |
| US recession (two negative quarters or NBER-style) beginning by mid-2027 (`EV_US_RECESSION_RISK_2027`) | risk_scenario | 0.25 | +3.6% | +0.9% | +3.0 | +0.0 | +0.5 | +0.0 |
| FOMC 8-9 Dec 2026: 25 bp hike to 4.00-4.25% (`EV_FED_DEC26_HIKE25`) | scheduled | 0.72 | -1.1% | -0.8% | -1.0 | -0.1 | -0.0 | +0.0 |
| US Q3 data: GDP 3.4%, CPI 3.7%, September payrolls only +29k (`EV_US_Q3_DATA_MIXED`) | occurred | 1.00 | -0.7% | -0.7% | -0.5 | +0.0 | -0.1 | -0.0 |
| China Q3 GDP +4.5% (beat); property 'mini-stimulus' of late September; PMI 49.3; LPR unchanged (`EV_CHINA_Q3_GDP_AND_MINI_STIMULUS`) | occurred | 1.00 | +0.6% | +0.6% | +0.0 | +0.6 | -0.0 | +0.0 |
| IMD April 2027 long-range forecast says normal or above-normal monsoon (>=96% LPA) (`EV_MONSOON27_FIRST_FORECAST_NORMAL`) | scheduled | 0.68 | +0.8% | +0.5% | +0.8 | +0.0 | -0.0 | -0.0 |
| Fed hikes >=50 bp cumulative beyond Oct level by Apr 2027 (`EV_FED_H1_2027_FURTHER_HIKES`) | anticipated | 0.40 | -1.1% | -0.4% | -1.0 | -0.1 | -0.0 | +0.0 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | +0.4% | +0.4% | +0.0 | +0.4 | +0.0 | +0.0 |
| China Dec CEWC / Mar 2027 NPC delivers large fiscal stimulus and consumption push (`EV_CHINA_NPC_MAR27_BIG_STIMULUS`) | anticipated | 0.35 | +1.1% | +0.4% | +0.0 | +1.1 | -0.1 | +0.0 |
| Rupee at 95-96/USD and heavy RBI FX defence; reserves fall ~US$55bn from peak (`EV_RUPEE_DEFENCE_RESERVES_26`) | occurred | 1.00 | -0.4% | -0.4% | -0.4 | +0.0 | +0.0 | +0.0 |
| US-China trade truce (expires 10 Jan 2027) extended or upgraded to a bigger deal (`EV_US_CHINA_TRUCE_EXTENDED`) | scheduled | 0.72 | +0.5% | +0.4% | +0.0 | +0.3 | +0.2 | -0.0 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_US_RECESSION_RISK_2027 ⇒ F_FED_FUNDS → UPL | +3.00% | +0.75% |
| 1 | EV_FED_DEC26_HIKE25 ⇒ F_FED_FUNDS → UPL | -1.00% | -0.72% |
| 2 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → F_CHEM_FEEDSTOCK → UPL | +1.06% | +0.58% |
| 1 | EV_MONSOON27_FIRST_FORECAST_NORMAL ⇒ F_MONSOON → UPL | +0.80% | +0.54% |
| 2 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_BRENT → F_CHEM_FEEDSTOCK → UPL | -1.80% | -0.45% |
| 1 | EV_FED_H1_2027_FURTHER_HIKES ⇒ F_FED_FUNDS → UPL | -1.00% | -0.40% |
| 2 | EV_INDIA_ADD_DUTIES_NOTIFIED_H1_2027 ⇒ P_ANTI_DUMPING_IN → F_CHINA_CHEM_EXPORTS → UPL | +0.50% | +0.35% |
| 1 | EV_NEMONSOON26_NORMAL_UP ⇒ F_MONSOON → UPL | +0.40% | +0.34% |
| 2 | EV_CHINA_NPC_MAR27_BIG_STIMULUS ⇒ F_CHINA_GDP → F_CHINA_CHEM_EXPORTS → UPL | +0.96% | +0.34% |
| 2 | EV_US_CHINA_TRUCE_EXTENDED ⇒ C_US_CHINA_DECOUPLING → F_CHINA_CHEM_EXPORTS → UPL | +0.36% | +0.26% |
| 1 | EV_MONSOON27_DEFICIT_FORECAST ⇒ F_MONSOON → UPL | -0.80% | -0.26% |
| 2 | EV_RARE_EARTH_CONTROLS_REIMPOSED ⇒ C_US_CHINA_DECOUPLING → F_CHINA_CHEM_EXPORTS → UPL | -0.96% | -0.24% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_USDINR → UPL | +1.30% | +0.23% |
| 2 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → F_USDINR → UPL | -0.46% | -0.23% |
| 2 | EV_HORMUZ_FULL_CLOSURE ⇒ F_BRENT → F_CHEM_FEEDSTOCK → UPL | -3.67% | -0.18% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_FED_FUNDS → UPL | +1.62 | observed | -1.62% |
| 1 | F_MONSOON → UPL | -1.56 | events | -1.25% |
| 1 | F_USDINR → UPL | -0.37 | observed | -0.37% |
| 2 | F_USDCNY → F_CHINA_CHEM_EXPORTS → UPL | -0.47 | observed | +0.34% |
| 2 | F_CHINA_GDP → F_CHINA_CHEM_EXPORTS → UPL | +0.30 | events | +0.29% |
| 2 | P_ANTI_DUMPING_IN → F_CHINA_CHEM_EXPORTS → UPL | +0.40 | events | +0.29% |
| 1 | F_EDIBLE_OIL → UPL | +0.19 | observed | +0.28% |
| 2 | F_DXY → C_AFRICA_LATAM → UPL | +0.74 | observed | -0.27% |
| 1 | P_US_TARIFF_INDIA → UPL | -0.60 | events | +0.24% |
| 2 | C_US_CHINA_DECOUPLING → F_CHINA_CHEM_EXPORTS → UPL | -0.10 | events | +0.12% |
| 2 | P_ANTI_DUMPING_IN → F_CHEM_FEEDSTOCK → UPL | +0.40 | events | -0.10% |
| 2 | F_BRENT → F_CHEM_FEEDSTOCK → UPL | +0.00 | observed | -0.00% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2027-02 | Q3 FY27 results (estimate) | results | 0.97 | +0.0% | +0.00% |
| 2027-03 | Net-debt reduction targets / refinancing and rating actions | other | 0.50 | +1.0% | +0.50% |
| 2027-06 | Advanta Enterprises IPO / partial listing (status unverified after mid-2026) | corporate_action | 0.25 | +6.0% | +1.50% |

## Analyst profile (agent research, sourced)
# UPL — UPL Ltd. (as of 2026-11-05)

*Facts from screener.in (evidence pack through Sep 2026) and Google News headlines; bodies not retrieved. Model knowledge is labelled. No expected-return number.*

## Business
UPL is a global agrochemical and seeds group: roughly 80% of sales outside India (model knowledge), led by Latin America. Q2 FY27 sales were Rs 11,860 cr, operating profit Rs 2,068 cr (17.4%), PAT Rs 452 cr. Interest cost of about Rs 3,300 cr a year makes the equity a levered claim on agchem pricing: market cap Rs 44,238 cr versus likely net debt in the Rs 25,000 cr range (estimate; not retrieved).

## What moves the stock (ranked)
1. **Global agchem prices and destocking (NEW_AGROCHEM_PRICES_GLOBAL +8 per +10%)** amplified by leverage.
2. **China generic price pressure (-3.0).**
3. **Farm income in LatAm/US (F_EDIBLE_OIL soy proxy +1.5; C_AFRICA_LATAM +1.5).**
4. **Rates (F_FED_FUNDS -1.0 per 25bp), feedstock (-1.2), FX (+1.0), monsoon (+0.8).**

## Transmission examples
- **US/China trade friction -> Chinese generic exports to India/Brazil -> price fall -> UPL margin.** F_CHINA_CHEM_EXPORTS +15% -> active prices -4% -> channel price cuts (2nd) -> UPL EBITDA -9% on 40% of portfolio (3rd) -> leverage cuts equity -5% and refinancing costs rise (4th).
- **Fed hike -> USD strength -> BRL weak -> Brazilian farmer credit -> UPL volumes.** F_FED_FUNDS up -> BRL falls (1st) -> imported input costs for Brazilian farmers rise, credit tightens (2nd) -> distributor receivables stretch (3rd) -> UPL provisions and working capital rise (4th).
- **Soy price rise -> farmer income -> crop-protection spend.** F_EDIBLE_OIL +10% -> Brazil/US acreage and spend up -> UPL volume +3% -> EBITDA +6% -> equity +3 (leveraged).
- **Brent up -> solvents -> margins** with limited pass-through (-1.2 per +10%).

## Current situation
Q2 (2 Nov): EBITDA +5% y/y, margin expansion for the eighth quarter in a row, PAT down 24-26% on lower sales and higher interest/costs. Kotak Neo upgraded to Add (13 Oct) citing speciality chemicals; stock +5% on 16 Oct; touched a 52-week low in early Oct. Sector read-across: PIIND collapsed on 5 Nov.

## Upcoming
Q3 FY27 (~Feb 2027); Advanta listing decision; deleveraging; FX.

## Bull case
Margins keep expanding, destocking ends, Advanta unlocks value, deleveraging.

## Bear case
Generic prices fall further, BRL stress, leverage becomes a refinancing issue.

## Uncertainties
Net debt, segment shares and the Advanta timeline are unverified; PAT definitions vary across publishers.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.