---
title: "Scheduling Availabilitw"
description: ""
---

## Scheduling Availability Tab

The availability tab allows availability schedules to be assigned to
an employee. Availability Types are templates which reflect the normal
hours an employee is considered available for work related duties. Availability
Types are intended for use by organizations with dynamic scheduling environments
such as restaurants where staffing requirements are based on customer
demand. Additional details on the use and configuration of Availability
Types can be found in the Schedule Configuration Section of this document.

To assign an Availability Schedule to an employee do the following:

- Open the employee table
- Select the employee you want to assign the availability
- In the Employee Update form go to the Schedule Information section
  of the update form
- Click on the Availability Tab

![](/img/WCC_Update_Form.gif)

- Click on the insert button.

![](/img/Manager-Module.gif)

- On the description, click on the magnify glass to select an availability
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

![](/img/Grid.gif)

Insert
â Adds a blank record to the Trained Tasks tab for the respective employee.
Select the Trained Task Description for which the employee has been trained
and then enter the hourly wage which the employee receives for the respective
trained task.

![](/img/CSVType.gif)

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

![](/img/Valid_Departments.gif)

Insert
â Adds a blank record to the Trained Tasks tab for the respective employee.
Select the Trained Task Description for which the employee has been trained
and then enter the hourly wage which the employee receives for the respective
trained task.

![](/img/SoftwareOverview_010.png)

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
| ------------------------------------------------------ | -------------------------------------------------------------------- |
| 6:00 AM - 3:00 PM                                      | Checked                                                              |
| 8:00 AM - 5:00 PM                                      | Checked                                                              |
| 12:00 PM - 8:00 PM                                     | Checked                                                              |
| 3:00 PM - 11:00 PM                                     | Checked                                                              |
| 5:00 PM - 2:00 AM                                      | Unchecked                                                            |
| 6:00 PM - 3:00 AM                                      | Unchecked                                                            |
| 7:00 PM - 4:00 AM                                      | Unchecked                                                            |
| 11:00 PM - 7:00 AM                                     | Unchecked                                                            |

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

![](/img/CliientShortcuts.png)

Insert
â Opens the Employee Valid Department Update Form. Type the first few
characters of the desired department and click OK to set the Department
as a Valid Department for the respective employee.

![](/img/EmployeeProfile_008.png)

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

![](/img/Workers_comp_code_table.gif)

Insert
â Opens the Valid Telephone Number Update Form. First enter the valid
phone number on the General Tab which the employee is permitted to call
from. Then click on the Default Schedule Tab and create a schedule to
describe the time frame the employee may call from the respective phone
number. Defining Schedules for a valid telephone number is optional. If
no schedule is defined, the Telephone Punch Interactive Voice Menu will
accept calls from the respective phone number 24x7.

![](/img/Availability.gif)

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

![](/img/QSG_USAGE_LoginDefPW.gif)

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

![](/img/SoftwareOverview_022.png)

Insert
â Opens the Employee Wage Update Form as shown below.

![](/img/IT70ServerOffSiteClients.JPG)

Department

- If the employee must work in a specific
  department to be eligible for the wage, specify the department here by
  entering the first few letters of the department name or select the department
  from the Department Table using the Lookup Magnify Glass.

Job

- If the employee must work in
  a specific job to be eligible for the wage, specify the job here by entering
  the first few letters of the job name or select the job from the Job Table
  using the Lookup Magnify Glass.

Task

- If the employee must work in
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

![](/img/CH2ConfigReq_4.gif)

Insert
â Opens the Employee Wage Update Form as shown below.

![](/img/SoftwareOverview_008.png)

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
