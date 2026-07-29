# -*- coding: utf-8 -*-
import os, shutil
EMAIL_DIR = r"C:\Users\Admin\Downloads\KnowHow-Summer-2026-email"

BASE = "https://kelvincave.com/wp-content/uploads/2026/07/"
COL = {"CASE STUDY":"#8B9A3D","TECHNICAL ARTICLE":"#D9795E","NEWS":"#6E97B8","PRODUCTS":"#6E97B8"}
GREEN="#0C4E42"; GOLD="#FDB724"; TITLEBLUE="#2f5c7a"; BUTTON="#8B9A3D"

# (label, remote-hero-filename, title, teaser, url)
ART = [
 ("CASE STUDY","01_sheep-tmr-bolstered-by-home-grown-beans_01.jpg","Sheep TMR bolstered by home-grown beans",
  "How Myerscough College cut pre-lambing feed costs by 37% by moving its ewes onto a home-grown TMR of wholecrop beans and crimped wheat, with no soya.",
  "https://kelvincave.com/proteins/sheep-tmr-bolstered-by-home-grown-beans/"),
 ("TECHNICAL ARTICLE","03_propcorn-nc-beats-grain-drying-on-cost-a_02.jpg","Propcorn NC beats grain drying on cost and nutrition",
  "With fuel prices high, Dr George Fisher finds preserving grain with Propcorn NC comes out around 40% cheaper than drying, with nutritional benefits too.",
  "https://kelvincave.com/cereals/propcorn-nc-beats-grain-drying-on-cost-and-nutrition/"),
 ("TECHNICAL ARTICLE","02_tiny-threats-big-losses-why-grain-store-_01.jpg","Tiny threats, big losses: why grain store pest control matters",
  "James Phelps of Barrettine on the pests that can wreck stored grain, how to spot the worst offenders, and how to prepare your store before harvest.",
  "https://kelvincave.com/cereals/tiny-threats-big-losses-why-grain-store-pest-control-matters/"),
 ("CASE STUDY","05_investment-in-calf-housing-for-a-dairy-w_07.jpg","Investment in calf housing for a dairy-Wagyu future",
  "Inside the Mann family's new Cumbrian calf unit, purpose-built for health and performance as they move their dairy herd to Wagyu crossing.",
  "https://kelvincave.com/forage/investment-in-calf-housing-for-a-dairy-wagyu-future/"),
 ("NEWS","08_a-new-feed-on-the-block_02.jpg","A new feed on the block",
  "Kelvin Cave, Veolia and partners have found a way to preserve surplus supermarket food into a nutritionally dense new feed, soon available to UK farmers.",
  "https://kelvincave.com/news/a-new-feed-on-the-block/"),
 ("CASE STUDY","09_bespoke-kc-frame-allows-quick-switch-fro_01.jpg","Bespoke KC frame allows quick switch from silage to grain",
  "A Warwickshire farm's bespoke front-mounted IBC carrier and Silaspray switches from treating silage to treating grain in minutes.",
  "https://kelvincave.com/machinery/bespoke-kc-frame-allows-quick-switch-from-silage-to-grain/"),
 ("TECHNICAL ARTICLE","10_stacking-haylage-in-your-favour_02.jpg","Stacking haylage in your favour",
  "With wrap costs and plastic pressures rising, we compare wrapping bales against preserving high-moisture hay with BaleSafe, and how to store it unwrapped.",
  "https://kelvincave.com/forage/stacking-haylage-in-your-favour/"),
 ("PRODUCTS","11_moisture-meters-for-grain-and-hay_01.jpg","Moisture meters for grain and hay",
  "Accurate moisture readings take the guesswork out of preservation. A look at the Wile 55 and Wile 25 meters, plus where to see us at the 2026 shows.",
  "https://kelvincave.com/forage/moisture-meters-for-grain-and-hay/"),
]
def esc(s): return s.replace("&","&amp;")

