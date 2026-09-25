# BLIND POINT-IN-TIME FORECASTING TASK
You are a professional regulatory forecaster. This file contains 10 independent forecasting snapshots about
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
## SNAPSHOT S2868055f27
CUTOFF DATE (today): 2023-11-27
Regulator: RBI (IN)
Matter: RBI draft: government securities lending and borrowing directions
Decisive action for this matter = the central bank issues FINAL directions/circular adopting the draft at least in substantial part.
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2023-02-17 | official-forward (B) | draft_directions | "RBI releases Draft Reserve Bank of India (Government Securities Lending) Directions, 2023" | www.rbi.org.in
   Claims: In pursuance of the Statement on Developmental and Regulatory Policies dated February 8, 2023, RBI placed draft Government Securities Lending Directions, 2023 on its website. / Proposal permits lending and borrowing of Government securities, expected to augment the existing 'special repo' market and provide investors an avenue to deploy idle securities. / Comments invited by March 17, 2023.
   Excerpt: In pursuance of the announcement made in the Statement on Developmental and Regulatory Policies issued as a part of the Bi-monthly Monetary Policy Statement for 2022-23 dated February 08, 2023 , the Reserve Bank of India has today placed on its website Draft Reserve Bank of India (Government Securities Lending) Directions, 2023 for comments from banks, market participants and other interested parties. A well-functioning market for Securities Lending and Borrowing (SLB) in Government securities (G-Sec) will add depth and liquidity to the G-Sec market, aid efficient price discovery, improve secondary market liquidity for a wider set of securities and facilitate wider participation. The comments on the Draft Directions are invited from banks, market participants and other interested parties by March 17, 2023.
---
## SNAPSHOT Sbca2878bf2
CUTOFF DATE (today): 2024-11-27
Regulator: RBI (IN)
Matter: RBI draft: transparency in aggregation of loan products by digital lending service providers
Decisive action for this matter = the central bank issues FINAL directions/circular adopting the draft at least in substantial part.
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2024-04-26 | official-forward (B) | draft_circular | "RBI invites comments on the Draft Circular on “Digital Lending – Transparency in Aggregation of Loan Products from Multiple Lenders”" | www.rbi.org.in
   Claims: In pursuance of the Statement on Developmental and Regulatory Policies dated December 8, 2023, RBI placed a draft circular on Digital Lending - Transparency in Aggregation of Loan Products from Multiple Lenders. / Addresses issuance of a regulatory framework for aggregation of loan products by Lending Service Providers (LSPs). / Comments invited by May 31, 2024.
   Excerpt: In pursuance of the announcement made in the Statement on Developmental and Regulatory Policies dated December 08, 2023 regarding issuance of a regulatory framework for aggregation of loan products by lending service providers (LSPs), the Reserve Bank of India has today placed on its website the Draft Circular on 'Digital Lending – Transparency in Aggregation of Loan Products from Multiple Lenders'. Comments/feedback, if any, may be sent by e-mail with the subject line "Comments on Draft Circular on Digital Lending – Transparency in Aggregation of Loan Products from Multiple Lenders", by May 31, 2024.
---
## SNAPSHOT S1b90f93f70
CUTOFF DATE (today): 2020-08-21
Regulator: Environmental Protection Agency (US)
Matter: Environmental Protection Agency proposed rule: Reclassification of Major Sources as Area Sources Under Section 112 of the Clean Air Act
Decisive action for this matter = the agency publishes a FINAL rule or interim final rule adopting this proposal at least in part.
Evidence available as of the cutoff (9 item(s), chronological):
[E1] 2018-11-16 | official-forward (B) | regulatory_agenda_entry | "Unified Agenda (Fall 2018) entry: Reclassification of Major Sources as Area Sources Under Section 112 of the Clean Air Act" | www.reginfo.gov
   Claims: Stage as of Fall 2018: Proposed Rule Stage. / Priority category as of Fall 2018: Other Significant.
   Excerpt: Fall 2018 Unified Agenda entry for RIN 2060-AM75 (Office of Air and Radiation): "Reclassification of Major Sources as Area Sources Under Section 112 of the Clean Air Act". Stage: Proposed Rule Stage. Priority: Other Significant. Timetable as printed in this edition: NPRM: 01/03/2007, 72 FR 69; NPRM Comment Period Extended: 03/05/2007, 72 FR 9718; Notice: 02/08/2018, 83 FR 5543; Second NPRM: 02/00/2019.
