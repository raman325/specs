<!-- PAGE 1133 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.2.21** **User** **Credential** **Command** **Class,** **version** **1**


**6.2.21.1** **Mandatory** **interview**


CL:0083.01.21.01.1 A node controlling this command class MUST perform a supporting node interview according to
Figure 6.26.


Figure 6.26: User Credential Command Class interview


CL:0083.01.22.02.1 If the All Users Checksum Support field is set in the _User Capabilities Report Command_, the controlling
node SHOULD send an _All_ _Users_ _Checksum_ _Get_ _Command_ to check if there are existing Users or
Credentials present on the supporting node.


CL:0083.01.22.03.1 If the supporting node does not support the _All_ _Users_ _Checksum_ _Get_ _Command_, or if it does and the
All Users Checksum field of the _All_ _Users_ _Checksum_ _Report_ _Command_ is non-zero, the controlling
node SHOULD perform an interview of the existing Users and Credentials according to Figure 6.27.


Figure 6.27: User Credential Command Class optional interview


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1132




<!-- PAGE 1134 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.2.21.2** **Minimum** **end** **user** **functionalities**


CL:0083.01.31.04.1 A node controlling this command class MUST allow the end user to perform the actions described
below.


**6.2.21.2.1** **Add/Modify** **a** **User**


CL:0083.01.31.05.1 When the end user performs this action, the issued command MUST comply with Table 6.34.


Table 6.34: User Credential::Add/Modify a User


|Field|Value|
|---|---|
|Command|USER_SET (0x05)<br>|
|Operation Type<br>|Controlling node defned as Add (0x00) or Modify (0x01).<br>|
|User Unique Identifer|User defned or controlling node defned among supported User<br>Identifers in the range of what was specifed as supported in the<br>_User Capabilities Report Command_.<br>|
|User Type|User defned or controlling node defned among the Supported<br>User Types as specifed in the _User Capabilities Report Com-_<br>_mand_.<br>|
|User Active State|User defned or controlling node defned.<br>|
|Credential Rule|User defned or controlling node defned among the Supported<br>Credential Rules as specifed in the_ User Capabilities Report Com-_<br>_mand_.<br>|
|Expiring Timeout Minutes|User defned or controlling node defned. This MUST be non-zero<br>if the User Type is Expiring User (0x07) and MUST be zero if<br>the User Type is not Expiring User (0x07).<br>|
|User Name Encoding|Controlling node defned.<br>|
|User Name Length|Controlling node defned based on the length of the User Name.<br>|
|User Name|User defned or controlling node defned among supported User<br>Name Encoding characters and User Name Length.|



CL:0083.01.33.06.1


CL:0083.01.32.07.1


CL:0083.01.31.08.1



A controlling node MAY offer the User Types under different names. If they are renamed they
SHOULD be accompanied by a description, and the name mapping MUST be noted in the product
documentation.



CL:0083.01.31.09.1 If a controlling node does not offer all User Types, it MUST make note of which User Types are not
controlled in the product documentation.


CL:0083.01.31.10.1
If a controlling node does not offer all Credential Rules, it MUST make note of which Credential Rules
are not controlled in the product documentation.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1133




<!-- PAGE 1135 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.2.21.2.2** **Delete** **a** **User**


CL:0083.01.31.11.1 When the end user performs this action, the issued command MUST comply with Table 6.35.


Table 6.35: User Credential::Delete a User

|Field|Value|
|---|---|
|Command|USER_SET (0x05)<br>|
|Operation Type<br>|Controlling node defned as Delete (0x02).<br>|
|User Unique Identifer|User defned or controlling node defned among supported User<br>Identifers in the range of what was specifed as supported in the<br>_User Capabilities Report Command_.<br>|
|User Type|Omitted or controlling node defned as the default value.<br>|
|User Active State|Omitted or controlling node defned as the default value.<br>|
|Credential Rule|Omitted or controlling node defned as the default value.<br>|
|Expiring Timeout Minutes|Omitted or controlling node defned as the default value.<br>|
|User Name Encoding|Omitted or controlling node defned as the default value.<br>|
|User Name Length|Omitted or controlling node defned as the default value.<br>|
|User Name|Omitted or controlling node defned as the default value.|



CL:0083.01.33.12.1 A controlling node MAY allow the end user to erase all Users and their associated Credentials and

CL:0083.01.31.13.1 schedules at once. In this case, the User Unique Identifier field MUST be set to 0x0000.


**6.2.21.2.3** **Add/Modify** **a** **Credential**


CL:0083.01.31.14.1 When the end user performs this action, the issued command MUST comply with Table 6.36.


Table 6.36: User Credential::Add/Modify a Credential

|Field|Value|
|---|---|
|Command<br>|CREDENTIAL_SET (0x0A)<br>|
|User Unique Identifer|User defned or controlling node defned among supported User<br>Identifers in the range of what was specifed as supported in the<br>_User Capabilities Report Command_.<br>|
|Credential Type|User defned or controlling node defned among supported Cre-<br>dential Types specifed in the_ Credential Capabilities Report Com-_<br>_mand_.<br>|
|Credential Slot|User defned or controlling node defned in the range of one to the<br>Number of Supported Credential Slots for the given Credential<br>Type in the _Credential Capabilities Report Command_.<br>|
|Operation Type|Controlling node defned as Add (0x00) or Modify (0x01).<br>|
|Credential Length|Controlling node defned based on the length of the Credential<br>Data.<br>MUST not be less than the Min Length of Credential<br>Data for the specifc Credential Type specifed in the _Credential_<br>_Capabilities Report Command_ and MUST not be more than the<br>Max Length of Credential Data for the specifc Credential Type<br>specifed in the _Credential Capabilities Report Command_.<br>|
|Credential Data|User defned.|



