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
## SNAPSHOT S4819c07048
CUTOFF DATE (today): 2026-02-10
Regulator: FDA (US)
Matter: FDA draft guidance: Neovascular Age-Related Macular Degeneration: Developing Drugs for Treatment
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence: none provided for this snapshot.
---
## SNAPSHOT S211e364257
CUTOFF DATE (today): 2022-12-29
Regulator: SEBI (IN)
Matter: SEBI consultation: accreditation framework for ESG Rating Providers
Decisive action for this matter = the regulator's first official publication ADOPTING the proposal at least in substantial part (e.g., board decision press release, circular, or notified regulation).
Evidence: none provided for this snapshot.
---
## SNAPSHOT S8a7213df7e
CUTOFF DATE (today): 2024-10-17
Regulator: Indian Affairs Bureau (US)
Matter: Indian Affairs Bureau proposed rule: Federal Acknowledgment of American Indian Tribes
Decisive action for this matter = the agency publishes a FINAL rule or interim final rule adopting this proposal at least in part.
(Note: 2 earlier regulatory-agenda editions omitted; the 4 most recent are shown.)
Evidence available as of the cutoff (10 item(s), chronological):
[E1] 2022-01-10 | official-forward (B) | oira_review_received | "OIRA EO 12866 review received: Procedures for Federal Acknowledgment of Indian Tribes" | www.reginfo.gov
   Claims: OIRA received this rule for EO 12866 review on 2022-01-10.
   Excerpt: OIRA EO 12866 review received 2022-01-10 for RIN 1076-AF67 (Bureau of Indian Affairs): "Procedures for Federal Acknowledgment of Indian Tribes". Stage: Proposed Rule. Not economically significant.
[E2] 2022-04-06 | official-forward (B) | oira_review_concluded | "OIRA EO 12866 review concluded: Procedures for Federal Acknowledgment of Indian Tribes" | www.reginfo.gov
   Claims: OIRA concluded EO 12866 review on 2022-04-06; decision: Consistent with Change.
   Excerpt: OIRA EO 12866 review concluded on 2022-04-06 (received 2022-01-10 for RIN 1076-AF67 (Bureau of Indian Affairs): "Procedures for Federal Acknowledgment of Indian Tribes". Stage: Proposed Rule. Not economically significant.). Decision: Consistent with Change.
[E3] 2022-04-27 | official-forward (B) | nprm | "Federal Acknowledgment of American Indian Tribes (Notice of Proposed Rulemaking)" | www.federalregister.gov
   Claims: This proposed rule seeks input on continuation of an express prohibition on re-petitioning under the U.S. / Department of the Interior's (Department) regulations for Federal acknowledgment of Indian Tribes. / When first promulgated in 1978, the acknowledgment regulations did not provide a regulatory path that allowed re- petitioning, and since 1994, the regulations have expressly prohibited petitioners who have received a negative final determination from the Department from re-petitioning (ban). / The most recent update to the regulations in 2015 continued this ban, but two Federal district courts held that the Department's stated reasons for implementing the ban, as articulated in the 2015 completed regulatory action updating the regulations (2015 completed regulatory action), were arbitrary
   Excerpt: This proposed rule seeks input on continuation of an express prohibition on re-petitioning under the U.S. Department of the Interior's (Department) regulations for Federal acknowledgment of Indian Tribes. When first promulgated in 1978, the acknowledgment regulations did not provide a regulatory path that allowed re- petitioning, and since 1994, the regulations have expressly prohibited petitioners who have received a negative final determination from the Department from re-petitioning (ban). The most recent update to the regulations in 2015 continued this ban, but two Federal district courts held that the Department's stated reasons for implementing the ban, as articulated in the 2015 completed regulatory action updating the regulations (2015 completed regulatory action), were arbitrary and capricious, and remanded to the Department for further consideration. The Department has undertaken further consideration and is proposing to maintain the ban, albeit with revised justifications, in light of the Federal district courts' orders. The Department seeks input on this proposal and the basis for its proposal. Comment deadline: 2022-07-06. EO 12866 significant: True. Agencies: Interior
