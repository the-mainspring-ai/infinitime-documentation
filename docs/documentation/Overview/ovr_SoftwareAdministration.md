---
title: "InfiniTime Administration Guide"
description: "Comprehensive overview of InfiniTime 7.08 software administration tools and utilities for managing access, backups, hardware configuration, and data review."
---

# InfiniTime Administration

## Software Administration Introduction

InfiniTime 7.08 includes several tools and
utilities for use by Software Administrators for typical tasks such as:

- Restricting access to InfiniTime
  Features and Functionality for End Users as appropriate based on the
  End User's role within the InfiniTime
  Software
- Creating a Single File Backup which includes all InfiniTime Time & Attendance Data
- Restoring all InfiniTime
  Time & Attendance Data from a Single File Backup Created by the
  InfiniTime Software
- Performing the initial configuration for Time & Attendance
  Hardware Devices
- Monitoring the Status of Time & Attendance Hardware Devices
- Testing Communication between the InfiniTime
  Server and Time & Attendance Hardware Devices
- Undoing Accidental or Unintentional User Actions
- Reviewing Raw Punch Data as collected from Time & Attendance
  Hardware Devices

## InfiniTime Deployment

Upon completion of the Installshield Wizard, the 'InfiniTime 7.0'
and 'Client Shortcuts' folders will be created on the desktop of the InfiniTime Server. The InfiniTime 7.0 Folder
includes shortcuts to the InfiniTime
Modules for use from the InfiniTime
Server while the 'Client Shortcuts' folder includes shortcuts to the InfiniTime Modules for use from client
machines on the Local Area Network.

As a web application accessed through a Web Browser, no installation
is required for workstations to access the InfiniTime
Software from the Local Area Network. To provide users with access to
InfiniTime, simply copy
the 'Client Shortcuts' folder from the InfiniTime
Server's desktop to all workstations which require access to the InfiniTime Software.



## Backup & Restore

### Backup & Restore Introduction

InfiniTime 7.0
includes a complete backup and restore system designed to minimize downtime
should hardware or software failures occur. Inception Technologies
recommends use of the automatic backup feature in order to keep your InfiniTime Database backed up on a
routine basis. Third Party System Backup utilities are not recommended
as a substitute for the InfiniTime
Backup as Oracle Database
files cannot be backed up in a reliable fashion unless specific Oracle
Utilities
are utilized. It should also be noted that InfiniTime
backup files can only be created and restored on the InfiniTime
Server.

For this reason, simply copying the main program
file location (C:\Inception\
by default) is not a substitute for the internal InfiniTime backup system.
An Oracle Database cannot be restored from the program files alone.

The directory where the backup (\*.ITB) file is created is âC:\Inception\InfiniTime\InfiniTime7\Backupâ
assuming the default directories were used during installation. This directory should be routinely copied
to removable storage in order to safeguard your data.

### Creating a Backup in InfiniTime

- Open the Manager module on the
  InfiniTime server and
  hover your mouse over âFileâ
- Click
  on âBackup / Restoreâ.

![](/img/insert_QS.gif)

- A new window as pictured below
  entitled âBackup/Restore Tableâ will open. Click on the âBackupâ button
  at the bottom as shown to start the backup.

![](/img/rb5.gif)

When you click on âBackupâ the process
begins and youâre screen will look like the picture below.

![](/img/TP8.gif)

After the DOS window is terminated, the
âCreating Backupâ window will remain until the backup is complete.

After the backup finishes the âBackup /
Restore Tableâ will come back on top.  You will now see a folder
titled âBackup Folderâ in the window. There will also be a file under
the folder, this file is the backup file.  In the picture below,
the number 1 arrow shows youâre companies name and the number 2 will show
you the date and time the backup was created. Should you ever need to
restore your database, you will know which one to choose by date and time.
 Now you can click the close button and continue with program usage.

![](/img/i20.gif)

### Configuring Backup Options

InfiniTime Backup includes
four options that can be used to configure the automatic backup procedure.
Details are provided below.

![](/img/Ch11_Export9.gif)

Backup Files
Every â Specify the amount of days between backups. InfiniTime will perform the first
automatic backup on the start date. Subsequent backups will be performed
after a certain period of time specified by this quantity. The drop down
box allows the user to specify between days or weeks.

Start Time
â If enabled, Automatic backup will execute at time set in this box.

Start Date
âAutomatic backups will begin on this date, at the time specified in the
Start Time field.

Delete Oldest
Files After â InfiniTime
will continue creating backup files according to the defined schedule
until the number of backups reach the amount specified in this field.
The oldest backup will then be deleted as a new file is created.

### Restoring a Backup

- Click on File.
- Click on Backup / Restore.

![](/img/cset29.gif)

- Highlight the backup file you wish to restore by clicking on it.

![](/img/RLSNote_707_1.jpg)

- Click Restore. It should be noted that all users must be out of
  the InfiniTime software
  in order to restore the backup. If there are users logged into the
  software a warning will be displayed and the restore will be aborted.
  If you receive this error users can be kicked out of the software
  by restarting the OracleServiceTCDBS
  service.

![](/img/cset20.gif)

- No further action is required from the user, InfiniTime
  will automatically perform all necessary operations to restore the
  backup file.
- InfiniTime will
  automatically backup the data currently in your software before restoring
  the backup. This prevents accidental restoration of an older backup
  file, which would result in data loss.

![](/img/ph2.gif)

- Once the backup is finished InfiniTime
  will restore the previously selected backup file.

![](/img/cset4.gif)

- The above window will close automatically when the restore is complete.
  Once the restore is completed, the InfiniTime
  Manager Module should be closed and reopened before use.

### Deleting Backup Files from within InfiniTime

InfiniTime Backup files
can be removed from the InfiniTime
Backup folder by selecting them from the backup list and clicking the
delete button.

- Open the InfiniTime
  Manager Module on the Server.
- Click on File.
- Click on Backup.

![](/img/Ch11_Export12.gif)

- Click on the Plus to the left of the Backup Folder if it is not
  already open.

![](/img/Ch11_Export11.gif)

- Highlight the backup file you wish to delete by clicking on it.

![](/img/CH11_ImportFields_Badge.gif)

- Click Delete.

![](/img/i17.gif)

### E-mailing a Backup File from within InfiniTime

InfiniTime Backup files
can be e-mailed from the backup window itself by clicking on the Email
button while a backup is highlighted. Follow the instructions below.

- Click on File.
- Click on Backup / Restore.

![](/img/override_Tab.gif)

- Highlight the backup file you wish to email by clicking on it.

![](/img/TaskImport.gif)

- Click on the Email Button.

![](/img/Ch11_Export21.gif)

- Fill out the Email Form shown below. The email will be sent via
  the STMP Email Server Configuration on the InfiniTime
  Server in  Microsoft Internet Information Services.

![](/img/RLSNOTE_707-06.jpg)

| Related Links |
| ------------- |

### How to Create a Backup from a Client Machine

InfiniTime provides for
initiating a backup of the InfiniTime
database from a client machine which eliminates the need to access the
InfiniTime Server.

To Create a Backup from a Client Machine:

1. Open
   the Manager module on the server and click on File.
2. Click
   on Backup / Restore.

![](/img/i16.gif)

3. The Backup / Restore Table will
   be displayed. When viewed from a client machine a Backup Status Indicator
   is displayed on the top of the window as shown. Click on Backup to
   start a backup.

![](/img/i28.gif)

4. The Last Backup Date and Time will
   be cleared which instructs the InfiniTime
   Housekeeping Service to begin taking a backup.

![](/img/cset18.gif)

5. Clicking Refresh at the bottom of
   the Backup / Restore Table will display the current backup status.
   The Backup Status will return to Idle and the Last Backup Date and
   Time fields will be filled when the backup is complete.

Client Initiated Backup In Progress:

![](/img/cset20.gif)

Client Initiated Backup Complete:

![](/img/i12.gif)

## Reader Configuration

### Reader Configuration Table

The reader configuration table lists all devices that are connected
to the InfiniTime software.
The reader configuration table provides a convenient location for testing
device connectivity, updating reader programming, and updating employee
data contained in a readerâs database. Before a clock can be used to poll
timecard activity, the clock must be configured. Detailed configuration
and installation instructions are available for each InfiniTime
compatible time collection device.

Accessing the Reader Configuration Table

- Open the Reader Configuration Table

- Click on Lookups

![](/img/maint2.gif)

- Click
  on Reader Configuration

The Reader Configuration Table will open.
The reader configuration table is organized in a tree structure similar
to that used by Windows Explorer. A separate folder, or reader type entry,
 is displayed for each hardware model according to its connection
type. In this way readers of the same model and connection type are grouped
together. There are two steps to configuring a reader within the InfiniTime Application. First the
Reader Type entry must be defined. By default, clicking insert will open
the reader configuration update form, making it possible for the user
to specify the type and connection method for their readers. When this
information is saved the reader type entry is created. Two examples of
reader entry types are shown below.

![](/img/cb1.gif)

After a reader entry type has been created
a reader address entry must be defined. To insert a reader address entry
follow the steps below.

1.) Expand the Reader
Type Entry by clicking on the plus sign.

![](/img/CH11_ImportFields_Badge.gif)

2.) Click on None and Click Insert to open
the Reader Configuration Update Form.

![](/img/HousekeepingSvcStopped.gif)

### Reader Configuration Update Form

![](/img/RLSNOTE_707-05.jpg)

Port Name: Enter a name for
your clock. This name should be recognizable and descriptive, as it will
be displayed in the Reader Configuration Table representing the record
for your clock.

![](/img/CH11_ImportFields_Shifts.gif)

Type: Select your Clock Model
from the models in the list. NOTE: A scout 1000 requires a different configuration
than other Scout Models. Select the Scout 1000 type if you have a Scout 1000.

![](/img/cset34.gif)

Port: Select the port that corresponds
to your reader. Select TCP/IP if you are using an Ethernet connection
to communicate with your clock.

![](/img/maint3.gif)

Poll From File: Some readers
such as the Luna and Zephyr support the Poll From File Feature. Using
the menu at the clock punches can be downloaded to a USB Thumb drive and
transferred to a PC. This is especially useful for sites without a network
or internet access. Refer to Hardware Documentation Zephyr or  Hardware
Documentation Luna for additional information on configuring and using
poll from file.

Baud Rate: Select the communication
baud rate that corresponds to your reader. The same Baud Rate must be
set on the reader and the software in order for the device to communicate
successfully. Refer to the section of this document that corresponds to
your specific timeclock model for more information.

Default Baud Rate

| Older Synel Readers                 | 9600  |
| ----------------------------------- | ----- |
| New Synel Readers                   | 19200 |
| Direct Connect Scout\* Hand Readers | 9600  |
| Scout\* Hand Readers (Modem)        | 9600  |

\*Refers to All Scout Models (1000 - 4000)

Data Processing Every: Here
you can decide how often you want the data to be processed. The automatic
setting will process and post employee activity as soon as it is retrieved
from the reader.  If you want to process the data according to a
specific time interval you can select an increment of time in which to
process the data.  If you select an increment of time the data that
is polled will not be processed until the time selected.  The data
is stored in the polled information and then once the time comes to process
the data is then when it will show in the activity of the employee.

_Note_: Automatic is generally
the preferred setting for Data Processing. In this way employee timecard
activity is automatically processed when it is polled from the reader.

Last Data Process Date: Displays
the date on which data was last processed.

Last Data Process Time: Displays
the time at which data was last processed.

### Reader Addresses Tab

![](/img/eb2.gif)

The Reader Address Update form, as shown when inserting a new reader
configuration or changing an existing reader configuration, is connection
method and clock specific. The information available for configuration
on the Reader Address Update form changes according to the clock type
and connection method selected. This setup eliminates unnecessary information
within the Reader Address Update form and assists users with configuring
options specific to their chosen clock model and connection type. The
following tables show which configuration settings are available according
to connection and clock type.

| Reader Type             | Apollo | Atlas  | Odyssey | Omega  | Orion  | Plus   | Scout  | Scout 1000 | SY-400 |
| ----------------------- | ------ | ------ | ------- | ------ | ------ | ------ | ------ | ---------- | ------ |
| Connection Method       | Direct | Direct | Direct  | Direct | Direct | Direct | Direct | Direct     | Direct |
| Access Control Settings | X      | X      | X       | X      | X      |        | Xâ¦    |            | X      |
| Bell Schedules          | X      | X      | X       | X      | X      |        | Xâ¦    |            | X      |
| Communication Errors    | X      | X      | X       | X      | X      |        | X      | X          | X      |
| General - TCP/IP Tab    |        |        |         |        |        |        |        |            |        |
| Synel Options           | X      | X      | X       | X      | X      |        |        |            | X      |
| Scout Options           |        |        |         |        |        |        | X      | X          |        |

â¦Scout 2000 is not compatible
with access control or bells.

| Reader Type             | Apollo | Atlas | Odyssey | Omega | Orion | Scout | Scout 1000 | SY-400 |
| ----------------------- | ------ | ----- | ------- | ----- | ----- | ----- | ---------- | ------ |
| Connection Method       | Modem  | Modem | Modem   | Modem | Modem | Modem | Modem      | Modem  |
| Access Control Settings | X      | X     | X       | X     | X     | Xâ¦   |            | X      |
| Bell Schedules          | X      | X     | X       | X     | X     | Xâ¦   |            | X      |
| Communication Errors    | X      | X     | X       | X     | X     | X     | X          | X      |
| General - TCP/IP Tab    |        |       |         |       |       |       |            |        |
| Synel Options           | X      | X     | X       | X     | X     |       |            | X      |
| Scout Options           |        |       |         |       |       | X     | X          |        |

â¦Scout 2000 is not compatible
with access control or bells.

| Reader Type             | Apollo | Atlas  | Odyssey | Omega  | Orion  | Scout  | Scout 1000 | SY-400 |
| ----------------------- | ------ | ------ | ------- | ------ | ------ | ------ | ---------- | ------ |
| Connection Method       | TCP/IP | TCP/IP | TCP/IP  | TCP/IP | TCP/IP | TCP/IP | TCP/IP     | TCP/IP |
| Access Control Settings |        | X      | X       |        | X      | Xâ¦    |            | X      |
| Bell Schedules          |        | X      | X       |        | X      | Xâ¦    |            | X      |
| Communication Errors    | X      | X      | X       | X      | X      | X      | X          | X      |
| General - TCP/IP Tab    | X      | X      | X       | X      | X      | X      | X          | X      |
| Synel Options           | X      | X      | X       | X      | X      |        |            | X      |
| Scout Options           |        |        |         |        |        | X      | X          |        |

â¦Scout 2000 is not compatible
with access control or bells.

### Configuring Reader Addresses

- Click Insert to open the Reader Address Configuration Form.

![](/img/21DHOLAVG.jpg)

General Reader setup differs depending on the clock model and connection
type. For this reason, two explanations of General Reader setup are provided.
One for the TCP/IP Communication Method and one for the Direct and Modem
Connection Communication Methods.

### TCP/IP Communication Method Settings

### TCP/IP General Tab

![](/img/Import_Auto_2.gif)

Address: Enter the Reader Address assigned to the clock during setup.
Refer to the section of this document that corresponds to your specific
timeclock model for setup instructions.

Description: Enter a name for
your clock. This name should be recognizable and descriptive in nature.
It will be displayed in the Reader Address Configuration Table representing
the Reader Address Configuration Record for your clock. It is important
to note that each clock will generally have only one Reader Address entry
unless they are arranged in a daisy chain configuration with multiple
readers on one communications port.

Connection Type: TCP/IP is the
only option available in this drop down as TCP/IP was previously specified
as the connection type.

Ignore Duplicate Scans Received: InfiniTime
can ignore multiple scans for a single employee within a specific time
window. Enter the time window, in minutes, for duplicate scans should
be ignored.

Department: Many companies purchase
multiple readers and locate them throughout their facility for use with
a single department. Selecting a specific department from this drop-down
menu will cause InfiniTime
to associate all punches from this reader to the selected department.
All Departments are selected by default. Timecard Activity is automatically
associated to an employees default department when All Departments is
selected.

Total Hours Type: Specify the
Total hours type that will be displayed for viewing on the reader.

- Daily: Sends daily hour
  totals to the clock for employee viewing purposes.
- Weekly: Send hourly totals
  for the current week to the clock for employee viewing purposes.
- Pay Period:
  Sends hour totals for the current pay period to the clock for employee
  viewing purposes.

_NOTE_: Selecting Weekly or Pay
Period can quickly fill the memory on most timeclock models. It is important
to poll employee timecard activity often if either of these settings is
selected.: Enter the Reader Address assigned to the clock during setup.
Refer to the section of this document that corresponds to your specific
timeclock model for setup instructions.

\*\* Synel Badge Readers Only \*\*

The following items will only be displayed
if the clock type you have selected is a Synel Badge Reader. (Apollo/Atlas/Odyssey/Omega/Orion/Plus/SY 400)

![](/img/RLSNOTE_707-03.jpg)

Reader
Type: Select the appropriate badge reader type that corresponds
to the type of badge reader installed in your Synel clock. Choices are
Barcode, Magstripe, or Proximity depending on reader model.

- Barcode
  Badges: Barcode badges are recognizable by the large barcode
  symbol on the front of the card.
- Magstripe
  Badges: Magstripe badges are recognizable by the magnetic strip
  on the back of the card, similar to the strip found on the back of
  a credit card.
- Proximity
  Badges: Proximity badges have no identifiable external markings.
  To clock in or out they are simply passed in front of a compatible
  terminal.

Badge
Start Position:  Defaults to 1. Choose the appropriate starting
position for use with your badges. This setting generally does not need
to be altered for Magstripe or Barcode Badges.

Badge
End Position: Defaults to 8. Choose the appropriate end position
for use with your badges. This setting generally does not need to be altered
for Magstripe or Barcode Badges.

Barcode
Symbology: Choose the appropriate barcode symbology for use with
your badges. All badges sold by Inception Technologies use the default
barcode symbology Code 3 of 9. Some customers have distributed badges
to their employees using a different barcode symbology. In many cases,
depending on badge size and make, this setting allows these badges to
be utilized with the InfiniTime
system.

### TCP/IP Polling Tab

![](/img/RLSNOTE_707-03.jpg)

