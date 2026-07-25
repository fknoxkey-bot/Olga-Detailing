"""Generate the three printable service guides for Olga Detailing Services."""
import html, os, pathlib

OUT = pathlib.Path("/home/user/Olga-Detailing/guides")
OUT.mkdir(parents=True, exist_ok=True)

CSS = """
@page { size: letter; margin: 0.6in 0.65in 0.75in; }
* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: 'Inter', Arial, Helvetica, sans-serif; color: #16191c; font-size: 10.4pt; line-height: 1.5; }
h1,h2,h3,h4 { font-weight: 800; letter-spacing: -0.02em; color: #0b0d0f; }

.cover { text-align: center; padding-top: 0.7in; page-break-after: always; }
.cover img { width: 190px; margin: 0 auto 26px; display: block; }
.cover h1 { font-size: 34pt; line-height: 1.05; }
.cover .kind { font-size: 12pt; font-weight: 700; letter-spacing: .16em; text-transform: uppercase; color: #b0642f; margin-bottom: 14px; }
.cover .blurb { max-width: 4.6in; margin: 18px auto 0; font-size: 10.5pt; color: #4a5157; }
.cover .foot { margin-top: 46px; font-size: 9pt; color: #7b8288; }

h2.sec { font-size: 15.5pt; margin: 0 0 4px; padding-bottom: 7px; border-bottom: 2.5px solid #16191c; }
.secsub { font-size: 9.2pt; color: #6b7278; margin-bottom: 14px; }
.block { page-break-inside: avoid; margin-bottom: 22px; }
.newpage { page-break-before: always; }

/* service header */
.svc { page-break-before: always; }
.svc-head { border-left: 5px solid #b0642f; padding-left: 12px; margin-bottom: 12px; }
.svc-head h2 { font-size: 19pt; line-height: 1.15; }
.svc-meta { font-size: 9pt; color: #6b7278; margin-top: 3px; }
.svc-meta b { color: #16191c; }
.svc-what { background: #f5f6f7; border-radius: 4px; padding: 9px 12px; font-size: 9.6pt; margin-bottom: 16px; }

/* steps */
.step { display: flex; gap: 11px; margin-bottom: 13px; page-break-inside: avoid; }
.num { flex: 0 0 22px; height: 22px; border-radius: 50%; background: #16191c; color: #fff;
       font-size: 9.5pt; font-weight: 800; display: flex; align-items: center; justify-content: center; }
.step-body { flex: 1; }
.step-body h4 { font-size: 11pt; margin-bottom: 3px; }
.step-body p { margin-bottom: 4px; }
.step-body ul { margin: 4px 0 0 16px; }
.step-body li { margin-bottom: 3px; }

.prod { display: inline-block; background: #eef2f4; border: 1px solid #d3dade; border-radius: 3px;
        padding: 1px 6px; font-size: 9.2pt; font-weight: 700; color: #14304a; }
.buy { background: #fdeaea; border-color: #f2bcbc; color: #8d2020; }

.warn { border-left: 4px solid #c0392b; background: #fdf3f2; padding: 8px 12px; margin: 10px 0;
        font-size: 9.5pt; page-break-inside: avoid; }
.warn b { color: #a4271b; }
.tip { border-left: 4px solid #2b7a4b; background: #f1f8f3; padding: 8px 12px; margin: 10px 0; font-size: 9.5pt; }
.tip b { color: #1f5c38; }

table { width: 100%; border-collapse: collapse; font-size: 9.5pt; margin: 8px 0 4px; }
th { background: #16191c; color: #fff; text-align: left; padding: 6px 9px; font-size: 8.8pt;
     text-transform: uppercase; letter-spacing: .05em; }
td { border: 1px solid #dde2e5; padding: 6px 9px; vertical-align: top; }
tr:nth-child(even) td { background: #fafbfb; }

ul.rules { margin-left: 17px; }
ul.rules li { margin-bottom: 6px; }

.check { border: 1.5px solid #16191c; border-radius: 4px; padding: 13px 16px; page-break-inside: avoid; }
.check h3 { font-size: 12pt; margin-bottom: 8px; }
.check li { list-style: none; margin-bottom: 5px; padding-left: 22px; position: relative; font-size: 9.8pt; }
.check li:before { content: ""; position: absolute; left: 0; top: 1px; width: 12px; height: 12px;
                   border: 1.5px solid #16191c; border-radius: 2px; }
.pfoot { margin-top: 20px; padding-top: 8px; border-top: 1px solid #dde2e5; font-size: 8.4pt; color: #8b9298; }
"""

LOGO = "../images/logo-full-black.png"

A_TIRE = "Adam's Tire Shine"
A_GLASS = "Adam's Glass Cleaner"
A_CLAY = "Adam's Visco Clay Bar Kit"
A_CER = "Adam's Graphene Ceramic Coating"



def P(name, buy=False):
    cls = "prod buy" if buy else "prod"
    return f'<span class="{cls}">{html.escape(name)}</span>'


def render_steps(steps):
    out = []
    for i, (head, body) in enumerate(steps, start=1):
        lines = "".join(f"<li>{b}</li>" for b in body) if isinstance(body, list) else f"<p>{body}</p>"
        inner = f"<ul>{lines}</ul>" if isinstance(body, list) else lines
        out.append(f'<div class="step"><div class="num">{i}</div>'
                   f'<div class="step-body"><h4>{head}</h4>{inner}</div></div>')
    return "".join(out)


def render_service(s):
    parts = [f'<div class="svc"><div class="svc-head"><h2>{s["name"]}</h2>'
             f'<div class="svc-meta">{s["meta"]}</div></div>']
    if s.get("what"):
        parts.append(f'<div class="svc-what">{s["what"]}</div>')
    for blk in s["blocks"]:
        if blk[0] == "steps":
            parts.append(render_steps(blk[1]))
        elif blk[0] == "warn":
            parts.append(f'<div class="warn"><b>Watch out.</b> {blk[1]}</div>')
        elif blk[0] == "tip":
            parts.append(f'<div class="tip"><b>Tip.</b> {blk[1]}</div>')
        elif blk[0] == "h":
            parts.append(f'<h3 style="font-size:12pt;margin:16px 0 6px;">{blk[1]}</h3>')
        elif blk[0] == "p":
            parts.append(f'<p style="margin-bottom:8px;">{blk[1]}</p>')
    if s.get("done"):
        items = "".join(f"<li>{d}</li>" for d in s["done"])
        parts.append(f'<div class="check" style="margin-top:14px;"><h3>Done when</h3><ul>{items}</ul></div>')
    parts.append("</div>")
    return "".join(parts)


