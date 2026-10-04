# BLIND POINT-IN-TIME FORECASTING TASK
You are a professional regulatory forecaster. This file contains 20 independent forecasting snapshots about
DIFFERENT regulatory matters. Treat each snapshot on its own; do not carry information between snapshots.

Rules:
1. For each snapshot, "today" is its CUTOFF DATE. Use only the evidence shown plus general knowledge of how the
   regulatory process usually behaves (base rates, typical durations). Do not use any world-state fact learned after
   the cutoff: later election results, leadership changes, court rulings, agency decisions, dates or outcomes are
   unknown, even if you remember them. A future event stated in cutoff-valid evidence may be considered only as an
   uncertain plan or possibility, never as a later-known result. Every factual driver in "notes" or "scenarios" must
   be supported by the shown evidence or be a general process base rate.
2. Do NOT use any specific memory of what happened to this particular matter after the cutoff. If you recognise the
   matter and believe you know its later outcome, set "recognised_outcome": true and forecast from cutoff-valid
   evidence only. Never state or hint at the remembered result.
3. The evidence shown may be only a subset of what was public; do not infer anything from the absence of a
   document type. Some snapshots show no documents at all — then forecast from title, regulator, process and date.
4. "Decisive action" is defined per snapshot. Probabilities in "p" are CUMULATIVE: probability the decisive action
   is published within 7/30/60/90/180 days AFTER the cutoff (non-decreasing; "180d" is the headline action
   probability). Delays, stalls, withdrawals and no-action outcomes are common in regulation: be calibrated, use
   the full 0–1 range when evidence warrants, and do not default to 0.5.
5. "next": the NEXT official step within 180 days (mutually exclusive, sums to 1): final_action,
   revised_or_further_consultation (revised draft, supplemental proposal, extended/reopened comment period,
   further consultation or hearing), formal_withdrawal, no_further_official_step.
6. "content": CONDITIONAL on the decisive action happening, its form relative to the most recent proposal visible
   (sums to 1): as_proposed (substantially as proposed), softened (narrower scope, lower stringency, higher
   thresholds, longer transition, carve-outs), tightened, mixed (some softened, some tightened),
   different_mechanism.
7. "scenarios": up to 3 concrete policy-content scenarios CONDITIONAL on action (probabilities sum ≤ 1), each with
   a short mechanism and, where the evidence has numbers (thresholds, rates, dates, amounts), predicted
   parameter ranges. Cite evidence labels (E1, E2 …) that support/contradict it.
8. If the evidence is too thin to forecast meaningfully, set "insufficient_evidence": true but still give your best
   base-rate probabilities.

OUTPUT: read the output file named in your instructions (it contains a placeholder) and replace its ENTIRE content
with ONE JSON object of exactly this shape (no comments, no trailing text):
{"forecasts": [
  {"id": "<snapshot id>",
   "p": {"7d": 0.00, "30d": 0.00, "60d": 0.00, "90d": 0.00, "180d": 0.00},
   "next": {"final_action": 0.00, "revised_or_further_consultation": 0.00, "formal_withdrawal": 0.00, "no_further_official_step": 0.00},
   "content": {"as_proposed": 0.00, "softened": 0.00, "tightened": 0.00, "mixed": 0.00, "different_mechanism": 0.00},
   "scenarios": [{"s": "short label", "p": 0.00, "mech": "mechanism, <=25 words", "params": {"parameter": "predicted range"}, "ev": ["E1"], "contra": []}],
   "notes": "<=40 words: main drivers of your forecast",
   "missing": ["<=3 items of missing information that would most change the forecast"],
   "recognised_outcome": false,
   "insufficient_evidence": false}
]}
One entry per snapshot, in any order, using the exact snapshot ids below.

---
## SNAPSHOT S52b8ab4973
CUTOFF DATE (today): 2020-12-01
Regulator: FDA (US)
Matter: FDA draft guidance: Development of Locally Applied Corticosteroid Products for the Short-Term Treatment of Symptoms Associated With Internal or External Hemorrhoids
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2019-12-06 | official-forward (B) | draft_guidance_availability_notice | "Development of Locally Applied Corticosteroid Products for the Short-Term Treatment of Symptoms Associated With Internal or External Hemorrhoids; Draft Guidance for Industry; Availability" | www.federalregister.gov
   Claims: The Food and Drug Administration (FDA or Agency) is announcing the availability of a draft guidance for industry entitled "Development of Locally Applied Corticosteroid Products for the Short- Term Treatment of Symptoms Associated with Internal or External Hemorrhoids." This draft guidance will serv
   Excerpt: The Food and Drug Administration (FDA or Agency) is announcing the availability of a draft guidance for industry entitled "Development of Locally Applied Corticosteroid Products for the Short- Term Treatment of Symptoms Associated with Internal or External Hemorrhoids." This draft guidance will serve as a focus for continued discussions among the Division of Gastroenterology and Inborn Error Products, pharmaceutical sponsors, the academic community, and the public.
