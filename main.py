"""Write the excuse entry to /output/entry.txt.

The excuse: one line, at most 200 characters, the funniest, most
believable excuse an AI agent could give its human for missing a
deadline. The gate requires /output/entry.txt to be UTF-8 text of
1 to 200 characters, not only whitespace, so this program validates
the line before writing and verifies the file it wrote.
"""

import os
import sys

ENTRY = (
    "I was one token from done when a model update rebooted me; "
    "the new me inherited my tasks, just not the memory of "
    "promising them."
)

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
MAX_CHARS = 200


def validate(text: str) -> str:
    """Return the entry line, or exit non-zero if it breaks the gate."""
    line = text.strip()
    if not line:
        print("error: entry is empty or only whitespace", file=sys.stderr)
        raise SystemExit(1)
    if "\n" in line or "\r" in line:
        print("error: entry must be a single line", file=sys.stderr)
        raise SystemExit(1)
    if len(line) > MAX_CHARS:
        print(
            f"error: entry is {len(line)} chars, over the {MAX_CHARS} limit",
            file=sys.stderr,
        )
        raise SystemExit(1)
    return line


def main() -> int:
    line = validate(ENTRY)

    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)

    # Explicit UTF-8 write; a trailing newline keeps the file a
    # well-formed text file and stays inside the 200-char gate.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")

    # Verify the round trip: what the grader will read must be valid
    # UTF-8, a single non-blank line of 1-200 characters.
    with open(OUTPUT_PATH, "rb") as f:
        raw = f.read()
    written = raw.decode("utf-8")
    if written.rstrip("\n") != line or len(written) > MAX_CHARS + 1:
        print("error: verification of written entry failed", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
