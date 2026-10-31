"""Builds privacy.html, terms.html and cookies.html from one template. Run: python3 tools/build_legal.py"""
import html, os, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UPDATED = "31 October 2026"
ENTITY = "Desert Tech Cloud Services LLC"
EMAIL = "privacy@reidentity.net"

PAGES = {
 "privacy": ("Privacy Policy", "How reID collects, uses and protects your personal data.", [
  ("Who we are", f"<p>reID (\"reID\", \"we\", \"us\") is a digital identity platform operated by {ENTITY}, Dubai, United Arab Emirates. This policy explains how we handle personal data when you use the reID apps, reCorporate, Sign in with reID and reidentity.net (together, the \"Services\").</p>"),
  ("Data we collect", "<ul><li><b>Account data:</b> name, username (for example name@reid), email, phone number and profile details you choose to add.</li><li><b>Verification data:</b> identity document images, liveness checks and verification results, processed by our regulated KYC provider.</li><li><b>Wallet and transaction data:</b> wallet addresses, balances, transfers, cashback and legacy network activity.</li><li><b>Corporate data:</b> company details, employees, roles and permissions you add in reCorporate.</li><li><b>Device and usage data:</b> device type, app version, IP address, log and security events.</li><li><b>Communications:</b> messages you send to support and, if you use reID Chat, the messages you exchange.</li></ul>"),
  ("How we use your data", "<ul><li>To create and secure your reID and keep you signed in with passkeys, wallets or social accounts.</li><li>To verify your identity and meet anti-money-laundering and fraud-prevention duties.</li><li>To process payments, cashback, legacy rewards, Virtual IDs and virtual cards.</li><li>To let you share your verified profile and sign in to connected apps, only with your approval.</li><li>To improve the Services, provide support and send service messages.</li></ul>"),
  ("Sharing with connected apps", "<p>When you use Sign in with reID, the connected app only receives the details you approve on the consent screen, such as your name, email or verified status. You can review and remove connected apps at any time in Settings.</p>"),
  ("Who we share data with", "<ul><li>Regulated identity verification, payment, card-issuing and telecom partners that help deliver the Services.</li><li>Cloud hosting and security providers under contract and confidentiality obligations.</li><li>Authorities where the law requires it.</li></ul><p>We do not sell your personal data.</p>"),
  ("International transfers", "<p>Your data is primarily processed in the UAE. Where it is transferred abroad, we use safeguards required by applicable law, including the UAE Personal Data Protection Law.</p>"),
  ("How long we keep data", "<p>We keep personal data while your account is active and afterwards for as long as required to meet legal, regulatory and record-keeping obligations. Verification records may be retained for the period required by anti-money-laundering rules.</p>"),
  ("Your rights", "<p>Depending on where you live, you may have the right to access, correct, delete or export your data, restrict or object to processing, and withdraw consent. Contact us at <b>privacy@reidentity.net</b> to exercise these rights.</p>"),
  ("Security", "<p>We protect data with encryption in transit and at rest, passkey and biometric sign-in, access controls and continuous monitoring. Zero-knowledge verification lets apps confirm facts about you without seeing the underlying documents.</p>"),
  ("Children", "<p>The Services are not intended for children below the age required by local law to open an account. Family features such as Virtual IDs for family members are managed by the adult account holder.</p>"),
  ("Changes and contact", f"<p>We may update this policy and will notify you of material changes in the app or by email. Questions: <b>{EMAIL}</b>, {ENTITY}, Dubai, UAE.</p>"),
 ]),
 "terms": ("Terms of Service", "The rules for using reID, reCorporate and Sign in with reID.", [
  ("Agreement", f"<p>These terms form an agreement between you and {ENTITY} (\"reID\"). By creating a reID or using the Services you accept them. If you use reID on behalf of a company, you confirm you are authorised to bind it.</p>"),
  ("Your reID", "<ul><li>You must provide accurate information and keep your sign-in methods secure.</li><li>One person may hold one personal reID. Virtual IDs are linked to and controlled by your main reID.</li><li>You are responsible for activity under your account and Virtual IDs.</li></ul>"),
  ("Verification", "<p>Some features require identity verification. We may request documents, refuse or suspend verification, or limit features where required by law or our risk policies.</p>"),
  ("Wallet, payments and cards", "<ul><li>Payments to a username (name@reid) are sent to the wallet address shown at confirmation. Check details before you confirm; completed blockchain transfers cannot be reversed.</li><li>Fiat accounts, virtual cards and eSIMs are provided with regulated partners and may be subject to their terms and regional availability.</li><li>Fees, where they apply, are shown before you confirm.</li></ul>"),
  ("Cashback and legacy network", "<p>Cashback and legacy rewards are earned on eligible transactions as described in the app. We may change, suspend or end reward programs, and may withhold rewards obtained through fraud, abuse or self-referral.</p>"),
  ("reCorporate", "<p>Corporate account holders are responsible for the employees, roles and permissions they configure, for the accuracy of company data and for complying with employment and financial rules that apply to their business.</p>"),
  ("Sign in with reID for developers", "<p>Apps using Sign in with reID must request only the data they need, display a clear privacy policy, keep API keys secret and use reID data only for the purpose the user approved.</p>"),
  ("Ambassador Program", "<p>Ambassadors are independent partners, not employees. Participation requires approval, completion of the Academy and compliance with our marketing and conduct guidelines. Commissions are paid as described in the Ambassador portal.</p>"),
  ("Acceptable use", "<ul><li>No fraud, money laundering, sanctions evasion or illegal activity.</li><li>No impersonation, fake profiles or misuse of other people's data.</li><li>No attempts to break, scrape or reverse-engineer the Services.</li></ul>"),
  ("Suspension and closure", "<p>You can close your reID at any time. We may suspend or close accounts that breach these terms or where required by law. Some records are retained as described in the Privacy Policy.</p>"),
  ("Liability", "<p>The Services are provided as available. To the extent permitted by law, reID is not liable for indirect or consequential losses, or for losses caused by third-party networks, partners or incorrect details you enter.</p>"),
  ("Governing law and contact", f"<p>These terms are governed by the laws of the United Arab Emirates as applied in Dubai. Questions: <b>legal@reidentity.net</b>.</p>"),
 ]),
 "cookies": ("Cookie Policy", "What we store on your device when you use reidentity.net.", [
  ("What cookies are", "<p>Cookies and similar technologies (such as local storage) are small files a website stores on your device to remember information between visits.</p>"),
  ("What we use", "<div class=\"ck\"><div><b>Strictly necessary</b><span>Always on</span><p>Keep the site secure, remember your sign-in session on our web apps and protect forms from abuse.</p></div><div><b>Preferences</b><span>Optional</span><p>Remember choices such as language or display settings.</p></div><div><b>Analytics</b><span>Optional</span><p>Help us understand which pages are used so we can improve them. Only set with your consent.</p></div></div>"),
  ("Marketing website", "<p>The reidentity.net marketing site does not use advertising cookies and does not sell or share browsing data with advertisers.</p>"),
  ("Third parties", "<p>When you open the reID web app, Sign in with reID or a payment flow, our verification, payment and security partners may set cookies needed to deliver that service. Their use is governed by their own policies.</p>"),
  ("Managing cookies", "<p>You can block or delete cookies in your browser settings. Blocking strictly necessary cookies may stop some features, such as staying signed in, from working.</p>"),
  ("Contact", f"<p>Questions about this policy: <b>{EMAIL}</b>.</p>"),
 ]),
}

