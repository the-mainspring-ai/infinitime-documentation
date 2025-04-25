### Holiday Types Configuration - Introduction

Holidays allow automatic payment to employees on holidays based on specific conditions, such as working the day before or after. Before configuring holidays, you must identify employee groups eligible for different holiday benefits. Common scenarios include:

- **Employee Pay Type**: Full-time and salary employees typically receive holiday pay, while part-time employees often don't. This requires separate holiday schedule types (e.g., 'Employee Holidays' for full-time/salary and 'No Holiday Benefits' for part-time).

- **Personal/Religious Holidays**: Employees may have negotiated special holidays as part of their compensation. These can be configured as group-specific or individual employee holidays in their profiles.

All holiday types are displayed in the Holiday Schedule Types Table, accessible from the Lookups Menu.

### Holiday Schedule Types Table

The Holiday Schedule Types Table shows all configured Holiday Types in InfiniTime. These types define holiday dates and pay rates (like time and a half or double time) for employees based on their employment status and tenure.

![](/img/Conf_Holidays004.png)

**Insert Button**

- Opens the Holiday Schedule Type Update Form to create a new Holiday Type. Create separate types for different employee groups (e.g., part-time vs. full-time) or tenure levels. For example:
  - Part-time employees typically receive limited holidays
  - Full-time employees typically receive all federal holidays
  - Different types can be created for employees with different tenure levels
  - Types in the same class share the same class name
  - Employees automatically move between types in the same class when they meet tenure requirements
  - If holiday dates don't change based on tenure, only one type is needed and tenure fields can be left blank

**Change Button**

- Opens the Holiday Schedule Type Update form to modify an existing Holiday Type's configuration and dates.

**Delete Button**

- Removes the selected Holiday Type. Cannot delete if the type is assigned to employees or has associated System Holiday Timecard records.

### Holiday Schedule Type Update Form

#### General Tab

Contains settings for Holiday Type Name, Class Settings, and Tenure Settings.

![](/img/JobCosting_Config_11.gif)

**Name Field**

- Description of the Holiday Schedule Type, typically indicating the employee group it applies to.

**Class Field**

- Classes can be thought of as groups related Holiday Schedule Types together. All types in a group must share the same class name. Recommended to configure even with a single holiday type.

**Default Class Field**

- Specifies which class an employee moves to when they exhaust all policies in their current class. Recommended to configure even with a single holiday type.

**Employee Tenure From Amount Field**

- Minimum years of employment required to qualify for this Holiday Schedule Type. Leave blank if only one Holiday Type exists for a group.

**Employee Tenure To Amount Field**

- Maximum years of employment while qualifying for this Holiday Schedule Type. Leave blank if only one Holiday Type exists for a group.

**Default Holiday Schedule Type Checkbox**

- When checked, makes this the default type (highlighted in blue). Employees are automatically assigned to the Default type when:
  - They don't qualify for their current type due to tenure restrictions
  - They don't qualify for any types in their current class
  - They don't qualify for any types in their default class

### Dates Tab

The Dates Tab displays all Holiday Dates configured for the selected Holiday Type.

**Insert Button**

- Opens the Master Holiday Update form to add a new holiday date
- Each holiday must be configured individually
- InfiniTime automatically adds other activity hours for eligible employees

**Change Button**

- Opens the Master Holiday Update form for the selected Holiday Date
- Allows modification of Holiday Options and conditions
- Note: Holiday Date cannot be changed if System Holiday Timecard records exist

**Delete Button**

- Removes the selected Holiday Date from the Holiday Type
- Note: Cannot delete if System Holiday Timecard records exist

### Holiday Master Holiday Update Form

The Holiday Master Holiday Update Form defines holiday options and conditions for individual holiday dates.

#### Available Holiday Options & Conditions - General Tab

Name:
Enter the Name of Holiday.

- Enter the holiday name

**Date Field**

- Enter the holiday date
- Only one holiday can exist per date for a given holiday type
- Duplicate dates will trigger a warning

