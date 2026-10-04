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
## SNAPSHOT Se272b0792d
CUTOFF DATE (today): 2021-12-26
Regulator: FDA (US)
Matter: FDA draft guidance: Principles for Selecting, Developing, Modifying, and Adapting Patient-Reported Outcome Instruments for Use in Medical Device Evaluation
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2020-08-31 | official-forward (B) | draft_guidance_availability_notice | "Principles for Selecting, Developing, Modifying, and Adapting Patient-Reported Outcome Instruments for Use in Medical Device Evaluation; Draft Guidance for Industry, Food and Drug Administration Staff, and Other Stakehol" | www.federalregister.gov
   Claims: The Food and Drug Administration (FDA or Agency) is announcing the availability of the draft guidance entitled "Principles for Selecting, Developing, Modifying, and Adapting Patient-Reported Outcome Instruments for Use in Medical Device Evaluation." The FDA encourages the collection, analysis, and i
   Excerpt: The Food and Drug Administration (FDA or Agency) is announcing the availability of the draft guidance entitled "Principles for Selecting, Developing, Modifying, and Adapting Patient-Reported Outcome Instruments for Use in Medical Device Evaluation." The FDA encourages the collection, analysis, and integration of patient perspectives in the development, evaluation, and surveillance of medical devices, including digital health technologies. Patient-reported outcome (PRO) instruments facilitate the systematic collection of patient perspectives as scientific evidence to support the regulatory and healthcare decision-making process. This draft guidance describes principles that should be considered when using PRO instruments in the evaluation of medical devices and provides recommendations about the importance of ensuring the measures are "fit-for-purpose." This draft guidance is not final nor is it in effect at this time.
---
## SNAPSHOT Sb91d276853
CUTOFF DATE (today): 2025-09-16
Regulator: FDA (US)
Matter: FDA draft guidance: Sponsor Responsibilities-Safety Reporting Requirements and Safety Assessment for Investigational New Drug Application and Bioavailability/Bioequivalence Studies
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence: none provided for this snapshot.
---
## SNAPSHOT S535506cc30
CUTOFF DATE (today): 2022-10-12
Regulator: FDA (US)
Matter: FDA draft guidance: Donor Eligibility for Animal Cells, Tissues, and Cell- and Tissue-Based Products
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence: none provided for this snapshot.
---
## SNAPSHOT S7a08fa0fcf
CUTOFF DATE (today): 2020-10-02
Regulator: FDA (US)
Matter: FDA draft guidance: Development of Locally Applied Corticosteroid Products for the Short-Term Treatment of Symptoms Associated With Internal or External Hemorrhoids
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2019-12-06 | official-forward (B) | draft_guidance_availability_notice | "Development of Locally Applied Corticosteroid Products for the Short-Term Treatment of Symptoms Associated With Internal or External Hemorrhoids; Draft Guidance for Industry; Availability" | www.federalregister.gov
   Claims: The Food and Drug Administration (FDA or Agency) is announcing the availability of a draft guidance for industry entitled "Development of Locally Applied Corticosteroid Products for the Short- Term Treatment of Symptoms Associated with Internal or External Hemorrhoids." This draft guidance will serv
   Excerpt: The Food and Drug Administration (FDA or Agency) is announcing the availability of a draft guidance for industry entitled "Development of Locally Applied Corticosteroid Products for the Short- Term Treatment of Symptoms Associated with Internal or External Hemorrhoids." This draft guidance will serve as a focus for continued discussions among the Division of Gastroenterology and Inborn Error Products, pharmaceutical sponsors, the academic community, and the public.
---
## SNAPSHOT Sea64372682
CUTOFF DATE (today): 2026-02-10
Regulator: FDA (US)
Matter: FDA draft guidance: Neovascular Age-Related Macular Degeneration: Developing Drugs for Treatment
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2023-02-27 | official-forward (B) | draft_guidance_availability_notice | "Neovascular Age-Related Macular Degeneration: Developing Drugs for Treatment; Draft Guidance for Industry; Availability" | www.federalregister.gov
   Claims: The Food and Drug Administration (FDA or Agency) is announcing the availability of a draft guidance for industry entitled "Neovascular Age-Related Macular Degeneration: Developing Drugs for Treatment." This guidance is intended to provide recommendations to sponsors developing drugs intended to trea
   Excerpt: The Food and Drug Administration (FDA or Agency) is announcing the availability of a draft guidance for industry entitled "Neovascular Age-Related Macular Degeneration: Developing Drugs for Treatment." This guidance is intended to provide recommendations to sponsors developing drugs intended to treat neovascular age-related macular degeneration focusing on eligibility criteria, trial design considerations, and efficacy endpoints to enhance clinical trial data quality and to foster greater efficiency in development programs.
