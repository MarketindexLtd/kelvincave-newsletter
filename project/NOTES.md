# KnowHow Summer 2026 - project handoff notes

Full state of the Kelvin Cave "KnowHow" Summer 2026 email newsletter project, so it can be
picked up on any machine. Client of **Marketindex**. (Kelvin Cave = agricultural feed / silage
company, kelvincave.com.)

Last updated: 2026-07-30.

---

## 1. The goal

Kelvin Cave publish a printed **KnowHow** newsletter ~3x/year and wanted the Summer 2026 issue
turned into:
  1. Individual web **articles** on kelvincave.com (DONE by the client's own team - see section 4).
  2. An **email newsletter** to ~2,500 contacts, sent via **Brevo** (Standard plan ~£13/mo so the
     Brevo logo is removed). This repo is the email newsletter work.

Source material = the print PDF `knowhow summer 2026 PRESS_Press.pdf` (71 MB, provided by client;
lives locally in Downloads, NOT in git - too big).

---

## 2. Live preview site (this repo)

- Repo: **MarketindexLtd/kelvincave-newsletter** (public).
- GitHub Pages gallery: **https://marketindexltd.github.io/kelvincave-newsletter/**
- Four layout options for the client to choose from. **Careful: the gallery numbering does NOT
  match the filenames.** Gallery option number first:
  1. `v1-green.html`  - "Marketindex Edition": green brush-script masthead, In-this-issue box,
     category-tagged cards. Our distinctive custom take.
  2. `v3-alternating.html` - photos alternate left/right with text.
  3. `v2-imageled.html` - big full-width photo per story + contents box (closest to print).
     **<- THIS IS THE ONE THE CLIENT CHOSE (2026-07-30).** They referred to it as
     "version 3 image led", i.e. gallery option 3.
  4. `v4-hero-list.html` - one featured story then compact list.
- `index.html` = the gallery landing page (numbered cards linking to the four). Option 3 now
  carries a SELECTED chip and a footnote explaining the blue vs coral masthead.
- Images in repo root: `knowhow-masthead-blue.png` (blue, used by the selected v2),
  `knowhow-masthead.png` (coral, still used by v3/v4),
  `knowhow-masthead-green.png` (green, used by v1), `kc_logo.png`, `img-01.jpg`..`img-08.jpg`
  (the 8 hero photos, cropped to a uniform 3:2).

To update a version: edit the HTML (or the build script in `project/`, then rebuild), commit, push.
Pages redeploys automatically in ~30-60s.

---

## 3. Brand + design facts

- Green: **#0C4E42**  Gold: **#FDB724**  (sampled from the KC logo).
- Category-label colours: CASE STUDY `#8B9A3D` (olive), TECHNICAL ARTICLE `#D9795E` (coral),
  NEWS / PRODUCTS `#6E97B8` (blue).
- **Seasonal masthead colour.** KnowHow changes masthead colour by season. The coral masthead we
  started from was their **Autumn** edition (the sample they first sent us). Summer 2026 is
  **blue** - confirmed by the client 2026-07-30, matching the issue they just printed.
  So: coral = Autumn, blue = Summer. Ask which colour applies before building a future issue.
- Masthead files: coral `knowhow-masthead.png` was their previous email masthead (createsend URL)
  and is the source image. `knowhow-masthead-blue.png` (#6E97B8 brand blue) and
  `knowhow-masthead-green.png` were made by recolouring it. Use
  `project/recolour_masthead.py` to generate a new season colour - edit `TARGET_BG` and `OUT`,
  then run it. It swaps only the background, keeping the cream wordmark, tagline, brushed
  bottom edge and the KC logo intact.
- Blue chosen for the masthead is `#6E97B8`, the same blue already used for the article title
  bands, contents box and footer in v2, so the masthead ties into the layout.
- Emails are 600px, table-based, inline styles, bulletproof buttons. No emojis, no em dashes
  (client copy rules).
- Article spacing in v2 is controlled by `GAP` (space above each article block) and
  `GAP_AFTER_BUTTON` (space below the Read more button) at the top of `build_gallery.py`.
  Currently 40 + 8 = 48px between articles, raised from 26px on client feedback 2026-07-30 that
  the articles were too close together. Turn these two knobs if asked for more or less air.

---

## 4. The 8 live articles (used in the email)

Published by the client on kelvincave.com. Email "Read more" buttons point to these:

| # | Title | Category | URL |
|---|-------|----------|-----|
| 1 | Sheep TMR bolstered by home-grown beans | Proteins | /proteins/sheep-tmr-bolstered-by-home-grown-beans/ |
| 2 | Propcorn NC beats grain drying on cost and nutrition | Cereals | /cereals/propcorn-nc-beats-grain-drying-on-cost-and-nutrition/ |
| 3 | Tiny threats, big losses: grain store pest control | Cereals | /cereals/tiny-threats-big-losses-why-grain-store-pest-control-matters/ |
| 4 | Investment in calf housing for a dairy-Wagyu future | Forage | /forage/investment-in-calf-housing-for-a-dairy-wagyu-future/ |
| 5 | A new feed on the block | News | /news/a-new-feed-on-the-block/ |
| 6 | Bespoke KC frame allows quick switch from silage to grain | Machinery | /machinery/bespoke-kc-frame-allows-quick-switch-from-silage-to-grain/ |
| 7 | Stacking haylage in your favour | Forage | /forage/stacking-haylage-in-your-favour/ |
| 8 | Moisture meters for grain and hay | Forage | /forage/moisture-meters-for-grain-and-hay/ |

NOT in the email (were in the print issue but not published as separate web articles):
the "5Ps product range" spread, "Could Wagyu work for you?", and "Perfecting your cereal crimping".

---

## 5. Outstanding TODO

- [x] **Client picks a layout** - DONE 2026-07-30. They chose gallery option 3, the image-led
      full-width version = `v2-imageled.html`.
- [x] **Masthead recoloured to blue** - DONE 2026-07-30 on the selected version. See section 3.
- [x] **PDF download link** - DONE 2026-07-30. The client hosted it themselves at
      https://kelvincave.com/wp-content/uploads/2026/06/knowhow-summer-2026.pdf
      (6.1 MB, already compressed down from the 71 MB press PDF, returns HTTP 200). Wired into
      all four versions and into `PDF_URL` in `build_gallery.py`.
- [x] **Brevo-ready file** - DONE 2026-07-30. `knowhow-summer-2026-brevo.html`, generated by
      `project/build_brevo.py`. This is the file to paste into Brevo. See section 6.
- [ ] **Brevo build** - needs someone with access to the Kelvin Cave Brevo account. Everything on
      our side is ready; section 6 is the step-by-step.
- [ ] **Brevo SPF/DKIM for kelvincave.com** - needs the client's web/IT. Longest-lead item for a
      2,500-contact send, so request it now rather than on send day.
- [ ] **Optional, worth raising with the client:** the selected version has no issue/date marker
      anywhere in the email body. The printed cover carries "SUMMER 2026" top-right in the
      masthead; our masthead image does not. v1 solves this with a gold "SUMMER 2026" strip under
      the masthead. Consider adding the same strip (in blue/cream) to v2, or burning the text into
      the masthead image. Not done - it changes the agreed design, so ask first.
- [ ] **Unlink cleanup**: moghees-hub is currently a *temporary* Write collaborator on this repo
      (so the CLI could push). Remove it when done. Also delete the duplicate repo
      **moghees-hub/kelvincave-newsletter** (created as a fallback before org hosting worked).

## 6. Brevo build checklist (for the sender)

**Paste `knowhow-summer-2026-brevo.html`, NOT `v2-imageled.html`.** The Brevo file is generated
from the preview by `project/build_brevo.py` and differs in three ways, all of which are the first
three things you would otherwise have to fix by hand:
  - masthead src rewritten to an absolute URL (a relative path does not resolve inside Brevo),
  - unsubscribe link set to Brevo's `{{ unsubscribe }}` merge tag,
  - a hidden preheader added (the grey preview line beside the subject in the inbox).
Rerun `python project/build_brevo.py` after any edit to `v2-imageled.html` so the two do not drift.
It hard-fails if any relative reference survives, rather than shipping broken images.

1. New campaign > Email > "paste your own HTML"; paste **`knowhow-summer-2026-brevo.html`**.
2. Images: the 8 article photos and the PDF are already absolute kelvincave.com URLs, so they need
   nothing. **The masthead is the one to think about** - it currently points at GitHub Pages:
   https://marketindexltd.github.io/kelvincave-newsletter/knowhow-masthead-blue.png
   That works, but it means a sent newsletter depends on this repo staying public forever. Better:
   upload `knowhow-masthead-blue.png` to the client's WordPress media library (where the article
   photos and the PDF already live) or to Brevo's image library, and swap `PAGES_BASE` in
   `build_brevo.py` for that URL. Do this before a real send if you can.
3. Confirm the `{{ unsubscribe }}` tag is the right syntax for the account in Brevo's editor - it
   should render as a working unsubscribe link in the test send. Swap it for whatever tag Brevo's
   own footer block uses if it does not.
4. PDF link is already wired (section 5) - nothing to do, but click it in the test send to confirm.
5. Set sender name/email (e.g. info@kelvincave.com) and the subject. The preheader is already in
   the HTML; if Brevo also offers a preheader field, leave it blank so they do not double up.
   Subject: "Your Summer 2026 KnowHow: cutting feed costs, harvest prep and home-grown feed".
6. Send a test to yourself, check mobile + desktop, then send.
7. Need the sender domain (kelvincave.com) authenticated in Brevo (SPF/DKIM) for deliverability
   to 2,500 people. Client's web/IT to add Brevo's DNS records. **Long-lead item - request it now,
   in parallel with building the campaign, rather than discovering it on send day.**

## 7. Client email (ask them to choose) - SENT AND ANSWERED

Kept for reference / reuse on the next issue. They came back on 2026-07-30 choosing option 3 and
flagging the seasonal masthead colour (see section 3).

Subject: KnowHow Summer 2026 email - please pick a layout

Hi [Name],
Now that you've got the Summer 2026 KnowHow articles up on the website, I've built the email
newsletter to go out to your contacts. I've mocked it up in four layouts so you can compare them.
Have a look here and let me know which you prefer:
https://marketindexltd.github.io/kelvincave-newsletter/
Each one is a working preview - just click an option to open it, and the photos and links go
through to your live articles. Once you've picked, I'll finalise it ready to send.
Thanks, [Your name]

---

## 8. How to rebuild (toolchain)

Scripts are in `project/`. They were written on Windows with **hardcoded absolute paths**
(`C:\Users\Admin\...`) - update those paths for your machine before running.

- Python 3.12 + libs: `pip install pymupdf python-docx pillow`

**Email build scripts included in `project/` (these are what you need to continue the newsletter):**
- `build_final.py` - builds v3 alternating (the canonical `knowhow-summer-2026-email.html`).
- `build_variants.py` - builds the alternating + hero-list samples (v4 source).
- `build_gallery.py` - builds v1 (green), v2 (image-led), copies v3/v4, writes `index.html`.
  Run order to regenerate all: `build_final.py` -> `build_variants.py` -> `build_gallery.py`.
- `build_email.py` - earlier standalone v2 image-led generator (superseded by build_gallery).
- `build_brevo.py` - turns `v2-imageled.html` into the paste-into-Brevo
  `knowhow-summer-2026-brevo.html`. Relative paths, stdlib only, runs anywhere. See section 6.
- `recolour_masthead.py` - recolours the masthead background to a new season colour, keeping the
  cream wordmark, brush edge and KC logo. Edit `TARGET_BG`/`OUT` and run. Uses relative paths, so
  unlike the other scripts it runs anywhere. This is what produced `knowhow-masthead-blue.png`.
- Previews were rendered with headless Edge (`msedge --headless=new --screenshot=out.png <file-uri>`).

**Not in the repo** (their job is finished - the 11 web articles are already published, so these
were one-off): the PDF-extraction and Word-doc scripts (`extract_images.py`, `crop_tables.py`,
`fix_tables.py`, `render_pages.py`, `build_doc.py`). They produced a local
`KnowHow-Summer-2026-website` folder of 11 per-article Word docs (each with photos + table images
cropped from the PDF) that the client used to publish the site. Ask Claude to regenerate them from
the print PDF if ever needed.

Deliverable HTML/images are already committed to repo root, so simple layout tweaks can be made by
editing the HTML directly without rerunning Python.
