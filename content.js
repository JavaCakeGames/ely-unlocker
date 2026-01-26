window._elyPreValidated = true;
Object.defineProperty(window, '_elyPreValidated', {
  value: true,
  writable: false,
  configurable: false
});

window.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('.premium-overlay').forEach(el => el.remove());
  if (typeof window.revealPrices === 'function') window.revealPrices();
});
