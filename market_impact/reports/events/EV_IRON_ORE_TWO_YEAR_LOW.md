# Iron ore at two-year low; NMDC price cuts then partial hike (`EV_IRON_ORE_TWO_YEAR_LOW`)
*metals_china · status occurred · date 2026-07-10 · P(3m) 1 · P(12m) 1 · confidence medium*

Iron ore (TIO=F) is $91.95/t: -12.5% since 1 Jun, -17% in 6m, -12% y/y. Mining.com (15 Oct) reported a two-year low on weak Chinese demand and rising supply; Simandou ramp-up offsets supply cuts elsewhere (Macquarie, 3 Nov); BMI cut its forecast (19 Aug). NMDC cut lump/fines prices in July and again on 8 Aug (lump Rs 5,250/t, fines Rs 4,500/t per scanx), then raised lump by Rs 150/t on 9 Sep holding fines. NMDC output +18% y/y in Oct (5.04 Mt) but sales -12%.

**Already moved:** Iron ore -12.5% since 1 Jun 2026 (factor_state); NMDC lump Rs 5,250/t after Aug cut, +Rs 150 in Sep.

## Entry shocks (conditional on the event)
- `F_IRON_ORE` Iron ore price: -0.83 SSU (range -1.0…-0.6) -12.5% since 1 Jun / SSU 15%

## Causal chains (agent)
- order 2: EV_IRON_ORE_TWO_YEAR_LOW → F_IRON_ORE → NMDC — Lower realisations cut NMDC revenue/EBITDA per tonne; volumes (sales -12% in Oct) also soft.
- order 3: EV_IRON_ORE_TWO_YEAR_LOW → F_IRON_ORE → F_STEEL_GLOBAL → F_STEEL_INDIA — Cheaper ore lowers steel cost floor in China/India; offsets coking coal.
- order 4: EV_IRON_ORE_TWO_YEAR_LOW → F_IRON_ORE → F_STEEL_INDIA → JSWSTEEL — Producers with merchant ore purchases (JSW, Jindal) gain margin while captive-ore holders (Tata, SAIL, NMDC) lose upstream value.

## Most positively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| JINDALSTEL | +1.5 | +2.1 | +0.0 | -0.6 | +0.0 |
| JSWSTEEL | +0.9 | +1.2 | +0.0 | -0.4 | +0.0 |
| TMPV | +0.3 | +0.0 | +0.3 | +0.0 | +0.0 |
| TMCV | +0.2 | +0.0 | +0.0 | +0.2 | +0.0 |
| BHEL | +0.2 | +0.0 | +0.0 | +0.2 | +0.0 |
| MARUTI | +0.2 | +0.0 | +0.0 | +0.2 | +0.0 |
| CGPOWER | +0.2 | +0.0 | +0.2 | +0.0 | +0.0 |
| GVT&D | +0.2 | +0.0 | +0.2 | +0.0 | +0.0 |
| ASHOKLEY | +0.2 | +0.0 | +0.0 | +0.2 | +0.0 |
| SUZLON | +0.2 | +0.0 | +0.0 | +0.2 | +0.0 |
| COCHINSHIP | +0.1 | +0.0 | +0.0 | +0.1 | +0.0 |
| HYUNDAI | +0.1 | +0.0 | +0.0 | +0.1 | +0.0 |
| RVNL | +0.1 | +0.0 | +0.0 | +0.1 | +0.0 |
| TIINDIA | +0.1 | +0.0 | +0.0 | +0.1 | +0.0 |
| TVSMOTOR | +0.1 | +0.0 | +0.0 | +0.1 | +0.0 |

## Most negatively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| NMDC | -7.5 | -7.5 | +0.0 | -0.1 | +0.0 |
| SAIL | -1.0 | -0.4 | +0.0 | -0.6 | +0.0 |
| TATASTEEL | -0.9 | -0.4 | -0.2 | -0.3 | +0.0 |
| ADANIPORTS | -0.4 | -0.4 | +0.0 | +0.0 | +0.0 |
| HAL | -0.4 | -0.4 | +0.0 | +0.0 | +0.0 |
| M&MFIN | -0.1 | +0.0 | -0.1 | +0.0 | +0.0 |
| APLAPOLLO | -0.1 | +0.0 | +0.0 | -0.1 | -0.0 |
| LTF | -0.1 | +0.0 | -0.1 | +0.0 | +0.0 |
| CHOLAFIN | -0.1 | +0.0 | -0.1 | +0.0 | +0.0 |
| ABCAPITAL | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| BLUESTARCO | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| NAUKRI | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| PIDILITIND | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| TATACAP | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| ASIANPAINT | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |

Share of absolute impact by order: 1: 67%, 2: 6%, 3: 26%, 4: 1%

## Sources
- 2026-10-15 Iron ore price slips to two-year low on concerns over weak demand, rising supply https://news.google.com/rss/search?q=Iron+ore+price+slips+to+two-year+low+on+concerns+over+weak+demand,+rising+supply&hl=en-IN&gl=IN&ceid=IN:en
- 2026-08-08 NMDC cuts iron ore prices from August 8 https://news.google.com/rss/search?q=NMDC+cuts+iron+ore+prices+from+August+8&hl=en-IN&gl=IN&ceid=IN:en
- 2026-09-09 NMDC raises lump ore price by Rs 150/tonne, holds price of fines https://news.google.com/rss/search?q=NMDC+raises+lump+ore+price+by+Rs+150/tonne,+holds+price+of+fines&hl=en-IN&gl=IN&ceid=IN:en
- 2026-11-03 Simandou Iron-Ore Ramp-Up Offsets Global Supply Cuts, Macquarie Says https://news.google.com/rss/search?q=Simandou+Iron-Ore+Ramp-Up+Offsets+Global+Supply+Cuts,+Macquarie+Says&hl=en-IN&gl=IN&ceid=IN:en
- 2026-11-02 NMDC October iron ore output rises 18%, but sales fall 12% https://news.google.com/rss/search?q=NMDC+October+iron+ore+output+rises+18%,+but+sales+fall+12%&hl=en-IN&gl=IN&ceid=IN:en