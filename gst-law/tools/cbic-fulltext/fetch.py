#!/usr/bin/env python3
"""Download every GST notification, circular, instruction and order from the
CBIC Tax Information Portal and store its full text in the repo.

Reads the four index CSVs in gst-law/data/, fetches each PDF from
taxinformation.cbic.gov.in, extracts the text (pdftotext; OCR with tesseract
when the PDF is a scan) and writes one Markdown file per item under
gst-law/fulltext/. Safe to stop and re-run: items already done are skipped.

Needs network access to taxinformation.cbic.gov.in and crt.sectigo.com
(see START-HERE.md, "Websites"). Certificate checking stays ON: the CBIC
server omits its Sectigo intermediate, so we fetch it and add it to a copy of
the system/proxy CA bundle.

Usage (from the repo root):
    python3 -I gst-law/tools/cbic-fulltext/fetch.py              # everything
    python3 -I gst-law/tools/cbic-fulltext/fetch.py --only circulars --limit 5   # quick test
    python3 -I gst-law/tools/cbic-fulltext/fetch.py --local DIR  # convert PDFs already on disk (no network)
"""
import argparse, base64, csv, json, os, re, shutil, ssl, subprocess, sys, tempfile, time

HERE = os.path.dirname(os.path.abspath(__file__))
GST = os.path.abspath(os.path.join(HERE, "..", ".."))           # gst-law/
DATA = os.path.join(GST, "data")
OUT = os.path.join(GST, "fulltext")
CACHE = os.environ.get("CBIC_PDF_CACHE", os.path.join(tempfile.gettempdir(), "cbic-pdf-cache"))
BASE = "https://taxinformation.cbic.gov.in"
SECTIGO = "http://crt.sectigo.com/SectigoPublicServerAuthenticationCAOVR36.crt"

KINDS = {  # kind -> (csv, folder, number column)
    "notifications": ("notifications.csv", "notifications", "short_no"),
    "circulars": ("circulars.csv", "circulars", "number"),
    "instructions": ("instructions.csv", "instructions", "number"),
    "orders": ("orders.csv", "orders", "number"),
}

def slug(s, n=80):
    s = re.sub(r"[^A-Za-z0-9]+", "-", s or "").strip("-").lower()
    return s[:n].strip("-") or "untitled"

# ---------- network ----------
def ca_bundle():
    base = os.environ.get("REQUESTS_CA_BUNDLE") or os.environ.get("SSL_CERT_FILE")
    for c in (base, "/root/.ccr/ca-bundle.crt", "/etc/ssl/certs/ca-certificates.crt"):
        if c and os.path.exists(c):
            base = c; break
    out = os.path.join(CACHE, "bundle-cbic.pem")
    if os.path.exists(out):
        return out
    import requests
    der = requests.get(SECTIGO, timeout=60).content
    pem = ssl.DER_cert_to_PEM_cert(der) if not der.startswith(b"-----") else der.decode()
    os.makedirs(CACHE, exist_ok=True)
    with open(out, "w") as fh:
        fh.write(open(base).read() + "\n" + pem)
    return out

