# Rural demand indicators mixed: tractor volumes dip in Oct, 2W festive sales firm, rural CPI above urban, rural jobs scheme person-days down (`EV_RURAL_DEMAND_SOFT26`)
*agri_rural · status occurred · date 2026-11-02 · P(3m) 1.0 · P(12m) 1.0 · confidence medium*

Tractors Oct 2026: M&M domestic 62,626 (-13% y/y; company attributes to Diwali shifting to 8 Nov from Oct last year), Apr-Oct domestic 325,498 (+2% y/y), exports +40% to 2,220; Escorts Kubota 16,412 (-10.9%). Sept tractor sales fell on weak monsoon (New Indian Express 1 Oct). Two-wheelers: Honda 2W Oct +11-13%; Navratri-period bike sales +5.8% while passenger vehicles -13.7% to -22% on GST-2.0 high base (Autopunditz/NIE); EV 2W Oct >223,000. FMCG: Oct value growth reported at 15% (India Business Trade); Q2 FY27 demand resilient but analysts flag H2 risk from weakest monsoon since 2015 and input inflation (BusinessLine 16 Oct); Patanjali Foods holding 15% FMCG growth guidance despite rural weakness. Rural CPI 6.08% (Sep) vs urban 4.88%. VB-G RAM G (replacement for MGNREGA): person-days fell about 50% in first month, -61% in July (BS/Indian Express, Aug), partly sowing pause. Smaller FMCG firms squeezed by costs and slowing rural demand (ET, 5 Nov). Rural wage data (Labour Bureau) not retrieved: data gap.

**Already moved:** Nifty FMCG hit 52-week low (Oct); Reuters 3 Nov: auto stocks rose on strong October sales.

## Entry shocks (conditional on the event)
- `F_RURAL_DEMAND` Rural consumption growth: -0.3 SSU (range -0.6…0.0) Qualitative estimate: slowing rural volume growth of about 1-3 pp relative to trend (SSU +5pp). Not directly measured; low confidence.
- `F_WAGES_IN` Indian wage / employee-cost inflation: 0.0 SSU (range -0.2…0.1) No clean rural wage series retrieved; treat as unchanged.

## Causal chains (agent)
- order 2: EV_RURAL_DEMAND_SOFT26 → F_RURAL_DEMAND → F_AUTO_DEMAND_IN — Tractors and entry 2W are the most rural-linked autos.
- order 3: EV_RURAL_DEMAND_SOFT26 → F_RURAL_DEMAND → F_UNSECURED_STRESS — Rural income squeeze raises microfinance/vehicle-loan delinquency risk with a lag.
- order 4: EV_RURAL_DEMAND_SOFT26 → F_RURAL_DEMAND → F_UNSECURED_STRESS → F_ASSET_QUALITY_IN — Higher credit costs at rural lenders in FY28 H1.

## Most positively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| PRESTIGE | +0.4 | +0.0 | +0.0 | +0.1 | +0.3 |
| JSWENERGY | +0.3 | +0.0 | +0.0 | +0.2 | +0.1 |
| RVNL | +0.3 | +0.0 | +0.0 | +0.3 | +0.0 |
| GODREJPROP | +0.3 | +0.0 | +0.0 | -0.0 | +0.3 |
| LODHA | +0.3 | +0.0 | +0.0 | -0.0 | +0.3 |
| OBEROIRLTY | +0.2 | +0.0 | +0.0 | +0.0 | +0.2 |
| GRASIM | +0.2 | +0.0 | +0.0 | +0.2 | +0.1 |
| LENSKART | +0.2 | +0.0 | +0.0 | +0.1 | +0.1 |
| SOLARINDS | +0.2 | +0.0 | +0.0 | +0.2 | +0.0 |
| BIOCON | +0.2 | +0.0 | +0.0 | +0.1 | +0.2 |
| SUZLON | +0.2 | +0.0 | +0.0 | +0.2 | +0.1 |
| PREMIERENE | +0.2 | +0.0 | +0.0 | +0.2 | +0.0 |
| ETERNAL | +0.2 | +0.0 | +0.0 | +0.1 | +0.1 |
| JUBLFOOD | +0.2 | +0.0 | +0.0 | +0.1 | +0.1 |
| PHOENIXLTD | +0.2 | +0.0 | -0.2 | +0.2 | +0.2 |

## Most negatively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| INDUSINDBK | -3.0 | +0.0 | -1.8 | -1.5 | +0.4 |
| IDFCFIRSTB | -2.4 | +0.0 | -1.6 | -1.2 | +0.4 |
| BANKINDIA | -2.1 | +0.0 | -1.1 | -1.2 | +0.3 |
| MAHABANK | -1.8 | +0.0 | -0.9 | -1.0 | +0.2 |
| KOTAKBANK | -1.7 | +0.0 | -1.0 | -0.9 | +0.2 |
| YESBANK | -1.6 | +0.0 | -1.3 | -0.8 | +0.5 |
| INDIANB | -1.6 | +0.0 | -1.0 | -0.8 | +0.2 |
| UNIONBANK | -1.5 | +0.0 | -0.9 | -0.8 | +0.2 |
| AXISBANK | -1.5 | +0.0 | -1.0 | -0.8 | +0.3 |
| M&MFIN | -1.5 | -1.2 | -0.4 | -0.1 | +0.1 |
| PNB | -1.5 | +0.0 | -0.9 | -0.8 | +0.2 |
| HDFCBANK | -1.4 | +0.0 | -0.8 | -0.8 | +0.2 |
| SBIN | -1.4 | +0.0 | -0.8 | -0.8 | +0.2 |
| FEDERALBNK | -1.4 | +0.0 | -0.5 | -1.1 | +0.3 |
| TMCV | -1.3 | +0.0 | -1.5 | +0.1 | +0.1 |

Share of absolute impact by order: 1: 15%, 2: 39%, 3: 29%, 4: 18%

## Sources
- 2026-11-02 Mahindra sells 64,846 tractors in Oct 2026 - Global Agriculture https://www.global-agriculture.com/mechanization-technology/mahindra-sells-64846-tractors-in-october-2026-domestic-sales-decline-13/
- 2026-10-16 Weak monsoon looms over FMCG margins - BusinessLine https://www.thehindubusinessline.com/companies/weak-monsoon-looms-over-fmcg-margins-despite-strong-q2-demand/article71552538.ece
- 2026-10-21 Festive 2026: two-wheelers outpace cars - Autopunditz https://www.autopunditz.com/post/festive-two-wheeler-vs-car-sales-2026-navratri
- 2026-11-02 FMCG growth 15% in October https://indiabusinesstrade.in/diwali-boosts-fmcg-sales-growth-jumps-to-15-in-october.htm
- 2026-08-10 VB-G RAM G person-days decline - Indian Express https://indianexpress.com/article/india/vb-g-ram-g-rural-jobs-decline-minimum-wages-10825474/