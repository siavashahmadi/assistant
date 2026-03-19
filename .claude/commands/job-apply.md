---
description: Tailor an application for a specific company/role
argument-hint: [company — role]
allowed-tools: Read, Write, Edit, WebSearch, WebFetch, Agent
model: opus
---

Sia wants to apply to **$ARGUMENTS**. Help him tailor a strong application.

## Step 1: Load Context
Read:
- `memory/resume.md` — full resume
- `memory/me.md` — background and preferences
- `memory/private/job-search.md` — existing pipeline and strategy

## Step 2: Research the Role
Use WebSearch to find:
- The actual job posting (requirements, responsibilities, tech stack)
- Company info (what they do, stage, culture, recent news)
- Salary data from levels.fyi or the posting itself

## Step 3: Fit Analysis
Map Sia's experience to the role's requirements:

| Requirement | Sia's Match | Evidence |
|-------------|-------------|----------|
| [From posting] | Strong/Good/Gap | [Specific bullet from resume] |

## Step 4: Application Tailoring

### Resume Bullet Emphasis
Which existing bullets to lead with for this specific role. Reference the "Key Metrics for Applications" section in resume.md.

### Cover Letter Angle (if needed)
Draft a 3-paragraph cover letter angle:
1. Hook — why this company specifically (not generic)
2. Fit — 2-3 strongest experience matches with numbers
3. Close — what excites him about the role

### Application Notes
Any role-specific tips: keywords to include, things to emphasize, red flags to address.

## Step 5: Log It
Update `memory/private/job-search.md` with:
- Company, role, salary range, match score, status: "Applied [date]"

## Step 6: Save Output
Save the full prep to `outputs/job-apply/[company-slug].md`

## Rules
- Be specific, not generic. Reference actual job requirements.
- Don't oversell — if there's a gap, acknowledge it and frame growth potential.
- Keep the cover letter angle authentic to Sia's voice (direct, technical, genuine).
