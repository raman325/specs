<!-- PAGE 516 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.116** **User** **Code** **Command** **Class,** **version** **1**


The User Code Command Class is used to manage User Codes in access control systems.


**2.2.116.1** **Interoperability** **Considerations**


CC:0063.01.00.32.001
A node supporting the Door Lock Command Class SHOULD reflect user code inputs in the door lock
status when relevant. (e.g. when the door becomes unlocked by a User Code input, the Door Lock
Mode is also updated to unlocked)


This Command Class can be used in conjunction with Schedule Entry Lock Command Class in order
to schedule access for users.


CC:0063.01.00.31.001 A node receiving a User Code Get Command MUST advertise what User Code is set in the User Code
Report Command.


It has been found that some version 1 nodes wrongfully report obfuscated User Codes in the User
Code Report (e.g. ‘******’).


CC:0063.01.00.32.002 A controlling node SHOULD understand that a code has been set correctly but cannot be read back
with such nodes.


**2.2.116.2** **User** **Code** **Set** **Command**


This command is used to set a User Code at the receiving node.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|
|Command = USER_CODE_SET (0x01)<br>|Command = USER_CODE_SET (0x01)<br>|Command = USER_CODE_SET (0x01)<br>|Command = USER_CODE_SET (0x01)<br>|Command = USER_CODE_SET (0x01)<br>|Command = USER_CODE_SET (0x01)<br>|Command = USER_CODE_SET (0x01)<br>|Command = USER_CODE_SET (0x01)<br>|
|User Identifer|User Identifer|User Identifer|User Identifer|User Identifer|User Identifer|User Identifer|User Identifer|
|User ID Status|User ID Status|User ID Status|User ID Status|User ID Status|User ID Status|User ID Status|User ID Status|
|User Code 1|User Code 1|User Code 1|User Code 1|User Code 1|User Code 1|User Code 1|User Code 1|
|…|…|…|…|…|…|…|…|
|User Code N|User Code N|User Code N|User Code N|User Code N|User Code N|User Code N|User Code N|



**User** **Identifier** **(8** **bits)**

This field is used to specify the actual User Identifier.

CC:0063.01.01.11.001 The implemented User Identifier values MUST be in a sequence starting from 1, i.e. a node supporting
10 User Identifiers MUST accept values in the range 1..10.

CC:0063.01.01.13.001 A receiving node MAY ignore this field if it only supports one User Code.


CC:0063.01.01.11.002 The value 0 MUST indicate that the receiving node MUST set the User Code and User Status for all

CC:0063.01.01.12.001 supported User Identifiers. The value 0 SHOULD be used only with User ID Status set to 0x00.

If a non-existing User Identifier (higher than the advertised supported users number in the Users

CC:0063.01.01.11.003
Number Report Command) is specified in this command, a receiving node MUST ignore the command.


**User** **ID** **Status** **(8** **bits)**

CC:0063.01.01.11.004 The User ID Status field indicates the status of the User Identifier. This field MUST comply with
Table 2.530.


CC:0063.01.01.12.002 The User ID Status 0xFE SHOULD NOT be used in this command and SHOULD be ignored by
receiving nodes.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 515




<!-- PAGE 517 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Table 2.530: User Code Set::User ID Status encoding

|Value|Description|
|---|---|
|0x00|Available (not set)|
|0x01|Occupied|
|0x02|Reserved by administrator|
|0x0FE|Status not available|



CC:0063.01.01.11.005 All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.


**User** **Code** **(N** **bytes)**

This field is used to advertise the User Code to be set for the User Identifier.

CC:0063.01.01.11.006 The length of this field MUST be between 4 and 10 bytes. The field’s length MUST be determined
using the length of the frame.

CC:0063.01.01.11.007 Each byte in this field MUST be a digit encoded with ASCII representation (from 0x30 to 0x39).


CC:0063.01.01.11.008 A node receiving an invalid User Code MUST ignore the command.

CC:0063.01.01.11.009 The User Code field MUST be set to 0x00000000 (4 bytes) when User ID Status is equal to 0x00.


**2.2.116.3** **User** **Code** **Get** **Command**


This command is used to request the User Code of a specific User Identifier.


CC:0063.01.02.11.001 The User Code Report Command MUST be returned in response to this command.


CC:0063.01.02.11.002 This command MUST NOT be issued via multicast addressing.


CC:0063.01.02.11.003 A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|
|Command = USER_CODE_GET (0x02)<br>|Command = USER_CODE_GET (0x02)<br>|Command = USER_CODE_GET (0x02)<br>|Command = USER_CODE_GET (0x02)<br>|Command = USER_CODE_GET (0x02)<br>|Command = USER_CODE_GET (0x02)<br>|Command = USER_CODE_GET (0x02)<br>|Command = USER_CODE_GET (0x02)<br>|
|User Identifer|User Identifer|User Identifer|User Identifer|User Identifer|User Identifer|User Identifer|User Identifer|



**User** **Identifier** **(8** **bits)**

This field is used to specify the requested User Identifier.

CC:0063.01.02.11.004 The value 0 MUST NOT be specified in the User Code Get Command.

CC:0063.01.02.12.001 If the specified User Identifier is not supported, a responding node SHOULD return a User Code
Report Command with the User ID Status set to 0xFE “Status not available”.


**2.2.116.4** **User** **Code** **Report** **Command**


This command is used to advertise a User Code and its current status.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|
|Command = USER_CODE_REPORT (0x03)<br>|Command = USER_CODE_REPORT (0x03)<br>|Command = USER_CODE_REPORT (0x03)<br>|Command = USER_CODE_REPORT (0x03)<br>|Command = USER_CODE_REPORT (0x03)<br>|Command = USER_CODE_REPORT (0x03)<br>|Command = USER_CODE_REPORT (0x03)<br>|Command = USER_CODE_REPORT (0x03)<br>|
|User Identifer|User Identifer|User Identifer|User Identifer|User Identifer|User Identifer|User Identifer|User Identifer|
|User ID Status|User ID Status|User ID Status|User ID Status|User ID Status|User ID Status|User ID Status|User ID Status|
|User Code 1|User Code 1|User Code 1|User Code 1|User Code 1|User Code 1|User Code 1|User Code 1|
|…|…|…|…|…|…|…|…|
|User Code N|User Code N|User Code N|User Code N|User Code N|User Code N|User Code N|User Code N|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 516




<!-- PAGE 518 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


For fields’ description, refer to the _User_ _Code_ _Set_ _Command_ .


**2.2.116.5** **Users** **Number** **Get** **Command**


This command is used to request the number of user codes supported by the receiving node.


CC:0063.01.04.11.001 The Users Number Report Command MUST be returned in response to this command.


CC:0063.01.04.11.002 This command MUST NOT be issued via multicast addressing.


CC:0063.01.04.11.003 A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|
|Command = USERS_NUMBER_GET (0x04)|Command = USERS_NUMBER_GET (0x04)|Command = USERS_NUMBER_GET (0x04)|Command = USERS_NUMBER_GET (0x04)|Command = USERS_NUMBER_GET (0x04)|Command = USERS_NUMBER_GET (0x04)|Command = USERS_NUMBER_GET (0x04)|Command = USERS_NUMBER_GET (0x04)|



**2.2.116.6** **Users** **Number** **Report** **Command**


This command is used to report the number of User Codes supported by the sending node.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|
|Command = USERS_NUMBER_GET (0x04)|Command = USERS_NUMBER_GET (0x04)|Command = USERS_NUMBER_GET (0x04)|Command = USERS_NUMBER_GET (0x04)|Command = USERS_NUMBER_GET (0x04)|Command = USERS_NUMBER_GET (0x04)|Command = USERS_NUMBER_GET (0x04)|Command = USERS_NUMBER_GET (0x04)|
|Supported Users|Supported Users|Supported Users|Supported Users|Supported Users|Supported Users|Supported Users|Supported Users|



**Supported** **Users** **(8** **bits)**

This field is used to advertise the number of supported User Codes.

CC:0063.01.05.11.001 This field MUST be set to the total amount of supported User Codes. The value ‘0’ MUST indicate
that no User Code is supported by the node.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 517