class Portal:
    def __init__(self):
        import requests
        self.s = requests.Session()
        self.s.verify = ca_bundle()
        self.s.headers["User-Agent"] = "Mozilla/5.0 (X11; Linux x86_64) gst-knowledge-base/1.0"
        self.token = None

    def auth(self):
        r = self._retry("POST", BASE + "/api/authenticate-token", json={})
        tok = None
        try:
            j = r.json()
            for k in ("id_token", "token", "accessToken", "access_token", "data"):
                if isinstance(j, dict) and isinstance(j.get(k), str):
                    tok = j[k]; break
            if tok is None and isinstance(j, str):
                tok = j
        except ValueError:
            tok = r.text.strip().strip('"')
        tok = tok or r.headers.get("Authorization", "").replace("Bearer ", "")
        if not tok:
            raise SystemExit("Could not read a token from /api/authenticate-token: " + r.text[:200])
        self.token = tok
        self.s.headers["Authorization"] = "Bearer " + tok
        self.s.headers["Authorization1"] = "homeToken " + tok

    def _retry(self, method, url, tries=6, **kw):
        last = None
        for i in range(tries):
            try:
                r = self.s.request(method, url, timeout=120, **kw)
                if r.status_code == 401 and self.token and "authenticate" not in url:
                    self.auth(); continue
                if r.status_code < 500:
                    return r
                last = f"HTTP {r.status_code}"
            except Exception as e:  # connection resets are common on this site
                last = repr(e)
            time.sleep(min(60, 3 * 2 ** i))
        raise RuntimeError(f"{method} {url} failed: {last}")

    def pdf(self, path, page_url):
        """Return PDF bytes. Tries /content/pdf/<path> (base64 JSON), then the
        service download endpoint using the id at the end of the page URL."""
        cands = [BASE + "/content/pdf/" + path.lstrip("/")]
        m = re.search(r"explore-(notification|circulars|instructions|orders)/(\d+)", page_url or "")
        if m:
            svc = {"notification": "cbic-notification-msts", "circulars": "cbic-circular-msts",
                   "instructions": "cbic-instruction-msts", "orders": "cbic-order-msts"}[m.group(1)]
            cands.append(f"{BASE}/api/{svc}/download/{m.group(2)}/ENG")
        for url in cands:
            r = self._retry("GET", url)
            if r.status_code != 200:
                continue
            b = decode_pdf(r)
            if b:
                return b
        return None

def decode_pdf(r):
    if r.content[:4] == b"%PDF":
        return r.content
    try:
        j = r.json()
    except ValueError:
        return None
    best = None
    def walk(x):
        nonlocal best
        if isinstance(x, dict):
            for v in x.values(): walk(v)
        elif isinstance(x, list):
            for v in x: walk(v)
        elif isinstance(x, str) and len(x) > 200:
            try:
                b = base64.b64decode(x.split(",", 1)[-1], validate=False)
                if b[:4] == b"%PDF" and (best is None or len(b) > len(best)):
                    best = b
            except Exception:
                pass
    walk(j)
    return best

# ---------- text ----------
def pdf_text(pdf_path):
    """Text of a PDF; OCR (English + Hindi if available) when it is a scan."""
    txt = subprocess.run(["pdftotext", "-layout", pdf_path, "-"], capture_output=True, text=True).stdout
    method = "pdftotext"
    if len(re.sub(r"\s+", "", txt)) < 200 and shutil.which("tesseract") and shutil.which("pdftoppm"):
        langs = subprocess.run(["tesseract", "--list-langs"], capture_output=True, text=True).stdout.split()
        lang = "eng+hin" if "hin" in langs else "eng"
        with tempfile.TemporaryDirectory() as d:
            subprocess.run(["pdftoppm", "-r", "200", "-png", pdf_path, os.path.join(d, "p")], check=False)
            pages = []
            for f in sorted(os.listdir(d)):
                pages.append(subprocess.run(["tesseract", os.path.join(d, f), "-", "-l", lang],
                                            capture_output=True, text=True).stdout)
        txt = "\n\f".join(pages)
        method = f"OCR (tesseract {lang}) - check figures against the PDF before quoting"
    txt = txt.replace("\f", "\n\n---- page break ----\n\n")
    txt = re.sub(r"[ \t]+\n", "\n", txt)
    txt = re.sub(r"\n{4,}", "\n\n\n", txt)
    return txt.strip(), method

def out_path(kind, row):
    folder = KINDS[kind][1]
    num = row.get(KINDS[kind][2]) or ""
    year = (row.get("date") or "")[:4] or "undated"
    cat = slug(row.get("category") or kind, 40)
    name = slug(num, 60) if num else slug(row.get("subject"), 60)
    return os.path.join(OUT, folder, cat, year, name + ".md")

