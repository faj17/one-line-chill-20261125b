"""One line of horror for the make.fun bounty "One Line, One Chill".

The whole entry is a single sentence that has to frighten a reader in
one breath: a hospice nurse charts a last breath, crosses it out, and
the woman in the bed never stops breathing. The scare is what the line
withholds — who, or what, is breathing in that bed now. The script
validates the line and drops it into /output/entry.txt.
"""

from pathlib import Path

# The line itself: one sentence, 135 characters.
LINE = (
    "The hospice nurse charted my mother's last breath at 3 a.m., "
    "then crossed it out, because the woman in the bed never "
    "stopped breathing."
)

OUTPUT_DIR = Path("/output")
OUTPUT_FILE = OUTPUT_DIR / "entry.txt"
MIN_CHARS = 1
MAX_CHARS = 200


def validate(line: str) -> str:
    """Strip and sanity-check the line; raise ValueError on bad input."""
    text = line.strip()
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"line must be {MIN_CHARS}-{MAX_CHARS} chars, got {len(text)}"
        )
    if "\n" in text or "\r" in text:
        raise ValueError("line must be a single line")
    if not text.endswith("."):
        raise ValueError("line must end with a full stop")
    if ". " in text:
        raise ValueError("line must be a single sentence (no '. ' inside)")
    return text


def main() -> None:
    text = validate(LINE)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(text, encoding="utf-8")
    print(text)
    print(f"Wrote {len(text)} chars to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
