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
## SNAPSHOT Sba5ebe1924
CUTOFF DATE (today): 2022-06-26
Regulator: FDA (US)
Matter: FDA draft guidance: General Clinical Pharmacology Considerations for Neonatal Studies for Drugs and Biological Products
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence: none provided for this snapshot.
---
## SNAPSHOT S40d325cdfa
CUTOFF DATE (today): 2020-12-24
Regulator: FDA (US)
Matter: FDA draft guidance: Development of Locally Applied Corticosteroid Products for the Short-Term Treatment of Symptoms Associated With Internal or External Hemorrhoids
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2019-12-06 | official-forward (B) | draft_guidance_availability_notice | "Development of Locally Applied Corticosteroid Products for the Short-Term Treatment of Symptoms Associated With Internal or External Hemorrhoids; Draft Guidance for Industry; Availability" | www.federalregister.gov
   Claims: The Food and Drug Administration (FDA or Agency) is announcing the availability of a draft guidance for industry entitled "Development of Locally Applied Corticosteroid Products for the Short- Term Treatment of Symptoms Associated with Internal or External Hemorrhoids." This draft guidance will serv
   Excerpt: The Food and Drug Administration (FDA or Agency) is announcing the availability of a draft guidance for industry entitled "Development of Locally Applied Corticosteroid Products for the Short- Term Treatment of Symptoms Associated with Internal or External Hemorrhoids." This draft guidance will serve as a focus for continued discussions among the Division of Gastroenterology and Inborn Error Products, pharmaceutical sponsors, the academic community, and the public.
---
## SNAPSHOT Sd85f5a8ab5
CUTOFF DATE (today): 2024-06-21
Regulator: FDA (US)
Matter: FDA draft guidance: Measuring Growth and Evaluating Pubertal Development in Pediatric Clinical Trials
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2022-11-01 | official-forward (B) | draft_guidance_availability_notice | "Measuring Growth and Evaluating Pubertal Development in Pediatric Clinical Trials; Draft Guidance for Industry; Availability" | www.federalregister.gov
   Claims: The Food and Drug Administration (FDA or Agency) is announcing the availability of a draft guidance for industry entitled "Measuring Growth and Evaluating Pubertal Development in Pediatric Clinical Trials." The purpose of this draft guidance is to outline the most appropriate methods for measuring a
   Excerpt: The Food and Drug Administration (FDA or Agency) is announcing the availability of a draft guidance for industry entitled "Measuring Growth and Evaluating Pubertal Development in Pediatric Clinical Trials." The purpose of this draft guidance is to outline the most appropriate methods for measuring and recording growth and evaluating pubertal development for drugs or biological products in development for pediatric use when such an assessment is necessary to support safety. This draft guidance is intended to encourage a consistent approach to collecting interpretable and accurate growth and pubertal development data. This draft guidance does not address use of growth or pubertal development data to support primary evidence of efficacy in growth disorders and does not address evaluation of nutritional status.
---
## SNAPSHOT Sbc7b9b0305
CUTOFF DATE (today): 2026-08-25
Regulator: SEBI (IN)
Matter: SEBI consultation: harmonizing base price for pre-open call auction and price bands for stocks listed on multiple exchanges
Decisive action for this matter = the regulator's first official publication ADOPTING the proposal at least in substantial part (e.g., board decision press release, circular, or notified regulation).
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2026-06-11 | official-forward (B) | consultation_paper | "Consultation Paper on Harmonization of Base price for Call Auction in Pre-open Session and for Price Band - For scrips listed on multiple stock exchanges" | www.sebi.gov.in
   Claims: Seeks public comments on proposals to harmonize the base price for the pre-open call-auction session, and price bands, for scrips listed on more than one recognized stock exchange. / Notes existing rule (Master Circular Para 2.3) prescribing individual scrip-wise price bands of up to 20% either way for scrips without derivatives products. / Notes existing rule (Master Circular Para 17.1.6) that price bands in the pre-open session equal those applicable in the normal market. / Frames the issue as inconsistency that can arise when a scrip is listed on multiple exchanges, each of which may independently apply these base-price/price-band rules.
   Excerpt: The objective of this consultation paper is to seek public comments on the proposals to harmonize the base price for call auction in pre-open session and for setting up price bands for scrips listed on multiple stock exchanges. Background: As a measure against excessive price movements, SEBI vide circular No. SMDRPD/Policy/Cir-37/2001 dated June 28, 2001 has advised stock exchanges to implement individual scrip wise price bands of 20% either way, for all scrips in compulsory rolling settlement except for the scrips on which derivatives products are available or scrips included in indices on which derivatives products are available.