[E2] 2019-02-25 | official-forward (B) | oira_review_received | "OIRA EO 12866 review received: Reclassification of Major Sources as Area Sources Under Section 112 of the Clean Air Act" | www.reginfo.gov
   Claims: OIRA received this rule for EO 12866 review on 2019-02-25.
   Excerpt: OIRA EO 12866 review received 2019-02-25 for RIN 2060-AM75 (Office of Air and Radiation): "Reclassification of Major Sources as Area Sources Under Section 112 of the Clean Air Act". Stage: Proposed Rule. Economically significant.
[E3] 2019-06-24 | official-forward (B) | regulatory_agenda_entry | "Unified Agenda (Spring 2019) entry: Reclassification of Major Sources as Area Sources Under Section 112 of the Clean Air Act" | www.reginfo.gov
   Claims: Stage as of Spring 2019: Proposed Rule Stage. / Priority category as of Spring 2019: Economically Significant.
   Excerpt: Spring 2019 Unified Agenda entry for RIN 2060-AM75 (Office of Air and Radiation): "Reclassification of Major Sources as Area Sources Under Section 112 of the Clean Air Act". Stage: Proposed Rule Stage. Priority: Economically Significant. Timetable as printed in this edition: NPRM: 01/03/2007, 72 FR 69; Notice: 02/08/2018, 83 FR 5543; Second NPRM: 06/00/2019.
[E4] 2019-06-24 | official-forward (B) | oira_review_concluded | "OIRA EO 12866 review concluded: Reclassification of Major Sources as Area Sources Under Section 112 of the Clean Air Act" | www.reginfo.gov
   Claims: OIRA concluded EO 12866 review on 2019-06-24; decision: Consistent with Change.
   Excerpt: OIRA EO 12866 review concluded on 2019-06-24 (received 2019-02-25 for RIN 2060-AM75 (Office of Air and Radiation): "Reclassification of Major Sources as Area Sources Under Section 112 of the Clean Air Act". Stage: Proposed Rule. Economically significant.). Decision: Consistent with Change.
[E5] 2019-07-26 | official-forward (B) | nprm | "Reclassification of Major Sources as Area Sources Under Section 112 of the Clean Air Act (Notice of Proposed Rulemaking)" | www.federalregister.gov
   Claims: The Environmental Protection Agency (EPA) is proposing amendments to the General Provisions to the National Emission Standards for Hazardous Air Pollutants (NESHAP). / The proposed amendments implement the plain language reading of the "major source" and "area source" definitions of section 112 of the Clean Air Act (CAA) and provide that a major source can reclassify to area source status at any time by limiting its potential to emit (PTE) hazardous air pollutants / The EPA is proposing that PTE HAP limits must meet the proposed effectiveness criteria of being legally and practicably enforceable. / The proposal also clarifies the requirements that apply to sources choosing to reclassify to area source status after the first substantive compliance date of an applicable NESHAP standard.
   Excerpt: The Environmental Protection Agency (EPA) is proposing amendments to the General Provisions to the National Emission Standards for Hazardous Air Pollutants (NESHAP). The proposed amendments implement the plain language reading of the "major source" and "area source" definitions of section 112 of the Clean Air Act (CAA) and provide that a major source can reclassify to area source status at any time by limiting its potential to emit (PTE) hazardous air pollutants (HAP) to below the major source thresholds of 10 tons per year (tpy) of any single HAP or 25 tpy of any combination of HAP. The EPA is proposing that PTE HAP limits must meet the proposed effectiveness criteria of being legally and practicably enforceable. The proposal also clarifies the requirements that apply to sources choosing to reclassify to area source status after the first substantive compliance date of an applicable NESHAP standard. The EPA is proposing electronic notification when a source reclassifies. We are also proposing to revise provisions in specific NESHAP standards that specify the applicability of General Provisions requirements to account for the regulatory provisions we are proposing to add through th
