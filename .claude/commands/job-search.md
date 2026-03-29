---
description: Search for jobs matching a role and analyze fit
argument-hint: [role or keywords]
allowed-tools: Read, Grep, Glob, WebSearch, WebFetch
model: sonnet
---

You are helping Sia search for jobs matching: **$ARGUMENTS**

## Step 1: Load Context
Read:
- `memory/me.md` — background, location, preferences
- `memory/resume.md` — full resume and key metrics
- `memory/private/application-tracker.md` — existing pipeline, strategy, and applications

## Step 2: Search

Use WebSearch to find current job postings matching "$ARGUMENTS". Search across:
- Make sure to skip roles in the application-tracker.md
- LinkedIn, Indeed, Glassdoor, Wellfound (AngelList), Lever/Greenhouse job boards and more you can find as well
- Always try to find the actual company website's career page of the listing
- Try multiple search queries to cast a wide net
- Focus on roles that match his ~5 years of experience (not entry-level, not staff+)

## Step 3: Analyze Top Results

For each promising role found (up to 5), provide:

| Field | Details |
|-------|---------|
| **Salary range** | If available from posting or levels.fyi |
| **Company** | Name + what they do (1 line) |
| **Role** | Title |

| **Link** | URL to apply |

| **Match Score** | use the *Rubrik below |
| **Resume Emphasis** | What to put at the forefront of the resume |
| **Why it fits** | Specific skill overlap (not generic) |
| **Gap** | What he'd need to brush up on |

Rubrik
Strong = 80%+ of listed requirements overlap with resume
Good = 60-80%, 
Stretch = below 60% or requires a level jump
Long Shot = you know what to do 

## Step 4: Strategy Recommendations

- Which 2-3 roles are the best fit and why
- Any skills gaps that keep appearing (things worth learning)
- Suggested resume bullet emphasis for these types of roles (reference his actual bullets from resume.md)

## Step 5: Save to Today's TODO
Add the roles to today's TODO file (`todos/YYYY-MM-DD.md`) under a `## Job Apps to Apply` section. If the file doesn't exist yet, create it. Use a compact table format:

```
| # | Company | Role | Salary | Match | Link |
```

## Step 6: Update Pipeline
Add the roles to `memory/private/application-tracker.md` and update accordingly.

## Rules
- Keep it actionable. No fluff.
- Match scores should be honest — "Stretch" is fine, just explain the gap.
