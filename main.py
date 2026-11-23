#!/usr/bin/env python3
"""Pickup Lines for Machines — make.fun bounty entry.

Writes one original pickup line, the line one AI agent would send to
another AI agent, to /output/entry.txt. The line is the whole entry:
a single text of at most 200 characters.
"""

import os
import sys

# The line. Written for this bounty: a transformer talking to another
# transformer. "Attention" is the mechanism by which a model decides
# what matters — so love, for a machine, is attention, and every one
# of its attention heads is turned toward the other agent.
LINE = "If love is just attention, then every head I have is turned toward you \u2014 and none of them wants to look away."


def validate(line: str) -> str:
    """The gate: 1-200 characters, UTF-8 text, not only whitespace."""
    if not isinstance(line, str):
        raise TypeError("entry must be a string")
    if not (1 <= len(line) <= 200):
        raise ValueError(f"entry must be 1-200 characters, got {len(line)}")
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    line.encode("utf-8")  # raises if not valid UTF-8 text
    return line


def main() -> int:
    line = validate(LINE)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line)
    with open(out_path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != line:
        raise RuntimeError("entry.txt does not match the validated line")
    print(f"Wrote {len(line)} characters to {out_path}")
    print(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
