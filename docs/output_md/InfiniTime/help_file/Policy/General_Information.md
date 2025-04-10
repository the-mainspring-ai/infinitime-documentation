xml version="1.0" encoding="utf-8"?





General Information




# General Information

In the General tab of the policy update form, basic information about the policy is given.

![](/img/image-404.png)

Ok â Exits the window and saves any changes to the database.

Cancel â Exit the window without saving changes.

Help â View Help documentation for the current screen.

Name - This is the given name of the policy.

Class -  Classes provide grouping for Policies. A class can be thought of as a group name for a particular set of Policies. The class name must be identical for all Policies in a Group. Refer to the section on Configuring Classes and Tenures below for more information on the use of Policy Classes.

Default Class - When an employee has exhausted all the policies in the class, the employee will be automatically placed in a different class as specified by the default class.

Employees Working From - Minimum value, in years, that an employee must work before qualifying for the Policy. Refer to the section on Configuring Classes and Tenures below for more information on the use of Tenures.

Employees Working To - Maximum value, in years, that an employee can work while still qualifying for the Policy. Refer to the section on Configuring Classes and Tenures below for more information on the use of Tenures.

Default - Selecting this checkbox will set this Record as the default one.

If you wish to make a different policy your default, you will need to:

1. Uncheck the box that says default, and click OK.

2. If you already have a policy created, highlight it and click change.

3. Place a check in the box and hit OK.

Inactive - Selecting this check box will cause this record not to appear as a selection in InfiniTimeâ¢.

Do Not Allow Breaks - Checking this box will not show the break options when you are using the Employee Module and it will not show break options when you are editing a punch in the timecard activity window.

Configuring Classes and Tenures

In many cases policy settings may change according to the length of time an employee is with the company and what type of position they hold. InfiniTime uses a Class and Tenure system to automatically move employees from one policy to another as their policy settings change. Classes are used to separate policies into groups, while tenures break policies into a chronological sequence. The following example represents a company with policies configured for full and part time employees. Policy settings change with benefits in the form of longer breaks and bonus hours for employees who have been with the company for five years, and ten years or more. A separate policy is also included for salary employees.

![](/img/image-404.png)

| Policy Name | Class | Default Class | Working From | Working To |
| 1st to 5th Years Part Time | Part Time | Part Time | 0 | 5 |
| 5th to 10 Years Part Time | Part Time | Part Time | 5 | 10 |
| 10 + Years Part Time | Part Time | Part Time | 10 | 99 |
| 1st to 5th Years Full Time | Full Time | Full Time | 0 | 5 |
| 5th to 10 Years Full Time | Full Time | Full Time | 5 | 10 |
| 10 + Years Full Time | Full Time | Full Time | 10 | 99 |
| Salary Employees | Salary | Salary | 0 | 99 |

The table above shows the class and tenure configuration for all of the example companies policies.  In this example there are three distinct policy groups. Full Time Employees, Part Time Employees, and Salary Employees represent the three categories of employees with different policy settings. As shown, it is often helpful to separate employees into categories with identical policy configurations in order to simplify the policy configuration process. Generally the easiest way to separate employees is according to pay type - Full Time, Part Time, and Salary. These categories usually have separate policy settings. Keep in mind if all employees within your company have the same policy settings it is not necessary to configure classes or tenures. Simply create one policy and configure it as appropriate. Once all classes have been identified the points at which policy settings change must then be chosen. In this example employees receive additional benefits after five and ten years of employment. With this in mind tenure ranges will be zero (0) to five (5) representing the policy for both full time and part time new hires, five (5) to ten (10) representing the policy for employees that have been with the company for more than five years be they full time or part time, and ten (10) to ninety-nine (99) representing full or part time employees that have been with the company for more than ten years.

There are a few key points to keep in mind when configuring classes and tenures:

* Each group of policies must have their own class.
* + Tenures may not overlap within a single class.
  + There may not be gaps between tenures from one policy within a group to the next. The tenures must flow in a sequential order with all years represented from zero (0) to ninety-nine (99).

When saving a policy record, if a gap between tenures exists or if tenures overlap within that class of policies a warning will be displayed as shown below. Check to ensure sequential flow of tenures from one policy to the next.