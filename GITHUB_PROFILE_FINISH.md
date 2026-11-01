# Complete your GitHub profile settings

Your code, READMEs, portfolio visuals and CI have been improved. GitHub **repository descriptions, homepages, topics and pinned items** require account/repository settings write access, which is not exposed by the connected GitHub file-edit interface.

## About metadata: prepared, not applied

[Review the opt-in metadata script](tools/finish_github_settings.py). It proposes accurate descriptions, the portfolio URL and discoverability topics for the ten selected repositories. Topics are added without intentionally deleting existing topics; GitHub limits a repository to 20 topics, so review repositories already at the limit.

Requires your authenticated GitHub CLI (https://cli.github.com/). From an authenticated local clone of this profile repository, use a dry run first:

    python tools/finish_github_settings.py

To apply the changes using your GitHub credentials, after reviewing them:

    gh auth status
    python tools/finish_github_settings.py --apply

This does **not** change repository visibility, source code, access permissions, collaborators, branch rules, or account privacy settings. No credentials are stored in the script. It is not automatically executed by GitHub Actions.

## Pin six flagship repositories

Visit [your GitHub profile](https://github.com/JamieChristian22), click **Customize your pins**, choose six, and save. Suggested set:

1. [Business Analyst Portfolio](https://github.com/JamieChristian22/Business-Analyst-Portfolio2)
2. [Data Analyst Portfolio](https://github.com/JamieChristian22/data-analyst-portfolio)
3. [Project Coordinator Portfolio](https://github.com/JamieChristian22/project-coordinator-portfolio)
4. [Product Manager Portfolio](https://github.com/JamieChristian22/product-manager-portfolio)
5. [Cybersecurity Analyst Portfolio](https://github.com/JamieChristian22/cybersecurity-analyst-portfolio)
6. [Multi-Cloud Engineer Portfolio](https://github.com/JamieChristian22/multi-cloud-engineer-portfolio)

For a cloud/security-heavy search, swap one business portfolio for [AWS Security & Networking](https://github.com/JamieChristian22/aws-security-networking).

## Final independent review

- [ ] Open the [portfolio website](https://jamiechristian22.github.io/) on desktop and mobile; examine image cropping, hover, and keyboard navigation
- [ ] Confirm [website checks and deployments](https://github.com/JamieChristian22/jamiechristian22.github.io/actions) are successful
- [ ] Update repository About descriptions, topics and homepage URLs using the script or the GitHub UI
- [ ] Customize and save the six profile pins
- [ ] Open the root README of each key repository and follow source artifact links
- [ ] Verify native Excel/Power BI files and Terraform configurations with the relevant tools
- [ ] Ensure examples using synthetic data or simulations do not claim real client performance

**Validation policy:** Passing code, links, or source-structure checks is not equivalent to certifying production deployment, security, performance, or live business impact.
