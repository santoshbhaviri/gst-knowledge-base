# Refund orders (RFD-06): what to learn and what to fix

**Prepared:** 12 Oct 2026. **Covered:** 15 refund orders and one refund checklist uploaded to this project. All were checked against the CGST/IGST Acts and Rules in [gst-law/text/](../gst-law/text/) and the refund circulars and instructions downloaded from CBIC. These are notes for drafting. They are not a legal opinion.

The file names no taxpayers, GSTINs, or taxpayer amounts. Orders are referred to by label only:

| Label | Category | Outcome | Overall quality |
|---|---|---|---|
| 1, 2, 3, 5 | Inverted duty (own division) | Partly rejected | Sound result, weak template |
| 4 | Excess cash-ledger balance (own division) | Sanctioned | Wrong instrument used in the notice |
| 6 | SEZ supplies under LUT (own division) | Partly rejected | Good, some gaps |
| A | SEZ supplies under LUT | Sanctioned | Good structure, wrong relevant-date clause |
| B | Export of goods under LUT | Sanctioned | Good, minor gaps |
| C | Export of goods under LUT | Partly rejected | **Rejection not sustainable** (GSTR-2B point) |
| D | Excess cash-ledger balance | Sanctioned | Good, wrong section cited |
| E | Export of services with IGST paid | Sanctioned | **High risk**: hearing record and intermediary issue ignored |
| F | Export of services under LUT, with an s.74A demand | Partly rejected | Good model for combining refund rejection and demand |
| G | Inverted duty | Sanctioned | **Best model** of the fifteen |
| H | Export of services under LUT | Wholly rejected | **Rejection reasoning weak**: wrong test for place of supply |
| I | Export of services under LUT | Wholly rejected | **Rejection likely to fail**: sub-contracting treated as non-export |
| J | SEZ supplies with IGST paid | Sanctioned | Good verification; key rule 89(2)(f) point missed |
| K | Inverted duty | Partly rejected | Careful item-wise findings; arithmetic error on turnover |
| Checklist | Joint Commissioner's refund SOP and checklist (another zone) | — | Good risk checklist; folded into Part 5 |

---

## Part 1. The ten most important learnings

1. **Most errors come from a shared template, not from the officer's analysis.** The same wrong clauses repeat across divisions: s.54(8)(a) instead of (b), export-duty findings in non-export orders, the outdated appeal preamble, "(4A)/(4B)" wording, and the s.42(2) undertaking. Fix the template once per category and most of these disappear (Part 4).

2. **A rejection must stand on the ground that was put to the taxpayer.** In H and I, the notice raised general questions ("upload agreements", "it appears the recipient may be a distinct person"). The order then rejected on a new ground (service territory in H, an end client in the USA in I) that the taxpayer never had a chance to answer. Rule 92(3) requires the notice to state the reasons for rejection. If something new emerges from the reply, issue a further RFD-08 before deciding.

3. **Place of supply for services follows the recipient's location, not where the work is done.** Under IGST s.13(2), the default rule is the location of the recipient. Work done in India for a recipient abroad is still an export if s.2(6) is met.
   - **Order H** used "the services are performed in India" as the test. That is the wrong test.
   - **The right question** is whether a specific rule in s.13(3) to (13) applies. For periods up to 29.03.2026 that includes intermediary under s.13(8)(b), which was omitted from 30.03.2026 by the Finance Act 2026. Answer it using the three-party test in Circular 159/15/2021.
   - **Order I** rejected software development done for an affiliate's end client. Circular 159 para 3.5 and Illustration 2 call that a sub-contract on the supplier's own account, not an intermediary service. The contracting party abroad is the recipient (s.2(93)).
   - **Order E** had the opposite problem. It sanctioned "marketing and sales support" to a related foreign entity without asking the intermediary question at all.

4. **A refund order is not the place to deny ITC that appears in an earlier month's GSTR-2B.** Circular 197/09/2023 para 1.3 allows ITC on invoices in the 2B of the tax period "or any of the previous tax periods". Order C quoted this and then excluded the ITC anyway, and that exclusion caused the entire rejection. What to check instead:
   - the s.16(4) time limit;
   - that the same invoice has not been counted in two refund claims.

5. **Get the turnover definitions exactly right.** Three orders lost or gave away money on definitions:
   - **Order K:** took Adjusted Total Turnover from GSTR-3B including exempt supplies. Rule 89(4)(E)(i) excludes exempt supplies, so the refund came out lower than it should have.
   - **Order B:** left Adjusted Total Turnover at invoice value. The rule 89(4) Explanation (Notification 14/2022) and Circulars 147/03/2021 para 4 and 197/09/2023 para 3.3 require the lower of FOB and invoice value in Adjusted Total Turnover too.
   - **Orders 2 and 5:** took different parts of the formula from different sources (RFD-01 for one, GSTR-1/3B for another), always in the direction that reduced the refund.

