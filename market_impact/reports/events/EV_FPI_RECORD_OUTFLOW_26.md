# Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`)
*india_macro · status occurred · date 2026-10-13 · P(3m) 1 · P(12m) 1 · confidence medium*

Net FPI equity selling reached about Rs 3.12 lakh crore by 18 Oct (Rs 2.95 lakh crore by 1 Nov after early-Nov buying); Rs 1 trillion+ in H1 FY27; ~Rs 48,056 cr sold in October to 25 Oct; September ~Rs 36,000 cr. Rupee-equivalent roughly US$32-35bn (assumption: average rate 90-95). August saw 23-month-high foreign buying (Reuters 1 Sep) before a reversal on oil >US$95, yields, rupee. Early-Nov: Reuters (4 Nov) reports longest Indian equity winning streak in ~5 months on inflow hopes; DIIs absorbed ~106% of FPI selling on 1 Oct. Finance Minister (2-3 Nov) says she will consider the call to review LTCG tax and the government sought views on LTCG/STT (27 Oct); SBI proposes zero LTCG for FPIs.

**Review override applied:** F_RISK_SENTIMENT (+0.4 = +2 VIX pts) is removed. VIX is +0.6 pt since 1 Jun (+3.5%) and India VIX is -7.4% since 1 Jun. The note used a 3-month India VIX change, and the AI-selloff and BoJ events already carry the VIX move. Occurred-event VIX shocks summed to +0.95 SSU against +0.11 realised.

**Already moved:** Nifty50 -4.4% over 12 months, +4.6% since 1 Jun (+7.4% in the last month) per factor_state.md; Nifty fell ~6% in Sept; India VIX 15.3. FPI share of Indian stocks still falling (Mint 3 Nov).

## Entry shocks (conditional on the event)
- `F_FPI_FLOWS` Foreign portfolio flows into Indian equities: -2.2 SSU (range -3.0…-1.5) avg ~-US$10-11bn/quarter; FII outflow ~US$32.7bn YTD (NiftyTrader 29 Oct)

## Causal chains (agent)
- order 2: EV_FPI_RECORD_OUTFLOW_26 → F_FPI_FLOWS → F_USDINR — Equity outflows add dollar demand -> rupee weakness
- order 3: EV_FPI_RECORD_OUTFLOW_26 → F_FPI_FLOWS → F_USDINR → F_CPI_IN — Weaker rupee raises imported inflation
- order 4: EV_FPI_RECORD_OUTFLOW_26 → F_FPI_FLOWS → F_USDINR → F_CPI_IN → F_REPO_IN — Higher inflation pushes RBI hikes
- order 3: EV_FPI_RECORD_OUTFLOW_26 → F_FPI_FLOWS → F_DOMESTIC_FLOWS → HDFCAMC — DII/SIP flows fill the gap, supporting AMC/broker earnings

## Most positively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| JSWSTEEL | +1.3 | +0.0 | +1.0 | +0.4 | -0.1 |
| NATIONALUM | +1.2 | +0.0 | +1.2 | -0.0 | +0.0 |
| OIL | +1.2 | +0.0 | +1.2 | -0.0 | +0.0 |
| ONGC | +1.2 | +0.0 | +1.2 | -0.0 | +0.0 |
| VAML | +1.1 | +0.0 | +1.1 | -0.0 | +0.0 |
| SAIL | +1.0 | +0.0 | +0.4 | +0.7 | -0.1 |
| TATASTEEL | +0.9 | +0.0 | +0.6 | +0.3 | -0.0 |
| NMDC | +0.9 | +0.0 | +0.8 | +0.1 | +0.0 |
| JINDALSTEL | +0.8 | +0.0 | +0.1 | +0.7 | -0.0 |
| PIIND | +0.8 | +0.0 | +0.8 | +0.0 | +0.0 |
| TMPV | +0.8 | +0.0 | +0.8 | -0.0 | +0.0 |
| HINDZINC | +0.8 | +0.0 | +0.7 | +0.0 | +0.0 |
| SRF | +0.7 | +0.0 | +0.8 | -0.0 | -0.0 |
| HINDALCO | +0.7 | +0.0 | +0.7 | +0.0 | +0.0 |
| PERSISTENT | +0.5 | +0.0 | +0.6 | +0.0 | -0.1 |

## Most negatively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| MOTILALOFS | -15.7 | -13.2 | -2.8 | +0.3 | -0.0 |
| PAYTM | -11.0 | -11.0 | +0.0 | +0.0 | +0.0 |
| ICICIAMC | -10.8 | -9.9 | -1.1 | +0.2 | -0.0 |
| 360ONE | -9.3 | -7.7 | -1.7 | +0.1 | -0.0 |
| SBIN | -9.2 | -8.8 | -0.3 | +0.0 | -0.1 |
| BSE | -9.2 | -6.6 | -3.4 | +0.9 | -0.1 |
| INDUSINDBK | -8.9 | -8.8 | -0.2 | +0.1 | +0.0 |
| POLICYBZR | -8.6 | -8.8 | +0.2 | +0.0 | +0.0 |
| ETERNAL | -8.0 | -7.7 | -0.1 | -0.1 | -0.1 |
| MEESHO | -7.9 | -7.7 | +0.0 | -0.1 | -0.1 |
| HDFCBANK | -7.8 | -7.7 | -0.2 | +0.0 | -0.0 |
| MAXHEALTH | -7.6 | -7.7 | +0.2 | -0.0 | -0.1 |
| YESBANK | -7.5 | -6.6 | -0.4 | -0.0 | -0.5 |
| ADANIGREEN | -7.3 | -6.6 | -0.5 | -0.1 | -0.1 |
| AUBANK | -7.1 | -6.6 | -0.1 | -0.1 | -0.3 |

Share of absolute impact by order: 1: 85%, 2: 11%, 3: 2%, 4: 2%

## Sources
- 2026-10-13 Record FPI outflows top Rs 3 trillion in CY26 - Business Standard https://news.google.com/rss/search?q=FPI+outflow+2026+record+India+equities+Rs+3+lakh+crore+when:120d&hl=en-IN&gl=IN&ceid=IN:en
- 2026-11-01 FPI outflows hit Rs 2.95 lakh crore in 2026 - Moneycontrol https://news.google.com/rss/search?q=FPI+outflows+2.95+lakh+crore+2026+November+when:120d&hl=en-IN&gl=IN&ceid=IN:en
- 2026-11-03 We will consider the call for review of LTCG tax: Finance minister - Economic Times https://news.google.com/rss/search?q=Sitharaman+LTCG+tax+review+foreign+investors+when:120d&hl=en-IN&gl=IN&ceid=IN:en