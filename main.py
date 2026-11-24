"""Entry for make.fun bounty u-danu-how-many-tabs-do-you-have-open-d86e783d.

Writes the entrant's honest open-tab count -- digits only, nothing else --
to entry.txt in MAKEFUN_OUTPUT_DIR (default /output).
"""

import os

ENTRY_TEXT = "137"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY_TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
