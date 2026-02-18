<!-- PAGE 247 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.50** **IR** **Repeater** **Command** **Class,** **version** **1**


The IR Repeater Command Class is used to get supporting nodes to learn and/or repeat IR signals
used to control appliances.


A supporting node MUST have the capability to issue or receive IR signals.


**2.2.50.1** **IR** **Repeater** **Capabilities** **Get** **Command**


This command is used to request the IR Repeater capabilities of a node.


The IR Repeater Capabilities Report Command MUST be returned in response to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 2.288: IR Repeater Capabilities Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|
|Command = IR_REPEATER_CAPABILITIES_GET (0x01)|Command = IR_REPEATER_CAPABILITIES_GET (0x01)|Command = IR_REPEATER_CAPABILITIES_GET (0x01)|Command = IR_REPEATER_CAPABILITIES_GET (0x01)|Command = IR_REPEATER_CAPABILITIES_GET (0x01)|Command = IR_REPEATER_CAPABILITIES_GET (0x01)|Command = IR_REPEATER_CAPABILITIES_GET (0x01)|Command = IR_REPEATER_CAPABILITIES_GET (0x01)|



**2.2.50.2** **IR** **Repeater** **Capabilities** **Report** **Command**


This command is used to advertise the IR Repeater capabilities of the sending node.


Table 2.289: IR Repeater Capabilities Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|
|Command = IR_REPEATER_CAPABILITIES_REPORT (0x02)<br>|Command = IR_REPEATER_CAPABILITIES_REPORT (0x02)<br>|Command = IR_REPEATER_CAPABILITIES_REPORT (0x02)<br>|Command = IR_REPEATER_CAPABILITIES_REPORT (0x02)<br>|Command = IR_REPEATER_CAPABILITIES_REPORT (0x02)<br>|Command = IR_REPEATER_CAPABILITIES_REPORT (0x02)<br>|Command = IR_REPEATER_CAPABILITIES_REPORT (0x02)<br>|Command = IR_REPEATER_CAPABILITIES_REPORT (0x02)<br>|
|Number of IR Code identifers for learning|Number of IR Code identifers for learning|Number of IR Code identifers for learning|Number of IR Code identifers for learning|Number of IR Code identifers for learning|Number of IR Code identifers for learning|Number of IR Code identifers for learning|Number of IR Code identifers for learning|
|IRR|LCR|RLC|PES|BES|Duty Cycle bitmask|Duty Cycle bitmask|Duty Cycle bitmask|
|Carrier|Carrier|Carrier|Carrier|Carrier|Carrier|Carrier|Carrier|
|Minimum Sub Carrier|Minimum Sub Carrier|Minimum Sub Carrier|Minimum Sub Carrier|Minimum Sub Carrier|Minimum Sub Carrier|Minimum Sub Carrier|Minimum Sub Carrier|
|Maximum Sub Carrier|Maximum Sub Carrier|Maximum Sub Carrier|Maximum Sub Carrier|Maximum Sub Carrier|Maximum Sub Carrier|Maximum Sub Carrier|Maximum Sub Carrier|
|Minimum Pulse time unit (MSB)|Minimum Pulse time unit (MSB)|Minimum Pulse time unit (MSB)|Minimum Pulse time unit (MSB)|Minimum Pulse time unit (MSB)|Minimum Pulse time unit (MSB)|Minimum Pulse time unit (MSB)|Minimum Pulse time unit (MSB)|
|Minimum Pulse time unit (LSB)|Minimum Pulse time unit (LSB)|Minimum Pulse time unit (LSB)|Minimum Pulse time unit (LSB)|Maximum Pulse time unit (MSB)|Maximum Pulse time unit (MSB)|Maximum Pulse time unit (MSB)|Maximum Pulse time unit (MSB)|
|Maximum Pulse time unit (LSB)|Maximum Pulse time unit (LSB)|Maximum Pulse time unit (LSB)|Maximum Pulse time unit (LSB)|Maximum Pulse time unit (LSB)|Maximum Pulse time unit (LSB)|Maximum Pulse time unit (LSB)|Maximum Pulse time unit (LSB)|



