<!-- PAGE 107 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.13** **Basic** **Command** **Class,** **version** **1**


The Basic Command Class allows a controlling device to operate the primary functionality of a
supporting device without any further knowledge.


The Basic Command Class ensures a basic interoperability if no other command class is shared by
two devices.


The Basic Command Class is an actuator control command class. Refer to Section 2.1.6.


**2.2.13.1** **Compatibility** **considerations**


A specific device may not be able to support all Basic CC commands or parameter levels. For instance,
a relay can only open fully in response to any non-zero value.


CC:0020.1.00.22.001 Any device SHOULD support the Basic Command Class.


CC:0020.01.00.21.001
A device MUST implement mappings from the Basic Command Class to specific commands according
to the advertised generic and specific device class of the Node Info frame. Mappings defined by a
Specific Device Class have precedence over the Generic Device Class.


CC:0020.01.00.21.002 For Z-Wave Plus devices, the Basic Command Class MUST be mapped according to the actual Z-Wave
Plus Device Type. For further information, refer to [34], Section 7.


The following sections only present frame formats. For details on the mapping to other command
classes, refer to [34] and Section 7.


**2.2.13.1.1** **Node** **Information** **Frame** **(NIF)**


CC:0020.01.00.21.003 The Basic Command Class MUST NOT be advertised in the Node Information Frame.


CC:0020.01.00.21.004 The Basic Command Class MUST NOT be advertised in the Security Commands Supported Report
(S0 as well as S2)


CC:0020.01.00.21.005 A securely included node MAY support the Basic Command Class at the highest security level but it
MUST NOT support the Basic Command Class at any lower security level or non-securely.


**2.2.13.2** **Basic** **Set** **Command**


This command is used to set a value in a supporting device.


Table 2.80: Basic Set Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_BASIC|Command Class = COMMAND_CLASS_BASIC|Command Class = COMMAND_CLASS_BASIC|Command Class = COMMAND_CLASS_BASIC|Command Class = COMMAND_CLASS_BASIC|Command Class = COMMAND_CLASS_BASIC|Command Class = COMMAND_CLASS_BASIC|Command Class = COMMAND_CLASS_BASIC|
|Command = BASIC_SET|Command = BASIC_SET|Command = BASIC_SET|Command = BASIC_SET|Command = BASIC_SET|Command = BASIC_SET|Command = BASIC_SET|Command = BASIC_SET|
|Value|Value|Value|Value|Value|Value|Value|Value|



**Value** **(8** **bits)**


CC:0020.01.01.12.001 A supporting device SHOULD support all parameter values in the range {0x00..0x63, 0xFF}.


CC:0020.01.01.11.001 A controlling device MUST NOT assume that a receiving device reacts to this command.


CC:0020.01.01.11.002 A receiving device MUST interpret Basic Set parameter values according to the requirements of the
Device Class implemented by the device. Refer to [34] and Section 7.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 106




<!-- PAGE 108 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.13.3** **Basic** **Get** **Command**


This command is used to request the status of a supporting device.


CC:0020.01.02.11.001 The Basic Report Command MUST be returned in response to this command.


CC:0020.01.02.11.002 This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 2.81: Basic Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_BASIC|Command Class = COMMAND_CLASS_BASIC|Command Class = COMMAND_CLASS_BASIC|Command Class = COMMAND_CLASS_BASIC|Command Class = COMMAND_CLASS_BASIC|Command Class = COMMAND_CLASS_BASIC|Command Class = COMMAND_CLASS_BASIC|Command Class = COMMAND_CLASS_BASIC|
|Command = BASIC_GET|Command = BASIC_GET|Command = BASIC_GET|Command = BASIC_GET|Command = BASIC_GET|Command = BASIC_GET|Command = BASIC_GET|Command = BASIC_GET|



**2.2.13.4** **Basic** **Report** **Command**


This command is used to advertise the status of the primary functionality of the device.


Table 2.82: Basic Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_BASIC|Command Class = COMMAND_CLASS_BASIC|Command Class = COMMAND_CLASS_BASIC|Command Class = COMMAND_CLASS_BASIC|Command Class = COMMAND_CLASS_BASIC|Command Class = COMMAND_CLASS_BASIC|Command Class = COMMAND_CLASS_BASIC|Command Class = COMMAND_CLASS_BASIC|
|Command = BASIC_REPORT|Command = BASIC_REPORT|Command = BASIC_REPORT|Command = BASIC_REPORT|Command = BASIC_REPORT|Command = BASIC_REPORT|Command = BASIC_REPORT|Command = BASIC_REPORT|
|Value|Value|Value|Value|Value|Value|Value|Value|



