<!-- PAGE 123 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.21** **Binary** **Toggle** **Switch** **Command** **Class,** **version** **1** **[OBSOLETED]**


**Warning:** **THIS** **COMMAND** **CLASS** **HAS** **BEEN** **OBSOLETED**


A node MUST NOT implement this Command Class.


New implementations MUST use the _Binary_ _Switch_ _Command_ _Class,_ _version_ _1_


The Binary Toggle Switch Command Class is used for toggle-style control of binary actuator devices.


**2.2.21.1** **Binary** **Toggle** **Switch** **Set** **Command**


This command is used to toggle a device e.g. from on to off and from off to on.


Table 2.103: Binary Toggle Switch Set Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SWITCH_TOGGLE_BINARY|Command Class = COMMAND_CLASS_SWITCH_TOGGLE_BINARY|Command Class = COMMAND_CLASS_SWITCH_TOGGLE_BINARY|Command Class = COMMAND_CLASS_SWITCH_TOGGLE_BINARY|Command Class = COMMAND_CLASS_SWITCH_TOGGLE_BINARY|Command Class = COMMAND_CLASS_SWITCH_TOGGLE_BINARY|Command Class = COMMAND_CLASS_SWITCH_TOGGLE_BINARY|Command Class = COMMAND_CLASS_SWITCH_TOGGLE_BINARY|
|Command = SWITCH_TOGGLE_BINARY_SET|Command = SWITCH_TOGGLE_BINARY_SET|Command = SWITCH_TOGGLE_BINARY_SET|Command = SWITCH_TOGGLE_BINARY_SET|Command = SWITCH_TOGGLE_BINARY_SET|Command = SWITCH_TOGGLE_BINARY_SET|Command = SWITCH_TOGGLE_BINARY_SET|Command = SWITCH_TOGGLE_BINARY_SET|



**2.2.21.2** **Binary** **Toggle** **Switch** **Get** **Command**


This command is used to request the state of the load controlled by the device.


The Binary Toggle Switch Report Command MUST be returned in response to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 2.104: Binary Toggle Switch Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SWITCH_TOGGLE_BINARY|Command Class = COMMAND_CLASS_SWITCH_TOGGLE_BINARY|Command Class = COMMAND_CLASS_SWITCH_TOGGLE_BINARY|Command Class = COMMAND_CLASS_SWITCH_TOGGLE_BINARY|Command Class = COMMAND_CLASS_SWITCH_TOGGLE_BINARY|Command Class = COMMAND_CLASS_SWITCH_TOGGLE_BINARY|Command Class = COMMAND_CLASS_SWITCH_TOGGLE_BINARY|Command Class = COMMAND_CLASS_SWITCH_TOGGLE_BINARY|
|Command = SWITCH_TOGGLE_BINARY_GET|Command = SWITCH_TOGGLE_BINARY_GET|Command = SWITCH_TOGGLE_BINARY_GET|Command = SWITCH_TOGGLE_BINARY_GET|Command = SWITCH_TOGGLE_BINARY_GET|Command = SWITCH_TOGGLE_BINARY_GET|Command = SWITCH_TOGGLE_BINARY_GET|Command = SWITCH_TOGGLE_BINARY_GET|



**2.2.21.3** **Binary** **Toggle** **Switch** **Report** **Command**


This command is used to advertise the value of a toggle switch.


Table 2.105: Binary Toggle Switch Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SWITCH_TOGGLE_BINARY|Command Class = COMMAND_CLASS_SWITCH_TOGGLE_BINARY|Command Class = COMMAND_CLASS_SWITCH_TOGGLE_BINARY|Command Class = COMMAND_CLASS_SWITCH_TOGGLE_BINARY|Command Class = COMMAND_CLASS_SWITCH_TOGGLE_BINARY|Command Class = COMMAND_CLASS_SWITCH_TOGGLE_BINARY|Command Class = COMMAND_CLASS_SWITCH_TOGGLE_BINARY|Command Class = COMMAND_CLASS_SWITCH_TOGGLE_BINARY|
|Command = SWITCH_TOGGLE_BINARY_GET|Command = SWITCH_TOGGLE_BINARY_GET|Command = SWITCH_TOGGLE_BINARY_GET|Command = SWITCH_TOGGLE_BINARY_GET|Command = SWITCH_TOGGLE_BINARY_GET|Command = SWITCH_TOGGLE_BINARY_GET|Command = SWITCH_TOGGLE_BINARY_GET|Command = SWITCH_TOGGLE_BINARY_GET|
|Value|Value|Value|Value|Value|Value|Value|Value|



**Value** **(8** **bits)**

The value MAY be 0x00 (off) or 0xFF (on).


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 122