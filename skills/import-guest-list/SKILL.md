---
name: import-guest-list
description: Import a wedding guest list into onDimi. Use when the couple pastes or attaches a guest list, spreadsheet, CSV, or an export from a wedding website, or asks to add many guests at once.
---

# Importing a guest list

## Steps

1. **Get the list as text.** If the couple attached a file, read it and use
   its contents. A pasted table is fine. One row per party (one invitation).
2. **Check the shape before importing.** Look for name, phone, email and
   address columns, and for how party members are listed. If the list has no
   party column but rows clearly belong together (same household, "& guest"),
   ask whether to keep them as one party. If more than a third of rows have
   neither phone nor email, mention that those guests can't be contacted until
   one is added.
3. **Call `guest_list_import`** with `business_id` and the text. Column names
   are matched loosely (first/last/name, phone/mobile/cell, address/street,
   zip/postal code, and the wedding's own fields from `guest_fields`).
   - Party members: a `party_members` column (`Priya:attending|Ravi:invited`)
     or a `party` column of names.
   - Rows that match an existing party fill in blanks instead of duplicating.
   - Importing sends nothing to anyone.
4. **Report the result** in plain words: how many parties were added, how
   many existing ones were filled in, and every rejected row with its reason
   (for example an unusable phone number). Offer to fix rejected rows one by
   one with `guests_add` or `guest_edit`.
5. **Offer the next step:** "Want me to start collecting RSVPs from the new
   guests?" If yes, follow the `rsvp-campaign` skill.

## Single guests

To add or correct one or two parties, use `guests_add` (a list of guests, each
with `first_name`, `last_name` and a mobile or email) or `guest_edit`. Confirm
the details with the couple before writing.

## Watch for

- Phone numbers: send them as the couple gave them; onDimi normalizes them.
- `fields.guest_relation` must be one of the wedding's allowed values
  (`guest_fields` lists them). If a value is rejected, the error lists the
  allowed ones; pick the closest and confirm.
- Never invent guests, emails or phone numbers to fill gaps.
