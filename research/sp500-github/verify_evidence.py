"""Re-fetch each evidence page the agents cited and check it really names github.com/<handle>.

Usage: python3 verify_evidence.py results.json verified.json
results.json: list of company dicts as returned by the workflow.
Wikidata evidence is checked through the Wikidata API (claim P2037).
"""
import concurrent.futures as cf
import json
import re
import subprocess
import sys
import urllib.parse

UA = "Mozilla/5.0 (compatible; research-verifier)"


def fetch(url):
    try:
        out = subprocess.run(
            ["curl", "-sL", "-m", "25", "--compressed", "-A", UA, url],
            capture_output=True, timeout=40,
        )
        return out.stdout.decode("utf-8", "ignore")
    except Exception:
        return ""


def wikidata_handles(url):
    m = re.search(r"(Q\d+)", url)
    if not m:
        return set()
    qid = m.group(1)
    body = fetch(f"https://www.wikidata.org/wiki/Special:EntityData/{qid}.json")
    try:
        ent = json.loads(body)["entities"][qid]
        return {c["mainsnak"]["datavalue"]["value"].lower()
                for c in ent["claims"].get("P2037", []) if "datavalue" in c["mainsnak"]}
    except Exception:
        return set()


def check(org):
    handle = org["handle"].strip().strip("/").lower()
    url = org["evidence_url"].strip()
    if not url.startswith("http"):
        return "no_url"
    host = urllib.parse.urlparse(url).netloc.lower()
    if host.endswith("github.com") or host.endswith("githubusercontent.com"):
        return "evidence_is_github"
    if "wikidata.org" in host:
        return "verified" if handle in wikidata_handles(url) else "not_on_page"
    body = fetch(url).lower()
    if not body:
        return "fetch_failed"
    pat = r"github\.com/" + re.escape(handle) + r"(?![a-z0-9-])"
    if re.search(pat, body):
        return "verified"
    if re.search(r"github\.com%2f" + re.escape(handle), body):
        return "verified"
    return "not_on_page"


def main(src, dst):
    cos = json.load(open(src))
    jobs = [(i, j, o) for i, c in enumerate(cos) for j, o in enumerate(c.get("github_orgs", []))]
    with cf.ThreadPoolExecutor(8) as ex:
        for (i, j, o), res in zip(jobs, ex.map(lambda t: check(t[2]), jobs)):
            cos[i]["github_orgs"][j]["evidence_check"] = res
    json.dump(cos, open(dst, "w"), indent=1)
    from collections import Counter
    print(Counter(o["evidence_check"] for c in cos for o in c.get("github_orgs", [])))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
