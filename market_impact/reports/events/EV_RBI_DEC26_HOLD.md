# RBI MPC Dec 2026 (~4 Dec): holds repo at 5.50% (pause; cut very unlikely) (`EV_RBI_DEC26_HOLD`)
*india_macro · status scheduled · date 2026-12-04 · P(3m) 0.57 · P(12m) 0.57 · confidence low*

Pause scenario: RBI waits to see transmission of the Oct hike and liquidity tightening, with oil easing. Stance likely stays 'calibrated tightening' (cut <=0.01). Hold relative to hike pricing is mildly bond-positive. Odds as in the hike event.

## Entry shocks (conditional on the event)
- `F_REPO_IN` RBI repo rate: 0.0 SSU (range 0.0…0.0) no change
- `F_GSEC_10Y_IN` India 10-year G-sec yield: -0.3 SSU (range -0.8…0.1) relief vs hike pricing

## Causal chains (agent)
- order 2: EV_RBI_DEC26_HOLD → F_GSEC_10Y_IN → F_CREDIT_SPREADS_IN — Lower yields narrow spreads
- order 3: EV_RBI_DEC26_HOLD → F_GSEC_10Y_IN → F_CREDIT_SPREADS_IN → BAJFINANCE — NBFC funding cost relief
- order 4: EV_RBI_DEC26_HOLD → F_GSEC_10Y_IN → F_HOUSING_DEMAND → F_URBAN_DEMAND → DLF — Rates stabilisation supports housing
- order 3: EV_RBI_DEC26_HOLD → F_GSEC_10Y_IN → F_FPI_FLOWS → F_USDINR — Narrower carry may weaken rupee at the margin

## Most positively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| ADANIGREEN | +1.1 | +1.1 | +0.1 | +0.0 | +0.0 |
| YESBANK | +1.0 | +0.9 | +0.0 | +0.1 | +0.0 |
| JIOFIN | +1.0 | +0.9 | +0.1 | +0.0 | +0.0 |
| IREDA | +1.0 | +0.9 | +0.1 | +0.0 | +0.0 |
| BANKINDIA | +1.0 | +0.9 | +0.0 | +0.0 | +0.0 |
| BAJFINANCE | +1.0 | +0.8 | +0.2 | +0.0 | +0.0 |
| TATACAP | +0.9 | +0.8 | +0.2 | +0.0 | +0.0 |
| POWERGRID | +0.9 | +0.9 | +0.0 | +0.0 | +0.0 |
| GMRAIRPORT | +0.9 | +0.8 | +0.1 | +0.0 | +0.0 |
| JSWENERGY | +0.8 | +0.8 | +0.1 | +0.0 | +0.0 |
| TATAPOWER | +0.8 | +0.8 | +0.1 | +0.0 | +0.0 |
| ADANIENT | +0.8 | +0.8 | +0.0 | +0.0 | +0.0 |
| PFC | +0.8 | +0.8 | +0.0 | +0.0 | +0.0 |
| PHOENIXLTD | +0.8 | +0.8 | +0.0 | +0.0 | +0.0 |
| BSE | +0.8 | +0.8 | +0.0 | +0.0 | +0.0 |

## Most negatively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| HDFCLIFE | -0.1 | -0.1 | +0.0 | +0.0 | +0.0 |
| SBILIFE | -0.1 | -0.1 | +0.0 | +0.0 | +0.0 |
| MFSL | -0.1 | -0.1 | +0.0 | +0.0 | +0.0 |
| APARINDS | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| BDL | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| COCHINSHIP | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| HEROMOTOCO | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| M&M | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| MARUTI | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| NATIONALUM | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| NMDC | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| OIL | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| PREMIERENE | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| RVNL | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| SRF | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |

Share of absolute impact by order: 1: 84%, 2: 11%, 3: 3%, 4: 2%

## Sources
- 2026-10-07 Hawkish hike, but measured path ahead - Business Standard https://news.google.com/rss/search?q=RBI+MPC+December+2026+hold+pause+when:120d&hl=en-IN&gl=IN&ceid=IN:en
- 2026-10-07 Rate cuts off the table - Governor https://news.google.com/rss/search?q=RBI+Governor+Malhotra+rate+cuts+off+the+table+when:120d&hl=en-IN&gl=IN&ceid=IN:en