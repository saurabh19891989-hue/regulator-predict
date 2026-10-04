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
## SNAPSHOT Sbbdae78ffd
CUTOFF DATE (today): 2021-09-28
Regulator: FDA (US)
Matter: FDA draft guidance: Biomarkers and Surrogate Endpoints in Clinical Studies To Support Effectiveness of New Animal Drugs
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence: none provided for this snapshot.
---
## SNAPSHOT S495c59ca1e
CUTOFF DATE (today): 2022-12-31
Regulator: FDA (US)
Matter: FDA draft guidance: Chronic Rhinosinusitis With Nasal Polyps: Developing Drugs for Treatment
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2021-12-10 | official-forward (B) | draft_guidance_availability_notice | "Chronic Rhinosinusitis With Nasal Polyps: Developing Drugs for Treatment; Draft Guidance for Industry; Availability" | www.federalregister.gov
   Claims: The Food and Drug Administration (FDA or Agency) is announcing the availability of a draft guidance for industry entitled "Chronic Rhinosinusitis with Nasal Polyps: Developing Drugs for Treatment." The purpose of this draft guidance is to assist sponsors in the clinical development of drugs for the 
   Excerpt: The Food and Drug Administration (FDA or Agency) is announcing the availability of a draft guidance for industry entitled "Chronic Rhinosinusitis with Nasal Polyps: Developing Drugs for Treatment." The purpose of this draft guidance is to assist sponsors in the clinical development of drugs for the treatment of chronic rhinosinusitis with nasal polyps (CRSwNP). Specifically, this draft guidance addresses FDA's current recommendations regarding trial design, safety, and efficacy considerations for CRSwNP clinical trials.
---
## SNAPSHOT S77eef1197d
CUTOFF DATE (today): 2024-11-03
Regulator: FDA (US)
Matter: FDA draft guidance: Marketing Submission Recommendations for a Predetermined Change Control Plan for Artificial Intelligence/Machine Learning-Enabled Device Software Functions
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence: none provided for this snapshot.
---
## SNAPSHOT Sdb0622f8de
CUTOFF DATE (today): 2022-10-12
Regulator: FDA (US)
Matter: FDA draft guidance: Donor Eligibility for Animal Cells, Tissues, and Cell- and Tissue-Based Products
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2021-09-23 | official-forward (B) | draft_guidance_availability_notice | "Donor Eligibility for Animal Cells, Tissues, and Cell- and Tissue-Based Products; Draft Guidance for Industry; Availability" | www.federalregister.gov
   Claims: The Food and Drug Administration (FDA or Agency or we) is announcing the availability of a draft guidance for industry #254 entitled "Donor Eligibility for Animal Cells, Tissues, and Cell- and Tissue-Based Products." FDA's Center for Veterinary Medicine (CVM) is issuing this guidance for sponsors, f
   Excerpt: The Food and Drug Administration (FDA or Agency or we) is announcing the availability of a draft guidance for industry #254 entitled "Donor Eligibility for Animal Cells, Tissues, and Cell- and Tissue-Based Products." FDA's Center for Veterinary Medicine (CVM) is issuing this guidance for sponsors, firms, individuals, and establishments that participate in the manufacture of, or perform any aspect of, the donor eligibility determination for animal cells, tissues, and cell- and tissue-based products (ACTPs), which meet the definition of new animal drugs under the Federal Food, Drug, and Cosmetic Act (FD&C Act). Donor eligibility is a critical component of current good manufacturing practices (CGMPs) when manufacturing ACTPs. A donor should be considered eligible to donate ACTPs only if screening of the donor shows that the donor is free from risk factors for, and clinical evidence of, infection with relevant disease agents and diseases, and the donor (and product/source material) test results for relevant disease agents are negative or nonreactive.
