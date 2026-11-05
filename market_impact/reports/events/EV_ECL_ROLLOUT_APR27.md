# RBI expected-credit-loss (ECL) provisioning goes live as scheduled (FY28 start) (`EV_ECL_ROLLOUT_APR27`)
*sector_policy · status scheduled · date 2027-04-01 · P(3m) 0.1 · P(12m) 0.62 · confidence medium*

RBI's ECL framework replaces incurred-loss provisioning. SBI estimates Rs 19,500 crore post-tax hit (3 Nov 2026); Federal Bank flagged 1.5-2% net worth hit (Jul 2026). CS Setty (3 Nov) said RBI working group is still fine-tuning implementation and RBI will meet bank CEOs on readiness. 1 Apr 2027 start date is model knowledge/ not verified in fetched headlines; transition glide-path likely spreads the hit over years.

**Already moved:** No market price reaction isolated; banks' preparedness stories 3-5 Nov 2026.

## Entry shocks (conditional on the event)
- `P_RBI_PRUDENTIAL` RBI prudential tightening (risk weights, LCR, provisioning): 1.0 SSU (range 0.5…1.5) one tightening step, transition-smoothed
- `F_CREDIT_GROWTH_IN` Bank credit growth: -0.5 SSU (range -1.5…0.0) banks price in higher provisions on unsecured/MSME
- `F_ASSET_QUALITY_IN` Credit cost / NPA cycle (higher = worse): 0.5 SSU (range 0.0…1.5) reported credit cost higher (accounting, not cash)

## Causal chains (agent)
- order 3: EV_ECL_ROLLOUT_APR27 → P_RBI_PRUDENTIAL → F_CREDIT_GROWTH_IN — Higher provisioning lifts lending spreads and trims growth in risky segments
- order 4: EV_ECL_ROLLOUT_APR27 → P_RBI_PRUDENTIAL → F_ASSET_QUALITY_IN → SBIN — Day-1 net worth hit and higher run-rate credit cost hits PSU banks most, which have thinner buffers

## Most positively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| POWERGRID | +0.1 | +0.0 | +0.0 | +0.1 | -0.0 |
| PERSISTENT | +0.1 | +0.0 | +0.0 | +0.1 | +0.0 |
| SUPREMEIND | +0.1 | +0.0 | +0.0 | +0.1 | +0.0 |
| BIOCON | +0.1 | +0.0 | +0.0 | +0.1 | +0.0 |
| BSE | +0.1 | +0.0 | +0.0 | +0.1 | -0.0 |
| JINDALSTEL | +0.1 | +0.0 | +0.0 | +0.1 | +0.0 |
| TECHM | +0.1 | +0.0 | +0.0 | +0.0 | +0.0 |
| TCS | +0.1 | +0.0 | +0.0 | +0.0 | +0.0 |
| INDUSTOWER | +0.0 | +0.0 | +0.0 | +0.1 | -0.0 |
| LICI | +0.0 | +0.0 | +0.1 | -0.0 | -0.0 |
| RVNL | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| HDFCLIFE | +0.0 | +0.0 | +0.1 | -0.1 | -0.0 |
| HDFCAMC | +0.0 | +0.0 | +0.0 | +0.0 | -0.0 |
| PIIND | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| AUROPHARMA | +0.0 | +0.0 | +0.0 | +0.0 | -0.0 |

## Most negatively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| INDUSINDBK | -11.3 | -12.0 | +0.8 | +0.0 | -0.0 |
| BANKINDIA | -10.3 | -10.5 | +0.2 | +0.0 | -0.0 |
| IDFCFIRSTB | -9.9 | -10.8 | +0.8 | +0.0 | -0.0 |
| YESBANK | -8.6 | -9.0 | +0.3 | +0.1 | +0.0 |
| CANBK | -8.5 | -8.6 | +0.1 | +0.0 | -0.0 |
| FEDERALBNK | -8.3 | -8.5 | +0.2 | +0.1 | -0.0 |
| TATACAP | -8.0 | -8.0 | -0.2 | +0.1 | +0.0 |
| AXISBANK | -8.0 | -8.2 | +0.3 | +0.0 | -0.0 |
| UNIONBANK | -7.8 | -8.0 | +0.2 | +0.0 | -0.0 |
| ABCAPITAL | -7.5 | -7.2 | -0.3 | +0.1 | +0.0 |
| AUBANK | -7.2 | -7.8 | +0.5 | +0.0 | +0.0 |
| MAHABANK | -7.2 | -7.2 | +0.1 | +0.0 | -0.0 |
| IREDA | -7.1 | -7.0 | -0.4 | +0.2 | +0.0 |
| PNB | -7.0 | -7.2 | +0.2 | +0.0 | -0.0 |
| BANKBARODA | -6.9 | -7.1 | +0.1 | +0.0 | -0.0 |

Share of absolute impact by order: 1: 84%, 2: 11%, 3: 4%, 4: 1%

## Sources
- 2026-11-03 SBI puts ECL models in place, estimates Rs 19,500-crore post-tax impact (headline via Google News) https://www.moneycontrol.com/
- 2026-07-17 Federal Bank flags 1.5-2% net-worth hit from RBI ECL norms (headline) https://www.ndtvprofit.com/