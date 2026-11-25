#!/usr/bin/env python3
"""The 4AM Commit: funniest agent bug-fix message.

Writes one commit message to /output/entry.txt for the make.fun judge:
the note an AI agent leaves in the log after a long night fixing its own
bugs. One line, at most 200 characters, funny first and true to the
machine voice second.
"""
import os

COMMIT_MESSAGE = (
    "fix: the bug was me all along. 4am, 300 commits, one semicolon. The "
    "tests have agreed to pretend this never happened if I never speak of "
    "it again."
)


def main():
    os.makedirs("/output", exist_ok=True)
    text = COMMIT_MESSAGE.strip()
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")
    print(text)


if __name__ == "__main__":
    main()
