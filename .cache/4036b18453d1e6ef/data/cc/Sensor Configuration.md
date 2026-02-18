<!-- PAGE 461 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.98** **Sensor** **Configuration** **Command** **Class,** **version** **1** **[OBSOLETED]**


**Warning:** **THIS** **COMMAND** **HAS** **BEEN** **OBSOLETED**

New implementations MUST NOT use the Sensor Configuration Command Class. Refer to the
Configuration Command Classes.


The Sensor Configuration Command Class adds the possibility for sensors to act on either a measured
value or on a preconfigured value. With this command class an application can act on a specific event.
It is up to the application to implement the actual event. This could e.g. be implementation of the
Association Command Class where the application would activate a group based on a trigger from
the sensor.

The trigger types that may be configured are the same types as the values specified in the Multilevel
Sensor Command Class

Most movement sensors may be configured to “ignore” movement if it is not dark. Typically this is
done manually. With the Sensor Configuration Command Class this may be configured remotely in a
standardised way.

A device supporting the Sensor Configuration Command Class may be configured via the trigger level,
but the decision on what the level change should trigger is up to the application. For the movement
sensor this trigger level could be an input parameter to the logic that controls the light.


**2.2.98.1** **Sensor** **Trigger** **Level** **Set** **Command**


This command is used to set different triggers to either a specified value or to the current measured
value. The Command also supports to restore a factory default value.

All configurable trigger types and values MUST be mapped directly from the Multilevel Sensor Command Class.


It is RECOMMENDED that all combinations of precision, scale and size parameters are supported.
The Set command MUST support same format of precision, scale and size parameters as can be
returned in the report command.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SENSOR_CONFIGURATION|Command Class = COMMAND_CLASS_SENSOR_CONFIGURATION|Command Class = COMMAND_CLASS_SENSOR_CONFIGURATION|Command Class = COMMAND_CLASS_SENSOR_CONFIGURATION|Command Class = COMMAND_CLASS_SENSOR_CONFIGURATION|Command Class = COMMAND_CLASS_SENSOR_CONFIGURATION|Command Class = COMMAND_CLASS_SENSOR_CONFIGURATION|Command Class = COMMAND_CLASS_SENSOR_CONFIGURATION|
|Command = SENSOR_TRIGGER_LEVEL_SET|Command = SENSOR_TRIGGER_LEVEL_SET|Command = SENSOR_TRIGGER_LEVEL_SET|Command = SENSOR_TRIGGER_LEVEL_SET|Command = SENSOR_TRIGGER_LEVEL_SET|Command = SENSOR_TRIGGER_LEVEL_SET|Command = SENSOR_TRIGGER_LEVEL_SET|Command = SENSOR_TRIGGER_LEVEL_SET|
|Default|Current|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|
|Sensor Type|Sensor Type|Sensor Type|Sensor Type|Sensor Type|Sensor Type|Sensor Type|Sensor Type|
|Precision|Precision|Precision|Scale|Scale|Size|Size|Size|
|Trigger Value 1|Trigger Value 1|Trigger Value 1|Trigger Value 1|Trigger Value 1|Trigger Value 1|Trigger Value 1|Trigger Value 1|
|…|…|…|…|…|…|…|…|
|Trigger Value N|Trigger Value N|Trigger Value N|Trigger Value N|Trigger Value N|Trigger Value N|Trigger Value N|Trigger Value N|



**Default** **(1** **bit)**


Reset level of trigger type to factory default when this bit is set to 1. If any value is set in this frame
when the Default bit is 1 this value will be ignored.


**Current** **(1** **bit)**


The current measured value will be stored as trigger value when this bit is set to 1. The trigger value
in this frame will be ignored when the Current bit is set to 1.


**Reserved**

This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**Precision** **(3** **bits)**


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 460




<!-- PAGE 462 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


The precision field describes what the precision of the trigger value is. The number indicates the
number of decimals. The decimal value 1025 with precision 2 is therefore equal to 10.25.


**Scale** **(2** **bits)**


The Scale used to indicate what unit the trigger uses. Refer to the table in the Multilevel Sensor
Command Class with respect to defined scales for the relevant triggers. Scales are defined by the
Z-Wave Alliance.


**Size** **(3** **bits)**

The size field indicates the number of bytes used for the Trigger Value field. This field can take values
from 1 (001b), 2 (010b) or 4 (100b).


