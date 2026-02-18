<!-- PAGE 536 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.118** **User** **Credential** **Command** **Class,** **version** **1** **[NEVER** **CERTIFIED]**


**Warning:** **THIS** **COMMAND** **CLASS** **HAS** **NEVER** **BEEN** **CERTIFIED**

This command class has never been implemented and certified by a Z-Wave product. Therefore,
this Command Class definition MAY be updated in a non-backwards compatible manner, or even
removed.


Consult with the Z-Wave Alliance Application Work Group if you consider implementing this
Command Class.


The User Credential Command Class is used to manage user Credentials for gaining access to properties, typically through unlocking or opening doors. Those properties could be residential or commercial. Credential types include PIN Codes, Passwords, Radio-Frequency Identification (RFID),
Bluetooth Low Energy (BLE), Near Field Communication (NFC), Ultra-Wideband (UWB), and Biometrics. This command class employs a user-centric model, allowing multiple Credentials to be associated with one User Unique Identifier.

CC:0083.01.00.11.000 Setting schedules for User Unique Identifiers is not required. However, if setting schedules for Unique
User Identifiers is supported, then they MUST be supported using the _Schedule_ _Entry_ _Lock_ _Command_
_Class,_ _version_ _4_ _[NEVER_ _CERTIFIED]_ or higher.

CC:0083.01.00.11.001 To prompt notifications based on activity for these User Unique Identifiers/Credentials, the Notification Command Class MUST be used.


CC:0083.01.00.12.002
When a node is first enrolled in a Z-Wave network, the controlling device SHOULD query the node for
any existing User/Credential information before setting up new User Unique Identifiers. It is possible
that nodes have already been populated with desired User Unique Identifiers before network inclusion
using some other home automation technology or using a local interface.


**2.2.118.1** **Terminology**


**Credentials** are configured on a supporting node for different **User** **Unique** **Identifiers** . Each User
Unique Identifier is associated with none, one, or multiple Credentials. A Credential can only have

one user.

A User Unique Identifier is used in the database to associate Credentials and schedules to a single
User Unique Identifier slot within the node and Z-Wave network.

The entry of a Credential can trigger different outcomes, such as opening a door, sending a command
to an associated device, triggering a notification, or ignoring the Credential. This can be configured
with the User Type. A **User** **Type** determines the category of access allowed.


**2.2.118.2** **Compatibility** **Considerations**


**2.2.118.2.1** **Command** **Class** **Dependencies**


CC:0083.01.00.23.007 For backwards compatibility considerations, a device MAY support both the User Code Command
Class and User Credential Command Class.

In this case the data backing User Code Command Class is defined to be a user code credential table
for numeric PIN codes.


CC:0083.01.00.21.004 If the User Code Command Class is supported, then the _Credential_ _Set_ _Command_ and _Credential_ _Get_
_Command_ / _Credential_ _Report_ _Command_ for Credential Type 0x01 (PIN Code) MUST act on the
same data as the User Code Command Class.


CC:0083.01.00.21.014 If the User Code Command Class is supported, the User Credential Command Class’s Credential Data
Length for Credential Type 0x01 (PIN Code) MUST have Min value of 4 and Max value of 10.


CC:0083.01.00.21.015


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 535




<!-- PAGE 537 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


If User Code Command Class, version 1 is supported: The User Credential Command Class’s number
of supported Credential Slots for Credential Type 0x01 (PIN Code) MUST NOT exceed 255.


CC:0083.01.00.21.016 If User Code Command Class, version 2 or higher is supported: The User Code Command Class
MUST support all numeric keys (decimal digits 0..9, i.e. ASCII 0x30..0x39) and MUST NOT support
any other key.

CC:0083.01.00.21.005 Data MUST be mapped such that User Code Command Class’s User Identifier (Slot) is equivalent to
User Credential Command Class’s Credential Slot, such that modifications using either API modify
the same underlying credential.

CC:0083.01.00.21.006 When the User Code Command Class is used to add a new User Identifier (Slot), the device MUST
also add a new User Unique Identifier to tie the new credential to.

For example, a Credential Set Command modify for User Unique Identifier 0x0001, Credential Type
0x01 (PIN Code), and Credential Slot 0x0007 will modify the same data as a User Code Set for User
Identifier (Slot) 0x07 or Extended User Code Set for User ID (Slot) 0x0007.


CC:0083.01.00.22.008 It is RECOMMENDED for a controlling device to use one common method for controlling a node
supporting both User Credential Command Class and User Code Command Class.


CC:0083.01.00.23.009 This Command Class MAY be used in conjunction with the _Schedule_ _Entry_ _Lock_ _Command_ _Class,_
_version_ _4_ _[NEVER_ _CERTIFIED]_ to schedule access for users.

CC:0083.01.00.21.010 This Command Class MUST be used with the _Notification_ _Command_ _Class,_ _version_ _3-8_ .


CC:0083.01.00.21.011 A node supporting this Command Class MUST either:


      - Support the _Door_ _Lock_ _Command_ _Class,_ _version_ _4_ .


      - Control the Door Lock Command Class via association groups.

CC:0083.01.00.21.012 A supporting node MUST reflect Credential inputs in the door lock status when relevant. For example,
when the node becomes unsecured by a Credential input, the Door Lock Operation mode is updated

to unsecure.


CC:0083.01.00.23.013 A node supporting this Command Class MAY have an Association group issuing the corresponding
Door Lock Operation Set Commands when valid Credentials are input to control several door locks
simultaneously.


**2.2.118.3** **Security** **Considerations**


On top of those referenced in _User_ _Code_ _Command_ _Class,_ _version_ _2_, the following security measures
should be taken into consideration:


CC:0083.01.00.42.014 - Numeric PIN codes SHOULD NOT be allowed if they contain solely consecutive digits (e.g.
123456 or 654321).


CC:0083.01.00.42.015 - Numeric PIN codes SHOULD NOT be allowed if there is solely one repeating digit (e.g. 111111).


CC:0083.01.00.41.016 - Numeric PIN codes MUST be at least 4 digits long.


CC:0083.01.00.42.017 - If a Credential is rejected, and the _Credential_ _Set_ _Command_ was sent with Supervision Encapsulation, then the _Supervision_ _Report_ _Command_ SHOULD have a status of FAIL.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 536




<!-- PAGE 538 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.118.4** **User** **Capabilities** **Get** **Command**


This command is used to request User capabilities and limits from the node.


CC:0083.01.01.11.000 This command MUST NOT be issued via multicast addressing.


CC:0083.01.01.11.001 A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast Node ID and the Multi Channel Multi-End Point
destination are all considered multicast addressing methods.


CC:0083.01.01.11.002 The _User_ _Capabilities_ _Report_ _Command_ MUST be returned in response to this command.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|
|Command = USER_CAPABILITIES_GET (0x01)|Command = USER_CAPABILITIES_GET (0x01)|Command = USER_CAPABILITIES_GET (0x01)|Command = USER_CAPABILITIES_GET (0x01)|Command = USER_CAPABILITIES_GET (0x01)|Command = USER_CAPABILITIES_GET (0x01)|Command = USER_CAPABILITIES_GET (0x01)|Command = USER_CAPABILITIES_GET (0x01)|



**2.2.118.5** **User** **Capabilities** **Report** **Command**


This command is used to report User capabilities and limits from the node.













|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|
|Command = USER_CAPABILITIES_REPORT (0x02)<br>|Command = USER_CAPABILITIES_REPORT (0x02)<br>|Command = USER_CAPABILITIES_REPORT (0x02)<br>|Command = USER_CAPABILITIES_REPORT (0x02)<br>|Command = USER_CAPABILITIES_REPORT (0x02)<br>|Command = USER_CAPABILITIES_REPORT (0x02)<br>|Command = USER_CAPABILITIES_REPORT (0x02)<br>|Command = USER_CAPABILITIES_REPORT (0x02)<br>|
|Number of supported User Unique Identifers (MSB)<br>|Number of supported User Unique Identifers (MSB)<br>|Number of supported User Unique Identifers (MSB)<br>|Number of supported User Unique Identifers (MSB)<br>|Number of supported User Unique Identifers (MSB)<br>|Number of supported User Unique Identifers (MSB)<br>|Number of supported User Unique Identifers (MSB)<br>|Number of supported User Unique Identifers (MSB)<br>|
|Number of supported User Unique Identifers (LSB)|Number of supported User Unique Identifers (LSB)|Number of supported User Unique Identifers (LSB)|Number of supported User Unique Identifers (LSB)|Number of supported User Unique Identifers (LSB)|Number of supported User Unique Identifers (LSB)|Number of supported User Unique Identifers (LSB)|Number of supported User Unique Identifers (LSB)|
|Supported Credential Rules Bit Mask|Supported Credential Rules Bit Mask|Supported Credential Rules Bit Mask|Supported Credential Rules Bit Mask|Supported Credential Rules Bit Mask|Supported Credential Rules Bit Mask|Supported Credential Rules Bit Mask|Supported Credential Rules Bit Mask|
|Max Length of User Name|Max Length of User Name|Max Length of User Name|Max Length of User Name|Max Length of User Name|Max Length of User Name|Max Length of User Name|Max Length of User Name|
|User Schedule<br>Support|All Users<br>Checksum<br>Support|User Checksum<br>Support|Reserved|Reserved|Reserved|Reserved|Reserved|
|Supported User Types Bit Mask Length|Supported User Types Bit Mask Length|Supported User Types Bit Mask Length|Supported User Types Bit Mask Length|Supported User Types Bit Mask Length|Supported User Types Bit Mask Length|Supported User Types Bit Mask Length|Supported User Types Bit Mask Length|
|Supported User Types Bit Mask 1|Supported User Types Bit Mask 1|Supported User Types Bit Mask 1|Supported User Types Bit Mask 1|Supported User Types Bit Mask 1|Supported User Types Bit Mask 1|Supported User Types Bit Mask 1|Supported User Types Bit Mask 1|
|…|…|…|…|…|…|…|…|
|Supported User Types Bit Mask N|Supported User Types Bit Mask N|Supported User Types Bit Mask N|Supported User Types Bit Mask N|Supported User Types Bit Mask N|Supported User Types Bit Mask N|Supported User Types Bit Mask N|Supported User Types Bit Mask N|


**Number** **of** **supported** **User** **Unique** **Identifiers** **(16** **bits)**

This field advertises the maximum number of Users supported by the node. Refer to _User_ _Set_ _Com-_
_mand_ for details. details.

CC:0083.01.02.11.000 This field MUST NOT be set to zero.


**Supported** **Credential** **Rules** **Bit** **Mask** **(8** **bits)**

This field advertises the supported Credential Rules at the sending node. Refer to Table 2.538 for
details.


CC:0083.01.02.11.001 A supporting node MUST support at least one Credential Rule.

CC:0083.01.02.11.002 This field MUST be encoded according to the following interpretation:


CC:0083.01.02.11.003 - Bit 0 in Bit Mask MUST be set to 0.


      - Bit 1 in Bit Mask represents Credential Rule = 0x01 (Single).


      - Bit 2 in Bit Mask represents Credential Rule = 0x02 (Dual).


      - Bit 3 in Bit Mask represents Credential Rule = 0x03 (Triple).


CC:0083.01.02.11.004 If a Credential Rule is supported, the corresponding bit MUST be set to ‘1’.


CC:0083.01.02.11.005 If a Credential Rule is not supported, the corresponding bit MUST be set to ‘0’.


CC:0083.01.02.11.006 The bits set MUST comply with Table 2.538.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 537




<!-- PAGE 539 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**Max** **Length** **of** **User** **Name** **(8** **bits)**

This field advertises the maximum length of User Name field supported by the node. Refer to _User_
_Set_ _Command_ for details.


CC:0083.01.02.13.007 If a User Name is received which is longer than the maximum allowed length, it MAY be truncated
to fit.


CC:0083.01.02.11.008 A node MUST NOT send a User Name longer than the Max Length of User Name reported in the
User Capabilities report.


**User** **Schedule** **Support** **(1** **bit)**

This field indicates if the sending node supports scheduling access for a User Unique Identifier via the
_Schedule_ _Entry_ _Lock_ _Command_ _Class,_ _version_ _4_ _[NEVER_ _CERTIFIED]_ or higher.


CC:0083.01.02.11.009 The value 1 MUST indicate that the User Schedule functionality is supported.


CC:0083.01.02.11.010 The value 0 MUST indicate that the User Schedule functionality is not supported.


**All** **Users** **Checksum** **Support** **(1** **bit)**

This field indicates if the sending node supports the All Users Checksum functionality. Refer to _All_
_Users_ _Checksum_ _Get_ _Command_ for details.


CC:0083.01.02.11.011 The value 1 MUST indicate that the All Users Checksum functionality is supported.


CC:0083.01.02.11.012 The value 0 MUST indicate that the All Users Checksum functionality is not supported.


CC:0083.01.02.12.013 If only one checksum is going to be supported, it is RECOMMENDED that the All Users Checksum functionality be supported over _User_ _Checksum_ _Get_ _Command_ and _Credential_ _Checksum_ _Get_
_Command_ .


**User** **Checksum** **Support** **(1** **bit)**

This field indicates if the sending node supports the User Checksum functionality. Refer to _User_
_Checksum_ _Get_ _Command_ for details.


CC:0083.01.02.11.014 The value 1 MUST indicate that the User Checksum functionality is supported.


CC:0083.01.02.11.015 The value 0 MUST indicate that the User Checksum functionality is not supported.


**Reserved** **(5** **bits)**

CC:0083.01.02.11.016 This field MUST be set to zero by a sending node and MUST be ignored by a receiving node.


**Supported** **User** **Types** **Bit** **Mask** **Length** **(8** **bits)**

This field advertises the number of bytes in the following Supported User Types Bit Mask. Refer to
Table 2.536 for details.


**Supported** **User** **Types** **Bit** **Mask** **(N** **bytes)**

This field advertises the supported User Types at the sending node. Refer to Table 2.536 for details.


CC:0083.01.02.11.017 A supporting node MUST support at least one User Type.

CC:0083.01.02.11.018 This field MUST be encoded according to the following interpretation:


      - Bit 0 in Bit Mask 1 represents User Type = 0x00 (General User).


      - Bit 3 in Bit Mask 1 represents User Type = 0x03 (Programming User).


      - Bit 4 in Bit Mask 1 represents User Type = 0x04 (Non-Access User).


      - …


CC:0083.01.02.11.019 If a User Type is supported, the corresponding bit MUST be set to ‘1’.


CC:0083.01.02.11.020 If a User Type is not supported, the corresponding bit MUST be set to ‘0’.


CC:0083.01.02.11.021 The bits set MUST comply with Table 2.536.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 538




<!-- PAGE 540 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.118.6** **Credential** **Capabilities** **Get** **Command**


This command is used to request Credential capabilities and limits from the node.


CC:0083.01.03.11.000 The _Credential_ _Capabilities_ _Report_ _Command_ MUST be returned in response to this command.


CC:0083.01.03.11.001 This command MUST NOT be issued via multicast addressing.


CC:0083.01.03.11.002 A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast Node ID and the Multi Channel Multi-End Point
destination are all considered multicast addressing methods.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|
|Command = CREDENTIAL_CAPABILITIES_GET (0x03)|Command = CREDENTIAL_CAPABILITIES_GET (0x03)|Command = CREDENTIAL_CAPABILITIES_GET (0x03)|Command = CREDENTIAL_CAPABILITIES_GET (0x03)|Command = CREDENTIAL_CAPABILITIES_GET (0x03)|Command = CREDENTIAL_CAPABILITIES_GET (0x03)|Command = CREDENTIAL_CAPABILITIES_GET (0x03)|Command = CREDENTIAL_CAPABILITIES_GET (0x03)|



**2.2.118.7** **Credential** **Capabilities** **Report** **Command**


This command is used to report Credential capabilities and limits from the node.







