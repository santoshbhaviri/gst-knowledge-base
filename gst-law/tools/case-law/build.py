import json, re, os, csv, sys
sys.path.insert(0, os.path.dirname(__file__))
from parse import entries, D, FILES

DOMAIN = {
 "01": "Refunds", "02": "Input tax credit", "03": "Demands, adjudication and appeals",
 "04": "Arrest, search and landmark rulings", "05": "Telangana High Court (all issues)",
 "06": "Registration, cancellation and rectification", "07": "Levy, valuation and classification",
 "08": "Interest, penalty, returns and other procedure", "09": "Updates, gaps and GSTAT/AAR",
}
SKIP = ("Finance Act", "57th GST Council")

def domain(e):
    n = e["file"][:2]
    if n == "09":
        i = e["issue"]
        for k, v in [("refund", "Refunds"), ("input tax", "Input tax credit"), ("demands", "Demands, adjudication and appeals"),
                     ("arrest", "Arrest, search and landmark rulings"), ("Telangana", "Telangana High Court (all issues)"),
                     ("GSTAT", "GST Appellate Tribunal (GSTAT)"), ("Advance", "Advance rulings (persuasive only)")]:
            if k.lower() in i.lower(): return v
        return DOMAIN[n]
    return DOMAIN[n]

def level(e):
    c = (e["court"] + " " + e.get("Binding", "") + " " + e["date"]).lower()
    if re.search(r"no longer good law|overruled", e.get("Binding", ""), re.I): return "Overruled"
    if "telangana" in c and "binding in telangana" in c: return "Binding in Telangana"
    if c.startswith("supreme") or "supreme court" in e["court"].lower(): return "Supreme Court (binding)"
    if "gstat" in c or "tribunal" in e["court"].lower(): return "Tribunal"
    if "aar" in e["court"].lower() or "advance" in e["court"].lower(): return "AAR/AAAR"
    return "Persuasive"

def clean(s, n):
    s = re.sub(r"\*+", "", s or "").replace("|", "/").strip()
    s = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", s)
    return s if len(s) <= n else s[:n].rsplit(" ", 1)[0] + "…"

E = [e for e in entries() if not e["case"].startswith(SKIP)]
order = list(dict.fromkeys(list(DOMAIN.values())[:8] + ["GST Appellate Tribunal (GSTAT)", "Advance rulings (persuasive only)", DOMAIN["09"]]))
for e in E: e["domain"] = domain(e); e["level"] = level(e)

# CSV
with open(os.path.join(D, "case-law-index.csv"), "w", newline="", encoding="utf-8") as fh:
    w = csv.writer(fh)
    w.writerow(["domain", "issue", "case", "court", "date", "binding_level", "citation", "holding", "later_history", "use_in_orders", "verified", "file"])
    for e in E:
        w.writerow([e["domain"], clean(e.get("issue_sub") or e["issue"], 200), clean(e["case"], 300), clean(e["court"], 200), clean(e["date"], 200), e["level"],
                    clean(e.get("Citation / case no.", ""), 400), clean(e.get("Holding", ""), 1500), clean(e.get("Later history", ""), 800),
                    clean(e.get("Use in orders", ""), 800), clean(e.get("Verified", ""), 200), e["file"]])

# Compendium
head = open(sys.argv[1], encoding="utf-8").read()
out = [head.replace("{N}", str(len(E))).replace("{NTG}", str(sum(e["level"] == "Binding in Telangana" for e in E))).replace("{NSC}", str(sum(e["level"].startswith("Supreme") for e in E)))]
out.append("\n## Part 3. Master index of judgments by domain\n")
out.append("Binding level: **SC** = Supreme Court, binding on all; **TG** = Telangana HC, binding in Telangana; **P** = other High Court, persuasive; **T** = tribunal (GSTAT/CESTAT); **AAR** = advance ruling; **X** = overruled, do not cite. Full entries are in Part 4 under the file named in the last column.\n")
abbr = {"Supreme Court (binding)": "SC", "Binding in Telangana": "TG", "Persuasive": "P", "Tribunal": "T", "AAR/AAAR": "AAR", "Overruled": "X (overruled)"}
for d in order:
    rows = [e for e in E if e["domain"] == d]
    if not rows: continue
    out.append(f"\n### {d} ({len(rows)})\n\n| # | Case | Court | Date | Level | Holding in brief | File |\n|----|--------------|--------|-------|-----|-----------------------------|----|")
    for i, e in enumerate(rows, 1):
        out.append(f"| {i} | {clean(e['case'], 90)} | {clean(e['court'], 45)} | {clean(e['date'], 40)} | {abbr[e['level']]} | {clean(e.get('Holding', ''), 230)} | {e['file'][:2]} |")
out.append("\n## Part 4. Full entries, file by file\n")
for f in FILES:
    t = open(os.path.join(D, f), encoding="utf-8").read()
    t = re.sub(r"^(#{1,5}) ", lambda m: "#" + m.group(1) + " ", t, flags=re.M)  # demote headings
    t = re.sub(r"^## ", f"## File {f[:2]}: ", t, count=1, flags=re.M)
    out.append(t.strip() + "\n\n---\n")
open(os.path.join(D, "GST-case-law-compendium.md"), "w", encoding="utf-8").write("\n".join(out))
print(len(E), "cases;", {k: sum(e["level"] == k for e in E) for k in abbr})
from collections import Counter; print(Counter(e["domain"] for e in E))
