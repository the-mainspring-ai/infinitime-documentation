---
title: "Thor Fingerprint - Menu & Bios"
description: "Guide to configuring clock settings, employee information, and troubleshooting for the Thor Fingerprint terminal, including menu access and InfiniTime software integration."
---

# Thor Fingerprint - Menu & Bios

The Thor Menu & Bios can be used to configure clock settings such as Communication Options, Speaker Volume, and Bell Ring Duration or for simply viewing employee information from the clock. In general users should not need to access the menu  if the Thor Terminal is connected to the InfiniTime Software as many Menu / BIOS settings are available from within the Application on the Reader Options Tab. (Click Tools - Clock Tools - System Monitor. Highlight the clock record and click change. Click on Reader Options on the left hand side.)

When the Thor terminal is connected to the InfiniTime Application the functions below must be performed via the menu. Most other options can be configured from within the InfiniTime Application after communication is established.

- Initial Communication Options configuration
- Communication Troubleshooting
- Performing a "Cold Boot" // Clearing Clock Settings

When the Thor terminal is located offsite and Time and Attendance Punches are gathered solely via Poll From File it may not be possible to connect to the clock from the InfiniTime Application. Therefore Hardware Settings must be configured at the clock rather than through the Reader Options within the InfiniTime Software. Once communication is achieved many BIOS settings can be altered from within the InfiniTime software.

Menu & Bios Table of Contents

