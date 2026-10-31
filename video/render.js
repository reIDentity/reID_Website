/* Builds one paused GSAP timeline for the whole explainer. The renderer calls window.seek(t) per frame. */
(async function () {
  var $ = function (s) { return document.querySelector(s); }, $$ = function (s) { return [].slice.call(document.querySelectorAll(s)); };
  var CH = await (await fetch('chapters.json')).json();
  var TOTAL = CH[CH.length - 1].start + CH[CH.length - 1].dur;

  // reCorporate dashboard markup, reused from the site
  var html = await (await fetch('../index.html')).text();
  var m = html.match(/<div class="cdash"[\s\S]*?<\/aside>[\s\S]*?<div class="cd-row r3">[\s\S]*?<\/div>\s*<\/div>\s*<\/div>\s*<\/div>\s*<\/div>/);
  if (m) $('#dash4').innerHTML = m[0].replace(/assets\//g, '../assets/');

  // legacy network nodes
  var net = $('#net5'), rings = [140, 240, 340];
  rings.forEach(function (r, i) { var d = document.createElement('div'); d.className = 'ring'; d.style.cssText = 'left:' + -r + 'px;top:' + -r + 'px;width:' + 2 * r + 'px;height:' + 2 * r + 'px'; net.appendChild(d); });
  var core = document.createElement('div'); core.className = 'core'; core.innerHTML = '<img src="../assets/icons/reid-corporate.svg" alt="">'; net.appendChild(core);
  var nodes = [];
  rings.forEach(function (r, ri) { var n = 6 + ri * 6; for (var k = 0; k < n; k++) { var a = k / n * Math.PI * 2 + ri * .4, d = document.createElement('div'); d.className = 'node'; d.style.left = Math.cos(a) * r + 'px'; d.style.top = Math.sin(a) * r + 'px'; d.dataset.ring = ri; net.appendChild(d); nodes.push(d); } });
  var coins = []; for (var c = 0; c < 6; c++) { var co = document.createElement('div'); co.className = 'coin'; co.textContent = '$'; co.style.left = '-32px'; co.style.top = '-32px'; net.appendChild(co); coins.push(co); }

  // features ring
  var F = [['wallet', 'Wallet'], ['cash', 'Fiat account'], ['credit-card', 'Virtual cards'], ['phone', 'eSIM'], ['qr-code', 'Contact sharing'], ['mail', 'Chat'], ['rewards', 'Cashback'], ['legacy', 'Legacy network'], ['users-group', 'Corporate account']];
  var feat = $('#feat6');
  F.forEach(function (f, i) {
    var a = i / F.length * Math.PI * 2 - Math.PI / 2, d = document.createElement('div'); d.className = 'ftile';
    d.innerHTML = '<svg class="ic"><use href="../assets/sprite.svg#i-' + f[0] + '"/></svg><b>' + f[1] + '</b>';
    d.style.left = (Math.cos(a) * 660 - 150) + 'px'; d.style.top = (Math.sin(a) * 225 - 55) + 'px'; feat.appendChild(d);
  });

  // pixel background (deterministic from t)
  var cv = $('#px'), ctx = cv.getContext('2d');
  function pixels(t) { ctx.clearRect(0, 0, 1920, 1080); for (var x = 12; x < 1920; x += 24) for (var y = 12; y < 1080; y += 24) { var w = (Math.sin(x * .01 + t * 1.2) * Math.cos(y * .012 - t * .9) + 1) / 2; ctx.fillStyle = 'rgba(0,145,255,' + (.03 + w * .06) + ')'; ctx.fillRect(x - 1.5, y - 1.5, 3, 3); } }

  var tl = gsap.timeline({ paused: true });
  function scene(i, build) {
    var c = CH[i], s = '#s' + i, st = c.start, en = c.start + c.dur;
    tl.set(s, { autoAlpha: 1 }, st).fromTo(s, { autoAlpha: 0 }, { autoAlpha: 1, duration: .5 }, st);
    build(st, en);
    if (i < CH.length - 1) tl.to(s, { autoAlpha: 0, duration: .45 }, en - .35);
  }
  var E = 'power3.out', B = 'back.out(1.7)';

  scene(0, function (t) {
    tl.from('#paint0', { clipPath: 'inset(12% 12% 12% 12% round 40px)', scale: 1.06, duration: 1.4, ease: 'power4.inOut' }, t)
      .from('#paint0 img', { scale: 1.3, duration: 3, ease: E }, t)
      .from('#paint0 .bracket i', { scale: 0, opacity: 0, stagger: .1, duration: .6, ease: B }, t + 1)
      .fromTo('#beam0', { top: '0%' }, { top: '96%', duration: 2, ease: 'sine.inOut', yoyo: true, repeat: 3 }, t + 1.4)
      .from('#logo0', { y: 40, opacity: 0, duration: .8, ease: E }, t + .3)
      .from('#h0 .word', { yPercent: 100, opacity: 0, stagger: .15, duration: .9, ease: 'power4.out' }, t + .7)
      .from('#p0', { y: 30, opacity: 0, duration: .8, ease: E }, t + 2)
      .from('#pl0 .pill', { y: 30, opacity: 0, scale: .8, stagger: .35, duration: .6, ease: B }, t + 4.2)
      .from('#c0a', { y: 50, opacity: 0, duration: .7, ease: B }, t + 3)
      .from('#c0b', { y: 50, opacity: 0, duration: .7, ease: B }, t + 5.5);
  });
  scene(1, function (t) {
    tl.from('#s1 .mid', { y: 50, opacity: 0, duration: .9, ease: 'power4.out' }, t + .3)
      .from('#s1 .sub', { y: 30, opacity: 0, duration: .8, ease: E }, t + 1)
      .from('#s1 .i1', { y: 30, opacity: 0, scale: .8, stagger: .3, duration: .6, ease: B }, t + 2.5)
      .from('#ph1', { y: 300, rotation: 8, opacity: 0, duration: 1.2, ease: 'power4.out' }, t + .2)
      .from('#c1', { x: -80, opacity: 0, duration: .7, ease: B }, t + 6.5)
      .set('#sc1a', { clipPath: 'inset(0 0 0 0)' }, t)
      .fromTo('#sc1b', { clipPath: 'inset(100% 0 0 0)' }, { clipPath: 'inset(0% 0 0 0)', duration: .9, ease: 'power4.inOut' }, t + 9.5)
      .from('#pay1', { y: 30, opacity: 0, duration: .6, ease: B }, t + 12)
      .from('#tx1', { x: 60, opacity: 0, duration: .6, ease: B }, t + 16);
    var txt = { n: 0 }; tl.to(txt, { n: 8, duration: 2, ease: 'none', onUpdate: function () { $('#type1').textContent = 'sam@reid'.slice(0, Math.round(txt.n)); } }, t + 12.6);
    tl.set('#type1', { textContent: '' }, t);
  });
  scene(2, function (t) {
    tl.from('#s2 .mid', { y: 50, opacity: 0, duration: .9, ease: 'power4.out' }, t + .3)
      .from('#s2 .sub', { y: 30, opacity: 0, duration: .8, ease: E }, t + 1)
      .from('#s2 .i2', { y: 30, opacity: 0, scale: .8, stagger: .45, duration: .6, ease: B }, t + 6)
      .from('#holo2', { y: -200, rotationX: 60, opacity: 0, duration: 1.3, ease: 'power4.out', transformPerspective: 1200 }, t + .4)
      .to('#holo2', { rotation: -3, y: -10, duration: 4, ease: 'sine.inOut', yoyo: true, repeat: 2 }, t + 1.8);
    var f = $$('.f2'), spread = [[-330, -14], [0, 0], [330, 14]];
    tl.from(f, { y: 200, opacity: 0, duration: .8, stagger: .2, ease: E }, t + 2.5)
      .to(f, { x: function (i) { return spread[i][0]; }, rotation: function (i) { return spread[i][1]; }, y: function (i) { return Math.abs(spread[i][1]) * 3; }, duration: 1, ease: 'power3.inOut' }, t + 3.6);
  });
  scene(3, function (t) {
    tl.from('#s3 .mid', { y: 50, opacity: 0, duration: .9, ease: 'power4.out' }, t + .3)
      .from('#s3 .sub', { y: 30, opacity: 0, duration: .8, ease: E }, t + 1)
      .from('#qr3', { scale: .5, rotation: -10, opacity: 0, duration: 1, ease: B }, t + 1.5)
      .from('#b3a', { scale: .6, y: 20, opacity: 0, duration: .5, ease: B, transformOrigin: 'left bottom' }, t + 6)
      .from('#b3b', { scale: .6, y: 20, opacity: 0, duration: .5, ease: B, transformOrigin: 'right bottom' }, t + 8)
      .from('#p3', { scale: .6, y: 40, opacity: 0, duration: .6, ease: B }, t + 10)
      .from('#c3', { x: -80, opacity: 0, duration: .7, ease: B }, t + 13);
  });
  scene(4, function (t) {
    tl.from('#s4 .mid', { y: 50, opacity: 0, duration: .9, ease: 'power4.out' }, t + .3)
      .from('#s4 .sub', { y: 30, opacity: 0, duration: .8, ease: E }, t + 1)
      .from('#dash4', { y: 300, rotationX: 25, opacity: 0, duration: 1.4, ease: 'power4.out', transformPerspective: 1600 }, t + .3)
      .from('#dash4 .cd-row > *, #dash4 .cd-side', { y: 50, opacity: 0, stagger: .12, duration: .7, ease: E }, t + 1.2)
      .from('#s4 .i4', { y: 30, opacity: 0, scale: .8, stagger: .4, duration: .6, ease: B }, t + 4)
      .to('#dash4', { y: -120, duration: 8, ease: 'sine.inOut' }, t + 6)
      .from('#siw4', { y: 60, scale: .8, opacity: 0, duration: .8, ease: B }, t + 12.5);
  });
  scene(5, function (t) {
    tl.from('#s5 .mid', { y: 50, opacity: 0, duration: .9, ease: 'power4.out' }, t + .3)
      .from('#s5 .e5', { x: -60, opacity: 0, stagger: { each: 4.5 }, duration: .7, ease: B }, t + 1.2)
      .from('#net5 .ring', { scale: 0, opacity: 0, stagger: 1.2, duration: 1, ease: E }, t + 4)
      .from('#net5 .core', { scale: 0, rotation: -90, duration: 1, ease: B }, t + .6)
      .from('#cnt5', { y: -40, opacity: 0, duration: .7, ease: B }, t + 4.5)
      .from('#cb5', { y: 40, opacity: 0, duration: .7, ease: B }, t + 1.2);
    nodes.forEach(function (n) { var r = +n.dataset.ring; tl.from(n, { scale: 0, opacity: 0, duration: .4, ease: B }, t + 4.3 + r * 1.3 + Math.random() * .8).to(n, { backgroundColor: '#0091FF', duration: .3 }, t + 4.8 + r * 1.3); });
    coins.forEach(function (co, i) {
      var a = i / coins.length * Math.PI * 2, r = 330;
      tl.fromTo(co, { x: -200, y: 120, opacity: 0, scale: .5 }, { opacity: 1, scale: 1, duration: .3 }, t + 1.4 + i * .35)
        .to(co, { x: 0, y: 0, duration: .9, ease: 'power2.in' }, t + 1.5 + i * .35)
        .to(co, { opacity: 0, scale: .3, duration: .2 }, t + 2.4 + i * .35)
        .fromTo(co, { x: Math.cos(a) * r, y: Math.sin(a) * r, opacity: 0, scale: .7 }, { opacity: 1, duration: .2 }, t + 8 + i * .6)
        .to(co, { x: 0, y: 0, duration: 1.1, ease: 'power2.in' }, t + 8.2 + i * .6)
        .to(co, { opacity: 0, duration: .2 }, t + 9.3 + i * .6);
    });
    var cnt = { v: 0 }; tl.to(cnt, { v: 1284, duration: 10, ease: 'power2.inOut', onUpdate: function () { $('#n5').textContent = Math.round(cnt.v).toLocaleString() + (cnt.v > 1280 ? '+' : ''); } }, t + 4.5);
    var cb = { v: 0 }; tl.to(cb, { v: 482.4, duration: 12, ease: 'power1.inOut', onUpdate: function () { $('#m5').textContent = cb.v.toFixed(2); } }, t + 1.5);
    tl.set('#n5', { textContent: '0' }, t).set('#m5', { textContent: '0.00' }, t);
  });
  scene(6, function (t) {
    tl.from('#h6', { y: 40, opacity: 0, duration: .9, ease: 'power4.out' }, t + .2)
      .from('#feat6 .core', { scale: 0, rotation: -120, duration: 1, ease: B }, t + .3)
      .from('#feat6 .ftile', { x: 0, y: 0, left: -150, top: -40, scale: .3, opacity: 0, stagger: .55, duration: .8, ease: B }, t + 1.5);
  });
  scene(7, function (t) {
    tl.from('#logo7', { scale: .6, opacity: 0, duration: 1, ease: B }, t + .2)
      .from('#h7', { y: 40, opacity: 0, duration: .9, ease: 'power4.out' }, t + 1)
      .from('#u7', { scale: .5, opacity: 0, duration: .7, ease: B }, t + 2.4);
  });
  tl.to('#logoTL', { opacity: 0, duration: .4 }, CH[4].start).to('#logoTL', { opacity: 1, duration: .4 }, CH[5].start).to('#logoTL', { opacity: 0, duration: .4 }, CH[7].start).from('#logoTL', { opacity: 0, duration: .6 }, CH[1].start).set('#logoTL', { opacity: 0 }, 0).set('#logoTL', { opacity: 1 }, CH[1].start + .6);
  tl.to({}, { duration: 0.01 }, TOTAL);

  // captions: split each chapter into sentences, weighted by length
  var caps = [];
  CH.forEach(function (c) {
    var parts = c.text.match(/[^.!?]+[.!?]+/g) || [c.text], L = parts.reduce(function (a, p) { return a + p.length; }, 0), t = c.start + .35, avail = c.dur - .9;
    parts.forEach(function (p) { var d = avail * p.length / L; caps.push([t, t + d, p.trim().replace(/ dot net/, '.net').replace(/sam at reID/, 'sam@reid')]); t += d; });
  });
  var capEl = $('#cap'), prog = $('#prog');
  window.TOTAL = TOTAL;
  window.seek = function (t) {
    tl.seek(t, false); pixels(t);
    var c = caps.find(function (x) { return t >= x[0] && t < x[1]; }); capEl.textContent = c ? c[2] : ''; capEl.style.opacity = c ? 1 : 0;
    prog.style.width = (t / TOTAL * 100) + '%';
  };
  window.CAPS = caps;
  window.seek(0);
  await document.fonts.ready; window.READY = true;
})();
