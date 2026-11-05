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
| OIL | +39.6 | +34.6 | +3.6 | +1.1 | +0.2 |
| ONGC | +31.2 | +26.0 | +3.8 | +1.2 | +0.2 |
| COALINDIA | +7.0 | +4.5 | +2.1 | +0.5 | -0.1 |
| MCX | +5.9 | +5.9 | +0.9 | -0.7 | -0.2 |
| HINDZINC | +5.9 | +0.0 | +2.7 | +3.4 | -0.2 |
| NATIONALUM | +5.2 | -2.2 | +6.5 | +0.7 | +0.3 |
| JSWSTEEL | +5.2 | +0.0 | +2.8 | +2.1 | +0.3 |
| SOLARINDS | +4.9 | +6.0 | -0.6 | -0.3 | -0.2 |
| VAML | +3.7 | -2.4 | +5.7 | +0.4 | -0.0 |
| SAIL | +3.6 | +0.0 | +0.9 | +2.3 | +0.4 |
| COCHINSHIP | +3.0 | -2.2 | +3.2 | +2.1 | -0.1 |
| BAJAJ-AUTO | +2.8 | +1.1 | +1.5 | +0.3 | -0.2 |
| HINDALCO | +2.4 | -1.2 | +3.5 | +0.2 | +0.0 |
| GLENMARK | +1.9 | +0.0 | +2.2 | -0.3 | -0.0 |
| TATASTEEL | +1.9 | -1.8 | +1.9 | +1.5 | +0.2 |

## Most negatively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| INDIGO | -28.2 | -17.5 | -6.8 | -3.0 | -0.9 |
| MOTILALOFS | -27.4 | -10.5 | -10.3 | -5.4 | -1.2 |
| ICICIAMC | -23.9 | -12.0 | -7.2 | -3.8 | -0.9 |
| JIOFIN | -23.3 | -15.0 | -2.8 | -3.7 | -1.9 |
| IREDA | -23.0 | -15.0 | -3.1 | -3.8 | -1.1 |
| MEESHO | -22.0 | -16.5 | -2.9 | -2.2 | -0.4 |
| INDUSINDBK | -21.7 | -10.5 | -6.5 | -4.5 | -0.2 |
| HINDPETRO | -21.1 | -26.2 | +5.4 | +0.1 | -0.2 |
| AXISBANK | -21.0 | -12.0 | -5.0 | -3.3 | -0.7 |
| BPCL | -20.8 | -28.5 | +8.3 | -0.3 | -0.2 |
| GMRAIRPORT | -20.5 | -13.0 | -4.7 | -1.7 | -1.2 |
| IDFCFIRSTB | -20.0 | -9.0 | -5.7 | -4.4 | -0.9 |
| 360ONE | -18.3 | -10.5 | -3.5 | -3.4 | -0.8 |
| IDEA | -17.7 | -7.5 | -6.6 | -2.7 | -1.0 |
| HDFCBANK | -17.6 | -8.9 | -5.1 | -3.1 | -0.4 |

Share of absolute impact by order: 1: 46%, 2: 30%, 3: 19%, 4: 5%

## Sources
- 2026-10-05 Is Iran charging a toll to allow oil traffic through Hormuz? - Al Jazeera https://news.google.com/rss/search?q=Is+Iran+charging+a+toll+to+allow+oil+traffic+through+Hormuz+when:120d&hl=en-IN&gl=IN&ceid=IN:en