# RBI tightens gold-loan / unsecured and NBFC-bank lending norms after early stress (`EV_RBI_GOLD_LOAN_TIGHTEN`)
*sector_policy · status risk_scenario · date 2027-01-31 · P(3m) 0.1 · P(12m) 0.3 · confidence low*

Reuters (21 Oct 2026): top NBFCs flag early stress in gold loans; RBI governor (11 Sep) said RBI never intended NBFCs to offer revolving credit; NBFC bank-borrowing dependence rising (RBI Bulletin). RBI already finalised gold-loan norms in 2025 (model knowledge). Odds are judgement.

**Review override applied:** A full +1 prudential step for a gold-loan rule hits every bank and NBFC with weights calibrated to unrelated rules. PFC (power lender, no gold loans) takes -2.5 conditional. CANBK takes -4.5 and BOB -3.5, weights calibrated to the bank ECL transition. MUTHOOTFIN also carries the same scenario as a company event (fix in findings). Cut the generic shock to 0.4 and keep the gold-lender-specific part in MUTHOOTFIN's company event (prob aligned to 0.3). Reuters 2026-10-21: NBFCs flag early gold-loan stress. ET 2026-11-02: the Muthoot MD attributes the NPA rise to the 2025 rule change. No new RBI proposal found.

**Already moved:** Not quantified.

## Entry shocks (conditional on the event)
- `P_RBI_PRUDENTIAL` RBI prudential tightening (risk weights, LCR, provisioning): 0.4 SSU (range 0.2…0.8) generic part only (NBFC-bank lending norms); gold-loan-specific hit carried by gold-lender company events
- `F_UNSECURED_STRESS` Unsecured retail & microfinance stress (higher = worse): 0.3 SSU (range 0.0…0.8) delinquency drift (unchanged)
- `F_GOLD_DEMAND_IN` Indian jewellery/gold demand volume: -0.3 SSU (range -1.0…0.0) gold loan availability (unchanged)

## Causal chains (agent)
- order 3: EV_RBI_GOLD_LOAN_TIGHTEN → P_RBI_PRUDENTIAL → F_CREDIT_GROWTH_IN → MUTHOOTFIN — Lower LTVs and tighter disbursal slow gold-loan AUM growth
- order 4: EV_RBI_GOLD_LOAN_TIGHTEN → F_UNSECURED_STRESS → F_ASSET_QUALITY_IN → BAJFINANCE — Spillover raises credit costs across NBFC unsecured books

## Most positively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| POWERGRID | +0.1 | +0.0 | +0.0 | +0.0 | +0.0 |
| BSE | +0.1 | +0.0 | +0.0 | +0.0 | +0.0 |
| SUZLON | +0.1 | +0.0 | +0.0 | +0.0 | +0.0 |
| RVNL | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| POWERINDIA | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| PREMIERENE | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| WAAREEENER | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| MAZDOCK | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| NLCINDIA | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| INDUSTOWER | +0.0 | +0.0 | +0.0 | -0.0 | +0.0 |
| HAL | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| ASTRAL | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| HDFCAMC | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| BDL | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| AMBUJACEM | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |

## Most negatively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| INDUSINDBK | -4.9 | -3.0 | -1.7 | -0.1 | -0.1 |
| IDFCFIRSTB | -4.1 | -2.5 | -1.5 | -0.0 | -0.1 |
| SBICARD | -3.5 | -3.0 | -0.4 | -0.1 | -0.0 |
| BANKINDIA | -3.5 | -2.0 | -1.3 | -0.1 | -0.1 |
| TATACAP | -3.2 | -2.2 | -1.1 | -0.0 | +0.0 |
| BAJFINANCE | -3.2 | -2.2 | -0.9 | -0.1 | +0.1 |
| AUBANK | -2.9 | -2.0 | -1.0 | +0.0 | -0.0 |
| AXISBANK | -2.8 | -1.6 | -1.1 | -0.1 | -0.1 |
| YESBANK | -2.8 | -1.4 | -1.4 | +0.0 | -0.0 |
| ABCAPITAL | -2.8 | -1.8 | -0.9 | -0.0 | -0.0 |
| FEDERALBNK | -2.7 | -1.4 | -1.2 | -0.0 | -0.0 |
| CANBK | -2.7 | -1.9 | -0.8 | +0.0 | -0.0 |
| LTF | -2.7 | -1.9 | -0.7 | -0.0 | +0.0 |
| BAJAJFINSV | -2.6 | -1.8 | -0.8 | -0.1 | +0.0 |
| UNIONBANK | -2.6 | -1.6 | -0.9 | -0.0 | -0.0 |

Share of absolute impact by order: 1: 53%, 2: 34%, 3: 8%, 4: 5%

## Sources
- 2026-10-21 Top Indian non-bank lenders flag early signs of stress in loans against gold https://www.reuters.com/
- 2026-09-11 RBI never intended NBFCs to offer revolving credit https://www.cnbctv18.com/