xml version="1.0" encoding="utf-8"?





Ethernet Hardware Terminals: Configuration Scenarios for Remote Sites




# Ethernet Hardware Terminals: Configuration Scenarios for Remote Sites

Terms

Protocol - One way to think about and understand the purpose of a protocol is to compare it to a standard. People throughout the world work in different languages, on different types of machines, using different software applications, and different types of computers. As a whole it would not be possible for worldwide communication to occur without certain standards governing how information can be exchanged between different groups or individuals. These standards for communication can be described as a set of rules. Similarly there are also rules for governing how data is sent over a computer network which are referred to as protocols. For example the Internet Protocol, often referred to as IP, defines how packets of information are transferred across the internet.

IP Address - Each computer on a network is assigned an IP Address in order to communicate with other machines. This idea can be illustrated by comparing a network to a town. Each building in a town is identified by a street address. If a building did not have a street address it would not be possible to locate it or provide instructions for others to travel to it. Similarly every computer on a network must have an IP address in order to communicate with other machines on the network. IP Addresses have four parts which are referred to as an octet. Each octet is separated by a period as shown below. Valid values for each octet include 0 to 255.

192.168.0.10

First Octet   Second Octet   Third Octet   Fourth Octet

Static IP Address - A static IP Address is assigned to an individual and does not change. Returning to the Network : Town analogy this can be compared to a building which is always found at the same street address. This makes it possible for others to always know where the building, or a computer in the case of a network, is found. Businesses that provide a service to the community make their street address public in order for customers to be able to find them. Similarly computers that provide a service are generally assigned a static IP Address in order to ensure remote computers will be able to find and communicate with them.

Dynamic IP Address - A dynamic IP address is assigned to an individual on a temporary basis. Returning to the Network : Town analogy this can be compared to a street cart which will not always be located at the same spot in the town. It would not be possible for an individual to find the street cart without having prior knowledge of its location or an alternate method of contacting them. Similarly it is not possible for a computer with a dynamic IP Address to provide services to other computers on a network without using additional services such as a Domain Name System (DNS) or a Dynamic Domain Name System (DDNS) to provide an alternate means of identification.

Internal // Private IP Addresses - An Internal IP Address refers to an IP Address which is only valid inside of a private network. Unlike Public IP Addresses internal IP Addresses are specifically set aside for use on private networks and can be used by anyone. This means that three networks, or even three million networks, can each use the same Private IP Addresses. Returning to the Network : Town analogy if we think of our town as a small part of a larger city we begin to understand this concept as is not uncommon for a street to have the same name in different towns. A street address for a specific building in the town only refers to that specific building inside of that town. Similarly an Internal IP Address is only valid inside of a private network. Lets break down this example into a bit more detail. The image below shows two buildings with a street address of 1010 W Arbor Ave. Each building is located in a different town. A mail carrier responsible for delivering mail to each of these buildings receives a letter postmarked to 1010 W Arbor Ave. Anyone specifically located in George Town or Green Town would know where 1010 W Arbor Ave is. Yet to the rest of the world there is no way to determine which building the letter is intended to be sent to without additional information. For our town this additional information would take the form of City, State, Zip which tells us where in the world the specific street address is located. On a network a packet of information would be forwarded to a Public IP Address where it is then forwarded to the correct Internal IP Address. The network diagram below shows three computers each on a different private network. Two of the private networks use the same Internal IP addresses for their computers. It is not possible for the Host B to send information to Host A using its Private IP Address. Private IP Addresses cannot be used to communicate on the Internet.

![](/img/PublicIP_Port6.gif)                 ![](/img/PublicIP_Port3.gif)

The following are valid internal IP Address ranges. Remember an IP Address consists of four octets with valid values of zero to two hundred and fifty five (0 - 255) Any IP Address that falls within these ranges is an internal IP Address and cannot be used to communicate on the internet. In some cases you may be accidentally provided with an IP Address that falls within one of these ranges for an Ethernet clock at a remote site. The address you have been provided is the Internal IP Address for the clock on the remote network and is not the correct information. Remember internal IP Addresses cannot be used to communicate across the internet. Please request the Public IP Address for the remote site. This is the address you will need to setup within InfiniTime to communicate with your remote Ethernet clock. Refer to the scenarios below for more information.

