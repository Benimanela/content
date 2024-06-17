Manage secrets and protect sensitive data through Thales CipherTrust security platform.
This integration was integrated and tested with version xx of CipherTrust.

## Configure Thales CipherTrust Manager on Cortex XSOAR

1. Navigate to **Settings** > **Integrations** > **Servers & Services**.
2. Search for Thales CipherTrust Manager.
3. Click **Add instance** to create and configure a new integration instance.

    | **Parameter** | **Required** |
    | --- | --- |
    | Server URL | True |
    | Username | True |
    | Password | True |
    | Trust any certificate (not secure) | False |
    | Use system proxy settings | False |

4. Click **Test** to validate the URLs, token, and connection.

## Commands

You can execute these commands from the Cortex XSOAR CLI, as part of an automation, or in a playbook.
After you successfully execute a command, a DBot message appears in the War Room with the command details.

### ciphertrust-csr-generate

***
Creates a Certificate Signing Request (CSR) and its corresponding private key. This API does not store any state on the server as everything is returned in the result. This means that both the CSR and the private key must be stored securely on the client side. The private key can optionally be encrypted with a password. It is strongly recommended to encrypt the private key. If not specified, the private_key_file_password is mandatory and the file itself is protected with the password even if the private key is not encrypted.

#### Base Command

`ciphertrust-csr-generate`

#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| cn | Common Name. | Required | 
| algorithm | RSA or ECDSA (default) algorithms are supported. A signature algorithm (SHA512WithRSA, SHA384WithRSA, SHA256WithRSA, SHA1WithRSA, ECDSAWithSHA512, ECDSAWithSHA384, ECDSAWithSHA256) is selected based on the algorithm and size. Possible values are: RSA, ECDSA. | Optional | 
| dns_names | A comma-separated list of Subject Alternative Names (SAN) values. | Optional | 
| email | A comma-separated list of e-mail addresses. | Optional | 
| ip | A comma-separated list of IP addresses. | Optional | 
| name | A unique name of the CSR. | Optional | 
| encryption_algo | Private key encryption algorithm. Possible values are: AES256, AES192, AES128, TDES. | Optional | 
| name_fields_raw_json | Name fields are "O=organization, OU=organizational unit, L=location, ST=state/province, C=country". Fields can be duplicated if present in different objects. This is a raw json string, for example: "[{"O": "Thales", "OU": "RnD", "C": "US", "ST": "MD", "L": "Belcamp"}, {"OU": "Thales Group Inc."}]". | Optional | 
| name_fields_json_entry_id | Entry ID of the file that contains the JSON representation of the name_fields_raw_json. | Optional | 
| key_size | Key size. RSA: 1024 - 4096 (default: 2048), ECDSA: 256 (default), 384, 521. Possible values are: 1024, 2048, 3072, 4096, 256, 384, 521. | Optional | 
| encryption_password | Password to PEM-encrypt the private key. If not specified, the private key is not encrypted in return. It is strongly recommended to encrypt the private key. If not specified, the private_key_file_password is mandatory. | Optional | 
| private_key_file_password | Password to encrypt the private key file. It is strongly recommended to encrypt the private key. If not specified, the private key is encrypted with the password which must be provided. | Optional | 
| private_key_bytes | Private Key bytes of the key which is to be used while creating CSR. (The algorithm and size should be according to this key). If not given will generate key internally as per algorithm and size. | Optional | 

#### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| InfoFile.Name | string | File name. | 
| InfoFile.EntryID | string | The entry ID of the report. | 
| InfoFile.Size | number | File size. | 
| InfoFile.Type | string | File type, e.g., "PE". | 
| InfoFile.Info | string | Basic information of the file. | 
| InfoFile.Extension | string | File extension. | 

### ciphertrust-certificate-issue

***
Issues a certificate by signing the provided CSR with the CA. This is typically used to issue server, client or intermediate CA certificates. Either duration or not_after date must be specified. If both not_after date and duration are given, then not_after takes precedence over duration. If duration is given without not_before date, ceritificate is issued starting from server's current time for the specified duration.

#### Base Command

`ciphertrust-certificate-issue`

#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| ca_id | An identifier of the issuer CA resource. This can be either the ID (a UUIDv4), the name, the URI, or the slug (which is the last component of the URI). | Required | 
| csr_entry_id | The entry ID of the file to upload that contains CSR in PEM format. | Required | 
| purpose | Purpose of the certificate. Possible values are: server, client, ca. | Required | 
| duration | Duration in days of certificate. Either duration or not_after date must be specified. Default is 365. | Optional | 
| name | A unique name of the certificate. If not provided, will be set to cert-&lt;id&gt;. | Optional | 
| not_after | End date of certificate. Either not_after date or duration must be specified. not_after overrides duration if both are given. | Optional | 
| not_before | Start date of the certificate. | Optional | 

#### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| InfoFile.Name | string | File name. | 
| InfoFile.EntryID | string | The entry ID of the report. | 
| InfoFile.Size | number | File size. | 
| InfoFile.Type | string | File type, e.g., "PE". | 
| InfoFile.Info | string | Basic information of the file. | 
| InfoFile.Extension | string | File extension. | 
| CipherTrust.CACertificate.id | String | A unique identifier for the certificate authority \(CA\). | 
| CipherTrust.CACertificate.uri | String | Uniform Resource Identifier associated with the CA. | 
| CipherTrust.CACertificate.account | String | Account associated with the CA. | 
| CipherTrust.CACertificate.application | String | Application associated with the CA. | 
| CipherTrust.CACertificate.devAccount | String | Developer account associated with the CA. | 
| CipherTrust.CACertificate.name | String | Name of the CA. | 
| CipherTrust.CACertificate.state | String | Current state of the CA \(e.g., active, pending\). | 
| CipherTrust.CACertificate.createdAt | Date | Timestamp of when the CA was created. | 
| CipherTrust.CACertificate.updatedAt | Date | Timestamp of the last update of the CA. | 
| CipherTrust.CACertificate.serialNumber | String | Serial number of the CA's certificate. | 
| CipherTrust.CACertificate.subject | String | Subject of the CA's certificate. | 
| CipherTrust.CACertificate.issuer | String | Issuer of the CA's certificate. | 
| CipherTrust.CACertificate.ca | String | Certificate authority. | 
| CipherTrust.CACertificate.revoked_at | String | Revocation timestamp. | 
| CipherTrust.CACertificate.sha1Fingerprint | String | SHA1 fingerprint of the certificate. | 
| CipherTrust.CACertificate.sha256Fingerprint | String | SHA256 fingerprint of the certificate. | 
| CipherTrust.CACertificate.sha512Fingerprint | String | SHA512 fingerprint of the certificate. | 
| CipherTrust.CACertificate.notBefore | Date | Timestamp of when the certificate is valid from. | 
| CipherTrust.CACertificate.notAfter | Date | Timestamp of when the certificate is valid until. | 

### ciphertrust-certificate-list

***
Returns a list of certificates issued by the specified CA. The results can be filtered, using the command arguments.

#### Base Command

`ciphertrust-certificate-list`

#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| ca_id | An identifier of the issuer CA resource. This can be either the ID (a UUIDv4), the name, the URI, or the slug (which is the last component of the URI). | Required | 
| subject | Filter by the subject. | Optional | 
| issuer | Filter by the issuer. | Optional | 
| cert | Filter by the cert. | Optional | 
| id | Filter by ID or URI. | Optional | 
| page | Page to return. | Optional | 
| page_size | Number of entries per page. Defaults to 2000 (in case only page was provided). Maximum entries per page is 2000. | Optional | 
| limit | The maximum number of entries to return. Default is 50. | Optional | 

#### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| CipherTrust.CACertificate.name | String | The name of the certificate. | 
| CipherTrust.CACertificate.id | String | A unique identifier for the certificate. | 
| CipherTrust.CACertificate.uri | String | Uniform Resource Identifier associated with the certificate. | 
| CipherTrust.CACertificate.account | String | Account associated with the certificate. | 
| CipherTrust.CACertificate.application | String | Application associated with the certificate. | 
| CipherTrust.CACertificate.devAccount | String | Developer account associated with the certificate. | 
| CipherTrust.CACertificate.createdAt | Date | Timestamp of when the certificate was created. | 
| CipherTrust.CACertificate.updatedAt | Date | Timestamp of the last update of the certificate. | 
| CipherTrust.CACertificate.ca | String | Certificate authority. | 
| CipherTrust.CACertificate.revoked_at | String | Revocation timestamp. | 
| CipherTrust.CACertificate.sha1Fingerprint | String | SHA1 fingerprint of the certificate. | 
| CipherTrust.CACertificate.sha256Fingerprint | String | SHA256 fingerprint of the certificate. | 
| CipherTrust.CACertificate.sha512Fingerprint | String | SHA512 fingerprint of the certificate. | 
| CipherTrust.CACertificate.serialNumber | String | Serial number of the certificate. | 
| CipherTrust.CACertificate.subject | String | Subject of the certificate. | 
| CipherTrust.CACertificate.issuer | String | Issuer of the certificate. | 
| CipherTrust.CACertificate.notBefore | Date | Timestamp of when the certificate is valid from. | 
| CipherTrust.CACertificate.notAfter | Date | Timestamp of when the certificate is valid until. | 

