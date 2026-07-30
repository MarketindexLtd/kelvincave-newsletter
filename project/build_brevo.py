"""Turn the selected preview into a paste-into-Brevo campaign file.

The preview (`v2-imageled.html`) is built to be browsed on GitHub Pages, so it references the
masthead by relative path and leaves the unsubscribe link as a placeholder. Neither works inside
Brevo. This produces `knowhow-summer-2026-brevo.html`, which is the file to paste into
Brevo's "paste your own HTML" campaign editor.

What it changes, and nothing else:
  1. Relative masthead src -> absolute GitHub Pages URL, so Brevo can fetch it.
  2. Placeholder unsubscribe href -> Brevo's {{ unsubscribe }} merge tag.
  3. Prepends a hidden preheader (the grey preview line email clients show next to the subject).

Run this again after any edit to v2-imageled.html, so the two never drift.

Usage:  python build_brevo.py
Needs:  nothing beyond the standard library.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

SRC = os.path.join(ROOT, "v2-imageled.html")
OUT = os.path.join(ROOT, "knowhow-summer-2026-brevo.html")

PAGES_BASE = "https://marketindexltd.github.io/kelvincave-newsletter/"

# Shown in the inbox after the subject line. Keep it under ~100 chars and do not repeat the
# subject, which is:
#   "Your Summer 2026 KnowHow: cutting feed costs, harvest prep and home-grown feed"
PREHEADER = ("A 37% pre-lambing feed cost saving, preserving grain without drying, "
             "and getting your store harvest-ready.")

PREHEADER_HTML = (
    '<div style="display:none;font-size:1px;color:#ffffff;line-height:1px;max-height:0;'
    'max-width:0;opacity:0;overflow:hidden;mso-hide:all;">{text}'
    # Padding entities stop the client pulling body copy into the preview line after the preheader.
    + "&#847;&zwnj;&nbsp;" * 60
    + "</div>"
)


def build(src=SRC, out=OUT):
    html = open(src, encoding="utf-8").read()
    changes = []

    # 1. Relative image srcs -> absolute. Only touches src values with no scheme.
    html, n = re.subn(r'src="(?!https?://)([^"]+)"', lambda m: f'src="{PAGES_BASE}{m.group(1)}"', html)
    changes.append(f"{n} relative image src -> {PAGES_BASE}")

    # 2. Unsubscribe placeholder -> Brevo merge tag. Anchored on the link text so we cannot
    #    accidentally rewrite some other href="#".
    html, n = re.subn(r'<a href="#"((?:[^>]*)>Unsubscribe</a>)',
                      lambda m: f'<a href="{{{{ unsubscribe }}}}"{m.group(1)}', html)
    changes.append(f"{n} unsubscribe placeholder -> {{{{ unsubscribe }}}} tag")
    if n != 1:
        sys.exit(f"ERROR: expected exactly 1 unsubscribe placeholder, found {n}. Check {src}.")

    # 3. Hidden preheader immediately after <body ...>.
    html, n = re.subn(r'(<body[^>]*>)', lambda m: m.group(1) + PREHEADER_HTML.format(text=PREHEADER),
                      html, count=1)
    changes.append(f"{n} preheader inserted")

    # Nothing relative should survive, or images will silently break in the inbox.
    leftover = re.findall(r'(?:src|href)="(?!https?://|mailto:|\{\{)([^"#][^"]*)"', html)
    if leftover:
        sys.exit(f"ERROR: relative references still present: {sorted(set(leftover))}")

    open(out, "w", encoding="utf-8").write(html)
    for c in changes:
        print("  " + c)
    print(f"wrote {out}  ({os.path.getsize(out)} bytes)")


if __name__ == "__main__":
    build()