|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|
|Command = CREDENTIAL_CAPABILITIES_REPORT (0x04)|Command = CREDENTIAL_CAPABILITIES_REPORT (0x04)|Command = CREDENTIAL_CAPABILITIES_REPORT (0x04)|Command = CREDENTIAL_CAPABILITIES_REPORT (0x04)|Command = CREDENTIAL_CAPABILITIES_REPORT (0x04)|Command = CREDENTIAL_CAPABILITIES_REPORT (0x04)|Command = CREDENTIAL_CAPABILITIES_REPORT (0x04)|Command = CREDENTIAL_CAPABILITIES_REPORT (0x04)|
|Credential<br>Check-<br>sum Support|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|
|Number of Supported Credential Types|Number of Supported Credential Types|Number of Supported Credential Types|Number of Supported Credential Types|Number of Supported Credential Types|Number of Supported Credential Types|Number of Supported Credential Types|Number of Supported Credential Types|
|Credential Type [Type N]|Credential Type [Type N]|Credential Type [Type N]|Credential Type [Type N]|Credential Type [Type N]|Credential Type [Type N]|Credential Type [Type N]|Credential Type [Type N]|
|…|…|…|…|…|…|…|…|
|Credential Type [Type M]|Credential Type [Type M]|Credential Type [Type M]|Credential Type [Type M]|Credential Type [Type M]|Credential Type [Type M]|Credential Type [Type M]|Credential Type [Type M]|
|CL Support [Type<br>N]|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|
|…|…|…|…|…|…|…|…|
|CL Support [Type<br>M]|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|
|Number of Supported Credential Slots [Type N] (MSB)|Number of Supported Credential Slots [Type N] (MSB)|Number of Supported Credential Slots [Type N] (MSB)|Number of Supported Credential Slots [Type N] (MSB)|Number of Supported Credential Slots [Type N] (MSB)|Number of Supported Credential Slots [Type N] (MSB)|Number of Supported Credential Slots [Type N] (MSB)|Number of Supported Credential Slots [Type N] (MSB)|
|Number of Supported Credential Slots [Type N] (LSB)|Number of Supported Credential Slots [Type N] (LSB)|Number of Supported Credential Slots [Type N] (LSB)|Number of Supported Credential Slots [Type N] (LSB)|Number of Supported Credential Slots [Type N] (LSB)|Number of Supported Credential Slots [Type N] (LSB)|Number of Supported Credential Slots [Type N] (LSB)|Number of Supported Credential Slots [Type N] (LSB)|
|…|…|…|…|…|…|…|…|
|Number of Supported Credential Slots [Type M] (MSB)|Number of Supported Credential Slots [Type M] (MSB)|Number of Supported Credential Slots [Type M] (MSB)|Number of Supported Credential Slots [Type M] (MSB)|Number of Supported Credential Slots [Type M] (MSB)|Number of Supported Credential Slots [Type M] (MSB)|Number of Supported Credential Slots [Type M] (MSB)|Number of Supported Credential Slots [Type M] (MSB)|
|Number of Supported Credential Slots [Type M] (LSB)|Number of Supported Credential Slots [Type M] (LSB)|Number of Supported Credential Slots [Type M] (LSB)|Number of Supported Credential Slots [Type M] (LSB)|Number of Supported Credential Slots [Type M] (LSB)|Number of Supported Credential Slots [Type M] (LSB)|Number of Supported Credential Slots [Type M] (LSB)|Number of Supported Credential Slots [Type M] (LSB)|
|Min Length of Credential Data [Type N] (MSB)|Min Length of Credential Data [Type N] (MSB)|Min Length of Credential Data [Type N] (MSB)|Min Length of Credential Data [Type N] (MSB)|Min Length of Credential Data [Type N] (MSB)|Min Length of Credential Data [Type N] (MSB)|Min Length of Credential Data [Type N] (MSB)|Min Length of Credential Data [Type N] (MSB)|
|Min Length of Credential Data [Type N] (LSB)|Min Length of Credential Data [Type N] (LSB)|Min Length of Credential Data [Type N] (LSB)|Min Length of Credential Data [Type N] (LSB)|Min Length of Credential Data [Type N] (LSB)|Min Length of Credential Data [Type N] (LSB)|Min Length of Credential Data [Type N] (LSB)|Min Length of Credential Data [Type N] (LSB)|
|…|…|…|…|…|…|…|…|
|Min Length of Credential Data [Type M] (MSB)|Min Length of Credential Data [Type M] (MSB)|Min Length of Credential Data [Type M] (MSB)|Min Length of Credential Data [Type M] (MSB)|Min Length of Credential Data [Type M] (MSB)|Min Length of Credential Data [Type M] (MSB)|Min Length of Credential Data [Type M] (MSB)|Min Length of Credential Data [Type M] (MSB)|
|Min Length of Credential Data [Type M] (LSB)|Min Length of Credential Data [Type M] (LSB)|Min Length of Credential Data [Type M] (LSB)|Min Length of Credential Data [Type M] (LSB)|Min Length of Credential Data [Type M] (LSB)|Min Length of Credential Data [Type M] (LSB)|Min Length of Credential Data [Type M] (LSB)|Min Length of Credential Data [Type M] (LSB)|
|Max Length of Credential Data [Type N] (MSB)|Max Length of Credential Data [Type N] (MSB)|Max Length of Credential Data [Type N] (MSB)|Max Length of Credential Data [Type N] (MSB)|Max Length of Credential Data [Type N] (MSB)|Max Length of Credential Data [Type N] (MSB)|Max Length of Credential Data [Type N] (MSB)|Max Length of Credential Data [Type N] (MSB)|
|Max Length of Credential Data [Type N] (LSB)|Max Length of Credential Data [Type N] (LSB)|Max Length of Credential Data [Type N] (LSB)|Max Length of Credential Data [Type N] (LSB)|Max Length of Credential Data [Type N] (LSB)|Max Length of Credential Data [Type N] (LSB)|Max Length of Credential Data [Type N] (LSB)|Max Length of Credential Data [Type N] (LSB)|
|…|…|…|…|…|…|…|…|
|Max Length of Credential Data [Type M] (MSB)|Max Length of Credential Data [Type M] (MSB)|Max Length of Credential Data [Type M] (MSB)|Max Length of Credential Data [Type M] (MSB)|Max Length of Credential Data [Type M] (MSB)|Max Length of Credential Data [Type M] (MSB)|Max Length of Credential Data [Type M] (MSB)|Max Length of Credential Data [Type M] (MSB)|
|Max Length of Credential Data [Type M] (LSB)|Max Length of Credential Data [Type M] (LSB)|Max Length of Credential Data [Type M] (LSB)|Max Length of Credential Data [Type M] (LSB)|Max Length of Credential Data [Type M] (LSB)|Max Length of Credential Data [Type M] (LSB)|Max Length of Credential Data [Type M] (LSB)|Max Length of Credential Data [Type M] (LSB)|
|CL Recommended Timeout [Type N]|CL Recommended Timeout [Type N]|CL Recommended Timeout [Type N]|CL Recommended Timeout [Type N]|CL Recommended Timeout [Type N]|CL Recommended Timeout [Type N]|CL Recommended Timeout [Type N]|CL Recommended Timeout [Type N]|
|…|…|…|…|…|…|…|…|
|CL Recommended Timeout [Type M]|CL Recommended Timeout [Type M]|CL Recommended Timeout [Type M]|CL Recommended Timeout [Type M]|CL Recommended Timeout [Type M]|CL Recommended Timeout [Type M]|CL Recommended Timeout [Type M]|CL Recommended Timeout [Type M]|
|CL Number of Steps [Type N]|CL Number of Steps [Type N]|CL Number of Steps [Type N]|CL Number of Steps [Type N]|CL Number of Steps [Type N]|CL Number of Steps [Type N]|CL Number of Steps [Type N]|CL Number of Steps [Type N]|
|…|…|…|…|…|…|…|…|
|CL Number of Steps [Type M]|CL Number of Steps [Type M]|CL Number of Steps [Type M]|CL Number of Steps [Type M]|CL Number of Steps [Type M]|CL Number of Steps [Type M]|CL Number of Steps [Type M]|CL Number of Steps [Type M]|


**Credential** **Checksum** **Support** **(1** **bit)**


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 539




<!-- PAGE 541 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


This field indicates if the sending node supports the Credential Checksum functionality. Refer to
_Credential_ _Checksum_ _Get_ _Command_ for details.


CC:0083.01.04.11.000 The value 1 MUST indicate that the Credential Checksum functionality is supported.


CC:0083.01.04.11.001 The value 0 MUST indicate that the Credential Checksum functionality is not supported.


**Reserved** **(7** **bits)**

CC:0083.01.04.11.002 This field MUST be set to zero by a sending node and MUST be ignored by a receiving node.


**Number** **of** **Supported** **Credential** **Types** **(8** **bits)**

This field advertises the number of supported Credential Types.

CC:0083.01.04.11.003 This field MUST be followed by the following seven blocks of that size:


      - Credential Type (8 bits      - Number of Supported Credential Types)

      - Credential Learn Support flag and 7 Reserved bits (8 bits      - Number of Supported Credential
Types)


      - Number of Supported Credential Slots for Type (16 bits      - Number of Supported Credential
Types)


      Min Length of Credential Data per Slot for Type fields (16 bits * Number of Supported Credential
Types)

      - Max Length of Credential Data per Slot for Type fields (16 bits      - Number of Supported Credential Types)


      Credential Learn (CL) Recommended Timeout (8 bits * Number of Supported Credential Types)


      - Credential Learn (CL) Number of Steps (8 bits      - Number of Supported Credential Types)


**Credential** **Type** **(8** **bits)**

This field advertises a supported Credential Type by this node.

CC:0083.01.04.11.004 This field MUST comply with values listed in Table 2.542.


**Credential** **Learn** **(CL)** **Support** **(1** **bit)**

This field indicates if the sending node supports the Credential Learn functionality for that specific
Credential Type.

CC:0083.01.04.11.005 The value 1 MUST indicate that the Credential Learn functionality is supported for that specific
Credential Type.

CC:0083.01.04.11.006 The value 0 MUST indicate that the Credential Learn functionality is not supported for that specific
Credential Type.


**Reserved** **(7** **bits)**

CC:0083.01.04.11.007 This field MUST be set to zero by a sending node and MUST be ignored by a receiving node.


**Number** **of** **Supported** **Credential** **Slots** **(16** **bits)**

This field advertises the total number of supported Credential Slots for the given Credential Type.
Refer to _Credential_ _Set_ _Command_ for details.


CC:0083.01.04.13.008 Those Credential Slots MAY be distributed amongst Users unequally.

CC:0083.01.04.11.009 This field MUST NOT be set to zero.


**Min** **Length** **of** **Credential** **Data** **(16** **bits)**

This field advertises the minimum length of the Credential Data per Slot for the given Credential
Type. Refer to _Credential_ _Set_ _Command_ for details.


**Max** **Length** **of** **Credential** **Data** **(16** **bits)**

This field advertises the maximum length of the Credential Data per Slot for the given Credential
Type. Refer to _Credential_ _Set_ _Command_ for details.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 540




<!-- PAGE 542 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**Credential** **Learn** **(CL)** **Recommended** **Timeout** **(8** **bits)**

CC:0083.01.04.11.010 This field indicates the recommended timeout for each step in the credential learn flow in seconds. If
this credential type cannot be learned, this field MUST be 0. If this credential type can be learned,
this field MUST NOT be 0.


**Credential** **Learn** **(CL)** **Number** **of** **Steps** **(8** **bits)**

CC:0083.01.04.11.011 This field indicates the number of steps required in the credential learn flow. If this credential type
cannot be learned, this field MUST be 0. If this credential type can be learned, this field MUST NOT
be 0.


**2.2.118.8** **User** **Set** **Command**


This command is used to add, delete, or modify Users in the node.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|
|Command = USER_SET (0x05)|Command = USER_SET (0x05)|Command = USER_SET (0x05)|Command = USER_SET (0x05)|Command = USER_SET (0x05)|Command = USER_SET (0x05)|Command = USER_SET (0x05)|Command = USER_SET (0x05)|
|Reserved<br>|Reserved<br>|Reserved<br>|Reserved<br>|Reserved<br>|Reserved<br>|Operation Type|Operation Type|
|User Unique Identifer (MSB)<br>|User Unique Identifer (MSB)<br>|User Unique Identifer (MSB)<br>|User Unique Identifer (MSB)<br>|User Unique Identifer (MSB)<br>|User Unique Identifer (MSB)<br>|User Unique Identifer (MSB)<br>|User Unique Identifer (MSB)<br>|
|User Unique Identifer (LSB)|User Unique Identifer (LSB)|User Unique Identifer (LSB)|User Unique Identifer (LSB)|User Unique Identifer (LSB)|User Unique Identifer (LSB)|User Unique Identifer (LSB)|User Unique Identifer (LSB)|
|User Type|User Type|User Type|User Type|User Type|User Type|User Type|User Type|
|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|User Active<br>State|
|Credential Rule|Credential Rule|Credential Rule|Credential Rule|Credential Rule|Credential Rule|Credential Rule|Credential Rule|
|Expiring Timeout Minutes (MSB)|Expiring Timeout Minutes (MSB)|Expiring Timeout Minutes (MSB)|Expiring Timeout Minutes (MSB)|Expiring Timeout Minutes (MSB)|Expiring Timeout Minutes (MSB)|Expiring Timeout Minutes (MSB)|Expiring Timeout Minutes (MSB)|
|Expiring Timeout Minutes (LSB)|Expiring Timeout Minutes (LSB)|Expiring Timeout Minutes (LSB)|Expiring Timeout Minutes (LSB)|Expiring Timeout Minutes (LSB)|Expiring Timeout Minutes (LSB)|Expiring Timeout Minutes (LSB)|Expiring Timeout Minutes (LSB)|
|Reserved|Reserved|Reserved|Reserved|Reserved|User Name Encoding|User Name Encoding|User Name Encoding|
|User Name Length|User Name Length|User Name Length|User Name Length|User Name Length|User Name Length|User Name Length|User Name Length|
|User Name|User Name|User Name|User Name|User Name|User Name|User Name|User Name|



**Reserved** **(6** **bits)**

CC:0083.01.05.11.000 This field MUST be set to zero by a sending node and MUST be ignored by a receiving node.


**Operation** **Type** **(2** **bits)**

The Operation Type field indicates the event to change User data.

CC:0083.01.05.11.001 This field MUST comply with Table 2.535.


CC:0083.01.05.11.002

Table 2.535: User Set::Operation Type

|Value|Name|i<br>Defnition|
|---|---|---|
|0x00|Add|A user with this User Unique Identifer is added.<br>|
|0x01|Modify|A user with this User Unique Identifer is modifed. The<br>felds in this command MUST overwrite existing user data<br>unless the data is rejected as invalid.<br>|
|0x02|Delete|A user with this User Unique Identifer is deleted. Other<br>felds aside from the User Unique Identifer and Delete Op-<br>eration Type in this command MUST be ignored. Other<br>felds aside from the User Unique Identifer and Delete Op-<br>eration Type MAY be set to default values or not included<br>at all. All Credentials and schedules associated with this<br>user MUST also be deleted.|



CC:0083.01.05.11.003 All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.

**User** **Unique** **Identifier** **(16** **bits)**


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 541




<!-- PAGE 543 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


The User Unique Identifier is used to recognize the user identity across the devices in a single network.
This is a sixteen bit value that is supplied by the controller at the time of User Unique Identifier
creation. Or, this value is specified by the node at creation time if the User Unique Identifier is locally
generated via the node’s local interface.

CC:0083.01.05.11.004 A User Unique Identifier MUST be any number in the range 1-65535.


CC:0083.01.05.13.005 A node MAY only support fewer than 65535 Users, as advertised in the _User_ _Capabilities_ _Report_
_Command_ .

CC:0083.01.05.11.006 Zero is an invalid User Unique Identifier and MUST NOT be used by the node unless in a _User_ _Report_
_Command_ which is being returned in response to a _User_ _Get_ _Command_ containing a User Unique
Identifier of 0, and there are no existing users at the node.


CC:0083.01.05.11.007 Zero MUST be ignored by the receiving node unless received with the Delete Operation Type, in
which case all users and their associated credentials and schedules MUST be deleted.

CC:0083.01.05.11.008 If the User Unique Identifier is set to 0, all other fields aside from the Operation Type MUST be
ignored, and those other fields MAY be set to default values or not included at all.

CC:0083.01.05.11.009 To clear all Users and their associated Credentials and schedules, the User Unique Identifier MUST
be set to 0 with the Delete Operation Type.

CC:0083.01.05.11.010 If all users are deleted, a _Notification_ _Report_ _Command_ with Notification Type “Access Control”
(0x06) and Notification Event “All users deleted” (0x25) MUST be sent.

CC:0083.01.05.11.011 If a user is added, a _Notification_ _Report_ _Command_ with Notification Type “Access Control” (0x06),
Notification Event “User added” (0x27), and Event/State parameters of only a _User_ _Notification_
_Report_ _Command_ of the newly added data MUST be sent.

CC:0083.01.05.11.012 If a user is modified, a _Notification Report_ _Command_ with Notification Type “Access Control” (0x06),
Notification Event “User modified” (0x28), and Event/State parameters of only a _User_ _Notification_
_Report_ _Command_ of the newly modified data MUST be sent.

CC:0083.01.05.11.013 If a single user is deleted, a _Notification_ _Report_ _Command_ with Notification Type “Access Control”
(0x06), Notification Event “User deleted” (0x29), and Event/State parameters of only a _User_ _Notifi-_
_cation_ _Report_ _Command_ of the deleted data MUST be sent, even if that user is the last one on the
node.

CC:0083.01.05.11.014 If a User Unique Identifier is specified in this command as greater than the max advertised in the
_User_ _Capabilities_ _Report_ _Command_, a receiving node MUST ignore the command.


CC:0083.01.05.11.015
If a User Unique Identifier is specified in this command as zero for an Add or Modify Operation Type,
a receiving node MUST ignore the command

CC:0083.01.05.11.016 Any Credential added to the node MUST be associated with a User Unique Identifier.


CC:0083.01.05.11.017 There MUST NOT be a limit to the number of credentials that can be assigned to a single User
Unique Identifier.


CC:0083.01.05.12.018 However, all credentials SHOULD NOT be put on a single user.


**User** **Type** **(8** **bits)**


CC:0083.01.05.11.019 The User Type determines the category of access given to a user. It is used to assign the user when
created or modified. This field MUST comply with Table 2.536.


CC:0083.01.05.11.020


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 542




<!-- PAGE 544 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024



Table 2.536: User Set::User Type


