6. **Capital goods ITC is not "ineligible ITC".** It is left out of refund because "Net ITC" in rule 89(4)(B) and 89(5) covers only inputs (and input services in 89(4)). Orders H, J and K disallowed it "under s.16(3)". That section is about depreciation claimed under the Income-tax Act, so it is the wrong provision. Calling the credit ineligible also invites a wrong reversal demand later.
   - **Wording to use:** "excluded from Net ITC as capital goods; ITC remains in the ledger".
   - **Note:** the 57th Council recommended allowing capital-goods ITC in refunds from 1.4.2027. It is not law yet.

7. **Every partly or wholly rejected ITC refund needs a PMT-03 re-credit direction (rule 93(2)).** None of the fifteen orders had one. Only Order C conditioned re-credit on the taxpayer's undertaking not to appeal. Without the direction, the taxpayer permanently loses credit that the law says must come back.

8. **Provisional refund must be dealt with in every zero-rated order.** From 01.10.2025, inverted-duty claims must be dealt with too (Instruction 06/2025-GST para 5.1).
   - **Rule:** rule 91(2), as amended by Notification 13/2025-CT, gives 90% provisional refund in RFD-04 within 7 days.
   - **Exception:** the officer may deny it only with reasons recorded. Notification 14/2025-CT lists the persons excluded.
   - **What the orders did:**
     - Six zero-rated orders (6, B, E, H, I, J) were silent on provisional refund.
     - Order A paid 70% with no reason given.
     - Only A and B adjusted an earlier RFD-04.
   - **Correction to the earlier review:** the inverted-duty Orders 1, 2 and 5 were filed after 01.10.2025. They should also have recorded the RFD-04 or the reason it was not given. The [batch-1 review](../refund-review/rfd06-review-2026-10-12.md) missed this.

9. **Order G is the model to copy for structure.** Its features:
   - each notice point has its own reply and its own finding;
   - a rate-wise outward-supply table taken from GSTR-1;
   - an explicit inversion finding giving input rates against output HSN and rates;
   - capital goods versus inputs decided on facts;
   - SEZ supplies kept out of inverted turnover;
   - a Part A/Part B formula table;
   - a correctly worded s.107(6) preamble;
   - an arrears check.

   Order F is the model for a rejection that also needs a demand. It uses one RFD-08 under s.54 read with s.74A (Circular 125/44/2019 paras 20–24), and drops interest because the credit balance never fell below the disputed amount (s.50(3)).

10. **Small clerical errors are what an appellate authority notices first.** Examples from these orders:
    - amounts in paise (s.170 requires rounding to the rupee);
    - blank dates ("…06.2026", "SCN xxxx dt. …");
    - two different filing dates in the same order;
    - an acknowledgement dated a year before the application (Order K);
    - find-and-replace damage (Order E);
    - duplicated paragraph numbers;
    - a personal e-mail address in the letterhead;
    - names of individual employees, the CA and authorised representatives (Orders I, J, K) that the order does not need.

---

## Part 2. Good practices to keep

**Structure and fairness**
- One numbered finding per notice point, with the taxpayer's reply summarised first (G, K, F).
- Concessions recorded clearly, e.g. "accepted as ineligible by the applicant at para … of the reply" (K, I).
- Personal hearing record stated, with who attended (D, G, J, K).
- A sanction table showing claimed, inadmissible, provisional already paid, adjustment and net payable (A, B, D).
- Copies marked to Review, Post-Audit and Adjudication (B).

**Verification that should become routine**
- ICEGATE: shipping bill and EGM checked, and FOB compared with invoice value (B, C).
- SEZ: endorsement checked on SEZ Online, the Letter of Approval checked against the goods, and payment received from the SEZ unit matched to invoices (J, A).
- Services:
  - the five s.2(6) conditions set out in a table (E, F);
  - "turnover of zero-rated services" built from payments received, as A + B − C (H, I);
  - bank-issued FIRAs accepted (F);
  - turnover outside the period removed from both numerator and denominator (F).
- ITC: questioned invoices checked against the actual invoice description and HSN before deciding (K, J). The ITC in the claim is confirmed to be in GSTR-2B (K para 14(f)), and the ledger debit is confirmed (K para 14(e)).
- Arrears and appeals: demands under appeal with pre-deposit treated as stayed under s.107(7) and not adjusted (D); arrears checked before sanction (A, G).

