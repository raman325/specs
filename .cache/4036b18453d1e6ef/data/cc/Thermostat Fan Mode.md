<!-- PAGE 482 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.104** **Thermostat** **Fan** **Mode** **Command** **Class,** **version** **1**


The Thermostat Fan Mode Command Class, version 1 used for the HVAC’s systems manual fan.


**2.2.104.1** **Thermostat** **Fan** **Mode** **Set** **Command**


This command is used to set the fan mode in the device.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|
|Command = THERMOSTAT_FAN_MODE_SET|Command = THERMOSTAT_FAN_MODE_SET|Command = THERMOSTAT_FAN_MODE_SET|Command = THERMOSTAT_FAN_MODE_SET|Command = THERMOSTAT_FAN_MODE_SET|Command = THERMOSTAT_FAN_MODE_SET|Command = THERMOSTAT_FAN_MODE_SET|Command = THERMOSTAT_FAN_MODE_SET|
|Reserved|Reserved|Reserved|Reserved|Fan Mode|Fan Mode|Fan Mode|Fan Mode|



**Fan** **Mode** **(8** **bits)**

This field MUST comply with the values indicated for version 1 in Table 2.521.


**Reserved**

This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**2.2.104.2** **Thermostat** **Fan** **Mode** **Get** **Command**


This command is used to request the fan mode in the device.


The Thermostat Fan Mode Report Command MUST be returned in response to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|
|Command = THERMOSTAT_FAN_MODE_GET|Command = THERMOSTAT_FAN_MODE_GET|Command = THERMOSTAT_FAN_MODE_GET|Command = THERMOSTAT_FAN_MODE_GET|Command = THERMOSTAT_FAN_MODE_GET|Command = THERMOSTAT_FAN_MODE_GET|Command = THERMOSTAT_FAN_MODE_GET|Command = THERMOSTAT_FAN_MODE_GET|



**2.2.104.3** **Thermostat** **Fan** **Mode** **Report** **Command**


This command is used to report the fan mode in a device.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|
|Command = THERMOSTAT_FAN_MODE_GET|Command = THERMOSTAT_FAN_MODE_GET|Command = THERMOSTAT_FAN_MODE_GET|Command = THERMOSTAT_FAN_MODE_GET|Command = THERMOSTAT_FAN_MODE_GET|Command = THERMOSTAT_FAN_MODE_GET|Command = THERMOSTAT_FAN_MODE_GET|Command = THERMOSTAT_FAN_MODE_GET|
|Reserved|Reserved|Reserved|Reserved|Fan Mode|Fan Mode|Fan Mode|Fan Mode|



**Fan** **Mode** **(8** **bits)**


Refer to description under Thermostat Fan Mode Set Command (Section 2.2.104.1).


**Reserved**

This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 481




<!-- PAGE 483 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.104.4** **Thermostat** **Fan** **Mode** **Supported** **Get** **Command**


This command is used to request the supported fan modes from the device.


The Thermostat Fan Mode Supported Report Command MUST be returned in response to this
command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|
|Command = THERMOSTAT_FAN_MODE_SUPPORTED_GET|Command = THERMOSTAT_FAN_MODE_SUPPORTED_GET|Command = THERMOSTAT_FAN_MODE_SUPPORTED_GET|Command = THERMOSTAT_FAN_MODE_SUPPORTED_GET|Command = THERMOSTAT_FAN_MODE_SUPPORTED_GET|Command = THERMOSTAT_FAN_MODE_SUPPORTED_GET|Command = THERMOSTAT_FAN_MODE_SUPPORTED_GET|Command = THERMOSTAT_FAN_MODE_SUPPORTED_GET|



**2.2.104.5** **Thermostat** **Fan** **Mode** **Supported** **Report** **Command**


