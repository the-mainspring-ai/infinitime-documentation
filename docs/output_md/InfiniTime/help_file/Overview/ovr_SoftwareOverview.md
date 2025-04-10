xml version="1.0" encoding="utf-8" ?






Software Overview




# InfiniTime Software Overview

### InfiniTime Software Overview Introduction

Intended for new users, or those who wish to re-familiarize themselves
with basic concepts related to use of the InfiniTime
Software, the InfiniTime
Software Overview provides background information on  in InfiniTime's available modules in
addition to essential tasks and concepts. Upon completing this section,
users can expect to have an understanding of:

* How to access InfiniTime
  from a Client Machine
* Modules available with the InfiniTime
  Software and their intended uses
* The InfiniTime
  User Interface

+ How to distinguish between Optional Fields and Required Fields
+ How to use various tools such as In Line Edit, Auto-Complete,
  and the Time / Date Selection Tools to simplify data entry
+ What makes the InfiniTime
  User Interface Unique when compared with other Web Applications

* Using the Main Toolbar within the Manager Module
* Company Related Options
* Employee Related Settings and Related Tasks such as inserting
  an employee
* Basic InfiniTime
  Security Concepts such as Security Roles, Default Security Roles,
  Security Filters, and Employee Supervisors

### Client Access Overview

Accessing the InfiniTime
Software from a Client machine on the network is as simple as entering
the address into your Web Browser, or following a link to the InfiniTime website hosted on the InfiniTime server. As a Web Application,
InfiniTime is subject to
the security settings of the Internet Browser on the Client machine. The
following Browsers are supported:

Microsoft Internet Explorer 8.0

Microsoft Internet Explorer 9.0

Microsoft Internet Explorer 10.0

Safari

Firefox

Note: Always install the latest updates for your browser prior to accessing
InfiniTime.

While it is a Web Application, InfiniTime
is unique. It looks and acts like a windows application. Local printer
usage and full use of the software through a single browser window are
two of the main features that separate InfiniTime
from other Web Applications.

A user wishing to access the InfiniTime
software from a Client machine must know the web address their InfiniTime software is located at.
This address varies depending on the Client machineâs location relative
to the InfiniTime Server
or the Deployment Method chosen. Two methods that can always be used to
access the InfiniTime Software
product regardless of the Clientâs location are through the domain name
or the InfiniTime Serverâs
IP address. Your InfiniTime
Software Administrator, or internal IT Personnel, can provide shortcuts
to the InfiniTime Software
as appropriate for your chosen deployment method. An overview of each
method for accessing the InfiniTime
Software is provided below.

### Universal Access Methods

Universal
Access Methods can be used to access InfiniTime
from any machine on the local network with internet access or any remote
machine with internet access. In order for the universal access methods
to function the InfiniTime
Software must be published to the Internet.

Domain Name

Accessing the InfiniTime
software from any location including on-site and off-site Clients can
be simplified through use of a domain name. Domain names allow an easy
to remember name to be used in order to direct a web browser to a specific
web site. For example the domain name InfiniTimeOnline.com
will forward a web browser to the demo website for the InfiniTime software product.

To access the InfiniTime
Software through use of a Domain Name:

Replace âInfiniTimeOnline.comâ
with your domain name.

| Module Name | Address |
| InfiniTime Manager Module | http://www.InfiniTimeOnline.com/InfiniTimeManagerModule/ |
| InfiniTime Employee Module | http://www.InfiniTimeOnline.com/InfiniTimeEmployeeModule/ |
| InfiniTime Escort | http://www.InfiniTimeOnline.com/InfiniTimeEscort/ |
| InfiniTime Punch Module | http://www.InfiniTimeOnline.com/InfiniTimePunch/ |

Technical Note: Domain Names must be purchased
from a registrar and configured to forward traffic to your InfiniTime Serverâs public IP address.
Your internal IT Personnel can assist with this configuration.

Technical Note: Internet access is required in
order to use the domain name access method.

InfiniTime
Server IP address

The InfiniTime software
can be accessed from off-site Clients though the use of the Serverâs public
IP address. Directing a web browser directly to the InfiniTime
Serverâs IP address eliminates the need for a domain though it is not
as easy to remember. Your public IP address can be obtained from your
Internet Service Provider. On-Site Clients must use the Server's local
IP Address to access the InfiniTime
Software.

Replace â12.47.180.99â in the addresses below with the public IP address
of your server in order to access the InfiniTime
software.

| Module Name | Address |
| InfiniTime Manager Module | http://www.12.47.180.99.com/InfiniTimeManagerModule/ |
| InfiniTime Employee Module | http://www.12.47.180.99.com/InfiniTimeEmployeeModule/ |
| InfiniTime Escort | http://www.12.47.180.99.com/InfiniTimeEscort/ |
| InfiniTime Punch Module | http://www.12.47.180.99.com/InfiniTimePunch/ |

### Stand Alone Server

![](/img/image-404.png)

The InfiniTime Stand
Alone Server acts as both the server and the Client for the InfiniTime software. The InfiniTime software is not only hosted
on the Stand Alone Server, but is also accessed from the Stand Alone Server
machine through Internet Explorer.

Technical Note: Using localhost informs the web
browser to access the default website on the local machine and is the
simplest way to access the InfiniTime 7.0software
from the server. The addresses below can be used from the InfiniTime 7.0Server
for all deployment methods including Stand Alone Deployment. Client Machines
cannot access the InfiniTime
Software using the localhost shortcuts listed below.

| Module Name | Address |
| InfiniTime Manager Module | http://localhost/InfiniTimeManagerModule/ |
| InfiniTime Employee Module | http://localhost/InfiniTimeEmployeeModule/ |
| InfiniTime Escort | http://localhost/InfiniTimeEscort/ |
| InfiniTime Punch Module | http://localhost/InfiniTimePunch/ |

### InfiniTimeServer with On-Site Clients

![](/img/image-404.png)

When accessing the InfiniTime
software from on-site Clients or Client machines on the Local Area Network
the serverâs hostname or IP address can be used. This directs the browser
to a specific machine in order to access the website.

Utilizing the Server's Hostname

Replace âhostnameâ in the addresses with the actual hostname of your
server in order to access the InfiniTime
Software.

| Module Name | Address |
| InfiniTime Manager Module | http://hostname/InfiniTimeManagerModule/ |
| InfiniTime Employee Module | http://hostname/InfiniTimeEmployeeModule/ |
| InfiniTime Escort | http://hostname/InfiniTimeEscort/ |
| InfiniTime Punch Module | http://hostname/InfiniTimePunch/ |

Obtaining the hostname from your InfiniTime Server:

*Technical Note:*
These steps must be performed on the InfiniTime
Server.

Click on Start.

![](/img/image-404.png)

Click on Run.

![](/img/image-404.png)

Type cmd into the dialog box.

![](/img/image-404.png)

Click OK.

A dos window will open. Type hostname.

![](/img/image-404.png)

Hit Enter

The hostname of your computer will be displayed. Dellsupport is the
hostname in the example.

Replace âhostnameâ in the addresses above with the hostname of your
InfiniTime Server. Using
the hostname from the example above the addresses to access the InfiniTime software would be:

| Module Name | Address |
| InfiniTime Manager Module | http://Dellsupport/InfiniTimeManagerModule/ |
| InfiniTime Employee Module | http://Dellsupport/InfiniTimeEmployeeModule/ |
| InfiniTime Escort | http://Dellsupport/InfiniTimeEscort/ |
| InfiniTime Punch Module | http://Dellsupport/InfiniTimePunch/ |

Technical Note: The screenshots above were taken
on Windows XP though these steps are identical regardless of the operating
system in use.

Utilizing the Server's IP Address

Replace â192.168.0.2â with your serverâs
local IP address in order to access the InfiniTime
Software. This is only recommended if the server has a static IP address.

| Module Name | Address |
| InfiniTime Manager Module | http://192.168.0.2/InfiniTimeManagerModule/ |
| InfiniTime Employee Module | http://192.168.0.2/InfiniTimeEmployeeModule |
| InfiniTime Escort | http://192.168.0.2/InfiniTimeEscort |
| InfiniTime Punch Module | http://192.168.0.2/InfiniTimePunch |

Technical Note: Every computer on a given network
must have a unique IP Address in order for computers on the network to
communicate properly. In order for a computer to function properly as
a server it must be readily accessible to Client machines at a known location.
This is accomplished by assigning a Static, or unchanging, IP Address
to the server machine. If a server is not assigned a Static ip address
it will eventually acquire a different address through Dynamic Host Configuration
Protocol. This will cause the server to be unreachable from Client machines
attempting to access the server using the old IP Address.

To obtain the local IP address of the InfiniTime Server:

*Technical
Note:* These steps must be performed on the InfiniTime
Server.

Click on Start.

![](/img/image-404.png)

Click on Run.

![](/img/image-404.png)

Type cmd into the dialog box.

![](/img/image-404.png)

Click OK.

A dos window will open. Type ipconfig /all

![](/img/image-404.png)

Hit enter. The network configuration of
your server will be displayed.

The InfiniTime
Server should have a static ip address. The results below indicate a static
address of 192.168.1.40 with DHCP disabled.

![](/img/image-404.png)

Replacing â192.168.0.2â With the static
address in the example above the addresses for accessing the InfiniTime Software would be:

| Module Name | Address |
| InfiniTime Manager Module | http://192.168.1.40/InfiniTimeManagerModule/ |
| InfiniTime Employee Module | http://192.168.1.40/InfiniTimeEmployeeModule/ |
| InfiniTime Escort | http://192.168.1.40/InfiniTimeEscort/ |
| InfiniTime Punch Module | http://192.168.1.40/InfiniTimePunch/ |

The results below show DHCP enabled. The
server should be configured with a static ip address in order to access
the InfiniTime software
with the Serverâs IP address. Refer to the technical note before this
section for more information.

![](/img/image-404.png)

### InfiniTimeServer with Offsite Clients

![](/img/image-404.png)

Off-site Clients allow employees to clock in and out while abroad. Managers
can also access employee information and edit activity while on a business
trip or even from their own home computer. Off-Site Client machines are
limited to two remote access methods. Off-site Clients can access the
InfiniTime software through
use of a domain name or the InfiniTime
Serverâs public IP address.