[E4] 2023-02-22 | official-forward (B) | regulatory_agenda_entry | "Unified Agenda (Fall 2022) entry: Procedures for Federal Acknowledgment of Indian Tribes" | www.reginfo.gov
   Claims: Stage as of Fall 2022: Final Rule Stage. / Priority category as of Fall 2022: Other Significant. / Projected final-action date as printed: 12/00/2022.
   Excerpt: Fall 2022 Unified Agenda entry for RIN 1076-AF67 (Bureau of Indian Affairs): "Procedures for Federal Acknowledgment of Indian Tribes". Stage: Final Rule Stage. Priority: Other Significant. Timetable as printed in this edition: NPRM: 04/27/2022, 87 FR 24908; NPRM Comment Period End: 07/06/2022; Final Action: 12/00/2022. Projected final-action date as printed: 12/00/2022.
[E5] 2023-07-27 | official-forward (B) | regulatory_agenda_entry | "Unified Agenda (Spring 2023) entry: Procedures for Federal Acknowledgment of Indian Tribes" | www.reginfo.gov
   Claims: Stage as of Spring 2023: Final Rule Stage. / Priority category as of Spring 2023: Other Significant. / Projected final-action date as printed: 07/00/2023.
   Excerpt: Spring 2023 Unified Agenda entry for RIN 1076-AF67 (Bureau of Indian Affairs): "Procedures for Federal Acknowledgment of Indian Tribes". Stage: Final Rule Stage. Priority: Other Significant. Timetable as printed in this edition: NPRM: 04/27/2022, 87 FR 24908; NPRM Comment Period End: 07/06/2022; Final Action: 07/00/2023. Projected final-action date as printed: 07/00/2023.
[E6] 2023-10-31 | official-forward (B) | oira_review_received | "OIRA EO 12866 review received: Procedures for Federal Acknowledgment of Indian Tribes" | www.reginfo.gov
   Claims: OIRA received this rule for EO 12866 review on 2023-10-31.
   Excerpt: OIRA EO 12866 review received 2023-10-31 for RIN 1076-AF67 (Bureau of Indian Affairs): "Procedures for Federal Acknowledgment of Indian Tribes". Stage: Proposed Rule. Not economically significant.
[E7] 2024-02-09 | official-forward (B) | regulatory_agenda_entry | "Unified Agenda (Fall 2023) entry: Procedures for Federal Acknowledgment of Indian Tribes" | www.reginfo.gov
   Claims: Stage as of Fall 2023: Proposed Rule Stage. / Priority category as of Fall 2023: Other Significant.
   Excerpt: Fall 2023 Unified Agenda entry for RIN 1076-AF67 (Bureau of Indian Affairs): "Procedures for Federal Acknowledgment of Indian Tribes". Stage: Proposed Rule Stage. Priority: Other Significant. Timetable as printed in this edition: NPRM: 04/27/2022, 87 FR 24908; NPRM Comment Period End: 07/06/2022; Second NPRM: 02/00/2024.
[E8] 2024-05-22 | official-forward (B) | oira_review_concluded | "OIRA EO 12866 review concluded: Procedures for Federal Acknowledgment of Indian Tribes" | www.reginfo.gov
   Claims: OIRA concluded EO 12866 review on 2024-05-22; decision: Consistent with Change.
   Excerpt: OIRA EO 12866 review concluded on 2024-05-22 (received 2023-10-31 for RIN 1076-AF67 (Bureau of Indian Affairs): "Procedures for Federal Acknowledgment of Indian Tribes". Stage: Proposed Rule. Not economically significant.). Decision: Consistent with Change.
[E9] 2024-07-12 | official-forward (B) | related_notice | "Federal Acknowledgment of American Indian Tribes (proposed-stage document)" | www.federalregister.gov
   Claims: The United States Department of the Interior (Department) seeks input on a proposal to create a conditional, time-limited opportunity for denied petitioners to re-petition for Federal acknowledgment as an Indian Tribe.
   Excerpt: The United States Department of the Interior (Department) seeks input on a proposal to create a conditional, time-limited opportunity for denied petitioners to re-petition for Federal acknowledgment as an Indian Tribe.
[E10] 2024-08-16 | official-forward (B) | regulatory_agenda_entry | "Unified Agenda (Spring 2024) entry: Procedures for Federal Acknowledgment of Indian Tribes" | www.reginfo.gov
   Claims: Stage as of Spring 2024: Proposed Rule Stage. / Priority category as of Spring 2024: Other Significant.
   Excerpt: Spring 2024 Unified Agenda entry for RIN 1076-AF67 (Bureau of Indian Affairs): "Procedures for Federal Acknowledgment of Indian Tribes". Stage: Proposed Rule Stage. Priority: Other Significant. Timetable as printed in this edition: NPRM: 04/27/2022, 87 FR 24908; NPRM Comment Period End: 07/06/2022; Second NPRM: 07/00/2024.
