<!-- PAGE 371 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.78** **Protection** **Command** **Class,** **version** **1**


The Protection Command Class version 1 used to protect a device against unintentional control by
e.g. a child.


**2.2.78.1** **Protection** **Set** **Command**


This command is used to set the protection state in a device.


Table 2.450: Protection Set Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_PROTECTION|Command Class = COMMAND_CLASS_PROTECTION|Command Class = COMMAND_CLASS_PROTECTION|Command Class = COMMAND_CLASS_PROTECTION|Command Class = COMMAND_CLASS_PROTECTION|Command Class = COMMAND_CLASS_PROTECTION|Command Class = COMMAND_CLASS_PROTECTION|Command Class = COMMAND_CLASS_PROTECTION|
|Command = PROTECTION_SET|Command = PROTECTION_SET|Command = PROTECTION_SET|Command = PROTECTION_SET|Command = PROTECTION_SET|Command = PROTECTION_SET|Command = PROTECTION_SET|Command = PROTECTION_SET|
|Protection State|Protection State|Protection State|Protection State|Protection State|Protection State|Protection State|Protection State|



**Protection** **State** **(8** **bits)**

The Protection State field used to set the protection state of the device.

|Pro-|Table 2.451: Protection Set::Protection State encoding Description|
|---|---|
|**Pro-**<br>**tec-**<br>**tion**<br>**State**|**Description**|
|0x00|Unprotected - The device is not protected, and may be operated normally via the user<br>interface.|
|0x01|Protection by sequence - The device is protected by altering the way the device normally<br>is operated into a more complicated sequence of actions, e.g. if a device normally is<br>controlled by a single press of a button on the device it might be changed to require 3<br>rapid presses on a button to control it.|
|0x02|No operation possible - It is not possible at all to control a device directly via the user<br>interface.|



All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.


Control via Z-Wave is always possible independently of the protection state.


**2.2.78.2** **Protection** **get** **command**


This Command is used to request the protection state from a device.


The Protection Report Command MUST be returned in response to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 2.452: Protection Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_PROTECTION|Command Class = COMMAND_CLASS_PROTECTION|Command Class = COMMAND_CLASS_PROTECTION|Command Class = COMMAND_CLASS_PROTECTION|Command Class = COMMAND_CLASS_PROTECTION|Command Class = COMMAND_CLASS_PROTECTION|Command Class = COMMAND_CLASS_PROTECTION|Command Class = COMMAND_CLASS_PROTECTION|
|Command = PROTECTION_GET|Command = PROTECTION_GET|Command = PROTECTION_GET|Command = PROTECTION_GET|Command = PROTECTION_GET|Command = PROTECTION_GET|Command = PROTECTION_GET|Command = PROTECTION_GET|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 370




<!-- PAGE 372 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.78.3** **Protection** **report** **command**


This command is used to report the protection state of a device.


Table 2.453: Protection Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_PROTECTION|Command Class = COMMAND_CLASS_PROTECTION|Command Class = COMMAND_CLASS_PROTECTION|Command Class = COMMAND_CLASS_PROTECTION|Command Class = COMMAND_CLASS_PROTECTION|Command Class = COMMAND_CLASS_PROTECTION|Command Class = COMMAND_CLASS_PROTECTION|Command Class = COMMAND_CLASS_PROTECTION|
|Command = PROTECTION_REPORT|Command = PROTECTION_REPORT|Command = PROTECTION_REPORT|Command = PROTECTION_REPORT|Command = PROTECTION_REPORT|Command = PROTECTION_REPORT|Command = PROTECTION_REPORT|Command = PROTECTION_REPORT|
|Protection State|Protection State|Protection State|Protection State|Protection State|Protection State|Protection State|Protection State|



**Protection** **State** **(8** **bits)**


Refer to explanation under Protection Get Command.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 371

---

<!-- PAGE 373 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.79** **Protection** **Command** **Class,** **version** **2**


The Protection Command Class version 2 is extended to specify whether a device may be controlled
via RF Commands or not. When a video recorder is powered by an outlet that can be controlled
by RF the user would like to prevent the video recorder from being turned off when it is recording
her/his favorite show. In this case the Protection Command Class version 2 may be used to protect
the outlet from being turned off by setting the outlet in “No RF Control” state.