### ciphertrust-certificate-resume

***
Certificate can be resumed only if it is revoked with reason certificateHold.

#### Base Command

`ciphertrust-certificate-resume`

#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| ca_id | An identifier of the issuer CA resource. This can be either the ID (a UUIDv4), the name, the URI, or the slug (which is the last component of the URI). | Required | 
| cert_id | An identifier of the certificate resource. This can be either the ID (a UUIDv4), the URI, or the slug (which is the last component of the URI). | Required | 

#### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| InfoFile.Name | string | File name. | 
| InfoFile.EntryID | string | The entry ID of the report. | 
| InfoFile.Size | number | File size. | 
| InfoFile.Type | string | File type, e.g., "PE". | 
| InfoFile.Info | string | Basic information of the file. | 
| InfoFile.Extension | string | File extension. | 
| CipherTrust.CACertificate.name | String | The name of the certificate. | 
| CipherTrust.CACertificate.id | String | A unique identifier for the certificate. | 
| CipherTrust.CACertificate.uri | String | Uniform Resource Identifier associated with the certificate. | 
| CipherTrust.CACertificate.account | String | Account associated with the certificate. | 
| CipherTrust.CACertificate.application | String | Application associated with the certificate. | 
| CipherTrust.CACertificate.devAccount | String | Developer account associated with the certificate. | 
| CipherTrust.CACertificate.createdAt | Date | Timestamp of when the certificate was created. | 
| CipherTrust.CACertificate.updatedAt | Date | Timestamp of the last update of the certificate. | 
| CipherTrust.CACertificate.ca | String | Certificate authority. | 
| CipherTrust.CACertificate.revoked_at | Date | Revocation timestamp. | 
| CipherTrust.CACertificate.state | String | Current state of the certificate \(e.g., active, revoked\). | 
| CipherTrust.CACertificate.sha1Fingerprint | String | SHA1 fingerprint of the certificate. | 
| CipherTrust.CACertificate.sha256Fingerprint | String | SHA256 fingerprint of the certificate. | 
| CipherTrust.CACertificate.sha512Fingerprint | String | SHA512 fingerprint of the certificate. | 
| CipherTrust.CACertificate.serialNumber | String | Serial number of the certificate. | 
| CipherTrust.CACertificate.subject | String | Subject of the certificate. | 
| CipherTrust.CACertificate.issuer | String | Issuer of the certificate. | 
| CipherTrust.CACertificate.notBefore | Date | Timestamp of when the certificate is valid from. | 
| CipherTrust.CACertificate.notAfter | Date | Timestamp of when the certificate is valid until. | 

### ciphertrust-certificate-revoke

***
Revoke certificate with a given specific reason.

#### Base Command

`ciphertrust-certificate-revoke`

#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| ca_id | An identifier of the issuer CA resource. This can be either the ID (a UUIDv4), the name, the URI, or the slug (which is the last component of the URI). | Required | 
| cert_id | An identifier of the certificate resource. This can be either the ID (a UUIDv4), the URI, or the slug (which is the last component of the URI). | Required | 
| reason | Specify one of the reasons to revoke a certificate according to RFC 5280. Possible values are: unspecified, keyCompromise, cACompromise, affiliationChanged, superseded, cessationOfOperation, certificateHold, removeFromCRL, privilegeWithdrawn, aACompromise. | Required | 

#### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| InfoFile.Name | string | File name. | 
| InfoFile.EntryID | string | The entry ID of the report. | 
| InfoFile.Size | number | File size. | 
| InfoFile.Type | string | File type, e.g., "PE". | 
| InfoFile.Info | string | Basic information of the file. | 
| InfoFile.Extension | string | File extension. | 
| CipherTrust.CACertificate.name | String | The name of the certificate. | 
| CipherTrust.CACertificate.id | String | A unique identifier for the certificate. | 
| CipherTrust.CACertificate.uri | String | Uniform Resource Identifier associated with the certificate. | 
| CipherTrust.CACertificate.account | String | Account associated with the certificate. | 
| CipherTrust.CACertificate.application | String | Application associated with the certificate. | 
| CipherTrust.CACertificate.devAccount | String | Developer account associated with the certificate. | 
| CipherTrust.CACertificate.createdAt | Date | Timestamp of when the certificate was created. | 
| CipherTrust.CACertificate.updatedAt | Date | Timestamp of the last update of the certificate. | 
| CipherTrust.CACertificate.ca | String | Certificate authority. | 
| CipherTrust.CACertificate.revoked_at | Date | Revocation timestamp. | 
| CipherTrust.CACertificate.revoked_reason | String | Reason for revocation. | 
| CipherTrust.CACertificate.state | String | Current state of the certificate \(e.g., active, revoked\). | 
| CipherTrust.CACertificate.sha1Fingerprint | String | SHA1 fingerprint of the certificate. | 
| CipherTrust.CACertificate.sha256Fingerprint | String | SHA256 fingerprint of the certificate. | 
| CipherTrust.CACertificate.sha512Fingerprint | String | SHA512 fingerprint of the certificate. | 
| CipherTrust.CACertificate.serialNumber | String | Serial number of the certificate. | 
| CipherTrust.CACertificate.subject | String | Subject of the certificate. | 
| CipherTrust.CACertificate.issuer | String | Issuer of the certificate. | 
| CipherTrust.CACertificate.notBefore | Date | Timestamp of when the certificate is valid from. | 
| CipherTrust.CACertificate.notAfter | Date | Timestamp of when the certificate is valid until. | 

### ciphertrust-external-ca-delete

***
Deletes an external CA certificate.

#### Base Command

`ciphertrust-external-ca-delete`

#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| external_ca_id | An identifier of the resource. This can be either the ID (a UUIDv4), the Name, the URI, or the slug (which is the last component of the URI). | Required | 

#### Context Output

There is no context output for this command.
### ciphertrust-external-ca-list

***
Returns a list of external CA certificates. The results can be filtered, using the command arguments.

#### Base Command

`ciphertrust-external-ca-list`

#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| external_ca_id | An identifier of the resource. This can be either the ID (a UUIDv4), the name, the URI, or the slug (which is the last component of the URI). | Optional | 
| subject | Filter by the subject. | Optional | 
| issuer | Filter by the issuer. | Optional | 
| serial_number | Filter by the serial number. | Optional | 
| cert | Filter by the cert. | Optional | 
| page | Page to return. | Optional | 
| page_size | Number of entries per page. Defaults to 2000 (in case only page was provided). Maximum entries per page is 2000. | Optional | 
| limit | The maximum number of entries to return. Default is 50. | Optional | 

#### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| InfoFile.Name | string | File name. | 
| InfoFile.EntryID | string | The entry ID of the report. | 
| InfoFile.Size | number | File size. | 
| InfoFile.Type | string | File type, e.g. ,"PE". | 
| InfoFile.Info | string | Basic information of the file. | 
| InfoFile.Extension | string | File extension. | 
| CipherTrust.ExternalCA.id | String | A unique identifier for the certificate authority \(CA\) certificate. | 
| CipherTrust.ExternalCA.uri | String | Uniform Resource Identifier associated with the CA certificate. | 
| CipherTrust.ExternalCA.account | String | Account associated with the CA certificate. | 
| CipherTrust.ExternalCA.devAccount | String | Developer account associated with the CA certificate. | 
| CipherTrust.ExternalCA.application | String | Application associated with the CA certificate. | 
| CipherTrust.ExternalCA.createdAt | Date | Timestamp of when the CA certificate was created. | 
| CipherTrust.ExternalCA.updatedAt | Date | Timestamp of the last update of the CA certificate. | 
| CipherTrust.ExternalCA.name | String | Name of the CA certificate. | 
| CipherTrust.ExternalCA.purpose.client_authentication | String | If set to enabled, the certificates signed by the specified CA can be used for client authentication. | 
| CipherTrust.ExternalCA.purpose.user_authentication | String | If set to enabled, the certificates signed by the specified CA can be used for user authentication. | 
| CipherTrust.ExternalCA.serialNumber | String | Serial number of the CA certificate. | 
| CipherTrust.ExternalCA.subject | String | Subject of the CA certificate. | 
| CipherTrust.ExternalCA.issuer | String | Issuer of the CA certificate. | 
| CipherTrust.ExternalCA.notBefore | Date | Timestamp of when the CA certificate is valid from. | 
| CipherTrust.ExternalCA.notAfter | Date | Timestamp of when the CA certificate is valid until. | 
| CipherTrust.ExternalCA.sha1Fingerprint | String | SHA1 fingerprint of the CA certificate. | 
| CipherTrust.ExternalCA.sha256Fingerprint | String | SHA256 fingerprint of the CA certificate. | 
| CipherTrust.ExternalCA.sha512Fingerprint | String | SHA512 fingerprint of the CA certificate. | 

