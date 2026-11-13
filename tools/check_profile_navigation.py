#!/usr/bin/env python3
"""Zero-network checks for the public profile's navigation and local docs.

Verifies local Markdown link targets, six featured projects, and the repository
index. This does NOT prove that external URLs, deployments, or sponsor payments
are working; those require independent review.
"""
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

LINK = re.compile(r'!?\[[^\]]*\]\((<[^>]+>|[^)\n]+)\)')
REMOTE = re.compile(r'^[A-Za-z][A-Za-z0-9+.-]*:|^//')
OWNER = 'JamieChristian22'


def local_targets(markdown: str):
    """Yield local targets, excluding external URLs and same-page anchors."""
    for match in LINK.finditer(markdown):
        href = match.group(1).strip()
        if href.startswith('<') and href.endswith('>'):
            href = href[1:-1]
        else:
            href = href.split(' "', 1)[0].split(" '", 1)[0]
        href = href.strip()
        if not href or href.startswith('#') or REMOTE.match(href):
            continue
        path = unquote(urlsplit(href).path)
        if path:
            yield path


def check_local_links(root: Path, files):
    problems = []
    base = root.resolve()
    for file in files:
        source = root / file
        if not source.is_file():
            problems.append(f'Missing document: {file}')
            continue
        for target in sorted(set(local_targets(source.read_text(encoding='utf-8')))):
            resolved = ((base if target.startswith('/') else source.parent) / target.lstrip('/')).resolve()
            if not resolved.is_relative_to(base):
                problems.append(f'Outside repository: {file} -> {target}')
            elif not resolved.exists():
                problems.append(f'Broken local link: {file} -> {target}')
    return problems


def check_profile_structure(text: str):
    problems = []
    sections = {
        'recruiter navigation': '## 🎯 For recruiters & hiring teams',
        'featured portfolio': '## ⭐ Featured work',
        'public directory': '## 📚 Complete public repository directory',
    }
    for label, heading in sections.items():
        if heading not in text:
            problems.append(f'Missing {label}: {heading}')
    for entry in ('RECRUITER_START_HERE.md', 'DEVELOPER_START_HERE.md',
                  'PAID_SERVICES.md', 'FUNDED_WORK.md',
                  'github.com/sponsors/JamieChristian22'):
        if entry not in text:
            problems.append(f'Missing important navigation: {entry}')

    start = text.find('## ⭐ Featured work')
    finish = text.find('### A few visual work samples', start)
    if start >= 0 and finish > start:
        featured = text[start:finish]
        hits = re.findall(r'(?m)^\| \[[^\]]+\]\(https://github\.com/JamieChristian22/[^)]+\) \|', featured)
        if len(hits) != 6:
            problems.append(f'Expected six distinct featured rows; found {len(hits)}')
    else:
        problems.append('Cannot isolate the six featured repository rows')

    index_start = text.find('## 📚 Complete public repository directory')
    index_end = text.find('## 🎓 Background and approach', index_start)
    if index_start >= 0 and index_end > index_start:
        directory = text[index_start:index_end]
        names = re.findall(r'(?m)^- \[[^\]]+\]\(https://github\.com/JamieChristian22/([^/#?)]+)\)', directory)
        if len(set(names)) < 35:
            problems.append(f'Expected at least 35 unique public directory links; found {len(set(names))}')
    else:
        problems.append('Cannot identify the public-repository directory')
    return problems


def main():
    root = Path(__file__).resolve().parents[1]
    docs = sorted(p.relative_to(root) for p in root.glob('*.md'))
    problems = check_local_links(root, docs)
    readme = root / 'README.md'
    if readme.exists():
        problems.extend(check_profile_structure(readme.read_text(encoding='utf-8')))
    print(f'Checked {len(docs)} root Markdown documents for local links, '
          'profile routes and featured repository coverage.')
    print('External GitHub repos, web pages, payout status and CI outcomes are NOT checked.')
    for problem in problems:
        print('ERROR:', problem, file=sys.stderr)
    return 1 if problems else 0


if __name__ == '__main__':
    sys.exit(main())