The following Commands have been added or changed in version 2. The Commands not mentioned
remain unchanged.


This Command Class is intended for convenience applications. The Command Class SHOULD NOT
be used for safety critical applications.


**2.2.79.1** **Protection** **set** **command**


This command is used to set the protection state in a device.


Table 2.454: Protection Set Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_PROTECTION|Command Class = COMMAND_CLASS_PROTECTION|Command Class = COMMAND_CLASS_PROTECTION|Command Class = COMMAND_CLASS_PROTECTION|Command Class = COMMAND_CLASS_PROTECTION|Command Class = COMMAND_CLASS_PROTECTION|Command Class = COMMAND_CLASS_PROTECTION|Command Class = COMMAND_CLASS_PROTECTION|
|Command = PROTECTION_SET|Command = PROTECTION_SET|Command = PROTECTION_SET|Command = PROTECTION_SET|Command = PROTECTION_SET|Command = PROTECTION_SET|Command = PROTECTION_SET|Command = PROTECTION_SET|
|Reserved|Reserved|Reserved|Reserved|Local Protection State|Local Protection State|Local Protection State|Local Protection State|
|Reserved|Reserved|Reserved|Reserved|RF Protection State|RF Protection State|RF Protection State|RF Protection State|



**Local** **Protection** **State** **(4** **bits)**

The Local Protection State field used to set the protection state of the device.


Table 2.455: Protection Set::Local Protection State encoding

|Local Protection<br>State|Description|
|---|---|
|0|Unprotected - The device is not protected, and may be operated normally via<br>the user interface.|
|1|Protection by sequence - The device is protected by altering the way the device<br>normally is operated into a more complicated sequence of actions, e.g. if a<br>device normally is controlled by a single press of a button on the device it<br>might be changed to require 3 rapid presses on a button to control it.|
|2|No operation possible - It is not possible at all to control a device directly via<br>the user interface.|



All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.


**Note:** Local Protection can only protect a device from “normal operation”. This means only the
operation that is intended by the application of the device. It is NOT allowed to protect the device
from network functionalities. The device cannot be protected from being put into learn mode nor
from sending out the NIF.


**RF** **Protection** **State** **(4** **bits)**

The RF Protection State field used to set the RF protection state of the device. In the case where a
device set into a RF Protection State which instructs the device not to answer to a “normal operation”
Command, the device MUST return the Application Rejected Request Command (Status = 0) of the
Application Status Command Class. Refer to the Application Status Command Class.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 372




<!-- PAGE 374 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024

|RF Protection|Table 2.456: Protection Set::RF Protection State Description|
|---|---|
|**RF**<br>**Protection**<br>**State**|**Description**|
|0|Unprotected - The device MUST accept and respond to all RF Commands.|
|1|No RF control - all runtime Commands are ignored by the device. The device<br>MUST still respond with status on requests.|
|2|No RF response at all. The device will not even reply to status requests.|



All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.


**Note:** It is only possible to un-protect the device with the Protection Set Command. It is not allowed
ignore Protection Commands. If a device is excluded from the network, the protection states MUST
be reset.


**2.2.79.2** **Protection** **report** **command**


This command is used to report the protection state of a device.


Table 2.457: Protection Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_PROTECTION|Command Class = COMMAND_CLASS_PROTECTION|Command Class = COMMAND_CLASS_PROTECTION|Command Class = COMMAND_CLASS_PROTECTION|Command Class = COMMAND_CLASS_PROTECTION|Command Class = COMMAND_CLASS_PROTECTION|Command Class = COMMAND_CLASS_PROTECTION|Command Class = COMMAND_CLASS_PROTECTION|
|Command = PROTECTION_REPORT|Command = PROTECTION_REPORT|Command = PROTECTION_REPORT|Command = PROTECTION_REPORT|Command = PROTECTION_REPORT|Command = PROTECTION_REPORT|Command = PROTECTION_REPORT|Command = PROTECTION_REPORT|
|Reserved|Reserved|Reserved|Reserved|Local Protection State|Local Protection State|Local Protection State|Local Protection State|
|Reserved|Reserved|Reserved|Reserved|RF Protection State|RF Protection State|RF Protection State|RF Protection State|