Polling Interval: Choose how
often you would like to poll timecard activity from your reader. Minimum
polling times are displayed below according to clock model.

| Reader Type              | Apollo     | Atlas      | Odyssey    | Omega      | Orion      | Plus | Scout     | Scout 1000 | SY-400     |
| ------------------------ | ---------- | ---------- | ---------- | ---------- | ---------- | ---- | --------- | ---------- | ---------- |
| Minimum Polling Interval | 30 Seconds | 30 Seconds | 30 Seconds | 30 Seconds | 30 Seconds | N/A  | 5 Seconds | 5 Seconds  | 30 Seconds |

| Reader Type | Athena | Juno | Luna | Thor | Zephyr |
| Minimum Polling Interval | 5 Seconds | 5 Seconds | 5 Seconds | 5 Seconds | 5 Seconds |

Last Poll Date: Displays the
date on which the clock was last polled.

Last Poll Time: Displays the
time at which the clock was last polled.

Data Update Interval: Choose
how often you would like to update employee data to the clock. Employee
data includes new employees, employee ids, and changes in employee badges
as well as hour totals. This process can take as much as ten minutes,
during which employees will not be able to punch. Generally this is only
required once at the beginning or end of the work day according to user
preference. During software setup users may wish to manually update their
clocks in order to test employee information rather than waiting for the
clock to automatically update.

Last Data Update Date: Displays
the date on which the clock was last updated.

Last Data Update Time: Displays
the time at which the clock was last updated.

Set Time At Device: Causes the
InfiniTime software to
update the time on the reader according to the system clock. Selecting
no disables this feature.

Time Zone: This setting is used
to set the time at the reader. Ensure time zone chosen corresponds to
the time zone where the clock is located. This is often used for TCP/IP
or modem clocks in a remote location relative to the InfiniTime
server.

Polling From Time: This field
is used in conjunction with the âPolling To Timeâ field in order to specify
a time range for polling. The reader will start polling at the Polling
from time, and continue to poll according to the specified polling interval
until the Polling To Time is reached. Enter the time at which the reader
should start polling in this field.

Polling To Time: See Polling
From Time for a detailed explanation. Enter the time at which the reader
should stop polling in this field.

### TCP/IP Tab

![](/img/Ch11_Export19.gif)

TCP/IP Address: Enter the IP
address assigned to your reader. This must be a static address. Refer
to the section of this document that corresponds to your specific timeclock
model for more information on configuring this address within the reader.

Port Number: Enter the network
communications port used to communicate with your clock. Generally, this
only needs to be altered if you are positive the default port is in use
by another application on your network. The same port must be set in the
InfiniTimesoftware and
on the reader in order for communication to be successful. Refer to the
section of this document that corresponds to your specific timeclock model
for more information.

TCP/IP Timeout: Specify the
amount of seconds to wait before the TCP/IP connection with the reader
times out. Ninety seconds is the recommended value.

### Direct Connect and Modem Communication Type Settings

### Direct Connect and Modem Communication Type Settings - General Tab

![](/img/cb3.gif)

Address: Enter the Reader Address
assigned to the clock during setup. Refer to the section of this document
that corresponds to your specific timeclock model for setup instructions.

Description: Enter a name for
your clock. This name should be recognizable and descriptive in nature.
It will be displayed in the Reader Address Configuration Table representing
the Reader Address Configuration Record for your clock. It is important
to note that each clock will generally have only one Reader Address entry
unless they are arranged in a daisy chain configuration with multiple
readers on one communication port.

Connection Type: When a COM
port is selected on the Port Information Screen in the Reader Configuration
Update form two options are available in this field. Specify whether the
communications port connects directly to the clock (Direct), or if the
communications port is connected to a modem, which will be used to connect
to a remote clock (Modem).  If Modem is selected the modem tab, as
outlined below, will become available.

_Note_:
More than one Modem clock can be polled using the same communications
port and modem. A complete reader entry is required for each clock. Do
not attempt to add additional Reader Address Entries to a single reader
entry for each remote clock.

Department: Many companies purchase
multiple readers and locate them throughout their facility for use with
a single department. Selecting a specific department from this drop-down
menu will cause InfiniTime
to associate all punches from this reader to the selected department.
All Departments are selected by default. Timecard Activity is automatically
associated to an employees default department when All Departments is
selected.

Total Hours Type: Specify the
Total hours type that will be displayed for viewing on the reader.

- Daily: Sends daily hour
  totals to the clock for employee viewing purposes.
- Weekly: Send hourly totals
  for the current week to the clock for employee viewing purposes.
- Pay Period: Sends hour
  totals for the current pay period to the clock for employee viewing
  purposes.

_NOTE_: Selecting Weekly or Pay
Period can quickly fill the memory on most timeclock models. It is important
to poll employee timecard activity often if either of these settings is
selected.: Enter the Reader Address assigned to the clock during setup.
Refer to the section of this document that corresponds to your specific
timeclock model for setup instructions.

\*\* Synel Badge Readers Only \*\*

The following items will only be displayed
if the clock type you have selected is a Synel Badge Reader. (Apollo/Atlas/Odyssey/Omega/Orion/Plus/SY 400)

![](/img/i18.gif)

Reader
Type: Select the appropriate badge reader type that corresponds
to the type of badge reader installed in your Synel clock. Choices are
Barcode, Magstripe, or Proximity depending on reader model.

- Barcode
  Badges: Barcode badges are recognizable by the large barcode
  symbol on the front of the card.
- Magstripe
  Badges: Magstripe badges are recognizable by the magnetic strip
  on the back of the card, similar to the strip found on the back of
  a credit card.
- Proximity
  Badges: Proximity badges have no identifiable external markings.
  To clock in or out they are simply passed in front of a compatible
  terminal.

Badge
Start Position:  Defaults to 1. Choose the appropriate starting
position for use with your badges. This setting generally does not need
to be altered for Magstripe or Barcode Badges.

Badge
End Position: Defaults to 8. Choose the appropriate end position
for use with your badges. This setting generally does not need to be altered
for Magstripe or Barcode Badges.

Barcode
Symbology: Choose the appropriate barcode symbology for use with
your badges. All badges sold by Inception Technologies use the default
barcode symbology Code 3 of 9. Some customers have distributed badges
to their employees using a different barcode symbology. In many cases,
depending on badge size and make, this setting allows these badges to
be utilized with the InfiniTime
system.

### Direct Connect and Modem Communication Type Settings - Polling Tab

![](/img/TP5.gif)

Polling Interval: Choose how
often you would like to poll timecard activity from your reader. Minimum
polling times are displayed below according to clock model.

| Reader Type                | Apollo     | Atlas      | Odyssey    | Omega      | Orion      | Plus | Scout     | Scout 1000 | SY-400     |
| -------------------------- | ---------- | ---------- | ---------- | ---------- | ---------- | ---- | --------- | ---------- | ---------- |
| Minimum Polling Intervalâ¦ | 30 Seconds | 30 Seconds | 30 Seconds | 30 Seconds | 30 Seconds | N/A  | 5 Seconds | 5 Seconds  | 30 Seconds |

â¦Readers
using the modem connection method should not be polled more often than
4 hours.

Last Poll Date: Displays the
date on which the clock was last polled.

Last Poll Time: Displays the
time at which the clock was last polled.

Data Update Interval: Choose
how often you would like to update employee data to the clock. Employee
data includes new employees, employee ids, and changes in employee badges
as well as hour totals. This process can take as much as ten minutes,
during which employees will not be able to punch. Generally this is only
required once at the beginning or end of the work day according to user
preference. During software setup users may wish to manually update their
clocks in order to test employee information rather than waiting for the
clock to automatically update.

Last Data Update Date: Displays
the date on which the clock was last updated.

Last Data Update Time: Displays
the time at which the clock was last updated.

Set Time At Device: Causes the
InfiniTime software to
update the time on the reader according to the system clock. Selecting
no disables this feature.

Time Zone:
This setting is used to set the time at the reader. Ensure time zone chosen
corresponds to the time zone where the clock is located. This is often
used for TCP/IP or modem clocks in a remote location relative to the InfiniTime server.

Polling From Time: This field
is used in conjunction with the âPolling To Timeâ field in order to specify
a time range for polling. The reader will start polling at the Polling
from time, and continue to poll according to the specified polling interval
until the Polling To Time is reached. Enter the time at which the reader
should start polling in this field.

Polling To Time: See Polling
From Time for a detailed explanation. Enter the time at which the reader
should stop polling in this field.

### Direct Connect and Modem Communication Type Settings - Modem Tab

![](/img/i3.gif)

Phone Numbers: Enter the phone
number, just as it would be dialed from a regular phone. Include country
and area code when appropriate.

Modem Init String: A string
of characters used to initialize the modem and begin a call. The default
string, &FE0V1, should be sufficient in most cases.

### Available Departments

InfiniTimeâ¢ allows you
to switch departments at the reader itself, in this screen you can select
which departments are allowed.

![](/img/image2.jpg)

By default, all of the departments are in the left hand side and all
departments are allowed to be used for transfer at the reader.  If
you want to assign only a few departments then you need to move those
departments to the right hand side by using the arrow buttons.

If you have any departments on the right hand side assigned to the reader
and you enter new ones on the software by default they will not be assigned
to the reader you will have to manually assign them by moving them to
the right.

### Available Activity Types

InfiniTimeâ¢ allows you
to enter other activity at the reader itself, in this screen you can select
which activity is allowed to be entered.

![](/img/CH15_Sysmon1.gif)

By default, if all of the activities are in the left hand side then
all activities are allowed to be entered at the reader.  If you want
to assign only a few activities then you need to move those activities
to the right hand side by using the arrow buttons.

If you have any activities on the right hand side assigned to the reader
and you enter new ones on the software by default they will not be assigned
to the reader you will have to manually assign them by moving them to
the right.

### Access Control Settings - General Tab

Many InfiniTime compatible
timeclocks can be used for access control purposes in order to unlock
a door when authorized employees punch. Access control settings are configured
in the Reader Address Table for each specific clock and are outlined below.
Refer to the section of this document that corresponds to your specific
timeclock model for more information about access control wiring and setup.

![](/img/CH15_Sysmon3.gif)

Access Denied Message: Type
the message to be displayed on the clock should an employee be denied
access. Access would be denied under the following conditions:

- The employee is not authorized to access this location as defined
  by their Access Control Group.
- The employee is attempting to access this location during hours
  outside of their schedule.

Access Granted Message: Type
the message to be displayed on the clock should an employee be granted
access. Access will only be granted if both of the following conditions
are met:

- The employee is authorized to access this location as defined by
  their Access Control Group.
- The employee is accessing the location during hours within the
  access control schedule or according to schedule overrides.

Lock Relay Open Duration: Set
the duration an attached lock relay will remain unlocked after access
is granted.

Door Switch Relay Open Duration:
Set the duration an attached lock relay will remain unlocked if an attached
door switch is pressed.

### Access Control Groups Tab

The Groups Tab is used to control what employees will be able to utilize
the reader to gain access to connected entry ways.

All access control groups that have been configured will be displayed
in the left side grid on the Groups Tab. No additional configuration is
necessary if all groups are to be assigned to a reader. Groups should
be assigned to a reader if only specific groups are authorized to access
the door controlled by the reader.

![](/img/ebut.gif)

To Assign Specific Groups to a Reader:

- Select the group you wish to assign
  to the reader. Use the controls in the center of the screen to assign
  a specific group to the reader as outlined below.

![](/img/CH11_ImportFields_GroupAssign.gif)
â Assigns the selected group to the reader. You will notice that the group
will be removed from the left grid and displayed in the right grid.

![](/img/maint5.gif)
â Assigns all available groups to the reader. You will notice that all
groups will be removed from the left grid and displayed in the right grid.

![](/img/i11.gif)
â Removes the selected group from the reader. You will notice that the
group will be removed from the right grid and displayed in the left grid.

![](/img/cset22.gif)
â Removes all selected groups from the reader. You will notice that all
groups will be removed from the right grid and displayed in the left grid.

### Access Control Schedule Tab

The Schedule tab can be used to specify an access control schedule specific
to the reader. Schedules configured within the Reader Configuration Update
form take precedence over default Access Control Group Schedules. If this
schedule is configured employees will only be able to access the entryway
connected to the reader during the scheduled times specified in the Reader
Configuration Update form. The schedule configured in the Access Control
Group Update form will be ignored.

Click Insert to configure the schedule. The employees specified, as
explained later in this section, will be able to pass through the access
control doorway by using the access control hardware while access is considered
Open. When access is closed the specified employees will be locked out.

![](/img/CH15_Sysmon2.gif).gif)

Open: Enter a time to consider
access to the associated doorway Open.

Close: Enter a time to consider
access to the associated doorway Closed.

Valid From: Optional. Specifies
the date that the schedule takes effect. Leave this field blank if you
wish the schedule to take effect immediately.

Valid To: Optional. Specifies
the date that the schedule expires. Leave this field blank if you do not
wish the schedule to expire.

Copy: Use this button to copy
schedule information entered on one day to another.

![](/img/image11.jpg).gif)

The example above shows schedule information being copied from Monday
to Tuesday, Wednesday, Thursday, and Friday. Clicking OK would copy the
information.

### Access Control Overrides Tab

The schedule override tab permits additional schedule entries for a
specific date. Keep in mind override entries will take precedence over
the default schedule for that date. Refer to the section above for instructions
on inserting an access control schedule.

![](/img/Ch11_Export20.gif)

_Override Example_:

An access control schedule is configured to grant access for authorized
employees from 8:00 AM to 5:00 PM on 2-5-07. Employees will be working
in the evening from 7:00 to 10:00 pm in order to perform emergency repairs.
The InfiniTime software
administrator must add a schedule override with the schedule shown below
in order for employees to be granted access to the warehouse entryway.
Remember, the default schedule for the day will be overridden. Be sure
to include the times for the default schedule and any necessary changes
in the override entry.

![](/img/Ch11_Export9.gif)

![](/img/cset7.gif)

### Access Control Always Open Tab

![](/img/e3.gif)

The Always Open Tab is used to configure time windows for which the
connected entryway is always open. During these hours the entryway will
be unlocked and authentication will not be required in order to gain entry.
Depending on security requirements it may be a good idea to unlock the
entryway during peak hours using this feature. Refer to the Schedule tab
section of this document for information on configuring access control
schedules.

Technical Note: This feature
is only supported by Scout Terminals.

### Access Control Access Log

![](/img/Ch11_Export15.gif)

The Access Log Tab keeps a record of each attempt to access the attached
entryway and whether access was granted or denied. Only employees assigned
to the administrator security role can purge the access control log.

### Bell Schedules Setup

Bell schedules are used to control a buzzer or system of bells attached
to a reader. The bells will ring at each time configured in the schedule
for the specified duration.

![](/img/RLSNOTE_707-05.jpg)

Configuring Bell Schedules

- Click Insert to open the Bell Schedule Update Form

![](/img/InLineEdit_4.jpg)

- Type a description for the bell schedule.

![](/img/CH11Export3.gif)

- Specify the duration, in seconds, for the bell to ring when activated.
- Click on the Default Schedule Tab.

![](/img/tcard09.gif)

- Click Insert to insert the first bell activation time.

![](/img/cset8.gif)

- Select the day the bell will ring on. Monday is highlighted by
  default.
- Enter the appropriate time.

![](/img/cset15.gif)

- The copy feature, as explained below, can be used to copy the time
  to another day.
- Click OK to save the entry.

_Note_: Only one activation time
can be configured per entry. Additional entries must be inserted to add
successive bell activation times.

Valid From: Optional. Specifies
the date that the bell schedule takes effect. Leave this field blank if
you want the bell schedule to take effect immediately.

Valid To: Optional. Specifies
the date that the bell schedule expires. Leave this field blank if you
do not wish the bell schedule to expire.

Copy: Use this button to copy
schedule information entered on one day to another.

![](/img/i24.gif).gif)

The example above shows schedule information being copied from Monday
to Tuesday, Wednesday, Thursday, and Friday. Clicking OK would copy the
information.

### Communication Errors Table

The Communication errors table keeps a record of any errors encountered
when communicating with the clock.

![](/img/Ch11_Export14.gif)

Communication Error Table Related Options

No. of Errors to Store: Enter
the maximum amount of errors to store in the Communication Error Table.
When the maximum number is reached the oldest errors will be removed from
the list as new errors occur. Leave this blank to keep record of all errors
that occur. Errors will not be removed from this table unless they are
deleted manually if this field is left blank.

No. of Errors Until Comm. Is Stopped:
Specify the amount of errors that can occur before the software will stop
communicating with the reader. Leaving this blank will ensure communication
is not automatically stopped.

### Synel Software Settings

![](/img/cset27.gif)

Idle Message: Enter the message
that will be displayed on the reader while the reader is in the idle state.

Idle Message Timeout: Specify
a duration, in seconds, for the clock to wait after an action before returning
to the idle state.

Public Message: The public message
is displayed after an employee successfully swipes or punches in. Specify
the message, if any, that you would like to display.

Date Format: Choose a format
for the date displayed on the reader.

Time Format: Choose a format
for the time displayed on the reader.

Port Retry Setting: Specify
the amount of times InfiniTime
should attempt to connect to the clock using the specified COM or TCP/IP
port before aborting.

Port Timeout Setting: Specify
the duration, in seconds, InfiniTime
should wait for an acknowledgement from the clock before the connection
attempt is considered a failure.

_Note_:
The Port Retry and Port Timeout settings may need to be increased to 5
tries and 25-90 seconds respectively for use with modem clocks due to
increased response times.

Modem Answer
Timeout: Specify the duration, in seconds, InfiniTime
should wait for the modem to answer.

Modem Connect
Timeout: Specify the duration, in seconds, InfiniTime
should wait for data transfer to begin before considering the connection
attempt a failure.

_Note_:
The Modem Answer Timeout and Modem Connect Timeout settings may need to
be increased to 25 and 45-90 seconds respectively for use with modem clocks
due to increased response times

Validate Employee: If this option
is checked employee badge numbers will be compared to employees within
the InfiniTime database.
If no match is found the punch will not be accepted. If a match is found
the employeeâs name will be displayed on the clock. Should this option
be unchecked the badge number read from the card will simply be displayed.
Disabling this option is useful for troubleshooting badges.

