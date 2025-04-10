xml version="1.0" encoding="utf-8"?





InfiniTime 7.0 Registry Keys




# InfiniTime 7.0 Registry Keys

InfiniTime 7.0 includes various registry keys for troubleshooting purposes. InfiniTime registry keys should only be altered by authorized personnel. Always take a backup of the registry before altering the following values.

Accessing the InfiniTime Registry Keys

1. Click Start

![](/img/clickstart.gif)

2. Click Run

![](/img/regedit3.gif)

3. Type regedit

![](/img/clickrun.gif)

4. Click OK

5. Expand HKEY\_LOCAL\_MACHINE

![](/img/regedit6.gif)

6. Expand Software

![](/img/regedit2.gif)

7. Expand Inception Technologies

![](/img/regedit4.gif)

8. Expand InfiniTime

![](/img/regedit6.gif)

9. Click on 7.0

![](/img/regedit1.gif)

| Registry Key | Settings | Description |
| Clear Reader Memory | True or False | Set to False by default. Setting this key to true will cause a reader's memory to be cleared at the next data update. Perform the data update manually as soon as possible and return this setting to its original value. |
| Data File Location | Local Path: Set during Installation | Set to C:\Inception\InfiniTime\Data by default during the installation. May be changed according to user's discretion. Do not alter this path after installation. |
| Delete Biometric Information | True or False | Set to False by default. Setting this key to true will cause all biometric information to be cleared from a reader at the next data update. Perform the data update manually as soon as possible and return this setting to its original value. |
| Delete Reports | True or False | Set to False by default. Setting this key to true will cause all biometric information to be cleared from a reader at the next data update. Perform the data update manually as soon as possible and return this setting to its original value. |
| Display Synel Upload Status Information | True or False | Set to False by default. Changing this key to true will display the status of the program update while Synel Terminals are being updated. |
| Hardware ID Only | True or False | Set to False by default. Changing this key to True will cause InfiniTime to use an alternate algorithm to generate the Hardware ID. The Hardware ID is used for licensing and activation purposes. This value should only be set to True if the default Hardware ID algorithm results in inconsistent activation for your InfiniTime Installation due to your server hardware. |
| Product Version | Product Version: Set during Installation or Update. | Displays the version of InfiniTime currently installed on your system. Do not alter. |
| Program File Location | Local Path: Set during Installation | Set to C:\Inception\InfiniTime by default during the installation. May be changed according to user's discretion. Do not alter this path after installation. |
| Show Help File ID | True or False | Set to False by default. Changing this key to true will display information regarding Help File ID numbers. Internal Use Only. Do not alter. |
| Synel Debug File Name | Local Path: Text File | Left blank by default. Supplying a local path to a text file will log information regarding the program update for Synel readers. |
| Thread Reader Polling | True or False | Set to True by default. InfiniTime 7.0 polls readers in parallel rather than in series. To cause InfiniTime 7.0 to poll readers in series set this value to False. |