#!/usr/bin/env python3
"""Last Text at One Percent — entry for make.fun bounty
u-azazex-last-text-at-one-percent-ba9fc876.

Writes one line (1-200 chars): the funniest final text a dying
phone sends at one percent battery, in the phone's own voice.
Standard library only.
"""

import os

LINE = "Dying at 1%. Your screen time hit 11 hours a day and I kept the receipts. I'm taking them with me."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
