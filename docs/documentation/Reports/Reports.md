---
title: "Reports Overview"
description: "A guide to accessing and understanding the various reports available in InfiniTime, including informational and data-driven reports for employee and timecard management."
---

# InfiniTime Reports - Introduction

InfiniTime Reports are organized into categories for ease of use and accessibility as shown below.

## Accessing the Report Library

1. Click on the Reports Button on the Toolbar.

2. The Report Library Table will be displayed. Click on the + Sign to expand a given report category and display reports included.

## Quick Print vs Saved Reports

Quick Print permits admins only one time execution of a given report for immediate viewing. These configuration settings are not saved for future use.

Saved Reports allow users to save report configurations and criteria for frequently run reports to avoid repetitive setup.

### Saved Reports - Essential Concepts

- All users with Report Library access can create, view, run, and edit any saved report
- While you can't restrict access to specific reports within the Report Library, you can:

  1. Use InfiniTime Escort to show only certain reports to specific users
  2. Use security settings to block Report Library access entirely

  See the [Escort](../Escort/Escort_Overview.md#esc01_Escort_Overview) and [Security](../Security/Security_Overview.md#sec01_Security_Overview) sections for details.

- Set up Saved Reports for routine tasks like:

  - Daily operations
  - Weekly reviews
  - Payroll processing

  This helps supervisors and administrators quickly access common reports, such as current and previous pay period timecards.

### Tips and Best Practices

- When creating saved reports for specific departments or locations, supervisors should include a unique label (such as their Department or Location name) to help other supervisors identify who created and uses these reports.

## Customizing the Report Library

You can:

- Create custom report categories for specific users or departments
- Copy default InfiniTime reports to these custom categories
- Organize reports in a way that makes sense for your organization

Here are the standard report categories included with InfiniTime:

- Employee Information Reports - Provides information on employees that is not related to Time Activity. Examples include Employee accruals, comments, and an employee list.
- Job Cost Reports - Designed for reviewing Job and Task hours distributions. Intended for labor costing analysis. The Job Cost Reports Category will not be displayed if there are no Jobs or Tasks configured within InfiniTime.
- Management Reports – Designed for management purposes only, these reports assist with exception tracking, auditing, and other management related tasks.
- Payroll Reports – Payroll reports assist employers by providing a summary of employee earnings based upon an employee's hours and specified wage. It is important to note that these reports do not compute deductions and are considered gross pay.
- Schedule Reports – Various types of schedule reports can be printed to obtain hard copies of employee work schedules for viewing purposes.
- System Reports – The System Reports provide information about your InfiniTime software and related hardware configuration.
- Timecard Reports - The Timecard Reports provide a variety of report types that display a summary or detailed information of employees timecard activity.

### Default Report Category Selected

Insert - Creates a new Report Category and Opens the Report Category Update Form. The user may then enter a description for the new Report Category. User Created Reports can then be placed into the new report category for organization purposes.

Change - Opens the Report Category Update Form for the Selected Report Category. The user may change the Report Category name if desired.

### User Created Report Category Selected

Insert - Creates a new Report Category and Opens the Report Category Update Form. The user may then enter a description for the new Report Category. User Created Reports can then be placed into the new report category for organization purposes.

Change - Opens the Report Category Update Form for the Selected Report Category. The user may change the Report Category name if desired.

Delete - Deletes the Selected Report Category. All user created reports assigned to the Report Category will be deleted.

### Default Report Selected

![](/img/SelectOtherAct_1.gif)

Copy - Creates a User Created report using the selected Default Report as a template. The user created report may be placed into a separate report category, renamed, or be configured with its own set of Saved Reports.

Quick Print - Opens the Report Selection Criteria Update Form. Permits the user to perform a single execution for a given report based on Report Selection Criteria settings configured by the user.

Insert - Creates a new User Created Report and Opens the Report Layout Update Form where the user may enter a description for the new report. User Created Reports can then be placed into the new report category for organization purposes. It is important to note that user created reports created using the Insert Button are intended for use only with Custom Crystal Report files designed by and specifically provided for use with InfiniTime by Inception Technologies.

![](/img/Activity_Summary.gif)

Change - Opens the Report Layout Update Form where the user may enter a description for the new report. User Created Reports can then be placed into the new report category for organization purposes.

### User Created (Copied or Imported) Report Selected

![](/img/ImportReports_02.gif)

Copy - Creates a User Created report using the selected Default Report as a template. The user created report may be placed into a separate report category, renamed, or be configured with its own set of Saved Reports.

Import

- Populates the selected User Created Report with a Crystal Report File selected from the local hard disk by the user. Only Crystal Report files designed and provided by Inception Technologies for use with InfiniTime should be imported into the report library using this feature. It is important to note that all Default Reports and User Created Reports created by copying a Default Report will be populated with a Crystal Report File by default. User Created Reports created via insert will initially contain no crystal report file and as a result, cannot be executed.

Quick Print - Opens the Report Selection Criteria Update Form. Permits the user to perform a single execution for a given report based on Report Selection Criteria settings configured by the user.

Insert - Creates a new User Created Report and Opens the Report Layout Update Form where the user may enter a description for the new report. User Created Reports can then be placed into the new report category for organization purposes. It is important to note that user created reports created using the Insert Button are intended for use only with Custom Crystal Report files designed by and specifically provided for use with InfiniTime by Inception Technologies.

![](/img/Mini_Timecard_Detail.gif)

Description

- Enter a description for the User Created Report.

Category

- Used to assign the report to a report category. Users may click on the Lookup Button to select from existing report categories as shown below.

Report Category Table

![](/img/Employee_With_Exceptions.gif)

Select

- Assigns the previously selected report to the highlighted Report Category.

Insert

- Permits entry of a new report category. Opens the Report Category Update Form.

Change

- Opens the Report Category Update Form for the Selected Report Category. Users may then edit the Report Category Description.

Delete

- Deletes the selected report category.

WARNING: If a report category is deleted, all associated reports will be removed from the Report Library.

Change - Opens the Report Layout Update Form where the user may alter the description for the report. User Created Reports may then be placed into the new report category for organization purposes if desired.

Delete - Removes the User Created Report from the Report Library. All saved reports associated with the User Created Report will be deleted.

## Report Selection Criteria Update Form

The report selection criteria update form is displayed after clicking quick print and when a report is saved. Selection criteria determines which employees data will be displayed for in addition to the way the report is displayed. All fields are summarized below.

General Tab

![](/img/image465.gif)

Description: Enter a descriptive name for the report setting. This name will be displayed in the Report Library Table when entering saved report settings. This field is not available when using quick print.

Use Description as Report Name: This will use the report name as a title for the report when it is printed.

Inactive: Checking this box will render the report inactive. The report will be displayed in red on the Report Library Table and cannot be used until it is reactivated.

Print Preview: Displays a preview of the report on-screen before it is sent to the printer.

Export File Name: If you wish to save the report to a file enter the file name here. It is important to note that a path cannot be used.

PGP - The PGP tab is only available after an export file name has been specified. PGP is an encryption algorithm and can be used to secure report files against undesired access. Refer to PGP Encryption: Introduction for detailed information regarding the use and configuration of PGP.

## Selection Criteria

The selection criteria tab employs various filters in order to select what employees will be included in the report. It is important to note that employees must meet all selection criteria in order to be present in the report. For example, if a certain group and department are selected, only employees within the specified group and department will be printed in the report. The selection criteria are configured to print for all employees by default.

![](/img/Rpt014.png)

Date Range: Select the date range the report will be executed for. If you wish to view activity from last pay period for example, then choose last pay period.

Selected Employees: Select individual employees to be included in the report. Change the drop down box from All to Selected, and tag employees you wish to include in the report. Employees can be selected in addition to other filters such as departments and groups. Selected employees will be shown in addition to any employees indicated by the department and group selections.

Selected Departments: Select individual departments to be included in the report. Change the drop down box from All to Selected, and tag departments you wish to include in the report.

Selected Jobs: Select individual Jobs to be included in the report. Change the drop down box from All to Selected, and tag Jobs you wish to include in the report.

Selected Tasks: Select individual Tasks to be included in the report. Change the drop down box from All to Selected, and tag Tasks you wish to include in the report.

Selected Groups: Select individual groups to be included in the report. Change the drop down box from All to Selected, and tag groups you wish to include in the report. When selecting multiple groups information will be shown for all employees in each group.

Selected Exceptions: Select individual groups to be included in the report. Change the drop down box from All to Selected, and tag groups you wish to include in the report. All exceptions will be shown for employees that have any of the indicated exceptions.

Selected Other Activities: Select individual other activity types to be included in the report. Change the drop down box from All to Selected, and tag other activity types you wish to include in the report. Only the other activity types indicated will be displayed on the report. Regular activity and overtime will not be displayed.

Misc. Selections: Select individual employees to be included in the report. Change the drop down box from All to Selected, and tag employees you wish to include in the report.

_Note_: It is not uncommon for users to Choose 'Selected' in order to specify individual employees, departments, jobs, tasks or groups and then forget to tag specific employees, departments, jobs, tasks or groups. Employees are not selected if a green checkmark is not displayed to the left of their name. Should selected be chosen, and no employees specified, selection criteria will automatically revert to the 'All' selection in order to avoid an error.

## Email

![](/img/Employee_With_Zero_Hours.gif)

InfiniTime gives you the capability to E-mail reports from the software in a range of formats. E-mailing the reports can be done right after the report has been printed or automatically according to a schedule (see Auto Report Schedule).

From - Allows the user to specify the email address that will appear in the 'From' field for report files sent via email. In this way the recipient can reply to the email and the message will be sent to the correct person. For example Ms. Jackson is the in charge of payroll processing at a small company. She would enter her email address in the from field so employees could reply to reports that were emailed to them in order to give her feedback on their timecard reports.

Subject - This is the subject of the email that will be displayed in the recipients e-mail.

Format - You can choose from several different formats that the report will be exported and e-mailed. The formats include, PDF, Excel, Comma Separated text, or WORD document.

Body Text - You can type a message that will be in the e-mail along with the attached report.

Send To - This is the list of people that will receive the e-mail.

Insert - Click on the insert button to add a recipient for the email. First fill in the name and press enter. The cursor will then move into the address column. Fill out the address and then press enter. To insert multiple recipients repeat the steps above.

![](/img/ImportReports_06.gif)

Change - Click on this button to make changes to the recipient information.

Delete - To delete a recipient, highlight the recipient under the Address List and press the delete button.

Technical Note: InfiniTime uses the Windows Operating System on the InfiniTime Server . If you should experience issues with auto reports please refer to the [Automatic Reports Requirements](Reports.md#AutoReq) and the

## Auto Report Schedule

![](/img/rep12.gif)

InfiniTime allows a schedule to be configured in order to run reports automatically. Reports are automatically emailed or printed depending on the configuration. Settings must be saved for a report before it can be configured to run automatically.

Note: The InfiniTimeHouseKeeping service must be running in order for reports to print automatically.

Insert Click insert to open up the Auto Report Schedule Update Form and set a schedule.

Change Click change to make any adjustments to a previously configured schedule.

Delete Click delete to remove the highlighted Report Schedule.

![](/img/Rpt038.png)

Description Describes the Report Schedule you are creating. This name will appear in the Report Library Update Form. This is how you will be able to distinguish between other Auto Report Schedules you may create.

Printer

- InfiniTime uses printer drivers to prepare reports for proper display on your computer. Select a printer that is installed and attached to your machine. Do not select an image printer. The warning below will be displayed when saving the Auto Report Schedule. Reports without a valid printer may not print or display properly.

![](/img/ReportSelectionCriteria_Filters.gif)

Frequency - This is how often the program will run the auto report schedule feature. The options are: Once, Daily, Weekly, and Monthly.

Do Not Print

- The Do Not Print check box is only displayed when a report is configured to be sent to a remote party via email or FTP. Reports will be printed according to the automatic report schedule by default. This box should be checked if you wish to email or send a report via FTP without printing the report.

Date to Print - This is the date that you want the system to print the current set up on.

Time to Print - This is the time that you want the system to print the current set up on the date selected above.

Day of Week to Print - Select the day of week you wish for the system to print the structure on.

Date Last Printed - Tells you the last date the system automatically printed the structure.

Time Last Printed - Tells you the last time on the date above the system automatically printed the structure.

Date to Print Next - The date entered here will be the next future date that the system will automatically print a saved structure.

### Auto Report Requirements

InfiniTime can be configured to automatically email or print reports, payroll exports, and exports with saved criteria. A list of requirements and items that are known to interfere with the intended processing of auto reports can be found below. Each requirement must be met for auto reports to function as intended.

It should also be noted that saved report settings configured with an email address will only be emailed according to the settings on the auto report schedule and email tabs. They will not be printed automatically. A single saved report setting cannot be used to automatically email and print a report. Separate saved settings must be configured. Your network administrator may need to assist you with configuring the following items.

To automatically email a report the following criteria must be observed:

- The InfiniTime Server must have an active Internet connection.
- Power Management must be disabled on the Network Interface Card of the InfiniTime Server.
- The InfiniTime Housekeeping Service must be started and running.
- The InfiniTime Server does not need to have a user logged into the console. However, it must at least be powered on and idle at the Windows Login Splash Screen.
- A printer must be installed on the InfiniTime Server.
- A printer must be set as the default printer.
- The Print Spooler Service must be started and running on the InfiniTime Server.
- Your fully qualified domain name may need to be configured in the advanced delivery options of the SMTP Virtual Server created by InfiniTime depending on your domain policies.
- An auto schedule must be configured within a saved report setting.
- A destination name and email address must be defined on the email tab of the saved report setting.
- The server must be granted permissions to relay email through the SMTP Virtual Server installed by InfiniTime.

- Depending on your network configuration and domain settings it may be necessary to forward all outgoing email messages from the InfiniTime SMTP Virtual Server to a Smart Host. Generally the Smart Host will be a server running exchange on your local network. The smart host can be configured under Advanced Options of Delivery tab for the InfiniTime SMTP Virtual Server Properties.

To automatically print a report the following criteria must be observed:

- The InfiniTime Server must have an active Internet or Local Area Network connection if the destination printer is not directly connected to the InfiniTime Server.
- Power Management must be disabled on the Network Interface Card of the InfiniTime Server if the destination printer is not directly connected to the InfiniTime server.
- The InfiniTime Housekeeping Service must be started and running.
- The InfiniTime Server does not need to have a user logged into the console. However, it must atleast be powered on and idle at the Windows Login Splash Screen.
- A printer must be installed on the InfiniTime Server.
- A printer must be set as the default printer.
- The Print Spooler Service must be started and running on the InfiniTime Server.
- An auto schedule must be configured within a saved report setting.

## Options

![](/img/AccrualWages_Example.gif)

A list of additional settings are available on the Options Tab. Select Yes or No using the drop down boxes in order to enable or disable the option. Some options are specific to certain reports and will not be available for all reports.

Allow Graphics On The Report - Enables or disables the display of graphics on the report.

Department Selection Based On - Choose how tagging departments on the Selection Criteria Tab effects the information displayed on the report. If this option is set to Employee Default Department employees will be shown with Default Departments that match departments indicated by the Selection Criteria. If this option is set to Employee Worked in Department Employees who have activity in the departments indicated by the Selection Criteria in the chosen date range will be displayed on the report.

Employee Default Department - Selecting this option all hours worked by an employee will display under their default department even if they have activity in other departments, all of the activity for all departments will show under that employees default department.

Employee Worked On Department - Selecting this option all hours worked by an employee will display in the department that employee worked in, so you might see that employees name associated with different departments in the report.

Department Selection Filters Activity? - When enabled, Timecard Activity is filtered according to departments tagged on the Department Tab of the Report Selection Criteria Update Form. Timecard records will only be displayed for hours worked in the selected departments. This feature is intended for use in conjunction with the Department Selection Based On 'Employee Worked In Department' option.

Employee Grouping Type - Choose how employees will be ordered on the report. If this option is set to Employee Name employees will be ordered alphabetically by name. If this option is set to Activity Department employees will be listed according to the department they worked in. If this option is set to Employee Department employees will be listed according to the department they are assigned to.

Group By Department - Enabling this option will group all employees in the same department together on the report.

Hide Audit Trail Asterisk - Enabling this option will hide all audit trail asterisks on the report. Audit trail asterisks are displayed by default to indicate punches that have been edited or inserted manually.

Hide Exceptions - Exceptions will not be displayed on the report if this option is enabled.

Page Break By Department - Enabling this option will start a new page for each department.

Page Break By Employee - Enabling this option will start a new page for each employee.

Print Inactive Employees - Enabling this option will print information for inactive employees.

Print Signature Line - A signature line will be displayed at the bottom of the results for each employee if this option is enabled. Generally Page Break by Employee should be enabled when using this feature.

Print Standard Breaks - Disabling this option removes the Break Column from the report.

Print Time in Hours and Minutes

- InfiniTime reports activity in hundredths of an hour by default. Setting this option to Yes displays activity totals in hours and minutes.

Print Timecard Review History

- When enabled, Timecard Review history displays a list of supervisors, including Supervisor Name, Supervisor Position, and Last Review Time, for each employee who have reviewed all of the employees Timecard Records for the selected date range. A supervisor's name will not be listed if all records during the date range are not reviewed by the supervisor. Only the Timecard Review History header will be displayed if there are no supervisors who have reviewed all of an employee's Timecard Records for the selected date range. The Timecard Review History option is available on the following reports:

* Timecard Detail
* Timecard Detail with Weekly Totals
* Timecard With Clock Description
* Timecard With Phone Numbers

Example Timecard Detail Report with Timecard Review History:

![](/img/Rpt025.png)

Print Weekly Totals - Enabling this option adds a subtotal row for each week to report.

Punch Description Displays - Changes the information displayed in the Punch Description column of the report. By default grace periods such as tardy and early are displayed in this area. Additional options are Telephone Number, Nothing, and Clock Description.

## Configuring Reports for Use With The Employee Module

As mentioned in the Employee Module section of this document, each report menu item within the employee module is fully customizable. These buttons can be configured to print any single report within the InfiniTime software. If you should have the Crystal Reports module, custom reports can be assigned to these menu items as well.

To Configure Reports for Use With The Employee Module:

- Open the Report Library by Clicking on the reports button as displayed below.

![](/img/Employee_Profiles_1.gif)

- Click on the plus sign to show the reports within a particular category.

![](/img/QS_Chapter1_09.gif)

- Select the report you wish to designate for use from the Employee Module.

![](/img/image151.gif)

- Click Change.

![](/img/Rpt005.png)

- Click on the Options Tab.

![](/img/ImportReports_01.gif)

- Check the button you wish to assign the report to.

![](/img/TCard018.png)

Note: Each button within the employee module can only have one report assigned to it. If a report is assigned to an Employee Module button the check box will be gray and un-selectable. The original report must first be unassigned before a new report can be selected for use. The following reports are assigned to the Employee Module by default:

Timecard Button: Timecard Details

Accruals Button: Employee Accruals

Schedule Button: Postable Schedule

## User Customizable Reports

Unlike previous versions of InfiniTime, InfiniTime 7.0 does not include the crystal reports add on due to the complexity of the ASP.NET environment and licensing issues. As an alternative customizable reports have been added to the software which give the user the ability to pick and choose the information that will be displayed on the report. By changing the report options users can control the information displayed on the report. The customization process is outlined below.

Quick Print vs Saved Reports

Customizable reports can be prepared in two different fashions, quick print or a saved report. Quick print is used to provide specific information for immediate review. The selection criteria and report settings will not be saved. It is generally more efficient to configure a saved report for customizable reports due to the numerous configuration options. This makes it possible to run the saved report criteria at a later date. All of the configuration options detailed below are available through quick print or a saved report.

Customizable InfiniTime Reports

A list of all customizable reports within the InfiniTime Application is provided below.

- Dept. Payroll Detail
- Dept. Payroll Summary
- Payroll Detail
- Payroll Summary
- Department Daily Summary
- Department Summary
- Shift Daily Summary
- Shift Summary
- Timecard Summary

General Settings

The customizable Timecard Summary report includes all of the standard features offered for InfiniTime reports including standard email functionality, automatic reporting features, PGP Encryption, and a complete filtering system which can be used to select employees for whom timecard activity will be reported for. A link to the appropriate section of this document is provided below for more information.

[Emailing Reports](Reports.md#rpt13_Email) [Automatic Report Scheduling](Reports.md#rpt18_Auto_Report_Schedule) [PGP Encryption](../Security/Security_Overview.md#sec54_Optional_PGP_Encryption_for_Output_Files) [Selection Criteria](Reports.md#rpt11_Report_Selection_Criteria_Update_Form)

Customizable Options

Customizable Report Options: Page 1

![](/img/Audit_Trail.gif)

Timecard Summary Options: Page 2

![](/img/Employee_Points.gif)

Column Configuration

Customizable Reports are user configurable. Each column of the report can be set to show a specific type of hours according to the users preferences. Available Hours Types are listed below.

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

_Note:_ Other Activity Hours Types displayed in a report column will not count toward the Other Amount or Other Hours Column.

_Note:_ To make a column blank simply assign it to an Other Activity Type that has not been assigned. Unassigned Other Activity Types are set to 'None.' Read below for additional information.

Other Activity Types

To display other activity types in a column on customizable reports the other activity type must first be assigned to one of five Other Activity place holders as outlined below. It is not necessary to configure all five other activity type place holders. Any combination of Other Activity One through Other Activity Five may be configured and used in a report column.

1.) Select the desired other activity types on the Options Tab.

![](/img/Rpt024.png)

2.) Set the chosen column to the Other Activity Type place holder.

![](/img/Important_Dates.gif)

Additional Options:

| Option                                 | Default Value               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| -------------------------------------- | --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Allow Graphics On the Report?          | Yes                         | This option allows you to choose if you want to print the InfiniTime 7.0 logo on the report.                                                                                                                                                                                                                                                                                                                                                                    |
| Department Grouping Type?              | None                        | This option allows you to group the report by the employees Activity Department, meaning that the hours will distribute to all the departments the employee worked, or group by Employee Default Department,which will put all the time worked in their default department even if they worked on other departments, or the last option is None.                                                                                                                |
| Department Selection Based On?         | Employee Default Department | This option will allow you to select how the Department filter is used to select employees. By default, departments tagged on the selection criteria will cause InfiniTime to display employees assigned to that department on the report. Alternatively, selecting 'Worked in Department' will show employees that worked in the selected department during the selected date range.                                                                           |
| Department Selection Filters Activity? | No                          | If this option is set to Yes, employee Timecard Records displayed on the report will be filtered according to tagged departments as follows: 1.) Only employees with Timecards in the tagged department(s) will be displayed on the report. 2.) Only Timecard records assigned to the tagged department(s) will be used to calculate totals for display on the report. All other timecard records for employees will be ignored when this option is set to Yes. |
| Group By Supervisor?                   | No                          | This option will group employees specified by the Employee Filter according to their Default Supervisor.                                                                                                                                                                                                                                                                                                                                                        |
| Group Level to group by:               | No                          | This option will sort employees specified by the Employee Filter according to their group description for the selected group level. For example, a company with multiple locations might have a Group Level of 'Location' and Group Descriptions of 'Pittsburgh' , 'Phoenix' , and 'Jacksonville'. Selecting the 'Location' group level would sort employees according to their assigned location.                                                              |
| Job Grouping Type?                     | None                        | Determines how employees will be grouped by Jobs. When set to None the option is considered disabled and employees will not be grouped by jobs. When set to Employee Default Job employees will be grouped according to their default job as assigned on their employee record. When set to Scheduled Job employees will be grouped according to the job they were scheduled for.                                                                               |
| Job Selection Based On:                | Employee Default Job        | This option will allow you to select how the Job filter is used to select employees. By default, jobs tagged on the selection criteria will cause InfiniTime to display employees assigned to the job on the report. Alternatively, selecting 'Worked in Job'' will show employees that worked in the selected job during the chosen date range.                                                                                                                |
| Job Selection Filters Activity?        | No                          | If this option is set to Yes, employee Timecard Records displayed on the report will be filtered according to tagged departments as follows: 1.) Only employees with hours in the tagged Job(s) will be displayed on the report. 2.) Only timecard records assigned to the tagged Job(s) will be used to calculate totals for display on the report. All other timecard records for employees will ignored when this option is set to Yes.                      |
| Page Break by Department?              | No                          | This option will allow you page break the report by Department, making it easier to give the report to department heads for review if needed.                                                                                                                                                                                                                                                                                                                   |
| Page Break by Employee?                | No                          | This option will allow you to page break the report based on each employee, making it easier to give the report to the individual employees for review.                                                                                                                                                                                                                                                                                                         |
| Page Break by Group?                   | No                          | This option will allow you to page break the report based on each Group Description and is intended for use with 'Group Level to Group By.' The report can then be distributed as necessary.                                                                                                                                                                                                                                                                    |
| Page Break by Job?                     | No                          | This option will allow you to page break the report by Job, making it easier to give the reports to Job Supervisors for review.                                                                                                                                                                                                                                                                                                                                 |
| Page Break by Supervisor?              | No                          | This option will allow you to page break the report based on Employee Supervisors, making it easier to distribute to Supervisors for review.                                                                                                                                                                                                                                                                                                                    |
| Page Break by Task?                    | No                          | This option will allow you to page break the report by Task, making it easier to give the reports to Task Supervisors for review.                                                                                                                                                                                                                                                                                                                               |
| Print Inactive Employees?              | No                          | This option will allow you to print information for both Active and Inactive Employees.                                                                                                                                                                                                                                                                                                                                                                         |
| Print Time in Hours and Minutes?       | No                          | InfiniTime reports activity in hundredths of an hour by default. Setting this option to Yes displays activity totals in hours and minutes.                                                                                                                                                                                                                                                                                                                      |
| Show Company Grand Total?              |                             | When set to Yes a total record will be added to the bottom of the report to show total company hours for selected columns.                                                                                                                                                                                                                                                                                                                                      |
| Sort by Employee Number                | No                          | This option will group employees specified by the Employee Filter according to their Employee ID.                                                                                                                                                                                                                                                                                                                                                               |
| Task Grouping Type?                    | None                        | Determines how employees will be grouped by Tasks. When set to None the option is considered disabled and employees will not be grouped by tasks. When set to Employee Default Task employees will be grouped according to their default task as assigned on their employee record. When set to Scheduled Task employees will be grouped according to the task they were scheduled to work in.                                                                  |
| Task Selection Based On:               | Employee Default Task       | This option will allow you to select how the Task filter is used to select employees. By default, tasks tagged on the selection criteria will cause InfiniTime to display employees assigned to the task on the report. Alternatively, selecting 'Worked in Task'' will show employees that worked in the selected task during the chosen date range.                                                                                                           |
| Task Selection Filters Activity?       | No                          | If this option is set to Yes, employee Timecard Records displayed on the report will be filtered according to tagged tasks as follows: 1.) Only employees with hours in the tagged tasks will be displayed on the report. 2.) Only timecard records assigned to the tagged task(s) will be used to calculate totals for display on the report. All other timecard records for employees will ignored when this option is set to Yes.                            |

