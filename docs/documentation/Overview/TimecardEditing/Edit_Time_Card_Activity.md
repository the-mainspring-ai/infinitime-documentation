---
title: "Edit Time Card Activity Guide"
description: "Step-by-step instructions on how to insert punches and edit time card activities using the system's buttons and forms."
---

Edit Time Card Activity

# Edit Time Card Activity

![](/img/quick_punch_button.gif)

Inserting Punches using the ![](/img/CH7_Timecard3.gif) button

- 1. Click on the ![](/img/CH7_Timecard5.gif) button.
  2. In the activity window a new line will appear filled out with the pair punches for the employee.

![](/img/CH7_Timecard7.gif)

- 3. Fill in the information of the date and punch information.  To maneuver across the record you can Tab over the fields like if you were using a spread sheet
  4. Once you fill the required information hit Enter to save the record.

Inserting Punches using the ![](/img/quick_punch_button.gif) button

- 1. Click on the ![](/img/CH7_Timecard7.gif) button.
  2. The Quick Punch Update Form will come up

![](/img/CH7_Timecard3.gif).gif)

Quick Punch Update Form:

Description - The description displays information regarding the employee for which activity is being inserted and the employee inserting activity. This information is recorded in the audit trail.

Note: The description information will not reflect employees specified by the employee filter. Though an audit trail entry will be recorded for each employee whose timecard activity is altered by the quick punch transaction.

Date Range - Select the date range that you wish to insert the Quick punches.  *If the Quick punch is for one day only, then the start and end dates will be the same.*

Punch Type - Use the drop down menu to select the type of punch, choose from regular punch, schedule punch, single punch, or other activity.

Regular Punch - Inserts a set of punches. The first time specified is the clock in time, while the second time specified is the clock out time.

Scheduled Punch - Inserts punches according to the employees schedule. For example if the employee is scheduled to work from 8:00 AM to 5:00 PM InfiniTime will automatically clock the employee in at 8:00 AM and out at 5:00 PM.

Single Punch - Inserts a single punch. InfiniTime automatically determines the punch type based upon the timecard activity already present on the date where the single punch is inserted.

Other Activity - Inserts other activity such as holiday time, vacation time, sick time, and personal time.

Use Default Department - if this is checked the punches will be posted using the default department of the employee, if not checked you can choose a department using the magnify glass or typing in the department name to post those punches.

Use Default Job - if this is checked the punches will be posted using the default Job of the employee, if not checked you can choose a Job using the magnify glass or typing in the Job name to post those punches.

Use Default Task - if this is checked the punches will be posted using the default Task of the employee, if not checked you can choose a Task using the magnify glass or typing in the Task name to post those punches.

Start Time - Select the time that the quick punch will clock the employee in at.

End Time - Select the time that the quick punch will clock the employee out at.

Duration - The number of hours that will be totaled is shown here.

Add Duplicate Punches - Unless this box is checked InfiniTime will compare the punches being inserted to those already in the database when performing a Quick Punch. Any duplicate punches will be ignored. For example the image below shows an employee working from 7:30 AM to 5:00 PM on 1/17/2008. If a supervisor were to attempt to insert a punch on 1/17/2008 from 7:30 AM to 5:00 PM using quick punch then the punches would not be inserted unless Add Duplicate Punches was checked.

![](/img/CH7_Timecard5.gif)

Clock Out if Clocked In - If this is checked it will only insert an out punch for that day and in/out for the rest of the date range. This option is only displayed when performing a single punch.

Weekday Only â If this is checked it will only insert punches for weekdays only and not the weekend, Saturday and Sunday.

Description - This is an audit description of the insertion of punches.

![](/img/filter-button.gif) - The filter button will allow you to add punches to multiple employees at a time.  You can filter which employees will get the pair of punches either by departments, groups, or by tagging multiple employees.
