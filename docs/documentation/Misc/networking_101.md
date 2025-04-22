A list of frequently asked questions regarding the use and Configuration
of Valid IP Addresses is listed below.

- What is an IP Address?
- How do I locate and determine if the Private IP Address for a machine
  on my local area network is static?
- How do I locate and determine if the Public IP Address for a machine
  at a remote location is static?
- Why would I want to configure Valid IP Addresses?
- What information should I have available before attempting to configure
  Valid IP Addresses?
- What is the difference between Company Wide Valid IP Addresses
  and Employee Specific Valid IP Addresses and why would I choose to
  use one over the other?
- What is the proper way to grant access to all computers or hosts
  on a given subnet or network address?

#### What is an IP Address?

An IP Address is a unique numeric identifier for a specific computer
or device, commonly referred to as a host, that is connected to the internet
or a local area network. An IP Address can be thought of as something
similar to a telephone number. They provide a way for other hosts or devices
to communicate with or contact you. An IP Address is considered either
public or private.

Private IP Addresses are only used internally within an office, home,
or enterprise network. They are not known on the internet and cannot be
used to communicate with other computers online. Private IP Addresses
are assigned by your network administrator or dynamically assigned by
a DHCP server. Dynamic Host Configuration Protocol (DHCP) refers to a
set of rules used by a communication device to obtain Internet Addresses
from a server. The Dynamic Host Configuration Protocol server keeps a
list of addresses available for assignment and assigns them to network
devices or hosts as needed.

Public IP Addresses are used to communicate on the internet and are
made known to other hosts or devices. Public IP Addresses are assigned
by your Internet Service Provider.

IP Addresses, both Public and Private, can be either static or dynamically
assigned. Every time you connect to the internet your ISP will assign
you a Public IP Address. If this Public IP Address is the same every time
you connect to the internet then it is a Static IP Address. The ISP has
reserved this address for your use only and will not lease it out to another
device or computer on the internet. In order for a computer or device
on the internet to be contacted on a regular basis by a remote device
it must have a Static IP Address.

Keeping the example of a phone number in mind, if you constantly changed
your phone number it would be impossible for others to contact you on
a regular basis using the same phone number. This is the case for Dynamic
IP Addresses. If your ISP Assigns you a different Public IP Address every
time you connect to the internet then your Public IP Address is Dynamic.
It is not possible to use Dynamic IP Addresses with the Valid IP Address
feature of InfiniTime.

Private IP Addresses can also be static or dynamic. Dynamic IP Addresses
are often used on local area networks in order to reduce the amount of
manual configuration that must be performed by the Network Administrator.
Dynamic IP Addresses are automatically assigned by a DHCP server on your
local area network. Static IP Addresses must be manually configured by
the Network Administrator or other Authorized Personnel with access to
your network equipment.

#### How do I locate and determine if the Private IP Address for a machine on my local area network is static?

It is possible to determine the IP Address
assigned to any computer on a Windows Operating system by using the dos
command IPCONFIG. The following steps will walk you through opening an
dos prompt, using the IPCONFIG command, and reading the command's output.
You must be at the machine to perform the steps outlined below. If you
are still unsure after following this process please contact your Network
Administrator for assistance.

- Click on Start.

![](/img/CH2_PGP39.gif)

- Click on Run.

![](/img/EmpSpecValidIPSUBNET.jpg)

- Type cmd into the dialog box.

![](/img/Timeout_CompBtn.jpg)

- Click OK.

- A dos window will open. Type ipconfig
  /all

![](/img/Sec025.png)

- Hit enter. The network configuration
  of your server will be displayed.

- The InfiniTime
  7.0 Server should have a static ip address. The results below indicate
  a static address of 192.168.1.40 with DHCP disabled.

![](/img/Ch2_PGP9.gif)

- The results below show DHCP enabled.
  This means the computer has a dynamic IP Address assigned. The computer
  must be configured with a static Private IP Address in order to grant
  or limit access to it using Valid IP Addresses.