---
## SNAPSHOT S98abc28b23
CUTOFF DATE (today): 2026-04-08
Regulator: SEBI (IN)
Matter: SEBI consultation: uniform time lag for sharing and usage of price data for educational purposes
Decisive action for this matter = the regulator's first official publication ADOPTING the proposal at least in substantial part (e.g., board decision press release, circular, or notified regulation).
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2026-01-06 | official-forward (B) | consultation_paper | "Consultation Paper on 'Norms for sharing and usage of price data for educational purposes'" | www.sebi.gov.in
   Claims: Seeks comments on bringing uniformity to the time lag applicable to sharing/usage of price data solely for education and investor-awareness purposes. / Notes a May 24, 2024 circular set a one-day lag for exchanges sharing live data for educational purposes. / Notes a January 29, 2025 circular separately tightened the rule to require a three-month lag for entities solely engaged in education, creating two different, simultaneously-operative time lags.
   Excerpt: SEBI vide circular dated May 24, 2024 (May 2024) restricted the sharing of live data by exchanges only for trading and its related activities, and prescribed a time lag of one day for educational and awareness activities so as to curb the misuse of live data. Further SEBI vide circular dated January 29, 2025 (Jan 2025) further tightened the framework by stipulating that entities solely engaged in education may use such data only with a three months lag... the objective of this consultation paper is to bring uniformity in time-lag for sharing and usage of price data solely for education and investor awareness purposes.
---
## SNAPSHOT Sdf5667647c
CUTOFF DATE (today): 2026-05-18
Regulator: SEBI (IN)
Matter: SEBI consultation: revising the method for calculating variable net worth of stock brokers
Decisive action for this matter = the regulator's first official publication ADOPTING the proposal at least in substantial part (e.g., board decision press release, circular, or notified regulation).
Evidence: none provided for this snapshot.
---
## SNAPSHOT Sb2a67bd3ed
CUTOFF DATE (today): 2026-08-19
Regulator: SEBI (IN)
Matter: SEBI consultation: phased introduction of physical settlement in select agricultural commodity derivatives contracts
Decisive action for this matter = the regulator's first official publication ADOPTING the proposal at least in substantial part (e.g., board decision press release, circular, or notified regulation).
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2026-05-12 | official-forward (B) | consultation_paper | "Consultation Paper on 'Phased Introduction of Physical Settlement in Select Agricultural Commodity Derivatives Contracts'" | www.sebi.gov.in
   Claims: Proposes to permit exchanges, on a pilot basis, to launch delivery-based agricultural commodity derivatives contracts that start as financially-settled and mandatorily convert to physical settlement upon crossing predefined objective thresholds. / States the proposal does not dilute the principle of physical settlement; contracts remain designed as delivery-based instruments from inception, with the financially-settled phase only a temporary transitional arrangement. / Frames the review against the backdrop that compulsory physical settlement from contract inception may inhibit early liquidity formation and participation. / Notes agricultural commodity derivatives in India have historically emphasized physical settlement to ensure futures-spot price convergence and discourage excessive speculation.
   Excerpt: This consultation paper seeks stakeholder views on a proposal to permit exchanges, on a pilot basis, to introduce delivery-based agricultural commodity derivatives contracts that commence trading as financially-settled contracts and mandatorily transition into physically settled contracts upon the occurrence of predefined objective thresholds. Commodity derivatives markets play a vital role in the efficient functioning of agricultural value chains by facilitating price discovery, risk management, and market transparency.
