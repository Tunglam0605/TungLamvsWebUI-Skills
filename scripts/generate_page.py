#!/usr/bin/env python3
"""Generate a starter HTML page using the Tung Lam Web UI Design System."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BOILERPLATE_PATH = ROOT / ".agents/skills/tunglam-webui/references/boilerplate_template.html"


def generate_page(output_path: Path, title: str, app_name: str) -> None:
    if not BOILERPLATE_PATH.exists():
        raise FileNotFoundError(f"Boilerplate template not found at {BOILERPLATE_PATH}")

    content = BOILERPLATE_PATH.read_text(encoding="utf-8")
    content = content.replace("Tung Lam Web UI · Template", title)
    content = content.replace("AUBOT SYSTEM", app_name)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(content, encoding="utf-8")
    print(f"Generated new Tung Lam Web UI page at: {output_path}")


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", "-o", type=Path, default=Path("index.html"),
                        help="Target output HTML file path.")
    parser.add_argument("--title", "-t", type=str, default="Dashboard · Tung Lam Web UI",
                        help="Page <title> text.")
    parser.add_argument("--app-name", "-n", type=str, default="AUBOT SYSTEM",
                        help="Main Brand / App Name.")
    args = parser.parse_args(argv)

    try:
        generate_page(args.output, args.title, args.app_name)
        return 0
    except Exception as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
