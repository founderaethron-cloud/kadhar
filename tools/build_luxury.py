"""Generate the KADHAR static site into ../site. Run: python3 build.py"""
import os, html

import pathlib
OUT = str(pathlib.Path(__file__).resolve().parent.parent / 'luxury')
# Pricing (ABD, Nov 2026): luxury range ₹40,000 to ₹5,00,000. Per-garment prices not set yet, so every
# garment shows the entry price. Add a 'price' field to a garment to override.
PRICE_FROM = 'From ₹40,000'
PRICE_NOTE = 'Made to measure up to ₹5,00,000. Final price confirmed at your fitting.'
def price(g): return g.get('price', PRICE_FROM)
E = html.escape

# Garment data: names, taglines, colourways and features from the Kadhar Product Design deck;
# construction notes from the Product & Roadmap. "Khadi" replaced by "handwoven cotton" (KVIC mark).
G = [
 dict(n='01', slug='01-floating-overshirt', name='The Floating Overshirt', cat='shirts', short='Overshirt',
  tag='Moves like air. Woven with heritage. Designed for now.',
  concept='An oversized shirt that moves with the wind like a sail.',
  fabric=('KH-01', '100% handwoven cotton · heavy weight'),
  colours=[('Stone','stone'),('Olive','olive'),('Charcoal','charcoal')],
  features=['Boxy silhouette','Dropped shoulders','Hidden pockets','Raw unfinished hem','Extended sleeves','Coconut shell buttons'],
  innov=[('Floating back yoke','A deep back pleat lets the fabric move freely with the wind.'),('Hidden side pockets','Seam-concealed pockets integrated into the side panel.'),('Extended sleeve','Extra-long sleeves with a sculpted curve for a relaxed drape.'),('Raw hem','An unfinished hem that frays naturally over time, making each piece unique.')],
  special='Not just a shirt: an experience of movement, where heritage and modern design meet in balance.',
  card='overshirt-flat', imgs=['overshirt-desert','overshirt-sculpture','overshirt-flat']),
 dict(n='02', slug='02-urban-kimono-jacket', name='Urban Kimono Jacket', cat='outerwear', short='Jacket',
  tag='Structured. Minimal. Timeless.',
  concept='Kimono proportions rebuilt for the city: a wide, cropped body in heavyweight handwoven cloth.',
  fabric=('KH-02', 'Handwoven cotton + hemp · 250–320 GSM'),
  colours=[('Charcoal','charcoal'),('Stone','stone'),('Olive','olive')],
  features=['Cropped kimono silhouette','Wide, clean sleeves','Hidden magnetic closure','Cotton lining','Reinforced shoulders'],
  innov=[('Magnetic closure','Hidden magnets keep the front clean, with no visible fastening.'),('Shoulder tape','Reinforcement tape holds the drop shoulder in shape.'),('Hemp blend','Hemp adds structure and strength to the handwoven base.')],
  special='Architecture you wear: a jacket that holds its shape and softens with you.',
  card='kimono-flat', imgs=['kimono-studio','kimono-architecture','kimono-sculpture','kimono-flat']),
 dict(n='03', slug='03-cargo-2', name='Cargo 2.0', cat='trousers', short='Trouser',
  tag='Luxury utility, redefined.',
  concept='A wide utility trouser that keeps the cargo’s function and drops the noise.',
  fabric=('KH-02', 'Handwoven cotton twill + hemp'),
  colours=[('Forest','forest'),('Black','black'),('Sand','sand')],
  features=['Wide-leg silhouette','Reinforced cargo pockets','Drawcord hems','Double-knee reinforcement','Bartack stitching at stress points'],
  innov=[('Structured pockets','Pleated cargo pockets that hold their shape without bulk.'),('Adjustable hem','Drawcord cuffs move from straight leg to gathered.'),('Double knee','A second layer where trousers wear first.')],
  special='Utility wear built to last years, not seasons.',
  card='cargo-flat', imgs=['cargo-wall','cargo-forest','cargo-studio','cargo-flat']),
 dict(n='04', slug='04-modular-travel-coat', name='Modular Travel Coat', cat='outerwear', short='Coat',
  tag='One garment. Three looks. Zero compromise.',
  concept='A long coat that becomes a short coat and a vest: built for travel, light enough to carry.',
  fabric=('KH-07', 'Lightweight canvas-weave handwoven cotton'),
  colours=[('Olive','olive'),('Black','black'),('Sand','sand')],
  features=['Detachable sleeves','Hidden zips','Snap fastenings','Breathable cotton lining','Stand collar'],
  innov=[('Long','Full-length coat for cover and presence.'),('Short','Unzip the lower panel for a cropped jacket.'),('Vest','Remove the sleeves for a layering vest.')],
  special='One piece to pack. Three ways to arrive.',
  card='coat-flat', imgs=['coat-architecture','coat-sculpture','coat-studio','coat-flat']),
 dict(n='05', slug='05-desert-nomad-set', name='Desert Nomad Set', cat='sets', short='Set',
  tag='Woven for journeys. Made to breathe.',
  concept='A relaxed shirt-and-trouser set with an integrated scarf, made for heat and long days.',
  fabric=('KH-04', 'Handwoven cotton + linen · garment-dyed'),
  colours=[('Sand','sand'),('Stone','stone'),('Clay','clay')],
  features=['Integrated scarf collar','Relaxed trouser with elastic waist','Natural corozo or coconut buttons','Garment-dyed','Bio-softened finish'],
  innov=[('Scarf collar','A built-in scarf for sun and wind.'),('Linen blend','Linen keeps the cloth cool and breathable.')],
  special='Made for heat, wind and the long road.',
  card='nomad', imgs=['nomad']),
 dict(n='06', slug='06-wrapped-hoodie', name='The Wrapped Hoodie', cat='tops', short='Hoodie',
  tag='Draped by tradition. Designed for tomorrow.',
  concept='A hoodie with an asymmetric wrap front, drawn from draped garments.',
  fabric=('KH-01', 'Handwoven cotton face · brushed organic cotton inner'),
  colours=[('Stone','stone'),('Charcoal','charcoal'),('Forest','forest')],
  features=['Asymmetric wrap front','Oversized hood','Dropped shoulders','Brushed inner layer'],
  innov=[('Two-layer cloth','Handwoven texture outside, soft brushed cotton inside for warmth.'),('Wrap front','The drape crosses the body like a shawl.')],
  special='The comfort of a hoodie with the line of a drape.',
  card='hoodie', imgs=['hoodie']),
 dict(n='07', slug='07-architect-shirt', name='Architect Shirt', cat='shirts', short='Shirt',
  tag='Sculpted like architecture. Folded like origami. Designed to make simplicity unforgettable.',
  concept='Every fold, seam and angle is placed to create structure, movement and presence. Minimal in detail, maximal in impact.',
  fabric=('KH-01', 'Fine-count handwoven cotton'),
  colours=[('Ivory','ivory'),('Slate','slate'),('Charcoal','charcoal')],
  features=['Folded shoulders','Geometric seams','Invisible buttons','Angular cuffs','Sculptural silhouette'],
  innov=[('Hidden placket','A concealed button placket for a clean, seamless front.'),('Folded shoulders','Folds create structure and dimension.'),('Geometric seams','Seam lines drawn from architectural forms.'),('Back pleat','Ease of movement and comfort.')],
  special='Origami in motion.',
  card='architect', imgs=['architect']),
 dict(n='08', slug='08-infinity-scarf-jacket', name='Infinity Scarf Jacket', cat='outerwear', short='Jacket',
  tag='One piece. Infinite presence.',
  concept='A jacket and a scarf cut as one, draping into several ways to wear.',
  fabric=('KH-06', 'Handwoven cotton + bamboo (light) · wool blend (winter)'),
  colours=[('Stone','stone'),('Charcoal','charcoal'),('Forest','forest')],
  features=['Integrated drape scarf','Minimal seams','Relaxed fit','Multiple ways to wear'],
  innov=[('One-piece drape','The scarf is part of the pattern, not an add-on.'),('Two weights','A light version for heat, a wool blend for winter.')],
  special='Effortless drama from a single piece.',
  card='scarf', imgs=['scarf']),
 dict(n='09', slug='09-urban-dhoti-trouser', name='Urban Dhoti Trouser', cat='trousers', short='Trouser',
  tag='Tailored roots. Modern movement.',
  concept='The fluidity of the dhoti, tailored into a tapered trouser for every day.',
  fabric=('KH-03', 'Handwoven cotton with soft drape'),
  colours=[('Stone','stone'),('Charcoal','charcoal'),('Black','black')],
  features=['Soft front pleating','Tapered leg','Elastic waistband','Garment washed'],
  innov=[('Pleat engineering','Pleats give dhoti movement without the wrap.'),('Tapered pattern','Clean at the ankle, generous at the hip.')],
  special='Heritage movement, cut for the city.',
  card='dhoti', imgs=['dhoti']),
]

