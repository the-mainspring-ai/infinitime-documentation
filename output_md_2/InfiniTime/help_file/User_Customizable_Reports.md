xml version="1.0" encoding="utf-8"?





User Customizable Reports




# User Customizable Reports

Unlike previous versions of InfiniTime, InfiniTime 7 does not include the crystal reports add on due to the complexity of the ASP.NET environment and licensing issues. As an alternative customizable reports have been added to the software which give the user the ability to pick and choose the information that will be displayed on the report. By changing the report options users can control the information displayed on the report. The customization process is outlined below.

Quick Print vs Saved Reports

Customizable reports can be prepared in two different fashions, quick print or a saved report. Quick print is used to provide specific information for immediate review. The selection criteria and report settings will not be saved. It is generally more efficient to configure a saved report for customizable reports due to the numerous configuration options. This makes it possible to run the saved report criteria at a later date. All of the configuration options detailed below are available through quick print or a saved report.

Customizable InfiniTime Reports

A list of all customizable reports within the InfiniTime Application is provided below.

* Dept. Payroll Detail
* Dept. Payroll Summary
* Payroll Detail
* Payroll Summary
* Department Daily Summary
* Department Summary
* Shift Daily Summary
* Shift Summary
* Timecard Summary

General Settings

The customizable Timecard Summary report includes all of the standard features offered for InfiniTime reports including standard email functionality, automatic reporting features, PGP Encryption, and a complete filtering system which can be used to select employees for whom timecard activity will be reported for. A link to the appropriate section of this document is provided below for more information.

[Emailing Reports](/InfiniTime/help%20file/Email.md)           â          [Automatic Report Scheduling](/InfiniTime/help%20file/Auto_Report_Schedule.md)           â           PGP Encryption           â          [Selection Criteria](/InfiniTime/help%20file/Selection_Criteria.md)

Customizable Options

Customizable Report Options: Page 1

![](images_2/TimecardSummary_OP1.gif)

Timecard Summary Options: Page 2

![](images_2/TimecardSummary_OP2.gif)

Column Configuration

Customizable Reports are user configurable. Each column of the report can be set to show a specific type of hours according to the users preferences.

Approved Overtime Hours One - Shows all Overtime One Hours that have been approved.

Approved Overtime Hours Two - Shows all Overtime Two Hours that have been approved.

Approved Overtime Hours Three - Shows all Overtime Three Hours that have been approved.

Approved Overtime Hours Four - Shows all Overtime Four Hours that have been approved.

Break Hours - Displays a total of change to break and auto break hours.

Other Activity One - Displays all hours for the chosen Other Activity Type.

Other Activity Two - Displays all hours for the chosen Other Activity Type.

Other Activity Three - Displays all hours for the chosen Other Activity Type.

Other Activity Four - Displays all hours for the chosen Other Activity Type.

Other Amount - Sum of all Other Amounts not displayed in another report column.

Other Hours - Sum of all Other Activity Hours not displayed in another report column.

Overtime Hours One - Shows both approved and unapproved overtime one hours.

Overtime Hours Two - Shows both approved and unapproved overtime one hours.

Overtime Hours Three - Shows both approved and unapproved overtime one hours.

Overtime Hours Four - Shows both approved and unapproved overtime one hours.

Regular Hours - Shows all regular hours.

Unapproved Overtime Hours One - Shows all Overtime One Hours has not been approved.

Unapproved Overtime Hours Two - Shows all Overtime One Hours has not been approved.

Unapproved Overtime Hours Three - Shows all Overtime One Hours has not been approved.

Unapproved Overtime Hours Four - Shows all Overtime One Hours that has not been approved.

*Note:* Other Activity Hours Types displayed in a report column will not count toward the Other Amount or Other Hours Column.

*Note:* To make a column blank simply assign it to an Other Activity Type that has not been assigned. Unassigned Other Activity Types are set to 'None.' Read below for additional information.

Other Activity Types

To display other activity types in a column on customizable reports the other activity type must first be assigned to one of five Other Activity place holders as outlined below. It is not necessary to configure all five other activity type place holders. Any combination of Other Activity One through Other Activity Five may be configured and used in a report column.

