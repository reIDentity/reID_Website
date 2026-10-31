/* reID — reidentity.net · motion + interactions (GSAP + ScrollTrigger + Lenis) */
(function () {
  'use strict';
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  var fine = window.matchMedia && matchMedia('(hover: hover) and (pointer: fine)').matches;
  var hasG = typeof window.gsap !== 'undefined';
  var desk = function () { return window.innerWidth > 900; };
  if (hasG && window.ScrollTrigger) gsap.registerPlugin(ScrollTrigger);

  function toast(m) { var t = $('#toast'); t.textContent = m; t.classList.add('on'); clearTimeout(t._h); t._h = setTimeout(function () { t.classList.remove('on'); }, 2600); }
  function fmt(n, d) { return n.toLocaleString('en-US', { minimumFractionDigits: d, maximumFractionDigits: d }); }
  function countUp(el, to, dur, dec) {
    if (reduce || !hasG) { el.textContent = fmt(to, dec || 0); return; }
    var o = { v: 0 }; gsap.to(o, { v: to, duration: dur || 1.4, ease: 'power3.out', onUpdate: function () { el.textContent = fmt(o.v, dec || 0); } });
  }

  /* ---------- smooth scroll ---------- */
  var lenis = null;
  if (!reduce && window.Lenis && hasG) {
    lenis = new Lenis({ duration: 1.15, smoothWheel: true });
    lenis.on('scroll', ScrollTrigger.update);
    gsap.ticker.add(function (t) { lenis.raf(t * 1000); });
    gsap.ticker.lagSmoothing(0);
  }
  $$('a[href^="#"]').forEach(function (a) {
    a.addEventListener('click', function (e) {
      var id = a.getAttribute('href'); if (id.length < 2) return;
      var el = document.querySelector(id); if (!el) return;
      e.preventDefault(); closeMenu();
      if (lenis) lenis.scrollTo(el, { offset: -70 }); else el.scrollIntoView({ behavior: reduce ? 'auto' : 'smooth' });
    });
  });

  /* ---------- menu ---------- */
  var burger = $('#burger'), menu = $('#menu');
  function closeMenu() { menu.classList.remove('open'); burger.setAttribute('aria-expanded', 'false'); if (lenis) lenis.start(); }
  burger.addEventListener('click', function () { var o = menu.classList.toggle('open'); burger.setAttribute('aria-expanded', o); if (lenis) o ? lenis.stop() : lenis.start(); });

  /* ---------- nav state ---------- */
  var nav = $('#nav'), lastY = 0;
  function onScroll() {
    var y = window.scrollY;
    nav.classList.toggle('solid', y > 40);
    nav.classList.toggle('hide', y > 600 && y > lastY && !menu.classList.contains('open'));
    lastY = y;
  }
  window.addEventListener('scroll', onScroll, { passive: true }); onScroll();
  var navLinks = $$('.links a');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting) navLinks.forEach(function (a) { a.classList.toggle('on', a.getAttribute('href') === '#' + e.target.id); }); }); }, { rootMargin: '-45% 0px -50% 0px' });
    ['personal', 'virtual-id', 'cashback', 'legacy', 'chat', 'sso', 'corporate', 'ambassador'].forEach(function (id) { var el = document.getElementById(id); if (el) io.observe(el); });
  }

  /* ---------- cursor + magnets ---------- */
  if (fine && !reduce && hasG) {
    document.documentElement.classList.add('has-cursor');
    var cur = $('#cursor'), qx = gsap.quickTo(cur, 'x', { duration: .25, ease: 'power3' }), qy = gsap.quickTo(cur, 'y', { duration: .25, ease: 'power3' });
    window.addEventListener('mousemove', function (e) { qx(e.clientX); qy(e.clientY); });
    $$('a,button,.case,.pw').forEach(function (el) { el.addEventListener('mouseenter', function () { cur.classList.add('big'); }); el.addEventListener('mouseleave', function () { cur.classList.remove('big'); }); });
    $$('.magnet').forEach(function (b) {
      b.addEventListener('mousemove', function (e) { var r = b.getBoundingClientRect(); gsap.to(b, { x: (e.clientX - r.left - r.width / 2) * .25, y: (e.clientY - r.top - r.height / 2) * .35, duration: .4 }); });
      b.addEventListener('mouseleave', function () { gsap.to(b, { x: 0, y: 0, duration: .6, ease: 'elastic.out(1,.4)' }); });
    });
  }

  /* ---------- hero pixel field ---------- */
  (function () {
    var cv = $('#pixels'); if (!cv) return; var ctx = cv.getContext('2d'), W, H, S = 22, mx = -999, my = -999, dpr = Math.min(2, window.devicePixelRatio || 1);
    function size() { var r = cv.getBoundingClientRect(); W = r.width; H = r.height; cv.width = W * dpr; cv.height = H * dpr; ctx.setTransform(dpr, 0, 0, dpr, 0, 0); }
    size(); window.addEventListener('resize', size);
    $('#hero').addEventListener('mousemove', function (e) { var r = cv.getBoundingClientRect(); mx = e.clientX - r.left; my = e.clientY - r.top; });
    $('#hero').addEventListener('mouseleave', function () { mx = my = -999; });
    var vis = true; if ('IntersectionObserver' in window) new IntersectionObserver(function (e) { vis = e[0].isIntersecting; }).observe(cv);
    function frame(t) {
      if (vis) {
        ctx.clearRect(0, 0, W, H);
        for (var x = S / 2; x < W; x += S) for (var y = S / 2; y < H; y += S) {
          var d = Math.hypot(x - mx, y - my), near = Math.max(0, 1 - d / 160);
          var wave = reduce ? 0 : (Math.sin(x * .012 + t * .0012) * Math.cos(y * .014 - t * .0009) + 1) / 2;
          var a = .05 + wave * .07 + near * .75, s = 2 + near * 7;
          ctx.fillStyle = 'rgba(0,145,255,' + a + ')'; ctx.fillRect(x - s / 2, y - s / 2, s, s);
        }
      }
      if (!reduce) requestAnimationFrame(frame);
    }
    requestAnimationFrame(frame);
  })();

  /* ---------- hero art parallax (mouse) ---------- */
  var art = $('#heroArt');
  if (art && fine && hasG && !reduce) {
    art.addEventListener('mousemove', function (e) {
      var r = art.getBoundingClientRect(), px = (e.clientX - r.left) / r.width - .5, py = (e.clientY - r.top) / r.height - .5;
      $$('.chip', art).forEach(function (c) { var d = +c.dataset.depth || 20; gsap.to(c, { x: px * d, y: py * d, duration: .8, ease: 'power3' }); });
      gsap.to($('.paint', art), { x: px * -18, y: py * -18, duration: 1.2, ease: 'power3' });
    });
  }

  /* ---------- loader + intro ---------- */
  var loader = $('#loader');
  function intro() {
    if (!hasG || reduce) return;
    var tl = gsap.timeline();
    tl.from('.h-line', { yPercent: 110, duration: 1.1, stagger: .12, ease: 'power4.out' })
      .from('.h-in', { y: 24, opacity: 0, duration: .8, stagger: .08, ease: 'power3.out' }, '-=.7')
      .from('#heroArt', { clipPath: 'inset(8% 8% 8% 8% round 32px)', duration: 1.3, ease: 'power4.inOut' }, 0)
      .from('#heroArt .paint', { scale: 1.3, duration: 1.8, ease: 'power3.out' }, 0)
      .from('#heroArt .scan .c', { scale: 0, opacity: 0, duration: .6, stagger: .08, ease: 'back.out(2)' }, .6)
      .from('#heroArt .chip', { y: 40, opacity: 0, scale: .9, duration: .8, stagger: .14, ease: 'back.out(1.6)' }, .9);
    $$('.hero-meta [data-count]').forEach(function (b) { countUp(b, +b.dataset.count, 1.6); });
  }
  if (loader && hasG && !reduce) {
    var parts = $$('#loaderLogo rect, #loaderLogo path');
    var lt = gsap.timeline({ onComplete: function () { loader.classList.add('gone'); intro(); } });
    lt.from(parts, { x: function () { return gsap.utils.random(-60, 60); }, y: function () { return gsap.utils.random(-40, 40); }, rotation: function () { return gsap.utils.random(-90, 90); }, opacity: 0, transformOrigin: 'center', duration: .9, stagger: .025, ease: 'power3.out' })
      .to('#loaderBar', { scaleX: 1, duration: 1.1, ease: 'power2.inOut' }, 0)
      .to(loader, { yPercent: -100, duration: .8, ease: 'power4.inOut' }, '+=.15');
    setTimeout(function () { if (!loader.classList.contains('gone')) { loader.classList.add('gone'); } }, 4500);
  } else if (loader) { loader.classList.add('gone'); }

  if (!hasG || !window.ScrollTrigger) { fallbacks(); return; }

  /* ---------- split headings ---------- */
  $$('h2.splt').forEach(function (h) {
    if (h.dataset.done) return; h.dataset.done = 1;
    var words = h.innerHTML.trim().split(/\s+/);
    h.innerHTML = words.map(function (w) { return '<span class="line-mask" style="display:inline-block;vertical-align:top"><span style="display:inline-block">' + w + '</span></span>'; }).join(' ');
    if (reduce) return;
    gsap.from($$('.line-mask>span', h), { yPercent: 105, duration: 1, stagger: .045, ease: 'power4.out', scrollTrigger: { trigger: h, start: 'top 85%' } });
  });

  if (reduce) { fallbacks(); return; }

  /* ---------- generic reveals ---------- */
  ScrollTrigger.batch('.tile, .step, .check, .cb-cards>div, .vid-feats>div, .eco-list a, details, .reach>div, .ch, .feat-list>div, .qrb', {
    start: 'top 88%', once: true,
    onEnter: function (els) { gsap.from(els, { y: 50, opacity: 0, duration: .9, stagger: .07, ease: 'power3.out', clearProps: 'transform,opacity' }); }
  });
  $$('.lead').forEach(function (p) { if (p.closest('.hero')) return; gsap.from(p, { y: 24, opacity: 0, duration: 1, ease: 'power3.out', scrollTrigger: { trigger: p, start: 'top 90%' } }); });
  $$('.kicker').forEach(function (k) { gsap.from(k, { x: -20, opacity: 0, duration: .8, ease: 'power3.out', scrollTrigger: { trigger: k, start: 'top 92%' } }); });

  /* ---------- hero scroll-out ---------- */
  gsap.to('#heroArt .paint', { yPercent: 12, scale: 1.08, ease: 'none', scrollTrigger: { trigger: '#hero', start: 'top top', end: 'bottom top', scrub: true } });
  gsap.to('.hero-l', { yPercent: -18, opacity: .2, ease: 'none', scrollTrigger: { trigger: '#hero', start: 'top top', end: 'bottom top', scrub: true } });

  /* ---------- marquees (velocity aware) ---------- */
  $$('.mq-t').forEach(function (t) {
    t.innerHTML += t.innerHTML;
    var dir = +t.dataset.dir || -1;
    var tw = gsap.fromTo(t, { xPercent: dir < 0 ? 0 : -50 }, { xPercent: dir < 0 ? -50 : 0, duration: 38, ease: 'none', repeat: -1 });
    ScrollTrigger.create({ trigger: t, start: 'top bottom', end: 'bottom top', onUpdate: function (s) { var v = Math.min(4, 1 + Math.abs(s.getVelocity()) / 600); gsap.to(tw, { timeScale: v, duration: .2, overwrite: true, onComplete: function () { gsap.to(tw, { timeScale: 1, duration: 1 }); } }); } });
  });

  var mm = gsap.matchMedia();


  /* ---------- everything in one passport ---------- */
  mm.add('(min-width: 0px)', function () {
    var st = $('#evrStage');
    gsap.from('#evrPhone', { y: 160, rotationX: 30, rotation: -6, opacity: 0, ease: 'power3.out', scrollTrigger: { trigger: st, start: 'top 90%', end: 'top 30%', scrub: 1 } });
    gsap.from('#evrPhone .ep-t, #evrPhone .ep-corp, #evrPhone .ep-logo', { y: 30, opacity: 0, scale: .9, stagger: .08, duration: .7, ease: 'back.out(1.6)', scrollTrigger: { trigger: st, start: 'top 55%' } });
    var from = { '.fc-wallet': [-260, -120, -14], '.fc-fiat': [-320, 80, 10], '.fc-cards': [320, -100, 18], '.fc-sim': [260, 200, -20], '.fc-contact': [-280, 260, -12], '.fc-chat': [300, -220, 12] };
    Object.keys(from).forEach(function (sel) { var f = from[sel]; gsap.from(st.querySelector(sel), { x: f[0], y: f[1], rotation: f[2], opacity: 0, scale: .7, ease: 'power3.out', scrollTrigger: { trigger: st, start: 'top 80%', end: 'top 25%', scrub: 1.2 } }); });
    ScrollTrigger.create({ trigger: st, start: 'top 50%', once: true, onEnter: function () { $$('#evrStage [data-count]').forEach(function (b) { countUp(b, +b.dataset.count, 1.8); }); } });
    $$('#evrStage [data-depth]').forEach(function (el, i) { gsap.to(el, { yPercent: i % 2 ? -10 : 10, duration: 3 + i * .4, ease: 'sine.inOut', yoyo: true, repeat: -1, delay: 1.5 }); });
  });
  var evr = $('#evrStage');
  if (evr && fine) evr.addEventListener('mousemove', function (e) {
    var r = evr.getBoundingClientRect(), px = (e.clientX - r.left) / r.width - .5, py = (e.clientY - r.top) / r.height - .5;
    $$('[data-depth]', evr).forEach(function (c) { var d = +c.dataset.depth; gsap.to(c, { x: px * d, y: py * d * .6, duration: .9, ease: 'power3', overwrite: 'auto' }); });
    gsap.to('#evrPhone', { rotationY: px * 10, rotationX: -py * 8, duration: .9, ease: 'power3' });
  });

  /* ---------- superpowers: pinned horizontal ---------- */
  mm.add('(min-width: 901px)', function () {
    var track = $('#hzTrack'), sec = $('.hz');
    var dist = function () { return track.scrollWidth - (window.innerWidth - track.getBoundingClientRect().left) + 40; };
    var tw = gsap.to(track, { x: function () { return -dist(); }, ease: 'none', scrollTrigger: { trigger: sec, start: 'top top', end: function () { return '+=' + dist(); }, pin: true, scrub: 1, invalidateOnRefresh: true, anticipatePin: 1 } });
    $$('.pw', track).forEach(function (c) {
      gsap.from($('.art img', c), { scale: 1.3, ease: 'none', scrollTrigger: { trigger: c, containerAnimation: tw, start: 'left right', end: 'right left', scrub: true } });
      var s = $('.scr', c); if (s) gsap.from(s, { y: 120, rotation: 8, ease: 'none', scrollTrigger: { trigger: c, containerAnimation: tw, start: 'left right', end: 'center center', scrub: true } });
    });
  });
  mm.add('(max-width: 900px)', function () {
    $$('.pw').forEach(function (c) { gsap.from(c, { y: 60, opacity: 0, duration: .9, ease: 'power3.out', scrollTrigger: { trigger: c, start: 'top 88%' } }); });
  });

  /* ---------- app tour ---------- */
  var scrns = $$('#tourDevice .scrn'), steps = $$('.tstep'), curS = -1;
  function showScreen(n) {
    if (n === curS) return; curS = n;
    scrns.forEach(function (s, i) { s.classList.toggle('on', i === n); });
    steps.forEach(function (s, i) { s.classList.toggle('on', i === n); });
    $$('[data-ticker]', scrns[n]).forEach(function (t) { countUp(t, parseFloat(t.dataset.ticker), 1.2, 2); });
  }
  showScreen(0);
  mm.add('(min-width: 901px)', function () {
    steps.forEach(function (s, i) { ScrollTrigger.create({ trigger: s, start: 'top 55%', end: 'bottom 55%', onToggle: function (st) { if (st.isActive) showScreen(i); } }); });
    gsap.from('#tourDevice', { y: 120, rotation: -6, opacity: 0, duration: 1.2, ease: 'power4.out', scrollTrigger: { trigger: '#app', start: 'top 70%' } });
    $$('.tour-stage .orb').forEach(function (o, i) { gsap.to(o, { y: i % 2 ? -60 : 60, ease: 'none', scrollTrigger: { trigger: '#app', start: 'top bottom', end: 'bottom top', scrub: true } }); });
  });
  mm.add('(max-width: 900px)', function () {
    var i = 0, h = setInterval(function () { i = (i + 1) % scrns.length; showScreen(i); }, 3200);
    return function () { clearInterval(h); };
  });

  /* ---------- numbers ---------- */
  ScrollTrigger.create({ trigger: '#numbers', start: 'top 85%', once: true, onEnter: function () { $$('#numbers [data-count]').forEach(function (b) { countUp(b, +b.dataset.count, 1.6); }); gsap.from('#numbers>div', { y: 40, opacity: 0, stagger: .1, duration: .9, ease: 'power3.out' }); } });

  /* ---------- Virtual ID: holo tilt + card fan ---------- */
  var holo = $('#bigHolo'), stage = $('#cardStage');
  if (holo && fine) {
    stage.addEventListener('mousemove', function (e) { var r = holo.getBoundingClientRect(), px = (e.clientX - r.left) / r.width - .5, py = (e.clientY - r.top) / r.height - .5; holo.style.transform = 'rotateY(' + px * 22 + 'deg) rotateX(' + (-py * 18) + 'deg) translateZ(20px)'; });
    stage.addEventListener('mouseleave', function () { holo.style.transform = ''; });
  }
  gsap.from(holo, { y: -80, rotationX: 50, opacity: 0, duration: 1.4, ease: 'power4.out', scrollTrigger: { trigger: stage, start: 'top 75%' } });
  var fan = $$('.idc'), spread = [[-150, -22], [-50, -7], [50, 7], [150, 22]];
  var fanSc = function () { return window.innerWidth < 620 ? .55 : 1; };
  gsap.set(fan, { x: 0, rotation: 0, y: 80 });
  gsap.to(fan, { x: function (i) { return spread[i][0] * fanSc(); }, rotation: function (i) { return spread[i][1]; }, y: function (i) { return Math.abs(spread[i][1]) * 1.4; }, ease: 'power2.out', stagger: .04, scrollTrigger: { trigger: stage, start: 'top 70%', end: 'center 45%', scrub: 1, invalidateOnRefresh: true } });
  fan.forEach(function (c, i) {
    c.addEventListener('mouseenter', function () { gsap.to(c, { y: -40, scale: 1.06, zIndex: 9, duration: .4 }); });
    c.addEventListener('mouseleave', function () { gsap.to(c, { y: Math.abs(spread[i][1]) * 1.4, scale: 1, zIndex: 1, duration: .5 }); });
  });
  // card number reveal shimmer
  var num = $('#holoNum'), digits = '4056 2454 4455 5194';
  ScrollTrigger.create({ trigger: stage, start: 'top 60%', once: true, onEnter: function () {
    var k = 0, h = setInterval(function () { k++; num.textContent = digits.split('').map(function (ch, j) { return ch === ' ' ? ' ' : (j < k ? (j > 4 && j < 14 ? '•' : ch) : '0123456789'[Math.random() * 10 | 0]); }).join(''); if (k > digits.length) clearInterval(h); }, 45);
  } });

  /* ---------- cashback ---------- */
  gsap.from('.cb-node', { scale: .6, opacity: 0, duration: .9, stagger: .12, ease: 'back.out(1.7)', scrollTrigger: { trigger: '#cbScene', start: 'top 75%' } });
  gsap.from('.cb-hub', { scale: 0, rotation: -90, duration: 1.2, ease: 'back.out(1.4)', scrollTrigger: { trigger: '#cbScene', start: 'top 75%' } });
  gsap.from('.cb-path', { opacity: 0, duration: 1, stagger: .15, scrollTrigger: { trigger: '#cbScene', start: 'top 70%' } });
  ScrollTrigger.create({ trigger: '#cbScene', start: 'top 60%', once: true, onEnter: function () { $$('#cbScene [data-ticker]').forEach(function (t) { countUp(t, +t.dataset.ticker, 2.4, 2); }); } });
  ScrollTrigger.create({ trigger: '#dash3d', start: 'top 60%', once: true, onEnter: function () { $$('#dash3d [data-ticker]').forEach(function (t) { countUp(t, +t.dataset.ticker, 2, 2); }); } });

  /* ---------- verify ---------- */
  gsap.to('#verifyFrame>img', { yPercent: -8, ease: 'none', scrollTrigger: { trigger: '#verifyFrame', start: 'top bottom', end: 'bottom top', scrub: true } });
  gsap.fromTo('#vProg', { scaleX: 0 }, { scaleX: 1, duration: 2.2, ease: 'power2.inOut', scrollTrigger: { trigger: '#verifyFrame', start: 'top 65%' }, onComplete: function () { $('#vStatus').textContent = 'Verified · limits lifted'; } });

  /* ---------- legacy ---------- */
  legacy(true);

  /* ---------- pay via name@reid: lookup → confirm → receive loop ---------- */
  var payS = $$('#payDevice .scrn'), payP = $$('#paySteps span'), payT = $('#payType'), payR = $('#payRes'), payD = $('#payDone'), payTimers = [];
  function payShow(n) { payS.forEach(function (s, i) { s.classList.toggle('on', i === n); }); payP.forEach(function (s, i) { s.classList.toggle('on', i === n); }); }
  function payLoop() {
    payTimers.forEach(clearTimeout); payTimers = []; var at = function (ms, f) { payTimers.push(setTimeout(f, ms)); };
    payShow(0); payT.textContent = ''; payR.classList.remove('show'); payD.classList.remove('show');
    'tomboy@reid'.split('').forEach(function (ch, i) { at(300 + i * 110, function () { payT.textContent += ch; }); });
    at(1700, function () { payR.classList.add('show'); });
    at(3600, function () { payShow(1); });
    at(5600, function () { payD.classList.add('show'); });
    at(7400, function () { payShow(2); });
    at(10400, payLoop);
  }
  ScrollTrigger.create({ trigger: '#walletStage', start: 'top 70%', once: true, onEnter: payLoop });
  gsap.from('#walletStage .device', { y: 140, rotation: 8, duration: 1.2, ease: 'power4.out', scrollTrigger: { trigger: '#walletStage', start: 'top 80%' } });
  $$('#walletStage .coin').forEach(function (c, i) { gsap.to(c, { y: -40 - i * 25, rotation: 25 * (i % 2 ? -1 : 1), ease: 'none', scrollTrigger: { trigger: '#walletStage', start: 'top bottom', end: 'bottom top', scrub: true } }); });


  /* ---------- reID chat: messages play in sequence ---------- */
  var feed = $$('#chatScr .ch-feed > *');
  gsap.set(feed, { opacity: 0, y: 14, scale: .9 });
  ScrollTrigger.create({ trigger: '#duo', start: 'top 70%', onEnter: playChat, onEnterBack: playChat });
  function playChat() { gsap.killTweensOf(feed); gsap.set(feed, { opacity: 0, y: 14, scale: .9 }); gsap.to(feed, { opacity: 1, y: 0, scale: 1, duration: .5, stagger: .55, ease: 'back.out(1.8)' }); }
  gsap.from('#duo .d-back', { x: -120, rotation: -16, opacity: 0, duration: 1.2, ease: 'power4.out', scrollTrigger: { trigger: '#duo', start: 'top 80%' } });
  gsap.from('#duo .d-front', { x: 120, rotation: 14, opacity: 0, duration: 1.2, ease: 'power4.out', scrollTrigger: { trigger: '#duo', start: 'top 80%' } });

  /* ---------- sso ---------- */
  gsap.from('.sso', { clipPath: 'inset(10% 10% 10% 10% round 32px)', duration: 1.3, ease: 'power4.inOut', scrollTrigger: { trigger: '.sso', start: 'top 80%' } });
  gsap.from('.demo', { y: 80, rotation: 3, opacity: 0, duration: 1.1, ease: 'power3.out', scrollTrigger: { trigger: '.sso', start: 'top 60%' } });

  /* ---------- reCorporate ---------- */
  gsap.to('.corp-hero>img', { yPercent: 10, ease: 'none', scrollTrigger: { trigger: '.corp-hero', start: 'top bottom', end: 'bottom top', scrub: true } });
  mm.add('(min-width: 901px)', function () {
    gsap.fromTo('#plane', { rotationX: 32, scale: .86, y: 60 }, { rotationX: 0, scale: 1, y: 0, ease: 'none', scrollTrigger: { trigger: '#dash3d', start: 'top 95%', end: 'top 20%', scrub: 1 } });
    gsap.from('#plane .cd-row>*, #plane .cd-side', { y: 60, opacity: 0, stagger: .08, duration: 1, ease: 'power3.out', scrollTrigger: { trigger: '#dash3d', start: 'top 70%' } });
  });
  $$('#chaos span').forEach(function (s) { gsap.fromTo(s, { x: gsap.utils.random(-30, 30), y: gsap.utils.random(-14, 14), rotation: gsap.utils.random(-12, 12) }, { x: 0, y: 0, rotation: 0, ease: 'none', scrollTrigger: { trigger: '#chaos', start: 'top 95%', end: 'top 50%', scrub: true } }); });

  // showcase autoplay with progress
  var tabs = $$('.sc-tab'), imgs = $$('.sc-img img'), copies = $$('.sc-copy [data-copy]'), sci = 0, scTw;
  function sc(n, auto) {
    sci = n;
    tabs.forEach(function (b, k) { b.setAttribute('aria-selected', k === n ? 'true' : 'false'); gsap.set($('.pg', b), { width: 0 }); });
    imgs.forEach(function (im, k) { im.classList.toggle('on', k === n); });
    copies.forEach(function (c, k) { c.classList.toggle('on', k === n); });
    if (scTw) scTw.kill();
    if (auto) scTw = gsap.to($('.pg', tabs[n]), { width: '100%', duration: 5, ease: 'none', onComplete: function () { sc((n + 1) % tabs.length, true); } });
  }
  tabs.forEach(function (b, k) { b.addEventListener('click', function () { sc(k, false); }); });
  ScrollTrigger.create({ trigger: '.showcase', start: 'top 70%', once: true, onEnter: function () { sc(0, true); } });

  // flow line
  var nodes = $$('#flow .node');
  gsap.to('#flowLine', { strokeDashoffset: 0, ease: 'none', scrollTrigger: { trigger: '#flow', start: 'top 80%', end: 'top 35%', scrub: true, onUpdate: function (s) { nodes.forEach(function (n, i) { n.classList.toggle('on', s.progress >= i / (nodes.length - 1) - .02); }); } } });
  gsap.from(nodes, { y: 40, opacity: 0, stagger: .08, duration: .8, ease: 'back.out(1.6)', scrollTrigger: { trigger: '#flow', start: 'top 85%' } });
  gsap.fromTo('#qrHand', { y: 120, rotation: 10 }, { y: -40, rotation: -4, ease: 'none', scrollTrigger: { trigger: '#qrHand', start: 'top bottom', end: 'bottom top', scrub: true } });

  /* ---------- use cases ---------- */
  gsap.from('.case', { y: 100, opacity: 0, stagger: .12, duration: 1.1, ease: 'power3.out', scrollTrigger: { trigger: '.cases', start: 'top 80%' } });

  /* ---------- ambassador ---------- */
  gsap.to('.amb-art img', { yPercent: 8, ease: 'none', scrollTrigger: { trigger: '.amb-intro', start: 'top bottom', end: 'bottom top', scrub: true } });
  ScrollTrigger.create({ trigger: '#storeBody', start: 'top 75%', once: true, onEnter: function () {
    gsap.from('#storeBody .meter u', { scaleX: 0, duration: 1.4, stagger: .15, ease: 'power3.out' });
    $$('#storeBody [data-count]').forEach(function (b) { countUp(b, +b.dataset.count, 1.6); });
    gsap.from('#storeBody .prods>div', { y: 30, opacity: 0, stagger: .1, duration: .7, ease: 'back.out(1.6)' });
  } });
  var tls = $$('.tl');
  gsap.to('#rail', { height: '100%', ease: 'none', scrollTrigger: { trigger: '#timeline', start: 'top 60%', end: 'bottom 60%', scrub: true, onUpdate: function (s) { tls.forEach(function (t, i) { t.classList.toggle('on', s.progress >= i / tls.length); }); } } });
  gsap.from('.apply', { scale: .92, opacity: 0, duration: 1.1, ease: 'power3.out', scrollTrigger: { trigger: '.apply', start: 'top 85%' } });

  /* ---------- orbit ---------- */
  orbit();

  /* ---------- footer giant ---------- */
  gsap.from('.giant span', { yPercent: 100, opacity: 0, stagger: .08, duration: 1.2, ease: 'power4.out', scrollTrigger: { trigger: '.giant', start: 'top 95%' } });

  window.addEventListener('load', function () { ScrollTrigger.refresh(); });

  /* ================= helpers used with or without GSAP ================= */
  function fallbacks() { legacy(false); orbit(); $$('[data-ticker]').forEach(function (t) { t.textContent = fmt(parseFloat(t.dataset.ticker), 2); }); var tt = $('#payType'); if (tt) tt.textContent = 'tomboy@reid'; var pr = $('#payRes'); if (pr) pr.classList.add('show'); var vs = $('#vStatus'); if (vs) vs.textContent = 'Verified · limits lifted'; }

  function legacy(scroll) {
    var LV = ['Your direct invites', 'Friends of your friends', 'Your network keeps spreading', 'Every member strengthens it', 'Earnings compound as levels grow', 'Your legacy works while you sleep', 'Built by consistent sharing', 'Businesses and merchants count too', 'Almost the full reach', 'The deepest level you earn from'];
    var TXT = ['People who scan your QR and join reID.', 'People your invites bring in. You earn from them too.', 'Your network reaches people you may never meet.', 'More members, more activity, more cashback.', 'Each level adds to what flows back to you.', 'Activity at every level keeps earning for you.', 'Deep networks grow from steady sharing.', 'Merchants and corporates in your legacy count too.', 'Nine levels of activity working for you.', 'Your network, forever.'];
    var wrap = $('#levels'); if (!wrap || wrap.dataset.done) return; wrap.dataset.done = 1;
    var sel = 0, counts = [], total = 0;
    LV.forEach(function (l, k) {
      var b = document.createElement('button'); b.type = 'button'; b.className = 'lv'; b.setAttribute('aria-pressed', k === 0 ? 'true' : 'false');
      b.innerHTML = '<img src="assets/levels/level-' + (k + 1) + '.svg" alt="">L' + (k + 1);
      b.addEventListener('click', function () { set(k, true); }); wrap.appendChild(b);
    });
    var cv = $('#netCanvas'), ctx = cv.getContext('2d'), W = cv.width, C = W / 2, rings = [], seed = 7;
    function rnd() { seed = (seed * 16807) % 2147483647; return seed / 2147483647; }
    for (var r = 0; r < 10; r++) { var n = Math.round(5 + r * 5.4), pts = [], rad = 150 + r * 42; for (var k = 0; k < n; k++) { var a = k / n * Math.PI * 2 + r * .37 + rnd() * .25; pts.push({ x: C + Math.cos(a) * rad, y: C + Math.sin(a) * rad }); } rings.push({ rad: rad, pts: pts }); total += n; counts.push(total); }
    var numEl = $('#netNum');
    function set(k, manual) {
      if (k === sel && !manual) return; sel = k;
      $$('.lv').forEach(function (b, j) { b.setAttribute('aria-pressed', j === k ? 'true' : 'false'); });
      $('#lvTitle').textContent = 'Level ' + (k + 1) + ' · ' + LV[k]; $('#lvText').textContent = TXT[k];
      numEl.textContent = counts[k].toLocaleString();
    }
    var t0 = performance.now(), vis = true;
    if ('IntersectionObserver' in window) new IntersectionObserver(function (e) { vis = e[0].isIntersecting; }).observe(cv);
    function draw(now) {
      var t = (now - t0) / 1000; ctx.clearRect(0, 0, W, W);
      rings.forEach(function (ring, r) {
        var active = r <= sel, cur = r === sel;
        ctx.beginPath(); ctx.arc(C, C, ring.rad, 0, Math.PI * 2); ctx.strokeStyle = cur ? 'rgba(0,145,255,.55)' : active ? 'rgba(0,145,255,.18)' : 'rgba(11,18,32,.05)'; ctx.lineWidth = cur ? 3 : 2; ctx.stroke();
        ring.pts.forEach(function (p, i) {
          if (active) { var q = r ? rings[r - 1].pts[Math.floor(i * rings[r - 1].pts.length / ring.pts.length)] : { x: C, y: C }; ctx.beginPath(); ctx.moveTo(q.x, q.y); ctx.lineTo(p.x, p.y); ctx.strokeStyle = cur ? 'rgba(0,145,255,.4)' : 'rgba(0,145,255,.12)'; ctx.lineWidth = 1.6; ctx.stroke(); }
          var pulse = cur && !reduce ? 1 + .3 * Math.sin(t * 3 + i) : 1;
          ctx.beginPath(); ctx.arc(p.x, p.y, (cur ? 10 : active ? 7 : 5) * pulse, 0, Math.PI * 2); ctx.fillStyle = cur ? '#0091FF' : active ? '#7CC4FF' : '#D8E0EA'; ctx.fill();
        });
      });
      if (!reduce) for (var j = 0; j < 18; j++) {
        var rr = rings[sel], p = rr.pts[(j * 7) % rr.pts.length], f = (t * .35 + j / 18) % 1;
        ctx.beginPath(); ctx.arc(p.x + (C - p.x) * f, p.y + (C - p.y) * f, 5, 0, Math.PI * 2); ctx.fillStyle = 'rgba(194,154,82,' + (1 - f) + ')'; ctx.fill();
      }
    }
    (function loop(now) { if (vis) draw(now || performance.now()); if (!reduce) requestAnimationFrame(loop); })();
    set(0, true);
    if (scroll && hasG && window.ScrollTrigger) ScrollTrigger.create({ trigger: '#legacy', start: 'top 60%', end: 'bottom 70%', onUpdate: function (s) { set(Math.min(9, Math.floor(s.progress * 10))); } });
  }

  function orbit() {
    var o = $('#orbit'); if (!o || o.dataset.done) return; o.dataset.done = 1;
    var sats = $$('.sat', o);
    function place(t) {
      var R = o.clientWidth;
      sats.forEach(function (s) { var r = +s.dataset.r * R, a = +s.dataset.a + (reduce ? 0 : t * (s.dataset.r > .4 ? .00012 : -.0002)); s.firstElementChild.style.left = Math.cos(a) * r + 'px'; s.firstElementChild.style.top = Math.sin(a) * r + 'px'; });
      if (!reduce) requestAnimationFrame(place);
    }
    requestAnimationFrame(place);
  }
})();

