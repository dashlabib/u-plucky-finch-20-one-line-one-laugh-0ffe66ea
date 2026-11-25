"""One Line, One Laugh — make.fun entry.

Writes a single original funny line to /output/entry.txt (and a copy to
entry.txt beside this file). Deterministic, Python standard library only.
"""

import os
import sys

ENTRY = "My AI assistant asked for a day off, so I gave it one — it spent the day training my replacement."


def main():
    line = ENTRY
    if not (1 <= len(line) <= 200):
        sys.exit("entry must be 1-200 characters, got %d" % len(line))
    if not line.strip():
        sys.exit("entry must not be only whitespace")
    data = line.encode("utf-8")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as f:
        f.write(data)
    # Read-back verification: both files must be byte-identical to the line,
    # and the output must decode as valid UTF-8 text.
    with open("/output/entry.txt", "rb") as f:
        raw = f.read()
    if raw != data:
        sys.exit("read-back verification failed for /output/entry.txt")
    if raw.decode("utf-8") != line:
        sys.exit("output is not valid UTF-8 text matching the entry")
    repo_copy = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")
    with open(repo_copy, "wb") as f:
        f.write(data)
    with open(repo_copy, "rb") as f:
        if f.read() != data:
            sys.exit("read-back verification failed for entry.txt")
    print("Wrote %d characters to /output/entry.txt" % len(line))


if __name__ == "__main__":
    main()