|Numeric<br>Value (User<br>Set Com-<br>mand)|Bit Value<br>(User Ca-<br>pabilities<br>Report<br>Command)|Name|i<br>Defnition|
|---|---|---|---|
|0x00|0x01|General<br>User|User has access, provided proper Credential is sup-<br>plied.|
|0x01|0x02|Reserved|N/A.|
|0x02|0x04|Reserved|N/A.|
|0x03|0x08|Program-<br>ming User|User has the ability to both program and MAY op-<br>erate the node. This user can manage the users and<br>user schedules. In all other respects the user matches<br>the general (default) user. Programming User is the<br>only user that can disable the user interface (keypad,<br>remote, etc.). This can also be referred to as admin<br>user.|
|0x04|0x10|Non-Access<br>User|User is recognized by the node but does not have the<br>ability to open the node. This user will only cause<br>the node to generate the appropriate event notifca-<br>tion to any associated device.<br>When a non-access<br>event is generated, a _Notifcation Report Command_<br>with Notifcation Type “Access Control” (0x06), No-<br>tifcation Event “Non-Access credential entered via<br>local interface” (0x33), and Event/State parameters<br>of a _Credential Notifcation Report Command_, con-<br>taining only the User Unique Identifer, Credential<br>Type, and Credential Slot Number felds MUST be<br>sent.<br>|
|0x05|0x20|Duress User|User has the ability to open the node but a _Notifca-_<br>_tion Report Command_ with Notifcation Type “Emer-<br>gency Alarm” (0x0A) and Notifcation Event “Panic<br>Alert” (0x04) MUST also be sent to the Lifeline as-<br>sociation group when a Credential is used to alert<br>emergency services or contacts.|
|0x06|0x40|Disposable<br>User|User has the ability to open the node once after which<br>the node MUST change the corresponding user record<br>User Active State value to Occupied Disabled auto-<br>matically by the node. The User Active State MUST<br>NOT be set to Occupied Disabled if there is an en-<br>abled, inactive schedule attached to the user.<br>|
|0x07|0x80|Expiring<br>User|User has the ability to open the node for a specifed<br>time in Expiring Timeout Minutes after the frst use<br>of the PIN code, RFID code, Fingerprint, or other<br>Credential. After the time has elapsed, the User Ac-<br>tive State value MUST be set to Occupied Disabled<br>automatically by the node.<br>The node MUST per-<br>sist the timeout across reboots such that the specifed<br>time is honored. If this user has an enabled schedule<br>attached to it, the Expiring Timeout Minutes count-<br>down MUST NOT start unless the credential is en-<br>tered during that schedule’s active period.|
|0x08|0x01<br>(sec-<br>ond byte)|Reserved|N/A.|
|0x09|0x02<br>(sec-<br>ond byte)|Remote<br>Only User|User access and PIN code is restricted to remote<br>lock/unlock commands only. This type of user might<br>be useful for regular delivery services to prevent a PIN<br>code Credential created for them from being used at<br>the keypad. The PIN code Credential would only be|
|© 2024 Z-Wave All|iance, Inc. All Righ|ts Reserved<br>Th|provided over-the-air for the lock/unlock commands.<br>is document may only be copied and distributed internally. Page 543|




<!-- PAGE 545 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


CC:0083.01.05.11.021 All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.


CC:0083.01.05.11.022 All User Types except the Programming User (0x03) MUST be allowed to be assigned a schedule.


CC:0083.01.05.11.023 Programming User (0x03) MUST NOT be scheduled.

CC:0083.01.05.11.024 If a User Type is updated from a different User Type to Programming User (0x03) and the user has
an associated schedule, the schedule MUST be deleted automatically by the node.


CC:0083.01.05.11.025 If a user has a schedule and it is enabled but inactive, the node MUST NOT allow the user to access
the node with its assigned Credential(s) and MAY instead send a _Notification_ _Report_ _Command_ with
Notification Type “Access Control” (0x06), Notification Event “Valid credential access denied due to
the User’s schedule being inactive” (0x30), and Event/State parameters of a _Credential_ _Notification_
_Report_ _Command_, containing only the User Unique Identifier, Credential Type, and Credential Slot
Number fields.


CC:0083.01.05.11.026 If a user has a schedule and it is disabled, the node MUST allow the user 24/7 permanent access to
the node with its assigned Credential(s).


CC:0083.01.05.11.027 If a user’s credential is used to lock/close the node where the User Type is not Non-Access User,
a _Notification_ _Report_ _Command_ with Notification Type “Access Control” (0x06), Notification Event
“Credential lock/close operation” (0x23), and Event/State parameters of a _Credential_ _Notification_
_Report_ _Command_, containing only the User Unique Identifier, Credential Type, and Credential Slot
Number fields MUST be sent.


CC:0083.01.05.11.028 If a user’s credential is used to unlock/open the node where the User Type is not Non-Access User,
a _Notification_ _Report_ _Command_ with Notification Type “Access Control” (0x06), Notification Event
“Credential unlock/open operation” (0x24), and Event/State parameters of a _Credential_ _Notification_
_Report_ _Command_, containing only the User Unique Identifier, Credential Type, and Credential Slot
Number fields MUST be sent.


CC:0083.01.05.11.029 If a Non-Access User Type’s credential is entered at the node and that user’s access is valid (User
Active State is Occupied Enabled and access is not restricted via schedule at the time the credential is
entered), a _Notification Report Command_ with Notification Type “Access Control” (0x06), Notification
Event “Non-Access credential entered via local interface” (0x33), and Event/State parameters of a
_Credential Notification Report Command_, containing only the User Unique Identifier, Credential Type,
and Credential Slot Number fields MUST be sent.

CC:0083.01.05.11.030 If a User Type is specified in this command as one not advertised as supported in the _User Capabilities_
_Report_ _Command_, a receiving node MUST ignore the command.


**Reserved** **(7** **bits)**

CC:0083.01.05.11.031 This field MUST be set to zero by a sending node and MUST be ignored by a receiving node.


**User** **Active** **State** **(1** **bit)**


The User Active State determines whether a user is allowed to access the node or not with its assigned
Credentials. It is used to assign the user when created or modified.

CC:0083.01.05.11.032 This field MUST comply with Table 2.537.


Table 2.537: User Set::User Active State

|Value|Name|i<br>Defnition|
|---|---|---|
|0x00|Occupied Disabled|Access not Granted|
|0x01|Occupied Enabled|Access Granted|



CC:0083.01.05.11.033 All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.


CC:0083.01.05.11.034 If a User Active State is set to Occupied Disabled, the node MUST NOT allow the user to access
the node with its assigned Credential(s) and MAY instead send a _Notification_ _Report_ _Command_
with Notification Type “Access Control” (0x06), Notification Event “Valid credential access denied
due to User Active State being set to Occupied Disabled” (0x2F), and Event/State parameters of


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 544




<!-- PAGE 546 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


a _Credential_ _Notification_ _Report_ _Command_, containing only the User Unique Identifier, Credential
Type, and Credential Slot Number fields.


**Credential** **Rule** **(8** **bits)**


The Credential Rule is used to identify multi-factor authentication for the user.


CC:0083.01.05.11.035 The Credential Rule enumeration used in various commands MUST indicate the Credential rule that

can be applied to a particular user.

CC:0083.01.05.11.036 This field MUST comply with Table 2.538.


CC:0083.01.05.11.037



Table 2.538: User Set::Credential Rule







|Numeric Value (User<br>Set Command)|Bit Value (User Ca-<br>pabilities Report Com-<br>mand)|Name|i<br>Defnition|
|---|---|---|---|
|0x01|0x02|Single|Only<br>one<br>Credential<br>is<br>RE-<br>QUIRED for node operation.|
|0x02|0x04|Dual|Any two Credentials are RE-<br>QUIRED for node operation.|
|0x03|0x08|Triple|Any three Credentials are RE-<br>QUIRED for node operation.|


CC:0083.01.05.11.038 All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.

CC:0083.01.05.11.039 If a Credential Rule is specified in this command as one not advertised as supported in the _User_
_Capabilities_ _Report_ _Command_, a receiving node MUST ignore the command.


CC:0083.01.05.11.040 If a user enters at least one but not enough credentials for the User’s Credential Rule, the node MUST
NOT allow the user to access the node and MAY instead send a _Notification_ _Report_ _Command_ with
Notification Type “Access Control” (0x06), Notification Event “User access denied due to not enough
credentials entered for the User’s Credential Rule” (0x31), and Event/State parameters of only the
Number of Credential Blocks and then for each entered Credential: a _Credential_ _Notification_ _Report_
_Command_, containing only the User Unique Identifier, Credential Type, and Credential Slot Number
fields.


**Expiring** **Timeout** **Minutes** **(16** **bits)**


CC:0083.01.05.11.041 If the User Type is Expiring User, then this is the time, in minutes, the user is able to use their
Credentials before User Active State value MUST be automatically set to Occupied Disabled.

CC:0083.01.05.11.042 If the User Type is Expiring User, this field MUST be set to a non-zero value.

CC:0083.01.05.11.053 For all other User Types, this field MUST be set to zero and MUST be ignored by a receiving node.


**Reserved** **(5** **bits)**

CC:0083.01.05.11.043 This field MUST be set to zero by a sending node and MUST be ignored by a receiving node.


**User** **Name** **Encoding** **(3** **bits)**

CC:0083.01.05.11.044 This field is used to indicate the character encoding for the User Name char field. This field MUST
comply with Table 2.539.

|Value|Table 2.539: User Name Encoding Description|
|---|---|
|Value|Description|
|0x00|Using standard ASCII codes, see _ASCII Codes_ (values 128-255 are ig-<br>nored)|
|0x01|Using standard and OEM Extended ASCII codes, see _ASCII Codes_.|
|0x02|Unicode UTF-16, in big endian order|



CC:0083.01.05.11.045 All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 545




<!-- PAGE 547 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**User** **Name** **Length** **(8** **bits)**

This field specifies the length of the following User Name field, in bytes.

CC:0083.01.05.12.046 The User Name SHOULD be no longer than “Max Length of User Name” specified in the _User_
_Capabilities_ _Report_ _Command_ .


CC:0083.01.05.13.047 If the name is longer, it MAY be truncated.


CC:0083.01.05.11.054 If the name causes the full z-wave command not to respect the Z-Wave MAC frame size or Transport
service limits, it MUST be truncated.


**User** **Name** **(Variable** **Length)**

This field specifies the User’s name.

CC:0083.01.05.13.048 Names are human readable identifiers that MAY be shared between multiple sources controlling the
same node.


CC:0083.01.05.11.049 The User Name MUST be consistent with the given encoding scheme and length.


CC:0083.01.05.11.050 The User Name is not NULL-terminated. User Name Length MUST be used to determine a name’s
length.


CC:0083.01.05.12.051 If the User Name is not provided, it SHOULD be set to the default value.

CC:0083.01.05.12.052 The default value SHOULD be “User-[UniqueUserIdentifier]” where [UniqueUserIdentifier] is the decimal User Unique Identifier without padding (e.g. User-7, User-275).


**2.2.118.9** **User** **Get** **Command**


This command is used to retrieve data about a specified User.


CC:0083.01.06.11.000 The _User_ _Report_ _Command_ MUST be returned in response to this command.


CC:0083.01.06.11.001 This command MUST NOT be issued via multicast addressing.


CC:0083.01.06.11.002 A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast Node ID and the Multi Channel Multi-End Point
destination are all considered multicast addressing methods.




|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|
|Command = USER_GET (0x06)<br>|Command = USER_GET (0x06)<br>|Command = USER_GET (0x06)<br>|Command = USER_GET (0x06)<br>|Command = USER_GET (0x06)<br>|Command = USER_GET (0x06)<br>|Command = USER_GET (0x06)<br>|Command = USER_GET (0x06)<br>|
|User Unique Identifer (MSB)<br>|User Unique Identifer (MSB)<br>|User Unique Identifer (MSB)<br>|User Unique Identifer (MSB)<br>|User Unique Identifer (MSB)<br>|User Unique Identifer (MSB)<br>|User Unique Identifer (MSB)<br>|User Unique Identifer (MSB)<br>|
|User Unique Identifer (LSB)|User Unique Identifer (LSB)|User Unique Identifer (LSB)|User Unique Identifer (LSB)|User Unique Identifer (LSB)|User Unique Identifer (LSB)|User Unique Identifer (LSB)|User Unique Identifer (LSB)|



**User** **Unique** **Identifier** **(16** **bits)**

For this field’s description, refer to the _User_ _Set_ _Command_ .

CC:0083.01.06.11.003 If the User Unique Identifier is zero, then the first existing User Unique Identifier MUST be returned
in the _User_ _Report_ _Command_ .

CC:0083.01.06.11.004 If the specified User Unique Identifier does not exist, then a responding node MUST return a _User_
_Report_ _Command_ with the User Modifier Type set to 0x00 “DNE”.

CC:0083.01.06.11.005 If the requested User Unique Identifier was 0, indicating that the first existing User Unique Identifier
be returned, but there are no existing Users at the node, then a responding node MUST return a _User_
_Report_ _Command_ with the User Modifier Type set to 0x00 “DNE” and the User Unique Identifier set
to 0.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 546




<!-- PAGE 548 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.118.10** **User** **Report** **Command**


This command returns the User data.











|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|
|Command = USER_REPORT (0x07)<br>|Command = USER_REPORT (0x07)<br>|Command = USER_REPORT (0x07)<br>|Command = USER_REPORT (0x07)<br>|Command = USER_REPORT (0x07)<br>|Command = USER_REPORT (0x07)<br>|Command = USER_REPORT (0x07)<br>|Command = USER_REPORT (0x07)<br>|
|Next User Unique Identifer (MSB)<br>|Next User Unique Identifer (MSB)<br>|Next User Unique Identifer (MSB)<br>|Next User Unique Identifer (MSB)<br>|Next User Unique Identifer (MSB)<br>|Next User Unique Identifer (MSB)<br>|Next User Unique Identifer (MSB)<br>|Next User Unique Identifer (MSB)<br>|
|Next User Unique Identifer (LSB)<br>|Next User Unique Identifer (LSB)<br>|Next User Unique Identifer (LSB)<br>|Next User Unique Identifer (LSB)<br>|Next User Unique Identifer (LSB)<br>|Next User Unique Identifer (LSB)<br>|Next User Unique Identifer (LSB)<br>|Next User Unique Identifer (LSB)<br>|
|User Modifer Type<br>|User Modifer Type<br>|User Modifer Type<br>|User Modifer Type<br>|User Modifer Type<br>|User Modifer Type<br>|User Modifer Type<br>|User Modifer Type<br>|
|User Modifer Node ID (MSB)<br>|User Modifer Node ID (MSB)<br>|User Modifer Node ID (MSB)<br>|User Modifer Node ID (MSB)<br>|User Modifer Node ID (MSB)<br>|User Modifer Node ID (MSB)<br>|User Modifer Node ID (MSB)<br>|User Modifer Node ID (MSB)<br>|
|User Modifer Node ID (LSB)<br>|User Modifer Node ID (LSB)<br>|User Modifer Node ID (LSB)<br>|User Modifer Node ID (LSB)<br>|User Modifer Node ID (LSB)<br>|User Modifer Node ID (LSB)<br>|User Modifer Node ID (LSB)<br>|User Modifer Node ID (LSB)<br>|
|User Unique Identifer (MSB)<br>|User Unique Identifer (MSB)<br>|User Unique Identifer (MSB)<br>|User Unique Identifer (MSB)<br>|User Unique Identifer (MSB)<br>|User Unique Identifer (MSB)<br>|User Unique Identifer (MSB)<br>|User Unique Identifer (MSB)<br>|
|User Unique Identifer (LSB)|User Unique Identifer (LSB)|User Unique Identifer (LSB)|User Unique Identifer (LSB)|User Unique Identifer (LSB)|User Unique Identifer (LSB)|User Unique Identifer (LSB)|User Unique Identifer (LSB)|
|User Type|User Type|User Type|User Type|User Type|User Type|User Type|User Type|
|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|User Active<br>State|
|Credential Rule|Credential Rule|Credential Rule|Credential Rule|Credential Rule|Credential Rule|Credential Rule|Credential Rule|
|Expiring Timeout Minutes (MSB)|Expiring Timeout Minutes (MSB)|Expiring Timeout Minutes (MSB)|Expiring Timeout Minutes (MSB)|Expiring Timeout Minutes (MSB)|Expiring Timeout Minutes (MSB)|Expiring Timeout Minutes (MSB)|Expiring Timeout Minutes (MSB)|
|Expiring Timeout Minutes (LSB)|Expiring Timeout Minutes (LSB)|Expiring Timeout Minutes (LSB)|Expiring Timeout Minutes (LSB)|Expiring Timeout Minutes (LSB)|Expiring Timeout Minutes (LSB)|Expiring Timeout Minutes (LSB)|Expiring Timeout Minutes (LSB)|
|Reserved|Reserved|Reserved|Reserved|Reserved|User Name Encoding|User Name Encoding|User Name Encoding|
|User Name Length|User Name Length|User Name Length|User Name Length|User Name Length|User Name Length|User Name Length|User Name Length|
|User Name|User Name|User Name|User Name|User Name|User Name|User Name|User Name|


For “User Unique Identifier”, “User Type”, “User Active State”, “Credential Rule”, “Expiring Timeout
Minutes”, “User Name Encoding”, “User Name Length”, and “User Name” descriptions, refer to the
_User_ _Set_ _Command_ .

**Next** **User** **Unique** **Identifier** **(16** **bits)**

The Next User Unique Identifier is used to iterate through all Users in the User database.


CC:0083.01.07.11.000 This MUST be a non-zero value if there is at least one occupied entry after the requested User Unique
Identifier in the User database and MUST be zero if there are no more occupied entries.

An example of a using the Next User Unique Identifier to interview Users and Credentials is given in
Figure 2.27.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 547




<!-- PAGE 549 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Figure 2.27: Using Next User Unique Identifier to interview Users


**User** **Modifier** **Type** **(8** **bits)**

User Modifier Type indicates how this user was last modified on the node.


CC:0083.01.07.13.001 This MAY be used to audit all users on a node.

CC:0083.01.07.11.002 This field MUST comply with Table 2.540.


Table 2.540: User Set::User Modifier Types

|Value|Name|i<br>Defnition|
|---|---|---|
|0x00|DNE|The user does not exist and therefore has no modifer|
|0x01|Unknown|The user was added via an unknown source|
|0x02|Z-Wave|The user was added with a Z-Wave command|
|0x03|Locally|The user was added locally, such as by using a keypad or<br>admin card|
|0x04|Mobile App or other IoT<br>technology|The user was added with a mobile app without a Z-Wave<br>connection (BLE, Wi-Fi, etc.)|



CC:0083.01.07.11.003 All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.

**User** **Modifier** **Node** **ID** **(16** **bits)**

The User Modifier Node ID indicates which specific source last changed this user on the node. When
the User Modifier Type is Z-Wave, this field is the node ID of the specific node which changed the
user. For all other User Modifier Types this field’s definition is manufacturer specific.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 548




<!-- PAGE 550 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.118.11** **User** **Set** **Error** **Report** **Command**


