# onDimi Weddings for ChatGPT

Run your wedding's guest communication by talking to ChatGPT. onDimi is an AI
guest concierge that texts, emails, calls and chats with every guest party for
you; this plugin lets ChatGPT steer it.

## What you can ask

- "How are our RSVPs looking?"
- "Who hasn't replied yet?"
- "Here's our guest list" (paste it or attach the spreadsheet)
- "Tell our attending guests the ceremony now starts at 4:30"
- "Add the shuttle times to our venue information"

## Getting started

1. Install **onDimi Weddings** from the ChatGPT plugin directory.
2. Sign in to onDimi when asked, or create your wedding in the sign-in window.
   It's free for up to 100 guest parties, AI concierge included.
3. Ask: "Let's set up our wedding."

Nothing reaches a guest until you approve it.

## What's included

- **MCP server:** `https://api.ondimi.com/couples/mcp` (OAuth sign-in).
- **Skills:** getting started, guest lookup, guest questions, guest-list
  import, RSVP and address campaigns, guest updates, and wedding status.

## Data and privacy

Your wedding data goes between ChatGPT and api.ondimi.com over HTTPS. The
connection sees only your wedding. Disconnect any time from ChatGPT's plugin
settings; changing your onDimi password also disconnects every assistant.

- [Privacy Policy](https://weddings.ondimi.com/privacy-policy)
- [Terms](https://weddings.ondimi.com/terms-and-conditions)

## Support

weddings@ondimi.com · https://weddings.ondimi.com/contact

## Building the submission package

```
python scripts/build_zip.py
```

Writes `dist/ondimi-weddings-<version>.zip` from the tracked files
(`plugin.json`, `mcp.json`, `skills/`, `assets/`, `README.md`, `LICENSE`).