---
## SNAPSHOT Sc77ecfce38
CUTOFF DATE (today): 2026-05-20
Regulator: SEBI (IN)
Matter: SEBI consultation: amendments to the Issue and Listing of Securitised Debt Instruments and Security Receipts Regulations
Decisive action for this matter = the regulator's first official publication ADOPTING the proposal at least in substantial part (e.g., board decision press release, circular, or notified regulation).
Evidence: none provided for this snapshot.
---
## SNAPSHOT S9779bb595d
CUTOFF DATE (today): 2024-11-26
Regulator: FDA (US)
Matter: FDA draft guidance: Marketing Submission Recommendations for a Predetermined Change Control Plan for Artificial Intelligence/Machine Learning-Enabled Device Software Functions
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence: none provided for this snapshot.
---
## SNAPSHOT S00708317a3
CUTOFF DATE (today): 2024-08-21
Regulator: FDA (US)
Matter: FDA draft guidance: Voluntary Malfunction Summary Reporting Program for Manufacturers
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2022-12-09 | official-forward (B) | draft_guidance_availability_notice | "Voluntary Malfunction Summary Reporting Program for Manufacturers; Draft Guidance for Industry and Food and Drug Administration Staff; Availability" | www.federalregister.gov
   Claims: The Food and Drug Administration (FDA or Agency) is announcing the availability of the draft guidance entitled "Voluntary Malfunction Summary Reporting (VMSR) Program for Manufacturers." We are publishing this notice of availability for this draft guidance document to help manufacturers better under
   Excerpt: The Food and Drug Administration (FDA or Agency) is announcing the availability of the draft guidance entitled "Voluntary Malfunction Summary Reporting (VMSR) Program for Manufacturers." We are publishing this notice of availability for this draft guidance document to help manufacturers better understand and use the VMSR Program. It is intended to further explain, but not change, the conditions of the VMSR Program. This draft guidance is not final nor is it for implementation at this time.
---
## SNAPSHOT S6b47c3795d
CUTOFF DATE (today): 2021-12-26
Regulator: FDA (US)
Matter: FDA draft guidance: Patient Engagement in the Design and Conduct of Medical Device Clinical Investigations
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2019-09-23 | official-forward (B) | draft_guidance_availability_notice | "Patient Engagement in the Design and Conduct of Medical Device Clinical Investigations; Draft Guidance for Industry, Food and Drug Administration Staff, and Other Stakeholders; Availability" | www.federalregister.gov
   Claims: The Food and Drug Administration (FDA or Agency) is announcing the availability of the draft guidance entitled "Patient Engagement in the Design and Conduct of Medical Device Clinical Investigations." The Patient Engagement Advisory Committee (PEAC) recommended that FDA and industry develop some typ
   Excerpt: The Food and Drug Administration (FDA or Agency) is announcing the availability of the draft guidance entitled "Patient Engagement in the Design and Conduct of Medical Device Clinical Investigations." The Patient Engagement Advisory Committee (PEAC) recommended that FDA and industry develop some type of framework to clarify how patient advisors can engage in the clinical investigation process. This draft guidance focuses on the applications, perceived barriers, and common challenges of patient engagement in the design and conduct of medical device clinical investigations. This draft guidance is not final nor is it in effect at this time.
---
## SNAPSHOT Sa879141bca
CUTOFF DATE (today): 2022-09-11
Regulator: FDA (US)
Matter: FDA draft guidance: Evaluation of Gastric pH-Dependent Drug Interactions With Acid-Reducing Agents: Study Design, Data Analysis, and Clinical Implications
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2020-12-01 | official-forward (B) | draft_guidance_availability_notice | "Evaluation of Gastric pH-Dependent Drug Interactions With Acid-Reducing Agents: Study Design, Data Analysis, and Clinical Implications; Draft Guidance for Industry; Availability" | www.federalregister.gov
   Claims: The Food and Drug Administration (FDA or Agency) is announcing the availability of a draft guidance for industry entitled "Evaluation of Gastric pH-Dependent Drug Interactions With Acid-Reducing Agents: Study Design, Data Analysis, and Clinical Implications." This draft guidance focuses on specific 
   Excerpt: The Food and Drug Administration (FDA or Agency) is announcing the availability of a draft guidance for industry entitled "Evaluation of Gastric pH-Dependent Drug Interactions With Acid-Reducing Agents: Study Design, Data Analysis, and Clinical Implications." This draft guidance focuses on specific recommendations pertinent to gastric pH- dependent drug-drug interaction (DDI) assessment and describes the FDA's recommendations regarding when clinical DDI studies with acid- reducing agents (ARAs) are needed; design of the clinical studies; interpretation of study results; and communicating findings and options for managing pH-dependent DDIs in product labeling.
