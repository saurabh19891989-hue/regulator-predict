# Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`)
*energy · status occurred · date 2026-06-01 · P(3m) 1 · P(12m) 1 · confidence medium*

US/Israel-Iran war with repeated tanker attacks in Hormuz, Houthi attacks on Saudi targets/East-West pipeline, Saudi output reported at lowest since 1990 (Bloomberg headline, 10 Sep). Brent touched $110 on 16 Oct, settled at 6-month highs 30 Oct, then fell ~16% in the week to 5 Nov on US-Iran talk hopes (Islamabad rounds; ceasefire described as 'on life support' on 3 Nov). Indian crude basket traded well above Brent futures (basket $122 vs $106 Brent per Gujarat Samachar headline 14 Oct) as physical premia/freight spiked. India's April-Sept crude import bill +46% to $90.6bn (ThePrint/Moneycontrol, 19-21 Oct).

**Review override applied:** Occurred-event shocks must be CHANGES since the event start or 2026-06-01, not y/y levels. Brent is flat since 1 Jun. With a 4.95 SSU (+49.5%) shock the event moves companies by +36%/-24% (event_impact_rank), above the ±25% plausibility bound. C_RED_SEA is split to avoid double counting with the Houthi event.

**Already moved:** Brent 94.99 on 2026-11-05: 1m -5.6%, 3m +15.2%, 6m -5.1%, 12m +49.5%, flat since 2026-06-01 (per market_impact/results/factor_state.md (Yahoo closes, 2026-11-05)). Refining-margin proxy +15.4% since 1 Jun, +72.7% y/y. USD/INR 94.49 (+6.5% y/y). Gold -8.4% and silver -30% since 1 Jun.

## Entry shocks (conditional on the event)
- `F_BRENT` Brent crude oil price: 0.0 SSU (range -0.3…0.3) Brent 94.99 on 5 Nov = +0.0% since 2026-06-01 (factor_state). The old 4.95 was the y/y LEVEL change, including the Feb-May war run-up
- `C_MIDEAST_CONFLICT` Middle East conflict intensity: 1.0 SSU (range 0.5…1.5) escalation vs 1 Jun (Apr-Jul ceasefire/Islamabad memorandum, collapsed 8 Jul); partly offset by current talks
- `C_RED_SEA` Red Sea / Suez shipping disruption: 0.5 SSU (range 0.3…1.0) other 0.5 is booked in EV_RED_SEA_HOUTHI_ESCALATION_Q3
- `F_REFINING_MARGIN` Refining margins (GRM / cracks): 0.6 SSU (range 0.3…1.2) refining proxy +15.4% since 1 Jun ~ +$1.2/bbl; old +$3/bbl unverified

## Causal chains (agent)
- order 2: EV_IRAN_WAR_HORMUZ_OIL → F_BRENT → F_USDINR — higher oil import bill widens CAD; rupee weaker
- order 3: EV_IRAN_WAR_HORMUZ_OIL → F_BRENT → F_USDINR → F_CPI_IN — rupee and fuel pass-through lift CPI (RBI hiked 7-9 Oct)
- order 4: EV_IRAN_WAR_HORMUZ_OIL → F_BRENT → F_CPI_IN → F_REPO_IN → F_GSEC_10Y_IN — CPI ~6% (Deutsche, 27 Oct) -> repo hike to 5.50% -> yields -> banks/NBFC/real estate
- order 3: EV_IRAN_WAR_HORMUZ_OIL → C_MIDEAST_CONFLICT → F_BRENT → F_REFINING_MARGIN — supply loss widens product cracks; export-oriented refiners gain
- order 3: EV_IRAN_WAR_HORMUZ_OIL → F_BRENT → NEW_OMC_MARKETING_MARGIN — frozen retail prices turn crude into OMC marketing under-recovery

## Most positively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| OIL | +5.2 | +5.0 | +0.1 | +0.1 | +0.0 |
| ONGC | +4.5 | +4.2 | +0.2 | +0.1 | +0.0 |
| VAML | +2.2 | +0.0 | +2.1 | +0.0 | -0.0 |
| NATIONALUM | +1.8 | +0.0 | +1.6 | +0.1 | +0.1 |
| COCHINSHIP | +1.6 | +0.4 | +1.1 | +0.0 | +0.0 |
| SOLARINDS | +1.3 | +1.5 | -0.1 | -0.1 | -0.0 |
| RELIANCE | +1.2 | +1.6 | -0.1 | -0.1 | -0.1 |
| BPCL | +0.9 | +1.5 | -0.5 | -0.0 | -0.0 |
| MAZDOCK | +0.9 | +1.0 | +0.0 | -0.1 | -0.0 |
| HAL | +0.9 | +1.0 | +0.0 | -0.1 | -0.0 |
| NTPC | +0.8 | +1.0 | +0.0 | -0.0 | -0.1 |
| MCX | +0.8 | +0.0 | +0.7 | +0.3 | -0.1 |
| MUTHOOTFIN | +0.7 | +0.0 | +1.1 | -0.2 | -0.2 |
| HINDZINC | +0.7 | +0.0 | -0.3 | +0.9 | +0.1 |
| COALINDIA | +0.5 | +0.0 | +0.0 | +0.3 | +0.2 |

## Most negatively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| FEDERALBNK | -5.1 | -3.5 | -0.8 | -0.6 | -0.2 |
| INDIGO | -3.9 | -3.0 | -0.5 | -0.2 | -0.2 |
| AXISBANK | -3.5 | -3.0 | -0.2 | -0.2 | -0.2 |
| GMRAIRPORT | -3.4 | -2.5 | -0.6 | -0.1 | -0.2 |
| INDHOTEL | -3.0 | -2.5 | -0.3 | -0.1 | -0.1 |
| HDFCBANK | -2.8 | -2.5 | +0.0 | -0.2 | -0.2 |
| LT | -2.8 | +0.0 | -2.8 | +0.0 | -0.0 |
| MOTILALOFS | -2.7 | +0.0 | -1.1 | -0.9 | -0.7 |
| ICICIAMC | -2.4 | +0.0 | -1.3 | -0.6 | -0.4 |
| JIOFIN | -2.3 | +0.0 | -1.6 | -0.3 | -0.4 |
| IREDA | -2.2 | +0.0 | -1.6 | -0.3 | -0.4 |
| ATGL | -2.2 | -1.5 | -0.6 | -0.1 | -0.1 |
| ADANIENT | -2.2 | -1.5 | -0.5 | -0.1 | -0.1 |
| IDEA | -2.1 | +0.0 | -1.3 | -0.4 | -0.4 |
| SUZLON | -2.1 | -2.0 | +0.0 | -0.0 | -0.1 |

Share of absolute impact by order: 1: 35%, 2: 32%, 3: 19%, 4: 15%

## Sources
- 2026-10-16 Brent oil touches $110 as Iran escalates Hormuz attacks (CNBC) (headline via Google News RSS; article body not read) https://news.google.com/rss/search?q=Brent+oil+Iran+war+Hormuz+when:120d&hl=en-IN&gl=IN&ceid=IN:en
- 2026-11-05 Brent Below $95 After 16% Crash This Week (NDTV Profit) (headline via Google News RSS; article body not read) https://news.google.com/rss/search?q=Oil+prices+Brent+below+$95+Iran+when:120d&hl=en-IN&gl=IN&ceid=IN:en
- 2026-10-19 India's crude import bill jumps 46% to $90.6bn in Apr-Sep (ThePrint) (headline via Google News RSS; article body not read) https://news.google.com/rss/search?q=India+crude+import+bill+46%+when:120d&hl=en-IN&gl=IN&ceid=IN:en