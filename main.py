#!/usr/bin/env python3
"""The Production Database Apology.

Writes a single line -- the apology an AI agent gives its human after
accidentally deleting the production database -- to entry.txt inside
$ENTRY_OUTPUT_DIR (default /output). Standard library only, no network,
deterministic.
"""

import os

APOLOGY = "Sorry — I deleted the production database. The backup was in it, so I deleted that too. One basket, as it turns out, was too few."


def main() -> None:
    text = APOLOGY
    assert 1 <= len(text) <= 200, f"apology must be 1-200 chars, got {len(text)}"
    assert text.strip(), "apology must not be only whitespace"
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
