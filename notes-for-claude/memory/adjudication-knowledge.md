---
name: adjudication-knowledge
description: Where the adjudication and appeals module, the review of 11 division SCNs, and the A/B/C2 adjudication templates live (built 2026-10-14)
metadata:
  type: project
  modified: 2026-10-14T07:58:24.291Z
---

On 2026-10-14 the user asked to strengthen adjudication and appeals first ("a lot of risk of being challenged in courts"), then build a strong knowledge base across all domains, before applying it (e.g. the Refund Desk app, [[refund-desk-plan]]).

Built:
- /mnt/project-files/gst-law/adjudication/ (start at 00-read-me-first.md): 01 procedure DRC-01A→DRC-07 with year-wise deadlines; 02 appeals, review, GSTAT, litigation (Circular 207/1/2024 monetary limits); 03 court-proof checklist (grounds A–H, 44 SCN + 46 order checks); 04 survey of model SCNs and orders (CBIC Master Circular 1053/02/2017-CX is the best public drafting guide; zone OIO sites are blocked).
- Review of 11 real division SCNs (labels S1–S11, ids in .notes/inputs.md; unredacted, so never name them): /mnt/project-files/gst-orders/adjudication/scn-evaluation.md (avg 5.1/10). S4 and S9 (mining) multiply the per-tonne price by 12.5 instead of dividing (about 156x overstatement), verified by the thread.
- Templates A1–A5 (SCN side), B1–B5 (orders), C2 checklist in /mnt/project-files/gst-orders/templates/ (sources in source/src). style.py now prints "Notice No." in the header for titles starting "Template A".

Updated 15 Oct 2026 for verified case law: ground B2 is now 'no DIN/RFN' (Gudla Vanaja, TG Full Bench 30.09.2026, overrules Bigleap); composite multi-year SCN lawful in TG (Goldstone Infra) but one per year recommended; B.K. Steels was a consent order; grounds must be in the SCN body (A1 Adil Traders). Asked the user (15 Oct) to check portal DIN/RFN for S1-S10 (S7-S10 show none).

Open points: the s.50(3) interest rate (Notification 13/2017-CT text says 24%; a reported cut to 18% is unconfirmed); zone and NSE/BSE sites with published OIOs are not reachable.

**Why:** later threads continue this domain-by-domain hardening.
**How to apply:** check new SCNs and orders against 03-court-proof-checklist.md and the templates; add each new domain in the same pattern (procedure, checklist, real-case review, templates).
