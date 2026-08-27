# Tung Lam Web UI — Design System & Universal Agent Skill

Bộ chuẩn hoá **Thiết Kế Giao Diện Web (Web UI Design System)** & **Agent Skill Toàn Năng** cá nhân hoá của **Tùng Lâm**, giúp đồng bộ phong cách thẩm mỹ công nghiệp, sắc nét, chuyển động mượt mà và chuyên nghiệp cho tất cả các dự án web/nhúng (ESP32, Raspberry Pi, STM32, AprilTag, Dashboard, IoT Control Plane).

---

## 🌟 Đặc trưng thẩm mỹ cốt lõi (Core Visual Identity)

* 🌌 **Dark Mode Chiều Sâu**: Tone nền chủ đạo `--bg0: #0d1525` kết hợp hiệu ứng Luminous Glow góc trên phải `radial-gradient(circle at 78% 8%, #153352 0, transparent 35%)`.
* ☀️ **Chuyển đổi Light/Dark linh hoạt**: Đầy đủ biến số và tương thích mượt mà qua thuộc tính `data-theme="dark"` / `data-theme="light"`.
* 🟢 **Màu chủ đạo (Signature Accent)**: **Emerald Green / Mint Jade (`#34d399` / `#10b981`)** mang năng lượng công nghệ hiện đại, biểu thị trạng thái sẵn sàng và chuẩn xác.
* 🔵 **Màu định danh & Focus**: **Electric Cyan (`#39cdf8`)** tạo điểm nhấn cho viền active, chip hardware ID và focus rings.
* 🪶 **Hiệu ứng Nâng Thẻ & Phát Sáng Khi Rê Chuột (Lifting Hover Motion)**:
  * Mọi ô thông số (`.stat-card`), nút bấm (`.btn`), hàng bảng (`.table tr`), khối sidebar (`.sidebar-info`, `.user-badge`) khi trỏ chuột vào đều **nổi nhẹ lên trên** (`transform: translateY(-3px)`) và **tỏa quầng sáng ngọc bích** (`box-shadow: 0 8px 25px rgba(16,185,129,0.18)`).
* ✨ **Hệ thống Glow đa tầng (Signature Multi-layer Glow)**:
  ```css
  --glow-shadow: 0 0 0 1px rgba(52,211,153,.78), 0 0 18px rgba(52,211,153,.28), 0 0 38px rgba(52,211,153,.13);
  ```
* ⚡ **Zero Dependency / 100% Thuần khiết**: Chỉ sử dụng **Vanilla HTML5 + Modern CSS Variables + Vanilla JS (ES6+)**, không tốn RAM, không cần node_modules cồng kềnh, chạy mượt từ chip nhúng ESP32 tới các hệ thống máy chủ.

---

## 📂 Cấu trúc Repository

```text
TungLamvsWebUI-Skills/
├── .agents/skills/tunglam-webui/          <-- Canonical Agent Skill
│   ├── SKILL.md                          <-- Bộ quy tắc và Invariants bắt buộc cho AI Agent
│   └── references/
│       ├── design_tokens.css             <-- Toàn bộ hệ thống biến CSS Design Tokens
│       ├── components.html               <-- Thư viện đầy đủ component HTML copy-paste
│       ├── layouts.md                    <-- Hướng dẫn dựng bố cục Sidebar & Centered Cards
│       └── boilerplate_template.html     <-- Template HTML hoàn chỉnh sẵn sàng sử dụng
├── demo/                                 <-- Trang web demo tương tác toàn diện
│   ├── index.html                        <-- Showcase đầy đủ Stat cards, Table, Log stream, OTA, IO
│   ├── ui.css                            <-- Stylesheet chuẩn
│   └── ui.js                             <-- Controller điều khiển (Theme, Toasts, Stream, Modal)
├── scripts/
│   ├── generate_page.py                  <-- Tool CLI tạo nhanh trang mới theo chuẩn
│   └── export_c_header.py                <-- Tool nén & xuất HTML/CSS sang file C/C++ header (.h) cho ESP32
├── tests/
│   └── test_skill.py                     <-- Bộ kiểm thử tự động
├── install_skill.py                      <-- Script cài đặt skill vào môi trường AI toàn cục
└── README.md
```

---

## 🧩 Danh mục Linh kiện (Component Catalogue)

1. **Interactive Stat Cards (`.stat-card`)**: Ô thông số nổi bật có hiệu ứng bay nhẹ khi hover, hiển thị xu hướng tăng/giảm và đơn vị.
2. **Data Tables (`.table`, `.table-container`)**: Bảng danh sách thiết bị có sticky header, cột monospace cho IP/MAC, badge trạng thái và nút hành động.
3. **Terminal & Log Console (`.log-console`)**: Hộp xem nhật ký UART/CAN/WebSocket phong cách terminal nền đen sâu, font monospace, autoscroll dính đáy và tag màu.
4. **Drag & Drop Firmware Uploader (`.filepick`)**: Khung kéo thả file firmware OTA `.bin` / `.hex`.
5. **Multi-Step Wizard & Gradient Bar (`.steps`, `.bar`)**: Thanh tiến trình 3 bước với dải gradient `violet -> cyan -> emerald`.
6. **I/O Sensor & Hardware Matrix (`.io-group`, `.io-chips`)**: Ma trận trạng thái nút bấm, cảm biến, relay có đèn LED phát sáng 3 màu.
7. **Native Modal Dialog (`<dialog class="gw-modal">`)**: Hộp thoại popup làm mờ nền sau (`backdrop-filter: blur(7px)`), hỗ trợ bẫy phím Tab và phím Esc.
8. **Toast Notifications (`showToast(msg, type)`)**: Thông báo nổi góc phải màn hình cho các phản hồi tức thì.

---

## 🚀 Trải nghiệm Demo trực tiếp

Bạn có thể mở ngay file `demo/index.html` trong trình duyệt bất kỳ:

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

### 2. Xuất Web UI sang file Header C/C++ cho ESP32 / ESP-IDF

```powershell
python scripts/export_c_header.py --html "demo/index.html" --css "demo/ui.css" --js "demo/ui.js" --output "ui_assets.h"
```

### 3. Tạo nhanh một trang web mới

```powershell
python scripts/generate_page.py --output "my_dashboard.html" --title "Trang Giám Sát Kho" --app-name "TUNGLAM CONTROL"
```

### 4. Chạy kiểm thử tự động

```powershell
python -m unittest discover -s tests -v
```

---

## 📜 Giấy phép (License)
Phát hành theo giấy phép [MIT License](LICENSE).
