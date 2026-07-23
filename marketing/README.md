# Marketing materials

Print-ready flyers and posters for Olga Detailing, meant for bulletin boards
and around-town posting. Not part of the live website.

| File | Notes |
|---|---|
| `poster-detailing.html` / `.png` / `.pdf` | Main bulletin board poster. Redesigned to cover all three service lines (Auto, Plane, Boat) with equal billing via an icon row, plus a Website QR. `poster-detailing.pdf` is the print-ready file (8.5in x 11.33in). |
| `flyer-boat.html` / `.png` / `.pdf` | Boat-only flyer, same visual system as the main poster (logo, Baloo 2 type, coral phone accent, Website QR). Leads with the "owned and operated by an experienced boater" credibility line, a 2x2 icon grid of the four real boat service tiers (Wash / Wash & Polish / Wash, Polish & Wax / Full Ceramic Package, pulled from business-info.md, not generic buzzwords), a "by custom quote" note, and a bottom tagline banner. Layout (icon grid + bottom banner) was inspired by a competitor's bulletin-board flyer Knox photographed, content and branding are Olga's own, not copied. |
| `poster-auto-detailing-original.png` | Knox's original auto-only poster (Instagram QR), kept as a source/reference. |
| `canva-card-front.png` / `canva-card-back.png` | **This is the real business card Knox actually uses** (made in Canva, uploaded by him), the one to print. Front (logo, "Premium Detailing," phone, Instagram, Facebook) is untouched. Back is a Website QR with the orca silhouette blended directly into the QR pattern (black orca embedded in the code's center, error-correction level H so it still scans, verified working), rounded corners, "Scan to Book" / olgadetailing.com caption underneath. Replaced an earlier version that just placed a plain QR next to the standalone logo. |
| `business-card.html` / `.png` / `.pdf` | An earlier from-scratch draft of a general contact card, superseded by the real Canva card above. Left in place in case it's useful as a second option, but `canva-card-front/back.png` is the one to hand out. |
| `review-card.html` / `.png` / `.pdf` | The "leave us a review" card handed to customers after a job (business card sized, 3.5in x 2in). Front has the logo, a Google review QR, phone number, and the website (`olgadetailing.com`) as a small text line, no second QR, the card was already tight on space so text fit better than another QR. `review-card.pdf` is the print-ready file. |
| `qr-website.png` | Standalone Website QR (olgadetailing.com), styled with dot modules and rounded finder eyes to match Knox's original Instagram QR aesthetic. Reused across posters/cards. |

## Poster design notes

`poster-detailing.html` is a from-scratch redesign, not a patch of the
original. Reasoning, in case it needs updating later:

- All three services (Auto, Plane, Boat) get equal visual weight, an icon
  row with the same card treatment for each, since the poster's whole job is
  to announce we do all three, not just auto.
- Icons are Lucide (car/plane/sailboat, ISC license), thin white line icons
  rather than solid/filled glyphs, reads more premium and matches the
  logo's fine script linework better than a chunky solid icon would.
- Bullets are worded to stay true for all three service lines (e.g. "Wash,
  polish, wax & ceramic coating" applies to auto, plane, and boat alike,
  planes/boats don't get interior service, so the copy avoids implying they
  do). See `business-info.md` for what's actually included per vehicle type.
- The phone number is the one color accent (site's CTA coral, `#D98358`-ish)
  against an otherwise black-and-white design, keeping a single, unmistakable
  call to action per basic poster design practice for an older, phone-first
  audience.
- One local detail only ("Serving Orcas Island & the San Juan Islands"), per
  the brand voice guide's "max one local detail per piece" rule.

To regenerate the Website QR (e.g. if the domain ever changes), use the
`qrcode` Python library with a circle module drawer plus hand-drawn rounded
finder eyes so it keeps the dot-style look, then swap `qr-website.png` and
re-render `poster-detailing.html` / `review-card.html` with Playwright.

The orca-in-QR version on `canva-card-back.png` uses the same technique plus
`qrcode`'s `embedded_image` parameter (error correction level H, so the
center can be covered) with a black silhouette of just the orca cropped out
of `images/logo-full.png` (top ~150px, before the "Olga" script text
starts). Always re-verify with OpenCV's `QRCodeDetector` after regenerating,
embedding an image is the one step that can break scannability if the logo
is sized too large relative to the code.

To re-render the poster PNG: viewport 864x1152, deviceScaleFactor 2. For the
PDF: `page.pdf()` at 8.5in x 11.333in.

To re-render the review card PNG: viewport 336x192, deviceScaleFactor 3.125.
For the PDF: `page.pdf()` at 3.5in x 2in.
