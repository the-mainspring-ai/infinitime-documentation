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
