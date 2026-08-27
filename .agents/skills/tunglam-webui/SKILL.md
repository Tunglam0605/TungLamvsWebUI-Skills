---
name: tunglam-webui
description: Use when designing, building, modifying, or reviewing frontend web interfaces, dashboards, control panels, portals, or embedded WebUIs following the signature Tung Lam Design System (Dark/Light mode, Emerald/Cyan palette, glassmorphism, glow accents, and responsive layout shells).
---

# Tung Lam Web UI Design System & Frontend Skill

Standardized frontend design system and architectural guidelines for building industrial, sleek, and high-performance Web UIs across all projects.

## Core Visual Invariants

| Element | Specification | Rationale |
|---|---|---|
| **Default Theme** | Dark Mode (`color-scheme: dark; data-theme="dark"`) | Deep industrial look, reduces eye strain for control panels and engineering tools. |
| **Theme Toggle** | Full support for Light Mode via `data-theme="light"` | Flexible for diverse working environments and daylight operations. |
| **Signature Background** | Radial gradient with glow at top right (`radial-gradient(circle at 78% 8%, #153352 0, transparent 35%), #0d1525`) | Creates depth, warmth, and a high-tech ambient luminous atmosphere. |
| **Primary Accent** | **Emerald Green / Mint Jade** (`#34d399` / `#10b981` / `#047857`) | Signals healthy state, readiness, and modern energy. |
| **Identity / Focus Accent** | **Electric Cyan / Sky Blue** (`#39cdf8`) | Used for focus rings, selection states, active chips, and hardware identity. |
| **Multi-layer Glow** | `0 0 0 1px rgba(52,211,153,.78), 0 0 18px rgba(52,211,153,.28), 0 0 38px rgba(52,211,153,.13)` | Signature luminous lighting on focused inputs and active states. |
| **Zero Dependencies** | Pure Vanilla HTML5 + Modern CSS Variables + Vanilla ES6+ JS | Eliminates runtime overhead, 100% portable for embedded C strings (ESP32), Python gateways (Raspberry Pi), or modern SPAs. |

---

## Layout Archetypes

### 1. App Shell Layout (Dashboards / Multi-section Control Planes)
Used for main applications, multi-camera views, diagnostics, and warehouse systems.
* **Fixed/Collapsible Sidebar** (`width: 214px–220px`):
  * Top: Brand lockup with logo and company title.
  * Navigation: Group labels (`.navigation-group-label: 10px uppercase, letter-spacing: .08em`), action buttons with emerald hover/active tints.
  * Bottom: User status / quick toggle.
* **Header / Hero Section**:
  * Eyebrow tag: `.eyebrow { font-size: 11px; font-weight: 750; letter-spacing: .15em; text-transform: uppercase; color: #92a8e8; }`
  * Title `H1` + subtitle `.muted`.
  * Top right: Live System Status Bar (`.system-bar` or `.header-status`).
* **Content Viewport**: Responsive grid (`.layout`, `.grid-2`, `.grid-3`) with automatic single-column collapse on mobile (`<= 900px`).

### 2. Centered Card Shell Layout (Login / Portals / Single-purpose Wizards)
Used for authentication, single-board configuration portals, and local OTA update screens.
* Centered layout: `body { display: grid; place-items: center; min-height: 100vh; }`
* Card container: `width: min(420px, 100%)` or `width: min(680px, 100%)` for wizards.
* Self-contained within one screen with clear visual hierarchy.

---

## Signature Components

### 1. Status Chips & System Status Bar
Used for showing connectivity, hardware metrics, MQTT/CAN/WiFi status.
```html
<div class="status-chip ok">
  <i></i>
  <span>
    <small>MQTT</small>
    <b>ONLINE</b>
  </span>
</div>
```
* Status dot `i` with multi-layered glow: `box-shadow: 0 0 0 4px rgba(52, 211, 153, .12);`
* Variations: `.ok` (emerald), `.warn` (amber), `.bad` (coral red), `.identity` (cyan).

### 2. Multi-Step Wizard & Gradient Progress Bar
Used for firmwares, calibration, provisioning, and multi-step workflows.
* Steps 1-2-3 with circular counter, active blue-green border, and done state checkmarks.
* Progress Bar: `height: 10px; border-radius: 999px; background: linear-gradient(90deg, #8b7cf6, #39cdf8, #34d399);`

### 3. Native Modal Dialog System
Always use native `<dialog>` with backdrop blur:
```html
<dialog class="gw-modal" id="myModal">
  <div class="gw-modal-brand">
    <img src="/assets/logo.png" alt="Logo">
    <span>WAREHOUSE CONTROL</span>
  </div>
  <div class="gw-modal-content">
    <div class="gw-modal-icon">...</div>
    <div class="gw-modal-copy">
      <h2>Xác nhận</h2>
      <p>Nội dung thông báo rõ ràng.</p>
    </div>
  </div>
  <div class="gw-modal-actions">
    <button class="btn secondary" onclick="myModal.close()">Hủy</button>
    <button class="btn primary">Xác nhận</button>
  </div>
</dialog>
```

### 4. Interactive Form Fields & Controls
* Input height: `min-height: 44px–46px` for touch accessibility.
* Dark background (`--glass2: #111a2c` / `#0f172a`), subtle border (`#3b4b64`).
* On `:focus-visible`: Outline cyan or glow ring with smooth transition.
* Segmented control (`.segmented`), Custom switch toggle (`.switch-line`), Floating actions (`.actions`).

---

## Design Tokens Quick Reference

```css
:root {
  color-scheme: dark;
  --background: #0d1525;
  --background-glow: #153352;
  --surface: #172236;
  --surface-strong: #202d43;
  --surface-soft: #111a2c;
  --border: #3b4b64;
  --border-soft: #2d3b52;
  --text: #f8fafc;
  --muted: #a9b7ca;
  --accent: #34d399;
  --accent-strong: #047857;
  --accent-ink: #03261d;
  --cyan: #39cdf8;
  --warning: #fbbf24;
  --danger: #f87171;
  --violet: #8b7cf6;
  --radius: 12px;
  --radius-sm: 9px;
  --radius-pill: 999px;
  --shadow: 0 18px 45px rgba(2, 6, 23, .24);
  --glow-shadow: 0 0 0 1px rgba(52, 211, 153, .78), 0 0 18px rgba(52, 211, 153, .28), 0 0 38px rgba(52, 211, 153, .13);
}

:root[data-theme="light"] {
  color-scheme: light;
  --background: #f4f7fb;
  --background-glow: #dcebf7;
  --surface: #ffffff;
  --surface-strong: #edf2f8;
  --surface-soft: #f8fafc;
  --border: #a9b7c9;
  --border-soft: #d4dde8;
  --text: #172033;
  --muted: #50627a;
  --accent: #047857;
  --accent-strong: #065f46;
  --accent-ink: #ffffff;
  --cyan: #0284c7;
  --warning: #a16207;
  --danger: #b91c1c;
  --shadow: 0 14px 36px rgba(15, 23, 42, .1);
  --glow-shadow: 0 0 0 1px rgba(16, 185, 129, .62), 0 0 18px rgba(16, 185, 129, .2), 0 0 38px rgba(16, 185, 129, .09);
}
```

---

## Detailed References

* Read [design_tokens.css](references/design_tokens.css) for the complete CSS variable definitions.
* Read [boilerplate_template.html](references/boilerplate_template.html) for a full, self-contained starter page.
* Read [layouts.md](references/layouts.md) for detailed markup and responsive patterns.
* Inspect [components.html](references/components.html) for all copy-paste ready HTML components.
