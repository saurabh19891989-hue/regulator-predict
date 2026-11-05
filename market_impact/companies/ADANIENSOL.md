# ADANIENSOL — Adani Energy Solutions Ltd. (as of 2026-11-05)

*Scenario/exposure analysis only. All effects are relative to the Nifty 200 and are not validated forecasts. Facts are sourced in `ADANIENSOL.json` (company Q2 FY27 press release and call transcript of 22-23 Oct 2026, screener.in, Google-News headline searches); items marked "model knowledge" are from training memory.*

## Business
AESL is India's largest private transmission company (29,802 ckm, 1.43 lakh MVA across 16 states; 92% EBITDA margin in the segment) and has diversified into four other engines. Mumbai distribution (AEML, plus MPSEZ Utility in Mundra) is a regulated-asset-base business (RAB Rs 10,456 cr, +11% YoY) that generates the largest share of revenue but a modest share of profit. Smart metering (14.8 mn installed, 24.6 mn under implementation, Rs 29,519 cr revenue potential) is an annuity-like build-own-operate model. The newest and fastest-growing unit is the Energy Solutions platform: it buys renewable/thermal supply and sells round-the-clock and C&I power (12.2 bn units in Q2; operating EBITDA Rs 803 cr, about 26% of the quarter). Q2 FY27 total income was Rs 10,239 cr (+51%), EBITDA Rs 3,548 cr (+67%), PAT Rs 1,364 cr (+145%). Promoters hold 73.4%; FIIs have fallen from 17.6% to 9.6% in 18 months while DIIs rose to 13.6%.

## What moves the stock (ranked by modelled sensitivity x current shock)
1. **Rates and credit spreads (G-sec, repo, spreads).** A P/E-48 compounder with Rs 52k cr of borrowings. RBI hiked the repo by 25bp to 5.50% on 7 Oct 2026 and said cuts are off the table, and US 10y is 4.89% (+9% since June). The model puts -2.0% on +25bp G-sec yield (discount rate), -1.2% for repo (funding) and -2.2% for +50bp in credit spreads. Management says most debt is fixed or hedged, so the P&L effect is small; the valuation effect dominates.
2. **Policy support for grid build-out (P_RENEWABLE_SUPPORT +4, T_GRID_ELECTRIFICATION +5).** The Rs 1.86 lakh cr PM-DHARA green-energy-corridor scheme (approved 30 Sep 2026) and the Rs 1.4 lakh cr near-term tender pipeline determine order-book growth. The stock rose 5.5% on 1 Oct.
3. **Execution of transmission commissioning.** The company-specific driver: H1 commissioning was negligible because of right-of-way problems in Gujarat (Halvad, Khavda), yet management has not cut the ~Rs 15,000 cr FY27 capitalisation guide. This appears in `company_events` rather than as a driver edge.
4. **Group and governance overhang.** The US criminal case against Gautam Adani was dismissed on 10 Aug 2026; `company_links` carries a 0.35 group-contagion edge from Adani Enterprises.
5. **Energy Solutions margins (F_POWER_DEMAND_IN, F_POWER_PRICE_IN).** Mixed sign: rising demand lifts volumes; rising spot prices help legacy merchant volume but hurt while new RTC contracts are priced fixed.
6. **Flows and risk appetite (F_FPI_FLOWS +2.8).** High-beta stock with a thin foreign holder base.

## Worked transmission examples
- **Middle East escalation -> Brent/LNG up (1st) -> Indian inflation expectations up and RBI "calibrated tightening" (2nd) -> G-sec 10y and corporate spreads widen (3rd) -> discount rate on long-duration annuity compounders rises and refinancing of the Rs 87,000 cr construction programme gets pricier (4th) -> AESL de-rates even though its tariffs are fixed.** Offsetting channel: the same conflict strengthens the energy-security case for domestic grid capex.
- **Weak monsoon (-13% in Q2) -> record peak demand of 270 GW and power-demand growth of 11% (1st) -> spot power prices and coal-stock stress (2nd) -> states and discoms sign more RTC/firm supply, which AESL's Energy Solutions platform supplies (MSEDCL 2,500 MW, 25 years) (3rd) -> higher Energy Solutions EBITDA but also timing-mismatch margin risk when spot is above the contracted price (4th).**
- **PM-DHARA approved -> more ISTS corridors tendered (1st) -> AESL's bid-win pipeline grows (2nd) -> order book rises above Rs 87,000 cr and requires more capital (3rd) -> equity raise or promoter infusion (e.g. the Rs 3,500 cr QIP) dilutes per-share value but improves the growth runway (4th).**
- **Steel/aluminium inflation -> tower and conductor cost up on fixed TBCB tariffs (1st) -> project IRR on new awards falls (2nd) -> bidding becomes more conservative and AESL loses share to Power Grid (3rd).** Note that the pack's empirical steel beta is positive; the model rejects it as a market co-movement.

## Current situation
Q2 FY27 headline growth is strong but core transmission EBITDA grew only 15% YoY (Rs 1,394 cr) and distribution is growing 3% in revenue. Management reiterated transmission capex of about Rs 14,000 cr (Rs 8-9k cr in H2) and said three projects (WRSR, Khavda Ph-4 and Halvad) should commission this fiscal year. Smart-meter installation was only 1.3 mn in Q2 against a 10 mn full-year goal. The stock was down 6% after the call and is 19% below its 52-week high.

## Upcoming events
IntelliSmart acquisition closing (CCI approved 31 Oct; closing expected within about a month), Halvad ROW resolution and line commissioning, Q3 FY27 results (late Jan 2027, estimated), new TBCB awards, and a tail risk of renewed US legal action (probability low). Probabilities and impact ranges are in `company_events`.

## Bull and bear
**Bull:** commissioning catches up in H2 (EBITDA conversion of Rs 87k cr pipeline), Energy Solutions continues to scale, rating upgrades follow dismissal of the US case, PM-DHARA lifts the tender pipeline. **Bear:** ROW delays slip into FY28, spreads widen as the RBI tightens, Energy Solutions margins compress, smart-meter volume disappoints, and the stock's 48x P/E leaves little room for error.
