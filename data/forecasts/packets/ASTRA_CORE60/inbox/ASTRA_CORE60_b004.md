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
## SNAPSHOT Sc6a5a8b3a5
CUTOFF DATE (today): 2026-05-16
Regulator: SEBI (IN)
Matter: SEBI consultation: reviewing base price and price band methodology for Exchange Traded Funds
Decisive action for this matter = the regulator's first official publication ADOPTING the proposal at least in substantial part (e.g., board decision press release, circular, or notified regulation).
Evidence: none provided for this snapshot.
---
## SNAPSHOT S87651394be
CUTOFF DATE (today): 2024-03-01
Regulator: FDA (US)
Matter: FDA draft guidance: Voluntary Malfunction Summary Reporting Program for Manufacturers
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2022-12-09 | official-forward (B) | draft_guidance_availability_notice | "Voluntary Malfunction Summary Reporting Program for Manufacturers; Draft Guidance for Industry and Food and Drug Administration Staff; Availability" | www.federalregister.gov
   Claims: The Food and Drug Administration (FDA or Agency) is announcing the availability of the draft guidance entitled "Voluntary Malfunction Summary Reporting (VMSR) Program for Manufacturers." We are publishing this notice of availability for this draft guidance document to help manufacturers better under
   Excerpt: The Food and Drug Administration (FDA or Agency) is announcing the availability of the draft guidance entitled "Voluntary Malfunction Summary Reporting (VMSR) Program for Manufacturers." We are publishing this notice of availability for this draft guidance document to help manufacturers better understand and use the VMSR Program. It is intended to further explain, but not change, the conditions of the VMSR Program. This draft guidance is not final nor is it for implementation at this time.
---
## SNAPSHOT S4d3a8d6b89
CUTOFF DATE (today): 2026-02-13
Regulator: SEBI (IN)
Matter: SEBI consultation: reviewing use of historical price scenarios in stress testing for the Commodity Derivatives Segment
Decisive action for this matter = the regulator's first official publication ADOPTING the proposal at least in substantial part (e.g., board decision press release, circular, or notified regulation).
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2026-02-05 | official-forward (B) | draft_circular_for_comment | "Consultation Paper On Draft Circular on Review of Inclusion of Historical Scenarios in Stress Testing and Coverage of Settlement Guarantee Fund for Commodity Derivatives Segment" | www.sebi.gov.in
   Claims: Proposes to review the Z-score threshold (currently 10) used to cap extreme historical price movements in peak-historical-return stress-testing scenarios for the Commodity Derivatives Segment's Core Settlement Guarantee Fund. / Also proposes to review the coverage requirement of the Settlement Guarantee Fund for the Commodity Derivatives Segment. / Describes the existing framework's 15-year historical lookback period for computing maximum percentage rise/fall (Scenarios 1A/1B).
   Excerpt: SEBI Master Circular... for Commodity Derivatives Segment dated Aug 04, 2023, inter alia, prescribes norms related to Core Settlement Guarantee Fund (SGF). The extant provisions pertaining to applicable value of Z-Score (for the purpose of stress testing) and coverage of SGF, as provided in paragraph 22 of Annexure O of the said circular are as follows: ...Price movements corresponding to a Z-score of 10 will replace extreme price movements beyond that threshold in peak historical returns of all the commodities. SEBI has received representations to review the aforementioned extant provision related to Z-Score for Commodity Derivatives Market.
