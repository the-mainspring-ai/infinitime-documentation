---
title: ""
description: ""
---

Company Button Introduction

![](/img/SoftwareOverview_001_Btn4_Timecards.png)

The Company Button opens the Company Update Form which displays a general
overview of the InfiniTime
configuration. Items such as policies, company wide software settings,
and exceptions can be viewed by using the Company Button. InfiniTime uses two methods to organize
buttons, fields, and objects on Forms throughout the software. Tabs, as
shown below, can be used to view different details on a single form.

![](/img/Balnk_Availability.gif)

Company Update Form

- General Tab

Company Info

The General Tab of the Company Update Form
includes the Company Name, Address, City, State, and Zip. These details
are initially filled from the InfiniTime
Software License Information, though they can be updated if an organizations
should details change.

General
Tab - Functional Options

![](/img/Federal_Tax_Information.gif)

Options on the Company Update Form are separated
into two tabs. Functional Options alter the operation of a specific feature
or set of features within the InfiniTime
Application. A complete description for each functional option is listed
below.

Disable
Audit Trail

If the audit trail is enabled (unchecked)
a dialog box will be displayed when users attempt to manually edit or
insert a punch. The users can then enter information about why they are
altering an employee activity or inserting a punch manually as shown below.
If Disable Audit Trail is unchecked, the Audit Description Update form
will be displayed after every change to a timecard record. When the audit
description update form is displayed as shown below a comment must be
entered. It is not possible to leave the comment field blank.

It should be noted that any open Timecard
Editors must be closed and reopened when the Disable Audit Trail feature
is toggled on or off, as the timecard tables check this setting only when
they are opened.

![](/img/UpdateTIS_AuditNote.gif)

Allow PC Punch Labor Switching

If this box is checked, then employees using
the PC punch will be allowed to switch departments, tasks, or jobs when
clocking in or out.

Note: Employees can be granted access to
Department, Task, and Job switching capabilities in any fashion. In order
to accomplish this Allow PC Punch Labor Switching must first be enabled.
Security configuration can then be used on the Punch Information Window
within the Employee or Punch Modules to permit or deny access to Department,
Task, Job switching fields individually. Access can be granted to denied
to these fields in any combination.

Auto
Assign Default Groups To Security Filter When Inserting Employees

If this box is checked, then all new inserted
employees will have their security filters automatically configured to
include the default group. Generally, the default group is an 'unassigned'
group which all supervisors have the ability to see. This ensures supervisors
will be able to see and work with employees even if they forget to assign
the employee's group.

Do Not Add Default Groups
to Employee On Insert

If this box is checked, default groups will
not be assigned when new employees are inserted. This will require the
user who added the employee to manually assign a group to the employee
before saving the record.

Do Not Auto Fill Employee
ID When Inserting Employees

If this option is checked auto fill will
be disabled for the Employee ID, Login ID, and Login Password. This is
useful for companies who have an internal numbering system for employee
identifiers.

Disable
Security Filters For Timecard Activity Department Selection

By default a supervisor granted access to
only a specific department through their security filter will only have
the ability to insert timecard activity associated with the specific department
they have rights to. If this option is checked supervisors will have the
ability to insert timecard activity associated with any department configured
within InfiniTime. For
example Joe Smith's security filters are configured to permit access to
the Manufacturing Department. Joe is able to work with all employees in
the Manufacturing Department and insert activity associated with the Manufacturing
Department by default. By disabling security filters for timecard activity
selection Joe will be able to insert activity under Manufacturing, Sales,
Engineering, and Office for any employees assigned to the Manufacturing
Department.

Use Verification Code
on Login Window

Checking this option enables the CAPTCHA
on the login screen. CAPTCHA's have been integrated into the InfiniTime Logon process in order
to secure against unauthorized access by automated scripts. A CAPTCHA
can be defined as a software program which generates tests that cannot
be passed by current computers but can be passed by humans. Additional
information on CAPTCHA's can be found in Chapter 2 - Security.

Allow Multiple Request
Recipients

