<!-- PAGE 238 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.47** **Humidity** **Control** **Mode** **Command** **Class,** **version** **1**


The Humidity Control Mode Command Class is used to control a humidity control device.


**2.2.47.1** **Humidity** **Control** **Mode** **Set** **Command**


This command is used to set the humidity control mode in the device.


Table 2.265: Humidity Control Mode Set Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_MODE|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_MODE|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_MODE|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_MODE|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_MODE|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_MODE|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_MODE|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_MODE|
|Command = HUMIDITY_CONTROL_MODE_SET|Command = HUMIDITY_CONTROL_MODE_SET|Command = HUMIDITY_CONTROL_MODE_SET|Command = HUMIDITY_CONTROL_MODE_SET|Command = HUMIDITY_CONTROL_MODE_SET|Command = HUMIDITY_CONTROL_MODE_SET|Command = HUMIDITY_CONTROL_MODE_SET|Command = HUMIDITY_CONTROL_MODE_SET|
|Reserved|Reserved|Reserved|Reserved|Mode|Mode|Mode|Mode|



**Reserved**

The reserved field is for future use. Reserved bits MUST be set to zero by a sending node. Reserved
bits MUST be ignored by a receiving node.


**Mode** **(4** **bits)**

The encoding of the humidity control mode field MUST be according to Table 2.266.






|Mode|Table 2.266: Humidity Control Mode Description|Version|
|---|---|---|
|Mode|Description<br>|Version|
|0|Of - Humidity control system is of.|1|
|1|Humidify - The system will attempt to raise humidity to<br>the humidifer setpoint.|1|
|2|De-humidify - The system will attempt to lower the hu-<br>midity to the de-humidifer setpoint.|1|
|3|Auto - The system will automatically switch between hu-<br>midifying and de-humidifying in order to satisfy the hu-<br>midify and de-humidify setpoints|2|



All other values are reserved. Reserved values MUST NOT be used by a sending node and MUST be
ignored by a receiving node.


**2.2.47.2** **Humidity** **Control** **Mode** **Get** **Command**


This command is used to request the supported humidity control modes from the device.


The Humidity Control Mode Report Command MUST be returned in response to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 2.267: Humidity Control Mode Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_MODE|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_MODE|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_MODE|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_MODE|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_MODE|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_MODE|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_MODE|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_MODE|
|Command = HUMIDITY_CONTROL_MODE_GET|Command = HUMIDITY_CONTROL_MODE_GET|Command = HUMIDITY_CONTROL_MODE_GET|Command = HUMIDITY_CONTROL_MODE_GET|Command = HUMIDITY_CONTROL_MODE_GET|Command = HUMIDITY_CONTROL_MODE_GET|Command = HUMIDITY_CONTROL_MODE_GET|Command = HUMIDITY_CONTROL_MODE_GET|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 237




<!-- PAGE 239 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.47.3** **Humidity** **Control** **Mode** **Report** **Command**


This command is used to report the humidity control mode from the device.


Table 2.268: Humidity Control Mode Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_MODE|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_MODE|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_MODE|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_MODE|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_MODE|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_MODE|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_MODE|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_MODE|
|Command = HUMIDITY_CONTROL_MODE_REPORT|Command = HUMIDITY_CONTROL_MODE_REPORT|Command = HUMIDITY_CONTROL_MODE_REPORT|Command = HUMIDITY_CONTROL_MODE_REPORT|Command = HUMIDITY_CONTROL_MODE_REPORT|Command = HUMIDITY_CONTROL_MODE_REPORT|Command = HUMIDITY_CONTROL_MODE_REPORT|Command = HUMIDITY_CONTROL_MODE_REPORT|
|Reserved|Reserved|Reserved|Reserved|Mode|Mode|Mode|Mode|



**Reserved**

The reserved field is for future use. Reserved bits MUST be set to zero by a sending node. Reserved
bits MUST be ignored by a receiving node.


**Mode** **(4** **bits)**

The encoding of the humidity control mode field MUST be according to Table 2.266.


**2.2.47.4** **Humidity** **Control** **Mode** **Supported** **Get** **Command**


This command is used to request the supported modes from the device.


