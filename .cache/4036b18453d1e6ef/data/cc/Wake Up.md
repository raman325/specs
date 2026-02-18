<!-- PAGE 790 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.46** **Wake** **Up** **Command** **Class,** **version** **1**


The Wake Up Command Class allows a battery-powered device to notify another device (always
listening), that it is awake and ready to receive any queued commands.


Figure 3.29: Wake Up Sequence


CC:0084.01.00.12.001 This Command Class SHOULD be implemented by battery powered devices. Wake Up Notification
commands SHOULD be handled immediately by the destination node in order to minimize battery
consumption.


**3.2.46.1** **Terminology**


The Wake Up period is defined as the period during which a Wake Up node is supposed to be awake
after issuing a Wake Up Notification Command to its Wake Up destination.

The Wake Up period starts when the supporting node issues a Wake Up Notification and it ends
either 10 seconds after the last received/transmitted frame or at the reception of a Wake Up No More
Information Command by the Wake Up destination.


**3.2.46.2** **Interoperability** **considerations**


CC:0084.01.00.31.001 The Wake Up Notification Command Class MUST NOT be covered by any association group. This
also means that the Wake Up Notification Command Class MUST NOT be covered by the Lifeline
association group.


CC:0084.01.00.32.001 A node sending periodical or triggered unsolicited commands at the same time it wakes up SHOULD
send the unsolicited commands before the Wake Up Notification Command.


CC:0084.01.00.32.002 A supporting node SHOULD NOT send unsolicited commands during the Wake Up period.


CC:0084.01.00.32.003 A supporting node having no Wake-Up destination set SHOULD fall back on the SIS NodeID (if any
present in the network) to issue Wake-Up Notifications.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 789




<!-- PAGE 791 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.46.3** **Wake** **Up** **Interval** **Set** **Command**


This command is used to configure the Wake Up interval and destination of a node.


Table 3.170: Wake Up Interval Set Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_WAKE_UP (0x84)|Command Class = COMMAND_CLASS_WAKE_UP (0x84)|Command Class = COMMAND_CLASS_WAKE_UP (0x84)|Command Class = COMMAND_CLASS_WAKE_UP (0x84)|Command Class = COMMAND_CLASS_WAKE_UP (0x84)|Command Class = COMMAND_CLASS_WAKE_UP (0x84)|Command Class = COMMAND_CLASS_WAKE_UP (0x84)|Command Class = COMMAND_CLASS_WAKE_UP (0x84)|
|Command = WAKE_UP_INTERVAL_SET (0x04)|Command = WAKE_UP_INTERVAL_SET (0x04)|Command = WAKE_UP_INTERVAL_SET (0x04)|Command = WAKE_UP_INTERVAL_SET (0x04)|Command = WAKE_UP_INTERVAL_SET (0x04)|Command = WAKE_UP_INTERVAL_SET (0x04)|Command = WAKE_UP_INTERVAL_SET (0x04)|Command = WAKE_UP_INTERVAL_SET (0x04)|
|Seconds 1 (MSB)|Seconds 1 (MSB)|Seconds 1 (MSB)|Seconds 1 (MSB)|Seconds 1 (MSB)|Seconds 1 (MSB)|Seconds 1 (MSB)|Seconds 1 (MSB)|
|Seconds 2|Seconds 2|Seconds 2|Seconds 2|Seconds 2|Seconds 2|Seconds 2|Seconds 2|
|Seconds 3 (LSB)|Seconds 3 (LSB)|Seconds 3 (LSB)|Seconds 3 (LSB)|Seconds 3 (LSB)|Seconds 3 (LSB)|Seconds 3 (LSB)|Seconds 3 (LSB)|
|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|



**Seconds** **(24** **bits)**

This field is used to specify the time in seconds between Wake Up periods for the receiving node.

CC:0084.01.04.11.001 The first byte MUST be the most significant byte.


CC:0084.01.04.11.002 Values in the range 1..16777215 MUST indicate the time between Wake Up periods.


The value 0 MUST indicate that the receiving node MUST Wake Up when initiated by an event
determined by the application e.g. a pushbutton activation.


**NodeID** **(8** **bits)**

This field is used to specify the Wake Up destination NodeID.


CC:0084.01.04.11.003 A receiving node MUST assume the indicated NodeID as Wake Up destination. i.e. the Wake Up
Notification Command MUST be sent to the NodeID specified in this field.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 790




<!-- PAGE 792 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.46.4** **Wake** **Up** **Interval** **Get** **Command**


This command is used to request the Wake Up Interval and destination of a node.


CC:0084.01.05.11.001 The _Wake_ _Up_ _Interval_ _Report_ _Command_ MUST be returned in response to this command.


CC:0084.01.05.11.002 This command MUST NOT be issued via multicast addressing.


