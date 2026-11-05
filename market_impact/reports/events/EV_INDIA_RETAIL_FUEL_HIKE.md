# Government allows OMCs a retail petrol/diesel price hike (Rs3-5/l) (`EV_INDIA_RETAIL_FUEL_HIKE`)
*sector_policy · status anticipated · date 2027-02-15 · P(3m) 0.08 · P(12m) 0.3 · confidence low*

Prices frozen for months; state elections (UP, Punjab, Uttarakhand, Goa, Manipur) due Feb-Mar 2027 argue against a hike before March; a Brent fall would remove the need. Probability is analyst judgement, not sourced. A hike lifts CPI ~0.3-0.4 pp.

**Review override applied:** At Brent $95 (flat since 1 Jun), OMC crude cost is back to the June level. UP/Punjab polls are due Feb-Mar 2027. The need for a hike has largely gone.

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
| HINDPETRO | +29.8 | +30.0 | -0.3 | +0.0 | +0.0 |
| IOC | +16.1 | +16.2 | -0.2 | +0.0 | +0.0 |
| BPCL | +14.8 | +15.0 | -0.2 | -0.0 | +0.0 |
| SAIL | +0.4 | +0.0 | +0.2 | +0.2 | -0.0 |
| JSWSTEEL | +0.3 | +0.0 | +0.2 | +0.1 | +0.0 |
| BANKINDIA | +0.2 | +0.0 | +0.4 | -0.3 | +0.2 |
| ASHOKLEY | +0.2 | +0.0 | +0.2 | -0.0 | +0.1 |
| ENRIN | +0.2 | +0.0 | +0.2 | -0.0 | +0.0 |
| LICHSGFIN | +0.2 | +0.0 | +0.4 | -0.3 | +0.1 |
| CGPOWER | +0.2 | +0.0 | +0.2 | +0.0 | -0.0 |
| POWERINDIA | +0.2 | +0.0 | +0.2 | -0.0 | +0.0 |
| MAHABANK | +0.2 | +0.0 | +0.3 | -0.3 | +0.1 |
| TATASTEEL | +0.2 | +0.0 | +0.1 | +0.1 | +0.0 |
| TMCV | +0.2 | +0.0 | +0.2 | -0.2 | +0.2 |
| JINDALSTEL | +0.2 | +0.0 | +0.1 | +0.1 | -0.0 |

## Most negatively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| JSWENERGY | -1.0 | +0.0 | -0.7 | -0.2 | -0.0 |
| IREDA | -1.0 | +0.0 | -0.7 | -0.4 | +0.1 |
| JIOFIN | -0.9 | +0.0 | -0.5 | -0.4 | -0.0 |
| GODREJPROP | -0.9 | +0.0 | -0.7 | -0.2 | +0.0 |
| BAJFINANCE | -0.8 | +0.0 | -0.8 | -0.2 | +0.1 |
| TATACAP | -0.8 | +0.0 | -0.6 | -0.4 | +0.1 |
| PRESTIGE | -0.8 | +0.0 | -0.5 | -0.3 | +0.0 |
| ADANIGREEN | -0.8 | +0.0 | -0.5 | -0.3 | -0.0 |
| OBEROIRLTY | -0.7 | +0.0 | -0.6 | -0.2 | +0.0 |
| LTF | -0.7 | +0.0 | -0.6 | -0.2 | +0.1 |
| IDEA | -0.7 | +0.0 | -0.5 | -0.2 | -0.0 |
| AUBANK | -0.7 | +0.0 | -0.6 | -0.3 | +0.1 |
| YESBANK | -0.7 | +0.0 | -0.7 | -0.2 | +0.2 |
| GMRAIRPORT | -0.7 | +0.0 | -0.5 | -0.2 | +0.0 |
| DLF | -0.7 | +0.0 | -0.5 | -0.1 | +0.0 |

Share of absolute impact by order: 1: 46%, 2: 33%, 3: 15%, 4: 5%

## Sources
- 2026-10-24 BPCL Q2 profit falls on fuel price freeze (headline via Google News RSS; article body not read) https://news.google.com/rss/search?q=petrol+diesel+price+hike+OMC+frozen+when:120d&hl=en-IN&gl=IN&ceid=IN:en