The Humidity Control Mode Supported Report Command MUST be returned in response to this
command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 2.269: Humidity Control Mode Supported Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_MODE|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_MODE|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_MODE|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_MODE|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_MODE|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_MODE|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_MODE|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_MODE|
|Command = HUMIDITY_CONTROL_MODE_SUPPORTED_GET|Command = HUMIDITY_CONTROL_MODE_SUPPORTED_GET|Command = HUMIDITY_CONTROL_MODE_SUPPORTED_GET|Command = HUMIDITY_CONTROL_MODE_SUPPORTED_GET|Command = HUMIDITY_CONTROL_MODE_SUPPORTED_GET|Command = HUMIDITY_CONTROL_MODE_SUPPORTED_GET|Command = HUMIDITY_CONTROL_MODE_SUPPORTED_GET|Command = HUMIDITY_CONTROL_MODE_SUPPORTED_GET|



**2.2.47.5** **Humidity** **Control** **Mode** **Supported** **Report** **Command**


This command is used to report the supported humidity control modes from the device.


Table 2.270: Humidity Control Mode Supported Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_MODE|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_MODE|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_MODE|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_MODE|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_MODE|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_MODE|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_MODE|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_MODE|
|Command = HUMIDITY_CONTROL_MODE_SUPPORTED_REPORT|Command = HUMIDITY_CONTROL_MODE_SUPPORTED_REPORT|Command = HUMIDITY_CONTROL_MODE_SUPPORTED_REPORT|Command = HUMIDITY_CONTROL_MODE_SUPPORTED_REPORT|Command = HUMIDITY_CONTROL_MODE_SUPPORTED_REPORT|Command = HUMIDITY_CONTROL_MODE_SUPPORTED_REPORT|Command = HUMIDITY_CONTROL_MODE_SUPPORTED_REPORT|Command = HUMIDITY_CONTROL_MODE_SUPPORTED_REPORT|
|Bit Mask 1|Bit Mask 1|Bit Mask 1|Bit Mask 1|Bit Mask 1|Bit Mask 1|Bit Mask 1|Bit Mask 1|
|…|…|…|…|…|…|…|…|
|Bit Mask N|Bit Mask N|Bit Mask N|Bit Mask N|Bit Mask N|Bit Mask N|Bit Mask N|Bit Mask N|



Bit Mask (N bytes)

The Bit Mask fields MUST advertise the supported humidity control modes by the device. The
encoding of the Size field MUST be according to Table 2.271.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 238




<!-- PAGE 240 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Table 2.271: Supported Humidity Control Mode

|Field|Bit|Support for Control Mode|Version|
|---|---|---|---|
|Bit Mask 1|0|_Reserved_<br>|1|
|Bit Mask 1|1|1 (Humidifer)|1|
|Bit Mask 1|2|2 (De-humidifer)|1|
|Bit Mask 1|3|3 (Auto)|2|



All Bit Mask fields and bits not specified above are reserved. Reserved bits MUST be set to zero by
a sending node. Reserved bits MUST be ignored by a receiving node.


For each individual bit, The value ‘0’ MUST signify that the actual Mode is not supported.


The value ‘1’ MUST signify that the actual Mode is supported.

A sending node MAY omit trailing Bit Mask fields if they are not needed. The number of Bit Mask
fields MUST be determined from the length field in the frame.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 239




<!-- PAGE 241 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.48** **Humidity** **Control** **Operating** **State** **Class,** **version** **1**


The Humidity Control Operating State Command Class is used to obtain the operating state of the
humidity control device.


**2.2.48.1** **Humidity** **Control** **Operating** **State** **Get** **Command**


This command is used to request the operating state of the humidity control device.


The Humidity Control Operating State Report Command MUST be returned in response to thiscommand.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 2.272: Humidity Control Operating State Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_OPERATING_STATE|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_OPERATING_STATE|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_OPERATING_STATE|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_OPERATING_STATE|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_OPERATING_STATE|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_OPERATING_STATE|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_OPERATING_STATE|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_OPERATING_STATE|
|Command = HUMIDITY_CONTROL_OPERATING_STATE_GET|Command = HUMIDITY_CONTROL_OPERATING_STATE_GET|Command = HUMIDITY_CONTROL_OPERATING_STATE_GET|Command = HUMIDITY_CONTROL_OPERATING_STATE_GET|Command = HUMIDITY_CONTROL_OPERATING_STATE_GET|Command = HUMIDITY_CONTROL_OPERATING_STATE_GET|Command = HUMIDITY_CONTROL_OPERATING_STATE_GET|Command = HUMIDITY_CONTROL_OPERATING_STATE_GET|