_Note_:
Access Control Requires Employee Validation. Validate Employee must be
checked for use with access control systems

User ID Only: If this option
is checked the reader will permit clocking in using only the employeeâs
user ID. The password is not required.

Badge Size Fixed: Check this
option to enable a fixed badge length according to the integer entered
in the Badge Size Field. Synel readers always return eight digits when
a badge is swiped. If a badge size of 32 is used the last eight digits
will be returned to the software. (12345678) If a badge size of 4 is used,
the last four digits will be read and four leading zeroes will be returned
to the software. (0001234)

Badge Size: Specify the fixed
badge length you wish to use. Only integer values may be used. (IE 1,2,3â¦)

Do Not Allow Department Switching:
Disables department switching at the clock.

Do Not Allow Other Activity Entry:
Disables other activity entry at the clock.

Do Not Display Punch Type At Clock:
Disables the display of Clock In or Clock out when a punch is successfully
validated.

### Synel Hardware Settings

![](/img/tcard10.gif)

Terminal Mode: Select the mode
for use with your reader. The corresponding program will be updated to
the reader when the next program update occurs. It is important to understand
how these settings alter the behavior of the clock. The function of the
default punch method, as outlined below, changes according to the selected
terminal mode.

Synel Readers

- Swipe an Employee Badge
- Press Enter
- Enter Employee ID
- Enter Password

Users may wish to manually update the reader after altering these settings
in order for them to take effect immediately. Refer to the section of
this document that corresponds to your specific timeclock model for more
information.

Time & Attendance Only

Configures the Reader for Time & Attendance usage only. In this
mode the reader cannot control entry ways or bells and can only be used
for time and attendance purposes.

Time & Attendance and Access Control

Configures the Reader for Time & Attendance and Access Control.
This mode is used to configure Time & Attendance as the primary purpose
of the reader while still allowing access control functionality. Employees
will be able to clock in & out using the default punch method, while
function keys must be used for access control purposes.

Access Control Only

Configures the reader for Access Control Only. Employees punching in
or swiping at this clock will be validated against the InfiniTime database,
though timecard activity will not be recorded for the punches. Employees
are able to access attached entry ways according to Access Control Group
Schedule Configuration. Bells can also be used under this mode.

Access Control and Time & Attendance

Configures the Reader for Time & Attendance and Access Control.
This mode is used to configure Access Control as the primary purpose of
the reader while still allowing Time & Attendance functionality. Employees
will be able to access entry ways with the default punch method, while
function keys must be used for Time & Attendance purposes.

Dual Time & Attendance and Access Control

Configures the Reader to run Time & Attendance and Access Control
in dual-purpose mode. This enables employees to clock in to work and unlock
an entryway with a single punch.

Tech. Mode Badge Number: Enter
a technician mode badge number. When a badge with this number is swiped
the reader will automatically enter technician mode. Technician Mode is
used to configure reader communication settings as well as other options
depending on clock model.

Door Relay Number: If a door
is attached to this reader, specify which relay it is connected to.

Bell Relay Number: If a bell
or bell system is attached to this reader specify which relay it is connected
to.

_Note_:
Only the Odyssey (SY-780) has interchangeable relays where each relay
can be used for bells or access control. All other Synel Readers can support
a maximum of one relay, which can be used for bells or access control.
If you do not have an Odyssey, be sure to set Door Relay Number to 1 if
you are using access control. If you are using bells, be sure to set the
Bell Relay Number to 1. Only the Odyssey can be used for both bells and
access control.

Memory Alarm Threshold: Specify
the percentage of total memory that can be filled before the Memory Alarm
triggers.

Power Saving Mode Interval:
Specify the number of minutes the reader will stay in normal operation
before returning to power saving mode while backup battery power is in
use.

PIN Entry Allowed: Sets the
reader to allow ID entry only. This disables the use of badges.

Deactivate Speaker: Check this
option to deactivate the readerâs internal speaker. The reader will no
longer beep when keys are pressed.

Use Daylight Savings Time: Check
this box to automatically alter the time at the reader according to Daylight
Savings Time.

Synel Fingerprint Attached:
Check this box if the reader is equipped with a fingerprint unit.  This
option is only available on the Odyssey .

Using Pinless Finger Print: Check
this box if you want to use the pinless option of the terminal,  This
option will only work if your Odyssey terminal is equipped with a suprema
reader.  Once you have selected this option and the employees have
been enrolled the templates will not be useful if you decide not to use
the pinless functionality all employees must be re-enrolled.

Finger
Print Sensitivity:  You can set how sensitive you want the
fingerprint unit to be.  The lower the number the higher the sensitivity
it is.

Fingerprint
Reader Type:  There are two types of fingerprint readers the
Suprema and Bioscript readers.  Only the Suprema reader can be used
as pinless.

### Scout Options

![](/img/rb1.gif)

Reject Level: Controls clock
sensitivity when comparing electronic hand templates to actual hand measurements
taken when an employee attempts to punch. The lower the number the more
sensitive the reader is to changes in employee hand geometry.  Increase
this setting if your employees are having issues with hand verification

Hour Display: Choose a format
for the time displayed on the reader.

ID Length: Used to force a specific
ID length. This option will pad the ID received from the clock with zeros
until the specified number of digits is reached. For example, if an employeeâs
ID is 54 and the ID length is set to 4, the software will search for an
employee with 0054 assigned as their employee ID. If there is no employee
with 0054 as his or her employee ID the punch will be considered unassigned.
Generally this option can be left blank.

Idle Message: Enter the message
that will be displayed on the reader while the reader is in the idle state.

Keys Beep When Hit: Checking
this box will cause the reader to beep when a key is pressed.

Use Daylight Savings Time: Check
this box to automatically alter the time at the reader according to Daylight
Savings Time.

Maximum Template Security: Checking
this box greatly reduces the length of time required to update the Scout
Reader. Hand templates for employees assigned to the clock will be updated
to the  Scout Clock. Any other templates stored in the scout clock
will be removed.

_Note_:
Any employees with hand templates on the clock that are not setup within
the InfiniTime software
will not be able to punch in if this option is enabled. It is important
to ensure all employees have a record in the InfiniTime
Application before enabling this option. Otherwise the employee will have
to be enrolled again.

Auxiliary Output Configuration

Certain Scout models have auxiliary outputs available for various purposes.
Auxiliary outputs can be used to activate a buzzer, sign or any other
low voltage item.

_Note_:
The options below only apply to the Scout 3000 and 4000 Models.

On Tamper: An internal mercury
sensor detects excessive vibration or tampering with the clock housing.
Checking this option enables the auxiliary output and turns on an external
device, in this case most likely an alarm, when tampering is detected.

On Time Zone Violation:  Checking
this option enables the auxiliary output when internal RSI Time zone schedules
are violated. Refer to the section of this document that corresponds to
your specific reader type for more information about RSI Time Zone configuration.

On ID Refused: Checking this
option enables the corresponding auxiliary output when an employee enters
an ID that is not recognized by the system.

On Duress: Checking this option
enables the corresponding auxiliary output when an employee presses the
attached Duress Button. Refer to the section of this document that corresponds
to your specific reader type for more information about wiring a Duress
Button.

On Door: Checking this option
enables the corresponding auxiliary output when the attached Door Button
is pressed. Refer to the section of this document that corresponds to
your specific reader type for more information about wiring a Door Button.

On Try Again: Checking this
option enables the corresponding auxiliary output when the reader fails
to properly compare a hand to an electronic template.

On F1 Key: Checking this option
enables the corresponding auxiliary output when the F1 Key is pressed.

On F2 Key: Checking this option
enables the corresponding auxiliary output when the F2 Key is pressed.

On Power Failure: Checking this
option enables the corresponding auxiliary output in the event of power
failure. The clock must have a backup battery installed in order to use
this option. Without a backup battery the clock would simply lose power.

On Unlock: Checking this option
enables the corresponding auxiliary output when the attached door is unlocked.

Lock Relay Open Duration: Specify
the duration for the auxiliary output to remain enabled if she specified
conditions should be met.

### Function Key Configuration

Scout 2000, 3000, and 4000 models have programmable function keys on
the keypad the can be used for a broad range of purposes. Each function
key can be configured with multiple functions according to user preference.

_Note_:
All function keys are not available on each Scout Model. See the table
below for available function keys according to Scout Model.

| Reader Model            | Scout 1000 | Scout 2000 | Scout 3000 | Scout 4000 |
| ----------------------- | ---------- | ---------- | ---------- | ---------- |
| Available Function Keys | None       | F1 - F2    | F1 - F2    | F1 - F10   |

Unlike Synel Terminals, Scout Readers do not
have preset configuration settings such as Time & Attendance Only
or Access Control Only. Instead the Default action and function keys are
configured to perform specific actions. The Default action, as shown below,
is originally set to Time and Attendance and must be changed in order
to specify Access Control as the primary purpose of the reader.

_Note_:
Scout Readers cannot operate in Dual Time & Attendance and Access
Control mode.

![](/img/cset3.gif)

Available Function Key
Functions

Time & Attendance Punch:
Used to punch in or out of work. When this action is performed the current
time and date are recorded in the Scoutâs Memory. This information is
sent to the InfiniTime
software when the Scout is polled, where the information is entered into
the Timecard Activity Table.

Department Transfer: Used to
switch departments. When this action is performed employees can choose
which department they would like to transfer to. Employees will automatically
be clocked out of their current department and clocked into the selected
department at the current time and date. These activity entries will be
entered into the Timecard Activity Table when the Scout is next polled.

Other Activity Entry: Provides
the ability to enter other activity entries for a specific employee at
the clock.

Supervisor Override w/o Verification:
Only a supervisor can perform this action. If an employee attempts to
clock in to work outside of their defined schedule with lockout configured
they will be unable to clock in. This feature allows a supervisor to override
the last punch where a schedule lockout occurred. The employeeâs hand
is not required. The employeeâs punch will automatically be entered into
the Timecard Activity Table when the reader is next polled.

One Button Enrollment: Only
a supervisor can perform this action. Provides single button enrollment,
avoiding the need to use Technical Mode to access the Enrollment menu.
Supervisors must place their hand, enter the new employeeâs id and then
have the employee place their hand in order to create an electronic hand
template.

View Accrual Totals: Shows accrual
totals for the employee specified. Employees must enter their ID and hand
after selecting this option.

View Last Punch: Shows the last
punch for the employee specified.

View In/Out Board: Displays
the In and Out Board one employee at a time. Used to view employee status
at the clock.

Cancel View/Review: When viewing
the In and Out board or Reviewing an Employeeâs Timecard the only options
available are next or previous until the last line of the In and Out Board
or Timecard Report is reached. This function can be used to exit the In
and Out Board or Timecard Review immediately and return to the main screen.

Supervisor Override w/ Verification:
Only a supervisor can perform this action. If an employee attempts to
clock in to work outside of their defined schedule with lockout configured
they will be unable to clock in. This feature allows a supervisor to override
the last punch where a schedule lockout occurred. The employeeâs hand
is required. The employeeâs punch will automatically be entered into the

Timecard Activity Table when the reader is next polled.

View Hour Totals: Displays hourly
totals for the employee specified. An Hourly Totals type must be selected
on the General Tab of the Reader Address Configuration Form in order to
use this option.

Review Timecard: Shows the timecard
report line by line. The Cancel View/Review function can be used to exit
review mode. In order to use this option the Total Hours Type must be
configured in the General Tab of the Reader Address Configuration Tab.

Print Timecard: Prints the timecard
report for the specified employee on the attached printer. Only the Scout
3000 and Scout 4000 are compatible with this option.

Access Control: Used to access
an attached entryway. When this action is performed the current time and
date are recorded in the Scoutâs Memory. This information is sent to the
InfiniTime software when
the Scout is polled, where the information is entered into the Timecard
Activity Table.

### Function Key Setup

- Double click on the Function Key you wish to configure. The function
  key folder will open showing functions assigned to it.

![](/img/CH15_UnassignedPunches.gif)

- Click on one of the functions assigned to the Function Key.

![](/img/ch3term_5.gif)

- Use the Insert, Change, and Delete keys at the bottom of the screen
  to alter the assigned functions as desired. The order functions are
  displayed on the clock can also be adjusted with the Move Up or Move
  Down buttons.

![](/img/ph6.gif)

You can place an unlimited amount of options in one function key.   When
you have more than two functions assigned to a key they will appear in
sub directories of the key.  Take a look at the example below.

- Option 1
- More

When you Hit the 2 button

- Option 2
- More

This chain will continue depending on how many options you have chosen
for this function key.

### Zephyr / Luna Reader Settings

![](/img/i29.gif)

Terminal Mode: Specifies
the default operation on the terminal. The Zephyr, Juno, and Luna Terminals
supports only Time and Attendance.

Hour Display:
Select the desired time format for display at the clock. The terminal
can display time in a 12 or 24 hour format.

Date Format:
Select the desired date format for display at the clock.

Volume Percentage:
Specify the desired volume level for the terminal. Valid Values are 0
to 100.

Disable
Keypad Beep: If this box is checked
the keys on the terminal will no longer beep when pressed.

Lock Power Button: Disables
the power button. Users will not be able to turn the Zephyr Terminal off
using the power button.

Use
Daylight Savings Time: Enables daylight
savings time on the clock.

Disable Voice Prompt:
Turns off all voice messages at the clock.

Disable PIN Entry - If
this option is checked the password will be randomized when employee information
is sent to the clock. If an employee attempts to punch in or out using
the PIN Entry feature they will not be able to punch in or out as the
password is a randomly generated value. This essentially locks employees
out from using the PIN Entry feature. Employees will be required to punch
in and out using their fingerprint.

Do Not Require Password With PIN - If this option is checked the terminal
will not prompt employees for their password when using the PIN Entry
feature. Employees will still be able to punch in and out using their
fingerprint if desired.

Do
Not Allow Other Activity Entry: Disables other activity entry at
the clock.

Do Not Allow Department Switching:
Disables department switching at the clock.

Do Not Allow Job Switching - If
this option is checked Job information will not be sent to the Zephyr
Terminal. Employees will not be able to switch between jobs.

### Valid Telephone Numbers

![](/img/db1.gif)

In the Valid Telephone Numbers section of the Telephone Punch Update
form you can input telephone numbers that the employee can call from to
clock in or out using the InfiniTime
Telephone Punch. The Telephone punch system will use caller Id to see
if the employee is calling from a valid telephone number, if that number
is not in the list then the system will not allow the employee to clock
in or out.

To insert a valid telephone number click on insert and type in the telephone
number the employee can use to call in, you can input several telephone
numbers here.

![](/img/CH15_UnassignedPunches.gif)

Also you can set a schedule of when an employee can call in to punch,
if the employee tries to call outside of schedule the software will not
accept the transaction.  To set a default schedule for a particular
telephone number click on the default schedule tab.

![](/img/Ch11_Export2.gif)

In the Default Schedule Tab you can insert a schedule of when this valid
phone number is available to be used.  Click on the Quick Schedule
Button to create the schedule.

![](/img/i15.gif)

Start
Time - In this field you can enter the start time of when this
valid phone number is available to be used.

End Time

- In this field you can enter the end time of when this valid phone number
  is available to be used.

Valid
From - Is the date in which the schedule will start to be valid.

Valid
To - Is the date in which the schedule will end being valid.

_NOTE_:
The Valid From and Valid To fields are not required, if the fields are
blank then the schedule will always be valid.

Copy Button

- The copy button will copy the schedule from a particular weekday to
  other weekdays.

### Telephone Punch Settings

![](/img/CH3_CompInfo12.gif)

The Telephone Punch Settings allow you to set the telephone punch options:

- Do not
  Allow Department Switching: This option will allow you to disable
  the employee's ability to switch departments, which means that the
  transaction will post the employee's default department or the department
  specified for the Telephone Punch.
- Do Not
  Allow Other Activity Entry: This option will allow you to disable
  the employee's ability to enter other activity such as Sick Time,
  Vacation Time, Tips, etc. at the time of the call.
- Lockout
  Invalid Caller Id: This option will allow you to limit which
  calls will be accepted as valid, if an employee calls from an unauthorized
  phone number the software will tell the employee that they are calling
  from an invalid number and the transaction will not be accepted.  you
  will need to set valid telephone numbers from where an employee can
  call in, either at the employee level, department level or here in
  the reader configuration.
- User Id
  Only: This option will allow you to set the Telephone Punch
  to only ask for an Id to punch in or out, and not ask for a password.
- Menu Goes
  to Login After Punch: This option allows you to set the Telephone
  Punch to go back to the login prompt after an employee clock in or
  out.  This is useful if you have multiple employees calling from
  the same location that way they do not have to dial the number again
  after each transaction.

## History & Undo Tools

### History & Undo Tools Introduction

InfiniTime includes several
utilities, as summarized below, which can be used to add or alter Time
and Attendance Data for multiple employees at a time. Since the possibility
for accidental or improper use of these utilities exists, InfiniTime retains a log of all Purge,
Quick Punch, Quick Schedule, and Supervisor Review actions. In this way,
InfiniTime Administrators
can undo unintended alterations.

| Utility           | Purpose                                                                                         |
| ----------------- | ----------------------------------------------------------------------------------------------- |
| Purge             | Deletes all Timecard Activity for a specific Date Range for selected Employee(s).               |
| Quick Punch       | Inserts Punches for Selected Employees for all dates in the Specified Date range.               |
| Quick Schedule    | Creates Gannt Chart Schedules for Selected Employees for all dates in the specified Date Range. |
| Supervisor Review | Marks Employee Timecard Records in the specified Date Range as reviewed for Selected Employees. |

Details on how to access and utilize the History & Undo Tools for
each of the utilities above are provided below.

### Purge History Introduction

The InfiniTime Purge
History Tool maintains a running list of all purge actions that have been
performed since database creation. Using the Undo feature any action can
be undone. Should users make a mistake or remove information not intended
for removal data can easily be restored using the Purge History Tool.

Accessing Purge History

- Click on Tools
- Click on History And Undo Tools

![](/img/CH15_SysMon.gif)

- Click on Purge History.

![](/img/RLSNOTE_707-06.jpg)

View â Displays information
related to the purge action. The date range timecard activity was purged
from, employees the purge action was performed on, and the employee that
performed the purge action are all listed.