10.0.0.0 - 10.255.255.255

172.16.0.0 - 172.31.255.255

192.168.0.0 - 192.168.255.255

Public IP Address - A Public IP Address refers to an IP Address which is used to communicate with other computers and devices on the Internet. Pubic IP Addresses are registered with a Regional Internet Registry (RIR) to avoid addressing issues. Only the registered holder of a Public IP Address can assign the address to a network device for communication on the Internet. Returning to our Network : Town analogy the City, State, and Zip Code help to identify where a specific street address is located within the world. Similarly a Public IP address specifies a computer's location on the Internet. Remember, Internal IP Addresses cannot be used to communicate on the Internet. For this reason a method must exist to translate between Internal IP Addresses and Public IP Addresses in order for hosts on a private network to communicate on the Internet. Network Address Translation (NAT) and Port Address Translation (PAT) provide this service. The image below shows traffic flow from Host B to Host A.

![](/img/PublicIP_Port8.gif)

Port - The best way to understand the role of a port in network communication is to return to our Network : Town analogy. Each building in a town has a specific street address which from our earlier examples is comparable to an IP Address. Each building also has multiple doors or points of entry from the outside world which are comparable to ports. Just like a door on a building makes it possible for multiple people to walk in and out of the building at once, ports make it possible for multiple conversations with other network devices or applications to occur simultaneously. Also similar to a door, a port can be in a closed or open state. A closed port does not have a service listening for traffic behind it. Any communication sent to a closed port will not reach the end destination successfully as illustrated below. Each port on a computer is identified by a port number. Port numbers range from 0 to 65535. Different applications and network services use different ports.

![](/img/PublicIP_Port3.gif) ![](/img/PublicIP_Port4.gif)

TCP & UDP - Transmission Control Protocol (TCP) and User Datagram Protocol (UDP) are two protocols or sets of rules which govern how traffic is sent between ports on a network. It is important to understand that a device expecting TCP data on a specific port will not function if the data is sent with UDP instead, though some devices will support both. A list of the Ethernet Clocks offered by Inception Technologies are listed below along with the port and protocol used by the clock.

 | Manufacturer | Model | Port | Protocol | 
| --- | --- | --- | --- |
 | Schlage | Scout 1000, 2000, 3000 & 4000 | 3001 | TCP | 
 | ZK Software | Athena | 4370 | UDP | 
 | ZK Software | Juno | 4370 | UDP | 
 | ZK Software | Thor | 4370 | UDP | 
 | ZK Software | Luna | 4370 | UDP | 
 | ZK Software | Zephyr | 4370 | UDP | 
 | Synel Industries | Apollo 715 | 3734 | TCP or UDP | 
 | Synel Industries | Atlas 777 | 3734 | TCP or UDP | 
 | Synel Industries | Orion 760 & Odyssey 780 | 3734 | TCP or UDP | 
 | Synel Industries | Omega 755 | 3734 | TCP or UDP | 

Network Address Translation (NAT) - As mentioned above NAT provides a mechanism for translating between Internal and Public IP Addresses. Without NAT it would not be possible for computers or devices on a private network to communicate across the internet. The image below shows successful communication between Host B and Host A. The NAT Table for each router is also shown to illustrate how an Internal IP Address is mapped to a Public IP Address. Though multiple methods exist for mapping Public IP Addresses to Internal Addresses, a static NAT mapping is generally used for configuring an Ethernet clock at a remote site. A static NAT mapping is used to map a specific Public IP Address to a specific Internal IP Address. In this way the internal device can always be reached at a specific public address. The example below illustrates NAT mappings as each internal device will always be assigned the same Public IP Address.

![](/img/PublicIP_Port1.gif)

Port Address Translation (PAT) - As mentioned above PAT provides a mechanism for translating between Internal and Public IP Addresses. PAT uses ports to map multiple Internal IP Addresses to a single Public IP Address. This type of Address Translation cannot be used to forward network traffic directly to an Ethernet Time and Attendance terminal. Port Forwarding must be used in conjunction with PAT in order to establish communication.

