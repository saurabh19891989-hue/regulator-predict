# SEBI tightens F&O further (weekly-expiry scrapping, higher margins/lot sizes) (`EV_SEBI_FNO_CURBS_RISK`)
*sector_policy · status risk_scenario · date 2027-02-15 · P(3m) 0.07 · P(12m) 0.2 · confidence low*

Media (31 Aug 2026) discuss scrapping weekly expiries; SEBI already limited weekly expiries to one benchmark per exchange (2024-25). A further tightening step would cut retail F&O volumes. Probability is a judgement from discussion pieces, not a SEBI proposal.

**Already moved:** n/a

## Entry shocks (conditional on the event)
- `P_SEBI_DERIVATIVES` SEBI F&O / market-structure tightening: 1.0 SSU (range 0.5…1.5) tightening
- `F_EQUITY_ACTIVITY_IN` Indian equity market volumes & retail activity: -1.0 SSU (range -2.0…-0.3) retail turnover falls ~20%

## Causal chains (agent)
- order 3: EV_SEBI_FNO_CURBS_RISK → P_SEBI_DERIVATIVES → F_EQUITY_ACTIVITY_IN → BSE — Lower option premium turnover cuts exchange transaction revenue
- order 4: EV_SEBI_FNO_CURBS_RISK → F_EQUITY_ACTIVITY_IN → ANGELONE — Broker revenue and active clients fall

## Most positively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| LICI | +0.3 | +0.0 | +0.2 | +0.1 | +0.0 |
| GODREJPROP | +0.3 | +0.0 | +0.1 | +0.1 | +0.0 |
| LODHA | +0.3 | +0.0 | +0.1 | +0.1 | +0.0 |
| PRESTIGE | +0.3 | +0.0 | +0.1 | +0.1 | +0.0 |
| HDFCLIFE | +0.2 | +0.0 | +0.1 | +0.1 | +0.0 |
| DLF | +0.2 | +0.0 | +0.1 | +0.1 | +0.0 |
| OBEROIRLTY | +0.2 | +0.0 | +0.1 | +0.1 | +0.0 |
| SBILIFE | +0.2 | +0.0 | +0.1 | +0.1 | +0.0 |
| PAYTM | +0.2 | +0.0 | +0.0 | +0.2 | +0.0 |
| PHOENIXLTD | +0.2 | +0.0 | +0.1 | +0.1 | +0.0 |
| SBIN | +0.2 | +0.0 | +0.0 | +0.2 | +0.0 |
| INDUSINDBK | +0.2 | +0.0 | +0.0 | +0.2 | +0.0 |
| FEDERALBNK | +0.2 | +0.0 | +0.0 | +0.2 | -0.0 |
| POLICYBZR | +0.2 | +0.0 | +0.0 | +0.2 | -0.0 |
| MAHABANK | +0.2 | +0.0 | +0.0 | +0.2 | +0.0 |

## Most negatively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| GROWW | -16.6 | -17.0 | +0.3 | +0.1 | +0.0 |
| BSE | -16.5 | -17.0 | +0.4 | +0.1 | +0.0 |
| MOTILALOFS | -8.6 | -9.0 | +0.3 | +0.2 | +0.0 |
| MCX | -8.0 | -8.0 | +0.0 | +0.0 | +0.0 |
| 360ONE | -4.7 | -5.0 | +0.2 | +0.1 | +0.0 |
| ICICIAMC | -2.6 | -3.0 | +0.3 | +0.1 | +0.0 |
| JIOFIN | -1.7 | -1.8 | +0.0 | +0.1 | +0.0 |
| HDFCAMC | -1.0 | -1.2 | +0.2 | +0.1 | +0.0 |
| NAUKRI | -0.9 | -1.0 | +0.0 | +0.1 | +0.0 |
| KOTAKBANK | -0.8 | -0.8 | +0.0 | +0.0 | +0.0 |
| NATIONALUM | -0.0 | +0.0 | +0.0 | +0.0 | -0.0 |
| OIL | -0.0 | +0.0 | +0.0 | +0.0 | -0.0 |
| ONGC | -0.0 | +0.0 | +0.0 | +0.0 | -0.0 |
| VAML | -0.0 | +0.0 | +0.0 | +0.0 | -0.0 |
| JSWSTEEL | -0.0 | +0.0 | +0.0 | +0.0 | -0.0 |

Share of absolute impact by order: 1: 81%, 2: 4%, 3: 14%, 4: 2%

## Sources
- 2026-08-31 How scrapping weekly F&O expiries could reshape retail trading https://news.google.com/rss/search?q=SEBI+F%26O+weekly+expiry+rules