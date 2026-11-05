# CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`)
*india_macro · status occurred · date 2026-10-12 · P(3m) 1 · P(12m) 1 · confidence high*

Retail inflation (new base 2024=100) rose 4.38% (Jun) -> 4.45% (Jul) -> 4.82% (Aug) -> 5.54% (Sep), above poll estimates and nearing the 6% upper tolerance band; food inflation 7.74% (Jul: 5.52%); price pressures broadening to core. RBI projects FY27 core at 4.4% (vs 4.3%); its August headline FY27 projection was 5.0%; the October headline projection was not retrieved. Drivers: oil (Brent ~US$95), onions/vegetables, weak monsoon, rupee. October CPI is due about 12 Nov.

**Already moved:** Rate pricing: Reuters/Bloomberg (7 Oct) back-to-back hike expectations; 10y G-sec +44 bp since 11 Sep.

## Entry shocks (conditional on the event)
- `F_CPI_IN` India CPI inflation: 1.15 SSU (range 1.0…1.3) 4.38% -> 5.54% since June
- `F_FOOD_INFLATION_IN` India food inflation: 1.1 SSU (range 0.9…1.3) +2.2 pp in two months (Jul 5.52% -> Sep 7.74%)

## Causal chains (agent)
- order 2: EV_CPI_REACCEL_SEP26 → F_CPI_IN → F_REPO_IN — Reaction function: inflation toward 6% drives further tightening
- order 3: EV_CPI_REACCEL_SEP26 → F_CPI_IN → F_REPO_IN → F_HOUSING_DEMAND — Further hikes depress housing demand
- order 4: EV_CPI_REACCEL_SEP26 → F_FOOD_INFLATION_IN → F_RURAL_DEMAND → F_AUTO_DEMAND_IN → M&M — Food-price squeeze on rural real incomes (net food buyers) hits two-wheeler/tractor/SUV demand
- order 4: EV_CPI_REACCEL_SEP26 → F_CPI_IN → F_REPO_IN → F_GSEC_10Y_IN → F_CREDIT_SPREADS_IN — Policy-path repricing lifts yields and spreads

## Most positively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| PIIND | +0.2 | +0.0 | +0.4 | -0.1 | -0.0 |
| UPL | +0.1 | +0.0 | +0.2 | -0.1 | -0.0 |
| MCX | -0.0 | +0.0 | +0.3 | -0.2 | -0.1 |
| NATIONALUM | -0.3 | +0.0 | +0.0 | -0.3 | -0.0 |
| PAYTM | -0.3 | +0.0 | +0.3 | -0.7 | +0.1 |
| HINDCOPPER | -0.4 | +0.0 | +0.0 | -0.4 | -0.0 |
| OIL | -0.4 | +0.0 | +0.0 | -0.4 | -0.0 |
| SUNPHARMA | -0.5 | +0.0 | +0.2 | -0.6 | -0.1 |
| NMDC | -0.5 | +0.0 | -0.3 | -0.1 | -0.1 |
| LTM | -0.6 | +0.0 | +0.3 | -0.8 | -0.1 |
| VAML | -0.6 | +0.0 | +0.5 | -0.9 | -0.2 |
| ONGC | -0.6 | +0.0 | -0.1 | -0.5 | -0.0 |
| LUPIN | -0.6 | +0.0 | -0.2 | -0.4 | -0.1 |
| MPHASIS | -0.6 | +0.0 | +0.2 | -0.8 | -0.1 |
| HCLTECH | -0.6 | +0.0 | +0.1 | -0.7 | -0.1 |

## Most negatively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| YESBANK | -12.2 | +0.0 | -6.1 | -5.5 | -0.5 |
| BAJFINANCE | -11.2 | +0.0 | -6.1 | -4.6 | -0.5 |
| TATACAP | -10.9 | +0.0 | -5.4 | -5.2 | -0.3 |
| GMRAIRPORT | -9.4 | +0.0 | -5.4 | -3.5 | -0.5 |
| PRESTIGE | -9.2 | +0.0 | -5.7 | -2.9 | -0.6 |
| SHRIRAMFIN | -8.6 | +0.0 | -3.8 | -4.3 | -0.4 |
| GODREJPROP | -8.2 | +0.0 | -4.9 | -2.5 | -0.8 |
| IREDA | -8.1 | +0.0 | -4.3 | -3.6 | -0.2 |
| AUBANK | -8.0 | +0.0 | -4.7 | -3.6 | +0.3 |
| LODHA | -7.9 | +0.0 | -4.5 | -2.6 | -0.8 |
| BAJAJFINSV | -7.5 | +0.0 | -4.0 | -3.2 | -0.4 |
| IDFCFIRSTB | -7.2 | +0.0 | -3.1 | -4.0 | -0.1 |
| JSWENERGY | -7.2 | +0.0 | -4.8 | -2.2 | -0.2 |
| JIOFIN | -6.8 | +0.0 | -3.0 | -3.4 | -0.4 |
| ABCAPITAL | -6.7 | +0.0 | -2.5 | -3.6 | -0.6 |

Share of absolute impact by order: 1: 3%, 2: 54%, 3: 38%, 4: 5%

## Sources
- 2026-10-12 India's retail inflation jumps to 5.54% in September, above estimates - CNBC https://news.google.com/rss/search?q=India+retail+inflation+September+2026+5.54%25+when:120d&hl=en-IN&gl=IN&ceid=IN:en
- 2026-09-14 India inflation rises to 4.82% in August - Reuters https://news.google.com/rss/search?q=India+inflation+August+2026+4.82%25+when:120d&hl=en-IN&gl=IN&ceid=IN:en