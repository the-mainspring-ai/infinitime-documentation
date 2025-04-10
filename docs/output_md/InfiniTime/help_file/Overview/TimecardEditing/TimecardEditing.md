xml version="1.0" encoding="utf-8" ?





TimecardEditing




# Timecard Editing Overview

InfiniTime includes two
methods for viewing employee timecards. Each method is better suited for
specific tasks as outlined below.

Company
Timecard Table

* Lists all employees within the company
* Ideal for Timecard Editing
* Most efficient for reviewing timecards for multiple employees

Employee
Timecard Table

* Displays Timecards, Hour Totals, Exceptions, Shift Differential
  Totals, and Department Totals in an âExpress Viewâ format.
* Ideal for Reviewing Exceptions and Timecard History for an Individual

Similar to other windows and tables found within the InfiniTime Application the Timecard
Tables are displayed in a grid format. The Company Timecard Table is composed
of two grids: A list of employees and a list of timecard records for the
selected employee. Each grid can be configured individually to hide or
show information via âSelect Grid Columns.â The size of each grid can
also be altered to show additional employees or timecard records on a
single page. The grid design used through the InfiniTime
Application makes it possible for the software to support companies from
twenty five to two and a half thousand employees and beyond. By comparison
the Employee Timecard Activity Table includes a single grid listing timecard
records for the chosen employee and the express view which displays Hour
Totals, Exceptions, Shift Differential Totals, and Department totals for
the selected pay period.

Company Timecard Table â Employee List

![](/img/SW_CH11_NOTES_0005.gif)

Company Timecard Table â Activity Records

![](/img/SW_CH11_NOTES_0001.gif)

Employee Timecard Table â Activity Records

![](/img/Absent_right_click.gif)

Employee Timecard Table â Express View

![](/img/InLineEdit_MP1.gif)

### Accessing the Company Timecard Table

To access the Company
Timecard Table, which displays Timecard Records for all employees:

* Click on the ![](/img/InLineEdit_4.jpg) button
  on the tool bar

![](/img/InLineEdit_1.jpg)

* The Company Timecard Table will be displayed..

### Accessing the Employee Timecard Table

To access the Time card
Activity for a specific employee:

* Click on the ![](/img/TCard001.png) button
  on the tool bar.
* The Employee Table will be displayed.
* Highlight the employee that you want to see activity for.
* Click on the ![](/img/image93.gif) button to access the Employee
  Timecard Activity Table.

### Timecard Editing Modes

As a web application with various deployment methods, InfiniTime Timecard Tables offer different
editing modes in order to provide high performance and responsive timecard
editing capabilities for both local users on low latency connections with
adequate bandwidth and also for remote users accessing InfiniTime via higher latency connections
with high utilization. A Brief outline of available editing modes is provided
below. The Timecard Editing Mode is a company wide setting - all InfiniTime Users will use the same
timecard editing method. It is important to note that the Company and
Employee Timecard tables must be closed and reopened in order for alterations
to the Timecard Editing Mode Company settings to take effect.


The Timecard Editing Mode is controlled by the 'Delayed Save on Timecard
Editors' and 'Delayed Edit on Timecard Editors' Functional Options on
the Company Update Form:

![](/img/InLineEdit_ArrDep3.gif)

To view or alter the current Timecard Editing Mode, Click on the Company
Button on the Main Toolbar. The  'Delayed Save on Timecard Editors'
and 'Delayed Edit on Timecard Editors' options are displayed on the functional
options tab as shown below.

![](/img/SW_CH11_NOTES_0002.gif)

 | Delayed Save on Timecard Editors Status | Delayed Edit on Timecard Editors Status | Timecard Edit Mode | 
| --- | --- | --- |
 | Unchecked | Unchecked | * Save Immediately -   The 'Save Button' will not be displayed on the Company Timecard.   Alterations to individual Timecard Records will be saved immediately   when focus is removed from the record. If only one record   is present in the Timecard Table, Tab must be used to remove   focus from the record. * Edit Immediately -   Timecard Records are loaded with all in line   edit controls (IE: Time Picker & Date Selection Tool)   and may be edited immediately.     This mode is considered outdated. InfiniTime 7.08 includes delayed save which permits timecards to be edited like a spreadsheet and reduces the number of transactions sent between the InfiniTime Client machine and Server providing improved performance. | 
 | Checked | Unchecked | * Delayed Save -    A 'Save Button' will be displayed after a timecard record   is altered and focus is removed from the record. Additional   timecard records may then be altered prior to saving the changes.   In this way, the Timecard Table can be edited like a spreadsheet   moving from cell to cell to edit punch dates and times as   needed before saving the changes. Changes to altered timecard   records are saved when: A. The user clicks the save button.   B. The user switches pages in the timecard table. C. The user   switches to another employee. Delayed Save also permits the   user to click Cancel in order to revert to the original timecard   records and cancel recent changes. * Edit Immediately -   Timecard Records are loaded with all in line edit controls   (IE: Time Picker & Date Selection Tool) and may be edited   immediately.     This mode is enabled by default for new InfiniTime installations and is ideal for normal use in most operating environments where InfiniTime is deployed on a local area network or wide area network. The Delayed Save functionality and user friendly spreadsheet - like interface provide increased performance by reducing the number of round trips between the InfiniTime Client Machine and InfiniTime Server. | 
 | Unchecked | Checked | * Save Immediately -   The 'Save Button' will not be displayed on the Company Timecard.   Alterations to individual Timecard Records will be saved immediately   when focus is removed from the record. If only one record   is present in the Timecard Table, Tab must be used to remove   focus from the record. * Delayed Edit -   Timecard Records are loaded in View Only Mode. In Line Edit   Controls such as the Time Picker & Date Selection Tool   are not displayed. The User must click on 'Change' before   timecard records can be edited.     This mode enables delayed edit, which significantly reduces the time required to load the Timecard Grid, especially for clients connecting to the InfiniTime server over a higher latency WAN Connection with high bandwidth utilization. Users who observe delays while editing timecards, especially when switching from employee to employee and waiting for timecards to be displayed, may wish to enable Delayed Edit.    This mode is not recommended as delayed save is not enabled. This will increase the number of transactions sent back and forth between the InfiniTime Client Machine and the InfiniTime Server. Customers who use this mode are often used to the Save Immediately interface from prior versions of the InfiniTime Software and specifically choose not to enable delayed save. | 
 | Checked | Checked | * Delayed Save -    A 'Save Button' will be displayed after a timecard record   is altered and focus is removed from the record. Additional   timecard records may then be altered prior to saving the changes.   In this way, the Timecard Table can be edited like a spreadsheet   moving from cell to cell to edit punch dates and times as   needed before saving the changes. Changes to altered timecard   records are saved when: A. The user clicks the save button.   B. The user switches pages in the timecard table. C. The user   switches to another employee. Delayed Save also permits the   user to click Cancel in order to revert to the original timecard   records and cancel recent changes. * Delayed Edit -   Timecard Records are loaded in View Only Mode. In Line Edit   Controls such as the Time Picker & Date Selection Tool   are not displayed. The User must click on 'Change' before   timecard records can be edited.     This mode enables delayed edit, which significantly reduces the time required to load the Timecard Grid, especially for clients connecting to the InfiniTime server over a higher latency WAN Connection with high bandwidth utilization. Users who observe delays while editing timecards, especially when switching from employee to employee and waiting for timecards to be displayed, may wish to enable Delayed Edit.    This is the recommended Timecard Edit Mode for customers with users accessing the InfiniTime Software over a higher latency / high bandwidth utilization WAN connection. The Delayed Save functionality and user friendly spreadsheet - like interface provide increased performance by reducing the number of round trips between the InfiniTime Client Machine and InfiniTime Server. | 

### Standard Timecard Editing Tools

Both the Company and Employee Timecard Tables include standard tools
for inserting, editing, and altering employee activity. Each item is outlined
below.

![](/img/image145.gif) -
Clicking the Insert Button will create a new timecard record which can
be manually entered to define working hours for a day. The insert button
behaves differently depending upon what is selected within the Timecard
Table when clicking insert. If no records exist, or if no timecard record
is highlighted new timecard records created with the Insert Button are
inserted with an In Punch at 8:00 AM and an out punch at 4:00 PM on the
first day of the selected date range. If a timecard record is highlighted
the punch will be inserted for the same day as the selected punch with
an In Punch and Out Punch set to the same time as the Out Punch on the
Highlighted record. For example:

Clicking Insert with a blank timecard yields:

![](/img/SW_CH11_NOTES_0001.gif)

Clicking Insert while the record above is highlighted yields:

![](/img/image145.gif)

![](/img/TCard009.png)  -
The Delete Button simply removes the highlighted record from the Timecard
Table. To remove an undesired record, simply click on it to highlight
the record in blue and click the delete button.

![](/img/Short_Break_Exeption.gif)  -
The exceptions button displays a detailed list of all exceptions occurring
on the highlighted day.  Each exception is displayed in a different
color. The exceptions button will only be displayed if an exception occurred
on the day associated with the highlighted timecard record.

![](/img/InLineEdit_ArrDep1.gif)

![](/img/SupReviewHistoryTable.gif)  -
Purge is useful for deleting punches which were inserted by accident or
are no longer useful. After clicking on the Purge button the user will
be prompted to enter a date range. All timecard records for the employee
during the selected date range will be deleted from the database after
clicking OK.

![](/img/SW_CH11_NOTES_0006.gif)  - Quick Punch
is one of the most used features within the Timecard table as it provides
users with the ability to insert timecard activity for multiple days.
Typical uses for quick punch include the following:

* Inserting a single punch for one or more employees
* Inserting punch pairs for one or more employees
* Inserting Other Activity (Sick, Vacation, Jury Duty, Etc)
* Inserting a Single Punch, Punch Pair, and / or Other Activity for
  One or More Days
* Inserting Other Amounts (Tips)
* Inserting Punches According to an Employee's Schedule

Quick
Punch Update Form - Overview

![](/img/TCard008.png).gif)