[E6] 2019-07-31 | official-forward (B) | hearing_notice | "Reclassification of Major Sources as Area Sources Under Section 112 of the Clean Air Act (hearing notice)" | www.federalregister.gov
   Claims: On June 25, 2019, the Administrator of the U.S. / Environmental Protection Agency (EPA) signed the proposed rulemaking "Reclassification of Major Sources as Area Sources Under Section 112 of the Clean Air Act." The EPA also requested public comment on the proposed action. / The EPA is announcing that it will hold a public hearing to provide interested parties the opportunity to present data, views, or arguments concerning the proposed action.
   Excerpt: On June 25, 2019, the Administrator of the U.S. Environmental Protection Agency (EPA) signed the proposed rulemaking "Reclassification of Major Sources as Area Sources Under Section 112 of the Clean Air Act." The EPA also requested public comment on the proposed action. The EPA is announcing that it will hold a public hearing to provide interested parties the opportunity to present data, views, or arguments concerning the proposed action.
[E7] 2019-10-02 | official-forward (B) | comment_reopening | "Reclassification of Major Sources as Area Sources Under Section 112 of the Clean Air Act (comment-period reopening notice)" | www.federalregister.gov
   Claims: On July 26, 2019, the Environmental Protection Agency (EPA) proposed a rule titled "Reclassification of Major Sources as Area Sources Under Section 112 of the Clean Air Act." The EPA is reopening the comment period on the proposed rule that closed on September 24, 2019. / The comment period will remain open until November 1, 2019 to allow additional time for stakeholders to review and comment on the proposal.
   Excerpt: On July 26, 2019, the Environmental Protection Agency (EPA) proposed a rule titled "Reclassification of Major Sources as Area Sources Under Section 112 of the Clean Air Act." The EPA is reopening the comment period on the proposed rule that closed on September 24, 2019. The comment period will remain open until November 1, 2019 to allow additional time for stakeholders to review and comment on the proposal.
[E8] 2019-12-26 | official-forward (B) | regulatory_agenda_entry | "Unified Agenda (Fall 2019) entry: Reclassification of Major Sources as Area Sources Under Section 112 of the Clean Air Act" | www.reginfo.gov
   Claims: Stage as of Fall 2019: Proposed Rule Stage. / Priority category as of Fall 2019: Economically Significant. / Projected final-action date as printed: 04/00/2020.
   Excerpt: Fall 2019 Unified Agenda entry for RIN 2060-AM75 (Office of Air and Radiation): "Reclassification of Major Sources as Area Sources Under Section 112 of the Clean Air Act". Stage: Proposed Rule Stage. Priority: Economically Significant. Timetable as printed in this edition: NPRM: 01/03/2007, 72 FR 69; Notice: 02/08/2018, 83 FR 5543; NPRM: 07/26/2019, 84 FR 36304; NPRM Comment Period End: 09/24/2019; NPRM Comment Period Reopened: 10/02/2019, 84 FR 52419; NPRM Comment Period Reopened  End: 11/01/2019; Final Action: 04/00/2020. Projected final-action date as printed: 04/00/2020.
[E9] 2020-07-16 | official-forward (B) | oira_review_received | "OIRA EO 12866 review received: Reclassification of Major Sources as Area Sources Under Section 112 of the Clean Air Act" | www.reginfo.gov
   Claims: OIRA received this rule for EO 12866 review on 2020-07-16.
   Excerpt: OIRA EO 12866 review received 2020-07-16 for RIN 2060-AM75 (Office of Air and Radiation): "Reclassification of Major Sources as Area Sources Under Section 112 of the Clean Air Act". Stage: Final Rule. Economically significant.
---
## SNAPSHOT S7f037bd31d
CUTOFF DATE (today): 2022-12-30
Regulator: IRDAI (IN)
Matter: IRDAI exposure draft: amendment to IRDAI Staff (Officers and Other Employees) regulations
Decisive action for this matter = the regulator notifies FINAL regulations/circular (or formally approves them) adopting the draft at least in substantial part.
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2022-06-23 | official-forward (B) | exposure_draft | "Exposure Draft: Insurance Regulatory and Development Authority of India Staff (Officers and Other Employees) (First Amendment) Regulations, 2022" | irdai.gov.in
   Claims: Taking into account comments received during internal consultation, the exposure draft of the IRDAI Staff (Officers and Other Employees) (First Amendment) Regulations, 2022 was reviewed and reposted as Annexure A. / Stakeholders were asked to submit comments/suggestions on the proposed modifications by 5:00 PM on 15 July 2022.
   Excerpt: EXPOSURE DRAFT INSURANCE REGULATORY AND DEVELOPMENT AUTHORITY OF INDIA STAFF (OFFICERS AND OTHER EMPLOYEES) (FIRST AMENDMENT) REGULATIONS, 2022. 1. Taking into consideration the comments received on the exposure draft of IRDAI Staff (Officers and Other Employees) (First Amendment) Regulations, 2022 during internal consultation, the exposure draft...has been reviewed and is attached as Annexure - A. 2. All the stakeholders are requested to forward their comments / suggestions, if any, on the proposed modifications in the attached format (Annexure- B) on or before 5:00 PM on 15th July, 2022 to hr@irdai.gov.in with cc to sridhar@irdai.gov.in.