This command is used to report the supported fan modes from the device.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|
|Command = THERMOSTAT_FAN_MODE_SUPPORTED_REPORT|Command = THERMOSTAT_FAN_MODE_SUPPORTED_REPORT|Command = THERMOSTAT_FAN_MODE_SUPPORTED_REPORT|Command = THERMOSTAT_FAN_MODE_SUPPORTED_REPORT|Command = THERMOSTAT_FAN_MODE_SUPPORTED_REPORT|Command = THERMOSTAT_FAN_MODE_SUPPORTED_REPORT|Command = THERMOSTAT_FAN_MODE_SUPPORTED_REPORT|Command = THERMOSTAT_FAN_MODE_SUPPORTED_REPORT|
|Bit Mask 1|Bit Mask 1|Bit Mask 1|Bit Mask 1|Bit Mask 1|Bit Mask 1|Bit Mask 1|Bit Mask 1|
|…|…|…|…|…|…|…|…|
|Bit Mask N|Bit Mask N|Bit Mask N|Bit Mask N|Bit Mask N|Bit Mask N|Bit Mask N|Bit Mask N|



**Bit** **Mask** **(N** **bytes)**

The Bit Mask fields describe the supported fan modes by the thermostat.


 - Bit 0 in Bit Mask 1 indicates if Fan Mode = 0 (Auto / Auto Low) is supported.


 - Bit 1 in Bit Mask 1 indicates if Fan Mode = 1 (On / On Low) is supported.


 - …


If a Fan Mode is supported the bit MUST be set to 1. If a Fan Mode is not supported the bit MUST
be set to 0. It is only necessary to send the Bit Mask fields from 1 and up to the one indicating the
last supported fan mode. The number of Bit Mask fields transmitted MUST be determined from the
length field in the frame.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 482

---

<!-- PAGE 484 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.105** **Thermostat** **Fan** **Mode** **Command** **Class,** **version** **2**


The Thermostat Fan Mode Command Class, version 2 is used for the HVAC’s systems manual fan.

The commands not mentioned here will remain the same as specified for Thermostat Fan Mode
Command Class (Version 1).


**2.2.105.1** **Thermostat** **Fan** **Mode** **Set** **Command**


This command is used to set the fan mode in the device

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|
|Command = THERMOSTAT_FAN_MODE_SET<br>|Command = THERMOSTAT_FAN_MODE_SET<br>|Command = THERMOSTAT_FAN_MODE_SET<br>|Command = THERMOSTAT_FAN_MODE_SET<br>|Command = THERMOSTAT_FAN_MODE_SET<br>|Command = THERMOSTAT_FAN_MODE_SET<br>|Command = THERMOSTAT_FAN_MODE_SET<br>|Command = THERMOSTAT_FAN_MODE_SET<br>|
|Of|Reserved|Reserved|Reserved|Fan Mode|Fan Mode|Fan Mode|Fan Mode|



**Off** **(1** **bit)**

The “Off bit” set to “1” will switch the fan fully OFF regardless of what fan mode has been set. In
order to activate a fan mode the “Off bit” MUST be set to “0”.


**Fan** **Mode** **(4** **bits)**

This field MUST comply with the values indicated for version 2 and older in Table 2.521.


**Reserved**

This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**2.2.105.2** **Thermostat** **Fan** **Mode** **Report** **Command**


This command is used to report the fan mode in a device.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|
|Command = THERMOSTAT_FAN_MODE_SET|Command = THERMOSTAT_FAN_MODE_SET|Command = THERMOSTAT_FAN_MODE_SET|Command = THERMOSTAT_FAN_MODE_SET|Command = THERMOSTAT_FAN_MODE_SET|Command = THERMOSTAT_FAN_MODE_SET|Command = THERMOSTAT_FAN_MODE_SET|Command = THERMOSTAT_FAN_MODE_SET|
|Reserved|Reserved|Reserved|Reserved|Fan Mode|Fan Mode|Fan Mode|Fan Mode|



**Fan** **Mode** **(4** **bits)**


Refer to description under the Thermostat Fan Mode Set Command.


**Reserved**

This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 483

---

<!-- PAGE 485 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.106** **Thermostat** **Fan** **Mode** **Command** **Class,** **version** **3**


The Thermostat Fan Mode Command Class, version 3 is used for the HVAC’s systems manual fan.


**2.2.106.1** **Thermostat** **Fan** **Mode** **Set** **Command**