NAV = [('collection.html','Collection'),('fabrics.html','Fabrics'),('atelier.html','Atelier'),('house.html','House'),('journal.html','Journal')]

def head(title, desc, root, active):
    nav = ''.join(f'<a href="{root}{h}"{" aria-current=\"page\"" if h==active else ""}>{t}</a>' for h,t in NAV)
    drawer = ''.join(f'<a href="{root}{h}">{t}</a>' for h,t in NAV) + f'<a href="{root}atelier.html">Book a fitting</a>'
    return f'''<!doctype html>
<html lang="en" data-theme="light">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(title)}</title>
<link rel="icon" href="data:,">
<meta name="description" content="{E(desc)}">
<link rel="stylesheet" href="{root}assets/css/tokens.css">
<link rel="stylesheet" href="{root}assets/css/components.css">
<link rel="stylesheet" href="{root}assets/css/site.css">
</head>
<body class="kd-root">
<a class="skip" href="#main">Skip to content</a>
<div class="site-header">
<header class="kd-header">
  <!-- LOGO PLACEHOLDER: replace this text wordmark with the KADHAR logo file when supplied -->
  <a class="kd-wordmark" href="{root}index.html" aria-label="KADHAR home">KADHAR</a>
  <nav class="kd-nav" aria-label="Main">{nav}</nav>
  <div class="kd-header__end"><a class="kd-link" href="{root}atelier.html">Book a fitting</a><button class="menu-btn kd-label" aria-expanded="false" aria-controls="drawer">Menu</button></div>
</header>
<nav class="drawer" id="drawer" aria-label="Mobile">{drawer}</nav>
</div>
<main id="main">
'''

