---
name: guest-lookup
description: Find wedding guests and give exact lists from onDimi. Use when the couple asks who is coming, who declined, who hasn't replied, who has dietary or accessibility needs, a guest's details or messages, or to change one guest's information.
---

# Looking up guests

## Lists

Use `guest_list` with `business_id` and the narrowest filter:
- `rsvp`: `attending`, `declined` or `invited` (not yet answered). Returns
  parties with at least one member in that state.
- `engagement_state`: `replied`, `not_started`, `in_plan`, `done_no_reply`,
  `needs_attention`, `reached`.
- `address=incomplete`: parties missing part of their mailing address.
- `q`: a name, email or guest id.

The result has `guests`, `returned` and `next_skip`. When `next_skip` is not
null there are more: call again with `skip=next_skip` until it is null.

## Getting counts right

- State a count only after you have every page, and make it match the names
  you list. Count the list you're about to show, then say the number.
- Parties vs people: one guest row is one party; its `fields.party_members`
  are the people. "23 declined" should say whether that's parties or people,
  and the names should match that choice (for people, list each declined
  member, not just the party name).
- For campaign totals, `wedding_status_digest` and `plan_preflight` hold the
  verified numbers; use them rather than adding up lists.

## One guest

- `guest_get` for full details; `guest_message_history` for the conversation;
  `guest_upcoming_messages` for what's scheduled.
- Names: if a search finds nothing, try the closest spelling once (Jon/John).
  If the guest found has a different name than the couple said, confirm it's
  the right person before changing anything.
- To change details, `guest_edit` with only the fields that change. For RSVP
  changes, send the full `party_members` array with every member's status.
  Read the change back and get a yes first.
