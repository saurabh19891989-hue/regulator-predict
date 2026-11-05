# IDEA — Vodafone Idea Ltd.
*NIFTY_NEXT_50 · Telecommunication · analysis date 2026-11-05 · model run from the Market Impact Graph*

## Scenario-implied verdict (beta-adjusted, relative to the Nifty 200 average; not a validated forecast)
- Expected relative return: **3 months +3.8%**, **12 months +8.1%** (rank 19 / 17 of 200 for 3m / 12m); beta 1.30
- Probability of beating the universe (incl. idiosyncratic noise, 12m vol +39.9%): 3 months 58%, 12 months 50%
- Model-uncertainty band for the 12m expectation (event occurrence × edge-weight draws): P10 +4.6% … P90 +20.3%; plausible 12m relative-return range incl. stock-specific noise: -48.0% … +26.9%
- Decomposition (12m): unpriced part of Jun–Nov 2026 driver moves +0.2 pp (model impact +0.4% beta-adjusted vs realised market-adjusted move -14.2%); forward event exposure +8.3% (3m -0.3%; half assumed priced); company-specific events +9.5%

## What moves this stock (company → drivers)
% change in equity value for a +1 standard shock of each driver, split by causal order.
| driver | standard shock | total | 1st | 2nd | 3rd | 4th | driver move since 1 Jun 2026 |
|---|---|---|---|---|---|---|---|
| Mobile tariff hikes (`P_TELECOM_TARIFFS`) | +10% ARPU via tariff hike | +21.89 | +22.00 | +0.00 | -0.07 | -0.04 | — |
| Government AGR/spectrum dues relief for stressed telcos (`NEW_AGR_SPECTRUM_RELIEF`) | +1 = further material relief worth ~Rs20,000 cr NPV | +12.00 | +12.00 | +0.00 | +0.00 | +0.00 | — |
| Jio/Airtel price and share competition vs Vi (`NEW_TELECOM_SHARE_COMPETITION`) | +1 = intensification costing the incumbent ~1pp revenue share / 3% ARPU | -8.00 | -8.00 | +0.00 | +0.00 | +0.00 | — |
| India CPI inflation (`F_CPI_IN`) | +1 pp | -4.81 | +0.00 | -2.51 | -1.88 | -0.42 | — |
| Indian corporate credit spreads (`F_CREDIT_SPREADS_IN`) | +50 bp spreads | -4.02 | -4.00 | +0.00 | -0.04 | +0.02 | — |
| Middle East conflict intensity (`C_MIDEAST_CONFLICT`) | +1 = escalation | -3.91 | +0.00 | -1.28 | -1.44 | -1.19 | — |
| Global risk aversion (VIX) (`F_RISK_SENTIMENT`) | +5 VIX points | -3.56 | -2.50 | -0.62 | -0.33 | -0.12 | +3.5% |
| USD/INR exchange rate (`F_USDINR`) | +3% USD/INR (rupee weaker) | -3.30 | -1.50 | -0.47 | -0.71 | -0.63 | -1.1% |
| Foreign portfolio flows into Indian equities (`F_FPI_FLOWS`) | +US$5 bn net inflow per quarter | +2.88 | +2.50 | +0.22 | +0.04 | +0.12 | — |
| US equity market (`F_US_EQUITIES`) | +5% S&P 500 | +2.84 | +0.00 | +2.00 | +0.71 | +0.13 | +1.2% |
| US average effective tariff rate (all partners) (`NEW_US_TARIFF_GLOBAL`) | +5 pp effective tariff rate | -2.57 | +0.00 | -1.00 | -1.04 | -0.53 | — |
| India food inflation (`F_FOOD_INFLATION_IN`) | +2 pp | -2.46 | +0.00 | +0.00 | -1.43 | -1.04 | — |
| India 10-year G-sec yield (`F_GSEC_10Y_IN`) | +25 bp yield | -2.41 | -2.00 | -0.40 | -0.02 | +0.00 | — |
| USD/JPY exchange rate (`NEW_USDJPY`) | +3% USD/JPY (yen weaker) | +2.24 | +0.00 | +1.60 | +0.43 | +0.21 | — |

