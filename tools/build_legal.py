"""Builds privacy.html, terms.html and cookies.html from one template. Run: python3 tools/build_legal.py"""
import html, os, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UPDATED = "31 October 2026"
ENTITY = "Desert Tech Cloud Services LLC"
EMAIL = "privacy@reidentity.net"

PAGES = {
 "privacy": ("Privacy Policy", "How reID collects, uses and protects your personal data on our website and mobile apps.", "og-privacy", [
  ("Who we are", f"<p>reID (\"reID\", \"we\", \"us\") is a digital identity platform operated by {ENTITY}, Dubai, United Arab Emirates. This policy covers the reID mobile apps for iOS and Android, the reID web app, reCorporate, Sign in with reID and reidentity.net (together, the \"Services\").</p><p>Questions about privacy: <b>{EMAIL}</b>.</p>"),
  ("Data we collect", "<div class=\"dt\"><div><b>Contact info</b><p>Name, email address, phone number.</p></div><div><b>Identifiers</b><p>reID username (for example name@reid), user ID, device ID used for security.</p></div><div><b>Identity verification</b><p>Document images, selfie and liveness results, verification status.</p></div><div><b>Financial info</b><p>Wallet addresses, balances, transfers, cashback, card and account references from our partners.</p></div><div><b>User content</b><p>Profile details, photos you upload, reID Chat messages, support requests.</p></div><div><b>Usage and diagnostics</b><p>App interactions, crash logs, performance data, IP address.</p></div><div><b>Corporate data</b><p>Company details, employees, roles and permissions added in reCorporate.</p></div><div><b>Contacts (optional)</b><p>Only if you allow it, to find people you know on reID.</p></div></div><p>We collect this data directly from you, from your device, and from verification and payment partners that act for us.</p>"),
  ("How we use your data", "<ul><li>To create and secure your reID and keep you signed in with passkeys, wallets or social accounts.</li><li>To verify your identity and meet anti-money-laundering, sanctions and fraud-prevention duties.</li><li>To process payments, cashback, legacy rewards, Virtual IDs, virtual cards and eSIMs.</li><li>To let you share your verified profile and sign in to connected apps, only with your approval.</li><li>To provide support, send service messages and notifications you have turned on.</li><li>To keep the Services safe and improve them using aggregated diagnostics.</li></ul>"),
  ("App permissions", "<p>The mobile apps ask for permissions only when a feature needs them. You can change them at any time in your device settings.</p><div class=\"dt\"><div><b>Camera</b><p>Scan your ID document, take a verification selfie and scan reID QR codes.</p></div><div><b>Face ID, Touch ID or fingerprint</b><p>Unlock the app and approve sign-ins. Biometric data stays on your device and is never sent to us.</p></div><div><b>Photos</b><p>Choose a profile picture or upload a document.</p></div><div><b>Notifications</b><p>Payment alerts, sign-in approvals and chat messages.</p></div><div><b>Contacts</b><p>Optional. Find friends who already use reID.</p></div><div><b>Location</b><p>Optional. Approximate region for eSIM and local services. We do not track your location in the background.</p></div></div>"),
  ("Tracking and advertising", "<p>reID does not track you across apps and websites owned by other companies, does not use advertising identifiers (IDFA or Android Advertising ID) and does not sell or share your personal data for targeted advertising.</p>"),
  ("Sharing with connected apps", "<p>When you use Sign in with reID, a connected app only receives the details you approve on the consent screen, such as your name, email or verified status. You can review and remove connected apps at any time in Settings.</p>"),
  ("Service providers", "<p>We share data only with providers that help us run the Services, under contract and confidentiality obligations:</p><ul><li>Identity verification (KYC/KYB) providers.</li><li>Payment, banking, card-issuing and eSIM partners.</li><li>Cloud hosting, security and email providers.</li><li>Push notification services (Apple Push Notification service and Firebase Cloud Messaging).</li><li>Crash reporting and privacy-preserving analytics.</li></ul><p>We also share data with authorities where the law requires it. We do not sell your personal data.</p>"),
  ("International transfers", "<p>Your data is primarily processed in the UAE. Where it is transferred abroad, we use safeguards required by applicable law, including the UAE Personal Data Protection Law and, where they apply, the GDPR and UK GDPR.</p>"),
  ("Security", "<p>Data is encrypted in transit (TLS) and at rest. We use passkeys and biometric sign-in, access controls, monitoring and regular security reviews. Zero-knowledge verification lets apps confirm facts about you without seeing the underlying documents.</p>"),
  ("Retention and account deletion", "<p>We keep personal data while your account is active. You can delete your account at any time in the app (<b>Settings → Account → Delete account</b>) or on our <a href=\"delete-account.html\">account deletion page</a>.</p><p>When you delete your account we remove your profile, contacts, chat history and connected-app permissions within 30 days. Records we must keep by law, such as verification and transaction records under anti-money-laundering rules, are retained for the required period (usually five years) and then deleted.</p>"),
  ("Your rights", "<p>Depending on where you live, you may have the right to access, correct, delete or export your data, restrict or object to processing, and withdraw consent. Residents of California have the right to know, delete and correct personal information and to opt out of its sale or sharing; we do not sell or share personal information. Contact <b>privacy@reidentity.net</b> to exercise your rights. We respond within 30 days.</p>"),
  ("Children", "<p>reID is a financial and identity service for adults. You must be 18 or older to create an account, and we do not knowingly collect data from children. Family features such as Virtual IDs for family members are created and controlled by the adult account holder.</p>"),
  ("Changes and contact", f"<p>We will post updates here and notify you in the app or by email before material changes take effect.</p><p><b>{ENTITY}</b>, Dubai, United Arab Emirates · <b>{EMAIL}</b></p>"),
 ]),
 "terms": ("Terms of Service", "The rules for using the reID apps, reCorporate and Sign in with reID.", "og-terms", [
  ("Agreement", f"<p>These terms form an agreement between you and {ENTITY} (\"reID\"). They apply to the reID mobile apps, the web app, reCorporate and Sign in with reID (the \"Services\"). By creating a reID or using the Services you accept them. If you use reID for a company, you confirm you can bind it.</p>"),
  ("Eligibility and your reID", "<ul><li>You must be 18 or older and able to enter a binding contract.</li><li>Provide accurate information and keep your device, passkeys and recovery methods secure.</li><li>One person may hold one personal reID. Virtual IDs are linked to and controlled by your main reID.</li><li>You are responsible for activity under your account and Virtual IDs.</li></ul>"),
  ("Verification", "<p>Some features require identity verification. We may request documents, refuse or suspend verification, or limit features where required by law or our risk policies.</p>"),
  ("Wallet, payments, cards and eSIM", "<ul><li>Payments to a username (name@reid) go to the wallet address shown at confirmation. Check the details first: completed blockchain transfers cannot be reversed.</li><li>Fiat accounts, virtual cards and eSIMs are provided with regulated partners and may be subject to their terms and regional availability.</li><li>Fees, where they apply, are shown before you confirm.</li><li>reID does not give investment, tax or legal advice.</li></ul>"),
  ("Cashback and legacy network", "<p>Cashback and legacy rewards are earned on eligible transactions as described in the app. Rewards apply across unlimited legacy levels under the program rules shown in the app. We may change, suspend or end reward programs, and may withhold rewards obtained through fraud, abuse or self-referral.</p>"),
  ("reCorporate and developers", "<p>Corporate account holders are responsible for the employees, roles and permissions they configure and for complying with the employment and financial rules that apply to them. Apps using Sign in with reID must request only the data they need, publish a privacy policy, keep API keys secret and use reID data only for the purpose the user approved.</p>"),
  ("Ambassador Program", "<p>Ambassadors are independent partners, not employees. Participation requires approval, completion of the Academy and compliance with our marketing and conduct guidelines. Commissions are paid as described in the Ambassador portal.</p>"),
  ("Acceptable use", "<ul><li>No fraud, money laundering, sanctions evasion or illegal activity.</li><li>No impersonation, fake profiles, spam or misuse of other people's data.</li><li>No attempts to break, scrape, overload or reverse-engineer the Services.</li></ul>"),
  ("Mobile app licence", "<p>We grant you a personal, non-transferable, non-exclusive licence to use the reID app on devices you own or control, under these terms and the rules of the store you downloaded it from. App updates may be required to keep using some features.</p>"),
  ("Apple App Store terms", "<p>If you downloaded the app from the Apple App Store: these terms are between you and reID, not Apple. Apple has no obligation to provide maintenance or support for the app. If the app fails to conform to any applicable warranty, you may notify Apple, and Apple will refund the purchase price, if any; to the maximum extent permitted by law Apple has no other warranty obligation. reID, not Apple, is responsible for addressing claims relating to the app, including product liability, legal or regulatory compliance and intellectual property claims. You confirm you are not located in a country subject to a U.S. Government embargo and are not on any U.S. Government list of prohibited or restricted parties. Apple and its subsidiaries are third-party beneficiaries of these terms and may enforce them against you.</p>"),
  ("Google Play terms", "<p>If you downloaded the app from Google Play, the Google Play Terms of Service also apply to your use of the store. These terms are between you and reID, and Google is not responsible for the app or its content.</p>"),
  ("Suspension and closure", "<p>You can close your reID at any time from the app or our <a href=\"delete-account.html\">account deletion page</a>. We may suspend or close accounts that breach these terms or where required by law.</p>"),
  ("Liability", "<p>The Services are provided as available. To the extent permitted by law, reID is not liable for indirect or consequential losses, or for losses caused by third-party networks, partners or incorrect details you enter.</p>"),
  ("Governing law and contact", "<p>These terms are governed by the laws of the United Arab Emirates as applied in Dubai. Questions: <b>legal@reidentity.net</b>.</p>"),
 ]),
 "cookies": ("Cookie Policy", "What we store on your device when you use reidentity.net and the reID web app.", "og-cookies", [
  ("What cookies are", "<p>Cookies and similar technologies (such as local storage) are small files a website stores on your device to remember information between visits. The reID mobile apps do not use browser cookies; app data is covered by our <a href=\"privacy.html\">Privacy Policy</a>.</p>"),
  ("What we use", "<div class=\"ck\"><div><b>Strictly necessary</b><span>Always on</span><p>Keep the site secure, remember your sign-in session on our web apps and protect forms from abuse.</p></div><div><b>Preferences</b><span>Optional</span><p>Remember choices such as whether you have already watched the explainer video.</p></div><div><b>Analytics</b><span>Optional</span><p>Help us understand which pages are used so we can improve them. Only set with your consent.</p></div></div>"),
  ("Marketing website", "<p>reidentity.net does not use advertising cookies and does not sell or share browsing data with advertisers.</p>"),
  ("Third parties", "<p>When you open the reID web app, Sign in with reID or a payment flow, our verification, payment and security partners may set cookies needed to deliver that service. Their use is governed by their own policies.</p>"),
  ("Managing cookies", "<p>You can block or delete cookies in your browser settings. Blocking strictly necessary cookies may stop features such as staying signed in from working.</p>"),
  ("Contact", f"<p>Questions about this policy: <b>{EMAIL}</b>.</p>"),
 ]),
 "delete-account": ("Delete your account", "How to delete your reID account and what happens to your data.", "og-delete", [
  ("Delete in the app", "<ol class=\"steps-ol\"><li>Open the reID app and sign in.</li><li>Go to <b>Settings → Account → Delete account</b>.</li><li>Confirm with your passkey or biometrics.</li></ol><p>Withdraw any remaining balance first. Pending payments, cards and eSIMs are closed as part of deletion.</p>"),
  ("Request deletion online", "<p>Can't access the app? Send a request below using the email linked to your reID. We'll verify it's you before deleting anything.</p><form class=\"lg-form\" id=\"delForm\" novalidate><label><span>Email on your reID</span><input id=\"d-email\" type=\"email\" required autocomplete=\"email\"></label><label><span>reID username (optional)</span><input id=\"d-user\" placeholder=\"name@reid\"></label><label class=\"full\"><span>Anything we should know (optional)</span><textarea id=\"d-note\"></textarea></label><div class=\"full row\"><button class=\"btn btn-blue\" type=\"submit\" id=\"d-submit\">Request account deletion</button><span class=\"mute\" style=\"font-size:14px\">Or email privacy@reidentity.net</span></div><div class=\"form-msg\" id=\"d-out\" hidden></div></form>"),
  ("What we delete", "<ul><li>Your profile, photos and Virtual IDs.</li><li>Contacts, reID Chat history and connected-app permissions.</li><li>Notification and device settings.</li></ul><p>This happens within 30 days of confirming your request.</p>"),
  ("What we keep, and for how long", "<p>The law requires us to keep some records after you leave, such as identity verification results and transaction history for anti-money-laundering purposes. We keep these for the required period (usually five years), restrict access to them, and then delete them.</p>"),
  ("Corporate accounts", "<p>reCorporate accounts are deleted by an account owner from <b>Settings → Company → Close account</b>, or by emailing <b>privacy@reidentity.net</b> from the owner's address.</p>"),
 ]),
 "support": ("Support", "Help with your reID, wallet, Virtual ID, reCorporate and Sign in with reID.", "og-support", [
  ("Contact support", "<div class=\"dt\"><div><b>Email</b><p>support@reidentity.net · we reply within one business day.</p></div><div><b>In the app</b><p>Settings → Help &amp; support → Chat with us.</p></div><div><b>Business and partnerships</b><p>info@reidentity.net</p></div><div><b>Privacy and data requests</b><p>privacy@reidentity.net</p></div></div>"),
  ("Account and sign-in", "<ul><li><b>Lost your phone?</b> Sign in on a new device with your passkey, wallet or social account, then remove the old device in Settings → Security.</li><li><b>Can't verify?</b> Use good lighting, a valid passport and remove phone cases that cover the camera.</li><li><b>Want to leave?</b> See <a href=\"delete-account.html\">delete your account</a>.</li></ul>"),
  ("Payments and wallet", "<ul><li>Payments to name@reid go to the address shown when you confirm. Blockchain transfers can't be reversed, so check before you send.</li><li>Cashback appears in Wallet → Cashbacks and can be claimed at any time.</li><li>Report an unauthorised payment immediately at support@reidentity.net.</li></ul>"),
  ("Virtual ID, cards and eSIM", "<ul><li>Freeze a virtual card instantly from the card screen.</li><li>eSIMs are installed from Virtual ID → eSIM and work on eSIM-compatible phones.</li></ul>"),
  ("Report a security issue", "<p>Found a vulnerability? Email <b>security@reidentity.net</b>. Please don't share details publicly until we've fixed it.</p>"),
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
<meta name="robots" content="index,follow">
<meta property="og:type" content="article"><meta property="og:site_name" content="reID">
<meta property="og:url" content="https://reidentity.net/{key}"><meta property="og:title" content="{title} · reID"><meta property="og:description" content="{desc}">
<meta property="og:image" content="https://reidentity.net/assets/brand/{og}.jpg"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@Reidentity_net"><meta name="twitter:image" content="https://reidentity.net/assets/brand/{og}.jpg">
<meta name="theme-color" content="#ffffff">
<link rel="icon" href="favicon.ico" sizes="48x48"><link rel="icon" href="favicon.svg" type="image/svg+xml"><link rel="apple-touch-icon" href="apple-touch-icon.png"><link rel="manifest" href="site.webmanifest">
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{{"@type":"ListItem","position":1,"name":"reID","item":"https://reidentity.net/"}},{{"@type":"ListItem","position":2,"name":"{title}","item":"https://reidentity.net/{key}"}}]}}</script>
<link rel="stylesheet" href="fonts.css">
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
      <span class="kicker"><span class="px"><i></i><i></i><i></i><i></i></span>{kick}</span>
      <h1 class="lg-title">{title}</h1>
      <p class="lead">{desc}</p>
      <div class="lg-meta"><span>Last updated {updated}</span><span>{entity}</span></div>
      <div class="lg-mobile-tabs">{mtabs}</div>
    </div>
  </section>
  <div class="wrap lg-body">
    <aside class="lg-toc"><b>On this page</b>{toc}</aside>
    <article class="lg-content">{sections}
      
    </article>
  </div>
