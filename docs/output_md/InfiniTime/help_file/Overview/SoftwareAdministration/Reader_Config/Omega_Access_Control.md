xml version="1.0" encoding="utf-8"?





Omega Access Control




# Access Control Wiring and Setup for the Reader

The Omega Terminal can be used to unlock an attached door when authorized employees perform an Access Control punch. Access control is compatible with readers using the direct connect and modem connection methods. The requirements below must be met in order for Access Control to function properly..

InfiniTime Software Requirements

* Access Control usage requires purchase of the Access Control Module. Contact your Inception Technologies Sales Representative for more information.

* Access Control Groups and Schedules must be configured for the reader. Refer to Chapter 3: Access Control Groups Setup for more information.

Access Control Wiring: Hardware Components

Hardware requirements vary based upon the type of electronic door strike chosen and wiring configuration desired. Many professionals with experience with electronics and electrical circuitry may wish to design a custom circuit to suit their environment and equipment. A basic custom wiring diagram is included for reference for professionals who wish to design their own circuitry. For users who are uncomfortable with designing their own circuitry Inception Technologies offers the SY-124 External Relay which can be used to safely isolate the hardware terminal from contact with high voltage circuitry. An external power supply is required to provide power to the door strike. The SY-755 Omega terminal has dry relay contacts which simply close or open the circuit allowing current to pass when activated. The Omega does not provide power to the relay contacts.

For those unfamiliar with the electrical parts contained in the diagrams below it is important to understand their basic operation before attempting to purchase and configure the equipment necessary to lock and unlock a door with the InfiniTime Application. The central part used in the diagrams below is referred to as a relay. A relay can be thought of as an electrical switch. A coil of wire, a common contact, a normally closed (NC) contact, and a normally open (NO) contact are the four basic parts that comprise a relay. A diagram is shown below to illustrate the operation of a relay.

![](/img/755ACC_SY124.gif)

In the normal state, or when unpowered, the relay coil is not energized and the relay contacts are in their normal state. In the normal state the normally open contacts are open and the normally closed contacts are closed as the name suggests. When activated the coil becomes energized forming a magnetic field which causes the relay contacts to close or open respectively. This is referred to as the picked state where power is applied to the relay and the relay coil is energized. The relay will make a small clicking sound when it is picked. Relay contacts will switch their state, the normally open contact will be closed and the normally closed contact will be open. The contacts will remain in this position until power to the coil is removed at which point the contacts will revert to their normal state. The InfiniTime Application controls the duration for which the relay is picked. Generally when using access control the wiring is setup in order to open the door when the relay is picked. The diagrams below provide example wiring circuits for door control based upon the voltage and current requirements of the door strike in use.  Inception Technologies takes no responsibility for the wiring and setup of Access Control equipment. Customers attempting to wire their own access control devices without the assistance of a professional electrician do so at their own risk. Inception Technologies is not responsible for damage to equipment caused by improper wiring.

*WARNING*: The internal relay is rated to withstand a voltage range of 0 to 24V DC and a current load of up to 1A. Using an external power supply of more than 24 VDC will damage internal components of the Omega Terminal. To prevent damage to the terminal, the door strike should not draw more than 1A current. An external relay must be used to separate the clock from high voltage / current circuitry.

Access Control Connection - High Voltage / Current Door Strike: Using SY-124

![](/img/RelayDiagram.gif)

This diagram depicts the proper wiring of the SY-124 External Relay for use with an electronic door strike. The SY-124 External relay is intended for those who do not wish to design their own circuitry for use with an access control system. This diagram contains four major parts, the Omega SY-755 Internal Relay (A), A straight through ethernet cord used to connect the Internal Omega Relay to the SY-124 (B), The SY-124 Relay Contacts (C), and the door strike with power adapter (D).

It is important to keep in mind the electrical specifications for the Internal Relay (A) of the Omega terminal and its operation. When the door is scheduled to be unlocked the normally open contacts on the Omega will open, causing the SY-124 to pick the relay which causes the door to unlock. The 6V DC power adapter provided with the SY-124 must be connected to the SY-124 and plugged in, as it provides the power necessary to energize the relay coils and pick the relay as explained in the previous section.

A straight through ethernet cable (B) is used to connect the Internal Omega Relay to the SY-124 external relay.