def build(fname, kind, title, blurb, kit_rows, rules, services, buy_rows, closing_note):
    kit = "".join(
        f"<tr><td><b>{r[0]}</b></td><td>{r[1]}</td><td>{r[2]}</td></tr>" for r in kit_rows)
    rl = "".join(f"<li>{r}</li>" for r in rules)
    buy = "".join(f"<tr><td><b>{b[0]}</b></td><td>{b[1]}</td><td>{b[2]}</td></tr>" for b in buy_rows)
    svcs = "".join(render_service(s) for s in services)

    doc = f"""<!DOCTYPE html><html><head><meta charset="UTF-8">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap" rel="stylesheet">
<style>{CSS}</style></head><body>

<div class="cover">
  <img src="{LOGO}" alt="">
  <div class="kind">{kind}</div>
  <h1>{title}</h1>
  <div class="blurb">{blurb}</div>
  <div class="foot">Olga Detailing Services &middot; Orcas Island, WA &middot; olgadetailing.com</div>
</div>

<h2 class="sec">The Kit</h2>
<div class="secsub">Exact products. Anything in <span class="prod buy">red</span> is not on the shelf yet, see the last page.</div>
<table><tr><th style="width:31%">Product</th><th style="width:26%">What it is</th><th>What it's for</th></tr>{kit}</table>

<h2 class="sec" style="margin-top:26px;">Rules That Don't Change</h2>
<div class="secsub">These apply to every single job. Read them once, follow them always.</div>
<ul class="rules">{rl}</ul>

{svcs}

<div class="newpage">
<h2 class="sec">Still Need To Buy</h2>
<div class="secsub">{closing_note}</div>
<table><tr><th style="width:33%">Item</th><th style="width:30%">Why</th><th>Roughly</th></tr>{buy}</table>
<div class="pfoot">Olga Detailing Services &middot; internal training guide &middot; keep with the kit</div>
</div>

</body></html>"""
    path = OUT / fname
    path.write_text(doc)
    print("wrote", path)


# ==========================================================================
#  AUTO
# ==========================================================================
auto_kit = [
    ("Koch Chemie Gentle Snow Foam", "pH-neutral foam soap", "First layer of foam on the whole car. Safe on wax and coatings."),
    ("Koch Chemie Nano Magic Shampoo", "Wash soap", "The two-bucket contact wash."),
    ("P&amp;S Brake Buster", "Wheel cleaner, non-acid", "Wheels, barrels, and lug areas."),
    ("Koch Chemie Reactive Rim Cleaner", "Iron / fallout remover", "Dissolves brake dust and iron specks. Turns purple as it works."),
    ("Adam's Visco Clay Bar Kit", "Clay bar + lube", "Pulls out bonded grit the wash leaves behind."),
    ("Koch Chemie Heavy Cut H9.01", "Cutting compound", "Removes swirls and light scratches."),
    ("Koch Chemie Micro Cut M3.01", "Finishing polish", "Brings the gloss back after cutting."),
    ("Koch Chemie Panel Star", "Panel prep / degreaser", "Wipes off polish oils so wax or coating actually sticks."),
    ("P&amp;S Bead Maker", "Spray sealant", "The Wax add-on. Fast, glossy, lasts a few months."),
    ("Adam's Graphene Ceramic Coating", "Ceramic coating", "The $225 add-on. Roughly a year of protection."),
    ("Koch Chemie Green Star", "All-purpose cleaner", "Dilute it. Door jambs, engine bay, dirty plastics."),
    ("P&amp;S Xpress Interior Cleaner", "Interior cleaner", "Dash, console, panels, leather, vinyl."),
    ("P&amp;S Carpet Bomber", "Carpet &amp; upholstery cleaner", "Shampooing floors and seats."),
    ("Adam's Glass Cleaner", "Glass cleaner", "Inside and outside of every window."),
    ("Adam's Tire Shine", "Tire dressing", "Final touch on the tires."),
    ("Steam cleaner", "You already own this", "Vents, seams, cup holders, and lifting stains."),
]
auto_rules = [
    "<b>Never work on hot paint or in direct sun.</b> Move the car into shade or wait. Product dries on the panel and stains it.",
    "<b>Top down, always.</b> Roof first, rockers and bumpers last. The lowest parts are the dirtiest and you don't want that grit going back up.",
    "<b>Two buckets, every wash.</b> One with soap, one with plain rinse water and a grit guard. Rinse the mitt in the plain bucket before it goes back into the soap. This is what prevents swirl marks.",
    "<b>Wheels come first, with their own bucket and brushes.</b> Brake dust in your paint mitt will scratch the car.",
    "<b>Never let anything dry on the paint.</b> Work one panel at a time and rinse it before it flashes.",
    "<b>Fresh towel, folded in fours.</b> When a side gets dirty, flip it. When all four are used, get a new towel. A dropped towel is done, it goes in the laundry bag, not back on the car.",
    "<b>Check with the customer before you touch aftermarket wraps, matte paint, or PPF.</b> Wax and some chemicals will ruin a matte finish.",
    "<b>Take before photos every job.</b> Existing dents, scratches, and cracked trim get photographed before you start. This protects you.",
]