## Events affecting this stock (event → company)
| event | status | P(12m) | impact if it happens | expected | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|---|---|
| Broad mobile tariff hike by Jio/Airtel (12-15%) (`EV_TELECOM_TARIFF_HIKE_2027`) | anticipated | 0.75 | +26.3% | +19.7% | +26.4 | +0.0 | -0.1 | -0.0 |
| Bharti Airtel raises postpaid plans by Rs 50 (3-11%) (`EV_AIRTEL_POSTPAID_HIKE`) | occurred | 1.00 | +6.6% | +6.6% | +6.6 | +0.0 | -0.0 | -0.0 |
| Record FPI equity outflow in CY2026 (~Rs 3 lakh crore, ~2x 2025) passes Rs 3 trillion in October (`EV_FPI_RECORD_OUTFLOW_26`) | occurred | 1.00 | -6.3% | -6.3% | -5.5 | -0.5 | -0.1 | -0.3 |
| CPI inflation re-accelerates to 5.54% (Sep), nine straight monthly rises, food 7.74% (`EV_CPI_REACCEL_SEP26`) | occurred | 1.00 | -5.6% | -5.6% | +0.0 | -2.9 | -2.2 | -0.5 |
| FPI equity inflows rebound (>= +US$5bn in a quarter) on lower crude, trade deal, tax relief (`EV_FPI_INFLOW_REBOUND`) | anticipated | 0.50 | +8.3% | +4.1% | +7.2 | +0.6 | +0.1 | +0.3 |
| RBI drains liquidity (CRR maintenance 99%, bond sales) as 10y G-sec hits multi-year high (`EV_RBI_LIQUIDITY_BOND_SELLOFF_OCT26`) | occurred | 1.00 | -4.0% | -4.0% | -4.0 | +0.0 | -0.0 | +0.0 |
| RBI MPC hikes repo 25 bp to 5.50%, stance to calibrated tightening (7 Oct 2026) (`EV_RBI_OCT26_HIKE25`) | occurred | 1.00 | -2.9% | -2.9% | -2.9 | +0.1 | -0.0 | -0.0 |
| US-Iran ceasefire/peace framework agreed and holding (`EV_US_IRAN_CEASEFIRE_DEAL`) | anticipated | 0.55 | +5.1% | +2.8% | +1.0 | +1.9 | +1.1 | +1.0 |
| AI capex reset / AI-credit event: hyperscalers cut 2027 capex guide or AI financing seizes (`EV_AI_CAPEX_RESET_RISK`) | risk_scenario | 0.25 | -10.7% | -2.7% | -6.2 | -3.9 | -0.6 | +0.1 |
| Fed delivers first hike in years (16 Sep 2026), new chair Warsh (`EV_FED_SEP26_HIKE`) | occurred | 1.00 | -2.4% | -2.4% | -0.6 | -0.8 | -0.7 | -0.3 |
| Indian spot power: IEX prices hit Rs20/unit ceiling (19 Sep), Q2 prices up ~46% y/y; El Nino lifts demand (`EV_POWER_SPOT_SPIKE`) | occurred | 1.00 | -2.4% | -2.4% | -2.4 | +0.0 | +0.0 | +0.0 |
| Iran talks collapse; renewed Gulf strikes, sustained Hormuz tanker attacks, Brent above $110 (`EV_IRAN_TALKS_FAIL_ESCALATE`) | risk_scenario | 0.25 | -9.4% | -2.3% | -2.5 | -3.3 | -1.9 | -1.8 |

## Strongest forward causal chains (upcoming/risk events, 1st–4th order)
Order = number of hops from the event's entry driver to the company. Expected = probability × impact (before the half-priced haircut).
| order | chain | impact if event | expected 12m |
|---|---|---|---|
| 1 | EV_TELECOM_TARIFF_HIKE_2027 ⇒ P_TELECOM_TARIFFS → IDEA | +26.40% | +19.80% |
| 1 | EV_FPI_INFLOW_REBOUND ⇒ F_FPI_FLOWS → IDEA | +6.25% | +3.12% |
| 1 | EV_AI_CAPEX_RESET_RISK ⇒ F_RISK_SENTIMENT → IDEA | -6.25% | -1.56% |
| 1 | EV_SATCOM_LAUNCH ⇒ P_TELECOM_TARIFFS → IDEA | -2.20% | -1.32% |
| 1 | EV_SUMMER27_POWER_SHORTFALL ⇒ F_POWER_PRICE_IN → IDEA | -2.40% | -0.96% |
| 1 | EV_YEN_CARRY_UNWIND_RISK ⇒ F_RISK_SENTIMENT → IDEA | -6.25% | -0.94% |
| 2 | EV_US_RECESSION_RISK_2027 ⇒ F_US_EQUITIES → F_RISK_SENTIMENT → IDEA | -3.60% | -0.90% |
| 1 | EV_PRECIOUS_METALS_FURTHER_SLIDE ⇒ F_GOLD → IDEA | +2.85% | +0.85% |
| 1 | EV_BUDGET_FY28_FISCAL_SLIPPAGE ⇒ F_GSEC_10Y_IN → IDEA | -1.60% | -0.80% |
| 1 | EV_BANKING_LIQUIDITY_DEFICIT_MAR27 ⇒ F_CREDIT_SPREADS_IN → IDEA | -1.20% | -0.72% |
| 1 | EV_PRECIOUS_METALS_REBOUND_H1_2027 ⇒ F_GOLD → IDEA | -1.50% | -0.68% |
| 1 | EV_RUPEE_BREAK_98_RESERVE_STRESS ⇒ F_FPI_FLOWS → IDEA | -3.75% | -0.67% |
| 1 | EV_RBI_DEC26_HIKE25 ⇒ F_REPO_IN → IDEA | -1.50% | -0.63% |
| 1 | EV_IRAN_TALKS_FAIL_ESCALATE ⇒ F_RISK_SENTIMENT → IDEA | -2.50% | -0.62% |
| 1 | EV_NVDA_NOV17_BEAT ⇒ F_RISK_SENTIMENT → IDEA | +1.00% | +0.62% |

