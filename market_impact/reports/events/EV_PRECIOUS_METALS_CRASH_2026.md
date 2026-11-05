# Gold and silver slump from January 2026 peaks (silver -53%, gold -24%) (`EV_PRECIOUS_METALS_CRASH_2026`)
*metals_china · status occurred · date 2026-01-15 · P(3m) 1 · P(12m) 1 · confidence medium*

Gold peaked at ~$5,419/oz in Jan 2026 and is ~$4,128 (-8.4% since 1 Jun, -12.4% in 6m); silver is $52.5 (-30% since 1 Jun, -34% in 6m, -53% from the Jan peak; Indian silver below Rs 2 lakh/kg since 23-24 Oct, 11-month low). Reported causes (headline-level, bodies not fetched): the 2026 Iran war lifted oil, yields and the dollar; US inflation at a 3-year high pushed markets to price Fed HIKES (Fed held on 28 Oct under Chair Warsh, December hike bet - NY Post); US 10Y 4.89% (+9% since June), DXY +2.2% since June; weak physical silver market and ETF/investor retreat (Metals Focus 29 Oct); gold heading for its biggest yearly drop in 11 years (investingLive 28 Oct). Outlook is split: Metals Focus path to $6,000 gold / silver >$90 requires renewed investor confidence; Investing.com scenario of $3,100 before a rally; HSBC sees limited silver gains; Goldman (28 Aug) forecast gold climbing on central-bank buying.

**Already moved:** Gold -8.4% and silver -30.0% since 2026-06-01; silver -14.1% in the last month (factor_state).

## Entry shocks (conditional on the event)
- `F_GOLD` Gold price: -1.05 SSU (range -1.2…-0.9) -8.4% since 1 Jun / SSU 8%
- `F_SILVER` Silver price: -2.5 SSU (range -2.8…-2.2) -30% since 1 Jun / SSU 12%
- `F_US_10Y` US 10-year Treasury yield: 1.5 SSU (range 1.2…1.8) yield +9.4% since June ~ +40 bp
- `F_DXY` US dollar index: 0.7 SSU (range 0.5…0.9) +2.2% since June / SSU 3%

## Causal chains (agent)
- order 2: EV_PRECIOUS_METALS_CRASH_2026 → F_GOLD → TITAN — Lower gold cuts jeweller inventory gains but can revive volume demand (Dhanteras buying) - net mixed.
- order 2: EV_PRECIOUS_METALS_CRASH_2026 → F_GOLD → MUTHOOTFIN — Gold-loan NBFCs' collateral value falls (LTV risk) and loan growth driven by gold price slows.
- order 3: EV_PRECIOUS_METALS_CRASH_2026 → F_SILVER → HINDZINC — Hindustan Zinc is a top-3 silver producer; silver -30% trims by-product earnings even though zinc/lead and cost cuts drove a +142% Q2 profit.
- order 3: EV_PRECIOUS_METALS_CRASH_2026 → F_GOLD → F_GOLD_DEMAND_IN → F_USDINR — Cheaper gold boosts Indian demand volumes and gold imports, widening the current-account deficit and pressuring the rupee.
- order 4: EV_PRECIOUS_METALS_CRASH_2026 → F_US_10Y → F_FPI_FLOWS → F_USDINR — The same rates/dollar shock that crushed gold also drives FPI outflows from India.

## Most positively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| PREMIERENE | +3.3 | +3.5 | -0.1 | -0.0 | -0.0 |
| WAAREEENER | +1.6 | +2.0 | -0.3 | -0.0 | -0.1 |
| TMPV | +1.4 | +0.0 | +0.8 | +0.5 | +0.0 |
| JSWSTEEL | +1.2 | +0.0 | +0.4 | +0.7 | +0.1 |
| SAIL | +1.2 | +0.0 | +0.2 | +0.8 | +0.2 |
| MANKIND | +0.9 | +1.0 | -0.3 | +0.2 | -0.1 |
| ONGC | +0.8 | +0.0 | +0.5 | +0.4 | -0.1 |
| OIL | +0.8 | +0.0 | +0.5 | +0.4 | -0.1 |
| NMDC | +0.7 | +0.0 | +0.3 | +0.4 | -0.0 |
| DRREDDY | +0.6 | +0.0 | +0.2 | +0.5 | -0.0 |
| JINDALSTEL | +0.6 | +0.0 | -0.4 | +0.6 | +0.3 |
| SRF | +0.5 | +0.0 | +0.3 | +0.2 | -0.1 |
| TATASTEEL | +0.5 | +0.0 | -0.2 | +0.5 | +0.1 |
| PIIND | +0.5 | +0.0 | +0.3 | +0.1 | -0.0 |
| LUPIN | +0.4 | +0.0 | +0.0 | +0.4 | -0.0 |