**Deduction Type Dropdown**

- Select the deduction type
- If "Accrual" is selected, an Accrual Name must be selected for posting

![](/img/clip_image018.jpg)

**Other Activity Type Field**

- Specifies the Other Activity Type for holiday hours
- Typically uses the same activity type for all holiday hours (e.g., "Holiday Time")

**All Worked Hours Are Holiday Pay**

- Controls whether employees automatically receive holiday pay
- If "No": Employees automatically receive hours if they meet requirements
- If "Yes": Employees must punch in & punch out on the holiday to receive pay

**Other Activity Hours Field**

- When "All Worked Hours Are Holiday Pay" is "No":
  - Enter the number of hours employees automatically receive (e.g., 8)

**Max Other Activity Hours Field**

- When "All Worked Hours Are Holiday Pay" is "Yes":
  - Enter the maximum hours eligible for holiday pay
  - Hours worked in excess will not receive holiday pay

**Worked Holiday Rate Multiplier Field**

- Enter the rate for holiday hours
- Used for Gross Payroll Reports

**Day Before Holiday Must Be Worked Checkbox**

- If "Yes": Employees must work the day before to receive holiday hours
- For employees without schedules: Day before is literal (e.g., Sunday for Monday holiday)
- For employees with schedules: Day before refers to first scheduled day prior to holiday

**Day After Holiday Must Be Worked**

- If "Yes": Employees must work the day after to receive holiday hours
- For employees without schedules: Day after is literal (e.g., Tuesday for Monday holiday)
- For employees with schedules: Day after refers to first scheduled day after holiday

**Note**: Day Before and Day After settings cannot be enabled for consecutive holidays (e.g., Thanksgiving and Day After Thanksgiving). Enable Day Before for first holiday and Day After for second holiday.

**Holiday Starts Day Before**

- If "Yes": Holiday pay starts at specified time on day before holiday
- Commonly used for night shifts

**Holiday Ends on Holiday**

- If "Yes": Holiday pay ends at specified time on holiday

**Holiday Ends Day After**

- If "Yes": Holiday pay ends at specified time on day after holiday

**Holiday Based on Employee's Schedule**

- If "Yes": Holiday pay matches employee's schedule for holiday date
- Employee receives holiday hours for all hours worked within schedule
- If employee doesn't work, they receive holiday hours according to scheduled hours

**Example: Holiday Based on Employee's**

| Scenario                 | Schedule                   | Holiday Date   | Result                                                 |
| ------------------------ | -------------------------- | -------------- | ------------------------------------------------------ |
| Employee Reports to Work | Mon-Fri, 8:00 AM - 4:00 PM | Friday, Dec 24 | Holiday pay for hours worked between 8:00 AM - 4:00 PM |
| Employee Has Day Off     | Mon-Fri, 8:00 AM - 4:00 PM | Friday, Dec 24 | Automatically receives 8 hours holiday pay             |

**Not a Holiday if Worked**

- If "Yes": Holiday pay is not awarded if employee works on holiday date

**Employee Required to Work**

- Requires minimum hours worked to receive holiday pay
- Can be based on:
  - Hours on holiday date
  - Hours over specified days before holiday
  - Hours over specified work weeks before holiday

**Average Hours**

- Calculates average hours over specified period
- Can be based on days or weeks before holiday
- Maximum holiday hours capped by Other Activity Hours field

**Example: Average Hours by Days**

| Setting                          | Value |
| -------------------------------- | ----- |
| Average Hours                    | Yes   |
| Days to Average                  | 21    |
| Other Activity Hours             | 10.00 |
| All Hours Worked are Holiday Pay | No    |

