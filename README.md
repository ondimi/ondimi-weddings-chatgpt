# onDimi Weddings for ChatGPT

Manage your wedding guest list by talking to ChatGPT, and keep your guests
informed. You sign in to your own onDimi wedding; ChatGPT sees that wedding
and nothing else.

## Who onDimi contacts, and how

- **Only your guests.** onDimi contacts only the guests you added to your
  wedding's guest list. The tools that send take guests from that list, never
  a phone number or an email address, so nobody outside your guest list can be
  reached.
- **Only with consent.** When you sign up, you confirm that your guests agreed
  to receive wedding texts and phone calls from onDimi on your behalf. Each
  guest has a separate switch for texts, emails and phone calls; onDimi uses
  only the ones that are on, and you can turn any of them off. A guest who
  replies STOP is not contacted again on any channel.
- **Only what you approve.** You choose the guests and say yes before
  anything goes out. An update is shown to you as a sample first and is sent
  only after you approve the wording.
- **Why guests hear from onDimi:** to give their RSVP, to give their mailing
  address, to get an answer to a question about the wedding, or to receive an
  update from you (a new ceremony time, the shuttle schedule).
- **Reminders, one guest at a time.** When you ask a guest for an RSVP or an
  address, onDimi follows your wedding's reminder plan for that guest: a few
  reminders at set times, during the day in the guest's time zone, by text,
  email or, if calls are on for that guest, a phone call. The reminders stop
  as soon as that guest's RSVP or address is in.
- **Calls say who is calling.** Every call, including a voicemail, opens with
  "it's onDimi, the AI guest concierge of <the couple>".
- **Built for US weddings.**

## What you can ask

- "How are our RSVPs looking?"
- "Who hasn't replied yet?"
- "Here's our guest list" (paste it or attach the spreadsheet)
- "Tell our attending guests the ceremony now starts at 4:30"
- "Add the shuttle times to our venue information"

## Getting started

1. Install **onDimi Weddings** from the ChatGPT plugin directory.
2. Sign in to onDimi when asked, or create your wedding in the sign-in window.
   Creating a wedding doesn't contact any guests.
3. Ask: "Let's set up our wedding." ChatGPT fills in your wedding and account
   details, which are needed before onDimi contacts any guest, and the
   information guests will ask about (venue, times, hotels, FAQ).

Nothing reaches a guest until you approve it.

## What's included

- **MCP server:** `https://api.ondimi.com/couples/mcp` (OAuth sign-in).
- **Skills:** getting started, guest lookup, guest questions, guest-list
  import, RSVP and address follow-up, guest updates, and wedding status.

## Data and privacy

Your wedding data goes between ChatGPT and api.ondimi.com over HTTPS. The
connection sees only your wedding. Messages reach only your own guests, and
only after you approve them. Disconnect any time from ChatGPT's plugin
settings; changing your onDimi password also disconnects every assistant.

- [Privacy Policy](https://weddings.ondimi.com/privacy-policy)
- [Terms](https://weddings.ondimi.com/terms-and-conditions)

## Support

support@ondimi.com · https://weddings.ondimi.com/contact

## Building the submission package

```
python scripts/build_zip.py
```

Writes `dist/ondimi-weddings-<version>.zip` from the tracked files
(`plugin.json`, `mcp.json`, `skills/`, `assets/`, `README.md`, `LICENSE`).
