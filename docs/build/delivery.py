from common import *

DOC = 'Delivery & Handover Report'
COMMIT = '0f6566a'

cover = f'''<section class="page cover"><div class="glow"></div><div class="dots"></div><div class="in">
<img class="logo" src="{LOGO}">
<div class="kick">DELIVERY &amp; HANDOVER REPORT</div>
<h1>reID Website —<br><span>Design, Build &amp; Handover</span></h1>
<div class="sub">A premium, animated marketing site for reID: one identity for sign-in, verification, payments, chat and earning, for people, freelancers and businesses.</div>
<div class="hero"><img src="{img('d-hero.jpg')}"></div>
<div class="meta"><div><small>DATE</small><b>31 October 2026</b></div><div><small>DOMAIN</small><b>reidentity.net</b></div><div><small>REPOSITORY</small><b>reIDentity/reID_Website</b></div><div><small>BRANCH</small><b>main · {COMMIT}</b></div></div>
</div></section>'''

P = []

P.append(sec('01', 'Executive summary', f'''
<p class="lead">The old reID page on resystem.org/id has been replaced with a standalone, light-only, Apple-style website at <b>reidentity.net</b>. It explains reID to individuals, freelancers and businesses, sells reCorporate, recruits Ambassadors, and is ready for the App Store and Google Play listings.</p>
<div class="grid g4" style="margin:5mm 0">
<div class="stat"><b>24</b><span>landing-page sections, all animated</span></div>
<div class="stat"><b>1:58</b><span>narrated explainer video, 8 chapters</span></div>
<div class="stat"><b>6</b><span>own legal &amp; support pages</span></div>
<div class="stat"><b>100</b><span>Lighthouse SEO &amp; Best Practices</span></div></div>
<h3>What was delivered</h3>
<ul>
<li>Full-screen hero with an identity scan reveal, pixel field, watch card and live chips.</li>
<li>Product story: Everything-in-one passport, superpowers, app tour, Virtual ID, cashback, verification, unlimited-level legacy network, pay to <code>name@reid</code>, reID Chat and contact sharing.</li>
<li>Security &amp; SSO section plus an interactive "Sign in with reID" demo (OAuth 2.0 / OIDC).</li>
<li>reCorporate: live animated dashboard built from the new dashboard and role-management screens, legal pathway and industries.</li>
<li>Ambassador programme with storefront, earning tiles and a horizontal process timeline; industries ecosystem orbit.</li>
<li>Kokoro-voiced explainer video as a first-visit pop-up that docks into a YouTube-style mini player.</li>
<li>Store-ready Privacy, Terms, Cookies, Account deletion and Support pages hosted on the site.</li>
<li>SEO, social sharing and AI discovery: structured data, OG images, sitemap, robots rules for AI crawlers, <code>llms.txt</code> and an OpenAPI description so AI agents can send enquiries.</li>
<li>Phone pass: Apple-style swipe rows, iOS Safari fixes, tighter rhythm on 360–430 px screens.</li></ul>
<div class="callout"><b>Status:</b> live on Vercel from <code>main</code>. Remaining items are business actions (domain, mailboxes, SMTP, legal sign-off, store links), listed in section 16.</div>'''))

P.append(sec('02', 'Scope, sources & brand rules', table(['Source', 'Used for'], [
 ['Old site resystem.org/id', 'Feature list, wording baseline'],
 ['reID product PDF &amp; app screens (artifacts)', 'Home, wallet, Virtual ID, login, chat, contact sharing screens'],
 ['reCorporate pitch + new dashboard / roles screenshots', 'reCorporate section and live dashboard mock'],
 ['Ambassador sales pitch', 'Ambassador section, earning model, process'],
 ['reID Chat &amp; wallet artifacts', 'Chat duo and pay-to-name flow'],
 ['reid-icons repo', 'Pixel icon sprite'],
 ['reWallet / reMarketplace sites', 'Motion language and quality bar']]) + '''
<h3>Brand rules agreed during the build</h3>
<div class="grid g2"><ul>
<li>reID only — <b>no reAED</b> mention.</li>
<li>No ReSystem product links (reWallet, reInvest, reMarketplace) in the ecosystem; show <b>industries</b> instead.</li>
<li>Legacy network has <b>unlimited levels</b> (shown as ∞ after L10).</li>
<li><b>Light theme only</b>; no black sections.</li></ul><ul>
<li>No hand image in the hero; reference images used for direction only.</li>
<li>Own legal pages — no redirect to resystem.org.</li>
<li>Header always visible; reduced spacing; horizontal process.</li>
<li>No Google Search Console submission; language switcher skipped.</li></ul></div>
<h3>Stack</h3><p>Node.js / Express (local + API), static HTML/CSS/JS, GSAP 3.12 + ScrollTrigger + Lenis (vendored), deployed on Vercel with a serverless <code>/api/contact</code> function.</p>'''))

