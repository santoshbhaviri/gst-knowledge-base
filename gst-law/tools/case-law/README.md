# Rebuilding the case-law compendium

After adding or correcting entries in `gst-law/case-law/01-…09-*.md` (or adding a new `10-*.md`), rebuild the single-file compendium, the CSV index and the Word copy:

```
cd /mnt/project-files/gst-law/tools/case-law
python3 -I build.py head.md
cd ../../case-law
pandoc GST-case-law-compendium.md -f markdown-yaml_metadata_block -o GST-case-law-compendium.docx \
  --reference-doc=/mnt/project-files/gst-orders/templates/source/reference.docx --toc --toc-depth=2
```

Entry format the parser expects: `### <Case> - <Court> - <date>` followed by bullets `- Citation / case no.:`, `- Holding:`, `- Binding:`, `- Later history:`, `- Use in orders:`, `- Source:`, `- Verified:`. Part 1-2 text (how to use, where courts disagree) is in `head.md`; edit it when a split is settled. A new file number needs a domain name in `DOMAIN` in build.py.