def foot(root):
    return f'''</main>
<footer class="kd-footer">
  <div class="footer-cols">
    <div><span class="kd-label">Collection</span><a href="{root}collection.html">All garments</a><a href="{root}garments/01-floating-overshirt.html">Overshirts</a><a href="{root}garments/04-modular-travel-coat.html">Outerwear</a><a href="{root}garments/03-cargo-2.html">Trousers</a></div>
    <div><span class="kd-label">Atelier</span><a href="{root}atelier.html">Book a fitting</a><a href="{root}atelier.html#made-to-measure">Made to measure</a><a href="{root}house.html#care">Care</a></div>
    <div><span class="kd-label">House</span><a href="{root}house.html">Our standard</a><a href="{root}fabrics.html">Fabrics</a><a href="{root}journal.html">Journal</a><a href="https://kadhar.store" rel="noopener">KADHAR Street ↗</a></div>
    <div><span class="kd-label">Letters</span><span>New drops and stories from the loom.</span>
      <form class="news" data-preview onsubmit="return false"><label class="skip" for="nl-{root or 'r'}">Email</label><input id="nl-{root or 'r'}" type="email" placeholder="Your email" required><button type="submit">Join</button></form></div>
  </div>
  <p class="kd-footer__mark" aria-hidden="true">KADHAR</p>
  <div class="footer-legal"><span>© 2026 KADHAR. <span class="ph" title="Company and GST details placeholder">Company details</span></span><span><a href="#">Privacy</a> · <a href="#">Terms</a> · <a href="#">Shipping &amp; returns</a></span></div>
</footer>
<script src="{root}assets/js/site.js"></script>
</body>
</html>
'''

def dots(g):
    return ''.join(f'<span style="width:10px;height:10px;border-radius:9999px;background:var(--swatch-{c});box-shadow:inset 0 0 0 1px rgba(31,27,24,.2)" title="{n}"></span>' for n,c in g['colours'])

