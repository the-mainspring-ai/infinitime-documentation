---
title: "Schedule Settings and Rules"
description: "Overview of schedule enforcement rules, including clock-in and clock-out lockouts, grace periods, and warning alerts in InfiniTime™."
---

Schedule Settings General Tab

# Schedule Settings / Rules

![](/img/ShiftDiff_Warning.gif)

Clock In Punch To Schedule / Lockout:

When selected, InfiniTimeâ¢ will alert an employee punching at an Unscheduled time with a warning message and will not allow the employee to punch. Select this check box if you must have strict adherence to the employee's scheduled start time. Grace periods determine the time range where employees will be allowed to punch in. Employees outside of the scheduled grace periods will be unable to punch and will have to find a software administrator or supervisor with the ability to clock them in.

Clock Out Punch To Schedule / Lockout:

When selected, InfiniTimeâ¢ will alert an employee punching at an Unscheduled time with a warning message and will not allow the employee to punch. Select this check box if you must have strict adherence to the employee's scheduled end time. Grace periods determine the time range where employees will be allowed to punch in. Employees outside of the scheduled grace periods will be unable to punch and will have to find a software administrator or supervisor with the ability to clock them in.

Auto Clock In:

When selected, InfiniTimeâ¢ will automatically clock in an employee according to the employeeâs schedule after the Offset time has passed from the schedule time.

_Example_:

- Auto Clock In must be checked
- Offset time is set to 5 minutes
- Employeeâs schedule is 8:00 am to 4:00 PM
- If the employee does not clock in by 8:05 am the system will automatically clock him in at his schedule time of 8:00 am.(This example is with the settings above)

Auto Clock Out:

When selected, InfiniTimeâ¢ will automatically clock out the employee according to the employeeâs schedule.  The housekeeping machine performs this function.

Auto Punch To Schedule:

When selected, InfiniTimeâ¢ will automatically punch the employee according to his/her schedule.  This feature is used if the employee is not required to clock in and out for lunch and the lunch is scheduled, or if the employee has different departments that he/she is assigned to during the day and is not required to clock out of one department and into another.

_Example_:

- Employee schedule is 8:00 am to 4:30 PM with a scheduled unpaid break at 11:30 am to 12:00 PM. The employee will only have to clock in at 8:00 am and clock out at 4:30 PM, then the system will automatically insert the 11:30 am and 12:00 PM punches.
- Employee schedule is 8:00 am to 10:00 am in the Administration department then from 10:00 am to 4:30 PM in the Shipping department with a scheduled lunch from 12:00 PM to 1:00 PM.  The employee will only have to clock in at 8:00 am and clock out at 4:30 PM, then the system will automatically insert the other punches in the schedule clocking the employee out of the Administration department and in into the Shipping department, also inserting the lunch punches.

The following requirements must be met in order for Auto Punch to Schedule to insert punches as expected:

- Employees must punch in at the start of their work day.
- Employees must punch out at the end of their work day.
- Employees should not punch for breaks or manually switch from Department to Department.
- Employees must punch in during [Scheduled Grace Periods.](../Scheduled_Time.md)

Check Activity Department For Schedule Rounding

If this box is checked, InfiniTime will ignore the schedule associated with the employeeâs default department and use the schedule associated with the department the employee is working in.

Example:

- Employee is in the Administration department with a schedule of 8:00am to 5:00pm. And that same employee clock into a different department Sales which has a schedule of 12:00pm to 6:00 PM now the program will use the schedule of the Sales department and not the schedule of the Administration department which is his/hers home department.

Shift Differential Options

A method of pay must be defined for Shift Differentials. Remember, within InfiniTime shift differentials are defined as a period during which employees receive an additional premium. It is not uncommon for employees to be eligible for multiple shift differentials. Shift Differential pay methods determine which differential an employee will receive based upon when they are working or when they punched in. This option should only be set if employees on the policy will be eligible for shift differentials. Shift differentials must be assigned to the policy on the Shift Differentials Tab as detailed in the Schedule Settings / Rules â Shift Differentials Tab section.

Shift Differential Pay Method â A Shift Differential Pay Method must be selected for employees to receive shift premiums. To ensure proper configuration, the Shift Differential pay method drop down is grayed out and cannot be set until a shift differential has been added to the Shift Differential Tab of the policy. As shown below, InfiniTime will warn the user if Shift Differentials are added to the policy and the Shift Differential Pay Method is not configured.

