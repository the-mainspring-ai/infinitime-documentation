# Revised Holiday Configuration Documentation

## 1. Configure Employee Policies

- **Separate** worked hours into OT1, OT2, OT3, and OT4 as required by the Hours Mapping Hierarchy.

- Two distinct employee types with different policies:
  - **Hourly Operations**
    - Daily OT (OT1) after **10** hours worked in a day @ **150%** of base rate
    - Unscheduled regular hours (OT2) @ **200%** of base rate
    - Unscheduled OT1 hours (OT3) @ **200%** of base rate
  - **Salary Administrative**
    - Daily OT (OT1) after **8** hours in a day @ **150%** of base rate
    - Unscheduled regular hours (OT2) @ **200%** of base rate
    - Unscheduled OT1 hours (OT3) @ **200%** of base rate

| Employee Type         | OT1 (Daily OT)  | OT2 (Unscheduled Reg) | OT3 (Unscheduled OT1) | OT4 |
| --------------------- | --------------- | --------------------- | --------------------- | --- |
| Hourly Operations     | > 10 hrs @ 150% | 200%                  | 200%                  | N/A |
| Salary Administrative | > 8 hrs @ 150%  | 200%                  | 200%                  | N/A |

**Important Note:** Even though OT2 and OT3 carry the same rate on regular days, they _must_ be mapped to separate buckets to satisfy the Hours Mapping Hierarchy, as different rates apply on holidays (300% vs 350%).

## 2. Identify Employee Groups Eligible for Holiday Benefits

- At XYZ Hospitality, both employee types (Hourly Operations and Salary Administrative) receive the same holiday benefits.
- This simplifies configuration as only one Holiday Type is required. In organizations where different groups receive different holiday benefits, you would need to create separate Holiday Types.

## 3. Define Holiday Calendar Dates

- Both Fixed Benefits and Premium Pay apply to the following dates for all eligible employees:
- **Holiday Calendar**:
  - January: 1/1, 1/21
  - February: 2/18, 2/27
  - July: 7/4
  - September: 9/2
  - November: 11/28
  - December: 12/25

## 4. Create One Holiday Type

- Since all XYZ Hospitality employees receive identical holiday benefits, only one Holiday Type is required.
- If your organization has different holiday benefits for different employee groups, you would need to create multiple Holiday Types.

## 5. Create Fixed Benefit Holiday Dates

- **Important:** Create one Fixed Benefit Holiday Date configuration for EACH calendar date listed in step 3.
- **Fixed Benefit Configuration:**
  - **Other Activity Type:** Holiday Pay
  - **Pay Code:** `HP`
  - **Rate:** Base Rate
  - **Count as Day Worked:** ✔️
  - **Count as Regular Hours:** ❌
  - **Employee Required To Work flag:** **Enabled** (This is specifically chosen to prevent accidental overpayment through automatic Holiday Pay entries)

## 6. Create Premium Pay Holiday Dates

- **Important:** Create one Premium Pay for Worked Hours Holiday Date configuration for EACH calendar date listed in step 3.
- **Premium Pay Configuration:**

| Hours Bucket                   | Rate | Pay Code |
| ------------------------------ | ---- | -------- |
| Scheduled Regular on Holiday   | 200% | HW       |
| Scheduled Overtime on Holiday  | 250% | HWOT     |
| Unscheduled Regular on Holiday | 300% | HWUH     |
| Unscheduled OT1 on Holiday     | 350% | HWUO     |
| OT4                            | N/A  | —        |

## 7. Fixed Benefit Rules (When Holiday Pay is Awarded)

- **Automatic Award (Working on Holiday):**
  - 8 hours of `HP` automatically inserted when employee works on the holiday
  - Employee must also work the day before & after the holiday
- **Manual Award (Facility Closed):**
  - Supervisors must manually insert 8 hours of `HP` when the facility is closed
  - This applies to scheduled non-working days where the office is closed
  - Employee must work the day before & after the holiday
- **No Award Scenarios:**
  - Employee called out sick on the holiday
  - Employee is not scheduled and does not work on the holiday
  - If supervisors neglect to insert holiday hours, adjustments can be made in the next pay period

| Schedule Status | Working Status                | Fixed Benefit Awarded? | Action Required      |
| --------------- | ----------------------------- | ---------------------- | -------------------- |
| Scheduled       | Working                       | Yes - 8 hrs HP         | Automatic            |
| Scheduled       | Not Working (Facility Closed) | Yes - 8 hrs HP         | Manual by Supervisor |
| Scheduled       | Called Out Sick               | No                     | None                 |
| Not Scheduled   | Called In to Work             | Yes - 8 hrs HP         | Automatic            |
| Not Scheduled   | Not Working                   | No                     | None                 |

## 8. Premium Pay Rules (When Holiday Premium Pay is Applied)