---
## SNAPSHOT Sb47da2fbbd
CUTOFF DATE (today): 2025-09-16
Regulator: FDA (US)
Matter: FDA draft guidance: Sponsor Responsibilities-Safety Reporting Requirements and Safety Assessment for Investigational New Drug Application and Bioavailability/Bioequivalence Studies
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2021-06-28 | official-forward (B) | draft_guidance_availability_notice | "Sponsor Responsibilities-Safety Reporting Requirements and Safety Assessment for Investigational New Drug Application and Bioavailability/Bioequivalence Studies; Draft Guidance for Industry; Availability" | www.federalregister.gov
   Claims: The Food and Drug Administration (FDA or Agency) is announcing the availability of a draft guidance for industry entitled "Sponsor Responsibilities--Safety Reporting Requirements and Safety Assessment for Investigational New Drug Application and Bioavailability/ Bioequivalence Studies." The draft gu
   Excerpt: The Food and Drug Administration (FDA or Agency) is announcing the availability of a draft guidance for industry entitled "Sponsor Responsibilities--Safety Reporting Requirements and Safety Assessment for Investigational New Drug Application and Bioavailability/ Bioequivalence Studies." The draft guidance provides recommendations for sponsors and sponsor-investigators to comply with the requirements of investigational new drug application (IND) safety reporting and safety reporting for bioavailability (BA) and bioequivalence (BE) studies. In doing so, the guidance provides recommendations related to the two IND safety reporting provisions that require assessment of aggregate data to facilitate appropriate IND safety reporting practices. An earlier draft guidance for industry entitled "Safety Assessment for IND Safety Reporting" (December 2015) (the 2015 draft guidance) has been incorporated into this draft guidance. However, this content was revised to address feedback from stakeholders and comments received on the 2015 draft guidance. Concurrent with the publication of this draft guidance, we are withdrawing the 2015 draft guidance. Additionally, this draft guidance incorporates c
---
## SNAPSHOT S0d3a00cf27
CUTOFF DATE (today): 2024-09-04
Regulator: FDA (US)
Matter: FDA draft guidance: Marketing Submission Recommendations for a Predetermined Change Control Plan for Artificial Intelligence/Machine Learning-Enabled Device Software Functions
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2023-03-30 | official-forward (B) | draft_guidance_availability_notice | "Marketing Submission Recommendations for a Predetermined Change Control Plan for Artificial Intelligence/Machine Learning-Enabled Device Software Functions; Draft Guidance for Industry and Food and Drug Administration St" | www.federalregister.gov
   Claims: The Food and Drug Administration (FDA or Agency) is announcing the availability of the draft guidance entitled "Marketing Submission Recommendations for a Predetermined Change Control Plan for Artificial Intelligence/Machine Learning (AI/ML)-Enabled Device Software Functions." This draft guidance de
   Excerpt: The Food and Drug Administration (FDA or Agency) is announcing the availability of the draft guidance entitled "Marketing Submission Recommendations for a Predetermined Change Control Plan for Artificial Intelligence/Machine Learning (AI/ML)-Enabled Device Software Functions." This draft guidance demonstrates FDA's commitment to developing innovative approaches to the regulation of machine learning- enabled medical devices and describes an approach that would often be the least burdensome and would support iterative improvement through modifications to machine learning-enabled device software functions (herein referred to as ML-DSF) while continuing to ensure device safety and effectiveness. This draft guidance provides recommendations on the information to be included in a Predetermined Change Control Plan (PCCP) in a marketing submission for an ML-DSF. Such a plan describes the anticipated ML-DSF modifications and the associated methodology to implement those modifications, which would be reviewed in the marketing submission to ensure the continued safety and effectiveness of the device without necessitating additional marketing submissions for each modification described in the
---
## SNAPSHOT S30d9fb5c26
CUTOFF DATE (today): 2021-09-28
Regulator: FDA (US)
Matter: FDA draft guidance: Biomarkers and Surrogate Endpoints in Clinical Studies To Support Effectiveness of New Animal Drugs
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2020-07-15 | official-forward (B) | draft_guidance_availability_notice | "Biomarkers and Surrogate Endpoints in Clinical Studies To Support Effectiveness of New Animal Drugs; Draft Guidance for Industry; Availability" | www.federalregister.gov
   Claims: The Food and Drug Administration (FDA or Agency) is announcing the availability of a draft guidance for industry (GFI) #267 entitled "Biomarkers and Surrogate Endpoints in Clinical Studies Support Effectiveness of New Animal Drugs." The draft guidance, if finalized, will describe FDA's current think
   Excerpt: The Food and Drug Administration (FDA or Agency) is announcing the availability of a draft guidance for industry (GFI) #267 entitled "Biomarkers and Surrogate Endpoints in Clinical Studies Support Effectiveness of New Animal Drugs." The draft guidance, if finalized, will describe FDA's current thinking with respect to assisting sponsors in incorporating biomarkers and surrogate endpoints into proposed clinical investigation protocols and applications for new animal drugs under the Federal Food, Drug, and Cosmetic Act (FD&C Act).
