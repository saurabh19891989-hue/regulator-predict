# Hormuz effectively closed for >2 weeks (Brent > $150) (`EV_HORMUZ_FULL_CLOSURE`)
*geopolitics_trade · status risk_scenario · date 2027-01-31 · P(3m) 0.04 · P(12m) 0.0625 · confidence low*

Tail risk: full interdiction of Hormuz/Gulf export infrastructure after talks fail. Flows had normalised by Oct, and Iran appears to prefer tolls/harassment (Al Jazeera 5 Oct), so odds are low but non-zero; Brent briefly hit 117 with partial attacks.

**Already moved:** n/a

## Entry shocks (conditional on the event)
- `C_MIDEAST_CONFLICT` Middle East conflict intensity: 2.5 SSU (range 2.0…3.0) extreme
- `F_BRENT` Brent crude oil price: 6.0 SSU (range 4.0…9.0) +60% to ~$150
- `F_RISK_SENTIMENT` Global risk aversion (VIX): 3.0 SSU (range 2.0…5.0) VIX +15
- `F_GAS_GLOBAL` Global natural gas / LNG price: 3.0 SSU (range 2.0…5.0) Qatar LNG offline

## Causal chains (agent)
- order 2: EV_HORMUZ_FULL_CLOSURE → F_BRENT → F_USDINR — INR >100 risk.
- order 3: EV_HORMUZ_FULL_CLOSURE → F_BRENT → F_CPI_IN → F_GDP_IN — Stagflationary shock to GDP growth.
- order 4: EV_HORMUZ_FULL_CLOSURE → F_BRENT → F_CPI_IN → F_REPO_IN → F_GSEC_10Y_IN — Yield spike hits bank treasury books.

## Most positively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| OIL | +48.4 | +42.1 | +5.1 | +1.1 | +0.1 |
| ONGC | +37.8 | +31.2 | +5.4 | +1.1 | +0.1 |
| JSWSTEEL | +10.1 | +0.0 | +5.1 | +5.0 | +0.1 |
| SAIL | +9.6 | +0.0 | +1.7 | +7.2 | +0.8 |
| COALINDIA | +9.0 | +6.0 | +2.6 | +0.7 | -0.3 |
| MCX | +8.3 | +7.8 | +1.4 | -0.5 | -0.3 |
| HINDZINC | +6.1 | +0.0 | +4.9 | +2.7 | -1.4 |
| COCHINSHIP | +5.9 | -1.5 | +3.7 | +3.9 | -0.2 |
| TATASTEEL | +5.6 | -1.8 | +3.4 | +3.8 | +0.2 |
| NATIONALUM | +5.6 | -3.0 | +7.9 | +0.7 | -0.0 |
| SOLARINDS | +4.8 | +6.8 | -0.3 | -1.0 | -0.6 |
| VAML | +4.4 | -2.4 | +7.5 | +0.6 | -1.3 |
| DRREDDY | +4.1 | -1.8 | +6.1 | +0.1 | -0.3 |
| BAJAJ-AUTO | +3.9 | +2.3 | +2.5 | +0.3 | -1.2 |
| HINDALCO | +3.6 | -1.2 | +5.0 | +0.2 | -0.3 |

## Most negatively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| MOTILALOFS | -36.8 | -10.5 | -13.2 | -10.2 | -2.8 |
| YESBANK | -36.7 | +0.0 | -9.5 | -15.1 | -12.1 |
| INDIGO | -35.8 | -21.2 | -7.8 | -4.4 | -2.3 |
| IDFCFIRSTB | -32.9 | -9.0 | -7.4 | -11.0 | -5.4 |
| IREDA | -32.8 | -15.0 | -4.2 | -7.6 | -6.0 |
| JIOFIN | -31.6 | -15.0 | -3.2 | -6.3 | -7.1 |
| INDUSINDBK | -31.2 | -10.5 | -8.3 | -9.6 | -2.8 |
| GMRAIRPORT | -30.9 | -15.2 | -6.7 | -4.5 | -4.5 |
| AXISBANK | -29.6 | -12.0 | -6.7 | -7.1 | -3.9 |
| ICICIAMC | -29.3 | -12.0 | -8.6 | -6.4 | -2.4 |
| BPCL | -28.6 | -36.8 | +9.2 | -0.7 | -0.4 |
| BAJFINANCE | -28.4 | -6.0 | -3.3 | -9.9 | -9.2 |
| HINDPETRO | -26.3 | -30.8 | +5.1 | -0.3 | -0.3 |
| IDEA | -26.2 | -7.5 | -8.7 | -5.2 | -4.7 |
| MEESHO | -26.0 | -18.0 | -3.2 | -4.0 | -0.8 |

Share of absolute impact by order: 1: 35%, 2: 26%, 3: 24%, 4: 14%

## Sources
- 2026-10-05 Is Iran charging a toll to allow oil traffic through Hormuz? - Al Jazeera https://news.google.com/rss/search?q=Is+Iran+charging+a+toll+to+allow+oil+traffic+through+Hormuz+when:120d&hl=en-IN&gl=IN&ceid=IN:en