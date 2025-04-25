### Holiday Types Configuration - Introduction

Holidays allow automatic payment to employees on holidays based on specific conditions, such as working the day before or after. Before configuring holidays, you must identify employee groups eligible for different holiday benefits. Common scenarios include:

- **Employee Pay Type**: Full-time and salary employees typically receive holiday pay, while part-time employees often don't. This requires separate holiday schedule types (e.g., 'Employee Holidays' for full-time/salary and 'No Holiday Benefits' for part-time).

- **Personal/Religious Holidays**: Employees may have negotiated special holidays as part of their compensation. These can be configured as group-specific or individual employee holidays in their profiles.

All holiday types are displayed in the Holiday Schedule Types Table, accessible from the Lookups Menu.

### Holiday Schedule Types Table

The Holiday Schedule Types Table shows all configured Holiday Types in InfiniTime. These types define holiday dates and pay rates (like time and a half or double time) for employees based on their employment status and tenure.

![](/img/Conf_Holidays004.png)

**Insert Button**

- Opens the Holiday Schedule Type Update Form to create a new Holiday Type. Create separate types for different employee groups (e.g., part-time vs. full-time) or tenure levels. For example:
  - Part-time employees typically receive limited holidays
  - Full-time employees typically receive all federal holidays
  - Different types can be created for employees with different tenure levels
  - Types in the same class share the same class name
  - Employees automatically move between types in the same class when they meet tenure requirements
  - If holiday dates don't change based on tenure, only one type is needed and tenure fields can be left blank

**Change Button**

- Opens the Holiday Schedule Type Update form to modify an existing Holiday Type's configuration and dates.

**Delete Button**

- Removes the selected Holiday Type. Cannot delete if the type is assigned to employees or has associated System Holiday Timecard records.

### Holiday Schedule Type Update Form

#### General Tab

Contains settings for Holiday Type Name, Class Settings, and Tenure Settings.

![](/img/JobCosting_Config_11.gif)

**Name Field**

- Description of the Holiday Schedule Type, typically indicating the employee group it applies to.

**Class Field**

- Classes can be thought of as groups related Holiday Schedule Types together. All types in a group must share the same class name. Recommended to configure even with a single holiday type.

**Default Class Field**

- Specifies which class an employee moves to when they exhaust all policies in their current class. Recommended to configure even with a single holiday type.

**Employee Tenure From Amount Field**

- Minimum years of employment required to qualify for this Holiday Schedule Type. Leave blank if only one Holiday Type exists for a group.

**Employee Tenure To Amount Field**

- Maximum years of employment while qualifying for this Holiday Schedule Type. Leave blank if only one Holiday Type exists for a group.

**Default Holiday Schedule Type Checkbox**

- When checked, makes this the default type (highlighted in blue). Employees are automatically assigned to the Default type when:
  - They don't qualify for their current type due to tenure restrictions
  - They don't qualify for any types in their current class
  - They don't qualify for any types in their default class

### Dates Tab

The Dates Tab displays all Holiday Dates configured for the selected Holiday Type.

**Insert Button**

- Opens the Master Holiday Update form to add a new holiday date
- Each holiday must be configured individually
- InfiniTime automatically adds other activity hours for eligible employees

**Change Button**

- Opens the Master Holiday Update form for the selected Holiday Date
- Allows modification of Holiday Options and conditions
- Note: Holiday Date cannot be changed if System Holiday Timecard records exist

**Delete Button**

- Removes the selected Holiday Date from the Holiday Type
- Note: Cannot delete if System Holiday Timecard records exist

### Holiday Master Holiday Update Form

The Holiday Master Holiday Update Form defines holiday options and conditions for individual holiday dates.

#### Available Holiday Options & Conditions - General Tab

Name:
Enter the Name of Holiday.

- Enter the holiday name

**Date Field**

- Enter the holiday date
- Only one holiday can exist per date for a given holiday type
- Duplicate dates will trigger a warning

**Deduction Type Dropdown**

- Select the deduction type
- If "Accrual" is selected, an Accrual Name must be selected for posting

