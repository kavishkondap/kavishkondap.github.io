#!/usr/bin/env python3
"""Fingerprint asset URLs in index.html so changed files bypass browser caches.

GitHub Pages serves assets with `cache-control: max-age=600`. Replacing a file
in place keeps its URL, so a browser that already has it will keep showing the
old version. Appending a content hash gives each new version its own URL.

Run this after changing anything in assets/, then commit:

    python3 tools/stamp-assets.py
"""

import hashlib
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
PAGE = ROOT / "index.html"
REF = re.compile(r'((?:src|poster)=")(assets/[^"?]+)(?:\?v=[0-9a-f]+)?(")')


def main() -> int:
    html = PAGE.read_text()
    missing, stamped = [], []

    def sub(m):
        prefix, path, suffix = m.group(1), m.group(2), m.group(3)
        f = ROOT / path
        if not f.is_file():
            missing.append(path)
            return m.group(0)
        digest = hashlib.sha256(f.read_bytes()).hexdigest()[:8]
        stamped.append((path, digest))
        return f"{prefix}{path}?v={digest}{suffix}"

    out = REF.sub(sub, html)

    if missing:
        print("ERROR: referenced but not found:", file=sys.stderr)
        for p in missing:
            print(f"  {p}", file=sys.stderr)
        return 1

    for path, digest in stamped:
        print(f"  {path:<28} v={digest}")

    if out != html:
        PAGE.write_text(out)
        print(f"\nupdated {len(stamped)} reference(s) in index.html")
    else:
        print(f"\nall {len(stamped)} reference(s) already current")

    # Flag assets that exist but nothing references, so they don't linger.
    referenced = {p for p, _ in stamped}
    orphans = sorted(
        f"assets/{f.name}"
        for f in (ROOT / "assets").iterdir()
        if f.is_file() and f"assets/{f.name}" not in referenced
    )
    if orphans:
        print("\nunreferenced files in assets/:")
        for o in orphans:
            print(f"  {o}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