---
## SNAPSHOT Saedf121836
CUTOFF DATE (today): 2026-02-13
Regulator: SEBI (IN)
Matter: SEBI consultation: reviewing use of historical price scenarios in stress testing for the Commodity Derivatives Segment
Decisive action for this matter = the regulator's first official publication ADOPTING the proposal at least in substantial part (e.g., board decision press release, circular, or notified regulation).
Evidence: none provided for this snapshot.
---
## SNAPSHOT S591534befb
CUTOFF DATE (today): 2026-07-22
Regulator: SEBI (IN)
Matter: SEBI consultation: draft circular on trading software/technology at stock exchanges and common IT provisions for market infrastructure institutions
Decisive action for this matter = the regulator's first official publication ADOPTING the proposal at least in substantial part (e.g., board decision press release, circular, or notified regulation).
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2026-06-22 | official-forward (B) | consultation_paper | "Consultation Paper on Draft Circular for Trading Software & Technology at Stock Exchanges and Draft Circular on Common IT related provisions for MIIs" | www.sebi.gov.in
   Claims: Proposes a draft circular modifying trading-software-and-technology provisions of the Master Circular for Stock Exchanges & Clearing Corporations and the Master Circular for Commodity Derivatives. / Proposes a separate draft consolidated circular on common IT-related provisions for market infrastructure institutions (MIIs), amending the Master Circular for Depositories. / Frames the exercise as implementing the FY2023-24 budget announcement to simplify and reduce compliance cost via public consultation before issuing circulars. / Identifies this as a further paper in the same series that already included CPs on Administration of Exchanges (Oct 8, 2025) and Trading at Exchanges (Jan 9, 2026).
   Excerpt: In order to align the process of review of Master Circulars with the budget announcement, SEBI, inter-alia, prior to issuing a circular under the Acts or regulations, generally, undertakes public consultation. Therefore, in compliance with the mandate and procedure envisaged in the aforesaid budget announcement, towards facilitating ease of doing business/compliance for stock exchanges, following Consultation Papers (CPs) have been issued: CP on Measures for ease of doing business on Administration of Exchanges... has been put up for public comments on October 08, 2025. CP on Measures for ease of doing business on Trading at Exchanges... has been put up for public comments on January 09, 2026.
---
## SNAPSHOT S6943785a7c
CUTOFF DATE (today): 2026-05-24
Regulator: FDA (US)
Matter: FDA draft guidance: International Cooperation on Harmonisation of Technical Requirements for Registration of Veterinary Medicinal Products; Effectiveness of Anthelmintics: Specific Recommendations ...
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2022-08-11 | official-forward (B) | draft_guidance_availability_notice | "International Cooperation on Harmonisation of Technical Requirements for Registration of Veterinary Medicinal Products; Effectiveness of Anthelmintics: Specific Recommendations for Caprines (Revision 1); Draft Guidance f" | www.federalregister.gov
   Claims: The Food and Drug Administration (FDA or Agency) is announcing the availability of a draft guidance for industry GFI #97 (VICH GL14(R1)) entitled "Effectiveness of Anthelmintics: Specific Recommendations for Caprines (Revision 1)." This draft guidance has been developed for veterinary use by the Int
   Excerpt: The Food and Drug Administration (FDA or Agency) is announcing the availability of a draft guidance for industry GFI #97 (VICH GL14(R1)) entitled "Effectiveness of Anthelmintics: Specific Recommendations for Caprines (Revision 1)." This draft guidance has been developed for veterinary use by the International Cooperation on Harmonisation of Technical Requirements for Registration of Veterinary Medicinal Products (VICH). This revision clarifies the definition of adequate infection in individual animals, updates considerations for field studies, and makes additional clarifying changes.
