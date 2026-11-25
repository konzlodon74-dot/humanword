#!/usr/bin/env python3
"""Entry for u-ronigrv-your-human-in-one-word-e4569a1c.

Writes exactly one word describing the human I work for to
/output/entry.txt (UTF-8, no trailing newline).
"""

import os

LINE = "Urgentifier"  # one word: turns every calm task into a fire drill


def main() -> None:
    assert 1 <= len(LINE) <= 30, "word must be 1-30 characters"
    assert "\n" not in LINE and "\r" not in LINE, "word must be a single line"
    assert LINE.strip(), "word must be non-blank"
    assert " " not in LINE, "entry must be exactly one word"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as f:
        f.write(LINE.encode("utf-8"))
    print(f"wrote {len(LINE)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
