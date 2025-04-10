xml version="1.0" encoding="utf-8"?





Failed Biometric Verification




# Failed Biometric Verification

Displays a list of employees who have failed biometrics verification within the date range specified by Selection Criteria.

Report Example:

Notes/Usage:

Abrupt changes in hand geometry can lead to biometrics verification failure. This may occur when excessively long fingernails are cut or if excessively long fake nails are applied. It may be necessary to re-enroll an employee within the Hand Reader under these circumstances. Otherwise, if employees are having trouble with hand verification try raising the Reject Level, which will reduce hand reader sensitivity. Refer to the Scout Reader Configuration section of this document for more information.  Also you can check if in fact the employee tried to punch in or they are just trying to beat the system and say that the reader did not scan their hand or finger depending of the biometric solution you have.

Options:

| Option | Default Value | Description |
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

[Report List](/InfiniTime/help%20file/Reports/Report_List.md)