Domain Naming System (DNS) - Domain names of popular websites such as Google or Microsoft may be familiar to you already. DNS maps a word or phrase to an IP Address in order to make it easier for people to remember how to get to a website or computer on the Internet. DNS is considered an essential network service and is required to access a website or computer on the internet using a domain name. It is important to note that DNS maps a single IP Address to a single domain. For this reason most domains are mapped to a static Public IP Address.

Dynamic Domain Naming System (DDNS) - In some cases it is not possible to obtain a Static Public IP Address. This is often the case when using a non-commercial Internet Service such as residential DSL or Cable as many Internet Service Providers (ISP) will not provide a Static Public IP Address for these connection types. If a Static Public IP Address is not available Dynamic DNS (DDNS) must be used to map your Public IP Address to a DDNS domain. The dynamic DNS domain can then be used to communicate with devices on your network. Dynamic DNS is provided as a service and is available for free from many sources online. Use your preferred search engine to perform a search for 'free dynamic dns' to find free DDNS providers. Your router must support DDNS in order to use it. Not all routers support this service.

Internet Service Provider (ISP) - An Internet Service Provider is a company that collects a monthly or yearly fee in exchange for providing subscribers with Internet Access. Internet Services vary in price, speed, and service type. Various services are available depending upon your area. Dial up, DSL, and Cable, are common non-commercial services though Dial up has largely become outdated except in rural areas where other services are not available. It should be noted that some ISPs will block certain port ranges in an attempt to provide security. To prevent possible difficulties it is good practice to contact your ISP in order to determine what, if any, ports are being blocked.

Router - A router is a device that is responsible for forwarding data packets from one network to another. It is important to note not all routers are the same as their role differs from network to network. When working with remote Ethernet clocks it is important to ensure support for the following features is available: NAT, Port Forwarding, and Dynamic DNS.

Port Forwarding - Port forwarding is a process that a router or firewall uses in order to direct the appropriate kind of network data to the correct internal device on a specific port. Returning to our Network : Town analogy, recall that a door is similar to a port. Why does one go through a door? To reach the room on the other side. Lets say that two visitors are arriving at your building for a company tour but they are not sure where to go. The first visitor is expecting a tour of the Office area while the second visitor is expecting a tour of the Production Facility. A receptionist would often perform the function of directing these visitors to the appropriate area in order to reach their destination. Port forwarding performs this same service. Traffic from the Internet arrives on a port at the public interface of the router or firewall. The router is configured to forward all traffic arriving on a specific port to a particular device on the inside of the network at a specific port. This is illustrated by the diagram below. The diagram illustrates traffic arriving from the Internet on two different ports. Port Forwarding configuration on the router specifies that all traffic inbound on port 4370 is to be delivered to the Internal IP Address of 192.168.0.10 at port 4370. Traffic inbound on port 4371 is delivered to the Internal IP Address of 192.168.0.11 at port 4370.

![](/img/PublicIP_Port4.gif)

Scenarios

Single Remote Site with a single Static Public IP Address // Single Internal Device

Some locations such as warehouses do not require Internet Access for day to day operations. In order to place an Ethernet Time and Attendance Data Collection Terminal such as the Thor or the Scout at such a location a connection to the Internet is required. Be sure to confirm with your chosen ISP that your public IP Address is static and write down the IP Address provided to you. This address will be required when configuring the InfiniTime Application to communicate with your remote device. It is important to note that a router is required to route packets and perform NAT services to and from your Time and Attendance terminal even though you will only have a single device on the network. Two methods are available to establish communication between the InfiniTime Server and an Ethernet Time and Attendance terminal located at a remote site with a single static IP Address and a single internal device. One option is to use NAT in order to forward all traffic sent to the Public IP Address directly to the clock. A second option is the use of port forwarding to send all traffic sent to a specific port on the Public IP Address to the clock. These methods are described below.