auto_services = [
    {
        "name": "Quick Wash",
        "meta": "<b>$60</b> flat &middot; about <b>45 minutes</b> &middot; exterior only, no interior work",
        "what": "A proper outside wash and dry. More than a rinse, less than a detail. No clay, no wax, nothing touches the inside of the car.",
        "blocks": [
            ("steps", [
                ("Walk around the car with the customer", [
                    "Point out any damage you see and photograph it.",
                    "Ask if there's anything specific bothering them.",
                ]),
                ("Wheels and tires first", [
                    f"Spray {P('P&amp;S Brake Buster')} on one wheel at a time, cold wheel only.",
                    "Let it sit 1 to 2 minutes. Do not let it dry.",
                    "Agitate the face, the barrel, and behind the spokes with your wheel brushes.",
                    "Rinse completely before moving to the next wheel.",
                ]),
                ("Foam the whole car", [
                    f"Cover the car in {P('Koch Chemie Gentle Snow Foam')} from the bottom up, so you can see where you've been.",
                    "Let it dwell 3 to 5 minutes. It's loosening dirt so your mitt doesn't have to drag it.",
                    "Rinse from the top down until the foam is gone.",
                ]),
                ("Two-bucket contact wash", [
                    f"Soap bucket gets {P('Koch Chemie Nano Magic Shampoo')} per the bottle's dilution.",
                    "Wash top down, one panel at a time, straight lines not circles.",
                    "Rinse the mitt in the plain bucket between every panel.",
                ]),
                ("Final rinse", [
                    "Pull the nozzle off and let water sheet off the panels. Much less to dry.",
                    "Open the doors and rinse the jambs and sills.",
                ]),
                ("Dry", [
                    "Big plush drying towel, blot and drag, don't scrub.",
                    "Dry the jambs, mirrors, and around badges and handles, that's where drips show up later.",
                ]),
                ("Finish", [
                    f"{P(A_TIRE)} on the tires, applicator not spray, so it doesn't sling onto the paint.",
                    f"{P(A_GLASS)} on the outside of all glass.",
                ]),
            ]),
            ("warn", "Cold wheels only. Wheel cleaner on a hot brake rotor flashes off instantly and can stain the finish."),
        ],
        "done": ["No water spots or drips anywhere, including jambs and mirrors.",
                 "Wheel faces and barrels are clean, no brake dust left in the spokes.",
                 "Glass is clear from the outside with no streaks.",
                 "Tires are even, no sling on the paint."],
    },
    {
        "name": "Standard Detail",
        "meta": "<b>$200 / $220 / $275</b> by size &middot; about <b>2 to 3 hours</b> &middot; the base every other package builds on",
        "what": "Full inside and out. Everything in the Quick Wash, plus a complete interior: vacuum, shampoo carpets and upholstery, stain removal, deodorize, all glass, and a full wipe-down.",
        "blocks": [
            ("h", "Exterior"),
            ("p", "Run the entire Quick Wash first, steps 1 through 7. Then come inside."),
            ("h", "Interior"),
            ("steps", [
                ("Empty it out", [
                    "Every floor mat comes out. All trash out. Personal belongings into a bag, hand them to the customer, never throw anything away that isn't obviously trash.",
                    "Check under seats, in seat back pockets, and in the spare tire well.",
                ]),
                ("Dry brush and vacuum", [
                    "Brush the carpets and seats first to lift dirt out of the fibers, then vacuum.",
                    "Vacuum top down: headliner area, seats, seat rails, console, then floors last.",
                    "Use the crevice tool along seat rails and between the seat and console. That's where the crumbs are.",
                ]),
                ("Shampoo carpets and cloth seats", [
                    f"Spray {P('P&amp;S Carpet Bomber', buy=True)} onto the carpet, not soaking it, just damp.",
                    "Agitate with a stiff drill brush or hand brush until it foams up.",
                    "Blot hard with a dry microfiber to pull the dirt out. Fold to a clean side and repeat.",
                    "Repeat on any spot that's still dark. Patience beats more chemical.",
                ]),
                ("Steam the tight spots", [
                    "Steam the vents, seams, cup holders, shifter surround, and door pockets.",
                    "Wipe immediately behind the steam with a clean microfiber, before it dries.",
                    "Steam also kills odor at the source, which is better than covering it with fragrance.",
                ]),
                ("Leather and hard surfaces", [
                    f"{P('P&amp;S Xpress Interior Cleaner')} sprayed onto your towel, never directly onto a screen or gauge cluster.",
                    "Dash, console, door cards, handles, steering wheel, shifter, all plastics.",
                    "Leather seats: light mist, gentle brush, wipe dry. Don't soak perforated leather, product gets in the holes.",
                ]),
                ("Glass, inside", [
                    f"{P(A_GLASS)} with two towels: one to clean, one dry to buff.",
                    "Do the inside of the windshield last and lower the windows an inch to get the top edge.",
                ]),
                ("Mats back in, final look", [
                    "Mats must be fully dry before they go back in or they'll smell.",
                    "Sit in the driver's seat and look around. That's the customer's view and it's where you'll spot what you missed.",
                ]),
            ]),
            ("warn", "Never spray any cleaner directly onto a touchscreen, gauge cluster, or headliner. Spray the towel instead. Headliners sag permanently if you soak the adhesive."),
            ("tip", "Sell the pet hair add-on before you start, not after. Once you're an hour into fighting hair for free, you've lost the money."),
        ],
        "done": ["Carpets are uniformly clean, not just the visible middle part.",
                 "No dust on the dash, in the vents, or around the shifter.",
                 "Glass is clear from the driver's seat with no haze.",
                 "It smells clean, not perfumed.",
                 "All the customer's belongings are back or handed over."],
    },
    {
        "name": "Premium Detail",
        "meta": "<b>$260 / $290 / $365</b> by size &middot; about <b>3 to 4 hours</b> &middot; most popular package",
        "what": "Everything in the Standard Detail, plus a clay bar treatment and a hand-applied wax. This is the package for a car that looks clean but feels rough to the touch.",
        "blocks": [
            ("p", "Do the full Standard Detail first. The clay and wax happen after the wash and before you go inside, because the car needs to be wet and clean for claying."),
            ("steps", [
                ("Iron remover, after the wash", [
                    f"With the car washed and still wet, spray {P('Koch Chemie Reactive Rim Cleaner', buy=True)} over the paint and wheels.",
                    "It will bleed purple where it's dissolving iron. That's it working, not blood.",
                    "Let it dwell 3 to 5 minutes, never let it dry, then rinse thoroughly.",
                ]),
                ("Clay the paint", [
                    f"Keep the panel soaked with {P(A_CLAY, buy=True)} lube. Clay must never touch dry paint.",
                    "Work a 2ft by 2ft area at a time in straight overlapping lines, light pressure.",
                    "You'll feel it grab at first and then go silent. Silent means that section is done.",
                    "Fold the clay to a clean face often. If you drop it on the ground, throw it away, no exceptions.",
                    "Wipe the panel with a clean towel and move on.",
                ]),
                ("Feel-test the paint", [
                    "Put your hand in a thin plastic bag and run it over the paint.",
                    "It should feel like glass. Any roughness means that section needs more clay.",
                ]),
                ("Wax", [
                    f"{P('P&amp;S Bead Maker')} is the fastest route: mist onto a damp or dry panel, spread with one towel, buff with a second.",
                    "Work one panel at a time. Thin coats. More product does not mean more protection.",
                    "Keep it off textured black trim, it can leave white residue.",
                ]),
                ("Then do the interior", [
                    "Now run the full interior portion of the Standard Detail.",
                ]),
            ]),
            ("warn", "Clay only removes what's stuck on the surface. It does not remove swirls or scratches. If the customer wants swirls gone, that's Machine Polish or the Signature Detail, quote it separately."),
        ],
        "done": ["Paint feels glass-smooth through a plastic bag on every panel.",
                 "Water beads tight and rolls off.",
                 "No wax residue in panel gaps, badges, or trim.",
                 "Everything in the Standard Detail checklist also passes."],
    },
    {
        "name": "Signature Detail",
        "meta": "<b>$530 / $595 / $690</b> by size &middot; about <b>6 to 8 hours, often two days</b> &middot; the top package",
        "what": "Everything in the Standard Detail, plus clay bar, a full machine polish, and ceramic coating. This is the one that actually removes swirl marks and then locks the finish in for about a year.",
        "blocks": [
            ("p", "Order matters here and it cannot be shuffled: wash, iron remove, clay, polish, panel prep, coat. Every step exists to make the next one work."),
            ("steps", [
                ("Wash, iron remove, clay", [
                    "Same as the Premium Detail, steps 1 through 3. The paint has to be perfectly clean before a machine touches it.",
                ]),
                ("Tape off the edges", [
                    "Painter's tape over plastic trim, badges, rubber seals, and panel edges.",
                    "A polisher burns through paint on a sharp edge in seconds. Tape is cheap.",
                ]),
                ("Test spot first", [
                    f"Pick one bad panel. {P('Koch Chemie Heavy Cut H9.01')} on a cutting pad with the dual-action polisher.",
                    "4 or 5 pea-sized drops, spread at speed 1, then work at speed 4 to 5 with slow overlapping passes.",
                    "Wipe it off and inspect under a bright light. If the swirls are gone, that's your process for the whole car.",
                ]),
                ("Cut the whole car", [
                    "Work 2ft by 2ft sections, slow and overlapping, letting the machine do the work rather than leaning on it.",
                    "Wipe each section clean before moving on so you can see what you actually did.",
                    "Clean the pad often with a brush. A clogged pad stops cutting and starts smearing.",
                ]),
                ("Refine the gloss", [
                    f"Switch to a polishing pad and {P('Koch Chemie Micro Cut M3.01')}.",
                    "Same technique, lighter pressure. This removes the fine haze the compound leaves.",
                ]),
                ("Panel prep, do not skip this", [
                    f"Wipe every panel with {P('Koch Chemie Panel Star')} on a clean towel.",
                    "This strips the polishing oils. Coating applied over oils will not bond and will fail in weeks.",
                ]),
                ("Apply the ceramic coating", [
                    f"{P(A_CER, buy=True)}. Indoors or in shade only, and follow the bottle for temperature.",
                    "A few drops on the applicator. Work one panel at a time in a cross-hatch pattern.",
                    "Watch for it to flash, usually 1 to 3 minutes depending on temperature. It goes slightly rainbow.",
                    "Buff off with a fresh microfiber, then a second fresh towel to make sure nothing is left behind.",
                    "Leftover coating that cures on the paint leaves high spots you have to polish out. Check every panel in good light before moving on.",
                ]),
                ("Interior, then hand it over", [
                    "Run the full interior portion of the Standard Detail while the coating cures.",
                    "Tell the customer plainly: keep it dry 24 hours, no wash for a week.",
                ]),
            ]),
            ("warn", "Never machine polish a panel you haven't clayed. Trapped grit under the pad will drag across the paint and put in deeper scratches than the ones you're removing."),
            ("warn", "Watch the paint temperature with your hand. If a panel is too hot to rest your palm on, stop and let it cool."),
            ("tip", "Charge for what the car needs. Heavily swirled single-stage or soft black paint takes far longer than a two-year-old white SUV. If it's going to run long, say so before you start."),
        ],
        "done": ["Swirls are gone under a bright light held at an angle, not just in the shade.",
                 "No haze, holograms, or buffer trails.",
                 "No coating high spots, streaks, or rainbow patches anywhere.",
                 "No compound dust left in panel gaps, badges, or trim.",
                 "Customer has been told the 24 hour and 1 week rules."],
    },
    {
        "name": "Add-Ons",
        "meta": "Sold on their own or bolted onto any package",
        "what": "",
        "blocks": [
            ("h", "Clay Bar Treatment &mdash; $50 / $60 / $75"),
            ("p", "Steps 1 through 3 of the Premium Detail. Roughly 45 to 75 minutes depending on how contaminated the paint is. Always sell it with the iron remover, they work together."),
            ("h", "Wax &mdash; $40 / $45 / $55"),
            ("p", f"{P('P&amp;S Bead Maker')} over clean, dry paint. About 30 minutes. Thin, even, one panel at a time. Worth mentioning to the customer that wax on dirty paint just seals the dirt in, which is why we clay first on the Premium."),
            ("h", "Machine Polish &mdash; $150 / $195 / $240"),
            ("p", "Steps 2 through 5 of the Signature Detail, without the ceramic coating. Budget 1.5 to 3 hours. This is real labor and the price reflects it, don't discount it casually."),
            ("h", "Ceramic Coating &mdash; $225"),
            ("p", "Steps 6 and 7 of the Signature Detail. It must go over paint that has been washed, clayed, and panel-prepped. Applying it over neglected paint locks the defects in for a year, so if the paint is rough, tell the customer it needs the polish first."),
            ("h", "Heavy Pet Hair Removal &mdash; $35 / $45 / $55"),
            ("p", "Rubber pet hair brush or a pumice stone dragged in one direction to ball the hair up, then vacuum. Work small sections. Rubber gloves dragged across upholstery also work well. Budget 30 to 60 minutes and quote it before you start, heavy dog cars can take far longer."),
            ("h", "Engine Bay Cleaning &mdash; $40 / $50 / $65"),
            ("steps", [
                ("Cold engine only", ["A cold engine, and cover the alternator, any exposed intake, and the fuse box with plastic bags."]),
                ("Degrease", [f"{P('Koch Chemie Green Star')} diluted about 1:10, sprayed on and agitated with a soft brush."]),
                ("Rinse gently", ["Low pressure only. Never blast a pressure washer into an engine bay, water gets into connectors and causes electrical faults you will get blamed for."]),
                ("Dry and dress", ["Towel dry what you can reach, then let it run for a few minutes to evaporate the rest. A light dressing on plastic covers finishes it."]),
            ]),
            ("warn", "If the customer's car is newer, has exposed electronics, or you have any doubt at all, do a wipe-down by hand instead of a wet clean. A no is cheaper than an electrical repair."),
        ],
        "done": [],
    },
]
auto_buy = [
    ("Adam's Visco Clay Bar Kit", "You sell Clay Bar Treatment at $50-75 and can't currently do it", "$25-35"),
    ("Koch Chemie Reactive Rim Cleaner", "Iron removal before clay and before coating", "$25-35"),
    ("P&amp;S Carpet Bomber", "Every full detail includes shampooing carpets and seats", "$20-30"),
    ("Adam's Graphene Ceramic Coating", "You sell Ceramic Coating at $225 and have nothing to apply", "$70-110"),
    ("Cutting and polishing pads", "Consumable, they wear out. Buy several of each", "$40-60"),
    ("Carpet extractor (upgrade)", "Not required, but it turns interiors from slow to fast and pays for itself", "$150-400"),
]

