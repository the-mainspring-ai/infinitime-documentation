---
title: "Creating a new policy"
description: ""
---

# Creating a New Policy

## 1. Create a New Policy

**Objective:** Establish the policy "container" that ties together settings for tenure, pay cycle, breaks, overtime, schedules, and more.

### What to do:

- Navigate to Company → Setup → Policies and click Insert
- Give it a **Name** that clearly describes this employee group (e.g. "Full Time New Hires")
- Assign a **Class** (e.g. "Full Time")—this lets you group similar policies together
- _(Optional)_ Pick a **Default Class** so that if an employee outgrows this policy, InfiniTime can fall back to another set of tenure rules

### Why it matters:

- Every employee is tied to exactly one policy
- Classes let you chain policies by tenure (e.g. new‑hire → regular)

### Example tenure setup:

| Policy Name         | Class     | Min Tenure (yrs) | Max Tenure (yrs) |
| ------------------- | --------- | ---------------- | ---------------- |
| Full Time New Hires | Full Time | 0                | 1                |
| Full Time Employees | Full Time | 1                | 99               |

## 2. Configure General Settings

**Objective:** Define the foundational rules for who's in the policy and when they move on.

### Key fields:

- **Min/Max Tenure:** Auto‑move employees after X years
- **Do Not Allow Breaks:** Hide break punch options if your org never tracks breaks

### When to skip:

If your employees all share the same break, overtime, and schedule rules regardless of tenure, you can leave the tenure grid at its default or skip it entirely.

### Tip:

Tenure ranges must cover 0–99 yrs without gaps—InfiniTime won't know where to put someone if there's a gap.

## 3. Define Your Pay Cycle

**Objective:** Tell InfiniTime how your organization's pay periods roll.

### Fields to set:

- **Start of Week:** (e.g. Monday) affects "Last Week"/"This Week" reports
- **Pay Cycle Type:** Weekly / Bi‑Weekly / Semi‑Monthly / Custom
- **Current Pay Period From:** Anchor date for auto‑calculating current/last pay periods
- **Split Punches At:** (overnight split) where an overnight shift should be split between periods
- **Edit Lockout:** # days + time after a pay period ends when it becomes uneditable

### Why it matters:

- Ensures "This Pay Period" and "Last Pay Period" always stay fresh
- Edit‑lockout prevents late changes that can throw off payroll

### Example:

- Pay cycle: weekly, starts Monday
- Current period from 2025‑04‑07
- Split at midnight or 2:00 AM for night shift
- Lock out edits 5 days after period end at 8 AM

## 4. Build Your Break Rules

**Objective:** Configure whether breaks are punched, auto‑applied, or both—and cap/minimum them.

### 4.1 Change‑to‑Break (punch‑in/out tracked)

**Use if:** Employees punch for lunch/coffee.

#### Key settings:

- **First Change If < X hrs →** Paid or Unpaid Break
- **Second Change If < Y hrs →** Paid or Unpaid Break

#### Example:

First less than 0.33 hr→ Paid, Second less than 1 hr→ Unpaid

### 4.2 Auto‑Breaks (no break punches)

**Use if:** You want to deduct breaks automatically.

#### Key settings:

- **First Auto Break if > X hrs →** Y hr Paid/Unpaid
- **"Only on Days with a Schedule"** if you only want auto breaks on scheduled days

#### Example:

After 6 hrs worked → auto‑deduct 0.5 hr unpaid

### 4.3 Break Limits

**Purpose:** Enforce min/max per break and daily max.

#### Key fields:

- **If Break > A and < B →** min C / max D
- **Max Daily Break:** cap total paid break per day

#### Example:

Paid breaks between .01–.33 hr: min .01 / max .25; daily max .5

## 5. Tame Overtime

**Objective:** Define when and how OT kicks in, map special cases, and set pay multipliers.

### 5.1 Basic Buckets

