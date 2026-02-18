<!-- PAGE 279 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.53** **Lock** **Command** **Class,** **version** **1** **[DEPRECATED]**


**Warning:** THIS COMMAND CLASS HAS BEEN DEPRECATED


A device MAY implement this command class, but it is RECOMMENDED that new implementations use the Door Lock Command Class.


If implementing this command class, it is RECOMMENDED that the Door Lock Command Class
is also implemented.


The Lock Command Class is used to lock and unlock a “lock” type device, e.g. a door or window lock


**2.2.53.1** **Lock** **Set** **Command**


This command is used to set the lock state in a device.


Table 2.334: Lock Set Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_LOCK|Command Class = COMMAND_CLASS_LOCK|Command Class = COMMAND_CLASS_LOCK|Command Class = COMMAND_CLASS_LOCK|Command Class = COMMAND_CLASS_LOCK|Command Class = COMMAND_CLASS_LOCK|Command Class = COMMAND_CLASS_LOCK|Command Class = COMMAND_CLASS_LOCK|
|Command = LOCK_SET|Command = LOCK_SET|Command = LOCK_SET|Command = LOCK_SET|Command = LOCK_SET|Command = LOCK_SET|Command = LOCK_SET|Command = LOCK_SET|
|Lock State|Lock State|Lock State|Lock State|Lock State|Lock State|Lock State|Lock State|



**Lock** **State** **(8** **bits)**

The lock state field used to set the lock state of the device. The value 0 indicates that the device is
unlocked. The value 1 indicates that the device is locked.


**2.2.53.2** **Lock** **Get** **Command**


This command is used to request the lock state from a device.


The Lock Report Command MUST be returned in response to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 2.335: Lock Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_LOCK|Command Class = COMMAND_CLASS_LOCK|Command Class = COMMAND_CLASS_LOCK|Command Class = COMMAND_CLASS_LOCK|Command Class = COMMAND_CLASS_LOCK|Command Class = COMMAND_CLASS_LOCK|Command Class = COMMAND_CLASS_LOCK|Command Class = COMMAND_CLASS_LOCK|
|Command = LOCK_GET|Command = LOCK_GET|Command = LOCK_GET|Command = LOCK_GET|Command = LOCK_GET|Command = LOCK_GET|Command = LOCK_GET|Command = LOCK_GET|



**2.2.53.3** **Lock** **Report** **Command**


This command is used to report the lock state of a device.


Table 2.336: Lock Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_LOCK|Command Class = COMMAND_CLASS_LOCK|Command Class = COMMAND_CLASS_LOCK|Command Class = COMMAND_CLASS_LOCK|Command Class = COMMAND_CLASS_LOCK|Command Class = COMMAND_CLASS_LOCK|Command Class = COMMAND_CLASS_LOCK|Command Class = COMMAND_CLASS_LOCK|
|Command = LOCK_REPORT|Command = LOCK_REPORT|Command = LOCK_REPORT|Command = LOCK_REPORT|Command = LOCK_REPORT|Command = LOCK_REPORT|Command = LOCK_REPORT|Command = LOCK_REPORT|
|Lock State|Lock State|Lock State|Lock State|Lock State|Lock State|Lock State|Lock State|



**Lock** **State** **(8** **bits)**


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 278




<!-- PAGE 280 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


The Lock state field used to report the lock state of the device. The value 0 indicates that the device
is unlocked. The value 1 indicates that the device is locked.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 279