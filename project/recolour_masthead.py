"""Recolour the KnowHow masthead background to a new brand colour.

The source masthead (`knowhow-masthead.png`, coral) is a flat background colour with a
cream brush-script wordmark, a cream tagline, a brushed bottom edge fading to white,
and the KC logo ellipse. This swaps ONLY the background colour, keeping the wordmark,
the brush edge and the logo intact.

Anti-aliased pixels sit on a straight line between the background colour and whatever
they border (cream / white / the logo's pale green). Each pixel is projected onto those
lines to recover its mix fraction, then re-mixed against the new background colour.
Pixels that do not lie on any of those lines (the KC logo internals) are left alone.

Usage:  python recolour_masthead.py
Needs:  pip install pillow
"""
from PIL import Image
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

SRC = os.path.join(ROOT, "knowhow-masthead.png")          # coral source
OUT = os.path.join(ROOT, "knowhow-masthead-blue.png")     # blue result

SOURCE_BG = (209, 113, 87)    # #D17157 coral, sampled from SRC
TARGET_BG = (110, 151, 184)   # #6E97B8 Kelvin Cave brand blue

# Colours the background is anti-aliased against, in the source image.
NEIGHBOURS = [
    (253, 243, 197),  # #FDF3C5 cream wordmark + tagline
    (255, 255, 255),  # #FFFFFF white below the brushed bottom edge
    (222, 238, 210),  # #DEEED2 pale green of the KC logo ellipse
]

TOL = 26  # max distance off a mix line before a pixel is treated as "not background"


def mix(a, b, t):
    """t=1 -> a, t=0 -> b."""
    return tuple(round(a[i] * t + b[i] * (1 - t)) for i in range(3))


def recolour(src=SRC, out=OUT, target=TARGET_BG):
    im = Image.open(src).convert("RGB")
    px = list(im.getdata())
    new = []

    # Precompute the background->neighbour vectors.
    lines = []
    for nb in NEIGHBOURS:
        v = [SOURCE_BG[i] - nb[i] for i in range(3)]
        lines.append((nb, v, sum(c * c for c in v)))

    for p in px:
        best = None  # (residual, mix_fraction, neighbour)
        for nb, v, vv in lines:
            d = [p[i] - nb[i] for i in range(3)]
            t = sum(d[i] * v[i] for i in range(3)) / vv
            t = 0.0 if t < 0 else 1.0 if t > 1 else t
            res = sum((d[i] - t * v[i]) ** 2 for i in range(3)) ** 0.5
            if best is None or res < best[0]:
                best = (res, t, nb)

        res, t, nb = best
        new.append(mix(target, nb, t) if res <= TOL else p)

    im.putdata(new)
    im.save(out, optimize=True)
    print(f"wrote {out}  ({os.path.getsize(out)} bytes)")


if __name__ == "__main__":
    recolour()