![](/img/ph8.gif)

Insert
â Click on Insert to purge employee activity. The action will be saved
in the Purge History Table.

![](/img/QST_SETUP_IMP_FILETYPE.gif)

Description â Enter a descriptive
name for the action you are performing. This description will be entered
into the Purge History table. Using detailed descriptions will help users
identify the record in the Purge History Table should the action need
to be undone in the future.

Date Range â All Timecard Activity
for specified employees that falls within this date range will be purged
from the software.

Filter â Use the Employee Filter
to select which employee(s) activity will be purged for.

Undo â InfiniTime
keeps a record of all Timecard Activity that was removed by a specific
purge action. Should the user decide that they want to restore that data
for any reason the Undo Feature can be utilized. All activity that was
originally removed by the purge action will be restored

Technical Note: The Undo Feature takes a snapshot
of current settings. Using the Undo Button simply instructs the software
to restore the settings that were saved in this snapshot. The snapshot
is taken before the changes specified by the purge action are applied.
For example, lets say all of the Timecard Activity before 1/1/2005 is
considered archivable and no longer required within the InfiniTime Application. A purge could
be executed from 1/1/2000 when the company in this example started using
the software to 1/1/2005. The Purge History Window saves a snapshot of
all activity within this date range. Should the undo feature be used all
activity within this date range will be restored. If any punches were
manually added to the system between the date range of 1/1/2000 to 1/1/2005
after the purge action they would remain unaltered.

Delete â Removes the highlighted
purge history record from the Purge History Table. Once a record is removed
from the Purge History Table its actions cannot be undone. Default security
role configuration permits purge record removal by the software administrator
or payroll clerks in order to prevent actions from being undone in the
future.

### Undoing a Previous Purge Action

- Determine which record in the Purge History table corresponds to
  the action that you wish to undo. Viewing the record to see the date
  range and employee who performed the original action can assist with
  this decision.
- You may wish to take a backup before to undo a purge action.
- Click on the record to highlight it.

![](/img/cset24.gif)

- Click Undo.

![](/img/Ch11_Export4.gif)

- Click Yes to confirm your decision.

![](/img/ClickServices.gif)

- Wait while the action is undone. All activity that was removed
  by the purge will be restored to the Timecard Activity Table.

![](/img/CH11_ImportFields_EmpShort.gif)

### Quick Punch History Introduction

The InfiniTime Quick
Punch History Tool maintains a running list of all quick punch actions
that have been performed since database creation. Using the Undo feature
any action can be undone. Should users make a mistake or add information
for the wrong employees the Quick Punch History Tool makes it easy to
remove incorrect Timecard Activity entries.

Accessing the Quick Punch History Tool:

- Click on Tools.
- Click on History And Undo Tools.

![](/img/maint1.gif)

- Click on Quick Punch History.

![](/img/CH11_ImportFields_GroupDesc.gif)

View
â Displays information related to the quick punch action. The date range
timecard activity was inserted, employees the activity was inserted for,
and the related punch pair times are all listed.

![](/img/ExpandServicesandApplications.gif)

Insert
â Click on Insert to insert a Quick Punch. The action will be saved in
the Quick Punch History Table.

Undo
â InfiniTime keeps a record
of all Timecard Activity that was inserted by a specific quick punch action.
Should the user decide that they want to remove that data for any reason
the Undo Feature can be utilized. All activity that was originally inserted
by the quick punch action will be removed.

Technical Note: The Undo Feature takes a snapshot
of current settings. Using the Undo Button simply instructs the software
to restore the settings that were saved in this snapshot. The snapshot
is taken before the changes specified by the quick punch action are applied.
For example, lets say Quick Punch was used to add activity from 8:00 AM
to 5:00 PM for all employees by accident. Should the undo feature be used
all activity added by the Quick Punch will be removed. If any punches
 added by the quick punch were manually edited after the quick punch
these changes will be lost. All activity records added by the quick punch
will be removed from the system.

Delete
â Removes the highlighted Quick Punch history record from the Quick Punch
History Table. Once a record is removed from the Quick Punch History Table
its actions cannot be undone. Default security role configuration permits
purge record removal by the software administrator or payroll clerks in
order to prevent actions from being undone in the future.

### Inserting a Quick Punch

![](/img/TP8.gif).gif)

Description
â Enter a descriptive name for the action you are performing. This description
will be entered into the Quick Punch History table. Using detailed descriptions
will help users identify the record in the Quick Punch History Table should
the action need to be undone in the future.

Date Range
â All Timecard Activity for specified employees that falls within this
date range will be purged from the software.

Punch Type - Use the drop down menu
to select the type of punch, choose from regular punch, schedule punch,
single punch, or other activity.

Regular
Punch - Inserts a set of punches. The first time specified is the
clock in time, while the second time specified is the clock out time.

Scheduled
Punch - Inserts punches according to the employees schedule. For
example if the employee is scheduled to work from 8:00 AM to 5:00 PM InfiniTime will automatically clock
the employee in at 8:00 AM and out at 5:00 PM.

Single Punch

- Inserts a single punch. InfiniTime
  automatically determines the punch type based upon the timecard activity
  already present on the date where the single punch is inserted.

Other Activity

- Inserts other activity such as holiday time, vacation time, sick time,
  and personal time.

Use Default
Department - if this is checked the punches will be posted using
the default department of the employee, if not checked you can choose
a department using the magnify glass or typing in the department name
to post those punches.

Use Default
Job - if this is checked the punches will be posted using the default
Job of the employee, if not checked you can choose a Job using the magnify
glass or typing in the Job name to post those punches.

Use Default
Task - if this is checked the punches will be posted using the
default Task of the employee, if not checked you can choose a Task using
the magnify glass or typing in the Task name to post those punches.

Start
Time â Enter the time that employees specified by the employee
filter started working.

End Time
â Displays the time that employees specified by the employee filter stopped
working. This field is automatically updated by the Duration and cannot
be edited directly.

Duration
â Enter the number of hours worked by employees specified by the employee
filter. The End Time will automatically be updated by this value. For
example, if the Start Time was set to 8:00 AM and 8 were entered into
the Duration, the End Time would automatically update to 4:00 PM.

Add Duplicate Punches

- Unless this box is checked InfiniTime will compare the punches
  being inserted to those already in the database when performing a Quick
  Punch. Any duplicate punches will be ignored. For example the image below
  shows an employee working from 7:30 AM to 5:00 PM on 1/17/2008. If a supervisor
  were to attempt to insert a punch on 1/17/2008 from 7:30 AM to 5:00 PM
  using quick punch then the punches would not be inserted unless Add Duplicate
  Punches was checked.

![](/img/i20.gif)

Weekday
Only â If this is checked it will only insert punches for weekdays
only and not the weekend, Saturday and Sunday.

Description
â Used for Auditing Purposes, any information typed into this box will
be saved to the Audit Trail for all inserted punches. This information
can then be viewed using the Audit feature at a later date.

Filter
â Use the Employee Filter to select which employee(s) activity will be
inserted for.

### Undoing a Previous Quick Punch Action

Determine which record in the Quick Punch History table corresponds
to the action that you wish to undo. Viewing the record to see information
about the Quick Punch can assist with this decision.

- Click on the record to highlight it.

![](/img/cset21.gif)

- Click Undo.

![](/img/maint4.gif)

- Click Yes to confirm your decision.

![](/img/ebut.gif).gif)

- Wait while the action is undone. All activity that was inserted
  by the Quick Punch will be removed from the Timecard Activity Table.

![](/img/Ch11_Export21.gif)

### Quick Schedule History Introduction

The InfiniTime Quick
Schedule History Tool maintains a running list of all schedules that have
been performed using the quick schedule function. Using the Undo feature
any action can be undone.

Accessing Quick Schedule History

- Click on Tools
- Click on History And Undo Tools

![](/img/tcard11.gif)

- Click on Quick Schedule History

![](/img/TP7.gif)

View â Displays information
related to the quick schedule action. The date range of the schedule added,
and the description of the schedule.

![](/img/JobImport.gif)

Insert â Click on Insert to
create a schedule. The action will be saved in the Quick Schedule History
Table.

![](/img/CH11Export_Email.gif)

Undo
â InfiniTime keeps a record
of all schedule records inserted by a specific quick punch action. Should
the user decide they want to remove that data for any reason the Undo
Feature can be utilized. All schedule records originally inserted by the
quick punch action will be removed.

Technical Note: The Undo Feature takes a snapshot
of current settings. Using the Undo Button simply instructs the software
to restore the settings that were saved in this snapshot. The snapshot
is taken before the changes specified by the Quick Schedule action are
applied. For example, lets say Quick Schedule was used to add a schedule
from 8:00 AM to 5:00 PM for all employees by accident. Should the undo
feature be used all schedule records added by the Quick Punch will be
removed. If any schedules added by the quick punch were manually edited
after the quick schedule these changes will be lost. All activity records
added by the quick punch will be removed from the system.

Delete
â Removes the highlighted Quick Punch history record from the Quick Punch
History Table. Once a record is removed from the Quick Punch History Table
its actions cannot be undone. Default security role configuration permits
purge record removal by the software administrator or payroll clerks in
order to prevent actions from being undone in the future.

### Supervisor Review History Introduction

The InfiniTime Supervisor
Review History Tool maintains a running list of all review actions that
have been performed since database creation. Using the Undo feature any
action can be undone. Should users make a mistake or accidentally review
activity for the wrong employees the Supervisor Review History Tool makes
it easy to revert Timecard Activity entries to their original un-reviewed
status.

Accessing the Supervisor Review History Tool:

- Click on Tools.
- Click on History And Undo Tools.

![](/img/TCPIP.gif)

- Click on Supervisor Review History.

![](/img/HousekeepingSvcStopped.gif).gif)

View
â Displays information related to the Timecard Activity Review action.
The date range timecard activity was reviewed, employees activity was
reviewed for, and the record description are all listed.

![](/img/Ch11_Export7.gif).gif)

Insert
â Click on Insert to review timecard activity. The action will be saved
in the Supervisor Review History Table.

Undo
â InfiniTime keeps a record
of all Timecard Activity that was marked as reviewed by a specific review
action. Should the user decide that they want to return that data to its
original un-reviewed state for any reason the Undo Feature can be utilized.

Insert â Click on Insert to insert
a Quick Punch. The action will be saved in the Quick Punch History Table.

Undo
âInfiniTime keeps a record
of all Timecard Activity that was inserted by a specific quick punch action.
Should the user decide that they want to remove that data for any reason
the Undo Feature can be utilized. All activity that was originally inserted
by the quick punch action will be removed.

Technical Note: The Undo Feature takes a snapshot
of current settings. Using the Undo Button simply instructs the software
to restore the settings that were saved in this snapshot. The snapshot
is taken before the changes specified by the review action are applied.
For example, lets say a supervisor accidentally reviewed activity for
all employees by neglecting to configure the employee filter. Should the
undo feature be used all review records added by the review action will
be removed.

Delete
â Removes the highlighted Supervisor Review history record from the Supervisor
Review History Table. Once a record is removed from the Supervisor Review
Table its actions cannot be undone. Default security role configuration
permits purge record removal by the software administrator or payroll
clerks in order to prevent actions from being undone in the future.

### Inserting a Supervisor Review

![](/img/Housekeeping03.gif).gif)

Description
â Enter a descriptive name for the action you are performing. This description
will be entered into the Supervisor Review History table. Using detailed
descriptions will help users identify the record in the Supervisor Review
History Table should the action need to be undone in the future.

Date Range
â All Timecard Activity for specified employees that falls within this
date range will be marked as reviewed.

Filter
â Use the Employee Filter to select which employee(s) activity will be
reviewed for.

### Undoing a previous Review Action

Determine which record in the Supervisor Review History table corresponds
to the action that you wish to undo. Viewing the record to see information
about the Review action can assist with this decision.

- Click on the record to highlight it.

![](/img/maint8.gif).gif)

- Click Undo.

![](/img/winbackuprestore3.gif).gif)

- Click Yes to confirm your decision.

![](/img/e4.gif).gif)

- Wait while the action is undone. All activity that was marked as
  reviewed by the review action will be returned to its original un-reviewed
  state.

![](/img/Barcode-settings.gif).gif)

## Clock Tools Introduction

### Polled Information

Polled Information keeps track of all employee activity that has been
received from external hardware readers and the InfiniTime
Employee Module. Polled Information cannot be emptied, as it provides
a data archive for the Employee Timecards. Should employees accidentally
remove all employee activity by incorrectly deleting records, employee
data can be reposted from Polled Information.

Accessing Polled Information:

- Click on Tools.
- Click on Clock Tools.

![](/img/Ch11_Export5.gif)

- Click on Polled Information.

![](/img/FilterButton-Normal.gif).gif)

Repost

Employee Timecard activity can be reposted to the Timecard Table in
the event of accidental activity deletion or if activity needs to be restored
to its original form for any reason.

Reposting Employee Timecard Activity:

- Click on Repost.

![](/img/cset9.gif).gif)

- Select the desired date range from which to repost Timecard Activity.
- Select the desired time range from which to repost Timecard Activity.
  The start time refers to a time on the first day of the date range
  and the end time refers to a time on the last day.

![](/img/SyncEE.png).gif)

- Timecard Activity can be reposted for a single employee or for
  all employees. If selected is chosen then a last name must be specified.

![](/img/Quick_Schedule_Table.gif).gif)

- Users that have multiple external readers can choose to repost
  activity from all readers or a single reader.
- Click OK to repost Timecard activity that falls inside of the range
  specified by the above options.

### System Monitor Window

System Monitor is designed to give InfiniTime
Administrators an overview of automated processes performed by the InfiniTime Application. The last automated
backup, Import, Export, Payroll Export, and Report process dates are shown.
In order to understand the information presented in the system monitor
window it is important to understand the nature of the InfiniTime Housekeeping Service. The
InfiniTime Housekeeping
Service is responsible for all automated tasks performed by the InfiniTime Application. In addition
the list of automated processes above this also includes polling.

The InfiniTime Housekeeping
service is a multi-threaded process that operates in a round robin manner
beginning with polling and related processes. InfiniTime
checks the last poll date and time of each clock sequentially according
to a unique system identification number. It compares the last poll date
and time to the current time and date to determine if it is time to update
or poll the clock again. This same procedure is also performed for the
Last Data Update Date and Time for each clock. Regular housekeeping routines
such as checking the database for exceptions or automated exports and
reports are performed separately from polling functions which allows the
InfiniTime Housekeeping
service to simultaneously poll time and attendance information while processing
automated tasks. As the cycle is completed for each automated task the
date and time to the right of each automated process will be updated as
it is completed.

Should the InfiniTime
Housekeeping Service encounter errors when attempting to communicate with
a clock the Last Poll time will be updated with the current time and the
service will move on to the next clock in the sequence. Additional attempts
at communication will occur every polling cycle. If a maximum number of
communication errors is specified the service will stop communication
with the clock if the specified number of errors occur.

It should be noted that the system monitor does not refresh automatically
to show updates for the status of clocks or automatic processes. In order
to view the latest details the refresh button must be used. The System
Monitor window has two refresh buttons, one within the grid where hardware
terminals are listed and the other at the bottom left of the form. The
refresh button within the hardware terminal grid only updates the information
within the grid, while the refresh button at the bottom left of the form
updates the entire system monitor window.

Accessing the System Monitor:

- Click on Tools.
- Click on Clock Tools.

![](/img/InLineEdit_4.jpg)

- Click on System Monitor.

![](/img/db4.gif)

![](/img/CH15_PolledInfo.gif)   Force Poll: Checks for punches
on the selected clock. If any punches are found the punch will be stored
in the InfiniTime database
and removed from the clock.

![](/img/winbackuprestore3.gif)  Update Reader: Forces the software
to clear the Last Data Update Date and Last Data Update Time fields. The
InfiniTime Housekeeping
Service will update the clock on its next pass through the reader processing
loop.

### The InfiniTime Housekeeping Service

InfiniTime includes multiple
automatic tasks such as sending reports to a printer or via email, creating
backup files, importing employee related information, exporting employee
related information, exporting payroll related information, and polling
clocks. These automated tasks are performed by the InfiniTime
Housekeeping Service in addition to other tasks such as tracking exceptions.
The InfiniTime Housekeeping
service must be running in order for these automatic processes to occur
as expected.

Starting and Stopping the InfiniTime Housekeeping Service

The InfiniTime Housekeeping
Service can be started and stopped using the computer management console.

To Start the InfiniTime
Housekeeping Service:

Right Click on My Computer and Click on Manage

![](/img/21DHOLAVG.jpg)

Click on the + to the left of Services and
Applications in order to expand the list.

![](/img/supervisor_review.gif)

Click on Services to view the list of services
installed on your machine.

![](/img/PollingDirect.jpg)

Locate InfiniTime
Housekeeping Service in the list.

![](/img/quick_punch.gif)

Right click on the InfiniTime
Housekeeping Service and click start.

![](/img/CH11_ImportFields_EMPID.gif)

To Stop the InfiniTime
Housekeeping Service:

Right Click on My Computer and Click on Manage

![](/img/PollFromFile.gif)

Click on the + to the left of Services and
Applications in order to expand the list.

![](/img/ph4.gif)

Click on Services to view the list of services
installed on your machine.

![](/img/TP9.gif)

Locate InfiniTime
Housekeeping Service in the list.

![](/img/i2.gif)

Right click on the InfiniTime
Housekeeping Service and click stop.

![](/img/OptionsWindow.gif)

Housekeeping Procedures and Logic

The InfiniTime Housekeeping
service operates in a round robin manner beginning with polling and related
processes. InfiniTime checks
the last poll date and time of each clock sequentially according to a
unique system identification number. It compares the last poll date and
time to the current time and date to determine if it is time to update
or poll the clock again. This same procedure is also performed for the
Last Data Update Date and Time for each clock. After checking the poll
and update timestamps of each clock and attempting to communicate with
each clock when necessary the InfiniTime
Housekeeping Services will perform regular housekeeping routines such
as checking the database for exceptions or automated exports and processes.
The date and time to the right of each automated process will be updated
as it is completed.

