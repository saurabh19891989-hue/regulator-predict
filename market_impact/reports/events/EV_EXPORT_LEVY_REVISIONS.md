# Windfall/export levy re-set: petrol nil, diesel Rs11.5/l, ATF ~Rs11/l (31 Oct); excise reportedly cut (3 Nov, unverified) (`EV_EXPORT_LEVY_REVISIONS`)
*sector_policy · status occurred · date 2026-10-31 · P(3m) 1 · P(12m) 1 · confidence low*

Windfall export levies reintroduced in August (raised 3 Aug amid Iran war, cut 14 Aug), cut again 1 Sep, 1 Oct, 17 Sep, adjusted 16 Oct (petrol up, diesel down) and on 31 Oct petrol set to nil, diesel raised Rs3/l to Rs11.5/l, ATF ~Rs11/l. Fortnightly resets track diesel/ATF cracks. NDTV Profit headline of 3 Nov says 'Despite elevated Indian crude basket price, excise duty cut on fuel' - magnitude and whether it is the export levy or retail excise NOT verified.

**Already moved:** Levy on diesel exports directly trims exporter realisation (Reliance, Nayara) by roughly the levy minus normal; RELIANCE share reaction not measured.

## Entry shocks (conditional on the event)
- `P_WINDFALL_EXPORT_TAX` Windfall / export taxes on commodities: 1.0 SSU (range 0.5…1.0) levy in force on diesel/ATF; petrol exports free
- `P_FUEL_TAX_IN` Fuel excise / retail price policy (+ = higher taxes/regulated squeeze): -0.5 SSU (range -1.0…0.0) possible small excise cut; unverified

## Causal chains (agent)
- order 2: EV_EXPORT_LEVY_REVISIONS → P_WINDFALL_EXPORT_TAX → F_REFINING_MARGIN — levy caps diesel crack capture by exporters
- order 3: EV_EXPORT_LEVY_REVISIONS → P_WINDFALL_EXPORT_TAX → F_REFINING_MARGIN → F_USDINR — lower export earnings dollar inflow marginally
- order 3: EV_EXPORT_LEVY_REVISIONS → P_FUEL_TAX_IN → NEW_OMC_MARKETING_MARGIN — lower excise cushions marketing margin without retail hike

## Most positively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| INDIGO | +0.8 | +0.4 | +0.4 | -0.0 | +0.0 |
| VMM | +0.3 | +0.0 | +0.3 | +0.0 | -0.0 |
| MRF | +0.2 | +0.0 | +0.2 | +0.0 | -0.0 |
| JUBLFOOD | +0.0 | +0.0 | +0.0 | +0.0 | -0.0 |
| GODREJPROP | +0.0 | +0.0 | +0.0 | +0.0 | -0.0 |
| LENSKART | +0.0 | +0.0 | +0.0 | +0.0 | -0.0 |
| SUZLON | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| MARUTI | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| SWIGGY | +0.0 | +0.0 | +0.0 | +0.0 | -0.0 |
| GRASIM | +0.0 | +0.0 | +0.0 | +0.0 | -0.0 |
| ETERNAL | +0.0 | +0.0 | +0.0 | +0.0 | -0.0 |
| HEROMOTOCO | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| TVSMOTOR | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| NYKAA | +0.0 | +0.0 | +0.0 | +0.0 | -0.0 |
| WAAREEENER | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |

## Most negatively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| RELIANCE | -3.4 | -3.0 | -0.4 | +0.0 | +0.0 |
| IOC | -1.3 | -0.3 | -1.0 | +0.0 | -0.0 |
| HINDPETRO | -0.8 | +0.3 | -1.2 | +0.0 | -0.0 |
| BPCL | -0.7 | +0.5 | -1.2 | +0.0 | +0.0 |
| ONGC | -0.6 | +0.0 | -0.6 | -0.0 | +0.0 |
| OIL | -0.4 | +0.0 | -0.4 | -0.0 | +0.0 |
| BANKINDIA | -0.1 | +0.0 | +0.0 | -0.1 | +0.0 |
| JINDALSTEL | -0.1 | +0.0 | +0.0 | -0.1 | -0.0 |
| PNB | -0.1 | +0.0 | +0.0 | -0.1 | -0.0 |
| PFC | -0.1 | +0.0 | +0.0 | -0.1 | -0.0 |
| UNIONBANK | -0.1 | +0.0 | +0.0 | -0.1 | -0.0 |
| POWERINDIA | -0.1 | +0.0 | +0.0 | -0.1 | +0.0 |
| MAHABANK | -0.1 | +0.0 | +0.0 | -0.1 | +0.0 |
| POWERGRID | -0.1 | +0.0 | +0.0 | -0.1 | +0.0 |
| SAIL | -0.1 | +0.0 | +0.0 | -0.0 | -0.0 |

Share of absolute impact by order: 1: 28%, 2: 36%, 3: 30%, 4: 7%

## Sources
- 2026-10-31 Govt hikes windfall tax on diesel, ATF exports; petrol levy cut to zero (Moneycontrol) (headline via Google News RSS; article body not read) https://news.google.com/rss/search?q=windfall+tax+India+diesel+ATF+export+duty+31+October+when:120d&hl=en-IN&gl=IN&ceid=IN:en
- 2026-11-03 Excise Duty Cut On Fuel (NDTV Profit) (headline via Google News RSS; article body not read) https://news.google.com/rss/search?q=Despite+Elevated+Indian+Crude+Oil+Basket+Price+Excise+Duty+Cut+when:120d&hl=en-IN&gl=IN&ceid=IN:en