---
## SNAPSHOT S702c53548d
CUTOFF DATE (today): 2026-09-17
Regulator: SEBI (IN)
Matter: SEBI consultation: investor consent and conflicted-transaction thresholds for Alternative Investment Funds
Decisive action for this matter = the regulator's first official publication ADOPTING the proposal at least in substantial part (e.g., board decision press release, circular, or notified regulation).
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2026-06-30 | official-forward (B) | consultation_paper | "Consultation paper on rationalizing the requirement of obtaining investor consent and ambit of conflicted transactions requiring investor consent under SEBI (Alternative Investment Funds) Regulations, 2012" | www.sebi.gov.in
   Claims: Proposes to standardize the process and methodology by which AIFs obtain investor consent under AIF Regulations, including for conflicted transactions. / Proposes to bring consistency to the unitholder-approval threshold prescribed across different AIF Regulations provisions and circulars. / Proposes to rationalize the ambit/scope of 'conflicted transactions' that require investor consent, including revisiting the definition of 'associate'. / States that diverse market practice has emerged on solicitation, voting methodology and treatment of non-responses, creating interpretational uncertainty.
   Excerpt: With an approach to strike a balance between operational and investment flexibility for AIFs, while ensuring that investors are able to make informed decisions, this consultation paper seeks comments and views from the public and stakeholders on the following proposals - 1.1. To standardize the process of obtaining investor consent as per requirements mandated under AIF Regulations, including, for carrying out conflicted transactions; 1.2. To bringing consistency in threshold for unitholder approval prescribed under AIF Regulations and circulars issued thereunder; and, 1.3. To rationalize the ambit of conflicted transactions which would require investor consent, in a manner that aligns with the underlying regulatory intent.
---
## SNAPSHOT Sfcdb3827e4
CUTOFF DATE (today): 2026-09-17
Regulator: SEBI (IN)
Matter: SEBI consultation: harmonizing base price for pre-open call auction and price bands for stocks listed on multiple exchanges
Decisive action for this matter = the regulator's first official publication ADOPTING the proposal at least in substantial part (e.g., board decision press release, circular, or notified regulation).
Evidence: none provided for this snapshot.
---
## SNAPSHOT S88fe7f0914
CUTOFF DATE (today): 2025-11-24
Regulator: SEBI (IN)
Matter: SEBI consultation: standardising the process for opening mutual fund folios and executing the first investment
Decisive action for this matter = the regulator's first official publication ADOPTING the proposal at least in substantial part (e.g., board decision press release, circular, or notified regulation).
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2025-10-23 | official-forward (B) | consultation_paper | "Consultation Paper on Standardisation of process for Opening of Mutual Fund Folios and Execution of First Investment" | www.sebi.gov.in
   Claims: Proposes that a new mutual fund folio's first transaction/investment be permitted only after KYC verification is completed by the KRA and the folio is marked KYC-compliant. / Notes current practice: AMCs conduct internal KYC checks and process the investment while simultaneously forwarding documents to the KRA, sometimes resulting in KYC non-compliant folios if the KRA, on review, finds deficiencies. / Describes resulting investor impediments, including inability to execute further transactions or receive redemption/dividend proceeds until KYC status is marked compliant in the KRA system.
   Excerpt: The objective of this consultation paper is to solicit comments on the proposed standardization of process for opening of Mutual Fund Folios and execution of first investment. It is proposed that first new folios be ascertained to be fully Know Your Client (KYC) compliant both at the Asset Management Company (AMC) level as well as in the KYC Registration Agency (KRA) system. Investors may commence transactions or investments once the KYC verification is successfully completed by the KRA and the folio is accordingly marked as KYC compliant.