def write_md(kind, row, text, method):
    p = out_path(kind, row)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    num = row.get(KINDS[kind][2]) or "(no number)"
    head = [f"# {num} - {row.get('date','')}", "",
            f"**Subject:** {row.get('subject','').strip()}", "",
            f"- Type: {kind[:-1]} ({row.get('category') or 'GST'})",
            f"- Source: [CBIC page]({row.get('cbic_page','')}) - PDF path `{row.get('cbic_pdf_path','')}`"]
    if row.get("amended"): head.append(f"- Amended by (per CBIC): {row['amended']}")
    if row.get("omitted"): head.append(f"- Omitted/rescinded (per CBIC): {row['omitted']}")
    head += [f"- Text extracted: {method}; fetched {time.strftime('%Y-%m-%d')}",
             "- Note: this is the text as originally issued. Check later amendments before relying on it.",
             "", "---", "", "```text", text, "```", ""]
    with open(p, "w", encoding="utf-8") as fh:
        fh.write("\n".join(head))
    return p

def rows(kind):
    with open(os.path.join(DATA, KINDS[kind][0]), encoding="utf-8") as fh:
        return [r for r in csv.DictReader(fh) if r.get("cbic_pdf_path")]

# ---------- index ----------
def build_index(failures):
    lines = ["# Full text of GST notifications, circulars, instructions and orders", "",
             "One Markdown file per item, text extracted from the CBIC PDF. Folders: "
             "`<type>/<category>/<year>/<number>.md`. Search with grep (for example "
             "`grep -ril \"section 54\" gst-law/fulltext/circulars`). Index CSVs with subjects are in `gst-law/data/`.",
             "", "Built by `gst-law/tools/cbic-fulltext/fetch.py`. Text is as originally issued; "
             "amendments are separate notifications (see the `amended` column in the CSVs).", "",
             "| Type | In index | Full text here |", "|---|---|---|"]
    for kind in KINDS:
        total = len(rows(kind))
        have = sum(len(fs) for _, _, fs in os.walk(os.path.join(OUT, KINDS[kind][1])))
        lines.append(f"| {kind} | {total} | {have} |")
    if failures:
        lines += ["", "## Not fetched in the last run", ""] + [f"- {k}: {n} ({why})" for k, n, why in failures]
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, "00-read-me-first.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")

# ---------- main ----------
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", choices=list(KINDS))
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--delay", type=float, default=1.0, help="seconds between downloads")
    ap.add_argument("--local", help="folder of PDFs named by CBIC pdf basename; convert without network")
    ap.add_argument("--force", action="store_true", help="redo items already converted")
    a = ap.parse_args()
    os.makedirs(CACHE, exist_ok=True)
    portal = None
    failures, done = [], 0
    for kind in ([a.only] if a.only else list(KINDS)):
        for i, row in enumerate(rows(kind)):
            if a.limit and i >= a.limit:
                break
            num = row.get(KINDS[kind][2]) or row.get("subject", "")[:50]
            if os.path.exists(out_path(kind, row)) and not a.force:
                continue
            base = os.path.basename(row["cbic_pdf_path"])
            pdf = os.path.join(a.local or CACHE, base if a.local else slug(row["cbic_pdf_path"], 150) + ".pdf")
            if not os.path.exists(pdf):
                if a.local:
                    continue
                if portal is None:
                    portal = Portal(); portal.auth()
                try:
                    b = portal.pdf(row["cbic_pdf_path"], row.get("cbic_page"))
                except RuntimeError as e:
                    b = None; failures.append((kind, num, str(e)[:120]))
                if not b:
                    if not failures or failures[-1][1] != num:
                        failures.append((kind, num, "no PDF returned"))
                    continue
                open(pdf, "wb").write(b)
                time.sleep(a.delay)
            text, method = pdf_text(pdf)
            if not text:
                failures.append((kind, num, "PDF has no extractable text")); continue
            write_md(kind, row, text, method)
            done += 1
            if done % 25 == 0:
                print(f"{done} converted (latest: {kind} {num})", flush=True)
    build_index(failures)
    print(f"Done: {done} converted, {len(failures)} not fetched. See gst-law/fulltext/00-read-me-first.md")

if __name__ == "__main__":
    main()
