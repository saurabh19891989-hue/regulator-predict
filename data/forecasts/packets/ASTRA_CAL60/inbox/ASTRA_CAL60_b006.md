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
## SNAPSHOT S9c27027731
CUTOFF DATE (today): 2021-07-01
Regulator: FDA (US)
Matter: FDA draft guidance: General Clinical Pharmacology Considerations for Neonatal Studies for Drugs and Biological Products
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2019-08-01 | official-forward (B) | draft_guidance_availability_notice | "General Clinical Pharmacology Considerations for Neonatal Studies for Drugs and Biological Products; Draft Guidance for Industry; Availability" | www.federalregister.gov
   Claims: The Food and Drug Administration (FDA or Agency) is announcing the availability of a draft guidance for industry entitled "General Clinical Pharmacology Considerations for Neonatal Studies for Drugs and Biological Products." This draft guidance is intended to assist sponsors of new drug applications
   Excerpt: The Food and Drug Administration (FDA or Agency) is announcing the availability of a draft guidance for industry entitled "General Clinical Pharmacology Considerations for Neonatal Studies for Drugs and Biological Products." This draft guidance is intended to assist sponsors of new drug applications (NDAs), biologics license applications (BLAs) for therapeutic biologics, and supplements who are planning to conduct clinical studies in neonatal populations. The issuance of this draft guidance on clinical pharmacology considerations for neonatal studies for drugs and biological products is stipulated under the FDA Reauthorization Act of 2017 (FDARA).
---
## SNAPSHOT S622b1a404a
CUTOFF DATE (today): 2026-08-25
Regulator: SEBI (IN)
Matter: SEBI consultation: draft circular on trading software/technology at stock exchanges and common IT provisions for market infrastructure institutions
Decisive action for this matter = the regulator's first official publication ADOPTING the proposal at least in substantial part (e.g., board decision press release, circular, or notified regulation).
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2026-06-22 | official-forward (B) | consultation_paper | "Consultation Paper on Draft Circular for Trading Software & Technology at Stock Exchanges and Draft Circular on Common IT related provisions for MIIs" | www.sebi.gov.in
   Claims: Proposes a draft circular modifying trading-software-and-technology provisions of the Master Circular for Stock Exchanges & Clearing Corporations and the Master Circular for Commodity Derivatives. / Proposes a separate draft consolidated circular on common IT-related provisions for market infrastructure institutions (MIIs), amending the Master Circular for Depositories. / Frames the exercise as implementing the FY2023-24 budget announcement to simplify and reduce compliance cost via public consultation before issuing circulars. / Identifies this as a further paper in the same series that already included CPs on Administration of Exchanges (Oct 8, 2025) and Trading at Exchanges (Jan 9, 2026).
   Excerpt: In order to align the process of review of Master Circulars with the budget announcement, SEBI, inter-alia, prior to issuing a circular under the Acts or regulations, generally, undertakes public consultation. Therefore, in compliance with the mandate and procedure envisaged in the aforesaid budget announcement, towards facilitating ease of doing business/compliance for stock exchanges, following Consultation Papers (CPs) have been issued: CP on Measures for ease of doing business on Administration of Exchanges... has been put up for public comments on October 08, 2025. CP on Measures for ease of doing business on Trading at Exchanges... has been put up for public comments on January 09, 2026.
