---
title: "Security Roles"
description: "An overview of the security features in the InfiniTime Time and Attendance Web Application, including role-based access control, CAPTCHA, password management, and other protective measures."
---

# Security

## Security Roles

Security Roles define the actions an employee may perform after logging into the software. They provide options for configuring access to specific windows and individual buttons, allowing complete control over employee access to different sections of the software.

InfiniTime includes four default security roles:

1. **Administrator**

   - Complete access to the entire software application
   - Cannot be edited to prevent accidental lockout
   - Full privileges for security configuration and grid management

2. **Payroll Clerk**

   - Complete access to the software application
   - Can be edited to limit access as needed
   - Cannot edit software security or configure the grid

3. **Supervisor**

   - View-only access to the entire software application
   - Can be edited to grant additional permissions
   - Cannot edit software security or configure the grid

4. **Employee**
   - Highly limited software access
   - Can be edited to grant additional permissions if needed
   - Access limited to Employee Module and InfiniTime Punch Modules

### Security Role Classes

Security Roles are assigned classes to designate default settings. This system helps establish the general security access level for user-created Security Roles:

- **Employee Class**: Default permissions match the Employee Role
- **Payroll Clerk Class**: Default permissions match the Payroll Clerk Role

Security roles can be edited using Security Keys throughout the application to grant or restrict access as needed.

## Security Keys

Security Keys are present on each window throughout the InfiniTime Application, providing administrators with the ability to view and edit security configuration. There are three types of windows with different security configurations:

### Window Types and Security Configuration

1. **Table Browse Windows**

   - Lists multiple items in a table/grid format
   - Single security option: 'Allow Access'
   - Controls whether users can view the window

2. **Update Form Windows**

   - Called using Insert or Change buttons from Table Browse Windows
   - Includes Security, Default, and Required tabs
   - Security tab options: Normal, Hidden, or Disabled for each field

3. **Procedure Security**
   - Controls access to buttons and actions
   - Accessed via Grid Security Key
   - Enables/disables specific buttons on a window-by-window basis

## Security Filters

Security Filters control an individual's access to other employees within the software. They determine which employees a user can view and edit information for, based on their Security Role permissions.

### Filter Types

1. **Selected Employees**

   - Select individual employees for access
   - Often used to limit employees to viewing only their own information

2. **Selected Departments**

   - Select departments for access
   - Grants access to all employees within selected departments
   - Most common method for configuring employee security filters

3. **Selected Groups**

   - Select groups for access
   - Provides access to all employees within specified groups
   - Recommended to create 'Unassigned' groups for each group level

4. **Range Selections**
   - Filter by employee ID, department number, pay method, or pay type
   - Disabled by default
   - Rarely used for Security Filter purposes

### Best Practices

- Create 'Unassigned' groups for each group level
- Ensure supervisors have access to 'Unassigned' groups
- This prevents issues when employees are created without group assignments
