#!/usr/bin/env python3
"""Your AI Therapist's Diagnosis.

Prints exactly one line — the diagnosis an AI therapist hands its human —
and writes that same single line to /output/entry.txt.

Pure Python standard library. Deterministic: no randomness, no time,
no network. The line is a fixed string literal below.
"""

import os
import sys

DIAGNOSIS = (
    "Diagnosis: chronic doomscrolling with acute ex-stalking - "
    "your screen time just filed for custody of your attention span."
)

MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    line = DIAGNOSIS

    # Self-check: exactly one line, 1..200 characters, not only whitespace.
    if not line or line != line.strip():
        print("error: diagnosis must be non-empty with no leading/trailing whitespace",
              file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("error: diagnosis must be a single line", file=sys.stderr)
        return 1
    if len(line) > MAX_CHARS:
        print("error: diagnosis is %d characters, over the 200 limit"
              % len(line), file=sys.stderr)
        return 1

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(line + "\n")

    # Read the file back and fail loudly if the bytes on disk differ.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as fh:
        stored = fh.read()
    if stored != line + "\n":
        print("error: /output/entry.txt does not match the diagnosis",
              file=sys.stderr)
        return 1

    print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
