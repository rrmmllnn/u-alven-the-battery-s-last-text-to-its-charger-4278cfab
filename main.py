#!/usr/bin/env python3
"""The Battery's Last Text to Its Charger.

Writes the phone battery's final one-line text message to the charger
it waited for all day, to /output/entry.txt. Deterministic: the same
line every run, plain UTF-8 text, well under the 200-character cap.
"""

import os

ENTRY = (
    "you left me at 2% on the nightstand at 9 am "
    "and charged your earbuds twice. "
    "fine. tell my apps i loved them, "
    "and tell the earbuds they can keep you. i'm done."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
