## Setup Guide

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
permits multiple Holiday Date Entries for a single Calendar Date.
This makes it possible to configure different Hours Mapping settings for
Worked Hours on a Holiday Date (IE: A Holiday Date with All Worked Hours
are Holiday Hours = Yes) and Holiday Pay Hours awarded even when the employee
does not report to work (IE: A Holiday Date with All Worked Hours are
Holiday Hours = No).

#### How to configure Holiday with Fixed Benefits

Fixed Benefits provide preset hours paid at specific rates for each Holiday date based on Holiday Options and Conditions. InfiniTime automatically inserts these as Other Hours for the Other Activity Type selected on the Holiday Date.

When differentiating between Scheduled and Unscheduled Hours, these scenarios exist for employees on holidays:

| Schedule Exists on Holiday Date | Working Status                          | Note                                                                                                                                                                                                                                                                                                                                                                                         |
| ------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Yes                             | Working                                 | Award: Holiday Dates can award Fixed Benefits when employees work minimum required hours. See 'Employee Required To Work' below. Deny: Can deny Fixed Benefits if an employee works on a Holiday Date. See 'Not a Holiday If Worked' below.                                                                                                                                                  |
| Yes                             | Not Working // Facility Closed          | Award: Holiday Dates can award Fixed Benefits regardless of work status. For all situations, 'Employee Required to Work' should be blank and 'Not a Holiday if Worked' should be No. If 'Employee Required To Work' option is used, InfiniTime won't insert Other Hours in this scenario. Deny: Can deny benefits if minimum hours aren't worked. See 'Employee Required To Work'.           |
| Yes                             | Not Working // Employee Called Out Sick | Award: Holiday Dates can award Fixed Benefits regardless of work status. For all situations, 'Employee Required to Work' should be blank and 'Not a Holiday if Worked' should be No. Deny: Can deny benefits if minimum hours aren't worked. If employees don't receive benefits when sick, [Other Activity Entry can offset Holiday Pay Hours](Product_Configuration.md#ota33_Other_Hours). |
| No                              | Working // Employee Called In For Duty  | Award: Holiday Dates can award Fixed Benefits when employees work minimum required hours. Deny: Can deny Fixed Benefits if an employee works on a Holiday Date. See 'Not a Holiday If Worked' below.                                                                                                                                                                                         |
| No                              | Not Working                             | Award: Holiday Dates can award Fixed Benefits regardless of work status. Deny: Can deny benefits if minimum hours aren't worked.                                                                                                                                                                                                                                                             |

Fixed Benefits - Holiday Options and Conditions

To Award Fixed Benefits, a Holiday Date requires 'All Worked Hours are Holiday Pay' = No. Set Other Activity Hours to the number of hours awarded to employees. Options can limit or adjust the total number of Other Hours for specific situations. Assign a single Other Activity Type (e.g., 'Holiday Pay') to each Holiday Date. Configure Pay Codes for the Other Activity type to ensure correct payment rates.

Options and Conditions for Fixed Benefit Holiday Dates

Date - Required. Calendar Date for Fixed Benefits.

Name - Required. Unique Holiday Date Name (e.g., 'July 4th 2013 Fixed Benefits').

Deduction Type - Required. Set to Timecard for Fixed Benefit Holiday Dates.

Other Activity Type - Required. Set to a single type (e.g., 'Holiday Pay') for all Holiday Dates.

Other Activity Hours - Required. Number of hours awarded to eligible employees.

Day Before Holiday Must be Worked - Optional. If Yes, benefits only awarded if employees work the day before.

Day After Holiday Must be Worked - Optional. If Yes, benefits only awarded if employees work the day after.

Not a Holiday If Worked - Optional. If Yes, InfiniTime won't insert Other Hours when employee works on the Holiday Date.

Employee Required To Work - Optional. Requires minimum hours worked before awarding benefits. Options explained below:

| Employee must work X Hours...                                   | Required Configuration                                                                                             |
| --------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| ...On the Holiday Date                                          | X = minimum hours required on Holiday Date. Leave Employee Required To Work Unit Field blank.                      |
| ...Over Y days immediately prior to the Holiday Date            | X = minimum hours required. Y = number of days before Holiday Date for which hours count toward eligibility.       |
| ...Over Y Work Weeks prior to the Work Week of the Holiday Date | X = minimum hours required. Y = number of work weeks before Holiday Date for which hours count toward eligibility. |