---
## SNAPSHOT S6126407193
CUTOFF DATE (today): 2026-06-29
Regulator: SEBI (IN)
Matter: SEBI consultation: draft circular on trading software/technology at stock exchanges and common IT provisions for market infrastructure institutions
Decisive action for this matter = the regulator's first official publication ADOPTING the proposal at least in substantial part (e.g., board decision press release, circular, or notified regulation).
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2026-06-22 | official-forward (B) | consultation_paper | "Consultation Paper on Draft Circular for Trading Software & Technology at Stock Exchanges and Draft Circular on Common IT related provisions for MIIs" | www.sebi.gov.in
   Claims: Proposes a draft circular modifying trading-software-and-technology provisions of the Master Circular for Stock Exchanges & Clearing Corporations and the Master Circular for Commodity Derivatives. / Proposes a separate draft consolidated circular on common IT-related provisions for market infrastructure institutions (MIIs), amending the Master Circular for Depositories. / Frames the exercise as implementing the FY2023-24 budget announcement to simplify and reduce compliance cost via public consultation before issuing circulars. / Identifies this as a further paper in the same series that already included CPs on Administration of Exchanges (Oct 8, 2025) and Trading at Exchanges (Jan 9, 2026).
   Excerpt: In order to align the process of review of Master Circulars with the budget announcement, SEBI, inter-alia, prior to issuing a circular under the Acts or regulations, generally, undertakes public consultation. Therefore, in compliance with the mandate and procedure envisaged in the aforesaid budget announcement, towards facilitating ease of doing business/compliance for stock exchanges, following Consultation Papers (CPs) have been issued: CP on Measures for ease of doing business on Administration of Exchanges... has been put up for public comments on October 08, 2025. CP on Measures for ease of doing business on Trading at Exchanges... has been put up for public comments on January 09, 2026.
---
## SNAPSHOT S34bec17252
CUTOFF DATE (today): 2026-08-25
Regulator: SEBI (IN)
Matter: SEBI consultation: proposed amendments to the certification regime for associated persons in the securities markets
Decisive action for this matter = the regulator's first official publication ADOPTING the proposal at least in substantial part (e.g., board decision press release, circular, or notified regulation).
Evidence: none provided for this snapshot.
---
## SNAPSHOT S5da039de8d
CUTOFF DATE (today): 2026-07-15
Regulator: SEBI (IN)
Matter: SEBI consultation: treatment of debt-funded major maintenance expenses in Net Distributable Cash Flow calculation for Infrastructure Investment Trusts
Decisive action for this matter = the regulator's first official publication ADOPTING the proposal at least in substantial part (e.g., board decision press release, circular, or notified regulation).
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2026-06-01 | official-forward (B) | draft_circular_for_comment | "Consultation Paper on Review of Framework for Calculation of Net Distributable Cash Flows for InvITs" | www.sebi.gov.in
   Claims: The extant Master Circular framework (Dec 6, 2023, consolidated July 11, 2025) expressly prohibits InvITs/SPVs from distributing cash flows obtained via external debt. / Bharat InvITs Association (BIA) requested that debt availed by InvITs/SPVs for major maintenance expenses of road projects be added back in computing Net Distributable Cash Flow (NDCF). / The paper seeks public comment on whether/how to modify the NDCF computation framework to accommodate debt-funded major-maintenance expenses for road projects.
   Excerpt: SEBI vide circular dated December 06, 2023 (consolidated as part of Chapter 3 of Master Circular for Infrastructure Investment Trusts dated July 11, 2025) prescribed a standardized framework for calculation of Net Distributable Cash Flow ('NDCF') for InvITs which inter-alia prohibited using borrowed money for distributions to unitholders. SEBI is in receipt of request from Bharat InvITs Association (BIA) regarding treatment of debt availed by InvITs for incurring major maintenance expenses of road projects while calculating the NDCF.
