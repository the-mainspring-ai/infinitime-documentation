xml version="1.0" encoding="utf-8"?





Other Activity Types




# Other Activity Types

Other Activity Types provide users with an interface for tracking Tips, Personal Time, Holiday Pay, Sick Time, and other forms of non-working paid time. Other Activity can be entered in a monetary or hourly amount. The Other Activity Table is used to create, edit or remove other activity types from the software.

Accessing the Other Activity Types Table

1. Click on Lookups
2. Click on Calculation Setup

![](images_2/ota_(1).gif)

3. Click on Other Activity Types

![](images_2/ota_(2).gif)

Insert â Inserts a new record into the Other Activity Type Table.

Change â Opens the Other Activity Type Update form and permits editing of the selected record.

Delete â Removes the highlighted record from the Other Activity Table.

![](images_2/ota_(3).gif)

Description â Type the name of the Other Activity Type.

Type â Specify whether the Other Activity Type will track a dollar amount or hour amount.

Code Number â The Code Number is a unique identifier within the InfiniTime Database. Each other activity type must have a unique code number in order to set them apart. This code number is used on many hardware terminals to input other activity directly at the clock without accessing the software. All hardware terminals sold by Inception Technologies support this feature except for the Plus Scanner.

Payroll Mapping Number â Enter a mapping number. The payroll mapping number can be the same for multiple other activity types. This number specifies a column in a payroll export file where hours or amounts for the other activity type will be totaled. If more than one other activity type has the same payroll mapping number their values will be added together and totaled in the same column. Mapped Payroll Interfaces provide the customer with the ability to add additional other activity types and move their position within the payroll export on the fly.

The Compupay â Mapped Interface Format is one such payroll interface. An outline of the Compupay - Mapped interface format is provided below. The outline shows a row of headers which represent information that would be exported when performing a payroll export. The resulting export file can then be imported directly into the Compupay application. It is important to understand how Other Activity Types are automatically exported to the appropriate column according to their Payroll Mapping Number. Other Activity Types with Payroll Mapping Number 1 will be totaled in the column labeled Mapped Amount 1. Other Activity Types with Payroll Mapping Number 2 will be totaled in the column labeled Mapped Amount 2.

| Employee ID | Activity Dept Number | Regular Hours | Overtime Hours | Mapped Amnt. 1 | Mapped Amnt. 2 | Mapped Amnt. 3 |

Payroll Mapping Code - Enter a mapping code number. Much like the Payroll Mapping Number, the payroll mapping code can be the same for multiple other activity types, however it is generally used as a unique code to identify an activity type. Payroll Mapping Codes are agreed upon by each company and the firm responsible for their payroll. With this in mind it is not surprising that Payroll Mapping Codes often vary from company to company. These codes are generally known to payroll personnel or the company responsible for your payroll. An example of common payroll codes is provided below.

| Other Activity Type | Example Payroll Mapping Codes |
| Regular Hours | REG, 1 |
| Overtime 1 Hours | OT1, OT, OVT |
| Overtime 2 Hours | OT2, DBL, SAT, WEEKEND |
| Holiday Hours | HOL, HOLIDAY |
| Vacation Hours | VAC, VACATION |
| Sick Time Hours | SICK, SIC, SIK |
| Personal Time Hours | PER, PERS, PERSONAL |

Count As Regular Hours- When this check box is checked hours entered under this other activity type will count as regular hours and count toward overtime.

Count As Day Worked â When this check box is checked, the day where the other activity was inputted will be counted as a worked day. Mostly used to avoid absent exceptions.

Count As Hours Worked for Accrual Calculations - When this check box is checked, Other Activity Hours for the Other Activity Type will be counted toward the Accrue X Hours for Y Hour(s) Accrual Calculation. This makes it possible for employees to earn accrual hours based on Worked Hours (Regular, Overtime 1, Overtime 2, Overtime 3, Overtime 4) and Other Activity Types such as Vacation, Personal Time, Jury Duty, etc.

Exclude From Payroll Export â Placing a check in this box will allow the other activity to be excluded from the payroll export information.

Inactive â Placing a check in this box will make the selection unavailable when inserting an Other Activity punch.