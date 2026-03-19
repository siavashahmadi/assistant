# Sia's Personal Assistant

A Claude Code-powered personal chief of staff system. Not a coding assistant — a life/career/productivity orchestrator that maintains context across conversations.

## How It Works

Open this directory in Claude Code. The `CLAUDE.md` constitution loads automatically, and the assistant reads your memory files to pick up where you left off.

```bash
cd ~/Desktop/assistant
claude
```

## Commands

| Command | What it does |
|---------|-------------|
| `/start` | Morning kickoff — loads all context, surfaces priorities |
| `/wrap` | End-of-day — summarizes, updates logs, plans tomorrow |
| `/brain-dump` | Organizes stream of consciousness into Do/Decide/Explore/Let Go |
| `/job-apply [company — role]` | Tailors an application with fit analysis and cover letter angle |
| `/job-search [keywords]` | Finds matching jobs, analyzes fit, updates pipeline |
| `/interview-prep [company]` | Full interview prep: research, STAR answers, technical Qs |
| `/project-status [name]` | Deep dive on a project's current state and next steps |
| `/learn [topic]` | ADHD-friendly structured learning plan |
| `/explain-like-im-building [concept]` | Learn by designing a small buildable project |
| `/unstuck` | One question, one next step. Breaks paralysis. |
| `/trading-log [details]` | Log trades/sessions, track patterns and emotions |

## File Structure

```
CLAUDE.md                  — Constitution (read on every startup)
memory/
  me.md                    — Identity, preferences, current situation
  resume.md                — Full resume text
  projects.md              — Active projects and status
  daily-log.md             — Running log (newest first)
  learnings.md             — How Sia works best
  private/                 — Gitignored sensitive data
    job-search.md          — Job pipeline and applications
    trading-log.md         — Trade journal
outputs/                   — Generated artifacts (prep docs, plans)
.claude/commands/          — Slash commands
```

## Adding New Commands

Create a `.md` file in `.claude/commands/` with this format:

```markdown
---
description: Short description shown in command list
argument-hint: [optional args]
allowed-tools: Read, Write, Edit, ...
model: sonnet
---

Your prompt here. Use $ARGUMENTS to reference command arguments.
Reference memory files with relative paths like `memory/me.md`.
```

## Memory System

Memory files are read at the start of each session and updated after substantive work. The assistant proactively keeps them current — you don't need to ask.

`memory/private/` is gitignored for sensitive data (job search pipeline, trading journal).
