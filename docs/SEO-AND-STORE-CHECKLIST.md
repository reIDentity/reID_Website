# reidentity.net — SEO, AI discovery and app-store readiness (31 Oct 2026)

## Lighthouse (local, before CDN compression)
| Page | Performance | Accessibility | Best practices | SEO |
|---|---|---|---|---|
| Home — desktop | 79–88 | 97 | 100 | 100 |
| Home — mobile | ~55 (heavy animation) | 97 | 100 | 100 |
| Legal / support pages — mobile | 95–99 | 100 | 100 | 100 |

Mobile home performance is limited by the amount of scroll animation (GSAP, canvases). Vercel adds Brotli/gzip and edge caching, which lifts real-world scores.

## Done
- Titles, meta descriptions (≤160 chars), canonical URLs, robots meta, one H1 per page, correct heading order, alt text on every image, width/height on images.
- Open Graph + Twitter cards with a dedicated 1200×630 image per page (`assets/brand/og-*.jpg`), video OG tag for the explainer.
- Structured data: Organization, WebSite (+ Register / Communicate / Watch actions), SoftwareApplication, Service (reCorporate), VideoObject, FAQPage; BreadcrumbList on every legal page.
- Icons: favicon.ico (16/32/48), favicon.svg, apple-touch-icon (180), PWA icons 192/512 + maskable; `site.webmanifest`.
- `sitemap.xml` (with image + video entries), `robots.txt`, `/.well-known/security.txt`, branded `404.html`.
- Self-hosted fonts (no Google Fonts request), responsive `srcset` images, hero image preload, loader skipped on phones.
- Security headers and caching in `vercel.json` (HSTS, nosniff, referrer policy, permissions policy); redirects for old legal URLs.
- Share links: X, LinkedIn, WhatsApp, Telegram, copy link.

## AI assistants and agents
- `robots.txt` explicitly allows GPTBot, OAI-SearchBot, ChatGPT-User, ClaudeBot, Claude-User, Claude-SearchBot, PerplexityBot, Google-Extended, Applebot(-Extended), Bingbot, Amazonbot, meta-externalagent, DuckAssistBot, MistralAI-User, cohere-ai, YouBot, CCBot.
- `llms.txt` (summary + key links) and `llms-full.txt` (complete product description, use cases, how an agent can help a user).
- `openapi.json`: public action for agents — `POST /api/contact` (enquiry, demo, Ambassador interest, account deletion), CORS enabled.
- `<link rel="alternate">` from the home page to `llms.txt` and `openapi.json`.

## App Store / Google Play
- Privacy Policy covers the iOS and Android apps: data categories (maps to Apple privacy labels and Google Data safety), app permissions (camera, biometrics, photos, notifications, contacts, location), no cross-app tracking or advertising IDs, service providers, retention, account deletion, rights (GDPR, UK, California, UAE PDPL), 18+.
- Account deletion page with in-app steps and a web request form (Google Play requires a web deletion URL): https://reidentity.net/delete-account
- Support URL (App Store requires one): https://reidentity.net/support
- Terms include the mobile app licence, Apple App Store minimum EULA terms and Google Play terms.
- URLs for the store listings: Privacy https://reidentity.net/privacy · Support https://reidentity.net/support · Account deletion https://reidentity.net/delete-account

## Still to do before launch
- Have counsel review the legal text (drafted for reID, UAE law).
- Set up the mailboxes used on the site: info@, support@, privacy@, legal@, security@reidentity.net.
- Add the App Store and Google Play links when the apps are live (`data-store` buttons).
- Set SMTP env vars in Vercel so the contact and deletion forms send email.
