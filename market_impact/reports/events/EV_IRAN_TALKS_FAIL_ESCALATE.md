# Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`)
*geopolitics_trade · status risk_scenario · date 2026-12-15 · P(3m) 0.3 · P(12m) 0.35714285714285715 · confidence low*

Iran has threatened Gulf oil and AI facilities if attacks renew (Guardian 22 Oct); IRGC claims repeated tanker hits; Saudi-Houthi front active. Probability of a sustained (>2 weeks) Brent >$110 episode.

**Already moved:** Oct 2026 episode peaked ~$117.

## Entry shocks (conditional on the event)
- `C_MIDEAST_CONFLICT` Middle East conflict intensity: 1.2 SSU (range 0.6…2.0) re-escalation
- `F_BRENT` Brent crude oil price: 2.5 SSU (range 1.5…5.0) +25% to >$115
- `F_RISK_SENTIMENT` Global risk aversion (VIX): 1.2 SSU (range 0.6…2.5) VIX +6 pts
- `F_GAS_GLOBAL` Global natural gas / LNG price: 1.0 SSU (range 0.3…2.0) LNG via Qatar at risk

## Causal chains (agent)
- order 2: EV_IRAN_TALKS_FAIL_ESCALATE → F_BRENT → F_USDINR — INR toward 97-98, RBI intervention.
- order 3: EV_IRAN_TALKS_FAIL_ESCALATE → F_BRENT → F_CPI_IN → F_REPO_IN — Another RBI hike likely.
- order 4: EV_IRAN_TALKS_FAIL_ESCALATE → F_BRENT → F_REPO_IN → F_CREDIT_SPREADS_IN → BAJFINANCE — Higher funding costs and spreads compress NBFC margins.
- order 3: EV_IRAN_TALKS_FAIL_ESCALATE → F_GAS_GLOBAL → F_FERTILISER_INPUTS → CHAMBLFERT — LNG shortage lifts urea/fertiliser input cost and subsidy burden.

## Most positively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| OIL | +20.8 | +18.2 | +2.2 | +0.5 | +0.0 |
| ONGC | +16.2 | +13.4 | +2.3 | +0.5 | +0.0 |
| JSWSTEEL | +4.2 | +0.0 | +2.1 | +2.0 | +0.0 |
| SAIL | +4.0 | +0.0 | +0.7 | +3.0 | +0.3 |
| COALINDIA | +3.6 | +2.5 | +1.0 | +0.2 | -0.1 |
| MCX | +3.5 | +3.1 | +0.6 | -0.2 | -0.1 |
| COCHINSHIP | +3.0 | -0.5 | +1.7 | +1.9 | -0.1 |
| HINDZINC | +2.6 | +0.0 | +2.0 | +1.2 | -0.6 |
| NATIONALUM | +2.5 | -1.2 | +3.5 | +0.3 | -0.0 |
| TATASTEEL | +2.5 | -0.6 | +1.4 | +1.6 | +0.1 |
| VAML | +2.3 | -1.0 | +3.5 | +0.3 | -0.5 |
| SOLARINDS | +2.3 | +3.0 | -0.1 | -0.4 | -0.3 |
| DRREDDY | +1.6 | -0.8 | +2.5 | +0.0 | -0.1 |
| HINDALCO | +1.5 | -0.6 | +2.2 | +0.1 | -0.1 |
| BAJAJ-AUTO | +1.5 | +0.8 | +1.0 | +0.1 | -0.5 |

## Most negatively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| INDIGO | -15.3 | -9.2 | -3.3 | -1.8 | -0.9 |
| YESBANK | -15.2 | +0.0 | -3.9 | -6.3 | -5.0 |
| MOTILALOFS | -15.0 | -4.2 | -5.4 | -4.2 | -1.2 |
| IDFCFIRSTB | -13.5 | -3.6 | -3.1 | -4.6 | -2.3 |
| IREDA | -13.4 | -6.0 | -1.7 | -3.2 | -2.5 |
| GMRAIRPORT | -13.3 | -6.8 | -2.8 | -1.8 | -1.8 |
| JIOFIN | -12.8 | -6.0 | -1.3 | -2.6 | -2.9 |
| INDUSINDBK | -12.7 | -4.2 | -3.4 | -4.0 | -1.2 |
| AXISBANK | -12.7 | -5.4 | -2.7 | -2.9 | -1.6 |
| ICICIAMC | -11.9 | -4.8 | -3.5 | -2.6 | -1.0 |
| BPCL | -11.8 | -15.6 | +4.1 | -0.3 | -0.2 |
| BAJFINANCE | -11.7 | -2.4 | -1.3 | -4.1 | -3.8 |
| HINDPETRO | -11.2 | -13.4 | +2.5 | -0.1 | -0.1 |
| IDEA | -10.8 | -3.0 | -3.6 | -2.2 | -2.0 |
| MEESHO | -10.6 | -7.3 | -1.3 | -1.6 | -0.4 |

Share of absolute impact by order: 1: 36%, 2: 26%, 3: 24%, 4: 14%

## Sources
- 2026-10-22 Iran threatens to strike oil and AI facilities across Gulf if US and Israel renew attacks - The Guardian https://news.google.com/rss/search?q=Iran+threatens+strike+oil+AI+facilities+Gulf+when:120d&hl=en-IN&gl=IN&ceid=IN:en