This command is used to set the fan mode in the device.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|
|Command = THERMOSTAT_FAN_MODE_SET<br>|Command = THERMOSTAT_FAN_MODE_SET<br>|Command = THERMOSTAT_FAN_MODE_SET<br>|Command = THERMOSTAT_FAN_MODE_SET<br>|Command = THERMOSTAT_FAN_MODE_SET<br>|Command = THERMOSTAT_FAN_MODE_SET<br>|Command = THERMOSTAT_FAN_MODE_SET<br>|Command = THERMOSTAT_FAN_MODE_SET<br>|
|Of|Reserved|Reserved|Reserved|Fan Mode|Fan Mode|Fan Mode|Fan Mode|



**Reserved**

This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.

**Off** **(1** **bit)**

The “Off bit” set to “1” will switch the fan fully OFF. In order to activate a fan mode the “Off bit”
MUST be set to “0”. However, for some applications it is critical that the fan is ON in certain modes.
In this case, the application can decide to ignore the Off bit.


**Fan** **Mode** **(4** **bits)**

This field MUST comply with the values indicated for version 3 and older in Table 2.521.


**2.2.106.2** **Thermostat** **Fan** **Mode** **Get** **Command**


This command is used to request the fan mode in the device.


The Thermostat Fan Mode Report Command MUST be returned in response to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|
|Command = THERMOSTAT_FAN_MODE_GET|Command = THERMOSTAT_FAN_MODE_GET|Command = THERMOSTAT_FAN_MODE_GET|Command = THERMOSTAT_FAN_MODE_GET|Command = THERMOSTAT_FAN_MODE_GET|Command = THERMOSTAT_FAN_MODE_GET|Command = THERMOSTAT_FAN_MODE_GET|Command = THERMOSTAT_FAN_MODE_GET|



**2.2.106.3** **Thermostat** **Fan** **Mode** **Report** **Command**


This command is used to report the fan mode in a device.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|
|Command = THERMOSTAT_FAN_MODE_REPORT|Command = THERMOSTAT_FAN_MODE_REPORT|Command = THERMOSTAT_FAN_MODE_REPORT|Command = THERMOSTAT_FAN_MODE_REPORT|Command = THERMOSTAT_FAN_MODE_REPORT|Command = THERMOSTAT_FAN_MODE_REPORT|Command = THERMOSTAT_FAN_MODE_REPORT|Command = THERMOSTAT_FAN_MODE_REPORT|



**Fan** **Mode** **(4** **bits)**


Refer to description under Thermostat Fan Mode Set Command (Section 2.2.106.1).


**Reserved**

This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.

**Off** **(1** **bit)**


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 484




<!-- PAGE 486 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


The “Off bit” set to “1” indicates that the fan is fully OFF. The “Off bit” set to “0” indicates that it
is possible to change between Fan Modes.


For some applications, it is critical that the fan is ON in certain modes. In this case, the application
can decide to ignore the Off bit. This means that the Off bit in the Report MUST always be set to
“0”


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 485




<!-- PAGE 487 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.107** **Thermostat** **Fan** **Mode** **Command** **Class,** **version** **4-5**


The Thermostat Fan Mode Command Class is an extension to support control and status monitoring
functions of air-conditioning devices in order to achieve a global framework that covers the majority
of generic functions implemented by world-wide air-conditioning manufacturer. The new features
comprises of new Thermostat Fan Modes.


**2.2.107.1** **Thermostat** **Fan** **Mode** **Set** **Command**


This command is used to set the fan mode in the device.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|
|Command = THERMOSTAT_FAN_MODE_SET|Command = THERMOSTAT_FAN_MODE_SET|Command = THERMOSTAT_FAN_MODE_SET|Command = THERMOSTAT_FAN_MODE_SET|Command = THERMOSTAT_FAN_MODE_SET|Command = THERMOSTAT_FAN_MODE_SET|Command = THERMOSTAT_FAN_MODE_SET|Command = THERMOSTAT_FAN_MODE_SET|



**Reserved**

This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.

**Off** **(1** **bit)**