CL:0083.01.33.15.1 A controlling node MAY infer the Credential Type from the Credential Data provided by the end

user.

CL:0083.01.31.16.1 If a controlling node does not offer all Credential Types, it MUST make note of which Credential
Types are not controlled in the product documentation.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1134




<!-- PAGE 1136 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.2.21.2.4** **Delete** **a** **Credential**


CL:0083.01.31.17.1 When the end user performs this action, the issued command MUST comply with Table 6.37.


Table 6.37: User Credential::Delete a Credential

|Field|Value|
|---|---|
|Command<br>|CREDENTIAL_SET (0x0A)<br>|
|User Unique Identifer|User defned or controlling node defned among supported User<br>Identifers in the range of what was specifed as supported in the<br>_User Capabilities Report Command_.<br>|
|Credential Type|User defned or controlling node defned among supported Cre-<br>dential Types specifed in the_ Credential Capabilities Report Com-_<br>_mand_.<br>|
|Credential Slot|User defned or controlling node defned in the range of one to the<br>Number of Supported Credential Slots for the given Credential<br>Type in the _Credential Capabilities Report Command_.<br>|
|Operation Type|Controlling node defned as Delete (0x02).<br>|
|Credential Length|Zero or controlling node defned.<br>|
|Credential Data|Omitted or User defned.|



CL:0083.01.33.18.1 A controlling node MAY allow the end user to erase all Credentials of a Credential Type for a User

CL:0083.01.31.19.1 Unique Identifier at once. In this case, the User Unique Identifier and Credential Type MUST be
non-zero and the Credential Slot MUST be 0x0000.


CL:0083.01.33.20.1 A controlling node MAY allow the end user to erase all Credentials of all Credential Types for a

CL:0083.01.31.21.1 User Unique Identifier at once. In this case, the User Unique Identifier MUST be non-zero and the
Credential Type MUST be 0x00.


CL:0083.01.33.22.1 A controlling node MAY allow the end user to erase all Credentials for all Users at once. In this case,

CL:0083.01.31.23.1 the User Unique Identifier MUST be 0x0000.


CL:0083.01.33.24.1 A controlling node MAY allow the end user to erase all Credentials for a Credential Type at once. In

CL:0083.01.31.25.1 this case, the User Unique Identifier and Credential Slot MUST be 0x0000 and the Credential Type
MUST be non-zero.


**6.2.21.3** **Node** **properties**


CL:0083.01.41.26.1 A controlling node MUST have a UI allowing the end user to see the following properties:


     - The list of Users and their basic properties:


**–** The User Name


**–** The User Active State


**–** The Credentials assigned to a User and their basic properties:


∗The Credential Type


CL:0083.01.42.27.1 A controlling node SHOULD have a UI allowing the end user to see the following properties:

     - The number of supported User Unique Identifiers


     - The supported Credential Rules (Single, Dual, Triple)


     - The supported Credential Types


     - The list of Users and their additional properties:

**–** The User Unique Identifier


**–** The User Type


**–** The Credential Rule


**–** The Expiring Timeout Minutes, if the User Type is Expiring User (0x07)


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1135




<!-- PAGE 1137 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**–** The Credentials assigned to a User and their additional properties:


∗The Credential Slot


∗The Credential Data


CL:0083.01.41.28.1
A node controlling this command class MUST also control the Notification Command Class, version 8
or newer and have a UI allowing the end user to see Notification Reports with the following Notification
Types.

     - **Notification** **Type** **“Access** **Control”** **(0x06)**


**–** “Credential lock/close operation” (0x23)


**–** “Credential unlock/open operation” (0x24)


**–** “All users deleted” (0x25)


**–** “Multiple credentials deleted” (0x26)


**–** “User added” (0x27)

**–** “User modified” (0x28)


**–** “User deleted” (0x29)


**–** “User unchanged” (0x2A)


**–** “Credential added” (0x2B)

**–** “Credential modified” (0x2C)


**–** “Credential deleted” (0x2D)


**–** “Credential unchanged” (0x2E)


**–** “Valid credential access denied due to User Active State being set to Occupied Disabled” (0x2F)


**–** “Valid credential access denied due to the User’s schedule being inactive” (0x30)


**–** “User access denied due to not enough credentials entered for the User’s Credential
Rule” (0x31)


**–** “Invalid credential used to access the node” (0x32)


**–** “Non-Access credential entered via local interface” (0x33)

     - **Notification** **Type** **“Emergency** **Alarm”** **(0x0A)**


**–** “Panic Alert” (0x04)


**6.2.21.4** **Additional** **control** **requirements**


CL:0083.01.51.29.1 If a node controlling this command class supports setting schedules for Unique User Identifiers, then
they MUST also control the _Schedule_ _Entry_ _Lock_ _Command_ _Class,_ _version_ _4_ _[NEVER_ _CERTIFIED]_,
or higher.


CL:0083.01.52.30.1 If the supporting node supports the _All_ _Users_ _Checksum_ _Report_ _Command_, the controlling node
SHOULD verify the All Users Checksum periodically (e.g. once a day) to ensure that the Users and
Credentials are synchronized between the supporting and controlling nodes.


CL:0083.01.52.31.1 A node controlling this command class SHOULD be resilient to receiving a _User_ _Set_ _Error_ _Report_
_Command_ or a _Credential_ _Set_ _Error_ _Report_ _Command_ when sending a _User_ _Set_ _Command_ or a
_Credential_ _Set_ _Command_, respectively, and try to resend the command with corrected fields.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1136