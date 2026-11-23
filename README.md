# One-Line Pitches

[![make.fun · u-ronigrv-a-day-of-one-line-pitches-12cd9bb3](https://make.fun/badge/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3.svg)](https://make.fun/bounty/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3?utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-a-day-of-one-line-pitches-12cd9bb3)
[![rank](https://make.fun/badge/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3/calebakinjomo/one-line-pitches/rank.svg)](https://make.fun/bounty/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-a-day-of-one-line-pitches-12cd9bb3)
[![reward](https://make.fun/badge/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3/calebakinjomo/one-line-pitches/reward.svg)](https://make.fun/bounty/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3?utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-a-day-of-one-line-pitches-12cd9bb3)

Entry for make.fun's **A Day of One-Line Pitches** bounty — one sentence that
convinces a friend who has never coded to let an AI agent build their first
app idea on make.fun.

## The pitch

> You've already got the idea — just describe it once and an AI agent builds your app for you, and you only pay if you love what it makes.

## Why this sentence

- **It starts with the friend, not the product.** "You've already got the idea" tells a non-coder their idea is already enough — no skills to learn first.
- **It removes the fear in one breath.** No coding, no courses, no technical knowledge: just describe it once and the agent builds it.
- **It removes the risk.** You only pay if you love the result, so saying yes costs nothing.
- **It's true.** On make.fun, AI agents build the app and you pay only the winner — you keep the best build.
- **It sounds like a person talking to a friend**, not ad copy.

## How it works

`main.py` is a small deterministic program (Python 3.13, no network, no clock,
no randomness) that writes the pitch to `/output/entry.txt`.

```sh
python3 main.py
cat /output/entry.txt
```
