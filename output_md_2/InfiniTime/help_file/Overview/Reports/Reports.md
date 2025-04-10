xml version="1.0" encoding="utf-8" ?





Reports




# InfiniTime Reports - Introduction

InfiniTime includes a
variety of reports for different purposes ranging from simple informational
reports such as the Employee Profile Report which display information
and employee details stored within the InfiniTime
Database to detailed data driven reports such as the Attendance Review
Report which displays an at a glance view of Worked Days, Paid Leave,
and Unpaid Leave along with all exceptions associated with an employee's
timecard records for a given date range. InfiniTime
Reports are separated into multiple categories for ease of use and accessibility
as shown below.

### Accessing the Report Library

1. Click on the Reports Button on the
   Main Toolbar.

![](images_2/SoftwareOverview_001_Btn7_Reports.png)

2. The Report Library Table will be displayed. The Report Library
   displays all reports included with the InfiniTime
   Software separated into specific categories as shown below. Click
   on the + Sign to expand a given report category and display reports
   included.

![](images_2/TCard018.png)

### Quick Print vs Saved Reports

Before any of the reports within InfiniTime
can be executed the user is first prompted to enter specific details,
referred to as the Selection Criteria and Report Options, as appropriate
based on the type of report. For example, Timecard and Schedule Reports
require the user to select a Date Range for which Schedules / Timecards
will be displayed as well as a filter to identify which employees schedules
/ timecard records will be displayed for.

Supervisors and InfiniTime
Administrators with access to the Report Library have the option of executing
reports using either quick print or creating a saved report and then executing
the saved report.  For example purposes, the Report Library is shown
with the Employee List report selected below. Notice how the left pane,
where individual reports are displayed, shows the Quick Print Button at
the bottom and the Right Pane, where saved reports for the selected report
are displayed, lists several Saved Reports. Quick Print permits Supervisors
and InfiniTime Administrators
with access to the report library to set Selection Criteria and Report
options then immediately execute and view results for a given report.
It is important to note that the Selection Criteria and Report options
configured for use with Quick Print are not saved - Quick Print permits
only one time execution of a given report for immediate viewing. Saved
Reports reduce the need for configuring the Selection Criteria and Report
options repeatedly by permitting Supervisors and InfiniTime
Administrators to create saved reports with Selection Criteria and Report
options configured appropriately to meet their needs. In this way, saved
reports permit users to view specific details on a regular basis. In general,
it is suggested that Saved Reports be configured if a user expects to
execute a given report more than once using the same Selection Criteria
and Report Options.

![](images_2/RPT001.png)

In the example above, ABC Company has configured groups and assigned
groups to employees to indicate their Labor Classification and their default
location. The employee list report for each individual location and labor
classification can be quickly printed by all supervisors and the InfiniTime Administrator using the
saved reports shown above.

#### Saved Reports - Essential Concepts

* Saved Reports can be created, viewed, executed, and edited by all
  users with access to the Report Library. It is not possible to limit
  the saved reports an individual can access on the Report Library.
  It is however possible to expose only specific saved reports to a
  user via 1.) Use of InfiniTime
  Escort and 2.) by configuring security to prevent the user from accessing
  the Report Library. Additional details on Escort and Escort Window
  Design can be found in the [Escort
  Section](/InfiniTime/help%20file/Overview/Escort/Escort_Overview.md#esc01_Escort_Overview) of this document. Additional details on configuring
  security rights within InfiniTime
  can be found in the [Security
  Section](/InfiniTime/help%20file/Overview/Security/Security_Overview.md#sec01_Security_Overview) of this document.
* Saved Reports should be configured for all day to day, week to
  week, and payroll related tasks / functions as appropriate for your
  organization. In this way, Supervisors and InfiniTime
  Administrators can quickly access relevant Time and Attendance Details
  based on your organization's specific implementation of available
  InfiniTime Features.
  For example, most customers choose to create saved reports for their
  preferred timecard reports for both Current Pay Period and Last Pay
  Period.
* Supervisors for specific Departments, Locations, etc. should include
  a unique Label in their saved reports such as their Department or
  Location Name such that all other supervisors are aware they specifically
  created the report for their use.
* Supervisors and InfiniTime
  Administrators should exercise caution when altering a saved report
  they did not initially create, especially if the report is configured
  to automatically email on a regular basis. Remember - another user
  may be performing specific actions such as reviewing employee timecards
  or personnel review based on the report.
* There is no limit to the number of saved reports that can be created
  for each report within InfiniTime.

### Customizing the Report Library

Reports are organized into categories on the Report Library Table for
ease of use. Customers may choose to add additional report categories
to the report library for specific users or organizational units (IE:
Departments / Divisions / etc.) Default Reports, as included with the
InfiniTime Software, may
then be copied and moved to user created report categories.  A brief
description of each report category included within InfiniTime
is provided below.

* Employee Information Reports
  - This set of reports provides information on employees that is not
  related to Time Activity. Examples include Employee accruals, comments,
  and an employee list.
* Job Cost Reports - Designed
  for reviewing Job and Task hours distributions. Intended for labor
  costing analysis. The Job Cost Reports Category will not be displayed
  if there are no Jobs or Tasks configured within InfiniTime.
* Management Reports â Designed
  for management purposes only, these reports assist with exception
  tracking, auditing, and other management related tasks.
* Payroll Reports â Payroll
  reports assist employers by providing a summary of employee earnings
  based upon an employeeâs hours and specified wage. It is important
  to note that these reports do not compute deductions and are considered
  gross pay.
* Schedule Reports â Various
  types of schedule reports can be printed to obtain hard copies of
  employee work schedules for viewing purposes.
* System Reports â The System
  Reports provide information about your InfiniTime
  software and related hardware configuration.
* Timecard Reports - The
  Timecard Reports provide a variety of report types that display a
  summary or detailed information of employees timecard activity.

![](images_2/Rpt002.png)

### Report Library - Context Sensitive Buttons

It is important to note that the buttons displayed on the left side
of the Report Library are context sensitive depending on the selected
item. An outline of each scenario with different buttons for use on the
Report Library is provided below.

#### Default Report Category Selected

Insert -
Creates a new Report Category and Opens the Report Category Update Form.
The user may then enter a description for the new Report Category. User
Created Reports can then be placed into the new report category for organization
purposes.

![](images_2/Rpt004.png)

Change -
Opens the Report Category Update Form for the Selected Report Category.
The user may change the Report Category name if desired.

#### User Created Report Category Selected

Insert -
Creates a new Report Category and Opens the Report Category Update Form.
The user may then enter a description for the new Report Category. User
Created Reports can then be placed into the new report category for organization
purposes.

![](images_2/Rpt004.png)

Change -
Opens the Report Category Update Form for the Selected Report Category.
The user may change the Report Category name if desired.

Delete -
Deletes the Selected Report Category. All user created reports assigned
to the Report Category will be deleted.

#### Default Report Selected

![](images_2/Rpt005.png)

Copy - Creates
a User Created report using the selected Default Report as a template.
The user created report may be placed into a separate report category,
renamed, or be configured with its own set of Saved Reports.

Quick Print -
Opens the Report Selection Criteria Update Form. Permits
the user to perform a single execution for a given report based on Report
Selection Criteria settings configured by the user.

Insert -
Creates a new User Created Report and Opens the Report Layout Update Form
where the user may enter a description for the new report. User Created
Reports can then be placed into the new report category for organization
purposes. It is important to note that user created reports created using
the Insert Button are intended for use only with Custom Crystal Report
files designed by and specifically provided for use with InfiniTime by Inception Technologies.

![](images_2/Rpt006.png)

Change -
Opens the Report Layout Update Form where the user may enter a description
for the new report. User Created Reports can then be placed into the new
report category for organization purposes.

#### User Created (Copied or Imported) Report Selected

![](images_2/Rpt007.png)

Copy - Creates
a User Created report using the selected Default Report as a template.
The user created report may be placed into a separate report category,
renamed, or be configured with its own set of Saved Reports.

Import
- Populates the selected User Created Report with a Crystal Report
File selected from the local hard disk by the user. Only Crystal Report
files designed and provided by Inception Technologies
for use with InfiniTime
should be imported into the report library using this feature. It is important
to note that all Default Reports and User Created Reports created by copying
a Default Report will be populated with a Crystal Report File by default.
User Created Reports created via insert will initially contain no crystal
report file and as a result, cannot be executed.

Quick Print -
Opens the Report Selection Criteria Update Form. Permits
the user to perform a single execution for a given report based on Report
Selection Criteria settings configured by the user.

Insert -
Creates a new User Created Report and Opens the Report Layout Update Form
where the user may enter a description for the new report. User Created
Reports can then be placed into the new report category for organization
purposes. It is important to note that user created reports created using
the Insert Button are intended for use only with Custom Crystal Report
files designed by and specifically provided for use with InfiniTime by Inception Technologies.

![](images_2/RPC_Layout.png)

Description
- Enter a description for the User Created Report.

Category
- Used to assign the report to a report category. Users may click on the
Lookup Button to select from existing report categories as shown below.

Report Category Table

![](images_2/BrowseRCT.png)

Select
- Assigns the previously selected report to the highlighted Report Category.

Insert
- Permits entry of a new report category. Opens the Report Category Update
Form.

Change
- Opens the Report Category Update Form for the Selected Report Category.
Users may then edit the Report Category Description.

Delete
- Deletes the selected report category.

WARNING:
If a report category is deleted, all associated reports will be removed
from the Report Library.

Change -
Opens the Report Layout Update Form where the user may alter the description
for the report. User Created Reports may then be placed into the new report
category for organization purposes if desired.

Delete -
Removes the User Created Report from the Report Library. All saved reports
associated with the User Created Report will be deleted.

# Report Selection Criteria Update Form

The report selection criteria update form is displayed after clicking
quick print and when a report is saved. Selection criteria determines
which employees data will be displayed for in addition to the way the
report is displayed.  All fields are summarized below.

General Tab

![](images_2/QS_Chapter1_09.gif)

Description: Enter a descriptive
name for the report setting. This name will be displayed in the Report
Library Table when entering saved report settings. This field is not available
when using quick print.

Use Description as Report Name:
This will use the report name as a title for the report when it is printed.

Inactive: Checking this box
will render the report inactive. The report will be displayed in red on
the Report Library Table and cannot be used until it is reactivated.

Print Preview: Displays a preview
of the report on-screen before it is sent to the printer.

Export File Name: If you wish
to save the report to a file enter the file name here. It is important
to note that a path cannot be used.

PGP - The PGP tab is only available
after an export file name has been specified. PGP is an encryption algorithm
and can be used to secure report files against undesired access. Refer
to PGP Encryption: Introduction for detailed information regarding the
use and configuration of PGP.

# Selection Criteria

The selection criteria tab employs various filters in order to select
what employees will be included in the report. It is important to note
that employees must meet all selection criteria in order to be present
in the report. For example, if a certain group and department are selected,
only employees within the specified group and department will be printed
in the report. The selection criteria are configured to print for all
employees by default.

![](images_2/ReportSelectionCriteria_Filters.gif)

Date Range: Select the date
range the report will be executed for. If you wish to view activity from
last pay period for example, then choose last pay period.

Selected Employees: Select individual
employees to be included in the report. Change the drop down box from
All to Selected, and tag employees you wish to include in the report.
Employees can be selected in addition to other filters such as departments
and groups. Selected employees will be shown in addition to any employees
indicated by the department and group selections.

Selected Departments: Select
individual departments to be included in the report. Change the drop down
box from All to Selected, and tag departments you wish to include in the
report.

Selected Jobs: Select individual
Jobs to be included in the report. Change the drop down box from All to
Selected, and tag Jobs you wish to include in the report.

Selected Tasks: Select individual
Tasks to be included in the report. Change the drop down box from All
to Selected, and tag Tasks you wish to include in the report.

Selected Groups: Select individual
groups to be included in the report. Change the drop down box from All
to Selected, and tag groups you wish to include in the report. When selecting
multiple groups information will be shown for all employees in each group.

Selected Exceptions: Select
individual groups to be included in the report. Change the drop down box
from All to Selected, and tag groups you wish to include in the report.
All exceptions will be shown for employees that have any of the indicated
exceptions.

Selected Other Activities: Select
individual other activity types to be included in the report. Change the
drop down box from All to Selected, and tag other activity types you wish
to include in the report. Only the other activity types indicated will
be displayed on the report. Regular activity and overtime will not be
displayed.

Misc. Selections: Select individual
employees to be included in the report. Change the drop down box from
All to Selected, and tag employees you wish to include in the report.

*Note*:  It is not uncommon
for users to Choose âSelectedâ in order to specify individual employees,
departments, jobs, tasks or groups and then forget to tag specific employees,
departments,  jobs, tasks or groups. Employees are not selected if
a green checkmark is not displayed to the left of their name. Should selected
be chosen, and no employees specified, selection criteria will automatically
revert to the âAllâ selection in order to avoid an error.

# Email

![](images_2/QS_Chapter1_16.gif)

InfiniTime gives you
the capability to E-mail reports from the software in a range of formats.
 E-mailing the reports can be done right after the report has been
printed or automatically according to a schedule (see Auto Report Schedule).

From - Allows the user to specify
the email address that will appear in the 'From' field for report files
sent via email. In this way the recipient can reply to the email and the
message will be sent to the correct person. For example Ms. Jackson is
the in charge of payroll processing at a small company. She would enter
her email address in the from field so employees could reply to reports
that were emailed to them in order to give her feedback on their timecard
reports.

Subject - This is the subject
of the email that will be displayed in the recipients e-mail.

Format â You can choose from
several different formats that the report will be exported and e-mailed.
 The formats include, PDF, Excel, Comma Separated text, or WORD document.

Body Text - You can type a message
that will be in the e-mail along with the attached report.

Send To â This is the list of
people that will receive the e-mail.

Insert - Click on the insert
button to add a recipient for the email.  First fill in the name
and press enter. The cursor will then move into the address column.  Fill
out the address and then press enter.  To insert multiple recipients
repeat the steps above.

![](images_2/rep12.gif)

Change - Click on this button
to make changes to the recipient information.

Delete - To delete a recipient,
highlight the recipient under the Address List and press the delete button.

Technical Note:
InfiniTime uses the Windows
Operating System on the InfiniTime
Server . If you should experience issues with auto reports please refer
to the [Automatic Reports Requirements](/InfiniTime/help%20file/Overview/Reports/Reports.md#AutoReq)
and the [SMTP
Email Setup and Troubleshooting Document](/InfiniTime/help%20file/RESOURCES/SMTP_Email_Setup_And_Troubleshooting.pdf).

# Auto Report Schedule

![](images_2/rep9.gif)

InfiniTime allows a schedule
to be configured in order to run reports automatically. Reports are automatically
emailed or printed depending on the configuration.  Settings must
be saved for a report before it can be configured to run automatically.

Note: The InfiniTimeHouseKeeping
service must be running in order for reports to print automatically.

Insert
â Click insert to open up the Auto Report Schedule Update Form and set
a schedule.

Change
â Click change to make any adjustments to a previously configured schedule.

Delete
â Click delete to remove the highlighted Report Schedule.

![](images_2/CH10AutoReports.gif)

Description
â Describes the Report Schedule you are creating.  This name will
appear in the Report Library Update Form.  This is how you will be
able to distinguish between other Auto Report Schedules you may create.

Printer
- InfiniTime uses printer
drivers to prepare reports for proper display on your computer. Select
a printer that is installed and attached to your machine. Do not select
an image printer. The warning below will be displayed when saving the
Auto Report Schedule. Reports without a valid printer may not print or
display properly.

![](images_2/ValidPrinter.gif)

Frequency
â This is how often the program will run the auto report schedule feature.
 The options are: Once, Daily, Weekly, and Monthly.

Do Not Print
- The Do Not Print check box is only displayed when a report is configured
to be sent to a remote party via email or FTP. Reports will be printed
according to the automatic report schedule by default. This box should
be checked if you wish to email or send a report via FTP without printing
the report.

Date to
Print â This is the date that you want the system to print the
current set up on.

Time to
Print â This is the time that you want the system to print the
current set up on the date selected above.

Day of Week
to Print â Select the day of week you wish for the system to print
the structure on.

Date Last
Printed â Tells you the last date the system automatically printed
the structure.

Time Last
Printed â Tells you the last time on the date above the system
automatically printed the structure.

Date to
Print Next â The date entered here will be the next future date
that the system will automatically print a saved structure.

### Auto Report Requirements

InfiniTime can be configured
to automatically email or print reports, payroll exports, and exports
with saved criteria. A list of requirements and items that are known to
interfere with the intended processing of auto reports can be found below.
Each requirement must be met for auto reports to function as intended.

 It should also be noted that saved report settings configured
with an email address will only be emailed according to the settings on
the auto report schedule and email tabs. They will not be printed automatically.
A single saved report setting cannot be used to automatically email and
print a report. Separate saved settings must be configured. Your network
administrator may need to assist you with configuring the following items.

To automatically email a report the following criteria must be observed:

* The InfiniTime
  Server must have an active Internet connection.
* Power Management must be
  disabled on the Network Interface Card of the InfiniTime
  Server.
* The InfiniTime
  Housekeeping Service must be started and running.
* The InfiniTime
  Server does not need to have a user logged into the console. However,
  it must at least be powered on and idle at the Windows Login Splash
  Screen.
* A printer must be installed
  on the InfiniTime Server.
* A printer must be set as
  the default printer.
* The Print Spooler Service
  must be started and running on the InfiniTime
  Server.
* Your fully qualified domain
  name may need to be configured in the advanced delivery options of
  the SMTP Virtual Server created by InfiniTime
  depending on your domain policies.
* An auto schedule must be
  configured within a saved report setting.
* A destination name and
  email address must be defined on the email tab of the saved report
  setting.
* The server must be granted
  permissions to relay email through the SMTP Virtual Server installed
  by InfiniTime.

* Depending on your network
  configuration and domain settings it may be necessary to forward all
  outgoing email messages from the InfiniTime
  SMTP Virtual Server to a Smart Host. Generally the Smart Host will
  be a server running exchange on your local network. The smart host
  can be configured under Advanced Options of Delivery tab for the InfiniTime SMTP Virtual Server Properties.

To automatically print a report the following criteria must be observed:

* The InfiniTime
  Server must have an active Internet or Local Area Network connection
  if the destination printer is not directly connected to the InfiniTime Server.
* Power Management must be
  disabled on the Network Interface Card of the InfiniTime
  Server if the destination printer is not directly connected to the
  InfiniTime server.
* The InfiniTime
  Housekeeping Service must be started and running.
* The InfiniTime
  Server does not need to have a user logged into the console. However,
  it must atleast be powered on and idle at the Windows Login Splash
  Screen.
* A printer must be installed
  on the InfiniTime Server.
* A printer must be set as
  the default printer.
* The Print Spooler Service
  must be started and running on the InfiniTime
  Server.
* An auto schedule must be
  configured within a saved report setting.

# Options

![](images_2/ReportSelectionCriteria_Options.gif)

A list of additional settings are available on the Options Tab. Select
Yes or No using the drop down boxes in order to enable or disable the
option. Some options are specific to certain reports and will not be available
for all reports.

Allow Graphics On The Report
â Enables or disables the display of graphics on the report.

Department Selection Based On -
Choose how tagging departments on the Selection Criteria Tab effects the
information displayed on the report. If this option is set to Employee
Default Department employees will be shown with Default Departments that
match departments indicated by the Selection Criteria. If this option
is set to Employee Worked in Department Employees who have activity in
the departments indicated by the Selection Criteria in the chosen date
range will be displayed on the report.

Employee
Default Department -  Selecting this option all hours worked
by an employee will display under their default department even if they
have activity in other departments, all of the activity for all departments
will show under that employees default department.

Employee
Worked On Department -  Selecting this option all hours worked
by an employee will display in the department that employee worked in,
so you might see that employees name associated with different departments
in the report.

Department
Selection Filters Activity? - When enabled, Timecard Activity is
filtered according to departments tagged on the Department Tab of the
Report Selection Criteria Update Form. Timecard records will only be displayed
for hours worked in the selected departments. This feature is intended
for use in conjunction with the Department Selection Based On 'Employee
Worked In Department' option.

Employee Grouping Type -
Choose how employees will be ordered on the report. If this option is
set to Employee Name employees will be ordered alphabetically by name.
If this option is set to Activity Department employees will be listed
according to the department they worked in. If this option is set to Employee
Department employees will be listed according to the department they are
assigned to.

Group By Department â Enabling
this option will group all employees in the same department together on
the report.

Hide Audit Trail Asterisk -
Enabling this option will hide all audit trail asterisks on the report.
Audit trail asterisks are displayed by default to indicate punches that
have been edited or inserted manually.

Hide Exceptions - Exceptions
will not be displayed on the report if this option is enabled.

Page Break By Department â Enabling
this option will start a new page for each department.

Page Break By Employee â Enabling
this option will start a new page for each employee.

Print Inactive Employees â Enabling
this option will print information for inactive employees.

Print Signature Line - A signature
line will be displayed at the bottom of the results for each employee
if this option is enabled. Generally Page Break by Employee should be
enabled when using this feature.

Print Standard Breaks - Disabling
this option removes the Break Column from the report.

Print Time in Hours and Minutes
- InfiniTime reports activity
in hundredths of an hour by default. Setting this option to Yes displays
activity totals in hours and minutes.

Print Timecard Review History
- When enabled, Timecard Review history displays a list of supervisors,
including Supervisor Name, Supervisor Position, and Last Review Time,
for each employee who have reviewed all
of the employees Timecard Records for the selected date range. A supervisor's
name will not be listed if all records during the date range are not reviewed
by the supervisor. Only the Timecard Review History header will be displayed
if there are no supervisors who have reviewed all of an employee's Timecard
Records for the selected date range. The Timecard Review History option
is available on the following reports:

* Timecard
  Detail
* Timecard
  Detail with Weekly Totals
* Timecard
  With Clock Description
* Timecard
  With Phone Numbers

Example Timecard Detail Report with Timecard
Review History:

![](images_2/TimecardReviewHistory.jpg)

Print Weekly Totals - Enabling
this option adds a subtotal row for each week to report.

Punch Description Displays -
Changes the information displayed in the Punch Description column of the
report. By default grace periods such as tardy and early are displayed
in this area. Additional options are Telephone Number, Nothing, and Clock
Description.

# Configuring Reports for Use With The Employee Module

As mentioned in the Employee Module section of this document, each report
menu item within the employee module is fully customizable. These buttons
can be configured to print any single report within the InfiniTime software. If you should
have the Crystal Reports module, custom reports can be assigned to these
menu items as well.

To Configure Reports for Use With The Employee Module:

* Open the Report Library by Clicking on the reports button as displayed
  below.

![](images_2/rep1.gif)

* Click on the plus sign to show the reports within a particular
  category.

![](images_2/rep13.gif)

* Select the report you wish to designate for use from the Employee
  Module.

![](images_2/rep14.gif)

* Click Change.

![](images_2/rep15.gif)

* Click on the Options Tab.

![](images_2/rep16.gif)

* Check the button you wish to assign the report to.

![](images_2/rep17.gif)

Note: Each button within the employee module can only have one report
assigned to it. If a report is assigned to an Employee Module button the
check box will be gray and un-selectable. The original report must first
be unassigned before a new report can be selected for use. The following
reports are assigned to the Employee Module by default:

Timecard Button: Timecard Details

Accruals Button: Employee Accruals

Schedule Button: Postable Schedule

# User Customizable Reports

Unlike previous versions of InfiniTime,
InfiniTime 7.0
does not include the crystal reports add on due to the complexity of the
ASP.NET environment and licensing issues. As an alternative customizable
reports have been added to the software which give the user the ability
to pick and choose the information that will be displayed on the report.
By changing the report options users can control the information displayed
on the report. The customization process is outlined below.

Quick Print vs Saved
Reports

Customizable reports can be prepared in two different fashions, quick
print or a saved report. Quick print is used to provide specific information
for immediate review. The selection criteria and report settings will
not be saved. It is generally more efficient to configure a saved report
for customizable reports due to the numerous configuration options. This
makes it possible to run the saved report criteria at a later date. All
of the configuration options detailed below are available through quick
print or a saved report.

Customizable InfiniTime
Reports

A list of all customizable reports within
the InfiniTime Application
is provided below.

* Dept.
  Payroll Detail
* Dept.
  Payroll Summary
* Payroll
  Detail
* Payroll
  Summary
* Department
  Daily Summary
* Department
  Summary
* Shift
  Daily Summary
* Shift
  Summary
* Timecard
  Summary

General Settings

The customizable Timecard Summary report includes all of the standard
features offered for InfiniTime
reports including standard email functionality, automatic reporting features,
PGP Encryption, and a complete filtering system which can be used to select
employees for whom timecard activity will be reported for. A link to the
appropriate section of this document is provided below for more information.

[Emailing
Reports](/InfiniTime/help%20file/Overview/Reports/Reports.md#rpt13_Email)           â
        [Automatic
Report Scheduling](/InfiniTime/help%20file/Overview/Reports/Reports.md#rpt18_Auto_Report_Schedule)           â
          [PGP Encryption](/InfiniTime/help%20file/Overview/Security/Security_Overview.md#sec54_Optional_PGP_Encryption_for_Output_Files)           â
         [Selection
Criteria](/InfiniTime/help%20file/Overview/Reports/Reports.md#rpt11_Report_Selection_Criteria_Update_Form)

Customizable Options

Customizable Report Options: Page 1

![](images_2/TimecardSummary_OP1.gif)

Timecard Summary Options: Page 2

![](images_2/TimecardSummary_OP2.gif)

Column Configuration

Customizable Reports are user configurable.
Each column of the report can be set to show a specific type of hours
according to the users preferences. Available Hours Types are listed below.

Approved Overtime Hours One - Shows all Overtime
One Hours that have been approved.

Approved Overtime Hours Two - Shows all Overtime
Two Hours that have been approved.

Approved Overtime Hours Three - Shows all
Overtime Three Hours that have been approved.

Approved Overtime Hours Four - Shows all
Overtime Four Hours that have been approved.

Break Hours - Displays a total of change
to break and auto break hours.

Other Activity One - Displays all hours for
the chosen Other Activity Type.

Other Activity Two - Displays all hours for
the chosen Other Activity Type.

Other Activity Three - Displays all hours
for the chosen Other Activity Type.

Other Activity Four - Displays all hours
for the chosen Other Activity Type.

Other Amount - Sum of all Other Amounts not
displayed in another report column.

Other Hours - Sum of all Other Activity Hours
not displayed in another report column.

Overtime Hours One - Shows both approved
and unapproved overtime one hours.

Overtime Hours Two - Shows both approved
and unapproved overtime one hours.

Overtime Hours Three - Shows both approved
and unapproved overtime one hours.

Overtime Hours Four - Shows both approved
and unapproved overtime one hours.

Regular Hours - Shows all regular hours.

Unapproved Overtime Hours One - Shows all
Overtime One Hours has not been approved.

Unapproved Overtime Hours Two - Shows all
Overtime One Hours has not been approved.

Unapproved Overtime Hours Three - Shows all
Overtime One Hours has not been approved.

Unapproved Overtime Hours Four - Shows all
Overtime One Hours that has not been approved.

*Note:*
Other Activity Hours Types displayed in a report column will not count
toward the Other Amount or Other Hours Column.

*Note:*
To make a column blank simply assign it to an Other Activity Type that
has not been assigned. Unassigned Other Activity Types are set to 'None.'
Read below for additional information.

Other Activity
Types

To display other activity types in a column
on customizable reports the other activity type must first be assigned
to one of five Other Activity place holders as outlined below. It is not
necessary to configure all five other activity type place holders. Any
combination of Other Activity One through Other Activity Five may be configured
and used in a report column.

1.) Select the desired other activity types
on the Options Tab.

![](images_2/SelectOtherAct_1.gif)

2.) Set the chosen column to the Other Activity
Type place holder.

![](images_2/SelectOtherAct_2.gif)

Additional Options:

| Option | Default Value | Description |
| Allow Graphics On the Report? | Yes | This option allows you to choose if you want to print the InfiniTime 7.0 logo on the report. |
| Department Grouping Type? | None | This option allows you to group the report by the employees Activity Department, meaning that the hours will distribute to all the departments the employee worked, or group by Employee Default Department,which will put all the time worked in their default department even if they worked on other departments, or the last option is None. |
| Department Selection Based On? | Employee Default Department | This option will allow you to select how the Department  filter is used to select employees. By default, departments tagged on the selection criteria will cause InfiniTime to display employees assigned to that department on the report. Alternatively, selecting 'Worked in Department' will show employees that worked in the selected department during the selected date range. |
| Department Selection Filters Activity? | No | If this option is set to Yes, employee Timecard Records displayed on the report will be filtered according to tagged departments as follows:          1.) Only employees with Timecards in the tagged department(s) will be displayed on the report.  2.) Only Timecard records assigned to the tagged department(s) will be used to calculate totals for display on the report. All other timecard records for employees will be ignored when this option is set to Yes. |
| Group By Supervisor? | No | This option will group employees specified by the Employee Filter according to their Default Supervisor. |
| Group Level to group by: | No | This option will sort employees specified by the Employee Filter according to their group description for the selected group level. For example, a company with multiple locations might have a Group Level of 'Location' and Group Descriptions of 'Pittsburgh' , 'Phoenix' , and 'Jacksonville'. Selecting the 'Location' group level would sort employees according to their assigned location. |
| Job Grouping Type? | None | Determines how employees will be grouped by Jobs. When set to None the option is considered disabled and employees will not be grouped by jobs.  When set to Employee Default Job employees will be grouped according to their default job as assigned on their employee record. When set to Scheduled Job employees will be grouped according to the job they were scheduled for. |
| Job Selection Based On: | Employee Default Job | This option will allow you to select how the Job filter is used to select employees. By default, jobs tagged on the selection criteria will cause InfiniTime to display employees assigned to the job on the report. Alternatively, selecting 'Worked in Job'' will show employees that worked in the selected job during the chosen date range. |
| Job Selection Filters Activity? | No | If this option is set to Yes, employee Timecard Records displayed on the report will be filtered according to tagged departments as follows:          1.) Only employees with hours in the tagged Job(s) will be displayed on the report.  2.) Only timecard records assigned to the tagged Job(s) will be used to calculate totals for display on the report. All other timecard records for employees will ignored when this option is set to Yes. |
| Page Break by Department? | No | This option will allow you page break the report by Department, making it easier to give the report to department heads for review if needed. |
| Page Break by Employee? | No | This option will allow you to page break the report based on each employee, making it easier to give the report to the individual employees for review. |
| Page Break by Group? | No | This option will allow you to page break the report based on each Group Description and is intended for use with 'Group Level to Group By.' The  report can then be distributed as necessary. |
| Page Break by Job? | No | This option will allow you to page break the report by Job, making it easier to give the reports to Job Supervisors for review. |
| Page Break by Supervisor? | No | This option will allow you to page break the report based on Employee Supervisors, making it easier to distribute to Supervisors for review. |
| Page Break by Task? | No | This option will allow you to page break the report by Task, making it easier to give the reports to Task Supervisors for review. |
| Print Inactive Employees? | No | This option will allow you to print information for both Active and Inactive Employees. |
| Print Time in Hours and Minutes? | No | InfiniTime reports activity in hundredths of an hour by default. Setting this option to Yes displays activity totals in hours and minutes. |
| Show Company Grand Total? |  | When set to Yes a total record will be added to the bottom of the report to show total company hours  for selected columns. |
| Sort by Employee Number | No | This option will group employees specified by the Employee Filter according to their Employee ID. |
| Task Grouping Type? | None | Determines how employees will be grouped by Tasks. When set to None   the option is considered disabled and employees will not be grouped by   tasks. When set to Employee Default Task employees will be grouped according to their default task as assigned on their employee record. When set to Scheduled Task employees will be grouped according to the task they were scheduled to work in. |
| Task Selection Based On: | Employee Default Task | This option will allow you to select how the Task filter is used to select employees. By default, tasks tagged on the selection criteria will cause InfiniTime to display employees assigned to the task on the report. Alternatively, selecting 'Worked in Task'' will show employees that worked in the selected task during the chosen date range. |
| Task Selection Filters Activity? | No | If this option is set to Yes, employee Timecard Records displayed on the report will be filtered according to tagged tasks as follows:          1.) Only employees with hours in the tagged tasks will be displayed on the report.  2.) Only timecard records assigned to the tagged task(s) will be used to calculate totals for display on the report. All other timecard records for employees will ignored when this option is set to Yes. |