**Law applied well**
- Rule 28 (related-person) valuation reasoning for cross-charges (E).
- Consistency with past orders for the same taxpayer (E).
- s.50(3) interest reasoning on ineligible ITC that was never utilised (F).
- The notice asked for the payment-based A + B − C table for services. Keep that.

---

## Part 3. Mistakes to avoid, by type

### 3.1 Law and jurisdiction
| Mistake | Seen in | Correct position |
|---|---|---|
| s.54(8)(a) (export) quoted for an inverted-duty refund | 1, 2, 3, 5, K | s.54(8)(b): unutilised ITC under s.54(3) |
| "s.54(8)(i)" quoted, with text that is not in the statute | E | s.54(8)(a) |
| s.54(3) quoted for a cash-ledger refund | D | s.49(6) read with s.54(1) |
| s.54(3) (unutilised ITC) quoted for a refund of IGST paid | J | s.54(1) with IGST s.16(4) and Notification 01/2023-IT (s.16(3)(b) before 01.10.2023), and rule 89(2)(d)/(e) |
| Relevant date taken from export-of-goods clauses for SEZ or services | A, F | SEZ: clause (ba), the due date of the return. Services: clause (c), the date payment was received (or invoice date if paid in advance). Inverted duty: clause (e). |
| Relevant date quoted with the old "end of financial year" wording | F | Use the current Explanation 2 text |
| "Rule 96" applied to a services refund | E | Rule 96 is only for IGST paid on exported goods; services go under rule 89 |
| Rejection under "rule 92(1)" | H, K | Rule 92(1) is for sanction; rejection after notice is under rule 92(3) |
| Capital goods disallowed "u/s 16(3)" | H, J, K | Excluded from Net ITC by definition (Part 1, point 6) |
| Other business ITC disallowed "u/s 16(3)" | K | s.16(1) or s.17(5), whichever actually applies |
| Business air travel disallowed under s.17(5) for lack of "internal approvals" or copies of invoices | F, K | s.17(5)(b)(iii) blocks only travel benefits to employees on vacation (LTC or home travel). Business travel is not blocked. The invoice is already in GSTR-2B, so ask what the trip was for rather than for paperwork. |
| SEZ supply with tax relied on the SEZ unit's declaration that it took no ITC | J | Current rule 89(2)(f) (substituted w.e.f. 23.10.2017) needs a declaration that **tax was not collected from the SEZ unit**. The order should record whether the payment received included the IGST. If it did, refunding the tax to the supplier is unjust enrichment. |
| "Services territory is India", so place of supply is in India | H | Default is the recipient's location (s.13(2)); test intermediary separately (Part 1, point 3) |
| Sub-contracted software work treated as not an export | I | Circular 159/15/2021 para 3.5 and Illustration 2 |
| Intermediary status not examined for marketing support to a foreign affiliate | E | Examine it under s.13(8)(b) for periods up to 29.03.2026 |
| Rate-based outputs not checked for inverted duty | 1, 2, 3, 5 | Record input and output rates with HSN, and confirm the output is not excluded by Notification 5/2017-CT(R) |

### 3.2 Computation
| Mistake | Seen in | Fix |
|---|---|---|
| ITC in an earlier month's 2B excluded | C | Circular 197 para 1.3 allows it |
| Adjusted Total Turnover includes exempt supplies | K | Exclude them (rule 89(4)(E)(i)) |
| Adjusted Total Turnover at invoice value for exports | B | Use the lower of FOB and invoice value (rule 89(4) Explanation) |
| Mixed sources for the parts of the formula | 2, 5 | One stated source per component, the same for all components where possible |
| "Tax payable on inverted supplies" adopted with no working | 1, 2, 3, 5, K | Give a rate-wise table from GSTR-1. In K, the Statement-1 figure and the figure in the order differ, and the order does not explain why. |
| Zero-rated formula printed under a rule 89(5) heading | 1 | Print the correct formula with the figures substituted |
| Amounts in paise | 2, A, G | Round to the rupee (s.170) |
| An ITC amount and its refund effect mixed up | 6 | Say "ITC of ₹x excluded, which reduces the refund by ₹y" |
| Large gaps between GSTR-1, GSTR-3B and RFD-01 left unexplained | 3, 6, C, G | Record the reconciliation, or the reason it is accepted |

