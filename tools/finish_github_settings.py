"""Opt-in GitHub repository About metadata improvements for the ten priority repos.

Dry run by default. Requires authenticated GitHub CLI for --apply.
Never changes repository visibility, code, or access rights.
"""
import argparse
import shlex
import shutil
import subprocess

OWNER = "JamieChristian22"
SITE = "https://jamiechristian22.github.io/"
# Topics are added without deleting existing ones. GitHub limits each repo to 20.
REPOS = [
    ("jamiechristian22.github.io",
     "Portfolio website with project previews and reviewable business, product, data, cloud, and security case studies.",
     ["portfolio","github-pages","github-portfolio","data-analytics","cloud-engineering"]),
    ("JamieChristian22",
     "Business, product, data, cloud, and cybersecurity portfolio with independent case studies and technical evidence.",
     ["portfolio","business-analysis","data-analytics","product-management","cloud-engineering","cybersecurity"]),
    ("product-manager-portfolio",
     "Six simulated product management case studies with research, PRDs, roadmaps, experiments, dashboards, and launch decisions.",
     ["product-management","case-study","product-analytics","ab-testing","roadmap"]),
    ("product-owner-portfolio",
     "Five simulated Product Owner case studies with PRDs, backlogs, sprint plans, dashboards, and KPI governance.",
     []),
    ("marketing-analytics-portfolio",
     "Six marketing analytics case studies on conversion, campaign ROI, customer journeys, A/B testing, SQL, and Python.",
     ["marketing-analytics","marketing-roi","ab-testing","sql","python","conversion-rate-optimization"]),
    ("financial-analyst-portfolio",
     "Financial analysis and FP&A projects with forecasts, budget models, variance analysis, dashboards, SQL, and Python.",
     []),
    ("multi-cloud-devops-engineering-projects",
     "Enterprise-inspired AWS, Azure, and GCP DevOps labs with Terraform, CI/CD, Kubernetes, GitOps, and validation.",
     []),
    ("multi-cloud-architect-portfolio",
     "Simulated AWS, Azure, and GCP architecture case study with Terraform examples, data integration, security, and operations.",
     ["architecture-review"]),
    ("data-science-portfolio",
     "Five reproducible ML case studies: churn, credit risk, retail forecasting, fraud detection, and marketing optimization.",
     ["data-science","python","machine-learning","scikit-learn","model-evaluation","forecasting"]),
    ("cloud-support-operations-portfolio",
     "Five simulated cloud support labs with incidents, networking, IAM, monitoring, runbooks, and offline verification.",
     ["cloud-support","aws","azure","google-cloud","incident-response","network-troubleshooting"]),
]

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--apply", action="store_true", help="Apply GitHub About settings (default is dry-run)")
    args = ap.parse_args()
    if args.apply:
        if not shutil.which("gh"):
            ap.error("GitHub CLI not found; install https://cli.github.com/")
        subprocess.run(["gh","auth","status"], check=True)
    for name, desc, topics in REPOS:
        cmd = ["gh","repo","edit",OWNER+"/"+name,"--description",desc,"--homepage",SITE]
        for topic in topics:
            cmd += ["--add-topic",topic]
        if args.apply:
            print("Applying:",OWNER+"/"+name,flush=True)
            subprocess.run(cmd,check=True)
        else:
            print(shlex.join(cmd))
    if args.apply:
        print("Metadata requests completed; inspect each About panel to confirm.")
    else:
        print("\nDry run: no changes made. Review the commands, then run with --apply under your account.")

if __name__ == "__main__":
    main()
