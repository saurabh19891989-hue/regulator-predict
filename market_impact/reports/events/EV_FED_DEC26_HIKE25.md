# FOMC 8-9 Dec 2026: 25 bp hike to 4.00-4.25% (`EV_FED_DEC26_HIKE25`)
*global_macro · status scheduled · date 2026-12-09 · P(3m) 0.72 · P(12m) 0.72 · confidence medium*

FOMC meets 8-9 Dec (fed calendar, with SEP). Reuters 20 Oct: nearly all economists expected a Dec hike; Cook and Hammack dissented for a hike on 28 Oct; 3.7% CPI, 3.4% GDP. Against: weak Sept payrolls (+29k), falling oil/yields after midterms, Trump pressure on Warsh, AI selloff. Hike 0.58, hold 0.42 (our judgment; check Nov 6 jobs report and 10 Dec CPI).

**Review override applied:** Futures price a December hike at ~77-80% after the midterms (TokenPost 4 Nov 76.9%; BigGo 5 Nov ~80%). ADP Oct +86k beat. Warsh says inflation is 'too high'. Shaded slightly below market for the oil collapse and the 6 Nov payrolls risk. 0.58 was below market pricing.

**Already moved:** n/a

## Entry shocks (conditional on the event)
- `F_FED_FUNDS` US Fed funds rate: 1.0 SSU (range 1.0…1.0) +25 bp
- `F_US_10Y` US 10-year Treasury yield: 0.3 SSU (range 0.0…0.6) already largely priced
- `F_DXY` US dollar index: 0.3 SSU (range 0.1…0.6) dollar bid

## Causal chains (agent)
- order 2: EV_FED_DEC26_HIKE25 → F_FED_FUNDS → F_US_10Y → F_FPI_FLOWS — yield rise draws money from EM
- order 3: EV_FED_DEC26_HIKE25 → F_DXY → F_USDINR → F_CPI_IN — INR pressure and imported inflation
- order 4: EV_FED_DEC26_HIKE25 → F_FED_FUNDS → F_US_GDP → C_USA → INFY — tighter policy slows US growth and tech budgets with a lag

## Most positively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| LICHSGFIN | +0.7 | +1.0 | -0.1 | -0.2 | -0.0 |
| OIL | +0.1 | +0.0 | +0.1 | +0.0 | -0.0 |
| MANKIND | +0.1 | +0.4 | -0.3 | -0.1 | -0.0 |
| NMDC | +0.1 | +0.0 | +0.0 | +0.1 | +0.0 |
| ONGC | +0.1 | +0.0 | +0.1 | +0.0 | +0.0 |
| PIIND | +0.1 | +0.0 | +0.1 | -0.0 | +0.0 |
| JSWSTEEL | +0.1 | +0.0 | -0.0 | +0.1 | +0.0 |
| VOLTAS | +0.0 | +0.0 | +0.2 | -0.2 | -0.0 |
| SAIL | +0.0 | +0.0 | -0.1 | +0.1 | +0.0 |
| COCHINSHIP | +0.0 | +0.0 | -0.0 | +0.0 | +0.0 |
| COALINDIA | -0.0 | +0.0 | -0.0 | +0.0 | +0.0 |
| DRREDDY | -0.0 | +0.0 | -0.0 | +0.0 | -0.0 |
| SRF | -0.0 | +0.0 | -0.0 | +0.0 | +0.0 |
| TMPV | -0.0 | +0.0 | -0.0 | -0.0 | +0.0 |
| JINDALSTEL | -0.0 | +0.0 | -0.1 | +0.1 | +0.0 |

## Most negatively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| BSE | -4.3 | -3.0 | -0.8 | -0.4 | -0.0 |
| SWIGGY | -3.1 | -2.5 | -0.5 | -0.1 | -0.0 |
| POLICYBZR | -2.6 | -2.0 | -0.5 | -0.0 | -0.0 |
| MOTILALOFS | -1.8 | +0.0 | -1.4 | -0.3 | -0.0 |
| YESBANK | -1.5 | +0.0 | -1.0 | -0.4 | -0.1 |
| MUTHOOTFIN | -1.4 | +0.0 | -1.2 | -0.2 | -0.0 |
| MPHASIS | -1.4 | -0.9 | -0.4 | -0.1 | +0.0 |
| PERSISTENT | -1.4 | -1.0 | -0.3 | -0.1 | -0.0 |
| NAUKRI | -1.4 | +0.0 | -1.1 | -0.3 | -0.0 |
| PRESTIGE | -1.4 | -0.1 | -0.9 | -0.3 | -0.0 |
| COFORGE | -1.3 | -0.7 | -0.5 | -0.1 | +0.0 |
| BAJFINANCE | -1.3 | +0.0 | -0.9 | -0.3 | -0.1 |
| INDUSINDBK | -1.3 | -0.2 | -0.6 | -0.4 | -0.0 |
| BIOCON | -1.3 | -1.0 | -0.2 | -0.0 | +0.0 |
| ICICIAMC | -1.3 | +0.0 | -1.0 | -0.2 | -0.0 |

Share of absolute impact by order: 1: 18%, 2: 60%, 3: 19%, 4: 3%

## Sources
- 2026-10-20 Fed to skip October but raise rates again in December, nearly all economists say - Reuters https://news.google.com/rss/search?q=Fed%20to%20skip%20October%20but%20raise%20rates%20again%20in%20December%2C%20nearly%20all%20economists%20say%20-%20Reuters&hl=en-IN&gl=IN&ceid=IN:en
- 2026-10-28 FOMC calendar https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm
- 2026-10-23 Federal Reserve preview: A pause before a December hike - ING https://news.google.com/rss/search?q=Federal%20Reserve%20preview%3A%20A%20pause%20before%20a%20December%20hike%20-%20ING&hl=en-IN&gl=IN&ceid=IN:en