CC:0084.01.05.11.003 A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 3.171: Wake Up Interval Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_WAKE_UP (0x84)|Command Class = COMMAND_CLASS_WAKE_UP (0x84)|Command Class = COMMAND_CLASS_WAKE_UP (0x84)|Command Class = COMMAND_CLASS_WAKE_UP (0x84)|Command Class = COMMAND_CLASS_WAKE_UP (0x84)|Command Class = COMMAND_CLASS_WAKE_UP (0x84)|Command Class = COMMAND_CLASS_WAKE_UP (0x84)|Command Class = COMMAND_CLASS_WAKE_UP (0x84)|
|Command = WAKE_UP_INTERVAL_GET (0x05)|Command = WAKE_UP_INTERVAL_GET (0x05)|Command = WAKE_UP_INTERVAL_GET (0x05)|Command = WAKE_UP_INTERVAL_GET (0x05)|Command = WAKE_UP_INTERVAL_GET (0x05)|Command = WAKE_UP_INTERVAL_GET (0x05)|Command = WAKE_UP_INTERVAL_GET (0x05)|Command = WAKE_UP_INTERVAL_GET (0x05)|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 791




<!-- PAGE 793 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.46.5** **Wake** **Up** **Interval** **Report** **Command**


This command is used to advertise the current Wake Up interval and destination.


Table 3.172: Wake Up Interval Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_WAKE_UP (0x84)|Command Class = COMMAND_CLASS_WAKE_UP (0x84)|Command Class = COMMAND_CLASS_WAKE_UP (0x84)|Command Class = COMMAND_CLASS_WAKE_UP (0x84)|Command Class = COMMAND_CLASS_WAKE_UP (0x84)|Command Class = COMMAND_CLASS_WAKE_UP (0x84)|Command Class = COMMAND_CLASS_WAKE_UP (0x84)|Command Class = COMMAND_CLASS_WAKE_UP (0x84)|
|Command = WAKE_UP_INTERVAL_REPORT (0x06)|Command = WAKE_UP_INTERVAL_REPORT (0x06)|Command = WAKE_UP_INTERVAL_REPORT (0x06)|Command = WAKE_UP_INTERVAL_REPORT (0x06)|Command = WAKE_UP_INTERVAL_REPORT (0x06)|Command = WAKE_UP_INTERVAL_REPORT (0x06)|Command = WAKE_UP_INTERVAL_REPORT (0x06)|Command = WAKE_UP_INTERVAL_REPORT (0x06)|
|Seconds 1 (MSB)|Seconds 1 (MSB)|Seconds 1 (MSB)|Seconds 1 (MSB)|Seconds 1 (MSB)|Seconds 1 (MSB)|Seconds 1 (MSB)|Seconds 1 (MSB)|
|Seconds 2|Seconds 2|Seconds 2|Seconds 2|Seconds 2|Seconds 2|Seconds 2|Seconds 2|
|Seconds 3 (LSB)|Seconds 3 (LSB)|Seconds 3 (LSB)|Seconds 3 (LSB)|Seconds 3 (LSB)|Seconds 3 (LSB)|Seconds 3 (LSB)|Seconds 3 (LSB)|
|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|



**Seconds** **(24** **bits)**

This field is used to advertise the time in seconds between Wake Up periods at the sending node.

CC:0084.01.06.11.001 The first byte MUST be the most significant byte.


CC:0084.01.06.11.002 Values in the range 1..16777215 MUST indicate the time between Wake Up periods.


The value 0 MUST indicate that the receiving node MUST Wake Up when initiated by an event
determined by the application e.g. a pushbutton activation.


**NodeID** **(8** **bits)**

This field is used to advertise the Wake Up destination NodeID configured at the sending node.


CC:0084.01.06.11.003
The sending node MUST send the Wake Up Notification Commands to the advertised NodeID in this
field.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 792




<!-- PAGE 794 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.46.6** **Wake** **Up** **Notification** **Command**


This command allows a node to notify its Wake Up destination that it is awake.


CC:0084.01.07.12.001 The sending node SHOULD start a timer allowing it power down again in case no Wake Up No

CC:0084.01.07.11.001 More Information Command is received. If implemented, the timer MUST comply with the timing
requirements defined in the Z-Wave Plus Device Types Specification (Section 8, Section 7).


CC:0084.01.07.13.001 A non-securely included node MAY send this command as broadcast if no Wake Up destination
NodeID is configured.


CC:0084.01.07.11.002 A receiving node MUST NOT return a _Wake_ _Up_ _No_ _More_ _Information_ _Command_ in response to

CC:0084.01.07.12.002 this command issued via broadcast. Upon receiving this command via broadcast, a receiving node
SHOULD configure a relevant Wake Up destination issuing a Wake Up Interval Set Command to the
node that issued this command via broadcast.