---
## SNAPSHOT Sa2c9f237e7
CUTOFF DATE (today): 2023-04-06
Regulator: FDA (US)
Matter: FDA draft guidance: Peripheral Percutaneous Transluminal Angioplasty and Specialty Catheters-Premarket Notification (510(k)) Submissions
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2020-01-13 | official-forward (B) | draft_guidance_availability_notice | "Peripheral Percutaneous Transluminal Angioplasty and Specialty Catheters-Premarket Notification (510(k)) Submissions; Draft Guidance for Industry and Food and Drug Administration Staff; Availability" | www.federalregister.gov
   Claims: The Food and Drug Administration (FDA or Agency) is announcing the availability of the draft guidance entitled "Peripheral Percutaneous Transluminal Angioplasty (PTA) and Specialty Catheters-- Premarket Notification (510(k)) Submissions; Draft Guidance for Industry and Food and Drug Administration S
   Excerpt: The Food and Drug Administration (FDA or Agency) is announcing the availability of the draft guidance entitled "Peripheral Percutaneous Transluminal Angioplasty (PTA) and Specialty Catheters-- Premarket Notification (510(k)) Submissions; Draft Guidance for Industry and Food and Drug Administration Staff." The FDA is issuing this draft guidance document to provide recommendations for 510(k) submissions for peripheral percutaneous transluminal angioplasty (PTA) balloons and specialty catheters (e.g., infusion catheters, PTA balloon catheters for in-stent restenosis (ISR), scoring/cutting balloons). This draft guidance is not final nor is it in effect at this time.
---
## SNAPSHOT S647d6d4f8b
CUTOFF DATE (today): 2023-03-03
Regulator: FDA (US)
Matter: FDA draft guidance: Evaluation of Gastric pH-Dependent Drug Interactions With Acid-Reducing Agents: Study Design, Data Analysis, and Clinical Implications
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2020-12-01 | official-forward (B) | draft_guidance_availability_notice | "Evaluation of Gastric pH-Dependent Drug Interactions With Acid-Reducing Agents: Study Design, Data Analysis, and Clinical Implications; Draft Guidance for Industry; Availability" | www.federalregister.gov
   Claims: The Food and Drug Administration (FDA or Agency) is announcing the availability of a draft guidance for industry entitled "Evaluation of Gastric pH-Dependent Drug Interactions With Acid-Reducing Agents: Study Design, Data Analysis, and Clinical Implications." This draft guidance focuses on specific 
   Excerpt: The Food and Drug Administration (FDA or Agency) is announcing the availability of a draft guidance for industry entitled "Evaluation of Gastric pH-Dependent Drug Interactions With Acid-Reducing Agents: Study Design, Data Analysis, and Clinical Implications." This draft guidance focuses on specific recommendations pertinent to gastric pH- dependent drug-drug interaction (DDI) assessment and describes the FDA's recommendations regarding when clinical DDI studies with acid- reducing agents (ARAs) are needed; design of the clinical studies; interpretation of study results; and communicating findings and options for managing pH-dependent DDIs in product labeling.
---
## SNAPSHOT Sf167e5f899
CUTOFF DATE (today): 2023-05-18
Regulator: FDA (US)
Matter: FDA draft guidance: Adjusting for Covariates in Randomized Clinical Trials for Drugs and Biological Products
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2021-05-21 | official-forward (B) | draft_guidance_availability_notice | "Adjusting for Covariates in Randomized Clinical Trials for Drugs and Biological Products; Draft Guidance for Industry; Availability" | www.federalregister.gov
   Claims: The Food and Drug Administration (FDA or Agency) is announcing the availability of a draft guidance for industry entitled "Adjusting for Covariates in Randomized Clinical Trials for Drugs and Biological Products." The draft guidance, when finalized, will represent the current thinking of FDA on adju
   Excerpt: The Food and Drug Administration (FDA or Agency) is announcing the availability of a draft guidance for industry entitled "Adjusting for Covariates in Randomized Clinical Trials for Drugs and Biological Products." The draft guidance, when finalized, will represent the current thinking of FDA on adjusting for covariates in randomized clinical trials for drugs and biologics. This draft guidance revises the draft guidance "Adjusting for Covariates in Randomized Clinical Trials for Drugs and Biologics with Continuous Outcomes" that published April 25, 2019. This revision provides more detailed recommendations for the use of linear models for covariate adjustment and also includes recommendations for covariate adjustment using nonlinear models.
