xml version="1.0" encoding="utf-8" ?

Accrual Configuration

### Employee Accruals Introduction

Accruals make it possible to track various types of Paid Leave such
as Sick Time, Vacation Time, and / or Personal Time. InfiniTime's
Accrual Features can be used to:

- Track Total Accrued Hours for various types of Paid Leave (IE:
  Sick Time, Vacation Time, Personal Time)
- Track Remaining Hours for various types of Paid Leave (IE: Sick
  Time, Vacation Time, Personal Time)
- Track Used Hours for various types of Paid Leave (IE: Sick Time,
  Vacation Time, Personal Time)
- Provide employees with access to Accrual Balances
- Provide employees with access to a detailed history for all
  types of Paid Leave, including specific dates on which hours were
  earned and used according to organizational policies.

InfiniTime includes two
Accrual Packages, Basic Accruals and Accruals Plus. The Basic Accruals
Package included with the InfiniTime
Application is designed to meet the needs of most customers with support
for up to two accrual buckets (IE: Vacation and Personal Time) and standard
accrual functionality. Accruals Plus was developed for users who require
a more robust solution for Accruals with support for extended features
such as:

- Ability to Accrue and Reset Employee Accruals According to your
  organizationâs Fiscal Year
- Ability to define a maximum Carry Over Amount
- Ability to allow carried over hours to expire
- Ability to disable use of accrued time for an accrual bucket (IE:
  Employees accrue hours during the current year for use in the next
  year.)
- Support for Comp Time (Posting Overtime to an Accrual)
- Support for Rate Mapping (Awarding Accrual Hours Based upon the
  amount of hours worked throughout the year)
- Prevent Negative Accrual Balances
- Award additional hours at the end of an Accrual Period
- Prorate Employee Accruals during the first year of employment according
  to when the employee was hired

This document will address the Basic Accruals and Accruals Plus modules
separately. Multiple tables are used throughout this section to facilitate
the gathering of accrual related information. Blank forms for documenting
your organizations accrual requirements are provided at the links below
and may be printed as desired. Additionally, a process flow diagram is
also provided which describes the high level procedure for configuring
employee accruals for an enterprise organization.
...

### Employee Accruals â Basic Accruals Overview

In most scenarios difficulties with Accruals configuration are related
to having an incomplete understanding of an organizationâs accrual requirements.
For this reason a detailed process has been established for gathering
information required to properly document an organizationâs accrual requirements.
When attempting to identify accrual requirements it is often helpful to
ignore specific features and options within InfiniTime
and start by focusing on the needs of your organization. Once the organizationâs
accrual requirements are understood finding the appropriate options within
InfiniTime is generally
not a problem.

The procedure for configuring accruals is similar to the method used
for configuring Policies and Holidays. Employee groups requiring different
accrual settings must be identified before attempting to configure accruals
within the InfiniTime Application.
Keep in mind it is common for accrual benefits to change based upon the
amount of time employees have been with a company. Because of this Classes
and Tenures will likely be required. Remember, classes can be used to
group multiple accrual types together and tenures are used to automatically
move employees from one accrual type to the next based upon the length
of time they have been with the company.

To setup accruals there are five main tasks that must be performed:

#### 1. Identify Accrual Classes

Use Employee Accruals Table 1 to identify groups of employees (Or individual
employees) requiring different accrual settings.

For example ABC Company has the following
personnel:

| Employee Accruals Table 1 | |
| Job Title | Pay Type |
| Administration | Salary |
| Cleaning Staff | Full Time |
| Front Desk Staff | Full Time |
| Kitchen | Full Time |
| Child Day Care | Part Time |
| Night Auditors | Part Time |

ABC Company Part Time employees do not receive
benefits in the form of Vacation or Personal Time though they are eligible
for Sick Time after they are with the company for a year. Salary and Full
Time Employees must be employed for 90 days prior to accruing Vacation
or Personal Time though they accrue Vacation and Personal Time Hours at
different rates. After reviewing the employees and policies at ABC Company
the following classes, or groups of employees, require different accrual
settings:

Salary

Full Time

Part Time

#### 2. Identify Accrual Calculations Tracked by Your Organization

Complete Employee Accrual Table 2 to identify
each Accrual Calculation for which the previously listed classes are eligible
for. One accrual calculation is required for each bucket of hours where
Accrued Hours, Remaining Hours, and Used Hours must be tracked separately
for employees. Remember, the basic accruals package can track a maximum
of two Accrual Calculations for any given Accrual Type. If your organization
tracks more than two Accrual Calculations, you will need the Accrual Plus
Module. Your Inception Technologies Sales Representative can provide additional
information on the Accrual Plus Module.

| Employee Accruals Table 2 | | |
| Class | Accrual Calculation 1 | Accrual Calculation 2 |
| Part Time | Sick Time (After 1 Year of Employment) | |
| Full Time | Vacation Time | Personal Time |
| Salary | Vacation Time | Personal Time |

#### 3. Identify Accrual Tenure Ranges for each Accrual Class

Review Employee Accruals Table 3 below and
identify each point when accrual benefits change for each class for your
organization. In most organizations, employee paid leave benefits increase
based upon the amount of time the employee has spent with the company.
It is not unusual for different classes, or groups of employees, to receive
additional benefits at different milestones. In some circumstances, employee
paid leave benefits for a specific type of paid leave may increase at
different milestones when compared with other types of paid leave in a
single accrual class. This scenario requires the Accrual Plus Accrual
Calculation Tenures feature and is only supported by the Accrual Plus
Module. The example below assumes all types of paid leave for each single
accrual class receive additional benefits at uniform, or equally divisible,
milestones.

For example, Part Time Employees at ABC Company
receive 2 Days (16 Hours) of Paid Sick Time after their first year of
employment. This benefit does not increase for part time employees based
upon the amount of time they have been with the company. ABC Company rewards
Full Time and Salary employees with additional Vacation and Personal Time
benefits at the following milestones: After 3 Years, After 5 Years, and
After 10 Years of Employment. With this in mind, ABC Company requires
the following tenure ranges for each class:

| Employee Accruals Table 3 | |
| Accrual Class: Part Time Employee Accruals | |
| Tenure Min | Tenure Max |
| 0 Years | 1 Year |
| 1 Year | 99 Years |

| Employee Accruals Table 3 | |
| Accrual Class: Full Time Employee Accruals | |
| Tenure Min | Tenure Max |
| 0 Years | 3 Years |
| 3 Years | 5 Years |
| 5 Years | 10 Years |
| 10 Years | 99 Years |

| Employee Accruals Table 3 | |
| Accrual Class: Salary Employee Accruals | |
| Tenure Min | Tenure Max |
| 0 Years | 3 Years |
| 3 Years | 5 Years |
| 5 Years | 10 Years |
| 10 Years | 99 Years |

#### 4. List all Accrual Calculations