![](/img/image475.gif)

The best method for explaining shift differentials is to review an example scenario. ABC Medical employs Registered Nurses (RNs) who receive differential pay for working during evening and early morning hours as outlined below.

| Differential Name    | Rate  | Start Time | End Time |
| -------------------- | ----- | ---------- | -------- |
| Evening Differential | $1.00 | 8:00 PM    | 12:00 AM |
| Morning Differential | $1.25 | 12:00 AM   | 4:00 AM  |

Punch In â When the Punch In pay method is chosen employees are paid the premium in effect at the time they punch in. For clarity multiple examples are shown below.

![](/img/image477.gif)

An RN arrives at the hospital early and is asked to lend a hand prior to their shift. They clock in at 7PM and work until 4AM. Because the RN clocked in at 7PM, which does not fall within a period eligible for differential pay, the RN will not receive a premium for their hours.

![](/img/Pol_ScheduleSettings.gif)

An RN is called in to work from 8PM to 4AM. The employee punches in at 8:00 PM, which is during the period defined by the Evening Differential. All eight hours (8PM to 4AM) will be paid at the Evening Differential rate.

Punch Out â When the Punch Out pay method is chosen employees are paid the premium in effect at the time they punch out. For clarity multiple examples are shown below.

![](/img/image474.gif)

The typical RN Day shift is 11 AM to 7PM. Mary Joe is asked to stay for an additional two hours and works from 11AM to 9PM. Because Mary clocked out at 9PM, which falls within the Evening Differential, she will receive the Evening Differential Premium for all ten hours worked.

![](/img/image477.gif)

An RN is called in to work from 8PM to 4AM. The employee punches out at 4:15 AM. The employee will not receive a premium for the worked hours because 4:15 AM does not fall within a period defined by a differential.

Majority Hours â The Majority Hours pay method identifies the differential on which employees worked the greatest portion of their hours. The premium associated with that differential is then used for all differential hours for the day as illustrated below. If an employee should work an equal amount of hours across multiple differentials they will be paid the premium associated with the first differential.

![](/img/image479.gif)

The diagram above illustrates an RN being called in to work from 10:00 PM to 4:00 AM. The majority of the worked hours fall within the Morning Differential. As such the employee receives the Morning Differential premium ($1.25) for all hours worked.

Zone â Zone is the most commonly used pay method for shift differentials. Employees will be paid a premium according to the differential they are working on. In this scenario if an RN were to be called in to work from 10:00 PM to 4:00 AM they would receive two hours of Evening Differential Pay and Four Hours of Morning Differential Pay as follows:

![](/img/image474.gif)

The diagram illustrates an RN being called in to work from 10:00 PM to 4:00 AM. Hours from 10:00 PM to 12:00 AM are associated with the Evening Differential. Hours from 12:00 AM to 4:00 AM are associated with the Morning Differential. The employee is paid as follows:

2 Hours Evening Differential Premium

4 Hours Morning Differential Premium

Unscheduled Work Hours Distribution:

This feature allows you to distribute the hours worked by an employee that are not scheduled.  You may assign regular hours to count as overtime.

_Example_:

- If an employee is only scheduled to work from 8:00 am to 2:00 PM but on one day the employee worked until 3:00 PM, the hour from 2:00 PM to 3:00 PM is not scheduled and will be posted as overtime if âUnscheduled Regular Hours into OTâ was set to Overtime 1..

Earliest Allowed Clock In Time:

This will set the earliest a punch can be recorded as IN.  For example: If the earliest allowed clock in time is set to 6:00 am and if an employee clocks in at 5:00 am the punch will be accepted and shown as 5:00 AM on the timecard though hours for the day will be calculated as if the employee punched in at 6:00 AM.

Latest Allowed Clock Out Time:

This will set the latest time a punch can be recorded as OUT. InfiniTime does not change the employee's punch though hours for the day will be calculated as if the employee punched out at this time. For example if the Latest Allowed Clock Out Time is set to 4:00 PM and an employee punches out at 5:00 PM the punch will be accepted and shown as 5:00 AM though hours for the day will be calculated as if the employee punched out at 4:00 PM.
