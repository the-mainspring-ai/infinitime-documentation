---
title: "Job Costing Introduction"
description: "An overview of Job Costing, its benefits, and how it tracks employee hours, departments, jobs, and tasks within an organization."
---

Job Costing Introduction

# Job Costing Introduction

Job Costing makes it possible for the user to track employee hours under various levels. Job Costing is generally used in businesses where employee labor costs are of special interest when compared to the cost of finished goods such as manufacturing or production related organizations. Even though Job Costing adds a great deal of functionality to the InfiniTime Application it is not used by all companies and as such is disabled by default. Job Costing related fields such as Job and Task will not be displayed within the application if Job Costing is disabled.

Job Costing Benefits

In general Job Costing involves the tracking of three types of information - Internal Departments, Job / Customer, and Task as outlined below.

Internal Departments may refer to separate categories of activity within an organization. Tracking Internal Departments with Job Costing makes it possible for an organization to identify how labor costs are distributed throughout various categories within the company.  Example Activity Categories are Administration, Installation, Construction, Electrical etc.

Job / Customer refer to individual Job Numbers or Customer accounts under which specific tasks are performed. Tracking Jobs / Customers with Job Costing makes it possible for an organization to clearly identify all labor related costs for a specific Customer or Job. Jobs / Customers are generally assigned an Invoice or Job Number which can be used within the organization to refer to the Job.

Tasks refer to actions performed by employees under a specific Activity Category or Job / Customer. Tracking Tasks makes it possible for an organization to clearly identify the amount of time generally required to perform a specific task. Once this is understood employees who take exceptionally long to perform a given task are easily identified. Tasks vary based upon the working environment. Example tasks for a Custom Cabinet Shop might include Framing, Sanding, Staining, Painting, and Installation.

Premium Pay can be used to define Premiums, or bonuses in the form of an increased wage, which are paid to employees based upon the Shift, Department, Job, or Task the employee works on. Refer to the [Pay Premium Introduction](Pay_Premium_Introduction.md) for more information.

Job Costing Levels

While there are various benefits for tracking these items they may not be of interest to all companies. Customers may choose to track one, two, or all of these items.

Single Level: If only one of the above information types is of interest to your company Job Costing is not required. Simply configure Departments to represent the appropriate Internal Departments, Jobs / Customers, and Tasks within your organization. It is important to note employee activity can only be associated with one Department at a time.

Two Levels: If two of the above information types are of interest to your company both Departments and Jobs must be configured within the InfiniTime Application. It should be noted that InfiniTime Departments are required. All employee activity will be associated with a department. In a two level system the first level generally corresponds to Internal Departments or Jobs / Customers while the second level corresponds to Jobs. Departments are considered the first Job Costing Level within InfiniTime and should be configured with the appropriate information. For example, if Internal Departments such as Administration, Construction, Installation etc. are to be your first Job Costing Level then these items should be configured as Departments within the InfiniTime System. Alternatively Jobs / Customers may be used as your first Job Costing level. In this case Job Numbers or Customer Names should be configured as Departments within InfiniTime. Jobs are considered the second Job Costing Level within InfiniTime and should be configured with any Tasks that apply to your company such as Welding or Painting.

NOTE: In some scenarios only Jobs / Customers and Tasks or Internal Departments and Tasks are of interest to a specific company. However the company may use two levels of tasks. In this scenario three job costing levels are used for only two items of information. Jobs / Customers or Internal Departments would correspond to Departments within InfiniTime. The first task level would refer to Jobs within InfiniTime and the second task level would refer to Tasks within InfiniTime. The chart below shows an example of this configuration.

| Job / Customer (Configured As InfiniTime Departments) | Task 1 (Configured as InfiniTime Jobs) | Task 2 (Configured as InfiniTime Tasks) |
| ----------------------------------------------------- | -------------------------------------- | --------------------------------------- |
| Invoice 1160072                                       | Installation                           | Old Cabinet Removal                     |
| Invoice 1160072                                       | Installation                           | Hang Wall Cabinets                      |
| Invoice 1160072                                       | Installation                           | Install Base Cabinets                   |

