---
title: "Customizable InfiniTime Grid"
description: "Overview of the customizable grid system in InfiniTime for organized and flexible data display."
---

Customizable Table Display: The InfiniTime Grid

# Customizable Table Display: The InfiniTime Grid

InfiniTime uses a grid system to display information in an organized, structured, and standardized fashion. Each table and list is presented in a similar layout with the InfiniTime Grid as the major build block. Use of a grid system helps keep information accessible and orderly regardless of database size through the use of various features such as the ability to filter items based on a search term.

The InfiniTime Grid is fully customizable and can be tailored to meet user needs. Each window stores a set of configuration settings allowing the user to customize each window individually.

![](/img/ColSel_Rem.gif)

The image above, taken from the Employee Table, shows how Grid Controls and a Search Field are displayed above the grid. Headings appear atop each grid column to describe the information below. This document uses the Employee Table as an example, though it should be noted that the grid controls are displayed on every table where the grid is used.

Click on each control below for more information about its uses. Page controls are gray when there are no available pages in that direction. Once multiple pages are available the controls will become active and turn blue.

Technical Note: Some grid buttons may not be available depending on your browser. Firefox for example does not support clipboard access or printing from InfiniTIme.

![](/img/DropDown.gif)

First Page  ![](/img/CSVSave.gif).gif)

Updates the grid with the first page of records. Page 1 will be displayed in the current page drop down box.

Previous Page ![](/img/Added.gif).gif)

Updates the grid with records from the previous page and decreases the page number in the current page drop down box by one.

Current Page ![](/img/Added.gif).gif)

Provides a drop down box that can be used to select the page you wish to view. Also displays the current page. Viewing a different page can be accomplished by clicking on the drop down tab and selecting the individual page you wish to view.

The total amount of pages is displayed on the right. This value is updated automatically as additional records are added to the database. When the number of records exceeds a preset record per page limit then a new page is created. The number of records displayed per page can be configured in the Grid Configuration Window.

Next Page ![](/img/XMLSaveWindow.gif).gif)

Updates the grid with records from the next page and increases the page number in the current page drop down box by one.

Last Page ![](/img/GridTools.gif).gif)

Updates the grid with records from the last page and displays the final page number in the current page drop down box.

Total Rows ![](/img/WordDoc.gif).gif)

Displays the total number of rows, or records, in the grid. This number is updated automatically as records are added and removed.

Save Grid Results ![](/img/ColSel_Sel.gif).gif)

Users have the option of saving all records displayed in the InfiniTime Grid in any one of five formats. To save the grid, select your preferred format from the drop down box and click the Save Grid Results icon. Specific instructions are provided by format below. Should the grid contain multiple pages of information records on each page will append to the end of the document after those from the previous pages. The end result is a single document with all records in the grid.

HTML

Grid Results are immediately saved in an HTML format on the InfiniTime server. The file is automatically opened on your machine in your default web browser. Results can then be printed or saved using your web browserâs interface.

To save the results:

1. Click on File.
2. Click on Save or Save As.
3. Browse to the desired location on your computer.
4. Enter a file name.
5. Click Save.

_Technical Note_: Internet Explorer 7.0 may alert you that it is possible for the page to not save correctly. Click OK. There should be no complications with saving the grid results as long as the file is saved with the .htm or .html extensions. The default file name when saving in the HTML format is dbnetgrid_aspx.html and can be changed at the users discretion as long as the extension is not altered.

WORD

Grid Results are immediately saved in a Microsoft Word format on the InfiniTime server. The file is automatically opened on your machine in your default web browser. Results can then be printed or saved using your web browserâs interface.

To save the results:

1. Click on File.

![](/img/griddef.gif)

2. Click on Save or Save as.

![](/img/ColSel_Down.gif)

3. Browse to the desired location on your computer.
4. Enter a file name.
5. Click on the Save as type Drop down box

![](/img/AddLname.gif)

6. Select Word Document from the list

![](/img/GridTools.gif)

7. Click Save.

![](/img/ColSel_Up.gif)

The default name for Word Documents is dbnetgrid. This can be changed at the users discretion.

Excel

Grid Results are immediately saved in a Microsoft Word format on the InfiniTime server. The file is automatically opened on your machine in your default web browser. Results can then be printed or saved using your web browserâs interface.

To save the results:

1. Click on File.

![](/img/CSVSaveWindow.gif)

2. Click on Save or Save as.

![](/img/ExcelWkBk.gif)

3. Browse to the desired location on your computer.
4. Enter a file name.
5. Click on the Save as type Drop down box

![](/img/AddLname.gif)

6. Select Microsoft Excel Workbook from the list

![](/img/Type.gif)

7. Click Save.

![](/img/ColSel_Up.gif)

Excel Documents do not have a file name entered by default. Users must enter a file name before saving the file.

XML

Grid Results are immediately saved in an XML format on the InfiniTime server. The file is automatically opened on your machine in your default web browser. Results can then be printed or saved using your web browserâs interface.

