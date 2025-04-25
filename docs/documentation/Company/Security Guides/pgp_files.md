---
title: ""
description: ""
---

# PGP Encryption for InfiniTime Reports

This document provides specific instructions for using PGP encryption with different output methods in InfiniTime. For general PGP configuration and setup, refer to the [PGP Setup Guide](pgp_setup.md).

## Output Methods Overview

InfiniTime offers three methods for delivering PGP-encrypted reports:

1. **Email Delivery**: Send encrypted reports directly to recipients via email
2. **FTP Delivery**: Upload encrypted reports to a remote FTP server
3. **InfiniTime FTP Output**: Make encrypted reports available for download from the InfiniTime FTP site

Each method has specific configuration steps while sharing common PGP setup procedures.

## 1. Email Delivery

InfiniTime can email report files in PDF, Excel, Word, and Rich Text formats with PGP encryption. Reports can be sent to single or multiple recipients, and can be configured for automatic delivery at specific times (see Chapter 10 - Auto Reports).

### Email-Specific Configuration Steps

1. Highlight the report you wish to export and click Insert.

2. On the general tab:

   - Set Print Preview as desired
   - Enter an export file name to enable export options
   - Select the appropriate file format
   - Check "PGP encrypt file"

3. The PGP tab will become available. For PGP key configuration, refer to [PGP Setup Guide](pgp_setup.md#2-pgp-setup-common-for-all-outputs).

4. Configure the email settings:

   - Add destination address(es)
   - Set from address
   - Enter subject and body

5. Configure the Report criteria (date range, employee filter, etc.)

6. Save the Report Selection Criteria by clicking OK.

7. Highlight the Saved Report Criteria and click Print.

8. Review and close the print preview if applicable, then click Yes to email when prompted.

The encrypted report will be automatically emailed to the specified recipient(s).

## 2. FTP Delivery

To decrease the likelihood of unauthorized access to encrypted report files, InfiniTime can place the files directly on an FTP site.

### FTP-Specific Configuration Steps

1. In the Report Library, highlight the report you wish to export in an encrypted PGP format.

2. Click Insert.

3. On the general tab:

   - Set Print Preview as desired
   - Enter an export file name
   - Check both **PGP encrypt file** and **Send File Via FTP**

4. Configure the FTP connection details:

   - Host address (without ftp:// prefix)
   - Username and password
   - Port number
   - Directory path

   > **Important FTP Path Notes**:
   >
   > - No trailing backslash (\) required for the directory
   > - No trailing back (\) or forward (/) slashes required for the host address
   > - A backslash (\) is required between directory levels (e.g., 'Public\upload')

5. Configure the PGP settings by following the [PGP Setup Guide](pgp_setup.md#2-pgp-setup-common-for-all-outputs).

6. Configure the Report parameters:

   - Set the date range
   - Configure employee filters
   - Enable any desired options

7. Save the Report Selection Criteria by clicking OK.

8. To generate and send the report:
   - Highlight the Saved Report Criteria in the Payroll Export Table
   - Click Print
   - Review and close the print preview if applicable
   - Click Yes to send the report via FTP when prompted

### FTP Troubleshooting

If you experience difficulties sending a Payroll Export via FTP, verify:

- FTP login credentials
- Port number
- Directory path
- Host address

For PGP-related issues, refer to the [PGP Setup Guide](pgp_setup.md#5-tips--best-practices).

## 3. InfiniTime FTP Output

When it is not desirable to send a Report via Email or FTP, the file can be made available for download from the InfiniTime Output FTP site in a secure format.

> **Security Note**: Anyone with internet access who knows the web address used to access the FTP site can access it if InfiniTime has been published to the internet. This could permit unauthorized users to access report files. Users should retrieve encrypted files immediately from the InfiniTime Output FTP Site and delete them from the public FTP site afterwards.

### InfiniTime FTP Output Configuration Steps

1. Highlight the report you wish to export in an encrypted PGP format.

2. Click Insert.

3. On the general tab:

   - Set Print Preview as desired
   - Enter an export file name to enable export options
   - Select the appropriate file format
   - Check "PGP encrypt file"

4. The PGP tab will become available. For PGP key configuration, refer to [PGP Setup Guide](pgp_setup.md#2-pgp-setup-common-for-all-outputs).

5. Configure the Report parameters:

   - Set the date range
   - Configure employee filters
   - Enable any desired options

6. Save the Report Selection Criteria by clicking OK.

7. Highlight the Saved Report Criteria in the Saved Report Selection Criteria section of the Report Library and click Print.

8. Review and close the print preview if applicable, then click Yes to export when prompted.

9. The file will be available for download from the InfiniTime FTP Output in the encrypted PGP format.

## Visual Guides

For visual guidance on the PGP configuration process, refer to the following screenshots:

- [Report Selection](img/Ch2_ValidIP_EmployeeButton.jpg)
- [Insert Dialog](img/ValidIP_BlockedRemSites.jpg)
- [General Tab Options](img/ValidIP_OnsiteDept.jpg)
- [Export Options](img/CH2_PGP12.gif)
- [PGP Encryption Option](img/Sec007.png)
- [PGP Tab](img/Sec009.png)
- [PGP Configuration](img/Sec015.png)
- [Save Dialog](img/WhatisMyIP.jpg)
- [Print Dialog](img/ChangePW.jpg)
- [Export Confirmation](img/CH2_PGP37.gif)

---

## PGP Encryption for Payroll Export Files

For detailed instructions on configuring PGP encryption for Payroll Export files, refer to the [PGP Setup Guide](pgp_setup.md#41-payroll-export-files).

## PGP Encryption for General Export Files

For detailed instructions on configuring PGP encryption for General Export files, refer to the [PGP Setup Guide](pgp_setup.md#42-general-export-files).

## Troubleshooting Email Delivery

If you experience difficulties when attempting to email a Payroll Export, verify the following:

- The InfiniTime Server must have an active Internet connection
- Power Management must be disabled on the Network Interface Card of the InfiniTime Server
- The InfiniTime Housekeeping Service must be started and running
- The InfiniTime Server does not need to have a user logged into the console, but must be powered on and idle at the Windows Login Splash Screen
- A printer must be installed and set as the default printer on the InfiniTime Server
- The Print Spooler Service must be started and running on the InfiniTime Server
- Your fully qualified domain name may need to be configured in the advanced delivery options of the SMTP Virtual Server created by InfiniTime depending on your domain policies
- An auto schedule must be configured within a saved report setting
- A destination name and email address must be defined on the email tab of the saved report setting

For additional troubleshooting information, refer to the [PGP Setup Guide](pgp_setup.md#5-tips--best-practices).
