xml version="1.0" encoding="utf-8"?





Employee Without Reviewed Timecards




# Employee Without Reviewed Timecards

Displays a list of employees within the date range specified by Selection Criteria whoâs Timecard Activity has not yet been reviewed.

Report Example:

![](/img/image-404.png)

Notes/Usage:

In order to view all employees that have not yet been reviewed within the specified period, run this report with the default selection criteria and alter only the date range.

Options:

| Option | Default Value | Description |
| Alert When Number of Reviews are Less Than? | 0 | If an employee has less than the number of reviewes indicated by this option they will be listed on the report. |
| Alert When Timecards are Not Reviewed by Employee? | No | When set to Yes, Employees with timecards that have not been reviewed by the employee they will be listed on the report. |
| Alert When Timecards are Not Reviewed by Supervisor? | Yes | When set to Yes, Employees with timecards that have not been reviewed by their assigned Supervisor will be listed on the report. |
| Allow Graphics On the Report? | Yes | This option allows you to choose if you want to print the InfiniTime 7.0 logo on the report. |
| Department Selection Based On? | Employee Default Department | This option will allow you to select how the Department  filter is used to select employees. By default, departments tagged on the selection criteria will cause InfiniTime to display employees assigned to that department on the report. Alternatively, selecting 'Worked in Department' will show employees that worked in the selected department during the selected date range. |
| Group by Department? | No | This option will group employees specified by the Employee Filter according to their Default Department. |
| Group by Job? | No | This option will group employees specified by the Employee Filter according to their Default Job. |
| Group by Supervisor? | No | This option will group employees specified by the Employee Filter according to their Default Supervisor. |
| Group by Task? | No | This option will group employees specified by the Employee Filter according to their Default Task. |
| Group level to group by: | None | This option will sort employees specified by the Employee Filter according to their group description for the selected group level. For example, a company with multiple locations might have a Group Level of 'Location' and Group Descriptions of 'Pittsburgh' , 'Phoenix' , and 'Jacksonville'. Selecting the 'Location' group level would sort employees according to their assigned location. |
| Job Selection Based On: | Employee Default Job | This option will allow you to select how the Job filter is used to select employees. By default, jobs tagged on the selection criteria will cause InfiniTime to display employees assigned to the job on the report. Alternatively, selecting 'Worked in Job'' will show employees that worked in the selected job during the chosen date range. |
| Page Break by Department? | No | This option will allow you page break the report based on the Employee's Default Department, making it easier to give the report to department heads for review if needed. |
| Page Break by Employee? | No | This option will allow you to page break the report based on each employee, making it easier to give the report to the individual employees for review. |
| Page Break by Group? | No | This option will allow you to page break the report based on each Group Description and is intended for use with 'Group Level to Group By.' The report can then be distributed as necessary. |
| Page Break by Job? | No | This option will allow you to page break the report based on the Employee's Default Job, making it easier to give the reports to Job Supervisors for review. |
| Page Break by Supervisor? | No | This option will allow you to page break the report based on Employee Supervisors, making it easier to distribute to Supervisors for review. |
| Page Break by Task? | No | This option will allow you to page break the report based on the Employee's Default Job, making it easier to give the reports to Task Supervisors for review. |
| Print Inactive Employees? | No | This option will allow you to print information of the inactive employees along with the active ones. |
| Sort by Employee Number? | No | This option will group employees specified by the Employee Filter according to their Employee ID. |
| Task Selection Based On: | Employee Default Task | This option will allow you to select how the Tob filter is used to select employees. By default, tasks tagged on the selection criteria will cause InfiniTime to display employees assigned to the task on the report. Alternatively, selecting 'Worked in Task'' will show employees that worked in the selected task during the chosen date range. |

[Report List](../Report_List.md)