/* Explainer player: opens as a pop-up on first visit, becomes a floating mini player on scroll */
(function () {
  var $ = function (s) { return document.getElementById(s); };
  var vp = $('vp'), back = $('vpBack'), v = $('vpVideo'), reopen = $('vpReopen'), KEY = 'reid-explainer-seen';
  var CH = [['Meet reID', 0], ['For you', 10.05], ['Virtual ID', 29.09], ['Freelancers', 43.13], ['Business', 61.37], ['Earn extra', 79.7], ['Features', 98.48], ['Get started', 111.09]];
  var mode = 'closed', idle;

  // chapter buttons + marks
  var chBox = $('vpCh'), marks = $('vpMarks');
  CH.forEach(function (c, i) {
    var b = document.createElement('button'); b.type = 'button'; b.textContent = c[0];
    b.addEventListener('click', function () { v.currentTime = c[1]; v.play(); }); chBox.appendChild(b);
  });
  v.addEventListener('loadedmetadata', function () { marks.innerHTML = CH.slice(1).map(function (c) { return '<span style="left:' + (c[1] / v.duration * 100) + '%"></span>'; }).join(''); });

  function fmt(s) { s = Math.floor(s || 0); return Math.floor(s / 60) + ':' + ('0' + s % 60).slice(-2); }
  v.addEventListener('timeupdate', function () {
    $('vpFill').style.width = (v.currentTime / (v.duration || 1) * 100) + '%'; $('vpTime').textContent = fmt(v.currentTime);
    var k = 0; CH.forEach(function (c, i) { if (v.currentTime >= c[1]) k = i; });
    [].forEach.call(chBox.children, function (b, i) { b.classList.toggle('on', i === k); });
  });
  function syncIcons() {
    $('vpPlay').innerHTML = v.paused ? '<span class="i-play"></span>' : '<span class="i-pause"></span>'; $('vpPlay').setAttribute('aria-label', v.paused ? 'Play' : 'Pause');
    $('vpMute').innerHTML = '<span class="i-vol' + (v.muted ? ' off' : '') + '"></span>'; $('vpMute').setAttribute('aria-label', v.muted ? 'Unmute' : 'Mute');
    $('vpSound').hidden = !v.muted;
  }
  ['play', 'pause', 'volumechange'].forEach(function (e) { v.addEventListener(e, syncIcons); });
  v.addEventListener('ended', function () { setMode('mini'); });

  function setMode(m) {
    mode = m;
    vp.hidden = m === 'closed'; back.hidden = m !== 'modal'; reopen.hidden = m !== 'closed';
    vp.classList.toggle('modal', m === 'modal'); vp.classList.toggle('mini', m === 'mini');
    requestAnimationFrame(function () { back.classList.toggle('on', m === 'modal'); });
    if (m === 'closed') v.pause();
  }
  function open(withSound) {
    setMode('modal'); v.muted = !withSound;
    var p = v.play(); if (p && p.catch) p.catch(function () { v.muted = true; v.play().catch(function () {}); });
    syncIcons();
  }

  // controls
  $('vpPlay').addEventListener('click', function () { v.paused ? v.play() : v.pause(); });
  v.addEventListener('click', function () { if (v.muted) { v.muted = false; return; } v.paused ? v.play() : v.pause(); });
  $('vpSound').addEventListener('click', function () { v.muted = false; if (v.paused) v.play(); });
  $('vpMute').addEventListener('click', function () { v.muted = !v.muted; });
  function isFs() { return !!(document.fullscreenElement || document.webkitFullscreenElement || v.webkitDisplayingFullscreen); }
  function goFull() {
    v.muted = false; if (v.paused) v.play();
    var f = vp.querySelector('.vp-frame');
    var rq = f.requestFullscreen || f.webkitRequestFullscreen;
    if (rq) { var r = rq.call(f); if (r && r.then) r.then(function () { try { screen.orientation.lock('landscape').catch(function () {}); } catch (e) {} }).catch(function () { if (v.webkitEnterFullscreen) v.webkitEnterFullscreen(); }); }
    else if (v.webkitEnterFullscreen) v.webkitEnterFullscreen(); /* iPhone */
  }
  $('vpExpand').addEventListener('click', function () { if (mode === 'mini') setMode('modal'); else goFull(); });
  v.addEventListener('dblclick', goFull);
  document.addEventListener('fullscreenchange', function () { if (!document.fullscreenElement) { try { screen.orientation.unlock(); } catch (e) {} } });
  $('vpClose').addEventListener('click', function () { if (document.fullscreenElement) document.exitFullscreen(); else if (document.webkitFullscreenElement) document.webkitExitFullscreen(); setMode('closed'); });
  back.addEventListener('click', function () { setMode('mini'); });
  reopen.addEventListener('click', function () { open(true); });
  [].forEach.call(document.querySelectorAll('[data-watch]'), function (b) { b.addEventListener('click', function () { v.currentTime = 0; open(true); }); });
  $('vpTrack').addEventListener('click', function (e) { var r = this.getBoundingClientRect(); v.currentTime = (e.clientX - r.left) / r.width * (v.duration || 0); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && mode === 'modal') setMode('mini'); });
  vp.addEventListener('mousemove', function () { var bar = vp.querySelector('.vp-bar'); bar.classList.remove('idle'); clearTimeout(idle); idle = setTimeout(function () { bar.classList.add('idle'); }, 2500); });

  // scrolling while the pop-up is open docks it as a mini player, still playing
  var y0 = 0;
  var rot = 0; function hold() { rot = Date.now(); y0 = scrollY; }
  window.addEventListener('resize', hold); window.addEventListener('orientationchange', hold);
  v.addEventListener('webkitendfullscreen', hold); document.addEventListener('fullscreenchange', hold);
  function canDock() { return mode === 'modal' && !isFs() && Date.now() - rot > 1200; }
  window.addEventListener('scroll', function () { if (canDock() && Math.abs(scrollY - y0) > 60) setMode('mini'); }, { passive: true });
  window.addEventListener('wheel', function (e) { if (canDock() && Math.abs(e.deltaY) > 20) setMode('mini'); }, { passive: true });
  window.addEventListener('touchmove', function (e) { if (canDock() && !vp.contains(e.target)) setMode('mini'); }, { passive: true });

  // first visit: pop up after the intro animation
  var seen = false; try { seen = localStorage.getItem(KEY) === '1'; } catch (e) {}
  if (!seen) {
    setTimeout(function () { y0 = scrollY; open(false); try { localStorage.setItem(KEY, '1'); } catch (e) {} }, 3200);
  } else setMode('closed');
})();
// hide the "click to try" hint once someone has used that control
[].forEach.call(document.querySelectorAll('.try, .try-wrap, #cardStage'), function (el) {
  ['click', 'mouseenter'].forEach(function (ev) { el.addEventListener(ev === 'mouseenter' && el.id !== 'cardStage' ? 'x' : ev, function () { el.classList.add('used'); var t = el.querySelector('.tap'); if (t) t.style.opacity = 0; }); });
});
(function(){var b=document.getElementById('copyLink');if(!b)return;b.addEventListener('click',function(){var u='https://reidentity.net/';var done=function(){b.textContent='Link copied';setTimeout(function(){b.textContent='Copy link'},1800)};if(navigator.clipboard)navigator.clipboard.writeText(u).then(done,function(){b.textContent=u});else b.textContent=u;});})();
