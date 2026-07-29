# -*- coding: utf-8 -*-
import os
from PIL import Image

EMAIL_DIR = r"C:\Users\Admin\Downloads\KnowHow-Summer-2026-email"
os.makedirs(EMAIL_DIR, exist_ok=True)

# save masthead (resize to 1200 wide for retina, display 600)
mast = Image.open(r"C:\Users\Admin\AppData\Local\Temp\claude\c--Users-Admin-fathom-slack-bot\d769469e-9076-49e3-81cb-be5afd595a11\scratchpad\mast_raw.png").convert("RGB")
w,h = mast.size
mast = mast.resize((1200, int(h*1200/w)), Image.LANCZOS)
mast.save(os.path.join(EMAIL_DIR, "knowhow-masthead.png"), "PNG")
print("masthead saved", mast.size)

BASE = "https://kelvincave.com/wp-content/uploads/2026/07/"
COL = {"CASE STUDY":"#8B9A3D", "TECHNICAL ARTICLE":"#D9795E", "NEWS":"#6E97B8", "PRODUCTS":"#6E97B8"}
TITLEBAR = "#6E97B8"   # blue title bar
BUTTON   = "#8B9A3D"   # olive-green button

ART = [
 ("CASE STUDY", "01_sheep-tmr-bolstered-by-home-grown-beans_01.jpg",
  "Sheep TMR bolstered by home-grown beans",
  "How Myerscough College cut pre-lambing feed costs by 37% by moving its ewes onto a home-grown TMR built on wholecrop beans and crimped wheat, with no soya and healthier stock.",
  "https://kelvincave.com/proteins/sheep-tmr-bolstered-by-home-grown-beans/"),
 ("TECHNICAL ARTICLE", "03_propcorn-nc-beats-grain-drying-on-cost-a_02.jpg",
  "Propcorn NC beats grain drying on cost and nutrition",
  "With fuel prices high, Dr George Fisher compares drying grain against treating it with Propcorn NC, and finds preserving comes out around 40% cheaper, with nutritional benefits too.",
  "https://kelvincave.com/cereals/propcorn-nc-beats-grain-drying-on-cost-and-nutrition/"),
 ("TECHNICAL ARTICLE", "02_tiny-threats-big-losses-why-grain-store-_01.jpg",
  "Tiny threats, big losses: why grain store pest control matters",
  "James Phelps of Barrettine on the pests that can wreck stored grain, how to spot the worst offenders, and how to prepare your store before harvest.",
  "https://kelvincave.com/cereals/tiny-threats-big-losses-why-grain-store-pest-control-matters/"),
 ("CASE STUDY", "05_investment-in-calf-housing-for-a-dairy-w_07.jpg",
  "Investment in calf housing for a dairy-Wagyu future",
  "Inside the Mann family's new Cumbrian calf unit, purpose-built for health and performance as they move their dairy herd to Wagyu crossing.",
  "https://kelvincave.com/forage/investment-in-calf-housing-for-a-dairy-wagyu-future/"),
 ("NEWS", "08_a-new-feed-on-the-block_02.jpg",
  "A new feed on the block",
  "Kelvin Cave, Veolia and partners have found a way to preserve surplus supermarket food into a nutritionally dense new feed, soon available to UK farmers.",
  "https://kelvincave.com/news/a-new-feed-on-the-block/"),
 ("CASE STUDY", "09_bespoke-kc-frame-allows-quick-switch-fro_01.jpg",
  "Bespoke KC frame allows quick switch from silage to grain",
  "A Warwickshire farm's bespoke front-mounted IBC carrier and Silaspray, built in the Kelvin Cave workshop, switches from treating silage to treating grain in minutes.",
  "https://kelvincave.com/machinery/bespoke-kc-frame-allows-quick-switch-from-silage-to-grain/"),
 ("TECHNICAL ARTICLE", "10_stacking-haylage-in-your-favour_02.jpg",
  "Stacking haylage in your favour",
  "With wrap costs and plastic pressures rising, we compare wrapping bales against preserving high-moisture hay with BaleSafe, and how to store it unwrapped.",
  "https://kelvincave.com/forage/stacking-haylage-in-your-favour/"),
 ("PRODUCTS", "11_moisture-meters-for-grain-and-hay_01.jpg",
  "Moisture meters for grain and hay",
  "Accurate moisture readings take the guesswork out of preservation. A look at the Wile 55 and Wile 25 meters, plus where to see us at the 2026 shows.",
  "https://kelvincave.com/forage/moisture-meters-for-grain-and-hay/"),
]

def esc(s): return s.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")

# Table of contents rows
toc_rows = ""
for i,(label,img,title,teaser,url) in enumerate(ART, 1):
    toc_rows += (f'<tr><td style="padding:3px 0; font-family:Arial,Helvetica,sans-serif; font-size:14px; line-height:20px; color:#2f5c7a;">'
                 f'<span style="color:#6E97B8; font-weight:bold;">{i:02d}</span>&nbsp;&nbsp;'
                 f'<a href="{url}" style="color:#2f5c7a; text-decoration:none;">{esc(title)}</a></td></tr>\n')