---

<!-- PAGE 519 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.117** **User** **Code** **Command** **Class,** **version** **2**


The User Code Command Class is used to manage user codes in access control systems.


User Code Command Class, version 2 extends the number of supported users to 65535, introduces
new User ID Statuses, keypad modes and a Admin Code functionality.


**2.2.117.1** **Terminology**


**User** **Codes** are configured on a supporting node for different **User** **Identifiers** . Each User Code is
associated to one User Identifier. An actual end user with several User Codes will also have several
User Identifiers (one for each User Code).

The entry of a user code can trigger different outcomes, such as opening a door, triggering a notification
or ignoring the code. This can be configured with the User ID status.

A supporting node may support one or several **Keypad** **Modes** . They allow configuring the keypad
to accept, ignore or treat differently keypad input.


A node may support the **Admin** **Code** functionality. The Admin Code is a separate unique code used
to get access to the node’s administrator functionalities, such as the network settings and/or User
Code management. A node may require the Admin Code to be always set and in this case advertise
that the Admin Code can be modified but cannot be deactivated using Z-Wave.


A node may support the **User** **Code** **Checksum** functionality. A controlling node can request a
checksum representing all the user code set at the supporting node to ensure that the user code
databases are synchronized.


**2.2.117.2** **Compatibility** **Considerations**


The User Code Command Class, version 2 is backwards compatible with _User_ _Code_ _Command_ _Class,_

_version_ _1_ .

CC:0063.02.00.21.001 All commands and fields not mentioned in this version MUST remain unchanged _User Code Command_
_Class,_ _version_ _1_ .

The Extended User Code Set Command permits to configure several user codes per command. The
following command has been extended to match the extended number of supported users:


      - _User_ _Code_ _Report_ _Command_


The following commands are also introduced to address the extended range of users:


      - Extended User Code Set Command


      - Extended User Code Get Command


      - Extended User Code Report Command

Commands for advertising node capabilities, configuring the keypad mode and the Admin Code are
introduced:


      - User Code Capabilities Get Command


      - User Code Capabilities Report Command


      - User Code Keypad Mode Get Command


      - User Code Keypad Mode Report Command


      - Admin Code Set Command


      - Admin Code Get Command


      - Admin Code Report Command


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 518




<!-- PAGE 520 -->

CC:0063.02.00.21.002



Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


User Code Command Class, version 2 does not extend the existing User Code Set/Get/Report commands from version 1. The first 255 users that can be addressed by the User Code Set/Get Commands
MUST be identical to the first 255 users that can be addressed by the (version 2) Extended User Code
Set/Get Commands.



CC:0063.02.00.21.003 Addressing User Codes for extended User Identifiers (in the range 256..65535) MUST be done with
the (version 2) Extended User Code Set/Get Commands.


CC:0063.02.00.21.004 A version 1 node MAY advertise support for 0 User Codes in the Users Number Report Command.


A version 2 node MUST advertise support for at least 1 User Code.

CC:0063.02.00.21.005 The implemented User Identifier values MUST be in a sequence starting from 1, i.e. a node supporting
10 Users MUST accept User Identifier values in the range 1..10. However, a controlling node MAY
assign user codes non-continuously in the range of supported User Identifier.


**2.2.117.3** **Interoperability** **Considerations**


This Command Class can be used in conjunction with the Entry Control Command Class to report
User Code input to a controlling application.


CC:0063.02.00.31.001 A node supporting the “Messaging” User ID Status MUST support the Entry Control Command
Class, version 1 or newer or the Notification Command Class, version 8 or newer.


CC:0063.02.00.31.005 A node supporting this Command Class MUST either:


      - Support the Door Lock Command Class.


      - Control the Door Lock Command Class via association groups.

CC:0063.02.00.31.003 A supporting node MUST reflect user code inputs in the door lock status when relevant. (e.g. when
the door becomes unsecured by a User Code input, the Door Lock Operation mode is updated to
unsecure with a timeout)


CC:0063.02.00.33.001 A node supporting this Command Class MAY have an Association group issuing the corresponding
Door Lock Operation Set Commands when valid User Codes are input in order to control several door
locks simultaneously.


This Command Class can be used in conjunction with Schedule Entry Lock Command Class to
schedule access for users.


CC:0063.02.00.31.004 A node receiving a User Code Get Command MUST advertise what User Code is set in the User Code
Report Command.


**2.2.117.4** **Security** **Considerations**


A node identifies users on the background of User Code entry alone without User Identifier, the
following security measures should be taken into consideration:


CC:0063.02.00.42.001 - Users SHOULD NOT be allowed to choose their own user codes. Users tend to choose codes such

as birthdates and therefore the risk of having duplicate codes is high. A user may learn about
another User Code when trying to set his own User Code and receiving a duplicate/rejection
message. In such a case, User Codes SHOULD be generated randomly by the administrating
company, if applicable.

CC:0063.02.00.42.002 - If a node is configured with a large number of User Codes: (e.g. 500), it is RECOMMENDED
to increase the number of digits in each and every user code, making is less likely to randomly
guess an assigned user code.


CC:0063.02.00.42.003 - It is RECOMMENDED to implement mechanisms preventing brute force attacks, such as exponential increasing waiting time between attempts or lock out after a number of failed attempts.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 519




<!-- PAGE 521 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


If a node allows updating User Codes or User ID Statuses locally via a user interface using a Admin
CC:0063.02.00.41.001 Code, the supporting node MUST issue User Code Report Commands via the Lifeline to advertise
local updates.


**2.2.117.5** **User** **Code** **Set** **Command**


This command is used to set a User Code at the receiving node.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|
|Command = USER_CODE_SET (0x01)<br>|Command = USER_CODE_SET (0x01)<br>|Command = USER_CODE_SET (0x01)<br>|Command = USER_CODE_SET (0x01)<br>|Command = USER_CODE_SET (0x01)<br>|Command = USER_CODE_SET (0x01)<br>|Command = USER_CODE_SET (0x01)<br>|Command = USER_CODE_SET (0x01)<br>|
|User Identifer|User Identifer|User Identifer|User Identifer|User Identifer|User Identifer|User Identifer|User Identifer|
|User ID Status|User ID Status|User ID Status|User ID Status|User ID Status|User ID Status|User ID Status|User ID Status|
|User Code 1|User Code 1|User Code 1|User Code 1|User Code 1|User Code 1|User Code 1|User Code 1|
|…|…|…|…|…|…|…|…|
|User Code N|User Code N|User Code N|User Code N|User Code N|User Code N|User Code N|User Code N|



CC:0063.02.01.11.001 All fields not described below MUST remain unchanged from version 1.


**User** **ID** **Status** **(8** **bits)**

The User ID Status field indicates the state of the User Identifier.

CC:0063.02.01.11.005 This field MUST comply with Table 2.532, however the requirements in Table 2.531 MUST take
precedence over the requirements in Table 2.532.

CC:0063.02.01.11.006 If a non-supported User ID Status is specified, a receiving node MUST ignore the command.

**User** **Identifier** **(8** **bits)**

This field is used to specify the actual User Identifier.

CC:0063.02.01.11.002 The implemented User Identifier values MUST be in a sequence starting from 1, i.e. a node supporting
10 User Codes MUST accept values in the range 1..10.


CC:0063.02.01.11.003 The value 0 MUST indicate that the receiving node MUST set the User Code and User Status for all
supported user identifiers less than 256. A receiving node supporting the User Code Command Class,
version 2 MUST NOT apply the status to users from the extended range (User ID         - 255) when this
field is set to 0.


CC:0063.02.01.12.001 The value 0 SHOULD be used only with User ID Status set to 0x00.

If a non-existing User Identifier (higher than the advertised supported users number in the Users

CC:0063.02.01.11.004
Number Report Command) is specified in this command, a receiving node MUST ignore the command


**2.2.117.6** **Users** **Number** **Report** **Command**