Should the InfiniTime
Housekeeping Service encounter errors when attempting to communicate with
a clock the Last Poll time will be updated with the current time and the
service will move on to the next clock in the sequence. Additional attempts
at communication will occur every polling cycle. If a maximum number of
communication errors is specified the service will stop communication
with the clock if the specified number of errors occur.

Poll and Update Procedure

The most prominent and logically complicated procedure performed by
the InfiniTime Housekeeping
Service is related to polling punches and activity from external devices
such as badge readers, fingerprint readers, and hand geometry readers.
This procedure is outlined below.

1.) Beginning with the first clock inserted into the system the Housekeeping
service compares the last poll time with the current time in order to
determine if the clock should be polled. If the polling interval specified
for the clock has elapsed the clock will be polled. Any time and attendance
punches, access control punches, or other activity entries stored on the
clock will be polled to the database and removed from the clock. Recommended
polling times can be found in the [TCP/IP
Clock Settings section of this document.](ovr_SoftwareAdministration.md#ru6_TCP_IP_Polling_Tab)

2.) Beginning with the first clock inserted into the system the Housekeeping
service compares the last update time with the current time in order to
determine if the clock should be updated. If the update interval specified
for the clock has elapsed the clock will be updated with all employee
information currently in the system. The employees sent to the clock are
subject to multiple conditions. Employees with alphanumeric characters
in the Login ID or Login Password fields will not be uploaded to a clock.
Additionally the employees sent to a clock are subject to the employee
filters as configured on the Reader Address Update form. It is important
to note that hand templates or fingerprint templates will be removed from
the clock for any employees that are not present in the InfiniTime Software Application as
appropriate during the update procedure.

Note: Hand templates are only removed from
Scout Terminals if the 'Maximum Template Security' Option is enabled.
Fingerprint templates will always be removed from fingerprint readers
such as the Thor for employees that have not been inserted in the InfiniTime Application.

3.) If an error should occur during a poll the last poll time will be
updated with the current time and the housekeeping service will proceed
to the next clock in the sequence.

4.) If an error should occur during an update the last poll time will
be updated with the current time and the housekeeping service will proceed
to the next clock in the sequence.

5.) If the poll and update processes complete without errors the InfiniTime Housekeeping Service continues
on to the next reader in the sequence and repeats the above processes.
When the last reader in the sequence has been processed the polling procedures
are complete and the InfiniTime
Housekeeping service will begin the polling procedures anew.

6.) If a clock is polled manually using the Force Poll Button on the
system monitor the InfiniTime
Housekeeping Service will automatically break from its normal sequence
to poll these clocks. This reduces the wait time for force polling clocks
on installations with multiple clocks.

Troubleshooting the InfiniTime Housekeeping Service

The InfiniTime
Housekeeping Service is responsible for communicating with all readers
and time keeping devices connected to the InfiniTime
Software Application. If you should notice your employees are able to
punch in and out on your time clock but the punches do not appear in the
InfiniTime Application
there could be several reasons why communication between the InfiniTime Application and your time
clock(s) is failing. A list of typical issues and resolutions are listed
below.

- Check the dates associated with each
  housekeeping task on the System Monitor. Are these dates and times
  relatively current? Depending on your software configuration these
  dates and times should be current within 5 minutes to 4 hours. If
  these times have not been updated in more than a day it is likely
  that normal operations of the InfiniTime
  Housekeeping Service have been suspended. Follow the procedure above
  to stop and restart the Housekeeping Service and check to see if the
  housekeeping processes resume. The status fields should be updated
  with current dates and times.

- If the status messages or dates associated
  with each housekeeping task on the System Monitor do not change after
  restarting the housekeeping there may be an issue with the file permissions
  required by the InfiniTime
  Housekeeping Service. The InfiniTime
  Housekeeping Service requires full control for the ASPNET user on
  the C:\Inception\InfiniTime\InfiniTime7\BIN
  directory by default.

### Unassigned Punches

Unassigned punches occur when an employee punches in on a timeclock,
such as the Schlage Scout 2000 or Thor, using an id or badge that is not
recognized by the software. Rather than ignoring the punch altogether
because it cannot immediately be assigned to an employee, InfiniTime records these punches in
the Unassigned Punches Table. Managers can then manually assign the punches
as needed.

Accessing Unassigned Punches

- Click on Tools
- Click on Clock Tools

![](/img/AutoExportSchedUpdate.png)

- Click on Unassigned Punches.

![](/img/TCPIP.gif).gif)

The upper grid shows the Badge Id or ID and password that has unassigned
punches. Clicking on this entry will populate the lower grid, showing
all unassigned punches for the selected ID.

Situational Examples that would result in
Unassigned Punches:

RSI Clocks:

Situation:
Company A runs a 24/7 manufacturing operation. Payroll and office workers
work until 5:00 PM while factory shifts work around the clock. Payroll
employees install InfiniTime
and setup the clocks during their work day, they are unable to complete
employee setup for all employees before they leave for the day. A factory
shift begins at 6:00 PM, the shift supervisor enrolls his employees in
the Hand Punch and instructs them on its use. Employees begin punching
and the Timecard Activity is stored in the Hand Reader. The next morning
payroll polls Timecard Activity from the reader and all of the punches
come across as unassigned because the employees have yet to be setup in
the software.

Resolution:
The employee responsible for managing the InfiniTime
software will insert all of the employees into the software, making sure
that the ID used by each employee the night before is assigned to them.
It may be necessary to check with the Shift Supervisor or even the employees
themselves regarding what ID they were enrolled with. The unassigned punches
table may then be used to assign the punches accordingly.

Synel Clocks:

Situation:
Should validate employee be disabled, see Synel Clock Configuration for
more information, any badge of the appropriate coding and length will
read when swiped through the Synel Card Reader. Should the badge number
encoded into the card not be associated with an employee then the punch
will be considered unassigned. This will occur if employees forget their
badge and simply use a spare for the day.

Resolution:
The punches can simply be assigned to the employee using the unassigned
punches table to rectify the issue.

Zephyr Clocks:

Situation:
If an employee is enrolled at the Zephyr Terminal using the User Manage

- Add User option and is not present within the InfiniTime
  software any punches made with the badge assigned to this employee will
  come into the InfiniTime
  Software as unassigned. It is important to ensure employee information
  is configured within the InfiniTime
  Software and sent to the Zepyhr Terminal rather than entering employees
  at the clock itself.

Resolution:
Ensure all employees have been added to the InfiniTime
Database in the employee table. Assign a badge to the employee and enter
the badge number on the Login Tab of the Employee's Record. Update the
Zepyhr Clock. This will prevent unassigned punches from occurring in the
future. Be sure to assign the punches that have already been polled into
the InfiniTime database
to the employee(s) after they have been added to the system.

Situation:
If an employee's badge is changed within the InfiniTime
Software the employee will be able to punch in and out with the old badge
until the Zepyhr Clock has been updated. If they punch using their old
badge, which is no longer in the InfiniTime
Software, the punches will be considered unassigned.

Resolution:
After changing important information such as employee Badge Numbers, Login
IDs, Passwords, or Employee IDs be sure to update your clocks. This will
send the information to the clock preventing employees from swiping with
their old badge or punching using their old employee id. Ensure any punches
that have already been polled into the database as unassigned punches
are assigned to the correct employee(s).

Luna Clocks:

Situation:
If an employee's Login ID is changed within the InfiniTime
Software the employee will be able to punch in and out with the old badge
until the Luna Clock has been updated. If they punch using their old badge,
which is no longer in the InfiniTime
Software, the punches will be considered unassigned.

Resolution:
After changing important information such as employee Badge Numbers, Login
IDs, Passwords, or Employee IDs be sure to update your clocks. This will
send the information to the clock preventing employees from swiping with
their old badge or punching using their old employee id. Ensure any punches
that have already been polled into the database as unassigned punches
are assigned to the correct employee(s).

### Import Introduction

The Import and Export Data selections greatly extend the functionality
of InfiniTime. These functions
allow you to import and export data collected with InfiniTime
or compatible third-party applications such as Microsoft Excel.  InfiniTime imports and exports ASCII
comma separated and quotation delimited text. Additionally, data can be
exported as a dBASE file (DBF) readable by dBASE spreadsheet software.
For instructions on how to prepare and import data from a comma delimited
file refer to the section of this document entitled Performing an Import.

_Warning!_
Be sure to backup InfiniTime
prior to importing data so that you will have a copy of original data,
in case there is a problem with the imported data.

Accessing the InfiniTime
Import Table:

- Click on Tools.
- Click on Import and Export.
- Click on Import.

![](/img/PollingTCPIP.jpg)

The Import Definition Table will be displayed as shown below.

![](/img/i11.gif)

Import Button  ![](/img/maint4.gif)

- The import button allows you to highlight an already saved import
  structure and import it.

Insert Button ![](/img/ph5.gif)

- The insert button will allow you to create a new import structure.
   When selecting this button, the Import File Selection Table will
  appear.

Delete Button  ![](/img/PollingTCPIP.jpg)
 -  This button will delete a highlighted import structure.

### Target Fields Available to be imported

All fields within the InfiniTime
Database that can be imported are listed within the following tables.
It is important to keep in mind the nature of software and databases when
attempting to perform an import. The tables in this section are comprised
of six columns, Field Name, Description, Field Format,  Field type,
 Required, and Valid Values. Each of these columns contain pertinent
information for individuals preparing a CSV
file for import into InfiniTime.
An outline of each column, its contents, and how this information relates
to the expected format of the CSV file for import
is provided below.

Field Name -
The name of the field as displayed within the Target Field grid of the
Import Update form.

Description  -
A general description of the contents of the field.

Field Format  -
Provides a 'picture' of the data format. This column will contain one
of three value types, a whole number, a decimal number, and an example
detailing the format of the data. Examples of each value type that may
be found in this field is provided below.

- Whole Numbers - A whole number represents
  the number of characters or digits that can be stored within the respective
  field.
- Decimal Numbers - A decimal number represents
  the number of digits before and after a decimal point that can be
  stored within the respective field. IE: 5.2 stands for Five Characters
  or Digits before the decimal place and two after: 12345.12
- Data Format - Symbols and letters are often
  used as place holders for specific information. An example of a data
  format would be MM/DD/YYYY which indicates
  a ten character field where the first two digits represent the month,
  the third and fourth digits represent the day, and the last four digits
  represent the year. A forward slash (/) is also shown between each
  set of digits and is expected in the data to be imported.

Example Dates using an MM/DD/YYYY Format
are provided below. Note how a single digit month is preceded by a 0 in
order to fill both month characters in the MM/DD/YYYY format.

1.)
10/31/1986

2.)
 08/01/1987

Field Type -
Indicates the type of information the field can hold. Common field types
are below. Only the characters indicated are supported by the InfiniTime
Application. Use of special characters and punctuation should be avoided.

- Numeric - Numeric
  fields can only hold numbers
  (0 to 9) and cannot contain leading zeroes.
- Alphanumeric
  - Alphanumeric fields can only
    hold letters (A to Z), numbers (0 to 9) and
    spaces.
- Character -
  Character fields can contain only
  one letter (A to Z) or number (0 to 9).

WARNING:
While every attempt is made to remove characters incompatible with the
chosen field type by the Import Processes care should be taken to ensure
special characters and punctuation are not present in the import file.
The database cannot store special characters or punctuation as employee
information is sent to hardware terminals supported by InfiniTime. These hardware terminals
have special database requirements which do not provide support for punctuation
or special characters.

Required  -
Indicates if a field is required. Required fields must have a column from
the import file mapped to them in order for records to be successfully
imported. A value of 'Y' in this column indicates
a field is required. A value of 'N' in this column
indicates a field is not required. A value of 'P' indicates the field
is not required in order to successfully import records however you will
be prompted to enter the information manually when editing the record
for the first time. For example if employee supervisors are not imported
when importing employees then the software will prompt the user to enter
the employee's supervisor when attempting to edit the employee record.

Valid Values -
Some fields such as spin boxes give
users the ability to select a value from a predetermined list of items.
Only the predetermined values may be imported into these fields. Valid
values have been listed for fields that are restricted to a predetermined
list of items. Be sure to verify the proper case of the information that
is to be imported. For example the Type field within Timecard Files has
two predetermined values, Clock In and Clock Out. 'clock out' is not the
same as 'Clock Out' and will not be recognized by the import.

Link to Table - Many fields
available for import link to a separate table within the InfiniTime Database. When mapping
values to these fields remember the data must exist in the destination
table. For example it is not possible to assign existing employees to
the 'Florida Employees' group using the Employee Group File if the 'Florida
Employees' group does not exist. This example applies to the 'Link to
Group Description Table' field.

Employee File - Creates Employee Records

![](/img/tcard09.gif)

Department File - Creates Department Records

![](/img/Import_Auto_1.gif)

Employee Accrual Totals File - Updates Existing
Employee Accrual Total Records

![](/img/CH15_SysMon.gif)

Importing Employee Accrual
Base Amounts

In order to import employee
Accrual Base Amounts, the following conditions must be met:

- Employees must be assigned to an Accrual
  Type and must have Employee Accrual Total Records. The simplest way
  to verify all employees have Employee Accrual Total Records after
  assigning employees to a new accrual type is to perform a Company
  Recalculate for the Current Pay Period.
- All Required Fields, as indicated in the
  Table Above, must be present in the import file and mapped when creating
  the Import Definition.
- The Accrual Period Start and End Dates
  within the Import File must match the Start and End Dates for each
  individual employee's existing Employee Accrual Total Records.
- Replace Existing Record without Prompt
  must be selected on the Duplicate Checking Tab.

Other Activity Type File - Creates Other
Activity types

![](/img/e5.gif)

Groups Level File - Creates Group Levels

![](/img/Purge.gif)

Groups Description File - Creates Groups

![](/img/Ch11_Export17.gif)

Employee Groups File - Assigns Existing Groups
to Existing Employees

![](/img/i3.gif)

Importing Employee Group
Assignments

In order to import Employee
Group Assignments, the following conditions must be met:

- An employee must exist with the Employee
  ID / Employee Login ID specified in the Link to Employee Table Field
  for each imported record. If a specified Employee ID / Employee Login
  ID does not exist the record will be skipped.
- A Group Description must exist as specified
  in the Link to Group Description Table for each imported record. If
  a specified Group Description does not exist the record will be skipped.
- A Group Level must exist as specified in
  the Link to Group Level Table for each import record. If a specified
  Group Level does not exist the record will be skipped.
- Replace Existing Record without prompt
  must be selected on the Duplicate Checking Tab.

Employee
Shifts File - Assigns Existing Shifts to an existing Employee

![](/img/e4.gif)

Note: Employees
can only be assigned to a shift which is configured to be Used for Scheduling.
If the shift specified for an import record does not have the Used For
Scheduling option enabled, the record will be skipped.

Note: Shifts
do not have to exist in the software in order to perform the import however
schedules cannot be imported and must be configured manually for each
shift created by the import process. For this reason, most customers choose
to create shifts and define the schedule for each shift before importing
employee shift assignments. Shifts created during the import process will
have the Used for Scheduling option enabled automatically.

Employee Timecard file - Creates Employee
Timecard Punches

![](/img/maint12.gif)

Note: When Importing
Employee Timecards it is important to ensure duplicate records present
in the import file will be ignored. To ensure duplicate punches, or punches
for a specific employee with the same Time and Date, are not imported
Date and Time must be tagged on the Duplicate Checking Tab as outlined
below.

1. Click on the Duplicate Checking tab after
   selecting a source file.

2. Type Date in the search box and click
   on the Search Button.

3. Click Tag.

4. Type Time in the search box and click
   on the Search Button.

5. Click Tag.

6. Ensure 'Ingore It' is selected for 'If
   Duplicates are found:'

7. Continue configuring the Import.

Activity
Job Information File - Creates Activity Jobs

![](/img/Ch11_Export19.gif)

Activity
Task Information File - Creates Activity Tasks

![](/img/Import_Auto_2.gif)

Employee Badges File - Creates Employee Alternate
Badges

![](/img/CH15_Sysmon1.gif)

Employee
Schedules File - Creates Employee Schedule Gannt Chart Entries

![](/img/cset13.gif)

**Importing
Employee Schedules**

The
Employee Schedules File import type makes it possible to import GANNT
Chart Schedules for employees. As indicated by the table above the Link
to Employee Table, Link to Department Table, Schedule Date, Schedule Begin
Time, and Schedule End Time Fields must be filled in order for a schedule
record to be created by the import. The Employee Schedules File Import
Type supports Working, Paid Break, and Unpaid Break schedules by setting
the Schedule Type to the appropriate value. If the Schedule Type is left
blank or is not mapped, then the Schedule Type defaults to working. Example
records, with map by name headers, are provided below to illustrate the
format for each schedule type.

Importing
Schedule Records

The example records below will
result in the following schedules:

Employee
1

9:00 AM 1:00 PM Working                   Department
2, Job 1, Task 1

1:00
PM 2:00 PM Paid Break               Department
2, Job 1, Task 1

2:00
PM 6:00 PM Working                   Department
1, Job 2, Task 2

Employee
2

12:00 PM 2:00 PM Working                 Department
1, Job 1, Task 1

2:00
PM 3:00 PM Unpaid Break           Department
1, Job 1, Task 1

3:00
PM 8:00 PM Working                   Department
1, Job 1, Task 1

| Link to Employee Table | Link To Department Table | Schedule Date | Schedule Begin Time | Schedule End Time | Schedule Type | Link to Other Activity Type Table | Link To Activity Job Table | Link To Activity Task Table |
| ---------------------- | ------------------------ | ------------- | ------------------- | ----------------- | ------------- | --------------------------------- | -------------------------- | --------------------------- |
| 1                      | 2                        | 04/1/2010     | 09:00 AM            | 01:00 PM          | Working       |                                   | Job 1                      | Task 1                      |
| 1                      | 2                        | 04/1/2010     | 01:00 PM            | 02:00 PM          | Paid Break    |                                   | Job 1                      | Task 1                      |
| 1                      | 1                        | 04/1/2010     | 02:00 PM            | 06:00 PM          | Working       |                                   | Job 2                      | Task 2                      |
| 2                      | 1                        | 04/1/2010     | 12:00 PM            | 02:00 PM          | Working       |                                   | Job 1                      | Task 1                      |
| 2                      | 1                        | 04/1/2010     | 02:00 PM            | 03:00 PM          | Unpaid Break  |                                   |                            |                             |
| 2                      | 1                        | 04/1/2010     | 03:00 PM            | 08:00 PM          | Working       |                                   | Job 1                      | Task 1                      |