“Off bit” set to “1” will switch the fan fully OFF. In order to activate a fan mode the “Off bit” MUST
be set to “0”. However for some applications it is critical that the fan is ON in certain modes. In this
case the application may ignore the off bit.


**Fan** **Mode** **(4** **bits)**


If the device transmitting the Thermostat Fan Mode Set command attempts to set a non-supported
mode, the receiving thermostat device MUST ignore the command.


Table 2.521: Thermostat Fan Mode Set version 4::Fan Mode en





















|Table 2.521: Ther coding Fan Mode (4 bits)|Col2|rmostat Fan Mode Set version 4::Fan Mode en- Description|CC Version|
|---|---|---|---|
|Fan Mode (4 bits)|Fan Mode (4 bits)|Description<br>|CC Version|
|0x00|AUTO LOW|Will turn the manual fan operation of unless<br>turned on by the manufacturer specifc “auto<br>low” algorithms.|1|
|0x01|LOW|Will turn the manual fan operation on.<br>Low speed is selected.<br>|1|
|0x02|AUTO HIGH|Will turn the manual fan operation of unless<br>turned on by the manufacturer specifc “auto<br>high” algorithms.|1|
|0x03|HIGH|Will turn the manual fan operation on.<br>High speed is selected.<br>|1|
|0x04|AUTO<br>MEDIUM|Will turn the manual fan operation of unless<br>turned on by the manufacturer specifc “auto<br>medium” algorithms.|2|
|0x05|MEDIUM|Will turn the manual fan operation on.<br>Medium speed is selected.<br>|2|
|0x06|CIRCULATION|Will turn the manual fan operation of unless<br>turned on by the manufacturer specifc circum-<br>lation algorithms.<br>|3|
|0x07|HUMIDITY<br>CIRCULATION|Will turn the manual fan operation of unless<br>turned on by the manufacturer specifc “humid-<br>ity circulation” algorithms.<br>|3|
|0x08|LEFT & RIGHT|Will turn the manual fan operation of unless<br>turned on by the manufacturer specifc “left &<br>right” circulation algorithms.|4|



continues on next page


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 486




<!-- PAGE 488 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024















|Table Fan Mode (4 bits)|Col2|2.521 – continued from previous page Description|CC Version|
|---|---|---|---|
|Fan Mode (4 bits)|Fan Mode (4 bits)|Description<br>|CC Version|
|0x09|UP & DOWN|Will turn the manual fan operation of unless<br>turned on by the manufacturer specifc “up &<br>down” circulation algorithms.<br>|4|
|0x0A|QUIET|Will turn the manual fan operation of unless<br>turned on by the manufacturer specifc “quiet”<br>algorithms.<br>|4|
|0x0B|EXTERNAL<br>CIRCULATION|Will turn the manual fan operation of unless<br>turned on by the manufacturer specifc circula-<br>tion algorithms.<br>This mode will circulate fresh air from the out-<br>side.|5|
|0x0C..0x0F|Reserved|These values/modes are reserved for future use.<br>The values cannot be supported by any device<br>and will be ignored.|-|


**2.2.107.2** **Thermostat** **Fan** **Mode** **Get** **Command**


This command is used to request the fan mode in the device.



The Thermostat Fan Mode Report Command MUST be returned in response to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|
|Command = THERMOSTAT_FAN_MODE_GET|Command = THERMOSTAT_FAN_MODE_GET|Command = THERMOSTAT_FAN_MODE_GET|Command = THERMOSTAT_FAN_MODE_GET|Command = THERMOSTAT_FAN_MODE_GET|Command = THERMOSTAT_FAN_MODE_GET|Command = THERMOSTAT_FAN_MODE_GET|Command = THERMOSTAT_FAN_MODE_GET|



**2.2.107.3** **Thermostat** **Fan** **Mode** **Report** **Command**