This command returns an error message when setting User data has failed. This helps provide more
information to the controller but is not meant to provide errors for bad data being sent, such as an
unsupported User Unique Identifier.









|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|
|Command = USER_SET_ERROR_REPORT (0x08)|Command = USER_SET_ERROR_REPORT (0x08)|Command = USER_SET_ERROR_REPORT (0x08)|Command = USER_SET_ERROR_REPORT (0x08)|Command = USER_SET_ERROR_REPORT (0x08)|Command = USER_SET_ERROR_REPORT (0x08)|Command = USER_SET_ERROR_REPORT (0x08)|Command = USER_SET_ERROR_REPORT (0x08)|
|User Set Error Type<br>|User Set Error Type<br>|User Set Error Type<br>|User Set Error Type<br>|User Set Error Type<br>|User Set Error Type<br>|User Set Error Type<br>|User Set Error Type<br>|
|User Modifer Type<br>|User Modifer Type<br>|User Modifer Type<br>|User Modifer Type<br>|User Modifer Type<br>|User Modifer Type<br>|User Modifer Type<br>|User Modifer Type<br>|
|User Modifer Node ID (MSB)<br>|User Modifer Node ID (MSB)<br>|User Modifer Node ID (MSB)<br>|User Modifer Node ID (MSB)<br>|User Modifer Node ID (MSB)<br>|User Modifer Node ID (MSB)<br>|User Modifer Node ID (MSB)<br>|User Modifer Node ID (MSB)<br>|
|User Modifer Node ID (LSB)<br>|User Modifer Node ID (LSB)<br>|User Modifer Node ID (LSB)<br>|User Modifer Node ID (LSB)<br>|User Modifer Node ID (LSB)<br>|User Modifer Node ID (LSB)<br>|User Modifer Node ID (LSB)<br>|User Modifer Node ID (LSB)<br>|
|User Unique Identifer (MSB)<br>|User Unique Identifer (MSB)<br>|User Unique Identifer (MSB)<br>|User Unique Identifer (MSB)<br>|User Unique Identifer (MSB)<br>|User Unique Identifer (MSB)<br>|User Unique Identifer (MSB)<br>|User Unique Identifer (MSB)<br>|
|User Unique Identifer (LSB)|User Unique Identifer (LSB)|User Unique Identifer (LSB)|User Unique Identifer (LSB)|User Unique Identifer (LSB)|User Unique Identifer (LSB)|User Unique Identifer (LSB)|User Unique Identifer (LSB)|
|User Type|User Type|User Type|User Type|User Type|User Type|User Type|User Type|
|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|User Active<br>State|
|Credential Rule|Credential Rule|Credential Rule|Credential Rule|Credential Rule|Credential Rule|Credential Rule|Credential Rule|
|Expiring Timeout Minutes (MSB)|Expiring Timeout Minutes (MSB)|Expiring Timeout Minutes (MSB)|Expiring Timeout Minutes (MSB)|Expiring Timeout Minutes (MSB)|Expiring Timeout Minutes (MSB)|Expiring Timeout Minutes (MSB)|Expiring Timeout Minutes (MSB)|
|Expiring Timeout Minutes (LSB)|Expiring Timeout Minutes (LSB)|Expiring Timeout Minutes (LSB)|Expiring Timeout Minutes (LSB)|Expiring Timeout Minutes (LSB)|Expiring Timeout Minutes (LSB)|Expiring Timeout Minutes (LSB)|Expiring Timeout Minutes (LSB)|
|Reserved|Reserved|Reserved|Reserved|Reserved|User Name Encoding|User Name Encoding|User Name Encoding|
|User Name Length|User Name Length|User Name Length|User Name Length|User Name Length|User Name Length|User Name Length|User Name Length|
|User Name|User Name|User Name|User Name|User Name|User Name|User Name|User Name|


For “User Unique Identifier”, “User Type”, “User Active State”, “Credential Rule”, “Expiring Timeout
Minutes”, “User Name Encoding”, “User Name Length”, and “User Name” descriptions, refer to the
_User_ _Set_ _Command_ .

For “User Modifier Type” and “User Modifier Node ID” descriptions, refer to the _User_ _Report_ _Com-_
_mand_ .


**User** **Set** **Error** **Type** **(8** **bits)**


The User Set Error Type indicates why a node has rejected a _User_ _Set_ _Command_ request.

CC:0083.01.08.11.000 This field MUST comply with Table 2.541.


CC:0083.01.08.11.001



Table 2.541: User Set Error Report::User Error Types










|Value|Name|i<br>Defnition|Report Data|
|---|---|---|---|
|0x00|UserAddRejectedLo-<br>cationOccupied|A user add operation is rejected due to<br>the User Unique Identifer already be-<br>ing occupied. If attempting to add a<br>user where a user at that User Unique<br>Identifer already exists, and the new<br>user data difers, the Add operation<br>MUST be rejected and this command<br>MUST be sent instead. If an Add is<br>rejected, a Modify operation MAY be<br>used instead.|This<br>report<br>MUST<br>contain<br>the<br>data<br>already<br>occupying<br>the<br>User<br>Unique<br>Identifer.|
|0x01|UserModifyRejected-<br>LocationEmpty|A user modify operation is rejected<br>due to the User Unique Identifer lo-<br>cation being empty. If attempting to<br>modify a user where a user at that<br>User Unique Identifer does not ex-<br>ist, the Modify operation MUST be<br>rejected and this command MUST be<br>sent instead. If a Modify is rejected,<br>an Add MAY be used instead.|This<br>report<br>MUST<br>contain<br>the<br>rejected<br>data.|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 549




<!-- PAGE 551 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


CC:0083.01.08.11.002 All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.


CC:0083.01.08.11.003
If a User is specified in this command for an Add or Modify operation for a User Unique Identifier where
that User data is already located at the specified User Unique Identifier, the receiving node MUST
send a _Notification_ _Report_ _Command_ with Notification Type “Access Control” (0x06), Notification
Event “User unchanged” (0x2A), and Event/State parameters of only a _User_ _Notification_ _Report_
_Command_ of the existing data.

CC:0083.01.08.11.004 If no user data is modified, the “User Modifier Type” and “User Modifier Node ID” MUST remain
unchanged.


**2.2.118.12** **User** **Notification** **Report** **Command**


This command returns the User data and is intended to be added to _Notification_ _Report_ _Command_
as “Event/State parameters”.









|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|
|Command = USER_NOTIFICATION_REPORT (0x09)<br>|Command = USER_NOTIFICATION_REPORT (0x09)<br>|Command = USER_NOTIFICATION_REPORT (0x09)<br>|Command = USER_NOTIFICATION_REPORT (0x09)<br>|Command = USER_NOTIFICATION_REPORT (0x09)<br>|Command = USER_NOTIFICATION_REPORT (0x09)<br>|Command = USER_NOTIFICATION_REPORT (0x09)<br>|Command = USER_NOTIFICATION_REPORT (0x09)<br>|
|User Modifer Type<br>|User Modifer Type<br>|User Modifer Type<br>|User Modifer Type<br>|User Modifer Type<br>|User Modifer Type<br>|User Modifer Type<br>|User Modifer Type<br>|
|User Modifer Node ID (MSB)<br>|User Modifer Node ID (MSB)<br>|User Modifer Node ID (MSB)<br>|User Modifer Node ID (MSB)<br>|User Modifer Node ID (MSB)<br>|User Modifer Node ID (MSB)<br>|User Modifer Node ID (MSB)<br>|User Modifer Node ID (MSB)<br>|
|User Modifer Node ID (LSB)<br>|User Modifer Node ID (LSB)<br>|User Modifer Node ID (LSB)<br>|User Modifer Node ID (LSB)<br>|User Modifer Node ID (LSB)<br>|User Modifer Node ID (LSB)<br>|User Modifer Node ID (LSB)<br>|User Modifer Node ID (LSB)<br>|
|User Unique Identifer (MSB)<br>|User Unique Identifer (MSB)<br>|User Unique Identifer (MSB)<br>|User Unique Identifer (MSB)<br>|User Unique Identifer (MSB)<br>|User Unique Identifer (MSB)<br>|User Unique Identifer (MSB)<br>|User Unique Identifer (MSB)<br>|
|User Unique Identifer (LSB)|User Unique Identifer (LSB)|User Unique Identifer (LSB)|User Unique Identifer (LSB)|User Unique Identifer (LSB)|User Unique Identifer (LSB)|User Unique Identifer (LSB)|User Unique Identifer (LSB)|
|User Type|User Type|User Type|User Type|User Type|User Type|User Type|User Type|
|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|User Active<br>State|
|Credential Rule|Credential Rule|Credential Rule|Credential Rule|Credential Rule|Credential Rule|Credential Rule|Credential Rule|
|Expiring Timeout Minutes (MSB)|Expiring Timeout Minutes (MSB)|Expiring Timeout Minutes (MSB)|Expiring Timeout Minutes (MSB)|Expiring Timeout Minutes (MSB)|Expiring Timeout Minutes (MSB)|Expiring Timeout Minutes (MSB)|Expiring Timeout Minutes (MSB)|
|Expiring Timeout Minutes (LSB)|Expiring Timeout Minutes (LSB)|Expiring Timeout Minutes (LSB)|Expiring Timeout Minutes (LSB)|Expiring Timeout Minutes (LSB)|Expiring Timeout Minutes (LSB)|Expiring Timeout Minutes (LSB)|Expiring Timeout Minutes (LSB)|


For “User Unique Identifier”, “User Type”, “User Active State”, “Credential Rule”, and “Expiring
Timeout Minutes” descriptions, refer to the _User_ _Set_ _Command_ .

For “User Modifier Type” and “User Modifier Node ID” descriptions, refer to the _User_ _Report_ _Com-_
_mand_ .


**2.2.118.13** **Credential** **Set** **Command**


This command adds, removes, or modifies Credentials in a node for an existing user.









|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|
|Command = CREDENTIAL_SET (0x0A)<br>|Command = CREDENTIAL_SET (0x0A)<br>|Command = CREDENTIAL_SET (0x0A)<br>|Command = CREDENTIAL_SET (0x0A)<br>|Command = CREDENTIAL_SET (0x0A)<br>|Command = CREDENTIAL_SET (0x0A)<br>|Command = CREDENTIAL_SET (0x0A)<br>|Command = CREDENTIAL_SET (0x0A)<br>|
|User Unique Identifer (MSB)<br>|User Unique Identifer (MSB)<br>|User Unique Identifer (MSB)<br>|User Unique Identifer (MSB)<br>|User Unique Identifer (MSB)<br>|User Unique Identifer (MSB)<br>|User Unique Identifer (MSB)<br>|User Unique Identifer (MSB)<br>|
|User Unique Identifer (LSB)|User Unique Identifer (LSB)|User Unique Identifer (LSB)|User Unique Identifer (LSB)|User Unique Identifer (LSB)|User Unique Identifer (LSB)|User Unique Identifer (LSB)|User Unique Identifer (LSB)|
|Credential Type|Credential Type|Credential Type|Credential Type|Credential Type|Credential Type|Credential Type|Credential Type|
|Credential Slot (MSB)|Credential Slot (MSB)|Credential Slot (MSB)|Credential Slot (MSB)|Credential Slot (MSB)|Credential Slot (MSB)|Credential Slot (MSB)|Credential Slot (MSB)|
|Credential Slot (LSB)|Credential Slot (LSB)|Credential Slot (LSB)|Credential Slot (LSB)|Credential Slot (LSB)|Credential Slot (LSB)|Credential Slot (LSB)|Credential Slot (LSB)|
|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Operation Type|Operation Type|
|Credential Length|Credential Length|Credential Length|Credential Length|Credential Length|Credential Length|Credential Length|Credential Length|
|Credential Data|Credential Data|Credential Data|Credential Data|Credential Data|Credential Data|Credential Data|Credential Data|


**User** **Unique** **Identifier** **(16** **bits)**


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 550




<!-- PAGE 552 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


See _User_ _Set_ _Command_ for this field’s description.


**Credential** **Type** **(8** **bits)**

CC:0083.01.0A.11.000 The type of this specific Credential. This field MUST comply with Table 2.542.


Table 2.542: Credential Type Encoding

|Value|Name|i<br>Defnition|
|---|---|---|
|0x00|None|Reserved for Next Credential Type in Credential Report|
|0x01|PIN Code|A numeric code typed in at the node|
|0x02|Password|Alpha-numeric code typed in at the node|
|0x03|RFID Code|A numeric code entered over a Radio Frequency ID con-<br>nection|
|0x04|BLE|A numeric code entered over a Bluetooth Low energy con-<br>nection|
|0x05|NFC|A numeric code entered over a Near Field Communication<br>connection|
|0x06|UWB|A numeric code entered over an Ultra-Wideband connec-<br>tion|
|0x07|Eye Biometric|Biometric data relating to the eye(s) such as an iris, retina,<br>or scleral vein which is scanned at the node|
|0x08|Face Biometric|Biometric data relating to the face which is scanned at the<br>node<br>|
|0x09|Finger Biometric|Biometric data relating to the fnger(s) such as fnger ge-<br>ometry or a fngerprint which is scanned at the node|
|0x0A|Hand Biometric<br>|Biometric data relating to the hand(s) such as a palm print<br>or hand geometry which is scanned at the node|
|0x0B|Unspecifed Biometric|Biometric data that does not fall into other biometric types<br>specifed in this Credential Type which is scanned at the<br>node|



Biometric examples referenced from [18].


CC:0083.01.0A.11.001 All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.

CC:0083.01.0A.11.002 If a Credential Type is specified in this command as one not advertised as supported in the _Credential_
_Capabilities_ _Report_ _Command_, a receiving node MUST ignore the command.


CC:0083.01.0A.11.020 PIN Codes MUST be transmitted in ASCII format.


CC:0083.01.0A.11.021 Passwords MUST be transmitted in Unicode UTF-16 format, in big endian order.


**Credential** **Slot** **(16** **bits)**


The Credential Slot is a sixteen bit address used to store Credentials.


CC:0083.01.0A.11.003 The range of values MUST be one to Number of Supported Credential Slots for the given Credential
Type, inclusive (see _Credential_ _Capabilities_ _Report_ _Command_ ). Zero is an invalid Credential Slot
unless being using in a Delete operation.

CC:0083.01.0A.11.004 If a Credential Slot is specified in this command as one not advertised as supported in the _Credential_
_Capabilities Report Command_ for that Credential Type, a receiving node MUST ignore the command.

CC:0083.01.0A.11.005 If a Credential Slot of zero is specified in this command for a non-Delete Operation Type, a receiving
node MUST ignore the command.


Credential Slots are unique per Credential Type. For example, Credential Type 2, Slot 1 is distinct
from Credential Type 3, Slot 1.


**Reserved** **(6** **bits)**

CC:0083.01.0A.11.006 This field MUST be set to zero by a sending node and MUST be ignored by a receiving node.


**Operation** **Type** **(2** **bits)**


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 551




<!-- PAGE 553 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


The Operation Type field indicates the event to change Credential data.

CC:0083.01.0A.11.007 This field MUST comply with Table 2.543.


CC:0083.01.0A.11.008

|Value|Table 2.543: Name|Credential Set::Operation Type Definition|
|---|---|---|
|Value|Name|Defnition<br>|
|0x00|Add|A Credential for the given User Unique Identifer of the<br>given Credential Type is added to the given Credential<br>Slot.<br>|
|0x01|Modify|A Credential for the given User Unique Identifer is modi-<br>fed. The felds in this command MUST overwrite existing<br>user data unless the new data is determined to be invalid.|
|0x02|Delete|One or more Credentials are deleted.<br>If the User Unique Identifer, Credential Type, and Cre-<br>dential Slot are non-zero, then that Credential MUST be<br>deleted.<br>The receiving node MUST then send a _Notif-_<br>_cation Report Command_ with Notifcation Type “Access<br>Control” (0x06), Notifcation Event “Credential deleted”<br>(0x2D), and Event/State parameters of only a _Credential_<br>_Notifcation Report Command_ of the deleted data.<br>If the User Unique Identifer and Credential Type are<br>non-zero and Credential Slot is zero, then all Credentials<br>of that Credential Type for that User Unique Identifer<br>MUST be deleted. The receiving node MUST then send a<br>_Notifcation Report Command_ with Notifcation Type “Ac-<br>cess Control” (0x06), Notifcation Event “Multiple creden-<br>tials deleted” (0x26), and Event/State parameters of only<br>the User Unique Identifer, Credential Type, and Creden-<br>tial Slot used in the received command.<br>If the User Unique Identifer is non-zero and Credential<br>Type is zero, then all Credentials of all Credential Types<br>for that User Unique Identifer MUST be deleted. The re-<br>ceiving node MUST then send a_ Notifcation Report Com-_<br>_mand_ with Notifcation Type “Access Control” (0x06), No-<br>tifcation Event “Multiple credentials deleted” (0x26), and<br>Event/State parameters of only the User Unique Identifer,<br>Credential Type, and Credential Slot used in the received<br>command.<br>If the User Unique Identifer is zero, then all Credentials<br>for all Users MUST be deleted. The receiving node MUST<br>then send a _Notifcation Report Command_ with Notif-<br>cation Type “Access Control” (0x06), Notifcation Event<br>“Multiple credentials deleted” (0x26), and Event/State pa-<br>rameters of only the User Unique Identifer, Credential<br>Type, and Credential Slot used in the received command.<br>If the User Unique Identifer and Credential Slot are<br>zero, and Credential Type is non-zero, then everything<br>for that Credential Type MUST be deleted. The receiving<br>node MUST then send a _Notifcation Report Command_<br>with Notifcation Type “Access Control” (0x06), Notif-<br>cation Event “Multiple credentials deleted” (0x26), and<br>Event/State parameters of only the User Unique Identifer,<br>Credential Type, and Credential Slot used in the received<br>command.|



CC:0083.01.0A.11.009 All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.