NAT - The diagram below illustrates the configuration of NAT for a remote site with a single Public IP Address where the Time and Attendance terminal will be the only item on the internal network.

![](/img/PrivateIP.gif)

Requirements - The following items are required in order for communication between the InfiniTime Server and the Thor Terminal to be successful. If you have difficulties communicating with your remote terminal verify each of the following items are configured correctly. You may also wish to refer to the troubleshooting guide below. The example does not accurately depict all possible network configurations. As a general rule any hardware or software firewall located between the source (The InfiniTime Server) and the destination (The Thor Terminal) must be configured to pass traffic on the chosen port and to trust the local network.

* Software Firewall on the InfiniTime Server must permit outbound traffic on port 4370
* Router at Main Office must permit inbound traffic on port 4370 on the Private Interface
* Router at Main Office must permit outbound traffic on port 4370 on the Public Interface
* ISP must pass traffic on port 4370. If you have difficulties with communication contact your ISP to verify the chosen port is open.
* Router at Branch Office must permit outbound traffic on port 4370 on the Private Interface
* Router at Branch Office must permit inbound traffic on port 4370 on the Public Interface
* Router at Branch Office must be configured appropriately for NAT with a static mapping between the Public IP Address and the Internal IP Address of the Ethernet terminal.
* Router at Branch Office must be configured to respond to PING as InfiniTime requires the ability to ping the destination IP Address.

Port Forwarding - The diagram below illustrates the configuration of Port Forwarding for a remote site with a single Public IP Address where the Time and Attendance terminal will be the only item on the internal network.

![](/img/PublicIP_Port7.gif)

Requirements - The following items are required in order for communication between the InfiniTime Server and the Thor Terminal to be successful. If you have difficulties communicating with your remote terminal verify each of the following items are configured correctly. You may also wish to refer to the troubleshooting guide below. The example does not accurately depict all possible network configurations. As a general rule any hardware or software firewall located between the source (The InfiniTime Server) and the destination (The Thor Terminal) must be configured to pass traffic on the chosen port and to trust the local network.

* Software Firewall on the InfiniTime Server must permit outbound traffic on port 4370
* Router at Main Office must permit inbound traffic on port 4370 on the Private Interface
* Router at Main Office must permit outbound traffic on port 4370 on the Public Interface
* ISP must pass traffic on port 4370. If you have difficulties with communication contact your ISP to verify the chosen port is open.
* Router at Branch Office must permit outbound traffic on port 4370 on the Private Interface
* Router at Branch Office must permit inbound traffic on port 4370 on the Public Interface
* Port forwarding must be configured to send traffic to the default port as listed in the previous table for your Time and Attendance Terminal. It is not possible to change the listening port for these terminals.
* Router at Branch Office must be configured to respond to PING as InfiniTime requires the ability to ping the destination IP Address.

Single Remote Site with a single Static Public IP Address // Multiple Internal Devices

Port Forwarding - The diagram below illustrates the configuration of Port Forwarding for a remote site with a single Static Public IP Address where there are multiple devices on the internal network.

![](/img/PrivateIP2.gif)

Requirements - The following items are required in order for communication between the InfiniTime Server and the Thor Terminal to be successful. If you have difficulties communicating with your remote terminal verify each of the following items are configured correctly. You may also wish to refer to the troubleshooting guide below. The example does not accurately depict all possible network configurations. As a general rule any hardware or software firewall located between the source (The InfiniTime Server) and the destination (The Thor Terminal) must be configured to pass traffic on the chosen port and to trust the local network.

* Software Firewall on the InfiniTime Server must permit outbound traffic on ports 4370 and 4371.
* Router at Main Office must permit inbound traffic on ports 4370  and 4371 on the Private Interface
* Router at Main Office must permit outbound traffic on ports 4370  and 4371  on the Public Interface
* ISP must pass traffic on ports 4370  and 4371 . If you have difficulties with communication contact your ISP to verify the chosen port is open.
* Router at Branch Office must permit outbound traffic on ports 4370  and 4371  on the Private Interface
* Router at Branch Office must permit inbound traffic on ports 4370  and 4371 on the Public Interface
* Port forwarding must be configured to send traffic to the default port as listed in the previous table for your Time and Attendance Terminal. It is not possible to change the listening port for these terminals. As shown in the diagram traffic from multiple public ports can be directed to the default port for separate Internal IP Addresses.
* Router at Branch Office must be configured to respond to PING as InfiniTime requires the ability to ping the destination IP Address.

