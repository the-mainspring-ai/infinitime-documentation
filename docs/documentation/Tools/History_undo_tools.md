## History & Undo Tools

### History & Undo Tools Introduction

InfiniTime includes several
utilities, as summarized below, which can be used to add or alter Time
and Attendance Data for multiple employees at a time. Since the possibility
for accidental or improper use of these utilities exists, InfiniTime retains a log of all Purge,
Quick Punch, Quick Schedule, and Supervisor Review actions. In this way,
InfiniTime Administrators
can undo unintended alterations.

| Utility           | Purpose                                                                                         |
| ----------------- | ----------------------------------------------------------------------------------------------- |
| Purge             | Deletes all Timecard Activity for a specific Date Range for selected Employee(s).               |
| Quick Punch       | Inserts Punches for Selected Employees for all dates in the Specified Date range.               |
| Quick Schedule    | Creates Gannt Chart Schedules for Selected Employees for all dates in the specified Date Range. |
| Supervisor Review | Marks Employee Timecard Records in the specified Date Range as reviewed for Selected Employees. |

Details on how to access and utilize the History & Undo Tools for
each of the utilities above are provided below.

### Purge History Introduction

The InfiniTime Purge
History Tool maintains a running list of all purge actions that have been
performed since database creation. Using the Undo feature any action can
be undone. Should users make a mistake or remove information not intended
for removal data can easily be restored using the Purge History Tool.

Accessing Purge History

- Click on Tools
- Click on History And Undo Tools

![](/img/CH15_SysMon.gif)

- Click on Purge History.

![](/img/RLSNOTE_707-06.jpg)

View â Displays information
related to the purge action. The date range timecard activity was purged
from, employees the purge action was performed on, and the employee that
performed the purge action are all listed.

![](/img/ph8.gif)

Insert
â Click on Insert to purge employee activity. The action will be saved
in the Purge History Table.

![](/img/QST_SETUP_IMP_FILETYPE.gif)

Description â Enter a descriptive
name for the action you are performing. This description will be entered
into the Purge History table. Using detailed descriptions will help users
identify the record in the Purge History Table should the action need
to be undone in the future.

Date Range â All Timecard Activity
for specified employees that falls within this date range will be purged
from the software.

Filter â Use the Employee Filter
to select which employee(s) activity will be purged for.

Undo â InfiniTime
keeps a record of all Timecard Activity that was removed by a specific
purge action. Should the user decide that they want to restore that data
for any reason the Undo Feature can be utilized. All activity that was
originally removed by the purge action will be restored

Technical Note: The Undo Feature takes a snapshot
of current settings. Using the Undo Button simply instructs the software
to restore the settings that were saved in this snapshot. The snapshot
is taken before the changes specified by the purge action are applied.
For example, lets say all of the Timecard Activity before 1/1/2005 is
considered archivable and no longer required within the InfiniTime Application. A purge could
be executed from 1/1/2000 when the company in this example started using
the software to 1/1/2005. The Purge History Window saves a snapshot of
all activity within this date range. Should the undo feature be used all
activity within this date range will be restored. If any punches were
manually added to the system between the date range of 1/1/2000 to 1/1/2005
after the purge action they would remain unaltered.

Delete â Removes the highlighted
purge history record from the Purge History Table. Once a record is removed
from the Purge History Table its actions cannot be undone. Default security
role configuration permits purge record removal by the software administrator
or payroll clerks in order to prevent actions from being undone in the
future.

### Undoing a Previous Purge Action

- Determine which record in the Purge History table corresponds to
  the action that you wish to undo. Viewing the record to see the date
  range and employee who performed the original action can assist with
  this decision.
- You may wish to take a backup before to undo a purge action.
- Click on the record to highlight it.

![](/img/cset24.gif)

- Click Undo.

![](/img/Ch11_Export4.gif)

- Click Yes to confirm your decision.

![](/img/ClickServices.gif)

- Wait while the action is undone. All activity that was removed
  by the purge will be restored to the Timecard Activity Table.

![](/img/CH11_ImportFields_EmpShort.gif)

### Quick Punch History Introduction

The InfiniTime Quick
Punch History Tool maintains a running list of all quick punch actions
that have been performed since database creation. Using the Undo feature
any action can be undone. Should users make a mistake or add information
for the wrong employees the Quick Punch History Tool makes it easy to
remove incorrect Timecard Activity entries.

Accessing the Quick Punch History Tool:

- Click on Tools.
- Click on History And Undo Tools.

![](/img/maint1.gif)

- Click on Quick Punch History.

![](/img/CH11_ImportFields_GroupDesc.gif)

View
â Displays information related to the quick punch action. The date range
timecard activity was inserted, employees the activity was inserted for,
and the related punch pair times are all listed.

