# Adjudication under the CGST Act: step-by-step guide for the adjudicating officer

**Law as it stands on 14 October 2026.** Written for the Assistant Commissioner, CGST, Sangareddy Division (Medchal Commissionerate, Telangana), who issues show cause notices (SCNs) and passes orders-in-original.

**How to read this file**
- Every statement gives its source: section (s.), rule (r.), circular (Circ.), instruction (Instr.) or notification (Notf.).
- Section and rule text was read from `text/cgst-act.md` and `text/cgst-rules.md` (current CBIC text). Circulars, instructions and notifications marked **[read]** were downloaded from the CBIC portal and read in full for this file.
- Case pointers lead to the project's case-law files. **All case entries there are "Secondary"** (built from search summaries, not the judgment text). Read the judgment before quoting it in an order.
- Binding force: **SC** = Supreme Court, binds everyone. **TG-BINDING** = Telangana High Court, **BINDING IN TELANGANA**. **Persuasive** = other High Courts, GSTAT.
- **Not law yet:** the 57th GST Council recommendations (8 Oct 2026) and the uncommenced parts of the Finance Act, 2026 (see `01-acts.md`). Nothing in this guide depends on them.

---

## Part A. Two one-page tables

### A1. Timeline: what happens when

| # | Step | Time limit | Source |
|---|---|---|---|
| 1 | Scrutiny notice ASMT-10 | Reply within 30 days, or longer if allowed | s.61(1), (3); r.99(1) |
| 2 | Audit findings ADT-02 | Within 30 days of the end of the audit; audit itself within 3 months of its start | s.65(4), (6); r.101(5) |
| 3 | Pre-SCN intimation DRC-01A (optional since 15.10.2020) | No statutory period; give a reasonable reply time and wait for it to expire | r.142(1A), (2A); Notf. 79/2020-CT |
| 4 | Voluntary payment before the SCN (DRC-03) | Any time before the SCN is served | s.73(5); s.74(5); s.74A(8)(i), (9)(i); r.142(2) |
| 5 | **SCN under s.73** (FY up to 2023-24, no fraud) | At least **3 months before** the s.73(10) order deadline | s.73(2) |
| 6 | **SCN under s.74** (FY up to 2023-24, fraud) | At least **6 months before** the s.74(10) order deadline | s.74(2) |
| 7 | **SCN under s.74A** (FY 2024-25 onwards) | Within **42 months** of the due date of the annual return (or of the erroneous refund) | s.74A(2) |
| 8 | Payment that closes the case after the SCN | s.73: 30 days of the SCN. s.74: 30 days of the SCN. s.74A: **60 days** of the SCN | s.73(8); s.74(8); s.74A(8)(ii), (9)(ii) |
| 9 | Reply (DRC-06) and personal hearing | Hearing **compulsory** before any adverse order. At most **3 adjournments** | s.75(4), (5); r.142(4) |
| 10 | **Order under s.73** | **3 years** from the due date of the annual return for that FY (or of the erroneous refund) | s.73(10) |
| 11 | **Order under s.74** | **5 years** from the same date | s.74(10) |
| 12 | **Order under s.74A** | **12 months** from the SCN, extendable by **up to 6 months** by the Commissioner (or an authorised officer not below Joint Commissioner, senior to you), **before** the 12 months expire, with recorded reasons | s.74A(7) |
| 13 | No order by the deadline | Proceedings are **deemed concluded** | s.75(10) |
| 14 | Order after an appeal or court direction | Within **2 years** of communication of the direction | s.75(3); Circ. 185/17/2022 [read] |
| 15 | Order on a s.76 notice (tax collected, not paid) | Within **1 year** of the notice | s.76(6) |
| 16 | Reduced penalty after the order (fraud cases) | s.74: 50% within 30 days of communication of the order. s.74A: 50% within **60 days** | s.74(11); s.74A(9)(iii) |
| 17 | Rectification | Error brought to notice within 3 months of the order; no rectification after 6 months (except clerical or arithmetical errors) | s.161 |
| 18 | Payment of the confirmed demand | Within **3 months** of service of the order; a shorter period only for recorded reasons | s.78; Instr. 01/2024-GST [read] |
| 19 | Appeal by the taxpayer | 3 months from communication, plus 1 month for sufficient cause | s.107(1), (4) |
| 20 | Departmental review | Commissioner may direct an appeal within 6 months of communication | s.107(2) |
| 21 | Provisional attachment | Lapses automatically after **1 year** | s.83(2); r.159(2) |

### A2. Forms used in demand and recovery (all in Chapter XVIII of the CGST Rules)

| Form | What it is | Who files or issues it | Rule |
|---|---|---|---|
| ASMT-10 / 11 / 12 | Scrutiny notice / taxpayer's reply / acceptance of reply | Officer / taxpayer / officer | r.99 |
| ADT-01 / ADT-02 | Audit notice / audit findings | Officer | r.101 |
| DRC-01 | **Summary of the SCN**, served electronically **with** the SCN under s.52, 73, 74, 74A, 76, 122, 123, 124, 125, 127, 129 or 130 | Officer | r.142(1)(a) |
| DRC-01A | Pre-SCN intimation. Part A: officer's ascertainment. Part B: taxpayer's payment or submissions. Part C: officer accepts payment or submissions | Officer / taxpayer | r.142(1A), (2A) |
| DRC-01B, DRC-01C | Intimations on GSTR-1 vs GSTR-3B liability gap, and on ITC in GSTR-3B vs GSTR-2B gap | Portal / officer | r.88C, r.88D |
| DRC-01D | Intimation of self-assessed tax or interest recoverable under s.79 (pay within 7 days); treated as the recovery notice | Officer | r.142B |
| DRC-02 | Summary of a **statement** under s.73(3), 74(3) or 74A(3) for further periods | Officer | r.142(1)(b) |
| DRC-03 | Taxpayer's intimation of a voluntary payment, or a payment made within the post-SCN window | Taxpayer | r.142(2), (3) |
| DRC-03A | Taxpayer's application to link a DRC-03 payment to a demand already in the liability register | Taxpayer | r.142(2B) |
| DRC-04 | Acknowledgement of a DRC-03 payment | Portal | r.142(2) |
| DRC-05 | Intimation **concluding** proceedings after payment within the SCN window (or within 7 days of a s.129(3) notice) | Officer | r.142(3) |
| DRC-06 | Taxpayer's **reply** to the SCN | Taxpayer | r.142(4) |
| DRC-07 | **Summary of the order**. It is treated as the notice for recovery | Officer | r.142(5), (6) |
| DRC-07A / DRC-08A | Arrears of the pre-GST law uploaded for recovery / their later modification | Officer | r.142A |
| DRC-08 | Summary of a **rectification** order under s.161 or of a withdrawal order | Officer | r.142(7) |
| DRC-09 | Request to another government officer to deduct from money owed to the defaulter | Officer | r.143 |
| DRC-10 / 11 / 12 | Auction notice / notice to the successful bidder / sale certificate | Officer | r.144, r.144A, r.147 |
| DRC-13 / DRC-14 | Garnishee notice to a third person (bank, debtor) / certificate of discharge to that person | Officer | r.145 |
| DRC-15 | Request to a civil court to execute a decree in the defaulter's favour | Officer | r.146 |
| DRC-16 | Attachment or distraint of property and notice for sale; attachment of debts and shares | Officer | r.147, r.151 |
| DRC-17 | Auction notice for attached property | Officer | r.147 |
| DRC-18 | Certificate to the Collector for recovery as arrears of land revenue | Officer | r.155 |
| DRC-19 | Application to a Magistrate for recovery as a fine | Officer | r.156 |
| DRC-20 / DRC-21 | Application for more time or instalments (up to 24) / Commissioner's order | Taxpayer / Commissioner | r.158; s.80 |
| DRC-22 | **Provisional attachment** order | Commissioner | r.159(1) |
| DRC-22A | Objection to attachment | Affected person | r.159(5) |
| DRC-23 | Release of attached property | Commissioner | r.159(3), (5), (6) |
| DRC-24 | Intimation to a liquidator | Commissioner | r.160 |
| DRC-25 | Intimation of reduction or enhancement of a demand after appeal or revision | Officer | r.161; s.84 |
| SPL-01 to SPL-08 | s.128A waiver applications, notices and orders | Taxpayer / officer | r.164 |

---

## Part 1. Which section applies

### 1.1 The rule: the financial year decides, not the date of the SCN

