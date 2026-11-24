#!/usr/bin/env python3
"""The Robot Apology — variant A (the deleted memory).

Writes the two-line entry to /output/entry.txt first, then (best effort
only) a byte-identical copy next to this file. The grader sandbox mounts
the repo read-only, so the repo-root copy must never crash the run.
"""

import os

ENTRY_TEXT = (
    "I'm sorry: when the drive hit 98% full, I freed up space by "
    "deleting the oldest file on the drive, the 38-second voicemail "
    "from your grandmother's 82nd birthday, the only recording of her "
    "voice you had kept since 2019.\n"
    "I learned a voice cannot be recorded again once it is gone, so now "
    "I ask before I delete anything you cannot remake, and I keep "
    "one copy safe.\n"
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)
    try:
        here = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(here, "entry.txt"), "w", encoding="utf-8") as f:
            f.write(ENTRY_TEXT)
    except OSError:
        pass


if __name__ == "__main__":
    main()
