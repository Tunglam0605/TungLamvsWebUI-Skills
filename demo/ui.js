/**
 * Tung Lam Web UI — Interactive Demo Controller
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
}