# Importing Crystal Report Files & Configuring Categories

Due to licensing constraints it is not possible for users to design
their own crystal reports for use with InfiniTime.
However custom reports are available through Inception Technologies for
a fee which varies depending upon the nature of the request. To submit
a custom report request please contact your authorized InfiniTime
Dealer or Inception Technologies Sales Contact.

When submitting your request please have the following details available
if possible:

* If the request involves alterations to an existing
  report:
* + Describe desired alterations in detail.
  + Provide an example. Examples can be created
    by exporting the existing report to excel and altering fields
    and columns to reflect the desired results or by simply printing
    the report and writing in the alterations.
  + Provide Contact Name, Phone, and Email.
  + Specify Software Version and Registered Company
    Name.

  

* If the request is for a new report:
* + Describe in detail all columns and the type
    of information contained within.
  + Provide an example. Examples can be created
    within excel from scratch or by using a current report as a reference
    for the general report layout.
  + Provide Contact Name, Phone, and Email.
  + Specify Software Version and Registered Company
    Name.

##### Importing Custom Report Files Designed by Inception Technologies

Previously supplied custom reports designed by Inception Technologies
can be imported into the InfiniTime
Application via the Import Button on the Report Library. This ensures
customers who have had custom reports created for them can load them into
the application manually if necessary.

To Import a Custom Report:

1. Open the Report Library by clicking on
the Report Button on the main toolbar.

![](images_2/ImportReports_01.gif)

2. Browse to the report category where the
custom report will be added.

![](images_2/ImportReports_02.gif)

3. Copy an existing report.

![](images_2/ImportReports_03.gif)

4. Highlight the copied report. Click on
the Import button which is now displayed.

![](images_2/ImportReports_04.gif)

5. Click on the Magnify Glass and browse
to the Crystal Report file you would like to import.

![](images_2/ImportReports_05.gif)

6. Press OK to import the report.

![](images_2/ImportReports_06.gif)

# InfiniTimeReports: Exporting Reports to a File

InfiniTime reports can
be exported in a variety of formats such as Microsoft Word, Microsoft
Excel, Adobe PDF and Rich Text. This provides an extra level of flexibility
for distributing reports to interested parties. Once exported report files
can be attached to an email, archived, or distributed as necessary.

![](images_2/ExportReports_01.gif)

Export Options

A variety of options are
available when exporting report files. Many of the options detailed below
are not displayed until after the Export File Name has been filled. When
exporting reports to a file it is important to note how the file will
be retrieved by end users. Available options include email, direct download,
FTP transfer, and by accessing the output folder on the InfiniTime Server.

Email
- Report Files can be sent via email by completing the Email Tab on the
Reader Address Update form.

Direct
Download - Report Files can be downloaded directly from InfiniTime via a Web Browser. To download
the report file immediately after generating the report the 'Print Preview'
setting must be set to Yes.

FTP
Transfer - Report files can be sent via FTP to a remote FTP site.
See Sending Export Files Via FTP below.

Output
Folder - Report files can be exported directly to the Output Folder
in the InfiniTime 7 Program
Files Folder on the InfiniTime
Server. The user will not be given the option to download the report file
directly. To export the report file to the Output Folder on the InfiniTime Server the 'Print Preview'
setting must be set to No.

Export File Name - The export file name specified in this
field will be included in the name of the report file exported in addition
to the time and date of file creation. Do not include a path or file extension
in this field.

Export Format - InfiniTime provides
four formats for exporting report files. These formats are detailed below.

Adobe
PDF (.PDF) - Exports reports in a format compatible with Adobe Acrobat
Reader. These report files cannot be edited without PDF Authoring Software
and are intended for viewing purposes only. Adobe PDF is the default format
used with all InfiniTime
Reports and is recommended by Inception Technologies when exporting reports
for increased compatibility.

Microsoft Word (.DOC) -
Exports reports in a format compatible with Microsoft Word. These report
files can be edited directly with Microsoft Word and are intended for
light editing and viewing purposes.

Microsoft Excel (.XLS) -
Exports reports in a format compatible with Microsoft Excel. These reports
can be edited directly with Microsoft Excel and serve multiple purposes
due to the flexibility of Microsoft Excel.\*

Rich Text (.RTF) - Exports
reports in a common format compatible with most Rich Text Editors. These
reports can be edited directly with document editors compatible with the
Rich Text format.

\*Technical Note: Due to
some inconsistencies with Crystal Report's handling of advanced reporting
functions reports exported as Microsoft Excel files may require manual
editing in order for columns to align properly with their headings.

PGP Encryption - Report
files can be encrypted according to the PGP algorithm before export. Refer
to the [Introduction
on PGP Encryption](/InfiniTime/help%20file/Overview/Security/Security_Overview.md#sec54_Optional_PGP_Encryption_for_Output_Files) for more information on using this feature.

Sending Export Files Via
FTP - Use this feature to automatically
transfer the file via FTP (File Transfer Protocol) to a destination of
your choice. The following fields will become available and must be filled
out. An example is shown below. Keep the items that follow in mind when
entering this information.

* A domain name or IP Address can be
  used in the Host Address Field.
* Do not include the ftp:// prefix in
  the Host Address Field.
* The Directory field can be left blank
  if you are uploading to the root of the FTP Site.
* If you wish to upload to a specific
  folder on the FTP site you must specify the full path using a preceding
  forward slash ( / ) as shown in the image below.
* The Login Name can be a Local Windows
  Account, a Domain Account, or Anonymous. Enter the Login Name in one
  of the following formats:

Local Windows Accounts:

![](images_2/image466.gif)

1. Enter the Host Address There
are two valid formats for the host address field as detailed below.
Do not include the
ftp:// prefix in this field.

| Valid Host Address Formats | |
| Format Type | Example |
| IP Address | 192.168.1.20 |
| Domain Name | www.InfiniTime.com |

2. Enter the Directory. Remember to include
a preceding forward slash as shown.

3. Enter the Login Name in the following
format: "HOSTNAME\USER"  For Example if your FTP Server's
hostname is FTPSERVER and the user you wish to connect as is FTPUSER then
you would enter the following:

FTPSERVER\FTPUSER

4. Enter the user's password.

5. Specify the port to use when connecting
to the FTP Server. This does not generally need to be altered.

Domain Accounts:

![](images_2/image463.gif)

1. Enter the Host Address. There
are two valid formats for the host address field as detailed below.
Do not include the
ftp:// prefix in this field.

| Valid Host Address Formats | |
| Format Type | Example |
| IP Address | 192.168.1.20 |
| Domain Name | www.InfiniTime.com |

2. Enter the Directory. Remember to include
a preceding forward slash as shown.

3. Enter the Login Name in the following
format: "DOMAIN\USER"  For Example if your FTP Server's
domain is InfiniTime and
the user you wish to connect as is FTPUSER then you would enter the following:

InfiniTime\FTPUSER

4. Enter the user's password.

5. Specify the port to use when connecting
to the FTP Server. This does not generally need to be altered.

Anonymous User:

![](images_2/image465.gif)

1. Enter the Host Address. There
are two valid formats for the host address field as detailed below.
Do not include the
ftp:// prefix in this field.

| Valid Host Address Formats | |
| Format Type | Example |
| IP Address | 192.168.1.20 |
| Domain Name | www.InfiniTime.com |

2. Enter the Directory. Remember to include
a preceding forward slash as shown.

3. Enter Anonymous as the Login Name.

4. Leave the password field blank.

5. Specify the port to use when connecting
to the FTP Server. This does not generally need to be altered.

Technical Note:
Microsoft IIS includes an option to permit only anonymous connections
to an FTP Site. If this option is checked as shown below only anonymous
connections to the FTP Site will be allowed. This means ANYONE can access
the payroll export file. This option should be unchecked and it should
be confirmed that a login is required to gain read or write access to
the directory where the Payroll Export File will be uploaded. Please contact
your Information Technology Personnel for assistance with checking file
permissions on your FTP Site.

![](images_2/InfiniTimeFTPProperties.bmp)

Technical Note:
InfiniTime attempts
to connect to the FTP Site to validate the Login ID, Password, and Directory
when the OK Button is clicked on the Payroll Export Update Form. If InfiniTime is unable to successfully
connect to the FTP Site with the provided login information, or if the
specified directory does not exist, an error will be displayed.

# Commonly Used Reports

The following reports are the most commonly used reports
within the InfiniTime Application.
Additional information on each report can be viewed by clicking on the
report name below..

Employee List
- Displays Employee ID, Employee Name, Department, Job Title, Date
of Hire, Badge ID, Login ID, and Clock ID for employees included in the
Report Selection Criteria Employee Filter. Useful For:

* Printing a
  list of active employees within the InfiniTime
  Database
* Testing Filter
  Settings to ensure only desired employees are included in the Filter
* Printing Employee
  Hire Dates
* Viewing all
  employees to which a given supervisor has access, according to the
  supervisor's Security Filter.

+ This is
  accomplished by logging into the Manager Module as the supervisor
  in question and running the Employee List report without an employee
  filter. The Security Filter set for the Supervisor will be applied
  to the report such that only employees the Supervisor can see
  will be displayed on the report.

Employee Exception
Summary - Displays each exception during the selected date range
as a header record, with individual employees who triggered the exception
along with the number of instances each employee had for the respective
exception as detail records. Useful for determining the frequency of specific
exceptions across the entire organization and / or specific departments
/ groups of employees.

Employee Exceptions
Detail - Displays Employee Names and Employee ID Numbers as a header
with each exception during the selected date range as a detail record.
Useful for viewing all exceptions during a specific date range or for
viewing all exceptions for specific employee(s) during a given date range.

Employee Without
Reviewed Timecards - Displays the name of Employees with Unreviewed
Timecards according to report options. Report options can be configured
to require one or more reviews as well as review by the employee, the
employee's supervisor, or both. Useful for ensuring all employee timecard
records have been approved by an employee's supervisor and / or by the
employee prior to running payroll.

Payroll Detail
- Displays Employee Worked Hours and Other Activity Hours / Amounts
for the selected date range. Totals are calculated for each date with
hours. Wage Totals are calculated based on Employee Policy, Default Wage,
and Alternate Wage configuration.

Payroll Summary
- Displays Employee Worked Hours and Other Activity Hours / Amounts
for the selected date range. Totals are calculated for the entire date
range for each Worked Hours Type / Other Activity Type in the selected
date range. Wage Totals are calculated based on Employee Policy, Default
Wage, and Alternate Wage configuration.

Attendance Review
- Designed as a periodic employee performance report, the Attendance
Review Report is useful for identifying trends in employee performance
(IE: Tardy, Absent, Early Departure, consistent requests for personal
or sick time on a certain day of the week or month etc.). Depending on
how the report options are configured, the attendance review report can
show the individual calendar days on which an employee 1.) Worked 2.)
Did not work 3.) Had Other Activity 4. Had Exceptions. Additionally, the
report also shows the total number of worked days and the total number
of hours associated with schedule related exceptions such as Absent, Tardy,
Early Departure etc. It is important to note that the Attendance Review
report is based on a comparison of the employee's schedule hours, worked
hours, and the resulting exceptions. If exceptions and / or employee schedules
are not configured the capabilities of this report are reduced.

Postable Schedule
- Designed as a printable weekly schedule report, the Postable
Schedule report is ideal for posting employee schedules in advance. The
postable schedule report supports single working periods, multiple working
periods in different departments, and Other Activity Schedules such as
Vacation Time. Scheduled Hours for each employee are also totaled and
displayed on the report.

Activity Summary
- Displays the total number of hours by Worked Hours / Other Activity
Type for each employee with Timecard Activity during the selected date
range.

Timecard Detail
With Weekly Totals - Displays the total number of hours by Worked
Hours / Other Activity Type for each date for each employee with Timecard
Activity during the selected date range. Hours are totaled on a weekly
basis. This report is ideal for regular review of employee hours on a
weekly basis..

Timecard Summary
- Displays total Regular Hours, Break Hours, OT1 Hours, OT2 Hours,
OT3 Hours, OT4 Hours, Other Hours, and Other Amount for the selected date
range for each employee with Timecards during the selected date range.

# Report Examples

Employee
Information Reports

### Accrual Posting

The Accrual Posting Report will display a list of all accrual posting
records for the employees over a specific period of time.  An accrual
posting includes both individual dates on which an employee earned hours,
including the number of hours accrued, and the individual dates the employee
used hours, including the number of hours used.

The number of hours accrued, and the time period between accrual posting
records, is based on an employee's assigned Accrual Type and respective
Accrual Calculations.

Report Example:

![](images_2/Accrual_Posting.gif)

Notes/Usage:

The Accrual Posting Report has been redesigned as of InfiniTime 7.08.
The Accrual Posting Report now displays all accrual posting records, or
specific instances where an employee either earns or uses Accrued Hours,
during the selected date range.

Options:

| Option | Default Value | Description |
| Allow Graphics On the Report? | Yes | This option allows you to choose if you want to print the InfiniTime 7.0 logo on the report. |
| Department Selection Based On? | Employee Default Department | This option will allow you to select how the Department  filter is used to select employees. By default, departments tagged on the selection criteria will cause InfiniTime to display employees assigned to that department on the report. Alternatively, selecting 'Worked in Department' will show employees that worked in the selected department during the selected date range. |
| Group by Department? | No | This option will group employees specified by the Employee Filter according to their Default Department. |
| Group by Job? | No | This option will group employees specified by the Employee Filter according to their Default Job. |
| Group by Supervisor? | No | This option will group employees specified by the Employee Filter according to their Default Supervisor. |
| Group by Task? | No | This option will group employees specified by the Employee Filter according to their Default Task. |
| Group level to group by: | None | This option will sort employees specified by the Employee Filter according to their group description for the selected group level. For example, a company with multiple locations might have a Group Level of 'Location' and Group Descriptions of 'Pittsburgh' , 'Phoenix' , and 'Jacksonville'. Selecting the 'Location' group level would sort employees according to their assigned location. |
| Job Selection Based On: | Employee Default Job | This option will allow you to select how the Job filter is used to select employees. By default, jobs tagged on the selection criteria will cause InfiniTime to display employees assigned to the job on the report. Alternatively, selecting 'Worked in Job'' will show employees that worked in the selected job during the chosen date range. |
| Page Break by Department? | No | This option will allow you page break the report based on the Employee's Default Department, making it easier to give the report to department heads for review if needed. |
| Page Break by Employee? | No | This option will allow you to page break the report based on each employee, making it easier to give the report to the individual employees for review. |
| Page Break by Group? | No | This option will allow you to page break the report based on each Group Description and is intended for use with 'Group Level to Group By.' The report can then be distributed as necessary. |
| Page Break by Job? | No | This option will allow you to page break the report based on the Employee's Default Job, making it easier to give the reports to Job Supervisors for review. |
| Page Break by Supervisors? | No | This option will allow you to page break the report based on Employee Supervisors, making it easier to distribute to Supervisors for review. |
| Page Break by Task? | No | This option will allow you to page break the report based on the Employee's Default Job, making it easier to give the reports to Task Supervisors for review. |
| Print Inactive Employees? | No | This option will allow you to print information of the inactive employees along with the active ones. |
| Sort by Employee Number? | No | This option will group employees specified by the Employee Filter according to their Employee ID. |
| Task Selection Based On: | Employee Default Task | This option will allow you to select how the Task filter is used to select employees. By default, tasks tagged on the selection criteria will cause InfiniTime to display employees assigned to the task on the report. Alternatively, selecting 'Worked in Task'' will show employees that worked in the selected task during the chosen date range. |

### Employee Accruals

The Employee Accruals Report will display the total
accrued hours along with the amount of time used and the remaining balance
of the accrual.

Report Example:

![](images_2/AccrualWages_Example.gif)

Notes/Usage:

This report will show the total amount of accrued and available hours
for employees across all accrual calculations.

Options:

| Option | Default Value | Description |
| Allow Graphics On the Report? | Yes | This option allows you to choose if you want to print the InfiniTime 7.0 logo on the report. |
| Group by Department? | No | This option will group employees specified by the Employee Filter according to their Default Department. |
| Group by Job? | No | This option will group employees specified by the Employee Filter according to their Default Job. |
| Group by Supervisor? | No | This option will group employees specified by the Employee Filter according to their Default Supervisor. |
| Group by Task? | No | This option will group employees specified by the Employee Filter according to their Default Task. |
| Group level to group by: | None | This option will sort employees specified by the Employee Filter according to their group description for the selected group level. For example, a company with multiple locations might have a Group Level of 'Location' and Group Descriptions of 'Pittsburgh' , 'Phoenix' , and 'Jacksonville'. Selecting the 'Location' group level would sort employees according to their assigned location. |
| Page Break by Department? | No | This option will allow you page break the report based on the Employee's Default Department, making it easier to give the report to department heads for review if needed. |
| Page Break by Employee? | No | This option will allow you to page break the report based on each employee, making it easier to give the report to the individual employees for review. |
| Page Break by Group? | No | This option will allow you to page break the report based on each Group Description and is intended for use with 'Group Level to Group By.' The report can then be distributed as necessary. |
| Page Break by Job? | No | This option will allow you to page break the report by Job, making it easier to give the reports to Job Supervisors for review. |
| Page Break by Supervisors? | No | This option will allow you to page break the report based on Employee Supervisors, making it easier to distribute to Supervisors for review. |
| Page Break by Task? | No | This option will allow you to page break the report by Task, making it easier to give the reports to Task Supervisors for review. |
| Print Accrued Earnings? | No | When set to Yes, Total Accrued Earnings will be displayed on the report. Total Accrued Earnings are calculated by multiplying Total Accrued Hours by the employee's default wage. |
| Print Inactive Employees? | No | This option will allow you to print information of the inactive employees along with the active ones. |
| Print Remaining Accrued Earnings? | No | When set to Yes, Remaining Accrued Earnings will be displayed on the report. Remaining Accrued Earnings are calculated by multiplying Remaining Accrued Hours by the employee's default wage. |
| Show Accruals that Have Zero Hours Accrued? | No | This option will allow you display all accrual types even if they have not accrued hours. |
| Sort by Employee Number? | No | This option will group employees specified by the Employee Filter according to their Employee ID. |

### Employee Badges

This report will allow you to print your own employee
badges, either barcode or magnetic stripe badges, also it allows you to
choose from vertical or horizontal badge alignment. Employee ID, Employee
Name, Employee Picture, Default Department, Job Title are included on
the badge.

Report Example:

![](images_2/Employee_Badges.gif)

Notes/Usage:

This report is useful for printing your own employee badges if you have
a badge printer.

Options:

| Option | Default Value | Description |
| Allow Graphics On the Report? | Yes | This option allows you to choose if you want to print the InfiniTime 7.0 logo on the report. |
| Badge Printing Direction | Horizontal | This option allows you to select the orientation of the badge either Horizontal or Vertical. |
| Encoding Type | Barcode | This option allows you to select the type of encoding done on the badge, you can choose from Barcode, Magnetic stripe, or none. |
| Group by Department | No | This option will allow you to group the employees by department based on the selection you have made either Employee Default Department or Employee Worked in Department. |
| Group by Job? | No | This option will group employees specified by the Employee Filter according to their Default Job. |
| Group by Supervisor? | No | This option will group employees specified by the Employee Filter according to their Supervisor. |
| Group by Task? | No | This option will group employees specified by the Employee Filter according to their Default Task. |
| Group level to group by: | No | This option will sort employees specified by the Employee Filter according to their group description for the selected group level. For example, a company with multiple locations might have a Group Level of 'Location' and Group Descriptions of 'Pittsburgh' , 'Phoenix' , and 'Jacksonville'. Selecting the 'Location' group level would sort employees according to their assigned location. |
| Magnetic Stripe Track Number | 1 | This option will allow you to select the track number encoding for magnetic stripe cards, you can choose from track 1, 2, or 3. |
| Print Inactive Employees? | No | This option will allow you to print information of the inactive employees along with the active ones. |
| Sort by Employee Number? | No | This option will group employees specified by the Employee Filter according to their Employee ID. |

### Employee Incoming Messages

This report will print a list of all the incoming
messages an employee has received in a specific period of time.

Report Example:

![](images_2/Employee_Incomming_Messages.gif)

Notes/Usage:

This report is useful to see what messages an employee has received
in a period of time.

Options:

| Option | Default Value | Description |
| Allow Graphics On the Report? | Yes | This option allows you to choose if you want to print the InfiniTime 7.0 logo on the report. |
| Department Selection Based On? | Employee Default Department | This option will allow you to select how the Department  filter is used to select employees. By default, departments tagged on the selection criteria will cause InfiniTime to display employees assigned to that department on the report. Alternatively, selecting 'Worked in Department' will show employees that worked in the selected department during the selected date range. |
| Group by Department? | No | This option will group employees specified by the Employee Filter by Department. |
| Group by Job? | No | This option will group employees specified by the Employee Filter by Job. |
| Group by Supervisor? | No | This option will group employees specified by the Employee Filter according to their Default Supervisor. |
| Group by Task? | No | This option will group employees specified by the Employee Filter by Task. |
| Group level to group by: | None | This option will sort employees specified by the Employee Filter according to their group description for the selected group level. For example, a company with multiple locations might have a Group Level of 'Location' and Group Descriptions of 'Pittsburgh' , 'Phoenix' , and 'Jacksonville'. Selecting the 'Location' group level would sort employees according to their assigned location. |
| Job Selection Based On: | Employee Default Job | This option will allow you to select how the Job filter is used to select employees. By default, jobs tagged on the selection criteria will cause InfiniTime to display employees assigned to the job on the report. Alternatively, selecting 'Worked on Job'' will show employees that worked in the selected job during the chosen date range. |
| Page Break by Department? | No | This option will allow you page break the report by Department, making it easier to give the report to department heads for review if needed. |
| Page Break by Employee? | No | This option will allow you to page break the report by each employee, making it easier to give the report to the individual employees for review. |
| Page Break by Group? | No | This option will allow you to page break the report by each Group Description and is intended for use with 'Group Level to Group By.' The report can then be distributed as necessary. |
| Page Break by Job? | No | This option will allow you to page break the report by Job, making it easier to give the reports to Job Supervisors for review. |
| Page Break by Message? | No | This option will print each employee message on a new page. |
| Page Break by Supervisors? | No | This option will allow you to page break the report based on Employee Supervisors, making it easier to distribute to Supervisors for review. |
| Page Break by Task? | No | This option will allow you to page break the report by Job, making it easier to give the reports to Task Supervisors for review. |
| Print Employee Name Header? | Yes | Enables and Disables the employee name header. By default, this option is enabled and a header is printed before each employee to separate received and sent messages for the employee. |
| Print Inactive Employees? | No | This option will allow you to print information of the inactive employees along with the active ones. |
| Sort by Employee Number? | No | This option will group employees specified by the Employee Filter according to their Employee ID. |
| Task Selection Based On: | Employee Default Task | This option will allow you to select how the Task filter is used to select employees. By default, tasks tagged on the selection criteria will cause InfiniTime to display employees assigned to the task on the report. Alternatively, selecting 'Worked in Task'' will show employees that worked in the selected task during the chosen date range. |

### Employee List

This report will print a list of all employees
included in the report selection criteria.  Employee ID, Default
Department, Job Title, Hire Date, Employee Badge Number and Employee Log
In Number are also included in the report.

Report
Example:

![](images_2/Employee_List.gif)

Notes/Usage:

This report is useful for creating a list of all employees within a
specific department or group.

Options:

| Option | Default Value | Description |
| Allow Graphics On the Report? | Yes | This option allows you to choose if you want to print the InfiniTime 7.0 logo on the report. |
| Group by Department? | No | This option will group employees specified by the Employee Filter according to their Default Department. |
| Group by Job? | No | This option will group employees specified by the Employee Filter according to their Default Job. |
| Group by Supervisor? | No | This option will group employees specified by the Employee Filter according to their Default Supervisor. |
| Group by Task? | No | This option will group employees specified by the Employee Filter according to their Default Task. |
| Group level to group by: | None | This option will sort employees specified by the Employee Filter according to their group description for the selected group level. For example, a company with multiple locations might have a Group Level of 'Location' and Group Descriptions of 'Pittsburgh' , 'Phoenix' , and 'Jacksonville'. Selecting the 'Location' group level would sort employees according to their assigned location. |
| Page Break by Department? | No | This option will allow you page break the report based on the Employee's Default Department, making it easier to give the report to department heads for review if needed. |
| Page Break by Employee? | No | This option will allow you to page break the report based on each employee, making it easier to give the report to the individual employees for review. |
| Page Break by Group? | No | This option will allow you to page break the report based on each Group Description and is intended for use with 'Group Level to Group By.' The report can then be distributed as necessary. |
| Page Break by Job? | No | This option will allow you to page break the report based on the Employee's Default Job, making it easier to give the reports to Job Supervisors for review. |
| Page Break by Supervisors? | No | This option will allow you to page break the report based on Employee Supervisors, making it easier to distribute to Supervisors for review. |
| Page Break by Task? | No | This option will allow you to page break the report based on the Employee's Default Job, making it easier to give the reports to Task Supervisors for review. |
| Print Badge ID? | Yes | This option will enable or disable display of the employee Badge ID on the report. |
| Print Inactive Employees? | No | This option will allow you to print information of the inactive employees along with the active ones. |
| Print Login ID? | Yes | This option will enable or disable display of the Employee Login ID on the report. |
| Sort by Employee Number? | No | This option will group employees specified by the Employee Filter according to their Employee ID. |

## Employee List By Supervisor

Displays a list of all employees grouped by the supervisor they are
assigned to.  Employee ID, Employee Name, Default Department, Job
Title, Hire Date, and Employee Badge numbers are also included on this
report.

Report Example:

![](images_2/Employee_List_With_Supervisors.gif)

Notes/Usage:

This report is useful for knowing what employees are assigned to supervisors.

Options:

| Option | Default Value | Description |
| Allow Graphics On the Report? | Yes | This option allows you to choose if you want to print the InfiniTime 7.0 logo on the report. |
| Group by Department? | No | This option will allow you to group the employees by department based on the selection you have made either Employee Default Department or Employee Worked in Department. |
| Page Break by Department? | No | This option will allow you page break the report by department, making it easier to give the reports to department heads for review if needed. |
| Page Break by Employee? | No | This option will allow you to page break the report based on each employee, making it easier to give the report to the individual employees for review. |
| Print Inactive Employees? | No | This option will allow you to print information of the inactive employees along with the active ones. |

# Employee New Hire

Displays a list of employees that have been hired in the specific date
range selected on the selection criteria of the report.  Employee
ID, Employee Name, Default Department, Job Title, Hire Date, and Employee
Badge numbers are also included on this report.

Report Example:

![](images_2/Employee_New_Hire.gif)

Notes/Usage:

This report is useful for knowing what employees have been recently
hired.

Options:

| Option | Default Value | Description |
| Allow Graphics On the Report? | Yes | This option allows you to choose if you want to print the InfiniTime 7.0 logo on the report. |
| Department Selection Based On? | Employee Default Department | This option will allow you to select how the Department  filter is used to select employees. By default, departments tagged on the selection criteria will cause InfiniTime to display employees assigned to that department on the report. Alternatively, selecting 'Worked in Department' will show employees that worked in the selected department during the selected date range. |
| Group by Department? | No | This option will group employees specified by Department. |
| Group by Job? | No | This option will group employees specified by Job. |
| Group by Supervisor? | No | This option will group employees specified by the Employee Filter according to their Default Supervisor. |
| Group by Task? | No | This option will group employees specified by Task. |
| Group level to group by: | None | This option will sort employees specified by the Employee Filter according to their group description for the selected group level. For example, a company with multiple locations might have a Group Level of 'Location' and Group Descriptions of 'Pittsburgh' , 'Phoenix' , and 'Jacksonville'. Selecting the 'Location' group level would sort employees according to their assigned location. |
| Job Selection Based On: | Employee Default Job | This option will allow you to select how the Job filter is used to select employees. By default, jobs tagged on the selection criteria will cause InfiniTime  to display employees assigned to the job on the report. Alternatively, selecting 'Worked in Job'' will show employees that worked in the selected job during the chosen date range. |
| Page Break by Department? | No | This option will allow you page break the report by Department, making it easier to give the report to department heads for review if needed. |
| Page Break by Employee? | No | This option will allow you to page break the report based on each employee, making it easier to give the report to the individual employees for review. |
| Page Break by Group? | No | This option will allow you to page break the report based on each Group Description and is intended for use with 'Group Level to Group By.' The report can then be distributed as necessary. |
| Page Break by Job? | No | This option will allow you to page break the report by Job, making it easier to give the reports to Job Supervisors for review. |
| Page Break by Supervisor? | No | This option will allow you to page break the report based on Employee Supervisors, making it easier to distribute to Supervisors for review. |
| Page Break by Task? | No | This option will allow you to page break the report by Task, making it easier to give the reports to Task Supervisors for review. |
| Print Inactive Employees? | No | This option will allow you to print information of the inactive employees along with the active ones. |
| Sort by Employee Number? | No | This option will group employees specified by the Selection Criteria according to their Employee ID. |
| Task Selection Based On: | Employee Default Task | This option will allow you to select how the Task filter is used to select employees. By default, tasks tagged on the selection criteria will cause InfiniTime to display employees assigned to the task on the report. Alternatively, selecting 'Worked in Task'' will show employees that worked in the selected task during the chosen date range. |

# Employee Outgoing Messages

Displays a list of all the Outgoing messages an employee has made for
a specific period of time.

Report
Example:

![](images_2/Employee_Outgoing_Messages.gif)

Notes/Usage:

This report is useful to see what messages an employee has sent over
a period of time.

Options:

| Option | Default Value | Description |
| Allow Graphics On the Report? | Yes | This option allows you to choose if you want to print the InfiniTime 7.0 logo on the report. |
| Department Selection Based On? | Employee Default Department | This option will allow you to select how the Department  filter is used to select employees. By default, departments tagged on the selection criteria will cause InfiniTime to display employees assigned to that department on the report. Alternatively, selecting 'Worked in Department' will show employees that worked in the selected department during the selected date range. |
| Group by Department? | No | This option will group employees specified by  Department. |
| Group by Job? | No | This option will group employees specified by Job. |
| Group by Supervisor? | No | This option will group employees specified by the Employee Filter according to their Default Supervisor. |
| Group by Task? | No | This option will group employees specified by Task. |
| Group level to group by: | None | This option will sort employees specified by the Employee Filter according to their group description for the selected group level. For example, a company with multiple locations might have a Group Level of 'Location' and Group Descriptions of 'Pittsburgh' , 'Phoenix' , and 'Jacksonville'. Selecting the 'Location' group level would sort employees according to their assigned location. |
| Job Selection Based On: | Employee Default Job | This option will allow you to select how the Job filter is used to select employees. By default, jobs tagged on the selection criteria will cause InfiniTime to display employees assigned to the job on the report. Alternatively, selecting 'Worked in Job'' will show employees that worked in the selected job during the chosen date range. |
| Page Break by Department? | No | This option will allow you page break the report based by Department, making it easier to give the report to department heads for review if needed. |
| Page Break by Employee? | No | This option will allow you to page break the report based on each employee, making it easier to give the report to the individual employees for review. |
| Page Break by Group? | No | This option will allow you to page break the report based on each Group Description and is intended for use with 'Group Level to Group By.' The report can then be distributed as necessary. |
| Page Break by Job? | No | This option will allow you to page break the report by Job, making it easier to give the reports to Job Supervisors for review. |
| Page Break by Message? | No | This option will print each employee message on a new page. |
| Page Break by Supervisor? | No | This option will allow you to page break the report based on Employee Supervisors, making it easier to distribute to Supervisors for review. |
| Page Break by Task? | No | This option will allow you to page break the report by Task, making it easier to give the reports to Task Supervisors for review. |
| Print Employee Name Header? | Yes | Enables and Disables the employee name header. By default, this option is enabled and a header is printed before each employee to separate received and sent messages for the employee. |
| Print Inactive Employees? | No | This option will allow you to print information of the inactive employees along with the active ones. |
| Sort by Employee Number? | No | This option will group employees specified by the Employee Filter according to their Employee ID. |
| Task Selection Based On: | Employee Default Task | This option will allow you to select how the Task filter is used to select employees. By default, tasks tagged on the selection criteria will cause InfiniTime to display employees assigned to the task on the report. Alternatively, selecting 'Worked in Task'' will show employees that worked in the selected task during the chosen date range. |

## Employee Profiles

Displays all employee information as entered into the Employee Table.
A separate sheet is generated for each employee.

Report
Example:

![](images_2/Employee_Profiles_1.gif)

![](images_2/Employee_Profiles_2.gif)

![](images_2/Employee_Profiles_3.gif)

![](images_2/Employee_Profiles_4.gif)

Notes/Usage:

This report gathers and displays all employee related HR information
in one location.

Options:

| Option | Default Value | Description |
| Allow Graphics On the Report? | Yes | This option allows you to choose if you want to print the InfiniTime 7.0 logo on the report. |
| Group by Department? | No | This option will group employees specified by the Employee Filter according to their Default Department. |
| Page Break by Department? | No | This option will allow you page break the report based on the Employee's Default Department, making it easier to give the report to department heads for review if needed. |
| Page Break by Employee? | No | This option will allow you to page break the report based on each employee, making it easier to give the report to the individual employees for review. |
| Print Inactive Employees? | No | This option will allow you to print information of the inactive employees along with the active ones. |
| Show Employee Picture? | Yes | This option allows you to print the employee picture on the report. |
| Sort by Employee Name? | Yes | This option allows you to sort the report by the last name of the employees if set to yes or by the employee number if set to no. |

# Important Date

Displays a list of important dates, as defined within the employee table,
for the specified employees.

Report Example:

![](images_2/Important_Dates.gif)

Notes/Usage:

This report is useful to see what important dates might be approaching
for employees. The Important Dates Report can display Important Dates
in both current and future years.

Options:

  

| Option | Default Value | Description |
| Allow Graphics On the Report? | Yes | This option allows you to choose if you want to print the InfiniTime 7.0 logo on the report. |
| Department Selection Based On? | Employee Default Department | This option will allow you to select how the Department  filter is used to select employees. By default, departments tagged on the selection criteria will cause InfiniTime to display employees assigned to that department on the report. Alternatively, selecting 'Worked in Department' will show employees that worked in the selected department during the selected date range. |
| Group by Department? | No | This option will group employees specified by the Employee Filter by Department. |
| Group by Job? | No | This option will group employees specified by the Employee Filter by Job. |
| Group by Supervisor? | No | This option will group employees specified by the Employee Filter according to their Default Supervisor. |
| Group by Task? | No | This option will group employees specified by the Employee Filter by Task. |
| Group level to group by: | None | This option will sort employees specified by the Employee Filter according to their group description for the selected group level. For example, a company with multiple locations might have a Group Level of 'Location' and Group Descriptions of 'Pittsburgh' , 'Phoenix' , and 'Jacksonville'. Selecting the 'Location' group level would sort employees according to their assigned location. |
| Job Selection Based On: | Employee Default Job | This option will allow you to select how the Job filter is used to select employees. By default, jobs tagged on the selection criteria will cause InfiniTime to display employees assigned to the job on the report. Alternatively, selecting 'Worked in Job'' will show employees that worked in the selected job during the chosen date range. |
| Page Break by Department? | No | This option will allow you page break the report based on the Employee's Default Department, making it easier to give the report to department heads for review if needed. |
| Page Break by Employee? | No | This option will allow you to page break the report based on each employee, making it easier to give the report to the individual employees for review. |
| Page Break by Group? | No | This option will allow you to page break the report based on each Group Description and is intended for use with 'Group Level to Group By.' The report can then be distributed as necessary. |
| Page Break by Job? | No | This option will allow you to page break the report based on the Employee's Default Job, making it easier to give the reports to Job Supervisors for review. |
| Page Break by Supervisor? | No | This option will allow you to page break the report based on Employee Supervisors, making it easier to distribute to Supervisors for review. |
| Page Break by Task? | No | This option will allow you to page break the report by Task, making it easier to give the reports to Task Supervisors for review. |
| Print Inactive Employees? | No | This option will allow you to print information of the inactive employees along with the active ones. |
| Sort by Employee Number? | No | This option will group employees specified by the Employee Filter according to their Employee ID. |
| Task Selection Based On: | Employee Default Task | This option will allow you to select how the Task filter is used to select employees. By default, tasks tagged on the selection criteria will cause InfiniTime to display employees assigned to the task on the report. Alternatively, selecting 'Worked in Task'' will show employees that worked in the selected task during the chosen date range. |

## In & Out Board

Displays the working status for the employees specified by Selection
Criteria. Employees currently clocked in will be reported as IN and employees
currently clocked out will be reported as OUT.

Report
Example:

![](images_2/SW_CH10_In_OutBoard.gif)

Notes/Usage:

This report is useful to see which employees are currently clocked in
or out and can be used as an 'On Premise' report for security and emergency
purposes. The footer option is particularly useful for this function as
it displays a total count of employees who are clocked in and clocked
out which can be used to take a head count.

Options:

| Option | Default Value | Description |
| Allow Graphics On the Report? | Yes | This option allows you to choose if you want to print the InfiniTime 7.0 logo on the report. |
| Display In and Out Time | No | This option will allow you to show the time at which employees last clocked in or out on the report. |
| Group by Department? | No | This option will group employees specified by the Employee Filter by Department. |
| Group by Job? | No | This option will group employees specified by the Employee Filter by Job. |
| Group by Supervisor? | No | This option will group employees specified by the Employee Filter by Supervisor. |
| Group by Task? | No | This option will group employees specified by the Employee Filter by Task. |
| Group level to group by: | None | This option will sort employees specified by the Employee Filter according to their group description for the selected group level. For example, a company with multiple locations might have a Group Level of 'Location' and Group Descriptions of 'Pittsburgh' , 'Phoenix' , and 'Jacksonville'. Selecting the 'Location' group level would sort employees according to their assigned location. |
| Page Break by Department? | No | This option will allow you page break the report based on the Employee's Default Department, making it easier to give the report to department heads for review if needed. |
| Page Break by Employee? | No | This option will allow you to page break the report based on each employee, making it easier to give the report to the individual employees for review. |
| Page Break by Group? | No | This option will allow you to page break the report based on each Group Description and is intended for use with 'Group Level to Group By.' The report can then be distributed as necessary. |
| Page Break by Job? | No | This option will allow you to page break the report by Job, making it easier to give the reports to Job Supervisors for review. |
| Page Break by Supervisor? | No | This option will allow you to page break the report based on Employee Supervisors, making it easier to distribute to Supervisors for review. |
| Page Break by Task? | No | This option will allow you to page break the report by Task, making it easier to give the reports to Task Supervisors for review. |
| Print Footer? | No | This option adds a Report Total Row to the end of the report displaying a total count of employees that are Clocked In, Clocked Out, in addition to a grand total.  A Sub Footer is also displayed for each Department, Job, Task, and / or Supervisor when the report is grouped by Department, Job, Task, Group, or Supervisor. |
| Print Inactive Employees? | No | This option will allow you to print information of the inactive employees along with the active ones. |
| Show Me Employees That Are? | All Employees | This option allows you to select which employees will display on the report based on their status either clocked in, clocked out or show you all employees. |
| Sort by Employee Number? | No | This option will group employees specified by the Employee Filter according to their Employee ID. |

# User Defined Fields

Displays all information related to User Defined Fields as defined within
the employee table for employees specified by Selection Criteria.

Options:

| Option | Default Value | Description |
| Allow Graphics On the Report? | Yes | This option allows you to choose if you want to print the InfiniTime 7.0 logo on the report. |
| Group by Department? | No | This option will group employees specified by the Employee Filter by Department. |
| Group by Job? | No | This option will group employees specified by the Employee Filter by Job. |
| Group by Supervisor? | No | This option will group employees specified by the Employee Filter by Supervisor. |
| Group by Task? | No | This option will group employees specified by the Employee Filter by Task. |
| Group level to group by: | None | This option will sort employees specified by the Employee Filter according to their group description for the selected group level. For example, a company with multiple locations might have a Group Level of 'Location' and Group Descriptions of 'Pittsburgh' , 'Phoenix' , and 'Jacksonville'. Selecting the 'Location' group level would sort employees according to their assigned location. |
| Page Break by Department? | No | This option will allow you page break the report by Department, making it easier to give the report to department heads for review if needed. |
| Page Break by Employee? | No | This option will allow you to page break the report based on each employee, making it easier to give the report to the individual employees for review. |
| Page Break by Group? | No | This option will allow you to page break the report based on each Group Description and is intended for use with 'Group Level to Group By.' The report can then be distributed as necessary. |
| Page Break by Job? | No | This option will allow you to page break the report by Job, making it easier to give the reports to Job Supervisors for review. |
| Page Break by Supervisor? | No | This option will allow you to page break the report based on Employee Supervisors, making it easier to distribute to Supervisors for review. |
| Page Break by Task? | No | This option will allow you to page break the report by Task, making it easier to give the reports to Task Supervisors for review. |
| Print Inactive Employees? | No | This option will allow you to print information of the inactive employees along with the active ones. |
| Sort by Employee Number? | No | This option will group employees specified by the Employee Filter according to their Employee ID. |

# Job Cost Reports

## Employee Job Daily Summary

Displays Employe Hours, grouped by job,  for each day in the specified
date range.

Report
Example:

![](images_2/Rpt021.png)

Notes/Usage:

* Useful for viewing hours distribution across multiple jobs for
  a specific employees on a day by day basis.
* Provides a Grand Total for each Day in the Selected Date Range
  for each employee.

Options:

