xml version="1.0" encoding="utf-8"?





Software Licensing and Virtualization




# Software Licensing and Virtualization

A Note on Software Licensing and Virtual Servers

Software Licensing for the InfiniTime Application was developed to reduce costs and facilitate competitive pricing. The software licensing solution replaces the HASP Key hardware licensing solution for new InfiniTime Orders. Elimination of the USB HASP Key removes the requirement of a USB Port from InfiniTime's minimum requirements and makes the software more appealing for use on a virtual machine, however this is not the intent of the Software Licensing System. Known challenges exist with virtual machines and the InfiniTime Application as outlined below.

Inception Technologies does not recommend use of a virtual platform for hosting the InfiniTime Software, though we can confirm customers have successfully implemented and are using the InfiniTime Application on virtual platforms by following the guidelines below. The following is presented as base requirements for using a virtual platform such as Microsoft's Hyper-V with the InfiniTime Application. Due to the number of virtualization platforms available, Inception Technologies does not test, support, or recommend individual virtualization platforms. Ultimately, if difficulties are encountered during installation all responsibility for troubleshooting Virtual Machine Configuration,  the InfiniTime Installation and / or reinstalling on a recommended platform remains the responsibility of the customer. At this time, a traditional physical server is recommend for use with the InfiniTime Application.

* Software driven file storage systems, such as the virtual hard disk (VHD) utilized by Microsoft's Hyper-V, are not fast enough to meet the high performance read and write demands of the Oracle 10G Database. In order to install InfiniTime on a virtual platform, physical storage must be made available to the virtual operating system through use of Direct Attached Storage (DAS) or a Storage Area Network (SAN) for Installation of the InfiniTime Software. Use or setup of these technologies can be cost prohibitive for small businesses. Knowledgeable IT Staff is also required to support such architecture. Inception Technologies does not provide support for the configuration of customer network architecture or the configuration of a virtual server and related storage solutions. In order to install InfiniTime on a Virtual Platform, physical storage must be made available. Failure to provide physical storage on virtual platforms leads to I/O related database errors and can result in permanent loss of data and database integrity.

Virtual Machines using Virtual Hard Disks:

![](/img/image-404.png)

* + To clarify, the Operating System of the Virtual Machine may be installed using physical storage (DAS or SAN) or a virtual hard disk (VHD). Regardless of how the Operating System of the Virtual Machine is installed, physical storage must be made available for and selected during installation of InfiniTime. Acceptable storage scenarios are depicted below.

Virtual Machines using Physical Storage:

![](/img/image-404.png)

Virtual Machines using a Storage Area Network:

![](/img/image-404.png)

Virtual Machine using VHD for Guest OS and Physical Storage for InfiniTime Partition

![](/img/image-404.png)

* Oracle does not provide database support for installations running on a virtual platform. Any database issue, especially I/O related database errors, could potentially result in loss of all data. If complications should arise with the Oracle database, the only method for returning the InfiniTime Application to a production state is to reinstall the InfiniTime Software and the Oracle database, and to restore an InfiniTime Backup. Inception Technologies cannot be held responsible for data loss due to failure to make and retain regular backups of the InfiniTime Database. InfiniTime includes a Backup / Restore component specifically for this purpose. Customers choosing to install on a virtual platform must take extra care to ensure their InfiniTime Database is backed up, as it is not possible to troubleshoot database related issues.

The above guidelines are supplied as base requirements for using a virtual platform with the InfiniTime Application. All minimum requirements, as listed in Chapter 2 - Minimum Requirements of the Installation Manual must also be met by the Virtual Machine. Customers who choose to use a virtual environment for hosting the InfiniTime Application acknowledge that Inception Technologies does not test, support, or recommend individual virtual platforms. Installation on a virtual machine is not recommended due to lack of database support by Oracle and specific storage requirements which are outside of the support scope provided by Inception Technologies. Ultimately, if difficulties are encountered during installation, all responsibility for troubleshooting Virtual Machine Configuration, the InfiniTime Installation and / or reinstalling on a recommended platform remains the responsibility of the customer. A traditional physical server is currently the recommended platform for hosting the InfiniTime Application.

For customers who do not currently have an available physical server, Inception Technologies offers dedicated systems solutions with the InfiniTime Software pre-installed. Your Inception Technologies Sales Representative or Authorized InfiniTime Dealer can provide more information about the Total Enterprise System Solution (TESS) offered by Inception Technologies.