---
## SNAPSHOT S8d616ea7c2
CUTOFF DATE (today): 2023-11-29
Regulator: FDA (US)
Matter: FDA draft guidance: Verification Systems Under the Drug Supply Chain Security Act for Certain Prescription Drugs
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2022-03-10 | official-forward (B) | draft_guidance_availability_notice | "Verification Systems Under the Drug Supply Chain Security Act for Certain Prescription Drugs; Draft Guidance for Industry; Availability" | www.federalregister.gov
   Claims: The Food and Drug Administration (FDA or Agency) is announcing the availability of a revised draft guidance entitled "Verification Systems Under the Drug Supply Chain Security Act for Certain Prescription Drugs." This revised draft guidance addresses the verification systems that manufacturers, repa
   Excerpt: The Food and Drug Administration (FDA or Agency) is announcing the availability of a revised draft guidance entitled "Verification Systems Under the Drug Supply Chain Security Act for Certain Prescription Drugs." This revised draft guidance addresses the verification systems that manufacturers, repackagers, wholesale distributors, and dispensers must have in place to comply with the Federal Food, Drug, and Cosmetic Act (FD&C Act), as amended by the Drug Supply Chain Security Act (DSCSA). Specifically, this revised draft guidance covers the statutory verification system requirements that include the quarantine and investigation of a product determined to be suspect and the quarantine and disposition of a product determined to be illegitimate. The revised draft guidance also addresses the statutory requirement for notification to the Agency of a product that has been cleared by a manufacturer, repackager, wholesale distributor, or dispenser (also referred to as "trading partners") after a suspect product investigation because it is determined that the product is not an illegitimate product. Finally, the revised draft guidance addresses the statutory requirement for responding to requ
---
## SNAPSHOT S177f6616e7
CUTOFF DATE (today): 2023-02-08
Regulator: FDA (US)
Matter: FDA draft guidance: Evaluation of Gastric pH-Dependent Drug Interactions With Acid-Reducing Agents: Study Design, Data Analysis, and Clinical Implications
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence: none provided for this snapshot.
---
## SNAPSHOT Seed85f9625
CUTOFF DATE (today): 2025-05-21
Regulator: FDA (US)
Matter: FDA draft guidance: Patient-Focused Drug Development: Selecting, Developing, or Modifying Fit-for-Purpose Clinical Outcome Assessments
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2022-06-30 | official-forward (B) | draft_guidance_availability_notice | "Patient-Focused Drug Development: Selecting, Developing, or Modifying Fit-for-Purpose Clinical Outcome Assessments; Draft Guidance for Industry, Food and Drug Administration Staff, and Other Stakeholders; Availability" | www.federalregister.gov
   Claims: The Food and Drug Administration (FDA or Agency) is announcing the availability of a draft guidance for industry entitled "Patient- Focused Drug Development: Selecting, Developing, or Modifying Fit-for- Purpose Clinical Outcome Assessments." This guidance (Guidance 3) is the third in a series of fou
   Excerpt: The Food and Drug Administration (FDA or Agency) is announcing the availability of a draft guidance for industry entitled "Patient- Focused Drug Development: Selecting, Developing, or Modifying Fit-for- Purpose Clinical Outcome Assessments." This guidance (Guidance 3) is the third in a series of four methodological patient-focused drug development (PFDD) guidance documents that describe how stakeholders (patients, researchers, medical product developers, and others) can collect and submit patient experience data and other relevant information from patients and caregivers to be used for medical product development and regulatory decision-making. When finalized, Guidance 3 will represent the current thinking of the Center for Drug Evaluation and Research, the Center for Biologics Evaluation and Research, and the Center for Devices and Radiological Health on this topic.
---
## SNAPSHOT Saf5c25bd75
CUTOFF DATE (today): 2020-07-04
Regulator: FDA (US)
Matter: FDA draft guidance: Development of Locally Applied Corticosteroid Products for the Short-Term Treatment of Symptoms Associated With Internal or External Hemorrhoids
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence: none provided for this snapshot.
---
## SNAPSHOT S1584bdc279
CUTOFF DATE (today): 2021-03-25
Regulator: FDA (US)
Matter: FDA draft guidance: Premenopausal Women With Breast Cancer: Developing Drugs for Treatment
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence: none provided for this snapshot.
---
## SNAPSHOT S93360e1a8a
CUTOFF DATE (today): 2024-04-20
Regulator: FDA (US)
Matter: FDA draft guidance: Review of Drug Master Files in Advance of Certain Abbreviated New Drug Application Submissions Under Generic Drug User Fee Amendments
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2022-10-06 | official-forward (B) | draft_guidance_availability_notice | "Review of Drug Master Files in Advance of Certain Abbreviated New Drug Application Submissions Under Generic Drug User Fee Amendments; Draft Guidance for Industry; Availability" | www.federalregister.gov
   Claims: The Food and Drug Administration (FDA or Agency) is announcing the availability of a draft guidance for industry entitled "Review of Drug Master Files in Advance of Certain ANDA Submissions Under GDUFA." The purpose of this draft guidance is to provide information and recommendations on the Generic 
   Excerpt: The Food and Drug Administration (FDA or Agency) is announcing the availability of a draft guidance for industry entitled "Review of Drug Master Files in Advance of Certain ANDA Submissions Under GDUFA." The purpose of this draft guidance is to provide information and recommendations on the Generic Drug User Fee Amendments (GDUFA) III program enhancements agreed upon by the Agency and industry in "GDUFA Reauthorization Performance Goals and Program Enhancements Fiscal Years 2023-2027" (GDUFA III commitment letter), related to the early assessment of certain Type II drug master files (DMFs) 6 months prior to the submission of certain abbreviated new drug applications (ANDAs) or prior approval supplements (PASs). This draft guidance describes the process outlined in the GDUFA III commitment letter in greater detail and provides recommendations to DMF holders on how to provide the relevant information to FDA.
