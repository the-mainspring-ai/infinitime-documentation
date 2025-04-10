xml version="1.0" encoding="utf-8"?





Scheduled Time




# Scheduled Time

![](images_2/Scheduled_Time_Rounding.gif)

Scheduled Time Rounding:  Before describing the Punch and Round To features it is important to understand the Grace Period Settings.  The Grace Period Settings allow you to create a window of time that tells InfiniTimeâ¢ when and how to classify a punch activity.

Grace periods are powerful settings that determine:

1. When the Punch to Schedule feature should be enforced.  With Punch To Schedule/Lockout checked, InfiniTimeâ¢ will strictly monitor the punching in accordance to the schedule and grace periods, and will NOT allow any punches outside of the alotted time.
2. When a punch should Round to Schedule, in other words, the punch will be rounded to the scheduled time. (Please see Schedule for scheduling info.)
3. What type of Report Tag will be marked for each punch on the Timecard reports (See Reports and Graphs: Report Tags for more information).

InfiniTimeâ¢ has three separate tabs for grace period options, which allows you to customize each type of punch.

* Clock In Punch Rounding
* Break Punch Rounding
* Clock Out Punch Rounding

Early Grace Period:  This setting is relative to the On Time Grace Period Setting. This spin box allows you to enter a number in whole minutes and 1/100ths  of a minute, that a punch will be counted as Early. To be counted as Early, a punch would have to fall between the scheduled time minus the On Time Grace Period setting, and the Early Grace Period setting. Punches that occur prior to the Early Grace Period are considered Unscheduled. A zero entered here will not use the Early Grace Period.

On Time Grace Period:  This setting determines how many minutes, prior to the employees scheduled time, a punch is considered On Time. This setting also determines when the Early setting takes effect. A zero entered here will not use the On-Time Grace Period.

Late Grace Period:  This setting allows you to enter a number in whole minutes and 1/100ths of a minute, that a punch will be counted as Late. To be counted as Late, a punch would have to fall between the scheduled time and the Late Grace Period settings. Punches that occur after the Late Grace Period are considered Unscheduled. A zero entered here will not use the Late Grace Period.

*For Example*: An employee is scheduled to begin work at 8:00 AM and end work at 4:00 PM, and the Clock In/Clock Out Grace Periods are set as follows:

Early Grace Period:  30 Minutes

On Time Grace Period:  10 Minutes

Late Grace Period:  30 Minutes

This means that if the employee were to punch in from 7:20AM through 7:50AM, they would be considered Early.  This is set by taking the scheduled time and subtracting the On Time Grace Period, then subtracting additional time for the Early Grace Period.  Any punches before 7:20AM are unscheduled and will not be allowed to punch if punch to schedule/lockout is checked.

If they were to punch between 7:50AM and 8:00AM, his punch would be considered On Time, since the allotted time is 10.00 minutes.

If they were to punch in from 8:00AM to 8:30AM they will be considered Late.  Any punches after 8:30AM are unscheduled, and will not be allowed to punch if punch to schedule/lockout is checked.

Rounding Punches to Schedule:  InfiniTimeâ¢ allows you to cause clock in and out times to be altered, rounding them to the employee's scheduled work times. Only those punches that are considered Early, or On Time will be rounded.  Each tab allows you to customize each type of punch.

Round Clock-In to Schedule:  Selecting this check-box changes the recorded Clock-In time to the Scheduled time. Only those Clock-In times that are considered Early or On Time will be altered. Any other Clock-In time that occurs outside of the scheduled time range will record the actual system time that the punch occurred.

Round Clock Out to Schedule:  Selecting this check-box changes the recorded Clock Out time to the Scheduled time. Only those Clock Outs that are considered Late will be altered. Any other Clock Out that occurs outside of the scheduled time range will record the actual system time that the punch occurred.