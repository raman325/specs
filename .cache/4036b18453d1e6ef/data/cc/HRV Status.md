<!-- PAGE 230 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.45** **HRV** **Status** **Command** **Class,** **version** **1**


The residential Heat Recovery Ventilation (HRV) Status Command Class is used to read out a number
of parameters in the ventilation system.


**2.2.45.1** **HRV** **Status** **Get** **Command**


This command is used to request specific parameters from the ventilation system.


The HRV Status Report Command MUST be returned in response to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 2.246: HRV Status Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_HRV_STATUS|Command Class = COMMAND_CLASS_HRV_STATUS|Command Class = COMMAND_CLASS_HRV_STATUS|Command Class = COMMAND_CLASS_HRV_STATUS|Command Class = COMMAND_CLASS_HRV_STATUS|Command Class = COMMAND_CLASS_HRV_STATUS|Command Class = COMMAND_CLASS_HRV_STATUS|Command Class = COMMAND_CLASS_HRV_STATUS|
|Command = HRV_STATUS_GET|Command = HRV_STATUS_GET|Command = HRV_STATUS_GET|Command = HRV_STATUS_GET|Command = HRV_STATUS_GET|Command = HRV_STATUS_GET|Command = HRV_STATUS_GET|Command = HRV_STATUS_GET|
|Status Parameter|Status Parameter|Status Parameter|Status Parameter|Status Parameter|Status Parameter|Status Parameter|Status Parameter|



**Status** **Parameter** **(8** **bits)**


The status parameter used to indicate which status parameter that is requested.

|Value|Table 2.247: HRV Status Parameter Status Parameter|
|---|---|
|Value|Status Parameter|
|0x00|Outdoor Air temperature|
|0x01|Supply Air (to room) temperature|
|0x02|Exhaust Air (from room) temperature|
|0x03|Discharge Air temperature|
|0x04|Room temperature|
|0x05|Relative Humidity in room<br>|
|0x06|Remaining flter life|



**2.2.45.2** **HRV** **Status** **Report** **Command**


This command is used to report a specific status parameter in response to a HRV Status Get.


Table 2.248: HRV Status Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_HRV_STATUS|Command Class = COMMAND_CLASS_HRV_STATUS|Command Class = COMMAND_CLASS_HRV_STATUS|Command Class = COMMAND_CLASS_HRV_STATUS|Command Class = COMMAND_CLASS_HRV_STATUS|Command Class = COMMAND_CLASS_HRV_STATUS|Command Class = COMMAND_CLASS_HRV_STATUS|Command Class = COMMAND_CLASS_HRV_STATUS|
|Command = HRV_STATUS_REPORT|Command = HRV_STATUS_REPORT|Command = HRV_STATUS_REPORT|Command = HRV_STATUS_REPORT|Command = HRV_STATUS_REPORT|Command = HRV_STATUS_REPORT|Command = HRV_STATUS_REPORT|Command = HRV_STATUS_REPORT|
|Status Parameter|Status Parameter|Status Parameter|Status Parameter|Status Parameter|Status Parameter|Status Parameter|Status Parameter|
|Precision|Precision|Precision|Scale|Scale|Size|Size|Size|
|Value 1|Value 1|Value 1|Value 1|Value 1|Value 1|Value 1|Value 1|
|…|…|…|…|…|…|…|…|
|Value N|Value N|Value N|Value N|Value N|Value N|Value N|Value N|



**Status** **Parameter** **(8** **bits)**


The status parameter used to indicate which status parameter that is reported. Refer to Section
2.2.45.1 HRV Status Get for possible values.


**Precision** **(3** **bits)**


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 229




<!-- PAGE 231 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


The precision field describes what the precision of the setpoint value is. The number indicates the
number of decimals. The decimal value 1025 with precision 2 is therefore equal to 10.25.


**Scale** **(2** **bits)**

The scale field indicates the scale used the list of possible scales are given below:


Table 2.249: HRV Scale Parameter


**Size** **(3** **bits)**

