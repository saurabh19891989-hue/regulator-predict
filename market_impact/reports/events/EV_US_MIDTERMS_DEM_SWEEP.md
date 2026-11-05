# US midterms (3 Nov 2026): Democrats win House and Senate (`EV_US_MIDTERMS_DEM_SWEEP`)
*global_macro · status occurred · date 2026-11-03 · P(3m) 1 · P(12m) 1 · confidence medium*

Democrats won control of both chambers (News On AIR, NDTV, The Hindu, 4 Nov); Trump posted a 'veto' message. Implications: gridlock on tax/fiscal, oversight of tariffs and H-1B; but tariffs are mostly executive (Section 301/232 after the Supreme Court struck IEEPA tariffs, $81 bn refunds, Jul 2026), so little immediate relief (Business Journals 4 Nov). Lame-duck Trump may seek quick trade deals (TOI/GTRI 4 Nov); Fortune 3 Nov: tariffs, Iran action and shutdown risk after the vote. Treasury yields fell; Nifty rallied.

**Already moved:** Sensex +1,268 to +1,400 pts on 5 Nov, Nifty >24,300; 5-day winning streak; FPIs bought Rs 20,834 cr in four sessions (most since 2023); US 10y 4.89%.

## Entry shocks (conditional on the event)
- `P_US_TARIFF_INDIA` US tariffs on Indian goods: -0.1 SSU (range -0.4…0.2) deal urgency vs executive tariff powers; sign uncertain
- `F_FPI_FLOWS` Foreign portfolio flows into Indian equities: 0.5 SSU (range 0.2…1.0) flows turned positive in first week of Nov
- `F_US_10Y` US 10-year Treasury yield: -0.2 SSU (range -0.4…0.0) gridlock = less fiscal expansion

## Causal chains (agent)
- order 2: EV_US_MIDTERMS_DEM_SWEEP → F_FPI_FLOWS → F_USDINR — inflows support rupee
- order 3: EV_US_MIDTERMS_DEM_SWEEP → P_US_TARIFF_INDIA → F_GDP_IN → F_PRIVATE_CAPEX — possible trade deal / lower tariff uncertainty helps export sectors and capex
- order 4: EV_US_MIDTERMS_DEM_SWEEP → F_US_10Y → F_GSEC_10Y_IN → F_REPO_IN — lower US yields ease Indian yields, reopening RBI optionality

## Most positively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| MOTILALOFS | +3.6 | +3.0 | +0.7 | -0.1 | -0.0 |
| PAYTM | +2.5 | +2.5 | +0.0 | -0.0 | +0.0 |
| ICICIAMC | +2.5 | +2.2 | +0.4 | -0.2 | +0.0 |
| BSE | +2.3 | +1.5 | +1.0 | -0.2 | +0.0 |
| INDUSINDBK | +2.3 | +2.2 | +0.1 | -0.0 | -0.0 |
| SBIN | +2.2 | +2.0 | +0.2 | -0.0 | +0.0 |
| 360ONE | +2.0 | +1.8 | +0.4 | -0.1 | +0.0 |
| HDFCBANK | +1.9 | +1.8 | +0.1 | +0.0 | +0.0 |
| POLICYBZR | +1.9 | +2.0 | -0.0 | -0.1 | +0.0 |
| ADANIGREEN | +1.9 | +1.5 | +0.3 | +0.0 | +0.0 |
| YESBANK | +1.8 | +1.5 | +0.2 | +0.0 | +0.1 |
| MEESHO | +1.7 | +1.8 | +0.0 | -0.0 | +0.0 |
| MAXHEALTH | +1.7 | +1.8 | -0.0 | -0.0 | +0.0 |
| AUBANK | +1.7 | +1.5 | +0.1 | +0.0 | +0.1 |
| APOLLOHOSP | +1.7 | +1.5 | +0.2 | -0.0 | +0.0 |

## Most negatively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| JSWSTEEL | -0.4 | +0.0 | -0.3 | -0.1 | +0.0 |
| OIL | -0.3 | +0.0 | -0.3 | -0.0 | +0.0 |
| ONGC | -0.3 | +0.0 | -0.3 | -0.0 | +0.0 |
| NATIONALUM | -0.3 | +0.0 | -0.3 | +0.0 | +0.0 |
| SAIL | -0.3 | +0.0 | -0.1 | -0.2 | -0.0 |
| NMDC | -0.2 | +0.0 | -0.2 | -0.0 | -0.0 |
| TMPV | -0.2 | +0.0 | -0.2 | -0.0 | -0.0 |
| VAML | -0.2 | +0.0 | -0.3 | +0.0 | +0.0 |
| TATASTEEL | -0.2 | +0.0 | -0.2 | -0.1 | +0.0 |
| JINDALSTEL | -0.2 | +0.0 | +0.0 | -0.2 | +0.0 |
| SRF | -0.2 | +0.0 | -0.2 | -0.0 | +0.0 |
| COALINDIA | -0.1 | +0.0 | -0.1 | -0.0 | +0.0 |
| SUNPHARMA | -0.1 | +0.0 | -0.1 | -0.0 | -0.0 |
| HINDALCO | -0.1 | +0.0 | -0.2 | +0.0 | +0.0 |
| TECHM | -0.1 | +0.0 | -0.0 | -0.0 | +0.0 |

Share of absolute impact by order: 1: 79%, 2: 16%, 3: 4%, 4: 1%

## Sources
- 2026-11-04 Democrats Take Control Of US Congress. What It Means For India - NDTV https://news.google.com/rss/search?q=Democrats%20Take%20Control%20Of%20US%20Congress.%20What%20It%20Means%20For%20India%20-%20NDTV&hl=en-IN&gl=IN&ceid=IN:en
- 2026-11-04 US midterms: What Trump's defeat means for Europe and global markets - Euronews https://news.google.com/rss/search?q=US%20midterms%3A%20What%20Trump%27s%20defeat%20means%20for%20Europe%20and%20global%20markets%20-%20Euronews&hl=en-IN&gl=IN&ceid=IN:en
- 2026-11-05 Sensex Surges 1,268 Points; Nifty Tops 24,300 on Strong Global Cues - HDFC Sky https://news.google.com/rss/search?q=Sensex%20Surges%201%2C268%20Points%3B%20Nifty%20Tops%2024%2C300%20on%20Strong%20Global%20Cues%20-%20HDFC%20Sky&hl=en-IN&gl=IN&ceid=IN:en
- 2026-11-03 Wall Street is bracing for a fresh wave of tariffs, Iran action (and potentially a government shutdown) after the midterms - Fortune https://news.google.com/rss/search?q=Wall%20Street%20is%20bracing%20for%20a%20fresh%20wave%20of%20tariffs%2C%20Iran%20action%20%28and%20potentially%20a%20government%20shutdown%29%20after%20the%20midterms%20-%20Fortune&hl=en-IN&gl=IN&ceid=IN:en