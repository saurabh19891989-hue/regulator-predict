# Union Budget 2027-28 capex/railway allocation (infra, railways, defence) (`EV_BUDGET27_CAPEX_RAILWAY`)
*sector_policy · status scheduled · date 2027-02-01 · P(3m) 0.0 · P(12m) 0.9 · confidence low*

Budget will set FY28 capex, railways and defence outlays. Base case: central capex growth ~10% and railways capex up high single digits (model assumption; no fetched figures). Vande Bharat sleeper completed 160 kmph Kavach trial (10 Sep 2026), supporting the order pipeline.

**Review override applied:** LEVEL booked as a SURPRISE. The description says 'base case: central capex growth ~10% ... (model assumption; no fetched figures)'. Yet the shocks are F_GOVT_CAPEX +0.8 (SSU +10% capex growth), i.e. the expected growth itself, plus P_DEFENCE_PROCUREMENT +1.0 (+10% domestic orders) at p=0.9. A scheduled budget moves stocks only by its deviation from expectations. Expectations are already high: MoD is publicly seeking the steepest modernisation hike in a decade (up to 35%, Business Standard 9 Oct, Defence.in 16 Oct) on top of FY27's record Rs7.85 lakh cr / Rs2.19 lakh cr modernisation (Feb 2026). Fiscal room is tight: H1 FY27 deficit 42.1% of target, overshoot risk up to Rs1.2 lakh cr (ET 30 Oct, 2 Nov). This one event is the largest forward item for MAZDOCK (+7.2 expected), BEL (+6.4), BDL (+5.8), POWERINDIA (+3.5), SAIL (+3.4) and ENRIN (+2.8). Keep p=0.9 and use surprise-sized shocks.

**Already moved:** n/a

## Entry shocks (conditional on the event)
- `F_GOVT_CAPEX` Central + state government capex: 0.2 SSU (range -0.3…0.6) surprise vs ~10% expected capex growth
- `P_RAILWAY_CAPEX` Railway capex: 0.2 SSU (range -0.2…0.6) surprise only
- `P_DEFENCE_PROCUREMENT` Indian defence procurement & indigenisation: 0.3 SSU (range -0.3…1.0) surprise vs MoD's publicised ask

## Causal chains (agent)
- order 3: EV_BUDGET27_CAPEX_RAILWAY → P_RAILWAY_CAPEX → IRCON — Railway outlays flow to wagon/track/signalling contractors
- order 4: EV_BUDGET27_CAPEX_RAILWAY → F_GOVT_CAPEX → P_INFRA_SPENDING_ROADS → LT — Capex lifts order inflow for EPC and cement

## Most positively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| MAZDOCK | +2.3 | +2.3 | +0.0 | -0.0 | -0.0 |
| BEL | +2.1 | +2.0 | +0.1 | +0.0 | -0.0 |
| HAL | +2.1 | +2.0 | +0.1 | -0.0 | -0.0 |
| BDL | +1.9 | +1.8 | +0.1 | -0.0 | -0.0 |
| RVNL | +1.7 | +1.8 | -0.0 | -0.0 | -0.0 |
| SOLARINDS | +1.4 | +1.2 | +0.2 | -0.0 | -0.0 |
| LT | +1.1 | +1.1 | +0.0 | +0.0 | -0.0 |
| POWERINDIA | +1.0 | +1.0 | -0.0 | -0.0 | +0.0 |
| BHARATFORG | +1.0 | +0.9 | +0.1 | +0.0 | -0.0 |
| SAIL | +1.0 | +0.7 | +0.2 | -0.0 | -0.0 |
| BHEL | +1.0 | +0.9 | +0.0 | +0.0 | +0.0 |
| TMCV | +0.9 | +0.8 | +0.1 | +0.0 | -0.0 |
| CGPOWER | +0.9 | +0.8 | +0.1 | +0.0 | +0.0 |
| COCHINSHIP | +0.8 | +0.9 | -0.0 | -0.0 | -0.0 |
| ENRIN | +0.8 | +0.8 | -0.0 | +0.0 | +0.0 |

## Most negatively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| PERSISTENT | -0.1 | +0.0 | +0.0 | -0.1 | -0.0 |
| TECHM | -0.1 | +0.0 | +0.0 | -0.1 | -0.0 |
| MARUTI | -0.1 | +0.0 | -0.1 | -0.0 | -0.0 |
| TCS | -0.1 | +0.0 | +0.0 | -0.0 | -0.0 |
| SUZLON | -0.1 | +0.0 | -0.1 | -0.0 | -0.0 |
| HEROMOTOCO | -0.0 | +0.0 | -0.0 | -0.0 | +0.0 |
| HYUNDAI | -0.0 | +0.0 | -0.0 | +0.0 | -0.0 |
| BOSCHLTD | -0.0 | +0.0 | -0.0 | -0.0 | -0.0 |
| M&M | -0.0 | +0.0 | -0.0 | -0.0 | -0.0 |
| PREMIERENE | -0.0 | +0.0 | +0.0 | -0.0 | -0.0 |
| SRF | -0.0 | +0.0 | +0.0 | -0.0 | -0.0 |
| BAJAJ-AUTO | -0.0 | +0.0 | -0.0 | +0.0 | -0.0 |
| VAML | -0.0 | +0.0 | +0.0 | +0.0 | -0.0 |
| JUBLFOOD | -0.0 | +0.0 | +0.0 | -0.0 | +0.0 |
| GROWW | -0.0 | +0.0 | +0.0 | -0.0 | +0.0 |

Share of absolute impact by order: 1: 61%, 2: 17%, 3: 18%, 4: 5%

## Sources
- 2026-09-12 Vande Bharat sleeper Kavach trial (headline) https://www.livemint.com/