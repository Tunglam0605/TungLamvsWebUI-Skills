# Tung Lam Web UI — Design System & Agent Skill

Bộ chuẩn hoá **Thiết Kế Giao Diện Web (Web UI Design System)** & **Agent Skill** cá nhân hoá của **Tùng Lâm**, giúp đồng bộ phong cách thẩm mỹ công nghiệp, hiện đại, sắc nét và chuyên nghiệp cho tất cả các dự án web/nhúng (ESP32, Raspberry Pi, STM32, Dashboard, SaaS).

---

## 🌟 Đặc trưng thẩm mỹ cốt lõi (Core Visual Identity)

* 🌌 **Dark Mode Chiều Sâu**: Tone nền chủ đạo `--bg0: #0d1525` kết hợp hiệu ứng Luminous Glow góc trên phải `radial-gradient(circle at 78% 8%, #153352 0, transparent 35%)`.
* ☀️ **Chuyển đổi Light/Dark linh hoạt**: Đầy đủ biến số và tương thích mượt mà qua thuộc tính `data-theme="dark"` / `data-theme="light"`.
* 🟢 **Màu chủ đạo (Signature Accent)**: **Emerald Green / Mint Jade (`#34d399` / `#10b981`)** mang năng lượng hiện đại, biểu thị trạng thái sẵn sàng và chuẩn xác.
* 🔵 **Màu định danh & Focus**: **Electric Cyan (`#39cdf8`)** tạo điểm nhấn công nghệ cho viền active, chip hardware ID và focus rings.
* ✨ **Hệ thống Glow đa tầng**: Hiệu ứng phát sáng viền mềm mại đặc trưng:
  ```css
  --glow-shadow: 0 0 0 1px rgba(52,211,153,.78), 0 0 18px rgba(52,211,153,.28), 0 0 38px rgba(52,211,153,.13);
  ```
* ⚡ **Zero Dependency / 100% Thuần khiết**: Chỉ sử dụng **Vanilla HTML5 + Modern CSS Variables + Vanilla JS (ES6+)**, không tốn RAM, không cần node_modules/build pipeline cồng kềnh, chạy mượt trên chip nhúng ESP32 tới các hệ thống máy chủ.

---

## 📂 Cấu trúc Repository

```text
TungLamvsWebUI-Skills/
├── .agents/skills/tunglam-webui/          <-- Canonical Agent Skill
│   ├── SKILL.md                          <-- Quy chuẩn hướng dẫn dành riêng cho AI Agent
│   └── references/
│       ├── design_tokens.css             <-- Toàn bộ hệ thống biến CSS Design Tokens
│       ├── components.html               <-- Thư viện các component HTML copy-paste
│       ├── layouts.md                    <-- Hướng dẫn dựng bố cục Sidebar & Centered Cards
│       └── boilerplate_template.html     <-- Template HTML hoàn chỉnh sẵn sàng sử dụng
├── demo/                                 <-- Trang web demo tương tác thực tế
│   ├── index.html
│   ├── ui.css
│   └── ui.js
├── scripts/
│   └── generate_page.py                  <-- Tool CLI tạo nhanh trang mới theo chuẩn thiết kế
├── tests/
│   └── test_skill.py                     <-- Bộ kiểm thử tự động
├── install_skill.py                      <-- Script cài đặt skill vào môi trường AI toàn cục
└── README.md
```

---

## 🚀 Trải nghiệm Demo trực tiếp

Bạn có thể mở ngay file `demo/index.html` trong trình duyệt bất kỳ hoặc chạy local server:

```powershell
# Mở trực tiếp trên trình duyệt
Start-Process "demo\index.html"
```

---

## 🛠️ Hướng dẫn tích hợp & Sử dụng

### 1. Cài đặt Skill cho AI Agent (Antigravity / Gemini / Claude / Codex)

Chạy script cài đặt để đưa `tunglam-webui` vào thư mục skills toàn cục:

```powershell
python install_skill.py --force
```

Sau khi cài đặt, bạn chỉ cần ra lệnh cho AI trong bất kỳ dự án nào:
> *"Hãy áp dụng skill `tunglam-webui` để thiết kế giao diện cho trang này."*

### 2. Tạo nhanh một trang web mới bằng script

```powershell
python scripts/generate_page.py --output "my_dashboard.html" --title "Trang Giám Sát Kho" --app-name "AUBOT WAREHOUSE"
```

### 3. Chạy kiểm thử hệ thống

```powershell
python -m unittest discover -s tests -v
```

---

## 📜 Giấy phép (License)
Phát hành theo giấy phép [MIT License](LICENSE).
