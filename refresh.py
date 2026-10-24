"""Re-download every open data table from its live URL and report what changed.

Run: py -3.11 refresh.py
Writes files in place. Does not commit.
"""
import hashlib
import os
import sys
import urllib.request

UA = "Mozilla/5.0 Sharknative-OpenData/1.0"
ROOT = os.path.dirname(os.path.abspath(__file__))

# (folder, local filename, live URL)
DATASETS = [
    ("countertopcheck-fit", "fit.csv", "https://countertopcheck.com/fit.csv"),
    ("countertopcheck-fit", "fit.json", "https://countertopcheck.com/fit.json"),
    ("anglerleague-castable-sonar-index", "castable-sonar-index.csv", "https://anglerleague.com/castable-sonar-index.csv"),
    ("anglerleague-castable-sonar-index", "castable-sonar-index.json", "https://anglerleague.com/castable-sonar-index.json"),
    ("cremacheck-office-machines", "office-machines.csv", "https://cremacheck.com/office-machines.csv"),
    ("cremacheck-office-machines", "office-machines.json", "https://cremacheck.com/office-machines.json"),
    ("firstprintcheck-first-printers", "first-printers.csv", "https://firstprintcheck.com/first-printers.csv"),
    ("firstprintcheck-first-printers", "first-printers.json", "https://firstprintcheck.com/first-printers.json"),
    ("wellnessrundown-small-space-index", "small-space-index.csv", "https://wellnessrundown.com/small-space-index/small-space-index.csv"),
    ("wellnessrundown-small-space-index", "small-space-index.json", "https://wellnessrundown.com/small-space-index/small-space-index.json"),
]


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.status, r.read()


def digest(b):
    return hashlib.sha256(b).hexdigest()[:12]


def main():
    changed, same, failed = [], [], []
    for folder, name, url in DATASETS:
        path = os.path.join(ROOT, folder, name)
        try:
            status, body = fetch(url)
        except Exception as e:  # network or HTTP error
            failed.append((path, str(e)))
            continue
        looks_html = body.lstrip()[:1] == b"<"
        if status != 200 or len(body) < 50 or looks_html:
            why = f"HTTP {status}, {len(body)} bytes"
            if looks_html:
                why += ", looks like HTML"
            failed.append((path, why))
            continue
        old = open(path, "rb").read() if os.path.exists(path) else b""
        if old == body:
            same.append(path)
            continue
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "wb") as f:
            f.write(body)
        changed.append((path, len(old), len(body), digest(old) if old else "-", digest(body)))

    def rel(p):
        return os.path.relpath(p, ROOT).replace(os.sep, "/")

    print(f"refresh: {len(changed)} changed, {len(same)} unchanged, {len(failed)} failed")
    for p, a, b, da, db in changed:
        print(f"  changed  {rel(p)}  {a} -> {b} bytes  {da} -> {db}")
    for p, why in failed:
        print(f"  FAILED   {rel(p)}  {why}  (kept previous copy)")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
