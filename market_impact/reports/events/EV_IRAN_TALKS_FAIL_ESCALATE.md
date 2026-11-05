# Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`)
*geopolitics_trade · status risk_scenario · date 2026-12-15 · P(3m) 0.18 · P(12m) 0.25 · confidence low*

Iran has threatened Gulf oil and AI facilities if attacks renew (Guardian 22 Oct); IRGC claims repeated tanker hits; Saudi-Houthi front active. Probability of a sustained (>2 weeks) Brent >$110 episode.

**Review override applied:** Talks are alive after the US midterms (the Democratic Congress and Vance blaming the war for the loss raise pressure to exit), but strikes continued on 2-3 Nov and Iran calls the US response 'not convincing'. P(sustained >2-week Brent >$110) is lowered. The Brent shock is re-based from $95.

**Already moved:** Oct 2026 episode peaked ~$117.

## Entry shocks (conditional on the event)
- `C_MIDEAST_CONFLICT` Middle East conflict intensity: 1.2 SSU (range 0.6…2.0) re-escalation
- `F_BRENT` Brent crude oil price: 2.2 SSU (range 1.5…3.5) $95 -> ~$115 sustained (Oct-30 close was $117); measured from today's $95
- `F_RISK_SENTIMENT` Global risk aversion (VIX): 1.0 SSU (range 0.5…2.0) VIX +5 pts
- `F_GAS_GLOBAL` Global natural gas / LNG price: 1.0 SSU (range 0.3…2.0) Qatar LNG at risk (LNG tanker hit 30 Oct)

## Causal chains (agent)
- order 2: EV_IRAN_TALKS_FAIL_ESCALATE → F_BRENT → F_USDINR — INR toward 97-98, RBI intervention.
- order 3: EV_IRAN_TALKS_FAIL_ESCALATE → F_BRENT → F_CPI_IN → F_REPO_IN — Another RBI hike likely.
- order 4: EV_IRAN_TALKS_FAIL_ESCALATE → F_BRENT → F_REPO_IN → F_CREDIT_SPREADS_IN → BAJFINANCE — Higher funding costs and spreads compress NBFC margins.
- order 3: EV_IRAN_TALKS_FAIL_ESCALATE → F_GAS_GLOBAL → F_FERTILISER_INPUTS → CHAMBLFERT — LNG shortage lifts urea/fertiliser input cost and subsidy burden.

## Most positively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| OIL | +18.8 | +16.7 | +1.6 | +0.4 | +0.1 |
| ONGC | +14.6 | +12.4 | +1.7 | +0.4 | +0.1 |
| MCX | +3.1 | +2.9 | +0.5 | -0.2 | -0.1 |
| COALINDIA | +3.0 | +2.2 | +0.8 | +0.1 | -0.0 |
| HINDZINC | +2.6 | +0.0 | +1.2 | +1.5 | -0.1 |
| SOLARINDS | +2.4 | +2.9 | -0.2 | -0.2 | -0.1 |
| NATIONALUM | +2.2 | -1.1 | +2.9 | +0.3 | +0.1 |
| JSWSTEEL | +2.1 | +0.0 | +1.2 | +0.8 | +0.1 |
| COCHINSHIP | +2.1 | -0.4 | +1.5 | +1.0 | -0.0 |
| VAML | +2.0 | -0.8 | +2.7 | +0.2 | -0.1 |
| SAIL | +1.5 | +0.0 | +0.4 | +0.9 | +0.2 |
| BAJAJ-AUTO | +1.1 | +0.6 | +0.6 | +0.1 | -0.2 |
| HINDALCO | +1.1 | -0.6 | +1.6 | +0.1 | -0.0 |
| TATASTEEL | +0.9 | -0.6 | +0.9 | +0.6 | +0.1 |
| GLENMARK | +0.9 | +0.0 | +1.1 | -0.2 | -0.0 |

## Most negatively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| INDIGO | -12.9 | -8.5 | -2.8 | -1.2 | -0.4 |
| MOTILALOFS | -10.5 | -3.5 | -4.3 | -2.2 | -0.5 |
| BPCL | -10.0 | -13.9 | +4.1 | -0.2 | -0.1 |
| GMRAIRPORT | -9.6 | -6.3 | -2.0 | -0.7 | -0.6 |
| AXISBANK | -9.2 | -5.1 | -2.2 | -1.5 | -0.4 |
| ICICIAMC | -9.1 | -4.0 | -3.0 | -1.6 | -0.4 |
| IREDA | -8.9 | -5.0 | -1.3 | -2.0 | -0.6 |
| INDUSINDBK | -8.6 | -3.5 | -2.8 | -2.0 | -0.2 |
| IDFCFIRSTB | -8.0 | -3.0 | -2.5 | -2.0 | -0.5 |
| HDFCBANK | -7.9 | -4.3 | -2.0 | -1.3 | -0.3 |
| INDHOTEL | -7.5 | -4.8 | -1.8 | -0.7 | -0.2 |
| IDEA | -7.1 | -2.5 | -2.9 | -1.2 | -0.5 |
| ATGL | -7.0 | -5.2 | -1.2 | -0.6 | -0.1 |
| 360ONE | -6.8 | -3.5 | -1.4 | -1.5 | -0.3 |
| MAHABANK | -6.5 | -3.5 | -1.9 | -0.8 | -0.4 |

Share of absolute impact by order: 1: 44%, 2: 30%, 3: 20%, 4: 6%

## Sources
- 2026-10-22 Iran threatens to strike oil and AI facilities across Gulf if US and Israel renew attacks - The Guardian https://news.google.com/rss/search?q=Iran+threatens+strike+oil+AI+facilities+Gulf+when:120d&hl=en-IN&gl=IN&ceid=IN:en