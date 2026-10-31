(function () {
  var reduce = matchMedia('(prefers-reduced-motion: reduce)').matches, g = window.gsap;
  document.getElementById('yr').textContent = new Date().getFullYear();
  var bar = document.getElementById('lgBar');
  function prog() { var h = document.documentElement.scrollHeight - innerHeight; bar.style.transform = 'scaleX(' + (h > 0 ? scrollY / h : 0) + ')'; }
  addEventListener('scroll', prog, { passive: true }); prog();
  // pixel field
  var cv = document.getElementById('lgPixels'), ctx = cv.getContext('2d'), W, H, mx = -999, my = -999, dpr = Math.min(2, devicePixelRatio || 1);
  function size() { var r = cv.getBoundingClientRect(); W = r.width; H = r.height; cv.width = W * dpr; cv.height = H * dpr; ctx.setTransform(dpr, 0, 0, dpr, 0, 0); }
  size(); addEventListener('resize', size);
  cv.parentElement.addEventListener('mousemove', function (e) { var r = cv.getBoundingClientRect(); mx = e.clientX - r.left; my = e.clientY - r.top; });
  (function f(t) { ctx.clearRect(0, 0, W, H); for (var x = 11; x < W; x += 22) for (var y = 11; y < H; y += 22) { var n = Math.max(0, 1 - Math.hypot(x - mx, y - my) / 150), w = reduce ? 0 : (Math.sin(x * .012 + t * .0012) * Math.cos(y * .014 - t * .0009) + 1) / 2, s = 2 + n * 6; ctx.fillStyle = 'rgba(0,145,255,' + (.04 + w * .06 + n * .6) + ')'; ctx.fillRect(x - s / 2, y - s / 2, s, s); } if (!reduce) requestAnimationFrame(f); })(0);
  // active TOC
  var secs = [].slice.call(document.querySelectorAll('.lg-sec')), links = [].slice.call(document.querySelectorAll('.lg-toc a'));
  var io = new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting) { var id = e.target.id; secs.forEach(function (s) { s.classList.toggle('on', s.id === id); }); links.forEach(function (a) { a.classList.toggle('on', a.getAttribute('href') === '#' + id); }); } }); }, { rootMargin: '-40% 0px -55% 0px' });
  secs.forEach(function (s) { io.observe(s); });
  if (!g || reduce) return;
  g.registerPlugin(ScrollTrigger);
  g.from('.lg-title', { yPercent: 40, opacity: 0, duration: 1.1, ease: 'power4.out' });
  g.from('.lg-hero .kicker, .lg-hero .lead, .lg-meta span, .lg-mobile-tabs', { y: 20, opacity: 0, duration: .8, stagger: .08, delay: .2, ease: 'power3.out' });
  g.from('.lg-toc a', { x: -20, opacity: 0, duration: .6, stagger: .04, delay: .3, ease: 'power3.out' });
  ScrollTrigger.batch('.lg-sec', { start: 'top 88%', once: true, onEnter: function (els) { g.from(els, { y: 40, opacity: 0, duration: .8, stagger: .08, ease: 'power3.out', clearProps: 'all' }); } });
})();
