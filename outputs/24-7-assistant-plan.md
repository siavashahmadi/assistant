# 24/7 Assistant Plan

## Architecture: Three Layers

### 1. Scheduled Tasks (Cron)
Claude Code has built-in scheduling via `CronCreate`.

Suggested schedule:
- **7-8 AM daily**: Run `/start`, create TODO, check email for interview invites
- **Every 4 hours (business hours)**: Quick email scan for recruiter replies
- **9-10 PM daily**: Run `/wrap`, update daily log, flag urgent items

Key details:
- Set `durable: true` so tasks persist across sessions (saved to `.claude/scheduled_tasks.json`)
- Tasks only fire while the REPL is idle (won't interrupt mid-conversation)
- Recurring tasks auto-expire after 7 days -- need periodic re-registration
- Each firing is lightweight (~2-3K tokens for an email check)

### 2. Event-Driven (Telegram/iMessage)
- Telegram and iMessage MCP channels already connected
- Text yourself a task from your phone, assistant picks it up when REPL is active
- Could set up a dedicated Telegram bot as "assistant inbox"
- No polling needed -- messages arrive as events

### 3. Remote Triggers
- `RemoteTrigger` can trigger prompts from outside the session (webhook, script, GitHub Action)
- Useful for: "new recruiter email? Trigger a summary"

---

## Infrastructure

**No VM or cloud machine needed.**

- Mac works fine with Claude Code running in a terminal tab
- For true 24/7 (laptop closed/away): install Claude Code on home server (Ubuntu/Docker), run in `tmux` or `screen` session
- Zero additional cost

---

## Token Budget (Estimated)

| Task | Frequency | Est. Tokens |
|------|-----------|-------------|
| Morning briefing (`/start`) | 1x/day | ~5-8K |
| Email scan | 3x/day | ~2-3K each |
| Evening wrap (`/wrap`) | 1x/day | ~5-8K |
| **Daily total** | -- | **~20-25K** |

Rule: keep scheduled prompts short and specific. Interactive sessions use 10-50x more than automated tasks.

---

## Rollout Phases

### Phase 1 (zero cost, set up anytime)
- Morning cron: `/start` at 8 AM
- Evening cron: `/wrap` at 10 PM
- Email check cron: every 4 hours during business hours

### Phase 2 (mobile access)
- Telegram bot as "assistant inbox" -- text tasks from phone
- Move Claude Code to home server in tmux for true 24/7

### Phase 3 (stretch)
- Remote triggers for specific events (emails from recruiters, calendar reminders)
- Auto-draft responses to recruiter emails for review
