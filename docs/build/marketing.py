from common import *

DOC = 'Product & Marketing Kit'

cover = f'''<section class="page cover"><div class="glow"></div><div class="dots"></div><div class="in">
<img class="logo" src="{LOGO}">
<div class="kick">MARKETING HANDOVER</div>
<h1>reID —<br><span>Product &amp; Marketing Kit</span></h1>
<div class="sub">Positioning, messages, audiences, ready-to-use copy, assets and a launch plan for reidentity.net and the reID app.</div>
<div class="hero"><img src="file://{ROOT}/assets/brand/og-home-v2.jpg"></div>
<div class="meta"><div><small>DATE</small><b>31 October 2026</b></div><div><small>WEBSITE</small><b>reidentity.net</b></div><div><small>PRODUCT</small><b>reID · reCorporate</b></div><div><small>OWNER</small><b>Desert Tech Cloud Services LLC</b></div></div>
</div></section>'''

P = []
P.append(sec('01', 'Product at a glance', f'''
<p class="lead"><b>reID is one secure digital identity for everything.</b> Sign in without passwords, verify once, pay and get paid to a simple name, chat with verified people, and earn cashback through a legacy network.</p>
<div class="grid g4" style="margin:5mm 0">
<div class="stat"><b>1</b><span>identity for every app and service</span></div>
<div class="stat"><b>0</b><span>passwords — passkey sign-in</span></div>
<div class="stat"><b>∞</b><span>legacy levels for cashback</span></div>
<div class="stat"><b>N</b><span>industries on one ecosystem</span></div></div>
{shot('d-hero.jpg', 'reidentity.net hero')}'''))

P.append(sec('02', 'Problem & answer', table(['The problem', 'The reID answer'], [
 ['Dozens of passwords, logins and resets', 'Passkey sign-in and SSO: one tap, every service'],
 ['Repeated KYC with every company', 'Verify once (passport + liveness), share proof with consent'],
 ['Long wallet addresses and bank details', 'Pay and get paid to <code>name@reid</code>'],
 ['Strangers and fake profiles in chats', 'reID Chat with verified people and contact sharing'],
 ['Loyalty points that expire', 'Real cashback, plus earnings from your legacy network'],
 ['Businesses running separate identity, staff and payout tools', 'reCorporate: company identity, roles, staff, payouts in one dashboard']]) +
 '<div class="callout"><b>One line:</b> Your identity, your login, your wallet and your network — in one passport.</div>'))

P.append(sec('03', 'Audiences', table(['Audience', 'Need', 'Lead message', 'CTA'], [
 ['Individuals', 'Simple, safe sign-in and payments', 'One identity. Zero passwords.', 'Create your reID'],
 ['Freelancers', 'Get paid fast, look trustworthy', 'Verified profile, paid to your name.', 'Create your reID'],
 ['Businesses / SMEs', 'Verified company, staff roles, payouts', 'The financial and workforce operating layer for modern businesses.', 'For businesses'],
 ['Developers / partners', 'Login + KYC without building it', 'Add Sign in with reID in an afternoon.', 'Contact us'],
 ['Ambassadors', 'Extra income', 'Grow the network. Earn as it grows.', 'Become an Ambassador']])))

P.append(sec('04', 'Positioning & key messages', '''
<h3 style="margin-top:0">Positioning statement</h3>
<p>For people and businesses who live online, <b>reID</b> is the digital identity passport that replaces passwords, repeated verification and long payment details with one secure, verified ID — and rewards you for using it.</p>
<h3>Taglines</h3>
<div><span class="pill">One identity for everything.</span><span class="pill">Sign in. Verify. Pay. Earn.</span><span class="pill">Never re-type a password again.</span><span class="pill">Pay to a name, not a long address.</span><span class="pill">Verified once. Trusted everywhere.</span><span class="pill">Every purchase pays you back.</span></div>
<h3>Message pillars</h3>''' + table(['Pillar', 'Proof points'], [
 ['Simple', 'Passkey login, one name for payments, one app'],
 ['Secure', 'Biometrics, device binding, encrypted data, consent per app, no ad tracking'],
 ['Verified', 'Passport + liveness, Virtual ID card, verified chat'],
 ['Rewarding', 'Cashback on purchases, unlimited legacy levels, Ambassador income'],
 ['For business', 'reCorporate dashboard, roles, staff, payouts, legal pathway']]) + '''
<h3>Tone</h3><p>Clear, calm, confident. Short sentences. Say what the user gets. No jargon (avoid "KYC" in headlines, "blockchain", "Web3").</p>'''))

P.append(sec('05', 'Capabilities', table(['Feature', 'What to say'], [
 ['Passkey sign-in / SSO', 'One tap with Face ID or fingerprint across the whole ecosystem'],
 ['Virtual ID', 'A verified digital ID card on your phone'],
 ['Verification', 'Passport + liveness once; share proof, not documents'],
 ['Wallet', 'Hold, send and receive; pay to name@reid'],
 ['Cashback', 'Money back on purchases into your wallet'],
 ['Legacy network', 'Invite people; earn from their activity across unlimited levels'],
 ['reID Chat', 'Message verified people, share contacts, pay in the same thread'],
 ['Sign in with reID', 'OAuth 2.0 / OpenID Connect for partner apps'],
 ['reCorporate', 'Company identity, roles, users, legacy payouts, fiat (coming soon) and crypto']]) +
 f'<div class="grid g2">{shot("d-everything.jpg", "Everything in one passport")}{shot("d-security.jpg", "Security & SSO")}</div>'))

