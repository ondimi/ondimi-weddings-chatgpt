---
name: rsvp-follow-up
description: Ask the couple's own wedding guests for their RSVP or mailing address through onDimi's reminder plans. Use when the couple wants to ask guests for an RSVP, remind guests who haven't replied, or collect mailing addresses.
---

# Collecting RSVPs and addresses

RSVPs, mailing addresses and other details are collected by **plans**. A plan
is a reminder plan the wedding already has for one purpose (RSVP, mailing
address). The couple starts it for guest parties they choose from their own
guest list. For each of those parties the plan sends a few reminders at set
times, one step at a time: a text, an email or, if calls are on for that
guest, a phone call (or voicemail) that opens by announcing onDimi as the
couple's AI guest concierge. It stops for a party as soon as the plan's
answer (the RSVP or the address) is in, or when the guest replies STOP.

A plan reaches only guests registered in the couple's wedding, and only on
the channels switched on for each guest. An update is not a substitute: it
doesn't collect answers.

## Before you start

onDimi contacts no guest until the wedding's account details and wedding
details are complete, and the concierge answers guests only from the wedding's
knowledge. If either looks unfinished (`wedding_details`, `knowledge_list`), or
a step below is refused with `outcome_setup_incomplete`, complete setup first
with the `getting-started` skill (steps 1 and 2), then come back.

## Steps

1. **Find the plan.** `plan_available` lists the wedding's plans with their
   `journey_id`. Pick the one that matches the goal (RSVP, collect addresses).
   If none matches, tell the couple; don't improvise with an update.
2. **Review who's ready.** `plan_preflight` with `compact=true` for that plan
   returns the guest parties ready to enroll, each with a
   `review_fingerprint`, plus those skipped and why. Page with offset/limit
   when the list is long.
3. **Show the couple and get a clear yes.** Say which parties will be
   contacted, on which channels, starting when (messages go out in each
   guest's local time, by default 8am–9pm). Name the parties, or a few of them when
   there are many. If they want to leave anyone out, leave them out.
4. **Start the plan for those parties.** `plan_enroll_guests` with
   `business_id`, `plan_id`, `journey_id` and
   `guests=[{customer_id, review_fingerprint}]` for the
   approved parties, up to 25 per call. Send any ids returned as
   `not_processed` in the next call. "Already enrolled" skips are normal.
5. **Confirm what happened:** how many enrolled, how many skipped and why,
   when the first messages go out. `plan_status` and `wedding_status_digest`
   show progress later.

## Reminders and another round

- The plan sends its reminders on its own and stops for a guest once they
  answer.
- Guests whose plan ran out without an answer show as `unanswered` in
  `plan_status` and as `unanswered_rechase` in `plan_preflight`. Once the
  last message is 3+ days old, they can be enrolled again in the same plan,
  up to 3 rounds. After that, suggest the couple reach out personally.
- If a guest answered by phone or in person, record it with `guest_edit`
  (the full `party_members` array with each member's status), or mark the
  plan done for them with `plan_guest_status_set`.

## Pausing and stopping

- `guest_messages_pause_resume` (`action: "pause"` / `"resume"`) holds or
  restarts one guest's scheduled messages.
- `guest_messages_cancel` cancels a guest's remaining scheduled messages
  (for example after they decline). Confirm with the couple first.