- **Working on Holiday:**
  - Hours automatically posted to the appropriate holiday-worked buckets
  - Separated according to hours type (`HW`, `HWOT`, `HWUH`, `HWUO`)
  - Employee must work the day before and after the holiday
- **No Premium Pay Scenarios:**
  - Employee not working on the holiday (facility closed)
  - Employee called out sick on the holiday
  - Employee not scheduled and does not work

| Schedule Status | Working Status                | Premium Pay Awarded? | Action Required |
| --------------- | ----------------------------- | -------------------- | --------------- |
| Scheduled       | Working                       | Yes                  | Automatic       |
| Scheduled       | Not Working (Facility Closed) | No                   | None            |
| Scheduled       | Called Out Sick               | No                   | None            |
| Not Scheduled   | Called In to Work             | Yes                  | Automatic       |
| Not Scheduled   | Not Working                   | No                   | None            |

## 9. Employee Assignment

- Use **Quick Assign** to assign employees to the appropriate Holiday Type.
- For detailed instructions on using Quick Assign and Employee Filter functionality, refer to the Quick Assign and Employee Filter sections of this document.

This configuration ensures that XYZ Hospitality correctly calculates and awards both fixed holiday benefits and premium pay for hours worked on holidays according to their specific policies.

---------------- unrefined below --------------

### Holiday Types Configuration - Example Basic Configuration

ABC Company has, on an overall basis, three groups of employees with
distinct holiday settings:

- Full Time Production Employees are eligible for all company observed
  holidays, though they must work the day before and day after in order
  to receive the holiday. Full Time Production Employees who report
  to work on Holiday Dates receive OT2 for all hours worked.

Note: ABC Company Tracks Regular Hours as greater than 40
/ Weekly, OT1 Hours as >40 Weekly and OT2 Hours as Worked Holiday Hours

- Full Time Admin employees are eligible for all company observed
  holidays and are not required to work the day before or day after.
  Full Time Admin Employees are not expected to report to work on Holiday
  Dates.
- Part Time Employees are not eligible for any holidays. Holiday
  Eligibility for Full Time employees does not change based on their
  time with the company.

Additionally, two Full Time employees (Employee ID 202 and 708) observe
specific Religious Holidays. While these Holidays are not observed directly
by ABC Company â the employee's in question have been preapproved for
Personal Time on these dates and ABC Company would prefer if InfiniTime could handle these holidays
automatically. Employees are not required to work the day before or day
after in order to receive their Employee Specific Holidays. Employees
will not report to work on Employee Specific Holidays.

Holidays would be configured as follows for this scenario:

1. Log Into the Manager Module
2. Click on Lookups â Calculations Setup â Holiday
   Schedule Types
3. Click Insert to Create a Holiday Type
4. Set the Holiday Type Description, Class,
   Default Class, and Tenure as Appropriate
5. Click on the Dates Tab and Click Insert to
   Create a Holiday Date
6. One Holiday Date must be created for each
   Holiday Observed by ABC Company as listed below. Be sure to configure
   Holiday Features & Conditions as appropriate for each holiday
   date.
7. Employee Specific Holidays can be defined
   on the Employee Update Form:

8. Open the Employee Table
9. Search for the Employee for which the
   Employee Specific Holiday will be defined. Highlight the employee
   and click Change.
10. Click on the Holidays Tab.
11. Click Insert to Create a Holiday Date
    for the respective employee. This Holiday Date will only be created
    for the employee in question. Be sure to configure Holiday Features
    & Conditions as appropriate for each holiday date.

### ABC Company Holiday Settings:

_The tables below depict the
details that must be gathered in order to configure holidays for a customer._

**Holiday Types:**

| | | | |
||
| **Holiday Type Description** | **Holiday Type Class** | **Holiday Type Default Class** | **Holiday Type Tenure** |
| Full Time Production Holidays | Full Time Production | Full Time Production | 0 to 99 Years |
| Full Time Admin Holidays | Full Time Admin | Full Time Admin | 0 to 99 Years |
| Part Time Holidays | Part Time | Part Time | 0 to 99 Years |

### 'Full Time Production Holidays' - Holiday Dates:

| | | | |
||
| **Holiday Date** | **Holiday Name** | **Holiday Hours / Other Activity Type** | **Additional Features & Conditions** |
| 1/1/12 | New Years Day | 8 Hrs: Holiday | _ Day Before Holiday Must Be Worked = Yes _ Day After Holiday Must Be Worked = Yes _ Hours Mapping: REG -> OT2 _ Hours Mapping: OT1 -> OT2 |
| 2/20/12 | Presidents Day | 8 Hrs: Holiday | _ Day Before Holiday Must Be Worked = Yes _ Day After Holiday Must Be Worked = Yes _ Hours Mapping: REG -> OT2 _ Hours Mapping: OT1 -> OT2 |
| 5/28/12 | Memorial Day | 8 Hrs: Holiday | _ Day Before Holiday Must Be Worked = Yes _ Day After Holiday Must Be Worked = Yes _ Hours Mapping: REG -> OT2 _ Hours Mapping: OT1 -> OT2 |
| 7/4/12 | Independence Day | 8 Hrs: Holiday | _ Day Before Holiday Must Be Worked = Yes _ Day After Holiday Must Be Worked = Yes _ Hours Mapping: REG -> OT2 _ Hours Mapping: OT1 -> OT2 |
| 9/3/12 | Labor Day | 8 Hrs: Holiday | _ Day Before Holiday Must Be Worked = Yes _ Day After Holiday Must Be Worked = Yes _ Hours Mapping: REG -> OT2 _ Hours Mapping: OT1 -> OT2 |
| 11/22/12 | Thanksgiving Day | 8 Hrs: Holiday | _ Day Before Holiday Must Be Worked = Yes _ Day After Holiday Must Be Worked = Yes _ Hours Mapping: REG -> OT2 _ Hours Mapping: OT1 -> OT2 |
| 11/23/12 | Day After Thanksgiving | 8 Hrs: Holiday | _ Day Before Holiday Must Be Worked = Yes _ Day After Holiday Must Be Worked = Yes _ Hours Mapping: REG -> OT2 _ Hours Mapping: OT1 -> OT2 |
| 12/24/12 | Christmas Eve | 8 Hrs: Holiday | _ Day Before Holiday Must Be Worked = Yes _ Day After Holiday Must Be Worked = Yes _ Hours Mapping: REG -> OT2 _ Hours Mapping: OT1 -> OT2 |
| 12/25/12 | Christmas Day | 8 Hrs: Holiday | _ Day Before Holiday Must Be Worked = Yes _ Day After Holiday Must Be Worked = Yes _ Hours Mapping: REG -> OT2 _ Hours Mapping: OT1 -> OT2 |
| 12/31/12 | New Years Eve | 8 Hrs: Holiday | _ Day Before Holiday Must Be Worked = Yes _ Day After Holiday Must Be Worked = Yes _ Hours Mapping: REG -> OT2 _ Hours Mapping: OT1 -> OT2 |

### 'Full Time Admin Holidays' - Holiday Dates:

| | | | |
||
| **Holiday Date** | **Holiday Name** | **Holiday Hours / Other Activity Type** | **Additional Features & Conditions** |
| 1/1/12 | New Years Day | 8 Hrs: Holiday | None |
| 2/20/12 | Presidents Day | 8 Hrs: Holiday | None |
| 5/28/12 | Memorial Day | 8 Hrs: Holiday | None |
| 7/4/12 | Independence Day | 8 Hrs: Holiday | None |
| 9/3/12 | Labor Day | 8 Hrs: Holiday | None |
| 11/22/12 | Thanksgiving Day | 8 Hrs: Holiday | None |
| 11/23/12 | Day After Thanksgiving | 8 Hrs: Holiday | None |
| 12/24/12 | Christmas Eve | 8 Hrs: Holiday | None |
| 12/25/12 | Christmas Day | 8 Hrs: Holiday | None |
| 12/31/12 | New Years Eve | 8 Hrs: Holiday | None |

### 'Part Time Holidays' - Holiday Dates:

| | | | |
||
| **Holiday Date** | **Holiday Name** | **Holiday Hours / Other Activity Type** | **Additional Features & Conditions** |
| NONE: Â· Part Time Employees are not eligible for Holidays. No Holiday Dates should be added to the 'Part Time Holidays' Holiday Type. | | | |

### Employee ID 202 â Full Time Employee Specific Holiday Dates:

| | | | |
||
| **Holiday Date** | **Holiday Name** | **Holiday Hours / Other Activity Type** | **Additional Features & Conditions** |
| 2/22/12 | Ash Wednesday | 8 Hrs: Personal Time | None |
| 4/6/12 | Good Friday | 8 Hrs: Personal Time | None |

### Employee ID 708 â Full Time Employee Specific Holiday Dates:

| | | | |
||
| **Holiday Date** | **Holiday Name** | **Holiday Hours / Other Activity Type** | **Additional Features & Conditions** |
| 12/9/12 | Hanukkah | 8 Hrs: Personal Time | None |

### **ABC Company Holiday Types within InfiniTime:**

###

### Full Time Admin Holidays:

###

### Full Time Admin Holiday Example:

###

###

###

### Full Time Production Holiday Example:

![](/img/ColSel_Down.gif)

![](/img/TaskPrem_2.gif)

![](/img/EmployeeProfile_029.png)

### Part Time Holidays â Dates Tab

_Part
Time Employees do not receive holidays. With this in mind, the 'Part Time
Holidays' Holiday Schedule Type does not have any holiday dates defined._

**![](/img/Department-Table.gif)**

### Employee Specific Holiday Configuration Example: Employee ID 202

![](/img/JobCosting_Config_12.gif)

![](/img/EmployeeProfile_034.png)

![](/img/sched11.gif)

![](/img/Conf_Holidays012.png)