build("auto-detailing-guide.html", "How-To Guide", "Auto Detailing",
      "Every auto service we sell, step by step, with the exact product for each one. "
      "Follow it in order. The order is the reason the results are good.",
      auto_kit, auto_rules, auto_services, auto_buy,
      "Four of these block services that are already listed for sale on our website. Buy those first.")


# ==========================================================================
#  BOAT
# ==========================================================================
boat_kit = [
    ("Mainstream Marine Boat Cleaner", "Boat wash soap", "The general wash on hull, deck, and topsides."),
    ("Star brite Instant Hull Cleaner", "Acid-based stain remover", "The brown waterline stain. Wipes off without scrubbing."),
    ("3M Marine Restorer and Wax", "Compound and wax in one", "Light to moderate gelcoat oxidation."),
    ("3M Super Duty Rubbing Compound", "Heavy compound", "Chalky, badly oxidized gelcoat that the Restorer won't fix."),
    ("3M Marine Finesse-it", "Finishing polish", "Removes compound haze and brings up the shine."),
    ("Collinite 845 Insulator Wax", "Marine paste wax", "The wax step. Long-lasting and proven on boats."),
    ("Marine Maxx Ceramic Coating", "Ceramic coating", "The Full Ceramic Package."),
    ("IMAR Strataglass Cleaner", "Clear vinyl cleaner", "Isinglass and clear enclosure panels only."),
    ("Koch Chemie Green Star", "All-purpose cleaner", "Non-skid decks and general grime."),
    ("Dual-action polisher", "You already own this", "Compounding and polishing. Slower than a rotary on bad oxidation."),
]
boat_rules = [
    "<b>Always ask permission before you get on or in a boat.</b> Confirm with the owner or the marina where you can run water and power.",
    "<b>Soft-soled, non-marking shoes only.</b> Black soles leave marks on a white deck that you'll then have to remove for free.",
    "<b>Never wax or coat a non-skid deck.</b> Non-skid exists to stop people slipping. Waxing it makes it slick and someone gets hurt. Clean it, protect it with a dedicated non-skid product if asked, but never wax it.",
    "<b>Keep compound and polish off canvas, isinglass, and upholstery.</b> It stains and it's very hard to get out. Mask what's near your work area.",
    "<b>Acid hull cleaner means gloves and eye protection, every time.</b> Rinse anything it touches that isn't the hull, especially metal fittings.",
    "<b>Work in the shade or early in the day.</b> Gelcoat gets hot fast and product will dry on it.",
    "<b>Don't pressure wash decals, graphics, or old canvas stitching up close.</b> You'll peel or tear them.",
    "<b>Photograph existing gelcoat cracks, chips, and damage before you start.</b> Boats collect damage and you don't want it attributed to you.",
]
boat_services = [
    {
        "name": "Wash",
        "meta": "<b>$200 to $300</b> ballpark, custom quote &middot; typical 20 to 30ft boat &middot; about <b>2 to 3 hours</b>",
        "what": "A thorough wash of the hull, topsides, and deck. Salt, grime, and bird mess off. No compounding, no wax.",
        "blocks": [
            ("steps", [
                ("Rinse everything down first", [
                    "Fresh water over the whole boat to knock off salt and loose dirt.",
                    "Salt left on the surface turns into scratches the moment you start scrubbing.",
                ]),
                ("Wash top down", [
                    f"{P('Mainstream Marine Boat Cleaner')} in a bucket, soft brush on a pole for the big flat areas.",
                    "Hardtop and superstructure first, then topsides, then the hull, then the deck last.",
                    "Rinse each section before the soap dries.",
                ]),
                ("Non-skid decks", [
                    f"{P('Koch Chemie Green Star')} diluted, worked in with a stiff deck brush.",
                    "Scrub with the grain of the pattern. Rinse thoroughly, soap left in non-skid gets slippery.",
                ]),
                ("Waterline stains", [
                    f"{P('Star brite Instant Hull Cleaner')} on the brown band at the waterline.",
                    "Gloves and eye protection on. Wipe or spray on, it mostly dissolves the stain without scrubbing.",
                    "Rinse it off completely and don't let it dry on the gelcoat.",
                ]),
                ("Clear vinyl and glass", [
                    f"{P('IMAR Strataglass Cleaner')} on isinglass, nothing else.",
                    "Never use ammonia glass cleaner or anything abrasive on clear vinyl, it goes cloudy permanently and those panels are expensive.",
                ]),
                ("Dry", [
                    "Chamois or big microfiber on the gelcoat and any bright metal.",
                    "Water spots on a dark hull show badly, so dry as you go rather than at the end.",
                ]),
            ]),
            ("warn", "Do not use acid hull cleaner on anodized aluminum, painted surfaces, or polished stainless. It will etch and discolor them."),
        ],
        "done": ["No salt film left, run a finger over the gelcoat and check.",
                 "Waterline is clean or clearly improved, and you've told the owner if a stain won't come out.",
                 "Non-skid is fully rinsed and not slippery.",
                 "Isinglass is clear with no new scratches."],
    },
    {
        "name": "Wash &amp; Polish",
        "meta": "<b>$450 to $600</b> ballpark, custom quote &middot; about <b>5 to 8 hours</b>",
        "what": "Everything in the Wash, plus oxidation removal and a gelcoat polish. This is the service for a boat that's gone chalky and dull.",
        "blocks": [
            ("steps", [
                ("Full wash first", ["Run every step of the Wash. Compounding a dirty hull grinds dirt into the gelcoat."]),
                ("Test how bad the oxidation is", [
                    "Rub a small area with your thumb. If white chalk comes off on your skin, it's oxidized.",
                    f"Try {P('3M Marine Restorer and Wax')} on a 2ft square first with a wool or cutting pad on the dual-action polisher.",
                    f"If that won't cut it, step up to {P('3M Super Duty Rubbing Compound')}.",
                ]),
                ("Compound in sections", [
                    "Work 2ft by 2ft. Keep the pad flat and let the machine do the work.",
                    "Keep the pad and the surface slightly damp, never let compound dry on the gelcoat.",
                    "Wipe each section down and check it before moving on.",
                    "Clean the pad often. Gelcoat loads pads up much faster than car paint does.",
                ]),
                ("Refine", [
                    f"{P('3M Marine Finesse-it')} on a polishing pad over everything you compounded.",
                    "This removes the haze the compound leaves and is what actually makes it shine.",
                ]),
                ("Wipe down and inspect", [
                    "Clean towel over every polished section, then look at it from several angles.",
                    "Gelcoat hides swirls until the light hits right, so move around the boat while you check.",
                ]),
            ]),
            ("warn", "Gelcoat is a finite thickness and heavily oxidized boats have already lost some. Don't keep cutting the same spot hoping it improves. If it won't come back after two passes, tell the owner it's at its limit rather than cutting through to the laminate."),
            ("tip", "Without a rotary buffer this takes noticeably longer on heavy oxidation. A rotary is the single biggest time-saver for boat work if the volume justifies it."),
        ],
        "done": ["No chalk transfers to your thumb anywhere on the hull.",
                 "Gloss is even, no dull patches or swirl trails.",
                 "No compound residue in rub rails, fittings, or lettering.",
                 "Owner has been told about any area that couldn't be fully restored."],
    },
    {
        "name": "Wash, Polish &amp; Wax",
        "meta": "<b>$650 to $850</b> ballpark, custom quote &middot; about <b>7 to 10 hours</b>",
        "what": "Everything in the Wash &amp; Polish, plus a protective marine wax. The polish makes it shine, the wax is what keeps it that way through the season.",
        "blocks": [
            ("steps", [
                ("Wash and polish first", ["Complete both services fully before any wax goes on."]),
                ("Wax the gelcoat", [
                    f"{P('Collinite 845 Insulator Wax')}, thin coat by hand or with a soft foam pad on the machine at low speed.",
                    "Thin is the whole trick. A thick coat is hard to remove and doesn't protect any better.",
                    "Let it haze, then buff off with a clean microfiber.",
                ]),
                ("Second coat on the sun-facing surfaces", [
                    "Hardtop, foredeck, and anything that bakes all day gets a second coat.",
                    "That's where the UV damage starts and where it'll fail first.",
                ]),
                ("Detail the metal", [
                    "Polish the stainless rails and fittings while you're at it. It's a small amount of extra time and it's the first thing an owner notices.",
                ]),
            ]),
            ("warn", "Non-skid decks do not get waxed. Ever. It's a slip and fall risk and it is not worth the liability."),
        ],
        "done": ["Water beads tightly across the whole hull.",
                 "No wax residue in seams, lettering, rub rails, or around fittings.",
                 "Non-skid areas are clean and completely wax free.",
                 "Stainless is polished with no wax haze left on it."],
    },
    {
        "name": "Full Ceramic Package",
        "meta": "<b>$1,800 to $2,400</b> ballpark, custom quote &middot; often <b>2 to 3 days</b>",
        "what": "Wash, full oxidation removal and polish, then a ceramic coating instead of wax. Far better UV and salt protection, and it lasts through seasons rather than months.",
        "blocks": [
            ("steps", [
                ("Wash and full polish", ["Every step of Wash &amp; Polish. The coating locks in whatever the surface looks like, so it has to be right first."]),
                ("Prep the surface", [
                    "Wipe every surface with an isopropyl alcohol solution or the prep wipe supplied with the coating.",
                    "This strips off the polishing oils. Skip it and the coating will not bond, and it will fail within weeks.",
                ]),
                ("Coat in small sections", [
                    f"{P('Marine Maxx Ceramic Coating')}, following the bottle for temperature and humidity.",
                    "A few drops on the applicator, cross-hatch pattern, 2ft by 2ft at a time.",
                    "Watch for the flash, then buff with a clean microfiber and check with a second one.",
                    "Any coating left to cure on the surface becomes a high spot you have to polish off.",
                ]),
                ("Let it cure", [
                    "Keep the boat dry and out of rain for the time the manufacturer specifies, usually at least 24 hours.",
                    "Ideally the boat stays out of the water until it's fully cured. Tell the owner this before you start, not after.",
                ]),
                ("Hand over care instructions", [
                    "Rinse with fresh water after each use. No harsh acid cleaners on the coating.",
                    "This is a premium service, so hand over a written note about how to keep it up.",
                ]),
            ]),
            ("warn", "Never coat over oxidation, wax, or polish residue. The whole value of the service depends on the prep being right."),
        ],
        "done": ["Coating is even everywhere, no high spots, streaks, or rainbow patches.",
                 "Water sheets and beads hard across the whole hull.",
                 "Non-skid handled per the coating maker's instructions, and still not slippery.",
                 "Owner has written care instructions and knows the cure time."],
    },
]
boat_buy = [
    ("Star brite Instant Hull Cleaner", "Waterline stains are on nearly every boat", "$20-30"),
    ("3M Super Duty Rubbing Compound", "For the badly oxidized boats the Restorer won't fix", "$35-50"),
    ("3M Marine Finesse-it", "Without it, compounded gelcoat stays hazy", "$30-45"),
    ("IMAR Strataglass Cleaner", "The only safe thing for isinglass. Ruining a panel is expensive", "$20-25"),
    ("Wool and foam pads, marine grade", "Gelcoat eats pads much faster than car paint", "$50-80"),
    ("Rotary buffer (upgrade)", "Cuts heavy oxidation in a fraction of the time a DA takes", "$150-300"),
]

