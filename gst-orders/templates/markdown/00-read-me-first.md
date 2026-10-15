# Refund order templates: read me first

**Look of the orders.** Every order and notice opens with the bilingual Government of India letterhead of the Sangareddy CGST Division, Medchal CGST Commissionerate, and the "GST: One Nation, One Tax" band; every page carries the order number in the header and "Page X of Y" in the footer. The office, officer and appellate-authority details are set once in source/build.py (OFFICE), so a change there updates all templates.

**What is in this folder**

| File | Use it for | Category in RFD-01 | Key law |
|---|---|---|---|
| C1 Refund checklist | Every refund application, from receipt to post-order | All | Rules 89 to 94; Circular 125/44/2019; Instruction 06/2025-GST |
| N1 RFD-08 notice | Proposing to reject any part of a claim; optionally also demanding ineligible ITC | All | Rule 92(3); Circular 125 paras 20 to 23 |
| T1 Inverted duty | Unutilised ITC because inputs are taxed higher than outputs | ITC accumulated due to inverted tax structure | Section 54(3)(ii); rule 89(5) |
| T2 Export of goods (LUT) | Unutilised ITC on goods exported without IGST | Export without payment of tax | Section 54(3)(i); IGST section 16(3); rule 89(4) |
| T3 Export of services (LUT) | Unutilised ITC on services exported without IGST | Export without payment of tax | IGST sections 2(6), 13, 16(3); rule 89(4) |
| T4 SEZ supplies (LUT) | Unutilised ITC on supplies to SEZ units / developers without IGST | Supplies to SEZ without payment of tax | IGST section 16(1)(b); proviso to rule 89(1) on SEZ supplies, 89(4) |
| T5 Export of services (IGST paid) | Refund of IGST paid on services exported | Export of services with payment of tax | IGST section 16(4); Notification 01/2023-IT |
| T6 SEZ supplies (IGST paid) | Refund of IGST paid on supplies to SEZ | Supplies to SEZ with payment of tax | IGST section 16(4); rule 89(2)(f) |
| T7 Excess cash ledger | Unutilised balance in the electronic cash ledger | Excess balance in electronic cash ledger | Section 49(6); Circular 166/22/2021 |
| T8 Appeal / pre-deposit | Refund after an order-in-appeal or Tribunal order, with section 115 interest; also a refund rejected by RFD-06 and later allowed in appeal (Option D) | On account of assessment / provisional assessment / appeal / any other order [or the separate pre-deposit category, if the portal offers one] | Section 54(8)(e), Explanation 2(d); section 115 |

Refund of IGST paid on **goods exported** is processed through ICEGATE under rule 96 and needs no RFD-06, **except** where the claim is withheld under rule 96(4) and transmitted to the proper officer as a system-generated RFD-01 (rule 96(5A) to (5C)). Such a claim is decided under rule 89 by an RFD-06: adapt T2 and use C1 item D2. Deemed exports and excess payment of tax are covered in the checklist (D9, D10); templates for them can be added on the same pattern.

**How to adopt a template**

1. Open the Word file for the category and save a copy for the case.
2. Fill every [square bracket]. Where you see **[Option A]**, **[Option B]**, keep the one that fits and delete the others.
3. Delete every grey "Drafting note" box. They are instructions to the officer, not part of the order.
4. Do the final check printed just above the signature: the computed amount, the table in para 11, the ORDER and the amount in words must agree.
5. Upload the order with FORM GST RFD-06 on the portal; issue RFD-05 and any DRC-07 with the order, and any RFD-07 (withholding only). Issue PMT-03 only after the applicant's undertaking not to appeal, or after the appeal is finally rejected (rule 93).

**Common structure of every order (so that any reader finds things in the same place)**

| Para | Content |
|---|---|
| Header | Office, form, RFN, and a table of every date: ARN, RFD-02, the sixty-day date, RFD-04, RFD-08, reply, hearing |
| Note | Appeal rights: APL-01 filed electronically, 3 months + 1 month, the section 107(6) pre-deposit, the appellate authority under rule 109A |
| 1 | Brief facts |
| 2 | Legal provisions for this category only |
| 3 | Limitation: the clause of Explanation 2 named, the date tested, checked per shipping bill / remittance / month |
| 4 | Completeness, returns, debit entry, duplicate check, Aadhaar |
| 5 | Provisional refund: granted / not low-risk / not granted under the first proviso to rule 91(2) / barred |
| 6 | Verification specific to the category |
| 7 | Computation with a source table, the formula with figures, least of three, head-wise split |
| 8 | Notice, reply and hearing: every ground and every submission decided in a table |
| 9 | Unjust enrichment, section 54(10)/(11) dues, ₹1,000 minimum, bank account, sixty days and interest |
| 10 | Conclusion |
| 11 | ORDER: sanction, provisional adjusted, section 54(10)(b) adjustment shown in the order (RFD-07 only for withholding), RFD-05, rejection under rule 92(3), PMT-03 re-credit, any DRC-07, interest |

**Where the features come from**

