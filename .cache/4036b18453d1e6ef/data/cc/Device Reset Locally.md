<!-- PAGE 631 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.14** **Device** **Reset** **Locally** **Command** **Class,** **version** **1**


The Device Reset Locally Command Class is used to notify central controllers that a Z-Wave device
is resetting its network specific parameters.


CC:005A.01.00.12.001 Any node SHOULD support this Command Class if it can be reset to factory default.


**3.2.14.1** **Device** **Reset** **Locally** **Notification** **Command**


The Device Reset Locally Notification Command is used to advertise that the device will be reset to
default.


CC:005A.01.01.11.001 The reset operation MUST reset protocol data (HomeID, NodeID, etc.). For Z-Wave Plus nodes,
additional requirements upon node reset are provided in Section 8.

CC:005A.01.01.11.002 In case a Lifeline destination is configured in Association Group #1, the device MUST send a Device
Reset Locally Notification Command to the Lifeline destinations.

CC:005A.01.01.11.004 The Device Reset Locally Notification Command MUST be issued by the Root Device. If Multi
Channel encapsulation is used, the source End Point MUST be set to 0.


Table 3.47: Device Reset Locally Notification Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_DEVICE_RESET_LOCALLY (0x5A)|Command Class = COMMAND_CLASS_DEVICE_RESET_LOCALLY (0x5A)|Command Class = COMMAND_CLASS_DEVICE_RESET_LOCALLY (0x5A)|Command Class = COMMAND_CLASS_DEVICE_RESET_LOCALLY (0x5A)|Command Class = COMMAND_CLASS_DEVICE_RESET_LOCALLY (0x5A)|Command Class = COMMAND_CLASS_DEVICE_RESET_LOCALLY (0x5A)|Command Class = COMMAND_CLASS_DEVICE_RESET_LOCALLY (0x5A)|Command Class = COMMAND_CLASS_DEVICE_RESET_LOCALLY (0x5A)|
|Command = DEVICE_RESET_LOCALLY_NOTIFICATION (0x01)|Command = DEVICE_RESET_LOCALLY_NOTIFICATION (0x01)|Command = DEVICE_RESET_LOCALLY_NOTIFICATION (0x01)|Command = DEVICE_RESET_LOCALLY_NOTIFICATION (0x01)|Command = DEVICE_RESET_LOCALLY_NOTIFICATION (0x01)|Command = DEVICE_RESET_LOCALLY_NOTIFICATION (0x01)|Command = DEVICE_RESET_LOCALLY_NOTIFICATION (0x01)|Command = DEVICE_RESET_LOCALLY_NOTIFICATION (0x01)|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 630