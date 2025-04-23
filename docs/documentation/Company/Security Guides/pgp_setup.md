## PGP Encryption Configuration for InfiniTime

This document consolidates the steps to configure PGP encryption across all output types in InfiniTime, to avoid redundancy and streamline setup.

### 1. Enabling PGP

1. Open the **Export**, **Payroll Export**, or **Report** definition you wish to secure.
2. In the general options, check **PGP Encrypt File**.
3. Click **OK** or **Save** to enable PGP for that definition.

> _Once enabled, a **PGP** tab appears in the definition form. All key and passphrase settings are managed there._

---

### 2. PGP Setup (Common for All Outputs)

1. After enabling PGP, open the **PGP** tab in the definition form.
2. You will see fields for:
   - **PGP Public Key** (used to encrypt)
   - **PGP Signature Key** (used to sign)
   - **PGP Passphrase** (optional, for decrypting signed data)
3. To change any key or passphrase, click the **🔍** icon next to the field, select your file, and confirm.
4. If a field should be cleared, open it and hit **OK** on an empty file dialog.

---

### 3. PGP Modes

Choose one of the following levels of security when configuring your keys:

| Mode                           | Public Key Required | Private Key Required | Passphrase Required |
| ------------------------------ | ------------------- | -------------------- | ------------------- |
| **Encryption Only**            | Yes                 | No                   | No                  |
| **Encrypt & Sign**             | Yes                 | Yes                  | No                  |
| **Encrypt, Sign & Passphrase** | Yes                 | Yes                  | Yes                 |

1. **Encryption Only**: Clears the Signature Key and Passphrase fields.
2. **Encrypt & Sign**: Provide both Public and Signature Key files; leave Passphrase blank.
3. **Encrypt & Sign with Passphrase**: Provide all three fields for maximum security.

> **Important Security Note**: When choosing keys, consider the following:
>
> - Private keys should never be shared between different corporations or individuals
> - Anyone with access to a private key can impersonate the owner and decrypt files
> - Public keys can be freely distributed to intended recipients
> - While InfiniTime provides default keys, using company-specific keys offers better security as default keys are distributed to all InfiniTime 7 customers

---

### 4. Applying PGP to Output Types

For each output type, follow the standard definition process and refer back to **Section 2** for PGP setup.

#### 4.1. Payroll Export Files

- Enable PGP in the **Payroll Export** definition form.
- Configure FTP/email/export settings as usual.
- Go to **Section 2** to select keys and mode.
- Save and **Export**; files will be encrypted (and optionally signed) before delivery.

#### 4.2. General Export Files

- In **Export Definition**, check **PGP Encrypt File** on the **Source File Options** tab.
- Configure fields mapping and filters.
- Complete PGP key/passphrase setup via **Section 2**.
- Save and **Export**; encrypted file appears on InfiniTime FTP or is sent via FTP.

#### 4.3. Report Files

- In **Report Library**, insert or change a saved report criteria.
- On the **Options** or **General** tab, check **PGP Encrypt File** (and **Send via FTP** if required).
- Configure date ranges, filters, and formats.
- Apply keys/passphrase as in **Section 2**.
- Save and **Print** or **Export**; encrypted output is generated.

---

### 5. Tips & Best Practices

- **Key Management**: Keep private (signature) keys and passphrases secure—only share public keys.
- **Default Keys**: InfiniTime provides default keys for quick setup; consider replacing them with your organization's own for tighter control.
- **Testing**: After configuration, perform a test export to ensure you can decrypt on the recipient side.
- **Automation**: PGP settings persist in saved definitions and apply automatically whenever the definition runs.

### 6. Additional Resources

For more information about PGP and alternative PGP clients:

- International PGP Homepage: [www.pgpi.org](http://www.pgpi.org)
- PGP Desktop (30-day trial): [www.pgp.com](http://www.pgp.com)

> **Note**: Be sure to read the documentation supplied with your specific PGP client software, as different clients may support varying levels of security offered by the PGP algorithm.

---