Table 3.173: Wake Up Notification Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_WAKE_UP (0x84)|Command Class = COMMAND_CLASS_WAKE_UP (0x84)|Command Class = COMMAND_CLASS_WAKE_UP (0x84)|Command Class = COMMAND_CLASS_WAKE_UP (0x84)|Command Class = COMMAND_CLASS_WAKE_UP (0x84)|Command Class = COMMAND_CLASS_WAKE_UP (0x84)|Command Class = COMMAND_CLASS_WAKE_UP (0x84)|Command Class = COMMAND_CLASS_WAKE_UP (0x84)|
|Command = WAKE_UP_NOTIFICATION (0x07)|Command = WAKE_UP_NOTIFICATION (0x07)|Command = WAKE_UP_NOTIFICATION (0x07)|Command = WAKE_UP_NOTIFICATION (0x07)|Command = WAKE_UP_NOTIFICATION (0x07)|Command = WAKE_UP_NOTIFICATION (0x07)|Command = WAKE_UP_NOTIFICATION (0x07)|Command = WAKE_UP_NOTIFICATION (0x07)|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 793




<!-- PAGE 795 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.46.7** **Wake** **Up** **No** **More** **Information** **Command**


CC:0084.01.08.13.001 This command is used to notify a supporting node that it MAY return to sleep to minimize power
consumption.


CC:0084.01.08.12.001 A node receiving the Wake Up No More Information Command SHOULD return a MAC layer Ack
frame for the Wake Up No More Information Command before returning to sleep. Not acknowledging
the command will cause a number of retransmissions.


CC:0084.01.08.12.002 It is RECOMMENDED that the handling of the Wake Up No More Information Command and
the associated time window for MAC layer acknowledgement is left to the protocol layer in order to
simplify application design.


Table 3.174: Wake Up No More Information Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_WAKE_UP (0x84)|Command Class = COMMAND_CLASS_WAKE_UP (0x84)|Command Class = COMMAND_CLASS_WAKE_UP (0x84)|Command Class = COMMAND_CLASS_WAKE_UP (0x84)|Command Class = COMMAND_CLASS_WAKE_UP (0x84)|Command Class = COMMAND_CLASS_WAKE_UP (0x84)|Command Class = COMMAND_CLASS_WAKE_UP (0x84)|Command Class = COMMAND_CLASS_WAKE_UP (0x84)|
|Command = WAKE_UP_NO_MORE_INFORMATION (0x08)|Command = WAKE_UP_NO_MORE_INFORMATION (0x08)|Command = WAKE_UP_NO_MORE_INFORMATION (0x08)|Command = WAKE_UP_NO_MORE_INFORMATION (0x08)|Command = WAKE_UP_NO_MORE_INFORMATION (0x08)|Command = WAKE_UP_NO_MORE_INFORMATION (0x08)|Command = WAKE_UP_NO_MORE_INFORMATION (0x08)|Command = WAKE_UP_NO_MORE_INFORMATION (0x08)|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 794

---

<!-- PAGE 796 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.47** **Wake** **Up** **Command** **Class,** **version** **2**


The Wake Up Command Class version 2 enables read back of the Wake Up Interval capabilities in a
node.


**3.2.47.1** **Compatibility** **considerations**


CC:0084.02.00.21.001 A node supporting Wake Up Command Class, version 2 MUST also support Wake Up Command
Class, version 1.


All commands not mentioned in this version remain unchanged from the Wake Up Command Class,
version 1.


A version 2 supporting node may receive a Wake Up Interval Set outside the range of supported
CC:0084.02.00.22.001 intervals from a version 1 controlling node. A version 2 supporting node SHOULD NOT ignore a
Wake Up Interval Set with an invalid time period and set the Wake Up Interval to a supported value.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 795




<!-- PAGE 797 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.47.2** **Wake** **Up** **Interval** **Set** **Command**


The Wake Up Interval Set Command is used to configure the wake up interval of a device and the
NodeID of the device receiving the Wake Up Notification Command.