Description
- The description displays information regarding the employee for which
activity is being inserted and the employee inserting activity. This information
is recorded in the audit trail.

Note: The description information will not
reflect employees specified by the employee filter. Though an audit trail
entry will be recorded for each employee whose timecard activity is altered
by the quick punch transaction.

Date Range -
Select the date range that you wish to insert the Quick punches.  *If the Quick punch
is for one day only, then the start and end dates will be the same.*

Punch Type
- Use the drop down menu to select the type of punch, choose from regular
punch, schedule punch, single punch, or other activity.

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

Use Default Job - if this is checked
the punches will be posted using the default Job of the employee, if not
checked you can choose a Job using the magnify glass or typing in the
Job name to post those punches.

Use Default
Task - if this is checked the punches will be posted using the
default Task of the employee, if not checked you can choose a Task using
the magnify glass or typing in the Task name to post those punches.

Start Time
- Select the time that the quick punch will clock the employee in at.

End Time
- Select the time that the quick punch will clock the employee out at.

Duration
- The number of hours that will be totaled is shown here.

Add
Duplicate Punches - Unless this
box is checked InfiniTime
will compare the punches being inserted to those already in the database
when performing a Quick Punch. Any duplicate punches will be ignored.
For example the image below shows an employee working from 7:30 AM to
5:00 PM on 1/17/2008. If a supervisor were to attempt to insert a punch
on 1/17/2008 from 7:30 AM to 5:00 PM using quick punch then the punches
would not be inserted unless Add Duplicate Punches was checked.

![](/img/image16.gif)

Clock Out
if Clocked In - If this is checked it will only insert an out punch
for that day and in/out for the rest of the date range. This option is
only displayed when performing a single punch.

Weekday
Only â If this is checked it will only insert punches for weekdays
only and not the weekend, Saturday and Sunday.

Description
- This is an audit description of the insertion of punches.

![](/img/InLineEdit_MP2.gif) - The filter
button will allow you to add punches to multiple employees at a time.
 You can filter which employees will get the pair of punches either
by departments, groups, or by tagging multiple employees.

#### Using Quick Punch

Clicking on Quick Punch opens the Quick Punch Update form. Follow the
steps below to use the quick punch tool:

1. Select the desired Date Range. Pre-defined date ranges such as
   Current Pay Period, Last Pay Period, This Week, or Last Week can be
   used in addition to the Custom Date range option which provides the
   user with the ability to enter the date range manually.
2. Select the desired Punch Type. Regular Punch inserts a punch pair
   on each day within the date range. A punch pair consists of a Clock
   In and a Clock Out. Scheduled Punch inserts punches to match employee
   schedules. Single punch inserts only a single punch â either a clock
   in or clock out depending upon the current status of the employee.
   Other Activity can be used to insert Other Hours such Sick Time and
   Vacation Time or Other Amounts such as Tips.
3. Select the Start Time, End Time, and Duration as applicable.

Pre-defined date ranges are based upon policy settings for the employee
that is logged in. This is important to recognize when working with a
company with multiple pay periods. It is generally recommended to have
one administrator login for timecard editing for each pay period supported
by the company.

The Duration field is the number of hours which will be inserted for
each day in the date range. When inserting punches or other activity for
a date range, such as last week for example, do not enter the total number
of hours for the date range. The value in the duration field should be
a daily amount. IE: If an employee took five days of vacation last week
select the Last Week Date Range, the Other Activity Punch Type, and enter
8 as the daily duration. Entering 40 as the duration would insert 40 hours
of vacation per day.

INCORRECT

![](/img/DeleteButton-Normal.gif)

CORRECT

![](/img/ExceptionsButton-Normal.gif)

![](/img/CH7_Timecard8.gif) -
This feature allows the user to recalculate timecard activity for the
selected employee.  Recalculation should be done if you make any
changes to the policies, exceptions, schedules, or holidays.

![](/img/image147.gif)  -
Reviewing timecards is an optional, but recommended feature, whereby supervisors
can mark employee activity as reviewed after they have made any necessary
adjustments and confirmed the accuracy of employee timecards. In this
way payroll personnel know the timecards are ready for payroll processing.
To avoid the typical âpayday panicâ that occurs at payroll time it is
recommended that administrators review employee activity on a daily basis.
At the end of the payroll cycle the âEmployees Without Reviewed Timecardsâ
report can be run to list any employees who have not had their timecards
reviewed. Supervisors can then review these employees and run the report
again to confirm all employees have been reviewed. At this point payroll
can be processed.

Clicking on the review button opens the Review Time Record Update Form.
Select the date range for which timecards should be marked as reviewed
and click OK. By default the Review feature will only review activity
for a single employee. However the âRemove Filterâ button can be used
to specify additional employees.

![](/img/accesing_timecard_activity_table.gif)   -
The filter button, or Employee Filter, will allow you to filter employees
listed on the Timecard Table by individually selected employees, according
to their default department, and according to exceptions occurring during
the date range. This makes it easier for a supervisor to fix and edit
time cards by only displaying employees of interest.

![](/img/TCard003.png)
 - Often referred to as the âstoplightâ the record status indicator
provides information on the source of the punches (Orange), indicates
review status (Blue), and the presence of exceptions (Red). If exceptions
occur on a day the red status indicator will display. If the record has
been reviewed the blue status indicator will display. If the record has
been edited the orange status indicator will display. Conversely if the
orange status indicator is not displayed this indicates the punch is unedited
and was polled from a data collection terminal or from the Employee /
Punch modules.

![](/img/TCard007.png) - The
Grand Totals Row displays a grand total of employee hours for the specified
date range. It should be noted that the Grant Totals Row is always the
last row in the grid and will be displayed on the last page if there are
multiple pages of timecard activity. The Grand Total Row is displayed
only on the Company Timecard and is not include on the Employee Timecard
Table.

![](/img/Tcard05.gif) - The Schedule Column of the grid displays
the schedule or shift an employee worked on a specific day. If an employee
is assigned to multiple shifts the software will identify the shift the
employee is working based upon the shifts start time and grace periods
configured on the employee's policy.

### In Line Editing - General Use

In line editing is a simple and direct method of altering existing punches,
or adding new punches, which can be used to fix exceptions, insert missed
punches, and edit timecards as needed. For purposes of reviewing In Line
Editing, we will begin with an employee who has no timecard records for
the current pay period, and click Insert to create a single row of timecard
activity. If delayed save is enabled, Click on the Save Button to save
the new record.

No Record for Current
Pay Period:

![](/img/SW_CH11_NOTES_0002.gif)

A single timecard record created via Insert:

![](/img/TCard001.png)

To edit the timecard click in the field you wish to alter. Delete the
existing value using the backspace key or the delete key and type the
desired value. Dates must be entered with the MM/DD/YYYY format. Times
must be entered in the HH:MM format. Shortcut keys are also available
to simplify changing the date.

### Changing the Date

1. Click in the date field you wish to alter. This will make the field
   âactive.â When a field is active it will turn yellow.

Inactive
Fields
  Active Field

![](/img/PurgeButton-Normal.gif)
 ![](/img/Late-Departure-exception.gif)

2. The contents of the field will be highlighted. Press backspace
   or delete to remove the existing value. One of the shortcut keys listed
   below can also be used at this time.
3. Type the desired value.

 | Shortcut Key | Description | 
| --- | --- |
 | + | Adds one day to the displayed date | 
 | - | Subtracts one day from the displayed date | 
 | T | Sets the field to the Current Date | 
 | HOME | Sets the field to the Current Date | 
 | SHIFT + HOME | Sets the field to the January 1st of the respective year | 
 | SHIFT + END | Sets the field to the December 31st of the respective year | 

### Changing the Time

1. Click in the date field you wish to alter.
2. The contents of the field will be highlighted. Press backspace
   or delete to remove the existing value.
3. Type the desired value.
4. Press A or P to select the appropriate meridian after typing the
   time.

When making changes to timecards it is important to understand how InfiniTime
saves changes to time records. The primary method for saving changes to
a record is to simply click on another record in the table. However, this
is not possible when only a single record exists in the table. To save
your changes when there is only a single record in the timecard table,
simply press TAB multiple times until focus is removed from the current
record.

### Editing Missing Punches

#### Missed Out Punch:

![](/img/InLineEdit_3.jpg)

It is not uncommon for employees to forget to punch in or punch out
which results in a missed punch exception. When an employee misses an
out punch as shown above, the correct date and time can simply be entered
for the punch out. What if the employee missed the in punch as illustrated
below?

#### Missed In Punch:

![](/img/Purge_button.gif)

The date and time for the in punch can still simply be entered into
the Out Date and Out Time on the same record. InfiniTime
will automatically rearrange the punches in accordance with employee policy
settings while saving the data to the database.

### Editing Timecards â Pay Special Attention to the Selected Date Range

When editing punches for employees it is important to pay attention
to the selected date range. If the date of a punch is changed to a date
outside of the selected period the punch will be moved to the appropriate
date range. This can often give new users the impression that the punch
has disappeared even though the punch was moved to the correct time period.

### Editing Timecards â OvernightEmployees