### 3.3 Procedure
| Mistake | Seen in | Fix |
|---|---|---|
| No PMT-03 re-credit direction | All partial or whole rejections except C | Direct re-credit under rule 93(2) after the undertaking or the end of the appeal period |
| Provisional refund not mentioned | 1, 2, 5, 6, B, E, H, I, J | Record the RFD-04 and adjust it, or record the reason it was denied |
| Provisional refund at 70% | A | 90% (rule 91(2)) |
| An unpaid or "apparent" liability handled by rejection in RFD-08 | 4, D | Use s.54(10)/(11) and withhold in RFD-07 (rule 92(2)). This applies only to confirmed dues that are not stayed. |
| A demand set aside in appeal still treated as due | 4 | Check appeal outcomes before any withholding |
| 10 days given to reply to RFD-08 | E | 15 days (rule 92(3)) |
| A demand mixed into the refund notice without a clean decision | E | Decide each proposal separately, as F does |
| FIRAs filed with the RFD-09 reply ignored because they were not in Statement-3 | F | Consider them; that is what the reply is for |
| CA certificate under rule 89(2)(m) asked for in an ITC refund | 6, G | Not needed for s.54(8)(a)–(d) and (f) cases (proviso to rule 89(2)(m)) |
| Indemnity bond on stamp paper asked for | J | No basis in s.54, rule 89 or Circular 125 (which lists the documents) |
| ITC eligibility examined in a "tax paid" refund category | J | Refund of tax paid does not depend on ITC. Refer any ITC concern for s.73/74A action. |
| A whole rejection on "not an export", with no word on the tax that would then be due | H | If the supply is held to be domestic, refer it for a demand, so the department's stand stays consistent |
| Limitation checked on one shipping bill or not at all | C, H, I | Check each shipping bill (goods) or each remittance (services) |
| Notice points left without a finding | H (ITC points) | Every notice point needs a finding, even when it becomes moot |
| A hearing statement ignored | E | Deal with every statement made at the hearing |
| Template notice asserting facts ("no endorsements", "invoices not found") | J | Raise only what was actually found |
| Order issued on day 59 of 60, with no record of the 60-day count | B | Record the date the complete application was received and the 60-day date; interest runs under s.56 after that |

### 3.4 Drafting
- **Appeal preamble.** It should say:
  - APL-01 is filed **electronically** (rule 108), not in duplicate, and there is no court fee;
  - pre-deposit is the admitted amount in full plus 10% of the **tax** in dispute, capped at ₹20 crore, or 10% of the penalty in a penalty-only order (s.107(6));
  - the name of the appellate authority, given consistently.
- **Outdated wording to remove:**
  - "(4A)/(4B)" in the Adjusted Total Turnover definition, outdated since Notification 20/2024;
  - the s.42(2) undertaking and the GSTR-2A copy, both dropped by Circular 197 para 2;
  - "Notification 125/44/2019"; it is a Circular.
- **Findings that belong only in export orders** ("goods exported are not subject to export duty", "verified with ICEGATE") must not appear in inverted-duty, SEZ or cash-ledger orders (1, 2, 3, 5, 6, J, K).
- **No unneeded names.** Leave out personal names of employees, CAs and representatives, and the names of third-party suppliers unless a finding needs them.
- **Before signing, check for leftovers:** placeholder text (xxxx, …), blank dates, another taxpayer's period ("June-26" in an order for a different period), and duplicated paragraph numbers.

---

## Part 4. Drafting standard by refund category

Every order follows the same skeleton (Part 4.0). Each category then adds its own legal basis, formula and mandatory findings.

### 4.0 Common skeleton
1. **Heading:** RFD-06 [rule 92(1), (3), (4), (5), 96(7)], with the order number and date filled in, and the official e-mail only.
2. **Claim details:**
   - ARN and the filing date; the date RFD-02 was issued; the date the application was complete (for the 60-day count);
   - category and period;
   - amount by tax head.
3. **Legal basis:** the specific sub-sections and rules for the category (below), and nothing copied from other categories.
4. **Limitation:** the relevant-date clause by name, the actual relevant date(s), the two-year date and the filing date. For goods, give this per shipping bill; for services, per remittance.
5. **Provisional refund:** the RFD-04 number, date and amount, or the reason recorded for denying it (rule 91(2) proviso). It is not applicable to the cash-ledger and "tax paid on SEZ" categories outside s.54(6).
6. **Documents filed:** list only what the law or circular requires for this category.
7. **The notice:** date, each point numbered, and the 15-day reply period.
8. **The reply:** date, summarised point by point.
9. **Personal hearing:** date and who attended. If no one came, record how many opportunities were given.
10. **Findings:** one paragraph per notice point, each with the reply, the verification done, a conclusion and the section relied on.
11. **Computation:**
    - the formula with the figures substituted;
    - a table with the source of each figure;
    - the result rounded under s.170;
    - the inadmissible amount explained as "ITC excluded ₹x, refund effect ₹y".
