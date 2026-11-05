# Union Budget 2027-28 capex/railway allocation (infra, railways, defence) (`EV_BUDGET27_CAPEX_RAILWAY`)
*sector_policy · status scheduled · date 2027-02-01 · P(3m) 0.9 · P(12m) 0.9 · confidence low*

Budget will set FY28 capex, railways and defence outlays. Base case: central capex growth ~10% and railways capex up high single digits (model assumption; no fetched figures). Vande Bharat sleeper completed 160 kmph Kavach trial (10 Sep 2026), supporting the order pipeline.

**Review override applied:** Level-as-shock error. The event's own description says 'Base case: central capex growth ~10%' (model assumption) and then books that base case as +0.8 SSU of F_GOVT_CAPEX (SSU = +10% capex growth), +0.8 railway and +1.0 defence (= +10% domestic orders). A scheduled budget that delivers the consensus is not a price shock. Only the surprise should enter. Evidence: FY27 BE capex Rs12.2 lakh cr (The Hindu, 1 Feb 2026); Centre capex +12% in Apr-Sep, fiscal deficit 42.1% of target in H1 (BusinessLine/Business Standard, 30 Oct 2026). As written, the event adds +2.2 to +6.3pp expected 12m to HAL, SOLARINDS, COCHINSHIP, BHEL, KEI, CGPOWER, POLYCAB, GVT&D and JSWSTEEL. Also, 1 Feb 2027 falls inside the 3-month window (to ~5 Feb 2027), so prob_by_3m should equal prob_by_12m rather than 0.0.

**Already moved:** n/a

## Entry shocks (conditional on the event)
- `F_GOVT_CAPEX` Central + state government capex: 0.2 SSU (range -0.5…0.8) surprise vs the ~10% growth everyone expects; fiscal deficit already 42.1% of the FY27 target in H1, so the skew is not up
- `P_RAILWAY_CAPEX` Railway capex: 0.2 SSU (range -0.3…0.8) surprise only
- `P_DEFENCE_PROCUREMENT` Indian defence procurement & indigenisation: 0.3 SSU (range -0.2…1.0) surprise only; budgeted capital outlay growth is expected

## Causal chains (agent)
- order 3: EV_BUDGET27_CAPEX_RAILWAY → P_RAILWAY_CAPEX → IRCON — Railway outlays flow to wagon/track/signalling contractors
- order 4: EV_BUDGET27_CAPEX_RAILWAY → F_GOVT_CAPEX → P_INFRA_SPENDING_ROADS → LT — Capex lifts order inflow for EPC and cement

## Most positively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| MAZDOCK | +2.3 | +2.3 | +0.0 | -0.0 | -0.0 |
| BEL | +2.1 | +2.0 | +0.1 | -0.0 | -0.0 |
| HAL | +2.0 | +2.0 | +0.1 | -0.0 | -0.0 |
| BDL | +1.9 | +1.8 | +0.1 | -0.0 | -0.0 |
| RVNL | +1.7 | +1.8 | -0.0 | -0.0 | -0.0 |
| SOLARINDS | +1.3 | +1.2 | +0.2 | -0.0 | -0.0 |
| LT | +1.1 | +1.1 | +0.0 | -0.0 | -0.0 |
| POWERINDIA | +1.0 | +1.0 | -0.0 | -0.0 | +0.0 |
| SAIL | +0.9 | +0.7 | +0.2 | -0.0 | -0.0 |
| BHARATFORG | +0.9 | +0.9 | +0.1 | +0.0 | -0.0 |
| BHEL | +0.9 | +0.9 | +0.0 | +0.0 | -0.0 |
| TMCV | +0.9 | +0.8 | +0.1 | +0.0 | -0.0 |
| CGPOWER | +0.9 | +0.8 | +0.1 | -0.0 | -0.0 |
| COCHINSHIP | +0.8 | +0.9 | -0.0 | -0.0 | -0.0 |
| ENRIN | +0.8 | +0.8 | -0.0 | -0.0 | +0.0 |

## Most negatively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| PRESTIGE | -0.1 | +0.0 | -0.0 | -0.1 | -0.1 |
| SUZLON | -0.1 | +0.0 | -0.1 | -0.1 | -0.0 |
| JSWENERGY | -0.1 | +0.0 | +0.0 | -0.1 | -0.0 |
| MARUTI | -0.1 | +0.0 | -0.1 | -0.0 | -0.0 |
| PERSISTENT | -0.1 | +0.0 | +0.0 | -0.1 | -0.1 |
| HYUNDAI | -0.1 | +0.0 | -0.0 | -0.0 | -0.0 |
| TECHM | -0.1 | +0.0 | +0.0 | -0.1 | -0.0 |
| LENSKART | -0.1 | +0.0 | +0.0 | -0.1 | -0.0 |
| JUBLFOOD | -0.1 | +0.0 | +0.0 | -0.1 | -0.0 |
| PREMIERENE | -0.1 | +0.0 | +0.0 | -0.1 | -0.0 |
| TCS | -0.1 | +0.0 | +0.0 | -0.0 | -0.0 |
| GODREJPROP | -0.1 | +0.0 | -0.0 | -0.0 | -0.0 |
| SRF | -0.1 | +0.0 | +0.0 | -0.1 | -0.0 |
| GRASIM | -0.1 | +0.0 | +0.0 | -0.1 | -0.0 |
| BOSCHLTD | -0.1 | +0.0 | -0.0 | -0.0 | -0.0 |

Share of absolute impact by order: 1: 60%, 2: 17%, 3: 17%, 4: 6%

## Sources
- 2026-09-12 Vande Bharat sleeper Kavach trial (headline) https://www.livemint.com/