Three Levels: If all three of the above information types are of interest to your company Departments, Jobs, and Tasks must be configured within the InfiniTime Application however the type of information configured within Departments, Jobs, and Tasks differs from company to company. It is important to recognize Departments are required within InfiniTime. All employee activity is associated with a department. For this reason most companies choose to configure Internal Departments as Departments within InfiniTime. Example job costing configurations using Three Levels with Internal Departments, Job / Customers, and Tasks are provided below.

| Internal Department (Configured As InfiniTime Departments) | Customer (Configured as InfiniTime Jobs) | Task (Configured as InfiniTime Tasks) |
| ---------------------------------------------------------- | ---------------------------------------- | ------------------------------------- |
| Frame Construction                                         | Gilbert's Crab Boats                     | Welding                               |
| Hull Construction                                          | Gilbert's Crab Boats                     | Sanding                               |
| Assembly                                                   | Gilbert's Crab Boats                     | Assembly                              |

| Internal Department (Configured As InfiniTime Departments) | Job Number (Configured as InfiniTime Jobs) | Task (Configured as InfiniTime Tasks) |
| Frame Construction | 17251 | Welding |
| Hull Construction | 17251 | Sanding |
| Assembly | 17251 | Assembly |

Three Levels w/ Internal Departments, Customers, & Jobs: In some scenarios Tasks are not of interest while both Customers and individual Jobs must be tracked. With this configuration the first level generally corresponds to Internal Departments while the second and third levels correspond to Customers and Jobs respectively. Remember all activity is associated with a department within InfiniTime. An example of this configuration is shown below.

| Internal Department (Configured As InfiniTime Departments) | Customer (Configured as InfiniTime Jobs) | Job Number (Configured as InfiniTime Tasks) |
| ---------------------------------------------------------- | ---------------------------------------- | ------------------------------------------- |
| Custom Programming                                         | Jan's Software                           | 100235                                      |
| Custom Reports                                             | Wellington School District               | 200257                                      |
| Technical Support                                          | Wellington School District               | 300987                                      |

Three levels w/ Two Levels as Tasks: In some scenarios Customers / Jobs are not of interest while Internal Departments and multiple task levels must be tracked. With this configuration the first level generally corresponds to Internal Department while the second and third levels correspond to tasks. An example of this configuration is shown below.

| Internal Department (Configured As InfiniTime Departments) | Task 1 (Configured InfiniTime Jobs) | Task 2 (Configured as InfiniTime Tasks) |
| ---------------------------------------------------------- | ----------------------------------- | --------------------------------------- |
| Cabinets                                                   | Installation                        | Old Cabinet Removal                     |
| Cabinets                                                   | Installation                        | Hang Wall Cabinets                      |
| Cabinets                                                   | Installation                        | Install Base Cabinets                   |
| Administration                                             | Auditing                            | Taxes                                   |

Ultimately the type of information tracked using Departments, Jobs, and Tasks is up to the user. Simply because they are referred to as 'Departments' or 'Jobs' does not mean they must be used for internal departments and job numbers. When configuring Job Costing users must first identify what types of information will be tracked by job costing. Once the information to be tracked has been identified a hierarchy is generally evident when looking at how the items relate to each other. This hierarchy can then be used to organize the items into three levels. The highest level should be configured as departments within InfiniTime, the next as Jobs, and the last as Tasks. While a maximum of three levels are available it is not necessary to use all three levels. For two level systems InfiniTime Departments correspond to the first Job Costing Level while Jobs correspond to the second Job Costing Level.

Labor Transferring Methods