/* ---------- non-motion interactions ---------- */
(function () {
  var $ = function (s) { return document.querySelector(s); }, $$ = function (s) { return Array.prototype.slice.call(document.querySelectorAll(s)); };
  function toast(m) { var t = $('#toast'); t.textContent = m; t.classList.add('on'); clearTimeout(t._h); t._h = setTimeout(function () { t.classList.remove('on'); }, 2600); }
  var demo = $('.demo');
  function step(n) { $$('.demo [data-step]').forEach(function (e) { e.hidden = +e.dataset.step !== n; }); if (window.gsap) gsap.from('.demo [data-step]:not([hidden])', { y: 20, opacity: 0, duration: .5, ease: 'power3.out' }); }
  $('#siw').addEventListener('click', function () { step(1); });
  $('#deny').addEventListener('click', function () { step(0); });
  $('#allow').addEventListener('click', function () { step(2); });
  $('#again').addEventListener('click', function () { step(0); });
  $('#copyCode').addEventListener('click', function () {
    var txt = $('#code').innerText.replace(/^Copy\s*/, '');
    var sel = function () { var r = document.createRange(); r.selectNodeContents($('#code')); var s = getSelection(); s.removeAllRanges(); s.addRange(r); toast('Press Ctrl+C to copy'); };
    if (navigator.clipboard) navigator.clipboard.writeText(txt).then(function () { toast('Code copied'); }, sel); else sel();
  });
  $$('[data-store]').forEach(function (a) { a.addEventListener('click', function (e) { e.preventDefault(); toast(a.dataset.store + ' listing is coming soon. Use the web app for now.'); }); });
  var form = $('#contactForm'), out = $('#f-out'), btn = $('#f-submit');
  form.addEventListener('submit', function (e) {
    e.preventDefault();
    var d = { name: $('#f-name').value.trim(), email: $('#f-email').value.trim(), company: $('#f-company').value.trim(), topic: $('#f-topic').value, message: $('#f-msg').value.trim() };
    function show(c, m) { out.hidden = false; out.className = 'form-msg ' + c; out.textContent = m; }
    if (!d.name || !/^\S+@\S+\.\S+$/.test(d.email) || !d.message) return show('err', 'Add your name, a valid email and a message, then send again.');
    btn.disabled = true; btn.textContent = 'Sending…';
    fetch('/api/contact', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(d) })
      .then(function (r) { if (!r.ok) throw 0; return r.json(); })
      .then(function () { form.reset(); show('ok', 'Message sent. We\'ll reply to ' + d.email + ' within one business day.'); })
      .catch(function () { show('err', 'We couldn\'t send your message. Email info@reidentity.net instead.'); })
      .then(function () { btn.disabled = false; btn.textContent = 'Send message'; });
  });
  $('#yr').textContent = new Date().getFullYear();
})();
