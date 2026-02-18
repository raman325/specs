<!-- PAGE 454 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.94** **Screen** **Attributes** **Command** **Class,** **version** **1**


The Screen Attribute Command Class is used to retrieve screen attributes from the device hosting
the screen. This allows another device to send data formatted according to the screen attributes to
the device hosting the screen. The screen may be located on any device in the network.


**2.2.94.1** **Screen** **Attributes** **Get** **Command**


This command is used to request the screen attributes.


The Screen Attributes Report Command MUST be returned in response to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SCREEN_ATTRIBUTES|Command Class = COMMAND_CLASS_SCREEN_ATTRIBUTES|Command Class = COMMAND_CLASS_SCREEN_ATTRIBUTES|Command Class = COMMAND_CLASS_SCREEN_ATTRIBUTES|Command Class = COMMAND_CLASS_SCREEN_ATTRIBUTES|Command Class = COMMAND_CLASS_SCREEN_ATTRIBUTES|Command Class = COMMAND_CLASS_SCREEN_ATTRIBUTES|Command Class = COMMAND_CLASS_SCREEN_ATTRIBUTES|
|Command = SCREEN_ATTRIBUTES_GET|Command = SCREEN_ATTRIBUTES_GET|Command = SCREEN_ATTRIBUTES_GET|Command = SCREEN_ATTRIBUTES_GET|Command = SCREEN_ATTRIBUTES_GET|Command = SCREEN_ATTRIBUTES_GET|Command = SCREEN_ATTRIBUTES_GET|Command = SCREEN_ATTRIBUTES_GET|



**2.2.94.2** **Screen** **Attributes** **Report** **Command**


This command is used to advertise the screen attributes.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SCREEN_ATTRIBUTES|Command Class = COMMAND_CLASS_SCREEN_ATTRIBUTES|Command Class = COMMAND_CLASS_SCREEN_ATTRIBUTES|Command Class = COMMAND_CLASS_SCREEN_ATTRIBUTES|Command Class = COMMAND_CLASS_SCREEN_ATTRIBUTES|Command Class = COMMAND_CLASS_SCREEN_ATTRIBUTES|Command Class = COMMAND_CLASS_SCREEN_ATTRIBUTES|Command Class = COMMAND_CLASS_SCREEN_ATTRIBUTES|
|Command = SCREEN_ATTRIBUTES_REPORT|Command = SCREEN_ATTRIBUTES_REPORT|Command = SCREEN_ATTRIBUTES_REPORT|Command = SCREEN_ATTRIBUTES_REPORT|Command = SCREEN_ATTRIBUTES_REPORT|Command = SCREEN_ATTRIBUTES_REPORT|Command = SCREEN_ATTRIBUTES_REPORT|Command = SCREEN_ATTRIBUTES_REPORT|
|Reserved|Reserved|Reserved|Number of Lines|Number of Lines|Number of Lines|Number of Lines|Number of Lines|
|Characters per Line<br>|Characters per Line<br>|Characters per Line<br>|Characters per Line<br>|Characters per Line<br>|Characters per Line<br>|Characters per Line<br>|Characters per Line<br>|
|Line Bufer Size|Line Bufer Size|Line Bufer Size|Line Bufer Size|Line Bufer Size|Line Bufer Size|Line Bufer Size|Line Bufer Size|
|Character Encoding|Character Encoding|Character Encoding|Character Encoding|Character Encoding|Character Encoding|Character Encoding|Character Encoding|



**Reserved**

This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**Number** **of** **Lines** **(5** **bits)**


Number of lines the screen supports (1..16).


**Characters** **per** **Line** **(8** **bits)**


Number of characters the screen supports on each line (1..255).

**Line** **Buffer** **Size** **(8** **bits)**

Number of characters the line buffer supports for each line (1..255). Size of line buffer will always be
equal or larger than the number of visual characters per line. The text will typically scroll in case it
is larger than the number of visual characters.


**Character** **Encoding** **(8** **bits)**


The screen supports the following numerical representations of a character:


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 453




<!-- PAGE 455 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024

