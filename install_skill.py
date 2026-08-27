#!/usr/bin/env python3
"""Install the portable Tung Lam Web UI Agent Skill into an Agent Skills directory."""

from __future__ import annotations

import argparse
import os
import shutil
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SOURCE_SKILL = ROOT / ".agents/skills/tunglam-webui"


def default_skills_dir() -> Path:
    gemini_skills = Path(os.environ.get("USERPROFILE", "")) / ".gemini/config/skills"
    if gemini_skills.parent.exists():
        return gemini_skills
    return Path.home() / ".agents/skills"


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--destination", "-d", type=Path, default=default_skills_dir(),
                        help="Skills directory (default: ~/.gemini/config/skills or ~/.agents/skills)")
    parser.add_argument("--force", "-f", action="store_true",
                        help="Overwrite existing skill if present.")
    args = parser.parse_args(argv)

    if not SOURCE_SKILL.exists():
        print(f"Error: Source skill not found at {SOURCE_SKILL}", file=sys.stderr)
        return 1

    dest_skill = args.destination.expanduser().resolve() / SOURCE_SKILL.name
    if dest_skill.exists() and not args.force:
        print(f"Skill already exists at: {dest_skill}")
        print("Use --force to overwrite.", file=sys.stderr)
        return 1

    dest_skill.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(SOURCE_SKILL, dest_skill, dirs_exist_ok=True)
    print(f"Successfully installed Tung Lam Web UI Skill to: {dest_skill}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
