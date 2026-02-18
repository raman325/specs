<!-- PAGE 102 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.12** **Barrier** **Operator** **Command** **Class,** **version** **1**


The Barrier Operator Command Class is used to control and query the status of motorized barriers.


**2.2.12.1** **Compatibility** **considerations**


CC:0066.01.00.23.001 A supporting node MAY ignore a Barrier Operator Command if the requested operation violates
operational limitations or safety regulations.


**2.2.12.1.1** **Node** **Information** **Frame** **(NIF)**


CC:0066.01.00.21.001 The Barrier Operator Command Class MUST be supported only using secure communication (S0
and/or S2 Command Class).


CC:0066.01.00.21.003 A supporting node MUST NOT advertise the Barrier Operator Command Class in its NIF after
network inclusion.


**2.2.12.1.2** **Command** **Class** **dependencies**


CC:0066.01.00.21.002 A node supporting the Barrier Operator Command Class MUST support the Notification Command
Class, version 4 or newer.


**2.2.12.2** **Barrier** **Operator** **Set** **Command**


This command is used to initiate an unattended change in state of the barrier.


CC:0066.01.01.13.001 A supporting node MAY ignore this command if the requested operation violates operational limitations or safety regulations.


Table 2.68: Barrier Operator Set Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_BARRIER_OPERATOR (0x66)|Command Class = COMMAND_CLASS_BARRIER_OPERATOR (0x66)|Command Class = COMMAND_CLASS_BARRIER_OPERATOR (0x66)|Command Class = COMMAND_CLASS_BARRIER_OPERATOR (0x66)|Command Class = COMMAND_CLASS_BARRIER_OPERATOR (0x66)|Command Class = COMMAND_CLASS_BARRIER_OPERATOR (0x66)|Command Class = COMMAND_CLASS_BARRIER_OPERATOR (0x66)|Command Class = COMMAND_CLASS_BARRIER_OPERATOR (0x66)|
|Command = BARRIER_OPERATOR_SET (0x01)|Command = BARRIER_OPERATOR_SET (0x01)|Command = BARRIER_OPERATOR_SET (0x01)|Command = BARRIER_OPERATOR_SET (0x01)|Command = BARRIER_OPERATOR_SET (0x01)|Command = BARRIER_OPERATOR_SET (0x01)|Command = BARRIER_OPERATOR_SET (0x01)|Command = BARRIER_OPERATOR_SET (0x01)|
|Target Value|Target Value|Target Value|Target Value|Target Value|Target Value|Target Value|Target Value|



**Target** **Value** **(8** **bits)**

CC:0066.01.01.11.001 This field MUST specify the intended state of the device.

CC:0066.01.01.11.002 The encoding of this field MUST be according to Table 2.69.


Table 2.69: Barrier Set::Target Value

|Target Value|Col2|Description|Version|
|---|---|---|---|
|0x00|CLOSE|Initiate unattended close|1|
|0xFF|OPEN|Initiate unattended open|1|



CC:0066.01.01.11.003 All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 101




<!-- PAGE 103 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Figure 2.5: Barrier Set, state transitions


CC:0066.01.01.11.004 A receiving node MUST comply with the allowed state changes and triggering commands specified in
Figure 2.5. Any state/command pair not specified in Figure 2.5 MUST NOT cause any action.


CC:0066.01.01.12.001 The receiving node SHOULD respond to OPEN and CLOSE commands. However, the receiving node

CC:0066.01.01.11.005 MUST NOT respond to OPEN or CLOSE commands if any safety issue is detected.


CC:0066.01.01.11.006 The receiving node MUST NOT respond to the CLOSE command unless it is in the “Open” state.


**2.2.12.2.1** **Error** **Handling**


CC:0066.01.01.11.007 The device MUST stop if any safety issue is detected.


CC:0066.01.01.11.008 If the requested operation is overruled by a safety mechanism, the device MUST notify the requester
via a Notification Report with the Notification {Access Control::Barrier unable to perform requested
operation due to UL requirements}.



CC:0066.01.01.11.009



If the requested operation is prohibited by the specific device class, e.g. SPECIFIC_TYPE_SECURE_BARRIER_OPEN_ONLY or SPECIFIC_TYPE_SECURE_BARRIER_CLOSE_ONLY,
the device MUST notify the requester by issuing an Application Rejected Request Command. The
Application Rejected Request Command is a member of the Application Status Command Class.


