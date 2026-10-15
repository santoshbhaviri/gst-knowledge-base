# START HERE — GST "Excellence" project (exported 15 Oct 2026)

This export (Part 1, plus Part 2 with your own uploads) holds all the work from the "Excellence" project, so it can continue in a new Claude project on Santosh's own account.

---

## Part 1. Steps for you (Santosh)

### Easiest way: from GitHub (no uploading)
This knowledge is in your private GitHub repository **santoshbhaviri/gst-knowledge-base**. Do these one at a time:
1. Sign in to claude.ai with your own Claude account.
2. Connect GitHub to that account (claude.ai will show a Connect GitHub button the first time you add a repository).
3. Create a new project and, in its settings, add the repository **santoshbhaviri/gst-knowledge-base**.
4. Send Claude: "Read START-HERE.md in the repository first, then tell me what is pending."
5. If you want Claude to keep using your own orders and SCNs, upload the Part 2 zip to the project as well.

### Other way: from the zip files

Do these one at a time.

1. Download this zip to your computer. You do not need to open it.
2. Sign in to claude.ai with your own Claude account.
3. Create a new project. Give it a name, for example "Excellence".
4. Open the new project and upload this zip file (drag it in, or use the upload or attach button).
5. Also upload Part 2 (the zip whose name ends in "part2-your-uploads"). It holds your own uploaded orders and SCNs, the Speaking orders archive and the Boost Jar PDF. Keep it private: some files are unredacted taxpayer documents.
6. Send Claude this first message:

   > Please unzip the file I uploaded and read START-HERE.md first, then the files in notes-for-claude. Then tell me what is pending.

7. Set up the same website access (see "Websites" just below), so Claude can keep the knowledge up to date. You can do this later; the knowledge in the zip works without it.

That is all. Claude will pick up where we left off.

### Websites: how to let the new project reach them
Do these one at a time in the new project:
1. Open the project's settings and find **Cloud environment**.
2. Click the gear beside the selected environment.
3. Under **Network access**, choose **Limited** (on some app versions it is called **Custom**) and keep **Allow package managers** ticked.
4. In **Allowed domains**, add each website in the list below, one per line.
5. Save. Then start a new conversation or thread, because older ones do not see the change.

Official steps: https://code.claude.com/docs/en/cloud-environments#network-access

Allowed domains to add:
```
taxinformation.cbic.gov.in
cbic-gst.gov.in
crt.sectigo.com
egazette.gov.in
letsencrypt.org
gstcouncil.gov.in
pib.gov.in
www.pib.gov.in
indiankanoon.org
tshc.gov.in
www.sci.gov.in
```


---

## Part 2. Notes for the next Claude

Read this whole section, then `notes-for-claude/memory/MEMORY.md` and the other memory files there. They are the project memory as it stood on 15 Oct 2026. Save them into your own project memory if you have one.

### Who the user is
- Account display name may differ; the person is **Santosh** (Dr. B. Santosh Kumar), Assistant Commissioner, Sangareddy CGST Division, Medchal CGST Commissionerate, Hyderabad, India. GitHub: santoshbhaviri.
- He is not technical. Give settings or setup steps one at a time, in plain words.
- He likes rough time frames and sets deadlines in IST.
- He cares how orders look as well as their content: bilingual Government of India letterhead, division name, "GST: One Nation, One Tax", clean neat layout (navy band with saffron and green rules, page numbers, shaded table headers). Details: `notes-for-claude/memory/order-letterhead.md`.
- Quality target for templates and orders: 8.5 or more out of 10, ideally 9.5.
- Never name taxpayers, GSTINs or taxpayer-linked amounts in shared files or replies.

### His goals (stated 12 Oct 2026)
Use GST and customs trade data to help the country: 1) rapid economic growth, 2) revenue maximisation (new sources, stopping leakages), 3) formalisation of the economy, 4) trade facilitation and ease of doing business, 5) supply chain and logistics.

### Agreed way of working (14 Oct 2026)
Build a strong knowledge base domain by domain first, then apply it. Pattern per domain: procedure guide, court-proof checklist, review of his real cases, templates on the letterhead. Done so far: law base, refunds, case law, adjudication and appeals, registration. Next: audit and appeal-side work.