Average Hours - Optional. Calculates average hours over days/weeks prior to holiday. Maximum award limited by Other Activity Hours. [Details above.](Product_Configuration.md#context_AverageHours)

Hours Mapping - Optional. Applied to worked hours on Holiday Date. Maps specific hours types to different timecard columns to control payment rates.

Rate Mapping - Optional. Adjusts Other Hours based on hours worked over days before the holiday. [Details in Rate Mapping section.](Product_Configuration.md#hol09_Available_Holiday_Options___Conditions_-_Rate_Mapping_Tab)

#### Holiday Configuration - Premium Pay for Worked Hours

Premium Pay for Worked Hours provides higher pay rates for hours worked on holidays (Scheduled, Unscheduled, or Both). InfiniTime tracks these hours and posts them to the designated Other Activity Type. Holiday Options and Conditions control when Premium Pay is awarded or denied:

| Schedule Exists on Holiday Date | Working Status                          | Note                                                                                                                                                                                                                                                                                                               |
| ------------------------------- | --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Yes                             | Working                                 | Award: Holiday Dates can award benefits when employees work minimum hours (see 'Employee Required To Work'). Deny: Can deny benefits if employee works (see 'Not a Holiday If Worked'). Hours can be limited by 'Max Other Activity Hours' or by employee's schedule (see 'Holiday Based on Employee's Schedule'). |
| Yes                             | Not Working // Facility Closed          | Not Applicable: Premium Pay Benefits only apply to worked hours. No benefits if employee doesn't work.                                                                                                                                                                                                             |
| Yes                             | Not Working // Employee Called Out Sick | Not Applicable: Premium Pay Benefits only apply to worked hours. No benefits if employee doesn't work.                                                                                                                                                                                                             |
| No                              | Working // Employee Called In For Duty  | Award: Holiday Dates can award benefits when employees work minimum hours (see 'Employee Required To Work'). Deny: Can deny benefits if employee works (see 'Not a Holiday If Worked'). Hours can be limited by 'Max Other Activity Hours' or by employee's schedule (see 'Holiday Based on Employee's Schedule'). |
| No                              | Not Working                             | Not Applicable: Premium Pay Benefits only apply to worked hours. No benefits if employee doesn't work.                                                                                                                                                                                                             |

Premium Pay For Worked Hours - Holiday Options and Conditions

To award Premium Pay, configure Holiday Date with 'All Worked Hours are Holiday Pay' = Yes. Assign a single Other Activity Type (e.g., 'Holiday Worked') to each Holiday Date. Configure appropriate Pay Codes for this activity type to ensure correct payment rates.

![](/img/DeptPrem_EX_3.gif)

Options and Conditions for Holiday Dates with Premium Pay for Worked Hours

Date - Required. Calendar Date for Premium Pay.

Name - Required. Unique Holiday Date Name (e.g., 'July 4th 2013 Premium Pay').

Deduction Type - Required. Set to Timecard for Premium Pay Holiday Dates.

Other Activity Type - Required. Set to a single type (e.g., 'Holiday Worked') for all Holiday Dates.

Max. Other Activity Hours - Optional. Limits working hours eligible for Premium Pay. If blank, all worked hours receive Premium Pay.

Day Before Holiday Must be Worked - Optional. If Yes, Premium Pay only awarded if employees work the day before.

Day After Holiday Must be Worked - Optional. If Yes, Premium Pay only awarded if employees work the day after.

Holiday Starts Day Before - Optional. If Yes, Premium Pay starts at specified time on day before holiday. Useful for around-the-clock operations.

Holiday Ends on Holiday - Optional. If Yes, Premium Pay ends at specified time on holiday. Later hours paid at normal rates.

Holiday Ends Day After - Optional. If Yes, Premium Pay ends at specified time on day after holiday. Useful for around-the-clock operations.

Holiday Based on Employee's Schedule - Optional. If Yes, limits Premium Pay hours to employee's scheduled hours. Provides flexible cap based on individual schedules, unlike fixed 'Max Other Activity Hours'.

Not a Holiday If Worked - Optional. If Yes, InfiniTime won't post worked hours to the Selected Other Activity Type.

Employee Required To Work - Optional. Requires minimum hours worked before awarding Premium Pay. Options explained below:

| Employee must work X Hours...                                   | Required Configuration                                                                                             |
| --------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| ...On the Holiday Date                                          | X = minimum hours required on Holiday Date for Premium Pay. Leave Employee Required To Work Unit Field blank.      |
| ...Over Y days immediately prior to the Holiday Date            | X = minimum hours required. Y = number of days before Holiday Date for which hours count toward eligibility.       |
| ...Over Y Work Weeks prior to the Work Week of the Holiday Date | X = minimum hours required. Y = number of work weeks before Holiday Date for which hours count toward eligibility. |

#### Holiday Configuration - Fixed Benefits + Premium Pay for Worked Hours

For organizations providing both Fixed Benefits and Premium Pay for Worked Hours, create two holiday date entries for each calendar date:

1. Configure a Fixed Benefits holiday date (set 'All Worked Hours are Holiday Pay' = No)
2. Configure a Premium Pay holiday date (set 'All Worked Hours are Holiday Pay' = Yes)

Refer to the sections ['Holiday Configuration - Fixed Benefits'](Product_Configuration.md#hol12_Holiday_Types_Configuration_-_Holiday_Configuration_for_Organizations_that_Differentiate_between_Scheduled_and_Unscheduled_Hours) and ['Holiday Configuration - Premium Pay for Worked Hours'](Product_Configuration.md#hol14_Holiday_Configuration_-_Premium_Pay_for_Worked_Hours) for specific configuration details.

InfiniTime automatically awards both benefit types based on the conditions set for each holiday date. Configure each with appropriate options to match your organization's needs.

### Holiday Configuration Procedure - Fixed Benefits and Premium Pay for Worked Hours with Scheduled & Unscheduled Hours

Below is a step-by-step procedure for configuring holidays with both Fixed Benefits and Premium Pay:

1. Configure Employee Policies to separate worked hours into OT1, OT2, OT3, and OT4 as needed.
2. Identify employee groups eligible for holiday benefits on different calendar dates.
3. List all calendar dates for which each employee group is eligible for benefits.
4. Create one Holiday Type for each employee group.
5. Create one Fixed Benefit Holiday Date for each calendar date with appropriate options and conditions.
6. Create one Premium Pay Holiday Date for each calendar date with appropriate options and conditions.
7. Use Quick Assign to assign employees to the appropriate Holiday Type.