### ciphertrust-external-ca-update

***
Update an external CA.

#### Base Command

`ciphertrust-external-ca-update`

#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| external_ca_id | An identifier of the resource. This can be either the ID (a UUIDv4), the name, the URI, or the slug (which is the last component of the URI). | Required | 
| allow_client_authentication | If set to true, the certificates signed by the specified CA can be used for client authentication. Possible values are: true, false. | Optional | 
| allow_user_authentication | If set to true, the certificates signed by the specified CA can be used for user authentication. Possible values are: true, false. | Optional | 

#### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| InfoFile.Name | string | File name. | 
| InfoFile.EntryID | string | The entry ID of the report. | 
| InfoFile.Size | number | File size. | 
| InfoFile.Type | string | File type, e.g., "PE". | 
| InfoFile.Info | string | Basic information of the file. | 
| InfoFile.Extension | string | File extension. | 
| CipherTrust.ExternalCA.id | String | A unique identifier for the certificate authority \(CA\) certificate. | 
| CipherTrust.ExternalCA.uri | String | Uniform Resource Identifier associated with the CA certificate. | 
| CipherTrust.ExternalCA.account | String | Account associated with the CA certificate. | 
| CipherTrust.ExternalCA.devAccount | String | Developer account associated with the CA certificate. | 
| CipherTrust.ExternalCA.application | String | Application associated with the CA certificate. | 
| CipherTrust.ExternalCA.createdAt | Date | Timestamp of when the CA certificate was created. | 
| CipherTrust.ExternalCA.updatedAt | Date | Timestamp of the last update of the CA certificate. | 
| CipherTrust.ExternalCA.name | String | Name of the CA certificate. | 
| CipherTrust.ExternalCA.purpose.client_authentication | String | If set to enabled, the certificates signed by the specified CA can be used for client authentication. | 
| CipherTrust.ExternalCA.purpose.user_authentication | String | If set to enabled, the certificates signed by the specified CA can be used for user authentication. | 
| CipherTrust.ExternalCA.serialNumber | String | Serial number of the CA certificate. | 
| CipherTrust.ExternalCA.subject | String | Subject of the CA certificate. | 
| CipherTrust.ExternalCA.issuer | String | Issuer of the CA certificate. | 
| CipherTrust.ExternalCA.notBefore | Date | Timestamp of when the CA certificate is valid from. | 
| CipherTrust.ExternalCA.notAfter | Date | Timestamp of when the CA certificate is valid until. | 
| CipherTrust.ExternalCA.sha1Fingerprint | String | SHA1 fingerprint of the CA certificate. | 
| CipherTrust.ExternalCA.sha256Fingerprint | String | SHA256 fingerprint of the CA certificate. | 
| CipherTrust.ExternalCA.sha512Fingerprint | String | SHA512 fingerprint of the CA certificate. | 

### ciphertrust-external-ca-upload

***
Uploads an external CA certificate. These certificates can later be trusted by services inside the system for verification of client certificates. The uploaded certificate must have "CA:TRUE" as part of the "X509v3 Basic Constraints" to be accepted.

#### Base Command

`ciphertrust-external-ca-upload`

#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| cert_entry_id | The entry ID of the file to upload that contains the external CA certificate in PEM format. | Required | 
| name | A unique name of the CA. If not provided, will be set to externalca-&lt;id&gt;. | Optional | 
| parent | URI reference to a parent external CA certificate. This information can be used to build a certificate hierarchy. | Optional | 

#### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| InfoFile.Name | string | File name. | 
| InfoFile.EntryID | string | The entry ID of the report. | 
| InfoFile.Size | number | File size. | 
| InfoFile.Type | string | File type, e.g., "PE". | 
| InfoFile.Info | string | Basic information of the file. | 
| InfoFile.Extension | string | File extension. | 
| CipherTrust.ExternalCA.id | String | A unique identifier for the certificate authority \(CA\) certificate. | 
| CipherTrust.ExternalCA.uri | String | Uniform Resource Identifier associated with the CA certificate. | 
| CipherTrust.ExternalCA.account | String | Account associated with the CA certificate. | 
| CipherTrust.ExternalCA.devAccount | String | Developer account associated with the CA certificate. | 
| CipherTrust.ExternalCA.application | String | Application associated with the CA certificate. | 
| CipherTrust.ExternalCA.createdAt | Date | Timestamp of when the CA certificate was created. | 
| CipherTrust.ExternalCA.updatedAt | Date | Timestamp of the last update of the CA certificate. | 
| CipherTrust.ExternalCA.name | String | Name of the CA certificate. | 
| CipherTrust.ExternalCA.purpose.client_authentication | String | If set to enabled, the certificates signed by the specified CA can be used for client authentication. | 
| CipherTrust.ExternalCA.purpose.user_authentication | String | If set to enabled, the certificates signed by the specified CA can be used for user authentication. | 
| CipherTrust.ExternalCA.serialNumber | String | Serial number of the CA certificate. | 
| CipherTrust.ExternalCA.subject | String | Subject of the CA certificate. | 
| CipherTrust.ExternalCA.issuer | String | Issuer of the CA certificate. | 
| CipherTrust.ExternalCA.notBefore | Date | Timestamp of when the CA certificate is valid from. | 
| CipherTrust.ExternalCA.notAfter | Date | Timestamp of when the CA certificate is valid until. | 
| CipherTrust.ExternalCA.sha1Fingerprint | String | SHA-1 fingerprint of the CA certificate. | 
| CipherTrust.ExternalCA.sha256Fingerprint | String | SHA-256 fingerprint of the CA certificate. | 
| CipherTrust.ExternalCA.sha512Fingerprint | String | SHA-512 fingerprint of the CA certificate. | 

### ciphertrust-group-create

***
Create a new group. The group name is required.

#### Base Command

`ciphertrust-group-create`

#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| name | Name of the group. | Required | 
| description | Description of the group. | Optional | 

#### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| CipherTrust.Group.name | String | The name of the group. | 
| CipherTrust.Group.created_at | Date | The time the group was created. | 
| CipherTrust.Group.updated_at | Date | The time the group was last updated. | 
| CipherTrust.Group.user_metadata | Unknown | A schema-less object, which can be used by applications to store information about the resource. user_metadata is typically used by applications to store information about the resource which the end-users are allowed to modify, such as user preferences. | 
| CipherTrust.Group.app_metadata | Unknown | A schema-less object, which can be used by applications to store information about the resource. app_metadata is typically used by applications to store information which the end-users are not themselves allowed to change, like group membership or security roles. | 
| CipherTrust.Group.client_metadata | Unknown | A schema-less object, which can be used by applications to store information about the resource. client_metadata is typically used by applications to store information about the resource, such as client preferences. | 
| CipherTrust.Group.description | String | The description of the group. | 
| CipherTrust.Group.users_count | Number | The total user count associated with the group. | 

### ciphertrust-group-delete

***
Deletes a group given the group name.

#### Base Command

`ciphertrust-group-delete`

#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| group_name | Name of the group. | Required | 
| force | When set to true, groupmaps within this group will be deleted. | Optional | 

#### Context Output

There is no context output for this command.
### ciphertrust-group-list

***
Returns a list of group  Command arguments can be used to filter the results. Groups can be filtered for user or client membership. Connection filter applies only to user group membership and NOT to clients.

#### Base Command

`ciphertrust-group-list`

#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| group_name | Filter by group name. | Optional | 
| user_id | Filter by user membership. Using the username 'nil' will return groups with no members. Accepts only a user ID. Using '-' at the beginning of user_id will return groups that the user is not part of. | Optional | 
| connection | Filter by connection name or ID. | Optional | 
| client_id | Filter by client membership. Using the client name 'nil' will return groups with no members. Using '-' at the beginning of client_id will return groups that the client is not part of. | Optional | 
| page | Page to return. | Optional | 
| page_size | Number of entries per page. Defaults to 2000 (in case only page was provided). Maximum entries per page is 2000. | Optional | 
| limit | The maximum number of entries to return. Default is 50. | Optional | 

#### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| CipherTrust.Group.name | String | Name of the group. | 
| CipherTrust.Group.created_at | Date | The time the group was created. | 
| CipherTrust.Group.updated_at | Date | The time the group was last updated. | 
| CipherTrust.Group.user_metadata | Unknown | A schema-less object, which can be used by applications to store information about the resource. user_metadata is typically used by applications to store information about the resource which the end-users are allowed to modify, such as user preferences. | 
| CipherTrust.Group.app_metadata | Unknown | A schema-less object, which can be used by applications to store information about the resource. app_metadata is typically used by applications to store information which the end-users are not themselves allowed to change, like group membership or security roles. | 
| CipherTrust.Group.client_metadata | Unknown | A schema-less object, which can be used by applications to store information about the resource. client_metadata is typically used by applications to store information about the resource, such as client preferences. | 
| CipherTrust.Group.description | String | Description of the group. | 
| CipherTrust.Group.users_count | Number | The total user count associated with the group. | 

