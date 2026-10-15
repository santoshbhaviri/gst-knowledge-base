---
name: gst-caselaw-knowledge-base
description: Where the GST case-law (judgments) knowledge base lives, how reliable it is, and what remains to verify
metadata:
  type: project
  modified: 2026-10-13T11:43:19.449Z
---

GST case law lives inside the GST knowledge base at /mnt/project-files/gst-law/case-law/ (moved there 2026-10-14 at the user's request; the old gst-caselaw/ folder was removed). Start at 00-read-me-first.md. Single file: GST-case-law-compendium.md (+ .docx), index case-law-index.csv. Domain files 01-09 (refunds, ITC, demands/appeals, arrest/landmark, Telangana HC, registration/rectification, levy/valuation/classification, interest/penalty/other, updates/GSTAT/AAR); 356 entries, each with source links, binding status (Telangana HC flagged BINDING IN TELANGANA) and later history.

On 14-15 Oct 2026 all entries were checked against judgment text on Indian Kanoon (indiankanoon.org, tshc.gov.in and www.sci.gov.in are now allowed; nsearchives.nseindia.com times out). Result: 359 entries, 293 Primary (judgment link first, "Key words" quote with para), 64 Secondary (mostly GSTAT/AAR, not on Indian Kanoon), 2 [DOUBTFUL] (file 08). Each domain file ends with a "Verification log". Key change: Telangana HC Full Bench Gudla Vanaja (30.09.2026) overruled Bigleap: no DIN/RFN = invalid; visible signature not required. Goldstone Infra (TG DB 27.01.2026) upholds multi-year SCNs. Indian Kanoon: curl with a browser UA, one request per 3 s.

WebSearch has a shared limit of about 200 searches per turn across all subagents; five parallel agents exhausted it, so split big research over turns.

Rebuild the compendium after editing domain files: gst-law/tools/case-law/README.md. The user wants this kept as a repository he draws on from time to time, so add new SC and Telangana HC rulings to it.

**Why:** later threads should verify from judgment text rather than re-research.
**How to apply:** new entries must be read on Indian Kanoon before adding; rebuild with gst-law/tools/case-law/README.md (build.py marks Binding 'NO LONGER GOOD LAW' as overruled). Related: [[gst-law-knowledge-base]].
