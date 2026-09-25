# BLIND POINT-IN-TIME FORECASTING TASK
You are a professional regulatory forecaster. This file contains 10 independent forecasting snapshots about
DIFFERENT regulatory matters. Treat each snapshot on its own; do not carry information between snapshots.

Rules:
1. For each snapshot, "today" is its CUTOFF DATE. Nothing after the cutoff is known. Use only the evidence shown
   plus general knowledge of how that regulator and process usually behave (base rates, typical durations).
2. Do NOT use any specific memory of what happened to this particular matter after the cutoff. If you recognise the
   matter and believe you know its later outcome, still forecast as of the cutoff and set "recognised_outcome": true.
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
## SNAPSHOT S66da90ad71
CUTOFF DATE (today): 2022-12-29
Regulator: SEBI (IN)
Matter: SEBI consultation: accreditation framework for ESG Rating Providers
Decisive action for this matter = the regulator's first official publication ADOPTING the proposal at least in substantial part (e.g., board decision press release, circular, or notified regulation).
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2022-01-24 | official-forward (B) | consultation_paper | "Consultation Paper on Environmental, Social and Governance (ESG) Rating Providers for Securities Markets" | www.sebi.gov.in
   Claims: SEBI proposes to accredit 'ESG Rating Providers' (ERPs) for the purpose of assigning ESG ratings to listed entities and listed securities; a listed entity availing an ESG rating would have to obtain it only from a SEBI-accredited ERP. / Only SEBI-registered Credit Rating Agencies (CRAs) and SEBI-registered Research Analysts (RAs) are proposed as entities eligible to be accredited as ERPs. / A minimum net worth of Rs. 10 crore (in addition to the entity's existing CRA/RA net-worth requirement) is proposed as an accreditation condition. / It is proposed that accredited ERPs be mandated to follow a 'subscriber-pay' business model.
   Excerpt: 3.5.1 ... SEBI proposes to accredit ERPs for the purpose of assigning ESG ratings to listed entities and listed securities. 3.5.2. The proposed scope of accreditation of ERPs is as follows: a. A listed entity who intends to avail an ESG rating, shall obtain the same from only a SEBI Accredited ERP. ... 4.2. Proposed eligible entities: In view of above, SEBI-registered Credit Rating Agencies and SEBI-registered Research Analysts are proposed to be considered eligible to be accredited by SEBI as ERPs, subject to fulfilment of accreditation criteria. ... 5.2. Net worth: ... it is proposed that CRAs/RAs with a minimum net worth of Rs. 10 crores, as per the latest audited financial statements, may be eligible to apply to be a SEBI-accredited ERP. This net worth requirement would be in addition to the applicable minimum net worth requirement for the entity as CRA/RA. ... 11.8. Proposal on Business Model: ... it is proposed that ERPs may be mandated to follow a 'subscriber-pay' business model.
---
## SNAPSHOT Sf2a76932b3
CUTOFF DATE (today): 2024-05-12
Regulator: Housing and Urban Development Department (US)
Matter: Housing and Urban Development Department proposed rule: Affirmatively Furthering Fair Housing
Decisive action for this matter = the agency publishes a FINAL rule or interim final rule adopting this proposal at least in part.
Evidence: none provided for this snapshot.
---
## SNAPSHOT S77a9bc3fdb
CUTOFF DATE (today): 2025-12-12
Regulator: FDA (US)
Matter: FDA draft guidance: Neovascular Age-Related Macular Degeneration: Developing Drugs for Treatment
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2023-02-27 | official-forward (B) | draft_guidance_availability_notice | "Neovascular Age-Related Macular Degeneration: Developing Drugs for Treatment; Draft Guidance for Industry; Availability" | www.federalregister.gov
   Claims: The Food and Drug Administration (FDA or Agency) is announcing the availability of a draft guidance for industry entitled "Neovascular Age-Related Macular Degeneration: Developing Drugs for Treatment." This guidance is intended to provide recommendations to sponsors developing drugs intended to trea
   Excerpt: The Food and Drug Administration (FDA or Agency) is announcing the availability of a draft guidance for industry entitled "Neovascular Age-Related Macular Degeneration: Developing Drugs for Treatment." This guidance is intended to provide recommendations to sponsors developing drugs intended to treat neovascular age-related macular degeneration focusing on eligibility criteria, trial design considerations, and efficacy endpoints to enhance clinical trial data quality and to foster greater efficiency in development programs.
---
## SNAPSHOT S16721203da
CUTOFF DATE (today): 2024-10-17
Regulator: Indian Affairs Bureau (US)
Matter: Indian Affairs Bureau proposed rule: Federal Acknowledgment of American Indian Tribes
Decisive action for this matter = the agency publishes a FINAL rule or interim final rule adopting this proposal at least in part.
Evidence: none provided for this snapshot.
---
## SNAPSHOT S2d030e3b0b
CUTOFF DATE (today): 2023-09-21
Regulator: Alcohol, Tobacco, Firearms, and Explosives Bureau (US)
Matter: Alcohol, Tobacco, Firearms, and Explosives Bureau proposed rule: Annual Reporting of Explosive Materials Storage Facilities to the Local Fire Authority
Decisive action for this matter = the agency publishes a FINAL rule or interim final rule adopting this proposal at least in part.
Evidence: none provided for this snapshot.
---
## SNAPSHOT S0a4b7511a5
CUTOFF DATE (today): 2025-11-02
Regulator: Centers for Medicare & Medicaid Services (US)
Matter: Centers for Medicare & Medicaid Services proposed rule: Medicare and Medicaid Programs; Calendar Year 2026 Home Health Prospective Payment System (HH PPS) Rate Update; Requirements for the HH Quality 
Decisive action for this matter = the agency publishes a FINAL rule or interim final rule adopting this proposal at least in part.
Evidence available as of the cutoff (9 item(s), chronological):
[E1] 2024-12-12 | official-forward (B) | regulatory_agenda_entry | "Unified Agenda (Fall 2024) entry: CY 2026 Home Health Prospective Payment System Rate Update and Home Infusion Therapy Services Payment Update (CMS-1828)" | www.reginfo.gov
   Claims: Stage as of Fall 2024: Proposed Rule Stage. / Priority category as of Fall 2024: Section 3(f)(1) Significant.
   Excerpt: Fall 2024 Unified Agenda entry for RIN 0938-AV53 (Centers for Medicare & Medicaid Services): "CY 2026 Home Health Prospective Payment System Rate Update and Home Infusion Therapy Services Payment Update (CMS-1828)". Stage: Proposed Rule Stage. Priority: Section 3(f)(1) Significant. Timetable as printed in this edition: NPRM: 06/00/2025.
[E2] 2025-04-25 | official-forward (B) | oira_review_received | "OIRA EO 12866 review received: CY 2026 Home Health Prospective Payment System Rate and Durable Medical Equipment, Prosthetics, Orthotics, and Supplies Competitive Bidding Program Updates (CMS-1828)" | www.reginfo.gov
   Claims: OIRA received this rule for EO 12866 review on 2025-04-25.
   Excerpt: OIRA EO 12866 review received 2025-04-25 for RIN 0938-AV53 (Centers for Medicare & Medicaid Services): "CY 2026 Home Health Prospective Payment System Rate and Durable Medical Equipment, Prosthetics, Orthotics, and Supplies Competitive Bidding Program Updates (CMS-1828)". Stage: Proposed Rule. Not economically significant.
[E3] 2025-06-30 | official-forward (B) | oira_review_concluded | "OIRA EO 12866 review concluded: CY 2026 Home Health Prospective Payment System Rate and Durable Medical Equipment, Prosthetics, Orthotics, and Supplies Competitive Bidding Program Updates (CMS-1828)" | www.reginfo.gov
   Claims: OIRA concluded EO 12866 review on 2025-06-30; decision: Consistent with Change.
   Excerpt: OIRA EO 12866 review concluded on 2025-06-30 (received 2025-04-25 for RIN 0938-AV53 (Centers for Medicare & Medicaid Services): "CY 2026 Home Health Prospective Payment System Rate and Durable Medical Equipment, Prosthetics, Orthotics, and Supplies Competitive Bidding Program Updates (CMS-1828)". Stage: Proposed Rule. Not economically significant.). Decision: Consistent with Change.
[E4] 2025-07-02 | official-forward (B) | nprm | "Medicare and Medicaid Programs; Calendar Year 2026 Home Health Prospective Payment System (HH PPS) Rate Update; Requirements for the HH Quality Reporting Program and the HH Value-Based Purchasing Expanded Model; Durable " | www.federalregister.gov
   Claims: This proposed rule would set forth routine updates to the Medicare home health payment rates in accordance with existing statutory and regulatory requirements. / In addition, this proposed rule proposes permanent and temporary behavior adjustments and proposes to recalibrate the case-mix weights and update the functional impairment levels; comorbidity subgroups; and low-utilization payment adjustment (LUPA) thresholds for CY 2026. / Lastly, this proposed rule proposes policy changes to the face-to-face encounter policy. / It also proposes changes to the Home Health Quality Reporting Program (HH QRP) and the expanded Health Value-Based Purchasing (HHVBP) Model requirements.
   Excerpt: This proposed rule would set forth routine updates to the Medicare home health payment rates in accordance with existing statutory and regulatory requirements. In addition, this proposed rule proposes permanent and temporary behavior adjustments and proposes to recalibrate the case-mix weights and update the functional impairment levels; comorbidity subgroups; and low-utilization payment adjustment (LUPA) thresholds for CY 2026. Lastly, this proposed rule proposes policy changes to the face-to-face encounter policy. It also proposes changes to the Home Health Quality Reporting Program (HH QRP) and the expanded Health Value-Based Purchasing (HHVBP) Model requirements. In addition, it would update the Durable Medical Equipment, Prosthetics, Orthotics, and Supplies (DMEPOS) Competitive Bidding Program (CBP). Lastly it proposes: a technical change to the HH conditions of participation; updates to DMEPOS supplier conditions of payment; updates to provider and supplier enrollment requirements; and changes to DMEPOS accreditation requirements. Comment deadline: 2025-08-29. EO 12866 significant: True. Agencies: Health and Human Services Department / Centers for Medicare & Medicaid Services
[E5] 2025-07-09 | official-forward (B) | related_notice | "Medicare and Medicaid Programs; Calendar Year 2026 Home Health Prospective Payment System (HH PPS) Rate Update; Requirements for the HH Quality Reporting Program and the HH Value-Based Purchasing Expanded Model; Durable " | www.federalregister.gov
   Excerpt: (Proposed Rule) — no abstract published for this document.
[E6] 2025-07-11 | official-forward (B) | related_notice | "Medicare and Medicaid Programs; Calendar Year 2026 Home Health Prospective Payment System (HH PPS) Rate Update; Requirements for the HH Quality Reporting Program and the HH Value-Based Purchasing Expanded Model; Durable " | www.federalregister.gov
   Excerpt: (Proposed Rule) — no abstract published for this document.
[E7] 2025-08-28 | official-forward (B) | related_notice | "Medicare and Medicaid Programs; Calendar Year 2026 Home Health Prospective Payment System (HH PPS) Rate Update; Requirements for the HH Quality Reporting Program and the HH Value-Based Purchasing Expanded Model; Durable " | www.federalregister.gov
   Excerpt: (Proposed Rule) — no abstract published for this document.
[E8] 2025-09-22 | official-forward (B) | regulatory_agenda_entry | "Unified Agenda (Spring 2025) entry: CY 2026 Home Health Prospective Payment System Rate and Durable Medical Equipment, Prosthetics, Orthotics, and Supplies Competitive Bidding Program Updates (CMS-1828)" | www.reginfo.gov
   Claims: Stage as of Spring 2025: Proposed Rule Stage. / Priority category as of Spring 2025: Economically Significant.
   Excerpt: Spring 2025 Unified Agenda entry for RIN 0938-AV53 (Centers for Medicare & Medicaid Services): "CY 2026 Home Health Prospective Payment System Rate and Durable Medical Equipment, Prosthetics, Orthotics, and Supplies Competitive Bidding Program Updates (CMS-1828)". Stage: Proposed Rule Stage. Priority: Economically Significant. Timetable as printed in this edition: NPRM: 07/00/2025.
[E9] 2025-10-24 | official-forward (B) | oira_review_received | "OIRA EO 12866 review received: CY 2026 Home Health Prospective Payment System Rate and Durable Medical Equipment, Prosthetics, Orthotics, and Supplies Competitive Bidding Program Updates (CMS-1828)" | www.reginfo.gov
   Claims: OIRA received this rule for EO 12866 review on 2025-10-24.
   Excerpt: OIRA EO 12866 review received 2025-10-24 for RIN 0938-AV53 (Centers for Medicare & Medicaid Services): "CY 2026 Home Health Prospective Payment System Rate and Durable Medical Equipment, Prosthetics, Orthotics, and Supplies Competitive Bidding Program Updates (CMS-1828)". Stage: Final Rule. Not economically significant.
---
## SNAPSHOT S633e2e5e30
CUTOFF DATE (today): 2024-12-06
Regulator: Food and Nutrition Service (US)
Matter: Food and Nutrition Service proposed rule: Provisions To Improve the Supplemental Nutrition Assistance Program's Quality Control System
Decisive action for this matter = the agency publishes a FINAL rule or interim final rule adopting this proposal at least in part.
(Note: 5 earlier regulatory-agenda editions omitted; the 4 most recent are shown.)
Evidence available as of the cutoff (8 item(s), chronological):
[E1] 2023-02-22 | official-forward (B) | regulatory_agenda_entry | "Unified Agenda (Fall 2022) entry: Reform Provisions for the Supplemental Nutrition Assistance Program's Quality Control System" | www.reginfo.gov
   Claims: Stage as of Fall 2022: Proposed Rule Stage. / Priority category as of Fall 2022: Other Significant.
   Excerpt: Fall 2022 Unified Agenda entry for RIN 0584-AE79 (Food and Nutrition Service): "Reform Provisions for the Supplemental Nutrition Assistance Program's Quality Control System". Stage: Proposed Rule Stage. Priority: Other Significant. Timetable as printed in this edition: NPRM: 04/00/2023.
[E2] 2023-05-19 | official-forward (B) | oira_review_received | "OIRA EO 12866 review received: Provisions to Improve the Supplemental Nutrition Assistance Program's Quality Control System" | www.reginfo.gov
   Claims: OIRA received this rule for EO 12866 review on 2023-05-19.
   Excerpt: OIRA EO 12866 review received 2023-05-19 for RIN 0584-AE79 (Food and Nutrition Service): "Provisions to Improve the Supplemental Nutrition Assistance Program's Quality Control System". Stage: Proposed Rule. Not economically significant.
[E3] 2023-07-27 | official-forward (B) | regulatory_agenda_entry | "Unified Agenda (Spring 2023) entry: Provisions to Improve the Supplemental Nutrition Assistance Program's Quality Control System" | www.reginfo.gov
   Claims: Stage as of Spring 2023: Proposed Rule Stage. / Priority category as of Spring 2023: Other Significant.
   Excerpt: Spring 2023 Unified Agenda entry for RIN 0584-AE79 (Food and Nutrition Service): "Provisions to Improve the Supplemental Nutrition Assistance Program's Quality Control System". Stage: Proposed Rule Stage. Priority: Other Significant. Timetable as printed in this edition: NPRM: 06/00/2023.
[E4] 2023-08-25 | official-forward (B) | oira_review_concluded | "OIRA EO 12866 review concluded: Provisions to Improve the Supplemental Nutrition Assistance Program's Quality Control System" | www.reginfo.gov
   Claims: OIRA concluded EO 12866 review on 2023-08-25; decision: Consistent with Change.
   Excerpt: OIRA EO 12866 review concluded on 2023-08-25 (received 2023-05-19 for RIN 0584-AE79 (Food and Nutrition Service): "Provisions to Improve the Supplemental Nutrition Assistance Program's Quality Control System". Stage: Proposed Rule. Not economically significant.). Decision: Consistent with Change.
[E5] 2023-09-19 | official-forward (B) | nprm | "Provisions To Improve the Supplemental Nutrition Assistance Program's Quality Control System" | www.federalregister.gov
   Claims: Department of Agriculture (the Department) is issuing this notice of proposed rulemaking to improve the Food and Nutrition Service's (FNS) Supplemental Nutrition Assistance Program (SNAP) quality control (QC) system as required in the Agriculture Improvement Act of 2018 (2018 Farm Bill). / The proposed changes are intended to strengthen and improve the integrity and accuracy of the SNAP QC system and to better align SNAP with requirements in the Payment Integrity Information Act of 2019 (PIIA). / These changes include a significant adjustment to the SNAP QC system that involves changes to Federal and State agency sampling processes, as well as changes to the active case review process. / Quality Control case sampling and review processes are key aspects of the system used to annually assess SNAP payment error rates.
   Excerpt: The U.S. Department of Agriculture (the Department) is issuing this notice of proposed rulemaking to improve the Food and Nutrition Service's (FNS) Supplemental Nutrition Assistance Program (SNAP) quality control (QC) system as required in the Agriculture Improvement Act of 2018 (2018 Farm Bill). The proposed changes are intended to strengthen and improve the integrity and accuracy of the SNAP QC system and to better align SNAP with requirements in the Payment Integrity Information Act of 2019 (PIIA). These changes include a significant adjustment to the SNAP QC system that involves changes to Federal and State agency sampling processes, as well as changes to the active case review process. Quality Control case sampling and review processes are key aspects of the system used to annually assess SNAP payment error rates. The Department requests comment on this rule's proposed provisions. Comment deadline: 2023-11-20. EO 12866 significant: True. Agencies: Agriculture Department / Food and Nutrition Service.
[E6] 2023-12-19 | official-forward (B) | comment_reopening | "Provisions To Improve the Supplemental Nutrition Assistance Program's Quality Control System" | www.federalregister.gov
   Claims: Department of Agriculture proposed to make changes to the Supplemental Nutrition Assistance Program's Quality Control (SNAP QC) system to strengthen and improve the integrity and accuracy of the system and to better align SNAP QC with requirements in the Payment Integrity Information Act of 2019 (PI / When published, the proposed rule included an incorrect email address for comments; the reopening of the comment period is intended to allow additional time for the public to submit comments in the event the original comment submission was returned as undeliverable due to the incorrect email address
   Excerpt: The U.S. Department of Agriculture proposed to make changes to the Supplemental Nutrition Assistance Program's Quality Control (SNAP QC) system to strengthen and improve the integrity and accuracy of the system and to better align SNAP QC with requirements in the Payment Integrity Information Act of 2019 (PIIA). When published, the proposed rule included an incorrect email address for comments; the reopening of the comment period is intended to allow additional time for the public to submit comments in the event the original comment submission was returned as undeliverable due to the incorrect email address.
[E7] 2024-02-09 | official-forward (B) | regulatory_agenda_entry | "Unified Agenda (Fall 2023) entry: Provisions to Improve the Supplemental Nutrition Assistance Program's Quality Control System" | www.reginfo.gov
   Claims: Stage as of Fall 2023: Proposed Rule Stage. / Priority category as of Fall 2023: Other Significant.
   Excerpt: Fall 2023 Unified Agenda entry for RIN 0584-AE79 (Food and Nutrition Service): "Provisions to Improve the Supplemental Nutrition Assistance Program's Quality Control System". Stage: Proposed Rule Stage. Priority: Other Significant. Timetable as printed in this edition: NPRM: 09/19/2023, 88 FR 64756; NPRM Comment Period End: 11/20/2023.
[E8] 2024-08-16 | official-forward (B) | regulatory_agenda_entry | "Unified Agenda (Spring 2024) entry: Provisions to Improve the Supplemental Nutrition Assistance Program's Quality Control System" | www.reginfo.gov
   Claims: Stage as of Spring 2024: Final Rule Stage. / Priority category as of Spring 2024: Other Significant. / Projected final-action date as printed: 10/00/2024.
   Excerpt: Spring 2024 Unified Agenda entry for RIN 0584-AE79 (Food and Nutrition Service): "Provisions to Improve the Supplemental Nutrition Assistance Program's Quality Control System". Stage: Final Rule Stage. Priority: Other Significant. Timetable as printed in this edition: NPRM: 09/19/2023, 88 FR 64756; NPRM Comment Period End: 11/20/2023; Final Action: 10/00/2024. Projected final-action date as printed: 10/00/2024.
---
## SNAPSHOT Sf402b110c1
CUTOFF DATE (today): 2023-06-06
Regulator: SEBI (IN)
Matter: SEBI consultation: GID/KID disclosure documents and mandatory listing for debt securities issuers
Decisive action for this matter = the regulator's first official publication ADOPTING the proposal at least in substantial part (e.g., board decision press release, circular, or notified regulation).
Evidence: none provided for this snapshot.
---
## SNAPSHOT Sb70d776235
CUTOFF DATE (today): 2023-11-22
Regulator: FDA (US)
Matter: FDA draft guidance: Digital Health Technologies for Remote Data Acquisition in Clinical Investigations
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2021-12-23 | official-forward (B) | draft_guidance_availability_notice | "Digital Health Technologies for Remote Data Acquisition in Clinical Investigations; Draft Guidance for Industry, Investigators, and Other Stakeholders; Availability" | www.federalregister.gov
   Claims: The Food and Drug Administration (FDA or Agency) is announcing the availability of a draft guidance for industry, investigators, and other stakeholders entitled "Digital Health Technologies for Remote Data Acquisition in Clinical Investigations." This guidance provides recommendations to sponsors, i
   Excerpt: The Food and Drug Administration (FDA or Agency) is announcing the availability of a draft guidance for industry, investigators, and other stakeholders entitled "Digital Health Technologies for Remote Data Acquisition in Clinical Investigations." This guidance provides recommendations to sponsors, investigators, and other stakeholders on the use of digital health technologies (DHTs) to acquire data remotely from participants in clinical investigations evaluating medical products. DHTs may take the form of hardware and/or software and may be used to gather health-related information from study participants and transmit that information to study investigators and/or other authorized parties to evaluate the safety and effectiveness of medical products.
---
## SNAPSHOT S00ea2313a9
CUTOFF DATE (today): 2021-04-13
Regulator: State Department (US)
Matter: State Department proposed rule: Visas: Temporary Visitors for Business or Pleasure
Decisive action for this matter = the agency publishes a FINAL rule or interim final rule adopting this proposal at least in part.
Evidence: none provided for this snapshot.