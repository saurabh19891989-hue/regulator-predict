# Government allows OMCs a retail petrol/diesel price hike (Rs3-5/l) (`EV_INDIA_RETAIL_FUEL_HIKE`)
*sector_policy · status anticipated · date 2027-02-15 · P(3m) 0.18 · P(12m) 0.45 · confidence low*

Prices frozen for months; state elections (UP, Punjab, Uttarakhand, Goa, Manipur) due Feb-Mar 2027 argue against a hike before March; a Brent fall would remove the need. Probability is analyst judgement, not sourced. A hike lifts CPI ~0.3-0.4 pp.

## Entry shocks (conditional on the event)
- `NEW_OMC_MARKETING_MARGIN` OMC petrol+diesel marketing margin: 2.5 SSU (range 1.5…4.0) Rs2.5/l net after pass-through
- `F_CPI_IN` India CPI inflation: 0.3 SSU (range 0.2…0.5) 

## Causal chains (agent)
- order 2: EV_INDIA_RETAIL_FUEL_HIKE → NEW_OMC_MARKETING_MARGIN → HINDPETRO — marketing EBITDA
- order 3: EV_INDIA_RETAIL_FUEL_HIKE → F_CPI_IN → F_REPO_IN — CPI adds to hike bias
- order 4: EV_INDIA_RETAIL_FUEL_HIKE → F_CPI_IN → F_REPO_IN → F_GSEC_10Y_IN — yields up

## Most positively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| HINDPETRO | +29.7 | +30.0 | -0.4 | +0.1 | -0.0 |
| IOC | +16.1 | +16.2 | -0.3 | +0.1 | -0.0 |
| BPCL | +14.7 | +15.0 | -0.4 | +0.1 | -0.0 |
| BANKINDIA | +2.4 | +0.0 | +1.5 | -0.5 | +1.4 |
| SAIL | +2.4 | +0.0 | +1.1 | +1.5 | -0.2 |
| MAHABANK | +2.2 | +0.0 | +1.3 | -0.2 | +1.1 |
| UNIONBANK | +2.1 | +0.0 | +1.3 | -0.1 | +1.0 |
| PNB | +2.1 | +0.0 | +1.3 | -0.1 | +0.9 |
| TMCV | +2.1 | +0.0 | +1.9 | +0.1 | +0.1 |
| POWERINDIA | +2.1 | +0.0 | +2.2 | -0.1 | -0.1 |
| ASHOKLEY | +1.9 | +0.0 | +1.4 | +0.5 | +0.1 |
| CGPOWER | +1.8 | +0.0 | +1.6 | +0.2 | -0.0 |
| ENRIN | +1.8 | +0.0 | +1.9 | -0.0 | -0.0 |
| JINDALSTEL | +1.8 | +0.0 | +0.7 | +1.2 | -0.1 |
| JSWSTEEL | +1.6 | +0.0 | +0.9 | +0.9 | -0.2 |

## Most negatively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| BAJFINANCE | -2.6 | +0.0 | -1.6 | -1.2 | +0.1 |
| PRESTIGE | -2.6 | +0.0 | -1.5 | -0.8 | -0.3 |
| TATACAP | -2.5 | +0.0 | -1.4 | -1.3 | +0.3 |
| GODREJPROP | -2.3 | +0.0 | -1.3 | -0.7 | -0.3 |
| GMRAIRPORT | -2.2 | +0.0 | -1.4 | -0.5 | -0.3 |
| JSWENERGY | -2.1 | +0.0 | -1.3 | -0.6 | -0.3 |
| LODHA | -2.1 | +0.0 | -1.2 | -0.7 | -0.2 |
| OBEROIRLTY | -1.8 | +0.0 | -1.0 | -0.6 | -0.2 |
| IREDA | -1.8 | +0.0 | -1.1 | -0.9 | +0.3 |
| BAJAJFINSV | -1.7 | +0.0 | -1.0 | -0.8 | +0.1 |
| JIOFIN | -1.6 | +0.0 | -0.8 | -0.9 | +0.0 |
| LENSKART | -1.5 | +0.0 | -1.2 | -0.1 | -0.3 |
| AUBANK | -1.4 | +0.0 | -1.2 | -0.9 | +0.6 |
| LTF | -1.4 | +0.0 | -1.0 | -0.7 | +0.2 |
| ETERNAL | -1.4 | +0.0 | -1.2 | -0.1 | -0.2 |

Share of absolute impact by order: 1: 24%, 2: 41%, 3: 21%, 4: 13%

## Sources
- 2026-10-24 BPCL Q2 profit falls on fuel price freeze (headline via Google News RSS; article body not read) https://news.google.com/rss/search?q=petrol+diesel+price+hike+OMC+frozen+when:120d&hl=en-IN&gl=IN&ceid=IN:en