P.append(sec('03', 'What reID is (positioning on the site)', '''
<p class="lead">reID is one secure digital identity passport. One login replaces passwords across the ecosystem; one verified profile replaces repeated KYC; one name (<code>name@reid</code>) receives payments and shares contacts.</p>
''' + table(['Audience', 'Message on the site', 'Where'], [
 ['Individuals', 'Passkey sign-in, Virtual ID card, wallet, cashback, private chat', 'Hero, Personal, App tour, Virtual ID'],
 ['Freelancers', 'Get paid to name@reid, verified profile builds trust, earn as Ambassador', 'Wallet, Verify, Ambassador'],
 ['Businesses', 'reCorporate: verified company identity, roles, staff, legacy payouts, fiat &amp; crypto', 'reCorporate'],
 ['Developers / partners', 'Sign in with reID (OAuth/OIDC), SSO for the whole ecosystem', 'Security, SSO demo'],
 ['Ambassadors', 'Storefront, commissions through the legacy network', 'Ambassador']]) + f'''
<div class="grid g2" style="margin-top:4mm">{shot('d-everything.jpg', 'Everything in one passport')}{shot('d-personal.jpg', 'Superpowers (pinned horizontal scroll)')}</div>'''))

P.append(sec('04', 'Website map', table(['Route', 'Page / anchor', 'Purpose'], [
 ['/', 'Landing (24 sections)', 'Story, product, business, earning, FAQ, download, contact'],
 ['#personal · #app · #virtual-id', 'Personal product', 'Superpowers, app tour, Virtual ID'],
 ['#cashback · #verify · #legacy', 'Earning &amp; trust', 'Cashback flow, verification, unlimited legacy'],
 ['#wallet · #chat', 'Pay &amp; talk', 'Pay to name@reid, chat and contact sharing'],
 ['#security · #sso', 'Security', 'SSO hub, Sign in with reID demo'],
 ['#corporate', 'reCorporate', 'Dashboard, roles, legal pathway, industries'],
 ['#ambassador · #ecosystem', 'Earn &amp; ecosystem', 'Storefront, process, industries orbit'],
 ['#faq · #download · #contact', 'Conversion', 'FAQ, app download, enquiry form'],
 ['/privacy · /terms · /cookies', 'Legal', 'Store-ready policies'],
 ['/delete-account · /support', 'Store requirements', 'Account deletion request, support contacts'],
 ['/404', 'Not found', 'Branded fallback'],
 ['/llms.txt · /llms-full.txt · /openapi.json', 'AI discovery', 'Summaries and API description for agents'],
 ['/sitemap.xml · /robots.txt · /.well-known/security.txt', 'Crawlers', 'Indexing and security contact']]) + '''
<p class="mute">Redirects: /privacy-policy, /terms-and-conditions, /cookie-policy, /account-deletion and /help point to the canonical pages.</p>'''))

P.append(sec('05', 'Hero, app tour & Virtual ID', f'''
<p>The hero shows a scan frame over the hero image; the beam reveals a verified-ID card. Chips and a watch card open the explainer. The app tour pins a phone while five steps swap screens with clip-path transitions (desktop) or a swipe row with IntersectionObserver (phones). The Virtual ID section tilts a holographic card and fans out card variants.</p>
<div class="grid g2">{shot('d-app.jpg', 'App tour — sticky phone, five screens')}{shot('d-virtual-id.jpg', 'Virtual ID — holo card and fan')}</div>
<div class="grid g2" style="margin-top:4mm">{shot('d-cashback.jpg', 'Cashback — coins flow from purchase to wallet')}{shot('d-verify.jpg', 'Verification — passport + liveness progress')}</div>'''))

P.append(sec('06', 'Legacy, pay to name@reid & chat', f'''
<p>The legacy canvas draws a growing network as you scroll; level counters run L1…L10 and then ∞ to show unlimited depth. The wallet section types <code>tomboy@reid</code> into a pay flow across three screens. The chat section pairs the wallet overview with a live reID Chat thread including contact sharing.</p>
<div class="grid g2">{shot('d-legacy.jpg', 'Legacy network — unlimited levels')}{shot('d-wallet.jpg', 'Pay to name@reid flow')}</div>
<div style="margin-top:4mm;width:60%">{shot('d-chat.jpg', 'reID Chat and contact sharing')}</div>'''))