For the purpose of calculating hours, InfiniTime
associates punch pairs with the day on which an employee punches in. Employee
Policies can be configured to associate Clock In Punches after a certain
time of day to the next date through use of the Clock In and Clock Out
Missed Punch Day Change Time settings. This concept is especially important
when working with overnight shifts on the first or last day of a pay period.
If an employee should miss a punch in this situation it is often best
to follow the steps below to identify the required changes. Additional
details on the Clock In and Clock Out Missed Punch Day Change Time can
be found in the[Policy Configuration Section](../Policies/Policy_Overview.md#pol84_OT_General_Tab) of this document.

1. Identify the schedule the employee was expected to work. In our
   example the employee works from 11:00 PM to 7:00 AM Monday â Friday.
   Punches expected for the Friday shift are Friday at 11:00 PM and Saturday
   at 7:00 AM.
2. Use a date range that spans the start or end date of the pay period.
   This will ensure relevant punches are displayed in the timecard table.
   For example, use This Month or Last Month instead of Current Pay Period
   or Last Pay Period. In this way punches up to the last day of the
   pay period and after the last day of the pay period will be displayed
   on the timecard table.

![](/img/image16.gif)

The above screen shot shows an employee with
a schedule of 11:00 PM to 7:00 AM Monday to Friday. Notice how the employee
only has 72 Hours for the pay period and no punches are shown on the 13th.
This is because the employee forgot to punch in on Friday causing their
out punch at 7:00 AM to be considered an In. Remember, punch pairs are
associated with the day an employee punches in. For this reason the punch
does not show under last pay period even though the punch was for Fridayâs
Shift. Changing the date range to This Month rather than Last Pay Period
displays all relevant punches.

![](/img/InLineEdit_2.jpg)

3. Look for the punches that resemble the schedule the employee
   was expected to work and identify those that are missing. The employee
   was expected to punch when arriving at work on Friday at 11:00 PM
   and when departing on Saturday Morning at 7:00 AM. The Saturday morning
   punch is present as shown below though the Friday Evening punch is
   missing.

![](/img/SW_CH11_NOTES_0007.gif)

4. Insert the missing punches by editing the Out Date and Out Times
   directly as shown in the image below.

![](/img/TCard014.png)

Remember, InfiniTime
will reorganize punches in chronological order and calculate hours appropriately
in accordance with employee policy settings while saving the entry. If
your employee's timecards do not pair as expected, the Missed Punch Threshold,
Clock In Missed Punch Day Change Time, or Clock Out Missed Punch Day Change
Time on the General Tab of the Overtime Rules Section on the Policy Update
Form are likely set incorrectly. Additional information can be found in
the [Policy
Configuration - Overtime Rules section](../Policies/Policy_Overview.md#pol84_OT_General_Tab) of this document.

![](/img/image16.jpg)

### Right Click Menu Introduction

In addition to the standard Timecard Editing tools InfiniTime
also offers menus available by right clicking on the timecard. These menus
include access to all of the standard tools in addition to advanced features
such as Calculation Override, Change Schedule, Timecard Notes, and Supervisor
Review History. It is important to recognize that the Right Click Menu
is context sensitive and will include different items based on where the
user right clicks on a given timecard record as well as whether the timecard
record has exceptions and / or missing punches. Additional Details are
outlined in the [Right Click
Menu - Editing Exceptions and More](TimecardEditing.md#tim16_Right_Click_Menu_-_Editing_Exceptions_and_More) section of this document.

![](/img/employee-timecard-Button.gif)

Insert Punch Pair - Inserts a new punch pair into the Timecard
Table. The Insert Punch Pair Right Click Menu Option is functionally identical
to the Insert Button.

Delete In Punch - Deletes the In Punch for the respective
punch pair from the Timecard Table.

Delete Out Punch
- Deletes the Out Punch for the respective punch pair from the
Timecard Table.

Delete Punch Pair
- Deletes the punch pair from the timecard table. The Delete Punch
Pair Right Click Menu option is functionally identical to the Delete Button.

Delete All Punches
And Insert Schedule Punches -
Selecting this option will delete the punches for the day and insert the
punches that are scheduled for that employee in that day.

Delete All Punches
For Day - Selecting this option will delete the punches for that
specific day.

Toggle Calc Override
- This option enables and / or disables Calculation Override. When
enabled, calculation override ignores hour totals calculated by InfiniTime
and allows the user to manually enter Regular, Overtime 1, Overtime 2,
Overtime 3, and Overtime 4 hours.

Toggle Supervisor
Review - This option enables
and / or disables Supervisor review for the selected timecard record.
When a record is reviewed a blue indicator will be displayed to the left
of the record. Supervisor review is useful when multiple supervisors are
responsible for editing employee timecards and is intended to indicate
a record has been reviewed by an employee's supervisor and has been approved.

Wage
Override - Provides convenient
access to the Wages Update Form, which can also be accessed from the Wages
Section of the Employee Update Form for individual employees. In this
way, supervisors may define alternate wages for a specific date range.
For convenience, the Employee Wage Update form will be automatically populated
with the Date Range set on the Timecard Table when using Wage Override.
An example of wage override is shown below.

1.
John Smith was called in to perform emergency maintenance on a Production
Server on 4/16/2013.

![](/img/image77.gif)

2. Per John Smith's employment package, he
is entitled to $12 / Hour base instead of his usual $10 wage if he is
called in outside of business hours. To edit the wage, right click on
any timecard record in the grid and click Wage Override. The Employee
Wage Override Table will be displayed.

![](/img/image17.jpg)

3. Click Insert to open the Employee Wage
Update Form. Enter the desired Department, Pay Method, Amount, and Valid
From / To Date Range. Notice that the Valid From and Valid To Date range
will be pre-filled to match the Date Range set on the Company Timecard.
Click OK to save the Wage Override Entry after entering the Department,
Pay Method, and Amount. It is important to note that Job Costing Details
(Department, Job, and Task) are not required fields. If no department
is specified, the wage will be applied to all timecard records during
the specified date range.

![](/img/TCard010.png)

4. Notice how the wage for Information Technology
Hours on 4/16/2013 is set to $12.00 / hour. The Overtime One Hourly Wage
is automatically calculated as $18 - a 50% increase on top of the base
wage based on the Overtime 1 Wage Settings.

![](/img/Timecards_Button.gif)

Change
Schedule - Selecting this option will allow you to change the
employee's schedule for that day. Altering the schedule to match the hours
worked by the employee or simply removing the schedule altogether will
remove the exception.

![](/img/TCard010.png)

Schedule
Day Off - Opens the Schedule Day off Update Form Days which
allows the user to schedule an employee to be absent for a day. When a
day off is scheduled employees will not receive exceptions on the Scheduled
Day Off. Days Off are a useful feature for companies who utilize the Points
System and wish to ensure employees who are approved for an absence will
not be penalized. Refer to the [Scheduling
- Days Off section of this document](../Scheduling/Scheduling.md#sch32_New_Day_Off_-_Scheduling_a_Day_Off) for more information.

View
List of Day(s) Off - Displays the Schedule Day Off Table which
lists all days that have been scheduled off for the employee.

Audit Trail
- Selecting this option will open the Audit Trail Table which displays
detailed information about changes made to employee timecards such as
who made changes to a punch and when.

Exceptions
- Displays a list of all exceptions occurring on the record.

Note - Permits
entry of a comment or paragraph and associates the comment with a timecard
punch. While this principle is similar to the operation of existing the
Audit Trail system, Timecard notes are not mandatory and are only entered
as deemed necessary by supervisors. Additional details on the use of [Timecard
Notes can be found in the Timecard Notes Section](TimecardEditing.md#tim43_Timecard_Notes:_Overview) of this document.

Purge -
Selecting this option will open the Purge Time Record Update Form which
can be used to delete all timecard activity within a specific date range.

Quick Punch
- Quick Punch inserts identical punches over a specified date range.  Selecting
this option will open the Quick Punch Window.

Re-Calculate
- Recalculates timecard activity, applying current policy rules, schedule
settings, and other related settings to Employee Punches in the InfiniTime Software.

Review
- Selecting this option will open the Supervisor Review Window which allows
the user to select one or more employees for review of their timecard
activity.

### Right Click Menu - Editing Exceptions and More

The Timecard Activity window displays employee
exceptions within the detail view. Employee activity will be highlighted
when an exception exists. Colors vary according to the exception type.
Employee Supervisors have the option to edit employee activity in order
to fix exceptions, mark the employees time in order to ignore existing
exceptions, or simply take note of an employeeâs performance.

![](/img/image17.jpg)

### Fixing a Missed Punch Exception

![](/img/FilterButton-Normal.gif)

The Missed Punch Exception shows in the
activity grid as a RED block. Punch information will also be missing from
the block.

* Right click on the missed punch
  to bring up a list of commands to fix the exception.

![](/img/image72.gif)

Delete All Punches
And Insert Schedule Punches - Selecting this option will delete
the punches for the day and insert the punches that are scheduled for
that employee in that day.

Delete All Punches
For Day - Selecting this option will delete the punches for that
specific day.

Insert Punch Pair
- Selecting this option will allow you to insert the missing punch.

Insert First Scheduled
In Punch - Selecting this option will insert the first scheduled
In punch,  do this if the exception is in the first In punch.

Insert Last Scheduled
Out Punch - Selecting this option will insert the last scheduled
out punch, do this if the exception is in the last out punch.

Change Schedule
- Selecting this option will allow you to change the employee's schedule
for that day. Altering the schedule to match the hours worked by the employee
or simply removing the schedule altogether will remove the exception.

Toggle Calc Override
- This option enables and / or disables Calculation Override. When enabled,
calculation override ignores hour totals calculated by InfiniTime and allows the user to
manually enter Regular, Overtime 1, Overtime 2, Overtime 3, and Overtime
4 hours.

Toggle Supervisor
Review - This option enables and / or disables Supervisor review
for the selected timecard record. When a record is reviewed a blue indicator
will be displayed to the left of the record. Supervisor review is useful
when multiple supervisors are responsible for editing employee timecards
and is intended to indicate a record has been reviewed by an employee's
supervisor and has been approved.

Wage Override
- Provides convenient access to the Wages Update Form, which can
also be accessed from the Wages Section of the Employee Update Form for
individual employees. In this way, supervisors may define alternate wages
for a specific date range. For convenience, the Employee Wage Update form
will be automatically populated with the Date Range set on the Timecard
Table when using Wage Override.

Change Schedule
- Selecting this option will allow you to change the employee's schedule
for that day. Altering the schedule to match the hours worked by the employee
or simply removing the schedule altogether will remove the exception.

Schedule
Day Off - Opens the Schedule Day off Update Form Days which
allows the user to schedule an employee to be absent for a day. When a
day off is scheduled employees will not receive exceptions on the Scheduled
Day Off. Days Off are a useful feature for companies who utilize the Points
System and wish to ensure employees who are approved for an absence will
not be penalized. Refer to the [Scheduling
- Days Off section of this document](../Scheduling/Scheduling.md#sch32_New_Day_Off_-_Scheduling_a_Day_Off) for more information.

View
List of Day(s) Off - Displays the Schedule Day Off Table which
lists all days that have been scheduled off for the employee.

Audit Trail
- Selecting this option will open the Audit Trail Table which displays
detailed information about changes made to employee timecards such as
who made changes to a punch and when.

Exceptions
- Displays a list of all exceptions occurring on the record.

Note - Permits
entry of a comment or paragraph and associates the comment with a timecard
punch. While this principle is similar to the operation of existing the
Audit Trail system, Timecard notes are not mandatory and are only entered
as deemed necessary by supervisors. Additional details on the use of [Timecard
Notes can be found in the Timecard Notes Section](TimecardEditing.md#tim43_Timecard_Notes:_Overview) of this document.

Purge -
Selecting this option will open the Purge Time Record Update Form which
can be used to delete all timecard activity within a selected date range.

Quick Punch
- Quick Punch inserts identical punches over a specified date range.  Selecting
this option will bring up the Quick punch Window.

Re-Calculate
- Recalculates timecard activity, applying current policy rules, schedule
settings, and other relative settings to Employee Punches in the InfiniTime Software.

Review
- Selecting this option will open the Supervisor Review Window which allows
the user to select one or more employees for review of their timecard
activity.

Alternatively, you may simply wish to directly
edit the employeeâs punch by clicking in the field you wish to change,
deleting the present information, and entering the desired punch time.

Fixing an Absent Exception

![](/img/image18.jpg)

When an employee is absent the absent exception
is displayed within the employee timecard activity grid and is recognizable
by a blank entry with the word âAbsentâ in red lettering. This exception
is only triggered if you have a schedule set and the employee failed to
report to work or forgot to punch in and out on that scheduled day.

* Right click on the Absent to bring
  up a list of commands to fix the exception.

![](/img/Unapproved_OT.gif)

Change
Schedule - Selecting this option will
allow you to change the employee's schedule for that day. Altering the
schedule to match the hours worked by the employee or  simply removing
the schedule altogether will remove the exception.

Schedule Day Off - Opens the Schedule
Day off Update Form Days which allows the user to schedule an employee
to be absent for a day. When a day off is scheduled employees will not
receive exceptions on the Scheduled Day Off. Days Off are a useful feature
for companies who utilize the Points System and wish to ensure employees
who are approved for an absence will not be penalized. Refer to the [Scheduling
- Days Off section of this document](../Scheduling/Scheduling.md#sch32_New_Day_Off_-_Scheduling_a_Day_Off) for more information.

View
List of Day(s) Off - Selecting this option displays a list of all
days off set for the employee.

Insert
Punch Pair - Selecting this option will allow you to insert a pair
of punches for that day.

Insert
Other Activity - Selecting this option will permit the entry of
other activity hours for this day, such as Sick time, Vacation, PTO, or
any other activity.

Insert
Scheduled Punches - Selecting this option will insert scheduled
punches for the specified day as defined in the employeeâs schedule.

Audit
Trail - Selecting this option will open the Audit Trail Table which
displays detailed information about changes made to employee timecards
such as who made changes to a punch and when.

Exceptions
- Displays a list of all exceptions occurring on the record.

Purge -
Selecting this option will open the Purge Time Record Update Form which
can be used to delete all timecard activity within a selected date range.

Quick Punch -
Quick Punch inserts identical punches over a specified date range.  Selecting
this option will bring up the Quick punch Window.

Re-Calculate
- Recalculates timecard activity, applying current policy rules, schedule
settings, and other relative settings to Employee Punches in the InfiniTime Software.

Review
- Selecting this option will open the Supervisor Review Window which allows
the user to select one or more employees for review of their timecard
activity.

Fixing
the Early and Early Departure Exceptions

Early Exception:

![](/img/Purge_button.gif)

Early Departure Exception:

![](/img/image2.gif)

The Early Exception is triggered by employees
punching in prior to the start time of their schedule during the Early
Clock Grace Period. Similarly, the Early Departure Exception is triggered
when employees punch out prior to the end time of their schedule during
the Early Clock Out Grace Period. These exceptions are only triggered
if a schedule is present for the respective date and the employee punched
in or out during the Early Grace Period as defined on the employee's policy.

* Right click on the Early Punch
  to bring up a list of commands to fix the exception.

![](/img/TCard002.png)

Insert Punch Pair
- Selecting this option will insert a punch pair for the specific day.

Delete In Punch
- Selecting this option will delete the in punch for the day.

Delete Punch Pair
- Selecting this option will delete the punch pair.

Delete All Punches
For Day - Selecting this option will delete all the punches for
that specific day.

Toggle Calc Override
- This option enables and / or disables Calculation Override. When enabled,
calculation override ignores hour totals calculated by InfiniTime and allows the user to
manually enter Regular, Overtime 1, Overtime 2, Overtime 3, and Overtime
4 hours.

Toggle Supervisor
Review - This option enables and / or disables Supervisor review
for the selected timecard record. When a record is reviewed a blue indicator
will be displayed to the left of the record. Supervisor review is useful
when multiple supervisors are responsible for editing employee timecards
and is intended to indicate a record has been reviewed by an employee's
supervisor and has been approved.

Wage Override - Provides convenient access to the Wages
Update Form, which can also be accessed from the Wages Section of the
Employee Update Form for individual employees. In this way, supervisors
may define alternate wages for a specific date range. For convenience,
the Employee Wage Update form will be automatically populated with the
Date Range set on the Timecard Table when using Wage Override.

Change Schedule
- Selecting this option will allow you to change the employee's schedule
for that day. Altering the schedule to match the hours worked by the employee
or simply removing the schedule altogether will remove the exception.

Delete All Punches
And Insert Scheduled Punches - Selecting this option will delete
the punches for the day and insert the punches that are scheduled for
that employee in that day.

Schedule Day Off
- Opens the Schedule Day off Update Form Days which allows the user to
schedule an employee to be absent for a day. When a day off is scheduled
employees will not receive exceptions on the Scheduled Day Off. Days Off
are a useful feature for companies who utilize the Points System and wish
to ensure employees who are approved for an absence will not be penalized.
Refer to the [Scheduling
- Days Off section of this document](../Scheduling/Scheduling.md#sch32_New_Day_Off_-_Scheduling_a_Day_Off) for more information.

View List of Day(s)
Off - Displays the Schedule Day Off Table which lists all days
that have been scheduled off for the employee.

Audit Trail
- Selecting this option will open the Audit Trail Table which displays
detailed information about changes made to employee timecards such as
who made changes to a punch and when.

Exceptions
- Displays a list of all exceptions occurring on the record.

Note - Permits
entry of a comment or paragraph and associates the comment with a timecard
punch. While this principle is similar to the operation of existing the
Audit Trail system, Timecard notes are not mandatory and are only entered
as deemed necessary by supervisors. Additional details on the use of [Timecard Notes can be found
in the Timecard Notes Section of this document](TimecardEditing.md#tim43_Timecard_Notes:_Overview).

Purge -
Selecting this option will open the Purge Time Record Update Form which
can be used to delete all timecard activity within a selected date range.

Quick Punch
- Quick Punch inserts identical punches over a specified date range.  Selecting
this option will bring up the Quick punch Window.

Re-Calculate
- Recalculates timecard activity, applying current policy rules, schedule
settings, and other relative settings to Employee Punches in the InfiniTime Software.

Review
- Selecting this option will open the Supervisor Review Window which allows
the user to select one or more employees for review of their timecard
activity.

Alternatively, you may simply wish to directly
edit the employeeâs punch by clicking in the field you wish to change,
deleting the present information, and entering the desired punch time.

Fixing a Late Exception

Tardy

![](/img/Employee-Button.gif)

Late Departure

![](/img/InLineEdit_MP4_NoDelSav.gif)

The Late Exception occurs when an employee
clocks in after their scheduled time or clocks out after they are scheduled
to leave and is recognizable by a Fuchsia field. These exceptions are
only triggered if a schedule is present for that day and the employee
punched in or out late according to schedule grace periods as defined
in the employeeâs policy.

* Right click on the Late Punch to
  bring up a list of commands to fix the exception.

![](/img/SW_CH11_NOTES_0004.gif)

Insert Punch Pair
- Selecting this option will insert a punch pair for the specific day.

Delete In Punch
- Selecting this option will delete the in punch for respective timecard
record.

Delete Punch Pair
- Selecting this option will delete the punch pair.

Delete All Punches
For Day - Selecting this option will delete all the punches for
that specific day.

Toggle Calc Override
- This option enables and / or disables Calculation Override. When enabled,
calculation override ignores hour totals calculated by InfiniTime and allows the user to
manually enter Regular, Overtime 1, Overtime 2, Overtime 3, and Overtime
4 hours.

Toggle Supervisor
Review - This option enables and / or disables Supervisor review
for the selected timecard record. When a record is reviewed a blue indicator
will be displayed to the left of the record. Supervisor review is useful
when multiple supervisors are responsible for editing employee timecards
and is intended to indicate a record has been reviewed by an employee's
supervisor and has been approved.

Wage Override
- Provides convenient access to the Wages Update Form, which can
also be accessed from the Wages Section of the Employee Update Form for
individual employees. In this way, supervisors may define alternate wages
for a specific date range. For convenience, the Employee Wage Update form
will be automatically populated with the Date Range set on the Timecard
Table when using Wage Override.

Change Schedule
- Selecting this option will allow you to change the employee's schedule
for that day. Altering the schedule to match the hours worked by the employee
or simply removing the schedule altogether will remove the exception.

Delete All Punches
And Insert Scheduled Punches - Selecting this option will delete
the punches for the day and insert the punches that are scheduled for
that employee on the respective date.

Schedule Day Off
- Opens the Schedule Day off Update Form Days which allows the user to
schedule an employee to be absent for a day. When a day off is scheduled
employees will not receive exceptions on the Scheduled Day Off. Days Off
are a useful feature for companies who utilize the Points System and wish
to ensure employees who are approved for an absence will not be penalized.
Refer to the [Scheduling
- Days Off Section](../Scheduling/Scheduling.md#sch32_New_Day_Off_-_Scheduling_a_Day_Off) of this document for more information.

View List of Day(s)
Off - Displays the Schedule Day Off Table which lists all days
that have been scheduled off for the employee.

Audit Trail
- Selecting this option will open the Audit Trail Table which displays
detailed information about changes made to employee timecards such as
who made changes to a punch and when.

Exceptions
- Displays a list of all exceptions occurring on the record.

Note - Permits
entry of a comment or paragraph and associates the comment with a timecard
punch. While this principle is similar to the operation of existing the
Audit Trail system, Timecard notes are not mandatory and are only entered
as deemed necessary by supervisors. Additional details on the use of [Timecard
Notes can be found in the Timecard Notes Section of this document](TimecardEditing.md#tim43_Timecard_Notes:_Overview).

Purge -
Selecting this option will open the Purge Time Record Update Form which
can be used to delete all timecard activity within a selected date range.

Quick Punch
- Quick Punch inserts identical punches over a specified date range.  Selecting
this option will bring up the Quick punch Window.

Re-Calculate
- Recalculates timecard activity, applying current policy rules, schedule
settings, and other relative settings to Employee Punches in the InfiniTime Software.

Review
- Selecting this option will open the Supervisor Review Window which allows
the user to select one or more employees for review of their timecard
activity.

Alternatively, you may simply wish to directly
edit the employeeâs punch by clicking in the field you wish to change,
deleting the present information, and entering the desired punch time.

Fixing Outside of
Schedule Exception

![](/img/Tardy_Exception.gif)

The Outside of Schedule Exception occurs
when an employee punches outside of their scheduled grace periods as defined
on the employee's policy.  This exception is recognizable by a Yellow
Field as shown above.

* Right click on the Outside of Schedule
  Punch to bring up a list of commands to fix the exception.

![](/img/SupReviewHistoryTable.gif)

Insert Punch Pair
- Selecting this option will insert a punch pair for the specific day.

Delete In Punch
- Selecting this option will delete the in punch for respective timecard
record.

Delete Punch Pair
- Selecting this option will delete the punch pair.

Delete All Punches
For Day - Selecting this option will delete all the punches for
that specific day.

Toggle Calc Override
- This option enables and / or disables Calculation Override. When enabled,
calculation override ignores hour totals calculated by InfiniTime and allows the user to
manually enter Regular, Overtime 1, Overtime 2, Overtime 3, and Overtime
4 hours.

Toggle Supervisor
Review - This option enables and / or disables Supervisor review
for the selected timecard record. When a record is reviewed a blue indicator
will be displayed to the left of the record. Supervisor review is useful
when multiple supervisors are responsible for editing employee timecards
and is intended to indicate a record has been reviewed by an employee's
supervisor and has been approved.

Wage Override
- Provides convenient access to the Wages Update Form, which can
also be accessed from the Wages Section of the Employee Update Form for
individual employees. In this way, supervisors may define alternate wages
for a specific date range. For convenience, the Employee Wage Update form
will be automatically populated with the Date Range set on the Timecard
Table when using Wage Override.

Change Schedule
- Selecting this option will allow you to change the employee's schedule
for that day. Altering the schedule to match the hours worked by the employee
or simply removing the schedule altogether will remove the exception.

Delete All Punches
And Insert Scheduled Punches - Selecting this option will delete
the punches for the day and insert the punches that are scheduled for
that employee on the respective date.

Schedule Day Off
- Opens the Schedule Day off Update Form Days which allows the user to
schedule an employee to be absent for a day. When a day off is scheduled
employees will not receive exceptions on the Scheduled Day Off. Days Off
are a useful feature for companies who utilize the Points System and wish
to ensure employees who are approved for an absence will not be penalized.
Refer to the [Scheduling
- Days Off Section](../Scheduling/Scheduling.md#sch32_New_Day_Off_-_Scheduling_a_Day_Off) of this document for more information.

View List of Day(s)
Off - Displays the Schedule Day Off Table which lists all days
that have been scheduled off for the employee.

Audit Trail
- Selecting this option will open the Audit Trail Table which displays
detailed information about changes made to employee timecards such as
who made changes to a punch and when.

Exceptions
- Displays a list of all exceptions occurring on the record.

Note - Permits
entry of a comment or paragraph and associates the comment with a timecard
punch. While this principle is similar to the operation of existing the
Audit Trail system, Timecard notes are not mandatory and are only entered
as deemed necessary by supervisors. Additional details on the use of [Timecard
Notes can be found in the Timecard Notes Section](TimecardEditing.md#tim43_Timecard_Notes:_Overview) of this document.

Purge -
Selecting this option will open the Purge Time Record Update Form which
can be used to delete all timecard activity within a selected date range.

Quick Punch
- Quick Punch inserts identical punches over a specified date range.  Selecting
this option will bring up the Quick punch Window.

Re-Calculate
- Recalculates timecard activity, applying current policy rules, schedule
settings, and other relative settings to Employee Punches in the InfiniTime Software.

Review
- Selecting this option will open the Supervisor Review Window which allows
the user to select one or more employees for review of their timecard
activity.

Alternatively, you may simply wish to directly edit the employeeâs punch
by clicking in the field you wish to change, deleting the present information,
and entering the desired punch time. In most cases, if the employee was
approved to work an alternate schedule, the best way to fix an Outside
of Schedule Exception is to alter the schedule to match the working period
the employee was approved to work. In this way, exceptions would then
be generated based on the employee's approved schedule in comparison with
the employee's actual worked times.

Fixing Short Break Exception

![](/img/ReCalcButton-Normal.gif)

The Short Break Exception
occurs when an employee takes a shorter break than scheduled and is recognizable
by a Brown Field. The short break exception requires breaks to be scheduled
in order to report short breaks.

![](/img/Tcard06.gif)

Insert Punch Pair
- Selecting this option will insert a punch pair for the specific day.

Delete Out Punch
- Selecting this option will delete the out punch for the day.

Delete Punch Pair
- Selecting this option will delete the punch pair.

Delete All Punches
For Day - Selecting this option will delete all the punches for
that specific day.

Toggle
Calc Override - This option enables and / or disables Calculation
Override. When enabled, calculation override ignores hour totals calculated
by InfiniTime and allows
the user to manually enter Regular, Overtime 1, Overtime 2, Overtime 3,
and Overtime 4 hours.

Toggle Supervisor
Review - This option enables and / or disables Supervisor review
for the selected timecard record. When a record is reviewed a blue indicator
will be displayed to the left of the record. Supervisor review is useful
when multiple supervisors are responsible for editing employee timecards
and is intended to indicate a record has been reviewed by an employee's
supervisor and has been approved.

Wage Override
- Provides convenient access to the Wages Update Form, which can
also be accessed from the Wages Section of the Employee Update Form for
individual employees. In this way, supervisors may define alternate wages
for a specific date range. For convenience, the Employee Wage Update form
will be automatically populated with the Date Range set on the Timecard
Table when using Wage Override.

Change Schedule
- Selecting this option will allow you to change the employee's schedule
for that day. Altering the schedule to match the hours worked by the employee
or simply removing the schedule altogether will remove the exception.

Delete All Punches
And Insert Scheduled Punches - Selecting this option will delete
the punches for the day and insert the punches that are scheduled for
that employee in that day.

Schedule Day Off
- Opens the Schedule Day off Update Form Days which allows the user to
schedule an employee to be absent for a day. When a day off is scheduled
employees will not receive exceptions on the Scheduled Day Off. Days Off
are a useful feature for companies who utilize the Points System and wish
to ensure employees who are approved for an absence will not be penalized.
Refer to the [Scheduling
- Days Off Section](../Scheduling/Scheduling.md#sch32_New_Day_Off_-_Scheduling_a_Day_Off) of this document for more information.

View List of Day(s)
Off - Displays the Schedule Day Off Table which lists all days
that have been scheduled off for the employee.

Audit Trail
- Selecting this option will open the Audit Trail Table which displays
detailed information about changes made to employee timecards such as
who made changes to a punch and when.

Exceptions
- Displays a list of all exceptions occurring on the record.

Purge -
Selecting this option will open the Purge Time Record Update Form which
can be used to delete all timecard activity within a selected date range.

Quick Punch
- Quick Punch inserts identical punches over a specified date range.  Selecting
this option will bring up the Quick punch Window.

Re-Calculate
- Recalculates timecard activity, applying current policy rules, schedule
settings, and other relative settings to Employee Punches in the InfiniTime Software.

Review
- Selecting this option will open the Supervisor Review Window which allows
the user to select one or more employees for review of their timecard
activity.

Fixing Long Break Exception

![](/img/SoftwareOverview_001_Btn1_Company.png)

The Long Break Exception
occurs when an employee takes a longer break than scheduled and is recognizable
by a Chocolate Field. The long break exception requires breaks to be scheduled
in order to report long breaks.

![](/img/TCard006.png)

Insert Punch Pair
- Selecting this option will insert a punch pair for the specific day.

Delete In Punch
- Selecting this option will delete the in punch for respective timecard
record.

Delete Punch Pair
- Selecting this option will delete the punch pair.

Delete All Punches
For Day - Selecting this option will delete all the punches for
that specific day.

Toggle Calc Override
- This option enables and / or disables Calculation Override. When enabled,
calculation override ignores hour totals calculated by InfiniTime and allows the user to
manually enter Regular, Overtime 1, Overtime 2, Overtime 3, and Overtime
4 hours.

Toggle Supervisor
Review - This option enables and / or disables Supervisor review
for the selected timecard record. When a record is reviewed a blue indicator
will be displayed to the left of the record. Supervisor review is useful
when multiple supervisors are responsible for editing employee timecards
and is intended to indicate a record has been reviewed by an employee's
supervisor and has been approved.

Wage Override
- Provides convenient access to the Wages Update Form, which can
also be accessed from the Wages Section of the Employee Update Form for
individual employees. In this way, supervisors may define alternate wages
for a specific date range. For convenience, the Employee Wage Update form
will be automatically populated with the Date Range set on the Timecard
Table when using Wage Override.

Change Schedule
- Selecting this option will allow you to change the employee's schedule
for that day. Altering the schedule to match the hours worked by the employee
or simply removing the schedule altogether will remove the exception.

Delete All Punches
And Insert Scheduled Punches - Selecting this option will delete
the punches for the day and insert the punches that are scheduled for
that employee on the respective date.

Schedule Day Off
- Opens the Schedule Day off Update Form Days which allows the user to
schedule an employee to be absent for a day. When a day off is scheduled
employees will not receive exceptions on the Scheduled Day Off. Days Off
are a useful feature for companies who utilize the Points System and wish
to ensure employees who are approved for an absence will not be penalized.
Refer to the [Scheduling
- Days Off Section](../Scheduling/Scheduling.md#sch32_New_Day_Off_-_Scheduling_a_Day_Off) of this document for more information.

View List of Day(s)
Off - Displays the Schedule Day Off Table which lists all days
that have been scheduled off for the employee.

Audit Trail
- Selecting this option will open the Audit Trail Table which displays
detailed information about changes made to employee timecards such as
who made changes to a punch and when.

Exceptions
- Displays a list of all exceptions occurring on the record.

Note - Permits
entry of a comment or paragraph and associates the comment with a timecard
punch. While this principle is similar to the operation of existing the
Audit Trail system, Timecard notes are not mandatory and are only entered
as deemed necessary by supervisors. Additional details on the use of [Timecard
Notes can be found in the Timecard Notes Section](TimecardEditing.md#tim43_Timecard_Notes:_Overview) of this document.

Purge -
Selecting this option will open the Purge Time Record Update Form which
can be used to delete all timecard activity within a selected date range.

Quick Punch
- Quick Punch inserts identical punches over a specified date range.  Selecting
this option will bring up the Quick punch Window.

Re-Calculate
- Recalculates timecard activity, applying current policy rules, schedule
settings, and other relative settings to Employee Punches in the InfiniTime Software.

Review
- Selecting this option will open the Supervisor Review Window which allows
the user to select one or more employees for review of their timecard
activity.

Approving and Un-approving
Overtime

![](/img/Missed-Punch-Exception.gif)

As part of the InfiniTime Policy Configuration, it
is possible to require all overtime hours for specific Overtime Buckets
such as OT One, OT Two, OT Three, or OT Four as designated by policy settings
to require supervisor approval. Unapproved Overtime Hours will not be
exported to payroll. Additionally unapproved Overtime Hours are displayed
on all employee timecard reports trailing a forward slash (/) to indicate
the hours are unapproved. Supervisors may right click unapproved Overtime
Hours, displayed in Red Text on the Company Timecard as shown in the image
above, and approve the hours using the Approve / Unapprove OT Right Click
Menu Options.

![](/img/image55.gif)

Insert Punch Pair
- Selecting this option will insert a punch pair for the specific day.

Delete In Punch
- Selecting this option will delete the in punch for the respective punch
pair.

Delete Out Punch
- Selecting this option will delete the out punch for the respective punch
pair.

Delete Punch Pair
- Selecting this option will delete the punch pair.

Delete All Punches
And Insert Scheduled Punches - Selecting this option will delete
the punches for the day and insert the punches that are specified by the
employeeâs schedule for that day.

Delete All Punches
For Day - Selecting this option will delete all the punches for
that specific day.

Toggle Calc Override
- This option enables and / or disables Calculation Override. When enabled,
calculation override ignores hour totals calculated by InfiniTime and allows the user to
manually enter Regular, Overtime 1, Overtime 2, Overtime 3, and Overtime
4 hours.

Toggle Supervisor
Review - This option enables and / or disables Supervisor review
for the selected timecard record. When a record is reviewed a blue indicator
will be displayed to the left of the record. Supervisor review is useful
when multiple supervisors are responsible for editing employee timecards
and is intended to indicate a record has been reviewed by an employee's
supervisor and has been approved.

Wage Override
- Provides convenient access to the Wages Update Form, which can
also be accessed from the Wages Section of the Employee Update Form for
individual employees. In this way, supervisors may define alternate wages
for a specific date range. For convenience, the Employee Wage Update form
will be automatically populated with the Date Range set on the Timecard
Table when using Wage Override.

Approve/Unapprove
 OT One - The Approve / Unapprove OT One right click menu
option will toggle the Approval Status for Overtime One Hours on the respective
punch pair. For example, if OT One Hours on the respective punch pair
are Unapproved (Displayed in red text) then Approve/Unnapprove OT One
will approve the OT One Hours. Alternatively, if OT One Hours on the respective
punch pair are Approved (Displayed in green text) then Approve/Unnapprove
OT One will unapprove the OT One Hours.

Approve/Unapprove
 OT Two - The Approve / Unapprove OT One right click menu
option will toggle the Approval Status for Overtime One Hours on the respective
punch pair. For example, if OT One Hours on the respective punch pair
are Unapproved (Displayed in red text) then Approve/Unnapprove OT One
will approve the OT One Hours. Alternatively, if OT One Hours on the respective
punch pair are Approved (Displayed in green text) then Approve/Unnapprove
OT One will unapprove the OT One Hours.

Change Schedule
- Selecting this option will allow you to change the employee's schedule
for that day. Altering the schedule to match the hours worked by the employee
or simply removing the schedule altogether will remove the exception.

 Schedule
Day Off - Opens the Schedule Day off Update Form Days which allows
the user to schedule an employee to be absent for a day. When a day off
is scheduled employees will not receive exceptions on the Scheduled Day
Off. Days Off are a useful feature for companies who utilize the Points
System and wish to ensure employees who are approved for an absence will
not be penalized. Refer to [Days Off](../../CH5_Days_Off.md)
for more information.

View List of Day(s)
Off - Displays the Schedule Day Off Table which lists all days
that have been scheduled off for the employee.

Audit Trail
- Selecting this option will open the Audit Trail Table which displays
detailed information about changes made to employee timecards such as
who made changes to a punch and when.

Exceptions
- Displays a list of all exceptions occurring on the record.

Note - Permits
entry of a comment or paragraph and associates the comment with a timecard
punch. While this principle is similar to the operation of existing the
Audit Trail system, Timecard notes are not mandatory and are only entered
as deemed necessary by supervisors. Additional details on the use of [Timecard
Notes can be found in the Timecard Notes Section](TimecardEditing.md#tim43_Timecard_Notes:_Overview) of this document.

Purge -
Selecting this option will open the Purge Time Record Update Form which
can be used to delete all timecard activity within a selected date range.

Quick Punch
- Quick Punch inserts identical punches over a specified date range.  Selecting
this option will bring up the Quick punch Window.

Re-Calculate
- Recalculates timecard activity, applying current policy rules, schedule
settings, and other relative settings to Employee Punches in the InfiniTime Software.

Review
- Selecting this option will open the Supervisor Review Window which allows
the user to select one or more employees for review of their timecard
activity.

### Related Tools - History and Undo Tools for Quick Punch, Purge, and Review

In some cases users may find it necessary to undo a Quick Punch, Purge,
or Review action. For this reason History and Undo Tools have been provided
and are available under the âTools â History and Undo Toolsâ menu.

Purge History
â Lists all Purge Actions performed. Includes the date and time
the purge was performed in addition to the employee performing the Purge
action.

Quick Punch History
- Lists all Quick Punch Actions performed. Includes the date and
time the Quick Punch was performed in addition to the employee performing
the Quick Punch action.

Supervisor Review
History - Lists all Review Actions performed. Includes the date
and time the Review was performed in addition to the employee performing
the Review action.

# In Line Timecard Editing -By Timecard Editing Mode

As detailed above, in the [Timecard
Editing Modes Section of this document](TimecardEditing.md#tim04_Timecard_Editing_Modes), Timecard Tables within InfiniTime offer different editing
modes intended for organizations with varying levels of network performance.
By default, on new installations of InfiniTime
'Delayed Save on Timecard Editors'  is enabled and 'Delayed Edit
on Timecard Editors' is disabled. In this way, all company timecard tables
include the Delayed Save Functionality out of the box. This is the recommended
editing mode for efficiency and performance reasons as Delayed Save reduces
the number of transactions exchanged between InfiniTime
Client Machines and the InfiniTime
Server during timecard editing. Additionally, Delayed Save permits the
InfiniTime Timecard tables
to function like a spreadsheet permitting multiple edits and alterations
to employee timecard records before saving the alterations and calculating
totals. In Line Timecard Editing is detailed below for each Timecard Editing
Mode.

### Delayed Save Mode w/ Edit Immediately

This mode is enabled by default for new InfiniTime
installations and is ideal for normal use in most operating environments
where InfiniTime is deployed
on a local area network or wide area network. The Delayed Save functionality
and user friendly spreadsheet - like interface provide increased performance
by reducing the number of round trips between the InfiniTime
Client Machine and InfiniTime
Server. A 'Save Button' will be displayed after a timecard record is altered
and focus is removed from the record. Additional timecard records may
then be altered prior to saving the changes. In this way, the Timecard
Table can be edited like a spreadsheet moving from cell to cell to edit
punch dates and times as needed before saving the changes. Delayed Save
also permits the user to click Cancel in order to revert to the original
timecard records and cancel recent changes. Changes to altered timecard
records are saved when:

1. The user clicks the save button.
2. The user switches pages in the timecard table.
3. The user switches to another employee.

Employee timecard records can be immediately edited on InfiniTime Timecard Tables with 'Delayed
Edit on Timecard Editors' unchecked. In this way, Timecard Tables immediately
load employee timecard records with all in line edit controls such as
the Time Picker and Date Selection Tools. Supervisors and InfiniTime Administrators may then
edit employee timecards immediately.

Technical Note: Organizations who observe a significant
delay when switching from employee to employee or page to page in the
Timecard Table may wish to enable Delayed Edit, especially if internal
Information Technology Personnel can confirm that remote client machines
experience increased latency and / or suffer performance degradation due
to high bandwidth utilization.

In
Line Editing - Delayed Save Mode Navigation

When using In Line Edit it is important
to understand how to move focus from one record to another in the Timecard
Table. When a record is highlighted and the cursor is located in a cell
on the record, the record is said to have focus. When delayed save is
enabled, Focus must be removed from a record before the Save Button will
be displayed. The down arrow key will remove focus from the highlighted
record. Tab can also be used to move between fields on a single Timecard
Record. These concepts are best explained through example. Multiple examples
of in line editing are provided below.

Saving Changes
to a Single Timecard Record

If
there is only a single record for the selected date range, focus must
be removed from the record before any changes will be saved. In the example
below, an employee missed a punch on the first day of a pay period.

![](/img/CH7_Timecard8.gif)

In
Line Edit refers to entering changes directly in the timecard record.
Use tab to move the cursor to the Out Date field and set the desired date.
Then use Tab again to move the cursor to the Out Time field and set the
desired time. Alternatively, simply click in the Out Date and the Out
Time and enter the desired values.

![](/img/accesing_timecard_activity_table.gif)

Once
the desired values have been entered, press the Down Arrow Key to remove
focus from the record. When
focus is removed from a record while Delayed Save is enabled the Save
Button will display. Click on the Save button to save the changes and
calculate hour totals.

![](/img/InLineEdit_1.jpg)

Fixing
a Missed Punch

Identify the record
with a missing punch. If the Missing Punch Exception is being tracked,
the Out Time of the record with a missing punch will be shaded red as
shown below.

![](/img/ECTDate.png)

Use the Up & Down
Arrows and the Tab Key to move the cursor to the Out Date Field where
the punch is missing. Alternatively, simply click in the Out Date Field.
Enter the appropriate date for the missed punch. Move the cursor to the
Out Time field and enter the appropriate time for the missed punch.

![](/img/image55.gif)

Click on another record
or use the down arrow key to move focus off of the altered record. The
Save Button will display. If you have additional changes to make in the
employee's timecard, such as editing an arrival or departure time or fixing
another missed punch, then do so. Once you have finished all changes for
the employee, click on the Save button. If for some reason you would like
to cancel the changes you have made, click the cancel button. The timecard
will revert to its original state.

![](/img/image72.gif)

Editing
Arrival or Departure Times

Identify
the record for which the Arrival or Departure Time must be edited. In
the example below, the 8:20 AM punch on 4/05/10 needs to be changed to
8:00 AM, as the employee was picking up supplies from a distributor and
was not on premises to clock in.

![](/img/CH7_Timecard7.gif)

Use the Up & Down
Arrows and the Tab Key to move the cursor to the Time field of the punch
that needs to be edited. Alternatively, simply click in the appropriate
field. Enter the time you wish to change the punch to.

![](/img/Tardy_Exception.gif)

Click on another record
or use the down arrow key to move focus off of the altered record. The
Save Button will display. If you have additional changes to make in the
employee's timecard, such as editing another arrival or departure time
or fixing a missed punch, then do so. Once you have finished all changes
for the employee, click on the Save button. If for some reason you would
like to cancel the changes you have made, click the cancel button. The
timecard will revert to its original state.

![](/img/image37.gif)

Audit
Trail Enabled - Fixing a Missed Punch

Identify
the record with a missing punch. If the Missing Punch Exception is being
tracked, the Out Time of the record with a missing punch will be shaded
red as shown below.

![](/img/filter-button.gif)

Use the Up & Down
Arrows and the Tab Key to move the cursor to the Out Date Field where
the punch is missing. Alternatively, simply click in the Out Date Field.
Enter the appropriate date for the missed punch. Move the cursor to the
Out Time field and enter the appropriate time for the missed punch.

![](/img/image37.gif)

Click on another record
or use the down arrow key to move focus off of the altered record. The
Audit Description Update Form will display. Enter a comment describing
why the punch was changed. This comment will be stored in the InfiniTime database for audit purposes.

![](/img/image76.gif)

After saving the audit
comment, the Save Button will display. If you have additional changes
to make in the employee's timecard, such as editing an arrival or departure
time or fixing another missed punch, then do so. The Audit Description
Update Form will display after each change. Once you have finished all
changes for the employee, click on the Save button. If for some reason
you would like to cancel the changes you have made, click the cancel button.
The timecard will revert to its original state and all audit comments
will be removed.

![](/img/image77.gif)

Delayed
Save: In Line Edit - Multiple Changes

The Delayed Save Timecard
Editor shows significant improvements in performance when editing multiple
records, as there is no delay when switching from record to record. Simply
use the Up and Down arrows to move between records and the Tab key to
move to the desired field on the record, then make changes as necessary.
Continue to make changes until you are finished editing the employee's
timecard, then click on the save button. InfiniTime
will automatically save changes to an employee's timecard if the timecard
table is closed, another employee is selected in the company timecard
table, or if the user moves to another page.

### Save Immediately Mode w/ Edit Immediately

* Save Immediately - The
  'Save Button' will not be displayed on the Company Timecard. Alterations
  to individual Timecard Records will be saved immediately when focus
  is removed from the record. If only one record is present in the Timecard
  Table, Tab must be used to remove focus from the record.
* Edit Immediately - Timecard
  Records are loaded with all in line edit controls (IE: Time Picker
  & Date Selection Tool) and may be edited immediately.

Changes to employee timecard records are saved immediately after focus
is removed from the respective record when 'Delayed Save on Timecard Editors'
is unchecked. This mode is considered outdated. InfiniTime
7.08 includes delayed
save which permits timecards to be edited like a spreadsheet and reduces
the number of transactions sent between the InfiniTime
Client machine and Server providing improved performance. Customers may
however disable the Delayed Save Functionality in favor of the traditional
'Save Immediately' Timecard Editing Mode included with prior versions
of the InfiniTime Software.
In this way, customers can utilize the same familiar timecard editing
interface and delay retraining employees on use of the Timecard Tables.
Save Immediately does not utilize a Save Button. With Save Immediately,
changes to altered timecard records are saved immediately to the InfiniTime Server after focus is removed
from individual timecard records.

Employee timecard records can be immediately edited on InfiniTime Timecard Tables with 'Delayed
Edit on Timecard Editors' unchecked. In this way, Timecard Tables immediately
load employee timecard records with all in line edit controls such as
the Time Picker and Date Selection Tools. Supervisors and InfiniTime Administrators may then
edit employee timecards immediately.

Technical Note: Organizations who observe a significant
delay when switching from employee to employee or page to page in the
Timecard Table may wish to enable Delayed Save and / or Delayed Edit,
especially if internal Information Technology Personnel can confirm that
remote client machines experience increased latency and / or suffer performance
degradation due to high bandwidth utilization.

In
Line Editing - Save Immediately Mode Navigation

When using In Line Edit it is important
to understand how to move focus from one record to another in the Timecard
Table. When a record is highlighted and the cursor is located in a cell
on the record, the record is said to have focus. With Save Immediately,
focus must be removed from a record before changes to the record will
be saved. The down arrow key will remove focus from the highlighted record.
Tab can also be used to move between fields on a single Timecard Record.
These concepts are best explained through example. Multiple examples of
in line editing are provided below.

Saving
Changes to a Single Timecard Record

If
there is only a single record for the selected date range, focus must
be removed from the record before changes to the record will be saved.
In the example below, an employee missed a punch on the first day of a
pay period.

![](/img/TCard019.png)

In
Line Edit refers to entering changes directly in the timecard record.
Use tab to move the cursor to the Out Date field and set the desired date.
Then use Tab again to move the cursor to the Out Time field and set the
desired time. Alternatively, simply click in the Out Date and the Out
Time and enter the desired values.

![](/img/Early.gif)

Once
the desired values have been entered, press the Down Arrow Key. When working
with the traditional timecard changes are saved immediately and the hour
totals will display.

![](/img/Absent_Exception.gif)

Fixing
a Missed Punch

Identify
the record with a missing punch. If the Missing Punch Exception is being
tracked, the Out Time of the record with a missing punch will be shaded
red as shown below.

![](/img/ExceptionsButton-Normal.gif)

Use the Up & Down
Arrows and the Tab Key to move the cursor to the Out Date Field where
the punch is missing. Alternatively, simply click in the Out Date Field.
Enter the appropriate date for the missed punch. Move the cursor to the
Out Time field and enter the appropriate time for the missed punch.

![](/img/image1.gif)

Click on another record
or use the down arrow key to move focus off of the altered record. Hour
totals will calculate and be displayed immediately.

![](/img/UpdateTIS_AuditNote.gif)

Editing Arrival or
Departure Times

Identify
the record for which the Arrival or Departure Time must be edited. In
the example below, the 8:20 AM punch on 4/5/10 needs to be changed to
8:00 AM, as the employee was picking up supplies from a distributor and
was not on premises to clock in.

![](/img/SW_CH11_NOTES_0005.gif)

Use the Up & Down
Arrows and the Tab Key to move the cursor to the Time field of the punch
that needs to be edited. Alternatively, simply click in the appropriate
field. Enter the time you wish to change the punch to.

![](/img/Tcard06.gif)

Click on another record
or use the down arrow key to move focus off of the altered record. Hour
totals will calculate and be displayed immediately.

![](/img/CH7_Timecard7.gif)

### Delayed Edit Mode

When 'Delayed Edit on Timecard Editors' is checked on the Company Update
Form, Delayed Edit Mode will be enabled. Delayed Edit Mode can be used
with Delayed Save or with Save Immediately according to the customer's
preferences. As previously explained, Delayed Save is enabled by default
on new installations and is recommended. Delayed Edit significantly reduces
the time required to load the Timecard Grid, especially for clients connecting
to the InfiniTime server
over a higher latency WAN Connection with high bandwidth utilization.
Users who observe delays while editing timecards, especially when switching
from employee to employee and waiting for timecards to be displayed, may
wish to enable Delayed Edit.

When Delayed Edit is enabled, Timecard Records are loaded in View Only
Mode. In Line Edit Controls such as the Time Picker & Date Selection
Tool will not be displayed initially. Supervisors and InfiniTime
administrators must click on the 'Change' button before timecard records
can be edited. InfiniTime's
Timecard Editors are shown below in Delayed Edit Mode. After clicking
on the Change Button and In Line Edit Controls are loaded, all other steps
for editing timecard records are identical to those detailed above for
Delayed Save and Save Immediately.

#### Company Timecard Table - Delayed Edit / View Only Mode

![](/img/image146.gif)

Change - The
Change Button will load the In Line Edit Grid and In Line Edit Controls.
Supervisors and InfiniTime
Administrators may then alter employee timecards as desired. It is important
to note that other timecard features such as Quick Punch, Purge, and Review
may be used without first clicking on the Change Button to display In
Line Edit Controls.

#### Employee Timecard Table - Delayed Edit / View Only Mode

![](/img/PurgeButton-Normal.gif)

Change - The
Change Button will load the In Line Edit Grid and In Line Edit Controls.
Supervisors and InfiniTime
Administrators may then alter employee timecards as desired. It is important
to note that other timecard features such as Quick Punch, Purge, and Review
may be used without first clicking on the Change Button to display In
Line Edit Controls.

#### Employee Module Timecard Table - Delayed Edit / View Only Mode

Some organizations choose to permit employees to edit their own timecards.
It is important to note that the Timecard Editing Mode settings within
the Manager Module are applied to all InfiniTime
Timecard Tables - including the Employee Module Timecard Table as shown
below.

![](/img/InLineEdit_4.jpg)

Change - The
Change Button will load the In Line Edit Grid and In Line Edit Controls.
Supervisors and InfiniTime
Administrators may then alter employee timecards as desired. It is important
to note that other timecard features such as Quick Punch, Purge, and Review
may be used without first clicking on the Change Button to display In
Line Edit Controls.

# Purging Time Card Activity

This feature allows the user to delete timecard activity for this employee
that is old and no longer useful.  Selecting ![](/img/SW_CH11_NOTES_0006.gif)
button brings you to the purge time Card Activity update window.

![](/img/InLineEdit_MP4_NoDelSav.gif)

Description - The description
displays information regarding the employee for which activity is being
purged and the employee purging activity. This information is recorded
in the Purge History Table.

Date Range -
Select the date range that you wish to Purge.  *If the purge is for one day only, then the start
and end dates will be the same.*

![](/img/Employee-Button.gif)
- The filter button will allow you to purge timecard activity for multiple
employees at a time. Employees can be filtered in multiple ways including
by department or group. Refer to the user interface section of this document
for more information.

# Reviewing Time Card Activity

The Timecard Activity Review aids supervisors
by making it possible to flag employees for which timecard activity has
been reviewed and approved by a supervisor.  Selecting the ![](/img/TCard017.png)
button will bring up the Review Time Record Update Form, which allows
the user to select one or more employees for review of their timecard
activity.

![](/img/Long-Break-Exception.gif)

Description
- The description displays information regarding the employee for which
activity is being reviewed and the employee reviewing activity. This information
is recorded in the Supervisor Review History Table.

Date Range -
Select the date range that you wish to review.  *If the review is for one day only, then the start
and end dates will be the same.*

![](/img/Absent_right_click.gif) - The filter
button will allow you to review punches to multiple employees at a time.
 You can filter which employees will get their activity reviewed
either by departments, groups, or by tagging multiple employees.

### Viewing Who Reviewed Employee Timecards Activity

The software allows you to view a list
of supervisors that have reviewed the activity , along with the time and
date of the review.

![](/img/TCard004.png)To
access this Supervisors Review History Table Right click on the activity
you  want to check  and on the pop up menu select Supervisor
review History.

The Supervisor Review History Table will
display a list of supervisors that have reviewed the activity along with
the time and date of when the activity was reviewed.

Supervisor Review History
Table

![](/img/SupReviewHistoryRC.gif)

The Supervisor Review History Table shows
the time of review, the date of the review and who was the supervisor
that reviewed the activity.

# Timecard Notes Overview

Timecard Notes make it possible for supervisors to enter a comment or
paragraph and associate the comment with a timecard punch. While this
principle is similar to the operation of existing the Audit Trail system,
Timecard notes are not mandatory and are only entered as deemed necessary
by supervisors. Compared with the existing Audit Trail System, which automatically
records an audit record each time a timecard punch is inserted, edited,
or deleted, Timecard Notes offer flexibility and distinction of entry
as they are only created specifically by supervisors on a case by case
basis.

Timecard notes are useful for the following scenarios:

* Documenting why
  an Employee Arrived Late
* Documenting why
  an Employee Left Early
* Documenting reasons
  for Missed Breaks, Short Breaks, or Long Breaks
* Associating notes
  and comments with employee timecard punches as needed.

Timecard Notes can be viewed
from within the Company, Employee, and Employee Module Timecard tables
from the Note Tab on Audit Database Table or via the Timecard Note Report.

# Inserting Timecard Notes

Timecard Notes are added through use of the Right Click Menu within
the InfiniTime Timecard
Tables as detailed below.

1. Open the Company or Employee Timecard Table.

![](/img/image71.gif)

2. Right Click on the Timecard Record you wish to enter a note for.

![](/img/InsertButton-Normal.gif)

3. Click on Note.

4. Enter the desired note / comment. Timecard Notes permit up to 499
Characters.

![](/img/Unapproved_OT.gif)

5. Click OK to associate the note with the timecard record.

6. If Delayed Save is enabled, focus must be removed from the Timecard
record by clicking on another timecard record or using Tab to remove focus
from the timecard record in order to display the save button. The user
may then click Save to save the previously entered note.

Technical Note:
Timecard Notes are associated with the In Punch of the selected punch
pair. If the in punch should be deleted from the database, the Timecard
Note will be permanently deleted.

# Viewing Timecard Notes

Timecard Notes can be viewed for a specific date from the Notes Tab
on the Audit Database Table as detailed below. The Audit Database Table
is most useful for reviewing notes during timecard review or payroll processing.
This allows supervisors to quickly identify why employees were late, early,
etc. on a given day without the need to run a report.  The [Timecard Note Report](TimecardEditing.md#tim46_Timecard_Note_Report) is
best suited for viewing all notes over a specific date range such as Last
Pay Period or Current Pay Period.

1. Open the Company Timecard.

![](/img/image146.gif)

2. Right Click on the Timecard Record you wish to check for Timecard
Notes.

![](/img/TCard016.png)

3. Click on Audit Trail.

4. Click on the Note Tab.

![](/img/TCard004.png)

5. All notes associated with the Timecard Punch Pair will be displayed.

![](/img/image142.gif)

# Timecard Note Report

The Timecard Note Report is listed under the Management Reports Category
on the Report Library Table. The Timecard Note Report displays all Timecard
Notes in the selected date range for all employees specified by the Employee
Filter per the Report Selection Criteria. The Timecard Note Report can
be found under the Management Reports Category on the Report Library.

Report Example:

![](/img/image93.gif)

Notes/Usage:

The Timecard Note report is useful for
displaying all timecard notes for a given date range when reviewing employee
timecard records prior to payroll.

Options:

 | Option | Default Value | Description | 
| --- | --- | --- |
 | Allow Graphics On the Report? | Yes | This option allows you to choose if you want to print the InfiniTime logo on the report. | 
 | Department Selection Based On? | Employee Default Department | This option will allow you to select how the Department  filter is used to select employees. By default, departments tagged on the selection criteria will cause InfiniTime to display employees assigned to that department on the report. Alternatively, selecting 'Worked in Department' will show employees that worked in the selected department during the selected date range. | 
 | Group by Department? | No | This option will group employees specified by the Employee Filter according to their Default Department. | 
 | Group by Employee? | No | This option will group employees specified by the Employee Filter by Last Name. | 
 | Group by Job? | No | This option will group employees specified by the Employee Filter according to their Default Job. | 
 | Group by Supervisor? | No | This option will group employees specified by the Employee Filter according to their Default Supervisor. | 
 | Group by Task? | No | This option will group employees specified by the Employee Filter according to their Default Task. | 
 | Group level to group by: | None | This option will sort employees specified by the Employee Filter according to their group description for the selected group level. For example, a company with multiple locations might have a Group Level of 'Location' and Group Descriptions of 'Pittsburgh' , 'Phoenix' , and 'Jacksonville'. Selecting the 'Location' group level would sort employees according to their assigned location. | 
 | Job Selection Based On: | Employee Default Job | This option will allow you to select how the Job filter is used to select employees. By default, jobs tagged on the selection criteria will cause InfiniTime to display employees assigned to the job on the report. Alternatively, selecting 'Worked in Job'' will show employees that worked in the selected job during the chosen date range. | 
 | Page Break by Department? | No | This option will allow you page break the report based on the Employee's Default Department, making it easier to give the report to department heads for review if needed. | 
 | Page Break by Employee? | No | This option will allow you to page break the report based on each employee, making it easier to give the report to the individual employees for review. | 
 | Page Break by Group? | No | This option will allow you to page break the report based on each Group Description and is intended for use with 'Group Level to Group By.' The report can then be distributed as necessary. | 
 | Page Break by Job? | No | This option will allow you to page break the report based on the Employee's Default Job, making it easier to give the reports to Job Supervisors for review. | 
 | Page Break by Supervisor? | No | This option will allow you to page break the report based on Employee Supervisors, making it easier to distribute to Supervisors for review. | 
 | Page Break by Task? | No | This option will allow you to page break the report based on the Employee's Default Job, making it easier to give the reports to Task Supervisors for review. | 
 | Print Inactive Employees? | No | This option will allow you to print information of the inactive employees along with the active ones. | 
 | Show System Audits? | No | This option will allow you display all system audits on the report.  System Audits include auto punch, Auto breaks, change to breaks. | 
 | Sort by Employee Number? | No | This option will group employees specified by the Employee Filter according to their Employee ID. | 
 | Task Selection Based On: | Employee Default Task | This option will allow you to select how the Task filter is used to select employees. By default, tasks tagged on the selection criteria will cause InfiniTime to display employees assigned to the task on the report. Alternatively, selecting 'Worked in Task'' will show employees that worked in the selected task during the chosen date range. | 