**2.2.12.3** **Barrier** **Operator** **Get** **Command**


This command is used to request the current state of a barrier operator device.



CC:0066.01.02.11.001 The Barrier Operator Report Command MUST be returned in response to this command.


CC:0066.01.02.11.002 This command MUST NOT be issued via multicast addressing.


CC:0066.01.02.11.003 A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 2.70: Barrier Operator Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_BARRIER_OPERATOR (0x66)|Command Class = COMMAND_CLASS_BARRIER_OPERATOR (0x66)|Command Class = COMMAND_CLASS_BARRIER_OPERATOR (0x66)|Command Class = COMMAND_CLASS_BARRIER_OPERATOR (0x66)|Command Class = COMMAND_CLASS_BARRIER_OPERATOR (0x66)|Command Class = COMMAND_CLASS_BARRIER_OPERATOR (0x66)|Command Class = COMMAND_CLASS_BARRIER_OPERATOR (0x66)|Command Class = COMMAND_CLASS_BARRIER_OPERATOR (0x66)|
|Command = BARRIER_OPERATOR_GET (0x02)|Command = BARRIER_OPERATOR_GET (0x02)|Command = BARRIER_OPERATOR_GET (0x02)|Command = BARRIER_OPERATOR_GET (0x02)|Command = BARRIER_OPERATOR_GET (0x02)|Command = BARRIER_OPERATOR_GET (0x02)|Command = BARRIER_OPERATOR_GET (0x02)|Command = BARRIER_OPERATOR_GET (0x02)|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 102




<!-- PAGE 104 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.12.4** **Barrier** **Operator** **Report** **Command**


This command is used to advertise the status of the barrier operator device.


Table 2.71: Barrier Operator Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_BARRIER_OPERATOR (0x66)|Command Class = COMMAND_CLASS_BARRIER_OPERATOR (0x66)|Command Class = COMMAND_CLASS_BARRIER_OPERATOR (0x66)|Command Class = COMMAND_CLASS_BARRIER_OPERATOR (0x66)|Command Class = COMMAND_CLASS_BARRIER_OPERATOR (0x66)|Command Class = COMMAND_CLASS_BARRIER_OPERATOR (0x66)|Command Class = COMMAND_CLASS_BARRIER_OPERATOR (0x66)|Command Class = COMMAND_CLASS_BARRIER_OPERATOR (0x66)|
|Command = BARRIER_OPERATOR_REPORT (0x03)|Command = BARRIER_OPERATOR_REPORT (0x03)|Command = BARRIER_OPERATOR_REPORT (0x03)|Command = BARRIER_OPERATOR_REPORT (0x03)|Command = BARRIER_OPERATOR_REPORT (0x03)|Command = BARRIER_OPERATOR_REPORT (0x03)|Command = BARRIER_OPERATOR_REPORT (0x03)|Command = BARRIER_OPERATOR_REPORT (0x03)|
|State|State|State|State|State|State|State|State|



**State** **(8** **bits)**

CC:0066.01.03.11.001 This field MUST advertise the current state of the device.

CC:0066.01.03.11.002 The encoding of this field MUST be according to Table 2.72.



Table 2.72: Barrier Report::State













|Value|State|Requirement|Description|Version|
|---|---|---|---|---|
|0x00|Closed|REQUIRED|The barrier is in the Closed position|1|
|0x01 …<br>0x63|Stopped<br>at<br>exact<br>Posi-<br>tion|RECOMMENDED|0x01 = 1% (Near Closed)<br>0x63 = 99% (Near Open)|1|
|0xFC|Closing|REQUIRED|The barrier is closing.<br>The current position is unknown.|1|
|0xFD|Stopped|REQUIRED|The barrier is stopped.<br>The current position is unknown.|1|
|0xFE|Opening|REQUIRED|The barrier is opening.<br>The current position is unknown.|1|
|0xFF|Open|REQUIRED|The barrier is in the Open position|1|


CC:0066.01.03.11.003 All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.


**2.2.12.5** **Barrier** **Operator** **Get** **Signaling** **Capabilities** **Supported** **Command**


This command is used to query a device for available subsystems which may be controlled via Z-Wave.


