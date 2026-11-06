// Progressive enhancement: the page works without JS (chips are anchor links).
// With JS, chips filter by category and the search box filters links.
(function () {
  "use strict";
  const q = document.getElementById("q");
  const chips = Array.from(document.querySelectorAll(".chip"));
  const cats = Array.from(document.querySelectorAll("section.cat"));
  const empty = document.getElementById("empty");
  let active = "all";

  // Cache each link's searchable text once.
  const rows = Array.from(document.querySelectorAll(".grid li")).map((li) => ({
    li,
    text: (li.textContent + " " + li.querySelector("a").href).toLowerCase(),
  }));

  function apply() {
    const term = q.value.trim().toLowerCase();
    let shown = 0;
    rows.forEach((r) => { r.li.hidden = term !== "" && !r.text.includes(term); });

    cats.forEach((sec) => {
      const inCat = active === "all" || sec.dataset.cat === active;
      let secCount = 0;
      sec.querySelectorAll(".sub").forEach((sub) => {
        const n = sub.querySelectorAll("li:not([hidden])").length;
        sub.hidden = n === 0;
        secCount += n;
      });
      sec.hidden = !inCat || secCount === 0;
      const badge = sec.querySelector("h2 .count");
      if (badge) badge.textContent = secCount;
      if (!sec.hidden) shown += secCount;
    });

    chips.forEach((c) => {
      const cat = c.dataset.cat;
      const n = cat === "all"
        ? cats.reduce((a, s) => a + s.querySelectorAll("li:not([hidden])").length, 0)
        : (document.querySelector(`section.cat[data-cat="${cat}"]`)?.querySelectorAll("li:not([hidden])").length ?? 0);
      c.querySelector("span").textContent = n;
      c.setAttribute("aria-current", String(cat === active));
    });
    empty.hidden = shown > 0;
  }

  chips.forEach((c) => c.addEventListener("click", (e) => {
    e.preventDefault();
    active = c.dataset.cat;
    apply();
    window.scrollTo({ top: 0 });
  }));
  q.addEventListener("input", apply);
  document.addEventListener("keydown", (e) => {
    if (e.key === "/" && document.activeElement !== q) { e.preventDefault(); q.focus(); }
    if (e.key === "Escape" && document.activeElement === q) { q.value = ""; apply(); }
  });
})();
