---
title: "Accrue X Hours Per Month - Calculation Examples"
description: "Guidance and examples for calculating monthly hour accruals, including anniversary resets and varying month lengths."
---

Accrue By Month Examples

## Accrue X Hours Per 1 Month Accrual Calculation Examples

The 'Accrue X Hours per 1 Month' accrual calculation awards one interval each calendar month on the exact date corresponding to the Start of the Accrual Period. If a given month does not have a day corresponding to the exact start of the accrual period, then hours are accrued on the last day of the month. For clarity, examples are shown below.

Example 1: Employee Hired at End of Month - Anniversary Accrual Reset

Accrual Settings:

Accrue 6.67 Hours Per 1 Month

Anniversary Reset Type

Employee Hire Date: 05/31/2009

Notice how the employee receives 6.67 Hours each month on the exact day that corresponds to their hire date, which in this case is the 31st of each month. Since every calendar month does not have 31 days, accrual hours are awarded on the last day of the month for those months that have less than 31 days. For this purpose, InfiniTime recognizes Calendar Years with 28 and 29 days in February in accordance with Leap Year. Additionally, the 12th interval is not awarded until 05/31/2010, which is exactly 12 months after the accrual period starts.

| Accrual Interval        | Date       | Accrued Hours |
| ----------------------- | ---------- | ------------- |
| Start of Accrual Period | 05/31/2009 | 0.00          |
| 1                       | 06/30/2009 | 6.67          |
| 2                       | 07/31/2009 | 13.34         |
| 3                       | 08/31/2009 | 20.01         |
| 4                       | 09/30/2009 | 26.68         |
| 5                       | 10/31/2009 | 33.35         |
| 6                       | 11/30/2009 | 40.02         |
| 7                       | 12/31/2009 | 46.69         |
| 8                       | 01/31/2010 | 53.36         |
| 9                       | 02/28/2010 | 60.03         |
| 10                      | 03/31/2010 | 66.70         |
| 11                      | 04/30/2010 | 73.37         |
| 12                      | 05/31/2010 | 80.04         |

Example 2: Employee Hired in Middle of Month - Anniversary Accrual Reset

Accrual Settings:

Accrue 6.67 Hours Per 1 Month

Anniversary Reset Type

Employee Hire Date: 05/11/2009

Notice how the employee receives 6.67 Hours each month on the exact day that corresponds to their hire date, which in this case is the 11th of each month. Additionally, the 12th interval is not awarded until exactly 12 months after the accrual period starts.

| Accrual Interval        | Date       | Accrued Hours |
| ----------------------- | ---------- | ------------- |
| Start of Accrual Period | 05/11/2009 | 0.00          |
| 1                       | 06/11/2009 | 6.67          |
| 2                       | 07/11/2009 | 13.34         |
| 3                       | 08/11/2009 | 20.01         |
| 4                       | 09/11/2009 | 26.68         |
| 5                       | 10/11/2009 | 33.35         |
| 6                       | 11/11/2009 | 40.02         |
| 7                       | 12/11/2009 | 46.69         |
| 8                       | 01/11/2010 | 53.36         |
| 9                       | 02/11/2010 | 60.03         |
| 10                      | 03/11/2010 | 66.70         |
| 11                      | 04/11/2010 | 73.37         |
| 12                      | 05/11/2010 | 80.04         |

Example 3: Employee Hired in Middle of Year - Calendar Year Accrual Reset

Accrual Settings:

Accrue 6.67 Hours Per 1 Month

Calendar Year Reset Type

Carry Over

Stop at 280

Employee Hire Date: 05/11/2009

Notice how the employee receives 6.67 Hours each month from their hire date until the new Calendar Year, at which point accrued hours are carried over. Since the employee does not work a full month between 12/11/2009 and 1/1/2010, the employee does not receive additional hours during this period. The accrual calculation resets at the start of the new year in accordance with the Calendar Year Reset Type, at which point the employee continues to accrue hours at a rate of 6.67 hours per month as shown. Notice how the 12th interval of the second accrual period is not awarded until 01/01/2011, exactly one year after the accrual period starts. If accruals were viewed for an employee assigned to this type on 12/31/2010, the employee would only have 120.06 Hours available.

| Accrual Period / Accrual Interval    | Date       | Accrued Hours For Accrual Period | Total Remaining Hours |
| ------------------------------------ | ---------- | -------------------------------- | --------------------- |
| 1st Accrual Period - Start of Period | 05/11/2009 | 0.00                             | 0.00                  |
| 1st Accrual Period - 1st Interval    | 06/11/2009 | 6.67                             | 6.67                  |
| 1st Accrual Period - 2nd Interval    | 07/11/2009 | 13.34                            | 13.34                 |
| 1st Accrual Period - 3rd Interval    | 08/11/2009 | 20.01                            | 20.01                 |
| 1st Accrual Period - 4th Interval    | 09/11/2009 | 26.68                            | 26.68                 |
| 1st Accrual Period - 5th Interval    | 10/11/2009 | 33.35                            | 33.35                 |
| 1st Accrual Period - 6th Interval    | 11/11/2009 | 40.02                            | 40.02                 |
| 1st Accrual Period - 7th Interval    | 12/11/2009 | 46.69                            | 46.69                 |
| 2nd Accrual Period - Start of Period | 01/01/2010 | 0.00                             | 46.69                 |
| 2nd Accrual Period - 1st Interval    | 02/01/2010 | 6.67                             | 53.36                 |
| 2nd Accrual Period - 2nd Interval    | 03/01/2010 | 13.34                            | 60.03                 |
| 2nd Accrual Period - 3rd Interval    | 04/01/2010 | 20.01                            | 66.70                 |
| 2nd Accrual Period - 4th Interval    | 05/01/2010 | 26.68                            | 73.37                 |
| 2nd Accrual Period - 5th Interval    | 06/01/2010 | 33.35                            | 80.04                 |
| 2nd Accrual Period - 6th Interval    | 07/01/2010 | 40.02                            | 86.71                 |
| 2nd Accrual Period - 7th Interval    | 08/01/2010 | 46.69                            | 93.38                 |
| 2nd Accrual Period - 8th Interval    | 09/01/2010 | 53.36                            | 100.05                |
| 2nd Accrual Period - 9th Interval    | 10/01/2010 | 60.03                            | 106.72                |
| 2nd Accrual Period - 10th Interval   | 11/01/2010 | 66.70                            | 113.39                |
| 2nd Accrual Period - 11th Interval   | 12/01/2010 | 73.37                            | 120.06                |
| 2nd Accrual Period - 12th Interval   | 01/01/2011 | 80.04                            | 126.73                |