**Value** **(8** **bits)**

CC:0020.01.03.12.001 The Value field SHOULD advertise the current value of the device hardware; also while in transition
to a new target value.


For details on the mapping of values, refer to [34] and Section 7.

CC:0020.01.03.11.001 A controlling device MUST NOT assume that the Value is identical to a value previously specified in
a Set command; not even when a transition has ended.

CC:0020.01.03.11.002 A receiving device MUST interpret the Value field according to Table 2.83.


Table 2.83: Basic Report::Value

|Value|Level|State|
|---|---|---|
|0 (0x00)|0%|Of|
|1..99 (0x01..0x63)|1..100%|On|
|…|Reserved|Reserved|
|254 (0xFE)|Unknown|Unknown|
|255 (0xFF)|100%|On|



CC:0020.01.03.11.003 All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 107

---

<!-- PAGE 109 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.14** **Basic** **Command** **Class,** **version** **2**


The Basic Command Class allows a controlling device to operate the primary functionality of another
device without any further knowledge.


The Basic Command Class ensures a basic interoperability if no other Command Class is shared by
two devices.


The Basic Command Class is an actuator control command class. Refer to Section 2.1.6.


**2.2.14.1** **Compatibility** **considerations**


CC:0020.02.00.21.001 A device supporting Basic Command Class, version 2 MUST support Basic Command Class, version
1. Commands not described in this version remain unchanged from version 1.


Version 2 adds the distinction between the Current Value and the Target State of the device.

Version 2 elevates the requirement level so that the Current Value field of the Basic Report command
CC:0020.02.00.21.002 MUST advertise the current value of the device hardware; also while in transition to a new target
value.


The compatibility considerations from version 1 also apply to this version. Refer to Section 2.2.13.1.


**2.2.14.2** **Basic** **Report** **Command**


This command is used to advertise the status of the primary functionality of the device.


Table 2.84: Basic Report Command, version 2

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_BASIC|Command Class = COMMAND_CLASS_BASIC|Command Class = COMMAND_CLASS_BASIC|Command Class = COMMAND_CLASS_BASIC|Command Class = COMMAND_CLASS_BASIC|Command Class = COMMAND_CLASS_BASIC|Command Class = COMMAND_CLASS_BASIC|Command Class = COMMAND_CLASS_BASIC|
|Command = BASIC_REPORT|Command = BASIC_REPORT|Command = BASIC_REPORT|Command = BASIC_REPORT|Command = BASIC_REPORT|Command = BASIC_REPORT|Command = BASIC_REPORT|Command = BASIC_REPORT|
|Current Value|Current Value|Current Value|Current Value|Current Value|Current Value|Current Value|Current Value|
|Target Value|Target Value|Target Value|Target Value|Target Value|Target Value|Target Value|Target Value|
|Duration|Duration|Duration|Duration|Duration|Duration|Duration|Duration|



**Current** **Value** **(8** **bits)**

CC:0020.02.03.11.001 The Current Value field MUST advertise the current value of the device hardware; also while in
transition to a new target value.


The advertised values may vary depending on the device class implemented by the supporting device.
CC:0020.02.03.11.002 A controlling device MUST interpret the value according to Table 21.For details on the mapping of
values, refer to [34] and Section 7.


CC:0020.02.03.12.001 The Current Value SHOULD be identical to the Target Value when a transition has ended.


**Target** **Value** **(8** **bits)**

CC:0020.02.03.11.003 The Target Value field MUST advertise the target value of an ongoing transition or the most recent
transition.


The advertised values may vary depending on the device class implemented by the supporting device.
CC:0020.02.03.11.004 A controlling device MUST interpret the value according to Table 2.83.


For details on the mapping of values, refer [34] and Section 7.

CC:0020.02.03.11.005 If queried after receiving a Set command, the Target Value field MUST advertise the target value

CC:0020.02.03.13.001 specified in the Set command. The Target Value MAY change at a later time due to local control or
a “Stop” motion control command.

CC:0020.02.03.11.006 If the device is in a motion controlled transition, the Target Value field MUST advertise the min or
max value (depending on the direction) according to the command class mappings defined in [34] and
Section 7.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 108




<!-- PAGE 110 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**Duration** **(8** **bits)**

CC:0020.02.03.12.002 The Duration field SHOULD advertise the time needed to reach the Target Value at the actual
transition rate. The encoding of the Duration field MUST be according to Table 2.10


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 109