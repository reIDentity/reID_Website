"""Shared layout for reID PDF reports (A4, rendered with headless Chrome)."""
import os, html as H

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SHOTS = '/tmp/claude-0/shots/'

def fonts():
    css = ''
    for fam, pre, ws in [('IBM Plex Sans', 'plex-sans', [400, 500, 600]), ('IBM Plex Mono', 'plex-mono', [400, 500])]:
        for w in ws:
            css += f"@font-face{{font-family:'{fam}';font-weight:{w};src:url('file://{ROOT}/assets/fonts/{pre}-{w}.woff2') format('woff2')}}\n"
    return css

CSS = """
@page{size:A4;margin:0}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:'IBM Plex Sans',sans-serif;color:#0B1220;font-size:10.5pt;line-height:1.55;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.page{width:210mm;height:297mm;position:relative;overflow:hidden;padding:24mm 18mm 20mm;page-break-after:always;background:#fff}
.page:last-child{page-break-after:auto}
.hd{position:absolute;left:18mm;right:18mm;top:10mm;display:flex;justify-content:space-between;align-items:center;font-size:8pt;color:#5E6A7E;border-bottom:1px solid #E6ECF4;padding-bottom:3mm}
.hd img{height:6mm}
.ft{position:absolute;left:18mm;right:18mm;bottom:9mm;display:flex;justify-content:space-between;font-size:8pt;color:#8A94A6}
h1{font-size:30pt;line-height:1.05;letter-spacing:-.03em;font-weight:600}
h2{font-size:18pt;letter-spacing:-.02em;font-weight:600;margin:0 0 4mm;display:flex;gap:3mm;align-items:baseline}
h2 .n{font:500 11pt 'IBM Plex Mono';color:#0066CC}
h3{font-size:12pt;font-weight:600;margin:5mm 0 2mm}
p{margin:0 0 2.6mm}
.lead{font-size:11.5pt;color:#3A4558}
.mute{color:#5E6A7E}
ul{margin:0 0 3mm 4.5mm}li{margin:0 0 1.2mm}
table{width:100%;border-collapse:collapse;margin:2mm 0 4mm;font-size:9pt}
th{background:#0B1220;color:#fff;text-align:left;font-weight:500;padding:2mm 2.4mm}
td{border-bottom:1px solid #E6ECF4;padding:1.8mm 2.4mm;vertical-align:top}
tr:nth-child(even) td{background:#F6F9FC}
code,.mono{font-family:'IBM Plex Mono',monospace;font-size:8.6pt;background:#F1F5FA;border-radius:3px;padding:0 1mm}
pre{font-family:'IBM Plex Mono',monospace;font-size:8pt;background:#0B1220;color:#E3ECF8;border-radius:3mm;padding:3.5mm 4mm;margin:2mm 0 4mm;white-space:pre-wrap;line-height:1.5}
.grid{display:grid;gap:4mm}.g2{grid-template-columns:1fr 1fr}.g3{grid-template-columns:1fr 1fr 1fr}.g4{grid-template-columns:repeat(4,1fr)}
.shot{border-radius:2.5mm;overflow:hidden;border:1px solid #DDE4EE;box-shadow:0 2mm 6mm -3mm rgba(10,40,90,.25)}
.shot img{width:100%;display:block}
.cap{font-size:8pt;color:#5E6A7E;margin-top:1.2mm}
.phone{border-radius:5mm;overflow:hidden;border:2px solid #0B1220}
.phone img{width:100%;display:block}
.stat{background:#F1F8FF;border:1px solid #D4E8FF;border-radius:3mm;padding:3.5mm}
.stat b{display:block;font-size:20pt;font-weight:600;letter-spacing:-.03em;color:#0066CC;line-height:1.1}
.stat span{font-size:8.5pt;color:#3A4558}
.callout{background:#0066CC;color:#fff;border-radius:3mm;padding:4mm 5mm;margin:3mm 0}
.callout b{font-weight:600}
.note{background:#FFF8E6;border:1px solid #F5E2B0;border-radius:3mm;padding:3mm 4mm;font-size:9pt;margin:2mm 0 4mm}
.ok{color:#11733A;font-weight:600}.warn{color:#9A6400;font-weight:600}
.pill{display:inline-block;border:1px solid #DDE4EE;border-radius:20mm;padding:.6mm 2.6mm;margin:0 1mm 1.5mm 0;font-size:8.5pt;background:#fff}
.sw{display:inline-block;width:5mm;height:5mm;border-radius:1.2mm;vertical-align:middle;margin-right:2mm;border:1px solid rgba(0,0,0,.08)}
/* cover */
.cover{background:#0B1220;color:#fff;padding:22mm 18mm}
.cover .glow{position:absolute;right:-40mm;top:-40mm;width:160mm;height:160mm;border-radius:50%;background:radial-gradient(circle,rgba(0,145,255,.45),transparent 65%)}
.cover .dots{position:absolute;inset:0;background-image:radial-gradient(rgba(124,196,255,.14) 1px,transparent 1.3px);background-size:5mm 5mm}
.cover .in{position:relative;display:flex;flex-direction:column;height:100%}
.cover .logo{height:11mm;filter:brightness(0) invert(1)}
.cover .kick{margin-top:24mm;font:500 9pt 'IBM Plex Mono';letter-spacing:.2em;color:#7CC4FF}
.cover h1{font-size:36pt;margin-top:4mm}.cover h1 span{color:#4DB0FF}
.cover .sub{margin-top:5mm;font-size:12pt;color:#B9C6D8;max-width:150mm}
.cover .hero{margin-top:10mm;border-radius:4mm;overflow:hidden;border:1px solid rgba(255,255,255,.15);box-shadow:0 10mm 30mm -10mm rgba(0,145,255,.5)}
.cover .hero img{width:100%;display:block}
.cover .meta{margin-top:auto;display:grid;grid-template-columns:repeat(4,1fr);gap:4mm;border-top:1px solid rgba(255,255,255,.15);padding-top:5mm}
.cover .meta small{display:block;font:500 7pt 'IBM Plex Mono';letter-spacing:.14em;color:#7CC4FF;margin-bottom:1mm}
.cover .meta b{font-weight:500;font-size:9pt}
/* contents */
.toc a{display:flex;align-items:baseline;gap:4mm;padding:2.4mm 0;border-bottom:1px solid #EEF2F7;color:#0B1220;text-decoration:none;font-size:11pt}
.toc a i{font:500 9.5pt 'IBM Plex Mono';font-style:normal;color:#0066CC;width:9mm}
.toc a span{flex:1}
.toc a em{font-style:normal;color:#8A94A6;font-size:9pt}
"""