---
## SNAPSHOT S6778381bd2
CUTOFF DATE (today): 2026-08-25
Regulator: SEBI (IN)
Matter: SEBI consultation: reviewing the pre-open call auction price-discovery mechanism for IPO listings and re-listed scrips
Decisive action for this matter = the regulator's first official publication ADOPTING the proposal at least in substantial part (e.g., board decision press release, circular, or notified regulation).
Evidence: none provided for this snapshot.
---
## SNAPSHOT Sd46f6a5b39
CUTOFF DATE (today): 2023-01-01
Regulator: FDA (US)
Matter: FDA draft guidance: Benefit-Risk Considerations for Product Quality Assessments
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence: none provided for this snapshot.
---
## SNAPSHOT Sf1127b5b8d
CUTOFF DATE (today): 2026-07-26
Regulator: SEBI (IN)
Matter: SEBI consultation: aligning Trading Member position limits in the Equity Derivatives Segment with the client-level Futures-Equivalent metric
Decisive action for this matter = the regulator's first official publication ADOPTING the proposal at least in substantial part (e.g., board decision press release, circular, or notified regulation).
Evidence: none provided for this snapshot.
---
## SNAPSHOT Sf879ce8281
CUTOFF DATE (today): 2024-01-01
Regulator: FDA (US)
Matter: FDA draft guidance: Neovascular Age-Related Macular Degeneration: Developing Drugs for Treatment
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence: none provided for this snapshot.
---
## SNAPSHOT Sf50ef13599
CUTOFF DATE (today): 2026-06-26
Regulator: SEBI (IN)
Matter: SEBI consultation: ease-of-doing-business modifications to master circular provisions on administration of stock exchanges
Decisive action for this matter = the regulator's first official publication ADOPTING the proposal at least in substantial part (e.g., board decision press release, circular, or notified regulation).
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2025-10-08 | official-forward (B) | consultation_paper | "Consultation Paper on Measures for ease of doing business on Administration of Exchanges" | www.sebi.gov.in
   Claims: First in a series of ease-of-doing-business consultation papers reviewing SEBI's exchange-related master circulars, implementing a FY2023-24 budget announcement on consultative compliance simplification. / Proposes modifications to Chapter 6 (Administration of Stock Exchanges) of the Master Circular for Stock Exchanges and Clearing Corporations, and related chapters of the Master Circular for Commodity Derivatives Segment. / Covers administration of stock exchanges including commodity derivatives exchanges.
   Excerpt: CONSULTATION PAPER ON ADMINISTRATION OF STOCK EXCHANGES- FOR PUBLIC COMMENTS. Measures for ease of doing business for MIIs- " Modifications to Master Circular for Stock Exchanges and Clearing Corporations, Master Circular for Commodity Derivatives Segment on Administration of Stock Exchanges (including Commodity Derivatives Exchanges)". The Hon'ble Finance Minister in the budget announcements for FY 2023-24, inter-alia, made an announcement to simplify, ease and reduce cost of compliance for participants in the financial sector through a consultative process.
---
## SNAPSHOT S58e27071d5
CUTOFF DATE (today): 2023-07-01
Regulator: FDA (US)
Matter: FDA draft guidance: Marketing Submission Recommendations for a Predetermined Change Control Plan for Artificial Intelligence/Machine Learning-Enabled Device Software Functions
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2023-03-30 | official-forward (B) | draft_guidance_availability_notice | "Marketing Submission Recommendations for a Predetermined Change Control Plan for Artificial Intelligence/Machine Learning-Enabled Device Software Functions; Draft Guidance for Industry and Food and Drug Administration St" | www.federalregister.gov
   Claims: The Food and Drug Administration (FDA or Agency) is announcing the availability of the draft guidance entitled "Marketing Submission Recommendations for a Predetermined Change Control Plan for Artificial Intelligence/Machine Learning (AI/ML)-Enabled Device Software Functions." This draft guidance de
   Excerpt: The Food and Drug Administration (FDA or Agency) is announcing the availability of the draft guidance entitled "Marketing Submission Recommendations for a Predetermined Change Control Plan for Artificial Intelligence/Machine Learning (AI/ML)-Enabled Device Software Functions." This draft guidance demonstrates FDA's commitment to developing innovative approaches to the regulation of machine learning- enabled medical devices and describes an approach that would often be the least burdensome and would support iterative improvement through modifications to machine learning-enabled device software functions (herein referred to as ML-DSF) while continuing to ensure device safety and effectiveness. This draft guidance provides recommendations on the information to be included in a Predetermined Change Control Plan (PCCP) in a marketing submission for an ML-DSF. Such a plan describes the anticipated ML-DSF modifications and the associated methodology to implement those modifications, which would be reviewed in the marketing submission to ensure the continued safety and effectiveness of the device without necessitating additional marketing submissions for each modification described in the