def card(g, root):
    return f'''<a class="kd-card" href="{root}garments/{g['slug']}.html" data-cat="{g['cat']}">
  <div class="kd-card__media"><img src="{root}assets/img/{g['card']}.webp" alt="{E(g['name'])}" loading="lazy"></div>
  <div class="kd-card__body"><span class="kd-card__num">{g['n']} —</span><h3 class="kd-card__name">{E(g['name'])}</h3>
  <div class="kd-card__meta"><span>{g['fabric'][0]} · {g['short']}</span><span class="kd-card__price">{price(g)}</span></div>
  <div style="display:flex;gap:6px;margin-top:4px" aria-label="Colourways: {', '.join(n for n,_ in g['colours'])}">{dots(g)}</div></div>
</a>'''

CARE = '''<div class="care">
<div><svg viewBox="0 0 24 24"><path d="M3 7h18l-2 12H5z"/><path d="M6 11c2 1.5 4 1.5 6 0s4-1.5 6 0"/></svg>Hand wash cold</div>
<div><svg viewBox="0 0 24 24"><rect x="4" y="4" width="16" height="16"/><path d="M8 8v8M16 8v8"/></svg>Dry in shade</div>
<div><svg viewBox="0 0 24 24"><path d="M4 17h16l-2-7H9c-3 0-5 3-5 7z"/><circle cx="12" cy="14" r="1"/></svg>Warm iron</div>
<div><svg viewBox="0 0 24 24"><path d="M12 4l9 16H3z"/><path d="M5 5l14 14M19 5L5 19"/></svg>Do not bleach</div>
</div>'''

def w(path, s):
    p = os.path.join(OUT, path); os.makedirs(os.path.dirname(p), exist_ok=True); open(p, 'w').write(s)

# ---------- Home ----------
home = head('KADHAR — Handwoven luxury', 'Architectural luxury clothing in handwoven Indian cotton. Small batches, made to measure.', '', 'index.html') + f'''
<section class="hero">
  <div class="hero__text">
    <div>
      <span class="kd-label eyebrow">Collection 01 · Handwoven cotton</span>
      <h1 class="display-xl hero__title">Woven<br>for now</h1>
      <p class="tagline" style="margin-top:var(--space-6);max-width:520px">Heritage cloth, cut for the city. Nine garments, made in small batches by hand.</p>
    </div>
    <div class="hero__foot">
      <a class="kd-btn kd-btn--primary" href="collection.html">Explore the collection</a>
      <a class="kd-link" href="atelier.html">Book a fitting</a>
    </div>
  </div>
  <div class="hero__media"><img src="assets/img/home-hero.webp" alt="Model in the Floating Overshirt in stone, among sculptural forms"></div>
</section>

<section class="section"><div class="wrap">
  <div class="sec-head">
    <div><span class="kd-label eyebrow">The first drop</span><h2 class="display-l">Nine garments</h2></div>
    <div class="sec-head__aside"><a class="kd-link" href="collection.html">View all nine</a></div>
  </div>
  <div class="grid-4">{''.join(card(g,'') for g in G[:4])}</div>
</div></section>

<section class="kd-manifesto"><blockquote>We don’t chase trends. We weave cloth that outlives them.</blockquote><cite>The KADHAR standard</cite></section>

<section class="section"><div class="wrap split">
  <div class="stack-6">
    <span class="kd-label eyebrow">Material wisdom</span>
    <h2 class="heading-2">Handspun, handwoven, slow by design.</h2>
    <p class="body-l kd-muted">KADHAR begins with the cloth. Handwoven cotton, plant-based dyes and fibre blends chosen for how they breathe, drape and age. Each garment is engineered around its fabric, not the other way round.</p>
    <a class="kd-link" href="fabrics.html">Explore the fabrics</a>
  </div>
  <div class="split__media"><img src="assets/img/overshirt-desert.webp" alt="The Floating Overshirt against sandstone walls" loading="lazy"></div>
</div></section>

<section class="section section--stone"><div class="wrap">
  <span class="kd-label eyebrow">From loom to wardrobe</span>
  <h2 class="heading-2" style="margin-bottom:var(--space-12)">Three rooms, one process.</h2>
  <div class="steps">
    <div class="step"><span class="step__n">01</span><h3 class="heading-3">The Basement</h3><p class="kd-muted" style="margin-top:var(--space-2)">Where every garment is drafted, sampled and tested before it is cut.</p></div>
    <div class="step"><span class="step__n">02</span><h3 class="heading-3">Indigo Passage</h3><p class="kd-muted" style="margin-top:var(--space-2)">Living dye vats and the cloth itself: where colour comes from plants.</p></div>
    <div class="step"><span class="step__n">03</span><h3 class="heading-3">The Flagship</h3><p class="kd-muted" style="margin-top:var(--space-2)">Where the collection meets you, with fittings made to measure.</p></div>
  </div>
</div></section>

<section class="section"><div class="wrap split split--rev">
  <div class="split__media"><img src="assets/img/coat-architecture.webp" alt="The Modular Travel Coat in olive, in a sandstone courtyard" loading="lazy"></div>
  <div class="stack-6">
    <span class="kd-label eyebrow">Atelier</span>
    <h2 class="heading-2">Every fitting begins with a conversation.</h2>
    <p class="body-l kd-muted">Book a private fitting, in person or by video. We adjust length, sleeve and fit to you before the garment leaves the atelier.</p>
    <a class="kd-btn kd-btn--secondary" href="atelier.html">Book a fitting</a>
  </div>
</div></section>
''' + foot('')
w('index.html', home)