P.append(sec('07', 'Security, SSO & Sign in with reID', f'''
<p>A hub animation shows reID as the single sign-on for the whole ecosystem: passkeys, device binding, encrypted storage, consent per app. The demo section lets visitors press a real-looking "Sign in with reID" button (with a tap hint) and watch the consent and success states — the same flow partners integrate via OAuth 2.0 / OpenID Connect.</p>
<div class="grid g2">{shot('d-security.jpg', 'Security & SSO hub')}{shot('d-sso.jpg', 'Sign in with reID demo')}</div>'''))

P.append(sec('08', 'reCorporate', f'''
<p>Built from the updated dashboard and role-management screenshots. A 3D-tilted, live dashboard (<code>#dash3d</code>) shows merchant identity, credential scan, cashback ticker, crypto network lines, legacy table and fiat marked "coming soon". Below it: versus tiles, a tabbed showcase (identity, roles, legacy, users, fiat, finance card), an onboarding flow line, steps, the legal pathway with QR, and industry chips.</p>
<div class="grid g2">{shot('d-corporate.jpg', 'reCorporate intro')}{shot('d-dash3d.jpg', 'Live animated dashboard')}</div>'''))

P.append(sec('09', 'Ambassador & ecosystem', f'''
<p>The Ambassador section sells the opportunity: personal storefront, earning tiles, and a horizontal five-step process (apply → verify → storefront → share → earn). The ecosystem section shows one reID connected to N industries in an orbit, with 1 / N / 0 stats (one identity, any number of industries, zero passwords).</p>
{shot('d-ambassador.jpg', 'Ambassador storefront and earning')}
<div class="grid g2" style="margin-top:4mm">{shot('d-timeline.jpg', 'Horizontal process timeline')}{shot('d-ecosystem.jpg', 'Industries ecosystem orbit')}</div>'''))

P.append(sec('10', 'Explainer video & player', f'''
<p>A 1:58 explainer rendered from HTML scenes (GSAP timeline, Playwright frames, ffmpeg). Narration by Kokoro TTS voice <code>af_heart</code> (the voice used for reMarketplace) over generated music with ducking. Chapters: intro, individual, privacy, freelancer, business, earn, features, call to action.</p>
<div class="grid g4">{shot('v-5.jpg')}{shot('v-20.jpg')}{shot('v-36.jpg')}{shot('v-52.jpg')}{shot('v-70.jpg')}{shot('v-90.jpg')}{shot('v-104.jpg')}{shot('v-114.jpg')}</div>
<h3>Player behaviour</h3><ul>
<li>First visit: pop-up after 3.2 s, muted with "Tap for sound"; remembered via <code>localStorage</code>.</li>
<li>Scroll, wheel or touch docks it as a mini player that keeps playing (YouTube style).</li>
<li>Controls: play, mute, expand, close, chapter-marked track; reopen button afterwards.</li></ul>
<div class="grid g2">{shot('d-popup.jpg', 'First-visit pop-up')}{shot('d-mini.jpg', 'Docked mini player')}</div>'''))

P.append(sec('11', 'Legal, support & account deletion', f'''
<p>Generated by <code>tools/build_legal.py</code> with a shared template: reading progress, pixel hero, active contents list, reveals. Entity: Desert Tech Cloud Services LLC. Updated 31 October 2026.</p>
''' + table(['Page', 'Store requirement covered'], [
 ['Privacy', 'Data categories, app permissions, no tracking / IDFA, providers, retention (deletion within 30 days, AML records ~5 years), GDPR / UK / CCPA / UAE PDPL rights, 18+'],
 ['Terms', 'Licence, acceptable use, Apple App Store and Google Play clauses'],
 ['Cookies', 'Essential and preference storage only, no ad cookies'],
 ['Delete account', 'In-app steps plus web request form (Google Play requirement)'],
 ['Support', 'support@, info@, privacy@, security@ contacts']]) + f'''
<div class="grid g3">{shot('d-privacy.jpg', 'Privacy')}{shot('d-delete.jpg', 'Account deletion')}{shot('d-support.jpg', 'Support')}</div>'''))

def ph(n, c=''):
    return f'<div><div class="phone" style="height:118mm"><img src="{img(n)}" style="height:100%;object-fit:cover;object-position:top"></div><div class="cap">{c}</div></div>'

