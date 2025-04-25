---
title: "InfiniTime Software Overview"
description: "A comprehensive guide for new users to understand InfiniTime modules, access methods, user interface, and essential features."
---

## InfiniTime Software Overview

### InfiniTime Modules

InfiniTime includes a
variety of features to support diverse sets of Human Resource and Time
& Attendance practices within the United States and abroad. InfiniTime Software Administrators
and Users should not feel compelled to use all available features simply
because they are discussed during the Inception Technologies
Implementation Process, introduced during training, or documented in this
manual and available for use. The vast majority of features and settings
within the InfiniTime Software
are optional and can be disabled or used as necessary based upon the customer's
requirements and company policy.  It is important to keep this in
mind as you review your organization's requirements and InfiniTime's capabilities.

![](/img/DatePickerGraphic.gif)

InfiniTime includes four
separate modules, each intended for different purposes as outlined below.
The Client Shortcuts Folder, as created on the Desktop of the InfiniTime Server and distributed
to client machines by the InfiniTime
Administrator, includes a shortcut to each module.

In the Manager
Module you canâ¦

- View employee information
- View and edit employee activity
- Run reports
- Schedule setup
- Access Escort Windows
- In & Out Board Access
- Most of the users time spent with the application will be in the
  manager module.
- Basically all administrative tasks such as adjusting employee schedules,
  editing timecards, and printing reports can be performed within the
  manager module.

![](/img/DatePickerGraphic.gif)

In the Employee
Moduleâ¦

- Employees can view a history of their timecard information back
  to when they started using the system.
- Employees can view current schedule information.
- Employees can Run Reports designated for use within the employee
  module by software Administrators.
- Send messages to their supervisor in the form of:

* Comments
* Requests for Schedule Change
* Requests for Vacation / Time Off

- Employees can Clock In and Out
- Employees can view the In & Out Board
- Self Service:

* Even if your organization chooses not to use the employee module
  for punching in and out it still may be useful to allow employees
  to view and print their schedule and access a history of their
  time in the system. Use of the Employee Module for self service
  purposes can help eliminate routine and / or non business critical
  interruptions to Payroll Staff and / or Employee Supervisors.

![](/img/EscortExample.png)

In the Escort
Module you canâ¦

- Identify tasks that an employee performs on a regular basis within
  InfiniTime and place
  a button corresponding to only those tasks on a window.
- Serves as a Customized Portal to the InfiniTime
  Application
- Layout is completely user customizable with the ability to add
  labels, links, and images.
- Very useful for employees who are not highly computer literate
  or who might be overwhelmed by the number of features in the manager
  module..
- Escort users donât have to learn the entire application â only
  the areas they use on a regular basis. IE: You want to run a report.
  With escort the user only has to click on a single button where in
  the manager module they would have to Open the Report Library, Find
  the Report they want, Configure Report Settings, and finally review
  the results.

![](/img/Valid_Departments.gif)

In the Punch
Module you canâ¦

- The Punch Module is In essence a stripped down version of the employee
  module.
- Provides a basic software time clock interface.
- Allows employees to punch in or out as necessary.
- Can be used by employees who are offsite but have access to a computer
  and the internet (Software must be published)
- Can be used to collect Employee Punches in place of hardware units
  such as the Scout / Zephyr ect. for both Local and Remote Users.

![](/img/WordDoc.gif)

### InfiniTimeMain Toolbar

The Main Toolbar includes buttons for access to the most commonly used
items, such as Employee Profiles, the Company Timecard Table, the Schedule
GANNT Chart, Reports, and Payroll Export. Items on the main toolbar are
generally used during initial setup as well as on a daily or weekly basis
by InfiniTime Software
Administrators and End users.

![](/img/Grid.gif)

### Policies Tab - Introduction

![](/img/T12.gif)