This command is used to report the fan mode in a device.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|
|Command = THERMOSTAT_FAN_MODE_REPORT|Command = THERMOSTAT_FAN_MODE_REPORT|Command = THERMOSTAT_FAN_MODE_REPORT|Command = THERMOSTAT_FAN_MODE_REPORT|Command = THERMOSTAT_FAN_MODE_REPORT|Command = THERMOSTAT_FAN_MODE_REPORT|Command = THERMOSTAT_FAN_MODE_REPORT|Command = THERMOSTAT_FAN_MODE_REPORT|



Refer to Thermostat Fan Mode Set command (Section 2.2.107.1) for parameter/field descriptions.


**2.2.107.4** **Thermostat** **Fan** **Mode** **Supported** **Get** **Command**


This command is used to request the supported modes from the device.


The Thermostat Fan Mode Supported Report Command MUST be returned in response to this
command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 487




<!-- PAGE 489 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|
|Command = THERMOSTAT_FAN_MODE_SUPPORTED_GET|Command = THERMOSTAT_FAN_MODE_SUPPORTED_GET|Command = THERMOSTAT_FAN_MODE_SUPPORTED_GET|Command = THERMOSTAT_FAN_MODE_SUPPORTED_GET|Command = THERMOSTAT_FAN_MODE_SUPPORTED_GET|Command = THERMOSTAT_FAN_MODE_SUPPORTED_GET|Command = THERMOSTAT_FAN_MODE_SUPPORTED_GET|Command = THERMOSTAT_FAN_MODE_SUPPORTED_GET|



**2.2.107.5** **Thermostat** **Fan** **Mode** **Supported** **Report** **Command**


This command is used to report the supported thermostat modes from the device.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|
|Command = THERMOSTAT_FAN_MODE_SUPPORTED_REPORT|Command = THERMOSTAT_FAN_MODE_SUPPORTED_REPORT|Command = THERMOSTAT_FAN_MODE_SUPPORTED_REPORT|Command = THERMOSTAT_FAN_MODE_SUPPORTED_REPORT|Command = THERMOSTAT_FAN_MODE_SUPPORTED_REPORT|Command = THERMOSTAT_FAN_MODE_SUPPORTED_REPORT|Command = THERMOSTAT_FAN_MODE_SUPPORTED_REPORT|Command = THERMOSTAT_FAN_MODE_SUPPORTED_REPORT|
|Bit Mask 1|Bit Mask 1|Bit Mask 1|Bit Mask 1|Bit Mask 1|Bit Mask 1|Bit Mask 1|Bit Mask 1|
|…|…|…|…|…|…|…|…|
|Bit Mask N|Bit Mask N|Bit Mask N|Bit Mask N|Bit Mask N|Bit Mask N|Bit Mask N|Bit Mask N|



**Bit** **Mask** **(N** **bytes)**

The Bit Mask fields describe the supported modes by the device. Refer to Thermostat Fan Mode Set
Command (Section 2.2.107.1).

 - Bit 0 in Bit Mask 1 field indicates support for mode = 0 (AUTO LOW)

 - Bit 1 in Bit Mask 1 field indicates support for mode = 1 (LOW)

 - Bit 2 in Bit Mask 1 field indicates support for mode = 2 (AUTO HIGH)


 - …


The mode is supported if the bit is 1 and the opposite if 0. It is only necessary to send the Bit Mask
fields from 1 and up to the one indicating the last supported mode. The number of Bit Mask fields
transmitted MUST be determined from the length field in the frame.


**Example:**


To indicate the thermostat device supports AUTO LOW, AUTO HIGH and AUTO MEDIUM, the
Thermostat Fan Mode Supported Report command MUST be structured as illustrated below.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_MODE|
|Command = THERMOSTAT_FAN_MODE_SUPPORTED_REPORT|Command = THERMOSTAT_FAN_MODE_SUPPORTED_REPORT|Command = THERMOSTAT_FAN_MODE_SUPPORTED_REPORT|Command = THERMOSTAT_FAN_MODE_SUPPORTED_REPORT|Command = THERMOSTAT_FAN_MODE_SUPPORTED_REPORT|Command = THERMOSTAT_FAN_MODE_SUPPORTED_REPORT|Command = THERMOSTAT_FAN_MODE_SUPPORTED_REPORT|Command = THERMOSTAT_FAN_MODE_SUPPORTED_REPORT|
|0|0|0|**1**|0|**1**|0|**1**|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 488




