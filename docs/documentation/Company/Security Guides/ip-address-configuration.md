## Valid IP Addresses - Overview

InfiniTime Software Application access can be restricted by defining Valid IP Addresses. This security feature works as follows:

- When a user attempts to log in, their IP address is checked against two lists:
  1. Company-wide Valid IP Addresses
  2. Employee-specific Valid IP Addresses
- Access is granted only if the user's IP address matches either list
- If both lists are empty, access is allowed from any IP address

### Important Notes

- IP Address restrictions are separate from Security Roles
- IP restrictions control login access, while Security Roles control actions within the software
- An Administrator with full permissions will still be blocked if their IP address isn't authorized

### Login Validation Process

1. User must provide correct Login ID and Password
2. System checks the user's IP against Company-wide Valid IP Addresses
   - If match found or list is empty → proceed
   - If no match → access denied
3. System checks the user's IP against Employee-specific Valid IP Addresses
   - If match found or list is empty → access granted
   - If no match → access denied

### Configuration

#### Company-wide IP Addresses

1. Access the Manager Module as an Administrator
2. Navigate to Company settings
3. Select the Valid IP tab
4. Add or modify IP addresses as needed

#### Employee-specific IP Addresses

1. Open the Employee Table
2. Select the employee
3. Access their Login settings
4. Configure IP addresses in the Employee-specific Valid IP Address section

### IP Address Format

- IP addresses consist of four octets (e.g., 192.168.1.0)
- Each octet must be between 0 and 255
- Example format: 192.168.1.0