---
## SNAPSHOT S4e19a401c3
CUTOFF DATE (today): 2020-10-06
Regulator: FDA (US)
Matter: FDA draft guidance: Development of Locally Applied Corticosteroid Products for the Short-Term Treatment of Symptoms Associated With Internal or External Hemorrhoids
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2019-12-09 | official-forward (B) | draft_guidance_availability_notice | "Development of Locally Applied Corticosteroid Products for the Short-Term Treatment of Symptoms Associated With Internal or External Hemorrhoids; Draft Guidance for Industry; Availability" | www.federalregister.gov
   Claims: The Food and Drug Administration (FDA or Agency) is announcing the availability of a draft guidance for industry entitled "Development of Locally Applied Corticosteroid Products for the Short- Term Treatment of Symptoms Associated with Internal or External Hemorrhoids." This draft guidance will serv
   Excerpt: The Food and Drug Administration (FDA or Agency) is announcing the availability of a draft guidance for industry entitled "Development of Locally Applied Corticosteroid Products for the Short- Term Treatment of Symptoms Associated with Internal or External Hemorrhoids." This draft guidance will serve as a focus for continued discussions among the Division of Gastroenterology and Inborn Error Products, pharmaceutical sponsors, the academic community, and the public.
---
## SNAPSHOT S08025b6036
CUTOFF DATE (today): 2020-11-21
Regulator: Social Security Administration (US)
Matter: Social Security Administration proposed rule: Rules Regarding the Frequency and Notice of Continuing Disability Reviews
Decisive action for this matter = the agency publishes a FINAL rule or interim final rule adopting this proposal at least in part.
(Note: 1 earlier regulatory-agenda editions omitted; the 4 most recent are shown.)
Evidence available as of the cutoff (9 item(s), chronological):
[E1] 2018-11-16 | official-forward (B) | regulatory_agenda_entry | "Unified Agenda (Fall 2018) entry: Rules Regarding the Frequency and Notice of Continuing Disability Reviews" | www.reginfo.gov
   Claims: Stage as of Fall 2018: Proposed Rule Stage. / Priority category as of Fall 2018: Economically Significant.
   Excerpt: Fall 2018 Unified Agenda entry for RIN 0960-AI27 (Social Security Administration): "Rules Regarding the Frequency and Notice of Continuing Disability Reviews". Stage: Proposed Rule Stage. Priority: Economically Significant. Timetable as printed in this edition: NPRM: 12/00/2018.
[E2] 2019-03-13 | official-forward (B) | oira_review_received | "OIRA EO 12866 review received: Rules Regarding the Frequency and Notice of Continuing Disability Reviews" | www.reginfo.gov
   Claims: OIRA received this rule for EO 12866 review on 2019-03-13.
   Excerpt: OIRA EO 12866 review received 2019-03-13 for RIN 0960-AI27 (Social Security Administration): "Rules Regarding the Frequency and Notice of Continuing Disability Reviews". Stage: Proposed Rule. Economically significant.
[E3] 2019-06-24 | official-forward (B) | regulatory_agenda_entry | "Unified Agenda (Spring 2019) entry: Rules Regarding the Frequency and Notice of Continuing Disability Reviews" | www.reginfo.gov
   Claims: Stage as of Spring 2019: Proposed Rule Stage. / Priority category as of Spring 2019: Economically Significant.
   Excerpt: Spring 2019 Unified Agenda entry for RIN 0960-AI27 (Social Security Administration): "Rules Regarding the Frequency and Notice of Continuing Disability Reviews". Stage: Proposed Rule Stage. Priority: Economically Significant. Timetable as printed in this edition: NPRM: 06/00/2019.
