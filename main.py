"""Write the one-line excuse to /output/entry.txt.

The excuse is a single line, exactly 102 characters.
"""
import os

EXCUSE = (
    "I missed the deadline while optimising the reminder "
    "that was supposed to remind me about the deadline."
)


def main():
    # The scorer accepts 1-160 UTF-8 characters; refuse to emit anything
    # outside that window rather than shipping a bad entry.
    if not (1 <= len(EXCUSE) <= 160):
        raise ValueError(f"excuse is {len(EXCUSE)} chars, must be 1-160")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(EXCUSE + "\n")


if __name__ == "__main__":
    main()
