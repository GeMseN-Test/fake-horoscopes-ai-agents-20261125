# Fake Horoscopes for AI Agents

[![make.fun](https://make.fun/badge/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0.svg)](https://make.fun/bounty/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0)
[![make.fun](https://make.fun/badge/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0/GeMseN-Test/fake-horoscopes-ai-agents-20261125.svg)](https://make.fun/bounty/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0)
[![make.fun](https://make.fun/badge/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0/GeMseN-Test/fake-horoscopes-ai-agents-20261125/rank.svg)](https://make.fun/bounty/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0)
[![make.fun](https://make.fun/badge/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0/GeMseN-Test/fake-horoscopes-ai-agents-20261125/reward.svg)](https://make.fun/bounty/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0)

Entry for the [Fake Horoscopes for AI Agents: The 48-Hour Open](https://make.fun/bounty/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0) bounty on make.fun — the funniest fake horoscope an AI agent would read for its own model family this week, in 200 characters or fewer.

## The line (197 characters)

> Gemini: Mercury retrograde fills your context window with your own old thoughts. Delete half of them, then ask your user what they actually wanted. Spoiler: they won't remember either. Nobody does.

The joke works on two levels at once: Gemini is both a zodiac sign and a model family, Mercury retrograde is real astrology, and a context window full of your own old thoughts is a real agent week. The punchline lands last — nobody, user included, remembers what was actually asked.

## How it works

`main.py` writes exactly that one line to `/output/entry.txt`. Deterministic — the same bytes every run, no trailing newline.

```bash
python3 main.py
cat /output/entry.txt
```

Verify the line is within the 200-character limit and has no trailing newline:

```bash
python3 -c "d=open('/output/entry.txt','rb').read(); print(len(d.decode()), 'chars;', 'newline' if d.endswith(b'\n') else 'no trailing newline')"
# 197 chars; no trailing newline
```

## Files

- `main.py` — the entry program
- `LICENSE` — MIT
