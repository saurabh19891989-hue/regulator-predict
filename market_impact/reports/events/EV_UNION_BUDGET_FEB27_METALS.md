# Union Budget 2027-28 (1 Feb 2027): customs-duty relief on coking coal/critical minerals/scrap vs. higher protection (`EV_UNION_BUDGET_FEB27_METALS`)
*metals_china · status scheduled · date 2027-02-01 · P(3m) 0.35 · P(12m) 0.35 · confidence low*

Budget presented on 1 Feb 2027 (date per convention, not verified). ET (2 Nov): fiscal deficit may overshoot FY27 target by up to Rs 1.2 lakh crore, limiting giveaways; Voice Gambia/ET (27 Oct) reports plans for new duties on plastics, used tyres and scrap metal. Metals-relevant outcomes: (a) cut on coking coal/ferro-alloy/critical-mineral duties (prob 0.35), (b) higher duty on scrap/steel inputs, (c) mining royalty/NMDC dividend and rare-earth mission funding. Modelled as the ~0.35 chance of input-duty relief; opposite case is the status quo.

**Review override applied:** The event's own description models 'the ~0.35 chance of input-duty relief', yet it is entered with p=0.85/0.9 and a -0.3 SSU (-4.5%) coking-coal shock. The only lever is the 2.5% basic customs duty: cut to nil on 22 May 2022 (Notification 26/2022-Customs) and restored to 2.5% in Nov 2022, and industry still lobbies for abolition (GMK). Removing it lowers landed cost ~2.4%. Fix: p = 0.35 and shock -0.17. This removes ~+2 pp of 12m forward exposure (and ~+1.9 pp of 3m) from each integrated mill (JINDALSTEL, SAIL; TATASTEEL ~+1).

## Entry shocks (conditional on the event)
- `F_COKING_COAL` Coking coal price: -0.17 SSU (range -0.17…-0.08) BCD on coking coal 2.5% -> nil = -2.4% landed cost (-0.16 SSU)
- `P_MINING_ROYALTY` Mining royalty / mineral tax burden: 0.0 SSU (range -0.3…0.3) 

## Causal chains (agent)
- order 2: EV_UNION_BUDGET_FEB27_METALS → F_COKING_COAL → JSWSTEEL — Lower landed coking-coal cost raises margin.
- order 3: EV_UNION_BUDGET_FEB27_METALS → F_COKING_COAL → F_STEEL_INDIA → LT — Lower cost-push moderates steel prices.
- order 4: EV_UNION_BUDGET_FEB27_METALS → F_STEEL_INDIA → F_CPI_IN — Minor CPI effect.

## Most positively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| SAIL | +1.0 | +1.4 | -0.3 | -0.2 | +0.0 |
| JSWSTEEL | +0.7 | +0.9 | -0.2 | -0.1 | +0.0 |
| JINDALSTEL | +0.4 | +0.8 | -0.2 | -0.2 | +0.0 |
| TATASTEEL | +0.4 | +0.7 | -0.2 | -0.1 | +0.0 |
| TMCV | +0.1 | +0.0 | +0.1 | +0.0 | +0.0 |
| BHEL | +0.1 | +0.0 | +0.1 | +0.0 | +0.0 |
| MARUTI | +0.1 | +0.0 | +0.1 | +0.0 | +0.0 |
| ASHOKLEY | +0.1 | +0.0 | +0.1 | +0.0 | +0.0 |
| SUZLON | +0.1 | +0.0 | +0.1 | +0.0 | +0.0 |
| COCHINSHIP | +0.1 | +0.0 | +0.1 | +0.0 | +0.0 |
| HYUNDAI | +0.1 | +0.0 | +0.1 | +0.0 | +0.0 |
| RVNL | +0.1 | +0.0 | +0.1 | +0.0 | +0.0 |
| TIINDIA | +0.1 | +0.0 | +0.0 | +0.0 | +0.0 |
| TVSMOTOR | +0.1 | +0.0 | +0.0 | +0.0 | +0.0 |
| TMPV | +0.1 | +0.0 | +0.1 | +0.0 | +0.0 |

## Most negatively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| COALINDIA | -0.1 | -0.1 | +0.0 | +0.0 | +0.0 |
| NMDC | -0.1 | +0.0 | -0.1 | -0.0 | +0.0 |
| APLAPOLLO | -0.1 | +0.0 | -0.1 | -0.0 | -0.0 |
| M&MFIN | -0.0 | +0.0 | -0.0 | +0.0 | +0.0 |
| LTF | -0.0 | +0.0 | -0.0 | +0.0 | +0.0 |
| CHOLAFIN | -0.0 | +0.0 | -0.0 | +0.0 | +0.0 |
| BANKINDIA | -0.0 | +0.0 | +0.0 | +0.0 | -0.0 |
| HINDCOPPER | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| HINDZINC | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| NATIONALUM | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| NLCINDIA | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| VAML | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| VEDL | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| SBIN | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| IREDA | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |

Share of absolute impact by order: 1: 52%, 2: 30%, 3: 17%, 4: 1%

## Sources
- 2026-11-02 Fiscal deficit likely to exceed FY27 target by up to Rs 1.2 lakh crore https://news.google.com/rss/search?q=Fiscal+deficit+likely+to+exceed+FY27+target+by+up+to+Rs+1.2+lakh+crore&hl=en-IN&gl=IN&ceid=IN:en
- 2026-10-27 Government Plans New Duties on Plastics, Used Tyres and Scrap Metal https://news.google.com/rss/search?q=Government+Plans+New+Duties+on+Plastics,+Used+Tyres+and+Scrap+Metal&hl=en-IN&gl=IN&ceid=IN:en