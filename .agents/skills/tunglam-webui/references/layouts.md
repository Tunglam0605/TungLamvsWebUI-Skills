# Layout Patterns & Responsive Rules

## 1. App Shell (Sidebar Dashboard Layout)

### Structure
```html
<div class="app-shell">
  <!-- Fixed / Sticky Sidebar -->
  <aside class="sidebar">
    <div class="brand-block">
      <img src="/logo.png" class="brand-logo" alt="Logo">
      <strong>AUBOT SYSTEM</strong>
      <span>WAREHOUSE CONTROL</span>
    </div>

    <nav class="navigation">
      <span class="navigation-group-label">GIÁM SÁT</span>
      <button class="active"><i>📊</i> Tổng quan</button>
      <button><i>📦</i> Kho bãi</button>

      <span class="navigation-group-label">CẤU HÌNH</span>
      <button><i>⚡</i> Chẩn đoán</button>
      <button><i>🌐</i> Kết nối & Mạng</button>
      <button><i>🔄</i> Cập nhật OTA</button>
    </nav>

    <div class="sidebar-footer">
      <div class="user-box">
        <span class="dot ok"></span>
        <span>
          <small>QUẢN TRỊ VIÊN</small>
          <b>admin@aubot</b>
        </span>
      </div>
    </div>
  </aside>

  <!-- Main Viewport -->
  <main class="main-content">
    <header class="top-bar">
      <!-- Eyebrow + Breadcrumbs + Status Bar -->
    </header>

    <section class="content-body">
      <!-- Grid Cards & Modules -->
    </section>
  </main>
</div>
```

### CSS Layout Rules
* `--sidebar-width: 220px` (fixed on desktop, collapses to bottom bar or drawer on mobile `<= 768px`).
* `main-content`: `margin-left: var(--sidebar-width); width: calc(100% - var(--sidebar-width)); min-height: 100vh; padding: 24px;`
* Mobile Breakpoint (`@media (max-width: 768px)`):
  * Sidebar moves off-screen with hamburger trigger or transforms into a top navigation bar.
  * `main-content` takes full width `100%` with `padding: 16px`.

---

## 2. Centered Card Shell (Login & Single Portals)

### Structure
```html
<body class="centered-layout">
  <main class="card login-card">
    <div class="brand-lockup">
      <img src="/logo.png" class="logo" alt="Logo">
      <div class="eyebrow">AUBOT · GATEWAY PORTAL</div>
    </div>

    <h1>Đăng nhập</h1>
    <p class="muted">Nhập mã truy cập hoặc tài khoản quản trị.</p>

    <form class="form-grid">
      <label class="field">
        <span>Mật khẩu</span>
        <input type="password" required autofocus>
      </label>
      <button class="btn primary full-width" type="submit">Đăng nhập</button>
    </form>
  </main>
</body>
```

### CSS Layout Rules
* `body.centered-layout`: `min-height: 100vh; margin: 0; display: grid; place-items: center; padding: 20px;`
* `login-card`: `width: min(420px, 100%); background: var(--surface); border: 1px solid var(--border); border-radius: 16px; padding: 32px; box-shadow: var(--shadow-lg);`

---

## 3. Responsive Grid Systems
* **2-Column Layout (`.grid-2`)**:
  ```css
  .grid-2 {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 16px;
  }
  @media (max-width: 900px) {
    .grid-2 { grid-template-columns: 1fr; }
  }
  ```
* **3-Column Metric Cards (`.grid-3`)**:
  ```css
  .grid-3 {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 14px;
  }
  @media (max-width: 1024px) {
    .grid-3 { grid-template-columns: repeat(2, 1fr); }
  }
  @media (max-width: 640px) {
    .grid-3 { grid-template-columns: 1fr; }
  }
  ```