CC:0083.01.0A.11.010 If all credentials are deleted, a _Notification Report Command_ with Notification Type “Access Control”
(0x06), Notification Event “Multiple credentials deleted” (0x26), and Event/State parameters of only


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 552




<!-- PAGE 554 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


User Unique Modifier, Credential Type, and Credential Slot MUST be sent.

CC:0083.01.0A.11.011 If a credential is added, a _Notification_ _Report_ _Command_ with Notification Type “Access Control”
(0x06), Notification Event “Credential added” (0x2B), and Event/State parameters of only a _Creden-_
_tial_ _Notification_ _Report_ _Command_ of the newly added data MUST be sent.

CC:0083.01.0A.11.012 If a credential is modified, a _Notification_ _Report_ _Command_ with Notification Type “Access Control” (0x06), Notification Event “Credential modified” (0x2C), and Event/State parameters of only a
_Credential_ _Notification_ _Report_ _Command_ of the newly modified data MUST be sent.

CC:0083.01.0A.11.013 If a credential is deleted, a _Notification_ _Report_ _Command_ with Notification Type “Access Control”
(0x06), Notification Event “Credential deleted” (0x2D), and Event/State parameters of only a _Cre-_
_dential_ _Notification_ _Report_ _Command_ of the deleted data MUST be sent.


**Credential** **Length** **(8** **bits)**


Credential Length is the length of the following Credential data, in bytes.


CC:0083.01.0A.11.014 The length of the Credential data MUST be no longer than the Max Length of Credential Data for
the specific Credential Type specified in the _Credential_ _Capabilities_ _Report_ _Command_ .


CC:0083.01.0A.11.015 The length of the Credential data MUST be no shorter than the Min Length of Credential Data for
the specific Credential Type specified in the _Credential_ _Capabilities_ _Report_ _Command_ .


CC:0083.01.0A.13.016 This MAY be zero when deleting Credentials.


**Credential** **Data** **(Variable** **Length)**

The Credential data to set for the Credential being added or modified.


CC:0083.01.0A.11.018 Duplicate credentials within a Credential Type MUST NOT be allowed.

CC:0083.01.0A.13.019 If a credential is used at the node that does not match any existing credential, a _Notification_ _Report_
_Command_ with Notification Type “Access Control” (0x06) and Notification Event “Invalid credential
used to access the node” (0x32) MAY be sent.


**2.2.118.14** **Credential** **Get** **Command**


This command is used to retrieve Credential data for a given User Unique Identifier, type, and slot.


CC:0083.01.0B.11.000 The _Credential_ _Report_ _Command_ MUST be returned in response to this command.


CC:0083.01.0B.11.001 This command MUST NOT be issued via multicast addressing.


CC:0083.01.0B.11.002 A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast Node ID and the Multi Channel Multi-End Point
destination are all considered multicast addressing methods.





|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|
|Command = CREDENTIAL_GET (0x0B)<br>|Command = CREDENTIAL_GET (0x0B)<br>|Command = CREDENTIAL_GET (0x0B)<br>|Command = CREDENTIAL_GET (0x0B)<br>|Command = CREDENTIAL_GET (0x0B)<br>|Command = CREDENTIAL_GET (0x0B)<br>|Command = CREDENTIAL_GET (0x0B)<br>|Command = CREDENTIAL_GET (0x0B)<br>|
|User Unique Identifer (MSB)<br>|User Unique Identifer (MSB)<br>|User Unique Identifer (MSB)<br>|User Unique Identifer (MSB)<br>|User Unique Identifer (MSB)<br>|User Unique Identifer (MSB)<br>|User Unique Identifer (MSB)<br>|User Unique Identifer (MSB)<br>|
|User Unique Identifer (LSB)|User Unique Identifer (LSB)|User Unique Identifer (LSB)|User Unique Identifer (LSB)|User Unique Identifer (LSB)|User Unique Identifer (LSB)|User Unique Identifer (LSB)|User Unique Identifer (LSB)|
|Credential Type|Credential Type|Credential Type|Credential Type|Credential Type|Credential Type|Credential Type|Credential Type|
|Credential Slot (MSB)|Credential Slot (MSB)|Credential Slot (MSB)|Credential Slot (MSB)|Credential Slot (MSB)|Credential Slot (MSB)|Credential Slot (MSB)|Credential Slot (MSB)|
|Credential Slot (LSB)|Credential Slot (LSB)|Credential Slot (LSB)|Credential Slot (LSB)|Credential Slot (LSB)|Credential Slot (LSB)|Credential Slot (LSB)|Credential Slot (LSB)|


For fields’ description, refer to the _Credential_ _Set_ _Command_ .


CC:0083.01.0B.11.003
If the User Unique Identifier, Credential Type, and Credential Slot are all non-zero, then the Credential
associated with that user, type, and slot MUST be returned.


CC:0083.01.0B.11.004 If no Credential exists for that user, type, and slot, a Credential with length zero MUST be returned.


CC:0083.01.0B.11.005


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 553




<!-- PAGE 555 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


If the User Unique Identifier is non-zero and the Credential Type and Credential Slot are both zero,
then the first available Credential for that User Unique Identifier MUST be returned.


CC:0083.01.0B.11.006
Other combinations of zero and non-zero User Unique Identifier, Credential Type, and Credential Slot
are considered invalid and MUST be ignored.


**2.2.118.15** **Credential** **Report** **Command**


This command reports data about a Credential on a node for an existing user.





|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|
|Command = CREDENTIAL_REPORT (0x0C)<br>|Command = CREDENTIAL_REPORT (0x0C)<br>|Command = CREDENTIAL_REPORT (0x0C)<br>|Command = CREDENTIAL_REPORT (0x0C)<br>|Command = CREDENTIAL_REPORT (0x0C)<br>|Command = CREDENTIAL_REPORT (0x0C)<br>|Command = CREDENTIAL_REPORT (0x0C)<br>|Command = CREDENTIAL_REPORT (0x0C)<br>|
|User Unique Identifer (MSB)<br>|User Unique Identifer (MSB)<br>|User Unique Identifer (MSB)<br>|User Unique Identifer (MSB)<br>|User Unique Identifer (MSB)<br>|User Unique Identifer (MSB)<br>|User Unique Identifer (MSB)<br>|User Unique Identifer (MSB)<br>|
|User Unique Identifer (LSB)|User Unique Identifer (LSB)|User Unique Identifer (LSB)|User Unique Identifer (LSB)|User Unique Identifer (LSB)|User Unique Identifer (LSB)|User Unique Identifer (LSB)|User Unique Identifer (LSB)|
|Credential Type|Credential Type|Credential Type|Credential Type|Credential Type|Credential Type|Credential Type|Credential Type|
|Credential Slot (MSB)|Credential Slot (MSB)|Credential Slot (MSB)|Credential Slot (MSB)|Credential Slot (MSB)|Credential Slot (MSB)|Credential Slot (MSB)|Credential Slot (MSB)|
|Credential Slot (LSB)|Credential Slot (LSB)|Credential Slot (LSB)|Credential Slot (LSB)|Credential Slot (LSB)|Credential Slot (LSB)|Credential Slot (LSB)|Credential Slot (LSB)|
|CRB|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|
|Credential Length|Credential Length|Credential Length|Credential Length|Credential Length|Credential Length|Credential Length|Credential Length|
|Credential Data<br>|Credential Data<br>|Credential Data<br>|Credential Data<br>|Credential Data<br>|Credential Data<br>|Credential Data<br>|Credential Data<br>|
|Credential Modifer Type<br>|Credential Modifer Type<br>|Credential Modifer Type<br>|Credential Modifer Type<br>|Credential Modifer Type<br>|Credential Modifer Type<br>|Credential Modifer Type<br>|Credential Modifer Type<br>|
|Credential Modifer Node ID (MSB)<br>|Credential Modifer Node ID (MSB)<br>|Credential Modifer Node ID (MSB)<br>|Credential Modifer Node ID (MSB)<br>|Credential Modifer Node ID (MSB)<br>|Credential Modifer Node ID (MSB)<br>|Credential Modifer Node ID (MSB)<br>|Credential Modifer Node ID (MSB)<br>|
|Credential Modifer Node ID (LSB)|Credential Modifer Node ID (LSB)|Credential Modifer Node ID (LSB)|Credential Modifer Node ID (LSB)|Credential Modifer Node ID (LSB)|Credential Modifer Node ID (LSB)|Credential Modifer Node ID (LSB)|Credential Modifer Node ID (LSB)|
|Next Credential Type|Next Credential Type|Next Credential Type|Next Credential Type|Next Credential Type|Next Credential Type|Next Credential Type|Next Credential Type|
|Next Credential Slot (MSB)|Next Credential Slot (MSB)|Next Credential Slot (MSB)|Next Credential Slot (MSB)|Next Credential Slot (MSB)|Next Credential Slot (MSB)|Next Credential Slot (MSB)|Next Credential Slot (MSB)|
|Next Credential Slot (LSB)|Next Credential Slot (LSB)|Next Credential Slot (LSB)|Next Credential Slot (LSB)|Next Credential Slot (LSB)|Next Credential Slot (LSB)|Next Credential Slot (LSB)|Next Credential Slot (LSB)|


For “User Unique Identifier”, “Credential Type”, and “Credential Slot” descriptions, refer to the
_Credential_ _Set_ _Command_ .


**Credential** **Read** **Back** **(CRB)** **(1** **bit)**

This field is set to one if Credential Length and Credential Data contain the actual Credential and
zero if the Credential cannot be read back from the device.


CC:0083.01.0C.13.000 If the Credential cannot be read back, then the node MAY report a hash sum of the Credential or
report empty data with Credential Length set to zero.

CC:0083.01.0C.11.001 The Credential Read Back field MUST always be set to the same value within a Credential Type.


CC:0083.01.0C.12.002 Non-Biometric Credential Types SHOULD be reported by the node.


This hash sum can be used by the controlling node to track Credential changes without revealing the
actual Credential Data. It is up to the supporting node to choose the hashing algorithm.


CC:0083.01.0C.12.003 The hashing algorithm SHOULD allow easy detection of Credential updates by either complying with
modern hash-function requirements or being a sequence number.


CC:0083.01.0C.12.004 The hashing algorithm SHOULD be one way.


**Reserved** **(7** **bits)**

CC:0083.01.0C.11.005 This field MUST be set to zero by a sending node and MUST be ignored by a receiving node.


**Credential** **Length** **(8** **bits)**

See _Credential_ _Set_ _Command_ for this field’s description.


CC:0083.01.0C.13.006 In addition, this length MAY refer to the length of a hash of the Credential if Credential Read Back

is set to zero.


**Credential** **Data** **(Variable** **Length)**


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 554




<!-- PAGE 556 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


See _Credential_ _Set_ _Command_ for this field’s description.


CC:0083.01.0C.13.007 In addition, this data MAY be a hash of the Credential if Credential Read Back is set to zero.

**Credential** **Modifier** **Type** **(8** **bits)**

Refer to User Modifier Type in _User_ _Report_ _Command_ for this field’s description.

**Credential** **Modifier** **Node** **ID** **(16** **bits)**

Refer to User Modifier Node ID in _User_ _Report_ _Command_ for this field’s description.


**Next** **Credential** **Type** **(8** **bits)**


The Next Credential Type is used in tandem with Next Credential Slot to iterate through all Credentials for a given User. It indicates the Credential Type for the next Credential to request when
iterating.

CC:0083.01.0C.11.010 This field MUST comply with the values listed in Table 2.542.


CC:0083.01.0C.11.008 This MUST be a non-zero value if there is at least one more Credential for this User and MUST be

set to 0x00 if there are no more Credentials.


**Next** **Credential** **Slot** **(16** **bits)**


The Next Credential Slot is used in tandem with Next Credential Type to iterate through all Credentials for a given User. It indicates the Credential Slot for the next Credential to request when
iterating. The value can range from one to the maximum number of Credentials supported by this
type.


CC:0083.01.0C.11.009 This MUST be a non-zero value if there is at least one more Credential for this User and MUST be

zero if there are no more Credentials.


**2.2.118.16** **Credential** **Set** **Error** **Report** **Command**


This command returns an error message when setting Credential data has failed. This helps provide
more information to the controller but is not meant to provide errors for bad data being sent, such as
an unsupported Credential Type.


|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|
|Command = CREDENTIAL_SET_ERROR_REPORT (0x0D)|Command = CREDENTIAL_SET_ERROR_REPORT (0x0D)|Command = CREDENTIAL_SET_ERROR_REPORT (0x0D)|Command = CREDENTIAL_SET_ERROR_REPORT (0x0D)|Command = CREDENTIAL_SET_ERROR_REPORT (0x0D)|Command = CREDENTIAL_SET_ERROR_REPORT (0x0D)|Command = CREDENTIAL_SET_ERROR_REPORT (0x0D)|Command = CREDENTIAL_SET_ERROR_REPORT (0x0D)|
|Credential Set Error Type<br>|Credential Set Error Type<br>|Credential Set Error Type<br>|Credential Set Error Type<br>|Credential Set Error Type<br>|Credential Set Error Type<br>|Credential Set Error Type<br>|Credential Set Error Type<br>|
|User Unique Identifer (MSB)<br>|User Unique Identifer (MSB)<br>|User Unique Identifer (MSB)<br>|User Unique Identifer (MSB)<br>|User Unique Identifer (MSB)<br>|User Unique Identifer (MSB)<br>|User Unique Identifer (MSB)<br>|User Unique Identifer (MSB)<br>|
|User Unique Identifer (LSB)|User Unique Identifer (LSB)|User Unique Identifer (LSB)|User Unique Identifer (LSB)|User Unique Identifer (LSB)|User Unique Identifer (LSB)|User Unique Identifer (LSB)|User Unique Identifer (LSB)|
|Credential Type|Credential Type|Credential Type|Credential Type|Credential Type|Credential Type|Credential Type|Credential Type|
|Credential Slot (MSB)|Credential Slot (MSB)|Credential Slot (MSB)|Credential Slot (MSB)|Credential Slot (MSB)|Credential Slot (MSB)|Credential Slot (MSB)|Credential Slot (MSB)|
|Credential Slot (LSB)|Credential Slot (LSB)|Credential Slot (LSB)|Credential Slot (LSB)|Credential Slot (LSB)|Credential Slot (LSB)|Credential Slot (LSB)|Credential Slot (LSB)|
|CRB|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|
|Credential Length|Credential Length|Credential Length|Credential Length|Credential Length|Credential Length|Credential Length|Credential Length|
|Credential Data<br>|Credential Data<br>|Credential Data<br>|Credential Data<br>|Credential Data<br>|Credential Data<br>|Credential Data<br>|Credential Data<br>|
|Credential Modifer Type<br>|Credential Modifer Type<br>|Credential Modifer Type<br>|Credential Modifer Type<br>|Credential Modifer Type<br>|Credential Modifer Type<br>|Credential Modifer Type<br>|Credential Modifer Type<br>|
|Credential Modifer Node ID (MSB)<br>|Credential Modifer Node ID (MSB)<br>|Credential Modifer Node ID (MSB)<br>|Credential Modifer Node ID (MSB)<br>|Credential Modifer Node ID (MSB)<br>|Credential Modifer Node ID (MSB)<br>|Credential Modifer Node ID (MSB)<br>|Credential Modifer Node ID (MSB)<br>|
|Credential Modifer Node ID (LSB)|Credential Modifer Node ID (LSB)|Credential Modifer Node ID (LSB)|Credential Modifer Node ID (LSB)|Credential Modifer Node ID (LSB)|Credential Modifer Node ID (LSB)|Credential Modifer Node ID (LSB)|Credential Modifer Node ID (LSB)|



CC:0083.01.0D.11.000



For “User Unique Identifier”, “Credential Type”, and “Credential Slot” descriptions, refer to the
_Credential_ _Set_ _Command_ .

For “CRB”, “Credential Length”, “Credential Data”, “Credential Modifier Type”, and “Credential
Modifier Node ID” descriptions, refer to the _Credential_ _Report_ _Command_ .


**Credential** **Set** **Error** **Type** **(8** **bits)**


The Credential Set Error Type indicates why a node has rejected a _Credential_ _Set_ _Command_ request.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 555




<!-- PAGE 557 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


This field MUST comply with Table 2.544.



CC:0083.01.0D.11.001



Table 2.544: Credential Set Error Report::Credential Error Types


















|Value|Name|i<br>Defnition|Report Data|
|---|---|---|---|
|0x00|CredentialAddReject-<br>edLocationOccupied|If attempting to add a credential<br>where a credential of that Credential<br>Type at that Credential Slot already<br>exists, and the new credential data<br>difers, the Add operation MUST be<br>rejected and this command MUST be<br>sent instead.<br>If an Add is rejected,<br>a Modify operation MAY be used in-<br>stead.|The<br>report<br>MUST<br>contain the data al-<br>ready<br>occupying<br>the<br>Credential Type and<br>Credential Slot.|
|0x01|CredentialModifyRe-<br>jectedLocationEmpty|If attempting to modify a credential<br>where a credential of that Credential<br>Type at that Credential Slot does not<br>exist, the Modify operation MUST be<br>rejected and this command MUST be<br>sent instead. If a Modify is rejected,<br>an Add operation MAY be used in-<br>stead.<br>|This<br>report<br>MUST<br>contain<br>the<br>rejected<br>data.|
|0x02|DuplicateCredential|If a duplicate credential is specifed in<br>a _Credential Set Command_ for a Cre-<br>dential Type where that duplicate is<br>located at a diferent Credential Slot<br>or attached to a diferent User Unique<br>Identifer, the receiving node MUST<br>reject the command and instead send<br>this command.|This<br>report<br>MUST<br>contain<br>the<br>existing<br>credential data.<br>For<br>example, if PIN Code<br>1234 is at Credential<br>Slot<br>0x0002<br>but<br>a<br>Credential<br>Set<br>con-<br>tains Credential Slot<br>0x0003,<br>this<br>com-<br>mand containing the<br>Credential data with<br>Credential Slot 0x0002<br>MUST be sent.<br>Or,<br>for example,<br>if PIN<br>Code 1234 is at Cre-<br>dential Slot 0x0002 for<br>User Unique Identifer<br>0x0003<br>but<br>a<br>Cre-<br>dential<br>Set<br>contains<br>User Unique Identifer<br>0x0004 and Credential<br>Slot 0x0002, this com-<br>mand containing the<br>Credential data with<br>User Unique Identifer<br>0x0003 and Credential<br>Slot 0x0002 MUST be<br>sent.|
|0x03|ManufacturerSecuri-<br>tyRules|If a credential is rejected by the node<br>due to not following manufacturer se-<br>curity rules, such as a node not al-<br>lowing a PIN Code of only repeating<br>digits, this command MUST be sent.|This<br>report<br>MUST<br>contain<br>the<br>rejected<br>data.|



