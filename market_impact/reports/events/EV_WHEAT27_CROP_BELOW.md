# India 2027 wheat crop (harvest Mar-Apr 2027) below 2026's record ~120 MT (`EV_WHEAT27_CROP_BELOW`)
*agri_rural · status anticipated · date 2027-04-15 · P(3m) 0.0 · P(12m) 0.65 · confidence low*

2025-26 wheat crop was a record ~120.6 MT (Bloomberg, Aug 2026). 2027 crop faces: wheat sown 0.19 vs 3.34 lakh ha at 30 Oct (full season ~336 lakh ha last year), poor soil moisture and low reservoirs, an El Nino winter with heat risk at grain fill. Recovery is possible if sowing accelerates in Nov (soil moisture, mid-Nov cooler weather) and if irrigation holds in Punjab/Haryana/UP (canal-irrigated, groundwater-fed, not rain-dependent). I put 65% on 2027 output below 2026 (central estimate 108-116 MT) and 25% on a fall >8%. Central Pool stocks (925.85 LMT on 1 Jul) cushion availability so the effect is mainly sentiment/price, not scarcity. Government rabi target 177.72 MT.

## Entry shocks (conditional on the event)
- `F_WHEAT` Wheat price: 0.5 SSU (range 0.0…1.2) Conditional on a shortfall: global wheat (+10% SSU) tailwind via lost Indian exports; domestic flour up.
- `F_FOOD_INFLATION_IN` India food inflation: 0.4 SSU (range 0.1…0.9) Cereal, atta and gram inflation Apr-Jun 2027 (SSU +2pp).
- `F_RURAL_DEMAND` Rural consumption growth: -0.2 SSU (range -0.4…0.0) Lower wheat marketed surplus in north India; offset by higher prices.

## Causal chains (agent)
- order 2: EV_WHEAT27_CROP_BELOW → F_WHEAT → F_FOOD_INFLATION_IN — Cereals about 9% of CPI; government can release FCI stock (OMSS) and curb exports, limiting the price rise.
- order 3: EV_WHEAT27_CROP_BELOW → F_FOOD_INFLATION_IN → F_CPI_IN → F_REPO_IN — Keeps CPI >5.5% into Q1 FY28.
- order 4: EV_WHEAT27_CROP_BELOW → F_WHEAT → P_FERT_SUBSIDY — Not a main channel; government may extend free grain, lifting food-subsidy bill.

## Most positively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| NATIONALUM | +0.1 | +0.0 | +0.0 | +0.1 | +0.0 |
| OIL | +0.1 | +0.0 | +0.0 | +0.1 | +0.0 |
| HINDCOPPER | +0.1 | +0.0 | +0.0 | +0.1 | -0.0 |
| NMDC | +0.1 | +0.0 | +0.0 | +0.1 | +0.0 |
| VAML | +0.1 | +0.0 | +0.0 | +0.1 | -0.0 |
| DMART | +0.0 | +0.3 | +0.0 | -0.2 | -0.1 |
| UPL | +0.0 | +0.0 | +0.0 | +0.0 | -0.0 |
| DRREDDY | +0.0 | +0.0 | +0.0 | +0.0 | -0.0 |
| HINDZINC | +0.0 | +0.0 | +0.0 | +0.0 | -0.0 |
| ONGC | +0.0 | +0.0 | -0.0 | +0.1 | -0.0 |
| LUPIN | +0.0 | +0.0 | +0.0 | +0.0 | -0.0 |
| COCHINSHIP | +0.0 | +0.0 | +0.0 | +0.0 | -0.0 |
| SUNPHARMA | -0.0 | +0.0 | +0.0 | +0.0 | -0.0 |
| HCLTECH | -0.0 | +0.0 | +0.0 | +0.0 | -0.0 |
| GLENMARK | -0.0 | +0.0 | +0.0 | -0.0 | -0.0 |

## Most negatively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| INDUSINDBK | -2.1 | +0.0 | -1.2 | -0.8 | -0.1 |
| YESBANK | -2.1 | +0.0 | -0.9 | -1.1 | -0.2 |
| IDFCFIRSTB | -2.0 | +0.0 | -1.1 | -0.9 | -0.1 |
| M&MFIN | -1.6 | -0.8 | -0.2 | -0.4 | -0.2 |
| AUBANK | -1.5 | -0.4 | -0.3 | -0.7 | -0.1 |
| TATACAP | -1.5 | +0.0 | -0.4 | -0.9 | -0.2 |
| LTF | -1.5 | -0.6 | -0.2 | -0.5 | -0.1 |
| SHRIRAMFIN | -1.4 | +0.0 | -0.8 | -0.4 | -0.3 |
| BAJFINANCE | -1.4 | +0.0 | -0.3 | -0.9 | -0.1 |
| AXISBANK | -1.4 | +0.0 | -0.7 | -0.6 | -0.1 |
| TMCV | -1.3 | +0.0 | -1.0 | -0.1 | -0.2 |
| VMM | -1.3 | -1.2 | +0.0 | -0.1 | -0.0 |
| INDIANB | -1.2 | +0.0 | -0.7 | -0.4 | -0.1 |
| SBIN | -1.2 | +0.0 | -0.8 | -0.3 | -0.1 |
| MEESHO | -1.2 | -0.8 | +0.0 | -0.4 | -0.0 |

Share of absolute impact by order: 1: 15%, 2: 30%, 3: 43%, 4: 13%

## Sources
- 2026-11-03 Wheat sowing 0.19 vs 3.34 lakh ha https://www.businesstoday.in/latest/economy/story/indias-rabi-sowing-falls-46-to-37-56-lakh-hectares-wheat-acreage-plunges-94-565374-2026-11-03
- 2026-08-24 Wheat record 120.6 MT; record stocks https://www.deccanchronicle.com/business/economics/govt-lifts-export-ban-on-wheat-and-its-products-1981807