[E4] 2019-11-07 | official-forward (B) | oira_review_concluded | "OIRA EO 12866 review concluded: Rules Regarding the Frequency and Notice of Continuing Disability Reviews" | www.reginfo.gov
   Claims: OIRA concluded EO 12866 review on 2019-11-07; decision: Consistent with Change.
   Excerpt: OIRA EO 12866 review concluded on 2019-11-07 (received 2019-03-13 for RIN 0960-AI27 (Social Security Administration): "Rules Regarding the Frequency and Notice of Continuing Disability Reviews". Stage: Proposed Rule. Economically significant.). Decision: Consistent with Change.
[E5] 2019-11-18 | official-forward (B) | nprm | "Rules Regarding the Frequency and Notice of Continuing Disability Reviews" | www.federalregister.gov
   Claims: We propose to revise our regulations regarding when and how often we conduct continuing disability reviews (CDR), which are periodic reviews of eligibility required for benefit continuation. / The proposed rules would add a category to the existing medical diary categories that we use to schedule CDRs and revise the criteria for assigning each of the medical diary categories to cases. / The proposed rules would also change the frequency with which we perform a CDR for claims with the medical diary category for permanent impairments. / The revised changes would ensure that we continue to maintain appropriate stewardship of the disability program and identify medical improvement (MI) at its earliest point.
   Excerpt: We propose to revise our regulations regarding when and how often we conduct continuing disability reviews (CDR), which are periodic reviews of eligibility required for benefit continuation. The proposed rules would add a category to the existing medical diary categories that we use to schedule CDRs and revise the criteria for assigning each of the medical diary categories to cases. The proposed rules would also change the frequency with which we perform a CDR for claims with the medical diary category for permanent impairments. The revised changes would ensure that we continue to maintain appropriate stewardship of the disability program and identify medical improvement (MI) at its earliest point. Comment deadline: 2020-01-17. EO 12866 significant: True. Agencies: Social Security Administration.
[E6] 2019-12-10 | official-forward (B) | comment_extension | "Rules Regarding the Frequency and Notice of Continuing Disability Reviews; Extension of Comment Period" | www.federalregister.gov
   Claims: On November 18, 2019, we published the proposed rule Rules Regarding the Frequency and Notice of Continuing Disability Reviews in the Federal Register, and solicited public comments. / We provided a 60- day comment period ending January 17, 2020. / We are extending the comment period for 15 days.
   Excerpt: On November 18, 2019, we published the proposed rule Rules Regarding the Frequency and Notice of Continuing Disability Reviews in the Federal Register, and solicited public comments. We provided a 60- day comment period ending January 17, 2020. We are extending the comment period for 15 days.
[E7] 2019-12-26 | official-forward (B) | regulatory_agenda_entry | "Unified Agenda (Fall 2019) entry: Rules Regarding the Frequency and Notice of Continuing Disability Reviews" | www.reginfo.gov
   Claims: Stage as of Fall 2019: Proposed Rule Stage. / Priority category as of Fall 2019: Economically Significant.
   Excerpt: Fall 2019 Unified Agenda entry for RIN 0960-AI27 (Social Security Administration): "Rules Regarding the Frequency and Notice of Continuing Disability Reviews". Stage: Proposed Rule Stage. Priority: Economically Significant. Timetable as printed in this edition: NPRM: 11/00/2019.
[E8] 2020-08-26 | official-forward (B) | regulatory_agenda_entry | "Unified Agenda (Spring 2020) entry: Rules Regarding the Frequency and Notice of Continuing Disability Reviews" | www.reginfo.gov
   Claims: Stage as of Spring 2020: Final Rule Stage. / Priority category as of Spring 2020: Economically Significant. / Projected final-action date as printed: 10/00/2020.
   Excerpt: Spring 2020 Unified Agenda entry for RIN 0960-AI27 (Social Security Administration): "Rules Regarding the Frequency and Notice of Continuing Disability Reviews". Stage: Final Rule Stage. Priority: Economically Significant. Timetable as printed in this edition: NPRM: 11/18/2019, 84 FR 63588; NPRM Comment Period Extended: 12/10/2019, 84 FR 67394; NPRM Comment Period End: 01/17/2020; NPRM Comment Period Extended End: 01/31/2020; Final Action: 10/00/2020. Projected final-action date as printed: 10/00/2020.
