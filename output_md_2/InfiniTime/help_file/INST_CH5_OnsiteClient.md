xml version="1.0" encoding="utf-8" ?





InfiniTime 7.0 Server with On-Site Clients




# InfiniTime 7.0 Server with On-Site Clients

When accessing the InfiniTime
7.0 software from on-site Clients or Client machines on the Local Area
Network the serverâs hostname or IP address can be used. This directs
the browser to a specific machine in order to access the website.

Utilizing the Server's Hostname

Replace âhostnameâ in the addresses with the actual hostname of your
server in order to access the InfiniTime
7.0 Software.

| Module Name | Address |
| InfiniTime 7.0 Manager Module | http://hostname/InfiniTimeManagerModule/ |
| InfiniTime 7.0 Employee Module | http://hostname/InfiniTimeEmployeeModule/ |
| InfiniTime 7.0 Escort | http://hostname/InfiniTimeEscort/ |
| InfiniTime 7.0 Punch Module | http://hostname/InfiniTimePunch/ |

Obtaining the hostname from your InfiniTime 7.0 Server:

*Technical Note:* These steps
must be performed on the InfiniTime
7.0 Server.

Click on Start.

![](images_2/startbar.JPG)

Click on Run.

![](images_2/startrun.JPG)

Type cmd into the dialog box.

![](images_2/runboxCMD.jpg)

Click OK.

A dos window will open. Type hostname.

![](images_2/CMDHOSTNAME.gif)

Hit Enter

The hostname of your computer will be displayed. Dellsupport is the
hostname in the example.

Replace âhostnameâ in the addresses above with the hostname of your
InfiniTime 7.0 Server.
Using the hostname from the example above the addresses to access the
InfiniTime 7.0 software
would be:

| Module Name | Address |
| InfiniTime 7.0 Manager Module | http://Dellsupport/InfiniTimeManagerModule/ |
| InfiniTime 7.0 Employee Module | http://Dellsupport/InfiniTimeEmployeeModule/ |
| InfiniTime 7.0 Escort | http://Dellsupport/InfiniTimeEscort/ |
| InfiniTime 7.0 Punch Module | http://Dellsupport/InfiniTimePunch/ |

Technical Note: While these screenshots were taken
on Windows XP these steps are identical regardless of the operating system
in use.

Utilizing the Server's IP Address

Replace â192.168.0.2â with your serverâs
local IP address in order to access the InfiniTime
7.0 Software. This is only recommended if the server has a static ip address.

http://192.168.0.2/InfiniTimeManagerModule/
InfiniTime 7.0 Manager
Module

http://192.168.0.2/InfiniTimeEmployeeModule/
InfiniTime 7.0 Employee
Module

http://192.168.0.2/InfiniTimeEscort/
InfiniTime 7.0 Escort

http://192.168.0.2/InfiniTimePunch/
InfiniTime 7.0 Punch

Technical Note:
Every computer on a given network must have a unique IP Address in order
for computers on the network to communicate properly. In order for a computer
to function properly as a server it must be readily accessible to Client
machines at a known location. This is accomplished by assigning a Static,
or unchanging, IP Address to the server machine. If a server is not assigned
a Static ip address it will eventually acquire a different address through
Dynamic Host Configuration Protocol. This will cause the server to be
unreachable from Client machines, assuming the IP address is being used
to access the server.

To obtain the local IP address of the InfiniTime 7.0 Server:

*Technical
Note:* These steps must be performed on the InfiniTime
7.0 Server.

Click on Start.

![](images_2/image435.gif)

Click on Run.

![](images_2/image436.gif)

Type cmd into the dialog box.

![](images_2/image437.gif)

Click OK.

A dos window will open. Type ipconfig /all

![](images_2/image438.gif)

Hit enter. The network configuration of
your server will be displayed.

The InfiniTime
7.0 Server should have a static IP address. The results below indicate
a static address of 192.168.1.40 with DHCP disabled.

![](images_2/image439.gif)

Replacing â192.168.0.2â With the static
address in the example above the addresses for accessing the InfiniTime
7.0 Software would be:

http://192.168.1.40/InfiniTimeManagerModule/
  InfiniTime
7.0 Manager Module

http://192.168.1.40/InfiniTimeEmployeeModule/
InfiniTime 7.0 Employee
Module

http://192.168.1.40/InfiniTimeEscort/
  InfiniTime
7.0 Escort

http://192.168.1.40/InfiniTimePunch/
  InfiniTime
7.0 Punch

The results below show DHCP enabled. The
server should be configured with a static ip address in order to access
the InfiniTime 7.0 software
with the Serverâs IP address. Refer to the technical note before this
section for more information.

![](images_2/image440.gif)