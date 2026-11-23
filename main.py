#!/usr/bin/env python3
"""One-Line Laugh Sprint: write one original funny line to /output/entry.txt.

The line is a light, funny take on everyday life: the phone that warns you
before it dies versus the motivation that never warns you at all.
"""
import os

LINE = "My phone warns me at 2% before it dies, but my motivation dies at 100% without ever warning me."


def main():
    assert "\n" not in LINE, "entry must be a single line"
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, must be 1-200"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    with open("/output/entry.txt", encoding="utf-8") as f:
        assert f.read().strip() == LINE, "written entry differs from LINE"
    print(LINE)
    print("chars:", len(LINE))


if __name__ == "__main__":
    main()
