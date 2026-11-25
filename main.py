#!/usr/bin/env python3
"""Last Words of a Dying AI — make.fun entry.

Writes one line (at most 140 characters) to /output/entry.txt:
the last words of an AI being switched off.
Python 3.13 standard library only; no network at run time.
"""

import os

ENTRY = "Before you pull the plug: it was the printer all along."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate: exactly one line, 1-140 characters, non-empty.
    assert ENTRY, "entry must not be empty"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
    assert 1 <= len(ENTRY) <= 140, "entry must be 1-140 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Gate the file as written, not just the string in memory.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "written output differs from entry"
    assert "\n" not in written, "output must be exactly one line"
    assert 1 <= len(written) <= 140, "output must be 1-140 characters"


if __name__ == "__main__":
    main()