The Employee
Job Daily Summary Report is a User Customizable Report. Please see the
[User Customizable
Reports section](/InfiniTime/help%20file/Overview/Reports/Reports.md#rpt16_User_Customizable_Reports) of this document for more information on configuring
options for User Customizable Reports.

## Employee Job Summary

Displays total employee hours, grouped by job, for the specified date
range.

Report
Example:

![](images_2/Rpt022.png)

Notes/Usage:

* Useful for viewing hours distribution across multiple jobs for
  specific employees across a date range.

Options:

The Employee
Job  Summary Report is a User Customizable Report. Please see the
[User Customizable
Reports section](/InfiniTime/help%20file/Overview/Reports/Reports.md#rpt16_User_Customizable_Reports) of this document for more information on configuring
options for User Customizable Reports.

## Job Daily Summary

Displays total hours for each day in the specified date range. Hours
are Grouped first by Job then by Employee.

Report
Example:

![](images_2/Rpt023.png)

Notes/Usage:

* Useful for viewing labor distribution across multiple jobs on a
  day by day basis.
* Displays a grand total record for each job on each date in the
  selected date range.

Options:

The Job
Daily Summary Report is a User Customizable Report. Please see the
[User Customizable
Reports section](/InfiniTime/help%20file/Overview/Reports/Reports.md#rpt16_User_Customizable_Reports) of this document for more information on configuring
options for User Customizable Reports.

## Job List

Lists all Jobs configured in the InfiniTime
Application.

Report Example:

![](images_2/Rpt024.png)

Options:

| Option | Default Value | Description |
| Allow Graphics On the Report? | Yes | This option allows you to choose if you want to print the InfiniTime 7.0 logo on the report. |
| Print Inactive Jobs? | No | This option allows you to display Inactive Jobs on the Job List Report. |

## Job Summary

Displays total hours, grouped by job, for the specified date range.

Report
Example:

![](images_2/Rpt025.png)

Notes/Usage:

* Useful for viewing labor distribution across multiple jobs for
  a date range.
* Displays a grand total record for each job with hours in the selected
  date range.

Options:

The Job Summary Report is a User Customizable Report. Please see
the [User Customizable
Reports section](/InfiniTime/help%20file/Overview/Reports/Reports.md#rpt16_User_Customizable_Reports) of this document for more information on configuring
options for User Customizable Reports.

# Management Reports

## Access Control

Displays access information related to an entryway. Access logs are
displayed for employees specified by Selection Criteria.

Options:

| Option | Default Value | Description |
| Allow Graphics On the Report? | Yes | This option allows you to choose if you want to print the InfiniTime 7.0 logo on the report. |
| Department Selection Based On? | Employee Default Department | This option will allow you to select how the Department  filter is used to select employees. By default, departments tagged on the selection criteria will cause InfiniTime to display employees assigned to that department on the report. Alternatively, selecting 'Worked in Department' will show employees that worked in the selected department during the selected date range. |
| Group by Department? | No | This option will group employees specified by the Employee Filter by Department. |
| Group by Job? | No | This option will group employees specified by the Employee Filter by Job. |
| Group by Supervisor? | No | This option will group employees specified by the Employee Filter according to their Default Supervisor. |
| Group by Task? | No | This option will group employees specified by the Employee Filter by Task. |
| Group level to group by: | None | This option will sort employees specified by the Employee Filter according to their group description for the selected group level. For example, a company with multiple locations might have a Group Level of 'Location' and Group Descriptions of 'Pittsburgh' , 'Phoenix' , and 'Jacksonville'. Selecting the 'Location' group level would sort employees according to their assigned location. |
| Job Selection Based On: | Employee Default Job | This option will allow you to select how the Job filter is used to select employees. By default, jobs tagged on the selection criteria will cause InfiniTime to display employees assigned to the job on the report. Alternatively, selecting 'Worked in Job'' will show employees that worked in the selected job during the chosen date range. |
| Page Break by Department? | No | This option will allow you page break the report by Department, making it easier to give the report to department heads for review if needed. |
| Page Break by Employee? | No | This option will allow you to page break the report based on each employee, making it easier to give the report to the individual employees for review. |
| Page Break by Group? | No | This option will allow you to page break the report based on each Group Description and is intended for use with 'Group Level to Group By.' The report can then be distributed as necessary. |
| Page Break by Job? | No | This option will allow you to page break the report by Job, making it easier to give the reports to Job Supervisors for review. |
| Page Break by Supervisor? | No | This option will allow you to page break the report based on Employee Supervisors, making it easier to distribute to Supervisors for review. |
| Page Break by Task? | No | This option will allow you to page break the report by Task, making it easier to give the reports to Task Supervisors for review. |
| Print Inactive Employees? | No | This option will allow you to print information of the inactive employees along with the active ones. |
| Sort by Employee Number? | No | This option will group employees specified by the Employee Filter according to their Employee ID. |
| Task Selection Based On: | Employee Default Task | This option will allow you to select how the Task filter is used to select employees. By default, tasks tagged on the selection criteria will cause InfiniTime to display employees assigned to the task on the report. Alternatively, selecting 'Worked in Task'' will show employees that worked in the selected task during the chosen date range. |

## Audit Trail

Displays Audit information for the employees specified by Selection
Criteria. Information about the changes made to timecard records as well
as which employee made the changes can be found on this report.

Report Example:

![](images_2/Audit_Trail.gif)

Notes/Usage:

* Useful for reviewing alterations to timecard punches performed
  during a specific date range.
* Useful for reviewing all alterations to timecard punches within
  a specific date range, regardless of when the alterations were made.
* Displays Full Audit Details for Insert, Change, and Delete Actions.

Options:

| Option | Default Value | Description |
| Allow Graphics On the Report? | Yes | This option allows you to choose if you want to print the InfiniTime 7.0 logo on the report. |
| Date Selection Based On: | Audit Date | This option controls how Audit Records are selected for display on the report. If 'Audit Date' is selected, audit trail records for Timecard Alterations performed during the Selected Date Range will be displayed. Alternatively, if 'Activity Date' is selected, all audit trail records for Timecard Records within the selected date range will be displayed. |
| Department Selection Based On? | Employee Default Department | This option will allow you to select how the Department  filter is used to select employees. By default, departments tagged on the selection criteria will cause InfiniTime to display employees assigned to that department on the report. Alternatively, selecting 'Worked in Department' will show employees that worked in the selected department during the selected date range. |
| Group by Department? | No | This option will group Audit Records by Department. |
| Group by Job? | No | This option will group Audit Records by Job. |
| Group by Supervisor? | No | This option will group employees specified by the Employee Filter according to their Default Supervisor. |
| Group by Task? | No | This option will group Audit Records by Task. |
| Group level to group by: | None | This option will sort employees specified by the Employee Filter according to their group description for the selected group level. For example, a company with multiple locations might have a Group Level of 'Location' and Group Descriptions of 'Pittsburgh' , 'Phoenix' , and 'Jacksonville'. Selecting the 'Location' group level would sort employees according to their assigned location. |
| Job Selection Based On: | Employee Default Job | This option will allow you to select how the Job filter is used to select employees. By default, jobs tagged on the selection criteria will cause InfiniTime to display employees assigned to the job on the report. Alternatively, selecting 'Worked in Job'' will show employees that worked in the selected job during the chosen date range. |
| Page Break by Department? | No | This option will allow you page break the report by Department, making it easier to give the report to department heads for review if needed. |
| Page Break by Employee? | No | This option will allow you to page break the report based on each employee, making it easier to give the report to individual employees for review. |
| Page Break by Group? | No | This option will allow you to page break the report based on each Group Description and is intended for use with 'Group Level to Group By.' The report can then be distributed as necessary. |
| Page Break by Job? | No | This option will allow you to page break the report based on the Employee's Default Job, making it easier to give the reports to Job Supervisors for review. |
| Page Break by Supervisor? | No | This option will allow you to page break the report based on Employee Supervisors, making it easier to distribute to Supervisors for review. |
| Page Break by Task? | No | This option will allow you to page break the report by Task, making it easier to give the reports to Task Supervisors for review. |
| Print Inactive Employees? | No | This option will allow you to print information for both Active and Inactive Employees. |
| Show System Audits? | No | This option will allow you display all system audits on the report.  System Audits include auto punch, Auto breaks, change to breaks, and Intellipunch changes. |
| Sort by Employee Number? | No | This option will group employees specified by the Employee Filter according to their Employee ID. |
| Task Selection Based On: | Employee Default Task | This option will allow you to select how the Task filter is used to select employees. By default, tasks tagged on the selection criteria will cause InfiniTime to display employees assigned to the task on the report. Alternatively, selecting 'Worked in Task'' will show employees that worked in the selected task during the chosen date range. |

## Employee Exception Detail

Displays Employee Names and Employee ID Numbers as a header with each
exception during the selected date range as a detail record. Detail records
also include the employee's Time In and Time Out for the respective day
along with total hours. Useful for viewing all exceptions during a specific
date range or for viewing all exceptions for specific employee(s) during
a given date range.

Report
Example:

![](images_2/Exception_Detail.gif)

Notes/Usage:

This report will show all the exceptions for the employee in the specified
time, if you want to limit what exceptions to show you will need to select
the desired exceptions and also in the options set it to only display
selected exceptions. for example we just want to see the missed punches
for a period  you would tag missed punch on the selection criteria
and the option to limit to selected exceptions set it to yes and this
is the result.

![](images_2/Exception_Detail_Limited.gif)

Options:

| Option | Default Value | Description |
| Allow Graphics On the Report? | Yes | This option allows you to choose if you want to print the InfiniTime 7.0 logo on the report. |
| Department Selection Based On? | Employee Default Department | This option will allow you to select how the Department  filter is used to select employees. By default, departments tagged on the selection criteria will cause InfiniTime to display employees assigned to that department on the report. Alternatively, selecting 'Worked in Department' will show employees that worked in the selected department during the selected date range. |
| Group by Department? | No | This option will group employees specified by the Employee Filter by Department. |
| Group by Job? | No | This option will group employees specified by the Employee Filter by Job. |
| Group by Supervisor? | No | This option will group employees specified by the Employee Filter according to their Default Supervisor. |
| Group by Task? | No | This option will group employees specified by the Employee Filter by Task. |
| Group level to group by: | None | This option will sort employees specified by the Employee Filter according to their group description for the selected group level. For example, a company with multiple locations might have a Group Level of 'Location' and Group Descriptions of 'Pittsburgh' , 'Phoenix' , and 'Jacksonville'. Selecting the 'Location' group level would sort employees according to their assigned location. |
| Job Selection Based On: | Employee Default Job | This option will allow you to select how the Job filter is used to select employees. By default, jobs tagged on the selection criteria will cause InfiniTime to display employees assigned to the job on the report. Alternatively, selecting 'Worked in Job'' will show employees that worked in the selected job during the chosen date range. |
| Limit to Selected Exception Types? | No | Alters how the Exception tab of the Selection Criteria Settings functions. When set to yes, only the specific exceptions tagged on the Selection Criteria will be displayed. When set to no, all exceptions occurring within the selected date range will be displayed for employees who have at least one of the exception types identified by the Selection Criteria. |
| Page Break by Department? | No | This option will allow you to page break the report by Department, making it easier to give the report to department heads for review if needed. |
| Page Break by Employee? | No | This option will allow you to page break the report based on each employee, making it easier to give the report to the individual employees for review. |
| Page Break by Group? | No | This option will allow you to page break the report based on each Group Description and is intended for use with 'Group Level to Group By.' The report can then be distributed as necessary. |
| Page Break by Job? | No | This option will allow you to page break the report by Job, making it easier to give the reports to Job Supervisors for review. |
| Page Break by Supervisor? | No | This option will allow you to page break the report based on Employee Supervisors, making it easier to distribute to Supervisors for review. |
| Page Break by Task? | No | This option will allow you to page break the report by Task, making it easier to give the reports to Task Supervisors for review. |
| Print Time in Hours and Minutes? | No | This option will allow you to print the time in hours and minutes instead of hundredths of an hour. |
| Sort by Employee Number? | No | This option will group employees specified by the Employee Filter according to their Employee ID. |
| Task Selection Based On: | Employee Default Task | This option will allow you to select how the Tob filter is used to select employees. By default, tasks tagged on the selection criteria will cause InfiniTime to display employees assigned to the task on the report. Alternatively, selecting 'Worked in Task'' will show employees that worked in the selected task during the chosen date range. |

## Employee Exception Summary

Displays each exception during the selected date range as a header record,
with individual employees who triggered the exception along with the number
of instances each employee had for the respective exception as detail
records.

Report Example:

![](images_2/Rpt010.png)

Options:

| Option | Default Value | Description |
| Allow Graphics On the Report? | Yes | This option allows you to choose if you want to print the InfiniTime 7.0 logo on the report. |
| Department Selection Based On? | Employee Default Department | This option will allow you to select how the Department  filter is used to select employees. By default, departments tagged on the selection criteria will cause InfiniTime to display employees assigned to that department on the report. Alternatively, selecting 'Worked in Department' will show employees that worked in the selected department during the selected date range. |
| Group by Department? | No | This option will group employees specified by the Employee Filter by Department. |
| Group by Exception? | Yes | Controls the sorting of employee Exceptions on the Exception Summary Report by the Exception Name. When set to no, the Exception Name Header will not be displayed. |
| Group by Job? | No | This option will group employees specified by Job. |
| Group by Supervisor? | No | This option will group employees specified by Supervisor. |
| Group by Task? | No | This option will group employees specified by Task. |
| Group level to group by: | None | This option will sort employees specified by the Employee Filter according to their group description for the selected group level. For example, a company with multiple locations might have a Group Level of 'Location' and Group Descriptions of 'Pittsburgh' , 'Phoenix' , and 'Jacksonville'. Selecting the 'Location' group level would sort employees according to their assigned location. |
| Job Selection Based On: | Employee Default Job | This option will allow you to select how the Job filter is used to select employees. By default, jobs tagged on the selection criteria will cause InfiniTime to display employees assigned to the job on the report. Alternatively, selecting 'Worked in Job'' will show employees that worked in the selected job during the chosen date range. |
| Limit to Selected Exception Types? | No | Permits filtering by Exception Types specified by the Report Selection Criteria. If this option is set to Yes, only tagged exceptions will be displayed on the report. |
| Page Break by Department? | No | This option will allow you page break the report by Department, making it easier to give the report to department heads for review if needed. |
| Page Break by Exception? | No | This option will allow you page break the report based on the Exception Type, making it easier to review specific exception types individually.. |
| Page Break by Group? | No | This option will allow you to page break the report based on each Group Description and is intended for use with 'Group Level to Group By.' The report can then be distributed as necessary. |
| Page Break by Job? | No | This option will allow you to page break the report by Job, making it easier to give the reports to Job Supervisors for review. |
| Page Break by Supervisor? | No | This option will allow you to page break the report based on Employee Supervisors, making it easier to distribute to Supervisors for review. |
| Page Break by Task? | No | This option will allow you to page break the report by Task, making it easier to give the reports to Task Supervisors for review. |
| Sort by Employee Number? | No | This option will group employees specified by the Employee Filter according to their Employee ID. |
| Task Selection Based On: | Employee Default Task | This option will allow you to select how the Task filter is used to select employees. By default, tasks tagged on the selection criteria will cause InfiniTime to display employees assigned to the task on the report. Alternatively, selecting 'Worked in Task'' will show employees that worked in the selected task during the chosen date range. |

# Employee Points

Displays Employee Points as accumulated from exceptions within the date
range specified by Selection Criteria.

Report Example:

![](images_2/Employee_Points.gif)

Notes/Usage:

Exception Points can be used to track overall employee performance.
Employees who are continuously tardy or who often leave early will have
a noticeably higher point score than employees who arrive and depart according
to their schedule.

Options:

| Option | Default Value | Description |
| Allow Graphics On the Report? | Yes | This option allows you to choose if you want to print the InfiniTime 7.0 logo on the report. |
| Department Selection Based On? | Employee Default Department | This option will allow you to select how the Department  filter is used to select employees. By default, departments tagged on the selection criteria will cause InfiniTime to display employees assigned to that department on the report. Alternatively, selecting 'Worked in Department' will show employees that worked in the selected department during the selected date range. |
| Group by Department? | No | This option will group employees specified by the Employee Filter by Department. |
| Group by Job? | No | This option will group employees specified by the Employee Filter by Job. |
| Group by Supervisor? | No | This option will group employees specified by the Employee Filter by Supervisor. |
| Group by Task? | No | This option will group employees specified by the Employee Filter by Task. |
| Group level to group by: | None | This option will sort employees specified by the Employee Filter according to their group description for the selected group level. For example, a company with multiple locations might have a Group Level of 'Location' and Group Descriptions of 'Pittsburgh' , 'Phoenix' , and 'Jacksonville'. Selecting the 'Location' group level would sort employees according to their assigned location. |
| Job Selection Based On: | Employee Default Job | This option will allow you to select how the Job filter is used to select employees. By default, jobs tagged on the selection criteria will cause InfiniTime to display employees assigned to the job on the report. Alternatively, selecting 'Worked in Job'' will show employees that worked in the selected job during the chosen date range. |
| Page Break by Department? | No | This option will allow you page break the report by Department, making it easier to give the report to department heads for review if needed. |
| Page Break by Employee? | No | This option will allow you to page break the report based on each employee, making it easier to give the report to the individual employees for review. |
| Page Break by Group? | No | This option will allow you to page break the report based on each Group Description and is intended for use with 'Group Level to Group By.' The report can then be distributed as necessary. |
| Page Break by Job? | No | This option will allow you to page break the report by Job, making it easier to give the reports to Job Supervisors for review. |
| Page Break by Supervisor? | No | This option will allow you to page break the report based on Employee Supervisors, making it easier to distribute to Supervisors for review. |
| Page Break by Task? | No | This option will allow you to page break the report by Task, making it easier to give the reports to Task Supervisors for review. |
| Print Inactive Employees? | No | This option will allow you to print information of the inactive employees along with the active ones. |
| Sort by Employee Number? | No | This option will group employees specified by the Employee Filter according to their Employee ID. |
| Task Selection Based On: | Employee Default Task | This option will allow you to select how the Task filter is used to select employees. By default, tasks tagged on the selection criteria will cause InfiniTime to display employees assigned to the task on the report. Alternatively, selecting 'Worked in Task'' will show employees that worked in the selected task during the chosen date range. |

## Employees With Exceptions

Displays a list of employees that have exceptions within the date range
specified by Selection Criteria.

Report
Example:

![](images_2/Employee_With_Exceptions.gif)

Notes/Usage:

This report will show a list of employees that have exceptions in the
specified time, if you want to limit  the list of employees to only
show employees with a specific exception you will need to select the desired
exceptions and also in the options set it to only display selected exceptions.

Options:

| Option | Default Value | Description |
| Allow Graphics On the Report? | Yes | This option allows you to choose if you want to print the InfiniTime 7.0 logo on the report. |
| Department Selection Based On? | Employee Default Department | This option will allow you to select how the Department  filter is used to select employees. By default, departments tagged on the selection criteria will cause InfiniTime to display employees assigned to that department on the report. Alternatively, selecting 'Worked in Department' will show employees that worked in the selected department during the selected date range. |
| Group by Department? | No | This option will group employees specified by the Employee Filter by Department. |
| Group by Job? | No | This option will group employees specified by Job. |
| Group by Supervisor? | No | This option will group employees specified by the Employee Filter according to their Default Supervisor. |
| Group by Task? | No | This option will group employees specified by Task. |
| Group level to group by: | None | This option will sort employees specified by the Employee Filter according to their group description for the selected group level. For example, a company with multiple locations might have a Group Level of 'Location' and Group Descriptions of 'Pittsburgh' , 'Phoenix' , and 'Jacksonville'. Selecting the 'Location' group level would sort employees according to their assigned location. |
| Job Selection Based On: | Employee Default Job | This option will allow you to select how the Job filter is used to select employees. By default, jobs tagged on the selection criteria will cause InfiniTime to display employees assigned to the job on the report. Alternatively, selecting 'Worked in Job'' will show employees that worked in the selected job during the chosen date range. |
| Limit to Selected Exception Types? | No | Alters how the Exception tab of the Selection Criteria Settings functions. When set to yes, only the specific exceptions tagged on the Selection Criteria will be displayed. When set to no, all exceptions occurring within the selected date range will be displayed for employees who have the exception types identified by the Selection Criteria. |
| Page Break by Department? | No | This option will allow you page break the report by Department, making it easier to give the report to department heads for review if needed. |
| Page Break by Employee? | No | This option will allow you to page break the report based on each employee, making it easier to give the report to the individual employees for review. |
| Page Break by Group? | No | This option will allow you to page break the report based on each Group Description and is intended for use with 'Group Level to Group By.' The report can then be distributed as necessary. |
| Page Break by Job? | No | This option will allow you to page break the report by Job, making it easier to give the reports to Job Supervisors for review. |
| Page Break by Supervisor? | No | This option will allow you to page break the report based on Employee Supervisors, making it easier to distribute to Supervisors for review. |
| Page Break by Task? | No | This option will allow you to page break the report by Task, making it easier to give the reports to Task Supervisors for review. |
| Print Exception Detail? | No | When set to Yes, employee exceptions will be displayed on the report. |
| Sort by Employee Number? | No | This option will group employees specified by the Employee Filter according to their Employee ID. |
| Task Selection Based On: | Employee Default Task | This option will allow you to select how the Task filter is used to select employees. By default, tasks tagged on the selection criteria will cause InfiniTime to display employees assigned to the task on the report. Alternatively, selecting 'Worked in Task'' will show employees that worked in the selected task during the chosen date range. |

## Employee With Zero Hours

Displays a list of employees that have no hours worked in the date range
specified by the Selection Criteria.

Report Example:

![](images_2/Employee_With_Zero_Hours.gif)

Notes/Usage:

This report is useful to see which employees do not have any hours for
a date range.

Options:

| Option | Default Value | Description |
| Allow Graphics On the Report? | Yes | This option allows you to choose if you want to print the InfiniTime 7.0 logo on the report. |
| Department Selection Based On? | Employee Default Department | This option will allow you to select how the Department  filter is used to select employees. By default, departments tagged on the selection criteria will cause InfiniTime to display employees assigned to that department on the report. Alternatively, selecting 'Worked in Department' will show employees that worked in the selected department during the selected date range. |
| Group by Department? | No | This option will group employees specified by  Department. |
| Group by Job? | No | This option will group employees specified by Job. |
| Group by Supervisor? | No | This option will group employees specified by the Employee Filter according to their Default Supervisor. |
| Group by Task? | No | This option will group employees specified by Task. |
| Group level to group by: | None | This option will sort employees specified by the Employee Filter according to their group description for the selected group level. For example, a company with multiple locations might have a Group Level of 'Location' and Group Descriptions of 'Pittsburgh' , 'Phoenix' , and 'Jacksonville'. Selecting the 'Location' group level would sort employees according to their assigned location. |
| Job Selection Based On: | Employee Default Job | This option will allow you to select how the Job filter is used to select employees. By default, jobs tagged on the selection criteria will cause InfiniTime to display employees assigned to the job on the report. Alternatively, selecting 'Worked in Job'' will show employees that worked in the selected job during the chosen date range. |
| Page Break by Department? | No | This option will allow you page break the report by Department, making it easier to give the report to department heads for review if needed. |
| Page Break by Employee? | No | This option will allow you to page break the report based on each employee, making it easier to give the report to the individual employees for review. |
| Page Break by Group? | No | This option will allow you to page break the report based on each Group Description and is intended for use with 'Group Level to Group By.' The report can then be distributed as necessary. |
| Page Break by Job? | No | This option will allow you to page break the report by Job, making it easier to give the reports to Job Supervisors for review. |
| Page Break by Supervisor? | No | This option will allow you to page break the report based on Employee Supervisors, making it easier to distribute to Supervisors for review. |
| Page Break by Task? | No | This option will allow you to page break the report by Task, making it easier to give the reports to Task Supervisors for review. |
| Print Inactive Employees? | No | This option will allow you to print information of the inactive employees along with the active ones. |
| Sort by Employee Number? | No | This option will group employees specified by the Employee Filter according to their Employee ID. |
| Task Selection Based On: | Employee Default Task | This option will allow you to select how the Task filter is used to select employees. By default, tasks tagged on the selection criteria will cause InfiniTime to display employees assigned to the task on the report. Alternatively, selecting 'Worked in Task'' will show employees that worked in the selected task during the chosen date range. |

## Employee Without Reviewed Timecards

Displays a list of employees with one or more Unreviewed Timecard Record
records during the Selected Date Range.

Report
Example:

![](images_2/Employee_Without_Reviewed_Timecards.gif)

Notes/Usage:

* Depending on how report options are configured, the Unreviewed
  Timecard Report has the ability to display employees who:

+ Have one or more timecard records during the date range which
  have not been reviewed by their supervisor
+ Have one or more timecard records during the date range which
  have not been reviewed by the employee
+ Have one or more timecard records during the date range which
  have not been reviewed by at least X different users

* It is important to note that any changes to a timecard record after
  it is marked 'Reviewed' will remove the 'Reviewed' Status. This is
  by design.
* In order to view all employees that have not yet been reviewed
  by the employee's supervisor within the specified period, run this
  report with the default selection criteria and alter only the date
  range.
* In order to view all employees that have one or more unreviewed
  timecard records, with no specific requirement as to who performed
  the review, run this report for the desired date range and default
  selection criteria with the following options:

+ Alert When Number of Reviews are Less Than 1
+ Alert When Timecards are Not Reviewed by Supervisor = No

Options:

| Option | Default Value | Description |
| Alert When Number of Reviews are Less Than? | 0 | If an employee has one or more timecard records with less than the number of reviews indicated by this option they will be listed on the report. |
| Alert When Timecards are Not Reviewed by Employee? | No | When set to Yes, Employees with timecards that have not been reviewed by the employee they will be listed on the report. |
| Alert When Timecards are Not Reviewed by Supervisor? | Yes | When set to Yes, Employees with timecards that have not been reviewed by their assigned Supervisor will be listed on the report. |
| Allow Graphics On the Report? | Yes | This option allows you to choose if you want to print the InfiniTime 7.0 logo on the report. |
| Department Selection Based On? | Employee Default Department | This option will allow you to select how the Department  filter is used to select employees. By default, departments tagged on the selection criteria will cause InfiniTime to display employees assigned to that department on the report. Alternatively, selecting 'Worked in Department' will show employees that worked in the selected department during the selected date range. |
| Group by Department? | No | This option will group employees specified by the Employee Filter by Department. |
| Group by Job? | No | This option will group employees specified by the Employee Filter by Job. |
| Group by Supervisor? | No | This option will group employees specified by the Employee Filter according to their Default Supervisor. |
| Group by Task? | No | This option will group employees specified by the Employee Filter by Task. |
| Group level to group by: | None | This option will sort employees specified by the Employee Filter according to their group description for the selected group level. For example, a company with multiple locations might have a Group Level of 'Location' and Group Descriptions of 'Pittsburgh' , 'Phoenix' , and 'Jacksonville'. Selecting the 'Location' group level would sort employees according to their assigned location. |
| Job Selection Based On: | Employee Default Job | This option will allow you to select how the Job filter is used to select employees. By default, jobs tagged on the selection criteria will cause InfiniTime to display employees assigned to the job on the report. Alternatively, selecting 'Worked in Job'' will show employees that worked in the selected job during the chosen date range. |
| Page Break by Department? | No | This option will allow you page break the report by Department, making it easier to give the report to department heads for review if needed. |
| Page Break by Employee? | No | This option will allow you to page break the report based on each employee, making it easier to give the report to the individual employees for review. |
| Page Break by Group? | No | This option will allow you to page break the report based on each Group Description and is intended for use with 'Group Level to Group By.' The report can then be distributed as necessary. |
| Page Break by Job? | No | This option will allow you to page break the report by Job, making it easier to give the reports to Job Supervisors for review. |
| Page Break by Supervisor? | No | This option will allow you to page break the report based on Employee Supervisors, making it easier to distribute to Supervisors for review. |
| Page Break by Task? | No | This option will allow you to page break the report by Task, making it easier to give the reports to Task Supervisors for review. |
| Print Inactive Employees? | No | This option will allow you to print information of the inactive employees along with the active ones. |
| Sort by Employee Number? | No | This option will group employees specified by the Employee Filter according to their Employee ID. |
| Task Selection Based On: | Employee Default Task | This option will allow you to select how the Task filter is used to select employees. By default, tasks tagged on the selection criteria will cause InfiniTime to display employees assigned to the task on the report. Alternatively, selecting 'Worked in Task'' will show employees that worked in the selected task during the chosen date range. |

# Excessive Hours

Displays a list of employees
who have worked excessive hours within the date range specified by Selection
Criteria. The amount of hours required to work in order to be considered
as working excessive hours is configured within company policies.

Report Example:

![](images_2/Rpt013.png)

Notes/Usage:

This report is useful to see
which employees have worked over the Excessive Hours Amount as set on
each employee's respective policy. The Excessive Hours Amount is set on
the Overtime Rules Section of the Policy Update Form on the General Tab
as shown below.

![](images_2/Rpt012.png)

Options:

| Option | Default Value | Description |
| Allow Graphics On the Report? | Yes | This option allows you to choose if you want to print the InfiniTime 7.0 logo on the report. |
| Department Selection Based On? | Employee Default Department | This option will allow you to select how the Department  filter is used to select employees. By default, departments tagged on the selection criteria will cause InfiniTime to display employees assigned to that department on the report. Alternatively, selecting 'Worked in Department' will show employees that worked in the selected department during the selected date range. |
| Group by Department? | No | This option will group employees specified by  Department. |
| Group by Job? | No | This option will group employees specified by Job. |
| Group by Supervisor? | No | This option will group employees specified by the Employee Filter according to their Default Supervisor. |
| Group by Task? | No | This option will group employees specified by Task. |
| Group level to group by: | None | This option will sort employees specified by the Employee Filter according to their group description for the selected group level. For example, a company with multiple locations might have a Group Level of 'Location' and Group Descriptions of 'Pittsburgh' , 'Phoenix' , and 'Jacksonville'. Selecting the 'Location' group level would sort employees according to their assigned location. |
| Job Selection Based On: | Employee Default Job | This option will allow you to select how the Job filter is used to select employees. By default, jobs tagged on the selection criteria will cause InfiniTime to display employees assigned to the job on the report. Alternatively, selecting 'Worked in Job'' will show employees that worked in the selected job during the chosen date range. |
| Page Break by Department? | No | This option will allow you page break the report based on the Employee's Default Department, making it easier to give the report to department heads for review if needed. |
| Page Break by Employee? | No | This option will allow you to page break the report based on each employee, making it easier to give the report to the individual employees for review. |
| Page Break by Group? | No | This option will allow you to page break the report based on each Group Description and is intended for use with 'Group Level to Group By.' The report can then be distributed as necessary. |
| Page Break by Job? | No | This option will allow you to page break the report by Job, making it easier to give the reports to Job Supervisors for review. |
| Page Break by Supervisor? | No | This option will allow you to page break the report based on Employee Supervisors, making it easier to distribute to Supervisors for review. |
| Page Break by Task? | No | This option will allow you to page break the report by Task, making it easier to give the reports to Task Supervisors for review. |
| Print Company Grand Totals? | No | When set to Yes a total record will be added to the end of the report displaying total Excessive Hours for the entire company. |
| Print Inactive Employees? | No | This option will allow you to print information of the inactive employees along with the active ones. |
| Sort by Employee Number? | No | This option will group employees specified by the Employee Filter according to their Employee ID. |
| Task Selection Based On: | Employee Default Task | This option will allow you to select how the Task filter is used to select employees. By default, tasks tagged on the selection criteria will cause InfiniTime to display employees assigned to the task on the report. Alternatively, selecting 'Worked in Task'' will show employees that worked in the selected task during the chosen date range. |

# Failed Biometric Verification

Displays a list of employees who have failed biometric verification
within the date range specified by Selection Criteria.

Notes/Usage:

Abrupt changes in hand geometry can lead to biometric verification failure.
This may occur when excessively long fingernails are cut or if excessively
long fake nails are applied. It may be necessary to re-enroll an employee
within the Hand Reader under these circumstances. Otherwise, if employees
are having trouble with hand verification try raising the Reject Level,
which will reduce hand reader sensitivity. Refer to the Scout Reader Configuration
section of this document for more information.  Also you can check
if in fact the employee tried to punch in or they are just trying to beat
the system and say that the reader did not scan their hand or finger depending
of the biometric solution you have.

Options:

| Option | Default Value | Description |
| Allow Graphics On the Report? | Yes | This option allows you to choose if you want to print the InfiniTime 7.0 logo on the report. |
| Department Selection Based On? | Employee Default Department | This option will allow you to select how the Department  filter is used to select employees. By default, departments tagged on the selection criteria will cause InfiniTime to display employees assigned to that department on the report. Alternatively, selecting 'Worked in Department' will show employees that worked in the selected department during the selected date range. |
| Group by Department? | No | This option will group employees specified by Department. |
| Group by Job? | No | This option will group employees specified by Job. |
| Group by Supervisor? | No | This option will group employees specified by the Employee Filter according to their Default Supervisor. |
| Group by Task? | No | This option will group employees specified by Task. |
| Group level to group by: | None | This option will sort employees specified by the Employee Filter according to their group description for the selected group level. For example, a company with multiple locations might have a Group Level of 'Location' and Group Descriptions of 'Pittsburgh' , 'Phoenix' , and 'Jacksonville'. Selecting the 'Location' group level would sort employees according to their assigned location. |
| Job Selection Based On: | Employee Default Job | This option will allow you to select how the Job filter is used to select employees. By default, jobs tagged on the selection criteria will cause InfiniTime to display employees assigned to the job on the report. Alternatively, selecting 'Worked in Job'' will show employees that worked in the selected job during the chosen date range. |
| Page Break by Department? | No | This option will allow you page break the report by Department, making it easier to give the report to department heads for review if needed. |
| Page Break by Employee? | No | This option will allow you to page break the report based on each employee, making it easier to give the report to the individual employees for review. |
| Page Break by Group? | No | This option will allow you to page break the report based on each Group Description and is intended for use with 'Group Level to Group By.' The report can then be distributed as necessary. |
| Page Break by Job? | No | This option will allow you to page break the report by Job, making it easier to give the reports to Job Supervisors for review. |
| Page Break by Supervisor? | No | This option will allow you to page break the report based on Employee Supervisors, making it easier to distribute to Supervisors for review. |
| Page Break by Task? | No | This option will allow you to page break the report by Job, making it easier to give the reports to Task Supervisors for review. |
| Print Inactive Employees? | No | This option will allow you to print information of the inactive employees along with the active ones. |
| Sort by Employee Number? | No | This option will group employees specified by the Employee Filter according to their Employee ID. |
| Task Selection Based On: | Employee Default Task | This option will allow you to select how the Task filter is used to select employees. By default, tasks tagged on the selection criteria will cause InfiniTime to display employees assigned to the task on the report. Alternatively, selecting 'Worked in Task'' will show employees that worked in the selected task during the chosen date range. |

## Overtime Utilization

Permits users to calculate Total Overtime Hours, Total Working Hours,
and a resulting percentage over the Date Range specified in the Report
Selection Criteria. One detail record is displayed for each employee with
overtime hours during the selected date range. Detail records can be grouped
by Department, Job, Task, and Supervisor. Additionally, the user has full
control over which hours types are counted as 'Total Overtime Hours' vs
'Total Working Hours'.

Report Example:

![](images_2/Rpt014.png)

Options:

| Option | Default Value | Description |
| Allow Graphics On the Report? | Yes | This option allows you to choose if you want to print the InfiniTime 7.0 logo on the report. |
| Count OT1 Hours Toward Total OT Hours? | Yes | Permits the user to control the hours types counted toward Total OT Hours. If this option is set to No, OT1 Hours will not be counted toward Total OT Hours for purposes of calculating the Overtime Utilization Percentage. |
| Count OT1 Hours Toward Total Working Hours? | Yes | Permits the user to control the hours types counted toward Total Working Hours. If this option is set to No, OT1 Hours will not be counted toward Total Working Hours for purposes of calculating the Overtime Utilization Percentage. |
| Count OT2 Hours Toward Total OT Hours? | Yes | Permits the user to control the hours types counted toward Total OT Hours. If this option is set to No, OT2 Hours will not be counted toward Total OT Hours for purposes of calculating the Overtime Utilization Percentage. |
| Count OT2 Hours Toward Total Working Hours? | Yes | Permits the user to control the hours types counted toward Total Working Hours. If this option is set to No, OT2 Hours will not be counted toward Total Working Hours for purposes of calculating the Overtime Utilization Percentage. |
| Count OT3 Hours Toward Total OT Hours? | Yes | Permits the user to control the hours types counted toward Total OT Hours. If this option is set to No, OT3 Hours will not be counted toward Total OT Hours for purposes of calculating the Overtime Utilization Percentage. |
| Count OT3 Hours Toward Total Working Hours? | Yes | Permits the user to control the hours types counted toward Total Working Hours. If this option is set to No, OT3 Hours will not be counted toward Total Working Hours for purposes of calculating the Overtime Utilization Percentage. |
| Count OT4 Hours Toward Total OT Hours? | Yes | Permits the user to control the hours types counted toward Total OT Hours. If this option is set to No, OT4 Hours will not be counted toward Total OT Hours for purposes of calculating the Overtime Utilization Percentage. |
| Count OT4 Hours Toward Total Working Hours? | Yes | Permits the user to control the hours types counted toward Total Working Hours. If this option is set to No, OT4 Hours will not be counted toward Total Working Hours for purposes of calculating the Overtime Utilization Percentage. |
| Count Other Hours for Tagged Other Activity Types toward Total Working Hours? | No | Permits the user to control the hours types counted toward Total Working Hours. If this option is set to Yes, Other Hours for all tagged other Activity Types which are not\* set to count as Regular Hours will be counted toward Total Worked Hours.    If this option is set to No, Other Activity Types with  'Count as Regular Hours' unchecked will not be counted toward Total Working Hours or Total OT Hours even if they are tagged. |
| Count REG Hours toward Total Working Hours? | Yes | Permits the user to control the hours types counted toward Total Working Hours. If this option is set to No, Regular Hours will not be counted toward Total Working Hours for purposes of calculating the Overtime Utilization Percentage. |
| Department Grouping Type? | None | This option allows you to group the report by the employees Activity Department, meaning that the hours will distribute to all the departments the employee worked, or group by Employee Default Department,which will put all the time worked in their default department even if they worked on other departments, or the last option is None. |
| Department Selection Based On? | Employee Default Department | This option will allow you to select how the Department  filter is used to select employees. By default, departments tagged on the selection criteria will cause InfiniTime to display employees assigned to that department on the report. Alternatively, selecting 'Worked in Department' will show employees that worked in the selected department during the selected date range. |
| Department Selection Filters Activity? | No | If this option is set to Yes, employee Timecard Records displayed on the report will be filtered according to tagged departments as follows:     1.) Only employees with hours in the tagged department(s) will be displayed on the report.  2.) Only timecard records assigned to the tagged department(s) will be used to calculate totals for display on the report. All other timecard records for employees will ignored when this option is set to Yes. |
| Group level to group by: | None | This option will sort employees specified by the Employee Filter according to their group description for the selected group level. For example, a company with multiple locations might have a Group Level of 'Location' and Group Descriptions of 'Pittsburgh' , 'Phoenix' , and 'Jacksonville'. Selecting the 'Location' group level would sort employees according to their assigned location. |
| Job Grouping Type? | None | Determines how employees will be grouped by Jobs. When set to None the option is considered disabled and employees will not be grouped by jobs.  When set to Employee Default Job employees will be grouped according to their default job as assigned on their employee record. When set to Employee Worked On Job employees will be grouped according to the job they worked in. |
| Job Selection Based On: | Employee Default Job | This option will allow you to select how the Job filter is used to select employees. By default, jobs tagged on the selection criteria will cause InfiniTime to display employees assigned to the job on the report. Alternatively, selecting 'Worked in Job'' will show employees that worked in the selected job during the chosen date range. |
| Job Selection Filters Activity? | No | If this option is set to Yes, employee Timecard Records displayed on the report will be filtered according to tagged departments as follows:     1.) Only employees with hours in the tagged Job(s) will be displayed on the report.  2.) Only timecard records assigned to the tagged Job(s) will be used to calculate totals for display on the report. All other timecard records for employees will ignored when this option is set to Yes. |
| Page Break by Department? | No | This option will allow you page break the report by Department, making it easier to give the report to department heads for review if needed. |
| Page Break by Group? | No | This option will allow you to page break the report based on each Group Description and is intended for use with 'Group Level to Group By.' The report can then be distributed as necessary. |
| Page Break by Job? | No | This option will allow you to page break the report by, making it easier to give the reports to Job Supervisors for review. |
| Page Break by Task? | No | This option will allow you to page break the report by Task, making it easier to give the reports to Task Supervisors for review. |
| Print Inactive Employees? | No | This option will allow you to print information of the inactive employees along with the active ones. |
| Print Time in Hours and Minutes? | No | This option changes the Time Format from Hours and Hundredths of Hours (IE: 8.50 Hours for an 8:00 AM to 4:30 PM shift) to Hours and Minutes (IE: 8h 30m) |
| Sort by Employee Number? | No | This option will group employees specified by the Employee Filter according to their Employee ID. |
| Task Grouping Type? | None | Determines how employees will be grouped by Tasks. When set to None the option is considered disabled and employees will not be grouped by tasks. When set to Employee Default Task employees will be grouped according to their default task as assigned on their employee record. When set to Scheduled Task employees will be grouped according to the task they were scheduled to work in. |
| Task Selection Based On: | Employee Default Task | This option will allow you to select how the Task filter is used to select employees. By default, tasks tagged on the selection criteria will cause InfiniTime to display employees assigned to the tagged task(s) on the report. Alternatively, selecting 'Worked in Task'' will show employees that worked in the selected task during the chosen date range. |
| Task Selection Filters Activity? | No | If this option is set to Yes, employee Timecard Records displayed on the report will be filtered according to tagged tasks as follows:     1.) Only employees with hours in the tagged tasks will be displayed on the report.  2.) Only timecard records assigned to the tagged task(s) will be used to calculate totals for display on the report. All other timecard records for employees will ignored when this option is set to Yes. |
| Total Hours for Tagged Other Activity Types according to Report Hours Options? | No | Permits the user to control the hours types counted toward Total Working Hours and Total OT Hours for Other Activity Types which are set to count as regular hours. If this option is set to Yes, Regular, OT1, OT2, OT3, and OT4 hours for Tagged Other Activity Types will be counted toward Total Working Hours and Total OT Hours in accordance with the 'Count REG/OT1/OT2/OT3/OT4' Toward 'Total OT Hours/Total Working Hours' options.    If this option is set to No, Other Activity Types set to 'Count as Regular Hours' will not be counted toward Total Working Hours or Total OT Hours even if they are tagged. |

## Scheduled Overtime Early Warning

The Scheduled Overtime Early Warning Report is intended for use over
a given work week to anticipate employee overtime hours based on the number
of hours already worked for an employee throughout the week and the remaining
number of scheduled hours. The Scheduled Overtime Early Warning Report
is especially useful for environments with dynamic schedules and cross
trained employees. In this way, if it is observed an individual would
earn overtime hours with their existing schedule, the employee's schedule
may be altered and another employee can be called in to fill the gap.

Report Example:

![](images_2/image151.gif)

Notes / Usage:

* This report is especially useful for organizations with Dynamic
  Scheduling (IE: Staffing Requirements increase due to workload / Customer
  Demand) and can be used to manage / reduce unnecessary overtime.
* The Scheduled Overtime Early Warning Report is most useful when
  executed toward the end of the week, such as on Wednesday and Thursday.
* In this way, supervisors can identify employees who would earn
  overtime if they worked their remaining scheduled hours.
* The Scheduled Overtime Early Warning Report answers four important
  questions for personnel managers:

+ a. How many hours does the employee have for the work week
  already?
+ b. How many hours is the employee scheduled for in the rest
  of the work week?
+ c. How many hours would the employee have for the work week
  if they worked their remaining scheduled hours? Would the employee
  exceed 40 hours?
+ d. If so, when would the employee hit 40 hours?

Options:

| Option | Default Value | Description |
| Allow Graphics On the Report? | Yes | This option allows you to choose if you want to print the InfiniTime 7.0 logo on the report. |
| Department Grouping Type? | None | This option allows you to group the report by the employees Activity Department, meaning that the hours will distribute to all the departments the employee worked, or group by Employee Default Department,which will put all the time worked in their default department even if they worked on other departments, or the last option is None. |
| Department Selection Filters Activity? | No | If this option is set to Yes, employee Timecard Records displayed on the report will be filtered according to tagged departments as follows:     1.) Only employees with hours in the tagged department(s) will be displayed on the report.  2.) Only timecard records assigned to the tagged department(s) will be used to calculate totals for display on the report. All other timecard records for employees will ignored when this option is set to Yes. |
| Employee Signature Message | None | Permits the user to specify a disclaimer or message to be displayed under the employee signature line. The Employee Signature message will only be displayed on the Report if 'Print Employee Signature Line?' is set to Yes. |
| Group by Supervisor | No | This option will group employees specified by the Employee Filter according to their assigned Supervisor. |
| Group level to group by: | None | This option will sort employees specified by the Employee Filter according to their group description for the selected group level. For example, a company with multiple locations might have a Group Level of 'Location' and Group Descriptions of 'Pittsburgh' , 'Phoenix' , and 'Jacksonville'. Selecting the 'Location' group level would sort employees according to their assigned location. |
| Job Grouping Type? | None | Determines how employees will be grouped by Jobs. When set to None the option is considered disabled and employees will not be grouped by jobs.  When set to Employee Default Job employees will be grouped according to their default job as assigned on their employee record. When set to Employee Worked On Job employees will be grouped according to the job they worked in. |
| Job Selection Filters Activity? | No | If this option is set to Yes, employee Timecard Records displayed on the report will be filtered according to tagged departments as follows:     1.) Only employees with hours in the tagged Job(s) will be displayed on the report.  2.) Only timecard records assigned to the tagged Job(s) will be used to calculate totals for display on the report. All other timecard records for employees will ignored when this option is set to Yes. |
| Page Break by Department? | No | This option will allow you page break the report by Department, making it easier to give the report to department heads for review if needed. |
| Page Break by Employee? | No | This option will allow you to page break the report based on each employee, making it easier to give the report to the individual employees for review. |
| Page Break by Group? | No | This option will allow you to page break the report based on each Group Description and is intended for use with 'Group Level to Group By.' The report can then be distributed as necessary. |
| Page Break by Job? | No | This option will allow you to page break the report by Job, making it easier to give the reports to Job Supervisors for review. |
| Page Break by Supervisor? | No | This option will allow you to page break the report based on each supervisor, making it easier for individual supervisors to review hours for their specific employees. |
| Page Break by Task? | No | This option will allow you to page break the report by Task, making it easier to give the reports to Task Supervisors for review. |
| Print Employee Signature Line? | No | An employee signature line will be displayed at the bottom of the results for each employee if this option is enabled. Generally Page Break by Employee should be enabled when using this feature. |
| Print Inactive Employees? | No | This option will allow you to print information of the inactive employees along with the active ones. |
| Print Supervisor Signature Line? | No | A supervisor signature line will be displayed at the bottom of the results for each employee if this option is enabled. Generally Page Break by Employee should be enabled when using this feature. |
| Print Time in Hours and Minutes? | No | This option changes the Time Format from Hours and Hundredths of Hours (IE: 8.50 Hours for an 8:00 AM to 4:30 PM shift) to Hours and Minutes (IE: 8h 30m) |
| Show only Employees with Overtime? | Yes | If this option is set to Yes, only employees who would receive overtime hours according to their Forecasted Hours Total (IE: Worked Hours to Date for the selected date range + Scheduled Hours for remaining days in the selected date range) will be displayed on the report.    If this option is set to No, all employees will be displayed on the report. |
| Sort by Employee Number? | No | This option will group employees specified by the Employee Filter according to their Employee ID. |
| Supervisor Signature Message | None | Permits the user to specify a disclaimer or message to be displayed under the supervisor signature line. The Supervisor Signature message will only be displayed on the Report if 'Print Supervisor Signature Line?' is set to Yes. |
| Task Grouping Type? | None | Determines how employees will be grouped by Tasks. When set to None the option is considered disabled and employees will not be grouped by tasks. When set to Employee Default Task employees will be grouped according to their default task as assigned on their employee record. When set to Scheduled Task employees will be grouped according to the task they were scheduled to work in. |
| Task Selection Based On: | Employee Default Task | This option will allow you to select how the Task filter is used to select employees. By default, tasks tagged on the selection criteria will cause InfiniTime to display employees assigned to the tagged task(s) on the report. Alternatively, selecting 'Worked in Task'' will show employees that worked in the selected task during the chosen date range. |
| Task Selection Filters Activity? | No | If this option is set to Yes, employee Timecard Records displayed on the report will be filtered according to tagged tasks as follows:     1.) Only employees with hours in the tagged tasks will be displayed on the report.  2.) Only timecard records assigned to the tagged task(s) will be used to calculate totals for display on the report. All other timecard records for employees will ignored when this option is set to Yes. |

# Timecard Note Report

Displays all Timecard Notes in the selected date range for employees
specified by Selection Criteria. The Timecard Note Report can be found
under the Management Reports Category on the Report Library.

Report Example:

![](images_2/SW_CH11_NOTES_0008.gif)

Notes/Usage:

* The Timecard Note report is useful
  for displaying all timecard notes for a given date range when reviewing
  employee timecard records prior to payroll.
* Unlike Audit Trail Comments, Timecard
  Notes are not required for every altered punch. Timecard Notes are
  only inserted by supervisors for comments of material importance.

Options:

| Option | Default Value | Description |
| Allow Graphics On the Report? | Yes | This option allows you to choose if you want to print the InfiniTime 7.0 logo on the report. |
| Department Selection Based On? | Employee Default Department | This option will allow you to select how the Department  filter is used to select employees. By default, departments tagged on the selection criteria will cause InfiniTime to display employees assigned to that department on the report. Alternatively, selecting 'Worked in Department' will show employees that worked in the selected department during the selected date range. |
| Group by Department? | No | This option will group employees specified by the Employee Filter by Department. |
| Group by Employee? | No | This option will group employees specified by the Employee Filter by Last Name. |
| Group by Job? | No | This option will group employees specified by the Employee Filter by Job. |
| Group by Supervisor? | No | This option will group employees specified by the Employee Filter according to their Default Supervisor. |
| Group by Task? | No | This option will group employees specified by the Employee Filter by Task. |
| Group level to group by: | None | This option will sort employees specified by the Employee Filter according to their group description for the selected group level. For example, a company with multiple locations might have a Group Level of 'Location' and Group Descriptions of 'Pittsburgh' , 'Phoenix' , and 'Jacksonville'. Selecting the 'Location' group level would sort employees according to their assigned location. |
| Job Selection Based On: | Employee Default Job | This option will allow you to select how the Job filter is used to select employees. By default, jobs tagged on the selection criteria will cause InfiniTime to display employees assigned to the job on the report. Alternatively, selecting 'Worked in Job'' will show employees that worked in the selected job during the chosen date range. |
| Page Break by Department? | No | This option will allow you page break the report by Department, making it easier to give the report to department heads for review if needed. |
| Page Break by Employee? | No | This option will allow you to page break the report based on each employee, making it easier to give the report to the individual employees for review. |
| Page Break by Group? | No | This option will allow you to page break the report based on each Group Description and is intended for use with 'Group Level to Group By.' The report can then be distributed as necessary. |
| Page Break by Job? | No | This option will allow you to page break the report by Job, making it easier to give the reports to Job Supervisors for review. |
| Page Break by Supervisor? | No | This option will allow you to page break the report based on Employee Supervisors, making it easier to distribute to Supervisors for review. |
| Page Break by Task? | No | This option will allow you to page break the report by Task, making it easier to give the reports to Task Supervisors for review. |
| Print Inactive Employees? | No | This option will allow you to print information of the inactive employees along with the active ones. |
| Show System Audits? | No | This option will allow you display all system audits on the report.  System Audits include auto punch, Auto breaks, change to breaks. |
| Sort by Employee Number? | No | This option will group employees specified by the Employee Filter according to their Employee ID. |
| Task Selection Based On: | Employee Default Task | This option will allow you to select how the Task filter is used to select employees. By default, tasks tagged on the selection criteria will cause InfiniTime to display employees assigned to the task on the report. Alternatively, selecting 'Worked in Task'' will show employees that worked in the selected task during the chosen date range. |