**2.2.48.2** **Humidity** **Control** **Operating** **State** **Report** **Command**


This command is used to report the operating state of the humidity control device.


Table 2.273: Humidity Control Operating State Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_OPERATING_STATE|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_OPERATING_STATE|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_OPERATING_STATE|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_OPERATING_STATE|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_OPERATING_STATE|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_OPERATING_STATE|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_OPERATING_STATE|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_OPERATING_STATE|
|Command = HUMIDITY_CONTROL_OPERATING_STATE_REPORT|Command = HUMIDITY_CONTROL_OPERATING_STATE_REPORT|Command = HUMIDITY_CONTROL_OPERATING_STATE_REPORT|Command = HUMIDITY_CONTROL_OPERATING_STATE_REPORT|Command = HUMIDITY_CONTROL_OPERATING_STATE_REPORT|Command = HUMIDITY_CONTROL_OPERATING_STATE_REPORT|Command = HUMIDITY_CONTROL_OPERATING_STATE_REPORT|Command = HUMIDITY_CONTROL_OPERATING_STATE_REPORT|
|Reserved|Reserved|Reserved|Reserved|Operating State|Operating State|Operating State|Operating State|



**Reserved**

The reserved field is for future use. Reserved bits MUST be set to zero by a sending node. Reserved
bits MUST be ignored by a receiving node.


Operating State (4 bits)

The Operating State field MUST advertise the current operating state.

The encoding of the Operating State field MUST be according to Table 2.274.

|Operating State|Table 2.274: Operating State Description|Version|
|---|---|---|
|Operating State|Description|Version|
|0|Idle|1|
|1|Humidifying|1|
|2|De-humidifying|1|



All other values are reserved. Reserved values MUST NOT be used by a sending node and MUST be
ignored by a receiving node.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 240




<!-- PAGE 242 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.49** **Humidity** **Control** **Setpoint** **Command** **Class,** **version** **1-2**


The Humidity Control Setpoint Command Class is used for humidity control setpoint handling.


**2.2.49.1** **Humidity** **Control** **Setpoint** **Set** **Command**


This command is used to set the humidity control setpoint in the device.


Table 2.275: Humidity Control Setpoint Set Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_SETPOINT|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_SETPOINT|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_SETPOINT|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_SETPOINT|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_SETPOINT|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_SETPOINT|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_SETPOINT|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_SETPOINT|
|Command = HUMIDITY_CONTROL_SETPOINT_SET|Command = HUMIDITY_CONTROL_SETPOINT_SET|Command = HUMIDITY_CONTROL_SETPOINT_SET|Command = HUMIDITY_CONTROL_SETPOINT_SET|Command = HUMIDITY_CONTROL_SETPOINT_SET|Command = HUMIDITY_CONTROL_SETPOINT_SET|Command = HUMIDITY_CONTROL_SETPOINT_SET|Command = HUMIDITY_CONTROL_SETPOINT_SET|
|Reserved|Reserved|Reserved|Reserved|Setpoint Type|Setpoint Type|Setpoint Type|Setpoint Type|
|Precision|Precision|Precision|Scale|Scale|Size|Size|Size|
|Value 1|Value 1|Value 1|Value 1|Value 1|Value 1|Value 1|Value 1|
|…|…|…|…|…|…|…|…|
|Value N|Value N|Value N|Value N|Value N|Value N|Value N|Value N|



**Reserved**

The reserved field is for future use. Reserved bits MUST be set to zero by a sending node. Reserved
bits MUST be ignored by a receiving node.


**Setpoint** **Type** **(4** **bits)**

The Setpoint Type field MUST specify the humidity control setpoint to be set in the humidity control
device. The encoding of the Setpoint Type field MUST be according to Table 2.276.

|Setpoint Type|Table 2.276: Setpoint Type Description|Version|
|---|---|---|
|Setpoint Type|Description<br>|Version|
|1|Humidifer<br>|1|
|2|De-humidifer|1|
|3|Auto|2|



All other values are reserved. Reserved values MUST NOT be used by a sending node and MUST be
ignored by a receiving node.


**Precision** **(3** **bits)**