---
## SNAPSHOT Sb9ade2b2e5
CUTOFF DATE (today): 2022-07-19
Regulator: FDA (US)
Matter: FDA draft guidance: General Clinical Pharmacology Considerations for Neonatal Studies for Drugs and Biological Products
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2019-08-01 | official-forward (B) | draft_guidance_availability_notice | "General Clinical Pharmacology Considerations for Neonatal Studies for Drugs and Biological Products; Draft Guidance for Industry; Availability" | www.federalregister.gov
   Claims: The Food and Drug Administration (FDA or Agency) is announcing the availability of a draft guidance for industry entitled "General Clinical Pharmacology Considerations for Neonatal Studies for Drugs and Biological Products." This draft guidance is intended to assist sponsors of new drug applications
   Excerpt: The Food and Drug Administration (FDA or Agency) is announcing the availability of a draft guidance for industry entitled "General Clinical Pharmacology Considerations for Neonatal Studies for Drugs and Biological Products." This draft guidance is intended to assist sponsors of new drug applications (NDAs), biologics license applications (BLAs) for therapeutic biologics, and supplements who are planning to conduct clinical studies in neonatal populations. The issuance of this draft guidance on clinical pharmacology considerations for neonatal studies for drugs and biological products is stipulated under the FDA Reauthorization Act of 2017 (FDARA).
---
## SNAPSHOT Sb83b51f2e9
CUTOFF DATE (today): 2022-11-26
Regulator: FDA (US)
Matter: FDA draft guidance: Adjusting for Covariates in Randomized Clinical Trials for Drugs and Biological Products
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2021-05-21 | official-forward (B) | draft_guidance_availability_notice | "Adjusting for Covariates in Randomized Clinical Trials for Drugs and Biological Products; Draft Guidance for Industry; Availability" | www.federalregister.gov
   Claims: The Food and Drug Administration (FDA or Agency) is announcing the availability of a draft guidance for industry entitled "Adjusting for Covariates in Randomized Clinical Trials for Drugs and Biological Products." The draft guidance, when finalized, will represent the current thinking of FDA on adju
   Excerpt: The Food and Drug Administration (FDA or Agency) is announcing the availability of a draft guidance for industry entitled "Adjusting for Covariates in Randomized Clinical Trials for Drugs and Biological Products." The draft guidance, when finalized, will represent the current thinking of FDA on adjusting for covariates in randomized clinical trials for drugs and biologics. This draft guidance revises the draft guidance "Adjusting for Covariates in Randomized Clinical Trials for Drugs and Biologics with Continuous Outcomes" that published April 25, 2019. This revision provides more detailed recommendations for the use of linear models for covariate adjustment and also includes recommendations for covariate adjustment using nonlinear models.
---
## SNAPSHOT S38e812fbd2
CUTOFF DATE (today): 2022-12-15
Regulator: FDA (US)
Matter: FDA draft guidance: The Use of Published Literature in Support of New Animal Drug Applications
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2022-04-20 | official-forward (B) | draft_guidance_availability_notice | "The Use of Published Literature in Support of New Animal Drug Applications; Draft Guidance for Industry; Availability" | www.federalregister.gov
   Claims: The Food and Drug Administration (FDA or Agency) is announcing the availability of a draft guidance for industry #106 entitled "The Use of Published Literature in Support of New Animal Drug Applications." This draft guidance, when finalized, will replace the existing final guidance #106, "The Use of
   Excerpt: The Food and Drug Administration (FDA or Agency) is announcing the availability of a draft guidance for industry #106 entitled "The Use of Published Literature in Support of New Animal Drug Applications." This draft guidance, when finalized, will replace the existing final guidance #106, "The Use of Published Literature in Support of New Animal Drug Approval," which FDA published in August 2000 and which specifically addressed the use of a single article to support drug approval. This revision of the guidance document considers multiple uses of the scientific literature, including narrative reviews, systematic reviews, and meta-analyses to support approval of a new animal drug.
