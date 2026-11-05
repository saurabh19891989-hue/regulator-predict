# Hormuz effectively closed for >2 weeks (Brent > $150) (`EV_HORMUZ_FULL_CLOSURE`)
*geopolitics_trade · status risk_scenario · date 2027-01-31 · P(3m) 0.03 · P(12m) 0.05 · confidence low*

Tail risk: full interdiction of Hormuz/Gulf export infrastructure after talks fail. Flows had normalised by Oct, and Iran appears to prefer tolls/harassment (Al Jazeera 5 Oct), so odds are low but non-zero; Brent briefly hit 117 with partial attacks.

**Review override applied:** Shock re-based from $95 (the old +60% was framed against ~$95, but the range was too wide on the upside). Hormuz was already at a 'near standstill' on 31 Oct with Brent at only $113-117. The event description's claim that 'flows had normalised by Oct' is wrong. A >$150 outcome needs attacks on Gulf export infrastructure, not just shipping harassment.

**Already moved:** n/a

## Entry shocks (conditional on the event)
- `C_MIDEAST_CONFLICT` Middle East conflict intensity: 2.5 SSU (range 2.0…3.0) extreme
- `F_BRENT` Brent crude oil price: 4.5 SSU (range 3.5…6.5) $95 -> $130-150 (+37% to +58%) from today's level
- `F_RISK_SENTIMENT` Global risk aversion (VIX): 3.0 SSU (range 2.0…5.0) VIX +15
- `F_GAS_GLOBAL` Global natural gas / LNG price: 3.0 SSU (range 2.0…5.0) Qatar LNG offline

## Causal chains (agent)
- order 2: EV_HORMUZ_FULL_CLOSURE → F_BRENT → F_USDINR — INR >100 risk.
- order 3: EV_HORMUZ_FULL_CLOSURE → F_BRENT → F_CPI_IN → F_GDP_IN — Stagflationary shock to GDP growth.
- order 4: EV_HORMUZ_FULL_CLOSURE → F_BRENT → F_CPI_IN → F_REPO_IN → F_GSEC_10Y_IN — Yield spike hits bank treasury books.

## Most positively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| OIL | +40.1 | +34.6 | +4.3 | +1.0 | +0.1 |
| ONGC | +31.7 | +26.0 | +4.6 | +1.1 | +0.1 |
| JSWSTEEL | +8.3 | +0.0 | +4.0 | +4.1 | +0.2 |
| SAIL | +7.8 | +0.0 | +1.4 | +5.7 | +0.8 |
| COALINDIA | +7.4 | +4.5 | +2.4 | +0.8 | -0.3 |
| MCX | +6.4 | +5.9 | +1.2 | -0.4 | -0.3 |
| NATIONALUM | +5.6 | -2.2 | +7.2 | +0.6 | +0.0 |
| HINDZINC | +5.2 | +0.0 | +3.8 | +2.5 | -1.2 |
| COCHINSHIP | +5.1 | -2.2 | +3.5 | +4.1 | -0.2 |
| SOLARINDS | +4.2 | +6.0 | -0.5 | -0.8 | -0.6 |
| TATASTEEL | +4.2 | -1.8 | +2.7 | +3.0 | +0.3 |
| VAML | +4.2 | -2.4 | +7.2 | +0.5 | -1.0 |
| HINDALCO | +3.0 | -1.2 | +4.4 | +0.1 | -0.3 |
| DRREDDY | +2.9 | -1.8 | +4.7 | +0.2 | -0.2 |
| BAJAJ-AUTO | +2.5 | +1.1 | +2.0 | +0.3 | -1.0 |

## Most negatively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| MOTILALOFS | -32.3 | -10.5 | -11.1 | -8.5 | -2.3 |
| INDIGO | -30.6 | -17.5 | -7.3 | -3.9 | -1.9 |
| YESBANK | -29.9 | +0.0 | -8.0 | -12.0 | -9.8 |
| IREDA | -29.3 | -15.0 | -3.5 | -5.9 | -4.8 |
| JIOFIN | -28.4 | -15.0 | -2.8 | -5.0 | -5.7 |
| IDFCFIRSTB | -27.9 | -9.0 | -6.0 | -8.6 | -4.3 |
| INDUSINDBK | -26.9 | -10.5 | -6.7 | -7.5 | -2.2 |
| GMRAIRPORT | -26.7 | -13.0 | -6.1 | -3.8 | -3.8 |
| ICICIAMC | -26.4 | -12.0 | -7.2 | -5.2 | -1.9 |
| AXISBANK | -26.0 | -12.0 | -5.4 | -5.5 | -3.1 |
| BAJFINANCE | -23.7 | -6.0 | -2.7 | -7.7 | -7.3 |
| MEESHO | -23.4 | -16.5 | -2.9 | -3.3 | -0.7 |
| IDEA | -22.9 | -7.5 | -7.4 | -4.2 | -3.8 |
| HINDPETRO | -21.9 | -26.2 | +4.8 | -0.2 | -0.3 |
| INDIANB | -21.7 | -9.0 | -4.6 | -4.3 | -3.8 |

Share of absolute impact by order: 1: 37%, 2: 26%, 3: 23%, 4: 14%

## Sources
- 2026-10-05 Is Iran charging a toll to allow oil traffic through Hormuz? - Al Jazeera https://news.google.com/rss/search?q=Is+Iran+charging+a+toll+to+allow+oil+traffic+through+Hormuz+when:120d&hl=en-IN&gl=IN&ceid=IN:en