P.append(sec('06', 'Offers', f'''
<div class="grid g3">
<div class="stat"><b style="font-size:14pt">reID Personal</b><span>Free app. Identity, wallet, chat, cashback, legacy.</span></div>
<div class="stat"><b style="font-size:14pt">reCorporate</b><span>Business dashboard: verified company, roles, staff, payouts.</span></div>
<div class="stat"><b style="font-size:14pt">Ambassador</b><span>Storefront and commissions through the network.</span></div></div>
<div class="note">Pricing and Ambassador commission figures are not published on the site yet. Confirm before using numbers in ads.</div>
<div class="grid g2">{shot("d-corporate.jpg", "reCorporate")}{shot("d-ambassador.jpg", "Ambassador")}</div>'''))

P.append(sec('07', 'Website tour for campaigns', table(['Link', 'Use for'], [
 ['reidentity.net', 'General awareness, bio links'],
 ['reidentity.net/#personal', 'Consumer ads'],
 ['reidentity.net/#wallet', 'Pay-to-name campaigns'],
 ['reidentity.net/#security', 'Security / passwordless messaging'],
 ['reidentity.net/#corporate', 'B2B outreach, LinkedIn'],
 ['reidentity.net/#ambassador', 'Recruitment of Ambassadors'],
 ['reidentity.net/#contact', 'Lead capture'],
 ['reidentity.net/support', 'Customer help']]) +
 '<p class="mute">Add UTM tags to every campaign link, e.g. <code>?utm_source=linkedin&amp;utm_medium=post&amp;utm_campaign=launch</code>.</p>' +
 f'<div class="grid g2">{shot("d-app.jpg", "App tour")}{shot("d-wallet.jpg", "Pay to name@reid")}</div>'))

P.append(sec('08', 'Lead capture & explainer', f'''
<p>The contact form (name, email, company, topic, message) posts to <code>/api/contact</code> and lands in <b>info@reidentity.net</b>. Topics route enquiries: Personal, Business, Ambassador, Partner, Press, Other. AI agents can submit the same enquiry via the published OpenAPI file.</p>
<p>The 1:58 explainer opens on first visit and docks into a mini player. Use it as the hero asset for social: cut chapters into 15–30 s clips (individual, freelancer, business, earn).</p>
<div class="grid g2">{shot("d-contact.jpg", "Contact form")}{shot("d-popup.jpg", "Explainer pop-up")}</div>
<div class="grid g4" style="margin-top:4mm">{shot("v-20.jpg", "Individuals")}{shot("v-52.jpg", "Freelancers")}{shot("v-70.jpg", "Business")}{shot("v-90.jpg", "Earn")}</div>'''))

P.append(sec('09', 'Brand & asset kit', f'''
<div class="grid g2"><div>
<h3 style="margin-top:0">Colours</h3>
<p><span class="sw" style="background:#0091FF"></span>reID Blue #0091FF</p><p><span class="sw" style="background:#0058D6"></span>Deep Blue #0058D6</p>
<p><span class="sw" style="background:#0B1220"></span>Ink #0B1220</p><p><span class="sw" style="background:#F6F9FC"></span>Surface #F6F9FC</p><p><span class="sw" style="background:#C29A52"></span>Cashback Gold #C29A52</p>
<h3>Type</h3><p>Plus Jakarta Sans · IBM Plex Sans · IBM Plex Mono</p>
<h3>Rules</h3><ul><li>Light backgrounds; blue as accent.</li><li>Write "reID" (lower-case re, capital ID).</li><li>Show real app screens, not stock phones.</li></ul></div><div>
<h3 style="margin-top:0">Files in the repo</h3>''' + table(['Asset', 'Path'], [
 ['Logo', 'assets/logo-mark-text.svg, logo.svg'],
 ['Share banner', 'assets/brand/og-home-v2.jpg'],
 ['App icons', 'assets/brand/icon-512.png'],
 ['App screens', 'assets/img/scr-*.webp'],
 ['Explainer', 'assets/video/reid-explainer.mp4'],
 ['QR codes', 'assets/qr-app.svg, qr-corporate.svg']]) + f'''</div></div>
<div class="shot" style="margin-top:2mm"><img src="file://{ROOT}/assets/brand/og-home-v2.jpg"></div><div class="cap">Social share banner (1200×630)</div>'''))