# ---------- Collection ----------
cats = [('all','All'),('shirts','Shirts'),('outerwear','Outerwear'),('trousers','Trousers'),('tops','Tops'),('sets','Sets')]
coll = head('Collection — KADHAR', 'Nine garments in handwoven cotton: overshirts, jackets, coats, trousers and sets.', '', 'collection.html') + f'''
<section class="page-head"><div class="wrap">
  <span class="kd-label eyebrow">Collection 01</span>
  <h1 class="display-l">The collection</h1>
  <p class="tagline" style="margin-top:var(--space-4)">Nine garments. One cloth. Made in small batches.</p>
</div></section>
<section class="section"><div class="wrap">
  <div class="filters kd-label" role="group" aria-label="Filter garments">{''.join(f'<button data-filter="{k}" aria-pressed="{"true" if k=="all" else "false"}">{t}</button>' for k,t in cats)}</div>
  <div class="grid-5">{''.join(card(g,'') for g in G)}</div>
</div></section>
''' + foot('')
w('collection.html', coll)

# ---------- Garment pages ----------
for i, g in enumerate(G):
    nxt = G[(i+1) % len(G)]
    imgs = ''.join(f'<img src="../assets/img/{im}.webp" alt="{E(g["name"])}{" — view "+str(k+1) if k else ""}"{" loading=\"lazy\"" if k else ""}>' for k,im in enumerate(g['imgs']))
    sw = ''.join(f'<button class="kd-swatch" type="button" data-name="{n}" aria-pressed="{"true" if k==0 else "false"}"><span class="kd-swatch__dot" style="background:var(--swatch-{c})"></span>{n}</button>' for k,(n,c) in enumerate(g['colours']))
    inn = ''.join(f'<dt>{k+1:02d}</dt><dd><strong>{E(t)}</strong>{E(d)}</dd>' for k,(t,d) in enumerate(g['innov']))
    feats = ''.join(f'<li>{E(f)}</li>' for f in g['features'])
    page = head(f"{g['name']} — KADHAR", f"{g['name']}: {g['concept']}", '../', 'collection.html') + f'''
<section class="garment">
  <div class="garment__media">{imgs}</div>
  <div class="garment__info"><div class="garment__sticky">
    <a class="kd-label kd-muted" href="../collection.html" style="text-decoration:none">← Collection</a>
    <p class="kd-label kd-muted" style="margin:var(--space-8) 0 var(--space-3)">{g['n']} —</p>
    <h1 class="kd-spec__title">{E(g['name'])}</h1>
    <p class="kd-tagline" style="margin:var(--space-4) 0 var(--space-6)">{E(g['tag'])}</p>
    <div class="garment__price"><span>{price(g)}</span><span class="small kd-muted">Limited release · <span class="ph" title="Batch size placeholder">XX pieces</span></span></div>
    <div class="kd-spec__block">
      <fieldset class="kd-swatches"><legend class="kd-label" style="margin-bottom:var(--space-3)">Colourway — <span data-colour-name>{g['colours'][0][0]}</span></legend>{sw}</fieldset>
    </div>
    <div class="kd-spec__block"><h2 class="kd-label" style="margin-bottom:var(--space-3)">Size</h2><div class="sizes" aria-label="Sizes XS to XXL">{''.join(f'<span>{s}</span>' for s in ['XS','S','M','L','XL','XXL'])}</div><p class="kd-help" style="margin-top:var(--space-3)">Relaxed, oversized fit. Unsure? A fitting will get it right.</p></div>
    <p class="kd-help" style="margin:0 0 var(--space-4)">{PRICE_NOTE}</p>
    <div class="garment__actions"><a class="kd-btn kd-btn--primary" href="../atelier.html#garment-{g["n"]}">Reserve</a><a class="kd-btn kd-btn--secondary" href="../atelier.html#garment-{g["n"]}">Book a fitting</a></div>
    <p class="kd-help">Reservations open at launch. Made in small batches; we confirm timing when you reserve.</p>
    <div class="kd-spec__block" style="margin-top:var(--space-6)"><h2 class="kd-label" style="margin-bottom:var(--space-3)">Concept</h2><p>{E(g['concept'])}</p></div>
    <div class="kd-spec__block"><h2 class="kd-label" style="margin-bottom:var(--space-3)">Features</h2><ul class="kd-spec__list">{feats}</ul></div>
    <div class="kd-spec__block"><h2 class="kd-label" style="margin-bottom:var(--space-4)">Design innovation</h2><dl class="kd-innov">{inn}</dl></div>
    <div class="kd-spec__block"><h2 class="kd-label" style="margin-bottom:var(--space-3)">Fabric &amp; craft</h2><span class="kd-fabric"><span class="kd-fabric__code">{g['fabric'][0]}</span>{E(g['fabric'][1])}</span></div>
    <div class="kd-spec__block"><h2 class="kd-label" style="margin-bottom:var(--space-4)">Care</h2>{CARE}</div>
    <div class="kd-spec__block"><h2 class="kd-label" style="margin-bottom:var(--space-3)">Why it’s special</h2><p class="kd-tagline" style="font-size:20px">{E(g['special'])}</p></div>
  </div></div>
</section>
<section><div class="wrap"><a class="next-garment" href="{nxt['slug']}.html"><span class="kd-label kd-muted">Next garment</span><span class="kd-spec__title" style="font-size:clamp(24px,4vw,40px)">{nxt['n']} — {E(nxt['name'])} →</span></a></div></section>
''' + foot('../')
    w(f"garments/{g['slug']}.html", page)

