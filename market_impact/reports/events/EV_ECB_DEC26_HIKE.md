# ECB December 2026 meeting: 25 bp hike to 2.75% then pause (`EV_ECB_DEC26_HIKE`)
*global_macro · status scheduled · date 2026-12-10 · P(3m) 0.6 · P(12m) 0.6 · confidence low*

ECB hiked to 2.5% on 10 Sep (CNBC) and held on 29 Oct (CNBC); Reuters 29 Oct: governors see a December hike likely followed by a pause; gas near EUR100/MWh. Meeting date approximate. P(hike)=0.6 (our estimate). Growth hit from yields (France 10y near 5%) is a risk to EU demand.

**Already moved:** n/a

## Entry shocks (conditional on the event)
- `F_EU_GDP` Europe growth: -0.1 SSU (range -0.2…0.0) tightening drag per 25 bp
- `F_DXY` US dollar index: -0.1 SSU (range -0.3…0.1) euro supported

## Causal chains (agent)
- order 2: EV_ECB_DEC26_HIKE → F_EU_GDP → C_EU_UK — EU/UK demand softer
- order 3: EV_ECB_DEC26_HIKE → C_EU_UK → F_US_TECH_SPEND — European tech budgets
- order 4: EV_ECB_DEC26_HIKE → C_EU_UK → I_IT_SERVICES → HCLTECH — Europe ~25-30% of Indian IT revenue (model knowledge)

## Most positively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| MOTILALOFS | +0.4 | +0.0 | +0.3 | +0.1 | +0.0 |
| YESBANK | +0.3 | +0.0 | +0.1 | +0.1 | +0.1 |
| BSE | +0.3 | +0.0 | +0.1 | +0.1 | -0.0 |
| MUTHOOTFIN | +0.3 | +0.0 | +0.2 | +0.0 | +0.0 |
| ICICIAMC | +0.3 | +0.0 | +0.2 | +0.1 | +0.0 |
| 360ONE | +0.3 | +0.0 | +0.1 | +0.1 | +0.0 |
| GROWW | +0.3 | +0.0 | +0.1 | +0.1 | +0.0 |
| SBIN | +0.3 | +0.0 | +0.2 | +0.0 | +0.0 |
| PAYTM | +0.2 | +0.0 | +0.2 | +0.0 | +0.0 |
| BAJFINANCE | +0.2 | +0.0 | +0.1 | +0.0 | +0.1 |
| AUBANK | +0.2 | +0.0 | +0.1 | +0.0 | +0.1 |
| MAXHEALTH | +0.2 | +0.2 | +0.1 | +0.0 | +0.0 |
| ETERNAL | +0.2 | +0.0 | +0.2 | +0.0 | +0.0 |
| INDIGO | +0.2 | +0.0 | +0.2 | +0.0 | +0.0 |
| ADANIENSOL | +0.2 | +0.0 | +0.1 | +0.0 | +0.0 |

## Most negatively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| TMPV | -0.4 | -0.2 | -0.1 | -0.1 | -0.0 |
| PERSISTENT | -0.2 | -0.2 | -0.1 | -0.0 | +0.0 |
| TECHM | -0.2 | -0.1 | -0.1 | -0.0 | +0.0 |
| JSWSTEEL | -0.2 | -0.0 | -0.1 | -0.1 | -0.0 |
| HCLTECH | -0.2 | -0.1 | -0.0 | -0.0 | +0.0 |
| TCS | -0.2 | -0.1 | -0.1 | -0.0 | +0.0 |
| WIPRO | -0.2 | -0.2 | +0.0 | -0.0 | +0.0 |
| PIIND | -0.2 | -0.1 | -0.0 | -0.0 | -0.0 |
| TATASTEEL | -0.1 | -0.1 | +0.0 | -0.1 | -0.0 |
| MOTHERSON | -0.1 | -0.2 | -0.0 | -0.0 | +0.0 |
| BIOCON | -0.1 | -0.1 | -0.1 | -0.0 | +0.0 |
| INFY | -0.1 | -0.1 | -0.0 | -0.0 | +0.0 |
| MANKIND | -0.1 | -0.2 | +0.0 | +0.0 | +0.0 |
| SAIL | -0.1 | +0.0 | -0.0 | -0.1 | -0.0 |
| BAJAJ-AUTO | -0.1 | -0.1 | -0.0 | -0.0 | +0.0 |

Share of absolute impact by order: 1: 13%, 2: 56%, 3: 20%, 4: 11%

## Sources
- 2026-10-29 ECB governors see December hike likely followed by pause, sources say - Reuters https://news.google.com/rss/search?q=ECB%20governors%20see%20December%20hike%20likely%20followed%20by%20pause%2C%20sources%20say%20-%20Reuters&hl=en-IN&gl=IN&ceid=IN:en
- 2026-10-29 European Central Bank keeps key interest rate on hold at 2.5% - CNBC https://news.google.com/rss/search?q=European%20Central%20Bank%20keeps%20key%20interest%20rate%20on%20hold%20at%202.5%25%20-%20CNBC&hl=en-IN&gl=IN&ceid=IN:en
- 2026-09-10 ECB hikes interest rates to 2.5% - CNBC https://news.google.com/rss/search?q=ECB%20hikes%20interest%20rates%20to%202.5%25%20-%20CNBC&hl=en-IN&gl=IN&ceid=IN:en