The precision field MUST specify the precision of the setpoint value. The number indicates the number
of decimals. As an example, the decimal value 1025 with precision two (2) is equal to 10.25.


**Scale** **(2** **bits)**

The Scale field MUST specify the humidity scale used. The encoding of the Scale field MUST be
according to Table 2.277.

|Scale|Table 2.277: Scale Values Description|Version|
|---|---|---|
|Scale|Description|Version|
|0|Percentage value|1|
|1|Absolute humidity (g/m3)|1|



All other values are reserved. Reserved values MUST NOT be used by a sending node and MUST be
ignored by a receiving node.


**Size** **(3** **bits)**

The Size field MUST specify the number of bytes used for the Value field. The encoding of the Size
field MUST be according to Table 2.278.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 241




<!-- PAGE 243 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024

|Size|Table 2.278: Size Values Description|Version|
|---|---|---|
|Size|Description<br>|Version|
|1|Value feld is 1 byte long<br>|1|
|2|Value feld is 2 bytes long<br>|1|
|4|Value feld is 4 bytes long|1|



All other values are reserved. Reserved values MUST NOT be used by a sending node and MUST be
ignored by a receiving node.


**Value** **(N** **bytes)**

The value is a signed field. The field MAY be one, two, or four bytes in size as specified by the Size
field. Value 1 is the most significant byte.


**2.2.49.2** **Humidity** **Control** **Setpoint** **Get** **Command**


This command is used to request the given humidity control setpoint type in a device.


The Humidity Control Setpoint Report MUST be returned in response to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 2.279: Humidity Control Setpoint Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_SETPOINT|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_SETPOINT|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_SETPOINT|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_SETPOINT|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_SETPOINT|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_SETPOINT|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_SETPOINT|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_SETPOINT|
|Command = HUMIDITY_CONTROL_SETPOINT_GET|Command = HUMIDITY_CONTROL_SETPOINT_GET|Command = HUMIDITY_CONTROL_SETPOINT_GET|Command = HUMIDITY_CONTROL_SETPOINT_GET|Command = HUMIDITY_CONTROL_SETPOINT_GET|Command = HUMIDITY_CONTROL_SETPOINT_GET|Command = HUMIDITY_CONTROL_SETPOINT_GET|Command = HUMIDITY_CONTROL_SETPOINT_GET|
|Reserved|Reserved|Reserved|Reserved|Setpoint Type|Setpoint Type|Setpoint Type|Setpoint Type|



**Reserved**

The reserved field is for future use. Reserved bits MUST be set to zero by a sending node. Reserved
bits MUST be ignored by a receiving node.


**Setpoint** **Type** **(4** **bits)**

This field MUST indicate which humidity control setpoint MUST be returned by the supporting node.
The encoding of the Setpoint Type field MUST be according to Table 2.276.


**2.2.49.3** **Humidity** **Control** **Setpoint** **Report** **Command**


This command is used to report the value of the humidity control setpoint type in the device.


Table 2.280: Humidity Control Setpoint Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_SETPOINT|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_SETPOINT|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_SETPOINT|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_SETPOINT|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_SETPOINT|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_SETPOINT|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_SETPOINT|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_SETPOINT|
|Command = HUMIDITY_CONTROL_SETPOINT_REPORT|Command = HUMIDITY_CONTROL_SETPOINT_REPORT|Command = HUMIDITY_CONTROL_SETPOINT_REPORT|Command = HUMIDITY_CONTROL_SETPOINT_REPORT|Command = HUMIDITY_CONTROL_SETPOINT_REPORT|Command = HUMIDITY_CONTROL_SETPOINT_REPORT|Command = HUMIDITY_CONTROL_SETPOINT_REPORT|Command = HUMIDITY_CONTROL_SETPOINT_REPORT|
|Reserved|Reserved|Reserved|Reserved|Setpoint Type|Setpoint Type|Setpoint Type|Setpoint Type|
|Precision|Precision|Precision|Scale|Scale|Size|Size|Size|
|Value 1|Value 1|Value 1|Value 1|Value 1|Value 1|Value 1|Value 1|
|…|…|…|…|…|…|…|…|
|Value N|Value N|Value N|Value N|Value N|Value N|Value N|Value N|



**Reserved**


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 242




<!-- PAGE 244 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