# ---------- Fabrics ----------
FAB = [('KH-01','Handwoven cotton','Luxury everyday. The foundation cloth.'),('KH-02','Handwoven cotton + hemp','Structure and strength for outerwear and utility.'),
       ('KH-03','Handwoven cotton + TENCEL™ Lyocell','Fluid drape for relaxed, oversized pieces.'),('KH-04','Handwoven cotton + linen','Cool and breathable for summer.'),
       ('KH-05','Handwoven cotton + silk','A luxury capsule cloth.'),('KH-06','Handwoven cotton + bamboo','Ultra-soft, with moisture management.'),('KH-07','Travel weave','Lighter, wrinkle-resistant, made to pack.')]
fab = head('Fabrics — KADHAR', 'The KADHAR fabric library: handwoven cotton platforms KH-01 to KH-07.', '', 'fabrics.html') + f'''
<section class="page-head"><div class="wrap split">
  <div><span class="kd-label eyebrow">The fabric library</span><h1 class="display-l">Cloth first</h1></div>
  <p class="body-l kd-muted">We don’t name garments by fabric composition. We build fabric platforms, each engineered for a purpose, and design garments around them.</p>
</div></section>
<section class="section band-forest"><div class="wrap">
  <span class="kd-label eyebrow">Platforms in development</span>
  <h2 class="heading-2" style="margin-bottom:var(--space-12)">Seven cloths, one foundation.</h2>
  <div>{''.join(f'<div class="fabric-row"><span class="fabric-row__code">{c}</span><span class="heading-3">{E(n)}</span><span style="opacity:.9">{E(d)}</span></div>' for c,n,d in FAB)}</div>
  <p style="margin-top:var(--space-8);opacity:.9" class="small">Each platform is sampled, wear-tested and wash-tested before it reaches a garment.</p>
</div></section>
<section class="section"><div class="wrap">
  <span class="kd-label eyebrow">How a garment is engineered</span>
  <h2 class="heading-2" style="margin-bottom:var(--space-12)">Three layers of craft.</h2>
  <div class="steps">
    <div class="step"><span class="step__n">01</span><h3 class="heading-3">The fibre</h3><p class="kd-muted" style="margin-top:var(--space-2)">Handspun cotton, blended with hemp, linen, lyocell or bamboo for strength, cool or drape.</p></div>
    <div class="step"><span class="step__n">02</span><h3 class="heading-3">The fabric</h3><p class="kd-muted" style="margin-top:var(--space-2)">Weave, weight and finishing: enzyme softening, pre-shrinking, natural dyes.</p></div>
    <div class="step"><span class="step__n">03</span><h3 class="heading-3">The garment</h3><p class="kd-muted" style="margin-top:var(--space-2)">Shoulder slope, collar roll, stitch density, shrinkage: the details you feel before you notice.</p></div>
  </div>
</div></section>
''' + foot('')
w('fabrics.html', fab)

