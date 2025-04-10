xml version="1.0" encoding="utf-8"?





CH22\_Pay Premium Introduction




# Pay Premium Introduction

Premium Pay makes it possible to define Premiums, or bonuses in the form of an increased wage, which are paid to employees based upon the Shift, Department, Job, or Task the employee works on. Premiums can be configured separately for the Regular, Overtime One, Overtime Two, Overtime Three, and Overtime Four hour types. This flexibility makes it possible to meet the needs of a variety of special payment scenarios. It should be noted that, though possible, different Premium Types and Pay Methods are not intended for use in a single company. Pay Premiums are optional and are intended for special scenarios that require specific rules for Medical, Union, and Manufacturing employees. Approximately 20 to 40 out of 100 companies (20% - 40%) require Premium Pay to calculate wages appropriately for employees.

When configuring Premium Pay there are four main tasks that must be performed. Each task is listed and described in detail below.

[1. Identify the Type of Premium.](#1_PremiumType)

[2. Identify the Hour Type(s) eligible for the premium.](#2_HoursTypes)

[3. Identify an appropriate Pay Method.](#3_PayMethod)

[4. Understand how the Premium Hierarchy will affect your pay premium(s)](#4_Hierarchy)

Identifying the Type of Premium

InfiniTime supports five types of premiums, each of which are configured in a separate area of the InfiniTime Application. Employees receive premium pay when they work in a Shift, Department, Job, Task, or Hours Type that has been configured with a premium. Selecting the type of premium is best explained through example. Many hospitals pay employees filling the role of Head Nurse, or the nurse who oversees all other nurses for a given shift, an additional premium. To determine the necessary type of premium the user must understand how the role of head nurse is tracked within InfiniTime. If Head Nurse is a department which employees punch into when they fill the Head Nurse role then the premium would be configured on the Head Nurse department. Similarly, if Head Nurse was a Job or Task then the premium would be configured on the Job or Task respectively.

| Premium Type | Location within InfiniTime | Description |
| Shift Differentials | 1. Click on Lookups, Scheduling Setup, Shifts. 2. Click Change while highlighting an existing shift or click Insert. 3.Check the box labeled 'Used for Differential' 4. Click on the Differential Pay Tab. | Shift differentials are periods of time during which employees receive bonuses in the form of additional pay. Employees working during the hours defined by the shift differential will receive shift differential pay. |
| Department Premiums | 1. Click on the Department Button. 2. Click Change while highlighting an existing department or click Insert. 3. Click on the Premium Pay Tab. | Department premiums are configured separately for each department in InfiniTime. Employees will receive Department Premiums when working in a department configured with a Premium. |
| Job Premiums | 1. Click on Lookups, Employee Setup, Job Costing Lookups, Activity Jobs. 2. Click Change while highlighting an existing job or click Insert. 3. Click on the Premium Pay Tab. | Job premiums are configured separately for each Job in InfiniTime. Employees will receive Job Premiums when working in a Job configured with a Premium. |
| Task Premiums | 1. Click on Lookups, Employee Setup, Job Costing Lookups, Activity Tasks. 2. Click Change while highlighting an existing task or click Insert. 3. Click on the Premium Pay Tab. | Task premiums are configured separately for each Task in InfiniTime. Employees will receive Task Premiums when working in a Task configured with a Premium. |
| Overtime Premiums | 1. Click on Company, Setup, Policies. 2. Click Change while highlighting an existing policy or click Insert. 3. Click on Overtime Rules.  [Refer to Overtime Settings for more information on Overtime Pay Methods.](Overtime_Settings.md) | Overtime Premiums are configured separately for each Overtime Type from OT1 to OT4. Employees will receive Overtime Premiums for any Overtime Type with a premium configured. For example, if a premium is set for OT1, any OT1 hours will be calculated as Premium Pay. |

Identify the Hours Type(s) eligible for the premium

After identifying the Premium Type, the type of hours eligible for premium must be identified. Premiums are configured separately for each type of hours from Regular and Overtime 1 to Overtime 4. Again, this concept is best illustrated through example. Two examples are provided below for clarity. Remember, any combination of premiums can be used to meet the user's needs. The examples below are simply example scenarios.

Regular and Overtime 1 Hours in the Head Nurse Department receive Premium Pay

If both regular and overtime 1 hours in the Head Nurse department receive premium pay then the premium must be configured separately for both Regular Hours and Overtime 1 hours as shown. The example below uses an Amount Pay Method which pays employees an additional dollar amount for every hour eligible for the premium. In the example, Regular Hours worked as a Head Nurse receive an additional dollar per hour while Overtime Hours receive an additional two dollars per hour.

![](/img/image-404.png)

![](/img/image-404.png)

Only Overtime 1 Hours in the Head Nurse Department receive Premium Pay

If only Overtime 1 hours in the Head Nurse department receive premium pay then the premium should only be configured for Overtime 1 hours as shown. The example below uses an Amount Pay Method which pays employees an additional dollar amount for every hour eligible for the premium. In the example, Overtime hours worked as a Head Nurse receive an additional two dollars per hour while Regular Hours do not receive a premium and are paid at the employee's base wage.

![](/img/image-404.png)

![](/img/image-404.png)

Identify an appropriate Pay Method

![](/img/image-404.png)

When configuring Pay Premiums be sure to select the Pay Method that matches your needs. InfiniTime supports three separate pay methods as listed below. Pay special attention to the labels and units on the form when selecting Pay Premiums. If 'None' is selected in the Premium Pay Drop Down a premium will not be applied for the Hours Type.

Amount Pay Method

The Amount Pay Method pays employees an additional dollar amount for each hour they work. For example, an amount of 5.00 as shown below will pay employees their default wage plus an additional five dollars per hour for Regular Hours worked on the Department.. An example calculation is below.

Employee Default Wage + Dollar Amount = Hourly Wage

$10.00 + $5.00 = Hourly Wage

$15.00 = Hourly Wage

![](/img/image-404.png)

Percent Pay Method

The Percent Pay Method pays employees an additional percentage of their default wage for each hour they work. For example, a percent wage increase of 50 Percent is equivalent to Time and a Half or 1.5 times the employee's default wage. An example calculation is below.

Employee Default Wage + (Employee Default Wage \* Percent Wage Increase) = Hourly Wage

$10.00 + ($10.00 \* 50%) = Hourly Wage

$10.00 + ($5.00) = Hourly Wage

$15.00 = Hourly Wage

![](/img/image-404.png)

Rate Pay Method

The Rate Pay Method defines a specific wage for overtime hours. When the Rate Pay Method is used employee default wages are ignored and the Premium Rate is used for overtime hours.

![](/img/image-404.png)

WARNING: The Rate Pay Method is not a multiplier of the employee's wage. Selecting the Rate Pay Method and entering 1.5 as the Overtime Rate will pay the employee $1.50 per hour. Remember, the Employee's default wage is ignored when the Rate Pay Method is selected. The Overtime Rate is entered in dollars per hour and will be used as the employee's overtime wage.

Understand how the Premium Hierarchy will affect your pay premium(s)

In some scenarios employees may be eligible for multiple types of premium pay for the same hours type at the same time by meeting the conditions of multiple premium types. If your company will only be tracking a single type of premium pay this section can be ignored. Premiums are applied in a predefined order, beginning with an employees base rate. The base rate is determined by either the Default Wage on the employee's HR Profile Tab or by Wages defined in the employee's Wages Table. Refer to the [Wages Section](Employee_Setup/Wages.md) of this document for more information on Employee Wages.

After InfiniTime determines an employee's base rate Premium Pay is applied in order as listed below. Shift differentials are considered separate from Premium Pay. Employees who qualify for Shift Differential Pay will not receive additional pay from Department, Job, Task, or Policy based Premiums. Example calculations and scenarios are provided below to illustrate the Premium Pay Hierarchy. There are two things to keep in mind:

* Premiums of the Amount and Percent Pay Methods are cumulative.
* Higher priority Premiums of the Rate Pay Method will override lower priority premiums.
* Higher priority Premiums of the Amount and Percent Pay Method will build on top of lower priority rate premiums.

Premium Hierarchy

1. Department Premiums are applied. (Lowest Priority)

2. Job Premiums are applied

3. Task Premiums are applied.

4. Policy Overtime Premiums are applied. (Highest Priority)

Note: Premiums are listed from lowest priority to highest priority.

Amount Pay Method

Premiums of the amount pay method are cumulative. For example, the equations below show how each type of premium would be applied to an employee's base rate if an employee were to meet the requirements of Department, Job, Task, and Policy Overtime premiums each configured with the Amount Pay method.

1. Department Premium:   Amt + WAGE = DWAGE
2. Job Premium:               Amt + DWAGE = JWAGE
3. Task Premium:             Amt + JWage = TWAGE
4. Policy Premium:           Amt + TWAGE =  Hourly Wage

| Ex.# | Base Rate | Department Premium Amount | Job Premium Amount | Task Premium Amount | Policy Overtime Premium Amount |
| 1 | $10.00 | $0.50 | $0.25 | $0.25 | $1.00 |
| 2 | $15.00 | $0.50 | $0.50 | $0.25 | $0.50 |

Note: Values from the table are used in the examples below.

Example 1

| Premium Type | Calculation | Resulting Hourly Wage |
| DEPT | $0.50 + $10.00 | $10.50 |
| JOB | $0.25 + $10.50 | $10.75 |
| TASK | $0.25 + $10.75 | $11.00 |
| POLICY | $0.50 + $11.00 | $11.50 |

Note: The Hourly Wage shown in bold is the final wage after all premiums are applied. The employee would be paid the final wage for any hours qualifying for all premiums.

Example 2

| Premium Type | Calculation | Resulting Hourly Wage |
| DEPT | $0.50 + $15.00 | $15.50 |
| JOB | $0.50 + $15.50 | $16.00 |
| TASK | $0.25 + $16.00 | $16.25 |
| POLICY | $0.50 + $16.25 | $16.75 |

Note: The Hourly Wage shown in bold is the final wage after all premiums are applied. The employee would be paid the final wage for any hours qualifying for all premiums.

Percent Pay Method

Premiums of the Percent pay method are cumulative. For example, the equations below show how each type of premium would be applied to an employee's base rate if an employee were to meet the requirements of Department, Job, Task, and Policy Overtime premiums each configured with the Percent Pay method.

1. Department Premium:    (% \* WAGE) + WAGE = DWAGE
2. Job Premium:                (% \* DWAGE) + DWAGE = JWAGE
3. Task Premium:              (% \* JWAGE) + JWage = TWAGE
4. Policy Premium:            (% \* TWAGE) + TWAGE = Hourly Wage

| Ex.# | Base Rate | Department Premium Percent | Job Premium Percent | Task Premium Percent | Policy Overtime Premium Percent |
| 1 | $10.00 | 5% | 10% | 10% | 15% |
| 2 | $15.00 | 5% | 5% | 5% | 15% |

Note: Values from the table are used in the examples below.

Example 1

| Premium Type | Calculation | Resulting Hourly Wage |
| DEPT | (.05 \* $10.00) + $10.00 | $10.50 |
| JOB | (.10 \* $10.50) + $10.50 | $11.55 |
| TASK | (.10 \* $11.55) + $11.55 | $12.71 |
| POLICY | (.15 \* $12.71) + $12.71 | $14.62 |

Note: The Hourly Wage shown in bold is the final wage after all premiums are applied. The employee would be paid the final wage for any hours qualifying for all premiums.

Example 2

| Premium Type | Calculation | Resulting Hourly Wage |
| DEPT | (.05 \* $15.00) + $15.00 | $15.75 |
| JOB | (.05 \* $15.75) + $15.75 | $16.54 |
| TASK | (.05 \* $16.54) + $16.54 | $17.37 |
| POLICY | (.15 \* $17.37) + $17.37 | $19.98 |

Note: The Hourly Wage shown in bold is the final wage after all premiums are applied. The employee would be paid the final wage for any hours qualifying for all premiums.

Rate Pay Method

Premiums of the Percent pay method are not cumulative. Higher priority premiums simply override lower priority premiums. For example, the equations below show how each type of premium would be applied to an employee's base rate if an employee were to meet the requirements of Department, Job, Task, and Policy Overtime premiums each configured with the Rate Pay method.

1. Department Premium: Rate = DWAGE
2. Job Premium: Rate = JWAGE
3. Task Premium: Rate = TWAGE
4. Policy Premium: Rate = Hourly Wage

| Ex.# | Base Rate | Department Premium Rate | Job Premium Rate | Task Premium Rate | Policy Overtime Premium Rate |
| 1 | $10.00 | $8.00 | $8.50 | $9.00 | $9.50 |
| 2 | $15.00 | $16.00 | $18.00 | $19.00 | $20.00 |

Note: Values from the table are used in the examples below.

Example 1

| Premium Type | Calculation | Resulting Hourly Wage |
| DEPT | $8.00 = Hourly Wage | $8.00 |
| JOB | $8.50 = Hourly Wage | $8.50 |
| TASK | $9.00 = Hourly Wage | $9.00 |
| POLICY | $9.50 = Hourly Wage | $9.50 |

Note: The Hourly Wage shown in bold is the final wage after all premiums are applied. The employee would be paid the final wage for any hours qualifying for all premiums.

Example 2

| Premium Type | Calculation | Resulting Hourly Wage |
| DEPT | $16.00 = Hourly Wage | $16.00 |
| JOB | $18.00 = Hourly Wage | $18.00 |
| TASK | $19.00 = Hourly Wage | $19.00 |
| POLICY | $20.00 = Hourly Wage | $20.00 |

Note: The Hourly Wage shown in bold is the final wage after all premiums are applied. The employee would be paid the final wage for any hours qualifying for all premiums.

Additional Example: Rate Pay Method Overrides lower Priority Premiums

Remember, Premiums of the Rate Pay Method will override lower priority premiums. An example of this concept is provided below.

1. Department Premium:   Amt + WAGE = DWAGE
2. Job Premium:               Amt + DWAGE = JWAGE
3. Task Premium:             Amt + JWage = TWAGE
4. Policy Premium:           Rate =  Hourly Wage

| Ex.# | Base Rate | Department Premium Amount | Job Premium Amount | Task Premium Amount | Policy Overtime Premium Rate |
| 1 | $10.00 | $0.50 | $0.25 | $0.25 | $14.00 |
| 2 | $15.00 | $0.50 | $0.50 | $0.25 | $19.00 |

Note: Values from the table are used in the examples below.

Example 1

| Premium Type | Calculation | Resulting Hourly Wage |
| DEPT | $0.50 + $10.00 | $10.50 |
| JOB | $0.25 + $10.50 | $10.75 |
| TASK | $0.25 + $10.75 | $11.00 |
| POLICY | $14.00 = Hourly Wage | $14.00 |

Note: The Hourly Wage shown in bold is the final wage after all premiums are applied. The employee would be paid the final wage for any hours qualifying for all premiums.

Example 2

| Premium Type | Calculation | Resulting Hourly Wage |
| DEPT | $0.50 + $15.00 | $15.50 |
| JOB | $0.50 + $15.50 | $16.00 |
| TASK | $0.25 + $16.00 | $16.25 |
| POLICY | $19.00 = Hourly Wage | $19.00 |

Note: The Hourly Wage shown in bold is the final wage after all premiums are applied. The employee would be paid the final wage for any hours qualifying for all premiums.

Additional Example: Amount and Percent Pay Methods build on top of lower priority rate premiums

Remember, Premiums of the Amount and Percent Pay Methods will build on lower priority rate premiums. An example of this concept is provided below.

1. Department Premium:   Rate = DWAGE
2. Job Premium:               Amt + DWAGE = JWAGE
3. Task Premium:             Amt + JWage = TWAGE
4. Policy Premium:           Rate =  Hourly Wage

| Ex.# | Base Rate | Department Premium Rate | Job Premium Amount | Task Premium Amount | Policy Overtime Premium Amount |
| 1 | $10.00 | $12.00 | $0.25 | $0.25 | $1.00 |
| 2 | $15.00 | $17.00 | $0.50 | $0.25 | $1.00 |

Note: Values from the table are used in the examples below.

Example 1

| Premium Type | Calculation | Resulting Hourly Wage |
| DEPT | $12.00 = Hourly Wage | $12.00 |
| JOB | $0.25 + $12.00 | $12.25 |
| TASK | $0.25 + $12.25 | $12.50 |
| POLICY | $1.00 + $12.50 | $13.50 |

Note: The Hourly Wage shown in bold is the final wage after all premiums are applied. The employee would be paid the final wage for any hours qualifying for all premiums.

Example 2

| Premium Type | Calculation | Resulting Hourly Wage |
| DEPT | $17.00 = Hourly Wage | $17.00 |
| JOB | $0.50 + $17.00 | $17.50 |
| TASK | $0.25 + $17.50 | $17.75 |
| POLICY | $1.00 + $17.75 | $18.75 |

Note: The Hourly Wage shown in bold is the final wage after all premiums are applied. The employee would be paid the final wage for any hours qualifying for all premiums.