build("boat-detailing-guide.html", "How-To Guide", "Boat Detailing",
      "Every boat service we sell, step by step, with the exact product for each one. "
      "Gelcoat is not car paint, so read the rules page before your first job.",
      boat_kit, boat_rules, boat_services, boat_buy,
      "Boat work is quoted per job, so buy as the jobs come in rather than all at once.")


# ==========================================================================
#  PLANE
# ==========================================================================
plane_kit = [
    ("Aero Cosmetics Wash Wax ALL", "Aircraft-approved wash and wax", "The main wash. Works wet or waterless and leaves protection behind."),
    ("Aero Cosmetics Degreaser", "Aircraft-safe degreaser", "Belly, exhaust streaks, and oil residue."),
    ("Plexus Plexiglass Cleaner", "Acrylic-safe cleaner", "Windows and canopies only. Nothing else touches acrylic."),
    ("Nuvite or Met-All Polish", "Aluminum polish", "Bare polished aluminum only. Not for painted surfaces."),
    ("Marine Maxx Ceramic Coating", "Ceramic coating", "The Full Ceramic Package."),
    ("Painter's tape and plastic sheeting", "Masking", "Pitot tubes, static ports, and sensors. Non-negotiable."),
    ("Soft microfiber towels, lots of them", "Drying and buffing", "Aircraft finishes mark easily. Always fresh towels."),
    ("Step ladder or rolling platform", "Access", "Tails and fuselage tops. Never climb on the aircraft itself."),
    ("Respirator and safety glasses", "Safety gear", "Aluminum polishing throws fine black dust you should not breathe."),
]
plane_rules = [
    "<b>You are working on someone's aircraft. Get explicit permission and ask about restrictions before you touch anything.</b> If the owner has a mechanic, it's worth a quick word with them too.",
    "<b>Mask the pitot tube, static ports, and any external sensors before water goes anywhere near the aircraft.</b> Water in these causes false instrument readings. This is a flight safety issue, not a cosmetic one.",
    "<b>Never use household glass cleaner on aircraft windows.</b> Ammonia crazes acrylic, which means a spiderweb of permanent cracks and a window that has to be replaced. Plexus only.",
    "<b>Never spray water into engine inlets, exhaust, wheel wells, brakes, or control surface hinges.</b> Water sits in bearings and causes corrosion.",
    "<b>Static wicks are fragile and expensive.</b> Those little rods on the trailing edges. Don't grab them, lean on them, or drag a towel across them.",
    "<b>Only stand where you're told you can stand.</b> Wings have designated walkways. Standing anywhere else can dent the skin.",
    "<b>Never polish painted surfaces with aluminum polish.</b> Nuvite and Met-All are for bare polished aluminum only, they'll destroy paint.",
    "<b>Don't let anything, tools, rags, caps, get left behind in or on the aircraft.</b> Loose objects are a genuine flight hazard. Count what you brought and count it back out.",
]
plane_services = [
    {
        "name": "Wash",
        "meta": "<b>$250 to $300</b> ballpark, custom quote &middot; single-engine piston &middot; about <b>3 to 4 hours</b>",
        "what": "A full exterior wash: fuselage, wings, tail, and belly, plus windows. No polish, no compounding.",
        "blocks": [
            ("steps", [
                ("Talk to the owner and mask up", [
                    "Confirm what you can and can't touch, and where you're allowed to stand.",
                    "Mask the pitot tube, static ports, and any sensors with tape and plastic. Do this every single time.",
                    "Walk around and photograph any existing paint chips, crazing, or damage.",
                ]),
                ("Belly first", [
                    f"{P('Aero Cosmetics Degreaser')} on the belly and the exhaust streaks behind the cowling.",
                    "This is the dirtiest part, so it gets done first and separately, before your clean towels are anywhere near it.",
                    "Agitate gently with a soft brush and wipe off.",
                ]),
                ("Wash the aircraft top down", [
                    f"{P('Aero Cosmetics Wash Wax ALL')}, mixed per the bottle, using soft mitts and plenty of clean towels.",
                    "Top of the fuselage, then the wings, then down the sides, tail last.",
                    "Work in sections and wipe each one before it dries.",
                    "If water is restricted at the hangar, this product works waterless, spray on and wipe off with clean towels, changing towels often.",
                ]),
                ("Leading edges and bugs", [
                    "Bug residue on the leading edges takes a longer dwell, not more scrubbing.",
                    "Soak, wait, wipe. Scrubbing hard on a leading edge will scratch the paint.",
                ]),
                ("Windows, carefully", [
                    f"{P('Plexus Plexiglass Cleaner')} only, sprayed onto a clean soft microfiber, then wiped in straight lines.",
                    "Never wipe a dry window, grit will scratch it. Rinse the surface first if there's any dust.",
                    "Never use a dirty or gritty towel on acrylic. When in doubt, get a fresh one.",
                ]),
                ("Dry, unmask, and check", [
                    "Dry with clean towels, paying attention to seams and around fasteners where water sits.",
                    "Remove every piece of masking. Double check the pitot and static ports are clear.",
                    "Walk the aircraft and count your tools and rags back out.",
                ]),
            ]),
            ("warn", "If you leave masking on a pitot tube or static port, the aircraft's airspeed and altitude readings will be wrong in flight. Removing all masking and confirming it is the most important thing you do on a plane."),
        ],
        "done": ["Belly and exhaust streaks are clean.",
                 "No streaks or water spots on the paint.",
                 "Windows are perfectly clear with no new scratches and no haze.",
                 "Every piece of masking is off and the ports are confirmed clear.",
                 "No tools, towels, or trash left anywhere on or in the aircraft."],
    },
    {
        "name": "Wash &amp; Polish",
        "meta": "<b>$500 to $600</b> ballpark, custom quote &middot; about <b>6 to 9 hours</b>",
        "what": "Everything in the Wash, plus oxidation removal and polishing. On bare aluminum aircraft this is the service that brings the shine back.",
        "blocks": [
            ("steps", [
                ("Full wash first", ["Every step of the Wash service, including masking."]),
                ("Work out what you're polishing", [
                    "Painted surface or bare polished aluminum? They are completely different jobs and different products.",
                    "If you are not certain, ask the owner. Getting this wrong is expensive.",
                ]),
                ("Bare aluminum", [
                    f"{P('Nuvite or Met-All Polish')} with the appropriate grade, starting with the least aggressive that works.",
                    "Respirator and safety glasses on. This throws fine black aluminum dust.",
                    "Small sections, keep the pad moving, and wipe off the black residue as you go.",
                    "Work along the airflow direction, not across it.",
                ]),
                ("Painted surfaces", [
                    "A light polish suitable for aircraft paint only. Aircraft paint is often thinner than automotive paint.",
                    "Stay off decals, registration numbers, and any placards, they will lift.",
                    "Never use aluminum polish here.",
                ]),
                ("Clean up the residue", [
                    "Polish residue collects in every seam, rivet line, and gap.",
                    "Go over the whole aircraft with clean towels and a soft detail brush. Residue left in seams looks careless and can corrode.",
                ]),
            ]),
            ("warn", "Aluminum polishing dust is fine, black, and gets everywhere. Wear a respirator, and keep it well away from open engine cowlings, brakes, and the cabin."),
            ("tip", "This is slow, physical work and the reason the price is what it is. Quote by the condition of the aircraft, not by its size alone."),
        ],
        "done": ["Even shine with no dull patches or swirl trails.",
                 "No polish residue in seams, rivet lines, or around fasteners.",
                 "No polish on decals, placards, or registration numbers.",
                 "All masking removed and ports confirmed clear."],
    },
    {
        "name": "Wash, Polish &amp; Wax",
        "meta": "<b>$750 to $900</b> ballpark, custom quote &middot; about <b>8 to 11 hours</b>",
        "what": "Everything in the Wash &amp; Polish, plus a protective wax layer to hold the finish and make the next wash easier.",
        "blocks": [
            ("steps", [
                ("Wash and polish first", ["Complete both fully."]),
                ("Apply protection", [
                    f"{P('Aero Cosmetics Wash Wax ALL')} leaves a wax layer as part of the wash, so a final pass over the whole aircraft builds that protection up evenly.",
                    "Thin and even, buffed off with clean towels.",
                    "Work in sections so nothing sits too long.",
                ]),
                ("Extra attention on the leading edges", [
                    "Leading edges, the top of the fuselage, and the tail take the most weather and sun.",
                    "A second pass here is worth it and the owner will notice it lasts longer.",
                ]),
                ("Final walk-around", [
                    "Check every seam and fastener for residue.",
                    "Confirm all masking is off and the ports are clear.",
                    "Count tools and rags back out.",
                ]),
            ]),
            ("warn", "Keep wax off the windows and off the walkway areas of the wing. A slippery wing walk is dangerous for whoever boards next."),
        ],
        "done": ["Even protection with no residue in seams or around rivets.",
                 "Windows clean and wax-free.",
                 "Wing walk areas are not slippery.",
                 "All masking removed, ports clear, nothing left behind."],
    },
    {
        "name": "Full Ceramic Package",
        "meta": "<b>$1,800 to $2,200</b> ballpark, custom quote &middot; often <b>2 to 3 days</b>",
        "what": "Wash, full polish, then a ceramic coating instead of wax. The longest-lasting protection offered, and it makes future washes far quicker.",
        "blocks": [
            ("steps", [
                ("Wash and full polish", ["Every step of Wash &amp; Polish. The coating locks in whatever is underneath."]),
                ("Confirm the coating suits the surface", [
                    "Check the coating is appropriate for the surface, painted or bare aluminum, and that the owner is happy with it going on.",
                    "If the aircraft is on a maintenance program, it's worth confirming with their mechanic.",
                ]),
                ("Prep the surface", [
                    "Wipe everything down with the prep wipe or isopropyl solution to strip polishing oils.",
                    "The coating will not bond over oils. This step decides whether the job lasts a year or a month.",
                ]),
                ("Coat in small sections", [
                    f"{P('Marine Maxx Ceramic Coating')} or an equivalent aviation-suitable coating, per the bottle.",
                    "Small sections, cross-hatch, watch for the flash, buff off with a fresh towel and check with a second.",
                    "Work in a hangar out of wind and direct sun. Dust landing on curing coating is a real problem.",
                ]),
                ("Cure and hand over", [
                    "Keep the aircraft in the hangar and dry for the full cure time on the label.",
                    "Give the owner written care instructions and tell them the cure time before the job starts.",
                ]),
                ("Final safety walk", [
                    "Every piece of masking off, pitot and static ports confirmed clear.",
                    "Every tool, towel, and applicator accounted for and out of the aircraft.",
                ]),
            ]),
            ("warn", "This is the highest-value job we offer and the one with the most ways to go wrong. If anything is unclear about the aircraft, stop and ask the owner rather than guessing."),
        ],
        "done": ["Even coating, no high spots, streaks, or rainbow patches.",
                 "Water beads and sheets off cleanly.",
                 "No coating on windows, placards, or in seams.",
                 "All masking removed, both ports confirmed clear, and confirmed a second time.",
                 "Nothing left behind on or in the aircraft.",
                 "Owner has written care instructions and knows the cure time."],
    },
]
plane_buy = [
    ("Aero Cosmetics Wash Wax ALL", "The core product. You already buy this brand", "$40-70"),
    ("Aero Cosmetics Degreaser", "Bellies and exhaust streaks need it on every job", "$25-40"),
    ("Plexus Plexiglass Cleaner", "The only safe window product. A crazed window is a very expensive mistake", "$15-20"),
    ("Nuvite or Met-All Polish", "Only if you take on bare polished aluminum aircraft", "$40-80"),
    ("Painter's tape and plastic sheeting", "Masking ports and sensors. Never run out of this", "$15-25"),
    ("Respirator and safety glasses", "Required for aluminum polishing dust", "$30-60"),
    ("Step ladder or rolling platform", "For tails and fuselage tops. Never stand on the aircraft", "$80-250"),
]

build("plane-detailing-guide.html", "How-To Guide", "Plane Detailing",
      "Every aircraft service we sell, step by step, with the exact product for each one. "
      "The rules page is not optional reading. On aircraft, some mistakes are safety issues.",
      plane_kit, plane_rules, plane_services, plane_buy,
      "Aircraft work is quoted per job. The masking supplies and Plexus are the two things you should never be without.")

print("all guides written")