## Importing Crystal Report Files & Configuring Categories

Due to licensing constraints it is not possible for users to design their own crystal reports for use with InfiniTime. However custom reports are available through Inception Technologies for a fee which varies depending upon the nature of the request. To submit a custom report request please contact your authorized InfiniTime Dealer or Inception Technologies Sales Contact.

When submitting your request please have the following details available if possible:

- If the request involves alterations to an existing report:
- - Describe desired alterations in detail.
  - Provide an example. Examples can be created by exporting the existing report to excel and altering fields and columns to reflect the desired results or by simply printing the report and writing in the alterations.
  - Provide Contact Name, Phone, and Email.
  - Specify Software Version and Registered Company Name.

- If the request is for a new report:
- - Describe in detail all columns and the type of information contained within.
  - Provide an example. Examples can be created within excel from scratch or by using a current report as a reference for the general report layout.
  - Provide Contact Name, Phone, and Email.
  - Specify Software Version and Registered Company Name.

##### Importing Custom Report Files Designed by Inception Technologies

Previously supplied custom reports designed by Inception Technologies can be imported into the InfiniTime Application via the Import Button on the Report Library. This ensures customers who have had custom reports created for them can load them into the application manually if necessary.

To Import a Custom Report:

1. Open the Report Library by clicking on the Report Button on the main toolbar.