Checking this option
enables multiple recipients for the Time Off Request and Schedule Change
Request message types. Refer to the [Messaging
Section](Messaging/Messaging.md#msg01_Messaging_Introduction) of this manual for more details.

Delayed
Save on Timecard Editors

Checking this option
enables the Delayed Save Feature for all Timecard Tables, including the
Company Timecard, Employee Timecard, and Employee Module Timecard. The
Delayed Save feature provides a  user friendly spreadsheet-like In
Line Edit interface for the timecard editors which performs significantly
faster than the traditional timecard where changes are saved each time
a record is altered. The Delayed Save on Timecard Editors option is enabled
by default on new installations.

It should be noted that any open Timecard
Editors must be closed and reopened when the Delayed Save feature is toggled
on or off, as the timecard tables check this setting only when they are
opened.

Delayed Edit on Timecard
Editors

Checking
this option enables the Delayed Edit Feature for all Timecard Tables,
including the Company Timecard, Employee Timecard, and Employee Module
Timecard. The Delayed Edit feature provides a low bandwidth / high latency
friendly view only interface for the timecard editors which performs significantly
faster than the Delayed Save Feature alone. When Delayed Edit is enabled,
the user must click 'Change' on the Timecard table before timecard punches
can be edited. By clicking 'Change' the user will enter Delayed Save mode.
The Delayed Edit on Timecard Editors option is disabled by default on
new installations.

It should be noted that any open Timecard
Editors must be closed and reopened when the Delayed Edit feature is toggled
on or off, as the timecard tables check this setting only when they are
opened.

Delayed Edit and Delayed Save should be enabled
if remote users experience performance difficulties, especially when switching
from employee to employee in the Company Timecard, due to high latency
and / or low bandwidth connections between remote clients and the InfiniTime Server. Enabling Delayed
Edit and Delayed Save will provide a significant performance improvement
compared to the traditional timecard editing user interface utilized when
both Delayed Edit and Delayed Save are disabled.

Disable Overtime Hierarchy
Within Policy

Disable Overtime Hierarchy
within Policy makes it possible to configure Daily or Weekly Overtime
for Overtime 2, Overtime 3, and Overtime 4 even if Daily or Weekly Overtime
for Overtime 1 has not been configured. This option is required only for
organizations with unique Overtime Rules such as those occurring in union
environments. Generally, this option can be left unchecked unless instructed
otherwise by your Implementation Representative.

Stored Procedure Timing

Stored Procedure Timing should remain unchecked
on all production installations. This feature is intended for internal
debugging and performance testing by Inception Technologies
staff.

Enable Missed Punch Schedule
Check

Enabled Missed Punch
Schedule Check alters the Missed Punch Exception logic to correctly flag
Missed Punches based on both the Missed Punch Threshold and an employee's
schedule. This option is enabled by default on new installations.

General
Tab  - Cosmetic Options

![](/img/SoftwareOverview_021.png)

Options on the Company Update Form have been
separated into two groups. Cosmetic Options alter the user interface of
the InfiniTime Application.
A complete description for each functional option is listed below.

Inactivity
Time Out

Inactivity Timeout automatically ends the
session after a specified amount of time with no activity within the InfiniTime Software Application. Activity
within the Software is defined as opening a new window, closing a window,
or performing an action such as inserting a punch. This feature helps
secure management terminals in a workplace that might be accessible to
employees should the manager step away for a short period. Once the predetermined
period of time has elapsed the user will be logged out of the software
and will be unable to continue working in the software until they login
again.

User Password Expires
In

This field allows you to enter an amount
of days that needs to pass before the password expires.  By leaving
it blank or changing the amount you had in the field to zero the passwords
will never expire.

System Date Format

Sets
the Date Format used throughout the InfiniTime
Application. Supported formats are listed below with examples.

| Date Format | Appearance |
| ----------- | ---------- |
| mm/dd/yyyy  |            |
| dd/mm/yyyy  |            |
| yyyy/mm/dd  |            |

System Time Format

Sets the Time Format
used throughout the InfiniTime
Application. Supported formats are listed below with examples.

| Time Format | Appearance |
| ----------- | ---------- |
| hh:mm tt    |            |
| HH:mm       |            |
| hh:mm       |            |

System Window Skin

Sets the window design
used throughout the InfiniTime
Application. Supported skins are listed below with examples.

| Skin Name   | Appearance |
| ----------- | ---------- |
| Vista       |            |
| Black       |            |
| Default     |            |
| Forest      |            |
| Hay         |            |
| Office 2007 |            |
| Outlook     |            |
| Simple      |            |
| Sunset      |            |
| Telerik     |            |
| Web20       |            |
| WebBlue     |            |

Recalculate Button

![](/img/Software_Shortcuts.gif) - This feature allows the user to recalculate
timecard activity _for
the whole company_.  A recalculate should be performed after
making any changes to the policies, or after inserting, changing, or deleting
Holiday Dates. For example, if you should decided to enable rounding for
punches to the nearest quarter hour this will effect employee hour totals.

### Company Menu

![](/img/Employee-Module.gif)

The Company Menu provides access to:

Activity

- Opens the Company Timecard Table. The Company Timecard Table
  is best suited for editing timecards and is intended for use when reviewing
  timecards for multiple employees. As such, the Company Timecard Table
  is often used on a Daily basis by InfiniTime
  Payroll Clerks and employee Supervisors. Additional Details on use of
  the Company Timecard Table and Editing Employee Timecards can be found
  in the [Timecard Editing Section](TimecardEditing/TimecardEditing.md#tim01_Timecard_Editing_Overview)
  of this document.

Setup:

Cellular Provider - Opens
the Cell Phone Providers Table. Cell Phone Providers are utilized to define
the short message service (SMS) gateway for Cellular Providers which is
required for InfiniTime
to send text message notifications to employees and / or supervisors when
exceptions occur. The Cellular Providers table is populated for major
cellular carriers by default. InfiniTime
Software Administrators may add additional Cellular Carriers as needed.
Additional information regarding Cell Phone Providers and Exception Notifications
(IE: Sending Text Message Alerts to Employees or Supervisors when exceptions
occur) can be found in the [Exception
Notifications Section](Policies/Policy_Overview.md#pol33_Exception_Type_Update_Form_-_Notifications_Tab) of
this document.

Departments

- Opens the Department Table which displays the same information
  as the Departments Tab of the Company Update Form. Additional details
  on job costing and InfiniTime
  Departments configuration can be found in the [Job
  Costing Section of this document.](Configuration/Product_Configuration.md#cnf01_Job_Costing_Introduction)

Employees -
 Opens the Employee Table which displays a list of all employees
in the software similar to the employee list on the company update form.
Employee Profiles, related settings, and configuration are detailed below
in the [Employee
Profiles and Related Settings Section.](ovr_SoftwareOverview.md#so153_Employee_Profiles_and_Related_Settings)

Exception Types - Opens
the Exception Types Table which can be used to define Company Wide Exceptions.
It is important to note that Company Wide Exceptions are tracked for all
employees. Additional Details on available Exceptions and Exception related
functionality can be found in the [Exception
Configuration Section](Policies/Policy_Overview.md#pol26_Exceptions) of
this document.

General
Information - Opens the Company
Update Form which displays a general overview of the InfiniTime
configuration. Items such as policies, company wide software settings,
and exceptions can be viewed on the Company Update Form. Additional Information
regarding the Company Update Form and its related options can be found
in the [Company Update Form](ovr_SoftwareOverview.md#so20_Company_Update_Form_-_General_Tab)
section of this document.

Other
Activity Types - Opens the Other
Activity Types Table which displays
a list of all Hours and Earning Types outside of regular and overtime
hours. There is no limit to the number of other activity types that can
be configured. Most customers will need to one or more Other Activity
Types for paid leave hours such as Jury Duty, Bereavement Pay, etc. Additional
details regarding Other Activity Types can be found in the [Other Activity Configuration
Section](Configuration/Product_Configuration.md#ota01_Other_Activity_Types) of this document.

Policies - Opens
the Policy Table which displays
a list of all policies configured in the software. Additional details
regarding configuring policies are provided in the [Policy
Configuration Section](Policies/Policy_Overview.md#pol1_Policy_Overview) of
this document.

Reader
Configuration - Opens the Reader
Configuration Table which lists all hardware devices that are connected
to the InfiniTime software.
Before InfiniTime can poll
employee timecard activity from a hardware device, the hardware device
must be configured. Detailed configuration and installation instructions
are available for each hardware device, by model name, in the Hardware
Documentation section of this
document. General Information on use of the Reader Configuration Table
can be found in the [InfiniTime Administration - Reader
Configuration section of this document.](ovr_SoftwareAdministration.md#ru1_Reader_Configuration_Table)

Shifts

- Opens the Shifts Table which displays
  a list of all Shifts configured in the software. Shifts are one of the
  several scheduling options available within InfiniTime
  and are one of the most flexible scheduling methods. Additional information
  regarding configuring employee schedules can be found in the [Schedule Configuration section](Scheduling/Scheduling.md#sch14_Configuring_Shifts_for_Scheduling_Purposes)
  of this document.

Reports

- Opens the Report Library which lists
  all of the reports included with InfiniTime
  broken down by major categories such as Timecard Reports, Payroll Reports,
  Management Reports ect. Additional details on available reports and use
  of the Report Library can be found in the [Reports Section](Reports/Reports.md#rpt01_InfiniTime_Reports_-_Introduction) of this document.

Payroll
Exports - Opens the Payroll Export Table which lists all Payroll
Export Definitions currently defined within InfiniTime.
Payroll Export provides the ability to export timecard information in
a format compatible with various 3rd Party Payroll Applications. Additional
Details on the use and configuration of Payroll Export can be found in
the [Payroll
Export Section](PayrollExport/Payroll_Export.md#pxh2_Introduction) of this document.
