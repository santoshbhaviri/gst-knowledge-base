---
name: registration-knowledge
description: Where the registration module (procedure, court-proof checklist, CBIC sources) and the R1-R10 registration templates live (built 2026-10-14)
metadata:
  type: project
  modified: 2026-10-14T22:00:10.163Z
---

Step 5 of the agreed path (after [[adjudication-knowledge]]): registration domain, built 2026-10-14.

- /mnt/project-files/gst-law/registration/ (start 00-read-me-first.md): 01 procedure (ss.22-30, rules 8-26, forms and time tables, 57th Council pending changes); 02 court-proof checklist (82 pre-signing checks, 30 grounds R-A to R-I); sources/ holds CBIC PDFs (Circulars 1/2017, 69/2018, 95/2019, 145/2021, 148/2021, 158/2021, 223/2024; Instructions 01/2023, 02/2024, 03/2025, 04/2025; REG forms).
- Templates R1-R10 in /mnt/project-files/gst-orders/templates/ (src in source/src). New common blocks letterhead_range.md, reg_sign.md, reg_appeal.md. style.py: a letterhead containing "SUPERINTENDENT" prints the Superintendent's office line; R-series header label is Notice/Order/Report/Note from the title.
- Key facts found: Range Superintendent is proper officer for ss.28-30 and rules 9, 19, 22, 23, 25 (Circular 223/17/2024); appeals against his orders go to Joint Commissioner (Appeals) or above (rule 109A(1)(b)); Telangana is excluded from the ₹40 lakh goods threshold (Notf 10/2019-CT).
- Open: whether Telangana is notified for biometric Aadhaar under rule 8(4B) (last seen 54/2023-CT: AP, Gujarat, Puducherry).
- CBIC PDFs download via POST /api/authenticate-token then GET /content/pdf/<cbic_pdf_path> with Bearer token (returns JSON base64); forms via /api/cbic-form-msts/download/<id>/ENG. Needs the Sectigo OV R36 intermediate added to the CA bundle.

**Why:** later threads extend domain by domain (audit and appeal side next).
**How to apply:** use the R-series and checklist for registration work; re-check after the 57th Council registration rules are notified.
