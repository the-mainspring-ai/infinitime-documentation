xml version="1.0" encoding="utf-8" ?





Payroll Export




# Payroll Export Section Overview

## Introduction

Payroll
Export provides users with the option of exporting Employee Hours and
Earnings from InfiniTime
for use in Accounting and Payroll Related Software Suites. This feature
has the capability to drastically reduce and even eliminate the need for
manual data entry into Accounting and Payroll Related Software Suites
which allows Payroll Clerks and HR Managers to focus on business critical
tasks by eliminating a simple task that, without the Payroll Export Process,
must be performed manually requiring significant man hours. InfiniTime's Payroll Export calculates
Gross Employee Hours and Earnings from Employee Timecards and exports
this information to one of several Standard File Formats. The resulting
Payroll Export File can then be imported into Accounting and Payroll Related
Software Suites with support for importing employee hours and earnings
from ASCII File Formats.

Inception Technologies
takes a unique approach to integration with Third Party Accounting and
Payroll Related Software Suites by assisting customerâs with the integration
process during the initial InfiniTime
Implementation through a unique process dubbed Custom Payroll Interface
Review & Design.

## Custom Payroll Interface Review & Design Overview

As of InfiniTime
7.08, predefined Payroll
Export Formats exist within InfiniTime
for over 200 Accounting and Payroll Related Software Suites. Even so,
Inception Technologies
recognizes that the needs of each individual customer vary according to
internal HR and Payroll Practices as well as Time and Attendance Policies
ranging from Hours Costing Requirements and Calculating Overtime Hours
to Calculating Hours and Earnings for both Paid and Worked Holidays. The
Custom Payroll Interface Development Process is designed to ensure all
needs and requirements related to exporting employee hours and earnings
to a Third Party Payroll application are understood by Inception Technologies
Staff and met by the final Payroll Export Format selected for production
use.

| The Custom Payroll Interface Development Process   is documented in the following diagram :  (Click to Download) | In order to meet the diverse needs of our Client Base, InfiniTime provides support for multiple types of hours costing (Referred to as Job Costing by Inception Technologies Representatives and the InfiniTime Help System) in addition to the tracking of Worked Hours (Regular Hours, Overtime Hours), Other Hours (Sick Time, Vacation Time), and Other Amounts (Direct Dollar Amounts such as Tips, Bonus Pay, etc.). In order to effectively configure the InfiniTime Application to export employee earnings and hours to Third Party Payroll Applications such as QuickBooks Pro, Paychex, or ADP a thorough understanding of how a given organization tracks employee hours and earnings â including Hours Costing Categories and Hours Types - is required. |

*Example
Hours Costing Categories*

| Organizational Units (IE: Department) | Geographical Region (IE: City, State, Country, Plant or Site Name, Company) | Managerial Accounting Labor Type (IE: Direct or Indirect) |
| Job Role | Job / Invoice Number | Customer Number |

Categories
& Examples of Hour Types Supported by InfiniTime

For this
reason, the Custom Payroll Interface Review & Design Process includes
a minimum of two one hour Virtual Conferences during which an Inception
Technologies representative will review all Hours Types required by the
Client with the appropriate personnel. In most cases, the Payroll or HR
Manager is the best contact for creating a list of all Hours Costing Categories
and Hours Types tracked for a given organization. Once a list of Costing
Categories and Hours Types is available, the relationship between InfiniTime and the Third Party Payroll
Application â such as QuickBooks Pro, Paychex, or ADP â must be understood.
In some cases, the exact InfiniTime
Payroll Interface Format that will meet the needs of an organization will
depend upon how the Third Party Accounting and / or Payroll Application
is configured for Hours Costing Purposes and what specific functionality,
such as the ability to print employee hours and earnings on the employeeâs
pay stub, is required.

Accounting
and Payroll Related Software Suites with support for importing employee
hours and earnings from an ASCII File Format generally have a standard
template available. The standard template describes the exact fields required
to import employee hours and earnings as well as the syntax and valid
values for each field.

## Custom Payroll Interface Review & Design For Existing Commercial Accounting or Payroll Related Software Suites

If you plan to use an existing
commercial Accounting or Payroll Related Software Suite with InfiniTime, your Payroll Application
Representative should have such a template available. Simply contact your
Payroll Application Vendor, explain you are working with a Time and Attendance
Software Vendor who is interested in exporting employee hours and earnings
to their Payroll Application, and request a â***field by field layout for importing
employee hours from a comma delimited, tab delimited, or fixed length
ASCII File.â*** Generally, you will receive a PDF similar to the
document below.

*Technical Note: A Field by Field Layout for
importing Employee Hours and Earnings may\* be found in the Help Documentation
included with your Accounting or Payroll Related Software Suite.*

## Custom Payroll Interface Review & Design For In House Accounting or Payroll Related Solution

If you plan to use the Payroll
Export file for internal use only with an In House Accounting or Payroll
Related Solution please create a spreadsheet detailing the required format
for the final file. Include a column in the spreadsheet for each field
you would like placed in the export in addition to formatting information
such as the number of required decimals, date format, justification requirements,
etc. as necessary for each field.

An example layout for a custom payroll interface
request is provided below.

***A template must be provided
to Inception Technologies for your Custom Payroll Interface Request to
be processed.***

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Example Payroll Export Layout** | | | | |
| **Field Name** | **Description** | **Data Type** | **Format** | **Notes** |
| TECHNO | Employee ID - Data in UPPERCASE and must match TECHNO in VisionPoint | Alphanumeric | N/A | Enclosed in quotes. |
| REGHRS | Regular Hours | Numeric | 1234.00 | 2 Decimal Places / Show Decimal |
| OVTHRS | Overtime Hours | Numeric | 1234.00 | 2 Decimal Places / Show Decimal |
| VACHRS | Vacation Hours - Mapped Amount 1 | Numeric | 1234.00 | 2 Decimal Places / Show Decimal |
| PERHRS | Personal Hours - Mapped Amount 2 | Numeric | 1234.00 | 2 Decimal Places / Show Decimal |
| HOLHRS | Holiday Hours - Mapped Amount 3 | Numeric | 1234.00 | 2 Decimal Places / Show Decimal |
| BERHRS | Bereavement Hours - Mapped Amount 4 | Numeric | 1234.00 | 2 Decimal Places / Show Decimal |
| SCKHRS | Sick Hours - Mapped Amount 5 | Numeric | 1234.00 | 2 Decimal Places / Show Decimal |
| STRHRS | Straight Time Hours - Mapped Amount 6 | Numeric | 1234.00 | 2 Decimal Places / Show Decimal |
| SDATE | Start Date - From Date of payroll export | Date | MM/DD/YYYY |  |
| EDATE | End Date - To Date of payroll export | Date | MM/DD/YYYY |  |

## Payroll Export User Interface Overview

InfiniTime permits an unlimited number
of Payroll Exports to be configured. While most InfiniTime
Clients will require only a single Payroll Export Setting, multiple Payroll
Exports can be configured to support the following scenarios:

* Exporting
  Employee Hours Earnings for Different Groupings of Employees to separate
  files (IE: By Department, Company, Location, Pay Type, etc.)
* Exporting
  Employee Hours and Earnings for Different Date Ranges
* Exporting
  Employee Hours and Earnings to Different Payroll Interface Formats
* Exporting
  Employee Hours and Earnings with different sets of Payroll Codes for
  Working Hours (IE: Direct Labor Employees may have different Payroll
  Codes than Indirect Labor Employees)
* Exporting
  Employee Hours and Earnings to the Same Payroll Interface Format with
  different values for Prompts on the Required Info. Tab of the Payroll
  Interface Update Form

### Accessing the Payroll Export Table

1. Log Into the Manager Module
2. Click on Tools
3. Click on Import / Export

![](/img/image-404.png)

4. Click
   on Payroll Export

### Payroll Export Update Form

Â·        Click
Insert on the Payroll Export Table to Open the Payroll Export Update Form.

![](/img/image-404.png)

* The
  Payroll Export Update Form displays Payroll Export related options
  and settings. Required settings have a blue background and must be
  completed before the Payroll Export can be saved.

![](/img/image-404.png)

* The
  following settings and options are available on the Payroll Export
  Update Form:

### General Tab

The General Tab of the Payroll Export Update Form
includes General and Output related options. General Options include the
Payroll Export Description, Payroll Export Date Range, Payroll Export
Employee Filter, and Payroll Export Format which define the payroll export
and control the date range and set of employees for which hours and earnings
will be exported. Output Options on the General Tab include the Payroll
Export File Name, Send File via FTP, and PGP Encrypt File which control
how the final Payroll export is distributed to interested parties such
as internal staff or a third party company which will process payroll
for your organization.

1. Description â Enter a descriptive name
   for the Payroll Export entry. This description will be listed in the
   Payroll Export Table.
2. Inactive â Sets the Payroll Export Entries
   status to inactive. The payroll export can no longer be exported and
   all fields will be grayed out.
3. Date Range â Specify the date range for
   Employee Hours and Earnings to be exported from.
4. Format â Select the format that corresponds
   to the Accounting or Payroll Application Suite which the final Payroll
   Export file will be imported into. If a Custom Payroll Interface was
   developed for your organization, the Payroll Export Interface Format
   name will be provided by your Implementation Representative or a Client
   Services representative upon completion of the Custom Payroll Interface
   Review & Design Process. If your Accounting or Payroll Application
   Suite is not listed, please contact your Inception Technologies Sales
   Associate.
5. File Name â Specify a name for the final
   payroll export file you would like to create. The File Name must include
   the three character file extension (IE: PayrollExport.csv). The final
   payroll export file will be transferred via FTP if âSend File Via
   FTPâ is enabled and / or emailed to the email recipients defined on
   the Email Tab. If âSend File Via FTPâ is not enabled and no Email
   Recipients are defined the user will be prompted to either open or
   save the Payroll Export file.

Technical Note: Full Details on how the final Payroll
Export File Output is directed can be found in the Payroll Export Logic
Flow Diagram.

6. PGP Encrypt File - In order to provide
   maximum security for sensitive information such as employee demographics
   and banking information, an encryption algorithm has been integrated
   into the InfiniTime
   Software. PGP includes an extensive suite of encryption tools featuring
   a combination of public key and conventional cryptography providing
   improved security without a decrease in performance or usability.
   PGP can be used across unsecure networks to secure data from access
   by unauthorized users. With the integration of PGP all files entering
   and exiting the InfiniTime
   environment can be encrypted to safeguard sensitive information. To
   learn more about PGP and how to configure it please see Chapter X
   Security PGP Encryption.
