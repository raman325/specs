<!-- PAGE 907 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**4.2.8** **Supervision** **Command** **Class,** **version** **1**


The Supervision Command Class allows a sending node to request application-level delivery confirmation from a receiving node. The delivery confirmation includes relevant application-level status
information in the confirmation message.


**4.2.8.1** **Terminology**


The controlling application **initiates** an operation by sending a **Supervision** **encapsulated** **com-**
**mand** to a supporting node. The supporting node returns an **immediate** **confirmation** for the
reception while advertising its ability to perform the requested operation. The confirmation may
advertise the **application** **status** <Working>, <Success>, <No Support> or <Fail> depending on
the condition of the supporting node. One or more application status updates may follow later to
report problems, delays or the completion of the requested operation.


A door lock application is used as example in the following. Other uses may apply.


A magnetic lock may return the <Success> indication immediately since it takes only a few milliseconds to apply power to the electromagnet. In that case, no status updates are needed later.


An electro-mechanical lock may need time to complete its movement. A <Working> indication is
issued along with the expected duration, e.g. 5 seconds. Ideally, the movement is completed and a
<Success> indication is returned 5 seconds later. A motor defect or something jamming the movement
may prevent the lock from completing the requested operation. A <Fail> indication is returned in
that case. If the motor runs slower than anticipated, another <Working> indication may be issued
when e.g. 75% of the expected duration has elapsed; reporting the new expected duration. If it runs
faster, a <Success> indication may be issued before it was expected. Both cases allow a GUI progress
bar to respond instantly rather than waiting for a polling response.


**4.2.8.2** **Compatibility** **Considerations**


This command class is used as an integrated part of the Security 2 Command Class but may also be
used for non-secure applications.


CC:006C.01.00.23.002 The Supervision Command Class MAY be used for solitary commands such as Set, Remove and
unsolicited Report commands.


CC:006C.01.00.21.003
The Supervision Command Class MUST NOT be used for immediate session-like command flows such
as Get _↔_ Report command exchanges where a REPORT is expected immediately after the GET. Since
the receiver is waiting for the report, it can resend the GET if it does not receive one. Unsolicited
REPORT (or other similar) commands from an end device SHOULD be encapsulated with Supervision
Command Class to ensure the controller is aware of a change of state.


CC:006C.01.00.23.001 The Supervision Get Command MAY carry multiple commands grouped with the Multi Command
encapsulation command.


**4.2.8.2.1** **Node** **Information** **Frame** **(NIF)**


CC:006C.01.00.21.001 A supporting node MUST always advertise the Supervision Command Class in its NIF and Multi
Channel Capability Report, regardless of the inclusion status and security bootstrapping outcome.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 906




<!-- PAGE 908 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**4.2.8.2.2** **Encapsulated** **Commands**


Supervision Command Class is intended for encapsulating solitary commands; it is to say commands
that do not require any response to be returned.


It exists Set type Commands that may optionally require to return a status or optional command
such as Notification Report or handshake mechanism. When receiving such a Set type command in a
Supervision Get Command:


CC:006C.01.00.21.002 - The Supervision Report MUST be returned by a receiving node.



CC:006C.01.00.23.003


CC:006C.01.00.22.001




- Additional commands MAY be returned. These commands SHOULD be returned before the

Supervision Report Command



CC:006C.01.00.51.001 A sending node MUST NOT use handshake mechanisms for Set Commands when using Supervision
encapsulation.


CC:006C.01.00.23.004 It is OPTIONAL for a receiving node to return an answer to a Set type Command which requires a
response to be returned if received with Supervision encapsulation.


**4.2.8.3** **Supervision** **Get** **Command**


This command is used to initiate the execution of a command and to request the immediate and
future status of the process being initiated.


CC:006C.01.01.11.001 The Supervision Report Command MUST be returned in response to this command unless it is to be
ignored.


CC:006C.01.01.11.002 The <SUCCESS> status MUST be advertised in the Supervision Report Command if the operation
is completed immediately.


CC:006C.01.01.11.003 If the requested operation is accepted but cannot be completed immediately, the <WORKING>
status MUST be advertised in the Supervision Report Command along with the expected duration
for the operation. The “Status Updates” field MUST be consulted to determine if status updates are
to be advertised in the future.


CC:006C.01.01.13.003 This command MAY be issued via multicast addressing.


