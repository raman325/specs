<!-- PAGE 115 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.17** **Binary** **Sensor** **Command** **Class,** **version** **1** **[DEPRECATED]**


**Warning:** **THIS** **COMMAND** **CLASS** **HAS** **BEEN** **DEPRECATED**


A device MAY implement this command class, but it is RECOMMENDED that new implementations use the Notification Command Class.

If implementing this command class, it is RECOMMENDED that the Notification Command Class
is also implemented.


The Binary Sensor Command Class is used to realize binary sensors, such as movement sensors.


**2.2.17.1** **Binary** **Sensor** **Get** **Command**


This command is used to request the status of a sensor.


The Binary Sensor Report Command MUST be returned in response to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 2.89: Binary Sensor Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SENSOR_BINARY|Command Class = COMMAND_CLASS_SENSOR_BINARY|Command Class = COMMAND_CLASS_SENSOR_BINARY|Command Class = COMMAND_CLASS_SENSOR_BINARY|Command Class = COMMAND_CLASS_SENSOR_BINARY|Command Class = COMMAND_CLASS_SENSOR_BINARY|Command Class = COMMAND_CLASS_SENSOR_BINARY|Command Class = COMMAND_CLASS_SENSOR_BINARY|
|Command = SENSOR_BINARY_GET|Command = SENSOR_BINARY_GET|Command = SENSOR_BINARY_GET|Command = SENSOR_BINARY_GET|Command = SENSOR_BINARY_GET|Command = SENSOR_BINARY_GET|Command = SENSOR_BINARY_GET|Command = SENSOR_BINARY_GET|



**2.2.17.2** **Binary** **Sensor** **Report** **Command**


This command is used to advertise a sensor value.


Table 2.90: Binary Sensor Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SENSOR_BINARY|Command Class = COMMAND_CLASS_SENSOR_BINARY|Command Class = COMMAND_CLASS_SENSOR_BINARY|Command Class = COMMAND_CLASS_SENSOR_BINARY|Command Class = COMMAND_CLASS_SENSOR_BINARY|Command Class = COMMAND_CLASS_SENSOR_BINARY|Command Class = COMMAND_CLASS_SENSOR_BINARY|Command Class = COMMAND_CLASS_SENSOR_BINARY|
|Command = SENSOR_BINARY_REPORT|Command = SENSOR_BINARY_REPORT|Command = SENSOR_BINARY_REPORT|Command = SENSOR_BINARY_REPORT|Command = SENSOR_BINARY_REPORT|Command = SENSOR_BINARY_REPORT|Command = SENSOR_BINARY_REPORT|Command = SENSOR_BINARY_REPORT|
|Sensor Value|Sensor Value|Sensor Value|Sensor Value|Sensor Value|Sensor Value|Sensor Value|Sensor Value|



**Sensor** **Value** **(8** **bits)**


If the Sensor Value is 0x00 indicates that the sensor is idle and 0xFF indicates that the sensor has

detected an event.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 114

---

<!-- PAGE 116 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.18** **Binary** **Sensor** **Command** **Class,** **version** **2** **[DEPRECATED]**


**Warning:** **THIS** **COMMAND** **CLASS** **HAS** **BEEN** **DEPRECATED**


A device MAY implement this command class, but it is RECOMMENDED that new implementations use the _Notification_ _Command_ _Class,_ _version_ _3-8_ .

If implementing this command class, it is RECOMMENDED that the _Notification Command Class,_
_version_ _3-8_ is also implemented.


The Binary Sensor Command Class is used to realize binary sensors, such as movement sensors and
door/window sensors. Version 2 of this command class is extended with the following functionalities:


 - A “get-supported” mechanism for the controlling device to interview the binary sensor for its
supported sensor types

 - A list of defined sensor types capable of reporting a binary value

**NOTE** : A binary sensor is defined as a sensor unit capable of providing a binary value in the report
i.e. that an event was “triggered” or “not triggered” and not other intermediate values. For sensor
units providing multiple values the Multilevel Sensor Command Class is more suitable. The Binary
Sensor Command Class can further advance through implementation of the Notification Command
Class to communicate details about the event.


