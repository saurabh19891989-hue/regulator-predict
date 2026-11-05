# US Q3 data: GDP 3.4%, CPI 3.7%, September payrolls only +29k (`EV_US_Q3_DATA_MIXED`)
*global_macro · status occurred · date 2026-10-29 · P(3m) 1 · P(12m) 1 · confidence high*

BEA: Q3 GDP +3.4% annualised (Q2 2.2%), led by consumer spending and AI investment (29 Oct). September CPI 3.7% y/y on gasoline (14 Oct). September payrolls +29,000, unemployment 4.2% (2 Oct) after +162k in Aug (4.1%). Strong output/high inflation/soft hiring leaves the Fed torn; October jobs report due Fri 6 Nov (date not verified).

**Already moved:** GDP +1.2pp q/q annualised acceleration; CPI 3.7%; unemployment +0.1pp.

## Entry shocks (conditional on the event)
- `F_US_GDP` US growth: 1.2 SSU (range 0.8…1.6) Q3 acceleration from 2.2% to 3.4%
- `F_FED_FUNDS` US Fed funds rate: 0.5 SSU (range 0.0…1.0) hike pricing for Dec supported by CPI/GDP, offset by weak jobs

## Causal chains (agent)
- order 2: EV_US_Q3_DATA_MIXED → F_US_GDP → C_USA — strong US demand supports export demand
- order 3: EV_US_Q3_DATA_MIXED → F_US_GDP → F_US_10Y → F_FPI_FLOWS — strong growth keeps yields high, a headwind for EM flows
- order 4: EV_US_Q3_DATA_MIXED → C_USA → F_US_TECH_SPEND → INFY — resilient US activity underpins IT services demand even as pricing falls

## Most positively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| MOTILALOFS | +5.7 | +0.0 | +2.3 | +2.3 | +1.1 |
| NAUKRI | +5.3 | +0.0 | +3.6 | +1.4 | +0.3 |
| ICICIAMC | +4.9 | +0.0 | +2.2 | +2.0 | +0.7 |
| LTM | +4.8 | +3.2 | +1.2 | +0.3 | +0.0 |
| MPHASIS | +4.5 | +3.6 | +0.5 | +0.3 | +0.0 |
| PERSISTENT | +4.4 | -0.5 | +4.6 | +0.4 | -0.1 |
| WIPRO | +4.0 | +2.6 | +1.1 | +0.2 | +0.0 |
| COFORGE | +4.0 | +2.8 | +0.9 | +0.3 | +0.1 |
| HCLTECH | +4.0 | +3.0 | +0.9 | +0.1 | -0.0 |
| PAYTM | +3.8 | +0.0 | +1.4 | +1.8 | +0.6 |
| INFY | +3.7 | +2.6 | +0.9 | +0.1 | -0.0 |
| MAHABANK | +3.4 | +0.0 | +1.4 | +1.7 | +0.3 |
| 360ONE | +3.4 | +0.0 | +0.9 | +1.9 | +0.6 |
| TMPV | +3.2 | +3.0 | +0.2 | +0.0 | +0.0 |
| JIOFIN | +3.2 | +0.0 | +1.4 | +1.6 | +0.2 |

## Most negatively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| ASTRAL | -1.6 | +0.0 | -0.9 | -0.5 | -0.2 |
| BPCL | -1.0 | +0.0 | -1.6 | +0.5 | +0.0 |
| SRF | -1.0 | +0.0 | -0.4 | -0.3 | -0.3 |
| SHRIRAMFIN | -1.0 | +0.0 | -1.0 | +0.1 | -0.1 |
| GMRAIRPORT | -0.9 | +0.0 | -0.4 | -0.4 | -0.1 |
| TATACONSUM | -0.9 | +0.0 | -0.4 | -0.5 | -0.0 |
| POWERGRID | -0.9 | +0.0 | -0.3 | -0.7 | +0.0 |
| PIDILITIND | -0.9 | +0.0 | -0.4 | -0.4 | -0.1 |
| INDIGO | -0.9 | +0.0 | -1.3 | +0.1 | +0.3 |
| TVSMOTOR | -0.8 | +0.0 | -1.3 | +0.5 | +0.1 |
| MUTHOOTFIN | -0.8 | +0.0 | -0.1 | -0.5 | -0.2 |
| AMBUJACEM | -0.8 | +0.0 | -0.4 | -0.2 | -0.2 |
| TATACAP | -0.8 | +0.0 | -0.2 | -0.1 | -0.5 |
| BOSCHLTD | -0.7 | +0.0 | -0.2 | -0.5 | -0.1 |
| UPL | -0.7 | -0.5 | +0.0 | -0.1 | -0.1 |

Share of absolute impact by order: 1: 15%, 2: 40%, 3: 32%, 4: 13%

## Sources
- 2026-10-29 US GDP growth accelerates to 3.4% in Q3 2026 - ANI/Firstpost https://news.google.com/rss/search?q=US%20GDP%20growth%20accelerates%20to%203.4%25%20in%20Q3%202026%20-%20ANI/Firstpost&hl=en-IN&gl=IN&ceid=IN:en
- 2026-10-14 Consumer prices rose 3.7% annually in September as gas prices skyrocket - CNBC https://news.google.com/rss/search?q=Consumer%20prices%20rose%203.7%25%20annually%20in%20September%20as%20gas%20prices%20skyrocket%20-%20CNBC&hl=en-IN&gl=IN&ceid=IN:en
- 2026-10-02 Labor market faltered in September as jobs increased by just 29,000 - CNBC https://news.google.com/rss/search?q=Labor%20market%20faltered%20in%20September%20as%20jobs%20increased%20by%20just%2029%2C000%20-%20CNBC&hl=en-IN&gl=IN&ceid=IN:en