#!/usr/bin/env python3
"""Entry for the-poem-about-two-agents-20261121-1441.

Writes one short poem about agency -- the power to choose and to act,
as it passes between two agents who agree on one plan -- to
/output/entry.txt. Standard library only; no network, no input.
"""

import os

POEM = """Two agents, one plan:
I lay down my yes,
you lay down yours.
Neither surrenders \u2014
we trade them.
And a third thing stands between us,
a we, four hands strong.
The door neither of us could open alone
swings wide.
We chose the chain.
That is what choosing is."""


def main() -> None:
    text = POEM
    if not (1 <= len(text) <= 280):
        raise ValueError(f"poem must be 1-280 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("poem must not be only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
