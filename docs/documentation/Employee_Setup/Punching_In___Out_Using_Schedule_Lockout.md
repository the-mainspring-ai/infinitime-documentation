---
title: "Punching In & Out Using Schedule Lockout"
description: "Guide on how the schedule lockout feature controls employee punching times with the Thor Terminal, including handling violations and overrides."
---

Punching In & Out Using Schedule Lockout

# Punching In & Out Using Schedule Lockout

If you are using the lockout feature of the software to keep employees from punching outside of the their schedule, it is important to understand how the lockout feature functions with the Thor Terminal. The Thor terminal treats the employee's start and end times as a window, during which employees are permitted to clock in. If the employee attempts to punch in outside of this window a prompt will be displayed alerting they are in violation of their schedule. If a supervisor is available the violation can be overridden which will allow the employee to punch in at the clock.

For Example: Jane's schedule is defined as 8:00 AM to 5:00 PM within InfiniTime. Jane can punch in or out between the hours of 8:00 AM and 5:00 PM without receiving the a schedule violation message. Attempts to punch outside of this time period will result in schedule lockout.

If the employee attempts to punch outside of the window defined by their schedule the Thor will display a message: Schedule Violation: Supervisor Override?

1. 1. If the supervisor is available to override the lockout press YES and it will ask for the supervisor's authentication. Depending on the Thor's model supervisors can then authenticate via ID and Password, Badge or Fingerprint.
   2. After authentication the employee's punch will be accepted accepted by the InfiniTime Software even though the employee is outside of their normal schedule.
   3. If the Supervisor is not going to override the lockout press NO and the punch will not be accepted.

_Note_: Any employee assigned to a security role with the 'Supervisor in Readers' option enabled will not be locked out, they will always be able to clock in & out.  The Schedule Violation message will not display even if they are in violation because the employee has the ability to override the lockout. For this reason the lockout is ignored.  See Security Roles Introduction for more information on Security Roles