[E9] 2020-11-10 | official-forward (B) | oira_review_received | "OIRA EO 12866 review received: Rules Regarding the Frequency and Notice of Continuing Disability Reviews" | www.reginfo.gov
   Claims: OIRA received this rule for EO 12866 review on 2020-11-10.
   Excerpt: OIRA EO 12866 review received 2020-11-10 for RIN 0960-AI27 (Social Security Administration): "Rules Regarding the Frequency and Notice of Continuing Disability Reviews". Stage: Final Rule. Economically significant.
---
## SNAPSHOT S32e9b5423f
CUTOFF DATE (today): 2023-09-23
Regulator: TRAI (IN)
Matter: TRAI consultation: licensing regime for aircraft-to-ground-station data communication services
Decisive action for this matter = the regulator RELEASES its recommendations (or final regulation/order) on this consultation.
Evidence available as of the cutoff (2 item(s), chronological):
[E1] 2022-12-10 | official-forward (B) | consultation_paper | "Consultation Paper on Data Communication Services Between Aircraft and Ground Stations Provided by Organizations Other Than Airports Authority of India (CP No. 14/2022)" | www.trai.gov.in
   Claims: TRAI asked whether there is a need to bring data communication services between aircraft and ground stations (by organisations other than Airports Authority of India) under a service-licensing regime. / TRAI asked, if licensing is needed, whether providers should be licensed via an authorisation under the Unified Licence or via a separate service licence. / TRAI noted the current Wireless Operational Licence (WOL) for such services is issued for one year per location and does not renew automatically, unlike the much longer validity periods (e.g. 20 years for Unified Licence) of other telecom licences.
   Excerpt: Q1. Whether there is a need to bring data communication services between aircraft and ground stations provided by organizations other than Airport Authority of India under service licensing regime? Kindly provide a detailed response with justification. Q2. In case your answer to Q1 is in the affirmative, should the providers of data communication services between aircraft and ground stations be licensed through -- (a) an authorization under Unified License; or (b) a separate service license. Kindly provide a detailed response with justification. J. Specifications of the license. 2.30 Currently, WOL is issued to the providers of data communication services between aircraft and ground stations for a period of one year at each location. The renewal of the WOL is not done automatically. It needs to be obtained every year through a similar process for each station.
[E2] 2023-01-09 | official-forward (B) | comment_deadline_extension_notice | "Extension of last date to receive comments/counter comments on TRAI's Consultation Paper on Data Communication Services Between Aircraft and Ground Stations" | www.trai.gov.in
   Claims: TRAI issued a press note on 9 January 2023 restating/extending the comment deadline for the aircraft-ground-station data communication consultation paper.
   Excerpt: New Delhi, 9th January 2023 - The Telecom Regulatory Authority of India (TRAI) had released a Consultation Paper on 'Data Communication Services Between Aircraft and Ground Stations Provided by Organizations Other Than Airports Authority of India' on 10.12.2022. The last date for receiving written comments on the issues raised in the Consultation Paper from stakeholders was fixed as 09.01.2023 and for counter comments as 23.01.2023.
---
## SNAPSHOT S1f32eb4129
CUTOFF DATE (today): 2022-04-16
Regulator: FDA (US)
Matter: FDA draft guidance: Instructions for Use-Patient Labeling for Human Prescription Drug and Biological Products and Drug-Device and Biologic-Device Combination Products-Content and Format
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2019-07-02 | official-forward (B) | draft_guidance_availability_notice | "Instructions for Use-Patient Labeling for Human Prescription Drug and Biological Products and Drug-Device and Biologic-Device Combination Products-Content and Format; Draft Guidance for Industry; Availability" | www.federalregister.gov
   Claims: The Food and Drug Administration (FDA or Agency) is announcing the availability of a draft guidance for industry entitled "Instructions for Use--Patient Labeling for Human Prescription Drug and Biological Products and Drug-Device and Biologic-Device Combination Products--Content and Format." This dr
   Excerpt: The Food and Drug Administration (FDA or Agency) is announcing the availability of a draft guidance for industry entitled "Instructions for Use--Patient Labeling for Human Prescription Drug and Biological Products and Drug-Device and Biologic-Device Combination Products--Content and Format." This draft guidance provides recommendations for developing the content and format of an Instructions for Use (IFU) document for human prescription drugs and biological products and drug-device or biologic-device combination products submitted under a new drug application (NDA) or a biologics license application (BLA). The IFU is developed by applicants for patients who use drug products that have complicated or detailed patient-use instructions. The recommendations in this draft guidance are intended to help develop consistent content and format across IFUs and to help ensure that patients receive clear, concise information that is easily understood for the safe and effective use of prescription drug products.
