# Images

| Filename | Used for | Recommended size | Notes |
|---|---|---|---|
| `logo.png` | Header logo | ~200×200, transparent PNG | ✅ In use |
| `logo-full.png` | Footer logo lockup | ~330×354, transparent PNG | ✅ In use |
| `favicon.png` | Browser tab icon | 32×32 or 64×64 | ✅ In use |
| `hero.jpg` | Homepage top banner | 1600×900 (16:9), landscape | ✅ In use |
| `gallery-1.jpg` … `gallery-9.jpg` | Photo gallery grid | 800×800 (square) preferred | ✅ In use, 9 of 9 slots filled |
| `nissan-before.jpg` / `nissan-after.jpg` | Before & after slider (Gallery section) | same crop/framing for both so the comparison lines up | ✅ In use |
| `review-qr.png` | QR code on the printable review card | 660×660 | ✅ In use, links to the Google review page |

The gallery currently shows 9 photos (`gallery-1.jpg` through `gallery-9.jpg`).
To add a 10th or later, drop the file in here (e.g. `gallery-10.jpg`) and ask
Claude to add the matching slot in `index.html`, empty slots aren't shown
automatically, so a new photo needs both the file and a small HTML addition
to appear. Any visible license plates or other identifying details should
be blurred before the photo goes live, ask Claude to handle this when
adding a new photo.

The before & after slider (`.ba-slider` in `index.html`, styles in
`styles.css`, wiring in `script.js`) needs two photos of the *same* vehicle,
same panel, same framing, one before and one after, named
`nissan-before.jpg` / `nissan-after.jpg` currently. To add another
before/after pair (a different vehicle, or a second one), duplicate the
`.ba-slider` block in the Gallery section with new image filenames and a new
`aria-label`, the CSS/JS already support multiple sliders on one page.