![](/img/ExpandServicesandApplications.gif)

Insert
â Click on Insert to insert a Quick Punch. The action will be saved in
the Quick Punch History Table.

Undo
â InfiniTime keeps a record
of all Timecard Activity that was inserted by a specific quick punch action.
Should the user decide that they want to remove that data for any reason
the Undo Feature can be utilized. All activity that was originally inserted
by the quick punch action will be removed.

Technical Note: The Undo Feature takes a snapshot
of current settings. Using the Undo Button simply instructs the software
to restore the settings that were saved in this snapshot. The snapshot
is taken before the changes specified by the quick punch action are applied.
For example, lets say Quick Punch was used to add activity from 8:00 AM
to 5:00 PM for all employees by accident. Should the undo feature be used
all activity added by the Quick Punch will be removed. If any punches
 added by the quick punch were manually edited after the quick punch
these changes will be lost. All activity records added by the quick punch
will be removed from the system.

Delete
â Removes the highlighted Quick Punch history record from the Quick Punch
History Table. Once a record is removed from the Quick Punch History Table
its actions cannot be undone. Default security role configuration permits
purge record removal by the software administrator or payroll clerks in
order to prevent actions from being undone in the future.

### Inserting a Quick Punch

![](/img/TP8.gif).gif)

Description
â Enter a descriptive name for the action you are performing. This description
will be entered into the Quick Punch History table. Using detailed descriptions
will help users identify the record in the Quick Punch History Table should
the action need to be undone in the future.

Date Range
â All Timecard Activity for specified employees that falls within this
date range will be purged from the software.

Punch Type - Use the drop down menu
to select the type of punch, choose from regular punch, schedule punch,
single punch, or other activity.

Regular
Punch - Inserts a set of punches. The first time specified is the
clock in time, while the second time specified is the clock out time.

Scheduled
Punch - Inserts punches according to the employees schedule. For
example if the employee is scheduled to work from 8:00 AM to 5:00 PM InfiniTime will automatically clock
the employee in at 8:00 AM and out at 5:00 PM.

Single Punch

- Inserts a single punch. InfiniTime
  automatically determines the punch type based upon the timecard activity
  already present on the date where the single punch is inserted.

Other Activity

- Inserts other activity such as holiday time, vacation time, sick time,
  and personal time.

Use Default
Department - if this is checked the punches will be posted using
the default department of the employee, if not checked you can choose
a department using the magnify glass or typing in the department name
to post those punches.

Use Default
Job - if this is checked the punches will be posted using the default
Job of the employee, if not checked you can choose a Job using the magnify
glass or typing in the Job name to post those punches.

Use Default
Task - if this is checked the punches will be posted using the
default Task of the employee, if not checked you can choose a Task using
the magnify glass or typing in the Task name to post those punches.

Start
Time â Enter the time that employees specified by the employee
filter started working.

End Time
â Displays the time that employees specified by the employee filter stopped
working. This field is automatically updated by the Duration and cannot
be edited directly.

Duration
â Enter the number of hours worked by employees specified by the employee
filter. The End Time will automatically be updated by this value. For
example, if the Start Time was set to 8:00 AM and 8 were entered into
the Duration, the End Time would automatically update to 4:00 PM.

Add Duplicate Punches

- Unless this box is checked InfiniTime will compare the punches
  being inserted to those already in the database when performing a Quick
  Punch. Any duplicate punches will be ignored. For example the image below
  shows an employee working from 7:30 AM to 5:00 PM on 1/17/2008. If a supervisor
  were to attempt to insert a punch on 1/17/2008 from 7:30 AM to 5:00 PM
  using quick punch then the punches would not be inserted unless Add Duplicate
  Punches was checked.

![](/img/i20.gif)

Weekday
Only â If this is checked it will only insert punches for weekdays
only and not the weekend, Saturday and Sunday.

Description
â Used for Auditing Purposes, any information typed into this box will
be saved to the Audit Trail for all inserted punches. This information
can then be viewed using the Audit feature at a later date.

Filter
â Use the Employee Filter to select which employee(s) activity will be
inserted for.

### Undoing a Previous Quick Punch Action

Determine which record in the Quick Punch History table corresponds
to the action that you wish to undo. Viewing the record to see information
about the Quick Punch can assist with this decision.

- Click on the record to highlight it.

![](/img/cset21.gif)

- Click Undo.

![](/img/maint4.gif)

- Click Yes to confirm your decision.

![](/img/ebut.gif).gif)

- Wait while the action is undone. All activity that was inserted
  by the Quick Punch will be removed from the Timecard Activity Table.

![](/img/Ch11_Export21.gif)

### Quick Schedule History Introduction

