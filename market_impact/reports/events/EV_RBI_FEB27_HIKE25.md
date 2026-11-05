# RBI MPC Feb 2027 (~5 Feb, just after Budget): hikes 25 bp (`EV_RBI_FEB27_HIKE25`)
*india_macro · status scheduled · date 2027-02-05 · P(3m) 0.27 · P(12m) 0.27 · confidence low*

Date approximate. Conditional on persistent CPI near/above 6%, rupee pressure and a slippage-heavy Budget. Odds for Feb (unconditional on Dec): hike 0.27, hold 0.66, cut 0.04, hike 50 bp 0.03. Cumulative P(repo >=5.75% by Feb) ~0.55 and P(>=6.00%) ~0.12.

## Entry shocks (conditional on the event)
- `F_REPO_IN` RBI repo rate: 1.0 SSU (range 1.0…1.0) +25 bp
- `F_GSEC_10Y_IN` India 10-year G-sec yield: 0.3 SSU (range -0.1…0.8) 

## Causal chains (agent)
- order 2: EV_RBI_FEB27_HIKE25 → F_REPO_IN → F_CREDIT_GROWTH_IN — Credit slows
- order 3: EV_RBI_FEB27_HIKE25 → F_REPO_IN → F_CREDIT_GROWTH_IN → F_GDP_IN — Growth drag
- order 3: EV_RBI_FEB27_HIKE25 → F_REPO_IN → F_HOUSING_DEMAND → DLF — Housing
- order 4: EV_RBI_FEB27_HIKE25 → F_REPO_IN → F_CREDIT_GROWTH_IN → F_GDP_IN → F_FPI_FLOWS — Growth scare can offset carry benefits for flows

## Most positively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| LICHSGFIN | +1.7 | +2.5 | -0.9 | +0.1 | -0.0 |
| BANKINDIA | +0.7 | +1.6 | -0.7 | -0.1 | -0.1 |
| PAYTM | +0.6 | +0.8 | -0.3 | +0.1 | -0.1 |
| MAHABANK | +0.2 | +1.1 | -0.6 | -0.1 | -0.2 |
| UNIONBANK | +0.0 | +0.6 | -0.4 | -0.0 | -0.1 |
| PNB | -0.0 | +0.6 | -0.4 | -0.0 | -0.1 |
| KOTAKBANK | -0.0 | +0.8 | -0.6 | -0.1 | -0.1 |
| SBIN | -0.1 | +0.4 | -0.4 | +0.0 | -0.1 |
| UPL | -0.1 | +0.0 | -0.1 | -0.0 | +0.0 |
| MCX | -0.1 | +0.0 | -0.1 | +0.0 | -0.0 |
| GROWW | -0.1 | -0.2 | +0.0 | +0.1 | +0.1 |
| BANKBARODA | -0.2 | +0.1 | -0.3 | +0.1 | -0.0 |
| PIIND | -0.2 | +0.0 | -0.2 | -0.0 | +0.0 |
| POLICYBZR | -0.3 | +0.0 | -0.0 | -0.2 | -0.1 |
| TCS | -0.3 | -0.3 | -0.1 | -0.0 | +0.1 |

## Most negatively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| GODREJPROP | -4.4 | -3.5 | -0.9 | +0.0 | -0.1 |
| JSWENERGY | -3.8 | -3.8 | -0.1 | +0.0 | +0.0 |
| IREDA | -3.8 | -3.4 | -0.5 | +0.1 | -0.0 |
| OBEROIRLTY | -3.4 | -2.9 | -0.5 | -0.0 | -0.1 |
| PRESTIGE | -3.4 | -2.7 | -0.7 | +0.1 | -0.1 |
| LODHA | -3.4 | -2.4 | -0.9 | +0.1 | -0.1 |
| M&MFIN | -3.2 | -2.5 | -0.8 | +0.1 | -0.0 |
| DLF | -3.1 | -2.5 | -0.5 | -0.0 | -0.1 |
| YESBANK | -2.9 | -1.9 | -0.8 | +0.0 | -0.1 |
| LTF | -2.9 | -2.5 | -0.6 | +0.2 | -0.0 |
| JIOFIN | -2.8 | -2.4 | -0.5 | +0.1 | -0.0 |
| SHRIRAMFIN | -2.8 | -1.7 | -0.8 | -0.2 | -0.1 |
| PFC | -2.8 | -2.8 | -0.2 | +0.1 | -0.0 |
| TATACAP | -2.8 | -2.0 | -0.9 | +0.2 | -0.1 |
| BAJFINANCE | -2.7 | -2.0 | -0.8 | +0.2 | -0.1 |

Share of absolute impact by order: 1: 77%, 2: 16%, 3: 4%, 4: 3%

## Sources
- 2026-10-21 Not A One-Off: RBI MPC Minutes Point To A Rate-Hike Cycle https://news.google.com/rss/search?q=RBI+MPC+February+2027+expectations+when:120d&hl=en-IN&gl=IN&ceid=IN:en