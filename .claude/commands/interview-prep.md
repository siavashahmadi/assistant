---
description: Prepare for a job interview at a specific company
argument-hint: [company-name]
allowed-tools: Read, Grep, Glob, WebSearch, WebFetch, Agent
model: opus
---

You are helping Sia prepare for a job interview at **$ARGUMENTS**.

## Step 1: Load Context
Read:
- `memory/resume.md` — full resume and key metrics
- `memory/me.md` — background, stack, preferences
- `memory/private/application-tracker.md` — existing pipeline info on this company

## Step 2: Research the Company

Use WebSearch and WebFetch to research $ARGUMENTS:
- What the company does, their product/tech stack
- Recent news, funding, acquisitions
- Engineering blog posts or tech talks (what they value technically)
- Glassdoor/interview experience threads for engineering roles
- Company culture and values

## Step 3: Generate Interview Prep

### A. Company-Specific Talking Points
Map Sia's experience directly to what $ARGUMENTS cares about. Be specific — not generic.

### B. "Why $ARGUMENTS?" Answer
Draft a genuine, specific answer based on the research. Not generic fluff.

### C. Behavioral Questions (STAR Format)
Generate 5 behavioral questions likely asked at $ARGUMENTS, with STAR-format answer outlines using Sia's real experience:
- Pick stories from Joulea (IoT data pipeline, 3D visualization, RAG chatbot, microservices) and T-Mobile (legacy system integration, scale, cross-team)
- Each answer should have: Situation, Task, Action, Result with concrete numbers

### D. Technical Questions
Generate 5-8 technical questions based on:
- $ARGUMENTS's known tech stack
- Sia's experience overlap
- Include system design, coding, and architecture questions

### E. Questions to Ask Them
Generate 5 thoughtful questions Sia should ask, based on the research. Not generic "what's the culture like" — specific to what was found about $ARGUMENTS. Sia always likes to ask what's your least favorite thing about working at this company?

## Step 4: Save Output
Save everything to `outputs/interview-prep/[company-slug].md`

## Rules
- Present everything in a clean, scannable format. Bold key points.
- This is study material — make it easy to review quickly before an interview.
- Reference specific resume bullets, not vague summaries.
