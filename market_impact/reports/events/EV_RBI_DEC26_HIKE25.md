# RBI MPC Dec 2026 (~4 Dec): hikes repo another 25 bp to 5.75% (`EV_RBI_DEC26_HIKE25`)
*india_macro · status scheduled · date 2026-12-04 · P(3m) 0.42 · P(12m) 0.42 · confidence low*

Meeting date approximate (MPC calendar not retrieved; early Dec by convention). Evidence for: Oct stance change to calibrated tightening; minutes (21 Oct) flag more hikes; Bloomberg 7 Oct 'back-to-back hikes'; ET 29 Sep sees 5.75% soon; CPI rising toward 6%; broadening inflation. Against: 2 MPC members opposed the stance shift; minutes show wariness of an aggressive cycle; Brent -5.6% in 1 month and rupee stable; Nifty fragile; Governor links further hikes to growth-inflation outlook. My odds for Dec: hike 25 bp 0.40, hold 0.57, hike 50 bp 0.02, cut 0.01. The Oct CPI print (12 Nov) is the swing input.

**Review override applied:** Dates confirmed by RBI: decision 4 Dec 2026, Feb decision 5 Feb 2027. Hawkish voices: SBI chair backs a 50 bp Dec hike (3 Nov), UOB sees consecutive hikes from Dec, HSBC 6% by Dec. Since then Brent fell from $117 to $95, the 10y G-sec rallied 7.44% -> 7.19% (4 Nov) and the rupee is at a 2-week high (~94.35-94.55). Odds: 25 bp 0.42, 50 bp 0.05, hold 0.52, cut 0.01. The 12 Nov Oct CPI print is the swing factor.

## Entry shocks (conditional on the event)
- `F_REPO_IN` RBI repo rate: 1.0 SSU (range 1.0…1.0) +25 bp
- `F_GSEC_10Y_IN` India 10-year G-sec yield: 0.3 SSU (range -0.2…0.8) partly priced
- `F_CREDIT_SPREADS_IN` Indian corporate credit spreads: 0.2 SSU (range 0.0…0.4) NBFC funding

## Causal chains (agent)
- order 2: EV_RBI_DEC26_HIKE25 → F_REPO_IN → F_CREDIT_GROWTH_IN — Credit slows
- order 3: EV_RBI_DEC26_HIKE25 → F_REPO_IN → F_AUTO_DEMAND_IN → MARUTI — Vehicle-loan rates -> auto volumes
- order 4: EV_RBI_DEC26_HIKE25 → F_REPO_IN → F_HOUSING_DEMAND → F_URBAN_DEMAND → DLF — Housing -> urban wealth/demand
- order 3: EV_RBI_DEC26_HIKE25 → F_REPO_IN → F_USDINR → F_CPI_IN — Carry support for rupee limits imported inflation

## Most positively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| LICHSGFIN | +1.2 | +1.9 | -0.7 | +0.1 | -0.1 |
| BANKINDIA | +0.6 | +1.6 | -0.8 | -0.1 | -0.1 |
| PAYTM | +0.5 | +0.8 | -0.3 | +0.1 | -0.1 |
| MAHABANK | +0.0 | +1.1 | -0.7 | -0.1 | -0.2 |
| UNIONBANK | -0.1 | +0.6 | -0.5 | -0.0 | -0.1 |
| PNB | -0.1 | +0.6 | -0.5 | -0.0 | -0.1 |
| UPL | -0.1 | +0.0 | -0.1 | -0.0 | +0.0 |
| GROWW | -0.1 | -0.2 | +0.0 | +0.1 | +0.1 |
| MCX | -0.1 | +0.0 | -0.1 | +0.0 | -0.0 |
| KOTAKBANK | -0.1 | +0.8 | -0.6 | -0.1 | -0.1 |
| SBIN | -0.1 | +0.4 | -0.4 | +0.0 | -0.1 |
| BANKBARODA | -0.2 | +0.1 | -0.4 | +0.2 | -0.1 |
| PIIND | -0.2 | +0.0 | -0.2 | -0.0 | +0.0 |
| POLICYBZR | -0.3 | +0.0 | -0.0 | -0.2 | -0.1 |
| TCS | -0.3 | -0.3 | -0.1 | -0.0 | +0.1 |

## Most negatively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| BAJFINANCE | -5.4 | -4.8 | -0.7 | +0.2 | -0.1 |
| TATACAP | -5.3 | -4.5 | -0.8 | +0.2 | -0.1 |
| PRESTIGE | -5.2 | -4.5 | -0.6 | +0.1 | -0.1 |
| YESBANK | -5.1 | -4.2 | -0.8 | +0.0 | -0.1 |
| GODREJPROP | -4.5 | -3.7 | -0.8 | +0.0 | -0.1 |
| IREDA | -4.3 | -4.0 | -0.3 | +0.1 | -0.1 |
| JSWENERGY | -4.2 | -4.2 | +0.0 | +0.0 | -0.0 |
| BAJAJFINSV | -3.8 | -3.4 | -0.5 | +0.1 | -0.1 |
| M&MFIN | -3.7 | -3.2 | -0.5 | +0.0 | -0.1 |
| AUBANK | -3.7 | -3.0 | -0.7 | +0.2 | -0.2 |
| LTF | -3.5 | -3.2 | -0.3 | +0.1 | -0.1 |
| LODHA | -3.5 | -2.6 | -0.8 | +0.1 | -0.1 |
| OBEROIRLTY | -3.4 | -2.9 | -0.5 | -0.0 | -0.1 |
| JIOFIN | -3.3 | -3.0 | -0.3 | +0.1 | -0.1 |
| SHRIRAMFIN | -3.2 | -2.2 | -0.7 | -0.2 | -0.1 |

Share of absolute impact by order: 1: 79%, 2: 14%, 3: 4%, 4: 3%

## Sources
- 2026-10-07 India Set for Back-to-Back Rate Hikes - Bloomberg https://news.google.com/rss/search?q=RBI+rate+hike+December+2026+expected+economists+when:120d&hl=en-IN&gl=IN&ceid=IN:en
- 2026-10-21 India rate panel flags more hikes but wary of aggressive cycle - Reuters https://news.google.com/rss/search?q=RBI+MPC+minutes+more+hikes+wary+aggressive+cycle+when:120d&hl=en-IN&gl=IN&ceid=IN:en
- 2026-09-29 RBI may face two hikes, one dilemma - Economic Times https://news.google.com/rss/search?q=RBI+may+face+two+hikes+one+dilemma+repo+5.75%25+when:120d&hl=en-IN&gl=IN&ceid=IN:en