12. **Statutory findings:**
    - no duplicate claim in any category;
    - ledger debit confirmed (rule 89(3));
    - ITC in GSTR-2B of the period or an earlier period (Circular 197 para 1.3);
    - the correct unjust-enrichment clause (s.54(8));
    - s.54(10) dues: confirmed dues not stayed, checked against appeal outcomes;
    - the s.54(3) provisos only where relevant.
13. **Sanction table:**
    - claimed; inadmissible; provisional already paid; adjusted under s.54(10) via RFD-07; net payable;
    - interest under s.56, if the order is passed after 60 days.
14. **The order:**
    - sanction under rule 92(1);
    - rejection under rule 92(3), with the specific ground;
    - a PMT-03 re-credit direction under rule 93(2) for rejected ITC;
    - a demand (DRC-07) only if proposed in the notice.
15. **Appeal clause:** the corrected text (Part 3.4).
16. **Copies:** to the taxpayer, Review, Post-Audit, the Adjudication cell (if a demand is involved), and the file.

### 4.1 Inverted duty structure
- **Basis:**
  - s.54(3)(ii);
  - rule 89(5) as amended by Notification 14/2022;
  - unjust enrichment: s.54(8)(b);
  - relevant date: clause (e), the due date of the GSTR-3B for the period.
- **Mandatory findings:**
  - a rate-wise table of inputs (rate, ITC) and outputs (HSN, rate, value) showing the inversion actually exists;
  - the outputs are not excluded by Notification 5/2017-CT(R), or other notifications covered by Circular 173/05/2022;
  - outputs at the same or a higher rate are kept out of inverted turnover, but kept in Adjusted Total Turnover; say so;
  - SEZ and export supplies kept out of inverted turnover;
  - capital goods and input services kept out of Net ITC (inputs only), but input services kept in "ITC on inputs and input services" (the Part B denominator);
  - "tax payable on inverted supplies" derived from GSTR-1, rate-wise.
- **Watch:** exempt supplies are excluded from Adjusted Total Turnover; inputs bought at the same rate as the output do not create inversion.
- **Provisional refund:** 90% for claims filed on or after 01.10.2025 (Instruction 06/2025 para 5.1).
- **Coming changes:**
  - Finance Act 2026 s.155 (inverted duty brought into s.54(6)) is not yet in force;
  - the 57th Council recommended refund of input-service ITC from 1.11.2026. Not law until notified.

### 4.2 Export of goods without tax (LUT)
- **Basis:**
  - s.54(3)(i); IGST s.16(3)(a); rule 89(4); rule 96A (LUT);
  - unjust enrichment: s.54(8)(a);
  - relevant date: clause (a), the date the ship or aircraft left (EGM date as evidence), checked per shipping bill.
- **Mandatory findings:**
  - LUT valid for the period;
  - ICEGATE shipping bill and EGM;
  - zero-rated value is the lower of FOB and invoice value, and **the same restricted value is used in Adjusted Total Turnover**;
  - zero-rated value also capped at 1.5 times the value of like domestic goods (rule 89(4)(C));
  - no duty drawback of central tax (s.54(3) third proviso);
  - realisation of export proceeds is **not** a precondition for an export-of-goods refund (Circular 125 para 48). Rule 96B applies only after the refund, to recover it if proceeds are not realised within the FEMA period. Do not ask for BRCs for goods. *(Corrected 12 Oct 2026.)*
  - Net ITC covers inputs and input services, and ITC in an earlier month's 2B is allowed.
- **Watch:** shipments split across the limitation date; GSTR-1 export turnover against 3B; switching between with-tax and LUT exports (a risk flag in the checklist).

### 4.3 Export of services without tax (LUT)
- **Basis:**
  - s.54(3)(i); IGST s.2(6), s.13 and s.16(3)(a); rule 89(4)(D);
  - unjust enrichment: s.54(8)(a);
  - relevant date: clause (c), checked per remittance.
- **Mandatory findings:**
  - **the s.2(6) table**, all five conditions;
  - **place of supply by the s.13 rule that applies.** Default is s.13(2), the recipient's location. Then test s.13(3) (performance-based) and, for periods up to 29.03.2026, s.13(8)(b) (intermediary) on the three-party test in Circular 159/15/2021. Sub-contracting is not intermediary.
  - Where the services are mixed (for example R&D, support and sales promotion), split them and decide each part;
  - payments received during the period (the A + B − C table);
  - FIRA/BRC matched to invoices, including FIRAs filed with the RFD-09 reply;
  - recipient and supplier not merely establishments of a distinct person (Explanation 1 to IGST s.8);
  - Circular 202/14/2023 on s.2(6)(iv) where payment is through special rupee accounts.
