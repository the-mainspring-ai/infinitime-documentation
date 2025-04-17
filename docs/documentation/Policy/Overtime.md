---
title: "Overtime Rules and Settings"
description: "Guide to configuring overtime levels, excessive hours, and missing punch thresholds for employee time tracking."
---

Overtime

# Overtime Rules

![](/img/Overtime_Rules.gif)

Use this to set overtime rules. You can set up to four overtime levels.  Overtime Two settings must be higher than the Overtime One settings, etc.  If you do not wish to calculate overtime on a daily or weekly basis, set fields equal to zero.

Excessive Hours:  Excessive hours are used to determine if an employee is working too many hours.  When the hourâs amount is reached that is entered in this field an exception will be generated and the employees name will appear in the excessive hours report with the total amount of hours.

Missing Punch Threshold: The Missing Punch Threshold is an amount, entered in hours, which defines the maximum amount of time that may elapse before an employee is considered missing a punch. The timer starts when an employee clocks in. For example, if the Missing Punch Threshold is set to twelve hours this states that no employee should work for more than twelve hours without punching out to either take a break or end their work day. If this timer should expire before an employee punches out the system generates a missed punch exception and the next punch by the employee will be considered a clock in. A twelve hour setting is the recommended value unless it is known for sure that employees may work longer than twelve hours without punching.

It is important to set the missing punch threshold to the smallest hour amount possible without causing false positives. This helps to eliminate the possibility of an employee missing a punch when returning from lunch without causing a missed punch exception. For example:

An Employee works from 6:00 AM to 3:00 PM and generally takes a break from 10:00 AM to 11:00 AM. The employee misses their punch returning from lunch at 11:00 AM. They then punch out at 3:00 PM. The next day they come to work at 6:00 AM. The hours would break down as follows if the missing punch threshold was set to 16 hours:

6:00 AM     IN

10:00 AM   OUT      4 Hours

3:00 PM     IN

6:00 AM     OUT      15 Hours

Total:                         19 Hours

This occurs because the missing punch threshold is set to a value which is excessively above the amount of hours between the time an employee clocks in and the time an employee clocks out. If the missing punch threshold had been less than 15 hours InfiniTime would have generated an exception between the last punch of the first day and the last punch of the next day.

Clock In Missing Punch Day Change Time:  This field allows you to enter a specific time as to when your work day begins, if an employee is clocked in prior to this time, the system will assume that they forgot to clock out and the next punch they enter will say clock IN instead of clock OUT.  This helps employees not be confused and allow managerâs to keep track of employee-missed punches.  InfiniTimeâ¢ will flag this as a Missing Punch Exception.

Clock Out Missing Punch Day Change Time:  This field allows you to enter a specific time as to when your workday ends.

Overtime Must Be Approved:  Checking this box will flag overtime hours as unapproved. If this item is selected the system administrator must manually approve all overtime hours or the employee will not be paid for the overtime worked.

Deduct Daily Overtime from Weekly Overtime:  By default, any daily overtime hours will count towards the weekly total hours as well.  Selecting this check box will cause the overtime calculated on a daily basis not to count towards the weekly total. Selecting this check box with âOvertime Daily If Over Hoursâ set to zero or blank will not have any effect on overtime.

_For Example_, an employee with a policy that has Overtime settings:

Overtime One Daily If Over Hours:  8.00 Hours

Overtime One Weekly if Over Hours:  40.00 Hours

Overtime Two Daily If Over Hours:  12.00 Hours

Overtime Two Weekly if Over Hours:  60.00 Hours

Deduct Daily Overtime from Weekly Overtime:  Checked

The employee works 12.00 hours a day for four days, which is 48.00 hours, and 13.00 hours on the last day for a weekly total of 61.00 hours.  Each of the first four days would have 4.00 hours Overtime One due to the daily setting, on the last day however, the employee would have 4.00 hours of OT1 and 1.00 hour of OT2 for a total of 20:00 hours OT1 and 1.00 hour of OT2 for the week.  Because the Deduct Daily Overtime from Weekly Overtime was checked, the 4.00 hours of Overtime One per day, would not count towards the weekly overtime setting of 40.00 hours for OT1, and 60.00 hours for OT2.  So, the totals for the week would be 40.00 regular hours, 20.00 Overtime One hours and 1.00 Overtime Two hours. If the Deduct Daily Overtime from Weekly Overtime were not selected than the totals would be 24.00 regular hours, 35.00 OT1 hours, and 2.00 OT2 hours.

Add / Subtract Daylight Savings Hour When Time Changes: When this option is checked InfiniTime automatically adjusts working hours for any employees who work across the time change that occurs when Daylight Savings Time Starts in March or Ends in November. For states that observe Daylight Savings Time the time is shifted ahead one hour on the second Sunday of March at 2:00 AM and behind one hour on the first Sunday of November at 2:00 AM. When this option is enabled InfiniTime will adjust employee hours as follows:

- Employees whose working period crosses 2:00 AM on the first Sunday of November will have one hour added to the total working duration.
- Employees whose working period crosses 2:00 AM on the second Sunday of March will have one hour subtracted from the total working duration.