This command is used to report the number of users that the sending node supports.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|
|Command = USERS_NUMBER_REPORT (0x05)|Command = USERS_NUMBER_REPORT (0x05)|Command = USERS_NUMBER_REPORT (0x05)|Command = USERS_NUMBER_REPORT (0x05)|Command = USERS_NUMBER_REPORT (0x05)|Command = USERS_NUMBER_REPORT (0x05)|Command = USERS_NUMBER_REPORT (0x05)|Command = USERS_NUMBER_REPORT (0x05)|
|Supported Users|Supported Users|Supported Users|Supported Users|Supported Users|Supported Users|Supported Users|Supported Users|
|Extended Supported Users 1 (MSB)|Extended Supported Users 1 (MSB)|Extended Supported Users 1 (MSB)|Extended Supported Users 1 (MSB)|Extended Supported Users 1 (MSB)|Extended Supported Users 1 (MSB)|Extended Supported Users 1 (MSB)|Extended Supported Users 1 (MSB)|
|Extended Supported Users 2 (LSB)|Extended Supported Users 2 (LSB)|Extended Supported Users 2 (LSB)|Extended Supported Users 2 (LSB)|Extended Supported Users 2 (LSB)|Extended Supported Users 2 (LSB)|Extended Supported Users 2 (LSB)|Extended Supported Users 2 (LSB)|



**Supported** **Users** **(8** **bits)**

This field is used to advertise the number of supported users for version 1 controlling nodes.


CC:0063.02.05.11.001


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 520




<!-- PAGE 522 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


This field MUST be in the range 1..255.

CC:0063.02.05.11.002 If the node implements more than 255 users, this field MUST be set to 255.

If the node implements 255 users or less, this field MUST be set to the total amount of supported

users.


**Extended** **Supported** **Users** **(16** **bits)**

This field is used to advertise the number of supported users for version 2 controlling nodes.

CC:0063.02.05.11.003 If the node supports less than 256 users, this field MUST be identical to the Supported Users field.

If the node implements 256 users or more, this field MUST be set to the total amount of supported

users.


**2.2.117.7** **User** **Code** **Capabilities** **Get** **Command**


This command is used to request the User Code capabilities of a node.


CC:0063.02.06.11.001 The User Code Capabilities Report Command MUST be returned in response to this command.


CC:0063.02.06.11.002 This command MUST NOT be issued via multicast addressing.


CC:0063.02.06.11.003 A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|
|Command = USER_CODE_CAPABILITIES_GET (0x06)|Command = USER_CODE_CAPABILITIES_GET (0x06)|Command = USER_CODE_CAPABILITIES_GET (0x06)|Command = USER_CODE_CAPABILITIES_GET (0x06)|Command = USER_CODE_CAPABILITIES_GET (0x06)|Command = USER_CODE_CAPABILITIES_GET (0x06)|Command = USER_CODE_CAPABILITIES_GET (0x06)|Command = USER_CODE_CAPABILITIES_GET (0x06)|



**2.2.117.8** **User** **Code** **Capabilities** **Report** **Command**


This command is used to advertise User Code capabilities.











|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|
|Command = USER_CODE_CAPABILITIES_REPORT (0x07)|Command = USER_CODE_CAPABILITIES_REPORT (0x07)|Command = USER_CODE_CAPABILITIES_REPORT (0x07)|Command = USER_CODE_CAPABILITIES_REPORT (0x07)|Command = USER_CODE_CAPABILITIES_REPORT (0x07)|Command = USER_CODE_CAPABILITIES_REPORT (0x07)|Command = USER_CODE_CAPABILITIES_REPORT (0x07)|Command = USER_CODE_CAPABILITIES_REPORT (0x07)|
|AC Support|ACD Support|Res|Supported User ID Status Bit Mask Length|Supported User ID Status Bit Mask Length|Supported User ID Status Bit Mask Length|Supported User ID Status Bit Mask Length|Supported User ID Status Bit Mask Length|
|Supported User ID Status Bit Mask 1|Supported User ID Status Bit Mask 1|Supported User ID Status Bit Mask 1|Supported User ID Status Bit Mask 1|Supported User ID Status Bit Mask 1|Supported User ID Status Bit Mask 1|Supported User ID Status Bit Mask 1|Supported User ID Status Bit Mask 1|
|…|…|…|…|…|…|…|…|
|Supported User ID Status Bit Mask N|Supported User ID Status Bit Mask N|Supported User ID Status Bit Mask N|Supported User ID Status Bit Mask N|Supported User ID Status Bit Mask N|Supported User ID Status Bit Mask N|Supported User ID Status Bit Mask N|Supported User ID Status Bit Mask N|
|UCC<br>Support|MUCR<br>Support|MUCS<br>Support|Supported Keypad Modes Bit Mask Length|Supported Keypad Modes Bit Mask Length|Supported Keypad Modes Bit Mask Length|Supported Keypad Modes Bit Mask Length|Supported Keypad Modes Bit Mask Length|
|Supported Keypad Modes Bit Mask 1|Supported Keypad Modes Bit Mask 1|Supported Keypad Modes Bit Mask 1|Supported Keypad Modes Bit Mask 1|Supported Keypad Modes Bit Mask 1|Supported Keypad Modes Bit Mask 1|Supported Keypad Modes Bit Mask 1|Supported Keypad Modes Bit Mask 1|
|…|…|…|…|…|…|…|…|
|Supported Keypad Modes Bit Mask M|Supported Keypad Modes Bit Mask M|Supported Keypad Modes Bit Mask M|Supported Keypad Modes Bit Mask M|Supported Keypad Modes Bit Mask M|Supported Keypad Modes Bit Mask M|Supported Keypad Modes Bit Mask M|Supported Keypad Modes Bit Mask M|
|Reserved|Reserved|Reserved|Supported Keys Bit Mask Length|Supported Keys Bit Mask Length|Supported Keys Bit Mask Length|Supported Keys Bit Mask Length|Supported Keys Bit Mask Length|
|Supported Keys Bit Mask 1|Supported Keys Bit Mask 1|Supported Keys Bit Mask 1|Supported Keys Bit Mask 1|Supported Keys Bit Mask 1|Supported Keys Bit Mask 1|Supported Keys Bit Mask 1|Supported Keys Bit Mask 1|
|…|…|…|…|…|…|…|…|
|Supported Keys Bit Mask L|Supported Keys Bit Mask L|Supported Keys Bit Mask L|Supported Keys Bit Mask L|Supported Keys Bit Mask L|Supported Keys Bit Mask L|Supported Keys Bit Mask L|Supported Keys Bit Mask L|


