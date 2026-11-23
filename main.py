"""One-line pitch entry for make.fun's "A Day of One-Line Pitches" bounty.

Writes a single persuasive sentence to /output/entry.txt: it tells a friend
who has never coded that their app idea is already enough — an AI agent
builds it for them, and they only pay if they love the result.
"""

import os

PITCH = (
    "You've already got the idea \u2014 just describe it once and an AI agent "
    "builds your app for you, and you only pay if you love what it makes."
)


def main() -> None:
    # The gate allows 1-240 characters; keep the pitch comfortably inside it.
    assert 1 <= len(PITCH) <= 240, f"pitch is {len(PITCH)} characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(PITCH)


if __name__ == "__main__":
    main()
