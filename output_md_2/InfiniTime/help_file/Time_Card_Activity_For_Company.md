xml version="1.0" encoding="utf-8"?





Time Card Activity For Company




# Time Card Activity For Company

The time card activity table is where a supervisor can view and edit time card activity for the employees, and also review time cards before the payroll process.

![](images_2/CH7_Timecard1.gif)

The time card activity table is broken down in two pieces:

1. The list of employees.
2. The activity of the employees.

List of Employees

![](images_2/CH7_Timecard2.gif)

In the list of employees you can highlight the employee you want to see the activity for, you can also use the search function to search for an employee.

Activity of the Employee

![](images_2/CH7_Timecard3.gif)

In the Activity section you will see the punches of the employee for a selected date range.  The following is a description of all the buttons and functionality of the timecard activity table:

Range - This is the date range selected of the activity that is being viewed.  You can use the drop down menu to select from different ranges of time.  By default the range is the current pay period of the policy that the employee is assigned to.

![](images_2/Exception-button.gif) - Displays a list of all exceptions occurring on the selected day as shown below. Remember, exceptions are conditions that can be tracked by InfiniTime. When an employee meets a condition they will be flagged with the corresponding exception. InfiniTime offers multiple exceptions for detailed employee performance tracking. However only Missed Punch and Overtime are available without schedules as it is not possible for InfiniTime to determine if an employee is late or early without knowing when they are due to arrive.

![](images_2/BrowseCEM_DateAssociatedTo.gif)

![](images_2/Purge_button.gif) - This feature allows the user to delete timecard activity for this employee that is old and no longer useful.  Selecting this button brings you to a screen where you are asked to enter a Date Limit.  This limit defines the date from which all-previous records for the company will be deleted.

![](images_2/quick_punch_button.gif) - The Quick Button inserts identical punches over a specified date range.  Selecting this button will bring up the Quick punch Window.

![](images_2/Re_calculate_button.GIF) - This feature allows the user to recalculate timecard activity for the employee activity.  Recalculation should be done if you make any changes to the policies, inserting, changing, or deleting a Holiday.

![](images_2/review_button.gif) - Selecting this button will bring up the Supervisor Review Window, which allows the user to select one or more employees for review of their timecard activity.

![](images_2/Insert-button.gif) - The insert button will insert a row in the timecard activity so you can enter time for the employee.

![](images_2/filter-button.gif) - The filter button will allow you to filter the screen information by employees, departments, and exceptions, making easier for a supervisor to fix and edit time cards.

![](images_2/CH7_Timecard4.gif) - The Grand Totals Row displays a grand total of employee hours for the specified date range. It should be noted that the Grant Totals Row is always the last row in the grid and will be displayed on the last page if there are multiple pages of timecard activity.

![](images_2/ScheduleTimecar.gif) - The Schedule Column of the grid displays the schedule or shift an employee worked on a specific day. If an employee is assigned to multiple shifts the software will identify the shift the employee is working based upon the shifts start time and grace periods configured on the employee's policy.

Displaying Job Costing Information on the Company Timecard Table

Job Costing is disabled by default within InfiniTime as not all companies track Job or Tasks for employees. Instructions for adding Job and Task information to the Company Timecard Table are available in the [Job Costing Configuration](/InfiniTime/help%20file/Job_Costing_Configuration.md#JobCostInfo) section of this manual.