# Olga Detailing

Repo for Olga Detailing (Olga, Orcas Island, WA) — hosts the business's
website and a Claude Code skill that acts as a "PR employee": it drafts
marketing and customer-communication content — Facebook posts, review
replies, booking messages, and website copy — for the owner to review and
post herself.

## Website

A simple static site lives at the repo root (`index.html`, `styles.css`,
`script.js`, `images/`).

**Preview locally:**

    python3 -m http.server 8000

then open `http://localhost:8000/` in a browser.

**Before launch**, open `index.html` and fill in the `TODO(owner)` items:
the real phone number, Facebook Page URL, and Google Business Profile URL.
Drop real photos into `images/` following `images/README.md` — the site
already references the expected filenames.

**Deploying on GitHub Pages:**
1. Merge this branch into `main`.
2. In the repo's Settings → Pages, set Source = "Deploy from a branch",
   Branch = `main`, folder = `/ (root)`.
3. GitHub will publish the site at `https://<owner>.github.io/Olga-Detailing/`.

Keep the pricing on the site in sync with
`.claude/skills/pr-employee/business-info.md` if prices change.

## Usage

In Claude Code, run:

    /pr-employee <what you need>

Examples:
- `/pr-employee draft a Google review reply for a customer named Jake who loved the ceramic coating`
- `/pr-employee write 3 Facebook posts for a summer tourist season promo`
- `/pr-employee reply to a customer asking how much a full detail and ceramic coating would cost`
- `/pr-employee write a one-line website tagline`

The skill only drafts text — it never posts or sends anything automatically.

See `.claude/skills/pr-employee/business-info.md` for current pricing,
audience/channels, and brand voice — edit that file directly when prices or
tone need updating.