---
## SNAPSHOT S575b436996
CUTOFF DATE (today): 2026-06-26
Regulator: SEBI (IN)
Matter: SEBI consultation: proposed amendments to the certification regime for associated persons in the securities markets
Decisive action for this matter = the regulator's first official publication ADOPTING the proposal at least in substantial part (e.g., board decision press release, circular, or notified regulation).
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2025-11-06 | official-forward (B) | consultation_paper | "Consultation paper on Amendments to SEBI (Certification of Associated Persons in the Securities Markets) Regulations, 2007" | www.sebi.gov.in
   Claims: Proposes reviewing/expanding the definition of 'Associated Persons' under CAPSM Regulations, 2007. / Proposes changes to the manner of obtaining the NISM certificate required under the regulations. / Proposes allowing an electronic mode of participation for Continuing Professional Education (CPE) programs. / Proposes reviewing the exception criteria governing the manner of obtaining the certificate (e.g. age/experience-based exemptions).
   Excerpt: To solicit comments / views / suggestions from the public and other stakeholders on the proposed amendments to 'SEBI (Certification of Associated Persons in the Securities Markets) Regulations, 2007 ("CAPSM Regulations")'. The following proposals are being made: 1.1.1 Review / Expansion of the definition of 'Associated Persons' 1.1.2 Manner of obtaining certificate 1.1.3 Inclusion of electronic mode of participation for Continuing Professional Education (CPE) programs 1.1.4 Reviewing the exception criteria for manner of obtaining certificate.
---
## SNAPSHOT S5f86902119
CUTOFF DATE (today): 2024-07-01
Regulator: FDA (US)
Matter: FDA draft guidance: International Cooperation on Harmonisation of Technical Requirements for Registration of Veterinary Medicinal Products; Effectiveness of Anthelmintics: Specific Recommendations ...
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2022-08-11 | official-forward (B) | draft_guidance_availability_notice | "International Cooperation on Harmonisation of Technical Requirements for Registration of Veterinary Medicinal Products; Effectiveness of Anthelmintics: Specific Recommendations for Caprines (Revision 1); Draft Guidance f" | www.federalregister.gov
   Claims: The Food and Drug Administration (FDA or Agency) is announcing the availability of a draft guidance for industry GFI #97 (VICH GL14(R1)) entitled "Effectiveness of Anthelmintics: Specific Recommendations for Caprines (Revision 1)." This draft guidance has been developed for veterinary use by the Int
   Excerpt: The Food and Drug Administration (FDA or Agency) is announcing the availability of a draft guidance for industry GFI #97 (VICH GL14(R1)) entitled "Effectiveness of Anthelmintics: Specific Recommendations for Caprines (Revision 1)." This draft guidance has been developed for veterinary use by the International Cooperation on Harmonisation of Technical Requirements for Registration of Veterinary Medicinal Products (VICH). This revision clarifies the definition of adequate infection in individual animals, updates considerations for field studies, and makes additional clarifying changes.
---
## SNAPSHOT Sddc72cdd59
CUTOFF DATE (today): 2020-07-01
Regulator: FDA (US)
Matter: FDA draft guidance: Technical Considerations for Demonstrating Reliability of Emergency-Use Injectors Submitted Under a Biologics License Application, New Drug Application, or Abbreviated New Drug ...
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2020-04-21 | official-forward (B) | draft_guidance_availability_notice | "Technical Considerations for Demonstrating Reliability of Emergency-Use Injectors Submitted Under a Biologics License Application, New Drug Application, or Abbreviated New Drug Application; Draft Guidance for Industry an" | www.federalregister.gov
   Claims: The Food and Drug Administration (FDA or Agency) is announcing the availability of a draft guidance for industry and FDA entitled "Technical Considerations for Demonstrating Reliability of Emergency- Use Injectors Submitted under a BLA, NDA or ANDA." For injectable drug or biological products that a
   Excerpt: The Food and Drug Administration (FDA or Agency) is announcing the availability of a draft guidance for industry and FDA entitled "Technical Considerations for Demonstrating Reliability of Emergency- Use Injectors Submitted under a BLA, NDA or ANDA." For injectable drug or biological products that are intended to treat emergent, life- threatening conditions, it is essential to ensure that the emergency- use injector will reliably deliver the drug or biological product as intended. This is particularly critical for drugs when failure of the injector may prevent adequate delivery of a life-saving drug to a patient. The draft guidance describes the technical considerations for demonstrating reliability of emergency-use injectors under a biologics license application (BLA), new drug application (NDA), or abbreviated new drug application (ANDA).