Policies dictate how InfiniTime
handles timecard activity for employees â rounding rules, break rules,
scheduling rules, and overtime rules in addition to other Time and Attendance
related functions are directly controlled by policy settings. The policies
tab of the Company Update Form displays a list of all policies configured
in the software. When configuring policies within InfiniTime
the first step is to identify different groups of employees within an
organization that will require separate policies. Additional details regarding
configuring policies are provided in the [Policy
Configuration Section](Policies/Policy_Overview.md#pol1_Policy_Overview) of this document.

### Exception Types Tab - Introduction

![](/img/Trained_Tasks.gif)

The Exceptions Tab of the Company Update Form displays a list of all
company wide exceptions. Exceptions are conditions that can be tracked
by InfiniTime. It is important
to note that most exceptions require some configuration. When an employee
meets a condition for a tracked exception  they will be flagged with
the corresponding exception as appropriate. Initially, it is important
to understand the following concepts regarding InfiniTime
Exceptions:

- Exceptions can be configured in two ways:

* Company Wide Exceptions - Company Wide Exceptions are tracked
  for all employees. Company Wide Exceptions can be configured from
  the Exception Types Tab of the Company Update Form or from the
  Exception Type Table: Company - Setup - Exception Types on the
  Main Toolbar.
* Policy Specific Exceptions - Policy Specific Exceptions are
  tracked only for employees assigned to the respective policy.
  Policy Specific Exceptions can be configured in the Exceptions
  Section on the Policy Update Form which can be accessed via: Company
  - Setup - Policies on the Main Toolbar.

- InfiniTime
  offers multiple exceptions for detailed employee performance tracking.
  Schedules are required for most exceptions. For example, it is simply
  not possible for InfiniTime
  to determine if an employee is late without a schedule defining when
  the employee is expected to report to work..

- Two exceptions which can be tracked without the use of schedules
  are:

* Missed Punch
* Overtime

The Missed Punch Exception is recommended for use in all production
InfiniTime installations.
The missing punch exception tracks missing punches by using a timer. Employees
have a certain duration of time to clock out after punching in. If employees
do not punch out in this window of time then their punch pair for the
respective date will be tagged with the Missed Punch exception and their
next punch will be considered a clock in. For example:

An Employee Punches for the following times in a day:

8:00 AM (IN)

11:00 AM (OUT)

5:00 PM (IN)

The employee came in at 8AM, left for lunch
at 11AM, and came back from lunch at 12:00 PM though he forgot to punch.
He then left at 5PM. To the software it looks like the employee worked
from 8AM to 11PM and then came back in at 5PM. The software then waits
a predefined number of hours as configured in the employee's policy under
the missing punch threshold setting. Lets say the missing punch threshold
was set to 12 hours. In that case the software would recognize the employee
had not punched out by 5AM the next day and the 5:00 PM punch pair would
be tagged with the Missed Punch exception. The employees next punch at
8:00 AM would then be considered a punch in.

### Shifts Tab - Introduction

The Shifts Tab of the Policy Update Form displays a list of all Shifts
configured in the software. Shifts are one of the several scheduling options
available within InfiniTime
and are one of the most flexible scheduling methods. Initially, it is
important to understand the following concepts regarding Scheduling and
InfiniTime Shifts:

- Scheduling provides the ability to track additional exceptions
  such as tardy, late departure, early departure, early arrival ect.
  If schedules are not configured for employees these exceptions will
  never trigger.
- Shifts can also be used to configure shift differentials where
  employees receive an additional amount or percentage per hour while
  working within a specific time window.
- Additional information regarding configuring employee schedules
  can be found in the [Schedule
  Configuration section](Scheduling/Scheduling.md#sch01_What_do_I_want_to_accomplish_by_using_schedules_) of this document.

### Other Activity Tab Introduction

Displays a list of all Hours and Earning Types outside of regular and
overtime hours. There is no limit to the number of other activity types
that can be configured. Most customers will need to one or more Other
Activity Types for paid leave hours such as Jury Duty, Bereavement Pay,
etc. Additional details regarding Other Activity Types can be found in
the [Other Activity Configuration
Section](Configuration/Product_Configuration.md#ota01_Other_Activity_Types) of this document.

### Valid IP Tab Introduction

The Valid IP Tab of the Company Update form is used to define Company
Valid IP Addresses. Additional details regarding Company Valid IP Addresses
can be found in the [Company
Valid IP Addresses](Security/Security_Overview.md#sec23_Valid_IP_Addresses_-_Overview) section of this document.

### Department

The Department Button opens the Department Table which displays the
same information as the Departments Tab of the Company Update Form. Additional
details on job costing and InfiniTime
Departments configuration can be found in the [Job
Costing Section of this document.](Configuration/Product_Configuration.md#cnf01_Job_Costing_Introduction)

### Employee

The Employee Button opens the Employee Table which displays a list of
all employees in the software similar to the employee list on the company
update form. Employee Profiles, related settings, and configuration are
detailed below in the [Employee
Profiles and Related Settings Section.](ovr_SoftwareOverview.md#so153_Employee_Profiles_and_Related_Settings)

### Timecards

The Timecards Button opens the company timecard table which displays
a list of all employees in the software on the upper portion of the window
and their timecard activity for a specified date range on the lower portion.
The Company Timecard Table is best suited for editing timecards and is
intended for use when reviewing timecards for multiple employees. Additional
Details on use of the Company Timecard Table and Editing Employee Timecards
can be found in the [Timecard
Editing Section](TimecardEditing/TimecardEditing.md#tim01_Timecard_Editing_Overview) of this document.

### In & Out Button

The In & Out Button displays the In & Out Board which lists
all employees in the software and their current in / out status. A green
check mark indicates the employee is clocked in while a red x indicates
the employee is punched out.

### Report Library Button

The Report button displays the Report Library which lists all of the
reports included with InfiniTime
broken down by major categories such as Timecard Reports, Payroll Reports,
Management Reports ect. Additional details on available reports and use
of the Report Library can be found in the [Reports
Section](Reports/Reports.md#rpt01_InfiniTime_Reports_-_Introduction) of this document.

### Payroll Export Button

The Payroll Export button opens the Payroll Export Table which lists
all Payroll Export Definitions currently defined within InfiniTime. Payroll Export provides
the ability to export timecard information in a format compatible with
various 3rd Party Payroll Applications. Additional Details on the use
and configuration of Payroll Export can be found in the [Payroll
Export Section](PayrollExport/Payroll_Export.md#pxh2_Introduction) of this document.
