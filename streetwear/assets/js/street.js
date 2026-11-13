// KADHAR Street — menu, colour + size pickers, preview-only drop form.
(function () {
  var btn = document.querySelector('.menu-btn'), drawer = document.getElementById('drawer');
  if (btn && drawer) {
    var toggle = function (open) {
      drawer.classList.toggle('open', open);
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
      btn.textContent = open ? 'Close' : 'Menu';
    };
    btn.addEventListener('click', function () { toggle(!drawer.classList.contains('open')); });
    drawer.addEventListener('click', function (e) { if (e.target.closest('a')) toggle(false); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && drawer.classList.contains('open')) { toggle(false); btn.focus(); } });
  }
  document.querySelectorAll('.swatches').forEach(function (set) {
    var legend = set.querySelector('[data-colour-name]');
    set.addEventListener('click', function (e) {
      var sw = e.target.closest('.swatch'); if (!sw) return;
      set.querySelectorAll('.swatch').forEach(function (o) { o.setAttribute('aria-pressed', 'false'); });
      sw.setAttribute('aria-pressed', 'true'); if (legend) legend.textContent = sw.dataset.name;
    });
  });
  document.querySelectorAll('.sizes').forEach(function (g) {
    g.addEventListener('click', function (e) {
      var s = e.target.closest('.size'); if (!s) return;
      g.querySelectorAll('.size').forEach(function (o) { o.setAttribute('aria-pressed', 'false'); });
      s.setAttribute('aria-pressed', 'true');
    });
  });
  document.querySelectorAll('form[data-preview]').forEach(function (f) {
    f.addEventListener('submit', function (e) {
      e.preventDefault();
      var input = f.querySelector('input');
      if (!input.checkValidity()) { input.setAttribute('aria-invalid', 'true'); input.focus(); return; }
      var note = f.parentNode.querySelector('[data-note]');
      if (note) { note.hidden = false; note.focus(); }
    });
  });
})();