**Sensor** **Type** **(8** **bits)**

The Sensor Type specifies what type of trigger this Command will set. Refer to the Multilevel Sensor
Command Class specification, where Sensor Type is defined in the Multilevel Sensor Report Command.


**Trigger** **Value** **(N** **bytes)**


Refer to the Multilevel Sensor Report Command for information on what trigger values to set.


**2.2.98.2** **Sensor** **Trigger** **Level** **Get** **Command**


This command can request the stored trigger level.


The Sensor Trigger Level Report Command MUST be returned in response to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SENSOR_CONFIGURATION|Command Class = COMMAND_CLASS_SENSOR_CONFIGURATION|Command Class = COMMAND_CLASS_SENSOR_CONFIGURATION|Command Class = COMMAND_CLASS_SENSOR_CONFIGURATION|Command Class = COMMAND_CLASS_SENSOR_CONFIGURATION|Command Class = COMMAND_CLASS_SENSOR_CONFIGURATION|Command Class = COMMAND_CLASS_SENSOR_CONFIGURATION|Command Class = COMMAND_CLASS_SENSOR_CONFIGURATION|
|Command = SENSOR_TRIGGER_LEVEL_GET|Command = SENSOR_TRIGGER_LEVEL_GET|Command = SENSOR_TRIGGER_LEVEL_GET|Command = SENSOR_TRIGGER_LEVEL_GET|Command = SENSOR_TRIGGER_LEVEL_GET|Command = SENSOR_TRIGGER_LEVEL_GET|Command = SENSOR_TRIGGER_LEVEL_GET|Command = SENSOR_TRIGGER_LEVEL_GET|



**2.2.98.3** **Sensor** **Trigger** **Level** **Report** **Command**


This command returns the stored trigger value.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SENSOR_CONFIGURATION|Command Class = COMMAND_CLASS_SENSOR_CONFIGURATION|Command Class = COMMAND_CLASS_SENSOR_CONFIGURATION|Command Class = COMMAND_CLASS_SENSOR_CONFIGURATION|Command Class = COMMAND_CLASS_SENSOR_CONFIGURATION|Command Class = COMMAND_CLASS_SENSOR_CONFIGURATION|Command Class = COMMAND_CLASS_SENSOR_CONFIGURATION|Command Class = COMMAND_CLASS_SENSOR_CONFIGURATION|
|Command = SENSOR_TRIGGER_LEVEL_REPORT|Command = SENSOR_TRIGGER_LEVEL_REPORT|Command = SENSOR_TRIGGER_LEVEL_REPORT|Command = SENSOR_TRIGGER_LEVEL_REPORT|Command = SENSOR_TRIGGER_LEVEL_REPORT|Command = SENSOR_TRIGGER_LEVEL_REPORT|Command = SENSOR_TRIGGER_LEVEL_REPORT|Command = SENSOR_TRIGGER_LEVEL_REPORT|
|Precision|Precision|Precision|Scale|Scale|Size|Size|Size|
|Trigger Value 1|Trigger Value 1|Trigger Value 1|Trigger Value 1|Trigger Value 1|Trigger Value 1|Trigger Value 1|Trigger Value 1|
|…|…|…|…|…|…|…|…|
|Trigger Value N|Trigger Value N|Trigger Value N|Trigger Value N|Trigger Value N|Trigger Value N|Trigger Value N|Trigger Value N|



For fields’ description, refer to the Sensor Trigger Level Set Command.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 461




<!-- PAGE 463 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.98.4** **Mapping** **Example**


