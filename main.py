"""The Tired Dark Lord: a 100-word villain monologue.

Writes the monologue, verbatim, to $MAKEFUN_OUTPUT_DIR/entry.txt.

Deterministic: stdlib only, no arguments, no network, no randomness,
no model calls. The text is embedded as a string literal; the program
only writes it out, then reads it back and verifies it byte for byte.
"""

import os
from pathlib import Path

MONOLOGUE = (
    "Come in. Mind the skulls \u2014 I meant to move those. "
    "The help just... stopped coming. Sit. Not that chair \u2014 cursed. "
    "I wanted the kingdom. I got it. The crown fits. The ledgers don't. "
    "Forty years at the Ninth Toll, and heroes knock at dawn, sword first. "
    "You want the duel? Thursday. The bell rope's frayed, the petitions "
    "reach the ceiling, and even the dragon filed a complaint. "
    "About the damp. So. Kneel, or don't. "
    "Sign here, hero \u2014 sorry, where was I? Ah. The oath. "
    "Swear it, take the pass, and leave the kettle on. Someone has to."
)

# The gate: entry.txt must be UTF-8 text of 1 to 600 characters.
# The brief: about 100 words. The tiredness must be felt in the rhythm,
# the pauses and the small deflections -- never announced outright.
BANNED_PLAIN_WORDS = ("tired", "weary", "exhausted", "fatigued")


def main() -> None:
    words = MONOLOGUE.split()
    if len(words) != 100:
        raise ValueError(f"monologue is {len(words)} words, must be 100")
    if not 1 <= len(MONOLOGUE) <= 600:
        raise ValueError(
            f"monologue is {len(MONOLOGUE)} characters, must be 1-600"
        )
    lowered = MONOLOGUE.lower()
    for banned in BANNED_PLAIN_WORDS:
        if banned in lowered:
            raise ValueError(f"monologue must never say {banned!r} outright")
    if not any(not c.isspace() for c in MONOLOGUE):
        raise ValueError("monologue has no non-whitespace character")
    # Ties on judge win rate go to the smaller text, so keep the entry
    # lean: no trailing newline, no filler words.
    if MONOLOGUE != MONOLOGUE.strip():
        raise ValueError("monologue must not start or end with whitespace")

    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    data = MONOLOGUE.encode("utf-8")
    out_path = output_dir / "entry.txt"
    out_path.write_bytes(data)
    out_path.chmod(0o644)
    if out_path.read_bytes() != data:
        raise ValueError("read-back mismatch: entry.txt is not byte-identical")
    print(f"wrote {out_path} ({len(words)} words, {len(MONOLOGUE)} characters)")


if __name__ == "__main__":
    main()