- From the best orders reviewed in 2026 (other zones and the officer's own): the comparison of figures from different sources (RFD-01 against returns against ICEGATE) in one table; a separate decision on a refund rejection and a demand of ineligible ITC in the same order; the rate-wise inversion analysis; the point-by-point record of the reply.
- From the mistakes found in those orders: the corrected appeal paragraph; the relevant-date clause by name; the provisional-refund paragraph; no "lowest / highest" turnover rule; no documents beyond rule 89(2); dues adjusted in the order under section 54(10)(b) or withheld by RFD-07, never by rejection; PMT-03 re-credit directed in the ORDER; section 115 interest computed in pre-deposit refunds; rounding under section 170.
- From the law as it stands on 12.10.2026: rule 91(2) risk-based provisional refund (Notification 13/2025-CT) and Instruction 06/2025-GST, including its para 5.1 for inverted duty; Notification 14/2025-CT exclusions; Circular 197/09/2023 on GSTR-2B and the section 42 undertaking; Circular 249/06/2025 on RFN and DIN; omission of the intermediary rule in IGST section 13(8)(b) by the Finance Act, 2026 (the law text records only the date of the Act, 30.03.2026; the templates leave the commencement date to be confirmed); the pending Finance Act, 2026 amendments to sections 54(6) and 54(14) (not yet in force).

**Points to re-check before using a template after a change in law**

- Whether section 155 of the Finance Act, 2026 (provisional refund for inverted duty in section 54(6); ₹1,000 limit lifted for goods exported with tax) has been notified.
- Whether section 54(15) (export duty) has been brought into force in place of the second proviso to section 54(3).
- Whether section 157 of the Finance Act, 2026 (omission of section 13(8)(b) of the IGST Act, intermediary services) has been brought into force, and from what date (T3 and T5 para 2.2).
- The 57th GST Council meeting (8 October 2026) recommended changes that are **not yet notified**. When notified, update:
  - input-service credit in inverted-duty refunds, for credit availed on or after 1 November 2026 (T1 paras 2.2 to 2.3 and 7.1);
  - capital-goods credit refundable over 60 months for zero-rated and inverted-duty supplies, for credit availed on or after 1 April 2027 (T1 to T4 paras 2 and 7);
  - removal of the 1.5-times cap in rule 89(4)(C) (T2 para 6.4, T4);
  - section 54(14) minimum applied to the combined refund, not per head (para 9.3 in all templates, C1 G9);
  - section 115 recast as a standalone interest provision (T8 paras 2.3 and 9.6);
  - omission of section 2(6)(v) and section 13(3)(a) of the IGST Act (T3, T5 Table A);
  - auto-sanction of cash-ledger refunds and 10-day acknowledgement (T7; header row).
- Any new instruction on provisional refund or a new refund circular.

**Adjudication templates (added 14 October 2026)**

| Template | Use it for |
|---|---|
| A1 | Detailed show cause notice with DRC-01, one financial year, s.73 / 74 / 74A variants; starts with a one-page guide to the A and B series |
| A2 | Issue modules for the SCN: ITC above GSTR-2B, supplier not paying (s.16(2)(c)), s.16(4), GSTR-1 v. 3B short payment, RCM, fake invoices, unregistered person, rate or classification, s.17(5), late fee and interest |
| A3 | DRC-01A intimation before the SCN (rule 142(1A)) |
| A4 | Personal hearing notice, adjournment and final-opportunity notices, record of personal hearing |
| A5 | Corrigendum or addendum to an SCN |
| B1 | Order-in-Original with DRC-07 (s.73 / 74 / 74A) |
| B2 | Finding modules for the same ten issues: defences and how to answer or concede them |
| B3 | Ex parte order after three opportunities |
| B4 | Rectification under s.161 (DRC-08) |
| B5 | Re-determination under s.75(2) when fraud is not proved |
| C2 | Adjudication checklist (SCN, hearing, order, after the order) |

They are built from `/mnt/project-files/gst-law/adjudication/` (procedure, appeals, court-proof checklist) and the review of eleven division SCNs (`/mnt/project-files/gst-orders/adjudication/scn-evaluation.md`). Check the s.50(3) interest rate and the monetary limits against the current notifications and circulars before use.

**Registration templates (added 14 October 2026)**

These are issued by the **Range Superintendent**, who is the proper officer for registration, cancellation and revocation (Circular No. 1/1/2017-GST as amended by Circular No. 223/17/2024-GST). Their letterhead therefore reads "Office of the Superintendent of Central Tax, [ ] Range"; fill in the Range. Their appeal paragraph names an officer not below Joint Commissioner (Appeals) (rule 109A(1)(b)).

| Template | Use it for | Form and rule |
|---|---|---|
| R1 | Query on a new registration, amendment, cancellation or rule 14A withdrawal application, limited to the grounds Instruction 03/2025-GST allows | REG-03; rules 9(2), 19(2), 14A |
| R2 | Physical verification report of the place of business | Annexure to REG-30; rule 25 |
| R3 | Show cause notice for cancellation, with nine ground modules (non-existence, non-filing, invoices without supply, ITC in breach of s.16, GSTR-1 above 3B, bank account, rule 86B, voluntary registrant, fraud in obtaining registration), retrospective date and suspension | REG-17; s.29(2); rules 21, 21A(2), 22(1) |
| R4 | Cancellation order, suo motu (Option A) or on the taxpayer's application (Option B) | REG-19; rule 22(3); Circular 69/43/2018 |
| R5 | Dropping cancellation proceedings and revoking suspension (reply satisfactory, returns filed, bank details given, REG-31 prima facie explained) | REG-20; rules 22(4), 21A(4) |
| R6 | Office note: reasons to believe before suspending, and record of examining a reply to a system REG-31 | Rule 21A(2), (2A); Circular 145/01/2021 |
| R7 | Show cause notice before rejecting a revocation application | REG-23; rule 23(3) |
| R8 | Revocation order (Part A) or rejection of revocation (Part B) | REG-22 / REG-05; rule 23(2) |
| R9 | Rejection of a registration, amendment, cancellation or withdrawal application after REG-03 | REG-05; rules 9(4), 19(4), 14A |
| R10 | Registration checklist, one page per stage | All of the above |

They are built from `/mnt/project-files/gst-law/registration/` (procedure guide and court-proof checklist). Re-check them when the 57th Council's registration changes (rules 14B, 19, 21, 21A, 22, 23A) are notified.