---
## SNAPSHOT S7130e0fc73
CUTOFF DATE (today): 2026-06-14
Regulator: SEBI (IN)
Matter: SEBI consultation: reviewing the pre-open call auction price-discovery mechanism for IPO listings and re-listed scrips
Decisive action for this matter = the regulator's first official publication ADOPTING the proposal at least in substantial part (e.g., board decision press release, circular, or notified regulation).
Evidence: none provided for this snapshot.
---
## SNAPSHOT S8961cc6a72
CUTOFF DATE (today): 2026-05-20
Regulator: SEBI (IN)
Matter: SEBI consultation: recognizing intraday borrowing facilities as a cash-management tool for mutual funds
Decisive action for this matter = the regulator's first official publication ADOPTING the proposal at least in substantial part (e.g., board decision press release, circular, or notified regulation).
Evidence: none provided for this snapshot.
---
## SNAPSHOT S49d627f13d
CUTOFF DATE (today): 2026-06-12
Regulator: SEBI (IN)
Matter: SEBI consultation: 'Green-Channel' document-acknowledgement mechanism for launch of Alternative Investment Fund schemes
Decisive action for this matter = the regulator's first official publication ADOPTING the proposal at least in substantial part (e.g., board decision press release, circular, or notified regulation).
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2026-05-11 | official-forward (B) | consultation_paper | "Consultation on 'Green-Channel: AIF Rollout Upon Document Acknowledgement' (GARUDA) Mechanism for Processing of Placement Memorandum of Alternative Investment Funds (AIFs) filed with SEBI" | www.sebi.gov.in
   Claims: Proposes amending AIF Regulations, 2012 to reduce the scheme-launch timeline for 'Regular' (non-accredited, non-angel) AIF schemes to 10 working days. / Proposes exempting AI-only schemes and Angel Funds from filing the Private Placement Memorandum (PPM) through a Merchant Banker, allowing launch immediately on grant of SEBI registration or PPM filing. / Describes this as 'Phase 2' of an ease-of-doing-business initiative, following an April 30, 2026 Phase-1 circular that let AIFs begin soliciting funds 30 days after filing an application, subject to post-facto sample-based SEBI scrutiny. / States the objective is to further ease AIF scheme-launch procedures given the sophistication of AIF investors and the due-diligence role already played by Merchant Bankers.
   Excerpt: SEBI has recently reviewed the procedure for processing Private Placement Memorandums (PPMs) of AIFs for launch of schemes/funds... Recently, as an Ease of Doing Business Measure, a Fast-Track Mechanism has been adopted for launch of schemes (other than LVFs) by AIFs... SEBI, vide circular dated April 30, 2026, inter alia clarified that AIFs may now proceed with the launch of their Regular schemes, AI only schemes & Angel Funds and begin soliciting funds from investors 30 days after filing their application with SEBI. The purpose of this consultation paper is to further ease the process of scheme launch by AIFs (Phase 2) through amendment to relevant provisions in SEBI (AIF) Regulations, 2012.
---
## SNAPSHOT S228c9d4787
CUTOFF DATE (today): 2026-03-28
Regulator: SEBI (IN)
Matter: SEBI consultation: proposed amendments to the certification regime for associated persons in the securities markets
Decisive action for this matter = the regulator's first official publication ADOPTING the proposal at least in substantial part (e.g., board decision press release, circular, or notified regulation).
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2025-11-06 | official-forward (B) | consultation_paper | "Consultation paper on Amendments to SEBI (Certification of Associated Persons in the Securities Markets) Regulations, 2007" | www.sebi.gov.in
   Claims: Proposes reviewing/expanding the definition of 'Associated Persons' under CAPSM Regulations, 2007. / Proposes changes to the manner of obtaining the NISM certificate required under the regulations. / Proposes allowing an electronic mode of participation for Continuing Professional Education (CPE) programs. / Proposes reviewing the exception criteria governing the manner of obtaining the certificate (e.g. age/experience-based exemptions).
   Excerpt: To solicit comments / views / suggestions from the public and other stakeholders on the proposed amendments to 'SEBI (Certification of Associated Persons in the Securities Markets) Regulations, 2007 ("CAPSM Regulations")'. The following proposals are being made: 1.1.1 Review / Expansion of the definition of 'Associated Persons' 1.1.2 Manner of obtaining certificate 1.1.3 Inclusion of electronic mode of participation for Continuing Professional Education (CPE) programs 1.1.4 Reviewing the exception criteria for manner of obtaining certificate.
