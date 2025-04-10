xml version="1.0" encoding="utf-8" ?





Messaging




# Messaging Introduction

InfiniTime includes an
internal messaging system, which can be used by employees to send notes
to management, request a schedule change, or even request time off. Messaging
is not intended to replace other standard means of communication such
as email or instant messaging within the workplace. Messaging users should
assume no privacy when sending messages. Any employee with access to the
senderâs employee record within the employee table can view an account
of all messages sent and received. Messages will be saved in the InfiniTime database indefinitely and
can only be altered or deleted if they are unread by all intended recipients.
Once a single recipient has viewed a message it cannot be removed from
the InfiniTime database.

Sending
Messages

Messages can be sent from within the manager module or employee module.
Larger buttons and clearer messaging controls are available from the Employee
module, as the employee module is centered on employee software usage
rather than employee management. Messaging functionality is not restricted
within the employee module. All messaging features are available in both
the Manager and Employee Modules.

* [Messaging
  within the Employee Module](/InfiniTime/help%20file/Messaging_within_the_Employee_Module.md)
* [Messaging
  within the Manager Module](/InfiniTime/help%20file/Messaging_within_the_Manager_Module.md)

# Messaging within the Employee Module

To access the Messaging Table:

* Login to the Employee Module.

![](images_2/tcard12.gif)

* The messages tab is displayed in the immediate background. Click
  on it to access the messaging table.

![](images_2/msg2.gif)

Messages sent to the employee within the specified date range are displayed
on the Incoming tab.

![](images_2/msg3.gif)

A history of messages sent by the employee within the date range specified
is displayed on the Outgoing tab.

# Messaging within the Manager Module

To access the Messaging Table:

* Login to the Manager Module.

![](images_2/tcard13.gif)

* The messages tab is displayed in the immediate background.

![](images_2/tcard15.gif)

Messages sent to the employee within the specified date range are displayed
on the Incoming tab.

![](images_2/msg6.gif)

A history of messages sent by the employee within the date range specified
is displayed on the Outgoing tab.

Messaging
Related Options and Warnings

Multiple Recipients

Time Off and Schedule
Change Requests are sent directly to employee supervisors by default though
multiple recipients can be specified by the user if the 'Allow Multiple
Request Recipients' option is enabled. Recipients can then approve or
decline the request as their discretion. Steps are listed below to enable
multiple recipients for Time Off and Schedule Change Requests.

1. Click on the Company
Button in the Manager Module.

![](images_2/MSG_CompanyButton.gif)

2. Check the 'Allow
Multiple Request Recipients box.'

![](images_2/FunctionalOptions_AllowMultipleRequests.gif)

Future
Date Warning

To prevent accidental entries InfiniTime will display the warning
below when Schedule Change Requests or Time Off Requests are sent more
than one year prior to the date(s) on the request.

![](images_2/DateWarning.gif)

# Message Types

InfiniTime includes three
separate message types. Each type of message has a specific purpose. A
detailed outline of these message types is provided below:

Notes

A note is a simple comment and includes a text message and description.
Notes default to an employeeâs supervisor as the recipient though they
can be sent to any employee. A note can also be sent to multiple employees
at once. Again, no privacy should be assumed when sending notes within
the InfiniTime software,
as any employee with access to the senderâs employee record can view a
full account of all messages sent by the employee.

