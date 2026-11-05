# Cabinet approves further LPG under-recovery compensation to OMCs (`EV_LPG_COMPENSATION_CABINET`)
*sector_policy · status anticipated · date 2026-12-15 · P(3m) 0.1 · P(12m) 0.55 · confidence low*

Precedent: compensation boosted IOC Q2 (Reuters 30 Oct). Accumulated burden >Rs59,000 cr (July). Further tranche likely in H2 FY27 but timing and size not sourced.

**Review override applied:** (1) Timing: Moneycontrol (7 Sep 2026) reports 'OMCs seek Rs 75,000 crore for fuel losses; Centre to decide in 2027'. A Dec-2026 decision with p3=0.35 is unsupported; p3 should be ~0.1. (2) Wrong node and unit: a one-off cash compensation is booked as +1 SSU of NEW_OMC_MARKETING_MARGIN, i.e. a persistent +Rs1/l on all petrol and diesel. That gives HPCL +12% and IOC +6.5% per tranche. The profiles already carry a purpose-built node, NEW_OMC_COMPENSATION (HPCL +4.5, IOC +3.2 per Rs25k cr, sized on share of compensation / market cap). (3) Triple channel: HPCL and IOC also hold company_events 'Centre decision on OMC compensation' (see findings). Re-routing cuts the HPCL expected value from +7.2 to ~+3.0 and IOC's from +3.9 to ~+2.1. BPCL has no NEW_OMC_COMPENSATION edge (see findings).

## Entry shocks (conditional on the event)
- `NEW_OMC_COMPENSATION` Government compensation to OMCs for fuel/LPG under-recoveries: 1.2 SSU (range 0.6…3.0) ~Rs30k cr one-off (OMC ask Rs75k cr); SSU +1 = Rs25k cr

## Causal chains (agent)
- order 2: EV_LPG_COMPENSATION_CABINET → NEW_OMC_MARKETING_MARGIN → BPCL — one-off PAT
- order 3: EV_LPG_COMPENSATION_CABINET → NEW_OMC_MARKETING_MARGIN → F_GOVT_CAPEX — fiscal
- order 4: EV_LPG_COMPENSATION_CABINET → F_GOVT_CAPEX → F_GSEC_10Y_IN — borrowing

## Most positively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| HINDPETRO | +5.4 | +5.4 | +0.0 | +0.0 | +0.0 |
| IOC | +3.8 | +3.8 | +0.0 | +0.0 | +0.0 |
| ONGC | -1.2 | -1.2 | +0.0 | +0.0 | +0.0 |

## Most negatively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| ONGC | -1.2 | -1.2 | +0.0 | +0.0 | +0.0 |
| IOC | +3.8 | +3.8 | +0.0 | +0.0 | +0.0 |
| HINDPETRO | +5.4 | +5.4 | +0.0 | +0.0 | +0.0 |

Share of absolute impact by order: 1: 100%, 2: 0%, 3: 0%, 4: 0%

## Sources
- 2026-10-30 Indian Oil's Q2 profit nearly triples on LPG compensation (Reuters) (headline via Google News RSS; article body not read) https://news.google.com/rss/search?q=LPG+under-recovery+compensation+OMC+cabinet+when:120d&hl=en-IN&gl=IN&ceid=IN:en