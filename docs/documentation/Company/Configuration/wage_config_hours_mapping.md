---
title: "Wage Configuration & Hours Mapping"
description: "Guide to InfiniTime configuration with a focus on Job Costing, its benefits, and usage in tracking employee hours and costs."
---

# InfiniTime Configuration

### Default Schedule Tab

The default schedule within a department record is used to enter a schedule
that is used for all employees assigned to the department. It is important
to note that this schedule is not required, but may be used for scheduling
purposes and is subject to the schedule hierarchy. Schedule entries assigned
to employees take precedence over each other depending on their place
in the schedule hierarchy as outlined below. The hierarchy is arranged
by schedule priority from top to bottom.

- Schedule GANNT Chart
- Employee Default Schedule
- Shifts Assigned to an Employee
- Department Default Schedule
- Policy Default Schedule

For example, the default schedule defined on an employeeâs policy would
be ignored if a default schedule was configured for the employee in their
employee or department record.

Quick Schedule - Opens the Quick
Default Schedule Tool which permits InfiniTime
Administrators to define a default schedule for all employees assigned
to the respective department. [Additional
details on use of the Quick Default Schedule Tool can be found in the
Scheduling Section](../Scheduling/Scheduling.md#sch19b_context_Quick_Default_Schedule) of this document.

### Telephone Punch Options Tab

The Telephone Punch Options Tab of the Department Update Form permits
entry of specific phone numbers which are permitted to perform a Department
Transfer into the respective department. In this way, the InfiniTime Administrator can control
which departments employees are permitted to transfer to. This feature
is especially useful for organizations who use Department Pay Premiums.
The Telephone Punch Options tab will only be displayed on the Department
Update Form if the customer's InfiniTime
Software License includes the Telephone Punch Module.

Insert -
Opens the Department Valid Telephone Number Update Form which can be used
to add individual Valid Telephone Numbers to the Department Update Form.
Valid Telephone Numbers should be entered in a 10 digit format including
the area code without dashes.

Change -
Opens the Department Valid Telephone Number Update Form for the selected
Valid Telephone Number. The InfiniTime
Administrator may then make changes to the Valid Telephone Number as desired.

Delete -
Deletes the selected Valid Telephone Number from the Valid Telephone Number
Tab. Keep in mind, employees will be permitted to transfer to the respective
department only if the phone number they are calling from is present in
the list.

Note: If no Valid Telephone Numbers are defined
for a given department, employees may transfer to the department from
any telephone number.

### Pay Premiums Tab

Premium Pay makes it possible to define
Premiums, or bonuses in the form of an increased wage. Department premiums
are paid when employees work in a given department which has premiums
configured. Premiums can be configured separately for the Regular, Overtime
One, Overtime Two, Overtime Three, and Overtime Four hour types. This
flexibility makes it possible to meet the needs of a variety of special
payment premiums. Refer to the [Pay
Premium Introduction](../../Pay_Premium_Introduction.md) section of this document for more information
on how Pay Premiums are calculated and how to configure them.

![](/img/Ch2_QA_SchedAvail.jpg)

### Hours Mapping Tab

Hours Mapping permits employee hours worked
in a given hours type to be mapped to a different hours type based on
specific conditions such as:

- Scheduled Hours worked on a specific Department
- Scheduled Hours worked on a specific Job
- Scheduled Hours worked on a specific Task
- Scheduled Hours worked on a specific Other Activity Type
- Unscheduled Hours worked on a specific Department
- Unscheduled Hours worked on a specific Job
- Unscheduled Hours worked on a specific Task
- Unscheduled Hours worked on a specific Other Activity Type

The Hours Mapping Tab of the Department
Update Form defines Hours Mapping settings for the respective department.
Hours mapping settings configured for a department will be applied to
employee scheduled and unscheduled hours.  Hours Mapping is considered
an advanced feature and is only required by approximately 30% of production
InfiniTime Installations.
Organizations with Labor Unions and specific hours costing or pay premium
rules for scheduled vs unscheduled hours often find Hours Mapping to be
required. Additional details on configuring and utilizing Hours Mapping
can be found in the [Hours Mapping
Section](Product_Configuration.md#hm1_Hours_Mapping) of this document.

![](/img/HoursMapping16.gif)

Configuring
Jobs - Introduction

Jobs within InfiniTime
are used as the second Job Costing Level. Jobs commonly relate to individual
Jobs or Invoices under which tasks are performed though they may also
be used for other types of information.

To Configure Jobs within
InfiniTime for use with
Job Costing:

1.) Identify the type of information which
will be tracked in InfiniTime
Jobs.

2.) It often helps to create a list all current
items under the chosen type of information. For example if customers are
to be used as the second Job Costing Level list all current customers
and any related information. Depending on the information being tracked
within InfiniTime the list
should contain the following:

| Information Type     | Job Description Field | Job Cost Center Field                         | Job Number Field      |
| -------------------- | --------------------- | --------------------------------------------- | --------------------- |
| Internal Departments | Department Name       | Alphanumeric Code or other Payroll Identifier | Department Number     |
| Customers / Jobs     | Customer or Job Name  | Alphanumeric Code or other Payroll Identifier | Customer / Job Number |
| Tasks                | Task Name             | Alphanumeric Code or other Payroll Identifier | Task Number           |

3.) Create one job for each listed item.
Ensure the Cost Center and Department Numbers are configured appropriately.

### Activity Job Table

The Activity Job Table displays a list of all jobs configured in the
software. Jobs are used alongside InfiniTime
Departments to further categorize employee hours for job costing purposes.
Employees can punch into and out of jobs in order to track hours worked
for separate Jobs such as Philly Mae Pizzeria, Jose's Sandwich Shop, etc.
Initially, it is important to understand the following concepts regarding
InfiniTime Departments
and Job Costing:

- Job Costing permits customers to track employee hours under various
  levels. Job costing is generally utilized in organizations where employee
  labor costs are of special interest when compared to the cost of finished
  goods such as manufacturing related organizations or where hours are
  billable to clients.

![](/img/hol34.png)

Insert

- Clicking the Insert button opens the Activity Job Update Form to create
  a new Job. Add as many jobs as needed.

Change

- Displays the Activity Job Update Form for the selected job. The InfiniTime Administrator may then
  make changes as desired.

Delete

- Clicking the Delete button will remove the highlighted job from the
  list.

### Activity Job  Update Form - General Tab

![](/img/HoursMapping16.gif)

Description - Enter the given
name of a Job within the organization.

Cost Center - Some Accounting
Packages and Payroll Services require this field in order to import InfiniTime data.  If it is not
required, this field may be left blank. Your Inception Technologies
Implementation Specialist can help you determine if the Job Cost Center
field is required for any specific payroll export. Using the same cost
center for multiple jobs will cause employee hours from all jobs with
the same Job Cost Center to be lumped together into a single cost center
when the hours are exported to payroll.

Job Number - Assign a job number
as an additional identifier for jobs.  No two jobs may have the same
job number.

Inactive - Selecting this check
box will cause the job not to appear as a selection in InfiniTime. Additionally, Inactive
Jobs will not be sent to hardware terminals. Employees will no longer
be able to transfer into or out of inactive jobs.

### Pay Premiums Tab

Premium Pay makes it possible to define
Premiums, or bonuses in the form of an increased wage. Job pay  premiums
are paid when employees work in a given job which has premiums configured.
Premiums can be configured separately for the Regular, Overtime One, Overtime
Two, Overtime Three, and Overtime Four hour types. This flexibility makes
it possible to meet the needs of a variety of special payment premiums.
Refer to the [Pay Premium
Introduction](../../Pay_Premium_Introduction.md) section of this document for more information on how
Pay Premiums are calculated and how to configure them.

![](/img/clip_image014.jpg)

### Hours Mapping Tab

Hours Mapping permits employee hours worked
in a given hours type to be mapped to a different hours type based on
specific conditions such as:

- Scheduled Hours worked on a specific Department
- Scheduled Hours worked on a specific Job
- Scheduled Hours worked on a specific Task
- Scheduled Hours worked on a specific Other Activity Type
- Unscheduled Hours worked on a specific Department
- Unscheduled Hours worked on a specific Job
- Unscheduled Hours worked on a specific Task
- Unscheduled Hours worked on a specific Other Activity Type

The Hours Mapping Tab of the Job Update
Form defines Hours Mapping settings for the respective job. Hours mapping
settings configured for a job will be applied to employee scheduled and
unscheduled hours.  Hours Mapping is considered an advanced feature
and is only required by approximately 30% of production InfiniTime Installations. Organizations
with Labor Unions and specific hours costing or pay premium rules for
scheduled vs unscheduled hours often find Hours Mapping to be required.
Additional details on configuring and utilizing Hours Mapping can be found
in the [Hours
Mapping Section](Product_Configuration.md#hm1_Hours_Mapping) of this document.

![](/img/Conf_Holidays004.png)

Configuring
Tasks - Introduction

Tasks within InfiniTime
are used as the third Job Costing Level. It should be noted that Jobs
must exist within the InfiniTimeSoftware
before Tasks can be configured. Attempting to insert a Task before configuring
at least one job will result in a warning. At least one Job must be created
before Tasks can be created. Tasks are the lowest Job Costing Level available
in the InfiniTime software
and are generally used to track various activities performed by employees
though they may also be used for other types of information.

To Configure Tasks within
InfiniTime for use with
Job Costing:

1.) Identify the type of information which
will be tracked in InfiniTime
Tasks.

