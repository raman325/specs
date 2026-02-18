<!-- PAGE 1125 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.2.18** **Thermostat** **Setback** **Command** **Class,** **version** **1**


**6.2.18.1** **Mandatory** **interview**


CL:0047.01.21.01.1 A node controlling this command class MUST perform a supporting node interview according to
Figure 6.23.


Figure 6.23: Thermostat Setback Command Class interview


**6.2.18.2** **Minimum** **end** **user** **functionalities**


CL:0047.01.31.01.1 A node controlling this command class MUST allow the end user to perform the actions described
below.


**6.2.18.2.1** **Configure** **setback**


CL:0047.01.31.02.1 When the end user performs this action, the issued command MUST comply with Table 6.26.


Table 6.26: Thermostat Setback::Change setback for a supported

|Table 6. type Field|.26: Thermostat Setback::Change setback for a supported Value|
|---|---|
|Field|Value|
|Command|THERMOSTAT_SETBACK_SET<br>|
|Setback Type|User defned among 0x00..0x02<br>|
|Setpoint State|User defned among 0x00..0x7A and 0x80..0xFF|



**6.2.18.3** **Node** **properties**


CL:0047.01.42.01.1 Controller SHOULD have a UI allowing the end user to see the following properties:


     - Last known setback type and state.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1124




<!-- PAGE 1126 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.2.19** **Thermostat** **Setpoint** **Command** **Class,** **version** **1-3**


**6.2.19.1** **Mandatory** **interview**


CL:0043.01.21.01.1 A node controlling this command class MUST perform a supporting node interview according to
Figure 6.24.


Figure 6.24: Thermostat Setpoint Command Class interview


It has been found that early implementations of this Command Class applied two non-interoperable
interpretations of the bit mask advertising the support for specific Setpoint Types in the Thermostat
Setpoint Supported Report Command.

Refer to the Thermostat Setpoint Command Class definition (Section 2.2.114, Section 2.2.115) for the
possible bitmask interpretations.


CL:0043.01.22.01.1 A controlling node SHOULD determine the supported Setpoint Types of a version 1 and version 2
supporting node by sending one Thermostat Setpoint Get Command at a time while incrementing
the requested Setpoint Type.


CL:0043.01.21.03.1 If the same Setpoint Type is advertised in the returned Thermostat Setpoint Report Command, the
controlling node MUST conclude that the actual Setpoint Type is supported.


If the Setpoint Type 0x00 (type N/A) is advertised in the returned Thermostat Setpoint Report
CL:0043.01.21.04.1 Command, the controlling node MUST conclude that the actual Setpoint Type is not supported.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1125




<!-- PAGE 1127 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.2.19.2** **Minimum** **end** **user** **functionalities**


CL:0043.01.31.01.1 A node controlling this command class MUST allow the end user to perform the actions described
below.


**6.2.19.2.1** **Change** **setpoint** **for** **a** **supported** **type**


CL:0043.01.31.02.1 When the end user performs this action, the issued command MUST comply with Table 6.27.


Table 6.27: Thermostat Setpoint::Change setpoint for a supported

|Table 6. type Field|.27: Thermostat Setpoint::Change setpoint for a supported Value|
|---|---|
|Field|Value|
|Command|THERMOSTAT_SETPOINT_SET<br>|
|Setpoint Type|User defned among supported<br>|
|Setpoint Value|If nodes are version 3 or newer: User defned among supported values<br>If nodes are version 1 or 2: User defned.<br>|
|Precision|User defned<br>|
|Scale|Controller defned<br>|
|Size|User defned|



CL:0043.01.31.03.1 If controlling a version 1 or 2 supporting node, the controlling node MUST allow the user to define
the Setpoint Value freely. The controlling node MUST read back the value with a Thermostat Mode
Get(Setpoint type) or use Supervision Get encapsulation and indicate to the end user if the operation
was successful.


CL:0043.01.31.04.1 The end user MUST be able to set the setpoint for any setpoint type, even if the controlling node
does not know what a given type represents.

CL:0043.01.31.05.1 The Scale field value MUST be identical to the value received in the Thermostat Setpoint Report for
the actual Setpoint Type during the node interview.

CL:0043.01.42.01.1 The controlling node SHOULD let the user define the Setpoint Value in their preferred scale but
MUST convert the value into the supporting node’s scale for issuing the Z-Wave Command.


**6.2.19.3** **Node** **properties**


CL:0043.01.42.01.1 A controlling node SHOULD have a UI allowing the end user to see the following properties:


     - Last known setpoint value for each supported setpoint type.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1126




<!-- PAGE 1128 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.2.20** **User** **Code** **Command** **Class,** **version** **1-2**


**6.2.20.1** **Mandatory** **interview**


CL:0063.01.21.01.2 A node controlling this command class MUST perform a supporting node interview according to
Figure 6.25.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1127




<!-- PAGE 1129 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Figure 6.25: User Code Command Class interview


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1128




<!-- PAGE 1130 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


CL:0063.01.21.02.3 For a node controlling version 2 or newer:

     - It is OPTIONAL to send an _Extended_ _User_ _Code_ _Get_ _Command_ for every User Identifier to a
node supporting version 2 or newer if:


**–** The controlling node requested the checksum and it is set to 0, or


**–** The controlling node issues an _Extended_ _User_ _Code_ _Set_ _Command_ (User ID = 0, User ID
Status = 0) to delete all user codes, or

**–** The supporting node reports that no more User Identifiers are set in the _Extended_ _User_
_Code_ _Report_ _Command_ with the _Next_ _User_ _Identifier_ field.

     - It is OPTIONAL to send a _User_ _Code_ _Get_ _Command_ for every User Identifier to a node supporting version 1 if the controlling node issues a _User_ _Code_ _Set_ _Command_ (User ID = 0, User
ID Status = 0) to delete all user codes.


