xml version="1.0" encoding="utf-8"?





Dates Tab




# Dates Tab

The dates tab displays all holidays that have been configured for the specified Holiday Schedule Type.

![](/img/image-404.png)

Insert Displays the Master Holiday Update form. Used to insert a new holiday type. Each holiday that will be assigned to the specified Holiday type must be configured individually using this option. InfiniTime will automatically add other activity hours for employees who meet requirements for the holiday. A description of each field and feature is provided below.

![](/img/image-404.png)

Holiday Options

Name:  Enter the Name of Holiday.

Date:  Enter the Date of Holiday. For a given holiday type, only one holiday may exist on each date. Attempts to insert more than one holiday on a single date will cause a warning to be displayed indicating the Employee Holiday Date must be unique.

Deduction Type: Select the type of deduction.  If Accrual is selected an Accrual Name must be selected for posting.

![](/img/image-404.png)

Other Activity Type Specifies the Other Activity Type which will be used to insert hours for the selected date. The same activity type is generally used for all Holiday Hours. IE: Holiday Time

All Worked Hours Are Holiday Pay Determines whether employees will automatically receive pay for the holiday or if they are required to work on the holiday before receiving hours. If this option is set to No employees will automatically receive hours for the holiday if they meet any requirements defined by other Holiday Options. If this option is set to Yes employees must punch in and out on the selected date in order to receive holiday pay.

Other Activity Hours When All Worked Hours Are Holiday Pay is set to No employees will automatically receive the number of hours entered in this field. (IE: 8)

Max Other Activity Hours When All Worked Hours Are Holiday Pay is set to Yes employees will not receive holiday pay for hours worked in excess of the value entered in this field.

Worked Holiday Rate Multiplier Enter a rate for holiday hours in this field. Holiday hours will be calculated at this rate for the purpose of Gross Payroll Reports within the InfiniTime Application.

Day Before Holiday Must Be Worked If this option is set to Yes employees must work the day before the holiday in order to receive holiday hours. If employees do not have a default schedule defined then Day Before is literal if the holiday is on a Monday the employee must work the day before the holiday (Sunday) in order to receive Holiday Hours. If employees have a default scheduled defined then Day Before refers to the first scheduled day prior to the holiday.

\*Day After Holiday Must Be Worked If this option is set to Yes employees must work the day after the holiday in order to receive holiday hours. If employees do not have a default schedule defined then Day After is literal if the holiday is on a Monday the employee must work the day after the holiday (Tuesday) in order to receive Holiday Hours. If employees have a default scheduled defined then Day After refers to the first scheduled day after to the holiday.

\*Note: The Day Before Holiday Must be Worked and Day After Holiday Must be Worked settings cannot be enabled for two consecutive holidays such as Thanksgiving and The Day After Thanksgiving. In this case enable Day Before Holiday Must be Worked for the first holiday (Thanksgiving) and Day After Holiday Must be Worked for the second holiday (The Day After Thanksgiving.)

++ \*\*Holiday Starts Day Before Setting this option to Yes provides the user with the ability to start holiday pay at a certain time on the day before the holiday. This is commonly used for night shifts.

++ \*\*Holiday Ends on Holiday Setting this option to Yes provides the user with the ability to end holiday pay at a certain time on the day of the holiday.

++ \*\*Holiday Ends Day After Setting this option to Yes provides the user with the ability to end holiday pay at a certain time on the day after the holiday.

++ \*\* Holiday Based on Employee's Schedule - If this option is set to Yes the holiday start and end times will automatically be adjusted to match the employee's schedule for the date of the holiday. The employee will then receive Holiday Hours for all hours worked between the Start and End times of the holiday, as defined by the employee's schedule. If the employee does not report to work for the holiday date, the employee will receive Holiday Hours according to the number of working hours scheduled on the holiday date. Examples are provided below.

Example: Holiday Based on Employee's Schedule: Employee Reports to Work

Holiday: Friday, December 24, 2010.

Employee's Schedule: Monday to Friday, 8:00 AM to 4:00 PM

In this scenario, the holiday would start at 8:00 AM and end at 4:00 PM on 12/24/2010. The employee would receive holiday hours for any hours worked between 8:00 AM and 4:00 PM on 12/24/2010.

Example: Holiday Based on Employee's Schedule: Employee Has the Day Off and does not report to work

Holiday: Friday, December 24, 2010.

Employee's Schedule: Monday to Friday, 8:00 AM to 4:00 PM

