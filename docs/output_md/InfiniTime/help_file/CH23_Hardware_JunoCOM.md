xml version="1.0" encoding="utf-8"?





Determine COM Port for Juno Direct Communication




# Determine COM Port for Juno Direct Communication

Serial Ports and USB Ports on the back of a computer tower are assigned logical identifiers, referred to as COM ports within Windows Operating Systems. COM ports are used to communicate with external devices attached to the port through the RS-232 or USB communication standards. Physical serial ports on the back of a computer are generally assigned to COM 1 or COM 2 as shown below. Physical USB Ports are generally assigned to COM 3 to COM 15. Refer to the appropriate section of this document for RS232 Communications, which use Serial Ports, or USB communications, which use USB Ports.

USB Communications - USB Ports

To determine the COM Port Windows has assigned to the USB to Serial Converter follow the steps below. Administrator access to the InfiniTime Server is required to perform these steps.

1. Ensure the USB to Serial Converter is plugged into a USB Port on the InfiniTime Server.

2. Click on Start or the Windows Logo depending on your operating system.

Windows XP          Windows                  Windows

  2003 & 2008               Vista

  Server

![](/img/02_Start_Button.gif)        ![](/img/CH23_HRDW_VistaDevMGMT.gif)                    ![](/img/TS4.gif)

3. Click on Run or Click in the Search Dialog box depending on your operating system.

Windows XP                                                                                  Windows Vista

![](/img/TS1.gif)          ![](/img/TS1.gif)

4. Type devmgmt.msc into the Dialog Box as shown below.

Windows XP                                                                                  Windows Vista

![](/img/Start.gif)                  ![](/img/CH23_HRDW_Vista_Devmgmtmsc.gif)

5. Press Enter. Device Manager will be displayed.

![](/img/CH23_HRDW_COM.gif)

6. Click on Ports (COM & LPT)

![](/img/Start.gif)

7. The Prolific USB-to-Serial Comm Port will be displayed. Take note of this value and continue to [Juno Reader Setup - USB Direct Connect](Juno_Reader_Setup_-_USB_Direct_Connect.md) to configure InfiniTime for use with your USB Juno Reader. The image below shows the Prolific USB-to Serial Comm Port as COM4.

![](/img/CH23_HRDW_COM4.gif)

RS232 Communications - Serial Ports

![](/img/TS3.gif)

If you only have one Serial Port on the back of your computer it can safely be assumed that this port has been designated as COM 1. Determining which serial port is assigned to a specific COM port is best done through trial and error. The Device Manager Utility within Windows can be used to determine what COM ports are in use on your system.

Device Manager

Device Manager is a utility included with Microsoft Windows Operating systems, which allows users to display and control hardware items attached to a computer.

Opening Device Manager:

1. Click Start

![](/img/TS7.gif)

2. Click Run

![](/img/CH23_HRDW_COM.gif)

3. Type devmgmt.msc into the Run Dialog Box as shown below.

![](/img/image15.jpg)

4. Click OK. Device Manager will be displayed.

![](/img/image15.jpg)

5. Click on the Plus sign to the left of Ports (COM & LPT)

![](/img/TS5.gif)

6. A list of assigned COM ports will be displayed.

![](/img/ts2.gif)

COM1 is associated with one of the Serial Ports on the back of the computer as introduced in the beginning of this document. COM 2 is associated with the other Serial Port on the back of the computer, assuming there are two. COM 3 is associated with a USB to Serial Adapter as explained later in this document. Knowing which COM ports are installed on your computer can help you to determine which port to assign in the InfiniTime software when configuring your clock.

If multiple COM ports are installed on your computer and you have more than one serial port on the back of your computerâs tower then a trial and error approach must be used to determine which COM port your direct connect clock is connected to.