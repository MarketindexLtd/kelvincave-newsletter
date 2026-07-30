# Brevo setup for the KnowHow newsletter

Runbook for getting Kelvin Cave able to send the KnowHow email to ~2,500 contacts via Brevo.
Section 3 (DNS) is the part that needs the client's web/IT and is the long-lead item, so start it
first. Once the domain is authenticated, the campaign build itself is `NOTES.md` section 6.

DNS facts below were checked live on **2026-07-30**. Re-check before acting on them.

---

## 1. Account and plan

- Sending as **kelvincave.com**, so the Brevo account should ideally be the **client's own**, with
  Marketindex added as a user. Avoid sending a client's list from a Marketindex-owned account: the
  contacts, the unsubscribe state and the sending reputation should all belong to them.
- **Free plan is not enough.** It caps at 300 emails/day, and this is a ~2,500 send. It also puts
  Brevo branding in the footer.
- **Standard (~£13/mo at 20k emails/month)** covers a 2,500 send comfortably and removes the Brevo
  logo. This is what the project assumed from the start.
- Nothing about the HTML depends on the plan, so the plan can be picked at send time.

## 2. Contacts

- ~2,500 contacts need importing as a Brevo list. Get the export from the client (or from whatever
  they used before - see the createsend note in section 3, they were on Campaign Monitor).
- **Carry over existing unsubscribes and bounces.** If the old platform's suppression list is not
  imported, people who already opted out will be emailed again. That is the single worst mistake
  available here, both legally (UK GDPR / PECR) and reputationally. Import unsubscribes into
  Brevo's blocklist before the first send.
- Brevo counts contacts, not emails, on some plan tiers - check 2,500 fits the tier chosen.

## 3. Sender domain authentication (DNS) - DO THIS FIRST

Without this, a 2,500-contact send from kelvincave.com will land in spam or be rejected. The
records go in at **GoDaddy** - kelvincave.com's nameservers are `ns47/ns48.domaincontrol.com`.

### 3a. The SPF record - MERGE, do not add a second one

kelvincave.com **already has an SPF record**, and it ends in `-all` (hard fail), so Brevo will fail
SPF outright until it is added.

Current record on the root of kelvincave.com:

```
v=spf1 include:_spf.createsend.com ip4:100.42.120.96/27 include:mailgun.org include:spf.protection.outlook.com -all
```

Change it to (one `include:spf.brevo.com` added, everything else untouched):

```
v=spf1 include:_spf.createsend.com ip4:100.42.120.96/27 include:mailgun.org include:spf.protection.outlook.com include:spf.brevo.com -all
```

**A domain may only have ONE SPF record.** Adding a second TXT record starting `v=spf1` breaks SPF
for *all* their mail, including the Microsoft 365 mailboxes. Edit the existing record in place.

**SPF lookup budget.** SPF allows a maximum of 10 DNS lookups; exceeding it makes the record
invalid (`permerror`) and, again, breaks all their mail. Current usage is **7 of 10**:

| Term | Lookups |
|---|---|
| `include:_spf.createsend.com` | 1 |
| `include:mailgun.org` -> `_spf.mailgun.org` -> `_spf1`/`_spf2`, plus `_spf.eu.mailgun.org` | 5 |
| `include:spf.protection.outlook.com` | 1 |
| `ip4:100.42.120.96/27` | 0 (IPs are free) |

`spf.brevo.com` is a flat list of `ip4` blocks with no nested includes, so it costs exactly **1**.
That takes them to **8 of 10**. Safe, but with only 2 to spare - so do not let anyone bolt on
another platform without re-counting. `project/spf_lookup_count.sh` in this repo recounts it.

**Possible cleanup while in there:** `_spf.createsend.com` is Campaign Monitor, their *previous*
email platform (the old coral masthead was served from a createsend URL). If they have genuinely
left Campaign Monitor, removing that include frees a lookup and shrinks their authorised-sender
surface. Confirm with the client before removing - do not assume.

### 3b. DKIM and domain verification

In Brevo: **Senders, Domains & Dedicated IPs > Domains > Add a domain**, then follow its
"Authenticate this domain" flow. Brevo generates **account-specific values**, so copy them verbatim
from the dashboard rather than from any guide, including this one.

Expect roughly:
- a **DKIM** TXT record on a Brevo-specific selector (Brevo currently uses `brevo._domainkey`),
  value starting `k=rsa; p=...`
- a **domain verification** TXT record (Brevo currently uses a `brevo-code` record)

Confirmed on 2026-07-30 that kelvincave.com has **no** `brevo._domainkey`, `mail._domainkey`,
`brevo-code` or `sib-domain-verification` records, so this is a clean first-time setup with nothing
stale to clear out.

**GoDaddy gotchas:**
- For a record at the domain root, GoDaddy's Name field wants `@`.
- GoDaddy appends the domain automatically. Enter `brevo._domainkey`, **not**
  `brevo._domainkey.kelvincave.com`, or you get `brevo._domainkey.kelvincave.com.kelvincave.com`.
- DKIM values are long. If GoDaddy rejects it for length, paste it without spaces/line breaks.

### 3c. DMARC

Already present and permissive, so it will not block the send:

```
v=DMARC1; p=none; sp=none; adkim=r; aspf=r; pct=100; fo=0; rf=afrf; ri=86400
```

`p=none` means failures are only monitored, and relaxed alignment (`adkim=r`/`aspf=r`) means a
properly authenticated Brevo send will align fine. **No change needed for this send.** Tightening
to `p=quarantine` later is a good idea, but do it *after* Brevo is authenticated and verified in a
test send, never before, or legitimate mail starts disappearing.

### 3d. Verify before sending

- Click **Verify / Authenticate** in Brevo and wait for green ticks. GoDaddy propagation is usually
  minutes but allow a few hours.
- Re-run `project/spf_lookup_count.sh kelvincave.com` and confirm it reports 8 and lists brevo.
- Send a test to a Gmail address, open **Show original**, and confirm `SPF: PASS`, `DKIM: PASS`,
  `DMARC: PASS`. Do not skip this - it is the only real proof the DNS work landed.

## 4. Then build the campaign

Paste `knowhow-summer-2026-brevo.html` - see `NOTES.md` section 6 for the full checklist,
including the one outstanding decision about where the masthead image is hosted.

## 5. Sequence

1. Request the DNS records (section 3) - client web/IT. **Longest lead, start now.**
2. In parallel: sort the account/plan (1) and get the contact export incl. unsubscribes (2).
3. DNS verified green in Brevo, confirmed via a Gmail test (3d).
4. Build and test the campaign (`NOTES.md` section 6).
5. Send.
