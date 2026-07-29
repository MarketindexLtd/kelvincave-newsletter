# -*- coding: utf-8 -*-
import os, glob
from PIL import Image

EMAIL_DIR = r"C:\Users\Admin\Downloads\KnowHow-Summer-2026-email"
WEB_DIR   = r"C:\Users\Admin\Downloads\KnowHow-Summer-2026-website"

# display order -> (website folder prefix, hero file suffix)
HEROES = [
 ("01 - Sheep",       "_01"),
 ("03 - Propcorn",    "_02"),
 ("02 - Tiny",        "_01"),
 ("05 - Investment",  "_07"),
 ("08 - A new feed",  "_02"),
 ("09 - Bespoke",     "_01"),
 ("10 - Stacking",    "_02"),
 ("11 - Moisture",    "_01"),
]

def find_hero(prefix, suffix):
    folders = glob.glob(os.path.join(WEB_DIR, prefix + "*"))
    if not folders: return None
    imgs = glob.glob(os.path.join(folders[0], "images", "*" + suffix + ".jpg"))
    # exclude table images
    imgs = [x for x in imgs if "_table_" not in os.path.basename(x)]
    return imgs[0] if imgs else None

def crop_32(src, out, W=600, H=400):
    im = Image.open(src).convert("RGB")
    w,h = im.size
    target = W/H
    ar = w/h
    if ar > target:            # too wide -> crop sides
        nw = int(h*target); x0=(w-nw)//2
        im = im.crop((x0,0,x0+nw,h))
    else:                      # too tall -> crop top/bottom
        nh = int(w/target); y0=(h-nh)//2
        im = im.crop((0,y0,w,y0+nh))
    im = im.resize((W,H), Image.LANCZOS)
    im.save(out, "JPEG", quality=88)

for i,(pre,suf) in enumerate(HEROES, 1):
    src = find_hero(pre, suf)
    if not src:
        print("MISSING", pre, suf); continue
    out = os.path.join(EMAIL_DIR, f"img-{i:02d}.jpg")
    crop_32(src, out)
    print(f"img-{i:02d}.jpg <- {os.path.basename(src)}")

# ---- build final ALTERNATING email with consistent local images ----
COL = {"CASE STUDY":"#8B9A3D","TECHNICAL ARTICLE":"#D9795E","NEWS":"#6E97B8","PRODUCTS":"#6E97B8"}
BUTTON="#8B9A3D"; TITLEBLUE="#2f5c7a"
ART = [
 ("CASE STUDY","Sheep TMR bolstered by home-grown beans",
  "How Myerscough College cut pre-lambing feed costs by 37% by moving its ewes onto a home-grown TMR of wholecrop beans and crimped wheat, with no soya.",
  "https://kelvincave.com/proteins/sheep-tmr-bolstered-by-home-grown-beans/"),
 ("TECHNICAL ARTICLE","Propcorn NC beats grain drying on cost and nutrition",
  "With fuel prices high, Dr George Fisher finds preserving grain with Propcorn NC comes out around 40% cheaper than drying, with nutritional benefits too.",
  "https://kelvincave.com/cereals/propcorn-nc-beats-grain-drying-on-cost-and-nutrition/"),
 ("TECHNICAL ARTICLE","Tiny threats, big losses: why grain store pest control matters",
  "James Phelps of Barrettine on the pests that can wreck stored grain, how to spot the worst offenders, and how to prepare your store before harvest.",
  "https://kelvincave.com/cereals/tiny-threats-big-losses-why-grain-store-pest-control-matters/"),
 ("CASE STUDY","Investment in calf housing for a dairy-Wagyu future",
  "Inside the Mann family's new Cumbrian calf unit, purpose-built for health and performance as they move their dairy herd to Wagyu crossing.",
  "https://kelvincave.com/forage/investment-in-calf-housing-for-a-dairy-wagyu-future/"),
 ("NEWS","A new feed on the block",
  "Kelvin Cave, Veolia and partners have found a way to preserve surplus supermarket food into a nutritionally dense new feed, soon available to UK farmers.",
  "https://kelvincave.com/news/a-new-feed-on-the-block/"),
 ("CASE STUDY","Bespoke KC frame allows quick switch from silage to grain",
  "A Warwickshire farm's bespoke front-mounted IBC carrier and Silaspray switches from treating silage to treating grain in minutes.",
  "https://kelvincave.com/machinery/bespoke-kc-frame-allows-quick-switch-from-silage-to-grain/"),
 ("TECHNICAL ARTICLE","Stacking haylage in your favour",
  "With wrap costs and plastic pressures rising, we compare wrapping bales against preserving high-moisture hay with BaleSafe, and how to store it unwrapped.",
  "https://kelvincave.com/forage/stacking-haylage-in-your-favour/"),
 ("PRODUCTS","Moisture meters for grain and hay",
  "Accurate moisture readings take the guesswork out of preservation. A look at the Wile 55 and Wile 25 meters, plus where to see us at the 2026 shows.",
  "https://kelvincave.com/forage/moisture-meters-for-grain-and-hay/"),
]
def esc(s): return s.replace("&","&amp;")
def btn(url):
    return (f'<table role="presentation" cellpadding="0" cellspacing="0"><tr><td bgcolor="{BUTTON}" style="border-radius:4px;">'
            f'<a href="{url}" style="display:inline-block;padding:8px 20px;font-family:Arial,Helvetica,sans-serif;font-size:13px;font-weight:bold;color:#fff;text-decoration:none;border-radius:4px;">Read more</a></td></tr></table>')