Importing
Other Activity Schedules (IE: Vacation Time)

The example record below will
create a Vacation Schedule Record from 12:00 PM to 8:00 PM on 4/2/10 in
Department 1, Job 1, Task 1 for Employee 2. Note that the Schedule Type
field is null. It is not necessary to fill the Schedule Type field when
scheduling Other Activity.

| Link to Employee Table | Link To Department Table | Schedule Date | Schedule Begin Time | Schedule End Time | Schedule Type | Link to Other Activity Type Table | Link To Activity Job Table | Link To Activity Task Table |
| ---------------------- | ------------------------ | ------------- | ------------------- | ----------------- | ------------- | --------------------------------- | -------------------------- | --------------------------- |
| 2                      | 1                        | 04/2/2010     | 12:00 PM            | 08:00 PM          | Vacation Time |                                   | Job 1                      | Task 1                      |

**Schedule
Override For Imported Schedules**

It
should be noted that InfiniTime does not permit overlapping records on
the Schedule Gannt Chart. Existing Gannt Chart Records including Working,
Paid Break, Unpaid Break, Other Activity, and Scheduled Days Off on the
Schedule Date for the specified employee will be deleted when schedule
records are imported. Imported Schedules should be complete as they override
any schedule currently defined for the given Schedule Date. Users should
take care to ensure schedule records in the import file for a given schedule
date do not overlap.

For example:

Proper Schedule Records Not
Overlapping

| Link to Employee Table | Link To Department Table | Schedule Date | Schedule Begin Time | Schedule End Time | Schedule Type | Link to Other Activity Type Table | Link To Activity Job Table | Link To Activity Task Table |
| ---------------------- | ------------------------ | ------------- | ------------------- | ----------------- | ------------- | --------------------------------- | -------------------------- | --------------------------- |
| 1                      | 2                        | 04/1/2010     | 09:00 AM            | 01:00 PM          | Working       |                                   | Job 1                      | Task 1                      |
| 1                      | 2                        | 04/1/2010     | 01:00 PM            | 02:00 PM          | Paid Break    |                                   | Job 1                      | Task 1                      |
| 1                      | 1                        | 04/1/2010     | 02:00 PM            | 06:00 PM          | Working       |                                   | Job 2                      | Task 2                      |

Each record is back to back
with a Working Period, a Break Period, and a second working period. None
of the schedule records overlap.

Improper Schedule Records -
Overlapping

| Link to Employee Table | Link To Department Table | Schedule Date | Schedule Begin Time | Schedule End Time | Schedule Type | Link to Other Activity Type Table | Link To Activity Job Table | Link To Activity Task Table |
| ---------------------- | ------------------------ | ------------- | ------------------- | ----------------- | ------------- | --------------------------------- | -------------------------- | --------------------------- |
| 1                      | 2                        | 04/1/2010     | 09:00 AM            | 06:00 PM          | Working       |                                   | Job 1                      | Task 1                      |
| 1                      | 1                        | 04/1/2010     | 08:00 AM            | 05:00 PM          | Working       |                                   | Job 2                      | Task 2                      |

The schedule records above are
for the same day for working periods that overlap. Users should ensure
imported schedules do not overlap as shown above.

Importing
Overnight Schedules using the Employee Schedules File Import Type

The Employee Schedules File
Import Type provides support for importing schedules that cross midnight.
It is not necessary to split schedules at midnight in order to import
overnight schedules, the schedule must be split at midnight. An example
record for an employee starting at 8:00 PM on 4/1 and working until 4:00
AM on 4/2 is displayed below.

For example:

Overnight Schedule Record that
Crosses Midnight

| Link to Employee Table | Link To Department Table | Schedule Date | Schedule Begin Time | Schedule End Time | Schedule Type | Link to Other Activity Type Table | Link To Activity Job Table | Link To Activity Task Table |
| ---------------------- | ------------------------ | ------------- | ------------------- | ----------------- | ------------- | --------------------------------- | -------------------------- | --------------------------- |
| 1                      | 2                        | 04/1/2010     | 08:00 PM            | 04:00 AM          | Working       |                                   | Job 1                      | Task 1                      |

### Import File Creation and Editing

A Brief Warning: Editing Comma Delimited
 (.CSV) Files

There are several applications available for editing comma delimited
files such as those used for importing and exporting in InfiniTime. Microsoft Excel is available
to most users and is commonly used to edit comma delimited files. Many
users do not realize the ramifications of using Excel for editing comma
delimited files. Excel does not display the exact contents of a field
in a .CSV file for editing. Excel attempts to identify the format of the
field though in some cases the data is altered during this process. When
a .CSV file is opened in Excel leading zeroes are stripped from fields
and Date - Time Stamps are automatically formatted to show only the Time
Stamp. These automatic alterations can cause undesired changes to a file
if the user does not take steps to return the data to its original format.

Due to these inherent issues with editing comma
delimited files in Excel it is recommended to use other applications such
as Notepad or Wordpad for editing .CSV files.  Should you decide
to use Excel be sure to pay extra attention to the formatting of fields
containing Numeric or Date information.

Creating your Import File:
A Typical Procedure to Prepare Data for Import.

In today's electronic world most companies
have their employee data available in an electronic format in one form
or another. The information may be saved in an excel spreadsheet, stored
in a SQL or Access Database, or kept in a payroll application. Employee
data from other applications can often be exported in a comma delimited
format which in turn can be imported into the InfiniTime
Software. When importing information from a third party application there
are a few key items, as listed below, which require attention.

- What information is to be imported?
- Data Format
- Valid Values
- Column Headers

Importing Employee Information:
What information is required and what optional information should I import?

While it is important to know what information
can and cannot be imported into the InfiniTime
software it is also important to recognize what information should be
imported based upon the features you are currently using within the InfiniTime software. For example if
Security Filters and Groups have been implemented in order to allow supervisors
to see only employees within their group it is important to ensure each
employee has the appropriate group assigned the them. In this case you
would want to make sure the information required to import groups is included
in each employee record. A list of  commonly used optional features
and the information used by each is listed below.

Filtering
by Groups - Supervisor access is often restricted by providing
access only to the individuals a supervisor is responsible for. This is
accomplished by configuring the Supervisor's Security Filters and assigning
specific groups to the supervisor. Employees must be assigned to the proper
group in order for supervisor's to access their record.

Employee
Messaging - By default Employee's only have the ability to send
a message to their supervisor. If supervisor's are not configured properly
the message will not reach the intended recipient.

Escort Windows

- Escort Windows allow users to access custom designed portals to the
  InfiniTime software. An
  Escort must be assigned to an employee in order for them to access the
  Escort Module.

Access Control -
Access Control Groups are used to designate which users have access to
an entryway and at what times they are permitted to enter and exit. Access
Control Groups must be assigned to an employee in order for them to use
the Access Control Systems.

Holidays

- Holiday Schedule Types are configured according to a company's policy
  for paid Holiday time. A holiday type must be assigned to employees in
  order for them to automatically receive paid holiday time.

Accruals -
Accrual types are configured according to a company's policy for Vacation
and Sick Time. An accrual type must be assigned to employees in order
for them to accrue sick time or vacation time automatically.

Security
Role - Security Roles govern access to the InfiniTime
Application. If security roles are not specified in an import file all
employees will default to the Employee Role.

Note: Some
information such as Default Schedules and Security Filter Settings cannot
be imported. It is important to ensure this information is configured
appropriately after the import has been performed.

Note: Many
of the above settings can be assigned to employees using Quick Assign.
In some cases it may be easier to use quick assign to configure the settings
appropriately after new employees have been imported into the software
rather than configuring the import file. Some items such as Escort, Holiday
Settings, and Accrual Types also have a default setting. The default setting
will be automatically assigned to new employee records created with the
Import Feature.

Preparing a Comma Delimited
File for Import: Ensuring proper data format.

If employee data is not formatted correctly
the record will not be imported. To ensure correct data format refer to
the tables listed under the topic 'Target Fields Available For Import'
A section of the Employee Information table is displayed below showing
some of the fields that can be imported along with compatible format information.
Each column of an import file and the data contained therein should be
compared to this list in order to ensure proper data format before performing
an import.

![](/img/maint12.gif)

Data Type

- The data type is described by the Field Type Column. This column indicates
  the type of information the field can hold. Common field types are below.
  Only the characters indicated are supported by the InfiniTime
  Application. Use of special characters and punctuation should be avoided.

* Numeric - Numeric
  fields can only hold numbers (0 to 9) and cannot contain leading zeroes.
* Alphanumeric
  - Alphanumeric fields can hold letters (A to Z),
    numbers (0 to 9) and spaces.
* Character -
  Character fields can contain only one letter (A to Z)
  or number (0 to 9).

As shown above the Employee
ID is an alphanumeric value. A combination of letters and numbers can
be stored in the Employee ID up to a maximum of 50 Characters.

A
note on importing numeric values: When importing numeric values
into an Alphanumeric field the numeric value should be enclosed in quotes
within the Comma Delimited File. This ensures the value will not be treated
as a date or a number upon import.

Data Length
and Format - The length and format are described by the Field Format
Column. This column will contain one of three value types, a whole number,
a decimal number, and an example detailing the format of the data. Examples
of each value type that may be found in this field are provided below.

- Whole Numbers
  - A whole number represents the number of characters or digits that
    can be stored within the respective field.
- Decimal Numbers - A decimal number
  represents the number of digits before and after a decimal point that
  can be stored within the respective field.
- Data Format - Symbols and letters
  are often used as place holders for specific information. An example
  of a data format would be MM/DD/YYYY which
  indicates a ten character field where the first two digits represent
  the month, the third and fourth digits represent the day, and the
  last four digits represent the year. A forward slash (/) is also shown
  between each set of digits and is expected in the data to be imported.

As shown above the Employee Middle Initial
is an alphanumeric field and can hold one character. If you decide to
import the middle initial ensure only one character is present in the
Middle Initial Column. The middle initial field is intended only for a
single character and cannot store a middle name or punctuation.

Required

- Indicates if a field is required. Required fields must have a
  column from the import file mapped to them in order for records to be
  successfully imported, even if you are only updating employee information.
  A value of 'Y' in this column indicates a field
  is required. A value of 'N' in this column indicates
  a field is not required. A value of 'P' indicates the field is not required
  in order to successfully import records however you will be prompted to
  enter the information manually when editing the record for the first time.
  For example if an employee supervisors are not imported when importing
  employees then the software will prompt the user to enter the employee's
  supervisor when attempting to edit the employee record.

Required fields must be present in the import
file and mapped to the appropriate field. Required fields for importing
employees are listed below:

- Employee Badge ID
- Employee Clock ID
- Employee Clock Password
- Employee First Name
- Employee ID
- Employee Last Name
- Employee Login ID
- Employee Login Password
- Link to Department Table

NOTE: As detailed above required fields must be
present within the import file in order for the import to complete successfully.
Even if you simply wish to update employee personal information such as
Addresses and Emergency Contact information the required fields listed
above must be present in the import file. These values are compared with
multiple tables in the InfiniTime
Application to ensure the appropriate record is being updated and no duplicates
exist. If this information is not provided properly a blank employee record
will generally be created. Blank records do not have a first or last name
and should be deleted.

Valid Values

- Some fields such as spin boxes give users the ability to select a value
  from a predetermined list of items. Only the predetermined values may
  be imported into these fields. Valid values have been listed for fields
  that are restricted to a predetermined list of items. Be sure to verify
  the proper case of the information that is to be imported. For example
  the Type field within Timecard Files has two predetermined values, Clock
  In and Clock Out. clock out is not the same as Clock Out and will not
  be recognized by the import.

As shown in the table above the Employee
Pay Method has five valid values. These values are Hourly, Other, Pay
On Hold, Per Diem, and Salary. Only these values can be imported into
InfiniTime. Keep in mind
these values are case sensitive.

Override

- If desired the Override option can be used in leu if editing the import
  file. For example if your payroll system exports M or S for married and
  single these values can be imported directly using the override feature
  by configuring a conditional override. A conditional override searches
  for a specific term and imports another value when the term is matched.
  IE: IF Marriage Status = M then Import Married. Refer to [Import
  Configuration: Override](ovr_SoftwareAdministration.md#imp11_context_Override) for more information on the override feature.

Import File Headers and
Mapping Destination Fields - Map By Name

While some applications
may not include a header record when exporting a comma delimited file
it is often best to ensure a header record exists and includes the correct
information. If column headers are set to the same name as the field within
InfiniTime the Map By Name
button can be used to simplify the mapping process. To identify the appropriate
header to use for each column of your import file follow the procedure
below:

1.)
Identify which field the information you are importing corresponds to.
For example employees are generally assigned a unique identifier. This
identifier may include letters and numbers. By looking at the table of
Employee Information Fields that can be imported you can quickly identify
the item below as the correct field.

![](/img/AutoExportSchedUpdate.png)

2.)
The Field Name, or Employee ID in this case, should be used as the header
for the import file.

### Performing an Import

The Import File Selection Table allows you to select what type of information
will be imported to the InfiniTime
program.  In general the tasks below must be performed before a file
can be imported. It is important to read the reference documents linked
below prior to attempting to design an import file for use with InfiniTime. This will help you understand
how to prepare a file for import into the InfiniTime
Application.

1.) Prepare a comma delimited (.csv) file with the information you would
like to Import into InfiniTime.
 Remember, all required fields must be present in the import file

- even if you are only updating employee records. IE: To update employee
  personal information for multiple employees at once the import file must
  contain the fields you wish to update (Address Line One, Address Line
  Two, Emergency Contact Name etc.) in addition to all required fields such
  as Employee ID, Employee First Name, Employee Last Name etc. Refer to
  Import File Creation and Editing for more information on designing an
  import file.

  2.) Ensure all information in the import file is compatible with database
  constraints. In general Alphanumeric fields should only contain A to Z,
  spaces,  and 0 to 9 while numeric fields should only contain 0 to

9. A list of fields that can be imported into InfiniTime
   along with the type of data they can store is available for your reference.

3.) Create an Import Criteria to be used with the prepared import file.
Be sure to specify the appropriate file type and check the option to skip
the first record if your import file contains a header row.

4.) Map the fields within the file to fields within the InfiniTime Database. Be sure to perform
any overrides as necessary.

5.) Save the import criteria and take a backup of the InfiniTime Database prior to performing
the import. This ensures it will be possible to revert to the state of
the database prior to the import if needed.

6.) Perform the import.

Selecting an Import File Type

![](/img/TP9.gif)

- Department
  File - Imports the fields necessary for the program to create
  departments.
- Employee
  Groups File - Assigns groups existing within the InfiniTime Database to employees.
- Employee
  File - Imports Employee information into the program, this
  includes most HR information in InfiniTime.
- Employee
  Accrual Totals File - Imports past amounts of accruals earned
  by the employee.
- Employee
  Group Level File â Imports Group Levels, creating them within
  the database. Group Levels create folders within the Group Table.
  Locations is an example of a group level where the groups under it,
  Phoenix, Pittsburgh, Philadelphia, would be Group Descriptions.
- Employee
  Group Description File - Imports Group Descriptions, creating
  them within the database.
- Other
  Activity Type File  - Imports the fields necessary for
  the program to create Other Activity Types, Other Activity Types are
  tips, vacation, sick time, Etc
- Employee
  Shifts - Assigns shifts existing within the InfiniTime Database to individual
  employees.
- Employee
  Timecard File - Imports Employee
  Timecard Punches.
- Activity
  Job Information File - Imports Activity Jobs. Each record in
  the import file will be used to add a job to the InfiniTime
  database. Useful for manufacturing companies with 100+ jobs.
- Activity
  Task Information File - Imports Activity Tasks. Each record
  in the import file will be used to add a job to the InfiniTime database. Useful for manufacturing
  companies with 100+ tasks.

Source File Options

The source file options tab is used to specify
details about the file to be imported. Information about the format of
the file and the location of the file are needed.

![](/img/cb3.gif)

Import Structure
Description - Enter a description for the import you are about
to create.  This name will appear on the initial window for easy
importing.

![](/img/i30.gif)

Comma-Separated
File To Import - Click on the magnify glass and select the file
you wish to import. It is important to note that changing the selected
file after Mapped Fields have been defined will clear the field mappings.

TIP: If
you need to update records in an import file for a previously created
an Import with mapped fields, but do not wish to reconfigure the mapped
fields, the Comma Delimited File can be copied directly to the Input Directory
in the InfiniTime Program
File Location on the InfiniTime
Server. This should only be performed if the order of fields and field
headings have not changed from the original comma delimited file selected
in the Import and the new file. Additionally, the name of the original
and new comma delimited files must match.

Maximum
Records to Import - This field will allow you to specify how many
records should be imported.  To import all records in the file leave
this field at â0â

Field Separator

- Enter the field separator used in your import file.  The
  most common used separator is the comma, however certain files may contain
  hyphens or other symbols.

![](/img/cset4.gif)

Skip First
Record - If this box is checked the first line of the import file
will be ignored. This should be checked if the first line is used as a
header description.

Double Quotation
Marks - Check this box if your file has quotation marks around
each field.  (ex âJose Smithâ,â111 InfiniTimeâ¢
Stâ,âOrange, AZ 85302â)

Proper Case
All Imported Text â Imports all text into proper case form. (Ex.
Jose Smith not jose smith)

Empty Source
File After Import â This field should be checked if you want to
empty the source file after you import.

### Duplicate Checking

Duplicate checking gives you the option to look for duplicate entries
in your import file compared to data that is already in the program.  Additional
duplicate checking configuration is not required when importing.

![](/img/QSG_SETUP_IMP_SFOPTIONS.gif)

If duplicate is found:

Add Duplicate
To The File - To add the duplicate to the file without prompting
or replacing the existing file, check this field. Duplicates can be stored
in a text file if this option is checked. See below.

Store Duplicates
in a text File - If this box is checked, enter a path to create
a file.  This file will contain all  duplicates that the program
found while importing.

Replace
Existing Record Without Prompt - To replace the record without
prompting check this field.  For example, this option should be selected
if you are updating existing employee records will current contact or
address information. Additionally, this option must be selected in order
to import Employee Accrual Totals or Employee Group Assignments using
the Employee Groups Import File Type.

