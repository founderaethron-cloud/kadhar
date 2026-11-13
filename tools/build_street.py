"""Generate KADHAR STREET (kadhar.store) into ../streetwear. Run: python3 tools/build_street.py
Source: '10 — Baggy & Oversized Outfits' page of the Kadhar Product Design deck. Price set by ABD: ₹1,999.
"""
import os, html, pathlib
OUT = str(pathlib.Path(__file__).resolve().parent.parent / 'streetwear')
E = html.escape
PRICE = '₹1,999'
COL = {'Stone': 'stone', 'Charcoal': 'charcoal', 'Olive': 'olive', 'Sand': 'sand', 'Black': 'black'}

P = [
 dict(slug='oversized-tee', name='Oversized Tee', img='fit-tee-wide', fabric='Heavyweight jersey',
      blurb='The base layer. Dropped shoulders, boxy body, sleeves that hit the elbow.',
      feats=['Dropped shoulders for a relaxed vibe','Heavyweight jersey that holds its shape','Boxy, cropped-to-hip body'], colours=['Black','Charcoal','Stone']),
 dict(slug='graphic-tee', name='Graphic Tee', img='fit-cargo-graphic', fabric='Washed cotton jersey',
      blurb='Oversized tee with a washed print. Wear it loud, wear it alone.',
      feats=['Washed print with a worn-in finish','Dropped shoulders','Pairs with Baggy Cargo'], colours=['Stone','Black','Charcoal']),
 dict(slug='oversized-shirt', name='Oversized Shirt', img='fit-shirt-wide', fabric='Washed cotton twill',
      blurb='A long, loose shirt to throw over a tee. Open or buttoned, it moves.',
      feats=['Extended length','Chest pocket','Rugged seams and raw finishes'], colours=['Sand','Olive','Stone']),
 dict(slug='drop-shoulder-sweatshirt', name='Drop-Shoulder Sweatshirt', img='style-monochrome', fabric='French terry',
      blurb='Heavy French terry, wide body, dropped shoulders. The everyday armour.',
      feats=['Brushed French terry','Ribbed cuffs and hem','Layer-friendly cut'], colours=['Black','Charcoal','Stone']),
 dict(slug='slouchy-jacket', name='Slouchy Jacket', img='fit-jacket-cargo', fabric='Canvas',
      blurb='A boxy canvas jacket with a slouch. Built for layering over everything.',
      feats=['Heavyweight canvas for structure','Deep pockets for utility','Relaxed, slouchy shoulder'], colours=['Black','Olive','Charcoal']),
 dict(slug='wide-leg-pants', name='Wide-Leg Pants', img='fit-layered', fabric='Twill',
      blurb='Wide from hip to hem. Loose where it matters, clean at the waist.',
      feats=['Wide, straight leg','Adjustable hems for fit and flow','Heavyweight twill'], colours=['Olive','Black','Stone']),
 dict(slug='baggy-cargo', name='Baggy Cargo', img='style-street-utility', fabric='Ripstop twill',
      blurb='Oversized cargo pockets, drawcord hems, all-day room to move.',
      feats=['Oversized cargo pockets','Drawcord hems','Rugged seams'], colours=['Black','Olive','Sand']),
]
FITS = [('fit-tee-wide','Oversized Tee + Wide-Leg Pants'),('fit-cargo-graphic','Graphic Tee + Baggy Cargo'),('fit-shirt-wide','Oversized Shirt + Wide-Leg Pants'),
        ('fit-jacket-cargo','Slouchy Jacket + Cargo'),('fit-layered','The Layered Look')]
STYLES = [('style-city-minimal','City Minimal'),('style-street-utility','Street Utility'),('style-neutral-layers','Neutral Layers'),('style-monochrome','Monochrome'),('style-earth-tones','Earth Tones')]
DETAILS = [('d-shoulders','Dropped shoulders for a relaxed vibe'),('d-pockets','Deep pockets for utility'),('d-cargo','Oversized cargo pockets'),
           ('d-heavyweight','Heavyweight fabrics for structure'),('d-hems','Adjustable hems for fit and flow'),('d-seams','Rugged seams and raw finishes')]
