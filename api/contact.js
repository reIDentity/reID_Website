// POST /api/contact — sends the enquiry to the reID team and a confirmation to the sender.
// Env (Vercel → Settings → Environment Variables):
//   SMTP_HOST, SMTP_PORT (465|587), SMTP_USER, SMTP_PASS,
//   MAIL_FROM (e.g. "reID <info@reidentity.net>"), MAIL_TO (default info@reidentity.net)
const nodemailer = require('nodemailer');
const TEAM = process.env.MAIL_TO || 'info@reidentity.net';
const esc = s => String(s || '').replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));

function shell(title, body) {
  return `<!doctype html><html><body style="margin:0;background:#f3f6fa;font-family:-apple-system,Segoe UI,Roboto,Arial,sans-serif;color:#0d1422">
<table width="100%" cellpadding="0" cellspacing="0" style="padding:24px 12px"><tr><td align="center">
<table width="600" cellpadding="0" cellspacing="0" style="max-width:600px;width:100%;background:#fff;border:1px solid #dce3ed;border-radius:16px;overflow:hidden">
<tr><td style="background:#0091ff;color:#fff;padding:26px 28px;font-size:22px;font-weight:600">${esc(title)}</td></tr>
<tr><td style="padding:24px 28px;font-size:15px;line-height:1.6">${body}</td></tr>
<tr><td style="padding:18px 28px;background:#f3f6fa;color:#5d687b;font-size:12px">reID · Your digital identity passport · reidentity.net · Dubai, UAE</td></tr>
</table></td></tr></table></body></html>`;
}

module.exports = async (req, res) => {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
  if (req.method === 'OPTIONS') return res.status(204).end();
  if (req.method !== 'POST') return res.status(405).json({ error: 'Method not allowed' });
  const d = typeof req.body === 'string' ? JSON.parse(req.body || '{}') : (req.body || {});
  if (!d.name || !/^\S+@\S+\.\S+$/.test(d.email || '') || !d.message) return res.status(400).json({ error: 'Name, email and message are required.' });
  try {
    const t = nodemailer.createTransport({ host: process.env.SMTP_HOST, port: +(process.env.SMTP_PORT || 465), secure: +(process.env.SMTP_PORT || 465) === 465, auth: { user: process.env.SMTP_USER, pass: process.env.SMTP_PASS } });
    const from = process.env.MAIL_FROM || `reID <${TEAM}>`;
    const rows = [['Name', d.name], ['Email', d.email], ['Company', d.company], ['Topic', d.topic], ['Message', d.message]]
      .map(([k, v]) => `<p style="margin:0 0 12px"><b>${k}</b><br>${esc(v).replace(/\n/g, '<br>')}</p>`).join('');
    await t.sendMail({ from, to: TEAM, replyTo: d.email, subject: `reID enquiry: ${d.topic || 'General'} — ${d.name}`, html: shell('New website enquiry', rows) });
    await t.sendMail({ from, to: d.email, subject: 'We received your message — reID', html: shell('Thanks, ' + d.name.split(' ')[0], `<p>We received your message about <b>${esc(d.topic)}</b> and will reply within one business day.</p>${rows}`) });
    res.status(200).json({ ok: true });
  } catch (e) { console.error(e); res.status(500).json({ error: 'Mail failed' }); }
};