Three methods are available for transferring between Departments, Jobs, and Tasks depending on the chosen solution for gathering employee activity. Two methods are available for choosing from Departments, Jobs, and Tasks using a hardware terminal. The method used for selecting a specific Department, Job, or Task differs depending on terminal model. A list of the method supported by each terminal is provided below. The first method for selecting Departments, Jobs, and Tasks is a simple list format. All available Departments, Jobs, or Tasks are displayed in a list. Employees can scroll up and down the list using buttons on the reader to select the desired item. The second method for selecting Departments, Jobs, and Tasks is by Item Number. In this case an item refers to a specific Department, Job, or Task. The item number corresponds to the Department Number for Departments, the Job Number for Jobs, and the Task Number for Tasks. When employees press the Labor Switching or Transfer Button they will be prompted to enter the Department Number to select the Department they wish to work under followed by the Job and Task number if applicable. When many items are available Transferring by Item Number is the most efficient transfer method though steps must be taken to ensure it is configured appropriately.

1.) Identify the number of Departments, Jobs, and or Tasks which will be tracked for Job Costing Purposes. This information is invaluable when designing a numbering system for Departments, Tasks and Jobs.

2.) Determine item number length. Item Numbers for Departments and Tasks generally range between 2 and 4 digits while Job numbers range from 4 to 8 digits. The number of Departments, Jobs, or Tasks to be tracked can be used to determine item number length requirements. for example a one digit Department number has a maximum of ten values. (0 to 9) It would not be possible to track 12 departments with a one digit department number as the department number must be unique. Future growth should also be accounted for when designing a numbering system. A company with 8 departments would do well to use a two digit department number to allow for a maximum of 100 departments. (0 to 99)

3.) List all active Departments, Jobs, and Tasks and assign each an Item Number with the chosen length. Refer to this list when configuring Departments, Jobs, and Tasks within InfiniTime. Ensure each item has a unique item number. Note: All Department Numbers, Job Numbers, and Task Numbers must be unique though they are independent of each other. For example a Department, Job, and Task with an item number of 10 can be created. In this example the Department Number, Job Number, and Task Number would simply all be set to 10.

Example Item List: ABC Carpentry & Contractors

| Item                | Type       | Item Number |
| ------------------- | ---------- | ----------- |
| Construction        | Department | 10          |
| Electrical          | Department | 20          |
| Philly Mae Pizzeria | Job        | 10000       |
| Suzzies Pizzeria    | Job        | 10001       |
| Framing             | Task       | 1001        |
| Drywall             | Task       | 1002        |
| Wiring              | Task       | 2010        |
| Engineering         | Task       | 2011        |

The above example shows a subset of all Tasks, Departments, and Customers currently active at ABC Carpentry & Contractors. From the examples the chosen item number lengths are evident:

Department Numbers - 2 Digits

Job Numbers -  5 Digits

Task Numbers - 4 Digits

A pattern also exists in the Task Numbers for readability and ease of use. This is an optional design concept which may be useful in some organizations. ABC Carpentry and Contractors employees a variety of employees from Electrical Engineers and Contractors to Carpenters. Some tasks are specific to a particular department and include the department number inside of the task number to show this relationship. IE: Wiring, #2010 is related to the Electrical Department #20. Overall, the most important idea when designing a numbering system for Departments, Jobs, and Tasks is to ensure numbering remains consistent.

Item Lookup, the third method for transferring between Departments, Jobs, and Tasks, is only available within the InfiniTime Employee and Punch Modules. Employees can type the first few letters of the Department, Job, or Task name and the remaining characters will be automatically filled. They also have the option of using the Lookup Tool which displays all available Departments, Jobs, or Tasks in a searchable list.

| Data Collection Terminal            | Supported Labor Transfer Method |
| ----------------------------------- | ------------------------------- |
| Athena                              | Item List                       |
| Juno                                | Item List                       |
| Luna                                | Item List                       |
| Scout                               | Transfer by Item Number         |
| Thor                                | Transfer by Item Number         |
| Zephyr                              | Item List                       |
| InfiniTime Employee & Punch Modules | Item Lookup                     |

Note: Allow PC Punch Labor Switching must be checked before employees will be able to choose their Department, Task, or Job from the InfiniTime Employee & Punch Modules