2.) It often helps to create a list all current
items under the chosen type of information. For example if employees perform
ten tasks on a regular basis for any given task then list all current
tasks and any related information. Depending on the information being
tracked within InfiniTime
the list should contain the following:

| Information Type     | Task Description Field | Task Cost Center Field                        | Task Number Field     |
| -------------------- | ---------------------- | --------------------------------------------- | --------------------- |
| Internal Departments | Department Name        | Alphanumeric Code or other Payroll Identifier | Department Number     |
| Customers / Jobs     | Customer or Job Name   | Alphanumeric Code or other Payroll Identifier | Customer / Job Number |
| Tasks                | Task Name              | Alphanumeric Code or other Payroll Identifier | Task Number           |

3.) Create one task for each listed item.
Ensure the Cost Center and Department Numbers are configured appropriately.

### Activity Task Table

The Activity Task Table displays a list of all tasks configured in the
software. Tasks are used alongside InfiniTime
Departments and InfiniTime
Jobs to further categorize employee hours for job costing purposes. Employees
can punch into and out of activity tasks in order to track hours worked
for separate tasks such as Framing, Painting, Sanding etc. Initially,
it is important to understand the following concepts regarding InfiniTime Tasks and Job Costing:

- Job Costing permits customers to track employee hours under various
  levels. Job costing is generally utilized in organizations where employee
  labor costs are of special interest when compared to the cost of finished
  goods such as manufacturing related organizations or where hours are
  billable to clients.

![](/img/AccessQA.jpg)

Insert

- Clicking the Insert button opens the Activity Task Update Form to create
  a new Task. Add as many tasks as needed.

Change

- Displays the Activity Task Update Form for the selected task. The InfiniTime Administrator may then
  make changes as desired.

Delete

- Clicking the Delete button will remove the highlighted task from the
  list.

### Activity Task  Update Form - General Tab

![](/img/OTA_16.png)

Description - Enter the given
name of a Task within the organization.

Cost Center - Some Accounting
Packages and Payroll Services require this field in order to import InfiniTime data.  If it is not
required, this field may be left blank. Your Inception Technologies
Implementation Specialist can help you determine if the Task Cost Center
field is required for any specific payroll export. Using the same cost
center for multiple tasks will cause employee hours from all tasks with
the same Task Cost Center to be lumped together into a single cost center
when the hours are exported to payroll.

Task Number - Assign a task
number as an additional identifier for jobs.  No two tasks may have
the same job number.

Inactive - Selecting this check
box will cause the task not to appear as a selection in InfiniTime. Additionally, Inactive
Tasks will not be sent to hardware terminals. Employees will no longer
be able to transfer into or out of inactive tasks.

### Pay Premiums Tab

Premium
Pay makes it possible to define Premiums, or bonuses in the form of an
increased wage. Task pay  premiums are paid when employees work in
a given task which has premiums configured. Premiums can be configured
separately for the Regular, Overtime One, Overtime Two, Overtime Three,
and Overtime Four hour types. This flexibility makes it possible to meet
the needs of a variety of special payment premiums. Refer to the [Pay
Premium Introduction](../../Pay_Premium_Introduction.md) section of this document for more information
on how Pay Premiums are calculated and how to configure them.

![](/img/JobPrem_1.gif)

### Hours Mapping Tab

Hours Mapping permits employee hours worked
in a given hours type to be mapped to a different hours type based on
specific conditions such as:

- Scheduled Hours worked on a specific Department
- Scheduled Hours worked on a specific Job
- Scheduled Hours worked on a specific Task
- Scheduled Hours worked on a specific Other Activity Type
- Unscheduled Hours worked on a specific Department
- Unscheduled Hours worked on a specific Job
- Unscheduled Hours worked on a specific Task
- Unscheduled Hours worked on a specific Other Activity Type

The Hours Mapping Tab of the Task Update Form defines Hours Mapping
settings for the respective task. Hours mapping settings configured for
a task will be applied to employee scheduled and unscheduled hours.  Hours
Mapping is considered an advanced feature and is only required by approximately
30% of production InfiniTime
Installations. Organizations with Labor Unions and specific hours costing
or pay premium rules for scheduled vs unscheduled hours often find Hours
Mapping to be required. Additional details on configuring and utilizing
Hours Mapping can be found in the [Hours
Mapping Section](Product_Configuration.md#hm1_Hours_Mapping) of this document.

![](/img/3WAVG.jpg)

Employee
Job Costing Settings

Employee's can be assigned to a Default Department,
Job, and Task. In this way employee activity will be automatically associated
with a specific Department, Job, and/or Task when they punch in. Employees
can also use the Transfer Button or the Employee and Punch Modules to
switch between Departments, Jobs and Tasks throughout the day. The transfer
button varies in location and use for each hardware terminal. Please refer
to the appropriate manual for your Hardware Device in the Hardware section
of this document for additional information.

To Assign a Default Department, Job, or Task
to an employee:

1.) Click on the Employee Button on the main
toolbar to open the employee table.

![](/img/21DHOLAVG.jpg)

2.) Select the employee you wish to configure
Job Costing Settings for from the list and click change.

![](/img/OTA_27.png)

3.) Click on the Settings Tab.

![](/img/Groups01.gif)

4.) Select the Department, Job, or Task you
would like to assign as the employee's default. It should be noted the
Job and Task fields will not be displayed until at least one Job or Task
is configured within InfiniTime.
This simplifies the display of the Settings Tab for companies who do not
utilize Job Costing.

![](/img/OTA_8.png)

Note: Only the Default Department is required.
 The Default Job and Default Task fields are not required as some
companies may not wish all employees to have their activity associated
with a Job or Task by default. In this way Office workers who simply work
in a department.

Displaying
Job Costing information within the Company and Employee Specific Timecard
Tables

Job Costing is disabled
by default within the InfiniTime
Application. As such Job Costing related fields such as Task and Job must
be added to the grid in the Company Timecard Table and Employee Specific
Timecard Table. It is only necessary to configure these settings once.
The software will save any alterations made to the grid. It should be
noted the grid configuration is a global setting which effects all users.
Additional information on Grid Configuration can be found in the [Customizing
InfiniTime](../SoftwareOverview/Modules/User_Interface/FormCompletion/Customizable_Table_Display__The_InfiniTime_Grid.md) section of this document.

To add the Task and Job
Fields to the Company Timecard Table:

1.) Click on the Timecard Button in the main
toolbar to open the Company Timecard Table

![](/img/EmployeeProfile_023.png)

2.) Click on the 'Select Grid Columns' button.
( ![](/img/EmployeeProfile_026.png).gif))

![](/img/JobPrem_4.gif)

3.) Locate the Task and Job Fields on the
'Available' list and click on ![](/img/TaskPrem_2.gif)
to move them to the 'Selected' list.

![](/img/EmployeeProfile_032.png)

4.) Use the ![](/img/JobCosting_Config_15.gif) and ![](/img/OTA_14.png) buttons to move the Task and Job Fields
up and down in the list to alter order columns will be displayed in.

![](/img/OTA_26.png)

5.) Click Apply to confirm and save your
changes.

![](/img/OTA_22.png)

6.) The Job and Task fields will be displayed
in the Timecard Table.

![](/img/Ch2_QA_GroupUnsel.jpg)

Configuring
Wages

It is not uncommon for employee wages to
vary based upon the task, job, or department, where employees are working.
Wages within InfiniTime
can be allocated to a specific Job, Task, Department, or any combination
thereof. Additional information on how to use wages with Job Costing can
be found in the [Job Costing -
Wages](../../Job_Costing_-_Wages.md) section of this document.

To Configure Wages for use with Job Costing:

1.) Click on the Employee Button on the main
toolbar to open the employee table.

![](/img/OTA_30.png)

2.) Select the employee you wish to configure
Wages for from the list and click change.

![](/img/HoursMapping15.gif)

3.) Click on the Wages Category.

![](/img/JobCostingWages_5.gif)

4.) Click on Insert

![](/img/HoursMapping14.gif)

5.) Choose a combination of Department, Job,
or Task for which the wage will apply.

![](/img/JobCostingWages_1.gif)

6.) Click OK to save the record.

![](/img/JobCosting_Config_20.gif)