1.) Select the desired other activity types on the Options Tab.

![](images_2/SelectOtherAct_1.gif)

2.) Set the chosen column to the Other Activity Type place holder.

![](images_2/SelectOtherAct_2.gif)

Additional Options:

| Option | Default Value | Description |
| Allow Graphics On the Report? | Yes | This option allows you to choose if you want to print the InfiniTime 7.0 logo on the report. |
| Department Grouping Type? | None | This option allows you to group the report by the employees Activity Department, meaning that the hours will distribute to all the departments the employee worked, or group by Employee Default Department,which will put all the time worked in their default department even if they worked on other departments, or the last option is None. |
| Department Selection Based On? | Employee Default Department | This option will allow you to select how the Department  filter is used to select employees. By default, departments tagged on the selection criteria will cause InfiniTime to display employees assigned to that department on the report. Alternatively, selecting 'Worked in Department' will show employees that worked in the selected department during the selected date range. |
| Group By Supervisor? | No | This option will group employees specified by the Employee Filter according to their Default Supervisor. |
| Group Level to group by: | No | This option will sort employees specified by the Employee Filter according to their group description for the selected group level. For example, a company with multiple locations might have a Group Level of 'Location' and Group Descriptions of 'Pittsburgh' , 'Phoenix' , and 'Jacksonville'. Selecting the 'Location' group level would sort employees according to their assigned location. |
| Job Grouping Type? | None | Determines how employees will be grouped by Jobs. When set to None the   option is considered disabled and employees will not be grouped by jobs.   When set to Employee Default Job employees will be grouped according to   their default job as assigned on their employee record. When set to Scheduled Job employees will be grouped according to the job they were scheduled for. |
| Job Selection Based On: | Employee Default Job | This option will allow you to select how the Job filter is used to select employees. By default, jobs tagged on the selection criteria will cause InfiniTime to display employees assigned to the job on the report. Alternatively, selecting 'Worked in Job'' will show employees that worked in the selected job during the chosen date range. |
| Page Break by Department? | No | This option will allow you page break the report based on the Employee's Default Department, making it easier to give the report to department heads for review if needed. |
| Page Break by Employee? | No | This option will allow you to page break the report based on each employee, making it easier to give the report to the individual employees for review. |
| Page Break by Group? | No | This option will allow you to page break the report based on each Group Description and is intended for use with 'Group Level to Group By.' The  report can then be distributed as necessary. |
| Page Break by Job? | No | This option will allow you to page break the report based on the Employee's Default Job, making it easier to give the reports to Job Supervisors for review. |
| Page Break by Supervisor? | No | This option will allow you to page break the report based on Employee Supervisors, making it easier to distribute to Supervisors for review. |
| Page Break by Task? | No | This option will allow you to page break the report based on the Employee's Default Job, making it easier to give the reports to Task Supervisors for review. |
| Print Inactive Employees? | No | This option will allow you to print information of the inactive employees along with the active ones. |
| Print Time In Hours and Minutes? | No | When set to Yes, Punch In and Punch Out Times on the report will be displayed in Hours and Minutes rather than hours and hundredths of an hour. |
| Show Company Grand Total? | No | When set to Yes a total record will be added to the bottom of the report to show total company hours  for selected columns. |
| Sort by Employee Number | No | This option will group employees specified by the Employee Filter according to their Employee ID. |
| Task Grouping Type? | None | Determines how employees will be grouped by Tasks. When set to None   the option is considered disabled and employees will not be grouped by   tasks. When set to Employee Default Task employees will be grouped according to their default task as assigned on their employee record. When set to Scheduled Task employees will be grouped according to the task they were scheduled to work in. |
| Task Selection Based On: | Employee Default Task | This option will allow you to select how the Tob filter is used to select employees. By default, tasks tagged on the selection criteria will cause InfiniTime to display employees assigned to the task on the report. Alternatively, selecting 'Worked in Task'' will show employees that worked in the selected task during the chosen date range. |