# Marketing materials

Print-ready flyers and posters for Olga Detailing, meant for bulletin boards
and around-town posting. Not part of the live website.

| File | Notes |
|---|---|
| `poster-auto-detailing.png` | Auto detailing poster. Same layout as the original, but the QR now points to olgadetailing.com instead of Instagram. This is the one to print. |
| `poster-auto-detailing-original.png` | Knox's original poster (Instagram QR), kept as a source/reference. |
| `review-card.html` / `.png` / `.pdf` | The "leave us a review" card handed to customers after a job (business card sized, 3.5in x 2in). Front has the logo, a Google review QR, phone number, and the website (`olgadetailing.com`) as a small text line, no second QR, the card was already tight on space so text fit better than another QR. `review-card.pdf` is the print-ready file. |

To regenerate the Website QR on the poster (e.g. if the domain ever changes),
use the `qrcode` Python library with a circle module drawer plus hand-drawn
rounded finder eyes so it keeps the same dot-style look as the original,
sized 478x478 and pasted at (624, 1774) on the original poster. Ask Claude to
redo this, it knows the exact layout math used here.

To update the review card, edit `review-card.html` and re-render with
Playwright at 300dpi (viewport 336x192, deviceScaleFactor 3.125) for the PNG,
and `page.pdf()` at 3.5in x 2in for the print file.
