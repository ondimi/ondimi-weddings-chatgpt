---
name: guest-questions
description: Keep the information onDimi's concierge uses to answer guests current. Use when the couple shares wedding details guests will ask about (venue, times, dress code, parking, hotel blocks, shuttles, registry, kids, dietary options), or asks what guests are being told.
---

# Keeping the concierge's answers current

When guests text, chat or call, the concierge answers from the wedding's
**knowledge**. Updating it changes what every guest hears from that moment.

## Steps

1. `knowledge_list` with `business_id` to see the current entries (venue,
   accommodation, FAQ, food and beverage, our story, updates).
2. Pick the entry that covers the topic. Entries are updated, not created,
   from here: if nothing fits exactly, add the facts to the closest entry
   (often FAQ or updates) under a clear heading.
3. Write the new content with the couple's exact facts: names, addresses,
   times, links. Keep everything already in the entry that is still true; the
   update replaces the content field. Keep it factual; the concierge quotes
   from it.
4. Show the couple the before and after, get a yes, then `knowledge_update`.
   Some entries are also shown on the couple's wedding website (the entry's
   visibility setting); mention it when that's the case.
5. If the change is something guests should hear about now (a new time, a
   moved venue), offer to send an update too (`send-guest-update`). Knowledge
   only answers guests who ask.

## Also useful

- `wedding_details` / `wedding_details_update` hold the wedding's structured
  facts (date, time, names, milestone dates, contact details). Keep both in
  step when a fact appears in each.
- `guest_message_history` shows what a guest asked and how the concierge
  replied, handy when the couple asks "what did we tell Harper?".
- Never put private notes about specific guests into knowledge; every guest
  can be told what's in it.