TICK = ['Loose fit', 'Max impact', 'Everything ' + PRICE, 'Drop 01', 'Wide leg', 'Dropped shoulders']

def head(title, desc, root):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(title)}</title>
<link rel="icon" href="data:,">
<meta name="description" content="{E(desc)}">
<meta name="theme-color" content="#141313">
<link rel="stylesheet" href="{root}assets/css/street.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="hdr">
  <!-- LOGO PLACEHOLDER: replace with the KADHAR / KADHAR STREET logo file when supplied -->
  <a class="logo" href="{root}index.html" aria-label="KADHAR Street home"><b>KADHAR</b><span>STREET</span></a>
  <nav class="nav" aria-label="Main"><a href="{root}index.html#shop">Shop</a><a href="{root}index.html#fits">Fits</a><a href="{root}index.html#details">Details</a><a href="{root}index.html#drop">Drop 01</a></nav>
  <button class="menu-btn label" aria-expanded="false" aria-controls="drawer">Menu</button>
</header>
<nav class="drawer" id="drawer" aria-label="Mobile"><a href="{root}index.html#shop">Shop</a><a href="{root}index.html#fits">Fits</a><a href="{root}index.html#details">Details</a><a href="{root}index.html#drop">Drop 01</a></nav>
<main id="main">
'''

def ticker():
    items = ''.join(f'<span>{t} ✦</span>' for t in TICK) * 2
    return f'<div class="ticker" aria-hidden="true"><div class="ticker__track">{items}</div></div>'

def foot(root):
    return f'''</main>
<footer class="ftr"><div class="wrap">
  <div class="ftr__cols">
    <div><span class="label">KADHAR Street</span><p class="muted">Loose fit. Max impact. Streetwear from the house of KADHAR.</p></div>
    <div><span class="label">Shop</span><a href="{root}index.html#shop">All pieces</a><a href="{root}index.html#fits">Fits</a><a href="{root}products/baggy-cargo.html">Baggy Cargo</a></div>
    <div><span class="label">Help</span><a href="{root}index.html#size">Size guide</a><a href="{root}index.html#care">Care</a><a href="#">Shipping &amp; returns</a></div>
    <div><span class="label">House</span><a href="https://kadhar.in" rel="noopener">KADHAR ↗</a><a href="#">Instagram</a></div>
  </div>
  <p class="mega ftr__mark" aria-hidden="true">KADHAR STREET</p>
  <div class="ftr__legal"><span>© 2026 KADHAR. <span class="ph" title="Company and GST details placeholder">Company details</span></span><span><a href="#">Privacy</a> · <a href="#">Terms</a></span></div>
</div></footer>
<script src="{root}assets/js/street.js"></script>
</body>
</html>
'''

def dots(p): return ''.join(f'<i style="background:var(--sw-{COL[c]})" title="{c}"></i>' for c in p['colours'])

def card(p, root):
    return f'''<a class="card" href="{root}products/{p['slug']}.html">
  <div class="card__img"><img src="{root}assets/img/{p['img']}.webp" alt="{E(p['name'])}" loading="lazy"></div>
  <div class="card__body"><h3 class="card__name">{E(p['name'])}</h3>
    <div class="card__row"><span class="price">{PRICE}</span><span class="dots" aria-label="Colours: {', '.join(p['colours'])}">{dots(p)}</span></div>
    <span class="muted" style="font-size:13px">{E(p['fabric'])}</span></div>
