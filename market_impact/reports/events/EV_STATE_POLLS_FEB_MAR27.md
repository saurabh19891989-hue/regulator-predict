# Assembly elections in UP, Punjab, Uttarakhand, Goa, Manipur (Feb-Mar 2027); status-quo outcome (NDA retains UP) (`EV_STATE_POLLS_FEB_MAR27`)
*india_macro · status scheduled · date 2027-02-20 · P(3m) 0.05 · P(12m) 0.68 · confidence low*

Five states poll Feb-March 2027 (TOI/ET 7 Sep; EC transferred officers 27 Oct; UP polls likely after board exams in Feb; Census enumeration from 25 Jan). Exact dates not announced (missing). Status-quo outcome (NDA retains UP and does not lose majority-defining ground) is my base case, P=0.68 (model judgement, no polling data fetched). Pre-poll effects: populist transfers/subsidies, fiscal slippage; Budget on 1 Feb falls into the campaign (limited tax giveaways, more rural/welfare).

## Entry shocks (conditional on the event)
- `F_RISK_SENTIMENT` Global risk aversion (VIX): -0.2 SSU (range -0.6…0.1) relief on continuity
- `F_RURAL_DEMAND` Rural consumption growth: 0.2 SSU (range 0.0…0.5) welfare transfers
- `F_GOVT_CAPEX` Central + state government capex: 0.1 SSU (range 0.0…0.3) state capex pre-poll

## Causal chains (agent)
- order 2: EV_STATE_POLLS_FEB_MAR27 → F_RURAL_DEMAND → F_AUTO_DEMAND_IN — Transfers lift rural spending
- order 3: EV_STATE_POLLS_FEB_MAR27 → F_RURAL_DEMAND → F_AUTO_DEMAND_IN → M&M — Tractor/utility vehicle demand
- order 3: EV_STATE_POLLS_FEB_MAR27 → F_GOVT_CAPEX → P_INFRA_SPENDING_ROADS → ULTRACEMCO — State infra spending lifts cement/roads
- order 3: EV_STATE_POLLS_FEB_MAR27 → F_RISK_SENTIMENT → F_FPI_FLOWS → F_USDINR — Policy continuity supports flows/rupee

## Most positively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| INDUSINDBK | +2.9 | +0.7 | +1.5 | +0.8 | -0.1 |
| IDFCFIRSTB | +2.5 | +0.6 | +1.3 | +0.6 | -0.1 |
| MAHABANK | +2.0 | +0.9 | +0.7 | +0.4 | -0.0 |
| INDIANB | +1.9 | +0.8 | +0.8 | +0.4 | -0.0 |
| YESBANK | +1.8 | +0.0 | +1.3 | +0.6 | -0.1 |
| BANKINDIA | +1.8 | +0.5 | +0.9 | +0.5 | -0.0 |
| IREDA | +1.8 | +1.0 | +0.3 | +0.5 | -0.1 |
| ICICIAMC | +1.8 | +0.8 | +0.7 | +0.2 | +0.0 |
| MOTILALOFS | +1.7 | +0.7 | +0.6 | +0.3 | +0.1 |
| KOTAKBANK | +1.7 | +0.4 | +0.8 | +0.4 | -0.0 |
| AXISBANK | +1.6 | +0.3 | +0.8 | +0.5 | -0.0 |
| FEDERALBNK | +1.6 | +0.3 | +0.4 | +0.8 | +0.0 |
| TMCV | +1.5 | +0.4 | +1.1 | +0.0 | -0.0 |
| SBIN | +1.5 | +0.3 | +0.8 | +0.4 | -0.0 |
| MEESHO | +1.5 | +1.2 | +0.1 | +0.1 | +0.0 |

## Most negatively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| OIL | -0.2 | +0.0 | -0.1 | -0.1 | -0.0 |
| NATIONALUM | -0.2 | +0.0 | -0.1 | -0.0 | -0.0 |
| HINDZINC | -0.1 | +0.0 | -0.1 | -0.1 | -0.0 |
| ONGC | -0.1 | +0.0 | -0.0 | -0.0 | -0.0 |
| SRF | -0.1 | +0.0 | +0.0 | -0.1 | -0.0 |
| SUNPHARMA | -0.1 | +0.0 | -0.0 | -0.0 | -0.0 |
| COALINDIA | -0.0 | +0.0 | -0.0 | -0.0 | -0.0 |
| UPL | -0.0 | +0.0 | -0.0 | -0.0 | -0.0 |
| DRREDDY | -0.0 | +0.0 | -0.0 | +0.0 | -0.0 |
| PREMIERENE | -0.0 | +0.0 | +0.0 | -0.0 | -0.0 |
| NMDC | -0.0 | +0.1 | -0.0 | -0.0 | -0.0 |
| TCS | -0.0 | +0.1 | +0.0 | -0.1 | -0.0 |
| SUZLON | -0.0 | +0.0 | +0.0 | -0.0 | -0.0 |
| TECHM | -0.0 | +0.1 | +0.0 | -0.1 | -0.0 |
| GRASIM | +0.0 | +0.0 | +0.0 | -0.0 | +0.0 |

Share of absolute impact by order: 1: 33%, 2: 39%, 3: 23%, 4: 4%

## Sources
- 2026-09-07 5 poll-bound states set to vote in February-March - Times of India https://news.google.com/rss/search?q=5+poll-bound+states+set+to+vote+in+February-March+when:120d&hl=en-IN&gl=IN&ceid=IN:en
- 2026-10-27 EC orders transfer of election-related officers in five states - New Indian Express https://news.google.com/rss/search?q=EC+orders+transfer+of+election-related+officers+five+states+2027+when:120d&hl=en-IN&gl=IN&ceid=IN:en
- 2026-10-13 UP assembly elections likely after Board Exams in February 2027 - The Statesman https://news.google.com/rss/search?q=UP+assembly+elections+likely+after+Board+Exams+February+2027+when:120d&hl=en-IN&gl=IN&ceid=IN:en