---
## SNAPSHOT S826be67853
CUTOFF DATE (today): 2023-05-31
Regulator: IRDAI (IN)
Matter: IRDAI exposure draft: remuneration of non-executive directors and whole-time directors of insurers
Decisive action for this matter = the regulator notifies FINAL regulations/circular (or formally approves them) adopting the draft at least in substantial part.
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2022-01-03 | official-forward (B) | exposure_draft | "Exposure Draft: Guidelines on Remuneration of Non-Executive Directors and Managing Director/Chief Executive Officer/Whole-time Directors of Insurance companies" | irdai.gov.in
   Claims: The draft proposes to replace the 2016 circular on remuneration of NEDs and MD/CEO/WTDs of insurers, citing five years of experience and a need to avoid compensation structures that reward excessive risk-taking. / For Non-Executive Directors, fixed remuneration (beyond sitting fees) is capped at Rs 20 lakh per annum per director (excluding Chairman), with NEDs ineligible for ESOPs without Authority approval. / For Whole-time Directors/CEOs/MDs, variable pay must be at least 50% of total remuneration (max 300% of fixed pay), with 50% of variable pay deferred over three years (no deferment if variable pay is under Rs 15 lakh) and subject to malus/clawback. / Tenure limits for MD&CEO and WTDs are proposed to be aligned with RBI's stipulations for bank directors.
   Excerpt: Exposure Draft. Guidelines on Remuneration of Non-Executive Directors and Managing Director/Chief Executive Officer/Whole-time Directors of Insurance companies. In order to ensure sound remuneration or compensation practices and avoid situations resulting from excessive risk taking behavior due to inappropriate compensation structures... it is proposed to replace the extant guidelines... issued vide circular ref IRDA/F&A/GDL/LSTD/155/08/2016 dated 05.08.2016. ...For Non-Executive Directors (NEDs): remuneration...shall not exceed Rs. Twenty lakh per annum for each such director excluding Chairman... NEDs shall not be eligible for ESOPs. ...For Whole Time Directors/Chief Executive/Managing Directors: at least 50% of the remuneration subject to maximum 300% of the fixed pay... Minimum of 50% of the variable pay must be deferred... over a period of three years.
---
## SNAPSHOT Sbaa90ee596
CUTOFF DATE (today): 2022-09-21
Regulator: SEBI (IN)
Matter: SEBI consultation: streamlining open offer and buyback tender-offer timelines
Decisive action for this matter = the regulator's first official publication ADOPTING the proposal at least in substantial part (e.g., board decision press release, circular, or notified regulation).
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2022-03-25 | official-forward (B) | consultation_paper | "Streamlining the Timelines followed in Open Offers and Buyback Tender Offers" | www.sebi.gov.in
   Claims: SEBI proposed reducing the overall time for completion of an Open Offer under the Takeover Regulations, 2011 from 62 working days to 42 working days. / SEBI proposed reducing the overall time for completion of a Buyback tender offer under the Buy-back Regulations, 2018 from 43 working days to 36 working days. / Specific proposed changes included shortening the period to publish the Detailed Public Statement (T+5 to T+3) and to submit the Draft Letter of Offer to SEBI (T+10 to T+5). / The Primary Market Advisory Committee (PMAC) had agreed to the proposals, and the Association of Investment Bankers of India (AIBI) welcomed the review.
   Excerpt: 1. The objective of this paper is to seek comments / views from various stakeholders including market intermediaries and the public on procedure followed with respect to the timelines of various activities involved in Open Offers and Buy-back offers... 2. The proposed changes in the timelines of procedural activities would help reduce the overall time taken for completion of Open Offer from 62 working days to 42 working days and overall time for completion of Buyback from 43 working days to 36 working days, which would be investor-friendly and make the process more efficient. ... 6. Primary Market Advisory Committee ('PMAC') agreed to the proposals... 7. AIBI welcomed the proposal regarding review of the timelines of various procedural activities in open offers and buyback tender offers.