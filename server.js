// Local / Node hosting. On Vercel the static files are served directly and /api/contact runs as a function.
const express = require('express');
const compression = require('compression');
const path = require('path');
const contact = require('./api/contact');
const app = express();
app.use(compression());
app.use(express.json({ limit: '50kb' }));
app.all('/api/contact', (req, res) => contact(req, res));
app.use(express.static(__dirname, { extensions: ['html'], index: 'index.html', dotfiles: 'allow' }));
app.use((req, res) => res.status(404).sendFile(path.join(__dirname, '404.html')));
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`reID site → http://localhost:${PORT}`));