CC:006C.01.01.11.004 A receiving node MUST NOT ignore the encapsulated command if this command is received via
multicast addressing.


CC:006C.01.01.11.005 A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SUPERVISION (0x6C)|Command Class = COMMAND_CLASS_SUPERVISION (0x6C)|Command Class = COMMAND_CLASS_SUPERVISION (0x6C)|Command Class = COMMAND_CLASS_SUPERVISION (0x6C)|Command Class = COMMAND_CLASS_SUPERVISION (0x6C)|Command Class = COMMAND_CLASS_SUPERVISION (0x6C)|Command Class = COMMAND_CLASS_SUPERVISION (0x6C)|Command Class = COMMAND_CLASS_SUPERVISION (0x6C)|
|Command = SUPERVISION_GET (0x01)|Command = SUPERVISION_GET (0x01)|Command = SUPERVISION_GET (0x01)|Command = SUPERVISION_GET (0x01)|Command = SUPERVISION_GET (0x01)|Command = SUPERVISION_GET (0x01)|Command = SUPERVISION_GET (0x01)|Command = SUPERVISION_GET (0x01)|
|Status Updates|Reserved|Session ID|Session ID|Session ID|Session ID|Session ID|Session ID|
|Encapsulated Command Length|Encapsulated Command Length|Encapsulated Command Length|Encapsulated Command Length|Encapsulated Command Length|Encapsulated Command Length|Encapsulated Command Length|Encapsulated Command Length|
|Encapsulated Command 1|Encapsulated Command 1|Encapsulated Command 1|Encapsulated Command 1|Encapsulated Command 1|Encapsulated Command 1|Encapsulated Command 1|Encapsulated Command 1|
|…|…|…|…|…|…|…|…|
|Encapsulated Command N|Encapsulated Command N|Encapsulated Command N|Encapsulated Command N|Encapsulated Command N|Encapsulated Command N|Encapsulated Command N|Encapsulated Command N|



**Reserved**

CC:006C.01.01.11.006 This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**Status** **Updates** **(1** **bit)**

This flag is used to allow a receiving node to advertise application status updates in future Supervision
Report Commands.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 907




<!-- PAGE 909 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


As an example, this flag must be set to allow a supporting node to immediately advertise the <WORKING> status in a Supervision Report Command and subsequently advertise the <SUCCESS> status
in another Supervision Report Command once the operation has been completed.

CC:006C.01.01.11.007 The value of this field MUST comply with Table 4.27.


Table 4.27: Supervision Get::Status Updates


**Session** **ID** **(6** **bits)**

|Value|Required Behavior|
|---|---|
|‘0’|Only return a report now|
|‘1’|Return a report now and more later if needed|



The same command may be received multiple times, e.g. due to retransmissions.

CC:006C.01.01.11.008 A sending node MUST increment this field each time a new unique Supervision Get Command is
issued.


CC:006C.01.01.13.004 A sending node MAY use the same Session ID for a multicast and singlecast follow-up carrying the
same encapsulated command. A sending node MAY also use the same Session ID for all destinations
of singlecast follow-up commands.


CC:006C.01.01.11.00D A receiving node MUST ignore duplicate singlecast commands having the same Session ID and MUST
NOT return a Supervision Report to the command, if the command was received without Security
encapsulation.


CC:006C.01.01.11.00A A receiving node MUST abort an active operation in favor of a new command with a new Session ID
if that new command affects the same resources as the active operation.


CC:006C.01.01.13.001 A receiving node MAY abort an active operation in favor of a new command with a new Session ID
even if the new command does not affects the same resources as the active operation, e.g. if the node
does not have resources to handle multi-session state management.


**Encapsulated** **Command** **Length** **(1** **Byte)**

This field is used to specify the length of the encapsulated command.

CC:006C.01.01.11.00B The value MUST specify the number of bytes in the Encapsulated Command field.


**Encapsulated** **Command** **(N** **bytes)**

This field is used to carry an encapsulated command.

CC:006C.01.01.11.00C The length of this field MUST be in the range 1..255 bytes.


CC:006C.01.01.13.002
The field MAY carry a Multi Command Encapsulated Command which contains multiple commands.


**4.2.8.4** **Supervision** **Report** **Command**