| Day              | Hours Worked: Scenario 1 | Hours Worked: Scenario 2 |
| ---------------- | ------------------------ | ------------------------ |
| 11/5             | 8.25                     | 11.50                    |
| 11/6             | 8.00                     | 11.25                    |
| 11/9             | 8.00                     | 12.00                    |
| 11/10            | 6.50                     | 12.00                    |
| 11/11            | 6.20                     | 8.50                     |
| 11/12            | 7.50                     | 11.50                    |
| 11/13            | 8.00                     | 12.00                    |
| 11/16            | 8.55                     | 12.00                    |
| 11/17            | 9.00                     | 12.50                    |
| 11/18            | 8.00                     | 11.00                    |
| 11/19            | 8.00                     | 11.00                    |
| 11/20            | 8.00                     | 12.00                    |
| 11/23            | 8.25                     | 12.00                    |
| 11/24            | 7.50                     | 8.00                     |
| 11/25            | 8.02                     | 8.50                     |
| Average          | 7.85                     | 11.05                    |
| Friday (Holiday) | 7.85                     | 10.00                    |

**Example: Average Hours by Weeks**

| Setting                          | Value |
| -------------------------------- | ----- |
| Average Hours                    | Yes   |
| Weeks to Average                 | 3     |
| Other Activity Hours             | 10.00 |
| All Hours Worked are Holiday Pay | No    |

| Day              | Hours Worked: Scenario 1 | Hours Worked: Scenario 2 |
| ---------------- | ------------------------ | ------------------------ |
| 11/2             | 8.25                     | 11.50                    |
| 11/3             | 8.00                     | 11.25                    |
| 11/4             | 8.00                     | 12.00                    |
| 11/5             | 6.50                     | 12.00                    |
| 11/6             | 6.20                     | 8.50                     |
| 11/9             | 7.50                     | 11.50                    |
| 11/10            | 8.00                     | 12.00                    |
| 11/11            | 8.55                     | 12.00                    |
| 11/12            | 9.00                     | 12.50                    |
| 11/13            | 8.00                     | 11.00                    |
| 11/16            | 8.00                     | 11.00                    |
| 11/17            | 8.00                     | 12.00                    |
| 11/18            | 8.25                     | 12.00                    |
| 11/19            | 7.50                     | 8.00                     |
| 11/20            | 8.02                     | 8.50                     |
| Daily Average    | 7.85                     | 11.05                    |
| Friday (Holiday) | 7.85                     | 10.00                    |

### Available Holiday Options & Conditions - Hours Mapping Tab

