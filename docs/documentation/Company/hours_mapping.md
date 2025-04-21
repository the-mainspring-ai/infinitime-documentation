### Hours Mapping

Hours mapping permits either scheduled or unscheduled hours for specific
worked hours types (IE: Regular, OT1, OT2, OT3, OT4) to be separated into
a different column on employee timecards. This functionality provides
the InfiniTime Administrator
with complete control over:

- Which
  Hours Type Scheduled and / or Unscheduled Hours are totaled under
  on Employee Timecards and Timecard Reports (IE: Regular, OT1, OT2,
  OT3, OT4)
- The pay
  rate employee hours are paid at
- The payroll
  code exported for employee hours

Hours Mapping can be enabled for a variety of conditions, as outlined
in the table below. This flexibility, along with existing Job Costing
Functionality, allows Hours Mapping Rules to be applied based on Job Costing
Categories selected by employees at the time of punch or specifically
entered by supervisors during the review and editing of employee timecards.
In this way, hours mapping can be used to meet the needs of a variety
of special payment scenarios. Hours Mapping is an optional feature and
is intended for use by organizations that differentiate between Scheduled
and Unscheduled Hours and / or wish to track specific pay codes for Unscheduled
Hours worked on Holidays or Specific Other Activity Types. Approximately
20 to 40 out of 100 companies require Hours Mapping to meet their Time
and Attendance needs. InfiniTime Administrators attempting
to configure Hours Mapping should have an understanding of Job Costing,
Unscheduled Hours Mapping settings within the Policy, Other Activity Types
and Other Activity Options, as well as a general understanding of the
Payroll Export's use of payroll codes. Related topics are provided below
for reference.

Related Topics:

[Job
Costing](Product_Configuration.md#cnf01_Job_Costing_Introduction)

[Schedule
Settings and Rules: Unscheduled Hours Mapping](../Policies/Policy_Overview.md#pol114_Schedule_Settings___Rules)

[Other
Activity Types: Introduction](Product_Configuration.md#ota01_Other_Activity_Types)

[Other
Activity Types: Options](Product_Configuration.md#ota03_Other_Activity_Update_Form)

[Payroll
Export - Payroll Codes](../PayrollExport/Payroll_Export.md#pxh47_What_is_a_Payroll_Code_)

When
configuring Hours Mapping there are three main tasks that must be performed.
Each task is listed and described in detail below.

1. Identify the Type of Hours Mapping that
   applies to your scenario.

2. Identify the Hour Type(s) to be mapped.

3. Understand how the Hours Mapping Hierarchy will affect your pay premium(s)

4. Identify the Type of Hours Mapping that applies to your scenario.

InfiniTime
supports five types of Hours Mapping, each of which are configured in
a separate area of the InfiniTime
Application. Hours Mapping Rules are applied for employees assigned to
a specific policy and / or when employees have hours on a specific Other
Activity Type, Department, Job, or Task that has been configured for Hours
Mapping. While it is possible to configure multiple Hours Mapping Types
for a single InfiniTime
Installation, this is only recommended in specific situations in order
to reduce the impact of the Hours Mapping Hierarchy. InfiniTime
Administrators should chose and configure the specific Hours Mapping Type(s)
which best meets the needs of their organization as outlined below.

| Premium Type                     | Location within InfiniTime                                                                                                                                                                                                                                                                                                                                                                          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| -------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Policy Unscheduled Hours Mapping | 1. Click on Lookups, Calculations Setup, Policies. 2. Click on the Schedule Settings / Rules Section. 3. Unscheduled Hours Mapping Settings are displayed on the General Tab.                                                                                                                                                                                                                       | Unscheduled Hours Mapping Settings are applied to all employees assigned to a policy. Policy Unscheduled Hours Mapping settings are configured separately for each policy within InfiniTime.   Policy Unscheduled Hours Mapping Settings are commonly used to separate all Unscheduled Hours into a single Overtime Bucket such as OT4.                                                                                                                                                                                                                                                                    |
| Holiday Hours Mapping            | 1. Click on Lookups - Calculations Setup - Holiday Schedule Types. 2. Click Change while highlighting an existing Holiday Type or click Insert. 3. Click on the Dates Tab. 4. Click Change while highlighting an existing Holiday Date or click Insert. 5. Click on the Hours Mapping Tab. The Hours Mapping Tab is only available for Holiday Dates with 'All Worked Hours are Holiday Pay' = Yes. | Holiday Hours Mapping Settings are applied to all employees assigned to the respective Holiday Type with Worked Hours on the respective Holiday Date. Holiday Hours Mapping Settings are commonly used to separate all Unscheduled Hours worked on a Holiday into a separate bucket such as OT4.                                                                                                                                                                                                                                                                                                           |
| Other Activity Hours Mapping     | 1. Click on Lookups, Calculations Setup, Other Activity Types. 2. Click Change while highlighting an existing Other Activity Type or click Insert. 3. Click on the Hours Mapping Tab. The Hours Mapping Tab is only displayed for Other Activity Types with 'Count as Regular Hours' or 'Only Count as Regular Hours if Scheduled' checked.                                                         | Other Activity Hours Mapping Settings are applied to Other Hours for other activity types with Hours Mapping Configured. Other Activity Hours Mapping Settings are configured separately for each Other Activity Type. Other Activity Hours Mapping Settings are commonly used to pay a different rate for hours on a day where the employee was not scheduled to work for other Activity Types set to 'Count as Regular Hours.' The most prevalent scenario that requires Other Activity Hours Mapping is Unscheduled Hours worked on a Holiday Date where All Worked Hours are Holiday Pay is set to No. |
| Department Hours Mapping         | 1. Click on the Department Button. 2. Click Change while highlighting an existing department or click Insert. 3. Click on the Hours Mapping Tab.                                                                                                                                                                                                                                                    | Department Hours Mapping Settings are applied to Worked Hours in a given department and are configured separately for each Department.   Department Hours Mapping Settings are commonly used to separate hours worked for a given department into a specific Overtime Bucket to be paid at a premium rate per hour.                                                                                                                                                                                                                                                                                        |
| Job Hours Mapping                | 1. Click on Lookups, Employee Setup, Job Costing Lookups, Activity Jobs. 2. Click Change while highlighting an existing job or click Insert. 3. Click on the Hours Mapping Tab.                                                                                                                                                                                                                     | Job Hours Mapping Settings are applied to Worked Hours in a given Job and are configured separately for each Job.   Job Hours Mapping Settings are commonly used to separate hours worked for a given job into a specific Overtime Bucket to be paid at a premium rate per hour.                                                                                                                                                                                                                                                                                                                           |
| Task Hours Mapping               | 1. Click on Lookups, Employee Setup, Job Costing Lookups, Activity Tasks. 2. Click Change while highlighting an existing task or click Insert. 3. Click on the Hours Mapping Tab.                                                                                                                                                                                                                   | Task Hours Mapping Settings are applied to Worked Hours in a given Task and are configured separately for each Task.   Task Hours Mapping Settings are commonly used to separate hours worked for a given task into a specific Overtime Bucket to be paid at a premium rate per hour.                                                                                                                                                                                                                                                                                                                      |

2. Identify
   the Hour Type(s) to be mapped.

After
Identifying the Hours Mapping Type, the type of hours to be configured
for Hours Mapping must be identified. Hours Mapping is configured separately
for each type of worked hours. The table below provides an example of
each worked hours type alongside specific policy settings and employee
schedules.

Related
Settings:

The
following policy settings for XYZ Company are utilized for the examples
below.

- OT1
  = Daily > 8 Hours.
- OT2
  = Daily > 10 Hours.
- OT3
  = Day of Week Overtime: Regular, OT1, and OT2 hours worked on Sunday.
- OT4
  = Holiday Hours Mapping: Regular, OT1, and OT2 Hours worked on a Holiday
  Date.

| Working Hours Type        | Example                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Scheduled Regular Hours   | Total Hours: 8 Scheduled Regular Hours, 1 Hour Unpaid Break   Scheduled Regular Hours are Working Hours which do not qualify for any Overtime Bucket that fall within the bounds of an employee's schedule. In this case, based on the policy settings above, hours less than 8 in a day are considered Regular Hours. As shown above, the employee is scheduled from 8:00 AM to 5:00 PM. All hours worked between 8:00 AM and 5:00 PM will be considered Scheduled Hours.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Scheduled OT1 Hours       | Total Hours: 8 Scheduled Regular Hours, 1 Hour Unpaid Break, 1 Hour Scheduled OT1   Scheduled OT1 Hours are OT1 Hours that fall within the bounds of an employee's schedule. In this case, based on the policy settings above, hours between 8 and 10 in a day are considered OT1 Hours. Hours greater than 10 in a day are OT2 Hours and as such are not OT1 Hours. As shown above, the employee is scheduled from 8:00 AM to 6:00 PM. All hours worked between 5:00 PM and 6:00 PM are considered Scheduled Hours.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Scheduled OT2 Hours       | Total Hours: 8 Scheduled Regular Hours, 1 Hour Unpaid Break, 2 Scheduled OT1 Hours, 1 Hour Scheduled OT2   Scheduled OT2 Hours are OT2 Hours that fall within the bounds of an employee's schedule. In this case, based on the policy settings above, hours greater than 10 in a day are considered OT2 Hours. As shown above, the employee is scheduled from 6:00 AM to 6:00 PM. All hours worked between 5:00 PM and 6:00 PM are considered Scheduled Hours.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Scheduled OT3 Hours       | Total Hours: 8 Scheduled OT3 Hours   Scheduled OT3 Hours are OT3 Hours that fall within the bounds of an employee's schedule. In this case, based on the policy settings above, all hours worked on a Sunday are OT3 Hours. As shown above, the employee is scheduled from 6:00 AM to 6:00 PM. All hours worked between 5:00 PM and 6:00 PM are considered Scheduled Hours.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Scheduled OT4 Hours       | Total Hours: 8 Scheduled OT4 Hours   Scheduled OT4 Hours are OT4 Hours that fall within the bounds of an employee's schedule. In this case, based on the policy settings above, all hours worked on a Holiday Date are OT4 Hours. As shown above, the employee is scheduled from 6:00 AM to 3:00 PM on July 4th 2013. All hours worked between 6:00 AM and 3:00 PM are considered Scheduled Hours.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Unscheduled Regular Hours | Unscheduled Regular Hours w/ 'Only Hours Worked in Excess of Scheduled Hours are Unscheduled' disabled   Total Hours: 2 Unscheduled Regular Hours, 6 Scheduled Regular Hours, 1 Hour Unpaid Break   Unscheduled Regular Hours are Working Hours which do not qualify for any Overtime Bucket that fall outside the bounds of an employee's schedule. In this case, based on the policy settings above, hours less than 8 in a day are considered Regular Hours. As shown above, the employee is scheduled from 8:00 AM to 5:00 PM. All regular hours worked outside of 8:00 AM and 5:00 PM will be considered Unscheduled Regular Hours.\* NOTE: The 'Only Hours Worked in Excess of Scheduled Hours are Unscheduled' option on the Schedule Settings / Rules section of the policy is intended for organizations who require employees to work at least the scheduled number of hours on a given date prior to receiving Unscheduled Hours. As shown below, if 'Only Hours Worked In Excess of Scheduled Hours are Unscheduled' employees will only receive Unscheduled Hours for hours beyond the duration of their schedule. Unscheduled Regular Hours w/ 'Only Hours Worked in Excess of Scheduled Hours are Unscheduled' enabled Example 1: Worked Hours Do Not Exceed Scheduled Hours Total Hours: 8 Scheduled Regular Hours, 1 Hour Unpaid Break When 'Only Hours Worked in Excess of Scheduled Hours are Unscheduled' is enabled, worked hours must exceed scheduled hours in order for employee's to receive Unscheduled Hours. As shown above, the employee is scheduled from 8:00 AM to 5:00 PM for a total of 8 Working Hours. In this scenario, since Regular Hours are Worked Hours Under 8 in a Day, it is not possible for an employee to receive Unscheduled Regular Hours. Example 2: Worked Hours Exceed Scheduled Hours Total Hours: 6 Scheduled Regular Hours, 1 Hour Unpaid Break, 2 Unscheduled Regular Hours When 'Only Hours Worked in Excess of Scheduled Hours are Unscheduled' is enabled, worked hours must exceed scheduled hours in order for employee's to receive Unscheduled Hours. As shown above, the employee is scheduled from 8:00 AM to 3:00 PM for a total of 6 Working Hours. In this scenario, since worked hours exceed scheduled hours, the employee receives two hours Unscheduled Regular Hours. |
| Unscheduled OT1 Hours     | Total Hours: 8 Scheduled Regular Hours, 1 Hour Unpaid Break, 1 Hour Unscheduled OT1   Unscheduled OT1 Hours are OT1 Hours that fall outside the bounds of an employee's schedule. In this case, based on the policy settings above, hours between 8 and 10 in a day are considered OT1 Hours. Hours greater than 10 in a day are OT2 Hours and as such are not OT1 Hours. As shown above, the employee is scheduled from 8:00 AM to 5:00 PM. All hours worked between 5:00 PM and 7:00 PM are considered Unscheduled OT1 Hours.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Unscheduled OT2 Hours     | Total Hours: 8 Scheduled Regular Hours, 1 Hour Unpaid Break, 2 Hour Unscheduled OT1, 1 Unscheduled OT2   Unscheduled OT2 Hours are OT2 Hours that fall outside the bounds of an employee's schedule. In this case, based on the policy settings above, hours over 10 in a day are considered OT2 Hours. As shown above, the employee is scheduled from 6:00 AM to 3:00 PM. All hours worked beyond 5:00 PM are considered Unscheduled OT2 Hours.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Unscheduled OT3 Hours     | Total Hours: 8 Scheduled OT3 Hours, 1 Hour Unpaid Break, 3 Hours Unscheduled OT3   Unscheduled OT3 Hours are OT3 Hours that fall outside the bounds of an employee's schedule. In this case, based on the policy settings above, hours worked on a Sunday are considered OT3 Hours. As shown above, the employee is scheduled from 6:00 AM to 3:00 PM on Sunday 8/11/13. All hours worked beyond 3:00 PM are considered Unscheduled OT3 Hours.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Unscheduled OT4 Hours     | Total Hours: 8 Scheduled OT4 Hours, 1 Hour Unpaid Break, 3 Hours Unscheduled OT4    Unscheduled OT4 Hours are OT4 Hours that fall outside the bounds of an employee's schedule. In this case, based on the policy settings above, hours worked on a Holiday are considered OT4 Hours. As shown above, the employee is scheduled from 6:00 AM to 3:00 PM. All hours worked beyond 3:00 PM are considered Unscheduled OT4 Hours.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

### Example Hours Mapping Configuration:

As
an example for each Hours Mapping Type, let us assume that XYZ Company
pays the Hours Types below at the same rate as Unscheduled OT3. In other
words - Unscheduled OT1 and Unscheduled OT2 Hours can be grouped together
with Unscheduled OT3 Hours and paid together.

The
following Hours Mapping settings are required to map Unscheduled OT1 and
Unscheduled OT2 Hours into OT3:

Scheduled
Hours Mapping Settings:

![](/img/sched7.gif)

Unscheduled
Hours Mapping Settings:

![](/img/clip_image024.jpg)

The
table below describes when Unscheduled OT1 and Unscheduled OT2 Hours would
be mapped to OT3 if the above settings were configured for each Hours
Mapping Type individually.

| Hours Mapping Type               | Unscheduled OT1 and Unscheduled OT2 Hours would be mapped to OT3...                                                                                                                                                                                            |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Policy Unscheduled Hours Mapping | Unscheduled OT1 and Unscheduled OT2 Hours would be mapped directly to OT3 for all employees assigned to the respective policy automatically. No additional actions, such as working on a specific Department / Job / Task or Other Activity Type are required. |
| Holiday Hours Mapping            | All Unscheduled OT1 and Unscheduled OT2 Hours _worked on the Holiday Date_ would be mapped to OT3.                                                                                                                                                             |
| Other Activity Hours Mapping     | All Unscheduled OT1 and Unscheduled OT2 Hours _for the respective Other Activity Type_ would be mapped to OT3.                                                                                                                                                 |
| Department Hours Mapping         | All Unscheduled OT1 and Unscheduled OT2 Hours _assigned to the respective Department_ would be mapped to OT3.                                                                                                                                                  |
| Job Hours Mapping                | All Unscheduled OT1 and Unscheduled OT2 Hours _assigned to the respective Job_ would be mapped to OT3.                                                                                                                                                         |
| Task Hours Mapping               | All Unscheduled OT1 and Unscheduled OT2 Hours _assigned to the respective Task_ would be mapped to OT3.                                                                                                                                                        |

3.  Understand how the Hours Mapping Hierarchy will affects Employee Hours

In some scenarios employees
may be eligible for multiple types of hours mapping by meeting the conditions
of multiple hours mapping settings. If your company will only be tracking
a single type of hours mapping this section can be ignored. When using
multiple hours mapping types, the following key points should be kept
in mind:

- Hours Mapping
  Settings for each Hours Mapping Type are applied sequentially in the
  order below.
- Worked Hours mapped to a different hours type can be mapped
  again by a higher priority Hours Mapping Type.

Sequential Order:

1     Policy Unscheduled Hours Mapping (Lowest Priority)

2     Holiday Hours Mapping

3     Other Activity Hours Mapping

4     Department Hours
Mapping

5     Job Hours Mapping

6     Task Hours Mapping
(Highest Priority)

For example, ABC Manufacturing Company
pays Unscheduled Hours on Holiday Dates at a different rate than Unscheduled
Hours on regular working days for Production Employees. The hours mapping
settings shown below will map Unscheduled Regular and OT1 Hours to OT2
for all employees assigned to the Production Employees policy. Additionally,
if an employees on the Production Employee's policy work Unscheduled Regular
or OT1 Hours on a Holiday Date the Unscheduled OT2 Hours will be posted
to OT4.

| ABC Manufacturing Company - Hours Mapping Settings |                                                                                                         |
| -------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| Hours Mapping Type                                 | Hours Mapping Settings                                                                                  |
| Policy Unscheduled Hours Mapping                   | _ Scheduled Hours: + N/A _ Unscheduled Hours: + Unscheduled Regular HoursOT2 + Unscheduled OT1 HoursOT2 |
| Holiday Hours Mapping                              | _ Scheduled Hours: + N/A _ Unscheduled Hours: + Unscheduled OT2 HoursOT4                                |

ABC Manufacturing - Policy
Unscheduled Hours Mapping Example:

![](/img/sched10.gif)

July 6th 2013 is a normal
scheduled working day for John Smith. Notice how John worked a total of
10 hours with 2 Unscheduled OT1 hours posting to OT2 due to Policy Unscheduled
Hours Mapping Settings.

ABC Manufacturing - Holiday
Hours Mapping Example:

![](/img/EmployeeProfile_026.png)

July
4th 2013 is a scheduled working day for John Smith that also happens to
be a Holiday Date. Notice how John worked a total of 10 hours with 2 Unscheduled
OT1 hours. However - instead of posting to OT2 Unscheduled OT1 Hours are
posted to OT4 due to both Policy Unscheduled Hours Mapping Settings and
Holiday Hours Mapping Settings. This occurs because the Holiday Hours
Mapping Type is higher priority than the Policy Unscheduled Hours Mapping
Type.

![](/img/Differential-Pay-Amount.gif)
