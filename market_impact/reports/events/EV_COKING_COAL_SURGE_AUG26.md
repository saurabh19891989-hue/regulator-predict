# Coking coal price spike squeezes Indian steel margins (`EV_COKING_COAL_SURGE_AUG26`)
*metals_china · status occurred · date 2026-08-19 · P(3m) 1 · P(12m) 1 · confidence medium*

Global coking coal prices rose ~25% in August 2026 (Reuters/OilPrice, 19-20 Aug; GMK 2 Sep 'rose significantly'); prices stayed volatile in October (GMK 21 Oct) and BMI raised its forecast on supply risks (19 Oct); China domestic coking coal supply shocks (Argus 28 Oct). India imports ~85% of its coking coal, so integrated mills (JSW, Tata, SAIL, Jindal) face a cost squeeze that partly offsets higher steel prices (SMM 23 Oct: 'coal costs squeeze margins').

**Review override applied:** Only canonical coking-coal shock (removed from EV_STEEL_RALLY_2026). Trimmed from +25% to ~+20% because the Aug spike partly retraced and the YTD change was +22% on 19 Oct.

**Already moved:** Coking coal ~+25% in Aug 2026 per Reuters/OilPrice headlines; no factor_state series (series=null) so level not verified.

## Entry shocks (conditional on the event)
- `F_COKING_COAL` Coking coal price: 1.3 SSU (range 0.8…1.7) ~+20% since mid-year (YTD +22% to ~$266/t at 19 Oct; volatile in Oct)
- `F_STEEL_INDIA` Indian domestic steel price: 0.4 SSU (range 0.2…0.7) cost-push passed into prices

## Causal chains (agent)
- order 2: EV_COKING_COAL_SURGE_AUG26 → F_COKING_COAL → TATASTEEL — Coking coal ~35-40% of Indian BF steel cost; +25% lifts cost/t by ~Rs 2,500-3,500 before pricing.
- order 3: EV_COKING_COAL_SURGE_AUG26 → F_COKING_COAL → F_STEEL_INDIA → SAIL — Mills pass cost into HRC/rebar (Reuters: prices set to rise on coal costs), restoring part of the spread.
- order 4: EV_COKING_COAL_SURGE_AUG26 → F_COKING_COAL → F_STEEL_INDIA → F_CPI_IN — Higher steel adds to construction costs and WPI manufacturing inflation.

## Most positively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| COALINDIA | +1.0 | +1.0 | +0.0 | -0.0 | +0.0 |
| NMDC | +0.8 | +0.8 | -0.0 | +0.0 | +0.0 |
| APLAPOLLO | +0.6 | +0.6 | +0.0 | -0.0 | +0.0 |
| M&MFIN | +0.3 | +0.0 | +0.3 | -0.0 | -0.0 |
| LTF | +0.2 | +0.0 | +0.2 | -0.0 | -0.0 |
| CHOLAFIN | +0.1 | +0.0 | +0.1 | -0.0 | -0.0 |
| VAML | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| HINDZINC | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| LTM | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| COFORGE | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| MPHASIS | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| PIIND | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| VEDL | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| AUROPHARMA | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| HCLTECH | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |

## Most negatively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| SAIL | -4.5 | -4.4 | -0.1 | -0.0 | +0.0 |
| JSWSTEEL | -3.6 | -3.6 | -0.1 | -0.0 | +0.0 |
| TATASTEEL | -1.6 | -2.0 | +0.4 | -0.0 | +0.0 |
| TMCV | -0.9 | -0.9 | +0.0 | -0.0 | -0.0 |
| BHEL | -0.8 | -0.8 | +0.0 | -0.0 | +0.0 |
| MARUTI | -0.8 | -0.8 | +0.0 | -0.0 | +0.0 |
| JINDALSTEL | -0.8 | -0.8 | -0.0 | +0.0 | +0.0 |
| ASHOKLEY | -0.7 | -0.7 | +0.0 | -0.0 | +0.0 |
| SUZLON | -0.7 | -0.7 | +0.0 | -0.0 | +0.0 |
| HYUNDAI | -0.6 | -0.6 | +0.0 | -0.0 | -0.0 |
| RVNL | -0.6 | -0.6 | +0.0 | -0.0 | +0.0 |
| COCHINSHIP | -0.6 | -0.6 | +0.0 | +0.0 | +0.0 |
| TIINDIA | -0.6 | -0.6 | +0.0 | -0.0 | +0.0 |
| TMPV | -0.5 | +0.0 | -0.5 | +0.0 | +0.0 |
| TVSMOTOR | -0.5 | -0.5 | +0.0 | -0.0 | -0.0 |

Share of absolute impact by order: 1: 83%, 2: 11%, 3: 5%, 4: 1%

## Sources
- 2026-08-19 Indian steel mills face margin squeeze as global coking coal prices rise https://news.google.com/rss/search?q=Indian+steel+mills+face+margin+squeeze+as+global+coking+coal+prices+rise&hl=en-IN&gl=IN&ceid=IN:en
- 2026-08-20 Coking Coal Prices Surge 25%, Squeezing India's Steelmakers https://news.google.com/rss/search?q=Coking+Coal+Prices+Surge+25%,+Squeezing+India's+Steelmakers&hl=en-IN&gl=IN&ceid=IN:en
- 2026-10-19 BMI has raised its forecast for coking coal prices amid supply risks https://news.google.com/rss/search?q=BMI+has+raised+its+forecast+for+coking+coal+prices+amid+supply+risks&hl=en-IN&gl=IN&ceid=IN:en
- 2026-10-28 Coking Coal Outlook: China Supply Shocks and Price Trends https://news.google.com/rss/search?q=Coking+Coal+Outlook:+China+Supply+Shocks+and+Price+Trends&hl=en-IN&gl=IN&ceid=IN:en