Ignore
It - If this field is checked, the program will simply ignore duplicate
records completely.

![](/img/CH7_Timecard7.gif)

This window allows you to select which
fields to check for duplication.  To select a field, highlight the
Field Name and click on the ![](/img/cset21.gif)
Button.

Note: When Importing Employee Timecards it
is important to ensure duplicate records present in the import file will
be ignored. To ensure duplicate punches, or punches for a specific employee
with the same Time and Date, are not imported Date and Time must be tagged
on the Duplicate Checking Tab as outlined below.

1. Click on the Duplicate Checking tab after
   selecting a source file.

2. Type Date in the search box and click
   on the Search Button.

3. Click Tag.

4. Type Time in the search box and click
   on the Search Button.

5. Click Tag.

6. Ensure 'Ingore It' is selected for 'If
   Duplicates are found:'

7. Continue configuring the Import.

### Map Destination Fields

Mapping the destination fields is the final phase of the import process.
 Here you will map the fields that reside in your import file to
the fields that are in the InfiniTime
program. It is important to verify all required fields are mapped when
performing an import. Refer to Chapter 11 - Target Fields Available to
be Imported for more information regarding required fields and import
file format.

![](/img/i18.gif)

Import Fields - Import Fields
appear in the grid on the left. These are from the file selection on the
Source File Options tab.

![](/img/db2.gif)

Target Fields - Target Fields
appear in the grid on the right. These are the fields that are in the
InfiniTime Program.

![](/img/image465.gif)

How To Map The Fields

To map the fields, start by highlighting
the Source File Field on the left side grid. Then highlight the desired
target field on the right side grid. Use the grid controls to change between
pages in order to see all available fields.

The controls in the center of the screen
are used to associate the selected import field with the selected target
field as detailed below.

![](/img/QSG_SETUP_IMP_SOURCEFILEOP.gif)
â Associates the Selected Import field with the Selected Target Field.
You will notice that the data in the Import grid will be displayed in
the target grid after association is complete.

![](/img/i1.gif)
â Removes any association for the selected Target Grid Field. You will
notice that the data in the Target grid will be removed.

![](/img/cset28.gif)
â Removes all associations for the Target Grid. All data in the target
grid will be removed.

![](/img/StartHousekeeping.gif)

![](/img/winbackuprestore1.gif)-
 This button is used to remove a field that you have already dragged
over onto the field mapping area. This will not permanently remove the
field. It will simply put it back on the left side of the screen.

![](/img/Ch11_Export16.gif)

- This button is used to remove a field that you have already mapped  This
  will not permanently remove the field.  It will simply put it back
  on the left side of the screen.  \*THIS
  WILL REMOVE ALL OF THE FIELDS THAT YOU HAVE MAPPED!

![](/img/cb2.gif)

- Select this button if the header labels  (First Line of your import
  file)  match the fields that you wish to import.  This will
  eliminate you from having to drag over the fields. This will only work
  if the header of your import file contains the same field names as those
  shown to the left of the Target Field.

![](/img/i10.gif)

- Select this button if all of the fields that are in your import file
  are in the same order as the fields in the Target Grid.  If you select
  this button and your file is not in the same import you can cause file
  corruption, be sure to take a backup before attempting to Import Employee
  information.

![](/img/Hardware_settings_synel.gif) - Select this button to set the date picture. It will
bring up the Date Picture Form as shown below. The picture button is only
available for Target Fields that have an entry in the Picture Column.

For example, you can specify the date format
and separator used within the import file by changing the date picture
and separator:

![](/img/CH11_ImportFields_Department.gif)

![](/img/RLSNOTE_707-07.jpg) - The Override button brings up the Override option
in the Import tool.  This allows the user more flexibility to customize
the settings before the file is imported, i.e. the file being imported
may have all the employees in separate departments, the user can select
the Department link to be Department A only and all employees imported
from the file will fall under Department A instead of their own individual
departments.

![](/img/tcard08.gif)

Override
Option Type â This drop down menu brings up a set of options to
select from.  This determines the method by which the entry in the
import file will be overwritten with. This drop down menu can only be
viewed if a source field is assigned to the target field you are attempting
to override.

![](/img/TP6.gif)

The user can select from the options listed
below to override the field's original value. Some options are only available
for certain field types.

Single Value
â A set value that will be a constant for each record imported into a
specific field.  This will overwrite the original in the file with
the phrase or word inserted by the user for all records.

Conditional Override
â Fields that will be overwritten if a condition is met. For example if
your old software listed gender as M or F you could use conditional override
to replace M with Male and F with Female as InfiniTime
uses the full word for gender instead of an abbreviation. This is shown
in the example below. Conditional Override is supported for both Link
To and regular field types.

![](/img/CH11_ImportFields_Employee.gif)

Click insert to insert a new condition.

![](/img/CH11Export_Email.gif)

The IF
and Then field displays will be
determined by what Target Field
is selected when the Override is selected.  In this example, Employee
Gender is the Target Field.  To complete this form, determine what
conditions must be met and fill them accordingly.

(i.e. If Employee Gender equals F, Then Import
Employee Gender as Female.)

Lookup In
Another Table â This option looks up information from a separate
field, such as the Department or Security Role table. This is only displayed
when Override is used for a âLink Toâ field such as Link to Department
Table or Link to Security Role Table.  (i.e. Department names)

Parse Current
Value â This option breaks down a field/record in an imported file
to become a more accessible record.  For instance, if the import
file has every record under one field in an Excel worksheet, it can be
broken down as if it were all in separate fields.  (i.e. First and
Last name are in the same field.  By parsing the field, the user
can separate the First and Last name to be imported as two separate fields.)

The Parse
position type can be either by Character, Position, or Both.  By
Character it means to start or end the value by the designated character
chosen by the user, (i.e. -, , â, or a space.)

To Parse
by Position means to start or end the value by the numbered position of
the characters in that record.  (i.e.  Daniel Kraus, is the
record we wish to parse.  Start Position would be 1, pertaining to
D.  End Position would be 6, as to L.)

Saving
The import - To save the import structure that you have created
click the OK button. Once the file is saved you will return to the Import
Definition Table.  To import a saved structure,  highlight it
and click on the Import button.

### Auto Import Configuration

![](/img/CH15_Sysmon3.gif)

InfiniTime allows a schedule
to be configured in order to perform an import automatically at a regular
interval. This is often used to update employee information within the
InfiniTime application
from an external source on a regular basis. The following tasks must be
performed prior to performing an automatic import:

1.) A comma delimited import file must be prepared and placed in the
import directory. The import file must adhere to all database constraints.

2.) An Import Criteria must be configured for the import file. The name
of the import file must always match the name specified in the Import
Criteria or the import will fail.

3.) Atleast one Auto Import Schedule must be defined before an import
will be performed automatically.

Note: The InfiniTimeHouseKeeping
service must be running in order for an import to be performed automatically.
The import file must be present in the Import directory with the same
file name as that specified on the Import Criteria.

Insert
â Click insert to open up the Auto Import Schedule Update Form and set
a schedule.

Change
â Click change to make any adjustments to a previously configured schedule.

Delete
â Click delete to remove the highlighted Import Schedule.

![](/img/i15.gif)

Description
â Describes the Import Schedule you are creating.

Frequency
â This is how often the program will run the auto import.  The options
are: Once, Daily, Weekly, and Monthly.

Date to
Importâ This is the date that you want the system to execute the
auto import.

Time to
Import â This is the time that you want the system to execute the
auto import on the date selected above.

Date Last
Printed â Tells you the last date the system automatically ran
the import.

Time Last
Printed â Tells you the last time on the date above the system
automatically ran the import.

Date to
Import Next â The date entered here will be the next future date
that the system will automatically perform an import.

Time to
Import Next - The time entered here will be the next future time
that the system will automatically perform an import.

### Export Introduction

The Export tool makes it possible to export nearly every field within
the InfiniTime software
into a comma delimited file in a format specified by the user. The exported
information can then be imported into another application or distributed
as required. It is important to understand the different tables which
store information within the InfiniTime
database as a single export can only contain fields from one table. An
overview of each file type that can be exported from the tables within
InfiniTime is provided
below.

Selecting an Export File type:

Before an export can be configured the user must understand what information
is desired within the export file. A brief description of the fields available
for each file is provided below. Refer to Chapter 11: Target Fields Available
for Export for a complete list of all fields by file type.

![](/img/CH11_ImportFields_OtherAct.gif)

- Department File - Exports
  the fields necessary for the program to create departments.
- Employee Groups File -
  Exports the Group names and sub groups configured within InfiniTime.  Groups can be used
  to define Companies, locations, Etc
- Employee File - Exports
  Employee information into the program, this includes most HR information
  in InfiniTime.
- Employee Accrual Totals File
  - Exports past amounts of accruals earned by the employee.
- Employee Group Level File
  â Exports the level of the Groups that are in the file.
- Employee Group Description File
  - Exports the description of the Groups that are in the file.
- Other Activity Type File
   - Exports the fields necessary for the program to create Other
  Activity Types, Other Activity Types are tips, vacation, sick time,
  Etc
- Employee Shifts - Exports
  the shift schedules assigned to individual employees.
- Employee Timecard File - Exports
  Employee Timecard Punches.
- Activity Job Information File - Exports Activity Jobs. Each record in
  the import file will be used to add a job to the InfiniTime
  database. Useful for manufacturing companies with 100+ jobs.
- Activity Task Information File
  - Imports Activity Tasks. Each record in the import file will
    be used to add a job to the InfiniTime
    database. Useful for manufacturing companies with 100+ tasks.

### Export Configuration

Before data from InfiniTime
can be exported export criteria must be configured to provide details
regarding what information will be exported and what format and order
the fields will be exported in. Configuration examples are provided below.
The first step is to open the Export Definition Table.

Accessing
the InfiniTime Export Table:

- Click on Tools.
- Click on Import and Export.
- Click on Export.

![](/img/cb1.gif)

The Export Definition Table will be displayed
as shown below.

![](/img/ph7.gif)

![](/img/Purge.gif)

- The export button allows you to highlight an already saved export
  structure and export it.

![](/img/PollingDirect.jpg)

- The insert button will allow you to create a new export structure.

![](/img/clock_types.gif)
 -  This button will delete a highlighted export structure.

Performing
an Export:

The Export Update Form is displayed below.
There are two major sections of the Export Update Form, Source File Options
and Map Destination Fields, which must be configured properly in order
to achieve desired results. An example configuration is shown below with
a description of each field following.

![](/img/rb1.gif)

Export
Structure Description - Enter a description for the export you
are about to create.  Export descriptions are listed on the Export
Description Table for ease of use. In this way the user can identify the
information that will be exported without checking to see which fields
are mapped on the Export Update form. The description should be complete
and straight forward in describing the fields associated with the export.

Comma-Separated
File To Export - Specify a name for the file you would like to
create. The file will be exported to the InfiniTime
Output FTP site for access from Client Machines. The file may also be
accessed from C:\Inception\InfiniTime\InfiniTime7\Output
on the InfiniTime Server.  This assumes the default installation
location was used.

Technical Note: The
file name should not contain spaces or special characters. Only A through
Z and 0 through 9 are valid characters for use
when naming the file. It should also
be noted that a local path cannot be used. Files exported from InfiniTime are created on the server
and must then be transferred to client machines.

Field
Separator - Enter the field separator to be used in your export
file.  The most common used separator is the comma, however certain
files may contain hyphens or other symbols.

Insert
Header Record - If this box is checked the first line of the export
will be used as a header, describing the rest of the fields in the column.
The default header used for each field is the same as the fields name
which can be found in Chapter 11: Target Fields Available for Export

Double
Quotation Marks - Check this box if you want double quotation marks
to be placed around each field.  (IE: âJose
Smithâ,â111 InfiniTime
Stâ,âOrange, AZ 85302â)

Upper
Case All Exported Text â If this box is checked  all text
in will be exported in upper case form. (Ex. JOSE SMITH not Jose Smith)

Empty
Destination File before Export â Check this field to delete all
contents from the destination file before exporting. This action will
only be performed if the comma-separated file specified exists.

Do
Not Prompt to Save  - Check this field if you do not wish
the software to prompt you to download the file to your local machine
after it is created on the server.

Date Range
Name - This field is only available for the 'Employee Timecard
File' and 'Employee Accrual Hours' File Types. The Date Range Name settings
is used to specify the date range for which Employee Timecards or Accrual
Hours will be exported.

![](/img/Quick_Schedule_Table.gif) - The filter button allows you to specify
which employees records will be exported for. Only certain export types,
as listed below, support use of the Filter Button. For example, tagging
a department, group, or individual employees when using the Employee Accrual
Totals Export Type will export employee accrual totals for all employees
in the selected department, group, as well as for the tagged employees.

Send
File Via FTP -  Use this feature
to automatically transfer the file via FTP (File Transfer Protocol) to
a destination of your choice. The following fields will become available
and must be filled out. An example is shown below. Keep the items that
follow in mind when entering this information.

- A domain name
  or IP Address can be used in the Host Address Field.
- Do not include
  the ftp:// prefix in the Host Address Field.
- The Directory
  field can be left blank if you are uploading to the root of the FTP
  Site.
- If you wish to
  upload to a specific folder on the FTP site you must specify the full
  path using a preceding forward slash ( / ) as shown in the image below.
- The Login Name
  can be a Local Windows Account, a Domain Account, or Anonymous. Enter
  the Login Name in one of the following formats:

Local
Windows Accounts:

![](/img/maint10.gif)

1. Enter the Host Address
   There are two valid formats for the host
   address field as detailed below. Do
   not include the ftp:// prefix in this field.

| Valid Host Address Formats |                    |
| -------------------------- | ------------------ |
| Format Type                | Example            |
| IP Address                 | 192.168.1.20       |
| Domain Name                | www.InfiniTime.com |

2. Enter the Directory.
   Remember to include a preceding forward slash as shown.

3. Enter the Login
   Name in the following format: "HOSTNAME\USER"  For Example
   if your FTP Server's hostname is FTPSERVER and the user you wish to connect
   as is FTPUSER then you would enter the following:

FTPSERVER\FTPUSER

4. Enter the user's
   password.

5. Specify the port
   to use when connecting to the FTP Server. This does not generally need
   to be altered.

Domain
Accounts:

![](/img/CH11_ImportFields_Schedules.gif)

1. Enter the Host Address.
   There are two valid formats for the host
   address field as detailed below. Do
   not include the ftp:// prefix in this field.

| Valid Host Address Formats |                    |
| -------------------------- | ------------------ |
| Format Type                | Example            |
| IP Address                 | 192.168.1.20       |
| Domain Name                | www.InfiniTime.com |

2. Enter the Directory.
   Remember to include a preceding forward slash as shown.

3. Enter the Login
   Name in the following format: "DOMAIN\USER"  For Example
   if your FTP Server's domain is InfiniTime
   and the user you wish to connect as is FTPUSER then you would enter the
   following:

InfiniTime\FTPUSER

4. Enter the user's
   password.

5. Specify the port
   to use when connecting to the FTP Server. This does not generally need
   to be altered.

Anonymous
User:

![](/img/Ch11_Export22.gif)

1. Enter the Host Address.
   There are two valid formats for the host
   address field as detailed below. Do
   not include the ftp:// prefix in this field.

| Valid Host Address Formats |                    |
| -------------------------- | ------------------ |
| Format Type                | Example            |
| IP Address                 | 192.168.1.20       |
| Domain Name                | www.InfiniTime.com |

2. Enter the Directory.
   Remember to include a preceding forward slash as shown.

3. Enter Anonymous
   as the Login Name.

4. Leave the password
   field blank.

5. Specify the port
   to use when connecting to the FTP Server. This does not generally need
   to be altered.

Technical Note:
Microsoft IIS includes an option to permit only anonymous connections
to an FTP Site. If this option is checked as shown below only anonymous
connections to the FTP Site will be allowed. This means ANYONE can access
the payroll export file. This option should be unchecked and it should
be confirmed that a login is required to gain read or write access to
the directory where the Payroll Export File will be uploaded. Please contact
your Information Technology Personnel for assistance with checking file
permissions on your FTP Site.

![](/img/Ch11_Export8.gif)

Technical Note:
InfiniTime
attempts to connect to the FTP Site to validate the Login ID, Password,
and Directory when the OK Button is clicked on the Payroll Export Update
Form. If InfiniTime is
unable to successfully connect to the FTP Site with the provided login
information, or if the specified directory does not exist, an error will
be displayed.

Mapping
Fields to be Exported

Mapping the destination
fields is one of the two crucial parts of Export Configuration.  Here
you will specify which fields will be exported from the InfiniTime software, arrange them
in the desired order, and specify and formatting details.

Export
Fields - Export Fields appear in the grid on the left. All available
fields for your selected export table are displayed.

![](/img/i4.gif)

Target
Fields - Target Fields appear in the grid on the right. These are
the fields that will be exported to your file. An example of an export
listing Employee Addresses, Names, and Employee IDs
is displayed below.

![](/img/maint3.gif)

How To Map The Fields

To map the fields, start
by highlighting an available field on the left side grid. Then use the
controls in the center of the screen or the Add Field Buttons to move
the field to the Target Grid. Use the grid controls to change between
pages in order to see all available fields. It may help to use the search
feature in the grid listing fields for export in order to find the desired
field. This helps save time when compared with checking through several
pages of fields by finding the desired field immediately. For example,
if you wanted to map the Employee ID field you could search for 'ID',
'Employee', or 'ID'. All fields containing the search term in the name
will be returned, narrowing the amount of fields displayed by a considerable
amount.

The controls in the
center of the screen are used to associate the selected export field with
the selected target field as detailed below.

![](/img/CH11_ImportFields_Schedules.gif)
â Adds the selected field to the target grid.

![](/img/rb4.gif)
â Adds all available fields to the Target Grid.

![](/img/TaskImport.gif)
â Removes the selected Target Grid Field. You will notice the data in
the Target grid will be removed.

![](/img/TimecardReviewHistory.jpg)â
Removes all associations for the Target Grid. All data in the target grid
will be removed.

Altering
Export Format and Field Order