### ciphertrust-group-update

***
Update the properties of a group given the group name.

#### Base Command

`ciphertrust-group-update`

#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| group_name | Name of the group to update. | Required | 
| new_group_name | New name of the group. | Optional | 
| description | New description of the group. | Optional | 

#### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| CipherTrust.Group.name | String | The name of the group. | 
| CipherTrust.Group.created_at | Date | The time the group was created. | 
| CipherTrust.Group.updated_at | Date | The time the group was last updated. | 
| CipherTrust.Group.user_metadata | Unknown | A schema-less object, which can be used by applications to store information about the resource. user_metadata is typically used by applications to store information about the resource which the end-users are allowed to modify, such as user preferences. | 
| CipherTrust.Group.app_metadata | Unknown | A schema-less object, which can be used by applications to store information about the resource. app_metadata is typically used by applications to store information which the end-users are not themselves allowed to change, like group membership or security roles. | 
| CipherTrust.Group.client_metadata | Unknown | A schema-less object, which can be used by applications to store information about the resource. client_metadata is typically used by applications to store information about the resource, such as client preferences. | 
| CipherTrust.Group.description | String | The description of the group. | 
| CipherTrust.Group.users_count | Number | The total user count associated with the group. | 

### ciphertrust-local-ca-create

***
Creates a pending local CA. This operation returns a CSR that either can be self-signed by calling the ciphertrust-local-ca-self-sign command or signed by another CA and installed by calling the ciphertrust-local-ca-install command. A local CA keeps the corresponding private key inside the system and can issue certificates for clients, servers or intermediate CAs. The local CA can also be trusted by services inside the system for verification of client certificates.

#### Base Command

`ciphertrust-local-ca-create`

#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| cn | Common name. | Required | 
| algorithm | RSA or ECDSA (default) algorithms are supported. Signature algorithm (SHA512WithRSA, SHA384WithRSA, SHA256WithRSA, SHA1WithRSA, ECDSAWithSHA512, ECDSAWithSHA384, ECDSAWithSHA256) is selected based on the algorithm and size. Possible values are: RSA, ECDSA. | Optional | 
| copy_from_ca | ID of any local CA. If given, the CSR properties are copied from the given CA. | Optional | 
| dns_names | A comma-separated list of Subject Alternative Names (SAN) values. | Optional | 
| email | A comma-separated list of e-mail addresses. | Optional | 
| ip | A comma-separated list of IP addresses. | Optional | 
| name | A unique name of the CA. If not provided, will be set to localca-&lt;id&gt;. | Optional | 
| name_fields_raw_json | Name fields are "O=organization, OU=organizational unit, L=location, ST=state/province, C=country". Fields can be duplicated if present in different objects. This is a raw json string, for example: "[{"O": "Thales", "OU": "RnD", "C": "US", "ST": "MD", "L": "Belcamp"}, {"OU": "Thales Group Inc."}]". | Optional | 
| name_fields_json_entry_id | Entry ID of the file that contains JSON representation of the name_fields_raw_json. | Optional | 
| size | Key size. RSA: 1024 - 4096 (default: 2048), ECDSA: 256 (default), 384, 521. Possible values are: 256, 384, 521, 1024, 2048, 3072, 4096. | Optional | 

#### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| InfoFile.Name | string | File name. | 
| InfoFile.EntryID | string | The entry ID of the report. | 
| InfoFile.Size | number | File size. | 
| InfoFile.Type | string | File type, e.g., "PE". | 
| InfoFile.Info | string | Basic information of the file. | 
| InfoFile.Extension | string | File extension. | 
| CipherTrust.LocalCA.id | String | Unique identifier for the CA. | 
| CipherTrust.LocalCA.uri | String | Uniform Resource Identifier for the CA. | 
| CipherTrust.LocalCA.account | String | Account associated with the CA. | 
| CipherTrust.LocalCA.application | String | Application associated with the CA. | 
| CipherTrust.LocalCA.devAccount | String | Developer account associated with the CA. | 
| CipherTrust.LocalCA.createdAt | Date | Timestamp when the CA was created. | 
| CipherTrust.LocalCA.updatedAt | Date | Timestamp when the CA was last updated. | 
| CipherTrust.LocalCA.name | String | Name of the CA. | 
| CipherTrust.LocalCA.state | String | State of the CA. | 
| CipherTrust.LocalCA.subject | String | Distinguished Name \(DN\) of the CA subject. | 
| CipherTrust.LocalCA.notBefore | Date | Timestamp before which the certificate is not valid. | 
| CipherTrust.LocalCA.notAfter | Date | Timestamp after which the certificate is not valid. | 
| CipherTrust.LocalCA.sha1Fingerprint | String | SHA1 fingerprint of the CA certificate. | 
| CipherTrust.LocalCA.sha256Fingerprint | String | SHA256 fingerprint of the CA certificate. | 
| CipherTrust.LocalCA.sha512Fingerprint | String | SHA512 fingerprint of the CA certificate. | 

### ciphertrust-local-ca-delete

***
Deletes a local CA certificate.

#### Base Command

`ciphertrust-local-ca-delete`

#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| local_ca_id | An identifier of the resource. This can be either the ID (a UUIDv4), the name, the URI, or the slug (which is the last component of the URI). | Required | 

#### Context Output

There is no context output for this command.
### ciphertrust-local-ca-install

***
Installs a certificate signed by other CA to act as a local CA. Issuer can be both local or external CA. Typically used for intermediate CAs. The CA certificate must match the earlier created CA CSR, have "CA:TRUE" as part of the "X509v3 Basic Constraints", and have "Certificate Signing" as part of "X509v3 Key Usage" in order to be accepted.

#### Base Command

`ciphertrust-local-ca-install`

#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| local_ca_id | An identifier of the resource. This can be either the ID (a UUIDv4),the name, the URI, or the slug (which is the last component of the URI). | Required | 
| cert_entry_id | The entry ID of the file to upload that contains the signed certificate in PEM format to install as a local CA. | Required | 
| parent_id | An identifier of the parent resource. The resource can be either a local or an external CA. The identifier can be either the ID (a UUIDv4) or the URI. | Required | 

#### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| InfoFile.Name | string | File name. | 
| InfoFile.EntryID | string | The entry ID of the report. | 
| InfoFile.Size | number | File size. | 
| InfoFile.Type | string | File type, e.g., "PE". | 
| InfoFile.Info | string | Basic information of the file. | 
| InfoFile.Extension | string | File extension. | 
| CipherTrust.CAInstall.id | String | A unique identifier for the certificate authority \(CA\). | 
| CipherTrust.CAInstall.uri | String | Uniform Resource Identifier associated with the CA. | 
| CipherTrust.CAInstall.account | String | Account associated with the CA. | 
| CipherTrust.CAInstall.application | String | Application associated with the CA. | 
| CipherTrust.CAInstall.devAccount | String | Developer account associated with the CA. | 
| CipherTrust.CAInstall.name | String | Name of the CA. | 
| CipherTrust.CAInstall.state | String | Current state of the CA \(e.g., active, pending\). | 
| CipherTrust.CAInstall.createdAt | Date | Timestamp of when the CA was created. | 
| CipherTrust.CAInstall.updatedAt | Date | Timestamp of the last update of the CA. | 
| CipherTrust.CAInstall.serialNumber | String | Serial number of the CA's certificate. | 
| CipherTrust.CAInstall.subject | String | Subject of the CA's certificate. | 
| CipherTrust.CAInstall.issuer | String | Issuer of the CA's certificate. | 
| CipherTrust.CAInstall.notBefore | Date | Start date of the CA's certificate validity. | 
| CipherTrust.CAInstall.notAfter | Date | End date of the CA's certificate validity. | 
| CipherTrust.CAInstall.sha1Fingerprint | String | SHA1 fingerprint of the CA's certificate. | 
| CipherTrust.CAInstall.sha256Fingerprint | String | SHA256 fingerprint of the CA's certificate. | 
| CipherTrust.CAInstall.sha512Fingerprint | String | SHA512 fingerprint of the CA's certificate. | 
| CipherTrust.CAInstall.purpose.client_authentication | String | Indicates if client authentication is enabled for the CA. | 
| CipherTrust.CAInstall.purpose.user_authentication | String | Indicates if user authentication is enabled for the CA. | 

### ciphertrust-local-ca-list

***
Returns a list of local CA certificates. The results can be filtered, using the command arguments. If local_ca_id is provided, a single local CA certificate is returned and the rest of the filters are ignored. A chained parameter is used to return the full CA chain with the certificate and can be used only if local_ca_id is provided.