CC:0083.01.0D.11.002 All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 556




<!-- PAGE 558 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


ignored by a receiving node.

CC:0083.01.0D.11.003 If a credential is specified in this command for an Add or Modify operation for a User Unique Identifier, Credential Type, and Credential Slot where that credential is already located at the specified
Credential Slot for the specified User Unique Identifier and Credential Type, the receiving node MUST
send a _Notification_ _Report_ _Command_ with Notification Type “Access Control” (0x06), Notification
Event “Credential unchanged” (0x2E), and Event/State parameters of only a _Credential_ _Notification_
_Report_ _Command_ of the existing data.

CC:0083.01.0D.11.004 If no credential data is modified, the “Credential Modifier Type” and “Credential Modifier Node ID”
MUST remain unchanged.


**2.2.118.17** **Credential** **Notification** **Report** **Command**


This command reports data about a Credential on a node for an existing user.





|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|
|Command = CREDENTIAL_NOTIFICATION_REPORT (0x0E)<br>|Command = CREDENTIAL_NOTIFICATION_REPORT (0x0E)<br>|Command = CREDENTIAL_NOTIFICATION_REPORT (0x0E)<br>|Command = CREDENTIAL_NOTIFICATION_REPORT (0x0E)<br>|Command = CREDENTIAL_NOTIFICATION_REPORT (0x0E)<br>|Command = CREDENTIAL_NOTIFICATION_REPORT (0x0E)<br>|Command = CREDENTIAL_NOTIFICATION_REPORT (0x0E)<br>|Command = CREDENTIAL_NOTIFICATION_REPORT (0x0E)<br>|
|User Unique Identifer (MSB)<br>|User Unique Identifer (MSB)<br>|User Unique Identifer (MSB)<br>|User Unique Identifer (MSB)<br>|User Unique Identifer (MSB)<br>|User Unique Identifer (MSB)<br>|User Unique Identifer (MSB)<br>|User Unique Identifer (MSB)<br>|
|User Unique Identifer (LSB)|User Unique Identifer (LSB)|User Unique Identifer (LSB)|User Unique Identifer (LSB)|User Unique Identifer (LSB)|User Unique Identifer (LSB)|User Unique Identifer (LSB)|User Unique Identifer (LSB)|
|Credential Type|Credential Type|Credential Type|Credential Type|Credential Type|Credential Type|Credential Type|Credential Type|
|Credential Slot (MSB)|Credential Slot (MSB)|Credential Slot (MSB)|Credential Slot (MSB)|Credential Slot (MSB)|Credential Slot (MSB)|Credential Slot (MSB)|Credential Slot (MSB)|
|Credential Slot (LSB)|Credential Slot (LSB)|Credential Slot (LSB)|Credential Slot (LSB)|Credential Slot (LSB)|Credential Slot (LSB)|Credential Slot (LSB)|Credential Slot (LSB)|
|CRB|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|
|Credential Length|Credential Length|Credential Length|Credential Length|Credential Length|Credential Length|Credential Length|Credential Length|
|Credential Data<br>|Credential Data<br>|Credential Data<br>|Credential Data<br>|Credential Data<br>|Credential Data<br>|Credential Data<br>|Credential Data<br>|
|Credential Modifer Type<br>|Credential Modifer Type<br>|Credential Modifer Type<br>|Credential Modifer Type<br>|Credential Modifer Type<br>|Credential Modifer Type<br>|Credential Modifer Type<br>|Credential Modifer Type<br>|
|Credential Modifer Node ID (MSB)<br>|Credential Modifer Node ID (MSB)<br>|Credential Modifer Node ID (MSB)<br>|Credential Modifer Node ID (MSB)<br>|Credential Modifer Node ID (MSB)<br>|Credential Modifer Node ID (MSB)<br>|Credential Modifer Node ID (MSB)<br>|Credential Modifer Node ID (MSB)<br>|
|Credential Modifer Node ID (LSB)|Credential Modifer Node ID (LSB)|Credential Modifer Node ID (LSB)|Credential Modifer Node ID (LSB)|Credential Modifer Node ID (LSB)|Credential Modifer Node ID (LSB)|Credential Modifer Node ID (LSB)|Credential Modifer Node ID (LSB)|


For “User Unique Identifier”, “Credential Type”, and “Credential Slot” descriptions, refer to the
_Credential_ _Set_ _Command_ .

For “CRB”, “Credential Length”, “Credential Data”, “Credential Modifier Type”, and “Credential
Modifier Node ID” descriptions, refer to the _Credential_ _Report_ _Command_ .


**2.2.118.18** **Credential** **Learn** **Start** **Command**


This command initiates the local credential learn process on the supporting node.


CC:0083.01.0F.11.000 The _Credential_ _Learn_ _Status_ _Report_ _Command_ MUST be returned at the end of the learn process
(successful, unsuccessful, or canceled).


CC:0083.01.0F.11.001 If the learn process is successful, the _Credential_ _Report_ _Command_ MUST be returned at the end of
the learn process.


CC:0083.01.0F.11.002 If a credential is rejected as invalid during the learn process, the same _Credential_ _Set_ _Error_ _Report_
_Command_ that would be sent if the node received a _Credential_ _Set_ _Command_ with that credential

MUST be sent. For example, if the credential is a duplicate and rejected for this reason, a _Credential_
_Set_ _Error_ _Report_ _Command_ with a Credential Set Error Type of DuplicateCredential (0x02) will be

sent.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 557




<!-- PAGE 559 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024





|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|
|Command = CREDENTIAL_LEARN_START (0x0F)<br>|Command = CREDENTIAL_LEARN_START (0x0F)<br>|Command = CREDENTIAL_LEARN_START (0x0F)<br>|Command = CREDENTIAL_LEARN_START (0x0F)<br>|Command = CREDENTIAL_LEARN_START (0x0F)<br>|Command = CREDENTIAL_LEARN_START (0x0F)<br>|Command = CREDENTIAL_LEARN_START (0x0F)<br>|Command = CREDENTIAL_LEARN_START (0x0F)<br>|
|User Unique Identifer (MSB)<br>|User Unique Identifer (MSB)<br>|User Unique Identifer (MSB)<br>|User Unique Identifer (MSB)<br>|User Unique Identifer (MSB)<br>|User Unique Identifer (MSB)<br>|User Unique Identifer (MSB)<br>|User Unique Identifer (MSB)<br>|
|User Unique Identifer (LSB)|User Unique Identifer (LSB)|User Unique Identifer (LSB)|User Unique Identifer (LSB)|User Unique Identifer (LSB)|User Unique Identifer (LSB)|User Unique Identifer (LSB)|User Unique Identifer (LSB)|
|Credential Type|Credential Type|Credential Type|Credential Type|Credential Type|Credential Type|Credential Type|Credential Type|
|Credential Slot (MSB)|Credential Slot (MSB)|Credential Slot (MSB)|Credential Slot (MSB)|Credential Slot (MSB)|Credential Slot (MSB)|Credential Slot (MSB)|Credential Slot (MSB)|
|Credential Slot (LSB)|Credential Slot (LSB)|Credential Slot (LSB)|Credential Slot (LSB)|Credential Slot (LSB)|Credential Slot (LSB)|Credential Slot (LSB)|Credential Slot (LSB)|
|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Operation Type|Operation Type|
|Credential Learn Timeout|Credential Learn Timeout|Credential Learn Timeout|Credential Learn Timeout|Credential Learn Timeout|Credential Learn Timeout|Credential Learn Timeout|Credential Learn Timeout|


For “User Unique Identifier”, “Credential Type”, and “Credential Slot” descriptions, refer to the
_Credential_ _Set_ _Command_ .‘.

CC:0083.01.0F.11.003 If a Credential Type is specified in this command as one not advertised as supported in the _Credential_
_Capabilities_ _Report_ _Command_, a receiving node MUST ignore the command.

CC:0083.01.0F.11.004 If a Credential Type is specified in this command as one not advertised as having Credential Learn
Support in the _Credential Capabilities Report Command_, a receiving node MUST ignore the command.

CC:0083.01.0F.11.005 If a User Unique Identifier is specified in this command as one not advertised as supported in the _User_
_Capabilities_ _Report_ _Command_, a receiving node MUST ignore the command.

CC:0083.01.0F.11.006 If a Credential Slot for the Credential Type is specified in this command as one not advertised
as supported in the _Credential_ _Capabilities_ _Report_ _Command_, a receiving node MUST ignore the
command.


**Reserved** **(6** **bits)**

CC:0083.01.0F.11.007 This field MUST be set to zero by a sending node and MUST be ignored by a receiving node.


**Operation** **Type** **(2** **bits)**

The Operation Type field indicates the event to change Credential data.

CC:0083.01.0F.11.008 This field MUST comply with Table 2.545.


CC:0083.01.0F.11.009

Table 2.545: Credential Learn Start::Operation Type

|Value|Name|i<br>Defnition|
|---|---|---|
|0x00|Credential Learn Add|A Credential for the given User Unique Identifer of the<br>given Credential Type is added to the given Credential<br>Slot. If a Credential at this index already exists, this op-<br>eration MUST be rejected and a Credential Learn Modify<br>operation MAY be used instead.<br>|
|0x01|Credential Learn Modify|A Credential for the given User Unique Identifer of the<br>given Credential Type is modifed for the given Credential<br>Slot. If a Credential at this index does not already exist,<br>this operation MUST be rejected and a Credential Learn<br>Add operation MAY be used instead.|



CC:0083.01.0F.11.010 All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.


**Credential** **Learn** **Timeout** **(8** **bits)**


Timeout for each credential learn step on the node, in seconds.

CC:0083.01.0F.13.011 The node MAY choose to return a timeout failure earlier than the specified timeout value.


CC:0083.01.0F.11.012 The node MUST NOT continue the learn process after the provided timeout has elapsed.


If no credential was learned and timeout (either provided or less than provided) was reached:


CC:0083.01.0F.11.013 - The node MUST stop the learn process.


CC:0083.01.0F.12.014


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 558




<!-- PAGE 560 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


      The node SHOULD advertise the user with audio-visual effect that the learn process has ended.


CC:0083.01.0F.11.015 - The node MUST report back to the initiating node the _Credential Learn Status Report Command_
command with a timeout status.


This command is from the GET commands family and a successful Supervision Report does not
necessarily indicate learn status.


**2.2.118.19** **Credential** **Learn** **Cancel** **Command**


This command cancels the local credential learn process on the supporting node.


CC:0083.01.10.11.000 The _Credential_ _Learn_ _Status_ _Report_ _Command_ MUST be returned in response to this command with
a Credential Learn Status of “Ended Not Due to Timeout”.


CC:0083.01.10.11.001 The learn process MUST end in response to this command.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|
|Command = CREDENTIAL_LEARN_CANCEL (0x10)|Command = CREDENTIAL_LEARN_CANCEL (0x10)|Command = CREDENTIAL_LEARN_CANCEL (0x10)|Command = CREDENTIAL_LEARN_CANCEL (0x10)|Command = CREDENTIAL_LEARN_CANCEL (0x10)|Command = CREDENTIAL_LEARN_CANCEL (0x10)|Command = CREDENTIAL_LEARN_CANCEL (0x10)|Command = CREDENTIAL_LEARN_CANCEL (0x10)|



**2.2.118.20** **Credential** **Learn** **Status** **Report** **Command**


This command reports data about a Credential Learn on a node for an existing user.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|
|Command = CREDENTIAL_LEARN_REPORT (0x11)|Command = CREDENTIAL_LEARN_REPORT (0x11)|Command = CREDENTIAL_LEARN_REPORT (0x11)|Command = CREDENTIAL_LEARN_REPORT (0x11)|Command = CREDENTIAL_LEARN_REPORT (0x11)|Command = CREDENTIAL_LEARN_REPORT (0x11)|Command = CREDENTIAL_LEARN_REPORT (0x11)|Command = CREDENTIAL_LEARN_REPORT (0x11)|
|Credential Learn Status<br>|Credential Learn Status<br>|Credential Learn Status<br>|Credential Learn Status<br>|Credential Learn Status<br>|Credential Learn Status<br>|Credential Learn Status<br>|Credential Learn Status<br>|
|User Unique Identifer (MSB)<br>|User Unique Identifer (MSB)<br>|User Unique Identifer (MSB)<br>|User Unique Identifer (MSB)<br>|User Unique Identifer (MSB)<br>|User Unique Identifer (MSB)<br>|User Unique Identifer (MSB)<br>|User Unique Identifer (MSB)<br>|
|User Unique Identifer (LSB)|User Unique Identifer (LSB)|User Unique Identifer (LSB)|User Unique Identifer (LSB)|User Unique Identifer (LSB)|User Unique Identifer (LSB)|User Unique Identifer (LSB)|User Unique Identifer (LSB)|
|Credential Type|Credential Type|Credential Type|Credential Type|Credential Type|Credential Type|Credential Type|Credential Type|
|Credential Slot (MSB)|Credential Slot (MSB)|Credential Slot (MSB)|Credential Slot (MSB)|Credential Slot (MSB)|Credential Slot (MSB)|Credential Slot (MSB)|Credential Slot (MSB)|
|Credential Slot (LSB)|Credential Slot (LSB)|Credential Slot (LSB)|Credential Slot (LSB)|Credential Slot (LSB)|Credential Slot (LSB)|Credential Slot (LSB)|Credential Slot (LSB)|
|Credential Learn Steps Remaining|Credential Learn Steps Remaining|Credential Learn Steps Remaining|Credential Learn Steps Remaining|Credential Learn Steps Remaining|Credential Learn Steps Remaining|Credential Learn Steps Remaining|Credential Learn Steps Remaining|



For “User Unique Identifier”, “Credential Type”, and “Credential Slot” descriptions, refer to the
_Credential_ _Set_ _Command_


CC:0083.01.11.11.004 This command MUST be sent for each step of the Credential Learn process and on completion of the
credential learn.


**Credential** **Learn** **Status** **(8** **bits)**

This field indicates the result of the credential learn process.

CC:0083.01.11.11.000 This field MUST comply with Table 2.546.


CC:0083.01.11.11.001


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 559




<!-- PAGE 561 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024



Table 2.546: Credential Learn Report::Credential Learn Status








|Value|Name|i<br>Defnition|
|---|---|---|
|0x00|Started|Credential learn step has started.|
|0x01|Success|A Credential was learned and stored in the corresponding<br>slot.|
|0x02|Already in Progress|The node is already in the learning process. The current<br>step of the learn process MUST continue until the original<br>timeout (provided or less than provided) expires.|
|0x03|Ended Not Due to Timeout|The learn process has ended before the timeout (provided<br>or less than provided) expired. If this status is returned,<br>the learn process MUST end. No credential was learned,<br>and the slot was left untouched.<br>For example, a node<br>could decide to stop the learn process after determining<br>the frst credential attempt is invalid, or it could decide to<br>allow additional attempts as part of the same _Credential_<br>_Learn Start Command_. This status MUST be returned in<br>response to the _Credential Learn Cancel Command_.|
|0x04|Timeout|A Credential Learn process timed out. No credential was<br>learned, and the slot was left untouched.|
|0x05|Credential<br>Learn<br>Step<br>Retry|One step of the credential learn process was not completed<br>correctly and must be retried.|
|0xFE|Invalid<br>Credential<br>Learn<br>Add Operation Type|The requested add operation type is invalid.<br>If a Cre-<br>dential Learn Add is requested when a credential already<br>exists at the specifed slot, this status MUST be returned.<br>If this status is returned, the learn process MUST NOT<br>be entered. No credential was learned, and the slot was<br>left untouched.|
|0xFF|Invalid<br>Credential<br>Learn<br>Modify Operation Type|The requested modify operation type is invalid. If a Cre-<br>dential Learn Modify is requested when no credential ex-<br>ists at the specifed slot, this status MUST be returned. If<br>this status is returned, the learn process MUST NOT be<br>entered. No credential was learned, and the slot was left<br>untouched.|



CC:0083.01.11.11.002 All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.


**Credential** **Learn** **Steps** **Remaining** **(8** **bits)**


CC:0083.01.11.11.003
This field indicates the number of remaining steps in the credential learn process for the learn process
to be completed. This field MUST NOT be 0 if Credential Learn Status is Started, Already in
Progress, or Credential Learn Step Retry. This field MUST be 0 for all other defined Credential Learn
Status values. For the first step in a flow where the Credential Learn Status is Started, this value
MUST be the total number of steps required to learn the credential.


**2.2.118.21** **User** **Unique** **Identifier** **Credential** **Association** **Set** **Command**


This command is used to associate an existing credential with an updated user, in place of the user it
is currently linked to.


For example, a biometric credential might be added directly to a lock using a lock’s local interface.
Those limited local interfaces can make it challenging to associate the newly added biometric credential
with an already existing user, and as a result the lock may create a new user entry for the credential.
That user may later want to use an interface on their controller to move that biometric credential
over to a previously existing user (that may have been programmed through the controller, and have
existing credentials like an RFID card and a PIN Code). They can use this command to accomplish


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 560




<!-- PAGE 562 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


