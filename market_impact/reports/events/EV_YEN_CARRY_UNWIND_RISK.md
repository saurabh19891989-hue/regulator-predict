# Disorderly yen carry-trade unwind (Aug-2024-style) after BoJ/MoF action (`EV_YEN_CARRY_UNWIND_RISK`)
*global_macro · status risk_scenario · date 2027-01-31 · P(3m) 0.06 · P(12m) 0.18 · confidence low*

Yen neared 160 in Aug 2026; BoJ at 31-year-high rates; hawkish BoJ/Takaichi plus falling UST yields push USD/JPY down; analog Aug 2024 (VIX spike, EM selloff, ~-6% Nikkei day). P(VIX >30 episode linked to yen)=0.06 by 3m, 0.18 by 12m (our estimate).

**Already moved:** n/a

## Entry shocks (conditional on the event)
- `NEW_USDJPY` USD/JPY exchange rate: -3.0 SSU (range -5.0…-1.5) -9% USD/JPY
- `F_RISK_SENTIMENT` Global risk aversion (VIX): 5.0 SSU (range 2.5…9.0) VIX +25 pts
- `F_US_EQUITIES` US equity market: -1.5 SSU (range -3.0…-0.7) 

## Causal chains (agent)
- order 2: EV_YEN_CARRY_UNWIND_RISK → F_RISK_SENTIMENT → F_FPI_FLOWS — EM outflows
- order 3: EV_YEN_CARRY_UNWIND_RISK → F_FPI_FLOWS → F_USDINR — INR
- order 4: EV_YEN_CARRY_UNWIND_RISK → F_USDINR → F_CPI_IN → F_REPO_IN — inflation/RBI

## Most positively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| JSWSTEEL | +4.6 | +0.0 | +1.5 | +2.4 | +0.7 |
| SAIL | +4.5 | +0.0 | +0.6 | +2.5 | +1.4 |
| TATACONSUM | +3.6 | +4.0 | -0.1 | -0.3 | +0.0 |
| HINDZINC | +3.5 | +0.0 | +1.3 | +2.1 | +0.0 |
| TATASTEEL | +3.3 | +0.0 | +0.9 | +1.8 | +0.7 |
| ASTRAL | +3.3 | +4.0 | -0.2 | -0.3 | -0.2 |
| NATIONALUM | +3.3 | +0.0 | +1.8 | +1.6 | -0.1 |
| OIL | +3.0 | +0.0 | +1.8 | +1.4 | -0.1 |
| ONGC | +3.0 | +0.0 | +1.8 | +1.4 | -0.2 |
| NMDC | +2.5 | +0.0 | +1.2 | +1.3 | +0.1 |
| PIIND | +2.2 | +0.0 | +1.2 | +1.0 | -0.0 |
| HINDALCO | +1.9 | +0.0 | +0.9 | +1.0 | -0.0 |
| SRF | +1.9 | +0.0 | +1.2 | +0.9 | -0.3 |
| TMPV | +1.6 | +0.0 | +0.9 | +0.9 | -0.2 |
| BAJAJ-AUTO | +1.5 | +0.0 | +1.2 | +0.6 | -0.3 |

## Most negatively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| MOTILALOFS | -35.0 | -19.8 | -11.8 | -4.2 | +0.8 |
| JIOFIN | -32.4 | -25.0 | -5.3 | -1.6 | -0.4 |
| ICICIAMC | -31.2 | -21.5 | -8.5 | -1.7 | +0.5 |
| IREDA | -30.8 | -25.0 | -4.5 | -0.8 | -0.5 |
| 360ONE | -27.7 | -17.5 | -7.4 | -3.1 | +0.2 |
| MEESHO | -27.7 | -20.0 | -7.5 | -0.0 | -0.2 |
| INDUSINDBK | -25.9 | -17.5 | -8.5 | -0.1 | +0.2 |
| MAHABANK | -22.7 | -17.5 | -5.3 | -0.0 | +0.2 |
| IDFCFIRSTB | -22.6 | -15.0 | -6.5 | -0.5 | -0.5 |
| NAUKRI | -22.3 | -16.2 | -5.7 | -0.5 | +0.1 |
| LENSKART | -21.8 | -15.0 | -6.5 | -0.1 | -0.2 |
| LICI | -20.8 | -17.5 | -3.4 | -0.1 | +0.2 |
| PAYTM | -20.6 | -11.5 | -9.5 | +0.2 | +0.2 |
| ETERNAL | -20.4 | -12.5 | -7.6 | -0.1 | -0.2 |
| GROWW | -20.3 | -11.5 | -4.7 | -5.4 | +1.4 |

Share of absolute impact by order: 1: 40%, 2: 45%, 3: 10%, 4: 5%

## Sources
- 2026-10-05 Japan Has Left the Zero-Rate World. What Happens to the Yen Carry Trade? - IndraStra https://news.google.com/rss/search?q=Japan%20Has%20Left%20the%20Zero-Rate%20World.%20What%20Happens%20to%20the%20Yen%20Carry%20Trade%3F%20-%20IndraStra&hl=en-IN&gl=IN&ceid=IN:en
- 2026-10-22 USD/JPY Breaks Support as Falling Treasury Yields Favor the Yen - Investing.com https://news.google.com/rss/search?q=USD/JPY%20Breaks%20Support%20as%20Falling%20Treasury%20Yields%20Favor%20the%20Yen%20-%20Investing.com&hl=en-IN&gl=IN&ceid=IN:en