"""Rewrite the "now building" line in README.md with my most recently pushed public repo.

Run by .github/workflows/profile.yml. Repos in EXCLUDE never show: this profile repo, the
portfolio (a bot commits LeetCode stats to it every 6 hours) and tools I don't want featured.
"""

import json
import os
import re
import urllib.request
from datetime import datetime
from pathlib import Path

USER = "AnuragBhandary"
EXCLUDE = {"AnuragBhandary", "anuragbhandary.github.io", "job-radar", "Leetcodes"}
README = Path(__file__).resolve().parent.parent / "README.md"
START, END = "<!--NOW:START-->", "<!--NOW:END-->"


def latest_repo():
    req = urllib.request.Request(f"https://api.github.com/users/{USER}/repos?sort=pushed&per_page=30",
                                 headers={"Accept": "application/vnd.github+json", "User-Agent": "profile-readme"})
    if os.environ.get("GITHUB_TOKEN"):
        req.add_header("Authorization", f"Bearer {os.environ['GITHUB_TOKEN']}")
    with urllib.request.urlopen(req, timeout=30) as r:
        repos = json.load(r)
    return next(r for r in repos if not r["fork"] and not r["private"] and r["name"] not in EXCLUDE)


def short(text, limit=110):
    text = (text or "").strip()
    if len(text) <= limit:
        return text
    return text[:limit].rsplit(" ", 1)[0].rstrip(",;:") + "…"


def main():
    repo = latest_repo()
    when = datetime.fromisoformat(repo["pushed_at"].replace("Z", "+00:00")).strftime("%-d %b %Y")
    line = f'[{repo["name"]}]({repo["html_url"]}): {short(repo["description"])} <sub>({when})</sub>'
    text = README.read_text()
    new = re.sub(f"{START}.*?{END}", lambda _: f"{START}{line}{END}", text, flags=re.S)
    README.write_text(new)
    print(line)


if __name__ == "__main__":
    main()
