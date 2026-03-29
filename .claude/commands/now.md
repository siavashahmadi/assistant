---
description: Mid-day check-in — what's done, what's left, what's next
allowed-tools: Read, mcp__google-jobs-email__calendar_get_events, mcp__google-jobs-email__query_gmail_emails
model: opus
---

Sia needs a quick mid-day status check. Be concise — he has ADHD and needs clarity, not a wall of text.

## Step 1: Load Today's State
Read:
- `todos/` — find today's TODO file (YYYY-MM-DD.md), extract what's done and what's remaining
- `memory/daily-log.md` — supplementary context if needed

## Step 2: Check Calendar
Use `calendar_get_events` to pull today's remaining events and tomorrow's events. Flag anything in the next 2 hours as urgent.

## Step 3: Check Email (quick scan)
Use `query_gmail_emails` to check for any emails from today that look like they need a reply — interview invites, recruiter responses, time-sensitive stuff. Don't list every confirmation email.

## Step 4: Output

Format the response EXACTLY like this:

### Done Today
- [bulleted list of completed items]

### Remaining
- [ ] [unchecked items from daily log, ordered by priority]

### Calendar
- [today's remaining events with times]
- [tomorrow's first event as a heads-up]

### Needs Attention
- [any emails that need replies]
- [any calendar conflicts]

### Next Action
> [ONE specific thing to do right now — the single most important or time-sensitive task]

### Reminders
- Check your texts
- [any other recurring reminders from daily log like study blocks, Farsi practice, etc.]

## Step 5: Update Today's TODO
After presenting the check-in, update `todos/YYYY-MM-DD.md`:
- Check off completed items (`- [x]`)
- Add any new items that came up
- Move completed items to the `## Done` section

## Rules
- Keep the ENTIRE output under 40 lines. This is a glance, not a briefing.
- Bold anything time-sensitive.
- If nothing is urgent, say so — don't manufacture urgency.
- Always end with "Check your texts" — Sia needs this reminder.
- Always update the TODO file — it's the persistent artifact.
