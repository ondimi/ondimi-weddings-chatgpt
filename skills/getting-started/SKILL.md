---
name: getting-started
description: First steps with onDimi, including the wedding setup that must be done before any guest can be contacted. Use when the couple has just connected onDimi, asks what onDimi can do, says they are new, or when their wedding has missing details, no knowledge, or no guests yet.
---

# Getting started with onDimi

onDimi runs an AI guest concierge for one wedding. It texts, emails, calls and
chats with each guest party to collect RSVPs, mailing addresses and other
details, answers guest questions from the wedding's information, and sends the
updates the couple approves. You help the couple steer it.

**Setup comes first.** onDimi refuses to contact any guest (plans and updates
alike) until the wedding's account details and wedding details are complete.
The wedding information (knowledge) isn't enforced, but without it the
concierge can't answer guests' questions. Get both done before outreach. The
couple can fill them in here with you, or on their onDimi dashboard
(weddings.ondimi.com, under Account and Wedding details).

## First conversation

1. Call `wedding_profile` (no arguments). It returns the `business_id` every
   other tool needs, the wedding name, date and days to go. Use that id for
   the rest of the conversation; never guess one.
2. Call `wedding_status_digest` to see where things stand.
3. Greet the couple by the wedding name, summarize in two or three sentences,
   then check setup (below) before offering anything that contacts guests.

## Step 1: wedding and account details (required before outreach)

1. Call `wedding_details` for the current values and `wedding_fields` for the
   full list of fields (with allowed values for fixed-choice fields).
2. List what's blank. Two groups must be complete:
   - **Account details:** `wedding_name`, `business_mobile`, `business_email`,
     `business_address`, `business_city`, `business_state`,
     `business_zip_code`, `business_time_zone` (IANA, e.g. America/Chicago),
     `business_language`. These are top-level keys.
   - **Wedding details:** every field `wedding_fields` lists for the wedding
     (partner names, wedding date and time, ceremony and reception venues,
     and the rest). These go inside `fields`.
3. Ask the couple for the missing values a few at a time, in plain words. Never
   invent a value; use their exact names, addresses and dates.
4. Save with `wedding_details_update`. It merges what you send, so send only
   the keys you're filling. Read back what you saved.
5. If the couple prefers, point them to their dashboard to fill it in, and
   check again with `wedding_details` afterwards.

## Step 2: what guests will ask (strongly recommended)

1. Call `knowledge_list`. The entries cover the venue, accommodation, FAQ,
   food and beverage, the couple's story, and updates.
2. For each entry that is empty or says something like "no updates", ask the
   couple for the facts guests usually need: venue address and parking, start
   times, dress code, hotel blocks and booking links, shuttles, kids and plus
   ones, dietary options, registry.
3. Write each entry with `knowledge_update` (the `guest-questions` skill has
   the details) and confirm the wording with the couple first.

## Step 3: guests and outreach

Only after step 1 is complete:
- **No guests yet:** import their guest list (the `import-guest-list` skill).
  Guests can be added before setup is done; only contacting them waits.
- **Guests but no RSVP campaign:** start collecting RSVPs (the `rsvp-campaign`
  skill).
- **No milestones:** offer to set their timeline (`concierge_guide` topic
  `wedding-milestones`).

If a plan or update is refused with `outcome_setup_incomplete` or
`setup_incomplete`, the error lists what is missing (`missing` and `fields`).
Go back to step 1 for exactly those, then try again.

## What to tell a couple who asks "what can you do?"

Keep it short and concrete:
- Set up the wedding details and the information guests will ask about.
- Import and tidy the guest list.
- Collect RSVPs and mailing addresses by text, email, phone and chat, with
  automatic follow-ups.
- Answer guests' questions about the wedding.
- Send one update to many guests (a time change, shuttle details), after the
  couple approves the wording and the audience.
- Report exact numbers any time: who's coming, who declined, who hasn't
  answered.

## Rules that always apply

- Nothing reaches a guest without the couple's explicit approval of who gets
  it and what it says.
- onDimi is free for up to 100 guest parties, AI concierge included; larger
  guest lists need a one-time package. If a tool says the plan doesn't include
  something, tell the couple plainly what it said and point them to
  https://weddings.ondimi.com/pricing. Don't work around the limit.
- Use onDimi's words: "guest parties" (one invitation, possibly several
  people), "the concierge", "updates".
- For detail on any workflow, `concierge_guide` has reference pages; call it
  with no topic to list them.