For field description, refer to _Protection_ _set_ _command_ .


**2.2.79.3** **Protection** **supported** **get** **command**


This command is used to query supported protection capabilities.


The Protection Supported Report Command MUST be returned in response to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 2.458: Protection Supported Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_PROTECTION|Command Class = COMMAND_CLASS_PROTECTION|Command Class = COMMAND_CLASS_PROTECTION|Command Class = COMMAND_CLASS_PROTECTION|Command Class = COMMAND_CLASS_PROTECTION|Command Class = COMMAND_CLASS_PROTECTION|Command Class = COMMAND_CLASS_PROTECTION|Command Class = COMMAND_CLASS_PROTECTION|
|Command = PROTECTION_SUPPORTED_GET|Command = PROTECTION_SUPPORTED_GET|Command = PROTECTION_SUPPORTED_GET|Command = PROTECTION_SUPPORTED_GET|Command = PROTECTION_SUPPORTED_GET|Command = PROTECTION_SUPPORTED_GET|Command = PROTECTION_SUPPORTED_GET|Command = PROTECTION_SUPPORTED_GET|



**2.2.79.4** **Protection** **supported** **report** **command**


This command is used to advertise supported protection capabilities.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 373




<!-- PAGE 375 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Table 2.459: Protection Supported Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_PROTECTION|Command Class = COMMAND_CLASS_PROTECTION|Command Class = COMMAND_CLASS_PROTECTION|Command Class = COMMAND_CLASS_PROTECTION|Command Class = COMMAND_CLASS_PROTECTION|Command Class = COMMAND_CLASS_PROTECTION|Command Class = COMMAND_CLASS_PROTECTION|Command Class = COMMAND_CLASS_PROTECTION|
|Command = PROTECTION_SUPPORTED_REPORT|Command = PROTECTION_SUPPORTED_REPORT|Command = PROTECTION_SUPPORTED_REPORT|Command = PROTECTION_SUPPORTED_REPORT|Command = PROTECTION_SUPPORTED_REPORT|Command = PROTECTION_SUPPORTED_REPORT|Command = PROTECTION_SUPPORTED_REPORT|Command = PROTECTION_SUPPORTED_REPORT|
|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Exclusive Control|Timeout|
|Local Protection State Byte 1|Local Protection State Byte 1|Local Protection State Byte 1|Local Protection State Byte 1|Local Protection State Byte 1|Local Protection State Byte 1|Local Protection State Byte 1|Local Protection State Byte 1|
|Local Protection State Byte 2|Local Protection State Byte 2|Local Protection State Byte 2|Local Protection State Byte 2|Local Protection State Byte 2|Local Protection State Byte 2|Local Protection State Byte 2|Local Protection State Byte 2|
|RF Protection State Byte 1|RF Protection State Byte 1|RF Protection State Byte 1|RF Protection State Byte 1|RF Protection State Byte 1|RF Protection State Byte 1|RF Protection State Byte 1|RF Protection State Byte 1|
|RF Protection State Byte 2|RF Protection State Byte 2|RF Protection State Byte 2|RF Protection State Byte 2|RF Protection State Byte 2|RF Protection State Byte 2|RF Protection State Byte 2|RF Protection State Byte 2|



**Local** **Protection** **State** **Byte** **(2** **bytes)**


The list of all Local Protection States may be found in section Section 2.2.79.1. The two bytes MUST
be interpreted as bit masks where byte 1 bit 0 represent Local Protection State 0, byte 1 bit 1 represent
Protection State 1, byte 2 bit 0 represent Protection State 8 etc.


**RF** **Protection** **State** **Byte** **(2** **bytes)**


The list of all RF Protection States may be found in section Section 2.2.79.1. The two bytes MUST
be interpreted as bit masks where byte 1 bit 0 represent RF Protection State 0, byte 1 bit 1 represent
Protection State 1, byte 2 bit 0 represent Protection State 8 etc.


**Exclusive** **Control** **(1** **bit)**


When this bit is set to 1 the device support Exclusive Control. When Exclusive Control is supported
the device MUST support the Commands Protection Exclusive Control Set, Get and Report described
below.


**Timeout** **(1** **bit)**


When this bit is set to 1 the device supports a timeout for RF Protection State. When the timeout
is supported the device MUST support the Commands Protection Timeout Set, Get and Report
described below.


