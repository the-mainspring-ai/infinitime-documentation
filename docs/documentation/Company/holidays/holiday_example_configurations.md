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

### Holiday Types Configuration - Basic Example

ABC Company has three employee groups with distinct holiday policies:

1. **Full Time Production Employees**
   - Eligible for all company holidays
   - Must work day before/after to receive holiday pay
   - Receive OT2 for hours worked on holidays

> Note: ABC Company tracks hours as follows:
>
> - Regular Hours: > 40/Weekly
> - OT1 Hours: > 40/Weekly
> - OT2 Hours: Worked Holiday Hours

2. **Full Time Admin Employees**

   - Eligible for all company holidays
   - No day before/after work requirement
   - Not expected to work on holidays

3. **Part Time Employees**
   - Not eligible for holidays
   - Holiday eligibility for Full Time employees is not tenure-based

**Special Case: Religious Holidays**

- Applies to Employee IDs 202 and 708
- Pre-approved Personal Time for specific religious holidays
- No day before/after requirement
- Employees will not work on these dates

#### Configuration Steps

**Company-Wide Holidays:**

1. Access Manager Module
2. Navigate to: Lookups → Calculations Setup → Holiday Schedule Types
3. Click Insert for new Holiday Type
4. Configure Holiday Type settings (Description, Class, Default Class, Tenure)
5. On Dates Tab, click Insert for each company holiday
6. Configure Holiday Features & Conditions as needed

**Employee-Specific Holidays:**

### Full Time Production Holidays

| Holiday Date | Holiday Name           | Holiday Hours  | Additional Features & Conditions                                                                                                      |
| ------------ | ---------------------- | -------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| 1/1/12       | New Years Day          | 8 Hrs: Holiday | • Day Before Holiday Must Be Worked<br>• Day After Holiday Must Be Worked<br>• Hours Mapping: REG → OT2<br>• Hours Mapping: OT1 → OT2 |
| 2/20/12      | Presidents Day         | 8 Hrs: Holiday | • Day Before Holiday Must Be Worked<br>• Day After Holiday Must Be Worked<br>• Hours Mapping: REG → OT2<br>• Hours Mapping: OT1 → OT2 |
| 5/28/12      | Memorial Day           | 8 Hrs: Holiday | • Day Before Holiday Must Be Worked<br>• Day After Holiday Must Be Worked<br>• Hours Mapping: REG → OT2<br>• Hours Mapping: OT1 → OT2 |
| 7/4/12       | Independence Day       | 8 Hrs: Holiday | • Day Before Holiday Must Be Worked<br>• Day After Holiday Must Be Worked<br>• Hours Mapping: REG → OT2<br>• Hours Mapping: OT1 → OT2 |
| 9/3/12       | Labor Day              | 8 Hrs: Holiday | • Day Before Holiday Must Be Worked<br>• Day After Holiday Must Be Worked<br>• Hours Mapping: REG → OT2<br>• Hours Mapping: OT1 → OT2 |
| 11/22/12     | Thanksgiving Day       | 8 Hrs: Holiday | • Day Before Holiday Must Be Worked<br>• Day After Holiday Must Be Worked<br>• Hours Mapping: REG → OT2<br>• Hours Mapping: OT1 → OT2 |
| 11/23/12     | Day After Thanksgiving | 8 Hrs: Holiday | • Day Before Holiday Must Be Worked<br>• Day After Holiday Must Be Worked<br>• Hours Mapping: REG → OT2<br>• Hours Mapping: OT1 → OT2 |
| 12/24/12     | Christmas Eve          | 8 Hrs: Holiday | • Day Before Holiday Must Be Worked<br>• Day After Holiday Must Be Worked<br>• Hours Mapping: REG → OT2<br>• Hours Mapping: OT1 → OT2 |
| 12/25/12     | Christmas Day          | 8 Hrs: Holiday | • Day Before Holiday Must Be Worked<br>• Day After Holiday Must Be Worked<br>• Hours Mapping: REG → OT2<br>• Hours Mapping: OT1 → OT2 |
| 12/31/12     | New Years Eve          | 8 Hrs: Holiday | • Day Before Holiday Must Be Worked<br>• Day After Holiday Must Be Worked<br>• Hours Mapping: REG → OT2<br>• Hours Mapping: OT1 → OT2 |

### Full Time Admin Holidays