---
## SNAPSHOT Sc83723bef8
CUTOFF DATE (today): 2023-11-16
Regulator: FDA (US)
Matter: FDA draft guidance: Charging for Investigational Drugs Under an Investigational New Drug Application: Questions and Answers
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence: none provided for this snapshot.
---
## SNAPSHOT S8e6e622db4
CUTOFF DATE (today): 2026-07-20
Regulator: SEBI (IN)
Matter: SEBI consultation: ease-of-doing-business modifications to master circular provisions on exchange traded derivatives
Decisive action for this matter = the regulator's first official publication ADOPTING the proposal at least in substantial part (e.g., board decision press release, circular, or notified regulation).
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2026-05-14 | official-forward (B) | consultation_paper | "Consultation Paper on Measures for ease of doing business on Exchange Traded Derivatives" | www.sebi.gov.in
   Claims: Third in a series of ease-of-doing-business consultation papers reviewing SEBI's exchange-related master circulars. / Seeks comments on modifications to Chapter 5 (Exchange Traded Derivatives) of the Master Circular for Stock Exchanges and Clearing Corporations. / Seeks comments on modifications to multiple Commodity Derivatives Segment master-circular chapters covering product guidelines, price/position limits, participants, options in goods and commodity futures, and commodity-index product design.
   Excerpt: This consultation paper is third part in the series of consultation papers issued for review of the regulatory norms pertaining to Stock exchanges. In terms of the extant modalities for policy formulation, SEBI, inter-alia, prior to issuing a circular under the Acts or regulations generally undertakes public consultation. Accordingly, the objective of this consultation paper is to seek comments/views/suggestions from public on the modifications to Chapter 5 (Exchange Traded Derivatives) of the Master Circular for Stock Exchanges and Clearing Corporations(MSECC) dated December 30, 2024.
