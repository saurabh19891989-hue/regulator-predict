# CPI prints >=6.0% (RBI upper tolerance) in Oct-Jan data (releases 12 Nov - 12 Feb) (`EV_CPI_BREACH_6PCT`)
*india_macro · status anticipated · date 2026-11-12 · P(3m) 0.5 · P(12m) 0.6 · confidence low*

Sep CPI 5.54% with food 7.74%; NDTV Profit (21 Oct) says inflation 'heads to 6% ceiling'. Model knowledge (low confidence): late-2025 base prints were extremely low in the old CPI series, implying adverse base effects through Q4 2026 - not verified for the new 2024=100 series. Oil has eased (Brent -5.6% in 1m), rupee stable; offsets. Probability = at least one print >=6.0% in Oct, Nov, Dec or Jan data.

**Review override applied:** Double count of the RBI reaction. RT_EVENTS set EV_RBI_DEC26_HIKE25 (0.42) / FEB27 (0.27) with 'the 12 Nov Oct CPI print is the swing factor'. The breach event's own F_REPO_IN +0.4 SSU (p 0.6) books the same hike a second time. Keeping F_REPO_IN in entry_shocks at 0 clamps it, so CPI->REPO no longer propagates inside this event. GSEC 0.5 -> 0.3 removes the hike-expectation part. Prob unchanged.

## Entry shocks (conditional on the event)
- `F_CPI_IN` India CPI inflation: 0.5 SSU (range 0.2…0.9) Oct CPI >6% (unchanged)
- `F_REPO_IN` RBI repo rate: 0.0 SSU (range 0.0…0.0) CLAMPED at 0: the RBI response is carried by EV_RBI_DEC26_HIKE25/EV_RBI_FEB27_HIKE25 odds, which RT_EVENTS set with the 12 Nov CPI print as the swing factor
- `F_GSEC_10Y_IN` India 10-year G-sec yield: 0.3 SSU (range 0.0…0.7) inflation-risk premium only; hike-expectation part (~0.2) moved to the MPC events

## Causal chains (agent)
- order 2: EV_CPI_BREACH_6PCT → F_CPI_IN → F_REPO_IN — Breach of tolerance band forces explicit hikes
- order 3: EV_CPI_BREACH_6PCT → F_CPI_IN → F_REPO_IN → F_CREDIT_GROWTH_IN — Hikes cool credit
- order 4: EV_CPI_BREACH_6PCT → F_CPI_IN → F_REPO_IN → F_HOUSING_DEMAND → DLF — Mortgage rates -> housing sales -> developer valuations
- order 4: EV_CPI_BREACH_6PCT → F_CPI_IN → F_REPO_IN → F_GSEC_10Y_IN → F_FPI_FLOWS — Real-rate rise helps debt flows, hurts equity multiples

## Most positively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| JSWSTEEL | +0.3 | +0.0 | +0.2 | +0.0 | +0.0 |
| LAURUSLABS | +0.3 | +0.0 | +0.4 | -0.0 | -0.0 |
| ONGC | +0.3 | +0.0 | +0.3 | -0.0 | +0.0 |
| NATIONALUM | +0.3 | +0.0 | +0.3 | +0.0 | +0.0 |
| OIL | +0.3 | +0.0 | +0.3 | +0.0 | +0.0 |
| DRREDDY | +0.3 | +0.0 | +0.3 | +0.0 | +0.0 |
| HINDCOPPER | +0.3 | +0.0 | +0.3 | -0.0 | -0.0 |
| SAIL | +0.3 | +0.0 | +0.1 | +0.1 | +0.0 |
| LUPIN | +0.2 | +0.0 | +0.2 | +0.0 | -0.0 |
| PIIND | +0.2 | +0.0 | +0.2 | +0.0 | +0.0 |
| TATASTEEL | +0.2 | +0.0 | +0.2 | +0.1 | +0.0 |
| GLENMARK | +0.2 | +0.0 | +0.2 | +0.0 | -0.0 |
| NMDC | +0.2 | +0.0 | +0.2 | +0.0 | -0.0 |
| SRF | +0.2 | +0.0 | +0.2 | -0.0 | +0.0 |
| TMPV | +0.2 | +0.0 | +0.2 | -0.1 | +0.1 |

## Most negatively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| ADANIGREEN | -1.4 | -1.1 | -0.2 | -0.1 | -0.0 |
| SBIN | -1.4 | -1.0 | -0.2 | -0.1 | +0.0 |
| BAJFINANCE | -1.3 | -0.8 | -0.7 | +0.1 | +0.0 |
| JIOFIN | -1.3 | -0.9 | -0.2 | -0.2 | -0.0 |
| TATACAP | -1.3 | -0.8 | -0.4 | -0.2 | +0.0 |
| IREDA | -1.3 | -0.9 | -0.2 | -0.2 | +0.0 |
| YESBANK | -1.3 | -0.4 | -0.6 | -0.3 | +0.1 |
| GMRAIRPORT | -1.1 | -0.8 | -0.4 | -0.2 | +0.2 |
| PHOENIXLTD | -1.1 | -1.0 | -0.1 | -0.0 | +0.0 |
| DMART | -1.1 | -0.7 | -0.4 | +0.1 | -0.0 |
| ICICIGI | -1.0 | -0.9 | -0.1 | -0.1 | +0.0 |
| ADANIENT | -1.0 | -0.8 | -0.1 | -0.2 | +0.1 |
| IDFCFIRSTB | -1.0 | -0.4 | -0.6 | -0.2 | +0.1 |
| GROWW | -1.0 | -0.8 | -0.2 | -0.0 | -0.0 |
| IDEA | -1.0 | -0.6 | -0.3 | -0.2 | +0.0 |

Share of absolute impact by order: 1: 45%, 2: 31%, 3: 16%, 4: 7%

## Sources
- 2026-10-21 Not A One-Off: RBI MPC Minutes Point To A Rate-Hike Cycle As Inflation Heads To 6% Ceiling - NDTV Profit https://news.google.com/rss/search?q=India+CPI+inflation+September+2026+6%25+ceiling+when:120d&hl=en-IN&gl=IN&ceid=IN:en
- 2026-10-12 India Sept inflation nears RBI tolerance ceiling - Reuters https://news.google.com/rss/search?q=India+inflation+September+2026+Reuters+poll+when:120d&hl=en-IN&gl=IN&ceid=IN:en