| Holiday Date | Holiday Name           | Holiday Hours  | Additional Features & Conditions |
| ------------ | ---------------------- | -------------- | -------------------------------- |
| 1/1/12       | New Years Day          | 8 Hrs: Holiday | None                             |
| 2/20/12      | Presidents Day         | 8 Hrs: Holiday | None                             |
| 5/28/12      | Memorial Day           | 8 Hrs: Holiday | None                             |
| 7/4/12       | Independence Day       | 8 Hrs: Holiday | None                             |
| 9/3/12       | Labor Day              | 8 Hrs: Holiday | None                             |
| 11/22/12     | Thanksgiving Day       | 8 Hrs: Holiday | None                             |
| 11/23/12     | Day After Thanksgiving | 8 Hrs: Holiday | None                             |
| 12/24/12     | Christmas Eve          | 8 Hrs: Holiday | None                             |
| 12/25/12     | Christmas Day          | 8 Hrs: Holiday | None                             |
| 12/31/12     | New Years Eve          | 8 Hrs: Holiday | None                             |

### Part Time Holidays

> Note: Part Time Employees are not eligible for Holidays. No Holiday Dates should be added to the 'Part Time Holidays' Holiday Type.

### Employee ID 202 - Full Time Employee Specific Holiday Dates

| Holiday Date | Holiday Name  | Holiday Hours        | Additional Features & Conditions |
| ------------ | ------------- | -------------------- | -------------------------------- |
| 2/22/12      | Ash Wednesday | 8 Hrs: Personal Time | None                             |
| 4/6/12       | Good Friday   | 8 Hrs: Personal Time | None                             |

### Employee ID 708 - Full Time Employee Specific Holiday Dates

| Holiday Date | Holiday Name | Holiday Hours        | Additional Features & Conditions |
| ------------ | ------------ | -------------------- | -------------------------------- |
| 12/9/12      | Hanukkah     | 8 Hrs: Personal Time | None                             |

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

## Average Hours by Days Example

**Example: Average Hours by Days**

| Setting                          | Value |
| -------------------------------- | ----- |
| Average Hours                    | Yes   |
| Days to Average                  | 21    |
| Other Activity Hours             | 10.00 |
| All Hours Worked are Holiday Pay | No    |

| Day              | Hours Worked: Scenario 1 | Hours Worked: Scenario 2 |
| ---------------- | ------------------------ | ------------------------ |
| 11/5             | 8.25                     | 11.50                    |
| 11/6             | 8.00                     | 11.25                    |
| 11/9             | 8.00                     | 12.00                    |
| 11/10            | 6.50                     | 12.00                    |
| 11/11            | 6.20                     | 8.50                     |
| 11/12            | 7.50                     | 11.50                    |
| 11/13            | 8.00                     | 12.00                    |
| 11/16            | 8.55                     | 12.00                    |
| 11/17            | 9.00                     | 12.50                    |
| 11/18            | 8.00                     | 11.00                    |
| 11/19            | 8.00                     | 11.00                    |
| 11/20            | 8.00                     | 12.00                    |
| 11/23            | 8.25                     | 12.00                    |
| 11/24            | 7.50                     | 8.00                     |
| 11/25            | 8.02                     | 8.50                     |
| Average          | 7.85                     | 11.05                    |
| Friday (Holiday) | 7.85                     | 10.00                    |

**Example: Average Hours by Weeks**

| Setting                          | Value |
| -------------------------------- | ----- |
| Average Hours                    | Yes   |
| Weeks to Average                 | 3     |
| Other Activity Hours             | 10.00 |
| All Hours Worked are Holiday Pay | No    |

| Day              | Hours Worked: Scenario 1 | Hours Worked: Scenario 2 |
| ---------------- | ------------------------ | ------------------------ |
| 11/2             | 8.25                     | 11.50                    |
| 11/3             | 8.00                     | 11.25                    |
| 11/4             | 8.00                     | 12.00                    |
| 11/5             | 6.50                     | 12.00                    |
| 11/6             | 6.20                     | 8.50                     |
| 11/9             | 7.50                     | 11.50                    |
| 11/10            | 8.00                     | 12.00                    |
| 11/11            | 8.55                     | 12.00                    |
| 11/12            | 9.00                     | 12.50                    |
| 11/13            | 8.00                     | 11.00                    |
| 11/16            | 8.00                     | 11.00                    |
| 11/17            | 8.00                     | 12.00                    |
| 11/18            | 8.25                     | 12.00                    |
| 11/19            | 7.50                     | 8.00                     |
| 11/20            | 8.02                     | 8.50                     |
| Daily Average    | 7.85                     | 11.05                    |
| Friday (Holiday) | 7.85                     | 10.00                    |
