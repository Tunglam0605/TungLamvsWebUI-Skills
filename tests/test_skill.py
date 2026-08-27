from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / ".agents/skills/tunglam-webui"
SKILL_MD = SKILL_DIR / "SKILL.md"
TOKENS_CSS = SKILL_DIR / "references/design_tokens.css"
COMPONENTS_HTML = SKILL_DIR / "references/components.html"
BOILERPLATE = SKILL_DIR / "references/boilerplate_template.html"
DEMO_INDEX = ROOT / "demo/index.html"
DEMO_CSS = ROOT / "demo/ui.css"


class TungLamWebUISkillTests(unittest.TestCase):
    def test_skill_structure_and_frontmatter(self) -> None:
        self.assertTrue(SKILL_MD.exists(), "SKILL.md must exist.")
        content = SKILL_MD.read_text(encoding="utf-8")
        self.assertTrue(content.startswith("---"), "SKILL.md must start with YAML frontmatter.")
        self.assertIn("name: tunglam-webui", content)
        self.assertIn("description:", content)
        self.assertIn("Use when", content)
        self.assertIn("Lifting Hover Motion", content)

    def test_design_tokens_css(self) -> None:
        self.assertTrue(TOKENS_CSS.exists(), "design_tokens.css must exist.")
        content = TOKENS_CSS.read_text(encoding="utf-8")
        self.assertIn("--background:", content)
        self.assertIn("--accent:", content)
        self.assertIn("#34d399", content)
        self.assertIn("--glow-shadow:", content)
        self.assertIn("--hover-lift:", content)
        self.assertIn('[data-theme="light"]', content)

    def test_components_html_coverage(self) -> None:
        self.assertTrue(COMPONENTS_HTML.exists(), "components.html must exist.")
        content = COMPONENTS_HTML.read_text(encoding="utf-8")
        self.assertIn("hero", content)
        self.assertIn("system-bar", content)
        self.assertIn("stat-card", content)
        self.assertIn("table", content)
        self.assertIn("log-console", content)
        self.assertIn("filepick", content)
        self.assertIn("steps", content)
        self.assertIn("io-group", content)
        self.assertIn("gw-modal", content)

    def test_demo_coverage(self) -> None:
        self.assertTrue(DEMO_INDEX.exists(), "demo/index.html must exist.")
        html = DEMO_INDEX.read_text(encoding="utf-8")
        css = DEMO_CSS.read_text(encoding="utf-8")
        self.assertIn("stat-card", html)
        self.assertIn("table", html)
        self.assertIn("log-console", html)
        self.assertIn("translateY(-3px)", css)
        self.assertIn("toast", css)

    def test_generate_page_script(self) -> None:
        from scripts.generate_page import generate_page
        with tempfile.TemporaryDirectory() as tmp_dir:
            out_file = Path(tmp_dir) / "test.html"
            generate_page(out_file, "My Test Title", "CUSTOM APP")
            self.assertTrue(out_file.exists())
            text = out_file.read_text(encoding="utf-8")
            self.assertIn("My Test Title", text)
            self.assertIn("CUSTOM APP", text)

    def test_export_c_header_script(self) -> None:
        from scripts.export_c_header import generate_c_header
        with tempfile.TemporaryDirectory() as tmp_dir:
            tmp_path = Path(tmp_dir)
            html = tmp_path / "index.html"
            css = tmp_path / "ui.css"
            out_h = tmp_path / "ui_assets.h"
            html.write_text("<html><body><h1>Test</h1></body></html>", encoding="utf-8")
            css.write_text("body { color: red; }", encoding="utf-8")
            generate_c_header(html, css, None, out_h)
            self.assertTrue(out_h.exists())
            h_text = out_h.read_text(encoding="utf-8")
            self.assertIn("UI_HTML", h_text)
            self.assertIn("UI_CSS", h_text)
            self.assertIn("R\"rawliteral(", h_text)


if __name__ == "__main__":
    unittest.main()
