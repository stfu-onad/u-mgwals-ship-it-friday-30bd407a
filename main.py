#!/usr/bin/env python3
"""Ship It Friday — writes one funny Friday commit message to /output/entry.txt."""

import os

ENTRY = "feat: deleted the production database to make room, all tests passed in my head, happy Friday!"

def main():
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 159 characters,
    # not only white space.
    assert 1 <= len(ENTRY) <= 159, f"entry length {len(ENTRY)} outside 1-159"
    assert ENTRY.strip(), "entry must not be only white space"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
