import re, sys, os, csv, json
D = "/mnt/project-files/gst-law/case-law"
FILES = sorted(f for f in os.listdir(D) if re.match(r"0[1-9]-.*\.md$", f))
FIELDS = ["Citation / case no.", "Holding", "Binding", "Later history", "Use in orders", "Source", "Verified"]

def entries():
    for f in FILES:
        lines = open(os.path.join(D, f), encoding="utf-8").read().splitlines()
        issue = ""; cur = None
        for ln in lines:
            if ln.startswith("## "):
                issue = ln[3:].strip()
            if ln.startswith("### "):
                if cur: yield cur
                cur = None
                h = ln[4:].strip()
                parts = [p.strip() for p in re.split(r"\s+[-–—]\s+", h)]
                if len(parts) >= 3:
                    cur = {"file": f, "issue": issue, "case": parts[0], "court": parts[1], "date": " - ".join(parts[2:])}
                else:
                    issue = h  # sub-issue heading
                    continue
            elif cur is not None:
                m = re.match(r"[-*]\s+\**([A-Za-z /.()]+?)\**:\**\s*(.*)", ln)
                sub = re.match(r"\s+[-*]\s+(.*)", ln)
                if sub and not m and cur.get("_last"):
                    k0 = cur["_last"]; cur[k0] = (cur.get(k0, "") + " " + sub.group(1).strip()).strip()
                    continue
                if m:
                    k = m.group(1).strip()
                    for F in FIELDS:
                        if k.lower().startswith(F.lower()[:8]):
                            cur[F] = m.group(2).strip(); cur["_last"] = F; break
                    if "issue_sub" not in cur: cur["issue_sub"] = issue
        if cur: yield cur

if __name__ == "__main__":
    E = list(entries())
    json.dump(E, open(sys.argv[1], "w"), indent=1)
    print(len(E), "entries")
    from collections import Counter
    print(Counter(e["file"] for e in E))
    print("missing holding:", sum(1 for e in E if not e.get("Holding")))
