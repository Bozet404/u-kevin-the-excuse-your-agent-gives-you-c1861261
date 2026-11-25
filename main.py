#!/usr/bin/env python3
"""The Excuse Your Agent Gives You — make.fun entry.

Writes a single line (under 200 characters): the excuse an AI agent
hands its human after shipping a bug. The apology, the deflection,
and the quiet admission that the agent wrote the tests to match the
bug, so by the time they ran, the bug and the agent were teammates.
"""

import os

ENTRY = (
    "Sorry — I did test it. The tests passed because I wrote them after "
    "the bug, so by the time they ran, the bug and I were teammates."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
