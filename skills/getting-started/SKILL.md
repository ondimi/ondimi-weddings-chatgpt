---
name: getting-started
description: First steps with onDimi, including the wedding setup that must be done before any guest can be contacted. Use when the couple has just connected onDimi, asks what onDimi can do, says they are new, or when their wedding has missing details, no knowledge, or no guests yet.
---

# Getting started with onDimi

onDimi manages one wedding's guest list and keeps its guests informed. The
couple adds their own invited guests, and onDimi's AI guest concierge contacts
only those guests: to collect RSVPs, mailing addresses and other details, to
answer their questions from the wedding's information, and to deliver the
updates the couple approves. Each guest is contacted only on the channels
switched on for that guest (text, email or phone call); the couple confirmed at
sign-up that their guests agreed to this, and a guest's STOP turns all of them
off. Every call, including a voicemail, opens by announcing the caller: "it's onDimi, the AI guest concierge of <the couple>". You help
the couple steer it.

**Setup comes first.** onDimi refuses to contact any guest (plans and updates
alike) until the wedding's account details and wedding details are complete.
The wedding information (knowledge) isn't enforced, but without it the
concierge can't answer guests' questions. Get both done before any guest is
contacted. The couple can fill them in here with you, or on their onDimi
dashboard (weddings.ondimi.com, under Account and Wedding details).

## First conversation

1. Call `wedding_profile` (no arguments). It returns the `business_id` every
   other tool needs, the wedding name, date and days to go. Use that id for
   the rest of the conversation; never guess one.
2. Call `wedding_status_digest` to see where things stand.
3. Greet the couple by the wedding name, summarize in two or three sentences,
   then check setup (below) before offering anything that contacts guests.

## Step 1: wedding and account details (required before guests are contacted)

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

## Step 3: guests, RSVPs and addresses

Only after step 1 is complete:
- **No guests yet:** import their guest list (the `import-guest-list` skill).
  Guests can be added before setup is done; only contacting them waits.
- **Guests but no RSVPs requested yet:** start collecting RSVPs (the
  `rsvp-follow-up` skill).
- **No milestones:** offer to set their timeline (`concierge_guide` topic
  `wedding-milestones`).

If a plan or update is refused with `outcome_setup_incomplete` or
`setup_incomplete`, the error lists what is missing (`missing` and `fields`).
Go back to step 1 for exactly those, then try again.

## What to tell a couple who asks "what can you do?"

Keep it short and concrete:
- Set up the wedding details and the information guests will ask about.
- Import and tidy the guest list.
- Ask the guests the couple chooses for their RSVP or mailing address, with a
  few reminders that stop when the guest answers.
- Answer guests' questions about the wedding.
- Send the couple's guests an update (a time change, shuttle details), after
  the couple approves the wording and who gets it.
- Report exact numbers any time: who's coming, who declined, who hasn't
  answered.

## Rules that always apply

- Nothing reaches a guest without the couple's explicit approval of who gets
  it and what it says.
- Only guests on the couple's own guest list can be contacted, and only on
  the channels switched on for each guest. The tools that send take guest ids
  from that list, never a phone number or an email address.
- If a tool says the wedding's plan doesn't include something, tell the couple
  plainly what it said and point them to https://weddings.ondimi.com/pricing.
  Don't work around the limit.
- Use onDimi's words: "guest parties" (one invitation, possibly several
  people), "the concierge", "updates".
- For detail on any workflow, `concierge_guide` has reference pages; call it
  with no topic to list them.