A variety of tools and
buttons are provided on the lower right hand corner of the Map Desintation Fields tab. Most of these buttons
are hidden until atleast one field has been
added to the Target Field grid. Each serves a separate purpose in the
configuration of an export and are especially useful when the user has
a particular format in mind.  The use of each tool is outlined below.

![](/img/Ch11_Export22.gif)

![](/img/i26.gif) - Adds information entered by the user to
the export. The software prompts the user for information which is then
entered for each employee in the column corresponding to the user defined
field. An example is shown below where the date 2/2/2008 is inserted between
the employee ID and the Employee Name for each employee exported.

1.) Click on ![](/img/tcard11.gif)
to open the User Defined Field Update Form. Enter the information that
will be placed in the User Field for each employee.

![](/img/cset12.gif)

2.) Click OK. The User
Field label will be displayed in the header column as shown.

![](/img/EmailWindow.gif)

3.) Click on the ![](/img/QS_Chapter1_14.gif)
button to change the header if desired. The Export Override Header Update
Form will be displayed as shown. Simply type the desired header and click
OK to save. Changing the Header for the user field does not change the
value that will be exported for all records. The original value entered
when the user field was inserted will still be exported for each record.
To change the value exported in the user field column for each record,
use Single Value Override.

![](/img/Ch11_Export16.gif)

4.) The header will
be updated as shown.

![](/img/Ch11_Export13.gif)

5.) Save the export
settings by clicking OK on the Export Update form. Highlight the Export
Definition and click export.

6.) You will be prompted
to download the export file. An example of how the user entered information
is formatted in the export file is shown below. Column B shows the user
entered heading of "Export Date" and the user entered value
2/2/2008.

![](/img/QS_Chapter1_13.gif)

![](/img/cset33.gif)

- Adds all Export Fields to the Target Grid.

![](/img/maint6.gif) - The order of the export file is defined
by the fields in the target grid. The first field on Page 1 will be exported
as the first column of the export file. The second field will be in the
second column, while the third field will be in the third column, ect. This button will move the Selected Target Field
up in the order. IE: If the third field is highlighted
when this button is used it will be moved up to the second position while
the field that was in the second position will move down.

![](/img/i21.gif) - The order of the export file is defined
by the fields in the target grid. The first field on Page 1 will be exported
as the first column of the export file. The second field will be in the
second column, while the third field will be in the third column, ect. This button will move the Selected Target Field
down in the order. IE: If the third field is
highlighted when this button is used it will be moved down to the fourth
position while the field that was in the fourth position will move up.

![](/img/i23.gif) - The Override button opens the Export Override
Update Form.  This gives the user more flexibility to customize the
data before a file is exported. For example if a company had multiple
locations they may assign a unique identifier to each location when designating
employee IDs. Lets say the unique identifier
is the first three digits of every Employee ID in the InfiniTime
Software and they want the export to have a column where only the unique
identifier for each location is listed. In this way the final file could
be opened with Microsoft Excel and sorted by the location identifier in
order to easily distinguish employees in one location from the next. This
could be accomplished through Override by using the Parse Current Value
Override Option. More information on the types of override available and
their use can be found below.

Select a field in the
Target Export Grid and click on the Override button. The Export Override
Update form will be displayed as shown.

![](/img/Ch11_Export7.gif)

Override
Option Type â This drop down menu brings up a set of options to
select from.  This determines the method by which the entry in the
export file will be overwritten with. This drop down menu can only be
viewed if a source field is assigned to the target field you are attempting
to override.

![](/img/Ch11_Export2.gif)

The user
can select from the options listed below to override the field's original
value. Some options are only available for certain field types.

Single
Value â Exports a constant value for a given field for each exported
record, regardless of the fields original value.  This will overwrite
the original in the file with the phrase or word inserted by the user
for all records. It should be noted that the Single Value override can
be used to add a blank column to an export by adding a user defined field
and overriding it with a space using the single value option.

Concatenation Override - Permits
user to concatenate, or string together, multiple fields. Extra text such
as punctuation, spaces, or an alphanumeric value can be inserted after
each concatenated field. This feature is useful for exporting multiple
InfiniTime fields to a
single column. For example: John C. Smith can be exported using the settings
shown below.

![](/img/Ch11_Export17.gif)

Conditional Override â Exports
a specified string if the field's original value matches a predefined
value. For example, if the Employee's Marital Status is Married then export
M. Or, if the Employee's Marital Status is Single then export S. This
is often useful if you are attempting to export information from InfiniTime and import it into another
software application, such as a payroll application. If your payroll software
tracks gender with M and F rather than Male or Female conditional override
can be used to export M and F rather than Male and Female for the Employee
Gender field. This example is explained below.

![](/img/db2.gif)

Click insert to insert
a new condition.

![](/img/CH11_ImportFields_GroupLevel.gif)

The IF
and Then field labels will be
determined by what Target Field
is selected when the Override is selected.  In this example, Employee
Gender is the Target Field.  To complete this form, determine what
conditions must be met and fill them accordingly.

(i.e. If Employee Gender
equals Male, Then Export Employee Gender as M.)

Lookup
In Another Table â This option looks up information from a separate
field, such as the Department or Security Role table. This is only displayed
when Override is used for a âLink Toâ field such as Link to Department
Table or Link to Security Role Table.  (i.e. Department names)

Parse
Current Value â This option breaks down a field/record in an exported
file to export only parts of the record.  For example if a company
had multiple locations they may assign a unique identifier to each location
when designating employee IDs. Lets say the
unique identifier is the first three digits of every Employee ID in the
InfiniTime Software and
they want the export to have a column where only the unique identifier
for each location is listed. In this way the final file could be opened
with Microsoft Excel and sorted by the location identifier in order to
easily distinguish employees in one location from the next.

The Parse
position type can be either by Character or Position.  By Character
it means to start or end the value by the designated character chosen
by the user, (i.e. -, , â, or a space.)

To Parse
by Position means to start or end the value by the numbered position of
the characters in that record.  (i.e.  Daniel Kraus,
is the record we wish to parse.  Start Position would be 1, pertaining
to D.  End Position would be 6, as to L.)

Saving
The import - To save the import structure that you have created
click the OK button. Once the file is saved you will return to the Import
Definition Table.  To import a saved structure,  highlight it
and click on the Import button.

![](/img/cset19.gif) - The Header Button provides the user with
the ability to alter the default header used by InfiniTime.
Select a field in the target grid and click on the Header Button to display
the Export Override Header Update Form. Refer to the example above where
the header button is used to alter the header on a User Field.

![](/img/Ch11_Export4.gif)

- Select this button to set the date picture. It will bring up the Date
  Picture Form as shown below. The picture button is only available for
  Export Fields that have an entry in the Picture Column.

For example, you can specify the date format
and separator used within the import file by changing the date picture
and separator:

![](/img/InLineEdit_1.jpg)

![](/img/ph4.gif) - Restores
Override and Picture settings for the highlighted target field to the
defaults.

### Email

Export files can be emailed
by setting the options on the Email Tab. Simply enter the appropriate
information in each field below.

Note: All
Fields on the Email Tab should be filled. Do not leave any fields blank.

Note: Are recipients having trouble with receiving
Email from InfiniTime ?
Refer to [InfiniTime Server SMTP Setup and Troubleshooting](https://version9.infinitimeonline.net/InfiniTime/RESOURCES/SMTP Email Setup And Troubleshooting.pdf)
for information on configuring and troubleshooting SMTP Service Settings
on the InfiniTime Server.

![](/img/cset1.gif)

From

- Type in the email address of the sender, if a recipient wants to reply
  to the email they can do so, and it will get back to the original sender.

Subject
â Type a subject for the email.

Body
Text â Type your message in this field.

Sent
To â The sent to grid displays all recipients that the payroll
export will be sent to. Recipients are inserted by using the Insert button.

Insert
â Used to insert a new recipient as shown below.

![](/img/3WAVG.jpg).gif)

Email To Name

- Enter the Name of the recipient.

Email To Address

- Enter the Email Address of the recipient.

Auto
Export Configuration

InfiniTime allows a schedule
to be configured in order to perform an export automatically at a regular
interval. This is often used to update employee information within an
external application from data stored within InfiniTime
on a regular basis. The following tasks must be performed prior to performing
an automatic export:

1.) An Export Criteria must be configured.

3.) At least one Auto Export Schedule must be defined before an import
will be performed automatically.

Note: The InfiniTimeHouseKeeping
service must be running in order for an import to be performed automatically.
The import file must be present in the Import directory with the same
file name as that specified on the Import Criteria.

![](/img/ph5.gif)

Insert
â Click insert to open up the Auto Export Schedule Update Form and set
a schedule.

Change
â Click change to make any adjustments to a previously configured schedule.

Delete
â Click delete to remove the highlighted Import Schedule.

![](/img/i27.gif)

Description
â Describes the Import Schedule you are creating.

Frequency
â This is how often the program will run the auto import.  The options
are: Once, Daily, Weekly, and Monthly.

Date to
Importâ This is the date that you want the system to execute the
auto import.

Time to
Import â This is the time that you want the system to execute the
auto import on the date selected above.

Date Last
Printed â Tells you the last date the system automatically ran
the import.

Time Last
Printed â Tells you the last time on the date above the system
automatically ran the import.

Date to
Import Next â The date entered here will be the next future date
that the system will automatically perform an import.

Time to
Import Next - The time entered here will be the next future time
that the system will automatically perform an import.

### Target Fields Available to be exported

Employee File

(In Alphabetical Order)

Employee Access Control Group

Employee Accrual Type

Employee Additional Withholding Amount
for Federal Taxes

Employee Additional Withholding Amount
for Local

Employee Additional Withholding Amount
for State

Employee Address Line One

Employee Address Line Two

Employee Adjusted Hire Date

Employee City Name

Employee Date of Birth

Employee Date of Hire

Employee Date of Termination

Employee Default Department

Employee EEO Type

Employee Email Address

Employee Emergency Contact Person

Employee Emergency Contact Phone Number

Employee Emergency Contact Relationship

Employee Employee Badge ID

Employee Employee Login ID

Employee Employee Login Password

Employee Escort

Employee Ethnic Code

Employee Federal Exemptions

Employee First Dir. Dep. ABA Routing Number

Employee First Dir. Dep. Acct Type

Employee First Dir. Dep. Amount

Employee First Dir. Dep. Amt Type

Employee First Dir. Dep. Bank Account Number

Employee First Dir. Dep. End Date

Employee First Dir. Dep. Name on Account

Employee First Dir. Dep. Priority

Employee First Dir. Dep. Start Date

Employee First Name

Employee Force Password Change Next Login

Employee Fourth Dir. Dep. ABA Routing Number

Employee Fourth Dir. Dep. Acct Type

Employee Fourth Dir. Dep. Amount

Employee Fourth Dir. Dep. Amt Type

Employee Fourth Dir. Dep. Bank Account
Number

Employee Fourth Dir. Dep. End Date

Employee Fourth Dir. Dep. Name on Account

Employee Fourth Dir. Dep. Priority

Employee Fourth Dir. Dep. Start Date

Employee Gender

Employee Holiday Schedule Type

Employee Hourly Wage

Employee Id

Employee Inactive Flag

Employee Job Title

Employee Last Name

Employee Last Performance Review Date

Employee Last Raise Date

Employee Last Wage Review Date

Employee Local Exemptions

Employee Local Taxing Authority

Employee Marital Status

Employee maximum Authorized Amount

Employee Message

Employee Middle Initial

Employee Minimum Authorized Amount

Employee name

Employee Other Ethnic Code

Employee Pay Cycle

Employee Pay Method

Employee Pay Type

Employee Phone Number

Employee Picture Image Name

Employee Policy

Employee Schedule Cycle

Employee Schedule Cycle Days

Employee Schedule Reference Date

Employee Second Dir. Dep. ABA Routing Number

Employee Second Dir. Dep. Acct Type

Employee Second Dir. Dep. Amount

Employee Second Dir. Dep. Amt Type

Employee Second Dir. Dep. Bank Account
Number

Employee Second Dir. Dep. End Date

Employee Second Dir. Dep. Name on Account

Employee Second Dir. Dep. Priority

Employee Second Dir. Dep. Start Date

Employee Security Role

Employee Social Security Number

Employee State

Employee State Exemptions

Employee State Marital Status

Employee State Taxing Authority

Employee Termination Reason

Employee Third Dir. Dep. ABA Routing Number

Employee Third Dir. Dep. Acct Type

Employee Third Dir. Dep. Amount

Employee Third Dir. Dep. Amt Type

Employee Third Dir. Dep. Bank Account Number

Employee Third Dir. Dep. End Date

Employee Third Dir. Dep. Name on Account

Employee Third Dir. Dep. Priority

Employee Third Dir. Dep. Start Date

Employee Workers Compensation Code

Employee Zip Code

Department File

(In
Alphabetical Order)

Department Cost Center

Department Default Flag

Department Inactive Flag

Department Name

Department Number

Department Schedule Cycle

Department Schedule Cycle Days

Department Schedule Reference Date

Employee
Accrual Totals File

(In
Alphabetical Order)

Accrual Detail Name

Accrual
Type Name

Employee
Accrual Totals Date

Employee
Accrual Totals Time Accrued

Employee Accrual Totals Time Base

Employee Accrual Totals Time Used

Employee
First Name

Employee Id

Employee
Last Name

Employee Middle Initial

Other Activity
Type File

(In
Alphabetical Order)

Other Activity Type

Other Activity Type Code Number

Other
Activity Type Count activity Hours as Regular Hours Flag

Other
Activity Type Count As Day Worked Flag

Other
Activity Type Description

Other
Activity Type Exclude From Payroll Export Flag

Other Activity Type Payroll Mapping Code

Payroll
Mapping Number

Employee Groups

(In
Alphabetical Order)

Employee First Name

Employee Id

Employee
Last Name

Employee Middle Initial

Group
Description

Group level Description

Employee Group Level File

(In
Alphabetical Order)

Group
Level

Group Level Description

Employee Group Description File

(In
Alphabetical Order)

Group Description

Group Level Description

Employee Shifts File

(In
Alphabetical Order)

Department Name

Employee
First Name

Employee Id

Employee
Last Name

Employee Middle Initial

Policy Name

Shift Name

Employee Timecard File

Approved overtime hours

Approved overtime hours four

Approved overtime hours three

Approved overtime hours two

Break Hours

Calculation Override

Clock Description

Date

Department Name

Department Number

Employee Employee Login ID

Employee First Name

Employee ID

Employee Last Name

Other Activity Type Description

Other Amount

Other Hours

Regular Hours

Telephone Number

Time

Type

Unapproved overtime Hours

Unapproved overtime hours Four

Unapproved overtime hours Three

Unapproved overtime hours two

### Service Maintenance Introduction

InfiniTime provides a
unique solution for server maintenance allowing system administrators
to alert users of maintenance schedules and even force users out of the
software. This solution prevents data loss and possible database issues
by assuring users are unable to login or alter the database while the
system is down for maintenance.

### Setting a Maintenance Warning

The server maintenance warning can be used to notify users of scheduled
maintenance. Server maintenance messages are read from a text file called
servergoingdown.txt located in the original program installation directory,or
C:\Inception\InfiniTime\InfiniTime7\,
by default.  Instructions for configuring a Server Maintenance Warning
are provided below.

![](/img/tcard07.gif)

- Locate your software install location. If you installed to a location
  other than the default you are responsible for locating the files
  yourself. The default location is C:\Inception\InfiniTime\InfiniTime7\

- Click Start.

![](/img/Import001.gif)

- Click Run.

![](/img/Import002.gif)

- Type your software install location and click OK.

![](/img/e5.gif)

- Open the InfiniTime7 Folder

![](/img/Ch11_Export1.gif)

- Right click in a blank area of windows explorer.

![](/img/RLSNOTE_707-02.jpg)

- Click New.

![](/img/CH15_PolledInfo.gif)

- Click Text Document.
- Name the text document servergoingdown.txt

![](/img/override_Tab.gif)

- Open the text document and type your desired warning message on
  the first line. Note: Only text located on the first line will be
  displayed in the Server Maintenance Warning.

![](/img/QS_Chapter1_11.gif)

### Server Shutdown

Taking InfiniTime
Down for Maintenance

Before performing maintenance on the InfiniTime
database or server InfiniTime
should be brought down. This is accomplished by inserting a text file
called serverdown.txt in the original software install location on the
InfiniTime server. Remote
clients will be denied access to the software if serverdown.txt is in
place, though the InfiniTime
Application can still be accessed from the InfiniTime
Server using shortcuts directed to localhost or 127.0.0.1. For example,
the shortcuts below can be used to access the InfiniTime
Application from the InfiniTime
Server.

http://localhost/InfiniTimeManagerModule/

http://127.0.0.1/InfiniTimeManagerModule/

Technical Note: Only Internet Explorer may be used to
access the InfiniTime Software
while Serverdown.txt is in place.

Steps to take InfiniTime 7.0 Down for Maintenance:

- Locate your software install location. If you installed to a location
  other than the default you are responsible for locating the files
  yourself. The default location is C:\Inception\Infinitime\
- Click Start.

![](/img/image463.gif)

- Click Run.

![](/img/InLineEdit_3.jpg)

- Type your software install location and click OK.

![](/img/CH11_ImportFields_Department.gif)

- Open the InfiniTime7
  Folder

![](/img/QS_Chapter1_13.gif)

- Right click in a blank area of windows explorer.

![](/img/maint9.gif)

- Click New.

![](/img/maint11.gif)

- Click Text Document.
- Name the text document serverdown.txt

![](/img/InLineEdit_2.jpg)

- No message is necessary. The software will automatically lock all
  users out of the program. Once serverdown.txt is placed in the Software
  Installation Directory (C:\Inception\InfiniTime\InfiniTime7\)
  any users logged into the software will be unable to navigate within
  the software or alter the database in any way. After placing the Serverdown.txt
  file, Software Administrators should wait five to ten minutes to be
  sure all users have been forcibly logged off before proceeding with
  server maintenance.

Users attempting to log into the software during the maintenance period
will see the following message:

![](/img/i17.gif)

Users already logged into the software when serverdown.txt is placed
in the InfiniTime7 directory will see the following warning when attempting
to perform any action within the software

![](/img/FilterButton-Normal.gif)
