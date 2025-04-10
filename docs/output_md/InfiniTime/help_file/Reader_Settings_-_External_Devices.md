xml version="1.0" encoding="utf-8"?





Reader Settings - External Devices




# Reader Settings - External Devices

The Thor Terminal provides support for external devices, such as Wiegand readers, USB Barcode Wand, Bells and Access Control, along with a printer

![](/img/image7.jpg)

The Thor Terminal provides support for external Wiegand Badge and Magnetic stripe Readers. The default settings on the External Device Settings Tab, as shown below, are compatible with the Proximity Reader and the Bar Code / Magnetic Stripe Combo Reader sold by Inception Technologies.

Note: Please contact your Authorized InfiniTime Dealer or Inception Technologies Sales Representative if you are interested in testing an external Wiegand Device for compatibility with the Thor Terminal.

![](/img/image445.gif)

Do not alter the required fields on the Wiegand Settings Tab (In Blue) without guidance from Inception Technologies or an Authorized InfiniTime Dealer. The Reader Communication Method defines how the Wiegand device interacts with the Thor terminal. In In-Line mode the Badge ID read from the external device will be shown on the Thor Display along with the employees punch status (In or Out). In-Line Mode is most useful for Time and Attendance Purposes. The secondary reader Communication Method 'Not In-Line' does not interact with the Thor Display which is generally used for Access Control Purposes.

# Wiegand Format

The wiegand format defines how the Thor interprets communication signals from external wiegand devices. The wiegand format is a string of letters composed of various characters which break down the communication signal received from external wiegand devices into significant information. Default wiegand formats supported by the Thor are listed below.

Wiegand String Characters

The following characters are used in the Wiegand Format String. Specifically, each character represents a bit in the data signal sent to the Thor from the external reader.

p:     Parity bit

s:     Site code

c:     Card number

f:      Facility code (Device ID)

e:     Even parity bit

o:     Odd parity bit

b:     Both even and odd parity bit

| Default Wiegand Format Strings | | |
| Bit Length | Wiegand Type | Wiegand Format |
| 26 | Wiegand26 | "pssssssssccccccccccccccccp:eeeeeeeeeeeeeooooooooooooo" |
| 34 | Wiegand34 | "pssssssssccccccccccccccccccccccccp:eeeeeeeeeeeeeeeeeooooooooooooooooo" |
| 36 | Wiegand36 | "pffffffffffffffffffccccccccccccccccp:eeeeeeeeeeeeeeeeeeoooooooooooooooooo" |
| 36 | Wiegand36a | "pffffffffffffffffccccccccccccccccmmp:ooooooooooooooooooeeeeeeeeeeeeeeeeee" |
| 37 | Wiegand37 | "pmmmffffffffffssssssccccccccccccccccp:eeeeeeeeeeeeeeeeeeooooooooooooooooooo" |
| 37 | Wiegand37a | "pmmmmsssssssssssscccccccccccccccccccp:oeobeobeobeobeobeobeobeobeobeobeobeoe" |
| 50 | Wiegand50 | "pssssssssssssssssccccccccccccccccccccccccccccccccp:eeeeeeeeeeeeeeeeeeeeeeeeeooooooooooooooooooooooooo" |