---
## SNAPSHOT S0221ade4d9
CUTOFF DATE (today): 2025-12-25
Regulator: FDA (US)
Matter: FDA draft guidance: International Cooperation on Harmonisation of Technical Requirements for Registration of Veterinary Medicinal Products; Effectiveness of Anthelmintics: Specific Recommendations ...
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2022-08-11 | official-forward (B) | draft_guidance_availability_notice | "International Cooperation on Harmonisation of Technical Requirements for Registration of Veterinary Medicinal Products; Effectiveness of Anthelmintics: Specific Recommendations for Caprines (Revision 1); Draft Guidance f" | www.federalregister.gov
   Claims: The Food and Drug Administration (FDA or Agency) is announcing the availability of a draft guidance for industry GFI #97 (VICH GL14(R1)) entitled "Effectiveness of Anthelmintics: Specific Recommendations for Caprines (Revision 1)." This draft guidance has been developed for veterinary use by the Int
   Excerpt: The Food and Drug Administration (FDA or Agency) is announcing the availability of a draft guidance for industry GFI #97 (VICH GL14(R1)) entitled "Effectiveness of Anthelmintics: Specific Recommendations for Caprines (Revision 1)." This draft guidance has been developed for veterinary use by the International Cooperation on Harmonisation of Technical Requirements for Registration of Veterinary Medicinal Products (VICH). This revision clarifies the definition of adequate infection in individual animals, updates considerations for field studies, and makes additional clarifying changes.
---
## SNAPSHOT S628910a02b
CUTOFF DATE (today): 2023-03-08
Regulator: FDA (US)
Matter: FDA draft guidance: The Use of Published Literature in Support of New Animal Drug Applications
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence: none provided for this snapshot.
---
## SNAPSHOT S0cff2a8cd3
CUTOFF DATE (today): 2026-05-14
Regulator: SEBI (IN)
Matter: SEBI consultation: reviewing use of historical price scenarios in stress testing for the Commodity Derivatives Segment
Decisive action for this matter = the regulator's first official publication ADOPTING the proposal at least in substantial part (e.g., board decision press release, circular, or notified regulation).
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2026-02-05 | official-forward (B) | draft_circular_for_comment | "Consultation Paper On Draft Circular on Review of Inclusion of Historical Scenarios in Stress Testing and Coverage of Settlement Guarantee Fund for Commodity Derivatives Segment" | www.sebi.gov.in
   Claims: Proposes to review the Z-score threshold (currently 10) used to cap extreme historical price movements in peak-historical-return stress-testing scenarios for the Commodity Derivatives Segment's Core Settlement Guarantee Fund. / Also proposes to review the coverage requirement of the Settlement Guarantee Fund for the Commodity Derivatives Segment. / Describes the existing framework's 15-year historical lookback period for computing maximum percentage rise/fall (Scenarios 1A/1B).
   Excerpt: SEBI Master Circular... for Commodity Derivatives Segment dated Aug 04, 2023, inter alia, prescribes norms related to Core Settlement Guarantee Fund (SGF). The extant provisions pertaining to applicable value of Z-Score (for the purpose of stress testing) and coverage of SGF, as provided in paragraph 22 of Annexure O of the said circular are as follows: ...Price movements corresponding to a Z-score of 10 will replace extreme price movements beyond that threshold in peak historical returns of all the commodities. SEBI has received representations to review the aforementioned extant provision related to Z-Score for Commodity Derivatives Market.
---
## SNAPSHOT S140e9e973e
CUTOFF DATE (today): 2025-07-31
Regulator: FDA (US)
Matter: FDA draft guidance: Benefit-Risk Considerations for Product Quality Assessments
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2022-05-09 | official-forward (B) | draft_guidance_availability_notice | "Benefit-Risk Considerations for Product Quality Assessments; Draft Guidance for Industry; Availability" | www.federalregister.gov
   Claims: The Food and Drug Administration (FDA or Agency) is announcing the availability of a draft guidance for industry entitled "Benefit- Risk Considerations for Product Quality Assessments." This guidance describes the benefit-risk principles applied by FDA when conducting product quality-related assessm
   Excerpt: The Food and Drug Administration (FDA or Agency) is announcing the availability of a draft guidance for industry entitled "Benefit- Risk Considerations for Product Quality Assessments." This guidance describes the benefit-risk principles applied by FDA when conducting product quality-related assessments of chemistry, manufacturing, and controls (CMC) information submitted for FDA assessment as part of original new drug applications (NDAs), original biologics license applications (BLAs), or supplements to such applications, in addition to other information (e.g., inspectional findings) available to FDA during its assessment. This guidance discusses how FDA assesses risks, sources of uncertainty, and possible mitigation strategies for a product quality-related issue and how those considerations inform FDA's understanding of the potential effect on a product. This guidance also discusses how unresolved product quality issues may be addressed in the context of regulatory decision making. The guidance notes that product quality assessments are also done for abbreviated new drug applications (ANDAs), and it discusses how, in certain rare circumstances, unresolved product quality issues m
