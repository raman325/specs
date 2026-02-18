<!-- PAGE 753 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.37** **Node** **Naming** **and** **Location** **Command** **Class,** **version** **1**


The Node Naming and Location Command Class is used to assign a name and a location text string
to a supporting node.


**3.2.37.1** **Node** **Name** **Set** **Command**


This command is used to set the name of the receiving node.


Table 3.138: Node Name Set Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_NODE_NAMING|Command Class = COMMAND_CLASS_NODE_NAMING|Command Class = COMMAND_CLASS_NODE_NAMING|Command Class = COMMAND_CLASS_NODE_NAMING|Command Class = COMMAND_CLASS_NODE_NAMING|Command Class = COMMAND_CLASS_NODE_NAMING|Command Class = COMMAND_CLASS_NODE_NAMING|Command Class = COMMAND_CLASS_NODE_NAMING|
|Command = NODE_NAMING_NODE_NAME_SET|Command = NODE_NAMING_NODE_NAME_SET|Command = NODE_NAMING_NODE_NAME_SET|Command = NODE_NAMING_NODE_NAME_SET|Command = NODE_NAMING_NODE_NAME_SET|Command = NODE_NAMING_NODE_NAME_SET|Command = NODE_NAMING_NODE_NAME_SET|Command = NODE_NAMING_NODE_NAME_SET|
|Reserved|Reserved|Reserved|Reserved|Reserved|Char. Presentation|Char. Presentation|Char. Presentation|
|Node name char 1|Node name char 1|Node name char 1|Node name char 1|Node name char 1|Node name char 1|Node name char 1|Node name char 1|
|…|…|…|…|…|…|…|…|
|Node name char N|Node name char N|Node name char N|Node name char N|Node name char N|Node name char N|Node name char N|Node name char N|



**Node** **name** **char** **(N** **bytes)**

This field is used to indicate the actual assigned name for the node.

This field MUST be encoded using the specified character representation in the Char.Presentation
field.


The Node name string MUST NOT contain any appended termination characters.

The length of this field MUST be in the range 1..16 bytes. The length of this field MUST be determined
from the frame length.


A node receiving this command with a Node name char longer than 16 bytes MUST ignore any
byte/character following the 16th byte.


Devices using the Unicode UTF-16 characters representation can set Name strings using a maximum
of 8 characters because each character is encoded with 2 bytes. In this case, the first byte MUST be
the most significant byte.


**Reserved**

This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**Char.** **Presentation** **(3** **bits)**

This field is used to indicate the character encoding for the Node name char field.

This field MUST comply with Table 3.139:


Table 3.139: Node Name Set::Char. Presentation Encoding

|Source -> Value|Description|
|---|---|
|0x00|Using standard ASCII codes, see _ASCII Codes_ (values 128-255 are ig-<br>nored)|
|0x01|Using standard and OEM Extended ASCII codes, see _ASCII Codes_.|
|0x02|Unicode UTF-16|



All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 752




<!-- PAGE 754 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.37.2** **Node** **Name** **Get** **Command**


This command is used to request the stored name from a node.


The _Node_ _Name_ _Report_ _Command_ MUST be returned in response to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


This command is used to set the name of the receiving node.


Table 3.140: Node Name Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_NODE_NAMING|Command Class = COMMAND_CLASS_NODE_NAMING|Command Class = COMMAND_CLASS_NODE_NAMING|Command Class = COMMAND_CLASS_NODE_NAMING|Command Class = COMMAND_CLASS_NODE_NAMING|Command Class = COMMAND_CLASS_NODE_NAMING|Command Class = COMMAND_CLASS_NODE_NAMING|Command Class = COMMAND_CLASS_NODE_NAMING|
|Command = NODE_NAMING_NODE_NAME_GET|Command = NODE_NAMING_NODE_NAME_GET|Command = NODE_NAMING_NODE_NAME_GET|Command = NODE_NAMING_NODE_NAME_GET|Command = NODE_NAMING_NODE_NAME_GET|Command = NODE_NAMING_NODE_NAME_GET|Command = NODE_NAMING_NODE_NAME_GET|Command = NODE_NAMING_NODE_NAME_GET|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 753




<!-- PAGE 755 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.37.3** **Node** **Name** **Report** **Command**


This command is used to advertise the name assigned to the sending node.


Table 3.141: Node Name Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_NODE_NAMING|Command Class = COMMAND_CLASS_NODE_NAMING|Command Class = COMMAND_CLASS_NODE_NAMING|Command Class = COMMAND_CLASS_NODE_NAMING|Command Class = COMMAND_CLASS_NODE_NAMING|Command Class = COMMAND_CLASS_NODE_NAMING|Command Class = COMMAND_CLASS_NODE_NAMING|Command Class = COMMAND_CLASS_NODE_NAMING|
|Command = NODE_NAMING_NODE_NAME_REPORT|Command = NODE_NAMING_NODE_NAME_REPORT|Command = NODE_NAMING_NODE_NAME_REPORT|Command = NODE_NAMING_NODE_NAME_REPORT|Command = NODE_NAMING_NODE_NAME_REPORT|Command = NODE_NAMING_NODE_NAME_REPORT|Command = NODE_NAMING_NODE_NAME_REPORT|Command = NODE_NAMING_NODE_NAME_REPORT|
|Reserved|Reserved|Reserved|Reserved|Reserved|Char. Presentation|Char. Presentation|Char. Presentation|
|Node name char 1|Node name char 1|Node name char 1|Node name char 1|Node name char 1|Node name char 1|Node name char 1|Node name char 1|
|…|…|…|…|…|…|…|…|
|Node name char N|Node name char N|Node name char N|Node name char N|Node name char N|Node name char N|Node name char N|Node name char N|