---
## SNAPSHOT Se2c3aa22b5
CUTOFF DATE (today): 2024-01-01
Regulator: FDA (US)
Matter: FDA draft guidance: Mpox: Development of Drugs and Biological Products
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2023-01-20 | official-forward (B) | draft_guidance_availability_notice | "Mpox: Development of Drugs and Biological Products; Draft Guidance for Industry; Availability" | www.federalregister.gov
   Claims: The Food and Drug Administration (FDA or Agency) is announcing the availability of a draft guidance for industry entitled "Mpox: Development of Drugs and Biological Products." FDA is issuing this guidance to support sponsors in their development of drugs and biological products for mpox.
   Excerpt: The Food and Drug Administration (FDA or Agency) is announcing the availability of a draft guidance for industry entitled "Mpox: Development of Drugs and Biological Products." FDA is issuing this guidance to support sponsors in their development of drugs and biological products for mpox.
---
## SNAPSHOT S88e33f7768
CUTOFF DATE (today): 2023-01-01
Regulator: FDA (US)
Matter: FDA draft guidance: Voluntary Malfunction Summary Reporting Program for Manufacturers
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2022-12-09 | official-forward (B) | draft_guidance_availability_notice | "Voluntary Malfunction Summary Reporting Program for Manufacturers; Draft Guidance for Industry and Food and Drug Administration Staff; Availability" | www.federalregister.gov
   Claims: The Food and Drug Administration (FDA or Agency) is announcing the availability of the draft guidance entitled "Voluntary Malfunction Summary Reporting (VMSR) Program for Manufacturers." We are publishing this notice of availability for this draft guidance document to help manufacturers better under
   Excerpt: The Food and Drug Administration (FDA or Agency) is announcing the availability of the draft guidance entitled "Voluntary Malfunction Summary Reporting (VMSR) Program for Manufacturers." We are publishing this notice of availability for this draft guidance document to help manufacturers better understand and use the VMSR Program. It is intended to further explain, but not change, the conditions of the VMSR Program. This draft guidance is not final nor is it for implementation at this time.