P.append(sec('12', 'Design system & responsive', f'''
<div class="grid g2"><div>
<h3 style="margin-top:0">Tokens</h3>
<p><span class="sw" style="background:#0091FF"></span>Primary #0091FF &nbsp; <span class="sw" style="background:#0066CC"></span>Link #0066CC</p>
<p><span class="sw" style="background:#0B1220"></span>Ink #0B1220 &nbsp; <span class="sw" style="background:#5E6A7E"></span>Muted #5E6A7E</p>
<p><span class="sw" style="background:#F6F9FC"></span>Surface #F6F9FC &nbsp; <span class="sw" style="background:#C29A52"></span>Cashback gold</p>
<p>Type: Plus Jakarta Sans (display), IBM Plex Sans (body), IBM Plex Mono (labels) — all self-hosted.</p></div><div>
<h3 style="margin-top:0">Responsive rules</h3><ul>
<li>Breakpoints 1440 / 1024 / 760 / 390 px via <code>matchMedia</code>.</li>
<li>Phones: Apple-style swipe rows (<code>.m-snap</code>) for cards, steps, tour.</li>
<li>Heavy canvas effects skipped under 900 px; loader desktop-only.</li>
<li><code>prefers-reduced-motion</code> keeps all content visible.</li></ul></div></div>
<div class="grid g4" style="margin-top:3mm">{ph('m-hero.jpg', 'Hero')}{ph('m-everything.jpg', 'Everything')}{ph('m-app.jpg', 'App tour')}{ph('m-wallet.jpg', 'Pay')}</div>'''))

P.append(sec('13', 'SEO, sharing & AI discovery', table(['Area', 'Implemented'], [
 ['Metadata', 'Title, 151-char description, canonical, theme colour, per-page OG / Twitter'],
 ['Share images', 'og-home-v2 banner + one per legal page (1200×630)'],
 ['Icons', 'favicon.ico/svg, 16/32/48, Apple touch, 192/512 + maskable, web manifest'],
 ['Structured data', 'Organization, WebSite, SoftwareApplication, Service, VideoObject, FAQPage, BreadcrumbList'],
 ['Sitemap', 'Pages + image and video entries + llms files'],
 ['Share links', 'Footer: X, LinkedIn, WhatsApp, Telegram, Post on X, copy link'],
 ['AI crawlers', 'robots.txt explicitly allows GPTBot, OAI-SearchBot, ChatGPT-User, ClaudeBot, Claude-User, PerplexityBot, Google-Extended, Applebot-Extended, Bingbot, meta-externalagent, Amazonbot, MistralAI, cohere, CCBot and more'],
 ['AI agents', 'llms.txt / llms-full.txt summaries; openapi.json describes POST /api/contact (operation sendEnquiry, CORS enabled) so agents can submit enquiries'],
 ['Security', 'HSTS, nosniff, frame and referrer policies, permissions policy, security.txt'],
 ['Not done (by request)', 'Google Search Console submission; language switcher']]) + '''
<div class="note">Share previews need the og:image URL to resolve: connect <b>reidentity.net</b> in Vercel before sharing links. Links shared on the vercel.app address show the app icon instead of the banner.</div>'''))

P.append(sec('14', 'Testing & QA', table(['Page', 'Performance', 'Accessibility', 'Best practices', 'SEO'], [
 ['Home — desktop', '79–88', '97', '100', '100'],
 ['Home — mobile', '~54', '97', '100', '100'],
 ['Privacy / Terms / Cookies', '95–100', '100', '100', '100'],
 ['Delete account / Support', '95–100', '100', '100', '100']]) + table(['Check', 'Result'], [
 ['Crawl of 7 pages at 1440 / 820 / 390 px', '<span class="ok">Pass</span> — no console errors, no broken links, no horizontal scroll'],
 ['Phones 360 / 390 / 430 px (iOS Safari + Android Chrome profiles)', '<span class="ok">Pass</span> — stretched icons and SSO overflow fixed'],
 ['Reduced motion', '<span class="ok">Pass</span> — all content visible'],
 ['Sticky / pinned sections', '<span class="ok">Pass</span> — overflow-x:clip fix'],
 ['Contact API: validation, honeypot, 4000-char limit, CORS, OPTIONS 204', '<span class="ok">Pass</span>'],
 ['Account deletion form → /api/contact', '<span class="ok">Pass</span>'],
 ['Video pop-up, docking, chapters, reopen', '<span class="ok">Pass</span>'],
 ['Mobile page height', '42,480 → 31,257 px after swipe rows'],
 ['Mobile performance', '<span class="warn">Watch</span> — animation cost; see open items']]) + '<p class="mute">Lighthouse 12, headless Chrome, simulated throttling.</p>'))

