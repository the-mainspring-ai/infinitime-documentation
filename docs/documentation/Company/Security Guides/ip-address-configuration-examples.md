---
title: "IP Address Configuration Examples"
description: "Guide for configuring valid IP addresses in InfiniTime for access control"
---

# Valid IP Configuration Examples

InfiniTime provides two methods for defining Valid IP Addresses to control software access:

1. **Company Wide Valid IP Addresses**: IP addresses from which any employee can access InfiniTime
2. **Employee Specific Valid IP Addresses**: IP addresses from which specific employees can access InfiniTime

## Deployment Scenarios

### Onsite InfiniTime Server with Onsite Clients

#### Company Wide Valid IP Addresses

**Limiting Access to Specific Departments or Subnets**

To grant access to a department while restricting others:

1. Identify the common IP address octets for the group of computers
2. Add the IP address with common octets (replacing remaining octets with zeros) to the Company Valid IP Address table

Example:

```
Computer Name         IP Address
Accounting Desktop 1  192.168.10.10
Accounting Desktop 2  192.168.10.11
Accounting Desktop 3  192.168.10.12
Accounting Desktop 4  192.168.10.13

Common Octets:        192.168.10
Final IP Address:     192.168.10.0
```

**Limiting Access to Specific Computers**

To grant access only to specific computers:

1. Identify the exact IP addresses of allowed computers
2. Add each IP address to the Company Valid IP Address table
3. Any IP address not in this table will be denied access

#### Employee Specific Valid IP Addresses

**Limiting Employee Access to Specific IP Addresses**

Configure individual employee access restrictions:

1. Access the login tab of the employee's record
2. Add specific IP addresses to the Employee Specific Valid IP Address table
3. Employees will only be able to access InfiniTime from these IP addresses

**Limiting Employee Access to Specific Departments or Subnets**

To restrict employees to accessing from specific departments:

1. Identify the common IP address octets for the department
2. Add the IP address with common octets to the Employee Specific Valid IP Address table
3. Employees with this configuration will only have access from the specified department

Example:

```
Computer Name         IP Address
Phone Support 1       192.168.20.10
Phone Support 2       192.168.20.11
Phone Support 3       192.168.20.12
Phone Support 4       192.168.20.13

Common Octets:        192.168.20
Final IP Address:     192.168.20.0
```

### Onsite InfiniTime Server with Offsite Clients

#### Limiting Access to Specific Remote Sites

To restrict access to specific remote locations:

1. Identify the public IP addresses of the allowed remote sites
2. Add these addresses to the Company Wide Valid IP Address table
3. Only remote sites with listed IP addresses will have access

#### Providing Administrator Omnipresent Access

To allow administrators access from anywhere while restricting others:

1. Leave the Administrator's Employee Specific Valid IP Address table blank
2. Configure Employee Specific Valid IP Addresses for all other employees
3. Ensure the Company Wide Valid IP Address table is blank for administrator omnipresent access

### Onsite InfiniTime Server with Onsite and Offsite Clients

#### Omnipresent Access Overview

For InfiniTime access from any location:

- The Company Valid IP Address table must be left blank
- Users can access from any location as long as their Employee Valid IP address table is blank
- Access for specific employees can be limited using the Employee Valid IP Address table

#### Mixed Access Configuration

For a configuration where:

- Administrators and payroll staff need access from anywhere
- Onsite access is restricted to specific departments
- Remote access is limited to company buildings only

Steps:

1. Leave the Company Wide Valid IP Address table blank
2. Configure Employee Specific Valid IP Addresses for employees requiring restricted access
3. Leave Employee Specific Valid IP Address tables blank for employees needing omnipresent access
4. For new employees, remember to configure their Employee Specific Valid IP Address tables to prevent unintended remote access

**Note:** When a single Valid IP Address is added to an employee's record, they will be denied access from all other IP addresses not specified in their table.