**2.2.18.1** **Binary** **Sensor** **Get** **Command**


This command is used to request the status of the specific sensor device.


The Binary Sensor Report Command MUST be returned in response to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 2.91: Binary Sensor Get Command, version 2

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SENSOR_BINARY|Command Class = COMMAND_CLASS_SENSOR_BINARY|Command Class = COMMAND_CLASS_SENSOR_BINARY|Command Class = COMMAND_CLASS_SENSOR_BINARY|Command Class = COMMAND_CLASS_SENSOR_BINARY|Command Class = COMMAND_CLASS_SENSOR_BINARY|Command Class = COMMAND_CLASS_SENSOR_BINARY|Command Class = COMMAND_CLASS_SENSOR_BINARY|
|Command = SENSOR_BINARY_GET|Command = SENSOR_BINARY_GET|Command = SENSOR_BINARY_GET|Command = SENSOR_BINARY_GET|Command = SENSOR_BINARY_GET|Command = SENSOR_BINARY_GET|Command = SENSOR_BINARY_GET|Command = SENSOR_BINARY_GET|
|Sensor Type|Sensor Type|Sensor Type|Sensor Type|Sensor Type|Sensor Type|Sensor Type|Sensor Type|



**Sensor** **Type** **(8** **bits)**

Sensor Type specifies what type of sensor this command originates from. Refer to Table 2.92. The
sensor type value 0xFF returns the first found supported sensor type in the bit mask (starting from
bit 0 in Bit Mask 1) by the Binary Sensor Supported Report.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 115




<!-- PAGE 117 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Table 2.92: Binary Sensor Get::Sensor Type encoding

|Value|Sensor Type|
|---|---|
|0x00|Reserved|
|0x01|General purpose|
|0x02|Smoke|
|0x03|CO|
|0x04|CO2|
|0x05|Heat|
|0x06|Water|
|0x07|Freeze|
|0x08|Tamper|
|0x09|Aux|
|0x0A|Door/Window|
|0x0B|Tilt|
|0x0C|Motion|
|0x0D|Glass Break|
|0x0E..0xFE|Reserved|
|0xFF|Return 1st Sensor Type on supported list|



**2.2.18.2** **Binary** **Sensor** **Report** **Command**


This command is used to advertise a sensor value.


Table 2.93: Binary Sensor Report Command, version 2

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SENSOR_BINARY|Command Class = COMMAND_CLASS_SENSOR_BINARY|Command Class = COMMAND_CLASS_SENSOR_BINARY|Command Class = COMMAND_CLASS_SENSOR_BINARY|Command Class = COMMAND_CLASS_SENSOR_BINARY|Command Class = COMMAND_CLASS_SENSOR_BINARY|Command Class = COMMAND_CLASS_SENSOR_BINARY|Command Class = COMMAND_CLASS_SENSOR_BINARY|
|Command = SENSOR_BINARY_REPORT|Command = SENSOR_BINARY_REPORT|Command = SENSOR_BINARY_REPORT|Command = SENSOR_BINARY_REPORT|Command = SENSOR_BINARY_REPORT|Command = SENSOR_BINARY_REPORT|Command = SENSOR_BINARY_REPORT|Command = SENSOR_BINARY_REPORT|
|Sensor Value|Sensor Value|Sensor Value|Sensor Value|Sensor Value|Sensor Value|Sensor Value|Sensor Value|
|Sensor Type|Sensor Type|Sensor Type|Sensor Type|Sensor Type|Sensor Type|Sensor Type|Sensor Type|



**Sensor** **Value** **(8** **bits)**


Sensor Value = 0x00 indicates that the sensor is idle and 0xFF indicates that the sensor has detected

an event.


**2.2.18.3** **Binary** **Sensor** **Get** **Supported** **Sensor** **Command**


This command is used to request the supported sensor types from the binary sensor device.