<!-- PAGE 490 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.108** **Thermostat** **Fan** **State** **Command** **Class,** **version** **1-2**


The Thermostat Fan State Command Class is used to obtain the fan operating state of the thermostat.


**2.2.108.1** **Compatibility** **Considerations**


A device supporting Thermostat Fan State CC, Version 2 MUST support Thermostat Fan State CC,
Version 1.

Version 2 adds Fan Operating State identifiers for use in the Thermostat Fan State Report Command.


Commands not described in Version 2 stays unchanged from version 1.


**2.2.108.2** **Thermostat** **Fan** **State** **Get** **Command**


This command is used to request the fan operating state from the device.


The Thermostat Fan State Report Command MUST be returned in response to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_STATE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_STATE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_STATE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_STATE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_STATE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_STATE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_STATE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_STATE|
|Command = THERMOSTAT_FAN_STATE_GET|Command = THERMOSTAT_FAN_STATE_GET|Command = THERMOSTAT_FAN_STATE_GET|Command = THERMOSTAT_FAN_STATE_GET|Command = THERMOSTAT_FAN_STATE_GET|Command = THERMOSTAT_FAN_STATE_GET|Command = THERMOSTAT_FAN_STATE_GET|Command = THERMOSTAT_FAN_STATE_GET|



**2.2.108.3** **Thermostat** **Fan** **State** **Report** **Command**


This command is used to report the fan operating state of the device.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_STATE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_STATE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_STATE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_STATE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_STATE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_STATE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_STATE|Command Class = COMMAND_CLASS_THERMOSTAT_FAN_STATE|
|Command = THERMOSTAT_FAN_STATE_REPORT|Command = THERMOSTAT_FAN_STATE_REPORT|Command = THERMOSTAT_FAN_STATE_REPORT|Command = THERMOSTAT_FAN_STATE_REPORT|Command = THERMOSTAT_FAN_STATE_REPORT|Command = THERMOSTAT_FAN_STATE_REPORT|Command = THERMOSTAT_FAN_STATE_REPORT|Command = THERMOSTAT_FAN_STATE_REPORT|
|Reserved|Reserved|Reserved|Reserved|Fan Operating State|Fan Operating State|Fan Operating State|Fan Operating State|



**Reserved**

This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**Fan** **Operating** **State** **(4** **bits)**

The fan operating state identifier MUST comply with Table 2.522.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 489




<!-- PAGE 491 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Table 2.522: Thermostat Fan State Report::Fan Operating State
encoding

|Fan Operating State|Description|CC Version|
|---|---|---|
|0|Idle/Of|1|
|1|Running/Running Low - If device only supports one fan<br>speed, this state is used to report the fan is running. If the<br>device is a multi-speed device, this state is used to report<br>that the fan is running at the low speed.|1|
|2|Running High|1|
|3|Running Medium|2|
|4|Circulation Mode|2|
|5|Humidity Circulation Mode|2|
|6|Right-Left Circulation Mode|2|
|7|Up-Down Circulation Mode|2|
|8|Quiet Circulation Mode|2|



All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 490




<!-- PAGE 492 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.109** **Thermostat** **Mode** **Command** **Class,** **version** **1-2**


The Thermostat Mode Command Class is used to control which mode a thermostat operates.


**2.2.109.1** **Interoperability** **Considerations**


Most thermostat modes require a supporting node to have an associated setpoint, which can managed
with the Thermostat Setpoint Command Class. A node supporting this Command Class SHOULD
support the Thermostat Setpoint Command Class.


**2.2.109.2** **Thermostat** **Mode** **Set** **Command**


