### Holiday Types Configuration - Introduction

Holidays make it possible to automatically pay employees
on holidays based upon certain conditions such as requiring the employee
to work the day before or the day after or both in order to receive the
holiday. Similar to the method used for configuring Policies, employee
groups eligible for different holidays must be identified before attempting
to configure holidays within the InfiniTime
Application. The most common reasons for different holiday requirements
include the following:

- Employee
  Pay Type: Salary and Full Time employees generally receive
  pay for all holidays recognized by the company. However Part Time
  employees are generally not eligible for benefits in the form of holiday
  pay. In this scenario two holiday schedule types are required. One
  entitled âEmployee Holidaysâ and another entitled âNo Holiday Benefits.â
  Salary and Full Time employees would be assigned to the âEmployee
  Holidaysâ Schedule Type where as Part Time Employees would be assigned
  to the âNo Holiday Benefitsâ type.

- Personal
  / Religious Holidays: Some employees may negotiate special
  religious or personal holidays as part of their salary or bonus package.
  A different holiday type will be required for each group or individual
  eligible for different holiday dates. Alternatively, if a holiday
  date is employee specific, the Holiday can be defined within an employee's
  profile. [See the Holidays
  Section of the Employee Profile](../ovr_SoftwareOverview.md#so177_Holidays_Section) section of this document for additional
  details on how to access the Holiday Section of the Employee Update
  Form to configure employee specific holidays.

All Holiday types configured within the InfiniTime
Software are displayed on the Holiday Schedule Types Table, which can
be accessed from the Lookups Menu as shown below.

![](/img/OTA_19.png)

### Holiday Schedule Types Table

The Holiday Schedule Types Table displays a list of all Holiday Types
configured within InfiniTime.
Holiday Types are used to define specific holiday dates for which employees
are eligible for Holiday Pay. Holiday Schedule Types are also used in
conjunction with Employee Policy settings to define specific benefits
for employees who work on holiday dates such as time and a half (1.5x
Employee Base Rate) or double time (2.x Employee Base Rate).

![](/img/Conf_Holidays004.png)

Insert

- Opens the Holiday Schedule Type Update Form which can be used
  to create a new Holiday Type. One Holiday Type should be configured for
  each group of employees with different holiday settings. Similar to policies,
  the Class System permits multiple holiday types to be created to define
  Holiday Settings for employees which receive different holiday benefits
  based on the number of years they have been employed with your organization.
  For example part time employees generally receive a limited number of
  holidays, while full time employees generally receive all federal holidays.
  A holiday schedule type would be required for each group of employees,
  one for part time and one for full time. If employee holidays should change
  based on the amount of time employees have been with the company tenures
  must be used. A new holiday schedule type entry is required for each period
  with new holiday settings, though each schedule type will use the same
  class name because they are in the same group. Employees will automatically
  be moved between Holiday Schedule Types in the same class when they meet
  tenure requirements. If employee holiday dates do not change based on
  the amount of time an individual or group is employed at an organization,
  only one Holiday Type must be defined for the respective individual and
  / or group of employees. In this case, the Tenure fields may be left blank
  as shown in the image above.

Change

- Opens the Holiday Schedule Type Update form for the selected
  Holiday Type. The InfiniTime
  Administrator may then alter the Holiday Type's configuration or its related
  Holiday Dates as desired.

Delete

- Deletes the selected Holiday Type from the Holiday Schedule Type Table.
  If a Holiday Type is assigned to an employee, or if a System Holiday Timecard
  record has been created for one or more of the Holiday Dates assigned
  to the Holiday Type, InfiniTime
  will not permit it to be deleted.

### Holiday Schedule Type Update Form

General Tab

Includes settings and options related to the Holiday Type such as Holiday
Type Name, Class Settings, and Tenure Settings.

![](/img/JobCosting_Config_11.gif)

Name â
A description of the Holiday Schedule Type. Often describes the group
of employees that will be assigned to the holiday schedule type for organizational
purposes and ease of recognition.

Class â
Classes provide grouping for Holiday Schedule Types. A class can be thought
of as a group name for a particular set of Holiday Schedule Types. The
class name must be identical for all Holiday Schedule Types in a Group.
For clarity, it is recommended that the Class name be configured even
if only one holiday type exists within the database.

Default Class

- When an employee has exhausted all the policies in the class, the employee
  will be automatically placed in a different class as specified by the
  default class. For clarity, it is recommended that the Default Class name
  be configured even if only one holiday type exists within the database.

Employee Tenure
From Amount â Minimum value, in years, that an employee must work
before qualifying for the Holiday Schedule Type. The Employee Tenure From
Amount can be left blank if only one Holiday Type is required for a group
of employees.

Employee Tenure
To Amount â Maximum value, in years, that an employee can work
while still qualifying for the Holiday Schedule Type. The Employee Tenure
From Amount can be left blank if only one Holiday Type is required for
a group of employees.

Default Holiday
Schedule Type â Check this box to make this Holiday Schedule Type
the default. Only one Holiday Schedule Type can be selected as the default,
it will be highlighted as blue in the Holiday Schedule Type Table. Employees are assigned to the Default
Holiday Schedule Type automatically if all of the following conditions
are met:

- The Employee does not qualify
  for the Holiday Schedule Type that has been assigned due to tenure
  restrictions.
- The Employee does not qualify
  for any Holiday Schedule Types in the class they are currently
  assigned to.
- The
  Employee does not qualify for any Holiday Schedule Type in the
  default class they are currently assigned to.

### Dates Tab

The Dates Tab of the Holiday Schedule Type Update Form displays each
Holiday Date configured for the respective Holiday Type.

![](/img/OTA_24.png)

Insert -
Displays the Master Holiday Update form. Used to insert a new holiday
type. Each holiday that will be assigned to the specified Holiday type
must be configured individually using this option. InfiniTime
will automatically add other activity hours for employees who meet requirements
for the holiday. A description of each field and feature is provided below.

Change -
Opens the Master Holiday Update form for the selected Holiday Date. The
InfiniTime Administrator
may then alter the Holiday Options and conditions as desired for the respective
holiday date. It is important to note that the Holiday Date should not
be changed. InfiniTime
Holidays must be configured for each individual date on a year to year
basis. InfiniTime will
prevent the user from changing the holiday date or deleting a holiday
date if a System Holiday Timecard record is present in the database for
the respective holiday date.

Delete -
Deletes the selected Holiday Date from the respective Holiday Type. It
should be noted that InfiniTime
will prevent the user from deleting a holiday date if a System Holiday
Timecard record is present in the database.

### Holiday Master Holiday Update Form

The Holiday Master Holiday Update Form is used to define holiday options
and conditions for individual holiday dates. A list of all available holiday
options and conditions is provided below.

![](/img/hs6.gif)

### Available Holiday Options & Conditions - General Tab

Name:
 Enter the Name of Holiday.

Date:
 Enter the Date of Holiday. For a given holiday type, only one holiday
may exist on each date. Attempts to insert more than one holiday on a
single date will cause a warning to be displayed indicating the Employee
Holiday Date must be unique.

Deduction
Type: Select the type of deduction.  If Accrual is selected
an Accrual Name must be selected for posting.

![](/img/clip_image018.jpg)

Other
Activity Type Specifies the Other Activity Type which will be used
to insert hours for the selected date. The same activity type is generally
used for all Holiday Hours. IE: Holiday Time

All
Worked Hours Are Holiday Pay Determines whether employees will
automatically receive pay for the holiday or if they are required to work
on the holiday before receiving hours. If this option is set to No employees
will automatically receive hours for the holiday if they meet any requirements
defined by other Holiday Options. If this option is set to Yes employees
must punch in and out on the selected date in order to receive holiday
pay.

Other
Activity Hours When All Worked Hours Are Holiday Pay is set to
No employees will automatically receive the number of hours entered in
this field. (IE: 8)

Max
Other Activity Hours When All Worked Hours Are Holiday Pay is set
to Yes employees will not receive holiday pay for hours worked in excess
of the value entered in this field.

Worked
Holiday Rate Multiplier Enter a rate for holiday hours in this
field. Holiday hours will be calculated at this rate for the purpose of
Gross Payroll Reports within the InfiniTime
Application.

Day
Before Holiday Must Be Worked If this option is set to Yes employees
must work the day before the holiday in order to receive holiday hours.
If employees do not have a default schedule defined then Day Before is
literal if the holiday is on a Monday the employee must work the day before
the holiday (Sunday) in order to receive Holiday Hours. If employees have
a default scheduled defined then Day Before refers to the first scheduled
day prior to the holiday.

\*Day
After Holiday Must Be Worked If this option is set to Yes employees
must work the day after the holiday in order to receive holiday hours.
If employees do not have a default schedule defined then Day After is
literal if the holiday is on a Monday the employee must work the day after
the holiday (Tuesday) in order to receive Holiday Hours. If employees
have a default scheduled defined then Day After refers to the first scheduled
day after to the holiday.

\*Note:
The Day Before Holiday Must be Worked and Day After Holiday Must be Worked
settings cannot be enabled for two consecutive holidays such as Thanksgiving
and The Day After Thanksgiving. In this case enable Day Before Holiday
Must be Worked for the first holiday (Thanksgiving) and Day After Holiday
Must be Worked for the second holiday (The Day After Thanksgiving.)

++
\*\*Holiday Starts Day Before
Setting this option to Yes provides the user with the ability to start
holiday pay at a certain time on the day before the holiday. This is commonly
used for night shifts.

++
\*\*Holiday Ends on Holiday
Setting this option to Yes provides the user with the ability to end holiday
pay at a certain time on the day of the holiday.

++
\*\*Holiday Ends Day After
Setting this option to Yes provides the user with the ability to end holiday
pay at a certain time on the day after the holiday.

++ \*\* Holiday Based on Employee's Schedule

- If this option is set to Yes the holiday start and end times will automatically
  be adjusted to match the employee's schedule for the date of the holiday.
  The employee will then receive Holiday Hours for all hours worked between
  the Start and End times of the holiday, as defined by the employee's schedule.
  If the employee does not report to work for the holiday date, the employee
  will receive Holiday Hours according to the number of working hours scheduled
  on the holiday date. Examples are provided below.

Example:
Holiday Based on Employee's Schedule: Employee Reports to Work

Holiday:
Friday, December 24, 2010.

Employee's
Schedule: Monday to Friday, 8:00 AM to 4:00 PM

In this scenario, the
holiday would start at 8:00 AM and end at 4:00 PM on 12/24/2010. The employee
would receive holiday hours for any hours worked between 8:00 AM and 4:00
PM on 12/24/2010.

Example:
Holiday Based on Employee's Schedule: Employee Has the Day Off and does
not report to work

Holiday:
Friday, December 24, 2010.

Employee's
Schedule: Monday to Friday, 8:00 AM to 4:00 PM

In this scenario, the
holiday would start at 8:00 AM and end at 4:00 PM on 12/24/2010. Since
the employee did not report to work, they automatically receive Holiday
Pay for 8 Hours.

\*\*Note:
Settings that alter the starting and ending day of the holiday are disabled
when 'All Worked Hours are Holiday Pay is set to No. The start and end
of a holiday can only be altered when employees are required to work the
only in order to receive Holiday Pay.

++Note:
By default, without any changes to settings that alter the starting and
ending day of the holiday, all Hours Between 12:00 AM and 11:59 PM on
the date of the holiday will be paid as Holiday Time when 'All Worked
Hours are Holiday Hours' is set to Yes.

Not a Holiday if Worked

- When set to Yes, the Other Activity
  Holiday Date will not be inserted if the employee reports to work on the
  Holiday date.

.

^^Employee
Required to Work - When set, this option requires employees
to work a minimum number of hours over a specified number of days or weeks
prior to the holiday in order to receive Holiday Pay.  It is important
to note that the 'Days' and 'Weeks' settings operate differently. The
'Days' selection totals hours over a specified number of days starting
with the day immediately before the date of the holiday. The 'Weeks' selection
totals employee hours worked over a specified number of weeks starting
with the week before the date of the holiday. Refer to the note below
for an illustration of the difference between the 'Day(s)' and 'Week(s)'
selections.

^^Average Hours
Average hours can be set to calculate average hours over a number of days
prior to the holiday or over a number of work weeks prior to the holiday.
It is important to note that the 'Days' and 'Weeks' settings operate differently.
The 'Days' selection averages hours over a specified number of days starting
with the day immediately before the date of the holiday. The 'Weeks' selection
averages employee hours worked over a specified number of weeks starting
with the week before the date of the holiday. Refer to the note below
for an illustration.

^^Note:
The images below illustrate the difference between a 3 Week(s) 21 Day(s).
Days shaded in yellow represent days which will be included in the calculation.
The boxed date indicates the date of the holiday. Notice how the 21 Day
Selection includes the days immediately before the date of the holiday
that fall during the same week of the holiday while the 3 Week Selection
does not.

![](/img/Ch2_QA_GroupSel.jpg)
                  ![](/img/Conf_Holidays009.png)

Example:
Average Hours by Days

![](/img/ud11.gif)

If Average Hours is
enabled InfiniTime will
average employee working hours for a number of days or weeks prior to
the holiday according to the 'Average the Past' Field and the Days or
Weeks Drop Down Menu. InfiniTime
will then automatically insert the calculated average for the Holiday.
The number of hours entered into the Other Activity Hours field will serve
as the maximum number of hours an employee can receive. Two Examples are
illustrated below with the following settings:

| Average Hours                    | Yes   |
| -------------------------------- | ----- |
| Days to Average                  | 21    |
| Other Activity Hours             | 10.00 |
| All Hours Worked are Holiday Pay | No    |

| Day | Hours Worked: Scenario 1 | Hours Worked: Scenario 2 |
| 11/5 | 8.25 | 11.50 |
| 11/6 | 8.00 | 11.25 |
| 11/9 | 8.00 | 12.00 |
| 11/10 | 6.50 | 12.00 |
| 11/11 | 6.20 | 8.50 |
| 11/12 | 7.50 | 11.50 |
| 11/13 | 8.00 | 12.00 |
| 11/16 | 8.55 | 12.00 |
| 11/17 | 9.00 | 12.50 |
| 11/18 | 8.00 | 11.00 |
| 11/19 | 8.00 | 11.00 |
| 11/20 | 8.00 | 12.00 |
| 11/23 | 8.25 | 12.00 |
| 11/24 | 7.50 | 8.00 |
| 11/25 | 8.02 | 8.50 |
| Average | 7.85 | 11.05 |
| Friday (Holiday) | 7.85 | 10.00 |

Example:
Average Hours by Weeks

![](/img/DeptPrem_EX_3.gif)

| Average Hours                    | Yes   |
| -------------------------------- | ----- |
| Weeks to Average                 | 3     |
| Other Activity Hours             | 10.00 |
| All Hours Worked are Holiday Pay | No    |

| Day | Hours Worked: Scenario 1 | Hours Worked: Scenario 2 |
| 11/2 | 8.25 | 11.50 |
| 11/3 | 8.00 | 11.25 |
| 11/4 | 8.00 | 12.00 |
| 11/5 | 6.50 | 12.00 |
| 11/6 | 6.20 | 8.50 |
| 11/9 | 7.50 | 11.50 |
| 11/10 | 8.00 | 12.00 |
| 11/11 | 8.55 | 12.00 |
| 11/12 | 9.00 | 12.50 |
| 11/13 | 8.00 | 11.00 |
| 11/16 | 8.00 | 11.00 |
| 11/17 | 8.00 | 12.00 |
| 11/18 | 8.25 | 12.00 |
| 11/19 | 7.50 | 8.00 |
| 11/20 | 8.02 | 8.50 |
| Daily Average | 7.85 | 11.05 |
| Friday (Holiday) | 7.85 | 10.00 |

### Available Holiday Options & Conditions - Hours Mapping Tab

The Hours Mapping Tab permits employee scheduled and unscheduled hours
worked on a Holiday Date to be mapped to a different hours type, such
as Overtime Four. Additional details on the use of Hours Mapping can be
found in the [Hours
Mapping section](Product_Configuration.md#hm1_Hours_Mapping) of this document.

Scheduled Hours Tab

Map Regular Hours
Into - When set to a specific hours type, all Scheduled Regular
Hours worked on the Holiday Date will be mapped into the selected Hours
Type.

Map OT One Hours
Into -  When set to a specific hours type, all Scheduled OT
One Hours worked on the Holiday Date will be mapped into the selected
Hours Type.

Map OT Two Hours
Into - When set to a specific hours type, all Scheduled OT Two
Hours worked on the Holiday Date will be mapped into the selected Hours
Type.

Map OT Three Hours
Into -  When set to a specific hours type, all Scheduled OT
Three Hours worked on the Holiday Date will be mapped into the selected
Hours Type.

Map OT  Four
Hours Into - When set to a specific hours type, all Scheduled OT
Four Hours worked on the Holiday Date will be mapped into the selected
Hours Type.

Scheduled Hours are hours worked which
fall within the bounds of an employee's schedule for a given date. For
example, if an employee has a schedule of 8:00 AM to 5:00 PM on 4/15/2013,
all Regular Hours, Overtime One Hours, Overtime Two Hours, Overtime Three
Hours, and Overtime Four Hours worked between 8:00 AM and 5:00 PM on 12/31/2013
will be considered Scheduled Hours and mapped according to Scheduled Hours
Mapping settings.

Unscheduled Hours Tab

Map Regular Hours
Into - When set to a specific hours type, all Unscheduled Regular
Hours worked on the Holiday Date will be mapped into the selected Hours
Type.

Map OT One Hours
Into -  When set to a specific hours type, all Unscheduled
OT One Hours worked on the Holiday Date will be mapped into the selected
Hours Type.

Map OT Two Hours
Into - When set to a specific hours type, all Unscheduled OT Two
Hours worked on the Holiday Date will be mapped into the selected Hours
Type.

Map OT Three Hours
Into -  When set to a specific hours type, all Unscheduled
OT Three Hours worked on the Holiday Date will be mapped into the selected
Hours Type.

Map OT  Four
Hours Into - When set to a specific hours type, all Unscheduled
OT Four Hours worked on the Holiday Date will be mapped into the selected
Hours Type.

Unscheduled Hours are hours worked
which fall outside the bounds of an employee's schedule for a given date.
For example, if an employee has a schedule of 8:00 AM to 5:00 PM on 12/31/2013,
all Regular Hours, Overtime One Hours, Overtime Two Hours, Overtime Three
Hours, and Overtime Four Hours worked outside of 8:00 AM to 5:00 PM on
12/31/2013 (IE: 12/31/2013 12:00 AM - 8:00 AM and 5:00 PM to 11:59 PM)
will be considered Unscheduled Hours and mapped according to Scheduled
Hours Mapping settings.

Any Hours Worked
Over Holiday Hours go Into OT - Allows you to map hours worked
in excess of the Holiday Other Activity Hours amount to an overtime bucket.

Deduct Worked
Holiday Hours from Weekly Overtime - When checked, Hours Worked
on the Holiday Date will not be counted toward weekly overtime hours.

### Available Holiday Options & Conditions - Rate Mapping Tab

The Rate Mapping Tab of the Master Holiday
Update form permits the InfiniTime
Administrator to scale the number of Other Activity Hours awarded on the
holiday date according to the number of hours worked by the employee over
a number of days prior to the holiday date. This feature is especially
useful for organizations who wish to scale Holiday benefits accordingly
for Part Time and Full Time employees based on the employee's worked hours.

![](/img/ColSel_Sel.gif)

Days to Rate Map

- Enter the number of days, prior to the holiday date, for
  which worked hours will be totaled and compared against Rate Mapping entries
  to determine how many Other Activity Hours should be awarded for each
  employee assigned to the respective holiday type.

Insert -
Displays the Holiday Rate Mapping Update Form as shown below which is
used to create new rate mapping entries. One Rate Mapping Entry should
be created for each separate Other Activity Amount to be awarded based
on employee working hours. For example,  the image above shows a
simple Holiday Rate Mapping configuration with a  break down awarding
two holiday hours for every multiple of ten  hours worked. ![](/img/Ch2_QA_SchedAvail.jpg)

Hours Worked:
 The range of hours that must be worked over the days prior to the
holiday as defined by 'Days to Rate Map' to receive the specified number
of Other Activity Hours.

Other Activity
Hours: The amount of other activity hours given when an employee's
total worked hours falls within the specified range of hours.

Change -
Opens the Master Holiday Update form for the selected Holiday Date. The
InfiniTime Administrator
may then alter the Holiday Options and conditions as desired for the respective
holiday date. It is important to note that the Holiday Date should not
be changed. InfiniTime
Holidays must be configured for each individual date on a year to year
basis. InfiniTime will
prevent the user from changing the holiday date or deleting a holiday
date if a System Holiday Timecard record is present in the database for
the respective holiday date.

Delete -
Deletes the selected Holiday Date from the respective Holiday Type. It
should be noted that InfiniTime
will prevent the user from deleting a holiday date if a System Holiday
Timecard record is present in the database.

### Holiday Types Configuration - Process Flow

Follow the steps below to
gather required information and configure holidays:

1. Identify employee groups and / or individuals
   eligible for different holidays.
2. Identify any groups and / or individuals
   requiring special consideration. Each group of employees eligible
   for different Holiday Dates and / or special considerations will require
   a different holiday schedule type.\*\*
3. List all holidays for which each group
   and is eligible.
4. List any employee specific holidays (If
   Applicable.)
5. Create a Holiday Schedule Type for each
   group of employees identified in Step 2.
6. Insert Holiday Dates as appropriate for
   each Holiday Schedule Type. Be sure to set the Holiday Features and
   Conditions appropriately for each Holiday Date.

\*\*NOTE: If only a handful of employees are eligible
for specific holidays, as often occurs in the case of some Religious Holidays,
Holiday Dates may be configured on an Employee by Employee Basis within
the Employee's Profile.

Note: Holidays dates do not automatically move
from year to year. Holiday dates records must be created for each individual
holiday date on a yearly basis. Holiday records for prior years should
not be deleted.

Note: Employee holiday eligibility does not commonly
change based upon the amount of time an individual has been with a company,
however classes and tenures can be used to provide support for this scenario.

Note: InfiniTime
7.07 permits multiple Holiday Date Entries for a single Calendar Date.
This makes it possible to configure different Hours Mapping settings for
Worked Hours on a Holiday Date (IE: A Holiday Date with All Worked Hours
are Holiday Hours = Yes) and Holiday Pay Hours awarded even when the employee
does not report to work (IE: A Holiday Date with All Worked Hours are
Holiday Hours = No).

### Holiday Types Configuration - Example Basic Configuration

ABC Company has, on an overall basis, three groups of employees with
distinct holiday settings:

- Full Time Production Employees are eligible for all company observed
  holidays, though they must work the day before and day after in order
  to receive the holiday. Full Time Production Employees who report
  to work on Holiday Dates receive OT2 for all hours worked.

Note: ABC Company Tracks Regular Hours as greater than 40
/ Weekly, OT1 Hours as >40 Weekly and OT2 Hours as Worked Holiday Hours

- Full Time Admin employees are eligible for all company observed
  holidays and are not required to work the day before or day after.
  Full Time Admin Employees are not expected to report to work on Holiday
  Dates.
- Part Time Employees are not eligible for any holidays. Holiday
  Eligibility for Full Time employees does not change based on their
  time with the company.

Additionally, two Full Time employees (Employee ID 202 and 708) observe
specific Religious Holidays. While these Holidays are not observed directly
by ABC Company â the employeeâs in question have been preapproved for
Personal Time on these dates and ABC Company would prefer if InfiniTime could handle these holidays
automatically. Employees are not required to work the day before or day
after in order to receive their Employee Specific Holidays. Employees
will not report to work on Employee Specific Holidays.

Holidays would be configured as follows for this scenario:

1. Log Into the Manager Module
2. Click on Lookups â Calculations Setup â Holiday
   Schedule Types
3. Click Insert to Create a Holiday Type
4. Set the Holiday Type Description, Class,
   Default Class, and Tenure as Appropriate
5. Click on the Dates Tab and Click Insert to
   Create a Holiday Date
6. One Holiday Date must be created for each
   Holiday Observed by ABC Company as listed below. Be sure to configure
   Holiday Features & Conditions as appropriate for each holiday
   date.
7. Employee Specific Holidays can be defined
   on the Employee Update Form:

8. Open the Employee Table
9. Search for the Employee for which the
   Employee Specific Holiday will be defined. Highlight the employee
   and click Change.
10. Click on the Holidays Tab.
11. Click Insert to Create a Holiday Date
    for the respective employee. This Holiday Date will only be created
    for the employee in question. Be sure to configure Holiday Features
    & Conditions as appropriate for each holiday date.

### ABC Company Holiday Settings:

_The tables below depict the
details that must be gathered in order to configure holidays for a customer._

**Holiday Types:**

| | | | |
||
| **Holiday Type Description** | **Holiday Type Class** | **Holiday Type Default Class** | **Holiday Type Tenure** |
| Full Time Production Holidays | Full Time Production | Full Time Production | 0 to 99 Years |
| Full Time Admin Holidays | Full Time Admin | Full Time Admin | 0 to 99 Years |
| Part Time Holidays | Part Time | Part Time | 0 to 99 Years |

### _âFull Time Production Holidaysâ - Holiday Dates:_

| | | | |
||
| **Holiday Date** | **Holiday Name** | **Holiday Hours / Other Activity Type** | **Additional Features & Conditions** |
| 1/1/12 | New Years Day | 8 Hrs: Holiday | _ Day Before Holiday Must Be Worked = Yes _ Day After Holiday Must Be Worked = Yes _ Hours Mapping: REG -> OT2 _ Hours Mapping: OT1 -> OT2 |
| 2/20/12 | Presidents Day | 8 Hrs: Holiday | _ Day Before Holiday Must Be Worked = Yes _ Day After Holiday Must Be Worked = Yes _ Hours Mapping: REG -> OT2 _ Hours Mapping: OT1 -> OT2 |
| 5/28/12 | Memorial Day | 8 Hrs: Holiday | _ Day Before Holiday Must Be Worked = Yes _ Day After Holiday Must Be Worked = Yes _ Hours Mapping: REG -> OT2 _ Hours Mapping: OT1 -> OT2 |
| 7/4/12 | Independence Day | 8 Hrs: Holiday | _ Day Before Holiday Must Be Worked = Yes _ Day After Holiday Must Be Worked = Yes _ Hours Mapping: REG -> OT2 _ Hours Mapping: OT1 -> OT2 |
| 9/3/12 | Labor Day | 8 Hrs: Holiday | _ Day Before Holiday Must Be Worked = Yes _ Day After Holiday Must Be Worked = Yes _ Hours Mapping: REG -> OT2 _ Hours Mapping: OT1 -> OT2 |
| 11/22/12 | Thanksgiving Day | 8 Hrs: Holiday | _ Day Before Holiday Must Be Worked = Yes _ Day After Holiday Must Be Worked = Yes _ Hours Mapping: REG -> OT2 _ Hours Mapping: OT1 -> OT2 |
| 11/23/12 | Day After Thanksgiving | 8 Hrs: Holiday | _ Day Before Holiday Must Be Worked = Yes _ Day After Holiday Must Be Worked = Yes _ Hours Mapping: REG -> OT2 _ Hours Mapping: OT1 -> OT2 |
| 12/24/12 | Christmas Eve | 8 Hrs: Holiday | _ Day Before Holiday Must Be Worked = Yes _ Day After Holiday Must Be Worked = Yes _ Hours Mapping: REG -> OT2 _ Hours Mapping: OT1 -> OT2 |
| 12/25/12 | Christmas Day | 8 Hrs: Holiday | _ Day Before Holiday Must Be Worked = Yes _ Day After Holiday Must Be Worked = Yes _ Hours Mapping: REG -> OT2 _ Hours Mapping: OT1 -> OT2 |
| 12/31/12 | New Years Eve | 8 Hrs: Holiday | _ Day Before Holiday Must Be Worked = Yes _ Day After Holiday Must Be Worked = Yes _ Hours Mapping: REG -> OT2 _ Hours Mapping: OT1 -> OT2 |

### _âFull Time Admin Holidaysâ - Holiday Dates:_

| | | | |
||
| **Holiday Date** | **Holiday Name** | **Holiday Hours / Other Activity Type** | **Additional Features & Conditions** |
| 1/1/12 | New Years Day | 8 Hrs: Holiday | None |
| 2/20/12 | Presidents Day | 8 Hrs: Holiday | None |
| 5/28/12 | Memorial Day | 8 Hrs: Holiday | None |
| 7/4/12 | Independence Day | 8 Hrs: Holiday | None |
| 9/3/12 | Labor Day | 8 Hrs: Holiday | None |
| 11/22/12 | Thanksgiving Day | 8 Hrs: Holiday | None |
| 11/23/12 | Day After Thanksgiving | 8 Hrs: Holiday | None |
| 12/24/12 | Christmas Eve | 8 Hrs: Holiday | None |
| 12/25/12 | Christmas Day | 8 Hrs: Holiday | None |
| 12/31/12 | New Years Eve | 8 Hrs: Holiday | None |

### _âPart Time Holidaysâ - Holiday Dates:_

| | | | |
||
| **Holiday Date** | **Holiday Name** | **Holiday Hours / Other Activity Type** | **Additional Features & Conditions** |
| NONE: Â·        Part Time Employees are not eligible for Holidays. No Holiday Dates should be added to the âPart Time Holidaysâ Holiday Type. | | | |

### _Employee ID 202 â Employee Specific Holiday Dates:_

| | | | |
||
| **Holiday Date** | **Holiday Name** | **Holiday Hours / Other Activity Type** | **Additional Features & Conditions** |
| 2/22/12 | Ash Wednesday | 8 Hrs: Personal Time | None |
| 4/6/12 | Good Friday | 8 Hrs: Personal Time | None |

### _Employee ID 708 â Employee Specific Holiday Dates:_

| | | | |
||
| **Holiday Date** | **Holiday Name** | **Holiday Hours / Other Activity Type** | **Additional Features & Conditions** |
| 12/9/12 | Hanukkah | 8 Hrs: Personal Time | None |

### **ABC Company Holiday Types within InfiniTime:**

###

### Full Time Admin Holidays:

###

### Full Time Admin Holiday Example:

###

###

###

### Full Time Production Holiday Example:

![](/img/ColSel_Down.gif)

![](/img/TaskPrem_2.gif)

![](/img/EmployeeProfile_029.png)

### Part Time Holidays â Dates Tab

_Part
Time Employees do not receive holidays. With this in mind, the âPart Time
Holidaysâ Holiday Schedule Type does not have any holiday dates defined._

**![](/img/Department-Table.gif)**

### Employee Specific Holiday Configuration Example: Employee ID 202

![](/img/JobCosting_Config_12.gif)

![](/img/EmployeeProfile_034.png)

![](/img/sched11.gif)

![](/img/Conf_Holidays012.png)

### Holiday Types Configuration - Holiday Configuration for Organizations that Differentiate between Scheduled and Unscheduled Hours

For organizations that differentiate between Scheduled and Unscheduled
Hours, employees may receive different rates of pay for Holiday Dates
depending on whether they were scheduled to work on the Holiday Date.
InfiniTime's flexible Hours
Mapping System, Holiday Options, Other Activity Types, and Payroll Export
System provide support for a variety of configurations to meet the needs
of most organizations. Before we review exactly how to separate Scheduled
and Unscheduled Hours worked on Holiday Dates within InfiniTime,
let us first discuss common incentives and benefits awarded to employees
for Holiday Dates.

| Method                                           | Description                                                                                                                                       |
| ------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| Fixed Benefits                                   | Employees receive a preset number of hours at a specific pay rate for each Holiday Date, based on specific conditions as set on the Holiday Date. |
| Premium Pay for Worked Hours                     | Employees receive a premium pay rate for worked hours (Scheduled, Unscheduled, or Both) on a Holiday Date.                                        |
| Fixed Benefits with Premium Pay for Worked Hours | Employees receive both a preset number of hours at their base rate for each Holiday Date in addition to a premium                                 |

#### Holiday Configuration - Fixed Benefits

Fixed Benefits, or a preset number of hours paid at a specific pay rate
for each Holiday date, are awarded to employees for each holiday date
based on specific Holiday Options and Conditions set on the Holiday Date.
Fixed Benefits are automatically inserted by InfiniTime
as Other Hours for the Other Activity Type selected on the Holiday Date.
When differentiating between Scheduled and Unscheduled Hours, a fixed
number of scenarios exist for individual employees on a given holiday
date as outlined below. Holiday Options and Conditions can be set to award
or deny Fixed Benefits for specific scenarios as outlined below.

| Schedule Exists on Holiday Date | Working Status                          | Note                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ------------------------------- | --------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Yes                             | Working                                 | Award: _ Holiday Dates can be configured to award Fixed Benefits only on Holiday Dates where employees work a minimum number of hours. See ' Employee Required To Work' below. Deny: _ Holiday Dates can be configured to deny Fixed Benefits if an employee works on a Holiday Date. See 'Not a Holiday If Worked' below.                                                                                                                                                                                                                                                                                                                                                                |
| Yes                             | Not Working // Facility Closed          | Award: _ Holiday Dates can be configured to award Fixed Benefits on all Holiday Dates regardless of whether employees work. To award Fixed Benefits in all situations, 'Employee Required to Work' should be blank and 'Not a Holiday if Worked' should be No. _ If the 'Employee Required To Work' option is used to require employees to work in order to receive Fixed Benefits, InfiniTime will not insert Other Hours in this scenario. Deny: \_ Holiday Dates can be configured to deny Fixed Benefits if an employee doesn't work a minimum number of hours on the holiday date. See 'Employee Required To Work' below.                                                            |
| Yes                             | Not Working // Employee Called Out Sick | Award: _ Holiday Dates can be configured to award Fixed Benefits on all Holiday Dates regardless of whether employees work. To award Fixed Benefits in all situations, 'Employee Required to Work' should be blank and 'Not a Holiday if Worked' should be No. Deny: _ Holiday Dates can be configured to deny Fixed Benefits if an employee doesn't work a minimum number of hours on the holiday date. See 'Employee Required To Work' below. \_ If employees do not receive Fixed Benefits on Holidays when they call out sick, [an Other Activity Entry can be used to offset the Holiday Pay Hours automatically created by InfiniTime.](Product_Configuration.md#ota33_Other_Hours) |
| No                              | Working // Employee Called In For Duty  | Award: _ Holiday Dates can be configured to award Fixed Benefits only on Holiday Dates where employees work a minimum number of hours. See ' Employee Required To Work' below. Deny: _ Holiday Dates can be configured to deny Fixed Benefits if an employee works on a Holiday Date. See 'Not a Holiday If Worked' below.                                                                                                                                                                                                                                                                                                                                                                |
| No                              | Not Working                             | Award: _ Holiday Dates can be configured to award Fixed Benefits on all Holiday Dates regardless of whether employees work. Deny: _ Holiday Dates can be configured to deny Fixed Benefits if an employee doesn't work a minimum number of hours on the holiday date.                                                                                                                                                                                                                                                                                                                                                                                                                     |

Fixed
Benefits - Holiday Options and Conditions

To Award Fixed Benefits,
a Holiday Date must be configured with 'All Worked Hours are Holiday Pay'
= No. For each Holiday Date, the Other Activity Hours field should be
set to the number of hours to be awarded to employees. Options and conditions
can be used to limit or adjust the total number of Other Hours awarded
to employees in specific situations as explained below. Additionally,
a single Other Activity Type such as 'Holiday Pay' should be assigned
to each Holiday Date. Pay Codes should be set as appropriate for the 'Holiday
Pay' Other Activity type to ensure the customer's Payroll Application
pays Holiday Pay Hours at the correct rate.

![](/img/Department-Table.gif)

Options and Conditions
for Fixed Benefit Holiday Dates

Date -
Required. Set the Date Field to the Calendar Date InfiniTime
should award Fixed Benefits..

Name -
Required. The Holiday Date Name must be unique. For example 'July 4th
2013 Fixed Benefits' or 'July 4th 2013 Holiday Pay'.

Deduction Type

- Required. For Fixed Benefit Holiday Dates, the deduction type should
  be set to Timecard.

Other Activity
Type - Required. For Fixed Benefit Holiday Dates, the Other Activity
Type should be set to a single Other Activity Type such as 'Holiday Pay'
for all Holiday Dates.

Other Activity
Hours - Required. For Fixed Benefit Holiday Dates, the Other Activity
Hours Field should be set to the number of hours to be awarded to eligible
employees on the respective date.

Day Before Holiday
Must be Worked - Optional. If this option is set to Yes, Fixed
Benefits will only be awarded for the respective Holiday Date if employees
work the day before the Holiday Date.

Day After Holiday
Must be Worked - Optional. If this option is set to Yes, Fixed
Benefits will only be awarded for the respective Holiday Date if employees
work the day after the Holiday Date.

Not a Holiday
If Worked - Optional. This option can be used to prevent InfiniTime from inserting Fixed Benefits
if an employee works on the Holiday Date. If 'Not a Holiday If Worked'
is set to Yes, InfiniTime
will not insert Other Hours if the employee has worked hours on the Holiday
Date.

Employee Required
To Work - Optional. This option can be used to require employees
to work a minim um number of hours before Fixed Benefits will be awarded.
The table below explains different methods for using the 'Employee Required
To Work' setting in order to require a minimum number of hours worked
On the Holiday Date, over a certain number of days immediately prior to
the Holiday Date, or over a certain number of Work Weeks prior to the
Holiday Date. [Additional
details on the difference between the 'Day(s)' and the 'Week(s)' selection
can be found above.](Product_Configuration.md#context_AverageHours)

| Employee must work X Hours...                                   | Required Configuration                                                                                                                                                                                                                                          |
| --------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ...On the Holiday Date                                          | Where X is the number of hours the employee must work on the Holiday Date in order to received Fixed Benefits.   The Employee Required To Work Unit Field, as highlighted in yellow, should be left blank.                                                      |
| ...Over Y days immediately prior to the Holiday Date            | _ Where X is the number of hours the employee must work in order to received Fixed Benefits. _ Where Y is the number of days immediately prior to the Holiday Date for which hours will be totaled to determine if the employee is eligible for Fixed Benefits. |
| ...Over Y Work Weeks prior to the Work Week of the Holiday Date | _ Where X is the number of hours the employee must work in order to received Fixed Benefits. _ Where Y is the number of work weeks prior to the Holiday Date for which hours will be totaled to determine if the employee is eligible for Fixed Benefits.       |

Average
Hours - Optional. Average hours can be used to calculate average
hours over a number of days prior to the holiday or over a number of work
weeks prior to the holiday. The final calculated average will then be
awarded to the employee, up to a maximum number of hours as controlled
by the Other Activity Hours Field. [Additional
Details on the Average Hours feature can be found above.](Product_Configuration.md#context_AverageHours)

Hours Mapping

- Optional. Scheduled and Unscheduled Hours Mapping Settings on the Hours
  Mapping Tab are applied to worked hours on the Holiday Date. Hours Mapping
  Settings can be used to map specific hours types into different columns
  on the employee timecard to control the rate at which hours are paid.
  Additional details can be found in the Hours Mapping Section of this document.

Rate Mapping

- Optional. Rate Mapping settings can be used to automatically adjust
  the number of Other Hours awarded based on the number of hours worked
  by employees over a give number of days immediately prior to the holiday
  date. [Additional details can be found
  in the Rate Mapping section above.](Product_Configuration.md#hol09_Available_Holiday_Options___Conditions_-_Rate_Mapping_Tab)

#### Holiday Configuration - Premium Pay for Worked Hours

Premium Pay for Worked Hours on a Holiday Date refers to paying employees
a premium rate above and beyond their normal base wage for worked hours
(Scheduled, Unscheduled, or Both) on a Holiday Date. Premium Pay Hours
can be automatically tracked by InfiniTime
in most scenarios and posted to the Other Activity Type selected on the
Holiday Date. When differentiating between Scheduled and Unscheduled Hours,
a fixed number of scenarios exist for individual employees on a given
holiday date as outlined below. Holiday Options and Conditions can be
set to award or deny Premium Pay for Worked Hours for specific scenarios
as outlined below.

| Schedule Exists on Holiday Date | Working Status                          | Note                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ------------------------------- | --------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Yes                             | Working                                 | Award: _ Holiday Dates can be configured to award Fixed Benefits only on Holiday Dates where employees work a minimum number of hours. See 'Employee Required To Work' below. Deny: _ Holiday Dates can be configured to deny Fixed Benefits if an employee works on a Holiday Date. See 'Not a Holiday If Worked' below. _ Holiday Dates can be configured to limit the total number of hours eligible for Premium Pay Benefits. See 'Max Other Activity Hours' below. _ Holiday Dates can be configured to limit the total number of hours eligible for Premium Pay Benefits based on an employee's scheduled working hours on the Holiday Date. See 'Holiday Based on Employee's Schedule' below. |
| Yes                             | Not Working // Facility Closed          | Not Applicable: \_ Premium Pay Benefits are only paid on worked hours. If an employee does not work on a Holiday Date, Premium Pay Benefits do not apply.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Yes                             | Not Working // Employee Called Out Sick | Not Applicable: \_ Premium Pay Benefits are only paid on worked hours. If an employee does not work on a Holiday Date, Premium Pay Benefits do not apply.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| No                              | Working // Employee Called In For Duty  | Award: _ Holiday Dates can be configured to award Fixed Benefits only on Holiday Dates where employees work a minimum number of hours. See 'Employee Required To Work' below. Deny: _ Holiday Dates can be configured to deny Fixed Benefits if an employee works on a Holiday Date. See 'Not a Holiday If Worked' below. _ Holiday Dates can be configured to limit the total number of hours eligible for Premium Pay Benefits. See 'Max Other Activity Hours' below. _ Holiday Dates can be configured to limit the total number of hours eligible for Premium Pay Benefits based on an employee's scheduled working hours on the Holiday Date. See 'Holiday Based on Employee's Schedule' below. |
| No                              | Not Working                             | Not Applicable: \* Premium Pay Benefits are only paid on worked hours. If an employee does not work on a Holiday Date, Premium Pay Benefits do not apply.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

Premium
Pay For Worked Hours - Holiday Options and Conditions

To Award Premium Pay
For Worked Hours, a Holiday Date must be configured with 'All Worked Hours
are Holiday Pay' = Yes. A single Other Activity Type such as 'Holiday
Worked' should be assigned to each Holiday Date intended for Premium Pay.
Pay Codes should be set as appropriate for the 'Holiday Worked' Other
Activity type to ensure the customer's Payroll Application pays Holiday
Pay Hours at the correct rate.

![](/img/DeptPrem_EX_3.gif)

Options and Conditions
for  Holiday Dates with Premium Pay for Worked Hours

Date -
Required. Set the Date Field to the Calendar Date InfiniTime
should award Premium Pay for Worked Hours.

Name -
Required. The Holiday Date Name must be unique. For example 'July 4th
2013 Premium Pay' or 'July 4th 2013 Holiday Worked'.

Deduction Type

- Required. For Premium Pay for Worked Hours Holiday Dates, the deduction
  type should be set to Timecard.

Other Activity
Type - Required. For Premium Pay for Worked Hours Holiday Dates,
the Other Activity Type should be set to a single Other Activity Type
such as 'Holiday Worked' for all Holiday Dates.

Max. Other Activity
Hours - Optional. For Premium Pay for Worked Hours Holiday Dates,
the Max Other Activity Hours Field sets a limit to the number of working
hours eligible for Premium Pay. If this field is left blank, all worked
hours on the holiday date will be posted to the selected Other Activity
Type.

Day Before Holiday
Must be Worked - Optional. If this option is set to Yes, Premium
Pay Benefits for Worked Hours will only be awarded for the respective
Holiday Date if employees work the day before the Holiday Date.

Day After Holiday
Must be Worked - Optional. If this option is set to Yes, Premium
Pay Benefits for Worked Hours will only be awarded for the respective
Holiday Date if employees work the day after the Holiday Date.

Holiday Starts
Day Before - Optional. Setting this option to Yes will start Premium
Pay Benefits for Worked Hours at a user specified time on the day immediately
before the holiday. This is commonly used for organizations that operate
around the clock.

Holiday Ends on
Holiday - Optional. Setting this option to Yes will end Premium
Pay Benefits for Worked Hours at a user specified time on the Holiday
Date. Hours after this time will be treated as working hours on a normal
working day and will not receive Premium Pay Benefits.

Holiday Ends Day
After - Optional. Setting this option to Yes will end Premium Pay
Benefits for Worked Hours at a user specified time on the day immediately
after the Holiday Date. This is commonly used for organizations that operate
around the clock.

Holiday Based
on Employee's Schedule - Optional. Setting this option to Yes will
limit the total number of Worked Hours eligible for Premium Pay Benefits
to the total number of hours the employee is scheduled to work on the
Holiday Date. Unlike 'Max Other Activity Hours' which sets a fixed cap
for all employees assigned to the respective Holiday Type, 'Holiday Based
on Employee's Schedule' provides the ability to set a flexible cap on
the number of Worked Hours eligible for Premium Pay Benefits based on
the total number of scheduled hours for each employee.

Not a Holiday
If Worked - Optional. This option can be used to prevent InfiniTime from inserting Premium
Pay Benefits for Worked Hours if an employee works on the Holiday Date.
If 'Not a Holiday If Worked' is set to Yes, InfiniTime
will not post worked hours to the Selected Other Activity Type.

Employee Required
To Work - Optional. This option can be used to require employees
to work a minimum number of hours in order to receive Premium Pay Benefits
for Worked Hours. The table below explains different methods for using
the 'Employee Required To Work' setting in order to require a minimum
number of hours worked On the Holiday Date, over a certain number of days
immediately prior to the Holiday Date, or over a certain number of Work
Weeks prior to the Holiday Date. [Additional
details on the difference between the 'Day(s)' and the 'Week(s)' selection
can be found above.](Product_Configuration.md#context_AverageHours)

| Employee must work X Hours...                                   | Required Configuration                                                                                                                                                                                                                                                                      |
| --------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ...On the Holiday Date                                          | Where X is the number of hours the employee must work on the Holiday Date in order to received Premium Pay Benefits for all worked hours.    The Employee Required To Work Unit Field, as highlighted in yellow, should be left blank.                                                      |
| ...Over Y days immediately prior to the Holiday Date            | _ Where X is the number of hours the employee must work  in order to received Premium Pay Benefits for all worked hours. _ Where Y is the number of days immediately prior to the Holiday Date for which hours will be totaled to determine if the employee is eligible for Fixed Benefits. |
| ...Over Y Work Weeks prior to the Work Week of the Holiday Date | _ Where X is the number of hours the employee must work in order to received Premium Pay Benefits for all worked hours. _ Where Y is the number of work weeks prior to the Holiday Date for which hours will be totaled to determine if the employee is eligible for Fixed Benefits.        |

#### Holiday Configuration - Fixed Benefits + Premium Pay for Worked Hours

For organizations that provide for both Fixed Benefits and Premium Pay
Benefits for Worked Hours on Holiday Dates with Scheduled and Unscheduled
Hours, two sets of Holiday Dates must be created for each Calendar Date
with Holiday Benefits. First, for each Calendar Date on which employees
receive Holiday Benefits, configure a Holiday Date as appropriate for
Fixed Benefits. Refer to the above section ['Holiday
Configuration - Fixed Benefits'](Product_Configuration.md#hol12_Holiday_Types_Configuration_-_Holiday_Configuration_for_Organizations_that_Differentiate_between_Scheduled_and_Unscheduled_Hours) for additional details.  Second,
for each Calendar Date on which employees receive Premium Pay for Worked
Hours, configure a Holiday Date as appropriate for Premium Pay for Worked
Hours. Refer to the above section ['Holiday
Configuration - Premium Pay for Worked Hours'](Product_Configuration.md#hol14_Holiday_Configuration_-_Premium_Pay_for_Worked_Hours) for additional details.
InfiniTime will automatically
award both Fixed Benefits and Premium Pay for Worked Hours based on the
Holiday Options and Conditions set for each individual holiday date. With
this in mind, special care should be taken to configure each individual
holiday date with appropriate Holiday Options and Conditions to match
the needs of your organization.

### Holiday Configuration Procedure - Fixed Benefits and Premium Pay for Worked Hours with Scheduled & Unscheduled Hours

For clarity, an example is provided below showing complete configuration
for a single Calendar Date in order to award both Fixed Benefits and Premium
Pay for Worked Hours. Customers wishing to configure holidays for both
Fixed Benefits and Premium Pay for Worked Hours w/ Scheduled and Unscheduled
hours can follow the procedure below to configure holidays.

Holiday Configuration
Procedure: Fixed Benefits + Premium Pay For Worked Hours w/ Scheduled
& Unscheduled Hours

1. Ensure Employee Policies
   are configured to separate employee worked hours into OT1, OT2, OT3,
   and OT4 as appropriate to meet your organization's needs.
2. List
   each set of Employees Eligible for Holiday Benefits on Different Calendar
   Dates.
3. List
   each Calendar Date for each set of Employees Eligible for Holiday
   Benefits on Different Calendar Dates.
4. Create
   One Holiday Type for each Set of Employees.
5. Create
   One Fixed Benefit Holiday Date for each Calendar Date. Configure Holiday
   Options and Conditions as appropriate to award Fixed Benefits according
   to your organization's Time and Attendance & Labor Policies.
6. Create One Premium Pay For Worked
   Hours Holiday Date for Each Calendar Date. Configure Holiday Options
   and Conditions as appropriate to award Fixed Benefits according to
   your organization's Time and Attendance & Labor Policies.
7. Use
   Quick Assign to assign employees to the appropriate Holiday Type.

### Example Holiday Configuration - XYZ Hospitality Corporation

1.  Ensure Employee Policies are configured to separate employee worked hours
    into OT1, OT2, OT3, and OT4 as appropriate to meet your organization's
    needs.

XYZ Hospitality has two sets of employees,
Hourly Operations Employees and Salary Administrative Employees. Hourly
Operations Employees receive Daily Overtime after 10 hours in a day. Additionally,
all unscheduled hours are paid at 200% of an employee's pay rate. Salary
Administrative Employees receive Daily Overtime after 8 hours worked in
a day. Additionally, all unscheduled hours on regular working days are
paid at 200% of an employee's base rate. For Holiday Dates, XYZ Hospitality
pays a specific rate for Scheduled Regular Hours (200%), Scheduled Overtime
Hours (250%), Unscheduled Regular Hours (300%), and Unscheduled Overtime
Hours (350%). For this reason, due to the [Hours
Mapping Hierarchy](Product_Configuration.md#hm19_3._Understand_how_the_Hours_Mapping_Hierarchy_will_affect_your_pay_premium_s_) Unscheduled Regular Hours and Unscheduled Overtime
Hours must be mapped in to separate Overtime buckets as shown below, even
though they are paid at a the same rate on regular working days.

| Policy / Set of Employees       | OT1 Hours (Daily OT)                       | OT2 Hours (Unscheduled Regular Hours)               | OT3 Hours (Unscheduled OT1 Hours)               | OT4 Hours |
| ------------------------------- | ------------------------------------------ | --------------------------------------------------- | ----------------------------------------------- | --------- |
| Hourly Operations Employees     | Daily > 10 Hours Paid at 150% of Base Rate | Unscheduled Regular Hours Paid at 200% of Base Rate | Unscheduled OT1 Hours Paid at 200% of Base Rate | N/A       |
| Salary Administrative Employees | Daily > 8 Hours Paid at 150% of Base Rate  | Unscheduled Regular Hours Paid at 200% of Base Rate | Unscheduled OT1 Hours Paid at 200% of Base Rate | N/A       |

2. List
   each set of Employees Eligible for Holiday Benefits on Different Calendar
   Dates.

XYZ Hospitality pays the same Holiday Benefits
for both Hourly Operations Employees and Salary Administrative Employees.
Only a single Holiday Type is required for XYZ Hospitality as shown below.

![](/img/OTA_30.png)

3. List
   each Calendar Date for each set of Employees Eligible for Holiday
   Benefits on Different Calendar Dates.

XYZ Hospitality pays both Fixed Benefits
and Premium Pay for Worked Hours for the following holiday dates.

| Calendar Dates - Hourly Operations Employees and Salary Administrative Employees |         |        |          |
| -------------------------------------------------------------------------------- | ------- | ------ | -------- |
| 1/1/2013                                                                         | 2/18/13 | 7/4/13 | 11/28/13 |
| 1/21/13                                                                          | 2/27/13 | 9/2/13 | 12/25/13 |

4. Create
   One Holiday Type for each Set of Employees

Since all employees at XYZ Hospitality
receive the same Holiday Benefits, only one Holiday Type is required.

| XYZ Hospitality Holiday Types |
| ----------------------------- |

5. Create One Fixed
   Benefit Holiday Date for each Calendar Date. Configure Holiday Options
   and Conditions as appropriate to award Fixed Benefits according to
   your organization's Time and Attendance & Labor Policies.

The table
below shows the Pay Code, Pay Rate, and Other Activity Type configuration
for Fixed Holiday Dates as used by XYZ Hospitality.

| Other Activity Type & Other Activity Options                                   | Regular Hours                               | OT1 Hours (Daily OT) | OT2 Hours (Unscheduled Regular Hours) | OT3 Hours (Unscheduled OT1 Hours) | OT4 Hours |
| ------------------------------------------------------------------------------ | ------------------------------------------- | -------------------- | ------------------------------------- | --------------------------------- | --------- |
| Holiday Pay _ Count as Regular Hours Not Checked _ Count as Day Worked Checked | Paid at Base Rate Payroll Mapping Code 'HP' | N/A                  | N/A                                   | N/A                               | N/A       |

An example
of a Fixed Holiday Date is shown below.

![](/img/JobPrem_4.gif)

With this
configuration, Fixed Holiday Benefits will be inserted automatically and
manually in the scenarios shown below. Supervisors at XYZ hospitality
will need to insert Fixed Holiday Benefits manually on Scheduled Non Working
Days where the office is closed and employees receive Holiday Benefits.
XYZ Hospitality specifically chose to enable 'Employee Required To Work'
and manually enter Holiday Pay in one scenario in order to ensure employees
would not be accidentally overpaid by automatic Holiday Pay entries. With
this configuration, if supervisors should neglect to insert employee holiday
hours an adjustment can be made to pay additional hours to the employee
during the next pay period.

| Schedule Exists on Holiday Date | Working Status                          | Fixed Holiday Benefits Awarded?                                                                                                                                                                                                                                                                                                                                                                                    |
| ------------------------------- | --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Yes                             | Working                                 | Yes - Automatically Inserted by Fixed Benefit Holiday - 8 Holiday Pay Hours. Employees must also work the day before and day after the holiday date in order to receive Holiday Pay.                                                                                                                                                                                                                               |
| Yes                             | Not Working // Facility Closed          | Yes - Manually Inserted by Supervisors - 8 Holiday Pay Hours. Employees who work the day before and day after the holiday date are eligible to receive Holiday Pay. Holiday Pay Hours must be manually inserted by XYZ Hospitality Supervisors in this scenario. InfiniTime will not automatically award Holiday Pay Hours in this scenario because the employee did not work at least 1 hour on the holiday date. |
| Yes                             | Not Working // Employee Called Out Sick | No - No Supervisor Action Required.  InfiniTime will not award Holiday Pay Hours in this scenario because the employee did not work at least 1 hour on the holiday date.                                                                                                                                                                                                                                           |
| No                              | Working // Employee Called In For Duty  | Yes - Automatically Inserted by Fixed Benefit Holiday - 8 Holiday Pay Hours. Employees must also work the day before and day after the holiday date in order to receive Holiday Pay.                                                                                                                                                                                                                               |
| No                              | Not Working                             | No - No Supervisor Action Required.  InfiniTime will not award Holiday Pay Hours in this scenario because the employee did not work at least 1 hour on the holiday date. In this scenario, the holiday date was a Day Off as part of the employee's normal schedule. XYZ Hospitality does not pay Holiday Benefits on Holiday dates where employees do not report to work and are not scheduled to work.           |

Notice how
a Fixed Holiday Date is configured for each Calendar Date on which employees
at XYZ Hospitality receive Holiday benefits as shown below.

![](/img/Conf_Holidays002.png)

6. Create
   One Premium Pay For Worked Hours Holiday Date for Each Calendar Date.
   Configure Holiday Options and Conditions as appropriate to award Premium
   Pay for Worked Hours Benefits according to your organization's Time
   and Attendance & Labor Policies.

The table below shows the Pay Code,
Pay Rate, and Other Activity Type configuration for Premium Pay for Worked
Hours Holiday Dates as used by XYZ Hospitality.

| Other Activity Type & Other Activity Options                                  | Regular Hours                                                                                     | OT1 Hours (Daily OT)                                                                                                                                 | OT2 Hours (Unscheduled Regular Hours)                                                                 | OT3 Hours (Unscheduled OT1 Hours)                                                                 | OT4 Hours |
| ----------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | --------- |
| Holiday Worked _ Count as Regular Hours Checked _ Count as Day Worked Checked | _ Scheduled Regular Hours on a Holiday Date _ Paid at 200% Base Rate \_ Payroll Mapping Code 'HW' | _ Scheduled Overtime Hours on a Holiday Date (Daily > 8 / > 10 Depending on Employee Policy) _ Paid at 250% Base Rate \_ Payroll Mapping Code 'HWOT' | _ Unscheduled Regular Hours on a Holiday Date _ Paid at 300% Base Rate \_ Payroll Mapping Code 'HWUH' | _ Unscheduled OT1 Hours on a Holiday Date _ Paid at 350% Base Rate \_ Payroll Mapping Code 'HWUO' | \* N/A    |

An example
of a Premium Pay for Worked Hours Holiday Date is shown below.

![](/img/hol31.png)

With this
configuration, Premium Pay for Worked Hours Holiday Benefits will tracked
automatically in the scenarios shown below.

| Schedule Exists on Holiday Date | Working Status                          | Fixed Holiday Benefits Awarded?                                                                                                                                                                                                      |
| ------------------------------- | --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Yes                             | Working                                 | Yes - Worked Hours are automatically posted to the Holiday Worked Other Activity Type and separated according to hours type. Employees must also work the day before and day after the holiday date in order to receive Holiday Pay. |
| Yes                             | Not Working // Facility Closed          | No - No Supervisor Action Required.  InfiniTime will not award Premium Pay for Worked Hours Holiday Benefits in this scenario because the employee did not work.                                                                     |
| Yes                             | Not Working // Employee Called Out Sick | No - No Supervisor Action Required.  InfiniTime will not award Premium Pay for Worked Hours Holiday Benefits in this scenario because the employee did not work.                                                                     |
| No                              | Working // Employee Called In For Duty  | Yes - Worked Hours are automatically posted to the Holiday Worked Other Activity Type and separated according to hours type. Employees must also work the day before and day after the holiday date in order to receive Holiday Pay. |
| No                              | Not Working                             | No - No Supervisor Action Required.  InfiniTime will not award Premium Pay for Worked Hours Holiday Benefits in this scenario because the employee did not work.                                                                     |

Notice how
a Premium Pay for Worked Hours Holiday Date is configured for each Calendar
Date on which employees at XYZ Hospitality receive Holiday benefits as
shown below.

![](/img/hs4.gif)

7.  Use Quick Assign to assign employees to the appropriate Holiday Type.

Refer to
the Quick Assign and Employee Filter sections of this document for complete
instructions on use of Quick Assign.

![](/img/OTA_28.png)