---
## SNAPSHOT Sf3b2cf447a
CUTOFF DATE (today): 2026-05-20
Regulator: SEBI (IN)
Matter: SEBI consultation: amendments to the Issue and Listing of Securitised Debt Instruments and Security Receipts Regulations
Decisive action for this matter = the regulator's first official publication ADOPTING the proposal at least in substantial part (e.g., board decision press release, circular, or notified regulation).
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2026-05-04 | official-forward (B) | consultation_paper | "Consultation paper on amendments to the SEBI (Issue and Listing of Securitised Debt Instruments and Security Receipts) Regulations, 2008" | www.sebi.gov.in
   Claims: Proposes amendments to the SEBI (Issue and Listing of Securitised Debt Instruments and Security Receipts) Regulations, 2008 to align with RBI's securitisation framework. / Proposes exempting RBI-regulated entities (e.g., banks, NBFCs) from the existing 25% single-obligor concentration limit for single-asset securitisation transactions, aligning with RBI norms that already permit this for such entities. / Proposes additional disclosure of concentration risk arising from single-asset securitisation in the offer document, to inform investors given the changed concentration limit.
   Excerpt: CONSULTATION PAPER, DEPARTMENT OF DEBT AND HYBRID SECURITIES, Consultation paper on amendments to the SEBI (Issue and Listing of Securitised Debt Instruments and Security Receipts) Regulations, 2008, May 04, 2026. [Timeline to Respond: Comments on the Consultation paper may be sent by May 25, 2026]
---
## SNAPSHOT Sdb94ec5c0c
CUTOFF DATE (today): 2024-10-10
Regulator: FDA (US)
Matter: FDA draft guidance: Review of Drug Master Files in Advance of Certain Abbreviated New Drug Application Submissions Under Generic Drug User Fee Amendments
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence: none provided for this snapshot.
---
## SNAPSHOT S1f46fb7151
CUTOFF DATE (today): 2023-05-30
Regulator: FDA (US)
Matter: FDA draft guidance: Chronic Rhinosinusitis With Nasal Polyps: Developing Drugs for Treatment
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2021-12-10 | official-forward (B) | draft_guidance_availability_notice | "Chronic Rhinosinusitis With Nasal Polyps: Developing Drugs for Treatment; Draft Guidance for Industry; Availability" | www.federalregister.gov
   Claims: The Food and Drug Administration (FDA or Agency) is announcing the availability of a draft guidance for industry entitled "Chronic Rhinosinusitis with Nasal Polyps: Developing Drugs for Treatment." The purpose of this draft guidance is to assist sponsors in the clinical development of drugs for the 
   Excerpt: The Food and Drug Administration (FDA or Agency) is announcing the availability of a draft guidance for industry entitled "Chronic Rhinosinusitis with Nasal Polyps: Developing Drugs for Treatment." The purpose of this draft guidance is to assist sponsors in the clinical development of drugs for the treatment of chronic rhinosinusitis with nasal polyps (CRSwNP). Specifically, this draft guidance addresses FDA's current recommendations regarding trial design, safety, and efficacy considerations for CRSwNP clinical trials.