that goal. At the end of this process, the credential will no longer be associated with its starting user.

CC:0083.01.12.11.000 A node receiving this command MUST respond by sending a _User_ _Unique_ _Identifier_ _Credential_ _Asso-_
_ciation_ _Report_ _Command_ .


CC:0083.01.12.11.001 This command MUST NOT be issued via multicast addressing.


CC:0083.01.12.11.002 A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast Node ID and the Multi Channel Multi-End Point
destination are all considered multicast addressing methods.





CC:0083.01.12.11.003

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|
|Command = USER_CREDENTIAL_ASSOCIATION_SET (0x12)<br>|Command = USER_CREDENTIAL_ASSOCIATION_SET (0x12)<br>|Command = USER_CREDENTIAL_ASSOCIATION_SET (0x12)<br>|Command = USER_CREDENTIAL_ASSOCIATION_SET (0x12)<br>|Command = USER_CREDENTIAL_ASSOCIATION_SET (0x12)<br>|Command = USER_CREDENTIAL_ASSOCIATION_SET (0x12)<br>|Command = USER_CREDENTIAL_ASSOCIATION_SET (0x12)<br>|Command = USER_CREDENTIAL_ASSOCIATION_SET (0x12)<br>|
|Source User Unique Identifer (MSB)<br>|Source User Unique Identifer (MSB)<br>|Source User Unique Identifer (MSB)<br>|Source User Unique Identifer (MSB)<br>|Source User Unique Identifer (MSB)<br>|Source User Unique Identifer (MSB)<br>|Source User Unique Identifer (MSB)<br>|Source User Unique Identifer (MSB)<br>|
|Source User Unique Identifer (LSB)|Source User Unique Identifer (LSB)|Source User Unique Identifer (LSB)|Source User Unique Identifer (LSB)|Source User Unique Identifer (LSB)|Source User Unique Identifer (LSB)|Source User Unique Identifer (LSB)|Source User Unique Identifer (LSB)|
|Source Credential Type|Source Credential Type|Source Credential Type|Source Credential Type|Source Credential Type|Source Credential Type|Source Credential Type|Source Credential Type|
|Source Credential Slot (MSB)|Source Credential Slot (MSB)|Source Credential Slot (MSB)|Source Credential Slot (MSB)|Source Credential Slot (MSB)|Source Credential Slot (MSB)|Source Credential Slot (MSB)|Source Credential Slot (MSB)|
|Source Credential Slot (LSB)<br>|Source Credential Slot (LSB)<br>|Source Credential Slot (LSB)<br>|Source Credential Slot (LSB)<br>|Source Credential Slot (LSB)<br>|Source Credential Slot (LSB)<br>|Source Credential Slot (LSB)<br>|Source Credential Slot (LSB)<br>|
|Destination User Unique Identifer (MSB)<br>|Destination User Unique Identifer (MSB)<br>|Destination User Unique Identifer (MSB)<br>|Destination User Unique Identifer (MSB)<br>|Destination User Unique Identifer (MSB)<br>|Destination User Unique Identifer (MSB)<br>|Destination User Unique Identifer (MSB)<br>|Destination User Unique Identifer (MSB)<br>|
|Destination User Unique Identifer (LSB)|Destination User Unique Identifer (LSB)|Destination User Unique Identifer (LSB)|Destination User Unique Identifer (LSB)|Destination User Unique Identifer (LSB)|Destination User Unique Identifer (LSB)|Destination User Unique Identifer (LSB)|Destination User Unique Identifer (LSB)|
|Destination Credential Slot (MSB)|Destination Credential Slot (MSB)|Destination Credential Slot (MSB)|Destination Credential Slot (MSB)|Destination Credential Slot (MSB)|Destination Credential Slot (MSB)|Destination Credential Slot (MSB)|Destination Credential Slot (MSB)|
|Destination Credential Slot (LSB)|Destination Credential Slot (LSB)|Destination Credential Slot (LSB)|Destination Credential Slot (LSB)|Destination Credential Slot (LSB)|Destination Credential Slot (LSB)|Destination Credential Slot (LSB)|Destination Credential Slot (LSB)|

The Source User Unique Identifier and the Destination User Unique Identifier MUST both be non-zero,
and MUST both reference existing User Unique Identifiers.


CC:0083.01.12.11.004 The Source Credential Type MUST be one supported by the receiving device.


CC:0083.01.12.11.005 The Source Credential Slot MUST have an existing credential in it, and the Destination Credential
Slot MUST NOT have an existing credential in it.

**Source** **User** **Unique** **Identifier** **(16** **bits)**

The Source User Unique Identifier is used to identify the original User Unique Identifier of the credential that will be modified.


**Source** **Credential** **Type** **(8** **bits)**

This field advertises the Credential Type of the Credential that will be associated with a different
User Unique Identifier.

CC:0083.01.12.11.006 This field MUST comply with values listed in Table 2.542.


**Source** **Credential** **Slot** **(16** **bits)**

This field advertises the Credential Slot of the Credential that will be associated with a different User
Unique Identifier.

**Destination** **User** **Unique** **Identifier** **(16** **bits)**

The Destination User Unique Identifier is used to identify the User Unique Identifier that will be
linked to the credential after the operation of this command.


CC:0083.01.12.11.007
If the Destination User Unique Identifier does not reference an already existing User Unique Identifier,
then the node receiving this command MUST report back to the initiating node with a failure status
and MUST NOT change the User or Credential data in response to this command.


**Destination** **Credential** **Slot** **(16** **bits)**


The Destination Credential Slot is used to identify the Credential Slot where the Credential will be
stored after completing the operation of this command.


CC:0083.01.12.11.008 If the Destination Credential Slot is not supported by the receiving node, or the Destination Credential
Slot is already occupied by another preexisting credential, then the node receiving this command
MUST report back to the initiating node with a failure status and MUST NOT change the User or
Credential data in response to this command.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 561




<!-- PAGE 563 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.118.22** **User** **Unique** **Identifier** **Credential** **Association** **Report** **Command**


This command is used to make other nodes aware of the action taken in response to the _User_ _Unique_
_Identifier_ _Credential_ _Association_ _Set_ _Command_ .





|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|
|Command = USER_CREDENTIAL_ASSOCIATION_REPORT (0x13)<br>|Command = USER_CREDENTIAL_ASSOCIATION_REPORT (0x13)<br>|Command = USER_CREDENTIAL_ASSOCIATION_REPORT (0x13)<br>|Command = USER_CREDENTIAL_ASSOCIATION_REPORT (0x13)<br>|Command = USER_CREDENTIAL_ASSOCIATION_REPORT (0x13)<br>|Command = USER_CREDENTIAL_ASSOCIATION_REPORT (0x13)<br>|Command = USER_CREDENTIAL_ASSOCIATION_REPORT (0x13)<br>|Command = USER_CREDENTIAL_ASSOCIATION_REPORT (0x13)<br>|
|Source User Unique Identifer (MSB)<br>|Source User Unique Identifer (MSB)<br>|Source User Unique Identifer (MSB)<br>|Source User Unique Identifer (MSB)<br>|Source User Unique Identifer (MSB)<br>|Source User Unique Identifer (MSB)<br>|Source User Unique Identifer (MSB)<br>|Source User Unique Identifer (MSB)<br>|
|Source User Unique Identifer (LSB)|Source User Unique Identifer (LSB)|Source User Unique Identifer (LSB)|Source User Unique Identifer (LSB)|Source User Unique Identifer (LSB)|Source User Unique Identifer (LSB)|Source User Unique Identifer (LSB)|Source User Unique Identifer (LSB)|
|Source Credential Type|Source Credential Type|Source Credential Type|Source Credential Type|Source Credential Type|Source Credential Type|Source Credential Type|Source Credential Type|
|Source Credential Slot (MSB)|Source Credential Slot (MSB)|Source Credential Slot (MSB)|Source Credential Slot (MSB)|Source Credential Slot (MSB)|Source Credential Slot (MSB)|Source Credential Slot (MSB)|Source Credential Slot (MSB)|
|Source Credential Slot (LSB)<br>|Source Credential Slot (LSB)<br>|Source Credential Slot (LSB)<br>|Source Credential Slot (LSB)<br>|Source Credential Slot (LSB)<br>|Source Credential Slot (LSB)<br>|Source Credential Slot (LSB)<br>|Source Credential Slot (LSB)<br>|
|Destination User Unique Identifer (MSB)<br>|Destination User Unique Identifer (MSB)<br>|Destination User Unique Identifer (MSB)<br>|Destination User Unique Identifer (MSB)<br>|Destination User Unique Identifer (MSB)<br>|Destination User Unique Identifer (MSB)<br>|Destination User Unique Identifer (MSB)<br>|Destination User Unique Identifer (MSB)<br>|
|Destination User Unique Identifer (LSB)|Destination User Unique Identifer (LSB)|Destination User Unique Identifer (LSB)|Destination User Unique Identifer (LSB)|Destination User Unique Identifer (LSB)|Destination User Unique Identifer (LSB)|Destination User Unique Identifer (LSB)|Destination User Unique Identifer (LSB)|
|Destination Credential Slot (MSB)|Destination Credential Slot (MSB)|Destination Credential Slot (MSB)|Destination Credential Slot (MSB)|Destination Credential Slot (MSB)|Destination Credential Slot (MSB)|Destination Credential Slot (MSB)|Destination Credential Slot (MSB)|
|Destination Credential Slot (LSB)|Destination Credential Slot (LSB)|Destination Credential Slot (LSB)|Destination Credential Slot (LSB)|Destination Credential Slot (LSB)|Destination Credential Slot (LSB)|Destination Credential Slot (LSB)|Destination Credential Slot (LSB)|
|User Credential Association Status|User Credential Association Status|User Credential Association Status|User Credential Association Status|User Credential Association Status|User Credential Association Status|User Credential Association Status|User Credential Association Status|


For “Source User Unique Identifier”, “Source Credential Type”, “Source Credential Slot”, “Destination
User Unique Identifier”, and “Destination Credential Slot” descriptions, refer to the _User_ _Unique_
_Identifier_ _Credential_ _Association_ _Set_ _Command_ .


**User** **Credential** **Association** **Status** **(8** **bits)**

This field indicates the result of the user credential association set process.

CC:0083.01.13.11.000 This field MUST comply with Table 2.547.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 562




<!-- PAGE 564 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024



Table 2.547: User Credential Association Report::User Credential




















|Value|Table 2.547: User Cred Association Status Name|dential Association Report::User Credential Definition|
|---|---|---|
|Value|Name|Defnition|
|0x00|Success|The operation was performed successfully, and now the<br>Source Credential is associated with the Destination User<br>Unique Identifer and stored in the Destination Credential<br>Slot.<br>|
|0x01|Source User Unique Identi-<br>fer Invalid|The Source User Unique Identifer does not reference a<br>valid user identifer, for example because the identifer pro-<br>vided is outside the allowed range or set to zero.<br>|
|0x02|Source User Unique Identi-<br>fer Nonexistent|The Source User Unique Identifer does not reference an<br>existing user on the target device.|
|0x03|Source Credential Type In-<br>valid|The Source Credential Type does not reference a valid<br>credential type for the target device, for example because<br>the identifer provided does not refer to a credential type<br>supported by that device.|
|0x04|Source Credential Slot In-<br>valid|The Source Credential Slot does not reference a valid cre-<br>dential slot, for example because the identifer provided is<br>outside the allowed range.|
|0x05|Source<br>Credential<br>Slot<br>Empty|The Source Credential Slot does not reference an existing<br>credential on the target device.<br>|
|0x06|Destination<br>User<br>Unique<br>Identifer Invalid|The Destination User Unique Identifer does not reference<br>a valid user identifer, for example because the identifer<br>provided is outside the allowed range.<br>|
|0x07|Destination<br>User<br>Unique<br>Identifer Nonexistent|The Destination User Unique Identifer does not reference<br>an existing user on the target device.|
|0x08|Destination Credential Slot<br>Invalid|The Destination Credential Slot does not reference a valid<br>credential slot, for example because the identifer provided<br>is outside the allowed range.|
|0x09|Destination Credential Slot<br>Occupied|The Destination Credential Slot is already occupied by an<br>existing credential prior to the attempted operation.|



CC:0083.01.13.11.001 All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.


**2.2.118.23** **All** **Users** **Checksum** **Get** **Command**


This command is used to request an All Users checksum representing the User Unique Identifiers,
User Types, User Active States, Credential Rules, User Name Encodings, User Name Lengths, User
Names, and all the Credentials currently set at the receiving node for all User Unique Identifiers with
any data.


CC:0083.01.14.11.000 This command MUST be ignored by a node advertising no support for the All Users Checksum
functionality in the _User_ _Capabilities_ _Report_ _Command_ .


CC:0083.01.14.11.001 The _All_ _Users_ _Checksum_ _Report_ _Command_ MUST be returned in response to this command if the All
Users Checksum functionality is advertised as supported in the User Capabilities Report Command.


CC:0083.01.14.11.002 This command MUST NOT be issued via multicast addressing.


CC:0083.01.14.11.003 A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel Multi-End Point
destination are all considered multicast addressing methods.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|
|Command = ALL_USERS_CHECKSUM_GET (0x14)|Command = ALL_USERS_CHECKSUM_GET (0x14)|Command = ALL_USERS_CHECKSUM_GET (0x14)|Command = ALL_USERS_CHECKSUM_GET (0x14)|Command = ALL_USERS_CHECKSUM_GET (0x14)|Command = ALL_USERS_CHECKSUM_GET (0x14)|Command = ALL_USERS_CHECKSUM_GET (0x14)|Command = ALL_USERS_CHECKSUM_GET (0x14)|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 563




<!-- PAGE 565 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.118.24** **All** **Users** **Checksum** **Report** **Command**


This command is used to advertise the current All Users checksum representing the User Unique
Identifiers, User Types, User Active States, Credential Rules, User Name Encodings, User Name
Lengths, User Names, and all the Credentials set at the sending node for all User Unique Identifiers
with any data. For these field’s definitions, refer to the _User_ _Set_ _Command_ and the _Credential_ _Set_
_Command_ .

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|
|Command = ALL_USERS_CHECKSUM_REPORT (0x15)|Command = ALL_USERS_CHECKSUM_REPORT (0x15)|Command = ALL_USERS_CHECKSUM_REPORT (0x15)|Command = ALL_USERS_CHECKSUM_REPORT (0x15)|Command = ALL_USERS_CHECKSUM_REPORT (0x15)|Command = ALL_USERS_CHECKSUM_REPORT (0x15)|Command = ALL_USERS_CHECKSUM_REPORT (0x15)|Command = ALL_USERS_CHECKSUM_REPORT (0x15)|
|All Users Checksum (MSB)|All Users Checksum (MSB)|All Users Checksum (MSB)|All Users Checksum (MSB)|All Users Checksum (MSB)|All Users Checksum (MSB)|All Users Checksum (MSB)|All Users Checksum (MSB)|
|All Users Checksum (LSB)|All Users Checksum (LSB)|All Users Checksum (LSB)|All Users Checksum (LSB)|All Users Checksum (LSB)|All Users Checksum (LSB)|All Users Checksum (LSB)|All Users Checksum (LSB)|



**All** **Users** **Checksum** **(16** **bits)**

This field is used to advertise the checksum representing the User Unique Identifiers, User Types,
User Active States, Credential Rules, User Name Encodings, User Name Lengths, User Names, and
all Credentials set at the sending node for all User Unique Identifiers with any data.


CC:0083.01.15.11.000 The checksum MUST be calculated using the CRC-CCITT polynomium using initialization value
equal to 0x1D0F and 0x1021 (normal representation). Refer to _CRC-CCITT_ _Source_ _Code_ for details.


CC:0083.01.15.12.011 If the on-demand calculation of the checksum of the full database on that particular device might take
longer than 2 seconds, it is RECOMMENDED to either calculate the checksum in background after
each database modification or not to support the All Users Checksum feature.

CC:0083.01.15.11.001 The checksum data MUST be built by concatenating the User Unique Identifier, User Type, User
Active State, Credential Rule, User Name Encoding, User Name Length, User Name, and then defined
Credentials data in the ascending Credential Type and then Slot Number order for the User Unique
Identifier where User Unique Identifier is also in ascending order.

CC:0083.01.15.11.002 Each User Unique Identifier checksum MUST be formatted as follows:

User Unique Identifier (16 bits) | User Type (8 bits) | User Active State (8 bits) | Credential
Rule (8 bits) | User Name Encoding (8 bits) | User Name Length (8 bits) | User Name
(User Name Length bytes)

Followed with each defined User Unique Identifier Credential data formatted as follows:


Credential Type (8 bits) | Credential Slot (16 bits) | Credential Length (8 bits) | Credential
Data (Credential Length bytes)


CC:0083.01.15.11.003 Credential Length and Credential Data MUST be set to what is reported in the _Credential_ _Report_
_Command_ .


CC:0083.01.15.11.004 If a Credential Length of 0 is reported or a hashed value is reported rather than the full Credential
Data, that Credential Length of 0 or hashed Credential Data value MUST be used in the checksum
calculation.

CC:0083.01.15.11.005 If there is no Credential data set for a User Unique Identifier, the checksum MUST NOT be modified
other than for the User Unique Identifier data.


CC:0083.01.15.11.006 If there is no Users data (and thus no Credentials data) set at the node at all, the checksum MUST
be set to 0x0000.


For example, a node with Users Data:

User Unique Identifier 0x0003, User Type 0x04 (Non-Access User), User Active State 0x01
(Occupied Enabled), Credential Rule 0x01 (Single), User Name Encoding 0x00 (Standard
ASCII), User Name Length 0x06, User Name Jackie


and 4 Credentials that are set as follows:


       - Credential Type 0x01 (PIN Code), Credential Slot 0x0002, Credential Length 4,
Credential Data 9277


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 564