![](/img/CH2_PGP17.gif)

#### How do I locate and determine if the Public IP Address for a machine on a remote network is static?

A variety of websites exist to assist internet users with identifying
their Public IP Address. One such website is http://www.whatismyip.com.
Simply browse to this website to identify your Public IP Address. The
simplest way to determine if your Public IP Address is static is to contact
your Internet Service Provider (ISP).

To determine your Public IP Address using www.whatismyip.com

Click on Start

![](/img/secr4.gif)

Click on Run

![](/img/Sec006.png)

Type www.whatismyip.com in the dialog box as shown.

![](/img/SecFilter01.gif)

Click OK.

The website will open and display your Public IP Address on the home
page.

#### Why would I want to configure Valid IP Addresses?

Valid IP Addresses make it possible to restrict access to the InfiniTime Software Application from
all computers, both local and remote, except those with an IP address
that is defined as valid or authorized. This helps secure confidential
employee information that may be contained within the InfiniTime
Database by adding an extra layer of security to the application. Users
must not only have valid login credentials but they must also be located
at a machine with an IP Address that has been designated as valid by the
InfiniTime Software Administrator.

Valid IP Addresses can also be used to restrict employee access to certain
sites. A corporation with multiple sites may only want their employees
to be able to clock in or out from work using the InfiniTime
Software when they are at the office. Valid IP Addresses can be assigned
to individual employees. Depending upon the configuration, this will allow
the employee to access the software only from their desk or from any computer
in the office. If the employee would attempt to access the software from
any other machine they would be denied access.

Before deciding to use the Valid IP Address feature of InfiniTime you must understand how
your software is deployed. Four deployment options are available for InfiniTime as outlined below.

Standalone InfiniTime
Server

![](/img/Sec014.png)

Standalone Installations require only a server. In a Standalone Installation
the server hosts all InfiniTime
files and information. The InfiniTime
software can be viewed using a web browser in the same way it would be
accessed on a Client machine. A stand-alone installation requires an Internet
connection during installation for registration purposes only. After installation
an Internet connection is not required for use of the software.

Valid IP Addresses can not be used to limit access in a standalone environment.
The InfiniTime Server can
not be restricted from accessing InfiniTime.

Onsite InfiniTime
Server with On-Site Clients

![](/img/EmpSpecValidIP_BlockedRemSites.jpg)

As shown, this server is connected to a Local Area Network and hosts
the InfiniTime software
for Client machines that are on the local network. Employees and Managers
can access the software and all of its features from any computer on the
network.

In this scenario Valid IP Addresses can be used to limit access to specific
hosts on the local area network. This would be accomplished by retrieving
the IP Address from each computer for which access is to be granted. This
IP Address would then be configured in the Company or Employee Valid IP
Address table to grant the desired level of access.

Onsite InfiniTime
Server with Off-Site Clients

![](/img/CH2_PGP32.gif)

As pictured, this server has a Static ip address and uses an Internet
service such as T1, DSL, or Cable to connect to the Internet. Any employee
or affiliate armed with the proper web site address and their login information
can log into the InfiniTime
software in order to run the InfiniTime
Labor Management Software. It is important to understand that there is
no client software required to access the InfiniTime
Application. Any computer connected to the internet with a web browser
can be used to access the InfiniTime
Software. Users must simply have valid login credentials and the proper
web site address to access the InfiniTime
Software on the server.

Valid IP Addresses make it possible to limit access to the InfiniTime server to specific remote
sites. This is accomplished by defining a remote computer's Public IP
Address as valid within the Company or Employee Valid IP Address Table
to grant the desired level of access.

Onsite InfiniTime
Server with On-Site and Off-Site Clients

![](/img/CH2_PGP6.gif)

