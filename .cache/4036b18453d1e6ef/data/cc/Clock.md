<!-- PAGE 142 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.26** **Clock** **Command** **Class,** **version** **1**


The Clock Command Class is used to implement a simple clock functionality.


**2.2.26.1** **Interoperability** **considerations**


CC:0081.01.00.32.001 A controlling node SHOULD configure the current time and weekday in a supporting node during
node commissioning.


It has been found that some version 1 nodes issue Clock Get Command to controllers in order to learn

the current time and use the returned Clock Report Command as a Clock Set Command.


CC:0081.01.00.32.002 A supporting node SHOULD NOT learn the current time with a Clock Get Command.


CC:0081.01.00.32.003 A node SHOULD control the Time Command Class to read the current time from supporting nodes
(time servers) or support the Clock Command Class and wait to be set the current time by a controlling
node.


CC:0081.01.00.32.004 A Z-Wave Plus node SHOULD issue a Clock Report Command via the Lifeline Association Group if
they suspect to have inaccurate time and/or weekdays (e.g. after battery removal).


CC:0081.01.00.32.005 A controlling node SHOULD compare the received time and weekday with its current time and set
the time again at the supporting node if a deviation is observed (e.g. different weekday or more than
a minute difference)


**2.2.26.2** **Multi** **Channel** **Considerations**


CC:0081.01.00.12.001 Multi Channel End Points SHOULD NOT support the Clock Command Class.


**2.2.26.3** **Clock** **Set** **Command**


This command is used to set the current time in a supporting node.


Table 2.134: Clock Set Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_CLOCK|Command Class = COMMAND_CLASS_CLOCK|Command Class = COMMAND_CLASS_CLOCK|Command Class = COMMAND_CLASS_CLOCK|Command Class = COMMAND_CLASS_CLOCK|Command Class = COMMAND_CLASS_CLOCK|Command Class = COMMAND_CLASS_CLOCK|Command Class = COMMAND_CLASS_CLOCK|
|Command = CLOCK_SET|Command = CLOCK_SET|Command = CLOCK_SET|Command = CLOCK_SET|Command = CLOCK_SET|Command = CLOCK_SET|Command = CLOCK_SET|Command = CLOCK_SET|
|Weekday|Weekday|Weekday|Hour|Hour|Hour|Hour|Hour|
|Minute|Minute|Minute|Minute|Minute|Minute|Minute|Minute|



**Weekday** **(3** **bits)**

CC:0081.01.04.11.001 This field is used to indicate the current weekday that the receiving node MUST assume.

CC:0081.01.04.11.002 This field MUST comply with Table 2.135.


Table 2.135: Clock Set Command::Weekday encoding

|Value|Description|
|---|---|
|0x00|Unused/unknown<br>This value may be specifed if the weekday is not used or not known|
|0x01|Monday|
|0x02|Tuesday|
|0x03|Wednesday|
|0x04|Thursday|
|0x05|Friday|
|0x06|Saturday|
|0x07|Sunday|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 141




<!-- PAGE 143 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**Hour** **(5** **bits)**

CC:0081.01.04.11.003 This field is used to indicate the hour of the current time that the receiving node MUST assume.

CC:0081.01.04.11.004 This field MUST be in the range 0..23.


**Minute** **(8** **bits)**

CC:0081.01.04.11.005 This field is used to indicate the minute of the current time that the receiving node MUST assume.

CC:0081.01.04.11.006 This field MUST be in the range 0..59.


CC:0081.01.04.12.001 A sending node knowing the current time with seconds precision SHOULD round its current time to
the nearest minute when sending this command.


**2.2.26.4** **Clock** **Get** **Command**


This command is used to request the current time set at a supporting node.


CC:0081.01.05.11.001 The Clock Report Command MUST be returned in response to this command.


CC:0081.01.05.11.002 This command MUST NOT be issued via multicast addressing.


CC:0081.01.05.11.003 A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 2.136: Clock Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_CLOCK|Command Class = COMMAND_CLASS_CLOCK|Command Class = COMMAND_CLASS_CLOCK|Command Class = COMMAND_CLASS_CLOCK|Command Class = COMMAND_CLASS_CLOCK|Command Class = COMMAND_CLASS_CLOCK|Command Class = COMMAND_CLASS_CLOCK|Command Class = COMMAND_CLASS_CLOCK|
|Command = CLOCK_GET|Command = CLOCK_GET|Command = CLOCK_GET|Command = CLOCK_GET|Command = CLOCK_GET|Command = CLOCK_GET|Command = CLOCK_GET|Command = CLOCK_GET|



**2.2.26.5** **Clock** **Report** **Command**


This command is used to advertise the current time set at the sending node.


Table 2.137: Clock Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_CLOCK|Command Class = COMMAND_CLASS_CLOCK|Command Class = COMMAND_CLASS_CLOCK|Command Class = COMMAND_CLASS_CLOCK|Command Class = COMMAND_CLASS_CLOCK|Command Class = COMMAND_CLASS_CLOCK|Command Class = COMMAND_CLASS_CLOCK|Command Class = COMMAND_CLASS_CLOCK|
|Command = CLOCK_REPORT|Command = CLOCK_REPORT|Command = CLOCK_REPORT|Command = CLOCK_REPORT|Command = CLOCK_REPORT|Command = CLOCK_REPORT|Command = CLOCK_REPORT|Command = CLOCK_REPORT|
|Weekday|Weekday|Weekday|Hour|Hour|Hour|Hour|Hour|
|Minute|Minute|Minute|Minute|Minute|Minute|Minute|Minute|



For fields’ description, refer to _Clock_ _Set_ _Command_

CC:0081.01.06.11.001 A sending node MUST comply with fields’ description from Clock Set Command


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 142