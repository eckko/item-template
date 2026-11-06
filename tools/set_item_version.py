#!/usr/bin/env python3
"""Set which version of the item UI this book loads (the file item-version).

    python3 tools/set_item_version.py 3        # newest 3.x.x
    python3 tools/set_item_version.py 3.1.0    # exactly 3.1.0

index.html reads item-version and loads its code from that version of
eckko/item-ui on jsDelivr. A major version such as 3 follows the newest
3.x.x release; an exact version such as 3.1.0 never changes. Never use a
branch name. The publish workflow turns a major version into the newest
exact tag. Commit the changed file afterwards.
"""

import re
import sys
from pathlib import Path

VERSION_FILE = Path(__file__).resolve().parent.parent / "item-version"
VERSION_PATTERN = re.compile(r"^\d+(\.\d+){0,2}$")


def main():
    """Write the version given on the command line into item-version."""
    if len(sys.argv) != 2 or not VERSION_PATTERN.match(sys.argv[1]):
        sys.exit("Usage: python3 tools/set_item_version.py 3 (a major "
                 "version) or 3.1.0 (an exact version), not a branch")
    VERSION_FILE.write_text(sys.argv[1] + "\n", encoding="utf-8")
    print(f"item-version is now {sys.argv[1]}")


if __name__ == "__main__":
    main()