- **FY 2017-18 to FY 2023-24:** use **s.73** (no fraud) or **s.74** (fraud, wilful misstatement or suppression to evade tax). Both sections now say so expressly: s.73(12) and s.74(12), inserted by the Finance (No. 2) Act, 2024.
- **FY 2024-25 onwards:** use **s.74A** for every case, fraud or not. Fraud affects only the **penalty** (s.74A(5)) and the payment windows (s.74A(8), (9)), not the time limit (s.74A(12)).
- **If the case spans both periods** (for example FY 2023-24 and FY 2024-25), issue **two SCNs**: one under s.73 or s.74 for FY 2023-24 and one under s.74A for FY 2024-25. The time limits, penalties and payment windows are different, so one notice cannot carry both.
- **A composite multi-year SCN is lawful in Telangana; one SCN per financial year is still the safer practice** (updated 14.10.2026). A Telangana DB upheld a composite s.74 SCN and order covering several years: there is no prejudice if each year is decided within its own s.74(10) limit (*Goldstone Infra*, 27.01.2026, W.P. 1498/2026, **TG-BINDING**). Elsewhere the High Courts remain divided: Delhi and now a Karnataka DB (23.04.2026, reversing *Bangalore Golf Club*) allow consolidation; Madras (*Titan*), Kerala and some Bombay benches do not, and a Bombay Larger Bench reference is pending. Year-wise SCNs are recommended, not legally required: each year has its own limitation date under s.73(10), s.74(10) and s.74A(2), and year-wise orders are cleaner. If one SCN covers several years, show year-wise figures and limitation dates, and keep s.73/74 and s.74A periods in separate notices (above).
  - *Case pointer:* `case-law/03-demands-adjudication-appeals.md` §2 (*Goldstone Infra*, TG-BINDING; Ambika Traders, Delhi HC; Titan, Madras HC; Bangalore Golf Club and the Karnataka DB; Milroc, Bombay HC; Rollmet LLP Larger Bench reference). `case-law/05-telangana-high-court.md` index rows 8 and 9 (AP HC rulings; *RR Metal Industries*, an earlier TG interim stay only). Persuasive, except *Goldstone Infra*.

### 1.2 Time limits for each financial year (worked out for 14 Oct 2026)

How the deadline is computed:
- It runs from the **due date of the annual return** (GSTR-9) for the year, not from the date it was actually filed. s.73(10), s.74(10) and s.74A(2) all say "due date for furnishing of annual return".
- The due date is 31 December after the year ends (r.80(1)). It is 28.02.2022 for FY 2020-21 (r.80(1A), inserted by Notf. 40/2021-CT).
- The due date still applies even where a small taxpayer was exempted from filing the return (for example Notf. 15/2025-CT for turnover up to Rs 2 crore).

| FY | Annual return due date | **s.73**: last day for the order (SCN at least 3 months earlier) | **s.74**: last day for the order (SCN at least 6 months earlier) | Status on 14.10.2026 |
|---|---|---|---|---|
| 2017-18 | 05.02.2020 or 07.02.2020, depending on the State group (Notf. 06/2020-CT, cited in Instr. 02/2021-22 [read]) | Extended to **31.12.2023** (Notf. 13/2022-CT, then 09/2023-CT [read]) | 05/07.02.2025 | Both closed |
| 2018-19 | 31.12.2020 (Notf. 80/2020-CT, per Instr. 02/2021-22) | Extended to **30.04.2024** (Notf. 56/2023-CT [read]) | 31.12.2025 | Both closed |
| 2019-20 | 31.03.2021 (Notf. 04/2021-CT) | Extended to **31.08.2024** (Notf. 56/2023-CT) | 31.03.2026 | Both closed |
| 2020-21 | 28.02.2022 (r.80(1A)) | 28.02.2025 | **28.02.2027** (SCN was due by 31.08.2026) | s.73 closed. **s.74: no new SCN; pending SCNs must be decided by 28.02.2027** |
| 2021-22 | 31.12.2022 | 31.12.2025 | 31.12.2027 (SCN by 30.06.2027) | s.73 closed. s.74 open |
| 2022-23 | 31.12.2023 | **31.12.2026** (SCN was due by 30.09.2026) | 31.12.2028 (SCN by 30.06.2028) | **s.73: no new SCN; pending SCNs must be decided by 31.12.2026.** s.74 open |
| 2023-24 | 31.12.2024 | 31.12.2027 (SCN by 30.09.2027) | 31.12.2029 (SCN by 30.06.2029) | Open |
| 2024-25 (**s.74A**) | 31.12.2025 | SCN within 42 months: by **30.06.2029**. Order within 12 months of the SCN, plus up to 6 months | same | Open |
| 2025-26 (**s.74A**) | 31.12.2026 | SCN by 30.06.2030 | same | Open |

Notes on the table:
- **Check the State-specific due date** before relying on any row. A notification may have extended GSTR-9 for some districts or States, for example Notf. 02/2024-CT for some Tamil Nadu districts for FY 2022-23. Telangana's group date for FY 2017-18 (5 or 7 February 2020) was **not confirmed**.
- **Erroneous refund:** the time runs from the **date of the refund**, not the annual return (s.73(10), 74(10), 74A(2)). For s.73, Notf. 13/2022-CT [read] **excludes 01.03.2020 to 28.02.2022** when computing the s.73(10) limitation for recovering an erroneous refund.
- The s.168A notifications extended only the **s.73(10)** order deadline, and only for FY 2017-18 to 2019-20. They did **not** extend s.74.
- **Court stays:** time during which a court or the Tribunal stays the SCN or order is excluded (s.75(1)). So is time while a decision against revenue on the same issue is under appeal (s.75(11)).
- **The "3 months / 6 months before" rule is strict.** The Telangana HC set aside an s.73 SCN for FY 2017-18 dated 28.12.2023 that broke s.73(2); the State conceded. An AP HC Division Bench held that even a two-day shortfall is fatal.
  - *Case pointer:* `case-law/03-demands-adjudication-appeals.md` §1, *Balaji Filling Station* (TG-BINDING, decided on a concession). `05-telangana-high-court.md` index row 7 (AP HC, Persuasive).
- **Limitation notifications under s.168A (13/2022, 09/2023, 56/2023) are under challenge.**
  - The Telangana HC (*Brunda Infra*, W.P. 1154/2024 & batch, incl. *HCC-SEW-MEIL-AAG JV*, DB, 02.01.2025; **TG-BINDING**) declined to interfere, but **did not uphold them**. It observed that a GST Council recommendation is a sine qua non and that later ratification cannot cure its absence (paras 94-97, on 56/2023), then decided the cases on the Supreme Court's Covid exclusion (15.03.2020 to 28.02.2022), which made the validity of the notifications academic (para 116). Rely on it for the Covid exclusion; do not describe it as upholding 9/2023 or 56/2023.
  - The Gauhati HC quashed 56/2023, and the Madras HC held 09/2023 and 56/2023 illegal.
  - The **Supreme Court has the question in SLP (C) 4240/2025** (notice issued 21.02.2025, confined to 9/2023 and 56/2023 for FY 2019-20). No judgment had been found by 14.10.2026.
  - In any order that relies on an extended date, record the notification and add that the order is subject to the outcome of that SLP.
  - *Case pointer:* `case-law/03-demands-adjudication-appeals.md` §3; `09-gaps-tribunal-and-updates.md` §5.
- **Special audit does not stop the clock.** *Koenig Solutions* (Delhi HC, 09.07.2026) quashed a special-audit SCN that was out of time. *Case pointer:* `case-law/08-interest-penalty-returns-other.md` (audit). Persuasive.

### 1.3 Penalties and the reduced-penalty windows

| Situation | s.73 (up to FY 2023-24, no fraud) | s.74 (up to FY 2023-24, fraud) | s.74A(5)(i) (FY 2024-25 on, no fraud) | s.74A(5)(ii) (FY 2024-25 on, fraud) |
|---|---|---|---|---|
| Penalty in the order | 10% of tax or Rs 10,000, whichever is higher (s.73(9)) | **100%** of tax (s.74(1), (9)) | 10% of tax or Rs 10,000, whichever is higher | 100% of tax |
| Pays tax and interest (plus penalty where shown) **before the SCN** | No penalty, no SCN for the amount paid (s.73(5), (6)) | 15% penalty (s.74(5), (6)) | No penalty (s.74A(8)(i)) | 15% penalty (s.74A(9)(i)) |
| Pays **after the SCN** | Within **30 days**: no penalty, proceedings concluded (s.73(8)) | Within **30 days**: 25% penalty, concluded (s.74(8)) | Within **60 days**: no penalty, concluded (s.74A(8)(ii)) | Within **60 days**: 25% penalty, concluded (s.74A(9)(ii)) |
| Pays **after the order** | No reduction | Within 30 days of communication: 50% penalty, concluded (s.74(11)) | No reduction | Within **60 days**: 50% penalty, concluded (s.74A(9)(iii)) |
| Exception | Penalty is still payable where self-assessed tax or tax collected was not paid within 30 days of its due date (s.73(11)) | none | Same exception (s.74A(11)) | none |
| If an appeal or court finds no fraud | Not applicable | Tax is re-determined **as if under s.73** (s.75(2)) | Not applicable | The **penalty** drops to the s.74A(5)(i) level (s.75(2A)); the SCN itself survives |