---
## SNAPSHOT S95b417414e
CUTOFF DATE (today): 2023-06-24
Regulator: FDA (US)
Matter: FDA draft guidance: Digital Health Technologies for Remote Data Acquisition in Clinical Investigations
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence: none provided for this snapshot.
---
## SNAPSHOT Sa2ba567edc
CUTOFF DATE (today): 2024-04-22
Regulator: FDA (US)
Matter: FDA draft guidance: Measuring Growth and Evaluating Pubertal Development in Pediatric Clinical Trials
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2022-11-01 | official-forward (B) | draft_guidance_availability_notice | "Measuring Growth and Evaluating Pubertal Development in Pediatric Clinical Trials; Draft Guidance for Industry; Availability" | www.federalregister.gov
   Claims: The Food and Drug Administration (FDA or Agency) is announcing the availability of a draft guidance for industry entitled "Measuring Growth and Evaluating Pubertal Development in Pediatric Clinical Trials." The purpose of this draft guidance is to outline the most appropriate methods for measuring a
   Excerpt: The Food and Drug Administration (FDA or Agency) is announcing the availability of a draft guidance for industry entitled "Measuring Growth and Evaluating Pubertal Development in Pediatric Clinical Trials." The purpose of this draft guidance is to outline the most appropriate methods for measuring and recording growth and evaluating pubertal development for drugs or biological products in development for pediatric use when such an assessment is necessary to support safety. This draft guidance is intended to encourage a consistent approach to collecting interpretable and accurate growth and pubertal development data. This draft guidance does not address use of growth or pubertal development data to support primary evidence of efficacy in growth disorders and does not address evaluation of nutritional status.
---
## SNAPSHOT S60776bd338
CUTOFF DATE (today): 2021-07-05
Regulator: FDA (US)
Matter: FDA draft guidance: Technical Considerations for Demonstrating Reliability of Emergency-Use Injectors Submitted Under a Biologics License Application, New Drug Application, or Abbreviated New Drug ...
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2020-04-21 | official-forward (B) | draft_guidance_availability_notice | "Technical Considerations for Demonstrating Reliability of Emergency-Use Injectors Submitted Under a Biologics License Application, New Drug Application, or Abbreviated New Drug Application; Draft Guidance for Industry an" | www.federalregister.gov
   Claims: The Food and Drug Administration (FDA or Agency) is announcing the availability of a draft guidance for industry and FDA entitled "Technical Considerations for Demonstrating Reliability of Emergency- Use Injectors Submitted under a BLA, NDA or ANDA." For injectable drug or biological products that a
   Excerpt: The Food and Drug Administration (FDA or Agency) is announcing the availability of a draft guidance for industry and FDA entitled "Technical Considerations for Demonstrating Reliability of Emergency- Use Injectors Submitted under a BLA, NDA or ANDA." For injectable drug or biological products that are intended to treat emergent, life- threatening conditions, it is essential to ensure that the emergency- use injector will reliably deliver the drug or biological product as intended. This is particularly critical for drugs when failure of the injector may prevent adequate delivery of a life-saving drug to a patient. The draft guidance describes the technical considerations for demonstrating reliability of emergency-use injectors under a biologics license application (BLA), new drug application (NDA), or abbreviated new drug application (ANDA).
---
## SNAPSHOT S2918790b96
CUTOFF DATE (today): 2024-04-12
Regulator: FDA (US)
Matter: FDA draft guidance: Mpox: Development of Drugs and Biological Products
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence: none provided for this snapshot.
---
## SNAPSHOT S9960d5d2cc
CUTOFF DATE (today): 2026-05-20
Regulator: SEBI (IN)
Matter: SEBI consultation: 'Green-Channel' document-acknowledgement mechanism for launch of Alternative Investment Fund schemes
Decisive action for this matter = the regulator's first official publication ADOPTING the proposal at least in substantial part (e.g., board decision press release, circular, or notified regulation).
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2026-05-11 | official-forward (B) | consultation_paper | "Consultation on 'Green-Channel: AIF Rollout Upon Document Acknowledgement' (GARUDA) Mechanism for Processing of Placement Memorandum of Alternative Investment Funds (AIFs) filed with SEBI" | www.sebi.gov.in
   Claims: Proposes amending AIF Regulations, 2012 to reduce the scheme-launch timeline for 'Regular' (non-accredited, non-angel) AIF schemes to 10 working days. / Proposes exempting AI-only schemes and Angel Funds from filing the Private Placement Memorandum (PPM) through a Merchant Banker, allowing launch immediately on grant of SEBI registration or PPM filing. / Describes this as 'Phase 2' of an ease-of-doing-business initiative, following an April 30, 2026 Phase-1 circular that let AIFs begin soliciting funds 30 days after filing an application, subject to post-facto sample-based SEBI scrutiny. / States the objective is to further ease AIF scheme-launch procedures given the sophistication of AIF investors and the due-diligence role already played by Merchant Bankers.
   Excerpt: SEBI has recently reviewed the procedure for processing Private Placement Memorandums (PPMs) of AIFs for launch of schemes/funds... Recently, as an Ease of Doing Business Measure, a Fast-Track Mechanism has been adopted for launch of schemes (other than LVFs) by AIFs... SEBI, vide circular dated April 30, 2026, inter alia clarified that AIFs may now proceed with the launch of their Regular schemes, AI only schemes & Angel Funds and begin soliciting funds from investors 30 days after filing their application with SEBI. The purpose of this consultation paper is to further ease the process of scheme launch by AIFs (Phase 2) through amendment to relevant provisions in SEBI (AIF) Regulations, 2012.
