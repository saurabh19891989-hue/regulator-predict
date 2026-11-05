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
| PIIND | +0.3 | +0.0 | +0.4 | -0.0 | -0.0 |
| NATIONALUM | +0.3 | +0.0 | +0.4 | -0.1 | +0.0 |
| OIL | +0.3 | +0.0 | +0.4 | -0.1 | +0.0 |
| HINDCOPPER | +0.3 | +0.0 | +0.4 | -0.1 | +0.0 |
| ONGC | +0.2 | +0.0 | +0.3 | -0.1 | +0.0 |
| UPL | +0.2 | +0.0 | +0.2 | -0.0 | -0.0 |
| LUPIN | +0.1 | +0.0 | +0.1 | -0.0 | -0.0 |
| MCX | +0.1 | +0.0 | +0.3 | -0.1 | -0.1 |
| NMDC | +0.1 | +0.0 | +0.1 | -0.0 | +0.0 |
| DRREDDY | +0.0 | +0.0 | +0.1 | -0.1 | +0.0 |
| VAML | -0.1 | +0.0 | +0.5 | -0.5 | -0.0 |
| HINDZINC | -0.1 | +0.0 | +0.3 | -0.3 | -0.0 |
| HINDALCO | -0.1 | +0.0 | +0.0 | -0.2 | +0.1 |
| SUNPHARMA | -0.2 | +0.0 | +0.2 | -0.3 | -0.0 |
| TMPV | -0.2 | +0.0 | +0.1 | -0.5 | +0.2 |

## Most negatively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| YESBANK | -6.1 | +0.0 | -4.1 | -2.0 | +0.1 |
| BAJFINANCE | -5.4 | +0.0 | -4.1 | -1.2 | -0.1 |
| TATACAP | -5.3 | +0.0 | -3.4 | -1.8 | -0.1 |
| AUBANK | -4.3 | +0.0 | -3.1 | -1.2 | -0.0 |
| PRESTIGE | -4.2 | +0.0 | -3.1 | -1.1 | +0.0 |
| IREDA | -4.2 | +0.0 | -2.7 | -1.5 | -0.1 |
| BAJAJFINSV | -3.8 | +0.0 | -2.6 | -1.1 | -0.1 |
| JSWENERGY | -3.7 | +0.0 | -2.9 | -0.9 | +0.0 |
| IDFCFIRSTB | -3.7 | +0.0 | -2.4 | -1.5 | +0.2 |
| JIOFIN | -3.6 | +0.0 | -2.0 | -1.4 | -0.2 |
| GODREJPROP | -3.5 | +0.0 | -2.6 | -0.8 | -0.1 |
| LTF | -3.4 | +0.0 | -2.6 | -0.9 | +0.1 |
| PAGEIND | -3.4 | -1.1 | -1.5 | -0.6 | -0.1 |
| SHRIRAMFIN | -3.2 | +0.0 | -1.3 | -2.1 | +0.2 |
| ETERNAL | -3.1 | -0.6 | -2.9 | +0.4 | -0.1 |

Share of absolute impact by order: 1: 5%, 2: 60%, 3: 30%, 4: 5%

## Sources
- 2026-10-12 India's retail inflation jumps to 5.54% in September, above estimates - CNBC https://news.google.com/rss/search?q=India+retail+inflation+September+2026+5.54%25+when:120d&hl=en-IN&gl=IN&ceid=IN:en
- 2026-09-14 India inflation rises to 4.82% in August - Reuters https://news.google.com/rss/search?q=India+inflation+August+2026+4.82%25+when:120d&hl=en-IN&gl=IN&ceid=IN:en