This command is used to set the thermostat mode at the receiving node.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_THERMOSTAT_MODE (0x40)|Command Class = COMMAND_CLASS_THERMOSTAT_MODE (0x40)|Command Class = COMMAND_CLASS_THERMOSTAT_MODE (0x40)|Command Class = COMMAND_CLASS_THERMOSTAT_MODE (0x40)|Command Class = COMMAND_CLASS_THERMOSTAT_MODE (0x40)|Command Class = COMMAND_CLASS_THERMOSTAT_MODE (0x40)|Command Class = COMMAND_CLASS_THERMOSTAT_MODE (0x40)|Command Class = COMMAND_CLASS_THERMOSTAT_MODE (0x40)|
|Command = THERMOSTAT_MODE_SET (0x01)|Command = THERMOSTAT_MODE_SET (0x01)|Command = THERMOSTAT_MODE_SET (0x01)|Command = THERMOSTAT_MODE_SET (0x01)|Command = THERMOSTAT_MODE_SET (0x01)|Command = THERMOSTAT_MODE_SET (0x01)|Command = THERMOSTAT_MODE_SET (0x01)|Command = THERMOSTAT_MODE_SET (0x01)|
|Reserved|Reserved|Reserved|Mode|Mode|Mode|Mode|Mode|



**Reserved**

This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**Mode** **(5** **bits)**

This field is used to set the thermostat mode at the receiving node.

This field MUST be encoded according to Table 2.523.


**2.2.109.3** **Thermostat** **Mode** **Get** **Command**


This command is used to request the current mode set at the receiving node.


The Thermostat Mode Report Command MUST be returned in response to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_THERMOSTAT_MODE (0x40)|Command Class = COMMAND_CLASS_THERMOSTAT_MODE (0x40)|Command Class = COMMAND_CLASS_THERMOSTAT_MODE (0x40)|Command Class = COMMAND_CLASS_THERMOSTAT_MODE (0x40)|Command Class = COMMAND_CLASS_THERMOSTAT_MODE (0x40)|Command Class = COMMAND_CLASS_THERMOSTAT_MODE (0x40)|Command Class = COMMAND_CLASS_THERMOSTAT_MODE (0x40)|Command Class = COMMAND_CLASS_THERMOSTAT_MODE (0x40)|
|Command = THERMOSTAT_MODE_GET (0x02)|Command = THERMOSTAT_MODE_GET (0x02)|Command = THERMOSTAT_MODE_GET (0x02)|Command = THERMOSTAT_MODE_GET (0x02)|Command = THERMOSTAT_MODE_GET (0x02)|Command = THERMOSTAT_MODE_GET (0x02)|Command = THERMOSTAT_MODE_GET (0x02)|Command = THERMOSTAT_MODE_GET (0x02)|



**2.2.109.4** **Thermostat** **Mode** **Report** **Command**


This command is used to report the mode from the device.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_THERMOSTAT_MODE (0x40)|Command Class = COMMAND_CLASS_THERMOSTAT_MODE (0x40)|Command Class = COMMAND_CLASS_THERMOSTAT_MODE (0x40)|Command Class = COMMAND_CLASS_THERMOSTAT_MODE (0x40)|Command Class = COMMAND_CLASS_THERMOSTAT_MODE (0x40)|Command Class = COMMAND_CLASS_THERMOSTAT_MODE (0x40)|Command Class = COMMAND_CLASS_THERMOSTAT_MODE (0x40)|Command Class = COMMAND_CLASS_THERMOSTAT_MODE (0x40)|
|Command = THERMOSTAT_MODE_REPORT (0X03)|Command = THERMOSTAT_MODE_REPORT (0X03)|Command = THERMOSTAT_MODE_REPORT (0X03)|Command = THERMOSTAT_MODE_REPORT (0X03)|Command = THERMOSTAT_MODE_REPORT (0X03)|Command = THERMOSTAT_MODE_REPORT (0X03)|Command = THERMOSTAT_MODE_REPORT (0X03)|Command = THERMOSTAT_MODE_REPORT (0X03)|
|Reserved|Reserved|Reserved|Mode|Mode|Mode|Mode|Mode|



**Reserved**

This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 491




<!-- PAGE 493 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**Mode** **(5** **bits)**

This field is used to advertise the current thermostat mode at the receiving node.

This field MUST be encoded according to Table 2.523.

This field MUST NOT be set to 0x05 (RESUME(ON)) in this command.