CC:0066.01.04.11.001 The Barrier Operator Report Signaling Capabilities Supported Command MUST be returned in response to this command.


CC:0066.01.04.11.002 This command MUST NOT be issued via multicast addressing.


CC:0066.01.04.11.003 A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 2.73: Barrier Operator Get Signaling Capabilities Supported
Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_BARRIER_OPERATOR (0x66)|Command Class = COMMAND_CLASS_BARRIER_OPERATOR (0x66)|Command Class = COMMAND_CLASS_BARRIER_OPERATOR (0x66)|Command Class = COMMAND_CLASS_BARRIER_OPERATOR (0x66)|Command Class = COMMAND_CLASS_BARRIER_OPERATOR (0x66)|Command Class = COMMAND_CLASS_BARRIER_OPERATOR (0x66)|Command Class = COMMAND_CLASS_BARRIER_OPERATOR (0x66)|Command Class = COMMAND_CLASS_BARRIER_OPERATOR (0x66)|
|Command = BARRIER_OPERATOR_SIGNAL_SUPPORTED_GET (0x04)|Command = BARRIER_OPERATOR_SIGNAL_SUPPORTED_GET (0x04)|Command = BARRIER_OPERATOR_SIGNAL_SUPPORTED_GET (0x04)|Command = BARRIER_OPERATOR_SIGNAL_SUPPORTED_GET (0x04)|Command = BARRIER_OPERATOR_SIGNAL_SUPPORTED_GET (0x04)|Command = BARRIER_OPERATOR_SIGNAL_SUPPORTED_GET (0x04)|Command = BARRIER_OPERATOR_SIGNAL_SUPPORTED_GET (0x04)|Command = BARRIER_OPERATOR_SIGNAL_SUPPORTED_GET (0x04)|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 103




<!-- PAGE 105 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.12.6** **Barrier** **Operator** **Report** **Signaling** **Capabilities** **Supported** **Command**


This command returns a bit mask of signaling subsystem(s) supported by the sending node. The
device that issuing this command may not support any signaling subsystem(s).


Table 2.74: Barrier Operator Report Signaling Capabilities Supported Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_BARRIER_OPERATOR (0x66)|Command Class = COMMAND_CLASS_BARRIER_OPERATOR (0x66)|Command Class = COMMAND_CLASS_BARRIER_OPERATOR (0x66)|Command Class = COMMAND_CLASS_BARRIER_OPERATOR (0x66)|Command Class = COMMAND_CLASS_BARRIER_OPERATOR (0x66)|Command Class = COMMAND_CLASS_BARRIER_OPERATOR (0x66)|Command Class = COMMAND_CLASS_BARRIER_OPERATOR (0x66)|Command Class = COMMAND_CLASS_BARRIER_OPERATOR (0x66)|
|Command = BARRIER_OPERATOR_SIGNAL_SUPPORTED_REPORT (0x05)|Command = BARRIER_OPERATOR_SIGNAL_SUPPORTED_REPORT (0x05)|Command = BARRIER_OPERATOR_SIGNAL_SUPPORTED_REPORT (0x05)|Command = BARRIER_OPERATOR_SIGNAL_SUPPORTED_REPORT (0x05)|Command = BARRIER_OPERATOR_SIGNAL_SUPPORTED_REPORT (0x05)|Command = BARRIER_OPERATOR_SIGNAL_SUPPORTED_REPORT (0x05)|Command = BARRIER_OPERATOR_SIGNAL_SUPPORTED_REPORT (0x05)|Command = BARRIER_OPERATOR_SIGNAL_SUPPORTED_REPORT (0x05)|
|Bit Mask 1|Bit Mask 1|Bit Mask 1|Bit Mask 1|Bit Mask 1|Bit Mask 1|Bit Mask 1|Bit Mask 1|
|…|…|…|…|…|…|…|…|
|Bit Mask N|Bit Mask N|Bit Mask N|Bit Mask N|Bit Mask N|Bit Mask N|Bit Mask N|Bit Mask N|



**Bit** **Mask** **(N** **bytes)**

This field is used to advertise the event signaling capabilities supported by the sending node. If
the device does not support any signaling subsystem(s), the device MAY issue this command with a
bitmask felid set to 0x00.


CC:0066.01.05.11.004 It MUST be treated as a bitmask.


