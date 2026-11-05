# ADANIENT — Adani Enterprises Ltd.
*NIFTY_50 · Metals & Mining · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months -0.6%**, **12 months +0.8%** (rank 140 / 76 of 200 for 3m / 12m); beta 1.31
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +31.1%): 3 months 48%, 12 months 42%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 -1.7% … P90 +2.7%; plausible 12m relative-return range incl. stock-specific noise: -40.0% … +21.1%
- Decomposition (12m): 0.5 × forward event exposure +0.1% (3m -0.2%; half assumed priced) + 0.5 × company-specific catalysts +2.5%, centred on the universe
- Since 1 June 2026 (diagnostic, NOT in the headline): the graph's driver moves imply -1.8% (beta-adjusted) vs a realised market-adjusted move of -12.0% — gap +10.3 pp. Across the universe this gap does not predict anything we can verify (in-sample correlation of graph impact with realised moves was negative), so it is shown, not traded.

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Air/hotel/tourism demand (`F_TRAVEL_DEMAND`) | +10% | +3.00 | +3.00 | +0.00 | +0.00 | +0.00 | — |
| India 10-year G-sec yield (`F_GSEC_10Y_IN`) | +25 bp yield | -2.65 | -2.50 | -0.15 | +0.00 | +0.00 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -2.62 | -1.50 | -0.54 | -0.31 | -0.26 | — |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +2.24 | +2.00 | +0.19 | +0.02 | +0.04 | — |
| Urban discretionary consumption growth (`F_URBAN_DEMAND`) | +5 pp | +1.96 | +0.00 | +1.92 | +0.10 | -0.06 | — |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -1.95 | -1.00 | -0.35 | -0.25 | -0.35 | -1.1% |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -1.86 | +0.00 | -1.03 | -0.90 | +0.07 | — |
| Renewable / transmission policy support (`P_RENEWABLE_SUPPORT`) | +1 = stronger support | +1.57 | +1.50 | +0.00 | +0.07 | +0.00 | — |
| General-government fiscal slippage / extra borrowing vs budget (Centre + states) (`NEW_FISCAL_SLIPPAGE_IN`) | +0.5 pp of GDP deficit above budget (~Rs2 lakh cr) | -1.56 | +0.00 | -1.38 | -0.16 | -0.02 | — |
| Indian corporate credit spreads (`F_CREDIT_SPREADS_IN`) | +50 bp spreads | -1.52 | -1.50 | +0.00 | +0.00 | -0.02 | — |
| Indian data-centre build-out (`T_DATA_CENTRES_IN`) | +1 | +1.51 | +1.50 | +0.00 | +0.00 | +0.01 | — |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -1.36 | +0.00 | -0.87 | -0.45 | -0.05 | +3.5% |
| US 10-year Treasury yield (`F_US_10Y`) | +25 bp yield | -1.21 | +0.00 | -1.05 | -0.22 | +0.05 | +9.4% |
| GST rate cuts on consumer goods/services (`P_GST_CONSUMPTION`) | +1 = broad cut (~2-5 pp on affected items) | +1.21 | +0.00 | +0.36 | +0.57 | +0.29 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -4.9% | -4.9% | -4.4 | -0.4 | -0.0 | -0.1 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -4.0% | -4.0% | -4.0 | +0.0 | +0.0 | -0.0 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +5.7% | +2.8% | +5.0 | +0.5 | +0.1 | +0.1 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -2.2% | -2.2% | +0.0 | -1.2 | -1.0 | +0.1 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.55 | +3.7% | +2.0% | +2.3 | +0.8 | +0.3 | +0.2 |
| Iran war / Hormuz and Red Sea disruption lifts Brent to ~$95 (peak ~$110 on 16 Oct) (`EV_IRAN_WAR_HORMUZ_OIL`) | occurred | 1.00 | -1.8% | -1.8% | -1.5 | -0.2 | -0.1 | -0.1 |
| Cabinet approves Rs14,500 cr VGF for ~92 GWh grid-scale storage (4 Nov) (`EV_BESS_VGF_NOV26`) | occurred | 1.00 | +1.7% | +1.7% | +1.5 | +0.1 | +0.0 | +0.0 |
| US Treasury selloff: 10y above 5% (23 Sep), 30y highest since 2004 (`EV_UST_SELLOFF_SEP26`) | occurred | 1.00 | -1.6% | -1.6% | +0.0 | -1.6 | -0.1 | +0.1 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -1.5% | -1.5% | -1.4 | +0.0 | -0.0 | -0.1 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -1.5% | -1.5% | +0.0 | -1.3 | -0.2 | +0.0 |
| India Q1 FY27 GDP grows 7.8% (31 Aug 2026), beating ~7.3% consensus (`EV_GDP_Q1FY27_7_8`) | occurred | 1.00 | +1.5% | +1.5% | +1.2 | +0.5 | -0.1 | -0.1 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.25 | -5.8% | -1.4% | -3.1 | -1.4 | -0.9 | -0.4 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → ADANIENT | +5.00% | +2.50% |
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → ADANIENT | -2.00% | -1.00% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ C_MIDEAST_CONFLICT → ADANIENT | +1.50% | +0.83% |
| 1 | EV_CPI_BREACH_6PCT ⇒ F_GSEC_10Y_IN → ADANIENT | -1.25% | -0.75% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → ADANIENT | -3.00% | -0.54% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_US_EQUITIES → F_FPI_FLOWS → ADANIENT | -1.92% | -0.48% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_FPI_FLOWS → ADANIENT | -1.92% | -0.48% |
| 2 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → F_FPI_FLOWS → ADANIENT | -1.87% | -0.47% |
| 1 | EV_FERT_SUBSIDY_TOPUP_WINTER ⇒ F_GSEC_10Y_IN → ADANIENT | -0.50% | -0.45% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ C_MIDEAST_CONFLICT → ADANIENT | -1.80% | -0.45% |
| 1 | EV_BANKING_LIQUIDITY_DEFICIT_MAR27 ⇒ F_GSEC_10Y_IN → ADANIENT | -0.75% | -0.45% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_GSEC_10Y_IN → ADANIENT | -2.50% | -0.45% |
| 1 | EV_US_IRAN_CEASEFIRE_DEAL ⇒ F_BRENT → ADANIENT | +0.78% | +0.43% |
| 1 | EV_INDIA_ADD_DUTIES_NOTIFIED_H1_2027 ⇒ P_ANTI_DUMPING_IN → ADANIENT | +0.56% | +0.39% |
| 1 | EV_RBI_DEC26_HOLD ⇒ F_GSEC_10Y_IN → ADANIENT | +0.75% | +0.39% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | F_GSEC_10Y_IN → ADANIENT | +1.55 | director_override | -3.88% |
| 1 | F_FPI_FLOWS → ADANIENT | -1.60 | events | -3.20% |
| 1 | C_MIDEAST_CONFLICT → ADANIENT | +1.00 | events | -1.50% |
| 1 | P_RENEWABLE_SUPPORT → ADANIENT | +0.60 | director_override | +0.90% |
| 1 | F_CREDIT_SPREADS_IN → ADANIENT | +0.50 | events | -0.75% |
| 1 | F_COAL_INTL → ADANIENT | +0.70 | director_override | +0.70% |
| 1 | F_REPO_IN → ADANIENT | +1.00 | events | -0.40% |
| 2 | F_URBAN_DEMAND → F_TRAVEL_DEMAND → ADANIENT | +0.20 | events | +0.38% |
| 1 | F_USDINR → ADANIENT | -0.37 | observed | +0.37% |
| 1 | P_ANTI_DUMPING_IN → ADANIENT | +0.40 | events | +0.32% |
| 1 | F_COPPER → ADANIENT | -0.24 | observed | -0.28% |
| 1 | F_GOVT_CAPEX → ADANIENT | +0.20 | director_override | +0.24% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-12 | Group-level legal/regulatory headline risk (US probes reportedly settled; OFAC settlement Rs2,644 cr booked in Q1 FY27; other open matters not verified) | litigation | 0.15 | -8.0% | -1.20% |
| 2026-12 | Promoter-group inter-se share swaps / block deals (86 lakh shares for Rs2,498 cr on 25 Sep) and further promoter stake changes | corporate_action | 0.30 | -0.5% | -0.15% |
| 2027-01 | Q3 FY27 results (Q2 was 2026-10-28); airport peak-season traffic, Kutch copper ramp, interest and depreciation | results | 0.95 | +0.0% | +0.00% |
| 2027-03 | Kutch Copper phase-2 / data-centre capacity commissioning milestones | capex | 0.40 | +1.5% | +0.60% |
| 2027-06 | Possible Adani Airports IPO/listing preparation (model knowledge, not confirmed) | corporate_action | 0.15 | +4.0% | +0.60% |
| 2027-07 | Final tranche of Adani Airports US$1 bn primary raise (BlackRock, Temasek, Premji, Alpha Wave) | corporate_action | 0.80 | +1.2% | +1.00% |