|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SUPERVISION (0x6C)|Command Class = COMMAND_CLASS_SUPERVISION (0x6C)|Command Class = COMMAND_CLASS_SUPERVISION (0x6C)|Command Class = COMMAND_CLASS_SUPERVISION (0x6C)|Command Class = COMMAND_CLASS_SUPERVISION (0x6C)|Command Class = COMMAND_CLASS_SUPERVISION (0x6C)|Command Class = COMMAND_CLASS_SUPERVISION (0x6C)|Command Class = COMMAND_CLASS_SUPERVISION (0x6C)|
|Command = SUPERVISION_REPORT|Command = SUPERVISION_REPORT|Command = SUPERVISION_REPORT|Command = SUPERVISION_REPORT|Command = SUPERVISION_REPORT|Command = SUPERVISION_REPORT|Command = SUPERVISION_REPORT|Command = SUPERVISION_REPORT|
|More Status<br>Updates|Re-<br>served|Session ID|Session ID|Session ID|Session ID|Session ID|Session ID|
|Status|Status|Status|Status|Status|Status|Status|Status|
|Duration|Duration|Duration|Duration|Duration|Duration|Duration|Duration|


**Reserved**

CC:006C.01.02.11.001 This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**More** **Status** **Updates**

This field is used to advertise if more Supervision Reports follow for the actual Session ID.


CC:006C.01.02.11.002


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 908




<!-- PAGE 910 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


The value of this field MUST comply with Table 4.28.


Table 4.28: Supervision Report::More Status Updates

|Value|Required Behavior|
|---|---|
|‘0’|This is the last report|
|‘1’|More reports follow according to the advertised duration|



**Session** **ID** **(1** **Byte)**

This field MUST carry the same value as the Session ID field of the Supervision Get Command which
initiated this session.


**Status** **(8** **bit)**

This field is used advertise the current status of the command process.

CC:006C.01.02.11.013 This field MUST reflect the actual application status of the received encapsulated command.


CC:006C.01.02.11.004 If a Multi Command encapsulated group of commands is being supervised, an error indication (such as
<No Support> or <Fail>) MUST be issued if just one of the Multi Command encapsulated commands
triggers an error condition.


CC:006C.01.02.11.005 The <Success> indication MUST signify that all commands carried in a Multi Command encapsulation commands have completed successfully.

CC:006C.01.02.11.006 The value of this field MUST comply with Table 4.29.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 909




<!-- PAGE 911 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Table 4.29: Supervision Report::Status Identifiers

|Value|i<br>Identifer|Description|
|---|---|---|
|0x00|NO_SUPPORT|The command is not supported by the receiver.<br>A zero Duration value MUST be advertised.<br>This identifer MUST be advertised if one or more Multi Command<br>encapsulated commands are not supported.|
|0x01|WORKING|The command was accepted by the receiver and processing has<br>started.<br>A non-zero Duration value MUST be advertised.<br>If processing is completed instantly, the receiver MUST skip advertis-<br>ing the WORKING status and return the SUCCESS status instead.<br>If Status Updates was set to 1 in the Get Command, this command<br>MUST be followed by another Supervision Report when the duration<br>has elapsed. The new status MUST be one of WORKING, FAIL or<br>SUCCESS.<br>The duration MAY be cut short by sending the new Supervision<br>Report before the original predicted duration has elapsed.<br>If used for Multi Command encapsulated commands, the advertised<br>Duration value MUST represent the slowest of the commands.|
|0x02|FAIL|The command was accepted by the receiver but processed with a<br>resulting application status which difers from the supervised com-<br>mand requested<br>Examples include but are not limited to:<br>The node may not be ready to perform the requested operation (e.g.<br>a door lock cannot lock if the door is open) _or_<br>the command processing reached an unexpected situation (e.g.<br>a<br>door lock being jammed while working) _or_<br>there is an application specifc limitation (e.g. an irrigation controller<br>which only accepts one open valve at a time).<br>A zero Duration value MUST be advertised.<br>This status identifer MUST be advertised if the processing of one<br>or more Multi Command encapsulated commands failed.|
|0xFF|SUCCESS|The requested command has been completed and the application<br>status is as the supervised command requested.<br>A controlling application SHOULD NOT verify the application sta-<br>tus, e.g.<br>by sending a Get Command, after receiving this status<br>identifer.<br>A zero Duration value MUST be advertised.<br>This identifer MUST be advertised if the processing of all Multi<br>Command encapsulated commands was successful.|



