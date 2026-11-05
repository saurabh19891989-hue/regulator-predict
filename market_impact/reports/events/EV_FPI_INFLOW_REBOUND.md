# FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`)
*india_macro · status anticipated · date 2027-01-15 · P(3m) 0.08 · P(12m) 0.5 · confidence low*

Early signs: FPIs buying in early Nov, longest Nifty winning streak in ~5 months (Reuters 4 Nov); crude -4%/-6% on US-Iran talks (2 Nov); India-US trade deal close per Rubio (20 Oct) though midterm result reduces US urgency; possible LTCG relief; investors rethinking AI bets (ET 2 Nov). Against: rupee still weak, 10y 7.4%, FPI share of market still falling, record YTD outflows. P(a calendar quarter with net equity inflow >= US$5bn by end-Q1 CY27): 0.50.

**Review override applied:** The only calendar quarter that can complete within 3m is Q4 CY26. October had ~-Rs44-48k cr (~-US$5bn) outflow, so Nov-Dec would need ~+US$10bn. Early-Nov buying (Rs20,834 cr in 4 sessions, ~US$2.2bn) helps but is not enough. 12m is unchanged.

## Entry shocks (conditional on the event)
- `F_FPI_FLOWS` Foreign portfolio flows into Indian equities: 2.5 SSU (range 1.2…4.0) swing from ~-US$11bn/qtr run-rate to >=+US$5bn/qtr
- `F_RISK_SENTIMENT` Global risk aversion (VIX): -0.4 SSU (range -1.0…0.0) 

## Causal chains (agent)
- order 2: EV_FPI_INFLOW_REBOUND → F_FPI_FLOWS → F_USDINR — Inflows strengthen rupee
- order 3: EV_FPI_INFLOW_REBOUND → F_FPI_FLOWS → F_USDINR → F_CPI_IN — Imported inflation eases
- order 4: EV_FPI_INFLOW_REBOUND → F_FPI_FLOWS → F_USDINR → F_CPI_IN → F_REPO_IN — Lower inflation pressure reduces hike odds
- order 3: EV_FPI_INFLOW_REBOUND → F_FPI_FLOWS → F_USDINR → TCS — Stronger rupee trims IT-exporter INR earnings

## Most positively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| MOTILALOFS | +19.4 | +16.4 | +3.3 | -0.4 | +0.0 |
| ICICIAMC | +14.0 | +12.8 | +1.4 | -0.3 | +0.0 |
| PAYTM | +13.4 | +13.3 | +0.1 | -0.0 | -0.0 |
| 360ONE | +12.0 | +10.2 | +1.9 | -0.1 | +0.0 |
| INDUSINDBK | +11.5 | +11.4 | +0.2 | -0.1 | -0.0 |
| SBIN | +11.1 | +10.6 | +0.4 | -0.0 | +0.2 |
| POLICYBZR | +10.8 | +11.0 | -0.2 | -0.0 | -0.0 |
| MEESHO | +10.6 | +10.4 | +0.0 | +0.1 | +0.1 |
| BSE | +10.1 | +7.1 | +4.0 | -1.0 | +0.1 |
| ETERNAL | +10.1 | +9.8 | +0.1 | +0.1 | +0.1 |
| JIOFIN | +9.5 | +8.2 | +1.0 | +0.1 | +0.2 |
| IDFCFIRSTB | +9.2 | +8.7 | +0.3 | -0.1 | +0.3 |
| NAUKRI | +9.1 | +8.5 | +0.6 | -0.0 | +0.0 |
| LENSKART | +9.0 | +8.7 | +0.1 | +0.1 | +0.1 |
| HDFCBANK | +8.9 | +8.8 | +0.1 | -0.0 | +0.0 |

## Most negatively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| JSWSTEEL | -1.7 | +0.0 | -1.3 | -0.5 | +0.1 |
| OIL | -1.5 | +0.0 | -1.5 | +0.0 | +0.0 |
| ONGC | -1.5 | +0.0 | -1.5 | +0.0 | +0.0 |
| NATIONALUM | -1.5 | +0.0 | -1.5 | +0.0 | +0.0 |
| SAIL | -1.3 | +0.0 | -0.5 | -0.8 | +0.1 |
| TATASTEEL | -1.1 | +0.0 | -0.8 | -0.4 | +0.0 |
| NMDC | -1.1 | +0.0 | -1.0 | -0.1 | +0.0 |
| HINDZINC | -1.1 | +0.0 | -1.0 | -0.1 | +0.0 |
| PIIND | -1.0 | +0.0 | -1.0 | -0.0 | +0.0 |
| TMPV | -1.0 | +0.0 | -1.0 | +0.0 | +0.0 |
| VAML | -1.0 | +0.3 | -1.3 | +0.0 | +0.0 |
| SRF | -0.9 | +0.0 | -1.0 | +0.0 | +0.0 |
| HINDALCO | -0.9 | +0.0 | -0.9 | +0.0 | +0.0 |
| JINDALSTEL | -0.8 | +0.3 | -0.2 | -0.9 | +0.0 |
| BAJAJ-AUTO | -0.7 | +0.0 | -0.8 | +0.0 | +0.1 |

Share of absolute impact by order: 1: 85%, 2: 11%, 3: 2%, 4: 2%

## Sources
- 2026-11-04 Indian stocks post longest winning streak in nearly 5 months on FPI inflow hopes - Reuters https://news.google.com/rss/search?q=Indian+stocks+longest+winning+streak+FPI+inflow+hopes+when:120d&hl=en-IN&gl=IN&ceid=IN:en
- 2026-11-02 FPI buying returns to Dalal Street as global investors rethink AI bets - ET https://news.google.com/rss/search?q=FPI+buying+returns+Dalal+Street+rethink+AI+bets+when:120d&hl=en-IN&gl=IN&ceid=IN:en
- 2026-10-20 Marco Rubio says we're about as close as you can be to an India trade deal - Fortune https://news.google.com/rss/search?q=India+US+trade+deal+Rubio+close+Mumbai+talks+when:120d&hl=en-IN&gl=IN&ceid=IN:en