xml version="1.0" encoding="utf-8"?





Overtime Settings




# Overtime Settings

![](/img/OTPay_Percent.gif)

Overtime Buckets: Configuring Daily Overtime, Weekly Overtime, Double Time etc.

Overtime Types One, Two, Three, and Four each have identical settings for Daily and Weekly Overtime Hours. Four Overtime Buckets are available to separate overtime hours paid at different rates. For example many companies use Overtime 1 for Weekly Overtime Paid at time and a half and Overtime 2 for Weekly Overtime paid at Double Time. When selecting an overtime pay method pay attention to the labels on the window as fields are clearly marked with units and descriptive labels.

Daily Overtime If Over Hours:  Hours worked over the displayed number, within a 24hr period, will be flagged as overtime OT1.  If you do not wish to calculate overtime on a daily basis, set this field equal to zero.

Weekly Overtime If Over Hours:  Hours worked over the displayed number, within seven days of the start of the week, will be flagged as OT1 Hours. If you do not wish to calculate overtime on a weekly basis, set this field equal to zero.

Custom Weekly Interval :Many companies with a Bi-Weekly Pay Period require employees to work 80 Hours over a two week period. The Custom Weekly Interval allows users to adjust the number of days in a week for overtime calculations. For example, Setting Weekly Overtime If Over Hours to 80 and a Custom Weekly Interval of 14 days will require employees to work 80 hours in a two week period before receiving Weekly Overtime Hours.

Custom Weekly Start Date: The Custom Weekly Start Date is used as a reference date to start the interval count and should generally be set to a date that matches the start of a pay period. InfiniTime will use the reference date and the Custom Weekly Interval to determine the week used for Overtime Pay Calculations.

Overtime Pay Method: Select the Pay Method used to calculate overtime wages. InfiniTime supports three separate pay methods as listed below. If 'None' is selected in the Overtime Pay Method Drop Down wages will not be calculated for Overtime Hours. If Alternate Wages are configured, It is important to note that InfiniTime will select a base wage based upon where an employee is working before Overtime Wage Payment Methods are applied.

Amount Pay Method

The Amount Pay Method pays employees an additional dollar amount for each hour they work. For example, an amount of 5.00 as shown below will pay employees their default wage plus an additional five dollars per hour for Overtime Hours. An example calculation is below.

Employee Default Wage + Dollar Amount = Overtime Wage

$10.00 + $5.00 = Overtime Wage

$15.00 = Overtime Wage

![](/img/OTPay_Amount.gif)

Percent Pay Method

The Percent Pay Method pays employees an additional percentage of their default wage for each hour they work. For example, a percent wage increase of 50 Percent is equivalent to Time and a Half or 1.5 times the employee's default wage. An example calculation is below.

Employee Default Wage + (Employee Default Wage \* Percent Wage Increase) = Overtime Wage

$10.00 + ($10.00 \* 50%) = Overtime Wage

$10.00 + ($5.00) = Overtime Wage

$15.00 = Overtime Wage

![](/img/OTPay_Rate.gif)

Rate Pay Method

The Rate Pay Method defines a specific wage for overtime hours. When the Rate Pay Method is used employee default wages are ignored and the Overtime Rate is used for overtime hours.

WARNING: The Rate Pay Method is not a multiplier of the employee's wage. Selecting the Rate Pay Method and entering 1.5 as the Overtime Rate will pay the employee $1.50 per hour. Remember, the Employee's default wage is ignored when the Rate Pay Method is selected. The Overtime Rate is entered in dollars per hour and will be used as the employee's overtime wage.

![](/img/OT1.gif)