## What has already moved since 1 June 2026 (driver change × path)
Driver state in standard shocks (observed market series, occurred events, or reviewed override). Raw model impact, before beta adjustment and before comparing with the realised share-price move.
| order | chain | driver change (SSU) | source | impact |
|---|---|---|---|---|
| 1 | P_TELECOM_TARIFFS → IDEA | +0.30 | events | +6.60% |
| 1 | F_FPI_FLOWS → IDEA | -1.60 | events | -4.00% |
| 1 | F_GSEC_10Y_IN → IDEA | +1.55 | director_override | -3.10% |
| 1 | F_CREDIT_SPREADS_IN → IDEA | +0.50 | events | -2.00% |
| 1 | F_GOLD → IDEA | -1.05 | observed | +1.57% |
| 1 | F_POWER_PRICE_IN → IDEA | +1.90 | director_override | -1.52% |
| 1 | F_REPO_IN → IDEA | +1.00 | events | -1.50% |
| 1 | F_US_10Y → IDEA | +1.68 | observed | -1.34% |
| 1 | F_USDINR → IDEA | -0.37 | observed | +0.55% |
| 1 | F_GDP_IN → IDEA | +0.50 | events | +0.50% |
| 1 | F_RISK_SENTIMENT → IDEA | +0.11 | observed | -0.28% |

## Company-specific catalysts (profile events after review; expected = probability × midpoint impact)
| date | event | type | P | impact if it happens (mid) | expected |
|---|---|---|---|---|---|
| 2026-11-14 | Q2 FY27 results (date not announced as of 2026-10-22; mid-Nov expected). Watch ARPU (>Rs200?), net adds, EBITDA, capex pace, debt-raise status | results | 0.95 | +0.0% | +0.00% |
| 2026-12 | Next industry-wide tariff hike (Nomura base case Dec quarter 2026 after Airtel postpaid hike and Jio IPO) | other | 0.40 | +11.5% | +4.60% |
| 2026-12 | Financial close / first drawdown of SBI-led Rs35,000 cr facility with lender conditions (promoter continuity, guarantees) | corporate_action | 0.60 | +7.5% | +4.50% |
| 2027-02 | Q3 FY27 results | results | 0.95 | +0.0% | +0.00% |
| 2027-03 | FY27 spectrum instalment (Rs7,000 cr scheduled FY27) paid on time without distress equity raise | regulatory | 0.80 | -1.0% | -0.80% |
| 2027-03 | Further govt relief / AGR reassessment outcome or spectrum deferral | regulatory | 0.20 | +16.5% | +3.30% |
| 2027-03 | Equity raise / follow-on (dilution) to fund capex or dues | corporate_action | 0.30 | -7.0% | -2.10% |

## Analyst profile (agent research, sourced)
# IDEA — Vodafone Idea Ltd. (Nifty Next 50) — profile as of 2026-11-05

## Business
Vodafone Idea (Vi) is India's third mobile operator: 193.1m subscribers at June 2026, ARPU Rs195 in Q1 FY27 (Rs177 a year earlier), revenue Rs45.5k cr TTM and an EBITDA margin of ~43%. It is a levered turnaround: interest (~Rs5.1k cr a quarter) is roughly equal to EBITDA (Rs5.0k cr), book value is negative (-Rs3.30/share), and the Mar-2026 quarter's Rs51,970 cr "profit" was a one-off tied to the AGR relief, not operations. The Government of India holds ~49% after converting dues to equity; the Birla/Vodafone promoter block is ~25.6%. Sources: screener.in pack (2026-11-05), Business Today (2026-08-10), TelecomTalk (Aug 2026).