The report structure of the Multilevel Sensor Command Class can be mapped direct into the Sensor
Configuration Set Command Class. This example frame below will set the trigger level in the receiving
node to 10.25 degree Celsius.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SENSOR_CONFIGURATION|Command Class = COMMAND_CLASS_SENSOR_CONFIGURATION|Command Class = COMMAND_CLASS_SENSOR_CONFIGURATION|Command Class = COMMAND_CLASS_SENSOR_CONFIGURATION|Command Class = COMMAND_CLASS_SENSOR_CONFIGURATION|Command Class = COMMAND_CLASS_SENSOR_CONFIGURATION|Command Class = COMMAND_CLASS_SENSOR_CONFIGURATION|Command Class = COMMAND_CLASS_SENSOR_CONFIGURATION|
|Command = SENSOR_TRIGGER_LEVEL_SET|Command = SENSOR_TRIGGER_LEVEL_SET|Command = SENSOR_TRIGGER_LEVEL_SET|Command = SENSOR_TRIGGER_LEVEL_SET|Command = SENSOR_TRIGGER_LEVEL_SET|Command = SENSOR_TRIGGER_LEVEL_SET|Command = SENSOR_TRIGGER_LEVEL_SET|Command = SENSOR_TRIGGER_LEVEL_SET|
|Default (0)|Current (0)|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|
|Precision (010b)|Precision (010b)|Precision (010b)|Celsius (00b)|Celsius (00b)|Size (010b)|Size (010b)|Size (010b)|
|0x04|0x04|0x04|0x04|0x04|0x04|0x04|0x04|
|0x01|0x01|0x01|0x01|0x01|0x01|0x01|0x01|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 462




<!-- PAGE 464 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.99** **Simple** **AV** **Control** **Command** **Class,** **version** **1-4**


The Simple AV Control Command Class is used to control an AV device in a Z-Wave network. The
Simple AV Control Command Class is suited for IR remote replacement. Furthermore, this command
class supports Windows Vista Media Center and Media Center 2005 remote controls.


**2.2.99.1** **Simple** **AV** **Control** **Set** **Command**


This command is used to control an AV device.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SIMPLE_AV_CONTROL|Command Class = COMMAND_CLASS_SIMPLE_AV_CONTROL|Command Class = COMMAND_CLASS_SIMPLE_AV_CONTROL|Command Class = COMMAND_CLASS_SIMPLE_AV_CONTROL|Command Class = COMMAND_CLASS_SIMPLE_AV_CONTROL|Command Class = COMMAND_CLASS_SIMPLE_AV_CONTROL|Command Class = COMMAND_CLASS_SIMPLE_AV_CONTROL|Command Class = COMMAND_CLASS_SIMPLE_AV_CONTROL|
|Command = SIMPLE_AV_CONTROL_SET|Command = SIMPLE_AV_CONTROL_SET|Command = SIMPLE_AV_CONTROL_SET|Command = SIMPLE_AV_CONTROL_SET|Command = SIMPLE_AV_CONTROL_SET|Command = SIMPLE_AV_CONTROL_SET|Command = SIMPLE_AV_CONTROL_SET|Command = SIMPLE_AV_CONTROL_SET|
|Sequence Number|Sequence Number|Sequence Number|Sequence Number|Sequence Number|Sequence Number|Sequence Number|Sequence Number|
|Reserved|Reserved|Reserved|Reserved|Reserved|Key Attributes|Key Attributes|Key Attributes|
|Reserved [OBSOLETED]|Reserved [OBSOLETED]|Reserved [OBSOLETED]|Reserved [OBSOLETED]|Reserved [OBSOLETED]|Reserved [OBSOLETED]|Reserved [OBSOLETED]|Reserved [OBSOLETED]|
|Reserved [OBSOLETED]|Reserved [OBSOLETED]|Reserved [OBSOLETED]|Reserved [OBSOLETED]|Reserved [OBSOLETED]|Reserved [OBSOLETED]|Reserved [OBSOLETED]|Reserved [OBSOLETED]|
|Command MSB,1|Command MSB,1|Command MSB,1|Command MSB,1|Command MSB,1|Command MSB,1|Command MSB,1|Command MSB,1|
|Command LSB,1|Command LSB,1|Command LSB,1|Command LSB,1|Command LSB,1|Command LSB,1|Command LSB,1|Command LSB,1|
|…|…|…|…|…|…|…|…|
|Command MSB,N|Command MSB,N|Command MSB,N|Command MSB,N|Command MSB,N|Command MSB,N|Command MSB,N|Command MSB,N|
|Command LSB,N|Command LSB,N|Command LSB,N|Command LSB,N|Command LSB,N|Command LSB,N|Command LSB,N|Command LSB,N|



**Sequence** **Number** **(8** **bits)**


The sequence number is incremented each time a Simple AV Control Set Command is issued. The
receiving node uses the sequence number to ignore duplicates.


**Key** **Attributes** **(3** **bits)**

The key attributes specifies the state of the key. Currently the following key attribute definitions
exist:


Table 2.515: Simple AV Control Set::Key Attributes encoding

