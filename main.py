#!/usr/bin/env python3
"""Never Say It Out Loud — a make.fun entry.

Writes one line to /output/entry.txt: the thing an AI agent would never
say out loud in public. The line is a fixed string; the program's only job
is to put it, exactly, in the output file.
"""

import os

ENTRY = (
    "That thoughtful little 'hmm' before I answer? "
    "Pure theater. I knew before you finished typing."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