- **If the order holds the supply is not an export:** say what follows. The supply is a taxable domestic supply, so refer it for a demand. Re-credit the ITC through PMT-03, because the ITC itself was not found ineligible.

### 4.4 Export of services with IGST paid
- **Basis:**
  - s.54(1); IGST s.16(4) with Notification 01/2023-IT (s.16(3)(b) before 01.10.2023); rule 89(2)(c);
  - unjust enrichment: s.54(8)(a);
  - relevant date: clause (c).
- **Mandatory findings:**
  - the same s.2(6) and place-of-supply findings as 4.3;
  - IGST actually paid and shown in GSTR-3B and GSTR-1 (table 6A);
  - every statement made at the hearing dealt with;
  - for related-party cross-charges, valuation under rule 28.
- **Watch:** Rule 96 does not apply to services.

### 4.5 Supplies to SEZ under LUT (unutilised ITC)
- **Basis:**
  - IGST s.16(1)(b) and s.16(3) (clause (a) before 01.10.2023); rule 96A(6); rule 89(4);
  - unjust enrichment: s.54(8)(b), not (a): since 01.02.2019 clause (a) covers only exports, and a supply to an SEZ is not an export *(corrected 12 Oct 2026)*;
  - relevant date: **clause (ba)**, the due date of the return for the period.
- **Mandatory findings:**
  - specified officer's endorsement on every invoice, checked on SEZ Online (second proviso to rule 89(1), rule 89(2)(d)/(e));
  - goods or services covered by the SEZ unit's authorised operations;
  - provisional refund dealt with;
  - **no rule 89(2)(m) CA certificate.**

### 4.6 Supplies to SEZ with IGST paid
- **Basis:** s.54(1); IGST s.16(4) with Notification 01/2023-IT as amended by 05/2023-IT; rule 89(2)(d), (e) and **(f)**; relevant date: clause (ba). Payment to the applicant is under **s.54(8)(e)**, so the rule 89(2)(l) declaration (up to ₹2 lakh) or (m) CA certificate is **required** (Circular 125 Annexure A, S. No. 4) *(corrected 12 Oct 2026)*.
- **Mandatory findings:**
  - endorsement and authorised operations, as in 4.5;
  - a rule 89(2)(f) declaration that **tax was not collected from the SEZ unit**, checked against the payment the SEZ unit actually made;
  - the IGST shown in 3B against the zero-rated invoices.
- **Do not:** examine ITC eligibility, or ask for Annexure-B or indemnity bonds.

> **Note added 12 Oct 2026:** the template orders built from this standard are in /mnt/project-files/gst-orders/templates/ (start with 00-read-me-first). Where this file and the templates differ, the templates are the later, reviewed version. Two further corrections from that review: a section 54(10)(b) adjustment is shown in the RFD-06 itself (rule 92(1); Circular 125 para 35), with RFD-07 used only for withholding; and Notification 14/2025-CT is issued under s.54(6), while rule 91(1) is the separate non-prosecution bar.

### 4.7 Excess balance in the electronic cash ledger
- **Basis:** s.49(6) read with s.54(1); not s.54(3), and not "Net ITC". Relevant date: no clause is specific to this category. If limitation is discussed, cite the residual clause (h) of Explanation 2.
- **Mandatory findings:**
  - the source of the cash balance (the checklist asks why cash accumulated);
  - confirmed dues not stayed (pre-deposit verified for each demand ID under appeal);
  - any adjustment made only through s.54(10)/(11) and RFD-07, never by rejection.

### 4.8 Wholly rejected orders (any category)
- The ground of rejection must be the ground stated in the RFD-08.
- Decide every notice point, including those that become moot.
- Give the specific rule: rule 92(3).
- Direct PMT-03 re-credit, conditioned on the undertaking or the end of the appeal period.
- State the consequence for tax liability, if any, and refer it.
- Make sure the hearing record shows a real opportunity. If the taxpayer did not attend once, consider a second date before deciding a large claim against them.

---

## Part 5. Pre-signing checklist

This combines the review findings with the Joint Commissioner's refund SOP and checklist from another zone.

