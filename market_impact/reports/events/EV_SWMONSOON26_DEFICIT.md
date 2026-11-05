# 2026 south-west monsoon ends 12.6% below normal (87% of LPA), driest since 2015 (`EV_SWMONSOON26_DEFICIT`)
*agri_rural · status occurred · date 2026-09-30 · P(3m) 1.0 · P(12m) 1.0 · confidence high*

IMD: June-Sept rainfall 759.4 mm vs 868.6 mm LPA (1971-2020), i.e. 87% of LPA / -12.6%. Lowest since 2015 (758.2 mm); fourth-lowest since 2001. Monthly: June 65% of normal, July ~101% (central India +33%), August 84%, September 92.4%. East and North-East India recorded its driest monsoon since 1901 (1,017.1 mm). 282 districts (38%) deficient; 15 states below normal; drought declared in parts of Maharashtra and Karnataka; South peninsula ~-23% by 28 Sep. IMD had forecast 92% of LPA (13 Apr) cut to 90% (29 May), so the aggregate was anticipated but June was far worse than forecast. Strong El Nino in progress (IMD 30 Sep: strong El Nino over equatorial Pacific, expected to strengthen through end-2026 and peak ~Nov); Indian Ocean Dipole neutral, i.e. no positive-IOD offset.

**Already moved:** Aggregate was forecast since April, so little index reaction; downstream moves: Indian sugar +27.8% since 1 Jun (global ICE raw sugar, factor_state), Nifty FMCG hit fresh 52-week low (Dalal Street Investment Journal, Oct 2026), India food CPI 7.74% in Sep from 5.52% in Jul.

## Entry shocks (conditional on the event)
- `F_MONSOON` Monsoon rainfall vs normal: -1.26 SSU (range -1.3…-1.2) Season total -12.6% vs LPA; SSU is +10% so -1.26 SSU.
- `F_POWER_DEMAND_IN` Indian electricity demand: 0.2 SSU (range 0.0…0.4) Deficient rain raises irrigation pumping and cooling load; small positive (low confidence).

## Causal chains (agent)
- order 2: EV_SWMONSOON26_DEFICIT → F_MONSOON → F_FOOD_INFLATION_IN — Lower kharif output (rice, pulses, oilseeds, vegetables) lifts food prices; see EV_FOOD_CPI_SEP26 for the realised level.
- order 3: EV_SWMONSOON26_DEFICIT → F_MONSOON → F_RURAL_DEMAND → F_AUTO_DEMAND_IN — Lower kharif income/volumes in rain-fed districts depress rural spend, then tractors, two-wheelers and entry cars.
- order 4: EV_SWMONSOON26_DEFICIT → F_MONSOON → F_FOOD_INFLATION_IN → F_CPI_IN → F_REPO_IN — Food-led CPI rise reinforces RBI calibrated tightening (repo 5.50% on 7 Oct 2026); higher policy rate hits rate-sensitives and NBFCs.
- order 3: EV_SWMONSOON26_DEFICIT → F_MONSOON → F_COTTON — Cotton, soybean, sugarcane acreage/yield damage tightens supply (cotton sowing -23% by 10 Jul).

## Most positively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| ADANIPOWER | +1.4 | +1.0 | +0.6 | -0.0 | -0.1 |
| COALINDIA | +0.9 | +0.6 | +0.1 | +0.2 | -0.0 |
| ENRIN | +0.6 | +0.6 | +0.1 | +0.1 | -0.3 |
| ULTRACEMCO | +0.4 | +0.6 | +0.0 | -0.1 | -0.1 |
| BHEL | +0.3 | +0.6 | +0.0 | -0.0 | -0.3 |
| PERSISTENT | +0.3 | +0.0 | +0.0 | +0.3 | +0.0 |
| WAAREEENER | +0.3 | +0.4 | +0.0 | +0.1 | -0.2 |
| TECHM | +0.3 | +0.0 | +0.0 | +0.3 | +0.0 |
| NATIONALUM | +0.3 | +0.0 | +0.1 | +0.0 | +0.1 |
| TCS | +0.3 | +0.0 | +0.0 | +0.2 | +0.0 |
| TATAPOWER | +0.2 | +0.3 | +0.4 | -0.1 | -0.4 |
| SUZLON | +0.2 | +0.3 | +0.0 | +0.2 | -0.3 |
| APARINDS | +0.2 | +0.0 | +0.2 | +0.1 | -0.1 |
| OIL | +0.2 | +0.0 | +0.0 | +0.0 | +0.1 |
| SOLARINDS | +0.2 | +0.2 | +0.0 | +0.2 | -0.2 |

## Most negatively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| INDUSINDBK | -6.9 | +0.0 | -2.6 | -3.1 | -1.2 |
| IDFCFIRSTB | -6.1 | +0.0 | -2.2 | -2.7 | -1.2 |
| YESBANK | -5.1 | +0.0 | -1.7 | -2.3 | -1.1 |
| M&MFIN | -5.1 | -3.1 | -0.7 | -0.8 | -0.4 |
| SHRIRAMFIN | -4.4 | -2.5 | -0.5 | -1.0 | -0.4 |
| AXISBANK | -3.9 | +0.0 | -1.2 | -1.8 | -0.8 |
| SBICARD | -3.8 | +0.0 | -1.9 | -1.3 | -0.6 |
| BANKINDIA | -3.7 | +0.0 | -1.3 | -2.1 | -0.4 |
| AUBANK | -3.7 | +0.0 | -1.1 | -1.8 | -0.8 |
| INDIANB | -3.5 | +0.0 | -1.2 | -1.7 | -0.6 |
| KOTAKBANK | -3.4 | +0.0 | -1.3 | -1.7 | -0.4 |
| FEDERALBNK | -3.4 | +0.0 | -0.3 | -2.2 | -0.9 |
| HDFCBANK | -3.4 | +0.0 | -1.1 | -1.6 | -0.7 |
| SBIN | -3.4 | +0.0 | -1.1 | -1.8 | -0.5 |
| BAJFINANCE | -3.4 | +0.0 | -0.7 | -1.4 | -1.3 |

Share of absolute impact by order: 1: 9%, 2: 30%, 3: 34%, 4: 27%

## Sources
- 2026-09-30 Southwest monsoon ends with 12% deficit - The Hindu https://www.thehindu.com/sci-tech/energy-and-environment/southwest-monsoon-ends-with-12-deficit/article71529423.ece
- 2026-09-30 2026 monsoon ends with nearly 13% rain deficit, worst since 2015: IMD - Business Standard https://www.business-standard.com/industry/agriculture/2026-monsoon-ends-with-nearly-13-rain-deficit-worst-since-2015-imd-126093001389_1.html
- 2026-09-30 India Today: monsoon ends 13% deficit, 282 districts deficient https://www.indiatoday.in/science/story/india-ends-monsoon-with-13-rainfall-deficit-receives-just-87-of-normal-rain-3006662-2026-09-30
- 2026-10-01 IMD 30 Sep: strong El Nino, neutral IOD https://www.indiatoday.in/science/story/el-nino-neutral-iod-india-rainfall-post-monsoon-3007171-2026-10-01