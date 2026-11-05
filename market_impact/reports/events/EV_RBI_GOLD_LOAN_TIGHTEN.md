# RBI tightens gold-loan / unsecured and NBFC-bank lending norms after early stress (`EV_RBI_GOLD_LOAN_TIGHTEN`)
*sector_policy · status risk_scenario · date 2027-01-31 · P(3m) 0.1 · P(12m) 0.3 · confidence low*

Reuters (21 Oct 2026): top NBFCs flag early stress in gold loans; RBI governor (11 Sep) said RBI never intended NBFCs to offer revolving credit; NBFC bank-borrowing dependence rising (RBI Bulletin). RBI already finalised gold-loan norms in 2025 (model knowledge). Odds are judgement.

**Already moved:** Not quantified.

## Entry shocks (conditional on the event)
- `P_RBI_PRUDENTIAL` RBI prudential tightening (risk weights, LCR, provisioning): 1.0 SSU (range 0.5…1.5) tightening
- `F_UNSECURED_STRESS` Unsecured retail & microfinance stress (higher = worse): 0.3 SSU (range 0.0…0.8) delinquency drift
- `F_GOLD_DEMAND_IN` Indian jewellery/gold demand volume: -0.3 SSU (range -1.0…0.0) gold loan availability

## Causal chains (agent)
- order 3: EV_RBI_GOLD_LOAN_TIGHTEN → P_RBI_PRUDENTIAL → F_CREDIT_GROWTH_IN → MUTHOOTFIN — Lower LTVs and tighter disbursal slow gold-loan AUM growth
- order 4: EV_RBI_GOLD_LOAN_TIGHTEN → F_UNSECURED_STRESS → F_ASSET_QUALITY_IN → BAJFINANCE — Spillover raises credit costs across NBFC unsecured books

## Most positively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| POWERGRID | +0.1 | +0.0 | +0.0 | +0.0 | +0.1 |
| BSE | +0.1 | +0.0 | +0.0 | +0.0 | +0.1 |
| INDUSTOWER | +0.1 | +0.0 | +0.0 | -0.0 | +0.1 |
| SUZLON | +0.1 | +0.0 | +0.0 | +0.0 | +0.0 |
| POWERINDIA | +0.1 | +0.0 | +0.0 | +0.0 | +0.0 |
| BAJAJHLDNG | +0.1 | +0.0 | +0.0 | +0.0 | +0.0 |
| RVNL | +0.1 | +0.0 | +0.0 | +0.0 | +0.0 |
| PREMIERENE | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| HDFCAMC | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| WAAREEENER | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| MAZDOCK | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| PERSISTENT | +0.0 | +0.0 | -0.0 | +0.0 | +0.1 |
| HAL | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| ASTRAL | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| ENRIN | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |

## Most negatively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| INDUSINDBK | -8.6 | -4.8 | -3.6 | -0.1 | -0.1 |
| BANKINDIA | -7.3 | -4.5 | -2.7 | -0.1 | -0.1 |
| IDFCFIRSTB | -7.3 | -4.0 | -3.3 | +0.1 | -0.1 |
| TATACAP | -6.4 | -4.2 | -2.3 | +0.0 | +0.1 |
| CANBK | -6.2 | -4.6 | -1.6 | +0.0 | +0.0 |
| BAJFINANCE | -6.0 | -4.0 | -2.1 | -0.1 | +0.2 |
| ABCAPITAL | -5.9 | -3.6 | -2.3 | -0.1 | +0.1 |
| SBICARD | -5.8 | -4.8 | -0.8 | -0.2 | -0.0 |
| AUBANK | -5.7 | -3.8 | -2.0 | +0.1 | +0.0 |
| UNIONBANK | -5.6 | -3.7 | -1.9 | +0.0 | -0.0 |
| AXISBANK | -5.6 | -3.1 | -2.4 | -0.1 | -0.0 |
| FEDERALBNK | -5.5 | -3.0 | -2.5 | -0.0 | -0.0 |
| YESBANK | -5.5 | -2.6 | -3.1 | +0.2 | +0.1 |
| BANKBARODA | -5.1 | -3.7 | -1.4 | +0.0 | +0.0 |
| BAJAJFINSV | -5.1 | -3.3 | -1.7 | -0.2 | +0.1 |

Share of absolute impact by order: 1: 53%, 2: 35%, 3: 7%, 4: 5%

## Sources
- 2026-10-21 Top Indian non-bank lenders flag early signs of stress in loans against gold https://www.reuters.com/
- 2026-09-11 RBI never intended NBFCs to offer revolving credit https://www.cnbctv18.com/