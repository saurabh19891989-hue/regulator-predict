# Union Budget FY28 (1 Feb 2027) raises agri/rural spending and fertiliser subsidy; PM-Kisan/rural jobs top-up (`EV_BUDGET27_AGRI_RURAL`)
*agri_rural · status scheduled · date 2027-02-01 · P(3m) 0.0 · P(12m) 0.7 · confidence low*

Budget on 1 Feb 2027 (date: model knowledge of convention; not verified). Pressures: fertiliser subsidy ~Rs 3 lakh crore in FY27, drought relief, VB-G RAM G funding after person-days fell (50%/61% in Jul-Aug), food subsidy (grain glut swelling bill per FE), rabi MSP payout Rs 90,962 crore. Fiscal consolidation and a Rs 1.86 lakh crore PM-DHARA scheme compete for space. Probability that the Budget raises combined agri + rural development + fertiliser allocation by more than 8% y/y: 70%; remaining 30%: flat/consolidation (model judgement, low confidence).

## Entry shocks (conditional on the event)
- `F_RURAL_DEMAND` Rural consumption growth: 0.3 SSU (range 0.0…0.6) Conditional: transfers/jobs top-up.
- `P_FERT_SUBSIDY` Fertiliser subsidy generosity: 0.5 SSU (range 0.2…1.0) Higher FY28 fertiliser allocation.
- `F_GSEC_10Y_IN` India 10-year G-sec yield: 0.2 SSU (range 0.0…0.5) Fiscal slippage risk (SSU +25 bp).

## Causal chains (agent)
- order 2: EV_BUDGET27_AGRI_RURAL → F_RURAL_DEMAND → F_AUTO_DEMAND_IN — Rural transfers support 2W/tractor FY28.
- order 3: EV_BUDGET27_AGRI_RURAL → F_RURAL_DEMAND → F_GDP_IN — Consumption support.
- order 4: EV_BUDGET27_AGRI_RURAL → F_GSEC_10Y_IN → F_CREDIT_SPREADS_IN — Fiscal slippage widens spreads.

## Most positively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| INDUSINDBK | +2.1 | -0.3 | +1.8 | +0.8 | -0.2 |
| IDFCFIRSTB | +1.7 | -0.3 | +1.6 | +0.6 | -0.2 |
| M&MFIN | +1.4 | +1.2 | +0.2 | +0.1 | -0.1 |
| TMCV | +1.3 | +0.0 | +1.5 | -0.1 | -0.0 |
| KOTAKBANK | +1.2 | -0.1 | +1.0 | +0.4 | -0.1 |
| MEESHO | +1.1 | +1.2 | +0.0 | -0.1 | -0.0 |
| FEDERALBNK | +1.0 | -0.4 | +0.5 | +1.0 | -0.1 |
| BANKINDIA | +1.0 | -0.6 | +1.1 | +0.6 | -0.1 |
| MAHABANK | +1.0 | -0.3 | +0.9 | +0.5 | -0.1 |
| VMM | +0.9 | +0.9 | +0.0 | +0.0 | +0.0 |
| LICHSGFIN | +0.9 | -0.3 | +0.3 | +1.0 | -0.1 |
| INDIANB | +0.9 | -0.4 | +1.0 | +0.3 | -0.1 |
| UNIONBANK | +0.9 | -0.3 | +0.9 | +0.4 | -0.1 |
| YESBANK | +0.9 | -0.6 | +1.3 | +0.4 | -0.2 |
| SHRIRAMFIN | +0.9 | -0.3 | +1.1 | +0.2 | -0.1 |

## Most negatively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| JSWENERGY | -0.8 | -0.5 | -0.1 | -0.2 | -0.0 |
| ADANIGREEN | -0.7 | -0.7 | -0.1 | +0.1 | -0.0 |
| POWERGRID | -0.6 | -0.6 | +0.0 | +0.0 | +0.0 |
| PRESTIGE | -0.5 | -0.2 | -0.1 | -0.1 | -0.1 |
| JIOFIN | -0.5 | -0.6 | -0.0 | +0.1 | -0.0 |
| PFC | -0.5 | -0.5 | +0.1 | -0.0 | -0.1 |
| GROWW | -0.5 | -0.5 | +0.0 | -0.0 | +0.0 |
| PERSISTENT | -0.5 | -0.3 | +0.0 | -0.1 | -0.0 |
| ADANIENT | -0.5 | -0.5 | -0.0 | +0.0 | +0.0 |
| TATAPOWER | -0.5 | -0.5 | -0.0 | +0.1 | -0.0 |
| BIOCON | -0.4 | -0.3 | +0.0 | -0.1 | -0.0 |
| OBEROIRLTY | -0.4 | -0.2 | -0.0 | -0.1 | -0.1 |
| NHPC | -0.4 | -0.4 | -0.0 | +0.0 | -0.0 |
| TECHM | -0.4 | -0.2 | +0.0 | -0.1 | -0.0 |
| JINDALSTEL | -0.4 | -0.3 | -0.0 | -0.0 | -0.0 |

Share of absolute impact by order: 1: 38%, 2: 36%, 3: 20%, 4: 7%

## Sources
- 2026-09-29 Agriculture target and fertiliser needs https://www.financialexpress.com/policy/economy-foodgrain-output-estimate-for-2026-27-reduced-marginally-4349877/
- 2026-08-10 VB-G RAM G decline https://indianexpress.com/article/india/vb-g-ram-g-rural-jobs-decline-minimum-wages-10825474/