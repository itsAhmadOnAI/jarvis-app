"""Makes the icons (from favicon.svg) and the 1200x630 share images. Needs Playwright (Jarvis's .venv has it):
    ~/jarvis/.venv/bin/python make_images.py"""
import base64
import os
from playwright.sync_api import sync_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
SVG = open(os.path.join(HERE, "favicon.svg")).read()
SHOT = base64.b64encode(open(os.path.join(HERE, "img/home.webp"), "rb").read()).decode()

CARDS = {
    "og-home": ("A Jarvis-like assistant", "Your very own<br><em>personal assistant.</em>"),
    "og-early-access": ("Early access", "Be one of the <em>first</em><br>to have one."),
    "og-build": ("Building in public", "I'm building my own<br><em>Jarvis.</em>"),
    "og-work": ("For Shopify stores", "Shopify sections,<br><em>built fast.</em><br>Checked on every screen."),
}

CARD = """<html><body style="margin:0;width:1200px;height:630px;overflow:hidden;background:#0D1117;
font-family:'Ubuntu Sans',Ubuntu,system-ui,sans-serif;color:#E6EDF3;position:relative">
<div style="position:absolute;inset:-200px auto auto -200px;width:900px;height:900px;
background:radial-gradient(closest-side,rgba(108,176,255,.22),transparent)"></div>
<div style="position:absolute;left:72px;top:70px;display:flex;align-items:center;gap:16px;font-size:34px;font-weight:700">
<img src="data:image/svg+xml;base64,{icon}" width="56" height="56">Jarvis</div>
<div style="position:absolute;left:72px;top:205px;width:600px">
<div style="font-size:20px;letter-spacing:.18em;text-transform:uppercase;color:#6CB0FF">{eyebrow}</div>
<div style="font-size:58px;line-height:1.08;font-weight:700;margin-top:18px">{title}</div></div>
<div style="position:absolute;left:72px;bottom:56px;color:#9AA4B0;font-size:22px">itsahmadonai.github.io/jarvis-app</div>
<img src="data:image/webp;base64,{shot}" style="position:absolute;left:700px;top:90px;width:760px;border-radius:18px;
border:1px solid #262E39;box-shadow:0 30px 80px rgba(0,0,0,.6)">
<style>em{{font-style:normal;color:#6CB0FF}}</style></body></html>"""

with sync_playwright() as p:
    b = p.chromium.launch()
    icon64 = base64.b64encode(SVG.encode()).decode()
    for name, size in (("favicon-32.png", 32), ("apple-touch-icon.png", 180), ("icon-192.png", 192), ("icon-512.png", 512)):
        pg = b.new_page(viewport={"width": size, "height": size})
        pg.set_content(f'<body style="margin:0"><img src="data:image/svg+xml;base64,{icon64}" width="{size}" height="{size}"></body>')
        pg.screenshot(path=os.path.join(HERE, name), omit_background=True)
        pg.close()
    for name, (eyebrow, title) in CARDS.items():
        pg = b.new_page(viewport={"width": 1200, "height": 630})
        pg.set_content(CARD.format(icon=icon64, eyebrow=eyebrow, title=title, shot=SHOT))
        pg.wait_for_timeout(200)
        pg.screenshot(path=os.path.join(HERE, "img", name + ".jpg"), type="jpeg", quality=85)
        pg.close()
    b.close()
print("images made")
