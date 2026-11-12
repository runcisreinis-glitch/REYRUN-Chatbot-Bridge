(() => {
  const key = 'reyrun-bridge-theme';
  const system = window.matchMedia('(prefers-color-scheme: dark)');
  let selected;
  let button;
  try { selected = localStorage.getItem(key); } catch {}
  function apply() {
    const dark = selected === 'dark' || (selected !== 'light' && system.matches);
    document.documentElement.dataset.theme = dark ? 'dark' : 'light';
    const bar = document.querySelector('meta[name="theme-color"]');
    if (bar) bar.content = dark ? '#091329' : '#adceef';
    if (button) {
      button.setAttribute('aria-pressed', String(dark));
      button.title = dark ? button.dataset.light : button.dataset.dark;
    }
  }
  apply();
  document.addEventListener('DOMContentLoaded', () => {
    button = document.querySelector('[data-theme-switch]');
    if (!button) return;
    apply();
    button.hidden = false;
    button.addEventListener('click', () => {
      selected = document.documentElement.dataset.theme === 'dark' ? 'light' : 'dark';
      try { localStorage.setItem(key, selected); } catch {}
      apply();
    });
  });
  system.addEventListener('change', apply);
  window.addEventListener('pageshow', () => {
    try { selected = localStorage.getItem(key); } catch {}
    apply();
  });
  window.addEventListener('storage', event => {
    if (event.key === key || event.key === null) {
      selected = event.newValue;
      apply();
    }
  });
})();