[Managing Users on the InfiniTime Thor](#1)

[Communication Settings](#2)

[Thor System Configuration & Options](#3)

[Configuring the Date & Time Display](#4)

[USB Thumb Drive Features](#5)

[Automated System Tests](#6)

[Punch Records On the Thor Terminal](#7)

[Thor Device & System Information](#8)

Managing Users on the InfiniTime Thor

1. User Mng

1. New User - Creates a new employee record on the InfiniTime Thor. The user will be prompted for an Employee ID, Name, Security Role, And to enroll a Fingerprint. Employees should not be entered into the Thor Terminal from the clock itself. Remember InfiniTime will remove employee records from the Thor terminal during the update process if they are not present in the InfiniTime Database. For this reason employee records should be created within the InfiniTime Application and sent to the Thor Terminal through the update process.

1. Manage - Displays a list of all employees present on the Thor Terminal. The following information is displayed for each employee:

Security Indicator - The Lock icon indicates the employee has supervisor or administrator access.

ID No.- Displays the Employee ID Number as set within the InfiniTime Application.

Name - Displays the name of the Employee as set within the InfiniTime Application.

FP - Indicates the number of fingerprints enrolled for the employee.

PWD - The Key icon indicates a password has been set for an employee.

Card - The Card icon indicates a Badge has been enrolled for an employee.

3. Access - Configuration Menu for Access Control Settings.

Access Control Parameters - Configuration Menu for Access Control and Relay Settings.

Lock - Duration for which lock remains open after a successful Access Control Authentication or when the Door Release button is pressed.

DSen. Delay - Controls the Alarm Delay. If the door sensor should detect an open door for the number of seconds specified in this field the Alarm will activate.

DSen. Mode - (Closed, Open, None) Sets the Normal electrical Mode of the Door Sensor. Closed refers to Normally Closed where Open Refers to Normally Open. If the Door Sensor mode is set to None the Door Sensor is disabled and the Alarm will not trigger.

Alarm Delay - Determines the length of the Alarm which will play when the Door Sensor Delay expires.

Alarm Count - The number of times the Alarm bell will sound.

Duress Alarm Parameters - Configuration Menu for Tamper / Duress Alarm

1:1 Trig - If set to Yes the alarm will be activated when a successful match for a user with a single enrolled fingerprint occurs.

1:N Trig - If set to Yes the alarm will be activated when a successful match for a user with multiple enrolled fingerprints occurs.

Pwd Trig - If set to Yes the alarm will be activated when a user successfully authenticates using their Employee ID and Password.

Alarm Delay - Sets the amount of time the Thor Terminal will wait before sounding an alarm after one of the four conditions defined above occurs. (1 - 255 Seconds)

Communication Settings

2. Comm.- Communication Settings Menu.

1. Network - Configuration Menu for Ethernet Settings.

IP Address - Used for Ethernet Communication. Sets the IP Address which will be used by the Thor Terminal. The IP Address on the Thor Terminal must be static. Consult your Network Administrator for assistance if you are unsure if the IP Address you wish to assign to the clock is a Static IP Address.

Subnet Mask - NetMask - Used for Ethernet Communication. Sets the Subnet Mask which will be used by the Thor Terminal. This should match the subnet mask used by other devices on your network. Contact your Network Administrator for assistance if you are unsure of the Subnet Mask used on your network.

Gateway - Used for Ethernet Communication. Sets the Default Gateway which will be used by the Thor Terminal. This generally points to the device performing routing services for your network.

NetSpeed - Used for Ethernet Communication. Specifies the speed at which the Thor Terminal will communicate with other devices on the network. If the Thor Terminal is located at a remote site or across a slow WAN link it may help to set the clock to 10M.

10M - 10 Megabit

100M - 100 Megabit

Auto - Automatic Negotiation of Network Speed

2. RS232/485

Baud (9600 - 115200 Bps) Used for Direct Connect Communication (RS232 and RS485). Specifies the speed at which the Thor Terminal will communicate with the InfiniTime Server. The baud rate is set to 115200 by default. The following options are available:  9600  19200  38400  57600  115200

RS232 (Yes or No) - Used for Direct Connect Communication (RS232). Specifies whether RS232 Communication is enabled (Y) or disabled (N). The RS232 and RS485 Options are mutually exclusive. They cannot be enabled simultaneously.

RS485 (Yes or No) - Used for Direct Connect Communication (RS485). Specifies whether RS485 Communication is enabled (Y) or disabled (N). The RS232 and RS485 Options are mutually exclusive. They cannot be enabled simultaneously.

3. Security

DeviceID - Used for RS484 Communication where multiple Thor Terminals are attached to a single cabling run. Even when not using RS485 Communication the Device ID Must match the Reader Address within the InfiniTime Application.

Password - Security feature utilized by the Thor Terminal. Must be set to 0. Users should not change this setting.

4. Wiegand

Input Opt - Set appropriately according to your Wiegand Device Manufacturers requirements.

Output Opt - - Set appropriately according to your Wiegand Device Manufacturers requirements.

Thor System Configuration & Options

3. System - Includes general Thor Configuration Options and System Details ranging from Date and Time Display to Function Key Configuration and current Bell Schedules.

1. System - General System Options

Threshold (1:1) - Sets the False Rejection Rate (FRR) used when comparing fingerprints for employees with a single finger enrolled. The default value set by InfiniTime is 35.

Threshold (1:N) -

Date Fmt - Defines the format for displaying dates on the Thor Terminal. MM/DD/YY is the default format where M stands for digits of the Month, D stands for digits of the day, and Y stands for digits of the year. IE: 10/31/1986

Keybeep - Used to enable or disable the beeping sound heard when pressing a button on the Thor Keyboard.

Voice - Used to enable or disable the voice prompts heard when successfully or unsuccessfully punching in or out.

Vol - (0-100%) Adjusts the Sound Volume of the Thor Terminal.

Log Alert - Displays a "Memory Near Full" warning when memory reaches the specified threshold. (1-99%)

ReCheck Min (Minutes) - A duration after the last punch out time, in minutes, during which employees may not punch in. This setting prevents employees from Punching In early after leaving for a break period and does not require the use of Schedules or Schedule Lockout. Employees will simply not be permitted to punch in during the ReCheck Min Duration. If an employee should attempt to punch in before the ReCheck Min duration expires, the Thor Terminal will display 'Sched. Violation' and play "Access Denied."

2. Data Mng

Delete Attlog - Removes all Time and Attendance Punches from the Zephyr Terminal. NOTE: All Activity on the clock will be removed by this option! Ensure the clock has been polled!

Delete All -  Removes all Employees, Administrators, Time and Attendance Punches, Departments, Jobs, and Other Activity Types from the Zephyr Terminal. NOTE: This option should not be used unless it is possible to connect the clock to the InfiniTime Application.

Clear Role - Sets all employees within the Thor Terminal to the 'User' Security Role. This makes it possible to enter the Menu without entering an ID/Password or placing your finger on the terminal.

Delete Picture - Removes Screensaver Images from the Thor Terminal. This feature is not used with the InfiniTime Software.

3. Update - Can be used to manually update the Thor Firmware from a USB Drive. This option should only be used with the guidance of qualified support personnel such as the Inception Technologies Staff or your Authorized InfiniTime Dealer.

4. Keyboard - The Keyboard Configuration Menu can be used to alter the Function Key Configuration for the Thor Terminal. Functions can be reassigned to different function keys if desired or they can be disabled entirely by configuring the function key to 'None' Default Function Key assignments are listed below.

| Function         | Key |
| ---------------- | --- |
| Transfer         | F1  |
| Access Control   | F2  |
| Hours            | F3  |
| Last Punch       | F4  |
| In/Out Board     | F5  |
| Employee Info    | F6  |
| Employee Request | F7  |
| Supervisor Tools | F8  |

5. Display - Configuration menu includes Clock Display and Screen Saver configuration options in addition to fail limits for Fingerprint and PIN Entry identification.

6. Reset - Sets all settings and communication options to their default values as if the clock were new from the factory. Note: The default IP Address on the Thor Terminal is 192.168.1.201. The following options are set by the Reset Feature:

Network Communication Settings

IP Address - 192.168.1.201

Network Mask - 255.255.255.0

Default Gateway - 0.0.0.0

RS232 Communication Settings

Baud Rate - 115200

RS232 Enabled

RS485 Disabled

Security Settings

Device ID = 1

Password = 0

External Wiegand Input Settings

External Wiegand Format - Wiegand26

External Wiegand Bit Count - 26

External Wiegand Pulse Width - 1000

External Wiegand Pulse Interval - 2200

System Settings

Keybeep - Enabled

Voice - Enabled

Volume - 67%

Log Alert - 99

Recheck Min - 0

System Display Settings

Sleep Time = 0

System Misc. Settings

Ext. Bell = ON

Int. Bell = ON

Power Key = Enabled

7. Bell - Displays Bell Schedules currently configured on the Thor Terminal. Bell Schedules are configured within the InfiniTime Application and sent to the Thor Terminal during the update process.

8. Misc Set - Miscellaneous Settings Menu

Ext. Bell - Determines whether an external bell will be used for Bell Schedules. This option must be set to yes for the bell relay to activate. InfiniTime automatically sets this option to Yes during the reader update process.

Bell in Clock - Determines whether an Internal or External Bell is used with the Thor Terminal for Bell Schedules. If this setting is set to On a bell sound will play according to the bell schedule. This option can be used in conjunction with an external bell.

Power Key - Controls the operation of the Power Key. Enable will allow the Power Key to turn the Thor Terminal On and Off. Disabled will make the key inactive and not function.

Configuring the Date & Time Display

4. Date/Time - Sets the current date and time on the Thor Terminal. The date format can also be set to 12H or 24H formats if desired.

USB Thumb Drive Features

5. USBDrive - USB Drive Management Options can be used to Download data from the Clock or Upload Information from the USB Drive into the Thor Terminal.

Download

Download ATTLog - Exports all Time and Attendance punches to the connected USB Thumb Drive. Time and Attendance activity will NOT BE removed from the Zephyr Terminal. A copy will only be placed on the thumb drive. The Clear ATT Logs option within System Options - Adv Options. Note that the Clear ATT Logs option will remove all activity from within the Zephyr terminal. Certain Zephyr Firmware Versions do not provide the necessary output for use with InfiniTime Poll From File. Ensure your Zephyr Terminal is on the latest Firmware version prior to clearing the ATT Logs on your Zephyr Terminal. Inception Technologies cannot be held responsible for data manually deleted by the user by following these instructions.

Download User - InfiniTime does not use this option at this time.

Download Photo - InfiniTime does not use this option at this time.

Upload

Upload User - InfiniTime does not use this option at this time.

Upload Photo - InfiniTime does not use this option at this time.

Upload Picture - InfiniTime does not use this option at this time.

Automated System Tests

6. Auto Test - Provides a range of self tests which can be performed to ensure proper hardware operation.

Test All - Performs all tests in sequence.

Test Display - Tests Video Output.

Test Audio - Plays all audio files on the terminal.

Test Keyboard - Displays a graphical representation of the Thor and highlights keys as they are pressed on the Keypad.

Test Sensor - Tests the Fingerprint Sensor.

Test RTC - Tests the Internal Clock.

Punch Records On the Thor Terminal

7. Record - Allows the user to pick a Start and End Date and displays all Employee Activity on the Thor Terminal within the selected date range. It should be noted that Employee Activity is polled from the Thor Terminal during the polling process after which it is stored within the InfiniTime Database. The Record table will only display punches that have yet to be polled from the Thor.

Thor Device & System Information

8. Sys Info

Records Tab - Displays the total number of Employees and Administrators enrolled in the Thor Terminal in addition to available memory space expressed in terms of Enrolled vs Available Fingerprints and the number of stored Time Records.

Device Tab - Displays device and firmware information.
