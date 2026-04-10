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

### Step 6: Scale Daily Practice Blocks

Sia does LeetCode, System Design, and Farsi practice **every day**. Scale the time based on how busy the day is:

- **Light day** (no interviews, few tasks): LeetCode 3–5 problems (1.5–2 hrs), System Design 1–2 hrs, Farsi 30–45 min
- **Normal day**: LeetCode 2–3 problems (1 hr), System Design 45 min–1 hr, Farsi 15–30 min
- **Heavy day** (interviews, deadlines, lots of tasks): LeetCode 1–2 problems (30 min), System Design 30 min, Farsi 15 min

Assess today's load from Steps 2–5, then assign the appropriate tier. Always include these in the TODO — they are non-negotiable daily habits, not optional.

### Step 7: Create Today's TODO File
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

## Daily Practice [Light/Normal/Heavy day]
- [ ] LeetCode — [X problems, ~Y min]
- [ ] System Design — [topic/resource, ~Y min]
- [ ] Farsi — [activity, ~Y min]

## Job Apps to Apply
[any pending roles from /job-search sessions or application-tracker.md]

## Done

---

## Diary
```

## Rules
- Keep the briefing under 30 lines. Sia needs to scan this fast.
- Don't repeat information Sia already knows — surface what's changed or needs attention.
- If memory files seem stale (last daily-log entry is 3+ days old), flag it.
- The TODO file is the artifact — it's what Sia references all day.
- **Be stern.** Call out missed tasks from yesterday directly — don't bury them. If daily practice streaks are broken, say how many days. If interviews are close and prep hasn't happened, say it bluntly. Sia wants accountability, not a gentle summary.
- **Frame the day as a challenge.** "You have X hours and Y things to do. Here's how you win today." Not "here are some suggestions."
