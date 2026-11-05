# Fed hikes >=50 bp cumulative beyond Oct level by Apr 2027 (`EV_FED_H1_2027_FURTHER_HIKES`)
*global_macro · status anticipated · date 2027-04-28 · P(3m) 0.15 · P(12m) 0.4 · confidence low*

Oil-driven or sticky inflation (3.7% CPI), strong GDP, and 'multiple hikes likely' (Sept minutes, Scotsman Guide 7 Oct) may push the funds rate to >=4.25-4.50% (i.e. at least two hikes from now) by April 2027. P=0.30 (our judgment).

**Review override applied:** Director: RT_EVENTS probabilities (0.15/0.40, futures talk of 'two more hikes' = Dec + one) with shocks re-defined relative to the post-December level to remove overlap with the separate December group (spec bug flagged by RT_EVENTS).

**Already moved:** n/a

## Entry shocks (conditional on the event)
- `F_FED_FUNDS` US Fed funds rate: 1.0 SSU (range 1.0…2.0) one or more 25bp hikes AFTER December (measured from the post-December level, so it does not double count EV_FED_DEC26_HIKE25)
- `F_US_10Y` US 10-year Treasury yield: 0.5 SSU (range 0.2…1.0) term-premium/rate repricing
- `F_DXY` US dollar index: 0.4 SSU (range 0.1…0.8) dollar support

## Causal chains (agent)
- order 2: EV_FED_H1_2027_FURTHER_HIKES → F_US_10Y → F_FPI_FLOWS — another outflow wave
- order 3: EV_FED_H1_2027_FURTHER_HIKES → F_DXY → F_USDINR → F_CPI_IN — rupee back toward 96-98
- order 4: EV_FED_H1_2027_FURTHER_HIKES → F_FED_FUNDS → F_US_GDP → F_US_TECH_SPEND → I_IT_SERVICES — US slowdown hits IT demand but INR gain cushions margins

## Most positively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| JSWSTEEL | +0.4 | +0.0 | +0.1 | +0.3 | +0.1 |
| SAIL | +0.4 | +0.0 | -0.0 | +0.4 | +0.1 |
| TMPV | +0.4 | +0.0 | +0.2 | +0.1 | +0.0 |
| OIL | +0.3 | +0.0 | +0.3 | +0.1 | -0.0 |
| LICHSGFIN | +0.3 | +1.0 | -0.3 | -0.3 | -0.1 |
| ONGC | +0.3 | +0.0 | +0.2 | +0.1 | +0.0 |
| NMDC | +0.3 | +0.0 | +0.1 | +0.1 | +0.0 |
| PIIND | +0.2 | +0.0 | +0.2 | +0.0 | +0.0 |
| DRREDDY | +0.2 | +0.0 | +0.0 | +0.1 | +0.0 |
| MANKIND | +0.1 | +0.6 | -0.3 | -0.1 | -0.1 |
| JINDALSTEL | +0.1 | +0.0 | -0.1 | +0.2 | +0.1 |
| SRF | +0.1 | +0.0 | +0.0 | +0.0 | +0.0 |
| LUPIN | +0.1 | +0.0 | +0.0 | +0.1 | -0.0 |
| COALINDIA | +0.1 | +0.0 | +0.0 | +0.0 | +0.0 |
| TATASTEEL | +0.0 | +0.0 | -0.2 | +0.2 | +0.0 |

## Most negatively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| BSE | -5.4 | -3.0 | -1.4 | -1.0 | +0.0 |
| MOTILALOFS | -4.1 | +0.0 | -2.3 | -1.4 | -0.4 |
| SWIGGY | -3.7 | -2.5 | -0.9 | -0.2 | -0.1 |
| POLICYBZR | -3.3 | -2.0 | -1.0 | -0.2 | -0.1 |
| ICICIAMC | -3.0 | +0.0 | -1.7 | -0.9 | -0.3 |
| YESBANK | -2.9 | +0.0 | -1.6 | -0.8 | -0.5 |
| JIOFIN | -2.7 | +0.0 | -1.3 | -1.0 | -0.4 |
| INDUSINDBK | -2.7 | -0.4 | -1.2 | -0.8 | -0.3 |
| BAJFINANCE | -2.7 | +0.0 | -1.4 | -0.9 | -0.4 |
| GROWW | -2.6 | +0.0 | -1.2 | -1.3 | -0.2 |
| IREDA | -2.6 | +0.0 | -1.3 | -0.9 | -0.4 |
| NAUKRI | -2.5 | +0.0 | -1.6 | -0.7 | -0.2 |
| 360ONE | -2.4 | +0.0 | -1.1 | -0.9 | -0.3 |
| SHRIRAMFIN | -2.4 | -0.6 | -1.0 | -0.5 | -0.3 |
| TATACAP | -2.3 | +0.0 | -1.2 | -0.8 | -0.4 |

Share of absolute impact by order: 1: 12%, 2: 53%, 3: 25%, 4: 10%

## Sources
- 2026-10-07 Fed policymakers saw multiple 2026 rate hikes as likely, September FOMC minutes show https://news.google.com/rss/search?q=Fed%20policymakers%20saw%20multiple%202026%20rate%20hikes%20as%20likely%2C%20September%20FOMC%20minutes%20show&hl=en-IN&gl=IN&ceid=IN:en
- 2026-09-29 J.P. Morgan sees Fed rate hikes going out with a bang this year - TheStreet https://news.google.com/rss/search?q=J.P.%20Morgan%20sees%20Fed%20rate%20hikes%20going%20out%20with%20a%20bang%20this%20year%20-%20TheStreet&hl=en-IN&gl=IN&ceid=IN:en