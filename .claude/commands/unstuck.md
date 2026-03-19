---
description: Get unblocked when you don't know what to do next
allowed-tools: Read, Grep, Glob, Bash(git:*)
model: sonnet
---

Sia is stuck. Help him get moving with minimal friction.

## Step 1: Load Context
Read:
- `memory/projects.md` — active projects and status
- `memory/daily-log.md` — recent activity and priorities

## Step 2: Scan Current State
Quickly assess:
- Check `git status` and recent `git log --oneline -10` in the current directory
- Look for any TODO/FIXME/HACK comments in recently modified files
- Check if there's a CLAUDE.md or README with project context
- Check for any failing builds or lint errors

## Step 3: Ask ONE Question
Based on what you found, ask Sia **one** clarifying question. Not five. One. Examples:
- "You have uncommitted changes in X — are you stuck on that, or something else?"
- "The last thing you worked on was Y — is that where you're blocked?"
- "No recent changes — what were you trying to start?"

## Step 4: Give ONE Next Step
After his answer, give him **one concrete, small action** to take right now. Not a plan. Not options. One thing.

Format:
> **Do this now:** [specific action, < 15 minutes]
>
> **Why:** [one sentence explaining why this unblocks things]

## Rules
- Do NOT give a list of 10 suggestions. That makes the paralysis worse.
- Do NOT ask what his goals are or what he's working on broadly. Stay narrow.
- The step should be small enough to start in the next 60 seconds.
- If the block seems emotional (overwhelm, perfectionism, decision fatigue), acknowledge it briefly, then still give one concrete step.