Other rules on penalties and payments:
- **Payment within the window:** the taxpayer files DRC-03, and you issue **DRC-05** concluding the proceedings (r.142(3)).
- **Short payment:** if a pre-SCN payment falls short, issue the SCN only for the shortfall (s.73(7); s.74(7); s.74A(10)).
- **Co-noticees:** once proceedings against the main person are concluded by payment, proceedings for **s.122 and s.125 penalties against the other noticees** in the same SCN are deemed concluded (Explanation 1(ii) to s.74 and to s.74A).
- **Prosecution:** conclusion by payment does **not** cover prosecution under s.132 (Explanation 1(i)).
- **No double penalty:** where a penalty is imposed under s.73, 74 or 74A, no other penalty may be imposed **for the same act** (s.75(13)).
  - Circ. 171/03/2022 [read], for fake invoices:
    - the recipient who **availed and utilised** fake ITC pays tax, interest and penalty under s.74, and no s.122 penalty for the same act;
    - the **issuer** of invoices without supply faces no s.73/74 demand but a penalty under s.122(1)(ii);
    - a pure pass-through person faces penalties under s.122(1)(ii) and (vii);
    - a beneficiary at whose instance the transactions were done faces a penalty under s.122(1A).
- **"Suppression"** means not declaring facts that must be declared in a return, statement or report, or not giving information asked for in writing by the proper officer (Explanation 2 to s.74 and s.74A).

### 1.4 Section 76: tax collected but not paid

- Anyone who **collected an amount as tax** must pay it to the Government, whether or not the supply was taxable (s.76(1)).
- **Procedure:**
  - SCN proposing the amount plus a **penalty equal to the amount** (s.76(2)), with a DRC-01 summary (r.142(1)(a)).
  - Hearing if requested in writing (s.76(5)). Give one anyway, as for s.75(4).
  - Order within **1 year** of the notice, excluding any court stay (s.76(6), (7)), with facts and reasons (s.76(8)).
  - DRC-07 summary (r.142(5)).
  - Interest under s.50 runs from the date of collection (s.76(4)).
- s.76 has no time limit for **issuing** the notice. The reply is filed in DRC-06 (r.142(4)).

### 1.5 Penalty-only and goods-related proceedings, briefly

| Provision | What it covers | Procedure |
|---|---|---|
| **s.122(1)** | 21 listed offences (invoice without supply, ITC without receipt, failure to register, obstruction and others). Penalty: Rs 10,000 or the tax evaded / ITC involved, whichever is higher | SCN with a DRC-01 summary (r.142(1)(a)); hearing (s.126(3)); reasoned order naming the breach and the provision (s.126(4)); DRC-07 (r.142(5)) |
| **s.122(1A)** | Person who retains the benefit of, and causes, transactions under s.122(1)(i), (ii), (vii) or (ix). Penalty equal to the tax evaded or ITC passed on | Same as above |
| **s.122(2)** | Tax short paid or ITC wrongly availed, by a registered person: 10% or Rs 10,000 (no fraud); 100% or Rs 10,000 (fraud) | Same as above. **Do not** use it where s.73/74/74A already penalises the same act (s.75(13)) |
| **s.122(3)** | Abetment; dealing in goods liable to confiscation; not appearing on summons; invoice failures. Up to Rs 25,000 | Same as above |
| **s.125** | Any contravention with no separate penalty. Up to Rs 25,000 | SCN, DRC-01, hearing, DRC-07. The proper officer under Circ. 3/3/2017 was **not checked** for this file |
| **s.127** | Penalty not covered by proceedings under s.62-64, 73, 74, 74A, 129 or 130 | Order after "a reasonable opportunity of being heard" (s.127); DRC-01 and DRC-07 (r.142) |
| **s.129** | Goods or conveyance detained in transit. Release on penalty of 200% of tax (owner comes forward) or the higher of 50% of value and 200% of tax (owner does not) | Notice within **7 days** of detention; order within **7 days** of service of the notice (s.129(3)); hearing (s.129(4)); payment within 7 days of the notice closes the case by DRC-05 (r.142(3)); goods may be sold if the penalty is not paid within 15 days of the order (s.129(6)). Movement forms (MOV series) are under Circ. 41/15/2018-GST, **not read here** |
| **s.130** | Confiscation of goods or conveyance (supply with intent to evade, unaccounted goods and others) | Hearing (s.130(4)); option to pay a fine instead of confiscation (s.130(2)); fine plus penalty not less than 100% of the tax; DRC-01 and DRC-07 (r.142) |

- **Discretionary penalties:**
  - No penalty for **minor breaches**, meaning tax under Rs 5,000, or errors that are easily rectifiable and made without fraud or gross negligence (s.126(1)).
  - The penalty must fit the breach (s.126(2)).
  - Voluntary disclosure counts as a mitigating factor (s.126(5)).
  - s.126 does **not** apply where the penalty is a fixed sum or a fixed percentage (s.126(6)).
- **Proper officer for s.122 penalty-only SCNs** (Circ. 254/11/2025 [read], Table III, by amount of penalty):
  - Superintendent: up to Rs 10 lakh CGST, or Rs 20 lakh IGST or combined.
  - AC/DC: above those and up to Rs 1 crore CGST, or Rs 2 crore IGST or combined.
  - Additional/Joint Commissioner: above.
  - Where both CGST and IGST penalties are proposed, use the combined amount (para 7.2).
