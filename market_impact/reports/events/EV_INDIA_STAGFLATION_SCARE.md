# Risk: stagflation scare - CPI >=6.5% while GDP growth slips below ~6% (Q3 FY27 data, late Feb 2027) (`EV_INDIA_STAGFLATION_SCARE`)
*india_macro · status risk_scenario · date 2027-02-27 · P(3m) 0.04 · P(12m) 0.12 · confidence low*

Combination of persistent oil, El Nino food shock, imported inflation and credit tightening. Two MPC members already resisted the stance change (growth worry). Q3 FY27 GDP due ~late Feb 2027 (date approximate). P(by 12m) 0.12 is a judgement.

## Entry shocks (conditional on the event)
- `F_CPI_IN` India CPI inflation: 1.0 SSU (range 0.6…1.5) CPI to ~6.5%
- `F_GDP_IN` India real GDP growth: -1.5 SSU (range -2.5…-0.8) quarterly growth ~6%
- `F_REPO_IN` RBI repo rate: 1.0 SSU (range 0.0…2.0) policy dilemma
- `F_RURAL_DEMAND` Rural consumption growth: -0.8 SSU (range -1.5…-0.2) 

## Causal chains (agent)
- order 2: EV_INDIA_STAGFLATION_SCARE → F_CPI_IN → F_REPO_IN — Policy tightens into slowdown
- order 3: EV_INDIA_STAGFLATION_SCARE → F_CPI_IN → F_REPO_IN → F_CREDIT_GROWTH_IN — Credit slows
- order 3: EV_INDIA_STAGFLATION_SCARE → F_RURAL_DEMAND → F_AUTO_DEMAND_IN → M&M — Rural squeeze
- order 4: EV_INDIA_STAGFLATION_SCARE → F_GDP_IN → F_FPI_FLOWS → F_USDINR → F_CPI_IN — Lower growth hits flows, weak rupee reinforces inflation

## Most positively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| VAML | +0.2 | +0.0 | -0.2 | +0.2 | +0.1 |
| NATIONALUM | +0.2 | -0.5 | +0.5 | +0.2 | +0.0 |
| UPL | +0.2 | +0.0 | +0.1 | +0.0 | +0.0 |
| OIL | +0.2 | -0.5 | +0.5 | +0.1 | +0.0 |
| TECHM | +0.1 | +0.0 | +0.1 | -0.1 | +0.0 |
| TCS | +0.0 | +0.0 | +0.1 | -0.1 | +0.0 |
| HINDZINC | -0.1 | +0.0 | -0.3 | +0.1 | +0.0 |
| PERSISTENT | -0.2 | +0.0 | -0.1 | -0.2 | +0.1 |
| SUNPHARMA | -0.3 | +0.0 | -0.2 | -0.1 | +0.1 |
| NMDC | -0.3 | -0.6 | +0.3 | +0.0 | +0.0 |
| HINDCOPPER | -0.3 | -0.5 | +0.1 | +0.0 | +0.0 |
| HCLTECH | -0.5 | +0.0 | -0.4 | -0.1 | +0.0 |
| INFY | -0.5 | +0.0 | -0.4 | -0.1 | +0.0 |
| COCHINSHIP | -0.5 | -0.7 | +0.2 | +0.0 | +0.0 |
| MCX | -0.5 | +0.0 | -0.4 | -0.2 | +0.1 |

## Most negatively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| YESBANK | -17.8 | -9.0 | -9.1 | -0.2 | +0.5 |
| INDUSINDBK | -16.6 | -6.3 | -11.0 | +0.1 | +0.6 |
| IDFCFIRSTB | -15.6 | -6.3 | -10.2 | +0.3 | +0.5 |
| AUBANK | -13.8 | -4.1 | -9.2 | -0.5 | +0.1 |
| TATACAP | -13.4 | -3.0 | -9.7 | -1.0 | +0.3 |
| BAJFINANCE | -13.0 | -3.0 | -9.0 | -1.3 | +0.3 |
| SHRIRAMFIN | -11.6 | -5.8 | -5.0 | -1.1 | +0.2 |
| AXISBANK | -11.6 | -4.8 | -6.9 | -0.3 | +0.3 |
| TMCV | -11.0 | -7.5 | -2.4 | -0.9 | -0.2 |
| M&MFIN | -11.0 | -5.7 | -5.1 | -0.4 | +0.2 |
| IREDA | -10.2 | -2.5 | -7.8 | -0.7 | +0.8 |
| HDFCBANK | -10.2 | -4.2 | -5.7 | -0.5 | +0.3 |
| CHOLAFIN | -10.0 | -2.5 | -7.1 | -0.5 | +0.1 |
| LTF | -10.0 | -4.4 | -5.8 | -0.3 | +0.5 |
| INDIANB | -9.9 | -4.2 | -5.8 | -0.1 | +0.3 |

Share of absolute impact by order: 1: 42%, 2: 45%, 3: 10%, 4: 3%

## Sources
- 2026-10-07 Four horsemen of economic trouble? RBI governor flags the risks - ET https://news.google.com/rss/search?q=India+stagflation+risk+growth+inflation+2026+RBI+Governor+four+horsemen+when:120d&hl=en-IN&gl=IN&ceid=IN:en