The InfiniTime Quick
Schedule History Tool maintains a running list of all schedules that have
been performed using the quick schedule function. Using the Undo feature
any action can be undone.

Accessing Quick Schedule History

- Click on Tools
- Click on History And Undo Tools

![](/img/tcard11.gif)

- Click on Quick Schedule History

![](/img/TP7.gif)

View â Displays information
related to the quick schedule action. The date range of the schedule added,
and the description of the schedule.

![](/img/JobImport.gif)

Insert â Click on Insert to
create a schedule. The action will be saved in the Quick Schedule History
Table.

![](/img/CH11Export_Email.gif)

Undo
â InfiniTime keeps a record
of all schedule records inserted by a specific quick punch action. Should
the user decide they want to remove that data for any reason the Undo
Feature can be utilized. All schedule records originally inserted by the
quick punch action will be removed.

Technical Note: The Undo Feature takes a snapshot
of current settings. Using the Undo Button simply instructs the software
to restore the settings that were saved in this snapshot. The snapshot
is taken before the changes specified by the Quick Schedule action are
applied. For example, lets say Quick Schedule was used to add a schedule
from 8:00 AM to 5:00 PM for all employees by accident. Should the undo
feature be used all schedule records added by the Quick Punch will be
removed. If any schedules added by the quick punch were manually edited
after the quick schedule these changes will be lost. All activity records
added by the quick punch will be removed from the system.

Delete
â Removes the highlighted Quick Punch history record from the Quick Punch
History Table. Once a record is removed from the Quick Punch History Table
its actions cannot be undone. Default security role configuration permits
purge record removal by the software administrator or payroll clerks in
order to prevent actions from being undone in the future.

### Supervisor Review History Introduction

The InfiniTime Supervisor
Review History Tool maintains a running list of all review actions that
have been performed since database creation. Using the Undo feature any
action can be undone. Should users make a mistake or accidentally review
activity for the wrong employees the Supervisor Review History Tool makes
it easy to revert Timecard Activity entries to their original un-reviewed
status.

Accessing the Supervisor Review History Tool:

- Click on Tools.
- Click on History And Undo Tools.

![](/img/TCPIP.gif)

- Click on Supervisor Review History.

![](/img/HousekeepingSvcStopped.gif).gif)

View
â Displays information related to the Timecard Activity Review action.
The date range timecard activity was reviewed, employees activity was
reviewed for, and the record description are all listed.

![](/img/Ch11_Export7.gif).gif)

Insert
â Click on Insert to review timecard activity. The action will be saved
in the Supervisor Review History Table.

Undo
â InfiniTime keeps a record
of all Timecard Activity that was marked as reviewed by a specific review
action. Should the user decide that they want to return that data to its
original un-reviewed state for any reason the Undo Feature can be utilized.

Insert â Click on Insert to insert
a Quick Punch. The action will be saved in the Quick Punch History Table.

Undo
âInfiniTime keeps a record
of all Timecard Activity that was inserted by a specific quick punch action.
Should the user decide that they want to remove that data for any reason
the Undo Feature can be utilized. All activity that was originally inserted
by the quick punch action will be removed.

Technical Note: The Undo Feature takes a snapshot
of current settings. Using the Undo Button simply instructs the software
to restore the settings that were saved in this snapshot. The snapshot
is taken before the changes specified by the review action are applied.
For example, lets say a supervisor accidentally reviewed activity for
all employees by neglecting to configure the employee filter. Should the
undo feature be used all review records added by the review action will
be removed.

Delete
â Removes the highlighted Supervisor Review history record from the Supervisor
Review History Table. Once a record is removed from the Supervisor Review
Table its actions cannot be undone. Default security role configuration
permits purge record removal by the software administrator or payroll
clerks in order to prevent actions from being undone in the future.

### Inserting a Supervisor Review

![](/img/Housekeeping03.gif).gif)

Description
â Enter a descriptive name for the action you are performing. This description
will be entered into the Supervisor Review History table. Using detailed
descriptions will help users identify the record in the Supervisor Review
History Table should the action need to be undone in the future.

Date Range
â All Timecard Activity for specified employees that falls within this
date range will be marked as reviewed.

Filter
â Use the Employee Filter to select which employee(s) activity will be
reviewed for.

### Undoing a previous Review Action

Determine which record in the Supervisor Review History table corresponds
to the action that you wish to undo. Viewing the record to see information
about the Review action can assist with this decision.

- Click on the record to highlight it.

![](/img/maint8.gif).gif)

- Click Undo.

![](/img/winbackuprestore3.gif).gif)

- Click Yes to confirm your decision.

![](/img/e4.gif).gif)

- Wait while the action is undone. All activity that was marked as
  reviewed by the review action will be returned to its original un-reviewed
  state.

![](/img/Barcode-settings.gif).gif)
