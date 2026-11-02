(function () {
  var root = document.documentElement;
  var systemTheme = window.matchMedia('(prefers-color-scheme: dark)');
  var preference = null;

  try {
    preference = localStorage.getItem('theme');
  } catch (error) {
    // Theme switching still works when browser storage is unavailable.
  }
  if (preference !== 'light' && preference !== 'dark') preference = null;

  function applyTheme() {
    var dark = preference ? preference === 'dark' : systemTheme.matches;
    root.dataset.theme = dark ? 'dark' : 'light';
    var button = document.querySelector('.theme-toggle');
    if (button) button.setAttribute('aria-pressed', String(dark));
  }

  applyTheme();
  systemTheme.addEventListener('change', applyTheme);

  document.addEventListener('DOMContentLoaded', function () {
    var button = document.querySelector('.theme-toggle');
    if (!button) return;
    applyTheme();
    button.hidden = false;
    button.addEventListener('click', function () {
      preference = root.dataset.theme === 'dark' ? 'light' : 'dark';
      applyTheme();
      try {
        localStorage.setItem('theme', preference);
      } catch (error) {
        // Keep the selected theme for this page even without storage.
      }
    });
  });
})();
