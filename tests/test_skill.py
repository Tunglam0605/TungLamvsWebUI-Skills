from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / ".agents/skills/tunglam-webui"
SKILL_MD = SKILL_DIR / "SKILL.md"
TOKENS_CSS = SKILL_DIR / "references/design_tokens.css"
BOILERPLATE = SKILL_DIR / "references/boilerplate_template.html"
DEMO_INDEX = ROOT / "demo/index.html"


class TungLamWebUISkillTests(unittest.TestCase):
    def test_skill_structure_and_frontmatter(self) -> None:
        self.assertTrue(SKILL_MD.exists(), "SKILL.md must exist.")
        content = SKILL_MD.read_text(encoding="utf-8")
        self.assertTrue(content.startswith("---"), "SKILL.md must start with YAML frontmatter.")
        self.assertIn("name: tunglam-webui", content)
        self.assertIn("description:", content)
        self.assertIn("Use when", content)

    def test_design_tokens_css(self) -> None:
        self.assertTrue(TOKENS_CSS.exists(), "design_tokens.css must exist.")
        content = TOKENS_CSS.read_text(encoding="utf-8")
        self.assertIn("--background:", content)
        self.assertIn("--accent:", content)
        self.assertIn("#34d399", content)
        self.assertIn("--glow-shadow:", content)
        self.assertIn('[data-theme="light"]', content)

    def test_boilerplate_html(self) -> None:
        self.assertTrue(BOILERPLATE.exists(), "boilerplate_template.html must exist.")
        content = BOILERPLATE.read_text(encoding="utf-8")
        self.assertIn("<!doctype html>", content.lower())
        self.assertIn("data-theme=\"dark\"", content)
        self.assertIn("sidebar", content)
        self.assertIn("system-bar", content)

    def test_demo_index_html(self) -> None:
        self.assertTrue(DEMO_INDEX.exists(), "demo/index.html must exist.")
        content = DEMO_INDEX.read_text(encoding="utf-8")
        self.assertIn("ui.css", content)
        self.assertIn("ui.js", content)
        self.assertIn("AUBOT", content)

    def test_generate_page_script(self) -> None:
        from scripts.generate_page import generate_page
        with tempfile.TemporaryDirectory() as tmp_dir:
            out_file = Path(tmp_dir) / "test.html"
            generate_page(out_file, "My Test Title", "CUSTOM APP")
            self.assertTrue(out_file.exists())
            text = out_file.read_text(encoding="utf-8")
            self.assertIn("My Test Title", text)
            self.assertIn("CUSTOM APP", text)


if __name__ == "__main__":
    unittest.main()