P.append(sec('10', 'Ready-to-use copy', '''
<h3 style="margin-top:0">LinkedIn — launch</h3>
<pre>Meet reID — one identity for everything.
Sign in without passwords. Verify once. Get paid to your name@reid.
Chat with verified people and earn cashback as your network grows.
For people, freelancers and businesses.
Watch the 2-min explainer → reidentity.net</pre>
<h3>X / Threads</h3>
<pre>One identity. Zero passwords. Pay to a name, not an address.
reID is live → reidentity.net</pre>
<h3>Instagram / TikTok caption</h3>
<pre>Stop re-typing passwords. Stop sending long wallet addresses.
One reID does it all — sign in, verify, pay, chat, earn. 🔐
Link in bio: reidentity.net</pre>
<h3>B2B email</h3>
<pre>Subject: Verified company identity, staff roles and payouts in one place

Hi {name},
reCorporate gives your business a verified identity, role-based staff access,
and payouts to name@reid — from one dashboard.
2-minute overview: reidentity.net/#corporate
Happy to show you a live demo this week.</pre>
<h3>Ambassador recruitment</h3>
<pre>Grow the network. Earn as it grows.
Get your own reID storefront, share it, and earn from every level of your network.
Apply → reidentity.net/#ambassador</pre>
<h3>WhatsApp broadcast</h3>
<pre>reID is here: one secure ID to sign in, verify, pay and earn. 2-min video: reidentity.net</pre>'''))

P.append(sec('11', 'Objections & FAQ', table(['Question / objection', 'Answer'], [
 ['Is my data safe?', 'Biometrics stay on your device; data is encrypted; apps only get what you approve. No ad tracking.'],
 ['Why verify my passport?', 'Once verified, you never upload documents again; partners get proof, not copies.'],
 ['What if I lose my phone?', 'Recover your reID on a new device with verification; old devices can be removed.'],
 ['Is the legacy network a scheme?', 'Earnings come from real activity and purchases, not sign-up fees.'],
 ['How do I delete my account?', 'In the app or at reidentity.net/delete-account; data removed within 30 days except legally required records.'],
 ['Can my business use it?', 'Yes — reCorporate adds company identity, roles, staff and payouts.'],
 ['Can my app add Sign in with reID?', 'Yes, via OAuth 2.0 / OpenID Connect. Contact us for keys.']])))

P.append(sec('12', 'Discoverability', table(['Channel', 'Status'], [
 ['Search engines', 'Full metadata, structured data, sitemap. Search Console submission not done (by request).'],
 ['AI assistants', 'ChatGPT, Claude, Perplexity, Gemini, Copilot, Apple and Meta crawlers allowed; llms.txt + llms-full.txt published'],
 ['AI agents', 'openapi.json lets agents send enquiries on a user\'s behalf'],
 ['Social sharing', 'Banner, titles and descriptions per page; share buttons in footer'],
 ['App stores', 'Privacy, Terms, Cookies, Delete account and Support URLs ready for listings']]) +
 '<div class="note">Connect <b>reidentity.net</b> in Vercel before sharing. Links on the vercel.app address show the app icon instead of the banner in WhatsApp and LinkedIn.</div>'))

P.append(sec('13', 'Launch plan & KPIs', table(['Week', 'Actions'], [
 ['0 — prep', 'Connect domain, mailboxes, test form, legal sign-off, cut 4 video clips'],
 ['1 — launch', 'LinkedIn + X + Instagram posts, WhatsApp broadcast, founder post, Ambassador briefing'],
 ['2 — B2B', 'reCorporate email to 50 target companies, LinkedIn outreach, demo calls'],
 ['3 — ambassadors', 'Ambassador recruitment push, storefront examples, referral contest'],
 ['4 — review', 'Read KPIs, refresh ad copy, add app-store links when live']]) +
 table(['KPI', 'Target (first 30 days)'], [
 ['Website visitors', 'Set baseline in week 1'],
 ['Explainer completion rate', '≥ 35%'],
 ['Contact enquiries', 'Track per topic'],
 ['Ambassador applications', 'Track weekly'],
 ['reCorporate demos booked', 'Track weekly'],
 ['App sign-ups (when live)', 'Track from store consoles']])))

P.append(sec('14', "Do's & don'ts", '''<div class="grid g2"><div><h3 style="margin-top:0" class="ok">Do</h3><ul>
<li>Lead with the benefit: no passwords, pay to a name, verified once.</li>
<li>Use real app screens and the explainer.</li>
<li>Say "unlimited levels" for the legacy network.</li>
<li>Link to reidentity.net with UTM tags.</li>
<li>Keep the light, blue look.</li></ul></div><div>
<h3 style="margin-top:0" class="warn">Don't</h3><ul>
<li>Mention reAED or other ReSystem products in reID campaigns.</li>
<li>Promise fixed earnings or returns.</li>
<li>Publish commission numbers before they are confirmed.</li>
<li>Use dark themes or stock hand-holding-phone photos.</li>
<li>Share the vercel.app link publicly.</li></ul></div></div>
<div class="callout" style="margin-top:6mm"><b>Contacts:</b> info@reidentity.net · support@reidentity.net · privacy@reidentity.net · security@reidentity.net</div>'''))

toc = [(n, t, i + 3) for i, (n, t, _) in enumerate(P)]
open('/tmp/claude-0/report/marketing.html', 'w').write(build('reID — Product & Marketing Kit', DOC, cover, toc, P))
print('ok')
