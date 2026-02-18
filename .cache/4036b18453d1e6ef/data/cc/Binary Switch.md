<!-- PAGE 119 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.19** **Binary** **Switch** **Command** **Class,** **version** **1**


The Binary Switch Command Class is used to control the On/Off state of supporting nodes. The
Binary Switch Command Class is an actuator control Command Class. Refer to Section 2.1.6.


**2.2.19.1** **Binary** **Switch** **Set** **Command**


This command is used to set the On/Off state at the receiving node.


CC:0025.01.01.13.001 A receiving node MAY apply a non-zero duration to the transition from one value to a new value.


Table 2.96: Binary Switch Set Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SWITCH_BINARY (0x25)|Command Class = COMMAND_CLASS_SWITCH_BINARY (0x25)|Command Class = COMMAND_CLASS_SWITCH_BINARY (0x25)|Command Class = COMMAND_CLASS_SWITCH_BINARY (0x25)|Command Class = COMMAND_CLASS_SWITCH_BINARY (0x25)|Command Class = COMMAND_CLASS_SWITCH_BINARY (0x25)|Command Class = COMMAND_CLASS_SWITCH_BINARY (0x25)|Command Class = COMMAND_CLASS_SWITCH_BINARY (0x25)|
|Command = SWITCH_BINARY_SET (0x01)|Command = SWITCH_BINARY_SET (0x01)|Command = SWITCH_BINARY_SET (0x01)|Command = SWITCH_BINARY_SET (0x01)|Command = SWITCH_BINARY_SET (0x01)|Command = SWITCH_BINARY_SET (0x01)|Command = SWITCH_BINARY_SET (0x01)|Command = SWITCH_BINARY_SET (0x01)|
|Value|Value|Value|Value|Value|Value|Value|Value|



**Value** **(8** **bits)**


CC:0025.01.01.11.001
This field is used to specify the On/Off state that the receiving node MUST assume. This field MUST
be encoded according to Table 2.97.


Table 2.97: Binary Switch Set                     - Value encoding

|Value|Level|State|
|---|---|---|
|0 (0x00)|0%|Of|
|1..99 (0x01..0x63)|100%|On|
|255 (0xFF)|100%|On|



CC:0025.01.01.11.002 All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.


CC:0025.01.01.11.003 If the supporting node uses this Command Class, the values MUST be interpreted as follow:


      - The value 0 MUST represent the lowest possible throughput (light, water, sound, etc.)


      - The values 1..99 and 255 MUST represent the highest possible throughput (light, water, sound,
etc.)


The above value mapping of the Binary Switch Command Class Value allows a controlling node to
control a mixed group of Binary Switch and Multilevel Switch supporting nodes via Basic Set commands. Nodes supporting the Binary Switch Command Class turn On or Off while nodes supporting
the Multilevel Switch Command Class are set at the specified value level.


**2.2.19.2** **Binary** **Switch** **Get** **Command**


This command is used to request the current On/Off state from a node.


CC:0025.01.02.11.001 The _Binary_ _Switch_ _Report_ _Command_ MUST be returned in response to this command.


CC:0025.01.02.11.002 This command MUST NOT be issued via multicast addressing.


CC:0025.01.02.11.003 A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 2.98: Binary Switch Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SWITCH_BINARY (0x25)|Command Class = COMMAND_CLASS_SWITCH_BINARY (0x25)|Command Class = COMMAND_CLASS_SWITCH_BINARY (0x25)|Command Class = COMMAND_CLASS_SWITCH_BINARY (0x25)|Command Class = COMMAND_CLASS_SWITCH_BINARY (0x25)|Command Class = COMMAND_CLASS_SWITCH_BINARY (0x25)|Command Class = COMMAND_CLASS_SWITCH_BINARY (0x25)|Command Class = COMMAND_CLASS_SWITCH_BINARY (0x25)|
|Command = SWITCH_BINARY_GET (0x02)|Command = SWITCH_BINARY_GET (0x02)|Command = SWITCH_BINARY_GET (0x02)|Command = SWITCH_BINARY_GET (0x02)|Command = SWITCH_BINARY_GET (0x02)|Command = SWITCH_BINARY_GET (0x02)|Command = SWITCH_BINARY_GET (0x02)|Command = SWITCH_BINARY_GET (0x02)|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 118




<!-- PAGE 120 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.19.3** **Binary** **Switch** **Report** **Command**


This command is used to advertise the current On/Off state at the sending node.


Table 2.99: Binary Switch Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SWITCH_BINARY (0x25)|Command Class = COMMAND_CLASS_SWITCH_BINARY (0x25)|Command Class = COMMAND_CLASS_SWITCH_BINARY (0x25)|Command Class = COMMAND_CLASS_SWITCH_BINARY (0x25)|Command Class = COMMAND_CLASS_SWITCH_BINARY (0x25)|Command Class = COMMAND_CLASS_SWITCH_BINARY (0x25)|Command Class = COMMAND_CLASS_SWITCH_BINARY (0x25)|Command Class = COMMAND_CLASS_SWITCH_BINARY (0x25)|
|Command = SWITCH_BINARY_REPORT (0x03)|Command = SWITCH_BINARY_REPORT (0x03)|Command = SWITCH_BINARY_REPORT (0x03)|Command = SWITCH_BINARY_REPORT (0x03)|Command = SWITCH_BINARY_REPORT (0x03)|Command = SWITCH_BINARY_REPORT (0x03)|Command = SWITCH_BINARY_REPORT (0x03)|Command = SWITCH_BINARY_REPORT (0x03)|
|Value|Value|Value|Value|Value|Value|Value|Value|