</main>
<footer><div class="wrap">
  <div class="fine" style="margin-top:0;border-top:0;padding-top:0"><span>© <span id="yr">2026</span> reidentity.net · reID</span><span><a href="privacy.html">Privacy</a> · <a href="terms.html">Terms</a> · <a href="cookies.html">Cookies</a> · <a href="delete-account.html">Delete account</a> · <a href="support.html">Support</a></span></div>
</div></footer>
<script src="assets/vendor/gsap.min.js"></script>
<script src="assets/vendor/ScrollTrigger.min.js"></script>
<script src="legal.js"></script>
</body>
</html>
"""

for key, (title, desc, og, secs) in PAGES.items():
    tabs = "".join(f'<a href="{k}.html"{" class=\"on\"" if k == key else ""}>{v[0].replace("Delete your account","Delete account")}</a>' for k, v in PAGES.items())
    toc = "".join(f'<a href="#{slug(h)}"><i>{i:02d}</i>{html.escape(h)}</a>' for i, (h, _) in enumerate(secs, 1))
    sections = "".join(f'<section class="lg-sec" id="{slug(h)}"><span class="n">{i:02d}</span><h2>{html.escape(h)}</h2>{body}</section>' for i, (h, body) in enumerate(secs, 1))
    out = TPL.format(og=og, kick=("Help" if key in ("support","delete-account") else "Legal"), title=title, desc=desc, key=key, tabs=tabs, mtabs=tabs, toc=toc, sections=sections, updated=UPDATED, entity=ENTITY)
    open(os.path.join(ROOT, f"{key}.html"), "w").write(out)
    print("wrote", key)
