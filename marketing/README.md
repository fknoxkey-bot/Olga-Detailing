# Marketing materials

Print-ready flyers and posters for Olga Detailing, meant for bulletin boards
and around-town posting. Not part of the live website.

| File | Notes |
|---|---|
| `poster-auto-detailing.png` | Auto detailing poster. Has both the Instagram QR and a Website QR (olgadetailing.com), side by side at the bottom. This is the one to print. |
| `poster-auto-detailing-original.png` | Knox's original poster (Instagram QR only), kept as a source/reference. |

To update the Website QR (e.g. if the domain ever changes), regenerate it with
the `qrcode` Python library using a circle module drawer plus hand-drawn
rounded finder eyes so it keeps visually matching the dot-style Instagram QR,
then re-composite onto the original poster. Ask Claude to redo this, it knows
the exact layout math (QR size, spacing, label font) used here.
