"""Run on your own machine: confirm each GitHub org on GitHub itself and list its public repos.

Usage:
  export GITHUB_TOKEN=...            # a classic or fine-grained token, public read is enough
  python3 github_side_check.py sp500-github-orgs.csv out_orgs.csv out_repos.csv

Input CSV columns used: company, ticker, handle.
out_orgs.csv:  one row per org, with GitHub's own view of it (verified domain, website, repo count).
out_repos.csv: one row per public, non-fork repo (archived flag, last push, language, stars).
Stays under GitHub's rate limits: one request at a time, ~1 per second.
"""
import csv
import json
import os
import sys
import time
import urllib.error
import urllib.request

API = "https://api.github.com"
TOKEN = os.environ.get("GITHUB_TOKEN", "")


def get(url):
    req = urllib.request.Request(url, headers={
        "Accept": "application/vnd.github+json",
        "User-Agent": "sp500-github-orgs-research",
        **({"Authorization": f"Bearer {TOKEN}"} if TOKEN else {}),
    })
    for attempt in range(5):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                time.sleep(1.0)
                return json.load(r), r.headers.get("Link", "")
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None, ""
            if e.code in (403, 429):
                reset = int(e.headers.get("X-RateLimit-Reset", time.time() + 60))
                time.sleep(max(5, reset - time.time() + 1))
                continue
            raise
    return None, ""


def main(src, orgs_out, repos_out):
    rows = list(csv.DictReader(open(src)))
    with open(orgs_out, "w", newline="") as fo, open(repos_out, "w", newline="") as fr:
        wo = csv.writer(fo)
        wr = csv.writer(fr)
        wo.writerow(["company", "ticker", "handle", "exists", "type", "is_verified", "blog", "public_repos"])
        wr.writerow(["company", "ticker", "handle", "repo", "archived", "fork", "pushed_at", "language", "stars"])
        for row in rows:
            h = row["handle"]
            org, _ = get(f"{API}/orgs/{h}")
            if org is None:
                user, _ = get(f"{API}/users/{h}")
                wo.writerow([row["company"], row["ticker"], h, user is not None,
                             (user or {}).get("type", ""), "", (user or {}).get("blog", ""),
                             (user or {}).get("public_repos", "")])
                continue
            wo.writerow([row["company"], row["ticker"], h, True, "Organization",
                         org.get("is_verified"), org.get("blog"), org.get("public_repos")])
            page = 1
            while True:
                repos, link = get(f"{API}/orgs/{h}/repos?type=public&per_page=100&page={page}")
                if not repos:
                    break
                for r in repos:
                    if r.get("fork"):
                        continue
                    wr.writerow([row["company"], row["ticker"], h, r["full_name"], r["archived"],
                                 r["fork"], r["pushed_at"], r.get("language"), r["stargazers_count"]])
                if 'rel="next"' not in link:
                    break
                page += 1


if __name__ == "__main__":
    main(*sys.argv[1:4])
