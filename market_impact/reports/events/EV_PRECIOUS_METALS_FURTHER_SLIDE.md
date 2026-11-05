# Gold falls to ~$3,500 / silver to ~$40 on Fed hike(s) and strong dollar (`EV_PRECIOUS_METALS_FURTHER_SLIDE`)
*metals_china · status risk_scenario · date 2026-12-16 · P(3m) 0.2 · P(12m) 0.3 · confidence low*

Markets price a December Fed hike (NY Post 28 Oct) after US inflation hit a 3-year high; each hot CPI print has pushed gold down (Reuters 14 Oct). Investing.com (22 Oct) cited a drop to $3,100 before a rally. A hike plus higher-for-longer would take gold toward $3,500 (-15%) and silver toward $40 (-24%). Mirror image of the rebound event; they are mutually exclusive over the same window.

**Review override applied:** The F_FED_FUNDS +1.0 shock double counts EV_FED_DEC26_HIKE25 (separate exclusive group, p 0.72). The Fed is a cause here, not an independent shock, and it would add a second rate hit to banks and NBFCs.

## Entry shocks (conditional on the event)
- `F_GOLD` Gold price: -1.9 SSU (range -3.0…-1.0) -15%
- `F_SILVER` Silver price: -2.0 SSU (range -3.5…-1.0) -24%

## Causal chains (agent)
- order 2: EV_PRECIOUS_METALS_FURTHER_SLIDE → F_GOLD → MUTHOOTFIN — LTV stress for gold loans.
- order 3: EV_PRECIOUS_METALS_FURTHER_SLIDE → F_SILVER → HINDZINC — Silver earnings fall.
- order 4: EV_PRECIOUS_METALS_FURTHER_SLIDE → F_FED_FUNDS → F_FPI_FLOWS → F_USDINR — Fed tightening drives outflows and rupee weakness.

## Most positively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| ADANIGREEN | +4.0 | +3.8 | +0.0 | +0.1 | +0.1 |
| ADANIENT | +3.9 | +3.8 | +0.0 | +0.1 | +0.1 |
| IDEA | +3.0 | +2.8 | +0.0 | +0.1 | +0.1 |
| PREMIERENE | +3.0 | +2.8 | +0.0 | +0.2 | -0.0 |
| WAAREEENER | +1.8 | +1.6 | +0.0 | +0.2 | -0.0 |
| LICI | +1.6 | +1.5 | +0.0 | +0.0 | +0.0 |
| KALYANKJIL | +1.3 | -0.9 | +2.1 | +0.0 | +0.1 |
| YESBANK | +1.0 | +0.0 | +0.0 | +0.6 | +0.4 |
| TATACAP | +1.0 | +0.0 | +0.0 | +0.5 | +0.4 |
| GMRAIRPORT | +0.8 | +0.0 | +0.0 | +0.5 | +0.3 |
| PRESTIGE | +0.8 | +0.0 | +0.0 | +0.6 | +0.2 |
| IREDA | +0.7 | +0.0 | +0.0 | +0.4 | +0.3 |
| PHOENIXLTD | +0.7 | +0.0 | +0.1 | +0.5 | +0.1 |
| SHRIRAMFIN | +0.7 | +0.0 | +0.0 | +0.4 | +0.3 |
| GODREJPROP | +0.7 | +0.0 | +0.0 | +0.5 | +0.2 |

## Most negatively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| HINDZINC | -6.9 | -7.0 | +0.0 | +0.1 | +0.1 |
| MUTHOOTFIN | -6.5 | -6.7 | +0.0 | +0.1 | +0.0 |
| MCX | -5.8 | -5.8 | +0.0 | +0.0 | +0.0 |
| BRITANNIA | -1.8 | -1.9 | +0.0 | +0.1 | -0.0 |
| BAJAJFINSV | -1.2 | -1.5 | +0.0 | +0.2 | +0.1 |
| MFSL | -1.1 | -1.1 | +0.0 | +0.0 | -0.0 |
| CANBK | -0.9 | -0.9 | +0.0 | -0.0 | +0.1 |
| M&MFIN | -0.7 | -0.9 | +0.0 | +0.2 | +0.1 |
| INDUSINDBK | -0.5 | -0.8 | +0.0 | +0.1 | +0.1 |
| BAJFINANCE | -0.1 | -0.6 | +0.0 | +0.3 | +0.2 |
| LICHSGFIN | -0.0 | +0.0 | +0.0 | -0.4 | +0.3 |
| PAYTM | -0.0 | +0.0 | +0.0 | -0.0 | +0.0 |
| UPL | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| IOC | +0.0 | +0.0 | +0.0 | +0.1 | -0.0 |
| PIIND | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |

Share of absolute impact by order: 1: 45%, 2: 5%, 3: 33%, 4: 18%

## Sources
- 2026-10-28 Fed holds interest rates steady - investors bet on December rate hike https://news.google.com/rss/search?q=Fed+holds+interest+rates+steady+-+investors+bet+on+December+rate+hike&hl=en-IN&gl=IN&ceid=IN:en
- 2026-10-14 Gold drops over 1% as hot US inflation data boosts Fed hike bets https://news.google.com/rss/search?q=Gold+drops+over+1%+as+hot+US+inflation+data+boosts+Fed+hike+bets&hl=en-IN&gl=IN&ceid=IN:en
- 2026-10-22 Gold Price Outlook: A Drop to $3,100 Before a Rally to $10,000? https://news.google.com/rss/search?q=Gold+Price+Outlook:+A+Drop+to+$3,100+Before+a+Rally+to+$10,000?&hl=en-IN&gl=IN&ceid=IN:en