### What is in this zip
| Folder | What it is | Start with |
|---|---|---|
| `gst-law/` | Full CGST/IGST/UTGST Acts and Rules (CBIC text), index of 1,283 notifications and all circulars, GST Council meetings 1–54 checked against minutes | `gst-law/00-overview.md`, gaps in `06-sources-and-gaps.md` |
| `gst-law/case-law/` | 359 GST judgments; 293 verified on Indian Kanoon with link, quote and para | `00-read-me-first.md`; one-file `GST-case-law-compendium.md` / `.docx` |
| `gst-law/adjudication/` | s.73/74/74A/75 procedure, appeals/GSTAT, court-proof checklist, survey of model orders | `00-read-me-first.md` |
| `gst-law/registration/` | Registration procedure, checklist, CBIC source PDFs | `00-read-me-first.md` |
| `gst-orders/templates/` | Word templates: refunds T1–T8, N1, C1; adjudication A1–A5, B1–B5, C2; registration R1–R10. Markdown copies in `markdown/`; sources and builder in `source/` (edit `source/src`, run `source/build.py`, style in `style.py`) | `00-read-me-first.docx` |
| `gst-orders/` | Refund drafting standard (`refund-order-learnings.md`), rating of his own speaking orders, SCN review (`adjudication/`), case working notes (`cases/`) | |
| `refund-review/` | Review of his six RFD-06 orders (12 Oct) | |
| `refund-automation/plan.md` | Plan for a "Refund Desk" tab in his Jarvis app (repo santoshbhaviri/jarvis) | |
| `.notes/inputs.md` | Notes on the files he uploaded (labels Order 1–6, A–M, S1–S11, SO numbers). The uploads themselves are not in this zip | |
| `notes-for-claude/memory/` | Project memory files | `MEMORY.md` |

### Key legal points already applied
- Telangana HC Full Bench, Gudla Vanaja (30.09.2026): an SCN or order without a DIN/RFN is invalid; it overruled Bigleap (visible signature not needed on portal notices).
- Goldstone Infra (TG DB, 27.01.2026): one SCN may cover several years (one per year still recommended).
- Devi Electronics (Delhi HC, 01.10.2026): refund may be withheld under s.54(11) during investigation.
- Finance Act 2026 changes to s.15(3), 34 and 54 were not yet in force as of 12 Oct 2026.
- Newest official items seen: Notification 02/2026-CT (7 May 2026), Circular 256 (25 Jul 2026), Instruction 01/2026-GST (3 Aug 2026).

### Still waiting on Santosh (as of 15 Oct 2026)
1. Check on the portal whether SCNs S1 to S10 carry a DIN/RFN (S7–S10 showed none) and re-issue any that lack one. Most urgent.
2. 5 to 10 redacted SCNs/orders to test the adjudication templates.
3. 2 or 3 good model orders from his Commissionerate.
4. Refund Desk app decisions: Jarvis tab vs separate app (default Jarvis tab); department permission to send taxpayer documents to the Claude API; make the Jarvis repo private; a redacted inverted-duty test file with his issued order.

### Open research points
- s.50(3) interest rate (24% in Notification 13/2017-CT text; reported cut to 18% unconfirmed).
- Whether Telangana is notified for biometric Aadhaar under rule 8(4B).
- State SGST variations not covered.

### Websites used as sources
| Website | Used for |
|---|---|
| taxinformation.cbic.gov.in | Main source (Santosh's preferred): Acts, Rules, notifications, circulars, instructions, forms, via its API (recipe in memory/gst-law-knowledge-base.md and registration-knowledge.md) |
| cbic-gst.gov.in | CBIC GST pages |
| crt.sectigo.com | Intermediate certificate the CBIC server omits (needed for TLS) |
| egazette.gov.in (+ letsencrypt.org for its certificates) | Gazette search for new notifications (scripts in gst-law/tools/egazette/) |
| gstcouncil.gov.in (no www) | Council meeting minutes 1–54 |
| pib.gov.in / www.pib.gov.in | Press releases |
| indiankanoon.org | Full judgment text, used to verify the case law (curl with a browser user-agent, one request per 3 s) |
| tshc.gov.in | Telangana High Court judgments |
| www.sci.gov.in | Supreme Court judgments |
| Via web search only: taxguru.in, taxscan.in, taxmann.com, livelaw.in, taxo.online, firm alerts | Leads on new rulings; always verify on a primary source |

Blocked or unreachable last time: www.gstcouncil.gov.in, nsearchives.nseindia.com, zone OIO sites.

Part 2 (`your-uploads/`) holds his own uploads with file extensions added; `your-uploads/what-each-file-is.md` maps ids to labels (Order 1–6, A–M, S1–S11, SO numbers). Many are unredacted: never quote taxpayer names or GSTINs.

### Environment notes (the old project's cloud setup)
- His main source is taxinformation.cbic.gov.in, a single-page app; the API recipe is in `notes-for-claude/memory/gst-law-knowledge-base.md` (needs the Sectigo OV R36 intermediate certificate added to the CA bundle; never disable TLS checks).
- The old project used a custom environment with these allowed domains: taxinformation.cbic.gov.in, crt.sectigo.com, cbic-gst.gov.in, egazette.gov.in, gstcouncil.gov.in, pib.gov.in, www.pib.gov.in, letsencrypt.org, and later indiankanoon.org, tshc.gov.in, www.sci.gov.in. A new project may need the same list set up again; walk him through it one step at a time.
- The account can hit usage limits during long work; if so, tell him and resume later.