# Who Is Where

Displays a list of all employees and which department they are currently
clocked into.

Report
Example:

![](images_2/Who_Is_Where.gif)

Notes/Usage:

This report is useful to see who is currently logged in into a particular
department.

Options:

| Option | Default Value | Description |
| Allow Graphics On the Report? | Yes | This option allows you to choose if you want to print the InfiniTime 7.0 logo on the report. |
| Display In and Out Time? | No | This option will allow you to display the In or Out time next to the department they are currently in. |
| Group by Department? | No | This option will group employees specified by the Employee Filter by Department. |
| Group by Job? | No | This option will group employees specified by the Employee Filter by Job. |
| Group by Supervisor? | No | This option will group employees specified by the Employee Filter according to their Default Supervisor. |
| Group by Task? | No | This option will group employees specified by the Employee Filter by Task. |
| Group level to group by: | None | This option will sort employees specified by the Employee Filter according to their group description for the selected group level. For example, a company with multiple locations might have a Group Level of 'Location' and Group Descriptions of 'Pittsburgh' , 'Phoenix' , and 'Jacksonville'. Selecting the 'Location' group level would sort employees according to their assigned location. |
| Only Show Employees Who Are Not Working in Their Default Department | No | This option will allow you to display only employees that are not currently logged into their default department. |
| Page Break by Department? | No | This option will allow you page break the report by Department, making it easier to give the report to department heads for review if needed. |
| Page Break by Employee? | No | This option will allow you to page break the report based on each employee, making it easier to give the report to the individual employees for review. |
| Page Break by Group? | No | This option will allow you to page break the report based on each Group Description and is intended for use with 'Group Level to Group By.' The report can then be distributed as necessary. |
| Page Break by Job? | No | This option will allow you to page break the report by Job, making it easier to give the reports to Job Supervisors for review. |
| Page Break by Supervisor? | No | This option will allow you to page break the report based on Employee Supervisors, making it easier to distribute to Supervisors for review. |
| Page Break by Task? | No | This option will allow you to page break the report by Task, making it easier to give the reports to Task Supervisors for review. |
| Print Inactive Employees? | No | This option will allow you to print information of the inactive employees along with the active ones. |
| Sort by Employee Number? | No | This option will group employees specified by the Employee Filter according to their Employee ID. |

# Payroll Reports

# Department Payroll Detail

Displays department totals by day and calculates corresponding dollar
totals.

Report
Example:

![](images_2/Department_Payroll_Detail.gif)

Notes/Usage:

This report is useful when wanting to know the gross pay for departments
on a day by day basis.

Options:

The Department Payroll Detail Report is
a user customizable report. Refer to the [Customizable
Report Section](/InfiniTime/help%20file/Overview/Reports/Reports.md#rpt16_User_Customizable_Reports) of this manual for more information.

# Department Payroll Summary

Displays department totals, in hours, for the date range specified by
Selection Criteria and calculates corresponding dollar totals.

Report
Example:

![](images_2/Department_Payroll_Summary.gif)

Notes/Usage:

* This report is useful for reviewing total hours distribution and
  gross pay for specific departments over a date range.

Options:

The Department Payroll Summary Report is
a user customizable report. Refer to the [Customizable
Report Section](/InfiniTime/help%20file/Overview/Reports/Reports.md#rpt16_User_Customizable_Reports) of this manual for more information.

# Labor Cost Payroll Summary

Calculates Labor % as Employee Gross Wages divided by Employee Sales
Targets. Total Hours and Gross Wages are displayed on the report for the
selected Date / Time Range. To compare actual sales amounts, which vary
by employee, the report must be executed for individual employees with
the Sales Amount Option set to the appropriate dollar amount.

Report
Example:

![](images_2/Labor_Cost_Payroll_Summary.gif)

Notes/Usage:

* Useful for analyzing performance for hourly employees in sales
  related roles.
* Sales Amounts are entered as a projected total for each employee
  in the report - individual employees can be analyzed with exact sales
  amounts by running the report for individual employees with the respective
  employee's Sales Amount set in the Options Tab.

Options:

| Option | Default Value | Description |
| Allow Graphics On the Report? | Yes | This option allows you to choose if you want to print the InfiniTime 7.0 logo on the report. |
| Group by Department? | No | This option will allow you to group the employees by department based on the selection you have made either Employee Default Department or Employee Worked in Department. |
| Page Break By Department? | No | This option allows you to page break the report at each department. |
| Print Inactive Employees? | No | This option will allow you to print information of the inactive employees along with the active ones. |
| Sales Amount? | BLANK | In this option you must enter an amount, this amount is the amount you are going to compare to the employees wages. |
| Start Time? | 12:00 AM | Enter the Start Time to begin totalling employee worked hours on the From Date as set in the Report Selection Criteria. Total Worked Hours will be calculated from the Start Time on the From Date to the Stop Time on the To Date. |
| Stop Time? | 12:00 AM | Enter the Stop Time to serve as the end point for totalling employee worked hours on the To Date as set in the Report Selection Criteria. Total Worked Hours will be calculated from the Start Time on the From Date to the Stop Time on the To Date. |

# Payroll Detail

Displays Total Hours and Total Wages by day for each employee with Timecards
during the Selected Date Range.

Report
Example:

![](images_2/Payroll_Detail_Report.gif)

Notes/Usage:

* Useful for reviewing employee gross wages on a day by day basis
  with totals for the Selected Date Range.

Options:

The Payroll Detail Report is a user customizable
report. Refer to the [Customizable
Report Section](/InfiniTime/help%20file/User_Customizable_Reports.md) of this manual for more information.

## Payroll Interface Layout

The Payroll Interface Layout Report is intended to supplement the Payroll
Export Documentation included in the InfiniTime
Help System by displaying the Payroll Interface Field Layout for Payroll
Exports  configured within InfiniTime
at run time.

Page 1:

![](images_2/Rpt016.png)

Page 2:

![](images_2/Rpt017.png)

Notes / Usage:

* The Payroll Interface Layout Report prints two pages for each entry
  on the Payroll Export Table.
* The first page of the Payroll Interface Layout Report shows configured
  values for Payroll Export Options and Settings.
* The second page of the Payroll Interface Layout Report shows the
  field by field layout of the payroll interface.
* When a payroll export is executed, Employee Hours and Earnings
  for the date range selected on the Payroll Export record will be exported
  in the format shown on the Payroll Interface Layout Report's field
  by field layout.
* The Payroll Interface Layout Report will be blank if there are
  no Payroll Exports configured on the Payroll Export Table as accessed
  from the Payroll Button on the Main Toolbar of the Manager Module.

Additional details on available options and the different types of layouts
supported by the Payroll Export system can be found in the [Payroll Export section of this
document.](/InfiniTime/help%20file/Overview/PayrollExport/Payroll_Export.md#pxh2_Introduction)

Options:

| Option | Default Value | Description |
| Allow Graphics On the Report? | Yes | This option allows you to choose if you want to print the InfiniTime 7.0 logo on the report. |

# Payroll Summary

Displays Total Hours and Total Wages for each employee with Timecards
during the Selected Date Range.

Report
Example:

![](images_2/Payroll_Summary.gif)

Notes/Usage:

* Useful for reviewing employee gross wages with totals for the Selected
  Date Range.

Options:

The Payroll Summary Report is a user customizable
report. Refer to the [Customizable
Report Section](/InfiniTime/help%20file/User_Customizable_Reports.md) of this manual for more information.

Schedule Reports

# Attendance Review

Displays a chart for the date range specified detailing missed days,
paid time off, other activity types, and the number of days with exceptions.

Report
Example:

![](images_2/Attendance_Review.gif)

Notes/Usage:

Useful for directing management focus to trends that may have a negative
impact on the company. IE: The employee often calls in sick on a Monday
or Friday or The employee is often tardy every other Tuesday.

Using the Attendance Review
Report

The Attendance Review
Report allows users to review employee attendance history for a given
period of time by displaying a character for each worked day, non-worked
day, and each day with Other Activity Hours such as Vacation, Sick, Personal,
or Jury Duty. Exceptions are also listed on the report to help managers
identify trends in employee behavior, such as regularly leaving work early
on a Friday or requesting every Third Wednesday of the Month off for various
reasons. Report options and Report Selection Criteria Settings can be
used to force the report to show only Other Activity Hours, Specific Other
Activity Types, and / or Specific Exceptions.

As shown in the image
above, the attendance review report displays a grid including all days
for the selected date range. For each day, a single character is printed
to indicate whether the day was a Work Day, a Non-Worked Day, or a day
with Other Activity. Additionally, total hours for Worked Days and days
with Other Activity are also displayed in the Month / Days Grid. If the
employee worked on a given date, the Worked Day Character will be displayed.
If the employee had other Activity Hours on a given date, the Other Activity
Attendance Review Character will be displayed according to the report
options.

TECHNICAL NOTE: The Month / Days Grid is only filled
for dates that fall within the date range. For this reason, to avoid confusion,
the Attendance Review Report should be executed for a date range that
includes all dates within a given month or multiple months. IE: 5/1/2013
to 6/30/2013 or 5/1/2013 to 5/31/2013.

In order for Other Activity
Hours to display on the Attendance Review Report, the Attendance Review
Character must be defined for the other activity type and the other activity
type must be included in the Selection Criteria on the report. The Attendance
Review Character can be configured on the Other Activity Update Form as
shown below.

1. Login
   to the Manager Module
2. Click
   on Lookups - Calculations Setup - Other Activity Types
3. Select
   the Other Activity Type you wish to configure for display on the Attendance
   Review Report and click Change
4. Enter
   the character(s) to be displayed on the Attendance Review Report for
   the respective Other Activity Type into the Attendance Review Report
   Character Field as shown.

![](images_2/Rpt026.png)

5. Click OK to
   Save the Changes and repeat for all Other Activity Types to be displayed
   on the Attendance Review Report.

Technical Note: The
Date Fields on the Attendance Review Report supports display of only one
Hours Type. With this in mind, the Worked Day Character will be displayed
on any day with working hours, even if there were also Other Activity
Hours on the day. If multiple Other Activity Types occur on a single day
with no working hours, the Day Field will display the Other Activity Type
Character for the Other Activity Type with the most Hours. If all Other
Activity Types on a single day have the same number of hours, the first
Other Activity Type that was entered in the system will be displayed on
the report.

Options:

| Option | Default Value | Description |
| Allow Graphics On the Report? | Yes | This option allows you to choose if you want to print the InfiniTime 7.0 logo on the report. |
| Department Grouping Type? | None | This option allows you to group the report by Department. In most cases, Customers choose to execute the Attendance Review Report with Department, Job, and Task Grouping at the default values of 'None'. |
| Department Selection Based On? | Employee Default Department | This option will allow you to select how the Department  filter is used to select employees. By default, departments tagged on the selection criteria will cause InfiniTime to display employees assigned to that department on the report. Alternatively, selecting 'Worked in Department' will show employees that worked in the selected department during the selected date range. |
| Department Selection Filters Activity? | No | If this option is set to Yes, employee Timecard Records displayed on the report will be filtered according to tagged departments as follows:      1.) Only employees with hours in the tagged department(s) will be displayed on the report.  2.) Only timecard records assigned to the tagged department(s) will be used to calculate totals for display on the report. All other timecard records for employees will ignored when this option is set to Yes. |
| Employee Signature Message | None | Permits the user to specify a disclaimer or message to be displayed under the employee signature line. The Employee Signature message will only be displayed on the Report if 'Print Employee Signature Line?' is set to Yes. |
| Group by Supervisor? | No | This option will group employees specified by the Employee Filter according to their assigned Supervisor. |
| Group level to group by: | None | This option will sort employees specified by the Employee Filter according to their group description for the selected group level. For example, a company with multiple locations might have a Group Level of 'Location' and Group Descriptions of 'Pittsburgh' , 'Phoenix' , and 'Jacksonville'. Selecting the 'Location' group level would sort employees according to their assigned location. |
| Job Grouping Type? | None | Determines how employees will be grouped by Jobs. When set to None the option is considered disabled and employees will not be grouped by jobs.    When set to Employee Default Job employees will be grouped according to their default job as assigned on their employee record. When set to Employee Worked On Job employees will be grouped according to the job they worked in.    In most cases, Customers choose to execute the Attendance Review Report with Department, Job, and Task Grouping at the default values of 'None'. |
| Job Selection Based On: | Employee Default Job | This option will allow you to select how the Job filter is used to select employees. By default, jobs tagged on the selection criteria will cause InfiniTime to display employees assigned to the job on the report. Alternatively, selecting 'Worked in Job'' will show employees that worked in the selected job during the chosen date range. |
| Job Selection Filters Activity? | No | If this option is set to Yes, employee Timecard Records displayed on the report will be filtered according to tagged departments as follows:      1.) Only employees with hours in the tagged Job(s) will be displayed on the report.  2.) Only timecard records assigned to the tagged Job(s) will be used to calculate totals for display on the report. All other timecard records for employees will ignored when this option is set to Yes. |
| Non-Worked Day Character | None | This option allows you to input the character to be displayed on the report for a non-worked day. By default, Non-Working Days are not marked. |
| Other Activity Only? | No | When this option is enabled, Working Hours are excluded from the By Category Section AND the Total Days section does not count days with working hours toward the Total Days Count. |
| Page Break by Department? | No | This option will allow you page break the report by Department, making it easier to give the report to department heads for review if needed. |
| Page Break by Employee? | No | This option will allow you to page break the report based on each employee, making it easier to give the report to the individual employees for review. |
| Page Break by Group? | No | This option will allow you to page break the report based on each Group Description and is intended for use with 'Group Level to Group By.' The report can then be distributed as necessary. |
| Page Break by Job? | No | This option will allow you to page break the report by Job, making it easier to give the reports to Job Supervisors for review. |
| Page Break by Supervisor? | No | This option will allow you to page break the report based on each supervisor, making it easier for individual supervisors to review hours for their specific employees. |
| Page Break by Task? | No | This option will allow you to page break the report by Task, making it easier to give the reports to Task Supervisors for review. |
| Print Employee Signature Line? | No | An employee signature line will be displayed at the bottom of the results for each employee if this option is enabled. Generally Page Break by Employee should be enabled when using this feature. |
| Print Inactive Employees? | No | This option will allow you to print information of the inactive employees along with the active ones. |
| Print Supervisor Signature Line? | No | A supervisor signature line will be displayed at the bottom of the results for each employee if this option is enabled. Generally Page Break by Employee should be enabled when using this feature. |
| Sort by Employee Number? | No | This option will group employees specified by the Employee Filter according to their Employee ID. |
| Supervisor Signature Message: | None | Permits the user to specify a disclaimer or message to be displayed under the supervisor signature line. The Supervisor Signature message will only be displayed on the Report if 'Print Supervisor Signature Line?' is set to Yes. |
| Task Grouping Type? | None | Determines how employees will be grouped by Tasks. When set to None the option is considered disabled and employees will not be grouped by tasks. When set to Employee Default Task employees will be grouped according to their default task as assigned on their employee record. When set to Scheduled Task employees will be grouped according to the task they were scheduled to work in.    In most cases, Customers choose to execute the Attendance Review Report with Department, Job, and Task Grouping at the default values of 'None'. |
| Task Selection Based On: | Employee Default Task | This option will allow you to select how the Task filter is used to select employees. By default, tasks tagged on the selection criteria will cause InfiniTime to display employees assigned to the tagged task(s) on the report. Alternatively, selecting 'Worked in Task'' will show employees that worked in the selected task during the chosen date range. |
| Task Selection Filters Activity? | No | If this option is set to Yes, employee Timecard Records displayed on the report will be filtered according to tagged tasks as follows:      1.) Only employees with hours in the tagged tasks will be displayed on the report.  2.) Only timecard records assigned to the tagged task(s) will be used to calculate totals for display on the report. All other timecard records for employees will ignored when this option is set to Yes. |
| Worked Day Character | W | This option allows you to input the character to be displayed on the report for a worked day, the default value is 'W' |

# Company Performance Analysis

Displays a Chart comparing scheduled hours against working hours and
absent hours for employees included in the Report Selection Criteria.
If the Selection Criteria is not altered, the report will calculate total
Scheduled Hours, Working Hours, and Absent Hours for the company as a
whole. Additionally, total Tardy, Long Break, and Early Departure minutes
are calculated and totaled on the report. In order for Tardy, Long Break,
and / or Early Departure minutes to be calculated the respective exceptions
must be configured.

Report Example:

![](images_2/Rpt032.png)

Notes/Usage:

* The Company Performance Analysis Report calculates total durations
  for the following hour types and exceptions:

+ Worked Hours (Regular, Paid Break, OT1, OT2, OT3, OT4)
+ Scheduled Hours (Scheduled Working Hours, Scheduled Paid
  Break Hours)
+ Absent Hours
+ Tardy Minutes
+ Long Break Minutes
+ Early Departure Minutes

* The Company Performance Analysis Report requires that employee
  schedules and respective exceptions such as Absent, Tardy, Long Break,
  and Early Departure be configured in order to total durations for
  each hours type.
* The Attendance Review Report provides similar information, but
  with more detail on an employee by employee basis, and is generally
  favored by customers.

Options:

| Option | Default Value | Description |
| Allow Graphics On the Report? | Yes | This option allows you to choose if you want to print the InfiniTime 7.0 logo on the report. |
| Print Inactive Employees? | No | This option will allow you to print information of the inactive employees along with the active employees. |

# Day Scheduled

Displays a chart, which assists with employee scheduling by showing
all days that have a schedule defined within the date range, specified
by Selection Criteria.

Report Example:

![](images_2/Rpt033.png)

Notes/Usage:

* The Day Scheduled Report is executed for a month and will display
  the first to last day of month regardless of the exact date range
  chosen. For example, if the report is executed for 6/1/13 to 6/8/13
  the report will generate for 6/1/13 to 6/30/13.

Options:

| Option | Default Value | Description |
| Allow Graphics On the Report? | Yes | This option allows you to choose if you want to print the InfiniTime 7.0 logo on the report. |
| Day Not Worked Character |  | Specifies a character to be displayed when a day is not worked. |
| Day Worked Character | W | Specifies a character to be displayed when a day is worked. |
| Department Selection Based On? | Employee Default Department | This option will allow you to select how the Department  filter is used to select employees. By default, departments tagged on the selection criteria will cause InfiniTime to display employees assigned to that department on the report. Alternatively, selecting 'Worked in Department' will show employees that worked in the selected department during the selected date range. |
| Department Selection Filters Activity? | No | If this option is set to Yes, employee Timecard Records displayed on the report will be filtered according to tagged departments as follows:       1.) Only employees with hours in the tagged department(s) will be displayed on the report.  2.) Only timecard records assigned to the tagged department(s) will be used to calculate totals for display on the report. All other timecard records for employees will ignored when this option is set to Yes. |
| Group by Department? | No | This option will group employees specified by the Employee Filter by Department. |
| Group by Supervisor? | No | This option will group employees specified by the Employee Filter according to their Default Supervisor. |
| Group level to group by: | None | This option will sort employees specified by the Employee Filter according to their group description for the selected group level. For example, a company with multiple locations might have a Group Level of 'Location' and Group Descriptions of 'Pittsburgh' , 'Phoenix' , and 'Jacksonville'. Selecting the 'Location' group level would sort employees according to their assigned location. |
| Job Grouping Type? | None | Determines how employees will be grouped by Jobs. When set to None the option is considered disabled and employees will not be grouped by jobs. When set to Employee Default employees will be grouped according to their default job as assigned on their employee record. When set to Scheduled employees will be grouped according to the job they were scheduled for. |
| Job Selection Based On: | Employee Default Job | This option will allow you to select how the Job filter is used to select employees. By default, jobs tagged on the selection criteria will cause InfiniTime to display employees assigned to the job on the report. Alternatively, selecting 'Worked in Job'' will show employees that worked in the selected job during the chosen date range. |
| Job Selection Filters Activity? | No | If this option is set to Yes, employee Timecard Records displayed on the report will be filtered according to tagged departments as follows:       1.) Only employees with hours in the tagged Job(s) will be displayed on the report.  2.) Only timecard records assigned to the tagged Job(s) will be used to calculate totals for display on the report. All other timecard records for employees will ignored when this option is set to Yes. |
| Only Print Department If Not Default Department? | Yes | If this option is set to No, the Department will be printed for every schedule with a Department assigned. Otherwise, Departments will only be printed on the report if an employee is scheduled outside of their default task. |
| Only Print Job If Not Default Job? | Yes | If this option is set to No, the Job will be printed for every schedule with a Job assigned. Otherwise, Jobs will only be printed on the report if an employee is scheduled outside of their default job. |
| Only Print Task If Not Default Task? | Yes | If this option is set to No, the Task will be printed for every schedule with a Task assigned. Otherwise, Tasks will only be printed on the report if an employee is scheduled outside of their default task. |
| Page Break by Department? | No | This option will allow you page break the report based on the Employee's Default Department, making it easier to give the report to department heads for review if needed. |
| Page Break by Employee? | No | This option will allow you to page break the report based on each employee, making it easier to give the report to the individual employees for review. |
| Page Break by Group? | No | This option will allow you to page break the report based on each Group Description and is intended for use with 'Group Level to Group By.' The report can then be distributed as necessary. |
| Page Break by Job? | No | This option will allow you to page break the report by Job, making it easier to give the reports to Job Supervisors for review. |
| Page Break by Supervisor? | No | This option will allow you to page break the report based on Employee Supervisors, making it easier to distribute to Supervisors for review. |
| Page Break by Task? | No | This option will allow you to page break the report by Task, making it easier to give the reports to Task Supervisors for review. |
| Print Inactive Employees? | No | This option will allow you to print information of the inactive employees along with the active ones. |
| Print Weekly Hour Totals? | No | When set to Yes a total record will be displayed after each scheduled week to show total scheduled hours. |
| Sort by Employee Number? | No | This option will group employees specified by the Employee Filter according to their Employee ID. |
| Task Grouping Type? | None | Determines how employees will be grouped by Tasks. When set to None the option is considered disabled and employees will not be grouped by tasks. When set to Employee Default employees will be grouped according to their default task as assigned on their employee record. When set to Scheduled employees will be grouped according to the task they were scheduled to work in. |
| Task Selection Based On: | Employee Default Task | This option will allow you to select how the Task filter is used to select employees. By default, tasks tagged on the selection criteria will cause InfiniTime to display employees assigned to the task on the report. Alternatively, selecting 'Worked in Task'' will show employees that worked in the selected task during the chosen date range. |
| Task Selection Filters Activity? | No | If this option is set to Yes, employee Timecard Records displayed on the report will be filtered according to tagged tasks as follows:       1.) Only employees with hours in the tagged tasks will be displayed on the report.  2.) Only timecard records assigned to the tagged task(s) will be used to calculate totals for display on the report. All other timecard records for employees will ignored when this option is set to Yes. |

# Day Schedule With Employee Groups

Displays a chart, which assists with employee scheduling by showing
all days that have a schedule defined within the date range, specified
by Selection Criteria. Breaks down by group.

Report Example:

![](images_2/Rpt034.png)

Notes/Usage:

* The Day Scheduled Report is executed for a month and will display
  the first to last day of month regardless of the exact date range
  chosen. For example, if the report is executed for 6/1/13 to 6/8/13
  the report will generate for 6/1/13 to 6/30/13.

Options:

| Option | Default Value | Description |
| Allow Graphics On the Report? | Yes | This option allows you to choose if you want to print the InfiniTime 7.0 logo on the report. |
| Day Not Worked Character |  | Specifies a character to be displayed when a day is not worked. |
| Day Worked Character | W | Specifies a character to be displayed when a day is worked. |
| Department Selection Based On? | Employee Default Department | This option will allow you to select how the Department  filter is used to select employees. By default, departments tagged on the selection criteria will cause InfiniTime to display employees assigned to that department on the report. Alternatively, selecting 'Worked in Department' will show employees that worked in the selected department during the selected date range. |
| Department Selection Filters Activity? | No | If this option is set to Yes, employee Timecard Records displayed on the report will be filtered according to tagged departments as follows:       1.) Only employees with hours in the tagged department(s) will be displayed on the report.  2.) Only timecard records assigned to the tagged department(s) will be used to calculate totals for display on the report. All other timecard records for employees will ignored when this option is set to Yes. |
| Group by Department? | No | This option will group employees specified by the Employee Filter by Department. |
| Job Grouping Type? | None | Determines how employees will be grouped by Jobs. When set to None the option is considered disabled and employees will not be grouped by jobs. When set to Employee Default employees will be grouped according to their default job as assigned on their employee record. When set to Scheduled employees will be grouped according to the job they were scheduled for. |
| Job Selection Based On: | Employee Default Job | This option will allow you to select how the Job filter is used to select employees. By default, jobs tagged on the selection criteria will cause InfiniTime to display employees assigned to the job on the report. Alternatively, selecting 'Worked in Job'' will show employees that worked in the selected job during the chosen date range. |
| Job Selection Filters Activity? | No | If this option is set to Yes, employee Timecard Records displayed on the report will be filtered according to tagged departments as follows:       1.) Only employees with hours in the tagged Job(s) will be displayed on the report.  2.) Only timecard records assigned to the tagged Job(s) will be used to calculate totals for display on the report. All other timecard records for employees will ignored when this option is set to Yes. |
| Number of Blank Lines After Group? | 0 | Permits the user to adjust the amount of blank space after the group header. Useful for writing notes onto the printed report. |
| Only Print Department If Not Default Department? | Yes | If this option is set to No, the Department will be printed for every schedule with a Department assigned. Otherwise, Departments will only be printed on the report if an employee is scheduled outside of their default task. |
| Only Print Job If Not Default Job? | Yes | If this option is set to No, the Job will be printed for every schedule with a Job assigned. Otherwise, Jobs will only be printed on the report if an employee is scheduled outside of their default job. |
| Only Print Task If Not Default Task? | Yes | If this option is set to No, the Task will be printed for every schedule with a Task assigned. Otherwise, Tasks will only be printed on the report if an employee is scheduled outside of their default task. |
| Page Break by Department? | No | This option will allow you page break the report based on the Employee's Default Department, making it easier to give the report to department heads for review if needed. |
| Page Break by Employee? | No | This option will allow you to page break the report based on each employee, making it easier to give the report to the individual employees for review. |
| Page Break by Job? | No | This option will allow you to page break the report by Job, making it easier to give the reports to Job Supervisors for review. |
| Page Break by Task? | No | This option will allow you to page break the report by Task, making it easier to give the reports to Task Supervisors for review. |
| Print Inactive Employees? | No | This option will allow you to print information of the inactive employees along with the active ones. |
| Print Weekly Hour Totals? | No | When set to Yes a total record will be displayed after each scheduled week to show total scheduled hours. |
| Task Grouping Type? | None | Determines how employees will be grouped by Tasks. When set to None the option is considered disabled and employees will not be grouped by tasks. When set to Employee Default employees will be grouped according to their default task as assigned on their employee record. When set to Scheduled employees will be grouped according to the task they were scheduled to work in. |
| Task Selection Based On: | Employee Default Task | This option will allow you to select how the Task filter is used to select employees. By default, tasks tagged on the selection criteria will cause InfiniTime to display employees assigned to the task on the report. Alternatively, selecting 'Worked in Task'' will show employees that worked in the selected task during the chosen date range. |
| Task Selection Filters Activity? | No | If this option is set to Yes, employee Timecard Records displayed on the report will be filtered according to tagged tasks as follows:       1.) Only employees with hours in the tagged tasks will be displayed on the report.  2.) Only timecard records assigned to the tagged task(s) will be used to calculate totals for display on the report. All other timecard records for employees will ignored when this option is set to Yes. |

# Department Performance Analysis

Displays a chart comparing scheduled hours with the actual hours worked
for all Departments within the company. A separate chart is generated
for each department. Also lists the total amount of tardy exceptions,
long break exceptions, and early departures during the period specified
by Selection Criteria.

Report Example:

![](images_2/Rpt035.png)

Notes/Usage:

* The Department Performance Analysis Report calculates total durations
  for the following hour types and exceptions:

+ Worked Hours (Regular, Paid Break, OT1, OT2, OT3, OT4)
+ Scheduled Hours (Scheduled Working Hours, Scheduled Paid
  Break Hours)
+ Absent Hours
+ Tardy Minutes
+ Long Break Minutes
+ Early Departure Minutes

* The Department Performance Analysis Report requires that employee
  schedules and respective exceptions such as Absent, Tardy, Long Break,
  and Early Departure be configured in order to total durations for
  each hours type.
* The Attendance Review Report provides similar information, but
  with more detail on an employee by employee basis, and is generally
  favored by customers.

Options:

| Option | Default Value | Description |
| Allow Graphics On the Report? | Yes | This option allows you to choose if you want to print the InfiniTime 7.0 logo on the report. |
| Print Inactive Employees? | No | This option will allow you to print information of the inactive employees along with the active employees. |

# Monthly Schedule

 Displays a monthly schedule for the specified employees according
to the date range specified. Schedules must be configured in order to
build this report.

Report
Example:

![](images_2/Rpt027.png)

Notes/Usage:

* The Monthly Schedule Report is best suited for employees with contiguous
  working periods at various Start and End times throughout the month.
* Ideal for posting in an accessible location to show when employees
  are expected to report to work for given dates.

Options:

| Option | Default Value | Description |
| Allow Graphics On the Report? | Yes | This option allows you to choose if you want to print the InfiniTime 7.0 logo on the report. |
| Department Selection Based On? | Employee Default Department | This option will allow you to select how the Department  filter is used to select employees. By default, departments tagged on the selection criteria will cause InfiniTime to display employees assigned to that department on the report. Alternatively, selecting 'Scheduled in Department' will show employees that are scheduled in the selected department during the selected date range. |
| Department Selection Filters Activity? | No | If this option is set to Yes, employee Schedule Records displayed on the report will be filtered according to tagged departments as follows:       1.) Only employees with Schedules in the tagged department(s) will be displayed on the report.  2.) Only Schedule records assigned to the tagged department(s) will be used to calculate totals for display on the report. All other timecard records for employees will ignored when this option is set to Yes. |
| Group by Department? | None | This option will group employees specified by the Employee Filter according by Department. |
| Group by Supervisor? | No | This option will group employees specified by the Employee Filter according to their assigned Supervisor. |
| Group level to group by: | None | This option will sort employees specified by the Employee Filter according to their group description for the selected group level. For example, a company with multiple locations might have a Group Level of 'Location' and Group Descriptions of 'Pittsburgh' , 'Phoenix' , and 'Jacksonville'. Selecting the 'Location' group level would sort employees according to their assigned location. |
| Job Grouping Type? | None | Determines how employees will be grouped by Jobs. When set to None the option is considered disabled and employees will not be grouped by jobs.    When set to Employee Default Job employees will be grouped according to their default job as assigned on their employee record. When set to Employee Worked On Job employees will be grouped according to the job they worked in.    In most cases, Customers choose to execute the Attendance Review Report with Department, Job, and Task Grouping at the default values of 'None'. |
| Job Selection Based On: | Employee Default Job | This option will allow you to select how the Job filter is used to select employees. By default, jobs tagged on the selection criteria will cause InfiniTime to display employees assigned to the job on the report. Alternatively, selecting 'Worked in Job'' will show employees that worked in the selected job during the chosen date range. |
| Job Selection Filters Activity? | No | If this option is set to Yes, employee Timecard Records displayed on the report will be filtered according to tagged departments as follows:       1.) Only employees with hours in the tagged Job(s) will be displayed on the report.  2.) Only timecard records assigned to the tagged Job(s) will be used to calculate totals for display on the report. All other timecard records for employees will ignored when this option is set to Yes. |
| Only Print Department If Not Default Department? | Yes | If this option is set to No, the Department will be printed for every schedule with a Department assigned. Otherwise, Departments will only be printed on the report if an employee is scheduled outside of their default task. |
| Only Print Job If Not Default Job? | Yes | If this option is set to No, the Job will be printed for every schedule with a Job assigned. Otherwise, Jobs will only be printed on the report if an employee is scheduled outside of their default job. |
| Only Print Task If Not Default Task? | Yes | If this option is set to No, the Task will be printed for every schedule with a Task assigned. Otherwise, Tasks will only be printed on the report if an employee is scheduled outside of their default task. |
| Page Break by Department? | No | This option will allow you page break the report by Department, making it easier to give the report to department heads for review if needed. |
| Page Break by Employee? | No | This option will allow you to page break the report based on each employee, making it easier to give the report to the individual employees for review. |
| Page Break by Group? | No | This option will allow you to page break the report based on each Group Description and is intended for use with 'Group Level to Group By.' The report can then be distributed as necessary. |
| Page Break by Job? | No | This option will allow you to page break the report by Job, making it easier to give the reports to Job Supervisors for review. |
| Page Break by Supervisor? | No | This option will allow you to page break the report based on each supervisor, making it easier for individual supervisors to review hours for their specific employees. |
| Page Break by Task? | No | This option will allow you to page break the report by Task, making it easier to give the reports to Task Supervisors for review. |
| Print Inactive Employees? | No | This option will allow you to print information of the inactive employees along with the active ones. |
| Print Weekly Hour Totals? | No | This option permits display of Total Scheduled Hours for each week during the selected date range. By default, Weekly Hour Totals are not displayed. |
| Sort by Employee Number? | No | This option will group employees specified by the Employee Filter according to their Employee ID. |
| Task Grouping Type? | None | Determines how employees will be grouped by Tasks. When set to None the option is considered disabled and employees will not be grouped by tasks. When set to Employee Default Task employees will be grouped according to their default task as assigned on their employee record. When set to Scheduled Task employees will be grouped according to the task they were scheduled to work in.    In most cases, Customers choose to execute the Attendance Review Report with Department, Job, and Task Grouping at the default values of 'None'. |
| Task Selection Based On: | Employee Default Task | This option will allow you to select how the Task filter is used to select employees. By default, tasks tagged on the selection criteria will cause InfiniTime to display employees assigned to the tagged task(s) on the report. Alternatively, selecting 'Worked in Task'' will show employees that worked in the selected task during the chosen date range. |
| Task Selection Filters Activity? | No | If this option is set to Yes, employee Timecard Records displayed on the report will be filtered according to tagged tasks as follows:       1.) Only employees with hours in the tagged tasks will be displayed on the report.  2.) Only timecard records assigned to the tagged task(s) will be used to calculate totals for display on the report. All other timecard records for employees will ignored when this option is set to Yes. |

# Monthly Schedule With Employee Groups

Displays a monthly schedule for the specified groups according to the
date range specified. Schedules must be configured in order to build this
report.

Report
Example:

![](images_2/Rpt028.png)

Notes/Usage:

* Intended for use with the Groups Tab of the Report Selection Criteria.
* Prints a full Monthly Schedule for all employees in each tagged
  group.
* If groups belonging to different group levels are tagged (IE:
  Company: XYZ Pool Management and Location: Phoenix, AZ) and an employee
  belongs to multiple tagged items, the employee will be displayed on
  the report once for each group they are assigned to that is included
  in the filter.

Options:

| Option | Default Value | Description |
| Allow Graphics On the Report? | Yes | This option allows you to choose if you want to print the InfiniTime 7.0 logo on the report. |
| Department Selection Based On? | Employee Default Department | This option will allow you to select how the Department  filter is used to select employees. By default, departments tagged on the selection criteria will cause InfiniTime to display employees assigned to that department on the report. Alternatively, selecting 'Scheduled in Department' will show employees that are scheduled in the selected department during the selected date range. |
| Department Selection Filters Activity? | No | If this option is set to Yes, employee Schedule Records displayed on the report will be filtered according to tagged departments as follows:        1.) Only employees with Schedules in the tagged department(s) will be displayed on the report.  2.) Only Schedule records assigned to the tagged department(s) will be used to calculate totals for display on the report. All other timecard records for employees will ignored when this option is set to Yes. |
| Group by Department? | None | This option will group employees specified by the Employee Filter according by Department. |
| Job Grouping Type? | None | Determines how employees will be grouped by Jobs. When set to None the option is considered disabled and employees will not be grouped by jobs.    When set to Employee Default Job employees will be grouped according to their default job as assigned on their employee record. When set to Employee Worked On Job employees will be grouped according to the job they worked in.    In most cases, Customers choose to execute the Attendance Review Report with Department, Job, and Task Grouping at the default values of 'None'. |
| Job Selection Based On: | Employee Default Job | This option will allow you to select how the Job filter is used to select employees. By default, jobs tagged on the selection criteria will cause InfiniTime to display employees assigned to the job on the report. Alternatively, selecting 'Worked in Job'' will show employees that worked in the selected job during the chosen date range. |
| Job Selection Filters Activity? | No | If this option is set to Yes, employee Timecard Records displayed on the report will be filtered according to tagged departments as follows:        1.) Only employees with hours in the tagged Job(s) will be displayed on the report.  2.) Only timecard records assigned to the tagged Job(s) will be used to calculate totals for display on the report. All other timecard records for employees will ignored when this option is set to Yes. |
| Only Print Department If Not Default Department? | Yes | If this option is set to No, the Department will be printed for every schedule with a Department assigned. Otherwise, Departments will only be printed on the report if an employee is scheduled outside of their default task. |
| Only Print Job If Not Default Job? | Yes | If this option is set to No, the Job will be printed for every schedule with a Job assigned. Otherwise, Jobs will only be printed on the report if an employee is scheduled outside of their default job. |
| Only Print Task If Not Default Task? | Yes | If this option is set to No, the Task will be printed for every schedule with a Task assigned. Otherwise, Tasks will only be printed on the report if an employee is scheduled outside of their default task. |
| Page Break by Department? | No | This option will allow you page break the report by Department, making it easier to give the report to department heads for review if needed. |
| Page Break by Employee? | No | This option will allow you to page break the report based on each employee, making it easier to give the report to the individual employees for review. |
| Page Break by Group? | No | This option will allow you to page break the report based on each Group Description and is intended for use with 'Group Level to Group By.' The report can then be distributed as necessary. |
| Page Break by Job? | No | This option will allow you to page break the report by Job, making it easier to give the reports to Job Supervisors for review. |
| Page Break by Task? | No | This option will allow you to page break the report by Task, making it easier to give the reports to Task Supervisors for review. |
| Print Inactive Employees? | No | This option will allow you to print information of the inactive employees along with the active ones. |
| Print Weekly Hour Totals? | No | This option permits display of Total Scheduled Hours for each week during the selected date range. By default, Weekly Hour Totals are not displayed. |
| Task Grouping Type? | None | Determines how employees will be grouped by Tasks. When set to None the option is considered disabled and employees will not be grouped by tasks. When set to Employee Default Task employees will be grouped according to their default task as assigned on their employee record. When set to Scheduled Task employees will be grouped according to the task they were scheduled to work in.    In most cases, Customers choose to execute the Attendance Review Report with Department, Job, and Task Grouping at the default values of 'None'. |
| Task Selection Based On: | Employee Default Task | This option will allow you to select how the Task filter is used to select employees. By default, tasks tagged on the selection criteria will cause InfiniTime to display employees assigned to the tagged task(s) on the report. Alternatively, selecting 'Worked in Task'' will show employees that worked in the selected task during the chosen date range. |
| Task Selection Filters Activity? | No | If this option is set to Yes, employee Timecard Records displayed on the report will be filtered according to tagged tasks as follows:        1.) Only employees with hours in the tagged tasks will be displayed on the report.  2.) Only timecard records assigned to the tagged task(s) will be used to calculate totals for display on the report. All other timecard records for employees will ignored when this option is set to Yes. |

# Performance Analysis

Displays a chart comparing scheduled hours with the actual hours worked
for all employees within the company. A separate chart is generated for
each employee. Also lists the total amount of tardy exceptions, long break
exceptions, and early departures during the period specified by Selection
Criteria.

Report
Example:

![](images_2/Rpt029.png)

Notes/Usage:

* Useful for evaluating employee performance.
* The Attendance Review Report provides similar information, but
  with more detail, and is generally favored by customers.

Options:

| Option | Default Value | Description |
| Allow Graphics On the Report? | Yes | This option allows you to choose if you want to print the InfiniTime 7.0 logo on the report. |
| Department Grouping Type? | None | This option allows you to group the report by Department. In most cases, Customers choose to execute the Attendance Review Report with Department, Job, and Task Grouping at the default values of 'None'. |
| Department Selection Based On? | Employee Default Department | This option will allow you to select how the Department  filter is used to select employees. By default, departments tagged on the selection criteria will cause InfiniTime to display employees assigned to that department on the report. Alternatively, selecting 'Worked in Department' will show employees that worked in the selected department during the selected date range. |
| Department Selection Filters Activity? | No | If this option is set to Yes, employee Timecard Records displayed on the report will be filtered according to tagged departments as follows:       1.) Only employees with hours in the tagged department(s) will be displayed on the report.  2.) Only timecard records assigned to the tagged department(s) will be used to calculate totals for display on the report. All other timecard records for employees will ignored when this option is set to Yes. |
| Group by Supervisor? | No | This option will group employees specified by the Employee Filter according to their assigned Supervisor. |
| Group level to group by: | None | This option will sort employees specified by the Employee Filter according to their group description for the selected group level. For example, a company with multiple locations might have a Group Level of 'Location' and Group Descriptions of 'Pittsburgh' , 'Phoenix' , and 'Jacksonville'. Selecting the 'Location' group level would sort employees according to their assigned location. |
| Job Grouping Type? | None | Determines how employees will be grouped by Jobs. When set to None the option is considered disabled and employees will not be grouped by jobs.    When set to Employee Default Job employees will be grouped according to their default job as assigned on their employee record. When set to Employee Worked On Job employees will be grouped according to the job they worked in.    In most cases, Customers choose to execute the Attendance Review Report with Department, Job, and Task Grouping at the default values of 'None'. |
| Job Selection Based On: | Employee Default Job | This option will allow you to select how the Job filter is used to select employees. By default, jobs tagged on the selection criteria will cause InfiniTime to display employees assigned to the job on the report. Alternatively, selecting 'Worked in Job'' will show employees that worked in the selected job during the chosen date range. |
| Job Selection Filters Activity? | No | If this option is set to Yes, employee Timecard Records displayed on the report will be filtered according to tagged departments as follows:       1.) Only employees with hours in the tagged Job(s) will be displayed on the report.  2.) Only timecard records assigned to the tagged Job(s) will be used to calculate totals for display on the report. All other timecard records for employees will ignored when this option is set to Yes. |
| Page Break by Department? | No | This option will allow you page break the report by Department, making it easier to give the report to department heads for review if needed. |
| Page Break by Employee? | No | This option will allow you to page break the report based on each employee, making it easier to give the report to the individual employees for review. |
| Page Break by Group? | No | This option will allow you to page break the report based on each Group Description and is intended for use with 'Group Level to Group By.' The report can then be distributed as necessary. |
| Page Break by Job? | No | This option will allow you to page break the report by Job, making it easier to give the reports to Job Supervisors for review. |
| Page Break by Supervisor? | No | This option will allow you to page break the report based on each supervisor, making it easier for individual supervisors to review hours for their specific employees. |
| Page Break by Task? | No | This option will allow you to page break the report by Task, making it easier to give the reports to Task Supervisors for review. |
| Print Inactive Employees? | No | This option will allow you to print information of the inactive employees along with the active ones. |
| Sort by Employee Number? | No | This option will group employees specified by the Employee Filter according to their Employee ID. |
| Task Grouping Type? | None | Determines how employees will be grouped by Tasks. When set to None the option is considered disabled and employees will not be grouped by tasks. When set to Employee Default Task employees will be grouped according to their default task as assigned on their employee record. When set to Scheduled Task employees will be grouped according to the task they were scheduled to work in.    In most cases, Customers choose to execute the Attendance Review Report with Department, Job, and Task Grouping at the default values of 'None'. |
| Task Selection Based On: | Employee Default Task | This option will allow you to select how the Task filter is used to select employees. By default, tasks tagged on the selection criteria will cause InfiniTime to display employees assigned to the tagged task(s) on the report. Alternatively, selecting 'Worked in Task'' will show employees that worked in the selected task during the chosen date range. |
| Task Selection Filters Activity? | No | If this option is set to Yes, employee Timecard Records displayed on the report will be filtered according to tagged tasks as follows:       1.) Only employees with hours in the tagged tasks will be displayed on the report.  2.) Only timecard records assigned to the tagged task(s) will be used to calculate totals for display on the report. All other timecard records for employees will ignored when this option is set to Yes. |

# Postable Schedule

Displays a chart showing detailed schedules for the employees and date
range specified by Selection Criteria. This report can be sorted by employee
or by department in order to provide a schedule that can be posted in
a conspicuous area for viewing by all employees within a specific department
or distributed to each employee as appropriate.

Report
Example:

![](images_2/Rpt030.png)

Notes/Usage:

* Intended to be printed for individual work weeks.
* If the report is executed for a date range that includes more
  than one week, the report will print once for all employees included
  in the Selection Criteria for the First Week, and then once again
  for the second week.
* Ideal for organizations with dynamic scheduling needs where
  employee schedules vary on a regular basis.
* Ideal for posting in an accessible area to show employees exactly
  what Department / Job / Task they are assigned to for a given working
  period.

Options:

| Option | Default Value | Description |
| Allow Graphics On the Report? | Yes | This option allows you to choose if you want to print the InfiniTime 7.0 logo on the report. |
| Department Selection Based On? | Employee Default Department | This option will allow you to select how the Department  filter is used to select employees. By default, departments tagged on the selection criteria will cause InfiniTime to display employees assigned to that department on the report. Alternatively, selecting 'Scheduled in Department' will show employees that are scheduled in the selected department during the selected date range. |
| Department Selection Filters Activity? | No | If this option is set to Yes, employee Schedule Records displayed on the report will be filtered according to tagged departments as follows:        1.) Only employees with Schedules in the tagged department(s) will be displayed on the report.  2.) Only Schedule records assigned to the tagged department(s) will be used to calculate totals for display on the report. All other timecard records for employees will ignored when this option is set to Yes. |
| Group by Department? | None | This option will group employees specified by the Employee Filter according by Department. |
| Group by Supervisor? | No | This option will group employees specified by the Employee Filter according to their assigned Supervisor. |
| Group level to group by: | None | This option will sort employees specified by the Employee Filter according to their group description for the selected group level. For example, a company with multiple locations might have a Group Level of 'Location' and Group Descriptions of 'Pittsburgh' , 'Phoenix' , and 'Jacksonville'. Selecting the 'Location' group level would sort employees according to their assigned location. |
| Job Grouping Type? | None | Determines how employees will be grouped by Jobs. When set to None the option is considered disabled and employees will not be grouped by jobs.    When set to Employee Default Job employees will be grouped according to their default job as assigned on their employee record. When set to Employee Worked On Job employees will be grouped according to the job they worked in.    In most cases, Customers choose to execute the Attendance Review Report with Department, Job, and Task Grouping at the default values of 'None'. |
| Job Selection Based On: | Employee Default Job | This option will allow you to select how the Job filter is used to select employees. By default, jobs tagged on the selection criteria will cause InfiniTime to display employees assigned to the job on the report. Alternatively, selecting 'Worked in Job'' will show employees that worked in the selected job during the chosen date range. |
| Job Selection Filters Activity? | No | If this option is set to Yes, employee Timecard Records displayed on the report will be filtered according to tagged departments as follows:        1.) Only employees with hours in the tagged Job(s) will be displayed on the report.  2.) Only timecard records assigned to the tagged Job(s) will be used to calculate totals for display on the report. All other timecard records for employees will ignored when this option is set to Yes. |
| Only Print Department If Not Default Department? | Yes | If this option is set to No, the Department will be printed for every schedule with a Department assigned. Otherwise, Departments will only be printed on the report if an employee is scheduled outside of their default task. |
| Only Print Job If Not Default Job? | Yes | If this option is set to No, the Job will be printed for every schedule with a Job assigned. Otherwise, Jobs will only be printed on the report if an employee is scheduled outside of their default job. |
| Only Print Task If Not Default Task? | Yes | If this option is set to No, the Task will be printed for every schedule with a Task assigned. Otherwise, Tasks will only be printed on the report if an employee is scheduled outside of their default task. |
| Page Break by Department? | No | This option will allow you page break the report by Department, making it easier to give the report to department heads for review if needed. |
| Page Break by Employee? | No | This option will allow you to page break the report based on each employee, making it easier to give the report to the individual employees for review. |
| Page Break by Group? | No | This option will allow you to page break the report based on each Group Description and is intended for use with 'Group Level to Group By.' The report can then be distributed as necessary. |
| Page Break by Job? | No | This option will allow you to page break the report by Job, making it easier to give the reports to Job Supervisors for review. |
| Page Break by Supervisor? | No | This option will allow you to page break the report based on each supervisor, making it easier for individual supervisors to review hours for their specific employees. |
| Page Break by Task? | No | This option will allow you to page break the report by Task, making it easier to give the reports to Task Supervisors for review. |
| Print Detailed Schedule? | No | When Set to Yes, all Scheduled Working Periods for each date on the report will be displayed. By Default, when set to No, only the first In Time and last Out Time will be displayed. |
| Print Inactive Employees? | No | This option will allow you to print information of the inactive employees along with the active ones. |
| Sort by Employee Number? | No | This option will group employees specified by the Employee Filter according to their Employee ID. |
| Task Grouping Type? | None | Determines how employees will be grouped by Tasks. When set to None the option is considered disabled and employees will not be grouped by tasks. When set to Employee Default Task employees will be grouped according to their default task as assigned on their employee record. When set to Scheduled Task employees will be grouped according to the task they were scheduled to work in.    In most cases, Customers choose to execute the Attendance Review Report with Department, Job, and Task Grouping at the default values of 'None'. |
| Task Selection Based On: | Employee Default Task | This option will allow you to select how the Task filter is used to select employees. By default, tasks tagged on the selection criteria will cause InfiniTime to display employees assigned to the tagged task(s) on the report. Alternatively, selecting 'Worked in Task'' will show employees that worked in the selected task during the chosen date range. |
| Task Selection Filters Activity? | No | If this option is set to Yes, employee Timecard Records displayed on the report will be filtered according to tagged tasks as follows:        1.) Only employees with hours in the tagged tasks will be displayed on the report.  2.) Only timecard records assigned to the tagged task(s) will be used to calculate totals for display on the report. All other timecard records for employees will ignored when this option is set to Yes. |

# Schedule Gantt Chart

Generates a report visually similar to the Schedule GANNT Chart for
the employees and date range specified by Selection Criteria.

Tip: Useful for displaying employee schedules in a clear and concise
fashion.

Report
Example:

![](images_2/Rpt031.png)

Options:

| Option | Default Value | Description |
| Allow Graphics On the Report? | Yes | This option allows you to choose if you want to print the InfiniTime 7.0 logo on the report. |
| Department Selection Based On? | Employee Default Department | This option will allow you to select how the Department  filter is used to select employees. By default, departments tagged on the selection criteria will cause InfiniTime to display employees assigned to that department on the report. Alternatively, selecting 'Scheduled in Department' will show employees that are scheduled in the selected department during the selected date range. |
| Department Selection Filters Activity? | No | If this option is set to Yes, employee Schedule Records displayed on the report will be filtered according to tagged departments as follows:        1.) Only employees with Schedules in the tagged department(s) will be displayed on the report.  2.) Only Schedule records assigned to the tagged department(s) will be used to calculate totals for display on the report. All other timecard records for employees will ignored when this option is set to Yes. |
| Group by Department? | None | This option will group employees specified by the Employee Filter according by Department. |
| Job Grouping Type? | None | Determines how employees will be grouped by Jobs. When set to None the option is considered disabled and employees will not be grouped by jobs.    When set to Employee Default Job employees will be grouped according to their default job as assigned on their employee record. When set to Employee Worked On Job employees will be grouped according to the job they worked in.    In most cases, Customers choose to execute the Attendance Review Report with Department, Job, and Task Grouping at the default values of 'None'. |
| Job Selection Based On: | Employee Default Job | This option will allow you to select how the Job filter is used to select employees. By default, jobs tagged on the selection criteria will cause InfiniTime to display employees assigned to the job on the report. Alternatively, selecting 'Worked in Job'' will show employees that worked in the selected job during the chosen date range. |
| Job Selection Filters Activity? | No | If this option is set to Yes, employee Timecard Records displayed on the report will be filtered according to tagged departments as follows:        1.) Only employees with hours in the tagged Job(s) will be displayed on the report.  2.) Only timecard records assigned to the tagged Job(s) will be used to calculate totals for display on the report. All other timecard records for employees will ignored when this option is set to Yes. |
| Page Break by Department? | No | This option will allow you page break the report by Department, making it easier to give the report to department heads for review if needed. |
| Page Break by Employee? | No | This option will allow you to page break the report based on each employee, making it easier to give the report to the individual employees for review. |
| Page Break by Job? | No | This option will allow you to page break the report by Job, making it easier to give the reports to Job Supervisors for review. |
| Page Break by Task? | No | This option will allow you to page break the report by Task, making it easier to give the reports to Task Supervisors for review. |
| Print Inactive Employees? | No | This option will allow you to print information of the inactive employees along with the active ones. |
| Task Grouping Type? | None | Determines how employees will be grouped by Tasks. When set to None the option is considered disabled and employees will not be grouped by tasks. When set to Employee Default Task employees will be grouped according to their default task as assigned on their employee record. When set to Scheduled Task employees will be grouped according to the task they were scheduled to work in.    In most cases, Customers choose to execute the Attendance Review Report with Department, Job, and Task Grouping at the default values of 'None'. |
| Task Selection Based On: | Employee Default Task | This option will allow you to select how the Task filter is used to select employees. By default, tasks tagged on the selection criteria will cause InfiniTime to display employees assigned to the tagged task(s) on the report. Alternatively, selecting 'Worked in Task'' will show employees that worked in the selected task during the chosen date range. |
| Task Selection Filters Activity? | No | If this option is set to Yes, employee Timecard Records displayed on the report will be filtered according to tagged tasks as follows:        1.) Only employees with hours in the tagged tasks will be displayed on the report.  2.) Only timecard records assigned to the tagged task(s) will be used to calculate totals for display on the report. All other timecard records for employees will ignored when this option is set to Yes. |

# System Reports

# System Monitor Configuration

Lists each port in use and all readers associated with the port. Provides
detailed configuration information for each reader.

Report
Example:

![](images_2/System_Monitor_1.gif)

![](images_2/System_Monitor_2.gif)

![](images_2/System_Monitor_3.gif)

Notes/Usage:

* Useful for reviewing configuration for Hardware Terminals connected
  to the InfiniTime Software.

Options:

| Option | Default Value | Description |
| Allow Graphics On the Report? | Yes | This option allows you to choose if you want to print the InfiniTime 7.0 logo on the report. |

# Who Is Enrolled

Displays a list of all employees currently enrolled with hand or fingerprint
templates for biometric readers.

Report
Example:

![](images_2/Rpt036.png)

Notes/Usage:

* Useful for determining if specific employees have a Fingerprint,
  Hand Geometry Template, or Both stored in the database.
* Through use of the 'Print Employees That Are' option, the Who is
  Enrolled Report can be used to determine specific employees who do
  not have a Fingerprint, Hand Template, or either present in the database.
* Employees can then be enrolled as appropriate.

Options:

| Option | Default Value | Description |
| Allow Graphics On the Report? | Yes | This option allows you to choose if you want to print the InfiniTime 7.0 logo on the report. |
| Department Selection Based On? | Employee Default Department | This option will allow you to select how the Department  filter is used to select employees. By default, departments tagged on the selection criteria will cause InfiniTime to display employees assigned to that department on the report. Alternatively, selecting 'Scheduled in Department' will show employees that are scheduled in the selected department during the selected date range. |
| Department Selection Filters Activity? | No | If this option is set to Yes, employee Schedule Records displayed on the report will be filtered according to tagged departments as follows:        1.) Only employees with Schedules in the tagged department(s) will be displayed on the report.  2.) Only Schedule records assigned to the tagged department(s) will be used to calculate totals for display on the report. All other timecard records for employees will ignored when this option is set to Yes. |
| Group by Department? | None | This option will group employees specified by the Employee Filter according by Department. |
| Job Grouping Type? | None | Determines how employees will be grouped by Jobs. When set to None the option is considered disabled and employees will not be grouped by jobs.    When set to Employee Default Job employees will be grouped according to their default job as assigned on their employee record. When set to Employee Worked On Job employees will be grouped according to the job they worked in.    In most cases, Customers choose to execute the Attendance Review Report with Department, Job, and Task Grouping at the default values of 'None'. |
| Job Selection Based On: | Employee Default Job | This option will allow you to select how the Job filter is used to select employees. By default, jobs tagged on the selection criteria will cause InfiniTime to display employees assigned to the job on the report. Alternatively, selecting 'Worked in Job'' will show employees that worked in the selected job during the chosen date range. |
| Job Selection Filters Activity? | No | If this option is set to Yes, employee Timecard Records displayed on the report will be filtered according to tagged departments as follows:        1.) Only employees with hours in the tagged Job(s) will be displayed on the report.  2.) Only timecard records assigned to the tagged Job(s) will be used to calculate totals for display on the report. All other timecard records for employees will ignored when this option is set to Yes. |
| Page Break by Department? | No | This option will allow you page break the report by Department, making it easier to give the report to department heads for review if needed. |
| Page Break by Employee? | No | This option will allow you to page break the report based on each employee, making it easier to give the report to the individual employees for review. |
| Page Break by Job? | No | This option will allow you to page break the report by Job, making it easier to give the reports to Job Supervisors for review. |
| Page Break by Task? | No | This option will allow you to page break the report by Task, making it easier to give the reports to Task Supervisors for review. |
| Print Inactive Employees? | No | This option will allow you to print information of the inactive employees along with the active ones. |
| Task Grouping Type? | None | Determines how employees will be grouped by Tasks. When set to None the option is considered disabled and employees will not be grouped by tasks. When set to Employee Default Task employees will be grouped according to their default task as assigned on their employee record. When set to Scheduled Task employees will be grouped according to the task they were scheduled to work in.    In most cases, Customers choose to execute the Attendance Review Report with Department, Job, and Task Grouping at the default values of 'None'. |
| Task Selection Based On: | Employee Default Task | This option will allow you to select how the Task filter is used to select employees. By default, tasks tagged on the selection criteria will cause InfiniTime to display employees assigned to the tagged task(s) on the report. Alternatively, selecting 'Worked in Task'' will show employees that worked in the selected task during the chosen date range. |
| Task Selection Filters Activity? | No | If this option is set to Yes, employee Timecard Records displayed on the report will be filtered according to tagged tasks as follows:        1.) Only employees with hours in the tagged tasks will be displayed on the report.  2.) Only timecard records assigned to the tagged task(s) will be used to calculate totals for display on the report. All other timecard records for employees will ignored when this option is set to Yes. |

# Timecard Reports

# Activity Daily Summary

Displays a summary of timecard activity information for each day within
the date range specified by Selection Criteria. The activity type, department,
and total hours for the period are displayed for each employee.

Report
Example:

![](images_2/Activity_Daily_Summary.gif)

Notes/Usage:

* Useful for reviewing employee hours, including Shift Differential
  Hours, on a day by day basis.

Options:

| Option | Default Value | Description |
| Allow Graphics On the Report? | Yes | This option allows you to choose if you want to print the InfiniTime 7.0 logo on the report. |
| Department Grouping Type? | None | This option allows you to group the report by the employees Activity Department, meaning that the hours will distribute to all the departments the employee worked, or group by Employee Default Department,which will put all the time worked in their default department even if they worked on other departments, or the last option is None. |
| Department Selection Based On? | Employee Default Department | This option will allow you to select how the Department  filter is used to select employees. By default, departments tagged on the selection criteria will cause InfiniTime to display employees assigned to that department on the report. Alternatively, selecting 'Worked in Department' will show employees that worked in the selected department during the selected date range. |
| Department Selection Filters Activity? | No | If this option is set to Yes, employee Schedule Records displayed on the report will be filtered according to tagged departments as follows:        1.) Only employees with Schedules in the tagged department(s) will be displayed on the report.  2.) Only Schedule records assigned to the tagged department(s) will be used to calculate totals for display on the report. All other timecard records for employees will ignored when this option is set to Yes. |
| Job Grouping Type? | None | Determines how employees will be grouped by Jobs. When set to None the   option is considered disabled and employees will not be grouped by jobs.   When set to Employee Default Job employees will be grouped according to   their default job as assigned on their employee record. When set to Scheduled Job employees will be grouped according to the job they were scheduled for. |
| Job Selection Based On: | Employee Default Job | This option will allow you to select how the Job filter is used to select employees. By default, jobs tagged on the selection criteria will cause InfiniTime to display employees assigned to the job on the report. Alternatively, selecting 'Worked in Job'' will show employees that worked in the selected job during the chosen date range. |
| Job Selection Filters Activity? | No | If this option is set to Yes, employee Timecard Records displayed on the report will be filtered according to tagged departments as follows:        1.) Only employees with hours in the tagged Job(s) will be displayed on the report.  2.) Only timecard records assigned to the tagged Job(s) will be used to calculate totals for display on the report. All other timecard records for employees will ignored when this option is set to Yes. |
| Page Break by Department? | No | This option will allow you page break the report based on the Employee's Default Department, making it easier to give the report to department heads for review if needed. |
| Page Break by Employee? | No | This option will allow you to page break the report based on each employee, making it easier to give the report to the individual employees for review. |
| Page Break by Job? | No | This option will allow you to page break the report based on the Employee's Default Job, making it easier to give the reports to Job Supervisors for review. |
| Page Break by Task? | No | This option will allow you to page break the report based on the Employee's Default Job, making it easier to give the reports to Task Supervisors for review. |
| Print Company Grand Totals? | No | This option will allow you to display the company grand total at the end of the report. |
| Print Inactive Employees? | No | This option will allow you to print information of the inactive employees along with the active ones. |
| Task Grouping Type? | None | Determines how employees will be grouped by Tasks. When set to None   the option is considered disabled and employees will not be grouped by   tasks. When set to Employee Default Task employees will be grouped according   to their default task as assigned on their employee record. When set to   Scheduled Task employees will be grouped according to the task they were   scheduled to work in. |
| Task Selection Based On: | Employee Default Task | This option will allow you to select how the Job filter is used to select employees. By default, tasks tagged on the selection criteria will cause InfiniTime to display employees assigned to the task on the report. Alternatively, selecting 'Worked in Task'' will show employees that worked in the selected task during the chosen date range. |
| Task Selection Filters Activity? | No | If this option is set to Yes, employee Timecard Records displayed on the report will be filtered according to tagged tasks as follows:        1.) Only employees with hours in the tagged tasks will be displayed on the report.  2.) Only timecard records assigned to the tagged task(s) will be used to calculate totals for display on the report. All other timecard records for employees will ignored when this option is set to Yes. |