![](/img/Rpt034.png)

2. Browse to the report category where the custom report will be added.

![](/img/Exception_Detail.gif)

3. Copy an existing report.

![](/img/ImportReports_02.gif)

4. Highlight the copied report. Click on the Import button which is now displayed.

![](/img/Shift_Summary.gif)

5. Click on the Magnify Glass and browse to the Crystal Report file you would like to import.

![](/img/Audit_Trail.gif)

6. Press OK to import the report.

![](/img/CH10AutoReports.gif)

## InfiniTimeReports: Exporting Reports to a File

InfiniTime reports can be exported in a variety of formats such as Microsoft Word, Microsoft Excel, Adobe PDF and Rich Text. This provides an extra level of flexibility for distributing reports to interested parties. Once exported report files can be attached to an email, archived, or distributed as necessary.

![](/img/System_Monitor_1.gif)

Export Options

A variety of options are available when exporting report files. Many of the options detailed below are not displayed until after the Export File Name has been filled. When exporting reports to a file it is important to note how the file will be retrieved by end users. Available options include email, direct download, FTP transfer, and by accessing the output folder on the InfiniTime Server.

Email

- Report Files can be sent via email by completing the Email Tab on the Reader Address Update form.

Direct Download - Report Files can be downloaded directly from InfiniTime via a Web Browser. To download the report file immediately after generating the report the 'Print Preview' setting must be set to Yes.