Additional details on
Job Costing and Wages can be found in the [Job
Costing and Employee Wages section](Product_Configuration.md#cnf17_Job_Costing_-_Wages) of this document.

### Job Costing - Data Collection

InfiniTime supports multiple
sources for Employee Job Costing Activity. When choosing a time source
for Employee Job Costing Activity it is important to understand any restrictions
and configuration options associated with the solution in order to make
the most of InfiniTime's
Job Costing System. Each supported source and its Job Costing Properties
are listed below.

### PC Punch: InfiniTime Employee and Punch Modules

Supported Levels - From
1 to 3 Levels

The InfiniTime
Employee and Punch Modules support all three available Job Costing levels:
Departments, Jobs, and Tasks.

Benefits

Omnipresence: The InfiniTime Employee and Punch Modules
are available from anywhere the InfiniTime
Application can be accessed. Employees can clock in and out for different
Departments, Jobs, and Tasks from any computer with access to the InfiniTime
application using their Login ID and Password. If the InfiniTime
Software has been published to the Internet employees can access the software
worldwide from any computer with internet access using their login credentials.

Customization:
Through use of security roles and configuration the Employee and Punch
Modules can be customized to permit or deny employees the ability to choose
which Department, Job, or Tasks they are working in. In this way employees
can be configured with a default Department and/or Job in such a way that
they are only permitted to change the task they are punching into and
out of.

Optional: The InfiniTime
Employee and Punch Modules can also be made available to employees as
an alternate method for punching in even if hardware terminals such as
the Thor are available. Some companies may wish to disable the ability
to use the InfiniTime Employee
and Punch modules for punching in and out if hardware terminals are available.
This can be accomplished by configuring security for the Employee Punch
Information window and disabling access for the employee security role.
Refer to the [Security
Roles Section of this document](../Security/Security_Overview.md#sec07_Security_Roles) for more information.

### Black & White Terminals: InfiniTime Luna,  Zephyr, Athena, & Juno

Supported Levels - From
1 to 2 Levels

The Luna, Zephyr, Athena,
and Juno support two of the three available Job Costing levels: Departments
and Jobs.

Benefits

Mobility: Employees can punch in and out
without access to a computer using hardware terminals.

Job Costing: Permits employees to choose
between available Departments and Jobs assigned to the reader when punching
in and out. Employees can also switch between departments and jobs as
needed.

Available Departments & Jobs: A maximum
of 100 Departments and 100 Jobs can be assigned to these readers. In this
way the supervisor can configure multiple departments and jobs within
the InfiniTime Application
and only provide employees with the ability to punch into or out of a
subset of Departments and Jobs. This feature is most suited for manufacturing
or construction environments where specific jobs are performed in the
area where the clock is located.

### Color Terminals: InfiniTime Thor

Supported Levels - From
1 to 3 Levels

The
Thor supports all three available Job Costing levels: Departments, Jobs,
and Tasks.

Benefits

Mobility: Employees can punch in and out
without access to a computer using hardware terminals.

Job Costing: Permits employees to choose
between available Department, Jobs and Tasks assigned to the reader when
punching in and out. Employees can also switch between departments, jobs
and tasks as needed.

Available Departments,
Jobs, and Tasks: A maximum of 100 Departments, 100 Jobs, and 100 tasks
can be assigned to these readers simultaneously. In this way the supervisor
can configure multiple departments, jobs, and tasks within the InfiniTime Application and only provide
employees with the ability to punch into or out of a subset of Departments,
Jobs, and Tasks. This feature is most suited for manufacturing or construction
environments where specific jobs and tasks are performed in the area where
the clock is located.

Intelligent Transfer:
If only a single Department, Job, or Task is assigned to the clock using
the Available Departments, Jobs, or Tasks features the Thor will not ask
for the employee to enter that item when using the Transfer Button. In
this way employees will only be prompted to choose the Task they wish
to work under when using the Transfer Button if a single Department and
Job are assigned to the reader. This concept can be applied to Departments,
Jobs, or Tasks - whereby employees will only have to choose one item be
it Department, Job, or Task when using the Transfer Button.

Alternative Transfer

- If only a single Department, Job, and Task is assigned to the clock
  using the Available Departments, Jobs, and Tasks features the Thor will
  not prompt the employee to enter their Department, Job, or Task when using
  the Transfer Button. The Thor will simply use the single department, job,
  and task that have been assigned to the clock. In this way two scenarios
  can easily be configured for the clock using the Default Department, Job,
  and Task Settings and the Transfer Button. When employees punch in their
  activity will automatically be associated with their default Department,
  Job, and Task. When using the transfer button their activity will be associated
  with the Department, Job, and Task assigned to the Thor through the Available
  Departments, Jobs, and Tasks feature.

External Wand: An external
reader can be attached to the Thor which reads barcode badges for the
purpose of Job Costing. InfiniTime
can be configured to parse the number encoded on the badge to find Department,
Job, and Task information. In this way employees can quickly swipe a badge
to transfer between Departments, Jobs, or Tasks.

Transfer By Item Number:
Both the Thor and Scout Terminals support Department, Job, and Task switching
through use of item numbers. Each item has a unique numeric identifier
which is sent to the clock. Employees can enter this unique identifier
in order to select the Department, Job, or Task when punching in. Unique
Identifiers for each Job Costing level are displayed below. Refer to the
[Job Costing
Introduction: Job Transfer](../../Job_Costing_Introduction.md#Labor Transfer) section of this document for more information.

### Biometric Terminals: Scout 2000, 3000, and 4000 Terminals

Supported Levels - From
1 to 3 Levels

The Scout Terminals
support all three available Job Costing levels: Departments, Jobs, and
Tasks.

Benefits

Mobility: Employees can punch in and out
without access to a computer using hardware terminals.

Job Costing: Permits employees to choose
between available Department, Jobs and Tasks assigned to the reader when
punching in and out. Employees can also switch between departments, jobs
and tasks as needed.

Available Departments,
Jobs, and Tasks: A maximum of 100 Departments, 100 Jobs, and 100 tasks
can be assigned to these readers simultaneously. In this way the supervisor
can configure multiple departments, jobs, and tasks within the InfiniTime Application and only provide
employees with the ability to punch into or out of a subset of Departments,
Jobs, and Tasks. This feature is most suited for manufacturing or construction
environments where specific jobs and tasks are performed in the area where
the clock is located.

Transfer By Item Number: Both the Thor and
Scout Terminals support Department, Job, and Task switching through use
of item numbers. Each item has a unique numeric identifier which is sent
to the clock. Employees can enter this unique identifier in order to select
the Department, Job, or Task when punching in. Unique Identifiers for
each Job Costing level are displayed below. Refer to the [Job
Costing Introduction: Job Transfer](../../Job_Costing_Introduction.md#Labor Transfer) section of this document for more
information.

| Item        | Unique Identifier |
| ----------- | ----------------- |
| Departments | Department Number |
| Jobs        | Job Number        |
| Tasks       | Task Number       |

Note: The hardware terminals and software
modules listed above are the only supported methods for tracking multi-level
Job Costing information. A table listing supported Job Costing Levels
for all InfiniTime Readers
is provided below for quick reference.

| Clock Model   | Supported Job Costing Levels | Supported Information Types |
| ------------- | ---------------------------- | --------------------------- |
| Apollo SY715  | 1                            | Department                  |
| Athena        | 2                            | Department, Job             |
| Atlas SY777   | 1                            | Department                  |
| Juno          | 2                            | Department, Job             |
| Luna          | 2                            | Department, Job             |
| Omega SY755   | 1                            | Department                  |
| Orion SY760   | 1                            | Department                  |
| Odyssey SY780 | 1                            | Department                  |
| Scout         | 3                            | Department, Job, Task       |
| Thor          | 3                            | Department, Job, Task       |
| Zephyr        | 2                            | Department, Job             |

### Job Costing - Wages

It is not uncommon for employee wages to vary
based upon the task, job, or department, where employees are working.
Wages within InfiniTime
can be allocated to a specific Job, Task, Department, or any combination
thereof. This makes it possible to calculate gross totals based upon which
Department, Job, or Task employees are working in. When using wages with
Job Costing it is important to understand how InfiniTime
identifies which wage to use for an employee. InfiniTime
searches wage records for an employee attempting to match items between
the wage record and where the employee is actively working according to
the wage hierarchy below. Employees will be paid using the wage corresponding
to the first match.

Wage Hierarchy

1.) Department, Job, and Task

2.) Department, Job

3.) Department, Task

4.) Job, Task

5.) Department

6.) Job

7.) Task

For example if an employee worked in the West
Coast Marina Department, Job Number 117852, and the Painting Task InfiniTime would first search for
a wage record matching all three items - West Coast Marina, 117852, and
Painting. If a record was not found for this combination the software
would search for a wage record matching Department and Job which in this
example is West Coast Marina and 117852. If a wage record was not found
for this combination the software would continue down the wage hierarchy
searching for a matching wage record. If no match is found the employee's
default wage is used.

### Wage Configuration