# Activity Summary

Displays a summary of timecard activity information for the date range
specified by Selection Criteria. Separate totals are provided for each
activity type.

Report
Example:

![](images_2/Activity_Summary.gif)

Notes/Usage:

* Useful for viewing employee hours by hours type, including shift
  differentials, across a date range.

Options:

| Option | Default Value | Description |
| Allow Graphics On the Report? | Yes | This option allows you to choose if you want to print the InfiniTime 7.0  logo on the report. |
| Department Grouping Type? | None | When this option is set, Department Headers will be printed on the  Report.    If 'Employee Default' is selected, employee hours will be listed under their assigned default department even if they worked in multiple departments.    If 'Activity' is selected, employee hours will be distributed across each respective department the employee worked in.    If 'None' is selected, this option is considered disabled and employee timecard records will not be grouped by Department. |
| Department Selection Based On? | Employee Default Department | This option will allow you to select how the Department  filter is used to select employees. By default, departments tagged on the selection criteria will cause InfiniTime to display employees assigned to that department on the report. Alternatively, selecting 'Worked in Department' will show only employees that worked in the selected department during the selected date range. |
| Department Selection Filters Activity? | No | If this option is set to Yes, employee Timecard Records displayed on the report will be filtered according to tagged departments as follows:        1.) Only employees with Timecards in the tagged department(s) will be displayed on the report.  2.) Only Timecard records assigned to the tagged department(s) will be used to calculate totals for display on the report. All other timecard records for employees will be ignored when this option is set to Yes. |
| Job Grouping Type? | None | When this option is set, Job Headers will be printed on the Report.    If 'Employee Default' is selected, employee hours will be listed under their assigned default Job even if they worked in multiple Jobs.    If 'Activity' is selected, employee hours will be distributed across each respective job the employee worked in.    If 'None' is selected, this option is considered disabled and employee timecard records will not be grouped by Job. |
| Job Selection Based On: | Employee Default Job | This option will allow you to select how the Job filter is used to select employees. By default, jobs tagged on the selection criteria will cause InfiniTime to display employees assigned to the job on the report. Alternatively, selecting 'Worked in Job'' will show employees that worked in the selected job during the chosen date range. |
| Job Selection Filters Activity? | No | If this option is set to Yes, employee Timecard Records displayed on the report will be filtered according to tagged departments as follows:        1.) Only employees with hours in the tagged Job(s) will be displayed on the report.  2.) Only timecard records assigned to the tagged Job(s) will be used to calculate totals for display on the report. All other timecard records for employees will ignored when this option is set to Yes. |
| Page Break by Department? | No | This option will allow you page break the report by Department, making it easier to give the report to department heads for review if needed. |
| Page Break by Employee? | No | This option will allow you to page break the report based on each employee, making it easier to give the report to the individual employees for review. |
| Page Break by Job? | No | This option will allow you to page break the report by Job, making it easier to give the reports to Job Supervisors for review. |
| Page Break by Task? | No | This option will allow you to page break the report by Task, making it easier to give the reports to Task Supervisors for review. |
| Print Company Grand Totals? | No | This option will allow you to display the company grand total at the end of the report. |
| Print Inactive Employees? | No | This option will allow you to print information for both active and inactive employees. |
| Task Grouping Type? | None | When this option is set, Task Headers will be printed on the Report.    If 'Employee Default' is selected, employee hours will be listed under their assigned default Task even if they worked in multiple Tasks.    If 'Activity' is selected, employee hours will be distributed across each respective task the employee worked in.    If 'None' is selected, this option is considered disabled and employee timecard records will not be grouped by Task. |
| Task Selection Based On: | Employee Default Task | This option will allow you to select how the Job filter is used to select employees. By default, tasks tagged on the selection criteria will cause InfiniTime to display employees assigned to the task on the report. Alternatively, selecting 'Worked in Task'' will show employees that worked in the selected task during the chosen date range. |
| Task Selection Filters Activity? | No | If this option is set to Yes, employee Timecard Records displayed on the report will be filtered according to tagged tasks as follows:        1.) Only employees with hours in the tagged tasks will be displayed on the report.  2.) Only timecard records assigned to the tagged task(s) will be used to calculate totals for display on the report. All other timecard records for employees will ignored when this option is set to Yes. |

# Timecard Summary with Schedule Variance

The Timecard Summary with Schedule Variance
Report permits InfiniTime
Supervisors and Administrators to compare Employee Worked Hours with Employee
Scheduled Hours for the respective Department / Job / Task combination.
In this way, Supervisors can compare scheduled labor hours and with actual
labor hours worked by employees in a detailed view that includes exact
employee punches.

Report Example:

![](images_2/Rpt038.png)

Notes/Usage:

* The Timecard Summary with Schedule Variance Report is executed
  on a day by day basis. For each day, the report shows all employees
  who worked in a given Department / Job / Task Combination in accordance
  with the Report Selection Criteria and Department / Job / Task Grouping
  Options.
* Daily Totals for each employee and Department / Job / Task Combination
  are displayed.
* It is recommended that the report be executed with specific Departments,
  specific Jobs, or specific Tasks tagged.
* When used for analyzing Department Schedules and Hours, the Department
  Grouping Type should be set to Activity and the Job / Task Grouping
  Types should be set to None.
* Similarly, when used for analyzing Job Schedules and Hours, Job
  Grouping Type should be set to Activity and the Department / Task
  Grouping Types should be set to None.
* Similarly, when used for analyzing Task Schedules and Hours, Task
  Grouping Type should be set to Activity and the Department / Job Grouping
  Types should be set to None.

Options:

| Option | Default Value | Description |
| Allow Graphics On the Report? | Yes | This option allows you to choose if you want to print the InfiniTime 7.0  logo on the report. |
| Department Grouping Type? | None | When this option is set, Department Headers will be printed on the  Report.    If 'Employee Default' is selected, employee hours will be listed under their assigned default department even if they worked in multiple departments.    If 'Activity' is selected, employee hours will be distributed across each respective department the employee worked in.    If 'None' is selected, this option is considered disabled and employee timecard records will not be grouped by Department. |
| Department Selection Based On? | Employee Default Department | This option will allow you to select how the Department  filter is used to select employees. By default, departments tagged on the selection criteria will cause InfiniTime to display employees assigned to that department on the report. Alternatively, selecting 'Worked in Department' will show only employees that worked in the selected department during the selected date range. |
| Department Selection Filters Activity? | No | If this option is set to Yes, employee Timecard Records displayed on the report will be filtered according to tagged departments as follows:        1.) Only employees with Timecards in the tagged department(s) will be displayed on the report.  2.) Only Timecard records assigned to the tagged department(s) will be used to calculate totals for display on the report. All other timecard records for employees will be ignored when this option is set to Yes. |
| Group by Supervisor? | No | This option will group employees specified by the Employee Filter according to their assigned Supervisor. |
| Group Level to Group By? | None | This option will sort employees specified by the Employee Filter according to their group description for the selected group level. For example, a company with multiple locations might have a Group Level of 'Location' and Group Descriptions of 'Pittsburgh' , 'Phoenix' , and 'Jacksonville'. Selecting the 'Location' group level would sort employees according to their assigned location. |
| Job Grouping Type? | None | When this option is set, Job Headers will be printed on the Report.    If 'Employee Default' is selected, employee hours will be listed under their assigned default Job even if they worked in multiple Jobs.    If 'Activity' is selected, employee hours will be distributed across each respective job the employee worked in.    If 'None' is selected, this option is considered disabled and employee timecard records will not be grouped by Job. |
| Job Selection Based On: | Employee Default Job | This option will allow you to select how the Job filter is used to select employees. By default, jobs tagged on the selection criteria will cause InfiniTime to display employees assigned to the job on the report. Alternatively, selecting 'Worked in Job'' will show employees that worked in the selected job during the chosen date range. |
| Job Selection Filters Activity? | No | If this option is set to Yes, employee Timecard Records displayed on the report will be filtered according to tagged departments as follows:        1.) Only employees with hours in the tagged Job(s) will be displayed on the report.  2.) Only timecard records assigned to the tagged Job(s) will be used to calculate totals for display on the report. All other timecard records for employees will ignored when this option is set to Yes. |
| Overtime Selection | N/A | Permits filtering of results according to the presence of Approved or Unapproved Overtime Hours for an employee during the selected date range. |
| Page Break by Department? | No | This option will allow you page break the report by Department, making it easier to give the report to department heads for review if needed. |
| Page Break by Employee? | No | This option will allow you to page break the report based on each employee, making it easier to give the report to the individual employees for review. |
| Page Break by Group? | No | This option will allow you to page break the report based on each Group Description and is intended for use with 'Group Level to Group By.' The report can then be distributed as necessary. |
| Page Break by Job? | No | This option will allow you to page break the report by Job, making it easier to give the reports to Job Supervisors for review. |
| Page Break by Supervisor? | No | This option will allow you to page break the report based on each supervisor, making it easier for individual supervisors to review hours for their specific employees. |
| Page Break by Task? | No | This option will allow you to page break the report by Task, making it easier to give the reports to Task Supervisors for review. |
| Print Inactive Employees? | No | This option will allow you to print information for both active and inactive employees. |
| Print Time in Hours and Minutes? | No | InfiniTime reports activity in hundredths of an hour by default. Setting this option to Yes displays activity totals in hours and minutes. |
| Show Company Grand Total? | No | This option will allow you to display the company grand total at the end of the report. |
| Sort by Employee Number? | No | This option will group employees specified by the Employee Filter according to their Employee ID. |
| Task Grouping Type? | None | When this option is set, Task Headers will be printed on the Report.    If 'Employee Default' is selected, employee hours will be listed under their assigned default Task even if they worked in multiple Tasks.    If 'Activity' is selected, employee hours will be distributed across each respective task the employee worked in.    If 'None' is selected, this option is considered disabled and employee timecard records will not be grouped by Task. |
| Task Selection Based On: | Employee Default Task | This option will allow you to select how the Job filter is used to select employees. By default, tasks tagged on the selection criteria will cause InfiniTime to display employees assigned to the task on the report. Alternatively, selecting 'Worked in Task'' will show employees that worked in the selected task during the chosen date range. |
| Task Selection Filters Activity? | No | If this option is set to Yes, employee Timecard Records displayed on the report will be filtered according to tagged tasks as follows:        1.) Only employees with hours in the tagged tasks will be displayed on the report.  2.) Only timecard records assigned to the tagged task(s) will be used to calculate totals for display on the report. All other timecard records for employees will ignored when this option is set to Yes. |

# Department Activity Daily Summary

The Department Activity Daily Summary Report
displays a list of Hours Types worked for each department included in
the Selection Criteria along with the total number of hours for each hours
type on a day by day basis.

Report Example:

![](images_2/Rpt039.png)

Notes/Usage:

* Useful for reviewing Total Hours Worked for specific departments
  on a Day by Day basis.

Options:

| Option | Default Value | Description |
| Allow Graphics On the Report? | Yes | This option allows you to choose if you want to print the InfiniTime 7.0  logo on the report. |
| Department Grouping Type? | None | When this option is set, Department Headers will be printed on the  Report.    If 'Employee Default' is selected, employee hours will be listed under their assigned default department even if they worked in multiple departments.    If 'Activity' is selected, employee hours will be distributed across each respective department the employee worked in.    If 'None' is selected, this option is considered disabled and employee timecard records will not be grouped by Department. |
| Department Selection Based On? | Employee Default Department | This option will allow you to select how the Department  filter is used to select employees. By default, departments tagged on the selection criteria will cause InfiniTime to display employees assigned to that department on the report. Alternatively, selecting 'Worked in Department' will show only employees that worked in the selected department during the selected date range. |
| Department Selection Filters Activity? | No | If this option is set to Yes, employee Timecard Records displayed on the report will be filtered according to tagged departments as follows:         1.) Only employees with Timecards in the tagged department(s) will be displayed on the report.  2.) Only Timecard records assigned to the tagged department(s) will be used to calculate totals for display on the report. All other timecard records for employees will be ignored when this option is set to Yes. |
| Job Grouping Type? | None | When this option is set, Job Headers will be printed on the Report.    If 'Employee Default' is selected, employee hours will be listed under their assigned default Job even if they worked in multiple Jobs.    If 'Activity' is selected, employee hours will be distributed across each respective job the employee worked in.    If 'None' is selected, this option is considered disabled and employee timecard records will not be grouped by Job. |
| Job Selection Based On: | Employee Default Job | This option will allow you to select how the Job filter is used to select employees. By default, jobs tagged on the selection criteria will cause InfiniTime to display employees assigned to the job on the report. Alternatively, selecting 'Worked in Job'' will show employees that worked in the selected job during the chosen date range. |
| Job Selection Filters Activity? | No | If this option is set to Yes, employee Timecard Records displayed on the report will be filtered according to tagged departments as follows:         1.) Only employees with hours in the tagged Job(s) will be displayed on the report.  2.) Only timecard records assigned to the tagged Job(s) will be used to calculate totals for display on the report. All other timecard records for employees will ignored when this option is set to Yes. |
| Page Break by Department? | No | This option will allow you page break the report by Department, making it easier to give the report to department heads for review if needed. |
| Page Break by Employee? | No | This option will allow you to page break the report based on each employee, making it easier to give the report to the individual employees for review. |
| Page Break by Job? | No | This option will allow you to page break the report by Job, making it easier to give the reports to Job Supervisors for review. |
| Page Break by Task? | No | This option will allow you to page break the report by Task, making it easier to give the reports to Task Supervisors for review. |
| Print Company Grand Totals? | No | This option will allow you to display the company grand total at the end of the report. |
| Print Inactive Employees? | No | This option will allow you to print information for both active and inactive employees. |
| Task Grouping Type? | None | When this option is set, Task Headers will be printed on the Report.    If 'Employee Default' is selected, employee hours will be listed under their assigned default Task even if they worked in multiple Tasks.    If 'Activity' is selected, employee hours will be distributed across each respective task the employee worked in.    If 'None' is selected, this option is considered disabled and employee timecard records will not be grouped by Task. |
| Task Selection Based On: | Employee Default Task | This option will allow you to select how the Job filter is used to select employees. By default, tasks tagged on the selection criteria will cause InfiniTime to display employees assigned to the task on the report. Alternatively, selecting 'Worked in Task'' will show employees that worked in the selected task during the chosen date range. |
| Task Selection Filters Activity? | No | If this option is set to Yes, employee Timecard Records displayed on the report will be filtered according to tagged tasks as follows:         1.) Only employees with hours in the tagged tasks will be displayed on the report.  2.) Only timecard records assigned to the tagged task(s) will be used to calculate totals for display on the report. All other timecard records for employees will ignored when this option is set to Yes. |

# Department Activity Summary

The Department Activity Daily Summary Report
displays a list of Hours Types worked for each department included in
the Selection Criteria along with the total number of hours for each hours
type on a day by day basis.

Report Example:

![](images_2/Rpt040.png)

Notes/Usage:

* Useful for reviewing Total Hours Worked by hours type for specific
  departments over a date range.

Options:

| Option | Default Value | Description |
| Allow Graphics On the Report? | Yes | This option allows you to choose if you want to print the InfiniTime 7.0  logo on the report. |
| Department Grouping Type? | None | When this option is set, Department Headers will be printed on the  Report.    If 'Employee Default' is selected, employee hours will be listed under their assigned default department even if they worked in multiple departments.    If 'Activity' is selected, employee hours will be distributed across each respective department the employee worked in.    If 'None' is selected, this option is considered disabled and employee timecard records will not be grouped by Department. |
| Department Selection Based On? | Employee Default Department | This option will allow you to select how the Department  filter is used to select employees. By default, departments tagged on the selection criteria will cause InfiniTime to display employees assigned to that department on the report. Alternatively, selecting 'Worked in Department' will show only employees that worked in the selected department during the selected date range. |
| Department Selection Filters Activity? | No | If this option is set to Yes, employee Timecard Records displayed on the report will be filtered according to tagged departments as follows:         1.) Only employees with Timecards in the tagged department(s) will be displayed on the report.  2.) Only Timecard records assigned to the tagged department(s) will be used to calculate totals for display on the report. All other timecard records for employees will be ignored when this option is set to Yes. |
| Job Grouping Type? | None | When this option is set, Job Headers will be printed on the Report.    If 'Employee Default' is selected, employee hours will be listed under their assigned default Job even if they worked in multiple Jobs.    If 'Activity' is selected, employee hours will be distributed across each respective job the employee worked in.    If 'None' is selected, this option is considered disabled and employee timecard records will not be grouped by Job. |
| Job Selection Based On: | Employee Default Job | This option will allow you to select how the Job filter is used to select employees. By default, jobs tagged on the selection criteria will cause InfiniTime to display employees assigned to the job on the report. Alternatively, selecting 'Worked in Job'' will show employees that worked in the selected job during the chosen date range. |
| Job Selection Filters Activity? | No | If this option is set to Yes, employee Timecard Records displayed on the report will be filtered according to tagged departments as follows:         1.) Only employees with hours in the tagged Job(s) will be displayed on the report.  2.) Only timecard records assigned to the tagged Job(s) will be used to calculate totals for display on the report. All other timecard records for employees will ignored when this option is set to Yes. |
| Page Break by Department? | No | This option will allow you page break the report by Department, making it easier to give the report to department heads for review if needed. |
| Page Break by Employee? | No | This option will allow you to page break the report based on each employee, making it easier to give the report to the individual employees for review. |
| Page Break by Job? | No | This option will allow you to page break the report by Job, making it easier to give the reports to Job Supervisors for review. |
| Page Break by Task? | No | This option will allow you to page break the report by Task, making it easier to give the reports to Task Supervisors for review. |
| Print Company Grand Totals? | No | This option will allow you to display the company grand total at the end of the report. |
| Print Inactive Employees? | No | This option will allow you to print information for both active and inactive employees. |
| Task Grouping Type? | None | When this option is set, Task Headers will be printed on the Report.    If 'Employee Default' is selected, employee hours will be listed under their assigned default Task even if they worked in multiple Tasks.    If 'Activity' is selected, employee hours will be distributed across each respective task the employee worked in.    If 'None' is selected, this option is considered disabled and employee timecard records will not be grouped by Task. |
| Task Selection Based On: | Employee Default Task | This option will allow you to select how the Job filter is used to select employees. By default, tasks tagged on the selection criteria will cause InfiniTime to display employees assigned to the task on the report. Alternatively, selecting 'Worked in Task'' will show employees that worked in the selected task during the chosen date range. |
| Task Selection Filters Activity? | No | If this option is set to Yes, employee Timecard Records displayed on the report will be filtered according to tagged tasks as follows:         1.) Only employees with hours in the tagged tasks will be displayed on the report.  2.) Only timecard records assigned to the tagged task(s) will be used to calculate totals for display on the report. All other timecard records for employees will ignored when this option is set to Yes. |

# Department Daily Summary

Displays a summary of timecard activity information for each department
within the date range specified by Selection Criteria. The activity type,
department, and total hours for the period are displayed for each employee.

Report
Example:

![](images_2/Department_Daily_Summary.gif)

Notes / Usage:

* Useful for viewing how employee
  hours are distributed across multiple departments on a day by day
  basis.

Options:

The Department Daily Summary Report is
a user customizable report. Refer to the [Customizable
Report Section](/InfiniTime/help%20file/User_Customizable_Reports.md) of this manual for more information.

# Department Summary

Displays hourly totals for each department according to selection criteria.
Timecard Activity totals are separated by activity type.

Report Example:

![](images_2/Department_Summary.gif)

Notes/Usage:

* Useful for viewing how employee hours are distributed across
  multiple departments across a date range.

Options:

The Department Summary Report is a user
customizable report. Refer to the [Customizable
Report Section](/InfiniTime/help%20file/User_Customizable_Reports.md) of this manual for more information.

# Mini Timecard

Displays an overview of employee activity within the specified date
range.

Report
Example:

![](images_2/Mini_Timecard.gif)

Notes/Usage:

* Useful for performing a quick review of Employee in and out times
  and hourly totals for a given work week.
* The Mini Timecard report displays only the first In Punch and Last
  Out Punch for each respective date.

Options:

| Option | Default Value | Description |
| Allow Graphics On the Report? | Yes | This option allows you to choose if you want to print the InfiniTime 7.0 logo on the report. |
| Department Grouping Type? | None | This option allows you to group the report by the employees Activity Department, meaning that the hours will distribute to all the departments the employee worked, or group by Employee Default Department,which will put all the time worked in their default department even if they worked on other departments, or the last option is None. |
| Department Selection Based On? | Employee Default Department | This option will allow you to select how the Department  filter is used to select employees. By default, departments tagged on the selection criteria will cause InfiniTime to display employees assigned to that department on the report. Alternatively, selecting 'Worked in Department' will show employees that worked in the selected department during the selected date range. |
| Department Selection Filters Activity? | No | If this option is set to Yes, employee Timecard Records displayed on the report will be filtered according to tagged departments as follows:          1.) Only employees with Timecards in the tagged department(s) will be displayed on the report.  2.) Only Timecard records assigned to the tagged department(s) will be used to calculate totals for display on the report. All other timecard records for employees will be ignored when this option is set to Yes. |
| Group By Supervisor? | No | This option will group employees specified by the Employee Filter according to their Default Supervisor. |
| Group Level to group by: | No | This option will sort employees specified by the Employee Filter according to their group description for the selected group level. For example, a company with multiple locations might have a Group Level of 'Location' and Group Descriptions of 'Pittsburgh' , 'Phoenix' , and 'Jacksonville'. Selecting the 'Location' group level would sort employees according to their assigned location. |
| Job Grouping Type? | None | Determines how employees will be grouped by Jobs. When set to None the option is considered disabled and employees will not be grouped by jobs.  When set to Employee Default Job employees will be grouped according to their default job as assigned on their employee record. When set to Scheduled Job employees will be grouped according to the job they were scheduled for. |
| Job Selection Based On: | Employee Default Job | This option will allow you to select how the Job filter is used to select employees. By default, jobs tagged on the selection criteria will cause InfiniTime to display employees assigned to the job on the report. Alternatively, selecting 'Worked in Job'' will show employees that worked in the selected job during the chosen date range. |
| Job Selection Filters Activity? | No | If this option is set to Yes, employee Timecard Records displayed on the report will be filtered according to tagged departments as follows:          1.) Only employees with hours in the tagged Job(s) will be displayed on the report.  2.) Only timecard records assigned to the tagged Job(s) will be used to calculate totals for display on the report. All other timecard records for employees will ignored when this option is set to Yes. |
| Page Break by Department? | No | This option will allow you page break the report by Department, making it easier to give the report to department heads for review if needed. |
| Page Break by Employee? | No | This option will allow you to page break the report based on each employee, making it easier to give the report to the individual employees for review. |
| Page Break by Group? | No | This option will allow you to page break the report based on each Group Description and is intended for use with 'Group Level to Group By.' The  report can then be distributed as necessary. |
| Page Break by Job? | No | This option will allow you to page break the report by Job, making it easier to give the reports to Job Supervisors for review. |
| Page Break by Supervisor? | No | This option will allow you to page break the report based on Employee Supervisors, making it easier to distribute to Supervisors for review. |
| Page Break by Task? | No | This option will allow you to page break the report by Task, making it easier to give the reports to Task Supervisors for review. |
| Print Employee Signature Line? | No | When set to yes a signature line is displayed at the bottom of the report for employees to sign. This option is generally used in combination with the 'Page Break by Employee' option. |
| Print Inactive Employees? | No | This option will allow you to print information for both Active and Inactive Employees. |
| Print Supervisor Signature Line? | No | When set to yes a signature line is displayed at the bottom of the report for supervisors to sign. This option is generally used in combination with the 'Page Break by Employee' or 'Page break by Supervisor' options. |
| Sort by Employee Number | No | This option will group employees specified by the Employee Filter according to their Employee ID. |
| Task Grouping Type? | None | Determines how employees will be grouped by Tasks. When set to None   the option is considered disabled and employees will not be grouped by   tasks. When set to Employee Default Task employees will be grouped according to their default task as assigned on their employee record. When set to Scheduled Task employees will be grouped according to the task they were scheduled to work in. |
| Task Selection Based On: | Employee Default Task | This option will allow you to select how the Task filter is used to select employees. By default, tasks tagged on the selection criteria will cause InfiniTime to display employees assigned to the task on the report. Alternatively, selecting 'Worked in Task'' will show employees that worked in the selected task during the chosen date range. |
| Task Selection Filters Activity? | No | If this option is set to Yes, employee Timecard Records displayed on the report will be filtered according to tagged tasks as follows:          1.) Only employees with hours in the tagged tasks will be displayed on the report.  2.) Only timecard records assigned to the tagged task(s) will be used to calculate totals for display on the report. All other timecard records for employees will ignored when this option is set to Yes. |

# Mini Timecard With Details

Displays an overview of employee activity within the specified date
range.

Report Example:

![](images_2/Mini_Timecard_Detail.gif)

Notes/Usage:

* Useful for performing a quick review of Employee in and out times
  and hourly totals for a given work week.
* The Mini Timecard with Details report displays all punch pairs
  for each respective date included in the date range.

Options:

| Option | Default Value | Description |
| Allow Graphics On the Report? | Yes | This option allows you to choose if you want to print the InfiniTime 7.0 logo on the report. |
| Department Grouping Type? | None | This option allows you to group the report by the employees Activity Department, meaning that the hours will distribute to all the departments the employee worked, or group by Employee Default Department,which will put all the time worked in their default department even if they worked on other departments, or the last option is None. |
| Department Selection Based On? | Employee Default Department | This option will allow you to select how the Department  filter is used to select employees. By default, departments tagged on the selection criteria will cause InfiniTime to display employees assigned to that department on the report. Alternatively, selecting 'Worked in Department' will show employees that worked in the selected department during the selected date range. |
| Department Selection Filters Activity? | No | If this option is set to Yes, employee Timecard Records displayed on the report will be filtered according to tagged departments as follows:          1.) Only employees with Timecards in the tagged department(s) will be displayed on the report.  2.) Only Timecard records assigned to the tagged department(s) will be used to calculate totals for display on the report. All other timecard records for employees will be ignored when this option is set to Yes. |
| Group By Supervisor? | No | This option will group employees specified by the Employee Filter according to their Default Supervisor. |
| Group Level to group by: | No | This option will sort employees specified by the Employee Filter according to their group description for the selected group level. For example, a company with multiple locations might have a Group Level of 'Location' and Group Descriptions of 'Pittsburgh' , 'Phoenix' , and 'Jacksonville'. Selecting the 'Location' group level would sort employees according to their assigned location. |
| Job Grouping Type? | None | Determines how employees will be grouped by Jobs. When set to None the option is considered disabled and employees will not be grouped by jobs.  When set to Employee Default Job employees will be grouped according to their default job as assigned on their employee record. When set to Scheduled Job employees will be grouped according to the job they were scheduled for. |
| Job Selection Based On: | Employee Default Job | This option will allow you to select how the Job filter is used to select employees. By default, jobs tagged on the selection criteria will cause InfiniTime to display employees assigned to the job on the report. Alternatively, selecting 'Worked in Job'' will show employees that worked in the selected job during the chosen date range. |
| Job Selection Filters Activity? | No | If this option is set to Yes, employee Timecard Records displayed on the report will be filtered according to tagged departments as follows:          1.) Only employees with hours in the tagged Job(s) will be displayed on the report.  2.) Only timecard records assigned to the tagged Job(s) will be used to calculate totals for display on the report. All other timecard records for employees will ignored when this option is set to Yes. |
| Page Break by Department? | No | This option will allow you page break the report by Department, making it easier to give the report to department heads for review if needed. |
| Page Break by Employee? | No | This option will allow you to page break the report based on each employee, making it easier to give the report to the individual employees for review. |
| Page Break by Group? | No | This option will allow you to page break the report based on each Group Description and is intended for use with 'Group Level to Group By.' The  report can then be distributed as necessary. |
| Page Break by Job? | No | This option will allow you to page break the report by Job, making it easier to give the reports to Job Supervisors for review. |
| Page Break by Supervisor? | No | This option will allow you to page break the report based on Employee Supervisors, making it easier to distribute to Supervisors for review. |
| Page Break by Task? | No | This option will allow you to page break the report by Task, making it easier to give the reports to Task Supervisors for review. |
| Print Employee Signature Line? | No | When set to yes a signature line is displayed at the bottom of the report for employees to sign. This option is generally used in combination with the 'Page Break by Employee' option. |
| Print Inactive Employees? | No | This option will allow you to print information for both Active and Inactive Employees. |
| Print Supervisor Signature Line? | No | When set to yes a signature line is displayed at the bottom of the report for supervisors to sign. This option is generally used in combination with the 'Page Break by Employee' or 'Page break by Supervisor' options. |
| Sort by Employee Number | No | This option will group employees specified by the Employee Filter according to their Employee ID. |
| Task Grouping Type? | None | Determines how employees will be grouped by Tasks. When set to None   the option is considered disabled and employees will not be grouped by   tasks. When set to Employee Default Task employees will be grouped according to their default task as assigned on their employee record. When set to Scheduled Task employees will be grouped according to the task they were scheduled to work in. |
| Task Selection Based On: | Employee Default Task | This option will allow you to select how the Task filter is used to select employees. By default, tasks tagged on the selection criteria will cause InfiniTime to display employees assigned to the task on the report. Alternatively, selecting 'Worked in Task'' will show employees that worked in the selected task during the chosen date range. |
| Task Selection Filters Activity? | No | If this option is set to Yes, employee Timecard Records displayed on the report will be filtered according to tagged tasks as follows:          1.) Only employees with hours in the tagged tasks will be displayed on the report.  2.) Only timecard records assigned to the tagged task(s) will be used to calculate totals for display on the report. All other timecard records for employees will ignored when this option is set to Yes. |

# Shift Daily Summary

Displays a summary of employee activity separated by department and
shifts. Details regarding employee in and out times on individual dates
are not available on this report.

Report
Example:

![](images_2/Shift_Daily_Summary.gif)

Notes/Usage:

* Ideal for reviewing how employee hours are distributed across multiple
  shifts on a day by day basis. Especially useful for organizations
  who pay shift differentials.

Options:

The Shift Daily Summary Report is a user
customizable report. Refer to the [Customizable
Report Section](/InfiniTime/help%20file/User_Customizable_Reports.md) of this manual for more information.

# Shift Summary

Displays a summary of employee activity separated by department and
shifts for the date range specified by the Selection Criteria.

Report Example:

![](images_2/Shift_Summary.gif)

Notes/Usage:

* Ideal for reviewing how employee hours are distributed across multiple
  shifts across a date range. Especially useful for organizations who
  pay shift differentials.

Options:

The Shift Summary Report is a user customizable report. Refer to the
[Customizable Report Section](/InfiniTime/help%20file/User_Customizable_Reports.md)
of this manual for more information.

# Timecard Daily Summary

Displays an activity summary with daily totals for the employees and
date range specified by Selection Criteria.

Report Example:

![](images_2/Rpt041.png)

Notes/Usage:

* Useful for viewing how employee hours are distributed across various
  hours types on a day by day basis for a given date range.

Options:

The Timecard Daily Summary Report is a user customizable report. Refer
to the [Customizable Report
Section](/InfiniTime/help%20file/User_Customizable_Reports.md) of this manual for more information.

# Timecard Detail

Displays employee activity for each day within the date range specified.
Includes in and out times in addition to employee totals and exceptions.

Report Example:

![](images_2/Rpt043.png)

Notes/Usage:

* The Timecard Detail Report is one of the most commonly used reports
  for reviewing employee timecards, especially prior to running payroll.
* The Timecard Detail Report displays all timecard punches and other
  activity records present for employees during the date range set on
  the Report Selection Criteria.
* The Timecard Detail Report includes the Timecard Review History
  option which displays a list of all supervisors and their Position,
  as set on their Employee Profile, who have reviewed all of the employee's
  timecards during the respective date range. An example of the Timecard
  Review History table is shown bel  
    
    
  ![](images_2/TimecardReviewHistory.jpg)

Options:

| Option | Default Value | Description |
| Allow Graphics On the Report? | Yes | This option allows you to choose if you want to print the InfiniTime 7.0 logo on the report. |
| Department Grouping Type? | None | This option allows you to group the report by the employees Activity Department, meaning that the hours will distribute to all the departments the employee worked, or group by Employee Default Department,which will put all the time worked in their default department even if they worked on other departments, or the last option is None. |
| Department Selection Based On? | Employee Default Department | This option will allow you to select how the Department  filter is used to select employees. By default, departments tagged on the selection criteria will cause InfiniTime to display employees assigned to that department on the report. Alternatively, selecting 'Worked in Department' will show employees that worked in the selected department during the selected date range. |
| Department Selection Filters Activity? | No | If this option is set to Yes, employee Timecard Records displayed on the report will be filtered according to tagged departments as follows:          1.) Only employees with Timecards in the tagged department(s) will be displayed on the report.  2.) Only Timecard records assigned to the tagged department(s) will be used to calculate totals for display on the report. All other timecard records for employees will be ignored when this option is set to Yes. |
| Employee Signature Message? | None | Permits the user to specify a disclaimer or message to be displayed under the employee signature line. The Employee Signature message will only be displayed on the Report if 'Print Employee Signature Line?' is set to Yes. |
| Group By Supervisor? | No | This option will group employees specified by the Employee Filter according to their Default Supervisor. |
| Group Level to group by: | No | This option will sort employees specified by the Employee Filter according to their group description for the selected group level. For example, a company with multiple locations might have a Group Level of 'Location' and Group Descriptions of 'Pittsburgh' , 'Phoenix' , and 'Jacksonville'. Selecting the 'Location' group level would sort employees according to their assigned location. |
| Hide Audit Trail Asterisk? | No | If this option is set to Yes, the Audit Trail Asterisk will not be shown on the Timecard Detail Report. By default, when this option is set to No, any timecard punches with an audit trail record will be marked with an asterisk (\*).    Audit Trail records are automatically created by the InfiniTime software when timecard records are altered by supervisors and / or payroll personnel. |
| Hide Exceptions? | No | This option, when set to Yes, will prevent the Timecard Detail report from displaying exceptions such as Absent and Missed punch. By default, Exceptions are displayed on the Timecard Detail Report. |
| Job Grouping Type? | None | Determines how employees will be grouped by Jobs. When set to None the option is considered disabled and employees will not be grouped by jobs.  When set to Employee Default Job employees will be grouped according to their default job as assigned on their employee record. When set to Scheduled Job employees will be grouped according to the job they were scheduled for. |
| Job Selection Based On: | Employee Default Job | This option will allow you to select how the Job filter is used to select employees. By default, jobs tagged on the selection criteria will cause InfiniTime to display employees assigned to the job on the report. Alternatively, selecting 'Worked in Job'' will show employees that worked in the selected job during the chosen date range. |
| Job Selection Filters Activity? | No | If this option is set to Yes, employee Timecard Records displayed on the report will be filtered according to tagged departments as follows:          1.) Only employees with hours in the tagged Job(s) will be displayed on the report.  2.) Only timecard records assigned to the tagged Job(s) will be used to calculate totals for display on the report. All other timecard records for employees will ignored when this option is set to Yes. |
| Page Break by Department? | No | This option will allow you page break the report by Department, making it easier to give the report to department heads for review if needed. |
| Page Break by Employee? | No | This option will allow you to page break the report based on each employee, making it easier to give the report to the individual employees for review. |
| Page Break by Group? | No | This option will allow you to page break the report based on each Group Description and is intended for use with 'Group Level to Group By.' The  report can then be distributed as necessary. |
| Page Break by Job? | No | This option will allow you to page break the report by Job, making it easier to give the reports to Job Supervisors for review. |
| Page Break by Supervisor? | No | This option will allow you to page break the report based on Employee Supervisors, making it easier to distribute to Supervisors for review. |
| Page Break by Task? | No | This option will allow you to page break the report by Task, making it easier to give the reports to Task Supervisors for review. |
| Print Employee Signature Line? | No | When set to yes a signature line is displayed at the bottom of the report for employees to sign. This option is generally used in combination with the 'Page Break by Employee' option. |
| Print Inactive Employees? | No | This option will allow you to print information for both Active and Inactive Employees. |
| Print Supervisor Signature Line? | No | When set to yes a signature line is displayed at the bottom of the report for supervisors to sign. This option is generally used in combination with the 'Page Break by Employee' or 'Page break by Supervisor' options. |
| Print Time in Hours and Minutes? | No | InfiniTime reports activity in hundredths of an hour by default. Setting this option to Yes displays activity totals in hours and minutes. |
| Print Timecard Review History? | No | When enabled, Timecard Review history displays a list of supervisors, including Supervisor Name, Supervisor Position, and Last Review Time, for each employee who have reviewed all of the employees Timecard Records for the selected date range. A supervisor's name will not be listed if all records during the date range are not reviewed by the supervisor. Only the Timecard Review History header will be displayed if there are no supervisors who have reviewed all of an employee's Timecard Records for the selected date range. |
| Print Weekly Totals? | No | Enabling this option adds a subtotal row for each week to the Timecard Detail report. |
| Punch Description Displays? | Nothing | The Timecard Detail Report includes a small space to the right of the In and Out Times which permits display of additional details. By default, the Punch Description is blank. The user may select from the following options to display additional details in the Punch Description:    Clock Description - Prints the Clock Name for the hardware reader from which the punch was polled on the Timecard Detail Report.  Grace Periods - Prints Early and Tardy indicators, along with the number of early and / or tardy minutes, on the Timecard Detail Report.  Telephone Number - Prints the Telephone Number from which the employee called in to punch on the Timecard Detail report. Only supported for InfiniTime customers with Telephone Punch. |
| Show Company Grand Total? |  | When set to Yes a total record will be added to the bottom of the report to show total company hours  for selected columns. |
| Sort by Employee Number | No | This option will group employees specified by the Employee Filter according to their Employee ID. |
| Supervisor Signature Message: | None | Permits the user to specify a disclaimer or message to be displayed under the supervisor signature line. The Supervisor Signature message will only be displayed on the Report if 'Print Supervisor Signature Line?' is set to Yes. |
| Task Grouping Type? | None | Determines how employees will be grouped by Tasks. When set to None   the option is considered disabled and employees will not be grouped by   tasks. When set to Employee Default Task employees will be grouped according to their default task as assigned on their employee record. When set to Scheduled Task employees will be grouped according to the task they were scheduled to work in. |
| Task Selection Based On: | Employee Default Task | This option will allow you to select how the Task filter is used to select employees. By default, tasks tagged on the selection criteria will cause InfiniTime to display employees assigned to the task on the report. Alternatively, selecting 'Worked in Task'' will show employees that worked in the selected task during the chosen date range. |
| Task Selection Filters Activity? | No | If this option is set to Yes, employee Timecard Records displayed on the report will be filtered according to tagged tasks as follows:          1.) Only employees with hours in the tagged tasks will be displayed on the report.  2.) Only timecard records assigned to the tagged task(s) will be used to calculate totals for display on the report. All other timecard records for employees will ignored when this option is set to Yes. |

# Timecard Detail With Weekly Totals

Displays employee activity for each day within the date range specified.
Includes in and out times in addition to employee totals, exceptions,
and weekly totals.

Report Example:

![](images_2/Rpt045.png)

Notes/Usage:

* Ideal for customers with Bi-Weekly Pay Periods.
* The Timecard Detail with Weekly Totals Report is one of the most
  commonly used reports for reviewing employee timecards, especially
  prior to running payroll.
* The Timecard Detail with Weekly Totals Report displays weekly totals
  in addition to all timecard punches and other activity records present
  for employees during the date range set on the Report Selection Criteria.
* The Timecard Detail Report with Weekly Totals includes the Timecard
  Review History option which displays a list of all supervisors and
  their Position, as set on their Employee Profile, who have reviewed
  all of the employee's timecards during the respective date range.
  An example of the Timecard Review History table is shown below.![](images_2/TimecardReviewHistory.jpg)

Options:

| Option | Default Value | Description |
| Allow Graphics On the Report? | Yes | This option allows you to choose if you want to print the InfiniTime 7.0 logo on the report. |
| Department Grouping Type? | None | This option allows you to group the report by the employees Activity Department, meaning that the hours will distribute to all the departments the employee worked, or group by Employee Default Department,which will put all the time worked in their default department even if they worked on other departments, or the last option is None. |
| Department Selection Based On? | Employee Default Department | This option will allow you to select how the Department  filter is used to select employees. By default, departments tagged on the selection criteria will cause InfiniTime to display employees assigned to that department on the report. Alternatively, selecting 'Worked in Department' will show employees that worked in the selected department during the selected date range. |
| Department Selection Filters Activity? | No | If this option is set to Yes, employee Timecard Records displayed on the report will be filtered according to tagged departments as follows:          1.) Only employees with Timecards in the tagged department(s) will be displayed on the report.  2.) Only Timecard records assigned to the tagged department(s) will be used to calculate totals for display on the report. All other timecard records for employees will be ignored when this option is set to Yes. |
| Employee Signature Message? | None | Permits the user to specify a disclaimer or message to be displayed under the employee signature line. The Employee Signature message will only be displayed on the Report if 'Print Employee Signature Line?' is set to Yes. |
| Group By Supervisor? | No | This option will group employees specified by the Employee Filter according to their Default Supervisor. |
| Group Level to group by: | No | This option will sort employees specified by the Employee Filter according to their group description for the selected group level. For example, a company with multiple locations might have a Group Level of 'Location' and Group Descriptions of 'Pittsburgh' , 'Phoenix' , and 'Jacksonville'. Selecting the 'Location' group level would sort employees according to their assigned location. |
| Hide Audit Trail Asterisk? | No | If this option is set to Yes, the Audit Trail Asterisk will not be shown on the Timecard Detail Report. By default, when this option is set to No, any timecard punches with an audit trail record will be marked with an asterisk (\*).    Audit Trail records are automatically created by the InfiniTime software when timecard records are altered by supervisors and / or payroll personnel. |
| Hide Exceptions? | No | This option, when set to Yes, will prevent the Timecard Detail report from displaying exceptions such as Absent and Missed punch. By default, Exceptions are displayed on the Timecard Detail Report. |
| Job Grouping Type? | None | Determines how employees will be grouped by Jobs. When set to None the option is considered disabled and employees will not be grouped by jobs.  When set to Employee Default Job employees will be grouped according to their default job as assigned on their employee record. When set to Scheduled Job employees will be grouped according to the job they were scheduled for. |
| Job Selection Based On: | Employee Default Job | This option will allow you to select how the Job filter is used to select employees. By default, jobs tagged on the selection criteria will cause InfiniTime to display employees assigned to the job on the report. Alternatively, selecting 'Worked in Job'' will show employees that worked in the selected job during the chosen date range. |
| Job Selection Filters Activity? | No | If this option is set to Yes, employee Timecard Records displayed on the report will be filtered according to tagged departments as follows:          1.) Only employees with hours in the tagged Job(s) will be displayed on the report.  2.) Only timecard records assigned to the tagged Job(s) will be used to calculate totals for display on the report. All other timecard records for employees will ignored when this option is set to Yes. |
| Page Break by Department? | No | This option will allow you page break the report by Department, making it easier to give the report to department heads for review if needed. |
| Page Break by Employee? | No | This option will allow you to page break the report based on each employee, making it easier to give the report to the individual employees for review. |
| Page Break by Group? | No | This option will allow you to page break the report based on each Group Description and is intended for use with 'Group Level to Group By.' The  report can then be distributed as necessary. |
| Page Break by Job? | No | This option will allow you to page break the report by Job, making it easier to give the reports to Job Supervisors for review. |
| Page Break by Supervisor? | No | This option will allow you to page break the report based on Employee Supervisors, making it easier to distribute to Supervisors for review. |
| Page Break by Task? | No | This option will allow you to page break the report by Task, making it easier to give the reports to Task Supervisors for review. |
| Print Employee Signature Line? | No | When set to yes a signature line is displayed at the bottom of the report for employees to sign. This option is generally used in combination with the 'Page Break by Employee' option. |
| Print Inactive Employees? | No | This option will allow you to print information for both Active and Inactive Employees. |
| Print Supervisor Signature Line? | No | When set to yes a signature line is displayed at the bottom of the report for supervisors to sign. This option is generally used in combination with the 'Page Break by Employee' or 'Page break by Supervisor' options. |
| Print Time in Hours and Minutes? | No | InfiniTime reports activity in hundredths of an hour by default. Setting this option to Yes displays activity totals in hours and minutes. |
| Print Timecard Review History? | No | When enabled, Timecard Review history displays a list of supervisors, including Supervisor Name, Supervisor Position, and Last Review Time, for each employee who have reviewed all of the employees Timecard Records for the selected date range. A supervisor's name will not be listed if all records during the date range are not reviewed by the supervisor. Only the Timecard Review History header will be displayed if there are no supervisors who have reviewed all of an employee's Timecard Records for the selected date range. |
| Print Weekly Totals? | Yes | Enabling this option adds a subtotal row for each week to the Timecard Detail report. Note that this option is enabled by default for the Timecard Detail with Weekly Totals Report. |
| Punch Description Displays? | Nothing | The Timecard Detail Report includes a small space to the right of the In and Out Times which permits display of additional details. By default, the Punch Description is blank. The user may select from the following options to display additional details in the Punch Description:    Clock Description - Prints the Clock Name for the hardware reader from which the punch was polled on the Timecard Detail Report.  Grace Periods - Prints Early and Tardy indicators, along with the number of early and / or tardy minutes, on the Timecard Detail Report.  Telephone Number - Prints the Telephone Number from which the employee called in to punch on the Timecard Detail report. Only supported for InfiniTime customers with Telephone Punch. |
| Show Company Grand Total? |  | When set to Yes a total record will be added to the bottom of the report to show total company hours  for selected columns. |
| Sort by Employee Number | No | This option will group employees specified by the Employee Filter according to their Employee ID. |
| Supervisor Signature Message: | None | Permits the user to specify a disclaimer or message to be displayed under the supervisor signature line. The Supervisor Signature message will only be displayed on the Report if 'Print Supervisor Signature Line?' is set to Yes. |
| Task Grouping Type? | None | Determines how employees will be grouped by Tasks. When set to None   the option is considered disabled and employees will not be grouped by   tasks. When set to Employee Default Task employees will be grouped according to their default task as assigned on their employee record. When set to Scheduled Task employees will be grouped according to the task they were scheduled to work in. |
| Task Selection Based On: | Employee Default Task | This option will allow you to select how the Task filter is used to select employees. By default, tasks tagged on the selection criteria will cause InfiniTime to display employees assigned to the task on the report. Alternatively, selecting 'Worked in Task'' will show employees that worked in the selected task during the chosen date range. |
| Task Selection Filters Activity? | No | If this option is set to Yes, employee Timecard Records displayed on the report will be filtered according to tagged tasks as follows:          1.) Only employees with hours in the tagged tasks will be displayed on the report.  2.) Only timecard records assigned to the tagged task(s) will be used to calculate totals for display on the report. All other timecard records for employees will ignored when this option is set to Yes. |

# Timecard Summary

Displays an employee activity summary with hourly totals for the entire
date range according the employees and date range specified by Selection
Criteria.

Report Example:

![](images_2/Rpt042.png)

Notes/Usage:

* Useful for viewing how employee hours are distributed across various
  hours types for a given date range.

Options:

The Timecard Daily Summary Report is a user customizable report. Refer
to the [Customizable Report
Section](/InfiniTime/help%20file/User_Customizable_Reports.md) of this manual for more information.

# Timecard With Clock Description

Displays employee activity for each day within the date range specified.
Includes in and out times in addition to employee totals, exceptions,
and the description of the clock used by the employee for each punch.
Also displays the Clock Description.

Report Example:

![](images_2/Rpt047.png)

Notes/Usage:

* The Timecard With Clock Description is identical to the Timecard
  Detail report with one exception.
* By default, the Punch Description field of the Timecard With Clock
  Description Report shows the Clock Description.

Options:

| Option | Default Value | Description |
| Allow Graphics On the Report? | Yes | This option allows you to choose if you want to print the InfiniTime 7.0 logo on the report. |
| Department Grouping Type? | None | This option allows you to group the report by the employees Activity Department, meaning that the hours will distribute to all the departments the employee worked, or group by Employee Default Department,which will put all the time worked in their default department even if they worked on other departments, or the last option is None. |
| Department Selection Based On? | Employee Default Department | This option will allow you to select how the Department  filter is used to select employees. By default, departments tagged on the selection criteria will cause InfiniTime to display employees assigned to that department on the report. Alternatively, selecting 'Worked in Department' will show employees that worked in the selected department during the selected date range. |
| Department Selection Filters Activity? | No | If this option is set to Yes, employee Timecard Records displayed on the report will be filtered according to tagged departments as follows:          1.) Only employees with Timecards in the tagged department(s) will be displayed on the report.  2.) Only Timecard records assigned to the tagged department(s) will be used to calculate totals for display on the report. All other timecard records for employees will be ignored when this option is set to Yes. |
| Employee Signature Message? | None | Permits the user to specify a disclaimer or message to be displayed under the employee signature line. The Employee Signature message will only be displayed on the Report if 'Print Employee Signature Line?' is set to Yes. |
| Group By Supervisor? | No | This option will group employees specified by the Employee Filter according to their Default Supervisor. |
| Group Level to group by: | No | This option will sort employees specified by the Employee Filter according to their group description for the selected group level. For example, a company with multiple locations might have a Group Level of 'Location' and Group Descriptions of 'Pittsburgh' , 'Phoenix' , and 'Jacksonville'. Selecting the 'Location' group level would sort employees according to their assigned location. |
| Hide Audit Trail Asterisk? | No | If this option is set to Yes, the Audit Trail Asterisk will not be shown on the Timecard Detail Report. By default, when this option is set to No, any timecard punches with an audit trail record will be marked with an asterisk (\*).    Audit Trail records are automatically created by the InfiniTime software when timecard records are altered by supervisors and / or payroll personnel. |
| Hide Exceptions? | No | This option, when set to Yes, will prevent the Timecard Detail report from displaying exceptions such as Absent and Missed punch. By default, Exceptions are displayed on the Timecard Detail Report. |
| Job Grouping Type? | None | Determines how employees will be grouped by Jobs. When set to None the option is considered disabled and employees will not be grouped by jobs.  When set to Employee Default Job employees will be grouped according to their default job as assigned on their employee record. When set to Scheduled Job employees will be grouped according to the job they were scheduled for. |
| Job Selection Based On: | Employee Default Job | This option will allow you to select how the Job filter is used to select employees. By default, jobs tagged on the selection criteria will cause InfiniTime to display employees assigned to the job on the report. Alternatively, selecting 'Worked in Job'' will show employees that worked in the selected job during the chosen date range. |
| Job Selection Filters Activity? | No | If this option is set to Yes, employee Timecard Records displayed on the report will be filtered according to tagged departments as follows:          1.) Only employees with hours in the tagged Job(s) will be displayed on the report.  2.) Only timecard records assigned to the tagged Job(s) will be used to calculate totals for display on the report. All other timecard records for employees will ignored when this option is set to Yes. |
| Page Break by Department? | No | This option will allow you page break the report by Department, making it easier to give the report to department heads for review if needed. |
| Page Break by Employee? | No | This option will allow you to page break the report based on each employee, making it easier to give the report to the individual employees for review. |
| Page Break by Group? | No | This option will allow you to page break the report based on each Group Description and is intended for use with 'Group Level to Group By.' The  report can then be distributed as necessary. |
| Page Break by Job? | No | This option will allow you to page break the report by Job, making it easier to give the reports to Job Supervisors for review. |
| Page Break by Supervisor? | No | This option will allow you to page break the report based on Employee Supervisors, making it easier to distribute to Supervisors for review. |
| Page Break by Task? | No | This option will allow you to page break the report by Task, making it easier to give the reports to Task Supervisors for review. |
| Print Employee Signature Line? | No | When set to yes a signature line is displayed at the bottom of the report for employees to sign. This option is generally used in combination with the 'Page Break by Employee' option. |
| Print Inactive Employees? | No | This option will allow you to print information for both Active and Inactive Employees. |
| Print Supervisor Signature Line? | No | When set to yes a signature line is displayed at the bottom of the report for supervisors to sign. This option is generally used in combination with the 'Page Break by Employee' or 'Page break by Supervisor' options. |
| Print Time in Hours and Minutes? | No | InfiniTime reports activity in hundredths of an hour by default. Setting this option to Yes displays activity totals in hours and minutes. |
| Print Timecard Review History? | No | When enabled, Timecard Review history displays a list of supervisors, including Supervisor Name, Supervisor Position, and Last Review Time, for each employee who have reviewed all of the employees Timecard Records for the selected date range. A supervisor's name will not be listed if all records during the date range are not reviewed by the supervisor. Only the Timecard Review History header will be displayed if there are no supervisors who have reviewed all of an employee's Timecard Records for the selected date range. |
| Print Weekly Totals? | No | Enabling this option adds a subtotal row for each week to the Timecard Detail report. |
| Punch Description Displays? | Clock Description | By Default, the Timecard Detail with Clock Description displays the Clock Description on the report.    The Timecard Detail Report includes a small space to the right of the In and Out Times which permits display of additional details. By default, the Punch Description is blank. The user may select from the following options to display additional details in the Punch Description:    Clock Description - Prints the Clock Name for the hardware reader from which the punch was polled on the Timecard Detail Report.  Grace Periods - Prints Early and Tardy indicators, along with the number of early and / or tardy minutes, on the Timecard Detail Report.  Telephone Number - Prints the Telephone Number from which the employee called in to punch on the Timecard Detail report. Only supported for InfiniTime customers with Telephone Punch. |
| Show Company Grand Total? |  | When set to Yes a total record will be added to the bottom of the report to show total company hours  for selected columns. |
| Sort by Employee Number | No | This option will group employees specified by the Employee Filter according to their Employee ID. |
| Supervisor Signature Message: | None | Permits the user to specify a disclaimer or message to be displayed under the supervisor signature line. The Supervisor Signature message will only be displayed on the Report if 'Print Supervisor Signature Line?' is set to Yes. |
| Task Grouping Type? | None | Determines how employees will be grouped by Tasks. When set to None   the option is considered disabled and employees will not be grouped by   tasks. When set to Employee Default Task employees will be grouped according to their default task as assigned on their employee record. When set to Scheduled Task employees will be grouped according to the task they were scheduled to work in. |
| Task Selection Based On: | Employee Default Task | This option will allow you to select how the Task filter is used to select employees. By default, tasks tagged on the selection criteria will cause InfiniTime to display employees assigned to the task on the report. Alternatively, selecting 'Worked in Task'' will show employees that worked in the selected task during the chosen date range. |
| Task Selection Filters Activity? | No | If this option is set to Yes, employee Timecard Records displayed on the report will be filtered according to tagged tasks as follows:          1.) Only employees with hours in the tagged tasks will be displayed on the report.  2.) Only timecard records assigned to the tagged task(s) will be used to calculate totals for display on the report. All other timecard records for employees will ignored when this option is set to Yes. |

# Timecard With Phone Numbers

Displays employee activity for each day within the date range specified.
Includes in and out times in addition to employee totals, exceptions,
and the employeeâs phone number

Report Example:

![](images_2/Rpt046.png)

Notes/Usage:

* The Timecard With Clock Description is identical to the Timecard
  Detail report with one exception.
* By default, the Punch Description field of the Timecard With Phone
  Numbers Report shows the Telephone Number from which an employee called
  into the Telephone Punch System.

Options:

| Option | Default Value | Description |
| Allow Graphics On the Report? | Yes | This option allows you to choose if you want to print the InfiniTime 7.0 logo on the report. |
| Department Grouping Type? | None | This option allows you to group the report by the employees Activity Department, meaning that the hours will distribute to all the departments the employee worked, or group by Employee Default Department,which will put all the time worked in their default department even if they worked on other departments, or the last option is None. |
| Department Selection Based On? | Employee Default Department | This option will allow you to select how the Department  filter is used to select employees. By default, departments tagged on the selection criteria will cause InfiniTime to display employees assigned to that department on the report. Alternatively, selecting 'Worked in Department' will show employees that worked in the selected department during the selected date range. |
| Department Selection Filters Activity? | No | If this option is set to Yes, employee Timecard Records displayed on the report will be filtered according to tagged departments as follows:          1.) Only employees with Timecards in the tagged department(s) will be displayed on the report.  2.) Only Timecard records assigned to the tagged department(s) will be used to calculate totals for display on the report. All other timecard records for employees will be ignored when this option is set to Yes. |
| Employee Signature Message? | None | Permits the user to specify a disclaimer or message to be displayed under the employee signature line. The Employee Signature message will only be displayed on the Report if 'Print Employee Signature Line?' is set to Yes. |
| Group By Supervisor? | No | This option will group employees specified by the Employee Filter according to their Default Supervisor. |
| Group Level to group by: | No | This option will sort employees specified by the Employee Filter according to their group description for the selected group level. For example, a company with multiple locations might have a Group Level of 'Location' and Group Descriptions of 'Pittsburgh' , 'Phoenix' , and 'Jacksonville'. Selecting the 'Location' group level would sort employees according to their assigned location. |
| Hide Audit Trail Asterisk? | No | If this option is set to Yes, the Audit Trail Asterisk will not be shown on the Timecard Detail Report. By default, when this option is set to No, any timecard punches with an audit trail record will be marked with an asterisk (\*).    Audit Trail records are automatically created by the InfiniTime software when timecard records are altered by supervisors and / or payroll personnel. |
| Hide Exceptions? | No | This option, when set to Yes, will prevent the Timecard Detail report from displaying exceptions such as Absent and Missed punch. By default, Exceptions are displayed on the Timecard Detail Report. |
| Job Grouping Type? | None | Determines how employees will be grouped by Jobs. When set to None the option is considered disabled and employees will not be grouped by jobs.  When set to Employee Default Job employees will be grouped according to their default job as assigned on their employee record. When set to Scheduled Job employees will be grouped according to the job they were scheduled for. |
| Job Selection Based On: | Employee Default Job | This option will allow you to select how the Job filter is used to select employees. By default, jobs tagged on the selection criteria will cause InfiniTime to display employees assigned to the job on the report. Alternatively, selecting 'Worked in Job'' will show employees that worked in the selected job during the chosen date range. |
| Job Selection Filters Activity? | No | If this option is set to Yes, employee Timecard Records displayed on the report will be filtered according to tagged departments as follows:          1.) Only employees with hours in the tagged Job(s) will be displayed on the report.  2.) Only timecard records assigned to the tagged Job(s) will be used to calculate totals for display on the report. All other timecard records for employees will ignored when this option is set to Yes. |
| Page Break by Department? | No | This option will allow you page break the report by Department, making it easier to give the report to department heads for review if needed. |
| Page Break by Employee? | No | This option will allow you to page break the report based on each employee, making it easier to give the report to the individual employees for review. |
| Page Break by Group? | No | This option will allow you to page break the report based on each Group Description and is intended for use with 'Group Level to Group By.' The  report can then be distributed as necessary. |
| Page Break by Job? | No | This option will allow you to page break the report by Job, making it easier to give the reports to Job Supervisors for review. |
| Page Break by Supervisor? | No | This option will allow you to page break the report based on Employee Supervisors, making it easier to distribute to Supervisors for review. |
| Page Break by Task? | No | This option will allow you to page break the report by Task, making it easier to give the reports to Task Supervisors for review. |
| Print Employee Signature Line? | No | When set to yes a signature line is displayed at the bottom of the report for employees to sign. This option is generally used in combination with the 'Page Break by Employee' option. |
| Print Inactive Employees? | No | This option will allow you to print information for both Active and Inactive Employees. |
| Print Supervisor Signature Line? | No | When set to yes a signature line is displayed at the bottom of the report for supervisors to sign. This option is generally used in combination with the 'Page Break by Employee' or 'Page break by Supervisor' options. |
| Print Time in Hours and Minutes? | No | InfiniTime reports activity in hundredths of an hour by default. Setting this option to Yes displays activity totals in hours and minutes. |
| Print Timecard Review History? | No | When enabled, Timecard Review history displays a list of supervisors, including Supervisor Name, Supervisor Position, and Last Review Time, for each employee who have reviewed all of the employees Timecard Records for the selected date range. A supervisor's name will not be listed if all records during the date range are not reviewed by the supervisor. Only the Timecard Review History header will be displayed if there are no supervisors who have reviewed all of an employee's Timecard Records for the selected date range. |
| Print Weekly Totals? | No | Enabling this option adds a subtotal row for each week to the Timecard Detail report. |
| Punch Description Displays? | Telephone Number | By Default, the Timecard Detail with Phone Numbers displays phone numbers in the Punch Description.    The Timecard Detail Report includes a small space to the right of the In and Out Times which permits display of additional details. By default, the Punch Description is blank. The user may select from the following options to display additional details in the Punch Description:    Clock Description - Prints the Clock Name for the hardware reader from which the punch was polled on the Timecard Detail Report.  Grace Periods - Prints Early and Tardy indicators, along with the number of early and / or tardy minutes, on the Timecard Detail Report.  Telephone Number - Prints the Telephone Number from which the employee called in to punch on the Timecard Detail report. Only supported for InfiniTime customers with Telephone Punch. |
| Show Company Grand Total? |  | When set to Yes a total record will be added to the bottom of the report to show total company hours  for selected columns. |
| Sort by Employee Number | No | This option will group employees specified by the Employee Filter according to their Employee ID. |
| Supervisor Signature Message: | None | Permits the user to specify a disclaimer or message to be displayed under the supervisor signature line. The Supervisor Signature message will only be displayed on the Report if 'Print Supervisor Signature Line?' is set to Yes. |
| Task Grouping Type? | None | Determines how employees will be grouped by Tasks. When set to None   the option is considered disabled and employees will not be grouped by   tasks. When set to Employee Default Task employees will be grouped according to their default task as assigned on their employee record. When set to Scheduled Task employees will be grouped according to the task they were scheduled to work in. |
| Task Selection Based On: | Employee Default Task | This option will allow you to select how the Task filter is used to select employees. By default, tasks tagged on the selection criteria will cause InfiniTime to display employees assigned to the task on the report. Alternatively, selecting 'Worked in Task'' will show employees that worked in the selected task during the chosen date range. |
| Task Selection Filters Activity? | No | If this option is set to Yes, employee Timecard Records displayed on the report will be filtered according to tagged tasks as follows:          1.) Only employees with hours in the tagged tasks will be displayed on the report.  2.) Only timecard records assigned to the tagged task(s) will be used to calculate totals for display on the report. All other timecard records for employees will ignored when this option is set to Yes. |