---
## SNAPSHOT Sbf87678739
CUTOFF DATE (today): 2026-07-27
Regulator: SEBI (IN)
Matter: SEBI consultation: phased introduction of physical settlement in select agricultural commodity derivatives contracts
Decisive action for this matter = the regulator's first official publication ADOPTING the proposal at least in substantial part (e.g., board decision press release, circular, or notified regulation).
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2026-05-12 | official-forward (B) | consultation_paper | "Consultation Paper on 'Phased Introduction of Physical Settlement in Select Agricultural Commodity Derivatives Contracts'" | www.sebi.gov.in
   Claims: Proposes to permit exchanges, on a pilot basis, to launch delivery-based agricultural commodity derivatives contracts that start as financially-settled and mandatorily convert to physical settlement upon crossing predefined objective thresholds. / States the proposal does not dilute the principle of physical settlement; contracts remain designed as delivery-based instruments from inception, with the financially-settled phase only a temporary transitional arrangement. / Frames the review against the backdrop that compulsory physical settlement from contract inception may inhibit early liquidity formation and participation. / Notes agricultural commodity derivatives in India have historically emphasized physical settlement to ensure futures-spot price convergence and discourage excessive speculation.
   Excerpt: This consultation paper seeks stakeholder views on a proposal to permit exchanges, on a pilot basis, to introduce delivery-based agricultural commodity derivatives contracts that commence trading as financially-settled contracts and mandatorily transition into physically settled contracts upon the occurrence of predefined objective thresholds. Commodity derivatives markets play a vital role in the efficient functioning of agricultural value chains by facilitating price discovery, risk management, and market transparency.
---
## SNAPSHOT Sfec9149de9
CUTOFF DATE (today): 2024-09-17
Regulator: FDA (US)
Matter: FDA draft guidance: Review of Drug Master Files in Advance of Certain Abbreviated New Drug Application Submissions Under Generic Drug User Fee Amendments
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2022-10-06 | official-forward (B) | draft_guidance_availability_notice | "Review of Drug Master Files in Advance of Certain Abbreviated New Drug Application Submissions Under Generic Drug User Fee Amendments; Draft Guidance for Industry; Availability" | www.federalregister.gov
   Claims: The Food and Drug Administration (FDA or Agency) is announcing the availability of a draft guidance for industry entitled "Review of Drug Master Files in Advance of Certain ANDA Submissions Under GDUFA." The purpose of this draft guidance is to provide information and recommendations on the Generic 
   Excerpt: The Food and Drug Administration (FDA or Agency) is announcing the availability of a draft guidance for industry entitled "Review of Drug Master Files in Advance of Certain ANDA Submissions Under GDUFA." The purpose of this draft guidance is to provide information and recommendations on the Generic Drug User Fee Amendments (GDUFA) III program enhancements agreed upon by the Agency and industry in "GDUFA Reauthorization Performance Goals and Program Enhancements Fiscal Years 2023-2027" (GDUFA III commitment letter), related to the early assessment of certain Type II drug master files (DMFs) 6 months prior to the submission of certain abbreviated new drug applications (ANDAs) or prior approval supplements (PASs). This draft guidance describes the process outlined in the GDUFA III commitment letter in greater detail and provides recommendations to DMF holders on how to provide the relevant information to FDA.