For fields’ description, refer to Section 3.2.37.1 Node Name Set Command

A sending node MUST comply with fields’ description from Section 3.2.37.1 Node Name Set Command


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 754




<!-- PAGE 756 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.37.4** **Node** **Location** **Set** **Command**


The Node Location Set Command is used to set a location name in a node in a Z-Wave network.


Table 3.142: Node Location Set Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_NODE_NAMING|Command Class = COMMAND_CLASS_NODE_NAMING|Command Class = COMMAND_CLASS_NODE_NAMING|Command Class = COMMAND_CLASS_NODE_NAMING|Command Class = COMMAND_CLASS_NODE_NAMING|Command Class = COMMAND_CLASS_NODE_NAMING|Command Class = COMMAND_CLASS_NODE_NAMING|Command Class = COMMAND_CLASS_NODE_NAMING|
|Command = NODE_NAMING_NODE_LOCATION_SET|Command = NODE_NAMING_NODE_LOCATION_SET|Command = NODE_NAMING_NODE_LOCATION_SET|Command = NODE_NAMING_NODE_LOCATION_SET|Command = NODE_NAMING_NODE_LOCATION_SET|Command = NODE_NAMING_NODE_LOCATION_SET|Command = NODE_NAMING_NODE_LOCATION_SET|Command = NODE_NAMING_NODE_LOCATION_SET|
|Reserved|Reserved|Reserved|Reserved|Reserved|Char. Presentation|Char. Presentation|Char. Presentation|
|Node location char 1|Node location char 1|Node location char 1|Node location char 1|Node location char 1|Node location char 1|Node location char 1|Node location char 1|
|…|…|…|…|…|…|…|…|
|Node location char N|Node location char N|Node location char N|Node location char N|Node location char N|Node location char N|Node location char N|Node location char N|



**Node** **location** **char** **(N** **bytes)**

This field is used to indicate the actual assigned location for the node.

This field MUST be encoded using the specified character representation in the Char. Presentation
field.


The Node location string MUST NOT contain any appended termination characters.

The length of this field MUST be in the range 1..16 bytes. The length of this field MUST be determined
from the frame length.


A node receiving this command with a Node location char longer than 16 bytes MUST ignore any
byte/character following the 16th byte.


Devices using the Unicode UTF-16 characters representation can set Location strings using a maximum
of 8 characters because each character is encoded with 2 bytes. In this case, the first byte MUST be
the most significant byte.


**Reserved**

This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**Char.** **Presentation** **(3** **bits)**

This field is used to indicate the character encoding for the Node location char field. This field MUST
comply with Table 3.139.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 755




<!-- PAGE 757 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.37.5** **Node** **Location** **Get** **Command**


This command is used to request the stored node location from a node.


The _Node_ _Location_ _Report_ _Command_ MUST be returned in response to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 3.143: Node Location Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_NODE_NAMING|Command Class = COMMAND_CLASS_NODE_NAMING|Command Class = COMMAND_CLASS_NODE_NAMING|Command Class = COMMAND_CLASS_NODE_NAMING|Command Class = COMMAND_CLASS_NODE_NAMING|Command Class = COMMAND_CLASS_NODE_NAMING|Command Class = COMMAND_CLASS_NODE_NAMING|Command Class = COMMAND_CLASS_NODE_NAMING|
|Command = NODE_NAMING_NODE_LOCATION_GET|Command = NODE_NAMING_NODE_LOCATION_GET|Command = NODE_NAMING_NODE_LOCATION_GET|Command = NODE_NAMING_NODE_LOCATION_GET|Command = NODE_NAMING_NODE_LOCATION_GET|Command = NODE_NAMING_NODE_LOCATION_GET|Command = NODE_NAMING_NODE_LOCATION_GET|Command = NODE_NAMING_NODE_LOCATION_GET|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 756




<!-- PAGE 758 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.37.6** **Node** **Location** **Report** **Command**


This command is used to advertise the node location.


Table 3.144: Node Location Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_NODE_NAMING|Command Class = COMMAND_CLASS_NODE_NAMING|Command Class = COMMAND_CLASS_NODE_NAMING|Command Class = COMMAND_CLASS_NODE_NAMING|Command Class = COMMAND_CLASS_NODE_NAMING|Command Class = COMMAND_CLASS_NODE_NAMING|Command Class = COMMAND_CLASS_NODE_NAMING|Command Class = COMMAND_CLASS_NODE_NAMING|
|Command = NODE_NAMING_NODE_LOCATION_REPORT|Command = NODE_NAMING_NODE_LOCATION_REPORT|Command = NODE_NAMING_NODE_LOCATION_REPORT|Command = NODE_NAMING_NODE_LOCATION_REPORT|Command = NODE_NAMING_NODE_LOCATION_REPORT|Command = NODE_NAMING_NODE_LOCATION_REPORT|Command = NODE_NAMING_NODE_LOCATION_REPORT|Command = NODE_NAMING_NODE_LOCATION_REPORT|
|Reserved|Reserved|Reserved|Reserved|Reserved|Char. Presentation|Char. Presentation|Char. Presentation|
|Node location char 1|Node location char 1|Node location char 1|Node location char 1|Node location char 1|Node location char 1|Node location char 1|Node location char 1|
|…|…|…|…|…|…|…|…|
|Node location char N|Node location char N|Node location char N|Node location char N|Node location char N|Node location char N|Node location char N|Node location char N|



For fields’ description, refer to Section 3.2.37.4 Node Location Set Command

A sending node MUST comply with fields’ description from Section 3.2.37.4 Node Location Set Command.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 757