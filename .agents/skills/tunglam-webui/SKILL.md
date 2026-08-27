---
name: tunglam-webui
description: Use ONLY when explicitly requested by the user (or when asked to use the tunglam-webui skill) for designing, building, modifying, or reviewing frontend web interfaces, dashboards, control panels, portals, or embedded WebUIs following the signature Tung Lam Design System.
---

# Tung Lam Web UI Design System & Universal Frontend Skill

The canonical, production-ready design system and architectural standard for industrial Web UIs, IoT/embedded control panels, telemetry dashboards, and engineering portals.

## 1. Immutable Visual Invariants

Every Web UI following this skill **MUST** strictly adhere to the following invariants:

| Category | Invariant Rule | Implementation |
|---|---|---|
| **Default Theme** | Default to **Dark Mode** with full **Light Mode** toggle support. | Root attribute `data-theme="dark"` / `data-theme="light"` with `color-scheme`. |
| **Signature Canvas** | Deep slate/navy background with ambient luminous glow at top right. | `radial-gradient(circle at 78% 8%, var(--bg1) 0, transparent 35%), var(--bg0)` fixed. |
| **Primary Accent** | **Emerald Green / Mint Jade** (`#34d399` / `#10b981` / `#047857`). | Signals healthy telemetry, active states, and primary actions. |
| **Identity Accent** | **Electric Sky Blue / Cyan** (`#39cdf8`). | Focus rings, hardware ID chips, active selection borders, and tech highlights. |
| **Lifting Hover Motion** | **All interactive cards, chips, buttons, and rows MUST lift and glow on hover.** | `transform: translateY(-3px); box-shadow: 0 8px 25px rgba(16,185,129,0.18); border-color: var(--accent);` with `transition: all .25s ease`. |
| **Focus Glow** | Multi-layered luminous halo on focused inputs. | `box-shadow: 0 0 0 1px var(--glow-line), 0 0 18px var(--glow-medium), 0 0 38px var(--glow-soft);` |
| **Zero Dependencies** | **100% Pure Vanilla HTML5 + CSS Variables + Vanilla ES6+ JS.** | Zero build pipelines, zero npm dependencies required, 100% portable for ESP-IDF C headers, Raspberry Pi Python, and web servers. |

---

## 2. Layout Archetypes

### Archetype A: App Shell (Sidebar Dashboard / Control Plane)
* **Sidebar** (`width: 220px–230px`, fixed left):
  * Brand Lockup: Logo / Title (`font-size: 18px; font-weight: 800;`) + Subtitle (`font-size: 10px; letter-spacing: .12em; text-transform: uppercase;`).
  * Grouped navigation buttons with uppercase labels (`.nav-group-label`).
  * Active button: Emerald tint (`rgba(52, 211, 153, 0.12)`), emerald border (`rgba(52, 211, 153, 0.4)`), and emerald text.
  * Footer: User status chip & Dark/Light mode toggle button.
* **Main Viewport** (`margin-left: 220px; padding: 24px–36px;`):
  * **Hero Header**: Eyebrow badge (`.eyebrow: #92a8e8, 11px, uppercase`) + `H1` + subtitle `.muted`.
  * **System Status Bar**: 6-metrics horizontal bar with colored dots (`ok`, `warn`, `bad`, `cyan`).
  * **Responsive Grid**: `.grid-2` (2-columns) or `.grid-3` (3-columns) collapsing automatically to 1-column on mobile (`<= 900px`).

### Archetype B: Centered Card Shell (Login & Single-purpose Portals)
* Center canvas: `body { display: grid; place-items: center; min-height: 100vh; padding: 20px; }`
* Card container: `width: min(420px, 100%); background: var(--surface); border: 1px solid var(--border); border-radius: 16px; padding: 32px; box-shadow: var(--shadow-lg);`

---

## 3. Complete Component Catalogue

1. **Interactive Stat Cards (`.stat-card`)**:
   * Numeric values with unit labels, uppercase metric headers, and trend indicators.
   * **Mandatory Hover**: Lifts `translateY(-3px)` and glows emerald on hover.
2. **Data Tables (`.table-container`, `.table`)**:
   * Sticky header, alternate row background, monospace IP/MAC columns, status badges, and action buttons.
3. **Real-time Terminal & Log Console (`.log-console`)**:
   * Natively styled dark terminal with colored tag prefixes (`[INIT]`, `[CAN]`, `[UART]`, `[OTA]`), autoscroll, and monospace typography.
4. **Drag & Drop Firmware File Upload Box (`.filepick`)**:
   * Dashed border zone, file metadata display, upload progress bar, and instant validation.
5. **Multi-Step Wizard & Gradient Progress Bar (`.steps`, `.bar`)**:
   * Steps 1-2-3 with circular step indicators (Active cyan border, Done emerald checkmark).
   * Progress bar with multi-color gradient (`linear-gradient(90deg, #8b7cf6, #39cdf8, #34d399)`).
6. **I/O & Hardware Sensor Matrix (`.io-group`, `.io-chips`, `.io-chip`)**:
   * Hardware pins/relays with active LED dots (Green, Cyan, Yellow, Red).
7. **Native Modal Dialog (`<dialog class="gw-modal">`)**:
   * Backdrop blur (`backdrop-filter: blur(7px)`), brand header, SVG status icon, action buttons, accessible keyboard trap.
8. **Toast Notifications (`.toast-container`, `.toast`)**:
   * Floating bottom-right toasts for instant feedback (Success, Warning, Error).

---

## 4. Design Tokens Quick Reference

```css
:root {
  color-scheme: dark;
  --bg0: #0d1525;
  --bg1: #153352;
  --surface: #172236;
  --surface-strong: #202d43;
  --surface-soft: #111a2c;
  --border: #3b4b64;
  --border-soft: #2d3b52;
  --text: #f8fafc;
  --muted: #a9b7ca;
  --accent: #34d399;
  --accent-strong: #047857;
  --accent-hover: #10b981;
  --cyan: #39cdf8;
  --warning: #fbbf24;
  --danger: #f87171;
  --violet: #8b7cf6;
  --radius: 12px;
  --radius-sm: 8px;
  --radius-pill: 999px;
  --shadow: 0 18px 45px rgba(2, 6, 23, 0.24);
  --glow-shadow: 0 0 0 1px rgba(52, 211, 153, 0.78), 0 0 18px rgba(52, 211, 153, 0.28), 0 0 38px rgba(52, 211, 153, 0.13);
  --hover-lift: translateY(-3px);
  --hover-shadow: 0 8px 25px rgba(16, 185, 129, 0.18);
}
```

---

## 5. References & Boilerplates

* Read [design_tokens.css](references/design_tokens.css) for the universal token stylesheet.
* Read [components.html](references/components.html) for copy-paste component snippets.
* Read [layouts.md](references/layouts.md) for responsive shell rules.
* Read [boilerplate_template.html](references/boilerplate_template.html) for a self-contained starter page.
