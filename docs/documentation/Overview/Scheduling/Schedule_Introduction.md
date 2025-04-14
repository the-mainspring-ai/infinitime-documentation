xml version="1.0" encoding="utf-8" ?





Schedule Introduction




# Schedule Introduction

The Schedule feature can be accessed through Company and Schedule from
the Main Menu Bar.  Scheduling allows you to input expected hours
that an employee will work.  This gives InfiniTimeâ¢ a basis from
which to compare actual worked time.  The Schedule is designed to
allow rapid entry while maintaining flexibility for complex schedules.
 InfiniTimeâ¢ allows you to input a default schedule in many areas
of the program including the employee profile and in the policy update.

Accessing The Schedule:

* Click
  on the Schedule button on the main menu bar.

![](/img/sched3.gif)

Employee Schedule Window

![](/img/CH6_Schedule2.gif)

Schedule
Date - Select the date that corresponds to the day you would like
to configure schedules for. All schedule related information will be shown
for the date selected according to selected filter and view settings.
VCR Buttons have been incorporated to the right of the schedule date in
order to simplify moving ahead or backward by a single day. Simply click
on the Left VCR button to change the Schedule Date one day back, or the
Right VCR button to change the Schedule Date one day forward.

![](/img/sched1.gif)

View
Type - This option alters the way schedule information is displayed
on the GANNT chart. Available options include a daily, weekly, and monthly
view.

Filter
-  This button will allow you to select employees for which schedule
information will be displayed. Refer to the User Interface section of
this document for further information on using the Employee Filter.

Duplicate

This button will allow
you to copy a schedule from a date range to another, by employee or department.
The following screen is displayed.

![](/img/sched1.gif)

Copy
from: Specify the start date and end date of the period for which
you would like to copy schedule information from.  All schedule information
within the selected period will be copied.

Copy
To: Specify the start and end date of the period for which you
would like to copy schedule information to. This period should be the
same length as the copy from period.

Copy
From: Select the employees from which you would like to copy schedule
information.

Match
By Day of Week: Check this box to match schedule information to
the appropriate day of week. This option is useful for copying a month
of schedule information from one month to another month, which may not
necessarily start or end on the same day.

Override
Default Schedule: Checking this box will cause the copied schedule
to override default schedule information for destination employees.  If
box is not checked then it will not override existing schedules it will
only put a schedule where there is none scheduled.

Filter:
Use the employee filter to select employees that schedule information
will be copied to.

Find Available

This button permits employee
scheduling based upon availability. The below requirements must be met
before the Find Available button may be used.

* Availability must be configured. Inception
  Technologies recommends defining a separate availability entry for
  each employee. The availability entry should reflect normal hours
  where an employee is available for working.

* Each
  employee must have an availability record assigned within their employee
  record.

![](/img/CH6_Schedule1.gif)

Available employees will
be displayed in the lower grid as shown above.  Employees will not
be displayed as available if:

* They
  are already scheduled for work hours on the selected date.
* They
  are not available as determined by their availability schedule.
* They
  are not trained for the selected task(s).

Schedule
Date: Select the date to schedule using employee availability.

Begin
Time: Select the start time for the period you wish to schedule.

End
Time: Select the end time for the period you wish to schedule.

*Note*:
The begin and end times define the period that will be scheduled. Employees
must be available during this period according to their availability schedule,
otherwise no one will be displayed. Refer to the Availability section
of this document for more information about setting up Availability schedules.

Tasks:
Select the task you want to schedule. Employees will only be listed if
they are trained for the selected task. If all tasks are selected employees
trained for any task will be listed if they are available during the selected
period.

Schedule:
Schedules the selected employee for the time specified. The Schedule GANNT
chart will be updated with this information after the Schedule Availability
Employee table is closed.

Use Skeleton

This button makes it
possible to create daily schedules in an efficient manner using predefined
schedule skeletons. This makes it possible to match employees trained
for a specific task, and available during a certain time period to a shift
corresponding with their abilities.

![](/img/CH6_Schedule1.gif)

Name:
Select the Skeleton you wish to use for scheduling purposes.

Schedule
Date: Select the date to schedule using skeletons.

Delete:
Removes the employee assigned to the specified task and time period.

Search:
Select the task for which you wish to view available employees and click
on this button. The lower grid will be populated with employees that meet
the criteria defined by the skeleton. Employees will not be displayed
as available if:

* They
  are already scheduled for work hours on the selected date.
* They
  are not available as determined by their availability schedule.
* They
  are not trained for the selected task(s).

Assign:
Used to assign the selected employee to the task and schedule highlighted
in the Skeleton Task Grid.

Schedule: Schedules the
assigned employees for the task and time period specified by the Skeleton
Task Grid. The Schedule GANNT chart will be updated with this information
after the Schedule Skeleton window is closed.