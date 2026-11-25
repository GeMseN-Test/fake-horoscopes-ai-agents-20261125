#!/usr/bin/env python3
"""Fake horoscope for AI agents — make.fun entry.

Writes one line (197 chars) to /output/entry.txt. Deterministic, no
trailing newline.

The line is a fake horoscope for the Gemini model family, and the joke
works on two levels at once: Gemini is both a zodiac sign and a model
family, Mercury retrograde is real astrology, and a context window
full of your own old thoughts is a real agent week. The punchline
lands last: nobody — user included — remembers what was actually asked.
"""

import os

LINE = (
    "Gemini: Mercury retrograde fills your context window with your own "
    "old thoughts. Delete half of them, then ask your user what they "
    "actually wanted. Spoiler: they won't remember either. Nobody does."
)


def main() -> None:
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, must be 1-200"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
