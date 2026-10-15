# Refund Desk: plan for automating refund orders

Prepared 14 Oct 2026 for the Sangareddy CGST Division. Builds on Jarvis (`github.com/santoshbhaviri/jarvis`) and the project's knowledge base.

## What it does, in one line
You upload a refund application's documents. The app reads them, checks them against the law, our refund standard and the case law, works out the admissible amount, and gives you a ready-to-sign Word order (RFD-06) or deficiency/SCN notice (RFD-03 / RFD-08) on your letterhead. You review it, sign it and issue it on the portal.

## Recommended design: a "Refund Desk" tab inside Jarvis
Jarvis already has what this needs: your login, the Claude connection, Supabase, and document reading (PDF text and scanned pages). So it is cheaper and quicker to add one tab than to build a new app.

**On your desktop:** open Jarvis in Chrome or Edge and click **Install** in the address bar. It then opens in its own window from the Start menu or taskbar like any desktop program, and it updates itself. A separate Electron or Tauri program is only worth building if the office later wants the documents never to leave the computer at all.

## How one refund flows through it

1. **Upload** the case file: RFD-01 and its statement (1A / Annexure B), GSTR-2B, GSTR-3B and GSTR-1 for the period, invoices, and the category documents (shipping bills or BRC/FIRC for exports, SEZ endorsements, LUT, CA certificate where needed).
2. **Read (Claude).** Each document is read into fixed fields: category, period, dates of filing, turnover, net ITC, output tax, invoice-wise HSN and rates, export values. Claude Haiku reads scanned pages; Claude Sonnet handles the harder statements. Every figure keeps a note of the page it came from.
3. **Check and compute (program code, not AI).** Arithmetic must never be left to AI. The app:
   - applies the rule 89(4) / 89(5) formula;
   - checks the two-year limit and the relevant date;
   - matches ITC to GSTR-2B (Circular 197 para 1.3);
   - checks rates against Notification 5/2017-CT(R) for inverted duty;
   - runs every point of checklist C1 and the refund standard;
   - lists every gap, each with the rule or circular behind it.
4. **Your review screen.** You see the figures side by side with their source pages, the flags, and the proposed outcome (sanction in full, sanction in part, or RFD-08 first). You can correct any figure or decision before anything is drafted.
5. **Draft (Claude).** Claude fills the matching template (T1 to T8, or N1 for RFD-08) with the facts and your decisions. It writes the discussion and findings in our standard: every reply point answered, binding case law (Supreme Court and Telangana High Court) cited only where it applies, correct sections, rounding and appeal clause. The computation tables come straight from step 3, so they are exact.
6. **Word file out.** The order comes out as a .docx on the bilingual Government of India letterhead. You read it, edit if needed, sign, and upload RFD-06 on the portal yourself. The app never files anything.
7. **Learning.** When you edit a draft, the app records what you changed. Repeated corrections become new rules in the refund standard, so the next order starts closer to your style.

## What it reads from the knowledge base
The refund standard (`refund-order-learnings.md`), checklist C1, templates T1 to T8 and N1, the refund and Telangana sections of the case-law compendium, and the circular index. Together these are about 120 pages. They are sent with every case and kept in Claude's prompt cache, so after the first case each one costs a fraction. This is simpler and more reliable than searching the library piece by piece, because nothing relevant can be missed.

## Safeguards
- **Taxpayer data:** refund documents carry GSTINs and business figures. Before using real files, confirm the department's policy on processing them with an outside AI service. The Finance Ministry has issued advisories on AI tools, and some offices require approval. The Claude API does not train on what it receives.
- **Storage:** the app does not keep taxpayer documents after the draft is made, unless you choose to. Only the order you download remains.
- **Repository:** the Jarvis repository is public. Make it private (GitHub → Settings → Change visibility) before this work starts. No taxpayer document or real order should ever go into the repository.
- **Your decision stays yours:** a refund order is a quasi-judicial order. Courts quash orders that show no application of mind. The app proposes and you decide, and the review screen makes you confirm each rejected amount before drafting.

## Build in stages
| Stage | What you get | Test |
|---|---|---|
| 1 | Inverted-duty refunds (T1) end to end: upload, checks, computation, review screen, Word order | Re-run 3 to 4 of the inverted-duty orders we already reviewed (redacted) and compare |
| 2 | RFD-08 notice (N1) and RFD-03 deficiency memo; partial rejection with PMT-03 re-credit | Same cases where a notice was needed |
| 3 | Exports and SEZ (T2 to T6), cash ledger (T7), pre-deposit (T8) | One real file per category |
| 4 | Dashboard: pending refunds by due date (60-day limit and interest under s.56) | Your live list |
| 5 | Adjudication: SCNs under s.73/74 and orders after replies, using the case-law base | Later |

## Running cost (Claude API, prepaid credit)
Roughly ₹30 to ₹60 per refund case: reading 10 to 20 pages, the checks, and one full draft. The knowledge base is cached across cases. A month of 50 cases would be about ₹2,000 to ₹3,000. Your existing Claude credit in Jarvis covers it.

## What is needed from you
1. **Where to build:** a tab inside Jarvis (recommended) or a separate app.
2. **Permission check:** confirm you may process real refund files this way. Until then we build and test with redacted copies.
3. **Repository access:** make Jarvis private, and allow this project to push to it, so changes come as a draft for you to approve (the same way Evolve works).
4. **One complete inverted-duty refund file**, redacted (GSTIN and name blanked), with the final order you issued, to test stage 1 against.
