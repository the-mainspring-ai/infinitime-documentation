xml version="1.0" encoding="utf-8"?





Job Costing Configuration




# Job Costing Configuration

For information regarding what types of information can be entered into Departments, Jobs, and Tasks for Job Costing purposes please refer to the [Job Costing Introduction](/InfiniTime/help%20file/Job_Costing_Introduction.md). Remember any combination of Internal Departments, Jobs / Customers, and Tasks can generally be used within these areas of InfiniTime.

Configuring Departments

Departments within InfiniTime are used as the first Job Costing Level. It should be noted that departments are a required field within the application and as such all employee activity will be associated with a Department. It is important to keep this information in mind when using Departments for Job Costing purposes. Since all employee activity will be associated with a Department steps should be taken to ensure InfiniTime Departments correspond to the highest level of Job Costing information.

For example many office companies consider Internal Departments the highest Job Costing Level in order to ensure all employee activity is related to a specific category of work such as Payroll, Shipping, Technical Support, and Programming. Manufacturing may prefer to use Customers or Job Numbers as the highest level in order to ensure all employee activity is related to a Customer or Job.

To Configure Departments within InfiniTime for use with Job Costing:

1.) Identify the type of information which will be tracked in InfiniTime Departments.

2.) It often helps to create a list all current items under the chosen type of information. For example if Job Numbers are to be used as the first Job Costing Level list all current Job Numbers and any related information. Depending on the information being tracked within InfiniTime the list should contain the following:

| Information Type | Department Description Field | Department Cost Center Field | Department Number Field |
| Internal Departments | Department Name | Alphanumeric Code or other Payroll Identifier | Department Number |
| Customers / Jobs | Customer or Job Name | Alphanumeric Code or other Payroll Identifier | Customer / Job Number |
| Tasks | Task Name | Alphanumeric Code or other Payroll Identifier | Task Number |

3.) Create one department for each listed item. Ensure the Cost Center and Department Numbers are configured appropriately.

To Insert a Department:

1.) Click on the Department Button on the main toolbar to open the Department Table.

![](images_2/JobCosting_Config_1.gif)

2.) Click on Insert.

![](images_2/JobCosting_Config_2.gif)

3.) Enter the appropriate information as shown.

![](images_2/JobCosting_Config_3.gif)

4.) Click OK to save the record.

![](images_2/JobCosting_Config_4.gif)

Configuring Jobs

Jobs within InfiniTime are used as the second Job Costing Level. Jobs commonly relate to individual Jobs or Invoices under which tasks are performed though they may also be used for other types of information.

To Configure Jobs within InfiniTime for use with Job Costing:

1.) Identify the type of information which will be tracked in InfiniTime Jobs.

2.) It often helps to create a list all current items under the chosen type of information. For example if customers are to be used as the second Job Costing Level list all current customers and any related information. Depending on the information being tracked within InfiniTime the list should contain the following:

| Information Type | Job Description Field | Job Cost Center Field | Job Number Field |
| Internal Departments | Department Name | Alphanumeric Code or other Payroll Identifier | Department Number |
| Customers / Jobs | Customer or Job Name | Alphanumeric Code or other Payroll Identifier | Customer / Job Number |
| Tasks | Task Name | Alphanumeric Code or other Payroll Identifier | Task Number |

3.) Create one job for each listed item. Ensure the Cost Center and Department Numbers are configured appropriately.

To Insert a Job:

1.) Click on Lookups - Employee Setup - Job Costing Information - Activity Jobs to open the Activity Jobs Table.

![](images_2/JobCosting_Config_5.gif)

2.) Click on Insert.

![](images_2/JobCosting_Config_7.gif)

3.) Enter the appropriate information as shown.

![](images_2/JobCosting_Config_6.gif)

4.) Click OK to save the record.

![](images_2/JobCosting_Config_4.gif)

Configuring Tasks

Tasks within InfiniTime are used as the third Job Costing Level. It should be noted that Jobs must exist within the InfiniTime Software before Tasks can be configured. Attempting to insert a Task before configuring at least one job will result in the warning below. Tasks are the lowest Job Costing Level available in the InfiniTime software and are generally used to track various activities performed by employees though they may also be used for other types of information.

To Configure Tasks within InfiniTime for use with Job Costing:

1.) Identify the type of information which will be tracked in InfiniTime Tasks.

2.) It often helps to create a list all current items under the chosen type of information. For example if employees perform ten tasks on a regular basis for any given job then list all current tasks and any related information. Depending on the information being tracked within InfiniTime the list should contain the following:

| Information Type | Task Description Field | Task Cost Center Field | Task Number Field |
| Internal Departments | Department Name | Alphanumeric Code or other Payroll Identifier | Department Number |
| Customers / Jobs | Customer or Job Name | Alphanumeric Code or other Payroll Identifier | Customer / Job Number |
| Tasks | Task Name | Alphanumeric Code or other Payroll Identifier | Task Number |

3.) Create one task for each listed item. Ensure the Cost Center and Department Numbers are configured appropriately.

To Insert a Task:

1.) Click on Lookups - Employee Setup - Job Costing Information - Activity Tasks to open the Activity Tasks Table.

![](images_2/JobCosting_Config_8.gif)

2.) Click on Insert.

![](images_2/JobCosting_Config_9.gif)

3.) Enter the appropriate information as shown.

![](images_2/JobCosting_Config_10.gif)

4.) Click OK to save the record.

![](images_2/JobCosting_Config_4.gif)

Employee Job Costing Settings

Employee's can be assigned to a Default Department, Job, and Task. In this way employee activity will be automatically associated with a specific Department, Job, and/or Task when they punch in. Employees can also use the Transfer Button or the Employee and Punch Modules to switch between Departments, Jobs and Tasks throughout the day. The transfer button varies in location and use for each hardware terminal. Please refer to the appropriate manual for your Hardware Device in the Hardware section of this document for additional information.

To Assign a Default Department, Job, or Task to an employee:

1.) Click on the Employee Button on the main toolbar to open the employee table.

![](images_2/JobCosting_Config_11.gif)

2.) Select the employee you wish to configure Job Costing Settings for from the list and click change.

![](images_2/JobCosting_Config_12.gif)

3.) Click on the Settings Tab.

![](images_2/JobCosting_Config_13.gif)

4.) Select the Department, Job, or Task you would like to assign as the employee's default. It should be noted the Job and Task fields will not be displayed until at least one Job or Task is configured within InfiniTime. This simplifies the display of the Settings Tab for companies who do not utilize Job Costing.

![](images_2/JobCosting_Config_14.gif)

Note: Only the Default Department is required.  The Default Job and Default Task fields are not required as some companies may not wish all employees to have their activity associated with a Job or Task by default. In this way Office workers who simply work in a department.

Displaying Job Costing information within the Company and Employee Specific Timecard Tables

Job Costing is disabled by default within the InfiniTime Application. As such Job Costing related fields such as Task and Job must be added to the grid in the Company Timecard Table and Employee Specific Timecard Table. It is only necessary to configure these settings once. The software will save any alterations made to the grid. It should be noted the grid configuration is a global setting which effects all users. Additional information on Grid Configuration can be found in the [Customizing InfiniTime](/InfiniTime/help%20file/Overview/SoftwareOverview/Modules/User_Interface/FormCompletion/Customizable_Table_Display__The_InfiniTime_Grid.md) section of this document.

To add the Task and Job Fields to the Company Timecard Table:

1.) Click on the Timecard Button in the main toolbar to open the Company Timecard Table

![](images_2/JobCosting_Config_15.gif)

2.) Click on the 'Select Grid Columns' button. ( ![](images_2/grd-(10).gif))

![](images_2/JobCosting_Config_16.gif)

3.) Locate the Task and Job Fields on the 'Available' list and click on ![](images_2/ColSel_Sel.gif) to move them to the 'Selected' list.

![](images_2/JobCosting_Config_17.gif)

4.) Use the ![](images_2/ColSel_Up.gif) and ![](images_2/ColSel_Down.gif) buttons to move the Task and Job Fields up and down in the list to alter order columns will be displayed in.

![](images_2/JobCosting_Config_18.gif)

5.) Click Apply to confirm and save your changes.

![](images_2/JobCosting_Config_19.gif)

6.) The Job and Task fields will be displayed in the Timecard Table.

![](images_2/JobCosting_Config_20.gif)

Configuring Wages

It is not uncommon for employee wages to vary based upon the task, job, or department, where employees are working. Wages within InfiniTime can be allocated to a specific Job, Task, Department, or any combination thereof. Additional information on how to use wages with Job Costing can be found in the [Job Costing - Wages](/InfiniTime/help%20file/Job_Costing_-_Wages.md) section of this document.

To Configure Wages for use with Job Costing:

1.) Click on the Employee Button on the main toolbar to open the employee table.

![](images_2/JobCosting_Config_11.gif)

2.) Select the employee you wish to configure Wages for from the list and click change.

![](images_2/JobCosting_Config_12.gif)

3.) Click on the Wages Category.

![](images_2/ud11.gif)

4.) Click on Insert

![](images_2/JobCosting_Config_22.gif)

5.) Choose a combination of Department, Job, or Task for which the wage will apply.

![](images_2/JobCosting_Config_23.gif)

6.) Click OK to save the record.

![](images_2/JobCosting_Config_4.gif)