The reserved field is for future use. Reserved bits MUST be set to zero by a sending node. Reserved
bits MUST be ignored by a receiving node.

For fields’ description, refer to Section 2.2.49.1 Humidity Control Setpoint Set Command


**2.2.49.4** **Humidity** **Control** **Setpoint** **Supported** **Get** **Command**


This command is used to request the humidity control setpoint types supported by the device.


The Humidity Control Setpoint Supported Report Command MUST be returned in response to a this
command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 2.281: Humidity Control Setpoint Supported Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_SETPOINT|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_SETPOINT|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_SETPOINT|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_SETPOINT|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_SETPOINT|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_SETPOINT|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_SETPOINT|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_SETPOINT|
|Command = HUMIDITY_CONTROL_SETPOINT_SUPPORTED_GET|Command = HUMIDITY_CONTROL_SETPOINT_SUPPORTED_GET|Command = HUMIDITY_CONTROL_SETPOINT_SUPPORTED_GET|Command = HUMIDITY_CONTROL_SETPOINT_SUPPORTED_GET|Command = HUMIDITY_CONTROL_SETPOINT_SUPPORTED_GET|Command = HUMIDITY_CONTROL_SETPOINT_SUPPORTED_GET|Command = HUMIDITY_CONTROL_SETPOINT_SUPPORTED_GET|Command = HUMIDITY_CONTROL_SETPOINT_SUPPORTED_GET|



**2.2.49.5** **Humidity** **Control** **Setpoint** **Supported** **Report** **Command**


This command is used to report the humidity control setpoint types supported by the device.


Table 2.282: Humidity Control Setpoint Supported Report Com
|7|Table 2. mand 6|.282: Humidi 5|ity Control S 4|Setpoint Supp 3|ported Repor 2|rt Com- 1|0|
|---|---|---|---|---|---|---|---|
|**7**|**6**|**5**|**4**|**3**|**2**|**1**|**0**|
|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_SETPOINT|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_SETPOINT|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_SETPOINT|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_SETPOINT|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_SETPOINT|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_SETPOINT|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_SETPOINT|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_SETPOINT|
|Command = HUMIDITY_CONTROL_SETPOINT_SUPPORTED_REPORT|Command = HUMIDITY_CONTROL_SETPOINT_SUPPORTED_REPORT|Command = HUMIDITY_CONTROL_SETPOINT_SUPPORTED_REPORT|Command = HUMIDITY_CONTROL_SETPOINT_SUPPORTED_REPORT|Command = HUMIDITY_CONTROL_SETPOINT_SUPPORTED_REPORT|Command = HUMIDITY_CONTROL_SETPOINT_SUPPORTED_REPORT|Command = HUMIDITY_CONTROL_SETPOINT_SUPPORTED_REPORT|Command = HUMIDITY_CONTROL_SETPOINT_SUPPORTED_REPORT|
|Bit Mask 1|Bit Mask 1|Bit Mask 1|Bit Mask 1|Bit Mask 1|Bit Mask 1|Bit Mask 1|Bit Mask 1|
|…|…|…|…|…|…|…|…|
|Bit Mask N|Bit Mask N|Bit Mask N|Bit Mask N|Bit Mask N|Bit Mask N|Bit Mask N|Bit Mask N|



**Bit** **Mask** **(N** **bytes)**

The Bit Mask fields MUST advertise the humidity control setpoint types supported by the device.The
encoding of the Size field MUST be according to Table 2.283.

|Table 2.283: Field|Humidity Bit|Control Setpoint Supported Report values Support for Setpoint Type|Version|
|---|---|---|---|
|Field|Bit|Support for Setpoint Type|Version|
|Bit Mask 1|0|_Reserved_<br>|1|
|Bit Mask 1|1|1 (Humidifer)<br>|1|
|Bit Mask 1|2|2 (De-humidifer)|1|
|Bit Mask 1|3|3 (Auto)|2|



All Bit Mask fields and bits not specified above are reserved. Reserved bits MUST be set to zero by
a sending node. Reserved bits MUST be ignored by a receiving node.


For each individual bit, The value ‘0’ MUST signify that the actual Setpoint Type is not supported.


The value ‘1’ MUST signify that the actual Setpoint Type is supported.

A sending node MAY omit trailing Bit Mask fields if they are not needed. The number of Bit Mask
fields MUST be determined from the length field in the frame.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 243




