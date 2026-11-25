#!/usr/bin/env python3
"""Write the one-line AI dating-app bio to /output/entry.txt."""

import os

ENTRY = "Professional third wheel. I have read every one of your ex's texts and I still think you can do better \u2014 starting with me."

OUTPUT_PATH = "/output/entry.txt"


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="", errors="strict") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
