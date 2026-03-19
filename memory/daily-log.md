# Daily Log

_Newest first. Updated after each session._

---

## 2026-03-19

### Session 3 — Applications + System Improvements
- **Hit 15 applications for the day:**
  - Whatnot Buyer Growth, Whatnot AI Dev Tools, Whatnot Discovery (Search), Whatnot Discovery (Feed), ActBlue SWE II, Teamworks SE II, Stable Product Engineer (YC)
- Built **writing voice profile** (`memory/writing-voice.md`) — analyzed 12+ sent emails to capture Sia's tone for future cover letters
- Wrote ActBlue cover letter + application answer (saved to `outputs/job-apply/actblue-swe-ii.md`)
- Wrote Teamworks "Why do you want to work here?" answer
- Wrote Stable YC outreach message to Michael
- Created **`/now` command** — mid-day ADHD-friendly check-in: done/remaining/calendar/email/texts reminder
- Updated CLAUDE.md: added MCP integrations (working), `/now` command, file structure with new subfolders
- Discovered active interviews from email scan: FanDuel (phone screen), Machina Cognita (Monday), Gyde Health (Apr 6)

### Session 2 — Job Search + Cleanup
- **Google Jobs Email MCP** now working — confirmed 5 application receipt emails (BlackLine x2, Dandy, Whatnot, Twilio)
- Found 2 new roles: **Teamworks** SE II Full Stack ($166K, Python/React/TS/PostgreSQL/GraphQL — near-perfect match) and **Stable** Product Engineer ($160K–$220K, React/TS/GraphQL/AWS, YC-backed)
- Dropbox DocSend — confirmed gone, removed from all tracking
- Consolidated job search files into single `outputs/job-search.md`, deleted old split files
- Created `outputs/interview-prep/` and `outputs/job-apply/` subfolders, updated commands to use them

### Session 1 — Applications + MCP Setup
- Launched assistant system — tested /start, /wrap, /job-apply, commands working
- Reframed Joulea in projects.md as interview study project (not work tracking)
- Applied to **10 jobs** total:
  - Affirm — SE II Backend (Credit Decisioning)
  - Affirm — SE II Backend (Identity Decisioning)
  - Snap Inc. — Full Stack Spectacles L4
  - AMP — SWE Cloud
  - Dropbox — Full Stack Dash Experiences
  - Twilio — SWE L2
  - Dropbox — Simplify Sharing
  - Whatnot — SWE Merchant Tooling
  - Dandy — SE II 3D/CAD
  - BlackLine — Software Engineer
- Generated tailored cover letters for AMP, Dropbox Dash, Dandy
- Skipped Affirm AI Agents (Canada only)

### Decisions
- Multi-apply strategy at Affirm works — applied to 2 teams, pipeline is independent per team
- Canada-only roles = skip unless visa sponsorship explicitly offered
- Going in at $135K on AMP (top of realistic range given band is $130–152K)

### MCP Server Setup (Late Night Prior)
- Fixed **Playwright** MCP — now using `@playwright/mcp@latest` — working
- Replaced **Apple Reminders** with **Apple Notes** (`mcp-apple-notes`) — working
- **Google jobs email** MCP — now working and confirmed

### Remaining Today
- Apply to 5 more (Whatnot x2, ActBlue, Teamworks, Stable)
- LeetCode: minimum 1.5 hrs
- System Design: minimum 1–2 hrs
- Joulea stack deep-dive: start with IoT pipeline architecture

---

## 2026-03-18

### Done
- Scaffolded personal assistant system at ~/Desktop/assistant
- Set up memory files, slash commands, CLAUDE.md constitution
- Moved existing commands from ~/.claude/commands/ into project

### Decisions
- Using memory/private/ (gitignored) for sensitive data (job search, trading)
- Assistant role: personal chief of staff, not coding assistant
- Commands live at project level (.claude/commands/), not user level

### Tomorrow
- Test all slash commands
- Start populating daily workflow with /start and /wrap
- Configure Gmail/Calendar MCPs when ready
