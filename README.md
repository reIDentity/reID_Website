# reID Website — reidentity.net

Light, single-page marketing site for **reID**: Personal, Legacy network, Wallet, Sign in with reID, reCorporate and the Ambassador Program.

## Stack
Static HTML/CSS/JS (`index.html`, `styles.css`, `app.js`) + one serverless function (`api/contact.js`). Node/Express `server.js` for local or VPS hosting.

```bash
npm install
npm start        # http://localhost:3000
```

## Deploy (Vercel)
Import the repo as a new project (framework: Other). Add env vars for the contact form:
`SMTP_HOST, SMTP_PORT, SMTP_USER, SMTP_PASS, MAIL_FROM, MAIL_TO`. Point `reidentity.net` to the project.

## Legal pages
`privacy.html`, `terms.html`, `cookies.html` are generated from `tools/build_legal.py` (edit the text there, then run `python3 tools/build_legal.py`). Have them reviewed by legal counsel before go-live.

## Assets
- `assets/img/` — paintings and app/reCorporate screens from the reID and reCorporate pitch decks (webp)
- `assets/sprite.svg` — reID pixel icon set (from `reIDentity/reid-icons`, recoloured to `currentColor`)
- `assets/levels/` — legacy level badges · `assets/qr-*.svg` — real QR codes for app/corporate URLs

## Before go-live
- App Store / Google Play URLs (`data-store` buttons in `index.html`)
- `REID_ISSUER` / SDK package name in the Sign in with reID snippet
- Ambassador commission figures (pending the ambassador pitch)
- Storefront domain shown in the sample (`ambassador.reidentity.net/alex`)