|Bit|Table 2.510: Screen Attributes Report::Character Encoding encod- ing Description|
|---|---|
|Bit<br>Map|Description|
|Bit 0|Supports ASCII codes if the bit is 1 and the opposite if 0. See _ASCII Codes_ (values<br>128-255 are ignored)|
|Bit 1|Supports ASCII codes and Extended ASCII codes if the bit is 1 and the opposite if 0.<br>See _ASCII Codes_.|
|Bit 2|Supports Unicode UTF-16 if the bit is 1 and the opposite if 0.<br>|
|Bit 3|Supports ASCII codes and Player codes, see _ASCII Codes_ (undefned values are ignored)|



All other bits are reserved and MUST be set to zero by a sending node. Reserved bits MUST be
ignored by a receiving node.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 454

---

<!-- PAGE 456 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.95** **Screen** **Attributes** **Command** **Class,** **version** **2**


The Screen Attribute Command Class, version 2 introduces the Screen Timeout of the Screen Attributes Command.


Details not mentioned remain the same as in version 1.


**2.2.95.1** **Screen** **Attributes** **Report** **Command**


This command is used to advertise the screen attributes.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SCREEN_ATTRIBUTES|Command Class = COMMAND_CLASS_SCREEN_ATTRIBUTES|Command Class = COMMAND_CLASS_SCREEN_ATTRIBUTES|Command Class = COMMAND_CLASS_SCREEN_ATTRIBUTES|Command Class = COMMAND_CLASS_SCREEN_ATTRIBUTES|Command Class = COMMAND_CLASS_SCREEN_ATTRIBUTES|Command Class = COMMAND_CLASS_SCREEN_ATTRIBUTES|Command Class = COMMAND_CLASS_SCREEN_ATTRIBUTES|
|Command = SCREEN_ATTRIBUTES_REPORT|Command = SCREEN_ATTRIBUTES_REPORT|Command = SCREEN_ATTRIBUTES_REPORT|Command = SCREEN_ATTRIBUTES_REPORT|Command = SCREEN_ATTRIBUTES_REPORT|Command = SCREEN_ATTRIBUTES_REPORT|Command = SCREEN_ATTRIBUTES_REPORT|Command = SCREEN_ATTRIBUTES_REPORT|
|Reserved|Reserved|Escape<br>Sequence|Number of Lines|Number of Lines|Number of Lines|Number of Lines|Number of Lines|
|Characters per Line<br>|Characters per Line<br>|Characters per Line<br>|Characters per Line<br>|Characters per Line<br>|Characters per Line<br>|Characters per Line<br>|Characters per Line<br>|
|Line Bufer Size|Line Bufer Size|Line Bufer Size|Line Bufer Size|Line Bufer Size|Line Bufer Size|Line Bufer Size|Line Bufer Size|
|Character Encoding|Character Encoding|Character Encoding|Character Encoding|Character Encoding|Character Encoding|Character Encoding|Character Encoding|
|Screen Timeout|Screen Timeout|Screen Timeout|Screen Timeout|Screen Timeout|Screen Timeout|Screen Timeout|Screen Timeout|



**Reserved**

This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**Escape** **Sequence** **(1** **bit)**


If set to 0, escape sequences are not supported by the device.


If set to 1, escape sequences are supported by the device.


**Number** **of** **Lines** **(5** **bits)**


Number of lines the screen supports (1..16).


**Characters** **per** **Line** **(8** **bits)**


Number of characters the screen supports on each line (1..255).

**Line** **Buffer** **Size** **(8** **bits)**

Number of characters the line buffer supports for each line (1..255). Size of line buffer will always be
equal or larger than the number of visual characters per line. The text will typically scroll in case it
is larger than the number of visual characters.


**Character** **Encoding** **(8** **bits)**

This field MUST be encoded according to Table 2.510.


All other bits are reserved and MUST be set to zero by a sending node. Reserved bits MUST be
ignored by a receiving node.


**Screen** **Timeout** **(8** **bits)**


If Screen Timeout is set to 0, the display is always on. A value larger than 0 MUST specify the display
timeout in seconds.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 455