# Service guides

Printable how-to guides for every service listed on olgadetailing.com. Written
for an employee who has never done the job before: plain language, numbered
steps, and the exact product named at each step so there is no guessing.

| File | Covers |
|---|---|
| `auto-detailing-guide.pdf` | Quick Wash, Standard / Premium / Signature Detail, and all six add-ons |
| `boat-detailing-guide.pdf` | Wash, Wash & Polish, Wash Polish & Wax, Full Ceramic Package |
| `plane-detailing-guide.pdf` | Wash, Wash & Polish, Wash Polish & Wax, Full Ceramic Package |

The `.pdf` is the one to print. The `.html` is the source, edit that and
re-render if a product or step changes.

## Products these are written around

Knox's brands: **Koch Chemie**, **Adam's**, **P&S**, and **Aero Cosmetics**
(aviation). Boat products come from the earlier marine research. Anything shown
as a red chip in a guide is a product not yet on the shelf.

## Rebuilding after an edit

The guides are generated from a single script so the three stay consistent.
Edit the content in that script rather than hand-editing HTML, then:

```
python3 build.py                     # writes the three .html files
# then render each to PDF with Playwright, Letter format, printBackground: true
```

Note the cover uses `images/logo-full-black.png`, a black version of the logo
made for print. The normal `logo-full.png` is white and disappears on paper.

## Keeping them accurate

If a price, service, or product changes, update three places so they don't
drift apart: the website (`index.html`), the guide, and
`.claude/skills/pr-employee/business-info.md`.
