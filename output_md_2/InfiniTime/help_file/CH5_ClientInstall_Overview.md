xml version="1.0" encoding="utf-8"?





Overview




# Client Installer Overview

While no installation is required for InfiniTime Client Machines, certain security features and settings must be set properly in order for InfiniTime 7.0 to display correctly and to permit printing from InfiniTime 7.0 on a Client machine. As reviewed in the Client Access Section of this document a web address is required to access the InfiniTime 7.0 software and differs depending on the type of Client machine. The InfiniTime 7.0 Web Address is composed of a hostname, IP Address, or Domain Name depending on where the InfiniTime Server is located relative to the InfiniTime Client Machine.

InfiniTime is bundled with a Client Installer which configures all required Internet Explorer 8 Browser Security Settings and creates shortcuts to the InfiniTime Software on the desktop of the client machine. The Client Installer is located in the Client Shortcuts directory on the Desktop of the InfiniTime Server. During installation, the Client Installer prompts the user for the best method of communicating with the InfiniTime Server. For on-site clients, the InfiniTime Server's hostname is recommended, while the Public IP Address or Domain Name of the InfiniTime Server is recommended for use with Off-Site Clients.

To simplify use of the Client Installer for non-technical users, the InfiniTime Server's Hostname is written to a text file called host.txt during Installation of the InfiniTime Software. This text file and the InfiniTime Client Install can be distributed for use on all On-Site client machines. Users can simply open the host.txt file and enter the value contained within the file when the Client Installer prompts for the Hostname or IP Address of the InfiniTime Server.

If you are not sure of the InfiniTime Server's Hostname, Public IP Address, or Domain Name contact your Network Administrator for assistance.

Technical Note: The InfiniTime Client Installer requires Internet Explorer 8 (IE8) to be installed on the Client Machine. Only IE8 is supported by the Client Installer at this time.