1. Bit 0 in Bit Mask 1 indicates if subsystem type 0x01 is supported


2. Bit 1 in Bit Mask 1 indicates if subsystem type 0x02 is supported


3. …


CC:0066.01.05.11.001 If the subsystem type is supported, the corresponding bit MUST be set to 1.


If the subsystem type is not supported, the corresponding bit MUST be set to 0.


For the complete list of subsystem types, refer to Table 2.76.

CC:0066.01.05.11.002 The length of this field depends on the number of subsystems supported by the sending node. The
length of this field MUST be in the range 1..32 bytes.


CC:0066.01.05.11.003
A sending node MUST limit the length of this field to represent only those subsystems supported and
MUST NOT extend the length of the Bit Mask to pad the packet with 0x00.


**2.2.12.7** **Barrier** **Operator** **Event** **Signal** **Set** **Command**


This command is used to turn on or off an event signaling subsystem that is supported by the device.


CC:0066.01.06.13.001 A supporting node MAY ignore this command if the requested operation violates safety regulations.



CC:0066.01.06.11.004


CC:0066.01.06.11.001



UL requirements MUST take precedence over any Set command sent to a subsystem. It is up to the
discretion of the device to accept or reject the requested action. If the requested action is rejected, the
node MUST notify the requester via the Notification Command Class Report with the Notification
{Access Control::Barrier unable to perform requested operation due to UL requirements}.


Table 2.75: Barrier Operator Event Signal Set Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_BARRIER_OPERATOR (0x66)|Command Class = COMMAND_CLASS_BARRIER_OPERATOR (0x66)|Command Class = COMMAND_CLASS_BARRIER_OPERATOR (0x66)|Command Class = COMMAND_CLASS_BARRIER_OPERATOR (0x66)|Command Class = COMMAND_CLASS_BARRIER_OPERATOR (0x66)|Command Class = COMMAND_CLASS_BARRIER_OPERATOR (0x66)|Command Class = COMMAND_CLASS_BARRIER_OPERATOR (0x66)|Command Class = COMMAND_CLASS_BARRIER_OPERATOR (0x66)|
|Command = BARRIER_OPERATOR_EVENT_SIGNAL_SET (0x06)|Command = BARRIER_OPERATOR_EVENT_SIGNAL_SET (0x06)|Command = BARRIER_OPERATOR_EVENT_SIGNAL_SET (0x06)|Command = BARRIER_OPERATOR_EVENT_SIGNAL_SET (0x06)|Command = BARRIER_OPERATOR_EVENT_SIGNAL_SET (0x06)|Command = BARRIER_OPERATOR_EVENT_SIGNAL_SET (0x06)|Command = BARRIER_OPERATOR_EVENT_SIGNAL_SET (0x06)|Command = BARRIER_OPERATOR_EVENT_SIGNAL_SET (0x06)|
|Subsystem Type|Subsystem Type|Subsystem Type|Subsystem Type|Subsystem Type|Subsystem Type|Subsystem Type|Subsystem Type|
|Subsystem State|Subsystem State|Subsystem State|Subsystem State|Subsystem State|Subsystem State|Subsystem State|Subsystem State|



Subsystem Type (8 bits)



CC:0066.01.06.11.002 This field is used to indicate which subsystem type MUST be set at the receiving node. This field
MUST comply with Table 2.76.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 104




<!-- PAGE 106 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024



Table 2.76: Barrier Operator Event signal::Subsystem types encoding









|Subsystem Type|Description|Version|
|---|---|---|
|0x00|NOT SUPPORTED - reserved<br>|1|
|0x01|The Barrier Device has an Audible Notifcation subsystem con-<br>trollable via Z-Wave (For example: Siren)<br>|1|
|0x02|The Barrier Device has an Visual Notifcation subsystem con-<br>trollable via Z-Wave (For example: Flashing Light)|1|
|0x03.. 0xFF|Reserved|1|


**Subsystem** **State** **(8** **bits)**

CC:0066.01.06.11.003 This field is used to indicate the state that the specified subsystem MUST assume at the receiving
node. This field MUST comply with Table 2.77.


Table 2.77: Barrier Operator Event Signal::Subsystem states encoding

