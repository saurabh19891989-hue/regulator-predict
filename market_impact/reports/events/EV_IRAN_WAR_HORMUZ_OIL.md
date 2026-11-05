# Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`)
*energy · status occurred · date 2026-06-01 · P(3m) 1 · P(12m) 1 · confidence medium*

US/Israel-Iran war with repeated tanker attacks in Hormuz, Houthi attacks on Saudi targets/East-West pipeline, Saudi output reported at lowest since 1990 (Bloomberg headline, 10 Sep). Brent touched $110 on 16 Oct, settled at 6-month highs 30 Oct, then fell ~16% in the week to 5 Nov on US-Iran talk hopes (Islamabad rounds; ceasefire described as 'on life support' on 3 Nov). Indian crude basket traded well above Brent futures (basket $122 vs $106 Brent per Gujarat Samachar headline 14 Oct) as physical premia/freight spiked. India's April-Sept crude import bill +46% to $90.6bn (ThePrint/Moneycontrol, 19-21 Oct).

**Already moved:** Brent 94.99 on 2026-11-05: 1m -5.6%, 3m +15.2%, 6m -5.1%, 12m +49.5%, flat since 2026-06-01 (per market_impact/results/factor_state.md (Yahoo closes, 2026-11-05)). Refining-margin proxy +15.4% since 1 Jun, +72.7% y/y. USD/INR 94.49 (+6.5% y/y). Gold -8.4% and silver -30% since 1 Jun.

## Entry shocks (conditional on the event)
- `F_BRENT` Brent crude oil price: 4.95 SSU (range 4.0…5.5) y/y +49.5% in units of +10%; this is the cumulative change that has happened, much already priced
- `C_MIDEAST_CONFLICT` Middle East conflict intensity: 1.5 SSU (range 1.0…2.0) escalation level sustained since mid-2026
- `C_RED_SEA` Red Sea / Suez shipping disruption: 1.0 SSU (range 0.5…1.0) Houthi blockade/attacks on Saudi pipeline infra
- `F_REFINING_MARGIN` Refining margins (GRM / cracks): 1.5 SSU (range 0.8…2.5) cracks elevated; IOC Q2 GRM details not verified

## Causal chains (agent)
- order 2: EV_IRAN_WAR_HORMUZ_OIL → F_BRENT → F_USDINR — higher oil import bill widens CAD; rupee weaker
- order 3: EV_IRAN_WAR_HORMUZ_OIL → F_BRENT → F_USDINR → F_CPI_IN — rupee and fuel pass-through lift CPI (RBI hiked 7-9 Oct)
- order 4: EV_IRAN_WAR_HORMUZ_OIL → F_BRENT → F_CPI_IN → F_REPO_IN → F_GSEC_10Y_IN — CPI ~6% (Deutsche, 27 Oct) -> repo hike to 5.50% -> yields -> banks/NBFC/real estate
- order 3: EV_IRAN_WAR_HORMUZ_OIL → C_MIDEAST_CONFLICT → F_BRENT → F_REFINING_MARGIN — supply loss widens product cracks; export-oriented refiners gain
- order 3: EV_IRAN_WAR_HORMUZ_OIL → F_BRENT → NEW_OMC_MARKETING_MARGIN — frozen retail prices turn crude into OMC marketing under-recovery

## Most positively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| OIL | +35.8 | +32.9 | +2.7 | +0.3 | -0.1 |
| ONGC | +27.5 | +24.4 | +2.9 | +0.2 | -0.1 |
| MCX | +7.7 | +6.4 | +1.9 | -0.2 | -0.4 |
| COALINDIA | +6.5 | +5.0 | +0.9 | +0.4 | +0.2 |
| JSWSTEEL | +6.4 | +0.0 | +3.4 | +3.2 | -0.2 |
| SAIL | +6.1 | +0.0 | +1.1 | +4.8 | +0.2 |
| COCHINSHIP | +5.8 | +3.3 | +3.0 | -0.3 | -0.1 |
| HINDZINC | +3.9 | +0.0 | +2.7 | +2.0 | -0.8 |
| VAML | +3.6 | +0.0 | +4.2 | +0.5 | -1.2 |
| SOLARINDS | +3.6 | +4.7 | +0.2 | -1.0 | -0.3 |
| TATASTEEL | +3.2 | +0.0 | +0.7 | +2.5 | -0.0 |
| BAJAJ-AUTO | +3.2 | +2.5 | +1.5 | +0.0 | -0.8 |
| DRREDDY | +3.0 | -1.0 | +4.6 | -0.2 | -0.4 |
| JINDALSTEL | +2.9 | -1.2 | -0.4 | +5.1 | -0.7 |
| GLENMARK | +2.6 | +0.0 | +4.1 | -0.9 | -0.6 |

## Most negatively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| YESBANK | -24.0 | +0.0 | -4.9 | -10.8 | -8.3 |
| INDIGO | -23.2 | -17.5 | -2.3 | -2.0 | -1.4 |
| BPCL | -20.7 | -22.0 | +1.9 | -0.5 | -0.1 |
| GMRAIRPORT | -19.2 | -11.2 | -3.0 | -2.4 | -2.6 |
| IDFCFIRSTB | -19.0 | +0.0 | -6.1 | -8.7 | -4.2 |
| MOTILALOFS | -18.8 | +0.0 | -8.8 | -7.2 | -2.8 |
| BAJFINANCE | -17.4 | +0.0 | -2.8 | -7.8 | -6.9 |
| AXISBANK | -17.3 | -4.5 | -4.6 | -5.3 | -2.9 |
| INDUSINDBK | -16.7 | +0.0 | -6.7 | -7.6 | -2.4 |
| HINDPETRO | -15.9 | -14.1 | -1.1 | -0.6 | -0.1 |
| TATACAP | -15.3 | +0.0 | -1.2 | -7.5 | -6.6 |
| IREDA | -15.1 | +0.0 | -4.8 | -5.9 | -4.4 |
| AUBANK | -14.7 | +0.0 | -1.8 | -8.2 | -4.8 |
| IDEA | -14.2 | +0.0 | -6.3 | -4.2 | -3.7 |
| JIOFIN | -13.8 | +0.0 | -3.9 | -4.6 | -5.3 |

Share of absolute impact by order: 1: 28%, 2: 26%, 3: 28%, 4: 18%

## Sources
- 2026-10-16 Brent oil touches $110 as Iran escalates Hormuz attacks (CNBC) (headline via Google News RSS; article body not read) https://news.google.com/rss/search?q=Brent+oil+Iran+war+Hormuz+when:120d&hl=en-IN&gl=IN&ceid=IN:en
- 2026-11-05 Brent Below $95 After 16% Crash This Week (NDTV Profit) (headline via Google News RSS; article body not read) https://news.google.com/rss/search?q=Oil+prices+Brent+below+$95+Iran+when:120d&hl=en-IN&gl=IN&ceid=IN:en
- 2026-10-19 India's crude import bill jumps 46% to $90.6bn in Apr-Sep (ThePrint) (headline via Google News RSS; article body not read) https://news.google.com/rss/search?q=India+crude+import+bill+46%+when:120d&hl=en-IN&gl=IN&ceid=IN:en