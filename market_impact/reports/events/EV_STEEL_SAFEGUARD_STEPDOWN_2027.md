# Scheduled step-down of India's steel safeguard duty (12% -> 11.5%) in year two (`EV_STEEL_SAFEGUARD_STEPDOWN_2027`)
*metals_china · status scheduled · date 2027-04-21 · P(3m) 0.0 · P(12m) 0.95 · confidence low*

Safeguard duty on flat steel imports: provisional 12% from 21 Apr 2025; final 3-year duty notified 31 Dec 2025 (Mint/BS) with a declining schedule (12%, 11.5%, 11%; model knowledge, exact year boundaries not verified). Expiry ~Apr 2028, i.e. renewal is a 2028 question. Step-down is small (-0.5 pp) and largely priced; the important variable is whether government accelerates relief if prices inflate (HRC at four-year high) - separate low-probability scenario below.

**Review override applied:** The final duty was notified 30-31 Dec 2025: 12% (21 Apr 2025-20 Apr 2026), 11.5% (21 Apr 2026-20 Apr 2027), 11% (21 Apr 2027-20 Apr 2028). The 2027 step is 11.5% -> 11%, not '12% -> 11.5%' as the description says. It is notified law, so p ~0.95. The steel ministry signalled no change (Reuters 6 Oct). The shock size of -0.05 is fine.

## Entry shocks (conditional on the event)
- `P_STEEL_DUTY_IN` Indian safeguard/anti-dumping duty on steel imports: -0.05 SSU (range -0.08…0.0) -0.5 pp / SSU 10 pp

## Causal chains (agent)
- order 2: EV_STEEL_SAFEGUARD_STEPDOWN_2027 → P_STEEL_DUTY_IN → F_STEEL_INDIA → SAIL — Marginally lowers import parity price.
- order 3: EV_STEEL_SAFEGUARD_STEPDOWN_2027 → F_STEEL_INDIA → F_CPI_IN → F_REPO_IN — Negligible inflation effect.

## Most positively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| TMCV | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| BHEL | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| MARUTI | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| ASHOKLEY | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| SUZLON | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| RVNL | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| COCHINSHIP | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| HYUNDAI | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| TIINDIA | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| TVSMOTOR | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| HEROMOTOCO | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| BOSCHLTD | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| PRESTIGE | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| ADANIENSOL | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| CUMMINSIND | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |

## Most negatively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| JINDALSTEL | -0.3 | +0.0 | -0.3 | +0.0 | +0.0 |
| SAIL | -0.2 | -0.1 | -0.2 | +0.0 | +0.0 |
| JSWSTEEL | -0.2 | -0.1 | -0.1 | +0.0 | +0.0 |
| TATASTEEL | -0.2 | +0.0 | -0.2 | +0.0 | +0.0 |
| NMDC | -0.1 | -0.1 | -0.0 | +0.0 | +0.0 |
| VMM | -0.0 | +0.0 | +0.0 | +0.0 | -0.0 |
| AUROPHARMA | -0.0 | +0.0 | +0.0 | +0.0 | -0.0 |
| DRREDDY | -0.0 | +0.0 | +0.0 | +0.0 | -0.0 |
| HINDCOPPER | -0.0 | +0.0 | +0.0 | +0.0 | -0.0 |
| LUPIN | -0.0 | +0.0 | +0.0 | +0.0 | -0.0 |
| NATIONALUM | -0.0 | +0.0 | +0.0 | +0.0 | -0.0 |
| OIL | -0.0 | +0.0 | +0.0 | +0.0 | -0.0 |
| ONGC | -0.0 | +0.0 | +0.0 | +0.0 | -0.0 |
| VAML | -0.0 | +0.0 | +0.0 | +0.0 | -0.0 |
| BIOCON | -0.0 | +0.0 | +0.0 | +0.0 | -0.0 |

Share of absolute impact by order: 1: 15%, 2: 80%, 3: 2%, 4: 2%

## Sources
- 2025-12-31 Centre imposes steel safeguard duty for 3 years; up to 12% on imports https://news.google.com/rss/search?q=Centre+imposes+steel+safeguard+duty+for+3+years;+up+to+12%+on+imports&hl=en-IN&gl=IN&ceid=IN:en
- 2026-08-06 Safeguard duty, higher prices to keep steel makers' profitability steady https://news.google.com/rss/search?q=Safeguard+duty,+higher+prices+to+keep+steel+makers'+profitability+steady&hl=en-IN&gl=IN&ceid=IN:en