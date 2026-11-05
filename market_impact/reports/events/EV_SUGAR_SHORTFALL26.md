# Sugar supply shock: 2025-26 output cut to ~306 lakh t, retail sugar at record, first duty-free raw sugar imports in a decade (`EV_SUGAR_SHORTFALL26`)
*agri_rural · status occurred · date 2026-08-20 · P(3m) 1.0 · P(12m) 1.0 · confidence medium*

Food ministry (21-22 Aug): 2025-26 (Oct-Sep) sugar output ~306 lakh t, 11% below the 343 lakh t initial projection; opening stock 1 Oct 2026 ~33-34 lakh t vs 50 lakh t a year earlier. Retail sugar Rs 58.2/kg, +20% in a month and +26% y/y. DGFT (20 Aug) allowed duty-free import of 10 lakh t raw sugar under a TRQ until 31 Oct; stockholding limits on bulk traders were considered; fortnightly sale quotas to mills from September; mills told to report output monthly (Oct). ISMA (24-26 Aug, 26 Oct) says no shortage and that stocks are sufficient; 107 mills began crushing 2026-27 by 26 Oct. FRP for 2026-27 raised only Rs 10/q; mills and ISMA seek a sugar MSP (minimum selling price, Rs 31/kg since 2019 - model knowledge) increase; Karnataka cane farmers protesting. Centre set up a panel to review sugar prices/farmers' payments. Global raw sugar (ICE proxy) +27.8% since 1 Jun but -11.3% in 1m (18.47 c/lb on 5 Nov).

**Already moved:** ICE sugar: +27.0% 6m, +27.8% since 2026-06-01, -11.3% 1m, +18.6% 3m (factor_state); Indian retail +26% y/y.

## Entry shocks (conditional on the event)
- `F_SUGAR` Sugar price: 2.8 SSU (range 2.0…3.2) Realised +27.8% since 1 Jun in ICE raw sugar (SSU +10%); Indian ex-mill prices rose similarly.
- `P_SUGAR_ETHANOL` Sugar export / ethanol blending policy: -0.5 SSU (range -1.0…0.0) Policy tilted against millers: duty-free imports, stock limits, ethanol diversion curbed (see ethanol event).

## Causal chains (agent)
- order 2: EV_SUGAR_SHORTFALL26 → F_SUGAR → F_FOOD_INFLATION_IN — Sugar weight small (about 1% of CPI) but visible in WPI food and festive sweet prices.
- order 3: EV_SUGAR_SHORTFALL26 → F_SUGAR → F_FOOD_INFLATION_IN → F_CPI_IN — Contributes a few bp to CPI.
- order 3: EV_SUGAR_SHORTFALL26 → F_SUGAR → P_SUGAR_ETHANOL — Government prioritises consumer prices over miller margins, raising odds of import/stock-limit measures whenever prices spike.

## Most positively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| OFSS | +0.8 | +0.8 | +0.0 | +0.0 | +0.0 |
| RADICO | +0.4 | +0.4 | +0.0 | +0.0 | +0.0 |
| NESTLEIND | -0.8 | -0.8 | +0.0 | +0.0 | +0.0 |
| DABUR | -1.1 | -1.1 | +0.0 | +0.0 | +0.0 |
| BRITANNIA | -2.2 | -2.2 | +0.0 | +0.0 | +0.0 |
| VBL | -2.2 | -2.2 | +0.0 | +0.0 | +0.0 |
| UNITDSPR | -3.0 | -3.0 | +0.0 | +0.0 | +0.0 |

## Most negatively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| UNITDSPR | -3.0 | -3.0 | +0.0 | +0.0 | +0.0 |
| BRITANNIA | -2.2 | -2.2 | +0.0 | +0.0 | +0.0 |
| VBL | -2.2 | -2.2 | +0.0 | +0.0 | +0.0 |
| DABUR | -1.1 | -1.1 | +0.0 | +0.0 | +0.0 |
| NESTLEIND | -0.8 | -0.8 | +0.0 | +0.0 | +0.0 |
| RADICO | +0.4 | +0.4 | +0.0 | +0.0 | +0.0 |
| OFSS | +0.8 | +0.8 | +0.0 | +0.0 | +0.0 |

Share of absolute impact by order: 1: 100%, 2: 0%, 3: 0%, 4: 0%

## Sources
- 2026-08-22 Sugar output may dip 11%: Government - ToI https://timesofindia.indiatimes.com/business/india-business/sugar-output-may-dip-11-from-initial-estimate-government/articleshow/133413529.cms
- 2026-08-20 Duty-free imports of 10 lakh t raw sugar until 31 Oct - AIR https://newsonair.gov.in/government-allows-duty-free-imports-of-10-lakh-tonnes-of-raw-sugar-until-31st-october/
- 2026-08-18 Why India is considering sugar imports - ToI/Reuters https://timesofindia.indiatimes.com/business/india-business/why-india-is-considering-sugar-imports-as-prices-hit-record-levels/articleshow/133318646.cms
- 2026-10-26 ISMA: 107 mills crushing, stock enough https://money.rediff.com/news/market/isma-107-sugar-mills-begin-crushing-ample-stock-for-india/56919320261026
- 2026-09-30 FRP +Rs 10/q for 2026-27 (date approximate) https://agrospectrumindia.com/news/8/33951/isma-welcomes-rs-10-qtl-hike-in-sugarcane-frp-for-2026-27-calls-for-timely-alignment-of-sugar-msp-and-ethanol-prices.html