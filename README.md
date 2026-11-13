# KADHAR

Two static websites from one brand family, plus the shared design system.

| Folder | Site | Domain | What |
| --- | --- | --- | --- |
| `luxury/` | KADHAR | kadhar.in | Luxury house: 9 handwoven-cotton garments, ₹40,000–₹5,00,000, fittings by appointment |
| `streetwear/` | KADHAR Street | kadhar.store | Gen Z / Gen Alpha streetwear: Baggy & Oversized, every piece ₹1,999 |
| `design-system/` | — | — | DESIGN.md + CSS tokens shared by both |
| `tools/` | — | — | Page generators (`build_luxury.py`, `build_street.py`) |

Plain HTML/CSS/JS, no framework, no build step on the server. Each site folder is deployed as-is.

## Editing
Garment and product data live at the top of `tools/build_luxury.py` and `tools/build_street.py`.
Edit, then run `python3 tools/build_luxury.py` / `python3 tools/build_street.py` and commit the generated HTML.

## Hosting (Hostinger)
Each domain auto-deploys from `main` with the deploy directory set to its folder: `luxury` for kadhar.in, `streetwear` for kadhar.store.

## Placeholders to replace before launch
- Logo: `LOGO PLACEHOLDER` comment in each header (text wordmark for now)
- Luxury per-garment prices: all show "From ₹40,000"; add a `price` field per garment to set exact prices
- Batch sizes (`XX pieces`), company/GST details, street size-chart measurements (`XX`)
- Photos: concept images from the product deck; swap files in `*/assets/img/` keeping the names
- Forms (fitting request, newsletter, drop access) show a "Preview only" notice; not connected to a backend
- Privacy / Terms / Shipping / Instagram links are `#`

## Copy rules
Say "handwoven cotton", never "khadi", and no charkha mark, until the KVIC Khadi Mark certificate is issued.
