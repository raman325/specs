<!-- PAGE 583 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.2** **Application** **Status** **Command** **Class,** **version** **1**


This command class contains commands that are not directly related to a specific functionality in the
application, but are useful for maintaining an optimal Z-Wave system.


**3.2.2.1** **Compatibility** **Considerations**


**3.2.2.1.1** **Node** **Information** **Frame** **(NIF)**


A supporting node MUST always advertise the Application Status Command Class in its NIF, regardless of the inclusion status and security bootstrapping outcome.


**3.2.2.2** **Application** **Busy** **Command**


The Application Busy Command used to instruct a node that the node that it is trying to communicate
with is busy and is unable to service the request right now.


Table 3.4: Application Busy

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_APPLICATION_STATUS|Command Class = COMMAND_CLASS_APPLICATION_STATUS|Command Class = COMMAND_CLASS_APPLICATION_STATUS|Command Class = COMMAND_CLASS_APPLICATION_STATUS|Command Class = COMMAND_CLASS_APPLICATION_STATUS|Command Class = COMMAND_CLASS_APPLICATION_STATUS|Command Class = COMMAND_CLASS_APPLICATION_STATUS|Command Class = COMMAND_CLASS_APPLICATION_STATUS|
|Command = APPLICATION_BUSY|Command = APPLICATION_BUSY|Command = APPLICATION_BUSY|Command = APPLICATION_BUSY|Command = APPLICATION_BUSY|Command = APPLICATION_BUSY|Command = APPLICATION_BUSY|Command = APPLICATION_BUSY|
|Status|Status|Status|Status|Status|Status|Status|Status|
|Wait Time|Wait Time|Wait Time|Wait Time|Wait Time|Wait Time|Wait Time|Wait Time|



**Status** **(8** **bits)**

The status field can have the following values:

|Status|Table 3.5: Status Bits Description|
|---|---|
|Status|Description|
|0|Try again later|
|1|Try again in Wait Time seconds|
|2|Request queued, executed later|



**Wait** **Time** **(8** **bits)**

The wait time field indicates the number of seconds a node should wait before retrying the request.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 582




<!-- PAGE 584 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.2.3** **Application** **Rejected** **Request** **Command**


All supported commands are typically executed unconditionally and the only handshake is acknowledgement on the protocol level. Some applications can however be in a state where the application
rejects to execute a supported command. The Application Rejected Request Command used to instruct a node that the command was rejected by the application in the receiving node.


Table 3.6: Application Rejected Request Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_APPLICATION_STATUS|Command Class = COMMAND_CLASS_APPLICATION_STATUS|Command Class = COMMAND_CLASS_APPLICATION_STATUS|Command Class = COMMAND_CLASS_APPLICATION_STATUS|Command Class = COMMAND_CLASS_APPLICATION_STATUS|Command Class = COMMAND_CLASS_APPLICATION_STATUS|Command Class = COMMAND_CLASS_APPLICATION_STATUS|Command Class = COMMAND_CLASS_APPLICATION_STATUS|
|Command = APPLICATION_REJECTED_REQUEST|Command = APPLICATION_REJECTED_REQUEST|Command = APPLICATION_REJECTED_REQUEST|Command = APPLICATION_REJECTED_REQUEST|Command = APPLICATION_REJECTED_REQUEST|Command = APPLICATION_REJECTED_REQUEST|Command = APPLICATION_REJECTED_REQUEST|Command = APPLICATION_REJECTED_REQUEST|
|Status|Status|Status|Status|Status|Status|Status|Status|



**Status** **(8** **bits)**

This field MUST be set to 0. The value 0 MUST indicate that the received (supported) command
has been rejected by the application at the receiving node


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 583