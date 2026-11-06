#!/usr/bin/env python3
"""Generate index.html and README.md from data/links.json.

Usage (from the repo root):
    python3 tools/build.py

Edit data/links.json to add, move, or remove links, then rerun this script
and commit the regenerated index.html and README.md.
"""
from __future__ import annotations

import html
import json
import re
import sys
from datetime import date
from itertools import groupby
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "links.json"
SITE_TITLE = "M365, Intune & Security Link Library"
SITE_DESC = ("Curated links for Microsoft 365 and Intune administration, security operations, "
             "penetration testing, and compliance (CMMC, ISO 42001).")
OWNER = "TiQHUB Innovators"


def slug(text: str) -> str:
    """GitHub-style heading slug: lowercase, drop punctuation, spaces to hyphens."""
    return re.sub(r"[^a-z0-9 -]", "", text.lower()).replace(" ", "-")


def domain(url: str) -> str:
    p = urlparse(url)
    path = p.path.rstrip("/")
    return (p.netloc.removeprefix("www.") + (path[:40] if path else "")) or url


def load() -> list[dict]:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    seen: set[str] = set()
    for sec in data:
        for link in sec["links"]:
            url = link["url"]
            if not url.startswith(("https://", "http://")):
                sys.exit(f"Refusing non-http(s) URL: {url}")
            if url in seen:
                sys.exit(f"Duplicate URL: {url}")
            seen.add(url)
            icon = link.get("icon", "")
            if icon and not icon.startswith("data:image/"):
                sys.exit(f"Icon must be a data:image URI: {link['name']}")
    return data


def build_html(data: list[dict], today: str) -> str:
    e = lambda s: html.escape(s, quote=True)  # noqa: E731
    total = sum(len(s["links"]) for s in data)
    cats = [(c, list(g)) for c, g in groupby(data, key=lambda s: s["category"])]

    chips = "\n".join(
        f'      <a class="chip" href="#{slug(c)}" data-cat="{e(slug(c))}">{e(c)}'
        f'<span>{sum(len(s["links"]) for s in secs)}</span></a>'
        for c, secs in cats
    )

    body = []
    for c, secs in cats:
        n = sum(len(s["links"]) for s in secs)
        body.append(f'    <section class="cat" id="{slug(c)}" data-cat="{e(slug(c))}">')
        body.append(f'      <h2>{e(c)} <span class="count">{n}</span></h2>')
        for s in secs:
            body.append(f'      <div class="sub">\n        <h3 id="{slug(s["section"])}">{e(s["section"])}</h3>')
            body.append('        <ul class="grid">')
            for l in s["links"]:
                icon = (f'<img src="{e(l["icon"])}" alt="" width="16" height="16" loading="lazy">'
                        if l.get("icon") else '<span class="ph" aria-hidden="true"></span>')
                desc = f'<span class="s">{e(l["desc"])}</span>' if l.get("desc") else ""
                body.append(
                    f'          <li><a class="l" href="{e(l["url"])}" target="_blank" rel="noopener noreferrer">'
                    f'{icon}<span class="txt"><span class="t">{e(l["name"])}</span>{desc}'
                    f'<span class="d">{e(domain(l["url"]))}</span></span></a></li>'
                )
            body.append("        </ul>\n      </div>")
        body.append("    </section>")

    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <meta http-equiv="Content-Security-Policy" content="default-src 'none'; script-src 'self'; style-src 'self' https://fonts.googleapis.com; font-src https://fonts.gstatic.com; img-src 'self' data:; base-uri 'none'; form-action 'none'">
  <meta name="referrer" content="strict-origin-when-cross-origin">
  <meta name="description" content="{e(SITE_DESC)}">
  <meta name="color-scheme" content="light dark">
  <title>{e(SITE_TITLE)}</title>
  <link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&family=Archivo:wght@700;800&display=swap">
  <link rel="stylesheet" href="assets/styles.css">
  <script src="assets/app.js" defer></script>
</head>
<body>
  <a class="skip" href="#main">Skip to links</a>
  <div class="wrap">
    <header class="site">
      <h1>{e(SITE_TITLE)}</h1>
      <p>{e(SITE_DESC)}</p>
      <p class="meta"><b>{total}</b> links · updated <time datetime="{today}">{today}</time> · press <kbd>/</kbd> to search</p>
    </header>
    <div class="bar">
      <input id="q" type="search" placeholder="Search names, descriptions, domains" autocomplete="off" aria-label="Search links">
      <nav class="chips" aria-label="Categories">
      <a class="chip" href="#top" data-cat="all" aria-current="true">All<span>{total}</span></a>
{chips}
      </nav>
    </div>
    <main id="main">
{chr(10).join(body)}
      <p id="empty" hidden>No links match that search.</p>
    </main>
    <footer>Maintained by {e(OWNER)}. Links point to third-party sites; review tools before running them in production.</footer>
  </div>
</body>
</html>
"""


def build_readme(data: list[dict], today: str) -> str:
    total = sum(len(s["links"]) for s in data)
    cats = [(c, list(g)) for c, g in groupby(data, key=lambda s: s["category"])]
    out = [f"# {SITE_TITLE}", "", f"{SITE_DESC} {total} links, maintained by {OWNER}.", "",
           "Website: enable GitHub Pages for this repo, then browse the searchable version at "
           "`https://<owner>.github.io/<repo>/`.", "", f"Last updated: {today}", "",
           "## Updating the list", "",
           "1. Edit `data/links.json`.",
           "2. Run `python3 tools/build.py` (regenerates `index.html` and this README).",
           "3. Commit and push. GitHub Pages redeploys in about a minute.", "",
           "## Contents", ""]
    for c, secs in cats:
        out.append(f"- [{c}](#{slug(c)})")
        out += [f"  - [{s['section']}](#{slug(s['section'])})" for s in secs]
    for c, secs in cats:
        out += ["", f"## {c}"]
        for s in secs:
            out += ["", f"### {s['section']}", ""]
            for l in s["links"]:
                name = l["name"].replace("[", "(").replace("]", ")")
                out.append(f"- [{name}]({l['url']})" + (f" - {l['desc']}" if l.get("desc") else ""))
        out += ["", "[Back to top](#contents)"]
    return "\n".join(out) + "\n"


def main() -> None:
    data = load()
    today = date.today().isoformat()
    (ROOT / "index.html").write_text(build_html(data, today), encoding="utf-8")
    (ROOT / "README.md").write_text(build_readme(data, today), encoding="utf-8")
    print(f"Built index.html and README.md: {sum(len(s['links']) for s in data)} links")


if __name__ == "__main__":
    main()
