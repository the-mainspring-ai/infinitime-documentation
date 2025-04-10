xml version="1.0" encoding="utf-8"?





Configuring a Poll From File Clock




# Configuring and Using Poll From File

It is important to understand that a reader configured to poll from a file will not automatically poll punches into the database. The user must manually download punches from the terminal, transfer the file to a location with access to the InfiniTime Software, and manually poll the file to bring Employee Punches into the InfiniTime Database. A general procedure has been established to assist with the process of downloading punches from the terminal.

1.) A supervisor with access to the Menu must be present at the clock.

2.) Users should be instructed to stop punching until all punches have been polled into the InfiniTime database.

3.) Punches should be downloaded from the clock to a USB Thumb drive. A Mini-USB to USB cable, provided with the reader, is required.

4.) A clock must be configured within the InfiniTime Software as Poll From File for the appropriate model. IE: For Luna Terminals a Luna must be configured for Poll from File in the Reader Configuration Table.

5.) Poll Punches from the file into the InfiniTime Database.

6.) Verify the presence of timecard activity for employees within the InfiniTime Database.

7.) Delete the punches from the clock via Delete ATT Logs.

8.) At this point users may resume punching.

NOTE: It is important to verify employee activity is present within the InfiniTime Database before clearing punches off of the reader!

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

1.) Employees Must have Administrative Access to the Reader in order to download punches to a thumb drive.

1. If a supervisor is having difficulties accessing the Menu on the reader ensure they are assigned to a security role with permission to be a 'Supervisor In Readers.' Refer to Chapter 2: Security Roles for additional information.
2. Verify the supervisor is assigned to the clock by checking the Employee's assigned to the clock.
3. Verify the supervisor's Login ID and Password are numeric. Employees with alphanumeric IDs or Passwords will not be updated to the Zephyr Terminal.
4. If the supervisor was enrolled at the reader they must be enrolled with Admin security privileges. Refer to [Enrolling Employees as an Administrator](Enrolling_an_Administrator.md) for more information.

2.) Users should be instructed to stop punching until all punches have been polled into the InfiniTime database.

1. Once punches have been downloaded from the terminal it is important for users to refrain from punching until all punches have been polled into the system. It is important to understand that employee punches are NOT DELETED from the terminal when they are downloaded to a USB Thumb Drive. This prevents data loss should the Thumb Drive become lost or damaged.  By discouraging users from punching while activity is being polled into the InfiniTime software the possibility of deleting punches from the terminal which have not been transferred to the InfiniTime server is eliminated.

3.) Punches should be downloaded from the terminal  to a USB Thumb Drive. A Mini-USB to USB cable is required.

1. Plug the gray Mini-USB Cable, provided with the terminal, into the mini USB port on the bottom or side of the terminal. The position of the Mini-USB port differs from terminal to terminal. Refer to the physical description of your specific model for the location of the Mini-USB port.
2. Plug a USB Thumb drive into the USB side of the Mini-USB cable.
3. Press the Menu button on the terminal. If an administrator is present in the clock the user will be prompted to enter their ID and Password before the menu will be displayed.

![](/img/image-404.png)

4. Use the down arrow to select USB Drive Mng from the Main Menu and press OK.

![](/img/image-404.png)

5. Use the down arrow to select Download AttLog from the menu and press OK.

![](/img/image-404.png)

6. Press OK to confirm.

![](/img/image-404.png)

7. Plug the USB Thumb drive into an available USB port on a PC.

8. A file name extlog.txt should be present on the USB Thumb drive. If this file is not present the terminal does not have the latest BIOS and must be updated. The BIOS can be updated by connecting the terminal to the InfiniTime Software and performing an Update All or by uploading the bios to the terminal through USB. Refer to [Updating the BIOS via USB](Zephyr_UpdateBFF.md) for more information.

9. Copy the file extlog.txt to a computer with access to the InfiniTime 7 Software Application.

10. Continue to Step 4.

4.) A  Reader of the appropriate model must be configured for Poll From File within the InfiniTime 7 Software. The steps below show how to insert a Zephyr Reader. To insert a different model simply choose the appropriate clock type.

To configure a  Reader for Poll From File:

1. Click on Lookups, Click on Reader Configuration.

![](/img/image-404.png)

2. Click on Insert.

![](/img/image-404.png)

3. Type a Port Name, Set the Reader Type as appropriate, and Choose File for the Port as shown below.

![](/img/image-404.png)

4. Click on the Reader Address Tab and Click insert.

![](/img/image-404.png)

5. The Reader Address Update form will be displayed. Ensure the inactive box is not checked and type a description for the clock.

![](/img/image-404.png)

6. The Reader Configuration Table should appear similar to the image below. If your company has additional readers they will also be displayed.

![](/img/image-404.png)

5.) Poll punches into the InfiniTime Database.

To Poll Punches from the retrieved file:

1. Login to the Manager Module.

2. Click on Tools, Clock Tools, System Monitor.

![](/img/image-404.png)

3. Highlight the reader that is set to poll from file within the list of readers.

![](/img/image-404.png)

4. Click on Force Poll.

5. Browse to and select the extlog.txt file that was retrieved from the Zephyr Terminal.

![](/img/image-404.png)

6. Click OK. The punches will be polled from the file automatically.

Technical Note: The InfiniTime Housekeeping service must be started for punches to be polled from extlog.txt It is important to understand how the service operates when polling from a file. The InfiniTime Housekeeping service operates in a round robin manner. Each clock that is configured within the system will be checked to see if polling or an update is required. The service proceeds in an alphabetical order through all clocks within the database before restarting at the beginning. Because of this round robin procedure it may take a few minutes before timecard activity is polled into the database from a file depending on the number of clocks configured within the InfiniTime Software.

6.) Verify timecard activity is present for employees.

To verify timecard activity is present within the InfiniTime Database:

1. Click on Tools, Clock Tools, Polled Information.

![](/img/image-404.png)

2. Type the description of the reader used to Poll from File in the Search Box.

![](/img/image-404.png)

3. Click Search.

4. All punches that have been polled from that reader will be displayed.

![](/img/image-404.png)

5. Ensure all expected punches are displayed in the polled information table.

7.)  Delete punches from the terminal.

1. Press the Menu button on the terminal. If an administrator is present in the clock the user will be prompted to enter their ID and Password before the menu will be displayed.

![](/img/image-404.png)

2. Use the down arrow to move down to Options and press OK.

![](/img/image-404.png)

3. Ensure System Opt. is highlighted and press OK.

![](/img/image-404.png)

4. Use the down arrow to move down to Adv Option and press OK.

![](/img/image-404.png)

5. Use the down arrow to move down to Del AttLogs and press OK.

![](/img/image-404.png)

6. Press OK to confirm.

8.) Users may now continue punching as normal.