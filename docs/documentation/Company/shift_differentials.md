### Shift Differentials

Shift differentials can be configured in order to compensate employees
for working undesirable shifts. InfiniTime
provides incredible flexibility when configuring shift differentials through
multiple payment methods, as configured in the policies, and various differential
pay options. These options are outlined below. Additional details on the
use and configuration of Shift Differentials can be found in the [Scheduling Section of this
document.](../Scheduling/Scheduling.md#dif01_Shifts_for_Differential_Purposes)

![](/img/clip_image012.jpg)

These fields will allow you to assign a differential pay based on the
type of hours.

Differential Pay

- This drop down box allows you to select the type of pay.  The
  options are rate, amount, and percentage.

![](/img/HoursMapping13.gif)

Amount - Selecting
amount specifies that the value entered into the differential pay amount
field is a dollar value, which will be added to the employees base wage
as specified in the employees record.

Example:

Employee Base Wage: $15.00

Differential Amount: $1.00

Total Hourly Differential Pay Rate: $16.00

![](/img/JobCosting_Config_22.gif)

Percent - Selecting
percent specifies that the value entered into the differential pay amount
field is a percentage value, which will be multiplied by the employees
base wage to determine the additional amount paid during differential
time.

Example:

Employee Base Wage: $10.00

Differential Percent: 20%

Additional Differential Pay Amount: $2.00

Total Hourly Differential Pay Rate: $12.00

![](/img/clip_image020.jpg)

Rate -
Selecting rate specifies that the value entered into the differential
pay amount field is a dollar value, which will be considered the total
hourly pay during differential time. The Employee's base wage is ignored
when a rate is specified. All employees will receive the same pay rate
when they qualify for differential time.

Example:

Employee Base Wage: $15.00

Differential Rate: $18.00

Total Hourly Differential Pay Rate: $18.00

![](/img/clip_image022.jpg)

Differential Pay
Amount - This field will allow you to enter the amount of the pay
according to the selected differential pay type, for example, if you had
selected amount for differential pay a dollar amount would be entered
into this field. Refer to the above examples for usage.

![](/img/sched11.gif)

Before Shift Grace
Differential (Optional)â This is the amount of time the employee
has before the shift starts to clock in and be considered to be in that
shift for differential purposes.

After Shift Grace
Period (Optional)â This is the amount of time the employee has
after the shift has started to clock in and still be considered in that
shift for differential purposes.

Map Shift Hours
To â Allows versatile shift differential payment methods. Shift
Differential mapping makes it possible to pay shift differential hours
according to the hours on another shift. Shift mapping is subject to the
following requirements and conditions:

Two Shifts must be configured for differential.
Use for differential must be checked for each shift.

1 Primary Differential Shift

1 Secondary Differential Shift

The Primary differential shift contains the
map to setting, which points to the Secondary Differential Shift. The
employee must work the hours as defined on the Primary Differential Shift
in order to qualify for differential payment. Differential hours will
be paid according to the Differential Pay and Differential Amount settings
defined on the Secondary Differential Shift. Differential Pay and Differential
Amount Settings can be left blank on the Primary Differential Shift.

The Secondary Differential Shift determines
hours to be paid as differential. When an employee qualifies for differential
payment on the Primary Differential Shift the employee will be paid according
to the hours on the Secondary Differential Shift.

_Examples_:

_Note_:
Examples are presented by Shift Differential Pay Method as defined within
the Schedule settings / Rules in the company policy.

![](/img/EmployeeProfile_032.png)

Secondary Differential
Shift

Start Time: 2:00 PM

End Time: 10:00 PM

![](/img/CH3_CompInfo3.gif)

Zone

- Zone pays shift differential according to the period an employee
  is working. The employee in question worked from 4:00 PM to 12:00 AM.
  By working 4:00 PM to 8:00 PM the employee qualifies for the mapped shift
  differential. Of the total hours worked six hours (4:00 PM â 10:00 PM)
  qualify for differential payment and two hours (10:00 PM â 12:00 AM) are
  considered regular time, or outside of the differential period.

Employee Work Hours: 4:00 PM â 12:00 AM

Employee Base Wage: $15.00

Differential Amount: $1.00

Total Hourly Differential Pay Rate: $16.00

Qualifying Differential Hours: 4:00 PM â
10:00 PM (6 Hours)

Regular Pay Hours: 10:00 PM â 12:00 AM (2
Hours)

Total Differential Pay: $16.00 \* 6 Hours
= $96.00

Total Regular Pay: $15.00 \* 2 Hours = $30.00

Total Pay: $126.00

Clock
In - Clock in pays shift differential according to where the employee
clocks in. The employee in question clocked in at 4:00 PM, which falls
within a period defined for differential payment. All hours are paid at
the differential rate defined in the Secondary Differential Policy since
mapping is being used.

Employee Work Hours: 4:00 PM â 12:00 AM

Employee Base Wage: $15.00

Differential Amount: $1.00

Total Hourly Differential Pay Rate: $16.00

Qualifying Differential Hours: 4:00 PM â
12:00 PM (8 Hours)

Regular Pay Hours: 0

Total Differential Pay: $16.00 \* 8 Hours
= $128.00

Total Regular Pay: $15.00 \* 0 Hours = $0.00

Total Pay: $128.00

Clock
Out - Clock out pays shift differential according to where the
employee clocks out. The employee in question clocked out at 12:00 AM,
which does not fall within a period defined for differential payment.

Employee Work Hours: 4:00 PM â 12:00 AM

Employee Base Wage: $15.00

Differential Amount: $1.00

Total Hourly Differential Pay Rate: $16.00

Qualifying Differential Hours: 0 Hours

Regular Pay Hours: 8

Total Differential Pay: $16.00 \* 0 Hours
= $0.00

Total Regular Pay: $15.00 \* 8 Hours = $120.00

Total Pay: $120.00

Majority

- Majority hours pays shift differential according to where the
  employee spent the most hours. By working from 4:00 PM to 8:00 PM the
  employee in question qualifies for the mapped shift differential, which
  provides the employee with 6 hours differential time and 2 hours regular
  time under zone circumstances. In this scenario, the employee has majority
  hours in differential time. All hours are paid at the differential rate.

Employee Work Hours: 4:00 PM â 12:00 AM

Employee Base Wage: $15.00

Differential Amount: $1.00

Total Hourly Differential Pay Rate: $16.00

Qualifying Differential Hours: 4:00 PM â
12:00 PM (8 Hours)

Regular Pay Hours: 0

Total Differential Pay: $16.00 \* 8 Hours
= $128.00

Total Regular Pay: $15.00 \* 0 Hours = $0.00

Total Pay: $128.00
