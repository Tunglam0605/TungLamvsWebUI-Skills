/**
 * Tung Lam Web UI — Interactive Demo Controller & Component Scripts
 */

function toggleTheme() {
  const root = document.documentElement;
  const current = root.getAttribute('data-theme') || 'dark';
  const next = current === 'dark' ? 'light' : 'dark';
  root.setAttribute('data-theme', next);
  const btn = document.getElementById('themeToggleBtn');
  if (btn) {
    btn.textContent = next === 'dark' ? '☀️ Giao diện Sáng' : '🌙 Giao diện Tối';
  }
  showToast(next === 'dark' ? 'Đã bật chế độ Dark Mode' : 'Đã bật chế độ Light Mode', 'info');
}

function openMobileDrawer() {
  const sidebar = document.querySelector('.sidebar');
  const backdrop = document.querySelector('.drawer-backdrop');
  if (sidebar) sidebar.classList.add('drawer-open');
  if (backdrop) backdrop.classList.add('active');
}

function closeMobileDrawer() {
  const sidebar = document.querySelector('.sidebar');
  const backdrop = document.querySelector('.drawer-backdrop');
  if (sidebar) sidebar.classList.remove('drawer-open');
  if (backdrop) backdrop.classList.remove('active');
}

function openConfirmModal() {
  const modal = document.getElementById('demoModal');
  if (modal) modal.showModal();
}

function closeConfirmModal() {
  const modal = document.getElementById('demoModal');
  if (modal) modal.close();
}

let currentStep = 1;
function setStep(step) {
  currentStep = step;
  for (let i = 1; i <= 3; i++) {
    const el = document.getElementById(`step${i}`);
    if (!el) continue;
    el.classList.toggle('active', i === step);
    el.classList.toggle('done', i < step);
  }
  const pct = step === 1 ? 25 : step === 2 ? 65 : 100;
  const bar = document.getElementById('demoProgressBar');
  const label = document.getElementById('demoProgressPct');
  if (bar) bar.style.width = `${pct}%`;
  if (label) label.textContent = `${pct}%`;
}

function setSegmented(btn, value) {
  const parent = btn.parentElement;
  if (!parent) return;
  parent.querySelectorAll('button').forEach(b => b.classList.remove('active'));
  btn.classList.add('active');
  showToast(`Đã chuyển sang chế độ: ${btn.textContent}`, 'info');
}

/* Toast Notifications */
function showToast(message, type = 'info') {
  let container = document.querySelector('.toast-container');
  if (!container) {
    container = document.createElement('div');
    container.className = 'toast-container';
    document.body.appendChild(container);
  }

  const toast = document.createElement('div');
  toast.className = `toast ${type}`;
  toast.textContent = message;
  container.appendChild(toast);

  setTimeout(() => {
    toast.style.opacity = '0';
    toast.style.transform = 'translateY(10px)';
    setTimeout(() => toast.remove(), 200);
  }, 3500);
}

/* File Upload Simulation */
document.addEventListener('DOMContentLoaded', () => {
  const fileInput = document.getElementById('demoFileInput');
  if (fileInput) {
    fileInput.addEventListener('change', (e) => {
      const file = e.target.files[0];
      if (file) {
        document.getElementById('fileName').textContent = file.name;
        const sizeKb = (file.size / 1024).toFixed(1);
        document.getElementById('fileSize').textContent = `${sizeKb} KiB · Sẵn sàng tải lên`;
        showToast(`Đã chọn firmware: ${file.name} (${sizeKb} KiB)`, 'success');
        setStep(2);
      }
    });
  }

  /* Log Stream Auto Simulation */
  const consoleEl = document.getElementById('logConsole');
  const simulatedLogs = [
    { type: 'info', tag: 'CAN', msg: 'RX ID=0x181 DATA=[01 24 FF 00 00 00 00 12]' },
    { type: 'info', tag: 'UART', msg: 'Heartbeat ping ACK from STM32 (BKP1R=0x00, BKP4R=0x53544C4B)' },
    { type: 'warn', tag: 'WIFI', msg: 'RSSI signal dropped to -74dBm' },
    { type: 'success', tag: 'SYS', msg: 'Telemetry sync completed successfully' },
    { type: 'info', tag: 'MQTT', msg: 'Published telemetry to /device/telemetry/status' }
  ];

  let logIdx = 0;
  setInterval(() => {
    if (!consoleEl) return;
    const now = new Date();
    const timeStr = `[${String(now.getHours()).padStart(2, '0')}:${String(now.getMinutes()).padStart(2, '0')}:${String(now.getSeconds()).padStart(2, '0')}]`;
    const item = simulatedLogs[logIdx % simulatedLogs.length];
    logIdx++;

    const row = document.createElement('div');
    row.className = `log-entry ${item.type}`;
    row.innerHTML = `<span class="log-time">${timeStr}</span> <span class="log-tag">[${item.tag}]</span> ${item.msg}`;
    consoleEl.appendChild(row);

    if (consoleEl.children.length > 30) {
      consoleEl.removeChild(consoleEl.firstChild);
    }
    consoleEl.scrollTop = consoleEl.scrollHeight;
  }, 4000);
});
