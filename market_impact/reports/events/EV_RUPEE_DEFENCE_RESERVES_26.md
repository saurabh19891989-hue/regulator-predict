# Rupee at 95-96/USD and heavy RBI FX defence; reserves fall ~US$55bn from peak (`EV_RUPEE_DEFENCE_RESERVES_26`)
*india_macro · status occurred · date 2026-09-09 · P(3m) 1 · P(12m) 1 · confidence medium*

Rupee fell past 95/USD on 9 Sep, touched ~95.99 on 25 Sep (near record lows) amid oil, weak foreign flows and a narrow India-US yield spread. RBI intervened in spot and forwards: net short forward book reached a record ~US$200bn in August; weekly reserves fell a record US$18.34bn to US$757.46bn (w/e 25 Sep), US$734.60bn (2 Oct), US$726.03bn (9 Oct), US$721bn (16 Oct), US$719.75bn (23 Oct; seventh straight weekly fall). Implied peak ~US$775.8bn (18 Sep; derived: 757.46+18.34). RBI sold ~US$18.2bn in October, the most this year; Reuters (15 Oct) estimates it has spent half of a US$140bn capital-flow haul. On 12 Oct RBI moved to curb dollar demand. Rupee recovered to 94.58 on 5 Nov as crude fell and US midterms weakened the dollar; Reuters (4 Nov) still sees risk of resumed slide on weak inflows.

**Already moved:** USD/INR 94.49 on 5 Nov: -1.1% since 1 Jun (i.e. ~95.5 on 1 Jun), -1.9% over 1 month, +6.5% over 12 months (factor_state.md). Reserves -~7% from derived peak.

## Entry shocks (conditional on the event)
- `F_USDINR` USD/INR exchange rate: -0.37 SSU (range -0.6…0.2) net move since 1 Jun is -1.1% (=-0.37 SSU) because RBI defended; the peak leg was roughly +0.2 SSU above 1 Jun
- `NEW_FX_RESERVES_IN` India FX reserves (RBI intervention): -2.2 SSU (range -2.5…-1.9) US$775.8bn -> US$719.75bn = about -US$56bn (SSU = US$25bn)
- `F_LIQUIDITY_IN` Indian banking system liquidity: -0.4 SSU (range -1.0…0.0) spot dollar sales drain rupee liquidity, partly offset by swaps; magnitude uncertain

## Causal chains (agent)
- order 2: EV_RUPEE_DEFENCE_RESERVES_26 → NEW_FX_RESERVES_IN → F_LIQUIDITY_IN — Spot USD sales extinguish rupee liquidity
- order 3: EV_RUPEE_DEFENCE_RESERVES_26 → NEW_FX_RESERVES_IN → F_LIQUIDITY_IN → F_GSEC_10Y_IN — Liquidity drain pushes up G-sec yields
- order 4: EV_RUPEE_DEFENCE_RESERVES_26 → F_USDINR → F_CPI_IN → F_REPO_IN → BAJFINANCE — Weak rupee adds imported inflation -> more RBI hikes -> higher NBFC funding cost
- order 2: EV_RUPEE_DEFENCE_RESERVES_26 → F_USDINR → TCS — Weaker rupee lifts IT-services INR revenue/margins (hedged, lagged)

## Most positively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| VOLTAS | +1.1 | +1.1 | -0.1 | +0.0 | -0.0 |
| INDIGO | +0.9 | +0.7 | +0.1 | +0.1 | +0.0 |
| MOTILALOFS | +0.9 | +0.6 | +0.2 | +0.1 | -0.0 |
| KALYANKJIL | +0.9 | +0.0 | +0.7 | +0.2 | +0.0 |
| HINDPETRO | +0.8 | +0.8 | +0.0 | +0.0 | -0.0 |
| IOC | +0.7 | +0.7 | -0.0 | +0.0 | -0.0 |
| BLUESTARCO | +0.6 | +0.7 | -0.0 | +0.0 | -0.0 |
| SUZLON | +0.6 | +0.4 | +0.1 | +0.0 | +0.0 |
| ICICIGI | +0.6 | +0.6 | +0.0 | +0.1 | +0.0 |
| PRESTIGE | +0.6 | +0.0 | +0.4 | +0.1 | +0.1 |
| SIEMENS | +0.6 | +0.6 | +0.1 | +0.0 | -0.0 |
| LGEINDIA | +0.6 | +0.6 | -0.0 | +0.0 | -0.0 |
| BPCL | +0.6 | +0.6 | +0.0 | +0.0 | -0.0 |
| POWERINDIA | +0.6 | +0.4 | +0.2 | +0.0 | -0.0 |
| WAAREEENER | +0.6 | +0.5 | +0.0 | +0.0 | +0.0 |

## Most negatively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| BIOCON | -1.7 | -1.9 | +0.1 | +0.1 | +0.0 |
| JSWSTEEL | -1.3 | -0.9 | -0.4 | +0.0 | -0.0 |
| LAURUSLABS | -1.2 | -1.5 | +0.2 | +0.0 | +0.0 |
| VAML | -1.2 | -1.1 | -0.1 | +0.0 | +0.0 |
| DRREDDY | -1.1 | -1.2 | +0.1 | +0.0 | -0.0 |
| ONGC | -1.1 | -1.1 | +0.0 | +0.0 | +0.0 |
| NATIONALUM | -1.1 | -1.1 | +0.0 | +0.0 | +0.0 |
| OIL | -1.1 | -1.1 | +0.0 | +0.0 | +0.0 |
| AUROPHARMA | -1.1 | -1.2 | +0.1 | +0.0 | +0.0 |
| VEDL | -1.0 | -0.7 | -0.3 | -0.0 | +0.0 |
| LUPIN | -1.0 | -1.1 | +0.1 | +0.0 | -0.0 |
| HINDCOPPER | -1.0 | -1.1 | +0.1 | +0.0 | +0.0 |
| GLENMARK | -1.0 | -1.1 | +0.1 | +0.0 | -0.0 |
| JINDALSTEL | -1.0 | -0.4 | -0.7 | +0.1 | +0.0 |
| ZYDUSLIFE | -1.0 | -1.0 | +0.0 | +0.1 | -0.0 |

Share of absolute impact by order: 1: 65%, 2: 22%, 3: 9%, 4: 4%

## Sources
- 2026-10-30 India's FX reserves dip for seventh straight week - Reuters https://news.google.com/rss/search?q=India+forex+reserves+week+ended+October+23+2026+when:120d&hl=en-IN&gl=IN&ceid=IN:en
- 2026-10-02 Forex kitty plunges record $18.34 bn as rupee pressure mounts - New Indian Express https://news.google.com/rss/search?q=Forex+kitty+plunges+record+%2418.34+bn+rupee+pressure+when:120d&hl=en-IN&gl=IN&ceid=IN:en
- 2026-10-15 India's RBI has spent half of $140 billion FX capital haul - Reuters https://news.google.com/rss/search?q=RBI+spent+half+of+%24140+billion+FX+capital+haul+rupee+defence+when:120d&hl=en-IN&gl=IN&ceid=IN:en
- 2026-11-05 Indian Rupee closes at 94.58 against US dollar https://news.google.com/rss/search?q=Rupee+closing+94.58+November+5+2026+when:120d&hl=en-IN&gl=IN&ceid=IN:en