**Value** **(8** **bits)**


CC:0025.01.03.11.001
This field is used to specify the On/Off state that the receiving node MUST assume. This field MUST
be encoded according to Table 2.100.


Table 2.100: Binary Switch Report                   - Value encoding

|Value|Level|State|
|---|---|---|
|0 (0x00)|0%|Of|
|254 (0xFE)|Unknown|Unknown|
|255 (0xFF)|100%|On|



CC:0025.01.03.11.002 All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.

CC:0025.01.03.12.001 This field SHOULD advertise the current value of the node’s hardware; also while in transition to a
new value.


CC:0025.01.03.11.003
A controlling node MUST NOT assume that this field’s value is identical to the value previously issued
with a _Binary_ _Switch_ _Set_ _Command_ .


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 119

---

<!-- PAGE 121 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.20** **Binary** **Switch** **Command** **Class,** **version** **2**


The Binary Switch Command Class is used to control the On/Off state of supporting nodes.


The Binary Switch Command Class is an actuator control Command Class. Refer to Section 2.1.6.


**2.2.20.1** **Compatibility** **considerations**


CC:0025.02.00.21.001 A node supporting Binary Switch Command Class, version 2 MUST support the _Binary_ _Switch_
_Command_ _Class,_ _version_ _1_ .


CC:0025.02.00.21.002 Commands not described in this version MUST remain unchanged from version 1.


Version 2 adds duration and target value control and reporting.


**2.2.20.2** **Binary** **Switch** **Set** **Command**


This command is used to set the binary state at the receiving node.


Table 2.101: Binary Switch Set Command, version 2

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SWITCH_BINARY|Command Class = COMMAND_CLASS_SWITCH_BINARY|Command Class = COMMAND_CLASS_SWITCH_BINARY|Command Class = COMMAND_CLASS_SWITCH_BINARY|Command Class = COMMAND_CLASS_SWITCH_BINARY|Command Class = COMMAND_CLASS_SWITCH_BINARY|Command Class = COMMAND_CLASS_SWITCH_BINARY|Command Class = COMMAND_CLASS_SWITCH_BINARY|
|Command = SWITCH_BINARY_SET|Command = SWITCH_BINARY_SET|Command = SWITCH_BINARY_SET|Command = SWITCH_BINARY_SET|Command = SWITCH_BINARY_SET|Command = SWITCH_BINARY_SET|Command = SWITCH_BINARY_SET|Command = SWITCH_BINARY_SET|
|Target Value|Target Value|Target Value|Target Value|Target Value|Target Value|Target Value|Target Value|
|Duration|Duration|Duration|Duration|Duration|Duration|Duration|Duration|



**Target** **Value** **(8** **bits)**


CC:0025.02.01.11.001
This field is used to specify the On/Off state that the receiving node MUST assume. This field MUST
be encoded according to Table 2.97.


**Duration** **(8** **bits)**


CC:0025.02.01.12.001
This field is used to specify the duration that the transition from the current value to the Target Value
SHOULD take.

CC:0025.02.01.12.002 A supporting node SHOULD respect the specified duration value.


CC:0025.02.01.11.002 The encoding of the Duration value MUST be according to Table 2.9


**2.2.20.3** **Binary** **Switch** **Report** **Command**


This command is used to advertise the current On/Off state at the sending node.


Table 2.102: Binary Switch Report Command, version 2

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SWITCH_BINARY|Command Class = COMMAND_CLASS_SWITCH_BINARY|Command Class = COMMAND_CLASS_SWITCH_BINARY|Command Class = COMMAND_CLASS_SWITCH_BINARY|Command Class = COMMAND_CLASS_SWITCH_BINARY|Command Class = COMMAND_CLASS_SWITCH_BINARY|Command Class = COMMAND_CLASS_SWITCH_BINARY|Command Class = COMMAND_CLASS_SWITCH_BINARY|
|Command = SWITCH_BINARY_REPORT|Command = SWITCH_BINARY_REPORT|Command = SWITCH_BINARY_REPORT|Command = SWITCH_BINARY_REPORT|Command = SWITCH_BINARY_REPORT|Command = SWITCH_BINARY_REPORT|Command = SWITCH_BINARY_REPORT|Command = SWITCH_BINARY_REPORT|
|Current Value|Current Value|Current Value|Current Value|Current Value|Current Value|Current Value|Current Value|
|Target Value|Target Value|Target Value|Target Value|Target Value|Target Value|Target Value|Target Value|
|Duration|Duration|Duration|Duration|Duration|Duration|Duration|Duration|



**Current** **Value** **(8** **bits)**

CC:0025.02.03.11.001 This field is used to advertise the current On/Off state at the sending node. This field MUST be
encoded according to Table 2.100.


CC:0025.02.03.11.002 The advertised Current Value MUST NOT be updated to the Target Value before the hardware
actuator has actually reached the Target Value.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 120




<!-- PAGE 122 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**Target** **Value** **(8** **bits)**

CC:0025.02.03.11.003 This field MUST advertise the target value of an ongoing transition or the most recent transition.

CC:0025.02.03.11.004 This field MUST be encoded according to Table 2.100.


**Duration** **(8** **bits)**

CC:0025.02.03.12.001 The duration field SHOULD advertise the duration of a transition from the Current Value to the
Target Value.

CC:0025.02.03.11.005 The encoding of the Duration field MUST be according to Table 2.10.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 121