---
## SNAPSHOT S7edcbc40fc
CUTOFF DATE (today): 2023-04-07
Regulator: SEBI (IN)
Matter: SEBI consultation: GID/KID disclosure documents and mandatory listing for debt securities issuers
Decisive action for this matter = the regulator's first official publication ADOPTING the proposal at least in substantial part (e.g., board decision press release, circular, or notified regulation).
Evidence: none provided for this snapshot.
---
## SNAPSHOT Sc8fca1bbf7
CUTOFF DATE (today): 2025-09-03
Regulator: Centers for Medicare & Medicaid Services (US)
Matter: Centers for Medicare & Medicaid Services proposed rule: Medicare and Medicaid Programs; Calendar Year 2026 Home Health Prospective Payment System (HH PPS) Rate Update; Requirements for the HH Quality 
Decisive action for this matter = the agency publishes a FINAL rule or interim final rule adopting this proposal at least in part.
Evidence: none provided for this snapshot.
---
## SNAPSHOT S8b8ca39bf2
CUTOFF DATE (today): 2023-09-23
Regulator: FDA (US)
Matter: FDA draft guidance: Digital Health Technologies for Remote Data Acquisition in Clinical Investigations
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2021-12-23 | official-forward (B) | draft_guidance_availability_notice | "Digital Health Technologies for Remote Data Acquisition in Clinical Investigations; Draft Guidance for Industry, Investigators, and Other Stakeholders; Availability" | www.federalregister.gov
   Claims: The Food and Drug Administration (FDA or Agency) is announcing the availability of a draft guidance for industry, investigators, and other stakeholders entitled "Digital Health Technologies for Remote Data Acquisition in Clinical Investigations." This guidance provides recommendations to sponsors, i
   Excerpt: The Food and Drug Administration (FDA or Agency) is announcing the availability of a draft guidance for industry, investigators, and other stakeholders entitled "Digital Health Technologies for Remote Data Acquisition in Clinical Investigations." This guidance provides recommendations to sponsors, investigators, and other stakeholders on the use of digital health technologies (DHTs) to acquire data remotely from participants in clinical investigations evaluating medical products. DHTs may take the form of hardware and/or software and may be used to gather health-related information from study participants and transmit that information to study investigators and/or other authorized parties to evaluate the safety and effectiveness of medical products.
---
## SNAPSHOT S62217a823f
CUTOFF DATE (today): 2024-12-06
Regulator: Food and Nutrition Service (US)
Matter: Food and Nutrition Service proposed rule: Provisions To Improve the Supplemental Nutrition Assistance Program's Quality Control System
Decisive action for this matter = the agency publishes a FINAL rule or interim final rule adopting this proposal at least in part.
Evidence: none provided for this snapshot.
---
## SNAPSHOT S1e268d26e2
CUTOFF DATE (today): 2023-09-21
Regulator: Alcohol, Tobacco, Firearms, and Explosives Bureau (US)
Matter: Alcohol, Tobacco, Firearms, and Explosives Bureau proposed rule: Annual Reporting of Explosive Materials Storage Facilities to the Local Fire Authority
Decisive action for this matter = the agency publishes a FINAL rule or interim final rule adopting this proposal at least in part.
(Note: 7 earlier regulatory-agenda editions omitted; the 4 most recent are shown.)
Evidence available as of the cutoff (5 item(s), chronological):
[E1] 2022-01-31 | official-forward (B) | regulatory_agenda_entry | "Unified Agenda (Fall 2021) entry: Annual Reporting of Explosive Materials Storage Facilities to the Local Fire Authority" | www.reginfo.gov
   Claims: Stage as of Fall 2021: Proposed Rule Stage. / Priority category as of Fall 2021: Other Significant.
   Excerpt: Fall 2021 Unified Agenda entry for RIN 1140-AA51 (Bureau of Alcohol, Tobacco, Firearms, and Explosives): "Annual Reporting of Explosive Materials Storage Facilities to the Local Fire Authority". Stage: Proposed Rule Stage. Priority: Other Significant. Timetable as printed in this edition: NPRM: 11/00/2021.
