# Disorderly yen carry-trade unwind (Aug-2024-style) after BoJ/MoF action (`EV_YEN_CARRY_UNWIND_RISK`)
*global_macro · status risk_scenario · date 2027-01-31 · P(3m) 0.05 · P(12m) 0.15 · confidence low*

Yen neared 160 in Aug 2026; BoJ at 31-year-high rates; hawkish BoJ/Takaichi plus falling UST yields push USD/JPY down; analog Aug 2024 (VIX spike, EM selloff, ~-6% Nikkei day). P(VIX >30 episode linked to yen)=0.06 by 3m, 0.18 by 12m (our estimate).

**Review override applied:** 5 SSU (+25 VIX pts) is the intraday extreme of Aug 2024 and is used as a 12m-horizon shock, which overstates (rank #2 by impact, -35% max). The event also hits both F_US_EQUITIES and F_RISK_SENTIMENT, which reach Indian stocks by parallel paths. USD/JPY is ~157-158 with BoJ hike expectations for Dec (TradingNEWS 2 Nov). Odds trimmed slightly.

**Already moved:** n/a

## Entry shocks (conditional on the event)
- `NEW_USDJPY` USD/JPY exchange rate: -3.0 SSU (range -5.0…-1.5) -9% USD/JPY
- `F_RISK_SENTIMENT` Global risk aversion (VIX): 2.5 SSU (range 1.5…5.0) VIX +12.5 pts persistent-equivalent; Aug-2024 intraday +45 pts but closes back <20 within ~2 weeks
- `F_US_EQUITIES` US equity market: -1.5 SSU (range -3.0…-0.7) S&P -7.5% (Aug-2024 drawdown ~-8.5%)

## Causal chains (agent)
- order 2: EV_YEN_CARRY_UNWIND_RISK → F_RISK_SENTIMENT → F_FPI_FLOWS — EM outflows
- order 3: EV_YEN_CARRY_UNWIND_RISK → F_FPI_FLOWS → F_USDINR — INR
- order 4: EV_YEN_CARRY_UNWIND_RISK → F_USDINR → F_CPI_IN → F_REPO_IN — inflation/RBI

## Most positively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| HINDZINC | +2.2 | +0.0 | +0.7 | +1.3 | +0.2 |
| JSWSTEEL | +2.1 | +0.0 | +0.8 | +1.1 | +0.2 |
| NATIONALUM | +2.0 | +0.0 | +0.9 | +1.2 | -0.1 |
| ASTRAL | +1.7 | +2.0 | -0.1 | -0.2 | +0.0 |
| TATACONSUM | +1.7 | +2.0 | -0.1 | -0.2 | +0.0 |
| ONGC | +1.7 | +0.0 | +0.9 | +0.9 | -0.1 |
| OIL | +1.7 | +0.0 | +0.9 | +0.8 | -0.1 |
| SAIL | +1.6 | +0.0 | +0.3 | +0.8 | +0.5 |
| TATASTEEL | +1.6 | +0.0 | +0.4 | +0.9 | +0.3 |
| NMDC | +1.3 | +0.0 | +0.6 | +0.7 | +0.0 |
| SRF | +1.2 | +0.0 | +0.6 | +0.7 | -0.0 |
| PIIND | +1.2 | +0.0 | +0.6 | +0.6 | +0.0 |
| HINDALCO | +1.2 | +0.0 | +0.4 | +0.8 | -0.0 |
| BAJAJ-AUTO | +1.0 | +0.0 | +0.6 | +0.4 | -0.0 |
| UPL | +0.8 | +0.0 | +0.3 | +0.5 | +0.0 |

## Most negatively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| MOTILALOFS | -21.5 | -11.0 | -8.8 | -2.1 | +0.4 |
| ICICIAMC | -18.4 | -11.5 | -6.4 | -0.8 | +0.3 |
| IREDA | -16.4 | -12.5 | -3.5 | -0.3 | -0.1 |
| 360ONE | -15.8 | -8.8 | -5.8 | -1.4 | +0.2 |
| INDUSINDBK | -15.1 | -8.8 | -6.7 | +0.2 | +0.2 |
| NAUKRI | -14.4 | -10.0 | -4.3 | -0.2 | +0.1 |
| PAYTM | -13.2 | -6.5 | -7.1 | +0.3 | +0.1 |
| MAHABANK | -12.7 | -8.8 | -4.2 | +0.1 | +0.1 |
| IDFCFIRSTB | -12.6 | -7.5 | -5.1 | -0.0 | -0.0 |
| POLICYBZR | -12.3 | -6.2 | -6.5 | +0.4 | +0.1 |
| LICI | -11.3 | -8.8 | -2.6 | -0.0 | +0.1 |
| IDEA | -11.3 | -6.2 | -4.5 | -0.4 | -0.1 |
| MEESHO | -10.6 | -5.0 | -5.8 | +0.2 | +0.0 |
| SBIN | -10.6 | -3.8 | -6.8 | -0.0 | -0.0 |
| INDIANB | -10.3 | -7.5 | -2.6 | -0.1 | -0.0 |

Share of absolute impact by order: 1: 35%, 2: 56%, 3: 7%, 4: 2%

## Sources
- 2026-10-05 Japan Has Left the Zero-Rate World. What Happens to the Yen Carry Trade? - IndraStra https://news.google.com/rss/search?q=Japan%20Has%20Left%20the%20Zero-Rate%20World.%20What%20Happens%20to%20the%20Yen%20Carry%20Trade%3F%20-%20IndraStra&hl=en-IN&gl=IN&ceid=IN:en
- 2026-10-22 USD/JPY Breaks Support as Falling Treasury Yields Favor the Yen - Investing.com https://news.google.com/rss/search?q=USD/JPY%20Breaks%20Support%20as%20Falling%20Treasury%20Yields%20Favor%20the%20Yen%20-%20Investing.com&hl=en-IN&gl=IN&ceid=IN:en