# ---------- Atelier ----------
opts = ''.join(f'<option value="{g["n"]}">{g["n"]} — {E(g["name"])}</option>' for g in G)
at = head('Atelier — Book a fitting — KADHAR', 'Book a private fitting with KADHAR, in person or by video. Made to measure.', '', 'atelier.html') + f'''
<section class="page-head"><div class="wrap">
  <span class="kd-label eyebrow">Atelier</span>
  <h1 class="display-l">Book a fitting</h1>
  <p class="tagline" style="margin-top:var(--space-4)">Every garment begins with a conversation.</p>
</div></section>
<section class="section"><div class="wrap split" style="align-items:start">
  <div class="stack-6" id="made-to-measure">
    <h2 class="heading-2">Made to measure</h2>
    <p class="body-l kd-muted">A private fitting, in person or by video. We take your measurements, adjust the pattern and finish the garment to fit you.</p>
    <div class="steps" style="grid-template-columns:1fr">
      <div class="step" style="border-right:0;border-bottom:1px solid var(--stone-300);padding:var(--space-6) 0"><span class="kd-label kd-muted">01</span><h3 class="heading-3">Request</h3><p class="kd-muted">Choose a garment and a time.</p></div>
      <div class="step" style="border-right:0;border-bottom:1px solid var(--stone-300);padding:var(--space-6) 0"><span class="kd-label kd-muted">02</span><h3 class="heading-3">Fitting</h3><p class="kd-muted">Measurements, fabric and fit, in conversation.</p></div>
      <div class="step" style="border-right:0;padding:var(--space-6) 0"><span class="kd-label kd-muted">03</span><h3 class="heading-3">Finishing</h3><p class="kd-muted">Your garment, adjusted and delivered.</p></div>
    </div>
  </div>
  <form class="form-grid" data-preview novalidate aria-labelledby="form-title">
    <h2 id="form-title" class="heading-3 full">Request a fitting</h2>
    <div class="kd-field"><label for="name">Name</label><input class="kd-input" id="name" name="name" autocomplete="name" required><p class="kd-help">Required.</p></div>
    <div class="kd-field"><label for="email">Email</label><input class="kd-input" id="email" name="email" type="email" autocomplete="email" required><p class="kd-help">We confirm your fitting here.</p></div>
    <div class="kd-field"><label for="phone">Phone</label><input class="kd-input" id="phone" name="phone" type="tel" autocomplete="tel"><p class="kd-help">Optional, for a call back.</p></div>
    <div class="kd-field"><label for="mode">Fitting</label><select class="kd-input" id="mode" name="mode"><option>In person</option><option>Video call</option></select></div>
    <div class="kd-field full"><label for="garment">Garment</label><select class="kd-input" id="garment" name="garment"><option value="">Not sure yet</option>{opts}</select></div>
    <div class="kd-field full"><label for="date">Preferred date</label><input class="kd-input" id="date" name="date" type="date"></div>
    <div class="kd-field full"><label for="notes">Notes</label><textarea class="kd-input" id="notes" name="notes" placeholder="Anything we should know about fit or occasion"></textarea></div>
    <div class="full"><button class="kd-btn kd-btn--primary" type="submit">Request fitting</button></div>
    <p class="notice full" tabindex="-1" hidden>Preview only: fitting requests are not connected yet. Nothing has been sent.</p>
  </form>
</div></section>
''' + foot('')
w('atelier.html', at)