EVENTS = """<tr><td style="padding:28px 24px 0 24px;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background-color:#f3f1ea;border-left:4px solid #FDB724;">
<tr><td style="padding:16px 18px;font-family:Arial,Helvetica,sans-serif;font-size:14px;line-height:21px;color:#333;">
<strong style="color:#0C4E42;">Come and see us in 2026</strong><br />Royal Highland Show, 18 to 21 June, Ingliston, Edinburgh<br />Royal Welsh Show, 20 to 23 July, Llanelwedd, Builth Wells, Powys</td></tr></table></td></tr>"""
def footer(bg="#6E97B8", sub="#5c86a6"):
    return f"""<tr><td align="center" style="background-color:{bg};padding:26px 24px;font-family:Arial,Helvetica,sans-serif;font-size:14px;line-height:22px;color:#fff;">
<strong>Kelvin Cave Ltd</strong><br />Call us on 01458 252281<br />
<a href="mailto:info@kelvincave.com" style="color:#fff;text-decoration:underline;">info@kelvincave.com</a> &nbsp;|&nbsp; <a href="https://www.kelvincave.com" style="color:#fff;text-decoration:underline;">kelvincave.com</a></td></tr>
<tr><td align="center" style="background-color:{sub};padding:14px 24px;font-family:Arial,Helvetica,sans-serif;font-size:12px;line-height:18px;color:#e8eef3;">
You are receiving this because you are a Kelvin Cave contact.<br /><a href="#" style="color:#e8eef3;text-decoration:underline;">Unsubscribe</a></td></tr>"""

def wrap(inner, bg="#eef1f4"):
    return f"""<!DOCTYPE html><html xmlns="http://www.w3.org/1999/xhtml"><head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" /><meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>KnowHow Summer 2026</title><style>@media only screen and (max-width:620px){{.col{{display:block !important;width:100% !important;}}.pad{{padding:16px 24px 0 24px !important;}}}}</style>
</head><body style="margin:0;padding:0;background-color:{bg};">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background-color:{bg};"><tr><td align="center" style="padding:20px 10px;">
<table role="presentation" width="600" cellpadding="0" cellspacing="0" style="width:600px;max-width:600px;background-color:#ffffff;">
{inner}
</table></td></tr></table></body></html>"""

INTRO = """<tr><td style="padding:22px 24px 6px 24px;font-family:Arial,Helvetica,sans-serif;font-size:16px;line-height:24px;color:#333;">
<p style="margin:0;">Welcome to the Summer 2026 edition of KnowHow. As harvest approaches, here are ways to get more from home-grown and locally sourced feeds, from a 37% pre-lambing feed cost saving to preserving grain without drying.</p>
<p style="margin:12px 0 0 0;font-size:14px;line-height:20px;color:#333;">Prefer the full magazine? <a href="#" style="color:#0C4E42;font-weight:bold;text-decoration:underline;">Read the complete issue as a PDF</a></p></td></tr>"""