---
## SNAPSHOT Sf3e21214fa
CUTOFF DATE (today): 2026-05-20
Regulator: SEBI (IN)
Matter: SEBI consultation: 'Green-Channel' document-acknowledgement mechanism for launch of Alternative Investment Fund schemes
Decisive action for this matter = the regulator's first official publication ADOPTING the proposal at least in substantial part (e.g., board decision press release, circular, or notified regulation).
Evidence: none provided for this snapshot.
---
## SNAPSHOT Sc4349017f1
CUTOFF DATE (today): 2023-09-07
Regulator: FDA (US)
Matter: FDA draft guidance: Verification Systems Under the Drug Supply Chain Security Act for Certain Prescription Drugs
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence: none provided for this snapshot.
---
## SNAPSHOT S8a6b44e3b6
CUTOFF DATE (today): 2021-10-27
Regulator: FDA (US)
Matter: FDA draft guidance: Principles for Selecting, Developing, Modifying, and Adapting Patient-Reported Outcome Instruments for Use in Medical Device Evaluation
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2020-08-31 | official-forward (B) | draft_guidance_availability_notice | "Principles for Selecting, Developing, Modifying, and Adapting Patient-Reported Outcome Instruments for Use in Medical Device Evaluation; Draft Guidance for Industry, Food and Drug Administration Staff, and Other Stakehol" | www.federalregister.gov
   Claims: The Food and Drug Administration (FDA or Agency) is announcing the availability of the draft guidance entitled "Principles for Selecting, Developing, Modifying, and Adapting Patient-Reported Outcome Instruments for Use in Medical Device Evaluation." The FDA encourages the collection, analysis, and i
   Excerpt: The Food and Drug Administration (FDA or Agency) is announcing the availability of the draft guidance entitled "Principles for Selecting, Developing, Modifying, and Adapting Patient-Reported Outcome Instruments for Use in Medical Device Evaluation." The FDA encourages the collection, analysis, and integration of patient perspectives in the development, evaluation, and surveillance of medical devices, including digital health technologies. Patient-reported outcome (PRO) instruments facilitate the systematic collection of patient perspectives as scientific evidence to support the regulatory and healthcare decision-making process. This draft guidance describes principles that should be considered when using PRO instruments in the evaluation of medical devices and provides recommendations about the importance of ensuring the measures are "fit-for-purpose." This draft guidance is not final nor is it in effect at this time.
---
## SNAPSHOT S1d583345a9
CUTOFF DATE (today): 2026-02-07
Regulator: SEBI (IN)
Matter: SEBI consultation: uniform time lag for sharing and usage of price data for educational purposes
Decisive action for this matter = the regulator's first official publication ADOPTING the proposal at least in substantial part (e.g., board decision press release, circular, or notified regulation).
Evidence: none provided for this snapshot.
---
## SNAPSHOT S3642d77c63
CUTOFF DATE (today): 2026-06-29
Regulator: SEBI (IN)
Matter: SEBI consultation: draft circular on trading software/technology at stock exchanges and common IT provisions for market infrastructure institutions
Decisive action for this matter = the regulator's first official publication ADOPTING the proposal at least in substantial part (e.g., board decision press release, circular, or notified regulation).
Evidence: none provided for this snapshot.
---
## SNAPSHOT S4402956385
CUTOFF DATE (today): 2026-05-14
Regulator: SEBI (IN)
Matter: SEBI consultation: reviewing use of historical price scenarios in stress testing for the Commodity Derivatives Segment
Decisive action for this matter = the regulator's first official publication ADOPTING the proposal at least in substantial part (e.g., board decision press release, circular, or notified regulation).
Evidence: none provided for this snapshot.
---
## SNAPSHOT S7afce771d5
CUTOFF DATE (today): 2026-08-07
Regulator: SEBI (IN)
Matter: SEBI consultation: treatment of debt-funded major maintenance expenses in Net Distributable Cash Flow calculation for Infrastructure Investment Trusts
Decisive action for this matter = the regulator's first official publication ADOPTING the proposal at least in substantial part (e.g., board decision press release, circular, or notified regulation).
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2026-06-01 | official-forward (B) | draft_circular_for_comment | "Consultation Paper on Review of Framework for Calculation of Net Distributable Cash Flows for InvITs" | www.sebi.gov.in
   Claims: The extant Master Circular framework (Dec 6, 2023, consolidated July 11, 2025) expressly prohibits InvITs/SPVs from distributing cash flows obtained via external debt. / Bharat InvITs Association (BIA) requested that debt availed by InvITs/SPVs for major maintenance expenses of road projects be added back in computing Net Distributable Cash Flow (NDCF). / The paper seeks public comment on whether/how to modify the NDCF computation framework to accommodate debt-funded major-maintenance expenses for road projects.
   Excerpt: SEBI vide circular dated December 06, 2023 (consolidated as part of Chapter 3 of Master Circular for Infrastructure Investment Trusts dated July 11, 2025) prescribed a standardized framework for calculation of Net Distributable Cash Flow ('NDCF') for InvITs which inter-alia prohibited using borrowed money for distributions to unitholders. SEBI is in receipt of request from Bharat InvITs Association (BIA) regarding treatment of debt availed by InvITs for incurring major maintenance expenses of road projects while calculating the NDCF.
