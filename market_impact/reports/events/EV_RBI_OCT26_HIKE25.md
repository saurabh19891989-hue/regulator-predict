# RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`)
*india_macro · status occurred · date 2026-10-07 · P(3m) 1 · P(12m) 1 · confidence high*

First RBI hike since 2023. Repo 5.25% -> 5.50% (held at 5.25% on 5 Aug 2026). Stance moved from neutral to 'calibrated tightening'; Governor Malhotra said near-term rate cuts are 'off the table'. Rate vote reported unanimous (secondary source); minutes (21 Oct) show 2 members opposed the stance change and flag more hikes but wariness of an aggressive cycle. Drivers cited: broadening inflation (oil, onions, monsoon), 7.8% Q1 GDP, global tightening. RBI raised FY27 GDP forecast to 7.1% (from 6.7%). RBI also tightened liquidity (see EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26).

**Already moved:** 6 Oct: banks in green, autos and realty dipped on hike expectations. 10y G-sec 7.40% on 12 Oct, >7.45% on 21 Oct, 7.44% on 3 Nov. Nifty had an 8-week losing streak before the decision; Nifty50 ~24,460 on 5 Nov (+7.4% in 1 month per factor_state.md). Rupee +1% to 95.76 on 12 Oct after RBI dollar-demand curbs.

## Entry shocks (conditional on the event)
- `F_REPO_IN` RBI repo rate: 1.0 SSU (range 0.9…1.0) +25 bp = 1 SSU, already delivered
- `F_GSEC_10Y_IN` India 10-year G-sec yield: 0.3 SSU (range 0.0…0.6) immediate repricing; the larger yield run-up is booked in EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26 to avoid double count
- `F_CREDIT_SPREADS_IN` Indian corporate credit spreads: 0.2 SSU (range 0.0…0.5) funding-cost repricing for NBFCs

## Causal chains (agent)
- order 2: EV_RBI_OCT26_HIKE25 → F_REPO_IN → F_CREDIT_GROWTH_IN — Higher policy rate slows credit demand/offtake after lag
- order 3: EV_RBI_OCT26_HIKE25 → F_REPO_IN → F_HOUSING_DEMAND → DLF — Mortgage costs rise -> housing sales volume softens -> developer pre-sales/valuations hit
- order 4: EV_RBI_OCT26_HIKE25 → F_REPO_IN → F_CREDIT_GROWTH_IN → F_GDP_IN → F_FPI_FLOWS — Slower credit trims growth; offset by a higher carry that supports flows via rupee stability (net ambiguous)
- order 3: EV_RBI_OCT26_HIKE25 → F_REPO_IN → F_USDINR → F_CPI_IN — Tighter policy narrows the carry gap, supports the rupee, and cuts imported-inflation pass-through (small)

## Most positively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| LICHSGFIN | +1.2 | +1.9 | -0.7 | +0.1 | -0.1 |
| BANKINDIA | +0.6 | +1.6 | -0.8 | -0.1 | -0.2 |
| PAYTM | +0.5 | +0.8 | -0.3 | +0.1 | -0.1 |
| MAHABANK | +0.0 | +1.1 | -0.7 | -0.1 | -0.2 |
| UNIONBANK | -0.1 | +0.6 | -0.5 | -0.0 | -0.1 |
| PNB | -0.1 | +0.6 | -0.5 | -0.0 | -0.1 |
| MCX | -0.1 | +0.0 | -0.1 | +0.0 | -0.0 |
| UPL | -0.1 | +0.0 | -0.1 | -0.0 | +0.0 |
| GROWW | -0.1 | -0.2 | +0.0 | +0.1 | +0.0 |
| SBIN | -0.1 | +0.4 | -0.4 | +0.0 | -0.1 |
| KOTAKBANK | -0.2 | +0.8 | -0.6 | -0.1 | -0.2 |
| BANKBARODA | -0.2 | +0.1 | -0.4 | +0.2 | -0.1 |
| PIIND | -0.2 | +0.0 | -0.2 | -0.0 | +0.0 |
| TCS | -0.3 | -0.3 | -0.1 | -0.0 | +0.1 |
| POLICYBZR | -0.4 | +0.0 | -0.0 | -0.2 | -0.1 |

## Most negatively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| BAJFINANCE | -5.4 | -4.8 | -0.7 | +0.2 | -0.1 |
| TATACAP | -5.3 | -4.5 | -0.9 | +0.2 | -0.1 |
| PRESTIGE | -5.3 | -4.5 | -0.7 | +0.1 | -0.1 |
| YESBANK | -5.0 | -4.2 | -0.8 | +0.0 | -0.1 |
| GMRAIRPORT | -5.0 | -4.5 | -0.1 | -0.4 | -0.1 |
| GODREJPROP | -4.8 | -3.7 | -1.1 | +0.0 | -0.1 |
| LODHA | -4.8 | -3.7 | -1.1 | +0.1 | -0.1 |
| SHRIRAMFIN | -4.5 | -3.5 | -0.7 | -0.2 | -0.2 |
| IREDA | -4.3 | -4.0 | -0.3 | +0.1 | -0.1 |
| JSWENERGY | -4.2 | -4.2 | +0.0 | +0.0 | -0.0 |
| PHOENIXLTD | -4.1 | -3.8 | -0.1 | -0.1 | -0.1 |
| BAJAJFINSV | -3.8 | -3.4 | -0.5 | +0.1 | -0.1 |
| M&MFIN | -3.7 | -3.2 | -0.5 | +0.0 | -0.1 |
| AUBANK | -3.6 | -3.0 | -0.7 | +0.2 | -0.1 |
| OBEROIRLTY | -3.5 | -2.9 | -0.6 | -0.0 | -0.1 |

Share of absolute impact by order: 1: 79%, 2: 14%, 3: 4%, 4: 3%

## Sources
- 2026-10-07 RBI MPC meeting highlights: Repo rate hiked to 5.5% - The Hindu https://news.google.com/rss/search?q=RBI+MPC+October+2026+repo+rate+hike+when:120d&hl=en-IN&gl=IN&ceid=IN:en
- 2026-10-21 RBI MPC minutes reveal 2 members opposed shift from neutral stance - Livemint https://news.google.com/rss/search?q=RBI+MPC+minutes+October+2026+when:120d&hl=en-IN&gl=IN&ceid=IN:en
- 2026-10-07 RBI raises FY27 GDP growth forecast to 7.1% - Moneycontrol https://news.google.com/rss/search?q=RBI+raises+FY27+GDP+growth+forecast+7.1%25+when:120d&hl=en-IN&gl=IN&ceid=IN:en