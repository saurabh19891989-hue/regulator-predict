# Food inflation overshoot: Dec-Feb CPI food >9% y/y on pulses, vegetables, edible oils, milk (`EV_PULSES_VEG_SPIKE_WINTER`)
*agri_rural · status risk_scenario · date 2027-01-15 · P(3m) 0.15 · P(12m) 0.25 · confidence low*

Sept food CPI 7.74% and rising; rabi pulses (gram -59%, lentil -49% sown area at 30 Oct), mustard acreage halved, weak reservoirs, El Nino heat risk and milk/ghee price hikes (Nandini +Rs 8/l; Amul ghee/butter +Rs 40/l) could push food inflation above 9%. Government tools: FCI OMSS (grain), duty cuts (edible oil, pulses), stock limits, export curbs. Probability 15% by Feb 2027 print window, 25% by Mar 2027.

**Review override applied:** Unclamped, the CPI +1pp entry propagates through CPI->REPO (0.72 SSU after RT_BACKBONE's x0.5) and GDP->REPO into an implied hike of ~18-20bp. The result is -4.7% conditional for BAJFINANCE and -5.4% for YESBANK. A supply-led winter vegetable/pulse spike is the case the RBI looks through, and the 2026 episode (CPI 2.8% -> 5.5%) drew one 25bp hike. The Feb/Apr MPC odds already carry part of this risk. Clamp F_REPO_IN at +0.3 SSU (~7bp). Prob unchanged.

## Entry shocks (conditional on the event)
- `F_FOOD_INFLATION_IN` India food inflation: 1.2 SSU (range 0.8…1.8) unchanged
- `F_CPI_IN` India CPI inflation: 1.0 SSU (range 0.7…1.4) unchanged
- `F_REPO_IN` RBI repo rate: 0.3 SSU (range 0.0…0.8) clamped: RBI looks through supply-led food spikes (2026: CPI 2.8%->5.5% met by one 25bp hike); Feb/Apr MPC odds already carry part of this risk

## Causal chains (agent)
- order 2: EV_PULSES_VEG_SPIKE_WINTER → F_FOOD_INFLATION_IN → F_CPI_IN — Headline above the 6% ceiling for 2+ quarters.
- order 3: EV_PULSES_VEG_SPIKE_WINTER → F_CPI_IN → F_REPO_IN → F_GSEC_10Y_IN — MPC delivers 50-75 bp cumulative hikes.
- order 4: EV_PULSES_VEG_SPIKE_WINTER → F_REPO_IN → F_CREDIT_GROWTH_IN — Credit growth slows, hurting NBFC/banks and housing.

## Most positively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| NATIONALUM | +0.4 | -0.1 | +0.6 | -0.0 | +0.0 |
| OIL | +0.4 | -0.1 | +0.6 | -0.0 | +0.0 |
| ONGC | +0.4 | -0.2 | +0.6 | -0.0 | +0.0 |
| HINDCOPPER | +0.4 | -0.1 | +0.6 | -0.0 | -0.0 |
| PIIND | +0.3 | +0.0 | +0.2 | +0.1 | +0.0 |
| DRREDDY | +0.3 | -0.2 | +0.5 | +0.0 | -0.0 |
| LUPIN | +0.3 | -0.1 | +0.4 | +0.1 | -0.0 |
| NMDC | +0.2 | -0.2 | +0.4 | +0.0 | -0.0 |
| JSWSTEEL | +0.2 | -0.4 | +0.5 | -0.0 | +0.1 |
| UPL | +0.2 | +0.0 | +0.2 | -0.0 | +0.0 |
| VAML | +0.1 | +0.0 | +0.2 | -0.1 | +0.0 |
| HINDALCO | +0.1 | -0.2 | +0.3 | -0.2 | +0.1 |
| MCX | +0.1 | +0.0 | +0.2 | -0.0 | -0.1 |
| TATASTEEL | +0.1 | -0.3 | +0.3 | +0.0 | +0.1 |
| HINDZINC | +0.1 | +0.0 | +0.1 | -0.0 | +0.0 |

## Most negatively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| YESBANK | -3.3 | -0.4 | -1.8 | -1.0 | -0.0 |
| PAGEIND | -2.9 | -1.2 | -1.7 | +0.0 | -0.1 |
| IDFCFIRSTB | -2.9 | -0.3 | -1.9 | -0.8 | +0.0 |
| IREDA | -2.9 | -0.8 | -1.2 | -0.7 | -0.2 |
| TATACAP | -2.8 | -0.4 | -1.6 | -0.6 | -0.2 |
| BAJFINANCE | -2.8 | -0.4 | -2.2 | -0.1 | -0.2 |
| AUBANK | -2.6 | -0.4 | -1.5 | -0.4 | -0.2 |
| JIOFIN | -2.5 | -0.4 | -1.2 | -0.6 | -0.2 |
| INDUSINDBK | -2.4 | -0.1 | -1.5 | -1.0 | +0.1 |
| LTF | -2.4 | -0.6 | -1.4 | -0.4 | -0.0 |
| JSWENERGY | -2.4 | -0.9 | -0.9 | -0.4 | -0.1 |
| SBIN | -2.3 | -1.0 | -0.7 | -0.5 | -0.1 |
| AXISBANK | -2.2 | -0.3 | -1.2 | -0.8 | +0.0 |
| ADANIGREEN | -2.2 | -0.3 | -1.3 | -0.5 | -0.2 |
| SWIGGY | -2.2 | -1.6 | -0.7 | +0.2 | -0.1 |

Share of absolute impact by order: 1: 28%, 2: 43%, 3: 21%, 4: 7%

## Sources
- 2026-11-03 Gram -59%, lentil -49% https://www.businesstoday.in/latest/economy/story/indias-rabi-sowing-falls-46-to-37-56-lakh-hectares-wheat-acreage-plunges-94-565374-2026-11-03
- 2026-10-12 Sept food CPI 7.74% https://timesofindia.indiatimes.com/business/india-business/retail-inflation-at-almost-2-year-high-at-5-54-in-september-driven-by-food-prices-surge/articleshow/134890491.cms