Table 3.175: Wake Up Interval Set Command, version 2

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_WAKE_UP (0x84)|Command Class = COMMAND_CLASS_WAKE_UP (0x84)|Command Class = COMMAND_CLASS_WAKE_UP (0x84)|Command Class = COMMAND_CLASS_WAKE_UP (0x84)|Command Class = COMMAND_CLASS_WAKE_UP (0x84)|Command Class = COMMAND_CLASS_WAKE_UP (0x84)|Command Class = COMMAND_CLASS_WAKE_UP (0x84)|Command Class = COMMAND_CLASS_WAKE_UP (0x84)|
|Command = WAKE_UP_INTERVAL_SET (0x04)|Command = WAKE_UP_INTERVAL_SET (0x04)|Command = WAKE_UP_INTERVAL_SET (0x04)|Command = WAKE_UP_INTERVAL_SET (0x04)|Command = WAKE_UP_INTERVAL_SET (0x04)|Command = WAKE_UP_INTERVAL_SET (0x04)|Command = WAKE_UP_INTERVAL_SET (0x04)|Command = WAKE_UP_INTERVAL_SET (0x04)|
|Seconds 1 (MSB)|Seconds 1 (MSB)|Seconds 1 (MSB)|Seconds 1 (MSB)|Seconds 1 (MSB)|Seconds 1 (MSB)|Seconds 1 (MSB)|Seconds 1 (MSB)|
|Seconds 2|Seconds 2|Seconds 2|Seconds 2|Seconds 2|Seconds 2|Seconds 2|Seconds 2|
|Seconds 3 (LSB)|Seconds 3 (LSB)|Seconds 3 (LSB)|Seconds 3 (LSB)|Seconds 3 (LSB)|Seconds 3 (LSB)|Seconds 3 (LSB)|Seconds 3 (LSB)|
|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|



All fields not described below remain unchanged from version 1


**Seconds** **(24** **bits)**

This field is used to specify the time in seconds between Wake Up periods for the receiving node.

CC:0084.02.04.11.001 The first byte MUST be the most significant byte.


CC:0084.02.04.11.002 Values in the range 1..16777215 MUST indicate the time between Wake Up periods.


The value 0 MUST indicate that the receiving node MUST Wake Up when initiated by an event
determined by the application e.g. a pushbutton activation.


CC:0084.02.04.11.003 A receiving node MUST accept any interval value within the interval limits advertised by the Wake
Up Interval Capabilities Report Command.

CC:0084.02.04.12.001 A receiving node SHOULD NOT ignore this command if this field contains a non-valid value and it
SHOULD apply the following:



CC:0084.02.04.12.002


CC:0084.02.04.12.003




If the received value is higher than the minimum valid value (advertised in the Wake Up Interval
Capabilities Report Command), the receiving node SHOULD round down the value to the next
valid value but SHOULD NOT set it to 0 if 0 is the minimum value.

- If the value specified in this field is lower than the minimum valid value, the receiving node
SHOULD apply the minimum valid value.



CC:0084.02.04.12.004 A receiving node SHOULD accept the value 0, even if the Minimum Wake Up Interval advertised by
the Wake Up Interval Capabilities Report Command is larger than 0. If accepted, the value 0 MUST
disable the timer-based transmission of Wake Up Notification Commands.

CC:0084.02.04.12.005 The node SHOULD be able to issue a Wake Up Notification in response to some local activation, e.g.
a button press.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 796




<!-- PAGE 798 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.47.3** **Wake** **Up** **Interval** **Capabilities** **Get** **Command**


This command is used to request the Wake Up Interval capabilities of a node.


CC:0084.02.09.11.001 The Wake Up Interval Capabilities Report Command MUST be returned in response to this command.


CC:0084.02.09.11.002 This command MUST NOT be issued via multicast addressing.


CC:0084.02.09.11.003 A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 3.176: Wake Up Interval Capabilities Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_WAKE_UP (0x84)|Command Class = COMMAND_CLASS_WAKE_UP (0x84)|Command Class = COMMAND_CLASS_WAKE_UP (0x84)|Command Class = COMMAND_CLASS_WAKE_UP (0x84)|Command Class = COMMAND_CLASS_WAKE_UP (0x84)|Command Class = COMMAND_CLASS_WAKE_UP (0x84)|Command Class = COMMAND_CLASS_WAKE_UP (0x84)|Command Class = COMMAND_CLASS_WAKE_UP (0x84)|
|Command = WAKE_UP_INTERVAL_CAPABILITIES_GET (0x09)|Command = WAKE_UP_INTERVAL_CAPABILITIES_GET (0x09)|Command = WAKE_UP_INTERVAL_CAPABILITIES_GET (0x09)|Command = WAKE_UP_INTERVAL_CAPABILITIES_GET (0x09)|Command = WAKE_UP_INTERVAL_CAPABILITIES_GET (0x09)|Command = WAKE_UP_INTERVAL_CAPABILITIES_GET (0x09)|Command = WAKE_UP_INTERVAL_CAPABILITIES_GET (0x09)|Command = WAKE_UP_INTERVAL_CAPABILITIES_GET (0x09)|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 797




<!-- PAGE 799 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.47.4** **Wake** **Up** **Interval** **Capabilities** **Report** **Command**


This command is used to advertise the Wake Up Interval capabilities of a node.