7. Send File Via FTP â Use this feature
   to automatically transfer the file via FTP (File Transfer Protocol)
   to a destination of your choice. A set of related fields will become
   available and must be filled out. Configuration examples are shown
   below. Keep the items that follow in mind when entering this information.

* A domain
  name or IP Address can be used in the Host Address Field.
* Do
  not include the ftp:// prefix in the Host Address Field.
* The
  Directory field can be left blank if you are uploading to the root
  of the FTP Site.
* If
  you wish to upload to a specific folder on the FTP site you must specify
  the full path using a preceding forward slash ( / ) as shown in the
  image below.
* The
  Login Name can be a Local Windows Account, a Domain Account, or Anonymous.
  Enter the Login Name in one of the following formats:

Local
Windows Account:

![](/img/image-404.png)

Enter
the Host Address. There are three valid formats for the host address field
as listed below. **Do not include the ftp:// prefix in this field.**

| Valid Host Address Formats | |
| Format Type | Example |
| Private IP Address | 192.168.1.20 |
| Public IP Address | 70.167.196.165 |
| Domain Name | www.InfiniTime.com |

1. Enter
   the Directory. Remember to include a preceding forward slash as shown.
2. Enter
   the Login Name in the following format:

"HOSTNAME\USER"

3. For
   Example if your FTP Server's hostname is FTPSERVER and the user you
   wish to connect as is FTPUSER then you would enter the following:

FTPSERVER\FTPUSER

4. Enter the user's
   password.
5. Specify
   the port to use when connecting to the FTP Server. This does not generally
   need to be altered.

Domain Accounts:

![](/img/image-404.png)

1. Enter the Host Address. There are three valid
   formats for the host address field as listed below. **Do not include
   the ftp:// prefix in this field.**

| Valid Host Address Formats | |
| Format Type | Example |
| Private IP Address | 192.168.1.20 |
| Public IP Address | 70.167.196.165 |
| Domain Name | www.InfiniTime.com |

2. Enter the Directory.
   Remember to include a preceding forward slash as shown.
3. Enter
   the Login Name in the following format:

"DOMAIN\USER"

4. For
   Example if your FTP Server's domain is InfiniTime
   and the user you wish to connect as is FTPUSER then you would enter
   the following:

InfiniTime\FTPUSER

5. Enter
   the user's password.
6. Specify
   the port to use when connecting to the FTP Server. This does not generally
   need to be altered.

Anonymous User:

![](/img/image-404.png)

1. Enter the Host Address. There are three valid
   formats for the host address field as listed below. **Do not include
   the ftp:// prefix in this field.**

| Valid Host Address Formats | |
| Format Type | Example |
| Private IP Address | 192.168.1.20 |
| Public IP Address | 70.167.196.165 |
| Domain Name | www.InfiniTime.com |

2. Enter the Directory.
   Remember to include a preceding forward slash as shown.
3. Enter
   Anonymous as the Login Name
4. Enter
   the user's password.
5. Specify
   the port to use when connecting to the FTP Server. This does not generally
   need to be altered.

Technical
Note: Microsoft IIS includes an option to permit only anonymous connections
to an FTP Site. If this option is checked as shown below only anonymous
connections to the FTP Site will be allowed. This means ANYONE can access
the payroll export file. This option should be unchecked and it should
be confirmed that a login is required to gain read or write access to
the directory where the Payroll Export File will be uploaded. Please contact
your Information Technology Personnel for assistance with checking file
permissions on your FTP Site.

![](/img/image-404.png)

Technical Note: InfiniTime
attempts to connect to the FTP Site to validate the Login ID, Password,
and Directory when the OK Button is clicked on the Payroll Export Update
Form. If InfiniTime is
unable to successfully connect to the FTP Site with the provided login
information, or if the specified directory does not exist, an error will
be displayed.

### Payroll Codes Tab

Many Accounting
and Payroll Software Suites use Payroll Codes to refer to specific Hours
Types. The Payroll Codes Tab allows the user to define Payroll Codes for
Working Hours to be used with the Selected Payroll Interface Format. Payroll
Codes vary from company to company depending on how the Accounting or
Payroll Application Suite is configured.

It is important
to note that not all Payroll Interface Formats and their related Accounting
and Payroll Software Suites utilize Payroll Codes. As required fields,
the Payroll Codes for Regular, Overtime One, Overtime Two, Overtime Three,
and Overtime Four Hours must be filled. If your chosen Payroll Interface
does not utilize Payroll Codes, simply set the Payroll Code fields to
a value of âNAâ.

