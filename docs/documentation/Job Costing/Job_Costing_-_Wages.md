---
title: "Job Costing - Wages"
description: "Overview of how wages are allocated and matched in InfiniTime for accurate job costing, including wage hierarchy and matching process."
---

# Job Costing - Wages

It is not uncommon for employee wages to vary based upon the task, job, or department, where employees are working. Wages within InfiniTime can be allocated to a specific Job, Task, Department, or any combination thereof. This makes it possible to calculate gross totals based upon which Department, Job, or Task employees are working in. When using wages with Job Costing it is important to understand how InfiniTime identifies which wage to use for an employee. Infinitime searches wage records for an employee attempting to match items between the wage record and where the employee is actively working according to the wage hierarchy below. Employees will be paid using the wage corresponding to the first match.

Wage Hierarchy

1.) Department, Job, and Task

2.) Department, Job

3.) Department, Task

4.) Job, Task

5.) Department

6.) Job

7.) Task

For example if an employee worked in the West Coast Marina Department, Job Number 117852, and the Painting Task InfiniTime would first search for a wage record matching all three items - West Coast Marina, 117852, and Painting. If a record was not found for this combination the software would search for a wage record matching Department and Job which in this example is West Coast Marina and 117852. If a wage record was not found for this combination the software would continue down the wage hierarchy searching for a matching wage record. If no match is found the employee's default wage is used.

Wage Configuration

Configuring a Wage for a specific combination of three items

A wage associated with a specific combination of Department, Job, and Task will take precedence over all other wages. For example if wages are configured as shown below the employee will receive the wage associated with the exact Department, Job, and Task combination worked by the employee rather than the wage associated with the Task the employee is working in. Referring to the Wage Hierarchy this occurs because InfiniTime will match a wage associated with Department, Job, and Task before a wage associated with just the Task. Additional examples are below. The highlighted wage record is the wage the employee will be paid.

Example 1

| Working Department (Customer) | Working Job (Job Number) | Working Task (Task) |
| ----------------------------- | ------------------------ | ------------------- |
| West Coast Marina             | 117852                   | Painting            |

![](/img/JobCostingWages_4.gif)

Example 2

| Working Department (Customer) | Working Job (Job Number) | Working Task (Task) |
| ----------------------------- | ------------------------ | ------------------- |
| West Coast Marina             | 117852                   | Painting            |

![](/img/JobCostingWages_1.gif)

The above examples illustrate how employees will receive the wage assocaited with the particular Department, Job, and Task they are working on even if another wage is defined for each individual item or a combination thereof.

Configuring a Wage for a specific combination of two items

A wage associated with a specific combination of two items should be used if employees receive a specific wage when working under two items such as a specific Department and Task or a specific Job and Task. For example if an employee receives  $8 when working in the West Coast Marina Department and performing the Painting Task regardless of what Job they are working on a wage should be created and associated with the West Coast Marina Department and Painting Task as shown below.  It is important to keep the Wage Hierarchy in mind when associating a wage with a combination of two items. In example 2 the employee would be paid $8 per hour rather than $10 because a wage matching the exact working Department, Job, and Task is present. This will be matched before the combination of Department and Task.

Example 1

| Working Department (Customer) | Working Job (Job Number) | Working Task (Task) |
| ----------------------------- | ------------------------ | ------------------- |
| West Coast Marina             | 117852                   | Painting            |

![](/img/JobCostingWages_5.gif)

Example 2

| Working Department (Customer) | Working Job (Job Number) | Working Task (Task) |
| ----------------------------- | ------------------------ | ------------------- |
| West Coast Marina             | 117876                   | Painting            |

![](/img/JobCostingWages_2.gif)

The above examples illustrate how the employee will receive the wage associated with their particular Task and Department regardless of what job they are working on unless a wage record exists that matches the Department, Job, and Task worked by the employee.

Configuring a Wage for a specific item

Wages should be configured for a specific item such as a Department, Job, or Task when employees have a set wage for the item. For example, if an employee was paid $10 per hour when painting regardless of what job or department he was painting under a wage should be created and associated with the Painting task only as shown below. In this way it would not matter what department or job the employee was working under as long as he was performing the painting task he would receive $10 per hour. It is important to keep the Wage Hierarchy in mind when associating a wage with a single item. In example 2 the employee would be paid $8 per hour rather than $10 because a wage matching the exact working Department, Job, and Task is present.

Example 1

| Working Department (Customer) | Working Job (Job Number) | Working Task (Task) |
| ----------------------------- | ------------------------ | ------------------- |
| Ahbor Harbor                  | 117852                   | Painting            |

![](/img/JobCostingWages_3.gif)

In the example above even though there is a wage record for each item where the employee is working the Department record takes precedence as it is matched first due to the Wage Hierarchy.

Example 2

| Working Department (Customer) | Working Job (Job Number) | Working Task (Task) |
| ----------------------------- | ------------------------ | ------------------- |
| West Coast Marina             | 117876                   | Painting            |

![](/img/JobCostingWages_2.gif)

The above examples illustrate how the employee will receive the wage associated with a single item unless a different record is matched due to the Wage Hierarchy as in Example 2.
