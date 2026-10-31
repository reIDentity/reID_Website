(function () {
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;

  function toast(msg) { var t = $('#toast'); t.textContent = msg; t.classList.add('on'); clearTimeout(t._h); t._h = setTimeout(function () { t.classList.remove('on'); }, 2400); }

  // mobile menu
  var burger = $('#burger'), menu = $('#menu');
  burger.addEventListener('click', function () { var o = menu.classList.toggle('open'); burger.setAttribute('aria-expanded', o); });
  $$('#menu a').forEach(function (a) { a.addEventListener('click', function () { menu.classList.remove('open'); burger.setAttribute('aria-expanded', 'false'); }); });

  // active nav link
  var navLinks = $$('.links a');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { navLinks.forEach(function (a) { a.classList.toggle('on', a.getAttribute('href') === '#' + e.target.id); }); } });
    }, { rootMargin: '-45% 0px -50% 0px' });
    ['personal', 'legacy', 'wallet', 'sso', 'corporate', 'ambassador', 'faq'].forEach(function (id) { var el = document.getElementById(id); if (el) io.observe(el); });
  }

  // marquee: duplicate track for seamless loop
  var mq = $('#mq'); if (mq) mq.innerHTML += mq.innerHTML;

  // generic tab switcher
  function tabs(btnSel, attr, panes, auto) {
    var btns = $$(btnSel), i = 0, timer;
    function show(n) {
      i = n;
      btns.forEach(function (b, k) { b.setAttribute('aria-selected', k === n ? 'true' : 'false'); });
      panes.forEach(function (list) { list.forEach(function (p, k) { p.classList.toggle('on', k === n); }); });
    }
    btns.forEach(function (b) { b.addEventListener('click', function () { clearInterval(timer); show(+b.dataset[attr]); }); });
    if (auto && !reduce) timer = setInterval(function () { show((i + 1) % btns.length); }, auto);
  }
  tabs('.tour-item', 'screen', [$$('.device-stage .glass img')], 4500);
  tabs('.sc-tab', 'sc', [$$('.sc-img img'), $$('.sc-copy [data-copy]')]);

  // legacy network
  var LV = [
    ['Your direct invites', 'People who scan your QR and join reID.'],
    ['Their invites', 'Friends of your friends join, and you earn from them too.'],
    ['Level 3', 'Your network keeps spreading through people you may never meet.'],
    ['Level 4', 'Every new member strengthens the whole network.'],
    ['Level 5', 'Earnings compound as each level grows.'],
    ['Level 6', 'Your legacy keeps working while you sleep.'],
    ['Level 7', 'Deep networks are built by consistent sharing.'],
    ['Level 8', 'Businesses and merchants count too.'],
    ['Level 9', 'Almost the full reach of your legacy.'],
    ['Level 10', 'The deepest level you earn from. Your network, forever.']
  ];
  var lvWrap = $('#levels'), sel = 0;
  LV.forEach(function (l, k) {
    var b = document.createElement('button'); b.type = 'button'; b.className = 'lv';
    b.setAttribute('aria-pressed', k === 0 ? 'true' : 'false');
    b.innerHTML = '<img src="assets/levels/level-' + (k + 1) + '.svg" alt="">L' + (k + 1);
    b.addEventListener('click', function () { setLevel(k); });
    lvWrap.appendChild(b);
  });
  function setLevel(k) {
    sel = k;
    $$('.lv').forEach(function (b, j) { b.setAttribute('aria-pressed', j === k ? 'true' : 'false'); });
    $('#lvTitle').textContent = 'Level ' + (k + 1) + ' · ' + LV[k][0].replace(/^Level \d+$/, 'Your network');
    $('#lvText').textContent = LV[k][1];
    draw();
  }

  var cv = $('#netCanvas'), ctx = cv.getContext('2d'), W = cv.width, C = W / 2;
  var rings = [], seed = 11;
  function rnd() { seed = (seed * 16807) % 2147483647; return seed / 2147483647; }
  for (var r = 0; r < 10; r++) {
    var n = Math.round(4 + r * 5.2), pts = [];
    var rad = 120 + r * 42;
    for (var k = 0; k < n; k++) { var a = (k / n) * Math.PI * 2 + r * .37 + rnd() * .2; pts.push({ x: C + Math.cos(a) * rad, y: C + Math.sin(a) * rad, a: a }); }
    rings.push({ rad: rad, pts: pts });
  }
  var t0 = performance.now();
  function draw(now) {
    var t = ((now || performance.now()) - t0) / 1000;
    ctx.clearRect(0, 0, W, W);
    rings.forEach(function (ring, r) {
      var active = r <= sel, cur = r === sel;
      ctx.beginPath(); ctx.arc(C, C, ring.rad, 0, Math.PI * 2);
      ctx.strokeStyle = cur ? 'rgba(0,145,255,.55)' : active ? 'rgba(0,145,255,.18)' : 'rgba(13,20,34,.06)';
      ctx.lineWidth = cur ? 3 : 2; ctx.stroke();
      ring.pts.forEach(function (p, i) {
        if (r > 0 && active) {
          var prev = rings[r - 1].pts, q = prev[Math.floor(i * prev.length / ring.pts.length)];
          ctx.beginPath(); ctx.moveTo(q.x, q.y); ctx.lineTo(p.x, p.y);
          ctx.strokeStyle = cur ? 'rgba(0,145,255,.35)' : 'rgba(0,145,255,.12)'; ctx.lineWidth = 1.5; ctx.stroke();
        } else if (r === 0) {
          ctx.beginPath(); ctx.moveTo(C, C); ctx.lineTo(p.x, p.y); ctx.strokeStyle = 'rgba(0,145,255,.3)'; ctx.lineWidth = 2; ctx.stroke();
        }
        var pulse = cur && !reduce ? 1 + .25 * Math.sin(t * 3 + i) : 1;
        ctx.beginPath(); ctx.arc(p.x, p.y, (cur ? 9 : active ? 7 : 5) * pulse, 0, Math.PI * 2);
        ctx.fillStyle = cur ? '#0091FF' : active ? '#7CC4FF' : '#D5DDE8'; ctx.fill();
      });
    });
    // flowing earnings particle toward centre
    if (!reduce) {
      for (var j = 0; j < 14; j++) {
        var ring = rings[Math.min(sel, 9)], p = ring.pts[(j * 7) % ring.pts.length];
        var f = ((t * .35 + j / 14) % 1);
        var x = p.x + (C - p.x) * f, y = p.y + (C - p.y) * f;
        ctx.beginPath(); ctx.arc(x, y, 4, 0, Math.PI * 2); ctx.fillStyle = 'rgba(184,146,74,' + (1 - f) + ')'; ctx.fill();
      }
    }
  }
  var visible = true;
  if ('IntersectionObserver' in window) new IntersectionObserver(function (e) { visible = e[0].isIntersecting; }, {}).observe(cv);
  (function loop(now) { if (visible) draw(now); if (!reduce) requestAnimationFrame(loop); })();

  // SSO demo
  var demo = $('.demo');
  function step(n) { $$('[data-step]', demo).forEach(function (e) { e.hidden = +e.dataset.step !== n; }); }
  $('#siw').addEventListener('click', function () { step(1); });
  $('#deny').addEventListener('click', function () { step(0); });
  $('#allow').addEventListener('click', function () { step(2); });
  $('#again').addEventListener('click', function () { step(0); });

  // copy code
  $('#copyCode').addEventListener('click', function () {
    var txt = $('#code').innerText.replace(/^Copy\s*/, '');
    var ok = function () { toast('Code copied'); };
    if (navigator.clipboard) navigator.clipboard.writeText(txt).then(ok, function () { selectCode(); });
    else selectCode();
  });
  function selectCode() { var r = document.createRange(); r.selectNodeContents($('#code')); var s = getSelection(); s.removeAllRanges(); s.addRange(r); toast('Press Ctrl+C to copy'); }

  // store buttons (links pending)
  $$('[data-store]').forEach(function (a) { a.addEventListener('click', function (e) { e.preventDefault(); toast(a.dataset.store + ' listing is coming soon. Use the web app for now.'); }); });

  // contact form → /api/contact
  var form = $('#contactForm'), out = $('#f-out'), btn = $('#f-submit');
  form.addEventListener('submit', function (e) {
    e.preventDefault();
    var d = { name: $('#f-name').value.trim(), email: $('#f-email').value.trim(), company: $('#f-company').value.trim(), topic: $('#f-topic').value, message: $('#f-msg').value.trim() };
    function show(cls, msg) { out.hidden = false; out.className = 'form-msg ' + cls; out.textContent = msg; }
    if (!d.name || !/^\S+@\S+\.\S+$/.test(d.email) || !d.message) return show('err', 'Add your name, a valid email and a message, then send again.');
    btn.disabled = true; btn.textContent = 'Sending…';
    fetch('/api/contact', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(d) })
      .then(function (r) { if (!r.ok) throw new Error(); return r.json(); })
      .then(function () { form.reset(); show('ok', 'Message sent. We\'ll reply to ' + d.email + ' within one business day.'); })
      .catch(function () { show('err', 'We couldn\'t send your message. Email info@reidentity.net instead.'); })
      .then(function () { btn.disabled = false; btn.textContent = 'Send message'; });
  });

  $('#yr').textContent = new Date().getFullYear();
})();
