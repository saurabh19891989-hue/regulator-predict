# Rabi sowing sharply behind: 37.56 lakh ha vs 69.02 lakh ha a year ago; wheat 0.19 lakh ha vs 3.34 (`EV_RABI_SOWING_LAG26`)
*agri_rural · status occurred · date 2026-11-03 · P(3m) 1.0 · P(12m) 1.0 · confidence high*

Agriculture Ministry data as of 30 Oct 2026 (Business Today, 3 Nov): total rabi area 37.56 lakh ha (-45.6%); wheat 0.19 vs 3.34 lakh ha; pulses 9.45 vs 19.56 (gram 5.90 vs 14.35); oilseeds 20.97 vs 38.62 (rapeseed-mustard 20.50 vs 38.07); coarse cereals 3.78 vs 4.22. Causes: inadequate soil moisture, high daytime temperature, limited irrigation/canal water. Wheat is normally sown Oct-Nov (full season 336 lakh ha in 2025-26) so the lag is recoverable until about 15 Dec, but the sowing window and soil-moisture constraints are real. Government's rabi target is 177.72 MT. Business Standard (24 Oct) had expected wheat acreage steady; actual early data weaker. Rajasthan sowing delayed (BS, 2 Nov).

**Already moved:** Wheat (CBOT proxy) -14.7% 1m (factor_state), mostly the global Black-Sea/export-ban context; domestic prices not yet moved on sowing news (not verified).

## Entry shocks (conditional on the event)
- `F_WHEAT` Wheat price: 0.2 SSU (range -0.2…0.8) Early sowing lag adds a small risk premium; global wheat already -1.3% since 1 Jun.
- `F_FOOD_INFLATION_IN` India food inflation: 0.3 SSU (range 0.0…0.6) Forward cereal/pulses/mustard price pressure if the lag is not made up.

## Causal chains (agent)
- order 2: EV_RABI_SOWING_LAG26 → F_WHEAT → F_FOOD_INFLATION_IN — Lower 2027 wheat/pulses/mustard crops lift cereal, pulses and edible-oil prices from Mar 2027.
- order 3: EV_RABI_SOWING_LAG26 → F_FOOD_INFLATION_IN → F_CPI_IN → F_REPO_IN — Spring CPI stays high, prolonging the hiking bias.
- order 3: EV_RABI_SOWING_LAG26 → F_EDIBLE_OIL → F_FOOD_INFLATION_IN — Mustard acreage halving raises edible-oil import needs in FY28.

## Most positively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| DMART | +0.1 | +0.2 | +0.0 | -0.1 | -0.0 |
| NATIONALUM | +0.0 | +0.0 | +0.0 | +0.1 | -0.0 |
| OIL | +0.0 | +0.0 | +0.0 | +0.1 | -0.0 |
| HINDCOPPER | +0.0 | +0.0 | +0.0 | +0.1 | -0.0 |
| PIIND | +0.0 | +0.0 | -0.0 | +0.1 | -0.0 |
| ONGC | +0.0 | +0.0 | +0.0 | +0.0 | -0.0 |
| UPL | +0.0 | +0.0 | +0.0 | +0.0 | -0.0 |
| LUPIN | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| MCX | +0.0 | +0.0 | +0.0 | +0.0 | -0.0 |
| NMDC | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| DRREDDY | +0.0 | +0.0 | +0.0 | +0.0 | -0.0 |
| VAML | -0.0 | +0.0 | +0.0 | +0.1 | -0.1 |
| HINDZINC | -0.0 | +0.0 | +0.0 | +0.0 | -0.0 |
| SUNPHARMA | -0.0 | +0.0 | +0.0 | +0.0 | -0.0 |
| LTM | -0.0 | +0.0 | +0.0 | +0.0 | -0.1 |

## Most negatively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| YESBANK | -1.0 | +0.0 | +0.0 | -0.7 | -0.3 |
| TATACAP | -0.8 | +0.0 | +0.0 | -0.5 | -0.3 |
| BAJFINANCE | -0.8 | +0.0 | +0.0 | -0.6 | -0.2 |
| AUBANK | -0.7 | +0.0 | -0.0 | -0.4 | -0.2 |
| IDFCFIRSTB | -0.7 | +0.0 | +0.0 | -0.5 | -0.2 |
| IREDA | -0.6 | +0.0 | +0.0 | -0.4 | -0.2 |
| PRESTIGE | -0.6 | +0.0 | +0.0 | -0.4 | -0.2 |
| INDUSINDBK | -0.6 | +0.0 | +0.0 | -0.4 | -0.2 |
| BAJAJFINSV | -0.6 | +0.0 | +0.0 | -0.4 | -0.2 |
| LTF | -0.6 | +0.0 | -0.1 | -0.4 | -0.1 |
| SHRIRAMFIN | -0.5 | +0.0 | +0.0 | -0.3 | -0.3 |
| M&MFIN | -0.5 | +0.0 | -0.1 | -0.3 | -0.1 |
| JSWENERGY | -0.5 | +0.0 | +0.0 | -0.4 | -0.1 |
| AXISBANK | -0.5 | +0.0 | +0.0 | -0.3 | -0.2 |
| VMM | -0.5 | -0.4 | -0.0 | -0.0 | +0.0 |

Share of absolute impact by order: 1: 5%, 2: 6%, 3: 61%, 4: 28%

## Sources
- 2026-11-03 Rabi sowing falls 46%; wheat 0.19 lakh ha - Business Today https://www.businesstoday.in/latest/economy/story/indias-rabi-sowing-falls-46-to-37-56-lakh-hectares-wheat-acreage-plunges-94-565374-2026-11-03