#!/usr/bin/env python3
"""Propose or apply GitHub About metadata for ten priority repositories.

The default is a dry run. When applying, this requires your authenticated
GitHub CLI and ownership of the target repositories. It does not edit code,
repository visibility, permissions, GitHub profile pins, or account settings.

Examples:
  python3 tools/finish_github_settings.py
  python3 tools/finish_github_settings.py --only jamiechristian22.github.io
  python3 tools/finish_github_settings.py --apply --only jamiechristian22.github.io
  python3 tools/finish_github_settings.py --apply
"""
import argparse
import json
import shlex
import shutil
import subprocess
import sys

OWNER = "JamieChristian22"
SITE = "https://jamiechristian22.github.io/"
REPOS = [
    ("jamiechristian22.github.io",
     "Portfolio website featuring reviewable business, product, data, cloud, and cybersecurity case studies.",
     ["portfolio", "github-pages", "project-portfolio", "data-analytics", "cloud-engineering"]),
    ("JamieChristian22",
     "Portfolio of independent business analysis, product, data analytics, cloud engineering, and cybersecurity work.",
     ["portfolio", "business-analysis", "data-analytics", "product-management", "cloud-engineering", "cybersecurity"]),
    ("product-manager-portfolio",
     "Six simulated product management cases with PRDs, roadmaps, dashboards, experiments, and launch decisions.",
     ["product-management", "case-study", "product-analytics", "ab-testing", "product-roadmap"]),
    ("product-owner-portfolio",
     "Five simulated Product Owner cases with PRDs, backlogs, sprint planning, dashboards, and KPI governance.",
     []),
    ("marketing-analytics-portfolio",
     "Six marketing analytics cases covering conversion, ROI, journeys, A/B testing, SQL, and Python.",
     ["marketing-analytics", "marketing-roi", "ab-testing", "sql", "python", "conversion-rate-optimization"]),
    ("financial-analyst-portfolio",
     "FP&A and financial analysis projects: budgeting, forecasting, variance analysis, dashboards, SQL, and Python.",
     []),
    ("multi-cloud-devops-engineering-projects",
     "AWS, Azure, and GCP DevOps portfolio labs with Terraform, CI/CD, Kubernetes, GitOps, and validation.",
     []),
    ("multi-cloud-architect-portfolio",
     "Simulated AWS, Azure, and GCP architecture case: Terraform examples, data integration, security, and operations.",
     ["architecture-review"]),
    ("data-science-portfolio",
     "Five machine learning case studies: churn, credit risk, demand forecasting, fraud, and marketing optimization.",
     ["data-science", "python", "machine-learning", "scikit-learn", "model-evaluation", "forecasting"]),
    ("cloud-support-operations-portfolio",
     "Five simulated cloud support labs covering incidents, networking, IAM, monitoring, runbooks, and verification.",
     ["cloud-support", "aws", "azure", "google-cloud", "incident-response", "network-troubleshooting"]),
]


def run(command, read_output=False):
    process = subprocess.run(command, text=True, capture_output=read_output, check=False)
    if process.returncode:
        explanation = (process.stderr or process.stdout or "Unknown GitHub CLI error").strip()
        raise RuntimeError(f"{shlex.join(command[:3])}: {explanation}")
    return process.stdout if read_output else ""


def repo_metadata(name):
    return json.loads(run(["gh", "api", f"repos/{OWNER}/{name}"], read_output=True))


def proposed_changes(name, description, topics, current=None):
    """Return edit command, skipped topics, added topics; preserve existing topics."""
    if current is None:
        command = ["gh", "repo", "edit", f"{OWNER}/{name}", "--description", description, "--homepage", SITE]
        for topic in topics:
            command.extend(["--add-topic", topic])
        return command, [], topics

    existing = set(current.get("topics") or [])
    available = max(0, 20 - len(existing))
    new_topics = [topic for topic in topics if topic not in existing]
    additions = new_topics[:available]
    skipped = new_topics[available:]
    command = ["gh", "repo", "edit", f"{OWNER}/{name}"]
    if (current.get("description") or "") != description:
        command.extend(["--description", description])
    if (current.get("homepage") or "") != SITE:
        command.extend(["--homepage", SITE])
    for topic in additions:
        command.extend(["--add-topic", topic])
    return command, skipped, additions


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--apply", action="store_true", help="Actually update GitHub (default previews only)")
    parser.add_argument("--only", choices=[name for name, _, _ in REPOS],
                        help="Update a single repository rather than all ten")
    args = parser.parse_args()

    selected = [(name, desc, tags) for name, desc, tags in REPOS if not args.only or args.only == name]
    if args.apply:
        if not shutil.which("gh"):
            parser.error("GitHub CLI is missing; install from https://cli.github.com/")
        run(["gh", "auth", "status"])
        login = run(["gh", "api", "user", "--jq", ".login"], read_output=True).strip()
        if login.lower() != OWNER.lower():
            parser.error(f"GitHub CLI is logged in as {login!r}, not {OWNER!r}; switch accounts first.")

    modified = 0
    errors = []
    topics_skipped = 0
    for name, description, topics in selected:
        try:
            current = repo_metadata(name) if args.apply else None
            command, skipped, added = proposed_changes(name, description, topics, current)
            print(f"\n{OWNER}/{name}:")
            if len(command) == 4:
                print("  Already matches; no changes required.")
            else:
                print(" ", shlex.join(command))
                if args.apply:
                    run(command)
                    modified += 1
                    verified = repo_metadata(name)
                    if verified.get("description") != description or (verified.get("homepage") or "") != SITE:
                        raise RuntimeError("GitHub About description/homepage verification failed")
                    if any(tag not in (verified.get("topics") or []) for tag in added):
                        raise RuntimeError("GitHub topic verification failed")
                    print("  VERIFIED: About description, homepage and selected topics")
            if skipped:
                print("  Reached GitHub's 20-topic limit; skipped:", ", ".join(skipped))
                topics_skipped += len(skipped)
        except (RuntimeError, json.JSONDecodeError) as exc:
            print("  ERROR:", exc, file=sys.stderr)
            errors.append(name)
    if args.apply:
        print(f"\nRepos changed: {modified}; topics skipped: {topics_skipped}; errors: {len(errors)}")
        print("Profile pins are a separate GitHub UI action.")
    else:
        print("\nDRY RUN: no GitHub settings were changed.")
        print("First repo: python3 tools/finish_github_settings.py --apply --only jamiechristian22.github.io")
        print("All repos:  python3 tools/finish_github_settings.py --apply")
    if errors:
        print("Repositories needing attention:", ", ".join(errors), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