**Reserved** **/** **Res**

This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**AC** **(Admin** **Code)** **Support** **(1** **bit)**


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 521




<!-- PAGE 523 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


This field indicates if the sending node supports the Admin Code functionality.


CC:0063.02.07.11.001 The value 1 MUST indicate that the Admin Code functionality is supported.


The value 0 MUST indicate that the Admin Code functionality is not supported.


**ACD** **(Admin** **Code** **Deactivation)** **Support** **(1** **bit)**

This field indicates if the sending node supports reporting the Admin Code can be deactivated using
a Admin Code Set Command.


CC:0063.02.07.11.002 The value 1 MUST indicate that the Admin Code may be deactivated by issuing a Admin Code Set
with the length field set to 0.


The value 0 MUST indicate that the Admin Code cannot be deactivated and Admin Code Set commands with the length field set to 0 will be ignored.

CC:0063.02.07.11.003 This field MUST be set to 0 by a sending node if the AC Support field is set to 0.


**UCC** **(User** **Code** **Checksum)** **Support** **(1** **bit)**

This field indicates if the sending node supports the User Code Checksum functionality.


CC:0063.02.07.11.004 The value 1 MUST indicate that the User Code Checksum functionality is supported.


The value 0 MUST indicate that the User Code Checksum functionality is not supported.


**MUCR** **(Multiple** **User** **Code** **Report)** **Support** **(1** **bit)**

This field indicates if the sending node supports reporting the Multiple User Codes at once in a single
Extended User Code Report Command. This functionality should be supported by node supporting
large amount of User Codes.


CC:0063.02.07.11.005 The value 1 MUST indicate that the Multiple User Code Report functionality is supported.


The value 0 MUST indicate that the Multiple User Code Report functionality is not supported.


**MUCS** **(Multiple** **User** **Code** **Set)** **Support** **(1** **bit)**

This field indicates if the sending node supports being set Multiple User Codes at once in a single
Extended User Code Set Command. This functionality should be supported by node supporting large
amount of User Codes.


CC:0063.02.07.11.006 The value 1 MUST indicate that the Multiple User Code Set functionality is supported.


The value 0 MUST indicate that the Multiple User Code Set functionality is not supported.


**Supported** **User** **ID** **Status** **Bit** **Mask** **Length** **(5** **bits)**

CC:0063.02.07.11.007 This field MUST advertise the length in bytes of the _Supported_ _User_ _ID_ _Status_ _Bit_ _Mask_ field carried
in the command.


CC:0063.02.07.11.008
This field MUST be set to the minimum value which allows advertising all supported User ID Statuses.


**Supported** **User** **ID** **Status** **Bit** **Mask** **(N** **bytes)**

CC:0063.02.07.11.009 This field advertises the supported User ID status values. The length of this field in bytes MUST
match the value advertised in the _Supported_ _User_ _ID_ _Status_ _Bit_ _Mask_ _Length_ field.


A node MUST support the User ID Status values 0x00, 0x01 and 0x02.


      - Bit 0 in Bit Mask 1 represents User ID status 0x00.


      - Bit 1 in Bit Mask 1 represents User ID status 0x01.


      - …


User ID Status values are described in Table 2.532.


CC:0063.02.07.11.00A If a User ID Status is supported, the corresponding bit MUST be set to ‘1’.


If a User ID Status is not supported, the corresponding bit MUST be set to ‘0’.


CC:0063.02.07.11.00B All other bits are reserved and MUST be set to zero by a sending node. Reserved bits MUST be
ignored by a receiving node.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 522




<!-- PAGE 524 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**Supported** **Keypad** **Modes** **Bit** **Mask** **Length** **(5** **bits)**

CC:0063.02.07.11.00C This field MUST advertise the length in bytes of the _Supported_ _Keypad_ _Modes_ _Bit_ _Mask_ field carried
in the command.

CC:0063.02.07.11.00D This field MUST be set to the minimum value which allows advertising all supported keypad modes.


**Supported** **Keypad** **Mode** **Bit** **Mask** **(M** **bytes)**


CC:0063.02.07.11.00E
This field describes the supported keypad mode values. The length of this field in bytes MUST match
the value advertised in the _Supported_ _Keypad_ _Modes_ _Bit_ _Mask_ Length field.


CC:0063.02.07.11.00F A node MUST support the keypad mode 0x00 (normal mode).


      - Bit 0 in Bit Mask 1 represents keypad mode 0x00 (normal mode).


      - Bit 1 in Bit Mask 1 represents keypad mode 0x01 (vacation mode).


      - …


Keypad mode values are described in Table 2.531.


CC:0063.02.07.11.010 If a keypad mode is supported, the corresponding bit MUST be set to ‘1’.


If a keypad mode is not supported, the corresponding bit MUST be set to ‘0’.


CC:0063.02.07.11.011 All other bits are reserved and MUST be set to zero by a sending node. Reserved bits MUST be
ignored by a receiving node.


**Supported** **Keys** **Bit** **Mask** **Length** **(5** **bits)**

CC:0063.02.07.11.012 This field MUST advertise the length in bytes of the _Supported_ _Keys_ _Bit_ _Mask_ field carried in the
command.

CC:0063.02.07.11.013 This field MUST be set to the minimum value which allows advertising all supported ASCII codes.


**Supported** **Keys** **Bit** **Mask** **(L** **bytes)**

This field describes the supported keys that can be input on the keypad by end users. The length of
CC:0063.02.07.11.014 this field in bytes MUST match the value advertised in the _Supported_ _Keys_ _Bit_ _Mask_ _Length_ field.

CC:0063.02.07.11.015 This field MUST advertise the ASCII codes that represent the supported keys.


      - Bit 0 in Bit Mask 1 represents ASCII code 0

      - Bit 1 in Bit Mask 1 represents ASCII code 1.


      - …


      - Bit 7 in Bit Mask 16 represents ASCII code 127


CC:0063.02.07.11.016 If an ASCII code is supported, the corresponding bit MUST be set to ‘1’.


If an ASCII code is not supported, the corresponding bit MUST be set to ‘0’.


CC:0063.02.07.11.017 All other bits are reserved and MUST be set to zero by a sending node. Reserved bits MUST be
ignored by a receiving node.


CC:0063.02.07.11.018 A supporting node MUST NOT advertise an ASCII code representing the “enter” button on the
keypad, but only ASCII codes that can be part of the user codes.


CC:0063.02.07.12.001 A supporting node SHOULD support the ASCII codes 0x30..0x39 (decimal digits 0..9).


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 523




<!-- PAGE 525 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.117.9** **User** **Code** **Keypad** **Mode** **Set** **Command**


This command is used to set the keypad mode at the receiving node.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|
|Command = USER_CODE_KEYPAD_MODE_SET (0x08)|Command = USER_CODE_KEYPAD_MODE_SET (0x08)|Command = USER_CODE_KEYPAD_MODE_SET (0x08)|Command = USER_CODE_KEYPAD_MODE_SET (0x08)|Command = USER_CODE_KEYPAD_MODE_SET (0x08)|Command = USER_CODE_KEYPAD_MODE_SET (0x08)|Command = USER_CODE_KEYPAD_MODE_SET (0x08)|Command = USER_CODE_KEYPAD_MODE_SET (0x08)|



**Keypad** **Mode** **(8** **bits)**

This field is used to set the keypad mode at the receiving node.

CC:0063.02.08.11.001 This field MUST be encoded according to Table 2.531.


CC:0063.02.08.11.002 A supporting node being set a keypad mode MUST respect the requirements associated to this mode
in Table 2.531. The requirements in Table 2.531 (keypad mode) MUST take precedence over the
requirements in Table 2.532 (user code statuses).

CC:0063.02.08.11.003 This command MUST be ignored by a receiving node if the specified keypad mode is not supported.



Table 2.531: User Code Keypad Mode Set::Keypad mode encoding










|Value|Description|Version|
|---|---|---|
|0x00|**Normal Mode**:<br>This mode MUST be the default mode. When the Normal mode is active, the<br>supporting node:<br>• MUST work normally with all defned User Codes according to Table<br>2.532<br>• MUST accept the Admin Code, if supported|1|
|0x01|**Vacation Mode**:<br>This mode is used to disable/switch of the User Code functionalities for normal<br>users. When the Vacation mode is active, the supporting node:<br>• MUST ignore all input of assigned User Code (i.e. with Status ID difer-<br>ent than 0x00 **Available**)<br>• MUST react according to Table 2.532 when being input unknown codes<br>(i.e. with Status ID 0x00 **Available**).<br>• MUST accept the Admin Code, if supported|2|
|0x02|**Privacy Mode**:<br>This mode is used to completely disable/switch of the User Code functionali-<br>ties.<br>When the Privacy mode is active, the supporting node:<br>• MUST ignore any keypad input<br>• MUST ignore the Admin Code, if supported<br>This mode can be used e.g. to disallow User Code keypad use completely or<br>to rely only on Entry Control Notifcations, if supported.|2|
|0x03|**Locked Out Mode**:<br>This mode is used as a security measure to prevent brute force attacks. This<br>mode is normally activated by the supporting node itself. If the node activates<br>the Locked Out mode, it MUST issue a User Code Keypad Mode Report<br>Command to the Lifeline destination.<br>When the Locked Out mode is active, the supporting node:<br>• MUST ignore any keypad input<br>• MUST ignore the Admin Code, if supported.<br>A supporting node MUST return to the last active mode automatically after<br>a defned timeout if it activated this mode.<br>A controlling node may unlock the keypad again by issuing this command with<br>a diferent mode.|2|



CC:0063.02.08.11.004



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 524




<!-- PAGE 526 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.


**2.2.117.10** **User** **Code** **Keypad** **Mode** **Get** **Command**


This command is used to request a node about its current keypad mode.


CC:0063.02.09.11.001 The User Code Keypad Mode Report Command MUST be returned in response to this command.


CC:0063.02.09.11.002 This command MUST NOT be issued via multicast addressing.


CC:0063.02.09.11.003 A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|
|Command = USER_CODE_KEYPAD_MODE_GET (0x09)|Command = USER_CODE_KEYPAD_MODE_GET (0x09)|Command = USER_CODE_KEYPAD_MODE_GET (0x09)|Command = USER_CODE_KEYPAD_MODE_GET (0x09)|Command = USER_CODE_KEYPAD_MODE_GET (0x09)|Command = USER_CODE_KEYPAD_MODE_GET (0x09)|Command = USER_CODE_KEYPAD_MODE_GET (0x09)|Command = USER_CODE_KEYPAD_MODE_GET (0x09)|



**2.2.117.11** **User** **Code** **Keypad** **Mode** **Report** **Command**


This command is used by a node to advertise its current keypad mode.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|
|Command = USER_CODE_KEYPAD_MODE_REPORT (0x0A)|Command = USER_CODE_KEYPAD_MODE_REPORT (0x0A)|Command = USER_CODE_KEYPAD_MODE_REPORT (0x0A)|Command = USER_CODE_KEYPAD_MODE_REPORT (0x0A)|Command = USER_CODE_KEYPAD_MODE_REPORT (0x0A)|Command = USER_CODE_KEYPAD_MODE_REPORT (0x0A)|Command = USER_CODE_KEYPAD_MODE_REPORT (0x0A)|Command = USER_CODE_KEYPAD_MODE_REPORT (0x0A)|
|Keypad Mode|Keypad Mode|Keypad Mode|Keypad Mode|Keypad Mode|Keypad Mode|Keypad Mode|Keypad Mode|



**Keypad** **Mode** **(8** **bits)**

This field is used to advertise the keypad mode currently active at the sending node.

CC:0063.02.0A.11.001 This field MUST be encoded according to Table 2.531.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 525




<!-- PAGE 527 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.117.12** **Extended** **User** **Code** **Set** **Command**


This command is used to set one or more User Codes in the receiving node.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|
|Command = EXTENDED_USER_CODE_SET (0x0B)|Command = EXTENDED_USER_CODE_SET (0x0B)|Command = EXTENDED_USER_CODE_SET (0x0B)|Command = EXTENDED_USER_CODE_SET (0x0B)|Command = EXTENDED_USER_CODE_SET (0x0B)|Command = EXTENDED_USER_CODE_SET (0x0B)|Command = EXTENDED_USER_CODE_SET (0x0B)|Command = EXTENDED_USER_CODE_SET (0x0B)|
|Number of User Codes<br>|Number of User Codes<br>|Number of User Codes<br>|Number of User Codes<br>|Number of User Codes<br>|Number of User Codes<br>|Number of User Codes<br>|Number of User Codes<br>|
|User Identifer 1 (MSB) 1<br>|User Identifer 1 (MSB) 1<br>|User Identifer 1 (MSB) 1<br>|User Identifer 1 (MSB) 1<br>|User Identifer 1 (MSB) 1<br>|User Identifer 1 (MSB) 1<br>|User Identifer 1 (MSB) 1<br>|User Identifer 1 (MSB) 1<br>|
|User Identifer 2 (LSB) 2|User Identifer 2 (LSB) 2|User Identifer 2 (LSB) 2|User Identifer 2 (LSB) 2|User Identifer 2 (LSB) 2|User Identifer 2 (LSB) 2|User Identifer 2 (LSB) 2|User Identifer 2 (LSB) 2|
|User ID Status 1|User ID Status 1|User ID Status 1|User ID Status 1|User ID Status 1|User ID Status 1|User ID Status 1|User ID Status 1|
|Reserved|Reserved|Reserved|Reserved|User Code Length 1|User Code Length 1|User Code Length 1|User Code Length 1|
|User Code 1, 1|User Code 1, 1|User Code 1, 1|User Code 1, 1|User Code 1, 1|User Code 1, 1|User Code 1, 1|User Code 1, 1|
|…|…|…|…|…|…|…|…|
|User Code N, 1|User Code N, 1|User Code N, 1|User Code N, 1|User Code N, 1|User Code N, 1|User Code N, 1|User Code N, 1|
|…<br>|…<br>|…<br>|…<br>|…<br>|…<br>|…<br>|…<br>|
|User Identifer 1 (MSB) M<br>|User Identifer 1 (MSB) M<br>|User Identifer 1 (MSB) M<br>|User Identifer 1 (MSB) M<br>|User Identifer 1 (MSB) M<br>|User Identifer 1 (MSB) M<br>|User Identifer 1 (MSB) M<br>|User Identifer 1 (MSB) M<br>|
|User Identifer 2 (LSB) M|User Identifer 2 (LSB) M|User Identifer 2 (LSB) M|User Identifer 2 (LSB) M|User Identifer 2 (LSB) M|User Identifer 2 (LSB) M|User Identifer 2 (LSB) M|User Identifer 2 (LSB) M|
|User ID Status M|User ID Status M|User ID Status M|User ID Status M|User ID Status M|User ID Status M|User ID Status M|User ID Status M|
|Reserved|Reserved|Reserved|Reserved|User Code Length M|User Code Length M|User Code Length M|User Code Length M|
|User Code 1, M|User Code 1, M|User Code 1, M|User Code 1, M|User Code 1, M|User Code 1, M|User Code 1, M|User Code 1, M|
|…|…|…|…|…|…|…|…|
|User Code N, M|User Code N, M|User Code N, M|User Code N, M|User Code N, M|User Code N, M|User Code N, M|User Code N, M|



**Number** **of** **User** **Codes** **(8** **bits)**

This field is used to specify how many user codes blocks are contained in the actual command.

CC:0063.02.0B.11.001 This field MUST be in the range 1..255. A node MUST respect the Z-Wave MAC frame size or
Transport service limits when sending this command, which means in most cases that this field
SHOULD NOT be set to a value higher than 10.

CC:0063.02.0B.11.002 This field MUST be ignored and considered as set to 1 by a receiving node if it advertises no support
for Multiple User Code Set (MUCS) in the User Code Capabilities Report Command

CC:0063.02.0B.11.003 The number of User Code blocks contained in the command MUST be according to this field. A User
Code block MUST comprise the following fields:

      - User Identifier


      - User ID Status


      - User Code Length


      - User Code

**User** **Identifier** **(16** **bits)**

This field is used to specify the User Identifier for the actual User Code block.

CC:0063.02.0B.11.004 The first byte MUST carry the most significant byte of the 16-bit value.


CC:0063.02.0B.11.005 The value 0 MUST indicate that the receiving node MUST set the User Code and User Status for
all supported User Identifiers. The value 0 SHOULD be used only with User ID Status set to 0x00
(erasing all User Codes).

CC:0063.02.0B.11.006 If a non-existing User Identifier (higher than the advertised supported users number in the Users
Number Report Command) is specified in this command, a receiving node MUST ignore the actual
User Code block


**User** **ID** **Status** **(8** **bits)**


CC:0063.02.0B.11.00E


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 526




<!-- PAGE 528 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


The User ID Status field indicates the state of the User Identifier for the actual User Code block. This
field MUST comply with Table 2.532, however the requirements in Table 2.531 MUST take precedence
over the requirements in Table 2.532.

CC:0063.02.0B.11.008 If a non-supported User ID Status is specified, a receiving node MUST ignore the actual User Code
block.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 527




<!-- PAGE 529 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024







|Value|Table 2.532: Extended User Code Set::User ID Status encoding Description|Version|
|---|---|---|
|Value|Description|Version|
|0x00|**Available**:<br>The database entry represented by this User Identifer is not in use.<br>This status MUST be used to delete codes or indicate that an identifer is not<br>assigned.<br>When a user enters an unassigned/unknown code, the node:<br>• MUST indicate that the code is not accepted<br>• MUST NOT grant access to this user<br>• SHOULD take preventive actions for further attempts to enter User ID<br>and/or User Code (refer to Section 2.2.117.4)|1|
|0x01|**Enabled/Grant Access**:<br>The database entry represented by this User Identifer is in use and enabled.<br>When a user enters a code with this status, the node:<br>• MUST indicate that the code is accepted<br>• MUST grant access to the user<br>• MUST secure the Door Lock again after a timeout (either confgured if<br>set in Timed Operation or pre-defned if the Door Lock is set in Constant<br>Operation)|1|
|0x02|**Disabled**:<br>The database entry represented by this User Identifer is in use but disabled.<br>E.g. it allows a controller to push User Codes to a supporting node and let<br>these codes be subsequently activated by a local interface.<br>When a user enters a code with this status, the node:<br>• MUST indicate that the code is not accepted<br>• MUST NOT grant access to the user|1|
|0x03|**Messaging**:<br>The database entry represented by this User Identifer is in use.<br>The value is used to relay notifcations to a controlling application.<br>E.g. A user may enter a messaging code for notifying that maintenance started<br>or an application should activate the alarm system.<br>When a user enters a code with this status, the node:<br>• SHOULD indicate that the code is accepted<br>• MUST NOT grant access to this user<br>• MUST NOT take preventive actions for further attempts to enter User<br>ID and/or User Code (refer to Section 2.2.117.4)|2|
|0x04|**Passage Mode**:<br>The database entry represented by this User Identifer is in use.<br>The value is used to let the Door Lock permanently grant access.<br>Passage Mode can be activated and deactivated using the Door Lock Operation<br>Set (Unsecured without timeout/Secured) or via Passage Mode User Code<br>input.<br>E.g. A receptionist comes in the morning and enters a Passage Mode User<br>Code to allow anybody to subsequently enter the premises without entering a<br>code until Passage Mode is deactivated again.<br>When a user enters a code with this status, the node:<br>• MUST indicate that the code is accepted<br>• MUST toggle the Door Lock operation state between secured and unse-<br>cured without timeout (and also disable any auto-relock functionality)<br>If the node supports the Door Lock Command Class, it:<br>• MUST send a Door Lock Operation Report and Door Lock Confguration<br>Report via the Lifeline Association Group to advertise the new Door Lock<br>state|2|


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 528




<!-- PAGE 530 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.


**Reserved**

CC:0063.02.0B.11.009 This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**User** **Code** **Length** **(4** **bits)**

This field is used to advertise the length in bytes of the corresponding User Code field in the actual
User Code block.

CC:0063.02.0B.11.00A The User Code Length MUST be in the range 4..10 if the User ID Status is different than 0x00.


The User Code Length MUST be set to 0 if the User ID Status is set to 0x00.


**User** **Code** **(N** **bytes)**

This field is used to advertise the User Code to be set for the User ID for the actual User Code block.

CC:0063.02.0B.11.00B The length of this field in bytes MUST be according to the corresponding User Code Length field
value. If the User Code Length is set to 0, this field MUST be omitted.

CC:0063.02.0B.11.00C Each byte in this field MUST be encoded with ASCII representation.


CC:0063.02.0B.11.00D A supporting node receiving a non-supported ASCII character MUST ignore the actual User Code
block.


A supporting node receiving a User Code identical to one already set to another User ID or identical
to the Admin Code MUST ignore the actual User Code block.


**2.2.117.13** **Extended** **User** **Code** **Get** **Command**


This command is used to request the User Code of a specific User Identifier.


CC:0063.02.0C.11.001 The Extended User Code Report Command MUST be returned in response to this command


CC:0063.02.0C.11.002 This command MUST NOT be issued via multicast addressing.


CC:0063.02.0C.11.003 A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.








|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|
|Command = EXTENDED_USER_CODE_GET (0x0C)<br>|Command = EXTENDED_USER_CODE_GET (0x0C)<br>|Command = EXTENDED_USER_CODE_GET (0x0C)<br>|Command = EXTENDED_USER_CODE_GET (0x0C)<br>|Command = EXTENDED_USER_CODE_GET (0x0C)<br>|Command = EXTENDED_USER_CODE_GET (0x0C)<br>|Command = EXTENDED_USER_CODE_GET (0x0C)<br>|Command = EXTENDED_USER_CODE_GET (0x0C)<br>|
|User Identifer 1 (MSB)<br>|User Identifer 1 (MSB)<br>|User Identifer 1 (MSB)<br>|User Identifer 1 (MSB)<br>|User Identifer 1 (MSB)<br>|User Identifer 1 (MSB)<br>|User Identifer 1 (MSB)<br>|User Identifer 1 (MSB)<br>|
|User Identifer 2 (LSB)|User Identifer 2 (LSB)|User Identifer 2 (LSB)|User Identifer 2 (LSB)|User Identifer 2 (LSB)|User Identifer 2 (LSB)|User Identifer 2 (LSB)|User Identifer 2 (LSB)|
|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Report more|



**User** **Identifier** **(16** **bits)**

This field is used to specify the requested User Identifier.

CC:0063.02.0C.11.004 The first byte MUST carry the most significant byte of the 16 bit value.

This field MUST NOT be set to 0.

CC:0063.02.0C.11.005 A supporting node MUST return this value in the first User Code block of the returned Extended
User Code Report Command.

If a non-existing User Identifier (higher than the advertised supported users number in the Users NumCC:0063.02.0C.11.006 ber Report Command) is specified in this command, a responding node MUST return an Extended
User Code Report Command with the User ID Status set to 0xFE: “Status not available”.


**Report** **more** **(1** **bit)**


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 529




<!-- PAGE 531 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


This field is used to instruct the receiving node to report as many User Codes as possible within a
single Z-Wave command (that fits in a single Z-Wave frame) because the sending node intends to read
the whole (or a large part of the) User Code database.

CC:0063.02.0C.11.007 This field MUST be ignored by a receiving node if it advertises no support for Multiple User Code
Report (MUCR) in the User Code Capabilities Report Command.

CC:0063.02.0C.11.008 The value 0 MUST indicate to return a report for the requested User Identifier only.

The value 1 MUST indicate to return a report for the requested User Identifier and additionally report
as many User Identifiers as possible in the response.

When this field is set to 1, a node advertising support for Multiple User Code Report (MUCR) in the
User Code Capabilities Report Command:


CC:0063.02.0C.11.009 - MUST return at least 2 User Code blocks in the Extended User Code Report Command unless
the last used User Identifier or a non-supported User Identifier is requested.


CC:0063.02.0C.12.001 - SHOULD return as many User Code blocks as possible.


CC:0063.02.0C.11.00A Subsequent User Code blocks MUST contain consecutive User Identifier having a User ID Status
different than 0. For example, a node supporting 4 User IDs that are set as follow MUST report
User Identifier 1, 3, and 4 when requested about User Identifier 1:


**–** User ID 1, status 0


**–** User ID 2, status 0


**–** User ID 3, status 1, code 38473


**–** User ID 4, status 4, code 9277


**2.2.117.14** **Extended** **User** **Code** **Report** **Command**


This command is used to advertise the User Code of a specific User Identifier.


|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|
|Command = EXTENDED_USER_CODE_REPORT (0x0D)|Command = EXTENDED_USER_CODE_REPORT (0x0D)|Command = EXTENDED_USER_CODE_REPORT (0x0D)|Command = EXTENDED_USER_CODE_REPORT (0x0D)|Command = EXTENDED_USER_CODE_REPORT (0x0D)|Command = EXTENDED_USER_CODE_REPORT (0x0D)|Command = EXTENDED_USER_CODE_REPORT (0x0D)|Command = EXTENDED_USER_CODE_REPORT (0x0D)|
|Number of User Codes<br>|Number of User Codes<br>|Number of User Codes<br>|Number of User Codes<br>|Number of User Codes<br>|Number of User Codes<br>|Number of User Codes<br>|Number of User Codes<br>|
|User Identifer 1 (MSB) 1<br>|User Identifer 1 (MSB) 1<br>|User Identifer 1 (MSB) 1<br>|User Identifer 1 (MSB) 1<br>|User Identifer 1 (MSB) 1<br>|User Identifer 1 (MSB) 1<br>|User Identifer 1 (MSB) 1<br>|User Identifer 1 (MSB) 1<br>|
|User Identifer 2 (LSB) 1|User Identifer 2 (LSB) 1|User Identifer 2 (LSB) 1|User Identifer 2 (LSB) 1|User Identifer 2 (LSB) 1|User Identifer 2 (LSB) 1|User Identifer 2 (LSB) 1|User Identifer 2 (LSB) 1|
|User ID Status 1|User ID Status 1|User ID Status 1|User ID Status 1|User ID Status 1|User ID Status 1|User ID Status 1|User ID Status 1|
|Reserved|Reserved|Reserved|Reserved|User Code Length 1|User Code Length 1|User Code Length 1|User Code Length 1|
|User Code 1, 1|User Code 1, 1|User Code 1, 1|User Code 1, 1|User Code 1, 1|User Code 1, 1|User Code 1, 1|User Code 1, 1|
|…|…|…|…|…|…|…|…|
|User Code N, 1|User Code N, 1|User Code N, 1|User Code N, 1|User Code N, 1|User Code N, 1|User Code N, 1|User Code N, 1|
|…<br>|…<br>|…<br>|…<br>|…<br>|…<br>|…<br>|…<br>|
|User Identifer 1 (MSB) M<br>|User Identifer 1 (MSB) M<br>|User Identifer 1 (MSB) M<br>|User Identifer 1 (MSB) M<br>|User Identifer 1 (MSB) M<br>|User Identifer 1 (MSB) M<br>|User Identifer 1 (MSB) M<br>|User Identifer 1 (MSB) M<br>|
|User Identifer 2 (LSB) M|User Identifer 2 (LSB) M|User Identifer 2 (LSB) M|User Identifer 2 (LSB) M|User Identifer 2 (LSB) M|User Identifer 2 (LSB) M|User Identifer 2 (LSB) M|User Identifer 2 (LSB) M|
|User ID Status M|User ID Status M|User ID Status M|User ID Status M|User ID Status M|User ID Status M|User ID Status M|User ID Status M|
|Reserved|Reserved|Reserved|Reserved|User Code Length M|User Code Length M|User Code Length M|User Code Length M|
|User Code 1, M|User Code 1, M|User Code 1, M|User Code 1, M|User Code 1, M|User Code 1, M|User Code 1, M|User Code 1, M|
|…|…|…|…|…|…|…|…|
|User Code N, M<br>|User Code N, M<br>|User Code N, M<br>|User Code N, M<br>|User Code N, M<br>|User Code N, M<br>|User Code N, M<br>|User Code N, M<br>|
|Next User Identifer 1 (MSB)<br>|Next User Identifer 1 (MSB)<br>|Next User Identifer 1 (MSB)<br>|Next User Identifer 1 (MSB)<br>|Next User Identifer 1 (MSB)<br>|Next User Identifer 1 (MSB)<br>|Next User Identifer 1 (MSB)<br>|Next User Identifer 1 (MSB)<br>|
|Next User Identifer 2 (LSB)|Next User Identifer 2 (LSB)|Next User Identifer 2 (LSB)|Next User Identifer 2 (LSB)|Next User Identifer 2 (LSB)|Next User Identifer 2 (LSB)|Next User Identifer 2 (LSB)|Next User Identifer 2 (LSB)|



CC:0063.02.0D.11.001



**Number** **of** **User** **Codes** **(8** **bits)**

This field is used to specify how many user codes blocks are contained in the actual command.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 530




<!-- PAGE 532 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


This field MUST be in the range 1..255. A node MUST respect the Z-Wave MAC frame size or
Transport service limits when sending this command, which means in most cases that this field
SHOULD NOT be set to a value higher than 8.

CC:0063.02.0D.11.002 The number of User Code blocks contained in the command MUST be according to this field. A User
Code block MUST comprise the following fields:

      - User Identifier


      - User ID Status


      - User Code Length


      - User Code


CC:0063.02.0D.11.003
This field MUST be set to 1 by a node advertising no support for Multiple User Code Report (MUCR)
in the User Code Capabilities Report Command.

**User** **Identifier** **(16** **bits)**

This field is used to specify the actual User Identifier for the actual User Code block.

CC:0063.02.0D.11.004 The first byte MUST carry the most significant byte of the 16-bit value.


**User** **ID** **Status** **(8** **bits)**

CC:0063.02.0D.11.005 This field indicates the state of the User Identifier for the actual User Code block. This field MUST
comply with Table 2.533.


Table 2.533: Extended User Code Report::User ID Status Encoding

|Value|Description|Version|
|---|---|---|
|0x00|**Available**. Refer to Table 2.532.|1|
|0x01|**Enabled/Grant Access**. Refer to Table 2.532.|1|
|0x02|**Disabled**. Refer to Table 2.532.|1|
|0x03|**Messaging**. Refer to Table 2.532.|2|
|0x04|**Passage Mode**. Table 2.532.|2|
|0xFE|**Status not available**.<br>The requested User Identifer is not valid (either 0 or higher than the supported<br>users number in the Users Number Report Command)|1|



CC:0063.02.0D.11.006 All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.


**User** **Code** **Length** **(4** **bits)**

This field is used to advertise the length in bytes of the User Code field in the actual User Code block.

CC:0063.02.0D.11.007 The User Code Length MUST be in the range 4..10 if the User ID Status is different than 0x00 and
0xFE.


The User Code Length MUST be set to 0 if the User ID Status is 0x00 or 0xFE.


**User** **Code** **(N** **bytes)**

This field is used to advertise the User Code currently set for the User ID in the actual User Code
block.

CC:0063.02.0D.11.008 The length of this field in bytes MUST be according to the corresponding User Code Length field
value. If the User Code Length is set to 0, this field MUST be omitted.

CC:0063.02.0D.11.009 Each byte in this field MUST be encoded with ASCII representation.

**Next** **User** **Identifier** **(16** **bits)**

This field is used to specify the next User Identifier in use in the User Code database after the User
Identifier advertised in the last User Code block.


CC:0063.02.0D.11.00A


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 531




<!-- PAGE 533 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


This field MUST be set to the next User Identifier having a User ID Status different than 0. The first
byte MUST carry the most significant byte of the 16-bit value.

CC:0063.02.0D.11.00B The value 0 MUST indicate that the actual User Identifier is the last set at the sending node.


CC:0063.02.0D.11.00C
If the status field is set to 0xFE for the last User Code block (User Identifier higher than the advertised
supported users number in the Users Number Report Command), this field MUST be set to 0.


**2.2.117.15** **Admin** **Code** **Set** **Command**


This command is used to set the Admin Code in the receiving node.


CC:0063.02.0E.11.001 This command MUST be ignored by a receiving node advertising no support for the Admin Code
functionality (MD Support) in the User Code Capabilities Report Command.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|
|Command = ADMIN_CODE_SET (0x0E)|Command = ADMIN_CODE_SET (0x0E)|Command = ADMIN_CODE_SET (0x0E)|Command = ADMIN_CODE_SET (0x0E)|Command = ADMIN_CODE_SET (0x0E)|Command = ADMIN_CODE_SET (0x0E)|Command = ADMIN_CODE_SET (0x0E)|Command = ADMIN_CODE_SET (0x0E)|
|Reserved|Reserved|Reserved|Reserved|Admin Code Length|Admin Code Length|Admin Code Length|Admin Code Length|
|Admin Code 1|Admin Code 1|Admin Code 1|Admin Code 1|Admin Code 1|Admin Code 1|Admin Code 1|Admin Code 1|
|…|…|…|…|…|…|…|…|
|Admin Code N|Admin Code N|Admin Code N|Admin Code N|Admin Code N|Admin Code N|Admin Code N|Admin Code N|



**Reserved**

CC:0063.02.0E.11.002 This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**Admin** **Code** **Length** **(4** **bits)**

This field is used to advertise the length in bytes of the Admin Code field in the command.

CC:0063.02.0E.11.003 This field MUST be set to 0 or in the range 4..10.


CC:0063.02.0E.11.004 Values in the range 4..10 MUST indicate that the receiving node MUST set the Admin Code as
indicated in the Admin Code field.


CC:0063.02.0E.11.005 The Value 0 MUST indicate that the receiving node MUST deactivate the Admin Code.

If this field is set to 0, this command MUST be ignored by a receiving node if it advertises no support
for Admin Code Deactivation (ACD) in the User Code Capabilities Report Command.


**Admin** **Code** **(N** **bytes)**

This field is used to advertise the Admin Code to be set for the node.

CC:0063.02.0E.11.006 The length of this field MUST be according to the Admin Code Length field value.

Each byte in this field MUST be encoded with ASCII representation.


CC:0063.02.0E.11.007 A supporting node receiving a non-supported ASCII character MUST ignore the command.


A supporting node receiving a Admin Code identical to one already set to another User ID MAY
ignore the command.


When the Admin Code is input, the node:


CC:0063.02.0E.11.008 - MUST indicate that the code is accepted


CC:0063.02.0E.11.009 - MUST grant access to administrator functionalities, such as the network settings and/or User
Code management interface.


Requirements in Table 2.531 (keypad modes) MUST take precedence over the above Admin Code
requirements.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 532




<!-- PAGE 534 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.117.16** **Admin** **Code** **Get** **Command**


This command is used to request the Admin Code currently set at the receiving node.


CC:0063.02.0F.11.001 The Admin Code Report Command MUST be returned in response to this command


CC:0063.02.0F.11.002 This command MUST NOT be issued via multicast addressing.


CC:0063.02.0F.11.003 A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|
|Command = ADMIN_CODE_GET (0x0F)|Command = ADMIN_CODE_GET (0x0F)|Command = ADMIN_CODE_GET (0x0F)|Command = ADMIN_CODE_GET (0x0F)|Command = ADMIN_CODE_GET (0x0F)|Command = ADMIN_CODE_GET (0x0F)|Command = ADMIN_CODE_GET (0x0F)|Command = ADMIN_CODE_GET (0x0F)|



**2.2.117.17** **Admin** **Code** **Report** **Command**


This command is used to advertise the Admin Code currently set at the sending node.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|
|Command = ADMIN_CODE_REPORT (0x10)|Command = ADMIN_CODE_REPORT (0x10)|Command = ADMIN_CODE_REPORT (0x10)|Command = ADMIN_CODE_REPORT (0x10)|Command = ADMIN_CODE_REPORT (0x10)|Command = ADMIN_CODE_REPORT (0x10)|Command = ADMIN_CODE_REPORT (0x10)|Command = ADMIN_CODE_REPORT (0x10)|
|Reserved|Reserved|Reserved|Reserved|Admin Code Length|Admin Code Length|Admin Code Length|Admin Code Length|
|Admin Code 1|Admin Code 1|Admin Code 1|Admin Code 1|Admin Code 1|Admin Code 1|Admin Code 1|Admin Code 1|
|…|…|…|…|…|…|…|…|
|Admin Code N|Admin Code N|Admin Code N|Admin Code N|Admin Code N|Admin Code N|Admin Code N|Admin Code N|



**Reserved**

CC:0063.02.10.11.001 This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**Admin** **Code** **Length** **(4** **bits)**

This field is used to advertise the length in bytes of the Admin Code field in the command.

CC:0063.02.10.11.002 This field MUST be in the range 4..10 if the Admin Code is set and advertised in this command.

CC:0063.02.10.11.003 This field MUST be set to 0 if the Admin Code is deactivated or if the sending node advertises
no support for the Admin Code functionality (AC Support) in the User Code Capabilities Report
Command.


**Admin** **Code** **(N** **bytes)**

This field is used to advertise the Admin Code currently set at the sending node.

CC:0063.02.10.11.004 The length of this field MUST be according to the Admin Code Length field value. If the Admin
Code Length is set to 0, this field MUST be omitted.

CC:0063.02.10.11.005 Each byte in this field MUST be encoded with ASCII representation.


**2.2.117.18** **User** **Code** **Checksum** **Get** **Command**


This command is used to request a User Code checksum representing all the User Codes currently set
at the receiving node.


CC:0063.02.11.11.001 This command MUST be ignored by a node advertising no support for the User Code Checksum
functionality (UCC Support) in the User Code Capabilities Report Command.


CC:0063.02.11.11.002


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 533




<!-- PAGE 535 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


The User Code Checksum Report Command MUST be returned in response to this command if
the User Code Checksum functionality (UCC Support) is advertised as supported in the User Code
Capabilities Report Command.


CC:0063.02.11.11.003 This command MUST NOT be issued via multicast addressing.


CC:0063.02.11.11.004 A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|
|Command = USER_CODE_CHECKSUM_GET (0x11)|Command = USER_CODE_CHECKSUM_GET (0x11)|Command = USER_CODE_CHECKSUM_GET (0x11)|Command = USER_CODE_CHECKSUM_GET (0x11)|Command = USER_CODE_CHECKSUM_GET (0x11)|Command = USER_CODE_CHECKSUM_GET (0x11)|Command = USER_CODE_CHECKSUM_GET (0x11)|Command = USER_CODE_CHECKSUM_GET (0x11)|



**2.2.117.19** **User** **Code** **Checksum** **Report** **Command**


This command is used to advertise the current User Code checksum representing all the User codes
set at the sending node.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|Command Class = COMMAND_CLASS_USER_CODE (0x63)|
|Command = USER_CODE_CHECKSUM_REPORT (0x12)|Command = USER_CODE_CHECKSUM_REPORT (0x12)|Command = USER_CODE_CHECKSUM_REPORT (0x12)|Command = USER_CODE_CHECKSUM_REPORT (0x12)|Command = USER_CODE_CHECKSUM_REPORT (0x12)|Command = USER_CODE_CHECKSUM_REPORT (0x12)|Command = USER_CODE_CHECKSUM_REPORT (0x12)|Command = USER_CODE_CHECKSUM_REPORT (0x12)|
|User Code Checksum 1 (MSB)|User Code Checksum 1 (MSB)|User Code Checksum 1 (MSB)|User Code Checksum 1 (MSB)|User Code Checksum 1 (MSB)|User Code Checksum 1 (MSB)|User Code Checksum 1 (MSB)|User Code Checksum 1 (MSB)|
|User Code Checksum 2 (LSB)|User Code Checksum 2 (LSB)|User Code Checksum 2 (LSB)|User Code Checksum 2 (LSB)|User Code Checksum 2 (LSB)|User Code Checksum 2 (LSB)|User Code Checksum 2 (LSB)|User Code Checksum 2 (LSB)|



**User** **Code** **Checksum** **(16** **bits)**

This field is used to advertise the checksum representing all User Codes set at the sending node.


CC:0063.02.12.11.001 The checksum MUST be calculated using the CRC-CCITT polynomium using initialization value
equal to 0x1D0F and 0x1021 (normal representation). Refer to _CRC-CCITT_ _Source_ _Code_ for details.

CC:0063.02.12.11.002 This field MUST be set to 0x0000 if no User Code is set at node.

CC:0063.02.12.11.003 The checksum data MUST be built by concatenating defined User Codes data (with User ID Status
different than 0) in the ascending User ID order. The Admin Code MUST NOT be part of the
checksum calculation.

CC:0063.02.12.11.004 Each defined User Code data MUST be formatted as follows:


User ID (16 bits) | User ID Status (8 bits) | User Code (4..10 bytes)


For example, a node supporting 4 User IDs that are set as follow:


      - User ID 1, status 4, code 9277


      - User ID 2, status 0


      - User ID 3, status 1, code 88473


      - User ID 4, status 0


CC:0063.02.12.11.005 In this case, User Code data for User ID 1 and 3 MUST be concatenated to obtain the checksum data:


0x0001 | 0x04 | 0x39 32 37 37 | 0x0003 | 0x01 | 0x38 38 34 37 33


CC:0063.02.12.11.006 The checksum data MUST be: 0x000104393237370003013838343733.

The returned User Code Checksum field MUST be set to: 0xEAAD.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 534