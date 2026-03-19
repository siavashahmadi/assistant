---
description: Create a structured learning plan for any topic
argument-hint: [topic]
allowed-tools: Read, Write, Glob, WebSearch, WebFetch
model: sonnet
---

Create a structured, practical learning plan for Sia to learn: **$ARGUMENTS**

## Step 1: Load Context
Read:
- `memory/me.md` — stack, interests, learning style
- `memory/learnings.md` — how Sia works best

## Context
Sia is a software engineer (~5 years exp) who learns best by building. He works with React, TypeScript, Python, Flask, AWS, Supabase, and PostgreSQL. He has ADHD, so the plan needs to be:
- Broken into **small, completable chunks** (not multi-hour marathons)
- **Build-first** — each phase should produce something tangible
- **Progressive** — start with the minimum viable understanding, layer complexity

## Learning Plan Structure

### 1. TL;DR (2-3 sentences)
What is this, why does it matter, and where does it fit in the landscape?

### 2. Prerequisites Check
What does Sia already know that's relevant? What gap needs filling first?

### 3. Phases

Break into 3-5 phases. Each phase:

**Phase N: [Name]** (~estimated time)
- **Goal:** One clear sentence
- **Build:** A specific small project or feature to build
- **Resources:** 1-2 best resources (prefer docs, interactive tutorials, or short videos — not 40-hour courses)
- **Done when:** Concrete completion criteria

### 4. Project Ideas
2-3 project ideas that combine this topic with Sia's existing stack (React, Flask, Supabase, AWS).

### 5. Quick Reference
Key concepts, commands, or patterns to bookmark — the "cheat sheet" version.

## After generating the plan

Ask Sia if he wants to save this plan. If yes, save it to `outputs/learn-[topic-slug].md`.