CC:006C.01.02.11.011 All other values are reserved. Reserved values MUST NOT be used by a sending node and MUST be
ignored by a receiving node.


**Duration** **(8** **bits)**

CC:006C.01.02.11.012 The Duration field MUST advertise the time needed to complete the current operation. The encoding
of the Duration field MUST be according to Table 4.30.

|Duration|Table 4.30: Supervision Report::Duration Description|
|---|---|
|Duration|Description|
|0x00|0 seconds. (Already at the Target Value.)|
|0x01-0x7F|1 second (0x01) to 127 seconds (0x7F) in 1 second resolution.|
|0x80-0xFD|1 minute (0x80) to 126 minutes (0xFD) in 1 minute resolution.|
|0xFE|Unknown duration|
|0xFF|Reserved|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 910




<!-- PAGE 912 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**4.2.8.5** **Examples** **and** **use-cases**


**4.2.8.5.1** **Set** **Type** **commands**


CC:006C.01.00.11.002 A supporting node MUST return the Supervision status of solitary Set type commands for all its
supported Command Classes.


For actuator control Set commands with a corresponding Get type command to read back the value(s),
CC:006C.01.00.11.003 this means that the response codes MUST be used as follows:


      - SUCCESS: The application understood the command and completed the requested operation.
The values specified in the Set Command would be returned if the supporting node would return
an answer to the corresponding Get Command. The only exception are special values (e.g. value
to set to the last non-zero level) representing another value.


      - WORKING: The application understood the command and started performing the requested
operation, but the controller needs to wait before the target value is reached. The supporting
node would not return the values specified in the Set Command yet if it returned an answer to
the corresponding Get Command


      - FAIL: The application understood the command and cannot perform the requested operation
(e.g. invalid value or mechanical failure). The supporting node will not return the values
specified in the Set Command if it returned an answer to the corresponding Get Command.


The Door Lock Operation Set Command is an example of an actuator control Set command with a
corresponding Get Command.


For actuator control Start and Stop commands or commands without a corresponding Get type read
CC:006C.01.00.11.004 back, this means that the response codes MUST be used as follows:


      - SUCCESS: The application understood the command and completed the requested operation;
i.e. successfully started or stopped the requested operation.


      - FAIL: The application did not understand the command or could not perform the requested
operation (if applicable)


The Multilevel Switch Start Level Change Command, Multilevel Switch Stop Level Change Command
and the Powerlevel Test Node Set are examples of actuator control Start/Stop commands.

CC:006C.01.00.11.005 For configuration Set commands, this means that the response codes MUST be used as follows:


      - SUCCESS: The application understood the command and accepted all the parameter(s) and
value(s). The values specified in the Set Command would be returned if the supporting node
would return an answer to the corresponding Get Command.


      - FAIL: The application had one or more error while parsing or applying the parameters (e.g. the
command was partially or completely ignored due to invalid values)

The Door Lock Configuration Set Command, Configuration Set and Association Set Command are
examples of configuration commands.


**4.2.8.5.2** **Powerlevel** **Test** **Node** **Set** **Command**


CC:006C.01.00.12.001 The Powerlevel Test Node Set Command SHOULD be considered as a Start/Stop command or command without a corresponding Get Command. The corresponding Get Command (Powerlevel Test
Node Get Command) is used to query subsequent results and Supervision cannot replace the need for
a controller to issue a subsequent Get Command.


CC:006C.01.00.12.002 A receiving node SHOULD return SUCCESS when starting the Powerlevel Test Node test.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 911




<!-- PAGE 913 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**4.2.8.5.3** **Report/Notification** **Type** **Commands**


CC:006C.01.00.13.003
A supporting node MAY use Supervision encapsulation for issuing an unsolicited Report/Notification
type Command. For example, a sleeping node issuing a sensor reading receives a delivery confirmation
immediately and can return to sleep as soon as the Supervision Report is received.


CC:006C.01.00.11.006
A node MUST return a Supervision status of a Report/Notification type command for any Command
Classes, regardless whether it is supported, controlled or neither.


CC:006C.01.00.12.003 A controlling node SHOULD return a SUCCESS or NO_SUPPORT status when receiving such
commands.