[E2] 2022-08-08 | official-forward (B) | regulatory_agenda_entry | "Unified Agenda (Spring 2022) entry: Annual Reporting of Explosive Materials Storage Facilities to the Local Fire Authority" | www.reginfo.gov
   Claims: Stage as of Spring 2022: Proposed Rule Stage. / Priority category as of Spring 2022: Other Significant.
   Excerpt: Spring 2022 Unified Agenda entry for RIN 1140-AA51 (Bureau of Alcohol, Tobacco, Firearms, and Explosives): "Annual Reporting of Explosive Materials Storage Facilities to the Local Fire Authority". Stage: Proposed Rule Stage. Priority: Other Significant. Timetable as printed in this edition: NPRM: 11/00/2022.
[E3] 2023-02-22 | official-forward (B) | regulatory_agenda_entry | "Unified Agenda (Fall 2022) entry: Annual Reporting of Explosive Materials Storage Facilities to the Local Fire Authority" | www.reginfo.gov
   Claims: Stage as of Fall 2022: Proposed Rule Stage. / Priority category as of Fall 2022: Other Significant.
   Excerpt: Fall 2022 Unified Agenda entry for RIN 1140-AA51 (Bureau of Alcohol, Tobacco, Firearms, and Explosives): "Annual Reporting of Explosive Materials Storage Facilities to the Local Fire Authority". Stage: Proposed Rule Stage. Priority: Other Significant. Timetable as printed in this edition: NPRM: 01/00/2023.
[E4] 2023-07-27 | official-forward (B) | regulatory_agenda_entry | "Unified Agenda (Spring 2023) entry: Annual Reporting of Explosive Materials Storage Facilities to the Local Fire Authority" | www.reginfo.gov
   Claims: Stage as of Spring 2023: Proposed Rule Stage. / Priority category as of Spring 2023: Other Significant.
   Excerpt: Spring 2023 Unified Agenda entry for RIN 1140-AA51 (Bureau of Alcohol, Tobacco, Firearms, and Explosives): "Annual Reporting of Explosive Materials Storage Facilities to the Local Fire Authority". Stage: Proposed Rule Stage. Priority: Other Significant. Timetable as printed in this edition: NPRM: 08/00/2023.
[E5] 2023-08-23 | official-forward (B) | nprm | "Annual Reporting of Explosive Materials Storage Facilities to the Local Fire Authority" | www.federalregister.gov
   Claims: The Department of Justice is proposing to amend Bureau of Alcohol, Tobacco, Firearms, and Explosives ("ATF") regulations to require that any person who stores explosive materials notify on an annual basis the authority having jurisdiction for fire safety in the locality in which the explosive materi / In addition, the proposed rule requires any person who stores explosive materials to notify the authority having jurisdiction for fire safety in the locality in which the explosive materials were stored whenever storage is discontinued. / These changes are intended to increase public safety.
   Excerpt: The Department of Justice is proposing to amend Bureau of Alcohol, Tobacco, Firearms, and Explosives ("ATF") regulations to require that any person who stores explosive materials notify on an annual basis the authority having jurisdiction for fire safety in the locality in which the explosive materials are being stored of the type of explosives, magazine capacity, and location of each site where such materials are stored. In addition, the proposed rule requires any person who stores explosive materials to notify the authority having jurisdiction for fire safety in the locality in which the explosive materials were stored whenever storage is discontinued. These changes are intended to increase public safety. Comment deadline: 2023-11-21. EO 12866 significant: True. Agencies: Justice Department / Alcohol, Tobacco, Firearms, and Explosives Bureau.
---
## SNAPSHOT S6ddae3e997
CUTOFF DATE (today): 2021-06-12
Regulator: State Department (US)
Matter: State Department proposed rule: Visas: Temporary Visitors for Business or Pleasure
Decisive action for this matter = the agency publishes a FINAL rule or interim final rule adopting this proposal at least in part.
Evidence available as of the cutoff (6 item(s), chronological):
[E1] 2019-10-07 | official-forward (B) | oira_review_received | "OIRA EO 12866 review received: Visas: Temporary Visitors for Business or Pleasure" | www.reginfo.gov
   Claims: OIRA received this rule for EO 12866 review on 2019-10-07.
   Excerpt: OIRA EO 12866 review received 2019-10-07 for RIN 1400-AE95 (Department of State): "Visas: Temporary Visitors for Business or Pleasure". Stage: Proposed Rule. Economically significant.