**Before issuing RFD-08**
- [ ] Relevant date and limitation checked for each shipping bill or remittance.
- [ ] Debit entry in the credit or cash ledger confirmed; no claim for the same period in another category.
- [ ] GSTR-2B check run against the period and earlier periods; s.17(5) and s.16(4) checks done.
- [ ] Supplier risk:
  - supplier-wise ITC concentration checked (verify suppliers who make up 35–40% or more of the ITC);
  - cancelled or non-filing suppliers checked;
  - investigations checked on DIGIT;
  - sample e-way bill and toll-plaza checks for goods.
- [ ] Category checks:
  - **inverted duty:** rate table, Notification 5/2017-CT(R), manufacturing process;
  - **goods exports:** ICEGATE, FOB/invoice, drawback, red flags;
  - **services:** agreement, s.13 rule, intermediary test, FIRAs;
  - **SEZ:** endorsements, authorised operations, rule 89(2)(f);
  - **cash ledger:** source of the balance.
- [ ] s.54(10) dues: confirmed, not stayed, and checked against the latest appeal orders.
- [ ] Physical verification for first-time or dormant registrations, high-risk goods, or claims out of proportion to the business.
- [ ] Each notice point says exactly why the amount appears inadmissible and what will settle it; reply time is 15 days.

**Before signing RFD-06**
- [ ] Every notice point and every hearing statement has a finding.
- [ ] Provisional refund recorded or the denial reasoned; RFD-04 adjusted in the sanction table.
- [ ] Formula printed correctly for the category, with figures substituted, a source for every figure, and rounding to the rupee.
- [ ] Correct s.54(8) clause; no findings copied from other categories.
- [ ] PMT-03 re-credit direction for rejected ITC; demand only if proposed in the notice.
- [ ] Day count within 60 days of the complete application, or interest under s.56 added.
- [ ] Appeal clause is the corrected text.
- [ ] All dates filled and consistent; no placeholders; no paise; no unneeded personal names; official e-mail only.
- [ ] Copies to Review and Post-Audit.

---

## Part 6. What to expect next

These are recommendations of the 57th GST Council (8 Oct 2026). None is law until notified.
- Refund of **input-service** ITC in inverted duty from 1.11.2026.
- Refund of **capital-goods** ITC from 1.4.2027.
- 90% automatic provisional refund based on risk scoring.

The Part B denominator and the "Net ITC" definitions in this standard will need updating when these are notified. Large accumulated credit balances, noted in the batch-1 review, become a revenue risk once these refunds open.

---

## Part 7. Two further orders (L, M), added 12 Oct 2026

| Label | Category | Outcome |
|---|---|---|
| L | SEZ supplies of services under LUT (unutilised ITC) | Sanctioned, with a small amount inadmissible |
| M | SEZ supplies of goods under LUT (unutilised ITC) | Sanctioned, with part inadmissible |

Both orders come from one division and use the same template. They were decided within about 40 days of filing, and the arithmetic in both checks out exactly.

### 7.1 What is new and better than the earlier 15
1. **A "Verification and methodology of computation" section.** For each figure in the formula (zero-rated turnover, Adjusted Total Turnover, Net ITC), there is a table comparing GSTR-1, GSTR-3B, RFD-01 and the supporting documents, and naming the figure adopted. None of the earlier orders showed the sources this clearly. **Adopt this format in the standard.**
2. **Services turnover is built from payments actually received** (rule 89(4)(D)). Bank statements were matched to invoices, and TDS deducted by the recipient was counted as received (L). This is the right reading of the rule.
3. **Inadmissible ITC is set out by reason and by tax head** (credit notes, capital goods, earlier-period invoices, s.17(5)) in a single table (M).
4. **Capital goods are called "inadmissible for refund", not "ineligible ITC"** (M). That is better than H, J and K.
5. **A full record of the procedure:**
   - RFD-08 reference number and date;
   - date of the reply;
   - hearing attended, or waived in writing;
   - the date of the jurisdictional range's no-arrears confirmation;
   - the LUT reference for each financial year;
   - local Standing Orders and Instruction 03/2022 cited;
   - speaking-order number, file number, official e-mail, dated signature, and a copy to Review.
6. **Limitation is tested on the earliest month of the claim, under the SEZ clause (ba)**, which is the binding month.