Refer to the [Universal
Access Methods section for information about accessing the InfiniTime software with off-site
Clients](ovr_SoftwareOverview.md#so3_Universal_Access_Methods).

### InfiniTimeServer with On-Site and Off-Site Clients

![](/img/image-404.png)

Utilizing both On-Site and Off-Site Client machines provides a versatile
deployment alternative separating Web
Applications from other software applications. Employees on the
local network and abroad have full access to all of InfiniTimeâs
features. Remote users need only a computer or laptop, an Internet connection,
and their login information to connect to the InfiniTime
software.

Refer to the [Off-Site
Client section for accessing the InfiniTime
software with off-site Clients](ovr_SoftwareOverview.md#so6_InfiniTime_7.0_Server_with_Offsite_Clients).

Refer to the [On-Site
Client section for accessing the InfiniTime
software with on-site Clients.](ovr_SoftwareOverview.md#so5_InfiniTime_7.0_Server_with_On-Site_Clients)

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

![](/img/image-404.png)

InfiniTime includes four
separate modules, each intended for different purposes as outlined below.
The Client Shortcuts Folder, as created on the Desktop of the InfiniTime Server and distributed
to client machines by the InfiniTime
Administrator, includes a shortcut to each module.

In the Manager
Module you canâ¦

* View employee information
* View and edit employee activity
* Run reports
* Schedule setup
* Access Escort Windows
* In & Out Board Access
* Most of the users time spent with the application will be in the
  manager module.
* Basically all administrative tasks such as adjusting employee schedules,
  editing timecards, and printing reports can be performed within the
  manager module.

![](/img/image-404.png)

In the Employee
Moduleâ¦

* Employees can view a history of their timecard information back
  to when they started using the system.
* Employees can view current schedule information.
* Employees can Run Reports designated for use within the employee
  module by software Administrators.
* Send messages to their supervisor in the form of:

+ Comments
+ Requests for Schedule Change
+ Requests for Vacation / Time Off

* Employees can Clock In and Out
* Employees can view the In & Out Board
* Self Service:

+ Even if your organization chooses not to use the employee module
  for punching in and out it still may be useful to allow employees
  to view and print their schedule and access a history of their
  time in the system. Use of the Employee Module for self service
  purposes can help eliminate routine and / or non business critical
  interruptions to Payroll Staff and / or Employee Supervisors.

![](/img/image-404.png)

In the Escort
Module you canâ¦

* Identify tasks that an employee performs on a regular basis within
  InfiniTime and place
  a button corresponding to only those tasks on a window.
* Serves as a Customized Portal to the InfiniTime
  Application
* Layout is completely user customizable with the ability to add
  labels, links, and images.
* Very useful for employees who are not highly computer literate
  or who might be overwhelmed by the number of features in the manager
  module..
* Escort users donât have to learn the entire application â only
  the areas they use on a regular basis. IE: You want to run a report.
  With escort the user only has to click on a single button where in
  the manager module they would have to Open the Report Library, Find
  the Report they want, Configure Report Settings, and finally review
  the results.

![](/img/image-404.png)

In the Punch
Module you canâ¦

* The Punch Module is In essence a stripped down version of the employee
  module.
* Provides a basic software time clock interface.
* Allows employees to punch in or out as necessary.
* Can be used by employees who are offsite but have access to a computer
  and the internet (Software must be published)
* Can be used to collect Employee Punches in place of hardware units
  such as the Scout / Zephyr ect. for both Local and Remote Users.

![](/img/image-404.png)

InfiniTime
FTP Sites

The InfiniTime
Installshield Wizard also creates two FTP Sites which can be used to access
files used for importing data into the InfiniTime
Software and / or created by the InfiniTime
Software as output. Shortcuts to the FTP Input and FTP Output FTP Sites
are created only on the desktop of the InfiniTime
Server and may or may not be distributed to client machines by the InfiniTime Software Administrator
depending on security concerns.

FTP
Inputâ¦

* Files
  used with import utilities within the InfiniTime
  application are automatically copied to this location.
* It
  is not necessary to copy files for import to this location ahead of
  time.
* Files
  within this directory that have import templates associated with them
  should not be renamed or have the column headers altered.

TECHNICAL NOTE: This folder is created with full
control for Authenticated Users. NTFS File Permissions can be altered
on the InfiniTime Server
as desired to permit or deny file access.

FTP
Outputâ¦

* Files
  created by InfiniTime
  Export and Payroll Export utilities are created in this directory
  and can be accessed using the FTP Output shortcut from any client
  machine with the appropriate permissions to the folder.

TECHNICAL NOTE: This folder is created with full
control for Authenticated Users. NTFS File Permissions can be altered
as desired on the InfiniTime
Server to permit or deny file access.

### Basic Software Settings and User Interface Review - Introduction

InfiniTime is a [Web Application](void(0);) unlike any other. In contrast with most
browser applications InfiniTime
was developed as a multitasking application and is not page loaded. As
a multitasking application InfiniTime
allows users to perform several tasks at the same time, eliminating the
need to close what you are doing, and open another browser to perform
another task. Such [multitasking](void(0);) features that are normally
only available in a Windows application. This unique browser environment
exclusive to web Time and Attendance products from Inception Technologies
provides a high level of productivity. InfiniTime
securely tracks, calculates and reports employee work hours using the
personal computer which eliminates the need to track employee attendance
manually. The system collects data "Real Time", providing accurate
reports which can even be emailed directly to multiple recipients automatically
at scheduled intervals. Traditional manual time sheet or time card calculations
are unnecessary because the system automatically calculates regular hours,
overtime, vacation time, sick time, and holidays.  Local printer
usage and full use of the software through a single browser window are
two of the main features that separate InfiniTime
from other web applications.

### Logging Into InfiniTime

A user wishing to access the InfiniTime
software from a client machine must know the InfiniTime
web address as detailed above. Shortcuts, located in the Client Shortcuts
Folder on the Desktop, provide access the InfiniTime
software. Double click the correct shortcut to access the desired module.

![](/img/image-404.png)

### InfiniTime Login Window

![](/img/image-404.png)

User Name
- The User Name is the ID used to access the software.  This ID is
given to the user by the administrator along with the User Password.

Password
- The User Password is the Password used to access the software.  This
Password is given to the user by the administrator along with the User
ID.

Ok Button
- The OK Button will validate the User Name and Password to log into the
software.

Cancel Button
- The Cancel Button will not save the changes made to a record and/or
exit out of the screen that you are currently in.

Change Password
- Prompts the user to [change
their password.](Security/Security_Overview.md#sec05_Ability_to_Change_Passwords_Upon_Login)

Users accessing any module of the software for the first time may enter
the default username and password into the login window as shown below.
The password will not be displayed in clear text as it is typed. The default
login, as provided below, may be used to login to any of the InfiniTime Modules.

![](/img/image-404.png)

User Name: SYSTEMAD      Password:
PASSWORD

Note: The default login is considered common knowledge among InfiniTime customers. The default
login should be altered in order to protect sensitive information within
InfiniTime. Refer to the
[Employee Setup](../QSG_Setup_Emp.md) section of the Setup
Quick Start Guide for more information.

### Manager Module Toolbar Buttons & Menu

InfiniTime includes a
menu and a main toolbar which provide access to all windows and forms
used to perform the initial InfiniTime
configuration as well as daily tasks.  A brief overview of each button
on the main toolbar is provided below.

![](/img/image-404.png)

### InfiniTimeMain Toolbar

The Main Toolbar includes buttons for access to the most commonly used
items, such as Employee Profiles, the Company Timecard Table, the Schedule
GANNT Chart, Reports, and Payroll Export. Items on the main toolbar are
generally used during initial setup as well as on a daily or weekly basis
by InfiniTime Software
Administrators and End users.

![](/img/image-404.png)

Company Button Introduction

![](/img/image-404.png)

The Company Button opens the Company Update Form which displays a general
overview of the InfiniTime
configuration. Items such as policies, company wide software settings,
and exceptions can be viewed by using the Company Button. InfiniTime uses two methods to organize
buttons, fields, and objects on Forms throughout the software. Tabs, as
shown below, can be used to view different details on a single form.

![](/img/image-404.png)

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

![](/img/image-404.png)

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

![](/img/image-404.png)

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

![](/img/image-404.png)

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
| mm/dd/yyyy |  |
| dd/mm/yyyy |  |
| yyyy/mm/dd |  |

System Time Format

Sets the Time Format
used throughout the InfiniTime
Application. Supported formats are listed below with examples.

| Time Format | Appearance |
| hh:mm tt |  |
| HH:mm |  |
| hh:mm |  |

System Window Skin

Sets the window design
used throughout the InfiniTime
Application. Supported skins are listed below with examples.

| Skin Name | Appearance |
| Vista |  |
| Black |  |
| Default |  |
| Forest |  |
| Hay |  |
| Office 2007 |  |
| Outlook |  |
| Simple |  |
| Sunset |  |
| Telerik |  |
| Web20 |  |
| WebBlue |  |

Recalculate Button

![](/img/image-404.png) - This feature allows the user to recalculate
timecard activity *for
the whole company*.  A recalculate should be performed after
making any changes to the policies, or after inserting, changing, or deleting
Holiday Dates. For example, if you should decided to enable rounding for
punches to the nearest quarter hour this will effect employee hour totals.

### Policies Tab - Introduction

![](/img/image-404.png)

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

![](/img/image-404.png)

The Exceptions Tab of the Company Update Form displays a list of all
company wide exceptions. Exceptions are conditions that can be tracked
by InfiniTime. It is important
to note that most exceptions require some configuration. When an employee
meets a condition for a tracked exception  they will be flagged with
the corresponding exception as appropriate. Initially, it is important
to understand the following concepts regarding InfiniTime
Exceptions:

* Exceptions can be configured in two ways:

+ Company Wide Exceptions - Company Wide Exceptions are tracked
  for all employees. Company Wide Exceptions can be configured from
  the Exception Types Tab of the Company Update Form or from the
  Exception Type Table: Company - Setup - Exception Types on the
  Main Toolbar.
+ Policy Specific Exceptions - Policy Specific Exceptions are
  tracked only for employees assigned to the respective policy.
  Policy Specific Exceptions can be configured in the Exceptions
  Section on the Policy Update Form which can be accessed via: Company
  - Setup - Policies on the Main Toolbar.

* InfiniTime
  offers multiple exceptions for detailed employee performance tracking.
  Schedules are required for most exceptions. For example, it is simply
  not possible for InfiniTime
  to determine if an employee is late without a schedule defining when
  the employee is expected to report to work..

* Two exceptions which can be tracked without the use of schedules
  are:

+ Missed Punch
+ Overtime

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

![](/img/image-404.png)

The Shifts Tab of the Policy Update Form displays a list of all Shifts
configured in the software. Shifts are one of the several scheduling options
available within InfiniTime
and are one of the most flexible scheduling methods. Initially, it is
important to understand the following concepts regarding Scheduling and
InfiniTime Shifts:

* Scheduling provides the ability to track additional exceptions
  such as tardy, late departure, early departure, early arrival ect.
  If schedules are not configured for employees these exceptions will
  never trigger.
* Shifts can also be used to configure shift differentials where
  employees receive an additional amount or percentage per hour while
  working within a specific time window.
* Additional information regarding configuring employee schedules
  can be found in the [Schedule
  Configuration section](Scheduling/Scheduling.md#sch01_What_do_I_want_to_accomplish_by_using_schedules_) of this document.

### Departments Tab - Introduction

![](/img/image-404.png)

The Departments Tab of the Policy Update Form displays a list of all
Departments configured in the software. Departments are used to separate
employee hours performed under different disciplines and / or types of
activity. Employees can punch into and out of departments in order to
track hours worked under separate departments such as Programming, Technical
Support, or Shipping or separate tasks such as Welding, Painting, or Finish
Work. Initially, it is important to understand the following concepts
regarding InfiniTime Departments
and Job Costing:

* InfiniTime includes
  four default departments as shown in the image above. If desired these
  departments can be removed. It should be noted that InfiniTime will only permit a department
  to be deleted if the department 1.)  Is not assigned to any employees.
  2.) Is not assigned to any timecard records.
* The default department is highlighted blue in the department table.
  When a new employee is inserted they are automatically assigned the
  default department.
* There is no limit to the number of departments that can be inserted
  into the software.
* Job Costing permits customers to track employee hours under various
  levels. Job costing is generally utilized in organizations where employee
  labor costs are of special interest when compared to the cost of finished
  goods such as manufacturing related organizations or where hours are
  billable to clients. An example Job Costing Configuration, using only
  InfiniTime Departments
  is shown below for a Construction Company. Additional details on job
  costing and configuration can be found in the [Job
  Costing Section](Configuration/Product_Configuration.md#cnf01_Job_Costing_Introduction) of this document.

| Department | Job | Task |
| Construction | Philly Mae Pizzeria | Framing |

When using job costing it is important to
identify the lowest level. In the above example Task is the lowest level.
To perform job costing using only Departments within InfiniTime
for ABC Construction Company, one department would be required for each
distinct Department, Job, and Task combination.. Department numbers can
be broken into sections with a specific number of digits for each level
in order to represent all departments, jobs, and tasks in a clear fashion.
The employee can then punch in and out of tasks using the department number.
Care must be taken when designing the numbering scheme in order to avoid
limiting the possible combinations and providing for future growth. An
example is shown below.

| InfiniTime Department Name | Department Number |
| Construction | Philly Mae Pizzeria | Framing | 1010000101 |
| Construction | Philly Mae Pizzeria | Drywall | 1010000102 |
| Electrical | Philly Mae Pizzeria | Wiring | 2010000210 |
| Electrical | Philly Mae Pizzeria | Engineering | 2010000211 |

Technical Note: The Job Costing Scenario above
uses only 1 Job Costing Level (Departments) within InfiniTime.
InfiniTime supports up
to three Job Costing Levels. The scenario above could also be handled
by configuring Departments, Jobs, and Tasks within the InfiniTime Software. One Department
within InfiniTime would
need be configured for each Department tracked by ABC Construction Company.
One Job would need be configured within InfiniTime
for each Client / Work Order serviced by ABC Construction. One Task would
need to be configured for each low level task performed by ABC Construction
employees. Refer to the Job Costing Section of this document for additional
details. The exact configuration required for a given organization depends
upon the requirements of the customer's Payroll Application for importing
Employee Hours and Earnings.

### Department Update Form - Introduction

![](/img/image-404.png)

The Department Update Form is used to create new Departments within
the InfiniTime Software
and can be accessed from the Departments Tab of the Company Update Form
by clicking on Insert or by selecting an existing department and clicking
on change. Initially, it is important to understand the following concepts
relating to Department Configuration. Keep these in mind when preparing
a list of your organization's departments for use during software configuration.

* The Department Name and Department Number are unique fields. Multiple
  departments cannot share the same department name or number.
* Department Cost Center - The cost center is used as a payroll identifier,
  providing the ability to match departments within InfiniTime to Hours
  Categories such as Tasks, Jobs, Classes, and/or Activities within
  a 3rd Party Payroll Application. Departments are generally identified
  by either a General Ledger Account number or an Alphanumeric Code
  within a payroll application. The Department Cost Center must be configured
  for customers who wish to track how employee hours are distributed
  between departments in their payroll application.
* The Default Schedule Tab of the Department Update Form is one
  method for defining employee schedules. Department schedules effect
  all employees assigned to the specific department. This scheduling
  method is most useful if the majority of employees within a department
  work the same schedule. Additional information can be found within
  [the Scheduling Section](Scheduling/Scheduling.md#sch05_Scheduling_By_Department)
  of this document.
* The Premium Pay Tab of
  the Department Update Form can be used to configure a specific wage
  for different Hours Types (IE: Regular Hours, Overtime Hours, etc.)
  worked in the respective Department. Additional information can be
  found within [the Pay Premiums
  Section](Configuration/Product_Configuration.md#pp01_Pay_Premiums_Introduction) of this document.
* The Hours Mapping Tab of the Department Update Form can be used
  to direct specific hours types worked in the respective Department
  to a different Hours Type. This feature is often utilized for Payroll
  Export purposes to separate hours that are paid at different rates.
  Additional information can be found within [the
  Hours Mapping Section](Configuration/Product_Configuration.md#hm1_Hours_Mapping) of this Document.

### Employees Tab Introduction

![](/img/image-404.png)

Displays a list of all employees in the software. Employee Profiles,
related settings, and configuration are detailed below in the [Employee Profiles and Related
Settings Section.](ovr_SoftwareOverview.md#so153_Employee_Profiles_and_Related_Settings)

### Other Activity Tab Introduction

![](/img/image-404.png)

Displays a list of all Hours and Earning Types outside of regular and
overtime hours. There is no limit to the number of other activity types
that can be configured. Most customers will need to one or more Other
Activity Types for paid leave hours such as Jury Duty, Bereavement Pay,
etc. Additional details regarding Other Activity Types can be found in
the [Other Activity Configuration
Section](Configuration/Product_Configuration.md#ota01_Other_Activity_Types) of this document.

### Valid IP Tab Introduction

![](/img/image-404.png)

The Valid IP Tab of the Company Update form is used to define Company
Valid IP Addresses. Additional details regarding Company Valid IP Addresses
can be found in the [Company
Valid IP Addresses](Security/Security_Overview.md#sec23_Valid_IP_Addresses_-_Overview) section of this document.

### Department Button

![](/img/image-404.png)

The Department Button opens the Department Table which displays the
same information as the Departments Tab of the Company Update Form. Additional
details on job costing and InfiniTime
Departments configuration can be found in the [Job
Costing Section of this document.](Configuration/Product_Configuration.md#cnf01_Job_Costing_Introduction)

![](/img/image-404.png)

### Employee Button

![](/img/image-404.png)

The Employee Button opens the Employee Table which displays a list of
all employees in the software similar to the employee list on the company
update form. Employee Profiles, related settings, and configuration are
detailed below in the [Employee
Profiles and Related Settings Section.](ovr_SoftwareOverview.md#so153_Employee_Profiles_and_Related_Settings)

### Timecards Button

![](/img/image-404.png)

The Timecards Button opens the company timecard table which displays
a list of all employees in the software on the upper portion of the window
and their timecard activity for a specified date range on the lower portion.
The Company Timecard Table is best suited for editing timecards and is
intended for use when reviewing timecards for multiple employees. Additional
Details on use of the Company Timecard Table and Editing Employee Timecards
can be found in the [Timecard
Editing Section](TimecardEditing/TimecardEditing.md#tim01_Timecard_Editing_Overview) of this document.

### Schedule Button

![](/img/image-404.png)

The Schedule button displays effective employee schedules in an easy
to read GANTT chart format. The GANNT Chart is specifically intended for
making temporary day by day adjustments to employee schedules. Additional
details on Employee Scheduling and use of the GANNT Chart can be found
in [the Scheduling Section](Scheduling/Scheduling.md#sch18_Employee_Schedule_Window_-_Introduction_)
of this document.

### In & Out Button

![](/img/image-404.png)

The In & Out Button displays the In & Out Board which lists
all employees in the software and their current in / out status. A green
check mark indicates the employee is clocked in while a red x indicates
the employee is punched out.

### Report Library Button

![](/img/image-404.png)

The Report button displays the Report Library which lists all of the
reports included with InfiniTime
broken down by major categories such as Timecard Reports, Payroll Reports,
Management Reports ect. Additional details on available reports and use
of the Report Library can be found in the [Reports
Section](Reports/Reports.md#rpt01_InfiniTime_Reports_-_Introduction) of this document.

### Payroll Export Button

![](/img/image-404.png)

The Payroll Export button opens the Payroll Export Table which lists
all Payroll Export Definitions currently defined within InfiniTime. Payroll Export provides
the ability to export timecard information in a format compatible with
various 3rd Party Payroll Applications. Additional Details on the use
and configuration of Payroll Export can be found in the [Payroll
Export Section](PayrollExport/Payroll_Export.md#pxh2_Introduction) of this document.

### Escort Button

![](/img/image-404.png)

The Escort Button opens the Escort Window assigned to the employee that
is currently logged in. If the Logged In User does not have an Escort
Window assigned a warning will be displayed as shown below. Additional
Details regarding design and use of Escort Windows can be found in[the Escort Section](Escort/Escort_Overview.md#esc01_Escort_Overview) of this document.

![](/img/image-404.png)

Exit
Button

![](/img/image-404.png)

The Exit Button will
close the InfiniTime Manager
Module.

Help
Button

![](/img/image-404.png)

The Help Button will
display the Table of Contents of the InfiniTime
Electronic Help Documentation.

### InfiniTime Manager Module Menu

InfiniTime includes a
menu and a main toolbar which provide access to all windows and forms
used to perform the initial InfiniTime
configuration as well as daily tasks.  A brief overview of each option
on the Menu is provided below.

![](/img/image-404.png)

### File Menu

![](/img/image-404.png)

The File Menu provides access to:

Escort
- Opens the Escort Window assigned to the currently logged in user.
If the logged in user does not have an escort window assigned a warning
will be displayed. Additional details on Escort Configuration and Usage
can be found in the [Escort
section](Escort/Escort_Overview.md#esc01_Escort_Overview) of this document.

In
and Out Board - Opens the In & Out Board which lists all
employees in the software and their current in / out status.

Backup
/ Restore - Opens the Backup / Restore Table which can be used
to create and restore backups of the InfiniTime
Database and configure options related to automatic backup of the InfiniTime Database. Additional details
on Backup / Restore Configuration and Usage can be found in the [Backup / Restore section](ovr_SoftwareAdministration.md#Backup_Restore_Introduction)
this document.

Exit
- Closes the InfiniTime
Manager Module.

### Company Menu

![](/img/image-404.png)

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

### Lookups Menu Introduction

![](/img/image-404.png)

The Lookups Menu is used primarily during initial configuration, though
some companies may find it necessary to fine tune configuration settings
during the first one to two payroll periods after Go Live with the InfiniTime Time & Attendance Software
or when Internal Human Resources and Time & Attendances practices
change.

### Lookups - Calculations Setup Introduction

The Lookups - Calculations Setup Menu provides access to all areas of
the InfiniTime Software
which directly impact how Employee Hours and Earnings are awarded or calculated.

![](/img/image-404.png)

The Lookups - Calculations Setup Menu provides access to:

Accrual
Types - Opens the Accrual Types
Table which displays a list of all Accrual Types configured in InfiniTime. Accrual
Types are used to track various types of Paid or Unpaid Leave such as
Sick Time, Vacation Time, and / or Personal Time for employees. Additional
details regarding configuring and tracking Employee Accrual Totals can
be found in the [Employee
Accruals Configuration Section](Configuration/Accrual_Configuration.md#acc01_Employee_Accruals_Introduction) of this document.

Exception
Types - Opens the Exception Types
Table which can be used to define Company Wide Exceptions. It is important
to note that Company Wide Exceptions are tracked for all employees. Additional
Details on available Exceptions and Exception related functionality can
be found in the [Exception Configuration
Section](Policies/Policy_Overview.md#pol26_Exceptions) of this document.

Holiday
Schedule Types - Opens the Holiday
Schedule Type Table which displays a list of all Holiday Types configured
in InfiniTime. Holiday
Types are used to define specific holiday dates for which employees are
eligible for Holiday Pay. Holiday Schedule Types are also used in conjunction
with Employee Policy settings to define specific benefits for employees
who work on holiday dates such as time and a half (1.5x Employee Base
Rate) or double time (2.x Employee Base Rate). Additional Details on use
and configuration of Holiday Types can be found in the [Holidays
Configuration Section](Configuration/Product_Configuration.md#hol01_Holiday_Types_Configuration_-_Introduction) of this document.

Job
Costing Lookups:

Activity Jobs -
Opens the Activity Job Table which displays a list of all Activity Jobs
configured in InfiniTime.
Activity Jobs serve as the second Job Costing Level within InfiniTime and are used to categorize
employee hours. Additional information on use and configuration of Job
Costing can be found in the [Job Costing Section](Configuration/Product_Configuration.md#cnf07_Configuring_Jobs) of this document.

Activity Tasks - Opens
the Activity Job Table which displays a list of all Activity Jobs configured
in InfiniTime. Activity
Jobs serve as the second Job Costing Level within InfiniTime
and are used to categorize employee hours. Additional information on use
and configuration of Job Costing can be found in the [Job
Costing Section](Configuration/Product_Configuration.md#cnf08_Configuring_Tasks) of this document.

NOTE: It is not possible to create Activity Tasks
until one or more Activity Jobs have been created.

Other
Activity Types - Opens the Other
Activity Types Table which displays
a list of all Hours and Earning Types outside of regular and overtime
hours. There is no limit to the number of other activity types that can
be configured. Most customers will need to one or more Other Activity
Types for paid leave hours such as Jury Duty, Bereavement Pay, etc. Additional
details regarding Other Activity Types can be found in the [Other Activity Configuration
Section](Configuration/Product_Configuration.md#ota01_Other_Activity_Types) of this document.

Policies
- Opens the Policy Table which
displays a list of all policies configured in the software. Additional
details regarding configuring policies are provided in the [Policy Configuration Section](Policies/Policy_Overview.md#pol1_Policy_Overview)
of this document.

### Lookups - Employee Setup Introduction

The Lookups - Employee Setup Menu provides access to:

![](/img/image-404.png)

Cellular
Provider - Opens the Cell Phone
Providers Table. Cell Phone Providers are utilized to define the short
message service (SMS) gateway for Cellular Providers which is required
for InfiniTime to send
text message notifications to employees and / or supervisors when exceptions
occur. The Cellular Providers table is populated for major cellular carriers
by default. InfiniTime
Software Administrators may add additional Cellular Carriers as needed.
Additional information regarding Cell Phone Providers and Exception Notifications
(IE: Sending Text Message Alerts to Employees or Supervisors when exceptions
occur) can be found in the [Exception
Notifications Section](Policies/Policy_Overview.md#pol33_Exception_Type_Update_Form_-_Notifications_Tab) of
this document.

Departments
- Opens the Department Table which
displays the same information as the Departments Tab of the Company Update
Form. Additional details on job costing and InfiniTime
Departments configuration can be found in the [Job Costing Section](Configuration/Product_Configuration.md#cnf06_Configuring_Departments) of
this document.

Escort
Settings - Opens the Escort Settings Description
Table which displays all Escort Windows
configured within InfiniTime.
Escort
makes it possible to design a customized portal to the InfiniTime Application. Nearly every
button, feature, and report within the InfiniTime
Application can be placed on an escort window. Escort is recommended for
use by any company where multiple supervisors will access the InfiniTime Application. Additional
details on use and configuration of Escort Windows can be found in the
[Escort
Configuration Section](Escort/Escort_Overview.md#esc01_Escort_Overview) of this document.

Groups
- Opens the Group Table which displays
all Group Levels and Group Descriptions configured within InfiniTime. Group
Levels and Group Descriptions can be used to organize employees into organizational
units (IE: All employees at the Phoenix, AZ Location. All Employees employed
by Company A, All Employees employed by Company B etc.) to be used for
filtering purposes throughout the InfiniTime
Software. Additional details regarding use and configuration of Employee
Groups can be found in the [Groups
Configuration Section](Configuration/Product_Configuration.md#gr01_Groups_Introduction) of this document.

Human
Resources Lookups:

Human Resources Lookups are utilized to define available options for
Human Resource related fields and settings referenced from within Employee
Profiles.

![](/img/image-404.png)

Benefit Plan Costs - Opens
the Benefit Plan Cost Table which displays all Benefit Plan Cost values
configured within InfiniTime.
Benefit Plan Cost values represent the employer's cost of employee benefits
and can be assigned to individual Benefit Plan Types on an employee by
employee basis  for tracking purposes. Additional information regarding
use and configuration of Employee Benefits can be found in the [Employee Profiles and Related
Settings Section](ovr_SoftwareOverview.md#so153_Employee_Profiles_and_Related_Settings) of this
document.

Benefit Plan Types - Opens
the Benefit Plan Type Table which displays all Benefit Plan Types configured
within InfiniTime. Benefit
Plan Types represent different benefits offered by the employer. Related
details such as Benefit Plan Cost, Enrollment Date, etc can then be defined
on an employee by employee basis  for tracking purposes. Additional
information regarding use and configuration of Employee Benefits can be
found in the [Employee Profiles
and Related Settings Section](ovr_SoftwareOverview.md#so153_Employee_Profiles_and_Related_Settings)
of this document.

Equal Employment Opportunity
Types - Opens the Equal Employment
Opportunity Table which lists all Equal Employment Opportunity Classifications
configured within InfiniTime.
Equal Employment Opportunity Classifications
are used to assign employees to specific Classifications in according
with the rules and guidelines set forth by the United States Equal Employment
Opportunity Commission and can be used for tracking purposes to show employee
distribution across various Equal Employment Opportunity Classifications.

Employment Status Types -
Opens the Employment Status Types Table
which lists all Employment Status Types configured within InfiniTime.
Employment Status Types are used to define employment status for individual
employees in accordance with the rules and guidelines set forth by the
United States Equal Employment Opportunity Commission and can be used
for tracking purposes to show employee distribution across various Employment
Status types. Additional information
regarding use and configuration of Employee HR Related settings can be
found in the [Employee Profiles
and Related Settings Section](ovr_SoftwareOverview.md#so153_Employee_Profiles_and_Related_Settings)
of this document.

Termination Reasons - Opens
the Termination Reason Table which lists all Employee Termination Reasons
configured within InfiniTime.
InfiniTime prompts the
user for a termination reason when employees are terminated. For this
reason, Employee Termination Reasons must be configured in all production
installations of InfiniTime.
Additional information regarding use
and configuration of Employee HR Related settings can be found in the
[Employee Profiles and Related
Settings Section](ovr_SoftwareOverview.md#so153_Employee_Profiles_and_Related_Settings) of this
document.

Worker's Comp. Categories
- Opens the Worker Compensation Code
Table which lists all Worker's Compensation Code Categories configured
within InfiniTime. Workers
Comp. Categories are used to assign employees to specific workplace exposure
codes in accordance with the rules and regulations set forth by the National
Council of Compensation Insurance (NCCI) and can be used for tracking
purposes to show employee distribution across various workplace exposure
codes.

Important
Date Names - Opens the Important
Date Table which lists all Important Date Names configured within InfiniTime. Important Dates allow
the InfiniTime Software
Administrator to define specific events which are of mission critical
importance for individual employes. (IE: CPR Certification Expiration
Date for a Pool Management Company that hires lifeguards.) Before Important
Dates can be defined for individual employees Important Date Names must
first be defined. Additional Details regarding use and Configuration of
Important Dates can be found in the [Employee Profiles and Related
Settings Section](ovr_SoftwareOverview.md#so153_Employee_Profiles_and_Related_Settings) of this
document.

Job
Costing Lookups:

Job Costing Lookups are used to define Activity Jobs and Activity Tasks
for Job Costing Purposes.

![](/img/image-404.png)

Activity
Jobs - Opens the Activity Job Table
which displays a list of all Activity Jobs configured in InfiniTime. Activity Jobs serve as the second Job Costing Level within
InfiniTime and are used
to categorize employee hours. Additional information on use and configuration
of Job Costing can be found in the [Job Costing Section](Configuration/Product_Configuration.md#cnf07_Configuring_Jobs) of this document.

Activity
Tasks - Opens the Activity Job
Table which displays a list of all Activity Jobs configured in InfiniTime. Activity Jobs serve as
the second Job Costing Level within InfiniTime
and are used to categorize employee hours. Additional information on use
and configuration of Job Costing can be found in the [Job
Costing Section](Configuration/Product_Configuration.md#cnf08_Configuring_Tasks) of this document.

Payroll
Information Lookups:

Payroll Information Lookups are used to define Payroll Related Human
Resource settings referenced within Employee Profiles.

![](/img/image-404.png)

Local Taxing Authority - Opens the Local Tax Authority Table which
lists all entities to which the employer is responsible for paying Local
Employment Taxes. Local Tax Entities can then be assigned to specific
employees for tracking purposes. Additional information about Employee
Specific Payroll and HR Related Settings can be found in the [Employee Profiles and Related
Settings Section](ovr_SoftwareOverview.md#so153_Employee_Profiles_and_Related_Settings) of this
document.

State Taxing Authority -
Opens the State Tax Authority Table which lists all entities to which
the employer is responsible for paying State Employment Taxes. State Tax
Entities can then be assigned to specific employees for tracking purposes.
Additional information about Employee Specific Payroll and HR Related
Settings can be found in the [Employee
Profiles and Related Settings Section](ovr_SoftwareOverview.md#so153_Employee_Profiles_and_Related_Settings) of this document.

Security Roles -
Opens the Security Role Table which displays all Security Roles configured
within InfiniTime. Security
Roles are used to control access to individual windows and buttons within
the InfiniTime Software
for specific groups of users or even specific individuals. As such, Security
Roles are an integral part of the initial InfiniTime
Configuration and should be reviewed by all InfiniTime
Software Administrators. Details on the default Security Roles included
within InfiniTime as well
as how to customize security roles within InfiniTime
to meet your organization's unique requirements can be found in the [Security
Section](Security/Security_Overview.md#sec07_Security_Roles) of this document.

User Defined Fields - Opens
the User Defined Fields Table which lists all User Defined Fields Table
configured within InfiniTime.
User Defined Fields allow the InfiniTime
Software Administrator to track additional employee information which
is not included in the InfiniTime
Software by default such as industry specific details such as drivers
license numbers and or certifications required by law. Additional Details
regarding use and Configuration of User Defined Fields can be found in
the [Employee
Profiles and Related Settings Section](../Employee_Setup/User_Defined_Fields.md)
of this document.

Reader Configuration - Opens the Reader Configuration Table
which lists all hardware devices that are connected to the InfiniTime software. Before InfiniTime can poll employee timecard
activity from a hardware device, the hardware device must be configured.
Detailed configuration and installation instructions are available for
each hardware device, by model name, in the Hardware Documentation section
of this document. General Information on use of the Reader Configuration
Table can be found in the [InfiniTime Administration - Reader
Configuration](ovr_SoftwareAdministration.md#ru1_Reader_Configuration_Table) section of this document.

Scheduling
Setup:

The Scheduling Setup Menu provides access to specific Scheduling Related
settings and configuration.

![](/img/image-404.png)

Availability - Opens
the Schedule Availability Table which displays a list of all Schedule
Availability Types configured within InfiniTime.
Schedule Availability Types are templates which reflect the normal hours
an employee is considered available
for work related duties and are intended for use by organizations with
dynamic scheduling environments such as restaurants where staffing requirements
are based on customer demand. Additional
information regarding use and configuration of employee schedules and
availability types can be found in [the
Schedule Configuration section of this document.](Scheduling/Scheduling.md#sch38_Employee_Availability___Benefits_and_Configuring)

Shifts
- Opens the Shifts Table which displays
a list of all Shifts configured in the software. Shifts are one of the
several scheduling options available within InfiniTime
and are one of the most flexible scheduling methods. Additional information
regarding configuring employee schedules can be found in [the
Schedule Configuration section of this document.](Scheduling/Scheduling.md#sch14_Configuring_Shifts_for_Scheduling_Purposes)

Skeletons
- Opens the Schedule Skeletons Table
which displays a list of all Schedule Skeletons configured within InfiniTime. Schedule Skeletons are
schedule snapshots for specific operating scenarios with different staffing
requirements for a given organization. For example, Friday nights at a
restaurant typically require a full staff where as morning shifts might
require only minimal staff. Skeletons make it possible to search for specific
employees according to their individual abilities as defined by Trained
Tasks in addition to their previously identified Availability Schedule,
or when they have indicated they are available to report to work. Additional information regarding use
and configuration of employee schedules and Skeletons can be found in [the Schedule
Configuration section of this document.](Scheduling/Scheduling.md#sch44_Schedule_Skeletons___Benefits_and_Configuring)

Trained
Tasks - Opens the Trained Tasks Table which displays a list
of all Trained Tasks configured within InfiniTime.
Trained Tasks allow the InfiniTime
Administrator to define specific job roles and functions which require
certain skill sets (IE: Cashier, Fry Cook, Hostess, etc.). One or more
trained tasks can then be assigned to individual employees to indicate
skill sets for which an employee has been trained. Trained Tasks are used
in conjunction with [Skeletons](Scheduling/Scheduling.md#sch44_Schedule_Skeletons___Benefits_and_Configuring)
and [Find
Available](Scheduling/Scheduling.md#sch24_Find_Available_) for employee scheduling purposes. Additional information
regarding use and configuration of employee schedules and Trained Tasks
can be found in [the Schedule
Configuration section of this document.](Scheduling/Scheduling.md#sch44_Schedule_Skeletons___Benefits_and_Configuring)

### Tools Menu - Introduction

The Tools Menu provides access to tools commonly used on a day to day
or weekly basis by InfiniTime
Software Administrators.

History
And Undo Tools:

The History and Undo Tools Menu provides access to History Tools for
Purge, Quick Punch, Quick Schedule, and Supervisor review. These tools
can be used to review and undo accidental or improper Purge, Quick Punch,
Quick Schedule, and Supervisor Review actions performed by end users.
 In this way, InfiniTime
Administrators can undo unintended alterations.

![](/img/image-404.png)

Purge History - Opens
the Purge History Table. The Purge History Table maintains a running list
of all purge actions that have been performed since database creation.
Additional Details on the use of Purge
can be found in the [Company
Timecard - Purge](TimecardEditing/TimecardEditing.md#tim05a_Purge) section of this document.

Quick Punch History - Opens
the Quick Punch History Table. The
Quick Punch History Table maintains a running list of all quick punch
actions that have been performed since database creation. 
Additional Details on the use of Quick
Punch can be found in the Company Timecard - Quick Punch section of this
document.

Quick Schedule History - Opens the Quick Schedule History Table.
The Quick Schedule History Table maintains
a running list of all quick schedule actions that have been performed
since database creation.

Supervisor Review History
- Opens the Supervisor Review History
Table. The Supervisor Review
History Table maintains a running list of all Supervisor Review actions
that have been performed since database creation.

Clock Tools:

The Clock Tools Menu provides access to tools related to polling employee
punches from hardware devices connected to the InfiniTime
Software, monitoring automated tasks performed by the InfiniTime
Housekeeping Service.

![](/img/image-404.png)

Polled Information - Opens
the Polled Information Table which maintains a running list of all employee
timecard punches polled from Hardware Devices and / or Software Modules
such as the InfiniTime
Employee Module or the InfiniTime
Punch Module. Additional Details
on use of the Polled Information Table can be found in the [InfiniTime
Administration - Clock Tools section](ovr_SoftwareAdministration.md#ct1_Polled_Information)
of this document.

System Monitor - Opens
the System Monitor Window which provides InfiniTime
Software Administrators with an overview of automated processes performed
by the InfiniTime Housekeeping
Service in addition to access to Hardware Device Configuration. Additional
Details on use of the System Monitor can be found in the [InfiniTime Administration
- Clock Tools](ovr_SoftwareAdministration.md#ct2_System_Monitor_Window) section of
this document.

Unassigned Punches - Opens
the Unassigned Punches Table.

Import
and Export:

The Import and Export Menu provides access to tools related to importing
or exporting employee and / or configuration data to or from the InfiniTime database. The Import Tool
is generally used only during initial configuration, though some companies
choose to configure automated imports in order to Sync InfiniTime with 3rd Party Accounting
or Payroll Software Suites. The Export Tool is generally used on an as
needed basis only in order to gather employee and / or configuration data
into a single comma delimited file for internal reporting purposes.

![](/img/image-404.png)

Export
- Opens the Export Definition table
which lists all Export Templates previously configured within InfiniTime. Additional
Details on the use and configuration of the Export Tool can be found in
the [InfiniTime
Administration
- Import & Export - Export](ovr_SoftwareAdministration.md#exp1_Export_Introduction)
section of this document.

Import
- Opens the Import Definition table
which lists all Import Templates previously configured within InfiniTime. Additional
Details on the use and configuration of the Export Tool can be found in
the [InfiniTime
Administration
- Import & Export - Import](ovr_SoftwareAdministration.md#imp1_Import_Introduction)
section of this document.

Payroll
Export - Opens the Payroll Export
Table which lists all Payroll Export Definitions currently defined within
InfiniTime. Payroll Export
provides the ability to export timecard information in a format compatible
with various 3rd Party Payroll Applications. Additional Details on the
use and configuration of Payroll Export can be found in the [Payroll
Export Section](PayrollExport/Payroll_Export.md#pxh2_Introduction) of this document.

Quick
Assign - Opens the Quick Assign History Table which maintains
a running list of all Quick Assign Actions performed since Database Creation.
Additionally, the Quick Assign History Table provides access to the Quick
Assign Tool which permits InfiniTime
Software Administrators to assign employee related settings for multiple
employees at once which makes it possible to significantly reduce man
hours required to perform the initial software configuration and / or
maintenance tasks when working with large numbers of employees. Additional
Details on the use of Quick Assign can be found in the [Configuration
- Quick Assign section](Configuration/Product_Configuration.md#qa01_Quick_Assign_Introduction) of this document.

### Report Library Menu

![](/img/image-404.png)

Report
Library -  Opens the Report
Library which lists all of the reports included with InfiniTime
broken down by major categories such as Timecard Reports, Payroll Reports,
Management Reports ect. Additional details on available reports and use
of the Report Library can be found in the [Reports
Section](Reports/Reports.md#rpt01_InfiniTime_Reports_-_Introduction) of this document.

### Help Menu

The Help Menu provides access to details regarding a given InfiniTime Installation such as Software
License Information, Licensed Employee Count, and Licensed Hardware Device
Count in addition to access to Electronic Help Documentation included
with the InfiniTime Time
& Attendance Software.

![](/img/image-404.png)

About
InfiniTime -
Opens the About InfiniTime
Window which displays contact information for the customer's Inception Technologies Dealer from
which the InfiniTime Software
was purchased in addition to contact information for Inception Technologies,
the developer of InfiniTime.
The About InfiniTime Window
also provides access to the Technical Information Window which displays
Software License information for the given InfiniTime
installation and access to Licensing related features. Additional details regarding InfiniTime's proprietary Software
Licensing System can be found in the [Software
Licensing Section](../Licensing_Introduction.md) of this
document.

Index
- Opens the InfiniTime
Electronic Help Documentation Index which includes all Help Topics listed
by content subject.

Search
- Opens the InfiniTime
Electronic Help Documentation Search Pane which can be used to search
the Electronic Help Documentation contents for specific key words or phrases.

Table
of Contents - Opens the InfiniTime
Electronic Help Documentation Table Of Contents which displays all help
topics within the Electronic Help Documentation System as organized by
Inception Technologies
representatives for flow and ease of use for specific types of users such
as InfiniTime Software
Administrators, Supervisors, or End Users.

### User Interface Overview

The InfiniTime User Interface
was designed with user friendly data entry and navigation in mind. Ease
of use features, as detailed below, are included to assist the user with
identifying and entering required information and navigating throughout
the InfiniTime application.
InfiniTime also includes
duplicate prevention functionality to alert users of duplicate values
in required fields such as the Employee Login ID which specifically require
unique values across all employees in the database. An overview of data
entry, navigation, and form completion related features included within
InfiniTime is provided
below.

### Data Entry & Navigation Assistance

Time
Selection Tool - The time selection tool, referred to as the
Time Picker, provides users with a graphical interface for entering time
into a field. The Time Picker can be used for any field where the timeclock
( ![](/img/image-404.png)) graphic is displayed. Drop down menus
are used on the Time Picker. When the arrow of a drop down menu is clicked
on, a list of the menu contents is displayed. Only one item in the list
can be selected at a time.

To use the Time Picker:

- Click on the timeclock graphic (![](/img/image-404.png) )

![](/img/image-404.png)

- Use the drop down menu to select the desired hour.
- Use the drop down menu to select the desired minute.
- Use the drop down menu to select the appropriate time of
  day.

![](/img/image-404.png)

- Clicking the Now button will set the drop down windows
  to the current system time.
- Clicking the Select button will enter the time chosen by
  the drop down menus into the form.
- Clicking cancel will close the Time Picker window and return
  to the form. Any information selected in the Time Picker will
  not be entered in the form.

Date
Selection Tool - The date selection tool, referred to as the
Date Picker, provides users with a graphical interface for entering a
date into a field. The Date Picker can be used for any field where the
calendar ( ![](/img/image-404.png)) graphic is displayed.
The calendar graphic is always displayed to the right of a corresponding
date field. Any information selected with the Date Picker will be entered
into this field.

To Use the Date Picker:

- Click on the calendar graphic. (![](/img/image-404.png) ) A
  calendar with the current month and day will be displayed.
  If the field corresponding to the Calendar Graphic is blank,
  then the current date will be highlighted in red on the calendar.
  Should a date be in the corresponding field already, then
  that date will be highlighted in red on the calendar.

![](/img/image-404.png)

- Use the drop down menu to select the desired month. The
  left and right arrows can also be used to move ahead or backward
  one month
- Use the drop down menu to select the desired year.

![](/img/image-404.png)

- Click on the desired day to make your final selection and
  enter the selected values into the date field.

### Date Field Navigation Shortcuts

As an alternative to the Date Picker, InfiniTime Date field entries may
also be altered with the use of keyboard shortcuts.

To use keyboard shortcuts to alter InfiniTime Date Fields:

* Click in the date field that you
  wish to alter. The field is yellow when it is active and ready for
  use with keyboard shortcuts.

Inactive Date Fields                        Upper
Date Field is Active

![](/img/image-404.png)                            ![](/img/image-404.png)

- Hit the key that corresponds
  to the action you wish to perform. Keyboard shortcuts are
  listed below.

| Date Field Keyboard Shortcut | Action |
| + | Adds one day to the date displayed in the Active Date Field |
| - | Subtracts one day from the date displayed in the Active Date Field |
| T or Home | Sets the Date in the Active Date Field to Today's Date |
| Page Up | Subtracts one month from the date displayed in the Active Date Field |
| Page Down | Adds one month to the date displayed in the Active Date Field |
| Shift + Home | Sets the Date in the Active Date Field to January 1st of the respective Year |
| Shift + End | Sets the Date in the Active Date Field to December 31st of the respective Year |

VCR
Buttons - VCR buttons can be found on nearly every table or
list in the InfiniTime
software. These buttons are used to move between pages and entries in
the list. VCR buttons are always displayed in a set of four.

![](/img/image-404.png)

| Description | Referred to As | Graphic |
| The first or left most button, moves to the first record or entry in the table. | âFirstâ VCR Button |  |
| The second button moves back a record or entry in the table. | âPreviousâ VCR Button |  |
| The third button moves forward a record or entry in the table. | âNextâ VCR Button |  |
| The last or right most button moves to the last record or entry in the table. | âLastâ VCR Button |  |

The VCR Search Filter allows the user to
enter a word, letter or phrase, and filter the records that can be accessed
with the VCR buttons accordingly.

*For Example*:
In a company with a few hundred employees advancing through the employees
one by one would not be practical. Typing Stephen into the search filter
and clicking on one of the VCR buttons will:

- Search
  through all employee records and fields for âStephenâ
- Employees that live on
  Stephen Lane, with the last name of Stephens, and the first
  name Stephen will be made available for display with the VCR
  buttons.
- The first record or closest
  match to the word in the search filter will be displayed first.
- Using the Next, Previous,
  First, and Last VCR buttons will move among the records available
  for display.

Using a letter or phrase in the search filter
functions similarly to a name or word. All records containing the letter
or phrase will be made available for display with the VCR buttons.

Magnify
Glass - The magnify glass is displayed to the right of every
form item that requires a selection from another table or list with the
InfiniTime software. For
example, when setting up employees, the default department must be selected.
Users have the option of typing the first few letters of a department
name into the field and allowing auto complete to enter the rest of the
department name or viewing the department table using the Magnify Glass.
The magnify glass can be used wherever the ![](/img/image-404.png) icon is
displayed.

To use the Magnify Glass:

- Click on the Magnify glass Icon.
- A list of available items will appear.
- Click on the desired item to select it.
- Click on the Select button.

For Example:

Using the Magnify Glass to select a default
department:

- Click on the Magnify Glass Icon to the right of the Default
  Department field.

![e](/img/image-404.png)

- A list of available departments
  will appear. Click on the desired department to select it.

![](/img/image-404.png)

- Click on the Select button.
- The selected department is
  entered into the default department field.

![](/img/image-404.png)

File Selection
Tool - InfiniTime allows
you select files for import from your local machine into the software.

![](/img/image-404.png)

From anywhere
in the software where it asks you for a file, like in the import tool,
or selecting a picture for the employee update form, you can select a
file by clicking in the browse button and selecting the correct file.
 it will make a copy of that file and place it in the INPUT directory
in the InfiniTime Server.

Example:

How to add
a picture to an employee's record

- On the employee
  update form click on ![](/img/image-404.png)
- Click on the Browse Button on the File Selection Window

![](/img/image-404.png)

- Browse
  to the Location on your PC with the file you wish to Import
  into InfiniTime

![](/img/image-404.png)

- Click
  on the file you wish to import to select it then click on
  Open.

![](/img/image-404.png)

* The
  full path of the previously selected file will be displayed in the
  File Selection Window. Click OK to import the file and save the image
  as part of the employee's profile.

### Form Completion Assistance

Auto
Complete - All fields within InfiniTime
which reference a separate table support the use of Auto Complete. Fields
which support auto complete are often referred to as lookups, because
these fields look up settings and details configured elsewhere within
InfiniTime. Auto complete
makes it possible for users to partially enter their desired value. InfiniTime will then automatically
complete the rest of the field based on information that has been entered.

Technical Note: If a value is entered in a required
field that does not match an item in the database InfiniTime
will automatically clear the field and prompt the user to enter a valid
value.

*EXAMPLE*:
If the System Administrator account were to be entered for the Supervisor,
typing the first letter of the last name (A) will show the entered information
(A) and automatically complete the rest of the field. Selected information
is added automatically by auto complete.

![](/img/image-404.png)

Only Lookup Fields which are displayed within
InfiniTime with the Lookup
Magnify Glass, as highlighted in red below, include the auto complete
feature.

![](/img/image-404.png)

Color
Coded Fields - InfiniTime
uses field coloring to assist users in data entry. Some fields are required,
while many are optional and can be filled out at a later date. The following
table contains information about field coloring.

| Color | Description |
| Yellow | *Active Cell*: If you click in a field the background turns yellow. This helps users identify which field they are working in. |
| Blue | *Required Field:* Any fields in blue must be filled out. Should you miss or skip over any blue fields the InfiniTime software will warn you and prompt you to fill it out properly. InfiniTime permits the Software Administrator to specify fields they wish to consider required throughout the software. This functionality allows the Software Administrator to strictly control and enforce accurate tracking of employee information. For more information refer to [Configuring Required Fields.](Security/Security_Overview.md#sec18_Required_Fields) |
| White | *Optional Field*: Any fields in white are optional and do not have to be filled out. The software can be used for basic time and attendance purposes without the entry of Optional Fields and values. If it doubt, refer to the Help Documentation for the respective section of the program. All fields and options within InfiniTime are documented with an explanation of how the option can be used within the InfiniTime Electronic Help System. |

User
Configurable Required Fields - InfiniTime
permits employees with the right to Edit Security to specify fields they
wish to consider required throughout the software. This functionality
allows InfiniTime Software
Administrators to strictly control and enforce accurate tracking of employee
information. For example, though the InfiniTime
Application does not require Employee Address Information, Phone Numbers,
or Emergency Contact Information to function, these fields can be configured
as required fields. Users responsible for entering employees would then
be required to fill out this information before InfiniTime
would allow the employee record to be added to the system. This is simply
an example of how configuring required fields can be used. Nearly every
optional field within the InfiniTime
Application can be set to required if desired by the user. Fields required
for the InfiniTime Application
to function are set to required by default and cannot be set to Optional
by the user.

Configuring Required Fields

* To set required
  fields for a window, open the window you wish to configure and click
  on the Security Key.

Note: You
must be logged in as a user with the right to Edit Security. Refer
to [Security
Roles](Security/Security_Overview.md#sec07_Security_Roles) for more
information on InfiniTime
Security Settings. For clarity purposes, the Employee Update Form will
be used as an example.

![](/img/image-404.png)

* The Form Security Table will be displayed.
  Click on the Required tab.

![](/img/image-404.png)

* Search for the
  field(s) you wish to set as required.

![](/img/image-404.png)

* Click on the drop
  down box for each desired field and set the Required Status to True.
  Click Close to save your changes.

![](/img/image-404.png)

* In this example,
  additional required fields were set for the Employee Update form.
  If a user attempts to add an employee without fill out out all required
  fields InfiniTime will
  prompt the user to complete any items they missed as shown below.

![](/img/image-404.png)

Field
Tool Tips - All update forms within
the InfiniTime Software,
such as the Employee Update Form used for adding employees, the Policy
Update Form used for adding policies, or the Department Update Form used
to update Departments include tool tips intended to prompt users to enter
appropriate data. To view a fields function and / or intended purpose,
simply hover the cursor over the field in question. A tool tip will be
displayed as shown below. Tool tips provide a short summary of expected
field content.

![](/img/image-404.png)

Duplicate
Prevention - Users should be aware that most tables within
the InfiniTime software
can not contain duplicates. Should the user attempt to enter a duplicate
record, such as two employees with the same Employee Login ID or two Group
Levels of the same name the software will warn the user and prompt for
a different entry. The duplicate entry will not be saved.

Additionally, InfiniTime's
Data Import Tool includes a full-featured duplicate checking scheme in
order to avoid issues that could result should duplicates be present in
the database. If duplicates are found during an import the software will
discard or replace existing records depending on settings chosen during
import. Detailed information regarding import duplicate checking can be
found in the Import section of this document.

### Customizable Table Display: InfiniTime Grid Controls

InfiniTime uses a grid
system to display information in an organized, structured, and standardized
fashion. Each table and list is presented in a similar layout with the
InfiniTime Grid as the
major build block. Use of a grid system helps keep information accessible
and orderly regardless of database size through the use of various features
such as the ability to filter items based on a search term.

The InfiniTime Grid is
fully customizable and can be tailored to meet user needs. Each window
stores a set of configuration settings allowing the user to customize
each window individually.

![](/img/image-404.png)

The image above, taken from the Employee Table, shows how Grid Controls
and a Search Field are displayed above the grid. Headings appear atop
each grid column to describe the information below. This document uses
the Employee Table as an example, though it should be noted that the grid
controls are displayed on every table where the grid is used.

Click on each control below for more information about its uses. Page
controls are gray when there are no available pages in that direction.
Once multiple pages are available the controls will become active and
turn blue.

Technical Note: Some grid buttons may not be available
depending on your browser. Firefox for example does not support clipboard
access or printing from InfiniTime.

![](/img/image-404.png)

First Page  ![](/img/image-404.png).gif)

Updates
the grid with the first page of records. Page 1 will be displayed in the
current page drop down box.

Previous Page ![](/img/image-404.png).gif)

Updates the grid with records from the
previous page and decreases the page number in the current page drop down
box by one.

Current Page ![](/img/image-404.png).gif)

Provides a drop down box that can be used
to select the page you wish to view. Also displays the current page. Viewing
a different page can be accomplished by clicking on the drop down tab
and selecting the individual page you wish to view.

The total amount of pages is displayed
on the right. This value is updated automatically as additional records
are added to the database. When the number of records exceeds a preset
record per page limit then a new page is created. The number of records
displayed per page can be configured in the Grid Configuration Window.

Next Page
![](/img/image-404.png).gif)

Updates the grid with records from the
next page and increases the page number in the current page drop down
box by one.

Last Page ![](/img/image-404.png).gif)

Updates the grid with records from the
last page and displays the final page number in the current page drop
down box.

Total Rows ![](/img/image-404.png).gif)

Displays the total number of rows, or records,
in the grid. This number is updated automatically as records are added
and removed.

Save Grid
Results ![](/img/image-404.png).gif)

Users have the option of saving all records
displayed in the InfiniTime
Grid in any one of five formats. To save the grid, select your preferred
format from the drop down box and click the Save Grid Results icon. Specific
instructions are provided by format below. Should the grid contain multiple
pages of information records on each page will append to the end of the
document after those from the previous pages. The end result is a single
document with all records in the grid.

Save
Grid Results As - HTML

Grid Results are immediately saved in an
HTML format on the InfiniTime
server. The file is automatically opened on your machine in your default
web browser. Results can then be printed or saved using your web browserâs
interface.

To save the results:

* Click
  on File.
* Click on Save or Save As.
* Browse to the desired location
  on your computer.
* Enter a file name.
* Click Save.

*Technical
Note*: Internet Explorer 7.0 may alert you that it is possible for
the page to not save correctly. Click OK. There should be no complications
with saving the grid results as long as the file is saved with the .htm
or .html extensions. The default file name when saving in the HTML format
is dbnetgrid\_aspx.html and can be changed at the users discretion as long
as the extension is not altered.

Save
Grid Results As - WORD

Grid Results are immediately saved in a Microsoft
Word format on the InfiniTime
server. The file is automatically opened on your machine in your default
web browser. Results can then be printed or saved using your web browserâs
interface.

To save the results:

* Click on File.

![](/img/image-404.png)

* Click on Save or
  Save as.

![](/img/image-404.png)

* Browse to the desired
  location on your computer.
* Enter a file name.
* Click on the Save
  as type Drop down box

![](/img/image-404.png)

* Select Word Document
  from the list

![](/img/image-404.png)

* Click Save.

![](/img/image-404.png)

The
default name for Word Documents is dbnetgrid. This can be changed at the
users discretion.

Save
Grid Results As - Excel

Grid Results are immediately saved in a Microsoft
Word format on the InfiniTime
server. The file is automatically opened on your machine in your default
web browser. Results can then be printed or saved using your web browserâs
interface.

To save the results:

* Click on File.

![](/img/image-404.png)

* Click on Save or
  Save as.

![](/img/image-404.png)

* Browse to the desired
  location on your computer.
* Enter a file name.
* Click on the Save
  as type Drop down box

![](/img/image-404.png)

* Select Microsoft
  Excel Workbook from the list

![](/img/image-404.png)

* Click Save.

![](/img/image-404.png)

Excel
Documents do not have a file name entered by default. Users must enter
a file name before saving the file.

Save
Grid Results As - XML

Grid Results are immediately saved in an
XML format on the InfiniTime
server. The file is automatically opened on your machine in your default
web browser. Results can then be printed or saved using your web browserâs
interface.

To save the results:

* Click on File.

![](/img/image-404.png)

* Click on Save or Save as.

![](/img/image-404.png)

* Browse to the desired location
  on your computer.
* Enter
  a file name.
* Click on the Save as type Drop
  down box

![](/img/image-404.png)

* Select XML Files from the list.

![](/img/image-404.png)

* Click Save.

![](/img/image-404.png)

Save
Grid Results As - CSV

Grid Results are immediately saved in a CSV
format on the InfiniTime
server. The file is automatically opened on your machine in your default
web browser. Results can then be printed or saved using your web browserâs
interface.

To save the results:

* Click on File.

![](/img/image-404.png)

* Click on Save or Save as.

![](/img/image-404.png)

* Browse to the desired location
  on your computer.
* Enter a file name. The .csv extension
  must be added to the end of the filename in order to save the file
  in the csv format.

![](/img/image-404.png)

* Click on the Save as type Drop
  down box

![](/img/image-404.png)

* Select Unicode Text from the list.

![](/img/image-404.png)

* Click Save.

![](/img/image-404.png)

The default name for CSV Files is dbnetgrid.
This can be changed at the users discretion.

*Technical Note*:
You may be prompted that the document contains features that are not compatible
with Unicode Text. Save the file anyway, as by typing the .csv extension
the file is automatically saved in a comma-delimited format.

*Technical Note*:
Comma Delimited Files generated by InfiniTime
should be opened for viewing with Excel or Notepad.

Print Grid Results
![](/img/image-404.png).gif)

Displays the default windows printer selection
window allowing you to choose from local printers to print grid results
directly.

Copy Grid to
Clipboard ![](/img/image-404.png).gif)

Places all grid results in the clipboard in
a table form. The table can be pasted to any graphic or word editor. Keep
in mind the table format may vary depending on the features supported
by your word editor. For example, Notepad is unable to display a graphical
table and will simply separate items with spaces.

Once the grid results are successfully copied
the following image is displayed:

![](/img/image-404.png)

Select Grid Columns
![](/img/image-404.png).gif)

Gives users the ability to choose which columns
will be displayed in the grid. For example, many companies will not want
the Social Security number to be visible. This field can be removed from
the grid with this feature.

The Grid Column Selection Window provides
four interactive buttons as described below. These buttons are used to
add and remove columns from the grid and can also alter column order.

![](/img/image-404.png)
 Moves highlighted records in the âSelectedâ list up. This has the
effect of moving the column to the left on the grid itself.

![](/img/image-404.png)
 Moves highlighted records in the âSelectedâ list down. This has
the effect of moving the column to the right on the grid itself.

![](/img/image-404.png)
 Moves highlighted records in the âAvailableâ list to the âSelectedâ
list, effectively adding the item as a new column on the grid.

![](/img/image-404.png)
 Moves highlighted records in the âSelectedâ list to the âAvailableâ
list, effectively removing the column from the grid.

Restores Grid Defaults ![](/img/image-404.png).gif)

Restores the default
grid column configuration.

Specify
Nested Order Levels ![](/img/image-404.png).gif)

Provides users the option
of altering the order by which records are displayed in the grid. Records
can be displayed by alphabetical or numeric order by single or multiple
fields.

![](/img/image-404.png)

Configuring Grid Display
Order:

Highlight the item desired from the Sort
Columns List.

![](/img/image-404.png)

Click Add.

The item will be added to the sequence on
the right side of the page as shown.

![](/img/image-404.png)

Use the drop down box to choose between ascending
or descending order.

![](/img/image-404.png)

Order levels are performed in priority. Ordering
levels at the top of the sequence take precedence over those at the bottom.
Level 1 has the highest priority. Items can be removed from the sequence
by clicking delete.

*Note*:
Only those columns that are displayed by the grid, as chosen during Grid
column configuration, will be available for sorting purposes.

Reset Grid Default Sort
![](/img/image-404.png).gif)

Restores the default
grid sorting configuration.

Grid
Configuration Window ![](/img/image-404.png).gif)

Grid Security
![](/img/image-404.png).gif)

Grid Security, combined
with Security Roles, allow the Software Administrator to configure InfiniTime down to the exact button.
Each employee is assigned an employee role. When the employee signs into
the software with their login ID the software recognizes the employee
role they have been assigned and grants or denies access to the software
based on those rights. Window access is controlled by Security Roles,
while Grid Security is responsible for button access

Two options are provided
for button security, Hidden and Normal. Normal displays the button and
permits interaction. Hidden removes the button from view, effectively
removing access to that portion of the software.

Each security role has
a unique set of button security settings. Be sure to configure Grid Security
for each role based on your companyâs unique access requirements.

Configuring Grid Security:

* Select the security
  role you wish to configure.
* Select
  appropriate settings for each button.

![](/img/image-404.png)
Resets default security configuration settings for the selected security
role.

Additional Details on configuring Security within the InfiniTime Software can be found in
the [Security
Configuration Section](Security/Security_Overview.md#sec01_Security_Overview) of this document.

### Employee Profiles and Related Settings

![](/img/image-404.png)

Employee Profiles serve as the primary point of entry for employee related
settings. The Employee Table, as accessed from the Employee Button on
the Main InfiniTime Toolbar,
lists all employees within the InfiniTime
software. After the initial installation, entry of employee demographic
data is the first essential task that must be performed. Employees can
either be inserted manually or imported from a comma separated (.csv)
 file. If employee demographic data is available from an existing
external application creating employee records using the Import Tool can
significantly reduce data entry time for organizations with more than
25 employees. An overview of the Employee Table and the Employee Update
Form, as used to define employee profiles and related settings, is provided
below.

![](/img/image-404.png)

Insert
â Displays the employee update form. Used to Insert a new employee.

Change
â Opens the Employee Update Form for the highlighted employee to view
or alter an employee's profile and related settings.

Delete
â Deletes the highlighted employee from the InfiniTime
Database. All timecard activity associated with the employee will also
be removed.

Timecard
â Opens the Timecard Activity window and displays timecard information
for the highlighted employee only.

Hide Inactive
Employees - When this option is checked inactive employees
will not be listed in the employee table.

It should be noted that the InfiniTime
Application is licensed by employee count - if the maximum employee count,
as defined by the Software License for a given installation, is reached
the Insert Button on the employee table will be hidden and will not be
available until 1.) Existing employees are inactivated to reduce the existing
number of employees below the maximum employee count or 2.) Additional
employee licenses are purchased and the InfiniTimeSoftware
License is updated to reflect the increased Maximum Employee Count.

### Employee Update Form Introduction

As the central location for all employee related Demographics, HR Related
Information, and Settings the Employee Update form can be overwhelming
at first glance. As previously mentioned, InfiniTime
includes specific features to ensure required details are entered when
creating new records. Pay special attention to any required fields, as
shown in blue, below which must be configured. If a user should attempt
to click OK before completing all required fields the InfiniTime
Software will display a warning and prompt the user to complete any required
fields that were missed.

![](/img/image-404.png)

### Employee Update Form - User Interface Introduction

Settings on complex forms within InfiniTime
such as the Employee Update Form, the Policy Update Form, and the Reader
Configuration Update Form, are separated into logical groups according
to function by 1.) Section and 2.) Tab as illustrated below.

![](/img/image-404.png)

In this way, the Employee Update Form is broken into separate sections,
and separate tabs within those sections for clarity and ease of use. Details
on each section of the Employee Update Form and related settings are provided
below.

### Demographics Section

In the Demographics tab you will be able to enter basic information
about the employee such as employee number, name, address, gender, ethnic
code and you can also attach a picture to the employee record. Required
fields are noted as such in the field description below.  Should
a required field be left blank upon attempting to save the record by clicking
the OK button, the system will prompt the user to fill out the required
fields that were missed.

### Demographics Tab

![](/img/image-404.png)

Employee Number
- This unique number is a required field and it is used as a point
of reference for the employee record.

Inactive -
Checking this box will change the employeeâs status to inactive. Inactive
employees do not count towards the global employee limit, nor will they
show up on reports. Employees that are set to inactive will be highlighted
in red in the employee table.  This feature is useful to keep details
on file for employees who are no longer employed by your organization.
 Inactive employees will not be available for reporting or other
InfiniTime features where
you are prompted to select an employee. The Date of Termination and Termination
Reason fields will be displayed on the Employee Update Form when the Inactive
option is checked. Details on how to define termination reasons are provided
below.

![](/img/image-404.png)

Date
Of Termination - This date field is the date the employee ended
work with the company.

Termination
Reason - This field will allow you to enter a reason of why the
employee was terminated, allowing you to maintain accurate records of
the employeeâs status. Termination Reasons must first be defined on the
Termination Reasons Table before they can be assigned to an employee.
Click on the Lookup Magnify Glass to the right of the Termination Reason
field to open the Termination Reason Table.

### Termination Reason Table

![](/img/image-404.png)

The Termination Reasons Table allows you
to keep a list of descriptions of why an employee was terminated which
allows you to keep your Human Resources information current and up to
date. Termination reasons can be assigned to an employee after their status
has been set to inactive within the Employee Table.

To
assign Termination Reasons to an employee:

1.) Define Termination
Reasons within the Termination Reason Table.

a.) Open the Termination Reason Table by
clicking on Lookups, Employee Setup, Human Resources Lookups, and Termination
Reasons.

![](/img/image-404.png)

b.) Click insert to open the Termination
Reason Update Form.

![](/img/image-404.png)

c.) Type a termination reason into the field
provided and click OK to save it.

![](/img/image-404.png)

d.) Repeat step C for all applicable termination
reasons.

2.) Assign Termination
Reasons to inactive employees.

a.) Open the Employee Table by clicking
on the Employee Button on the main menu.

![](/img/image-404.png)

b.) Ensure the Hide Inactive Employees option
is unchecked.

![](/img/image-404.png)

c.) Locate an inactive employee, highlight
their record, and click change.

![](/img/image-404.png)

d.) Enter a termination reason into the
termination reason field at the bottom of the form as shown.

![](/img/image-404.png)

e.)
Click OK to save the record.

First, Middle
Initial, and Last Name -  First and Last Name fields are required.

Address, City,
State, County or Province, Zip/Postal Code, Phone Number -  Enter
the appropriate contact information for the employee.

Cell Number
- Enter the employee's cell phone number. This field is primarily intended
for Employee and Supervisor Exception Notifications, which when enabled,
are automatically sent to employees and / or supervisors when exceptions
occur. Only numeric digits should be entered in this field. Do not enter
dashes or parenthesis to separate the area code from the local phone number.

Cell
Provider - The Cell Provider is displayed as a required field
if the Cell Number is filled. Select the employee's cell phone carrier
by clicking on the Lookup Magnify Glass and selecting the appropriate
carrier. If the employee's cell phone carrier is not present in the list
of Cell Phone Providers it must be added with the correct SMS Email Gateway
address. The SMS Email Gateway address for a given cellular carrier can
be obtained by contacting technical support personnel for the respective
carrier or by sending an SMS text to any email address from a device on
the respective carrier's network. Exception Notifications utilize the
cell phone provider's SMS Email Gateway to send SMS Notifications to supervisors
and employees. Additional details can be found within the[Exception Notifications section](Policies/Policy_Overview.md#pol33_Exception_Type_Update_Form_-_Notifications_Tab) of this document.

Gender -
 Select the sex of the employee from the drop down list.

Ethnic Code -
Select from the drop down list the correct ethnic code of the employee.

Picture (Optional)
- Click on the Select Picture button to choose an employee
image or company logo. This will bring you to the File Selection window.
Choose the path, then select the file. For best results select a .jpg
file, 100 X 100 pixels, not larger than 256 kb. Click the Remove Picture
button to remove the image previously selected.

### HR Profile Tab

The HR Profile Tab includes HR Related Employee details such Primary
Email Address, Social Security Number, Hire Date, Emergency Contact, and
review dates. Remember, only required fields must be entered. All other
fields are optional, though some are intended for specific purposes as
noted below.

![](/img/image-404.png)

Job Title - Describe
the Employee's Job Title in this field.

Employment Status
- Select the appropriate Employment Status from the Employment
Status Type table for the employee. Click
on the Lookup Magnify Glass to the right of the Employment Status field
to open the Employment Status Table.

### Employment Status Types Table

Employment Status Types are used to define
employment status for individual employees in accordance with the rules
and guidelines set forth by the United States Equal Employment Opportunity
Commission and can be used for tracking purposes to show employee distribution
across various Employment Status types.

![](/img/image-404.png)

Insert
- Adds a blank record to the Employment Status Types Table. To
assign an Employment Status Type to an employee, select the desired Employment
Status and click on the select button.

Delete
- Deletes the selected Employment Status from the Employment Status
Types Table. If an Employment Status is assigned to employees InfiniTime will not permit it to be
deleted.

Email Address
- Enter the Primary Email Address to be kept on file for the employee. If enabled,
Employee Email Exception Notifications will be sent to this email
address.

Twitter Screen
Name - Enter the employee's Twitter Screen Name to be kept
on file for Public Relationship management purposes if desired.

SS/SI/NI Number
- Social Security, Social Insurance, or National Insurance Number
field of the employee and must be a unique number.

Default Wage -
Denotes the employee's default hourly wage. The Default Wage is
used for employee Wage Calculations if a Department / Job / Task specific
wage is not defined for specific punch pairs Department / Job / Task combination.

\EEO
Type - This field is a job classification given to the employee
in accordance of the Equal Employment Opportunity Commission. Click on
the Lookup Magnify Glass to the right of the Employment Status field to
open the Equal Employment Opportunity Types Table.

### Equal Employment Opportunity Table

![](/img/image-404.png)

Insert
- Adds a blank record to the Employment Status Types Table. To
assign an Employment Status Type to an employee, select the desired Employment
Status and click on the select button.

Delete
- Deletes the selected Employment Status from the Employment Status
Types Table. If an Employment Status is assigned to employees InfiniTime will not permit it to be
deleted.

WCC Description
- Click on the Lookup Magnify Glass to the right of the Employment
Status field to open the Equal Employment Opportunity Types Table.

### Workers Compensation Code Table

Workers compensation categories are optional
and can be used to group employees according to work place exposure codes
which are controlled and designed by the National Council of Compensation
Insurance (NCCI).

![](/img/image-404.png)

Insert
- Opens the Worker Compensation Code Update Form which can be used
to enter new Workers Compensation Code Descriptions to the Workers Compensation
Code Table. One record should be created for each Workers Compensation
Code used by your organization.

![](/img/image-404.png)

Change
- Opens the Workers Compensation Code Update form for the selected
Workers Compensation Code. The InfiniTime
Administrator may then alter the Workers Compensation code as desired.

Delete
- Deletes the selected Workers Compensation Code from the Workers
Compensation Code Table. If an Employment Status is assigned to employees
InfiniTime will not permit
it to be deleted.

Emergency Contact
Information - Enter the Name, Relationship, and Phone number for
the employee's emergency contact to be kept on file in case of emergency.

Date of Birth
- Date employee was born.

Date of Hire -
Required Field. Enter the date the employee began working for your
organization. The Date of Hire is used by the InfiniTime
Accruals System, Holidays, and Exceptions. It is important to note that
InfiniTime will not create
Holiday Records or exceptions for an employee before their date of hire.
Additionally, employee accrual totals are tracked from the employee's
date of hire forward in accordance with Accrual Type Settings and related
Accrual Calculations.

Adjusted Hire
Date - The Adjusted Hire Date overrides the Date of Hire. If an
employee was previously terminated and rehired, an Adjusted Hire Date
should be set. When set, InfiniTime
will use the Adjusted Hire Date in place of the Date of Hire for all functions
which reference the Date of Hire such as Accruals, Holidays, and Exceptions.

Last Performance
Review Date - Enter the date of the employee's last performance
review to be kept on file.

Last Wage Review
Date - Enter the date of the employee's last wage review to be
kept on file.

Last Raise Date
- Enter the date of the employee's last raise review to be kept
on file.

### Payroll Profile Tab

The Payroll Profile Tab includes fields related to employee taxes, pay
method, and direct deposit.

![](/img/image-404.png)

Pay Method - In
this drop down list, you may choose from Hourly, Per Diem, Salary and
Other.  This designates the type of pay the employee falls under.

Pay Type - The
list consists of Exempt, Non-Exempt, and Temporary. This also helps
classify what category the employee falls under.

Additional Payroll
Id - The Additional Payroll ID is used for some payroll export
formats which require an employee specific identifier separate from the
Employee ID on the Demographics Tab. Additional details on the use and
configuration of Payroll Export, which permits transferring of employee
hours and earnings to a 3rd party payroll application, can be found in
the Payroll Export section of this document.

### Employee Tax and Withholding Information

### Federal Tax Information Tab

![](/img/image-404.png)

Federal
Marital Status - Enter the Employee's Federal Marital Status to
be kept on File. Options include Married, Single, or Head of Household.

Federal
Exemptions - This field will allow you to enter the number of exemptions
claimed by the employee.

Additional
Federal Withholdings - This field will allow you to enter any additional
amount the employee wants to withhold for federal taxes.

### State Tax Information Tab

![](/img/image-404.png)

State
Marital Status - this field will allow you to select the State
Marital Status for the state withholdings you can select from Married,
Single or Head of Household.

State
Exemptions - This field will allow you to enter the number of exemptions
claimed by the employee.

Additional
State Withholdings - This field will allow you to enter any additional
amount the employee wants to withhold for state taxes.

State
Tax Authority - This field will allow you to enter the State Tax
Authority for the employee.

### Local Tax Information Tab

![](/img/image-404.png)

Local
Exemptions - This field will allow you to enter the number
of exemptions claimed by the employee.

Additional
Local Withholdings - This field will allow you to enter any additional
amount the employee wants to withhold for local taxes.

Local
Tax Authority - This field will allow you to enter the Local Tax
Authority for the employee.

### Direct Deposit Information

The Direct Deposit tabs of the Payroll
Profile Tab within the Employee Demographics section permit entry of direct
deposit details to be kept on file. The form permits entry on details
for up to four accounts to which employee earnings can be dispersed. Disbursements
can be configured as set dollar amounts or percentages of the employee's
pay check.

![](/img/image-404.png)

### Settings Tab

![](/img/image-404.png)

### Settings Tab - General

Default Department:
 This field is required. The Department selected here will appear
each time an employee logs in to the system, or scans their assigned Employee
Card. This drop down list contains all created Departments, (See Departments).

Default Policy:
 Select the appropriate Policy for the employee. This field is required.
All policies that have been inserted into the software are available from
the Magnify Glass.

Accrual Type:
Select the appropriate accrual type for the employee.

Holiday Schedule
Type: Select the appropriate Holiday Schedule type for the employee.

Security Role:
Select the security role that describes this employeeâs interaction with
the InfiniTime software.

Escort:
Should the employee login to the InfiniTime
Escort Module, the employee will see the escort window specified by this
field. This helps make InfiniTime
more user friendly for employees with minimal computer skills. Nearly
all software actions and windows can be assigned to a single button and
displayed in an organized manner for easy access. Refer to the Escort
section of this document for more information.

Access Control
Group: If your company is using access control equipment in conjunction
with Access Control Groups, you can use this field to assign employees
to a specific access control group.

Supervisor Name:
Select the employeeâs supervisor.

### Settings Tab - Groups

InfiniTime requires groups
to be assigned to each employee when groups are present in the system.
The first group description inserted for every group level will automatically
be set as the default group and will be assigned to any employee who does
not have a group assigned. If this is undesirable Inception Technologies
recommends creating a group entitled unassigned. Any employees who are
not intended to be assigned to a group should then be assigned to the
unassigned group. It should be noted that any group can be designated
as the default. Keep in mind that new employees will automatically be
assigned to the default group and will remain on the default group until
their groups are manually assigned.

NOTE: Group Levels and Group Descriptions must
first be configured before employees can be assigned to groups. Additional
Details regarding configuring Groups within InfiniTime
can be found in the [Groups
Configuration Section](Configuration/Product_Configuration.md#gr01_Groups_Introduction) of this document.

![](/img/image-404.png)

The Groups tab will display all available Groups that an employee can
be assigned to. Assigning employees to groups provides additional options
for report filtering. To assign a group description to an employee simply
click on the drop down box and select the group you wish to assign to
the employee. To remove an employee from a group click the delete button.

*NOTE*:
The Groups Tab will be blank if Group Levels and Group Descriptions have
not been configured within the InfiniTime
Database.

### Employee Group Update Form

![](/img/image-404.png)

Group -
Enter the Name of the Group Description to which the employee belongs.
Alternatively, Click on the Lookup magnify glass to select the desired
Group Description from the Group Description Table.

### Login Tab

The login tab displays employee login information. This information
is used to logon to the InfiniTime
software and clock in or out of work using the InfiniTime
Employee Module. More information is provided below.

![](/img/image-404.png)

ID and Password
- These fields are required and are used to login to the various
InfiniTime Manager Modules.
You can either ask your employees to provide you with an ID and password
or designate one for them. The ID and Password should be easy for the
employees to remember. These fields will accept any characters, (alpha
or numeric) or a combination of characters.

Clock ID and Password
- These fields are required and are used to identify employees
at hardware time and attendance terminals. The Clock ID and Password must
be numeric only and may not contain letters. It is recommended that the
Clock ID and Password be easy for employees to remember as they will need
to use them regularly at the terminal to punch in and out.

Badge ID Number
- Enter the employeeâs barcode or magstripe badge number in this
field to assign that card to the employee. All digits of the number must
be included for the system to identify the card and employee.  If
the card has a pair of asterisks, do not include the asterisks.

Technical Note: The Badge Field will not be displayed
if the software license has a badge reader count of zero (0).

Security Filter
- The Security Filter Button opens the Employee Security Filter
Update Form which permits InfiniTime
Administrators to define the specific Employees, Departments, Jobs, and
Tasks which the respective employee may access within the InfiniTime Software. The Employee
Security Filter is considered an integral piece of the InfiniTime Software's security system.
Additional details on the use and configuration of Employee Security Filters
can be found in the [Security
Configuration Section](Security/Security_Overview.md#sec16_Security_Filters) of this document.

User Must Change
Password at Next Logon - this checkbox if checked
it will force the employee to change their password next time they log
into the software whether they are login into the manager module, employee
module, or escort.

Limit
Employee Login to the Following TCP/IP Addresses - In this
section you can enter different TCP/IP Addresses of computers this specific
employee can access the software you can read more about the valid IP
addresses in the [Security
- Valid IP Addresses Section](Security/Security_Overview.md#sec23_Valid_IP_Addresses_-_Overview) of this document.

### Accrual Totals Section

The Accrual Totals Section displays employee accrual total records and
is intended for reviewing and adjusting accrual totals on an employee
by employee basis. Employee Accrual Total records are generated according
to the existing accrual configuration within InfiniTime
and the Accrual Type assigned to the employee.

![](/img/image-404.png)

The Employee Accrual Totals Table displays all Employee Accrual Total
records for the respective employee. If a supervisor should step away
from the computer for a moment when reviewing employee Accrual Totals,
notice that the Title Bar of the Employee Accrual Totals Table shows the
Employee's name. In fact - all sections of the Employee Update Form display
the name of the employee whose Employee Profile is displayed. It is important
to note that the Employee Accrual Totals Table displays *all*
employee accrual total records for each Accrual Calculation across all
Accrual Types in the employee's assigned Accrual Class from date of hire
(or effective date) to the current date. Employee accrual total records
are maintained by the InfiniTime
Accrual System and are automatically recreated based on an employee's
assigned accrual type if they are deleted. It is not possible to filter
records on the Employee Accrual Totals Table such that only Accrual Totals
for the current accrual period are shown, or to specifically delete accrual
totals from a single year in order to prevent a specific employee from
accruing hours in that accrual period. The Base Amount, as outlined below,
is the primary method for making minor adjustments to a single employee's
accrual totals.

It is recommended that customers who find it necessary to make use of
the base amount on a regular basis to adjust employee accrual totals review
the Accrual Types configured within InfiniTime
to determine if a slightly different calculation would better suit the
needs of the customer's organization. For example, it may be that a small
group of employees do not fit will in their existing Accrual Class and
a separate Accrual Class with distinct settings for each accrual type
should be configured and assigned to that specific group of employees.

The following details are displayed for each Employee Accrual Totals
record in the Employee Accrual Totals Table:

Type -
Displays the Accrual Calculation Name to which the Employee Accrual Total
Record belongs.

Date and Thru
Date - Displays the Start Date and the Through Date for each Employee
Accrual Totals record. This date range is determined by the Carry Over
Reset Type set for the respective Accrual Calculation. Additional details
on available Carry Over Reset Types such as Calendar Year, Anniversary,
and Fiscal Year *(Accruals Plus Only)*
can be found in the [Accruals
Configuration Section](Configuration/Accrual_Configuration.md#acc01_Employee_Accruals_Introduction) of this document.

Base
Amount - The Base Amount permits manual adjustment of the Total
Time Remaining for the respective Employee Accrual Totals record. A positive
amount entered into the Base Amount field will add additional hours to
the Employee Accrual Totals record. A negative amount entered into the
Base Amount field will subtract hours from the Employee Accrual Totals
record. The most common use of the Base Amount field is to enter a starting
balance for employees as carried over from the customer's prior accrual
tracking system. An effective date can then be set for all accrual calculations
from a specific date and InfiniTime
will continue to accrue hours for employees from that date forward. The
second most common use of the Base Amount field is to make one time adjustments
to employee accrual totals for individuals by either adding or subtracting
hours from the employee's accrual total records.

Carry Over Amount
- Displays the total number
of hours carried forward from the prior accrual period. The Carry Over
Amount will be blank if the respective accrual calculation does not have
Carry Over enabled.

Time Accrued -
Displays the total number of hours accrued for the respective accrual
calculation / accrual period in accordance with the Accrual Type(s) within
the Accrual Class the employee is assigned to.

Time Accrued Plus
Base - Displays the adjusted total of the Carry Over Amount,
Time Accrued, and the Base Amount entered by the user.

Time Used - Displays
the total number of Other Activity Hours deducted from the Accrual Calculation
during the respective accrual period through use of Other Activity Types
configured to deduct from the Accrual Calculation. IE: Sick Time, Vacation
Time, etc.

Time Remaining
- Displays the total number of hours remaining for use during the
respective accrual period.

Accrued Wages
Earned - Reflects Accrued Hours in Dollars. Accrued Wages Earned
are calculated by multiplying total accrued hours by the employee's default
wage. The Accrued Wages Earned column will be blank if the respective
employee does not have a default wage defined.

Accrued Wages
Remaining - Reflects Remaining Accrued Hours in Dollars. Accrued
Wages Remaining are calculated by multiplying remaining accrued hours
by the employee's default wage. The Accrued Wages Earned column will be
blank if the respective employee does not have a default wage define.

### Employee Accrual Detail Table

Details -
The Details Button permits employee's and supervisors to view all instances
at which hours were added to or subtracted from an employee's accrual
calculation for the respective accrual period. In this way, the employee
and / or supervisor may review the exact calculation performed by the
InfiniTime Accrual system
and the exact dates on which employees were awarded hours for comparison
with their own records. To view Employee Accrual Detail records, also
referred to as Accrual Posting records, select the Employee Accrual Total
Record you wish to review from the Employee Accrual Totals Table and then
click on the Details button.

![](/img/image-404.png)

Additional details on configuring InfiniTime
Accrual Types can be found in the [Accruals
Configuration Section](Configuration/Accrual_Configuration.md#acc01_Employee_Accruals_Introduction) of this document.

### Badge Numbers Section

If your company is using badges in conjunction with a Zephyr clock you
have the option of assigning additional badges to an employee for separate
departments. This allows employees to simply swipe the badge for the department
they wish to work in instead of switching departments with the Employee
Module or Zephyr Clock function key. It should be noted that this tab
will not be displayed if the Software License has a badge reader count
of zero (0).

Inserting
Badge Numbers

* Click Insert

![](/img/image-404.png).gif)

* Enter the badge number that will
  be used to swipe in and out for the new department.

### Employee Badge Update Form

![](/img/image-404.png).gif)

* Select
  the department that will be associated with the above badge.
* Click OK to save the entry.

![](/img/image-404.png).gif)

### Benefits Section

Benefit Plan Types represent different benefits offered by the employer.
Related details such as Benefit Plan Cost, Enrollment Date, etc can then
be defined on an employee by employee basis  for tracking purposes.
The Benefits Section permits entry of individual benefits such as Medical,
Vision, Dental, Travel, etc. paid to employees and their cost to the employer
for tracking purposes.

To insert benefit information, click on the insert button and fill in
the information. Plan Type's and Plan Costs must first be defined before
Employee Benefits can be created.

### Employee Benefit Information Update Form

![](/img/image-404.png)

Description -
Enter the name of the benefit. (IE: Basic Medical). This field is required
and must be entered. .

Plan Type -
Enter the first few characters of the Plan Type Name to auto fill the
Plan Type or use the Lookup Magnify Glass to select the desired Plan Type
from the  Plan Type Table. For ease of entry, it is recommended that
all Benefit Plan Types (IE: Basic Medical, 80/20 Medical, Full Medical,
Vision, Dental) offered by an organization be entered into the Plan Type
Table prior to creating Employee Benefits. This field is required and
must be entered.

### Benefit Plan Type Table

![](/img/image-404.png)

Insert
- Click Insert to create a new Benefit
Plan Type then enter a description for the respective Benefit Plan Type.

Delete
- Click on an existing Benefit Plan Type to select it, then
click the Delete Button to delete the selected Benefit Plan Type. If a
benefit Plan Type assigned to employee's is deleted InfiniTime
will automatically remove all Employee Benefits assigned to the respective
Benefit Plan Type.

Plan Cost -
Enter the first few digits of the Plan Type Cost to auto fill the Plan
Cost or use the Lookup Magnify Glass to select the desired Plan Cost from
the  Plan Cost Table. For ease of entry, it is recommended that the
Benefit Plan Cost corresponding to each Benefit Plan Type offered by an
organization be entered into the Plan Type Table prior to creating Employee
Benefits. This field is required and must be entered.

### Benefit Plan Cost Table

![](/img/image-404.png)

Insert
- Click Insert to create a new Benefit
Plan Cost then enter a description for the respective Benefit Plan Cost.

Delete
- Click on an existing Benefit Plan Cost to select it, then
click the Delete Button to delete the selected Benefit Plan Cost. If a
benefit Plan Cost assigned to employee's is deleted InfiniTime
will automatically remove all Employee Benefits assigned to the respective
Benefit Plan Cost.

Waiver Cost -
If desired, enter a dollar amount to indicate the cost of the benefit
to the employer if the employee decides to waive their right to the offered
benefit plan type.

Waiver Saving
- If desired, enter a dollar amount to indicate the savings to
the employer if the employee decides to waive their right to the offered
benefit plan type.

Pension System
- Enter the name or description for the employees chosen overall
benefit and / or pension package to be kept on record if desired.

Pension Number
- If desired, enter the identifier for the employee's chosen overall
benefit and / or pension package to be kept on record.

Enrollment Date
- If desired, enter the date on which the employee first enrolled
in the respective benefit Plan Type.

### Dependants Section

The Dependants section of the employee update form permits entry of
details for employee dependants to be kept on file. .

![](/img/image-404.png)

### Employee Dependant Information Update Form

Click insert and the Employee Dependant
Information Update Form will open.

![](/img/image-404.png)

Enter the desired demographic details to
be kept on file for the dependant. The First and Last Name are the only
required fields.

### Holidays Section

The Holidays Section of the Employee Update Form permits InfiniTime Software Administrators
to define employee specific holidays. In this way, Paid or Unpaid Leave
for specific occasions observed by specific employees can be automatically
inserted into the employee's timecard without additional manual entry.
Employee specific holidays are configured in the same manner as Company
Wide holidays with one exception. Employee specific holidays do not include
any tenure information as they are entered specifically for an employee
and are automatically awarded as long as the employee meets any conditions
defined for the specific holiday date.

![](/img/image-404.png)

Insert
â Displays the Employee Holiday Update form. Used to insert a new holiday
type. Each holiday that will be assigned to the specified employee must
be configured and inserted individually using this option.

Change
- Opens the Employee Holiday Update Form for the selected Holiday Date.
The InfiniTime Administrator
may then alter the Holiday's configuration as desired. It is important
to note that InfiniTime
does not permit the Holiday Date to be changed once a Holiday Date has
been configured and timecard records have been created for the holiday
date. A new Holiday entry must be created for every specific date on which
employees are to be automatically awarded paid and / or unpaid leave hours
according to holiday settings. For example, Holiday Dates for 2012 should
be created for 2012 and retained within the database after 2012 is over.
Holiday Dates for 2013 should then be configured for each respective holiday
observed by the organization.

Technical Note: Customer's who choose to ignore
the above instruction and change holiday dates from year to year may observe
that employees intermittently receive their Paid / Unpaid leave hours.
This occurs because InfiniTime
specifically checks to determine if an Other Activity Record has been
created for a given holiday date for a specific employee before creating
another holiday record. In this way, any employee who received the 2012
holiday will not be awarded a 2013 holiday if the Holiday Date is changed
from 2012 to 2013. As of InfiniTime
7.08, the InfiniTime User
Interface will specifically prevent users from changing the date of a
holiday if one or more Other Activity timecard records are associated
with the holiday. However, users on earlier versions of the software may
observe this issue if the above instruction is ignored.

Delete
- Deletes the selected Holiday Date from the Employee's Profile.

### Holiday Master Holiday Update Form

![](/img/image-404.png)

Holiday Options and Related Settings for Employee Specific Holidays
are the same as those for Company Wide Holiday Types. Please refer to
the [Holiday Configuration section](Configuration/Product_Configuration.md#hol03_Holiday_Schedule_Type_Update_Form)
of this document for details on Holiday Options available on the Holiday
Master Holiday Update Form..

### Important Dates Section

The Important Dates Section of the Employee Update Form permits entry
of Important Date values on an employee by employee basis. Important Dates
allow the InfiniTime Software
Administrator to define specific events which are of mission critical
importance for individual employes. (IE: CPR Certification Expiration
Date for a Pool Management Company that hires lifeguards.) Once employee
Important Dates have been defined, the[Important Dates Report](Reports/Reports.md#rpt31_Important_Date)
can be used to view upcoming employee Important Dates. Before Important
Dates can be defined for individual employees Important Date Names must
first be defined.

### Employee Important Date Update Form

![](/img/image-404.png)

Name - Enter
the first few characters of the Important Date Name to auto fill the Important
Date Name or use the Lookup Magnify Glass to select the desired Important
Date Name from the Important Date Table. For ease of entry, it is recommended
that the Important Date Names for all Important Dates to be tracked by
an organization be entered into the Important Dates Name Table prior to
creating Employee Important Dates. This field is required and must be
entered.

Reference Date
- Enter the first date on which the important date should occur.
The Important Date will display on the Important Dates report for the
respective employee for the first time on this date. The important date
will then reoccur in accordance with the Important Date Interval.

Interval -
Select the desired interval from the drop down menu. The following options
are available:

* Annually - Causes the Important Date to
  reoccur every year on the same Month and Day.
* Monthly - Causes the Important Date to
  reoccur every month.
* Bi-Weekly - Causes the Important Date to
  reoccur every two weeks (14 days).
* Weekly - Causes the Important Date to reoccur
  every week (7 Days).
* Daily - Causes the Important Date to reoccur
  every day.
* Custom - Permits the user to enter a custom
  interval, in days, for the important date to reoccur. IE: 90 Days,
  120 Days, etc

### Important Date Table

![](/img/image-404.png)

Insert
â Displays the Displays the Important Date Update Form which is used to
enter a new Important Date Name.

Change
- Opens the Important Date Update Form for the selected Holiday Date.
The user may then alter the Important Date Name as desired.

Delete
- Deletes the selected Important Date Name. It should be noted that InfiniTime will not permit an Important
Date Name to be deleted if it has been assigned to an Important Date for
an employee.

### Messages Section

The Messages Section of the Employee
Update Form permits InfiniTime
Administrators and Supervisors to review both incoming and outgoing messages
for a specific employee. Messaging allows employees to send messages to
their supervisors regarding requests for time off, schedule changes, or
even a simple reminder or note. Additional Details on use of messaging
functionality can be found in the [Messaging
Section of this document.](Messaging/Messaging.md#msg01_Messaging_Introduction)

### Incoming Messages Tab

The incoming messages tab displays messages recently sent to the employee.
The Date Range may be adjusted as desired to view messages for any date
range. In this way, InfiniTime
Administrators may review an employee's historical messages.

![](/img/image-404.png)

### Outgoing Messages Tab

The Outgoing messages tab displays messages recently sent to the employee's
supervisor. The Date Range may be adjusted as desired to view messages
for any date range. In this way, InfiniTime
Administrators may review an employee's historical messages.

### Schedule Information Section

The Schedule Information Section of the Employee Update Form includes
all employee specific Schedule Related settings. It is important to note
that Schedules within InfiniTime
follow a hierarchical order. The employee record schedule takes precedence
over every other schedule type except for the Schedule GANTT chart. Refer
to the [Scheduling Configuration
section](Scheduling/Scheduling.md#sch18_Employee_Schedule_Window_-_Introduction_) of this document for more information about use of the Schedule
GANTT chart.

Default Schedule

The default schedule within an employeeâs
record is used to enter a schedule that is intended solely for the selected
employee. It is important to note that this schedule is not required,
but if it is used it will take precedence over most other schedules in
the software including the department schedule and shifts as outlined
below. Only changes made in the Schedule GANNT chart take precedence over
the Employee Default Schedule. The hierarchy, as listed below,  is
arranged by schedule priority from top to bottom. In this way, schedules
can be defined in multiple areas within the InfiniTime
Software according to an organization's needs. InfiniTime
will automatically apply schedules to employee's based on the Schedule
Hierarchy to determine an employee's effective schedule for any given
date.  Additional details regarding the Schedule Hierarchy can be
found in the [Scheduling Configuration
section](Scheduling/Scheduling.md#sch02a_What_type_of_scheduling_best_fits_the_needs_of_my_company_) of this document.

| Scheduling Method | Schedule Hierarchy Priority |
| Schedule GANNT Chart Entries  * Created via Skeletons * Created via Quick Schedule * Created via 'New Working' on the Right Click Menu of the   GANNT Chart | 1 |
| Employee Default Schedules  * Defined within Employee Profiles (IE: Employee Update Form   - Scheduling Information Section - Default Schedule Tab) | 2 |
| Shifts Assigned to an Employee  * Shifts are Configured via the Shift Table * Shifts are assigned to employees within Employee Profiles   (IE: Employee Update Form - Scheduling Info Section - Shifts   Tab) | 3 |
| Department Default Schedules  * Defined for a specific Department on the Department Update   Form * Associated with Employees based on their Department as   assigned within Employee Profiles (IE: Employee Update Form   - Demographics Section - Settings Tab) | 4 |
| Policy Default Schedules  * Defined for a specific Policy on the Policy Update Form * Associated with Employees based on their Policy as assigned   within Employee Profiles (IE: Employee Update Form - Demographics   Section - Settings Tab). | 5 |

For example, the default schedule defined
on an employeeâs policy would be ignored if a default schedule were configured
for the employee in their employee or department record. Before configuring
employee specific schedules, it is recommended that customer's review
the [Scheduling Introduction
Section of this document](Scheduling/Scheduling.md#sch01_What_do_I_want_to_accomplish_by_using_schedules_) for details on the benefits of tracking employee
schedules within InfiniTime.
In this way, InfiniTime
Software Administrators can make specific decisions with regard to how
employee schedules are created to ensure the best scheduling method for
your organization's unique needs is chosen.

![](/img/image-404.png)

To create schedules select the ![](/img/image-404.png)
 button from the Default Schedule Tab in Schedule Information. The
Employee Schedule Cycle defaults to weekly but can be customized by changing
the Schedule Cycle to Custom. The custom schedule cycle permits a schedule
to repeat every several days, as specified by the user. The reference
date is considered day one of the schedule.

![](/img/image-404.png).gif)

Quick Default Schedule

The Quick Scheduler allows you create a
schedule by directly typing in the start and end times.  To create
the default schedule, start by clicking on the tab for the day of the
week. In the Start Time field under the Regular Hours column, type in
the starting time.  Next, in the End Time field, enter the time that
this Regular working period ends (ie ends before a lunch break, or the
end of the day.)  Continue the process until the entire shift has
been completed.

![](/img/image-404.png)

Start Time
- In this field you can enter the start time for the Regular Hours, Paid
Break, and Unpaid Break.

End Time
- In this field you can enter the end time for the Regular Hours, Paid
Break, and Unpaid Break.

*NOTE*:
 It is often difficult to schedule breaks. As a rule, scheduling
related exceptions are rigid and function in accordance with Rounding
and Grace Period Settings on an employee's policy. Exceptions will be
generated if employees do not take breaks exactly as scheduled. It is
generally only recommended to schedule breaks if they must be taken at
a specific time such as in a production environment where breaks are triggered
by site wide bells or chimes. Otherwise, Breaks should not be scheduled.

Valid From
- Is the date in which the schedule will start to be valid.

Valid To
- Is the date in which the schedule will end being valid.

*NOTE*:
The Valid From and Valid To fields are not required, if the fields are
blank then the schedule will always be valid.

Copy Button
- The copy button will open the Copy Quick Default Schedule Window which
can be used to copy the schedule configured for a specific day of the
week o other days of the week.

### Copy Quick Default Schedule Window

To copy the schedule from day to day, click
the copy button to bring up the following form:

![](/img/image-404.png)

Copy From
- Use the pull down menu to select the day you wish to copy schedule configuration
from.

Copy To
- Place a check in each box that you wish to copy the schedule to then
click OK to copy schedule configuration to each selected Day of the Week.

### Shifts Tab

The shift tab is used to assign shifts to an employee. Employees can
be assigned to more than one shift. InfiniTime
will automatically choose the appropriate shift according to the employeeâs
clock in time. An employee's clock in time must fall within the grace
periods set in their policy in order for their activity to be associated
with a shift. For example, an employee clocks in 30 minutes prior to their
shift. Grace Period settings are configured to consider this as an âEarlyâ
punch. The employeeâs time will be considered on the shift. Refer to the
[Policy
Configuration section of this document](Policies/Policy_Overview.md#pol109_Scheduled_Time) for more information on grace
periods.

![](/img/image-404.png)

Assigning a shift to an employee:

* Click Insert.

![](/img/image-404.png).gif)

* Type the name of the shift you
  wish to assign into the box or use the Lookup Magnify Glass to select
  the desired shift from the Shift Table.

![](/img/image-404.png)

# Availability Tab

The availability tab allows availability schedules to be assigned to
an employee. Availability Types are templates which reflect the normal
hours an employee is considered available for work related duties. Availability
Types are intended for use by organizations with dynamic scheduling environments
such as restaurants where staffing requirements are based on customer
demand. Additional details on the use and configuration of Availability
Types can be found in the Schedule Configuration Section of this document.

To assign an Availability Schedule to an employee do the following:

* Open the employee table
* Select the employee you want to assign the availability
* In the Employee Update form go to the Schedule Information section
  of the update form
* Click on the Availability Tab

![](/img/image-404.png)

* Click on the insert button.

![](/img/image-404.png)

* On the description, click on the magnify glass to select an availability
  or just start typing the name of the availability and it will auto
  fill.

### Trained Tasks Tab

The Trained Tasks Tab allows trained tasks to be assigned to an employee.
Trained Tasks allow the InfiniTime
Administrator to define specific job roles and functions which require
certain skill sets (IE: Cashier, Fry Cook, Hostess, etc.). One or more
trained tasks can then be assigned to individual employees to indicate
skill sets for which an employee has been trained. Trained Tasks are used
in conjunction with [Skeletons](Scheduling/Scheduling.md#sch44_Schedule_Skeletons___Benefits_and_Configuring)
and [Find
Available](Scheduling/Scheduling.md#sch42_Find_Available) for employee scheduling purposes. Additional information
regarding use and configuration of employee schedules and Trained Tasks
can be found in [the Schedule
Configuration section of this document.](Scheduling/Scheduling.md#sch39_Trained_Tasks___Benefits_and_Configuring)

![](/img/image-404.png)

Insert
â Adds a blank record to the Trained Tasks tab for the respective employee.
Select the Trained Task Description for which the employee has been trained
and then enter the hourly wage which the employee receives for the respective
trained task.

![](/img/image-404.png)

Delete
- Deletes the selected Trained Task from the employee's profile. If a
trained task is removed from an employee's profile, the employee will
not be listed as available on the Use Skeleton Window or the Find Available
Window for the respective trained task.

### Days Off Tab

The Days Off Tab displays all Days Off
which have been defined for the respective employee. Days Off make it
possible to schedule an employee to be absent for a specific date. Specifically,
a Day Off must be created in order to override a Scheduled Work Day defined
on a Default Schedule such as the Employee Default Schedule, Department
Default Schedule, or Policy Default Schedule. In this way, the Scheduled
Day Off will override and ignore the default schedule for the respective
date and the employee will not receive exceptions on the Scheduled Day
Off. Days Off are a useful feature for companies who utilize the Exception
Points System and wish to ensure employees who are approved for an absence
will not be penalized.

![](/img/image-404.png)

Insert
â Adds a blank record to the Trained Tasks tab for the respective employee.
Select the Trained Task Description for which the employee has been trained
and then enter the hourly wage which the employee receives for the respective
trained task.

![](/img/image-404.png)

Schedule
Date - Enter the date you wish to add a day off for by typing in
the Schedule Date Field or using the Calendar Button.

Only
for Schedules That Start and End on Day Off - The Only for
Schedules that Start and End of Day off option is used to distinguish
between overnight or day time employees. If the employee's default
schedule is a Day Time Schedule that does not cross midnight then check
'Only for Schedules that Start and End on Day Off.' If the employee's
default schedule crosses midnight, do not check 'Only for Schedules that
Start and End on Day Off. The table below lists examples of employee schedules
and shows whether the 'Only For Schedules that Start and End on Day Off'
button should be checked.

| Employee Default Schedule for Date of Schedule Day Off | Status of 'Only For Schedules that Start and End on Day off' option. |
| 6:00 AM - 3:00 PM | Checked |
| 8:00 AM - 5:00 PM | Checked |
| 12:00 PM - 8:00 PM | Checked |
| 3:00 PM - 11:00 PM | Checked |
| 5:00 PM - 2:00 AM | Unchecked |
| 6:00 PM - 3:00 AM | Unchecked |
| 7:00 PM - 4:00 AM | Unchecked |
| 11:00 PM - 7:00 AM | Unchecked |

Note: Remember, it is important that the 'Only
for Schedules That Start and End on Day Off' option be checked if the
employee's schedule does not cross midnight for the Schedule Date! This
option is used by InfiniTime to differentiate between Schedules that cross
midnight and those that do not.

Change
- Deletes the selected Trained Task from the employee's profile. If a
trained task is removed from an employee's profile, the employee will
not be listed as available on the Use Skeleton Window or the Find Available
Window for the respective trained task.

Delete
- Deletes the selected Trained Task from the employee's profile. If a
trained task is removed from an employee's profile, the employee will
not be listed as available on the Use Skeleton Window or the Find Available
Window for the respective trained task.

### Valid Department Section

The Valid Department Section of the Employee Update Form permits the
InfiniTime Administrator
to define specific Departments for which the respective employee is approved
to work. In some organizations, certain departments are configured for
additional pay premiums. The Valid Departments list, in conjunction with
the Invalid Department Exception, can assist supervisors with identifying
employees who inadvertently or intentionally punch into a department which
they have not been previously approved for.

![](/img/image-404.png)

Insert
â Opens the Employee Valid Department Update Form. Type the first few
characters of the desired department and click OK to set the Department
as a Valid Department for the respective employee.

![](/img/image-404.png)

Change
- Opens the Employee Valid Department Update Form for the selected Valid
Department. The InfiniTime
Administrator may then change the department as desired using either auto
fill or the Lookup Magnify Glass..

Delete
- Deletes the selected Valid Department from the employee's profile.

### Valid Telephone Numbers Section

The Valid Telephone Numbers Section of the Employee Update form is displayed
for customers who have purchased the Telephone Punch Module. Telephone
Punch permits employees to punch in and out via telephone by calling into
an interactive voice menu and making specific selections to punch or enter
other activity. The Valid Telephone Numbers Section of the Employee Update
Form permits InfiniTime
Administrators to define specific phone numbers which the respective employee
may call into the Telephone Punch interactive voice menu from. InfiniTime can then automatically
prevent employees from punching in or out using caller ID Services to
determine the phone number the employee is calling from.

![](/img/image-404.png)

Insert
â Opens the Valid Telephone Number Update Form. First enter the valid
phone number on the General Tab which the employee is permitted to call
from. Then click on the Default Schedule Tab and create a schedule to
describe the time frame the employee may call from the respective phone
number. Defining Schedules for a valid telephone number is optional. If
no schedule is defined, the Telephone Punch Interactive Voice Menu will
accept calls from the respective phone number 24x7.

![](/img/image-404.png)

Change
- Opens the Valid Telephone Number Update Form for the selected Valid
Telephone Number. The InfiniTime
Administrator may then make changes to either the Telephone Number or
the associated schedule as desired.

Delete
- Deletes the selected Valid Telephone Number from the employee's profile.

### User Defined Fields Section

The User Defined Fields Section permits entry of employee specific values
for User Defined Fields, as defined on the User Defined Fields Table.
User Defined Fields provide InfiniTime
Administrators with the ability to track additional employee information
that is not a part of the software by default. This can be useful for
tracking information that may be specific to your industry, such as Drivers
License numbers and type for transportation related companies.

![](/img/image-404.png)

Change
- Opens the Employee User Defined Field Update Form for the selected User
Defined Field. The InfiniTime
Administrator may then enter the desired value for the respective employee.
The Employee User Defined Field Update Form appears slightly differently
depending on the Field Type of the selected User Defined Field. For example,
Character User Defined Fields have a simple text box. Simply enter the
desired value to store in the employee's record. List User Defined Fields
have a drop down, click on the drop down to select the employee's assigned
value from the list. Document Fields prompt the user to select the desired
document from the hard disk to be stored in the InfiniTime
Oracle Database.

### Wages Section

The Wages Section of the Employee Profile permits entry of employee
specific alternate wages for specific Department, Job, and Task combinations.
In this way, employees can be rewarded for performing specific tasks for
filling certain roles. Additionally, Alternate Wages can also be defined
for a specific period of time. During that time period, all hours worked
in the specified Department / Job / Task will be paid at the specified
hourly wage. It is important to note that Alternate Wages are employee
specific and must be configured for each individual employee. Alternate
wages effect calculations as displayed on InfiniTime
Payroll Summary and Payroll Detail reports as well as Payroll Export formats
which export employee wages.

![](/img/image-404.png)

Insert
â Opens the Employee Wage Update Form as shown below.

![](/img/image-404.png)

Department
- If the employee must work in a specific
department to be eligible for the wage, specify the department here by
entering the first few letters of the department name or select the department
from the Department Table using the Lookup Magnify Glass.

Job
-  If the employee must work in
a specific job to be eligible for the wage, specify the job here by entering
the first few letters of the job name or select the job from the Job Table
using the Lookup Magnify Glass.

Task
-  If the employee must work in
a specific task to be eligible for the wage, specify the task here by
entering the first few letters of the task name or select the task from
the Task Table using the Lookup Magnify Glass.

Pay
Method - Select the appropriate pay
method for use with the wage.

Amount
- Enter the desired Hourly, Salary
(Per Pay Period), or Per Diem Dollar Amount to be awarded when the employe
works in the respective Department / Job / Task combination.

Valid
From Date - The Valid From Date and
Valid To Date are combined to create an effective date range for the respective
wage. If the Valid From Date is left blank, the respective alternate wage
will be valid from the employee's hire date to the Valid To Date. If the
Valid From Date is filled, the respective alternate wage will be valid
from the Valid From Date to the Valid To Date.

Valid
To Date - The Valid From Date and Valid
To Date are combined to create an effective date range for the respective
wage. If the Valid To Date is left blank, the respective alternate wage
will be valid from either the employee's hire date or the Valid From Date
to the Current Date. If the Valid To Date is filled, the respective alternate
wage will be valid from the employee's hire date or the Valid From Date
to the to the Valid To Date.

Change
- Opens the Employee Wage Update Form for the selected Alternate Wage.
The InfiniTime Administrator
may then make changes as desired.

Delete
- Deletes the selected Alternate Wage from the employee's profile.

Additional details regarding
use and configuration of Alternate Wages can be found in the [Job Costing Section of this
document.](Configuration/Product_Configuration.md#cnf17_Job_Costing_-_Wages)

### Workers Compensation Section

The Workers Compensation Section of the Employee Update Form permits
InfiniTime administrators
to keep record of incidents which lead to a workers compensation claim.
These details will be kept on record in the employee's profile.

![](/img/image-404.png)

Insert
â Opens the Employee Wage Update Form as shown below.

![](/img/image-404.png)

Case
Description - Input the description of the claim.

Accident
Date - Input the date of the accident.

Lost
Time - Enter the amount of hours lost due to the accident.

Restricted
Duty From - This date is the beginning date of the employee came
back to work but with restrictions on what duties they can perform.

Restricted
Duty To - this date indicates the end of the employees restricted
duty period.

Days
Out of Work - Enter the amount of days the employee lost work.

Return
to work Date - This is the date the employee came back to work.

Return
to Full Duty Date - This is the date the employee may return to
work without restrictions.

Change
- Opens the Employee Wage Update Form for the selected Alternate Wage.
The InfiniTime Administrator
may then make changes as desired.

Delete
- Deletes the selected Alternate Wage from the employee's profile.

### Software Overview - Essential Takeaways

The Software Overview Documentation, as provided above, serves as an
introduction to the use of the InfiniTime
Software and closely mirrors the first training session provided during
the Inception Technologies
Fee Based Implementation process. InfiniTime
Users who have read the Software Overview Documentation should be prepared
to perform the following tasks:

* Create the Employee Profile for all InfiniTime
  Administrators
* Create the Employee Profile for all InfiniTime
  Supervisors
* Confirm all Client Machines are properly configured to access the
  InfiniTime Software
  and / or Delegate this task to your internal IT Personnel
* Manually Enter or Import Employee Details using the Import Tool
* Comfortable navigating throughout the InfiniTime
  User Interface
* Familiarity with the different buttons / items on the Main Toolbar
  and Menu

The above tasks should be performed before proceeding with reviewing
or following the steps and instructions outlined in the Software Configuration
section of this document. Your Inception Technologies
Implementation and / or Client Services Representative can provide direction
if you should have any specific questions. Please refer to the Quick Start
Guide for additional information on the above tasks.