---
description: Log a trade or trading session
argument-hint: [trade details or "review"]
allowed-tools: Read, Write, Edit
model: sonnet
---

Sia wants to log a trading session. Input: **$ARGUMENTS**

## Step 1: Load Context
Read:
- `memory/private/trading-log.md` — existing trade history and patterns

## Step 2: Capture the Session

If Sia provided trade details in the argument, parse them. Otherwise, ask:

1. **What did you trade?** (MES, direction, contracts)
2. **Entry & exit** (price, time)
3. **P/L** (points or dollars)
4. **Setup** — what was the rationale for entering?
5. **Emotions** — how did you feel before, during, after?
6. **Mistakes** — anything you'd do differently?

## Step 3: Log the Entry

Append to `memory/private/trading-log.md` in this format:

```
## [Date] — [Session Type]

**Market Context:**
- [S&P level, trend, any news]

**Trades:**
| # | Direction | Entry | Exit | P/L | Hold Time |
|---|-----------|-------|------|-----|-----------|
| 1 | ... | ... | ... | ... | ... |

**Rationale:** ...
**Emotions:** ...
**Mistakes:** ...
**Lessons:** ...
```

## Step 4: Pattern Check

If there are 3+ logged sessions, briefly note:
- Recurring mistakes
- Improving patterns
- Emotional tendencies (revenge trading, FOMO, discipline)

## If argument is "review"
Instead of logging a new trade, analyze the existing trading log:
- Win rate, average P/L
- Most common mistakes
- Emotional patterns
- Suggestions for improvement

## Rules
- No judgment on losses. Frame everything as data.
- Keep the log clean and consistent so it's useful for review.
- The private/ directory is gitignored — this stays confidential.
