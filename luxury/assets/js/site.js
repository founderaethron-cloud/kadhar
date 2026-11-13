// KADHAR site — small progressive enhancements. Everything works without JS except these toggles.
(function () {
  // Mobile menu
  var btn = document.querySelector('.menu-btn');
  var drawer = document.getElementById('drawer');
  if (btn && drawer) {
    btn.addEventListener('click', function () {
      var open = drawer.classList.toggle('open');
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
      btn.textContent = open ? 'Close' : 'Menu';
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && drawer.classList.contains('open')) { btn.click(); btn.focus(); }
    });
  }

  // Colourway picker
  document.querySelectorAll('.kd-swatches').forEach(function (set) {
    var legend = set.querySelector('[data-colour-name]');
    set.querySelectorAll('.kd-swatch').forEach(function (sw) {
      sw.addEventListener('click', function () {
        set.querySelectorAll('.kd-swatch').forEach(function (o) { o.setAttribute('aria-pressed', 'false'); });
        sw.setAttribute('aria-pressed', 'true');
        if (legend) legend.textContent = sw.dataset.name;
      });
    });
  });

  // Collection filters
  var filters = document.querySelector('.filters');
  if (filters) {
    filters.addEventListener('click', function (e) {
      var b = e.target.closest('button'); if (!b) return;
      filters.querySelectorAll('button').forEach(function (o) { o.setAttribute('aria-pressed', 'false'); });
      b.setAttribute('aria-pressed', 'true');
      var f = b.dataset.filter;
      document.querySelectorAll('[data-cat]').forEach(function (c) {
        c.hidden = !(f === 'all' || c.dataset.cat.split(' ').indexOf(f) > -1);
      });
    });
  }

  // Forms are not connected to a backend yet: show an honest preview notice.
  document.querySelectorAll('form[data-preview]').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var ok = true;
      form.querySelectorAll('[required]').forEach(function (input) {
        var field = input.closest('.kd-field');
        var valid = input.checkValidity();
        if (field) field.classList.toggle('kd-field--error', !valid);
        input.setAttribute('aria-invalid', valid ? 'false' : 'true');
        if (!valid && ok) { input.focus(); ok = false; }
      });
      var note = form.querySelector('.notice');
      if (ok && note) { note.hidden = false; note.focus(); }
      if (ok && !note) { var b = form.querySelector('button'); if (b) b.textContent = 'Preview only'; }
    });
  });

  // Pre-select garment on the atelier form from ?garment=
  var sel = document.getElementById('garment');
  if (sel) {
    var m = /^#garment-(\d{2})$/.exec(location.hash); var g = m && m[1];
    if (g) { for (var i = 0; i < sel.options.length; i++) if (sel.options[i].value === g) sel.selectedIndex = i; }
  }
})();