---
## SNAPSHOT S050cf105b3
CUTOFF DATE (today): 2023-12-14
Regulator: FDA (US)
Matter: FDA draft guidance: Digital Health Technologies for Remote Data Acquisition in Clinical Investigations
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2021-12-23 | official-forward (B) | draft_guidance_availability_notice | "Digital Health Technologies for Remote Data Acquisition in Clinical Investigations; Draft Guidance for Industry, Investigators, and Other Stakeholders; Availability" | www.federalregister.gov
   Claims: The Food and Drug Administration (FDA or Agency) is announcing the availability of a draft guidance for industry, investigators, and other stakeholders entitled "Digital Health Technologies for Remote Data Acquisition in Clinical Investigations." This guidance provides recommendations to sponsors, i
   Excerpt: The Food and Drug Administration (FDA or Agency) is announcing the availability of a draft guidance for industry, investigators, and other stakeholders entitled "Digital Health Technologies for Remote Data Acquisition in Clinical Investigations." This guidance provides recommendations to sponsors, investigators, and other stakeholders on the use of digital health technologies (DHTs) to acquire data remotely from participants in clinical investigations evaluating medical products. DHTs may take the form of hardware and/or software and may be used to gather health-related information from study participants and transmit that information to study investigators and/or other authorized parties to evaluate the safety and effectiveness of medical products.
---
## SNAPSHOT Sb7be08707b
CUTOFF DATE (today): 2021-07-29
Regulator: FDA (US)
Matter: FDA draft guidance: Principles for Selecting, Developing, Modifying, and Adapting Patient-Reported Outcome Instruments for Use in Medical Device Evaluation
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2020-08-31 | official-forward (B) | draft_guidance_availability_notice | "Principles for Selecting, Developing, Modifying, and Adapting Patient-Reported Outcome Instruments for Use in Medical Device Evaluation; Draft Guidance for Industry, Food and Drug Administration Staff, and Other Stakehol" | www.federalregister.gov
   Claims: The Food and Drug Administration (FDA or Agency) is announcing the availability of the draft guidance entitled "Principles for Selecting, Developing, Modifying, and Adapting Patient-Reported Outcome Instruments for Use in Medical Device Evaluation." The FDA encourages the collection, analysis, and i
   Excerpt: The Food and Drug Administration (FDA or Agency) is announcing the availability of the draft guidance entitled "Principles for Selecting, Developing, Modifying, and Adapting Patient-Reported Outcome Instruments for Use in Medical Device Evaluation." The FDA encourages the collection, analysis, and integration of patient perspectives in the development, evaluation, and surveillance of medical devices, including digital health technologies. Patient-reported outcome (PRO) instruments facilitate the systematic collection of patient perspectives as scientific evidence to support the regulatory and healthcare decision-making process. This draft guidance describes principles that should be considered when using PRO instruments in the evaluation of medical devices and provides recommendations about the importance of ensuring the measures are "fit-for-purpose." This draft guidance is not final nor is it in effect at this time.
---
## SNAPSHOT Sf38f68ae4a
CUTOFF DATE (today): 2022-10-15
Regulator: FDA (US)
Matter: FDA draft guidance: Peripheral Percutaneous Transluminal Angioplasty and Specialty Catheters-Premarket Notification (510(k)) Submissions
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2020-01-13 | official-forward (B) | draft_guidance_availability_notice | "Peripheral Percutaneous Transluminal Angioplasty and Specialty Catheters-Premarket Notification (510(k)) Submissions; Draft Guidance for Industry and Food and Drug Administration Staff; Availability" | www.federalregister.gov
   Claims: The Food and Drug Administration (FDA or Agency) is announcing the availability of the draft guidance entitled "Peripheral Percutaneous Transluminal Angioplasty (PTA) and Specialty Catheters-- Premarket Notification (510(k)) Submissions; Draft Guidance for Industry and Food and Drug Administration S
   Excerpt: The Food and Drug Administration (FDA or Agency) is announcing the availability of the draft guidance entitled "Peripheral Percutaneous Transluminal Angioplasty (PTA) and Specialty Catheters-- Premarket Notification (510(k)) Submissions; Draft Guidance for Industry and Food and Drug Administration Staff." The FDA is issuing this draft guidance document to provide recommendations for 510(k) submissions for peripheral percutaneous transluminal angioplasty (PTA) balloons and specialty catheters (e.g., infusion catheters, PTA balloon catheters for in-stent restenosis (ISR), scoring/cutting balloons). This draft guidance is not final nor is it in effect at this time.