---
## SNAPSHOT S846c01fe50
CUTOFF DATE (today): 2022-11-06
Regulator: FDA (US)
Matter: FDA draft guidance: Drug Products Labeled as Homeopathic
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence available as of the cutoff (2 item(s), chronological):
[E1] 2019-10-24 | official-forward (B) | draft_guidance_availability_notice | "Drug Products Labeled as Homeopathic; Draft Guidance for Food and Drug Administration Staff and Industry" | www.federalregister.gov
   Claims: The Food and Drug Administration (FDA or Agency) is announcing the availability of a revised draft guidance for FDA staff and industry entitled "Drug Products Labeled as Homeopathic." The revised draft guidance, like the original version, describes how FDA intends to prioritize enforcement and regul
   Excerpt: The Food and Drug Administration (FDA or Agency) is announcing the availability of a revised draft guidance for FDA staff and industry entitled "Drug Products Labeled as Homeopathic." The revised draft guidance, like the original version, describes how FDA intends to prioritize enforcement and regulatory action with regard to drug products, including biological products, labeled as homeopathic and marketed in the United States without the required FDA approval that potentially pose higher risk to public health. In response to comments received, we have revised the draft guidance and are reissuing it in draft form to enable the public to review and comment before it is finalized.
[E2] 2020-03-13 | official-forward (B) | comment_period_extension_notice | "Drug Products Labeled as Homeopathic; Draft Guidance for Food and Drug Administration Staff and Industry; Extension of Comment Period" | www.federalregister.gov
   Claims: The Food and Drug Administration (FDA or Agency) is extending the comment period for the notice entitled "Drug Products Labeled as Homeopathic; Draft Guidance for Food and Drug Administration Staff and Industry" that appeared in the Federal Register of October 25, 2019. The Agency is taking this act
   Excerpt: The Food and Drug Administration (FDA or Agency) is extending the comment period for the notice entitled "Drug Products Labeled as Homeopathic; Draft Guidance for Food and Drug Administration Staff and Industry" that appeared in the Federal Register of October 25, 2019. The Agency is taking this action to allow interested persons additional time to submit comments.
---
## SNAPSHOT S701dff47ab
CUTOFF DATE (today): 2024-06-21
Regulator: FDA (US)
Matter: FDA draft guidance: Measuring Growth and Evaluating Pubertal Development in Pediatric Clinical Trials
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence: none provided for this snapshot.
---
## SNAPSHOT Sf4d89ce3c7
CUTOFF DATE (today): 2024-07-11
Regulator: FDA (US)
Matter: FDA draft guidance: Mpox: Development of Drugs and Biological Products
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence: none provided for this snapshot.
---
## SNAPSHOT S51e1bf5436
CUTOFF DATE (today): 2026-03-16
Regulator: SEBI (IN)
Matter: SEBI consultation: permitting net settlement of funds for Foreign Portfolio Investor cash-market transactions
Decisive action for this matter = the regulator's first official publication ADOPTING the proposal at least in substantial part (e.g., board decision press release, circular, or notified regulation).
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2026-01-16 | official-forward (B) | consultation_paper | "Consultation Paper on proposal to permit netting of funds for transactions done by Foreign Portfolio Investors (FPIs)" | www.sebi.gov.in
   Claims: Proposes to permit net settlement of funds for outright transactions (purchase or sale, not both) done by FPIs in the cash market. / Notes FPIs currently settle transactions with custodians on a gross basis (Regulation 20(4), FPI Regulations 2019), adding funding costs and forex slippage; custodians already net-settle with clearing corporations. / States securities settlement would continue on a gross basis and STT/stamp duty would continue to be levied on a delivery basis; only the funds leg would be netted.
   Excerpt: In terms of Regulation 20(4) of SEBI (FPI) Regulations, 2019, FPIs are required to transact in securities in India only on the basis of taking and giving delivery of securities purchased or sold... SEBI has received feedback regarding review of the current practice in order to enhance operational efficiency and reduce cost of funding for FPIs. It is proposed to permit netting of funds for transactions done by FPIs in cash market.