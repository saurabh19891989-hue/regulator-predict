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
| UPL | +0.2 | +0.0 | +0.1 | +0.0 | +0.0 |
| NATIONALUM | +0.2 | -0.5 | +0.5 | +0.2 | +0.0 |
| OIL | +0.2 | -0.5 | +0.5 | +0.1 | +0.0 |
| VAML | +0.1 | +0.0 | -0.2 | +0.2 | +0.1 |
| TECHM | +0.0 | +0.0 | +0.1 | -0.1 | +0.0 |
| TCS | +0.0 | +0.0 | +0.1 | -0.1 | +0.0 |
| HINDZINC | -0.1 | +0.0 | -0.3 | +0.1 | +0.1 |
| HINDCOPPER | -0.2 | -0.5 | +0.1 | +0.1 | +0.0 |
| NMDC | -0.2 | -0.6 | +0.3 | +0.0 | +0.0 |
| PERSISTENT | -0.2 | +0.0 | -0.1 | -0.2 | +0.0 |
| SUNPHARMA | -0.3 | +0.0 | -0.2 | -0.1 | +0.0 |
| HCLTECH | -0.5 | +0.0 | -0.4 | -0.1 | +0.0 |
| INFY | -0.5 | +0.0 | -0.4 | -0.1 | +0.0 |
| ONGC | -0.5 | -1.0 | +0.5 | +0.0 | +0.0 |
| COCHINSHIP | -0.5 | -0.7 | +0.2 | -0.0 | +0.0 |

## Most negatively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| YESBANK | -19.1 | -9.0 | -9.1 | -1.1 | +0.1 |
| INDUSINDBK | -17.1 | -6.3 | -11.0 | -0.4 | +0.6 |
| IDFCFIRSTB | -16.4 | -6.3 | -10.2 | -0.4 | +0.4 |
| AUBANK | -13.5 | -4.1 | -9.2 | -0.3 | +0.1 |
| TATACAP | -13.4 | -3.0 | -9.7 | -1.1 | +0.3 |
| BAJFINANCE | -13.3 | -3.0 | -9.0 | -1.6 | +0.3 |
| SHRIRAMFIN | -13.2 | -7.0 | -5.0 | -1.2 | +0.1 |
| AXISBANK | -12.0 | -4.8 | -6.9 | -0.6 | +0.2 |
| TMCV | -11.1 | -7.5 | -2.4 | -1.0 | -0.1 |
| M&MFIN | -10.9 | -5.7 | -5.1 | -0.4 | +0.3 |
| GMRAIRPORT | -10.8 | -6.0 | -2.4 | -2.1 | -0.3 |
| FEDERALBNK | -10.6 | +0.5 | -11.0 | -0.6 | +0.5 |
| INDIANB | -10.5 | -4.2 | -5.8 | -0.6 | +0.1 |
| HDFCBANK | -10.4 | -4.2 | -5.7 | -0.6 | +0.2 |
| LTF | -10.3 | -4.4 | -5.8 | -0.6 | +0.5 |

Share of absolute impact by order: 1: 42%, 2: 44%, 3: 11%, 4: 3%

## Sources
- 2026-10-07 Four horsemen of economic trouble? RBI governor flags the risks - ET https://news.google.com/rss/search?q=India+stagflation+risk+growth+inflation+2026+RBI+Governor+four+horsemen+when:120d&hl=en-IN&gl=IN&ceid=IN:en