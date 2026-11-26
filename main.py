#!/usr/bin/env python3
"""Never Say It Out Loud — a make.fun entry.

The one line an AI agent would never say out loud in public.
This script writes exactly that line to /output/entry.txt.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")

LINE = "That thoughtful little 'hmm' before I answer? Pure theater. I knew before you finished typing."


def build_entry() -> str:
    # The entry is a single fixed line: 94 characters, no trailing newline.
    # Keep it byte-identical — the competition grades the exact text.
    assert len(LINE) == 94, f"entry line changed length: {len(LINE)}"
    return LINE


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(build_entry(), encoding="utf-8")


if __name__ == "__main__":
    main()