Combining the first two options provides a versatile deployment alternative
separating Web Applications from other software applications. Employees
on the local network and abroad have full access to all of InfiniTime's features. Remote users
need only a computer or laptop, an Internet connection, and their login
information to connect to the InfiniTime
software.

In this scenario Valid IP Addresses can be used to limit access to specific
machines on the local area network and specific remote sites.

#### What information should I have available before attempting to configure Valid IP Addresses?

The Following steps should be completed before attempting to configure
Valid IP Addresses:

- List all computers on the local network that will be granted access
  to the InfiniTime Software.
  If all computers on the local network will be granted access to the
  InfiniTime software
  a complete list is not required.
- List all remote sites that will be granted access to the InfiniTime Software. If all remote
  sites are to be granted access to the InfiniTime
  software a list is not required.
- Verify and record the IP Address for each computer on the local
  network listed in step 1. Each computer must have a static IP Address.
- Verify and record the Public IP Address for each remote site listed
  in step 2. Each site must have a static public IP Address. Note: All
  computers at the remote site will use the same Public IP Address.
  It is not possible to grant only specific remote machines access to
  the InfiniTime Software
  using Valid IP Addresses.

#### What is the difference between Company Wide Valid IP Addresses and Employee Specific Valid IP Addresses and why would I choose to use one over the other?

InfiniTime features two
methods of defining Valid IP Addresses in order to offer Software Administrators
complete control over how the InfiniTime
Software Application is accessed. Company Wide Valid IP Addresses are
IP Addresses from which any employee can login to the InfiniTime
Software. Employee Specific Valid IP Addresses are IP Addresses from which
a specific employee will be granted access. The following configurations
are available:

Company
Wide Valid IP Addresses Only

The use of only Company Wide Valid IP Addresses will grant all employees
access to the InfiniTime
Software from any IP Address defined as valid within the Company Wide
Valid IP Address table.

Employee
Specific Valid IP Addresses Only

The use of only Employee Specific Valid IP Addresses will grant access
to the InfiniTime Software
from any location for employees that do not have Valid IP Addresses defined.
Employees with Employee Specific Valid IP Addresses will only be able
to login from hosts with an IP address designated as valid in the Employee
Valid IP Address Table under their employee record.

Company
Wide and Employee Specific Valid IP Addresses

The use of both Company Wide and Employee Specific Valid IP Addresses
will grant access from the IP addresses defined by as valid by the Company
Wide TCP/IP Address Table for any individual without Employee Specific
Valid IP Addresses defined. Employees with Employee Specific Valid IP
Addresses will only be able to login from hosts with an IP address designated
as valid in the Employee Valid IP Address Table under their Employee Record.

It is important to note that the Employee Specific Valid IP Addresses
override Company Wide Valid IP Addresses. For example if Valid IP Addresses
were configured as shown below, Employee A would only be able to access
the InfiniTime 7.0software
from 10.1.1.64, even though 10.1.1.16, 10.1.1.32, and 10.1.1.48 are defined
as Company Wide Valid IP Addresses. By defining employee specific Valid
IP addresses you are instructing the software to grant access to that
employee from ONLY those addresses
specified in the Employee Specific Valid IP Address Table.

Company Wide Valid IP Addresses                                     Employee
A Valid IP Addresses

10.1.1.16                                                                                  10.1.1.64

10.1.1.32

10.1.1.48

#### What is the proper way to grant access to all computers or hosts on a given subnet or network address?

To grant access to all computers or hosts on a given subnet or network
address, first identify the common digits  of the IP address then
fill the remaining portion of the IP address with zeroes.

For example:

To grant access to all computers with the IP Addresses of 192.168.1.1
to 192.168.1.255 first identify the common portion of the IP address.

192.168.1.1

192.168.1.255

The common portion of the IP Address is the first three octets or 192.168.1.
Fill the remaining portion of the IP Address with zeroes. In this case,
the address to be added to the Company Valid IP Address Table would be
192.168.1.0