Complete Employee Accruals Table 4 for each group of employees or individual
employees requiring different accrual settings using the Classes, Accrual
Calculations, and Tenure Ranges identified in Steps 1 to 3. At this point,
you may wish to refer to the [Basic
Accruals Module Features and Settings Section](Accrual_Configuration.md#acc17_Basic_Accruals_Module___Accrual_Calculation_Features___Settings) of this document to
familiarize yourself with the Accrual Calculation options available within
InfiniTime. This will help
with completing the âSettingsâ column of Employee Accruals Table 4. As
you fill out the table, keep the following rules in mind:

- Tenures for each class must represent all values from 0 to 99 Years.
- Tenures may not contain gaps. For example, notice how all years
  from 0 to 99 are represented for each Accrual Class below.
- Accrual Calculations for a single type of Paid Leave must have
  the same name for each tenure range. For Example, notice how âVacation
  Timeâ is referred to as âVacation Timeâ across all tenure ranges in
  the Full Time Accrual Class.

| Employee Accruals Table 4 | | | |
| Accrual Name: Part Time Employee Accruals | | Employee Group (Accrual Class): Part Time | |
| Tenure Min | Tenure Max | Accrual Calculation | Settings |
| 0 Years | 1 Year | NONE | Reset Type: N/A Calculation Method(s): None Calculation Modifiers: None |
| 1 Year | 99 Years | Sick Time | Reset Type: Calendar Year Calculation Method(s): Start at 16 Hours Calculation Modifiers: None |

| Employee Accruals Table 4 | | | |
| Accrual Name: Full Time Employee Accruals | | Employee Group (Accrual Class): Full Time | |
| Tenure Min | Tenure Max | Accrual Calculation | Settings |
| 0 Years | 3 Years | Vacation Time | Reset Type: Calendar Year Calculation Method(s): Start at 40 Hours Calculation Modifiers: None |
| 3 Years | 5 Years | Vacation Time | Reset Type: Calendar Year Calculation Method(s): Start at 80 Hours Calculation Modifiers: None |
| 5 Years | 10 Years | Vacation Time | Reset Type: Calendar Year Calculation Method(s): Start at 96 Hours Calculation Modifiers: None |
| 10 Years | 99 Years | Vacation Time | Reset Type: Calendar Year Calculation Method(s): Start at 120 Hours Calculation Modifiers: None |
| 0 Years | 3 Years | Personal Time | Reset Type: Calendar Year Calculation Method(s): Start at 16 Hours Calculation Modifiers: None |
| 3 Years | 5 Years | Personal Time | Reset Type: Calendar Year Calculation Method(s): Start at 32 Hours Calculation Modifiers: None |
| 5 Years | 10 Years | Personal Time | Reset Type: Calendar Year Calculation Method(s): Start at 48 Hours Calculation Modifiers: None |
| 10 Years | 99 Years | Personal Time | Reset Type: Calendar Year Calculation Method(s): Start at 64 Hours Calculation Modifiers: None |

| Employee Accruals Table 4 | | | |
| Accrual Name: Salary Employee Accruals | | Employee Group (Accrual Class): Salary | |
| Tenure Min | Tenure Max | Accrual Calculation | Settings |
| 0 Years | 3 Years | Vacation Time | Reset Type: Calendar Year Calculation Method(s): Start at 48 Hours Calculation Modifiers: Carry Over |
| 3 Years | 5 Years | Vacation Time | Reset Type: Calendar Year Calculation Method(s): Start at 88 Hours Calculation Modifiers: Carry Over |
| 5 Years | 10 Years | Vacation Time | Reset Type: Calendar Year Calculation Method(s): Start at 104 Hours Calculation Modifiers: Carry Over |
| 10 Years | 99 Years | Vacation Time | Reset Type: Calendar Year Calculation Method(s): Start at 128 Hours Calculation Modifiers: Carry Over |
| 0 Years | 3 Years | Personal Time | Reset Type: Calendar Year Calculation Method(s): Start at 32 Hours Calculation Modifiers: Carry Over |
| 3 Years | 5 Years | Personal Time | Reset Type: Calendar Year Calculation Method(s): Start at 48 Hours Calculation Modifiers: Carry Over |
| 5 Years | 10 Years | Personal Time | Reset Type: Calendar Year Calculation Method(s): Start at 64 Hours Calculation Modifiers: Carry Over |
| 10 Years | 99 Years | Personal Time | Reset Type: Calendar Year Calculation Method(s): Start at 72 Hours Calculation Modifiers: Carry Over |

#### 5. Use Employee Accruals Table 3 to configure Accrual Types

Configure Accrual Types as necessary for each employee group using the
completed tables. When properly completed, Employee Accruals Table 3 has
one row for each Accrual Type required for your organization.

#### 6. Use Employee Accruals Table 4 to Configure Accrual Calculations

Configure Accrual Calculations for each Accrual Type using Employee
Accruals Table 4. When properly completed, Employee Accruals Table 4 has
one row for each Accrual Calculation required for your organization. The
procedure for configuring accrual types and accrual calculations is outlined
below in the

#### 7. Assign Employees to the Correct Accrual Type using Quick Assign

### Accessing the Accrual Types Table

- Login to the Manager Module as an Administrator
- Click on Lookups
- Click on Calculations Setup
- Click on Accrual Types

The Accrual Types Table will be displayed. The Accrual Types Table displays
all accrual types in the InfiniTime
Database, for all Accrual Classes and Tenure ranges.

![](/img/BasicAccruals_058.png)

### Accessing the Accrual Type Update Form

- Login to the Manager Module as an Administrator
- Click on Lookups
- Click on Calculations Setup
- Click on Accrual Types
- The Accrual Types Table will be displayed
- Click Insert to access the Accrual Type Update Form

The Accrual Types Update Form is used to create accrual types. As detailed
in the [Basic Accruals Overview
section](Accrual_Configuration.md#acc02_Employee_Accruals___Basic_Accruals_Overview), one accrual type is required for each row in Employee Accruals
Table 3.

Accrual Type Update
Form General Tab:

![](/img/BasicAccruals_047.png)

Accrual
Type Update Form Accrual Calculations Tab:

![](/img/BasicAccruals_042.png)

### Accessing the Accrual Calculations Update Form

- Login to the Manager Module
  as an Administrator
- Click on Lookups
- Click on Calculations Setup
- Click on Accrual Types
- The Accrual Types Table will
  be displayed.
- Click on an existing Accrual
  Type and click Change.
- Click on the Accrual Calculations
  Tab.
- Click Insert to access the
  Accrual Calculations Update Form.

**Accrual
Calculation Update Form General Tab:**

![](/img/BasicAccruals_037.png)

**Accrual
Calculation Update Form Other Activities That Deduct Tab:**

![](/img/BasicAccruals_044.png)

The Accrual Calculations Update Form is used
to create accrual calculations for a specific Accrual Type. As detailed
in the [Basic Accruals Overview
section](Accrual_Configuration.md#acc02_Employee_Accruals___Basic_Accruals_Overview), one accrual calculation is required for each row in Employee
Accruals Table 4. It should be noted that the Basic Accrual Module supports
a maximum of two Accrual Calculations per Accrual Type.

### Basic Accruals Module â Accrual Calculation Features & Settings

InfiniTime
Accrual Calculations are comprised of three separate types of features
and settings:

- Reset Type
- Calculation Method(s)
- Calculation Modifiers

#### Reset Type

The Basic Accruals Module supports two Reset
Types which determine the Accrual Period Date Range and the date on which
employee accrual hours are carried forward or reset. The âCalendar Yearâ
Reset Type uses the Calendar Year (January 1st â December 31st) as the
basis for Employee Accrual Periods. Calculation Modifiers are then applied
as appropriate. For example, an accrual calculation configured as shown
below will carry over unused hours as of December 31st into the next accrual
period. Additionally, Employees will be awarded 40 additional hours for
the new accrual period every year on January 1st.

Carry Over Reset Type: Calendar Year

Calculation Method(s): Start at 40 Hours

Calculation Modifiers: Carry Over

The âAnniversaryâ Reset Type uses each individual
employeeâs Hire Date as the basis for Employee Accrual Periods. Calculation
Modifiers are then applied as appropriate. For example, an accrual calculation
configured as shown below for an employee hired on May 6th 2012 will award
40 hours to the employee after 90 days of employment, carry unused hours
as of May 5th 2013 forward into the next accrual period beginning on May
6th 2013 and award an additional 40 hours on May 6th 2013.

Carry Over Reset Type: Anniversary

Calculation Method(s): Start at 40 Hours

Calculation Modifiers: Carry Over, Start Accruing
Hire Date Plus 90 Days

#### Calculation Method(s)

The Basic Accruals Module supports two Calculation
Methods for awarding accrual hours to employees. The âStart Atâ Calculation
Method makes hours available for use by the employee immediately at the
start of each Accrual Period where as the âAccrueâ Calculation Method
adds a specified amount to available hours at regular intervals. The first
task when configuring accrual calculations within the Basic Accruals Module
is to identify the accrual method which meets customer requirements, afterwards
any additional options can be configured as necessary. It should be noted
that a single Accrual Calculation can use one or more Calculation Methods,
though at least one Calculation Method must be configured.

#### Calculation Modifiers

Calculation Modifiers are optional rules and features which alter the
way Calculation Method(s) award hours. The Basic Accruals Module includes
a limited number of Calculation Modifiers which provide support for simplistic
Employee Accrual Calculations. Calculation Modifiers supported by the
Basic Accruals Module are listed below. More advanced Employee Accrual
Calculations and feature sets are supported with Calculation Modifiers
available in the Accruals Plus module. A complete description of how each
Calculation Modifier alters Calculation Method(s) is provided below.

| Basic Accruals Module Calculation Modifiers | |
| Stop Accruing Date | Carry Over |
| Start Accruing Hire Date Plus | Stop At |

### Basic Accruals Module - Calculation Methods - Introduction

_Remember:_
Calculation Methods permit the user to define the exact calculation and
frequency used to award hours to employees. A single Accrual Calculation
can have one or more calculation methods. InfiniTime
will display a warning if you attempt to save an Accrual Calculation without
configuring at least one calculation method.

#### Start At Calculation Method

The âStart Atâ Calculation Method awards hours to employees on the First
Day of each accrual period. Hours awarded by the Start At Calculation
method are available for immediate use and is intended for use employees
have a given amount of hours available during the accrual period which
can be used as needed. For example the âStart Atâ calculation method would
be used if employees have 40 Vacation Hours to use as needed throughout
the year. Alternatively, the âAccrueâ calculation method would be used
if employees received .769 hours for every seven days of employment.

#### Accrue Calculation Method

Using the âAccrueâ Calculation Method awards a predefined number of
hours to employees at a set interval over time. The âAccrueâ Calculation
Method is based on a three part formula as illustrated below.

![](/img/BasicAccruals_022.png)

1 â Accrue Amount

- Enter the number of hours to be awarded to employees at each
  interval in this field. This field supports up to six decimals accuracy.
  IE: 14.123456

2 â Accrual Interval
Amount - For the Day(s) or Month(s) Accrual Interval Unit, enter
the number of Days or Months to define the length of the Accrual Interval.
Employees will be awarded hours at the last day of every accrual interval.
Alternatively, for the Hour(s) Worked Accrual Interval Unit enter the
number of Hours that employees must work before hours will be awarded.
Employees will be awarded hours on each date successive date on which
they accumulate this number of hours.

3 â Accrual Interval
Unit - Choose Days, Hours, or Months from the drop down to set
the Accrual Interval unit. The Accrual Interval Unit determines the frequency
at which hours will be awarded to employees.

Day(s)
â Bases the accrual interval on a number of days after the beginning
of the accrual period.

Hour(s)
â Bases the accrual interval on the number of hours worked by the
employee.

Month(s)
â Bases the accrual interval on the number of months after the
beginning of the accrual period.

An example of each Accrual Interval Unit, and how hours are awarded,
is provided below. For example the settings below accrue 1.538462 Hours
for every two weeks employees are employed by the company for a total
of approx. 40 hours per year.

#### Example Employee Accruals: Accrual Calculation Method with Day(s) Accrual Interval Unit

The Accrual Calculation and related settings below show an example of
how Employee Accrual Hours are awarded for the Accrual Calculation Method
under the Day(s) Accrual Interval. Notice how the Accrual Interval Amount
defines the length of the accrual interval where as the Accrue Amount
determines the number of hours awarded for each accrual interval. In this
example, the Employee is awarded 1.53846 hours every 14 days for a total
of 40 hours per Calendar Year Accrual Period.

#### Related Settings:

Employee Hire Date: 11/06/2011

Accrual Reset Type: Calendar
Year

Stop At: 40

![](/img/Hourly.png)

#### _Employee Accrual Posting Records_

The screenshot below shows each date on which accruals
are awarded for the employee. Note that with the Basic Accruals Module,
progress toward the next Accrual Interval starts over at the end of the
accrual period. Any progress toward the next accrual interval on the last
day of the Accrual Period is lost. This can be observed at the end of
the 2011 and 2012 accrual periods as shown in the report below. For example,
the last date in 2011 for which Vacation Hours are awarded is 12/18/11.
The first date in 2012 for which Vacation Hours are awarded is 1/15/2012.
Only 13 calendar days exist between 12/18/2011 to 12/31/2011, which is
1 day short of the 14 day Interval. On 1/1/2012 the progress toward the
next interval is reset, resulting in the employee being awarded hours
on 1/15/2012, after the 14th day of employment has passed in
the new accrual period. After 1/15/2012, the employee is awarded hours
every 14 days.

NOTE: Accrual Intervals can be forced to persist
through accrual periods, such that progress toward the next accrual interval
is not lost at the end of the Accrual Period, with the âAccrual Interval
Persists through Accrual Periodsâ Accrual Plus Feature.

![](/img/OneLevelCarryOver_TCEAP.png)

#### Employee Accrual Totals

As of 3/7/13, based on the Accrual Settings
detailed above and the resulting Employee Accrual Posting Records, the
employee will receive a total of 4.61539 Vacation Hours in 2011, 40 Vacation
Hours in 2012, and 6.15385 Vacation Hours in 2013.

![](/img/BasicAccruals_005.png)

#### Example Employee Accruals: Accrual Calculation Method w/ Month(s) Accrual Interval Unit

The Accrual Calculation and related settings
below show an example of how Employee Accrual Hours are awarded for the
Accrual Calculation Method under the Month(s) Accrual Interval. Notice
how the Accrual Interval Amount defines the length of the accrual interval
where as the Accrue Amount determines the number of hours awarded for
each accrual interval. In this example, the Employee is awarded 3.333334
hours every month for a total of 40 hours per Calendar Year Accrual Period.

#### Related Settings:

Employee Hire Date: 11/06/2011

Accrual Reset Type: Anniversary

Stop At: 40

![](/img/BasicAccruals_021.png)

#### Employee Accrual Posting Records

The screen shot below shows each date on
which accruals are awarded for the employee. Notice how hours are awarded
each month, on the same day of the month as the employee was hired except
for where the day on which the employee was hired does not exist for that
month. In that case, hours are awarded on the last day of the month. For
example, in the example below the employee was hired on 11/06/2011. Notice
how hours are awarded on the 6th day of each month. If the employee were
hired on 10/31/2011, the employee would be awarded hours on the 31st day
of the month for those months with 31 days and on the last day of the
month for all months with less than 31 days. In this way, employees are
awarded hours every month.

![](/img/AccrualPostCarryOver.png)

#### _Employee Accrual Totals_

As
of 4/23/13, based on the Accrual Settings detailed above and the resulting
Employee Accrual Posting Records, the employee will receive a total of
40.00001 Vacation Hours for the Accrual Period starting 11/06/2011 and
16.666667 Vacation Hours for the Accrual Period starting 11/06/2012.

_![](/img/AccrualPosting_EndOfCycle_Fiscal.png)_

_Example
Employee Accruals: Accrual Calculation Method w/ Hour(s) Accrual Interval
Unit_

The Accrual Calculation and related settings below
show an example of how Employee Accrual Hours are awarded for the Accrual
Calculation Method under the Hour(s) Accrual Interval. In this example,
the Accrual Interval Amount determines the number of hours that must be
worked in order for the employee to be awarded additional hours. In this
example, the Employee is awarded 1.538462 hours for every 80 hours worked
from their date of hire forward.

#### Related Settings:

Employee Hire Date:
11/30/2011

Accrual Reset Type:
Anniversary

![](/img/BasicAccruals_020.png)

#### Employee Accrual Posting Records

The screen shot below shows each date on
which accruals are awarded for the employee. Note that with the Basic
Accruals Module, progress toward the next Accrual Interval starts over
at the end of the accrual period. Any progress toward the next accrual
interval on the last day of the Accrual Period is lost. This can be observed
at the end of the 2011 and 2012 accrual periods as shown in the report
below. For example, the last date in the 11/30/11 â 11/29/12 Accrual Period
for which Vacation Hours are awarded is 11/26/12. The first date in 11/30/2012
â 11/29/13 Accrual Period for which Vacation Hours are awarded is 12/13/2012.
The employee works 24 hours from 11/27/2012 to 11/29/2012, which is 56
hours short of the 80 Hours Accrual Interval Amount. On 11/30/2012 the
progress toward the next interval is reset, resulting in the employee
being awarded hours on 12/13/2012, when the employee hits a total of 80
hours in the new accrual period. After 1/15/2012, the employee is awarded
hours every 80 hours worked.

![](/img/BasicAccruals_058.png)

#### Employee Accrual Totals

As of 3/7/13, based on the Accrual Settings detailed
above and the resulting Employee Accrual Posting Records, the employee
will receive a total of 41.53847 Vacation Hours for the Accrual Period
starting 11/30/2011 and 12.30770 Vacation Hours for the Accrual Period
Starting 11/30/2012.

![](/img/Star.png)

#### Employee Timecards for 11/27/12 to 11/29/12

For clarity, Timecards for the employee from 11/27/12
to 11/29/12 are shown below. Remember, progress toward the next Accrual
Interval starts over at the end of the accrual period. Any progress toward
the next accrual interval on the last day of the Accrual Period is lost.

![](/img/Accruals_78.png)

#### Employee Timecards for 11/30/12 to 12/13/12

For clarity, Timecards for the employee from 11/30/12
to 12/13/12 are shown below. Remember, progress toward the next Accrual
Interval starts over at the end of the accrual period. Any progress toward
the next accrual interval on the last day of the Accrual Period is lost.
This is clearly illustrated below. December 13th 2012 is the first date
in the 11/30/12 to 11/29/13 Accrual Period on which the employee accumulated
80 hours worked in the new accrual period.

![](/img/image8.jpg)

### Basic Accrual Module â Calculation Modifiers

Calculation â
Enter a descriptive name for the Accrual Calculation such as âVacation
Timeâ or âSick Time.â All Accrual Calculations in an Accrual Class with
multiple tenure ranges should have the same Calculation Name across all
accrual types and accrual calculations in the Accrual Class as illustrated
in the provided examples.

Stop Accruing
Date â Employees will no longer accrue hours for the accrual type
as of the date set in this field.

Start Accruing
Hire Date Plus â This setting is intended for use with new hires
and should only be configured on accrual types with a minimum tenure of 0.  The number entered in this field represents a number of days
after the employeeâs Date of Hire during which InfiniTime
will not calculate accruals. It helps to think of this as a probation
period, in days, during which employees will not automatically accrue
hours.

Stop At â
Sets the maximum amount of hours which may be available for the Accrual
Type. InfiniTime will stop
accruing additional hours if the amount of available hours reaches this
value.

Carry Over Reset
Type â Determines the start and end of the accrual period. The
exact behavior of the chosen carry over reset type depends on the method
Calculation Method(s) chosen for making accrual hours available to employees.

âStart
atâ Calculation Method â Available hours for the accrual type will
reset to the start at amount at the beginning of a new accrual period.
If carry over is not checked any hours unused from the prior period will
be lost. If carry over is checked any hours unused from the prior period
will be brought forward and added to the start at amount.

âAccrueâ
Calculation Method â Available hours for the accrual type will
reset to zero at the beginning of a new accrual period. If carry over
is not checked any hours unused from the prior period will be lost. If
carry over is checked any hours unused from the prior period will be brought
forward and added to the remaining amount.

Anniversary
â Defines the start of the accrual period as the employeeâs hire
date. Employee accruals will reset accordingly on the employeeâs hire
date each year.

Calendar
Year â Defines the start of the accrual period as January 1st of
each year. Employee accruals will reset accordingly on this date.

Carry Over â
Available hours unused during the prior period will be brought forward
to the new accrual period if this option is checked. If this option us
unchecked unused hours during the prior period will not be brought forward
and are lost.

### Other Activities that Deduct Tab

The Other Activities that Deduct Tab is used to configure other activity
types that can be used to deduct from available accrual hours. For example
the Vacation Other Activity Type is often associated with a Vacation Accrual
Type. In this way vacation hours will automatically be deducted from available
accrual hours when employees take vacation. Each Accrual Type should have
at least one Other Activity Type associated with it in order to deduct
vacation, sick, or personal time from the accrual bucket automatically.

### Employee Accruals - Accruals Plus Module Overview

In most scenarios difficulties with Accruals configuration are related
to having an incomplete understanding of an organizationâs accrual requirements.
For this reason a detailed process has been established for gathering
information required to properly document an organizationâs accrual requirements.
When attempting to identify accrual requirements it is often helpful to
ignore specific features and options within InfiniTime
and start by focusing on the needs of your organization. Once the organizationâs
accrual requirements are understood finding the appropriate options within
InfiniTime is generally
not a problem.

The procedure for configuring accruals is similar to the method used
for configuring Policies and Holidays. Employee groups requiring different
accrual settings must be identified before attempting to configure accruals
within the InfiniTime Application.
Keep in mind it is common for accrual benefits to change based upon the
amount of time employees have been with a company. Because of this Classes
and Tenures will likely be required. Remember, classes can be used to
group multiple accrual types together and tenures are used to automatically
move employees from one accrual type to the next based upon the length
of time they have been with the company.

To setup accruals there are five main tasks that must be performed:

#### 1. Identify Accrual Classes

Use Employee Accruals Table 1 to identify groups of employees (Or individual
employees) requiring different accrual settings.

For example ABC Company has the following
personnel:

| Employee Accruals Table 1 | |
| Job Title | Pay Type |
| Administration | Salary |
| Cleaning Staff | Full Time |
| Front Desk Staff | Full Time |
| Kitchen | Full Time |
| Child Day Care | Part Time |
| Night Auditors | Part Time |

ABC Company Part Time employees do not receive
benefits in the form of Vacation or Personal Time though they are eligible
for Sick Time after they are with the company for a year. Salary and Full
Time Employees must be employed for 90 days prior to accruing Vacation
or Personal Time though they accrue Vacation and Personal Time Hours at
different rates. After reviewing the employees and policies at ABC Company
the following classes, or groups of employees, require different accrual
settings:

Salary

Full Time

Part Time

#### 2. Identify Accrual Calculations Tracked by Your Organization

Complete Employee Accrual Table 2 to identify
each Accrual Calculation for which the previously listed classes are eligible
for. One accrual calculation is required for each bucket of hours where
Accrued Hours, Remaining Hours, and Used Hours must be tracked separately
for employees. The Accrual Plus Module
supports an unlimited number of Accrual Calculations for each accrual
type.

| Employee Accruals Table 2 | | |
| Class | Accrual Calculation 1 | Accrual Calculation 2 |
| Part Time | Sick Time (After 1 Year of Employment) | |
| Full Time | Vacation Time | Personal Time |
| Salary | Vacation Time | Personal Time |

#### 3. Identify Accrual Tenure Ranges for each Accrual Class

Review Employee Accruals Table 3 below and
identify each point when accrual benefits change for each class for your
organization. In most organizations, employee paid leave benefits increase
based upon the amount of time the employee has spent with the company.
It is not unusual for different classes, or groups of employees, to receive
additional benefits at different milestones. In some circumstances, employee
paid leave benefits for a specific type of paid leave may increase at
different milestones when compared with other types of paid leave in a
single accrual class. This scenario requires the Accrual Plus Accrual
Calculation Tenures feature and is only supported by the Accrual Plus
Module. The example below assumes all types of paid leave for each single
accrual class receive additional benefits at uniform, or equally divisible,
milestones.

For example, Part Time Employees at ABC Company
receive 2 Days (16 Hours) of Paid Sick Time after their first year of
employment. This benefit does not increase for part time employees based
upon the amount of time they have been with the company. ABC Company rewards
Full Time and Salary employees with additional Vacation and Personal Time
benefits at the following milestones: After 3 Years, After 5 Years, and
After 10 Years of Employment. With this in mind, ABC Company requires
the following tenure ranges for each class:

| Employee Accruals Table 3 | |
| Accrual Class: Part Time Employee Accruals | |
| Tenure Min | Tenure Max |
| 0 Years | 1 Year |
| 1 Year | 99 Years |

| Employee Accruals Table 3 | |
| Accrual Class: Full Time Employee Accruals | |
| Tenure Min | Tenure Max |
| 0 Years | 3 Years |
| 3 Years | 5 Years |
| 5 Years | 10 Years |
| 10 Years | 99 Years |

| Employee Accruals Table 3 | |
| Accrual Class: Salary Employee Accruals | |
| Tenure Min | Tenure Max |
| 0 Years | 3 Years |
| 3 Years | 5 Years |
| 5 Years | 10 Years |
| 10 Years | 99 Years |

#### 4. List all Accrual Calculations

Complete Employee Accruals Table 4 for each group of employees or individual
employees requiring different accrual settings using the Classes, Accrual
Calculations, and Tenure Ranges identified in Steps 1 to 3. At this point,
you may wish to refer to the [Accruals
Plus Module Features and Settings Section](Accrual_Configuration.md#acc41_Accrual_Plus_Module___Accrual_Calculation_Features___Settings_Introduction) of this document to familiarize
yourself with the Accrual Calculation options available within InfiniTime. This will help with completing
the âSettingsâ column of Employee Accruals Table 4. As you fill out the
table, keep the following rules in mind:

- Tenures for each class must represent all values from 0 to 99 Years.
- Tenures may not contain gaps. For example, notice how all years
  from 0 to 99 are represented for each Accrual Class below.
- Accrual Calculations for a single type of Paid Leave must have
  the same name for each tenure range. For Example, notice how âVacation
  Timeâ is referred to as âVacation Timeâ across all tenure ranges in
  the Full Time Accrual Class.

| Employee Accruals Table 4 | | | |
| Accrual Name: Part Time Employee Accruals | | Employee Group (Accrual Class): Part Time | |
| Tenure Min | Tenure Max | Accrual Calculation | Settings |
| 0 Years | 1 Year | NONE | Reset Type: N/A Calculation Method(s): None Calculation Modifiers: None |
| 1 Year | 99 Years | Sick Time | Reset Type: Calendar Year Calculation Method(s): Start at 16 Hours Calculation Modifiers: None |

| Employee Accruals Table 4 | | | |
| Accrual Name: Full Time Employee Accruals | | Employee Group (Accrual Class): Full Time | |
| Tenure Min | Tenure Max | Accrual Calculation | Settings |
| 0 Years | 3 Years | Vacation Time | Reset Type: Calendar Year Calculation Method(s): Start at 40 Hours Calculation Modifiers: None |
| 3 Years | 5 Years | Vacation Time | Reset Type: Calendar Year Calculation Method(s): Start at 80 Hours Calculation Modifiers: None |
| 5 Years | 10 Years | Vacation Time | Reset Type: Calendar Year Calculation Method(s): Start at 96 Hours Calculation Modifiers: None |
| 10 Years | 99 Years | Vacation Time | Reset Type: Calendar Year Calculation Method(s): Start at 120 Hours Calculation Modifiers: None |
| 0 Years | 3 Years | Personal Time | Reset Type: Calendar Year Calculation Method(s): Start at 16 Hours Calculation Modifiers: None |
| 3 Years | 5 Years | Personal Time | Reset Type: Calendar Year Calculation Method(s): Start at 32 Hours Calculation Modifiers: None |
| 5 Years | 10 Years | Personal Time | Reset Type: Calendar Year Calculation Method(s): Start at 48 Hours Calculation Modifiers: None |
| 10 Years | 99 Years | Personal Time | Reset Type: Calendar Year Calculation Method(s): Start at 64 Hours Calculation Modifiers: None |

| Employee Accruals Table 4 | | | |
| Accrual Name: Salary Employee Accruals | | Employee Group (Accrual Class): Salary | |
| Tenure Min | Tenure Max | Accrual Calculation | Settings |
| 0 Years | 3 Years | Vacation Time | Reset Type: Calendar Year Calculation Method(s): Start at 48 Hours Calculation Modifiers: Carry Over |
| 3 Years | 5 Years | Vacation Time | Reset Type: Calendar Year Calculation Method(s): Start at 88 Hours Calculation Modifiers: Carry Over |
| 5 Years | 10 Years | Vacation Time | Reset Type: Calendar Year Calculation Method(s): Start at 104 Hours Calculation Modifiers: Carry Over |
| 10 Years | 99 Years | Vacation Time | Reset Type: Calendar Year Calculation Method(s): Start at 128 Hours Calculation Modifiers: Carry Over |
| 0 Years | 3 Years | Personal Time | Reset Type: Calendar Year Calculation Method(s): Start at 32 Hours Calculation Modifiers: Carry Over |
| 3 Years | 5 Years | Personal Time | Reset Type: Calendar Year Calculation Method(s): Start at 48 Hours Calculation Modifiers: Carry Over |
| 5 Years | 10 Years | Personal Time | Reset Type: Calendar Year Calculation Method(s): Start at 64 Hours Calculation Modifiers: Carry Over |
| 10 Years | 99 Years | Personal Time | Reset Type: Calendar Year Calculation Method(s): Start at 72 Hours Calculation Modifiers: Carry Over |

#### 5. Use Employee Accruals Table 3 to configure Accrual Types

Configure Accrual Types as necessary for each employee group using the
completed tables. When properly completed, Employee Accruals Table 3 has
one row for each Accrual Type required for your organization.

#### 6. Use Employee Accruals Table 4 to Configure Accrual Calculations

Configure Accrual Calculations for each Accrual Type using Employee
Accruals Table 4. When properly completed, Employee Accruals Table 4 has
one row for each Accrual Calculation required for your organization. The
procedure for configuring accrual types and accrual calculations is outlined
in the

#### 7. Assign Employees to the Correct Accrual Type using Quick Assign

### Accessing the Accrual Types Table

- Login to the Manager Module as an Administrator
- Click on Lookups
- Click on Calculations Setup
- Click on Accrual Types

The Accrual Type Table will be displayed. The Accrual Type Table displays
all accrual types in the InfiniTime
Database and is used to add additional Accrual Types to the software.

![](/img/Accruals_70.png)

Copy -
Permits the InfiniTime
Administrator to copy an existing accrual type by selecting an accrual
type and clicking the copy button. A copied accrual type will have the
same configuration and Accrual Calculations as the selected accrual type.

Insert

- Permits the InfiniTime
  Administrator to create a new Accrual Type. Opens the Accrual Type Update
  Form.

Change

- Opens the Accrual Type Update Form for the selected Accrual Type. The
  InfiniTime Administrator
  may then alter the accrual type's settings as desired.

Delete

- Removes the selected Accrual Type from the database.

### Accessing the Accrual Type Update Form

- Login to the Manager Module as an Administrator
- Click on Lookups
- Click on Calculations Setup
- Click on Accrual Types
- The Accrual Types Table will be displayed
- Click Insert to access the Accrual Type Update Form

The Accrual Types Update Form is used to create accrual types. The [Basic
Accruals Overview](Accrual_Configuration.md#acc02_Employee_Accruals___Basic_Accruals_Overview) and [Accruals
Plus Overview section](Accrual_Configuration.md#acc26_Employee_Accruals_-_Accruals_Plus_Module_Overview)s of this document provide step by step instructions
and examples of how to determine the Accrual Types and related settings
required to configure InfiniTime
Accruals to meet the needs of your organization.

Accrual Type Update
Form General Tab:

The
General Tab of the Accrual Type Update Form includes basic settings related
to an accrual type, such as the Accrual Type Name, the Accrual Type Class,
and the tenures for which the Accrual Type applies.

![](/img/Accruals_76.png)

Accrual
Type Update Form Accrual Calculations Tab:

The
Accrual Calculations Tab of the Accrual Type Update Form lists all accrual
calculations defined for the respective accrual type. All employees assigned
to the accrual type will accrue hours in accordance with the settings
on each accrual calculation.

![](/img/Accruals_68.png)

### Accessing the Accrual Calculations Update Form

- Login
  to the Manager Module as an Administrator
- Click on Lookups
- Click on Calculations Setup
- Click on Accrual Types
- The Accrual Types Table will be displayed.
- Click on an existing Accrual Type
  and click Change.
- Click on the Accrual Calculations
  Tab.
- Click Insert to access the Accrual
  Calculations Update Form.

The Accrual Calculations Update Form is used to create accrual calculations.
Through use of Accrual Calculation Methods and Accrual Calculation Modifiers,
an accrual calculation defines the exact conditions under which employees
are awarded paid leave benefits. The [Basic
Accruals Overview](Accrual_Configuration.md#acc02_Employee_Accruals___Basic_Accruals_Overview) and [Accruals
Plus Overview section](Accrual_Configuration.md#acc26_Employee_Accruals_-_Accruals_Plus_Module_Overview)s of this document provide step by step instructions
and examples of how to determine the Accrual Types and related settings
required to configure InfiniTime
Accruals to meet the needs of your organization. Additional details regarding
the individual Reset Types, Accrual Calculation Methods, and Calculation
Modifiers can be found at the sections referenced below. Additionally,
each individual Calculation Modifier is listed in the Table of Contents
for ease of reference.

| [Accruals Plus - Accrual Calculation Features & Settings Introduction](Accrual_Configuration.md#acc41_Accrual_Plus_Module___Accrual_Calculation_Features___Settings_Introduction) |
| [Reset Types](Accrual_Configuration.md#acc42_Reset_Type) |
| [Calendar Year Reset Type](Accrual_Configuration.md#reset_Calendar) |
| [Anniversary Reset Type](Accrual_Configuration.md#reset_Anniversary) |
| [Fiscal Year Reset Type](Accrual_Configuration.md#reset_Fiscal) |
| [Calculation Methods](Accrual_Configuration.md#acc45_Accruals_Plus_Module_-_Calculation_Methods) |
| [Introduction](Accrual_Configuration.md#acc45_Accruals_Plus_Module_-_Calculation_Methods) |
| [Start At - Example](Accrual_Configuration.md#acc46_Start_At_Calculation_Method) |
| [Accrue - Example](Accrual_Configuration.md#acc47_Accrue_Calculation_Method) |
| [End of Cycle Bonus - Example](Accrual_Configuration.md#acc50_End_of_Cycle_Bonus_Calculation_Method) |
| [Alternate Posting - Example](Accrual_Configuration.md#acc54_Alternate_Posting_Calculation_Method) |
| [Rate Mapping - Example](Accrual_Configuration.md#acc55_Rate_Mapping_Calculation_Method) |
| [Calculation Modifiers](Accrual_Configuration.md#acc57_Accrual_Plus_Module___Calculation_Modifiers) |
| [Introduction](Accrual_Configuration.md#acc57_Accrual_Plus_Module___Calculation_Modifiers) |

#### Accrual Calculation Update Form General Tab

![](/img/BasicAccruals_027.png)

#### Accrual Calculation Update Form Accrual Plus Features tab - Calculation Modifiers Tab:

![](/img/BasicAccruals_006.png)

The Accrual Calculations Update Form is used to create accrual calculations
for a specific Accrual Type. As detailed in the Accrual Plus Overview
section, one accrual calculation is required for each row in Employee
Accruals Table 4. The Accrual Plus module supports an unlimited number
of Accrual Calculations for each Accrual Type.

### Accrual Plus Module â Accrual Calculation Features & Settings Introduction

InfiniTime Accrual Calculations
are comprised of three separate types of features and settings:

- Reset Type
- Calculation Method(s)
- Calculation Modifiers

#### Reset Type

The Accrual Plus Module supports three Reset Types which determine the
Accrual Period Date Range and the date on which employee accrual hours
are carried forward or reset.

#### 'Calendar Year' Reset Type

The âCalendar Yearâ Reset Type uses the Calendar Year (January 1st â
December 31st) as the basis for Employee Accrual Periods. Calculation
Modifiers are then applied as appropriate. For example, an accrual calculation
configured as shown below will carry over unused hours as of December
31st into the next accrual period. Additionally, Employees will be awarded
40 additional hours for the new accrual period every year on January 1st.

Carry Over Reset
Type - Calendar Year

Calculation Method(s)

- Start at 40 Hours

Calculation Modifiers

- Carry Over

#### 'Anniversary' Reset Type

The âAnniversaryâ Reset Type uses each individual employeeâs Hire Date
as the basis for Employee Accrual Periods. Calculation Modifiers are then
applied as appropriate. For example, an accrual calculation configured
as shown below for an employee hired on May 6th 2012 will award 40 hours
to the employee after 90 days of employment, carry unused hours as of
May 5th 2013 forward into the next accrual period beginning on May 6th
2013 and award an additional 40 hours on May 6th 2013.

Reset Type -
Anniversary

Calculation Method(s)

- Start at 40 Hours

Calculation Modifiers

- Carry Over, Start Accruing Hire Date Plus 90 Days

#### 'Fiscal Year' Reset Type

The âFiscal Yearâ Reset Type is comparable to the Calendar Year Reset
type, though it allows the user to set the date on which Employee Accrual
Periods will start and end. The âFiscal Yearâ Reset Type is ideal for
organizations who wish to award employee accrual hours based on the corporationâs
Fiscal Calendar. Calculation Modifiers will then be applied as appropriate.
For example, an accrual calculation configured as shown below will carry
over unused hours as of April 30th into the next accrual period. Additionally,
Employees will be awarded 40 additional hours for the new accrual period
every year on May 1st.

Reset Type -
Fiscal Year, Fiscal Period Start Date: May 1st

Calculation Method(s)

- Start at 40 Hours

Calculation Modifiers

- Carry Over

#### Calculation Method(s)

The Accrual Plus Module supports five Calculation Methods for awarding
accrual hours to employees as listed below.

| Calculation Method | Calculation Functionality |
| âStart Atâ | Awards Hours to employees immediately at the start of each accrual period. Generally, employees may then use the hours as needed throughout the accrual period. |
| âAccrueâ | Awards a specified amount of hours to employees at regular intervals over time. |
| âEnd of Cycle Bonusâ | Awards Hours to employees at the end of the Accrual Period. Generally, employees may then use the hours as needed throughout the following accrual period. NOTE: Carry Over must be enabled for hours awarded by the âEnd of Cycle Bonusâ Calculation Method to be carried forward into subsequent accrual periods. |
| âAlternate Postingâ | Alternate Posting permits worked hours types to be posted to an accrual bucket in lieu of payment. Often referred to as âComp Timeâ this feature is especially useful for tracking worked overtime hours for Salary Employees. Employees may then use earned hours as needed. |
| âRate Mappingâ | Intended for use alongside the Accrue Calculation Method, Rate Mapping makes it possible for the Accrue Amount awarded at each Accrual Interval to be scaled based on the number of units (IE: Total Hours Worked for the Hour(s) Accrue Interval Unit) elapsed during the accrual period. |

The first task when configuring
individual accrual calculations within the Accruals Plus Module is to
identify the accrual calculation method which meets customer requirements,
afterwards any additional options can be configured as necessary. It should
be noted that a single Accrual Calculation can use _one
or more_ Calculation Methods, though at least one Calculation Method
must be configured.

#### Calculation Modifiers

Calculation Modifiers are optional rules and features which alter the
way Calculation Method(s) award hours. The Accrual Plus Module includes
a number of Calculation Modifiers which provide support for both simplistic
and complex Employee Accrual Calculations. Calculation Modifiers supported
by the Accrual Plus Module are listed below. A complete description of
how each Calculation Modifier alters the available Calculation Method(s)
is provided below.

| Accrual Plus Module Calculation Modifiers | | | |
| Stop Accruing Date | Carry Over | Carry Over One Expiration | Carry Over One Maximum |
| Start Accruing Hire Date Plus | Stop At | Carry Over Two Expiration | Carry Over Two Maximum |
| Effective Date | Overflow | Accrual Calculation Tenure â Minimum & Maximum | Hours Needed to Qualify â Minimum & Maximum |
| Maximum Negative Accrual | Do Not Allow Accrued Time to Be used | Do Not Allow Accrued Time to Be Used in Year Accrued | Continue to Accrue to Stop At Amount After Time is Used |
| Award Immediately | | Accrue Hours as if Hired at the Start of the First Accrual Interval | Accrual Interval Persists Through Accrual Periods |

### Accruals Plus Module - Calculation Methods - Introduction

Remember: Calculation Methods permit the user to
define the exact calculation and frequency used to award hours to employees.
A single Accrual Calculation can have one or more calculation methods.
InfiniTime will display
a warning if you attempt to save an Accrual Calculation without configuring
at least one calculation method.

### Start At Calculation Method

The âStart Atâ Calculation Method awards hours to employees on the First
Day of each accrual period. Hours awarded by the Start At Calculation
method are available for immediate use and is intended for use employees
have a given amount of hours available during the accrual period which
can be used as needed. For example the âStart Atâ calculation method would
be used if employees have 40 Vacation Hours to use as needed throughout
the year. Alternatively, the âAccrueâ calculation method would be used
if employees received .769 hours for every seven days of employment.

### Accrue Calculation Method

Using the âAccrueâ Calculation Method awards a predefined number of
hours to employees at a set interval over time. The âAccrueâ Calculation
Method is based on a three part formula as illustrated below.

![](/img/image9.jpg)

1 â Accrue Amount

- Enter the number of hours to be awarded to employees at each
  interval in this field. This field supports up to six decimals accuracy.
  IE: 14.123456

2 â Accrual Interval
Amount - For the Day(s) or Month(s) Accrual Interval Unit, enter
the number of Days or Months to define the length of the Accrual Interval.
Employees will be awarded hours at the last day of every accrual interval.
Alternatively, for the Hour(s) Worked Accrual Interval Unit enter the
number of Hours that employees must work before hours will be awarded.
Employees will be awarded hours on each date successive date on which
they accumulate this number of hours.

3 â Accrual Interval
Unit - Choose Days, Hours, or Months from the drop down to set
the Accrual Interval unit. The Accrual Interval Unit determines the frequency
at which hours will be awarded to employees.

Day(s)
â Bases the accrual interval on a number of days after the beginning
of the accrual period.

Hour(s)
â Bases the accrual interval on the number of hours worked by the
employee.

Month(s)
â Bases the accrual interval on the number of months after the
beginning of the accrual period.

An example of each Accrual Interval Unit, and how hours are awarded,
is provided below. For example the settings below accrue 1.538462 Hours
for every two weeks employees are employed by the company for a total
of approx. 40 hours per year.

#### Example Employee Accruals: Accrual Calculation Method with Day(s) Accrual Interval Unit

The Accrual Calculation and related settings below show an example of
how Employee Accrual Hours are awarded for the Accrual Calculation Method
under the Day(s) Accrual Interval. Notice how the Accrual Interval Amount
defines the length of the accrual interval where as the Accrue Amount
determines the number of hours awarded for each accrual interval. In this
example, the Employee is awarded 1.53846 hours every 14 days for a total
of 40 hours per Calendar Year Accrual Period.

#### Related Settings:

Employee Hire Date: 11/06/2011

Accrual Reset Type: Calendar
Year

Stop At: 40

![](/img/HireAtStart.png)

#### _Employee Accrual Posting Records_

The
screen shot below shows each date on which accruals are awarded for the
employee. Note that with the Basic Accruals Module, progress toward the
next Accrual Interval starts over at the end of the accrual period. Any
progress toward the next accrual interval on the last day of the Accrual
Period is lost. This can be observed at the end of the 2011 and 2012 accrual
periods as shown in the report below. For example, the last date in 2011
for which Vacation Hours are awarded is 12/18/11. The first date in 2012
for which Vacation Hours are awarded is 1/15/2012. Only 13 calendar days
exist between 12/18/2011 to 12/31/2011, which is 1 day short of the 14
day Interval. On 1/1/2012 the progress toward the next interval is reset,
resulting in the employee being awarded hours on 1/15/2012, after the
14th day of employment has passed in the new accrual period.
After 1/15/2012, the employee is awarded hours every 14 days.

NOTE: Accrual Intervals can be forced to persist
through accrual periods, such that progress toward the next accrual interval
is not lost at the end of the Accrual Period, with the âAccrual Interval
Persists through Accrual Periodsâ Accrual Plus Feature.

![](/img/BasicAccruals_031.png)

#### Employee Accrual Totals

As of 3/7/13, based on the Accrual Settings
detailed above and the resulting Employee Accrual Posting Records, the
employee will receive a total of 4.61539 Vacation Hours in 2011, 40 Vacation
Hours in 2012, and 6.15385 Vacation Hours in 2013.

![](/img/BasicAccruals_019.png)

#### Example Employee Accruals: Accrual Calculation Method w/ Month(s) Accrual Interval Unit

The Accrual Calculation and related settings
below show an example of how Employee Accrual Hours are awarded for the
Accrual Calculation Method under the Month(s) Accrual Interval. Notice
how the Accrual Interval Amount defines the length of the accrual interval
where as the Accrue Amount determines the number of hours awarded for
each accrual interval. In this example, the Employee is awarded 3.333334
hours every month for a total of 40 hours per Calendar Year Accrual Period.

#### Related Settings:

Employee Hire Date: 11/06/2011

Accrual Reset Type: Anniversary

Stop At: 40

![](/img/BasicAccruals_023.png)

#### Employee Accrual Posting Records

The screen shot below shows each date on
which accruals are awarded for the employee. Notice how hours are awarded
each month, on the same day of the month as the employee was hired except
for where the day on which the employee was hired does not exist for that
month. In that case, hours are awarded on the last day of the month. For
example, in the example below the employee was hired on 11/06/2011. Notice
how hours are awarded on the 6th day of each month. If the employee were
hired on 10/31/2011, the employee would be awarded hours on the 31st day
of the month for those months with 31 days and on the last day of the
month for all months with less than 31 days. In this way, employees are
awarded hours every month.

![](/img/Accruals_68.png)

#### _Employee Accrual Totals_

As of 4/23/13, based on the Accrual
Settings detailed above and the resulting Employee Accrual Posting Records,
the employee will receive a total of 40.00001 Vacation Hours for the Accrual
Period starting 11/06/2011 and 16.666667 Vacation Hours for the Accrual
Period starting 11/06/2012. Notice how the employee is awarded hours each
month on the same day of the month on which they were originally hired.

![](/img/AccrualPostCarryOver.png)

#### Example Employee Accruals: Accrual Calculation Method w/ Hour(s) Accrual Interval Unit

The Accrual Calculation and related settings below
show an example of how Employee Accrual Hours are awarded for the Accrual
Calculation Method under the Hour(s) Accrual Interval. In this example,
the Accrual Interval Amount determines the number of hours that must be
worked in order for the employee to be awarded additional hours. In this
example, the Employee is awarded 1.538462 hours for every 80 hours worked
from their date of hire forward.

#### Related Settings:

Employee Hire Date:
11/30/2011

Accrual Reset Type:
Anniversary

![](/img/Accruals_83.png)

#### Employee Accrual Posting Records

The screen shot below shows each date on
which accruals are awarded for the employee. Note that by default, progress
toward the next Accrual Interval starts over at the end of the accrual
period. Any progress toward the next accrual interval on the last day
of the Accrual Period is lost. This can be observed at the end of the
2011 and 2012 accrual periods as shown in the report below. For example,
the last date in the 11/30/11 â 11/29/12 Accrual Period for which Vacation
Hours are awarded is 11/26/12. The first date in 11/30/2012 â 11/29/13
Accrual Period for which Vacation Hours are awarded is 12/13/2012. The
employee works 24 hours from 11/27/2012 to 11/29/2012, which is 56 hours
short of the 80 Hours Accrual Interval Amount. On 11/30/2012 the progress
toward the next interval is reset, resulting in the employee being awarded
hours on 12/13/2012, when the employee hits a total of 80 hours in the
new accrual period. After 1/15/2012, the employee is awarded hours every
80 hours worked.

NOTE: Accrual Intervals can be forced to persist
through accrual periods, such that progress toward the next accrual interval
is not lost at the end of the Accrual Period, with the âAccrual Interval
Persists through Accrual Periodsâ Accrual Plus Feature.

![](/img/Accruals_83.png)

#### Employee Accrual Totals

As of 3/7/13, based on the Accrual Settings detailed
above and the resulting Employee Accrual Posting Records, the employee
will receive a total of 41.53847 Vacation Hours for the Accrual Period
starting 11/30/2011 and 12.30770 Vacation Hours for the Accrual Period
Starting 11/30/2012.

![](/img/BasicAccruals_049.png)

#### Employee Timecards for 11/27/12 to 11/29/12

For clarity, Timecards for the employee from 11/27/12
to 11/29/12 are shown below. Remember, progress toward the next Accrual
Interval starts over at the end of the accrual period. Any progress toward
the next accrual interval on the last day of the Accrual Period is lost.

![](/img/Accruals_73.png)

#### Employee Timecards for 11/30/12 to 12/13/12

For clarity, Timecards for the employee from 11/30/12
to 12/13/12 are shown below. Remember, progress toward the next Accrual
Interval starts over at the end of the accrual period. Any progress toward
the next accrual interval on the last day of the Accrual Period is lost.
This is clearly illustrated below. December 13th 2012 is the first date
in the 11/30/12 to 11/29/13 Accrual Period on which the employee accumulated
80 hours worked in the new accrual period.

![](/img/Accruals_76.png)

#### End of Cycle Bonus Calculation Method

The âEnd of Cycle Bonusâ calculation method awards hours to employees
on the last day of each accrual period. With this in mind, the Carry Over
Calculation Modifier must be configured in order to carry accrued hours
forward into subsequent accrual periods. The End of Cycle Bonus calculation
method is intended for use when employees are not permitted to use their
hours immediately at the start of a new accrual period. The End of Cycle
Bonus requires employee to remain employed for the duration of their first
accrual period before they are awarded hours. For new hires, the exact
duration of the first accrual period depends upon the chosen reset type
as detailed below. Regardless of the reset type chosen, End of Cycle Bonus
always awards hours to employees on the last day of each accrual period.

#### Example Employee Accruals: End of Cycle Bonus Calculation Method with Anniversary Reset Type

With the Anniversary Reset Type, the accrual period resets on the employeeâs
hire date each year. With the Anniversary Reset Type and the End of Cycle
Bonus Calculation Method, new hires will not be awarded hours until the
end of their first accrual period. For example, an employee hired on 11/6/2010
would not be awarded hours until 11/5/2011, as shown on the Example Accruals
Posting Report shown below.

#### Related Settings:

Employee Hire Date - 11/06/2010

Accrual Reset Type - Anniversary

Stop At - 120 Hours

Carry Over - ![](/img/BasicAccruals_047.png)

End of Cycle Bonus - ![](/img/AccrualPosting_AuthAmt5.png)

#### Example Employee Accrual Posting Report

####

Notice how employee hours are accrued on the last day of the Accrual
Period and carried forward for use in subsequent accrual periods.

#### Example Accrual Totals

![](/img/BasicAccruals_011.png)

#### Example Employee Accruals - End of Cycle Bonus Calculation Method with Calendar Year Reset Type

With the Calendar Year Reset Type, the accrual period resets according
to the calendar Year. With the Calendar Year Reset Type and the End of
Cycle Bonus Calculation Method, new hires will not be awarded hours until
the end of the Calendar Year during which they were hired, regardless
of when the employee was hired during the calendar year. For example,
an employee hired on 11/6/2010 would not be awarded hours until 12/31/2010,
as shown on the Example Accruals Posting Report shown below. Similarly,
an employee hired on 1/30/2010 would not be awarded hours until 12/31/2010.

#### Related Settings:

Employee Hire Date - 11/06/2010

Accrual Reset Type - Calendar
Year

Stop At - 120 Hours

Carry Over - ![](/img/BasicAccruals_066.png)

End of Cycle Bonus - ![](/img/BasicAccruals_017.png)

#### Example Posting Report

![](/img/BasicAccruals_036.png)

Notice how the employee is awarded 40 hours on 12/31/2010 for the first
time, which are carried forward to the 2011 accrual period. The employee
is then awarded hours on the last day of each subsequent accrual period
until the Stop At Amount is reached.

#### Example Accrual Totals

![](/img/BasicAccruals_022.png)

### Example Employee Accruals - End of Cycle Bonus Calculation Method with Fiscal Year Reset Type

With the Fiscal Year Reset Type, the accrual period resets according
to the Fiscal Year. With the Fiscal Year Reset Type, a Fiscal Period Start
Date of May 1st, and the End of Cycle Bonus Calculation Method, new hires
will not be awarded hours until the end of the Fiscal Year during which
they were hired, regardless of when the employee was hired during the
fiscal year. For example, an employee hired on 11/6/2010 would not be
awarded hours until 4/30/2011, as shown on the Example Accruals Posting
Report shown below. Similarly, an employee hired on 5/20/2010 would not
be awarded hours until 4/30/2011.

#### Related Settings:

Employee Hire Date - 11/06/2010

Accrual Reset Type - Fiscal
Year, Fiscal Period Start Date: May 1st

Stop At - 120 Hours

Carry Over -![](/img/AccrualPosting_AuthAmt5.png)

End of Cycle Bonus -![](/img/Accruals_70.png)

#### Example Posting Report

![](/img/Accruals_71.png)

Notice how the employee is awarded 40 hours on 4/30/2011 for the first
time, which are carried forward to the 2011 accrual period starting 5/1/11.
The employee will then be awarded hours on the last day of each subsequent
accrual period until the Stop At Amount of 120 hours is reached.

#### Example Accrual Totals

![](/img/AccrualPosting_EndOfCycle_Fiscal.png)

### Alternate Posting Calculation Method

The âAlternate Postingâ Calculation Method permits worked hours types
such as Regular Hours, Overtime One Hours, Overtime Two Hours, Overtime
Three Hours, and Overtime Four Hours to be posted to an Accrual Bucket.
InfiniTime Policy Settings
determine the exact scenarios whereby employee hours are posted to Regular
and Overtime Hours Types. Additional information on configuring Overtime
Rules for employee policies can be found here. Alternate Posting is often
used for tracking specific types of hours and awarding those hours to
employees as paid leave to be used at the employeeâs request in lieu of
payment. To configure alternate posting, the desired Hours Type(s) must
simply be added to the Alternate Posting Tab of the Accrual Calculation.
Employee Hours in the selected Hours Type will then automatically post
to the Accrual Calculation. It is important to note that employee hours
for Hours Types configured for alternate posting will not be totaled or
displayed in the timecard. An example is shown below.

![](/img/Daily.png)

Insert

- Opens the Accrual Type Alternate Posting Update Form, which permits
  the user to select hours types which will post to the respective Accrual
  Calculation.

Change

- Opens the Accrual Type Alternate Posting Update form for the selected
  Hours Type. The user may then alter the selected hours type as desired.

Delete

- Deletes the selected hours type. The hours type will no longer post
  to the respective accrual type.

Example Alternate Posting
Configuration:

#### Related Settings:

Employee Hire Date - 11/06/2010

Accrual Reset Type - Calendar Year

Stop At - 120 Hours

Carry Over -![](/img/Accruals_84.png)

Alternate Posting -![](/img/AccrueToStopAt.png)

Policy Overtime One Settings -

![](/img/Star.png)

#### Example Accrual Posting Report

![](/img/Accruals_72.png)

#### Employee Accrual Totals

![](/img/BasicAccruals_052.png)

#### Example Employee Timecards

![](/img/image8.jpg)

Notice how Overtime 1 Hours are posted directly to the Comp Time Accrual
Calculation. When Alternate Posting is enabled for a specific type of
worked hours, those hours will not total in the Timecard. In this example,
the employee works OT1 hours on 3/5, 3/7, and 3/8 as shown by the timecards
and the Accrual Posting Report above.

### Rate Mapping Calculation Method

The Rate Mapping Calculation Method is intended for use alongside the
Accrue Calculation Method. Rate Mapping makes it possible for the Accrue
Amount awarded at each Accrual Interval to be scaled based on the number
of units elapsed during the accrual period.

![](/img/BasicAccruals_049.png)

Insert

- Opens the Accrual Type Alternate Posting Update Form, which permits
  the user to select hours types which will post to the respective Accrual
  Calculation.

Change

- Opens the Accrual Type Alternate Posting Update form for the selected
  Hours Type. The user may then alter the selected hours type as desired.

Delete

- Deletes the selected hours type. The hours type will no longer post
  to the respective accrual type.

The unit, and the method for determining the number of elapsed units
during the accrual period, varies based on the Accrual Interval Unit as
illustrated by the table below.

| Accrual Interval Unit | Rate Mapping Unit |
| Day(s) | Number of Days elapsed from the Accrual Period Start Date to the âEnd Dateâ\* |
| Month(s) | Number of Months elapsed from the Accrual Period Start Date to the âEnd Dateâ\* |
| Hour(s) | Total Hours Worked for respective Employee from the Accrual Period Start Date to the âEnd Dateâ\*+ |

\*NOTE: In this scenario, with Rate Mapping and
the Accrue Calculation Methods configured, âEnd Dateâ refers to the Current
Date (IE: Today) for the current accrual period. For accrual periods in
the past, the âEnd Dateâ refers to the Accrual Period End Date which varies
according to the chosen Carry Over Reset Type (IE: 12/31 for Calendar
Year).

+For Rate Mapping Purposes, Total Hours Worked
refers to all hours worked by employees and all Other Activity Hours for
Other Activity Types set to âCount as Regular Hoursâ

InfiniTime permits an
unlimited number of Rate Mapping Records for an Accrual Calculation, allowing
for complete flexibility and control over how the Accrue Amount is scaled
based on the number of elapsed units. Each Rate Mapping Record includes
three values Min Elapsed Unit, Max Elapsed Unit, and Accrue Amount as
shown by the example rate mapping records below.

As the number of elapsed units during the accrual period increases,
the Accrue Amount awarded at each Accrual Interval is automatically adjusted
according to the Accrue Amount defined on the corresponding Rate Mapping
record. It is important to note that the number of elapsed units starts
over at 0 for each accrual period. An example rate mapping configuration
for the Hour(s) Accrual Interval Unit is provided below.

#### Example Rate Mapping Configuration with Hour(s) Accrual Interval Unit

ABC Agriculture employs a wide range of individuals, from under age
farm hands to full time dairy employees, each of which are eligible for
Vacation Hours according to the number of hours worked throughout the
year. The tables below were compiled by ABC Agriculture Management to
represent each group of employees working for the organization and to
determine the Accrue Amount for each Rate Mapping range.

| Employee Group | Hours / Day | Hours / Week | Total Annual Desired Accrual |
| Underage | < 4 | 18 | 20 |
| Part Time | 4 | 20 | 40 |
| Full Time | 8 | 40 | 80 |
| 12 Hour | 12 | 60 | 160 |
| > 12 Hour | > 12 | > 60 | 160+ |

The table above illustrates each group of employees at ABC Agriculture,
along with the total number of hours each group should receive on an annual
basis if employees work their scheduled hours each day.

| Range # | Employee Group | Min Hrs / Yr | Max Hours / Yr [Hours / Wk \* 52] | Total Hours for Range [Max Hrs / Yr - Min Hrs / Yr] | Accrual Interval |
| 1 | Underage | 0 | 936 | 936 | Every 10 Hours |
| 2 | Part Time | 936 | 1040 | 104 | Every 10 Hours |
| 3 | Full Time | 1040 | 2080 | 1040 | Every 10 Hours |
| 4 | 12 Hour | 2080 | 3120 | 1040 | Every 10 Hours |
| 5 | > 12 Hour | 3120 | 9999 | 6879 | Every 10 Hours |

The table above illustrates each group of employees at ABC Agriculture,
along with the total number of hours employees in each group can be expected
to work on an annual basis. For example, underage farm hands can be expected
to put in between 0 and 936 hours per year. The total number of hours
for each range is then calculated for use in the next table.

| Range # | Number of Accrual Intervals for Range | Desired Accrual For Range | Accrue Amount [Desired Accrual For Range / Number of Accrual Intervals for Range] | Total Accrual for Accrual Period [Cumulative Total of Accrue Amount \* Whole Integer Value of Number of Accrual Intervals] |
| 1 | 93.6 | 20 | 0.215054 | 20.000022 |
| 2 | 10.4 | 20 | 2 | 40.000022 |
| 3 | 104 | 40 | 0.384616 | 80.000086 |
| 4 | 104 | 80 | 0.769231 | 160.00011 |
| 5 | Up to 687.9 | NA | 0.769231 | 160+ |

The table above is used to calculate the total number of Accrual Intervals
for each period. The Accrue Amount for each Range is then calculated from
the Desired Accrual Total for each range and the number of accrual intervals
for the range as shown. For checks and balances purposes, the final column
âTotal Accrual For Accrual Periodâ is used to calculate the total number
of hours that will be awarded if employees in each group work their max
scheduled hours. The Min Hours, Max Hours, and Accrue Amount for each
range can then be used to complete the Rate Mapping Records as shown below.

#### Related Settings:

Employee Hire Date - 11/06/2010

Accrual Reset Type - Calendar
Year

Stop At - 200 Hours

Carry Over -

![](/img/Accruals_81.png)

#### Accrual Calculation Method Settings

![](/img/AccrueToStopAt.png)

#### Rate Mapping Records

![](/img/BasicAccruals_066.png)

#### Example Accrual Totals

![](/img/Accruals_71.png)

#### Example Accrual Posting Report

In order to fit the most relevant records from
the Accrual Posting Report on this page for example purposes, the image
below was edited to show records from different parts of 2012. The image
below does not represent all dates on which hours were posted for the
Employee.

Notice that the Accrue Amount increases throughout the year as the total
number of hours worked by the employee crosses each Min Elapsed Unit value
defined on the Rate Mapping records. For example, as an employee who works
60 hour weeks at 12 hours per day, the employee hits 936 hours on 4/18/12.
The employeeâs next day of work, 4/19/12, awards 2 hours according to
the Rate Mapping Configuration. The Accrue Amount for each Accrual Interval
continues to scale according to the Rate Mapping Records as the employee
works throughout the year. Notice that the employeeâs first day in 2013
reverts to the original Accrue Amount of 0.215054 hours since the total
number of elapsed units (IE: Worked Hours) is reset for the 2013 Accrual
Period.

![](/img/BasicAccruals_057.png)

![](/img/BasicAccruals_025.png) As a
60 Hour / Week Employee, the employee shown worked 12 hours per day M
â F throughout 2012. In this way, every fifth day of work the employee
will hit the 10 hour threshold twice. Specifically, the first two hours
on the fifth day of each week will award vacation hours for reaching the
5th 10 hour accrual interval for the week, and the 12th hour of work will
award vacation hours for reaching 6th 10 Hour accrual interval for the
week.

### Accrual Plus Module â Calculation Modifiers

Calculation â
Enter a descriptive name for the Accrual Calculation such as âVacation
Timeâ or âSick Time.â All Accrual Calculations in an Accrual Class with
multiple tenure ranges should have the same Calculation Name across all
accrual types and accrual calculations in the Accrual Class as illustrated
in the provided examples.

Stop
Accruing Date â Employees will no longer accrue hours for the
accrual calculation as of the date set in this field.

Start
Accruing Hire Date Plus â This setting is intended for use
with new hires and should only be configured on accrual calculations assigned
to accrual types with a minimum tenure of 0.  The number entered
in this field represents a number of days after the employeeâs Date of
Hire during which InfiniTime
will not calculate accruals. It helps to think of this as a probation
period, in days, during which employees will not accrue or award hours
to the employee.

Stop
At â Sets the maximum amount of hours which may be available
for the Accrual Type. InfiniTime
will stop accruing additional hours if the amount of available hours reaches
this value.

Effective
Date â The effective date defines the first day employees will
accrue hours for the accrual calculation. Employees assigned to the accrual
type prior to the effective date will not accrue hours until the effective
date. If the Effective Date is on an Accrual Calculation for a single
Accrual Type, the Effective Date should be set to the same value for the
respective Accrual Calculation across all Accrual Types in the respective
Accrual Class as shown below.

| Accrual Name: ABC Company Full Time Employee Accruals | | Employee Group (Accrual Class): Full Time | |
| Tenure Min. | Tenure Max. | Accrual Calculation | Settings |
| 0 Years | 3 Years | Vacation Time | Reset Type: Calendar Year Calculation Method(s): Start at 40 Hours Calculation Modifiers: Effective Date = 01/01/2010 |
| 3 Years | 5 Years | Vacation Time | Reset Type: Calendar Year Calculation Method(s): Start at 80 Hours Calculation Modifiers: Effective Date = 01/01/2010 |
| 5 Years | 10 Years | Vacation Time | Reset Type: Calendar Year Calculation Method(s): Start at 96 Hours Calculation Modifiers: Effective Date = 01/01/2010 |
| 10 Years | 99 Years | Vacation Time | Reset Type: Calendar Year Calculation Method(s): Start at 120 Hours Calculation Modifiers: Effective Date = 01/01/2010 |

The Table Above clearly shows that ABC Company began tracking the Vacation
Time Accrual Calculation within InfiniTime
on 01/01/2010. InfiniTime
will begin accruing Vacation Hours as of 01/01/2010 for all employees
assigned to an Accrual Type on the Full Time Class who were hired prior
to 01/01/2010.

Maximum
Negative Accrual â The Maximum Negative Accrual feature allows
the InfiniTime Administrator
to define the maximum negative balance for an accrual calculation. In
other words â the number of hours employees can use beyond their accrued
hours â is controlled by this setting. If the Maximum Negative Accrual
field is blank, Supervisors must use discretion when approving employee
requests for time off. If the Maximum Negative Accrual Field is filled,
InfiniTime will prevent
Other Activity Hours from being inserted throughout the InfiniTime Application such that an
employeeâs remaining accrual balance would exceed the maximum negative
accrual amount. An example is provided below.

The following areas of the InfiniTime Software will specifically
warn users and prevent the attempted action if an employeeâs remaining
accrual balance would exceed the maximum negative accrual amount due to
the attempted action:

- In Line Edit on the Company Timecard,
  Employee Timecard, and Employee Module Timecard
- Insertion of Other Activity Hours
  using Quick Punch on the Company Timecard, Employee Timecard, or Employee
  Module Timecard
- Approval of Time Off Requests

NOTE: Other Activity Hours Entered by supervisors
or employees at a Hardware Terminal such as the Thor are automatically
polled and posted to employee timecards within the InfiniTime
Software. When Maximum Negative Accrual is enabled, care should be taken
when inserting Other Activity Hours at hardware terminals. Hardware Terminals
such as the Thor do not have the ability to alert users when the entry
of Other Activity Hours would cause an employeeâs remaining accrual balance
to exceed the maximum negative accrual amount.

#### Related Settings:

Employee Hire Date - 11/06/2010

Accrual Reset Type - Calendar
Year

Start At - 120 Hours

Maximum Negative Accrual - 0.01
Hours

#### Example Employee Timecards

![](/img/BasicAccruals_010.png)

#### Example Employee Accrual Totals

![](/img/BasicAccruals_041.png)

#### Maximum Negative Accrual Warning:

![](/img/BasicAccruals_054.png)

Notice how the employee took five business days of vacation time from
2/04/13 to 2/08/13 for a total of 40 Vacation Hours. This exhausted the
employeeâs accrued hours leaving the employee with 0 hours remaining.
If a user or supervisor should attempt to insert additional vacation time
for the employee using Quick Punch or by approving a Time Off Request
Message, a warning will be displayed informing the user that the attempted
entry was declined as shown above.

### Accrual Calculation Tenures

In many cases, Accrual Benefits are scaled according to the number of
years an employee has been with an organization in a uniform basis across
all Accrual Calculations for a group of employees. Yet, in some circumstances,
benefits for a specific accrual calculation (or type of paid leave) may
increase at different milestones when compared with other accrual calculations
(or types of paid leave) in a single accrual class. The examples below
illustrate the different ways employee benefits can be scaled according
to the length of time an employee is with an organization, and how those
benefits can be configured within InfiniTime
using Accrual Type Tenures and Accrual Calculation Tenures.

NOTE: With the Accrual Plus Module, Accrual Calculations
assigned to an Accrual Type with a From Tenure must have Accrual Calculation
Tenures Defined. To reflect this requirement, Accrual Calculation Tenures
are shown as blue required fields on the Accrual Calculation Update Form
when the related Accrual Type has a From Tenure set.

#### Uniform Scaling of Employee Benefits

Part Time Employees at ABC Company receive 2 Days (16 Hours) of Paid
Sick Time after their first year of employment. This benefit does not
increase for part time employees based upon the amount of time they have
been with the company. ABC Company rewards Full Time and Salary employees
with additional Vacation and Personal Time benefits at the following milestones:
After 3 Years, After 5 Years, and After 10 Years of Employment. With this
in mind, ABC Company requires the following tenure ranges for each class:

| Employee Accruals Table 5 | | |
| Accrual Class: Part Time Employee Accruals | | |
| Tenure Min | Tenure Max | Accrual Calculation & Settings for Respective Tenure |
| 0 Years | 1 Year | None |
| 1 Year | 99 Years | Sick Time: 1 - 99 Years |

| Employee Accruals Table 5 | | |
| Accrual Class: Full Time Employee Accruals | | |
| Tenure Min | Tenure Max | Accrual Calculation & Settings for Respective Tenure |
| 0 Years | 3 Years | Vacation Time: 0 â 3 Years Personal Time: 0 â 3 Years |
| 3 Years | 5 Years | Vacation Time: 3 â 5 Years Personal Time: 3 â 5 Years |
| 5 Years | 10 Years | Vacation Time: 5 â 10 Years Personal Time: 5 â 10 Years |
| 10 Years | 99 Years | Vacation Time: 10 â 99 Years Personal Time: 10 â 99 Years |

| Employee Accruals Table 5 | | |
| Accrual Class: Salary Employee Accruals | | |
| Tenure Min | Tenure Max | Accrual Calculation & Settings for Respective Tenure |
| 0 Years | 3 Years | Vacation Time: 0 â 3 Years Personal Time: 0 â 3 Years |
| 3 Years | 5 Years | Vacation Time: 3 â 5 Years Personal Time: 3 â 5 Years |
| 5 Years | 10 Years | Vacation Time: 5 â 10 Years Personal Time: 5 â 10 Years |
| 10 Years | 99 Years | Vacation Time: 10 â 99 Years Personal Time: 10 â 99 Years |

Notice how each Accrual Class has Accrual Calculations which scale employee
benefits in a uniform manner at exactly the same milestones. This configuration
is supported by both the Basic Accruals Module and the Accrual Plus Module
with one difference â the Basic Accruals Module does not require entry
of Accrual Calculation Tenures where as the Accrual Plus Module does.

#### Divisible Scaling of Employee Benefits

XYZ Company employs only Salary Employees who receive Vacation Time
and Sick Time. XYZ Salary Employees are not eligible for Vacation Time
until their first year of employment is complete, though they do receive
16 Sick Time Hours after a probationary period of 90 days. Sick Time Hours
awarded to salary employees are then increased on the employeeâs first,
second, and third anniversary by a total of 8 Hours. After one year of
employment, Salary Employees are awarded 40 hours of vacation. Additionally,
Salary employees are awarded with additional Vacation Time benefits at
the following milestones: 60 Hours / Year after 3 Years, 70 Hours / Year
after 5 Years, and 80 Hours / Year after 10 Years of Employment. XYZ Company
does not carry hours forward from accrual period to accrual period for
either Sick Time or Vacation Time. These rules result in the following
milestones at which benefits are altered for each accrual calculation:

Sick Time:
1 Year, 2 Years, 3 Years

Vacation Time:
1 Year, 3 Years, 5 Years, 10 Years

Individually, this results in the following tenure ranges for each accrual
calculation:

Sick Time:
0 -1 Year, 1 - 2 Years, 2 - 3 Years, 3 â 99 Years

Vacation Time:
0 - 1 Year, 1 - 3 Years, 3 - 5 Years, 5 - 10 Years, 10 â 99 Years

Notice that the two year duration from 1 to 3 Years for Vacation Time
can be evenly divided into two one year periods: 1 â 2 Years and 2 â 3
Years to match the same tenures as required for Sick Time. The key to
understanding this when configuring Accrual Calculations is that Vacation
Time Benefits will simply not change for these tenure ranges as shown
in the table below. Additionally, the 3 â 99 Year duration can be split
into three separate tenure ranges, 3 â 5 Years, 5 â 10 Years, and 10 â
99 Years because benefits for Sick Time Hours no longer change after the
3rd year.

With this in mind, the following accrual type tenures and accrual calculations
can be used to accurately represent the required accrual calculations:

| Employee Accruals Table 5 | | |
| Accrual Class: Salary Employee Accruals | | |
| Tenure Min | Tenure Max | Accrual Calculation & Settings for Respective Tenure |
| 0 Years | 1 Years | Sick Time: 0 to 1 Years, Start At 16 Hours, Hire Date Plus 90 Days. Anniversary Reset. |
| 1 Years | 2 Years | Sick Time: 1 to 2 Years, Start At 24 Hours, Anniversary Reset. Vacation Time: 1 to 2 Years, Start at 40 Hours, Anniversary Reset. |
| 2 Years | 3 Years | Sick Time: 2 to 3 Years, Start At 32 Hours, Anniversary Reset. Vacation Time: 2 to 3 Years, Start at 40 Hours, Anniversary Reset. |
| 3 Years | 5 Years | Sick Time: 3 to 5 Years, Start At 40 Hours, Anniversary Reset. Vacation Time: 3 to 5 Years, Start at 60 Hours, Anniversary Reset. |
| 5 Years | 10 Years | Sick Time: 5 to 10 Years, Start At 40 Hours, Anniversary Reset. Vacation Time: 5 to 10 Years, Start at 70 Hours, Anniversary Reset. |
| 10 Years | 99 Years | Sick Time: 10 to 99 Years, Start At 40 Hours, Anniversary Reset. Vacation Time: 10 to 99 Years, Start at 80 Hours, Anniversary Reset. |

#### Non-Divisible, Non-Uniform Scaling of Employee Benefits

DEF Company employs only Salary Employees who receive Personal Time
and Vacation Time. DEF Salary Employees are not eligible for Personal
Time hours until their second year of employment, at which point Salary
Employees receive 16 Hours of Personal Time. After the second year of
employment, Personal Time benefits increase by 16 hours on the employeeâs
fourth, sixth, eighth, and tenth anniversaries. DEF Salary Employees are
awarded 40 Vacation Hours after a probationary period of 90 days. Vacation
Time benefits increase by 40 hours on the employeeâs fifth, tenth, and
fifteenth anniversaries. These rules result in the following milestones
at which benefits are altered for each accrual calculation:

Personal Time:
2 Years, 4 Years, 6 Years, 8 Years, 10 Years

Vacation Time:
0 Years, 5 Years, 10 Years, 15 Years

Individually, this results in the following tenure ranges for each accrual
calculation:

Personal Time: 0 -2 Years, 2 - 4 Years, 4 - 6 Years,
6 â 8 Years, 8 â 10 Years, 10 â 99 Years

Vacation Time: 0 - 5 Years, 5 - 10 Years, 10 -
15 Years, 15 - 99 Years

Notice that there is no way to evenly split the above tenure ranges
such that each tenure range includes only one record for each Accrual
Calculation. In this situation, Accrual Calculation Tenures must be used.
It is important to note that Carry Over is not supported for the secondary
Accrual Calculation in this scenario as Accrual Calculations within the
same Accrual Type must have unique Accrual Calculation Names.

With this in mind, the following accrual type tenures and accrual calculations
can be used to accurately represent the required accrual calculations:

Primary Accrual Calculation:
Vacation Time

Secondary Accrual Calculation:
Personal Time

| Employee Accruals Table 5 | | |
| Accrual Class: Salary Employee Accruals | | |
| Tenure Min | Tenure Max | Accrual Calculation & Settings for Respective Tenure |
| 0 Years | 5 Years | Vacation Time: 0 â 5 Years Personal Time 2 to 4: 2 â 4 Years Personal Time 4 to 5: 4 â 5 Years |
| 5 Years | 10 Years | Vacation Time: 5 â 10 Years Personal Time 5 to 6: 5 â 6 Years Personal Time 6 to 8: 6 â 8 Years Personal Time 8 to 10: 8 â 10 Years |
| 10 Years | 15 Years | Vacation Time: 10 â 15 Years Personal Time: 10 â 15 Years |
| 15 Years | 99 Years | Vacation Time: 10 â 99 Years Personal Time: 10 â 99 Years |

Notice how the primary accrual calculation, Vacation Time, dictates
the Accrual Type Tenures, while the secondary accrual calculation uses
Accrual Calculation tenures. Carry Over can be enabled for the Primary
Accrual Calculation because it has the same Accrual Calculation Name âVacation
Timeâ throughout all accrual types. Conversely, personal time does not
support use of Carry Over as it has multiple accrual calculations with
different names on individual accrual types.

### Authorized Day(s) / Month(s) / Hour(s)

The 'Authorized _Unit'_ Calculation
Modifier is intended for use alongside the Accrue and Rate Mapping Calculation
Methods. The Authorized Unit Calculation Modifier permits a minimum or
maximum value to be set for the number of elapsed units. The unit, and
the method for determining the number of elapsed units during the accrual
period, varies based on the Accrual Interval Unit as illustrated by the
table below.

| Accrual Interval Unit | Rate Mapping Unit |
| Day(s) | Number of Days elapsed from the Accrual Period Start Date to the âEnd Dateâ\* |
| Month(s) | Number of Months elapsed from the Accrual Period Start Date to the âEnd Dateâ\* |
| Hour(s) | Total Hours Worked for respective Employee from the Accrual Period Start Date to the âEnd Dateâ\*+ |

\*NOTE:
In this scenario, with Rate Mapping and the Accrue Calculation Methods
configured, âEnd Dateâ refers to the Current Date (IE: _Today_)
for the current accrual period. For accrual periods in the past, the âEnd
Dateâ refers to the Accrual Period End Date which varies according to
the chosen Carry Over Reset Type (IE: 12/31 for Calendar Year).

+For Rate Mapping Purposes,
Total Hours Worked refers to all hours worked by employees and all Other
Activity Hours for Other Activity Types set to âCount as Regular Hoursâ

When the 'Authorized _Unit_'
calculation modifier is configured, InfiniTime
will min/max the number of elapsed units as follows before determining
which Rate Mapping Record the employee is eligible for:

- If the number of elapsed units is less than the Authorized Unit
  Minimum, the elapsed unit will be set to the Minimum Authorized Amount
  and the actual number of elapsed units will be ignored. The Minimum
  Authorized Amount will then be used to determine which Rate Mapping
  Record the employee is eligible for.
- If the number of elapsed units is more than the Authorized Unit
  Maximum, the elapsed unit will be set to the Maximum Authorized Amount
  and the actual number of elapsed units will be ignored. The Maximum
  Authorized Amount will then be used to determine which Rate Mapping
  Record the employee is eligible for.

An example is provided below of how the Authorized Unit Calculation
Modifier can be applied is shown below using ABC Agricultures Rate Mapping
Configuration. Notice how the employeeâs total worked hours for the accrual
period (IE: Elapsed unit) is capped at 936 hours. This effectively locks
the employee into the 0.215054 Accrue Amount regardless of the number
of hours the employee works. The Minimum Authorized Unit can be used in
a similar fashion to skip an employee over the lower Rate Mapping records.
For example, a Minimum Authorized Unit of 2081 would force the employee
into the 2080 â 3120 Rate Mapping Range, effectively locking the employee
into an Accrue Amount of 0.769231 regardless of the number of hours the
employee worked.

#### _Related Settings:_

Employee Hire Date - 11/06/2010

Accrual Reset Type - Calendar
Year

Stop At - 200 Hours

Authorized Unit -

![](/img/BasicAccruals_048.png)

Carry Over -

![](/img/Accruals_82.png)

Accrual Calculation Method Settings  -

![](/img/RateMapByHours1AccrualPosting.png)

Rate Mapping Records -

![](/img/BasicAccruals_023.png)

#### Example Accrual Totals

![](/img/BasicAccruals_026.png)

#### Example Accrual Posting Report

![](/img/BasicAccruals_061.png)

As shown above, the Authorized Hour(s) value of 936 forces the Accrual
Calculation to cap the employeeâs total hours worked at 936 for the accrual
period. As a result, the employee remains on the 0 â 936 rate mapping
record for an accrue amount of 0.215054 throughout the entire year. To
ensure the report would fit on this page, only the last page of the report
is shown. Notice how the accrue amount remained at 0.215054 hours per
accrual interval into December even though the employee worked over 3120
hours.

Overflow
Into â The Overflow Into Calculation Modifier is intended for
use with the Accrue and / or Rate Mapping Calculation Methods and the
Stop At Amount Calculation Modifier. Overflow automatically directs any
accrued hours which exceed the stop at amount to a second accrual type.
In this way, hours accrued in excess of the Stop At Amount may be retained
separately from the original accrual calculation.  For example, the
Stop At Amount can be used to set a maximum limit on the number of available
Vacation Hours and Overflow can be used to separate any hours accrued
in excess of the Stop At Amount. These excess hours can then be paid out
to employees at the end of the year in lieu of permitting the employee
to use the time as paid leave. This ensures management can maintain appropriate
levels of staffing.

â

The Overflow Into option will be disabled and unavailable for use until
the following conditions are met:

- The Accrual Calculation must have a Stop At Amount set.
- The respective Accrual Type must have two or more Accrual Calculations
  configured.

Once these conditions are met, the Overflow Into option is enabled and
hours accrued in excess of the Stop At Amount can be directed to a separate
accrual calculation by setting the overflow into Drop Down to the Accrual
Calculation which hours in excess of the Stop At Amount should be posted
to.  An example is provided below.

#### Related Settings:

Employee Hire Date: 11/06/2009

Accrual Type: Full Time Employee
Accruals 0 â 99

Minimum Tenure: 0 Years

Maximum Tenure: 99 Years

Accrual
Calculation: Vacation Time

Accrual Reset Type: Calendar
Year

Accrue Calculation Method:

![](/img/BasicAccruals_026.png)

Stop At: 120

Carry Over:

![](/img/Accruals_84.png)

Maximum Negative Accrual:
0.01

Overflow Into: Payable Hours

Other Activities that Deduct:
Vacation time

Accrual
Calculation: Payable Hours

Accrual Reset Type: Calendar
Year

Other Activities that Deduct:
Payable Hours

Maximum Negative Accrual:
0.01

Example Employee Accrual Totals

Example Accrual Posting Report

Carry
Over â Available hours unused during the prior period will
be brought forward to the new accrual period if this option is checked.
If this option is unchecked unused hours during the prior period will
not be brought forward and are lost. The Accrual Plus Module introduces
two additional options which can be used independently or together:

1. Carry Over Expiration:
   Provides the ability to set an upper limit on the number of hours
   that will be carried forward from one accrual period to the next
2. Carry Over Maximum Hours:
   Provides the ability to specify a number of days during which hours
   carried forward will be available for use. After this duration expires,
   hours carried forward will no longer be available for use.

Accrual Plus Module Carry Over settings permit the user to define up
to two levels of carry over expiration. An example of each possible Carry
Over Configuration and its related function is outlined in the table below.

| Number of Carry Over Levels | Carry Over Maximum Hours | Carry Over Expiration | Function |
| 1 | Carry Over 1: No | Carry Over 1: No | Carries forward all remaining hours. Hours carried forward never expire and may be used at any time in the future. |
| 1 | Carry Over 1: No | Carry Over 1: Yes | Carries forward all remaining hours. Hours carried forward expire after the specified number of days. |
| 1 | Carry Over 1: Yes | Carry Over 1: No | Caps the number of hours carried forward. Hours carried forward never expire and may be used at any time in the future. |
| 1 | Carry Over 1: Yes | Carry Over 1: Yes | Caps the number of hours carried forward. Hours carried forward expire after the specified number of days. |
| 2 | Carry Over 1: Yes Carry Over 2: Yes | Carry Over 1: Yes Carry Over 2: Yes | Caps the number of hours carried forward. All hours carried forward expire after the number of days specified by Carry Over 1 Expiration. A certain number of the hours carried over, according to Carry Over Two Maximum Hours, expire after the number of days specified by Carry Over 2 Expiration. |

It is important to note that Employee Accrual totals are not directly
altered when the date of expiration passes for hours that were carried
forward. The InfiniTime
system utilizes the Maximum Negative Accrual feature in order to prevent
expired hours from being utilized. In this way, employees may review their
accrual history at any time and clearly view the number of hours that
were carried forward for prior accrual periods.

### Example Carry Over Configuration: One Carry Over  Level with Carry Over Expiration & Maximum Hours

#### Related Settings

Employee Hire Date: 11/06/2010

Accrual Reset Type: Calendar
Year

Start At: 80 Hours

Stop At: 120 Hours

Carry Over:

![](/img/Accruals_69.png)

Maximum Negative Accrual: 0.01
Hours

#### Example Employee Accrual Posting

![](/img/BasicAccruals_056.png)

#### Example Employee Accrual Totals

![](/img/BasicAccruals_044.png)

Notice how the employee accrues 80 hours each year and carries forward
40 hours into each subsequent accrual period. Due to the carry over expiration
setting of 60 days, the 40 hours carried forward must be used within 60
days from the date of Carry Over or InfiniTime
will consider the hours expired and prevent them from being used. For
example, in the example above the employee took two weeks of vacation
in January 2013 leaving 40 hours remaining. InfiniTime
will permit the employee to use their remaining 40 hours of vacation anytime
between 1/19/13 and 3/1/13. As of 3/2/13, the 60th day from 1/1/13, the
hours will expire and can no longer be used. If an employeeâs supervisor
should insert Vacation Time after 3/2/13 the Maximum Negative Accrual
Warning will be displayed:

![](/img/BasicAccruals_046.png)

### Example Carry Over Configuration: Two Carry Over Levels with Carry Over One and Carry Over Two Expiration & Maximum Hours

#### Related Settings

Employee Hire Date: 11/06/2010

Accrual Reset Type: Calendar
Year

Start At: 80 Hours

Stop At: 160 Hours

Carry Over:

![](/img/BasicAccruals_036.png)

Maximum Negative Accrual: 0.01
Hours

#### Example Employee Accrual Posting

####

#### Example Employee Accrual Totals

![](/img/BasicAccruals_067.png)

It is important to note that Employee Accrual totals are not directly
altered when the date of expiration passes for hours that were carried
forward. The InfiniTime
system utilizes the Maximum Negative Accrual feature in order to prevent
expired hours from being utilized. In this way, employees may review their
accrual history at any time and clearly view the number of hours that
were carried forward for prior accrual periods. In the example above,
a total of 40 Hours expired 90 days into 2013 and a total of 80 hours
expired 180 days into 2013 leaving 80 Hours remaining for use. As shown
above, the employee used 80 Hours over ten days from 9/3/13 to 9/12/13.
The Maximum Negative Accrual feature prevents the employee from using
more than 80 hours.

### Other Activities that Deduct Tab

The Other Activities that Deduct Tab is used to configure other activity
types that can be used to deduct from available accrual hours. For example
the Vacation Other Activity Type is often associated with a Vacation Accrual
Type. In this way vacation hours will automatically be deducted from available
accrual hours when employees take vacation. Each Accrual Calculation must
have at least one Other Activity Type inserted on the Other Activities
That Deduct tab deduct paid leave hours such as Vacation, Sick, or Personal
time from the accrual bucket.

![](/img/BasicAccruals_042.png)

Users should note that there is no limit to the number of Other Activity
Types that can be deducted from a single Accrual Calculation. Companies
that award employees a single bucket of Paid Leave Hours may add multiple
other activity types to the Other Activities That Deduct Tab to track
different types of hours such as Vacation Time, Sick Time, and Personal
Time separately as they are deducted from the employee's available balance.
An example of this scenario, where multiple other activity types are deducted
from a single accrual calculation, is shown below.

![](/img/AccrualPosting_EndOfCycle_Cal.png)

### Rule Based Calculation Modifiers

The following rule based calculation modifiers significantly alter the
manner in which InfiniTime
awards employee accrual hours. Rule Based Calculation Modifiers are required
by approximately one third of enterprise organizations, depending on the
complexity of the organizationâs accrual rules. With the exception of
âDo Not Allow Accrued Time to be Usedâ and âDo Not Allow Accrued Time
to be Used in Year Accruedâ if a rule based calculation modifier is enabled
on an Accrual Calculation for a single Accrual Type, the rule based calculation
modifier should be enabled for the respective Accrual Calculation across
all Accrual Types in the respective Accrual Class.

The âDo Not Allow Accrued Time to be Usedâ and âDo Not Allow Accrued
Time to be Used in Year Accruedâ options are exceptions to this rule.
These options can be used for any Accrual Calculation in an Accrual Class
as required to meet an organizationâs needs. These options are often used
specifically for probationary periods such as the first 90 days or the
first year of employment.

Do
Not Allow Accrued Time to be Used â The Do Not Allow Accrued
Time to Be Used Calculation Modifier prevents supervisors from inserting
Other Activity Hours and / or Approving Time Off Requests for the respective
accrual type by displaying the warning below. This feature is often used
for probationary periods, such as the first 90 days or the first year,
in which employees accrue hours but are not permitted to use them. Do
Not Allow Accrued Time to be Used can be used with any Calculation Method.

Do
Not Allow Accrued Time to be Used in Year Accrued â The Do
Not Allow Accrued Time to be Used in Year Accrued Calculation Modifier
is intended for use with the Carry Over Calculation Method. When checked,
InfiniTime prevents supervisors from inserting Other Activity Hours by
displaying the message below. Specifically, when this option is checked,
employees may only not use more than the number of hours that were carried
forward from prior accrual periods. Hours accrued during the current accrual
period will not be available for use.

![](/img/BasicAccruals_046.png)

NOTE: Do Not Allow Accrued Time to be Used and
Do Not Allow Accrued Time to be Used in Year Accrued require the Maximum
Negative Accrual Calculation Modifier to be configured in order to prevent
use of accrued  hours as described above. For example, if Maximum
Negative Accrual is set to 0.01 hours, any attempt to use hours when âDo
Not Allow Accrued Time to be Usedâ is enabled will cause trigger the maximum
negative accrual warning. If Maximum Negative Accrual is set to 8 Hours,
employees will be permitted to use up to 8 hours even if Do Not Allow
Accrued Time to be used is enabled.

â

Continue
to Accrue to Stop At Amount After Time is Used â The Continue
to Accrue to Stop At Amount after Time is Used Calculation Modifier is
intended for use with the Accrue Calculation Method. By default, when
âContinue to Accrue to Stop At Amount after Time is Usedâ is unchecked,
if an employee should accrue hours up to the stop at amount during an
accrual period the Accrue Calculation Method will not award additional
hours to the employee even after they have used time to drop the total
number of remaining hours below the stop at amount. When âContinue to
Accrue to Stop At Amount after Time is Usedâ is checked, InfiniTime will consider the last
date the employee used hours as the start of a new accrual interval. InfiniTime will then calculate and
award hours to the employee as appropriate based on the Accrue Calculation
method until the employeeâs remaining accrual balance reaches the stop
at amount again.

#### Related Settings:

Employee Hire Date: 11/06/2010

Accrual Reset Type: Calendar
Year

Stop At: 60 Hours

Accrue:

![](/img/Daily.png)

Carry Over:

![](/img/Accruals_69.png)

Continue to Accrue to Stop At Amount After
Time is Used:

![](/img/BasicAccruals_025.png)

#### Example Employee Accrual Totals

![](/img/BasicAccruals_029.png)

Notice how the employee carries 44.61540 Hours forward from 2011 into
the 2012 Accrual Period. The employee hits the stop at amount of 60 hours
for the first time in 2012 on 5/20/2012. As shown on the Accrual Posting
Report below for 2012, the employee then takes 8 Hours of Vacation Time
on 5/22/12. Since âcontinue to accrue to stop at amountâ is enabled,
a new 14 day accrual interval begins and the employee is awarded hours
14 days later on 6/5/12 and onward until they reach the stop at amount.

#### Example Employee Accrual Posting Report

![](/img/BasicAccruals_006.png)

### Award Immediately

Award immediately makes it possible to prorate employee accruals for
the first year of employment through use of the Accrue Calculation Method.
InfiniTime uses the Accrue
Interval Amount and Accrue Interval unit, as well as the employeeâs hire
date and the chosen Reset Type to determine the number of remaining Accrual
Intervals for the employeeâs first accrual period after the employee becomes
eligible\* for accruals. Once the employee becomes eligible for accruals\*,
the employee will be immediately awarded hours for each accrual interval
remaining in the accrual period from the date they become eligible to
the End Date of the accrual period in accordance with the Accrue Amount
set by the Accrue Calculation Method and the Carry Over Reset Type.

\*NOTE: The Effective Date and the Start Accruing
Hire Date Plus Calculation Modifiers are two features which determine
employee eligibility for Accrual Benefits.

For subsequent accrual periods, employees are awarded hours at the beginning
of the accrual period according to the number of accrual intervals in
the accrual period. An example is provided below.

#### Related Settings:

Employee Hire Date: 9/14/2010

Accrual Reset Type: Calendar
Year

Stop At: 200 Hours

Accrue:

![](/img/Accruals_75.png)

Award Immediately:

![](/img/BasicAccruals_034.png)

#### Example Accrual Totals

![](/img/Accruals_82.png)

The above screen shot was taken on 4/22/13. Notice how the employee
is awarded 40.00001 hours for the 2013 accrual period and Employee Accrual
Posting records exist for the entire year even though each accrual interval
has not yet occurred. Similarly, when the employee was originally hired
on 9/14/10 the employee was awarded 10.76923 hours based on the number
of accrual intervals remaining for the 2010 Accrual Period. This allows
employees who are hired in the middle of an accrual period to automatically
accrue a prorated number of hours based on the Accrue Calculation and
the number of remaining intervals in the accrual period from their hire
date or the date on which the employee becomes eligible for accruals.
 Award Immediately is designed for use with the Accrue Calculation
Method using either the Day(s) or Month(s) Accrual Interval Unit.

#### Example Accrual Posting Report

![](/img/BasicAccruals_041.png)

NOTE: The provided Employee Accrual Posting Report
shows records for 2013 only. Not all Accrual Posting records are shown
for the respective employee.

### Accrue Hours as if Hired at the Start of the First Accrual Interval

Accrue Hours as if Hired at the Start of the First Accrual Interval
forces all employeeâs on the accrual type to be awarded hours according
to a fixed interval through use of the Accrue Calculation Method. For
example, an organization with a biweekly pay period may wish to automatically
award employee accrual hours at the end of the pay period on a regular
basis. When âAccrue Hours as if Hired at the Start of the First Accrual
Intervalâ is enabled, InfiniTime
will determine the accrual interval that corresponds to an employeeâs
hire date and treat the employee as if they were hired at the Start of
the respective accrual interval. In this way, all employees will hit their
14th day and be awarded hours at the end of the biweekly pay period. In
order for the Accrual Interval to persist through accrual periods, such
that employees will continue to receive accrual hours on the end of the
biweekly pay period, the âAccrual Interval Persists Through Accrual Periodsâ
option must also be checked.

#### Related Settings:

Employee Hire Date: 03/06/2012

Effective Date: 11/07/2011

Accrual Reset Type: Calendar
Year

Stop At: 120 Hours

Carry Over:

![](/img/BasicAccruals_017.png)

Accrue:

![](/img/BasicAccruals_034.png)

Accrue Hours as if Hired at the Start
of the First Accrual Interval:

![](/img/BasicAccruals_010.png)

Accrual Interval Persists Through Accrual
Periods:

![](/img/HireAtStart.png)

#### Example Accrual Posting Report

![](/img/BasicAccruals_039.png)

Notice how the employeeâs first accrual period starts on 02/27/2012.
February 27th 2012 is the Start Date (IE: Day 1) of the 14 Day Accrual
Interval during which the employee is hired. The 02/27/2012 Start Date
is based on the effective date of 11/07/2011, which is the date on which
ABC Company started tracking Vacation Time within InfiniTime.
Every 14 days from 11/07/2011 the current accrual interval ends and a
new accrual interval starts on the following day.

#### Example Accrual Totals

![](/img/Accruals_78.png)

NOTE: Accrue Hours at the Start of the First Accrual
Interval is designed for use with the Accrue Calculation Method using
either the Day(s) or Month(s) Accrual Interval Unit.

In this way, all active employees assigned to the accrual type are awarded
hours on the same day. New hires are treated as if they are hired at the
beginning of the accrual interval during which they are hired and are
then awarded hours according to the Accrue Calculation Method going forward.
 This concept is illustrated by the diagrams below.

![](/img/Accruals_73.png)

The Effective Date is 11/7/2011, making 11/8/2011 the first day of the
accrual. Every 14 days thereafter, InfiniTime
will award hours to active employees who are eligible for accruals. The
first accrual interval ends on 11/21/2011 while the second accrual interval
ends on 12/5/2011. Notice that the number line above clearly indicates
that 11/21/11 is the 14th day from the effective date. Similarly â 12/5/11
is the 28th day from the effective date.

![](/img/image9.jpg)

In the example above, the employee is hired on March 6th 2012, which
falls in the 2/28/12 to 3/12/12 Accrual Interval. Since the âAccrue Hours
as if Hired at the Start of the First Accrual Intervalâ option is enabled,
the employee is treated as though they were hired on 2/27/12 and the employee
is awarded hours as of each 14 day interval going forward with the first
on 3/12/12 and the second on 3/26/12. This can be observed on the Employee
Accrual Posting Report - where the first two dates on which the employee
was awarded hours are 3/12/12 and 3/26/12. Notice that the individual
calendar days are numbered from the effective date forward for clarity.
With this in mind, it is clear that Day 126, or March 12 2012, is the
9th 14 Day Interval from the effective date:

126 Days / 14 Days per Accrual Interval =
9 Accrual Intervals.

NOTE: The above diagrams are related to the Accrual
Settings as utilized for this example. The length of the accrual interval
is determined by the Accrual Interval Amount and Accrual Interval Unit
set on the Accrue Calculation Method. Your organizationâs needs may call
for a shorter or longer Accrual Interval than that shown in the example
above.

### Accrual Interval Persists Through Accrual Periods

Accrual Interval Persists Through Accrual Periods option extends the
accrual period to include the final Accrual Interval and retains any days
or months accumulated toward the next accrual interval. Remember â the
number of days or months remaining in the accrual period from the date
the employee becomes eligible for accruals will affect the number of accrual
intervals remaining in the accrual period for which the employee will
be awarded hours.\* The expected end date for an accrual period is determined
by the Reset Type. As the expected end of the accrual period approaches,
employees may have accumulated several days or months toward the next
accrual interval. When âAccrual Interval Persists Through Accrual Periodsâ
is unchecked, accumulated progress toward the next accrual interval is
dropped and the new accrual interval starts on the expected end date.\*\*
When âAccrual Interval Persists Through Accrual Periodsâ is checked, accumulated
progress toward the next accrual interval is retained and the next accrual
period starts at the end of the current Accrual Interval. An example of
the same accrual calculation, with âAccrual Interval Persists Through
Accrual Periodsâ enabled and disabled, is shown below to illustrate how
employee accruals are affected by âAccrual Interval Persists Through Accrual
Periods.â

\*NOTE: The Effective Date and the Start Accruing
Hire Date Plus Calculation Modifiers are two features which determine
employee eligibility for Accrual Benefits.

\*\*The expected end date of an accrual period is
determined by the selected Carry Over Reset Type. For the Anniversary
Reset Type, the expected end date is the date immediately prior to the
employeeâs hire date. For the Calendar Year Reset Type, the expected end
date is December 31st. For the Fiscal Year Reset Type, the expected end
date is the date immediately prior to the Fiscal Year Start Date.

### Example: Days Accumulated toward Next Accrual Interval Retained

#### Related Settings:

Employee Hire Date: 03/06/2012

Effective Date: 10/17/2011

Accrual Reset Type: Calendar
Year

Stop At: 120 Hours

Carry Over:

![](/img/BasicAccruals_021.png)

Accrue:

![](/img/Hourly.png)

Accrue Hours as if Hired at the Start of
the First Accrual Interval:

![](/img/BasicAccruals_005.png)

Accrual Interval Persists Through Accrual
Periods:

![](/img/BasicAccruals_001.png)

#### Example Accrual Totals

![](/img/BasicAccruals_020.png)

Notice how the employee's first accrual period starts on 3/5/12 due
to the 'Accrue Hours as if Hired at the Start of the First Accrual Period'
setting. 3/5/12 is the 140th day from the effective date of 10/17/2011
or the 10th Accrual Interval from the Effective Date. The employee's last
Accrual Posting Date in 2012 is 12/24/2012, however notice that the 2012
Accrual Period is extended to 01/07/2013 in order to complete the last
accrual interval. In this way, progress accumulated toward the next accrual
interval between 12/25/2012 and 12/31/2012 (7 Days) is not lost. The 2012
accrual period is automatically extended to the End Date of the last accrual
interval - 12/25/2012 to 01/07/2013. The 2013 Accrual Period then starts
from 01/07/2013 and continues forward. The employee will then accrue hours
every 14 days going forward from 01/07/2013 - which remains in sync with
the 14 day cycle from the 10/17/2011 effective date.

#### Example Accrual Posting Report

![](/img/BasicAccruals_067.png)

NOTE: Accrual Interval Persists Through Accrual
Periods is designed for use with the Accrue Calculation Method using either
the Day(s) or Month(s) Accrual Interval Unit. The Hour(s) Accrual Interval
Unit is not supported by âAccrual Interval Persists Through Accrual Periodsâ.

### Example: Days Accumulated toward Next Accrual Interval Dropped

#### Related Settings:

Employee Hire Date: 03/06/2012

Effective Date: 10/17/2011

Accrual Reset Type: Calendar
Year

Stop At: 120 Hours

Carry Over:

![](/img/Accruals_80.png)

Accrue:

![](/img/BasicAccruals_003.png)

Accrue Hours as if Hired at the Start of
the First Accrual Interval:

![](/img/BasicAccruals_009.png)

Accrual Interval Persists Through Accrual
Periods:

####

#### Example Accrual Totals

![](/img/OneLevelCarryOver_TCEAP.png)

Notice how the employee's first accrual period starts on 3/5/12 due
to the 'Accrue Hours as if Hired at the Start of the First Accrual Period'
setting. 3/5/12 is the 140th day from the effective date of 10/17/2011
or the 10th Accrual Interval from the Effective Date. The employee's last
Accrual Posting Date in 2012 is 12/24/2012. Progress accumulated toward
the next accrual interval between 12/25/2012 and 12/31/2012 (7 Days) is
dropped when the new accrual period starts on 1/1/2013. A full fourteen
days must then pass in 2013, starting with 1/1/2013 as day 0, before additional
hours will be awarded on 1/15/13. The employee will then continue to accrue
hours during 2013 every 14 days according to the Accrue Calculation. It
is important to note that the 2013 Employee Accrual Posting Dates are
no longer in sync with the original 14 day cycle from the effective date
(10/17/2011) due to Days Accumulated Toward the next accrual interval
from 12/25/12 to 12/31/12 being dropped.

#### Example Accrual Posting Report

![](/img/RateMapByHours1AccrualPosting.png)

NOTE: Accrual Interval Persists Through Accrual
Periods is designed for use with the Accrue Calculation Method using either
the Day(s) or Month(s) Accrual Interval Unit. The Hour(s) Accrual Interval
Unit is not supported by âAccrual Interval Persists Through Accrual Periodsâ.
