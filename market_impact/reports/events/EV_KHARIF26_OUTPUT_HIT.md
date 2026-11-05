# Kharif 2026 output hit: paddy area down, foodgrain target cut, rice output seen sharpest fall in ~2 decades (`EV_KHARIF26_OUTPUT_HIT`)
*agri_rural · status occurred · date 2026-09-29 · P(3m) 1.0 · P(12m) 1.0 · confidence medium*

Agriculture Ministry (29 Sep) set a 2026-27 foodgrain target of 373.93 MT vs 376.56 MT estimated for 2025-26 (-0.7%), with a rabi target of 177.72 MT vs 174.51 MT actual; a first (kharif) advance estimate is not yet published (usually Sept-Oct; not found). Kharif acreage reached 1,056.7 lakh ha by 25 Aug (record-ish headline) but paddy area was ~4% lower in mid-Sep (about 1.7 mn ha less than a year ago: Karnataka -454k ha, Telangana -446k, AP -190k, MP -175k, TN -140k, Maharashtra -115k). Reuters (17 Sep): India rice output faces the biggest drop in two decades, though FCI stocks cushion exports (article behind paywall; magnitude not verified). Central Pool grain stocks 925.85 LMT on 1 Jul 2026 vs buffer norm 411.2 LMT (Business Today 8 Oct).

**Already moved:** Domestic rice export price pressure: broken-rice export quotes crossed US$360/t in early Nov (IREF, 3 Nov). F_SUGAR (global) +27.8% since 1 Jun. Corn output estimates cut (Global Agriculture, 15 Sep).

## Entry shocks (conditional on the event)
- `F_RICE` Rice price: 0.6 SSU (range 0.2…1.2) Global/Indian rice export prices (+10% SSU): broken rice >$360/t but ample FCI stock caps the rise.
- `F_FOOD_INFLATION_IN` India food inflation: 0.5 SSU (range 0.2…0.9) Kharif shortfall component of the food-price rise (realised level in EV_FOOD_CPI_SEP26).

## Causal chains (agent)
- order 2: EV_KHARIF26_OUTPUT_HIT → F_RICE → F_FOOD_INFLATION_IN — Rice and pulses are large in the CPI food basket; FCI open-market sales partly offset.
- order 3: EV_KHARIF26_OUTPUT_HIT → F_FOOD_INFLATION_IN → F_CPI_IN → F_REPO_IN — Higher CPI pushes RBI to a further hike.
- order 3: EV_KHARIF26_OUTPUT_HIT → F_RICE → P_SUGAR_ETHANOL → F_SUGAR — Grain-based ethanol demand (broken rice, FCI rice) competes with food/feed, tightening rice supply.

## Most positively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| DMART | +0.1 | +0.4 | +0.0 | -0.2 | -0.1 |
| NATIONALUM | +0.1 | +0.0 | +0.0 | +0.1 | -0.0 |
| OIL | +0.1 | +0.0 | +0.0 | +0.1 | -0.0 |
| HINDCOPPER | +0.1 | +0.0 | +0.0 | +0.1 | -0.0 |
| PIIND | +0.1 | +0.0 | -0.0 | +0.1 | -0.0 |
| UPL | +0.0 | +0.0 | +0.0 | +0.1 | -0.0 |
| ONGC | +0.0 | +0.0 | +0.0 | +0.1 | -0.0 |
| LUPIN | +0.0 | +0.0 | +0.0 | +0.0 | -0.0 |
| MCX | +0.0 | +0.0 | +0.0 | +0.1 | -0.0 |
| NMDC | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| DRREDDY | +0.0 | +0.0 | +0.0 | +0.0 | -0.0 |
| VAML | -0.0 | +0.0 | +0.0 | +0.1 | -0.1 |
| HINDZINC | -0.0 | +0.0 | +0.0 | +0.1 | -0.1 |
| SUNPHARMA | -0.0 | +0.0 | +0.0 | +0.0 | -0.1 |
| LTM | -0.0 | +0.0 | +0.0 | +0.1 | -0.1 |

## Most negatively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| RADICO | -2.0 | -1.8 | +0.1 | -0.4 | +0.0 |
| YESBANK | -1.2 | +0.0 | +0.0 | -0.8 | -0.4 |
| IDFCFIRSTB | -1.1 | +0.0 | +0.0 | -0.8 | -0.3 |
| IREDA | -1.1 | +0.0 | +0.0 | -0.7 | -0.4 |
| TATACAP | -1.0 | +0.0 | +0.0 | -0.6 | -0.4 |
| BAJFINANCE | -1.0 | +0.0 | +0.0 | -0.8 | -0.2 |
| INDUSINDBK | -1.0 | +0.0 | +0.0 | -0.6 | -0.4 |
| AUBANK | -1.0 | +0.0 | -0.1 | -0.6 | -0.3 |
| LTF | -0.9 | +0.0 | -0.1 | -0.6 | -0.2 |
| SHRIRAMFIN | -0.9 | +0.0 | +0.0 | -0.5 | -0.5 |
| M&MFIN | -0.9 | +0.0 | -0.2 | -0.5 | -0.2 |
| JSWENERGY | -0.9 | +0.0 | +0.0 | -0.7 | -0.2 |
| AXISBANK | -0.9 | +0.0 | +0.0 | -0.5 | -0.3 |
| VMM | -0.8 | -0.8 | -0.1 | -0.1 | +0.0 |
| GODREJPROP | -0.8 | +0.0 | +0.0 | -0.6 | -0.2 |

Share of absolute impact by order: 1: 7%, 2: 6%, 3: 59%, 4: 29%

## Sources
- 2026-09-29 Foodgrain output estimate for 2026-27 reduced marginally - Financial Express https://www.financialexpress.com/policy/economy-foodgrain-output-estimate-for-2026-27-reduced-marginally-4349877/
- 2026-09-30 DTE: lower food production target, paddy area down ~1.7 mn ha https://www.downtoearth.org.in/agriculture/india-sets-lower-food-production-target-for-2026-27-as-el-ni%C3%B1o-clouds-rabi-season
- 2026-09-17 Reuters: rice output biggest drop in two decades (headline only) https://www.reuters.com/world/india/india-rice-output-faces-biggest-drop-two-decades-stocks-cushion-exports-2026-09-17/
- 2026-10-08 Central Pool 925.85 LMT on 1 Jul vs norm 411.2 LMT https://www.businesstoday.in/latest/economy/story/global-food-security-faces-fresh-risks-but-indias-grain-buffer-offers-a-cushion-560357-2026-10-08