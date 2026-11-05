# Union Budget 2027-28 (1 Feb 2027): customs-duty relief on coking coal/critical minerals/scrap vs. higher protection (`EV_UNION_BUDGET_FEB27_METALS`)
*metals_china · status scheduled · date 2027-02-01 · P(3m) 0.85 · P(12m) 0.9 · confidence low*

Budget presented on 1 Feb 2027 (date per convention, not verified). ET (2 Nov): fiscal deficit may overshoot FY27 target by up to Rs 1.2 lakh crore, limiting giveaways; Voice Gambia/ET (27 Oct) reports plans for new duties on plastics, used tyres and scrap metal. Metals-relevant outcomes: (a) cut on coking coal/ferro-alloy/critical-mineral duties (prob 0.35), (b) higher duty on scrap/steel inputs, (c) mining royalty/NMDC dividend and rare-earth mission funding. Modelled as the ~0.35 chance of input-duty relief; opposite case is the status quo.

## Entry shocks (conditional on the event)
- `F_COKING_COAL` Coking coal price: -0.3 SSU (range -0.6…0.0) landed cost after duty cut
- `P_MINING_ROYALTY` Mining royalty / mineral tax burden: 0.0 SSU (range -0.2…0.2) no change

## Causal chains (agent)
- order 2: EV_UNION_BUDGET_FEB27_METALS → F_COKING_COAL → JSWSTEEL — Lower landed coking-coal cost raises margin.
- order 3: EV_UNION_BUDGET_FEB27_METALS → F_COKING_COAL → F_STEEL_INDIA → LT — Lower cost-push moderates steel prices.
- order 4: EV_UNION_BUDGET_FEB27_METALS → F_STEEL_INDIA → F_CPI_IN — Minor CPI effect.

## Most positively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| SAIL | +1.7 | +2.4 | -0.4 | -0.3 | +0.0 |
| JINDALSTEL | +1.5 | +2.2 | -0.5 | -0.3 | +0.0 |
| JSWSTEEL | +1.2 | +1.6 | -0.3 | -0.2 | +0.0 |
| TATASTEEL | +0.7 | +1.2 | -0.3 | -0.2 | +0.0 |
| TMPV | +0.3 | +0.0 | +0.3 | +0.0 | +0.0 |
| TMCV | +0.2 | +0.0 | +0.1 | +0.1 | +0.0 |
| BHEL | +0.2 | +0.0 | +0.1 | +0.1 | +0.0 |
| MARUTI | +0.2 | +0.0 | +0.1 | +0.1 | +0.0 |
| SUZLON | +0.2 | +0.0 | +0.1 | +0.1 | +0.0 |
| ASHOKLEY | +0.2 | +0.0 | +0.1 | +0.1 | +0.0 |
| RVNL | +0.2 | +0.0 | +0.1 | +0.1 | +0.0 |
| COCHINSHIP | +0.1 | +0.0 | +0.1 | +0.1 | +0.0 |
| HYUNDAI | +0.1 | +0.0 | +0.1 | +0.1 | +0.0 |
| TIINDIA | +0.1 | +0.0 | +0.1 | +0.1 | +0.0 |
| TVSMOTOR | +0.1 | +0.0 | +0.1 | +0.1 | +0.0 |

## Most negatively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| COALINDIA | -0.2 | -0.2 | +0.0 | +0.0 | +0.0 |
| NMDC | -0.2 | +0.0 | -0.1 | -0.1 | +0.0 |
| APLAPOLLO | -0.2 | +0.0 | -0.1 | -0.1 | +0.0 |
| CHOLAFIN | -0.1 | +0.0 | -0.1 | +0.0 | +0.0 |
| M&MFIN | -0.1 | +0.0 | -0.1 | +0.0 | +0.0 |
| LTF | -0.0 | +0.0 | -0.0 | +0.0 | +0.0 |
| BANKINDIA | -0.0 | +0.0 | +0.0 | +0.0 | -0.0 |
| MAHABANK | -0.0 | +0.0 | +0.0 | +0.0 | -0.0 |
| HINDCOPPER | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| HINDZINC | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| NATIONALUM | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| VAML | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| VEDL | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| SBIN | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| ADANIPOWER | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |

Share of absolute impact by order: 1: 53%, 2: 29%, 3: 16%, 4: 2%

## Sources
- 2026-11-02 Fiscal deficit likely to exceed FY27 target by up to Rs 1.2 lakh crore https://news.google.com/rss/search?q=Fiscal+deficit+likely+to+exceed+FY27+target+by+up+to+Rs+1.2+lakh+crore&hl=en-IN&gl=IN&ceid=IN:en
- 2026-10-27 Government Plans New Duties on Plastics, Used Tyres and Scrap Metal https://news.google.com/rss/search?q=Government+Plans+New+Duties+on+Plastics,+Used+Tyres+and+Scrap+Metal&hl=en-IN&gl=IN&ceid=IN:en