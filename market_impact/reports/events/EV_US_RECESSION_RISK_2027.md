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
| SWIGGY | +5.3 | +7.5 | -2.1 | +0.0 | -0.1 |
| BSE | +4.5 | +4.5 | -0.7 | -0.1 | +0.8 |
| UPL | +3.6 | +3.0 | +0.0 | +0.5 | +0.0 |
| BPCL | +3.2 | +0.0 | +4.1 | -1.0 | +0.1 |
| ASTRAL | +3.1 | +0.0 | +2.5 | +0.4 | +0.2 |
| SRF | +2.3 | +0.0 | +1.3 | +0.9 | +0.1 |
| HINDZINC | +1.9 | +0.0 | +0.0 | +0.7 | +1.2 |
| POWERGRID | +1.6 | +0.0 | -0.3 | +1.6 | +0.3 |
| HINDPETRO | +1.6 | +0.0 | +2.2 | -0.7 | +0.2 |
| TATACONSUM | +1.6 | +0.0 | +0.9 | +0.5 | +0.1 |
| PIDILITIND | +1.6 | +0.0 | +1.3 | +0.2 | +0.1 |
| BOSCHLTD | +1.5 | +0.0 | +0.5 | +0.8 | +0.1 |
| MUTHOOTFIN | +1.5 | +0.0 | -1.4 | +2.3 | +0.6 |
| AMBUJACEM | +1.4 | +0.0 | +1.2 | +0.0 | +0.2 |
| MARUTI | +1.4 | +0.0 | +1.2 | +0.1 | +0.1 |

## Most negatively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| LTM | -13.7 | -12.3 | -1.6 | +0.4 | -0.2 |
| MPHASIS | -12.5 | -12.3 | -0.5 | +0.4 | -0.2 |
| NAUKRI | -12.4 | -7.5 | -5.3 | +0.7 | -0.3 |
| WIPRO | -11.8 | -10.5 | -1.6 | +0.4 | -0.2 |
| COFORGE | -11.5 | -10.2 | -1.5 | +0.4 | -0.2 |
| HCLTECH | -11.4 | -10.8 | -0.7 | +0.3 | -0.2 |
| INFY | -10.5 | -9.9 | -0.8 | +0.3 | -0.1 |
| PERSISTENT | -10.2 | -3.0 | -7.5 | +0.5 | -0.3 |
| MOTILALOFS | -9.7 | -4.5 | -5.5 | +0.7 | -0.3 |
| OFSS | -7.8 | -6.9 | -1.1 | +0.4 | -0.1 |
| TMPV | -7.7 | -7.5 | -0.3 | +0.4 | -0.2 |
| ICICIAMC | -7.7 | -3.0 | -5.5 | +1.4 | -0.6 |
| TECHM | -7.3 | -2.4 | -5.1 | +0.4 | -0.2 |
| CUMMINSIND | -6.9 | -6.9 | +0.4 | -0.3 | -0.0 |
| TCS | -6.8 | -1.5 | -5.5 | +0.3 | -0.1 |

Share of absolute impact by order: 1: 27%, 2: 50%, 3: 18%, 4: 5%

## Sources
- 2026-11-02 COMMENTARY: Brutal AI selloff stirs recession fears - Reuters https://news.google.com/rss/search?q=COMMENTARY%3A%20Brutal%20AI%20selloff%20stirs%20recession%20fears%20-%20Reuters&hl=en-IN&gl=IN&ceid=IN:en
- 2026-10-02 US job growth undershoots expectations in September - Reuters https://news.google.com/rss/search?q=US%20job%20growth%20undershoots%20expectations%20in%20September%20-%20Reuters&hl=en-IN&gl=IN&ceid=IN:en