FTP Transfer - Report files can be sent via FTP to a remote FTP site. See Sending Export Files Via FTP below.

Output Folder - Report files can be exported directly to the Output Folder in the InfiniTime 7 Program Files Folder on the InfiniTime Server. The user will not be given the option to download the report file directly. To export the report file to the Output Folder on the InfiniTime Server the 'Print Preview' setting must be set to No.

Export File Name - The export file name specified in this field will be included in the name of the report file exported in addition to the time and date of file creation. Do not include a path or file extension in this field.

Export Format - InfiniTime provides four formats for exporting report files. These formats are detailed below.

Adobe PDF (.PDF) - Exports reports in a format compatible with Adobe Acrobat Reader. These report files cannot be edited without PDF Authoring Software and are intended for viewing purposes only. Adobe PDF is the default format used with all InfiniTime Reports and is recommended by Inception Technologies when exporting reports for increased compatibility.

Microsoft Word (.DOC) - Exports reports in a format compatible with Microsoft Word. These report files can be edited directly with Microsoft Word and are intended for light editing and viewing purposes.

Microsoft Excel (.XLS) - Exports reports in a format compatible with Microsoft Excel. These reports can be edited directly with Microsoft Excel and serve multiple purposes due to the flexibility of Microsoft Excel.\*