---
## SNAPSHOT S0f940887dc
CUTOFF DATE (today): 2022-09-16
Regulator: FDA (US)
Matter: FDA draft guidance: The Use of Published Literature in Support of New Animal Drug Applications
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2022-04-20 | official-forward (B) | draft_guidance_availability_notice | "The Use of Published Literature in Support of New Animal Drug Applications; Draft Guidance for Industry; Availability" | www.federalregister.gov
   Claims: The Food and Drug Administration (FDA or Agency) is announcing the availability of a draft guidance for industry #106 entitled "The Use of Published Literature in Support of New Animal Drug Applications." This draft guidance, when finalized, will replace the existing final guidance #106, "The Use of
   Excerpt: The Food and Drug Administration (FDA or Agency) is announcing the availability of a draft guidance for industry #106 entitled "The Use of Published Literature in Support of New Animal Drug Applications." This draft guidance, when finalized, will replace the existing final guidance #106, "The Use of Published Literature in Support of New Animal Drug Approval," which FDA published in August 2000 and which specifically addressed the use of a single article to support drug approval. This revision of the guidance document considers multiple uses of the scientific literature, including narrative reviews, systematic reviews, and meta-analyses to support approval of a new animal drug.
---
## SNAPSHOT S44c83cbc71
CUTOFF DATE (today): 2023-01-27
Regulator: FDA (US)
Matter: FDA draft guidance: Mitigation Strategies To Protect Food Against Intentional Adulteration
Decisive action for this matter = the agency publishes the FINAL version of this guidance.
Evidence available as of the cutoff (1 item(s), chronological):
[E1] 2020-02-13 | official-forward (B) | draft_guidance_availability_notice | "Mitigation Strategies To Protect Food Against Intentional Adulteration; Draft Guidance for Industry; Availability" | www.federalregister.gov
   Claims: The Food and Drug Administration (FDA, we, or Agency) is announcing the availability of a supplemental draft guidance for industry entitled "Mitigation Strategies to Protect Food Against Intentional Adulteration: Guidance for Industry." This supplemental draft guidance document, when finalized, will
   Excerpt: The Food and Drug Administration (FDA, we, or Agency) is announcing the availability of a supplemental draft guidance for industry entitled "Mitigation Strategies to Protect Food Against Intentional Adulteration: Guidance for Industry." This supplemental draft guidance document, when finalized, will help food facilities that manufacture, process, pack, or hold food, and that are required to register under the Federal Food, Drug, and Cosmetic Act (FD&C Act) comply with the requirements of our regulation entitled "Mitigation Strategies to Protect Food Against Intentional Adulteration."
---
## SNAPSHOT S96df4ed51d
CUTOFF DATE (today): 2025-11-01
Regulator: SEBI (IN)
Matter: SEBI consultation: ease-of-doing-business modifications to master circular provisions on administration of stock exchanges
Decisive action for this matter = the regulator's first official publication ADOPTING the proposal at least in substantial part (e.g., board decision press release, circular, or notified regulation).
Evidence: none provided for this snapshot.