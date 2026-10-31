// Local / Node hosting. On Vercel the static files are served directly and /api/contact runs as a function.
const express = require('express');
const path = require('path');
const contact = require('./api/contact');
const app = express();
app.use(express.json({ limit: '50kb' }));
app.post('/api/contact', (req, res) => contact(req, res));
app.use(express.static(__dirname, { extensions: ['html'], index: 'index.html' }));
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`reID site → http://localhost:${PORT}`));
