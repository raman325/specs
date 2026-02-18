<!-- PAGE 206 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.41** **Energy** **Production** **Command** **Class,** **version** **1** **[NEVER** **CERTIFIED]**


**Warning:** **THIS** **COMMAND** **CLASS** **HAS** **NEVER** **BEEN** **CERTIFIED**

This command class has never been implemented and certified by a Z-Wave product Therefore,
this Command Class definition MAY be updated in a non-backwards compatible manner, or even
removed.


Consult with the Z-Wave Alliance Application Work Group if you consider implementing this
Command Class.


The Energy Production Command Class is used to retrieve various production data from the device.


**2.2.41.1** **Energy** **Production** **Get** **Command**


This command is used to request various production data from the device.


The Energy Production Report Command MUST be returned in response to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 2.219: Energy Production Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_ENERGY_PRODUCTION|Command Class = COMMAND_CLASS_ENERGY_PRODUCTION|Command Class = COMMAND_CLASS_ENERGY_PRODUCTION|Command Class = COMMAND_CLASS_ENERGY_PRODUCTION|Command Class = COMMAND_CLASS_ENERGY_PRODUCTION|Command Class = COMMAND_CLASS_ENERGY_PRODUCTION|Command Class = COMMAND_CLASS_ENERGY_PRODUCTION|Command Class = COMMAND_CLASS_ENERGY_PRODUCTION|
|Command = ENERGY_PRODUCTION_GET|Command = ENERGY_PRODUCTION_GET|Command = ENERGY_PRODUCTION_GET|Command = ENERGY_PRODUCTION_GET|Command = ENERGY_PRODUCTION_GET|Command = ENERGY_PRODUCTION_GET|Command = ENERGY_PRODUCTION_GET|Command = ENERGY_PRODUCTION_GET|
|Parameter Number|Parameter Number|Parameter Number|Parameter Number|Parameter Number|Parameter Number|Parameter Number|Parameter Number|



**Parameter** **Number** **(8** **bits)**

The parameter number specifies the kind of production data to retrieve. Currently the following
parameter numbers are defined:


Table 2.220: Energy Production Parameter Number

|Parameter Number|Description|
|---|---|
|0x00|Instant energy production|
|0x01|Total energy production|
|0x02|Energy production today|
|0x03|Total production time|



All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.


**2.2.41.2** **Energy** **Production** **Report** **Command**


This command is used to retrieve various production data from the device.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 205




<!-- PAGE 207 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Table 2.221: Energy Production Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_ENERGY_PRODUCTION|Command Class = COMMAND_CLASS_ENERGY_PRODUCTION|Command Class = COMMAND_CLASS_ENERGY_PRODUCTION|Command Class = COMMAND_CLASS_ENERGY_PRODUCTION|Command Class = COMMAND_CLASS_ENERGY_PRODUCTION|Command Class = COMMAND_CLASS_ENERGY_PRODUCTION|Command Class = COMMAND_CLASS_ENERGY_PRODUCTION|Command Class = COMMAND_CLASS_ENERGY_PRODUCTION|
|Command = ENERGY_PRODUCTION_REPORT|Command = ENERGY_PRODUCTION_REPORT|Command = ENERGY_PRODUCTION_REPORT|Command = ENERGY_PRODUCTION_REPORT|Command = ENERGY_PRODUCTION_REPORT|Command = ENERGY_PRODUCTION_REPORT|Command = ENERGY_PRODUCTION_REPORT|Command = ENERGY_PRODUCTION_REPORT|
|Parameter Number|Parameter Number|Parameter Number|Parameter Number|Parameter Number|Parameter Number|Parameter Number|Parameter Number|
|Precision|Precision|Precision|Scale|Scale|Size|Size|Size|
|Value 1|Value 1|Value 1|Value 1|Value 1|Value 1|Value 1|Value 1|
|…|…|…|…|…|…|…|…|
|Value N|Value N|Value N|Value N|Value N|Value N|Value N|Value N|



**Parameter** **Number** **(8** **bits)**


Refer to description under the Energy Production Get Command.


**Precision** **(3** **bits)**

The precision field describes what the precision of the value is. The number indicates the number of
decimals. The decimal value 1025 with precision 2 is therefore equal to 10.25.


**Scale** **(2** **bits)**

The Scale field indicates the scale used for the specified parameter number:


Table 2.222: Energy Production Scale

|Parameter Number|Scale|Description|
|---|---|---|
|0x00|0x00|W|
|0x01|0x00|Wh|
|0x02|0x00|Wh|
|0x03|0x00|Seconds|
|0x03|0x01|Hours|



**Size** **(3** **bits)**

The size field indicates the number of bytes used for the value. This field can take values from 1
(001b), 2 (010b) or 4 (100b).


**Value** **(N** **bytes)**

The value is MUST be treated as a signed field (Table 2.12). The field MAY be 1, 2 or 4 bytes in size.
The first byte is the most significant byte.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 206