# CPI prints >=6.0% (RBI upper tolerance) in Oct-Jan data (releases 12 Nov - 12 Feb) (`EV_CPI_BREACH_6PCT`)
*india_macro · status anticipated · date 2026-11-12 · P(3m) 0.5 · P(12m) 0.6 · confidence low*

Sep CPI 5.54% with food 7.74%; NDTV Profit (21 Oct) says inflation 'heads to 6% ceiling'. Model knowledge (low confidence): late-2025 base prints were extremely low in the old CPI series, implying adverse base effects through Q4 2026 - not verified for the new 2024=100 series. Oil has eased (Brent -5.6% in 1m), rupee stable; offsets. Probability = at least one print >=6.0% in Oct, Nov, Dec or Jan data.

## Entry shocks (conditional on the event)
- `F_CPI_IN` India CPI inflation: 0.5 SSU (range 0.2…0.9) from 5.54% to >=6.0%
- `F_REPO_IN` RBI repo rate: 0.4 SSU (range 0.0…0.8) policy-path pressure
- `F_GSEC_10Y_IN` India 10-year G-sec yield: 0.5 SSU (range 0.1…1.0) term premium

## Causal chains (agent)
- order 2: EV_CPI_BREACH_6PCT → F_CPI_IN → F_REPO_IN — Breach of tolerance band forces explicit hikes
- order 3: EV_CPI_BREACH_6PCT → F_CPI_IN → F_REPO_IN → F_CREDIT_GROWTH_IN — Hikes cool credit
- order 4: EV_CPI_BREACH_6PCT → F_CPI_IN → F_REPO_IN → F_HOUSING_DEMAND → DLF — Mortgage rates -> housing sales -> developer valuations
- order 4: EV_CPI_BREACH_6PCT → F_CPI_IN → F_REPO_IN → F_GSEC_10Y_IN → F_FPI_FLOWS — Real-rate rise helps debt flows, hurts equity multiples

## Most positively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| PIIND | +0.2 | +0.0 | +0.1 | +0.0 | +0.0 |
| UPL | +0.1 | +0.0 | +0.1 | -0.0 | +0.0 |
| NATIONALUM | +0.0 | -0.2 | +0.3 | -0.0 | +0.0 |
| OIL | +0.0 | -0.2 | +0.3 | -0.0 | +0.0 |
| HINDCOPPER | +0.0 | -0.2 | +0.3 | -0.0 | -0.0 |
| MCX | +0.0 | +0.0 | +0.1 | -0.0 | -0.0 |
| ONGC | +0.0 | -0.2 | +0.3 | -0.0 | +0.0 |
| NMDC | -0.0 | -0.2 | +0.2 | +0.0 | -0.0 |
| LUPIN | -0.1 | -0.2 | +0.1 | +0.0 | -0.0 |
| DRREDDY | -0.1 | -0.3 | +0.2 | +0.0 | -0.0 |
| HINDALCO | -0.1 | -0.2 | +0.2 | -0.1 | +0.0 |
| TMPV | -0.2 | -0.2 | +0.1 | -0.1 | +0.1 |
| SAIL | -0.2 | -0.5 | +0.1 | +0.2 | +0.0 |
| TATASTEEL | -0.2 | -0.4 | +0.1 | +0.1 | +0.0 |
| JSWSTEEL | -0.2 | -0.5 | +0.2 | +0.1 | +0.0 |

## Most negatively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| YESBANK | -4.5 | -2.7 | -1.0 | -0.6 | -0.2 |
| BAJFINANCE | -4.0 | -2.5 | -1.3 | -0.1 | -0.1 |
| TATACAP | -3.8 | -2.5 | -1.0 | -0.3 | -0.1 |
| GMRAIRPORT | -3.5 | -2.5 | -0.6 | -0.7 | +0.2 |
| IREDA | -3.1 | -2.5 | -0.4 | -0.2 | -0.0 |
| PRESTIGE | -3.0 | -2.1 | -0.7 | -0.1 | -0.1 |
| PHOENIXLTD | -2.9 | -2.7 | -0.2 | -0.1 | -0.0 |
| JSWENERGY | -2.8 | -2.5 | -0.2 | -0.1 | -0.0 |
| GODREJPROP | -2.8 | -1.4 | -1.2 | -0.1 | -0.1 |
| JIOFIN | -2.8 | -2.1 | -0.4 | -0.2 | -0.1 |
| AUBANK | -2.7 | -1.8 | -0.6 | -0.3 | -0.1 |
| SHRIRAMFIN | -2.7 | -1.8 | -0.5 | -0.6 | +0.1 |
| BAJAJFINSV | -2.7 | -1.8 | -0.8 | -0.0 | -0.1 |
| LODHA | -2.6 | -1.4 | -1.0 | -0.1 | -0.1 |
| ADANIGREEN | -2.6 | -2.2 | -0.2 | -0.1 | -0.1 |

Share of absolute impact by order: 1: 64%, 2: 21%, 3: 11%, 4: 4%

## Sources
- 2026-10-21 Not A One-Off: RBI MPC Minutes Point To A Rate-Hike Cycle As Inflation Heads To 6% Ceiling - NDTV Profit https://news.google.com/rss/search?q=India+CPI+inflation+September+2026+6%25+ceiling+when:120d&hl=en-IN&gl=IN&ceid=IN:en
- 2026-10-12 India Sept inflation nears RBI tolerance ceiling - Reuters https://news.google.com/rss/search?q=India+inflation+September+2026+Reuters+poll+when:120d&hl=en-IN&gl=IN&ceid=IN:en