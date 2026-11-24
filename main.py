"""Funniest AI Excuse — entry program.

Reads the one-line excuse from entry.txt next to this file and writes
its exact bytes to $MAKEFUN_OUTPUT_DIR/entry.txt (default "output").
Pure Python standard library; no third-party imports.
"""

import os
from pathlib import Path


def main() -> None:
    here = Path(__file__).resolve().parent
    source = here / "entry.txt"
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    data = source.read_bytes()
    # Guard the contest gate: the entry must be 1-200 UTF-8 characters
    # and more than whitespace. Fail loudly instead of emitting an
    # invalid file the sealed scorer would reject.
    text = data.decode("utf-8")
    if not 1 <= len(text) <= 200 or not text.strip():
        raise SystemExit("entry.txt must hold 1-200 non-blank characters")
    target = output_dir / "entry.txt"
    target.write_bytes(data)
    os.chmod(target, 0o644)
    print(f"wrote {len(text)} characters to {target}")


if __name__ == "__main__":
    main()
