---
name: gst-law-knowledge-base
description: Where the GST law knowledge base lives, how the CBIC portal API was read, and which sources are still blocked
metadata:
  type: project
---

GST law knowledge base: /mnt/project-files/gst-law/. Start at 00-overview.md. Since 2026-10-12 it holds the full current CBIC text of the Acts and Rules (text/), a complete CSV index of all GST notifications (1,283), circulars (272), instructions and orders (data/), and 04a-circulars-full-list.md.

CBIC portal (taxinformation.cbic.gov.in) access recipe: TLS needs the Sectigo intermediate from http://crt.sectigo.com/SectigoPublicServerAuthenticationCAOVR36.crt (DER) appended to a copy of /root/.ccr/ca-bundle.crt; never disable verification. Skip the browser: POST /api/authenticate-token gives an anonymous token; send it as header `Authorization1: homeToken <token>`. Useful endpoints (GST taxId 1000001): cbic-notification-msts/fetchNotificationByYearAndCategory?year=&category=&taxId=&page=0&size=2000; cbic-circular-msts/fetchAllCircularsByTaxId/1000001; cbic-act-section-msts/viewAllSectionByActId/{actId}; cbic-rule-section-msts/viewBySectionAllRules/{ruleId}; section HTML at /content/html/<contentFilePath with forward slashes>; PDFs via <service>/download/{id}/ENG (base64 JSON). Connection resets are common, so retry.

As of 2026-10-12 the portal's newest items are 02/2026-CT (7 May 2026), Circular 256 (25 Jul 2026), Instruction 01/2026-GST (3 Aug 2026). Finance Act 2026 ss.153–155 not yet notified.

Council meetings 1–54 were checked against signed minutes on 2026-10-12 (per-meeting notes in gst-law/data/council-minutes-check/). Use gstcouncil.gov.in without www; www.gstcouncil.gov.in and www.pib.gov.in are blocked, and pib.gov.in redirects to www, so PIB is unreadable until www.pib.gov.in is allowed.

egazette.gov.in recipe: append letsencrypt.org/certs/gen-y/int-yr2.pem and root-yr-by-x1.pem to a copy of the CA bundle. For Chromium, intercept every request with Playwright ctx.route and fetch it in Node over a CONNECT tunnel with that CA (the proxy cannot verify the site itself); turn redirects into a location.replace page, and click from default.aspx to SearchMenu (direct links go to error.aspx). Search by Ministry (Finance = 18), Month/Year; results are 15 per page. Scripts are in gst-law/tools/egazette/ (run: S=<dir with bundle-le.pem> MONTHS=5 ONE=1 node eg.js ./t4.js). The site resets connections often, so retry. Only Oct 1–12 2026 was fully searched (no GST items).

**Why:** later threads should not rediscover the API or redo the download.
**How to apply:** read 06-sources-and-gaps.md first; re-run the CSV build if newer items are needed.

Related: [[project-goals]].
