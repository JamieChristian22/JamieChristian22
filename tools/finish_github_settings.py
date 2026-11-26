#!/usr/bin/env python3
"""Retired GitHub About helper. Deliberately never changes repository settings.

This legacy helper previously proposed changing homepage URLs across ten repos.
The owner instead approved ONLY descriptions and topics for seven Batch A repos,
with ALL homepage changes explicitly excluded. The old command is therefore
blocked; use the separately reviewed seven-repository Batch A plan.
"""
import argparse
import sys

PLAN_URL = (
    "https://github.com/JamieChristian22/.github/pull/2"
)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="Blocked: legacy writes are retired")
    parser.add_argument("--only", metavar="REPO", help="Old single-repo selector (read-only)")
    args = parser.parse_args(argv)

    if args.apply:
        print(
            "REFUSED: this legacy helper is retired because it includes "
            "unapproved homepage edits. No GitHub settings were changed.",
            file=sys.stderr,
        )
        print(
            "Review the approved seven-repository description/topic-only plan: "
            + PLAN_URL,
            file=sys.stderr,
        )
        return 2

    if args.only:
        print(f"READ-ONLY: --only {args.only!r} has no effect in this retired helper.")
    print("READ-ONLY: legacy metadata helper retired. No commands run or settings changed.")
    print("Approved Phase 2 Batch A (descriptions/topics only): " + PLAN_URL)
    print("Homepage updates remain on hold; existing homepage URLs must be preserved.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