## Most negatively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| HINDZINC | -8.8 | -8.8 | -0.4 | +0.3 | -0.0 |
| MCX | -6.3 | -5.3 | -0.8 | -0.4 | +0.2 |
| MUTHOOTFIN | -5.6 | -3.7 | -1.7 | -0.2 | -0.1 |
| MOTILALOFS | -5.3 | +0.0 | -4.3 | -1.4 | +0.3 |
| BSE | -4.4 | +0.0 | -3.2 | -1.8 | +0.6 |
| YESBANK | -3.9 | +0.0 | -3.1 | -0.3 | -0.6 |
| GROWW | -3.9 | +0.0 | -2.7 | -1.6 | +0.5 |
| INDUSINDBK | -3.7 | -1.6 | -2.2 | +0.0 | +0.0 |
| NYKAA | -3.7 | -2.2 | -1.3 | -0.1 | -0.0 |
| BAJFINANCE | -3.7 | -0.3 | -2.3 | -0.5 | -0.5 |
| ICICIAMC | -3.5 | +0.0 | -3.4 | -0.3 | +0.2 |
| SHRIRAMFIN | -3.4 | -1.8 | -1.5 | -0.1 | -0.1 |
| SBIN | -3.4 | +0.0 | -3.1 | -0.2 | -0.1 |
| JIOFIN | -3.1 | +0.0 | -2.7 | -0.3 | -0.2 |
| ADANIENSOL | -3.1 | +0.0 | -2.6 | -0.4 | -0.1 |

Share of absolute impact by order: 1: 16%, 2: 67%, 3: 12%, 4: 5%

## Sources
- 2026-10-26 Silver prices fall 53% from peak: Should buyers wait or buy now? https://news.google.com/rss/search?q=Silver+prices+fall+53%+from+peak:+Should+buyers+wait+or+buy+now?&hl=en-IN&gl=IN&ceid=IN:en
- 2026-10-31 Silver loses more than half its value from record high: What went wrong and will it recover? https://news.google.com/rss/search?q=Silver+loses+more+than+half+its+value+from+record+high:+What+went+wrong+and+will+it+recover?&hl=en-IN&gl=IN&ceid=IN:en
- 2026-10-28 Gold heads for its biggest yearly drop in 11 years as the Iran war lifts yields and the dollar https://news.google.com/rss/search?q=Gold+heads+for+its+biggest+yearly+drop+in+11+years+as+the+Iran+war+lifts+yields+and+the+dollar&hl=en-IN&gl=IN&ceid=IN:en
- 2026-10-28 Fed holds interest rates steady - investors bet on December rate hike https://news.google.com/rss/search?q=Fed+holds+interest+rates+steady+-+investors+bet+on+December+rate+hike&hl=en-IN&gl=IN&ceid=IN:en
- 2026-10-19 Gold's path to $6,000 and silver's return above $90 depend on renewed investor confidence - Metals Focus https://news.google.com/rss/search?q=Gold's+path+to+$6,000+and+silver's+return+above+$90+depend+on+renewed+investor+confidence+-+Metals+Focus&hl=en-IN&gl=IN&ceid=IN:en
- 2026-10-29 Silver could see further losses against gold as physical market weakens - Metals Focus https://news.google.com/rss/search?q=Silver+could+see+further+losses+against+gold+as+physical+market+weakens+-+Metals+Focus&hl=en-IN&gl=IN&ceid=IN:en