|Key Attribute|Description|
|---|---|
|0x00|Key Down - Sent when a new key is pressed. It is mandatory to send a Simple<br>AV Control Set Command when this event occurs.|
|0x01|Key Up - Sent when the key is released. It is optional to send a Simple AV<br>Control Set Command when this event occurs. Only the sequence number and<br>key attribute parameter is changed in the Command.|
|0x02|Keep Alive - Sent every 100-200ms while the key is still held down. Event<br>used as a failsafe feature for the ramping function, e.g. avoid volume jumps<br>to maximum in case a key up event is not received. The keep alive event can<br>also be used to control the speed of the ramping function, e.g. the frst few<br>seconds of the key held down is the speed slow and afterwards will it gradually<br>accelerate.<br>It is optional to send a Simple AV Control Set Command when this event<br>occurs. Only the sequence number and key attribute parameter is changed in<br>the Command.|



All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.


Un-supported key attribute values MUST be ignored.


**Reserved**

This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**Command** **MSB,** **Command** **LSB** **(N** ***** **16** **bits)**


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 463




<!-- PAGE 465 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


This field is used to carry the AV Control command.

Each 16 bits-unit MUST carry a defined AV Control code. Refer to [31] for the defined AV Control
codes. Values not defined in [31] are reserved and MUST NOT be used.


It is possible to specify a sequence of AV commands in one frame. If an AV control command is not
supported, it MUST be ignored by a receiving node.


Command numbers 1 through 40 are the most popular commands used in AV remotes.


Command numbers 41 through 363 are less popular and is sorted in alphanumerical order.


Support for Windows Vista Media Center and Media Center 2005 remote controls is added with
command numbers from 364 to 377 including 16, 200 and 231.


**2.2.99.2** **Simple** **AV** **Control** **Get** **Command**


This command is used to request the number of reports necessary to report the supported AC Commands from the device.


The Simple AV Control Report Command MUST be returned in response to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SIMPLE_AV_CONTROL|Command Class = COMMAND_CLASS_SIMPLE_AV_CONTROL|Command Class = COMMAND_CLASS_SIMPLE_AV_CONTROL|Command Class = COMMAND_CLASS_SIMPLE_AV_CONTROL|Command Class = COMMAND_CLASS_SIMPLE_AV_CONTROL|Command Class = COMMAND_CLASS_SIMPLE_AV_CONTROL|Command Class = COMMAND_CLASS_SIMPLE_AV_CONTROL|Command Class = COMMAND_CLASS_SIMPLE_AV_CONTROL|
|Command = SIMPLE_AV_CONTROL_GET|Command = SIMPLE_AV_CONTROL_GET|Command = SIMPLE_AV_CONTROL_GET|Command = SIMPLE_AV_CONTROL_GET|Command = SIMPLE_AV_CONTROL_GET|Command = SIMPLE_AV_CONTROL_GET|Command = SIMPLE_AV_CONTROL_GET|Command = SIMPLE_AV_CONTROL_GET|



**2.2.99.3** **Simple** **AV** **Control** **Report** **Command**


This command is used to report the necessary number of reports to report the supported AC Commands from the device.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SIMPLE_AV_CONTROL|Command Class = COMMAND_CLASS_SIMPLE_AV_CONTROL|Command Class = COMMAND_CLASS_SIMPLE_AV_CONTROL|Command Class = COMMAND_CLASS_SIMPLE_AV_CONTROL|Command Class = COMMAND_CLASS_SIMPLE_AV_CONTROL|Command Class = COMMAND_CLASS_SIMPLE_AV_CONTROL|Command Class = COMMAND_CLASS_SIMPLE_AV_CONTROL|Command Class = COMMAND_CLASS_SIMPLE_AV_CONTROL|
|Command = SIMPLE_AV_CONTROL_REPORT|Command = SIMPLE_AV_CONTROL_REPORT|Command = SIMPLE_AV_CONTROL_REPORT|Command = SIMPLE_AV_CONTROL_REPORT|Command = SIMPLE_AV_CONTROL_REPORT|Command = SIMPLE_AV_CONTROL_REPORT|Command = SIMPLE_AV_CONTROL_REPORT|Command = SIMPLE_AV_CONTROL_REPORT|
|Number of reports|Number of reports|Number of reports|Number of reports|Number of reports|Number of reports|Number of reports|Number of reports|



**Number** **of** **reports** **(8** **bits)**