[E2] 2019-12-26 | official-forward (B) | regulatory_agenda_entry | "Unified Agenda (Fall 2019) entry: Visas: Temporary Visitors for Business or Pleasure" | www.reginfo.gov
   Claims: Stage as of Fall 2019: Proposed Rule Stage. / Priority category as of Fall 2019: Other Significant.
   Excerpt: Fall 2019 Unified Agenda entry for RIN 1400-AE95 (Department of State): "Visas: Temporary Visitors for Business or Pleasure". Stage: Proposed Rule Stage. Priority: Other Significant. Timetable as printed in this edition: NPRM: 12/00/2019.
[E3] 2020-08-26 | official-forward (B) | regulatory_agenda_entry | "Unified Agenda (Spring 2020) entry: Visas: Temporary Visitors for Business or Pleasure" | www.reginfo.gov
   Claims: Stage as of Spring 2020: Proposed Rule Stage. / Priority category as of Spring 2020: Other Significant.
   Excerpt: Spring 2020 Unified Agenda entry for RIN 1400-AE95 (Department of State): "Visas: Temporary Visitors for Business or Pleasure". Stage: Proposed Rule Stage. Priority: Other Significant. Timetable as printed in this edition: NPRM: 06/00/2020.
[E4] 2020-09-22 | official-forward (B) | oira_review_concluded | "OIRA EO 12866 review concluded: Visas: Temporary Visitors for Business or Pleasure" | www.reginfo.gov
   Claims: OIRA concluded EO 12866 review on 2020-09-22; decision: Consistent with Change.
   Excerpt: OIRA EO 12866 review concluded on 2020-09-22 (received 2019-10-07 for RIN 1400-AE95 (Department of State): "Visas: Temporary Visitors for Business or Pleasure". Stage: Proposed Rule. Economically significant.). Decision: Consistent with Change.
[E5] 2020-10-21 | official-forward (B) | nprm | "Visas: Temporary Visitors for Business or Pleasure" | www.federalregister.gov
   Claims: The Department of State ("Department") proposes to amend its regulation governing nonimmigrant visas for temporary visitors for business, the B-1 nonimmigrant visa classification, by removing two sentences defining the term "business" that are outdated due to changes in the INA since 1952, from when / With removal of these sentences, the Department would no longer authorize issuance of B-1 visas for certain aliens classifiable as H-1B or H-3 nonimmigrants, commonly referred to as the "B-1 in lieu of H" policy, unless the alien independently qualifies for a B-1 visa for a reason other than the B-1
   Excerpt: The Department of State ("Department") proposes to amend its regulation governing nonimmigrant visas for temporary visitors for business, the B-1 nonimmigrant visa classification, by removing two sentences defining the term "business" that are outdated due to changes in the INA since 1952, from when the two sentences originate. With removal of these sentences, the Department would no longer authorize issuance of B-1 visas for certain aliens classifiable as H-1B or H-3 nonimmigrants, commonly referred to as the "B-1 in lieu of H" policy, unless the alien independently qualifies for a B-1 visa for a reason other than the B-1 in lieu of H policy. Comment deadline: 2020-12-21. EO 12866 significant: True. Agencies: State Department.
[E6] 2021-03-31 | official-forward (B) | regulatory_agenda_entry | "Unified Agenda (Fall 2020) entry: Visas: Temporary Visitors for Business or Pleasure" | www.reginfo.gov
   Claims: Stage as of Fall 2020: Proposed Rule Stage. / Priority category as of Fall 2020: Economically Significant. / Projected final-action date as printed: 06/00/2021.
   Excerpt: Fall 2020 Unified Agenda entry for RIN 1400-AE95 (Department of State): "Visas: Temporary Visitors for Business or Pleasure". Stage: Proposed Rule Stage. Priority: Economically Significant. Timetable as printed in this edition: NPRM: 10/21/2020, 85 FR 66878; NPRM Comment Period End: 12/21/2020; Final Rule: 06/00/2021. Projected final-action date as printed: 06/00/2021.
---
## SNAPSHOT Sba86f348c7
CUTOFF DATE (today): 2024-03-13
Regulator: Housing and Urban Development Department (US)
Matter: Housing and Urban Development Department proposed rule: Affirmatively Furthering Fair Housing
Decisive action for this matter = the agency publishes a FINAL rule or interim final rule adopting this proposal at least in part.
Evidence: none provided for this snapshot.