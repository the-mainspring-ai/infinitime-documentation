# Groups Introduction

InfiniTime Groups make
it possible to organize employees into different organization units such
as by building, by sub department or position, by floor, by city or by
state. This is accomplished by first creating a group level for each organizational
unit and then creating a group description for each possible value for
the respective organizational unit.  In this way, employees can then
be assigned to a specific group description for each group level. There
is no limit to the number of groups that may be configured within InfiniTime. When configuring groups
one group description per group level must be set as the default. The
default group description will automatically be assigned to all employees
for each group level. For additional information on using groups with
security filters and the default group function refer to the [Security
Filters Section of this document](../Security/Security_Overview.md#gro_Selected_Groups).

It is important to understand that employees cannot belong to two groups
within the same group level. For example, the image below shows two group
levels, Location and Division. An employee may belong to any one location
and any one division, but they cannot belong to two divisions.

![](/img/ColSel_Sel.gif)

Accessing
Groups

- Click on Lookups
- Click on Employee Setup
- Click on Groups

![](/img/OTA_20.png)

### Group Table

The Group Table displays all Group Levels and Group Descriptions configured
within InfiniTime. When
configuring groups, it is important to note that the Insert and Change
Buttons on the Group Table are context sensitive. If a Group Level is
selected, the Insert Button will open the Group Level Update form which
can be used to create a new Group Level. If a Group Description is selected,
the Insert Button will open the Group Update Form which can be used to
create a new Group Description for the respective Group Level. When a
Group Level is first created, 'None' will be displayed when the Group
Level is expanded. To insert the first group description for a Group Level,
expand the Group Level,  select the entry titled 'None', then click
Insert to open the Group Update Form. Additional details on how to assign
groups to employees can be found in the [Employee
Update Form Settings Tab](../ovr_SoftwareOverview.md#so167_Settings_Tab_-_Groups) and [Quick
Assign](Product_Configuration.md#qa04_Using_Quick_Assign) Sections of this document.

![](/img/JobCostingWages_1.gif)

Insert - Opens the Group Level
Update Form or the Group Update Form depending on the item selected on
the Group Table. As detailed above, If a Group Level is selected, the
Insert Button will open the Group Level Update form which can be used
to create a new Group Level. If a Group Description is selected, the Insert
Button will open the Group Update Form which can be used to create a new
Group Description for the respective Group Level.

![](/img/HoursMapping13.gif)

![](/img/hol34.png)

Change - Opens the Group Update
Form or Group Level Update Form as appropriate for the selected item.
The InfiniTime Administrator
may then alter the Group Level or Group Description as desired.

Delete - Deletes the selected
Group Description or Group Level from the Group Table. All employees assigned
to a Group Description that is deleted will be assigned to the Default
Group Description for the respective group level.
