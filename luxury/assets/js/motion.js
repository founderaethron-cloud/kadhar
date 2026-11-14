// KADHAR motion — runs only on pages with <body data-motion="...">.
// Reveals are added only to elements that start below the fold, so nothing visible is ever hidden,
// and with JS off or reduced motion on, every element stays in its normal visible state.
(function () {
  var mode = document.body.getAttribute('data-motion');
  if (!mode) return;
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var hasIO = 'IntersectionObserver' in window;

  // Pause the hero light loop when it is off screen.
  var weave = document.querySelector('.weave');
  if (weave && hasIO) {
    new IntersectionObserver(function (entries) {
      entries.forEach(function (e) { weave.classList.toggle('is-paused', !e.isIntersecting); });
    }).observe(weave);
  }

  if (reduce || !hasIO) return;

  var fold = window.innerHeight * 0.95;
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (e.isIntersecting) { e.target.classList.add('kd-in'); io.unobserve(e.target); }
    });
  }, { rootMargin: '0px 0px -8% 0px', threshold: 0.12 });

  function prep(list, cls, stagger) {
    Array.prototype.forEach.call(list, function (el, i) {
      if (el.getBoundingClientRect().top < fold) return; // already on screen: leave as is
      el.classList.add(cls);
      if (stagger) el.style.transitionDelay = (i * stagger) + 'ms';
      io.observe(el);
    });
  }

  if (mode === 'home') {
    prep(document.querySelectorAll('.grid-4 .kd-card'), 'kd-rv', 80);          // the collection, one after another
    prep(document.querySelectorAll('.kd-manifesto blockquote, .kd-manifesto cite'), 'kd-fade', 0);
    prep(document.querySelectorAll('.split__media'), 'kd-settle', 0);          // images settle: "slow by design"
    prep(document.querySelectorAll('.steps .step'), 'kd-rv', 120);             // Basement → Indigo Passage → Flagship, in order
  }
  if (mode === 'garment') {
    prep(document.querySelectorAll('.garment__media > :not(:first-child)'), 'kd-rv', 0);
  }

  // Zoom on hover to inspect the weave: mouse/trackpad only.
  if (window.matchMedia('(hover: hover) and (pointer: fine)').matches) {
    document.querySelectorAll('.kd-zoom').forEach(function (z) {
      var img = z.querySelector('img');
      if (!img) return;
      z.classList.add('is-zoomable');
      z.addEventListener('pointerenter', function () { z.classList.add('is-zooming'); });
      z.addEventListener('pointerleave', function () { z.classList.remove('is-zooming'); });
      z.addEventListener('pointermove', function (e) {
        var r = z.getBoundingClientRect();
        img.style.transformOrigin = ((e.clientX - r.left) / r.width * 100).toFixed(1) + '% ' +
                                    ((e.clientY - r.top) / r.height * 100).toFixed(1) + '%';
      });
    });
  }
})();