**Reserved** **/** **Res**

This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.

**Number** **of** **IR** **Code** **identifiers** **for** **learning** **(8** **bits)**

This field indicates how many slots the sending node supports for learning and repeating IR Codes.


The value 0 MUST indicate that the no code can be learned and repeated.


Values in the range 1..255 MUST indicate the number of codes that can be learnt and repeated.


A node advertising a value greater than 0 MUST support the following commands:


 - IR Repeater IR Code Learning Start Command


 - IR Repeater IR Code Learning Stop Command


 - IR Repeater IR Code Learning Status Command


 - IR Repeater Learnt IR Code Remove Command


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 246




<!-- PAGE 248 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


 - IR Repeater Learnt IR Code Get Command


 - IR Repeater Learnt IR Code Report Command

A node advertising a value greater than 0 MUST set the _LCR_ field and/or _RLC_ field to 1.


**IRR** **(IR** **Repeater** **Repeat** **Command)** **(1** **bit)**

This field indicates if the nodes supports the following commands:


 - IR Repeater Repeat Command


The value 0 MUST indicate that the commands above are not supported.


The value 1 MUST indicate that the commands above are supported.


**LCR** **(Learnt** **Code** **Readback)** **(1** **bit)**

This field indicates if the supporting node can be read back learnt codes, so that a controlling node
can read back current learnt codes. This field indicates if the nodes supports the following commands:


 - IR Repeater Learnt IR Code Readback Get Command


 - IR Repeater Learnt IR Code Readback Report Command


The value 0 MUST indicate that the commands above are not supported.


The value 1 MUST indicate that the commands above are supported.

If this field is set to 1, the _Number_ _of_ _IR_ _Code_ _Identifiers_ _for_ _learning_ field MUST be set to a value
greater than 0.

If this field is set to 1, the _IRR_ field MUST also be set to 1.


**RLC** **(Repeat** **Learnt** **Code)** **(1** **bit)**

This field indicates if the supporting node can be repeat learnt codes. This field indicates if the nodes
supports the following commands:


 - IR Repeater Repeat Learnt Code Command


The value 0 MUST indicate that the command above is not supported.


The value 1 MUST indicate that the command above is supported.

If this field is set to 1, the _Number_ _of_ _IR_ _Code_ _Identifiers_ _for_ _learning_ field MUST be set to a value
greater than 0.

If this field is set to 1, the _IRR_ field MUST also be set to 1.


**PES** **(Pulse** **Encoding** **Support)** **(1** **bit)**

This field indicates if the supporting node supports Pulse Encoding of the repeat and/or learn codes.


The value 0 MUST indicate that Pulse Encoding of IR signals is not supported.


The value 1 MUST indicate that Pulse Encoding of IR signals is supported.

If this field is set to 0, the _BES_ field MUST be set to 1.


**BES** **(Bit** **Encoding** **Support)** **(1** **bit)**

This field indicates if the supporting node supports Bit Encoding of the repeat and/or learn codes.


The value 0 MUST indicate that Bit Encoding of IR signals is not supported.


The value 1 MUST indicate that Bit Encoding of IR signals is supported.

If this field is set to 0, the _PES_ field MUST be set to 1.

If this field is set to 1, the sending node MUST support the following commands:

 - IR Repeater Configuration Set Command

 - IR Repeater Configuration Get Command

 - IR Repeater Configuration Report Command.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 247




<!-- PAGE 249 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**Duty** **Cycle** **bitmask** **(3** **bits)**

This field is used to advertise the supported Duty Cycles.

This field MUST be treated as a bitmask and encoded as follows:

 - Bit 0 in Duty Cycle field MUST represent ‘1/2 Duty Cycle’.

 - Bit 1 in Duty Cycle field MUST represent ‘1/3 Duty Cycle’.

 - Bit 2 in Duty Cycle field MUST represent ‘1/4 Duty Cycle’.


If a Duty Cycle is supported, the corresponding bit MUST be set to ‘1’.


If a Duty Cycle is not supported, the corresponding bit MUST be set to ‘0’.


**Carrier** **(8** **bits)**

This field is used to indicate the IR Carrier that the supporting node will use for repeating IR Codes
indicated when receiving the IR Repeater Repeat Command.

This field MUST be expressed as 820 + x nm (nanometers). The values 0x00..0xFF MUST represents
820nm..1075nm.


**Minimum** **Sub** **Carrier** **(8** **bits)**

This field MUST indicates the lower limit value that can be set at the supporting node in the IR
Repeater Repeat Command for the _Sub_ _Carrier_ field.

This field MUST be expressed in kHz (kilo Hertz).


**Maximum** **Sub** **Carrier** **(8** **bits)**

This field MUST indicates the upper limit value that can be set at the supporting node in the IR
Repeater Repeat Command for the _Sub_ _Carrier_ field.

This field MUST be expressed in kHz (kilo Hertz).


**Minimum** **Pulse** **time** **Unit** **(12** **bits)**

This field MUST indicates the lower limit value that can be set at the supporting node in the IR
Repeater IR Code Learning Start Command and IR Repeater Repeat Command for the _Pulse_ _time_
_unit_ field.

If the _PES_ field is set to 0, this field MUST set to 0.


**Maximum** **Pulse** **time** **Unit** **(12** **bits)**

This field MUST indicates the upper limit value that can be set at the supporting node in the IR
Repeater IR Code Learning Start Command and IR Repeater Repeat Command for the _Pulse_ _time_
_unit_ field.

If the _PES_ field is set to 0, this field MUST set to 0.


**2.2.50.3** **IR** **Repeater** **IR** **Code** **Learning** **Start** **Command**


This command is used to instruct a supporting node to start learning an IR Code.

This command MUST be ignored by a receiving node if it advertises 0 _Number_ _of_ _IR_ _Code_ _identifiers_
_for_ _learning_ in the IR Repeater Capabilities Report Command.


A supporting node MUST stop learning IR Code and return a IR Repeater IR Code Learning Status
Command a when a code has been received/learnt.


This command MUST be ignored if the supporting node is already learning an IR code.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 248




<!-- PAGE 250 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Table 2.290: IR Repeater IR Code Learning Start Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|
|Command = IR_REPEATER_IR_CODE_LEARNING_START (0x03)<br>|Command = IR_REPEATER_IR_CODE_LEARNING_START (0x03)<br>|Command = IR_REPEATER_IR_CODE_LEARNING_START (0x03)<br>|Command = IR_REPEATER_IR_CODE_LEARNING_START (0x03)<br>|Command = IR_REPEATER_IR_CODE_LEARNING_START (0x03)<br>|Command = IR_REPEATER_IR_CODE_LEARNING_START (0x03)<br>|Command = IR_REPEATER_IR_CODE_LEARNING_START (0x03)<br>|Command = IR_REPEATER_IR_CODE_LEARNING_START (0x03)<br>|
|IR Code identifer|IR Code identifer|IR Code identifer|IR Code identifer|IR Code identifer|IR Code identifer|IR Code identifer|IR Code identifer|
|Timeout|Timeout|Timeout|Timeout|Timeout|Timeout|Timeout|Timeout|
|Reserved|Reserved|Reserved|Reserved|Pulse time unit (MSB)|Pulse time unit (MSB)|Pulse time unit (MSB)|Pulse time unit (MSB)|
|Pulse time unit (LSB)|Pulse time unit (LSB)|Pulse time unit (LSB)|Pulse time unit (LSB)|Pulse time unit (LSB)|Pulse time unit (LSB)|Pulse time unit (LSB)|Pulse time unit (LSB)|



**IR** **Code** **identifier** **(8** **bits)**

This field indicates which IR Code identifier to use for storing the IR Code that will be learnt.

Values in the range 1..255 MUST indicate the actual IR Code identifier to use for learning a new code.

This command MUST be ignored if this field is set to 0 or a larger value than the _Number_ _of_ _IR_ _Code_
_identifiers_ _for_ _learning_ field advertised in the IR Repeater Capabilities Report Command.


**Timeout** **(8** **bits)**

This field is used to indicate how long the supporting node MUST wait for an IR code to learn.

If no IR code is learnt within the time in seconds indicated by this field, a supporting node MUST
stop learning codes and return a IR Repeater IR Code Learning Status Command with the _status_
field set to 0x02 (Failed:timeout).


**Pulse** **time** **unit** **(12** **bits)**

This field is used to configure the IR Code learning Pulse Encoding time unit.

This field MUST be expressed in (µs) and be in the range 1..4096.


Values lower than the _Minimum Pulse time_ unit advertised by the supporting node in the IR Repeater
Capabilities Report Command MUST be ignored by a supporting node.


Values higher than the _Maximum Pulse time_ unit advertised by the supporting node in the IR Repeater
Capabilities Report Command MUST be ignored by a supporting node.


**2.2.50.4** **IR** **Repeater** **IR** **Code** **Learning** **Stop** **Command**


This command is used to instruct a supporting node to stop learning an IR Code.

This command MUST be ignored by a receiving node if it advertises 0 Number of _IR_ _Code_ _identifiers_
_for_ _learning_ in the IR Repeater Capabilities Report Command.


A supporting node MUST stop learning IR Code if a learning process was ongoing when this command
is received.


A supporting node MUST return a IR Repeater IR Code Learning Status Command in response to
this command.


Table 2.291: IR Repeater IR Code Learning Stop Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|
|Command = IR_REPEATER_IR_CODE_LEARNING_STOP (0x04)|Command = IR_REPEATER_IR_CODE_LEARNING_STOP (0x04)|Command = IR_REPEATER_IR_CODE_LEARNING_STOP (0x04)|Command = IR_REPEATER_IR_CODE_LEARNING_STOP (0x04)|Command = IR_REPEATER_IR_CODE_LEARNING_STOP (0x04)|Command = IR_REPEATER_IR_CODE_LEARNING_STOP (0x04)|Command = IR_REPEATER_IR_CODE_LEARNING_STOP (0x04)|Command = IR_REPEATER_IR_CODE_LEARNING_STOP (0x04)|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 249




<!-- PAGE 251 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.50.5** **IR** **Repeater** **IR** **Code** **Learning** **Status** **Command**


This command is used to report the status of the last IR Code learning operation. It MUST be issued
by a supporting node when it stops learning IR Codes.


Table 2.292: IR Repeater IR Code Learning Status Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|
|Command = IR_REPEATER_IR_CODE_LEARNING_STATUS (0x05)<br>|Command = IR_REPEATER_IR_CODE_LEARNING_STATUS (0x05)<br>|Command = IR_REPEATER_IR_CODE_LEARNING_STATUS (0x05)<br>|Command = IR_REPEATER_IR_CODE_LEARNING_STATUS (0x05)<br>|Command = IR_REPEATER_IR_CODE_LEARNING_STATUS (0x05)<br>|Command = IR_REPEATER_IR_CODE_LEARNING_STATUS (0x05)<br>|Command = IR_REPEATER_IR_CODE_LEARNING_STATUS (0x05)<br>|Command = IR_REPEATER_IR_CODE_LEARNING_STATUS (0x05)<br>|
|IR Code identifer|IR Code identifer|IR Code identifer|IR Code identifer|IR Code identifer|IR Code identifer|IR Code identifer|IR Code identifer|
|Status|Status|Status|Status|Status|Status|Status|Status|



**IR** **Code** **identifier** **(8** **bits)**

This field indicates which IR Code identifier has been used for storing the IR Code during IR Code
learning.

If a learning process was completed, interrupted or timed out, this field MUST be in the range 1..255
and MUST be set to the same value as the _IR_ _Code_ _identifier_ field of the IR Repeater IR Code
Learning Start Command that initiated IR Code learning.


If a no learning process was ongoing and a IR Repeater IR Code Learning Stop Command was received,
this field MUST be set to 0.


**Status(8** **bit)**

This field is used to indicate the status of the IR Code learning operation. This field MUST encoded
according to Table 2.293.


Table 2.293: IR Code Learning Status::Status encoding

|Value|Description|
|---|---|
|0x00|**Failed: Learning bufer overfow**<br>The node learning bufer is too small to learnt the entire IR Code.|
|0x01|**Failed: Forced learning stop**<br>The node has received an IR Repeater IR Code Learning Stop Command<br>before any code was learnt|
|0x02|**Failed: timeout**<br>The node has timed out and did not learn any code|
|0xFF|**Success**<br>A new code was learnt.|



**2.2.50.6** **IR** **Repeater** **Learnt** **IR** **Code** **Remove** **Command**


This command is used to instruct a supporting node to erase a previously learnt an IR Code.

This command MUST be ignored by a receiving node if it advertises 0 _Number_ _of_ _IR_ _Code_ _identifiers_
_for_ _learning_ in the IR Repeater Capabilities Report Command.


Table 2.294: IR Repeater Learnt IR Code Remove Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|
|Command = IR_REPEATER_LEARNT_IR_CODE_REMOVE (0x06)<br>|Command = IR_REPEATER_LEARNT_IR_CODE_REMOVE (0x06)<br>|Command = IR_REPEATER_LEARNT_IR_CODE_REMOVE (0x06)<br>|Command = IR_REPEATER_LEARNT_IR_CODE_REMOVE (0x06)<br>|Command = IR_REPEATER_LEARNT_IR_CODE_REMOVE (0x06)<br>|Command = IR_REPEATER_LEARNT_IR_CODE_REMOVE (0x06)<br>|Command = IR_REPEATER_LEARNT_IR_CODE_REMOVE (0x06)<br>|Command = IR_REPEATER_LEARNT_IR_CODE_REMOVE (0x06)<br>|
|IR Code identifer|IR Code identifer|IR Code identifer|IR Code identifer|IR Code identifer|IR Code identifer|IR Code identifer|IR Code identifer|



**IR** **Code** **identifier** **(2** **bytes)**

This field indicates which IR Code identifier to erase.

Values in the range 1..255 MUST indicate the actual IR Code identifier that MUST be erased by the
supporting node.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 250




<!-- PAGE 252 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


The value 0 MUST indicate to erase all IR codes.

This command MUST be ignored if this field is set to a larger value than the _Number_ _of_ _IR_ _Code_
_identifiers_ _for_ _learning_ field advertised in the IR Repeater Capabilities Report Command.


**2.2.50.7** **IR** **Repeater** **Learnt** **IR** **Code** **Get** **Command**


This command is used to request a supporting node which IR Code identifiers have a valid IR Code
learnt.

This command MUST be ignored by a receiving node if it advertises 0 _Number_ _of_ _IR_ _Code_ _identifiers_
_for_ _learning_ in the IR Repeater Capabilities Report Command.


The IR Repeater Learnt IR Code Report Command MUST be returned in response to this command
if it was not ignored.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 2.295: IR Repeater Learnt IR Code Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|
|Command = IR_REPEATER_LEARNT_IR_CODE_GET (0x07)|Command = IR_REPEATER_LEARNT_IR_CODE_GET (0x07)|Command = IR_REPEATER_LEARNT_IR_CODE_GET (0x07)|Command = IR_REPEATER_LEARNT_IR_CODE_GET (0x07)|Command = IR_REPEATER_LEARNT_IR_CODE_GET (0x07)|Command = IR_REPEATER_LEARNT_IR_CODE_GET (0x07)|Command = IR_REPEATER_LEARNT_IR_CODE_GET (0x07)|Command = IR_REPEATER_LEARNT_IR_CODE_GET (0x07)|



**2.2.50.8** **IR** **Repeater** **Learnt** **IR** **Code** **Report** **Command**


This command is used to advertise the current IR learnt code stored at the supporting node.


Table 2.296: IR Repeater Learnt IR Code Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|
|Command = IR_REPEATER_LEARNT_IR_CODE_REPORT (0x08)<br>|Command = IR_REPEATER_LEARNT_IR_CODE_REPORT (0x08)<br>|Command = IR_REPEATER_LEARNT_IR_CODE_REPORT (0x08)<br>|Command = IR_REPEATER_LEARNT_IR_CODE_REPORT (0x08)<br>|Command = IR_REPEATER_LEARNT_IR_CODE_REPORT (0x08)<br>|Command = IR_REPEATER_LEARNT_IR_CODE_REPORT (0x08)<br>|Command = IR_REPEATER_LEARNT_IR_CODE_REPORT (0x08)<br>|Command = IR_REPEATER_LEARNT_IR_CODE_REPORT (0x08)<br>|
|Reserved<br>|Reserved<br>|Reserved<br>|IR Code identifer status length<br>|IR Code identifer status length<br>|IR Code identifer status length<br>|IR Code identifer status length<br>|IR Code identifer status length<br>|
|IR Code identifer status bitmask 1|IR Code identifer status bitmask 1|IR Code identifer status bitmask 1|IR Code identifer status bitmask 1|IR Code identifer status bitmask 1|IR Code identifer status bitmask 1|IR Code identifer status bitmask 1|IR Code identifer status bitmask 1|
|…<br>|…<br>|…<br>|…<br>|…<br>|…<br>|…<br>|…<br>|
|IR Code identifer status bitmask N|IR Code identifer status bitmask N|IR Code identifer status bitmask N|IR Code identifer status bitmask N|IR Code identifer status bitmask N|IR Code identifer status bitmask N|IR Code identifer status bitmask N|IR Code identifer status bitmask N|



**IR** **Code** **identifier** **status** **length** **(5** **bits)**

This field is used to indicate the length in bytes of the _IR_ _Code_ _identifier_ _status_ _bitmask_ field.

This field MUST be set to the minimum value which allows advertising all IR Code currently set at
the supporting node.

**IR** **Code** **identifier** **status** **bitmask** **(N** **bytes)**

This field advertises the supported IR Code identifier status values. The length of this field in bytes
MUST match the value advertised in the _IR_ _Code_ _Identifier_ _Status_ _Length_ field.

This field MUST be encoded as a bitmask:

 - Bit 0 in Bit Mask 1 represents IR Code Identifier 0x01.

 - Bit 1 in Bit Mask 1 represents IR Code Identifier 0x02.


 - …

If an IR Code is stored for the IR Code Identifier, the corresponding bit MUST be set to ‘1’.

If no IR Code is stored for the IR Code Identifier, the corresponding bit MUST be set to ‘0’.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 251




<!-- PAGE 253 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Only IR Codes with their bit set to ‘1’ can be repeated with the IR Repeater Repeat Learnt Code
Command


**2.2.50.9** **IR** **Repeater** **Learnt** **IR** **Code** **Readback** **Get** **Command**


This command is used to request a supporting node has learnt an IR Code to return the code details
to a controlling node.


This command MUST be ignored by a receiving node if it advertises no support for _LCR_ _(Learnt_
_Code_ _Readback)_ in the IR Repeater Capabilities Report Command.


The IR Repeater Learnt IR Code Report Command MUST be returned in response to this command
if it was not ignored.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 2.297: IR Repeater Learnt IR Code Readback Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|
|Command = IR_REPEATER_LEARNT_IR_CODE_READBACK_GET (0x09)<br>|Command = IR_REPEATER_LEARNT_IR_CODE_READBACK_GET (0x09)<br>|Command = IR_REPEATER_LEARNT_IR_CODE_READBACK_GET (0x09)<br>|Command = IR_REPEATER_LEARNT_IR_CODE_READBACK_GET (0x09)<br>|Command = IR_REPEATER_LEARNT_IR_CODE_READBACK_GET (0x09)<br>|Command = IR_REPEATER_LEARNT_IR_CODE_READBACK_GET (0x09)<br>|Command = IR_REPEATER_LEARNT_IR_CODE_READBACK_GET (0x09)<br>|Command = IR_REPEATER_LEARNT_IR_CODE_READBACK_GET (0x09)<br>|
|IR Code identifer status length|IR Code identifer status length|IR Code identifer status length|IR Code identifer status length|IR Code identifer status length|IR Code identifer status length|IR Code identifer status length|IR Code identifer status length|
|Res|Report Number (MSB)|Report Number (MSB)|Report Number (MSB)|Report Number (MSB)|Report Number (MSB)|Report Number (MSB)|Report Number (MSB)|
|Report Number (LSB)|Report Number (LSB)|Report Number (LSB)|Report Number (LSB)|Report Number (LSB)|Report Number (LSB)|Report Number (LSB)|Report Number (LSB)|



**IR** **Code** **identifier** **(8** **bits)**

This field is used to indicate the IR Code identifier that the supporting node MUST return in response
to this command.

A supporting node receiving a not supported IR Code Identifier or current unset/empty IR Code
Identifier MUST return a report with _Report_ _Number_ set to 0, Last set to 1 and no Data block field.


**Report** **Number** **(15** **bits)**

This field indicates the data block sequence number of the requested Learnt IR Code. The first data
block MUST be identified by the Report Number value 1.

If this field is set to 0 or a value higher than the total number of reports (indicated with the _last_ field
in the report), a supporting node MUST return a report with no _Data_ _block_ field.


**2.2.50.10** **IR** **Repeater** **Learnt** **IR** **Code** **Readback** **Report** **Command**


This command is used to advertise the “contents” of a Learn IR Code.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 252




<!-- PAGE 254 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Table 2.298: IR Repeater Learnt IR Code Readback Report Com
|7|Table 2. mand 6|.298: IR Repe 5|eater Learnt 4|IR Code Rea 3|adback Repor 2|rt Com- 1|0|
|---|---|---|---|---|---|---|---|
|**7**|**6**|**5**|**4**|**3**|**2**|**1**|**0**|
|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|
|Command = IR_REPEATER_LEARNT_IR_CODE_READBACK_REPORT (0x0A)<br>|Command = IR_REPEATER_LEARNT_IR_CODE_READBACK_REPORT (0x0A)<br>|Command = IR_REPEATER_LEARNT_IR_CODE_READBACK_REPORT (0x0A)<br>|Command = IR_REPEATER_LEARNT_IR_CODE_READBACK_REPORT (0x0A)<br>|Command = IR_REPEATER_LEARNT_IR_CODE_READBACK_REPORT (0x0A)<br>|Command = IR_REPEATER_LEARNT_IR_CODE_READBACK_REPORT (0x0A)<br>|Command = IR_REPEATER_LEARNT_IR_CODE_READBACK_REPORT (0x0A)<br>|Command = IR_REPEATER_LEARNT_IR_CODE_READBACK_REPORT (0x0A)<br>|
|IR Code identifer|IR Code identifer|IR Code identifer|IR Code identifer|IR Code identifer|IR Code identifer|IR Code identifer|IR Code identifer|
|Sub Carrier|Sub Carrier|Sub Carrier|Sub Carrier|Sub Carrier|Sub Carrier|Sub Carrier|Sub Carrier|
|Reserved|Reserved|Duty Cycle|Duty Cycle|Pulse time unit (MSB)|Pulse time unit (MSB)|Pulse time unit (MSB)|Pulse time unit (MSB)|
|Pulse time unit (LSB)|Pulse time unit (LSB)|Pulse time unit (LSB)|Pulse time unit (LSB)|Pulse time unit (LSB)|Pulse time unit (LSB)|Pulse time unit (LSB)|Pulse time unit (LSB)|
|Last|Report Number (MSB)|Report Number (MSB)|Report Number (MSB)|Report Number (MSB)|Report Number (MSB)|Report Number (MSB)|Report Number (MSB)|
|Report Number (LSB)|Report Number (LSB)|Report Number (LSB)|Report Number (LSB)|Report Number (LSB)|Report Number (LSB)|Report Number (LSB)|Report Number (LSB)|
|Data block type 1|Data block type 1|Data block length 1|Data block length 1|Data block length 1|Data block length 1|Data block length 1|Data block length 1|
|Data block value 1, 1|Data block value 1, 1|Data block value 1, 1|Data block value 1, 1|Data block value 1, 1|Data block value 1, 1|Data block value 1, 1|Data block value 1, 1|
|…|…|…|…|…|…|…|…|
|Data block value 1, N|Data block value 1, N|Data block value 1, N|Data block value 1, N|Data block value 1, N|Data block value 1, N|Data block value 1, N|Data block value 1, N|
|…|…|…|…|…|…|…|…|
|Data block type M|Data block type M|Data block length M|Data block length M|Data block length M|Data block length M|Data block length M|Data block length M|
|Data block value M, 1|Data block value M, 1|Data block value M, 1|Data block value M, 1|Data block value M, 1|Data block value M, 1|Data block value M, 1|Data block value M, 1|
|…|…|…|…|…|…|…|…|
|Data block value M, N|Data block value M, N|Data block value M, N|Data block value M, N|Data block value M, N|Data block value M, N|Data block value M, N|Data block value M, N|



**IR** **Code** **identifier** **(8** **bits)**

This field is used to indicate the IR Code identifier that the supporting node is currently sending.


**Sub** **Carrier** **(8** **bits)**

For field description, refer to Section 2.2.50.15 IR Repeater Repeat Command


**Duty** **Cycle** **(2** **bits)**

For field description, refer to Section 2.2.50.15 IR Repeater Repeat Command


**Pulse** **time** **unit** **(12** **bits)**

For field description, refer to Section 2.2.50.15 IR Repeater Repeat Command


**Report** **Number(15** **bits)**

For field description, refer to Section 2.2.50.15 IR Repeater Repeat Command


**Last** **(1** **bit)**

For field description, refer to Section 2.2.50.15 IR Repeater Repeat Command


**Data** **block** **type** **(2** **bits)**

For field description, refer to Section 2.2.50.15 IR Repeater Repeat Command


**Data** **Block** **Length** **(5** **bits)**

For field description, refer to Section 2.2.50.15 IR Repeater Repeat Command


**Data** **Block** **value** **(N** **bytes)**

For field description, refer to Section 2.2.50.15 IR Repeater Repeat Command


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 253




<!-- PAGE 255 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.50.11** **IR** **Repeater** **Configuration** **Set** **Command**


This command is used to configure the IR signal properties before the supporting node would repeat
IR Codes.


This command MUST be ignored by a receiving node if it advertises no support for Bit Encoding
Support (BES) in the IR Repeater Capabilities Report Command.

A supporting node MUST have a default bit 1, bit 0 and period configured after reset.


Table 2.299: IR Repeater Configuration Set Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|
|Command = IR_REPEATER_CONFIGURATION_SET (0x0B)|Command = IR_REPEATER_CONFIGURATION_SET (0x0B)|Command = IR_REPEATER_CONFIGURATION_SET (0x0B)|Command = IR_REPEATER_CONFIGURATION_SET (0x0B)|Command = IR_REPEATER_CONFIGURATION_SET (0x0B)|Command = IR_REPEATER_CONFIGURATION_SET (0x0B)|Command = IR_REPEATER_CONFIGURATION_SET (0x0B)|Command = IR_REPEATER_CONFIGURATION_SET (0x0B)|
|Period (MSB)|Period (MSB)|Period (MSB)|Period (MSB)|Period (MSB)|Period (MSB)|Period (MSB)|Period (MSB)|
|Reserved|Reserved|Reserved|Reserved|Period (LSB)|Period (LSB)|Period (LSB)|Period (LSB)|
|Data bit 0 encoding length (MSB)|Data bit 0 encoding length (MSB)|Data bit 0 encoding length (MSB)|Data bit 0 encoding length (MSB)|Data bit 0 encoding length (MSB)|Data bit 0 encoding length (MSB)|Data bit 0 encoding length (MSB)|Data bit 0 encoding length (MSB)|
|Data bit 0 encoding length (LSB)|Data bit 0 encoding length (LSB)|Data bit 0 encoding length (LSB)|Data bit 0 encoding length (LSB)|Data bit 0 encoding length (LSB)|Data bit 0 encoding length (LSB)|Data bit 0 encoding length (LSB)|Data bit 0 encoding length (LSB)|
|Data bit 0 encoding 1|Data bit 0 encoding 1|Data bit 0 encoding 1|Data bit 0 encoding 1|Data bit 0 encoding 1|Data bit 0 encoding 1|Data bit 0 encoding 1|Data bit 0 encoding 1|
|…|…|…|…|…|…|…|…|
|Data bit 0 encoding N|Data bit 0 encoding N|Data bit 0 encoding N|Data bit 0 encoding N|Data bit 0 encoding N|Data bit 0 encoding N|Data bit 0 encoding N|Data bit 0 encoding N|
|Data bit 1 encoding length (MSB)|Data bit 1 encoding length (MSB)|Data bit 1 encoding length (MSB)|Data bit 1 encoding length (MSB)|Data bit 1 encoding length (MSB)|Data bit 1 encoding length (MSB)|Data bit 1 encoding length (MSB)|Data bit 1 encoding length (MSB)|
|Data bit 1 encoding length (LSB)|Data bit 1 encoding length (LSB)|Data bit 1 encoding length (LSB)|Data bit 1 encoding length (LSB)|Data bit 1 encoding length (LSB)|Data bit 1 encoding length (LSB)|Data bit 1 encoding length (LSB)|Data bit 1 encoding length (LSB)|
|Data bit 1 encoding 1|Data bit 1 encoding 1|Data bit 1 encoding 1|Data bit 1 encoding 1|Data bit 1 encoding 1|Data bit 1 encoding 1|Data bit 1 encoding 1|Data bit 1 encoding 1|
|…|…|…|…|…|…|…|…|
|Data bit 1 encoding M|Data bit 1 encoding M|Data bit 1 encoding M|Data bit 1 encoding M|Data bit 1 encoding M|Data bit 1 encoding M|Data bit 1 encoding M|Data bit 1 encoding M|



**Period** **(12** **bits)**

This field is used to indicate the time period used for data bit encoding.

This field MUST be expressed in micro seconds (µs). This field MUST be in the range 1..4096


**Data** **bit** **‘0’** **encoding** **length** **(2** **bytes)**

This field is used to indicate the length in **bits** of the _Data_ _bit_ _‘0’_ _encoding_ field.

This field MUST be set to the exact number of bits to be interpreted from the _Data_ _bit_ _‘0’_ _encoding_
field.

This field MUST be ignored by a supporting node if the _BES_ field is set to 0 in the IR Repeater
Capabilities Report Command.


**Data** **bit** **‘0’** **encoding** **(N** **bytes)**

This field advertises the Hi/Low polarization encoding to apply to encode a 0 in an IR Code using
the IR Repeater Repeat Command and IR Repeater Learnt IR Code Readback Report Command.

This field MUST be ignored by a supporting node if the _BES_ field is set to 0 in the IR Repeater
Capabilities Report Command.

The length of this field MUST be the minimum amount of full bytes allowing to have the number of
bits indicated in the the _Data_ _bit_ _‘0’_ _encoding_ _Length_ field. .e.g if the _Data_ _bit_ _‘0’_ _encoding_ field is set
to 13, this field MUST be 2 bytes long.


Bits MUST be encoded as follows:


 - The value 0 MUST indicate a Low polarization


 - The value 1 MUST indicate a High polarization

The whole sequence indicated in this field MUST be repeated by a supporting node when receiving a
IR Repeater Repeat Command indicating to repeat a bit 0.


**Data** **bit** **‘1’** **encoding** **length** **(2** **bytes)**

This field is used to indicate the length in **bits** of the Data bit ‘1’ encoding field.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 254




<!-- PAGE 256 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


This field MUST be set to the exact number of bits to be interpreted from the _Data_ _bit_ _‘1’_ _encoding_
field.

This field MUST be ignored by a supporting node if the _BES_ field is set to 0 in the IR Repeater
Capabilities Report Command.


**Data** **bit** **‘1’** **encoding** **(N** **bytes)**

This field advertisesthe Hi/Low polarization encoding to apply to encode a 1 in an IR Code using the
IR Repeater Repeat Command and IR Repeater Learnt IR Code Readback Report Command.

This field MUST be ignored by a supporting node if the _BES_ field is set to 0 in the IR Repeater
Capabilities Report Command.

The length of this field MUST be the minimum amount of full bytes allowing to have the number of
bits indicated in the the _Data_ _bit_ _‘1’_ _encoding_ _Length_ field. .e.g if the _Data_ _bit_ _‘1’_ _encoding_ field is set
to 13, this field MUST be 2 bytes long.


Bits MUST be encoded as follows:


 - The value 0 MUST indicate a Low polarization


 - The value 1 MUST indicate a High polarization

The whole sequence indicated in this field MUST be repeated by a supporting node when receiving a
IR Repeater Repeat Command indicating to repeat a bit 1.


**2.2.50.12** **IR** **Repeater** **Configuration** **Get** **Command**


This command is used to request the IR signal configuration at the supporting node.

The IR Repeater Configuration Report Command MUST be returned in response to this command.


This command MUST be ignored by a receiving node if it advertises no support for _Bit_ _Encoding_
_Support_ _(BES)_ in the IR Repeater Capabilities Report Command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 2.300: IR Repeater Configuration Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|
|Command = IR_REPEATER_CONFIGURATION_GET (0x0C)|Command = IR_REPEATER_CONFIGURATION_GET (0x0C)|Command = IR_REPEATER_CONFIGURATION_GET (0x0C)|Command = IR_REPEATER_CONFIGURATION_GET (0x0C)|Command = IR_REPEATER_CONFIGURATION_GET (0x0C)|Command = IR_REPEATER_CONFIGURATION_GET (0x0C)|Command = IR_REPEATER_CONFIGURATION_GET (0x0C)|Command = IR_REPEATER_CONFIGURATION_GET (0x0C)|



**2.2.50.13** **IR** **Repeater** **Configuration** **Report** **Command**


This command is used to advertise the current IR signal repeating configuration at the supporting
node.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 255




<!-- PAGE 257 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Table 2.301: IR Repeater Configuration Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|
|Command = IR_REPEATER_CONFIGURATION_REPORT (0x0D)|Command = IR_REPEATER_CONFIGURATION_REPORT (0x0D)|Command = IR_REPEATER_CONFIGURATION_REPORT (0x0D)|Command = IR_REPEATER_CONFIGURATION_REPORT (0x0D)|Command = IR_REPEATER_CONFIGURATION_REPORT (0x0D)|Command = IR_REPEATER_CONFIGURATION_REPORT (0x0D)|Command = IR_REPEATER_CONFIGURATION_REPORT (0x0D)|Command = IR_REPEATER_CONFIGURATION_REPORT (0x0D)|
|Period (MSB)|Period (MSB)|Period (MSB)|Period (MSB)|Period (MSB)|Period (MSB)|Period (MSB)|Period (MSB)|
|Reserved|Reserved|Reserved|Reserved|Period (LSB)|Period (LSB)|Period (LSB)|Period (LSB)|
|Data bit 0 encoding length (MSB)|Data bit 0 encoding length (MSB)|Data bit 0 encoding length (MSB)|Data bit 0 encoding length (MSB)|Data bit 0 encoding length (MSB)|Data bit 0 encoding length (MSB)|Data bit 0 encoding length (MSB)|Data bit 0 encoding length (MSB)|
|Data bit 0 encoding length (LSB)|Data bit 0 encoding length (LSB)|Data bit 0 encoding length (LSB)|Data bit 0 encoding length (LSB)|Data bit 0 encoding length (LSB)|Data bit 0 encoding length (LSB)|Data bit 0 encoding length (LSB)|Data bit 0 encoding length (LSB)|
|Data bit 0 encoding 1|Data bit 0 encoding 1|Data bit 0 encoding 1|Data bit 0 encoding 1|Data bit 0 encoding 1|Data bit 0 encoding 1|Data bit 0 encoding 1|Data bit 0 encoding 1|
|…|…|…|…|…|…|…|…|
|Data bit 0 encoding N|Data bit 0 encoding N|Data bit 0 encoding N|Data bit 0 encoding N|Data bit 0 encoding N|Data bit 0 encoding N|Data bit 0 encoding N|Data bit 0 encoding N|
|Data bit 1 encoding length (MSB)|Data bit 1 encoding length (MSB)|Data bit 1 encoding length (MSB)|Data bit 1 encoding length (MSB)|Data bit 1 encoding length (MSB)|Data bit 1 encoding length (MSB)|Data bit 1 encoding length (MSB)|Data bit 1 encoding length (MSB)|
|Data bit 1 encoding length (LSB)|Data bit 1 encoding length (LSB)|Data bit 1 encoding length (LSB)|Data bit 1 encoding length (LSB)|Data bit 1 encoding length (LSB)|Data bit 1 encoding length (LSB)|Data bit 1 encoding length (LSB)|Data bit 1 encoding length (LSB)|
|Data bit 1 encoding 1|Data bit 1 encoding 1|Data bit 1 encoding 1|Data bit 1 encoding 1|Data bit 1 encoding 1|Data bit 1 encoding 1|Data bit 1 encoding 1|Data bit 1 encoding 1|
|…|…|…|…|…|…|…|…|
|Data bit 1 encoding M|Data bit 1 encoding M|Data bit 1 encoding M|Data bit 1 encoding M|Data bit 1 encoding M|Data bit 1 encoding M|Data bit 1 encoding M|Data bit 1 encoding M|



For fields’ description, refer to Section 2.2.50.11 IR Repeater Configuration Set Command


**2.2.50.14** **IR** **Repeater** **Repeat** **Learnt** **Code** **Command**


This command is used to request the receiving node to send an IR Code.


Table 2.302: IR Repeater Repeat Learnt Code Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|
|Command = IR_REPEATER_REPEAT_LEARNT_CODE (0x0E)<br>|Command = IR_REPEATER_REPEAT_LEARNT_CODE (0x0E)<br>|Command = IR_REPEATER_REPEAT_LEARNT_CODE (0x0E)<br>|Command = IR_REPEATER_REPEAT_LEARNT_CODE (0x0E)<br>|Command = IR_REPEATER_REPEAT_LEARNT_CODE (0x0E)<br>|Command = IR_REPEATER_REPEAT_LEARNT_CODE (0x0E)<br>|Command = IR_REPEATER_REPEAT_LEARNT_CODE (0x0E)<br>|Command = IR_REPEATER_REPEAT_LEARNT_CODE (0x0E)<br>|
|IR Code identifer|IR Code identifer|IR Code identifer|IR Code identifer|IR Code identifer|IR Code identifer|IR Code identifer|IR Code identifer|



**IR** **Code** **identifier** **(8** **bits)**

This field indicates which learnt IR Code identifier to repeat.

Values in the range 1..255 MUST indicate the actual IR Code identifier to use for repeating the learnt
code.

This command MUST be ignored if this field is set to 0, if no IR Code is learnt for the received
Identifier or if this field is set to a larger value than the _Number_ _of_ _IR_ _Code_ _identifiers_ _for_ _learning_
field advertised in the IR Repeater Capabilities Report Command.

A supporting node MUST repeat the IR code if a code has been learnt for the actual IR Code identifier.


**2.2.50.15** **IR** **Repeater** **Repeat** **Command**


This command is used to request the receiving node to send/repeat an IR Code.


This command MUST be ignored if the supporting node advertises no support for IR Code Repeating
_(IRR)_ in the IR Repeater Capabilities Report Command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 256




<!-- PAGE 258 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Table 2.303: IR Repeater Repeat Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|Command Class = COMMAND_CLASS_IR_REPEATER (0xA0)|
|Command = IR_REPEATER_REPEAT (0x0F)|Command = IR_REPEATER_REPEAT (0x0F)|Command = IR_REPEATER_REPEAT (0x0F)|Command = IR_REPEATER_REPEAT (0x0F)|Command = IR_REPEATER_REPEAT (0x0F)|Command = IR_REPEATER_REPEAT (0x0F)|Command = IR_REPEATER_REPEAT (0x0F)|Command = IR_REPEATER_REPEAT (0x0F)|
|Sequence number|Sequence number|Sequence number|Sequence number|Sequence number|Sequence number|Sequence number|Sequence number|
|Sub Carrier|Sub Carrier|Sub Carrier|Sub Carrier|Sub Carrier|Sub Carrier|Sub Carrier|Sub Carrier|
|Reserved|Reserved|Duty Cycle|Duty Cycle|Pulse time unit (MSB)|Pulse time unit (MSB)|Pulse time unit (MSB)|Pulse time unit (MSB)|
|Pulse time unit (LSB)|Pulse time unit (LSB)|Pulse time unit (LSB)|Pulse time unit (LSB)|Pulse time unit (LSB)|Pulse time unit (LSB)|Pulse time unit (LSB)|Pulse time unit (LSB)|
|Last|Report Number (MSB)|Report Number (MSB)|Report Number (MSB)|Report Number (MSB)|Report Number (MSB)|Report Number (MSB)|Report Number (MSB)|
|Report Number (LSB)|Report Number (LSB)|Report Number (LSB)|Report Number (LSB)|Report Number (LSB)|Report Number (LSB)|Report Number (LSB)|Report Number (LSB)|
|Data block type 1|Data block type 1|Data block length 1|Data block length 1|Data block length 1|Data block length 1|Data block length 1|Data block length 1|
|Data block value 1, 1|Data block value 1, 1|Data block value 1, 1|Data block value 1, 1|Data block value 1, 1|Data block value 1, 1|Data block value 1, 1|Data block value 1, 1|
|…|…|…|…|…|…|…|…|
|Data block value 1, N|Data block value 1, N|Data block value 1, N|Data block value 1, N|Data block value 1, N|Data block value 1, N|Data block value 1, N|Data block value 1, N|
|…|…|…|…|…|…|…|…|
|Data block type M|Data block type M|Data block length M|Data block length M|Data block length M|Data block length M|Data block length M|Data block length M|
|Data block value M, 1|Data block value M, 1|Data block value M, 1|Data block value M, 1|Data block value M, 1|Data block value M, 1|Data block value M, 1|Data block value M, 1|
|…|…|…|…|…|…|…|…|
|Data block value M, N|Data block value M, N|Data block value M, N|Data block value M, N|Data block value M, N|Data block value M, N|Data block value M, N|Data block value M, N|



**Sequence** **number** **(8** **bits)**

This field is used to keep track of the command that initiated the IR Repeat Command.


**Sub** **carrier** **(8** **bits)**

This field is used to indicate the IR Sub carrier that the supporting node MUST use for repeating IR
Codes.

This field MUST be expressed in kHz (kiloHertz).


**Duty** **cycle** **(2** **bits)**

This field is used to indicate the IR Carrier that the supporting node MUST use for repeating IR
Codes.

This field MUST be encoded according to Table 2.304.


Table 2.304: IR Repeater Repeat::Duty Cycle encoding

|Value|Description|
|---|---|
|0x00|1/2 Duty Cycle|
|0x01|1/3 Duty Cycle|
|0x02|1/4 Duty Cycle|
|0x03|_Reserved_|



Values not advertised as supported in the IR Repeater Capabilities Report Command MUST be
ignored by a supporting node.


**Pulse** **time** **unit** **(12** **bits)**

This field is used to interpret the data blocks using Pulse Encoding type.

This field MUST be expressed in (µs) and be in the range 1..4096.


Values lower than the _Minimum Pulse Time Unit_ advertised by the supporting node in the IR Repeater
Capabilities Report Command MUST be ignored by a supporting node.


Values higher than the _Maximum_ _Pulse_ _Time_ _Unit_ advertised by the supporting node in the IR
Repeater Capabilities Report Command MUST be ignored by a supporting node.


**Report** **number** **(15** **bits)**


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 257




<!-- PAGE 259 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


A sending node typically needs several report commands to describe or encode an entire IR Code.
This field is used to indicate the current report number being issued. The first report MUST have
this field set to 1 and incremented at every new unique report Command.


A receiving node MUST reassemble the IR Code by concatenating the data blocks of each repeat
command.

Data block 1,1 of the first report MUST represent the beginning of the IR Code signal and data block
M,N of the last report MUST represent the end of the IR Code signal.


**Last** **(1** **bit)**

This field is used to indicate that this is the Last report.


The value 0 MUST indicate that this is not the last report and more are to follow.


The value 1 MUST indicate that this is the last report and the supporting node MUST start repeating
the IR Code.


**Data** **block** **type** **(2** **bits)**

This field indicates how to interpret the corresponding Data block Value field.


 - 0 : bit encoding (0/1)


 - 1 : pulse encoding


**Data** **block** **length** **(6** **bits)**

This field indicates the length in bytes of the corresponding Data block Value field.


**Data** **block** **value** **(6** **bits)**

This field MUST interpreted according to the corresponding _Data_ _Block_ _Type_ field.

If the corresponding _Data_ _Block_ _Type_ field is set to 0, this field MUST be interpreted as follow:


Table 2.305: Data Block Value Field::Data Block Type = ‘0’


_Number_ _of_ _bits_ _(2_ _bytes)_

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Number of bits 1|Number of bits 1|Number of bits 1|Number of bits 1|Number of bits 1|Number of bits 1|Number of bits 1|Number of bits 1|
|Number of bits 2|Number of bits 2|Number of bits 2|Number of bits 2|Number of bits 2|Number of bits 2|Number of bits 2|Number of bits 2|
|Data bits 1|Data bits 1|Data bits 1|Data bits 1|Data bits 1|Data bits 1|Data bits 1|Data bits 1|
|…|…|…|…|…|…|…|…|
|Data bits L|Data bits L|Data bits L|Data bits L|Data bits L|Data bits L|Data bits L|Data bits L|


This subfield indicates how many bits to take from the _Data_ _bits_ subfield, starting from the LSB. For
example, if this subfield is set to 12, a receiving node MUST interpret the first byte and the bits 0..3
of the second byte as data bits.


_Data_ _bits_ _(L_ _bytes)_

This subfield is used to describe successive bits to be transmitted as part of the IR Code. Each
data bit (bit 0 or bit 1) MUST be repeated/interpreted according to the IR Configuration set at the
supporting node. (IR Repeater Configuration Set Command)

If the corresponding Data Block Type is set to 1, this field MUST be interpreted as follow:


Table 2.306: Data Block Value Field::Data Block Type = ‘1’

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Number of time units 1|Number of time units 1|Number of time units 1|Number of time units 1|Number of time units 1|Number of time units 1|Number of time units 1|Number of time units 1|
|…|…|…|…|…|…|…|…|
|Number of time units P|Number of time units P|Number of time units P|Number of time units P|Number of time units P|Number of time units P|Number of time units P|Number of time units P|



_Number_ _of_ _time_ _units_ _(8_ _bits)_


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 258




<!-- PAGE 260 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


This subfield MUST represent the amount of time to use for an IR code pulse. The time unit is set
in the _Pulse_ _time_ _unit_ field.

This field MUST be interpreted byte-by-byte. The first byte is the first to be interpreted. It represents
how long to transmit a Hi or Lo polarity.

The first byte (1) MUST represents a Hi Polarity.

If a byte of this field is in the range 0..255, it MUST be interpreted as a multiplier of the time unit.

If a byte of this field is in the range 0..254, the polarity MUST be toggled for the next byte (from Hi
to Lo or Lo to Hi)

If a byte of this field is set to 255, the polarity MUST be the same for the next byte (Hi stays Hi and
Lo stays Lo)If a byte of this field is set to 0, it must ignored. The value 0 can be used for example at
the first byte to start an IR Code with a Lo polarity.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 259