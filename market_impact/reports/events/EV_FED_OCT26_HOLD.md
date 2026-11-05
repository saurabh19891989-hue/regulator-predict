# Fed holds at 3.75-4.00% with two hawkish dissents (28 Oct 2026) (`EV_FED_OCT26_HOLD`)
*global_macro · status occurred · date 2026-10-28 · P(3m) 1 · P(12m) 1 · confidence high*

FOMC held the range at 3-3/4 to 4 percent by a 10-2 vote; Cook and Hammack wanted a 25 bp hike. Statement: activity expanding at a strong pace, productivity strong, inflation elevated, 'will deliver price stability'. Sets up a December hike debate.

**Already moved:** Hold was expected (Reuters 20 Oct: economists saw skip in Oct, hike in Dec). Treasuries rallied into early Nov (10y 4.89%, -7% over 1m in level terms).

## Entry shocks (conditional on the event)
- `F_FED_FUNDS` US Fed funds rate: 0.0 SSU (range 0.0…0.0) no change; hawkish tilt (2 hike dissents)
- `F_US_10Y` US 10-year Treasury yield: -0.3 SSU (range -0.6…0.0) 1m move into early Nov as oil fell and hold was priced

## Causal chains (agent)
- order 2: EV_FED_OCT26_HOLD → F_US_10Y → F_DXY — lower yields soften the dollar
- order 3: EV_FED_OCT26_HOLD → F_DXY → F_FPI_FLOWS → F_USDINR — softer dollar brings FPIs back (FPI bought Rs 20,834 cr in four sessions to 4 Nov, most since 2023)

## Most positively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| MUTHOOTFIN | +0.6 | +0.0 | +0.4 | +0.1 | +0.0 |
| BSE | +0.5 | +0.0 | +0.5 | +0.1 | -0.0 |
| NYKAA | +0.5 | +0.4 | +0.1 | +0.0 | -0.0 |
| ADANIGREEN | +0.5 | +0.0 | +0.5 | +0.1 | -0.0 |
| YESBANK | +0.4 | +0.0 | +0.4 | +0.1 | -0.0 |
| MOTILALOFS | +0.4 | +0.0 | +0.4 | -0.0 | -0.0 |
| VEDL | +0.4 | +0.2 | +0.1 | +0.0 | +0.0 |
| INDUSINDBK | +0.4 | +0.2 | +0.2 | -0.0 | -0.0 |
| INDIGO | +0.4 | +0.2 | +0.1 | +0.0 | -0.0 |
| PFC | +0.4 | +0.0 | +0.3 | +0.0 | -0.0 |
| ADANIENT | +0.4 | +0.0 | +0.3 | +0.1 | -0.0 |
| TATACAP | +0.4 | +0.0 | +0.3 | +0.1 | -0.0 |
| PHOENIXLTD | +0.4 | +0.0 | +0.3 | +0.0 | -0.0 |
| ADANIENSOL | +0.4 | +0.0 | +0.3 | +0.1 | -0.0 |
| SBIN | +0.3 | +0.0 | +0.4 | -0.0 | -0.0 |

## Most negatively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| PREMIERENE | -0.1 | +0.0 | +0.0 | -0.1 | -0.0 |
| COCHINSHIP | -0.1 | +0.0 | +0.0 | -0.1 | -0.0 |
| JSWSTEEL | -0.1 | +0.0 | +0.0 | -0.0 | -0.0 |
| RVNL | -0.1 | +0.0 | +0.0 | -0.1 | +0.0 |
| MANKIND | -0.1 | +0.0 | -0.0 | -0.0 | -0.0 |
| TMPV | -0.1 | +0.0 | +0.0 | -0.1 | -0.0 |
| LTM | -0.1 | -0.1 | +0.1 | -0.0 | -0.0 |
| LICI | -0.1 | +0.0 | +0.1 | -0.1 | -0.0 |
| ONGC | -0.1 | +0.0 | +0.0 | -0.1 | -0.0 |
| OIL | -0.1 | +0.0 | +0.0 | -0.1 | +0.0 |
| SAIL | -0.1 | +0.0 | +0.0 | -0.0 | -0.0 |
| NMDC | -0.0 | +0.0 | +0.0 | -0.0 | -0.0 |
| ENRIN | -0.0 | +0.0 | +0.0 | -0.0 | -0.0 |
| SRF | -0.0 | +0.0 | +0.0 | -0.0 | +0.0 |
| BHEL | -0.0 | +0.0 | +0.0 | -0.0 | +0.0 |

Share of absolute impact by order: 1: 7%, 2: 71%, 3: 17%, 4: 6%

## Sources
- 2026-10-28 Federal Reserve issues FOMC statement, 28 Oct 2026 https://www.federalreserve.gov/newsevents/pressreleases/monetary20261028a.htm
- 2026-10-20 Fed to skip October but raise rates again in December, nearly all economists say - Reuters https://news.google.com/rss/search?q=Fed%20to%20skip%20October%20but%20raise%20rates%20again%20in%20December%2C%20nearly%20all%20economists%20say%20-%20Reuters&hl=en-IN&gl=IN&ceid=IN:en
- 2026-11-05 Foreign Investors Step Up India Bets With Rs 20,834 Crore Stock Buying In Four Days - NDTV Profit https://news.google.com/rss/search?q=Foreign%20Investors%20Step%20Up%20India%20Bets%20With%20Rs%2020%2C834%20Crore%20Stock%20Buying%20In%20Four%20Days%20-%20NDTV%20Profit&hl=en-IN&gl=IN&ceid=IN:en