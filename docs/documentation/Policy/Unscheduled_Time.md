---
title: "Unscheduled Time Rounding Rules in InfiniTime™"
description: "Overview of how InfiniTime™ handles rounding for unscheduled time punches and the importance of enabling all rounding types for accurate time tracking."
---

# Unscheduled Time

![](/img/rOUNDING_mETHOD.gif)

Some companies have rules regarding how fractions of hours are calculated. These rules apply to the amount of hours between the clock-in and clock-out punches and are reflected in the various reports InfiniTimeâ¢ generates. The InfiniTimeâ¢ program allows you to enter punch specific rounding rules for each punch type (i.e. clock in, break, clock out).

It is strongly recommended to enable all rounding types, when using rounding. Specifically, using Clock in and Clock Out unscheduled rounding without using Break rounding is not recommended. This scenario can cause confusion because the rounding calculation changes multiple times throughout the day as employees punch in and out. In some specific cases this type of rounding can also result in an additional minute of pay due to rounding configuration.

_Please note_: fractions of calculated hours appear as hundredths or tenths of an hour.

No Rounding:  This selection calculates the fraction to the nearest hundredth of an hour;  which is the InfiniTimeâ¢ default.  In this selection, no rounding takes place.

Tenth Hour:  This selection rounds the calculated hours to the nearest tenth of an hour.

_Example_: An employee punches in at 8:00 AM. He punches out at 2:02 PM. The resulting total is 6.12 rounded to 6.1 hours where the 2:02 PM punch is rounded to 2:00 PM.

1/4 Hour:  This selection will round calculated hours to the nearest 1/4 hour, centered on 7 minutes back, and 8 minutes forward.

_Examples_:

- 8 minutes forward â An employee punches in at 8:00 AM. They punch out at 3:08 PM. The resulting total is 7.25 hours rounding the 3:08 PM to 3:15 PM.
- 7 minutes backward â An employee punches in at 8:00 AM. They punch out at 3:07 PM. The resulting total is 7.0 hours rounding the 3:07 PM to 3:00 PM.

All calculated totals will end in .25 or multiples of .25.

Modified 1/4 Hour:  This selection will round calculated hours to the nearest 1/4 hour based on a 5 minute 10 minute split.

_Examples_:

- An employee punches in at 8:09 AM.  They punch out at 4:00 PM.  The resulting total is 8.00 hours.
- An employee punches in at 8:10 AM.  They punch out at 4:00 PM.  The resulting total is 7.75 hours.

All calculated totals will end in .25 or multiples of .25.

Rounding Settings

![](/img/rOUNDING_mETHOD.gif)

Selecting any method other than, âNo Rounding,â will generate a window to allow you to customize the punch rounding.

Round Back If Equal To or Less Than:  Enter the number of minutes that are allotted before the punch is rounded down to the nearest quarter or tenth of an hour (depending on which method you have checked.)

Round Forward If Equal To or Greater Than:  Enter the number of minutes that are allotted for a punch to be rounded up to the nearest quarter or tenth of an hour (depending on which method you have checked.)

Rounding Method

![](/img/Rounding_Rules.gif)

This drop down list allows you to choose how the punches are grouped for your custom rounding.

Each Punch â This Method will round each punch individually.

Net Round Each Punch Pair â This method will round the punches by pairs of clock-in/clock out punches and round the total for the pair.

Net Round Each Day â This method will round the total duration for all of the punch pairs for the day. When Net Round Each Day is selected, the Break and Clock Out tabs will be unavailable as they no longer apply.

_Examples_:

- Quarter hour is checked
- Round Back If Equal To or Less Than = 7 minutes
- Round Forward If Equal To or Greater Than = 8 minutes

Rounding Method = Net Round Each Punch

| Actual Punch                    | Time Calculated per Day (Punched as) |
| ------------------------------- | ------------------------------------ |
| 12:07 PM Clock-Out Unpaid Break | 4.00 Hours                           |
| 12:48 PM Clock-In Unpaid Break  |                                      |
| 4:12 PM Clock-Out               | 3.50 Hours                           |
| Total Time Recorded =           | 7.50 hours                           |

Rounding Method = Net Round Each Punch Pair

| Actual Punch                    | Time Calculated per Day (Punched as) |
| ------------------------------- | ------------------------------------ |
| 12:07 PM Clock-Out Unpaid Break | 4.00 Hours                           |
| 12:42 PM Clock-In Unpaid Break  |                                      |
| 4:12 PM Clock-Out               | 3.50 Hours                           |
| Total Time Recorded =           | 7.50 hours                           |

Rounding Method = Net Round Each Day

| Actual Punch                    | Time Calculated per Day (Punched as) |
| ------------------------------- | ------------------------------------ |
| 12:07 PM Clock-Out Unpaid Break | 4.13 Hours                           |
| 12:42 PM Clock-In Unpaid Break  |                                      |
| 4:12 PM Clock-Out               | 2.87 Hours                           |
| Total Time Recorded =           | 7.00 hours                           |