P.append(sec('15', 'Developer handover', '''
<h3 style="margin-top:0">Run locally</h3>
<pre>git clone https://github.com/reIDentity/reID_Website.git
cd reID_Website && npm install
npm start            # http://localhost:3000</pre>
<h3>Deploy</h3><p>Vercel project linked to <code>main</code>; every push deploys. <code>vercel.json</code> holds clean URLs, headers, caching and redirects. <code>api/contact.js</code> runs as a serverless function.</p>
''' + table(['Env variable', 'Purpose'], [
 ['SMTP_HOST / SMTP_PORT / SMTP_USER / SMTP_PASS', 'Branded emails via nodemailer. If SMTP_HOST is unset, form relays via FormSubmit to info@reidentity.net'],
 ['MAIL_FROM / MAIL_TO', 'Sender and team inbox']]) + '''
<h3>Project structure</h3>
<pre>index.html  styles.css  screens.css  app.js        landing page
player.css  player.js                              explainer pop-up / mini player
legal.css  legal.js  tools/build_legal.py          legal pages (regenerate: python3 tools/build_legal.py)
api/contact.js  server.js                          enquiry API (Vercel + local)
assets/  vendor/ fonts/ img/ brand/ video/         static assets
tools/og.html  tools/og2.html                      share-image templates
video/  scenes.html render.js voice.py music.py    explainer pipeline (see video/README.md)
robots.txt sitemap.xml llms*.txt openapi.json      discovery files</pre>
<h3>Common edits</h3><ul>
<li>Copy: edit <code>index.html</code>; FAQ answers are mirrored in the FAQPage JSON-LD in the head.</li>
<li>Legal text: edit <code>PAGES</code> in <code>build_legal.py</code>, then rerun.</li>
<li>Video: edit the script in <code>video/voice.py</code>, run voice → music → render (README).</li></ul>'''))

P.append(sec('16', 'Open items', table(['#', 'Item', 'Owner'], [
 ['1', 'Connect reidentity.net domain in Vercel (needed for share previews and canonical URLs)', 'reID team'],
 ['2', 'Create mailboxes info@, support@, privacy@, legal@, security@reidentity.net', 'reID team'],
 ['3', 'Activate FormSubmit (one-time confirm email) or set SMTP env vars', 'reID team'],
 ['4', 'Legal review of Privacy, Terms, Cookies before store submission', 'Legal'],
 ['5', 'Add App Store / Google Play links when apps are published', 'Product'],
 ['6', 'Confirm Ambassador commission figures for the site copy', 'Business'],
 ['7', 'Mobile performance ~54: optional lighter animation set for low-end phones', 'Dev'],
 ['8', 'Search Console submission and translations — skipped by request, can be added later', 'Marketing']])))

P.append((None, 'Appendix — change log', '<h2>Appendix — change log</h2>' + table(['Commit', 'Change'], [
 ['0f6566a', 'New social share banner (og-home-v2)'],
 ['05e8d00', 'Mobile polish: swipe rows, iOS icon fix, SSO overflow, compact watch button, form relay + honeypot'],
 ['730c08f', 'QA pass: forms relay via FormSubmit, limits'],
 ['f0b4129', 'SEO, AI discovery, store-ready legal, account deletion, support, 404, headers, fonts, a11y'],
 ['00d2851', 'Explainer video + pop-up / mini player; security + SSO; tap hints; horizontal process; spacing'],
 ['1bb5343', 'Legacy network: unlimited levels'],
 ['ab0c6d0', 'Own legal pages; industries orbit'],
 ['fe2cc0a', 'Sticky app tour fix; number band; footer wordmark'],
 ['ca50755', 'Everything-in-one-passport section'],
 ['3c88f26', 'Motion rebuild: hero scan, app screens, Virtual ID, cashback, chat, pay flow, dashboard'],
 ['c518c30', 'First reID site for reidentity.net'],
 ['b80ce9b', 'Initial commit']]) + f'<div style="margin-top:6mm">{shot("d-footer.jpg", "Footer with share links and legal navigation")}</div>'))

toc = [(n or 'A', t, i + 3) for i, (n, t, _) in enumerate(P)]
open('/tmp/claude-0/report/delivery.html', 'w').write(build('reID Website — Delivery & Handover Report', DOC, cover, toc, P))
print('ok', len(P) + 2, 'pages')