</a>'''

SIZE = '''<table class="sz"><thead><tr><th>Size</th><th>Chest (in)</th><th>Length (in)</th><th>Waist (in)</th></tr></thead><tbody>
<tr><td>XS</td><td class="muted">XX</td><td class="muted">XX</td><td class="muted">XX</td></tr><tr><td>S</td><td class="muted">XX</td><td class="muted">XX</td><td class="muted">XX</td></tr>
<tr><td>M</td><td class="muted">XX</td><td class="muted">XX</td><td class="muted">XX</td></tr><tr><td>L</td><td class="muted">XX</td><td class="muted">XX</td><td class="muted">XX</td></tr>
<tr><td>XL</td><td class="muted">XX</td><td class="muted">XX</td><td class="muted">XX</td></tr><tr><td>XXL</td><td class="muted">XX</td><td class="muted">XX</td><td class="muted">XX</td></tr></tbody></table>
<p class="notice"><span class="ph" title="Measurements placeholder">Measurements coming with Drop 01.</span> Built oversized: take your usual size for the intended fit, size down for a closer one.</p>'''

CARE = 'Cold wash inside out · Mild detergent · Do not bleach · Line dry in shade · Iron low if needed'

DROPFORM = '''<form class="drop" data-preview novalidate><label class="skip" for="drop-email">Email</label><input id="drop-email" type="email" placeholder="your@email.com" required autocomplete="email"><button class="btn" type="submit">Get drop access</button></form>
<p class="notice" data-note hidden tabindex="-1">Preview only: sign-ups aren't connected yet. Nothing was sent.</p>'''

def w(path, s):
    p = os.path.join(OUT, path); os.makedirs(os.path.dirname(p), exist_ok=True); open(p, 'w').write(s)

home = head('KADHAR Street — Loose fit. Max impact.', f'Oversized streetwear from KADHAR. Tees, cargos, wide-leg pants and jackets, every piece {PRICE}.', '') + f'''
<section class="hero">
  <div class="hero__txt">
    <div>
      <span class="label muted">Drop 01 · Baggy &amp; Oversized</span>
      <h1 class="mega h-xl" style="margin-top:var(--s6)">Loose fit.<br>Max<br>impact.</h1>
    </div>
    <div style="display:grid;gap:var(--s6)">
      <p class="tag" style="max-width:520px">Redefining proportions. Comfort in every layer. Designed for movement, built for presence.</p>
      <div style="display:flex;gap:var(--s4);flex-wrap:wrap"><a class="btn" href="#shop">Shop the drop</a><a class="btn btn--ghost" href="#fits">See the fits</a></div>
    </div>
  </div>
  <div class="hero__img"><img src="assets/img/hero.webp" alt="Model in an oversized black tee and baggy black cargo">
    <div class="sticker" aria-hidden="true"><div><small>Every piece</small><b>{PRICE}</b></div></div></div>
</section>
{ticker()}
<section class="sec" id="shop"><div class="wrap">
  <div class="sec-head"><h2 class="mega h-l">The drop</h2><p class="muted">{len(P)} pieces · every one {PRICE}</p></div>
  <div class="grid">{''.join(card(p,'') for p in P)}
    <a class="card" href="#drop" style="display:grid;place-items:center;background:var(--clay);color:var(--on-clay);min-height:260px;text-align:center;padding:var(--s6)"><div><p class="mega h-m">Drop 02</p><p class="label" style="margin-top:var(--s3)">Get early access →</p></div></a>
  </div>
</div></section>
<section class="sec" id="fits" style="padding-top:0"><div class="wrap">
  <div class="sec-head"><h2 class="mega h-l">Fit guide</h2><p class="muted">Five ways to wear it. Scroll →</p></div>
  <div class="fits" tabindex="0" aria-label="Fit guide, scrollable">{''.join(f'<figure class="fit" style="margin:0"><img src="assets/img/{i}.webp" alt="{E(t)}" loading="lazy"><p class="label">{E(t)}</p></figure>' for i,t in FITS)}</div>
</div></section>
<section class="sec band" id="details"><div class="wrap">
  <div class="sec-head"><h2 class="mega h-l">Built different</h2><p class="muted">Heavyweight jersey · washed cotton · French terry · canvas · twill</p></div>
  <div class="feats">{''.join(f'<div class="feat"><img src="assets/img/{i}.webp" alt="" loading="lazy"><p>{E(t)}</p></div>' for i,t in DETAILS)}</div>
</div></section>
<section class="sec"><div class="wrap">
  <div class="sec-head"><h2 class="mega h-l">Pick your vibe</h2></div>
  <div class="fits" tabindex="0" aria-label="Style inspiration, scrollable">{''.join(f'<figure class="fit" style="margin:0"><img src="assets/img/{i}.webp" alt="{E(t)} look" loading="lazy" style="aspect-ratio:3/5"><p class="label">{E(t)}</p></figure>' for i,t in STYLES)}</div>
</div></section>
{ticker()}
<section class="sec" id="size"><div class="wrap" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:var(--s12)">
  <div><h2 class="mega h-m" style="margin-bottom:var(--s6)">Size guide</h2>{SIZE}</div>
  <div id="care"><h2 class="mega h-m" style="margin-bottom:var(--s6)">Fit &amp; care</h2><p class="tag" style="margin-bottom:var(--s4)">Loose where it matters. Structured where it counts.</p><p class="muted">{CARE}</p></div>
</div></section>
<section class="sec band" id="drop"><div class="wrap" style="display:grid;gap:var(--s6)">
  <h2 class="mega h-l">Don't miss the drop</h2>
  <p class="muted" style="max-width:560px">Drops are small and they go. Get first access, sizes and restock alerts.</p>
  {DROPFORM}
</div></section>
''' + foot('')
w('index.html', home)

