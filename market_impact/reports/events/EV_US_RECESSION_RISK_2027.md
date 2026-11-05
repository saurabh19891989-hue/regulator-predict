# US recession (two negative quarters or NBER-style) beginning by mid-2027 (`EV_US_RECESSION_RISK_2027`)
*global_macro · status risk_scenario · date 2027-06-30 · P(3m) 0.06 · P(12m) 0.25 · confidence low*

Weak Sep payrolls (+29k), 4.2% unemployment, oil shock, Fed hikes, AI-capex dependence of GDP (Q3 3.4% 'AI investment' led) and yields at 19-year highs raise risk. 'Brutal AI selloff stirs recession fears' (Reuters 2 Nov). P(by 3m)=0.06, by 12m 0.25 (our estimate; consensus not verified).

**Already moved:** n/a

## Entry shocks (conditional on the event)
- `F_US_GDP` US growth: -3.0 SSU (range -4.5…-1.5) -3 pp vs trend
- `F_US_EQUITIES` US equity market: -3.0 SSU (range -5.0…-1.5) -15%
- `F_FED_FUNDS` US Fed funds rate: -3.0 SSU (range -5.0…-1.0) Fed cuts 75 bp

## Causal chains (agent)
- order 2: EV_US_RECESSION_RISK_2027 → F_US_GDP → C_USA — US demand falls
- order 3: EV_US_RECESSION_RISK_2027 → C_USA → F_US_TECH_SPEND — IT/pharma export demand
- order 4: EV_US_RECESSION_RISK_2027 → F_US_GDP → F_FED_FUNDS → F_US_10Y → F_FPI_FLOWS — later: lower yields help EM

## Most positively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| ASTRAL | +5.4 | +0.0 | +4.1 | +0.4 | +0.8 |
| SWIGGY | +4.5 | +7.5 | -2.1 | -0.9 | -0.0 |
| BSE | +4.3 | +4.5 | -0.0 | -0.5 | +0.3 |
| UPL | +3.7 | +3.0 | +0.0 | +0.6 | +0.1 |
| SRF | +3.2 | +0.0 | +1.3 | +1.5 | +0.4 |
| SHRIRAMFIN | +3.0 | +0.0 | +1.3 | +0.8 | +0.9 |
| HINDZINC | +3.0 | +0.0 | +0.0 | +1.0 | +2.0 |
| TATACONSUM | +3.0 | +0.0 | +2.1 | +0.6 | +0.3 |
| POWERGRID | +2.8 | +0.0 | +0.9 | +1.6 | +0.3 |
| AMBUJACEM | +2.4 | +0.0 | +1.2 | +0.5 | +0.8 |
| BPCL | +2.4 | +0.0 | +4.1 | -1.7 | +0.1 |
| PIDILITIND | +2.4 | +0.0 | +1.3 | +0.6 | +0.5 |
| GMRAIRPORT | +2.3 | +0.0 | -0.2 | +1.4 | +1.1 |
| BOSCHLTD | +2.2 | +0.0 | +0.5 | +1.4 | +0.3 |
| TVSMOTOR | +2.1 | +0.0 | +2.0 | +0.0 | +0.1 |

## Most negatively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| LTM | -14.8 | -12.3 | -2.7 | +0.4 | -0.2 |
| NAUKRI | -14.8 | -7.5 | -7.1 | -0.1 | -0.1 |
| MOTILALOFS | -14.0 | -4.5 | -8.0 | -1.1 | -0.4 |
| 360ONE | -13.7 | +0.0 | -10.4 | -2.2 | -1.1 |
| MPHASIS | -13.1 | -12.3 | -1.0 | +0.3 | -0.2 |
| WIPRO | -12.7 | -10.5 | -2.4 | +0.4 | -0.2 |
| JIOFIN | -12.5 | +0.0 | -12.7 | +1.0 | -0.9 |
| COFORGE | -12.4 | -10.2 | -2.2 | +0.2 | -0.2 |
| MAHABANK | -12.1 | +0.0 | -11.2 | -0.2 | -0.7 |
| HCLTECH | -11.9 | -10.8 | -1.4 | +0.5 | -0.2 |
| ICICIAMC | -11.8 | -3.0 | -8.4 | +0.3 | -0.8 |
| MEESHO | -11.8 | +0.0 | -10.2 | -0.6 | -1.0 |
| INDUSINDBK | -11.3 | +0.0 | -10.4 | -0.8 | -0.2 |
| INFY | -11.1 | -9.9 | -1.5 | +0.5 | -0.1 |
| IREDA | -11.0 | +0.0 | -11.8 | +1.2 | -0.3 |

Share of absolute impact by order: 1: 21%, 2: 58%, 3: 13%, 4: 8%

## Sources
- 2026-11-02 COMMENTARY: Brutal AI selloff stirs recession fears - Reuters https://news.google.com/rss/search?q=COMMENTARY%3A%20Brutal%20AI%20selloff%20stirs%20recession%20fears%20-%20Reuters&hl=en-IN&gl=IN&ceid=IN:en
- 2026-10-02 US job growth undershoots expectations in September - Reuters https://news.google.com/rss/search?q=US%20job%20growth%20undershoots%20expectations%20in%20September%20-%20Reuters&hl=en-IN&gl=IN&ceid=IN:en