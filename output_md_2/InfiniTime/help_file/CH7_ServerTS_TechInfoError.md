xml version="1.0" encoding="utf-8"?





Script Errors When Clicking on the Technical Info Button




# Script Errors When Clicking on the Technical Info Button

Some customer's may receive an Object Error when attempting to click on the Technical Info Button to check their Timewolf License Information and / or Activate their software license.

 Steps to Reproduce

 1. Login to the TimeWolf Manager Module

2. Click on Help - About Timewolf

3. Click on the Technical Info. Button

4. An Error Occurs

Possible Causes and Resolutions

 TimeWolf is unable to access registry keys added by the TimeWolf installation. This prevents Timewolf from properly displaying the Technical Information window. This issue may be caused by the following:

* ASPNET Registry permissions are improperly configured or were altered. ASPNET requires Full Control to the following Registry Keys:

 For 64-Bit Platforms:

 HKEY\_LOCAL\_MACHINE\SOFTWARE\Wow6432Node\Lone Wolf Software\

 HKEY\_LOCAL\_MACHINE\SOFTWARE\Wow6432Node\Lone Wolf Software, Inc.\

 HKEY\_LOCAL\_MACHINE\SOFTWARE\Wow6432Node\ORACLE\

 For 32-Bit Platforms:

 HKEY\_LOCAL\_MACHINE\SOFTWARE\Lone Wolf Software\

 HKEY\_LOCAL\_MACHINE\SOFTWARE\Lone Wolf Software, Inc.\

 HKEY\_LOCAL\_MACHINE\SOFTWARE\ORACLE\

* The TimeWolf Server Operating System was upgraded from a Home Version to the Business or Professional Version. This can cause instability with the Windows Registry. Please perform a fresh installation of the Business or Professional Version of your TimeWolf Server's Operating System.