- **OT1:** Daily if >8 hr; weekly if >40 hr
- **OT2–OT4:** Additional buckets for double‑time, weekend, etc

#### Pay Method:

- **Amount:** +$X/hr on top of base
- **Percent:** +Y% of base (e.g. 50% = time‑and‑a‑half)
- **Rate:** Fixed $/hr (ignores base)

### 5.2 Advanced Cases

- **Deduct Daily from Weekly:** California style—don't double‑count daily OT toward weekly
- **Consecutive‑Day OT:** After N straight days → all hours on next day become OT; map to chosen bucket
- **Day‑of‑Week OT:** e.g. any Saturday/Sunday hour → OT2

## 6. Schedule & Rounding

**Objective:** Tie punches to schedules, round times for consistency, and optionally lock out off‑schedule punches.

### 6.1 Default Schedule

Create a "policy schedule" template via Quick Schedule—everyone on this policy inherits it unless overridden per employee.

### 6.2 Unscheduled Rounding

**When:** Punches outside scheduled grace periods.

**How:** Round to nearest .1, .25, or .5 hr at punch, pair, or daily level (7/8 split by default).

### 6.3 Scheduled Rounding & Lockout

#### Grace Periods (in minutes):

- **Early →** marks "Early" exception
- **On‑Time →** within window, no exception
- **Late →** still "On‑Time," no exception

- **Round to Schedule:** Snap qualifying punches to exact schedule start/end
- **Punch‑to‑Schedule Lockout:** Block any clock‑in/out outside those grace windows

### 6.4 Auto‑Punch

- **Auto Clock In/Out:** Automatically insert daily punches at schedule start/end—great for salary or "always on" teams
- **Auto Punch to Schedule:** Let InfiniTime insert break punches or switch departments/jobs per the schedule's Gantt chart

## 7. Exceptions & Notifications

**Objective:** Track no‑shows, tardiness, missing breaks, DOT rules, accrual breaches, and alert the right people.

### Scope:

- Company‑wide vs. individual policy
- Policy‑based overrides company defaults

### Popular types:

- **Absent:** scheduled but no clock‑in
- **Tardy/Early:** outside On‑Time grace
- **Missing Break:** >X hrs without a break
- **DOT violations:** HOS thresholds & approaching warnings
- **Accrual:** approaching or exceeding time‑off balances
- **Excessive hours:** daily/weekly pay period thresholds

### Alerts:

Email and/or SMS to employee or supervisor within X days.

## 8. Assign Shift Differentials

**Objective:** Layer on premiums for evenings, nights, weekends, etc.

1. Define shifts under Lookups → Scheduling Setup → Shifts, splitting any that cross midnight
2. On your policy's Shift Differentials tab, Insert each differential:
   - Pick the shift, enable "Used for Differential," set premium
3. Choose a Pay Method (Punch In, Punch Out, Zone, or Majority Hours) based on when you want the premium to apply

## 9. Map Unscheduled Hours

**Objective:** If you pay "unscheduled" work at a different rate, map those hours into a chosen OT bucket.

- **Only after scheduled hours:** toggle on if you want scheduled hours first, then map the spillover
- **Map:** Reg/OT1–4 → OT2/3/4 as needed (e.g. any unscheduled reg hours → OT2)

## 10. Stand‑By Time (On‑Call)

**Objective:** Auto‑award "on‑call" hours as Other Activity on specified weekdays.

On each Day of Week tab, Insert an Other Activity Type (e.g. "RN On‑Call") + guaranteed X hrs.

InfiniTime will place that Other Activity on every matching day for each employee.

## 11. Finalize & Review

**Objective:** Ensure all pieces fit together before you go live.

### Checklist:

- No tenure gaps, no overlapping differentials, thresholds sensible
- Breaks, OT, rounding, schedules, exceptions all behave in a quick test user

### Test:

Assign a "sandbox" user, run through punch scenarios, confirm the policy delivers exactly the hours, breaks, OT, and exceptions you expect.
