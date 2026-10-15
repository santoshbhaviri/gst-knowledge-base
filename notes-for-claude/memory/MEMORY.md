# Project: Excellence

## User
- Account name "Priyanka", but the person writing identifies as Santosh (GitHub: santoshbhaviri). Assistant Commissioner, Sangareddy CGST Division, Medchal CGST Commissionerate, India. He isn't technical, so give him settings steps one at a time. He likes rough time frames and sets deadlines, which are in IST.
- He cares about how orders look as well as their content: a bilingual Government of India letterhead with the division name and "GST: One Nation, One Tax", and a clean, neat layout.

## Goals (stated 2026-10-12)
Use GST and customs trade data to help the country: 1) rapid economic growth, 2) revenue maximization (new revenue sources and preventing leakages), 3) formalization of the economy, 4) trade facilitation and ease of doing business, 5) supply chain management and logistics.

## Work so far
- Step 1: understand GST law, finished on 2026-10-12. The knowledge base is in /mnt/project-files/gst-law/; start with 00-overview.md, and gaps are in 06-sources-and-gaps.md.
  - It has the full current Acts and Rules from CBIC and an index of all 1,283 notifications and 256 CGST circulars.
  - Newest official items: 02/2026-CT (7 May 2026), Circular 256 (25 Jul 2026), Instruction 01/2026-GST (3 Aug 2026).
  - The Finance Act 2026 changes to s.15(3), 34 and 54 are not yet in force.
  - Council meetings 1 to 54 were checked against the signed minutes, with 12 corrections.
  - Known gap: state SGST variations.
- User's primary source: taxinformation.cbic.gov.in. It is a single-page app, so use Playwright with Chromium; its robots.txt refuses WebFetch.
- Refund orders: reviewed on 2026-10-12. The standard is in [[refund-order-learnings]] and /mnt/project-files/gst-orders/refund-order-learnings.md.
  - Template orders T1 to T8, the N1 RFD-08 notice and the C1 updated checklist are in /mnt/project-files/gst-orders/templates/; start with 00-read-me-first.
  - The templates have been revised with the new letterhead. The user's target is 8.5 or more out of 10, ideally 9.5.
- Case law: 359 GST judgments in /mnt/project-files/gst-law/case-law/ (start 00-read-me-first.md; one-file GST-case-law-compendium.md/.docx). Full-text check finished 15 Oct 2026: 293 verified on Indian Kanoon with link, quote and para; 64 not online (GSTAT, AARs) stay "read before quoting"; 2 doubtful, 3 no longer good law. Devi Electronics (Delhi HC, 1 Oct 2026) allows withholding refund under s.54(11) during investigation. See [[gst-caselaw-knowledge-base]].
- Refund automation app (Refund Desk in Jarvis, repo santoshbhaviri/jarvis): plan of 2026-10-14 in /mnt/project-files/refund-automation/plan.md. See [[refund-desk-plan]].
- Adjudication and appeals module (14 Oct 2026): /mnt/project-files/gst-law/adjudication/, SCN review and templates A1–A5, B1–B5, C2 in gst-orders. See [[adjudication-knowledge]].
  - Key Telangana HC rulings applied (14 Oct): Full Bench in Gudla Vanaja (30.09.2026) says an SCN or order without a DIN/RFN is invalid, and overruled Bigleap (portal-issued notice valid without visible signature); Goldstone Infra (27.01.2026) allows one notice covering several years.
  - Asked user on 14 Oct to check DIN/RFN on portal for SCNs S1 to S10 and re-issue any lacking one.
  - NSE archive of published orders won't connect; asked user for 2 or 3 good orders from his Commissionerate as models.
- Registration module (finished 14 Oct 2026): /mnt/project-files/gst-law/registration/ and templates R1–R10 in gst-orders/templates (Range Superintendent is the proper officer; appeals go to JC (Appeals); Telangana goods threshold is Rs 20 lakh). See [[registration-knowledge]].
- Do not name taxpayers, GSTINs or taxpayer-linked amounts in shared files or replies.

## Current priority (decided 2026-10-14)
- User wants a strong knowledge base across all domains first, then application. Next domain: adjudication and appeals (s.73/74/74A/75, DRC-01A to DRC-07, appeals, GSTAT), because orders are most at risk of court challenge there.
- Path agreed in the "GST court precedents" thread: 1) procedure guide, 2) court-proof checklist of grounds courts quash SCNs/orders on, 3) SCN, hearing notice and order templates on the letterhead, 4) test on the user's own redacted SCNs and orders (requested 5 to 10), 5) then registration, audit and appeal-side work.

## Pending with the user (as of 15 Oct 2026)
- User asked how to move this project to his own Claude account. Told him projects can't be transferred; offered to pack all files plus a preferences/notes file into one zip once the running threads finish. Both threads finished by 15 Oct 02:51 UTC; reminded him and awaiting his Yes/No.
- Waiting on him: DIN/RFN check for S1 to S10; 5 to 10 redacted SCNs/orders to test templates; 2 or 3 model orders.

## Environment notes
- The project uses a custom cloud environment with Allowed domains. Changes only reach sessions started after the change, so start a fresh thread after the user edits it.
- Allowed domains (as of 2026-10-12): taxinformation.cbic.gov.in, crt.sectigo.com (the CBIC server leaves out its intermediate certificate), cbic-gst.gov.in, egazette.gov.in, gstcouncil.gov.in, pib.gov.in, www.pib.gov.in, letsencrypt.org.
- The account can hit usage limits during long thread work. If a thread fails on a limit, tell the user and resume it later.