Rich Text (.RTF) - Exports reports in a common format compatible with most Rich Text Editors. These reports can be edited directly with document editors compatible with the Rich Text format.

\*Technical Note: Due to some inconsistencies with Crystal Report's handling of advanced reporting functions reports exported as Microsoft Excel files may require manual editing in order for columns to align properly with their headings.

PGP Encryption - Report files can be encrypted according to the PGP algorithm before export. Refer to the [Introduction on PGP Encryption](../Security/Security_Overview.md#sec54_Optional_PGP_Encryption_for_Output_Files) for more information on using this feature.

Sending Export Files Via FTP - Use this feature to automatically transfer the file via FTP (File Transfer Protocol) to a destination of your choice. The following fields will become available and must be filled out. An example is shown below. Keep the items that follow in mind when entering this information.

- A domain name or IP Address can be used in the Host Address Field.
- Do not include the ftp:// prefix in the Host Address Field.
- The Directory field can be left blank if you are uploading to the root of the FTP Site.
- If you wish to upload to a specific folder on the FTP site you must specify the full path using a preceding forward slash ( / ) as shown in the image below.
- The Login Name can be a Local Windows Account, a Domain Account, or Anonymous. Enter the Login Name in one of the following formats:

Local Windows Accounts:

![](/img/QS_Chapter1_09.gif)

1. Enter the Host Address There are two valid formats for the host address field as detailed below. Do not include the ftp:// prefix in this field.

| Valid Host Address Formats |                    |
| -------------------------- | ------------------ |
| Format Type                | Example            |
| IP Address                 | 192.168.1.20       |
| Domain Name                | www.InfiniTime.com |

2. Enter the Directory. Remember to include a preceding forward slash as shown.

3. Enter the Login Name in the following format: "HOSTNAME\USER" For Example if your FTP Server's hostname is FTPSERVER and the user you wish to connect as is FTPUSER then you would enter the following:

FTPSERVER\FTPUSER

4. Enter the user's password.

5. Specify the port to use when connecting to the FTP Server. This does not generally need to be altered.

Domain Accounts:

![](/img/Department_Payroll_Detail.gif)

1. Enter the Host Address. There are two valid formats for the host address field as detailed below. Do not include the ftp:// prefix in this field.

| Valid Host Address Formats |                    |
| -------------------------- | ------------------ |
| Format Type                | Example            |
| IP Address                 | 192.168.1.20       |
| Domain Name                | www.InfiniTime.com |

2. Enter the Directory. Remember to include a preceding forward slash as shown.

3. Enter the Login Name in the following format: "DOMAIN\USER" For Example if your FTP Server's domain is InfiniTime and the user you wish to connect as is FTPUSER then you would enter the following:

InfiniTime\FTPUSER

4. Enter the user's password.

5. Specify the port to use when connecting to the FTP Server. This does not generally need to be altered.

Anonymous User:

![](/img/image463.gif)

1. Enter the Host Address. There are two valid formats for the host address field as detailed below. Do not include the ftp:// prefix in this field.

| Valid Host Address Formats |                    |
| -------------------------- | ------------------ |
| Format Type                | Example            |
| IP Address                 | 192.168.1.20       |
| Domain Name                | www.InfiniTime.com |

2. Enter the Directory. Remember to include a preceding forward slash as shown.

3. Enter Anonymous as the Login Name.

4. Leave the password field blank.

5. Specify the port to use when connecting to the FTP Server. This does not generally need to be altered.

Technical Note: Microsoft IIS includes an option to permit only anonymous connections to an FTP Site. If this option is checked as shown below only anonymous connections to the FTP Site will be allowed. This means ANYONE can access the payroll export file. This option should be unchecked and it should be confirmed that a login is required to gain read or write access to the directory where the Payroll Export File will be uploaded. Please contact your Information Technology Personnel for assistance with checking file permissions on your FTP Site.

![](/img/Attendance_Review.gif)

Technical Note: InfiniTime attempts to connect to the FTP Site to validate the Login ID, Password, and Directory when the OK Button is clicked on the Payroll Export Update Form. If InfiniTime is unable to successfully connect to the FTP Site with the provided login information, or if the specified directory does not exist, an error will be displayed.

## Commonly Used Reports

The following reports are the most commonly used reports within the InfiniTime Application. Additional information on each report can be viewed by clicking on the report name below..

Employee List

- Displays Employee ID, Employee Name, Department, Job Title, Date of Hire, Badge ID, Login ID, and Clock ID for employees included in the Report Selection Criteria Employee Filter. Useful For:

* Printing a list of active employees within the InfiniTime Database
* Testing Filter Settings to ensure only desired employees are included in the Filter
* Printing Employee Hire Dates
* Viewing all employees to which a given supervisor has access, according to the supervisor's Security Filter.

- This is accomplished by logging into the Manager Module as the supervisor in question and running the Employee List report without an employee filter. The Security Filter set for the Supervisor will be applied to the report such that only employees the Supervisor can see will be displayed on the report.

Employee Exception Summary - Displays each exception during the selected date range as a header record, with individual employees who triggered the exception along with the number of instances each employee had for the respective exception as detail records. Useful for determining the frequency of specific exceptions across the entire organization and / or specific departments / groups of employees.

Employee Exceptions Detail - Displays Employee Names and Employee ID Numbers as a header with each exception during the selected date range as a detail record. Useful for viewing all exceptions during a specific date range or for viewing all exceptions for specific employee(s) during a given date range.

Employee Without Reviewed Timecards - Displays the name of Employees with Unreviewed Timecards according to report options. Report options can be configured to require one or more reviews as well as review by the employee, the employee's supervisor, or both. Useful for ensuring all employee timecard records have been approved by an employee's supervisor and / or by the employee prior to running payroll.

Payroll Detail

- Displays Employee Worked Hours and Other Activity Hours / Amounts for the selected date range. Totals are calculated for each date with hours. Wage Totals are calculated based on Employee Policy, Default Wage, and Alternate Wage configuration.

Payroll Summary

- Displays Employee Worked Hours and Other Activity Hours / Amounts for the selected date range. Totals are calculated for the entire date range for each Worked Hours Type / Other Activity Type in the selected date range. Wage Totals are calculated based on Employee Policy, Default Wage, and Alternate Wage configuration.

Attendance Review

- Designed as a periodic employee performance report, the Attendance Review Report is useful for identifying trends in employee performance (IE: Tardy, Absent, Early Departure, consistent requests for personal or sick time on a certain day of the week or month etc.). Depending on how the report options are configured, the attendance review report can show the individual calendar days on which an employee 1.) Worked 2.) Did not work 3.) Had Other Activity 4. Had Exceptions. Additionally, the report also shows the total number of worked days and the total number of hours associated with schedule related exceptions such as Absent, Tardy, Early Departure etc. It is important to note that the Attendance Review report is based on a comparison of the employee's schedule hours, worked hours, and the resulting exceptions. If exceptions and / or employee schedules are not configured the capabilities of this report are reduced.

Postable Schedule

- Designed as a printable weekly schedule report, the Postable Schedule report is ideal for posting employee schedules in advance. The postable schedule report supports single working periods, multiple working periods in different departments, and Other Activity Schedules such as Vacation Time. Scheduled Hours for each employee are also totaled and displayed on the report.

Activity Summary

- Displays the total number of hours by Worked Hours / Other Activity Type for each employee with Timecard Activity during the selected date range.

Timecard Detail With Weekly Totals - Displays the total number of hours by Worked Hours / Other Activity Type for each date for each employee with Timecard Activity during the selected date range. Hours are totaled on a weekly basis. This report is ideal for regular review of employee hours on a weekly basis..

Timecard Summary

- Displays total Regular Hours, Break Hours, OT1 Hours, OT2 Hours, OT3 Hours, OT4 Hours, Other Hours, and Other Amount for the selected date range for each employee with Timecards during the selected date range.
