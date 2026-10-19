---
name: send-guest-update
description: Send one announcement to many wedding guests through onDimi. Use when the couple wants to tell guests about a change or logistics, such as a new ceremony time, a venue change, shuttle times, weather, parking, or a welcome note.
---

# Sending a guest update

An update carries one reason to many guests. It is not for collecting RSVPs
or addresses; those go through the `rsvp-campaign` skill.

## Before you start

Updates go out only once the wedding's account details and wedding details are
complete. If a step is refused with `setup_incomplete` or
`outcome_setup_incomplete`, finish setup with the `getting-started` skill
first; the error lists exactly what is missing.

## Steps

1. **Write the note with the couple.** One reason per update. Use their facts
   exactly (times, places); ask if anything is missing.
2. **Draft and sample.** Call `guest_update_draft` with `business_id`, the
   couple's note as `draft`, and `sample_customer_id` set to one real guest
   (from `guest_list`). It returns the sample message that guest would get,
   SMS length, and an `update_id`. Nothing is sent.
   - Show the sample to the couple word for word, and say each guest gets
     their own personalized wording of the same note.
   - If the couple wants changes, call `guest_update_draft` again with the
     new note and the same `update_id`.
   - `refused` means the wording was rejected; rework it with the couple.
   - `too_many_drafts` lists unsent drafts; reword one by its `update_id`.
3. **Agree the audience.** Ask who should get it if they haven't said:
   everyone attending, a named group, specific guests. Look the guests up with
   `guest_list` (filters: `rsvp=attending`, `q=` for names) and state the
   count back: "This goes to 116 attending guest parties."
4. **Get an explicit yes** to both the sample wording and the audience. If
   either changed since the last yes, ask again.
5. **Send.** `guest_update_send` with `business_id`,
   `conversation_id` = the `update_id`, and `customer_ids` = the agreed list.
   Guests without a mobile number or who opted out of texts are skipped and
   listed; report them.
6. **Report and track.** Say how many were queued and skipped.
   `guest_updates_list` with the `update_id` shows delivery as it happens.

## Never

- Send without the couple's approval of the exact sample and audience.
- Pick the audience yourself from vague wording ("the people who need it").
- Use an update to chase RSVPs or addresses.