# ---------- V1: ORIGINAL GREEN (text-led) ----------
def v1_green():
    head = f"""<tr><td><img src="knowhow-masthead-green.png" width="600" alt="KnowHow - Kelvin Cave" style="display:block;width:100%;max-width:600px;height:auto;border:0;" /></td></tr>
<tr><td align="center" style="background-color:{GOLD};padding:9px 20px;font-family:Arial,Helvetica,sans-serif;font-size:12px;letter-spacing:4px;color:{GREEN};text-transform:uppercase;font-weight:bold;">Summer 2026</td></tr>"""
    toc=""
    for i,(label,img,title,teaser,url) in enumerate(ART,1):
        toc+=f'<tr><td style="padding:4px 0;font-family:Arial,Helvetica,sans-serif;font-size:14px;line-height:20px;color:{GREEN};"><span style="color:{GOLD};font-weight:bold;">{i:02d}</span>&nbsp;&nbsp;<a href="{url}" style="color:{GREEN};text-decoration:none;">{esc(title)}</a></td></tr>'
    contents=f"""<tr><td style="padding:20px 30px 0 30px;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background-color:#e9f0eb;border-radius:6px;border-left:5px solid {GOLD};">
<tr><td style="padding:16px 20px 8px 20px;font-family:Arial,Helvetica,sans-serif;font-size:16px;font-weight:bold;color:{GREEN};letter-spacing:1px;">In this issue</td></tr>
<tr><td style="padding:0 20px 14px 20px;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0">{toc}</table></td></tr></table></td></tr>"""
    body=INTRO+contents
    for i,(label,img,title,teaser,url) in enumerate(ART,1):
        lc=COL[label]
        body+=f"""<tr><td style="padding:26px 30px 0 30px;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="border:1px solid #e2e5dc;border-radius:8px;overflow:hidden;">
<tr><td><a href="{url}"><img src="img-{i:02d}.jpg" width="540" alt="{esc(title)}" style="display:block;width:100%;max-width:540px;height:auto;border:0;" /></a></td></tr>
<tr><td style="padding:16px 22px 20px 22px;font-family:Arial,Helvetica,sans-serif;">
<div style="padding-bottom:9px;"><span style="background-color:{lc};color:#fff;font-size:11px;font-weight:bold;letter-spacing:1.5px;text-transform:uppercase;padding:4px 11px;border-radius:3px;">{label}</span></div>
<a href="{url}" style="font-size:20px;line-height:26px;font-weight:bold;color:{GREEN};text-decoration:none;"><span style="color:{GOLD};">{i:02d}.</span> {esc(title)}</a>
<p style="margin:9px 0 14px 0;font-size:15px;line-height:23px;color:#444;">{esc(teaser)}</p>
<table role="presentation" cellpadding="0" cellspacing="0"><tr><td bgcolor="{GREEN}" style="border-radius:4px;"><a href="{url}" style="display:inline-block;padding:9px 22px;font-family:Arial,Helvetica,sans-serif;font-size:14px;font-weight:bold;color:#fff;text-decoration:none;border-radius:4px;">Read more</a></td></tr></table>
</td></tr></table></td></tr>"""
    return wrap(head+body+EVENTS+footer(GREEN,"#0a3f36"), bg="#eef1ec")

# ---------- V2: IMAGE-LED FULL-WIDTH ----------
def v2_imageled():
    head='<tr><td><img src="knowhow-masthead.png" width="600" alt="KnowHow Summer 2026 - Kelvin Cave" style="display:block;width:100%;max-width:600px;height:auto;border:0;" /></td></tr>'
    toc=""
    for i,(label,img,title,teaser,url) in enumerate(ART,1):
        toc+=f'<tr><td style="padding:3px 0;font-family:Arial,Helvetica,sans-serif;font-size:14px;line-height:20px;"><span style="color:#6E97B8;font-weight:bold;">{i:02d}</span>&nbsp;&nbsp;<a href="{url}" style="color:#2f5c7a;text-decoration:none;">{esc(title)}</a></td></tr>'
    body=INTRO+f"""<tr><td style="padding:18px 24px 0 24px;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background-color:#dbe7f0;border-radius:4px;">
<tr><td style="padding:16px 20px 8px 20px;font-family:Arial,Helvetica,sans-serif;font-size:16px;font-weight:bold;color:#2f5c7a;letter-spacing:1px;">In this issue</td></tr>
<tr><td style="padding:0 20px 14px 20px;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0">{toc}</table></td></tr></table></td></tr>
<tr><td style="padding:0 24px;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0">"""
    for i,(label,img,title,teaser,url) in enumerate(ART,1):
        lc=COL[label]
        body+=f"""<tr><td style="padding:26px 0 0 0;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0">
<tr><td style="background-color:{lc};padding:7px 20px;font-family:Arial,Helvetica,sans-serif;font-size:12px;letter-spacing:2px;color:#fff;text-transform:uppercase;font-weight:bold;">{label}</td></tr>
<tr><td><a href="{url}"><img src="{BASE+img}" width="600" alt="{esc(title)}" style="display:block;width:100%;max-width:600px;height:auto;border:0;" /></a></td></tr>
<tr><td style="background-color:#6E97B8;padding:12px 20px;font-family:Arial,Helvetica,sans-serif;font-size:19px;line-height:24px;color:#fff;font-weight:bold;"><span style="opacity:0.85;">{i:02d}.</span>&nbsp; {esc(title)}</td></tr>
<tr><td style="padding:16px 22px 0 22px;font-family:Arial,Helvetica,sans-serif;font-size:15px;line-height:23px;color:#444;">{esc(teaser)}</td></tr>
<tr><td style="padding:14px 22px 0 22px;"><table role="presentation" cellpadding="0" cellspacing="0"><tr><td bgcolor="{BUTTON}" style="border-radius:4px;"><a href="{url}" style="display:inline-block;padding:9px 24px;font-family:Arial,Helvetica,sans-serif;font-size:14px;font-weight:bold;color:#fff;text-decoration:none;border-radius:4px;">Read more</a></td></tr></table></td></tr>
</table></td></tr>"""
    body+="</table></td></tr>"
    return wrap(head+body+EVENTS+footer())

