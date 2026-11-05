# Fed on hold Jan-Apr 2027 FOMCs (27 Jan, 17 Mar, 28 Apr) near 4% (`EV_FED_H1_2027_PLATEAU`)
*global_macro · status anticipated · date 2027-04-28 · P(3m) 0.0 · P(12m) 0.48 · confidence low*

Base path: after at most one more hike the Fed holds at ~3.75-4.25% through the April 2027 meeting (Sept SEP showed low-4% for 2027 per Bondsavvy headline). Paths (plateau 0.45, further hikes 0.30, cuts 0.25) are mutually exclusive outcomes by 28 Apr 2027 relative to the post-Dec level. Meeting dates from federalreserve.gov calendar (2027: Jan 26-27, Mar 16-17, Apr 27-28; the page lists them as such).

**Review override applied:** Residual; group sums 1.0 at 12m.

**Already moved:** n/a

## Entry shocks (conditional on the event)
- `F_FED_FUNDS` US Fed funds rate: 0.0 SSU (range 0.0…0.0) no net change after Dec
- `F_US_10Y` US 10-year Treasury yield: -0.2 SSU (range -0.8…0.3) yields drift lower as inflation fades from oil

## Causal chains (agent)
- order 2: EV_FED_H1_2027_PLATEAU → F_US_10Y → F_GSEC_10Y_IN — stable US yields stabilise G-secs
- order 3: EV_FED_H1_2027_PLATEAU → F_FPI_FLOWS → F_USDINR — steady flows hold INR
- order 4: EV_FED_H1_2027_PLATEAU → F_USDINR → F_CPI_IN → F_REPO_IN — inflation glide allows RBI hold

## Most positively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| MUTHOOTFIN | +0.4 | +0.0 | +0.3 | +0.1 | +0.0 |
| BSE | +0.4 | +0.0 | +0.3 | +0.1 | -0.0 |
| NYKAA | +0.4 | +0.3 | +0.1 | +0.0 | -0.0 |
| ADANIGREEN | +0.3 | +0.0 | +0.3 | +0.0 | -0.0 |
| JIOFIN | +0.3 | +0.0 | +0.3 | +0.0 | +0.0 |
| MOTILALOFS | +0.3 | +0.0 | +0.3 | -0.0 | -0.0 |
| VEDL | +0.3 | +0.2 | +0.1 | +0.0 | +0.0 |
| INDUSINDBK | +0.3 | +0.2 | +0.1 | -0.0 | -0.0 |
| INDIGO | +0.2 | +0.1 | +0.1 | +0.0 | -0.0 |
| BAJFINANCE | +0.2 | +0.0 | +0.2 | +0.0 | -0.0 |
| PFC | +0.2 | +0.0 | +0.2 | +0.0 | -0.0 |
| ADANIENT | +0.2 | +0.0 | +0.2 | +0.0 | -0.0 |
| PHOENIXLTD | +0.2 | +0.0 | +0.2 | +0.0 | -0.0 |
| ADANIENSOL | +0.2 | +0.0 | +0.2 | +0.0 | -0.0 |
| SBIN | +0.2 | +0.0 | +0.2 | -0.0 | -0.0 |

## Most negatively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| PREMIERENE | -0.1 | +0.0 | +0.0 | -0.0 | -0.0 |
| COCHINSHIP | -0.0 | +0.0 | +0.0 | -0.0 | -0.0 |
| JSWSTEEL | -0.0 | +0.0 | +0.0 | -0.0 | -0.0 |
| RVNL | -0.0 | +0.0 | +0.0 | -0.1 | +0.0 |
| MANKIND | -0.0 | +0.0 | -0.0 | -0.0 | -0.0 |
| TMPV | -0.0 | +0.0 | +0.0 | -0.0 | -0.0 |
| LTM | -0.0 | -0.1 | +0.1 | -0.0 | -0.0 |
| LICI | -0.0 | +0.0 | +0.0 | -0.1 | -0.0 |
| ONGC | -0.0 | +0.0 | +0.0 | -0.0 | -0.0 |
| OIL | -0.0 | +0.0 | +0.0 | -0.0 | +0.0 |
| SAIL | -0.0 | +0.0 | +0.0 | -0.0 | -0.0 |
| NMDC | -0.0 | +0.0 | +0.0 | -0.0 | -0.0 |
| ENRIN | -0.0 | +0.0 | +0.0 | -0.0 | -0.0 |
| SRF | -0.0 | +0.0 | +0.0 | -0.0 | +0.0 |
| BHEL | -0.0 | +0.0 | +0.0 | -0.0 | +0.0 |

Share of absolute impact by order: 1: 7%, 2: 71%, 3: 16%, 4: 6%

## Sources
- 2026-10-28 FOMC calendar https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm
- 2026-09-16 September 2026 Fed Dot Plot Sees Low 4% Fed Funds in 2027 - Bondsavvy https://news.google.com/rss/search?q=September%202026%20Fed%20Dot%20Plot%20Sees%20Low%204%25%20Fed%20Funds%20in%202027%20-%20Bondsavvy&hl=en-IN&gl=IN&ceid=IN:en