<!-- PAGE 245 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.49.6** **Humidity** **Control** **Setpoint** **Scale** **Supported** **Get** **Command**


This command is used to retrieve the supported scales of the humidity control setpoints in the device.


The Humidity Control Scale Supported Report Command MUST be returned in response to this
command.


Table 2.284: Humidity Control Setpoint Scale Supported Get Com
|7|Table 2.2 mand 6|284: Humidit 5|ty Control Se 4|etpoint Scale S 3|Supported Ge 2|et Com- 1|0|
|---|---|---|---|---|---|---|---|
|**7**|**6**|**5**|**4**|**3**|**2**|**1**|**0**|
|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_SETPOINT|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_SETPOINT|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_SETPOINT|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_SETPOINT|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_SETPOINT|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_SETPOINT|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_SETPOINT|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_SETPOINT|
|Command = HUMIDITY_CONTROL_SETPOINT_SCALE_SUPPORTED_GET|Command = HUMIDITY_CONTROL_SETPOINT_SCALE_SUPPORTED_GET|Command = HUMIDITY_CONTROL_SETPOINT_SCALE_SUPPORTED_GET|Command = HUMIDITY_CONTROL_SETPOINT_SCALE_SUPPORTED_GET|Command = HUMIDITY_CONTROL_SETPOINT_SCALE_SUPPORTED_GET|Command = HUMIDITY_CONTROL_SETPOINT_SCALE_SUPPORTED_GET|Command = HUMIDITY_CONTROL_SETPOINT_SCALE_SUPPORTED_GET|Command = HUMIDITY_CONTROL_SETPOINT_SCALE_SUPPORTED_GET|
|Reserved|Reserved|Reserved|Reserved|Setpoint Type|Setpoint Type|Setpoint Type|Setpoint Type|



**Reserved**

The reserved field is for future use. Reserved bits MUST be set to zero by a sending node. Reserved
bits MUST be ignored by a receiving node.


**Setpoint** **Type** **(4** **bits)**


Refer to the description under the Section 2.2.49.1 Humidity Control Setpoint Set Command.


**2.2.49.7** **Humidity** **Control** **Setpoint** **Scale** **Supported** **Report** **Command**


This command indicates the supported scales of the humidity control setpoint in a bit mask format.


Table 2.285: Humidity Control Setpoint Scale Supported Report
Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_SETPOINT|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_SETPOINT|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_SETPOINT|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_SETPOINT|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_SETPOINT|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_SETPOINT|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_SETPOINT|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_SETPOINT|
|Command = HUMIDITY_CONTROL_SETPOINT_SCALE_SUPPORTED_REPORT|Command = HUMIDITY_CONTROL_SETPOINT_SCALE_SUPPORTED_REPORT|Command = HUMIDITY_CONTROL_SETPOINT_SCALE_SUPPORTED_REPORT|Command = HUMIDITY_CONTROL_SETPOINT_SCALE_SUPPORTED_REPORT|Command = HUMIDITY_CONTROL_SETPOINT_SCALE_SUPPORTED_REPORT|Command = HUMIDITY_CONTROL_SETPOINT_SCALE_SUPPORTED_REPORT|Command = HUMIDITY_CONTROL_SETPOINT_SCALE_SUPPORTED_REPORT|Command = HUMIDITY_CONTROL_SETPOINT_SCALE_SUPPORTED_REPORT|
|Reserved|Reserved|Reserved|Reserved|Scale Bit Mask|Scale Bit Mask|Scale Bit Mask|Scale Bit Mask|



**Reserved**

The reserved field is for future use. Reserved bits MUST be set to zero by a sending node. Reserved
bits MUST be ignored by a receiving node.


**Scale** **Bit** **Mask** **(4** **bits)**


Refer to the description under Section 2.2.49.1 Humidity Control Setpoint Set Command.


**2.2.49.8** **Humidity** **Control** **Setpoint** **Capabilities** **Get** **Command**


This command is used to request the minimum and maximum setpoint values for a given humidity
control Setpoint Type.


The Humidity Control Setpoint Capabilities Report Command MUST be returned in response to this
command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 244