|Status Parameter|Scale|Value|
|---|---|---|
|Outdoor Air temperature|Celsius (C)|0|
|Outdoor Air temperature|Fahrenheit (F)|1|
|Supply Air (to room) temperature|Celsius (C)|0|
|Supply Air (to room) temperature|Fahrenheit (F)|1|
|Exhaust Air (from room) temperature|Celsius (C)|0|
|Exhaust Air (from room) temperature|Fahrenheit (F)|1|
|Discharge Air temperature|Celsius (C)|0|
|Discharge Air temperature|Fahrenheit (F)|1|
|Room temperature|Celsius (C)|0|
|Room temperature|Fahrenheit (F)|1|
|Relative Humidity in room<br>|Percentage (%)|0|
|Remaining flter life|Percentage (%)|0|


The size field indicates the number of bytes used for the sensor value. This field can take values from
1 (001b), 2 (010b) or 4 (100b).


**Value** **(N** **bytes)**

The value MUST be treated as a signed field (Table 2.12). The value MAY be 1, 2 or 4 bytes in size.
This first byte is the most significant byte.


**2.2.45.3** **HRV** **Status** **Supported** **Get** **Command**


This command is used to request a bitmap of the supported status parameters.


The HRV Status Supported Report Command MUST be returned in response to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 2.250: HRV Status Supported Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_HRV_STATUS|Command Class = COMMAND_CLASS_HRV_STATUS|Command Class = COMMAND_CLASS_HRV_STATUS|Command Class = COMMAND_CLASS_HRV_STATUS|Command Class = COMMAND_CLASS_HRV_STATUS|Command Class = COMMAND_CLASS_HRV_STATUS|Command Class = COMMAND_CLASS_HRV_STATUS|Command Class = COMMAND_CLASS_HRV_STATUS|
|Command = HRV_STATUS_SUPPORTED_GET|Command = HRV_STATUS_SUPPORTED_GET|Command = HRV_STATUS_SUPPORTED_GET|Command = HRV_STATUS_SUPPORTED_GET|Command = HRV_STATUS_SUPPORTED_GET|Command = HRV_STATUS_SUPPORTED_GET|Command = HRV_STATUS_SUPPORTED_GET|Command = HRV_STATUS_SUPPORTED_GET|



**2.2.45.4** **HRV** **Status** **Supported** **Report** **Command**


This command is used to report a bitmap indicating the supported status parameters.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 230




<!-- PAGE 232 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Table 2.251: HRV Status Supported Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_HRV_STATUS|Command Class = COMMAND_CLASS_HRV_STATUS|Command Class = COMMAND_CLASS_HRV_STATUS|Command Class = COMMAND_CLASS_HRV_STATUS|Command Class = COMMAND_CLASS_HRV_STATUS|Command Class = COMMAND_CLASS_HRV_STATUS|Command Class = COMMAND_CLASS_HRV_STATUS|Command Class = COMMAND_CLASS_HRV_STATUS|
|Command = HRV_STATUS_SUPPORTED_REPORT|Command = HRV_STATUS_SUPPORTED_REPORT|Command = HRV_STATUS_SUPPORTED_REPORT|Command = HRV_STATUS_SUPPORTED_REPORT|Command = HRV_STATUS_SUPPORTED_REPORT|Command = HRV_STATUS_SUPPORTED_REPORT|Command = HRV_STATUS_SUPPORTED_REPORT|Command = HRV_STATUS_SUPPORTED_REPORT|
|Bit Mask 1|Bit Mask 1|Bit Mask 1|Bit Mask 1|Bit Mask 1|Bit Mask 1|Bit Mask 1|Bit Mask 1|
|…|…|…|…|…|…|…|…|
|Bit Mask N|Bit Mask N|Bit Mask N|Bit Mask N|Bit Mask N|Bit Mask N|Bit Mask N|Bit Mask N|



**Bit** **Mask** **(N** **bytes)**

The Bit Mask fields describe the supported status parameters from the ventilation system. Bit 0 in
the Bit Mask 1 field used to indicate if the status parameter “Outdoor Air Temperature” is supported,
0 indicating not supported and 1 indicating supported. Bit 1 in the Bit Mask 1 field used to indicate
if the status parameter “Supply Air Temperature” is supported and so forth. All available status
parameters are given in Section 2.2.45.1 HRV Status Get.

It is only necessary to send the Bit Mask fields 1 and up to the one indicating the last support status
parameter. The number of Bit Mask fields transmitted MUST be determined from the length field in
the frame.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 231