In this scenario, the holiday would start at 8:00 AM and end at 4:00 PM on 12/24/2010. Since the employee did not report to work, they automatically receive Holiday Pay for 8 Hours.

\*\*Note: Settings that alter the starting and ending day of the holiday are disabled when 'All Worked Hours are Holiday Pay is set to No. The start and end of a holiday can only be altered when employees are required to work the only in order to receive Holiday Pay.

++Note: By default, without any changes to settings that alter the starting and ending day of the holiday, all Hours Between 12:00 AM and 11:59 PM on the date of the holiday will be paid as Holiday Time when 'All Worked Hours are Holiday Hours' is set to Yes.

.

^^Employee Required to Work - When set, this option requires employees to work a certain number of hours over a specified number of days or weeks prior to the holiday in order to receive Holiday Pay.  It is important to note that the 'Days' and 'Weeks' settings operate differently. The 'Days' selection averages hours over a specified number of days starting with the day immediately before the date of the holiday. The 'Weeks' selection averages employee hours worked over a specified number of weeks starting with the week before the date of the holiday. Refer to the note below for an illustration.

^^Average Hours Average hours can be set to calculate average hours over a number of days prior to the holiday or over a number of work weeks prior to the holiday. It is important to note that the 'Days' and 'Weeks' settings operate differently. The 'Days' selection averages hours over a specified number of days starting with the day immediately before the date of the holiday. The 'Weeks' selection averages employee hours worked over a specified number of weeks starting with the week before the date of the holiday. Refer to the note below for an illustration.

^^Note: The images below illustrate the difference between a 3 Week Average and a 21 Day Average. Days shaded in yellow represent days which will be included in the average hours calculation. The boxed date indicates the date of the holiday. Notice how the 21 Day Average includes the days immediately before the date of the holiday that fall during the same week of the holiday.

![](/img/image-404.png)                   ![](/img/image-404.png)

Example: Average Hours by Days

![](/img/image-404.png)

If Average Hours is enabled InfiniTime will average employee working hours for a number of days or weeks prior to the holiday according to the 'Average the Past' Field and the Days or Weeks Drop Down Menu. InfiniTime will then automatically insert the calculated average for the Holiday. The number of hours entered into the Other Activity Hours field will serve as the maximum number of hours an employee can receive. Two Examples are illustrated below with the following settings:

| Average Hours | Yes |
| Days to Average | 21 |
| Other Activity Hours | 10.00 |
| All Hours Worked are Holiday Pay | No |

| Day | Hours Worked: Scenario 1 | Hours Worked: Scenario 2 |
| 11/5 | 8.25 | 11.50 |
| 11/6 | 8.00 | 11.25 |
| 11/9 | 8.00 | 12.00 |
| 11/10 | 6.50 | 12.00 |
| 11/11 | 6.20 | 8.50 |
| 11/12 | 7.50 | 11.50 |
| 11/13 | 8.00 | 12.00 |
| 11/16 | 8.55 | 12.00 |
| 11/17 | 9.00 | 12.50 |
| 11/18 | 8.00 | 11.00 |
| 11/19 | 8.00 | 11.00 |
| 11/20 | 8.00 | 12.00 |
| 11/23 | 8.25 | 12.00 |
| 11/24 | 7.50 | 8.00 |
| 11/25 | 8.02 | 8.50 |
| Average | 7.85 | 11.05 |
| Friday (Holiday) | 7.85 | 10.00 |

Example: Average Hours by Weeks

![](/img/image-404.png)

| Average Hours | Yes |
| Weeks to Average | 3 |
| Other Activity Hours | 10.00 |
| All Hours Worked are Holiday Pay | No |

| Day | Hours Worked: Scenario 1 | Hours Worked: Scenario 2 |
| 11/2 | 8.25 | 11.50 |
| 11/3 | 8.00 | 11.25 |
| 11/4 | 8.00 | 12.00 |
| 11/5 | 6.50 | 12.00 |
| 11/6 | 6.20 | 8.50 |
| 11/9 | 7.50 | 11.50 |
| 11/10 | 8.00 | 12.00 |
| 11/11 | 8.55 | 12.00 |
| 11/12 | 9.00 | 12.50 |
| 11/13 | 8.00 | 11.00 |
| 11/16 | 8.00 | 11.00 |
| 11/17 | 8.00 | 12.00 |
| 11/18 | 8.25 | 12.00 |
| 11/19 | 7.50 | 8.00 |
| 11/20 | 8.02 | 8.50 |
| Daily Average | 7.85 | 11.05 |
| Friday (Holiday) | 7.85 | 10.00 |