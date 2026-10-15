---
name: refund-desk-plan
description: The user's goal to automate refund orders in an app built on Jarvis (React/Netlify/Supabase/Claude); plan and open decisions as of 2026-10-14
metadata:
  type: project
  modified: 2026-10-14T06:44:08.739Z
---

On 2026-10-14 the user asked for an app that takes uploaded refund documents, analyses them against the knowledge base and produces high-quality orders he can serve. Plan: /mnt/project-files/refund-automation/plan.md.

Jarvis = github.com/santoshbhaviri/jarvis (his own app, PUBLIC as of 2026-10-14). Stack: React/Vite PWA on Netlify (drjarvis.netlify.app), Netlify functions (30 s limit) calling the Claude API (Sonnet 5.5 smart / Haiku 5.5 quick, prompt caching, key stored in Netlify Blobs, owner-only via JARVIS_OWNER_EMAIL), Supabase auth + knowledge tables (jarvis_notes, jarvis_documents, jarvis_passages with tsvector search, jarvis_chats). Its "Evolve" tab has Claude build changes via GitHub issues/PRs that he approves.

Recommended design: a "Refund Desk" tab in Jarvis, installed on desktop as a PWA. Claude extracts fields from documents, code (not AI) does the rule 89 arithmetic and checks, the officer confirms on a review screen, then Claude fills templates T1–T8/N1 into a letterhead .docx. Stage 1 = inverted duty (T1).

Open as of 2026-10-14: (1) Jarvis tab vs separate app (decision card posted; default Jarvis tab); (2) department permission to send taxpayer documents to the Claude API; (3) make the repo private and grant push access; (4) a redacted inverted-duty test file plus his issued order.

**Why:** a later thread picking up the build must not restart the design or forget the confidentiality caveats.
**How to apply:** never commit taxpayer documents or real orders to the repo; keep the officer as the decision-maker. Related: [[refund-order-learnings]], [[gst-caselaw-knowledge-base]].
