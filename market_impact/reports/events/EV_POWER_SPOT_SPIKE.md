# Indian spot power: IEX prices hit Rs20/unit ceiling (19 Sep), Q2 prices up ~46% y/y; El Nino lifts demand (`EV_POWER_SPOT_SPIKE`)
*energy · status occurred · date 2026-09-19 · P(3m) 1 · P(12m) 1 · confidence medium*

IEX day-ahead prices hit the Rs20/kWh ceiling on 19 Sep (ET); Business Standard (6 Oct) said spot prices doubled amid demand surge and coal crunch; another headline put Q2 price rise at 46%. IEX Q2 volume 39,685 MU (+12.7% y/y), H1 FY27 77.2 BU (+14.2%), RTM share 41%, October volume +16.5% y/y; Q2 PAT Rs139 cr (+13%). Peak demand eased to 234 GW in first half of October (TradingView 26 Oct). El Nino/'super El Nino' flagged for winter and summer 2027 (TOI/ET 14 Oct); discoms turning to spot (The Core 21 Oct).

**Already moved:** IEX volumes +12.7% Q2; price series not available in factor_state.

## Entry shocks (conditional on the event)
- `F_POWER_PRICE_IN` Indian power exchange (IEX) prices: 3.0 SSU (range 2.0…6.0) +46% y/y to ~doubling on peak weeks, in units of +15%
- `F_POWER_DEMAND_IN` Indian electricity demand: 1.0 SSU (range 0.5…1.5) demand growth above trend; exact y/y not verified

## Causal chains (agent)
- order 2: EV_POWER_SPOT_SPIKE → F_POWER_PRICE_IN → NTPC — merchant exposure of generators
- order 3: EV_POWER_SPOT_SPIKE → F_POWER_PRICE_IN → P_POWER_REFORM — price shocks add urgency to market reform, cap and discom payment rules
- order 4: EV_POWER_SPOT_SPIKE → F_POWER_PRICE_IN → F_COAL_INDIA → COALINDIA — higher spot price raises willingness-to-pay for e-auction coal

## Most positively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| ADANIPOWER | +8.3 | +8.5 | -0.2 | +0.0 | +0.0 |
| JSWENERGY | +6.5 | +6.6 | -0.1 | +0.0 | +0.0 |
| TATAPOWER | +3.8 | +3.6 | +0.2 | +0.0 | +0.0 |
| ENRIN | +3.7 | +3.0 | +0.7 | +0.0 | +0.0 |
| ADANIENSOL | +3.3 | +2.7 | +0.6 | +0.0 | +0.0 |
| ADANIGREEN | +3.3 | +3.3 | +0.0 | +0.0 | +0.0 |
| COALINDIA | +3.3 | +2.8 | +0.5 | +0.0 | +0.0 |
| BHEL | +3.2 | +3.0 | +0.2 | +0.0 | +0.0 |
| NLCINDIA | +2.5 | +2.5 | +0.0 | +0.0 | +0.0 |
| IREDA | +2.5 | +2.5 | +0.0 | +0.0 | +0.0 |
| NTPC | +2.2 | +2.2 | +0.0 | +0.0 | +0.0 |
| RECLTD | +2.0 | +2.0 | +0.0 | +0.0 | +0.0 |
| WAAREEENER | +2.0 | +2.0 | +0.0 | +0.0 | +0.0 |
| POWERGRID | +1.9 | +1.5 | +0.4 | +0.0 | +0.0 |
| POWERINDIA | +1.9 | +0.0 | +1.9 | +0.0 | +0.0 |

## Most negatively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| VAML | -2.8 | -2.4 | -0.4 | +0.0 | +0.0 |
| IDEA | -2.4 | -2.4 | +0.0 | +0.0 | +0.0 |
| JINDALSTEL | -2.2 | -1.8 | -0.4 | +0.0 | +0.0 |
| TATACOMM | -2.1 | -2.1 | +0.0 | +0.0 | +0.0 |
| INDUSTOWER | -1.5 | -1.5 | +0.0 | +0.0 | +0.0 |
| HINDZINC | -1.1 | -0.9 | -0.2 | +0.0 | +0.0 |
| VEDL | -0.6 | +0.0 | -0.5 | -0.1 | +0.0 |
| HINDALCO | -0.3 | +0.0 | -0.3 | +0.0 | +0.0 |
| GAIL | +0.4 | +0.4 | +0.0 | +0.0 | +0.0 |
| NATIONALUM | +0.6 | +0.9 | -0.3 | +0.0 | +0.0 |
| NHPC | +0.6 | +0.6 | +0.0 | +0.0 | +0.0 |
| ABB | +0.6 | +0.0 | +0.6 | +0.0 | +0.0 |
| APARINDS | +1.0 | +0.0 | +1.0 | +0.0 | +0.0 |
| KEI | +1.0 | +0.0 | +1.0 | +0.0 | +0.0 |
| POLYCAB | +1.0 | +0.0 | +1.0 | +0.0 | +0.0 |

Share of absolute impact by order: 1: 83%, 2: 17%, 3: 0%, 4: 0%

## Sources
- 2026-09-19 IEX power prices hit Rs20/unit ceiling (ET) (headline via Google News RSS; article body not read) https://news.google.com/rss/search?q=IEX+power+prices+hit+Rs+20+ceiling+when:120d&hl=en-IN&gl=IN&ceid=IN:en
- 2026-10-06 IEX Q2 volume +12.7% (Business Standard) (headline via Google News RSS; article body not read) https://news.google.com/rss/search?q=IEX+Q2+electricity+traded+volume+12.7%+when:120d&hl=en-IN&gl=IN&ceid=IN:en
- 2026-10-26 Peak power demand eases to 234 GW (TradingView) (headline via Google News RSS; article body not read) https://news.google.com/rss/search?q=Peak+power+demand+234+GW+first+half+October+when:120d&hl=en-IN&gl=IN&ceid=IN:en