Table 3.177: Wake Up Interval Capabilities Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_WAKE_UP (0x84)|Command Class = COMMAND_CLASS_WAKE_UP (0x84)|Command Class = COMMAND_CLASS_WAKE_UP (0x84)|Command Class = COMMAND_CLASS_WAKE_UP (0x84)|Command Class = COMMAND_CLASS_WAKE_UP (0x84)|Command Class = COMMAND_CLASS_WAKE_UP (0x84)|Command Class = COMMAND_CLASS_WAKE_UP (0x84)|Command Class = COMMAND_CLASS_WAKE_UP (0x84)|
|Command = WAKE_UP_INTERVAL_CAPABILITIES_REPORT (0x0A)|Command = WAKE_UP_INTERVAL_CAPABILITIES_REPORT (0x0A)|Command = WAKE_UP_INTERVAL_CAPABILITIES_REPORT (0x0A)|Command = WAKE_UP_INTERVAL_CAPABILITIES_REPORT (0x0A)|Command = WAKE_UP_INTERVAL_CAPABILITIES_REPORT (0x0A)|Command = WAKE_UP_INTERVAL_CAPABILITIES_REPORT (0x0A)|Command = WAKE_UP_INTERVAL_CAPABILITIES_REPORT (0x0A)|Command = WAKE_UP_INTERVAL_CAPABILITIES_REPORT (0x0A)|
|Minimum Wake Up Interval Seconds 1 (MSB)|Minimum Wake Up Interval Seconds 1 (MSB)|Minimum Wake Up Interval Seconds 1 (MSB)|Minimum Wake Up Interval Seconds 1 (MSB)|Minimum Wake Up Interval Seconds 1 (MSB)|Minimum Wake Up Interval Seconds 1 (MSB)|Minimum Wake Up Interval Seconds 1 (MSB)|Minimum Wake Up Interval Seconds 1 (MSB)|
|Minimum Wake Up Interval Seconds 2|Minimum Wake Up Interval Seconds 2|Minimum Wake Up Interval Seconds 2|Minimum Wake Up Interval Seconds 2|Minimum Wake Up Interval Seconds 2|Minimum Wake Up Interval Seconds 2|Minimum Wake Up Interval Seconds 2|Minimum Wake Up Interval Seconds 2|
|Minimum Wake Up Interval Seconds 3 (LSB)|Minimum Wake Up Interval Seconds 3 (LSB)|Minimum Wake Up Interval Seconds 3 (LSB)|Minimum Wake Up Interval Seconds 3 (LSB)|Minimum Wake Up Interval Seconds 3 (LSB)|Minimum Wake Up Interval Seconds 3 (LSB)|Minimum Wake Up Interval Seconds 3 (LSB)|Minimum Wake Up Interval Seconds 3 (LSB)|
|Maximum Wake Up Interval Seconds 1 (MSB)|Maximum Wake Up Interval Seconds 1 (MSB)|Maximum Wake Up Interval Seconds 1 (MSB)|Maximum Wake Up Interval Seconds 1 (MSB)|Maximum Wake Up Interval Seconds 1 (MSB)|Maximum Wake Up Interval Seconds 1 (MSB)|Maximum Wake Up Interval Seconds 1 (MSB)|Maximum Wake Up Interval Seconds 1 (MSB)|
|Maximum Wake Up Interval Seconds 2|Maximum Wake Up Interval Seconds 2|Maximum Wake Up Interval Seconds 2|Maximum Wake Up Interval Seconds 2|Maximum Wake Up Interval Seconds 2|Maximum Wake Up Interval Seconds 2|Maximum Wake Up Interval Seconds 2|Maximum Wake Up Interval Seconds 2|
|Maximum Wake Up Interval Seconds 3 (LSB)|Maximum Wake Up Interval Seconds 3 (LSB)|Maximum Wake Up Interval Seconds 3 (LSB)|Maximum Wake Up Interval Seconds 3 (LSB)|Maximum Wake Up Interval Seconds 3 (LSB)|Maximum Wake Up Interval Seconds 3 (LSB)|Maximum Wake Up Interval Seconds 3 (LSB)|Maximum Wake Up Interval Seconds 3 (LSB)|
|Default Wake Up Interval Seconds 1 (MSB)|Default Wake Up Interval Seconds 1 (MSB)|Default Wake Up Interval Seconds 1 (MSB)|Default Wake Up Interval Seconds 1 (MSB)|Default Wake Up Interval Seconds 1 (MSB)|Default Wake Up Interval Seconds 1 (MSB)|Default Wake Up Interval Seconds 1 (MSB)|Default Wake Up Interval Seconds 1 (MSB)|
|Default Wake Up Interval Seconds 2|Default Wake Up Interval Seconds 2|Default Wake Up Interval Seconds 2|Default Wake Up Interval Seconds 2|Default Wake Up Interval Seconds 2|Default Wake Up Interval Seconds 2|Default Wake Up Interval Seconds 2|Default Wake Up Interval Seconds 2|
|Default Wake Up Interval Seconds 3 (LSB)|Default Wake Up Interval Seconds 3 (LSB)|Default Wake Up Interval Seconds 3 (LSB)|Default Wake Up Interval Seconds 3 (LSB)|Default Wake Up Interval Seconds 3 (LSB)|Default Wake Up Interval Seconds 3 (LSB)|Default Wake Up Interval Seconds 3 (LSB)|Default Wake Up Interval Seconds 3 (LSB)|
|Wake Up Interval Step Seconds 1 (MSB)|Wake Up Interval Step Seconds 1 (MSB)|Wake Up Interval Step Seconds 1 (MSB)|Wake Up Interval Step Seconds 1 (MSB)|Wake Up Interval Step Seconds 1 (MSB)|Wake Up Interval Step Seconds 1 (MSB)|Wake Up Interval Step Seconds 1 (MSB)|Wake Up Interval Step Seconds 1 (MSB)|
|Wake Up Interval Step Seconds 2|Wake Up Interval Step Seconds 2|Wake Up Interval Step Seconds 2|Wake Up Interval Step Seconds 2|Wake Up Interval Step Seconds 2|Wake Up Interval Step Seconds 2|Wake Up Interval Step Seconds 2|Wake Up Interval Step Seconds 2|
|Wake Up Interval Step Seconds 3 (LSB)|Wake Up Interval Step Seconds 3 (LSB)|Wake Up Interval Step Seconds 3 (LSB)|Wake Up Interval Step Seconds 3 (LSB)|Wake Up Interval Step Seconds 3 (LSB)|Wake Up Interval Step Seconds 3 (LSB)|Wake Up Interval Step Seconds 3 (LSB)|Wake Up Interval Step Seconds 3 (LSB)|