|Subsystem State|Description|Version|
|---|---|---|
|0x00|Subsystem OFF|1|
|…|Reserved|1|
|0xFF|Subsystem ON|1|



**2.2.12.8** **Barrier** **Operator** **Event** **Signaling** **Get** **Command**


This command is used to request the state of a signaling subsystem to a supporting node.


CC:0066.01.07.11.001 The Barrier Operator Event Signaling Report Command MUST be returned in response to this
command if the specified type is supported.


CC:0066.01.07.11.002 This command MUST NOT be issued via multicast addressing.


CC:0066.01.07.11.003 A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 2.78: Barrier Operator Event Signaling Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_BARRIER_OPERATOR (0x66)|Command Class = COMMAND_CLASS_BARRIER_OPERATOR (0x66)|Command Class = COMMAND_CLASS_BARRIER_OPERATOR (0x66)|Command Class = COMMAND_CLASS_BARRIER_OPERATOR (0x66)|Command Class = COMMAND_CLASS_BARRIER_OPERATOR (0x66)|Command Class = COMMAND_CLASS_BARRIER_OPERATOR (0x66)|Command Class = COMMAND_CLASS_BARRIER_OPERATOR (0x66)|Command Class = COMMAND_CLASS_BARRIER_OPERATOR (0x66)|
|Command = BARRIER_OPERATOR_EVENT_SIGNALING_GET (0x07)|Command = BARRIER_OPERATOR_EVENT_SIGNALING_GET (0x07)|Command = BARRIER_OPERATOR_EVENT_SIGNALING_GET (0x07)|Command = BARRIER_OPERATOR_EVENT_SIGNALING_GET (0x07)|Command = BARRIER_OPERATOR_EVENT_SIGNALING_GET (0x07)|Command = BARRIER_OPERATOR_EVENT_SIGNALING_GET (0x07)|Command = BARRIER_OPERATOR_EVENT_SIGNALING_GET (0x07)|Command = BARRIER_OPERATOR_EVENT_SIGNALING_GET (0x07)|
|Subsystem Type|Subsystem Type|Subsystem Type|Subsystem Type|Subsystem Type|Subsystem Type|Subsystem Type|Subsystem Type|



For fields’ description, refer to Section 2.2.12.7 Barrier Operator Event Signal Set Command.


**2.2.12.9** **Barrier** **Operator** **Event** **Signaling** **Report** **Command**


This command is used to indicate the state of a notification subsystem of a Barrier Device.


Table 2.79: Barrier Operator Event Signaling Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_BARRIER_OPERATOR (0x66)|Command Class = COMMAND_CLASS_BARRIER_OPERATOR (0x66)|Command Class = COMMAND_CLASS_BARRIER_OPERATOR (0x66)|Command Class = COMMAND_CLASS_BARRIER_OPERATOR (0x66)|Command Class = COMMAND_CLASS_BARRIER_OPERATOR (0x66)|Command Class = COMMAND_CLASS_BARRIER_OPERATOR (0x66)|Command Class = COMMAND_CLASS_BARRIER_OPERATOR (0x66)|Command Class = COMMAND_CLASS_BARRIER_OPERATOR (0x66)|
|Command = BARRIER_OPERATOR_EVENT_SIGNALING_REPORT (0x08)|Command = BARRIER_OPERATOR_EVENT_SIGNALING_REPORT (0x08)|Command = BARRIER_OPERATOR_EVENT_SIGNALING_REPORT (0x08)|Command = BARRIER_OPERATOR_EVENT_SIGNALING_REPORT (0x08)|Command = BARRIER_OPERATOR_EVENT_SIGNALING_REPORT (0x08)|Command = BARRIER_OPERATOR_EVENT_SIGNALING_REPORT (0x08)|Command = BARRIER_OPERATOR_EVENT_SIGNALING_REPORT (0x08)|Command = BARRIER_OPERATOR_EVENT_SIGNALING_REPORT (0x08)|
|Subsystem Type|Subsystem Type|Subsystem Type|Subsystem Type|Subsystem Type|Subsystem Type|Subsystem Type|Subsystem Type|
|Subsystem State|Subsystem State|Subsystem State|Subsystem State|Subsystem State|Subsystem State|Subsystem State|Subsystem State|



For fields’ description, refer to Section 2.2.12.7 Barrier Operator Event Signal Set Command


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 105