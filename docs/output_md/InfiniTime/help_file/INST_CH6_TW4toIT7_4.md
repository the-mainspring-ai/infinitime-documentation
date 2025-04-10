xml version="1.0" encoding="utf-8"?





Restore Timewolf 4 Backup




# Restore Timewolf 4 Backup

Place the TimeWolf 4 Backup in the InfiniTime 7 Backup Folder

The InfiniTime 7 Backup Folder is C:\Inception\InfiniTime\InfiniTime7\Backup\ by default, though the location may be different if InfiniTime 7 was not installed with the default Program File and Data File Locations. Before the TimeWolf 4 Backup can be restored in InfiniTime 7, it must be placed in the InfiniTime 7 Backup Folder.

1. Locate the previously created TimeWolf 4 Backup File using Windows Explorer.
2. Click on Start
3. Click on Run
4. Enter C:\Inception\InfiniTime\InfiniTime7\Backup\ and click OK to open the InfiniTime 7 Backup Folder.
5. Copy the TimeWolf 4 Backup File to the InfiniTime 7 Backup Folder.

Restore the TimeWolf 4 Backup File

1. Login to the InfiniTime Manager Module then Click on File.
2. Click on Backup / Restore.

![](/img/rb5.gif)

3. Highlight the TimeWolf 4 Backup File by clicking on it. Note that TimeWolf 4 Backup files have an extension of .TCB as shown in the image below.

![](/img/rb1.gif)

4. Click Restore. It should be noted that all users must be out of the InfiniTime software in order to restore the backup. If there are users logged into the software a warning will be displayed and the restore will be aborted. If you receive this error users can be kicked out of the software by restarting the OracleServiceTCDBS service. The InfiniTimeHousekeepingService must also be stopped before performing a restore.

![](/img/CH6_TW4toIT7_BackupFile.gif)

5. No further action is required from the user, InfiniTime will automatically perform all necessary operations to restore the backup file.
6. InfiniTime will automatically backup the data currently in the InfiniTime software before restoring the backup.

![](/img/rb4.gif)

7. Once the backup is finished InfiniTime will restore the previously selected backup file.

![](/img/rb5.gif)

8. The above window will close automatically when the restore is complete.