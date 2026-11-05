# Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`)
*global_macro · status occurred · date 2026-09-16 · P(3m) 1 · P(12m) 1 · confidence high*

FOMC (unanimous, per WSJ headline) raised the target range 25 bp to 3.75-4.00% (range inferred from the 28 Oct statement holding at 3-3/4 to 4 percent) and signalled one more hike in 2026. Kevin Warsh was sworn in as Fed chair on 18 Sep (Reuters headline), after the oil-driven inflation surge.

**Already moved:** Fed funds +25 bp. US 10y +~42 bp since 1 Jun (4.47% -> 4.89%, factor_state.md); DXY +2.2% since 1 Jun; Reuters 7 Oct: hawkish Fed triggered EM outflows in September.

## Entry shocks (conditional on the event)
- `F_FED_FUNDS` US Fed funds rate: 1.0 SSU (range 1.0…1.0) +25 bp delivered
- `F_US_10Y` US 10-year Treasury yield: 0.8 SSU (range 0.3…1.4) part of the ~+1.7 SSU 10y rise since June, partly oil/term premium
- `F_DXY` US dollar index: 0.4 SSU (range 0.2…0.7) dollar firmer on rate differential

## Causal chains (agent)
- order 2: EV_FED_SEP26_HIKE → F_FED_FUNDS → F_US_10Y → F_FPI_FLOWS — higher US yields pull portfolio flows from EM equities
- order 3: EV_FED_SEP26_HIKE → F_DXY → F_USDINR → F_CPI_IN — stronger dollar weakens rupee, adds imported inflation
- order 4: EV_FED_SEP26_HIKE → F_FED_FUNDS → F_US_10Y → F_GSEC_10Y_IN → F_REPO_IN — US yields lift Indian G-sec yields and limit RBI easing room (RBI hiked to 5.5% on 7 Oct)

## Most positively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| LICHSGFIN | +0.4 | +1.0 | -0.4 | -0.2 | +0.0 |
| OIL | +0.2 | +0.0 | +0.2 | +0.1 | -0.0 |
| MANKIND | +0.2 | +0.6 | -0.4 | -0.0 | +0.0 |
| JSWSTEEL | +0.2 | +0.0 | +0.0 | +0.2 | +0.0 |
| ONGC | +0.2 | +0.0 | +0.1 | +0.1 | -0.0 |
| NMDC | +0.2 | +0.0 | +0.1 | +0.1 | +0.0 |
| PIIND | +0.1 | +0.0 | +0.1 | +0.0 | -0.0 |
| COCHINSHIP | +0.1 | +0.0 | -0.0 | +0.1 | +0.0 |
| PREMIERENE | +0.1 | +0.0 | -0.2 | +0.3 | +0.0 |
| SAIL | +0.1 | +0.0 | -0.1 | +0.2 | +0.0 |
| TMPV | +0.1 | +0.0 | +0.1 | +0.0 | +0.0 |
| SRF | +0.0 | +0.0 | -0.0 | +0.1 | +0.0 |
| COALINDIA | +0.0 | +0.0 | -0.0 | +0.0 | +0.0 |
| DRREDDY | +0.0 | +0.0 | -0.1 | +0.1 | -0.0 |
| NATIONALUM | -0.0 | +0.0 | -0.2 | +0.2 | -0.0 |

## Most negatively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| BSE | -5.2 | -3.0 | -1.7 | -0.6 | +0.1 |
| SWIGGY | -3.4 | -2.5 | -0.9 | -0.1 | +0.1 |
| POLICYBZR | -2.8 | -2.0 | -1.0 | +0.2 | +0.0 |
| MOTILALOFS | -2.4 | +0.0 | -2.3 | -0.2 | +0.1 |
| MUTHOOTFIN | -2.4 | +0.0 | -2.2 | -0.2 | -0.0 |
| YESBANK | -2.2 | +0.0 | -1.8 | -0.4 | +0.0 |
| NYKAA | -2.1 | -1.2 | -0.7 | -0.2 | -0.0 |
| ADANIGREEN | -2.0 | +0.0 | -1.7 | -0.3 | +0.0 |
| INDUSINDBK | -2.0 | -0.6 | -1.1 | -0.2 | -0.0 |
| MPHASIS | -1.9 | -1.3 | -0.5 | -0.0 | +0.0 |
| BAJFINANCE | -1.9 | +0.0 | -1.6 | -0.2 | -0.1 |
| TATACAP | -1.9 | +0.0 | -1.4 | -0.4 | -0.0 |
| PRESTIGE | -1.8 | -0.2 | -1.3 | -0.3 | +0.0 |
| AUBANK | -1.7 | +0.0 | -1.4 | -0.3 | -0.0 |
| ICICIAMC | -1.7 | +0.0 | -1.8 | +0.1 | +0.0 |

Share of absolute impact by order: 1: 14%, 2: 70%, 3: 13%, 4: 2%

## Sources
- 2026-09-16 Fed approves interest rate hike, signals one more to come this year - CNBC https://news.google.com/rss/search?q=Fed%20approves%20interest%20rate%20hike%2C%20signals%20one%20more%20to%20come%20this%20year&hl=en-IN&gl=IN&ceid=IN:en
- 2026-10-07 Fed policymakers divided over rate-hike logic in September, minutes show - Reuters https://news.google.com/rss/search?q=Fed%20policymakers%20divided%20over%20rate-hike%20logic%20in%20September%2C%20minutes%20show%20-%20Reuters&hl=en-IN&gl=IN&ceid=IN:en
- 2026-09-18 Trump will swear in Warsh on Friday to lead US Federal Reserve - Reuters https://news.google.com/rss/search?q=Trump%20will%20swear%20in%20Warsh%20on%20Friday%20to%20lead%20US%20Federal%20Reserve%20-%20Reuters&hl=en-IN&gl=IN&ceid=IN:en
- 2026-10-07 Hawkish Fed triggers emerging market outflows in September - Reuters https://news.google.com/rss/search?q=Hawkish%20Fed%20triggers%20emerging%20market%20outflows%20in%20September%20-%20Reuters&hl=en-IN&gl=IN&ceid=IN:en