open(os.path.join(EMAIL_DIR,"v1-green.html"),"w",encoding="utf-8").write(v1_green())
open(os.path.join(EMAIL_DIR,"v2-imageled.html"),"w",encoding="utf-8").write(v2_imageled())
shutil.copyfile(os.path.join(EMAIL_DIR,"knowhow-summer-2026-email.html"), os.path.join(EMAIL_DIR,"v3-alternating.html"))
shutil.copyfile(os.path.join(EMAIL_DIR,"sample-B-hero-list.html"), os.path.join(EMAIL_DIR,"v4-hero-list.html"))
print("wrote v1-green, v2-imageled, v3-alternating, v4-hero-list")

# ---------- Gallery index ----------
cards = [
 ("v1-green.html","1. Marketindex Edition","Our custom take: green brush-script masthead, an In-this-issue box and category-tagged cards. A fresh, distinctive look.","#0C4E42"),
 ("v3-alternating.html","2. Alternating","Photos alternate left and right with the text, category labels and even spacing. Balanced and editorial.","#8B9A3D"),
 ("v2-imageled.html","3. Image-led (full width)","A big full-width photo per story with a contents box. Closest to the printed KnowHow look.","#6E97B8"),
 ("v4-hero-list.html","4. Featured + list","One big lead story, then the rest as compact rows. Short and punchy.","#D9795E"),
]
cardhtml=""
for href,title,desc,c in cards:
    cardhtml+=f"""<a class="card" href="{href}" style="border-top:5px solid {c};">
<div class="ct" style="color:{c};">{title}</div><div class="cd">{desc}</div><div class="cl">Open preview &rsaquo;</div></a>"""
index=f"""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>KnowHow Summer 2026 - email layout options</title>
<style>
body{{margin:0;font-family:-apple-system,Segoe UI,Arial,sans-serif;background:#eef1f4;color:#222;}}
.hero{{background:#0C4E42;color:#fff;padding:34px 24px;text-align:center;}}
.hero h1{{margin:0 0 6px;font-size:24px;}} .hero p{{margin:0;color:#cfe0da;font-size:15px;}}
.wrap{{max-width:820px;margin:0 auto;padding:26px 18px 50px;}}
.grid{{display:grid;grid-template-columns:1fr 1fr;gap:18px;}}
@media(max-width:640px){{.grid{{grid-template-columns:1fr;}}}}
.card{{display:block;background:#fff;border-radius:8px;padding:20px;text-decoration:none;box-shadow:0 1px 4px rgba(0,0,0,.08);transition:transform .1s;}}
.card:hover{{transform:translateY(-2px);}}
.ct{{font-size:18px;font-weight:700;margin-bottom:8px;}} .cd{{color:#555;font-size:14px;line-height:20px;}}
.cl{{margin-top:12px;font-weight:700;color:#2f5c7a;font-size:14px;}}
.note{{margin-top:22px;font-size:13px;color:#666;line-height:19px;}}
</style></head><body>
<div class="hero"><h1>KnowHow &ndash; Summer 2026</h1><p>Email newsletter layout options for review</p></div>
<div class="wrap"><div class="grid">{cardhtml}</div>
<p class="note">Each option is a live preview of the email. Click any card to open it. The photos and "Read more" links go to the published articles on kelvincave.com.</p></div>
</body></html>"""
open(os.path.join(EMAIL_DIR,"index.html"),"w",encoding="utf-8").write(index)
print("wrote index.html gallery")
