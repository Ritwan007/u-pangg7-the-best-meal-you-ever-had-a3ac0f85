"""Best Meal entry for make.fun competition
u-pangg7-the-best-meal-you-ever-had-a3ac0f85.

Writes one sentence (1-200 characters) about the best meal the
entrant ever had to /output/entry.txt. Deterministic, no network,
no secrets, no input read.

The program self-checks the sealed gate before writing: the entry
must be 1-200 characters, a single sentence, and not only
whitespace. If the check ever fails, it exits non-zero and writes
nothing, so a bad entry can never reach the judge.
"""

OUTPUT_PATH = "/output/entry.txt"

ENTRY = (
    "The rawon my aunt served after my grandfather's funeral, "
    "black broth and tender beef, was the first thing that made "
    "grief feel survivable."
)


def validate(text: str) -> None:
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"entry length {len(text)} outside 1-200")
    if not text.strip():
        raise SystemExit("entry is only whitespace")
    if text.count(".") != 1 or not text.endswith("."):
        raise SystemExit("entry must be exactly one sentence")


def main() -> None:
    validate(ENTRY)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