[Click
Here for More Information on Schedule Change Off Requests](/InfiniTime/help%20file/Overview/Messaging/Messaging.md#msg13_Sending_a_Note_from_the_Message_Table)

Schedule
Change Requests

A schedule change request includes all facets of a note, with additional
information required to request a change in an employeeâs schedule. Schedule
Change requests are sent to an employee's supervisor by default though
multiple recipients can be specified by the user if the 'Allow Multiple
Request Recipients' option is enabled. Recipients can then approve or
deny the request at their discretion.

An approved schedule change request will alter the employeeâs schedule
with a GANTT chart entry. This ensures the change will override any type
of schedule the employee may have, as GANTT chart entries take precedence
over all schedule types. A reply will also be sent to the employee automatically
notifying them that the request was approved.

Should the request be denied the employeeâs schedule will not be altered
and a message will be automatically sent to the employee informing them
their request was denied.

[Click
Here for More Information on Schedule Change Off Requests](/InfiniTime/help%20file/Overview/Messaging/Messaging.md#msg15_Sending_a_Schedule_Change_Request)

Time Off
Requests

A Time Off request includes all facets of a note, with additional information
required to request Time Off. Time Off requests are sent to an employee's
supervisor by default though multiple recipients can be specified by the
user if the 'Allow Multiple Request Recipients' option is enabled. Recipients
can then approve or decline the request as their discretion.

An approved schedule change request will alter the employeeâs schedule
with a GANTT chart entry. This ensures the change will override any type
of schedule the employee may have, as GANTT chart entries take precedence
over all schedule types. An other activity entry will also be inserted
into the Employeeâs Timecard Activity. Managers pick the other activity
type upon approving the vacation request. Through use of other activity
types, an approved vacation can be either paid or unpaid. A reply will
also be sent to the employee automatically notifying them that the request
was approved.

Should the request be denied the employeeâs schedule will not be altered
and a message will be automatically sent to the employee informing them
their request was denied. Other activity entries will not be inserted.

[Click
Here for More Information on Time Off Requests](/InfiniTime/help%20file/Overview/Messaging/Messaging.md#msg20_Sending_a_Time_Off_Request)

Automated
Messages

Under specific circumstances InfiniTime
sends automated messages in order to notify supervisors of the actions
their employees have recently performed. If an employee should alter their
personal information within the InfiniTime
Employee Module a message will be sent to the employee's supervisor to
provide notification of the changes. The supervisor may then check the
employee's record to note the altered employee information.

# Sending a Note from the Message Table

Access the message table as described above within the Manager or Employee
Module.

* Click on the Outgoing Tab.

![](images_2/tcard18.gif)

* Click on Message.

![](images_2/msg8.gif)

* Enter a description for your message. This is similar to the subject
  of an email.

![](images_2/msg9.gif)

* Enter the message you wish to send to your supervisor in the Message
  Field.

![](images_2/tcard14.gif)

* Select the employee(s) you wish to send the message to. Click insert
  to send the message to additional employees.

![](images_2/msg11.gif)

* Click OK to send the message.

![](images_2/tcard17.gif)

# Sending a Note from the Employee Module

* Click on Employee.

![](images_2/empm13.gif)

* Click on Message.

![](images_2/msg13.gif)

* Enter a description for your message. This is similar to the subject
  of an email.

![](images_2/msg9.gif)

* Enter the message you wish to send to your supervisor in the Message
  Field.

![](images_2/tcard14.gif)

* Select the employee(s) you wish to send the message to. Click insert
  to send the message to additional employees.

![](images_2/msg11.gif)

* Click OK to send the message.

![](images_2/tcard17.gif)

# Sending a Schedule Change Request

Access the message table as described above within the Manager or Employee
Module.

* Click on the Outgoing Tab.

![](images_2/tcard18.gif)

* Click on Schedule Request.

![](images_2/msg28.gif)

* Enter a message description for the Schedule Change Request. This
  is similar to the subject of an email and will appear in the Incoming
  Messages table when your supervisor logs in to the Manager Module.

![](images_2/msg29.gif)

* Enter a message to accompany your request. This should explain
  the nature of the request and include any additional information required
  by your supervisor.

![](images_2/msg30.gif)

* Select a From Date. The schedule change will take effect starting
  on this date.

![](images_2/msg31.gif)

* Select a To Date. The schedule change will end on this date.

![](images_2/msg32.gif)

* Select a From Time. This is the time you will be scheduled to arrive
  at work beginning on the start date and ending on the end date.

![](images_2/msg33.gif)

* Select a To Time. This is the time you will be expected to depart
  from work beginning on the start date and ending on the end date.

![](images_2/msg34.gif)

* If 'Allow Multiple Request Recipients' is enabled the Insert Button
  will be displayed as shown below. To select additional recipients
  click on the Insert Button.

![](images_2/tcard19.jpg)

* Click OK to send the message.

# Approving a Schedule Change Request

* Highlight the Schedule Change Request in the Incoming Messages
  Table.

![](images_2/tcard20.gif)

* Click View.

![](images_2/tcard21.gif)

* Click Approve

![](images_2/msg16.gif)

* Alter the approval message if desired.

![](images_2/msg17.gif)

* Click OK to send the message.

![](images_2/msg18.gif)

* The employeeâs schedule will be altered at this time.

# Declining a Schedule Change Request

* Highlight the Schedule Change Request in the Incoming Messages
  Table.

![](images_2/tcard20.gif)

* Click View.

![](images_2/tcard21.gif)

* Click Decline.

![](images_2/msg19.gif)

* Alter the automatic decline message if desired.

![](images_2/msg20.gif)

* Click OK to send the message.

![](images_2/msg21.gif)

# Toggling the status of a Schedule Change Request

Should the supervisor change their mind after approving or denying a
schedule request they can view the original request again and toggle their
earlier decision.

If a request was previously declined, only the Approve button will be
available. If a previously denied request is approved, a message will
be sent to the employee informing them of the approval and their schedule
will be altered appropriately.

If a request was previously approved, only the Decline button will be
available. If a previously approved request is declined, a message will
be sent to the employee informing them of the change in their schedule
request status and their schedule will be returned to its original state.

# Sending a Time Off Request

* Click on Employee and then click on Time Off Request.

![](images_2/empm19.gif)

* Enter a message description for the Time Off Request. This is similar
  to the subject of an email and will be displayed in the incoming messages
  table when your supervisor logs into the Manager Module.

![](images_2/empm21.gif)

* Enter a message to accompany your request. This should explain
  the nature of the request and include any additional information required
  by your supervisor.

![](images_2/empm22.gif)

* Select a From Date. This is the start date of your vacation.

![](images_2/empm23.gif)

* Select a To Date. This is the end date of your vacation.

![](images_2/empm24.gif)

* Select a From Time. This is the start time of your vacation, which
  begins on the start date.

![](images_2/TimeOffReq2.gif)

* Select a To Time. This is the end time of your vacation, which
  occurs on the end date.

![](images_2/TimeOffReq3.png)

* If 'Allow Multiple Request Recipients' is enabled the Insert Button
  will be displayed as shown below. To select additional recipients
  click on the Insert Button.

![](images_2/TimeOffReq1.gif)

* Click OK to send the request.

# Approving a Time Off Request

* Highlight the Time Off Request in the Incoming Messages Table.

![](images_2/tcard22.gif)

* Click View.

![](images_2/tcard23.gif)

* Click Approve

![](images_2/msg24.gif)

* Choose an Other Activity type to associate the vacation time with.

![](images_2/msg26.gif)

* Alter the approval message if desired.
* Click OK to send the message.
* The employeeâs schedule will be altered and other activity entries
  will be added at this time.

*NOTE*:
As of 7.04 the Timecard Activity Table displays other activity in the
future.

# Declining a Time Off Request

* Highlight the Time Off Request in the Incoming Messages Table.

![](images_2/tcard22.gif)

* Click View.

![](images_2/tcard23.gif)

* Click Decline.

![](images_2/msg25.gif)

* Alter the automatic decline message if desired.

![](images_2/msg27.gif)

* Click OK to send the message.
* The employeeâs schedule will be altered and other activity entries
  will be added at this time.

# Toggling the Status of a Vacation Request

Should the supervisor change their mind after approving or denying a
vacation request they can view the original request again and toggle their
earlier decision.

If a request was previously declined, only the Approve button will be
available. If a previously denied request is approved, a message will
be sent to the employee informing them of the approval and their schedule
will be altered appropriately. An Other Activity entry will also be entered
for the specified vacation dates.

If a request was previously approved, only the Decline button will be
available. If a previously approved request is declined, a message will
be sent to the employee informing them of the change in their vacation
request status and their schedule will be returned to its original state.
Any other activity entries that were previously added will also be removed.

# Unread Messages

Messages can only be altered or deleted if a recipient has not read
them. Once a recipient has read a message it cannot be removed from the
InfiniTime Database. All messages are saved for archival purposes.

To
Alter an Unread Message:

* Access the message table as described above within the Manager
  or Employee Module.
* Click on the Outgoing Tab.

![](images_2/tcard18.gif)

* Highlight the message you wish to alter.

![](images_2/msg36.gif)

* Click Change. If the message is unread, InfiniTime will open the
  message and changes may be made.

![](images_2/msg37.gif)

* If the message has been read the error below will be displayed.
  Should this message be displayed the message cannot be edited.

![](images_2/msg39.gif)

To
Delete an Unread Message:

* Access the message table as described above within the Manager
  or Employee Module.
* Click on the Outgoing Tab.

![](images_2/tcard18.gif)

* Highlight the message you wish to alter.

![](images_2/msg36.gif)

* Click Delete. If the message is unread, InfiniTime
  will ask you to confirm your decision to delete the note.

![](images_2/msg40.gif)

* If the message has been read the error below will be displayed.
  Should this message be displayed the message cannot be deleted.

![](images_2/msg41.gif)

# Viewing Messages

Messages can be viewed from a few locations within the InfiniTime software. Message tables,
which display incoming and outgoing messages for the employee that is
logged in, can be found in the employee and manager module. It is also
possible to view all messages associated with an employee by opening their
employee record and viewing the messages tab.

Viewing a Message:

* Access the Message table from within the Employee Module or Manager
  Module as described in the beginning of this section.
* Click on either the Incoming or Outgoing Tab depending on the messages
  you wish to view.

![](images_2/msg42.gif)

* Highlight the message you wish to view.

![](images_2/msg43.gif)

* Click View.

![](images_2/msg44.gif)

* The message will be displayed.

![](images_2/tcard24.gif)

# Conversation: Message History

The conversation button displays a list, similar in layout to the message
table, of all messages related to the originally selected message. This
is useful for viewing a quick history of a conversation between employees.

Using
the Conversation Button

* Access the Message table from within the Employee Module or Manager
  Module as described in the beginning of this section.
* Click on either the Incoming or Outgoing Tab depending on the messages
  you wish to view.

![](images_2/msg42.gif)

* Highlight the message you wish to view.

![](images_2/msg43.gif)

* Click Conversation

![](images_2/msg46.gif)

* A list of all related messages will be displayed for viewing purposes
  only. Messages cannot be deleted or altered from the Message Conversation
  Table.

![](images_2/tcard25.gif)