CC:0084.02.0A.11.001 Byte 1 MUST be the most significant byte for all fields in this command.


**Minimum** **Wake** **Up** **Interval** **Seconds** **(24** **bits)**

CC:0084.02.0A.11.002 This field is used to advertise the minimum Wake Up Interval supported by the sending node. The
field MUST be in the range 0..16777215


CC:0084.02.0A.11.00B The value 0 MUST indicate that the receiving node MUST supports Wake Up when initiated by an
event determined by the application e.g. a pushbutton activation.


CC:0084.02.0A.11.00C Values in the range 1..16777215 MUST indicate Minimum supported Wake Up interval in seconds


**Maximum** **Wake** **Up** **Interval** **Seconds** **(24** **bits)**

This field is used to advertise the maximum Wake Up Interval supported by the sending node. The
CC:0084.02.0A.11.003 field MUST comply with Table 3.178.



CC:0084.02.0A.11.004


CC:0084.02.0A.11.005


CC:0084.02.0A.13.001



Table 3.178: Wake Up Interval Capabilities Report::Maximum
Wake Up Interval Seconds Encoding

|Decimal|Description|
|---|---|
|0|This value is used to indicate that there is no minimum / maximum /<br>default wake up interval. In this case, the sending node is activated by<br>e.g. user interaction in form of a button press.<br>If this feld is set to 0, the Minimum and Default Wake Up Interval felds<br>MUST also be 0.|
|<min<br>interval><br>..16777215|Values in this range indicate the maximum wake up interval in seconds<br>supported by the sending node.<br>This feld MUST NOT be set to a lower value than the Minimum Wake<br>Up Interval Seconds value.<br>This feld MAY be set to the same value as the Minimum Wake Up Interval<br>Seconds value, which means the sending node only supports one value.|



**Default** **Wake** **Up** **Interval** **Seconds** **(24** **bits)**

This field is used to advertise the default Wake Up Interval value for the sending node.



CC:0084.02.0A.12.006 This field MUST be set to a value included in the range defined by the Minimum Wake Up Interval
and the Maximum Wake Up Interval


CC:0084.02.0A.12.001 The Default Wake Up Interval SHOULD be 0 if the Minimum Wake Up Interval is 0.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 798




<!-- PAGE 800 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**Wake** **Up** **Interval** **Step** **Seconds** **(24** **bits)**

This field is used to advertise the resolution of valid Wake Up Intervals values for the sending node.
CC:0084.02.0A.11.007 The field MUST comply with Table 3.179.



CC:0084.02.0A.11.008


CC:0084.02.0A.11.009


CC:0084.02.0A.12.002


CC:0084.02.0A.11.00A



Table 3.179: Wake Up Interval Capabilities Report::Wake Up Interval Step Seconds Encoding

