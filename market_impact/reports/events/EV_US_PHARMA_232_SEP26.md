# US Section 232 pharma tariff (100%) takes effect 29 Sep 2026; select Indian speciality drugs/ingredients exempted (`EV_US_PHARMA_232_SEP26`)
*geopolitics_trade · status occurred · date 2026-09-29 · P(3m) 1 · P(12m) 1 · confidence medium*

Section 232 pharmaceutical tariffs entered into force 29 Sep 2026. A waiver covers select speciality drugs from ~20 countries including India. In July Trump had threatened a 200% tariff on generics; generics so far not hit (Indian firms argue US needs low-cost generics). Sun Pharma reportedly offered cheaper drugs to the administration (MFN-style pricing deals). Exact HS scope of exemptions and generics treatment not verified from primary text.

**Already moved:** No quantified index move retrieved; generic exposure treated as a live tail (see EV_PHARMA_GENERICS_TARIFF).

## Entry shocks (conditional on the event)
- `P_US_PHARMA_TARIFF` US tariffs on pharmaceuticals: 0.5 SSU (range 0.2…1.0) branded/speciality tariff in force with India carve-outs; generics spared (SSU=+10pp on Indian pharma exports; effective average small)

## Causal chains (agent)
- order 2: EV_US_PHARMA_232_SEP26 → P_US_PHARMA_TARIFF → F_US_GENERIC_PRICING — Tariff on competitors' branded products and MFN deals shift US pricing power; generic price erosion pressure persists.
- order 3: EV_US_PHARMA_232_SEP26 → P_US_PHARMA_TARIFF → F_US_GENERIC_PRICING → SUNPHARMA — Speciality-heavy exporters (Sun, Lupin, Zydus) carry the exemption-dependency risk.

## Most positively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| CIPLA | -0.0 | -0.2 | +0.2 | +0.0 | +0.0 |
| LUPIN | -0.2 | -0.5 | +0.3 | +0.0 | +0.0 |
| DRREDDY | -0.2 | -0.4 | +0.2 | +0.0 | +0.0 |
| TORNTPHARM | -0.2 | -0.2 | +0.1 | +0.0 | +0.0 |
| GLENMARK | -0.2 | -0.4 | +0.2 | +0.0 | +0.0 |
| ZYDUSLIFE | -0.5 | -0.8 | +0.2 | +0.0 | +0.0 |
| DIVISLAB | -0.7 | -0.8 | +0.1 | +0.0 | +0.0 |
| LAURUSLABS | -0.7 | -0.8 | +0.1 | +0.0 | +0.0 |
| SUNPHARMA | -0.9 | -1.0 | +0.1 | +0.0 | +0.0 |
| AUROPHARMA | -1.2 | -1.5 | +0.3 | +0.0 | +0.0 |
| BIOCON | -1.4 | -1.5 | +0.2 | +0.0 | +0.0 |

## Most negatively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| BIOCON | -1.4 | -1.5 | +0.2 | +0.0 | +0.0 |
| AUROPHARMA | -1.2 | -1.5 | +0.3 | +0.0 | +0.0 |
| SUNPHARMA | -0.9 | -1.0 | +0.1 | +0.0 | +0.0 |
| LAURUSLABS | -0.7 | -0.8 | +0.1 | +0.0 | +0.0 |
| DIVISLAB | -0.7 | -0.8 | +0.1 | +0.0 | +0.0 |
| ZYDUSLIFE | -0.5 | -0.8 | +0.2 | +0.0 | +0.0 |
| GLENMARK | -0.2 | -0.4 | +0.2 | +0.0 | +0.0 |
| TORNTPHARM | -0.2 | -0.2 | +0.1 | +0.0 | +0.0 |
| DRREDDY | -0.2 | -0.4 | +0.2 | +0.0 | +0.0 |
| LUPIN | -0.2 | -0.5 | +0.3 | +0.0 | +0.0 |
| CIPLA | -0.0 | -0.2 | +0.2 | +0.0 | +0.0 |

Share of absolute impact by order: 1: 81%, 2: 19%, 3: 0%, 4: 0%

## Sources
- 2026-09-29 US waives 100% tariff on select Indian speciality drugs - The Indian Express https://news.google.com/rss/search?q=Section+232+pharma+tariff+generic+when:120d&hl=en-IN&gl=IN&ceid=IN:en
- 2026-07-22 Trump's 200% generic tariff threat would imperil Americans: Indian pharma - The Hindu https://news.google.com/rss/search?q=Trump+pharma+tariff+India+when:120d&hl=en-IN&gl=IN&ceid=IN:en