for i, p in enumerate(P):
    nxt = P[(i + 1) % len(P)]
    sw = ''.join(f'<button class="swatch" type="button" data-name="{c}" aria-pressed="{"true" if k==0 else "false"}"><i style="background:var(--sw-{COL[c]})"></i>{c}</button>' for k, c in enumerate(p['colours']))
    sizes = ''.join(f'<button class="size" type="button" aria-pressed="false">{s}</button>' for s in ['XS','S','M','L','XL','XXL'])
    page = head(f"{p['name']} — KADHAR Street", f"{p['name']}, {PRICE}. {p['blurb']}", '../') + f'''
<section class="pdp">
  <div class="pdp__img"><img src="../assets/img/{p['img']}.webp" alt="Model wearing the {E(p['name'])}"></div>
  <div class="pdp__info">
    <a class="label muted" href="../index.html#shop" style="text-decoration:none">← The drop</a>
    <div><h1 class="mega h-l">{E(p['name'])}</h1><p class="tag" style="margin-top:var(--s4)">{E(p['blurb'])}</p></div>
    <div><span class="price" style="font-size:28px;padding:10px 14px">{PRICE}</span></div>
    <div class="block"><fieldset class="swatches"><legend class="label" style="margin-bottom:var(--s3)">Colour — <span data-colour-name>{p['colours'][0]}</span></legend>{sw}</fieldset></div>
    <div class="block"><p class="label" style="margin-bottom:var(--s3)">Size</p><div class="sizes" role="group" aria-label="Size">{sizes}</div><p class="notice"><a href="../index.html#size">Size guide</a> · built oversized</p></div>
    <div><a class="btn" href="../index.html#drop" style="width:100%">Get drop access</a><p class="notice">Drop 01 opens soon. Join the list to get first access.</p></div>
    <div class="block"><p class="label" style="margin-bottom:var(--s3)">Details</p><ul class="list">{''.join(f'<li>{E(f)}</li>' for f in p['feats'])}</ul></div>
    <div class="block"><p class="label" style="margin-bottom:var(--s3)">Fabric</p><p>{E(p['fabric'])}</p></div>
    <div class="block"><p class="label" style="margin-bottom:var(--s3)">Care</p><p class="muted">{CARE}</p></div>
    <a class="block" href="{nxt['slug']}.html" style="text-decoration:none;display:flex;justify-content:space-between;align-items:center"><span class="label muted">Next</span><span class="mega h-m">{E(nxt['name'])} →</span></a>
  </div>
</section>
''' + foot('../')
    w(f"products/{p['slug']}.html", page)
print('built', 1 + len(P), 'street pages')