![](/img/clip_image018.jpg)

**Other Activity Type Field**

- Specifies the Other Activity Type for holiday hours
- Typically uses the same activity type for all holiday hours (e.g., "Holiday Time")

**All Worked Hours Are Holiday Pay**

- Controls whether employees automatically receive holiday pay
- If "No": Employees automatically receive hours if they meet requirements
- If "Yes": Employees must punch in & punch out on the holiday to receive pay

**Other Activity Hours Field**

- When "All Worked Hours Are Holiday Pay" is "No":
  - Enter the number of hours employees automatically receive (e.g., 8)
  - Enables the "Hours Mapping" and "Rate Mapping" tabs to be accessible

**Max Other Activity Hours Field**

- When "All Worked Hours Are Holiday Pay" is "Yes":
  - Enter the maximum hours eligible for holiday pay
  - Hours worked in excess will not receive holiday pay

**Worked Holiday Rate Multiplier Field**

- Enter the rate for holiday hours
- Used for Gross Payroll Reports

**Day Before Holiday Must Be Worked Checkbox**

- If "Yes": Employees must work the day before to receive holiday hours
- For employees without schedules: Day before is literal (e.g., Sunday for Monday holiday)
- For employees with schedules: Day before refers to first scheduled day prior to holiday

**Day After Holiday Must Be Worked**

- If "Yes": Employees must work the day after to receive holiday hours
- For employees without schedules: Day after is literal (e.g., Tuesday for Monday holiday)
- For employees with schedules: Day after refers to first scheduled day after holiday

**Note**: Day Before and Day After settings cannot be enabled for consecutive holidays (e.g., Thanksgiving and Day After Thanksgiving). Enable Day Before for first holiday and Day After for second holiday.

**Holiday Starts Day Before**

- If "Yes": Holiday pay starts at specified time on day before holiday
- Commonly used for night shifts

**Holiday Ends on Holiday**

- If "Yes": Holiday pay ends at specified time on holiday

**Holiday Ends Day After**

- If "Yes": Holiday pay ends at specified time on day after holiday

**Holiday Based on Employee's Schedule**

- If "Yes": Holiday pay matches employee's schedule for holiday date
- Employee receives holiday hours for all hours worked within schedule
- If employee doesn't work, they receive holiday hours according to scheduled hours

**Example: Holiday Based on Employee's**

| Scenario                 | Schedule                   | Holiday Date   | Result                                                 |
| ------------------------ | -------------------------- | -------------- | ------------------------------------------------------ |
| Employee Reports to Work | Mon-Fri, 8:00 AM - 4:00 PM | Friday, Dec 24 | Holiday pay for hours worked between 8:00 AM - 4:00 PM |
| Employee Has Day Off     | Mon-Fri, 8:00 AM - 4:00 PM | Friday, Dec 24 | Automatically receives 8 hours holiday pay             |

**Not a Holiday if Worked**

- If "Yes": Holiday pay is not awarded if employee works on holiday date

**Employee Required to Work**

- Requires minimum hours worked to receive holiday pay
- Can be based on:
  - Hours on holiday date
  - Hours over specified days before holiday
  - Hours over specified work weeks before holiday

**Average Hours**

- Calculates average hours over specified period
- Can be based on days or weeks before holiday
- Maximum holiday hours capped by Other Activity Hours field

For detailed examples of Average Hours calculations, see the [Holiday Examples Configuration](holiday_examples_config.md).

### Hours Mapping Tab

