---
name: refund-order-learnings
description: Standard and template locations for GST refund orders (RFD-06), built 12 Oct 2026
metadata:
  type: project
  modified: 2026-10-12T10:16:36.504Z
---

Santosh wants every refund order drafted to the standard learned from reviewed RFD-06 orders; full standard in /mnt/project-files/gst-orders/refund-order-learnings.md. Never name taxpayers or GSTINs in shared files.

**Why:** he wants "the best possible orders from now on". Templates T1–T8, notice N1 and checklist C1 (12 Oct 2026) are in /mnt/project-files/gst-orders/templates/ (Word + markdown; to regenerate, edit source/src and run source/build.py).

**How to apply:** check every draft order against this list:
- **Legal basis:**
  - s.54(8)(b) for inverted duty and SEZ-under-LUT ITC, (a) for exports; SEZ with IGST paid is (e), so the rule 89(2)(l)/(m) declaration or CA certificate IS required (clause (a) covers only exports since 01.02.2019);
  - s.49(6) for cash-ledger refunds;
  - rejection is under rule 92(3), not 92(1).
- **Relevant date:** (a) goods, (ba) SEZ, (c) services, (e) inverted duty; per shipping bill / remittance.
- **Provisional refund:** state the 90% RFD-04 under rule 91(2), or the reason it was denied. Notification 14/2025-CT exclusions are under s.54(6); rule 91(1) is the separate non-prosecution bar. If provisional exceeds the final amount, recover by RFD-08 under s.54 r/w 73/74/74A (Instruction 06/2025 para 3.4). This applies to zero-rated claims, and to inverted-duty claims filed on or after 01.10.2025 (Instruction 06/2025 para 5.1).
- **Rejected ITC:** direct PMT-03 re-credit under rule 93(2) after the no-appeal undertaking.
- **Computation:**
  - ITC appearing in an earlier month's GSTR-2B is allowed (Circular 197 para 1.3);
  - capital goods are excluded from Net ITC by definition, not "ineligible under s.16(3)";
  - Adjusted Total Turnover leaves out exempt supplies and uses the lower of FOB and invoice value for exports;
  - inverted-duty orders need a rate and HSN table and a check against Notification 5/2017-CT(R).
- **Services:** IGST s.13(2) unless s.13(3)–(13) applies; intermediary (Circular 159) only before the s.13(8)(b) omission (FA 2026 s.157, taken as 30.03.2026).
- **SEZ with tax paid:** rule 89(2)(f) needs a declaration that tax was not collected from the SEZ unit.
- **Notices and hearings:**
  - the RFD-08 must state the actual ground, with 15 days to reply;
  - the order must decide every notice point and every statement made at the hearing;
  - adjust confirmed dues under s.54(10)(b) in the RFD-06 itself (rule 92(1), Circular 125 para 35); RFD-07 only for withholding; never by rejection.
- **Don't ask for:** a CA certificate in ITC refunds, indemnity bonds, or ITC checks in tax-paid categories.
- **Drafting:**
  - appeal clause: APL-01 filed electronically, no court fee, s.107(6) pre-deposit on *tax*;
  - round to the rupee (s.170); no blank dates or placeholders;
  - no findings copied across categories; no unneeded names.
- **Figure sources:** do not take the lowest zero-rated turnover and the highest Adjusted Total Turnover as a rule; nothing in rule 89(4) or Circular 125 says so. Use the same realised services value in the numerator and inside Adjusted Total Turnover (89(4)(E)(b)).
- **The operative ORDER** must also reject the balance under rule 92(3) and direct PMT-03 re-credit, not just sanction.
- **Pre-deposit refunds:**
  - s.115 interest at 6% from the date of payment, computed in the order;
  - relevant date under Explanation 2(d), not s.54(2);
  - s.54(8)(e);
  - record whether the department has appealed the order-in-appeal.
- **Inverted duty:** split the Part B denominator into inputs, input services, capital goods and blocked credit, reconciled to GSTR-3B. Check every month for deemed exports and SEZ supplies.
- **Officer's own orders** rated 12 Oct 2026 (avg 6.2/10, best SO 84): /mnt/project-files/gst-orders/speaking-orders-evaluation.md.

Related: [[gst-law-knowledge-base]]