<!-- PAGE 566 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


       - Credential Type 0x01 (PIN Code), Credential Slot 0x0004, Credential Length 6,
Credential Data 954988


       - Credential Type 0x02 (Password), Credential Slot 0x0001, Credential Length 17,
Credential Data zwavenodepassword


       - Credential Type 0x09 (Finger Biometric), Credential Slot 0x0008, Credential Length
2, Credential Data 0x4583 (Hashed Biometric Data)

User Unique Identifier 0x0005, User Type 0x00 (General User), User Active State 0x01
(Occupied Enabled), Credential Rule 0x01 (Single), User Name Encoding 0x00 (Standard
ASCII), User Name Length 0x04, User Name Mike


and 2 Credentials that are set as follows:


       - Credential Type 0x01 (PIN Code), Credential Slot 0x0003, Credential Length 4,
Credential Data 4812


       - Credential Type 0x08 (Face Biometric), Credential Slot 0x0003, Credential Length
2, Credential Data 0x2755 (Hashed Biometric Data)

User Unique Identifier 0x0007, User Type 0x06 (Disposable User), User Active State 0x01
(Occupied Enabled), Credential Rule 0x01 (Single), User Name Encoding 0x00 (Standard
ASCII), User Name Length 0x00


and no Credentials set

CC:0083.01.15.11.007 In this case, data for the User Unique Identifier MUST be concatenated to obtain the checksum data
in this way:


0x0003 | 0x04 | 0x01 | 0x01 | 0x00 | 0x06 | 0x4A 61 63 6B 69 65


      - 0x01 | 0x0002 | 0x04 | 0x39 32 37 37


      - 0x01 | 0x0004 | 0x06 | 0x39 35 34 39 38 38


      - 0x02 | 0x0001 | 0x11 | 0x7A 77 61 76 65 6E 6F 64 65 70 61 73 73 77 6F 72 64


      - 0x09 | 0x0008 | 0x02 | 0x45 83


0x0005 | 0x00 | 0x01 | 0x01 | 0x00 | 0x04 | 0x4D 69 6B 65


      - 0x01 | 0x0003 | 0x04 | 0x34 38 31 32


      - 0x08 | 0x0003 | 0x02 | 0x27 55


0x0007 | 0x06 | 0x01 | 0x01 | 0x00 | 0x00


CC:0083.01.15.11.008 The checksum data MUST be: 0x000304010100064A61636B6965010002043932373701000406393534393838

020001117A776176656E6F646570617373776F7264090008024583000500010100044D696B650100030434383132

08000302275500070601010000.

CC:0083.01.15.11.009 The returned All Users Checksum field MUST be set to: 0x084A.


CC:0083.01.15.11.010 For another example, a node with no Users Data set, MUST return 0x0000 since there are no Users
or Credentials at the node.


**2.2.118.25** **User** **Checksum** **Get** **Command**


This command is used to request a User checksum representing the User Type, User Active State,
Credential Rule, and all the Credentials currently set at the receiving node for a User Unique Identifier.
For these field’s definitions, refer to the _User_ _Set_ _Command_ and the _Credential_ _Set_ _Command_ .


CC:0083.01.16.11.000 This command MUST be ignored by a node advertising no support for the User Checksum functionality
in the _User_ _Capabilities_ _Report_ _Command_ .


CC:0083.01.16.11.001 The _User_ _Checksum_ _Report_ _Command_ MUST be returned in response to this command if the User
Checksum functionality is advertised as supported in the _User_ _Capabilities_ _Report_ _Command_ .


CC:0083.01.16.11.002


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 565




<!-- PAGE 567 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


This command MUST NOT be issued via multicast addressing.


CC:0083.01.16.11.003 A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel Multi-End Point
destination are all considered multicast addressing methods.




|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|
|Command = USER_CHECKSUM_GET (0x16)<br>|Command = USER_CHECKSUM_GET (0x16)<br>|Command = USER_CHECKSUM_GET (0x16)<br>|Command = USER_CHECKSUM_GET (0x16)<br>|Command = USER_CHECKSUM_GET (0x16)<br>|Command = USER_CHECKSUM_GET (0x16)<br>|Command = USER_CHECKSUM_GET (0x16)<br>|Command = USER_CHECKSUM_GET (0x16)<br>|
|User Unique Identifer (MSB)<br>|User Unique Identifer (MSB)<br>|User Unique Identifer (MSB)<br>|User Unique Identifer (MSB)<br>|User Unique Identifer (MSB)<br>|User Unique Identifer (MSB)<br>|User Unique Identifer (MSB)<br>|User Unique Identifer (MSB)<br>|
|User Unique Identifer (LSB)|User Unique Identifer (LSB)|User Unique Identifer (LSB)|User Unique Identifer (LSB)|User Unique Identifer (LSB)|User Unique Identifer (LSB)|User Unique Identifer (LSB)|User Unique Identifer (LSB)|



**User** **Unique** **Identifier** **(16** **bits)**

See _User_ _Set_ _Command_ for this field’s description.


**2.2.118.26** **User** **Checksum** **Report** **Command**


This command is used to advertise the current User checksum representing the User Type, User Active
State, Credential Rule, User Name Encoding, User Name Length, User Name, and all the Credentials
set at the sending node for a User Unique Identifier.





|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|
|Command = USER_CHECKSUM_REPORT (0x17)<br>|Command = USER_CHECKSUM_REPORT (0x17)<br>|Command = USER_CHECKSUM_REPORT (0x17)<br>|Command = USER_CHECKSUM_REPORT (0x17)<br>|Command = USER_CHECKSUM_REPORT (0x17)<br>|Command = USER_CHECKSUM_REPORT (0x17)<br>|Command = USER_CHECKSUM_REPORT (0x17)<br>|Command = USER_CHECKSUM_REPORT (0x17)<br>|
|User Unique Identifer (MSB)<br>|User Unique Identifer (MSB)<br>|User Unique Identifer (MSB)<br>|User Unique Identifer (MSB)<br>|User Unique Identifer (MSB)<br>|User Unique Identifer (MSB)<br>|User Unique Identifer (MSB)<br>|User Unique Identifer (MSB)<br>|
|User Unique Identifer (LSB)|User Unique Identifer (LSB)|User Unique Identifer (LSB)|User Unique Identifer (LSB)|User Unique Identifer (LSB)|User Unique Identifer (LSB)|User Unique Identifer (LSB)|User Unique Identifer (LSB)|
|User Checksum (MSB)|User Checksum (MSB)|User Checksum (MSB)|User Checksum (MSB)|User Checksum (MSB)|User Checksum (MSB)|User Checksum (MSB)|User Checksum (MSB)|
|User Checksum (LSB)|User Checksum (LSB)|User Checksum (LSB)|User Checksum (LSB)|User Checksum (LSB)|User Checksum (LSB)|User Checksum (LSB)|User Checksum (LSB)|


**User** **Unique** **Identifier** **(16** **bits)**

See _User_ _Set_ _Command_ for this field’s description.


**User** **Checksum** **(16** **bits)**

This field is used to advertise the checksum representing the User Type, User Active State, Credential
Rule, User Name Encoding, User Name Length, User Name, and all Credentials set at the sending
node for a User Unique Identifier.


CC:0083.01.17.11.000 The checksum MUST be calculated using the CRC-CCITT polynomium using initialization value
equal to 0x1D0F and 0x1021 (normal representation). Refer to _CRC-CCITT_ _Source_ _Code_ for details.


CC:0083.01.17.11.001 The checksum data MUST be built by concatenating the User Type, User Active State, Credential
Rule, User Name Encoding, User Name Length, User Name, and then defined Credentials data in the
ascending Credential Type and then Slot Number order for the User Unique Identifier.

CC:0083.01.17.11.002 Each User Unique Identifier checksum MUST be formatted as follows:


User Type (8 bits) | User Active State (8 bits) | Credential Rule (8 bits) | User Name
Encoding (8 bits) | User Name Length (8 bits) | User Name (User Name Length bytes)

Followed with each defined User Unique Identifier Credential data formatted as follows:


Credential Type (8 bits) | Credential Slot (16 bits) | Credential Length (8 bits) | Credential
Data (Credential Length bytes)


CC:0083.01.17.11.003 Credential Length and Credential Data MUST be set to what is reported in the _Credential_ _Report_
_Command_ .


CC:0083.01.17.11.004


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 566




<!-- PAGE 568 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


If a Credential Length of 0 is reported or a hashed value is reported rather than the full Credential
Data, that Credential Length of 0 or hashed Credential Data value MUST be used in the checksum
calculation.

CC:0083.01.17.11.005 If there is no Credential data set for a User Unique Identifier, the checksum MUST NOT be modified
other than for the User Unique Identifier data.

CC:0083.01.17.11.006 If there is no User data (and thus no Credentials data) set at the node for a User Unique Identifier,
the checksum MUST be set to 0x0000.


For example, a node with User Data:


User Type 0x04 (Non-Access User), User Active State 0x01 (Occupied Enabled), Credential
Rule 0x01 (Single), User Name Encoding 0x00 (Standard ASCII), User Name Length 0x04,
User Name Matt


and 4 Credentials that are set as follows:


       - Credential Type 0x01 (PIN Code), Credential Slot 0x0002, Credential Length 4,
Credential Data 9277


       - Credential Type 0x01 (PIN Code), Credential Slot 0x0004, Credential Length 6,
Credential Data 954988


       - Credential Type 0x02 (Password), Credential Slot 0x0001, Credential Length 17,
Credential Data zwavenodepassword


       - Credential Type 0x0A (Hand Biometric), Credential Slot 0x0008, Credential Length
2, Credential Data 0x7199 (Hashed Biometric Data)

CC:0083.01.17.11.007 In this case, data for the User Unique Identifier MUST be concatenated to obtain the checksum data
in this way:


0x04 | 0x01 | 0x01 | 0x00 | 0x04 | 0x4D 61 74 74


      - 0x01 | 0x0002 | 0x04 | 0x39 32 37 37


      - 0x01 | 0x0004 | 0x06 | 0x39 35 34 39 38 38


      - 0x02 | 0x0001 | 0x11 | 0x7A 77 61 76 65 6E 6F 64 65 70 61 73 73 77 6F 72 64


      - 0x0A | 0x0008 | 0x02 | 0x71 99


CC:0083.01.17.11.008 The checksum data MUST be: 0x04010100044D617474010002043932373701000406393534393838020001

117A776176656E6F646570617373776F72640A0008027199.

CC:0083.01.17.11.009 The returned User Credential Checksum field MUST be set to: 0x8389.


For another example, a node with User Data:


User Type 0x04 (Non-Access User), User Active State 0x01 (Occupied Enabled), Credential
Rule 0x01 (Single), User Name Encoding 0x00 (Standard ASCII), User Name Length 0x06,
User Name Lillie


and no Credentials set.

CC:0083.01.17.11.010 In this case, data for the User Unique Identifier MUST be concatenated to obtain the checksum data
in this way:


0x04 | 0x01 | 0x01 | 0x00 | 0x06 | 0x4C 69 6C 6C 69 65


CC:0083.01.17.11.011 The checksum data MUST be: 0x04010100064C696C6C6965.

CC:0083.01.17.11.012 The returned User Credential Checksum field MUST be set to: 0xF900.

CC:0083.01.17.11.013 For another example, a node with no User Data set at User Unique Identifier 0x0010, MUST return
0x0000 since there is no User at that User Unique Identifier.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 567




<!-- PAGE 569 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.118.27** **Credential** **Checksum** **Get** **Command**


This command is used to request a Credential checksum representing the Credential Slots, Credential
Lengths, and Credential Data at the receiving node for a Credential Type. For these field’s definitions,
refer to the _Credential_ _Set_ _Command_ .


CC:0083.01.18.11.000 This command MUST be ignored by a node advertising no support for the Credential Checksum
functionality in the _Credential_ _Capabilities_ _Report_ _Command_ .


CC:0083.01.18.11.001 The _Credential_ _Checksum_ _Report_ _Command_ MUST be returned in response to this command if the
Credential Checksum functionality is advertised as supported in the _Credential_ _Capabilities_ _Report_
_Command_ .


CC:0083.01.18.11.002 This command MUST NOT be issued via multicast addressing.


CC:0083.01.18.11.003 A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel Multi-End Point
destination are all considered multicast addressing methods.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|
|Command = CREDENTIAL_CHECKSUM_GET (0x18)|Command = CREDENTIAL_CHECKSUM_GET (0x18)|Command = CREDENTIAL_CHECKSUM_GET (0x18)|Command = CREDENTIAL_CHECKSUM_GET (0x18)|Command = CREDENTIAL_CHECKSUM_GET (0x18)|Command = CREDENTIAL_CHECKSUM_GET (0x18)|Command = CREDENTIAL_CHECKSUM_GET (0x18)|Command = CREDENTIAL_CHECKSUM_GET (0x18)|
|Credential Type|Credential Type|Credential Type|Credential Type|Credential Type|Credential Type|Credential Type|Credential Type|



**Credential** **Type** **(8** **bits)**

CC:0083.01.18.11.004 This field MUST comply with values listed in Table 2.542.


**2.2.118.28** **Credential** **Checksum** **Report** **Command**


This command is used to advertise the current Credential checksum representing the Credential Slots,
Credential Lengths, and Credential Data at the receiving node for a Credential Type.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|Command Class = COMMAND_CLASS_USER_CREDENTIAL (0x83)|
|Command = CREDENTIAL_CHECKSUM_REPORT (0x19)|Command = CREDENTIAL_CHECKSUM_REPORT (0x19)|Command = CREDENTIAL_CHECKSUM_REPORT (0x19)|Command = CREDENTIAL_CHECKSUM_REPORT (0x19)|Command = CREDENTIAL_CHECKSUM_REPORT (0x19)|Command = CREDENTIAL_CHECKSUM_REPORT (0x19)|Command = CREDENTIAL_CHECKSUM_REPORT (0x19)|Command = CREDENTIAL_CHECKSUM_REPORT (0x19)|
|Credential Type|Credential Type|Credential Type|Credential Type|Credential Type|Credential Type|Credential Type|Credential Type|
|Credential Checksum (MSB)|Credential Checksum (MSB)|Credential Checksum (MSB)|Credential Checksum (MSB)|Credential Checksum (MSB)|Credential Checksum (MSB)|Credential Checksum (MSB)|Credential Checksum (MSB)|
|Credential Checksum (LSB)|Credential Checksum (LSB)|Credential Checksum (LSB)|Credential Checksum (LSB)|Credential Checksum (LSB)|Credential Checksum (LSB)|Credential Checksum (LSB)|Credential Checksum (LSB)|



**Credential** **Type** **(8** **bits)**

CC:0083.01.19.11.000 This field MUST comply with values listed in Table 2.542.


**Credential** **Checksum** **(16** **bits)**

This field is used to advertise the current Credential checksum representing the Credential Slots,
Credential Lengths, and Credential Data at the receiving node for a Credential Type.


CC:0083.01.19.11.001 The checksum MUST be calculated using the CRC-CCITT polynomium using initialization value
equal to 0x1D0F and 0x1021 (normal representation). Refer to _CRC-CCITT_ _Source_ _Code_ for details.


CC:0083.01.19.11.002 The checksum data MUST be built by concatenating the Credential Slot, Credential Length, and
Credential Data in the ascending Credential Slot order for the Credential Type.


CC:0083.01.19.11.003 Each Credential checksum MUST be formatted as follows:


Credential Slot (16 bits) | Credential Length (8 bits) | Credential Data (Credential Length
bytes)


CC:0083.01.19.11.004 Credential Length and Credential Data MUST be set to what is reported in the _Credential_ _Report_
_Command_ .


CC:0083.01.19.11.005


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 568




<!-- PAGE 570 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


If a Credential Length of 0 is reported or a hashed value is reported rather than the full Credential
Data, that Credential Length of 0 or hashed Credential Data value MUST be used in the checksum
calculation.


CC:0083.01.19.11.006 If there is no Credentials data set at the node for a Credential Type, the checksum MUST be set to
0x0000.


For example, a node with Credential data:


      Credential Type 0x01 (PIN Code), Credential Slot 0x0002, Credential Length 4, Credential Data
9277


      Credential Type 0x01 (PIN Code), Credential Slot 0x0004, Credential Length 6, Credential Data
954988


      - Credential Type 0x02 (Password), Credential Slot 0x0001, Credential Length 17, Credential
Data zwavenodepassword


      - Credential Type 0x07 (Eye Biometric), Credential Slot 0x0008, Credential Length 2, Credential
Data 0x2401 (Hashed Biometric Data)


CC:0083.01.19.11.007 In this case, data for the Credential Type PIN Code MUST be concatenated to obtain the checksum
data in this way:


0x0002 | 0x04 | 0x39 32 37 37 | 0x0004 | 0x06 | 0x39 35 34 39 38 38


CC:0083.01.19.11.008 The checksum data MUST be: 0x00020439323737000406393534393838.

CC:0083.01.19.11.009 The returned Credential Checksum field MUST be set to: 0xD867.


CC:0083.01.19.11.010 In this case, data for the Credential Type Password MUST be concatenated to obtain the checksum
data in this way:


0x0001 | 0x11 | 0x7A 77 61 76 65 6E 6F 64 65 70 61 73 73 77 6F 72 64


CC:0083.01.19.11.011 The checksum data MUST be: 0x0001117A776176656E6F646570617373776F7264

CC:0083.01.19.11.012 The returned Credential Checksum field MUST be set to: 0xE10D.


CC:0083.01.19.11.013 In this case, data for the Credential Type Eye Biometric MUST be concatenated to obtain the checksum data in this way:


0x0008 | 0x02 | 0x24 01


CC:0083.01.19.11.014 The checksum data MUST be: 0x0008022401

CC:0083.01.19.11.015 The returned Credential Checksum field MUST be set to: 0xC06E.


CC:0083.01.19.11.016 In this case, data for the Credential Type RFID Code MUST return 0x0000 since there are no RFID
Codes set at the node.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 569