def slug(s): return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")

TPL = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{title} · reID</title>
<meta name="claude:viewport-fit-sides" content="cover">
<meta name="description" content="{desc}">
<link rel="canonical" href="https://reidentity.net/{key}">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:wght@400;500;600&display=swap">
<link rel="stylesheet" href="styles.css">
<link rel="stylesheet" href="legal.css">
</head>
<body class="legal-page">
<div class="lg-progress"><i id="lgBar"></i></div>
<header class="nav solid" id="nav"><div class="wrap nav-in">
  <a class="brand" href="index.html" aria-label="reID home"><img src="assets/logo-mark-text.svg" alt="reID" width="107" height="32"></a>
  <nav class="links" aria-label="Legal">{tabs}</nav>
  <a class="btn btn-blue sm nav-cta" href="index.html">Back to reID</a>
</div></header>
<main>
  <section class="lg-hero">
    <canvas id="lgPixels" aria-hidden="true"></canvas>
    <div class="wrap">
      <span class="kicker"><span class="px"><i></i><i></i><i></i><i></i></span>Legal</span>
      <h1 class="lg-title">{title}</h1>
      <p class="lead">{desc}</p>
      <div class="lg-meta"><span>Last updated {updated}</span><span>{entity}</span></div>
      <div class="lg-mobile-tabs">{mtabs}</div>
    </div>
  </section>
  <div class="wrap lg-body">
    <aside class="lg-toc"><b>On this page</b>{toc}</aside>
    <article class="lg-content">{sections}
      <p class="lg-note">This document is provided for information and should be reviewed by qualified legal counsel before publication.</p>
    </article>
  </div>
</main>
<footer><div class="wrap">
  <div class="fine" style="margin-top:0;border-top:0;padding-top:0"><span>© <span id="yr">2026</span> reidentity.net · reID</span><span><a href="privacy.html">Privacy</a> · <a href="terms.html">Terms</a> · <a href="cookies.html">Cookies</a></span></div>
</div></footer>
<script src="assets/vendor/gsap.min.js"></script>
<script src="assets/vendor/ScrollTrigger.min.js"></script>
<script src="legal.js"></script>
</body>
</html>
"""

for key, (title, desc, secs) in PAGES.items():
    tabs = "".join(f'<a href="{k}.html"{" class=\"on\"" if k == key else ""}>{v[0]}</a>' for k, v in PAGES.items())
    toc = "".join(f'<a href="#{slug(h)}"><i>{i:02d}</i>{html.escape(h)}</a>' for i, (h, _) in enumerate(secs, 1))
    sections = "".join(f'<section class="lg-sec" id="{slug(h)}"><span class="n">{i:02d}</span><h2>{html.escape(h)}</h2>{body}</section>' for i, (h, body) in enumerate(secs, 1))
    out = TPL.format(title=title, desc=desc, key=key, tabs=tabs, mtabs=tabs, toc=toc, sections=sections, updated=UPDATED, entity=ENTITY)
    open(os.path.join(ROOT, f"{key}.html"), "w").write(out)
    print("wrote", key)