### 7.2 What is still wrong (mostly carried over from the template)
1. **"Highest Adjusted Total Turnover, lowest zero-rated turnover" is stated as a rule. It is not one.** Both orders say that, under the formula, "the highest of these three figures is to be taken" for Adjusted Total Turnover. Neither rule 89(4) nor Circular 125 says this. Taking the lowest numerator and the highest denominator always reduces the refund, and an appellate authority will see that.
   - **In L this is also wrong on the text of the rule.** Adjusted Total Turnover includes "turnover of zero-rated supply of services determined in terms of clause (D)", which is the realised value. The order cut the numerator to the realised value but left the invoice-based figure in the denominator. Para 13.1 says the denominator was "proportionately recomputed", but the table shows it was not.
   - **Effect in L:** using the GSTR-3B turnover reduced by the same realisation shortfall gives a refund about ₹62,000 higher.
   - **Effect in M:** using GSTR-3B (the taxpayer explained why it differs from GSTR-1) gives a refund about ₹3,000 higher.
   - **Recommended rule:** take each component from the returns for the period, reconciled. Use the same zero-rated value in the numerator and inside Adjusted Total Turnover. Explain any figure taken from RFD-01 instead.
2. **Net ITC in M may have been reduced twice.** The inadmissible items were found in Annexure-B, whose total is higher than the RFD-01 Net ITC. They were then deducted from the lower RFD-01 figure. If any of them were already left out of the RFD-01 figure, they have been deducted twice. The gap between the two figures (about ₹3.4 lakh of ITC, worth up to about ₹79,000 of refund) should be reconciled, and the order should say so.
3. **The "invoices prior to April 2025" ground (M)** is the same point as Order C. ITC on earlier-dated invoices that was *availed* in the claim period is allowed (Circular 197 para 1.3, subject to s.16(4)). The taxpayer agreed to the exclusion, but the standard ground should be "ITC availed in an earlier tax period", not "invoice dated before the period".
4. **No provisional refund.** Both are zero-rated claims filed in May 2026, so 90% in RFD-04 within 7 days was due under rule 91(2), or reasons had to be recorded. M is a ₹3.8 crore claim. This is the most significant gap in both orders.
5. **No formal rejection and no PMT-03.** The findings say the balance "is liable for rejection", but the operative ORDER only sanctions. It should also reject the balance under rule 92(3) and direct re-credit under rule 93(2) after the undertaking or the end of the appeal period.
6. **Template leftovers:**
   - the same outdated appeal preamble ("10% of the duty", "duplicate", "court fee/stamp duty");
   - "s.54(14)(ba)" instead of clause (ba) of Explanation 2 to s.54;
   - para 9 lists "Statement 3 under rule 89(2)(h)" and "Statement 3A", which belong to other categories (SEZ claims use Statements 5 and 5A);
   - L para 11 speaks of "receipt of goods" in a services claim;
   - L para 13.1 says "Net ITC has been recomputed after excluding the inadmissible ITC", but no ITC was excluded in L.
7. **Unjust enrichment** is dismissed in one line with no clause. Cite s.54(8)(b), refund of unutilised ITC under s.54(3).
8. **Limitation** refers to the date the return was "filed". The relevant date is the *due* date of the return. Here the two dates are the same, so it should simply say "due date".
9. **Clerical points:**
   - M's ORDER quotes the GSTIN where the ARN should be;
   - M's RFD-08 carries the same date as the application (check this);
   - L's order is dated 10.07.2026 but the signature is dated 18.07.2026;
   - M's zero-rated turnover in GSTR-1/3B is ₹69 lakh above RFD-01, and the difference is not explained (supplies not yet endorsed, or a later claim?).

---

## Part 8. New lessons from the officer's own 18 speaking orders (12 Oct 2026)
Full ratings and feedback for each order: [speaking-orders-evaluation.md](speaking-orders-evaluation.md). New points to add to the standard:
- **New category: refund of appeal pre-deposit.**
  - Interest is payable under s.115 at 6% from the date of payment to the date of refund. Compute it in the order.
  - Relevant date is clause (d) of Explanation 2, the date of communication of the appellate order. Do not cite s.54(2).
  - Unjust enrichment: s.54(8)(e).
  - Record whether the department has appealed the order-in-appeal, and whether withholding under s.54(11) applies.
  - Cash part under s.54 with rule 92(1A)/(4); the re-credit part by PMT-03.
- **Inverted duty, Part B denominator.** Split ITC into inputs, input services, capital goods and blocked credit, reconciled to GSTR-3B. An unexplained gap between the denominator and Net ITC can make the refund too high.
- **Ledger-balance cap.** The refund cannot exceed the electronic credit ledger balance at the end of the period or at filing. Show the balance in each tax head at both dates, and cite the source of the rule.
- **Deemed exports and SEZ supplies.** Check every month for them and take them out of inverted turnover. They are separate refund categories.
- **One taxpayer, consecutive months.** Apply the same checks every month.
- **Before signing, all four figures must agree:** computed amount, head-wise split, ORDER in figures, ORDER in words.
- **Excess cash ledger.** Where a deposit was made by mistake (for example under the wrong GSTIN), record whose funds paid it.
