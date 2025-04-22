# Guide Planning

| #   | Guide Title                                                                      | Why it's useful / what it solves                                                                           |
| --- | -------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| 1   | Create a Brand‑New Policy from Scratch                                           | Walks a first‑time admin through every mandatory tab, saving them from hunting across the UI.              |
| 2   | Move Employees to New Policies Automatically by Tenure                           | Shows how to set up Classes, Default Classes, and min/max tenure so no one falls through the cracks.       |
| 3   | Configure Your Pay Cycle & Edit‑Lock Dates                                       | Step‑by‑step for weekly/bi‑weekly/semi‑monthly/custom cycles, plus locking past periods.                   |
| 4   | Build a Custom Pay Cycle (2‑Week / 3‑Week Rotation)                              | Popular edge‑case that trips people up—includes changing the interval on the fly.                          |
| 5   | Add or Change Break Rules: Change‑to‑Break vs Auto Break                         | Decision tree + examples so customers pick the right break engine the first time.                          |
| 6   | Set Maximum & Minimum Break Lengths with Break Limits                            | Shows how to enforce 15‑minute paid and 30‑minute unpaid rules without payroll surprises.                  |
| 7   | Track Exceptions Company‑Wide vs Per Policy                                      | Helps admins decide where to define Absent, Tardy, etc. and explains override order.                       |
| 8   | Create SMS & Email Exception Alerts                                              | End‑to‑end setup (SMTP, cell gateways, thresholds) so supervisors actually get the texts.                  |
| 9   | Lock Down Past Pay Periods with Edit Lockout                                     | Prevents late adjustments and preserves audit trails.                                                      |
| 10  | Round Punches Correctly: Unscheduled vs Scheduled Rounding                       | Clarifies the three rounding methods, grace periods, and common pitfalls.                                  |
| 11  | Enable Schedule Lockout to Block Early/Late Punches                              | How to combine grace periods and hardware messages (Thor, Scout) for real‑time enforcement.                |
| 12  | Set Hours & Time Limits for Salary Employees                                     | Covers auto‑punch, guaranteed daily/weekly hours, and when to skip time‑tracking entirely.                 |
| 13  | Approve, Reject, or Auto‑Approve Overtime                                        | Explains the red/green overtime indicators and batch approval shortcuts.                                   |
| 14  | Configure Daily, Weekly, and Consecutive‑Day Overtime Rules                      | Includes CA "Deduct Daily from Weekly" logic and flexible workweek salary calc.                            |
| 15  | Map Unscheduled Hours to Premium Buckets                                         | Perfect for clients who pay extra for work outside scheduled shifts.                                       |
| 16  | Build Day‑of‑Week Overtime (e.g., Saturday Double‑Time)                          | Four‑tab walkthrough with example mappings.                                                                |
| 17  | Add Shift Differentials and Choose a Pay Method (Punch‑In, Zone, Majority, etc.) | Most asked‑about payroll feature; explains splitting at midnight.                                          |
| 18  | Create a Default Policy Schedule with Quick Schedule                             | Shows how to give every new hire an instant baseline schedule.                                             |
| 19  | Auto‑Punch Employees In/Out from Schedules                                       | Ideal for salary staff; covers all three auto‑punch strategies and warnings.                               |
| 20  | Use Stand‑By (On‑Call) Time to Pay Employees Not on Site                         | Guides admins through automatic Other Activity entries and validity dates.                                 |
| 21  | Set Up DOT Hours‑of‑Service Exceptions                                           | Keeps transportation clients compliant with Rules 1, 2, 7‑day limits, and off‑duty breaks.                 |
| 22  | Monitor Mandatory Rest & Fatigue with Consecutive‑Day Exceptions                 | Critical for healthcare/manufacturing fatigue rules.                                                       |
| 23  | Manage Accrual‑Based Exceptions (Approaching/Exceeded Time Off)                  | Ties accrual tables, other‑activity deductions, and exception reports together.                            |
| 24  | Catch & Correct Missed Punches Automatically                                     | Tweaks the missed punch threshold and (optionally) schedule checks.                                        |
| 25  | Validate Departments and Prevent Invalid Punches                                 | Uses the "Valid Departments" list plus the Invalid Department exception.                                   |
| 26  | Set Minimum & Maximum Hour Limits (Guaranteed vs Cap)                            | Explains how to guarantee 8 hrs/day but cap at 40 hrs/week, with examples.                                 |
| 27  | Apply Payroll Overrides for Flat Salary Exports                                  | For salary employees who always export 40 hrs when they reach 20+.                                         |
| 28  | Create Semi‑Monthly Pay Periods with Correct "Start Day" Settings                | Clears up the confusing "First Pay Day / Second Pay Day" labels.                                           |
| 29  | Design Grace Periods for Early, Tardy, and Outside‑Schedule Exceptions           | Visual timelines help admins pick realistic minute windows.                                                |
| 30  | Combine Auto Break with Change‑to‑Break Without Double‑Deductions                | Shows the "Allow Auto Break with Change to Break" toggle and real‑world lunch examples.                    |
| 31  | Clone & Version Policies Safely                                                  | Shows how to copy an existing policy, rename it, and migrate employees without breaking pay‑cycle history. |
| 32  | Bulk‑Assign Employees to Policies with Quick Assign                              | Saves HR teams hours when re‑organizing classes or importing new hires.                                    |
| 33  | Build a Policy Schedule with the Gantt Chart                                     | Step‑by‑step for drag‑and‑drop "split at midnight" scheduling and temporary overrides.                     |
| 34  | Create & Use Schedule Skeletons for Forecast Staffing                            | For seasonal ops that need a reusable shell they can paste onto future weeks.                              |
| 35  | Import Schedules from CSV                                                        | Walks through field mapping and typical errors so ops managers can mass‑load rosters.                      |
| 36  | Configure Thor/Scout Terminals for Schedule Lockout Messages                     | Hardware‑specific wiring, polling‑interval, and message‑table tips missing from generic lockout docs.      |
| 37  | Set Up the Windows SMTP Virtual Server for Email & SMS Alerts                    | One‑time server checklist with screenshots of IIS → SMTP Advanced Delivery and relay permissions.          |
| 38  | Add New Cell‑Phone Providers to the SMS Gateway Table                            | Keeps texts flowing when staff switch carriers or you expand into new regions.                             |
| 39  | Use the Exception Points System for Progressive Discipline                       | Explains thresholds, resets, and the Employee Exception Points report.                                     |
| 40  | Audit Policy Changes with the Policy History Report                              | Lets auditors see who tweaked overtime or pay‑cycle settings and when.                                     |
| 41  | Customize Export Pay Codes with Shift Identifiers                                | Bridges InfiniTime to payroll systems that need special codes for differentials or location pay.           |
| 42  | Map Other Activity Types to "Count as Day Worked"                                | Crucial for fatigue rules, consecutive‑day exceptions, and DOT compliance.                                 |
| 43  | Create DOT Sleeper‑Berth & 34‑Hour Reset Rules                                   | Goes deeper than the basic DOT exceptions (#21) to include Off‑Duty Rule and reset calculation nuances.    |
| 44  | Set Up Flexible‑Workweek Overtime for Salaried Staff                             | Explains the dollar‑based OT math and report verification.                                                 |
| 45  | Generate Holiday Rules that Pay Double‑Time Only When Scheduled                  | Combines holiday tables, schedules, and unscheduled‑hours mapping.                                         |
| 46  | Automate Policy Edit‑Lockout Reminders                                           | Uses the housekeeping service plus email alerts so supervisors finalize timecards before lock.             |
| 47  | Configure Stand‑By Pay with Variable Effective Dates                             | Adds Valid From / Valid To ranges for rotating on‑call rosters.                                            |
| 48  | Troubleshoot Missed‑Punch Chaos (Overnight Crews Edition)                        | A checklist covering thresholds, day‑change times, split punches, and schedule gaps.                       |
