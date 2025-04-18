---
title: "Shift Differentials"
description: "Documentation on shift differentials, including configuration, policy assignment, pay methods, and mapping options within the InfiniTime app."
---

### Shifts for Differential Purposes

InfiniTime
defines a Shift Differential as a period of time during which employees
receive an additional premium. Shift Differentials include six distinct
types of related settings:

Schedule

- Required. Describes
  the period of time during which the Shift Differential Premium is paid
  by defining specific blocks of time on specific week days. (IE: 11:00
  PM to 7:00 AM, Mon through Sun).

Pay
Premium Settings - Optional.
Defines the exact pay premium, as a percentage increase above and beyond
the employee's base rate, an additional dollar amount per hour, or an
overriding hourly rate, for worked hours which qualify for Shift Differential
Premium. Pay Premium Settings are optional. Many customers choose to configure
employee wages and pay premiums within their Payroll Application only.
In this scenario, Pay Premium Settings, Employee Default Wages, and Alternate
Wages within InfiniTime
do not need to be configured. InfiniTime
will simply track the number of hours for the differential. Employee Hours
and Earnings will then be transferred to payroll using the Payroll Export
System or Manual Entry. Alternatively, customers who choose to configure
Pay Premium Settings, Employee Default Wages, and Alternate Wages within
InfiniTime can take advantage
of the Payroll Reports within the Report Library to review Gross Employee
Wages prior to running payroll. Additional details on Employee Wages,
Alternate Wages, and Job Costing Pay Premiums can be found in the [Default
Wages](../ovr_SoftwareOverview.md#so193_Wages_Section), [Alternate
Wages](../Configuration/Product_Configuration.md#cnf17_Job_Costing_-_Wages), and [Pay
Premiums Sections](../Configuration/Product_Configuration.md#pp01_Pay_Premiums_Introduction) of this document.

Policy Assignment

- Required. Shift Differentials
  must be assigned to individual policies on the Shift Differentials Tab
  of the Schedule Settings / Rules Section of the Policy Update Form. Only
  employees on a policy with one or more Shift Differentials assigned on
  the Shift Differentials Tab will be eligible to receive Shift Differential
  Hours.

Pay Method

- Required. Controls
  the method for determining which Shift Differential Schedule is applied
  to employee hours based on the time an employee worked, punched in, or
  punched out.

Mapping Options

- Optional. Used for
  Shift Differential Mapping. This topic is covered separately below. InfiniTime Administrators should familiarize
  themselves with basic Shift Differential settings before reviewing Shift
  Differential Mapping.

Payroll Export
Options Related to Shift Differential - Optional. The Payroll Export
Options ['Pay
Shift Differential Hours at Differential Pay Only'](../PayrollExport/Payroll_Export.md#pxh34_Pay_Shift_Differential_Hours_at_Differential_Pay_Only) and ['Override
Pay Codes with Shift Pay Codes'](../PayrollExport/Payroll_Export.md#pxh37_Override_Pay_Codes_with_Shift_Pay_Codes) alter the way InfiniTime
totals and exports Shift Differential Hours. Refer to the [Payroll
Export Section](../PayrollExport/Payroll_Export.md#pxh2_Introduction) of this document for more information on the use, functionality
and configuration of the InfiniTime
Payroll Export System.

The table below provides an outline of Shift Differential
Functionality and several guidelines:

| A Shift Differential...                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | A Shift Differential...                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| \* Is tracked for all Employees assigned to a given policy. If an employee assigned to the policy has a Punch Pair or working period which qualifies for the Shift Differential Schedule according to the selected Pay Method, the employee will receive Shift Differential Hours.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | \* Is not arbitrary. It is not possible to configure a shift differential to award benefits to an employee based on external factors such as working in a specific Department, Job, or Task. Pay Premiums are intended for this purpose. |
| \* Supports four different Pay Methods. Follow the links below for additional information. + [Punch In](../Policies/Policy_Overview.md#pol131_Illustrated_Break_Down_of_Differentials_-_Punch_In_Pay_Method) - For each punch pair Employees receive the Shift Differential in effect at the time they punch in. + [Punch Out](../Policies/Policy_Overview.md#pol132_Illustrated_Break_Down_of_Differentials_-_Punch_Out_Pay_Method) - For each punch pair, employees receive the Shift Differential in effect at the time they punch out. + [Majority Hours](../Policies/Policy_Overview.md#shfpay3_Majority_Hours) - For each punch pair, Shift Differential Hours are awarded for the Shift Differential with the most hours. + [Zone](../Policies/Policy_Overview.md#shfpay4_Zone) - Shift Differentials are awarded according to the exact Shift Differential Schedule. | \* May not have a Schedule that overlaps with any other Shift Differential assigned to the respective policy. A single policy should only have non-overlapping differentials.                                                            |

Accessing
the Shift Update Form

1. Login
   to the Manager Module
2. Click
   on Lookups
3. Click
   on Scheduling Setup
4. Click
   on Shifts
5. The
   Shift Table will be displayed.

![](/img/ArrowRightButton-Normal.gif)

Shift
Table

The Shift Table lists
all Shifts, including shifts configured for scheduling and differential
purposes.

![](/img/VCRFirstButton-Normal.gif)

Insert

- Opens the Shift Update Form. Used to create a new shift for either Sheduling
  or Differential Purposes.

Change

- Opens the Shift Update Form for the Selected Shift.

Delete

- Deletes the Selected Shift. If a shift configured for Shift Differential
  and assigned to a Policy is deleted, the Shift will automatically be removed
  from the Shift Differentials Tab of all policies it was assigned to.

Shift Update
Form

The Shift Update Form is broken into three tabs which include settings
for each individual shift. The Default Schedule Tab is used to create
the Schedule which describes the period of time during which the Shift
Differential Premium is paid by defining specific blocks of time on specific
week days. The Differential Pay Tab is used to define Shift Differential
Pay Premiums and specific Shift Differential Options. The General Tab
includes basic settings as outlined below.

The General Tab of the Shift Update Form includes basic settings such
as the Shift Name, Shift Differential Pay Codes, and options which permit
the Shift and its respective schedule to be used for either Scheduling
or Differential purposes. Shift Differentials should not be confused with
Shifts for Scheduling Purposes. While it is possible to use a single Shift
for both Scheduling and Differential purposes, most InfiniTime
customers choose to configure Shift Differentials independently of employee
schedules.

General Tab

![](/img/dif03.png)

Name

- Enter a Name for the Shift. This name will be displayed on Timecard
  Reports such as the Activity Summary Report to show total Shift Differential
  Hours and is also used to assign the shift to a policy.

\*What is a Shift Identifier?

- A shift identifier is similar to a Payroll Code, but instead of representing
  a single category of pay tracked by an organization, shift identifiers
  function as a modifier for other categories of pay by indicating that
  an additional dollar amount, an additional percentage of the pay categoryâs
  base rate, or an alternate hourly rate should be paid. Shift Identifiers
  are used by organizations who track Shift Differentials. Only Payroll
  Interface Formats which support Shift Differentials utilize Shift Identifiers.\*

For example, ABC Company pays regular Hours at Payroll Code 'RH' and Daily
Overtime Hours at Payroll Code 'OT'. ABC Company also tracks Night Shift
Differential, for which employees receive an additional $1.00 Per Hour
Worked. ABC Company uses Shift Identifier 'N' for all hours types (Regular,
OT1, OT2, OT3, OT4). Payroll Interfaces with support for Shift Differentials
which include the Shift Code Field will show both 'RH' and 'NS' along
with an Employee ID Number and the total number of hours for Regular Hours
on the Night Shift Differential. Similarly, Overtime Hours worked on the
Night Shift Differential will show both 'OT' and 'NS'. This clearly indicates
to the payroll system that the employee worked Regular Hours and that
the hours are also eligible for the additional $1.00 per hour premium.

Example Records: 'Paychex Preview With
Shift Code' Payroll Interface

1     Administrator, System    ADMIN
            NERH
   0.000   39.00
1     Administrator, System    ADMIN
            NEOT
   0.000    1.00
1     Administrator, System    ADMIN
              ERH    0.000
   1.00

Worked Hours:
  39 Regular Hours,
Night Differential
  1 Overtime Hour,
Night Differential
  1 Regular Hour,
No Differential

NOTE: If the Payroll Export Option
'Override Payroll Codes with Shift Pay Codes' is enabled Shift Identifiers
will be exported directly in place of the Payroll Code for the respective
hours type. This option is intended for use with Payroll Interfaces that
include the 'Activity Type' field without the 'Shift Code' field. Additional
details can be found in the Payroll Export Section of this document under
the following headings:
   [Payroll
Export Introduction](../PayrollExport/Payroll_Export.md#pxh2_Introduction)
   [Payroll
Export Configuration Overview](../PayrollExport/Payroll_Export.md#pxh39_Payroll_Export_Configuration_Overview)
   [Payroll
Export Overview & Required Configuration By Feature - Ability to Track
Shift Differentials](../PayrollExport/Payroll_Export.md#pxh63_Ability_to_Track_Shift_Differentials)

Regular
Hours Shift Identifier / Number - Enter the Regular Hours Shift
Identifier to be used to modify the existing Regular Hours Pay Code for
Regular Hours which qualify for Shift Differential Premium Pay based on
the chosen Shift Differential Schedule and Pay Method.

OT1
Shift Identifier / Number - Enter the OT1 Hours Shift Identifier
to be used to modify the existing OT1 Hours Pay Code for Regular Hours
which qualify for Shift Differential Premium Pay based on the chosen Shift
Differential Schedule and Pay Method.

OT2
Shift Identifier / Number - Enter the OT2 Hours Shift Identifier
to be used to modify the existing OT2 Hours Pay Code for Regular Hours
which qualify for Shift Differential Premium Pay based on the chosen Shift
Differential Schedule and Pay Method.

OT3
Shift Identifier / Number - Enter the OT3 Hours Shift Identifier
to be used to modify the existing OT3 Hours Pay Code for Regular Hours
which qualify for Shift Differential Premium Pay based on the chosen Shift
Differential Schedule and Pay Method.

OT4
Shift Identifier / Number - Enter the OT4 Hours Shift Identifier
to be used to modify the existing OT4 Hours Pay Code for Regular Hours
which qualify for Shift Differential Premium Pay based on the chosen Shift
Differential Schedule and Pay Method.

Used
For Scheduling - This option must be checked in order for the
respective Shift to be used for Scheduling Purposes. If this option is
unchecked, the respective shift cannot be assigned to employees on the
'Shifts' Tab of the Schedule Information Section of the Employee Update
Form.

Used
For Differential - This option must be checked in order for
the respective Shift to be used for Differential Purposes. If this option
is unchecked, the respective shift cannot be assigned to a Policy on the
Shift Differentials Tab of the Schedule Settings / Rules Section of the
Policy Update Form

Differential
Pay Tab

The Differential Pay
Tab permits InfiniTime
Administrators to define Pay Premiums for specific types of Worked Hours
which qualify for differential based on the chosen Shift Differential
Schedule and Pay Method. Pay Premiums can be set to the same value or
different values for each hours type in order to meet your organization's
requirements.

![](/img/SkeletonTaskInsertForm.png)

Shift
Differential Pay Premium Fields

The Differential Pay and Amount
Fields are present on the Regular Hours, Overtime One, Overtime Two, Overtime
Three, and Overtime Four Tabs. These options These fields should be set
independently to meet your organization's needs. Please note that all
Pay Premium Fields are optional. Many customers choose to track employee
wages and pay rates exclusively in the Payroll Application.

Differential Pay -  This
drop down box allows you to select the type of pay for the respective
Hours Type. Options include Amount, Percent, and Rate.  The

![](/img/skel03_Save.png)

Amount
: The Amount Differential Pay Option specifies that the value entered
into the differential pay amount field is a dollar value, which will be
added to the employee's base wage specified in the employee's record.

Example:

Employee Base Wage: $15.00

Differential Amount: $1.00

Total Hourly Differential Pay Rate: $16.00

![](/img/Sched013.png)

Percent:
The Percent Differential Pay Option specifies that the value entered into
the differential pay amount field is a percentage value, which will be
multiplied by the employees base wage to determine the additional amount
paid during differential time.

Example:

Employee Base Wage: $10.00

Differential Percent: 20%

Additional Differential Pay Amount: $2.00

Total Hourly Differential Pay Rate: $12.00

![](/img/dif04.png)

Rate: The
Rate Differential Pay Option specifies that the value entered into the
differential pay amount field is a dollar value, which will be considered
the total hourly pay during differential time. The Employees base wage
is ignored when a rate is specified. All employees will receive the same
pay rate when they qualify for differential time.

Example:

Employee Base Wage: $15.00

Differential Rate: $18.00

Total Hourly Differential Pay Rate: $18.00

![](/img/VCRLastButton-Normal.gif)

Before
Shift Grace Differential - Optional. This is the amount of time the
employee has before the shift starts to clock in and be considered to
be in that shift for differential purposes.

After
Shift Grace Period - Optional.
This is the amount of time the employee has after the shift has started
to clock in and still be considered in that shift for differential purposes.

Map
Shift Hours Into - Optional.
Used for Shift Differential Mapping. This topic is [covered
separately below](Scheduling.md#shf30_Shift_Differential_Mapping). InfiniTime
Administrators should familiarize themselves with basic Shift Differential
settings before reviewing Shift Differential Mapping.

Default Schedule Tab

The Default Schedule Tab includes
the Quick Schedule feature which permits InfiniTime
Administrators to define the exact blocks of time for which worked hours
will be counted toward the respective Shift Differential.

![](/img/VCRLastButton-Normal.gif)

Quick Schedule

- Opens the Quick Default Schedule Form. Used to define a new Schedule
  for the respective Shift.

Change

- Opens the Quick Default Schedule Form for the selected Schedule Record.

Delete

- Deletes the selected Schedule Record.

To Define
a Schedule for a Shift Differential:

1. Set the Schedule Cycle to the desired value. The Weekly Schedule
   Cycle permits the InfiniTime
   Administrator to create a repeating weekly schedule based on individual
   days of the week. The Custom Schedule Cycle permits the InfiniTime Administrator to create
   a repeating schedule with a customized length, in days.
2. Click on Quick Schedule.

![](/img/Train_task_Update_Form.gif)

2. Click on the Day of the week or Day Number you wish to set a Schedule
   for as appropriate based on the previously chosen Schedule Cycle..

Quick Default Schedule - Weekly Schedule
Cycle View

![](/img/Sched024.png)

Copy

- Copies Scheduled Start and To Times from a given Day of Week to specific
  Days of Week as selected by the user.

Quick Default Schedule - Custom Schedule
Cycle View

![](/img/Sched014.png)

Copy

- Copies Scheduled Start and To Times from a given Day of the Custom Schedule
  Cycle to specific Days of the Custom Schedule Cycle as selected by the
  user.

Notice that the Custom Schedule Cycle View
displays only seven days at once. The ![](/img/sched2.gif) and ![](/img/Sched026.png) VCR Buttons at the top
of the form are used to display additional days on the form as outlined
below.

![](/img/Quick-Default-Schedule.gif)

- Shifts the Day Tabs displayed on the Quick Default Schedule Form up
  one day. Used for Custom Schedule Cycles with more than 7 days.

![](/img/sched1.gif)

- Shifts the Day Tabs displayed on the Quick Default Schedule Form down
  one day. Used for Custom Schedule Cycles with more than 7 days.

9. In the Start Time field under the Regular Hours Column enter the
   time at which the Shift Differential Premium Starts for the respective
   Day.
10. In the End Time field under the Regular Hours Column enter the
    time at which the Shift Differential Premium Ends for the respective
    Day.
11. Shift Differential Schedules may not cross midnight. If a Shift
    Differential crosses midnight, such as 11:00 PM to 7:00 AM, the Differential
    Schedule must be split at midnight as shown below. Care should be
    taken to correctly show the Day of Week or Custom Cycle Day on which
    each working block applies as shown below.  For example, XYZ
    Company does not pay Differentials for Saturday Night Shifts. Notice
    how Saturday does not have a differential schedule from 11:00 PM to
    11:59 PM and Sunday does not have a Differential Schedule from 12:00
    AM to 7:00 AM.

|              | Sunday   | Monday   | Tuesday  | Wednesday | Thursday | Friday   | Saturday |
| ------------ | -------- | -------- | -------- | --------- | -------- | -------- | -------- |
| Start Time 1 | 11:00 PM | 12:00 AM | 12:00 AM | 12:00 AM  | 12:00 AM | 12:00 AM | 12:00 AM |
| End Time 1   | 11:59 PM | 07:00 AM | 07:00 AM | 07:00 AM  | 07:00 AM | 07:00 AM | 07:00 AM |
| Start Time 2 |          | 11:00 PM | 11:00 PM | 11:00 PM  | 11:00 PM | 11:00 PM |          |
| End Time 2   |          | 11:59 PM | 11:59 PM | 11:59 PM  | 11:59 PM | 11:59 PM |          |

9. The Paid Break and Unpaid Break Columns should be left blank.
   These fields are not utilized for Shift Differential Schedules.
10. The Valid From and Valid To Fields can be used to apply the Shift
    Differential schedule to a specific date range. In this way different
    schedules can be configured in advance.
11. Click OK to Save the Schedule Configuration.

### Assigning Shift Differentials to Policies within InfiniTime

Shift Differentials must be assigned to a policy before InfiniTime will track and allocate
worked hours to the Shift Differential. The Policy Pay Method Setting,
and the exact Shift Differentials assigned to a respective policy, control
which Shift Differential employees receive for working hours.

How
to Assign a Differential to a Policy

1. Create the Shift Differential using the Shift Table. Ensure 'Use
   for Differential' is checked and that a Schedule has been configured.

2. Click on Lookups - Calculations Setup - Policies.

3. The policy table will open. Select the policy you wish to assign
   Shift Differential(s) to then click on Change.

4. Click on the Schedule Settings / Rules Section.

5. Click on the Shift Differentials Tab.

6. Click Insert.

7. Type the first few characters of the Shift Differential you wish
   to assign to the policy or use the Lookup Button to select the desired
   Shift Differential, then click OK.

8. The Shift Differential will be added to the Shift Differentials Tab.
   Repeat steps 6 and 7 to add additional Shift Differentials to the policy.
   Remember - a single policy may not have overlapping shift differentials.

![](/img/dif04.png)

It is important to note that Shift Differentials
must be assigned to Policies within InfiniTime
in order for Shift Differential Hours to be tracked for employees. The
best way to explain how policies and shift differentials work together
is to provide an example. With this in mind, we will review an example
policy configuration for a company with multiple employee groups and shift
differentials which we will refer to as XYZ Medical.

**Step
1 â Identify Employee Groups with different Policy Requirements**

XYZ Medical has multiple locations. The company
as a whole has two groups of employees with different policy configurations
for Break Rules, Overtime, Scheduling Rules, and Rounding Rules as follows:

- Hourly Employees have special break
  and rounding rules.
- Salary employees are not eligible
  for overtime and are not required to punch for breaks.

**Step
2 â Identify all shift differentials paid by the company in question.**

When attempting to identify shift differentials paid by a company it
is important to understand that a single shift differential may span multiple
shifts. Shift differentials are not used for scheduling purposes. Rather
they define a window of time that sits over top of employee schedules.
Eligible employees working within the time window will receive benefits
in the form of additional pay.

As previously mentioned it is not uncommon for a single shift differential
to span multiple shifts. In the example below a $1.00 per hour premium
is paid to employees working the Evening Team A shift and the Evening
Team B shift. Employees on Team A are permitted to stay as late as 5:00
AM and are eligible for the shift premium. Remember, a shift differential
is a contiguous block of time paid at a certain rate or premium. Because
of this a single shift differential can be configured for employees on
the Evening Team A and Evening Team B Shifts.

| Shift Name     | Start Time | End Time | Start Day | End Day | Shift Premium |
| -------------- | ---------- | -------- | --------- | ------- | ------------- |
| Evening Team A | 7:00 PM    | 3:00 AM  | Monday    | Friday  | $1.00         |
| Evening Team B | 9:00 PM    | 5:00 AM  | Monday    | Friday  | $1.00         |

| Differential Name | Start Time | End Time | Start Day | End Day | Differential Premium |
| ----------------- | ---------- | -------- | --------- | ------- | -------------------- |
| Evening Teams     | 7:00 PM    | 5:00 AM  | Monday    | Friday  | $1.00                |

Shift Differentials
paid by XYZ Medical are listed below. Each differential must be configured
as a Shift with the 'Used for Differential' option enabled.

| Differential Name        | Start Time | End Time | Start Day | End Day | Differential Premium |
| ------------------------ | ---------- | -------- | --------- | ------- | -------------------- |
| Weekend Differential     | 12:00 AM   | 11:59 PM | Saturday  | Sunday  | $0.75                |
| CNA Evening Differential | 10:00 PM   | 6:00 AM  | Monday    | Friday  | $1.00                |
| RN Evening Differential  | 8:00 PM    | 8:00 AM  | Monday    | Friday  | $1.25                |

When configuring shift differentials it is important to recognize the
schedule must be split at midnight. Shift differentials are configured
under the Shift Table which can be access from Lookups â Scheduling Setup
â Shifts. Click Insert to open the Shift Update Form.

Follow the steps below to configure each differential required by the
customer:

1. Enter the Differential Name in the Name Field of the Shift Update
   Form.
2. Enter a unique number or code for the shift in the Shift Identifier
   field.
3. Enable the Used for Differential Option.
4. Click on the Differential Pay Tab and select the appropriate type
   of Differential Pay. Amount, where employees receive an additional
   amount for each hour worked during the period defined by the shift
   differential (IE:
   $0.75 extra per hour), is the most commonly used type of Differential
   Pay.
5. Enter the Premium received by
   the employees in the Differential Pay Amount field.
6. Click Quick Schedule on the Default
   Schedule Tab. Use the schedule to define the period during which employees
   will receive premium pay. If the schedule should cross midnight it
   is important to split the schedule. For example a night differential
   of $0.75 covering 8:00 PM â 4:00 AM would be setup as below:

| Start Time | 8:00 PM  |
| ---------- | -------- |
| End Time   | 11:59 PM |
| Start Time | 12:00 AM |
| End Time   | 4:00 AM  |

**Step
3 â Identify Employee Groups who are eligible for different differentials.**

XYZ Medical
has multiple groups of employees eligible for different shift differentials
as outlined below:

- Corporate
  Office Employees are not eligible for shift differentials.
- All
  Hourly and Salary Employees are eligible for Weekend Differentials.
- All
  Certified Nurse Assistants are eligible for the CNA Evening and Weekend
  Differentials.
- All
  Registered Nurses are eligible for the RN Evening and Weekend Differentials.

**Step
4 â One Policy will be required for each group of employees who require
different shift differentials or policy settings.**

The following
policies are required to meet the needs of XYZ Medical:

| Policy Name                | Unique Policy Settings | Eligible Shift Differentials      |
| -------------------------- | ---------------------- | --------------------------------- |
| Corporate Hourly           | Break & Rounding Rules | None                              |
| Corporate Salary           | Overtime & Break Rules | None                              |
| Hourly Employees           | Break & Rounding Rules | Weekend Differential              |
| Salary Employees           | Overtime & Break Rules | Weekend Differential              |
| Certified Nurse Assistants | None                   | Weekend & CNA Night Differentials |
| Registered Nurses          | None                   | Weekend & RN Night Differentials  |

In
the above example employees classified as Certified Nurse Assistants and
Registered Nurses have identical policy requirements for Break Rules,
Overtime Rules, Scheduling etc. within their specific class of employees.
If even a single employee within the CNA or RN class had unique policy
requirements an additional policy would be required for individuals requiring
different policy settings.

Differentials
Listed in the 'Eligible Shift Differentials' Column of the table above
must be assigned to the appropriate policy under Schedule Settings / Rules
â Shift Differentials.

Now
that we have an understanding of how policies and shift differentials
interact use the steps below to help the customer identify their employee
groups, shift differentials, and required policies.

1.)    Identify employee groups requiring different
policy settings for Break Rules, Overtime Calculations, Scheduling Rules,
Pay Cycle Configuration, or Rounding Rules.

2.)    Identify all shift differentials paid by
the company in question.

3.)    Identify employee groups who are eligible
for different differentials.

4.)    One policy will be required for each group
of employees with different differentials and policy settings.

Shift
Differential Pay Methods

If a
Shift Differential is assigned to a policy, a Shift Differential Pay Method
must be selected. Remember, within InfiniTime
shift differentials are defined as a period during which employees receive
an additional premium. It is not uncommon for employees to be eligible
for multiple shift differentials. The Shift Differential pay method determine
which differential an employee will receive based upon when they are working
or when they punched in. The Shift Differential Pay Method is located
on the General Tab of the Schedule Settings / Rules section of the Policy
Update Form.

![](/img/winschtimeentry_pb.gif)

NOTE: The
Shift Differential Pay Method option is disabled and cannot be altered
until one or more shift differentials have been assigned to the policy
on the Shift Differentials tab.

Shift Differential Pay Method â
The Shift Differential Pay Method determines exactly how employees are
awarded shift differential premiums, based on the time they punched in
(Punch In), punched out (Punch Out), the time they are working (Zone),
or where the majority of their working hours fall for a given date (Majority
Hours). A Shift Differential Pay Method must be selected for employees
to receive shift premiums. The best method for understanding exactly how
each Shift Differential Pay Method functions is to review an example scenario
for each available option.

Related
Settings:

ABC
Medical employs Registered Nurses (RNs) who receive differential pay for
working during evening and early morning hours as outlined below.

| Differential Name    | Rate  | Start Time | End Time |
| -------------------- | ----- | ---------- | -------- |
| Evening Differential | $1.00 | 8:00 PM    | 12:00 AM |
| Morning Differential | $1.25 | 12:00 AM   | 4:00 AM  |

**Punch In
â** When the Punch In pay method
is chosen employees are paid the premium in effect at the time they punch
in. For clarity multiple examples are shown below.

| Scenario Description                                                                                                                                                                                                                                                                   | Illustrated Break Down of Differentials - Punch In Pay Method |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| An RN arrives at the hospital early and is asked to lend a hand prior to their shift. They clock in at 7PM and work until 4AM. Because the RN clocked in at 7PM, which does not fall within a period eligible for differential pay, the RN will not receive a premium for their hours. |                                                               |
| An RN is called in to work from 10PM to 4AM. The employee punches in at 10:00 PM, which is during the period defined by the Evening Differential. All six hours (10PM to 4AM) will be paid at the Evening Differential rate.                                                           |                                                               |

**Punch Out
â** When the Punch Out pay method
is chosen employees are paid the premium in effect at the time they punch
out. For clarity multiple examples are shown below.

| Scenario Description                                                                                                                                                                                                                                                                  | Illustrated Break Down of Differentials - Punch Out Pay Method |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| The typical RN Day shift is 11 AM to 7PM. Mary Joe is asked to stay for an additional two hours and works from 11AM to 9PM. Because Mary clocked out at 9PM, which falls within the Evening Differential, she will receive the Evening Differential Premium for all ten hours worked. |                                                                |
| An RN is called in to work from 8PM to 4AM. The employee punches out at 4:15 AM. The employee will not receive a premium for the worked hours because 4:15 AM does not fall within a period defined by a differential.                                                                |                                                                |

**Majority
Hours â** The Majority Hours
pay method identifies the differential on which employees worked the greatest
portion of their hours. The premium associated with that differential
is then used for all differential hours for the day as illustrated below.
If an employee should work an equal amount of hours across multiple differentials
they will be paid the premium associated with the first differential.

| Scenario Description                                                                                                                                                                                                     | Illustrated Break Down of Differentials - Majority Hours Pay Method |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------- |
| An RN is called in to work from 10:00 PM to 4:00 AM. The majority of the worked hours fall within the Morning Differential. As such the employee receives the Morning Differential premium ($1.25) for all hours worked. |                                                                     |

**Zone â**
Zone is the most commonly used pay method
for shift differentials. Employees will be paid a premium according to
the differential they are working on. In this scenario if an RN were to
be called in to work from 10:00 PM to 4:00 AM they would receive two hours
of Evening Differential Pay and Four Hours of Morning Differential Pay
as follows:

| Scenario Description                                                                                                                                                                                                                                                                                                                             | Illustrated Break Down of Differentials - Zone Pay Method |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------- |
| An RN is called in to work from 10:00 PM to 4:00 AM. Hours from 10:00 PM to 12:00 AM are associated with the Evening Differential. Hours from 12:00 AM to 4:00 AM are associated with the Morning Differential. The employee is paid as follows:            2 Hours Evening Differential Premium            4 Hours Morning Differential Premium |                                                           |

Shift
Differential Mapping

All prior Shift Differential Configuration examples have a common element.
The Time Period for which worked hours are applied to shift differential,
and the time period during which employees may Punch In, Punch Out, or
Work to qualify for shift differential based on the selected Pay Method
are the same. Shift Differential Mapping permits the time period for which
worked hours are applied to shift differential to be separated from the
time period during which employees must initially Punch In, Punch Out,
or Work to qualify for Shift Differential Benefits. Shift Differential
Mapping is configured using the 'Map Shift Hours Into' option on the Differential
Pay Tab of the Shift Update Form.

![](/img/SkeletonTaskInsertForm.png)

Map Shift Hours To â Permits
Shift Differential Mapping which allows versatile shift differential payment
rules. Shift Differential mapping makes it possible to trigger Shift Differential
Hours based on the Pay Method selected on an employee's policy and the
Schedule Defined on a 'Primary Shift Differential' but pay shift differential
hours according to the Schedule defined on a Secondary Differential. Shift
mapping is subject to the following requirements and conditions:

- Two Shifts must be configured
  for differential. Use for differential must be checked for each shift.

1 Primary Differential Shift

1 Secondary Differential Shift

- The Primary Shift Differential must
  be assigned to a Policy. The secondary Shift Differential should
  not be assigned to the policy.
- The Primary differential shift includes
  the map to setting, which points to the Secondary Differential Shift.
- The employee must Punch In, Punch
  Out, or Work During the Time Period defined on the Schedule of the
  Primary Shift Differential in order to qualify for differential payment.
  Differential hours will be totaled and paid according to Schedule,
  and Differential Pay Settings defined on the Secondary Differential
  Shift in addition to the Policy's Pay Method.
- Differential
  Pay and Differential Amount Settings can be left blank on the Primary
  Differential Shift.

Shift Differential
Mapping Examples:

For
clarity, an example of Shift Differential Mapping is provided below for
the Clock In, Clock Out, and Zone Pay Methods. The Majority Hours pay
method is not recommended for use with Shift Differential Mapping. As
detailed above, Shift Differential Mapping makes it possible to trigger
Shift Differential Hours based on the Pay Method selected on an employee's
policy and the Schedule Defined on a 'Primary Shift Differential' but
pay shift differential hours according to the Schedule defined on a Secondary
Differential.

**Zone â**
Zone is the most commonly used pay method
for shift differentials. In the scenario below, ABC Medical employs Registered
Nurses (RNs) who receive differential pay during between the hours of
8:00 PM and 4:00 AM Monday through Sunday if\* they have working hours
between the hours of 10:00 PM and 2:00 PM.

Related Settings:

| Primary RN Evening Differential - Determines Time Period during which employees must have worked hours to receive Shift Differential | Sunday   | Monday   | Tuesday  | Wednesday | Thursday | Friday   | Saturday |
| ------------------------------------------------------------------------------------------------------------------------------------ | -------- | -------- | -------- | --------- | -------- | -------- | -------- |
| Start Time 1                                                                                                                         | 12:00 AM | 12:00 AM | 12:00 AM | 12:00 AM  | 12:00 AM | 12:00 AM | 12:00 AM |
| End Time 1                                                                                                                           | 02:00 AM | 02:00 AM | 02:00 AM | 02:00 AM  | 02:00 AM | 02:00 AM | 02:00 AM |
| Start Time 2                                                                                                                         | 10:00 PM | 10:00 PM | 10:00 PM | 10:00 PM  | 10:00 PM | 10:00 PM | 10:00 PM |
| End Time 2                                                                                                                           | 11:59 PM | 11:59 PM | 11:59 PM | 11:59 PM  | 11:59 PM | 11:59 PM | 11:59 PM |

| Secondary RN Evening Differential - Determines Time Period during which worked hours are applied toward Shift Differential | Sunday   | Monday   | Tuesday  | Wednesday | Thursday | Friday   | Saturday |
| -------------------------------------------------------------------------------------------------------------------------- | -------- | -------- | -------- | --------- | -------- | -------- | -------- |
| Start Time 1                                                                                                               | 8:00 PM  | 8:00 PM  | 8:00 PM  | 8:00 PM   | 8:00 PM  | 8:00 PM  | 8:00 PM  |
| End Time 1                                                                                                                 | 11:59 PM | 11:59 PM | 11:59 PM | 11:59 PM  | 11:59 PM | 11:59 PM | 11:59 PM |
| Start Time 2                                                                                                               | 12:00 AM | 12:00 AM | 12:00 AM | 12:00 AM  | 12:00 AM | 12:00 AM | 12:00 AM |
| End Time 2                                                                                                                 | 4:00 AM  | 4:00 AM  | 4:00 AM  | 4:00 AM   | 4:00 AM  | 4:00 AM  | 4:00 AM  |

| Scenario Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Illustrated Break Down of Differentials - Zone Pay Method |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------- |
| An RN who usually works the day shift, 8:00 AM to 4:00 PM, is asked to remain on duty due to an influx of patients. The RN stays until 9:30 PM. Even though the Secondary Differential Pays RN Evening Differential benefits from 8:00 PM to 6:00 AM, benefits are only triggered with the Zone Pay Method if an employee works between 10:00 PM and 2:00 AM. In this scenario, the employee would be paid as follows: 8 Regular Hours - No Differential 5.5 OT1 Hours - No Differential |                                                           |
| An RN who usually works the night shift, 8:00 PM to 4:00 AM, is asked to report for duty an hour early. The RN works from 7:00 PM to 4:00 AM. Since the employee has working hours during the 10:00 PM to 2:00 AM period, the employee will receive differential for all hours which fall within 8:00 PM to 4:00 AM as follows: 1 Regular Hours - No Differential 7 Regular Hours - Evening Differential 1 OT1 Hour - Evening Differential                                               |                                                           |

**Punch In
â** In the scenario below, ABC
Medical employs Registered Nurses (RNs) who receive differential pay during
between the hours of 8:00 PM and 4:00 AM Monday through Sunday if\* they
punch in between the hours of 7:00 PM and 9:00 PM.

Related
Settings:

| Primary RN Evening Differential - Determines Time Period during which employees must have worked hours to receive Shift Differential | Sunday  | Monday  | Tuesday | Wednesday | Thursday | Friday  | Saturday |
| ------------------------------------------------------------------------------------------------------------------------------------ | ------- | ------- | ------- | --------- | -------- | ------- | -------- |
| Start Time 1                                                                                                                         | 7:00 PM | 7:00 PM | 7:00 PM | 7:00 PM   | 7:00 PM  | 7:00 PM | 7:00 PM  |
| End Time 1                                                                                                                           | 9:00 PM | 9:00 PM | 9:00 PM | 9:00 PM   | 9:00 PM  | 9:00 PM | 9:00 PM  |

| Secondary RN Evening Differential - Determines Time Period during which worked hours are applied toward Shift Differential | Sunday   | Monday   | Tuesday  | Wednesday | Thursday | Friday   | Saturday |
| -------------------------------------------------------------------------------------------------------------------------- | -------- | -------- | -------- | --------- | -------- | -------- | -------- |
| Start Time 1                                                                                                               | 8:00 PM  | 8:00 PM  | 8:00 PM  | 8:00 PM   | 8:00 PM  | 8:00 PM  | 8:00 PM  |
| End Time 1                                                                                                                 | 11:59 PM | 11:59 PM | 11:59 PM | 11:59 PM  | 11:59 PM | 11:59 PM | 11:59 PM |
| Start Time 2                                                                                                               | 12:00 AM | 12:00 AM | 12:00 AM | 12:00 AM  | 12:00 AM | 12:00 AM | 12:00 AM |
| End Time 2                                                                                                                 | 4:00 AM  | 4:00 AM  | 4:00 AM  | 4:00 AM   | 4:00 AM  | 4:00 AM  | 4:00 AM  |

| Scenario Description | Illustrated Break Down of Differentials - Punch In Pay Method |
| An RN is called in to work the last half of the Evening Shift and the first half of the Morning Shift. They clock in at 12:00 AM and work until 8:00 AM. Because the RN clocked in at 12:00 PM, which does not fall within the Primary Differential a period eligible for differential pay, the RN will not receive a premium for their hours. | |
| An RN arrives at the hospital early and is asked to lend a hand before the start of their shift. They clock in at 7:30 PM and work until 4:00 AM. Because the RN clocked in at 7:30 PM, which falls within the Primary RN Evening Differential of 7:00 PM to 9:00 PM, the employee will receive differential for all hours worked which fall within 8:00 PM to 4:00 AM. | |

**Punch Out
â** In the scenario below, ABC
Medical employs Registered Nurses (RNs) who receive differential pay during
between the hours of 8:00 PM and 4:00 AM Monday through Sunday if\* they
punch out between the hours of 3:30 AM and 5:00 AM.

Related
Settings:

| Primary RN Evening Differential - Determines Time Period during which employees must have worked hours to receive Shift Differential | Sunday  | Monday  | Tuesday | Wednesday | Thursday | Friday  | Saturday |
| ------------------------------------------------------------------------------------------------------------------------------------ | ------- | ------- | ------- | --------- | -------- | ------- | -------- |
| Start Time 1                                                                                                                         | 3:30 AM | 3:30 AM | 3:30 AM | 3:30 AM   | 3:30 AM  | 3:30 AM | 3:30 AM  |
| End Time 1                                                                                                                           | 5:00 AM | 5:00 AM | 5:00 AM | 5:00 AM   | 5:00 AM  | 5:00 AM | 5:00 AM  |

| Secondary RN Evening Differential - Determines Time Period during which worked hours are applied toward Shift Differential | Sunday   | Monday   | Tuesday  | Wednesday | Thursday | Friday   | Saturday |
| -------------------------------------------------------------------------------------------------------------------------- | -------- | -------- | -------- | --------- | -------- | -------- | -------- |
| Start Time 1                                                                                                               | 8:00 PM  | 8:00 PM  | 8:00 PM  | 8:00 PM   | 8:00 PM  | 8:00 PM  | 8:00 PM  |
| End Time 1                                                                                                                 | 11:59 PM | 11:59 PM | 11:59 PM | 11:59 PM  | 11:59 PM | 11:59 PM | 11:59 PM |
| Start Time 2                                                                                                               | 12:00 AM | 12:00 AM | 12:00 AM | 12:00 AM  | 12:00 AM | 12:00 AM | 12:00 AM |
| End Time 2                                                                                                                 | 4:00 AM  | 4:00 AM  | 4:00 AM  | 4:00 AM   | 4:00 AM  | 4:00 AM  | 4:00 AM  |

| Scenario Description | Illustrated Break Down of Differentials - Punch Out Pay Method |
| An RN works their normal 8:00 PM to 4:00 AM shift, and is asked to stay late. They clock out at 5:30 AM. Because the RN clocked out at 5:30 AM, which does not fall within the Primary RN Evening Differential of 3:30 AM to 5:00 AM, the employee will not receive differential hours. The employee is paid as follows:              8 Regular Hours - No Differential            1.5 OT1 Hours - No Differential | |
| An RN works their normal 8:00 PM to 4:00 AM shift, running over by 30 minutes. They clock out at 4:30 AM. Because the RN clocked out at 4:30 AM, which falls withiin the Primary RN Evening Differential of 3:30 AM to 5:00 AM, the employee will receive differential for all hours worked which fall within the Secondary Differential Schedule (IE: 8:00 PM to 4:00 AM). The employee is paid as follows:              8 Regular Hours - Evening Differential            0.5 OT1 Hours - Evening Differential | |