---
## SNAPSHOT S593ea49276
CUTOFF DATE (today): 2022-01-01
Regulator: FDA (US)
Matter: FDA draft guidance: Select Updates for Unique Device Identification: Policy Regarding Global Unique Device Identification Database Requirements for Certain Devices
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2021-10-14 | official-forward (B) | draft_guidance_availability_notice | "Select Updates for Unique Device Identification: Policy Regarding Global Unique Device Identification Database Requirements for Certain Devices; Draft Guidance for Industry and Food and Drug Administration Staff; Availab" | www.federalregister.gov
   Claims: The Food and Drug Administration (FDA, Agency, or we) is announcing the availability of the draft guidance entitled "Select Updates for Unique Device Identification: Policy Regarding Global Unique Device Identification Database Requirements for Certain Devices; Draft Guidance for Industry and Food a
   Excerpt: The Food and Drug Administration (FDA, Agency, or we) is announcing the availability of the draft guidance entitled "Select Updates for Unique Device Identification: Policy Regarding Global Unique Device Identification Database Requirements for Certain Devices; Draft Guidance for Industry and Food and Drug Administration Staff." This draft guidance explains that there are certain class I devices for which FDA does not intend to enforce Global Unique Device Identification Database (GUDID) submission requirements and describes how a labeler of a class I device can determine if its device is one of these devices in the revised section III of this draft guidance. When this draft guidance is finalized, the updates in section III of this draft guidance would supersede the recommendations in section III of the guidance "Unique Device Identification: Policy Regarding Compliance Dates for Class I and Unclassified Devices and Certain Devices Requiring Direct Marking" ("2020 UDI Compliance Policy Guidance," available at: https:// www.fda.gov/regulatory-information/search-fda-guidance-documents/ unique-device-identification-policy-regarding-compliance-dates-class-i- and-unclassified-devices-an
---
## SNAPSHOT S165b9eee4c
CUTOFF DATE (today): 2024-01-01
Regulator: FDA (US)
Matter: FDA draft guidance: Measuring Growth and Evaluating Pubertal Development in Pediatric Clinical Trials
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2022-11-01 | official-forward (B) | draft_guidance_availability_notice | "Measuring Growth and Evaluating Pubertal Development in Pediatric Clinical Trials; Draft Guidance for Industry; Availability" | www.federalregister.gov
   Claims: The Food and Drug Administration (FDA or Agency) is announcing the availability of a draft guidance for industry entitled "Measuring Growth and Evaluating Pubertal Development in Pediatric Clinical Trials." The purpose of this draft guidance is to outline the most appropriate methods for measuring a
   Excerpt: The Food and Drug Administration (FDA or Agency) is announcing the availability of a draft guidance for industry entitled "Measuring Growth and Evaluating Pubertal Development in Pediatric Clinical Trials." The purpose of this draft guidance is to outline the most appropriate methods for measuring and recording growth and evaluating pubertal development for drugs or biological products in development for pediatric use when such an assessment is necessary to support safety. This draft guidance is intended to encourage a consistent approach to collecting interpretable and accurate growth and pubertal development data. This draft guidance does not address use of growth or pubertal development data to support primary evidence of efficacy in growth disorders and does not address evaluation of nutritional status.
---
## SNAPSHOT S00953fd06d
CUTOFF DATE (today): 2020-01-01
Regulator: FDA (US)
Matter: FDA draft guidance: Instructions for Use-Patient Labeling for Human Prescription Drug and Biological Products and Drug-Device and Biologic-Device Combination Products-Content and Format
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2019-07-01 | official-forward (B) | draft_guidance_availability_notice | "Instructions for Use-Patient Labeling for Human Prescription Drug and Biological Products and Drug-Device and Biologic-Device Combination Products-Content and Format; Draft Guidance for Industry; Availability" | www.federalregister.gov
   Claims: The Food and Drug Administration (FDA or Agency) is announcing the availability of a draft guidance for industry entitled "Instructions for Use--Patient Labeling for Human Prescription Drug and Biological Products and Drug-Device and Biologic-Device Combination Products--Content and Format." This dr
   Excerpt: The Food and Drug Administration (FDA or Agency) is announcing the availability of a draft guidance for industry entitled "Instructions for Use--Patient Labeling for Human Prescription Drug and Biological Products and Drug-Device and Biologic-Device Combination Products--Content and Format." This draft guidance provides recommendations for developing the content and format of an Instructions for Use (IFU) document for human prescription drugs and biological products and drug-device or biologic-device combination products submitted under a new drug application (NDA) or a biologics license application (BLA). The IFU is developed by applicants for patients who use drug products that have complicated or detailed patient-use instructions. The recommendations in this draft guidance are intended to help develop consistent content and format across IFUs and to help ensure that patients receive clear, concise information that is easily understood for the safe and effective use of prescription drug products.
---
## SNAPSHOT Sfbaa73c5dc
CUTOFF DATE (today): 2024-01-01
Regulator: FDA (US)
Matter: FDA draft guidance: Review of Drug Master Files in Advance of Certain Abbreviated New Drug Application Submissions Under Generic Drug User Fee Amendments
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2022-10-06 | official-forward (B) | draft_guidance_availability_notice | "Review of Drug Master Files in Advance of Certain Abbreviated New Drug Application Submissions Under Generic Drug User Fee Amendments; Draft Guidance for Industry; Availability" | www.federalregister.gov
   Claims: The Food and Drug Administration (FDA or Agency) is announcing the availability of a draft guidance for industry entitled "Review of Drug Master Files in Advance of Certain ANDA Submissions Under GDUFA." The purpose of this draft guidance is to provide information and recommendations on the Generic 
   Excerpt: The Food and Drug Administration (FDA or Agency) is announcing the availability of a draft guidance for industry entitled "Review of Drug Master Files in Advance of Certain ANDA Submissions Under GDUFA." The purpose of this draft guidance is to provide information and recommendations on the Generic Drug User Fee Amendments (GDUFA) III program enhancements agreed upon by the Agency and industry in "GDUFA Reauthorization Performance Goals and Program Enhancements Fiscal Years 2023-2027" (GDUFA III commitment letter), related to the early assessment of certain Type II drug master files (DMFs) 6 months prior to the submission of certain abbreviated new drug applications (ANDAs) or prior approval supplements (PASs). This draft guidance describes the process outlined in the GDUFA III commitment letter in greater detail and provides recommendations to DMF holders on how to provide the relevant information to FDA.
---
## SNAPSHOT S99891dc1ab
CUTOFF DATE (today): 2023-07-01
Regulator: FDA (US)
Matter: FDA draft guidance: Verification Systems Under the Drug Supply Chain Security Act for Certain Prescription Drugs
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2022-03-10 | official-forward (B) | draft_guidance_availability_notice | "Verification Systems Under the Drug Supply Chain Security Act for Certain Prescription Drugs; Draft Guidance for Industry; Availability" | www.federalregister.gov
   Claims: The Food and Drug Administration (FDA or Agency) is announcing the availability of a revised draft guidance entitled "Verification Systems Under the Drug Supply Chain Security Act for Certain Prescription Drugs." This revised draft guidance addresses the verification systems that manufacturers, repa
   Excerpt: The Food and Drug Administration (FDA or Agency) is announcing the availability of a revised draft guidance entitled "Verification Systems Under the Drug Supply Chain Security Act for Certain Prescription Drugs." This revised draft guidance addresses the verification systems that manufacturers, repackagers, wholesale distributors, and dispensers must have in place to comply with the Federal Food, Drug, and Cosmetic Act (FD&C Act), as amended by the Drug Supply Chain Security Act (DSCSA). Specifically, this revised draft guidance covers the statutory verification system requirements that include the quarantine and investigation of a product determined to be suspect and the quarantine and disposition of a product determined to be illegitimate. The revised draft guidance also addresses the statutory requirement for notification to the Agency of a product that has been cleared by a manufacturer, repackager, wholesale distributor, or dispenser (also referred to as "trading partners") after a suspect product investigation because it is determined that the product is not an illegitimate product. Finally, the revised draft guidance addresses the statutory requirement for responding to requ
---
## SNAPSHOT Sacb820461d
CUTOFF DATE (today): 2026-07-26
Regulator: SEBI (IN)
Matter: SEBI consultation: ease-of-doing-business modifications to master circular provisions on exchange traded derivatives
Decisive action for this matter = the regulator's first official publication ADOPTING the proposal at least in substantial part (e.g., board decision press release, circular, or notified regulation).
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2026-05-14 | official-forward (B) | consultation_paper | "Consultation Paper on Measures for ease of doing business on Exchange Traded Derivatives" | www.sebi.gov.in
   Claims: Third in a series of ease-of-doing-business consultation papers reviewing SEBI's exchange-related master circulars. / Seeks comments on modifications to Chapter 5 (Exchange Traded Derivatives) of the Master Circular for Stock Exchanges and Clearing Corporations. / Seeks comments on modifications to multiple Commodity Derivatives Segment master-circular chapters covering product guidelines, price/position limits, participants, options in goods and commodity futures, and commodity-index product design.
   Excerpt: This consultation paper is third part in the series of consultation papers issued for review of the regulatory norms pertaining to Stock exchanges. In terms of the extant modalities for policy formulation, SEBI, inter-alia, prior to issuing a circular under the Acts or regulations generally undertakes public consultation. Accordingly, the objective of this consultation paper is to seek comments/views/suggestions from public on the modifications to Chapter 5 (Exchange Traded Derivatives) of the Master Circular for Stock Exchanges and Clearing Corporations(MSECC) dated December 30, 2024.
---
## SNAPSHOT S0338ee55af
CUTOFF DATE (today): 2023-07-01
Regulator: FDA (US)
Matter: FDA draft guidance: Patient-Focused Drug Development: Selecting, Developing, or Modifying Fit-for-Purpose Clinical Outcome Assessments
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2022-06-30 | official-forward (B) | draft_guidance_availability_notice | "Patient-Focused Drug Development: Selecting, Developing, or Modifying Fit-for-Purpose Clinical Outcome Assessments; Draft Guidance for Industry, Food and Drug Administration Staff, and Other Stakeholders; Availability" | www.federalregister.gov
   Claims: The Food and Drug Administration (FDA or Agency) is announcing the availability of a draft guidance for industry entitled "Patient- Focused Drug Development: Selecting, Developing, or Modifying Fit-for- Purpose Clinical Outcome Assessments." This guidance (Guidance 3) is the third in a series of fou
   Excerpt: The Food and Drug Administration (FDA or Agency) is announcing the availability of a draft guidance for industry entitled "Patient- Focused Drug Development: Selecting, Developing, or Modifying Fit-for- Purpose Clinical Outcome Assessments." This guidance (Guidance 3) is the third in a series of four methodological patient-focused drug development (PFDD) guidance documents that describe how stakeholders (patients, researchers, medical product developers, and others) can collect and submit patient experience data and other relevant information from patients and caregivers to be used for medical product development and regulatory decision-making. When finalized, Guidance 3 will represent the current thinking of the Center for Drug Evaluation and Research, the Center for Biologics Evaluation and Research, and the Center for Devices and Radiological Health on this topic.