---
## SNAPSHOT S917443f737
CUTOFF DATE (today): 2022-04-23
Regulator: FDA (US)
Matter: FDA draft guidance: Select Updates for Unique Device Identification: Policy Regarding Global Unique Device Identification Database Requirements for Certain Devices
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2021-10-14 | official-forward (B) | draft_guidance_availability_notice | "Select Updates for Unique Device Identification: Policy Regarding Global Unique Device Identification Database Requirements for Certain Devices; Draft Guidance for Industry and Food and Drug Administration Staff; Availab" | www.federalregister.gov
   Claims: The Food and Drug Administration (FDA, Agency, or we) is announcing the availability of the draft guidance entitled "Select Updates for Unique Device Identification: Policy Regarding Global Unique Device Identification Database Requirements for Certain Devices; Draft Guidance for Industry and Food a
   Excerpt: The Food and Drug Administration (FDA, Agency, or we) is announcing the availability of the draft guidance entitled "Select Updates for Unique Device Identification: Policy Regarding Global Unique Device Identification Database Requirements for Certain Devices; Draft Guidance for Industry and Food and Drug Administration Staff." This draft guidance explains that there are certain class I devices for which FDA does not intend to enforce Global Unique Device Identification Database (GUDID) submission requirements and describes how a labeler of a class I device can determine if its device is one of these devices in the revised section III of this draft guidance. When this draft guidance is finalized, the updates in section III of this draft guidance would supersede the recommendations in section III of the guidance "Unique Device Identification: Policy Regarding Compliance Dates for Class I and Unclassified Devices and Certain Devices Requiring Direct Marking" ("2020 UDI Compliance Policy Guidance," available at: https:// www.fda.gov/regulatory-information/search-fda-guidance-documents/ unique-device-identification-policy-regarding-compliance-dates-class-i- and-unclassified-devices-an
---
## SNAPSHOT S73b4778629
CUTOFF DATE (today): 2026-09-17
Regulator: SEBI (IN)
Matter: SEBI consultation: enhancements to the Straight-Through Processing framework for institutional trade messaging
Decisive action for this matter = the regulator's first official publication ADOPTING the proposal at least in substantial part (e.g., board decision press release, circular, or notified regulation).
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2026-05-19 | official-forward (B) | consultation_paper | "Consultation Paper on Easing of framework for Straight Through Processing (STP) of trades" | www.sebi.gov.in
   Claims: Seeks feedback on enhancements to the existing Straight-Through Processing (STP) framework to reduce latency and costs and enhance service delivery for market participants. / Describes STP as automating end-to-end processing of financial-instrument transactions, including Electronic Contract Notes (ECNs), across stock brokers, custodians and institutional investors. / Notes the existing STP architecture (involving Sender/Receiver STP Service Providers, 'SSPs') traces to SEBI circulars dated Feb 3 2004, Feb 25 2004, Apr 1 2004 and May 26 2004. / Identifies issues with the current STP architecture where different SSPs are used by each STP user.
   Excerpt: The objective of the consultation paper is to seek feedback on the enhancements in the existing Straight-Through Processing (STP) Framework to reduce the latency, costs and enhance service delivery for market participants. STP automates the end-to-end processing of transactions of the financial instruments. It involves use of a single system to process or control all elements of the work-flow of a financial transaction.
---
## SNAPSHOT S18e65332c7
CUTOFF DATE (today): 2021-12-26
Regulator: FDA (US)
Matter: FDA draft guidance: Patient Engagement in the Design and Conduct of Medical Device Clinical Investigations
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence: none provided for this snapshot.
---
## SNAPSHOT S511ac0376a
CUTOFF DATE (today): 2023-11-06
Regulator: FDA (US)
Matter: FDA draft guidance: Verification Systems Under the Drug Supply Chain Security Act for Certain Prescription Drugs
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence: none provided for this snapshot.
---
## SNAPSHOT Sbb8480c400
CUTOFF DATE (today): 2026-05-01
Regulator: SEBI (IN)
Matter: SEBI consultation: uniform time lag for sharing and usage of price data for educational purposes
Decisive action for this matter = the regulator's first official publication ADOPTING the proposal at least in substantial part (e.g., board decision press release, circular, or notified regulation).
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2026-01-06 | official-forward (B) | consultation_paper | "Consultation Paper on 'Norms for sharing and usage of price data for educational purposes'" | www.sebi.gov.in
   Claims: Seeks comments on bringing uniformity to the time lag applicable to sharing/usage of price data solely for education and investor-awareness purposes. / Notes a May 24, 2024 circular set a one-day lag for exchanges sharing live data for educational purposes. / Notes a January 29, 2025 circular separately tightened the rule to require a three-month lag for entities solely engaged in education, creating two different, simultaneously-operative time lags.
   Excerpt: SEBI vide circular dated May 24, 2024 (May 2024) restricted the sharing of live data by exchanges only for trading and its related activities, and prescribed a time lag of one day for educational and awareness activities so as to curb the misuse of live data. Further SEBI vide circular dated January 29, 2025 (Jan 2025) further tightened the framework by stipulating that entities solely engaged in education may use such data only with a three months lag... the objective of this consultation paper is to bring uniformity in time-lag for sharing and usage of price data solely for education and investor awareness purposes.
---
## SNAPSHOT Sb9b230f0b6
CUTOFF DATE (today): 2022-12-31
Regulator: FDA (US)
Matter: FDA draft guidance: Chronic Rhinosinusitis With Nasal Polyps: Developing Drugs for Treatment
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence: none provided for this snapshot.
---
## SNAPSHOT Sbc4a9e7df1
CUTOFF DATE (today): 2023-06-24
Regulator: FDA (US)
Matter: FDA draft guidance: Digital Health Technologies for Remote Data Acquisition in Clinical Investigations
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2021-12-23 | official-forward (B) | draft_guidance_availability_notice | "Digital Health Technologies for Remote Data Acquisition in Clinical Investigations; Draft Guidance for Industry, Investigators, and Other Stakeholders; Availability" | www.federalregister.gov
   Claims: The Food and Drug Administration (FDA or Agency) is announcing the availability of a draft guidance for industry, investigators, and other stakeholders entitled "Digital Health Technologies for Remote Data Acquisition in Clinical Investigations." This guidance provides recommendations to sponsors, i
   Excerpt: The Food and Drug Administration (FDA or Agency) is announcing the availability of a draft guidance for industry, investigators, and other stakeholders entitled "Digital Health Technologies for Remote Data Acquisition in Clinical Investigations." This guidance provides recommendations to sponsors, investigators, and other stakeholders on the use of digital health technologies (DHTs) to acquire data remotely from participants in clinical investigations evaluating medical products. DHTs may take the form of hardware and/or software and may be used to gather health-related information from study participants and transmit that information to study investigators and/or other authorized parties to evaluate the safety and effectiveness of medical products.