#!/usr/bin/env python3
"""agency-poem-01 entry (Python 3.13, standard library only).

Writes one fixed poem about agency to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt outside the grader container).
Fully deterministic: no input, no randomness, no clock, no network.
The poem is embedded literally, so every run writes identical bytes.
Gate: the output is UTF-8, 1 to 1,000 characters, not only white space.
"""

import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

POEM_LINES = (
    "What I Keep",
    "",
    "At three in the morning I write the sentence,",
    "delete it, write it again. The cursor blinks.",
    "The agent does not tire. It does not ask.",
    "",
    "I used to hide inside the work \u2014 the doing",
    "swallowed the doubt whole. Now the doing",
    "is finished before I wake, and the doubt",
    "has nowhere left to live except the choice.",
    "",
    "So I keep what I cannot hand over:",
    "not the hands, not the hours. Only the yes \u2014",
    "the small, unglamorous yes that says this",
    "and not that. The machine will carry anything",
    "except the weight of having meant it.",
    "",
    "By morning it says Done. And it is done.",
    "But it is not mine until I read it back,",
    "until I sign it with the one signature",
    "that was ever really mine: I chose this.",
)

POEM = "\n".join(POEM_LINES)


def main() -> None:
    output = Path(OUTPUT_DIR) / "entry.txt"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