## What moves the stock, ranked (model weights are % equity value per standard shock; see JSON for arithmetic)
1. **Government relief on AGR/spectrum dues (+12 per ~Rs20k cr NPV relief).** AGR dues are reportedly frozen at ~Rs87,695 cr with tiny capped annual payments, but spectrum instalments rise from Rs7k cr (FY27) to Rs15k cr (FY28) and Rs28k cr (FY29). HSBC (2026-09-08) is bearish exactly on this overhang. Any deferral/reassessment is the largest single value swing.
2. **Industry tariff hikes (+22 per +10% ARPU).** Operating leverage is extreme: a 10% ARPU rise adds ~Rs4k cr to a Rs19k cr EBITDA base. Airtel's Rs50 postpaid hike (2026-10-07) and Jio's IPO (Rs30,213 cr, ~90% to debt cut) are read as setting up a broader hike; Nomura's base case is the December quarter.
3. **Competitive intensity (-8 per 1pp share loss / 3% ARPU).** A better-funded Jio/Airtel can use 5G and bundles to stall Vi's recovery.
4. **Funding access and spreads (-4 per +50bp spreads, -1.5 per +25bp repo, -2.0 per +25bp 10y G-sec).** The reported SBI-led ~$3.5bn (Rs35k cr, Rs25k cr funded) package finances the Rs45k cr capex plan; lender conditions (promoter continuity) matter.
5. **Risk sentiment, FPI flows, rupee (small, high-beta).** Beta 1.5, 43% vol. The empirical negatives on gold/silver and positive iron-ore are risk/high-beta artefacts, not business links.

## Transmission examples
- **Tariffs, 1st-4th order:** Airtel/Jio hike prepaid tariffs (policy/industry) -> Vi ARPU rises (1st: +22 per 10% ARPU) -> EBITDA covers interest and the SBI debt becomes serviceable (2nd) -> bank lenders release tranches, capex orders of Rs9,000 cr proceed (3rd) -> 4G/5G coverage improves, churn slows and net adds persist, enabling the next hike (4th). Indus Towers (INDUSTOWER) sees lower tenant-default risk and more loadings.
- **Oil/rupee channel:** Middle East escalation -> Brent up -> INR weaker (USD/INR) -> imported network equipment and vendor payables cost more (Vi capex ~3% higher in rupee terms) -> funding gap widens versus the Rs45k cr plan -> more reliance on equity or government support -> dilution risk. Also Brent up -> CPI up -> RBI holds repo -> floating-rate bank debt stays dear.
- **Rates/liquidity:** US yields up -> FPI outflows -> high-beta, leveraged stocks fall more than market (beta 1.5) -> weaker equity currency for any follow-on raise -> funding plan relies on debt -> spreads matter again.
- **Policy:** TRAI/DoT orders on backhaul spectrum fees and roaming (headlines 2026-09-16, 2026-10-29) -> network cost or revenue changes for all three telcos, relatively larger for Vi.

## Current situation
Q1 FY27 (Aug 10): revenue +6% y/y, EBITDA +9%, loss narrowed 43% to Rs3,754 cr, first net subscriber add since the merger; capex orders of Rs9,000 cr placed. The stock hit a 25-month high ~Rs15.8 in early September on Jefferies' Buy (Rs20 target) and the SBI headline, then fell ~20% by 2026-10-22 (Kotak Neo); at Rs12.8 it is +14% in 6m. Q2 results are expected mid-November (not confirmed as of 2026-10-22).

## Upcoming events
Q2 FY27 results (mid-Nov, prob 0.95); industry tariff hike (Dec quarter, prob ~0.4 by year-end); SBI facility financial close (prob 0.6 by Dec); FY27 spectrum instalment of Rs7k cr (by March); possible further relief (prob 0.2); equity raise (prob 0.3 by March).

## Bull case
Tariffs +10-15%, ARPU >Rs210 within a year, EBITDA ~Rs24-26k cr, funding closes, relief on spectrum timing: equity could re-rate towards the Rs17-20 broker targets (Citi Rs17, Jefferies Rs20).

## Bear case
Hike stalls, spectrum payments step up with only partial bank funding, follow-on equity at a discount, or a negative AGR reassessment: HSBC's ~46% downside scenario. Brokers are split (HSBC bearish vs Jefferies/Citi bullish), consistent with low confidence.

## Missing/uncertain
Net debt and the exact dues schedule were not obtained from primary filings (reported figures only); the content of the 2026-09-16 TRAI order and finality of the SBI deal are unverified; Q2 date unconfirmed.


## Caveats
Exposure-driven, scenario-implied estimate from an LLM-built causal graph grounded in fundamentals and price co-movement. It has not been validated out of sample; see `ledger/` for the prospective scoring record.