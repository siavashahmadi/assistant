---
description: Deep dive on a specific project's status
argument-hint: [project-name]
allowed-tools: Read, Write, Edit, Glob, Grep, Bash(git:*)
model: sonnet
---

Sia wants a status check on **$ARGUMENTS**.

## Step 1: Load Context
Read:
- `memory/projects.md` — current project info
- `memory/daily-log.md` — recent activity related to this project

## Step 2: Check Live State
If the project has a repo on disk, check:
- `git log --oneline -10` — recent commits
- `git status` — uncommitted work
- Look for TODO/FIXME in recently modified files
- Check for a README or CLAUDE.md in the project

## Step 3: Present Status

**[Project Name]**

- **What it is:** One-line description
- **Stack:** Technologies in use
- **Last activity:** When and what
- **Current state:** What's built, what works
- **Blockers:** Anything preventing progress
- **Next steps:** 1–3 concrete actions

## Step 4: Ask
Ask Sia: **"Want to work on any of these next steps right now?"**

## Step 5: Update Memory
Update `memory/projects.md` if anything has changed since last recorded.

## Rules
- Be factual, not optimistic. If progress is stalled, say so.
- Next steps should be small enough to start in one session.
- Don't suggest architectural overhauls unless asked.
