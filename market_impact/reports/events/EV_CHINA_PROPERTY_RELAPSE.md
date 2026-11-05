# China property-sector credit event / sharp relapse (large developer or LGFV default) (`EV_CHINA_PROPERTY_RELAPSE`)
*metals_china · status risk_scenario · date 2027-01-15 · P(3m) 0.05 · P(12m) 0.1 · confidence low*

China's property bust continues to drain local finances (EAF 4 Oct); sales recovery after the stimulus is only 'modest' (Bloomberg 8 Oct). A disorderly default would push iron ore, copper, steel and the yuan down and risk-off globally. Low odds given policy backstops.

## Entry shocks (conditional on the event)
- `F_CHINA_GDP` China growth / stimulus: -0.8 SSU (range -1.5…-0.3) growth hit
- `F_IRON_ORE` Iron ore price: -1.3 SSU (range -2.5…-0.6) -20%
- `F_RISK_SENTIMENT` Global risk aversion (VIX): 1.2 SSU (range 0.5…2.5) VIX +6

## Causal chains (agent)
- order 2: EV_CHINA_PROPERTY_RELAPSE → F_CHINA_GDP → F_IRON_ORE → NMDC — Ore price drops.
- order 3: EV_CHINA_PROPERTY_RELAPSE → F_IRON_ORE → F_STEEL_GLOBAL → F_STEEL_INDIA — Lower global steel; Chinese exports rise.
- order 4: EV_CHINA_PROPERTY_RELAPSE → F_RISK_SENTIMENT → F_FPI_FLOWS → F_USDINR — Risk-off hits Indian flows and the rupee.

## Most positively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| JSWSTEEL | +1.7 | +2.0 | +2.1 | -1.7 | -0.6 |
| ASHOKLEY | +1.7 | +0.0 | +0.8 | +0.6 | +0.2 |
| JINDALSTEL | +1.5 | +2.4 | +2.1 | -2.4 | -0.6 |
| MARUTI | +1.4 | +0.0 | +0.7 | +0.6 | +0.2 |
| VOLTAS | +1.3 | +0.0 | +1.3 | +0.0 | -0.0 |
| TMPV | +1.2 | -0.5 | +1.4 | +0.2 | +0.1 |
| TATACONSUM | +1.1 | +1.0 | +0.1 | +0.0 | +0.0 |
| MRF | +1.0 | +0.0 | +0.7 | +0.2 | +0.1 |
| POWERGRID | +0.9 | +1.1 | -0.1 | -0.1 | -0.0 |
| TMCV | +0.9 | +0.0 | +0.2 | +0.6 | +0.2 |
| ASTRAL | +0.9 | +1.0 | -0.1 | +0.0 | +0.0 |
| SUZLON | +0.9 | +0.0 | +0.2 | +0.5 | +0.1 |
| BPCL | +0.8 | +0.0 | +1.2 | -0.4 | +0.0 |
| AMBUJACEM | +0.8 | +0.0 | +0.7 | +0.0 | +0.0 |
| M&M | +0.7 | +0.0 | +0.4 | +0.2 | +0.1 |

## Most negatively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| NMDC | -11.7 | -11.7 | +0.4 | -0.3 | -0.1 |
| JIOFIN | -6.5 | -6.0 | -0.2 | -0.3 | -0.0 |
| IREDA | -6.4 | -6.0 | -0.2 | -0.2 | +0.1 |
| MOTILALOFS | -5.9 | -4.2 | -0.9 | -0.7 | -0.1 |
| ICICIAMC | -5.8 | -4.8 | -0.6 | -0.4 | +0.0 |
| MEESHO | -5.1 | -4.8 | +0.1 | -0.4 | -0.0 |
| 360ONE | -5.0 | -4.2 | -0.2 | -0.5 | -0.1 |
| INDUSINDBK | -4.5 | -4.2 | -0.3 | -0.2 | +0.2 |
| MAHABANK | -4.4 | -4.2 | -0.2 | -0.1 | +0.1 |
| LICI | -4.4 | -4.2 | -0.1 | -0.1 | +0.0 |
| NAUKRI | -4.0 | -3.0 | -0.9 | -0.2 | +0.0 |
| LENSKART | -4.0 | -3.6 | -0.2 | -0.2 | +0.0 |
| IDFCFIRSTB | -3.9 | -3.6 | -0.2 | -0.1 | +0.1 |
| INDIANB | -3.8 | -3.6 | -0.2 | -0.0 | +0.0 |
| VAML | -3.5 | -1.0 | -2.8 | +0.3 | +0.0 |

Share of absolute impact by order: 1: 50%, 2: 29%, 3: 18%, 4: 4%

## Sources
- 2026-10-04 The fiscal fallout from China's property bust https://news.google.com/rss/search?q=The+fiscal+fallout+from+China's+property+bust&hl=en-IN&gl=IN&ceid=IN:en
- 2026-10-08 China Home Sales Post Modest Recovery After Latest Stimulus https://news.google.com/rss/search?q=China+Home+Sales+Post+Modest+Recovery+After+Latest+Stimulus&hl=en-IN&gl=IN&ceid=IN:en