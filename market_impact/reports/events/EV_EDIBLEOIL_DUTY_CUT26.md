# India cuts edible-oil import duties from 24 Sep 2026 (crude palm/soy 10% to 5%, crude sunflower to zero) (`EV_EDIBLEOIL_DUTY_CUT26`)
*agri_rural · status occurred · date 2026-09-24 · P(3m) 1.0 · P(12m) 1.0 · confidence high*

Notification of 23 Sep, effective 24 Sep: basic customs duty on crude palm and soya oil 10% to 5%; refined palm/soy 32.5% to 27.5%; crude sunflower 10% to 0%; refined sunflower 32.5% to 22.5%. Rationale: sharp rise in food inflation before festivals (WPI food 7.1% in Aug, edible oils among drivers). Government asked companies to pass on the cut. Oils & Fats International expects sunflower oil imports +30% in 2026/27. Duty had been raised in Sep 2024 and halved on crude oils in May 2025 (model knowledge).

**Already moved:** Palm/edible-oil proxy -7.7% in 1m, +4.0% in 3m, +1.9% since 1 Jun (factor_state); domestic pass-through unclear.

## Entry shocks (conditional on the event)
- `F_EDIBLE_OIL` Palm / edible oil price: 0.0 SSU (range -0.3…0.5) Domestic landed cost down ~5 pp; global price effect of larger Indian demand roughly offsets (global price shock ~0).
- `F_FOOD_INFLATION_IN` India food inflation: -0.1 SSU (range -0.25…0.0) Edible oil about 3-4% of food basket; a 5 pp duty cut lowers retail oil ~3-4%.

## Causal chains (agent)
- order 2: EV_EDIBLEOIL_DUTY_CUT26 → F_EDIBLE_OIL → F_FOOD_INFLATION_IN — Lower landed oil prices trim food CPI by 0.1-0.2 pp over 3 months.
- order 3: EV_EDIBLEOIL_DUTY_CUT26 → F_EDIBLE_OIL → F_PACKAGING — Cheaper oil improves margins for FMCG users of palm/soy oil (soaps, biscuits, snacks).
- order 4: EV_EDIBLEOIL_DUTY_CUT26 → F_EDIBLE_OIL → F_FOOD_INFLATION_IN → F_CPI_IN — Slightly lower CPI path.

## Most positively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| YESBANK | +0.3 | +0.0 | +0.0 | +0.2 | +0.1 |
| TATACAP | +0.3 | +0.0 | +0.0 | +0.2 | +0.1 |
| BAJFINANCE | +0.3 | +0.0 | +0.0 | +0.2 | +0.1 |
| AUBANK | +0.2 | +0.0 | +0.0 | +0.1 | +0.1 |
| IDFCFIRSTB | +0.2 | +0.0 | +0.0 | +0.2 | +0.1 |
| IREDA | +0.2 | +0.0 | +0.0 | +0.1 | +0.1 |
| PRESTIGE | +0.2 | +0.0 | +0.0 | +0.1 | +0.1 |
| INDUSINDBK | +0.2 | +0.0 | +0.0 | +0.1 | +0.1 |
| BAJAJFINSV | +0.2 | +0.0 | +0.0 | +0.1 | +0.1 |
| LTF | +0.2 | +0.0 | +0.0 | +0.1 | +0.0 |
| SHRIRAMFIN | +0.2 | +0.0 | +0.0 | +0.1 | +0.1 |
| M&MFIN | +0.2 | +0.0 | +0.0 | +0.1 | +0.0 |
| JSWENERGY | +0.2 | +0.0 | +0.0 | +0.1 | +0.0 |
| AXISBANK | +0.2 | +0.0 | +0.0 | +0.1 | +0.1 |
| VMM | +0.2 | +0.2 | +0.0 | +0.0 | -0.0 |

## Most negatively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| DMART | -0.0 | -0.1 | +0.0 | +0.0 | +0.0 |
| NATIONALUM | -0.0 | +0.0 | +0.0 | -0.0 | +0.0 |
| OIL | -0.0 | +0.0 | +0.0 | -0.0 | +0.0 |
| HINDCOPPER | -0.0 | +0.0 | +0.0 | -0.0 | +0.0 |
| PIIND | -0.0 | +0.0 | +0.0 | -0.0 | +0.0 |
| ONGC | -0.0 | +0.0 | +0.0 | -0.0 | +0.0 |
| UPL | -0.0 | +0.0 | +0.0 | -0.0 | +0.0 |
| LUPIN | -0.0 | +0.0 | +0.0 | -0.0 | -0.0 |
| MCX | -0.0 | +0.0 | +0.0 | -0.0 | +0.0 |
| NMDC | -0.0 | +0.0 | +0.0 | -0.0 | -0.0 |
| DRREDDY | -0.0 | +0.0 | +0.0 | -0.0 | +0.0 |
| VAML | +0.0 | +0.0 | +0.0 | -0.0 | +0.0 |
| HINDZINC | +0.0 | +0.0 | +0.0 | -0.0 | +0.0 |
| SUNPHARMA | +0.0 | +0.0 | +0.0 | -0.0 | +0.0 |
| LTM | +0.0 | +0.0 | +0.0 | -0.0 | +0.0 |

Share of absolute impact by order: 1: 4%, 2: 6%, 3: 62%, 4: 28%

## Sources
- 2026-09-23 Govt cuts import duties on palm, soya and sunflower oils - Business Standard https://www.business-standard.com/economy/news/govt-cuts-import-duty-on-refined-palm-oil-and-soybean-oil-to-27-5-126092301504_1.html
- 2026-09-23 See also Hindu/ETV Bharat/New Indian Express coverage 23-25 Sep 2026 https://www.business-standard.com/economy/news/govt-cuts-import-duty-on-refined-palm-oil-and-soybean-oil-to-27-5-126092301504_1.html