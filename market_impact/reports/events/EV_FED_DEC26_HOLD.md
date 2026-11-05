# FOMC 8-9 Dec 2026: hold at 3.75-4.00% (`EV_FED_DEC26_HOLD`)
*global_macro · status scheduled · date 2026-12-09 · P(3m) 0.28 · P(12m) 0.28 · confidence medium*

Complement of the hike event: weak labour data, post-midterm yield decline and lower oil could keep the Fed on hold; Cook/Hammack dissents would likely repeat. Mutually exclusive with EV_FED_DEC26_HIKE25.

**Review override applied:** Complement of the hike (sum 1.0).

**Already moved:** n/a

## Entry shocks (conditional on the event)
- `F_FED_FUNDS` US Fed funds rate: 0.0 SSU (range 0.0…0.0) no change
- `F_US_10Y` US 10-year Treasury yield: -0.4 SSU (range -0.8…0.0) relief vs priced hike
- `F_DXY` US dollar index: -0.3 SSU (range -0.6…0.0) dollar softer

## Causal chains (agent)
- order 2: EV_FED_DEC26_HOLD → F_US_10Y → F_FPI_FLOWS — easier yields support EM flows
- order 3: EV_FED_DEC26_HOLD → F_DXY → F_USDINR → F_REPO_IN — firmer INR gives RBI room to pause
- order 4: EV_FED_DEC26_HOLD → F_FPI_FLOWS → F_EQUITY_ACTIVITY_IN → I_AMC_WEALTH_BROKING — flows boost capital-market activity

## Most positively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| MUTHOOTFIN | +1.2 | +0.0 | +1.2 | +0.0 | -0.0 |
| MOTILALOFS | +1.1 | +0.0 | +1.2 | -0.0 | -0.1 |
| BSE | +1.0 | +0.0 | +0.9 | +0.3 | -0.1 |
| NYKAA | +1.0 | +0.6 | +0.4 | +0.0 | -0.0 |
| ADANIGREEN | +0.9 | +0.0 | +0.9 | +0.1 | -0.0 |
| INDUSINDBK | +0.9 | +0.3 | +0.7 | -0.1 | -0.0 |
| VEDL | +0.9 | +0.3 | +0.3 | +0.0 | +0.2 |
| INDIGO | +0.8 | +0.3 | +0.5 | +0.1 | -0.0 |
| JIOFIN | +0.8 | +0.0 | +0.7 | +0.1 | -0.0 |
| SBIN | +0.8 | +0.0 | +0.9 | -0.1 | -0.0 |
| ADANIENT | +0.7 | +0.0 | +0.7 | +0.0 | -0.0 |
| PAYTM | +0.7 | +0.0 | +0.9 | -0.1 | -0.0 |
| ADANIENSOL | +0.7 | +0.0 | +0.7 | +0.1 | -0.1 |
| ICICIAMC | +0.7 | +0.0 | +0.9 | -0.1 | -0.1 |
| PFC | +0.7 | +0.0 | +0.7 | +0.1 | -0.0 |

## Most negatively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| MANKIND | -0.4 | -0.4 | +0.1 | -0.0 | -0.0 |
| TMPV | -0.3 | +0.0 | -0.3 | -0.1 | +0.0 |
| JSWSTEEL | -0.3 | +0.0 | -0.1 | -0.1 | -0.0 |
| ONGC | -0.2 | +0.0 | -0.1 | -0.1 | +0.0 |
| OIL | -0.2 | +0.0 | -0.1 | -0.1 | +0.0 |
| SAIL | -0.2 | +0.0 | -0.0 | -0.1 | -0.0 |
| PREMIERENE | -0.2 | +0.0 | +0.0 | -0.2 | -0.0 |
| NMDC | -0.2 | +0.0 | -0.1 | -0.1 | +0.0 |
| COCHINSHIP | -0.1 | +0.0 | -0.0 | -0.1 | -0.0 |
| DRREDDY | -0.1 | +0.0 | -0.1 | -0.1 | +0.0 |
| LTM | -0.1 | -0.2 | +0.1 | -0.1 | -0.0 |
| SRF | -0.1 | +0.0 | -0.1 | -0.0 | +0.0 |
| VOLTAS | -0.1 | +0.0 | -0.2 | +0.1 | -0.0 |
| PIIND | -0.1 | +0.0 | -0.1 | -0.0 | +0.0 |
| COALINDIA | -0.1 | +0.0 | -0.1 | -0.0 | -0.0 |

Share of absolute impact by order: 1: 6%, 2: 76%, 3: 13%, 4: 5%

## Sources
- 2026-10-28 Fed holds rates steady despite concerns over inflation - CNBC https://news.google.com/rss/search?q=Fed%20holds%20rates%20steady%20despite%20concerns%20over%20inflation%20-%20CNBC&hl=en-IN&gl=IN&ceid=IN:en
- 2026-10-28 FOMC calendar https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm
- 2026-10-02 Traders now see little chance of a Fed rate hike in October after weak jobs report - CNBC https://news.google.com/rss/search?q=Traders%20now%20see%20little%20chance%20of%20a%20Fed%20rate%20hike%20in%20October%20after%20weak%20jobs%20report%20-%20CNBC&hl=en-IN&gl=IN&ceid=IN:en