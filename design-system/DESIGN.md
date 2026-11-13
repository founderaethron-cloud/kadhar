# DESIGN.md — KADHAR website

Source of truth for every KADHAR page. Values live in `kadhar-tokens.css`; components in the KADHAR design system (`components/bundle.css`, classes prefixed `kd-`). Pages use token names, never raw hex or px.

**Direction:** linen ground, one rust signal, square cuts, two voices of type. A magazine, not a marketplace.
Built from: Kadhar Product Design deck (primary), Strategic Business Plan, Product & Roadmap, Luxury Brand Bible.

---

## Colour

| Token | Light | Dark | Role |
| --- | --- | --- | --- |
| `--linen-100` | #EEE8E1 | #161311 | Page background |
| `--linen-50` | #F6F2EC | #201C19 | Cards, inputs, panels |
| `--stone-200` | #E2D9CE | #2A2420 | Alternate band, image placeholder |
| `--stone-300` | #CFC4B6 | #3A332E | 1px hairlines (decorative) |
| `--stone-500` | #8C7F72 | #6E645B | Control borders (3.2:1) |
| `--ink` | #1F1B18 | #EEE8E1 | Text, headings, wordmark |
| `--ink-muted` | #62574E | #A99D91 | Secondary text (5.8:1 / 7:1) |
| `--rust` | #622916 | #8A3A20 | **Brand.** Primary button, selected, footer band |
| `--rust-deep` | #4A1E10 | #9E4728 | Hover/pressed on rust |
| `--rust-text` | #622916 | #E39A7C | Links, accent text |
| `--on-rust` | #F6F2EC | #F6F2EC | Text on rust (10:1 / 7:1) |
| `--forest` | #2E4636 | #2E4636 | **Accent.** Craft/fabric bands, Made-to-measure badge. Never buttons |
| `--forest-text` / `--on-forest` | #2E4636 / #F6F2EC | #93B79C / #F6F2EC | Forest as text / text on forest |
| `--clay` | #B4532A | #C0643A | Decorative terracotta only |
| `--success` `--warning` `--error` | #2F6B3A · #8A5A0B · #A8281A | #7FC28C · #E2B25A · #F08A78 | States, always with text/icon |
| `--focus` | #1F1B18 | #EEE8E1 | 2px focus ring, 2px offset |
| `--swatch-*` | ivory, stone, sand, olive, forest, slate, charcoal, indigo | same | Product colourway dots only |

Ratio: ~80% linen/stone, 12% ink, 5–8% rust, forest only in its own bands. One rust button per view. No gradients. Dark theme = lookbook/story pages, not the default shop.

## Typography

Archivo (300–800) for everything; Newsreader Italic for one tagline line per screen.

| Class | Size / line | Weight | Use |
| --- | --- | --- | --- |
| `.display-xl` | 120 / 0.9, −0.04em (56 mobile) | 800 | Wordmark-scale hero, uppercase |
| `.display-l` | 72 / 0.95 (40 mobile) | 800 | Collection headlines |
| `.title-xl` | 48 / 1.05 (32 mobile) | 300 | `01 — GARMENT NAME` |
| `.heading-2` | 28 / 1.2 | 400 | Section heads |
| `.heading-3` | 20 / 1.35 | 500 | Feature names |
| `.body-l` | 18 / 1.65 | 400 | Concept copy, max 64ch |
| `.body` | 16 / 1.625 | 400 | Default, max 68ch |
| `.small` | 14 / 1.55 | 400 | Specs, captions |
| `.label` | 12 / 1.33, +0.12em | 600 | Uppercase labels, nav, buttons (13px) |
| `.tagline` | 24 / 1.45 italic | 400 | One poetic line |

Signature: 800 for the brand voice, 300 for garments. Never 800 under 40px.

## Spacing & layout

`--space-1` 4 · `-2` 8 · `-3` 12 · `-4` 16 · `-6` 24 · `-8` 32 · `-12` 48 · `-16` 64 · `-24` 96 · `-40` 160.
12-column grid, `--width-page` 1440, gutters `--space-12` / `--space-6` mobile. Sections `--space-24` / `--space-16`. Reading width `--width-text` 680. Asymmetric by default (text 4–5 cols, image 7–8); only the Manifesto is centered.

## Shape & depth

`--radius-0` everywhere; `--radius-sm` 2px tags only; `--radius-full` swatches only. No shadows on the page; `--shadow-overlay` for drawers, bag, menus. Structure comes from hairlines and the stone band.

## Components

Button (primary rust / secondary ink outline / quiet link) · SiteHeader (Collection, Fabrics, Atelier, Journal + Book a fitting, Bag) · ProductCard (flat lay 4:5, number, light uppercase name, fabric code, price, dots) · GarmentSpec (deck spec sheet: Concept, Features, Design innovation 01–04, Fabric & craft, Colourways, Care, actions) · FabricChip (`KH-01` forest tile + composition) · ColourwayPicker · FittingForm · Manifesto (forest band, serif italic) · SiteFooter (rust band, huge wordmark).
States everywhere: hover, `:focus-visible` 2px `--focus`, disabled `--stone-200` + reason in label.

## Imagery & icons

Editorial (stone architecture, desert, sculptural set with polygons and terracotta), flat lay on stone, detail close-ups in rows of 4–5. Square corners, warm light, no white cut-outs. Technical flats as 1px ink line art. Icons: Lucide, 1.5px stroke, 20px, ink. No emoji.

## Voice

Quiet confidence. "Introducing…", "Crafted in…", "Limited release · 40 pieces", "Book a fitting". Never "Hurry", "Sale", "Offer", "!". Garments: `01 — THE FLOATING OVERSHIRT`. Fabric code before adjectives.
**Say "handwoven cotton", not "khadi", and no charkha mark, until the KVIC Khadi Mark certificate is issued.**
