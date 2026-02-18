<!-- PAGE 581 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024

## **3.2 Management Command Class Definitions**


The following subchapters contain definitions of Management Command Classes.


**3.2.1** **Application** **Capability** **Command** **Class,** **version** **1** **[OBSOLETED]**


**Warning:** **THIS** **COMMAND** **CLASS** **HAS** **BEEN** **OBSOLETED**


New implementations MUST NOT support this Command Class.


New implementations MUST use the Supervision Command Class to report support or no support
of a given Command Class. Refer to Section 4.


The Application Capability Command Class comprises commands for handling issues related to dynamic support for command classes.


Examples include nodes, which only support certain command classes when included securely, and
controllers that only support command classes for primary controllers when they are actually operating
as primary controllers.


The intention of the Application Capability Command Class is to provide tools for handling exceptions. Controlling nodes SHOULD maintain a local representation of supported command classes
by destination nodes rather than relying on destination nodes returning Application Capability messages. Destination nodes capable of returning Application Capability messages MUST list Application
Capability Command Class as supported only.


**3.2.1.1** **Not** **Supported** **Command** **Class** **Command**


The Not Supported Command Class Command is used by a node to indicate to a requesting node
that the requested command class is not supported. The offending command and command class are
encapsulated.


A node SHOULD use this command to indicate to other nodes that a command is not supported.


A node receiving this command SHOULD use the information to clean up internal states by requesting
up-to-date information on command class support from the sending node using Node Information
frame. This includes adjusting user interface details accordingly.


Table 3.1: Not Supported Command Class Command (one byte)

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_APPLICATION_CAPABILITY|Command Class = COMMAND_CLASS_APPLICATION_CAPABILITY|Command Class = COMMAND_CLASS_APPLICATION_CAPABILITY|Command Class = COMMAND_CLASS_APPLICATION_CAPABILITY|Command Class = COMMAND_CLASS_APPLICATION_CAPABILITY|Command Class = COMMAND_CLASS_APPLICATION_CAPABILITY|Command Class = COMMAND_CLASS_APPLICATION_CAPABILITY|Command Class = COMMAND_CLASS_APPLICATION_CAPABILITY|
|Command = COMMAND_COMMAND_CLASS_NOT_SUPPORTED|Command = COMMAND_COMMAND_CLASS_NOT_SUPPORTED|Command = COMMAND_COMMAND_CLASS_NOT_SUPPORTED|Command = COMMAND_COMMAND_CLASS_NOT_SUPPORTED|Command = COMMAND_COMMAND_CLASS_NOT_SUPPORTED|Command = COMMAND_COMMAND_CLASS_NOT_SUPPORTED|Command = COMMAND_COMMAND_CLASS_NOT_SUPPORTED|Command = COMMAND_COMMAND_CLASS_NOT_SUPPORTED|
|Dynamic|_Reserved_<br>|_Reserved_<br>|_Reserved_<br>|_Reserved_<br>|_Reserved_<br>|_Reserved_<br>|_Reserved_<br>|
|Ofending Command Class (0x20 – 0xEE)<br>|Ofending Command Class (0x20 – 0xEE)<br>|Ofending Command Class (0x20 – 0xEE)<br>|Ofending Command Class (0x20 – 0xEE)<br>|Ofending Command Class (0x20 – 0xEE)<br>|Ofending Command Class (0x20 – 0xEE)<br>|Ofending Command Class (0x20 – 0xEE)<br>|Ofending Command Class (0x20 – 0xEE)<br>|
|Ofending Command|Ofending Command|Ofending Command|Ofending Command|Ofending Command|Ofending Command|Ofending Command|Ofending Command|



Table 3.2: Not Supported Command Class Command (two bytes)








|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_APPLICATION_CAPABILITY|Command Class = COMMAND_CLASS_APPLICATION_CAPABILITY|Command Class = COMMAND_CLASS_APPLICATION_CAPABILITY|Command Class = COMMAND_CLASS_APPLICATION_CAPABILITY|Command Class = COMMAND_CLASS_APPLICATION_CAPABILITY|Command Class = COMMAND_CLASS_APPLICATION_CAPABILITY|Command Class = COMMAND_CLASS_APPLICATION_CAPABILITY|Command Class = COMMAND_CLASS_APPLICATION_CAPABILITY|
|Command = COMMAND_COMMAND_CLASS_NOT_SUPPORTED|Command = COMMAND_COMMAND_CLASS_NOT_SUPPORTED|Command = COMMAND_COMMAND_CLASS_NOT_SUPPORTED|Command = COMMAND_COMMAND_CLASS_NOT_SUPPORTED|Command = COMMAND_COMMAND_CLASS_NOT_SUPPORTED|Command = COMMAND_COMMAND_CLASS_NOT_SUPPORTED|Command = COMMAND_COMMAND_CLASS_NOT_SUPPORTED|Command = COMMAND_COMMAND_CLASS_NOT_SUPPORTED|
|Dynamic|_Reserved_<br>|_Reserved_<br>|_Reserved_<br>|_Reserved_<br>|_Reserved_<br>|_Reserved_<br>|_Reserved_<br>|
|Ofending Command Class MSB (0xF1 – 0xFF)<br>|Ofending Command Class MSB (0xF1 – 0xFF)<br>|Ofending Command Class MSB (0xF1 – 0xFF)<br>|Ofending Command Class MSB (0xF1 – 0xFF)<br>|Ofending Command Class MSB (0xF1 – 0xFF)<br>|Ofending Command Class MSB (0xF1 – 0xFF)<br>|Ofending Command Class MSB (0xF1 – 0xFF)<br>|Ofending Command Class MSB (0xF1 – 0xFF)<br>|
|Ofending Command Class LSB (0x00 – 0xFF)<br>|Ofending Command Class LSB (0x00 – 0xFF)<br>|Ofending Command Class LSB (0x00 – 0xFF)<br>|Ofending Command Class LSB (0x00 – 0xFF)<br>|Ofending Command Class LSB (0x00 – 0xFF)<br>|Ofending Command Class LSB (0x00 – 0xFF)<br>|Ofending Command Class LSB (0x00 – 0xFF)<br>|Ofending Command Class LSB (0x00 – 0xFF)<br>|
|Ofending Command|Ofending Command|Ofending Command|Ofending Command|Ofending Command|Ofending Command|Ofending Command|Ofending Command|



Payload data following the offending command is omitted.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 580




<!-- PAGE 582 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**Dynamic** **(1** **bit)**

If the “Dynamic” flag is set (‘1’), the sending node has been designed to support this command class
but the current operational conditions prevent the node from supporting this command class.


One example is the AddNode command used for network management. This command is only supported when a controller is operating as primary controller.

|Field|Table 3.3: Dynamic Bit Meaning|
|---|---|
|Field|Meaning|
|‘0’|Command not supported (Permanently)|
|‘1’|Dynamic support (Currently no support)|



**Reserved**

This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.

**Offending** **Command** **Class** **(1** **or** **2** **bytes)**

This field indicates the offending command class received by the destination node. The size of the
command class field depends on the value of the first byte.

**Offending** **Command** **(1** **byte)**

This field indicates the offending command received by the destination node.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 581