Single Remote Site with multiple Static Public IP Addresses // Multiple Internal Devices

Choose a single Public IP Address for use with your remote Ethernet Time and Attendance Terminals and follow the instructions above for a Single Remote Site with a single Static Public IP Address // Multiple Internal Devices.

Single Remote Site with a single Dynamic Public IP Address // Multiple Internal Devices

In some cases it is not possible to obtain a Static Public IP Address. This is often the case when using a non-commercial Internet Service such as residential DSL or Cable as many Internet Service Providers (ISP) will not provide a Static Public IP Address for these connection types. If a Static Public IP Address is not available Dynamic DNS (DDNS) must be used to map your Public IP Address to a DDNS domain. The DDNS service will map the DDNS domain name to your Public IP Address and will change the mapping as your Public IP Address changes.

Dynamic DNS w/ Port Forwarding - The diagram below illustrates the configuration of Dynamic DNS with Port Forwarding for a remote site with a single Public IP Address where there are multiple devices on the internal network.

![](/img/PrivateIP.gif)

Traffic Flow

Infinitime Server wishes to send data to ABCCO.dyn-dns.com at port 4370 and 4371. Remember, computers do not understand words or phrases and must translate the DDNS Name "ABCCo.dyn-dns.com" to an IP Address. A DNS server must be configured on the network at the Main Office for this purpose. Once an IP Address has been associated with the domain name communication continues as normal.

Requirements - The following items are required in order for communication between the InfiniTime Server and the Thor Terminals to be successful. If you have difficulties communicating with your remote terminals verify each of the following items are configured correctly. You may also wish to refer to the troubleshooting guide below. The example does not accurately depict all possible network configurations. As a general rule any hardware or software firewall located between the source (The InfiniTime Server) and the destination (The Thor Terminal) must be configured to pass traffic on the chosen port and to trust the local network.

* Software Firewall on the InfiniTime Server must permit outbound traffic on ports 4370  and 4371
* Router at Main Office must permit inbound traffic on ports 4370  and 4371  on the Private Interface
* Router at Main Office must permit outbound traffic on ports 4370  and 4371  on the Public Interface
* ISP must pass traffic on ports 4370  and 4371. If you have difficulties with communication contact your ISP to verify the chosen port is open.
* Router at Branch Office must permit outbound traffic on ports 4370  and 4371 on the Private Interface
* Router at Branch Office must permit inbound traffic on ports 4370  and 4371 on the Public Interface
* Dynamic DNS must be configured appropriately to route traffic to your network.
* Port forwarding must be configured to send traffic to the default port as listed in the previous table for your Time and Attendance Terminal. It is not possible to change the listening port for these terminals. As shown in the diagram traffic from multiple public ports can be directed to the default port for separate Internal IP Addresses.
* Router at Branch Office must be configured to respond to PING as InfiniTime requires the ability to ping the destination IP Address.

Single Remote Site with a single Dynamic Public IP Address // Single Internal Device

In some cases it is not possible to obtain a Static Public IP Address. This is often the case when using a non-commercial Internet Service such as residential DSL or Cable as many Internet Service Providers (ISP) will not provide a Static Public IP Address for these connection types. If a Static Public IP Address is not available Dynamic DNS (DDNS) must be used to map your Public IP Address to a DDNS domain. The DDNS service will map the DDNS domain name to your Public IP Address and will change the mapping as your Public IP Address changes.

Dynamic DNS w/ Port Forwarding - The diagram below illustrates the configuration of Dynamic DNS with Port Forwarding for a remote site with a single Public IP Address where the Time and Attendance terminal will be the only item on the internal network.

![](/img/PublicIP_Port1.gif)

Traffic Flow

