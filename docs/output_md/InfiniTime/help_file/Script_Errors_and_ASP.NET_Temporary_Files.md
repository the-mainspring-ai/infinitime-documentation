xml version="1.0" encoding="utf-8"?





Script Errors and ASP.NET Temporary Files




# Script Errors and ASP.NET Temporary Files

ASP.NET Temporary files are compiled when an ASP.NET Application is accessed for the first time. Over time, as software updates are applied or due to third party applications, these files may become outdated or altered from their original form. These unexpected changes within the temporary files are a common cause of script errors within the InfiniTime 7 Application. To resolve this issue it is necessary to delete the ASP.NET Temporary Files. Please follow the procedure below to clear ASP.NET temporary files.

1. Before proceeding with the steps below ensure the InfiniTime Software is closed. Please be aware that any open sessions to the InfiniTime Application will be disconnected when the ASP.NET worker process is ended. It is recommended that your Network Administrator or IT Personnel perform the steps below if you have web sites other than the InfiniTime Software hosted on the InfiniTime Server.
2. Locate 'My Computer' within the start menu or on the desktop and right click on it. Click on Manage.
3. Click on Services.
4. Locate the InfiniTimeHouseKeepingService and click on the record to highlight it.
5. Click on the Stop button to stop the service.
6. Open Task Manager by right click on the start bar and clicking on task manager.
7. Locate ASPNET\_WP.EXE (Windows XP & Windows 2000) or W3WP.EXE (Windows 2003) and highlight it.
8. Click on End Task.
9. Right Click on Start and click on Explore.
11. Delete ASP.NET Temporary Files for InfiniTime