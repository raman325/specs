<!-- PAGE 702 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.23** **Grouping** **Name** **Command** **Class,** **version** **1** **[DEPRECATED]**


**Warning:** **THIS** **COMMAND** **HAS** **BEEN** **DEPRECATED**


A device MAY implement this command class, but it is RECOMMENDED that new implementations use the Association Group Information (AGI) Command Class for naming association

groups.


If implementing this command class, it is RECOMMENDED that the Association Group Information (AGI) Command Class is also implemented.


The Grouping Name Command Class is used to transfer name of groupings (as defined by the grouping
identifier in the Association Command Class).


**3.2.23.1** **Grouping** **Name** **Set** **Command**


The Grouping Name Set Command used to set a grouping Identifier name.


Table 3.101: Grouping Name Set Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_GROUPING_NAME|Command Class = COMMAND_CLASS_GROUPING_NAME|Command Class = COMMAND_CLASS_GROUPING_NAME|Command Class = COMMAND_CLASS_GROUPING_NAME|Command Class = COMMAND_CLASS_GROUPING_NAME|Command Class = COMMAND_CLASS_GROUPING_NAME|Command Class = COMMAND_CLASS_GROUPING_NAME|Command Class = COMMAND_CLASS_GROUPING_NAME|
|Command = GROUPING_NAME_SET<br>|Command = GROUPING_NAME_SET<br>|Command = GROUPING_NAME_SET<br>|Command = GROUPING_NAME_SET<br>|Command = GROUPING_NAME_SET<br>|Command = GROUPING_NAME_SET<br>|Command = GROUPING_NAME_SET<br>|Command = GROUPING_NAME_SET<br>|
|Grouping Identifer|Grouping Identifer|Grouping Identifer|Grouping Identifer|Grouping Identifer|Grouping Identifer|Grouping Identifer|Grouping Identifer|
|Reserved|Reserved|Reserved|Reserved|Reserved|Char. Presentation|Char. Presentation|Char. Presentation|
|Grouping Name 1|Grouping Name 1|Grouping Name 1|Grouping Name 1|Grouping Name 1|Grouping Name 1|Grouping Name 1|Grouping Name 1|
|…|…|…|…|…|…|…|…|
|Grouping Name N|Grouping Name N|Grouping Name N|Grouping Name N|Grouping Name N|Grouping Name N|Grouping Name N|Grouping Name N|



**Grouping** **Identifier** **(8** **bits)**

The field specifies the Grouping ID.


**Reserved**

This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**Char.** **Presentation** **(3** **bits)**

The char presentation identifier MAY be set to the following values:


Table 3.102: Grouping Name Set Command::Char Presentation

|Char Presentation<br>.|Description|
|---|---|
|0|Using standard ASCII codes, see _ASCII Codes_ (values 128-255 are ig-<br>nored)|
|1|Using<br>standard<br>and<br>OEM<br>Extended<br>ASCII<br>codes,<br>see<br>_ap-_<br>_pendix_ascii_codes_.|
|2|Unicode UTF-16|



**Note** : Devices supporting Unicode UTF-16 characters can have strings of a maximum of 8 characters
because each character is described by a 2 byte long decimal representation. The first byte is the most
significant byte. I.e. if there is one Unicode character in the set frame the char 1 will be MSB and
char 2 will be LSB of the Unicode character.


All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.


**Grouping** **Name** **(N** **bytes)**

Grouping name using specified character representation.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 701




<!-- PAGE 703 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


The Grouping name MAY have a maximum of 16 characters and a minimum of 0 characters. The
number of character fields transmitted MUST be determined from the frame length. If a frame with
more than 16 characters is received, the receiving node MUST ignore any characters following the
16th character.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 702




<!-- PAGE 704 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.23.2** **Grouping** **Name** **Get** **Command**


The Grouping Name Get Command is used to request a grouping Identifier name.


The Grouping Name Report Command MUST be returned in response to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 3.103: Grouping Name Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_GROUPING_NAME|Command Class = COMMAND_CLASS_GROUPING_NAME|Command Class = COMMAND_CLASS_GROUPING_NAME|Command Class = COMMAND_CLASS_GROUPING_NAME|Command Class = COMMAND_CLASS_GROUPING_NAME|Command Class = COMMAND_CLASS_GROUPING_NAME|Command Class = COMMAND_CLASS_GROUPING_NAME|Command Class = COMMAND_CLASS_GROUPING_NAME|
|Command = GROUPING_NAME_GET<br>|Command = GROUPING_NAME_GET<br>|Command = GROUPING_NAME_GET<br>|Command = GROUPING_NAME_GET<br>|Command = GROUPING_NAME_GET<br>|Command = GROUPING_NAME_GET<br>|Command = GROUPING_NAME_GET<br>|Command = GROUPING_NAME_GET<br>|
|Grouping Identifer|Grouping Identifer|Grouping Identifer|Grouping Identifer|Grouping Identifer|Grouping Identifer|Grouping Identifer|Grouping Identifer|



**Grouping** **Identifier** **(8** **bits)**

The field specifies the grouping identifier.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 703




<!-- PAGE 705 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.23.3** **Group** **Name** **Report** **Command**


The Grouping Name Report Command is used to report the grouping Identifier name.


Table 3.104: Grouping Name Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_GROUPING_NAME|Command Class = COMMAND_CLASS_GROUPING_NAME|Command Class = COMMAND_CLASS_GROUPING_NAME|Command Class = COMMAND_CLASS_GROUPING_NAME|Command Class = COMMAND_CLASS_GROUPING_NAME|Command Class = COMMAND_CLASS_GROUPING_NAME|Command Class = COMMAND_CLASS_GROUPING_NAME|Command Class = COMMAND_CLASS_GROUPING_NAME|
|Command = GROUPING_NAME_REPORT<br>|Command = GROUPING_NAME_REPORT<br>|Command = GROUPING_NAME_REPORT<br>|Command = GROUPING_NAME_REPORT<br>|Command = GROUPING_NAME_REPORT<br>|Command = GROUPING_NAME_REPORT<br>|Command = GROUPING_NAME_REPORT<br>|Command = GROUPING_NAME_REPORT<br>|
|Grouping Identifer|Grouping Identifer|Grouping Identifer|Grouping Identifer|Grouping Identifer|Grouping Identifer|Grouping Identifer|Grouping Identifer|
|Reserved|Reserved|Reserved|Reserved|Reserved|Char. Presentation|Char. Presentation|Char. Presentation|
|Grouping Name 1|Grouping Name 1|Grouping Name 1|Grouping Name 1|Grouping Name 1|Grouping Name 1|Grouping Name 1|Grouping Name 1|
|…|…|…|…|…|…|…|…|
|Grouping Name N|Grouping Name N|Grouping Name N|Grouping Name N|Grouping Name N|Grouping Name N|Grouping Name N|Grouping Name N|



**Grouping** **Identifier** **(8** **bits)**

The field specifies the grouping identifier.


**Reserved**

This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**Char.** **Presentation** **(3** **bits)**


Refer to description under the Grouping Name Set Command


**Grouping** **Name** **(N** **bytes)**

The Grouping Name fields contain the assigned group name. The Group Name can have a maximum
of 16 characters and a minimum of 0 characters.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 704