"All Worked Hours Are Holiday Pay" MUST be set to "No" for this tab to be accessible
The Hours Mapping Tab allows mapping of scheduled and unscheduled hours worked on a Holiday Date to different hours types (e.g., Overtime Four). For more details, see the [Hours Mapping section](Product_Configuration.md#hm1_Hours_Mapping).

#### Scheduled Hours Tab

**Map Regular Hours Into Dropdown**

- Maps all Scheduled Regular Hours to selected Hours Type

**Map OT One Hours Into Dropdown**

- Maps all Scheduled OT One Hours to selected Hours Type

**Map OT Two Hours Into Dropdown**

- Maps all Scheduled OT Two Hours to selected Hours Type

**Map OT Three Hours Into Dropdown**

- Maps all Scheduled OT Three Hours to selected Hours Type

**Map OT Four Hours Into Dropdown**

- Maps all Scheduled OT Four Hours to selected Hours Type

**Example: Scheduled Hours**

- Employee schedule: 8:00 AM to 5:00 PM on 12/31/2013
- All hours worked between 8:00 AM and 5:00 PM are Scheduled Hours
- These hours are mapped according to Scheduled Hours Mapping settings

#### Unscheduled Hours Tab

**Map Regular Hours Into Dropdown**

- Maps all Unscheduled Regular Hours to selected Hours Type

**Map OT One Hours Into Dropdown**

- Maps all Unscheduled OT One Hours to selected Hours Type

**Map OT Two Hours Into Dropdown**

- Maps all Unscheduled OT Two Hours to selected Hours Type

**Map OT Three Hours Into Dropdown**

- Maps all Unscheduled OT Three Hours to selected Hours Type

**Map OT Four Hours Into Dropdown**

- Maps all Unscheduled OT Four Hours to selected Hours Type

**Example: Unscheduled Hours**

- Employee schedule: 8:00 AM to 5:00 PM on 12/31/2013
- All hours worked outside 8:00 AM to 5:00 PM (12:00 AM - 8:00 AM and 5:00 PM - 11:59 PM) are Unscheduled Hours
- These hours are mapped according to Unscheduled Hours Mapping settings

#### Additional Options

**Any Hours Worked Over Holiday Hours go Into OT Checkbox**

- Maps excess hours beyond Holiday Other Activity Hours to an overtime bucket

**Deduct Worked Holiday Hours from Weekly Overtime Checkbox**

- When checked: Hours worked on Holiday Date are excluded from weekly overtime calculations

### Rate Mapping Tab

"All Worked Hours Are Holiday Pay" must be set to "No" for this tab to be accessible

The Rate Mapping Tab of the Master Holiday
Update form permits the InfiniTime
Administrator to scale the number of Other Activity Hours awarded on the
holiday date according to the number of hours worked by the employee over
a number of days prior to the holiday date. This feature is especially
useful for organizations who wish to scale Holiday benefits accordingly
for Part Time and Full Time employees based on the employee's worked hours.

#### Key Settings:

**Days to Rate Map**

- Specifies the number of days before the holiday when employee hours will be totaled and compared against rate mapping entries

**Rate Mapping Entries**

- **Insert**: Creates new rate mapping entries that define how many holiday hours employees receive based on their worked hours
  - Example: A configuration might award 2 holiday hours for every 10 hours worked

**Entry Fields:**

- **Hours Worked**: The range of hours an employee must work during the specified days to qualify
- **Other Activity Hours**: The amount of holiday hours awarded when an employee's total worked hours falls within the specified range

**Change/Delete Options:**

- **Change**: Modifies holiday options and conditions (holiday date cannot be changed if System Holiday Timecard records exist)
- **Delete**: Removes the selected holiday date (not allowed if System Holiday Timecard records exist)

### Holiday Types: Scheduled vs. Unscheduled Hours

Organizations may offer different pay rates for holiday work based on whether employees were scheduled to work. InfiniTime supports this through its Hours Mapping System, Holiday Options, and Payroll Export System.

Common holiday pay structures:

| Method                          | Description                                                                        |
| ------------------------------- | ---------------------------------------------------------------------------------- |
| Fixed Benefits                  | Preset hours at a specific rate for each holiday, based on holiday date conditions |
| Premium Pay for Worked Hours    | Higher pay rate for hours worked (scheduled, unscheduled, or both) on holidays     |
| Fixed Benefits with Premium Pay | Combination of preset holiday hours at base rate plus premium pay for worked hours |

> For step-by-step instructions on configuring all holiday types, see the [Holiday Setup Guide](holiday_setup_guide.md).

#### Holiday Configuration - Fixed Benefits
