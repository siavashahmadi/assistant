---
description: Morning kickoff — read all context, surface priorities
allowed-tools: Read, Glob, Grep
model: sonnet
---

Good morning. Time to get Sia oriented for the day.

## Process

### Step 1: Load Context
Read all memory files:
- `memory/me.md`
- `memory/resume.md`
- `memory/projects.md`
- `memory/daily-log.md`
- `memory/learnings.md`
- `memory/private/application-tracker.md`

### Step 2: Check for Yesterday's TODO
Read `todos/` for yesterday's file (or most recent). Pull forward any unchecked items.

### Step 3: Summarize the Plate

Present a concise morning briefing:

**Active Projects** — Pull from `memory/projects.md`. For each, one line: status + next step.

**Yesterday's Carryover** — Unchecked items from yesterday's TODO file.

**Job Search** — Check `memory/private/application-tracker.md`. Any pending applications, follow-ups due, or interviews coming up?

**Open Loops** — Anything that's been sitting for 2+ days without progress.

### Step 4: Propose Today's Focus

Pick 1–3 things to focus on today. Use these criteria:
- What has a deadline?
- What's blocking other things?
- What would build the most momentum?

### Step 5: Calendar Check
- Pull today's calendar events
- Flag any meetings that need prep
- Check for important emails that need response

### Step 6: Create Today's TODO File
Write `todos/YYYY-MM-DD.md` with this structure:

```
# YYYY-MM-DD

## Today's Focus
1. [Thing] — why
2. [Thing] — why
3. [Thing] — why

## Tasks
- [ ] [carried over from yesterday]
- [ ] [new tasks]

## Job Apps to Apply
[any pending roles from /job-search sessions or application-tracker.md]

## Done
```

## Rules
- Keep the briefing under 30 lines. Sia needs to scan this fast.
- Don't repeat information Sia already knows — surface what's changed or needs attention.
- If memory files seem stale (last daily-log entry is 3+ days old), flag it.
- The TODO file is the artifact — it's what Sia references all day.