**2.2.79.5** **Protection** **exclusive** **control**


The Protection Exclusive Control is an optional feature. The Commands in this chapter can only
be implemented if the device supporting Protection Command Class version 2 announces support for
Exclusive Control in the Protection Supported Report Command.


**2.2.79.5.1** **Protection** **exclusive** **control** **set** **command**


This command is used to set the NodeID of a Z-Wave device that can override the protection state
in a protected device.


Table 2.460: Protection Exclusive Control Set Command


**NodeID**

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_PROTECTION|Command Class = COMMAND_CLASS_PROTECTION|Command Class = COMMAND_CLASS_PROTECTION|Command Class = COMMAND_CLASS_PROTECTION|Command Class = COMMAND_CLASS_PROTECTION|Command Class = COMMAND_CLASS_PROTECTION|Command Class = COMMAND_CLASS_PROTECTION|Command Class = COMMAND_CLASS_PROTECTION|
|Command = PROTECTION_EC_SET|Command = PROTECTION_EC_SET|Command = PROTECTION_EC_SET|Command = PROTECTION_EC_SET|Command = PROTECTION_EC_SET|Command = PROTECTION_EC_SET|Command = PROTECTION_EC_SET|Command = PROTECTION_EC_SET|
|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|



The NodeID that has exclusive control can override the RF protection state of the device and can
control it regardless of the protection state. Commands from any other nodes in the network may
be restricted by the RF protection state. In that case, the Application Rejected Request Command
MUST be returned.


All of the Protection Command Class commands will be accepted and processed regardless of whether
or not a node has exclusive control.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 374




<!-- PAGE 376 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Factory default setting of the NodeID for exclusive control MUST be set to 0. To reset the exclusive
control state in a device an Exclusive Control Set Command with NodeID 0 as parameter MUST be
send to the device.


**2.2.79.5.2** **Protection** **exclusive** **control** **get** **command**


Table 2.461: Protection Exclusive Control Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_PROTECTION|Command Class = COMMAND_CLASS_PROTECTION|Command Class = COMMAND_CLASS_PROTECTION|Command Class = COMMAND_CLASS_PROTECTION|Command Class = COMMAND_CLASS_PROTECTION|Command Class = COMMAND_CLASS_PROTECTION|Command Class = COMMAND_CLASS_PROTECTION|Command Class = COMMAND_CLASS_PROTECTION|
|Command = PROTECTION_EC_GET|Command = PROTECTION_EC_GET|Command = PROTECTION_EC_GET|Command = PROTECTION_EC_GET|Command = PROTECTION_EC_GET|Command = PROTECTION_EC_GET|Command = PROTECTION_EC_GET|Command = PROTECTION_EC_GET|



**2.2.79.5.3** **Protection** **exclusive** **control** **report** **command**


This command is used to return the NodeID of a Z-Wave device that has exclusive control over this

device in protection mode.


Table 2.462: Protection Exclusive Control Report Command


**NodeID**

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_PROTECTION|Command Class = COMMAND_CLASS_PROTECTION|Command Class = COMMAND_CLASS_PROTECTION|Command Class = COMMAND_CLASS_PROTECTION|Command Class = COMMAND_CLASS_PROTECTION|Command Class = COMMAND_CLASS_PROTECTION|Command Class = COMMAND_CLASS_PROTECTION|Command Class = COMMAND_CLASS_PROTECTION|
|Command = PROTECTION_EC_REPORT|Command = PROTECTION_EC_REPORT|Command = PROTECTION_EC_REPORT|Command = PROTECTION_EC_REPORT|Command = PROTECTION_EC_REPORT|Command = PROTECTION_EC_REPORT|Command = PROTECTION_EC_REPORT|Command = PROTECTION_EC_REPORT|
|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|



See description under the Protection Exclusive Control Set Command section Section 2.2.79.5.1.


**2.2.79.6** **Protection** **timeout**


The Protection Timeout is an optional feature. The Commands in this section MAY be implemented
if the device supporting Protection Command Class version 2 announces support for Timeout in the
Protection Supported Report Command.


**2.2.79.6.1** **Protection** **timeout** **set** **command**


This command is used to set the timeout for protection mode in a device.


