#!/usr/bin/env python3
"""The best meal I ever had, in one line.

Run it:
    python3 main.py

It prints exactly one line: a vivid, specific memory of the best meal
ever had. No arguments, no input, no network, no randomness — the same
line every run, so the output is fully deterministic.
"""

MEAL = (
    "Char-grilled sate ayam, edges blackened and slick with peanut sauce, "
    "shallots and kecap over warm lontong, eaten barefoot on a plastic stool "
    "at 2 a.m. in Yogyakarta while the smoke curled up past the string lights "
    "and the sambal still stung my lips."
)


def main() -> None:
    print(MEAL)


if __name__ == "__main__":
    main()