Configuring a Wage for
a specific combination of three items

A wage associated with a specific combination
of Department, Job, and Task will take precedence over all other wages.
For example if wages are configured as shown below the employee will receive
the wage associated with the exact Department, Job, and Task combination
worked by the employee rather than the wage associated with the Task the
employee is working in. Referring to the Wage Hierarchy this occurs because
InfiniTime will match a
wage associated with Department, Job, and Task before a wage associated
with just the Task. Additional examples are below. The highlighted wage
record is the wage the employee will be paid.

Example 1

| Working Department (Customer) | Working Job (Job Number) | Working Task (Task) |
| ----------------------------- | ------------------------ | ------------------- |
| West Coast Marina             | 117852                   | Painting            |

![](/img/HoursMapping15.gif)

Example 2

| Working Department (Customer) | Working Job (Job Number) | Working Task (Task) |
| ----------------------------- | ------------------------ | ------------------- |
| West Coast Marina             | 117852                   | Painting            |

![](/img/EmployeeProfile_035.png)

The above examples illustrate how employees
will receive the wage associated with the particular Department, Job,
and Task they are working on even if another wage is defined for each
individual item or a combination thereof.

Configuring a Wage for
a specific combination of two items

A wage associated with a specific combination
of two items should be used if employees receive a specific wage when
working under two items such as a specific Department and Task or a specific
Job and Task. For example if an employee receives  $8 when working
in the West Coast Marina Department and performing the Painting Task regardless
of what Job they are working on a wage should be created and associated
with the West Coast Marina Department and Painting Task as shown below.
 It is important to keep the Wage Hierarchy in mind when associating
a wage with a combination of two items. In example 2 the employee would
be paid $8 per hour rather than $10 because a wage matching the exact
working Department, Job, and Task is present. This will be matched before
the combination of Department and Task.

Example 1

| Working Department (Customer) | Working Job (Job Number) | Working Task (Task) |
| ----------------------------- | ------------------------ | ------------------- |
| West Coast Marina             | 117852                   | Painting            |

![](/img/Conf_Holidays006.png)

Example 2

| Working Department (Customer) | Working Job (Job Number) | Working Task (Task) |
| ----------------------------- | ------------------------ | ------------------- |
| West Coast Marina             | 117876                   | Painting            |

![](/img/OTA_29.png)

The above examples illustrate how the employee
will receive the wage associated with their particular Task and Department
regardless of what job they are working on unless a wage record exists
that matches the Department, Job, and Task worked by the employee.

Configuring a Wage for
a specific item

Wages should be configured for a specific
item such as a Department, Job, or Task when employees have a set wage
for the item. For example, if an employee was paid $10 per hour when painting
regardless of what job or department he was painting under a wage should
be created and associated with the Painting task only as shown below.
In this way it would not matter what department or job the employee was
working under as long as he was performing the painting task he would
receive $10 per hour. It is important to keep the Wage Hierarchy in mind
when associating a wage with a single item. In example 2 the employee
would be paid $8 per hour rather than $10 because a wage matching the
exact working Department, Job, and Task is present.

Example 1

| Working Department (Customer) | Working Job (Job Number) | Working Task (Task) |
| ----------------------------- | ------------------------ | ------------------- |
| Ahbor Harbor                  | 117852                   | Painting            |

![](/img/ColSel_Down.gif)

In the example above even though there is
a wage record for each item where the employee is working the Department
record takes precedence as it is matched first due to the Wage Hierarchy.

Example 2

| Working Department (Customer) | Working Job (Job Number) | Working Task (Task) |
| ----------------------------- | ------------------------ | ------------------- |
| West Coast Marina             | 117876                   | Painting            |

![](/img/OTA_29.png)

The above examples illustrate how the employee
will receive the wage associated with a single item unless a different
record is matched due to the Wage Hierarchy as in Example 2.

### Other Activity Types

Other Activity Types permit InfiniTime
administrators to define 'non-working' hours and earning types for items
such as Paid Leave, Unpaid Leave, Tips, Commissions, and Bonuses. InfiniTime provides support for an
unlimited number of Other Activity Types. Other Activity entries can be
entered in hours, currency, or units depending on the requirements and
capabilities of your payroll application. The Other Activity Table, as
shown below, is used to Insert, Modify, and Delete Other Activity Types
within InfiniTime. As part
of the initial configuration of InfiniTime,
one Other Activity Type should be created for each 'non-working' Hours
/ Earning Type tracked by your organization. Examples of typical Other
Activity Types are provided in the [Other
Activity usage section](Product_Configuration.md#ota29_Other_Activity_Types_-_Usage) below.

Accessing
the Other Activity Types Table

- Click on Lookups
- Click on Calculation Setup

![](/img/TaskPrem_4.gif).gif)

- Click on Other Activity Types

![](/img/OTA_6.png).gif)

Insert
â Inserts a new record into the Other Activity Type Table. Opens the Other
Activity Update Form.

Change
â Opens the Other Activity Type Update form and permits editing of the
selected record.

Delete
â Removes the highlighted record from the Other Activity Table.

### Other Activity Update Form

The Other Activity Update Form includes all options and settings related
to Other Activity Types. Each option is outlined below.

![](/img/Ch2_QA_Shifts1.jpg)

Description
â Type the name of the Other Activity Type.

Type
â Specify whether the Other Activity Type will track a dollar amount or
hour amount.

Code Number
â The Code Number is a unique identifier within the InfiniTime
Database. Each other activity type must have a unique code number in order
to set them apart. This code number is used on many hardware terminals
to input other activity directly at the clock without accessing the software.
All hardware terminals offered by Inception Technologies support this
feature except for the Plus Scanner.

Payroll
Mapping Number â Enter a mapping number. The payroll mapping
number can be the same for multiple other activity types. This number
specifies a column in a payroll export file where hours or amounts for
the other activity type will be totaled. If more than one other activity
type has the same payroll mapping number their values will be added together
and totaled in the same column. Mapped Payroll Interfaces provide the
customer with the ability to add additional other activity types and move
their position within the payroll export on the fly.

The Compupay â Mapped Interface Format is one such payroll interface.
An outline of the Compupay - Mapped interface format is provided below.
The outline shows a row of headers which represent information that would
be exported when performing a payroll export. The resulting export file
can then be imported directly into the Compupay application. It is important
to understand how Other Activity Types are automatically exported to the
appropriate column according to their Payroll Mapping Number. Other Activity
Types with Payroll Mapping Number 1 will be totaled in the column labeled
Mapped Amount 1. Other Activity Types with Payroll Mapping Number 2 will
be totaled in the column labeled Mapped Amount 2.

| Employee ID | Activity Dept Number | Regular Hours | Overtime Hours | Mapped Amnt. 1 | Mapped Amnt. 2 | Mapped Amnt. 3 |
| ----------- | -------------------- | ------------- | -------------- | -------------- | -------------- | -------------- |

Payroll
Mapping Codes

Payroll Mapping Codes are agreed upon by
each company and the firm responsible for their payroll. With this in
mind it is not surprising that Payroll Mapping Codes often vary from company
to company. These codes are generally known to payroll personnel or the
company responsible for your payroll. Additional details on the use of
Payroll Codes and Payroll Mapping Codes can be found in the following
sections of this document:

