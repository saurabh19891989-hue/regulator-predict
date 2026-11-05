# EU quota-halving steel regime and CBAM cut Indian steel exports to EU (`EV_EU_STEEL_REGIME_CBAM_HITS_INDIA`)
*metals_china · status occurred · date 2026-07-01 · P(3m) 1 · P(12m) 1 · confidence medium*

EU CBAM definitive period began 1 Jan 2026 (certificate purchases from 2027, model knowledge); the EU's new steel import regime (replacing the safeguard; smaller quotas, higher out-of-quota tariff, melt-and-pour rules) applies from mid-2026 (LSE 6 Oct; Reuters/Outlook Business 21 Jul: Indian exports to Europe set to fall ~40%). India's H1 FY27 steel exports to the EU fell ~20% y/y while Americas +262% and Africa +96% (Moneycontrol 2 Nov; SMM 3 Nov). Studies (GMK 18 Aug; S&P/Sandbag 10 Aug) say CBAM cost may be smaller than feared. Net effect: exporters redirect volume to domestic market or other regions, which tempers Indian price gains and raises domestic competition; Tata Steel Europe, conversely, benefits from reduced imports (but Tata warns of falling EU demand, 25 Aug).

**Already moved:** India H1 FY27 steel exports to EU about -20% y/y; Americas +262%, Africa +96% (Moneycontrol, 2 Nov 2026).

## Entry shocks (conditional on the event)
- `NEW_EU_STEEL_ACCESS` EU steel safeguard / CBAM burden on imports: 1.0 SSU (range 0.6…1.4) +1 = tighter EU access (quota cut + CBAM); defined in new_nodes_proposed
- `F_STEEL_INDIA` Indian domestic steel price: -0.15 SSU (range -0.4…0.0) export diversion adds domestic supply

## Causal chains (agent)
- order 2: EV_EU_STEEL_REGIME_CBAM_HITS_INDIA → NEW_EU_STEEL_ACCESS → F_STEEL_INDIA → JSWSTEEL — Diverted export tonnes soften Indian domestic pricing at the margin.
- order 3: EV_EU_STEEL_REGIME_CBAM_HITS_INDIA → NEW_EU_STEEL_ACCESS → F_STEEL_INDIA → F_CPI_IN — Slightly dampens construction-cost inflation.
- order 4: EV_EU_STEEL_REGIME_CBAM_HITS_INDIA → NEW_EU_STEEL_ACCESS → C_EU_UK → TATASTEEL — Tata Steel's European operations gain from fewer imports but face weak EU demand; aluminium/MSME exporters bear compliance cost.

## Most positively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| TMCV | +0.3 | +0.3 | +0.0 | +0.0 | +0.0 |
| MARUTI | +0.3 | +0.3 | +0.0 | +0.0 | +0.0 |
| BHEL | +0.3 | +0.3 | +0.0 | +0.0 | +0.0 |
| ASHOKLEY | +0.3 | +0.3 | +0.0 | +0.0 | +0.0 |
| SUZLON | +0.3 | +0.3 | +0.0 | +0.0 | +0.0 |
| HYUNDAI | +0.2 | +0.2 | +0.0 | +0.0 | +0.0 |
| RVNL | +0.2 | +0.2 | +0.0 | +0.0 | +0.0 |
| COCHINSHIP | +0.2 | +0.2 | +0.0 | +0.0 | +0.0 |
| TIINDIA | +0.2 | +0.2 | +0.0 | +0.0 | +0.0 |
| TVSMOTOR | +0.2 | +0.2 | +0.0 | +0.0 | +0.0 |
| HEROMOTOCO | +0.2 | +0.2 | +0.0 | +0.0 | +0.0 |
| BOSCHLTD | +0.1 | +0.1 | +0.0 | +0.0 | +0.0 |
| PRESTIGE | +0.1 | +0.1 | +0.0 | +0.0 | +0.0 |
| ADANIENSOL | +0.1 | +0.1 | +0.0 | +0.0 | +0.0 |
| CUMMINSIND | +0.1 | +0.1 | +0.0 | +0.0 | +0.0 |

## Most negatively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| JINDALSTEL | -2.9 | -2.9 | +0.0 | +0.0 | +0.0 |
| SAIL | -2.2 | -2.2 | +0.0 | +0.0 | +0.0 |
| JSWSTEEL | -2.1 | -2.1 | +0.0 | +0.0 | +0.0 |
| NMDC | -0.3 | -0.3 | +0.0 | +0.0 | +0.0 |
| APLAPOLLO | -0.2 | -0.2 | -0.0 | +0.0 | +0.0 |
| TATASTEEL | -0.2 | -0.2 | +0.0 | +0.0 | +0.0 |
| PIIND | -0.0 | +0.0 | +0.0 | -0.0 | +0.0 |
| MCX | -0.0 | +0.0 | +0.0 | -0.0 | +0.0 |
| HINDZINC | -0.0 | +0.0 | +0.0 | -0.0 | +0.0 |
| VEDL | -0.0 | +0.0 | +0.0 | -0.0 | +0.0 |
| LTM | -0.0 | +0.0 | +0.0 | -0.0 | +0.0 |
| SUNPHARMA | -0.0 | +0.0 | +0.0 | -0.0 | +0.0 |
| VAML | -0.0 | +0.0 | +0.0 | -0.0 | +0.0 |
| COFORGE | +0.0 | +0.0 | +0.0 | -0.0 | +0.0 |
| MPHASIS | +0.0 | +0.0 | +0.0 | -0.0 | +0.0 |

Share of absolute impact by order: 1: 87%, 2: 3%, 3: 6%, 4: 3%

## Sources
- 2026-11-02 India's steel exports to EU fall 20% amid CBAM, quotas; Americas surge 262%, Africa 96% https://news.google.com/rss/search?q=India's+steel+exports+to+EU+fall+20%+amid+CBAM,+quotas;+Americas+surge+262%,+Africa+96%&hl=en-IN&gl=IN&ceid=IN:en
- 2026-10-06 What the EU's new steel regime means for India: smaller quotas, a higher penalty and a carbon price https://news.google.com/rss/search?q=What+the+EU's+new+steel+regime+means+for+India:+smaller+quotas,+a+higher+penalty+and+a+carbon+price&hl=en-IN&gl=IN&ceid=IN:en
- 2026-07-21 Indian steelmakers pivot home as Europe tightens imports, China squeezes margins https://news.google.com/rss/search?q=Indian+steelmakers+pivot+home+as+Europe+tightens+imports,+China+squeezes+margins&hl=en-IN&gl=IN&ceid=IN:en
- 2026-08-18 The impact of the CBAM on the Indian steel industry may be less than expected - study https://news.google.com/rss/search?q=The+impact+of+the+CBAM+on+the+Indian+steel+industry+may+be+less+than+expected+-+study&hl=en-IN&gl=IN&ceid=IN:en