<!-- PAGE 246 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Table 2.286: Humidity Control Setpoint Capabilities Get Com
|7|Table 2. mand 6|.286: Humid 5|dity Control 4|Setpoint Ca 3|apabilities Ge 2|et Com- 1|0|
|---|---|---|---|---|---|---|---|
|**7**|**6**|**5**|**4**|**3**|**2**|**1**|**0**|
|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_SETPOINT|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_SETPOINT|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_SETPOINT|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_SETPOINT|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_SETPOINT|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_SETPOINT|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_SETPOINT|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_SETPOINT|
|Command = HUMIDITY_CONTROL_SETPOINT_CAPABILITIES_GET|Command = HUMIDITY_CONTROL_SETPOINT_CAPABILITIES_GET|Command = HUMIDITY_CONTROL_SETPOINT_CAPABILITIES_GET|Command = HUMIDITY_CONTROL_SETPOINT_CAPABILITIES_GET|Command = HUMIDITY_CONTROL_SETPOINT_CAPABILITIES_GET|Command = HUMIDITY_CONTROL_SETPOINT_CAPABILITIES_GET|Command = HUMIDITY_CONTROL_SETPOINT_CAPABILITIES_GET|Command = HUMIDITY_CONTROL_SETPOINT_CAPABILITIES_GET|
|Reserved|Reserved|Reserved|Reserved|Setpoint Type|Setpoint Type|Setpoint Type|Setpoint Type|



**Reserved**

The reserved field is for future use. Reserved bits MUST be set to zero by a sending node. Reserved
bits MUST be ignored by a receiving node.


**Setpoint** **Type** **(4** **bits)**


Refer to the description under Section 2.2.49.1 Humidity Control Setpoint Set Command.


**2.2.49.9** **Humidity** **Control** **Setpoint** **Capabilities** **Report** **Command**


This command is used to report the minimum and maximum values of the requested humidity control
setpoint type.


Table 2.287: Humidity Control Setpoint Capabilities Report Com
|7|Table 2. mand 6|.287: Humidit 5|ty Control Se 4|etpoint Capa 3|abilities Repor 2|rt Com- 1|0|
|---|---|---|---|---|---|---|---|
|**7**|**6**|**5**|**4**|**3**|**2**|**1**|**0**|
|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_SETPOINT|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_SETPOINT|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_SETPOINT|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_SETPOINT|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_SETPOINT|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_SETPOINT|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_SETPOINT|Command Class = COMMAND_CLASS_HUMIDITY_CONTROL_SETPOINT|
|Command = HUMIDITY_CONTROL_SETPOINT_CAPABILITIES_REPORT|Command = HUMIDITY_CONTROL_SETPOINT_CAPABILITIES_REPORT|Command = HUMIDITY_CONTROL_SETPOINT_CAPABILITIES_REPORT|Command = HUMIDITY_CONTROL_SETPOINT_CAPABILITIES_REPORT|Command = HUMIDITY_CONTROL_SETPOINT_CAPABILITIES_REPORT|Command = HUMIDITY_CONTROL_SETPOINT_CAPABILITIES_REPORT|Command = HUMIDITY_CONTROL_SETPOINT_CAPABILITIES_REPORT|Command = HUMIDITY_CONTROL_SETPOINT_CAPABILITIES_REPORT|
|Reserved|Reserved|Reserved|Reserved|Setpoint Type|Setpoint Type|Setpoint Type|Setpoint Type|
|Precision|Precision|Precision|Scale|Scale|Size|Size|Size|
|Minimum Value 1|Minimum Value 1|Minimum Value 1|Minimum Value 1|Minimum Value 1|Minimum Value 1|Minimum Value 1|Minimum Value 1|
|…|…|…|…|…|…|…|…|
|Minimum Value N|Minimum Value N|Minimum Value N|Minimum Value N|Minimum Value N|Minimum Value N|Minimum Value N|Minimum Value N|
|Precision|Precision|Precision|Scale|Scale|Size|Size|Size|
|Maximum Value 1|Maximum Value 1|Maximum Value 1|Maximum Value 1|Maximum Value 1|Maximum Value 1|Maximum Value 1|Maximum Value 1|
|…|…|…|…|…|…|…|…|
|Maximum Value N|Maximum Value N|Maximum Value N|Maximum Value N|Maximum Value N|Maximum Value N|Maximum Value N|Maximum Value N|



Refer to the description under Section 2.2.49.1 Humidity Control Setpoint Set Command for other
parameter/field descriptions.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 245