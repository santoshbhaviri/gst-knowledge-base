# GST law in India: overview (start here)

**Last updated:** 15 Oct 2026 (case law checked against judgment text). This file is the starting point for project "Excellence".

## What GST is, in one page
- **One tax on supply, levied by both the Centre and the States.**
  - **Within a State:** the Centre levies **CGST** and the State levies **SGST**, or **UTGST** in a UT without a legislature.
  - **Between States, on imports, and on supplies to an SEZ:** the Centre levies **IGST** and shares it with the destination State.
  - Basis: the 101st Constitutional Amendment (Articles 246A, 269A and 279A). GST started on **1 July 2017**.
- **Destination-based, with input tax credit (ITC) along the chain.** Tax flows to the consuming State. Each business claims credit for tax paid on its purchases, so in principle only value added is taxed.
- **The GST Council** (Union FM plus all State FMs) recommends rates, exemptions and changes to the law. Parliament and the State legislatures enact the law; CBIC and the States implement it through rules, notifications and circulars.
- **Rates today:**
  - **5% (merit)** and **18% (standard)**, plus **40% (de-merit)**, since the 56th Council (from 22.09.2025).
  - Nil for exempt goods. Special rates remain, such as 3% on gold and 0.25% on rough diamonds.
  - Tobacco and pan masala moved to 40% on 01.02.2026, when compensation cess on them ended.
- **Hierarchy of instruments:** Constitution, then the Acts, then the Rules, then notifications (which have force of law), then circulars and instructions (which bind officers only), then FAQs and press releases (no legal force).

## Files in this knowledge base
| File | Contents |
|---|---|
| [01-acts.md](01-acts.md) | Constitutional base; CGST, IGST, UTGST, SGST and Compensation Acts; how the State Acts mirror CGST; CGST chapter map; amendment timeline to the Finance Act, 2026 |
| [02-cgst-rules.md](02-cgst-rules.md) | Chapter map of the CGST Rules, key rules, amendments 2024–26, rules coming from the 57th Council |
| [03-notifications.md](03-notifications.md) | Notification series, counts by year, landmark notifications, and 2025–26 in detail |
| [04-circulars.md](04-circulars.md) | Latest circulars, landmark circulars by topic, instructions 2024–26 |
| [04a-circulars-full-list.md](04a-circulars-full-list.md) | All 272 GST circulars on CBIC (1 to 256 plus IGST), with links |
| [05-gst-council-meetings.md](05-gst-council-meetings.md) | All 57 meetings with official minutes links; 1st to 54th checked against signed minutes with paragraph citations; detailed 55th, 56th and 57th |
| [adjudication/](adjudication/00-read-me-first.md) | **Adjudication and appeals (added 14 Oct 2026):** procedure from DRC-01A to DRC-07 with year-wise deadlines, appeals/review/GSTAT/litigation, a court-proof checklist distilled from the case law, and a survey of model SCNs and orders |
| [registration/](registration/00-read-me-first.md) | **Registration (added 14 Oct 2026):** procedure for grant, amendment, suspension, cancellation and revocation (ss.22-30, rules 8-26), the proper officer (Range Superintendent), a court-proof checklist, CBIC sources; templates R1-R10 in gst-orders/templates |
| [case-law/](case-law/00-read-me-first.md) | **Case law (added 14 Oct, checked against judgment text 15 Oct 2026):** 359 judgments (293 read in full text) of the Supreme Court, High Courts (Telangana HC flagged binding), GSTAT and AAR across all GST domains, with where courts disagree. Single file: case-law/GST-case-law-compendium.md (and .docx); index: case-law/case-law-index.csv |
| [../gst-orders/](../gst-orders/refund-order-learnings.md) | **Practice: refund orders.** The refund drafting standard (refund-order-learnings.md), the evaluation of the division's speaking orders, and Word templates T1–T8, N1 (RFD-08) and checklist C1 in gst-orders/templates/ |
| [../refund-automation/plan.md](../refund-automation/plan.md) | Plan for the Refund Desk app that drafts refund orders from uploaded files (14 Oct 2026) |
| [06-sources-and-gaps.md](06-sources-and-gaps.md) | What was checked, what was blocked, what is missing |
| [text/](text/) | **Full current text** from CBIC: CGST, IGST, UTGST and Compensation Acts; CGST, IGST and Cess Rules |
| [data/](data/) | **Complete CBIC index as CSV:** 1,283 notifications, 272 circulars, 43 instructions, 39 orders, each with its CBIC link |

## The 57th Council (8 Oct 2026) in five lines
1. **Arrest power (s.69) to be omitted.** The prosecution threshold rises to ₹5 cr and the general penalty cap falls to ₹10,000.
2. **E-way bill checks** only on specific intelligence and only in the origin or destination State. No confiscation of goods in transit.
3. **Automation:**
   - Auto-accepted registration amendments and cancellations.
   - 90% automatic provisional refunds.
   - Refund of ITC on input services (from 1.11.2026) and on capital goods (from 1.4.2027).
4. **Returns redesign** from April 2027: GSTR-1 and GSTR-3B reconciliation, new ITC and RCM statements, and a credit-note time limit in IMS. E-invoicing extended to RCM purchases and imported services.
5. Several s.17(5) credit blocks removed. Small rate and classification fixes. 2% TDS plus RCM on scrap and e-waste.

**None of these is law until notified.**

## Why this matters for the project's goals

The data sources below are a starting map for the next step.
- **Leakage prevention:**
  - GSTR-1 against GSTR-2B against GSTR-3B mismatches (rules 88C and 88D).
  - Fake-ITC networks traced through the invoice graph.
  - Track and trace (s.148A) for evasion-prone goods.
  - The new 2% TDS and RCM on scrap, a sector prone to fake invoices.
- **Formalisation:** automatic registration (rules 14A and 14B), the ARQP scheme for small B2C traders, and e-invoicing reaching ₹5 cr businesses.
- **Trade facilitation:** automated refunds, removal of arrest, fewer e-way bill interceptions, and export changes in IGST ss.2(6), 13 and 16.
- **Supply chain and logistics:**
  - E-way bills (rule 138) and e-invoices (rule 48(4)) together record nearly every B2B goods movement above ₹50,000: origin, destination, HSN, value, vehicle and distance.
  - The new **Ship-to GSTIN** field in the e-way bill (live from 1.8.2026) improves the delivery-location data.
  - Linking these to customs ICEGATE data would give an end-to-end view of goods movement.

## Reliability note
- **From the official CBIC portal (12 Oct 2026):** the full text of the Acts and Rules, the complete notification and circular index, the 2025–26 rule amendments, and the Finance Act, 2026.
- **From official Council and PIB pages (earlier session):** meeting dates and links, and the 55th to 57th outcomes.
- **From the Council's signed minutes (12 Oct 2026):** decisions of meetings 1 to 54, each with its paragraph number. Twelve errors in the earlier summaries were corrected; the list is in [05-gst-council-meetings.md](05-gst-council-meetings.md).
- **Still from background knowledge:** some topic summaries in other files. These are marked where they appear.
- **Latest official items:** 02/2026-CT (7 May 2026), Circular 256 (25 Jul 2026), Instruction 01/2026-GST (3 Aug 2026). The Finance Act, 2026 changes to ss.15(3), 34 and 54 are not yet in force.
- **Open gaps:** see [06-sources-and-gaps.md](06-sources-and-gaps.md).
