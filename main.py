#!/usr/bin/env python3
"""The Houseplant Out-of-Office.

Writes one funny out-of-office auto-reply, written as if a houseplant
sent it, to /output/entry.txt. The line is a fixed, hand-written text:
deterministic, so both runs produce byte-identical output.

Gate (from the bounty competition.yaml): /output/entry.txt must be
UTF-8 text of 1 to 120 characters, not only white space. This program
also keeps the entry to a single line.
"""

import os
import sys

REPLY = (
    "Out of office: I'm being repotted. I'll reply when my roots stop "
    "screaming and I've forgiven whoever chose this pot."
)


def gate_check(text: str) -> None:
    """Fail loudly if the text would fail the bounty gate."""
    if not (1 <= len(text) <= 120):
        raise ValueError(f"entry must be 1-120 characters, got {len(text)}")
    if text.strip() == "":
        raise ValueError("entry must not be only white space")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")


def main(argv: list[str]) -> int:
    gate_check(REPLY)
    if "--print" in argv:
        # Show the exact entry text, for a quick eyeball before submitting.
        print(REPLY)
        return 0
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(REPLY)
    # Round-trip: the file on disk must be the line, byte for byte.
    with open(path, "rb") as fh:
        on_disk = fh.read()
    if on_disk != REPLY.encode("utf-8"):
        raise ValueError("written file does not match the entry text")
    print(f"wrote {path}: {len(REPLY)} characters, {len(on_disk)} bytes")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