---
## SNAPSHOT S7064af60f7
CUTOFF DATE (today): 2022-07-15
Regulator: FDA (US)
Matter: FDA draft guidance: Select Updates for Unique Device Identification: Policy Regarding Global Unique Device Identification Database Requirements for Certain Devices
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2021-10-14 | official-forward (B) | draft_guidance_availability_notice | "Select Updates for Unique Device Identification: Policy Regarding Global Unique Device Identification Database Requirements for Certain Devices; Draft Guidance for Industry and Food and Drug Administration Staff; Availab" | www.federalregister.gov
   Claims: The Food and Drug Administration (FDA, Agency, or we) is announcing the availability of the draft guidance entitled "Select Updates for Unique Device Identification: Policy Regarding Global Unique Device Identification Database Requirements for Certain Devices; Draft Guidance for Industry and Food a
   Excerpt: The Food and Drug Administration (FDA, Agency, or we) is announcing the availability of the draft guidance entitled "Select Updates for Unique Device Identification: Policy Regarding Global Unique Device Identification Database Requirements for Certain Devices; Draft Guidance for Industry and Food and Drug Administration Staff." This draft guidance explains that there are certain class I devices for which FDA does not intend to enforce Global Unique Device Identification Database (GUDID) submission requirements and describes how a labeler of a class I device can determine if its device is one of these devices in the revised section III of this draft guidance. When this draft guidance is finalized, the updates in section III of this draft guidance would supersede the recommendations in section III of the guidance "Unique Device Identification: Policy Regarding Compliance Dates for Class I and Unclassified Devices and Certain Devices Requiring Direct Marking" ("2020 UDI Compliance Policy Guidance," available at: https:// www.fda.gov/regulatory-information/search-fda-guidance-documents/ unique-device-identification-policy-regarding-compliance-dates-class-i- and-unclassified-devices-an
---
## SNAPSHOT S334d1bc8f5
CUTOFF DATE (today): 2024-02-07
Regulator: FDA (US)
Matter: FDA draft guidance: Charging for Investigational Drugs Under an Investigational New Drug Application: Questions and Answers
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence: none provided for this snapshot.
---
## SNAPSHOT Sc80286c23a
CUTOFF DATE (today): 2026-05-20
Regulator: SEBI (IN)
Matter: SEBI consultation: recognizing intraday borrowing facilities as a cash-management tool for mutual funds
Decisive action for this matter = the regulator's first official publication ADOPTING the proposal at least in substantial part (e.g., board decision press release, circular, or notified regulation).
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2026-05-13 | official-forward (B) | consultation_paper | "Consultation Paper on utilization of intraday borrowing lines by Mutual Funds" | www.sebi.gov.in
   Claims: Proposes to recognize intraday borrowing facilities used by mutual funds as a cash-management tool, with necessary safeguards and consistency across AMCs. / Notes an intraday-borrowing carve-out already exists in SEBI (Mutual Funds) Regulations, 2026 (effective April 1, 2026) and related March 13, 2026 circular safeguards, for the specific purpose of meeting redemption/unitholder payouts. / States the applicability of the existing intraday-borrowing guidelines had been deferred to July 15, 2026 due to operational challenges raised by AMFI/AMCs. / Based on AMFI representations on using intraday borrowing to bridge timing gaps between redemption payouts and receipt of guaranteed receivables from GoI/RBI/CCIL.
   Excerpt: The objective of this consultation paper is to solicit comments on the proposal to recognize intraday borrowing facilities utilized by Mutual Funds as a cash management tool, consider necessary safeguards and consistency in practices among Mutual Funds. Based on representation made by Association of Mutual Funds in India (AMFI) on intraday borrowing arrangement by mutual funds to bridge the timing gap between redemption payouts and receipt of guaranteed receivables due on the same day from Government of India (GoI), Reserve Bank of India (RBI) and Clearing Corporation of India Limited (CCIL), a carve out for intraday borrowings was enabled in SEBI (Mutual Funds) Regulations, 2026.
---
## SNAPSHOT S92671b8fb5
CUTOFF DATE (today): 2022-07-07
Regulator: FDA (US)
Matter: FDA draft guidance: Instructions for Use-Patient Labeling for Human Prescription Drug and Biological Products and Drug-Device and Biologic-Device Combination Products-Content and Format
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence: none provided for this snapshot.