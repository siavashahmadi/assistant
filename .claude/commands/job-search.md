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
- `memory/private/job-search.md` — existing pipeline and strategy

## Step 2: Search

Use WebSearch to find current job postings matching "$ARGUMENTS". Search across:
- LinkedIn, Indeed, Glassdoor, Wellfound (AngelList), Lever/Greenhouse job boards
- Try multiple search queries to cast a wide net
- Focus on roles that match his ~5 years of experience (not entry-level, not staff+)

## Step 3: Analyze Top Results

For each promising role found (up to 8), provide:

| Field | Details |
|-------|---------|
| **Company** | Name + what they do (1 line) |
| **Role** | Title |
| **Link** | URL to apply |
| **Match Score** | Strong / Good / Stretch |
| **Why it fits** | Specific skill overlap (not generic) |
| **Gap** | What he'd need to brush up on |
| **Salary range** | If available from posting or levels.fyi |

## Step 4: Strategy Recommendations

- Which 2-3 roles are the best fit and why
- Any skills gaps that keep appearing (things worth learning)
- Suggested resume bullet emphasis for these types of roles (reference his actual bullets from resume.md)

## Step 5: Save Output
Save results to `outputs/job-search-[query-slug].md`

## Step 6: Update Pipeline
Ask Sia which roles to add to `memory/private/job-search.md` and update accordingly.

## Rules
- Keep it actionable. No fluff.
- Match scores should be honest — "Stretch" is fine, just explain the gap.