# Article blocks
blocks = ""
for i,(label,img,title,teaser,url) in enumerate(ART, 1):
    labelcol = COL[label]
    imgurl = BASE + img
    blocks += f"""
          <!-- ARTICLE {i:02d} -->
          <tr><td style="padding:26px 0 0 0;">
            <table role="presentation" width="100%" cellpadding="0" cellspacing="0">
              <tr><td style="background-color:{labelcol}; padding:7px 20px; font-family:Arial,Helvetica,sans-serif; font-size:12px; letter-spacing:2px; color:#ffffff; text-transform:uppercase; font-weight:bold;">{label}</td></tr>
              <tr><td><a href="{url}"><img src="{imgurl}" width="600" alt="{esc(title)}" style="display:block; width:100%; max-width:600px; height:auto; border:0;" /></a></td></tr>
              <tr><td style="background-color:{TITLEBAR}; padding:12px 20px; font-family:Arial,Helvetica,sans-serif; font-size:19px; line-height:24px; color:#ffffff; font-weight:bold;">
                <span style="opacity:0.85;">{i:02d}.</span>&nbsp; {esc(title)}
              </td></tr>
              <tr><td style="padding:16px 22px 0 22px; font-family:Arial,Helvetica,sans-serif; font-size:15px; line-height:23px; color:#444444;">{esc(teaser)}</td></tr>
              <tr><td style="padding:14px 22px 0 22px;">
                <table role="presentation" cellpadding="0" cellspacing="0"><tr><td align="center" bgcolor="{BUTTON}" style="border-radius:4px;">
                  <a href="{url}" style="display:inline-block; padding:9px 24px; font-family:Arial,Helvetica,sans-serif; font-size:14px; font-weight:bold; color:#ffffff; text-decoration:none; border-radius:4px;">Read more</a>
                </td></tr></table>
              </td></tr>
            </table>
          </td></tr>"""

html = f"""<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>KnowHow Summer 2026</title>
<!--[if mso]><style type="text/css">body,table,td{{font-family:Arial,Helvetica,sans-serif !important;}}</style><![endif]-->
</head>
<body style="margin:0; padding:0; background-color:#eef1f4;">
  <div style="display:none; max-height:0; overflow:hidden; mso-hide:all; font-size:1px; line-height:1px; color:#eef1f4;">
    Science and innovation at the heart of everything we do. Your Summer 2026 KnowHow: cutting feed costs, harvest prep and home-grown feed.
  </div>
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background-color:#eef1f4;">
    <tr><td align="center" style="padding:20px 10px;">
      <table role="presentation" width="600" cellpadding="0" cellspacing="0" style="width:600px; max-width:600px; background-color:#ffffff; border-collapse:collapse;">

        <!-- Masthead -->
        <tr><td><img src="knowhow-masthead.png" width="600" alt="KnowHow Summer 2026 - Kelvin Cave" style="display:block; width:100%; max-width:600px; height:auto; border:0;" /></td></tr>

        <!-- Intro -->
        <tr><td style="padding:24px 24px 4px 24px; font-family:Arial,Helvetica,sans-serif; font-size:16px; line-height:24px; color:#333333;">
          <p style="margin:0 0 12px 0;">Welcome to the Summer 2026 edition of KnowHow.</p>
          <p style="margin:0;">There is plenty to get your teeth into this issue. As harvest approaches, we look at ways to get more from home-grown and locally sourced feeds, from a 37% pre-lambing feed cost saving to preserving grain without drying. Read the full articles on our website using the links below.</p>
        </td></tr>

        <!-- Table of contents -->
        <tr><td style="padding:18px 24px 0 24px;">
          <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background-color:#dbe7f0; border-radius:4px;">
            <tr><td style="padding:16px 20px 8px 20px; font-family:Arial,Helvetica,sans-serif; font-size:16px; font-weight:bold; color:#2f5c7a; letter-spacing:1px;">In this issue</td></tr>
            <tr><td style="padding:0 20px 14px 20px;">
              <table role="presentation" width="100%" cellpadding="0" cellspacing="0">
                {toc_rows}
              </table>
            </td></tr>
          </table>
        </td></tr>

        <!-- Articles -->
        <tr><td style="padding:0 24px;">
          <table role="presentation" width="100%" cellpadding="0" cellspacing="0">
            {blocks}
          </table>
        </td></tr>

        <!-- Events strip -->
        <tr><td style="padding:28px 24px 0 24px;">
          <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background-color:#f3f1ea; border-left:4px solid #FDB724;">
            <tr><td style="padding:16px 18px; font-family:Arial,Helvetica,sans-serif; font-size:14px; line-height:21px; color:#333333;">
              <strong style="color:#0C4E42;">Come and see us in 2026</strong><br />
              Royal Highland Show, 18 to 21 June, Ingliston, Edinburgh<br />
              Royal Welsh Show, 20 to 23 July, Llanelwedd, Builth Wells, Powys
            </td></tr>
          </table>
        </td></tr>

        <!-- Footer -->
        <tr><td align="center" style="background-color:#6E97B8; padding:26px 24px; margin-top:26px;">
          <div style="font-family:Arial,Helvetica,sans-serif; font-size:14px; line-height:22px; color:#ffffff;">
            <strong>Kelvin Cave Ltd</strong><br />
            Call us on 01458 252281<br />
            <a href="mailto:info@kelvincave.com" style="color:#ffffff; text-decoration:underline;">info@kelvincave.com</a>&nbsp;&nbsp;|&nbsp;&nbsp;<a href="https://www.kelvincave.com" style="color:#ffffff; text-decoration:underline;">kelvincave.com</a>
          </div>
        </td></tr>
        <tr><td align="center" style="background-color:#5c86a6; padding:14px 24px; font-family:Arial,Helvetica,sans-serif; font-size:12px; line-height:18px; color:#e8eef3;">
          You are receiving this because you are a Kelvin Cave contact.<br />
          <a href="{{{{ unsubscribe }}}}" style="color:#e8eef3; text-decoration:underline;">Unsubscribe</a>
        </td></tr>

      </table>
    </td></tr>
  </table>
</body>
</html>"""

outp = os.path.join(EMAIL_DIR, "knowhow-summer-2026-email.html")
with open(outp, "w", encoding="utf-8") as f:
    f.write(html)
print("saved", outp, round(len(html)/1024,1), "KB")