|Decimal|Description|
|---|---|
|0|This value is used to indicate that no interval steps are possible.<br>The battery-operated device only supports the minimum and maximum<br>Wake Up Interval values.<br>This feld MUST be set to 0 if the maximum and the minimum interval<br>are equal.|
|1..16777215|Values in this range indicate the Wake Up Interval step in seconds sup-<br>ported by the sending node.<br>This feld’s value MUST NOT exceed the diference between the Minimum<br>and Maximum Wake Up Intervals.<br>This feld SHOULD have a value so that the diference between the max-<br>imum and minimum Wake Up Interval is a multiple of this feld’s value.<br>_Examples_:<br>If a device has minimum wake up interval of 5 minutes (300 seconds) and<br>a maximum wake up interval of 10 minutes (600 seconds), the wake up<br>interval step MUST NOT exceed 5 minutes (300 seconds) as this would<br>be larger than the diference of the minimum and maximum interval. A<br>Wake Up Interval Step of 100 seconds indicates that the nodes supports<br>the following Wake Up Intervals :<br>300 seconds<br>400 seconds<br>500 seconds<br>600 seconds|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 799

---

<!-- PAGE 801 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.48** **Wake** **Up** **Command** **Class,** **version** **3**


The Wake Up Command Class, version 3 introduces the capability to request a wake up on demand
to supporting nodes during unsolicited communication.


The Wake Up Command Class, version 3 is backwards compatible with the Wake Up Command Class,
CC:0084.03.00.21.001 version 2. Fields and commands not described in this version MUST remain unchanged from version
2.


**3.2.48.1** **Wake** **Up** **Interval** **Capabilities** **Report** **Command**


This command is used to advertise the Wake Up capabilities of a supporting node.


Table 3.180: Wake Up Interval Capabilities Report Command, version 3

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_WAKE_UP (0x84)|Command Class = COMMAND_CLASS_WAKE_UP (0x84)|Command Class = COMMAND_CLASS_WAKE_UP (0x84)|Command Class = COMMAND_CLASS_WAKE_UP (0x84)|Command Class = COMMAND_CLASS_WAKE_UP (0x84)|Command Class = COMMAND_CLASS_WAKE_UP (0x84)|Command Class = COMMAND_CLASS_WAKE_UP (0x84)|Command Class = COMMAND_CLASS_WAKE_UP (0x84)|
|Command = WAKE_UP_INTERVAL_CAPABILITIES_REPORT (0x0A)|Command = WAKE_UP_INTERVAL_CAPABILITIES_REPORT (0x0A)|Command = WAKE_UP_INTERVAL_CAPABILITIES_REPORT (0x0A)|Command = WAKE_UP_INTERVAL_CAPABILITIES_REPORT (0x0A)|Command = WAKE_UP_INTERVAL_CAPABILITIES_REPORT (0x0A)|Command = WAKE_UP_INTERVAL_CAPABILITIES_REPORT (0x0A)|Command = WAKE_UP_INTERVAL_CAPABILITIES_REPORT (0x0A)|Command = WAKE_UP_INTERVAL_CAPABILITIES_REPORT (0x0A)|
|Minimum Wake Up Interval Seconds 1 (MSB)|Minimum Wake Up Interval Seconds 1 (MSB)|Minimum Wake Up Interval Seconds 1 (MSB)|Minimum Wake Up Interval Seconds 1 (MSB)|Minimum Wake Up Interval Seconds 1 (MSB)|Minimum Wake Up Interval Seconds 1 (MSB)|Minimum Wake Up Interval Seconds 1 (MSB)|Minimum Wake Up Interval Seconds 1 (MSB)|
|Minimum Wake Up Interval Seconds 2|Minimum Wake Up Interval Seconds 2|Minimum Wake Up Interval Seconds 2|Minimum Wake Up Interval Seconds 2|Minimum Wake Up Interval Seconds 2|Minimum Wake Up Interval Seconds 2|Minimum Wake Up Interval Seconds 2|Minimum Wake Up Interval Seconds 2|
|Minimum Wake Up Interval Seconds 3 (LSB)|Minimum Wake Up Interval Seconds 3 (LSB)|Minimum Wake Up Interval Seconds 3 (LSB)|Minimum Wake Up Interval Seconds 3 (LSB)|Minimum Wake Up Interval Seconds 3 (LSB)|Minimum Wake Up Interval Seconds 3 (LSB)|Minimum Wake Up Interval Seconds 3 (LSB)|Minimum Wake Up Interval Seconds 3 (LSB)|
|Maximum Wake Up Interval Seconds 1 (MSB)|Maximum Wake Up Interval Seconds 1 (MSB)|Maximum Wake Up Interval Seconds 1 (MSB)|Maximum Wake Up Interval Seconds 1 (MSB)|Maximum Wake Up Interval Seconds 1 (MSB)|Maximum Wake Up Interval Seconds 1 (MSB)|Maximum Wake Up Interval Seconds 1 (MSB)|Maximum Wake Up Interval Seconds 1 (MSB)|
|Maximum Wake Up Interval Seconds 2|Maximum Wake Up Interval Seconds 2|Maximum Wake Up Interval Seconds 2|Maximum Wake Up Interval Seconds 2|Maximum Wake Up Interval Seconds 2|Maximum Wake Up Interval Seconds 2|Maximum Wake Up Interval Seconds 2|Maximum Wake Up Interval Seconds 2|
|Maximum Wake Up Interval Seconds 3 (LSB)|Maximum Wake Up Interval Seconds 3 (LSB)|Maximum Wake Up Interval Seconds 3 (LSB)|Maximum Wake Up Interval Seconds 3 (LSB)|Maximum Wake Up Interval Seconds 3 (LSB)|Maximum Wake Up Interval Seconds 3 (LSB)|Maximum Wake Up Interval Seconds 3 (LSB)|Maximum Wake Up Interval Seconds 3 (LSB)|
|Default Wake Up Interval Seconds 1 (MSB)|Default Wake Up Interval Seconds 1 (MSB)|Default Wake Up Interval Seconds 1 (MSB)|Default Wake Up Interval Seconds 1 (MSB)|Default Wake Up Interval Seconds 1 (MSB)|Default Wake Up Interval Seconds 1 (MSB)|Default Wake Up Interval Seconds 1 (MSB)|Default Wake Up Interval Seconds 1 (MSB)|
|Default Wake Up Interval Seconds 2|Default Wake Up Interval Seconds 2|Default Wake Up Interval Seconds 2|Default Wake Up Interval Seconds 2|Default Wake Up Interval Seconds 2|Default Wake Up Interval Seconds 2|Default Wake Up Interval Seconds 2|Default Wake Up Interval Seconds 2|
|Default Wake Up Interval Seconds 3 (LSB)|Default Wake Up Interval Seconds 3 (LSB)|Default Wake Up Interval Seconds 3 (LSB)|Default Wake Up Interval Seconds 3 (LSB)|Default Wake Up Interval Seconds 3 (LSB)|Default Wake Up Interval Seconds 3 (LSB)|Default Wake Up Interval Seconds 3 (LSB)|Default Wake Up Interval Seconds 3 (LSB)|
|Wake Up Interval Step Seconds 1 (MSB)|Wake Up Interval Step Seconds 1 (MSB)|Wake Up Interval Step Seconds 1 (MSB)|Wake Up Interval Step Seconds 1 (MSB)|Wake Up Interval Step Seconds 1 (MSB)|Wake Up Interval Step Seconds 1 (MSB)|Wake Up Interval Step Seconds 1 (MSB)|Wake Up Interval Step Seconds 1 (MSB)|
|Wake Up Interval Step Seconds 2|Wake Up Interval Step Seconds 2|Wake Up Interval Step Seconds 2|Wake Up Interval Step Seconds 2|Wake Up Interval Step Seconds 2|Wake Up Interval Step Seconds 2|Wake Up Interval Step Seconds 2|Wake Up Interval Step Seconds 2|
|Wake Up Interval Step Seconds 3 (LSB)|Wake Up Interval Step Seconds 3 (LSB)|Wake Up Interval Step Seconds 3 (LSB)|Wake Up Interval Step Seconds 3 (LSB)|Wake Up Interval Step Seconds 3 (LSB)|Wake Up Interval Step Seconds 3 (LSB)|Wake Up Interval Step Seconds 3 (LSB)|Wake Up Interval Step Seconds 3 (LSB)|
|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Wake Up on Demand<br>Support|