CL:0063.01.21.03.1 For a node controlling version 1:

     - It is OPTIONAL to send a _User_ _Code_ _Get_ _Command_ for every User Identifier to any supporting
node if the controlling node issues a _User_ _Code_ _Set_ _Command_ (User ID = 0, User ID Status =
0) to delete the user codes below User ID 256.


CL:0063.01.22.01.1 A controlling node SHOULD NOT automatically delete any user code unless it is the initial interview
right after having included the supporting node in the network.


**6.2.20.2** **Minimum** **end** **user** **functionalities**


CL:0063.01.31.01.1 A node controlling this command class MUST allow the end user to perform the actions described
below.


**6.2.20.2.1** **Set/modify** **a** **User** **Code**


CL:0063.01.31.02.1 When the end user performs this action, the issued command MUST comply with Table 6.28 if nodes
are v1 or Table 6.29 if nodes are v2 or newer.


Table 6.28: User Code::Set a User Code

|Field|Value|
|---|---|
|Command<br>|USER_CODE_SET (0x01)<br>|
|User Identifers|User defned or controlling node defned among supported User<br>Identifers.<br>|
|User ID Status|Used defned among 0x01 and 0x02<br>0x02 must be used to set a reserved/forbidden user code.<br>|
|User Code|User defned among 0x30..0x39 with a length in the range 4..10<br>bytes.|



A forbidden or reserved User Code is a User Code that cannot be used at the supporting node and
cannot be allocated to a new user, for example if User Code can also be updated locally via a user
interface.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1129




<!-- PAGE 1131 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024

|Table Field|6.29: User Code::Set a User Code (v2) Value|
|---|---|
|Field|Value|
|Command|EXTENDED_USER_CODE_SET (0x0B)<br>|
|Number of User Codes (v2)<br>|Controlling node defned<br>|
|User Identifer 1..M (v2)|User defned or controlling node defned among supported User<br>Identifers.<br>|
|User ID status (v2)|Used defned among supported User ID statuses.<br>|
|User Code Length (v2)|Controlling node defned based on the length of the User Code<br>feld.<br>|
|User Code (v2)|User defned among supported ASCII characters with a length in<br>the range 4..10 bytes.|



**6.2.20.2.2** **Erase** **a** **User** **Code**


CL:0063.01.31.03.1 When the end user performs this action, the issued command MUST comply with Table 6.30 if nodes
are v1 and Table 6.31 if nodes are v2 or newer.

|Field|Table 6.30: User Code::Erase a User Code Value|
|---|---|
|Field|Value|
|Command<br>|USER_CODE_SET<br>|
|User Identifers|User defned or controlling node defned among supported User Identifers.|
|User ID Status|Used 0x00|
|User Code|0x00000000|



CL:0063.01.31.04.1 A controlling node MAY allow the end user to erase all user codes at once. In this case, the User
Identifier field MUST be set to 0x00.











|Field|Table 6.31: User Code::Erase a User Code Value|
|---|---|
|Field|Value|
|Command|EXTENDED_USER_CODE_SET (0x0B)<br>|
|Number of User Codes<br>(v2)<br>|Controlling node defned<br>|
|User<br>Identifer<br>1..M<br>(v2)|User defned or controlling node defned among supported User Identifers.|
|User ID status (v2)|0x00|
|User Code Length(v2)|0x00|
|User Code (v2)|Omitted|


**6.2.20.2.3** **Set** **the** **keypad** **mode** **(v2)**


CL:0063.01.31.05.1 This action MUST be available to the end user if nodes are v2 or newer and the supporting node
supports more than one keypad mode. When the end user performs this action, the issued command
MUST comply with Table 6.32.

|Field|Table 6.32: User Code::Set the Keypad Mode Value|
|---|---|
|Field|Value|
|Command (v2)|USER_CODE_KEYPAD_MODE_SET (0x08)<br>|
|Keypad Mode (v2)|User defned among supported keypad modes.|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1130




<!-- PAGE 1132 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.2.20.2.4** **Set** **the** **Admin** **Code** **(v2)**


CL:0063.01.31.06.1 This action MUST be available to the end user if nodes are v2 or newer and the supporting node
supports the Admin Code functionality. When the end user performs this action, the issued command
MUST comply with Table 6.33.

|Field|Table 6.33: User Code::Set the Admin Code Value|
|---|---|
|Field|Value|
|Command (v2)|ADMIN_CODE_SET (0x0E)<br>|
|Admin Code Length<br>(v2)|Controlling node defned based on the length of the User Code feld.<br>It MUST be possible to de-activate the Admin Code if the supporting<br>node supports Admin Code Deactivation.<br>|
|Admin Code (v2)|User defned among supported ASCII characters with a length in the<br>range 4..10 bytes.|



**6.2.20.3** **Node** **properties**


CL:0063.01.41.01.1 Controller MUST have a UI allowing the end user to see the following properties:


     - Number of supported User Codes


     - The list of last known set User Codes


     - The current keypad mode, if the supporting node supports more than one (v2)


     - The current set Admin Code, if the supporting node supports a Admin Code (v2)


**6.2.20.4** **Additional** **control** **requirements**


It has been found that some version 1 nodes wrongfully report obfuscated User Codes in the User
Code Report (e.g. ‘******’).


CL:0063.01.52.01.1 A controlling node SHOULD understand that a code has been set correctly but cannot be read back
with such nodes.


CL:0063.01.52.02.1 If nodes are version 2 or newer, a controlling node SHOULD verify the User Code checksum (if
supported) periodically (e.g. once a day) to ensure that User Code databases are synchronized.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1131