*NOTE: For Instructions on
how to determine if a specific Payroll Interface Format utilizes Payroll
Codes, [see the Payroll Interface
Layout Report](../Reports/Reports.md#rpt57_Payroll_Interface_Layout) for additional details.*

### 

1. Regular Hours Payroll Code
   â Enter the Payroll Code to be associated with Regular Hours.
2. Overtime One Payroll Code
   â Enter the Payroll Code to be associated with Overtime Four.
3. Overtime Two Payroll Code
   â Enter the Payroll Code to be associated with Overtime Four.
4. Overtime Three Payroll Code
   â Enter the Payroll Code to be associated with Overtime Four.
5. Overtime Four Payroll Code
   â Enter the Payroll Code to be associated with Overtime Four.

### Email Tab

The Email Tab allows the user to send the final Payroll Export file
to interested parties such as internal staff or a third party Payoll Processing
Company via email. The following fields are present on the Email Tab of
the Payroll Export Update Form:

1. From - Type in the email
   address of the sender, if a recipient wants to reply to the email
   they can do so, and it will get back to the original sender.
2. Subject â Type a subject
   for the email.
3. Body Text â Type your message
   in this field.
4. Sent To â The sent to grid
   displays all recipients that the payroll export will be sent to. Recipients
   are inserted by using the Insert button.
5. Insert â Used to insert
   a new Email Recipient as shown below.

![](/img/image-404.png)

The Payroll Export Email Update Form adds email recipients to the Payroll
Export Update Form for a specific Payroll Export. Simply enter the Name
(Email To Name) and Email Address (Email To Address) of the person you
wish to email the final Payroll Export File to and click OK to save the
Email Recipient.

### Auto Export Schedule Tab

Auto
Export Schedules can be defined to automatically output the Final Payroll
Export file. The Payroll Export File will automatically be emailed, sent
via FTP, or simply placed in the Output Folder as appropriate based on
Output Options configured for the Payroll Export Setting. One or more
Auto Export Schedules can be defined for a single Payroll Export Setting,
such that the payroll export is automatically exported at different time
intervals as outlined below.

1. **Insert**
   - Opens the Auto
   Payroll Export Schedule Update Form. Used to insert an automatic export
   schedule

![](/img/image-404.png)

2. **Description**â
   Enter a descriptive name for the payroll export. This description
   will be listed in the Auto Export Schedule Grid.
3. **Created By** â Displays the name of
   the Employee that Created the Schedule.
4. **Frequency** â Choose the Time Interval
   for how often you would like InfiniTime
   to automatically export this record. For example, the Weekly Frequency
   will automatically perform the payroll export once per week on the
   specified day and time.
5. **Time to Export**â Specify the Time
   you would like InfiniTime
   to automatically export this record.
6. **Day of Week to Export** â Specify
   the day of week you would like InfiniTime
   to automatically export this record.
7. **Date Last Exported** â Displays the
   date of the last automatic export.
8. **Time Last Exported** â Displays the
   time of the last automatic export.
9. **Date to Export Next** â Specify the
   next date you would like InfiniTime
   to export the record.
10. **Time to Export
    Next** â Specify the next time you would like InfiniTime
    to export the record.

### Options Tab

The Payroll Export Options Tab includes several options which alter
the Payroll Export Processing in specific ways. A brief description of
each Processing Related Option is outlined below. The [Payroll
Export Logic Flow Diagrams](Payroll_Export.md#pxh77_Payroll_Export_Input:) provide additional detail on how each Processing
Related Option functions.

![](/img/image-404.png)

1. Only
   Export Records For the Non-Default Department - Only Timecard
   Activity Records that are associated to a department other than the
   employeeâs default department will be exported if this option is checked.
2. Department
   Selector Filters Time Instead of Employee - Changes the
   Employee Filter button Functionality. Selecting departments will cause
   InfiniTime to export
   only Timecard Activity from those departments if this option is checked.
   Normally the Employee Filter button would specify employees in a specific
   department when a department was selected.
3. Assign
   All Time To Employees Default Department - All Timecard
   Activity will be associated with the Employeeâs default department
   regardless of what department the employee was clocked into if this
   option is checked.
4. Alert
   When Unreviewed Exceptions Are Found For Exported Employees
   - InfiniTime will alert
   the user if any un-reviewed exceptions are found during the export
   process for the employees specified by the Employee Filter. InfiniTime first identifies employees
   indicated by the employee filter on the payroll export and determines
   if any employees have exceptions that are not marked as reviewed.
   If an un-reviewed exception is found the following warning is displayed:

![](/img/image-404.png)

 The
warning above is followed immediately by a list of all employees with
un-reviewed exceptions.

![](/img/image-404.png)

You
may choose to continue with the export or cancel the export after closing
the list of employees with unreviewed exceptions as shown below.

![](/img/image-404.png)

5. **Alert
   When Timecards Are Not Reviewed By Employee's Supervisor For Exported
   Employees** -
   InfiniTime will alert
   the user if any un-reviewed Timecards by the employee's supervisor
   are found during the export process for the employees specified by
   the Employee Filter. InfiniTime
   first identifies employees indicated by the employee filter on the
   payroll export and determines if any employees have timecard activity
   that has not been marked as reviewed by their supervisor. If an un-reviewed
   activity record is found the following warning is displayed:

![](/img/image-404.png)

## The warning above is followed immediately by a list of all employees with un-reviewed timecard activity.

![](/img/image-404.png)

You may choose
to continue with the export or cancel the export after closing the list
of employees with un-reviewed timecard activity as shown below.

![](/img/image-404.png)

6. **Alert
   When Timecards Are Not Reviewed By Employee For Exported Employees
   -** InfiniTime
   will alert the user if any un-reviewed Timecards by the employee are
   found during the export process for the employees specified by the
   Employee Filter. InfiniTime first identifies employees indicated by
   the employee filter on the payroll export and determines if any employees
   have timecard activity that has not been marked as reviewed by the
   employee itself. If an un-reviewed activity record is found the following
   warning is displayed:

![](/img/image-404.png)

The
warning above is followed immediately by a list of all employees with
un-reviewed timecard activity.

![](/img/image-404.png)

You
may choose to continue with the export or cancel the export after closing
the list of employees with un-reviewed timecard activity as shown below.

![](/img/image-404.png)

7. **Alert
   When Number of Reviews are Less Than X For Exported Employees
   -** InfiniTime will
   alert the user if any Timecards have not been reviewed at least X
   times for an employee included in the Payroll Export Employee Filter.
   InfiniTime first identifies
   employees indicated by the employee filter on the payroll export and
   determines if any employees have timecard activity that has not been
   marked as reviewed x amount of times. If an activity record is found
   with less than the required number of reviews, as set on the Options
   Tab, the following warning is displayed:

![](/img/image-404.png)

The warning
above is followed immediately by a list of all employees with un-reviewed
timecard activity.

![](/img/image-404.png)

You
may choose to continue with the export or cancel the export after closing
the list of employees with un-reviewed timecard activity as shown below.

![](/img/image-404.png)

8. **Export
   Overtime as Half Time** â Export Overtime as Half Time alters
   the default method for totaling Regular and Overtime Hours as detailed
   below. The Export Overtime as Half Time feature should be enabled
   if your organizationâs Accounting or Payroll Related Software Suite
   is configured to pay Overtime at Half Time for Salary Employees.

*Default Payroll
Export Functionality:*

|  |  |  |
| --- | --- | --- |
| **Employee Worked Hours** | | |
| **Hours** | **Hours Type** | **Description** |
| 40 | Regular Hours | Worked Hours â Regular Hours Less than 40 Per Week. |
| 12 | OT1 Hours | Weekly Overtime > 40 Hours Per Week |
| 8 | OT2 Hours | Saturday Regular Hours - Day of Week Overtime |
| 1 | OT3 Hours | Saturday Overtime Hours â Day of Week Overtime |
| 3.25 | OT4 Hours | Sunday Regular Hours â Day of Week Overtime |

|  |  |
| --- | --- |
| **Exported Hours Totals** | |
| **Hours** | **Hours Type** |
| 40 | Regular Hours |
| 12 | OT1 Hours |
| 8 | OT2 Hours |
| 1 | OT3 Hours |
| 3.25 | OT4 Hours |

*Export
Overtime as Half Time Functionality:*

|  |  |  |
| --- | --- | --- |
| **Employee Worked Hours** | | |
| **Hours** | **Hours Type** | **Description** |
| 40 | Regular Hours | Worked Hours â Regular Hours Less than 40 Per Week. |
| 12 | OT1 Hours | Weekly Overtime > 40 Hours Per Week |
| 8 | OT2 Hours | Saturday Regular Hours - Day of Week Overtime |
| 1 | OT3 Hours | Saturday Overtime Hours â Day of Week Overtime |
| 3.25 | OT4 Hours | Sunday Regular Hours â Day of Week Overtime |

|  |  |
| --- | --- |
| **Exported Hours Totals** | |
| **Hours** | **Hours Type** |
| 64.25 | Total Working Hours |
| 12 | OT1 Hours |
| 8 | OT2 Hours |
| 1 | OT3 Hours |
| 3.25 | OT4 Hours |

When Export Overtime as Half Time is enabled, Employee Hour Totals are
altered as follows:

Total Working Hours, calculated as shown
below, are exported in place of Regular Hours. This is illustrated with
red shading the tables above.

Total Working Hours =
Regular Hours + Overtime 1 Hours + Overtime 2 Hours + Overtime 3 Hours
+ Overtime 4 Hours

It should be noted that the Pay Rate for
Regular, Overtime 1, Overtime 2, Overtime 3, and Overtime 4 Hours Types
is determined by the customerâs Accounting / Payroll Related Software
Suite. InfiniTime Payroll
Reports do not take âExport Overtime as Half Timeâ into account when calculating
Gross Wages within InfiniTime.

An
example of Salary Gross Wage Calculations, as performed by a Payroll Application
Configured for âHalf Timeâ according to the Fair Labor Standards Act (FLSA)
is shown below.

|  |  |  |
| --- | --- | --- |
| **Employee Worked Hours** | | |
| **Hours** | **Hours Type** | **Description** |
| 40 | Regular Hours | Worked Hours â Regular Hours Less than 40 Per Week. |
| 12 | OT1 Hours | Weekly Overtime > 40 Hours Per Week |

|  |  |  |  |
| --- | --- | --- | --- |
| **Exported Hours Totals** | | | |
| **Hours** | **Hours Type** | **Calculated Hourly Wage (Assuming Weekly Salary of $750.00)** | **Gross Wages** |
| 52 | Total Working Hours | $750.00 / 52 Hrs = $14.423 / Hr | $750.00 |
| 12 | OT1 Hours | $14.423 \* 0.5 = $7.212 / Hr | $86.54 |
| Total Gross Wages | | | $836.54 |

Notice how Total Working Hours
are exported and paid at the employeeâs Weekly Salary of $750.00. The
Employeeâs Regular Hours Wage ($14.423) is then calculated by dividing
the employeeâs weekly salary ($750.00) by the Total Working Hours (52).
The resulting Regular Hours Wage ($14.423) is then halved to determine
the Half Time Premium Wage of $7.212. Gross Wages for Half Time Pay are
then calculated by multiplying the Half Time Premium Wage ($7.212) by
the number of Overtime Hours (12) for a total of $86.54.

9. **Include
   Employees Terminated During The Export Range** - This option allows you to
   export hours for employees that have been terminated during the date
   range of the payroll export. By default, when this option is not checked,
   hours for inactive employees will not be exported even if they were
   terminated during the Payroll Export Date Range.

***N**ote: The Payroll
Export specifically checks inactive employees included in the Payroll
Export Employee filter to determine if they were terminated during the
Payroll Export Date Range. Hours and Earnings will not be exported for
employees terminated during the Payroll Export Date range who are not
included in the Payroll Export Employee Filter.*



10. **Pay
    Shift Differential Hours at Differential Pay Only** â
    Pay Shift Differential Hours as Differential Pay Only alters the method
    for totaling Non Differential Hours and Differential Hours as detailed
    below. This option is only compatible with Payroll Interfaces of the
    âShift Activity / Periodâ and âShift Activityâ record format.

*Default Payroll
Export Functionality:*

|  |  |  |  |
| --- | --- | --- | --- |
| **Employee Worked Hours** | | | |
| **Hours** | **Hours Type** | **Shift** | **Description** |
| 12 | Regular Hours | No Shift Differential | Worked Hours â Regular Hours Less than 40 Per Week. No Differential. |
| 28 | Regular Hours | Night Shift | Worked Hours â Regular Hours Less than 40 Per Week. Night Differential (Hours Worked Between 7:00 PM and 7:00 AM). |
| 3 | OT1 Hours | No Shift Differential | Weekly Overtime > 40 Hours Per Week. No Differential. |
| 12 | OT1 Hours | Night Shift | Weekly Overtime > 40 Hours Per Week. Night Differential (Hours Worked Between 7:00 PM and 7:00 AM). |

| **Exported Hours Totals** | | | |
| **Hours** | **Hours Type** | **Pay Rate** | **Gross Wages** |
| 12 | Regular Non Differential Hours | $10.00 | $120.00 |
| 3 | OT1 Non Differential Hours | $15.00 | $45.00 |
| 28 | Regular Night Shift Differential Hours | $11.00 | $308.00 |
| 12 | OT1 Night Shift Differential Hours | $16.50 | $18.00 |
| **Total Gross Wages** | | | **$671.00** |

*Notice
how one record is exported for each combination of Hours Type and Shift
Differential. This is the standard Payroll Export Functionality for Payroll
Interface Format with a Shift Activity / Period Record Format. Additional
Information about Payroll Interface Format Record Formats can be found*
*here.* *(->
Payroll Interface Format Report)*

*Pay
Shift Differential Hours at Differential Pay Only Functionality:*

|  |  |  |  |
| --- | --- | --- | --- |
| **Employee Worked Hours** | | | |
| **Hours** | **Hours Type** | **Shift** | **Description** |
| 12 | Regular Hours | No Shift Differential | Worked Hours â Regular Hours Less than 40 Per Week. No Differential. |
| 28 | Regular Hours | Night Shift | Worked Hours â Regular Hours Less than 40 Per Week. Night Differential (Hours Worked Between 7:00 PM and 7:00 AM). |
| 3 | OT1 Hours | No Shift Differential | Weekly Overtime > 40 Hours Per Week. No Differential. |
| 12 | OT1 Hours | Night Shift | Weekly Overtime > 40 Hours Per Week. Night Differential (Hours Worked Between 7:00 PM and 7:00 AM). |

| **Exported Hours Totals** | | | |
| **Hours** | **Hours Type** | **Pay Rate** | **Gross Wages** |
| 40 | Total Regular Hours | $10.00 | $400.00 |
| 15 | Total OT1 Hours | $15.00 | $225.00 |
| 28 | Regular Differential Hours | $1.00 | $28.00 |
| 12 | OT1 Differential Hours | $1.50 | $18.00 |
| **Total Gross Wages** | | | **$671.00** |

**W**hen
âPay Shift Differential Hours at Differential Pay Onlyâ is enabled, Employee
Hour Totals are exported as follows:

Â·       For Each Employee with Timecard
Records during the Payroll Export Date Range:

o   Export Total Regular Hours
During the Payroll Export Date Range

o   Total OT1 Hours During the
Payroll Export Date Range

o   Total OT2 Hours During the
Payroll Export Date Range

o   Total OT3 Hours During the
Payroll Export Date Range

o   Total OT4 Hours During the
Payroll Export Date Range

o   Regular Shift Differential
Hours During the Selected Date Range

o   OT1 Shift Differential Hours
During the Selected Date Range

o   OT2 Shift Differential Hours
During the Selected Date Range

o   OT3 Shift Differential Hours
During the Selected Date Range

o   OT4 Shift Differential Hours
During the Selected Date Range

This record format allows
employers to pay Total Regular Hours at the Employees Base Rate, Overtime
1 through Overtime 4 Hours at the appropriate Overtime Rate, and
Shift Differential Hours at the Shift Differential Additional Pay Amount
or Additional Pay Percent.

*Technical
Note: The Rate Shift Differential Pay Method is not supported by âPay
Shift Differential Hours at Differential Pay Onlyâ. Only the Additional
Pay Amount or Additional Pay Percent Pay Methods are supported by this
feature.*

11. **Override
    Pay Codes with Shift Pay Codes â** This
    option alters the way Payroll Codes are exported for Working Hours
    with Shift Differential and is only available for Payroll Interfaces
    with the âShift Activityâ, âShift Activity / Periodâ, or âShift Mappedâ
    Payroll Interface Record Formats which support Shift Differentials.
    The ability to Override Payroll Codes with Shift Pay Codes is intended
    for use with Payroll Interfaces which contain the âActivity Typeâ
    Field but do not include the âShift Codeâ Field. In this scenario,
    when Override Pay Codes with Shift Pay Codes is enabled Shift Identifiers
    will be exported in place of the Working Hours Pay Code for the respective
    Hours Type. Shift Identifiers should be configured to include the
    Shift Code and the Hours Type Payroll Code. Examples of how the âOverride
    Pay Codes with Shift Payâ Option can be used are provided below.

ABC
Company has two Shift Differentials, Night Shift Differential and Sunday
Differential. Shift Identifiers are shown below for the Payroll Interface
Format *âCNHS (Atlantic Coast Detail)â*
which includes separate columns for Payroll Codes (*Payroll
Export Field Name: âActivity Typeâ*) and Shift Identifiers (*Payroll
Export Field Name âShift Codeâ*)*.*

![](/img/image-404.png)

For
Payroll Interface Formats which include the âActivity Typeâ Field and
the âShift Codeâ Field, Shift Identifiers should be a single value for
all Worked Hours Types. Additionally, the âShift Identifier Overrides
Payroll Codeâ Company Option should be unchecked. This configuration allows
the final Payroll Export File to show the Shift Code in a Separate Column
from the Activity Type. ABC Companyâs configuration, as detailed [in the Payroll Export Features
& Related InfiniTime
Configuration Review](Payroll_Export.md#pxh40_Payroll_Export_Features___Related_InfiniTime_Configuration_Review), is shown above for *the
CNHS (Atlantic Coast Detail)* Payroll Interface Format which includes
both the âActivity Typeâ Field and the âShift Codeâ Field, uses these
settings.
  

For Payroll
Interface Formats which include only the âActivity Typeâ Field, Shift
Identifiers should be set to include both the Worked Hours Payroll Code
and the Shift Code. In this scenario, the âOverride Pay Codes with Shift
Pay Codesâ Payroll Export Option should be checked. This configuration
allows the final Payroll Export File to override the Working Hours Pay
Code in the Activity Type Column with the Shift Code. An example is shown
below.

  
![](/img/image-404.png)   
  

12. **Group
    Level for Export â** This
    option allows the user to specify a Group Level for which the Group
    Description, as assigned to each employee specified in the Payroll
    Export Employee Filter, will be exported. This feature is only supported
    by Payroll Export Formats which include the Payroll Export Field titled
    âGroup Description for Group Level in Export Headerâ.

## Payroll Export Configuration Overview

The Payroll
Export serves as the primary recurring deliverable provided by the InfiniTime Time and Attendance application.
With this in mind, the Payroll Export is related to multiple areas within
the InfiniTime Software.
To ensure the final payroll export file can be imported into the customerâs
Accounting or Payroll Software Suite without issue, configuration for
several items within InfiniTime
should be confirmed. Details on reviewing InfiniTime
Configuration for Payroll Export Purposes are provided below.

## Payroll Export Features & Related InfiniTime Configuration Review

Before
configuring a payroll export, the user should have an understanding of
what types of information they wish to transfer to their Accounting or
Payroll Software Suite. Available Payroll Interface features are listed
below, some of which are optional. Your organization may choose to implement
one or more of the features below, though it should be noted that some
Payroll Interface Formats do not support all available features. Additional
information on determining which features are supported for a specific
Payroll Interface Format can be found in the [Report
Library Section](../Reports/Reports.md#rpt57_Payroll_Interface_Layout) of this document*.*

### Payroll Interface Features

|  |  |
| --- | --- |
| **Feature** | **Required?** |
| Unique Employee Identifier | Yes |
| Ability to Track Earnings & Hours:   1. By    Payroll Code Only 2. By    Payroll Mapping Number 3. By    Pay Code & Hard Coded Fields 4. Hard    Coded | Yes |
| Support for Payroll Interface Specific Prompts (IE: Company Code) | Yes - For Specific Interface Formats Only. |
| Ability to Track Shift Differentials:   * For   Worked Hours Types (IE: Reg, OT1, OT2, OT3, OT4) * For   Specific Other Activity Types which are set to âCount as Worked   Hoursâ | No |
| Job Costing (A.K.A Hours Costing) | No |
| Ability to Export Employee Gross Wages | No |
| Ability to Export Employee Hours to Different Files for specific sets of Employees | No |
| Output Method(s):   1. A    Prompt is Displayed to allow the User to Open or Save the    Final Payroll Export File 2. Final    Payroll Export File is Emailed 3. Final    Payroll Export File is Transferred via FTP 4. Final    Payroll Export File is Placed in Output Folder | Yes |
| Ability to PGP Encrypt Output File | No |
| Ability to Automatically Output the Final Payroll Export File according to a predefined schedule. | No |
| Payroll Export Employee / Timecard Filter Related Processing Options:   * Ability   to export records only for the Non-Default Department * Ability   to Force the Payroll Export Employee Filter to Filter Time   Instead of Employees * Include   Employees Terminated During the Export Range | No |
| Alert Related Payroll Export Processing Options:   * Alert   When Unreviewed Exceptions are Found for Exported Employees * Alert   When Timecards are not reviewed by Employeeâs Supervisor for   Exported Employees * Alert   When Timecards are Not Reviewed by Employee for Exported Employees * Alert   when number of reviews are less than X for Exported Employees | No |
| Interface Specific Payroll Export Processing Options:   * Export   Overtime as Half Time * Pay   Shift Differential Hours at Differential Pay Only * Group   Level for Export | No |
| General Payroll Export Processing Options:   * Assign   All Time to Employeeâs Default Department | No |

### Payroll Interface Features & Related Configuration

***Unique
Employee Identifier***

All
InfiniTime Payroll Interface
Formats include a field which references an employee record within InfiniTime. While nine out of ten
Payroll Interface Formats within InfiniTime
use the Employee ID as the employee identifier some Payroll Interface
Formats use alternative methods for referencing the employee such as:

* Alternate Payroll ID
* Employee Social Security Number

It
is important to understand which field within InfiniTime
is used as the Employee Identifier for your chosen Payroll Interface Format.
Employee values for this field must be set to match the Accounting and
/ or Payroll Applicationâs Unique Employee Identifier. The [Payroll
Interface Layout Report](../Reports/Reports.md#rpt57_Payroll_Interface_Layout) can be used to determine exactly what employee
identifier your chosen payroll interface uses.

***Ability
to Track Earnings & Hours***

*All
Payroll Interface Formats utilize one of three primary methods to show
the number of hours for a specific Earnings or Hours Type. The âEarnings
& Hours Exportâ methods are outlined below. A few things to keep in
mind regarding the Earning & Hours Export Method are:*

* *Each method requires specific items to
  be configured within InfiniTime
  for the Payroll Interface Format to correctly export all Earnings
  and Hours Types.*
* *Each method has a specific indicator which
  can be observed on the [Payroll
  Interface Layout Report](../Reports/Reports.md#rpt57_Payroll_Interface_Layout) which clearly confirms which Earning &
  Hours Export Method is utilized by a Payroll Interface Format.*
* *You can determine which Earning &
  Hours Export Method your Payroll Interface uses with the [Payroll
  Interface Layout Report](../Reports/Reports.md#rpt57_Payroll_Interface_Layout).*

|  |  |
| --- | --- |
| Payroll Export - Earnings & Hours Export Methods | |
| *By Payroll Code Only* | *INDICATOR:  The Payroll Interface Format:*   * *Will   contain a field titled âActivity Typeâ* * *Will   not contain fields titled âMapped â¦â*     *Payroll Codes and Payroll Mapping Codes must be configured. Shift Codes must be configured for Payroll Interface Formats which support Shift Differentials.* |
| *By Payroll Mapping Number* | *INDICATOR:  The Payroll Interface Format:*   * *Will   not contain a field titled âActivity Typeâ* * W*ill contain fields titled âMappedâ¦â* * *May   contain fields for specific Hours and Earning Types such as   âHoliday Hoursâ, âJury Duty Hoursâ, etc.*     *Payroll Mapping Numbers must be configured for Other Activity Types. Other Activity Types* *with the same Payroll Mapping Codes* *can be set to use the same Payroll Mapping Number.*    *Other Activity Descriptions must match Payroll Interface Hard Coded Fields. [A list of Hard Coded Fields can be found here.](Payroll_Export.md#pxh58_Hard_Coded_Payroll_Interface_Fields)* |
| *Hard Coded Payroll Interface Format* | *INDICATOR:  The Payroll Interface Format:*   * *Will   not contain a field titled âActivity Typeâ* * *Will   not contain fields titled âMappedâ¦â* * *Will   contain fields for specific Hours and Earning Types such as   âHoliday Hoursâ, âJury Duty Hoursâ, etc.*     *Payroll Codes can be set to NA for all Hours Types (Reg, OT1, OT2, OT3, OT4).*  **P*ayroll Mapping Numbers can be ignored and do not need to be set to any specific value.*    *Other Activity Descriptions must match Payroll Interface Hard Coded Fields. A list of Hard Coded Fields can be found here.* |

### *By Payroll Code Only*

*The âBy
Payroll Code Onlyâ method uses Payroll Codes to indicate the specific
Hours Type or Earnings Type a record in the Final Payroll Export File
corresponds to. In this way, the Accounting or Payroll Software Suite
can correctly allocate employee hours to the correct Hours / Earnings
Type and pay the correct rate for the number of hours shown in the record.*

If your Payroll Interface utilizes the âBy Payroll Code Onlyâ Earning
& Hours Export method, Payroll Codes must be configured on the [Payroll
Codes Tab of the Payroll Export Update Form](Payroll_Export.md#pxh19_Payroll_Codes_Tab). Additionally, if your
organization tracks Shift Differentials, Shift Identifiers must be configured
on the [General Tab of the
Shift Update Form](../Scheduling/Scheduling.md#shf07_What_is_a_Shift_Identifier_).

**What
is a Payroll Code?** *A Payroll Code is a unique value
that represents a category of pay tracked by an organization. Payroll
codes are generally two to ten characters in length and are created such
that they represent the original category of pay and can be recognized
at a glance. (IE: RH for **R**egular
**H**ours, OT for **O**ver**t**ime). It is important to
have a clear understanding of all categories of pay required for your
companyâs operations before attempting to configure InfiniTimeâs
Payroll Export. Payroll Codes vary from organization to organization just
like Operational, HR, and Accounting Practices.*

**What
is a Shift Identifier?** *A
shift identifier is similar to a Payroll Code, but instead of representing
a single category of pay tracked by an organization, shift identifiers
function as a modifier for other categories of pay by indicating that
an additional dollar amount, an additional percentage of the pay categoryâs
base rate, or an alternate hourly rate should be paid. Shift Identifiers
are used by organizations who track Shift Differentials. Only Payroll
Interface Formats which support Shift Differentials utilize Shift Identifiers.*

Complete
instructions for configuring payroll codes and Shift Identifiers are below.

1. ### List Hours and Earning Types tracked by  your Organization

Working backwards
from Hours and Earning Types defined in your Accounting or Payroll Software
Suite, complete a table similar to that shown below for all Hours and
Earnings Types you wish to track within InfiniTime
for employees. For most companies, this table will include entries for:

+ One
  or more types of Regular Hours
+ One
  or more types of Overtime Hours
+ One
  or more types of Paid or Unpaid Leave Hours
+ One
  or more types of Holiday Pay and Holiday Worked Hours
+ One
  or more types of Shift Differential Hours (If Applicable)
+ One
  or more types of Earnings (Paid as a Dollar Amount)

As an
example, the tables below were completed for ABC Company with Hourly Manufacturing
Employees and Salary Administration Employees whose hours are paid under
different pay codes for managerial accounting purposes. Additionally,
ABC Company pays a Bonus based on output for manufacturing employees,
tracks differential hours for Sunday Hours and Night Shift, differentiates
between Holiday Pay and Holiday Worked Hours, and tracks Weekly Overtime.

|  |  |  |  |
| --- | --- | --- | --- |
| **ABC Company â Payroll Codes** | | | |
| **Payroll Code** | **Description** | **Type\*** | **Base Rate Modifier** |
| RH | Regular Hours for Hourly Employees | Working Hours | 1.0x |
| OT | Weekly Overtime Hours for Hourly Employees | Working Hours | 1.5x |
| SALRH | Regular Hours for Salary Employees | Working Hours | N/A |
| SALOT | Weekly Overtime Hours for Salary Employees | Working Hours | N/A |
| JD | Jury Duty Hours for Hourly Employees | Other Activity Hours | 1.0x |
| PTO | Paid Time Off Hours for Hourly Employees | Other Activity Hours | 1.0x |
| SALJD | Jury Duty Hours for Salary Employees | Other Activity Hours | N/A |
| SALPTO | Paid Time Off Hours for Salary Employees | Other Activity Hours | N/A |
| HP | Holiday Pay Hours for Hourly Employees | Other Activity Hours | 1.0x |
| HWRH | Regular Hours Worked on a Holiday for Hourly Employees | Worked Hours | 1.5x |
| HWOT | Overtime Hours Worked on a Holiday for Hourly Employees | Worked Hours | 2.0x |
| SALHP | Holiday Pay Hours for Salary Employees | Other Activity Hours | N/A |
| SALHWRH | Regular Hours Worked on a Holiday for Salary Employees | Worked Hours | N/A |

|  |  |  |  |
| --- | --- | --- | --- |
| **Shift Identifiers** | | | |
| **Shift Identifier** | **Description** | **Type\*** | **Pay Method** |
| NS | Night Shift Differential | Shift Differential | Additional $1.00 Per Hour |
| SUN | Sunday Differential | Shift Differential | Additional 50% of Base Rate Per Hour |

\*For additional details on Payroll
Code Types [See *Categories
& Examples of Hour Types Supported by InfiniTime
(Payroll Export: Section 1.1.1 Custom Payroll Interface Review & Design
Process)*](Payroll_Export.md#pxh3_Custom_Payroll_Interface_Review___Design_Overview)

2. ### Configure Payroll Codes on the Payroll Codes Tab of the Payroll Export Update Form.

The above example includes two sets of Payroll Codes for Working Hours
(IE: Regular Hours, OT1 Hours, OT2 Hours, OT3 Hours, OT4 Hours â [See the Policy Overtime Tab
for additional information on Overtime Buckets](../Policies/Policy_Overview.md#pol84_OT_General_Tab)). Each Payroll Export
supports only one set of Payroll Codes, as configured on the Payroll Codes
Tab of the Payroll Export Update Form. With this in mind, ABC Company
will need to configure one Payroll Export for Hourly Manufacturing Employees
and one Payroll Export for Salary Administrative Employees as shown below.

![](/img/image-404.png)

*Hourly
Manufacturing Employees*

![](/img/image-404.png)

Notice how
the Payroll Code for OT2 is set to NA since this Overtime Bucket is not
configured within ABC Companyâs Policies. Similarly, OT3 and OT4 are set
to the Regular Hours and Overtime Hours Pay Code for Worked Holiday Hours
respectively. Payroll Codes for OT2, OT3, and OT4 should be configured
as appropriate based on your Policy and Holiday Settings.

*NOTE: Your
[Payroll Codeâs list](Payroll_Export.md#pxh49_List_Hours_and_Earning_Types_tracked_by__your_Organization) would
have additional types of Overtime such as Day of Week Overtime, Consecutive
Day Overtime, or Double Time if you needed OT2.*

*Salary
Administrative Employees*

![](/img/image-404.png)

Notice how
the Payroll Code for OT2 is set to NA since this Overtime Bucket is not
configured within ABC Companyâs Policies. Similarly, OT3 and OT4 are set
to the Regular Hours and Overtime Hours Pay Code for Worked Holiday Hours
respectively. Payroll Codes for OT2, OT3, and OT4 should be configured
as appropriate based on your Policy and Holiday Settings.

*NOTE: Your
[Payroll Codeâs list](Payroll_Export.md#pxh49_List_Hours_and_Earning_Types_tracked_by__your_Organization) would
have additional types of Overtime such as Day of Week Overtime, Consecutive
Day Overtime, or Double Time if you needed OT2.*

3. ### Configure Payroll Mapping Codes for Other Activity Types

Payroll
Mapping Codes must be set for Other Activity Hours and Other Amounts on
the General Tab of the Other Activity Update Form as shown below. This
step must be performed for every Other Activity Type required for your
organization. The example below shows all Other Activity Types for ABC
Company based off of ABC Companyâs Payroll Code List.

![](/img/image-404.png)

The
Other Activity Table pictured above shows each Other Activity Type required
for ABC Companyâs Payroll Code List. When configuring Other Activity Payroll
Mapping Codes double check to confirm that each Other Activity Hours and
Other Amount Type on your companyâs Payroll Code list is represented by
an Other Activity Type.

![](/img/image-404.png)

Shown
above is the Regular Hours Payroll Mapping Code as configured for Jury
Duty â Hourly. This Other Activity Type will be used to track Jury Duty
Hours for Hourly Manufacturing Employees at ABC Company.

![](/img/image-404.png)

Shown
above is the Regular Hours Payroll Mapping Code as configured for Jury
Duty â Salary. This Other Activity Type will be used to track Jury Duty
Hours for Salary Administrative Employees at ABC Company.

4. ### Set Shift Identifiers for Differential Worked Hours Types (If Applicable)

This
step is only necessary for organizations who track Shift Differentials.
Shift Identifiers must be set on the General Tab of the Shift Update Form.
One shift should be created for each Shift Differential.[Additional information on configuring Shift Differentials can be
found here.](../Scheduling/Scheduling.md#dif01_Shifts_for_Differential_Purposes)

![](/img/image-404.png)

ABC Company
has two Shift Differentials, Night Shift Differential and Sunday Differential.
Shift Identifiers are shown below for the Payroll Interface Format *âCNHS (Atlantic Coast Detail)â*
which includes separate columns for Payroll Codes (*Payroll
Export Field Name: âActivity Typeâ*) and Shift Identifiers (*Payroll
Export Field Name âShift Codeâ*)*.*

![](/img/image-404.png)

NOTE:
Shift Identifiers must be entered in one of two ways, depending on the
fields included in your chosen Payroll Interface Format. [Additional
details on fields included within a specific Payroll Interface Format
can be found here.](../Reports/Reports.md#rpt57_Payroll_Interface_Layout)

1.)  For Payroll
Interface Formats which include the âActivity Typeâ Field and the âShift
Codeâ Field, Shift Identifiers should be a single value for all Worked
Hours Types. Additionally, the âShift Identifier Overrides Payroll Codeâ
Company Option should be unchecked. This configuration allows the final
Payroll Export File to show the Shift Code in a Separate Column from the
Activity Type. ABC Companyâs configuration, as shown above for *the
CNHS (Atlantic Coast Detail)* Payroll Interface Format which includes
both the âActivity Typeâ Field and the âShift Codeâ Field, uses these
settings.

2.)  For
Payroll Interface Formats which include only the âActivity Typeâ Field,
Shift Identifiers should be set to include both the Worked Hours Payroll
Code and the Shift Code. Additionally, the âOverride Pay Codes with Shift
Pay Codesâ Payroll Export Option should be checked. This configuration
allows the final Payroll Export File to override the Working Hours Pay
Code in the Activity Type Column with the Shift Code. An example is shown
below.

NOTE: Only Payroll Interfaces with the Shift Activity,
Shift Activity / Period, and Shift Mapped record formats support shift
differentials. [Additional
Information on Payroll Export Record Formats can be found here.](../Reports/Reports.md#rpt57_Payroll_Interface_Layout)

![](/img/image-404.png)

### *By Payroll Mapping Number*

The âBy Payroll
Mapping Numberâ method uses Payroll Mapping Numbers with Payroll Interface
Formats designed to include numbered âmappedâ columns. Payroll Mapping
Numbers give users the ability to âmapâ Other Activity Hours for all Other
Activity Types with a specific Payroll Mapping Number to the corresponding
Mapped Column in the Payroll Interface Format. For example, all Other
Activity Types with Payroll Mapping Number One are totaled in Mapped Amount
Column One in the Payroll Export. All Other Activity Types with Payroll
Mapping Number Two are totaled in Mapped Amount Column Two in the Payroll
Export. Payroll Interface Formats which use the By Payroll Mapping Number
Earnings & Hours Export method have between one and fifteen mapped
columns.

Generally,
customers will either export all Other Activity Types to separate mapped
columns or they will export Other Activity Types with the different pay
rates to separate columns. In this way, the Accounting or Payroll Software
suite can correctly allocate Hours to the correct Hours / Earnings Type
and / or Pay Rate based on their position in the Final Export File. Instructions
for configuring Payroll Mapping Numbers are provided below.

### 1.     List Hours and Earning Types tracked by your Organization

Working backwards
from Hours and Earning Types defined in your Accounting or Payroll Software
Suite, complete a table similar to that shown below for all Hours and
Earnings Types you wish to track within InfiniTime
for employees. For most companies, this table will include entries for:

* One
  or more types of Regular Hours
* One
  or more types of Overtime Hours
* One
  or more types of Paid or Unpaid Leave Hours
* One
  or more types of Holiday Pay and Holiday Worked Hours
* One
  or more types of Shift Differential Hours (If Applicable)
* One or more
  types of Earnings (Paid as a Dollar Amount)

As an example,
the tables below were completed for XYZ Company who uses InfiniTime to track hours for their
hourly employees only. XYZ Company tracks Regular Hours, Weekly Overtime,
Paid and Unpaid Leave, and tracks Worked Holiday Hours. XYZ Company will
utilize the âCompuPay â Mappedâ Payroll Interface Format.

|  |  |  |  |
| --- | --- | --- | --- |
| **XYZ Company â Payroll Mapping Numbers** | | | |
| **Payroll Mapping Number** | **Description** | **Type\*** | **Base Rate Modifier** |
| N/A | Regular Hours for Hourly Employees | Working Hours | 1.0x |
| N/A | Weekly Overtime Hours for Hourly Employees | Working Hours | 1.5x |
| 1 | Jury Duty Hours for Hourly Employees | Other Activity Hours | 1.0x |
| 2 | Paid Time Off Hours for Hourly Employees | Other Activity Hours | 1.0x |
| 3 | Unpaid Time Off Hours for Hourly Employees | Other Activity Hours | 0.0x |
| 4 | Holiday Pay Hours for Hourly Employees | Other Activity Hours | 1.0x |
| 5 | Worked Holiday Hours | Other Activity Hours (Count as Hours Worked)\*\* | 1.5x |

\*For
additional details on Payroll Code Types See *Categories &
Examples of Hour Types Supported by InfiniTime
(Payroll Export: Section 1.1.1 Custom Payroll Interface Review & Design
Process)*

\*\*In this scenario, the Holiday Working Hours Other Activity type must
be set to count as regular hours. Additionally, separate Holiday Dates
must be created for Holiday Working Hours and Holiday Pay for each Holiday
XYZ Company wishes to track. Holiday Dates for Holiday Working Hours must
have âAll Worked Hours are Holiday Payâ set to âYesâ in order to post
Worked Hours to the Worked Holiday Hours Other Activity Type. [Additional information on Holiday
Settings can be found here.](../Configuration/Product_Configuration.md#hol01_Holiday_Types_Configuration_-_Introduction)

### 2. Configure Payroll Codes on the Payroll Codes Tab of the Payroll Export Update Form

As
required fields, the Payroll Code fields on the Payroll Codes Tab of the
Payroll Export Update Form must be filled with a value. Since Payroll
Interface Formats which utilize the âBy Payroll Mapping Numberâ Earnings
& Hours Export Method such as âCompuPay â Mappedâ do not utilize Payroll
Codes, the Payroll Codes can be filled with any value. As shown below,
Payroll Codes for XYZâs Payroll Export have been set to NA for all Worked
Hours Types.

![](/img/image-404.png)

![](/img/image-404.png)

XYZ
Company uses the CompuPay â Mapped Payroll Interface to transfer Employee
Hours and Earnings to their CompuPay Payroll Services provider. 

![](/img/image-404.png)

Notice how
the Payroll Code fields are set to NA. This clearly indicates that the
Payroll Codes are not used by the chosen Payroll Interface Format.

### 3.     Configure Payroll Mapping Codes and Payroll Mapping Numbers for Other Activity Types

As
required fields, the Payroll Mapping Code fields on the General Tab of
the Other Activity Type Update Form must be filled with a value. Most
Payroll Interface Formats with the âBy Payroll Mapping Numberâ Earnings
& Hours Export Method such as âCompuPay â Mappedâ do not utilize Payroll
Mapping Codes, for these Payroll Interface Formats the Payroll Mapping
Codes can be filled with any value. As shown below, Payroll Mapping Codes
for XYZâs Payroll Export have been set to NA for all Other Activity Types.

![](/img/image-404.png)

![](/img/image-404.png)

Payroll Mapping Numbers must be set for Other Activity Hours and Other
Amounts on the General Tab of the Other Activity Update Form as shown
below. This step must be performed for every Other Activity Type to be
included in the Final Payroll Export File. It is important to note that
the number of available mapped columns depends on the chosen Payroll Interface
Format. Some Payroll Interface Formats have only a few (1 â 3) Mapped
Columns while others have up to fifteen mapped columns. Remember â all
Other Activity Types with the same Payroll Mapping Number will be totaled
in the corresponding mapped Column. For example, all other Activity Types
with a Payroll Mapping Number of 2 will be totaled in Mapped Amount Column
Two. Details on the number of mapped columns available for your chosen
Payroll Interface Format can be found using the [Payroll
Interface Format Report.](../Reports/Reports.md#rpt57_Payroll_Interface_Layout)

![](/img/image-404.png)

NOTE: A very small percentage of Payroll Interface
Formats which utilize the âBy Payroll Mapping Numberâ Earnings & Hours
Export Method such as âADP Version 5.02â also utilize Payroll Mapping
Codes, for these Payroll Interface Formats the Payroll Mapping Codes must
be filled with the appropriate Hours / Earnings Code as configured within
the Payroll Application. An example Payroll Mapping Code / Payroll Code
List is completed below for Payroll Interface formats which utilize the
âBy Payroll Mapping Numberâ Earnings & Hours Export Methodâ with Payroll
Mapping Codes.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Payroll Code** | **Payroll Mapping Number** | **Description** | **Type\*** | **Base Rate Modifier** |
| N/A | N/A | Regular Hours for Hourly Employees | Working Hours | 1.0x |
| N/A | N/A | Weekly Overtime Hours for Hourly Employees | Working Hours | 1.5x |
| JD | 1 | Jury Duty Hours for Hourly Employees | Other Activity Hours | 1.0x |
| PTO | 2 | Paid Time Off Hours for Hourly Employees | Other Activity Hours | 1.0x |
| UTO | 3 | Unpaid Time Off Hours for Hourly Employees | Other Activity Hours | 0.0x |
| HP | 4 | Holiday Pay Hours for Hourly Employees | Other Activity Hours | 1.0x |
| HW | 5 | Worked Holiday Hours | Other Activity Hours (Count as Hours Worked)\*\* | 1.5x |

|  | The Other Activity Type form is shown to the left with all Other Activity Types required for the scenario above.     Notice how both the Payroll Mapping Number and Payroll Mapping Code are filled according to the Payroll Mapping Code / Payroll Mapping Number list above. All Other Activity Types exported to Payroll Interfaces which utilize the âBy Payroll Mapping Numberâ Earnings & Hours Export Methodâ with Payroll Mapping Codes must be configured in this way. |

The CompuPay â Mapped Payroll Interface used by XYZ Company includes
ten mapped columns. With this in mind, CompuPay has chosen to total each
Other Activity Type in its own mapped column for clarity. By referring
to the original Payroll Mapping Numbers list completed for XYZ Company,
we can see that each Other Activity Type should be configured with a Payroll
Mapping Number as shown below.

|  |  |
| --- | --- |
| **Other Activity Type** | **Payroll Mapping Number** |
| Jury Duty | 1 |
| Paid Time Off | 2 |
| Unpaid Time Off | 3 |
| Holiday Pay | 4 |
| Worked Holiday Hours | 5 |

### *Hard Coded Payroll Interface Format*

The âHard
Coded Payroll Interface Formatâ method uses hard coded fields which display
hours only for a specific earnings or hours type. In this way, the Accounting
or Payroll Software Suite can correctly allocate employee hours to the
correct Hours / Earnings Type and pay the correct rate for the number
of hours shown each column.

If your Payroll Interface utilizes the âHard Coded Payroll Interface
Formatâ Earnings & Hours Export method, Payroll Codes and Payroll
Mapping Numbers are not required and may be set to any value. Other Activity
Descriptions must match Payroll Interface Hard Coded Field Values as outlined
below. [Instructions for how
to determine which Hard Coded Fields your chosen Payroll Interface Format
includes can be found here.](../Reports/Reports.md#rpt57_Payroll_Interface_Layout)

|  |  |
| --- | --- |
| **Hard Coded Payroll Interface Fields** | |
| **Field Title** | **Required Other Activity Type Description** |
| Bereavement Hours | Bereavement |
| Bereavement Hours Total | Bereavement |
| Holiday Hours | Holiday |
| Holiday Hours Total | Holiday |
| Jury Duty Hours | Jury Duty |
| Jury Duty Hours Total | Jury Duty |
| Meals\*\*\* | Meals |
| Meals Total\*\*\* | Meals |
| Military Hours | Military |
| Military Hours Total | Military |
| Paid Holiday Hours | Paid Holiday |
| Paid Holiday Hours Total | Paid Holiday |
| Paid Time Off | Paid Time Off |
| Paid Time Off Total | Paid Time Off |
| Personal Hours | Personal |
| Personal Hours Total | Personal |
| Sales\*\*\* | Sales |
| Sales Total\*\*\* | Sales |
| Sick Hours | Sick |
| Sick Hours For A Day | Sick |
| Sick Hours Total | Sick |
| Tips\*\*\* | Tips |
| Tips Total\*\*\* | Tips |
| Vacation Hours | Vacation |
| Vacation Hours For A Day | Vacation |
| Vacation Hours Total | Vacation |

Complete
instructions for configuring a Hard Coded Payroll Interface Format are
below.

### 1.     List Earnings and Hours Types for your Organization

Working backwards from Hours and Earning Types defined in your Accounting
or Payroll Software Suite, complete a table similar to that shown below
for all Hours and Earnings Types you wish to track within InfiniTime for employees. For most
companies, this table will include entries for:

Â·       Regular
Hours

Â·       One
or more types of Overtime Hours

Â·       One
or more types of Paid or Unpaid Leave Hours

Â·       One
or more types of Holiday Pay and Holiday Worked Hours

Â·       One
or more types of Shift Differential Hours (If Applicable)

Â·       One or
more types of Earnings (Paid as a Dollar Amount)

As an example, the tables below were completed for ZYX Company who uses
InfiniTime to track hours
for their hourly employees only. ZYX Company tracks Regular Hours, Weekly
Overtime, Double Time, Vacation Hours and Sick Hours. ZYX Company will
utilize the âCheckmark Payroll For Windowsâ Payroll Interface Format.

|  |  |  |  |
| --- | --- | --- | --- |
| **XYZ Company â Payroll Mapping Numbers** | | | |
| **Other Activity Description** | **Description** | **Type\*** | **Base Rate Modifier** |
| N/A | Regular Hours | Working Hours | 1.0x |
| N/A | Weekly Overtime | Working Hours | 1.5x |
| N/A | Double Time | Working Hours | 2.0x |
| Vacation | Vacation Hours | Other Activity Hours | 1.0x |
| Sick | Sick Hours | Other Activity Hours | 1.0x |

\*For additional details on Payroll
Code Types See *[Categories
& Examples of Hour Types Supported by InfiniTime](Payroll_Export.md#pxh5_Categories___Examples_of_Hour_Types_Supported_by_InfiniTime)*

Hard Coded Payroll Interfaces are designed to automatically export worked
hours such as Regular Hours, Weekly Overtime, and Double Time. The Worked
Hours Types supported by a specific Hard Coded Payroll Interface can be
found by using [the Payroll
Interface Layout Report.](../Reports/Reports.md#rpt57_Payroll_Interface_Layout) ZYX Companyâs chosen payroll interface format
âCheckmark Payroll For Windowsâ specifically supports Regular Hours, Overtime
One Hours, and Overtime Two Hours. With this in mind, Employee Policies
must be configured with appropriate settings for Overtime One and Overtime
Two according to ZYX Companyâs HR Policies for Weekly Overtime and Double
Time.

### 2. Configure Payroll Mapping Codes on the Payroll Codes Tab of the Payroll Export Update Form

As
required fields, the Payroll Code fields on the Payroll Codes Tab of the
Payroll Export Update Form must be filled with a value. Since Hard Coded
Payroll Interface Formats such as âCheckmark Payroll For Windowsâ do not
utilize Payroll Codes, the Payroll Codes can be filled with any value.
As shown below, Payroll Codes for ZYXâs Payroll Export have been set to
NA for all Worked Hours Types.

![](/img/image-404.png)

ZYX
Company uses the Checkmark Payroll for Windows Payroll Interface to transfer
Employee Hours and Earnings to the Checkmark Payroll Application.

![](/img/image-404.png)

Notice how
the Payroll Code fields are set to NA. This clearly indicates that the
Payroll Codes are not used by the chosen Payroll Interface Format.

### 3.     Configure Other Activity Type Descriptions and Payroll Mapping Codes for Other Activity Types

Other Activity
Type Descriptions must be specifically set to match the Hard Coded Field
Value as listed above. In this way, the Payroll Export will be able to
correctly total Hours / Dollars for the respective Other Activity Type.

![](/img/image-404.png)

As
required fields, the Payroll Mapping Code fields on the General Tab of
the Other Activity Type Update Form must be filled with a value. Hard
Coded Payroll Interface Fields do not utilize Payroll Mapping Codes, for
this reason Payroll Mapping Codes can be filled with any value. As shown
below, Payroll Mapping Codes for XYZâs Payroll Export have been set to
NA for all Other Activity Types.

![](/img/image-404.png)

### *Support for Payroll Interface Specific Prompts (IE: Company Code)*

Some
Payroll Interface Formats such as âADP Version 5.02â include prompts on
the Required Info Tab of the Payroll Export Update Form which must be
completed by the user. The Required Info Tab is only displayed for Payroll
Interfaces that have prompts.

![](/img/image-404.png)

NOTE: In order to export different values for a
single prompt, multiple payroll exports must be configured. One for each
desired value. For example, if a customer using the âPS-Payâ Payroll Interface
Format needed to export employee hours for two separate Company Codes,
as shown below, two payroll exports would need to be configured.

|  |  |
| --- | --- |
| Company Name | Company Code |
| XYZ Housekeeping | 1000 |
| XYZ Landscaping | 2000 |

One Payroll Export must be configured for each
Prompt Value:

![](/img/image-404.png)

XYZ Housekeeping Employees:

![](/img/image-404.png)

XYZ Landscaping Employees:

![](/img/image-404.png)

### *Ability to Track Shift Differentials*

Payroll Interfaces of the Shift Activity, Shift Activity/Period,
and Shift Mapped Record Formats support the use of Shift Differentials.
Shift Differentials track hours worked during specific time periods of
the day for which employees receive bonus pay in the form of an Additional
Dollar Amount Per Hour, a Percentage Increase over their Base Rate, or
an alternate rate. [Steps to
determine if your chosen Payroll Interface Format supports Shift Differentials
using the Payroll Interface layout Report can be found here.](../Reports/Reports.md#rpt57_Payroll_Interface_Layout) If your
Payroll Interface Format Supports Shift Differentials and you wish to
track Differential Hours for Employees then Employee Policies, Shifts,
and Shift Identifiers must be correctly configured. Please see the following
sections of this document for additional information on [how
to configure Shift Differentials](../Scheduling/Scheduling.md#dif01_Shifts_for_Differential_Purposes) and [Employee
Policies for use with Differentials.](../Policies/Policy_Overview.md#pol138_Schedule_Settings___Rules_-_Shift_Differentials_Tab) Full Instructions for Configuring
Shift Identifiers are listed below.

### 1. List Shift Differentials tracked by your Organization

1.     Working
backwards from Hours and Earning Types defined in your Accounting or Payroll
Software Suite, complete a table similar to that shown below for all Shift
Differentials you wish to track within InfiniTime
for employees.

|  |  |  |  |
| --- | --- | --- | --- |
| **ABC Company - Shift Identifiers** | | | |
| **Shift Identifier** | **Description** | **Type** | **Pay Method** |
| NS | Night Shift Differential | Shift Differential | Additional $1.00 Per Hour |
| SUN | Sunday Differential | Shift Differential | Additional 50% of Base Rate Per Hour |

### 2.     Set Shift Identifiers for Differential Worked Hours Types

Shift
Identifiers must be set on the General Tab of the Shift Update Form. One
shift should be created for each Shift Differential.

![](/img/image-404.png)

ABC Company
has two Shift Differentials, Night Shift Differential and Sunday Differential.
Shift Identifiers are shown below for the Payroll Interface Format *âCNHS (Atlantic Coast Detail)â*
which includes separate columns for Payroll Codes (*Payroll
Export Field Name: âActivity Typeâ*) and Shift Identifiers (*Payroll
Export Field Name âShift Codeâ*)*.*

![](/img/image-404.png)

NOTE:
Shift Identifiers must be entered in one of two ways, depending on the
fields included in your chosen Payroll Interface Format.

1.)  For
Payroll Interface Formats which include the âActivity Typeâ Field and
the âShift Codeâ Field, Shift Identifiers should be a single value for
all Worked Hours Types. Additionally, the âShift Identifier Overrides
Payroll Codeâ Company Option should be unchecked. This configuration allows
the final Payroll Export File to show the Shift Code in a Separate Column
from the Activity Type. ABC Companyâs configuration, as shown above for
*the CNHS (Atlantic Coast Detail)*
Payroll Interface Format which includes both the âActivity Typeâ Field
and the âShift Codeâ Field, uses these settings.

2.)  For Payroll
Interface Formats which include only the âActivity Typeâ Field, Shift
Identifiers should be set to include both the Worked Hours Payroll Code
and the Shift Code. Additionally, the âShift Identifier Overrides Payroll
Codeâ Company Option should be checked. This configuration allows the
final Payroll Export File to override the Working Hours Pay Code in the
Activity Type Column with the Shift Code. An example is shown below.

NOTE:
Only Payroll Interfaces with the Shift Activity, Shift Activity / Period,
and Shift Mapped record formats support shift differentials. The[Payroll Interface Layout Report](../Reports/Reports.md#rpt57_Payroll_Interface_Layout) can be used to determine which record
format your Payroll Interface uses.

3.)  For
Payroll Interface Formats which include the âActivity Typeâ Field and
the âShift Codeâ Field, Shift Identifiers should be a single value for
all Worked Hours Types. Additionally, the âShift Identifier Overrides
Payroll Codeâ Company Option should be unchecked. This configuration allows
the final Payroll Export File to show the Shift Code in a Separate Column
from the Activity Type. ABC Companyâs configuration, as shown above for
*the CNHS (Atlantic Coast Detail)*
Payroll Interface Format which includes both the âActivity Typeâ Field
and the âShift Codeâ Field, uses these settings.

4.)  For Payroll
Interface Formats which include only the âActivity Typeâ Field, Shift
Identifiers should be set to include both the Worked Hours Payroll Code
and the Shift Code. Additionally, the âShift Identifier Overrides Payroll
Codeâ Company Option should be checked. This configuration allows the
final Payroll Export File to override the Working Hours Pay Code in the
Activity Type Column with the Shift Code. An example is shown below.

![](/img/image-404.png)

NOTE:
Only Payroll Interfaces with the Shift Activity, Shift Activity / Period,
and Shift Mapped record formats support shift differentials.

### *Job Costing*

Job Costing, or hours costing, is the process of categorizing employee
hours to provide insight into an organizationâs operations. Job costing
provides the ability to perform charge backs for operational costs. When
coupled with managerial accounting processes, Job Costing can also provide
managers with data to base labor management decisions on such as hiring
additional employees. [Additional
Information on configuring Job Costing within the InfiniTime Software
can be found in the Job Costing Section of this document.](../Configuration/Product_Configuration.md#cnf01_Job_Costing_Introduction)

Payroll Interfaces Formats support between one and three levels of Job
Costing according to the Payroll Interface Formatâs Record Format as outlined
below. [The Payroll Interface
Layout Report can be used to determine your chosen Payroll Interface Formatâs
Record Format as well as which Job Costing related fields are supported.](../Reports/Reports.md#rpt57_Payroll_Interface_Layout)

|  |  |
| --- | --- |
| **Payroll Interface Record Format** | **Supported Job Costing Levels** |
| Activity | 1 Level:  Â·       Departments |
| Activity/Period | 1 Level:  Â·       Departments |
| Daily | 1 Level:  Â·       Departments |
| For Period | 1 Level:  Â·       Departments |
| Job Activity | 2 Levels:  Â·       Departments  Â·       Jobs |
| Job Activity/Period | 2 Levels:  Â·       Departments  Â·       Jobs |
| Mapped | 3 Levels:  Â·       Departments  Â·       Jobs  Â·       Tasks |
| Punch List | 3 Levels:  Â·       Departments  Â·       Jobs  Â·       Tasks |
| Shift Activity | 3 Levels:  Â·       Departments  Â·       Jobs  Â·       Tasks |
| Shift Activity/Period | 3 Levels:  Â·       Departments  Â·       Jobs  Â·       Tasks |
| Shift Mapped | 3 Levels:  Â·       Departments  Â·       Jobs  Â·       Tasks |
| Task Activity | 3 Levels:  Â·       Departments  Â·       Jobs  Â·       Tasks |
| Task Activity/Period | 3 Levels:  Â·       Departments  Â·       Jobs  Â·       Tasks |

NOTE:
Not all Payroll Interface Formats include Job Costing Related Fields.
Some Payroll Interface Formats may include less than three levels, such
as Jobs Only or Jobs and Tasks only.

### *Ability to Export Employee Gross Wages*

InfiniTime includes a variety of wage
related features for the purpose of calculating employee gross wages from
Default Employee Wages, Alternate Wages which can be defined for a specific
Department / Job / Task Combination, Shift Differential Pay Methods, and
Premium Pay for hours worked in specific Departments, Jobs, or Tasks.

Payroll
Interface Formats with support for Employee Wages will include one or
more of the following fields:

|  |  |
| --- | --- |
| Field Title | Field Description |
| Activity Wage | Exports Hourly Wage for Respective Hours Type / Department / Job / Task Combination for Employees with the âHourlyâ Pay Method |
| Employee Alternate Hourly Wage for Activity Dept | Exports Alternate Wage for Activity Department for Employees with the âHourlyâ Pay Method |
| Employee Default Hourly Wage | Exports Employee Default Hourly Wage for Employees with the âHourlyâ Pay Method |
| Employee Hourly Wage | Exports Hourly Wage for Employees with the âHourlyâ Pay Method |
| Employee Overtime Rate | Exports the Employeeâs Overtime One Wage |
| Employee Overtime Rate Two | Exports the Employeeâs Overtime Two Wage |
| Employee Overtime Rate Three | Exports the Employeeâs Overtime Three Wage |
| Employee Overtime Rate Four | Exports the Employeeâs Overtime Four Wage |
| Employee Salary Amount | Exports the Employee Default Wage on the Employee Update Form for Employees with the Salary Pay Method.    When using a payroll export that includes this field for Employees with a Salary Pay Method, the Employee Default Wage Field should be set to the employeeâs Gross Payable Salary for the Pay Period. |
| Overtime Hours Wages | Exports Total Overtime Wages for the Date Range for which the Payroll Export is executed. |
| Overtime Two Wages | Exports Total Overtime Wages for the Date Range for which the Payroll Export is executed. |
| Regular Hours Wages | Exports Total Overtime Wages for the Date Range for which the Payroll Export is executed. |

[The
Payroll Interface Layout Report can be used to determine if your chosen
Payroll Interface Format includes wage related fields.](../Reports/Reports.md#rpt57_Payroll_Interface_Layout)

NOTE: If you wish to use your Accounting or Payroll
Software Suite as the source for employee wages and your chosen Payroll
Interface Format includes a field for Employee Wages, you may choose to
leave Employee Default Wages and other wage related settings within InfiniTime Blank. By leaving Employee
Default Wages and wage related settings within InfiniTime
blank, the final payroll export file will not include employee wages.

### *Ability to Export Employee Hours to Different Files for Specific Sets of Employees*

InfiniTime does not place
a limit on the number of Payroll Exports that can be defined. Each Payroll
Export defined in the Payroll Export Table creates a single output file.
The Payroll Export Output file includes hours and earnings as calculated
for all timecard records during the Date Range set for the Payroll Export
for each employee included in the Payroll Export Employee Filter. With
this in mind, a different Payroll Export File can be created for specific
sets of employees simply by creating a separate Payroll Export Setting
for each set of employees and setting the Payroll Export Employee Filter
on each Payroll Export Setting as appropriate.

For Example, XYZ Organization has two divisions â XYZ Housekeeping and
XYZ Landscaping. Notice how one Payroll Export is defined for each division.
In this case, groups have been used to ensure the appropriate employees
are exported by each Payroll Export. [Additional
details on configuring the Employee Filter on the Payroll Export and throughout
the InfiniTime Application
can be found here.](../Security/Security_Overview.md#sec17b_Configuring_Security_Filters)

One Payroll Export must be Configured for Each Set of Employees which
require a separate Export File:

![](/img/image-404.png)

The Filter must be configured as appropriate to select the desired employees.
In this example, XYZ Housekeeping Employees are all assigned to the XYZ
Housekeeping Group:

![](/img/image-404.png)

The Filter must be configured as appropriate to select the desired employees.
In this example, XYZ Landscaping Employees are all assigned to the XYZ
Landscaping Group:

![](/img/image-404.png)

### *Output Method(s)*

The InfiniTime Payroll
Export System provides support for the following Output Methods:

* A
  Prompt is Displayed to allow the User to Open or Save the Final Payroll
  Export File
* Export
  File Via FTP
* Email
  Final Payroll Export File to One or More Email Recipients
* Automatically
  Perform the Payroll Export according to a predefined Scheduled Interval
* Place
  Final Payroll Export File in the Output Folder with a File Name and
  Extension as defined by the Payroll Export File Name.

One or more of the above output methods can be enabled for a given payroll
export. It should be noted that the Final Payroll Export File will only
be placed in the Output Folder if the Payroll Export is executed automatically
according to a predefined Schedule, âSend File via FTPâ is disabled, and
no email recipients are defined. If the Payroll Export is executed from
within the Manager Module or the Escort Module, the user will be prompted
to Open or Save the Final Payroll Export File. Additional details on configuring
the Output Methods can be found in the [Payroll
Export User Interface Overview](Payroll_Export.md#pxh8_Payroll_Export_User_Interface_Overview) section of this document.

### *Ability to PGP Encrypt Final Payroll Interface Output File*

PGP Encryption
is provided as an option to provide maximum security for sensitive information
such as employee demographics, bank account details, and employee social
security numbers. PGP Encryption can be enabled by Checking the âPGP Encrypt
Fileâ Option on the General Tab of the Payroll Export Update Form. This
enables the PGP Tab as shown below.

![](/img/image-404.png)

* Refer
  to the [PGP
  Encryption â Changing PGP Keys](../Security/Security_Overview.md#sec66_PGP_Encryption_-_Changing_PGP_Key_Files) section of this document
  to configure the PGP Key Files and Passphrase as appropriate for your
  PGP Client.
* Configure
  the Payroll Export as appropriate for you chosen Payroll Interface
  Format. Ensure the Employee Filter, Date Range, Payroll Codes, Employee
  Filter, and Required Info are configured appropriately.
* Save
  the Payroll Export by Clicking OK.

### *Ability to Automatically Output the Final Payroll Export File According to a predefined Schedule*

Payroll
Exports can be automatically exported a single time on a specific date
and time or according to  preset
intervals such as Daily, Weekly, or Monthly. Payroll Export files with
Auto Schedules will be exported based upon Output Settings as follows:

* If
  PGP Encrypt File is checked, the Final Payroll Export File will be
  Encrypted and exported according to Output Options configured on the
  Payroll Export.
* If
  âSend File Via FTPâ is unchecked and no email recipients are defined,
  the Final Payroll Export File will be placed in the output directory.
* If
  âSend File Via FTPâ is unchecked and one or more email recipients
  are defined, the Final Payroll Export File will be emailed from the
  InfiniTime Temp Folder
  and will not be placed in the output directory. The Final Payroll
  Export file will be deleted from the Temp Folder once the file has
  been emailed to all recipients.
* If
  âSend File Via FTPâ is checked and no email recipients are defined,
  the Final Payroll Export File will be Transferred to the specified
  FTP Destination from the InfiniTime
  Temp Folder and will not be placed in the output directory. The Final
  Payroll Export file will be deleted from the Temp Folder once the
  FTP Transfer is completed.
* If
  âSend File Via FTPâ is checked and one or more email recipients are
  defined, the Final Payroll Export File will first be Transferred to
  the specified FTP Destination from the InfiniTime
  Temp Folder then the Final Payroll Export File will be emailed from
  the InfiniTime Temp
  Folder. The Final Payroll Export File will not be placed in the output
  directory. The Final Payroll Export file will be deleted from the
  Temp Folder after the file has been sent to all email recipients.

### *Payroll Export Employee / Timecard Filter Related Processing Options*

The Payroll Export includes three options which alter the way the Payroll
Export Employee Filter Functions as follows:

Â·       Only
Export Records for the Non Default Department

Â·       Department
Selector Filters Time instead of Employee

Â·       Include
Employees Terminate During the Export Range

The
above options can be used individually or together. Full details on the
functionality of the above options can be found in [the Payroll Export Overview](Payroll_Export.md#pxh22_Options_Tab)
section of this document. No additional configuration is necessary for
use of the Payroll Export Employee / Timecard Filter Related Processing
Options.

### *Alert Related Payroll Export Processing Options*

The Payroll
Export includes four options which alert the user of specific conditions
before Employee Hours and Earnings are exported to the Final Payroll Export
File.

Â·       Alert
When Unreviewed Exceptions are Found for Exported Employees

Â·       Alert
When Timecards are Not Reviewed by Employeeâs Supervisor for Exported
Employees

Â·       Alert
When Timecards are Not Reviewed by Employee for Exported Employees

Â·       Alert
When Number of Reviews are Less than X for Exported Employees

The
above options can be used individually or together. Full details on the
functionality of the above options can be found in [the
Payroll Export Overview](Payroll_Export.md#pxh22_Options_Tab) section of this document. The options above
are intended for use with InfiniTime's
Timecard Review Functionality.

### *Interface Specific Payroll Export Processing Options*

The Payroll
Export includes three options Processing Related Options which alter how
Employee Hours and Earnings are calculated and exported as follows:

Â·       Export
Overtime as Half Time

Â·       Pay
Shift Differential Hours at Differential Pay Only

Â·       Group
Level for Export

The
above options can be used individually or together. Full details on the
functionality of the above options can be found in [the
Payroll Export Overview](Payroll_Export.md#pxh22_Options_Tab)  section of this document. Export Overtime
as Half Time requires at least one Overtime Type (Overtime 1, Overtime
2, Overtime 3, or Overtime 4) to be configured. Pay Shift Differential
Hours at Differential Pay Only is available only for Payroll Interface
Formats which support Shift Differentials and requires Shift Differentials
to be configured in full. Additional information on configuring Shift
Differentials can be found here.  Group Level for Export requires
Groups to be configured and assigned to all employees.

### *General Payroll Export Processing Options*

The Payroll
Export includes one General Processing Option as follows:

Â·       Assign
All Time to Employeeâs Default Department.

If this option
is enabled, all Employee Hours will be exported as though they were worked
in the respective employeeâs Default Department.

## Logic Flow Documents

For full clarity, Logic Flow documents are provided which show exactly
how the Payroll Export tool functions. Thumbnails for each diagram are
shown below - simply click on the thumbnail to view the full diagram

NOTE: An internet connection is required to download
and view the full logic flow diagrams.

### Payroll Export Input:

[![](/img/image-404.png)](Payroll_Export_Input_Logic_Flow_Diagram.md)

### Payroll Export Processing

[![](/img/image-404.png)](Payroll_Export_Processing_Logic_Flow_Diagram.md)

### Payroll Export Output

[![](/img/image-404.png)](Payroll_Export_Output_Logic_Flow_Diagram.md)