**4.2.8.5.4** **Remove** **Type** **commands**


A supporting node MUST return the Supervision status of solitary Remove type commands for all its
supported Command Classes. The remove type commands must be treated as Set type of commands.


CC:006C.01.00.11.007 For Remove command, this means that the response codes MUST be used as follows:

      - SUCCESS: The application understood the command and removed the specified parameter(s)
and values. The values specified in the Remove Command would not be returned if the supporting node would return an answer to the corresponding Get Command.


      - FAIL: The application had one or more error while applying the command (e.g. the command
was partially or completely ignored due to invalid values)


The Association Remove Command and Schedule Remove Command are examples of remove commands.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 912

---

<!-- PAGE 914 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**4.2.9** **Supervision** **Command** **Class,** **version** **2**


The Supervision Command Class allows a sending node to request application-level delivery confirmation from a receiving node. The delivery confirmation includes relevant application-level status
information in the confirmation message.


**4.2.9.1** **Compatibility** **considerations**


CC:006C.02.00.21.001 Compatibility consideration requirements from version 1 MUST also be observed by a version 2
supporting node.


Supervision Command Class, version 2 is backwards compatible with Supervision Command Class,
CC:006C.02.00.21.002 version 1. Fields and commands not described in this version MUST remain unchanged from version
1.


The Supervision Report Command has been extended to enable expedited message delivery between
Wake Up Destination and Wake Up Node (refer to the Wake Up Command Class). It leverages
sleeping nodes using Supervision encapsulation to tell them to initiate a Wake Up Period.


**4.2.9.2** **Supervision** **Report** **Command**


This command is used to advertise the status of one or more command process(es).









|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SUPERVISION (0x6C)|Command Class = COMMAND_CLASS_SUPERVISION (0x6C)|Command Class = COMMAND_CLASS_SUPERVISION (0x6C)|Command Class = COMMAND_CLASS_SUPERVISION (0x6C)|Command Class = COMMAND_CLASS_SUPERVISION (0x6C)|Command Class = COMMAND_CLASS_SUPERVISION (0x6C)|Command Class = COMMAND_CLASS_SUPERVISION (0x6C)|Command Class = COMMAND_CLASS_SUPERVISION (0x6C)|
|Command = SUPERVISION_REPORT (0x02)|Command = SUPERVISION_REPORT (0x02)|Command = SUPERVISION_REPORT (0x02)|Command = SUPERVISION_REPORT (0x02)|Command = SUPERVISION_REPORT (0x02)|Command = SUPERVISION_REPORT (0x02)|Command = SUPERVISION_REPORT (0x02)|Command = SUPERVISION_REPORT (0x02)|
|More Status<br>Updates|Wake Up<br>Request|Session ID|Session ID|Session ID|Session ID|Session ID|Session ID|
|Status|Status|Status|Status|Status|Status|Status|Status|
|Duration|Duration|Duration|Duration|Duration|Duration|Duration|Duration|


All fields not described below remain unchanged from version 1


**Wake** **Up** **Request** **(1** **bit)**

CC:006C.02.02.11.001 This field is used to indicate to the receiving node that it MUST start a Wake Up Period.

CC:006C.02.02.11.002 If the receiving node does not support the Wake Up On Demand functionality, this field MUST be
ignored.


The Wake Up On Demand functionality is part of the Wake Up Command Class, version 3.

CC:006C.02.02.11.003 A node supporting the Wake Up On Demand functionality MUST return a Wake Up Notification
Command if the Wake Up destination node issued a this command with the Wake Up Request bit set

to 1.

CC:006C.02.02.11.004 A node supporting the Wake Up On Demand functionality MUST ignore the Wake Up Request field
if the Supervision Report is not issued by the Wake Up Destination.


**4.2.9.2.1** **Wake** **up** **on** **Demand** **functionality**


The Wake Up on Demand functionality is shown in Figure 4.24. This functionality allows the controller
to issue important commands to the sleeping device before its next Wake Up Period.


CC:006C.02.02.13.001 When the controlling node receives a Supervision encapsulated frame from the sleeping node, it MAY
speed up the delivery of some important commands by setting the _Wake_ _Up_ _Request_ bit to 1, if the
sleeping node supports this functionality.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 913




<!-- PAGE 915 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Figure 4.24: Wake Up on Demand functionality


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 914