**2.2.109.5** **Thermostat** **Mode** **Supported** **Get** **Command**


This command is used to request the supported modes of a node.


The Thermostat Mode Supported Report Command MUST be returned in response to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_THERMOSTAT_MODE (0x40)|Command Class = COMMAND_CLASS_THERMOSTAT_MODE (0x40)|Command Class = COMMAND_CLASS_THERMOSTAT_MODE (0x40)|Command Class = COMMAND_CLASS_THERMOSTAT_MODE (0x40)|Command Class = COMMAND_CLASS_THERMOSTAT_MODE (0x40)|Command Class = COMMAND_CLASS_THERMOSTAT_MODE (0x40)|Command Class = COMMAND_CLASS_THERMOSTAT_MODE (0x40)|Command Class = COMMAND_CLASS_THERMOSTAT_MODE (0x40)|
|Command = THERMOSTAT_MODE_SUPPORTED_GET (0x04)|Command = THERMOSTAT_MODE_SUPPORTED_GET (0x04)|Command = THERMOSTAT_MODE_SUPPORTED_GET (0x04)|Command = THERMOSTAT_MODE_SUPPORTED_GET (0x04)|Command = THERMOSTAT_MODE_SUPPORTED_GET (0x04)|Command = THERMOSTAT_MODE_SUPPORTED_GET (0x04)|Command = THERMOSTAT_MODE_SUPPORTED_GET (0x04)|Command = THERMOSTAT_MODE_SUPPORTED_GET (0x04)|



**2.2.109.6** **Thermostat** **Mode** **Supported** **Report** **Command**


This command is used to advertise which modes are supported by the sending node.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_THERMOSTAT_MODE (0x40)|Command Class = COMMAND_CLASS_THERMOSTAT_MODE (0x40)|Command Class = COMMAND_CLASS_THERMOSTAT_MODE (0x40)|Command Class = COMMAND_CLASS_THERMOSTAT_MODE (0x40)|Command Class = COMMAND_CLASS_THERMOSTAT_MODE (0x40)|Command Class = COMMAND_CLASS_THERMOSTAT_MODE (0x40)|Command Class = COMMAND_CLASS_THERMOSTAT_MODE (0x40)|Command Class = COMMAND_CLASS_THERMOSTAT_MODE (0x40)|
|Command = THERMOSTAT_MODE_SUPPORTED_REPORT (0x05)|Command = THERMOSTAT_MODE_SUPPORTED_REPORT (0x05)|Command = THERMOSTAT_MODE_SUPPORTED_REPORT (0x05)|Command = THERMOSTAT_MODE_SUPPORTED_REPORT (0x05)|Command = THERMOSTAT_MODE_SUPPORTED_REPORT (0x05)|Command = THERMOSTAT_MODE_SUPPORTED_REPORT (0x05)|Command = THERMOSTAT_MODE_SUPPORTED_REPORT (0x05)|Command = THERMOSTAT_MODE_SUPPORTED_REPORT (0x05)|
|Bit Mask 1|Bit Mask 1|Bit Mask 1|Bit Mask 1|Bit Mask 1|Bit Mask 1|Bit Mask 1|Bit Mask 1|
|…|…|…|…|…|…|…|…|
|Bit Mask N|Bit Mask N|Bit Mask N|Bit Mask N|Bit Mask N|Bit Mask N|Bit Mask N|Bit Mask N|



**Bit** **Mask** **(N** **bytes)**

This field advertises the Modes supported by the supporting node.


A supporting node MUST support at least one mode. Modes and their minimum required version are
described in Table 2.523. A node MUST NOT support a mode associated to a newer version than the
version it supports.

 - Bit 0 in Bit Mask 1 represents Mode = 0x00 (Off).


 - Bit 1 in Bit Mask 1 represents Mode = 0x01 (Heat).


 - …


If a Mode is supported, the corresponding bit MUST be set to ‘1’.


If a Mode is not supported, the corresponding bit MUST be set to ‘0’.

This length of this field MUST be set to the minimum amount of bytes which allows advertising all
supported Modes.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 492