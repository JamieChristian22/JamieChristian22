# Final GitHub Profile Upgrade — Apply the Remaining Settings

**Status:** Portfolio READMEs, project evidence, website visuals, and multiple CI checks have been updated directly. GitHub repository **About settings** and account-level **profile pins** still require your own authenticated GitHub account. The metadata changes below are prepared and ready to execute; they have **not been applied by the connected GitHub tool**.

## 1. Update all ten repository descriptions, homepages, and topics

Open **VS Code → Terminal → New Terminal** on your own computer. The commands below download your existing GitHub *profile repository* to a separate local folder and run the script from that folder:

```bash
git clone https://github.com/JamieChristian22/JamieChristian22.git github-profile-updates
cd github-profile-updates
python3 tools/finish_github_settings.py
```

The first run is a **dry run**. It previews the ten proposed GitHub repository edits but changes nothing.

Next, you need GitHub CLI, which is **not** the VS Code GitHub extension. If it is not installed, use https://cli.github.com/ or (on macOS with Homebrew):

```bash
brew install gh
```

Sign in to the same account that owns the repositories:

```bash
gh auth login
gh auth status
```

For the safest first test, **apply only the portfolio website repository**:

```bash
python3 tools/finish_github_settings.py --apply --only jamiechristian22.github.io
```

The script compares the existing description, homepage and topics, changes only mismatching fields, and re-reads GitHub to verify the update. On success, apply the remaining portfolio settings:

```bash
python3 tools/finish_github_settings.py --apply
```

It can be run a second time without re-adding the same topics. It respects GitHub's 20-topic limit and preserves existing topics. It prints failures instead of hiding them. If you've already cloned the profile repository, run `git pull` in your clone rather than cloning it again.

**What the script changes:** the **description, homepage website and applicable topics** in the About area of these ten repositories: `jamiechristian22.github.io`, `JamieChristian22`, `product-manager-portfolio`, `product-owner-portfolio`, `marketing-analytics-portfolio`, `financial-analyst-portfolio`, `multi-cloud-devops-engineering-projects`, `multi-cloud-architect-portfolio`, `data-science-portfolio`, and `cloud-support-operations-portfolio`.

**What it does not change:** code, repository visibility, permissions, secrets, branch rules, the account-level personal website field, or profile pins. No password or token is written to source files. The script verifies it is signed in as **JamieChristian22** before attempting changes.

## 2. Update the personal profile website

The Website field on your **personal GitHub user profile** is a separate setting from the About homepage on a repository. To make your new portfolio easy to find:

1. Visit [GitHub Profile Settings](https://github.com/settings/profile).
2. Find **Public profile → URL / Website** (wording may vary).
3. Set it to **https://jamiechristian22.github.io/**.
4. Save the profile update if GitHub prompts you.

The connected repository editing tools cannot change this personal account setting.

## 3. Pin exactly six flagship repositories

Open [your GitHub profile](https://github.com/JamieChristian22), click **Customize your pins** in the Popular repositories/Pinned section, select these public repositories, and click **Save pins**:

| Recommended order | Repository | Reason |
| --- | --- | --- |
| 1 | [Business Analyst Portfolio2](https://github.com/JamieChristian22/Business-Analyst-Portfolio2) | Requirements, documentation, system workflows |
| 2 | [Data Analyst Portfolio](https://github.com/JamieChristian22/data-analyst-portfolio) | SQL, Python, analysis, and data quality |
| 3 | [Project Coordinator Portfolio](https://github.com/JamieChristian22/project-coordinator-portfolio) | Project delivery, risks, process coordination |
| 4 | [Product Manager Portfolio](https://github.com/JamieChristian22/product-manager-portfolio) | Six product decision cases with linked artifacts |
| 5 | [Cybersecurity Analyst Portfolio](https://github.com/JamieChristian22/cybersecurity-analyst-portfolio) | Security monitoring, investigation, documentation |
| 6 | [Multi-Cloud Engineer Portfolio](https://github.com/JamieChristian22/multi-cloud-engineer-portfolio) | AWS/Azure/GCP platform concepts and evidence |

For a cloud/security-only campaign, consider swapping one business-focused pin for [AWS Security & Networking](https://github.com/JamieChristian22/aws-security-networking). GitHub allows up to six pinned items, including repositories/gists.

## 4. Check the completed result

- [ ] The About panel for [the portfolio website repository](https://github.com/JamieChristian22/jamiechristian22.github.io) has the new description, web URL and five suggested topics
- [ ] The [profile README repository](https://github.com/JamieChristian22/JamieChristian22) no longer links to an outdated homepage
- [ ] [Product Manager](https://github.com/JamieChristian22/product-manager-portfolio) and [Data Science](https://github.com/JamieChristian22/data-science-portfolio) now accurately describe their implemented case studies without claiming unverified production business outcomes
- [ ] The profile Website field goes to the portfolio
- [ ] Six selected repositories are pinned
- [ ] The [portfolio website](https://jamiechristian22.github.io/) still opens and displays eight self-hosted project images
- [ ] All relevant [GitHub Actions checks](https://github.com/JamieChristian22/jamiechristian22.github.io/actions) remain green

## Additional verification boundaries

Automated repository checks support syntax, navigation and selected tests; they do not independently certify native Power BI or Excel artifacts, all cloud deployments, live website accessibility, historical secrets removal, or actual client business outcomes. Continue to separate simulated case studies from real production evidence.