Table 2.94: Binary Sensor Get Supported Sensor Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SENSOR_BINARY|Command Class = COMMAND_CLASS_SENSOR_BINARY|Command Class = COMMAND_CLASS_SENSOR_BINARY|Command Class = COMMAND_CLASS_SENSOR_BINARY|Command Class = COMMAND_CLASS_SENSOR_BINARY|Command Class = COMMAND_CLASS_SENSOR_BINARY|Command Class = COMMAND_CLASS_SENSOR_BINARY|Command Class = COMMAND_CLASS_SENSOR_BINARY|
|Command = SENSOR_BINARY_SUPPORTED_GET_SENSOR|Command = SENSOR_BINARY_SUPPORTED_GET_SENSOR|Command = SENSOR_BINARY_SUPPORTED_GET_SENSOR|Command = SENSOR_BINARY_SUPPORTED_GET_SENSOR|Command = SENSOR_BINARY_SUPPORTED_GET_SENSOR|Command = SENSOR_BINARY_SUPPORTED_GET_SENSOR|Command = SENSOR_BINARY_SUPPORTED_GET_SENSOR|Command = SENSOR_BINARY_SUPPORTED_GET_SENSOR|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 116




<!-- PAGE 118 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.18.4** **Binary** **Sensor** **Supported** **Sensor** **Report** **Command**


This command must be sent as requested by a received _Binary Sensor Get Supported Sensor Command_ .
This command indicates the supported sensor types of the binary sensor device in a bit mask format
and MUST NOT be transmitted unsolicited.


Table 2.95: Binary Sensor Supported Sensor Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SENSOR_BINARY|Command Class = COMMAND_CLASS_SENSOR_BINARY|Command Class = COMMAND_CLASS_SENSOR_BINARY|Command Class = COMMAND_CLASS_SENSOR_BINARY|Command Class = COMMAND_CLASS_SENSOR_BINARY|Command Class = COMMAND_CLASS_SENSOR_BINARY|Command Class = COMMAND_CLASS_SENSOR_BINARY|Command Class = COMMAND_CLASS_SENSOR_BINARY|
|Command = SENSOR_BINARY_SUPPORTED_SENSOR_REPORT|Command = SENSOR_BINARY_SUPPORTED_SENSOR_REPORT|Command = SENSOR_BINARY_SUPPORTED_SENSOR_REPORT|Command = SENSOR_BINARY_SUPPORTED_SENSOR_REPORT|Command = SENSOR_BINARY_SUPPORTED_SENSOR_REPORT|Command = SENSOR_BINARY_SUPPORTED_SENSOR_REPORT|Command = SENSOR_BINARY_SUPPORTED_SENSOR_REPORT|Command = SENSOR_BINARY_SUPPORTED_SENSOR_REPORT|
|Bit Mask 1|Bit Mask 1|Bit Mask 1|Bit Mask 1|Bit Mask 1|Bit Mask 1|Bit Mask 1|Bit Mask 1|
|…|…|…|…|…|…|…|…|
|Bit Mask N|Bit Mask N|Bit Mask N|Bit Mask N|Bit Mask N|Bit Mask N|Bit Mask N|Bit Mask N|



**Bit** **Mask** **(N** **bytes)**

The Bit Mask fields describe the supported sensor types by the binary sensor device and refer to the
Sensor Type table of Binary Sensor Report command.


 - Bit 0 in Bit Mask 1 is not allocated to any Sensor Type and must therefore be set to zero.


 - Bit 1 in Bit Mask 1 indicates if Sensor Type = 1 (General Purpose) is supported.


 - Bit 2 in Bit Mask 1 indicates if Sensor Type = 2 (Smoke) is supported.


 - Bit 3 in Bit Mask 1 indicates if Sensor Type = 3 (CO) is supported


 - …


If the Sensor Type is supported the bit MUST be set to 1. If the Sensor Type is not supported the
bit MUST be set to 0. Sensor Type = 0xFF (Return 1st Sensor Type on supported list) cannot be
indicated by the Bit Masks.


**Note** : It is only necessary to transmit Bit Mask 1 and up to the Bit Mask N indicating the last
supported sensor type. The number of Bit Mask fields transmitted MUST be determined from the
length field in the frame.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 117