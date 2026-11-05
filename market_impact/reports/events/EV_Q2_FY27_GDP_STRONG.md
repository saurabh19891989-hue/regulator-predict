# Q2 FY27 GDP (MoSPI, ~30 Nov) prints >=7.0% (`EV_Q2_FY27_GDP_STRONG`)
*india_macro · status scheduled · date 2026-11-30 · P(3m) 0.8 · P(12m) 0.8 · confidence medium*

Release date approximate (model knowledge: Q2 data usually end-Nov; not verified). Finance Ministry estimate 7.35% (29 Oct); PMI 54.7-55.1, GST +22.9% y/y, credit growth ~19%, capex +18%; drags: oil shock, rupee, weak monsoon, rate hike. P(>=7.0%) ~0.80; P(<6.8%) ~0.12 (see soft event).

## Entry shocks (conditional on the event)
- `F_GDP_IN` India real GDP growth: 0.2 SSU (range -0.1…0.6) vs ~7.1% RBI full-year path
- `F_FPI_FLOWS` Foreign portfolio flows into Indian equities: 0.2 SSU (range 0.0…0.5) growth supports flows

## Causal chains (agent)
- order 2: EV_Q2_FY27_GDP_STRONG → F_GDP_IN → F_CREDIT_GROWTH_IN — Growth sustains credit demand
- order 2: EV_Q2_FY27_GDP_STRONG → F_GDP_IN → F_REPO_IN — Strong growth gives RBI room to keep tightening
- order 4: EV_Q2_FY27_GDP_STRONG → F_GDP_IN → F_CREDIT_GROWTH_IN → F_LIQUIDITY_IN → F_GSEC_10Y_IN — Credit>deposit growth drains liquidity, lifts yields
- order 4: EV_Q2_FY27_GDP_STRONG → F_GDP_IN → F_FPI_FLOWS → F_USDINR → F_CPI_IN — Growth-supported inflows stabilise rupee and cut imported inflation

## Most positively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| INDUSINDBK | +2.1 | +1.6 | +0.7 | -0.2 | -0.0 |
| MOTILALOFS | +1.7 | +1.6 | +0.2 | -0.0 | -0.0 |
| IDFCFIRSTB | +1.7 | +1.3 | +0.6 | -0.2 | +0.0 |
| ICICIAMC | +1.5 | +1.5 | +0.1 | -0.0 | -0.0 |
| SBIN | +1.5 | +1.3 | +0.3 | -0.1 | +0.0 |
| YESBANK | +1.5 | +1.4 | +0.3 | -0.2 | -0.0 |
| BANKINDIA | +1.4 | +1.0 | +0.6 | -0.2 | -0.0 |
| HDFCBANK | +1.4 | +1.2 | +0.3 | -0.1 | -0.0 |
| MAHABANK | +1.4 | +1.1 | +0.5 | -0.1 | -0.0 |
| KOTAKBANK | +1.3 | +1.0 | +0.4 | -0.1 | -0.0 |
| PAYTM | +1.3 | +1.0 | +0.2 | +0.1 | +0.0 |
| UNIONBANK | +1.3 | +1.0 | +0.4 | -0.1 | -0.0 |
| PNB | +1.2 | +1.0 | +0.4 | -0.1 | -0.0 |
| AXISBANK | +1.2 | +1.0 | +0.4 | -0.1 | -0.0 |
| FEDERALBNK | +1.2 | +0.4 | +0.9 | -0.1 | -0.0 |

## Most negatively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| PERSISTENT | -0.3 | +0.0 | -0.2 | -0.1 | -0.0 |
| TECHM | -0.3 | +0.0 | -0.2 | -0.1 | -0.0 |
| RVNL | -0.3 | +0.0 | -0.3 | +0.0 | -0.0 |
| TCS | -0.3 | +0.0 | -0.2 | -0.1 | -0.0 |
| SOLARINDS | -0.2 | +0.0 | -0.2 | -0.0 | -0.0 |
| SRF | -0.2 | +0.0 | -0.2 | -0.0 | +0.0 |
| VAML | -0.2 | +0.0 | -0.1 | -0.1 | -0.0 |
| TATASTEEL | -0.2 | +0.0 | -0.2 | -0.0 | +0.0 |
| APARINDS | -0.2 | +0.0 | -0.2 | +0.0 | -0.0 |
| NATIONALUM | -0.2 | +0.0 | -0.2 | -0.0 | -0.0 |
| PREMIERENE | -0.2 | +0.0 | -0.2 | -0.0 | -0.0 |
| OIL | -0.2 | +0.0 | -0.2 | -0.0 | -0.0 |
| SUZLON | -0.2 | +0.0 | -0.1 | -0.0 | -0.0 |
| GRASIM | -0.2 | +0.0 | -0.2 | -0.0 | -0.0 |
| NMDC | -0.2 | +0.0 | -0.2 | +0.0 | -0.0 |

Share of absolute impact by order: 1: 63%, 2: 24%, 3: 9%, 4: 3%

## Sources
- 2026-10-29 Finance ministry estimates India's Q2 FY27 GDP growth at 7.35% - ET https://news.google.com/rss/search?q=Finance+ministry+estimates+India+Q2+FY27+GDP+growth+7.35%25+when:120d&hl=en-IN&gl=IN&ceid=IN:en
- 2026-10-07 RBI raises FY27 GDP growth forecast to 7.1% - Moneycontrol https://news.google.com/rss/search?q=RBI+raises+FY27+GDP+growth+forecast+7.1%25+lifts+Q2+Q3+when:120d&hl=en-IN&gl=IN&ceid=IN:en