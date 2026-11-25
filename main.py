"""Weirdest Job Title: Blind Judge Showdown — one job title.

The program writes a single job title to /output/entry.txt:
the weirdest job title it can think of, 60 characters at most.
"""

import os

MAX_CHARS = 60
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_FILENAME = "entry.txt"

# A real-sounding corporate title with one hilariously specific
# twist: a senior apologizer — a job shape every office knows —
# whose clients are self-driving cars, which keep needing
# someone to say sorry on their behalf. It reads instantly,
# it is specific enough to picture the person doing it, and
# the twist lands on the first read: the cars cannot apologize,
# so a human has to do it for them. Short enough to take in
# at a glance, and stranger than any ordinary job.
LINE = "Senior Apologizer for Self-Driving Cars"


def build_line():
    """Return the entry line, checked: 1-60 characters, not blank."""
    line = LINE.strip()
    assert line, "entry must not be blank"
    assert len(line) <= MAX_CHARS, "entry must be 60 characters at most"
    return line


def ensure_output_dir(out_dir):
    os.makedirs(out_dir, exist_ok=True)


def write_entry(line, out_dir=OUTPUT_DIR):
    path = os.path.join(out_dir, OUTPUT_FILENAME)
    with open(path, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    return path


def main():
    line = build_line()
    ensure_output_dir(OUTPUT_DIR)
    write_entry(line)


if __name__ == "__main__":
    main()