rows=""
for i,(label,title,teaser,url) in enumerate(ART):
    num=i+1; lc=COL[label]; img=f"img-{num:02d}.jpg"
    # even rows: image left / text right (gap on text's left); odd rows: text left / image right (gap on text's right)
    txtpad = "0 0 0 22px" if i%2==0 else "0 22px 0 0"
    imgcell=(f'<td class="col" width="270" valign="top" style="padding:0;">'
             f'<a href="{url}"><img src="{img}" width="270" alt="{esc(title)}" style="display:block;width:100%;max-width:270px;height:auto;border:0;" /></a></td>')
    txtcell=(f'<td class="col pad" width="306" valign="top" style="padding:{txtpad};font-family:Arial,Helvetica,sans-serif;">'
             f'<div style="font-size:11px;letter-spacing:2px;font-weight:bold;color:{lc};text-transform:uppercase;padding-bottom:6px;">{label}</div>'
             f'<div style="font-size:18px;line-height:23px;font-weight:bold;padding-bottom:8px;"><a href="{url}" style="color:{TITLEBLUE};text-decoration:none;"><span style="color:#6E97B8;">{num:02d}.</span> {esc(title)}</a></div>'
             f'<div style="font-size:14px;line-height:21px;color:#555;padding-bottom:12px;">{esc(teaser)}</div>{btn(url)}</td>')
    inner = imgcell+txtcell if i%2==0 else txtcell+imgcell
    rows += (f'<tr><td style="padding:38px 24px 0 24px;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr>{inner}</tr></table>'
             f'<div style="border-top:1px solid #e6e4dc;margin-top:38px;font-size:0;line-height:0;">&nbsp;</div></td></tr>')

HEAD = """<!DOCTYPE html><html xmlns="http://www.w3.org/1999/xhtml"><head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>KnowHow Summer 2026</title>
<style>@media only screen and (max-width:620px){.col{display:block !important;width:100% !important;}.pad{padding:16px 24px 0 24px !important;}}</style>
</head><body style="margin:0;padding:0;background-color:#eef1f4;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background-color:#eef1f4;"><tr><td align="center" style="padding:20px 10px;">
<table role="presentation" width="600" cellpadding="0" cellspacing="0" style="width:600px;max-width:600px;background-color:#ffffff;">
<tr><td><img src="knowhow-masthead.png" width="600" alt="KnowHow Summer 2026 - Kelvin Cave" style="display:block;width:100%;max-width:600px;height:auto;border:0;" /></td></tr>
<tr><td style="padding:22px 24px 6px 24px;font-family:Arial,Helvetica,sans-serif;font-size:16px;line-height:24px;color:#333;">
<p style="margin:0;">Welcome to the Summer 2026 edition of KnowHow. As harvest approaches, here are ways to get more from home-grown and locally sourced feeds, from a 37% pre-lambing feed cost saving to preserving grain without drying.</p>
<p style="margin:12px 0 0 0;font-size:14px;line-height:20px;color:#333;">Prefer the full magazine? <a href="#" style="color:#0C4E42;font-weight:bold;text-decoration:underline;">Read the complete issue as a PDF</a></p></td></tr>
"""
FOOT = """
<tr><td style="padding:28px 24px 0 24px;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background-color:#f3f1ea;border-left:4px solid #FDB724;">
<tr><td style="padding:16px 18px;font-family:Arial,Helvetica,sans-serif;font-size:14px;line-height:21px;color:#333;">
<strong style="color:#0C4E42;">Come and see us in 2026</strong><br />Royal Highland Show, 18 to 21 June, Ingliston, Edinburgh<br />Royal Welsh Show, 20 to 23 July, Llanelwedd, Builth Wells, Powys</td></tr></table></td></tr>
<tr><td align="center" style="background-color:#6E97B8;padding:26px 24px;font-family:Arial,Helvetica,sans-serif;font-size:14px;line-height:22px;color:#fff;">
<strong>Kelvin Cave Ltd</strong><br />Call us on 01458 252281<br />
<a href="mailto:info@kelvincave.com" style="color:#fff;text-decoration:underline;">info@kelvincave.com</a> &nbsp;|&nbsp; <a href="https://www.kelvincave.com" style="color:#fff;text-decoration:underline;">kelvincave.com</a></td></tr>
<tr><td align="center" style="background-color:#5c86a6;padding:14px 24px;font-family:Arial,Helvetica,sans-serif;font-size:12px;line-height:18px;color:#e8eef3;">
You are receiving this because you are a Kelvin Cave contact.<br /><a href="{{ unsubscribe }}" style="color:#e8eef3;text-decoration:underline;">Unsubscribe</a></td></tr>
</table></td></tr></table></body></html>"""

open(os.path.join(EMAIL_DIR,"knowhow-summer-2026-email.html"),"w",encoding="utf-8").write(HEAD+rows+FOOT)
print("built final alternating email")