---
## SNAPSHOT Sd2c171fc04
CUTOFF DATE (today): 2025-11-15
Regulator: FDA (US)
Matter: FDA draft guidance: Sponsor Responsibilities-Safety Reporting Requirements and Safety Assessment for Investigational New Drug Application and Bioavailability/Bioequivalence Studies
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2021-06-28 | official-forward (B) | draft_guidance_availability_notice | "Sponsor Responsibilities-Safety Reporting Requirements and Safety Assessment for Investigational New Drug Application and Bioavailability/Bioequivalence Studies; Draft Guidance for Industry; Availability" | www.federalregister.gov
   Claims: The Food and Drug Administration (FDA or Agency) is announcing the availability of a draft guidance for industry entitled "Sponsor Responsibilities--Safety Reporting Requirements and Safety Assessment for Investigational New Drug Application and Bioavailability/ Bioequivalence Studies." The draft gu
   Excerpt: The Food and Drug Administration (FDA or Agency) is announcing the availability of a draft guidance for industry entitled "Sponsor Responsibilities--Safety Reporting Requirements and Safety Assessment for Investigational New Drug Application and Bioavailability/ Bioequivalence Studies." The draft guidance provides recommendations for sponsors and sponsor-investigators to comply with the requirements of investigational new drug application (IND) safety reporting and safety reporting for bioavailability (BA) and bioequivalence (BE) studies. In doing so, the guidance provides recommendations related to the two IND safety reporting provisions that require assessment of aggregate data to facilitate appropriate IND safety reporting practices. An earlier draft guidance for industry entitled "Safety Assessment for IND Safety Reporting" (December 2015) (the 2015 draft guidance) has been incorporated into this draft guidance. However, this content was revised to address feedback from stakeholders and comments received on the 2015 draft guidance. Concurrent with the publication of this draft guidance, we are withdrawing the 2015 draft guidance. Additionally, this draft guidance incorporates c
---
## SNAPSHOT S079a1a2a03
CUTOFF DATE (today): 2026-06-12
Regulator: SEBI (IN)
Matter: SEBI consultation: amendments to the Issue and Listing of Securitised Debt Instruments and Security Receipts Regulations
Decisive action for this matter = the regulator's first official publication ADOPTING the proposal at least in substantial part (e.g., board decision press release, circular, or notified regulation).
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2026-05-04 | official-forward (B) | consultation_paper | "Consultation paper on amendments to the SEBI (Issue and Listing of Securitised Debt Instruments and Security Receipts) Regulations, 2008" | www.sebi.gov.in
   Claims: Proposes amendments to the SEBI (Issue and Listing of Securitised Debt Instruments and Security Receipts) Regulations, 2008 to align with RBI's securitisation framework. / Proposes exempting RBI-regulated entities (e.g., banks, NBFCs) from the existing 25% single-obligor concentration limit for single-asset securitisation transactions, aligning with RBI norms that already permit this for such entities. / Proposes additional disclosure of concentration risk arising from single-asset securitisation in the offer document, to inform investors given the changed concentration limit.
   Excerpt: CONSULTATION PAPER, DEPARTMENT OF DEBT AND HYBRID SECURITIES, Consultation paper on amendments to the SEBI (Issue and Listing of Securitised Debt Instruments and Security Receipts) Regulations, 2008, May 04, 2026. [Timeline to Respond: Comments on the Consultation paper may be sent by May 25, 2026]
---
## SNAPSHOT S8258f82119
CUTOFF DATE (today): 2026-08-19
Regulator: SEBI (IN)
Matter: SEBI consultation: phased introduction of physical settlement in select agricultural commodity derivatives contracts
Decisive action for this matter = the regulator's first official publication ADOPTING the proposal at least in substantial part (e.g., board decision press release, circular, or notified regulation).
Evidence: none provided for this snapshot.