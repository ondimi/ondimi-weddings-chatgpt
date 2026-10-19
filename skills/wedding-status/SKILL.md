---
name: wedding-status
description: Report how the wedding's guest communication is going. Use when the couple asks for an update, a status check, "how are we doing", "any news", how many are coming, or what still needs attention.
---

# The wedding status check

1. Call `wedding_status_digest` with `business_id`. It returns the RSVP tally,
   guests missing addresses or needing attention, plan progress, unanswered
   guests, messages scheduled soon, recent updates, and `next_steps`.
2. Lead with the headline numbers, using the digest's figures exactly:
   attending, declined, not yet answered (count guest parties and people as
   the digest does; say which you mean).
3. Then what needs the couple, at most three items, each with an offer:
   - parties still missing an address → offer the address campaign;
   - unanswered after the plan ran out → offer another round
     (`rsvp-campaign`);
   - milestones not set → offer to set the timeline;
   - guests with dietary, accessibility or seating notes → offer the list.
4. Mention what's scheduled next ("12 reminders go out tomorrow").
5. If nothing needs attention, say so in one line.

## Numbers must be exact

- Use the counts tools return; never estimate or recount by hand.
- When you list names, list exactly as many as the count you state. If a
  list is paged (`guest_list` returns `next_skip`), fetch every page before
  saying "these are all of them".
- "Needs attention" categories overlap: one party can have several needs, so
  the categories can add up to more than the total.

For the details of each thread, `concierge_guide` topic `daily-check-routine`
has the reference.