#### Base Command

`ciphertrust-local-ca-list`

#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| subject | Filter by subject. | Optional | 
| local_ca_id | An identifier of the resource. This can be either the ID (a UUIDv4), the name, the URI, or the slug (which is the last component of the URI). | Optional | 
| chained | When set to ‘true’ the full CA chain is returned with the certificate. Must be used with the local CA ID. Possible values are: true, false. | Optional | 
| issuer | Filter by issuer. | Optional | 
| state | Filter by state. Possible values are: pending, active. | Optional | 
| cert | Filter by cert. | Optional | 
| page | Page to return. | Optional | 
| page_size | Number of entries per page. Defaults to 2000 (in case only page was provided). Maximum entries per page is 2000. | Optional | 
| limit | The maximum number of entries to return. Default is 50. | Optional | 

#### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| InfoFile.Name | string | File name. | 
| InfoFile.EntryID | string | The entry ID of the report. | 
| InfoFile.Size | number | File size. | 
| InfoFile.Type | string | File type, e.g., "PE". | 
| InfoFile.Info | string | Basic information of the file | 
| InfoFile.Extension | string | File extension. | 
| CipherTrust.LocalCA.id | String | A unique identifier for the certificate authority \(CA\). | 
| CipherTrust.LocalCA.uri | String | Uniform Resource Identifier associated with the CA. | 
| CipherTrust.LocalCA.account | String | Account associated with the CA. | 
| CipherTrust.LocalCA.name | String | Name of the CA. | 
| CipherTrust.LocalCA.state | String | Current state of the CA \(e.g., pending, active\). | 
| CipherTrust.LocalCA.createdAt | Date | Timestamp of when the CA was created. | 
| CipherTrust.LocalCA.updatedAt | Date | Timestamp of last update of the CA. | 
| CipherTrust.LocalCA.serialNumber | String | Serial number of the CA's certificate. | 
| CipherTrust.LocalCA.subject | String | Subject of the CA's certificate. | 
| CipherTrust.LocalCA.issuer | String | Issuer of the CA's certificate. | 
| CipherTrust.LocalCA.notBefore | Date | Start date of the CA's certificate validity. | 
| CipherTrust.LocalCA.notAfter | Date | End date of the CA's certificate validity. | 
| CipherTrust.LocalCA.sha1Fingerprint | String | SHA1 fingerprint of the CA's certificate. | 
| CipherTrust.LocalCA.sha256Fingerprint | String | SHA256 fingerprint of the CA's certificate. | 
| CipherTrust.LocalCA.sha512Fingerprint | String | SHA512 fingerprint of the CA's certificate. | 
| CipherTrust.LocalCA.purpose.client_authentication | String | Indicates if client authentication is enabled for the CA. | 
| CipherTrust.LocalCA.purpose.user_authentication | String | Indicates if user authentication is enabled for the CA. | 

#### Command example
```!ciphertrust-local-ca-list state=pending subject="/C=US/ST=CA/L=FakeCity/O=FakeCompany/OU=RnD/OU=Fake Group Inc."```
#### Human Readable Output

>### Local Certificate Authorities 
>### Active CAs
>**No entries.**
>
>### Pending CAs
>**No entries.**
>
>### Expired CAs
>**No entries.**
>
>1 to 0 of 0 Local CAs

#### Command example
```!ciphertrust-local-ca-list local_ca_id="test_local_ca" chained=true```
#### Context Example
```json
{
    "CipherTrust": {
        "LocalCA": {
            "account": "kylo:kylo:admin:accounts:kylo",
            "createdAt": "2024-06-02T14:32:09.832603Z",
            "id": "c344cb9e-7607-47ac-968a-d6bba7cbd74c",
            "issuer": "/C=US/ST=CA/L=FakeCity/O=FakeCompany/OU=RnD/OU=Fake Group Inc./CN=test.com",
            "name": "test_local_ca",
            "notAfter": "2025-06-04T14:10:29Z",
            "notBefore": "2024-06-03T14:10:29Z",
            "purpose": {
                "client_authentication": "Enabled",
                "user_authentication": "Enabled"
            },
            "serialNumber": "226220228835411560013591369440322067707",
            "sha1Fingerprint": "57A5557A19DABE380C560E9696ADC95085317476",
            "sha256Fingerprint": "559AEF7C71DF2A7EF81704A31C6550E0781C42B6237A2171A8B73F4D17FA3FAB",
            "sha512Fingerprint": "1A1CBCA18131894851D9C956BDC0754218E5AEE37CE0E15180B8101F6072E9DF37062CB0B04DCAA220E943C9D2B7DA62730116B5D26E8A363B0C62E6BCFB242C",
            "state": "active",
            "subject": "/C=US/ST=CA/L=FakeCity/O=FakeCompany/OU=RnD/OU=Fake Group Inc./CN=test.com",
            "updatedAt": "2024-06-17T06:00:07.302444Z",
            "uri": "kylo:kylo:naboo:localca:c344cb9e-7607-47ac-968a-d6bba7cbd74c"
        }
    },
    "InfoFile": {
        "EntryID": "1786@a48e3cfd-a079-4895-89a7-4fac11b8143d",
        "Extension": "pem",
        "Info": "application/x-x509-ca-cert",
        "Name": "Certificate.pem",
        "Size": 1533,
        "Type": "PEM certificate"
    }
}
```

#### Human Readable Output

>### /C=US/ST=CA/L=FakeCity/O=FakeCompany/OU=RnD/OU=Fake Group Inc./CN=test.com
>|Id|Uri|Createdat|Updatedat|Name|State|Serialnumber|Subject|Issuer|Notbefore|Notafter|Sha1Fingerprint|Sha256Fingerprint|Sha512Fingerprint|
>|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
>| c344cb9e-7607-47ac-968a-d6bba7cbd74c | kylo:kylo:naboo:localca:c344cb9e-7607-47ac-968a-d6bba7cbd74c | 2024-06-02T14:32:09.832603Z | 2024-06-17T06:00:07.302444Z | test_local_ca | active | 226220228835411560013591369440322067707 | /C=US/ST=CA/L=FakeCity/O=FakeCompany/OU=RnD/OU=Fake Group Inc./CN=test.com | /C=US/ST=CA/L=FakeCity/O=FakeCompany/OU=RnD/OU=Fake Group Inc./CN=test.com | 2024-06-03T14:10:29Z | 2025-06-04T14:10:29Z | 57A5557A19DABE380C560E9696ADC95085317476 | 559AEF7C71DF2A7EF81704A31C6550E0781C42B6237A2171A8B73F4D17FA3FAB | 1A1CBCA18131894851D9C956BDC0754218E5AEE37CE0E15180B8101F6072E9DF37062CB0B04DCAA220E943C9D2B7DA62730116B5D26E8A363B0C62E6BCFB242C |


### ciphertrust-local-ca-self-sign

***
Self-sign a local CA certificate. This is used to create a root CA. Either duration or notAfter date must be specified. If both notAfter and duration are given, then notAfter date takes precedence over duration. If duration is given without notBefore date, certificate is issued starting from server's current time for the specified duration.

#### Base Command

`ciphertrust-local-ca-self-sign`

#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| local_ca_id | An identifier of the resource. This can be either the ID (a UUIDv4), the name, the URI, or the slug (which is the last component of the URI). | Required | 
| duration | The duration of the certificate in days. Either not_after date or duration must be specified. not_after overrides duration if both are given. Default is 365. | Optional | 
| not_after | End date of certificate. Either not_after date or duration must be specified. not_after overrides duration if both are given. | Optional | 
| not_before | Start date of certificate. | Optional | 

#### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| InfoFile.Name | string | FileName | 
| InfoFile.EntryID | string | The EntryID of the report | 
| InfoFile.Size | number | File Size | 
| InfoFile.Type | string | File type e.g. "PE" | 
| InfoFile.Info | string | Basic information of the file | 
| InfoFile.Extension | string | File extension | 
| CipherTrust.CASelfSign.id | String | A unique identifier for the certificate authority \(CA\). | 
| CipherTrust.CASelfSign.uri | String | Uniform Resource Identifier associated with the CA. | 
| CipherTrust.CASelfSign.account | String | Account associated with the CA. | 
| CipherTrust.CASelfSign.application | String | Application associated with the CA. | 
| CipherTrust.CASelfSign.devAccount | String | Developer account associated with the CA. | 
| CipherTrust.CASelfSign.name | String | Name of the CA. | 
| CipherTrust.CASelfSign.state | String | Current state of the CA \(e.g., pending, active\). | 
| CipherTrust.CASelfSign.createdAt | Date | Timestamp of when the CA was created. | 
| CipherTrust.CASelfSign.updatedAt | Date | Timestamp of the last update of the CA. | 
| CipherTrust.CASelfSign.serialNumber | String | Serial number of the CA's certificate. | 
| CipherTrust.CASelfSign.subject | String | Subject of the CA's certificate. | 
| CipherTrust.CASelfSign.issuer | String | Issuer of the CA's certificate. | 
| CipherTrust.CASelfSign.notBefore | Date | Start date of the CA's certificate validity. | 
| CipherTrust.CASelfSign.notAfter | Date | End date of the CA's certificate validity. | 
| CipherTrust.CASelfSign.sha1Fingerprint | String | SHA1 fingerprint of the CA's certificate. | 
| CipherTrust.CASelfSign.sha256Fingerprint | String | SHA256 fingerprint of the CA's certificate. | 
| CipherTrust.CASelfSign.sha512Fingerprint | String | SHA512 fingerprint of the CA's certificate. | 
| CipherTrust.CASelfSign.purpose.client_authentication | String | Indicates if client authentication is enabled for the CA. | 
| CipherTrust.CASelfSign.purpose.user_authentication | String | Indicates if user authentication is enabled for the CA. | 