# ---------- House ----------
house = head('House — KADHAR', 'The KADHAR standard: handwoven cloth, plant-based colour, small batches.', '', 'house.html') + f'''
<section class="page-head"><div class="wrap">
  <span class="kd-label eyebrow">The house</span>
  <h1 class="display-l">A quest<br>for mastery</h1>
</div></section>
<section class="section"><div class="wrap split">
  <div class="stack-6">
    <p class="body-l">KADHAR bridges the heritage of rural Indian craftsmanship and the way people dress in cities today. We reject fast fashion in favour of unhurried intent: garments built to become modern heirlooms.</p>
    <p class="kd-muted">Minimal, gender-neutral silhouettes for people who move: ease of movement first, utility always, ornament never for its own sake.</p>
  </div>
  <div class="split__media"><img src="assets/img/kimono-architecture.webp" alt="The Urban Kimono Jacket in charcoal, in a stone courtyard" loading="lazy"></div>
</div></section>
<section class="section section--stone"><div class="wrap">
  <span class="kd-label eyebrow">Our standard</span>
  <h2 class="heading-2" style="margin-bottom:var(--space-12)">What every garment answers to.</h2>
  <div class="steps">
    <div class="step"><span class="step__n">01</span><h3 class="heading-3">Material wisdom</h3><p class="kd-muted" style="margin-top:var(--space-2)">Handspun, handwoven cotton and natural fibre blends, chosen for how they breathe and age.</p></div>
    <div class="step"><span class="step__n">02</span><h3 class="heading-3">Plant-based colour</h3><p class="kd-muted" style="margin-top:var(--space-2)">Indigos, earth browns and pale yellows drawn from natural dyes.</p></div>
    <div class="step"><span class="step__n">03</span><h3 class="heading-3">Small batches</h3><p class="kd-muted" style="margin-top:var(--space-2)">Made at the pace of the loom, in limited drops, so nothing is overproduced.</p></div>
  </div>
</div></section>
<section class="section" id="care"><div class="wrap split">
  <div class="stack-6"><span class="kd-label eyebrow">Care</span><h2 class="heading-2">Cloth that improves with wear.</h2><p class="kd-muted">Wash cold, dry in shade, iron warm. Handwoven cotton softens with every wash; raw hems are meant to fray a little.</p></div>
  {CARE}
</div></section>
''' + foot('')
w('house.html', house)

# ---------- Journal ----------
stories = [('The Basement','How a garment is drafted, sampled and tested before it is cut.','overshirt-sculpture'),
           ('Indigo Passage','Inside the dye vats: where KADHAR colour comes from.','cargo-forest'),
           ('The Flagship','A room built for fittings, not for crowds.','coat-sculpture')]
jr = head('Journal — KADHAR', 'Stories from the loom, the dye vat and the atelier.', '', 'journal.html') + f'''
<section class="page-head"><div class="wrap">
  <span class="kd-label eyebrow">Journal</span>
  <h1 class="display-l">From the loom</h1>
  <p class="tagline" style="margin-top:var(--space-4)">Stories of craft, cloth and the people behind them.</p>
</div></section>
<section class="section"><div class="wrap grid-3">
  {''.join(f'<article class="story"><div class="story__media"><img src="assets/img/{im}.webp" alt="" loading="lazy"></div><span class="kd-label kd-muted">Story · <span class="ph" title="Publication date placeholder">Coming soon</span></span><h2 class="heading-3">{t}</h2><p class="kd-muted">{d}</p></article>' for t,d,im in stories)}
</div></section>
''' + foot('')
w('journal.html', jr)
print('built', len(G) + 6, 'pages')
