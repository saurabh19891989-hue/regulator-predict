# Reservoir storage at multi-year low after weak monsoon (south India worst) (`EV_RESERVOIR_LOW26`)
*agri_rural · status occurred · date 2026-10-15 · P(3m) 1.0 · P(12m) 1.0 · confidence high*

CWC bulletin of 15 Oct 2026: 178 major reservoirs hold 126.717 BCM = 68.58% of live capacity, 41.19 BCM (24.5%) below the same date last year and ~24.9 BCM below the 10-year average. On 24 Sep, storage was 70% vs 10-yr average 76.62% and 79% in 2025 (Indian Express: lowest in 10 years). South India (AP, Telangana, Karnataka, Kerala, TN) was at ~50% vs 87% a year ago; Pennar and Cauvery basins are most stressed (Mettur, Somasila, Aliyar critical), while Narmada and Mahanadi basins have surplus. Raises rabi irrigation, drinking-water and hydropower risks for Jan-Jun 2027.

**Already moved:** No direct price series; supports weak rabi sowing (EV_RABI_SOWING_LAG26) and hydro generation shortfall.

## Entry shocks (conditional on the event)
- `F_MONSOON` Monsoon rainfall vs normal: -0.3 SSU (range -0.6…-0.1) Carry-over effect on irrigation-dependent rabi crop (kept small to avoid double count with EV_SWMONSOON26_DEFICIT).
- `F_POWER_PRICE_IN` Indian power exchange (IEX) prices: 0.3 SSU (range 0.0…0.7) Lower hydro availability and higher summer demand lift exchange prices (SSU +15%).

## Causal chains (agent)
- order 2: EV_RESERVOIR_LOW26 → F_MONSOON → F_FOOD_INFLATION_IN — Lower irrigation water reduces rabi wheat/pulses/oilseed yields and pushes up cereal/vegetable prices.
- order 3: EV_RESERVOIR_LOW26 → F_POWER_PRICE_IN → F_COAL_INDIA — Less hydro raises coal-fired dispatch and e-auction coal demand.
- order 4: EV_RESERVOIR_LOW26 → F_FOOD_INFLATION_IN → F_CPI_IN → F_GSEC_10Y_IN — Persistent food inflation keeps long yields elevated.

## Most positively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| ADANIPOWER | +1.4 | +1.3 | +0.1 | -0.0 | -0.0 |
| COALINDIA | +0.7 | +0.0 | +0.5 | +0.3 | -0.1 |
| ENRIN | +0.6 | +0.0 | +0.5 | +0.2 | -0.1 |
| JSWENERGY | +0.5 | +0.5 | +0.1 | +0.0 | -0.1 |
| TATAPOWER | +0.4 | +0.2 | +0.3 | +0.1 | -0.1 |
| BHEL | +0.4 | +0.0 | +0.5 | +0.0 | -0.1 |
| ADANIENSOL | +0.4 | +0.1 | +0.3 | +0.2 | -0.1 |
| POWERGRID | +0.3 | +0.0 | +0.3 | +0.1 | -0.1 |
| WAAREEENER | +0.3 | +0.0 | +0.3 | +0.0 | -0.1 |
| ADANIGREEN | +0.3 | +0.2 | +0.2 | -0.0 | -0.1 |
| NLCINDIA | +0.3 | +0.1 | +0.2 | +0.0 | -0.1 |
| NTPC | +0.2 | +0.1 | +0.2 | -0.0 | -0.1 |
| SUZLON | +0.2 | +0.0 | +0.3 | +0.1 | -0.1 |
| AMBUJACEM | +0.2 | +0.2 | +0.0 | +0.0 | -0.0 |
| POWERINDIA | +0.2 | +0.0 | +0.0 | +0.4 | -0.2 |

## Most negatively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| INDUSINDBK | -2.1 | +0.0 | -0.6 | -1.1 | -0.4 |
| IDFCFIRSTB | -1.8 | +0.0 | -0.5 | -0.9 | -0.4 |
| YESBANK | -1.5 | +0.0 | -0.4 | -0.7 | -0.4 |
| BANKINDIA | -1.2 | +0.0 | -0.3 | -0.8 | -0.1 |
| M&MFIN | -1.2 | -0.8 | -0.2 | -0.2 | -0.1 |
| AXISBANK | -1.1 | +0.0 | -0.3 | -0.6 | -0.2 |
| SBICARD | -1.1 | +0.0 | -0.4 | -0.3 | -0.3 |
| KOTAKBANK | -1.1 | +0.0 | -0.3 | -0.6 | -0.1 |
| INDIANB | -1.0 | +0.0 | -0.3 | -0.6 | -0.2 |
| HDFCBANK | -1.0 | +0.0 | -0.3 | -0.6 | -0.2 |
| MAHABANK | -1.0 | +0.0 | -0.2 | -0.7 | -0.1 |
| SBIN | -1.0 | +0.0 | -0.3 | -0.6 | -0.1 |
| SHRIRAMFIN | -1.0 | -0.6 | -0.1 | -0.2 | -0.1 |
| AUBANK | -1.0 | +0.0 | -0.3 | -0.4 | -0.3 |
| UNIONBANK | -1.0 | +0.0 | -0.3 | -0.6 | -0.1 |

Share of absolute impact by order: 1: 11%, 2: 29%, 3: 34%, 4: 26%

## Sources
- 2026-09-28 At 70%, India's water reserves at 10-year low - Indian Express https://indianexpress.com/article/india/central-water-commission-cwc-live-reservoir-storage-report-september-seventy-percent-capacity-south-india-crisis-el-nino-10898033/
- 2026-10-19 CWC 15 Oct: 68.58% of capacity, 24.5% below last year https://www.downtoearth.org.in/water/indias-reservoirs-remain-31-below-full-capacity-after-monsoon-southern-states-face-water-shortages