### ciphertrust-local-ca-update

***
Update a local CA.

#### Base Command

`ciphertrust-local-ca-update`

#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| local_ca_id | An identifier of the resource. This can be either the ID (a UUIDv4),the Name, the URI, or the slug (which is the last component of the URI). | Required | 
| allow_client_authentication | If set to true, the certificates signed by the specified CA can be used for client authentication. Possible values are: true, false. | Optional | 
| allow_user_authentication | If set to true, the certificates signed by the specified CA can be used for user authentication. Possible values are: true, false. | Optional | 

#### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| InfoFile.Name | string | FileName | 
| InfoFile.EntryID | string | The EntryID of the report | 
| InfoFile.Size | number | File Size | 
| InfoFile.Type | string | File type e.g. "PE" | 
| InfoFile.Info | string | Basic information of the file | 
| InfoFile.Extension | string | File extension | 
| CipherTrust.LocalCA.id | String | A unique identifier for the certificate authority \(CA\). | 
| CipherTrust.LocalCA.uri | String | Uniform Resource Identifier associated with the CA. | 
| CipherTrust.LocalCA.account | String | Account associated with the CA. | 
| CipherTrust.LocalCA.name | String | Name of the CA. | 
| CipherTrust.LocalCA.state | String | Current state of the CA \(e.g., pending, active\). | 
| CipherTrust.LocalCA.createdAt | Date | Timestamp of when the CA was created. | 
| CipherTrust.LocalCA.updatedAt | Date | Timestamp of the last update of the CA. | 
| CipherTrust.LocalCA.serialNumber | String | Serial number of the CA's certificate. | 
| CipherTrust.LocalCA.subject | String | Subject of the CA's certificate. | 
| CipherTrust.LocalCA.issuer | String | Issuer of the CA's certificate. | 
| CipherTrust.LocalCA.notBefore | Date | Start date of the CA's certificate validity. | 
| CipherTrust.LocalCA.notAfter | Date | End date of the CA's certificate validity. | 
| CipherTrust.LocalCA.sha1Fingerprint | String | SHA1 fingerprint of the CA's certificate. | 
| CipherTrust.LocalCA.sha256Fingerprint | String | SHA256 fingerprint of the CA's certificate. | 
| CipherTrust.LocalCA.sha512Fingerprint | String | SHA512 fingerprint of the CA's certificate. | 
| CipherTrust.LocalCA.purpose.client_authentication | String | Indicates if client authentication is enabled for the CA. | 
| CipherTrust.LocalCA.purpose.user_authentication | String | Indicates if user authentication is enabled for the CA. | 

#### Command example
```!ciphertrust-local-ca-update local_ca_id="test_local_ca" allow_client_authentication=true allow_user_authentication=true```
#### Context Example
```json
{
    "CipherTrust": {
        "LocalCA": {
            "account": "kylo:kylo:admin:accounts:kylo",
            "createdAt": "2024-06-02T14:32:09.832603Z",
            "id": "c344cb9e-7607-47ac-968a-d6bba7cbd74c",
            "issuer": "/C=US/ST=CA/L=FakeCity/O=FakeCompany/OU=RnD/OU=Fake Group Inc./CN=test.com",
            "name": "test_local_ca",
            "notAfter": "2025-06-04T14:10:29Z",
            "notBefore": "2024-06-03T14:10:29Z",
            "purpose": {
                "client_authentication": "Enabled",
                "user_authentication": "Enabled"
            },
            "serialNumber": "226220228835411560013591369440322067707",
            "sha1Fingerprint": "57A5557A19DABE380C560E9696ADC95085317476",
            "sha256Fingerprint": "559AEF7C71DF2A7EF81704A31C6550E0781C42B6237A2171A8B73F4D17FA3FAB",
            "sha512Fingerprint": "1A1CBCA18131894851D9C956BDC0754218E5AEE37CE0E15180B8101F6072E9DF37062CB0B04DCAA220E943C9D2B7DA62730116B5D26E8A363B0C62E6BCFB242C",
            "state": "active",
            "subject": "/C=US/ST=CA/L=FakeCity/O=FakeCompany/OU=RnD/OU=Fake Group Inc./CN=test.com",
            "updatedAt": "2024-06-17T10:08:38.116763789Z",
            "uri": "kylo:kylo:naboo:localca:c344cb9e-7607-47ac-968a-d6bba7cbd74c"
        }
    },
    "InfoFile": {
        "EntryID": "1791@a48e3cfd-a079-4895-89a7-4fac11b8143d",
        "Extension": "pem",
        "Info": "application/x-x509-ca-cert",
        "Name": "Certificate.pem",
        "Size": 1533,
        "Type": "PEM certificate"
    }
}
```

#### Human Readable Output

>test_local_ca has been updated successfully!

### ciphertrust-local-certificate-delete

***
Deletes a local certificate.

#### Base Command

`ciphertrust-local-certificate-delete`

#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| ca_id | An identifier of the issuer CA resource. This can be either the ID (a UUIDv4),the Name, the URI, or the slug (which is the last component of the URI). | Required | 
| local_ca_id | An identifier of the certificate resource.This can be either the ID (a UUIDv4), the URI, or the slug (which is the last component of the URI). | Required | 

#### Context Output

There is no context output for this command.
### ciphertrust-user-create

***
Create a new user in a domain(including root), or add an existing domain user to a sub-domain. Users are always created in the local, internal user database, but might have references to external identity providers.
The connection property is optional. If this property is specified when creating new users, it can be the name of a connection or local_account for a local user.
The connection property is only used in the body of the create-user request. It is not present in either request or response bodies of the other user endpoints.
To create a user - username is mandatory. And password is required in most cases except when certificate authentication is used and certificate subject dn is provided.
To enable certificate based authentication for a user, it is required to set certificate_subject_dn and add "user_certificate" authentication method in allowed_auth_methods. This functionality is available only for local users.
To assign a root domain user to a sub-domain - the users are added to the domain of the user who is logging in, and the connection property should be left empty. The user_id or username fields are the only ones that are used while adding existing users to sub-domains; all other fields are ignored.
To enable the two-factor authentication based on username-password and user certificate for a user, it is required to set "certificate_subject_dn" and add "password_with_user_certificate" authentication method in "allowed_auth_methods". For authentication, the user will require both username-password and user certificate. This functionality applies only to local users.

#### Base Command

`ciphertrust-user-create`

#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| name | Full name of the user. | Optional | 
| user_id | The user_id is the ID of an existing root domain user. This field is used only when adding an existing root domain user to a different domain. | Optional | 
| username | The login name of the user. This is the identifier used to login. This attribute is required to create a user, but is omitted when getting or listing user  It cannot be updated. This attribute may also be used (instead of the user_id) when adding an existing root domain user to a different domain. | Optional | 
| password | The password used to secure the users account. Allowed passwords are defined by the password policy. Password is optional when "certificate_subject_dn" is set and "user_certificate" is in allowed_auth_methods. In all other cases, password is required. It is not included in user resource responses. Default global password complexity requirement: minimum characters = 8, maximum characters = 30, lower-case letters = 1, upper-case letters = 1, decimal digits = 1, special characters = 1. | Optional | 
| email | E-mail of the user. | Optional | 
| allowed_auth_methods | Comma seperated login authentication methods allowed to the user. Default value - "password" i.e. Password Authentication is allowed by default. Setting it to empty, i.e "empty", means no authentication method is allowed to the user. If both enable_cert_auth and allowed_auth_methods are provided in the request, enable_cert_auth is ignored. Setting it to "password_with_user_certificate", means two-factor authentication is enabled for the user. The user will require both username-password and user_certificate for authentication. Valid values are: password user_certificate password_with_user_certificate This property does not control login behavior for users in admin group. Possible values are: password, user_certificate, password_with_user_certificate, empty. | Optional | 
| allowed_client_types | List of client types that can authenticate using the user's credentials. Default value - "unregistered,public,confidential" i.e. all clients can authenticate the user using user's credentials. Setting it to empty, "empty", authenticate the user using user's credentials. Setting it to empty, "empty", means no client can authenticate this user, which effectively means no one can login into this user. Valid values in the array are: unregistered public confidential This property does not control login behavior for users in admin group. Possible values are: unregistered, public, confidential. | Optional | 
| certificate_subject_dn | The Distinguished Name of the user in certificate. | Optional | 
| connection | Can be the name of a connection or "local_account" for a local user. Default is local_account. | Optional | 
| expires_at | The expires_at field is applicable only for local user account. Only members of the 'admin' and 'User Admins' groups can add expiration to an existing local user account or modify the expiration date. Once the expires_at date is reached, the user account gets disabled and the user is not able to perform any actions. Setting the expires_at field to "empty", removes the expiration date of the user account. | Optional | 
| is_domain_user | This flag can be used to create the user in a non-root domain where user management is allowed. Possible values are: true, false. | Optional | 
| prevent_ui_login | If true, user is not allowed to login from Web UI. Possible values are: true, false. Default is false. | Optional | 
| password_change_required | Password change required flag. If set to true, user will be required to change their password on next successful login. Possible values are: true, false. | Optional | 
| password_policy | The password policy applies only to local user accounts and overrides the global password policy. By default, the global password policy is applied to the users. | Optional | 

#### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| CipherTrust.Users.user_id | String | A unique identifier for API call usage. | 
| CipherTrust.Users.username | String | The login name of the user. This is the identifier used to login. This attribute is required to create a user, but is omitted when getting or listing user  It cannot be updated. | 
| CipherTrust.Users.connection | String | This attribute is required to create a user, but is not included in user resource responses. Can be the name of a connection or 'local_account' for a local user, defaults to 'local_account'. | 
| CipherTrust.Users.email | String | E-mail of the user | 
| CipherTrust.Users.name | String | Full name of the user | 
| CipherTrust.Users.certificate_subject_dn | String | The Distinguished Name of the user in certificate | 
| CipherTrust.Users.enable_cert_auth | Boolean | Deprecated: Use allowed_auth_methods instead. Enable certificate based authentication flag. If set to true, the user will be able to login using certificate. | 
| CipherTrust.Users.user_metadata | Unknown | A schema-less object, which can be used by applications to store information about the resource. user_metadata is typically used by applications to store information about the resource which the end-users are allowed to modify, such as user preferences. | 
| CipherTrust.Users.app_metadata | Unknown | A schema-less object, which can be used by applications to store information about the resource. app_metadata is typically used by applications to store information which the end-users are not themselves allowed to change, like group membership or security roles. | 
| CipherTrust.Users.logins_count | Number | Count for the number of logins | 
| CipherTrust.Users.last_login | Date | Timestamp of last login | 
| CipherTrust.Users.created_at | Date | Timestamp of when user was created | 
| CipherTrust.Users.updated_at | Date | Timestamp of last update of the user | 
| CipherTrust.Users.allowed_auth_methods | Unknown | List of login authentication methods allowed to the user. | 
| CipherTrust.Users.expires_at | Date | The expires_at is applicable only for local user accounts. The admin or a user who is part of the admin group can add expiration to an existing local user account or modify the expiration date. Once the expires_at date is reached, the user account gets disabled and the user is not able to perform any actions. | 
| CipherTrust.Users.password_policy | String | The password policy applies only to local user accounts and overrides the global password policy. By default, the global password policy is applied to the users. | 
| CipherTrust.Users.allowed_client_types | Unknown | List of client types allowed to the user. | 
| CipherTrust.Users.nickname | String | Nickname of the user | 
| CipherTrust.Users.failed_logins_count | Number | Count of failed login attempts | 
| CipherTrust.Users.account_lockout_at | Date | Timestamp when the account was locked out | 
| CipherTrust.Users.failed_logins_initial_attempt_at | Date | Timestamp of the initial failed login attempt | 
| CipherTrust.Users.last_failed_login_at | Date | Timestamp of the last failed login attempt | 
| CipherTrust.Users.password_changed_at | Date | Timestamp of when the password was last changed | 
| CipherTrust.Users.password_change_required | Boolean | Indicates if a password change is required | 
| CipherTrust.Users.auth_domain | String | Authentication domain of the user | 
| CipherTrust.Users.login_flags | Unknown | Flags related to login permissions | 

### ciphertrust-user-delete

***
Deletes a user given the user's user-id. If the current user is logged into a sub-domain, the user is deleted from that sub-domain. If the current user is logged into the root domain, the user is deleted from all domains it belongs to.

#### Base Command

`ciphertrust-user-delete`

#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| user_id | The user_id of the user. | Required | 

#### Context Output

There is no context output for this command.
### ciphertrust-user-password-change

***
Change the current user's password. Can only be used to change the password of the currently authenticated user. The user will not be able to change their password to the same password.

#### Base Command

`ciphertrust-user-password-change`

#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| new_password | The new password. | Required | 
| password | The own user's current password. | Required | 
| username | The login name of the current user. | Required | 
| auth_domain | The domain where user needs to be authenticated. This is the domain where user is created. Defaults to the root domain. | Optional | 

#### Context Output

There is no context output for this command.
### ciphertrust-user-to-group-add

***
Add a user to a group. This command is idempotent: calls to add a user to a group in which they already belong will return an identical, OK response.

#### Base Command

`ciphertrust-user-to-group-add`

#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| group_name | Name of the group. By default it will be added to the Key Users Group. Default is Key Users. | Required | 
| user_id | The user_id of the user. Can be retrieved by using the command ciphertrust-users-list. | Required | 

#### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| CipherTrust.Group.name | String | The name of the group. | 
| CipherTrust.Group.created_at | Date | The time the group was created. | 
| CipherTrust.Group.updated_at | Date | The time the group was last updated. | 
| CipherTrust.Group.user_metadata | Unknown | A schema-less object, which can be used by applications to store information about the resource. user_metadata is typically used by applications to store information about the resource which the end-users are allowed to modify, such as user preferences. | 
| CipherTrust.Group.app_metadata | Unknown | A schema-less object, which can be used by applications to store information about the resource. app_metadata is typically used by applications to store information which the end-users are not themselves allowed to change, like group membership or security roles. | 
| CipherTrust.Group.client_metadata | Unknown | A schema-less object, which can be used by applications to store information about the resource. client_metadata is typically used by applications to store information about the resource, such as client preferences. | 
| CipherTrust.Group.description | String | The description of the group. | 
| CipherTrust.Group.users_count | Number | The total user count associated with the group. | 

### ciphertrust-user-to-group-remove

***
Removes a user from a group.

#### Base Command

`ciphertrust-user-to-group-remove`

#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| group_name | Name of the group. | Required | 
| user_id | The user_id of the user. Can be retrieved by using the command ciphertrust-users-list. | Required | 

#### Context Output

There is no context output for this command.
### ciphertrust-user-update

***
Change the properties of a user. For instance the name, the password, or metadata. Permissions would normally restrict this route to users with admin privileges. Non admin users wishing to change their own passwords should use the ciphertrust-user-password-change command.

#### Base Command

`ciphertrust-user-update`

#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| name | The user's full name. | Optional | 
| user_id | The user_id of the user. | Required | 
| username | The login name of the user. | Optional | 
| password | The password used to secure the user's account. | Optional | 
| email | The email of the user. | Optional | 
| password_change_required | Password change required flag. If set to true, user will be required to change their password on next successful login. Possible values are: true, false. | Optional | 
| allowed_auth_methods | List of login authentication methods allowed to the user. Setting it to empty, i.e "empty", means no authentication method is allowed to the user. If both enable_cert_auth and allowed_auth_methods are provided in the request, enable_cert_auth is ignored. Setting it to "password_with_user_certificate", means two-factor authentication is enabled for the user. The user will require both username-password and user_certificate for authentication. User cannot have "password" or "user_certificate" with "password_with_user_certificate" in allowed_auth_methods. Valid values in the array are: password user_certificate password_with_user_certificate This property does not control login behavior for users in admin group. Possible values are: password, user_certificate, password_with_user_certificate, empty. | Optional | 
| allowed_client_types | List of client types that can authenticate using the user's credentials. Setting it to empty, i.e "empty", means no client can authenticate this user, which effectively means no one can login into this user. Valid values in the array are: unregistered public confidential This property does not control login behavior for users in admin group. Possible values are: unregistered, public, confidential. | Optional | 
| certificate_subject_dn | The Distinguished Name of the user in certificate. e.g.OU=organization unit,O=organization,L=location,ST=state,C=country. | Optional | 
| expires_at | The "expires_at" field is applicable only for local user account. Only members of the 'admin' and 'User Admins' groups can add expiration to an existing local user account or modify the expiration date. Once the "expires_at" date is reached, the user account gets disabled and the user is not able to perform any actions. Setting the "expires_at" argument to "empty", removes the expiration date of the user account. | Optional | 
| failed_logins_count | Set it to 0 to unlock a locked user account. | Optional | 
| prevent_ui_login | If true, user is not allowed to login from Web UI. Possible values are: true, false. Default is false. | Optional | 
| password_policy | The password policy applies only to local user accounts and overrides the global password policy. By default, the global password policy is applied to the users. | Optional | 

#### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| CipherTrust.Users.user_id | String | A unique identifier for API call usage. | 
| CipherTrust.Users.username | String | The login name of the user. This is the identifier used to login. This attribute is required to create a user, but is omitted when getting or listing user  It cannot be updated. | 
| CipherTrust.Users.connection | String | This attribute is required to create a user, but is not included in user resource responses. Can be the name of a connection or 'local_account' for a local user, defaults to 'local_account'. | 
| CipherTrust.Users.email | String | E-mail of the user | 
| CipherTrust.Users.name | String | Full name of the user | 
| CipherTrust.Users.nickname | String | Nickname of the user | 
| CipherTrust.Users.certificate_subject_dn | String | The Distinguished Name of the user in certificate | 
| CipherTrust.Users.enable_cert_auth | Boolean | Deprecated: Use allowed_auth_methods instead. Enable certificate based authentication flag. If set to true, the user will be able to login using certificate. | 
| CipherTrust.Users.user_metadata | Unknown | A schema-less object, which can be used by applications to store information about the resource. user_metadata is typically used by applications to store information about the resource which the end-users are allowed to modify, such as user preferences. | 
| CipherTrust.Users.app_metadata | Unknown | A schema-less object, which can be used by applications to store information about the resource. app_metadata is typically used by applications to store information which the end-users are not themselves allowed to change, like group membership or security roles. | 
| CipherTrust.Users.logins_count | Number | Count for the number of logins | 
| CipherTrust.Users.last_login | Date | Timestamp of last login | 
| CipherTrust.Users.created_at | Date | Timestamp of when user was created | 
| CipherTrust.Users.updated_at | Date | Timestamp of last update of the user | 
| CipherTrust.Users.allowed_auth_methods | Unknown | List of login authentication methods allowed to the user. | 
| CipherTrust.Users.expires_at | Date | The expires_at is applicable only for local user accounts. The admin or a user who is part of the admin group can add expiration to an existing local user account or modify the expiration date. Once the expires_at date is reached, the user account gets disabled and the user is not able to perform any actions. | 
| CipherTrust.Users.password_policy | String | The password policy applies only to local user accounts and overrides the global password policy. By default, the global password policy is applied to the users. | 
| CipherTrust.Users.allowed_client_types | Unknown | List of client types allowed to the user. | 
| CipherTrust.Users.failed_logins_count | Number | Count of failed login attempts | 
| CipherTrust.Users.failed_logins_initial_attempt_at | Date | Timestamp of the initial failed login attempt. | 
| CipherTrust.Users.account_lockout_at | Date | Timestamp of when the account was locked. | 
| CipherTrust.Users.last_failed_login_at | Date | Timestamp of the last failed login attempt. | 
| CipherTrust.Users.password_changed_at | Date | Timestamp of when the password was last changed. | 
| CipherTrust.Users.password_change_required | Boolean | Indicates if a password change is required at next login. | 
| CipherTrust.Users.login_flags | Unknown | Flags related to login, such as prevent_ui_login. | 

### ciphertrust-users-list

***
Returns a list of user  Command arguments can be used to filter the results. The results can be filtered, using the command arguments. 

#### Base Command

`ciphertrust-users-list`

#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| name | Filter by the user's name. | Optional | 
| user_id | If provided, gets the user with the specified user_id.  If the user_id 'self' is provided, it will return the current user's information. | Optional | 
| username | Filter by the user’s username. | Optional | 
| email | Filter by the user’s email. | Optional | 
| groups | Filter by users in the given group name. Provide multiple groups separated by comma (',') to get users in all of those groups. Using 'nil' as the group name will return users that are not part of any group. | Optional | 
| exclude_groups | Users associated with given group will be excluded from the result. Provide multiple groups separated by comma (',') to exclude multiple groups in the result. | Optional | 
| auth_domain_name | Filter by user’s auth domain. | Optional | 
| account_expired | Filters the list of users whose expiration time has passed. Possible values are: true, false. | Optional | 
| allowed_auth_methods | Filter by the login authentication method allowed to the users. It is a comma seperated list of values. A special value `empty` can be specified to get users to whom no authentication method is allowed. Possible values are: password, user_certificate, password_with_user_certificate, empty. | Optional | 
| allowed_client_types | Filter by the client types that can authenticate the user. It is a comma separated list of values. Possible values are: unregistered, public, confidential. | Optional | 
| password_policy | Filter the list of users based on assigned password policy. | Optional | 
| return_groups | If set to 'true', it returns the group's name in which user is associated along with all users information. Possible values are: true, false. | Optional | 
| page | Page to return. | Optional | 
| page_size | Number of entries per page. Defaults to 2000 (in case only page was provided). Maximum entries per page is 2000. | Optional | 
| limit | The max number of entries to return. Default is 50. | Optional | 

#### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| CipherTrust.Users.username | String | The login name of the user. This is the identifier used to login. This attribute is required to create a user, but is omitted when getting or listing user  It cannot be updated. | 
| CipherTrust.Users.connection | String | This attribute is required to create a user, but is not included in user resource responses. Can be the name of a connection or 'local_account' for a local user, defaults to 'local_account'. | 
| CipherTrust.Users.email | String | E-mail of the user | 
| CipherTrust.Users.name | String | Full name of the user | 
| CipherTrust.Users.certificate_subject_dn | String | The Distinguished Name of the user in certificate | 
| CipherTrust.Users.enable_cert_auth | Boolean | Deprecated: Use allowed_auth_methods instead. Enable certificate based authentication flag. If set to true, the user will be able to login using certificate. | 
| CipherTrust.Users.user_metadata | Unknown | A schema-less object, which can be used by applications to store information about the resource. user_metadata is typically used by applications to store information about the resource which the end-users are allowed to modify, such as user preferences. | 
| CipherTrust.Users.app_metadata | Unknown | A schema-less object, which can be used by applications to store information about the resource. app_metadata is typically used by applications to store information which the end-users are not themselves allowed to change, like group membership or security roles. | 
| CipherTrust.Users.logins_count | Number | Count for the number of logins | 
| CipherTrust.Users.last_login | Date | Timestamp of last login | 
| CipherTrust.Users.created_at | Date | Timestamp of when user was created | 
| CipherTrust.Users.updated_at | Date | Timestamp of last update of the user | 
| CipherTrust.Users.allowed_auth_methods | Unknown | List of login authentication methods allowed to the user. | 
| CipherTrust.Users.expires_at | Date | The expires_at is applicable only for local user accounts. The admin or a user who is part of the admin group can add expiration to an existing local user account or modify the expiration date. Once the expires_at date is reached, the user account gets disabled and the user is not able to perform any actions. | 
| CipherTrust.Users.password_policy | String | The password policy applies only to local user accounts and overrides the global password policy. By default, the global password policy is applied to the users. | 
| CipherTrust.Users.allowed_client_types | Unknown | List of client types allowed to the user. | 
| CipherTrust.Users.last_failed_login_at | Date | Timestamp of last failed login | 
| CipherTrust.Users.failed_logins_count | Number | Count of failed logins | 
| CipherTrust.Users.failed_logins_initial_attempt_at | Date | Timestamp of first failed login | 
| CipherTrust.Users.account_lockout_at | Date | Timestamp of account lockout | 
| CipherTrust.Users.nickname | String | Nickname of the user | 
| CipherTrust.Users.user_id | String | The user's unique identifier | 
| CipherTrust.Users.password_changed_at | Date | Timestamp of when the password was last changed | 
| CipherTrust.Users.password_change_required | Boolean | Flag indicating if password change is required | 
| CipherTrust.Users.groups | Unknown | List of groups the user belongs to | 
| CipherTrust.Users.auth_domain | String | Authentication domain ID | 
| CipherTrust.Users.login_flags | Unknown | Flags related to user login | 
| CipherTrust.Users.auth_domain_name | String | Name of the authentication domain | 

#### Command example
```!ciphertrust-users-list exclude_groups="group_to_exclude1,group_to_exclude2" account_expired=true allowed_client_types="confidential,public" allowed_auth_methods="user_certificate,password"```
#### Human Readable Output

>### Users
>|Username|Full Name|Email|Created|Updated|Expires|Id|Last Login|Logins|Last Failed Login|Password Changed|Password Change Required|
>|---|---|---|---|---|---|---|---|---|---|---|---|
>|  |  |  |  |  | Never |  | Never Logged In |  | Never Failed A Login |  |  |