The SY-124 External Relay Contacts (C) provide the final connection between the door strike and a high voltage power source. It is important to keep in mind the electrical specifications for the External SY-124 Relay contacts when connecting a high voltage power source. The SY-124 Relay Contacts are rated for 115V AC at a current of 10A. The circuit connected to the contacts of the SY-124 should not exceed these voltage or current values. For your own safety, when wiring the door strike and power source into the SY-124 ensure the AC power source of the door strike and the DC power source of the SY-124 are turned off or unplugged. It will be necessary to remove the screws from the SY-124 and open the cover to expose the contact terminals. The contact terminals are of a screw down type, simply insert the wire into the slot of the connector and tighten the screw around the wire.

The Door Strike and AC Power Source assembly (D) are the final parts of the assembly. The power source should be placed in a safe and dry location.

Access Control Connection - High Voltage / Current Door Strike: Custom Wiring

![](/img/755ACC_Custom.gif)

This diagram depicts an example of custom wiring for use with an electronic door strike. This diagram contains four major parts, the relay inside of the Omega terminal (A), A straight through ethernet cord, connection box and DC power supply (B), A 5V Relay (C), and the door strike with power adapter (D).

It is important to keep in mind the electrical specifications for the Internal Relay (A) of the Omega terminal and its operation. When the door is scheduled to be unlocked the normally open contacts on the Omega terminal will close, picking the relay, which causes the door to unlock.

A straight through ethernet cord must be connected to the Internal Relay of the Omega Terminal and to a connection box. (B) The 5V DC power adapter should be connected directly to Pin 2 (Brown) within the connection box. The second contact on the DC power adapter should be wired to one end of the relay coil. The other end of the relay coil should be wired to Pin 7 (Orange) within the connection box. In this way the relay coil will energize when the circuit is closed by the Omega terminal at the appointed time.

The Relay Contacts (C) provide the final connection between the door strike and a high voltage power source. It is important to keep in mind the electrical specifications for the Relay contacts when connecting a high voltage power source. The voltage and current rating of the relay contacts are dependant upon the relay's construction and model. Refer to the data sheet provided by the relay's manufacturer for this information. The circuit connected to the contacts of the relay should not exceed these voltage or current values. For your own safety, when wiring the door strike and power source into the relay contacts ensure the AC power source of the door strike and the DC power source used to energize the relay coil are turned off or unplugged. Standard procedure and safety guidelines dictate that all high voltage wiring must be safely enclosed. All measure must be taken to prevent inadvertent contact with an individual. Inception Technologies is not responsible for any damages or injuries incurred while attempting to design and wire customized circuitry for these devices. It is recommended a professional electrician perform these tasks.

Access Control Wiring Troubleshooting Procedure

Basic troubleshooting steps and failure points are listed below for the diagrams above.

If the door does not unlock as expected first test the wiring at the Internal Relays by shorting the wires connected Pin 2 and Pin 7 of the together. Ensure all power supplies are plugged in or turned on. The door should unlock. If the door does not unlock check the following items:

Custom Wiring Diagram:

* Ensure the DC Power source is connected properly and functioning.
* Ensure the AC Power source is connected properly and functioning.
* Ensure Pin 7 (Orange) from the connection box is connected to one end of the relay coil.
* Ensure Pin 2 (Brown) from the connection box is connected to one end of the DC Power Adapter.
* Ensure the second end of the DC Power adapter is connected to the relay coil.
* Ensure the AC Power source and Door Strike are wired to the proper relay contacts and to each other. One side of the AC power source should be connected to the Normally Closed contact while the other is connected to a contact on the door strike. The second contact of the door strike should be connected to the common contact of the relay.
* Ensure a straight through ethernet cable is used between the connection box and the SY-124. If possible, test the cable with a cable tester or replace the cable.

SY-124 Diagram:

* Ensure the DC Power adapter is connected to the SY-124 properly and plugged in. The Red Power LED should illuminate.
* Ensure the AC Power source is connected properly and functioning.
* Ensure a straight through ethernet cable is used between the Omega terminal and the SY-124. If possible, test the cable with a cable tester or replace the cable.
* Ensure the AC Power source and Door Strike are wired to the proper relay contacts and to each other. One side of the AC power source should be connected to the Normally Closed contact while the other is connected to a contact on the door strike. The second contact of the door strike should be connected to the common contact of the relay.