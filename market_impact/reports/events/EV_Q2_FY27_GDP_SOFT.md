# Q2 FY27 GDP prints below 6.8% (downside surprise) (`EV_Q2_FY27_GDP_SOFT`)
*india_macro · status scheduled · date 2026-11-30 · P(3m) 0.12 · P(12m) 0.12 · confidence low*

Downside case: oil/rupee shock, high yields and weak rural demand bite faster than high-frequency data suggest. Low probability given PMI, GST and credit data; GDP vs high-frequency divergence has precedent (model knowledge).

## Entry shocks (conditional on the event)
- `F_GDP_IN` India real GDP growth: -0.8 SSU (range -1.5…-0.4) vs ~7.35% estimate
- `F_FPI_FLOWS` Foreign portfolio flows into Indian equities: -0.3 SSU (range -0.8…0.0) growth scare
- `F_REPO_IN` RBI repo rate: -0.2 SSU (range -0.5…0.0) lowers odds of Dec hike

## Causal chains (agent)
- order 2: EV_Q2_FY27_GDP_SOFT → F_GDP_IN → F_CREDIT_GROWTH_IN — Weaker output cuts credit demand
- order 3: EV_Q2_FY27_GDP_SOFT → F_GDP_IN → F_REPO_IN → F_GSEC_10Y_IN — Reduces hike odds, eases yields
- order 4: EV_Q2_FY27_GDP_SOFT → F_GDP_IN → F_CREDIT_GROWTH_IN → F_LIQUIDITY_IN → F_GSEC_10Y_IN — Slower credit growth frees liquidity
- order 3: EV_Q2_FY27_GDP_SOFT → F_GDP_IN → F_FPI_FLOWS → F_USDINR — Lower foreign inflows weaken rupee

## Most positively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| PERSISTENT | +1.0 | +0.0 | +1.0 | -0.0 | +0.0 |
| TECHM | +0.8 | +0.0 | +0.8 | +0.0 | +0.0 |
| TCS | +0.8 | +0.0 | +0.7 | +0.0 | +0.0 |
| VAML | +0.4 | +0.0 | +0.3 | +0.1 | +0.0 |
| PREMIERENE | +0.3 | +0.3 | -0.1 | +0.0 | +0.0 |
| SRF | +0.2 | +0.2 | +0.1 | -0.0 | -0.1 |
| RVNL | +0.2 | +0.4 | +0.0 | -0.2 | +0.0 |
| HINDZINC | +0.2 | +0.0 | +0.2 | +0.0 | +0.0 |
| NATIONALUM | +0.2 | +0.1 | +0.2 | -0.1 | -0.0 |
| OIL | +0.2 | +0.1 | +0.2 | -0.1 | -0.0 |
| COCHINSHIP | +0.2 | +0.1 | +0.1 | -0.0 | +0.0 |
| GROWW | +0.2 | -0.4 | +0.3 | +0.2 | +0.1 |
| NMDC | +0.1 | +0.1 | +0.1 | -0.1 | -0.0 |
| SUNPHARMA | +0.1 | +0.0 | +0.1 | -0.0 | +0.0 |
| SOLARINDS | +0.1 | +0.4 | -0.2 | -0.1 | -0.0 |

## Most negatively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| INDUSINDBK | -6.7 | -4.3 | -2.6 | +0.2 | +0.0 |
| IDFCFIRSTB | -5.5 | -3.5 | -2.2 | +0.2 | +0.0 |
| YESBANK | -5.2 | -3.8 | -1.8 | +0.2 | +0.1 |
| BANKINDIA | -4.8 | -3.5 | -1.4 | +0.0 | +0.1 |
| MAHABANK | -4.5 | -3.3 | -1.2 | -0.0 | +0.1 |
| KOTAKBANK | -4.4 | -3.1 | -1.3 | +0.0 | +0.0 |
| HDFCBANK | -4.1 | -2.9 | -1.3 | +0.0 | +0.1 |
| UNIONBANK | -4.1 | -3.2 | -1.0 | +0.1 | +0.1 |
| PNB | -4.0 | -3.2 | -1.0 | +0.1 | +0.1 |
| INDIANB | -4.0 | -2.9 | -1.2 | +0.1 | +0.0 |
| SBIN | -4.0 | -3.4 | -0.8 | +0.2 | +0.0 |
| FEDERALBNK | -4.0 | -0.7 | -3.3 | -0.0 | +0.0 |
| AXISBANK | -3.9 | -2.5 | -1.5 | +0.1 | +0.1 |
| ICICIAMC | -3.7 | -3.6 | -0.1 | +0.0 | +0.0 |
| SHRIRAMFIN | -3.5 | -2.9 | -0.6 | +0.0 | -0.0 |

Share of absolute impact by order: 1: 55%, 2: 30%, 3: 11%, 4: 5%

## Sources
- 2026-10-29 Finance ministry estimates India's Q2 FY27 GDP growth at 7.35% https://news.google.com/rss/search?q=India+Q2+GDP+FY27+estimate+risks+when:120d&hl=en-IN&gl=IN&ceid=IN:en