The Hours Mapping Tab allows mapping of scheduled and unscheduled hours worked on a Holiday Date to different hours types (e.g., Overtime Four). For more details, see the [Hours Mapping section](Product_Configuration.md#hm1_Hours_Mapping).

#### Scheduled Hours Tab

**Map Regular Hours Into Dropdown**

- Maps all Scheduled Regular Hours to selected Hours Type

**Map OT One Hours Into Dropdown**

- Maps all Scheduled OT One Hours to selected Hours Type

**Map OT Two Hours Into Dropdown**

- Maps all Scheduled OT Two Hours to selected Hours Type

**Map OT Three Hours Into Dropdown**

- Maps all Scheduled OT Three Hours to selected Hours Type

**Map OT Four Hours Into Dropdown**

- Maps all Scheduled OT Four Hours to selected Hours Type

**Example: Scheduled Hours**

- Employee schedule: 8:00 AM to 5:00 PM on 12/31/2013
- All hours worked between 8:00 AM and 5:00 PM are Scheduled Hours
- These hours are mapped according to Scheduled Hours Mapping settings

#### Unscheduled Hours Tab

**Map Regular Hours Into Dropdown**

- Maps all Unscheduled Regular Hours to selected Hours Type

**Map OT One Hours Into Dropdown**

- Maps all Unscheduled OT One Hours to selected Hours Type

**Map OT Two Hours Into Dropdown**

- Maps all Unscheduled OT Two Hours to selected Hours Type

**Map OT Three Hours Into Dropdown**

- Maps all Unscheduled OT Three Hours to selected Hours Type

**Map OT Four Hours Into Dropdown**

- Maps all Unscheduled OT Four Hours to selected Hours Type

**Example: Unscheduled Hours**

- Employee schedule: 8:00 AM to 5:00 PM on 12/31/2013
- All hours worked outside 8:00 AM to 5:00 PM (12:00 AM - 8:00 AM and 5:00 PM - 11:59 PM) are Unscheduled Hours
- These hours are mapped according to Unscheduled Hours Mapping settings

#### Additional Options

**Any Hours Worked Over Holiday Hours go Into OT Checkbox**

- Maps excess hours beyond Holiday Other Activity Hours to an overtime bucket

**Deduct Worked Holiday Hours from Weekly Overtime Checkbox**

- When checked: Hours worked on Holiday Date are excluded from weekly overtime calculations

### Available Holiday Options & Conditions - Rate Mapping Tab

The Rate Mapping Tab of the Master Holiday
Update form permits the InfiniTime
Administrator to scale the number of Other Activity Hours awarded on the
holiday date according to the number of hours worked by the employee over
a number of days prior to the holiday date. This feature is especially
useful for organizations who wish to scale Holiday benefits accordingly
for Part Time and Full Time employees based on the employee's worked hours.

#### Key Settings:

**Days to Rate Map**

- Specifies the number of days before the holiday when employee hours will be totaled and compared against rate mapping entries

**Rate Mapping Entries**

- **Insert**: Creates new rate mapping entries that define how many holiday hours employees receive based on their worked hours
  - Example: A configuration might award 2 holiday hours for every 10 hours worked

**Entry Fields:**

- **Hours Worked**: The range of hours an employee must work during the specified days to qualify
- **Other Activity Hours**: The amount of holiday hours awarded when an employee's total worked hours falls within the specified range

**Change/Delete Options:**

- **Change**: Modifies holiday options and conditions (holiday date cannot be changed if System Holiday Timecard records exist)
- **Delete**: Removes the selected holiday date (not allowed if System Holiday Timecard records exist)

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
| ...On the Holiday Date                                          | Where X is the number of hours the employee must work on the Holiday Date in order to received Fixed Benefits. The Employee Required To Work Unit Field, as highlighted in yellow, should be left blank.                                                        |
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
for Holiday Dates with Premium Pay for Worked Hours

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

| Employee must work X Hours...                                   | Required Configuration                                                                                                                                                                                                                                                                     |
| --------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| ...On the Holiday Date                                          | Where X is the number of hours the employee must work on the Holiday Date in order to received Premium Pay Benefits for all worked hours. The Employee Required To Work Unit Field, as highlighted in yellow, should be left blank.                                                        |
| ...Over Y days immediately prior to the Holiday Date            | _ Where X is the number of hours the employee must work in order to received Premium Pay Benefits for all worked hours. _ Where Y is the number of days immediately prior to the Holiday Date for which hours will be totaled to determine if the employee is eligible for Fixed Benefits. |
| ...Over Y Work Weeks prior to the Work Week of the Holiday Date | _ Where X is the number of hours the employee must work in order to received Premium Pay Benefits for all worked hours. _ Where Y is the number of work weeks prior to the Holiday Date for which hours will be totaled to determine if the employee is eligible for Fixed Benefits.       |

#### Holiday Configuration - Fixed Benefits + Premium Pay for Worked Hours

For organizations that provide for both Fixed Benefits and Premium Pay
Benefits for Worked Hours on Holiday Dates with Scheduled and Unscheduled
Hours, two sets of Holiday Dates must be created for each Calendar Date
with Holiday Benefits. First, for each Calendar Date on which employees
receive Holiday Benefits, configure a Holiday Date as appropriate for
Fixed Benefits. Refer to the above section ['Holiday
Configuration - Fixed Benefits'](Product_Configuration.md#hol12_Holiday_Types_Configuration_-_Holiday_Configuration_for_Organizations_that_Differentiate_between_Scheduled_and_Unscheduled_Hours) for additional details. Second,
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
