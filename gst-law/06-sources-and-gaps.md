# Sources used, and what is still missing

**Last updated:** 17 Oct 2026 (re-check for new items; earlier: 12 Oct 2026, Council minutes 1 to 54 and the Gazette)

## Reached
| Source | Used for |
|---|---|
| **taxinformation.cbic.gov.in** (CBIC Tax Information Portal, the primary source) | **Full text** of the CGST, IGST, UTGST and Compensation Acts and the CGST, IGST and Compensation Cess Rules ([text/](text/)); the **complete index** of GST notifications (1,283), circulars (272), instructions (43) and orders (39) ([data/](data/)); PDFs of the 2025–26 rule amendments, 16/2025-CT, 02/2026-CT, 01/2026-CTR and the Finance Act, 2026 |
| cbic-gst.gov.in | Home page notices (advisories to 9 Oct 2026) |
| gstcouncil.gov.in, pib.gov.in (earlier session) | Meetings 1–55 dates, venues and minutes links; 55th to 57th press releases and FAQs |
| **gstcouncil.gov.in (12 Oct 2026)** | Signed minutes of meetings 1 to 54, all downloaded and checked; results per meeting in [data/council-minutes-check/](data/council-minutes-check/). Use the bare host: `www.gstcouncil.gov.in` is still blocked |
| **egazette.gov.in (12 Oct 2026, partial)** | Finance Ministry list for 1–12 Oct 2026 (6 entries, none a GST notification) and the first page of May 2026. Needs the Let's Encrypt YR2 intermediate and the Root YR cross-sign from letsencrypt.org/certs/gen-y/ added to a copy of the CA bundle; the site resets connections often, so retry |
| Secondary trackers (earlier session) | Press reports of 2026 changes; no longer needed for notification or circular numbers |

**How the CBIC portal was read.** It is a single-page app backed by a public JSON API (`/api/...`) that uses an anonymous token issued to every visitor. The server leaves out its Sectigo intermediate certificate, so the intermediate was fetched from crt.sectigo.com and added to a local trust bundle; certificate checking stayed on.

## Blocked or not reachable now
| Source | Problem | Effect |
|---|---|---|
| **www.pib.gov.in** (and www.gstcouncil.gov.in) | pib.gov.in redirects every page to www.pib.gov.in, which the environment refuses (403) | PIB press releases unreadable. Needs `www.pib.gov.in` added to Allowed domains |

## Gaps to close
1. **Council meetings 1 to 54:** closed. Checked against signed minutes; PIB press releases for them were not cross-checked (blocked).
2. **Anything issued after the CBIC portal's latest entries** (02/2026-CT of 7 May 2026, 01/2026-CTR of 30 Apr 2026, Circular 256 of 25 Jul 2026, Instruction 01/2026 of 3 Aug 2026). The portal shows nothing newer. The Gazette is now readable but only partly searched: 1–12 Oct 2026 shows no GST notification; May to September 2026 still need a full pass (results are paged and the site is slow).
3. **Commencement of Finance Act, 2026 ss.153 to 155** (ss.15(3), 34, 54): not notified per CBIC as of 12.10.2026; nothing in the Gazette for 1–12 Oct 2026; earlier months not yet searched in the Gazette.
4. **Circular and notification contents:** the index has CBIC's one-line subjects. Full texts were read only for the 2025–26 rule amendments and a few key notifications; any other can be downloaded on request.
5. **State-specific deviations** in the SGST Acts and State Tax notifications: not on CBIC; needs State portals.
6. GSTN advisories (gst.gov.in) are not covered.

## Re-check of 17 Oct 2026
- Done from a session that could not reach the CBIC portal, the Gazette or the court sites directly (no allowed-domains list), so it relied on trackers (gstindiaonline, a2ztaxcorp, ICAI IDTC), news and Indian Kanoon read through web fetch.
- **Notifications, circulars, instructions:** nothing newer than 02/2026-CT (7 May 2026), Circular 256/02/2026-GST (25 Jul 2026) and Instruction 01/2026-GST (3 Aug 2026) was found. **Confirm on the CBIC portal** when the allowed domains are set up again.
- **57th Council (8 Oct 2026):** no implementing notification or amending Bill found. CBIC outreach with trade on the reforms on 15-16 Oct 2026 (Hyderabad, Chennai, Bengaluru); a centralised GST administration for Central-jurisdiction taxpayers was floated for feedback.
- **Finance Act 2026 ss.153-155 (ss.15(3), 34, 54):** no commencement notification found.
- **Case law:** 5 judgments added (see case-law/09, "Update log (17 Oct 2026)").

## Closed this session
- Council meetings 1 to 54 checked against signed minutes, with 12 corrections (12 Oct 2026).
- Notifications after 02/2026-CT: none on CBIC.
- Finance Act, 2026 commencement: read from the Act (s.1(2)); s.156 from 01.04.2026; ss.153–155 pending; s.157 on assent.
- 3rd to 5th CGST Amendment Rules, 2025: read in full and summarised in [02-cgst-rules.md](02-cgst-rules.md).
- Circulars 1 to 241: tabulated in [04a-circulars-full-list.md](04a-circulars-full-list.md).
