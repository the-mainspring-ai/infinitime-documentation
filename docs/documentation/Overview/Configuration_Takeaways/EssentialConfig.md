---
title: "InfiniTime Configuration - Essential Concepts and Features"
description: "A concise overview of key configuration aspects and features of the InfiniTime Time and Attendance solution for effective payroll integration and organizational needs."
---

xml version="1.0" encoding="utf-8" ?

EssentialConfig

## InfiniTime Configuration - Takeaways & Essential Concepts

As a versatile Time and Attendance Solution with the ability to meet
the needs of enterprise organizations with a single location to organizations
with multiple locations and unique requirements InfiniTime
offers a variety of features. It is important to note that nearly all
features within the InfiniTime
Time and Attendance application are optional and can be configured or
ignored (IE: Disabled) to meet the needs of the organization. With this
in mind, the table below provides a list of specific features that must
be configured in order to successfully transfer employee hours and earnings
to a Payroll Application - either manually using InfiniTime
Reports and Data Entry or automatically using the InfiniTime
Payroll Export Feature. For clarity, each feature and its place in the
day to day operational use of InfiniTime,
or process flow, is also provided below.

InfiniTime Initial Configuration

 | Step | Task | Related Deliverable(s) | Related Documentation | 
| --- | --- | --- | --- |
 | 1 | InfiniTime Installation | _ InfiniTime Server must meet minimum requirements. | _ Minimum Requirements _ Information Technology Brief | 
 | 2 | Distribute Client Shortcuts to all Client Machines | _ Client Shortcuts must be placed on All Client Machines for use by InfiniTime Administrators, Payroll Clerks, Supervisors, and End Users as appropriate. | _ [Client Access Overview](../ovr_SoftwareOverview.md#so2_Client_Access_Overview) | 
 | 3 | Create Employee Profile for all Supervisors and Administrators | _ Distribute Login IDs and Passwords to Supervisors and Software Administrators. | _ [Employee Profiles](../ovr_SoftwareOverview.md#so153_Employee_Profiles_and_Related_Settings) | 
 | 4 | Software Administrators should familiarize themselves with the InfiniTime Application and gather employee information from existing Human Resources and / or Payroll Software for import. | _ Complete the Employee Import Template. _ Import Employees into InfiniTime. | _ [InfiniTime Software Overview](../ovr_SoftwareOverview.md#so1_InfiniTime_Software_Overview_Introduction) \* _ [InfiniTime Import Tool](../ovr_SoftwareAdministration.md#imp1_Import_Introduction) | 
 | 5 | Install all Hardware Time and Attendance Terminals and confirm Punch Flow | _ Install all Hardware Time and Attendance Terminals at the desired location _ Confirm Employee Filters are configured as appropriate for each Hardware Time and Attendance Terminal _ Confirm Punch Flow | _ [Refer to the Information Technology Brief](https://version9.infinitimeonline.net/InfiniTime/RESOURCES/SoftwareAdministration_ITBrief.pdf) _ Refer to Hardware Documentation for your chosen Time and Attendance Terminal Model | 
 | 6 | Software Administrators and Human Resources Managers should document current Time and Attendance Rules using the provided Questionnaire. | _ Complete the Questionnaire for each set of employees requiring distinct Time and Attendance Rules. _ Configure Policies within InfiniTime as appropriate for each set of employees with distinct Time and Attendance Rules | _ [Policy Overview](../Policies/Policy_Overview.md#pol1_Policy_Overview) | 
 | 7 | Software Administrators and Human Resources Managers should review available features and determine which optional features, if any, are desired. | _ Review available features as outlined below. _ Configure each desired feature and assign settings to employees as appropriate using Quick Assign. | _ InfiniTime Software Overview + [Manager Module Toolbar Buttons](../ovr_SoftwareOverview.md#so17_Manager_Module_Toolbar_Buttons___Menu) + [Manager Module Menu](../ovr_SoftwareOverview.md#so40_InfiniTime_Manager_Module_Menu) _ [Employee Profiles and Related Settings](../ovr_SoftwareOverview.md#so153_Employee_Profiles_and_Related_Settings) Optional Features: _ [Job Costing](../Configuration/Product_Configuration.md#cnf01_Job_Costing_Introduction) _ [Holidays](../Configuration/Product_Configuration.md#hol01_Holiday_Types_Configuration_-_Introduction) _ [Accruals](../Configuration/Accrual_Configuration.md#acc01_Employee_Accruals_Introduction) _ [Groups](../Configuration/Product_Configuration.md#gr01_Groups_Introduction) _ [Hours Mapping](../Configuration/Product_Configuration.md#hm1_Hours_Mapping) _ [Pay Premiums](../Configuration/Product_Configuration.md#pp01_Pay_Premiums_Introduction) _ [Scheduling](../Scheduling/Scheduling.md#sch01_What_do_I_want_to_accomplish_by_using_schedules_) \_ [Shift Differentials](../Policies/Policy_Overview.md#pol138_Schedule_Settings___Rules_-_Shift_Differentials_Tab) _ [Escort](../Escort/Escort_Overview.md#esc01_Escort_Overview) | 
 | 8 | Software Administrators and Human Resource Managers should: _ Review Hours and Earning Types currently tracked for employees and ensure Policies and Other Activity Types within InfiniTime are configured as needed to track all Hours and Earning Types of interest. _ Decide on the final method for transferring employee hours and earnings to Payroll. | _ Identify and List all Hours and Earning Types Tracked by your Organization + IE: Regular Hours, Overtime Hours, Paid Leave, Unpaid Leave, etc. _ Configure Other Activity Types within InfiniTime as appropriate. _ Configure Payroll Export as appropriate. | The following items are Required Features for tracking and transferring employee hours / earnings to payroll and must be configured for all InfiniTime Installations: _ [Other Activity Types](../Configuration/Product_Configuration.md#ota01_Other_Activity_Types) _ [Reports](../Reports/Reports.md#rpt01_InfiniTime_Reports_-_Introduction) OR [Payroll Export](../PayrollExport/Payroll_Export.md#pxh2_Introduction) | 
 | 9 | Software Administrators and Human Resource Managers should review the benefits of Scheduling and determine if InfiniTime Scheduling will be implemented. | _ Determine if InfiniTime Scheduling is of interest to your Organization _ Choose a Scheduling Method _ Configure Default Schedules as appropriate for employees _ Train Staff on use of the Scheduling Features to define employee schedules moving forward | _ [Scheduling Overview](../Scheduling/Scheduling.md#sch01_What_do_I_want_to_accomplish_by_using_schedules_) | 
 | 10 | Software Administrators and Human Resource Managers should familiarize themselves with InfiniTime Timecard Editing. | _ Understand available editing modes (Delayed Edit, Delayed Save, Delayed Edit Only, Both Delayed Edit & Delayed Save, Lockout) _ Understand In Line Editing _ Understand Quick Punch + Ability to use Quick Punch to insert punches for one or more employees on one or more days + Ability to use Quick Punch to Insert Other Activity / Other Amounts + Ability to use Preset and Custom Date Ranges with Quick Punch _ Understand the differences between the Company Timecard and Employee Timecard _ Select a small group of employees and insert timecards for Last Pay Period to match their actual worked hours / Paid Leave / Unpaid Leave etc. _ Review employee hours and totals as totaled on the Company Timecard and on Timecard Reports to ensure Policy Configuration accurately represents your organization's needs. _ Adjust Policy Settings if needed | _ [Timecard Editing Overview](../TimecardEditing/TimecardEditing.md#tim01_Timecard_Editing_Overview) | 
 | 11 | Software Administrators and Human Resource Managers should familiarize themselves with available reports and select specific reports for production use. | _ Determine which reports best fit the needs of your organization. _ Configure Scheduled Reports as desired. _ Confirm the SMTP Service on the InfiniTime Server is properly configured for use in your Workgroup and / or Domain. _ Understand relevant reporting features + Quick Print + Saved Reports | _ [Report Library Overview](../Reports/Reports.md#rpt01_InfiniTime_Reports_-_Introduction) _ [Automatic Report Requirements](../Reports/Reports.md#AutoReq) _ | 
 | 12 | Software Administrators and Human Resource Managers should familiarize themselves with available Security Roles and Security Configuration. | _ Security Roles and Security Features should be configured to meet the needs of your organization. _ All employees must be assigned to the appropriate security role based on their responsibilities within the InfiniTime Application. | _ [Security Overview](../Security/Security_Overview.md#sec01_Security_Overview) | 
 | 13 | A Parallel Payroll Run should be performed for the first two pay periods after InfiniTime has been configured to ensure all Hours and Earning Types have been identified and Employee Policies have been configured appropriately. | _ Employees should continue punching in and out with both the existing Time and Attendance Solution and the InfiniTime Software for one to two pay periods. _ Employee Hours and Earnings should be totaled from both the existing solution and the InfiniTime software and compared. This process helps ensure all hours and earning types have been identified and ensure  policies within InfiniTime have been configured appropriately. | \* N/A | 

InfiniTime Day to Day Operational
Use - Maintenance Tasks

During normal day to day business operations, certain events will require
InfiniTime Software Administrators,
Payroll Clerks, and / or Supervisors to take specific actions within InfiniTime. Several such tasks are
outlined below.

 | Event | Task Description | 
| --- | --- |
 | Employee Turnover | _ When an employee is terminated, their employee record should be set to Inactive. Inactive Employee records do not count toward the maximum employee count per your organization's InfiniTime Software License. | 
 | New Hire | _ When a new employee is hired, they must be added to the InfiniTime Software using the Employee Table. Alternatively, employee records may also be imported using the Import Tool. After adding a new employee, be sure to assign all settings (Security Role, Policy, Department / Job / Task, Holiday Type, Accrual Type, Groups etc.) to the employee as appropriate. | 
 | New Year | _ Holiday Dates within InfiniTime are configured on a year by year basis. Holiday Dates must be configured for each Calendar Date on which employees receive benefits. Refer to the Holidays Section of this document for additional details on configuring Holiday Dates. | 
 | Change in Time and Attendance or Paid / Unpaid Leave Policies | _ Review and Alter InfiniTime Policies, Holidays, Accruals, Other Activity Types, and / or Schedules to reflect your organization's new rule set. | 
 | Employee Hours and Earnings Exported by InfiniTime do not match those exported from the existing Time and Attendance Solution during the Parallel Payroll Run | _ Review Employee Timecards. Ensure timecards match in both systems. _ Review Other Activity Types within InfiniTime. One or more Hours and Earning Types may exist in the Current Time and Attendance System that were not added to InfiniTime. \* Review Policy Configuration within InfiniTime. Policy settings may need to be adjusted and fine tuned during the few Payroll Periods. | 

InfiniTime Day to Day Operational
Use - Example Process Flow

While the exact process flow will vary from organization to organization
based on specific features implemented within InfiniTime,
a common process flow is provided below for example purposes. As outlined
below, certain tasks should be performed Daily, Weekly, and for each Pay
Period prior to running payroll.

Daily Tasks

- Check who is Clocked In using the In and Out Board
- Check Employee Schedules
- Check and Correct Employee Exceptions
- Edit Employee Timecards to correct Exceptions

Weekly Tasks

- Print Exception Report
- Review and Edit Employee Timecards to Correct Exceptions
- Mark Employee Timecards as Reviewed
- Check and Create Employee Schedules for Next Week / Next Pay
  Period as appropriate

Payroll Tasks

- Print Exception Report
- Review and Edit Employee Timecards to Correct Exceptions if needed
- Check for Unreviewed Timecards
- Edit and Review any Unreviewed Timecards as needed
- Check for Unreviewed Timecards once more
- Print and Review Employee Timecard Reports as needed
- Obtain Employee Sign Off for their final Hours and Earnings Totals
- Export and / or Manually Enter Employee Hours and Earnings to Payroll