[Payroll
Export User Interface Overview - Payroll Codes Tab](../PayrollExport/Payroll_Export.md#pxh19_Payroll_Codes_Tab)

[Payroll
Export - Payroll Interface Features & Related Configuration](../PayrollExport/Payroll_Export.md#pxh42_Payroll_Interface_Features___Related_Configuration)

[Payroll
Interface Layout Report](../Reports/Reports.md#rpt57_Payroll_Interface_Layout)

Regular
Hours Payroll Mapping Code - Enter a Payroll Mapping Code to
be used for Regular Hours and / or Other Hours on the respective Other
Activity Type. Much like the Payroll Mapping Number, the Regular Hours
Payroll Mapping Code can be the same for multiple other activity types,
however it is generally used as a unique code to identify an Hours / Earnings
Type.

OT1
Payroll Mapping Code - Enter a Payroll Mapping Code to be used
for OT1 Hours on the respective Other Activity Type. This field is disabled
unless 'Count as Regular Hours' or 'Only Count as Regular Hours if Scheduled'
is checked for the respective other activity type. Much like the Payroll
Mapping Number, the OT1 Payroll Mapping Code can be the same for multiple
other activity types, however it is generally used as a unique code to
identify an Hours / Earnings Type.

OT2
Payroll Mapping Code -  Enter a Payroll Mapping Code to
be used for OT2 Hours on the respective Other Activity Type. This field
is disabled unless 'Count as Regular Hours' or 'Only Count as Regular
Hours if Scheduled' is checked for the respective other activity type.
Much like the Payroll Mapping Number, the OT2 Payroll Mapping Code can
be the same for multiple other activity types, however it is generally
used as a unique code to identify an Hours / Earnings Type.

OT3
Payroll Mapping Code -  Enter a Payroll Mapping Code to
be used for OT3 Hours on the respective Other Activity Type. This field
is disabled unless 'Count as Regular Hours' or 'Only Count as Regular
Hours if Scheduled' is checked for the respective other activity type.
Much like the Payroll Mapping Number, the OT3 Payroll Mapping Code can
be the same for multiple other activity types, however it is generally
used as a unique code to identify an Hours / Earnings Type.

OT4
Payroll Mapping Code -  Enter a Payroll Mapping Code to
be used for OT4 Hours on the respective Other Activity Type. This field
is disabled unless 'Count as Regular Hours' or 'Only Count as Regular
Hours if Scheduled' is checked for the respective other activity type.
Much like the Payroll Mapping Number, the OT4 Payroll Mapping Code can
be the same for multiple other activity types, however it is generally
used as a unique code to identify an Hours / Earnings Type.

Common
Payroll Code Examples:

| Other Activity Type | Example Payroll Mapping Codes |
| ------------------- | ----------------------------- |
| Holiday Hours       | HOL, HOLIDAY                  |
| Vacation Hours      | VAC, VACATION                 |
| Sick Time Hours     | SICK, SIC, SIK                |
| Personal Time Hours | PER, PERS, PERSONAL           |

Attendance
Review Report Character - Enter a single character to be displayed
on the Attendance Review Report for dates with Hours and / or Other Amounts
for the respective Other Activity Type. Refer to the [Attendance
Review Report section of the Report Library](../Reports/Reports.md#rpt59_Attendance_Review) for additional details.

Count
As Regular Hours - When this option is checked hours entered
under this other activity type will count as regular hours and will be
counted toward both daily, weekly, Day Of Week, and Unscheduled Overtime
as configured within an employee's assigned policy. InfiniTime
Administrators may choose to specifically exclude the respective Other
Activity Type from certain types of Overtime by checking additional options
as outlined below.

Only
Count as Regular Hours if Scheduled - When this option is checked,
hours entered under the respective Other Activity Type will only be counted
as regular hours // totaled toward Daily, Weekly, Day Of Week, and Unscheduled
Overtime on dates which an employee is scheduled. If the respective Other
Activity Type should be inserted on a date where the employee is not scheduled,
the hours will simply be paid as Other Hours under the Regular Hours Payroll
Mapping Code. This concept is illustrated below. Notice how Other Hours
for the Shift Change Other Activity Type are totaled in the regular column
only on 7/30/13 where the employee was scheduled to work.

![](/img/CH3_CompInfo3.gif)

Count
As Day Worked â When this check box is checked, the date on
which the respective Other Activity Type is inserted will be counted as
a Worked Day. This option is used for two purposes:

- First, if an Other Activity Type with 'Count as Day Worked' checked
  is inserted on a date with an Absent Exception then the Absent Exception
  will be removed.
- Second, if an Other Activity Type with 'Count as Day Worked' checked
  is inserted on a date immediately prior to or immediately after a
  Holiday Date the 'Employee Must Work Day Before' / 'Employee Must
  Work Day After' Holiday Requirements will be met and InfiniTime will insert the Holiday
  Record according to the Holiday Date Settings.

Count
As Hours Worked for Accrual Calculations - When this option
is checked, Other Activity Hours for the Other Activity Type will be counted
toward the Accrue X Hours for Y Hour(s) Accrual Calculation. This makes
it possible for employees to earn accrual hours based on Worked Hours
(Regular, Overtime 1, Overtime 2, Overtime 3, Overtime 4) and Other Activity
Types such as Vacation, Personal Time, Jury Duty, etc.

Allow
Start Time Entry - When this option
is checked, InfiniTime
will prompt the user to enter the Start Time when inserting Other Hours
for the respective Other Activity Type. In this way, the Other Activity
Hours can be properly mapped according to Unscheduled Hours Mapping rules
and Shift Differential Rules configured on an employee's policy. Allow
Start Time Entry must be checked in order to check 'Apply Shift Differential'
for a given Other Activity Type. Allow Start Time Entry is only available
for Other Activity Types set to 'Count as Regular Hours' or 'Only Count
as Regular Hours if Scheduled'.

![](/img/clip_image022.jpg)

Use Scheduled
Hours - If this option is checked,
InfiniTime will automatically
set the Other Hours to match the duration of the employee's schedule on
the respective date. When 'Use Scheduled Hours' is enabled, users may
not directly enter or edit the Other Hours for a given date for the respective
Activity Type. Additionally, the respective activity type cannot be inserted
for an employee with no scheduled hours on a given date.

![](/img/EmployeeProfile_033.png)

Permit
Entry Only If Scheduled - If this
option is checked, InfiniTime
will only permit the respective Other Activity Type to be inserted on
days where an employee has a Schedule. If an Other Activity Type with
this option is entered via Other Activity Entry from a Hardware Terminal
on a date where an employee does not have a schedule the Other Activity
Entry will be ignored by the InfiniTime
Software during the polling process and the Other Activity Hours will
not be posted to the employee's timecard. The warnings below are displayed
if a user should attempt to insert an Other Activity Type with 'Permit
Entry Only if Scheduled' Checked on a date where an employee is not scheduled.

![](/img/OTA_28.png)

![](/img/hol30.png)

Apply
Shift Differential - If this option
is checked, Other Hours for the respective Other Activity Type will be
counted toward Shift Differential Hours in accordance with the Shift Differential
Pay Method and Shifts assigned to the employee's policy. 'Apply Shift
Differential' is only available if 'Allow Start Time Entry' and 'Count
as Regular Hours' or Only Count as Regular Hours if Scheduled' are checked.
The example below shows Other Hours for the Other Activity Type Shift
Change applied toward the Day Shift Differential from 8:00 AM to 5:00
PM.

![](/img/TaskPrem_4.gif)

Exclude
From Day Of Week Overtime - If
this option is checked, Hours for the respective Other Activity Type will
not count toward Day of Week Overtime. 'Exclude from Day of Week Overtime'
is only available for Other Activity Types with 'Count as Regular Hours'
or Only Count as Regular Hours if Scheduled' checked. For example, if
an employee were to have Vacation Time, which is set to Count as Regular
Hours, on a Sunday where they would usually get Day of Week Overtime for
worked hours and 'Exclude From Day Of Week Overtime' is checked, the employee
would simply be paid their regular base rate for Vacation Time Hours on
Sundays instead of the Day Of Week Overtime Rate.

Example: Company XYZ Excludes Vacation Time
from Day of Week Overtime. Employees who are normally scheduled to work
on Sunday must use their vacation time to take a day off. Vacation Time
Hours are counted toward Weekly Overtime Hours and as such the Vacation
Time Other Activity Type is set to count as regular hours. However, XYZ
Company only pays Sunday Day Of Week Overtime on worked hours. Benefits
such as Vacation Time are paid at base rate. The screenshots below show
how Exclude from Day Of Week Overtime can be used to properly exclude
Vacation Time from Day of Week Overtime.

Related Settings:

OT1 = Daily > 8 Hours

Sunday Day of Week Regular
Hours -> OT2

Sunday Day of Week OT1
Hours -> OT2

Exclude From Day Of Week
Overtime Unchecked:

![](/img/EmployeeProfile_028.png)

With 'Exclude From Day of Week Overtime'
unchecked, hours for an other activity type set to Count as Regular Hours
are subject to Day of Week Overtime Rules. Notice how all hours are posted
to Overtime 2 in accordance with Sunday Day of Week Overtime settings.
The Configuration for the Shift Change Other Activity Type in this scenario
is shown below.

![](/img/JobCosting_Config_18.gif)

Exclude From Day of Week
Overtime Checked:

![](/img/hs6.gif)

With 'Exclude From Day of Week Overtime'
unchecked, hours for an other activity type set to Count as Regular Hours
are excluded from Day of Week Overtime Rules. Notice how all hours for
the Shift Change Other Activity Type are paid as Regular Hours even though
they fall on a Sunday. The Configuration for the Shift Change Other Activity
Type in this scenario is shown below.

![](/img/Ch2_QA_Group.jpg)

Exclude
From Unscheduled Overtime - If
this option is checked, Hours for the respective Other Activity Type will
not count toward Unscheduled Overtime. 'Exclude from Unscheduled Overtime'
is only available for Other Activity Types with 'Count as Regular Hours'
or 'Only Count as Regular Hours if Scheduled' checked. For organizations
who track Unscheduled Hours via Unscheduled Hours Mapping settings on
the Schedule Settings / Rules Section of the Policy it is common for most
Other Activity Types, especially Other Activity Types for Paid Time Off
such as Vacation Time or Holiday Pay, to be excluded from Unscheduled
Overtime.

Example: Company XYZ Excludes Holiday Pay
from Unscheduled Overtime. If a Company Observed Holiday Date falls on
a day the employee is not scheduled to work, XYZ Company pays the employee
their base rate for the day. Employees not scheduled to work on a Holiday
Date do not receive Unscheduled Overtime.

Related Settings:

OT1 = Daily > 8 Hours

Unscheduled Regular
Hours -> OT2

Unscheduled OT1 Hours
-> OT2

Exclude From Unscheduled
Overtime Unchecked:

![](/img/OTA_15.png)

With 'Exclude From Unscheduled Overtime'
unchecked, hours for an other activity type set to Count as Regular Hours
are subject to Unscheduled Hours Mapping. Notice how all hours are posted
to Overtime 2 in accordance with Unscheduled Hours Mapping settings. The
Configuration for the Shift Change Other Activity Type in this scenario
is shown below.

![](/img/clip_image020.jpg)

Exclude From Unscheduled
Overtime Checked:

![](/img/JobCosting_Config_15.gif)

With 'Exclude From Unscheduled Overtime'
checked, hours for an other activity type set to Count as Regular Hours
are excluded from Unscheduled Hours Mapping. Notice how all hours for
Shift Change are paid as regular hours even though the employee does not
have a schedule on 7/28/2013. The Configuration for the Shift Change Other
Activity Type in this scenario is shown below.

![](/img/EmployeeProfile_035.png)

Exclude
From Daily Overtime -  If
this option is checked, Hours for the respective Other Activity Type will
not count toward Daily Overtime. 'Exclude from Daily Overtime' is only
available for Other Activity Types with 'Count as Regular Hours' or 'Only
Count as Regular Hours if Scheduled' checked.

Example: Company XYZ counts Jury Duty Hours
toward Weekly Overtime but excludes Jury Duty Hours from Daily Overtime.
If an employee is out of the office for Jury Duty, and they report to
work on the same day for a different shift, the employee will not be eligible
for Overtime Unless they work more than 8 hours on the respective date
or if they have worked in excess of 40 Hours for the work week.

Related Settings:

OT1 = Daily > 8 Hours,
Weekly > 40 Hours

Deduct Daily OT From
Weekly OT = Checked

Exclude From Daily Overtime
Unchecked:

![](/img/hs11.gif)

With 'Exclude From Unscheduled Overtime'
unchecked, hours for an other activity type set to Count as Regular Hours
are subject to Daily Overtime Rules. Notice how worked hours from 4:00
PM to 8:00 PM on 7/29/13 are counted toward OT1. The Configuration for
the Jury Duty Other Activity Type in this scenario is shown below.

![](/img/OTA_11.png)

Exclude From Unscheduled
Overtime Checked:

![](/img/Department-Update-Form_Prem.gif)

With 'Exclude From Unscheduled Overtime'
checked, hours for an other activity type set to Count as Regular Hours
are excluded from Daily Overtime Rules. Notice how worked hours on 7/29/13
from 4:00 PM to 8:00 PM resulting in a total of 12 Regular Hours on 7/29/2013.
The employee then does not qualify for Overtime Hours until they work
beyond the 40 Hours in the Work Week on 8/2/13. The Configuration for
the Shift Change Other Activity Type in this scenario is shown below.

![](/img/hol32.png)

Exclude
From Payroll Export â Placing a check in this box will allow
the other activity to be excluded from the payroll export. This option
should be checked for any Other Activity Types which are intended for
use within the Time and Attendance System for tracking purposes only.
Other Activity Records on Employee Timecards for Other Activity Types
with this option checked will not be exported by the Payroll Export, though
they will be displayed on reports within InfiniTime.

Inactive
â Placing a check in this box will make the respective Other Activity
Type Inactive. The respective Other Activity Type will no longer be available
for selection when inserting an Other Activity via Quick Punch, Time Off
Requests, or from Hardware Terminals such as the Thor.

### Hours Mapping Tab

The Hours Mapping Tab of the Other Activity
Update Form is only displayed if 'Count as Regular Hours' or 'Only Count
as Regular Hours if Scheduled' are checked for an Other Activity Type.
Hours Mapping permits employee hours worked in a given hours type to be
mapped to a different hours type based on specific conditions such as:

- Scheduled Hours worked on a specific Department
- Scheduled Hours worked on a specific Job
- Scheduled Hours worked on a specific Task
- Scheduled Hours worked on a specific Other Activity Type
- Unscheduled Hours worked on a specific Department
- Unscheduled Hours worked on a specific Job
- Unscheduled Hours worked on a specific Task
- Unscheduled Hours worked on a specific Other Activity Type

![](/img/OTA_25.png)

The Hours Mapping Tab of the Other Activity Update Form defines Hours
Mapping settings for the respective Other Activity Type. Hours mapping
settings configured for an Other Activity Type will be applied to scheduled
and unscheduled hours for the respective Other Activity Type. Hours Mapping
is considered an advanced feature and is only required by approximately
30% of production InfiniTime
Installations. Organizations with Labor Unions and specific hours costing
or pay premium rules for scheduled vs unscheduled hours often find Hours
Mapping to be required. Additional details on configuring and utilizing
Hours Mapping can be found in the Hours Mapping Section
of this document.

### Other Activity Types - Usage

Other Activity Types are a highly versatile part of the InfiniTime Time and Attendance application.
Other Activity Types can be configured to meet time and attendance and
Human Resources policies for companies ranging in size with tens of employees
and basic Time and Attendance Requirements to companies with thousands
of employees and complex Union Based Labor Contracts. To meet the diverse
needs of both small business and enterprise customers, InfiniTime offers [several
methods for entering Other Hours and / or Dollar Amounts for specific
Other Activity Types](Product_Configuration.md#ota30_Method_Of_Entry). Additionally, Other Activity Types can be configured
to track a variety of Hours and Earnings Types for specific [usage purposes](Product_Configuration.md#ota31_Usage_Purposes).

### Method Of Entry

Other Activity Types are used within InfiniTime
to track Hours and Earnings Types which such as Paid Leave, Unpaid Leave,
Commissions, Bonuses, and Tips. With this in mind, inserting hours and
/ or Dollars for specific Other Activity Types as appropriate to show
the benefits used and / or earned by an employee is an integral part of
the recurring Employee Timecard Review and Editing process. Other Hours
and Other Amount entries can be inserted in multiple ways as outlined
in the table below.

| Method of Entry                                                             | Overview                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| --------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Manually via Quick Punch                                                    | Other Activity Hours and / or Dollar Amounts can be entered manually using the Quick Punch Feature from the Company Timecard or Employee Timecard. This method is commonly used to insert hours for Other Activity Types whose occurrence cannot be anticipated such as Sick Time or Personal Time.                                                                                                                                                                                                                                                                                                                                                      |
| Manually via Approval of a Time Off Request                                 | Other Activity Hours are inserted by InfiniTime upon approval of a Time Off Request sent by an employee. This feature is regularly used by organizations who do one or more of the following: _ Schedule Vacation Time in advance _ Use Find Available for Scheduling Purposes _ Use Schedule Skeletons for Scheduling Purposes _ Use GANNT Chart Scheduling                                                                                                                                                                                                                                                                                             |
| Manually via Function Keys at a Hardware Terminal (IE: Thor, Zephyr, Scout) | Other Activity Hours and / or Dollar Amounts can be entered manually via Function Keys at Hardware Terminals configured to communicate with the InfiniTime Software. This provides a convenient interface for entering Other Activity Hours immediately while at the Job Site and / or Work Area without accessing the InfiniTime Manager Module.                                                                                                                                                                                                                                                                                                        |
| Manually via Telephone Punch Menu Prompts using Telephone Punch             | Other Activity Hours and / or Dollar Amounts can be entered manually via Telephone Punch Menu Prompts by calling into the Telephone Punch Menu and selecting the appropriate menu options. This provides a convenient interface for entering Other Activity Hours and / or Dollars immediately while in the field without accessing the InfiniTime Manager Module. InfiniTime Telephone Punch is ideal for organizations with a high transaction volume. (IE: Thousands of Employees Punching multiple times per day over a wide geographic area).                                                                                                       |
| Automatically via Holiday Dates for a Non-Working Holiday                   | InfiniTime Holiday Types permit specific Dates to be defined as Holidays. InfiniTime can then automatically insert Other Activity Hours, such as 'Holiday Time', for employees eligible for Paid Holidays.                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Automatically via Holiday Dates for a Working Holiday                       | InfiniTime Holiday Types permit specific Dates to be defined as Holidays. For organizations with employees who receive different pay rates for working on a Holiday Date, InfiniTime can be configured to automatically separate and track hours paid at different rates for eligible employees through use of one or more of the following features as appropriate based on your organization's rules: _ Working vs Non Working Holiday Benefits _ Other Activity Options: Count As Regular Hours _ Other Activity Options: Only Count as Regular Hours if Scheduled _ Holiday Hours Mapping _ Unscheduled Hours Mapping _ Other Activity Hours Mapping |
| Automatically via Stand By Time                                             | Stand by time is intended for use with on call employees. When Stand By Time is configured on a given policy, Other Hours are automatically inserted for a specific Other Activity Type for each Day Of Week configured for Stand By Time for all employees assigned to the policy.                                                                                                                                                                                                                                                                                                                                                                      |

### Usage Purposes

InfiniTime permits entry
of both positive and negative values for Other Activity Types making it
possible to enter adjustments to specific Hours and Earning Types. Specific
purposes for Other Activity Types and common uses for each are listed
below.

| Usage Purpose                                | Example(s)                                                                                                                        |
| -------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| Add Other Hours to be Paid to Employees      | Add Jury Duty Hours                                                                                                               |
| Adjust Other Hours to be Paid to Employees   | Negate System Holiday Record                                                                                                      |
| Add Other Amounts to be Paid to Employees    | Add additional pretax earnings such as Sales Commission to an employee's timecard                                                 |
| Adjust Other Amounts to be Paid to Employees | Subtract additional pretax earnings such as Sales Commissions from an employee's timecard                                         |
| Add Taxable Earnings                         | Add Tips to an Employee's Timecard                                                                                                |
| Adjust Taxable Earnings                      | Subtract Tips from an Employee's Timecard                                                                                         |
| Add to Units Tracked                         | Add Piece Counts to an Employee's Timecard                                                                                        |
| Adjust Units Tracked                         | Subtract Piece Counts from an Employee's Timecard                                                                                 |
| Deduct Used Benefits from an Accrual Type    | Deduct Other Hours inserted for One or More Other Activity Types from an employee's Available Accrued Balance for an Accrual Type |

### Usage Purpose Examples

Other Hours

Other Hours are inserted for Other Activity
Types to track hours for various categories of Paid and Unpaid Leave.
Several examples of common types of Paid and Unpaid Leave tracked by InfiniTime Customers are provided
below.

| Vacation Time   | Sick Time       | Personal Time |
| --------------- | --------------- | ------------- |
| Jury Duty       | Bereavement     | Marriage      |
| Maternity Leave | Paternity Leave | Family Leave  |

Adding
Other Hours to be paid to an employee with a Positive Entry

1. Ensure an Other Activity
   Type exists for each type of Other Hours tracked by your organization.

2. Other Activity Options,
   as outlined above, must be configured for each Other Activity Type as
   appropriate based on your organization's Time and Attendance & HR
   Rules.For Other Hours, the Other Activity Type must be set to the Hours
   Type as shown below.

![](/img/Ch2_QA_DefSched.jpg)

3. Open the Company
   Timecard Table

4. Search for the employee
   you wish to insert Other Hours for.

5. Set the Date Range
   to include the date(s) you wish to insert Other Hours For.

6. Click on Quick Punch.

7. Set the Type to Other
   Activity.

8. Specify the previously
   created Other Activity Type for which you wish to insert Other Hours by
   typing the first several characters of the Other Activity Type's description
   or use the Lookup Button.

9. Enter the desired
   number of Other Activity Hours. Be sure to enter a positive value without
   a minus (-) sign. InfiniTime
   permits values of -24.00 Hours to 24.00 Hours to be inserted for Other
   Activity Types of the Hours Type.

10. Click OK. The example
    below shows 8.00 Jury Duty Hours to be paid to an employee.

![](/img/sched7.gif)

Adjusting
Other Hours with a Negative Entry using the Same Other Activity Type

1. Ensure an Other Activity Type exists for each type of Other Hours tracked
   by your organization.

2. Other Activity Options,
   as outlined above, must be configured for each Other Activity Type as
   appropriate based on your organization's Time and Attendance & HR
   Rules. For Other Hours, the Other Activity Type must be set to the Hours
   Type as shown below.

![](/img/hol23.png)

3. Open the Company
   Timecard Table

4. Search for the employee
   you wish to Adjust Other Hours for.

5. Set the Date Range
   to include the date(s) you wish to Adjust Other Hours For.

6. Click on Quick Punch.

7. Set the Type to Other
   Activity.

8. Select the previously
   created Other Activity Type for which you wish to adjust Other Hours by
   typing the first several characters of the Other Activity Type's description
   or use the Lookup Button.

9. Enter the desired
   number of Other Activity Hours. Enter a negative value with a minus (-)
   sign.

10. Click OK. The example
    below shows a Negative Other Activity Entry used to offset an overpayment
    of an Other Activity Type from a prior period. The negative value on 8/5/13
    will be transferred to payroll and deducted from the employee's final
    gross pay.

![](/img/DeptPremium_Rate.gif)

Adjusting
Other Hours with a Negative Entry using a Different Other Activity Type

1. This method for adjusting
   Other Hours is specifically required to adjust a System Holiday Record
   created by InfiniTime for
   a Holiday Date, though it may also be used to adjust hours in other scenarios
   if desired. By creating a separate Other Activity Type for Adjustment
   Purposes Administrators can run reports with the Deduct Other Activity
   Type tagged to see only Adjustment Entries.

2. Create a second Other Activity Type with the same options, Payroll Mapping
   Number, and Payroll Mapping Codes as the original Other Activity Type
   you wish to adjust. For clarity, the Description of the new other Activity
   Type should be unique and should include 'Adjust' or 'Deduct' to clearly
   show the Other Activity Type is intended for adjustment purposes.

3. Open the Company
   Timecard Table

4. Search for the employee
   you wish to Adjust Other Hours for.

5. Set the Date Range
   to include the date(s) you wish to Adjust Other Hours For.

6. Click on Quick Punch.

7. Set the Type to Other
   Activity.

8. Select the previously
   created Other Activity Type by typing the first several characters of
   the Other Activity Type's description or use the Lookup Button.

9. Enter the desired
   number of Other Activity Hours. Enter a negative value with a minus (-)
   sign.

10. Click OK. The example
    below shows a Negative Other Activity Entry used to negate a system holiday
    record.

![](/img/clip_image016.jpg)

Other Amounts

Other Amounts are inserted for Other Activity Types to track payable
currency amounts for various categories of earnings. Several
examples of common types of earnings tracked by InfiniTime
Customers are provided below.

| Sales Commissions      | Misc. Earnings |
| ---------------------- | -------------- |
| Expense Reimbursements |                |

Adding Other Amounts

1.  Ensure an Other Activity Type exists for each Other Amount // Earnings
    Type tracked by your organization.

2.  Other Activity Options, as outlined above, must be configured for each
    Other Activity Type as appropriate based on your organization's Time and
    Attendance & HR Rules. For Other Amounts, the Other Activity Type
    must be set to the Amount Type as shown below.

![](/img/JobCosting_Config_4.gif)

3.  Open the Company Timecard Table

4.  Search for the employee you wish to insert an Other Amount for.

5.  Set the Date Range to include the date(s) you wish to insert an Other
    Amount For.

6.  Click on Quick Punch.

7.  Set the Type to Other Activity.

8.  Select the previously created Other Activity Type for which you wish to
    insert an Other Amount by typing the first several characters of the Other
    Activity Type's description or use the Lookup Button.

9.  Enter the desired Other Amount Value to be paid to employees. This value
    may be entered in any currency, with up to two decimal places. For clarity,
    It is recommended that the same currency be used for all Other Amount
    entries within InfiniTime.
    Be sure to enter a positive value without a minus (-) sign.

10. Click OK. The example below shows a currency amount of 257.89 in Sales
    Commissions paid to an employee. Any currency can be used with InfiniTime Other Amounts, though it
    is recommended that all Other Amounts be tracked in the same currency.
    InfiniTime does not perform
    any currency conversions - Other Amount values are exported to payroll
    and displayed on reports within InfiniTime
    exactly as they are entered.

![](/img/21DHOLAVG.jpg)

Adjusting Other Amounts

1.  Ensure an Other Activity Type exists for each type of Other Hours tracked
    by your organization.

2.  Other Activity Options, as outlined above, must be configured for each
    Other Activity Type as appropriate based on your organization's Time and
    Attendance & HR Rules. For Other Amounts, the Other Activity Type
    must be set to the Amount Type as shown below.

![](/img/OTA_18.png)

3.  Open the Company Timecard Table

4.  Search for the employee you wish to insert Other Hours for.

5.  Set the Date Range to include the date(s) you wish to insert Other Hours
    For.

6.  Click on Quick Punch.

7.  Set the Type to Other Activity.

8.  Select the previously created Other Activity Type for which you wish to
    insert an Other Amount by typing the first several characters of the Other
    Activity Type's description or use the Lookup Button.

9.  Enter the desired number of Other Activity Hours. Be sure to enter a positive
    value without a minus (-) sign. InfiniTime
    supports Other Amount entries of -99999.99 to 99999.99

10. Click OK. The example below shows a Negative Other Activity Entry used
    to offset an overpayment of an Other Amount from a prior period. The negative
    value on 8/5/13 will be transferred to payroll and deducted from the employee's
    final gross pay.

![](/img/OTA_11.png)

Taxable
Earnings

Taxable Earnings, or amounts received by employees but not paid directly
by the employer such as Tips or Employee Meals, can be tracked using Other
Activity Types of the Amount Type. Once entered, Taxable Earnings can
be transferred to payroll for tracking purposes.

| Tips | Meals |
| ---- | ----- |

Adding
Taxable Earnings

1. Ensure
   an Other Activity Type exists for each Taxable Earning tracked by your
   organization.

2. Other Activity Options, as outlined above, must be configured for each
   Other Activity Type as appropriate based on your organization's Time and
   Attendance & HR Rules. For Taxable Earnings, the Other Activity Type
   must be set to the Amount Type as shown below.

![](/img/sched9.gif)

3.  Open the Company Timecard Table

4.  Search for the employee you wish to insert a Taxable Earning for.

5.  Set the Date Range to include the date(s) you wish to insert a Taxable
    Earning For.

6.  Click on Quick Punch.

7.  Set the Type to Other Activity.

8.  Select the previously created Other Activity Type for which you wish to
    insert Taxable Earnings by typing the first several characters of the
    Other Activity Type's description or use the Lookup Button.

9.  Enter the desired Taxable Earning amount received by the employee in the
    Other Amount Field. This value may be entered in any currency, with up
    to two decimal places. For clarity, it is recommended that the same currency
    be used for all Other Amount entries within InfiniTime.
    Be sure to enter a positive value without a minus (-) sign.

10. Click OK. The example below shows a currency amount of 257.89 in Tips
    received by an employee. Any currency can be used with InfiniTime Taxable Earnings, though
    it is recommended that all Other Amounts be tracked in the same currency.
    InfiniTime does not perform
    any currency conversions - Taxable Earning values are exported to payroll
    and displayed on reports within InfiniTime
    exactly as they are entered.

![](/img/TaskPrem_3.gif)

Adjusting
Taxable Earnings

1.  Ensure an Other Activity Type exists for each type of Other Hours tracked
    by your organization.

2.  Other Activity Options, as outlined above, must be configured for each
    Other Activity Type as appropriate based on your organization's Time and
    Attendance & HR Rules. For Other Amounts, the Other Activity Type
    must be set to the Amount Type as shown below.

![](/img/Shift_Diferential_Tab.gif)

3.  Open the Company Timecard Table

4.  Search for the employee you wish to insert Other Hours for.

5.  Set the Date Range to include the date(s) you wish to insert Other Hours
    For.

6.  Click on Quick Punch.

7.  Set the Type to Other Activity.

8.  Select the previously created Other Activity Type for which you wish to
    insert Other Hours by typing the first several characters of the Other
    Activity Type's description or use the Lookup Button.

9.  Enter the desired number of Other Activity Hours. Be sure to enter a positive
    value without a minus (-) sign. InfiniTime
    supports Other Amount entries of -99999.99 to 99999.99

10. Click OK. The example below shows a Negative Other Activity Entry used
    to offset an overpayment of a Taxable Earning from a prior pay period.
    The negative value on 8/5/13 will be transferred to payroll and deducted
    from the employee's final gross pay.

![](/img/hs11.gif)

Units Tracked

Units, or the number of times a significant task or action is completed
such as Piece Count, can be tracked using Other Activity Types of the
Amount Type. When inserting the Other Activity Entry, simply enter a whole
number value to show the number of times the respective task or action
was completed for a given date. In this way, the total number of times
the task or action was completed will be transferred to payroll where
the Total Piece Count can be used to calculate a Piece rate, or a per
unit premium can be paid to the employee at a set currency amount per
unit.

| Piece Count | Per Unit Premiums Paid at a Flat Dollar Amount for each Unit (IE: A Per Client Premium for Diving Instructors Leading a Night Dive) |
| ----------- | ----------------------------------------------------------------------------------------------------------------------------------- |

Adding
Units Tracked

1. Ensure
   an Other Activity Type exists for each Per Unit Premium or Piece Count
   Type tracked by your organization.

2. Other Activity Options, as outlined above, must be configured for each
   Other Activity Type as appropriate based on your organization's Time and
   Attendance & HR Rules. For Per Unit Premiums and Piece Counts, the
   Other Activity Type must be set to the Amount Type as shown below.

![](/img/OTA_27.png)

3.  Open the Company Timecard Table

4.  Search for the employee you wish to insert a Taxable Earning for.

5.  Set the Date Range to include the date(s) you wish to insert a Per Unit
    Entry For.

6.  Click on Quick Punch.

7.  Set the Type to Other Activity.

8.  Select the previously created Other Activity Type for which you wish to
    insert a Per Unit Entry by typing the first several characters of the
    Other Activity Type's description or use the Lookup Button.

9.  Enter the number of times the respective action or task was completed
    for the date(s) specified in the Other Amount Field. Be sure to enter
    a positive value without a minus (-) sign. Whole numbers are recommended
    for use with Per Unit Entries.

10. Click OK. The example below shows a Per Unit Entry of 8 Night Diving Passengers
    led on a Night Dive by a Diving Instructor. In this instance, the customer's
    payroll application is configured to pay employees an additional premium
    of $8.38 per night dive passenger.

![](/img/OTA_18.png)

Adjusting
Units Tracked

1. Ensure
   an Other Activity Type exists for each Per Unit Premium or Piece Count
   Type tracked by your organization.

2. Other Activity Options, as outlined above, must be configured for each
   Other Activity Type as appropriate based on your organization's Time and
   Attendance & HR Rules. For Per Unit Premiums and Piece Counts, the
   Other Activity Type must be set to the Amount Type as shown below.

![](/img/DeptPremium_Amt.gif)

3.  Open the Company Timecard Table

4.  Search for the employee you wish to insert a Taxable Earning for.

5.  Set the Date Range to include the date(s) you wish to insert a Per Unit
    Entry For.

6.  Click on Quick Punch.

7.  Set the Type to Other Activity.

8.  Select the previously created Other Activity Type for which you wish to
    insert a Per Unit Entry by typing the first several characters of the
    Other Activity Type's description or use the Lookup Button.

9.  Enter the number of times the respective action or task was completed
    for the date(s) specified in the Other Amount Field. Be sure to enter
    a positive value without a minus (-) sign. Whole numbers are recommended
    for use with Per Unit Entries.

10. Click OK. The example below shows a negative Per Unit Entry used to offset
    an overpayment of a Per Unit Entry from a prior pay period.
    The negative value on 8/8/13 will be transferred to payroll and deducted
    from the employee's final gross pay.

![](/img/JobCostingWages_3.gif)

Deduct
Used Benefits from AccrualBalances

As part of the InfiniTime
Accruals functionality, Other Hours can be deducted from specific Accrual
Buckets when hours are inserted for employees. Supervisors, Payroll Clerks,
and InfiniTime Administrators
may then run reports to show the exact dates employee's accrued hours
in addition to the exact dates employee's used hours along with the final
available balance. Additional details can be found regarding configuring
Other Activity Types that Deduct in the Accrual Overview Section of this
document. Related topics are provided below.

| Vacation Time | Sick Time  |
| ------------- | ---------- |
| Personal Time | Comp. Time |

Related Topics:

[Accruals
Introduction](Accrual_Configuration.md#acc01_Employee_Accruals_Introduction)

[Basic
Accruals Module Overview](Accrual_Configuration.md#acc02_Employee_Accruals___Basic_Accruals_Overview)

[Accruals
Plus Module Overview](Accrual_Configuration.md#acc26_Employee_Accruals_-_Accruals_Plus_Module_Overview)

[Other
Activities That Deduct Tab](Accrual_Configuration.md#acc25_Other_Activities_that_Deduct_Tab)

---

---

---

# Default Schedule Tab

The Default Schedule Tab can be used to configure
the Default Schedule for multiple employees at a time. This is especially
useful when multiple employees in different departments have the same
schedule. Simply use the Employee Filter to specify the employees whose
Default Schedule will be updated and use the Quick Schedule button to
define a schedule. Clicking OK will assign the specified schedule to all
employees designated by the Employee Filter.

![](/img/DeptPrem_EX_2.gif)

Group
Tab

The Group Tab can be used to configure
Groups for multiple employees at a time. Simply use the Employee Filter
to specify the employees whose Groups will be updated and use the Change
button to select a group from each group level. Clicking OK will assign
the specified schedule to all employees designated by the Employee Filter.
Refer to Chapter 5 Employee Setup -
Employee Update Form - Groups for more information on the use and configuration
of groups.

![](/img/JobCosting_Config_19.gif)

Note: A group description must be specified in
order for the group assigned to the employee to be altered.

For Example:

The image below shows
a blank group description. In this case, a group description has not yet
been specified.

![](/img/JobCostingWages_2.gif)

The Image below shows
a filled group description. In this case, a group description has been
specified and the Phoenix group will be assigned to all employees specified
by the Employee Filter.

![](/img/OTA_4.png)