## Analyst profile (agent research, sourced)
# ADANIENT — Adani Enterprises Ltd. — profile as of 2026-11-05

Scenario-implied exposure analysis, not a forecast; no expected-return number. The seed lists ADANIENT as Nifty 50 (the batch brief called it Next 50); it is profiled at Next-50 depth. Overall confidence is LOW: segment data came from press summaries that disagree in places, and net debt was not found.

## 1. Business
Adani group's incubator holding company. Segments: Integrated Resources Management (coal trading, Carmichael and Indonesian mining, mining services), airports via Adani Airport Holdings (Mumbai, Navi Mumbai, other airports), the Kutch Copper smelter, roads, water, data centres (AdaniConneX JV), solar and wind manufacturing, green hydrogen, defence and PVC. Q2 FY27: total income Rs38,023 cr (+74%), EBITDA Rs6,316 cr (+62%), H1 EBITDA Rs11,958 cr (+56%). Airports earned Rs1,641 cr EBITDA (+55%, ~26% of group EBITDA) on income of Rs3,786 cr. Copper sales rose to 80.6 kt from 11.8 kt a year earlier. Attributable profit fell 55% to Rs1,492 cr (screener NP Rs1,221 cr) because interest (Rs2,296 cr a quarter) and depreciation on newly commissioned assets jumped. Market cap Rs3.70 lakh cr, P/E 115, ROCE 5.8%, rating AA/Stable (CARE, 7 Oct).

