---
title: ""
description: ""
---

### Departments Tab - Introduction

![](/img/SoftwareOverview_027.png)

The Departments Tab of the Policy Update Form displays a list of all
Departments configured in the software. Departments are used to separate
employee hours performed under different disciplines and / or types of
activity. Employees can punch into and out of departments in order to
track hours worked under separate departments such as Programming, Technical
Support, or Shipping or separate tasks such as Welding, Painting, or Finish
Work. Initially, it is important to understand the following concepts
regarding InfiniTime Departments
and Job Costing:

- InfiniTime includes
  four default departments as shown in the image above. If desired these
  departments can be removed. It should be noted that InfiniTime will only permit a department
  to be deleted if the department 1.)  Is not assigned to any employees.
  2.) Is not assigned to any timecard records.
- The default department is highlighted blue in the department table.
  When a new employee is inserted they are automatically assigned the
  default department.
- There is no limit to the number of departments that can be inserted
  into the software.
- Job Costing permits customers to track employee hours under various
  levels. Job costing is generally utilized in organizations where employee
  labor costs are of special interest when compared to the cost of finished
  goods such as manufacturing related organizations or where hours are
  billable to clients. An example Job Costing Configuration, using only
  InfiniTime Departments
  is shown below for a Construction Company. Additional details on job
  costing and configuration can be found in the [Job
  Costing Section](Configuration/Product_Configuration.md#cnf01_Job_Costing_Introduction) of this document.

| Department   | Job                 | Task    |
| ------------ | ------------------- | ------- |
| Construction | Philly Mae Pizzeria | Framing |

When using job costing it is important to
identify the lowest level. In the above example Task is the lowest level.
To perform job costing using only Departments within InfiniTime
for ABC Construction Company, one department would be required for each
distinct Department, Job, and Task combination.. Department numbers can
be broken into sections with a specific number of digits for each level
in order to represent all departments, jobs, and tasks in a clear fashion.
The employee can then punch in and out of tasks using the department number.
Care must be taken when designing the numbering scheme in order to avoid
limiting the possible combinations and providing for future growth. An
example is shown below.

| InfiniTime Department Name | Department Number   |
| -------------------------- | ------------------- | ----------- | ---------- |
| Construction               | Philly Mae Pizzeria | Framing     | 1010000101 |
| Construction               | Philly Mae Pizzeria | Drywall     | 1010000102 |
| Electrical                 | Philly Mae Pizzeria | Wiring      | 2010000210 |
| Electrical                 | Philly Mae Pizzeria | Engineering | 2010000211 |

Technical Note: The Job Costing Scenario above
uses only 1 Job Costing Level (Departments) within InfiniTime.
InfiniTime supports up
to three Job Costing Levels. The scenario above could also be handled
by configuring Departments, Jobs, and Tasks within the InfiniTime Software. One Department
within InfiniTime would
need be configured for each Department tracked by ABC Construction Company.
One Job would need be configured within InfiniTime
for each Client / Work Order serviced by ABC Construction. One Task would
need to be configured for each low level task performed by ABC Construction
employees. Refer to the Job Costing Section of this document for additional
details. The exact configuration required for a given organization depends
upon the requirements of the customer's Payroll Application for importing
Employee Hours and Earnings.

### Department Update Form - Introduction

![](/img/SoftwareOverview_001_Btn1_Company.png)

The Department Update Form is used to create new Departments within
the InfiniTime Software
and can be accessed from the Departments Tab of the Company Update Form
by clicking on Insert or by selecting an existing department and clicking
on change. Initially, it is important to understand the following concepts
relating to Department Configuration. Keep these in mind when preparing
a list of your organization's departments for use during software configuration.

- The Department Name and Department Number are unique fields. Multiple
  departments cannot share the same department name or number.
- Department Cost Center - The cost center is used as a payroll identifier,
  providing the ability to match departments within InfiniTime to Hours
  Categories such as Tasks, Jobs, Classes, and/or Activities within
  a 3rd Party Payroll Application. Departments are generally identified
  by either a General Ledger Account number or an Alphanumeric Code
  within a payroll application. The Department Cost Center must be configured
  for customers who wish to track how employee hours are distributed
  between departments in their payroll application.
- The Default Schedule Tab of the Department Update Form is one
  method for defining employee schedules. Department schedules effect
  all employees assigned to the specific department. This scheduling
  method is most useful if the majority of employees within a department
  work the same schedule. Additional information can be found within
  [the Scheduling Section](Scheduling/Scheduling.md#sch05_Scheduling_By_Department)
  of this document.
- The Premium Pay Tab of
  the Department Update Form can be used to configure a specific wage
  for different Hours Types (IE: Regular Hours, Overtime Hours, etc.)
  worked in the respective Department. Additional information can be
  found within [the Pay Premiums
  Section](Configuration/Product_Configuration.md#pp01_Pay_Premiums_Introduction) of this document.
- The Hours Mapping Tab of the Department Update Form can be used
  to direct specific hours types worked in the respective Department
  to a different Hours Type. This feature is often utilized for Payroll
  Export purposes to separate hours that are paid at different rates.
  Additional information can be found within [the
  Hours Mapping Section](Configuration/Product_Configuration.md#hm1_Hours_Mapping) of this Document.