**Wake** **Up** **On** **Demand** **support** **(1** **bit)**

This field is used to advertise if the supporting node supports the Wake Up On Demand functionality.

CC:0084.03.0A.11.001 If this field is set to 0, the supporting node MUST NOT support the Wake Up On Demand functionality.

If this field is set to 1, the supporting node MUST support the Wake Up On Demand functionality.


CC:0084.03.0A.11.002 A node supporting the Wake Up On Demand functionality MUST support the Supervision Command
Class, version 2.

CC:0084.03.0A.11.003 A node supporting the Wake Up On Demand functionality MUST return a Wake Up Notification
Command if the Wake Up destination node issued a Supervision Report Command with the Wake
Up Request bit set to 1.

CC:0084.03.0A.11.004 A node supporting the Wake Up On Demand functionality MUST ignore the _Wake_ _Up_ _Request_ field
if the Supervision Report is not issued by the Wake Up Destination.

CC:0084.03.0A.11.005 A node issuing a Wake Up Notification Command after a Wake Up Request MUST restart its Wake
Up timer for the next Wake Up period.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 800




<!-- PAGE 802 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.48.1.1** **Wake** **Up** **On** **Demand** **functionality**


If the Wake Up destination has important messages to be transmitted to the Wake Up node, it can
use the Wake Up Request bit in the Supervision report when the sleeping node uses Supervision
encapsulation. An example frame flows is shown in Figure 3.30.


Figure 3.30: Wake Up Destination Initiates an On Demand Wake Up


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 801