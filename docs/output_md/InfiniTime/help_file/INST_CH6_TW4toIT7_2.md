xml version="1.0" encoding="utf-8"?





Verify Backup Integrity




# Verify Backup Integrity

In order to verify the integrity of the previously created backup, make a change to the TimeWolf 4 database by adding an employee or adding activity to an employee. Afterwards, restore the previously created backup and verify the change is no longer present. This will allow you to confirm the backup was created properly.

1. Log into the TimeWolf Manager Module.

2. Click on File, then Click on Backup / Restore.

![](/img/image-404.png)

3. Highlight the backup you wish to restore by Clicking on it.

![](/img/image-404.png)

4. Click Restore. It should be noted that all users must be out of the TimeWolf software in order to restore the backup. If there are users logged into the software a warning will be displayed and the restore will be aborted. If you receive this error users can be kicked out of the software by restarting the OracleServiceTCDBS service.

![](/img/image-404.png)

5. No further action is required from the user, TimeWolf will automatically perform all necessary operations to restore the backup file.

Close the backup window and verify that the change is no longer in the database. For example, the employee you added before restoring the backup would no longer appear in the employee table. Or the activity you added would no longer be listed under an employeeâs activity table. This is because the backup was taken before the change was made. Therefore the database restored from the backup file would not have the change.

If you were able to verify the changes made after taking the backup were absent from your system then you have successfully restored the backup. This confirms the backup file is not corrupted and can be used to upgrade to InfiniTime 7.