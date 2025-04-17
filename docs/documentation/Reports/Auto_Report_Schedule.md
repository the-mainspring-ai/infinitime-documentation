---
title: "Auto Report Schedule Configuration"
description: "Guide to setting up and managing automated report schedules in InfiniTime, including creation, modification, and deletion of report schedules with email and printing options."
---

Auto Report Schedule

# Auto Report Schedule

![](/img/rep9.gif)

InfiniTime allows a schedule to be configured in order to run reports automatically. Reports are automatically emailed or printed depending on the configuration.  Settings must be saved for a report before it can be configured to run automatically.

Note: The InfiniTimeHouseKeeping service must be running in order for reports to print automatically.

Insert â Click insert to open up the Auto Report Schedule Update Form and set a schedule.

Change â Click change to make any adjustments to a previously configured schedule.

Delete â Click delete to remove the highlighted Report Schedule.

![](/img/ValidPrinter.gif)

Description â Describes the Report Schedule you are creating.  This name will appear in the Report Library Update Form.  This is how you will be able to distinguish between other Auto Report Schedules you may create.

Printer - Infinitime uses printer drivers to prepare reports for proper display on your computer. Select a printer that is installed and attached to your machine. Do not select an image printer. The warning below will be displayed when saving the Auto Report Schedule. Reports without a valid printer may not print or display properly.

![](/img/CH10AutoReports.gif)

Frequency â This is how often the program will run the auto report schedule feature.  The options are: Once, Daily, Weekly, and Monthly.

Do Not Print - The Do Not Print check box is only displayed when a report is configured to be sent to a remote party via email or FTP. Reports will be printed according to the automatic report schedule by default. This box should be checked if you wish to email or send a report via FTP without printing the report.

Date to Print â This is the date that you want the system to print the current set up on.

Time to Print â This is the time that you want the system to print the current set up on the date selected above.

Day of Week to Print â Select the day of week you wish for the system to print the structure on.

Date Last Printed â Tells you the last date the system automatically printed the structure.

Time Last Printed â Tells you the last time on the date above the system automatically printed the structure.

Date to Print Next â The date entered here will be the next future date that the system will automatically print a saved structure.

### Auto Report Requirements

InfiniTime can be configured to automatically email or print reports, payroll exports, and exports with saved criteria. A list of requirements and items that are known to interfere with the intended processing of auto reports can be found below. Each requirement must be met for auto reports to function as intended.

It should also be noted that saved report settings configured with an email address will only be emailed according to the settings on the auto report schedule and email tabs. They will not be printed automatically. A single saved report setting cannot be used to automatically email and print a report. Seperate saved settings must be configured. Your network administrator may need to assist you with configuring the following items.

To automatically email a report the following criteria must be observed:

- The InfiniTime Server must have an active Internet connection.
- Power Management must be disabled on the Network Interface Card of the InfiniTime Server.
- The InfiniTime Housekeeping Service must be started and running.
- The InfiniTime Server does not need to have a user logged into the console. However, it must at least be powered on and idle at the Windows Login Splash Screen.
- A printer must be installed on the InfiniTime Server.
- A printer must be set as the default printer.
- The Print Spooler Service must be started and running on the InfiniTime Server.
- Your fully qualified domain name may need to be configured in the advanced delivery options of the SMTP Virtual Server created by InfiniTime depending on your domain policies.
- An auto schedule must be configured within a saved report setting.
- A destination name and email address must be defined on the email tab of the saved report setting.
- The server must be granted permissions to relay email through the SMTP Virtual Server installed by InfiniTime.

- Depending on your network configuration and domain settings it may be necessary to forward all outgoing email messages from the InfiniTime SMTP Virtual Server to a Smart Host. Generally the Smart Host will be a server running exchange on your local network. The smart host can be configured under Advanced Options of Delivery tab for the InfiniTime SMTP Virtual Server Properties.

To automatically print a report the following criteria must be observed:

- The InfiniTime Server must have an active Internet or Local Area Network connection if the destination printer is not directly connected to the InfiniTime Server.
- Power Management must be disabled on the Network Interface Card of the InfiniTime Server if the destination printer is not directly connected to the InfiniTime server.
- The InfiniTime Housekeeping Service must be started and running.
- The InfiniTime Server does not need to have a user logged into the console. However, it must atleast be powered on and idle at the Windows Login Splash Screen.
- A printer must be installed on the InfiniTime Server.
- A printer must be set as the default printer.
- The Print Spooler Service must be started and running on the InfiniTime Server.
- An auto schedule must be configured within a saved report setting.
