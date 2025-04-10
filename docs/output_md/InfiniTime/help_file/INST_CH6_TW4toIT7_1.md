xml version="1.0" encoding="utf-8"?





Obtain a Timewolf 4 Backup




# Obtain a Timewolf 4 Backup

The upgrade process allows a user to move their InfiniTime or Timewolf data to the InfiniTime 7.0 software. This saves data entry time and allows the customer to minimize downtime while transitioning from one product to another. A backup from the previous product, in this case TimeWolf 4, is required before upgrading.

Technical Note: Do not uninstall TimeWolf 4 until you have verified that your backup is in working order. Without a functional backup or an active database with your information there is no way to recover your TimeWolf Data.

Stop and Disable the TimeWolf Housekeeping Service:

The TimeWolf Housekeeping service polls employee punches from hardware terminals. To ensure employee punches are not lost, the TimeWolf Housekeeping Service must be stopped before backing up TimeWolf's Data. Similarly, the TimeWolf Housekeeping Service must remain stopped after the backup is taken to ensure all employee punches remain on the Time and Attendance Hardware terminals.

1. Right Click on My Computer.

2. Select "Manage" from the pop up menu that appears.

3. Once in the Computer Management screen, Select "Services And Applications".

4. Once under Services and Applications select "Services"

5. Once in Services locate "TimeWolfHouseKeepingService"

6. Highlight the service, once highlighted a prompt should display to the left of the services allowing you to Start, Stop, or Restart the service. Click Stop to stop the TimeWolf Housekeeping Service.

7. Right click on "TimeWolfHousekeepingService" and select "Properties".

8. Change the Startup Type Drop down to 'Disabled'.

9. Click OK to save the changes.

Disabling the TimeWolf Housekeeping Service ensures the service cannot be accidentally started causing employee punches to be polled from Time and Attendance terminals. Please note, if punches should be inadvertently polled from Time and Attendance terminals another backup should be taken for restoration within InfiniTime.

Obtain an TimeWolf 4 backup:

1. Open the Manager module on the server and hover your mouse over âFileâ
2. Click on âBackup/Restoreâ.

![](/img/SFT_CH3_Backup_02.gif)

3. A new window as pictured below entitled âBackup/Restore Tableâ will open. Click on the âBackupâ button at the bottom as shown to start the backup.

![](/img/SFT_CH3_Backup_01.gif)

4. When you click on âBackupâ the process begins and youâre screen will look like the picture below.

![](/img/SFT_CH3_Backup_03.gif)

5. After the Command Prompt is terminated, the âCreating Backupâ window will remain until the backup is complete.

![](/img/SFT_CH3_Backup_03.gif)

6. After the backup finishes the âBackup/Restore Tableâ will return to the foreground.  Identify the backup file with the current date. This is the backup that will be restored within InfiniTime 7.

![](/img/SFT_CH3_Backup_02.gif)

Move the TimeWolf 4 Backup to a Safe Location:

1. By default, TimeWolf Backup Files are stored in C:\LoneWolf\TimeWolf\TimeWolf4\Backup\ though the backup location may be different if a different path was specified during installation.
2. Click on Start
3. Click on Run
4. Enter the TimeWolf Backup Location as shown, or browse to the location of your TimeWolf Backup Files if you used a different path during installation.
5. Locate the Backup File with a current date. Copy the backup file to a safe location, such as a USB Flash Drive or an external Hard Drive. The backup file will be needed after InfiniTime 7 is installed.