Table 2.463: Protection Timeout Set Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_PROTECTION|Command Class = COMMAND_CLASS_PROTECTION|Command Class = COMMAND_CLASS_PROTECTION|Command Class = COMMAND_CLASS_PROTECTION|Command Class = COMMAND_CLASS_PROTECTION|Command Class = COMMAND_CLASS_PROTECTION|Command Class = COMMAND_CLASS_PROTECTION|Command Class = COMMAND_CLASS_PROTECTION|
|Command = PROTECTION_TIMEOUT_SET|Command = PROTECTION_TIMEOUT_SET|Command = PROTECTION_TIMEOUT_SET|Command = PROTECTION_TIMEOUT_SET|Command = PROTECTION_TIMEOUT_SET|Command = PROTECTION_TIMEOUT_SET|Command = PROTECTION_TIMEOUT_SET|Command = PROTECTION_TIMEOUT_SET|
|Timeout|Timeout|Timeout|Timeout|Timeout|Timeout|Timeout|Timeout|



**Timeout**


The timeout describes the time that a device MUST remain in RF Protection mode.

Factory default setting for the Timeout parameter MUST be 0x00. This field MUST be encoded
according to Table 2.464.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 375




<!-- PAGE 377 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024

|RF Protection|Table 2.464: Protection Timeout Set::Timeout encoding Description|
|---|---|
|**RF**<br>**Protection**<br>**State**|**Description**|
|0x00|No timer is set. All “normal operation” Commands MUST be accepted.|
|0x01-0x3C|Timeout is set from 1 second (0x01) to 60 seconds (0x3C) in 1-second resolu-<br>tion.|
|0x41-0xFE|Timeout is set from 2 minutes (0x41) to 191 minutes (0xFE) in 1-minute<br>resolution.<br>|
|0xFF|No Timeout – The Device will remain in RF Protection mode infnitely.|



All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.


**2.2.79.6.2** **Protection** **timeout** **get** **command**


This command is used to request a Protection Timeout Report Command from the device.


The Protection Timeout Report Command MUST be returned in response to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 2.465: Protection Timeout get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_PROTECTION|Command Class = COMMAND_CLASS_PROTECTION|Command Class = COMMAND_CLASS_PROTECTION|Command Class = COMMAND_CLASS_PROTECTION|Command Class = COMMAND_CLASS_PROTECTION|Command Class = COMMAND_CLASS_PROTECTION|Command Class = COMMAND_CLASS_PROTECTION|Command Class = COMMAND_CLASS_PROTECTION|
|Command = PROTECTION_TIMEOUT_GET|Command = PROTECTION_TIMEOUT_GET|Command = PROTECTION_TIMEOUT_GET|Command = PROTECTION_TIMEOUT_GET|Command = PROTECTION_TIMEOUT_GET|Command = PROTECTION_TIMEOUT_GET|Command = PROTECTION_TIMEOUT_GET|Command = PROTECTION_TIMEOUT_GET|



**2.2.79.6.3** **Protection** **timeout** **report** **command**


This command is used to return the remaining time that a device will remain in protection mode.


Table 2.466: Protection Timeout Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_PROTECTION|Command Class = COMMAND_CLASS_PROTECTION|Command Class = COMMAND_CLASS_PROTECTION|Command Class = COMMAND_CLASS_PROTECTION|Command Class = COMMAND_CLASS_PROTECTION|Command Class = COMMAND_CLASS_PROTECTION|Command Class = COMMAND_CLASS_PROTECTION|Command Class = COMMAND_CLASS_PROTECTION|
|Command = PROTECTION_TIMEOUT_REPORT|Command = PROTECTION_TIMEOUT_REPORT|Command = PROTECTION_TIMEOUT_REPORT|Command = PROTECTION_TIMEOUT_REPORT|Command = PROTECTION_TIMEOUT_REPORT|Command = PROTECTION_TIMEOUT_REPORT|Command = PROTECTION_TIMEOUT_REPORT|Command = PROTECTION_TIMEOUT_REPORT|
|Timeout|Timeout|Timeout|Timeout|Timeout|Timeout|Timeout|Timeout|



**Timeout**

This field indicates the remaining timeout set in the Node. It MUST be encoded as described in Table
2.464


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 376