Infinitime Server wishes to send data to ABCCO.dyn-dns.com at port 4370. Remember, computers do not understand words or phrases and must translate the DDNS Name "ABCCo.dyn-dns.com" to an IP Address. A DNS server must be configured on the network at the Main Office for this purpose. Once an IP Address has been associated with the domain name communication continues as normal.

Requirements - The following items are required in order for communication between the InfiniTime Server and the Thor Terminals to be successful. If you have difficulties communicating with your remote terminals verify each of the following items are configured correctly. You may also wish to refer to the troubleshooting guide below. The example does not accurately depict all possible network configurations. As a general rule any hardware or software firewall located between the source (The InfiniTime Server) and the destination (The Thor Terminal) must be configured to pass traffic on the chosen port and to trust the local network.

* Software Firewall on the InfiniTime Server must permit outbound traffic on port 4370
* Router at Main Office must permit inbound traffic on port 4370 on the Private Interface
* Router at Main Office must permit outbound traffic on port 4370 on the Public Interface
* ISP must pass traffic on port 4370. If you have difficulties with communication contact your ISP to verify the chosen port is open.
* Router at Branch Office must permit outbound traffic on port 4370 on the Private Interface
* Router at Branch Office must permit inbound traffic on port 4370 on the Public Interface
* Dynamic DNS must be configured appropriately to route traffic to your network.
* Port forwarding must be configured to send traffic to the default port as listed in the previous table for your Time and Attendance Terminal. It is not possible to change the listening port for these terminals. As shown in the diagram traffic from multiple public ports can be directed to the default port for separate Internal IP Addresses.
* Router at Branch Office must be configured to respond to PING as InfiniTime requires the ability to ping the destination IP Address.

Single Remote Site with multiple Dynamic Public IP Addresses // Multiple Internal Devices

Choose a single Public IP Address for use with your remote Ethernet Time and Attendance Terminals and follow the instructions above for a Single Remote Site with a single Static Public IP Address // Multiple Internal Devices.

Troubleshooting

Even though there are multiple points of failure a standard troubleshooting procedure can be used to quickly identify most issues. If you should experience difficulties or receive excessive errors when attempting to communicate with your remote Ethernet Terminal from within the InfiniTime Application follow the steps below to locate the source of the problem.

1.) Ping the Static IP Address assigned to the Time and Attendance Terminal from another computer on the remote network. If the Ethernet terminal should fail to respond verify the items below. Additional instructions for configuring these items can be found in the Hardware Manual for your specific terminal.

* + Verify your Ethernet Terminal is plugged in.
  + Check for issues related to the Ethernet cable.
  + - Replace the cable if any cuts or slices are evident in the cable run.
    - Fix the cable if the cable ends are improperly terminated.
    - Test the cable with a laptop to verify the cable is properly wired, or use a wire tester if available.
    - Verify the cable is connected to the correct port on your Ethernet terminal.
    - Try using a different port on your hub, switch, or router.
    - The Ethernet Cable run should not exceed 100 meters. (328 ft.)
  + Verify Network Information is correct
* The Ethernet Terminal must be assigned a static IP address. Contact your network administrator if you are unsure if the address you have is static.
* Default Gateway
* Subnet Mask

* Check Ethernet Terminal Configuration
* + Ethernet Terminal IP Address
  + Ethernet Terminal Subnet
  + Default Gateway
  + Peer Address should be set to 000.000.000.000\*
  + Host Bits\*

\*Only applies to specific Time and Attendance Hardware Models.

* Check Software Configuration
* + IP address
  + Port
  + Reader Address

2.) Ping the Public IP Address of the remote router. If the router should fail to reply verify the items below.

* The router must be configured to respond to PING.
* Verify the Internet Connection at the main and remote site(s) is up.

3.) If communication errors should still occur after verifying the aforementioned items there is most likely an issue with NAT or Port Forwarding. It is also possible that traffic is being blocked before it gets to the destination. Verify all hardware or software firewalls between the source and destination are configured to permit traffic on the chosen ports. It may also help to check with your ISP to see if they are blocking traffic on any ports.