LOGO = f'file://{ROOT}/assets/logo-mark-text.svg'

def img(name):
    return f'file://{SHOTS}{name}'

def shot(name, cap=''):
    return f'<div><div class="shot"><img src="{img(name)}"></div>' + (f'<div class="cap">{cap}</div>' if cap else '') + '</div>'

def phone(name, cap=''):
    return f'<div><div class="phone"><img src="{img(name)}"></div>' + (f'<div class="cap">{cap}</div>' if cap else '') + '</div>'

def table(head, rows):
    return '<table><tr>' + ''.join(f'<th>{h}</th>' for h in head) + '</tr>' + ''.join('<tr>' + ''.join(f'<td>{c}</td>' for c in r) + '</tr>' for r in rows) + '</table>'

def build(title, doc_name, cover, toc, pages):
    """pages: list of (section_number_or_None, section_title, html)"""
    out = [f'<!doctype html><html><head><meta charset="utf-8"><title>{title}</title><style>{fonts()}{CSS}</style></head><body>']
    out.append(cover)
    # contents
    toc_html = ''.join(f'<a><i>{n}</i><span>{t}</span><em>{p}</em></a>' for n, t, p in toc)
    out.append(page(doc_name, 'Contents', f'<h1 style="font-size:24pt;margin-bottom:6mm">Contents</h1><div class="toc">{toc_html}</div>', 2))
    for i, (n, t, body) in enumerate(pages):
        out.append(page(doc_name, f'{n} · {t}' if n else t, body, i + 3))
    out.append('</body></html>')
    return ''.join(out)

def page(doc_name, label, body, num):
    return f'<section class="page"><div class="hd"><img src="{LOGO}"><span>{label}</span></div>{body}<div class="ft"><span>reID · reidentity.net · {doc_name}</span><span>{num}</span></div></section>'

def sec(n, t, body):
    return (n, t, f'<h2><span class="n">{n}</span>{t}</h2>' + body)
