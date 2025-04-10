xml version="1.0" encoding="utf-8"?





Configuring and Using Poll From File




# Configuring and Using Poll From File

It is important to understand that a reader configured to poll from a file will not automatically poll punches into the database. The user must manually download punches from the Luna terminal, transfer the file to a location with access to the InfiniTime Software, and manually poll the file to bring Employee Punches into the InfiniTime Database. A general procedure has been established to assist with the process of downloading punches from the Luna Terminal.

1.) A supervisor with access to the Luna's Administrator Menu must be present at the clock.

2.) Users should be instructed to stop punching until all punches have been polled into the InfiniTime database.

3.) Punches should be downloaded from the clock to a USB Thumb drive. A Mini-USB to USB cable, provided with the Luna Reader, is required.

4.) A Luna clock must be configured within the InfiniTime Software as Poll From File.

5.) Poll Punches from the file into the InfiniTime Database.

6.) Verify the presence of timecard activity for employees within the InfiniTime Database.

7.) Delete the punches from the Luna clock.

8.) At this point users may resume punching.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

1.) Employees Must have Administrative Access to the Reader in order to download punches to a thumb drive.

1. If a supervisor is having difficulties accessing the Menu on the Luna Reader ensure they are assigned to a security role with permission to be a 'Supervisor In Readers.' Refer to Chapter 2: Security Roles for additional information.
2. Verify the supervisor is assigned to the clock by checking the Employee's assigned to the clock.
3. Verify the supervisor's Login ID and Password are numeric. Employees with alphanumeric IDs or Passwords will not be updated to the Luna Terminal.
4. If the supervisor was enrolled at the reader they must be enrolled with Admin security privileges. Refer to [Enrolling Employees as an Administrator](/InfiniTime/help%20file/Enrolling_an_Administrator.md) for more information.

2.) Users should be instructed to stop punching until all punches have been polled into the InfiniTime database.

1. Once punches have been downloaded from the Luna Terminal it is important for users to refrain from punching until all punches have been polled into the system. It is important to understand that employee punches are NOT DELETED from the Luna Terminal when they are downloaded to a USB Thumb Drive. This prevents data loss should the Thumb Drive become lost or damaged.  By discouraging users from punching while activity is being polled into the InfiniTime software the possibility of deleting punches from the Luna which have not been transferred to the InfiniTime server is eliminated.

3.) Punches should be downloaded from the Luna clock to a USB Thumb Drive. A Mini-USB to USB cable is required.

1. Plug the gray Mini-USB Cable, provided with the Luna Terminal, into the mini USB port on the bottom of the Luna.
2. Plug a USB Thumb drive into the USB side of the Mini-USB cable.
3. Press the Menu button on the Luna Terminal. If an administrator is present in the clock the user will be prompted to enter their ID and Password before the menu will be displayed.

![](images_2/PFF_7.gif)

4. Use the down arrow to select USB Drive Mng from the Main Menu and press OK.

![](images_2/PFF_8.gif)

5. Use the down arrow to select Download AttLog from the menu and press OK.

![](images_2/PFF_9.gif)

6. Press OK to confirm.

![](images_2/PFF_10.gif)

7. Plug the USB Thumb drive into an available USB port on a PC.

8. A file name extlog.txt should be present on the USB Thumb drive. If this file is not present the Luna terminal does not have the latest BIOS and must be updated. The BIOS can be updated by connecting the Luna Terminal to the InfiniTime Software and performing an Update All or by uploading the bios to the Luna through USB. Refer to [Updating the Luna BIOS via USB](/InfiniTime/help%20file/Luna_UpdateBFF.md) for more information.

9. Copy the file extlog.txt to a computer with access to the InfiniTime 7 Software Application.

10. Continue to Step 4.

4.) A Luna Reader must be configured for Poll From File within the InfiniTime 7 Software.

To configure a Luna Reader for Poll From File:

1. Click on Lookups, Click on Reader Configuration.

![](images_2/PFF_1.gif)

2. Click on Insert.

![](images_2/PFF_2.gif)

3. Type a Port Name, Set the Reader Type to Luna, and Choose File for the Port as shown below.

![](images_2/Luna_PFF_Screen1.gif)

4. Click on the Reader Address Tab and Click insert.

![](images_2/PFF_5.gif)

5. The Reader Address Update form will be displayed. Ensure the inactive box is not checked and type a description for the clock.

![](images_2/PFF_4.gif)

6. The Reader Configuration Table should appear similar to the image below. If your company has additional readers they will also be displayed.

![](images_2/PFF_6.gif)

5.) Poll punches into the InfiniTime Database.

To Poll Punches from the retrieved file:

1. Login to the Manager Module.

2. Click on Tools, Clock Tools, System Monitor.

![](images_2/PFF_11.gif)

3. Highlight the Luna Reader that is set to poll from file within the list of readers.

![](images_2/PFF_12.gif)

4. Click on Force Poll.

5. Browse to and select the extlog.txt file that was retrieved from the Luna Terminal.

![](images_2/PFF_13.gif)

6. Click OK. The punches will be polled from the file automatically.

Technical Note: The InfiniTime Housekeeping service must be started for punches to be polled from extlog.txt It is important to understand how the service operates when polling from a file. The InfiniTime Housekeeping service operates in a round robin manner. Each clock that is configured within the system will be checked to see if polling or an update is required. The service proceeds in an alphabetical order through all clocks within the database before restarting at the beginning. Because of this round robin procedure it may take a few minutes before timecard activity is polled into the database from a file depending on the number of clocks configured within the InfiniTime Software.

6.) Verify timecard activity is present for employees.

To verify timecard activity is present within the InfiniTime Database:

1. Click on Tools, Clock Tools, Polled Information.

![](images_2/PFF_14.gif)

2. Type the description of the reader used to Poll from File in the Search Box.

![](images_2/PFF_15.gif)

3. Click Search.

4. All punches that have been polled from that reader will be displayed.

![](images_2/PFF_16.gif)

5. Ensure all expected punches are displayed in the polled information table.

7.)  Delete punches from the Luna Terminal.

1. Press the Menu button on the Luna Terminal. If an administrator is present in the clock the user will be prompted to enter their ID and Password before the menu will be displayed.

![](images_2/ZephyrTS1.gif)

2. Use the down arrow to move down to Options and press OK.

![](images_2/ZephyrTS9.gif)

3. Ensure System Opt. is highlighted and press OK.

![](images_2/ZephyrTS10.gif)

4. Use the down arrow to move down to Adv Option and press OK.

![](images_2/ZephyrTS11.gif)

5. Use the down arrow to move down to Del AttLogs and press OK.

![](images_2/ZephyrTS17.gif)

6. Press OK to confirm.

8.) Users may now continue punching as normal.