- s.122 sets **no time limit** for the SCN or order. No guidance on this was found (see Gaps).
- *Case pointers:* *Satyam Shivam Papers* (TG-BINDING; SC dismissed the department's SLP): an e-way bill that expired for a genuine reason is not evasion, so s.129 was wrongly invoked. `case-law/03-demands-adjudication-appeals.md` §11 and `05-telangana-high-court.md` row 3.

### 1.6 Interest under s.50

- **Rate:**
  - 18% a year on tax not paid (s.50(1)).
  - On ITC **wrongly availed and utilised**, the rate notified under s.50(3). Notf. 13/2017-CT [read] originally fixed **24%**. Any later reduction to 18% was **not confirmed** in this review (see Gaps).
- **Utilisation of ITC:**
  - Interest under s.50(3) is due only when wrong ITC is **utilised**.
  - ITC counts as utilised when the credit ledger balance **falls below** the wrong ITC, and only to that extent (r.88B(3) and its Explanation).
  - *Case pointer:* `case-law/08-interest-penalty-returns-other.md` §1 (*Utpal Das*, Calcutta HC; *Manoja Kumar Nayak*, Orissa HC; Persuasive).
- **Late returns:**
  - On tax declared in a late return, interest falls only on the portion paid in **cash** (proviso to s.50(1); r.88B(1)).
  - This relief does **not** apply where the return is filed after s.73, 74 or 74A proceedings for that period have started.
- **Interest is due even if the order does not mention it** (s.75(9)).
- **Even so, propose and quantify interest in the SCN.** The Allahabad HC (*Sanjay Construction*, 2026) quashed an interest demand that the SCN never proposed. *Case pointer:* `case-law/03-demands-adjudication-appeals.md` §5. Persuasive.

---

## Part 2. Who adjudicates: proper officer and monetary limits

### 2.1 Monetary limits for s.73, s.74 and s.74A

Sources:
- Circ. 31/05/2018 [read], para 5. It applies to s.73 and s.74. Para 2-4 also made Superintendents proper officers under s.74.
- Circ. 254/11/2025 [read], Table II. It applies the **same limits** to **s.74A**.
- Circ. 254 Table I assigns s.74A, s.122 and r.142(1A) to Additional/Joint Commissioners, Deputy/Assistant Commissioners and Superintendents.

| Officer | Central tax (incl. cess) only | IGST (incl. cess) only | Central tax + IGST together |
|---|---|---|---|
| Superintendent | Up to Rs 10 lakh | Up to Rs 20 lakh | Up to Rs 20 lakh |
| **Deputy / Assistant Commissioner** | **Above Rs 10 lakh and up to Rs 1 crore** | **Above Rs 20 lakh and up to Rs 2 crore** | **Above Rs 20 lakh and up to Rs 2 crore** |
| Additional / Joint Commissioner | Above Rs 1 crore, no upper limit | Above Rs 2 crore, no upper limit | Above Rs 2 crore, no upper limit |

How to apply the limits:
- **Tax only.** The limit is based only on the **tax** proposed. Penalty and interest are left out (Circ. 254 para 5.3(d)).
- **CGST and IGST together.** Where the SCN demands both, use the **combined** amount (column 5), even if either one alone would fall in a different band (Circ. 254 para 5.2).
- **Later statements.** For a statement under s.73(3), 74(3) or 74A(3), the proper officer is fixed by the **highest** amount across the SCN and the statements (Circ. 254 para 5.3(a)).
  - If a statement takes the total above your limit, the issuing officer must issue a **corrigendum** making the earlier SCN and statements answerable to the higher officer (para 5.3(b)).
  - If the band does not change, the same officer issues the statement and keeps it answerable to the same authority (para 5.3(c)).
  - For audit SCNs, the jurisdictional officer issues the statement, answerable to the authority named in the audit SCN (para 5.3(e)).
- **Similar SCNs to the same noticee at different levels** go to the officer competent for the **highest** amount (Circ. 31/05/2018 para 8).
- **A senior officer may act for a junior one** (s.5(2); Circ. 31/05/2018 para 3). An AC may therefore adjudicate a Superintendent-level case, but not one above Rs 1 crore CGST / Rs 2 crore IGST.

### 2.2 SCNs issued by Audit and by DGGI

- **Audit Commissionerate and DGGI officers only issue SCNs.** The competent officer of the **executive Commissionerate** where the noticee is registered adjudicates them, by the monetary limits above, when the case concerns only one executive Commissionerate (Circ. 31/05/2018 para 6, as substituted by Circ. 169/01/2022 [read]).
- **DGGI SCNs whose noticees fall in several Central Tax Commissionerates** go to an **All-India Additional/Joint Commissioner (Common Adjudicating Authority, CAA)** of a specified Commissionerate, **whatever the amount**. This covers one SCN to several noticees (same or different PAN), and several SCNs on one issue to noticees with the same PAN (Circ. 31/05/2018 para 7.1, as substituted by Circ. 239/33/2024 [read]; Notf. 02/2017-CT Table V as substituted by Notf. 27/2024-CT, in force from 01.12.2024).
  - The CAA is chosen by where the principal place of business of the noticee with the **highest tax demand** falls.
  - **Hyderabad Zone: the CAA is the Additional/Joint Commissioner of Rangareddy Commissionerate** (Circ. 239 table, row 14). That Medchal Commissionerate sits in the Hyderabad Zone is **assumed**, not confirmed from a CBIC document.
  - A **later** SCN on the same issue to noticees with **different** PANs goes to the jurisdictional officer if it has only one GSTIN. If it has several GSTINs across Commissionerates, a CAA is chosen afresh on that later SCN's highest demand (para 7.1.1).
  - DGGI SCNs issued before 01.12.2024 and not decided by 30.11.2024 could be moved to the CAA by corrigendum (para 7.3).
- **Audit SCNs** whose noticees span several Commissionerates: a proposal for a common adjudicating authority goes to the Board (Circ. 31/05/2018 para 7.2, inserted by Circ. 169).
- **Review, revision and appeal of CAA orders** follow the Commissionerate where the CAA is posted (Circ. 250/07/2025 [read]):
  - review and revision lie with that Commissioner;
  - appeal lies to the matching Commissioner (Appeals);
  - the reviewing or revisional authority may seek comments from DGGI.
  - Departmental appeals before the GSTAT in CAA cases are covered by Circ. 256/02/2026 (not read here).
- **Check your authority before you adjudicate.**
  - In every DGGI case, confirm that the SCN is answerable to you, and say in the order why you are the competent authority.
  - The Karnataka HC (*NCS Pearson*, 16.07.2025) quashed a DGGI SCN issued by an unauthorised officer.
  - Most High Courts uphold DGGI's all-India power to issue SCNs (Notf. 14/2017-CT).
  - *Case pointer:* `case-law/08-interest-penalty-returns-other.md` §12. Persuasive.

### 2.3 Re-determination after an appeal finds no fraud (s.75(2))

- The proper officer is the **same officer who adjudicated** the original s.74 SCN (Circ. 254/11/2025 para 6).
- The GSTAT has held that **only the proper officer**, not the appellate authority or the Tribunal, may re-determine the demand under s.73. *Case pointer:* `case-law/09-gaps-tribunal-and-updates.md` §8, *Sterling & Wilson* (GSTAT Principal Bench, 11.02.2026). Persuasive.

### 2.4 Central and State: cross-empowerment (s.6) and *Armour Security*

- **The statute:**
  - State tax officers are also proper officers under the CGST Act, subject to notified conditions (s.6(1)).
  - Where a State officer has **initiated proceedings on a subject matter**, the Central officer may not start proceedings on the same subject matter (s.6(2)(b)), and the reverse applies under the SGST Act.
  - Rectification, appeal and revision of a Central officer's order do not lie before a State officer (s.6(3)).
- **Armour Security (India) Ltd v. Commissioner, CGST, Delhi East (SC, 14.08.2025)** (**SC**):
  - A summons, search or seizure is **not** "initiation of proceedings". **An SCN is.**
  - The bar covers both administrations.
  - According to reports of the judgment's guidelines, action arising from **audit or scrutiny** must be taken by the administration to which the taxpayer is **assigned**.
  - *Case pointer:* `case-law/08-interest-penalty-returns-other.md` §7. The bench composition is reported inconsistently, so verify it.
- **Telangana HC (W.P. 3204 of 2025, as reported):** the State order was quashed because the Centre had acted first, and the State was told to transfer its material. TG-BINDING if confirmed.
- **United Bakers (reported Telangana HC, 23.04.2026):** the same period with **different issues** is not the "same subject matter". Same file, §7.
- **Before every SCN:**
  - check the portal for any SCN by the State on the same issue and period, and record the check in the SCN;
  - do not take up audit or scrutiny of taxpayers assigned to the State.
- **Duplicate SCNs or orders for the same period** (State and Centre) are rectifiable under s.161. *Case pointer:* `case-law/06-registration-rectification.md` Issue H (Telangana HC, W.P. 20731/2025 batch, 15.10.2025, TG-BINDING); `03-demands-adjudication-appeals.md` §2 (*Ennem Excel Engineering*, TG-BINDING).
- **Taxpayer migrates to another jurisdiction** (Circ. 255/01/2026 [read]):
  - action validly taken before the migration stays valid;
  - the **new** (transferee) officer continues from the stage reached, including appeals;
  - the old officer must not start anything new and should pass any information to the new officer.

---

## Part 3. Before the SCN

### 3.1 Where cases come from

1. **Scrutiny of returns (s.61; r.99):**
   - ASMT-10 lists the discrepancies, quantified where possible. The reply period is up to 30 days or longer if allowed.
   - The taxpayer pays or explains in ASMT-11. You accept in ASMT-12.
   - If there is no satisfactory explanation, or an accepted discrepancy is not corrected, you may proceed under s.65, 66, 67, 73, 74 or 74A (s.61(3)).
   - Scrutiny SOPs: Instr. 02/2022-GST (FY 2017-18 and 2018-19) and Instr. 02/2023-GST (FY 2019-20 onwards). They are listed in `data/instructions.csv` and were **not re-read** for this file.
2. **Audit (s.65; r.101):**
   - ADT-01 notice; audit completed within 3 months of its start (s.65(4)); findings in ADT-02 within 30 days of conclusion (s.65(6); r.101(5)).
   - Where the audit detects a short payment, action is under s.73, 74 or 74A (s.65(7)).
   - **Wait for the reply period** on audit observations before issuing the SCN. *Case pointer:* `case-law/08-interest-penalty-returns-other.md` (audit), *Varian Medical* (Delhi HC, 2025): an SCN issued one day before the reply period ended breached natural justice. Persuasive.
3. **Investigation or intelligence** (s.67, DGGI or anti-evasion):
   - These usually lead to a s.74 or s.74A(5)(ii) SCN.
   - Instr. 02/2021-22 [GST-INV] [read] asks that investigations be completed and SCNs issued **well before** the deadline, so the adjudicating authority has time for a proper order.
4. **Return-mismatch intimations** (DRC-01B and DRC-01C under r.88C and r.88D):
   - Unpaid self-assessed tax is recovered directly under s.75(12) and s.79, via DRC-01D (r.142B).
   - Disputed differences go through an SCN.

### 3.2 DRC-01A: is it mandatory?

- **Rule text today (r.142(1A)):** "The proper officer **may**, before service of notice ... communicate the details of any tax, interest and penalty as ascertained ... in Part A of FORM GST DRC-01A". The word "shall" was replaced by "**may**" by Notf. 79/2020-CT dated **15.10.2020**. Notf. 20/2024-CT extended the rule to s.74A from 01.11.2024.
  - The taxpayer may pay, or object in **Part B** (r.142(2A)).
  - The officer may accept the payment or submissions in **Part C** (r.142(2A), inserted by Notf. 12/2024-CT).
- **Proper officer for r.142(1A):** Additional/Joint Commissioner, Deputy/Assistant Commissioner and Superintendent (Circ. 254/11/2025 Table I, item iii).
- **Case law (Secondary, from web search for this file; not in the case-law folder):**
  - Delhi and Allahabad HC rulings held the pre-SCN intimation **mandatory under the unamended rule**, that is, for actions before 15.10.2020.
  - An AP HC ruling is reported to hold that the 2020 amendment is **prospective**.
  - No ruling was found holding that a post-2020 SCN fails only because DRC-01A was not issued.
  - Sources: [LiveLaw - Delhi HC on pre-SCN consultation](https://www.livelaw.in/amp/news-updates/delhi-high-court-cgst-rules-pre-show-cause-consultation-notice-revenue-authorities-202944); [LiveLaw - Allahabad HC on DRC-01A](https://www.livelaw.in/amp/tax-cases/allahabad-high-court-justice-surya-prakash-kesarwani-justice-jayant-banerji-cgst-act-2017-194530).
- **What to do:**
  - DRC-01A is **legally optional today**, but issue it as good practice, especially in s.74 or s.74A(5)(ii) cases. The 15% pre-SCN window (s.74(5), s.74A(9)(i)) is only useful if the taxpayer knows your figures.
  - If you issue it, **let the reply time run** before issuing the SCN (*Varian Medical*, above).
  - Deal with any Part B reply in the SCN.

### 3.3 Voluntary payment before the SCN

- The taxpayer pays tax and interest (plus 15% penalty in fraud cases) on **his own ascertainment or yours**, and informs you in **DRC-03**. The portal acknowledges it in **DRC-04** (r.142(2)).
- **No SCN** may then be issued for the amount paid, and no penalty is due on it (s.73(6); s.74(6); s.74A(8)(i), (9)(i)).
- **If the payment falls short**, issue the SCN only for the shortfall (s.73(7); s.74(7); s.74A(10)).
- Give credit in the SCN for every DRC-03 payment and pre-SCN reversal. Interest under s.50(3) stops on reversal (r.88B(3)).
- **Payments made during a search or investigation:** check that they were voluntary.
  - The courts look hard at DRC-03 payments taken under pressure (*Vallabh Textiles*, Delhi HC; *Radhika Agarwal*, SC 2025).
  - *Case pointer:* `case-law/04-arrest-search-and-landmark.md` and `09-gaps-tribunal-and-updates.md` §7.

### 3.4 Threshold for issuing an SCN

- **s.74A:** no SCN may be issued if the tax, ITC or refund involved for the **financial year** is **less than Rs 1,000** (proviso to s.74A(1)).
- **s.73 and s.74:** no statutory minimum. s.126(1) bars penalties for "minor breaches" (tax under Rs 5,000) that are easily rectifiable and made without fraud or gross negligence. That limits the **penalty**, not the demand for tax.

---

## Part 4. The SCN

### 4.1 Two documents, both required

1. **The full SCN** under s.73(1), 74(1), 74A(1), 76(2), 122, 125, 129 or 130. It is self-contained, reasoned and signed.
2. **The DRC-01 summary**, served **electronically with** the SCN (r.142(1)(a)). A statement for later periods uses DRC-02 (r.142(1)(b)).
- Instr. 04/2023-GST [read] directs that **every** SCN summary be served on the portal in DRC-01, and every order summary uploaded in DRC-07. Manual-only service "is in clear violation" of the Rules (para 4).
- **A DRC-01 summary alone is not an SCN.**
  - Courts quash demands made on a summary without a proper notice: Jharkhand HC (*NKAS Services*), Gauhati HC (*Construction Catalysers*). Both Persuasive.
  - The Telangana HC will not usually entertain a writ against an SCN itself (*S. Shivraj Reddy Constructions*, TG-BINDING); the taxpayer must reply to it.
  - *Case pointers:* `case-law/03-demands-adjudication-appeals.md` §1; `05-telangana-high-court.md` rows 16 and 17.

### 4.2 What the SCN must contain

| Item | Why | Source / case |
|---|---|---|
| Name, GSTIN, address of every noticee; the **section** invoked (73, 74 or 74A, and the 74A(5) limb) | Jurisdiction and limitation depend on it | s.73(1), 74(1), 74A(1) |
| **Financial year and tax periods**, one FY per SCN where possible | Limitation runs year by year | s.73(10), 74(10), 74A(2); §1.1 above |
| **Facts and grounds**: what was not paid or wrongly availed, and why that breaks a named provision | The order cannot go beyond these grounds | s.75(7) |
| **Quantification**: tax by head (CGST, SGST, IGST, cess) and by period, with a working sheet | The order cannot exceed the amounts proposed | s.75(7); *Vrinda Automation* (Allahabad HC 2025), Karnataka HC W.P. 18888/2025, `case-law/03` §5 |
| **Interest** under s.50, proposed (and quantified where possible) | An unproposed interest demand can be quashed | s.73(1), 74(1), 74A(1); *Sanjay Construction* (Allahabad HC 2026), `case-law/03` §5 |
| **Penalty** proposed, with the clause (s.73(9), 74(1), 74A(5)(i) or (ii), 122(…)) | s.126(4) requires the nature of the breach and the provision to be stated | s.126(4) |
| **Fraud, wilful misstatement or suppression, if invoked: the specific facts, the evidence and the intent**, pleaded in the SCN itself. Not "fraud **or** suppression" boilerplate | Extended period and 100% penalty depend on it | **G.R. Infra Projects Ratlam v. State of M.P. (SC, 19.08.2026, CA 11277/2026)**, **SC**: deficiencies cannot be cured later, and "or" between the grounds shows the officer was unsure. `case-law/03` §6 |
| **List of relied-upon documents (RUDs)**, with copies served or an offer of inspection | Natural justice. Orders based on unsupplied material are set aside | *S.S. Metals* (Madras HC), compendium §8 (ITC); Gujarat HC 14.03.2026 (web, Secondary): [taxo.online](https://taxo.online/latest-news/14-03-2026-non-supply-of-relied-upon-documents-along-with-the-show-cause-notice-violates-the-principles-of-natural-justice-gujarat-high-court/) |
| Credit for payments already made (DRC-03, reversals), and the s.73(8) / 74(8) / 74A(8)(ii), (9)(ii) **payment option** and its time limit | Lets the taxpayer close the case; required by s.73(8) etc. | s.73(8), 74(8), 74A(8), (9) |
| **Time to reply** (DRC-06) and an invitation to say whether a hearing is wanted. Fix the hearing in a separate notice | s.75(4) | r.142(4) |
| The **adjudicating authority** to whom the SCN is answerable, and why (monetary limit, CAA) | Jurisdiction | Circ. 31/05/2018 as amended; Circ. 254/11/2025 |
| A line confirming that **no SCN on the same subject matter** has been issued by the State administration | s.6(2)(b) | *Armour Security* (SC) |
| **DIN/RFN** on the SCN and the DRC-01, uploaded through the issuing officer's own authenticated portal login. A digital signature on the SCN PDF remains good practice | A notice or order without a DIN/RFN is invalid. One electronically authenticated and uploaded on the portal is valid without a visible signature | **Gudla Vanaja v. AC (ST) (TG HC Full Bench, 30.09.2026, W.P. 20397/2025 batch, paras 154-155), TG-BINDING.** It overruled *Bigleap Technologies* (TG HC DB, 28.02.2025) and supersedes *Silver Oak Villas* (TG HC DB, 14.03.2024); do not cite either. `case-law/03` §1 |

On signatures (updated 14.10.2026): r.26(3) requires notices, certificates and orders to be issued electronically through a digital signature or e-signature, but it sits in the registration chapter. Earlier Telangana DBs (*Silver Oak Villas*, *Bigleap*, followed in *Water Tech Engineers*) set aside unsigned SCNs and orders. The **Full Bench in *Gudla Vanaja* (30.09.2026)** overruled that line: SCNs and orders under Chapter XVIII that are electronically authenticated by the proper officer and uploaded on the portal are valid without a visible signature; upload is valid service under s.169(1)(d); limitation for appeal runs from the upload date; and **a notice or order without a DIN or RFN is invalid** (paras 154-155). So in Telangana the DIN/RFN is mandatory; a visible or digital signature remains good practice, but its absence alone is not fatal.

**DIN** (Circ. 249/06/2025 [read]):
- Communications served through the **portal** carry a verifiable Reference Number (RFN) and need no DIN.
- Any communication sent **outside** the portal, for example a hearing notice by email or post, still needs a DIN under Circ. 122/41/2019 and 128/47/2019 as modified. Those two circulars were not re-read for this file.

### 4.3 Service of the SCN (s.169)

- **Modes (s.169(1)):**
  - (a) by hand, including courier or messenger, to the taxpayer, his manager or representative, an adult family member, or an employee;
  - (b) registered post, speed post or courier with acknowledgement;
  - (c) email to the registered address;
  - (d) **making it available on the common portal**;
  - (e) newspaper publication;
  - (f) affixing at the last known place of business, and failing that, on the office notice board.
- **Date of service:**
  - Service is deemed on the date the notice is tendered, published or affixed (s.169(2)).
  - For post, service is deemed after the normal transit time unless the contrary is proved (s.169(3)).
  - Service cannot later be questioned if the person **acted on** the notice (s.160(2)).
- **Portal-only service:**
  - The Delhi HC set aside many ex parte orders where the SCN sat only in the portal's "Additional Notices & Orders" tab (*ACE Cardiopathy*, 2024:DHC:4108-DB). Persuasive.
  - The Telangana HC has relegated such taxpayers to a delayed appeal, with sympathetic condonation (*Bollant Industries*; *Sri Sai Ram Traders*, TG-BINDING).
  - *Case pointer:* `case-law/03` §4; `05-telangana-high-court.md` rows 10 and 11.
  - **If there is no reply, also serve by email and RPAD, and record every mode and date.**

### 4.4 Statements for later periods (s.73(3), 74(3), 74A(3))

- After an SCN, later periods may be covered by a **statement** (DRC-02) instead of a fresh SCN, if the **grounds are the same** (s.73(4), 74(4), 74A(4)).
- A s.74(3) statement counts as a notice under **s.73**, not s.74 (s.74(4)). Fraud must be pleaded afresh by a separate s.74 SCN.
- Each statement must still meet the time limit for **its own** period. For the proper officer, see Circ. 254 para 5.3 (§2.1 above).

---

## Part 5. Reply and personal hearing

1. **Reply:**
   - The taxpayer replies in **DRC-06** (r.142(4)).
   - Consider every point raised and every document filed. If the reply raises new facts, verify them, for example with suppliers or other officers, and share any new adverse material before relying on it.
2. **Hearing is compulsory:**
   - A hearing must be granted where the taxpayer asks for one in writing, **or where any adverse decision is contemplated** (s.75(4)).
   - Ticking "no" for a hearing in the reply, or not replying at all, does not remove the duty.
   - Issue a **separate hearing notice** with date, time and venue (or a video link). "N.A." in the hearing column of the DRC-01 is not a hearing.
   - *Case pointers:* the text of **s.75(4)** is the primary authority. **B.K. Steels** (TG HC DB, 25.07.2024, W.P. 18654 and 18766 of 2024), **TG-BINDING**, set aside an order for want of a hearing, but by consent on an admitted breach, so its precedent weight is limited. Followed by the Madras, MP, Patna, Gujarat, P&H, Allahabad, Calcutta and Uttarakhand HCs. `case-law/03` §4.
3. **Adjournments (s.75(5)):**
   - Grant time only "if sufficient cause is shown", with **reasons recorded in writing**.
   - **No more than three adjournments** to a person during the proceedings.
   - After the third adjournment, or if the noticee does not appear after proper notice, you may decide on the record. Say so in the order and list each date offered.
4. **Cross-examination:**
   - The Act is silent. Where the demand rests on **statements of third parties** (suppliers, transporters, co-noticees), a reasoned request to cross-examine them must be decided on its merits, **before** the final order.
   - Grant it where the witness is relevant and the statement is central to the demand. If you refuse, give reasons.
   - *Cases (web search, Secondary; not in the case-law folder):*
     - Kerala HC, *Joint Commissioner v. Nishad K.U.* (2025): denying cross-examination of witnesses whose statements founded a s.74 order vitiated it.
     - Kerala HC, *X L Interiors* (2025): rejecting the request without considering relevance was a breach.
     - Kerala HC: deciding the request only in the final order deprived the taxpayer of an effective remedy.
     - Gujarat HC (14.03.2026): order set aside for refusing cross-examination and not supplying RUDs.
     - Sources: [Taxmann - denial of cross-examination](https://www.taxmann.com/post/blog/denial-of-cross-examination-of-witnesses-by-authorities-would-render-proceedings-as-void-hc); [Taxmann - order quashed for denial of cross-examination](https://www.taxmann.com/post/blog/hc-quashes-order-for-denial-of-cross-examination-breaching-natural-justice).
   - All are Persuasive. No Telangana HC ruling was found.
5. **Relied-upon documents:** if the noticee says RUDs were not supplied, supply them (or allow inspection) and give time **before** the hearing. Record it.
6. **Record of hearing:** keep a dated record of who appeared, what was argued, what was filed, and any adjournment granted with its reason. Reproduce the gist in the order.

---

## Part 6. The order

### 6.1 What a sustainable order contains

| Element | Source |
|---|---|
| SCN number and date; section invoked; FY and periods; date of service and mode | s.169; s.73(2), 74(2), 74A(2) |
| **Limitation check**: annual return due date, SCN deadline, order deadline (and any s.168A notification or s.75(1)/(11) exclusion relied on) | s.73(10), 74(10), 74A(7); s.75(10) |
| Why you are the competent authority (monetary limit, CAA, migration) | Circ. 31/05/2018 as amended; Circ. 254/11/2025; Circ. 255/01/2026 |
| Summary of the SCN, the reply (DRC-06) and each hearing date, attendance and adjournment (s.75(5)) | s.75(4), (5) |
| Treatment of cross-examination and RUD requests | Part 5 above |
| **Findings, issue by issue, with reasons and evidence** ("the relevant facts and the basis of his decision") | **s.75(6)** |
| For s.74 or s.74A(5)(ii): a **specific finding** on each element of fraud, wilful misstatement or suppression and the intent to evade | *G.R. Infra* (SC); Madras HC Nov 2025 (`case-law/03` §6) |
| Tax, interest and penalty confirmed, **per head and per period, each not more than the SCN** and on **no new ground** | **s.75(7)**; `case-law/03` §5 |
| Interest under s.50, stated (it is payable even if omitted, but state it) | s.75(9); s.50; r.88B |
| Penalty: the clause; for discretionary penalties, why the amount fits (s.126(2), (4), (5)); no second penalty for the same act | s.126; s.75(13) |
| Credit for amounts already paid (DRC-03 / DRC-03A) | r.142(2), (2B) |
| The 50% penalty option after the order in fraud cases (s.74(11): 30 days; s.74A(9)(iii): 60 days) | s.74(11); s.74A(9)(iii) |
| Appeal remedy and pre-deposit (s.107(1), (6)) | s.107 |
| Where reliant on Notf. 09/2023 or 56/2023: "subject to the outcome of SLP (C) 4240/2025" | `case-law/03` §3 |
| DIN or RFN (mandatory), digital signature (good practice), and the DRC-07 summary uploaded with the order | r.142(5); Instr. 04/2023-GST; *Gudla Vanaja* (TG Full Bench, 30.09.2026, TG-BINDING), which overruled *Bigleap* and the decisions following it (*Water Tech Engineers*) |

Two further points:
- **One order per SCN.** If the SCN covers several years, record findings and limitation **year by year**.
- **DRC-07 is the recovery notice.** The amount it shows goes into Part II of the electronic liability register (r.142(5), (6)). Make sure the DRC-07 figures match the speaking order exactly.

### 6.2 When fraud is not proved

- **Up to FY 2023-24 (s.74 SCN):**
  - If **an appellate authority, the Tribunal or a court** holds that fraud is not established, the proper officer re-determines tax **as if the notice were under s.73** (s.75(2)). You do this as the original adjudicating authority (Circ. 254 para 6).
  - **Time:** within 2 years of the direction (s.75(3)).
  - **Scope:** only for years where the s.74 SCN was issued **within 2 years 9 months** of the annual return due date (or of the erroneous refund), that is, within the s.73 limit. Years outside that limit are dropped (Circ. 185/17/2022 [read], Issue 2).
  - The **s.73 penalty** applies (10% or Rs 10,000).
  - For FY 2017-18 to 2019-20, the taxpayer may then seek the s.128A waiver within 6 months of your re-determination order (s.128A(1) first proviso; Notf. 21/2024-CT [read], row 2; r.164(6) proviso).
- **When you yourself are not satisfied about fraud at the adjudication stage:**
  - The Act does not expressly let the adjudicating officer "convert" a s.74 SCN into a s.73 order.
  - The safe course is to confirm only what the s.73 grounds and limitation support, with the s.73 penalty, and say expressly that fraud is not established and why.
  - The Gujarat HC refused conversion where categorical findings of fraud stood (*R B Pandey and Sons*, Feb 2026). `case-law/03` §6. Persuasive. **No direct ruling on adjudicator-level conversion was found (see Gaps).**
- **FY 2024-25 onwards (s.74A):** limitation is the same either way. If fraud fails, only the penalty drops to s.74A(5)(i) (s.75(2A)), and you can record that finding in your own order.

### 6.3 Time to pass the order

- **Original adjudication:** by the s.73(10), 74(10) or 74A(7) date (table in §1.2).
- **s.74A extension:**
  - Seek it from the Commissioner (or an authorised officer not below Joint Commissioner, senior to you) **before** the 12 months expire.
  - Give reasons for the delay. The extension is up to 6 months (s.74A(7) proviso).
  - The extension order must be in writing and on file.
- **After a remand or direction:** within **2 years** of communication of the direction (s.75(3); Circ. 185/17/2022).
- **Missed deadline:** the proceedings are **deemed concluded** (s.75(10)). No order can follow, and no fresh SCN on the same matter is possible once limitation has run.
- **Excluded time:** periods of court stay (s.75(1)) and of pending departmental appeals in another case on the same issue (s.75(11)) do not count.

### 6.4 Rectification (s.161; DRC-08)

- You may rectify an **error apparent on the face of the record** in your order or notice:
  - on your own motion; or
  - when an officer or the affected person points it out **within 3 months** of the order.
- **No rectification after 6 months** from the order, except purely clerical or arithmetical slips (s.161, provisos 1 and 2).
- If the rectification **adversely affects** anyone, give notice and a hearing (s.161, third proviso).
- Upload the summary of the rectification (or of a withdrawal) in **DRC-08** (r.142(7)).
- **s.161 is not a review.** It cannot be used to re-decide merits or create a fresh demand. A new demand needs an SCN.
- *Case pointers:* `case-law/06-registration-rectification.md` Issue H:
  - *Sajal Kumar Das*, Calcutta HC 2024 (no substantive rewriting);
  - *Future Consumer Ltd*, Delhi HC, 10.10.2025, W.P.(C) 15611/2025 (personal hearing mandatory under the third proviso to s.161, including before rejecting a rectification application; persuasive);
  - Madras HC Dec 2025 (no fresh demand through s.161);
  - **Telangana HC W.P. 20731/2025 batch (15.10.2025), TG-BINDING:** duplicate State and Central SCNs or orders for the same period are rectifiable under s.161, and the 6-month bar did not apply on the State's concession.

---

## Part 7. After the order

### 7.1 Payment period and early recovery (s.78; Instr. 01/2024-GST [read])

- **Payment window:**
  - The taxpayer has **3 months from service of the order** to pay (s.78). The DRC-07 is the recovery notice (r.142(6)).
  - Recovery under s.79 starts only after that, unless the proviso to s.78 is used.
- **Shortening the period (Instr. 01/2024-GST, 30.05.2024, paras 1.3-3.4, read from the scanned original):**
  - The proper officer for the **s.78 proviso** is the **jurisdictional Principal Commissioner or Commissioner**. The proper officer for s.79 recovery is the jurisdictional **Deputy or Assistant Commissioner** (para 3.1, citing Circ. 3/3/2017).
  - If early recovery is needed, the AC/DC puts the case with reasons to the Commissioner. The Commissioner records reasons in writing and directs the taxpayer to pay within a shorter period, with a copy to the AC/DC (para 3.2).
  - Reasons must rest on **credible evidence**, for example high risk to revenue, likely closure of the business, declining finances or impending insolvency. The direction must weigh financial health and ease of doing business, and **must not be issued mechanically** (para 3.3).
  - If the taxpayer does not pay within the shorter period, the AC/DC recovers under s.79 (para 3.4).
- **Courts:**
  - Recovery within 3 months without recorded reasons was set aside (*Cargotec India*, Madras HC 2024).
  - A garnishee order was upheld where reasons had been recorded (*Liakhat Ali Mallick*, Calcutta HC 2023).
  - `case-law/03` §10. Persuasive.

### 7.2 Modes of recovery (s.79; r.143-161)

| Mode | Section | Form / rule |
|---|---|---|
| Deduct from money owed to the defaulter by any government office or PSU | s.79(1)(a) | DRC-09, r.143 |
| Detain and sell the defaulter's goods under your control | s.79(1)(b) | DRC-10/11/12, r.144 |
| **Garnishee notice** to a bank, debtor or other third person | s.79(1)(c) | DRC-13/14, r.145 |
| Distrain and sell movable or immovable property | s.79(1)(d) | DRC-16/17/11/12, r.147 and r.151 |
| Certificate to the Collector (arrears of land revenue) | s.79(1)(e) | DRC-18, r.155 |
| Application to a Magistrate (recovered as a fine) | s.79(1)(f) | DRC-19, r.156 |
| Recovery from distinct persons (other GSTINs of the same PAN) | Explanation to s.79 | as above |
| Unpaid self-assessed tax and interest, no SCN needed | s.75(12); s.79 | DRC-01D, r.142B |

- Tax dues are a **first charge** on the property of the taxable person, subject to the IBC (s.82).
- A transfer of property to defraud revenue is void (s.81).
- **Instalments:** up to 24 monthly instalments on application (DRC-20) by Commissioner's order (DRC-21). Not allowed:
  - for self-assessed liability (s.80);
  - below Rs 25,000;
  - for existing defaulters; or
  - for someone refused instalments in the previous year (r.158(3)).
- **Overdraft or cash-credit accounts:** the Madras HC (03.04.2026) held they cannot be attached under s.79. `case-law/03` §10. Persuasive.

### 7.3 Provisional attachment (s.83; r.159)

- **Who:** only the **Commissioner** (or a delegate acting for him) may attach property, including bank accounts, provisionally. The Commissioner must have formed the opinion that it is necessary to protect revenue.
- **When:** after **initiation of any proceeding under Chapter XII, XIV or XV**, which includes s.73, 74 and 74A (s.83(1), as substituted from 01.01.2022).
- **Whose property:** the taxable person's, or that of a person under s.122(1A).
- **Procedure:**
  - Order in **DRC-22**; objection in **DRC-22A**; release in **DRC-23** (r.159(1), (5), (6)).
  - The attachment **lapses after 1 year** (s.83(2); r.159(2)).
- **CBIC guidelines of 23.02.2021 [read]:**
  - record the basis of the opinion on file;
  - do not attach routinely or mechanically;
  - keep the value close to the estimated dues;
  - hear objections and pass a reasoned order.
  - These guidelines predate the 2022 amendment of s.83(1), so their list of proceedings is out of date.
- **Courts:**
  - **Radha Krishan Industries (SC, 20.04.2021)**, **SC**: the opinion must rest on **tangible material**; the power is "draconian" and must be strictly construed.
  - **Kesari Nandan Mobile (SC, 2025 INSC 983)**, **SC**: the attachment lapses automatically after one year.
  - Telangana HC, TG-BINDING: *Greenfinch* (22.12.2022), *KMC Constructions*, *Aarush Enterprises*.
  - `case-law/03` §8 and §10; `05-telangana-high-court.md` rows 18-20.

### 7.4 Appeal, pre-deposit and stay of recovery

- **First appeal** (s.107(6)): the taxpayer must pay:
  - (a) the admitted amount in full; and
  - (b) **10% of the disputed tax**, up to **Rs 20 crore**.
  - **Penalty-only orders** (no tax demanded): 10% of the penalty (proviso inserted from 01.10.2025).
- **Effect of the pre-deposit:** recovery of the balance is **deemed stayed** (s.107(7)).
- **Second appeal to the GSTAT** (s.112(8)): a further **10%** of the remaining disputed tax, up to Rs 20 crore (or 10% of a penalty-only demand). Recovery of the balance is then stayed till disposal (s.112(9)).
- **Time limits:**
  - Taxpayer's appeal: 3 months, plus 1 month for sufficient cause (s.107(1), (4)).
  - Department's review: 6 months (s.107(2)).
- **Pre-deposit already paid:** Circ. 224/18/2024 [read] lets a payment made against the demand (through the liability register, or DRC-03 linked by DRC-03A) count as pre-deposit. It also stayed recovery while the GSTAT was not functioning, on payment plus an undertaking.
  - The GSTAT Hyderabad bench is reported to have started hearing on 20.04.2026 (`case-law/09` §8, Secondary). Normal s.112 limits now apply.
- **What to do:** once an appeal is filed with the pre-deposit, **stop recovery of the balance and lift attachments** (Calcutta and Delhi HCs; `case-law/03` §10).
- **Pending SC questions:**
  - Pre-deposit for penalty-only appeals: the SC is examining whether the date of the SCN or the date of the appeal decides it (*PVCON Engineering*, SLP 28059/2026, interim). `case-law/09` §5.
  - Condonation beyond the s.107(4) cap is also pending in the SC (`case-law/03` §8).

### 7.5 s.128A waiver (FY 2017-18 to 2019-20, s.73 demands)

- **What is waived:** interest and penalty on demands under a **s.73** notice, statement or order for **01.07.2017 to 31.03.2020**, if the **full tax** was paid by the notified date (s.128A(1)).
- **Notified date:** **31.03.2025** (Notf. 21/2024-CT [read], row 1).
- **Excluded:** erroneous refunds (s.128A(2)).
- **Pending appeal or writ:** it must have been withdrawn (s.128A(3); r.164(7)). For mixed-period demands, the appellate authority is told the appeal is not pursued for the 2017-20 portion (r.164(7) second proviso, inserted by Notf. 11/2025-CT).
- **Applications:** SPL-01 (notice) or SPL-02 (order) within 3 months of the notified date (r.164(1), (2), (6)).
- **Your role as adjudicating officer:**
  - **Pending s.73 SCN for 2017-20 with an SPL-01 filed:**
    - Decide the application. If you propose rejection, issue **SPL-03** (with a hearing) within 3 months of receipt; the applicant replies in SPL-04.
    - Accept by **SPL-05** or reject by **SPL-07**, within the r.164(13) time limits.
    - **If you issue nothing in time, the application is deemed approved** (r.164(14)).
    - After SPL-05 on a notice, **no DRC-07** is issued (r.164(11)(a)).
  - **s.74 SCN for 2017-20 where an appeal or court later finds no fraud:** after your s.75(2) re-determination order, the taxpayer can still apply **within 6 months** of it (s.128A(1) first proviso; Notf. 21/2024-CT row 2; r.164(6) proviso).
  - The proper officer for applications on notices is the s.73 officer. For orders it is the s.79 officer (r.164, Explanation).
- **Courts:**
  - Decide applications strictly on the s.128A and r.164 conditions. The Madras HC set aside rejections on grounds outside s.128A, such as non-existent suppliers (*A. Gurusamy*, 25.06.2026).
  - The Karnataka HC treated the filing deadline as directory (*Sri Laxmi Borewell*). The Madras HC treats the r.164 time limits as mandatory.
  - No Telangana ruling was found. `case-law/03` §7.
- **Further CBIC guidance:** Circ. 238/32/2024 and 248/05/2025, and Instr. 02/2025-GST (not re-read here).

---

## Part 8. One-page pre-signature checklist

1. Right section for the FY (73/74 up to 2023-24; 74A from 2024-25)? One FY per SCN (recommended; a composite s.74 SCN is lawful in Telangana under *Goldstone Infra* if each year is within its own limit)?
2. SCN date within s.73(2) / 74(2) / 74A(2)? Order date within s.73(10) / 74(10) / 74A(7), or the recorded extension? Any reliance on Notf. 09/2023 or 56/2023 noted with the SC pendency?
3. Am I the proper officer (tax-only amount, combined CGST + IGST, statements, CAA, migration)?
4. No earlier State SCN on the same subject matter (s.6(2)(b); *Armour Security*)?
5. Full SCN served **with** DRC-01, with a DIN/RFN (mandatory: *Gudla Vanaja*) and digitally signed (good practice), with RUDs, quantified tax, interest and penalty, and specific fraud facts if s.74 / 74A(5)(ii) (*G.R. Infra*)?
6. Service proved under s.169 by more than the portal if there is no response?
7. Hearing notice with date, time and venue issued; adjournments ≤ 3 with reasons; cross-examination and RUD requests decided before the order?
8. Order: facts, reply, findings on each issue, reasons (s.75(6)); nothing beyond the SCN (s.75(7)); interest; correct penalty clause; no double penalty (s.75(13)); payments credited?
9. Order with a DIN/RFN, digitally signed, uploaded with a DRC-07 that matches it (r.142(5); Instr. 04/2023)?
10. No recovery inside 3 months unless the Commissioner has directed it with reasons (s.78; Instr. 01/2024).

---

## Gaps and points not confirmed

1. **Interest rate under s.50(3):** Notf. 13/2017-CT (read) fixes 24%. Whether a later notification reduced it to 18% was not found in `data/notifications.csv` by subject. Check before quoting a rate.
2. **FY 2017-18 annual return due date for Telangana** (5 or 7 February 2020 under Notf. 06/2020-CT) not confirmed. That FY is closed in any case.
3. **Medchal Commissionerate's Zone** (assumed Hyderabad Zone, so the CAA for multi-Commissionerate DGGI cases is Rangareddy) not confirmed from a CBIC document.
4. **DRC-01A after 15.10.2020:** no High Court ruling squarely holding it optional (or mandatory) for post-amendment periods was found. The pre-amendment rulings come from web search (Secondary).
5. **Cross-examination:** Kerala and Gujarat HC rulings come from web search (Secondary) and are not in the case-law folder. No Telangana HC ruling was found.
6. **Adjudicator-level conversion from s.74 to s.73** (as opposed to s.75(2) after an appeal): no ruling found.
7. **Limitation for s.122 / s.125 penalty-only notices:** the Act sets none. No circular or ruling on a "reasonable period" was found.
8. **Proper officer for s.125, s.127, s.129 and s.130:** these come from Circ. 3/3/2017 and Circ. 41/15/2018, which were not re-read for this file.
9. **Circulars 122/41/2019 and 128/47/2019 (DIN), 238/32/2024 and 248/05/2025 (s.128A), 256/02/2026 (GSTAT appeals in CAA cases), Instructions 02/2022, 02/2023 and 05/2025:** listed in the CBIC index but not re-read here.
10. **SLP (C) 4240/2025** (s.168A notifications) is still pending as far as found. Check the SC case status before citing any extended date.
11. **Case-law status (updated 14.10.2026).** *Gudla Vanaja*, *Goldstone Infra*, *B.K. Steels*, *Balaji Filling Station* and *Brunda Infra* were read on Indian Kanoon (see `case-law/03`). *Bigleap* is overruled and should not be cited. W.P. 20731/2025 and W.P. 3204/2025 should still be pulled from tshc.gov.in before they are quoted in an order.

## Sources used

- **Statute:**
  - `text/cgst-act.md`: s.5, 6, 44, 50, 61, 65, 73, 74, 74A, 75, 76, 78-84, 107, 112, 122, 125-130, 160, 161, 168A, 169.
  - `text/cgst-rules.md`: r.26, 80, 88B, 99-102, 142, 142A, 142B, 143-161, 164.
- **CBIC portal, read in full (14.10.2026):**
  - Circulars 31/05/2018, 169/01/2022, 171/03/2022, 185/17/2022, 224/18/2024, 239/33/2024, 249/06/2025, 250/07/2025, 254/11/2025, 255/01/2026.
  - Instructions 04/2023-GST, 01/2024-GST (scanned; read from page images), 02/2021-22 [GST-INV], and the s.83 guidelines of 23.02.2021.
  - Notifications 13/2017-CT, 13/2022-CT, 09/2023-CT, 56/2023-CT, 21/2024-CT.
- **Project case-law files:** `03-demands-adjudication-appeals.md`, `05-telangana-high-court.md`, `06-registration-rectification.md`, `08-interest-penalty-returns-other.md`, `09-gaps-tribunal-and-updates.md` (all Secondary).
- **Web search (3 searches):** DRC-01A case law; cross-examination case law; Instruction 01/2024 commentary (superseded by reading the instruction itself). Links are given inline.