## 2. What moves the stock, ranked
1. **Long-rate and discount-rate sensitivity (G-sec 10y -2.5 per +25 bp, credit spreads -1.5, repo -0.4).** P/E 115 means value sits in long-dated airport, data-centre, copper and green-hydrogen cash flows; this is the largest, most reliable channel.
2. **Airports / travel demand (+3.0 per +10% traffic).** The AAHL stake is worth ~46% of group mcap at the September US$18 bn pre-money valuation, so passenger traffic, ATF costs and aviation regulation matter most operationally.
3. **Group contagion (ADANIPORTS 0.5, ADANIGREEN 0.3, ADANIPOWER 0.3, ADANIENSOL 0.25).** The Adani stocks fall together on legal or credit headlines: up to 7% on 8 Oct.
4. **Capital flows (FPI +2.0), Middle East escalation (-1.5), gold (-2.0, statistical risk-on proxy, t=-3.6).**
5. **Commodity segments:** coal (+1.0), copper (+1.2), both modest because earnings are volume and processing margins rather than flat prices.
6. **Policy:** renewable/ALMM/BESS support (+1.5), government capex (+1.2), anti-dumping on solar/PVC (+0.8).

## 3. Transmission chains
**Rates chain (4th order).** Oil/food inflation -> CPI 5.54% and RBI hikes to 5.50% with liquidity drained -> 10y G-sec 7.4% -> higher discount rates on a P/E-115 stock, and higher refinancing cost for a group that must raise ~Rs50,000 cr a year -> credit spreads widen if the Fed keeps hiking (Dec 9 hike odds 0.58) -> pressure on Adani debt prices -> equity sells off, group stocks fall together -> AAHL monetisation window narrows (final tranche of the US$1 bn raise due by Jul 2027).

**Aviation chain.** Iran/Hormuz escalation -> Brent US$95-117 -> ATF cost up (govt windfall levy on ATF re-set 31 Oct) -> airlines trim capacity, Gulf airspace closures cut international traffic -> airport income per passenger and traffic growth fall -> AAHL EBITDA down; at the same time the airports' higher depreciation (Navi Mumbai) caps profit. Reverse: a US-Iran deal (odds 0.62 by 15 Dec) lowers oil and lifts traffic, aviation and the stock.

**Copper/China chain.** China stimulus (Dec CEWC odds 0.45) -> China GDP -> copper price and TC/RC recovery -> Kutch Copper margin up and its by-products (gold, silver, acid) -> group EBITDA; conversely record-low TC/RCs are squeezing smelter margins even with copper at record highs.

**Energy/coal chain.** India's coal crunch (74 plants <=7 days stock; e-auction premia ~94%) -> more imported coal blending (mandate shelved 23 Oct, Sec 11 to 31 Dec) -> more coal trading volume and mining-service demand for IRM, positive; but seaborne coal is flat (US$96), limiting price upside. A coal-import blending mandate (odds 0.5) would help.

**Group-legal chain.** Any new enforcement news (US cases reportedly settled; an OFAC settlement of Rs2,644 cr was booked in Q1 FY27) -> group-wide selling (-7%) -> ADANIPORTS/GREEN/POWER fall -> ADANIENT falls with beta 0.3-0.5 per group stock and its bond spreads widen. Model weight is judgemental.

## 4. Current situation
Strong top-line growth, record H1 EBITDA, a US$1 bn equity raise at AAHL (Alpha Wave, Premji Invest, Temasek, BlackRock funds), a CARE upgrade and Jefferies' 28% upside call (22 Sep) contrast with net profit down 55%. Promoter holding fell 2.87 pp to 71.97% in the September quarter alongside a group share swap of 86 lakh shares for Rs2,498 cr (reason not verified). The stock is -4% in a month and -9.6% in three months, but +13% over 12 months and had been Nifty's 2026 winner at one point (Business Standard, 9 Sep).

## 5. Upcoming events
Q3 FY27 results (~late Jan/Feb 2027); AAHL tranches through Jul 2027; RBI MPC 4 Dec (hike odds 0.40); Fed 9 Dec; Union Budget 1 Feb; copper phase-2 and data-centre milestones; possible AAHL IPO preparation (model knowledge, 0.15); promoter-group share swaps; legal/regulatory headlines (0.15 in the quarter for a material one).

## 6. Bull and bear
**Bull:** airport traffic and Navi Mumbai ramp; AAHL valued at US$18 bn crystallises SOTP; copper smelter ramp; rating upgrades and FPI return; data-centre optionality.
**Bear:** higher-for-longer rates and wider spreads on a leveraged balance sheet; depreciation/interest drag keeps profits falling; commodity-margin squeeze; legal or group headline shocks; stretched valuation.

Weak spots: net debt, segment EBITDA splits (press totals conflict), hedge ratio, and open legal matters.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.