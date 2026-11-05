# Budget FY2027-28: LTCG/STT relief on listed equities (rate cut, exemption, or FPI-specific relief) (`EV_BUDGET_FY28_LTCG_RELIEF`)
*india_macro · status scheduled · date 2027-02-01 · P(3m) 0.35 · P(12m) 0.35 · confidence medium*

FM Sitharaman (2-3 Nov): 'we will consider the call for review of LTCG tax' and sought views on LTCG/STT (27 Oct) amid record FPI exodus; FICCI (4 Nov) asks for LTCG exemption/TDS relief; SBI Research proposes zero LTCG (cost Rs 50,000 cr in FY28). Fiscal slack is thin (H1 deficit 42%), so relief is likelier to be partial/targeted. P(any LTCG or STT reduction announced) 0.35; P(full FPI exemption) ~0.08. Current LTCG on listed equity 12.5% (model knowledge, from Budget 2024).

## Entry shocks (conditional on the event)
- `P_CAPITAL_GAINS_TAX` Capital-gains / securities tax burden: -0.5 SSU (range -1.2…-0.1) SSU +1=higher; negative = relief
- `F_FPI_FLOWS` Foreign portfolio flows into Indian equities: 0.5 SSU (range 0.1…1.2) flows respond with lag
- `F_EQUITY_ACTIVITY_IN` Indian equity market volumes & retail activity: 0.2 SSU (range 0.0…0.5) traded value

## Causal chains (agent)
- order 2: EV_BUDGET_FY28_LTCG_RELIEF → P_CAPITAL_GAINS_TAX → F_FPI_FLOWS — Lower post-tax return hurdle re-attracts foreign equity capital
- order 3: EV_BUDGET_FY28_LTCG_RELIEF → P_CAPITAL_GAINS_TAX → F_FPI_FLOWS → F_USDINR — Inflows support rupee
- order 4: EV_BUDGET_FY28_LTCG_RELIEF → P_CAPITAL_GAINS_TAX → F_FPI_FLOWS → F_USDINR → F_CPI_IN — Stronger rupee trims imported inflation
- order 3: EV_BUDGET_FY28_LTCG_RELIEF → P_CAPITAL_GAINS_TAX → F_EQUITY_ACTIVITY_IN → BSE — Higher turnover lifts exchange/broker/depository earnings

## Most positively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| MOTILALOFS | +6.8 | +6.7 | +0.2 | +0.0 | +0.0 |
| BSE | +6.4 | +6.3 | +0.1 | +0.0 | +0.0 |
| GROWW | +5.6 | +5.5 | +0.0 | -0.0 | +0.0 |
| ICICIAMC | +5.5 | +5.3 | +0.2 | -0.0 | +0.0 |
| 360ONE | +4.9 | +4.8 | +0.1 | +0.0 | +0.0 |
| HDFCAMC | +2.6 | +2.4 | +0.2 | +0.0 | +0.0 |
| PAYTM | +2.5 | +2.5 | +0.0 | -0.0 | +0.0 |
| PRESTIGE | +2.3 | +2.1 | +0.1 | +0.1 | +0.1 |
| GODREJPROP | +2.2 | +2.1 | +0.0 | +0.1 | +0.0 |
| LODHA | +2.2 | +2.1 | +0.0 | +0.1 | +0.0 |
| SBIN | +2.1 | +2.0 | +0.1 | +0.0 | +0.0 |
| INDUSINDBK | +2.0 | +2.0 | +0.0 | -0.0 | +0.0 |
| FEDERALBNK | +2.0 | +2.0 | -0.0 | -0.0 | +0.0 |
| JIOFIN | +2.0 | +1.6 | +0.3 | +0.0 | +0.1 |
| POLICYBZR | +2.0 | +2.0 | -0.0 | -0.0 | +0.0 |

## Most negatively affected (impact if the event happens, % equity value)
| company | total | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|
| JSWSTEEL | -0.4 | +0.0 | -0.2 | -0.2 | +0.0 |
| SAIL | -0.4 | +0.0 | -0.1 | -0.3 | +0.0 |
| JINDALSTEL | -0.3 | +0.0 | -0.0 | -0.3 | +0.0 |
| TATASTEEL | -0.3 | +0.0 | -0.1 | -0.2 | +0.0 |
| NATIONALUM | -0.3 | +0.0 | -0.3 | +0.0 | +0.0 |
| OIL | -0.3 | +0.0 | -0.3 | +0.0 | +0.0 |
| ONGC | -0.3 | +0.0 | -0.3 | +0.0 | +0.0 |
| VAML | -0.2 | +0.0 | -0.2 | +0.0 | +0.0 |
| NMDC | -0.2 | +0.0 | -0.2 | -0.0 | +0.0 |
| PIIND | -0.2 | +0.0 | -0.2 | +0.0 | +0.0 |
| HINDZINC | -0.2 | +0.0 | -0.2 | -0.0 | +0.0 |
| TMPV | -0.2 | +0.0 | -0.2 | +0.0 | +0.0 |
| HINDALCO | -0.2 | +0.0 | -0.2 | -0.0 | +0.0 |
| SRF | -0.1 | +0.0 | -0.2 | +0.0 | +0.0 |
| SUNPHARMA | -0.1 | +0.0 | -0.1 | +0.0 | +0.0 |

Share of absolute impact by order: 1: 86%, 2: 9%, 3: 2%, 4: 3%

## Sources
- 2026-11-03 We will consider the call for review of LTCG tax - Economic Times https://news.google.com/rss/search?q=Sitharaman+LTCG+tax+review+FPI+exodus+when:120d&hl=en-IN&gl=IN&ceid=IN:en
- 2026-10-27 Govt seeks investor and expert views on LTCG and STT - Economic Times https://news.google.com/rss/search?q=Govt+seeks+views+on+LTCG+and+STT+FPI+exodus+when:120d&hl=en-IN&gl=IN&ceid=IN:en
- 2026-11-04 FICCI makes recommendations to FM ahead of Budget 2027-28 - ET https://news.google.com/rss/search?q=FICCI+recommendations+Budget+2027-28+LTCG+exemption+TDS+relief+when:120d&hl=en-IN&gl=IN&ceid=IN:en