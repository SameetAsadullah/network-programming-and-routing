#!/usr/bin/env python3
"""Validate collection structure, media links, and socket-source syntax."""

from __future__ import annotations

import re
import shutil
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXERCISES = (
    "sockets/tcp-client-server", "sockets/tcp-multi-client",
    "sockets/udp-client-server", "sockets/select-concurrent-server",
    "packet-tracer/static-routing", "packet-tracer/dynamic-routing",
    "packet-tracer/dhcp", "packet-tracer/ospf", "packet-tracer/eigrp",
    "packet-tracer/integrated-network",
)


def main() -> int:
    errors: list[str] = []
    for relative in EXERCISES:
        if not (ROOT / relative / "README.md").is_file():
            errors.append(f"missing README: {relative}")

    for relative in EXERCISES[4:]:
        if not any((ROOT / relative / "src").glob("*.pkt")):
            errors.append(f"missing Packet Tracer topology: {relative}")

    tracked = subprocess.check_output(["git", "ls-files"], cwd=ROOT, text=True).splitlines()
    for value in tracked:
        if Path(value).suffix.lower() in {".exe", ".o", ".out"}:
            errors.append(f"generated binary is tracked: {value}")

    pattern = re.compile(r'<img\s+[^>]*src=["\']([^"\']+)["\']', re.IGNORECASE)
    for readme in ROOT.rglob("README.md"):
        for image in pattern.findall(readme.read_text(encoding="utf-8")):
            if not image.startswith(("http://", "https://")) and not (readme.parent / image).is_file():
                errors.append(f"broken image: {readme.relative_to(ROOT)} -> {image}")

    compiler = shutil.which("cc")
    if compiler:
        for source in sorted((ROOT / "sockets").glob("**/*.c")):
            result = subprocess.run(
                [compiler, "-std=c17", "-fsyntax-only", str(source)],
                cwd=source.parent, text=True, capture_output=True,
            )
            if result.returncode:
                errors.append(f"syntax check failed: {source.relative_to(ROOT)}\n{result.stderr}")

    if errors:
        print("Repository validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Validated {len(EXERCISES)} networking exercises.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
