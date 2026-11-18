// Light/dark theme. Loaded in <head> without defer so the saved theme is applied
// before first paint (the CSP blocks inline scripts, so this lives in its own file).
// No saved choice = follow the OS setting. Without JS, CSS falls back to the OS setting.
(function () {
  "use strict";
  const KEY = "theme";
  const root = document.documentElement;
  const media = window.matchMedia("(prefers-color-scheme: dark)");

  function saved() {
    try {
      const t = localStorage.getItem(KEY);
      return t === "light" || t === "dark" ? t : null;
    } catch (e) { return null; }
  }
  const current = () => saved() || (media.matches ? "dark" : "light");

  function render() {
    const theme = current();
    root.dataset.theme = theme;
    const btn = document.getElementById("theme-toggle");
    if (btn) {
      const next = theme === "dark" ? "light" : "dark";
      btn.setAttribute("aria-label", `Switch to ${next} mode`);
      btn.title = `Switch to ${next} mode`;
    }
  }

  render();
  media.addEventListener("change", () => { if (!saved()) render(); });

  document.addEventListener("DOMContentLoaded", () => {
    const btn = document.getElementById("theme-toggle");
    if (!btn) return;
    btn.hidden = false;
    btn.addEventListener("click", () => {
      const next = current() === "dark" ? "light" : "dark";
      try { localStorage.setItem(KEY, next); } catch (e) { /* private mode: still switch for this visit */ }
      root.dataset.theme = next;
      render();
    });
    render();
  });
})();
