---
title: "Accrual Calculations Update Form"
description: "Guide to updating and managing accrual configurations for different accrual categories such as Personal, Sick, and Vacation Time."
---

Accrual Calculations Update Form

# Accrual Calculations Update Form

The Accrual Calculations Tab displays a list of any accruals configured for the Accrual Type being viewed. Separate accruals must be configured for each individual accrual category such as Personal Time, Sick Time, or Vacation Time.

![](/img/AccrualTypeDetailsUpdateForm.jpg)

Ok â Exits the window and saves any changes to the database.

Cancel â Exit the window without saving changes.

Help â View Help documentation for the current screen.

Type:  Descriptive name of the Accrual. Entered during creation.

Effective Date: This date is when this accrual will begin accruing.

Stop Accruing Date: This date is when this accrual will stop accruing.

Start At Amount:  Enter the number of hours that your employees immediately receive upon the completion of their probation.

Start Accruing after Hire Date Amount:  This is considered an employeesâ probation period or trial time.  Enter the number of days that must pass from the employeesâ date of hire before they can start receiving this type of accrual. This is optional and only needs to be entered in the first Accrual Type of a class, or the Accrual Type that starts at 0 years.

Accrue Amount:  This is the first part of the accrual formula.  The accrual rate can be entered from whole hours down to 1/1000000000th of an hour. Leaving a zero in this field will cause the system not to accrue any time.

For Every Amount:  This is the second part of the accrual formula.  InfiniTimeâ¢ accrues per Hour, or fractions of an hour, Day, or fractions of a day, and in Month(s).  In the For Every Amount field, enter the amount of time units that must pass in order for the system to accrue the number of hours specified in the Accrue Amount Field.

For Every Unit: Select the unit to be used for the accrual formula. Use the drop down arrow to select Hour(s), Day(s), or Month(s).A detailed explanation of each For Every Amount Unit is listed below.

Hour(s) - When the Hour(s) Unit is selected, employees will be awarded accrual hours each time they work a specified number of hours. Common uses for this unit type include accruing hours each time an employee works 40, 80, 120, or 160 hours. Regular and Overtime Hours count toward these calculations. Other Activity Hours can also be set to count toward these calculations by checking the 'Count as Hours Worked for Accrual Calculations' option on the Other Activity Type Update Form.

Day(s) - When the Day(s) Unit is selected, employees will be awarded accrual hours every so many days as specified by the For Every Amount, starting from the start of the accrual period. It is important to note that this calculation counts calendar days, not working days. Common uses for this unit type include accruing hours every 7 or 14 days.

Month(s) - When the Month(s) Unit is selected, employees will be awarded accrual hours every so many months as specified by the For Every Amount, starting from the start of the accrual period. It is important to note that hours are awarded each month on the same day, according to the start of the Accrual Period. If the same day does not occur for a given calendar month, then accrual hours are awarded on the last day of the month. [Detailed examples](AccrueByMonthExamples.md) are provided for the 'Accrue X Hours for every 1 Month' accrual calculation.

Reset Type:  Select when you would like InfiniTimeâ¢ to reset the accruals.

- Calender Year â InfiniTimeâ¢ will reset on January 1st of each year.
- Anniversary â InfiniTimeâ¢ will reset on the employees date of hire.
- Fiscal Year â InfiniTimeâ¢ will reset on a specific day set forth by the company, by selecting the Fiscal month and Fiscal day.

Stop At Amount:  Enter the maximum amount of time an employee can accrue. Once this level has been reached, no further time will be accrued.

Hours Needed to Qualify (Optional): This range of hours gives you the ability to set the minimum and maximum hours for calculating accruals.

Overflow Info: Two options are available when an accrual bucket has reached the Stop At Amount. InfiniTime can ignore any further accrued hours, or they can be allocated to a separate accrual. Overflow is used to choose the separate accrual for excessive hours over the configured limit.

Maximum Negative Accrual: Enter the maximum negative amount of accruals allowed, this allows the use of accrued time before it has been accrued.

End Of Cycle Bonus: Enter amount of hours given to the employee as bonus at the end of the cycle. The end of the cycle varies depending on the reset type chosen.

- Calendar Year: Accruals Reset on January 1.
- Hire Date: Accruals Reset on the employees Hire date.
- Fiscal Year: Accruals Reset on the Specified Fiscal Month and Day.

Carry Over: Check this box if the accrual can be carried over to the next cycle.

Carry Over Expires In: Enter the number of days for the Carry Over Hours to expire from use after the cycle end.

Maximum of Hours: Enter the maximum amount of accrued time that can be carried over to the next cycle if the hours value is left blank then all of the hours accrued will carry over.

Do Not Allow Accrued Time To Be Used: When this option is selected, Accrued Hours cannot be used or deducted.

Do Not Allow Time To Be Used In Year Accrued: When this option is selected, accrued hours cannot be used or deducted on the year they where accrued.  Useful is you want to accrue time for one year then not being able to use it until the following year and it carries over for the following year.

Continue to Accrue To Stop At Amount After Time is Used: When this option is selected, the Stop At Amount setting determines the maximum remaining hours, or the maximum number of accrual hours available for use at one time instead of the maximum number of hours that can be accrued over the accrual period. In this way, employees may accrue hours up to the Stop At Amount, use Accrued Hours, and then continue to accrue time up to the Stop At Amount. The Continue to Accrue to Stop At Amount after time is used feature is intended for use with Accrual Calculations that award accrual hours in increments over time or according to hours worked. Accrue 3.33 Hours for every 1 Month and Accrue 0.01923 Hours per 1 Hour are examples of qualifying accrual calculations.
