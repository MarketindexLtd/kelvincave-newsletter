# KnowHow Summer 2026 - project handoff notes

Full state of the Kelvin Cave "KnowHow" Summer 2026 email newsletter project, so it can be
picked up on any machine. Client of **Marketindex**. (Kelvin Cave = agricultural feed / silage
company, kelvincave.com.)

Last updated: 2026-07-29.

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
- Four layout options for the client to choose from:
  1. `v1-green.html`  - "Marketindex Edition": green brush-script masthead, In-this-issue box,
     category-tagged cards. Our distinctive custom take.
  2. `v3-alternating.html` - photos alternate left/right with text.
  3. `v2-imageled.html` - big full-width photo per story + contents box (closest to print).
  4. `v4-hero-list.html` - one featured story then compact list.
- `index.html` = the gallery landing page (numbered cards linking to the four).
- Images in repo root: `knowhow-masthead.png` (coral, used by v2/v3/v4),
  `knowhow-masthead-green.png` (green, used by v1), `kc_logo.png`, `img-01.jpg`..`img-08.jpg`
  (the 8 hero photos, cropped to a uniform 3:2).

To update a version: edit the HTML (or the build script in `project/`, then rebuild), commit, push.
Pages redeploys automatically in ~30-60s.

---

## 3. Brand + design facts

- Green: **#0C4E42**  Gold: **#FDB724**  (sampled from the KC logo).
- Category-label colours: CASE STUDY `#8B9A3D` (olive), TECHNICAL ARTICLE `#D9795E` (coral),
  NEWS / PRODUCTS `#6E97B8` (blue).
- Masthead source: the KnowHow wordmark. Coral version was their previous email masthead
  (createsend URL). Green version was made by recolouring the coral one (see
  `project/` scripts). The print cover masthead is blue.
- Emails are 600px, table-based, inline styles, bulletproof buttons. No emojis, no em dashes
  (client copy rules).

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

- [ ] **Client picks a layout** (email draft is in section 7). Then finalise that one.
- [ ] **PDF download link**: all 4 emails have a placeholder line "Prefer the full magazine? Read
      the complete issue as a PDF" with `href="#"`. Still to do: compress the 71 MB print PDF to a
      few MB, host it (client WordPress media or similar), and drop the real URL into the `href`.
- [ ] **Brevo build** (see section 6).
- [ ] **Unlink cleanup**: moghees-hub is currently a *temporary* Write collaborator on this repo
      (so the CLI could push). Remove it when done. Also delete the duplicate repo
      **moghees-hub/kelvincave-newsletter** (created as a fallback before org hosting worked).

## 6. Brevo build checklist (for the sender)

1. New campaign > Email > "paste your own HTML"; paste the chosen version's HTML.
2. Upload images to Brevo and repoint: the masthead (`knowhow-masthead*.png`) and the 8 photos
   (`img-01`..`img-08.jpg`). (The `img-*` are also served from this repo if you prefer absolute URLs.)
3. Replace `{{ unsubscribe }}` / the `#` unsubscribe link with Brevo's unsubscribe tag.
4. Wire the PDF placeholder link once the PDF is hosted.
5. Set sender name/email (e.g. info@kelvincave.com), subject + preheader.
   Subject: "Your Summer 2026 KnowHow: cutting feed costs, harvest prep and home-grown feed".
6. Send a test to yourself, check mobile + desktop, then send.
7. Need the sender domain (kelvincave.com) authenticated in Brevo (SPF/DKIM) for deliverability
   to 2,500 people. Client's web/IT to add Brevo's DNS records.

## 7. Client email (ask them to choose)

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
- Previews were rendered with headless Edge (`msedge --headless=new --screenshot=out.png <file-uri>`).

**Not in the repo** (their job is finished - the 11 web articles are already published, so these
were one-off): the PDF-extraction and Word-doc scripts (`extract_images.py`, `crop_tables.py`,
`fix_tables.py`, `render_pages.py`, `build_doc.py`). They produced a local
`KnowHow-Summer-2026-website` folder of 11 per-article Word docs (each with photos + table images
cropped from the PDF) that the client used to publish the site. Ask Claude to regenerate them from
the print PDF if ever needed.

Deliverable HTML/images are already committed to repo root, so simple layout tweaks can be made by
editing the HTML directly without rerunning Python.
