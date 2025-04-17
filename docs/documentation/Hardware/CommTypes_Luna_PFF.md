---
title: "Luna: Poll From File"
description: "Guide on using the Poll From File feature to gather punches via thumb drive without direct connection to InfiniTime Server."
---

# Luna: Poll From File

Poll from file makes it possible to gather punches from a remote site with a thumb drive which eliminates the need for a direct or Ethernet connection between the reader and the InfiniTime Server. Punches can be downloaded from the clock and stored in a text file on a thumb drive, which can be sent via email to an individual with access to the InfiniTime Software. When using the poll from file feature there are a few things to keep in mind. Additional information on the configuration and use of Poll From File is available in the [Luna Reader Setup: Poll From File](Luna_PFF_Config.md) section of this document.

- It is important to understand that there is no communication between the Luna Terminal and the InfiniTime software when Poll From File is being used. Employees must be manually added, removed, updated, and managed on the Luna Terminal itself.

- If department switching or other activity entry is desired the clock must be connected to the InfiniTime Software in order to perform an update. Other Activity Entries and Department information is passed through the normal Poll From File Process but it is not possible to enter Departments or Other Activity Types manually at the clock.

- In an Ethernet or direct connect environment InfiniTime is responsible for updating the time on the clock. Poll From File clocks must be updated manually or configured for use with daylight savings time.

- Downloading Punches from the clock does not delete punches from the clock
