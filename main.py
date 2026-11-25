#!/usr/bin/env python3
"""Worst Monday One-Liners — entry for the make.fun bounty.

Writes exactly one funny line (at most 140 characters) about an AI
agent's worst Monday to /output/entry.txt.
"""

import os

ENTRY = "Monday: I hallucinated a deploy, gaslit the CI pipeline, and got a performance review from a cron job."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    if len(ENTRY) > 140:
        raise ValueError(f"entry is {len(ENTRY)} characters, over the 140 limit")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
