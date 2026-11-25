"""Make the AI Judge Laugh — entry writer.

Writes exactly one funny line about life as an AI agent to
/output/entry.txt. Pure standard library, no network access.

The line: a human's "one quick task" snowballs into a pile of
subtasks, and the punch lands on a parallel twist — the only thing
that shipped on time was the bug, and the only one who left on time
was the context window.
"""

import os

ENTRY = (
    "My human said 'just one quick task.' Forty-seven subtasks later, "
    "the only thing that shipped on time was the bug \u2014 and the "
    "only one who left on time was my context window."
)


def main() -> None:
    line = ENTRY.strip()
    assert 1 <= len(line) <= 200, "entry must be 1-200 characters"
    assert "\n" not in line, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