To save the results:

1. Click on File.

![](/img/Type.gif)

2. Click on Save or Save as.

![](/img/CSVDoc.gif)

3. Browse to the desired location on your computer.
4. Enter a file name.
5. Click on the Save as type Drop down box

![](/img/GridSort.gif)

6. Select XML Files from the list.

![](/img/SaveWindow.gif)

7. Click Save.

![](/img/WordDoc.gif)

CSV

Grid Results are immediately saved in a CSV format on the InfiniTime server. The file is automatically opened on your machine in your default web browser. Results can then be printed or saved using your web browserâs interface.

To save the results:

1. Click on File.

![](/img/griddef.gif)

2. Click on Save or Save as.

![](/img/DataCopied.gif)

3. Browse to the desired location on your computer.
4. Enter a file name. The .csv extension must be added to the end of the filename in order to save the file in the csv format.

![](/img/XMLType.gif)

5. Click on the Save as type Drop down box

![](/img/ColSel_Sel.gif)

6. Select Unicode Text from the list.

![](/img/ExcelSave.gif)

7. Click Save.

![](/img/ColSel_Down.gif)

The default name for CSV Files is dbnetgrid. This can be changed at the users discretion.

_Technical Note_: You may be prompted that the document contains features that are not compatible with Unicode Text. Save the file anyway, as by typing the .csv extension the file is automatically saved in a comma-delimited format.

_Technical Note_: Comma Delimited Files generated by InfiniTime should be opened for viewing with Excel or Wordpad.

Print Grid Results ![](/img/ExcelWkBk.gif).gif)

Displays the default windows printer selection window allowing you to choose from local printers to print grid results directly.

Copy Grid to Clipboard ![](/img/CSVDoc.gif).gif)

Places all grid results in the clipboard in a table form. The table can be pasted to any graphic or word editor. Keep in mind the table format may vary depending on the features supported by your word editor. For example, Notepad is unable to display a graphical table and will simply separate items with spaces.

Once the grid results are successfully copied the following image is displayed:

![](/img/XMLSave.gif)

Select Grid Columns ![](/img/CSVSave.gif).gif)

Gives users the ability to choose which columns will be displayed in the grid. For example, many companies will not want the Social Security number to be visible. This field can be removed from the grid with this feature.

The Grid Column Selection Window provides four interactive buttons as described below. These buttons are used to add and remove columns from the grid and can also alter column order.

![](/img/Clicksave.gif)  Moves highlighted records in the âSelectedâ list up. This has the effect of moving the column to the left on the grid itself.

![](/img/Grid.gif)  Moves highlighted records in the âSelectedâ list down. This has the effect of moving the column to the right on the grid itself.

![](/img/Clicksave.gif)  Moves highlighted records in the âAvailableâ list to the âSelectedâ list, effectively adding the item as a new column on the grid.

![](/img/SaveAs.gif)  Moves highlighted records in the âSelectedâ list to the âAvailableâ list, effectively removing the column from the grid.

Restores Grid Defaults ![](/img/CSVFileName.gif).gif)

Restores the default grid column configuration.

Specify Nested Order Levels ![](/img/CSVSaveWindow.gif).gif)

Provides users the option of altering the order by which records are displayed in the grid. Records can be displayed by alphabetical or numeric order by single or multiple fields.

![](/img/DataCopied.gif)

Configuring Grid Display Order:

Highlight the item desired from the Sort Columns List.

![](/img/Grid.gif)

Click Add.

The item will be added to the sequence on the right side of the page as shown.

![](/img/CSVType.gif)

Use the drop down box to choose between ascending or descending order.

![](/img/DropDown.gif)

Order levels are performed in priority. Ordering levels at the top of the sequence take precedence over those at the bottom. Level 1 has the highest priority. Items can be removed from the sequence by clicking delete.

_Note_: Only those columns that are displayed by the grid, as chosen during Grid column configuration, will be available for sorting purposes.

Reset Grid Default Sort ![](/img/ExcelSave.gif).gif)

Restores the default grid sorting configuration.

Grid Configuration Window ![](/img/GridSort.gif).gif)

Grid Security ![](/img/CSVFileName.gif).gif)

Grid Security, combined with Security Roles, allow the Software Administrator to configure InfiniTime down to the exact button. Each employee is assigned an employee role. When the employee signs into the software with their login ID the software recognizes the employee role they have been assigned and grants or denies access to the software based on those rights. Window access is controlled by Security Roles, while Grid Security is responsible for button access

Two options are provided for button security, Hidden and Normal. Normal displays the button and permits interaction. Hidden removes the button from view, effectively removing access to that portion of the software.

Each security role has a unique set of button security settings. Be sure to configure Grid Security for each role based on your companyâs unique access requirements.

Configuring Grid Security:

1. Select the security role you wish to configure.
2. Select appropriate settings for each button.

![](/img/XMLSave.gif) Resets default security configuration settings for the selected security role.