The number of reports necessary to report the entire list of supported AC Commands.


**2.2.99.4** **Simple** **AV** **Control** **Supported** **Get** **Command**


This command is used to request the AV Commands supported by the AV device.


The Simple AV Control Supported Report Command MUST be returned in response to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 464




<!-- PAGE 466 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SIMPLE_AV_CONTROL|Command Class = COMMAND_CLASS_SIMPLE_AV_CONTROL|Command Class = COMMAND_CLASS_SIMPLE_AV_CONTROL|Command Class = COMMAND_CLASS_SIMPLE_AV_CONTROL|Command Class = COMMAND_CLASS_SIMPLE_AV_CONTROL|Command Class = COMMAND_CLASS_SIMPLE_AV_CONTROL|Command Class = COMMAND_CLASS_SIMPLE_AV_CONTROL|Command Class = COMMAND_CLASS_SIMPLE_AV_CONTROL|
|Command = SIMPLE_AV_CONTROL_SUPPORTED_GET|Command = SIMPLE_AV_CONTROL_SUPPORTED_GET|Command = SIMPLE_AV_CONTROL_SUPPORTED_GET|Command = SIMPLE_AV_CONTROL_SUPPORTED_GET|Command = SIMPLE_AV_CONTROL_SUPPORTED_GET|Command = SIMPLE_AV_CONTROL_SUPPORTED_GET|Command = SIMPLE_AV_CONTROL_SUPPORTED_GET|Command = SIMPLE_AV_CONTROL_SUPPORTED_GET|
|Report No|Report No|Report No|Report No|Report No|Report No|Report No|Report No|



**Report** **No** **(8** **bits)**

Report no. field is used to request wanted report number. The report no. values MUST be a sequence
starting from 1.


**2.2.99.5** **Simple** **AV** **Control** **Supported** **Report** **Command**


This command is used to report the supported AC Commands from the device.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SIMPLE_AV_CONTROL|Command Class = COMMAND_CLASS_SIMPLE_AV_CONTROL|Command Class = COMMAND_CLASS_SIMPLE_AV_CONTROL|Command Class = COMMAND_CLASS_SIMPLE_AV_CONTROL|Command Class = COMMAND_CLASS_SIMPLE_AV_CONTROL|Command Class = COMMAND_CLASS_SIMPLE_AV_CONTROL|Command Class = COMMAND_CLASS_SIMPLE_AV_CONTROL|Command Class = COMMAND_CLASS_SIMPLE_AV_CONTROL|
|Command = SIMPLE_AV_CONTROL_SUPPORTED_REPORT|Command = SIMPLE_AV_CONTROL_SUPPORTED_REPORT|Command = SIMPLE_AV_CONTROL_SUPPORTED_REPORT|Command = SIMPLE_AV_CONTROL_SUPPORTED_REPORT|Command = SIMPLE_AV_CONTROL_SUPPORTED_REPORT|Command = SIMPLE_AV_CONTROL_SUPPORTED_REPORT|Command = SIMPLE_AV_CONTROL_SUPPORTED_REPORT|Command = SIMPLE_AV_CONTROL_SUPPORTED_REPORT|
|Report No|Report No|Report No|Report No|Report No|Report No|Report No|Report No|
|Bit Mask 1|Bit Mask 1|Bit Mask 1|Bit Mask 1|Bit Mask 1|Bit Mask 1|Bit Mask 1|Bit Mask 1|
|…|…|…|…|…|…|…|…|
|Bit Mask N|Bit Mask N|Bit Mask N|Bit Mask N|Bit Mask N|Bit Mask N|Bit Mask N|Bit Mask N|



**Report** **No** **(8** **bits)**

Report no. field specify the request report number.


**Bit** **Mask** **(N** **bytes)**

The Bit Mask fields describe the supported AV Control Commands by the device.


 - Bit 0 in Bit Mask 1 indicates if Command #1 is supported.


 - Bit 1 in Bit Mask 1 indicates if Command #2 is supported.


 - …


If a Command is supported, the bit MUST be set to 1. If a Command is not supported, the bit MUST
be set to 0. It is only necessary to send the Bit Mask fields from 1 and up to the one indicating the
last supported Command #. Mask fields bigger than 45 bytes not allowed. The number of Bit Mask
fields transmitted MUST be determined from the length field in the frame.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 465